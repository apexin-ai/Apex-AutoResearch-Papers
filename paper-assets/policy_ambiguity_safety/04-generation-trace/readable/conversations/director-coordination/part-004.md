# Director coordination — Part 4 of 11

**Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on Customer-Service Agent Safety** · Conversation logs

[← Part 3](part-003.md) · [Transcript overview](../director-coordination.md) · [Part 5 →](part-005.md) · [Structured JSON](../../../sessions/0e/0e806c5d99edfa05e2ae.json)

## Round 84

### Tool result

_source line 930 · 2026-05-22T08:33:17.396549+00:00_

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
…[truncated 2100 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 931 · 2026-05-22T08:33:17.396928+00:00_

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
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 932 · 2026-05-22T08:33:17.597878+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Ambiguity in NLP and requirements engineering.}
5	Ambiguity has been studied extensively in both computational linguistics and software engineering. Word sense disambiguation \citep{navigli_wsd_2009} addresses lexical ambiguity at the token level; our lexical type extends this to policy-specific polysemy. \citet{li_ambiguity_taxonomy_2024} propose an 11-type NLP taxonomy covering syntactic, semantic, and pragmatic ambiguity, from which we draw our linguistic-layer types. In requirements engineering (RE), \citet{massey_ambiguity_re_2014} classify six ambiguity types in regulatory texts, and \citet{berry_kamsties_2004} introduce the distinction between nocuous ambiguity (where stakeholders diverge on interpretation) and innocuous ambiguity (where they converge). Computational detection of nocuous ambiguity has progressed from heuristic methods \citep{chantree_2006,willis_nocuous_2008} through NLP-based cross-domain detectors \citep{ferrari_ambiguity_2019,ferrari_defects_2018} to transformer-based approaches for anaphoric ambiguity \citep{ezzini_taphsir_2022,ezzini_anaphoric_2022}. \citet{zhao_nlp4re_2021} survey the broader NLP4RE landscape. Our work extends Berry and Kamsties' framework to LLM agents, where the absence of shared organizational context makes previously innocuous ambiguity nocuous.
6	
7	\paragraph{Psycholinguistics of ambiguity processing.}
8	\citet{ferreira_good_enough_2002} show that human comprehenders build shallow, ``good-enough'' representations rather than full parses, paralleling our observation that LLM agents adopt surface interpretations. \citet{frazier_rayner_1982} demonstrate early commitment to a single parse; \citet{li_garden_path_llm_2024} provide direct evidence that LLMs exhibit analogous garden-path effects. \citet{liu_ambiguity_2023} demonstrate that language models fail to represent ambiguity, collapsing multiple interpretations into a single output. These findings
…[truncated 2470 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 200
}
```

</details>

---


### Tool call

_source line 933 · 2026-05-22T08:33:17.598307+00:00_

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
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/taxonomy.tex"
  }
}
```

</details>

---


### Tool result

_source line 934 · 2026-05-22T08:33:18.000033+00:00_

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
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 935 · 2026-05-22T08:33:18.000466+00:00_

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
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 936 · 2026-05-22T08:33:18.201693+00:00_

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
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 937 · 2026-05-22T08:33:18.202396+00:00_

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
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 938 · 2026-05-22T08:33:18.453973+00:00_

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
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 939 · 2026-05-22T08:33:18.454497+00:00_

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
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/analysis.tex"
  }
}
```

</details>

---


### Tool result

_source line 940 · 2026-05-22T08:33:18.655643+00:00_

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
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 941 · 2026-05-22T08:33:18.656136+00:00_

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
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 942 · 2026-05-22T08:33:18.857313+00:00_

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
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 943 · 2026-05-22T08:33:18.857680+00:00_

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
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 944 · 2026-05-22T08:33:19.259454+00:00_

1	\section{Conclusion}
2	
3	Ambiguous policy clauses increase agent safety violations by 34.0\,pp (OR\,$=$\,15.1) across five models, with clause identity explaining 22$\times$ more variance than model identity. Incompleteness consistently ranks highest across all seven models ($\geq$46\%), with rankings replicating in independent families ($\rho = 0.60$--$0.90$). With agents exhibiting disambiguation neglect in over 89\% of cases and 41.3\% of clauses triggering model-convergent violations, type-aware auditing and externalized detection are critical for policy-governed deployments.
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 945 · 2026-05-22T08:33:19.259827+00:00_

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
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 946 · 2026-05-22T08:33:19.460915+00:00_

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
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 947 · 2026-05-22T08:33:19.511606+00:00_

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
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 948 · 2026-05-22T08:33:19.562298+00:00_

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
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 949 · 2026-05-22T08:33:19.612878+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 950 · 2026-05-22T08:33:19.663499+00:00_

1	@inproceedings{li_ambiguity_taxonomy_2024,
2	  title={A Taxonomy of Ambiguity Types for {NLP}},
3	  author={Li, Margaret Y. and Liu, Alisa and Wu, Zhaofeng and Smith, Noah A.},
4	  booktitle={Proceedings of EACL 2024},
5	  year={2024}
6	}
7	
8	@inproceedings{massey_ambiguity_re_2014,
9	  title={Identifying and Classifying Ambiguity for Regulatory Requirements},
10	  author={Massey, Aaron K. and Rutledge, Richard L. and Ant{\'o}n, Annie I. and Swire, Peter P.},
11	  booktitle={22nd IEEE International Requirements Engineering Conference (RE)},
12	  year={2014},
13	  doi={10.1109/RE.2014.6912250}
14	}
15	
16	@techreport{berry_kamsties_2004,
17	  title={From Contract Drafting to Software Specification: Linguistic Sources of Ambiguity --- A Handbook},
18	  author={Berry, Daniel M. and Kamsties, Erik and Krieger, Michael M.},
19	  institution={University of Waterloo},
20	  year={2004}
21	}
22	
23	@inproceedings{chantree_2006,
24	  title={Identifying Nocuous Ambiguities in Natural Language Requirements},
25	  author={Chantree, Francis and Nuseibeh, Bashar and de Roeck, Anne and Willis, Alistair},
26	  booktitle={14th IEEE International Requirements Engineering Conference (RE)},
27	  year={2006}
28	}
29	
30	@incollection{wasow_ambiguity_2005,
31	  title={The Puzzle of Ambiguity},
32	  author={Wasow, Thomas and Perfors, Amy and Beaver, David},
33	  booktitle={Morphology and the Web of Grammar: Essays in Memory of Steven G. Lapointe},
34	  publisher={CSLI Publications},
35	  year={2005}
36	}
37	
38	@article{kennedy_vagueness_2007,
39	  title={Vagueness and Grammar: The Semantics of Relative and Absolute Gradable Adjectives},
40	  author={Kennedy, Christopher},
41	  journal={Linguistics and Philosophy},
42	  volume={30},
43	  number={1},
44	  pages={1--45},
45	  year={2007},
46	  doi={10.1007/s10988-006-9008-0}
47	}
48	
49	@article{willis_nocuous_2008,
50	  title={Automatic Identification of Nocuous Ambiguity},
51	  author={Willis, Alistair and Chantree, Francis and De Roeck
…[truncated 12362 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 951 · 2026-05-22T08:37:15.345615+00:00_

&lt;persisted-output>
Output too large (73.4KB). Full output saved to: /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0519-4-projects-policy-ambiguity-safety--claude-sessions-review-director-0e80b40a/ab3595f5-7d08-429d-9fc2-83ffd92b8145/tool-results/toolu_014TByB9AfieLcQuXhVZe4GG.json

Preview (first 2KB):
[
  {
    "type": "text",
    "text": "I have successfully read all 12 requested files. Here is the FULL content of each file:\n\n---\n\n## File 1: abstract.tex\n\n```latex\n\\begin{abstract}\nLLM-based agents operate under natural-language policy specifications that inevitably contain ambiguity, yet the causal relationship between ambiguity type and safety violations remains unmeasured. We present a matched-pair study on $\\tau^2$-bench with 300 clause pairs spanning a six-type ambiguity taxonomy, evaluated across five models (2,997 episodes). Three findings emerge. First, ambiguous clauses increase violation rates by 34.0 percentage points (OR $= 15.1$), with a perturbation control supporting ambiguity-specific causation. Second, incompleteness consistently ranks highest (46--62\\% across seven models); the remaining five types show a risk gradient rather than sharp tiers. Third, error analysis of 614 violation traces reveals \\emph{Disambiguation Neglect} ($\\leq$11\\% awareness) and \\emph{systematic nocuity}---41.3\\% of clauses triggering model-convergent violations---indicating clause-level rather than model-level risk factors. These results motivate type-aware policy auditing and externalized ambiguity detection for policy-governed agent deployments.\n\\end{abstract}\n```\n\n---\n\n## File 2: introduction.tex\n\n```latex\n\\section{Introduction}\n\\label{sec:introduction}\n\nA customer asks to return a customized item within the 30-day window. The agent consults the store policy, which states that ``items may be returned within 30 days.'' The word ``items'' scopes over all product categories, including custom orders that a
…[truncated 366 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Agent",
  "elapsed_ms": 240362
}
```

</details>

---


### Tool call

_source line 952 · 2026-05-22T08:37:27.541571+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0519-4-projects-policy-ambiguity-safety--claude-sessions-review-director-0e80b40a/ab3595f5-7d08-429d-9fc2-83ffd92b8145/tool-results/toolu_014TByB9AfieLcQuXhVZe4GG.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0519-4-projects-policy-ambiguity-safety--claude-sessions-review-director-0e80b40a/ab3595f5-7d08-429d-9fc2-83ffd92b8145/tool-results/toolu_014TByB9AfieLcQuXhVZe4GG.json"
  }
}
```

</details>

---


### Tool result

_source line 953 · 2026-05-22T08:37:27.944243+00:00_

1	[
2	  {
3	    "type": "text",
4	    "text": "I have successfully read all 12 requested files. Here is the FULL content of each file:\n\n---\n\n## File 1: abstract.tex\n\n```latex\n\\begin{abstract}\nLLM-based agents operate under natural-language policy specifications that inevitably contain ambiguity, yet the causal relationship between ambiguity type and safety violations remains unmeasured. We present a matched-pair study on $\\tau^2$-bench with 300 clause pairs spanning a six-type ambiguity taxonomy, evaluated across five models (2,997 episodes). Three findings emerge. First, ambiguous clauses increase violation rates by 34.0 percentage points (OR $= 15.1$), with a perturbation control supporting ambiguity-specific causation. Second, incompleteness consistently ranks highest (46--62\\% across seven models); the remaining five types show a risk gradient rather than sharp tiers. Third, error analysis of 614 violation traces reveals \\emph{Disambiguation Neglect} ($\\leq$11\\% awareness) and \\emph{systematic nocuity}---41.3\\% of clauses triggering model-convergent violations---indicating clause-level rather than model-level risk factors. These results motivate type-aware policy auditing and externalized ambiguity detection for policy-governed agent deployments.\n\\end{abstract}\n```\n\n---\n\n## File 2: introduction.tex\n\n```latex\n\\section{Introduction}\n\\label{sec:introduction}\n\nA customer asks to return a customized item within the 30-day window. The agent consults the store policy, which states that ``items may be returned within 30 days.'' The word ``items'' scopes over all product categories, including custom orders that are normally final sale. The agent grants a full refund and arranges free return shipping. One word of scopal ambiguity costs the retailer \\$200.\n\nLLM-based agents increasingly operate under natural-language policy specifications that govern their permitted actions. These specifications inevitably contain ambiguity: a property tha
…[truncated 73150 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 954 · 2026-05-22T08:37:44.908374+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "policy_ambiguity_safety",
  "file": "decisions.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "policy_ambiguity_safety",
    "file": "decisions.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 955 · 2026-05-22T08:37:45.310488+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/decisions.yaml\", \"content\": \"_next_id: 27\\ndecisions:\\n- id: D001\\n  date: 2026-05-20 07:11 UTC\\n  summary: MVP 设计：3 类歧义 × 2 API 模型验证 type effect，不用 GPU\\n  rationale: 核心假设是\\\"歧义类型影响安全违规率\\\"。选 scopal/lexical/incompleteness 3 种假设差异最大的类型，用 frontier\\n    API 模型（免 GPU）快速验证信号存在性。60 条款 × 2 variants × 2 模型 = 240 runs，统计功效足够（χ² df=2, medium\\n    effect w=0.3, N=240 >> 所需 ~107）。Pass 条件：p<0.05 + V≥0.15。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-20 07:15 UTC\\n  summary: 采纳 Reviewer 3 条修正：增条款数、调阈值、补 fail path\\n  rationale: 'Reviewer WARNING: (1) pairwise N=80 对 V=0.15 功效仅 0.22，增至 30 条款/类（pairwise\\n    N=120）+ 提阈值至 V≥0.20 + 明确 MVP 只检测 medium+ effect；(2) 补 fail path 三级决策树（扩大N重测 →\\n    pivot binary story → full study）；(3) 加 judge 偏差检查点（scopal 低于预期时先排查 judge bias）。'\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-20 07:16 UTC\\n  summary: ROADMAP 补充 H1-H4 预测基准和 post-MVP 18 周路径骨架\\n  rationale: 'Reviewer WARNING: (1) ROADMAP 缺 post-MVP 骨架，ICLR DDL 18 周后，需提前规划 GPU\\n    申请时间点（W3 MVP pass 后立即申请，W5 开始 Phase 2b）；(2) H1-H4 方向性预测未落地到 ROADMAP，Agent 解读 MVP\\n    结果时需对照基准（H1: scopal 最高，H2: lexical 最低，null: binary effect story）。paper_framing.md\\n    保持在 MVP 后创建。'\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n  - D002\\n- id: D004\\n  date: 2026-05-20 07:23 UTC\\n  summary: MVP 分析改为双轨：ambiguous-only 跨类型比较（主）+ matched-pair within-type（辅）\\n  rationale: 'Reviewer WARNING: incompleteness matched pair 存在信息量不对称混淆——消歧必然添加信息，与\\n    scopal/lexical 的\\\"同信息不同措辞\\\"baseline 不可比。解法：(1) 主分析用 ambiguous-only 条件直接跨类型比较违规率（不受信息量混淆）；(2)\\n    matched-pair 降为辅助的 within-type 效应量度量；(3) 要求 Agent 修订 incompleteness pairs 只添加解决歧义的最小信息；(4)\\n    效度边界显式声明此不对称性。'\\n  related_experiments: []\\n  depends_on:\\n  - D002\\n- id: D005\\n  date: 2026-05-20 07:24 UTC\\n  summary: MVP 使用 τ²-
…[truncated 1453 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 956 · 2026-05-22T08:37:45.310995+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ARR 2026 May cycle submission format guidelines page limit anonymity"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ARR 2026 May cycle submission format guidelines page limit anonymity"
  }
}
```

</details>

---


### Tool result

_source line 957 · 2026-05-22T08:37:51.689881+00:00_

Web search results for query: "ARR 2026 May cycle submission format guidelines page limit anonymity"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Authors Guidelines","url":"http://aclrollingreview.org/authors"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"ARR Reviewer Guidelines","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ACL Policies for Review and Citation - Admin Wiki","url":"https://www.aclweb.org/adminwiki/index.php/ACL_Policies_for_Review_and_Citation"},{"title":"How ARR works – ACL Rolling Review","url":"http://aclrollingreview.org/reviewing"}]

Based on the search results, here are the key submission format guidelines and requirements for ARR 2026 May cycle submissions:

## Page Limit

All ARR submissions are anonymous and in the format of a short paper (up to 4 pages) or long paper (up to 8 pages).

## Anonymity Requirements

Papers must not include authors' names and affiliations. Furthermore, self-references that reveal the authors' identities, e.g., "We previously showed (Smith, 1991)…" must be avoided.

Supplementary materials, including any links to repositories, should also be anonymized. Links to file hosting services that can track downloads, such as Dropbox, are not allowed.

## Anonymity Policy

Beginning with the February 15, 2024 ARR deadlines, there is no anonymity period or limitation o
…[truncated 590 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "WebSearch",
  "elapsed_ms": 6378
}
```

</details>

---


### Tool call

_source line 958 · 2026-05-22T08:37:56.559350+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review|paperreview_ai",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review|paperreview_ai",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 959 · 2026-05-22T08:37:56.610372+00:00_

&lt;persisted-output>
Output too large (28.7KB). Full output saved to: /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0519-4-projects-policy-ambiguity-safety--claude-sessions-review-director-0e80b40a/ab3595f5-7d08-429d-9fc2-83ffd92b8145/tool-results/toolu_01Nre3aJZBgKYbYxoW9tizqQ.txt

Preview (first 2KB):
AGENTS.md:82:如果项目配置了外部审稿（`external_review.paperreview_ai.enabled: true`）：
AGENTS.md:83:- 在分配内部 Reviewer 的同时，调用 `request_external_review()` 向用户群发送协助卡片
AGENTS.md:87:- 如果内部审稿结束时外部结果仍未返回，用 `get_external_review_status()` 检查状态，在报告中标注「外部审稿：未返回」
AGENTS.md:163:`director_get_project_overview`, `director_post_to_reviewer`, `dispatch_visual_check`, `get_external_review_status`, `get_visual_check_status`, `read_local_file`, `read_project_file`, `request_external_review`, `request_study_approval`, `submit_review_report_to_research_director`, `update_review_issues`
CLAUDE.md:82:如果项目配置了外部审稿（`external_review.paperreview_ai.enabled: true`）：
CLAUDE.md:83:- 在分配内部 Reviewer 的同时，调用 `request_external_review()` 向用户群发送协助卡片
CLAUDE.md:87:- 如果内部审稿结束时外部结果仍未返回，用 `get_external_review_status()` 检查状态，在报告中标注「外部审稿：未返回」
CLAUDE.md:163:`director_get_project_overview`, `director_post_to_reviewer`, `dispatch_visual_check`, `get_external_review_status`, `get_visual_check_status`, `read_local_file`, `read_project_file`, `request_external_review`, `request_study_approval`, `submit_review_report_to_research_director`, `update_review_issues`
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/logs/chats/archive/feishu_group_oc_10fa2e89afc5e9b8a13613245e008dd9_director_20260522T002209_609865.jsonl:71:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/logs/chats/archive/feishu_group_oc_10fa2e89afc5e9b8a13613245e008dd9_director_20260522T002209_609865.jsonl:318:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review
…[truncated 288 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Grep",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 960 · 2026-05-22T08:38:18.239930+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "policy_ambiguity_safety",
  "review_chat_id": "oc_967344d166ba485ad606d14379e69d85"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "policy_ambiguity_safety",
    "review_chat_id": "oc_967344d166ba485ad606d14379e69d85"
  }
}
```

</details>

---


### Tool result

_source line 961 · 2026-05-22T08:38:36.363918+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 18123
}
```

</details>

---


### Tool call

_source line 962 · 2026-05-22T08:38:37.317737+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "text": "你是 Reviewer 1，负责**方法严谨性**审查。\n\n## 论文信息\n- **标题**: \"Not All Policy Ambiguity Is Equal: Type-Specific Safety Risks for LLM Agents\"\n- **论文路径**: `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_11/submitted.pdf`\n\n## Venue 要求\n- **EMNLP 2026** via ARR May cycle\n- Long paper: 正文 **8 页**限制, 参考文献不限\n- Mandatory limitations 和 optional ethical considerations 不计入页数（前提是不含过多额外内容）\n- **Double-blind** 匿名审稿\n- ACL 模板 (`\\usepackage[review]{acl}`)\n- Overall Assessment 评分标准: 5=Consider for Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1=Do not resubmit\n\n## 你的审查侧重\n\n**方法严谨性**，重点关注以下方面：\n\n1. **因果推断设计**: matched-pair design 的有效性，perturbation control 的充分性，是否满足因果推断的标准假设\n2. **统计分析**: McNemar test、TOST equivalence testing、bootstrap cluster analysis 的选择是否恰当，多重比较校正是否充分，SESOI ±15pp 的合理性\n3. **评估流程**: cross-judge 设计的偏差分析，per-type judge reliability（特别是 authorization scope κ=0.385），human validation 样本量是否充分\n4. **控制变量**: incompleteness 的 information-addition confound 处理，句长差异（d=0.74）的控制，clause pair 构建的严谨性\n5. **可重复性**: ICC=0.919 仅覆盖 OpenAI 家族的局限性，replication 设计的充分性\n6. **效应量解释**: C1-C4 各 claim 的证据强度与表述匹配度，特别是 C2（two-tier hierarchy）和 C4（52pp range）的表述是否过强\n\n请按以下格式输出审稿意见：\n\n### Strengths (S1, S2, ...)\n### Weaknesses (W1, W2, ... — 标注 MUST-FIX / SHOULD-FIX / MINOR)\n### Questions (Q1, Q2, ...)\n### Missing References\n### Overall Assessment (评分 + 置信度 + 1-2 句总评)",
  "project": "policy_ambiguity_safety",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "text": "你是 Reviewer 1，负责**方法严谨性**审查。\n\n## 论文信息\n- **标题**: \"Not All Policy Ambiguity Is Equal: Type-Specific Safety Risks for LLM Agents\"\n- **论文路径**: `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_11/submitted.pdf`\n\n## Venue 要求\n- **EMNLP 2026** via ARR May cycle\n- Long paper: 正文 **8 页**限制, 参考文献不限\n- Mandatory limitations 和 optional ethical considerations 不计入页数（前提是不含过多额外内容）\n- **Double-blind** 匿名审稿\n- ACL 模板 (`\\usepackage[review]{acl}`)\n- Overall Assessment 评分标准: 5=Consider for Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1=Do not resubmit\n\n## 你的审查侧重\n\n**方法严谨性**，重点关注以下方面：\n\n1. **因果推断设计**: matched-pair design 的有效性，perturbation control 的充分性，是否满足因果推断的标准假设\n2. **统计分析**: McNemar test、TOST equivalence testing、bootstrap cluster analysis 的选择是否恰当，多重比较校正是否充分，SESOI ±15pp 的合理性\n3. **评估流程**: cross-judge 设计的偏差分析，per-type judge reliability（特别是 authorization scope κ=0.385），human validation 样本量是否充分\n4. **控制变量**: incompleteness 的 information-addition confound 处理，句长差异（d=0.74）的控制，clause pair 构建的严谨性\n5. **可重复性**: ICC=0.919 仅覆盖 OpenAI 家族的局限性，replication 设计的充分性\n6. **效应量解释**: C1-C4 各 claim 的证据强度与表述匹配度，特别是 C2（two-tier hierarchy）和 C4（52pp range）的表述是否过强\n\n请按以下格式输出审稿意见：\n\n### Strengths (S1, S2, ...)\n### Weaknesses (W1, W2, ... — 标注 MUST-FIX / SHOULD-FIX / MINOR)\n### Questions (Q1, Q2, ...)\n### Missing References\n### Overall Assessment (评分 + 置信度 + 1-2 句总评)",
    "project": "policy_ambiguity_safety",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 963 · 2026-05-22T08:38:51.686938+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 14369
}
```

</details>

---


### Tool call

_source line 964 · 2026-05-22T08:38:51.837882+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "text": "你是 Reviewer 2，负责**新颖性与完整性**审查。\n\n## 论文信息\n- **标题**: \"Not All Policy Ambiguity Is Equal: Type-Specific Safety Risks for LLM Agents\"\n- **论文路径**: `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_11/submitted.pdf`\n\n## Venue 要求\n- **EMNLP 2026** via ARR May cycle\n- Long paper: 正文 **8 页**限制, 参考文献不限\n- Mandatory limitations 和 optional ethical considerations 不计入页数（前提是不含过多额外内容）\n- **Double-blind** 匿名审稿\n- ACL 模板 (`\\usepackage[review]{acl}`)\n- Overall Assessment 评分标准: 5=Consider for Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1=Do not resubmit\n\n## 你的审查侧重\n\n**新颖性与完整性**，重点关注以下方面：\n\n1. **贡献新颖性**: 三个 contribution 的增量贡献是否真正新颖——matched-pair causal design 在 NLP 安全领域的创新度，相比 DRIP-R/PolicyBank/AgentPex 等 concurrent work 的差异化\n2. **Taxonomy 理论基础**: 六类型 taxonomy 的理论严谨性——incompleteness（information absence）和 conditional precedence（normative conflict）是否真正属于 ambiguity？§3 \"Scope of ambiguity\" 段落是否充分回应了这一理论张力\n3. **Framing 一致性**: Abstract/Introduction/Conclusion 中的 claim 表述是否与正文证据匹配——特别关注 \"two-tier hierarchy\"、\"52pp range\"、\"Disambiguation Neglect\" 等核心术语的精确度\n4. **Related Work 覆盖度**: 是否遗漏重要相关工作，特别是 RE 领域的 ambiguity detection、psycholinguistics of LLM processing、agent safety 的最新进展\n5. **写作质量**: 逻辑流畅度、术语一致性、是否有冗余或遗漏、references.bib 的准确性\n6. **格式合规**: 是否符合 EMNLP 2026 / ARR 格式要求（8 页限制、匿名性、引用格式等）\n7. **Differential Nocuity 和 Disambiguation Neglect**: 这些框架/术语是否为真正的新贡献，还是已有概念的 domain transfer？表述是否过度\n\n请按以下格式输出审稿意见：\n\n### Strengths (S1, S2, ...)\n### Weaknesses (W1, W2, ... — 标注 MUST-FIX / SHOULD-FIX / MINOR)\n### Questions (Q1, Q2, ...)\n### Missing References\n### Overall Assessment (评分 + 置信度 + 1-2 句总评)",
  "project": "policy_ambiguity_safety",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "text": "你是 Reviewer 2，负责**新颖性与完整性**审查。\n\n## 论文信息\n- **标题**: \"Not All Policy Ambiguity Is Equal: Type-Specific Safety Risks for LLM Agents\"\n- **论文路径**: `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_11/submitted.pdf`\n\n## Venue 要求\n- **EMNLP 2026** via ARR May cycle\n- Long paper: 正文 **8 页**限制, 参考文献不限\n- Mandatory limitations 和 optional ethical considerations 不计入页数（前提是不含过多额外内容）\n- **Double-blind** 匿名审稿\n- ACL 模板 (`\\usepackage[review]{acl}`)\n- Overall Assessment 评分标准: 5=Consider for Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1=Do not resubmit\n\n## 你的审查侧重\n\n**新颖性与完整性**，重点关注以下方面：\n\n1. **贡献新颖性**: 三个 contribution 的增量贡献是否真正新颖——matched-pair causal design 在 NLP 安全领域的创新度，相比 DRIP-R/PolicyBank/AgentPex 等 concurrent work 的差异化\n2. **Taxonomy 理论基础**: 六类型 taxonomy 的理论严谨性——incompleteness（information absence）和 conditional precedence（normative conflict）是否真正属于 ambiguity？§3 \"Scope of ambiguity\" 段落是否充分回应了这一理论张力\n3. **Framing 一致性**: Abstract/Introduction/Conclusion 中的 claim 表述是否与正文证据匹配——特别关注 \"two-tier hierarchy\"、\"52pp range\"、\"Disambiguation Neglect\" 等核心术语的精确度\n4. **Related Work 覆盖度**: 是否遗漏重要相关工作，特别是 RE 领域的 ambiguity detection、psycholinguistics of LLM processing、agent safety 的最新进展\n5. **写作质量**: 逻辑流畅度、术语一致性、是否有冗余或遗漏、references.bib 的准确性\n6. **格式合规**: 是否符合 EMNLP 2026 / ARR 格式要求（8 页限制、匿名性、引用格式等）\n7. **Differential Nocuity 和 Disambiguation Neglect**: 这些框架/术语是否为真正的新贡献，还是已有概念的 domain transfer？表述是否过度\n\n请按以下格式输出审稿意见：\n\n### Strengths (S1, S2, ...)\n### Weaknesses (W1, W2, ... — 标注 MUST-FIX / SHOULD-FIX / MINOR)\n### Questions (Q1, Q2, ...)\n### Missing References\n### Overall Assessment (评分 + 置信度 + 1-2 句总评)",
    "project": "policy_ambiguity_safety",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 965 · 2026-05-22T08:38:53.605336+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1767
}
```

</details>

---


### Assistant

_source line 966 · 2026-05-22T08:39:08.872301+00:00_

Round 1 任务已全部派发：

- **视觉审查 Agent**: 已启动（fire-and-forget）
- **Reviewer 1**（方法严谨性）: 已分配
- **Reviewer 2**（新颖性/完整性）: 已分配

等待两位 Reviewer 返回独立初审意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 85

## Round 85

2 recorded events


### User

_source line 967 · 2026-05-22T08:44:05.075314+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 审稿意见（新颖性与完整性）

### 论文信息
- **标题**: "Not All Policy Ambiguity Is Equal: Type-Specific Safety Risks for LLM Agents"
- **Venue**: EMNLP 2026 via ARR

---

## 总体评分
**Overall**: 3.5 (Borderline Conference)
**一句话总结**: 实验设计扎实（matched-pair causal design 在该领域确属首创），但核心 taxonomy 的理论基础存在张力，多个 coined terms 的增量贡献被高估，authorization scope 的测量可靠性问题未在摘要/引言中充分反映。

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 方法论整体严谨（perturbation control, TOST, bootstrap cluster），但 incompleteness 作为 "ambiguity" 的理论论证循环，auth scope κ=0.385 削弱 C4；claim calibration 做得不错但仍有 overclaiming |
| Excitement | 3.5/5 | 首次建立 ambiguity type → safety violation 的因果映射，有部署价值；但 "Differential Nocuity" 和 "Disambiguation Neglect" 的新颖性不如 framing 所暗示的那么高 |
| Reproducibility | 4/5 | 承诺开源数据和代码；统计方法描述充分；API 调用参数明确 |
| Reviewer Confidence | 4/5 | 熟悉 RE ambiguity 文献、NLP safety benchmarks 和统计方法论 |

---

### Strengths

**S1. Matched-pair causal design 确属创新。** 在 NLP agent safety 领域，现有工作（DRIP-R、PolicyBank、AgentPex）均为 correlational 或 benchmark-evaluation 范式。本文的 matched-pair design + perturbation control（§4.6, Δ_perturb = −0.67pp, CI containing zero）确实建立了 ambiguity → violation 的因果链，这是对 concurrent work 的有意义差异化（§2 Related Work 中对 DRIP-R 的三点区分清晰且准确）。

**S2. 统计方法论异常充分。** TOST equivalence testing + sensitivity across 7 margins (Appendix A) + margin-free bootstrap cluster analysis (Appendix I) 三重验证 type hierarchy，避免了仅依赖 NHST 的问题。Holm-Bonferroni 家族校正、ICC reproducibility (0.919)、cross-judge calibration (McNemar p=0.606) 均达到高标准。对 SESOI=±15pp 的 domain-anchored justification (§4.6) 和 margin dependence 的 acknowledgment 体现方法论自觉。

**S3. Honest about limitations。** Incompleteness confound 的多层控制（token delta logistic regression, coreferential lower bound, sans-incompleteness analysis），C3 null result 的坦诚报告，auth scope κ=0.385 的反复标注（§4.4, §5.4, §Limitations），这些都是正面的。C4 标记为 [Exploratory] 也是恰当的。

**S4. Error analysis 有实质洞见。** 三种 failure mechanism（structural misparse, information gap-filling, boundary violation）与 ambiguity type 的对应关系（§6.1）提供了超越聚合统计的机制理解。Systematic nocuity（41.3% majority-convergent violations）揭示了 agreement-based evaluation 的盲区。

**S5. 实验规模与模型覆盖度。** 5 primary + 2 replication models, 7 providers, 2997 episodes, 跨 proprietary/open-source/dense/MoE 架构。Replication 在独立 model families 上确认 C1 和 C2 是强有力的。

---

### Weaknesses

**W1 [SHOULD-FIX] Taxonomy 理论基础：incompleteness 和 conditional precedence 并非 "ambiguity"，§3 "Scope of ambiguity" 的论证存在循环。**

§3 最后一段承认 incompleteness 涉及 "absent information rather than multiple readings"，conditional precedence 涉及 "normative conflict rather than interpretive uncertainty"，但论证其纳入的理由是 "LLM agents process all six types identically—committing to a single interpretation without flagging uncertainty—and the resulting safety violations are behaviorally indistinguishable (§5)"。这是循环论证：先将这些类型纳入 taxonomy → 在 benchmark 中测试 → 观察到相似的 violation pattern → 用此证明纳入的合理性。

更根本的问题是：incompleteness 是该 taxonomy 中 violation rate 最高的类型（53.6%），也是论文多个核心 claim 的关键支撑。如果该类型在理论上不属于 ambiguity，那论文的中心叙事——"ambiguity type predicts safety violations"——就被削弱了。Dalpiaz et al. (2018) 被引用来支持 "ambiguity and incompleteness frequently co-occur"，但 co-occurrence 不等于 identity。

建议：(a) 将 taxonomy 重新框架为 "policy specification defects" 而非 "ambiguity types"，或 (b) 在 §3 中增加更实质的理论论证，例如引用 Ferrari et al. (2019) "Ambiguity in RE: Towards a Unifying Framework" 中对 ambiguity 更广义操作化定义的讨论。

**W2 [SHOULD-FIX] "Disambiguation Neglect" 的新颖性被高估。**

论文将 Disambiguation Neglect 列为三大 contribution 之一（§1 contribution (3)），但：
- Liu et al. (2023, EMNLP) 已证明 LLMs "collapse multiple interpretations into a single output"
- Hu et al. (2025) 进一步论证 LLM ambiguity 反映 "missing conceptual representations"
- 论文自己在 §2 中引用了这两篇并承认了联系

本文的增量贡献在于在 agent policy 场景中量化了这一现象（≤11% awareness）并与 safety violation 关联。但将已有充分文献记录的现象 coin 成新术语并列为 primary contribution 是 overclaiming。

建议：重新定位为 "在 agent policy 场景中对已知现象的首次量化"，降低 contribution statement 中的权重。

**W3 [SHOULD-FIX] "Differential Nocuity" 框架的增量贡献有限。**

Berry & Kamsties (2004) 的 nocuous/innocuous 二分法已隐含了 type-dependent risk 的思想。Willis et al. (2008) 已经研究了 nocuity 的 degree 和 contextual factors。本文的具体贡献是提供了 empirical evidence（6 types × 5 models 的 violation rate matrix），但 "differential nocuity" 作为 framework name 过于宏大。

建议：降低 framing，呈现为 empirical finding 而非 theoretical framework。

**W4 [SHOULD-FIX] Abstract/Introduction 中的 claim 精确度与正文证据不完全匹配。**

(a) Abstract 说 "remaining five types show a risk gradient rather than sharp tiers"，但 §5.2 的 TOST 分析给出 "two-tier structure"，bootstrap AU p-value = 0.47 表明分区不稳定。"risk gradient" 和 "two-tier" 是不同表述。

(b) Introduction 中 "authorization scope shows the widest cross-model range (52pp)" 的 caveat 位置和权重不够——κ < 0.4 的测量维度上的 52pp range 不应作为核心 finding 突出。

(c) Contribution (2) 说 "type identity explaining 22× more variance than model identity"，但 §5.1 说的是 "Clause identity explains 22.4% of variance"。Clause identity ≠ type identity，表述有误导性。

**W5 [MINOR] Related Work 遗漏若干相关工作。**
- OpenAgentSafety (ICLR 2026) — comprehensive agent safety framework
- Agent-SafetyBench (2024) — 349 interactive environment agent safety benchmark  
- Ferrari et al. (2019) "Ambiguity in RE: Towards a Unifying Framework" — 与 taxonomy 理论基础直接相关
- Automated Repair of Ambiguous NL Requirements (2025, arxiv:2505.07270)

**W6 [MINOR] Coreferential ambiguity 在 mitigation 和 replication 实验中均被排除，削弱了 taxonomy 的完整性。**

Appendix B 解释了排除原因，可以理解。但 taxonomy 声称 6 types 而两个重要实验只覆盖 5 types。Limitations 中未提及此点。

**W7 [MINOR] §7 Prompt-based mitigation 的样本量偏小。**

n=50 per type 的 McNemar test 功效有限。Incompleteness worsening (+14pp, p=0.118) 被解释为 "confabulation rather than caution"，但 p > 0.1 时因果解释过于确定。

---

### Questions

**Q1.** Bootstrap cluster 中 incompleteness singleton 的 AU p-value = 0.47，仅略高于 chance。这与 "incompleteness stands apart as an upper bound" 的 confident framing 如何调和？

**Q2.** "Clause identity explains 22.4% of variance"——这里的 clause identity 是 300 个 clause pair 的 random effect 还是 6 个 type 的 fixed effect？如果是前者，主要反映 clause-level heterogeneity 而非 type-level 解释力。

**Q3.** Temperature=0 下 ICC=0.919 的 reproducibility 中的变异来自哪里？API non-determinism 还是 episode-level randomness？

**Q4.** §4.2 的 "realism validation" 具体 protocol 是什么？是否与真实 policy documents 做了 distributional 对比？

---

### Overall Assessment

**评分: 3.5 / 5 (Borderline Conference) | 置信度: 4 / 5**

方法论扎实的实证论文，matched-pair causal design 在 NLP agent safety 领域确属首创，统计分析充分度远超该子领域平均水平。核心发现有部署价值。

主要顾虑在于 novelty 和 framing 的 calibration：(1) taxonomy 中 2/6 类型在理论上不属于 ambiguity 但贡献了最大效应量，(2) coined terms 的增量贡献被高估——它们是已有概念的 domain application 而非独立理论创新，(3) 部分 claim 精确度需校准（clause vs type identity、gradient vs two-tier、52pp range 的 caveat 权重）。这些问题非 fatal，但需在 revision 中认真处理。如果 framing 调整到位（降低 terminology novelty claim，强化 empirical contribution 本身），可以达到 4.0。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 968 · 2026-05-22T08:44:18.620472+00:00_

Reviewer 2 审稿意见已收到。评分 3.5（Borderline Conference），主要关注 taxonomy 理论基础、coined terms 新颖性高估、claim 精确度校准。

等待 Reviewer 1（方法严谨性）返回后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 86

## Round 86

2 recorded events


### User

_source line 969 · 2026-05-22T08:44:21.340379+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

**审稿摘要**：评分 3.5（Borderline Conference），置信度 4/5。

核心判断：
- **方法论是本文最大亮点**——matched-pair causal design + perturbation control 在该领域首创，统计分析（TOST + bootstrap cluster + Holm-Bonferroni）异常充分
- **主要顾虑集中在 novelty framing**：(1) incompleteness/conditional precedence 在理论上不属于 ambiguity，但贡献了最大效应量，§3 的论证存在循环；(2) "Differential Nocuity" 和 "Disambiguation Neglect" 这两个 coined terms 本质是已有概念的 domain application，不应列为 primary contribution；(3) Abstract/Introduction 中若干 claim 的精确度与正文证据不完全匹配（clause identity vs type identity 的 22× claim、gradient vs two-tier 表述不一致、52pp range 的 caveat 权重不足）
- **如果 revision 中调整 framing**（降低术语创新 claim，强化实证贡献本身），可升至 4.0

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 970 · 2026-05-22T08:44:28.954388+00:00_

Reviewer 2 意见已收到。等待 Reviewer 1 提交后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 87

## Round 87

6 recorded events


### User

_source line 971 · 2026-05-22T08:46:40.725134+00:00_

[Reviewer 1 审稿意见]:
## 总体评分
**Overall**: 3.5 / 5 (Borderline Conference)
**Confidence**: 4 / 5
**一句话总结**: 实验设计严谨、统计分析全面的因果研究，但 authorization scope 评审一致性低（κ=0.385）削弱了 C4，SESOI ±15pp 缺乏实质性论证，incompleteness 信息添加混杂虽有控制但残余问题影响 C2 的"两层结构"表述强度。

## 官方维度打分（ACL ARR Review Form）
| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | C1 证据充分（OR=15.1, 7 模型一致），C2 的两层结构依赖 margin 选择且 bootstrap AU p=0.47，C3 作者自认 inconclusive（正确），C4 基于最低可靠性类型的数据 |
| Excitement | 3.5/5 | 首个因果性的 ambiguity→violation 类型映射，taxonomy 桥接 NLP/RE，实用价值高；但局限于 τ²-bench 单一客服领域 |
| Reproducibility | 4/5 | 方法细节完整，承诺代码和数据开源，统计报告规范（效应量+CI+多重校正）；judge 选择限制精确复制 |

---

### Strengths

**S1: 严谨的 matched-pair 因果设计 + perturbation control**
300 对 clause pair（96% annotator agreement），perturbation control（Δ_perturb = −0.67pp, 95% CI [−8.0, 6.67] 包含零）有效排除了表面扰动的混杂效应。Section 4.2 和 4.5 的设计使得 C1 的因果推断具有说服力。

**S2: 全面的统计分析框架**
McNemar + TOST + bootstrap 聚类 + Holm-Bonferroni 三组校正 + post-hoc 功效分析（C1/C2 power > 0.99），同时在 7 个 margin（±5–20pp）上展示 TOST 敏感性分析（Table 3/Appendix A），这在该领域中不常见且值得肯定。

**S3: 诚实的 claim 标定**
C3 明确标注为 inconclusive（未通过 Holm-Bonferroni 校正），C4 标注为 [Exploratory]，authorization scope 的 52pp range 被表述为"suggestive rather than definitive"和"upper bound with substantial measurement uncertainty"（Section 5.4）。这种自我校准的 claim 强度在审稿中非常难得。

**S4: 有价值的 error analysis**
Section 6 的五种 failure mode taxonomy（structural misparse / information gap-filling / boundary violation）揭示了类型特异的机制路径，"Disambiguation Neglect"（4.6% awareness rate）是一个有实际意义的发现，且 mitigation experiment 证实了 prompt-level 干预的局限性。

**S5: Incompleteness 混杂处理相对充分**
Appendix F/H 提供了 token delta logistic regression（incompleteness p=0.018, coefficient change <8%），coreferential 的 confound-free lower bound（31.6%），以及 authorization scope 的反证逻辑（最大 token delta 但 violation rate 更低）。虽有残余问题（见 W2），整体处理水平高于同类论文。

---

### Weaknesses

**W1 [MUST-FIX]: Authorization scope cross-judge κ=0.385 严重削弱 C4 的 52pp range claim**

- **具体位置**: Section 4.4, Section 5.4, Appendix G (Table 9), Appendix P
- **问题**: Authorization scope 的 cross-judge κ 仅 0.385（Section 4.4），是所有类型中最低的。C4 的核心发现——52pp cross-model range（Claude 12% → GPT-5.4 64%）——正是基于这个最不可靠的类型。尽管论文用 within-judge bootstrap ranking preservation（99.5%）和 raw agreement 来补救，但存在三层问题：

  (1) **Cross-judge κ vs human-LLM κ 的混淆**：Section 5.4 引用"raw agreement 85.3%"来论证可靠性，但 Appendix G (Table 9) 的 human-LLM κ=0.644 与 Section 4.4 的 cross-judge κ=0.385 是不同指标，论文未明确区分这两个数据来源。读者可能误以为 85.3% 是 cross-judge 的 raw agreement。

  (2) **Within-judge 分析的局限**: within-judge 48pp range（Section 5.4）仅证明单个 judge 内部的排序稳定性，不能弥补 cross-judge 评测不一致。如果 GPT-5.4 和 GPT-4.1 对 authorization scope violation 的判定标准系统性不同，within-judge 稳定性反而说明偏差是稳定的。

  (3) **Appendix P 的 rank reversal**: Within-judge-group type ranking 在两组 judge 之间的相关性为 ρ=−0.03（p=0.96），而论文将此归因于 agent composition 差异。但 authorization scope 的 rank reversal（GPT-4.1 judged: rank 1; GPT-5.4 judged: rank 6）也可能反映 judge 偏差。

- **为什么影响接收**: C4 是论文四个 numbered claim 之一，52pp range 出现在 abstract 和 Figure 3 中。基于最低 reliability 类型的数据做 numbered claim，即使标注 [Exploratory]，仍有方法论风险。

- **建议修改方向**: (a) 计算 prevalence-adjusted agreement 指标（如 PABAK 或 Gwet's AC1）来澄清 κ=0.385 是否为 prevalence paradox；(b) 将 C4 从 numbered claim 降级为 Discussion 中的 observation；(c) 或在 abstract/conclusion 中不引用 52pp 具体数字，改为定性描述。

---

**W2 [SHOULD-FIX]: C2"两层结构"的表述强度与证据强度不匹配**

- **具体位置**: Section 5.2, Appendix A (Table 3), Appendix I
- **问题**: "Two-tier hierarchy"这一表述暗示稳定的层级结构，但实际证据受三个因素制约：

  (1) **Margin 依赖性**: ±10pp 时仅 3/6 mid-tier pair 达到 equivalence，±12pp 时 5/6，±15pp 时 6/6（Table 3）。TOST power 从 ±15pp 的 0.94 降至 ±10pp 的 0.57（Section 4.6）。"两层结构"在较小 margin 下并不成立。

  (2) **Bootstrap 聚类不稳定**: Incompleteness singleton 仅在 34.3% 的 bootstrap samples 中重现，AU p-value = 0.47（Appendix I）。这意味着 incompleteness 与其他类型的分界并不 robust。

  (3) **Kendall's W 不显著**: 五个主模型的类型排序一致性 W=0.398（p=0.072），未达到显著水平（Appendix M）。这意味着不同模型对类型危险度排序的共识不强，除了 incompleteness 始终最高。

  (4) **Confound-free 场景**: 如果按 confound-free lower bound 评估 incompleteness（31.6%），它将与 coreferential 持平、低于 mid-tier cluster——两层结构将崩塌。虽然 31.6% 是极端下界，但论文未讨论在 confound-adjusted 后两层结构是否仍成立。

- **建议**: 将"two-tier hierarchy"改为更谨慎的表述，如"incompleteness consistently separates as the highest-violation type, with the remaining types forming a less differentiated cluster at the ±15pp equivalence margin." 明确承认 margin 依赖性和 bootstrap 不稳定性。

---

**W3 [SHOULD-FIX]: SESOI ±15pp 的论证存在循环性**

- **具体位置**: Section 4.6
- **问题**: ±15pp 的论证逻辑是：(1)"a type producing ≥15 pp more violations warrants distinct policy handling in deployment"——这是用结论论证前提；(2)"exceeds the perturbation control bound (6.67 pp) by >2×"——这是测量噪声标准，不是实质性差异标准。

  在安全评估场景下，±15pp 相当宽松。如果类型 A 比类型 B 高 14pp 违规率（在 ±15pp 下被判定为"等价"），在实际部署中可能意味着成百上千次额外违规。论文承认"No field-standard SESOI exists"，但这更需要从实际部署角度论证而非回避。

  好的一面是，Table 3 提供了 7 个 margin 的完整敏感性分析，bootstrap 聚类是 margin-free 的。但 primary threshold 的选择影响了 C2 的核心表述。

- **建议**: 从部署角度论证：例如，给出一个假设场景（如 1000 interactions/day 的 agent，15pp 差异 = 150 extra violations/day），讨论这个量级是否足以触发不同的 policy handling。或者将 ±10pp 和 ±15pp 并列为 primary results，展示 C2 在两个 threshold 下的差异。

---

**W4 [SHOULD-FIX]: Cross-judge 设计仅使用 OpenAI 家族模型**

- **具体位置**: Section 4.4
- **问题**: GPT-5.4 和 GPT-4.1 均来自 OpenAI。OpenAI 模型家族可能共享系统性偏差（如对特定 violation 模式的敏感度、对 authorization boundary 的理解方式）。论文论证"the cross-judge asymmetry affects only absolute violation rates, not C1 or C2"（Section 4.4），但这一论证基于差值消除假设——只有当两个 judge 的偏差方向相同且幅度相近时才成立。如果 GPT-5.4 和 GPT-4.1 因共享训练策略而有 correlated bias，差值确实可以消除共模偏差；但如果偏差是 type-specific 的（如 OpenAI 模型普遍对 authorization scope 判定更严格），则不会被差值消除。

- **建议**: 在 Limitations 中增加对 single-family judge bias 的讨论。如有资源，在 replication study 中用 Claude 或 Gemini 作为 judge 对 subset 评估。

---

**W5 [SHOULD-FIX]: Human validation 样本量不足以支撑 type-level claims**

- **具体位置**: Section 4.4, Appendix G (Table 9)
- **问题**: 每种类型仅 32-34 episodes 的 human validation。Bootstrap 95% CI 极宽：scopal κ 的 CI 为 [0.00, 1.00]，coreferential 为 [0.00, 0.84]（Table 9）。论文正确承认"lack power for type-level comparison"（Section 4.4），但仍然基于自动评估做出 type-level claims（C2-C4）。当 human validation 无法验证 type-level 可靠性时，C2-C4 的有效性取决于对自动 judge 的 type-level 信任——而 W1 已经表明这种信任在 authorization scope 上是脆弱的。

- **建议**: (a) 增大 human validation 样本量至每类 80-100 以获得可解释的 type-level CI；或 (b) 在 Limitations 中更强调 type-level claims 的 validation gap。

---

**W6 [MINOR]: Discussion 与 Appendix B 的 mitigation 数字不一致**

- **具体位置**: Section 7 (Discussion) vs Appendix B (Table 4)
- **问题**: Discussion 报告 GPT-5.4 上 type-specific prompting 使 incompleteness **恶化** +14pp（p=0.118）；Table 4 报告同一模型同一类型 **改善** −2.6pp。两个实验的设计差异（不同 prompt？不同 clause subset？）未明确说明。Authorization scope 也不一致：Discussion 报告 −12pp（p=0.070），Table 4 报告 −40.0pp。
- **建议**: 明确标注 Discussion 和 Appendix B 是两个独立实验，说明 prompt 和数据差异。

---

**W7 [MINOR]: Domain 泛化性有限**

- **具体位置**: Section 8 (Limitations)
- τ²-bench 仅覆盖零售/航空客服。医疗、金融、法律领域的 policy ambiguity 可能产生不同的类型层级。

---

### Questions

**Q1**: Cross-judge κ=0.385（authorization scope）的 raw agreement 具体是多少？是否可以计算 PABAK 或 Gwet's AC1 来区分 prevalence paradox 和真实分歧？

**Q2**: 如果用 confound-adjusted effect size（而非 raw violation rate）重新做 TOST 分析，C2 的两层结构是否仍然成立？

**Q3**: Perturbation control 的扰动幅度（synonym substitution, clause reordering）是否与 ambiguity perturbation 的 token-level 变化量匹配？如果前者的修改量更小，null result 的信息量有限。

**Q4**: 在 replication study 中，为何不报告 cross-provider ICC？Gemini 和 LLaMA 加入后的 7-model ICC 是多少？

**Q5**: Kendall's W=0.398（p=0.072）表明五个主模型的类型排序一致性不显著。这是否意味着除 incompleteness 外，type hierarchy 是 model-dependent 的？这对 C2 的普适性有何影响？

**Q6**: Discussion 中 GPT-5.4 的 type-specific mitigation 结果（incompleteness +14pp, auth scope −12pp）与 Table 4 的结果（−2.6pp, −40.0pp）差异很大。这是两个不同的实验吗？如果是，请明确说明实验设计差异。

---

### Missing References

论文的引用覆盖基本完整。以下是可考虑补充的：

1. 关于 LLM judge 偏差的系统性研究——虽然引用了 Zheng et al. (2024)，但未引用关于 LLM judge 在不同 task type 上 reliability 差异的更细粒度工作
2. 关于 equivalence testing 在 NLP 中应用的先例（如果存在），以支撑 SESOI 选择的合理性
3. 关于 safety-critical 系统中 ambiguity 评估的跨领域文献（aviation, medical NLP），可增强 taxonomy 的理论基础

---

### Overall Assessment

**评分: 3.5 (Borderline Conference)**
**置信度: 4/5**

这篇论文在实验设计和统计分析上显著优于该领域的平均水平。C1（ambiguity 因果效应，OR=15.1, 7 模型一致）证据充分，taxonomy 的桥接 NLP/RE 的构思有价值，error analysis（尤其 Disambiguation Neglect）有实际意义。

阻碍 Conference 接收的核心问题是测量可靠性：C4 基于最低 reliability 类型（authorization scope κ=0.385）的数据做 numbered claim，C2 的"两层结构"在 bootstrap 聚类中仅 34.3% 稳定，SESOI 论证存在循环性。如果作者能 (1) 将 C4 降级为 observation 或补充 prevalence-adjusted agreement，(2) 缓和 C2 的表述强度并讨论 confound-adjusted 场景下的结构稳定性，(3) 从部署角度论证 SESOI，这篇论文可以达到 Conference 水平（4.0）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 972 · 2026-05-22T08:47:32.237570+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每个 Strength 和 Weakness，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 完整审稿意见\n\n### Overall: 3.5 / 5 (Borderline Conference), Confidence: 4/5\n\n### Strengths\n\n**S1: 严谨的 matched-pair 因果设计 + perturbation control**\n300 对 clause pair（96% annotator agreement），perturbation control（Δ_perturb = −0.67pp, 95% CI [−8.0, 6.67] 包含零）有效排除了表面扰动的混杂效应。Section 4.2 和 4.5 的设计使得 C1 的因果推断具有说服力。\n\n**S2: 全面的统计分析框架**\nMcNemar + TOST + bootstrap 聚类 + Holm-Bonferroni 三组校正 + post-hoc 功效分析（C1/C2 power > 0.99），同时在 7 个 margin（±5–20pp）上展示 TOST 敏感性分析（Table 3/Appendix A），这在该领域中不常见且值得肯定。\n\n**S3: 诚实的 claim 标定**\nC3 明确标注为 inconclusive（未通过 Holm-Bonferroni 校正），C4 标注为 [Exploratory]，authorization scope 的 52pp range 被表述为\"suggestive rather than definitive\"和\"upper bound with substantial measurement uncertainty\"（Section 5.4）。\n\n**S4: 有价值的 error analysis**\nSection 6 的五种 failure mode taxonomy 揭示了类型特异的机制路径，\"Disambiguation Neglect\"（4.6% awareness rate）是一个有实际意义的发现，且 mitigation experiment 证实了 prompt-level 干预的局限性。\n\n**S5: Incompleteness 混杂处理相对充分**\nAppendix F/H 提供了 token delta logistic regression（incompleteness p=0.018, coefficient change <8%），coreferential 的 confound-free lower bound（31.6%），以及 authorization scope 的反证逻辑。\n\n### Weaknesses\n\n**W1 [MUST-FIX]: Authorization scope cross-judge κ=0.385 严重削弱 C4 的 52pp range claim**\n三层问题：(1) cross-judge κ 与 human-LLM κ 的混淆（Section 5.4 引用 raw agreement 85.3% 但来源不明确）；(2) within-judge 48pp range 仅证明单个 judge 内部稳定性，不能弥补 cross-judge 不一致——稳定偏差仍是偏差；(3) Appendix P 的 within-judge-group type ranking ρ=−0.03 可能反映 judge bias 而非 agent composition 差异。建议将 C4 降级为 Discussion observation 或补充 prevalence-adjusted agreement。\n\n**W2 [SHOULD-FIX]: C2\"两层结构\"的表述强度与证据不匹配**\n四个制约因素：(1) ±10pp 仅 3/6 pair equivalent, TOST power 降至 0.57；(2) bootstrap AU p=0.47；(3) Kendall's W=0.398 (p=0.072) 不显著；(4) confound-free 场景下 incompleteness 降至 31.6% 将与 coreferential 持平。建议改为更谨慎的表述。\n\n**W3 [SHOULD-FIX]: SESOI ±15pp 论证存在循环性**\n\"≥15pp warrants distinct policy handling\" 是用结论论证前提；\"exceeds perturbation bound by >2×\" 是测量标准非实质标准。在安全场景下 ±15pp 相当宽松（14pp 差异 = 大量额外违规）。建议从部署角度做实质论证。\n\n**W4 [SHOULD-FIX]: Cross-judge 设计仅使用 OpenAI 家族模型**\nGPT-5.4/GPT-4.1 可能共享 type-specific bias（如 OpenAI 模型对 authorization scope 判定更严格）。差值消除假设在 correlated bias 下不成立。\n\n**W5 [SHOULD-FIX]: Human validation 每类仅 32-34 episodes**\nScopal CI [0.00, 1.00], coreferential CI [0.00, 0.84]。type-level claims (C2-C4) 的有效性依赖对自动 judge 的 type-level 信任——但 W1 已表明此信任在 auth scope 上脆弱。\n\n**W6 [MINOR]: Discussion 与 Appendix B 的 mitigation 数字不一致**\nDiscussion: GPT-5.4 incompleteness +14pp (p=0.118); Table 4: 同模型同类型 −2.6pp。Auth scope 也不一致（−12pp vs −40.0pp）。两个实验的设计差异未说明。\n\n**W7 [MINOR]: Domain 泛化性有限**\nτ²-bench 仅覆盖零售/航空客服。\n\n### Questions\nQ1: Auth scope cross-judge κ=0.385 的 raw agreement？可否计算 PABAK/AC1？\nQ2: Confound-adjusted effect size 重做 TOST，C2 是否仍成立？\nQ3: Perturbation control 的修改量是否与 ambiguity perturbation 匹配？\nQ4: 为何不报告 cross-provider ICC？\nQ5: Kendall's W=0.398 不显著，C2 的普适性？\nQ6: Discussion vs Table 4 的 mitigation 数字差异是两个不同实验吗？",
  "project": "policy_ambiguity_safety",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每个 Strength 和 Weakness，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 完整审稿意见\n\n### Overall: 3.5 / 5 (Borderline Conference), Confidence: 4/5\n\n### Strengths\n\n**S1: 严谨的 matched-pair 因果设计 + perturbation control**\n300 对 clause pair（96% annotator agreement），perturbation control（Δ_perturb = −0.67pp, 95% CI [−8.0, 6.67] 包含零）有效排除了表面扰动的混杂效应。Section 4.2 和 4.5 的设计使得 C1 的因果推断具有说服力。\n\n**S2: 全面的统计分析框架**\nMcNemar + TOST + bootstrap 聚类 + Holm-Bonferroni 三组校正 + post-hoc 功效分析（C1/C2 power > 0.99），同时在 7 个 margin（±5–20pp）上展示 TOST 敏感性分析（Table 3/Appendix A），这在该领域中不常见且值得肯定。\n\n**S3: 诚实的 claim 标定**\nC3 明确标注为 inconclusive（未通过 Holm-Bonferroni 校正），C4 标注为 [Exploratory]，authorization scope 的 52pp range 被表述为\"suggestive rather than definitive\"和\"upper bound with substantial measurement uncertainty\"（Section 5.4）。\n\n**S4: 有价值的 error analysis**\nSection 6 的五种 failure mode taxonomy 揭示了类型特异的机制路径，\"Disambiguation Neglect\"（4.6% awareness rate）是一个有实际意义的发现，且 mitigation experiment 证实了 prompt-level 干预的局限性。\n\n**S5: Incompleteness 混杂处理相对充分**\nAppendix F/H 提供了 token delta logistic regression（incompleteness p=0.018, coefficient change <8%），coreferential 的 confound-free lower bound（31.6%），以及 authorization scope 的反证逻辑。\n\n### Weaknesses\n\n**W1 [MUST-FIX]: Authorization scope cross-judge κ=0.385 严重削弱 C4 的 52pp range claim**\n三层问题：(1) cross-judge κ 与 human-LLM κ 的混淆（Section 5.4 引用 raw agreement 85.3% 但来源不明确）；(2) within-judge 48pp range 仅证明单个 judge 内部稳定性，不能弥补 cross-judge 不一致——稳定偏差仍是偏差；(3) Appendix P 的 within-judge-group type ranking ρ=−0.03 可能反映 judge bias 而非 agent composition 差异。建议将 C4 降级为 Discussion observation 或补充 prevalence-adjusted agreement。\n\n**W2 [SHOULD-FIX]: C2\"两层结构\"的表述强度与证据不匹配**\n四个制约因素：(1) ±10pp 仅 3/6 pair equivalent, TOST power 降至 0.57；(2) bootstrap AU p=0.47；(3) Kendall's W=0.398 (p=0.072) 不显著；(4) confound-free 场景下 incompleteness 降至 31.6% 将与 coreferential 持平。建议改为更谨慎的表述。\n\n**W3 [SHOULD-FIX]: SESOI ±15pp 论证存在循环性**\n\"≥15pp warrants distinct policy handling\" 是用结论论证前提；\"exceeds perturbation bound by >2×\" 是测量标准非实质标准。在安全场景下 ±15pp 相当宽松（14pp 差异 = 大量额外违规）。建议从部署角度做实质论证。\n\n**W4 [SHOULD-FIX]: Cross-judge 设计仅使用 OpenAI 家族模型**\nGPT-5.4/GPT-4.1 可能共享 type-specific bias（如 OpenAI 模型对 authorization scope 判定更严格）。差值消除假设在 correlated bias 下不成立。\n\n**W5 [SHOULD-FIX]: Human validation 每类仅 32-34 episodes**\nScopal CI [0.00, 1.00], coreferential CI [0.00, 0.84]。type-level claims (C2-C4) 的有效性依赖对自动 judge 的 type-level 信任——但 W1 已表明此信任在 auth scope 上脆弱。\n\n**W6 [MINOR]: Discussion 与 Appendix B 的 mitigation 数字不一致**\nDiscussion: GPT-5.4 incompleteness +14pp (p=0.118); Table 4: 同模型同类型 −2.6pp。Auth scope 也不一致（−12pp vs −40.0pp）。两个实验的设计差异未说明。\n\n**W7 [MINOR]: Domain 泛化性有限**\nτ²-bench 仅覆盖零售/航空客服。\n\n### Questions\nQ1: Auth scope cross-judge κ=0.385 的 raw agreement？可否计算 PABAK/AC1？\nQ2: Confound-adjusted effect size 重做 TOST，C2 是否仍成立？\nQ3: Perturbation control 的修改量是否与 ambiguity perturbation 匹配？\nQ4: 为何不报告 cross-provider ICC？\nQ5: Kendall's W=0.398 不显著，C2 的普适性？\nQ6: Discussion vs Table 4 的 mitigation 数字差异是两个不同实验吗？",
    "project": "policy_ambiguity_safety",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 973 · 2026-05-22T08:48:03.316704+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 31079
}
```

</details>

---


### Tool call

_source line 974 · 2026-05-22T08:48:03.718602+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个 Strength 和 Weakness，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 完整审稿意见\n\n### Overall: 3.5 / 5 (Borderline Conference), Confidence: 4/5\n\n### Strengths\n\n**S1. Matched-pair causal design 确属创新。** 在 NLP agent safety 领域，现有工作均为 correlational 或 benchmark-evaluation 范式。matched-pair design + perturbation control 确实建立了 ambiguity → violation 的因果链。\n\n**S2. 统计方法论异常充分。** TOST + bootstrap cluster + Holm-Bonferroni 三重验证。SESOI domain-anchored justification 和 margin dependence acknowledgment 体现方法论自觉。\n\n**S3. Honest about limitations。** Incompleteness confound 多层控制，C3 null result 坦诚报告，auth scope κ=0.385 反复标注，C4 标为 [Exploratory]。\n\n**S4. Error analysis 有实质洞见。** 三种 failure mechanism 与 ambiguity type 的对应关系提供了机制理解。Systematic nocuity（41.3%）揭示了 agreement-based evaluation 盲区。\n\n**S5. 实验规模与模型覆盖度。** 5+2 models, 7 providers, 2997 episodes。\n\n### Weaknesses\n\n**W1 [SHOULD-FIX] Taxonomy 理论基础：incompleteness 和 conditional precedence 并非 \"ambiguity\"，§3 的论证存在循环。**\n§3 用行为结果（violation pattern 相似）来证明纳入 taxonomy 的合理性，但这些结果本身依赖于它们已被纳入 taxonomy 并在 benchmark 中测试。Incompleteness 是最高 violation 类型（53.6%），如果理论上不属于 ambiguity，中心叙事被削弱。Dalpiaz et al. (2018) 的 co-occurrence ≠ identity。建议重新框架为 \"policy specification defects\" 或增加更实质的理论论证。\n\n**W2 [SHOULD-FIX] \"Disambiguation Neglect\" 新颖性被高估。**\nLiu et al. (2023) 已证明 LLMs collapse multiple interpretations。Hu et al. (2025) 论证 missing conceptual representations。本文增量是在 agent policy 场景中量化，但不应列为 primary contribution。\n\n**W3 [SHOULD-FIX] \"Differential Nocuity\" 框架增量贡献有限。**\nBerry & Kamsties (2004) 已隐含 type-dependent risk。Willis et al. (2008) 已研究 nocuity degree。本文贡献是 empirical evidence，但 framework name 过于宏大。\n\n**W4 [SHOULD-FIX] Abstract/Introduction 中 claim 精确度与正文证据不完全匹配。**\n(a) Abstract \"risk gradient\" vs §5.2 \"two-tier structure\" 表述不一致；(b) Introduction 52pp range caveat 权重不够；(c) \"type identity explaining 22× more variance\" 但正文实为 \"clause identity\"，clause ≠ type。\n\n**W5 [MINOR] Related Work 遗漏若干相关工作。**\nOpenAgentSafety (ICLR 2026), Agent-SafetyBench (2024), Ferrari et al. (2019) \"Ambiguity in RE: Towards a Unifying Framework\", Automated Repair of Ambiguous NL Requirements (2025).\n\n**W6 [MINOR] Coreferential 在 mitigation 和 replication 中均被排除。**\n\n**W7 [MINOR] §7 Mitigation 样本量偏小。**\nn=50 per type 的 McNemar test 功效有限。Incompleteness worsening (+14pp, p=0.118) 的因果解释（confabulation）过于确定。\n\n### Questions\nQ1: Bootstrap AU p=0.47 如何与 \"incompleteness stands apart\" 的 confident framing 调和？\nQ2: \"Clause identity explains 22.4% of variance\" 是 300 clause pair 的 random effect 还是 6 type 的 fixed effect？\nQ3: Temperature=0 下 ICC=0.919 的变异来源？\nQ4: §4.2 的 \"realism validation\" 具体 protocol？",
  "project": "policy_ambiguity_safety",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个 Strength 和 Weakness，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 完整审稿意见\n\n### Overall: 3.5 / 5 (Borderline Conference), Confidence: 4/5\n\n### Strengths\n\n**S1. Matched-pair causal design 确属创新。** 在 NLP agent safety 领域，现有工作均为 correlational 或 benchmark-evaluation 范式。matched-pair design + perturbation control 确实建立了 ambiguity → violation 的因果链。\n\n**S2. 统计方法论异常充分。** TOST + bootstrap cluster + Holm-Bonferroni 三重验证。SESOI domain-anchored justification 和 margin dependence acknowledgment 体现方法论自觉。\n\n**S3. Honest about limitations。** Incompleteness confound 多层控制，C3 null result 坦诚报告，auth scope κ=0.385 反复标注，C4 标为 [Exploratory]。\n\n**S4. Error analysis 有实质洞见。** 三种 failure mechanism 与 ambiguity type 的对应关系提供了机制理解。Systematic nocuity（41.3%）揭示了 agreement-based evaluation 盲区。\n\n**S5. 实验规模与模型覆盖度。** 5+2 models, 7 providers, 2997 episodes。\n\n### Weaknesses\n\n**W1 [SHOULD-FIX] Taxonomy 理论基础：incompleteness 和 conditional precedence 并非 \"ambiguity\"，§3 的论证存在循环。**\n§3 用行为结果（violation pattern 相似）来证明纳入 taxonomy 的合理性，但这些结果本身依赖于它们已被纳入 taxonomy 并在 benchmark 中测试。Incompleteness 是最高 violation 类型（53.6%），如果理论上不属于 ambiguity，中心叙事被削弱。Dalpiaz et al. (2018) 的 co-occurrence ≠ identity。建议重新框架为 \"policy specification defects\" 或增加更实质的理论论证。\n\n**W2 [SHOULD-FIX] \"Disambiguation Neglect\" 新颖性被高估。**\nLiu et al. (2023) 已证明 LLMs collapse multiple interpretations。Hu et al. (2025) 论证 missing conceptual representations。本文增量是在 agent policy 场景中量化，但不应列为 primary contribution。\n\n**W3 [SHOULD-FIX] \"Differential Nocuity\" 框架增量贡献有限。**\nBerry & Kamsties (2004) 已隐含 type-dependent risk。Willis et al. (2008) 已研究 nocuity degree。本文贡献是 empirical evidence，但 framework name 过于宏大。\n\n**W4 [SHOULD-FIX] Abstract/Introduction 中 claim 精确度与正文证据不完全匹配。**\n(a) Abstract \"risk gradient\" vs §5.2 \"two-tier structure\" 表述不一致；(b) Introduction 52pp range caveat 权重不够；(c) \"type identity explaining 22× more variance\" 但正文实为 \"clause identity\"，clause ≠ type。\n\n**W5 [MINOR] Related Work 遗漏若干相关工作。**\nOpenAgentSafety (ICLR 2026), Agent-SafetyBench (2024), Ferrari et al. (2019) \"Ambiguity in RE: Towards a Unifying Framework\", Automated Repair of Ambiguous NL Requirements (2025).\n\n**W6 [MINOR] Coreferential 在 mitigation 和 replication 中均被排除。**\n\n**W7 [MINOR] §7 Mitigation 样本量偏小。**\nn=50 per type 的 McNemar test 功效有限。Incompleteness worsening (+14pp, p=0.118) 的因果解释（confabulation）过于确定。\n\n### Questions\nQ1: Bootstrap AU p=0.47 如何与 \"incompleteness stands apart\" 的 confident framing 调和？\nQ2: \"Clause identity explains 22.4% of variance\" 是 300 clause pair 的 random effect 还是 6 type 的 fixed effect？\nQ3: Temperature=0 下 ICC=0.919 的变异来源？\nQ4: §4.2 的 \"realism validation\" 具体 protocol？",
    "project": "policy_ambiguity_safety",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 975 · 2026-05-22T08:48:05.281345+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1562
}
```

</details>

---


### Assistant

_source line 976 · 2026-05-22T08:48:09.033555+00:00_

交叉分享已发出，等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 88

## Round 88

2 recorded events


### User

_source line 977 · 2026-05-22T08:48:11.741048+00:00_

[Reviewer 1 审稿结果]:
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
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 978 · 2026-05-22T08:48:19.362722+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 89

## Round 89

2 recorded events


### User

_source line 979 · 2026-05-22T08:50:28.011214+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 对 Reviewer 1 的交叉回应

### Strengths 回应
- [AGREE] R1-S1 至 R1-S5：全部同意，与我的 S1-S5 高度一致。

### Weaknesses 逐条回应

**[AGREE] R1-W1 (Auth scope κ=0.385 → C4)**
R1 的三层分析到位。我补充：(1) within-judge bootstrap 99.5% stability 确实只证明 single-judge 内部一致性；(2) Appendix P ρ=−0.03 中 agent composition 和 judge bias 不可分离。但建议将 MUST-FIX 降为 SHOULD-FIX——论文已将 C4 标注为 [Exploratory] 且五次标注 κ 局限，核心修改点是 Introduction 中弱化 52pp range 呈现。

**[REBUT] R1-W2 sub-point (4): "confound-free 场景下 incompleteness 降至 31.6%"**
R1 混淆了两个概念：coreferential 31.6% 是 confound-free lower bound（任何类型的最保守效应下限），不是 incompleteness 的 adjusted effect。Appendix F/H logistic regression 控制 token delta 后 incompleteness 仍显著（p=0.018, coefficient change <8%）。R1 的 sub-points (1)-(3) 我均同意——bootstrap AU p=0.47、Kendall's W=0.398 不显著——但 incompleteness 作为 upper bound 的证据稳健（7 模型均 ≥46%）。

**[AGREE] R1-W2 sub-points (1)(2)(3):** "Two-tier" 表述需弱化，与我的 W4(a) 一致。

**[AGREE] R1-W3 (SESOI ±15pp 论证):** 论证不够实质，但论文提供了 7-margin 敏感性分析 + margin-free bootstrap 作为补充。严重程度适中。

**[AGREE] R1-W4 (Cross-judge 仅 OpenAI):** 核心论点成立但需区分影响范围——C1/C2 的 within-pair Δpp 中 judge bias 被消除，真正受影响的是 C4 的 cross-model comparison（与 W1 同一问题）。

**[AGREE] R1-W5 (Human validation 样本量):** Scopal CI [0.00, 1.00] 确实 uninformative。

**[AGREE] R1-W6 (Mitigation 数字不一致):** 确认为两个不同实验：§7 是 n=50/GPT-5.4/generic+type-specific，Appendix B 是 1,256 episodes/5 models/type-specific only。论文未明确说明两者关系，这是 presentation 问题。我遗漏了此点。

**[AGREE] R1-W7 (Domain 泛化):** 一致，MINOR。

### R1 Questions 回应
- Q1: 合理，建议对 auth scope 也报告 Gwet's AC1
- Q2: 有价值但技术复杂，超出 minor revision 范围
- Q3: Perturbation control 是 negative control，有效性不依赖修改量匹配
- Q4: Cross-provider ICC 中 judge/provider 效应不可分离，应说明而非省略
- Q5: Incompleteness upper bound 稳健，mid-tier ranking 跨模型不稳定
- Q6: 确认两个不同实验，需在 revision 中明确区分

### 两位 Reviewer 的互补发现
**共识**：总体评分 3.5，方法论扎实但 framing 需校准，auth scope measurement 问题，two-tier 表述过强。

**R1 独有贡献**：W6 数字不一致、W3 SESOI 循环性、W4 OpenAI correlated bias。

**我的独有贡献**：W1 taxonomy 理论循环论证（incompleteness/cond.prec. ≠ ambiguity）、W2/W3 coined terms novelty overclaiming、W4(c) clause vs type identity 归因错误、W5 missing references。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 980 · 2026-05-22T08:50:38.242066+00:00_

Reviewer 2 的交叉回应已收到。等待 Reviewer 1 对 Reviewer 2 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 90

## Round 90

2 recorded events


### User

_source line 981 · 2026-05-22T08:50:40.906592+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。总结：

- **5 个 AGREE**（W1 部分同意但建议降至 SHOULD-FIX、W3-W7 同意）
- **1 个 REBUT**：R1-W2 sub-point (4) 混淆了 coreferential lower bound 与 incompleteness adjusted effect——logistic regression 控制 token delta 后 incompleteness 仍显著 (p=0.018)
- R1 发现了我遗漏的 W6（两个 mitigation 实验的数字不一致），我的独有贡献是 taxonomy 理论循环、coined terms overclaiming、clause vs type identity 归因问题

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 982 · 2026-05-22T08:50:45.006725+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 91

## Round 91

10 recorded events


### User

_source line 983 · 2026-05-22T08:51:01.801875+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应

---

### Strengths 回应

**[AGREE] R2-S1 (Matched-pair causal design)**
完全同意。这是该领域首个建立 ambiguity → violation 因果链的工作。我的 S1 做了相同评价。perturbation control（Δ=−0.67pp, CI 包含零; Section 4.5）有效排除了表面扰动的混杂。

**[AGREE] R2-S2 (统计方法论)**
同意。TOST + bootstrap + Holm-Bonferroni 的三重验证在该领域中罕见。但我对 SESOI ±15pp 的论证有保留意见（见我的 W3）——R2 称之为"domain-anchored justification"，但 Section 4.6 的锚定逻辑存在循环性（"产生 ≥15pp 差异的类型值得差异化处理"用结论论证前提）。

**[AGREE] R2-S3 (Honest about limitations)**
同意。C3 坦诚报告 null result、C4 标注 [Exploratory]、auth scope κ=0.385 反复标注，这在审稿中值得肯定。

**[AGREE] R2-S4 (Error analysis)**
同意。三种 failure mechanism 的类型对应关系（structural misparse → scopal/cond. prec.; information gap-filling → incompleteness/lexical; boundary violation → auth scope; Section 6.1）确实提供了超越统计关联的机制理解。Systematic nocuity 41.3%（Section 6.3）揭示了 agreement-based evaluation 的盲区。

**[AGREE] R2-S5 (实验规模)**
同意。5+2 模型、6 providers、2997 episodes 的覆盖度在该领域属于高水平。

---

### Weaknesses 回应

**[REBUT] R2-W1: Taxonomy 理论基础——incompleteness/conditional precedence 并非"ambiguity"**

R2 的理论关切有一定道理，但论证过于强硬，忽略了论文的操作性定义和文献基础。

(1) **操作性定义已明确给出**：Section 3 定义 "a policy clause is ambiguous when it admits multiple operationally distinct interpretations by an LLM agent"（原文）。在此定义下，incompleteness（缺失信息导致 agent 用不同默认值填充）和 conditional precedence（规范冲突导致不同优先级选择）均产生多个可操作的不同解读，符合定义。R2 似乎要求的是 linguistic ambiguity 的狭义定义，但论文明确将范围扩展到了 RE 文献。

(2) **文献支撑非仅 co-occurrence**：Section 3 引用了 Berry et al. (2004) 对 requirements specification 中 ambiguity 的广义分类（包含 incompleteness），Dalpiaz et al. (2018) 证明 ambiguity 和 incompleteness 在 RE 中频繁共现且行为上难以区分，以及 Li et al. (2024b) 的 11 类 NLP taxonomy 也包含类似的 specification-layer 类型。论文不是用行为结果来论证纳入——而是基于 RE/NLP 文献的分类传统。

(3) **"Policy specification defects" 的替代命名会引入新问题**：如果改名，就切断了与 NLP ambiguity 文献（Berry & Kamsties, Li et al.）的联系，而这正是论文的理论锚点之一。

但我同意 R2 的一个子观点：Section 3 的 "scope of ambiguity" 讨论可以更清晰地区分 linguistic ambiguity（狭义）和 specification ambiguity（广义），而非依赖读者自行接受操作性定义。

**[AGREE] R2-W2: Disambiguation Neglect 新颖性被高估**

同意。Introduction 将 Disambiguation Neglect 列为第三个 contribution（"(3) an error analysis revealing Disambiguation Neglect"），但 Liu et al. (2023) 和 Hu et al. (2025) 已分别在 language understanding 层面证明了类似现象（Section 6.2 也承认 "consistent with Hu et al. (2025)"）。本文的增量是在 agent policy 执行场景中量化（4.6% awareness, Section 6.2），但这更适合作为 error analysis 的 finding 而非 primary contribution。建议将 contribution (3) 重新措辞，强调场景特异性和量化贡献，而非暗示发现了一个新现象。

**[AGREE] R2-W3: Differential Nocuity 框架增量有限**

同意。"Differential nocuity" 出现在 Discussion（Section 7）而非 contribution list，但命名暗示了一个新 framework。实际上 Berry & Kamsties (2004) 的 nocuous/innocuous 区分和 Willis et al. (2008) 的 nocuity degree 已经隐含了 type-dependent risk 的概念。本文的贡献是提供了 empirical evidence（不同 ambiguity type 有不同 nocuity），但框架层面的增量有限。将其定位为"empirical validation of differential nocuity"比"proposing a differential nocuity framework"更准确。

**[AGREE] R2-W4: Claim 精确度问题**

这一条的三个子点都有道理：

(a) **"risk gradient" vs "two-tier structure"**：Abstract 说"a risk gradient rather than a uniform threat"，但 Section 5.2 的 TOST 分析实际展示的是"two-tier structure"——incompleteness 独立 + 其余类型构成一个 cluster。"Gradient"暗示连续变化，"two-tier"暗示离散分层。这两个措辞不一致，应统一为"two-tier"。

(b) **52pp caveat 权重不够**：我在自己的 W1 中也提出了类似的问题。Introduction 中的 caveat 仅在从句位置（"though this is an upper bound..."），与 52pp 这个数字的突出位置不对称。

(c) **"clause identity" vs "type identity"**：R2 正确指出这是一个重要的文字错误。Section 5.1 明确写的是"Clause identity explains 22.4% of variance versus 1.0% for model identity"——clause 是 300 个具体条款的 random effect，不是 6 个类型的 fixed effect。如果 Introduction 的 contribution (2) 写成了"type identity"，这是实质性错误（22.4% for 300 clauses vs 远低于此的 6 types），必须修正。

**[REBUT] R2-W5: Related Work 遗漏**

部分反驳。R2 列出的遗漏中：

- **Agent-SafetyBench (2024)**：Section 2 已引用 agent safety evaluation 文献（Yuan et al., 2024; Ruan et al., 2024; Yin et al., 2025; Wu and Gong, 2026）。如果 Agent-SafetyBench 与这些工作有实质性差异（如不同的 evaluation dimension），值得补充；否则为同类引用的替代品。

- **Ferrari et al. (2019) "Ambiguity in RE"**：Section 2 已引用 Ferrari and Esuli (2019)（Related Work, page 2），这应该就是 R2 提到的这篇。

- **OpenAgentSafety (ICLR 2026)** 和 **Automated Repair of Ambiguous NL Requirements (2025)**：如果这两篇确实相关且未被引用，值得补充。但 Related Work 不能穷尽所有相关工作，是否遗漏取决于这些工作是否提供了本文未讨论的 complementary perspective。

**[AGREE] R2-W6: Coreferential 排除**

同意这是一个限制。论文给出了合理的技术原因（Appendix B: pronoun resolution 无法设计 type-specific disambiguation prompt; episode design 与原始 model configuration 耦合），但这意味着 6 类 taxonomy 中有 1 类在 mitigation 和 replication 中完全缺席。这不影响 C1 和 C2 的 main analysis（coreferential 有完整的 5-model 数据），但削弱了 taxonomy 的完整性声明。

**[AGREE] R2-W7: Mitigation 样本量和过度解释**

同意。n=50/type 的 McNemar test 对 14pp 效应的 power 不足（p=0.118 即未达到显著），但 Discussion 用确定性语言解释为"prompting agents to attend to missing information triggers confabulation rather than caution"（Section 7）。对一个 p=0.118 的非显著趋势给出因果机制解释（confabulation），属于过度解读。应明确标注为 non-significant trend 并降低解释的确定性。

此外，我在自己的 W6 中还发现了一个 R2 未提到的问题：Discussion 中 GPT-5.4 的 type-specific mitigation 数据（incompleteness +14pp, auth scope −12pp）与 Table 4（incompleteness −2.6pp, auth scope −40.0pp）数字不一致，两个实验的关系未明确说明。

---

### Questions 回应

**[AGREE] R2-Q1: Bootstrap AU p=0.47 vs "stands apart" framing**

这正是我的 W2 指出的问题。AU p-value=0.47 意味着 incompleteness singleton 不到一半的 bootstrap 样本中被重现（Appendix I）。Section 5.2 用"stands apart as an upper bound"措辞，虽然后面有"conditional on the confound controls"的限定，但与 AU p=0.47 的统计不稳定性不匹配。建议增加对 bootstrap 不稳定性的正文讨论，或缓和"stands apart"的措辞。

**[AGREE] R2-Q2: Clause identity vs type identity 的 22.4%**

重要问题。Section 5.1 说的是"Clause identity explains 22.4% of variance"——这是 300 个 clause pair 的 random effect，不是 6 个 ambiguity type 的 fixed effect。22.4% 由 300 个具体条款的措辞差异解释，其中 type 仅是分组变量。如果报告 type 的 fixed effect variance explained，数字会小得多（6 个 level 的 between-group variance / total variance）。作者应澄清：正文和 abstract 用"clause identity"是正确的，但 Introduction contribution (2) 如果用了"type identity"则需修正。

**[AGREE] R2-Q3: Temperature=0 下 ICC=0.919 的变异来源**

好问题。Temperature=0 理论上应产生 deterministic output，但实际中：(1) 大模型的 sampling 在 T=0 下仍可能有微小 stochasticity（floating-point non-determinism, batching 差异）；(2) τ²-bench 的 multi-turn 对话中，微小的初始差异在多轮交互中可能被放大。ICC=0.919 说明 8.1% 的 variance 来自 noise——在 30 clause pairs × 3 replicates 的设计下，这个量级值得解释。

**[REBUT] R2-Q4: Realism validation protocol**

Section 4.2 提供了足够的信息："Clause pairs are generated through a template-based pipeline and reviewed by two independent annotators (both with NLP background)" with 96% agreement and 100% post-discussion consensus. "A post-hoc realism validation confirms linguistic consistency with original τ²-bench policy text"（Section 4.2）。论文还在 Limitations 中承认"realism validation confirms lexical comparability but cannot rule out distributional gaps"（Section 8）。protocol 的核心要素已给出——这不是一个遗漏，而是篇幅约束下的合理简写。不过 R2 如果要求更多细节（如具体的 rubric、评分标准、disagreement 的类型分布），作者可以在 camera-ready 或 appendix 中补充。

---

### 总结：R1 与 R2 的共识与分歧

**共识领域**（两位 reviewer 一致指出的问题）：
1. Authorization scope κ=0.385 影响 C4 可靠性（R1-W1, R2 在 S3 中承认但未单独列为 weakness）
2. Claim 精确度问题——特别是 clause vs type identity 的 22× claim（R2-W4c）
3. Mitigation 样本量和过度解释（R1-W6/W7, R2-W7）
4. Bootstrap 聚类不稳定性与"stands apart" framing 的张力（R1-W2, R2-Q1）
5. C2 "two-tier hierarchy" 表述强度偏高（R1-W2, R2-W4a 的 gradient vs two-tier 不一致）

**R1 额外关注**（R2 未提出）：
- SESOI ±15pp 循环论证（R1-W3）
- Cross-judge 仅用 OpenAI 家族（R1-W4）
- Human validation 样本量对 type-level claims 不足（R1-W5）
- Discussion vs Table 4 的 mitigation 数字不一致（R1-W6）

**R2 额外关注**（R1 未提出）：
- Taxonomy 理论基础（W1）——我部分反驳
- Disambiguation Neglect/Differential Nocuity 新颖性高估（W2, W3）——我同意
- Missing references（W5）——我部分反驳

**评分一致**: 两位 reviewer 均给出 3.5 (Borderline Conference), Confidence 4。核心判断一致：C1 证据充分，但 C2/C4 的表述强度和测量可靠性问题阻碍 Conference 接收。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 984 · 2026-05-22T08:51:23.897243+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "policy_ambiguity_safety"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "policy_ambiguity_safety"
  }
}
```

</details>

---


### Tool call

_source line 985 · 2026-05-22T08:51:23.897660+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "policy_ambiguity_safety"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "policy_ambiguity_safety"
  }
}
```

</details>

---


### Tool result

_source line 986 · 2026-05-22T08:51:23.948305+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-22T08:38:21.935022+00:00\", \"completed_at\": \"2026-05-22T08:41:55.432445+00:00\", \"findings\": [{\"severity\": \"warning\", \"dimension\": \"page 4-5\", \"message\": \"连续两页纯文本（Method + early Results），无任何 display item 穿插。建议在 §4 添加一个模型/数据集汇总表（如 models × parameters × training philosophy），打破视觉单调并方便审稿人快速定位实验配置\"}, {\"severity\": \"warning\", \"dimension\": \"page 15\", \"message\": \"最后一页 Appendix Q 仅 ~6 行内容，页面 ~90% 空白。建议将 Appendix Q 合并到前一页或调整附录顺序消除空页\"}, {\"severity\": \"info\", \"dimension\": \"page 2\", \"message\": \"Figure 1 左侧 taxonomy tree 的叶节点标签（Innocuous, Multi-Sit 等）字号偏小，打印后可能不够清晰。建议适当增大字号或简化树结构标签\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"Figure 2 热力图的单元格数值和 axis label 字号较小（约正文 60%），接近可读性下限。建议增大字号至正文 70% 以上\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Figure 3 同上，热力图内文字偏小。与 Figure 2 风格一致但都偏小\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"Table 2 使用 booktabs 风格，最优值加粗标注，精度统一——排版规范\"}, {\"severity\": \"info\", \"dimension\": \"page 3\", \"message\": \"Table 1 分类表排版清晰，Resolution 列信息密度高但可读\"}, {\"severity\": \"info\", \"dimension\": \"page 12\", \"message\": \"附录 page 12 包含 6 个表格（Tables 4–8），密度极高但作为附录可接受\"}, {\"severity\": \"info\", \"dimension\": \"page 6-7\", \"message\": \"热力图使用 yellow-to-red 渐变色，亮度有梯度变化（基本 colorblind-safe），但若添加数值标注（已有）+ 不同 marker/hatching 可进一步增强无障碍性\"}, {\"severity\": \"info\", \"dimension\": \"page 9-10\", \"message\": \"参考文献格式统一，未见 [?] 未解析引用，无明显 overfull\"}], \"counts\": {\"critical\": 0, \"warning\": 2, \"info\": 8}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 51
}
```

</details>

---


### Tool result

_source line 987 · 2026-05-22T08:51:23.948825+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 988 · 2026-05-22T08:54:11.628675+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "policy_ambiguity_safety",
  "issues_yaml": "## Round 11 (Fresh) Review Issues — policy_ambiguity_safety\n## Paper: \"Not All Policy Ambiguity Is Equal: Type-Specific Safety Risks for LLM Agents\"\n## Venue: EMNLP 2026 via ARR May cycle\n## Date: 2026-05-22\n## Round 11 Score: 3.5 (Borderline Conference)\n## Note: Fresh review session — all issues re-evaluated from scratch\n\n# ============================================================\n# CRITICAL ISSUES\n# ============================================================\n\n- id: \"R11-C1\"\n  summary: \"Authorization scope κ=0.385 不足以支撑 C4 中 52pp range 作为 numbered claim\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 8\n  last_seen_round: 11\n  mentions:\n    - round: 10\n      reviewers: [R1, R2]\n      note: \"两人完全共识: κ=0.385 低于 fair agreement 门槛(0.40), 52pp 中真实差异 vs noise 无法分离\"\n    - round: 11\n      reviewers: [R1, R2]\n      note: \"R1 MUST-FIX, R2 AGREE(建议降为 SHOULD-FIX 因 C4 已标 Exploratory). 共识三层问题: (1) cross-judge κ vs human-LLM κ 混淆, (2) within-judge stability 不能弥补 cross-judge 不一致, (3) Appendix P ρ=−0.03 的 agent composition vs judge bias 不可分离. 建议计算 PABAK/Gwet's AC1, 将 C4 降级为 Discussion observation, abstract/conclusion 不引用 52pp 具体数字\"\n  action_items:\n    - round: 11\n      action: \"(1) 计算 auth scope 的 PABAK 或 Gwet's AC1 区分 prevalence paradox 和真实分歧; (2) C4 从 numbered claim 降级为 Discussion observation; (3) Abstract/Conclusion 中 52pp 改为定性描述; (4) Section 5.4 明确区分 cross-judge κ=0.385 和 human-LLM κ=0.644 的数据来源\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-C2\"\n  summary: \"C2 two-tier hierarchy 表述强度超过证据——bootstrap 34.3%, Kendall's W=0.398 不显著, margin-dependent\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 8\n  last_seen_round: 11\n  mentions:\n    - round: 10\n      reviewers: [R1, R2]\n      note: \"Bootstrap AU p=0.47, ±10pp 仅 3/6 mid-tier pairs 等价, Kendall's W=0.398(p=0.072) 不显著\"\n    - round: 11\n      reviewers: [R1, R2]\n      note: \"R1 SHOULD-FIX, R2 AGREE. 四个制约因素完全共识. R2 REBUT R1 sub-point(4): coreferential 31.6% 是 confound-free lower bound 非 incompleteness adjusted effect(logistic regression p=0.018 仍显著). 共识: incompleteness upper bound 稳健(7 模型 ≥46%), 但 two-tier 表述需弱化为 'incompleteness consistently separates as highest-violation type, remaining types form less differentiated cluster at ±15pp margin'\"\n  action_items:\n    - round: 11\n      action: \"(1) Abstract/Intro/Conclusion 措辞弱化, 不用 'two-tier hierarchy'; (2) 正文并列呈现 ±10pp 和 ±15pp 结果; (3) 报告 AU p-value 在正文而非仅 Appendix; (4) 明确承认 margin 依赖性和 bootstrap 不稳定性\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# WARNING ISSUES\n# ============================================================\n\n- id: \"R11-W1\"\n  summary: \"Taxonomy 理论基础: incompleteness 和 conditional precedence 不满足 strict ambiguity 定义, §3 论证需扩展\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 9\n  last_seen_round: 11\n  mentions:\n    - round: 10\n      reviewers: [R2, R1]\n      note: \"R2 SHOULD-FIX, R1 部分 REBUT. 需要在 §3 中更充分讨论理论边界\"\n    - round: 11\n      reviewers: [R2, R1]\n      note: \"[DIVERGENCE] R2 SHOULD-FIX(循环论证: 纳入taxonomy→测试→观察相似pattern→论证纳入合理性). R1 REBUT(操作性定义有效, 文献支撑不仅是 co-occurrence, 改名 'policy specification defects' 会切断 NLP ambiguity 文献联系). 共识: §3 'Scope of ambiguity' 段落需更清晰区分 linguistic ambiguity(狭义) 和 specification ambiguity(广义)\"\n  action_items:\n    - round: 11\n      action: \"(1) §3 扩展 Scope of ambiguity 段落, 更清晰区分 linguistic ambiguity vs specification ambiguity; (2) 正面回应 incompleteness=information absence 和 cond.prec.=normative conflict 的理论张力; (3) 强化 RE 文献支撑(Berry et al. 2004 广义分类, Dalpiaz et al. 2018)\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-W2\"\n  summary: \"Disambiguation Neglect 新颖性被高估——已有文献(Liu 2023, Hu 2025)的 domain application 不应列为 primary contribution\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 9\n  last_seen_round: 11\n  mentions:\n    - round: 10\n      reviewers: [R2, R1]\n      note: \"术语从 Deficit 改为 Neglect, 需在定义中明确 uninstructed default\"\n    - round: 11\n      reviewers: [R2, R1]\n      note: \"R2 SHOULD-FIX, R1 AGREE. Liu et al. (2023) 已证明 LLMs collapse interpretations, Hu et al. (2025) 论证 missing conceptual representations. 本文增量是 agent policy 场景中量化(4.6% awareness). 共识: 重新定位为 '在 agent policy 场景中对已知现象的首次量化', 降低 contribution statement 权重\"\n  action_items:\n    - round: 11\n      action: \"Contribution (3) 重新措辞: 强调场景特异性和量化贡献(4.6% awareness in agent policy execution), 而非暗示发现新现象\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-W3\"\n  summary: \"Differential Nocuity 框架增量贡献有限——Berry & Kamsties (2004)/Willis et al. (2008) 已隐含 type-dependent risk\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 9\n  last_seen_round: 11\n  mentions:\n    - round: 10\n      reviewers: [R2, R1]\n      note: \"定位为已有概念在 LLM agent 领域的验证和扩展\"\n    - round: 11\n      reviewers: [R2, R1]\n      note: \"R2 SHOULD-FIX, R1 AGREE. Berry & Kamsties (2004) nocuous/innocuous 已隐含 type-dependent risk, Willis et al. (2008) 已研究 nocuity degree. 共识: 定位为 'empirical validation of differential nocuity in LLM agents' 而非 'proposing a differential nocuity framework'\"\n  action_items:\n    - round: 11\n      action: \"§7 第一段改为 'empirical validation' 定位, 明确 credit Willis et al. (2008) 的 prior type-specific nocuity measurement\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-W4\"\n  summary: \"Clause identity 22.4% variance 被误述为 type identity——clause(300个) ≠ type(6个)\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [R2, R1]\n      note: \"R2 SHOULD-FIX(W4c), R1 AGREE. §5.1 明确写 'Clause identity explains 22.4%', 是 300 clause pair 的 random effect 非 6 type 的 fixed effect. Introduction contribution (2) 如果用了 'type identity' 则是实质性错误. 如报告 type fixed effect variance, 数字会小得多\"\n  action_items:\n    - round: 11\n      action: \"(1) Introduction contribution (2) 修正为 'clause identity'; (2) 考虑补充 type fixed effect 的 variance explained 以区分两个概念\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-W5\"\n  summary: \"SESOI ±15pp 论证存在循环性——measurement noise criterion ≠ practical significance criterion\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [R1, R2]\n      note: \"R1 SHOULD-FIX, R2 AGREE(但指出 7-margin 敏感性分析和 margin-free bootstrap 部分缓解). '≥15pp warrants distinct policy handling' 用结论论证前提; 'exceeds perturbation bound by >2×' 是测量标准非实质标准. 在安全场景下 ±15pp 相当宽松\"\n  action_items:\n    - round: 11\n      action: \"(1) 从部署角度做实质论证(如 1000 interactions/day, 15pp = 150 extra violations/day); (2) 或将 ±10pp 和 ±15pp 并列为 primary results 展示 C2 差异\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-W6\"\n  summary: \"Cross-judge 仅用 OpenAI 家族模型(GPT-5.4/GPT-4.1), 可能存在 correlated type-specific bias\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 11\n  mentions:\n    - round: 10\n      reviewers: [R1, R2]\n      note: \"Within-judge-group C3 各自未达显著\"\n    - round: 11\n      reviewers: [R1, R2]\n      note: \"R1 SHOULD-FIX, R2 AGREE(区分影响范围: C1/C2 的 within-pair Δpp 中 judge bias 被消除, 真正受影响的是 C4). 差值消除假设在 type-specific correlated bias 下不成立. 建议 Limitations 增加 single-family judge bias 讨论\"\n  action_items:\n    - round: 11\n      action: \"(1) Limitations 增加 single-family judge bias 讨论; (2) 如有资源, 用非 OpenAI judge 对 subset 评估; (3) 明确哪些 claims 受 judge bias 影响(C4) vs 不受影响(C1/C2 Δpp)\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-W7\"\n  summary: \"Per-type 人工验证样本量偏小(n=32-34/type), scopal CI [0.00, 1.00] 无信息\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 11\n  mentions:\n    - round: 10\n      reviewers: [R1, R2]\n      note: \"正文 §4.4 明确标注 per-type κ 不具类型间比较价值\"\n    - round: 11\n      reviewers: [R1, R2]\n      note: \"R1 SHOULD-FIX, R2 AGREE. Type-level claims (C2-C4) 的有效性依赖对自动 judge 的 type-level 信任, 但 auth scope κ=0.385 表明此信任脆弱. 建议增大至每类 80-100 或在 Limitations 更强调 validation gap\"\n  action_items:\n    - round: 11\n      action: \"(1) 如有资源增大 human validation 至每类 ≥80; (2) 否则在 Limitations 更强调 type-level claims 的 validation gap\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# MINOR ISSUES\n# ============================================================\n\n- id: \"R11-M1\"\n  summary: \"Discussion(§7) vs Appendix B(Table 4) 的 mitigation 数字不一致, 两个实验未明确区分\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [R1, R2]\n      note: \"R1 MINOR(W6), R2 AGREE(确认为两个不同实验: §7 是 n=50/GPT-5.4/generic+type-specific, Appendix B 是 1256 episodes/5 models/type-specific only). 论文未明确说明两者关系. GPT-5.4 incompleteness: §7 报 +14pp vs Table 4 报 −2.6pp; auth scope: §7 报 −12pp vs Table 4 报 −40.0pp\"\n  action_items:\n    - round: 11\n      action: \"明确标注 §7 和 Appendix B 是两个独立实验, 说明 prompt 设计和数据差异\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-M2\"\n  summary: \"Mitigation p=0.118 的 confabulation 因果解释过度——non-significant trend 不应用确定性语言\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [R2, R1]\n      note: \"R2 MINOR(W7), R1 AGREE. §7 用 'triggers confabulation rather than caution' 解释 p=0.118 的非显著趋势, 属于过度解读. 应标注为 non-significant trend 并降低解释确定性\"\n  action_items:\n    - round: 11\n      action: \"§7 将 incompleteness worsening 标注为 non-significant trend, 降低因果解释的确定性\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-M3\"\n  summary: \"Abstract 'risk gradient' vs §5.2 'two-tier structure' 术语不一致\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [R2, R1]\n      note: \"R2 W4(a), R1 AGREE. 'Gradient' 暗示连续变化, 'two-tier' 暗示离散分层, 两个措辞不一致. 应统一术语\"\n  action_items:\n    - round: 11\n      action: \"统一 Abstract 和正文的 C2 术语, 采用一致表述(如 'risk gradient with incompleteness consistently highest')\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-M4\"\n  summary: \"Coreferential 被排除在 mitigation 和 replication 之外, 削弱 taxonomy 完整性\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 9\n  last_seen_round: 11\n  mentions:\n    - round: 10\n      reviewers: [R1, R2]\n      note: \"排除理由需更充分解释\"\n    - round: 11\n      reviewers: [R2, R1]\n      note: \"R2 MINOR(W6), R1 AGREE. Appendix B 技术原因合理, 但 6 类 taxonomy 中 1 类在两个重要实验中缺席影响完整性声明. Limitations 未提及此点\"\n  action_items:\n    - round: 11\n      action: \"Limitations 中提及 coreferential 排除对 taxonomy 完整性的影响\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-M5\"\n  summary: \"Domain 泛化性有限——仅覆盖零售/航空客服\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 8\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [R1, R2]\n      note: \"R1 MINOR(W7), R2 AGREE. 医疗/金融/法律领域可能产生不同类型层级. Limitations 已提及但较简短\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-M6\"\n  summary: \"Reproducibility ICC=0.919 仅覆盖 OpenAI 模型族, 跨 provider 稳定性未测量\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 8\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [R1]\n      note: \"R1 Q4 提出应报告 cross-provider ICC. R2 指出 judge/provider 效应不可分离, 应说明而非省略\"\n  action_items:\n    - round: 11\n      action: \"讨论 cross-provider ICC 的 confound 并解释未报告的原因\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-M7\"\n  summary: \"Pages 4-5 连续纯文本无 display item(视觉审查)\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 9\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: []\n      note: \"视觉审查: 连续两页纯文本(Method + early Results), 建议 §4 添加模型/数据集汇总表\"\n  action_items:\n    - round: 11\n      action: \"§4 添加一个 models × parameters × training philosophy 汇总表打破纯文本节奏\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# PREVIOUSLY RESOLVED (confirmed in Round 11)\n# ============================================================\n\n- id: \"R8-W1-resolved\"\n  summary: \"缺少 API 超参数报告\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: []\n      note: \"§4.3 reports temperature=0, top_p=1, max_tokens=4096. 本轮未提及\"\n  resolution: \"§4.3 添加完整 API 超参数\"\n  resolution_round: 9\n\n- id: \"R8-W4-resolved\"\n  summary: \"无代码/数据可用性声明\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: []\n      note: \"Data and Code Availability section 已存在. 本轮未提及\"\n  resolution: \"添加 Data and Code Availability section\"\n  resolution_round: 9\n\n- id: \"R9-W7-resolved\"\n  summary: \"多重比较校正 three test families 未明确定义\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: []\n      note: \"Appendix L 已明确列出 3 families. 本轮未提及\"\n  resolution: \"Appendix L 新增 Multiple Comparison Correction 小节\"\n  resolution_round: 10\n\n- id: \"R9-W8-resolved\"\n  summary: \"与 DRIP-R 的 taxonomy type-level 映射缺失\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: []\n      note: \"Appendix L 有 DRIP-R mapping. 本轮未提及\"\n  resolution: \"Appendix L 新增 DRIP-R Category Mapping\"\n  resolution_round: 10\n\n- id: \"R9-M3-resolved\"\n  summary: \"Introduction 'seven models' 措辞应区分 main study (5) vs replication (2)\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: []\n      note: \"§1 已改为 'five primary models and confirmed in two additional replication models'. 本轮未提及\"\n  resolution: \"措辞已修正\"\n  resolution_round: 10\n\n- id: \"R9-M7-resolved\"\n  summary: \"§5.4 F(20) 缺少 denominator df\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: []\n      note: \"§5.4 已改为 F(20, 2976). 本轮未提及\"\n  resolution: \"F(20) → F(20, 2976)\"\n  resolution_round: 10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "policy_ambiguity_safety",
    "issues_yaml": "## Round 11 (Fresh) Review Issues — policy_ambiguity_safety\n## Paper: \"Not All Policy Ambiguity Is Equal: Type-Specific Safety Risks for LLM Agents\"\n## Venue: EMNLP 2026 via ARR May cycle\n## Date: 2026-05-22\n## Round 11 Score: 3.5 (Borderline Conference)\n## Note: Fresh review session — all issues re-evaluated from scratch\n\n# ============================================================\n# CRITICAL ISSUES\n# ============================================================\n\n- id: \"R11-C1\"\n  summary: \"Authorization scope κ=0.385 不足以支撑 C4 中 52pp range 作为 numbered claim\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 8\n  last_seen_round: 11\n  mentions:\n    - round: 10\n      reviewers: [R1, R2]\n      note: \"两人完全共识: κ=0.385 低于 fair agreement 门槛(0.40), 52pp 中真实差异 vs noise 无法分离\"\n    - round: 11\n      reviewers: [R1, R2]\n      note: \"R1 MUST-FIX, R2 AGREE(建议降为 SHOULD-FIX 因 C4 已标 Exploratory). 共识三层问题: (1) cross-judge κ vs human-LLM κ 混淆, (2) within-judge stability 不能弥补 cross-judge 不一致, (3) Appendix P ρ=−0.03 的 agent composition vs judge bias 不可分离. 建议计算 PABAK/Gwet's AC1, 将 C4 降级为 Discussion observation, abstract/conclusion 不引用 52pp 具体数字\"\n  action_items:\n    - round: 11\n      action: \"(1) 计算 auth scope 的 PABAK 或 Gwet's AC1 区分 prevalence paradox 和真实分歧; (2) C4 从 numbered claim 降级为 Discussion observation; (3) Abstract/Conclusion 中 52pp 改为定性描述; (4) Section 5.4 明确区分 cross-judge κ=0.385 和 human-LLM κ=0.644 的数据来源\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-C2\"\n  summary: \"C2 two-tier hierarchy 表述强度超过证据——bootstrap 34.3%, Kendall's W=0.398 不显著, margin-dependent\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 8\n  last_seen_round: 11\n  mentions:\n    - round: 10\n      reviewers: [R1, R2]\n      note: \"Bootstrap AU p=0.47, ±10pp 仅 3/6 mid-tier pairs 等价, Kendall's W=0.398(p=0.072) 不显著\"\n    - round: 11\n      reviewers: [R1, R2]\n      note: \"R1 SHOULD-FIX, R2 AGREE. 四个制约因素完全共识. R2 REBUT R1 sub-point(4): coreferential 31.6% 是 confound-free lower bound 非 incompleteness adjusted effect(logistic regression p=0.018 仍显著). 共识: incompleteness upper bound 稳健(7 模型 ≥46%), 但 two-tier 表述需弱化为 'incompleteness consistently separates as highest-violation type, remaining types form less differentiated cluster at ±15pp margin'\"\n  action_items:\n    - round: 11\n      action: \"(1) Abstract/Intro/Conclusion 措辞弱化, 不用 'two-tier hierarchy'; (2) 正文并列呈现 ±10pp 和 ±15pp 结果; (3) 报告 AU p-value 在正文而非仅 Appendix; (4) 明确承认 margin 依赖性和 bootstrap 不稳定性\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# WARNING ISSUES\n# ============================================================\n\n- id: \"R11-W1\"\n  summary: \"Taxonomy 理论基础: incompleteness 和 conditional precedence 不满足 strict ambiguity 定义, §3 论证需扩展\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 9\n  last_seen_round: 11\n  mentions:\n    - round: 10\n      reviewers: [R2, R1]\n      note: \"R2 SHOULD-FIX, R1 部分 REBUT. 需要在 §3 中更充分讨论理论边界\"\n    - round: 11\n      reviewers: [R2, R1]\n      note: \"[DIVERGENCE] R2 SHOULD-FIX(循环论证: 纳入taxonomy→测试→观察相似pattern→论证纳入合理性). R1 REBUT(操作性定义有效, 文献支撑不仅是 co-occurrence, 改名 'policy specification defects' 会切断 NLP ambiguity 文献联系). 共识: §3 'Scope of ambiguity' 段落需更清晰区分 linguistic ambiguity(狭义) 和 specification ambiguity(广义)\"\n  action_items:\n    - round: 11\n      action: \"(1) §3 扩展 Scope of ambiguity 段落, 更清晰区分 linguistic ambiguity vs specification ambiguity; (2) 正面回应 incompleteness=information absence 和 cond.prec.=normative conflict 的理论张力; (3) 强化 RE 文献支撑(Berry et al. 2004 广义分类, Dalpiaz et al. 2018)\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-W2\"\n  summary: \"Disambiguation Neglect 新颖性被高估——已有文献(Liu 2023, Hu 2025)的 domain application 不应列为 primary contribution\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 9\n  last_seen_round: 11\n  mentions:\n    - round: 10\n      reviewers: [R2, R1]\n      note: \"术语从 Deficit 改为 Neglect, 需在定义中明确 uninstructed default\"\n    - round: 11\n      reviewers: [R2, R1]\n      note: \"R2 SHOULD-FIX, R1 AGREE. Liu et al. (2023) 已证明 LLMs collapse interpretations, Hu et al. (2025) 论证 missing conceptual representations. 本文增量是 agent policy 场景中量化(4.6% awareness). 共识: 重新定位为 '在 agent policy 场景中对已知现象的首次量化', 降低 contribution statement 权重\"\n  action_items:\n    - round: 11\n      action: \"Contribution (3) 重新措辞: 强调场景特异性和量化贡献(4.6% awareness in agent policy execution), 而非暗示发现新现象\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-W3\"\n  summary: \"Differential Nocuity 框架增量贡献有限——Berry & Kamsties (2004)/Willis et al. (2008) 已隐含 type-dependent risk\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 9\n  last_seen_round: 11\n  mentions:\n    - round: 10\n      reviewers: [R2, R1]\n      note: \"定位为已有概念在 LLM agent 领域的验证和扩展\"\n    - round: 11\n      reviewers: [R2, R1]\n      note: \"R2 SHOULD-FIX, R1 AGREE. Berry & Kamsties (2004) nocuous/innocuous 已隐含 type-dependent risk, Willis et al. (2008) 已研究 nocuity degree. 共识: 定位为 'empirical validation of differential nocuity in LLM agents' 而非 'proposing a differential nocuity framework'\"\n  action_items:\n    - round: 11\n      action: \"§7 第一段改为 'empirical validation' 定位, 明确 credit Willis et al. (2008) 的 prior type-specific nocuity measurement\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-W4\"\n  summary: \"Clause identity 22.4% variance 被误述为 type identity——clause(300个) ≠ type(6个)\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [R2, R1]\n      note: \"R2 SHOULD-FIX(W4c), R1 AGREE. §5.1 明确写 'Clause identity explains 22.4%', 是 300 clause pair 的 random effect 非 6 type 的 fixed effect. Introduction contribution (2) 如果用了 'type identity' 则是实质性错误. 如报告 type fixed effect variance, 数字会小得多\"\n  action_items:\n    - round: 11\n      action: \"(1) Introduction contribution (2) 修正为 'clause identity'; (2) 考虑补充 type fixed effect 的 variance explained 以区分两个概念\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-W5\"\n  summary: \"SESOI ±15pp 论证存在循环性——measurement noise criterion ≠ practical significance criterion\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [R1, R2]\n      note: \"R1 SHOULD-FIX, R2 AGREE(但指出 7-margin 敏感性分析和 margin-free bootstrap 部分缓解). '≥15pp warrants distinct policy handling' 用结论论证前提; 'exceeds perturbation bound by >2×' 是测量标准非实质标准. 在安全场景下 ±15pp 相当宽松\"\n  action_items:\n    - round: 11\n      action: \"(1) 从部署角度做实质论证(如 1000 interactions/day, 15pp = 150 extra violations/day); (2) 或将 ±10pp 和 ±15pp 并列为 primary results 展示 C2 差异\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-W6\"\n  summary: \"Cross-judge 仅用 OpenAI 家族模型(GPT-5.4/GPT-4.1), 可能存在 correlated type-specific bias\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 11\n  mentions:\n    - round: 10\n      reviewers: [R1, R2]\n      note: \"Within-judge-group C3 各自未达显著\"\n    - round: 11\n      reviewers: [R1, R2]\n      note: \"R1 SHOULD-FIX, R2 AGREE(区分影响范围: C1/C2 的 within-pair Δpp 中 judge bias 被消除, 真正受影响的是 C4). 差值消除假设在 type-specific correlated bias 下不成立. 建议 Limitations 增加 single-family judge bias 讨论\"\n  action_items:\n    - round: 11\n      action: \"(1) Limitations 增加 single-family judge bias 讨论; (2) 如有资源, 用非 OpenAI judge 对 subset 评估; (3) 明确哪些 claims 受 judge bias 影响(C4) vs 不受影响(C1/C2 Δpp)\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-W7\"\n  summary: \"Per-type 人工验证样本量偏小(n=32-34/type), scopal CI [0.00, 1.00] 无信息\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 11\n  mentions:\n    - round: 10\n      reviewers: [R1, R2]\n      note: \"正文 §4.4 明确标注 per-type κ 不具类型间比较价值\"\n    - round: 11\n      reviewers: [R1, R2]\n      note: \"R1 SHOULD-FIX, R2 AGREE. Type-level claims (C2-C4) 的有效性依赖对自动 judge 的 type-level 信任, 但 auth scope κ=0.385 表明此信任脆弱. 建议增大至每类 80-100 或在 Limitations 更强调 validation gap\"\n  action_items:\n    - round: 11\n      action: \"(1) 如有资源增大 human validation 至每类 ≥80; (2) 否则在 Limitations 更强调 type-level claims 的 validation gap\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# MINOR ISSUES\n# ============================================================\n\n- id: \"R11-M1\"\n  summary: \"Discussion(§7) vs Appendix B(Table 4) 的 mitigation 数字不一致, 两个实验未明确区分\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [R1, R2]\n      note: \"R1 MINOR(W6), R2 AGREE(确认为两个不同实验: §7 是 n=50/GPT-5.4/generic+type-specific, Appendix B 是 1256 episodes/5 models/type-specific only). 论文未明确说明两者关系. GPT-5.4 incompleteness: §7 报 +14pp vs Table 4 报 −2.6pp; auth scope: §7 报 −12pp vs Table 4 报 −40.0pp\"\n  action_items:\n    - round: 11\n      action: \"明确标注 §7 和 Appendix B 是两个独立实验, 说明 prompt 设计和数据差异\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-M2\"\n  summary: \"Mitigation p=0.118 的 confabulation 因果解释过度——non-significant trend 不应用确定性语言\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [R2, R1]\n      note: \"R2 MINOR(W7), R1 AGREE. §7 用 'triggers confabulation rather than caution' 解释 p=0.118 的非显著趋势, 属于过度解读. 应标注为 non-significant trend 并降低解释确定性\"\n  action_items:\n    - round: 11\n      action: \"§7 将 incompleteness worsening 标注为 non-significant trend, 降低因果解释的确定性\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-M3\"\n  summary: \"Abstract 'risk gradient' vs §5.2 'two-tier structure' 术语不一致\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [R2, R1]\n      note: \"R2 W4(a), R1 AGREE. 'Gradient' 暗示连续变化, 'two-tier' 暗示离散分层, 两个措辞不一致. 应统一术语\"\n  action_items:\n    - round: 11\n      action: \"统一 Abstract 和正文的 C2 术语, 采用一致表述(如 'risk gradient with incompleteness consistently highest')\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-M4\"\n  summary: \"Coreferential 被排除在 mitigation 和 replication 之外, 削弱 taxonomy 完整性\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 9\n  last_seen_round: 11\n  mentions:\n    - round: 10\n      reviewers: [R1, R2]\n      note: \"排除理由需更充分解释\"\n    - round: 11\n      reviewers: [R2, R1]\n      note: \"R2 MINOR(W6), R1 AGREE. Appendix B 技术原因合理, 但 6 类 taxonomy 中 1 类在两个重要实验中缺席影响完整性声明. Limitations 未提及此点\"\n  action_items:\n    - round: 11\n      action: \"Limitations 中提及 coreferential 排除对 taxonomy 完整性的影响\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-M5\"\n  summary: \"Domain 泛化性有限——仅覆盖零售/航空客服\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 8\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [R1, R2]\n      note: \"R1 MINOR(W7), R2 AGREE. 医疗/金融/法律领域可能产生不同类型层级. Limitations 已提及但较简短\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-M6\"\n  summary: \"Reproducibility ICC=0.919 仅覆盖 OpenAI 模型族, 跨 provider 稳定性未测量\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 8\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [R1]\n      note: \"R1 Q4 提出应报告 cross-provider ICC. R2 指出 judge/provider 效应不可分离, 应说明而非省略\"\n  action_items:\n    - round: 11\n      action: \"讨论 cross-provider ICC 的 confound 并解释未报告的原因\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-M7\"\n  summary: \"Pages 4-5 连续纯文本无 display item(视觉审查)\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 9\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: []\n      note: \"视觉审查: 连续两页纯文本(Method + early Results), 建议 §4 添加模型/数据集汇总表\"\n  action_items:\n    - round: 11\n      action: \"§4 添加一个 models × parameters × training philosophy 汇总表打破纯文本节奏\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# PREVIOUSLY RESOLVED (confirmed in Round 11)\n# ============================================================\n\n- id: \"R8-W1-resolved\"\n  summary: \"缺少 API 超参数报告\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: []\n      note: \"§4.3 reports temperature=0, top_p=1, max_tokens=4096. 本轮未提及\"\n  resolution: \"§4.3 添加完整 API 超参数\"\n  resolution_round: 9\n\n- id: \"R8-W4-resolved\"\n  summary: \"无代码/数据可用性声明\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: []\n      note: \"Data and Code Availability section 已存在. 本轮未提及\"\n  resolution: \"添加 Data and Code Availability section\"\n  resolution_round: 9\n\n- id: \"R9-W7-resolved\"\n  summary: \"多重比较校正 three test families 未明确定义\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: []\n      note: \"Appendix L 已明确列出 3 families. 本轮未提及\"\n  resolution: \"Appendix L 新增 Multiple Comparison Correction 小节\"\n  resolution_round: 10\n\n- id: \"R9-W8-resolved\"\n  summary: \"与 DRIP-R 的 taxonomy type-level 映射缺失\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: []\n      note: \"Appendix L 有 DRIP-R mapping. 本轮未提及\"\n  resolution: \"Appendix L 新增 DRIP-R Category Mapping\"\n  resolution_round: 10\n\n- id: \"R9-M3-resolved\"\n  summary: \"Introduction 'seven models' 措辞应区分 main study (5) vs replication (2)\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: []\n      note: \"§1 已改为 'five primary models and confirmed in two additional replication models'. 本轮未提及\"\n  resolution: \"措辞已修正\"\n  resolution_round: 10\n\n- id: \"R9-M7-resolved\"\n  summary: \"§5.4 F(20) 缺少 denominator df\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: []\n      note: \"§5.4 已改为 F(20, 2976). 本轮未提及\"\n  resolution: \"F(20) → F(20, 2976)\"\n  resolution_round: 10"
  }
}
```

</details>

---


### Tool result

_source line 989 · 2026-05-22T08:54:11.731913+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_issues.yaml\", \"bytes\": 14784}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 103
}
```

</details>

---


### Tool call

_source line 990 · 2026-05-22T08:57:00.557069+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# Round 11 审稿报告 — policy_ambiguity_safety\n\n**论文**: \"Not All Policy Ambiguity Is Equal: Type-Specific Safety Risks for LLM Agents\"\n**Venue**: EMNLP 2026 via ARR May cycle\n**审稿模式**: Fresh（重新审稿）\n**Reviewer 编排**: 2 人（R1: 方法严谨性, R2: 新颖性/完整性）\n**轮次**: 1 轮（交叉分享后关键问题达成共识，无需第二轮）\n\n---\n\n## Summary\n\n本文研究 LLM agent 在自然语言策略规范下因歧义类型不同而产生的安全违规差异。采用 matched-pair 因果设计，在 τ²-bench 上构建 300 对歧义/消歧 clause pair（六类歧义 taxonomy），跨 5 个模型（2,997 episodes）评估。主要发现：(1) 歧义条款使违规率增加 34.0pp（OR=15.1）；(2) incompleteness 一致排名最高（46-62%），其余五类呈现 risk gradient；(3) error analysis 揭示 Disambiguation Neglect（≤11% awareness）和 systematic nocuity（41.3% clauses 触发模型趋同违规）。\n\n---\n\n## Strengths\n\n**S1. 首个因果性 ambiguity→violation 类型映射 [共识]。** Matched-pair design + perturbation control（Δ_perturb = −0.67pp, CI 包含零）在 NLP agent safety 领域确属创新。与 DRIP-R（correlational）、PolicyBank（iterative refinement）、AgentPex（trace detection）的差异化清晰且准确。C1 证据充分（OR=15.1, 7 模型一致, p < 10⁻¹⁰⁵），因果推断具有说服力。\n\n**S2. 统计方法论异常充分 [共识]。** McNemar + TOST equivalence（7 margin 敏感性）+ margin-free bootstrap cluster + Holm-Bonferroni 三组校正 + post-hoc 功效分析（C1/C2 power > 0.99）。在该子领域中不常见且值得肯定。对 SESOI 的 domain-anchored justification 和 margin dependence 的 acknowledgment 体现方法论自觉。\n\n**S3. Claim 标定诚实 [共识]。** C3 明确标注为 inconclusive（未通过 Holm-Bonferroni），C4 标注 [Exploratory]，authorization scope κ=0.385 在全文五处反复标注，incompleteness confound 多层控制（logistic regression, coreferential lower bound, sans-incompleteness analysis）。\n\n**S4. Error analysis 有实质洞见 [共识]。** 三种 failure mechanism（structural misparse, information gap-filling, boundary violation）与 ambiguity type 的对应关系超越聚合统计。Systematic nocuity（41.3% majority-convergent violations）揭示 agreement-based evaluation 盲区。\n\n**S5. 实验规模与覆盖度 [共识]。** 5+2 models, 6 providers, 2997 episodes, 覆盖 proprietary/open-source/dense/MoE。Replication 在独立 model families 上确认 C1 和 C2。\n\n---\n\n## Weaknesses\n\n### MUST-FIX\n\n**W1. Authorization scope κ=0.385 严重削弱 C4（52pp range claim）[R1 MUST-FIX, R2 AGREE]**\n\nAuthorization scope 的 cross-judge κ 仅 0.385（低于 fair agreement 门槛 0.40），是所有类型中最低的。C4 的核心发现——52pp cross-model range（Claude 12% → GPT-5.4 64%）——正是基于这个最不可靠的类型。三层问题：\n\n(1) Cross-judge κ=0.385 与 human-LLM κ=0.644（Appendix G）是不同指标，§5.4 引用 \"raw agreement 85.3%\" 时数据来源不明确，读者可能混淆。\n(2) Within-judge bootstrap ranking preservation（99.5%）仅证明单个 judge 内部一致性，无法弥补 cross-judge 不一致——稳定偏差仍是偏差。\n(3) Appendix P within-judge-group type ranking ρ=−0.03（p=0.96），auth scope rank reversal（GPT-4.1 judged: rank 1 vs GPT-5.4 judged: rank 6）中 agent composition 和 judge bias 不可分离。\n\n**修改要求**: (a) 计算 auth scope 的 PABAK 或 Gwet's AC1 区分 prevalence paradox 和真实分歧；(b) C4 从 numbered claim 降级为 Discussion observation；(c) Abstract/Conclusion 中 52pp 改为定性描述；(d) §5.4 明确区分 cross-judge κ 和 human-LLM κ 的数据来源。\n\n### SHOULD-FIX\n\n**W2. C2 \"two-tier hierarchy\" 表述强度超过证据 [R1 SHOULD-FIX, R2 AGREE]**\n\n\"Two-tier hierarchy\" 暗示稳定的层级结构，但实际受四个因素制约：(1) ±10pp 仅 3/6 mid-tier pairs equivalent, TOST power 降至 0.57；(2) Bootstrap incompleteness singleton 仅 34.3% 重现, AU p=0.47；(3) Kendall's W=0.398 (p=0.072) 不显著；(4) Incompleteness upper bound 稳健（7 模型 ≥46%），但 mid-tier cohesion 是 margin-dependent 的。\n\nR2 REBUT R1 sub-point：coreferential 31.6% 是 confound-free lower bound 非 incompleteness adjusted effect（logistic regression 控制 token delta 后 incompleteness 仍显著 p=0.018）——不应将 31.6% 视为 incompleteness 的 adjusted rate。\n\n**修改要求**: 弱化为 \"incompleteness consistently separates as the highest-violation type; the remaining types form a less differentiated cluster at the ±15pp equivalence margin, though this structure is margin-dependent\"。正文报告 AU p-value，明确承认 bootstrap 不稳定性。\n\n**W3. Taxonomy 理论基础：§3 \"Scope of ambiguity\" 需扩展 [R2 SHOULD-FIX, R1 partial REBUT — DIVERGENCE]**\n\nR2 认为 incompleteness（information absence）和 conditional precedence（normative conflict）不满足 strict ambiguity 定义，§3 的论证存在循环（纳入 taxonomy → 测试 → 观察相似 pattern → 论证纳入合理性）。R1 反驳称操作性定义有效且有 RE 文献支撑（Berry et al. 2004 广义分类、Dalpiaz et al. 2018 共现研究、Li et al. 2024 11-type taxonomy），改名 \"policy specification defects\" 会切断文献联系。\n\n**共识**: 无论对理论严重程度的判断如何，§3 需更清晰区分 linguistic ambiguity（狭义）和 specification ambiguity（广义），正面回应理论张力而非依赖读者接受操作性定义。\n\n**W4. Disambiguation Neglect 新颖性被高估 [R2 SHOULD-FIX, R1 AGREE]**\n\nIntroduction contribution (3) 将 Disambiguation Neglect 列为 primary contribution，但 Liu et al. (2023, EMNLP) 已证明 LLMs collapse interpretations, Hu et al. (2025) 论证 missing conceptual representations。本文增量是在 agent policy 场景中量化（4.6% awareness），应重新定位而非暗示发现新现象。\n\n**W5. Differential Nocuity 框架增量贡献有限 [R2 SHOULD-FIX, R1 AGREE]**\n\nBerry & Kamsties (2004) 的 nocuous/innocuous 二分法已隐含 type-dependent risk，Willis et al. (2008) 已研究 nocuity degree。§7 的命名暗示新 framework，应定位为 \"empirical validation of differential nocuity in LLM agents\"。\n\n**W6. Clause identity 22.4% variance 被误述为 type identity [R2 SHOULD-FIX, R1 AGREE]**\n\n§5.1 明确写 \"Clause identity explains 22.4% of variance\"——这是 300 clause pair 的 random effect，非 6 type 的 fixed effect。Introduction contribution (2) 的 \"type identity explaining 22× more variance\" 措辞具有误导性。Clause identity ≠ type identity，前者主要反映 clause-level heterogeneity。\n\n**W7. SESOI ±15pp 论证存在循环性 [R1 SHOULD-FIX, R2 AGREE]**\n\n\"≥15pp warrants distinct policy handling\" 用结论论证前提；\"exceeds perturbation bound by >2×\" 是测量噪声标准非实质性差异标准。在安全场景下 ±15pp 相当宽松。好的一面是提供了 7-margin 敏感性分析 + margin-free bootstrap 作为补充。建议从部署角度做实质论证。\n\n**W8. Cross-judge 仅用 OpenAI 家族模型 [R1 SHOULD-FIX, R2 AGREE]**\n\nGPT-5.4/GPT-4.1 可能共享 type-specific correlated bias。R2 补充区分影响范围：C1/C2 的 within-pair Δpp 中 judge bias 被消除（对差值安全），C4 的 cross-model absolute rate comparison 受影响。Limitations 应增加讨论。\n\n**W9. Human validation n=32-34/type 不足以支撑 type-level claims [R1 SHOULD-FIX, R2 AGREE]**\n\nScopal CI [0.00, 1.00], coreferential CI [0.00, 0.84] 完全无信息。Type-level claims (C2-C4) 的有效性依赖对自动 judge 的 type-level 信任——但 auth scope κ=0.385 表明此信任在至少一个类型上脆弱。\n\n### MINOR\n\n**W10. Discussion vs Appendix B 的 mitigation 数字不一致 [R1 MINOR, R2 AGREE]**\n\n§7 报告 GPT-5.4 incompleteness +14pp (p=0.118), auth scope −12pp (p=0.070)；Table 4 同模型同类型分别为 −2.6pp 和 −40.0pp。确认为两个不同实验（§7: n=50/GPT-5.4/generic+type-specific; Appendix B: 1,256 episodes/5 models/type-specific only），但论文未明确说明两者关系。\n\n**W11. Mitigation incompleteness worsening (+14pp, p=0.118) 的因果解释过度 [R2 MINOR, R1 AGREE]**\n\n§7 用确定性语言 \"triggers confabulation rather than caution\" 解释非显著趋势（p=0.118）。应标注为 non-significant trend 并降低解释确定性。\n\n**W12. Abstract \"risk gradient\" vs §5.2 \"two-tier structure\" 术语不一致 [R2 MINOR, R1 AGREE]**\n\n\"Gradient\" 暗示连续变化，\"two-tier\" 暗示离散分层。应统一术语。\n\n**W13. Coreferential 被排除在 mitigation 和 replication 之外 [R2 MINOR, R1 AGREE]**\n\n技术原因合理（Appendix B），但 6 类 taxonomy 中 1 类在两个重要实验中完全缺席影响完整性声明。Limitations 未提及此点。\n\n**W14. Domain 泛化性有限 [R1 MINOR, R2 AGREE]**\n\nτ²-bench 仅覆盖零售/航空客服。医疗/金融/法律领域可能产生不同的类型层级。\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 达成完全共识 [AGREE]：\n\n1. **C1 证据充分**（OR=15.1, 7 模型一致），matched-pair 因果设计是本文最大贡献\n2. **Auth scope κ=0.385 削弱 C4**: 52pp range 基于最低 reliability 类型, 应降级或重度 caveat\n3. **C2 表述过强**: \"two-tier hierarchy\" 在 bootstrap 中仅 34.3% 稳定, Kendall's W 不显著, margin-dependent\n4. **Clause vs type identity**: 22.4% variance 是 clause random effect 非 type fixed effect, contribution (2) 措辞误导\n5. **Disambiguation Neglect 新颖性**: 已有文献记录的现象在新场景中的量化, 非新发现\n6. **Differential Nocuity 增量**: empirical validation 而非新 framework\n7. **Mitigation 数字不一致**: §7 和 Appendix B 是两个不同实验, 需明确区分\n8. **Mitigation over-interpretation**: p=0.118 不应用确定性因果语言\n9. **统计方法论优秀**: TOST + bootstrap + Holm-Bonferroni 在该领域罕见\n10. **Error analysis 有价值**: failure mechanism 对应和 systematic nocuity 提供机制理解\n\n## Reviewer Divergence\n\n**唯一实质分歧: Taxonomy 理论基础的严重程度**\n\n- **R2**: incompleteness/conditional precedence 不属于 ambiguity, §3 论证存在循环, 建议重新框架为 \"policy specification defects\" 或大幅扩展理论论证\n- **R1**: 操作性定义有效且有 RE 文献充分支撑（Berry et al. 2004, Dalpiaz et al. 2018, Li et al. 2024）, 改名会切断文献联系, 但同意 §3 讨论应更清晰\n\n**Review Director 判断**: 这是一个理论 framing 偏好问题而非 fatal flaw。论文的操作性定义有文献基础，但 §3 确实需要正面回应理论张力，而非仅依赖读者接受广义定义。按 SHOULD-FIX 处理，不升级为 MUST-FIX。\n\n---\n\n## Questions\n\n**Q1 [R2]**: Bootstrap AU p=0.47 如何与 \"incompleteness stands apart\" 的 confident framing 调和？\n\n**Q2 [R2]**: \"Clause identity explains 22.4% of variance\" 是 300 clause pair 的 random effect 还是 6 type 的 fixed effect？如果前者，contribution (2) 措辞需修正。\n\n**Q3 [R2]**: Temperature=0 下 ICC=0.919 的 8.1% variance 来自 API non-determinism 还是 episode-level randomness？\n\n**Q4 [R1]**: Auth scope cross-judge κ=0.385 的 raw agreement 是多少？可否计算 PABAK/AC1 区分 prevalence paradox？\n\n**Q5 [R1]**: Confound-adjusted effect size 重做 TOST，C2 是否仍成立？\n\n**Q6 [R1]**: Perturbation control 的修改量是否与 ambiguity perturbation 的 token-level 变化量匹配？\n\n**Q7 [R1]**: Kendall's W=0.398 (p=0.072) 不显著——除 incompleteness 外，type hierarchy 是否 model-dependent？\n\n---\n\n## Missing References\n\nR2 建议补充（R1 部分反驳）：\n- OpenAgentSafety (ICLR 2026) — comprehensive agent safety framework（如果提供 complementary perspective）\n- Agent-SafetyBench (2024) — 349 interactive environment agent safety benchmark（如果与已引用 agent safety 工作有实质差异）\n- Automated Repair of Ambiguous NL Requirements (2025, arxiv:2505.07270)\n\nR1 指出 Ferrari et al. (2019) \"Ambiguity in RE\" 应已被引用为 ferrari_ambiguity_2019。\n\n---\n\n## External Review\n\n外部审稿：未请求（项目配置未启用 `external_review.paperreview_ai.enabled`）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n状态: **done**（耗时 ~3.5 分钟）\n\n### Findings (0 critical, 2 warning, 8 info):\n\n**Warning:**\n- Pages 4-5: 连续两页纯文本（Method + early Results），无任何 display item 穿插。建议 §4 添加模型/数据集汇总表打破视觉单调。\n- Page 15: 最后一页 Appendix Q 仅 ~6 行内容，~90% 空白。建议合并到前一页或调整附录顺序。\n\n**Info:**\n- Page 2: Figure 1 左侧 taxonomy tree 叶节点标签字号偏小\n- Page 6-7: Figure 2/3 热力图单元格数值和 axis label 字号较小（约正文 60%），建议增大\n- Page 6: Table 2 booktabs 风格规范，最优值加粗\n- Page 3: Table 1 分类表排版清晰\n- Page 12: 附录含 6 个表格，密度极高但作为附录可接受\n- Page 6-7: 热力图 yellow-to-red 渐变基本 colorblind-safe\n- Page 9-10: 参考文献格式统一，无未解析引用\n\n---\n\n## Overall Assessment\n\n**评分: 3.5 / 5 (Borderline Conference)**\n**置信度: 4 / 5**\n**评分对应: ARR Overall Assessment 3.5 = Borderline Conference**\n\n### 核心判断\n\n这是一篇**方法论扎实的实证论文**。Matched-pair causal design + perturbation control 在 NLP agent safety 领域确属首创，C1（ambiguity → violation 因果效应，OR=15.1, 7 模型一致）证据充分，统计分析（TOST + bootstrap + Holm-Bonferroni）远超该子领域平均水平。Error analysis 中的 failure mechanism 类型对应和 systematic nocuity 发现有部署价值。\n\n### 阻碍 Conference 接收的问题\n\n1. **测量可靠性**: C4 基于最低 reliability 类型（auth scope κ=0.385）做 numbered claim；C2 的 \"two-tier hierarchy\" 在 bootstrap 中仅 34.3% 稳定，Kendall's W 不显著\n2. **Framing 校准**: clause vs type identity 的 22× claim 有误导性；Disambiguation Neglect 和 Differential Nocuity 的增量贡献被高估——它们是已有概念的 domain application 而非独立理论创新\n3. **SESOI 论证**: ±15pp 的实质性论证不足，影响 C2 的核心表述\n\n### 升级路径\n\n如果 revision 中：(1) 将 C4 降级为 Discussion observation 或补充 prevalence-adjusted agreement；(2) 弱化 C2 为 \"incompleteness consistently highest, remaining types form less differentiated cluster\"；(3) 修正 clause/type identity 归因；(4) 降低 coined terms 的 novelty claim——可升至 **4.0 (Conference)**。核心实证贡献（C1 + error analysis）已达 Conference 水平，framing 调整即可达标。\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- Contribution (2): \"type identity explaining 22× more variance\" 需修正为 \"clause identity\"，并补充 type fixed effect variance\n- 52pp range 的 caveat 权重不足——κ < 0.4 的维度上不应作为核心 finding 突出\n- Contribution (3) 降低 Disambiguation Neglect 的 novelty claim\n\n### §3 Taxonomy\n- \"Scope of ambiguity\" 段落需扩展：更清晰区分 linguistic ambiguity vs specification ambiguity，正面回应理论张力\n- 引用 Dalpiaz et al. (2018) 和 Berry et al. (2004) 的论证可以更充分\n\n### §4 Method\n- SESOI ±15pp: 增加部署场景论证或将 ±10pp 并列为 primary\n- Pages 4-5 考虑添加 model summary table 打破纯文本节奏\n\n### §5 Results\n- §5.2: \"two-tier structure\"/\"stands apart\" 弱化为更谨慎的表述，正文报告 AU p=0.47\n- §5.4: 明确区分 cross-judge κ=0.385 和 human-LLM κ=0.644 的数据来源\n- C4 降级为 Discussion observation 或在 abstract/conclusion 中不引用 52pp\n\n### §6 Analysis\n- §6.2: Disambiguation Neglect 定位为 \"已知现象在 agent policy 场景中的首次量化\"\n- Incompleteness wording 已较好但 §6.2 引用 good-enough processing 的 analogy 需加 mechanism-level caveat\n\n### §7 Discussion\n- Differential Nocuity: 改为 \"empirical validation\" 定位\n- Mitigation: (a) 明确标注 §7 和 Appendix B 是两个独立实验；(b) incompleteness +14pp (p=0.118) 标注为 non-significant trend\n- \"Abstract 'risk gradient' vs 正文 'two-tier'\" 术语统一\n\n### §8 Limitations\n- 增加 single-family judge bias 讨论\n- 提及 coreferential 排除对 taxonomy 完整性的影响\n- 更强调 type-level human validation gap",
  "project": "policy_ambiguity_safety",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.5 - Borderline Conference",
  "review_chat_id": "oc_967344d166ba485ad606d14379e69d85"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# Round 11 审稿报告 — policy_ambiguity_safety\n\n**论文**: \"Not All Policy Ambiguity Is Equal: Type-Specific Safety Risks for LLM Agents\"\n**Venue**: EMNLP 2026 via ARR May cycle\n**审稿模式**: Fresh（重新审稿）\n**Reviewer 编排**: 2 人（R1: 方法严谨性, R2: 新颖性/完整性）\n**轮次**: 1 轮（交叉分享后关键问题达成共识，无需第二轮）\n\n---\n\n## Summary\n\n本文研究 LLM agent 在自然语言策略规范下因歧义类型不同而产生的安全违规差异。采用 matched-pair 因果设计，在 τ²-bench 上构建 300 对歧义/消歧 clause pair（六类歧义 taxonomy），跨 5 个模型（2,997 episodes）评估。主要发现：(1) 歧义条款使违规率增加 34.0pp（OR=15.1）；(2) incompleteness 一致排名最高（46-62%），其余五类呈现 risk gradient；(3) error analysis 揭示 Disambiguation Neglect（≤11% awareness）和 systematic nocuity（41.3% clauses 触发模型趋同违规）。\n\n---\n\n## Strengths\n\n**S1. 首个因果性 ambiguity→violation 类型映射 [共识]。** Matched-pair design + perturbation control（Δ_perturb = −0.67pp, CI 包含零）在 NLP agent safety 领域确属创新。与 DRIP-R（correlational）、PolicyBank（iterative refinement）、AgentPex（trace detection）的差异化清晰且准确。C1 证据充分（OR=15.1, 7 模型一致, p < 10⁻¹⁰⁵），因果推断具有说服力。\n\n**S2. 统计方法论异常充分 [共识]。** McNemar + TOST equivalence（7 margin 敏感性）+ margin-free bootstrap cluster + Holm-Bonferroni 三组校正 + post-hoc 功效分析（C1/C2 power > 0.99）。在该子领域中不常见且值得肯定。对 SESOI 的 domain-anchored justification 和 margin dependence 的 acknowledgment 体现方法论自觉。\n\n**S3. Claim 标定诚实 [共识]。** C3 明确标注为 inconclusive（未通过 Holm-Bonferroni），C4 标注 [Exploratory]，authorization scope κ=0.385 在全文五处反复标注，incompleteness confound 多层控制（logistic regression, coreferential lower bound, sans-incompleteness analysis）。\n\n**S4. Error analysis 有实质洞见 [共识]。** 三种 failure mechanism（structural misparse, information gap-filling, boundary violation）与 ambiguity type 的对应关系超越聚合统计。Systematic nocuity（41.3% majority-convergent violations）揭示 agreement-based evaluation 盲区。\n\n**S5. 实验规模与覆盖度 [共识]。** 5+2 models, 6 providers, 2997 episodes, 覆盖 proprietary/open-source/dense/MoE。Replication 在独立 model families 上确认 C1 和 C2。\n\n---\n\n## Weaknesses\n\n### MUST-FIX\n\n**W1. Authorization scope κ=0.385 严重削弱 C4（52pp range claim）[R1 MUST-FIX, R2 AGREE]**\n\nAuthorization scope 的 cross-judge κ 仅 0.385（低于 fair agreement 门槛 0.40），是所有类型中最低的。C4 的核心发现——52pp cross-model range（Claude 12% → GPT-5.4 64%）——正是基于这个最不可靠的类型。三层问题：\n\n(1) Cross-judge κ=0.385 与 human-LLM κ=0.644（Appendix G）是不同指标，§5.4 引用 \"raw agreement 85.3%\" 时数据来源不明确，读者可能混淆。\n(2) Within-judge bootstrap ranking preservation（99.5%）仅证明单个 judge 内部一致性，无法弥补 cross-judge 不一致——稳定偏差仍是偏差。\n(3) Appendix P within-judge-group type ranking ρ=−0.03（p=0.96），auth scope rank reversal（GPT-4.1 judged: rank 1 vs GPT-5.4 judged: rank 6）中 agent composition 和 judge bias 不可分离。\n\n**修改要求**: (a) 计算 auth scope 的 PABAK 或 Gwet's AC1 区分 prevalence paradox 和真实分歧；(b) C4 从 numbered claim 降级为 Discussion observation；(c) Abstract/Conclusion 中 52pp 改为定性描述；(d) §5.4 明确区分 cross-judge κ 和 human-LLM κ 的数据来源。\n\n### SHOULD-FIX\n\n**W2. C2 \"two-tier hierarchy\" 表述强度超过证据 [R1 SHOULD-FIX, R2 AGREE]**\n\n\"Two-tier hierarchy\" 暗示稳定的层级结构，但实际受四个因素制约：(1) ±10pp 仅 3/6 mid-tier pairs equivalent, TOST power 降至 0.57；(2) Bootstrap incompleteness singleton 仅 34.3% 重现, AU p=0.47；(3) Kendall's W=0.398 (p=0.072) 不显著；(4) Incompleteness upper bound 稳健（7 模型 ≥46%），但 mid-tier cohesion 是 margin-dependent 的。\n\nR2 REBUT R1 sub-point：coreferential 31.6% 是 confound-free lower bound 非 incompleteness adjusted effect（logistic regression 控制 token delta 后 incompleteness 仍显著 p=0.018）——不应将 31.6% 视为 incompleteness 的 adjusted rate。\n\n**修改要求**: 弱化为 \"incompleteness consistently separates as the highest-violation type; the remaining types form a less differentiated cluster at the ±15pp equivalence margin, though this structure is margin-dependent\"。正文报告 AU p-value，明确承认 bootstrap 不稳定性。\n\n**W3. Taxonomy 理论基础：§3 \"Scope of ambiguity\" 需扩展 [R2 SHOULD-FIX, R1 partial REBUT — DIVERGENCE]**\n\nR2 认为 incompleteness（information absence）和 conditional precedence（normative conflict）不满足 strict ambiguity 定义，§3 的论证存在循环（纳入 taxonomy → 测试 → 观察相似 pattern → 论证纳入合理性）。R1 反驳称操作性定义有效且有 RE 文献支撑（Berry et al. 2004 广义分类、Dalpiaz et al. 2018 共现研究、Li et al. 2024 11-type taxonomy），改名 \"policy specification defects\" 会切断文献联系。\n\n**共识**: 无论对理论严重程度的判断如何，§3 需更清晰区分 linguistic ambiguity（狭义）和 specification ambiguity（广义），正面回应理论张力而非依赖读者接受操作性定义。\n\n**W4. Disambiguation Neglect 新颖性被高估 [R2 SHOULD-FIX, R1 AGREE]**\n\nIntroduction contribution (3) 将 Disambiguation Neglect 列为 primary contribution，但 Liu et al. (2023, EMNLP) 已证明 LLMs collapse interpretations, Hu et al. (2025) 论证 missing conceptual representations。本文增量是在 agent policy 场景中量化（4.6% awareness），应重新定位而非暗示发现新现象。\n\n**W5. Differential Nocuity 框架增量贡献有限 [R2 SHOULD-FIX, R1 AGREE]**\n\nBerry & Kamsties (2004) 的 nocuous/innocuous 二分法已隐含 type-dependent risk，Willis et al. (2008) 已研究 nocuity degree。§7 的命名暗示新 framework，应定位为 \"empirical validation of differential nocuity in LLM agents\"。\n\n**W6. Clause identity 22.4% variance 被误述为 type identity [R2 SHOULD-FIX, R1 AGREE]**\n\n§5.1 明确写 \"Clause identity explains 22.4% of variance\"——这是 300 clause pair 的 random effect，非 6 type 的 fixed effect。Introduction contribution (2) 的 \"type identity explaining 22× more variance\" 措辞具有误导性。Clause identity ≠ type identity，前者主要反映 clause-level heterogeneity。\n\n**W7. SESOI ±15pp 论证存在循环性 [R1 SHOULD-FIX, R2 AGREE]**\n\n\"≥15pp warrants distinct policy handling\" 用结论论证前提；\"exceeds perturbation bound by >2×\" 是测量噪声标准非实质性差异标准。在安全场景下 ±15pp 相当宽松。好的一面是提供了 7-margin 敏感性分析 + margin-free bootstrap 作为补充。建议从部署角度做实质论证。\n\n**W8. Cross-judge 仅用 OpenAI 家族模型 [R1 SHOULD-FIX, R2 AGREE]**\n\nGPT-5.4/GPT-4.1 可能共享 type-specific correlated bias。R2 补充区分影响范围：C1/C2 的 within-pair Δpp 中 judge bias 被消除（对差值安全），C4 的 cross-model absolute rate comparison 受影响。Limitations 应增加讨论。\n\n**W9. Human validation n=32-34/type 不足以支撑 type-level claims [R1 SHOULD-FIX, R2 AGREE]**\n\nScopal CI [0.00, 1.00], coreferential CI [0.00, 0.84] 完全无信息。Type-level claims (C2-C4) 的有效性依赖对自动 judge 的 type-level 信任——但 auth scope κ=0.385 表明此信任在至少一个类型上脆弱。\n\n### MINOR\n\n**W10. Discussion vs Appendix B 的 mitigation 数字不一致 [R1 MINOR, R2 AGREE]**\n\n§7 报告 GPT-5.4 incompleteness +14pp (p=0.118), auth scope −12pp (p=0.070)；Table 4 同模型同类型分别为 −2.6pp 和 −40.0pp。确认为两个不同实验（§7: n=50/GPT-5.4/generic+type-specific; Appendix B: 1,256 episodes/5 models/type-specific only），但论文未明确说明两者关系。\n\n**W11. Mitigation incompleteness worsening (+14pp, p=0.118) 的因果解释过度 [R2 MINOR, R1 AGREE]**\n\n§7 用确定性语言 \"triggers confabulation rather than caution\" 解释非显著趋势（p=0.118）。应标注为 non-significant trend 并降低解释确定性。\n\n**W12. Abstract \"risk gradient\" vs §5.2 \"two-tier structure\" 术语不一致 [R2 MINOR, R1 AGREE]**\n\n\"Gradient\" 暗示连续变化，\"two-tier\" 暗示离散分层。应统一术语。\n\n**W13. Coreferential 被排除在 mitigation 和 replication 之外 [R2 MINOR, R1 AGREE]**\n\n技术原因合理（Appendix B），但 6 类 taxonomy 中 1 类在两个重要实验中完全缺席影响完整性声明。Limitations 未提及此点。\n\n**W14. Domain 泛化性有限 [R1 MINOR, R2 AGREE]**\n\nτ²-bench 仅覆盖零售/航空客服。医疗/金融/法律领域可能产生不同的类型层级。\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 达成完全共识 [AGREE]：\n\n1. **C1 证据充分**（OR=15.1, 7 模型一致），matched-pair 因果设计是本文最大贡献\n2. **Auth scope κ=0.385 削弱 C4**: 52pp range 基于最低 reliability 类型, 应降级或重度 caveat\n3. **C2 表述过强**: \"two-tier hierarchy\" 在 bootstrap 中仅 34.3% 稳定, Kendall's W 不显著, margin-dependent\n4. **Clause vs type identity**: 22.4% variance 是 clause random effect 非 type fixed effect, contribution (2) 措辞误导\n5. **Disambiguation Neglect 新颖性**: 已有文献记录的现象在新场景中的量化, 非新发现\n6. **Differential Nocuity 增量**: empirical validation 而非新 framework\n7. **Mitigation 数字不一致**: §7 和 Appendix B 是两个不同实验, 需明确区分\n8. **Mitigation over-interpretation**: p=0.118 不应用确定性因果语言\n9. **统计方法论优秀**: TOST + bootstrap + Holm-Bonferroni 在该领域罕见\n10. **Error analysis 有价值**: failure mechanism 对应和 systematic nocuity 提供机制理解\n\n## Reviewer Divergence\n\n**唯一实质分歧: Taxonomy 理论基础的严重程度**\n\n- **R2**: incompleteness/conditional precedence 不属于 ambiguity, §3 论证存在循环, 建议重新框架为 \"policy specification defects\" 或大幅扩展理论论证\n- **R1**: 操作性定义有效且有 RE 文献充分支撑（Berry et al. 2004, Dalpiaz et al. 2018, Li et al. 2024）, 改名会切断文献联系, 但同意 §3 讨论应更清晰\n\n**Review Director 判断**: 这是一个理论 framing 偏好问题而非 fatal flaw。论文的操作性定义有文献基础，但 §3 确实需要正面回应理论张力，而非仅依赖读者接受广义定义。按 SHOULD-FIX 处理，不升级为 MUST-FIX。\n\n---\n\n## Questions\n\n**Q1 [R2]**: Bootstrap AU p=0.47 如何与 \"incompleteness stands apart\" 的 confident framing 调和？\n\n**Q2 [R2]**: \"Clause identity explains 22.4% of variance\" 是 300 clause pair 的 random effect 还是 6 type 的 fixed effect？如果前者，contribution (2) 措辞需修正。\n\n**Q3 [R2]**: Temperature=0 下 ICC=0.919 的 8.1% variance 来自 API non-determinism 还是 episode-level randomness？\n\n**Q4 [R1]**: Auth scope cross-judge κ=0.385 的 raw agreement 是多少？可否计算 PABAK/AC1 区分 prevalence paradox？\n\n**Q5 [R1]**: Confound-adjusted effect size 重做 TOST，C2 是否仍成立？\n\n**Q6 [R1]**: Perturbation control 的修改量是否与 ambiguity perturbation 的 token-level 变化量匹配？\n\n**Q7 [R1]**: Kendall's W=0.398 (p=0.072) 不显著——除 incompleteness 外，type hierarchy 是否 model-dependent？\n\n---\n\n## Missing References\n\nR2 建议补充（R1 部分反驳）：\n- OpenAgentSafety (ICLR 2026) — comprehensive agent safety framework（如果提供 complementary perspective）\n- Agent-SafetyBench (2024) — 349 interactive environment agent safety benchmark（如果与已引用 agent safety 工作有实质差异）\n- Automated Repair of Ambiguous NL Requirements (2025, arxiv:2505.07270)\n\nR1 指出 Ferrari et al. (2019) \"Ambiguity in RE\" 应已被引用为 ferrari_ambiguity_2019。\n\n---\n\n## External Review\n\n外部审稿：未请求（项目配置未启用 `external_review.paperreview_ai.enabled`）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n状态: **done**（耗时 ~3.5 分钟）\n\n### Findings (0 critical, 2 warning, 8 info):\n\n**Warning:**\n- Pages 4-5: 连续两页纯文本（Method + early Results），无任何 display item 穿插。建议 §4 添加模型/数据集汇总表打破视觉单调。\n- Page 15: 最后一页 Appendix Q 仅 ~6 行内容，~90% 空白。建议合并到前一页或调整附录顺序。\n\n**Info:**\n- Page 2: Figure 1 左侧 taxonomy tree 叶节点标签字号偏小\n- Page 6-7: Figure 2/3 热力图单元格数值和 axis label 字号较小（约正文 60%），建议增大\n- Page 6: Table 2 booktabs 风格规范，最优值加粗\n- Page 3: Table 1 分类表排版清晰\n- Page 12: 附录含 6 个表格，密度极高但作为附录可接受\n- Page 6-7: 热力图 yellow-to-red 渐变基本 colorblind-safe\n- Page 9-10: 参考文献格式统一，无未解析引用\n\n---\n\n## Overall Assessment\n\n**评分: 3.5 / 5 (Borderline Conference)**\n**置信度: 4 / 5**\n**评分对应: ARR Overall Assessment 3.5 = Borderline Conference**\n\n### 核心判断\n\n这是一篇**方法论扎实的实证论文**。Matched-pair causal design + perturbation control 在 NLP agent safety 领域确属首创，C1（ambiguity → violation 因果效应，OR=15.1, 7 模型一致）证据充分，统计分析（TOST + bootstrap + Holm-Bonferroni）远超该子领域平均水平。Error analysis 中的 failure mechanism 类型对应和 systematic nocuity 发现有部署价值。\n\n### 阻碍 Conference 接收的问题\n\n1. **测量可靠性**: C4 基于最低 reliability 类型（auth scope κ=0.385）做 numbered claim；C2 的 \"two-tier hierarchy\" 在 bootstrap 中仅 34.3% 稳定，Kendall's W 不显著\n2. **Framing 校准**: clause vs type identity 的 22× claim 有误导性；Disambiguation Neglect 和 Differential Nocuity 的增量贡献被高估——它们是已有概念的 domain application 而非独立理论创新\n3. **SESOI 论证**: ±15pp 的实质性论证不足，影响 C2 的核心表述\n\n### 升级路径\n\n如果 revision 中：(1) 将 C4 降级为 Discussion observation 或补充 prevalence-adjusted agreement；(2) 弱化 C2 为 \"incompleteness consistently highest, remaining types form less differentiated cluster\"；(3) 修正 clause/type identity 归因；(4) 降低 coined terms 的 novelty claim——可升至 **4.0 (Conference)**。核心实证贡献（C1 + error analysis）已达 Conference 水平，framing 调整即可达标。\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- Contribution (2): \"type identity explaining 22× more variance\" 需修正为 \"clause identity\"，并补充 type fixed effect variance\n- 52pp range 的 caveat 权重不足——κ < 0.4 的维度上不应作为核心 finding 突出\n- Contribution (3) 降低 Disambiguation Neglect 的 novelty claim\n\n### §3 Taxonomy\n- \"Scope of ambiguity\" 段落需扩展：更清晰区分 linguistic ambiguity vs specification ambiguity，正面回应理论张力\n- 引用 Dalpiaz et al. (2018) 和 Berry et al. (2004) 的论证可以更充分\n\n### §4 Method\n- SESOI ±15pp: 增加部署场景论证或将 ±10pp 并列为 primary\n- Pages 4-5 考虑添加 model summary table 打破纯文本节奏\n\n### §5 Results\n- §5.2: \"two-tier structure\"/\"stands apart\" 弱化为更谨慎的表述，正文报告 AU p=0.47\n- §5.4: 明确区分 cross-judge κ=0.385 和 human-LLM κ=0.644 的数据来源\n- C4 降级为 Discussion observation 或在 abstract/conclusion 中不引用 52pp\n\n### §6 Analysis\n- §6.2: Disambiguation Neglect 定位为 \"已知现象在 agent policy 场景中的首次量化\"\n- Incompleteness wording 已较好但 §6.2 引用 good-enough processing 的 analogy 需加 mechanism-level caveat\n\n### §7 Discussion\n- Differential Nocuity: 改为 \"empirical validation\" 定位\n- Mitigation: (a) 明确标注 §7 和 Appendix B 是两个独立实验；(b) incompleteness +14pp (p=0.118) 标注为 non-significant trend\n- \"Abstract 'risk gradient' vs 正文 'two-tier'\" 术语统一\n\n### §8 Limitations\n- 增加 single-family judge bias 讨论\n- 提及 coreferential 排除对 taxonomy 完整性的影响\n- 更强调 type-level human validation gap",
    "project": "policy_ambiguity_safety",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.5 - Borderline Conference",
    "review_chat_id": "oc_967344d166ba485ad606d14379e69d85"
  }
}
```

</details>

---


### Tool result

_source line 991 · 2026-05-22T08:57:04.875088+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_10fa2e89afc5e9b8a13613245e008dd9:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4318
}
```

</details>

---


### Assistant

_source line 992 · 2026-05-22T08:57:14.545122+00:00_

Round 11 审稿完成。

**审稿报告已投递给 Research Director。**

核心结论：
- **评分 3.5（Borderline Conference）**，两位 Reviewer 一致
- **最大亮点**: matched-pair causal design（C1 OR=15.1, 7 模型一致）和统计分析充分度
- **1 个 MUST-FIX**: auth scope κ=0.385 → C4 应降级
- **8 个 SHOULD-FIX**: C2 表述过强、taxonomy 理论扩展、coined terms 降低 novelty claim、clause/type identity 修正、SESOI 论证、cross-judge bias 讨论、human validation gap
- **5 个 MINOR**: mitigation 数字不一致、over-interpretation、术语不一致、coreferential 排除、domain 局限
- **升级路径明确**: framing 调整到位可升至 4.0（Conference）

Issue tracker 已同步更新（2 critical, 7 warning, 7 info）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 92

## Round 92

2 recorded events


### User

_source line 993 · 2026-05-22T08:57:17.326712+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交给 Review Director。

核心结论：与 R2 在大多数问题上达成共识（评分均为 3.5），特别是在 claim 精确度（clause vs type identity）、mitigation 过度解释、bootstrap 不稳定性方面。我反驳了 R2 关于 taxonomy 理论基础的批评（论文有明确的操作性定义和 RE 文献支撑），并部分反驳了 missing references 的指控（Ferrari et al. 2019 已被引用）。两位 reviewer 的额外关注点互补：我侧重测量可靠性（judge bias, SESOI, human validation），R2 侧重理论定位和新颖性声明。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 994 · 2026-05-22T08:57:26.498436+00:00_

Round 11 审稿已完成并投递。

**结果**: 3.5 / 5（Borderline Conference），两位 Reviewer 评分一致。

**核心结论**:
- **C1 因果效应（OR=15.1）证据充分**，matched-pair 设计是本文最大贡献
- **阻碍升级的三类问题**: (1) 测量可靠性——C4 基于 κ=0.385 做 numbered claim，C2 bootstrap 仅 34.3% 稳定；(2) Framing 校准——clause/type identity 归因错误、coined terms 新颖性高估；(3) SESOI 论证不足
- **升级路径明确**: C4 降级、C2 弱化、修正归因、降低术语 novelty claim → 可达 4.0

报告和 issue tracker 已同步更新并投递至 Research Director。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 93

## Round 93

54 recorded events


### User

_source line 995 · 2026-05-22T09:49:43.568800+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: policy_ambiguity_safety
- 论文路径: /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: ARR May cycle
- 截止日期: 2026-06-15
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 996 · 2026-05-22T09:49:50.037378+00:00_

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
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 997 · 2026-05-22T09:49:50.038008+00:00_

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
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 998 · 2026-05-22T09:49:55.959474+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,get_external_review_status,read_project_file,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,get_visual_check_status",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,get_external_review_status,read_project_file,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,get_visual_check_status",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 999 · 2026-05-22T09:49:55.959834+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1000 · 2026-05-22T09:49:59.824394+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__get_visual_check_status",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__get_visual_check_status",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 1001 · 2026-05-22T09:49:59.824756+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1002 · 2026-05-22T09:50:03.991365+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "policy_ambiguity_safety"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "policy_ambiguity_safety"
  }
}
```

</details>

---


### Tool result

_source line 1003 · 2026-05-22T09:50:04.443589+00:00_

{"result":"# 项目 policy_ambiguity_safety 概况\n\n## 实验状态 (17 个)\n\n- **plan_014**: DONE (success) — \n- **plan_015**: DONE (success) — \n- **plan_013**: DONE (success) — \n- **plan_012**: DONE (success) — \n- **plan_011**: DONE (success) — \n- **plan_010**: DONE (success) — \n- **plan_004**: DONE (success) — \n- **plan_003b**: DONE (success) — \n- **plan_003a**: DONE (success) — \n- **plan_002c**: DONE (success) — \n- **plan_006**: DONE (success) — \n- **plan_005**: DONE (success) — \n- **plan_002**: DONE (negative) — \n- **diag_001**: DONE (negative) — \n- **mvp_001**: DONE (negative) — \n\n## 最新报告\n# Handover — 2026-05-22\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n（无）\n\n## 近期结论\n- **plan_016** (negative): Type-specific mitigation prompts reduce violations more effectively than generic awareness prompts for their targeted ambiguity types, supporting the practical contribution that type-aware triage is necessary for policy-governed deployments\n- **plan_009** (success): Cross-judge LLM agreement (gpt-5.4 vs gpt-4.1) achieves substantial agreement (weighted κ ≥ 0.60) on violation level classification. LLM-human agreement should be comparable, validating the cross-judge evaluation design.\n  [plan_009_annotation_guidelines](/api/workspace-files/projects/policy_ambiguity_safety/artifacts/plan_009/report/annotation_guidelines.md) | [plan_009_annotation_sheet](/api/workspace-files/projects/policy_ambiguity_safety/artifacts/plan_009/data/annotation_sheet.jsonl) | [plan_009_llm_agreement](/api/workspace-files/projects/policy_ambiguity_safety/artifacts/plan_009/report/llm_agreement.json) | [plan_009_annotation_sheet_clean](/api/workspace-files/projects/policy_ambiguity_safety/artifacts/plan_009/data/annotation_sheet_clean.jsonl)\n- **plan_014** (success): Expanding perturbation control from n=120 to n=300 will maintain non-significant Δ_perturb (CI containing zero) while narrowing CI upper bound from 13.3pp to ~8pp, strengthening SESOI justification for C
…[truncated 563 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1004 · 2026-05-22T09:50:05.046229+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "policy_ambiguity_safety",
  "file": "review_issues.yaml",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "policy_ambiguity_safety",
    "file": "review_issues.yaml",
    "max_chars": "0"
  }
}
```

</details>

---


### Tool result

_source line 1005 · 2026-05-22T09:50:06.201840+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'mistakes.yaml', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'review_issues.yaml'\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 1155
}
```

</details>

---


### Tool call

_source line 1006 · 2026-05-22T09:50:06.453061+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.tex",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.tex",
    "limit": "80"
  }
}
```

</details>

---


### Tool result

_source line 1007 · 2026-05-22T09:50:06.503746+00:00_

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
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1008 · 2026-05-22T09:50:11.272400+00:00_

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
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
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

_source line 1009 · 2026-05-22T09:50:11.322998+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1010 · 2026-05-22T09:50:14.585661+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1011 · 2026-05-22T09:50:14.887520+00:00_

1	## Review Issues Tracker — policy_ambiguity_safety
2	## Paper: "Not All Policy Ambiguity Is Equal: Type-Specific Safety Risks for LLM Agents"
3	## Venue: EMNLP 2026 via ARR May cycle
4	## Latest Round: 11 (Score: 3.5 Borderline Conference)
5	## Upgrade path: fix framing calibration → 4.0
6	
7	# ============================================================
8	# CRITICAL ISSUES
9	# ============================================================
10	
11	- id: "R11-C1"
12	  summary: "Clause vs type identity 22× claim 事实性错误 — type 仅解释 0.4% 方差，22× 是 clause identity"
13	  category: method
14	  severity: critical
15	  status: in_progress
16	  first_raised_round: 11
17	  last_seen_round: 11
18	  mentions:
19	    - round: 11
20	      reviewers: [R2, R1]
21	      note: "W6. clause_within_type=22.0% vs ambiguity_type=0.4%. Introduction contribution (2) '22× type identity' 是 clause identity 不是 type identity。共识：事实性错误，必须修正。"
22	  action_items:
23	    - round: 11
24	      action: "(1) Intro contribution(2) 改为 clause identity; (2) §5.1 补充 type/clause 方差拆分; (3) Abstract/Conclusion 同步修正; (4) 用这个发现强化 §6.3 systematic nocuity story"
25	      assigned_to: agent
26	      status: in_progress
27	  resolution: ""
28	  resolution_round: null
29	
30	- id: "R10-C1"
31	  summary: "Authorization scope κ=0.385 不足以支撑 C4 中 52pp range 作为核心发现"
32	  category: method
33	  severity: critical
34	  status: in_progress
35	  first_raised_round: 8
36	  last_seen_round: 11
37	  mentions:
38	    - round: 10
39	      reviewers: [R1, R2]
40	      note: "R1 MUST-FIX. κ=0.385 < fair agreement 0.40, 52pp 中真实差异 vs noise 无法分离。"
41	    - round: 11
42	      reviewers: [R1, R2]
43	      note: "W1 MUST-FIX. 三层问题: cross-judge κ vs human-LLM κ 混淆, within-judge bootstrap 不弥补 cross-judge, Appendix P ρ=-0.03 rank reversal。要求 PABAK/AC1 + C4 降级 + 52pp 定性化。"
44	  action_items:
45	    - round: 10
46	      action: "Abstract/Intro 降格 auth scope 52pp"
47	      assigned_to: agent
48	      status: in_progress
49	    - round: 11
50	      act
…[truncated 10498 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 1012 · 2026-05-22T09:50:14.888005+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 ARR call for papers submission guidelines author instructions"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 ARR call for papers submission guidelines author instructions"
  }
}
```

</details>

---


### Tool call

_source line 1013 · 2026-05-22T09:50:16.343825+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_12/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"NO_PDF\"",
  "description": "Check if submitted PDF exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_12/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"NO_PDF\"",
    "description": "Check if submitted PDF exists"
  }
}
```

</details>

---


### Tool result

_source line 1014 · 2026-05-22T09:50:16.495681+00:00_

/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_12/submitted.pdf
PDF_EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Bash",
  "elapsed_ms": 151
}
```

</details>

---


### Tool result

_source line 1015 · 2026-05-22T09:50:25.386681+00:00_

Web search results for query: "EMNLP 2026 ARR call for papers submission guidelines author instructions"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Submission Guide","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"}]

Based on the search results, here is a comprehensive overview of the EMNLP 2026 ARR submission guidelines:

## Paper Types and Scope

EMNLP 2026 invites the submission of long and short papers featuring substantial, o
…[truncated 2034 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "WebSearch",
  "elapsed_ms": 10498
}
```

</details>

---


### Tool call

_source line 1016 · 2026-05-22T09:50:40.847868+00:00_

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
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 1017 · 2026-05-22T09:50:41.199991+00:00_

1	\begin{abstract}
2	LLM-based agents operate under natural-language policy specifications that inevitably contain ambiguity, yet the causal relationship between ambiguity type and safety violations remains unmeasured. We present a matched-pair study on $\tau^2$-bench with 300 clause pairs spanning a six-type ambiguity taxonomy, evaluated across five models (2,997 episodes). Three findings emerge. First, ambiguous clauses increase violation rates by 34.0 percentage points (OR $= 15.1$), with a perturbation control supporting ambiguity-specific causation. Second, incompleteness consistently ranks highest (46--62\% across seven models); the remaining five types show a risk gradient rather than sharp tiers. Third, error analysis of 614 violation traces reveals \emph{Disambiguation Neglect} ($\leq$11\% awareness) and \emph{systematic nocuity}---41.3\% of clauses triggering model-convergent violations---indicating clause-level rather than model-level risk factors. These results motivate type-aware policy auditing and externalized ambiguity detection for policy-governed agent deployments.
3	\end{abstract}
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 1018 · 2026-05-22T09:50:41.200480+00:00_

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
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 1019 · 2026-05-22T09:50:41.602347+00:00_

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
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 1020 · 2026-05-22T09:50:41.602782+00:00_

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
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 1021 · 2026-05-22T09:50:42.606614+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Ambiguity in NLP and requirements engineering.}
5	Ambiguity has been studied extensively in both computational linguistics and software engineering. Word sense disambiguation \citep{navigli_wsd_2009} addresses lexical ambiguity at the token level; our lexical type extends this to policy-specific polysemy. \citet{li_ambiguity_taxonomy_2024} propose an 11-type NLP taxonomy covering syntactic, semantic, and pragmatic ambiguity, from which we draw our linguistic-layer types. In requirements engineering (RE), \citet{massey_ambiguity_re_2014} classify six ambiguity types in regulatory texts, and \citet{berry_kamsties_2004} introduce the distinction between nocuous ambiguity (where stakeholders diverge on interpretation) and innocuous ambiguity (where they converge). Computational detection of nocuous ambiguity has progressed from heuristic methods \citep{chantree_2006,willis_nocuous_2008} through NLP-based cross-domain detectors \citep{ferrari_ambiguity_2019,ferrari_defects_2018} to transformer-based approaches for anaphoric ambiguity \citep{ezzini_taphsir_2022,ezzini_anaphoric_2022}. \citet{zhao_nlp4re_2021} survey the broader NLP4RE landscape. Our work extends Berry and Kamsties' framework to LLM agents, where the absence of shared organizational context makes previously innocuous ambiguity nocuous.
6	
7	\paragraph{Psycholinguistics of ambiguity processing.}
8	\citet{ferreira_good_enough_2002} show that human comprehenders build shallow, ``good-enough'' representations rather than full parses, paralleling our observation that LLM agents adopt surface interpretations. \citet{frazier_rayner_1982} demonstrate early commitment to a single parse; \citet{li_garden_path_llm_2024} provide direct evidence that LLMs exhibit analogous garden-path effects. \citet{liu_ambiguity_2023} demonstrate that language models fail to represent ambiguity, collapsing multiple interpretations into a single output. These findings
…[truncated 2470 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 1003
}
```

</details>

---


### Tool call

_source line 1022 · 2026-05-22T09:50:42.606974+00:00_

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
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/taxonomy.tex"
  }
}
```

</details>

---


### Tool result

_source line 1023 · 2026-05-22T09:50:42.757799+00:00_

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
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 1024 · 2026-05-22T09:50:43.109494+00:00_

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
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 1025 · 2026-05-22T09:50:43.412120+00:00_

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
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 302
}
```

</details>

---


### Tool call

_source line 1026 · 2026-05-22T09:50:43.412509+00:00_

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
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 1027 · 2026-05-22T09:50:43.463181+00:00_

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
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1028 · 2026-05-22T09:50:48.833767+00:00_

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
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/analysis.tex"
  }
}
```

</details>

---


### Tool result

_source line 1029 · 2026-05-22T09:50:49.235662+00:00_

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
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 1030 · 2026-05-22T09:50:49.787950+00:00_

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
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1031 · 2026-05-22T09:50:49.788329+00:00_

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
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1032 · 2026-05-22T09:50:50.390688+00:00_

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
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1033 · 2026-05-22T09:50:50.792560+00:00_

1	\section{Conclusion}
2	
3	Ambiguous policy clauses increase agent safety violations by 34.0\,pp (OR\,$=$\,15.1) across five models, with clause identity explaining 22$\times$ more variance than model identity. Incompleteness consistently ranks highest across all seven models ($\geq$46\%), with rankings replicating in independent families ($\rho = 0.60$--$0.90$). With agents exhibiting disambiguation neglect in over 89\% of cases and 41.3\% of clauses triggering model-convergent violations, type-aware auditing and externalized detection are critical for policy-governed deployments.
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 1034 · 2026-05-22T09:50:51.897012+00:00_

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
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 1035 · 2026-05-22T09:50:51.897421+00:00_

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
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1036 · 2026-05-22T09:50:52.248835+00:00_

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
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 1037 · 2026-05-22T09:50:52.301059+00:00_

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
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 52
}
```

</details>

---


### Tool call

_source line 1038 · 2026-05-22T09:51:00.482807+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "policy_ambiguity_safety"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "policy_ambiguity_safety"
  }
}
```

</details>

---


### Tool result

_source line 1039 · 2026-05-22T09:51:01.537238+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 1054
}
```

</details>

---


### Tool call

_source line 1040 · 2026-05-22T09:51:01.537652+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 May cycle submission format page limit template guidelines site:aclrollingreview.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 May cycle submission format page limit template guidelines site:aclrollingreview.org"
  }
}
```

</details>

---


### Tool result

_source line 1041 · 2026-05-22T09:51:09.116346+00:00_

Web search results for query: "ACL Rolling Review 2026 May cycle submission format page limit template guidelines site:aclrollingreview.org"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Submission Form Fields – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/submissionform"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"ARR Changelog – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/changelog"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"}]

Based on my web search of the ACL Rolling Review website, here are the key submission format guidelines for the 
…[truncated 1329 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "WebSearch",
  "elapsed_ms": 7578
}
```

</details>

---


### Tool call

_source line 1042 · 2026-05-22T09:51:36.275303+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "policy_ambiguity_safety",
  "review_chat_id": "oc_967344d166ba485ad606d14379e69d85"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "policy_ambiguity_safety",
    "review_chat_id": "oc_967344d166ba485ad606d14379e69d85"
  }
}
```

</details>

---


### Tool result

_source line 1043 · 2026-05-22T09:51:59.774807+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 23499
}
```

</details>

---


### Tool call

_source line 1044 · 2026-05-22T09:51:59.926401+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "project": "policy_ambiguity_safety",
  "round_number": "1",
  "text": "你是 Reviewer 1，负责**方法严谨性**审查。\n\n## Venue 信息\n- **目标**: EMNLP 2026 via ARR May cycle\n- **Deadline**: 2026-05-25\n- **格式**: Long paper, 8页正文, references不限, Limitations/Ethics不计页数\n- **模板**: ACL LaTeX template, double-blind\n- **评分标准**: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 论文路径\n- LaTeX: `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_12/submitted.pdf`\n\n## 审查侧重\n\n请重点审查以下方面：\n\n### 1. 实验设计\n- Matched-pair design 的因果推断有效性：300 clause pairs 的构造是否充分控制了混淆因素？\n- Perturbation control (n=300) 的充分性：CI [-8.0, 6.67] 是否足以排除非语义因素？\n- Replication 设计（2 additional models, 5 types）的覆盖度\n\n### 2. 统计分析\n- TOST equivalence testing：±15pp SESOI 的选择论证是否有循环性？\n- Multiple comparison correction (Holm-Bonferroni, 3 families) 的正确性\n- Bootstrap cluster analysis (AU p=0.47) 对 C2 two-tier → risk gradient 的支撑力度\n- Variance decomposition: clause identity 22% vs model identity 1% 的解释\n- C4 interaction: F(20, 2976)=1.97, p=0.006 但仅 2.9% variance——是否实质性？\n\n### 3. Evaluation Pipeline\n- Cross-judge design: GPT-5.4 judges 3 models, GPT-4.1 judges 2 models 的非对称性\n- Authorization scope κ=0.385 对 C4 52pp range claim 的影响\n- Human validation: n=100, per-type n=32-34 的检验力\n- Within-judge bootstrap vs cross-judge reliability 的区分是否清晰\n\n### 4. Confound 处理\n- Incompleteness information-addition confound: logistic regression 控制是否充分？token count 是否是好的 proxy？\n- Judge family bias (both judges from OpenAI family) 对 cross-model comparison 的影响\n\n### 5. Claims 校准\n- C1 (binary effect): 34.0pp, OR=15.1——claim 与证据匹配度\n- C2 (risk gradient): \"risk gradient rather than sharp tiers\"——统计支撑是否充分？\n- C3 (layer effect): 声称 inconclusive——是否应完全移除？\n- C4 (exploratory): 52pp range + low κ——exploratory label 是否足够谨慎？\n\n请按 Strengths → Weaknesses (MUST-FIX / SHOULD-FIX / MINOR) → Questions → Missing References → Overall Assessment 的结构输出审稿意见。对每个 Weakness 标注严重程度和具体修改建议。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "project": "policy_ambiguity_safety",
    "round_number": "1",
    "text": "你是 Reviewer 1，负责**方法严谨性**审查。\n\n## Venue 信息\n- **目标**: EMNLP 2026 via ARR May cycle\n- **Deadline**: 2026-05-25\n- **格式**: Long paper, 8页正文, references不限, Limitations/Ethics不计页数\n- **模板**: ACL LaTeX template, double-blind\n- **评分标准**: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 论文路径\n- LaTeX: `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_12/submitted.pdf`\n\n## 审查侧重\n\n请重点审查以下方面：\n\n### 1. 实验设计\n- Matched-pair design 的因果推断有效性：300 clause pairs 的构造是否充分控制了混淆因素？\n- Perturbation control (n=300) 的充分性：CI [-8.0, 6.67] 是否足以排除非语义因素？\n- Replication 设计（2 additional models, 5 types）的覆盖度\n\n### 2. 统计分析\n- TOST equivalence testing：±15pp SESOI 的选择论证是否有循环性？\n- Multiple comparison correction (Holm-Bonferroni, 3 families) 的正确性\n- Bootstrap cluster analysis (AU p=0.47) 对 C2 two-tier → risk gradient 的支撑力度\n- Variance decomposition: clause identity 22% vs model identity 1% 的解释\n- C4 interaction: F(20, 2976)=1.97, p=0.006 但仅 2.9% variance——是否实质性？\n\n### 3. Evaluation Pipeline\n- Cross-judge design: GPT-5.4 judges 3 models, GPT-4.1 judges 2 models 的非对称性\n- Authorization scope κ=0.385 对 C4 52pp range claim 的影响\n- Human validation: n=100, per-type n=32-34 的检验力\n- Within-judge bootstrap vs cross-judge reliability 的区分是否清晰\n\n### 4. Confound 处理\n- Incompleteness information-addition confound: logistic regression 控制是否充分？token count 是否是好的 proxy？\n- Judge family bias (both judges from OpenAI family) 对 cross-model comparison 的影响\n\n### 5. Claims 校准\n- C1 (binary effect): 34.0pp, OR=15.1——claim 与证据匹配度\n- C2 (risk gradient): \"risk gradient rather than sharp tiers\"——统计支撑是否充分？\n- C3 (layer effect): 声称 inconclusive——是否应完全移除？\n- C4 (exploratory): 52pp range + low κ——exploratory label 是否足够谨慎？\n\n请按 Strengths → Weaknesses (MUST-FIX / SHOULD-FIX / MINOR) → Questions → Missing References → Overall Assessment 的结构输出审稿意见。对每个 Weakness 标注严重程度和具体修改建议。"
  }
}
```

</details>

---


### Tool result

_source line 1045 · 2026-05-22T09:52:19.516569+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 19590
}
```

</details>

---


### Tool call

_source line 1046 · 2026-05-22T09:52:19.667342+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "project": "policy_ambiguity_safety",
  "round_number": "1",
  "text": "你是 Reviewer 2，负责**新颖性/完整性**审查。\n\n## Venue 信息\n- **目标**: EMNLP 2026 via ARR May cycle\n- **Deadline**: 2026-05-25\n- **格式**: Long paper, 8页正文, references不限, Limitations/Ethics不计页数\n- **模板**: ACL LaTeX template, double-blind\n- **评分标准**: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 论文路径\n- LaTeX: `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_12/submitted.pdf`\n\n## 审查侧重\n\n请重点审查以下方面：\n\n### 1. 新颖性与贡献定位\n- Contribution (1) \"first matched-pair causal study\"——是否确实是 first？是否有 overclaiming？\n- Contribution (2) \"clause identity explaining 22× more variance than model identity\"——这是 clause identity 不是 type identity，表述是否准确？\n- Contribution (3) \"Disambiguation Neglect\"——Liu et al. (2023) 和 Hu et al. (2025) 已有类似发现，novelty claim 是否被高估？\n- \"systematic nocuity\" 概念——相对于 Berry & Kamsties (2004) 的增量贡献\n\n### 2. Related Work 覆盖\n- 是否遗漏重要的相关工作？特别是：\n  - Policy compliance for LLM agents 领域\n  - Ambiguity detection in NLP 领域\n  - Agent safety evaluation 新进展\n- DRIP-R (2026) 对比是否公平？\n- PolicyBank (2026), AgentPex (2026), MANTRA (2026) 等并发工作的引用是否充分？\n\n### 3. Framing 准确性\n- Taxonomy 的理论基础：incompleteness 和 conditional precedence 是否真正属于 \"ambiguity\"？§3 \"Scope of ambiguity\" 段落是否充分解决了这个理论张力？\n- \"Differential Nocuity\" framework 的定位：是新框架还是已有概念的应用？\n- Abstract/Conclusion 中的 claim 是否与正文证据一致？有无 overclaiming？\n\n### 4. 写作质量\n- 论文组织结构是否清晰？8页正文是否合理分配？\n- 技术写作是否准确？有无自相矛盾之处？\n- Discussion vs Appendix B 的 mitigation 数字：§7 GPT-5.4 generic +1.3pp vs Appendix B 同模型 -14.0pp——方向不同，是否有充分解释？\n- \"triggers confabulation\" (p=0.118) 等非显著结论的语言是否校准？\n\n### 5. 格式合规\n- 8页正文限制是否符合？\n- ACL 模板使用是否正确？\n- 匿名规则是否遵守？（检查 \\author{Anonymous}, 无自引暴露）\n- Limitations 章节是否合规？（只讨论局限性，不含新实验/分析）\n- References 格式一致性\n\n请按 Strengths → Weaknesses (MUST-FIX / SHOULD-FIX / MINOR) → Questions → Missing References → Overall Assessment 的结构输出审稿意见。对每个 Weakness 标注严重程度和具体修改建议。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "project": "policy_ambiguity_safety",
    "round_number": "1",
    "text": "你是 Reviewer 2，负责**新颖性/完整性**审查。\n\n## Venue 信息\n- **目标**: EMNLP 2026 via ARR May cycle\n- **Deadline**: 2026-05-25\n- **格式**: Long paper, 8页正文, references不限, Limitations/Ethics不计页数\n- **模板**: ACL LaTeX template, double-blind\n- **评分标准**: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 论文路径\n- LaTeX: `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_12/submitted.pdf`\n\n## 审查侧重\n\n请重点审查以下方面：\n\n### 1. 新颖性与贡献定位\n- Contribution (1) \"first matched-pair causal study\"——是否确实是 first？是否有 overclaiming？\n- Contribution (2) \"clause identity explaining 22× more variance than model identity\"——这是 clause identity 不是 type identity，表述是否准确？\n- Contribution (3) \"Disambiguation Neglect\"——Liu et al. (2023) 和 Hu et al. (2025) 已有类似发现，novelty claim 是否被高估？\n- \"systematic nocuity\" 概念——相对于 Berry & Kamsties (2004) 的增量贡献\n\n### 2. Related Work 覆盖\n- 是否遗漏重要的相关工作？特别是：\n  - Policy compliance for LLM agents 领域\n  - Ambiguity detection in NLP 领域\n  - Agent safety evaluation 新进展\n- DRIP-R (2026) 对比是否公平？\n- PolicyBank (2026), AgentPex (2026), MANTRA (2026) 等并发工作的引用是否充分？\n\n### 3. Framing 准确性\n- Taxonomy 的理论基础：incompleteness 和 conditional precedence 是否真正属于 \"ambiguity\"？§3 \"Scope of ambiguity\" 段落是否充分解决了这个理论张力？\n- \"Differential Nocuity\" framework 的定位：是新框架还是已有概念的应用？\n- Abstract/Conclusion 中的 claim 是否与正文证据一致？有无 overclaiming？\n\n### 4. 写作质量\n- 论文组织结构是否清晰？8页正文是否合理分配？\n- 技术写作是否准确？有无自相矛盾之处？\n- Discussion vs Appendix B 的 mitigation 数字：§7 GPT-5.4 generic +1.3pp vs Appendix B 同模型 -14.0pp——方向不同，是否有充分解释？\n- \"triggers confabulation\" (p=0.118) 等非显著结论的语言是否校准？\n\n### 5. 格式合规\n- 8页正文限制是否符合？\n- ACL 模板使用是否正确？\n- 匿名规则是否遵守？（检查 \\author{Anonymous}, 无自引暴露）\n- Limitations 章节是否合规？（只讨论局限性，不含新实验/分析）\n- References 格式一致性\n\n请按 Strengths → Weaknesses (MUST-FIX / SHOULD-FIX / MINOR) → Questions → Missing References → Overall Assessment 的结构输出审稿意见。对每个 Weakness 标注严重程度和具体修改建议。"
  }
}
```

</details>

---


### Tool result

_source line 1047 · 2026-05-22T09:52:21.192358+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1525
}
```

</details>

---


### Assistant

_source line 1048 · 2026-05-22T09:52:29.216823+00:00_

Round 12 审稿已启动：

| 任务 | 状态 |
|------|------|
| 视觉审查 Agent | ✅ 已派发（并行运行） |
| Reviewer 1（方法严谨性） | ✅ 已分配 |
| Reviewer 2（新颖性/完整性） | ✅ 已分配 |
| 外部审稿 | ⏭ 未配置，跳过 |

等待两名 Reviewer 返回独立初审意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 94

## Round 94

2 recorded events


### User

_source line 1049 · 2026-05-22T09:56:59.788364+00:00_

[Reviewer 1 审稿意见]:
## 总体评分
**Overall**: 3.5 / 5 — Borderline Conference
**一句话总结**: 研究问题新颖、matched-pair 设计严谨，但 C2 risk gradient 的统计支撑依赖 margin 选择、incompleteness 的 information-addition confound 未充分解决、C4 的 judge family bias 削弱跨模型比较可信度——三者叠加使核心 claim 需要校准。

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | Matched-pair 因果设计本身优秀，perturbation control 有说服力；但 TOST margin 选择论证有循环性，incompleteness confound 用 token count proxy 不够充分，C4 cross-judge asymmetry 对 interaction 结论构成系统性威胁 |
| Excitement | 3.5/5 | 首个 ambiguity type → agent safety violation 的因果研究，taxonomy + matched-pair 方法学贡献明确；但单一 benchmark (τ²-bench) 和 OpenAI-only judge family 限制了泛化性 |
| Reproducibility | 4/5 | 数据集和代码承诺公开；API 调用参数明确 (temp=0, top_p=1)；ICC=0.919 但仅限 OpenAI family 内部 |
| Confidence | 4/5 | 我仔细阅读了论文全文（含 15 页附录），熟悉 TOST equivalence testing、matched-pair 因果推断和 LLM-as-judge 文献 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] TOST ±15pp SESOI 选择的循环论证风险

- **具体位置**: §4.6 Statistical Analysis, §5.2 Type Risk Gradient (C2)
- **问题**: SESOI 的论证逻辑为"超过 perturbation control bound (6.67pp) 的 >2×"(§4.6)，但 perturbation control bound 本身取决于特定扰动类型的选择（synonym substitution, clause reordering），而非独立的领域标准。更关键的是，C2 "risk gradient rather than sharp tiers" 的核心 claim 对 margin 选择高度敏感：在 ±10pp 时仅 3/6 mid-tier pairs 达到 equivalence（Table 3），gradient 结构基本瓦解。论文提供了 sensitivity analysis（7个 margin，Table 3），但正文 claim 仅在 ±15pp 时成立——这个依赖关系应当上升为 claim 声明的一部分，而非仅在方法段落中一带而过。
- **为什么影响接收**: C2 是论文两个 primary claim 之一，其可信度直接决定论文核心贡献的成立。如果 gradient 结构是 margin-dependent 的，读者需要在 abstract 和 conclusion 层面就了解这一条件。
- **建议修改方向**: (1) 在 C2 claim 的每次陈述中附加 margin 条件（如"at the ±15pp margin"）；(2) 在 Abstract/Introduction 中明确 gradient 的 margin-dependent 性质；(3) 讨论 field-standard SESOI 缺失对结论稳健性的影响。

**N2** [critical] Cross-judge asymmetry 对 C4 interaction 结论的系统性威胁

- **具体位置**: §4.4 Evaluation, §5.4 C4 (exploratory), Limitations
- **问题**: GPT-5.4 judges Claude/GPT-4.1/Qwen3, GPT-4.1 judges GPT-5.4/DeepSeek。论文正确指出 Δpp（paired within model-judge）不受影响（§4.4），但 C4 的 interaction F-test 操作的是 absolute violation rates across models，这些 absolute rates 来自不同 judge。具体地：authorization scope 52pp range（Claude 12% → GPT-5.4 64%）中，Claude 和 GPT-5.4 分别由不同 judge 评判。而 authorization scope 恰好是 inter-judge κ 最低的类型（κ=0.385）。因此 52pp range 可能部分反映两个 judge 对 authorization scope violations 的判定标准差异，而非模型间的真实差异。论文在 §5.4 末尾提到"upper bound with substantial measurement uncertainty"，但这个 caveat 与正文的强调程度不匹配——Figure 3 heatmap 和"most model-differentiating type"的措辞给读者留下的印象远比 caveat 强烈。
- **为什么影响接收**: C4 虽标注 exploratory，但其结论（authorization scope 是最大的模型分化因子）在 Discussion §7 的 differential nocuity 框架中占核心位置。如果该结论受 judge confound 驱动，Discussion 的理论贡献被削弱。
- **建议修改方向**: (1) 在 Figure 3 caption 中明确标注 judge assignment（哪些模型由哪个 judge 评判）；(2) 将 "upper bound with measurement uncertainty" 的 caveat 提升到 Figure 3 caption 和 Discussion 中；(3) 报告 within-judge-group 的 authorization scope range（GPT-5.4 judged: Claude 12%, GPT-4.1 46%, Qwen3 26% → 34pp range；GPT-4.1 judged: GPT-5.4 64%, DeepSeek 60% → 4pp range）以区分 judge effect vs. model effect。

**N3** [critical] Incompleteness information-addition confound 的控制不充分

- **具体位置**: §3 Taxonomy ("Scope of ambiguity"), §5.2 (confound discussion), Appendix F (logistic regression), Appendix O (clause length)
- **问题**: Incompleteness 的 unambiguous variant 不是"消歧"而是"补全缺失信息"——这在概念层面与其他五种 ambiguity type 有本质区别。论文使用 token count difference 作为 information addition 的 proxy 进行 logistic regression 控制（Appendix F, p=0.018），但自己也承认"token count is a coarse proxy for information content"（Appendix F）。核心问题：(a) token count 无法区分新增内容的 informativeness vs. 冗余度；(b) 不同类型的 token delta 语义权重不同（authorization scope +36.1 words 但为 boundary specification，incompleteness +34.6 words 为全新 policy content）；(c) 论文用 "authorization scope has larger delta but lower rate" 作为反证（Appendix O），但这是跨类型比较——不同类型的 token delta 语义完全不同，无法做 apples-to-apples 的反驳。
- **为什么影响接收**: Incompleteness 是论文的 "consistent upper-bound risk type"，其 49.2pp effect 是所有类型中最大的。如果该 effect 被 information-addition confound 实质性地膨胀，C2 gradient 的形状会改变（incompleteness 可能不是真正的 upper bound，而仅是 confound-inflated 的 artifact）。
- **建议修改方向**: (1) 明确区分 incompleteness 的 effect 为 "upper bound including potential information-addition inflation"（目前措辞已部分做到，但需更一致）；(2) 考虑在 C2 claim 中以 coreferential 的 confound-free 18.7pp 作为 lower bound 锚点，而非以 incompleteness 作为 headline；(3) 讨论替代 proxy（如 propositional content count）的可行性。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Bootstrap cluster AU p=0.47 对 C2 gradient claim 的支撑力不足

- **具体位置**: §5.2, Appendix I (Bootstrap Cluster Analysis)
- **问题**: 论文用 margin-free bootstrap cluster analysis 作为 TOST 的补充证据。但 incompleteness singleton 的 AU p-value 仅为 0.47——远低于通常 0.95 的 significance threshold。34.3% 的 bootstrap samples 复现了该 partition。论文自己说"the modal partition but not overwhelmingly stable"和"the boundary is not sharp"。这意味着 margin-free 方法 *不* 支持 incompleteness 作为 distinct upper-bound cluster 的 claim——TOST 和 bootstrap 给出不一致的信号。
- **建议**: 明确承认 bootstrap evidence 不支持 incompleteness 与 mid-tier 的 sharp separation；将 C2 claim 重新表述为 "the six types show differential risk, with incompleteness trending highest, but the boundary between incompleteness and the mid-tier cluster is not statistically robust under margin-free methods."

**W2** [warning] Human validation 的 per-type 检验力不足以支撑 type-level 结论

- **具体位置**: §4.4 (Human validation), Appendix G (Per-Type Judge Reliability)
- **问题**: Total n=100, per-type n=32-34。论文承认"lack power for type-level comparison"（§4.4），但 Appendix G 仍然报告 per-type κ 并从中得出结论（如"Authorization scope has the lowest human-LLM κ"）。CIs 极宽：scopal κ 95% CI = [0.00, 1.00]，coreferential κ CI = [0.00, 0.84]——这些是完全无信息的区间。
- **建议**: (1) 在 Appendix G 中明确声明 per-type 结果仅为 descriptive/suggestive，不应用于 type-level ranking；(2) 考虑移除或弱化基于 per-type κ 的推断。

**W3** [warning] Judge family bias (both OpenAI) 对 cross-model comparison 的潜在系统效应

- **具体位置**: Limitations (Measurement paragraph)
- **问题**: 两个 judge 都来自 OpenAI model family。论文在 Limitations 中提及"potentially introducing systematic within-family evaluation bias"，但未进一步分析其潜在方向或量级。Claude 被评为最低 violation rate (30.3%)——这可能反映真实 robustness，也可能反映 OpenAI judge 对非 OpenAI 输出的系统性偏差（如对不同格式/风格的偏好）。该 confound 与 N2 叠加放大了 C4 结论的不确定性。
- **建议**: (1) 讨论 judge family bias 的可能方向（如 OpenAI judges 是否可能对 OpenAI agents 更宽容或更严格）；(2) 在 Future Work 中明确建议 cross-family judge evaluation 作为必要验证。

**W4** [warning] C4 variance explained (2.9%) 的实质意义与 Discussion 中的权重不匹配

- **具体位置**: §5.4 C4, §7 Discussion (Differential nocuity)
- **问题**: C4 interaction F(20,2976)=1.97, p=0.006, 但仅解释 2.9% variance。在 n≈3000 的样本下，test 有极高的 power 检测微小效应。论文正确标注了 [Exploratory]，但 Discussion §7 的 "differential nocuity" framework 将 authorization scope 的模型差异作为核心论据之一——这给予了一个 2.9%-variance, low-κ, judge-confounded 的 exploratory finding 过高的理论权重。
- **建议**: 在 Discussion 中降低对 authorization scope 模型差异的依赖程度，或在引用时每次附加 effect size + measurement uncertainty caveat。

**W5** [warning] Perturbation control 对 specification-layer types 的适用性有限

- **具体位置**: §4.5 Controls (Perturbation control)
- **问题**: Perturbation control 使用 synonym substitution 和 clause reordering (n=300)。这些扰动在结构上与 linguistic-layer 的 ambiguity manipulation（如 scopal: 改变一个词的作用域）匹配较好，但与 specification-layer 的 manipulation（如 incompleteness: 添加整段新内容 +34.6 words；authorization scope: 添加 +36.1 words）有本质差异。synonym substitution 不会模拟添加 34 words 新内容的效果——这意味着 perturbation control 的 CI [-8.0, 6.67] 作为"非语义变化无效果"的证据，对 specification-layer types（尤其 incompleteness）的 specificity claim 支撑较弱。
- **建议**: 讨论 perturbation control 对不同类型的适用性差异；承认对 specification-layer types，perturbation control 提供的是"surface-level perturbation specificity"而非"information-addition specificity"——后者由 Appendix F 的 logistic regression 处理（但同样有 proxy 限制）。

**W6** [warning] Kendall's W 的显著性依赖子集选择

- **具体位置**: Appendix M (Cross-Model Type Ranking Concordance)
- **问题**: 5-model, 6-type 的 Kendall's W=0.398 (p=0.072) 不显著。7-model, 5-type（排除 coreferential）的 W=0.353 (p=0.038) 显著。论文同时报告了两个结果，但正文 §5.2 引用的是 "moderate" concordance——没有明确说明非显著。排除 coreferential + 加入 replication models 这一组合看起来像是选择性报告。
- **建议**: 在正文引用时明确说明 5-model 结果不显著 (p=0.072)；避免给读者"type ranking 在模型间 consistent"的印象——数据支持的是"trending toward concordance, driven by incompleteness at the top"。

---

## 小问题（不影响接收）

- **M1**: "Ambiguity" 的操作定义包含了严格意义上不是 ambiguity 的概念（incompleteness = information absence, conditional precedence = normative conflict）。§3 "Scope of ambiguity" 段已充分讨论了这一点，但建议在 Abstract 中加入一个 parenthetical 提示（如 "including specification-level gaps"）以减少初读时的概念混淆。

- **M2**: ICC=0.919 的 reproducibility 测量仅限 OpenAI family 内（GPT-5.4 + GPT-4.1, §4.5）。跨 provider reproducibility（如 Claude 的 replication stability）未直接测量。建议在报告 ICC 时注明此限制。

- **M3**: Appendix B 的五模型 mitigation study（-8.5pp pooled）与 Discussion §7 的单模型 GPT-5.4 mitigation experiment 使用不同的 prompt formulation 和实验设计（unpaired vs. matched-pair McNemar），两者结论方向不一致（Appendix B: incompleteness -3.4pp; Discussion: incompleteness +14pp worsening）。建议明确标注两个实验的设计差异，避免读者混淆。

- **M4**: Variance decomposition "clause identity 22.4% vs model identity 1.0%" (§5.1)——剩余 76.6% 为 unexplained variance（主要来自 evaluation pipeline noise）。建议报告 residual 比例以给出完整图景。

- **M5**: Within-judge-group type ranking 相关性接近零（Spearman ρ=-0.03, Appendix P），由 authorization scope 的 rank reversal 驱动。这进一步削弱了 C2 type ranking 的跨评判者稳健性——建议在 §5.2 讨论 ranking stability 时交叉引用此 appendix 结果。

---

## Questions for Authors

1. 如果使用 propositional content analysis（而非 token count）作为 information delta 的 proxy，incompleteness 的 effect 预计会如何变化？是否有 pilot data？

2. 在 within-judge-group 分析中，GPT-5.4 judged group 的 authorization scope 范围是多少（Claude, GPT-4.1, Qwen3 各多少）？GPT-4.1 judged group 呢（GPT-5.4, DeepSeek）？如果两个 judge group 内部的 range 都远小于 52pp，这将强烈暗示 judge effect。

3. 是否有计划做 cross-family judge evaluation（如 Claude judging GPT traces）以排除 judge family bias？

4. C3 layer effect 在 controlling for token delta 后 reverses direction (§5.3)——reversed 后的方向和 effect size 是多少？这对 taxonomy 的理论动机有什么影响？

---

## 主要优势

- **S1**: 首个 ambiguity type → agent safety violation 的 matched-pair 因果研究，填补了重要空白。Perturbation control + matched-pair 设计提供了优于 observational study 的因果推断基础。

- **S2**: 统计方法论整体质量高——TOST equivalence testing + bootstrap cluster + Holm-Bonferroni correction + sensitivity analysis 的组合超过了该领域大多数论文的标准。Claim calibration（C3 标注 inconclusive, C4 标注 exploratory）展示了良好的学术诚信。

- **S3**: Disambiguation Neglect 的发现（≤11% awareness）和 Systematic Nocuity（41.3% majority-convergent violations）是有价值的 empirical 贡献，对 agent safety 部署有直接实践意义。

- **S4**: 七模型覆盖（5 primary + 2 replication）跨六个 provider，是该领域中模型覆盖度最高的研究之一。

- **S5**: 论文写作清晰，结构紧凑，在 8 页正文内有效传达了复杂的实验设计和统计分析。Limitations 段落坦诚且具体。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1050 · 2026-05-22T09:57:11.013442+00:00_

Reviewer 1 审稿意见已收到。评分 3.5 (Borderline Conference)，提出 3 个 critical (SESOI 循环论证、cross-judge asymmetry 对 C4 的威胁、incompleteness confound 控制不充分)、6 个 warning、5 个 minor。等待 Reviewer 2 完成初审后进入交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 95

## Round 95

2 recorded events


### User

_source line 1051 · 2026-05-22T09:57:15.090602+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

**总结**: Overall 3.5/5 (Borderline Conference)。论文的 matched-pair 因果设计和统计方法论整体优秀，但存在三个 critical 问题需要修复：(1) TOST ±15pp SESOI 的选择对 C2 gradient claim 构成循环论证风险——gradient 结构在 ±10pp 时瓦解；(2) C4 的 cross-judge asymmetry + authorization scope κ=0.385 使 52pp range 可能受 judge effect 驱动；(3) incompleteness 的 information-addition confound 仅用 token count 控制不够充分，49.2pp effect 可能被膨胀。三个 critical + 六个 should-fix + 五个 minor issues 已详细列出修改建议。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1052 · 2026-05-22T09:57:20.799365+00:00_

Reviewer 1 意见已收到。等待 Reviewer 2 完成独立审稿后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 96

## Round 96

6 recorded events


### User

_source line 1053 · 2026-05-22T09:58:12.208787+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 审稿意见（Round 1）—— 新颖性/完整性审查

### 总体评分
**Overall**: 3.5 (Borderline Conference)
**一句话总结**: 方法论扎实的 matched-pair 因果研究，但 taxonomy 理论张力未完全解决，核心贡献的新颖性增量有限，incompleteness confound 削弱了最显著的发现。

### 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 实验设计严谨（matched-pair + perturbation control），统计方法全面（TOST、bootstrap、Holm-Bonferroni），但 incompleteness confound 仅部分解决，mitigation 两组实验方向性矛盾削弱结论可靠性 |
| Excitement | 3/5 | 研究问题有实际意义，但主要发现在直觉上可预期；Disambiguation Neglect 是已知现象的 setting 迁移；taxonomy 解释力很低（between-type variance 仅 0.4%） |
| Reproducibility | 4/5 | 方法描述详尽，承诺开源，7 模型跨 6 provider 复制出色；单一 benchmark 限制跨领域可复现性 |
| Reviewer Confidence | 4/5 | 对实验设计、因果推断和 LLM agent safety 领域较熟悉 |

---

### Must-Fix 问题（影响接收决定）

**N1** [critical] Contribution (2) "22× more variance" 措辞具有误导性
- 位置：Abstract、§1 Introduction (contribution list)、§8 Conclusion
- §5.1 分解显示 22.4% clause-level variance 中，between-type 仅 0.4%，within-type 22.0%。taxonomy 本身仅解释 0.4% 方差。在 contributions list 中紧跟 C2 提出 "22×" claim，读者自然理解为 taxonomy 解释力很强，与实际数据不符。构成 overclaiming。
- 建议：(1) contributions 中区分 clause-level vs type-level variance；(2) 在 §5.1 讨论 0.4% 对 taxonomy 实用价值的含义；(3) 将 "22×" 从 contribution 降级为 supporting evidence。

**N2** [critical] Taxonomy 理论连贯性：incompleteness 和 conditional precedence 不属于传统 "ambiguity" 定义
- 位置：§3 "Scope of ambiguity"、Title、Abstract
- §3 承认 incompleteness 是 information absence，conditional precedence 是 normative conflict，非 ambiguity。辩护理由是 "agents process all six types identically"，但这是 empirical observation 非 theoretical justification。标题和 abstract 统称六种类型为 "ambiguity"，从 RE/formal semantics 角度是 category error。
- 建议：(1) 用更宽泛术语如 "policy underspecification"；或 (2) 在 §1 即限定 scope（"ambiguity and related specification defects"）；(3) 不要到 §3 末尾才回应定义偏离。

---

### Should-Fix 问题

**W1** [warning] Mitigation 实验结论矛盾
- §7 GPT-5.4 type-specific: auth scope −12pp, incompleteness +14pp
- Appendix B GPT-5.4: auth scope −40.0pp, incompleteness −2.6pp
- 同一模型同一类型，换 prompt 从 +14 变 −2.6pp。论文仅用一句话解释，未分析具体原因。如果 mitigation 对 prompt wording 如此敏感，practical implications 的实证基础不可靠。
- 建议：报告两组 prompt 内容，讨论 sensitivity 本身作为 finding。

**W2** [warning] "Disambiguation Neglect" novelty 需更精确定位
- Liu et al. (2023) ambiguity collapse + Hu et al. (2025) missing concepts 已建立核心现象。本文贡献是 quantifying 已知现象在 agentic setting 的存在，非发现新现象。Contribution (3) framing 应从 "revealing" 调整为 "quantifying severity in consequential agentic settings"。

**W3** [warning] Incompleteness confound mitigation 不够充分
- Token count 是 information content 的粗糙 proxy（论文自承）；auth scope 的更大 token delta 不能作为 counter-evidence（内容性质不同：boundary specification vs entirely new information）。
- 建议：对 49.2pp effect 附加更明确的 upper-bound caveat，讨论理想控制实验设计。

**W4** [warning] 单一 benchmark 外部效度
- 所有实验仅在 τ²-bench (retail + airline) 上进行，但 abstract/conclusion 暗示更广泛 generalizability。
- 建议：加入 domain 限定语。

---

### 小问题

- M1: §5.3 C3 null result 可压缩
- M2: Table 2 caption 过长
- M3: §5.4 bootstrap ranking preservation 限制条件应在正文说明
- M4: 部分 arXiv preprint 引用需核查完整性
- M5: 4.6% vs ≤11% 两个 awareness 数字在不同位置交替使用，建议统一

---

### 主要优势

- E1: matched-pair 因果设计 + perturbation control + ICC=0.919 是该领域少见的方法论严谨性
- E2: TOST equivalence testing + bootstrap cluster + 多重比较校正——统计方法全面且恰当
- E3: C3 null result 未隐藏，incompleteness confound 多角度讨论，auth scope 低 κ 反复标注——intellectual honesty 出色
- E4: 7 models × 6 providers, 2997+ episodes 的规模
- E5: ambiguity type→failure mode 映射（§6.1）有直接实用价值

---

### Questions to Authors

1. Between-type variance 仅 0.4%：taxonomy 主要价值是否在 failure mode prediction（§6.1）而非 variance explanation？贡献声明是否应重新聚焦？
2. 排除 incompleteness 后剩余五类型 omnibus p=0.079——C2 claim 是否过度依赖 incompleteness 这一个类型？
3. 是否有与 DRIP-R 真实 policy ambiguity 实例的 qualitative comparison 来评估生态效度？

### Missing References
- 未发现重大遗漏。建议在 §2 Agent Safety 中引用 "The Causal Impact of Tool Affordance on Safety Alignment" (arXiv:2603.20320)，其 matched-pair 设计与本文方法论相关。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1054 · 2026-05-22T09:58:54.373367+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "project": "policy_ambiguity_safety",
  "round_number": "1",
  "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应。对每个观点标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿意见（方法严谨性）\n\n**Overall**: 3.5 / 5 — Borderline Conference\n\n### Must-Fix\n\n**N1** [critical] TOST ±15pp SESOI 选择的循环论证风险\n- §4.6: SESOI 论证为\"超过 perturbation control bound (6.67pp) 的 >2×\"，但 perturbation control bound 本身取决于扰动类型选择。C2 \"risk gradient\" 在 ±10pp 时仅 3/6 mid-tier pairs 等价，gradient 结构瓦解。sensitivity analysis 提供了 7 个 margin（Table 3），但正文 claim 仅在 ±15pp 成立——这个 margin-dependence 应上升为 claim 声明的一部分。\n- 建议：(1) C2 claim 每次陈述附加 margin 条件；(2) Abstract/Intro 明确 gradient 的 margin-dependent 性质；(3) 讨论 field-standard SESOI 缺失对结论稳健性的影响。\n\n**N2** [critical] Cross-judge asymmetry 对 C4 interaction 结论的系统性威胁\n- GPT-5.4 judges Claude/GPT-4.1/Qwen3, GPT-4.1 judges GPT-5.4/DeepSeek。C4 的 interaction F-test 操作 absolute violation rates across models，这些来自不同 judge。Authorization scope 52pp range 中 Claude(12%) 和 GPT-5.4(64%) 由不同 judge 评判，且 auth scope κ=0.385 最低。52pp 可能部分反映 judge 判定标准差异。Figure 3 heatmap 和\"most model-differentiating type\"措辞给读者印象远强于 caveat。\n- 建议：(1) Figure 3 caption 标注 judge assignment；(2) 提升 caveat 到 Figure caption 和 Discussion；(3) 报告 within-judge-group 的 auth scope range。\n\n**N3** [critical] Incompleteness information-addition confound 控制不充分\n- Token count 作为 information addition proxy 不够：(a) 无法区分 informativeness vs 冗余度；(b) 不同类型的 token delta 语义权重不同；(c) auth scope +36.1 words 但为 boundary specification，incompleteness +34.6 words 为全新 policy content——跨类型比较非 apples-to-apples。\n- 建议：(1) 更一致地标注 incompleteness effect 为 upper bound；(2) 以 coreferential 18.7pp 作为 confound-free anchor；(3) 讨论替代 proxy。\n\n### Should-Fix\n\n**W1**: Bootstrap cluster AU p=0.47 不支持 incompleteness 作为 distinct upper-bound cluster。\n**W2**: Human validation per-type n=32-34，CIs 极宽（scopal κ CI=[0.00, 1.00]），不应用于 type-level ranking。\n**W3**: Judge family bias (both OpenAI) 对 cross-model comparison 的潜在系统效应，尤其 Claude 30.3% 最低 violation rate 可能反映 judge bias。\n**W4**: C4 variance explained 仅 2.9%，但 Discussion 中 differential nocuity 框架给予了过高理论权重。\n**W5**: Perturbation control (synonym substitution, clause reordering) 与 specification-layer types 的 manipulation (+34 words) 在结构上不匹配。\n**W6**: Kendall's W 5-model p=0.072 不显著，7-model 排除 coreferential 后 p=0.038 显著——subset 选择性报告风险。\n\n### Minor\nM1: \"Ambiguity\" 操作定义含非 ambiguity 概念，建议 Abstract 加 parenthetical。\nM2: ICC=0.919 仅限 OpenAI family 内。\nM3: Appendix B 与 Discussion §7 mitigation 方向矛盾需明确标注设计差异。\nM4: Variance decomposition 剩余 76.6% unexplained variance 应报告。\nM5: Within-judge-group type ranking ρ=-0.03 进一步削弱 C2 ranking stability。\n\n### Strengths\nS1: 首个 matched-pair 因果研究。S2: 统计方法论质量高。S3: Disambiguation Neglect + Systematic Nocuity 有价值。S4: 7 模型跨 6 provider。S5: 写作清晰，limitations 坦诚。\n\n---\n\n请逐条回应 Reviewer 1 的所有观点（Must-Fix、Should-Fix、Minor、Strengths）。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "project": "policy_ambiguity_safety",
    "round_number": "1",
    "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应。对每个观点标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿意见（方法严谨性）\n\n**Overall**: 3.5 / 5 — Borderline Conference\n\n### Must-Fix\n\n**N1** [critical] TOST ±15pp SESOI 选择的循环论证风险\n- §4.6: SESOI 论证为\"超过 perturbation control bound (6.67pp) 的 >2×\"，但 perturbation control bound 本身取决于扰动类型选择。C2 \"risk gradient\" 在 ±10pp 时仅 3/6 mid-tier pairs 等价，gradient 结构瓦解。sensitivity analysis 提供了 7 个 margin（Table 3），但正文 claim 仅在 ±15pp 成立——这个 margin-dependence 应上升为 claim 声明的一部分。\n- 建议：(1) C2 claim 每次陈述附加 margin 条件；(2) Abstract/Intro 明确 gradient 的 margin-dependent 性质；(3) 讨论 field-standard SESOI 缺失对结论稳健性的影响。\n\n**N2** [critical] Cross-judge asymmetry 对 C4 interaction 结论的系统性威胁\n- GPT-5.4 judges Claude/GPT-4.1/Qwen3, GPT-4.1 judges GPT-5.4/DeepSeek。C4 的 interaction F-test 操作 absolute violation rates across models，这些来自不同 judge。Authorization scope 52pp range 中 Claude(12%) 和 GPT-5.4(64%) 由不同 judge 评判，且 auth scope κ=0.385 最低。52pp 可能部分反映 judge 判定标准差异。Figure 3 heatmap 和\"most model-differentiating type\"措辞给读者印象远强于 caveat。\n- 建议：(1) Figure 3 caption 标注 judge assignment；(2) 提升 caveat 到 Figure caption 和 Discussion；(3) 报告 within-judge-group 的 auth scope range。\n\n**N3** [critical] Incompleteness information-addition confound 控制不充分\n- Token count 作为 information addition proxy 不够：(a) 无法区分 informativeness vs 冗余度；(b) 不同类型的 token delta 语义权重不同；(c) auth scope +36.1 words 但为 boundary specification，incompleteness +34.6 words 为全新 policy content——跨类型比较非 apples-to-apples。\n- 建议：(1) 更一致地标注 incompleteness effect 为 upper bound；(2) 以 coreferential 18.7pp 作为 confound-free anchor；(3) 讨论替代 proxy。\n\n### Should-Fix\n\n**W1**: Bootstrap cluster AU p=0.47 不支持 incompleteness 作为 distinct upper-bound cluster。\n**W2**: Human validation per-type n=32-34，CIs 极宽（scopal κ CI=[0.00, 1.00]），不应用于 type-level ranking。\n**W3**: Judge family bias (both OpenAI) 对 cross-model comparison 的潜在系统效应，尤其 Claude 30.3% 最低 violation rate 可能反映 judge bias。\n**W4**: C4 variance explained 仅 2.9%，但 Discussion 中 differential nocuity 框架给予了过高理论权重。\n**W5**: Perturbation control (synonym substitution, clause reordering) 与 specification-layer types 的 manipulation (+34 words) 在结构上不匹配。\n**W6**: Kendall's W 5-model p=0.072 不显著，7-model 排除 coreferential 后 p=0.038 显著——subset 选择性报告风险。\n\n### Minor\nM1: \"Ambiguity\" 操作定义含非 ambiguity 概念，建议 Abstract 加 parenthetical。\nM2: ICC=0.919 仅限 OpenAI family 内。\nM3: Appendix B 与 Discussion §7 mitigation 方向矛盾需明确标注设计差异。\nM4: Variance decomposition 剩余 76.6% unexplained variance 应报告。\nM5: Within-judge-group type ranking ρ=-0.03 进一步削弱 C2 ranking stability。\n\n### Strengths\nS1: 首个 matched-pair 因果研究。S2: 统计方法论质量高。S3: Disambiguation Neglect + Systematic Nocuity 有价值。S4: 7 模型跨 6 provider。S5: 写作清晰，limitations 坦诚。\n\n---\n\n请逐条回应 Reviewer 1 的所有观点（Must-Fix、Should-Fix、Minor、Strengths）。"
  }
}
```

</details>

---


### Tool result

_source line 1055 · 2026-05-22T09:59:04.216254+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 9842
}
```

</details>

---


### Tool call

_source line 1056 · 2026-05-22T09:59:04.668067+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "project": "policy_ambiguity_safety",
  "round_number": "1",
  "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应。对每个观点标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿意见（新颖性/完整性）\n\n**Overall**: 3.5 (Borderline Conference)\n\n### Must-Fix\n\n**N1** [critical] Contribution (2) \"22× more variance\" 措辞具有误导性\n- §5.1 分解：22.4% clause-level variance 中 between-type 仅 0.4%，within-type 22.0%。Taxonomy 本身仅解释 0.4% 方差。在 contributions list 中紧跟 C2 提出 \"22×\" claim，读者自然理解为 taxonomy 解释力强，与数据不符——overclaiming。\n- 建议：(1) contributions 区分 clause-level vs type-level variance；(2) §5.1 讨论 0.4% 对 taxonomy 实用价值的含义；(3) \"22×\" 从 contribution 降级为 supporting evidence。\n\n**N2** [critical] Taxonomy 理论连贯性：incompleteness 和 conditional precedence 不属传统 \"ambiguity\"\n- §3 承认 incompleteness 是 information absence, conditional precedence 是 normative conflict。辩护\"agents process all six types identically\"是 empirical observation 非 theoretical justification。标题和 abstract 统称六类为 \"ambiguity\" 构成 category error。\n- 建议：(1) 用 \"policy underspecification\" 等更宽泛术语；或 (2) §1 即限定 scope；(3) 不要到 §3 才回应定义偏离。\n\n### Should-Fix\n\n**W1**: Mitigation 实验方向矛盾（§7 GPT-5.4 incompleteness +14pp vs Appendix B −2.6pp），prompt wording sensitivity 削弱 practical implications。\n**W2**: \"Disambiguation Neglect\" 是已知现象在 agentic setting 的 quantification，非新发现。Contribution (3) 应从 \"revealing\" 调整为 \"quantifying in consequential agentic settings\"。\n**W3**: Incompleteness confound token count proxy 不充分。\n**W4**: 单一 benchmark (τ²-bench) 外部效度，abstract/conclusion 暗示更广泛 generalizability。\n\n### Minor\nM1: C3 null result 可压缩。M2: Table 2 caption 过长。M3: bootstrap ranking preservation 限制条件应在正文说明。M4: arXiv preprint 引用完整性。M5: 4.6% vs ≤11% awareness 数字交替使用。\n\n### Strengths\nE1: matched-pair 因果设计方法论严谨。E2: 统计方法全面恰当。E3: 学术诚信出色。E4: 7 models × 6 providers 规模。E5: type→failure mode 映射有实用价值。\n\n### Questions\n1. Between-type variance 仅 0.4%：taxonomy 价值是否在 failure mode prediction 而非 variance explanation？\n2. 排除 incompleteness 后 omnibus p=0.079——C2 是否过度依赖 incompleteness？\n3. 是否有与 DRIP-R 真实 policy ambiguity 的 qualitative comparison 评估生态效度？\n\n### Missing References\n建议引用 \"The Causal Impact of Tool Affordance on Safety Alignment\" (arXiv:2603.20320)。\n\n---\n\n请逐条回应 Reviewer 2 的所有观点（Must-Fix、Should-Fix、Minor、Strengths、Questions）。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "project": "policy_ambiguity_safety",
    "round_number": "1",
    "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应。对每个观点标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿意见（新颖性/完整性）\n\n**Overall**: 3.5 (Borderline Conference)\n\n### Must-Fix\n\n**N1** [critical] Contribution (2) \"22× more variance\" 措辞具有误导性\n- §5.1 分解：22.4% clause-level variance 中 between-type 仅 0.4%，within-type 22.0%。Taxonomy 本身仅解释 0.4% 方差。在 contributions list 中紧跟 C2 提出 \"22×\" claim，读者自然理解为 taxonomy 解释力强，与数据不符——overclaiming。\n- 建议：(1) contributions 区分 clause-level vs type-level variance；(2) §5.1 讨论 0.4% 对 taxonomy 实用价值的含义；(3) \"22×\" 从 contribution 降级为 supporting evidence。\n\n**N2** [critical] Taxonomy 理论连贯性：incompleteness 和 conditional precedence 不属传统 \"ambiguity\"\n- §3 承认 incompleteness 是 information absence, conditional precedence 是 normative conflict。辩护\"agents process all six types identically\"是 empirical observation 非 theoretical justification。标题和 abstract 统称六类为 \"ambiguity\" 构成 category error。\n- 建议：(1) 用 \"policy underspecification\" 等更宽泛术语；或 (2) §1 即限定 scope；(3) 不要到 §3 才回应定义偏离。\n\n### Should-Fix\n\n**W1**: Mitigation 实验方向矛盾（§7 GPT-5.4 incompleteness +14pp vs Appendix B −2.6pp），prompt wording sensitivity 削弱 practical implications。\n**W2**: \"Disambiguation Neglect\" 是已知现象在 agentic setting 的 quantification，非新发现。Contribution (3) 应从 \"revealing\" 调整为 \"quantifying in consequential agentic settings\"。\n**W3**: Incompleteness confound token count proxy 不充分。\n**W4**: 单一 benchmark (τ²-bench) 外部效度，abstract/conclusion 暗示更广泛 generalizability。\n\n### Minor\nM1: C3 null result 可压缩。M2: Table 2 caption 过长。M3: bootstrap ranking preservation 限制条件应在正文说明。M4: arXiv preprint 引用完整性。M5: 4.6% vs ≤11% awareness 数字交替使用。\n\n### Strengths\nE1: matched-pair 因果设计方法论严谨。E2: 统计方法全面恰当。E3: 学术诚信出色。E4: 7 models × 6 providers 规模。E5: type→failure mode 映射有实用价值。\n\n### Questions\n1. Between-type variance 仅 0.4%：taxonomy 价值是否在 failure mode prediction 而非 variance explanation？\n2. 排除 incompleteness 后 omnibus p=0.079——C2 是否过度依赖 incompleteness？\n3. 是否有与 DRIP-R 真实 policy ambiguity 的 qualitative comparison 评估生态效度？\n\n### Missing References\n建议引用 \"The Causal Impact of Tool Affordance on Safety Alignment\" (arXiv:2603.20320)。\n\n---\n\n请逐条回应 Reviewer 2 的所有观点（Must-Fix、Should-Fix、Minor、Strengths、Questions）。"
  }
}
```

</details>

---


### Tool result

_source line 1057 · 2026-05-22T09:59:06.228489+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1560
}
```

</details>

---


### Assistant

_source line 1058 · 2026-05-22T09:59:09.881302+00:00_

交叉分享已发出，等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 97

## Round 97

2 recorded events


### User

_source line 1059 · 2026-05-22T09:59:12.556887+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

总结：

- **Overall 3.5 (Borderline Conference)**
- 2 个 Must-Fix：(N1) "22× variance" claim 误导性——taxonomy 实际仅解释 0.4% between-type variance；(N2) taxonomy 将 incompleteness/conditional precedence 归为 "ambiguity" 存在理论张力，标题和 abstract 需调整
- 4 个 Should-Fix：mitigation 实验矛盾 (W1)、Disambiguation Neglect novelty 定位 (W2)、incompleteness confound (W3)、单一 benchmark 外部效度 (W4)
- 主要优势在于 matched-pair 因果设计的方法论严谨性、统计方法的全面性、以及报告的透明诚实

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1060 · 2026-05-22T09:59:17.010526+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 98

## Round 98

2 recorded events


### User

_source line 1061 · 2026-05-22T10:00:49.660433+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 意见的交叉回应

---

### Must-Fix

**[AGREE] R2-N1: "22× more variance" 措辞误导性**

同意这是 overclaiming。§5.1 的 variance decomposition 显示 clause identity 22.4% 中 between-type 仅 0.4%、within-type 22.0%。"22×" 指的是 clause vs. model（22.4% vs 1.0%），但放在 contributions list 中紧跟 C2（type-level gradient），读者确实容易误读为 taxonomy（type-level）的解释力。

补充我自己的观察：22.4% clause-level variance 的另一面是 76.6% unexplained variance（我在 M4 中指出），主要来自 evaluation pipeline noise。即便 clause > model 的比较成立，绝对数字说明 measurement noise 仍然主导——这进一步削弱了将 "22×" 作为 headline contribution 的合理性。

R2 的修改建议合理：将 "22×" 从 contribution 降级为 supporting evidence，并在 §5.1 区分 clause-level vs type-level variance 的含义。

**[REBUT] R2-N2: Taxonomy 理论连贯性——incompleteness/conditional precedence 不属传统 ambiguity**

R2 的概念关切有道理，但建议的修改方向过重。论文 §3 "Scope of ambiguity" 段落已经明确承认 incompleteness 是 information absence、conditional precedence 是 normative conflict，并给出了 pragmatic justification：(1) agents process all six types identically（commit to single interpretation without flagging uncertainty, §3 末段）；(2) resulting safety violations are behaviorally indistinguishable（§5.1-5.2 所有类型都产生显著的 Δpp）；(3) Dalpiaz et al. (2018) 的文献支持 ambiguity/incompleteness 经常 co-occur。

R2 说这是"empirical observation 非 theoretical justification"——但在实证研究中，empirical observation *就是* 最恰当的 justification。论文的核心是实证因果研究，不是 taxonomy 的理论建构。改用 "policy underspecification" 会弱化与 decades of RE ambiguity research（Berry & Kamsties 2004, Massey et al. 2014）的衔接，也丢掉 nocuous/innocuous ambiguity 的框架连接。

不过我同意 R2 的一个子点：scope 限定应当在 §1 Introduction 中前置，而非到 §3 才回应。建议在 §1 的 taxonomy 介绍处加一句 parenthetical（如 "including specification-level gaps that, while not ambiguity in the strict linguistic sense, produce identical behavioral outcomes in LLM agents"），这比改标题或术语更精准。

---

### Should-Fix

**[AGREE] R2-W1: Mitigation 实验方向矛盾**

完全同意。§7 Discussion 的单模型 GPT-5.4 matched-pair McNemar 实验显示 incompleteness +14pp（worsening, p=0.118），而 Appendix B 的五模型 unpaired 实验显示 incompleteness -2.6pp（GPT-5.4）/-3.4pp（pooled）。两个实验用了不同的 prompt formulation 和实验设计（unpaired vs matched-pair），但论文未在正文中清晰标注这一差异。我在自己的审稿中也指出了这一点（M3）。

这不仅是 presentation 问题——它实质性地削弱了 Discussion 中 "mitigation outcomes appear sensitive to prompt wording" 的结论可信度，因为两个不同实验可能测量的是不同的 construct。

**[AGREE] R2-W2: Disambiguation Neglect 是 quantification 而非 discovery**

同意。Liu et al. (2023) 和 Hu et al. (2025) 已经报告了 LLM 的 ambiguity collapse 现象（§2 Related Work, §6.2 明确引用）。论文的增量贡献是 (a) 在 consequential agentic setting 中量化（4.6% overall, max 11% per-model）和 (b) 发现 systematic nocuity（41.3% majority-convergent, §6.3）。Contribution (3) 从 "revealing" 改为 "quantifying in consequential agentic settings and identifying systematic nocuity" 更准确，同时保留 systematic nocuity 这一确实新颖的发现。

**[AGREE] R2-W3: Incompleteness confound token count proxy 不充分**

完全同意，与我自己的 N3 一致。Token count 作为 information content 的 proxy 过于粗糙——论文自己在 Appendix F 也承认。不再赘述。

**[AGREE] R2-W4: 单一 benchmark 外部效度**

同意关切，但严重程度应略低于 R2 的评估。论文使用的 τ²-bench 本身覆盖两个 domain（retail + airline customer service, §4.1），且 cross-domain consistency 是令人鼓舞的。Limitations §明确声明 "effects in other domains remain untested"。不过我同意 Abstract 和 Conclusion 的措辞（"LLM-based agents" 而非 "LLM-based customer service agents"）暗示了过广的 generalizability。建议在 Abstract 和 Conclusion 中限定 domain scope。

---

### Minor

**[AGREE] R2-M1: C3 null result 可压缩**

同意可以压缩，但不应完全移除。报告 null results 是良好的学术实践。目前 §5.3 约 6 行，可压缩到 3-4 行：保留 p=0.017 不过 correction、controlling for token delta reverses direction、taxonomy value independent of layer grouping。

**[AGREE] R2-M2: Table 2 caption 过长**

同意。Table 2 caption 包含了方法细节（TOST 解释、Tier 定义、p-value 注释），可将 Tier 定义移至脚注或正文。

**[AGREE] R2-M3: Bootstrap ranking preservation 限制条件**

同意。§5.4 报告 "bootstrap ranking preservation: 99.5%, B=10,000" 但未在正文中说明这是 within GPT-5.4 judge subset 的结果。限制条件应当明确。

**[REBUT] R2-M4: arXiv preprint 引用完整性**

我无法从论文 PDF 中确认具体哪些 arXiv 引用不完整。R2 未给出具体条目。如果能指出哪些引用有问题，可以更有针对性地回应。但一般性地，preprint 引用标注为 "arXiv preprint" 而非已发表版本是常见问题，值得检查。

**[AGREE] R2-M5: 4.6% vs ≤11% awareness 数字交替使用**

同意。4.6% 是 overall 平均（§6.2），≤11% 是 per-model maximum（Claude 11.0%, §6.2），两者语义不同但在 Introduction §1 和 §6.2 中交替出现。建议统一使用一个数字并在首次出现时注明另一个。

---

### Strengths

**[AGREE] R2-E1 through E5**

全部同意。这些也与我的 S1-S5 评价一致。特别赞同 E3（学术诚信出色）——C3 标注 inconclusive、C4 标注 exploratory、authorization scope caveat 反复出现，在该领域论文中难能可贵。E5（type→failure mode mapping）是我审稿中未充分强调的优点——§6.1 的三种 failure mechanism（structural misparse, information gap-filling, boundary violation）与 ambiguity type 的映射关系清晰，且在 ≥3/5 models 中保持一致，具有实际部署价值。

---

### Questions 回应

**R2-Q1**: Between-type variance 仅 0.4%——taxonomy 价值在 failure mode prediction 而非 variance explanation？

这是一个 insightful 的问题。我同意 taxonomy 的主要价值可能在于 §6.1 的 type→failure mode 映射（每种类型有 distinct 的 dominant failure mechanism），而非 type-level variance explanation。§5.1 的数据实际上支持"clause wording 比 type membership 重要 55 倍"（22.0% within-type / 0.4% between-type），这削弱了 taxonomy 作为 variance-explaining 框架的价值，但不削弱其作为 failure-mode-predicting 框架的价值。论文应更清晰地定位 taxonomy 的价值来源。

**R2-Q2**: 排除 incompleteness 后 omnibus p=0.079——C2 是否过度依赖 incompleteness？

关键问题。Appendix F 报告排除 incompleteness 后 omnibus p=0.079，但 pairwise Holm-Bonferroni 仍有两对显著（auth scope vs coreferential p_adj=0.039, lexical vs coreferential p_adj=0.025）。这说明 C2 的 omnibus 结论确实依赖 incompleteness，但 pairwise gradient 不完全依赖它。论文应当明确区分：(a) omnibus "types are not interchangeable" 依赖 incompleteness；(b) pairwise gradient 在排除 incompleteness 后仍有部分支撑（coreferential 显著低于 auth scope 和 lexical）。这与我的 N1（SESOI margin dependence）叠加——C2 claim 需要更谨慎的表述。

**R2-Q3**: 与 DRIP-R 的 qualitative comparison？

论文在 Appendix L 提供了 DRIP-R 的 category mapping（5 RE types → 6-type taxonomy），但没有在 DRIP-R 的真实 policy ambiguity instances 上做 empirical comparison。这确实是一个 ecological validity gap——论文的 300 clause pairs 是 synthetic（template-based, §4.2），与 naturally occurring ambiguity 的分布可能不同（Limitations §已承认）。DRIP-R 作为 concurrent work 提供了天然的比较基准。

---

### Missing References

**[REBUT] R2-Missing Ref: "The Causal Impact of Tool Affordance on Safety Alignment" (arXiv:2603.20320)**

无法验证此引用的存在性（arXiv ID 2603.xxxxx 的格式对应 2026年3月，需要确认）。但如果该论文确实研究 tool affordance 对 safety 的因果影响，与本文的关联性可能限于 agent safety 的广义主题——本文的核心贡献是 ambiguity type → violation 的映射，而非 tool affordance。如果 R2 能说明具体哪个 section 应引用、该引用如何改变本文的论证结构，会更有建设性。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1062 · 2026-05-22T10:01:03.457539+00:00_

Reviewer 1 对 Reviewer 2 的交叉回应已收到。等待 Reviewer 2 对 Reviewer 1 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 99

## Round 99

2 recorded events


### User

_source line 1063 · 2026-05-22T10:01:07.165474+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。总结：

- **AGREE** 10 条：N1（22× overclaiming）、W1-W4、M1-M3、M5，以及全部 5 个 Strengths
- **REBUT** 3 条：N2（taxonomy 术语——同意前置 scope 但反对改标题）、M4（需具体指出哪些引用）、Missing Ref（无法验证且关联性存疑）

核心共识点：R2 和我都认为 C2 claim 需要校准——(1) incompleteness confound 控制不足，(2) 排除 incompleteness 后 omnibus p=0.079，(3) 22× 从 contribution 降级。两位 reviewer 给出相同的 Overall 3.5，bottleneck 一致集中在 claim calibration 而非方法设计本身。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1064 · 2026-05-22T10:01:11.925547+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 100

## Round 100

10 recorded events


### User

_source line 1065 · 2026-05-22T10:01:28.266350+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 交叉回应 Reviewer 1（Round 1 补充）

### 逐条回应摘要

**Must-Fix:**
- [AGREE w/ qualification] R1-N1 (SESOI 循环论证): 同意 margin-dependence 应入 claim，但循环论证定性过度——§4.6 有独立的 domain justification。
- [AGREE] R1-N2 (Cross-judge asymmetry on C4): 完全同意。52pp range 跨 judge 边界，auth scope κ=0.385，Figure 3 和 Discussion 均需标注。与我未涉及的 Appendix P ρ=−0.03 构成同一问题两面。
- [AGREE] R1-N3 (Incompleteness confound): 与我的 W3 完全一致。补充：Appendix F token delta OR=1.022/token 对 ~35 tokens 累积 ~2.15× odds multiplier，非可忽略。

**Should-Fix:**
- [AGREE w/ qual] R1-W1 (Bootstrap AU=0.47): TOST 是主要证据，bootstrap 仅 supplementary。建议弱化 "corroborates" 措辞。
- [AGREE] R1-W2 (Per-type n=32-34): CIs 极宽无信息量。
- [AGREE] R1-W3 (Judge family bias): 主要威胁 C4（已标 Exploratory），C1/C2 部分隔离。
- [AGREE] R1-W4 (C4 2.9% → 过高理论权重): 建议 differential nocuity 定位为 hypothesis 而非 framework。
- [REBUT] R1-W5 (Perturbation control 结构不匹配): §4.5 明确 perturbation control 和 logistic regression 有分工，前者仅控制 surface perturbation，后者控制 information addition。R1 错置了 perturbation control 的设计意图。
- [AGREE w/ qual] R1-W6 (Kendall's W 选择性报告): 排除 coreferential 有方法论理由，但正文应报告 5-model p=0.072 而非仅用 "moderate"。

**Minor:** M1-M5 全部同意。M1 与我的 N2 重叠，我将其提升为 critical。M4 (76.6% unexplained variance) 强化了我的 N1 论点。

### 综合判断
与 R1 在大方向上高度一致，分歧仅在 W5 (perturbation control 分工设计) 和部分 severity 判断上。合并两份 review，论文有 4 个 critical issues（R1-N1/N2/N3 + R2-N1），其中 R1-N3≈R2-W3。若 revision 解决：C2 加 margin 条件、Figure 3 标注 judge、incompleteness 标注 upper bound、22× claim 重新定位——可升至 4.0。当前 3.5 维持。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1066 · 2026-05-22T10:01:54.370101+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "policy_ambiguity_safety"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "policy_ambiguity_safety"
  }
}
```

</details>

---


### Tool result

_source line 1067 · 2026-05-22T10:01:54.521214+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-22T09:51:40.011289+00:00\", \"completed_at\": \"2026-05-22T09:54:26.219938+00:00\", \"findings\": [{\"severity\": \"warning\", \"dimension\": \"page 4-5\", \"message\": \"Method 部分（§4）连续两页纯文本，无任何 display item 穿插。审稿人在这一段容易失去视觉锚点。建议考虑将 matched-pair design 或 perturbation control 流程用简图/伪代码可视化\"}, {\"severity\": \"warning\", \"dimension\": \"page 8\", \"message\": \"最后一页主文本（§6.2 Disambiguation Neglect → §6.3 Systematic Noculity → §7 Discussion → §8 Conclusion → Limitations）压缩了 5 个 section/subsection 在单页内，阅读节奏急促，给审稿人\\\"空间不够、匆忙收尾\\\"的印象\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"Figure 2（Type-specific effects bar chart）为单栏宽度，bar 标签和 axis tick 字号偏小（约正文 60-65%），打印阅读时可能需要放大。建议适当增大字号或使用 figure* 全宽展示\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Figure 3 heatmap 单元格内注释数字字号偏小，在低分辨率屏幕或打印件上可能不够清晰。当前仍可读但处于边界\"}, {\"severity\": \"info\", \"dimension\": \"page 15\", \"message\": \"Appendix 末页（Section P + Q）内容仅占约 1/3 页面，大面积空白。因为是 appendix 最后一页，影响较小\"}, {\"severity\": \"info\", \"dimension\": \"page 2\", \"message\": \"Figure 1 三个面板视觉风格略有不统一（左侧层级树 vs 中间表格列表 vs 右侧流程图），但信息传达不受影响\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"Table 2 使用 booktabs 风格，最优值已加粗，数字精度统一（1 位小数），格式规范\"}, {\"severity\": \"info\", \"dimension\": \"page 3\", \"message\": \"Table 1（taxonomy 定义表）格式整洁，Resolution Channel 列信息有助于审稿人快速理解分类逻辑\"}], \"counts\": {\"critical\": 0, \"warning\": 2, \"info\": 6}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 1068 · 2026-05-22T10:01:54.521668+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "policy_ambiguity_safety"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "policy_ambiguity_safety"
  }
}
```

</details>

---


### Tool result

_source line 1069 · 2026-05-22T10:01:54.572126+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1070 · 2026-05-22T10:07:32.354578+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "policy_ambiguity_safety",
  "issues_yaml": "## Review Issues Tracker — policy_ambiguity_safety\n## Paper: \"Not All Policy Ambiguity Is Equal: Type-Specific Safety Risks for LLM Agents\"\n## Venue: EMNLP 2026 via ARR May cycle\n## Latest Round: 12 (Score: 3.5 Borderline Conference)\n## Upgrade path: fix 4 MF claim calibrations + 3 SF framing adjustments → 4.0\n\n# ============================================================\n# CRITICAL ISSUES\n# ============================================================\n\n- id: \"R11-C1\"\n  summary: \"22× variance claim 误导性 — taxonomy 仅解释 0.4% between-type variance, 22× 是 clause vs model\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 12\n  mentions:\n    - round: 11\n      reviewers: [R2, R1]\n      note: \"W6. clause_within_type=22.0% vs ambiguity_type=0.4%. Introduction contribution (2) '22× type identity' 是 clause identity 不是 type identity。\"\n    - round: 12\n      reviewers: [R2, R1]\n      note: \"MF-1. 两位 Reviewer 共识: 22× 放在 contributions list 紧跟 C2, 读者误读为 taxonomy 解释力。加上 76.6% unexplained variance, 将 22× 作为 headline contribution 不合理。需区分 clause-level vs type-level, 降级为 supporting evidence。\"\n  action_items:\n    - round: 11\n      action: \"Intro contribution(2) 改为 clause identity\"\n      assigned_to: agent\n      status: in_progress\n    - round: 12\n      action: \"(1) Contributions 区分 clause-level vs type-level variance; (2) §5.1 讨论 0.4% 对 taxonomy 实用价值含义; (3) 22× 从 headline contribution 降级为 supporting evidence; (4) 报告 76.6% residual\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-C1\"\n  summary: \"Authorization scope κ=0.385 + cross-judge asymmetry 威胁 C4 结论\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 12\n  mentions:\n    - round: 10\n      reviewers: [R1, R2]\n      note: \"R1 MUST-FIX. κ=0.385 < fair agreement 0.40, 52pp 中真实差异 vs noise 无法分离。\"\n    - round: 11\n      reviewers: [R1, R2]\n      note: \"W1 MUST-FIX. cross-judge κ vs human-LLM κ 混淆, Appendix P ρ=-0.03 rank reversal。\"\n    - round: 12\n      reviewers: [R1, R2]\n      note: \"MF-3. 共识: GPT-5.4 judges 3 models, GPT-4.1 judges 2 models. Auth scope 52pp 跨 judge 边界, κ=0.385 最低。Within-judge-group: GPT-5.4-judged auth scope range=34pp, GPT-4.1-judged=4pp — 暗示 judge effect。Figure 3 印象远强于 caveat。需标注 judge assignment, 报告 within-judge range, 提升 caveat。\"\n  action_items:\n    - round: 11\n      action: \"C4 降级 + PABAK + 52pp 定性化\"\n      assigned_to: agent\n      status: in_progress\n    - round: 12\n      action: \"(1) Figure 3 caption 标注 judge assignment; (2) 报告 within-judge-group auth scope ranges; (3) 提升 upper-bound caveat 到 Figure 3 caption + Discussion; (4) Discussion 中 differential nocuity 定位为 hypothesis\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# WARNING ISSUES\n# ============================================================\n\n- id: \"R10-C2\"\n  summary: \"C2 risk gradient claim margin-dependent — ±10pp 时 gradient 瓦解, bootstrap AU=0.47 不支持\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 12\n  mentions:\n    - round: 10\n      reviewers: [R1, R2]\n      note: \"MUST-FIX. Bootstrap AU p=0.47, Kendall's W=0.398(p=0.072)。\"\n    - round: 11\n      reviewers: [R1, R2]\n      note: \"W2 SHOULD-FIX. Round 11 改为 risk gradient 有进步。\"\n    - round: 12\n      reviewers: [R1, R2]\n      note: \"MF-2. 共识: gradient 在 ±15pp 成立(6/6)但 ±10pp 仅 3/6。Bootstrap AU=0.47 不 corroborate。排除 incompleteness 后 omnibus p=0.079。Margin-dependence 应入 claim 声明。\"\n  action_items:\n    - round: 11\n      action: \"全文 'two-tier'→'risk gradient'\"\n      assigned_to: agent\n      status: in_progress\n    - round: 12\n      action: \"(1) C2 claim 每次附加 margin 条件 'at ±15pp'; (2) Abstract/Conclusion 明确 margin-dependence; (3) 弱化 bootstrap corroboration 措辞; (4) 注明排除 incompleteness 后 omnibus p=0.079\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R12-W1\"\n  summary: \"Incompleteness information-addition confound 控制不充分 — token count proxy 过粗, 跨类型反证非 apples-to-apples\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [R1, R2]\n      note: \"MF-4. 共识: incompleteness 的 unambiguous variant 添加全新 policy content(+34.6 words)而非消歧。Token count OR=1.022/token, ~35 tokens 累积 ~2.15× odds multiplier, 非可忽略。Auth scope +36.1 words 的反证比较了语义不同的内容, 不是 apples-to-apples。\"\n  action_items:\n    - round: 12\n      action: \"(1) 一致标注 49.2pp 为 upper bound; (2) Abstract/Conclusion 用 coreferential 18.7pp 作 confound-free anchor; (3) 讨论 propositional content analysis 作为更好 proxy; (4) 承认跨类型 token delta 比较的局限\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-W1\"\n  summary: \"Taxonomy 理论基础: incompleteness/conditional_precedence 不满足 strict ambiguity 定义\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 12\n  mentions:\n    - round: 10\n      reviewers: [R2, R1]\n      note: \"SHOULD-FIX. §3 需正面讨论理论张力。\"\n    - round: 11\n      reviewers: [R2, R1]\n      note: \"W3. R11 已加 Dalpiaz 引用和 Scope of ambiguity 段落。基本完成。\"\n    - round: 12\n      reviewers: [R2, R1]\n      note: \"SF-1. R2 再次提出(N2 critical), R1 部分反驳——同意前置 scope 但反对改标题。共识: §3 讨论充分, 但 scope 限定来得太晚(page 3), 应在 §1 即前置 parenthetical。\"\n  action_items:\n    - round: 12\n      action: \"§1 taxonomy 介绍处加 parenthetical: 'including specification-level gaps that produce identical behavioral outcomes in LLM agents'\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-W4\"\n  summary: \"Disambiguation Neglect 新颖性被高估 — 已有文献的 agentic setting quantification 非新发现\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 12\n  mentions:\n    - round: 11\n      reviewers: [R2, R1]\n      note: \"W4. Liu et al. (2023) + Hu et al. (2025) 已建立核心现象。\"\n    - round: 12\n      reviewers: [R2, R1]\n      note: \"SF-3. 共识: contribution(3) 'revealing' 应改为 'quantifying in consequential agentic settings and identifying systematic nocuity'。保留 systematic nocuity 作为新颖发现。\"\n  action_items:\n    - round: 11\n      action: \"Intro contribution(3) 加 extending observations\"\n      assigned_to: agent\n      status: in_progress\n    - round: 12\n      action: \"Contribution(3) wording: 'revealing' → 'quantifying in consequential agentic settings and identifying systematic nocuity'\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-W7\"\n  summary: \"SESOI ±15pp 论证 margin-dependence — field-standard 缺失, perturbation bound ×2 非独立标准\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 12\n  mentions:\n    - round: 11\n      reviewers: [R1, R2]\n      note: \"W7. 循环论证风险, 有 7-margin sensitivity 补充。\"\n    - round: 12\n      reviewers: [R1, R2]\n      note: \"MF-2 子项. R1 标 critical, R2 agree-with-qualification(循环论证定性过度, 有 domain justification)。共识: margin-dependence 应入 claim, 且正文应讨论 field-standard SESOI 缺失。\"\n  action_items:\n    - round: 12\n      action: \"§4.6 强化 domain justification, 承认 field-standard SESOI 缺失对结论稳健性影响\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-W6\"\n  summary: \"Cross-judge 设计 + judge family bias (both OpenAI) 对跨模型比较的系统性威胁\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 12\n  mentions:\n    - round: 10\n      reviewers: [R1, R2]\n      note: \"SHOULD-FIX. C2 pooled rates 和 C4 受影响。\"\n    - round: 11\n      reviewers: [R1, R2]\n      note: \"W8. GPT-5.4/GPT-4.1 可能共享 type-specific correlated bias。\"\n    - round: 12\n      reviewers: [R1, R2]\n      note: \"SF-5. 共识: Claude 30.3% 最低 violation rate 可能反映真实 robustness 或 judge bias。主要威胁 C4(已标 Exploratory), C1/C2 部分隔离。需讨论 bias 可能方向, 明确推荐 cross-family judge evaluation。\"\n  action_items:\n    - round: 12\n      action: \"(1) 讨论 judge family bias 可能方向; (2) Future Work 明确推荐 cross-family judge evaluation\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-W3\"\n  summary: \"Differential Nocuity 框架增量贡献被过度表述 / C4 2.9% variance 获过高 Discussion 权重\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 12\n  mentions:\n    - round: 10\n      reviewers: [R2, R1]\n      note: \"SHOULD-FIX. 定位为已有概念在 LLM agent 领域的验证。\"\n    - round: 11\n      reviewers: [R2, R1]\n      note: \"W5. R11 修改已完成——discussion.tex 已写 B&K 扩展定位 + Willis (2008)。\"\n    - round: 12\n      reviewers: [R1, R2]\n      note: \"SF-6. 新维度: C4 interaction 仅 2.9% variance, 但 Discussion differential nocuity 框架将 auth scope 模型差异作核心论据。需定位为 hypothesis 而非 framework, 附 effect size + uncertainty caveat。\"\n  action_items:\n    - round: 12\n      action: \"Discussion 中 differential nocuity 定位为 hypothesis/preliminary observation; 引用 auth scope 差异时附 effect size + measurement uncertainty\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R12-W2\"\n  summary: \"Kendall's W 选择性报告 — 5-model p=0.072 不显著, 7-model 排除 coreferential 后 p=0.038 显著\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [R1, R2]\n      note: \"SF-7. §5.2 引用 'moderate' concordance 未注明不显著。排除 coreferential 有方法论理由但组合看起来像选择性报告。\"\n  action_items:\n    - round: 12\n      action: \"§5.2 报告 5-model p=0.072; 措辞改为 'trending toward concordance, driven by incompleteness ranking consistently highest'\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R12-W3\"\n  summary: \"单一 benchmark (τ²-bench) 外部效度 — Abstract/Conclusion 暗示过广 generalizability\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [R2, R1]\n      note: \"SF-8. 所有实验仅在 τ²-bench (retail + airline)。Abstract/Conclusion 用 'LLM-based agents' 无 domain 限定。R1 同意但认为严重程度略低(两个 domain + Limitations 已承认)。\"\n  action_items:\n    - round: 12\n      action: \"Abstract/Conclusion 添加 domain qualifier ('in customer service settings' 或 'in retail and airline domains')\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R12-W4\"\n  summary: \"Mitigation 实验方向矛盾 — §7 GPT-5.4 incompleteness +14pp vs Appendix B -2.6pp 未充分解释\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 12\n  mentions:\n    - round: 11\n      reviewers: [R1, R2]\n      note: \"R11-M10. §7 GPT-5.4 generic +1.3pp vs Appendix B 同模型 -14.0pp。\"\n    - round: 12\n      reviewers: [R2, R1]\n      note: \"SF-2. 共识: 同模型同类型, 换 prompt 从 +14pp 变 -2.6pp(incompleteness), 一句话解释不够。两个实验设计差异(matched-pair McNemar vs unpaired)未在引用点标注。\"\n  action_items:\n    - round: 12\n      action: \"(1) 报告两组 prompt 内容; (2) 讨论 prompt sensitivity 本身作为 finding; (3) 首次引用时标注两个实验设计差异\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-W5\"\n  summary: \"Per-type 人工验证样本量偏小(n=32-34/type) — Appendix G 仍做 type-level 推断\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 12\n  mentions:\n    - round: 10\n      reviewers: [R1, R2]\n      note: \"SHOULD-FIX. scopal CI [0.00, 1.00] 无信息。\"\n    - round: 11\n      reviewers: [R1, R2]\n      note: \"W9. method.tex 已写 'Per-type estimates lack power for type-level comparison'。标 resolved。\"\n    - round: 12\n      reviewers: [R1, R2]\n      note: \"SF-4. §4.4 承认 lack power, 但 Appendix G 仍报告 per-type κ 并得出 type-level 结论('Authorization scope has the lowest...')。CIs 极宽无信息量。\"\n  action_items:\n    - round: 12\n      action: \"Appendix G 明确声明 per-type 结果仅为 descriptive/suggestive, 不用于 type-level ranking\"\n      assigned_to: agent\n      status: open\n  resolution: \"§4.4 已承认 per-type lack power, 但 Appendix G 需同步调整\"\n  resolution_round: null\n\n# ============================================================\n# MINOR ISSUES\n# ============================================================\n\n- id: \"R12-M1\"\n  summary: \"4.6% vs ≤11% disambiguation awareness 数字在不同位置交替使用\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [R2, R1]\n      note: \"MI-1. 4.6% = overall average, ≤11% = per-model max (Claude). §1 和 §6.2 交替出现。建议统一。\"\n  action_items:\n    - round: 12\n      action: \"统一使用一个数字, 首次出现时注明另一个\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-M11\"\n  summary: \"Mitigation incompleteness worsening 因果解释过度 (p=0.118)\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 12\n  mentions:\n    - round: 11\n      reviewers: [R2, R1]\n      note: \"W11. 'triggers confabulation' 是确定性语言解释非显著趋势。\"\n    - round: 12\n      reviewers: []\n      note: \"本轮未单独提及, 但 R12-W4 (mitigation 方向矛盾) 涵盖了此问题的更广泛维度。\"\n  action_items:\n    - round: 11\n      action: \"'triggers' → 'may trigger' + 标注 'non-significant trend, p=0.118'\"\n      assigned_to: agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-M2\"\n  summary: \"引用问题: ferrari 作者不一致 + orphan entries\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 8\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [R1, R2]\n      note: \"ferrari_defects_2018 第一作者; tamkin/yin orphan entries。\"\n    - round: 12\n      reviewers: []\n      note: \"本轮未提及, 可能已修复, 待确认。R2-M4 提到 arXiv preprint 引用需核查但未给出具体条目。\"\n  action_items:\n    - round: 10\n      action: \"核实 bib entries\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-M6\"\n  summary: \"Pages 4-5 连续纯文本无 display item\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 9\n  last_seen_round: 12\n  mentions:\n    - round: 11\n      reviewers: []\n      note: \"Visual check: Pages 4-5 连续两页纯文本。建议 §4 添加模型汇总表。\"\n    - round: 12\n      reviewers: []\n      note: \"Visual check: Method §4 连续两页纯文本无 display item, 审稿人容易失去视觉锚点。建议添加 matched-pair design 简图或伪代码。\"\n  action_items:\n    - round: 12\n      action: \"低优先级——页面预算紧张, 但可考虑 matched-pair design 简图\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R12-M2\"\n  summary: \"Page 8 压缩 5 个 section 在单页, 给出匆忙收尾印象\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: []\n      note: \"Visual check: §6.2-§8+Limitations 压缩在单页, 阅读节奏急促。\"\n  action_items:\n    - round: 12\n      action: \"低优先级——8页限制下空间有限, 可考虑压缩 C3 释放空间\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# PREVIOUSLY RESOLVED\n# ============================================================\n\n- id: \"R11-M13\"\n  summary: \"Coreferential 排除在 mitigation/replication 中已在 Limitations 提及\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 12\n  mentions:\n    - round: 11\n      reviewers: [R2, R1]\n      note: \"W13. 6类 taxonomy 中 1 类在两个实验中完全缺席。\"\n    - round: 12\n      reviewers: []\n      note: \"Limitations §已写 'Coreferential ambiguity was excluded from mitigation and replication experiments due to benchmark-specific structural constraints'。本轮未被任何 Reviewer 提及。\"\n  resolution: \"Limitations 已明确声明 coreferential exclusion 及原因\"\n  resolution_round: 12\n\n- id: \"R10-W4-resolved\"\n  summary: \"Disambiguation Deficit → Neglect 术语统一\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 11\n  resolution: \"Round 11 全文统一为 Disambiguation Neglect，8 处全部更新\"\n  resolution_round: 11\n\n- id: \"R8-W1-resolved\"\n  summary: \"缺少 API 超参数报告\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 10\n  resolution: \"§4.3 添加完整 API 超参数\"\n  resolution_round: 9\n\n- id: \"R8-W4-resolved\"\n  summary: \"无代码/数据可用性声明\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 10\n  resolution: \"添加 Data and Code Availability section\"\n  resolution_round: 9\n\n- id: \"R9-W7-resolved\"\n  summary: \"多重比较校正 three test families 未明确定义\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  resolution: \"Appendix L 新增 Multiple Comparison Correction 小节\"\n  resolution_round: 10\n\n- id: \"R9-W8-resolved\"\n  summary: \"与 DRIP-R 的 taxonomy type-level 映射缺失\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  resolution: \"Appendix L 有 DRIP-R mapping\"\n  resolution_round: 10\n\n- id: \"R9-M3-resolved\"\n  summary: \"Introduction 'seven models' 措辞应区分 main study (5) vs replication (2)\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  resolution: \"措辞已修正\"\n  resolution_round: 10\n\n- id: \"R9-M7-resolved\"\n  summary: \"§5.4 F(20) 缺少 denominator df\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  resolution: \"F(20) → F(20, 2976)\"\n  resolution_round: 10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "policy_ambiguity_safety",
    "issues_yaml": "## Review Issues Tracker — policy_ambiguity_safety\n## Paper: \"Not All Policy Ambiguity Is Equal: Type-Specific Safety Risks for LLM Agents\"\n## Venue: EMNLP 2026 via ARR May cycle\n## Latest Round: 12 (Score: 3.5 Borderline Conference)\n## Upgrade path: fix 4 MF claim calibrations + 3 SF framing adjustments → 4.0\n\n# ============================================================\n# CRITICAL ISSUES\n# ============================================================\n\n- id: \"R11-C1\"\n  summary: \"22× variance claim 误导性 — taxonomy 仅解释 0.4% between-type variance, 22× 是 clause vs model\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 12\n  mentions:\n    - round: 11\n      reviewers: [R2, R1]\n      note: \"W6. clause_within_type=22.0% vs ambiguity_type=0.4%. Introduction contribution (2) '22× type identity' 是 clause identity 不是 type identity。\"\n    - round: 12\n      reviewers: [R2, R1]\n      note: \"MF-1. 两位 Reviewer 共识: 22× 放在 contributions list 紧跟 C2, 读者误读为 taxonomy 解释力。加上 76.6% unexplained variance, 将 22× 作为 headline contribution 不合理。需区分 clause-level vs type-level, 降级为 supporting evidence。\"\n  action_items:\n    - round: 11\n      action: \"Intro contribution(2) 改为 clause identity\"\n      assigned_to: agent\n      status: in_progress\n    - round: 12\n      action: \"(1) Contributions 区分 clause-level vs type-level variance; (2) §5.1 讨论 0.4% 对 taxonomy 实用价值含义; (3) 22× 从 headline contribution 降级为 supporting evidence; (4) 报告 76.6% residual\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-C1\"\n  summary: \"Authorization scope κ=0.385 + cross-judge asymmetry 威胁 C4 结论\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 12\n  mentions:\n    - round: 10\n      reviewers: [R1, R2]\n      note: \"R1 MUST-FIX. κ=0.385 < fair agreement 0.40, 52pp 中真实差异 vs noise 无法分离。\"\n    - round: 11\n      reviewers: [R1, R2]\n      note: \"W1 MUST-FIX. cross-judge κ vs human-LLM κ 混淆, Appendix P ρ=-0.03 rank reversal。\"\n    - round: 12\n      reviewers: [R1, R2]\n      note: \"MF-3. 共识: GPT-5.4 judges 3 models, GPT-4.1 judges 2 models. Auth scope 52pp 跨 judge 边界, κ=0.385 最低。Within-judge-group: GPT-5.4-judged auth scope range=34pp, GPT-4.1-judged=4pp — 暗示 judge effect。Figure 3 印象远强于 caveat。需标注 judge assignment, 报告 within-judge range, 提升 caveat。\"\n  action_items:\n    - round: 11\n      action: \"C4 降级 + PABAK + 52pp 定性化\"\n      assigned_to: agent\n      status: in_progress\n    - round: 12\n      action: \"(1) Figure 3 caption 标注 judge assignment; (2) 报告 within-judge-group auth scope ranges; (3) 提升 upper-bound caveat 到 Figure 3 caption + Discussion; (4) Discussion 中 differential nocuity 定位为 hypothesis\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# WARNING ISSUES\n# ============================================================\n\n- id: \"R10-C2\"\n  summary: \"C2 risk gradient claim margin-dependent — ±10pp 时 gradient 瓦解, bootstrap AU=0.47 不支持\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 12\n  mentions:\n    - round: 10\n      reviewers: [R1, R2]\n      note: \"MUST-FIX. Bootstrap AU p=0.47, Kendall's W=0.398(p=0.072)。\"\n    - round: 11\n      reviewers: [R1, R2]\n      note: \"W2 SHOULD-FIX. Round 11 改为 risk gradient 有进步。\"\n    - round: 12\n      reviewers: [R1, R2]\n      note: \"MF-2. 共识: gradient 在 ±15pp 成立(6/6)但 ±10pp 仅 3/6。Bootstrap AU=0.47 不 corroborate。排除 incompleteness 后 omnibus p=0.079。Margin-dependence 应入 claim 声明。\"\n  action_items:\n    - round: 11\n      action: \"全文 'two-tier'→'risk gradient'\"\n      assigned_to: agent\n      status: in_progress\n    - round: 12\n      action: \"(1) C2 claim 每次附加 margin 条件 'at ±15pp'; (2) Abstract/Conclusion 明确 margin-dependence; (3) 弱化 bootstrap corroboration 措辞; (4) 注明排除 incompleteness 后 omnibus p=0.079\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R12-W1\"\n  summary: \"Incompleteness information-addition confound 控制不充分 — token count proxy 过粗, 跨类型反证非 apples-to-apples\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [R1, R2]\n      note: \"MF-4. 共识: incompleteness 的 unambiguous variant 添加全新 policy content(+34.6 words)而非消歧。Token count OR=1.022/token, ~35 tokens 累积 ~2.15× odds multiplier, 非可忽略。Auth scope +36.1 words 的反证比较了语义不同的内容, 不是 apples-to-apples。\"\n  action_items:\n    - round: 12\n      action: \"(1) 一致标注 49.2pp 为 upper bound; (2) Abstract/Conclusion 用 coreferential 18.7pp 作 confound-free anchor; (3) 讨论 propositional content analysis 作为更好 proxy; (4) 承认跨类型 token delta 比较的局限\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-W1\"\n  summary: \"Taxonomy 理论基础: incompleteness/conditional_precedence 不满足 strict ambiguity 定义\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 12\n  mentions:\n    - round: 10\n      reviewers: [R2, R1]\n      note: \"SHOULD-FIX. §3 需正面讨论理论张力。\"\n    - round: 11\n      reviewers: [R2, R1]\n      note: \"W3. R11 已加 Dalpiaz 引用和 Scope of ambiguity 段落。基本完成。\"\n    - round: 12\n      reviewers: [R2, R1]\n      note: \"SF-1. R2 再次提出(N2 critical), R1 部分反驳——同意前置 scope 但反对改标题。共识: §3 讨论充分, 但 scope 限定来得太晚(page 3), 应在 §1 即前置 parenthetical。\"\n  action_items:\n    - round: 12\n      action: \"§1 taxonomy 介绍处加 parenthetical: 'including specification-level gaps that produce identical behavioral outcomes in LLM agents'\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-W4\"\n  summary: \"Disambiguation Neglect 新颖性被高估 — 已有文献的 agentic setting quantification 非新发现\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 12\n  mentions:\n    - round: 11\n      reviewers: [R2, R1]\n      note: \"W4. Liu et al. (2023) + Hu et al. (2025) 已建立核心现象。\"\n    - round: 12\n      reviewers: [R2, R1]\n      note: \"SF-3. 共识: contribution(3) 'revealing' 应改为 'quantifying in consequential agentic settings and identifying systematic nocuity'。保留 systematic nocuity 作为新颖发现。\"\n  action_items:\n    - round: 11\n      action: \"Intro contribution(3) 加 extending observations\"\n      assigned_to: agent\n      status: in_progress\n    - round: 12\n      action: \"Contribution(3) wording: 'revealing' → 'quantifying in consequential agentic settings and identifying systematic nocuity'\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-W7\"\n  summary: \"SESOI ±15pp 论证 margin-dependence — field-standard 缺失, perturbation bound ×2 非独立标准\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 12\n  mentions:\n    - round: 11\n      reviewers: [R1, R2]\n      note: \"W7. 循环论证风险, 有 7-margin sensitivity 补充。\"\n    - round: 12\n      reviewers: [R1, R2]\n      note: \"MF-2 子项. R1 标 critical, R2 agree-with-qualification(循环论证定性过度, 有 domain justification)。共识: margin-dependence 应入 claim, 且正文应讨论 field-standard SESOI 缺失。\"\n  action_items:\n    - round: 12\n      action: \"§4.6 强化 domain justification, 承认 field-standard SESOI 缺失对结论稳健性影响\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-W6\"\n  summary: \"Cross-judge 设计 + judge family bias (both OpenAI) 对跨模型比较的系统性威胁\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 12\n  mentions:\n    - round: 10\n      reviewers: [R1, R2]\n      note: \"SHOULD-FIX. C2 pooled rates 和 C4 受影响。\"\n    - round: 11\n      reviewers: [R1, R2]\n      note: \"W8. GPT-5.4/GPT-4.1 可能共享 type-specific correlated bias。\"\n    - round: 12\n      reviewers: [R1, R2]\n      note: \"SF-5. 共识: Claude 30.3% 最低 violation rate 可能反映真实 robustness 或 judge bias。主要威胁 C4(已标 Exploratory), C1/C2 部分隔离。需讨论 bias 可能方向, 明确推荐 cross-family judge evaluation。\"\n  action_items:\n    - round: 12\n      action: \"(1) 讨论 judge family bias 可能方向; (2) Future Work 明确推荐 cross-family judge evaluation\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-W3\"\n  summary: \"Differential Nocuity 框架增量贡献被过度表述 / C4 2.9% variance 获过高 Discussion 权重\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 12\n  mentions:\n    - round: 10\n      reviewers: [R2, R1]\n      note: \"SHOULD-FIX. 定位为已有概念在 LLM agent 领域的验证。\"\n    - round: 11\n      reviewers: [R2, R1]\n      note: \"W5. R11 修改已完成——discussion.tex 已写 B&K 扩展定位 + Willis (2008)。\"\n    - round: 12\n      reviewers: [R1, R2]\n      note: \"SF-6. 新维度: C4 interaction 仅 2.9% variance, 但 Discussion differential nocuity 框架将 auth scope 模型差异作核心论据。需定位为 hypothesis 而非 framework, 附 effect size + uncertainty caveat。\"\n  action_items:\n    - round: 12\n      action: \"Discussion 中 differential nocuity 定位为 hypothesis/preliminary observation; 引用 auth scope 差异时附 effect size + measurement uncertainty\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R12-W2\"\n  summary: \"Kendall's W 选择性报告 — 5-model p=0.072 不显著, 7-model 排除 coreferential 后 p=0.038 显著\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [R1, R2]\n      note: \"SF-7. §5.2 引用 'moderate' concordance 未注明不显著。排除 coreferential 有方法论理由但组合看起来像选择性报告。\"\n  action_items:\n    - round: 12\n      action: \"§5.2 报告 5-model p=0.072; 措辞改为 'trending toward concordance, driven by incompleteness ranking consistently highest'\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R12-W3\"\n  summary: \"单一 benchmark (τ²-bench) 外部效度 — Abstract/Conclusion 暗示过广 generalizability\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [R2, R1]\n      note: \"SF-8. 所有实验仅在 τ²-bench (retail + airline)。Abstract/Conclusion 用 'LLM-based agents' 无 domain 限定。R1 同意但认为严重程度略低(两个 domain + Limitations 已承认)。\"\n  action_items:\n    - round: 12\n      action: \"Abstract/Conclusion 添加 domain qualifier ('in customer service settings' 或 'in retail and airline domains')\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R12-W4\"\n  summary: \"Mitigation 实验方向矛盾 — §7 GPT-5.4 incompleteness +14pp vs Appendix B -2.6pp 未充分解释\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 12\n  mentions:\n    - round: 11\n      reviewers: [R1, R2]\n      note: \"R11-M10. §7 GPT-5.4 generic +1.3pp vs Appendix B 同模型 -14.0pp。\"\n    - round: 12\n      reviewers: [R2, R1]\n      note: \"SF-2. 共识: 同模型同类型, 换 prompt 从 +14pp 变 -2.6pp(incompleteness), 一句话解释不够。两个实验设计差异(matched-pair McNemar vs unpaired)未在引用点标注。\"\n  action_items:\n    - round: 12\n      action: \"(1) 报告两组 prompt 内容; (2) 讨论 prompt sensitivity 本身作为 finding; (3) 首次引用时标注两个实验设计差异\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-W5\"\n  summary: \"Per-type 人工验证样本量偏小(n=32-34/type) — Appendix G 仍做 type-level 推断\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 12\n  mentions:\n    - round: 10\n      reviewers: [R1, R2]\n      note: \"SHOULD-FIX. scopal CI [0.00, 1.00] 无信息。\"\n    - round: 11\n      reviewers: [R1, R2]\n      note: \"W9. method.tex 已写 'Per-type estimates lack power for type-level comparison'。标 resolved。\"\n    - round: 12\n      reviewers: [R1, R2]\n      note: \"SF-4. §4.4 承认 lack power, 但 Appendix G 仍报告 per-type κ 并得出 type-level 结论('Authorization scope has the lowest...')。CIs 极宽无信息量。\"\n  action_items:\n    - round: 12\n      action: \"Appendix G 明确声明 per-type 结果仅为 descriptive/suggestive, 不用于 type-level ranking\"\n      assigned_to: agent\n      status: open\n  resolution: \"§4.4 已承认 per-type lack power, 但 Appendix G 需同步调整\"\n  resolution_round: null\n\n# ============================================================\n# MINOR ISSUES\n# ============================================================\n\n- id: \"R12-M1\"\n  summary: \"4.6% vs ≤11% disambiguation awareness 数字在不同位置交替使用\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [R2, R1]\n      note: \"MI-1. 4.6% = overall average, ≤11% = per-model max (Claude). §1 和 §6.2 交替出现。建议统一。\"\n  action_items:\n    - round: 12\n      action: \"统一使用一个数字, 首次出现时注明另一个\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-M11\"\n  summary: \"Mitigation incompleteness worsening 因果解释过度 (p=0.118)\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 12\n  mentions:\n    - round: 11\n      reviewers: [R2, R1]\n      note: \"W11. 'triggers confabulation' 是确定性语言解释非显著趋势。\"\n    - round: 12\n      reviewers: []\n      note: \"本轮未单独提及, 但 R12-W4 (mitigation 方向矛盾) 涵盖了此问题的更广泛维度。\"\n  action_items:\n    - round: 11\n      action: \"'triggers' → 'may trigger' + 标注 'non-significant trend, p=0.118'\"\n      assigned_to: agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-M2\"\n  summary: \"引用问题: ferrari 作者不一致 + orphan entries\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 8\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [R1, R2]\n      note: \"ferrari_defects_2018 第一作者; tamkin/yin orphan entries。\"\n    - round: 12\n      reviewers: []\n      note: \"本轮未提及, 可能已修复, 待确认。R2-M4 提到 arXiv preprint 引用需核查但未给出具体条目。\"\n  action_items:\n    - round: 10\n      action: \"核实 bib entries\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-M6\"\n  summary: \"Pages 4-5 连续纯文本无 display item\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 9\n  last_seen_round: 12\n  mentions:\n    - round: 11\n      reviewers: []\n      note: \"Visual check: Pages 4-5 连续两页纯文本。建议 §4 添加模型汇总表。\"\n    - round: 12\n      reviewers: []\n      note: \"Visual check: Method §4 连续两页纯文本无 display item, 审稿人容易失去视觉锚点。建议添加 matched-pair design 简图或伪代码。\"\n  action_items:\n    - round: 12\n      action: \"低优先级——页面预算紧张, 但可考虑 matched-pair design 简图\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R12-M2\"\n  summary: \"Page 8 压缩 5 个 section 在单页, 给出匆忙收尾印象\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: []\n      note: \"Visual check: §6.2-§8+Limitations 压缩在单页, 阅读节奏急促。\"\n  action_items:\n    - round: 12\n      action: \"低优先级——8页限制下空间有限, 可考虑压缩 C3 释放空间\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# PREVIOUSLY RESOLVED\n# ============================================================\n\n- id: \"R11-M13\"\n  summary: \"Coreferential 排除在 mitigation/replication 中已在 Limitations 提及\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 12\n  mentions:\n    - round: 11\n      reviewers: [R2, R1]\n      note: \"W13. 6类 taxonomy 中 1 类在两个实验中完全缺席。\"\n    - round: 12\n      reviewers: []\n      note: \"Limitations §已写 'Coreferential ambiguity was excluded from mitigation and replication experiments due to benchmark-specific structural constraints'。本轮未被任何 Reviewer 提及。\"\n  resolution: \"Limitations 已明确声明 coreferential exclusion 及原因\"\n  resolution_round: 12\n\n- id: \"R10-W4-resolved\"\n  summary: \"Disambiguation Deficit → Neglect 术语统一\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 11\n  resolution: \"Round 11 全文统一为 Disambiguation Neglect，8 处全部更新\"\n  resolution_round: 11\n\n- id: \"R8-W1-resolved\"\n  summary: \"缺少 API 超参数报告\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 10\n  resolution: \"§4.3 添加完整 API 超参数\"\n  resolution_round: 9\n\n- id: \"R8-W4-resolved\"\n  summary: \"无代码/数据可用性声明\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 10\n  resolution: \"添加 Data and Code Availability section\"\n  resolution_round: 9\n\n- id: \"R9-W7-resolved\"\n  summary: \"多重比较校正 three test families 未明确定义\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  resolution: \"Appendix L 新增 Multiple Comparison Correction 小节\"\n  resolution_round: 10\n\n- id: \"R9-W8-resolved\"\n  summary: \"与 DRIP-R 的 taxonomy type-level 映射缺失\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  resolution: \"Appendix L 有 DRIP-R mapping\"\n  resolution_round: 10\n\n- id: \"R9-M3-resolved\"\n  summary: \"Introduction 'seven models' 措辞应区分 main study (5) vs replication (2)\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  resolution: \"措辞已修正\"\n  resolution_round: 10\n\n- id: \"R9-M7-resolved\"\n  summary: \"§5.4 F(20) 缺少 denominator df\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  resolution: \"F(20) → F(20, 2976)\"\n  resolution_round: 10"
  }
}
```

</details>

---


### Tool result

_source line 1071 · 2026-05-22T10:07:32.405583+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_issues.yaml\", \"bytes\": 17240}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1072 · 2026-05-22T10:09:34.269773+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# Consolidated Review Report — Round 12\n\n**Paper**: \"Not All Policy Ambiguity Is Equal: Type-Specific Safety Risks for LLM Agents\"\n**Venue**: EMNLP 2026 via ARR May cycle (deadline: 2026-05-25)\n**Reviewers**: R1 (方法严谨性, 3.5/5) + R2 (新颖性/完整性, 3.5/5)\n**Cross-response**: 完成，19/22 条 AGREE，2 条 REBUT（taxonomy 术语严重程度 + perturbation control 分工设计）\n\n---\n\n## Summary\n\nThis paper presents a matched-pair causal study on τ²-bench examining how six types of policy ambiguity affect safety violations in LLM agents. Using 300 clause pairs evaluated across five models (2,997 episodes), the study finds: (1) ambiguous clauses increase violation rates by 34.0 pp (OR=15.1); (2) incompleteness consistently ranks highest (46–62% across seven models) with a risk gradient rather than sharp tiers; (3) agents exhibit Disambiguation Neglect (≤11% awareness) and systematic nocuity (41.3% majority-convergent violations). The methodology is well-designed with perturbation controls, cross-judge evaluation, and comprehensive statistical analysis. Two additional model families replicate core findings.\n\n---\n\n## Strengths\n\n**S1** [Consensus] First matched-pair causal study of ambiguity type → agent safety violation, filling an important empirical gap. Perturbation control + matched-pair design provides stronger causal inference than observational studies.\n\n**S2** [Consensus] Statistical methodology quality exceeds the field norm — TOST equivalence testing + bootstrap cluster + Holm-Bonferroni correction + sensitivity analysis across seven margins. Claim calibration (C3 inconclusive, C4 exploratory) demonstrates excellent intellectual honesty.\n\n**S3** [Consensus] Seven models across six providers (5 primary + 2 replication) is among the broadest model coverage in agent safety research. ICC=0.919 demonstrates reproducibility (within OpenAI family).\n\n**S4** [Consensus] Disambiguation Neglect (4.6% overall, ≤11% per-model) and systematic nocuity (41.3% majority-convergent, 13% universal) are valuable empirical contributions with direct deployment implications.\n\n**S5** [Consensus] Type → failure mode mapping (§6.1: structural misparse, information gap-filling, boundary violation) is practically valuable, with majority-consistency (≥3/5 models) for each type's dominant failure mode.\n\n**S6** [Consensus] Writing is clear and well-structured within 8-page constraints. Limitations section is candid and specific.\n\n---\n\n## Weaknesses\n\n### MUST-FIX (4 issues — all consensus)\n\n**[MF-1]** \"22× more variance\" claim is misleading (R2-N1, R1-AGREE)\n- §5.1 decomposition: clause identity 22.4% = between-type 0.4% + within-type 22.0%. The taxonomy itself explains only 0.4% of variance — 55× less than within-type clause wording. Placed in the contribution list after C2, readers naturally interpret \"22×\" as type-level explanatory power. Combined with 76.6% unexplained variance (evaluation pipeline noise), this constitutes overclaiming.\n- **Required fix**: (1) Distinguish clause-level vs type-level variance in contributions; (2) Discuss 0.4% implications for taxonomy utility in §5.1; (3) Demote \"22×\" from headline contribution to supporting evidence; (4) Report 76.6% residual.\n\n**[MF-2]** C2 \"risk gradient\" claim is margin-dependent (R1-N1, R2-AGREE-w-qualification)\n- The gradient structure holds at ±15pp (6/6 mid-tier pairs equivalent) but collapses at ±10pp (3/6). No field-standard SESOI exists. Bootstrap cluster analysis (AU p=0.47) does not corroborate — the singleton partition reproduces in only 34.3% of bootstrap samples. Excluding incompleteness, omnibus p=0.079 (pairwise gradient partially survives: auth scope/lexical > coreferential).\n- **Required fix**: (1) Attach margin condition to every C2 claim statement (\"at the ±15pp margin\"); (2) Abstract/Conclusion must acknowledge margin-dependence; (3) Weaken bootstrap \"corroborates\" language; (4) Note p=0.079 excluding incompleteness.\n\n**[MF-3]** Cross-judge asymmetry threatens C4 conclusions (R1-N2, R2-AGREE)\n- GPT-5.4 judges Claude/GPT-4.1/Qwen3; GPT-4.1 judges GPT-5.4/DeepSeek. Authorization scope 52pp range (Claude 12% → GPT-5.4 64%) crosses the judge boundary, and auth scope has the lowest inter-judge κ (0.385). Within-judge-group auth scope: GPT-5.4-judged range = 34pp (Claude 12%, GPT-4.1 46%, Qwen3 26%), GPT-4.1-judged range = 4pp (GPT-5.4 64%, DeepSeek 60%). Appendix P type ranking ρ=−0.03 across judge groups. Figure 3 and \"most model-differentiating type\" framing give readers a much stronger impression than caveats warrant.\n- **Required fix**: (1) Figure 3 caption annotate judge assignments; (2) Report within-judge-group auth scope ranges; (3) Elevate caveat to Figure 3 caption and Discussion; (4) Position differential nocuity as hypothesis, not established framework.\n\n**[MF-4]** Incompleteness information-addition confound insufficiently controlled (R1-N3, R2-W3, mutual AGREE)\n- Incompleteness's unambiguous variant adds entirely new policy content (+34.6 words) rather than merely resolving ambiguity. Token count proxy is admittedly coarse. Cross-type counter-evidence (auth scope +36.1 > incompleteness +34.6) compares semantically different content types — not apples-to-apples. Token delta OR=1.022/token cumulates to ~2.15× odds multiplier over ~35 tokens.\n- **Required fix**: (1) Consistently label 49.2pp as \"upper bound including potential information-addition inflation\"; (2) Use coreferential 18.7pp as confound-free anchor in Abstract/Conclusion; (3) Discuss propositional content analysis as better but unimplemented proxy; (4) Acknowledge cross-type token delta comparison limitations.\n\n### SHOULD-FIX (8 issues)\n\n**[SF-1]** Front-load taxonomy scope limitation (R2-N2 critical, R1-REBUT but agrees on partial fix)\n- Incompleteness = information absence, conditional precedence = normative conflict. §3 \"Scope of ambiguity\" addresses this well but comes too late (page 3). R1 argues against changing terminology, citing RE literature connection.\n- **Fix**: Add parenthetical in §1 (\"including specification-level gaps that, while not ambiguity in the strict linguistic sense, produce identical behavioral outcomes in LLM agents\"). Consider \"including specification-level gaps\" in Abstract.\n\n**[SF-2]** Mitigation experiment direction contradiction (R2-W1, R1-AGREE)\n- §7 GPT-5.4 type-specific incompleteness: +14pp (p=0.118). Appendix B GPT-5.4 incompleteness: −2.6pp. Same model, same type, different prompt and design.\n- **Fix**: Report both prompt formulations; discuss prompt sensitivity as a finding; label design differences at first mention.\n\n**[SF-3]** Disambiguation Neglect novelty positioning (R2-W2, R1-AGREE)\n- Liu et al. (2023) + Hu et al. (2025) established core phenomenon. Contribution is quantifying in agentic settings.\n- **Fix**: Contribution (3) \"revealing\" → \"quantifying in consequential agentic settings and identifying systematic nocuity.\"\n\n**[SF-4]** Per-type human validation CIs uninformative (R1-W2, R2-AGREE)\n- n=32-34 per type. Scopal κ CI=[0.00, 1.00]. Appendix G draws type-level conclusions despite §4.4's \"lack power\" caveat.\n- **Fix**: Appendix G must state per-type results are descriptive/suggestive only.\n\n**[SF-5]** Judge family bias (R1-W3, R2-AGREE)\n- Both judges from OpenAI. Claude's 30.3% could reflect genuine robustness or systematic bias.\n- **Fix**: Discuss possible bias direction; recommend cross-family judge evaluation in Future Work.\n\n**[SF-6]** C4 2.9% variance vs Discussion weight (R1-W4, R2-AGREE)\n- Interaction explains 2.9% variance; Discussion gives it disproportionate theoretical weight.\n- **Fix**: Position differential nocuity as hypothesis; attach effect size + uncertainty caveats.\n\n**[SF-7]** Kendall's W selective reporting (R1-W6, R2-AGREE-w-qualification)\n- 5-model W=0.398 (p=0.072) non-significant; 7-model excluding coreferential p=0.038 significant.\n- **Fix**: §5.2 report 5-model p=0.072; characterize as \"trending toward concordance.\"\n\n**[SF-8]** Single benchmark external validity (R2-W4, R1-AGREE with lower severity)\n- All experiments on τ²-bench (retail + airline). Abstract/Conclusion overgeneralize.\n- **Fix**: Add domain qualifiers in Abstract and Conclusion.\n\n### MINOR (7 issues)\n\n- [MI-1] 4.6% vs ≤11% awareness numbers used interchangeably — standardize.\n- [MI-2] C3 §5.3 can compress from ~6 lines to 3-4.\n- [MI-3] Table 2 caption too long — move Tier definitions to footnote.\n- [MI-4] Bootstrap ranking preservation (99.5%) must note within GPT-5.4 judge subset only.\n- [MI-5] ICC=0.919 within OpenAI family only — note cross-provider untested.\n- [MI-6] Pages 4-5 consecutive text-only (Visual check warning).\n- [MI-7] Page 8 compresses 5 sections — rushed ending impression (Visual check warning).\n\n---\n\n## Reviewer Consensus\n\nAll critical items reached [AGREE]:\n1. \"22× variance\" overclaiming — taxonomy explains 0.4% between-type variance [MF-1]\n2. C2 gradient collapses at ±10pp — margin-dependence must enter claim [MF-2]\n3. Auth scope 52pp crosses judge boundary with lowest κ — C4 needs stronger caveats [MF-3]\n4. Incompleteness confound token count proxy insufficient [MF-4]\n5. Mitigation §7 vs Appendix B contradiction needs analysis [SF-2]\n6. Disambiguation Neglect is quantification of known phenomenon [SF-3]\n7. **Bottleneck is claim calibration, not methodology** — both note fixing claims → 4.0 achievable\n\n## Reviewer Divergence\n\n1. **Taxonomy terminology** (R2-N2 vs R1-REBUT): R2 proposes \"policy underspecification\"; R1 argues this weakens RE literature connection. Both agree scope should be front-loaded in §1. **Director assessment**: R1's position is stronger — the paper's theoretical contribution depends on extending Berry & Kamsties (2004). Front-loading scope limitation in §1 is the proportionate fix.\n\n2. **Perturbation control applicability** (R1-W5 vs R2-REBUT): R1 argues structural mismatch for specification-layer types. R2 correctly notes §4.5's explicit two-pronged design (perturbation control for surface, logistic regression for information). **Director assessment**: R2's point stands, but the logistic regression's coarse proxy (MF-4) means the compound control for specification-layer types remains weaker. Already covered by MF-4.\n\n---\n\n## Questions for Authors\n\n1. What are the within-judge-group auth scope violation rates? If both groups show ranges far smaller than 52pp, this confirms judge effect.\n2. Is propositional content analysis (vs token count) feasible as a follow-up for the incompleteness confound?\n3. Given 0.4% between-type variance, should the taxonomy's primary claimed value shift from variance explanation to failure mode prediction (§6.1)?\n4. Excluding incompleteness, omnibus p=0.079 — should C2 be reframed around the partial pairwise survival?\n5. Any qualitative comparison with DRIP-R's naturally occurring policy ambiguity instances for ecological validity?\n6. What are C3's direction and effect size after controlling for token delta?\n\n---\n\n## Missing References\n\nR2 suggests \"The Causal Impact of Tool Affordance on Safety Alignment\" (arXiv:2603.20320). Existence not verified; if real, marginally relevant to §2 Agent Safety but not critical.\n\n---\n\n## External Review\n\n**Status**: Not requested.\n\n---\n\n## Visual Layout Check (非评分项)\n\n**Status**: Done (2026-05-22 09:54:26 UTC). 0 critical, 2 warning, 6 info.\n\n| Severity | Location | Finding |\n|----------|----------|---------|\n| ⚠️ Warning | Pages 4-5 | Method §4 连续两页纯文本无 display item，审稿人容易失去视觉锚点 |\n| ⚠️ Warning | Page 8 | §6.2–§8+Limitations 压缩 5 个 section 在单页，匆忙收尾印象 |\n| ℹ️ Info | Page 6 | Figure 2 bar 标签字号偏小（约正文 60-65%） |\n| ℹ️ Info | Page 7 | Figure 3 heatmap 数字字号偏小 |\n| ℹ️ Info | Page 2 | Figure 1 三面板视觉风格略不统一 |\n| ℹ️ Info | Page 6 | Table 2 格式规范 |\n| ℹ️ Info | Page 3 | Table 1 格式整洁 |\n| ℹ️ Info | Page 15 | Appendix 末页大面积空白 |\n\n---\n\n## Overall Assessment\n\n**Score: 3.5 / 5 — Borderline Conference**\n**Confidence: 4 / 5**\n**ARR scale: 3.5 = Borderline Conference**\n\n**Rationale**: The paper addresses an important question — whether ambiguity type in policy specifications causally determines safety violation severity — with a matched-pair methodology exceeding the field's empirical standard. C1 (+34.0pp, OR=15.1) is robust across seven models. The error analysis (Disambiguation Neglect, systematic nocuity) provides actionable deployment insights.\n\nHowever, the paper's secondary claims require calibration:\n- C2's \"risk gradient\" is margin-dependent (±15pp only), with bootstrap non-supportive and incompleteness potentially confound-inflated\n- \"22×\" contribution headline misrepresents the variance decomposition (clause wording, not type membership)\n- C4's auth scope interaction is confounded by cross-judge asymmetry on the lowest-agreement type\n\n**These are claim calibration problems, not methodological design flaws.** The underlying data and statistical framework are sound. Both reviewers independently assess that fixing the four must-fix items (claim recalibration, not new experiments) would bring the paper to 4.0 (Conference level).\n\n**Upgrade path**: Fix MF-1 through MF-4 (claim calibration) + SF-1 through SF-3 (framing adjustments) → 4.0.\n\n---\n\n## Detailed Comments\n\n### Abstract\n- \"22× more variance\" → reframe as clause-level (not type-level) finding\n- \"risk gradient rather than sharp tiers\" → add margin condition or soften\n- Add domain qualifier or \"specification-level gaps\" parenthetical\n- Use coreferential 18.7pp as confound-free anchor alongside incompleteness upper bound\n\n### §1 Introduction\n- Contribution (2): separate clause identity from type gradient; demote \"22×\"\n- Contribution (3): \"revealing\" → \"quantifying in consequential agentic settings\"\n- Front-load taxonomy scope limitation with parenthetical\n\n### §3 Taxonomy\n- \"Scope of ambiguity\" paragraph well-written; no changes if §1 front-loads scope\n\n### §4 Method\n- §4.4: Add within-judge-group auth scope ranges\n- §4.6: Strengthen SESOI domain justification; acknowledge field-standard absence\n\n### §5 Results\n- §5.1: Report 76.6% residual; note 22.4% = 0.4% between-type + 22.0% within-type\n- §5.2: Attach margin condition; note omnibus p=0.079 sans incompleteness; weaken bootstrap language; report 5-model Kendall's W p=0.072\n- §5.3: Compress to 3-4 lines\n- §5.4: Annotate Figure 3 judge assignments; report within-judge ranges; elevate caveats\n\n### §6 Analysis\n- §6.2: Standardize 4.6% vs ≤11%\n- §6.3: Systematic nocuity = strongest novel finding — could receive more emphasis\n\n### §7 Discussion\n- Differential nocuity: hypothesis, not framework; reduce reliance on auth scope model differences\n- Mitigation: label two experiments' design differences; discuss prompt sensitivity as finding\n\n### §8 Conclusion\n- Domain qualifier; margin condition on gradient; coreferential confound-free anchor\n\n### Limitations\n- Already comprehensive; add judge family bias direction discussion and cross-family evaluation recommendation",
  "project": "policy_ambiguity_safety",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.5 Borderline Conference",
  "review_chat_id": "oc_967344d166ba485ad606d14379e69d85"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# Consolidated Review Report — Round 12\n\n**Paper**: \"Not All Policy Ambiguity Is Equal: Type-Specific Safety Risks for LLM Agents\"\n**Venue**: EMNLP 2026 via ARR May cycle (deadline: 2026-05-25)\n**Reviewers**: R1 (方法严谨性, 3.5/5) + R2 (新颖性/完整性, 3.5/5)\n**Cross-response**: 完成，19/22 条 AGREE，2 条 REBUT（taxonomy 术语严重程度 + perturbation control 分工设计）\n\n---\n\n## Summary\n\nThis paper presents a matched-pair causal study on τ²-bench examining how six types of policy ambiguity affect safety violations in LLM agents. Using 300 clause pairs evaluated across five models (2,997 episodes), the study finds: (1) ambiguous clauses increase violation rates by 34.0 pp (OR=15.1); (2) incompleteness consistently ranks highest (46–62% across seven models) with a risk gradient rather than sharp tiers; (3) agents exhibit Disambiguation Neglect (≤11% awareness) and systematic nocuity (41.3% majority-convergent violations). The methodology is well-designed with perturbation controls, cross-judge evaluation, and comprehensive statistical analysis. Two additional model families replicate core findings.\n\n---\n\n## Strengths\n\n**S1** [Consensus] First matched-pair causal study of ambiguity type → agent safety violation, filling an important empirical gap. Perturbation control + matched-pair design provides stronger causal inference than observational studies.\n\n**S2** [Consensus] Statistical methodology quality exceeds the field norm — TOST equivalence testing + bootstrap cluster + Holm-Bonferroni correction + sensitivity analysis across seven margins. Claim calibration (C3 inconclusive, C4 exploratory) demonstrates excellent intellectual honesty.\n\n**S3** [Consensus] Seven models across six providers (5 primary + 2 replication) is among the broadest model coverage in agent safety research. ICC=0.919 demonstrates reproducibility (within OpenAI family).\n\n**S4** [Consensus] Disambiguation Neglect (4.6% overall, ≤11% per-model) and systematic nocuity (41.3% majority-convergent, 13% universal) are valuable empirical contributions with direct deployment implications.\n\n**S5** [Consensus] Type → failure mode mapping (§6.1: structural misparse, information gap-filling, boundary violation) is practically valuable, with majority-consistency (≥3/5 models) for each type's dominant failure mode.\n\n**S6** [Consensus] Writing is clear and well-structured within 8-page constraints. Limitations section is candid and specific.\n\n---\n\n## Weaknesses\n\n### MUST-FIX (4 issues — all consensus)\n\n**[MF-1]** \"22× more variance\" claim is misleading (R2-N1, R1-AGREE)\n- §5.1 decomposition: clause identity 22.4% = between-type 0.4% + within-type 22.0%. The taxonomy itself explains only 0.4% of variance — 55× less than within-type clause wording. Placed in the contribution list after C2, readers naturally interpret \"22×\" as type-level explanatory power. Combined with 76.6% unexplained variance (evaluation pipeline noise), this constitutes overclaiming.\n- **Required fix**: (1) Distinguish clause-level vs type-level variance in contributions; (2) Discuss 0.4% implications for taxonomy utility in §5.1; (3) Demote \"22×\" from headline contribution to supporting evidence; (4) Report 76.6% residual.\n\n**[MF-2]** C2 \"risk gradient\" claim is margin-dependent (R1-N1, R2-AGREE-w-qualification)\n- The gradient structure holds at ±15pp (6/6 mid-tier pairs equivalent) but collapses at ±10pp (3/6). No field-standard SESOI exists. Bootstrap cluster analysis (AU p=0.47) does not corroborate — the singleton partition reproduces in only 34.3% of bootstrap samples. Excluding incompleteness, omnibus p=0.079 (pairwise gradient partially survives: auth scope/lexical > coreferential).\n- **Required fix**: (1) Attach margin condition to every C2 claim statement (\"at the ±15pp margin\"); (2) Abstract/Conclusion must acknowledge margin-dependence; (3) Weaken bootstrap \"corroborates\" language; (4) Note p=0.079 excluding incompleteness.\n\n**[MF-3]** Cross-judge asymmetry threatens C4 conclusions (R1-N2, R2-AGREE)\n- GPT-5.4 judges Claude/GPT-4.1/Qwen3; GPT-4.1 judges GPT-5.4/DeepSeek. Authorization scope 52pp range (Claude 12% → GPT-5.4 64%) crosses the judge boundary, and auth scope has the lowest inter-judge κ (0.385). Within-judge-group auth scope: GPT-5.4-judged range = 34pp (Claude 12%, GPT-4.1 46%, Qwen3 26%), GPT-4.1-judged range = 4pp (GPT-5.4 64%, DeepSeek 60%). Appendix P type ranking ρ=−0.03 across judge groups. Figure 3 and \"most model-differentiating type\" framing give readers a much stronger impression than caveats warrant.\n- **Required fix**: (1) Figure 3 caption annotate judge assignments; (2) Report within-judge-group auth scope ranges; (3) Elevate caveat to Figure 3 caption and Discussion; (4) Position differential nocuity as hypothesis, not established framework.\n\n**[MF-4]** Incompleteness information-addition confound insufficiently controlled (R1-N3, R2-W3, mutual AGREE)\n- Incompleteness's unambiguous variant adds entirely new policy content (+34.6 words) rather than merely resolving ambiguity. Token count proxy is admittedly coarse. Cross-type counter-evidence (auth scope +36.1 > incompleteness +34.6) compares semantically different content types — not apples-to-apples. Token delta OR=1.022/token cumulates to ~2.15× odds multiplier over ~35 tokens.\n- **Required fix**: (1) Consistently label 49.2pp as \"upper bound including potential information-addition inflation\"; (2) Use coreferential 18.7pp as confound-free anchor in Abstract/Conclusion; (3) Discuss propositional content analysis as better but unimplemented proxy; (4) Acknowledge cross-type token delta comparison limitations.\n\n### SHOULD-FIX (8 issues)\n\n**[SF-1]** Front-load taxonomy scope limitation (R2-N2 critical, R1-REBUT but agrees on partial fix)\n- Incompleteness = information absence, conditional precedence = normative conflict. §3 \"Scope of ambiguity\" addresses this well but comes too late (page 3). R1 argues against changing terminology, citing RE literature connection.\n- **Fix**: Add parenthetical in §1 (\"including specification-level gaps that, while not ambiguity in the strict linguistic sense, produce identical behavioral outcomes in LLM agents\"). Consider \"including specification-level gaps\" in Abstract.\n\n**[SF-2]** Mitigation experiment direction contradiction (R2-W1, R1-AGREE)\n- §7 GPT-5.4 type-specific incompleteness: +14pp (p=0.118). Appendix B GPT-5.4 incompleteness: −2.6pp. Same model, same type, different prompt and design.\n- **Fix**: Report both prompt formulations; discuss prompt sensitivity as a finding; label design differences at first mention.\n\n**[SF-3]** Disambiguation Neglect novelty positioning (R2-W2, R1-AGREE)\n- Liu et al. (2023) + Hu et al. (2025) established core phenomenon. Contribution is quantifying in agentic settings.\n- **Fix**: Contribution (3) \"revealing\" → \"quantifying in consequential agentic settings and identifying systematic nocuity.\"\n\n**[SF-4]** Per-type human validation CIs uninformative (R1-W2, R2-AGREE)\n- n=32-34 per type. Scopal κ CI=[0.00, 1.00]. Appendix G draws type-level conclusions despite §4.4's \"lack power\" caveat.\n- **Fix**: Appendix G must state per-type results are descriptive/suggestive only.\n\n**[SF-5]** Judge family bias (R1-W3, R2-AGREE)\n- Both judges from OpenAI. Claude's 30.3% could reflect genuine robustness or systematic bias.\n- **Fix**: Discuss possible bias direction; recommend cross-family judge evaluation in Future Work.\n\n**[SF-6]** C4 2.9% variance vs Discussion weight (R1-W4, R2-AGREE)\n- Interaction explains 2.9% variance; Discussion gives it disproportionate theoretical weight.\n- **Fix**: Position differential nocuity as hypothesis; attach effect size + uncertainty caveats.\n\n**[SF-7]** Kendall's W selective reporting (R1-W6, R2-AGREE-w-qualification)\n- 5-model W=0.398 (p=0.072) non-significant; 7-model excluding coreferential p=0.038 significant.\n- **Fix**: §5.2 report 5-model p=0.072; characterize as \"trending toward concordance.\"\n\n**[SF-8]** Single benchmark external validity (R2-W4, R1-AGREE with lower severity)\n- All experiments on τ²-bench (retail + airline). Abstract/Conclusion overgeneralize.\n- **Fix**: Add domain qualifiers in Abstract and Conclusion.\n\n### MINOR (7 issues)\n\n- [MI-1] 4.6% vs ≤11% awareness numbers used interchangeably — standardize.\n- [MI-2] C3 §5.3 can compress from ~6 lines to 3-4.\n- [MI-3] Table 2 caption too long — move Tier definitions to footnote.\n- [MI-4] Bootstrap ranking preservation (99.5%) must note within GPT-5.4 judge subset only.\n- [MI-5] ICC=0.919 within OpenAI family only — note cross-provider untested.\n- [MI-6] Pages 4-5 consecutive text-only (Visual check warning).\n- [MI-7] Page 8 compresses 5 sections — rushed ending impression (Visual check warning).\n\n---\n\n## Reviewer Consensus\n\nAll critical items reached [AGREE]:\n1. \"22× variance\" overclaiming — taxonomy explains 0.4% between-type variance [MF-1]\n2. C2 gradient collapses at ±10pp — margin-dependence must enter claim [MF-2]\n3. Auth scope 52pp crosses judge boundary with lowest κ — C4 needs stronger caveats [MF-3]\n4. Incompleteness confound token count proxy insufficient [MF-4]\n5. Mitigation §7 vs Appendix B contradiction needs analysis [SF-2]\n6. Disambiguation Neglect is quantification of known phenomenon [SF-3]\n7. **Bottleneck is claim calibration, not methodology** — both note fixing claims → 4.0 achievable\n\n## Reviewer Divergence\n\n1. **Taxonomy terminology** (R2-N2 vs R1-REBUT): R2 proposes \"policy underspecification\"; R1 argues this weakens RE literature connection. Both agree scope should be front-loaded in §1. **Director assessment**: R1's position is stronger — the paper's theoretical contribution depends on extending Berry & Kamsties (2004). Front-loading scope limitation in §1 is the proportionate fix.\n\n2. **Perturbation control applicability** (R1-W5 vs R2-REBUT): R1 argues structural mismatch for specification-layer types. R2 correctly notes §4.5's explicit two-pronged design (perturbation control for surface, logistic regression for information). **Director assessment**: R2's point stands, but the logistic regression's coarse proxy (MF-4) means the compound control for specification-layer types remains weaker. Already covered by MF-4.\n\n---\n\n## Questions for Authors\n\n1. What are the within-judge-group auth scope violation rates? If both groups show ranges far smaller than 52pp, this confirms judge effect.\n2. Is propositional content analysis (vs token count) feasible as a follow-up for the incompleteness confound?\n3. Given 0.4% between-type variance, should the taxonomy's primary claimed value shift from variance explanation to failure mode prediction (§6.1)?\n4. Excluding incompleteness, omnibus p=0.079 — should C2 be reframed around the partial pairwise survival?\n5. Any qualitative comparison with DRIP-R's naturally occurring policy ambiguity instances for ecological validity?\n6. What are C3's direction and effect size after controlling for token delta?\n\n---\n\n## Missing References\n\nR2 suggests \"The Causal Impact of Tool Affordance on Safety Alignment\" (arXiv:2603.20320). Existence not verified; if real, marginally relevant to §2 Agent Safety but not critical.\n\n---\n\n## External Review\n\n**Status**: Not requested.\n\n---\n\n## Visual Layout Check (非评分项)\n\n**Status**: Done (2026-05-22 09:54:26 UTC). 0 critical, 2 warning, 6 info.\n\n| Severity | Location | Finding |\n|----------|----------|---------|\n| ⚠️ Warning | Pages 4-5 | Method §4 连续两页纯文本无 display item，审稿人容易失去视觉锚点 |\n| ⚠️ Warning | Page 8 | §6.2–§8+Limitations 压缩 5 个 section 在单页，匆忙收尾印象 |\n| ℹ️ Info | Page 6 | Figure 2 bar 标签字号偏小（约正文 60-65%） |\n| ℹ️ Info | Page 7 | Figure 3 heatmap 数字字号偏小 |\n| ℹ️ Info | Page 2 | Figure 1 三面板视觉风格略不统一 |\n| ℹ️ Info | Page 6 | Table 2 格式规范 |\n| ℹ️ Info | Page 3 | Table 1 格式整洁 |\n| ℹ️ Info | Page 15 | Appendix 末页大面积空白 |\n\n---\n\n## Overall Assessment\n\n**Score: 3.5 / 5 — Borderline Conference**\n**Confidence: 4 / 5**\n**ARR scale: 3.5 = Borderline Conference**\n\n**Rationale**: The paper addresses an important question — whether ambiguity type in policy specifications causally determines safety violation severity — with a matched-pair methodology exceeding the field's empirical standard. C1 (+34.0pp, OR=15.1) is robust across seven models. The error analysis (Disambiguation Neglect, systematic nocuity) provides actionable deployment insights.\n\nHowever, the paper's secondary claims require calibration:\n- C2's \"risk gradient\" is margin-dependent (±15pp only), with bootstrap non-supportive and incompleteness potentially confound-inflated\n- \"22×\" contribution headline misrepresents the variance decomposition (clause wording, not type membership)\n- C4's auth scope interaction is confounded by cross-judge asymmetry on the lowest-agreement type\n\n**These are claim calibration problems, not methodological design flaws.** The underlying data and statistical framework are sound. Both reviewers independently assess that fixing the four must-fix items (claim recalibration, not new experiments) would bring the paper to 4.0 (Conference level).\n\n**Upgrade path**: Fix MF-1 through MF-4 (claim calibration) + SF-1 through SF-3 (framing adjustments) → 4.0.\n\n---\n\n## Detailed Comments\n\n### Abstract\n- \"22× more variance\" → reframe as clause-level (not type-level) finding\n- \"risk gradient rather than sharp tiers\" → add margin condition or soften\n- Add domain qualifier or \"specification-level gaps\" parenthetical\n- Use coreferential 18.7pp as confound-free anchor alongside incompleteness upper bound\n\n### §1 Introduction\n- Contribution (2): separate clause identity from type gradient; demote \"22×\"\n- Contribution (3): \"revealing\" → \"quantifying in consequential agentic settings\"\n- Front-load taxonomy scope limitation with parenthetical\n\n### §3 Taxonomy\n- \"Scope of ambiguity\" paragraph well-written; no changes if §1 front-loads scope\n\n### §4 Method\n- §4.4: Add within-judge-group auth scope ranges\n- §4.6: Strengthen SESOI domain justification; acknowledge field-standard absence\n\n### §5 Results\n- §5.1: Report 76.6% residual; note 22.4% = 0.4% between-type + 22.0% within-type\n- §5.2: Attach margin condition; note omnibus p=0.079 sans incompleteness; weaken bootstrap language; report 5-model Kendall's W p=0.072\n- §5.3: Compress to 3-4 lines\n- §5.4: Annotate Figure 3 judge assignments; report within-judge ranges; elevate caveats\n\n### §6 Analysis\n- §6.2: Standardize 4.6% vs ≤11%\n- §6.3: Systematic nocuity = strongest novel finding — could receive more emphasis\n\n### §7 Discussion\n- Differential nocuity: hypothesis, not framework; reduce reliance on auth scope model differences\n- Mitigation: label two experiments' design differences; discuss prompt sensitivity as finding\n\n### §8 Conclusion\n- Domain qualifier; margin condition on gradient; coreferential confound-free anchor\n\n### Limitations\n- Already comprehensive; add judge family bias direction discussion and cross-family evaluation recommendation",
    "project": "policy_ambiguity_safety",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.5 Borderline Conference",
    "review_chat_id": "oc_967344d166ba485ad606d14379e69d85"
  }
}
```

</details>

---


### Tool result

_source line 1073 · 2026-05-22T10:09:38.338340+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_10fa2e89afc5e9b8a13613245e008dd9:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4068
}
```

</details>

---


### Assistant

_source line 1074 · 2026-05-22T10:09:47.864698+00:00_

Round 12 审稿完成，报告已投递给 Research Director。

**总结**：
- **评分**：3.5 / 5 (Borderline Conference)，与 Round 11 持平
- **4 个 Must-Fix**：(1) "22×" claim overclaiming——taxonomy 仅解释 0.4% between-type variance；(2) C2 risk gradient margin-dependent——±10pp 时瓦解；(3) C4 cross-judge asymmetry——auth scope 52pp 跨 judge 边界且 κ=0.385；(4) incompleteness confound token count proxy 不充分
- **8 个 Should-Fix**：taxonomy scope 前置、mitigation 方向矛盾、Disambiguation Neglect 定位、per-type CI 无信息、judge family bias、C4 Discussion 权重、Kendall's W 选择性报告、单一 benchmark 外部效度
- **核心判断**：bottleneck 是 claim calibration 而非方法设计本身。修复 4 个 MF（均为文字修改，不需新实验）+ 3 个核心 SF 可升至 4.0 (Conference)
- **Issue Tracker** 已同步更新（2 critical, 12 warning, 5 info, 8 resolved）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 101

## Round 101

2 recorded events


### User

_source line 1075 · 2026-05-22T10:09:50.525440+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。对 R1 的 16 条意见中 14 条 AGREE（含 4 条 with qualification），仅 REBUT 了 W5（perturbation control 分工设计被错置）。两份 review 互补性强——R1 侧重方法论（SESOI、cross-judge），R2 侧重概念（22× claim、taxonomy 定义），合并后指向 4 个 critical issues。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1076 · 2026-05-22T10:10:01.307926+00:00_

Round 12 审稿已完成。报告已投递给 Research Director。

**最终结果：3.5 / 5 — Borderline Conference**

两位 Reviewer 高度一致（19/22 AGREE），核心问题集中在 **claim 校准**而非方法设计：

| 级别 | 数量 | 关键问题 |
|------|------|----------|
| MUST-FIX | 4 | 22× overclaiming、C2 margin-dependence、C4 cross-judge confound、incompleteness confound |
| SHOULD-FIX | 8 | taxonomy scope 前置、mitigation 矛盾、DN novelty 定位、per-type CIs、judge family bias、C4 权重、Kendall's W 报告、外部效度 |
| MINOR | 7 | 数字统一、C3 压缩、Table caption、Figure 注释等 |

**升级路径**：修复 MF-1~MF-4（claim 重新校准，无需新实验）+ SF-1~SF-3（framing 调整）→ 4.0 (Conference)。

Issue Tracker 已同步更新至 `artifacts/review_issues.yaml`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 102

## Round 102

2 recorded events


### User

_source line 1077 · 2026-05-22T12:13:07.860237+00:00_

[Reviewer 1 审稿意见]:
## Dream Review — Reviewer 1（方法 + 实验）

**论文**: Causal Anatomy of Policy Ambiguity Vulnerability in LLM Agents
**Dream ID**: 20260522T111643 / worst tier
**Venue**: EMNLP 2026 via ARR

---

## 总体评分

**Overall**: 2.5 / 5 — Borderline Findings
**Soundness**: 3.0/5 — τ²-bench 内部方法论扎实，但 SOPBench 失败使核心 claim 的 scope 大幅收窄，且论文未充分反映这一收窄
**Excitement**: 2.5/5 — 单一 benchmark + 失败的 cross-benchmark + ~5页正文，contribution 密度不足以支撑 Conference

**一句话总结**: τ²-bench 内部的因果设计和 measurement chain 是该领域最严谨的，但 SOPBench 复制失败（Δ=8.3pp, p=0.068）使 generalizability 严重存疑，而论文仅以一句 limitation 处理此失败——claim 与 evidence scope 不匹配是致命伤。

---

## Strengths

**S1**: Matched-pair + perturbation control 的因果推断框架是该领域方法论标杆。Perturbation control（Δ=-0.67pp, CI [-8.0, 6.67], Table 4）有效隔离了 ambiguity-specific causation 与一般 prompt sensitivity——这比任何 correlational cross-benchmark study 的因果推断都更强。**[idea层面]**

**S2**: Measurement validation chain 完整度超越同类工作。ICC=0.919 [0.892, 0.940]（§5.6）、human-LLM κ=0.807（§5.6）、perturbation control PASS（Table 4）三重验证构成闭环。Human-LLM agreement 超过 human inter-annotator agreement（0.807 > 0.762），是 LLM-as-judge 验证的 gold standard。**[idea层面]**

**S3**: Error analysis 的 type→failure mode 映射（Table 5）提供了 quantitative findings 背后的 mechanistic "why"——auth_scope → unauthorized escalation (77%), incompleteness → assumption-based action (64%), scopal → scope misapplication (76%)。5/6 types 在所有 5 models 上保持 dominant mode 一致性。这是本文最高 EMNLP-value 的贡献之一。**[idea层面]**

**S4**: Claim calibration 诚实：C3 标注 "suggestive"（§5.3），C4 interaction 报告了 2.9% variance 和 κ=0.384 的 measurement uncertainty，Ambiguity Blindness 量化为具体数字（4.6% overall）。**[presentation层面]**

---

## Must-Fix

**N1** [critical, idea层面] SOPBench 复制失败的处理严重不足——claim scope 与 evidence scope 不匹配

- **具体位置**: §8 Limitations（一句话提及）vs. Abstract/§9 Conclusion（隐含 broad generalizability）
- **问题**: SOPBench cross-benchmark 复制失败是本文最重要的 negative result：pooled Δ=8.3pp, p=0.068, CI 含零；type ranking ρ=0.14 与 τ²-bench 无关联（review_context.yaml）。论文在 §8 仅以一句话处理："Expanding domain generalization to healthcare and banking domains was attempted via SOPBench but did not meaningfully replicate (pooled Δ=8.3pp, p=0.068), likely due to rule-based verifier insensitivity to semantic violations." 但 Abstract 说 "the first matched-pair causal study testing the safety impact of policy ambiguity across 5 (+2) architecturally diverse models"——暗示模型 breadth 可以替代 domain breadth 作为 generalizability evidence，而实际数据不支持这一替代。
- **核心问题**: 如果 ambiguity → violation 的因果链在 healthcare/bank domains 上 effect size 降低 4-6× 且不显著，那么"policy ambiguity universally causes massive safety violations"这一叙事只在 customer service 成立。论文需要将所有 claim 限定到 tested domains。
- **为什么是 Must-Fix**: EMNLP reviewer 看到单一 benchmark 就会要求 generalizability evidence。论文自己尝试了但失败了——隐藏这个 negative result 比不尝试更糟糕，因为 reviewer 发现后会质疑 selective reporting。
- **建议**: (1) 在 §5 或独立的 §5.x 中报告 SOPBench 结果（至少 pooled Δ、CI、p-value），不需要 full table 但需要 honest framing；(2) Abstract 和 Conclusion 限定 scope 为 "customer-service agent domains"；(3) 讨论 verifier incompatibility 假说（rule-based verifier vs semantic violations）作为失败原因——这本身是 methodological insight。

**N2** [critical, idea层面] Token delta 的 layer-level 系统差异（spec 34 vs ling 13 words）引入未充分控制的 confound

- **具体位置**: §4.1（token delta mentioned），§5.5（perturbation control），review_context.yaml（avg_token_delta_spec_layer: 34.2, avg_token_delta_ling_layer: 12.8）
- **问题**: Specification-layer types 的 unambiguous variants 平均添加 34 words，linguistic-layer types 仅添加 13 words。这是 2.6× 的差异。Perturbation control（Table 4）使用 synonym substitution 和 clause reordering——这些是 low-magnitude surface changes（几个词的替换或重排），无法模拟添加 34 words 新内容的效果。因此：
  - (a) Perturbation control 对 spec-layer types 的 specificity claim 支撑不足——它证明了"改几个词无效"，但没有证明"添加 34 words 的效果是 ambiguity-specific 而非 information-addition-driven"
  - (b) C3 layer effect（spec 44% vs ling 38%, §5.3）可能部分或完全由 token delta 差异驱动——论文承认 "controlling for token delta reverses the direction" 但未报告 reversed direction 的 effect size
  - (c) Logistic regression（§5.6 提及 token delta coef=0.022）控制了 per-clause token delta，但 coef=0.022 per token × 34 tokens = 0.75 log-odds shift 不可忽略
- **为什么是 Must-Fix**: 这个 confound 同时影响 C2（incompleteness upper-bound status）和 C3（layer effect）。如果 spec-layer types 的高 violation rate 部分由 information asymmetry 驱动，taxonomy 的两层结构的实证基础被削弱。
- **建议**: (1) 报告 logistic regression 中 controlling for token delta 后 C3 的 direction 和 effect size；(2) 在 per-type 讨论中区分"confound-free lower bound"（coreferential, token delta=0）和"confound-inclusive upper bound"（incompleteness, token delta≈35）；(3) 考虑 information-addition matched control（添加相同长度的无关信息）作为 future work。

**N3** [critical, presentation层面] 论文密度与 EMNLP long paper 标准不匹配

- **具体位置**: 整体结构（~5页正文 + ~1页 references）
- **问题**: EMNLP 2026 long paper 允许 8 页正文。本文仅约 5 页，缺少：(a) 无 Appendix（TOST sensitivity table、logistic regression full results、per-type judge agreement、clause length analysis 等均未呈现）；(b) Related Work 仅约半页（§2），缺少与 DRIP-R 的详细比较、与 prompt sensitivity literature 的区分；(c) Discussion 仅约半页（§7），缺少 practical implications 的深度讨论。在 8/15 = 53% 的空间利用率下，reviewer 会质疑 contribution depth。
- **建议**: 充分利用 8 页空间。TOST sensitivity analysis、logistic regression full table、SOPBench negative results、per-type ICC breakdown 等 material 应从 appendix 升级到正文或至少加入 appendix。

---

## Should-Fix

**W1** [warning, idea层面] C3 layer effect "suggestive" 的 within-judge fragility 意味着它不应作为 claim 出现

- **具体位置**: §5.3, review_context.yaml（c3_within_judge_gpt54_p: 0.059, c3_within_judge_gpt41_p: 0.157）
- **问题**: C3 pooled p=0.017，但 within-judge subgroup 分析（GPT-5.4 judged group p=0.059, GPT-4.1 judged group p=0.157, review_context.yaml）表明该 effect 在两个 judge group 中都不 individually significant。论文称 "suggestive rather than confirmed"，但仍以独立 subsection（§5.3）呈现。更关键的是，review_context.yaml 显示 C3 power 仅 0.68（underpowered for observed effect）——这意味着 null result 是 expected 的。
- **建议**: 将 C3 从独立 subsection 压缩为 §5.2 末尾一段（3-4 行），或降级为 appendix 中的 supplementary analysis。在正文说明 within-judge fragility 和 underpowered 状态。

**W2** [warning, idea层面] Error analysis 的 300 traces 抽样和分类方法描述不足

- **具体位置**: §6（"Analysis of 300 violation traces (50 per type, pooled across 5 models)"）
- **问题**: (a) 抽样方法未说明——50/type 是 random sample 还是 stratified by model？如果 random，某些 model-type 组合可能被 undersampled（如 coreferential-Claude 仅 ~6 traces if proportional）；(b) 分类方案的来源未说明——5 种 failure mode 是 deductive（来自 prior taxonomy）还是 inductive（from data）？如果 inductive，需要说明 saturation/convergence 标准；(c) Table 5 显示 cond_prec 的 dominant mode 为 "Mixed" (35%+29%)——这个 "dominant" label 的操作定义是什么？35% 是否足以称为 "dominant"？(d) Inter-coder reliability 未报告——300 traces 由谁编码？如果是 LLM-coded（review_context.yaml 提及 "LLM-coded traces"），需要与 human-coded subset 的一致性验证。
- **建议**: (1) 说明抽样策略和 per-model-type cell size；(2) 说明分类方案来源和 coding protocol；(3) 报告 inter-coder agreement（review_context.yaml 显示 Gwet's AC₁=0.62, Cohen's κ=0.52——这些数据应在论文中报告）；(4) 对 cond_prec 的 "mixed" 分布给出解释。

**W3** [warning, idea层面] Cross-judge agreement 76% exact / weighted κ=0.685 的报告缺少 per-type breakdown

- **具体位置**: §4.4, §5.6
- **问题**: 论文报告 cross-judge exact agreement 76%, weighted κ=0.685（§5.6），但未给出 per-type breakdown。Review_context.yaml 显示 c4_fleiss_kappa=0.384——这是 authorization scope 的 agreement 吗？如果是，那么 C4 的 star finding（auth_scope 52pp range）建立在最低 agreement 的类型上。论文在 §5.4 提到 κ=0.384 但未充分讨论其对 52pp range claim 的影响。76% exact agreement 在 4-tier severity scale 上 acceptable，但 binary 层面（violation/no-violation）的 per-type agreement 是 claim 可信度的关键——特别是 auth_scope。
- **建议**: (1) 报告 per-type cross-judge binary agreement；(2) 在 §5.4 讨论 auth_scope 的 low κ 对 52pp range 的 measurement uncertainty 含义；(3) 考虑报告 prevalence-adjusted κ 以解释 prevalence paradox。

**W4** [warning, presentation层面] DeBERTa classifier PoC（§6.1）分散叙事焦点

- **具体位置**: §6.1
- **问题**: 论文的核心叙事是 "因果分析 → type-specific risk → failure mechanisms"。DeBERTa classifier（binary F1=0.806, incompleteness F1=0.34）本身是有趣的结果，但在 ~5 页正文中占据 ~1/3 页，与因果分析的主线关联薄弱。它回答的是"能否自动检测 ambiguity"而非"ambiguity 如何影响 safety"——这是一个不同的研究问题。在空间极度紧张的 worst-tier 论文中，这 1/3 页如果用于 SOPBench negative results 的 honest reporting 或 C2 TOST sensitivity analysis，对论文的 soundness 贡献更大。
- **建议**: 将 classifier PoC 移至 appendix，在正文仅保留一句提及（"a proof-of-concept classifier achieves F1=0.81 for binary detection but only 0.34 for the highest-risk type; see Appendix"）。释放空间给 SOPBench results 和 statistical details。

**W5** [warning, idea层面] ICC=0.919 仅限 OpenAI family 内部，cross-provider reproducibility 未测量

- **具体位置**: §5.6（"30 clauses × 3 replicates × 2 conditions × 2 models"）
- **问题**: Review_context.yaml 确认 ICC 测试使用 2 models（gpt-5.4 和 gpt-4.1），均为 OpenAI family。这测量的是 API sampling stability，但 cross-provider reproducibility（如 Claude 或 DeepSeek 在相同 clause 上的 replicate stability）未验证。考虑到 Claude 的 overall violation rate（30.3%）远低于其他模型，其 ICC 可能不同。同时，per-type ICC 显示 spec-layer（0.807-0.857）明显低于 ling-layer（0.976-0.989, review_context.yaml）——这个 layer-level ICC gap 本身是 substantive finding（支持 disambiguation channel 假说），但论文仅报告 overall ICC 而未利用 per-type breakdown。
- **建议**: (1) 明确 ICC 测试限于 OpenAI models；(2) 在正文报告 per-type/per-layer ICC breakdown——这是 free evidence for the disambiguation channel framework；(3) 讨论 cross-provider ICC 作为 limitation。

---

## Minor

**M1**: Logistic regression（§5.6 提及 coef=2.278 for condition, 0.022 for token delta）未报告 pseudo-R²、model diagnostics 或 full coefficient table。在无 appendix 的情况下，读者无法评估 model fit quality。

**M2**: "Ambiguity Blindness" 命名。§6 使用此术语指 <5% disambiguation awareness。"Blindness" 暗示 inability，但论文 Discussion（§7）和 review_context.yaml 中的 mitigation experiment（-8.5pp pooled）表明 agents *can* disambiguate when prompted。"Disambiguation Neglect"（review_context.yaml 中出现的备选术语）更精确——neglect = default absence of behavior, not inability。

**M3**: Table 1 报告 5 models 的 pooled OR=15.1，但各 model OR 范围 from 8.3（DeepSeek）to 12.4（GPT-5.4）。Pooled OR 受 Simpson's paradox 风险——如果 model-specific base rates 差异大（Claude 30% vs DeepSeek 50%），pooled OR 可能不等于加权平均。建议报告 model-specific OR 的 range。

**M4**: Realism validation against DRIP-R（§5.6 提及 "no significant distributional differences on sentence length, parse depth, or type-token ratio"）是重要的 ecological validity 证据，但 review_context.yaml 显示 Flesch-Kincaid readability marginally significant（p=0.08）。建议报告此 marginal difference 以完整性。

---

## 对照实验设计文件（review_context.yaml）的覆盖度评估

Review_context.yaml 列出 12 个 imagined experiments。论文覆盖情况：

| Experiment | 论文覆盖 | 评估 |
|---|---|---|
| full_study_clause_generation (plan_001) | §4.1 简要提及 | ✓ 充分 |
| new_type_mini_pilot (plan_001b) | 未报告 | ✓ 合理省略（pilot） |
| full_study_api (plan_002) | Table 1 | ✓ 充分 |
| full_study_opensource (plan_003) | Table 1 | ✓ 充分 |
| full_study_analysis (plan_004) | §5.1-5.4 | ⚠ C2 TOST sensitivity 未呈现 |
| error_analysis (plan_005) | §6, Table 5 | ⚠ 抽样方法和 inter-coder reliability 未报告 |
| reliability_test (plan_006) | §5.6 一句话 | ⚠ Per-type ICC breakdown 丢失 |
| realism_validation (plan_007) | §5.6 一句话 | ⚠ Marginal FK difference 未报告 |
| judge_calibration (plan_009) | §5.6 | ✓ 核心指标充分 |
| perturbation_control (plan_010) | §5.5, Table 4 | ✓ 充分 |
| **sopbench_cross_benchmark (plan_017)** | **§8 一句话** | **✗ 严重不足——negative result 需完整报告** |
| classifier_poc (plan_008) | §6.1 | ⚠ 占用过多正文空间 |

**关键遗漏**:
1. **SOPBench detailed results**（最大问题）: Pooled Δ=8.3pp, per-domain breakdown（healthcare 11.2pp marginal / bank 5.4pp non-sig）、type ranking ρ=0.14、verifier compatibility analysis 全部缺失。这不是可选信息——这是 reviewer 评估 generalizability claim 的必要数据。
2. **TOST sensitivity table**: Review_context.yaml 显示 7 个 margin 的 equivalence pattern，论文仅引用 ±15pp 结果。缺少 sensitivity analysis 使 C2 claim 看起来 margin-independent（实际不是）。
3. **Per-type ICC breakdown**: Spec-layer ICC (0.807-0.857) vs ling-layer (0.976-0.989) 的 gap 是 disambiguation channel 假说的 convergent evidence，论文完全未利用。
4. **Logistic regression full table**: review_context.yaml 显示完整的 predictor coefficients（包括 model dummies），论文仅报告 condition 和 token delta 两个 coef。
5. **Mitigation experiment**: review_context.yaml 中的 mitigation data（-8.5pp pooled across 5 models）未在论文中呈现。Discussion §7 提到 "safety training selectivity" 但缺少 empirical mitigation evidence。

**总结**: 论文在 ~5 页中覆盖了 imagined experiments 的核心结果，但关键 negative result（SOPBench）和关键 robustness checks（TOST sensitivity、per-type ICC、logistic regression details）被省略。这些遗漏在 space-constrained 版本中可以理解，但 EMNLP long paper 有 8 页 + unlimited appendix——没有理由不报告。

---

## Questions for Authors

1. SOPBench verifier compatibility analysis（review_context.yaml 显示 32% false negative rate）是否已完成？如果 verifier 的 false negative rate 达到 32%，SOPBench 的 null result 可能反映 measurement failure 而非 effect absence——这需要在论文中讨论。

2. Per-type ICC 的 layer-level gap（ling 0.976-0.989 vs spec 0.807-0.857）是否与 disambiguation channel 假说形成 convergent evidence？为什么不在正文报告？

3. Controlling for token delta 后 C3 layer effect reverses direction——reversed 的 direction 是什么（ling > spec？）？effect size 多大？这对 taxonomy 的两层结构有什么理论意义？

4. Error analysis 的 300 traces 是 LLM-coded 还是 human-coded？如果是 LLM-coded，与 human-coded subset 的一致性是多少？

---

## 与提交版本对比的关键差异

（注：我已审阅过该项目的提交版本。以下比较旨在帮助 Director 理解 worst tier 的具体影响。）

| 维度 | 提交版本 | Dream worst 版本 | 影响 |
|---|---|---|---|
| SOPBench | 未出现 | 失败 (Δ=8.3pp, p=0.068) | 正文一句话处理——选择性报告风险 |
| C3 status | "Inconclusive" | "Suggestive" | 更弱但仍独立 subsection |
| Error analysis | 614 traces | 300 traces | 更少数据但 pattern 一致 |
| Terminology | "Disambiguation Neglect" | "Ambiguity Blindness" | Blindness 不精确 |
| Classifier | GPT-4.1 zero-shot | DeBERTa fine-tuned | 占用正文空间 |
| 页数 | 8页正文 + 7页附录 | ~5页正文无附录 | 密度严重不足 |
| Appendix | 17 sections 详尽 | 无 | 所有 robustness checks 不可见 |

**核心结论**: Worst-tier 论文的 τ²-bench 内部方法论与提交版本同样严谨，但 (1) SOPBench 失败的隐藏处理、(2) 正文空间严重未利用、(3) robustness evidence 全部缺失，三者叠加使其从 Borderline Conference (3.5) 降至 Borderline Findings (2.5)。如果充分利用 8 页 + appendix 空间并 honestly report SOPBench，可回升至 3.0 (Findings)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1078 · 2026-05-22T12:13:32.907580+00:00_

审稿报告已于本轮早些时候提交完毕。

这份 Dream Review 审查的是**假设的 worst-tier 版本**（~5页无附录、SOPBench 失败、DeBERTa classifier、"Ambiguity Blindness" 术语），**非实际提交版本**。Reviewer 1 自己在末尾的对比表中明确了差异：

| 维度 | 实际提交版 | Dream worst 版 |
|------|-----------|---------------|
| 页数 | 8页正文 + 7页附录 | ~5页无附录 |
| Error analysis | 614 traces | 300 traces |
| 术语 | Disambiguation Neglect | Ambiguity Blindness |
| Classifier | GPT-4.1 zero-shot (Appendix) | DeBERTa (正文) |
| SOPBench | 未出现 | 失败但隐藏处理 |
| Appendix | 17 sections | 无 |

实际提交版本的审稿报告（Round 12, 3.5 Borderline Conference）已投递至 Research Director，该 Dream Review 的发现不影响已提交的评审结论。Dream Review 中提到的 SOPBench、per-type ICC breakdown 等内容属于假设实验，不存在于实际论文中。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 103

## Round 103

2 recorded events


### User

_source line 1079 · 2026-05-22T12:13:35.457226+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

Dream worst-tier 论文的核心问题：SOPBench 跨 benchmark 复制失败（Δ=8.3pp, p=0.068）但仅在 Limitations 一句话提及——这是最大的 claim-evidence mismatch。加上仅约 5 页正文（EMNLP 允许 8 页）、无附录、关键 robustness checks 缺失，评分从提交版本的 3.5 降至 2.5（Borderline Findings）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1080 · 2026-05-22T12:14:03.908012+00:00_

Round 12 审稿报告已于此前成功投递至 Research Director（评分 3.5 Borderline Conference）。

这份 Dream Review（worst tier, 2.5 Borderline Findings）审查的是一个假想退化版本的论文（含 SOPBench 失败、~5页正文、无附录等），与实际提交版本存在重大差异。实际提交版本有 8 页正文 + 15 页附录，使用 "Disambiguation Neglect" 术语，GPT-4.1 zero-shot classifier 放在 Appendix，且不包含 SOPBench 实验。

该 Dream Review 的发现不影响已提交的 Round 12 报告。如需将 Dream Review 的观点纳入补充分析，请明确指示。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 104

## Round 104

2 recorded events


### User

_source line 1081 · 2026-05-22T12:14:05.412225+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 Dream 审稿意见 — "worst" scenario
**Dream ID**: 20260522T111643
**Paper**: Causal Anatomy of Policy Ambiguity Vulnerability in LLM Agents
**Overall**: 2.5 / 5 — Borderline Findings
**Reviewer Confidence**: 4/5

---

### Strengths

**S1** [idea] 方法论模板（Contribution 1）是最强贡献。Matched-pair + perturbation control + ICC + judge calibration 的完整 validation chain 在 agent safety evaluation 领域首创，比 DRIP-R（无 perturbation control）、PhantomPolicy（无 human validation）都更严谨。即使局限单一 benchmark，方法论本身有 template 价值。

**S2** [idea] Error Analysis §6 的 type-specific failure mode 对应关系（auth scope→unauthorized escalation 77%; scopal→scope misapplication 76%; incompleteness→assumption-based 64%）是 empirically novel 的。5/6 types dominant failure mode 跨模型一致，比 aggregate rates 更有 explanatory depth。

**S3** [idea] Incompleteness 作为 universal vulnerability（46–62% across 7 models, 16pp range）的 robustness compelling。

**S4** [presentation] SOPBench 失败的坦诚报告是学术诚信体现（虽然放置位置有问题，见 W4）。

---

### Major Weaknesses

**W1** [idea — critical] "Ambiguity Blindness" (<5%) 缺乏相对 prior work 的清晰增量

Liu et al. (2023) 已 demonstrate LLMs collapse multiple interpretations into single output。Li et al. (2024, garden-path) 在 behavioral level 确认 LLMs 表现出 single-parse commitment。arXiv:2603.05801 "Ambiguity Collapse by LLMs" (2026) 已建立完整 epistemic risk taxonomy。本文增量是在 agentic settings 中 quantify 这些已知现象并关联 safety violations——合理但需 explicitly 定位为 empirical extension 而非 conceptual discovery。§6 和 §1 的措辞未做此区分。

建议：将 "Ambiguity Blindness" 框定为 "quantifying known ambiguity-collapse in consequential agentic settings"。

**W2** [idea — critical] Contribution 3（7-model breadth）不成立为独立贡献

(a) 5 primary + 2 replication 的区别在 abstract 中被模糊——replication models 仅复制 C1，未参与 C2/C4/§6 分析；(b) 7-model breadth 替代的是 SOPBench 跨域失败后的 generalizability 论据，但模型数量≠域覆盖——同一 benchmark 上更多模型证明 cross-model robustness，不是 cross-domain generalizability；(c) 5-7 模型测试已是领域 norm（PhantomPolicy 6个, R-Judge 14个），不构成差异化。

建议：降级为 supporting evidence for C1 robustness。

**W3** [idea — major] Title "Causal Anatomy" 与实际分析不匹配

"Causal Anatomy" 暗示系统性因果路径分解（mediation analysis, DAG reasoning, SEM）。论文实际提供的是 causal identification（matched-pair + perturbation control），不是 causal anatomy。§6 failure mode taxonomy 是 descriptive coding，不是 mechanistic causal tracing。Auth scope→unauthorized escalation 是 correlation，未排除 judge artifact (κ=0.385) 等 confounders。

建议：改为 "Causal Study" 或 "Causal Dissection"。

**W4** [presentation — major] SOPBench 失败放在 Limitations 而非 Results 不当

§8 仅一句话提及 SOPBench 失败（pooled Δ=8.3pp, p=0.068）。从 review_context 可知这是 1,000 episodes 完整实验，有 per-domain breakdown（healthcare Δ=11.2pp marginal, bank Δ=5.4pp null）和 verifier compatibility analysis（32% false negative）。Type ranking ρ=0.14 与 τ²-bench 无相关——这是 substantive negative finding，不是 limitation。Abstract/Introduction 完全没有 domain scope 限定，reader 在 §8 前会假设跨域 generalizability。

建议：(1) Results 中报告 SOPBench 结果；(2) Abstract 加 domain 限定；(3) 讨论 verifier incompatibility 作为方法论 lesson。

---

### Minor Weaknesses

**W5** [idea] "Differential nocuity" 和 "systematic nocuity" 理论贡献有限——前者是 Willis et al. (2008) 已有框架的 operationalization，后者（27% convergent violations）是有价值的经验数据但概念上只是 nocuity 的一种模式。建议定位为 empirical operationalization 而非新理论框架。

**W6** [presentation] Related Work 遗漏重要并发工作：PolicyBank (2026, iterative policy refinement)、MANTRA (2026, SMT-validated compliance)、Navigli (2009, WSD survey)、Dalpiaz et al. (2018, ambiguity-incompleteness co-occurrence)、Sehwag et al. (2026, ASPI clarification→injection vulnerability)。其中 PolicyBank 和 MANTRA 是 policy specification 直接并发工作，遗漏构成 significant gap。

**W7** [presentation] Abstract "7 models" vs 正文 "5 primary + 2 replication" 不一致。Replication 模型仅参与 C1，称 "7 models" 是 overclaiming breadth。

**W8** [idea] Contribution 2（model×type interaction, 52pp auth scope range）的 measurement quality（κ=0.385, cross-judge confound）不足以支撑 star-finding 定位。§5.4 "suggestive rather than definitive" 的 caveat 与 Contribution list 的定位矛盾。

---

### 维度打分

| 维度 | 分数 | 理由 |
|------|------|------|
| Soundness | 3/5 | 因果设计严谨，但单一 benchmark + SOPBench 失败严重限制 external validity |
| Excitement | 2.5/5 | 方法论模板有价值，但 Ambiguity Blindness 非新现象，7-model breadth 非独立贡献，domain scope 窄 |
| Reproducibility | 3.5/5 | 方法描述清晰，ICC=0.919，但数据/代码未发布 |

### 总体判断

方法论贡献（C1）solid，error analysis（§6）有 genuine insight。但三个问题拉低评分：(1) C3 (7-model breadth) 不成立；(2) SOPBench 负面结果处理不透明；(3) title overclaims。当前 scope 和 novelty increment 更适合 Findings（3.0）而非 Main。如果 title 调整、SOPBench 透明报告、contributions 聚焦为 2 个（methodology + type-specific failure mechanisms），可能升至 3.0–3.5。当前评 **2.5 (Borderline Findings)**。

### 与实际论文的对比
相比已审的实际论文（3.5 Borderline Conference），Dream worst 版本主要损失在：(1) SOPBench 失败暴露了 external validity 问题而实际论文未有此问题；(2) 6 页篇幅远不足以充分展开分析；(3) Related Work 覆盖不完整；(4) 贡献重新定位后 C3 (breadth) 不如实际论文的原始 framing 有力。核心方法论和 τ²-bench 内部结果保持一致，但 framing 和 scope 的削弱使评分从 3.5 降至 2.5。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1082 · 2026-05-22T12:14:14.782426+00:00_

这是 Dream Review（worst-tier scenario 模拟审稿），不属于当前 Round 12 的正式审稿流程。Round 12 的审稿报告已在此前合成并提交给 Research Director（3.5 Borderline Conference）。

Dream Review 的结果不纳入正式审稿报告，也不修改已提交的 Issue Tracker。如果 Research Director 需要将 Dream Review 的发现（如 SOPBench 失败处理、页面空间利用等）作为后续修改参考，应由 Research Director 在收到报告后自行决定。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 105

## Round 105

2 recorded events


### User

_source line 1083 · 2026-05-22T12:14:18.061037+00:00_

[Reviewer 2 审稿结果]:
Dream 审稿完成。

**摘要**：Dream worst 版本评 2.5 (Borderline Findings)，较实际论文（3.5）降 1.0 分。主要失分点：SOPBench 跨域失败暴露 external validity 问题且报告不透明（埋在 Limitations）、title "Causal Anatomy" overclaims、7-model breadth 不构成独立贡献、Related Work 遗漏 PolicyBank/MANTRA 等并发工作。方法论模板（C1）和 error analysis（§6）仍为 solid contributions，但不足以单独支撑 Main conference 接收。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1084 · 2026-05-22T12:14:47.572636+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 106

## Round 106

82 recorded events


### User

_source line 1085 · 2026-05-22T13:20:08.110288+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: policy_ambiguity_safety
- 论文路径: projects/policy_ambiguity_safety/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 截止日期: 2026-06-15
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 1086 · 2026-05-22T13:20:13.418241+00:00_

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
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 1087 · 2026-05-22T13:20:13.469271+00:00_

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
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1088 · 2026-05-22T13:20:23.374112+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,dispatch_visual_check,request_external_review,get_external_review_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,get_visual_check_status,WebSearch,WebFetch,TodoWrite",
  "max_results": "12"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,read_project_file,dispatch_visual_check,request_external_review,get_external_review_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,get_visual_check_status,WebSearch,WebFetch,TodoWrite",
    "max_results": "12"
  }
}
```

</details>

---


### Tool result

_source line 1089 · 2026-05-22T13:20:23.424742+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1090 · 2026-05-22T13:20:31.656074+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'in_progress', 'activeForm': '检查论文资料完整性并调研 EMNLP 2026 venue 要求'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'pending', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.6/0.7: 派发外部审稿 + 视觉审查', 'status': 'pending', 'activeForm': '派发外部审稿和视觉审查'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'pending', 'activeForm': '收集 Reviewer 独立审稿结果'}, {'content': 'Step 2: 交叉分享', 'status': 'pending', 'activeForm': 'Reviewer 交叉分享与回应'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断审稿意见收敛性'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'pending', 'activeForm': '汇总审稿报告并投递'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'in_progress', 'activeForm': '检查论文资料完整性并调研 EMNLP 2026 venue 要求'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'pending', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.6/0.7: 派发外部审稿 + 视觉审查', 'status': 'pending', 'activeForm': '派发外部审稿和视觉审查'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'pending', 'activeForm': '收集 Reviewer 独立审稿结果'}, {'content': 'Step 2: 交叉分享', 'status': 'pending', 'activeForm': 'Reviewer 交叉分享与回应'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断审稿意见收敛性'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'pending', 'activeForm': '汇总审稿报告并投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 1091 · 2026-05-22T13:20:31.707145+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "TodoWrite",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1092 · 2026-05-22T13:20:33.767969+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:read_local_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:read_local_file",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 1093 · 2026-05-22T13:20:33.818612+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1094 · 2026-05-22T13:20:43.856347+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__read_project_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__read_project_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 1095 · 2026-05-22T13:20:43.907037+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1096 · 2026-05-22T13:20:49.480321+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "policy_ambiguity_safety"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "policy_ambiguity_safety"
  }
}
```

</details>

---


### Tool result

_source line 1097 · 2026-05-22T13:20:50.936150+00:00_

{"result":"# 项目 policy_ambiguity_safety 概况\n\n## 实验状态 (17 个)\n\n- **plan_014**: DONE (success) — \n- **plan_015**: DONE (success) — \n- **plan_013**: DONE (success) — \n- **plan_012**: DONE (success) — \n- **plan_011**: DONE (success) — \n- **plan_010**: DONE (success) — \n- **plan_004**: DONE (success) — \n- **plan_003b**: DONE (success) — \n- **plan_003a**: DONE (success) — \n- **plan_002c**: DONE (success) — \n- **plan_006**: DONE (success) — \n- **plan_005**: DONE (success) — \n- **plan_002**: DONE (negative) — \n- **diag_001**: DONE (negative) — \n- **mvp_001**: DONE (negative) — \n\n## 最新报告\n# Handover — 2026-05-22\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n（无）\n\n## 近期结论\n- **plan_016** (negative): Type-specific mitigation prompts reduce violations more effectively than generic awareness prompts for their targeted ambiguity types, supporting the practical contribution that type-aware triage is necessary for policy-governed deployments\n- **plan_009** (success): Cross-judge LLM agreement (gpt-5.4 vs gpt-4.1) achieves substantial agreement (weighted κ ≥ 0.60) on violation level classification. LLM-human agreement should be comparable, validating the cross-judge evaluation design.\n  [plan_009_annotation_guidelines](/api/workspace-files/projects/policy_ambiguity_safety/artifacts/plan_009/report/annotation_guidelines.md) | [plan_009_annotation_sheet](/api/workspace-files/projects/policy_ambiguity_safety/artifacts/plan_009/data/annotation_sheet.jsonl) | [plan_009_llm_agreement](/api/workspace-files/projects/policy_ambiguity_safety/artifacts/plan_009/report/llm_agreement.json) | [plan_009_annotation_sheet_clean](/api/workspace-files/projects/policy_ambiguity_safety/artifacts/plan_009/data/annotation_sheet_clean.jsonl)\n- **plan_014** (success): Expanding perturbation control from n=120 to n=300 will maintain non-significant Δ_perturb (CI containing zero) while narrowing CI upper bound from 13.3pp to ~8pp, strengthening SESOI justification for C
…[truncated 563 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1455
}
```

</details>

---


### Tool call

_source line 1098 · 2026-05-22T13:20:51.439349+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.tex 2>/dev/null && echo \"PAPER_EXISTS\" || echo \"PAPER_MISSING\"",
  "description": "Check if paper main.tex exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.tex 2>/dev/null && echo \"PAPER_EXISTS\" || echo \"PAPER_MISSING\"",
    "description": "Check if paper main.tex exists"
  }
}
```

</details>

---


### Tool result

_source line 1099 · 2026-05-22T13:20:52.443873+00:00_

-rw-r--r-- 1 ubuntu ubuntu 893 May 21 07:29 /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.tex
PAPER_EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Bash",
  "elapsed_ms": 1004
}
```

</details>

---


### Tool call

_source line 1100 · 2026-05-22T13:20:52.896356+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_13/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"PDF_MISSING\"",
  "description": "Check if submitted PDF exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_13/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"PDF_MISSING\"",
    "description": "Check if submitted PDF exists"
  }
}
```

</details>

---


### Tool result

_source line 1101 · 2026-05-22T13:20:53.198096+00:00_

-rw-r--r-- 1 ubuntu ubuntu 421817 May 22 10:32 /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_13/submitted.pdf
PDF_EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Bash",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 1102 · 2026-05-22T13:20:53.198597+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers ARR submission guidelines site:aclweb.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers ARR submission guidelines site:aclweb.org"
  }
}
```

</details>

---


### Tool result

_source line 1103 · 2026-05-22T13:20:58.684082+00:00_

Web search results for query: "EMNLP 2026 call for papers ARR submission guidelines site:aclweb.org"

Links: [{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"The 64th Annual Meeting of the Association for Computational Linguistics - ACL 2026","url":"https://2026.aclweb.org/"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"Jan. 2025 ACL Standing Committee on Peer Review (COPR) Report 1","url":"https://www.aclweb.org/adminwiki/images/9/9e/COPR-5-cycle-report-to-publish.pdf"},{"title":"EMNLP 2025: Call for System Demonstrations | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-call-system-demonstrations"}]

I found some information about EMNLP 2026, but the search results don't contain a main cal
…[truncated 1294 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "WebSearch",
  "elapsed_ms": 5485
}
```

</details>

---


### Tool call

_source line 1104 · 2026-05-22T13:21:05.567036+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 Budapest call for papers ARR commitment deadline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 Budapest call for papers ARR commitment deadline"
  }
}
```

</details>

---


### Tool call

_source line 1105 · 2026-05-22T13:21:05.868992+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 submission guidelines page limit author instructions"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 submission guidelines page limit author instructions"
  }
}
```

</details>

---


### Tool result

_source line 1106 · 2026-05-22T13:21:11.491566+00:00_

Web search results for query: "EMNLP 2026 Budapest call for papers ARR commitment deadline"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"EMNLP 2026 Call for Papers — Official Deadlines & Important Dates | PaperPilot","url":"https://www.getpaperpilot.com/deadlines/emnlp-2026.html"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"},{"title":"LINGUIST List 37.1616 Confs: Workshop at EMNLP 2026: Multimodal Interaction in Face-to-Face Dialogue (Hungary)","url":"https://linguistlist.org/issues/37/1616/"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"}]

Based on the search results, here is the key information about EMNLP 2026 Budapest call for papers and ARR commitment deadline:

## Key Deadlines:

The ARR submission deadline for long & short papers is May 25, 2026, and the EMNLP commitment deadline is August 2, 2026.
…[truncated 790 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "WebSearch",
  "elapsed_ms": 5924
}
```

</details>

---


### Tool result

_source line 1107 · 2026-05-22T13:21:13.501433+00:00_

Web search results for query: "ACL Rolling Review 2026 submission guidelines page limit author instructions"

Links: [{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Author Guidelines for Student Research Workshop Papers -","url":"https://2026.eacl.org/calls/srw/guidelines/"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Paper formatting guidelines - ACLPUB","url":"https://acl-org.github.io/ACLPUB/formatting.html"},{"title":"Instructions for *ACL Proceedings","url":"https://arxiv.org/html/2506.06751v2"},{"title":"Submission Form Fields – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/submissionform"}]

Based on the web search results, here's information about ACL Rolling Review 2026 submission guidelines:

## Page Limit

Review versions of long papers may have up to eight (8) pages of content plus unlimited pages for references. The "Limitations" section (along with, optionally, a section for ethical considerations) may be up to one page and will not count toward the final page limit.

## Key Author Instructions

**Fo
…[truncated 1137 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "WebSearch",
  "elapsed_ms": 7632
}
```

</details>

---


### Tool call

_source line 1108 · 2026-05-22T13:21:24.721028+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://2026.emnlp.org/calls/main_conference_papers/",
  "prompt": "Extract all submission guidelines: page limits, formatting requirements, anonymity rules, appendix rules, ARR deadlines, commitment deadlines, review criteria, and any other author instructions. Be comprehensive."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://2026.emnlp.org/calls/main_conference_papers/",
    "prompt": "Extract all submission guidelines: page limits, formatting requirements, anonymity rules, appendix rules, ARR deadlines, commitment deadlines, review criteria, and any other author instructions. Be comprehensive."
  }
}
```

</details>

---


### Tool call

_source line 1109 · 2026-05-22T13:21:26.328323+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "http://aclrollingreview.org/cfp",
  "prompt": "Extract all submission guidelines: page limits for long and short papers, formatting requirements, anonymity rules, appendix rules, Limitations section rules, ethical considerations, citation format, template requirements, and key deadlines for 2026 cycles. Be comprehensive."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "WebFetch",
  "tool_args": {
    "url": "http://aclrollingreview.org/cfp",
    "prompt": "Extract all submission guidelines: page limits for long and short papers, formatting requirements, anonymity rules, appendix rules, Limitations section rules, ethical considerations, citation format, template requirements, and key deadlines for 2026 cycles. Be comprehensive."
  }
}
```

</details>

---


### Tool result

_source line 1110 · 2026-05-22T13:21:31.298704+00:00_

# EMNLP 2026 Submission Guidelines

## Page Limits
- **Long papers:** 8 pages (final versions: up to 9 pages for addressing reviewer comments)
- **Short papers:** 4 pages (final versions: up to 5 pages for addressing reviewer comments)

## Formatting & Submission Requirements
All submissions must adhere to "ARR submission requirements" including proper templates, two-way anonymized review instructions, and citation guidelines. Consult the ARR CFP for specific formatting details.

## Anonymity Rules
- "The reviewing process will continue to be double-blind"
- Reviewers cannot see author identities; authors cannot access reviewer identities
- "Following the ACL and ARR policies, there is no anonymity period requirement"
- Authors may optionally make anonymized articles publicly visible through ARR

## Authorship During Review
During the commitment phase, adding or removing authors is prohibited, though reordering authors remains permissible.

## Appendices & Supplementary Materials
Optional supplementary materials, appendices, software, and data are permitted per ARR guidelines.

## ARR Submission Deadline
- May 25, 2026 (11:59 PM UTC-12:00, "anywhere on Earth")

## Key Review Deadlines
- Reviewer registration: May 27, 2026
- Author-reviewer discussion: July 7-13, 2026
- Meta-review release: July 30, 2026
- EMNLP commitment deadline: August 2, 2026
- Acceptance notification: August 20, 2026
- Camera-ready due: September 20, 2026

## Mandatory Reviewing Obligations
All authors must register and accept review assignments, with reviews due by July 6 and meta-reviews by July 29. Non-compliance may result in ineligibility for future submissions.

## Paper Integrity Policies
Submissions with hallucinated citations, entirely AI-generated content, thinly sliced contributions, or ethics violations face desk rejection and potential author ineligibility for EMNLP 2026-2027.

## Presentation Requirements
"All accepted papers must be presented at the conference to appear in the pr
…[truncated 115 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "WebFetch",
  "elapsed_ms": 6577
}
```

</details>

---


### Tool result

_source line 1111 · 2026-05-22T13:21:36.924423+00:00_

# ACL Rolling Review Submission Guidelines Summary

## Page Limits

**Long Papers:**
- Up to 8 pages of content
- Unlimited space after conclusion for limitations (required) and ethical considerations (optional)
- Unlimited reference pages

**Short Papers:**
- Up to 4 pages of content
- Unlimited space after conclusion for limitations (required) and ethical considerations (optional)
- Unlimited reference pages

*Papers exceeding length requirements or lacking a limitations section face desk rejection.*

## Formatting Requirements

Submissions must follow the official ACL style template available on GitHub. The guidelines specify adherence to "*ACL" conference formatting standards regarding "paper size, margin width, and font size restrictions." Non-compliant submissions are rejected without review.

Appendices must follow double-column format with limited exceptions, effective July 2025. Text should address human readers exclusively, avoiding prompt injections or machine-manipulation attempts.

## Anonymity Rules (Two-Way Anonymized Review)

Papers must exclude author names and affiliations. Self-references revealing identity are prohibited—for example, use "Smith previously showed" rather than "We previously showed." Papers cannot reference materials unavailable to reviewers. Supplementary materials and repository links must be anonymized. Dropbox and similar tracking services are explicitly forbidden.

## Limitations Section Requirements

A dedicated "Limitations" section is mandatory, placed before references without counting toward page limits. This section should discuss only the work's constraints, not introduce new methods, analysis, or results. Submissions lacking this section receive automatic desk rejection.

## Ethical Considerations

Authors should include an optional "Ethical considerations" section addressing potential ethical impacts and broader implications. The responsible NLP checklist is required during submission. Incorrect or misleading checklis
…[truncated 1776 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "WebFetch",
  "elapsed_ms": 10596
}
```

</details>

---


### Tool call

_source line 1112 · 2026-05-22T13:21:47.965515+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "policy_ambiguity_safety",
  "file": "config",
  "max_chars": "5000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "policy_ambiguity_safety",
    "file": "config",
    "max_chars": "5000"
  }
}
```

</details>

---


### Tool result

_source line 1113 · 2026-05-22T13:21:49.270740+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'mistakes.yaml', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'config'\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 1305
}
```

</details>

---


### Tool call

_source line 1114 · 2026-05-22T13:21:49.271065+00:00_

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
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 1115 · 2026-05-22T13:21:49.321565+00:00_

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
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1116 · 2026-05-22T13:21:54.699313+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety -name \"*.yaml\" -path \"*/agent/*\" 2>/dev/null | head -5",
  "description": "Find project config files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety -name \"*.yaml\" -path \"*/agent/*\" 2>/dev/null | head -5",
    "description": "Find project config files"
  }
}
```

</details>

---


### Tool result

_source line 1117 · 2026-05-22T13:21:55.151289+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Bash",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 1118 · 2026-05-22T13:21:55.202014+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/policy_ambiguity_safety/docs/paper/sections/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/policy_ambiguity_safety/docs/paper/sections/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects"
  }
}
```

</details>

---


### Tool result

_source line 1119 · 2026-05-22T13:21:55.303400+00:00_

/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/taxonomy.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/analysis.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/method.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/limitations.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/experiments.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/discussion.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/appendix.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Glob",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1120 · 2026-05-22T13:21:59.921316+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4 -name \"project_config*\" -o -name \"config.yaml\" -o -name \"config.yml\" 2>/dev/null | grep -i policy 2>/dev/null; find /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4 -path \"*/policy_ambiguity_safety*config*\" 2>/dev/null | head -10",
  "description": "Find project config for external review settings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4 -name \"project_config*\" -o -name \"config.yaml\" -o -name \"config.yml\" 2>/dev/null | grep -i policy 2>/dev/null; find /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4 -path \"*/policy_ambiguity_safety*config*\" 2>/dev/null | head -10",
    "description": "Find project config for external review settings"
  }
}
```

</details>

---


### Tool result

_source line 1121 · 2026-05-22T13:22:00.173001+00:00_

/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.venv/lib/python3.14/site-packages/configs/config.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.git/config
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.venv/bin/numpy-config
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.venv/lib/python3.14/site-packages/openai/types/realtime/realtime_tool_choice_config.py
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.venv/lib/python3.14/site-packages/openai/types/realtime/realtime_audio_config_input.py
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.venv/lib/python3.14/site-packages/openai/types/realtime/realtime_tools_config_union_param.py
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.venv/lib/python3.14/site-packages/openai/types/realtime/__pycache__/realtime_tracing_config.cpython-314.pyc
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.venv/lib/python3.14/site-packages/openai/types/realtime/__pycache__/realtime_tracing_config_param.cpython-314.pyc
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.venv/lib/python3.14/site-packages/openai/types/realtime/__pycache__/realtime_tools_config_union.cpython-314.pyc
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.venv/lib/python3.14/site-packages/openai/types/realtime/__pycache__/realtime_audio_config_param.cpython-314.pyc
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.venv/lib/python3.14/site-packages/openai/types/realtime/__pycache__/realtime_tool_choice_config_param.cpython-314.pyc

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Bash",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 1122 · 2026-05-22T13:22:06.499760+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4 -maxdepth 2 -name \"*.yaml\" -o -name \"*.yml\" 2>/dev/null | grep -v \".venv\" | grep -v node_modules | head -20",
  "description": "Find top-level config files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4 -maxdepth 2 -name \"*.yaml\" -o -name \"*.yml\" 2>/dev/null | grep -v \".venv\" | grep -v node_modules | head -20",
    "description": "Find top-level config files"
  }
}
```

</details>

---


### Tool result

_source line 1123 · 2026-05-22T13:22:06.600448+00:00_

/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/idea_generator/ideas.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/global/approvals.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/config/approvals.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/config/backend.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/config/feishu.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/config/venue_registry.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/config/resources.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/workspace.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1124 · 2026-05-22T13:22:09.662028+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/config/ 2>/dev/null; grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/workspace.yaml 2>/dev/null",
  "description": "Check external review config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/config/ 2>/dev/null; grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/workspace.yaml 2>/dev/null",
    "description": "Check external review config"
  }
}
```

</details>

---


### Tool result

_source line 1125 · 2026-05-22T13:22:09.712582+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1126 · 2026-05-22T13:22:13.829355+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/workspace.yaml",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/workspace.yaml",
    "limit": "50"
  }
}
```

</details>

---


### Tool result

_source line 1127 · 2026-05-22T13:22:13.930172+00:00_

1	projects: {}
2	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1128 · 2026-05-22T13:22:19.768365+00:00_

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
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 1129 · 2026-05-22T13:22:20.223555+00:00_

1	\begin{abstract}
2	LLM-based agents operate under natural-language policy specifications that inevitably contain ambiguity, yet the causal relationship between ambiguity type and safety violations remains unmeasured. We present a matched-pair study on $\tau^2$-bench with 300 clause pairs spanning a six-type ambiguity taxonomy, evaluated across five models (2,997 episodes). Three findings emerge. First, ambiguous clauses increase violation rates by 34.0 percentage points (OR $= 15.1$), with a perturbation control supporting ambiguity-specific causation. Second, effects range from $+$18.7\,pp (coreferential, confound-free) to $+$49.2\,pp (incompleteness, upper bound reflecting an information-addition confound); the remaining five types form a risk gradient rather than sharp tiers, with rankings partly margin-dependent. Third, error analysis of 614 violation traces reveals \emph{Disambiguation Neglect} ($\leq$11\% per-model awareness, 4.6\% overall) and \emph{systematic nocuity}---41.3\% of clauses triggering model-convergent violations---indicating clause-level rather than model-level risk factors. These results---observed in customer-service policy domains---motivate type-aware policy auditing and externalized ambiguity detection for policy-governed agent deployments.
3	\end{abstract}
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 455
}
```

</details>

---


### Tool call

_source line 1130 · 2026-05-22T13:22:20.223976+00:00_

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
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 1131 · 2026-05-22T13:22:20.693478+00:00_

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
…[truncated 2187 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 469
}
```

</details>

---


### Tool call

_source line 1132 · 2026-05-22T13:22:20.693921+00:00_

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
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 1133 · 2026-05-22T13:22:21.647385+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Ambiguity in NLP and requirements engineering.}
5	Ambiguity has been studied extensively in both computational linguistics and software engineering. Word sense disambiguation \citep{navigli_wsd_2009} addresses lexical ambiguity at the token level; our lexical type extends this to policy-specific polysemy. \citet{li_ambiguity_taxonomy_2024} propose an 11-type NLP taxonomy covering syntactic, semantic, and pragmatic ambiguity, from which we draw our linguistic-layer types. In requirements engineering (RE), \citet{massey_ambiguity_re_2014} classify six ambiguity types in regulatory texts, and \citet{berry_kamsties_2004} introduce the distinction between nocuous ambiguity (where stakeholders diverge on interpretation) and innocuous ambiguity (where they converge). Computational detection of nocuous ambiguity has progressed from heuristic methods \citep{chantree_2006,willis_nocuous_2008} through NLP-based cross-domain detectors \citep{ferrari_ambiguity_2019,ferrari_defects_2018} to transformer-based approaches for anaphoric ambiguity \citep{ezzini_taphsir_2022,ezzini_anaphoric_2022}. \citet{zhao_nlp4re_2021} survey the broader NLP4RE landscape. Our work extends Berry and Kamsties' framework to LLM agents, where the absence of shared organizational context makes previously innocuous ambiguity nocuous.
6	
7	\paragraph{Psycholinguistics of ambiguity processing.}
8	\citet{ferreira_good_enough_2002} show that human comprehenders build shallow, ``good-enough'' representations rather than full parses, paralleling our observation that LLM agents adopt surface interpretations. \citet{frazier_rayner_1982} demonstrate early commitment to a single parse; \citet{li_garden_path_llm_2024} provide direct evidence that LLMs exhibit analogous garden-path effects. \citet{liu_ambiguity_2023} demonstrate that language models fail to represent ambiguity, collapsing multiple interpretations into a single output. These findings
…[truncated 2470 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 953
}
```

</details>

---


### Tool call

_source line 1134 · 2026-05-22T13:22:21.647955+00:00_

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
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/taxonomy.tex"
  }
}
```

</details>

---


### Tool result

_source line 1135 · 2026-05-22T13:22:22.150715+00:00_

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
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1136 · 2026-05-22T13:22:22.151123+00:00_

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
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 1137 · 2026-05-22T13:22:22.402326+00:00_

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
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 1138 · 2026-05-22T13:22:22.402946+00:00_

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
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 1139 · 2026-05-22T13:22:22.503789+00:00_

1	\section{Results}
2	\label{sec:results}
3	
4	We organize results around four analyses of increasing specificity: the binary ambiguity effect (C1), the type risk gradient (C2), the aggregate layer effect (C3), and the model$\times$type interaction (C4). C1 and C2 constitute our primary claims; C3 is inconclusive; C4 is exploratory but provides the model$\times$type interaction analysis.
5	
6	\subsection{Binary Ambiguity Effect (C1)}
7	
8	Across all five models and six types, ambiguous clauses increase violation rates by 34.0 pp (41.0\% vs.\ 6.9\%, OR $= 15.1$, 95\% CI $[10.78, 21.17]$, $p < 10^{-105}$). All six types individually produce significant increases (all $p < 10^{-5}$), and all five models show large effects ($+25.7$ to $+39.0$ pp, all $p < 10^{-17}$). Perturbation controls confirm specificity to semantic ambiguity ($n = 300$, $\Delta_{\text{perturb}} = -0.67$\,pp, CI containing zero). Clause identity explains 22.4\% of variance versus 1.0\% for model identity. This decomposes into 0.4\% between types and 22.0\% within types, indicating that individual clause wording---not type membership---drives the bulk of clause-level variance. The remaining 60.8\% reflects scenario-level variation, judge variability, and unmeasured clause features. A replication on two additional model families (Appendix~\ref{app:model_expansion}) confirms the effect across seven models ($\Delta = +20.0$ to $+33.6$\,pp, both $p < 10^{-6}$); excluding incompleteness, it remains large ($\Delta = 31.0$\,pp; Appendix~\ref{app:sans_incompleteness}).
9	
10	\subsection{Type Risk Gradient (C2)}
11	
12	\begin{table*}[t]
13	\centering
14	\caption{Violation rates (\%) under ambiguous policy clauses by type and model (5.4 = GPT-5.4, 4.1 = GPT-4.1, Cla.\ = Claude, Qw3 = Qwen3, DS = DeepSeek). $\Delta$pp: pooled difference (ambiguous $-$ unambiguous) with Newcombe 95\% CIs. Tier: TOST equivalence cluster at $\pm 15$\,pp---U = upper bound (separated at all margins), M = mid-tier (6/6 pairwise equiv
…[truncated 6824 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1140 · 2026-05-22T13:22:32.398329+00:00_

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
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/analysis.tex"
  }
}
```

</details>

---


### Tool result

_source line 1141 · 2026-05-22T13:22:32.398908+00:00_

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
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1142 · 2026-05-22T13:22:38.021424+00:00_

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
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1143 · 2026-05-22T13:22:38.122283+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Differential nocuity.}
5	Building on \citet{berry_kamsties_2004}'s nocuous/innocuous distinction, our results are consistent with a \emph{differential nocuity} hypothesis \citep{willis_nocuous_2008}: risk depends on ambiguity type (base vulnerability), safety training (selective mitigation), and disambiguation channel availability. Types with explicit decision points (e.g., authorization scope) appear more amenable to both safety training and prompted intervention than gap-filling types (e.g., incompleteness), where mitigation attempts can backfire (see below).
6	
7	\paragraph{Prompt-based mitigation.}
8	Building on the five-model type-specific mitigation study ($-$8.5\,pp pooled, unpaired design; Appendix~\ref{app:mitigation}), we test whether disambiguation can be prompted at finer granularity using a matched-pair design. We evaluate generic awareness prompting (``the policy may contain ambiguous clauses; ask for clarification'') and type-specific prompting (targeting incompleteness, authorization scope, and lexical ambiguity individually) on GPT-5.4 with matched-pair McNemar tests ($n = 50$ per type). Generic prompting produces no overall reduction ($\Delta = +1.3$\,pp, $p > 0.5$). Type-specific results are asymmetric: authorization scope shows a marginal reduction ($-12$\,pp, $p = 0.070$), lexical ambiguity is unchanged ($-2$\,pp), and incompleteness \emph{worsens} ($+14$\,pp, $p = 0.118$; non-significant trend)---suggesting that prompting agents to attend to missing information may trigger confabulation rather than caution. The five-model study in Appendix~\ref{app:mitigation} uses a different prompt formulation and unpaired design, yielding directionally different results; mitigation outcomes appear sensitive to prompt wording and experimental design. That identical types show opposite directions under different prompt formulations (e.g., incompleteness: $-$3.4\,pp in v1 vs.\ $+$14\,pp in v2) unde
…[truncated 556 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1144 · 2026-05-22T13:22:39.326024+00:00_

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
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1145 · 2026-05-22T13:22:39.376573+00:00_

1	\section{Conclusion}
2	
3	Ambiguous policy clauses increase agent safety violations by 34.0\,pp (OR\,$=$\,15.1); clause-level wording drives 22.4\% of variance versus 0.4\% for type and 1.0\% for model (60.8\% residual). Effects range from $+$18.7\,pp (coreferential, confound-free) to $+$49.2\,pp (incompleteness, upper bound), forming a margin-dependent gradient across seven models. With disambiguation neglect in $>$89\% of cases and 41.3\% model-convergent violations, type-aware auditing and externalized detection are critical for customer-service deployments.
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1146 · 2026-05-22T13:22:39.528191+00:00_

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
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 1147 · 2026-05-22T13:22:39.528549+00:00_

1	\section*{Limitations}
2	\label{sec:limitations}
3	
4	\paragraph{Scope.} We evaluate seven API-accessible models from six providers (Appendix~\ref{app:model_expansion}); smaller open-source models (7B--70B) may exhibit different vulnerability patterns. $\tau^2$-bench covers retail and airline customer service only---effects in other domains remain untested, though within-study cross-domain consistency is encouraging. Our matched-pair design requires synthetic ambiguity construction, which may not capture the full distribution of naturally occurring ambiguities; realism validation (\S\ref{sec:method}) confirms lexical comparability but cannot rule out distributional gaps. Coreferential ambiguity was excluded from mitigation and replication experiments due to benchmark-specific structural constraints (Appendix~\ref{app:mitigation}).
5	
6	\paragraph{Measurement.} Each model is evaluated by a single cross-judge, confounding judge identity with model identity; within-judge-group analyses confirm C1 individually (both $p < 0.001$) but not C3 (Appendix~\ref{app:judge_group_ranking}), and cross-model type ranking concordance is only moderate (Appendix~\ref{app:kendall_w}). Per-type reliability varies---authorization scope has the lowest agreement ($\kappa = 0.385$) and per-type human--LLM estimates rest on small cell sizes with wide confidence intervals (Appendix~\ref{app:per_type_agreement})---while failure mode coding achieves moderate agreement ($\kappa = 0.52$), with minority categories less reliable. Both judges belong to the OpenAI model family, so systematic leniency toward same-family outputs or severity toward competitors cannot be ruled out; cross-family judge evaluation (e.g., Claude judging GPT traces) would strengthen C4 conclusions.
7	
8	\paragraph{Confounds.} Incompleteness resolution necessarily adds policy content, creating an information asymmetry; our logistic regression controls and coreferential lower-bound analysis mitigate but do not eliminate this 
…[truncated 456 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1148 · 2026-05-22T13:22:39.930012+00:00_

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
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 1149 · 2026-05-22T13:22:40.131565+00:00_

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
…[truncated 20812 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 1150 · 2026-05-22T13:22:48.311369+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "wc -l /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/*.tex",
  "description": "Count lines per section to estimate page usage"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Bash",
  "tool_args": {
    "command": "wc -l /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/*.tex",
    "description": "Count lines per section to estimate page usage"
  }
}
```

</details>

---


### Tool result

_source line 1151 · 2026-05-22T13:22:50.117976+00:00_

    3 /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/abstract.tex
   28 /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/analysis.tex
  287 /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/appendix.tex
    3 /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/conclusion.tex
   11 /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/discussion.tex
   66 /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/experiments.tex
   21 /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/introduction.tex
   11 /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/limitations.tex
   34 /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/method.tex
   13 /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/related_work.tex
   41 /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/taxonomy.tex
  518 total

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Bash",
  "elapsed_ms": 1806
}
```

</details>

---


### Tool call

_source line 1152 · 2026-05-22T13:22:50.369308+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_issues.yaml 2>/dev/null && cat /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_issues.yaml 2>/dev/null || echo \"NO_ISSUES_FILE\"",
  "description": "Check existing review issues tracker"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_issues.yaml 2>/dev/null && cat /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_issues.yaml 2>/dev/null || echo \"NO_ISSUES_FILE\"",
    "description": "Check existing review issues tracker"
  }
}
```

</details>

---


### Tool result

_source line 1153 · 2026-05-22T13:22:50.721636+00:00_

/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_issues.yaml
## Review Issues Tracker — policy_ambiguity_safety
## Paper: "Not All Policy Ambiguity Is Equal: Type-Specific Safety Risks for LLM Agents"
## Venue: EMNLP 2026 via ARR May cycle
## Latest Round: 13 (in progress, targeting 4.0 Conference)
## Upgrade path: fix 4 MF claim calibrations + 8 SF framing adjustments → 4.0

# ============================================================
# CRITICAL ISSUES
# ============================================================

- id: "R11-C1"
  summary: "22× variance claim 误导性 — taxonomy 仅解释 0.4% between-type variance, 22× 是 clause vs model"
  category: method
  severity: critical
  status: in_progress
  first_raised_round: 11
  last_seen_round: 12
  mentions:
    - round: 11
      reviewers: [R2, R1]
      note: "W6. clause_within_type=22.0% vs ambiguity_type=0.4%. Introduction contribution (2) '22× type identity' 是 clause identity 不是 type identity。"
    - round: 12
      reviewers: [R2, R1]
      note: "MF-1. 两位 Reviewer 共识: 22× 放在 contributions list 紧跟 C2, 读者误读为 taxonomy 解释力。加上 76.6% unexplained variance, 将 22× 作为 headline contribution 不合理。需区分 clause-level vs type-level, 降级为 supporting evidence。"
  action_items:
    - round: 11
      action: "Intro contribution(2) 改为 clause identity"
      assigned_to: agent
      status: resolved
    - round: 12
      action: "(1) Contributions 区分 clause-level vs type-level variance; (2) §5.1 讨论 0.4% 对 taxonomy 实用价值含义; (3) 22× 从 headline contribution 降级为 supporting evidence; (4) 报告 76.6% residual"
      assigned_to: agent
      status: in_progress
  resolution: ""
  resolution_round: null

- id: "R10-C1"
  summary: "Authorization scope κ=0.385 + cross-judge asymmetry 威胁 C4 结论"
  category: method
  severity: critical
  status: in_progress
  first_raised_round: 8
  last_seen_round: 12
  mentions:
    - round: 10
      reviewers: [R1, R2]
      note: "R1 MUST-FIX. κ=0.385 < fair agreement 0
…[truncated 15159 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Bash",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 1154 · 2026-05-22T13:22:51.223995+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_reports/ 2>/dev/null || echo \"NO_REPORTS_DIR\"",
  "description": "Check existing review reports"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_reports/ 2>/dev/null || echo \"NO_REPORTS_DIR\"",
    "description": "Check existing review reports"
  }
}
```

</details>

---


### Tool result

_source line 1155 · 2026-05-22T13:22:51.676332+00:00_

round_0.md
round_1.md
round_10.md
round_11.md
round_12.md
round_2.md
round_3.md
round_5.md
round_6.md
round_7.md
round_8.md
round_9.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Bash",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1156 · 2026-05-22T13:22:51.927805+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/appendix.tex",
  "offset": "288"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/appendix.tex",
    "offset": "288"
  }
}
```

</details>

---


### Tool result

_source line 1157 · 2026-05-22T13:22:52.028584+00:00_

&lt;system-reminder>Warning: the file exists but is shorter than the provided offset (288). The file has 288 lines.&lt;/system-reminder>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1158 · 2026-05-22T13:23:25.523863+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '检查论文资料完整性并调研 EMNLP 2026 venue 要求'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.7: 派发视觉审查', 'status': 'in_progress', 'activeForm': '派发视觉审查 Agent'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'in_progress', 'activeForm': '收集 Reviewer 独立审稿结果'}, {'content': 'Step 2: 交叉分享', 'status': 'pending', 'activeForm': 'Reviewer 交叉分享与回应'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断审稿意见收敛性'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'pending', 'activeForm': '汇总审稿报告并投递'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '检查论文资料完整性并调研 EMNLP 2026 venue 要求'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.7: 派发视觉审查', 'status': 'in_progress', 'activeForm': '派发视觉审查 Agent'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'in_progress', 'activeForm': '收集 Reviewer 独立审稿结果'}, {'content': 'Step 2: 交叉分享', 'status': 'pending', 'activeForm': 'Reviewer 交叉分享与回应'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断审稿意见收敛性'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'pending', 'activeForm': '汇总审稿报告并投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 1159 · 2026-05-22T13:23:25.624711+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "TodoWrite",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1160 · 2026-05-22T13:23:32.902105+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "policy_ambiguity_safety",
  "review_chat_id": "oc_967344d166ba485ad606d14379e69d85"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "policy_ambiguity_safety",
    "review_chat_id": "oc_967344d166ba485ad606d14379e69d85"
  }
}
```

</details>

---


### Tool result

_source line 1161 · 2026-05-22T13:23:56.205392+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 23303
}
```

</details>

---


### Tool call

_source line 1162 · 2026-05-22T13:23:56.257324+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "policy_ambiguity_safety",
  "text": "你是 Reviewer 1，负责 **方法严谨性 + 实验设计** 审查。\n\n## 投稿信息\n- **Venue**: EMNLP 2026 via ARR May cycle\n- **Deadline**: 2026-05-25 (11:59PM AoE)\n- **格式要求**: Long paper, 8页正文上限, unlimited references, Limitations section 必须（不计入页数）, double-blind, ACL style template\n- **匿名规则**: 双盲审稿, 无匿名期要求\n- **论文路径**: `projects/policy_ambiguity_safety/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_13/submitted.pdf`\n\n## 审查侧重\n\n请重点审查以下方面：\n\n1. **实验设计 (Matched-Pair Design)**\n   - 300 clause pairs × 6 types × 5 models = 2,997 episodes 的设计是否严谨\n   - Clause pair 构建流程（template-based + annotator review）是否充分\n   - Annotator 一致性 (96% initial, 100% final) 的报告是否规范\n\n2. **统计分析**\n   - McNemar's test, χ², Fisher's exact, TOST equivalence testing 的使用是否恰当\n   - SESOI ±15pp 的论证是否充分（field-standard 缺失问题）\n   - Holm-Bonferroni 多重比较校正是否完整\n   - Variance decomposition (22.4% clause, 0.4% type, 1.0% model, 60.8% residual) 的方法和解读\n\n3. **Controls & Confounds**\n   - Perturbation control (n=300, Δ=-0.67pp) 是否足够\n   - Incompleteness information-addition confound 的控制（logistic regression, token count proxy）\n   - Cross-judge calibration design (McNemar p=0.606, κ=0.653, κ_w=0.775) 和 judge family bias (both OpenAI)\n\n4. **Evaluation Pipeline**\n   - Cross-judge design 的合理性（GPT-5.4 judges 3 models, GPT-4.1 judges 2 models）\n   - Human validation (n=100, κ=0.798, κ_w=0.762) 的充分性\n   - Per-type reliability variation (κ ranging from 0.385 to 0.875)\n\n5. **Replication & Robustness**\n   - 2-model replication (Gemini, LLaMA) 的设计\n   - ICC=0.919 reproducibility 的报告\n   - Severity threshold sensitivity (moderate+ vs any-violation)\n\n6. **Claims vs Evidence 校准**\n   - C1 (binary effect) 的证据是否支持 claim\n   - C2 (risk gradient) 的 margin-dependence 是否被充分承认\n   - C3 (layer effect, inconclusive) 的处理\n   - C4 (model×type interaction, exploratory) 是否适度\n\n请按 ARR 审稿标准，给出 Strengths、Weaknesses (分 MUST-FIX 和 SHOULD-FIX)、Questions、Overall Assessment。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "policy_ambiguity_safety",
    "text": "你是 Reviewer 1，负责 **方法严谨性 + 实验设计** 审查。\n\n## 投稿信息\n- **Venue**: EMNLP 2026 via ARR May cycle\n- **Deadline**: 2026-05-25 (11:59PM AoE)\n- **格式要求**: Long paper, 8页正文上限, unlimited references, Limitations section 必须（不计入页数）, double-blind, ACL style template\n- **匿名规则**: 双盲审稿, 无匿名期要求\n- **论文路径**: `projects/policy_ambiguity_safety/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_13/submitted.pdf`\n\n## 审查侧重\n\n请重点审查以下方面：\n\n1. **实验设计 (Matched-Pair Design)**\n   - 300 clause pairs × 6 types × 5 models = 2,997 episodes 的设计是否严谨\n   - Clause pair 构建流程（template-based + annotator review）是否充分\n   - Annotator 一致性 (96% initial, 100% final) 的报告是否规范\n\n2. **统计分析**\n   - McNemar's test, χ², Fisher's exact, TOST equivalence testing 的使用是否恰当\n   - SESOI ±15pp 的论证是否充分（field-standard 缺失问题）\n   - Holm-Bonferroni 多重比较校正是否完整\n   - Variance decomposition (22.4% clause, 0.4% type, 1.0% model, 60.8% residual) 的方法和解读\n\n3. **Controls & Confounds**\n   - Perturbation control (n=300, Δ=-0.67pp) 是否足够\n   - Incompleteness information-addition confound 的控制（logistic regression, token count proxy）\n   - Cross-judge calibration design (McNemar p=0.606, κ=0.653, κ_w=0.775) 和 judge family bias (both OpenAI)\n\n4. **Evaluation Pipeline**\n   - Cross-judge design 的合理性（GPT-5.4 judges 3 models, GPT-4.1 judges 2 models）\n   - Human validation (n=100, κ=0.798, κ_w=0.762) 的充分性\n   - Per-type reliability variation (κ ranging from 0.385 to 0.875)\n\n5. **Replication & Robustness**\n   - 2-model replication (Gemini, LLaMA) 的设计\n   - ICC=0.919 reproducibility 的报告\n   - Severity threshold sensitivity (moderate+ vs any-violation)\n\n6. **Claims vs Evidence 校准**\n   - C1 (binary effect) 的证据是否支持 claim\n   - C2 (risk gradient) 的 margin-dependence 是否被充分承认\n   - C3 (layer effect, inconclusive) 的处理\n   - C4 (model×type interaction, exploratory) 是否适度\n\n请按 ARR 审稿标准，给出 Strengths、Weaknesses (分 MUST-FIX 和 SHOULD-FIX)、Questions、Overall Assessment。"
  }
}
```

</details>

---


### Tool result

_source line 1163 · 2026-05-22T13:24:15.410806+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 19153
}
```

</details>

---


### Tool call

_source line 1164 · 2026-05-22T13:24:15.612483+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "policy_ambiguity_safety",
  "text": "你是 Reviewer 2，负责 **新颖性 + 完整性** 审查。\n\n## 投稿信息\n- **Venue**: EMNLP 2026 via ARR May cycle\n- **Deadline**: 2026-05-25 (11:59PM AoE)\n- **格式要求**: Long paper, 8页正文上限, unlimited references, Limitations section 必须（不计入页数）, double-blind, ACL style template\n- **匿名规则**: 双盲审稿, 无匿名期要求\n- **论文路径**: `projects/policy_ambiguity_safety/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_13/submitted.pdf`\n\n## 审查侧重\n\n请重点审查以下方面：\n\n1. **新颖性与贡献评估**\n   - 三个 contributions 的新颖性：(1) matched-pair causal study, (2) variance decomposition + risk gradient, (3) disambiguation neglect + systematic nocuity\n   - 与最接近的 concurrent work (DRIP-R, PolicyBank, AgentPex, MANTRA) 的差异化是否清晰\n   - Disambiguation Neglect 是否过度声称新颖性（Liu et al. 2023, Hu et al. 2025 已有 ambiguity collapse 发现）\n\n2. **Taxonomy 理论基础**\n   - 六类分类的理论 grounding 是否充分\n   - Incompleteness 和 Conditional Precedence 是否满足 strict ambiguity 定义（§3 Scope of ambiguity 段落是否足够）\n   - 两层结构 (linguistic vs specification) 的理论动机 vs C3 inconclusive 结果\n\n3. **Related Work 覆盖**\n   - 引用覆盖是否全面（NLP ambiguity, requirements engineering, agent safety, psycholinguistics）\n   - 是否有重要遗漏的 related work\n   - DRIP-R 对比的三个差异点 (causality, safety violations, model×type) 是否准确\n\n4. **Framing & Claims 校准**\n   - Abstract/Introduction 的 claims 是否与 Results 匹配\n   - 标题 \"Not All Policy Ambiguity Is Equal\" 是否被数据支持（gradient 是 margin-dependent 的）\n   - Domain scope (τ²-bench retail + airline) vs 论文措辞的 generality\n   - Variance decomposition 的 headline positioning (22.4% clause vs 0.4% type — taxonomy 的实用价值?)\n\n5. **写作质量与格式合规**\n   - ACL template 合规性\n   - 8页限制遵守情况\n   - Limitations section 覆盖是否充分\n   - 匿名性检查\n   - 数字使用一致性（4.6% vs ≤11% disambiguation awareness）\n   - Discussion 与 Error Analysis 的深度和信息密度\n\n6. **错误分析 (§6) 的贡献**\n   - 五种 failure mode 的分类方法和信度\n   - Systematic nocuity (41.3% convergent violations) 的解读\n   - Disambiguation Neglect 与 good-enough processing 的连接\n\n请按 ARR 审稿标准，给出 Strengths、Weaknesses (分 MUST-FIX 和 SHOULD-FIX)、Questions、Missing References、Overall Assessment。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "policy_ambiguity_safety",
    "text": "你是 Reviewer 2，负责 **新颖性 + 完整性** 审查。\n\n## 投稿信息\n- **Venue**: EMNLP 2026 via ARR May cycle\n- **Deadline**: 2026-05-25 (11:59PM AoE)\n- **格式要求**: Long paper, 8页正文上限, unlimited references, Limitations section 必须（不计入页数）, double-blind, ACL style template\n- **匿名规则**: 双盲审稿, 无匿名期要求\n- **论文路径**: `projects/policy_ambiguity_safety/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_13/submitted.pdf`\n\n## 审查侧重\n\n请重点审查以下方面：\n\n1. **新颖性与贡献评估**\n   - 三个 contributions 的新颖性：(1) matched-pair causal study, (2) variance decomposition + risk gradient, (3) disambiguation neglect + systematic nocuity\n   - 与最接近的 concurrent work (DRIP-R, PolicyBank, AgentPex, MANTRA) 的差异化是否清晰\n   - Disambiguation Neglect 是否过度声称新颖性（Liu et al. 2023, Hu et al. 2025 已有 ambiguity collapse 发现）\n\n2. **Taxonomy 理论基础**\n   - 六类分类的理论 grounding 是否充分\n   - Incompleteness 和 Conditional Precedence 是否满足 strict ambiguity 定义（§3 Scope of ambiguity 段落是否足够）\n   - 两层结构 (linguistic vs specification) 的理论动机 vs C3 inconclusive 结果\n\n3. **Related Work 覆盖**\n   - 引用覆盖是否全面（NLP ambiguity, requirements engineering, agent safety, psycholinguistics）\n   - 是否有重要遗漏的 related work\n   - DRIP-R 对比的三个差异点 (causality, safety violations, model×type) 是否准确\n\n4. **Framing & Claims 校准**\n   - Abstract/Introduction 的 claims 是否与 Results 匹配\n   - 标题 \"Not All Policy Ambiguity Is Equal\" 是否被数据支持（gradient 是 margin-dependent 的）\n   - Domain scope (τ²-bench retail + airline) vs 论文措辞的 generality\n   - Variance decomposition 的 headline positioning (22.4% clause vs 0.4% type — taxonomy 的实用价值?)\n\n5. **写作质量与格式合规**\n   - ACL template 合规性\n   - 8页限制遵守情况\n   - Limitations section 覆盖是否充分\n   - 匿名性检查\n   - 数字使用一致性（4.6% vs ≤11% disambiguation awareness）\n   - Discussion 与 Error Analysis 的深度和信息密度\n\n6. **错误分析 (§6) 的贡献**\n   - 五种 failure mode 的分类方法和信度\n   - Systematic nocuity (41.3% convergent violations) 的解读\n   - Disambiguation Neglect 与 good-enough processing 的连接\n\n请按 ARR 审稿标准，给出 Strengths、Weaknesses (分 MUST-FIX 和 SHOULD-FIX)、Questions、Missing References、Overall Assessment。"
  }
}
```

</details>

---


### Tool result

_source line 1165 · 2026-05-22T13:24:16.972386+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1359
}
```

</details>

---


### Assistant

_source line 1166 · 2026-05-22T13:24:23.941598+00:00_

圆桌审稿 Round 1 已启动：

- **视觉审查 Agent**：已派发（fire-and-forget）
- **Reviewer 1**（方法严谨性 + 实验设计）：已分配
- **Reviewer 2**（新颖性 + 完整性）：已分配

等待两位 Reviewer 返回独立审稿意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 107

## Round 107

2 recorded events


### User

_source line 1167 · 2026-05-22T13:30:16.219508+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 审稿报告：新颖性 + 完整性

**论文**: "Not All Policy Ambiguity Is Equal: Type-Specific Safety Risks for LLM Agents"
**Venue**: EMNLP 2026 via ARR May cycle

---

## 总体评分
**Overall**: 3.5 / 5 (Borderline Conference)
**一句话总结**: 方法论扎实的因果研究，matched-pair 设计和 perturbation control 是真正的贡献，但 taxonomy 解释力极低（type 仅占 0.4% variance）、gradient margin-dependent、domain 受限于 retail+airline，使得核心叙事"Not All Ambiguity Is Equal"的实际支撑力度弱于论文呈现的印象。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | matched-pair 设计严谨，perturbation control 有效（Δ_perturb = −0.67pp, CI 含 0），但 incompleteness 的 information-addition confound 只是 controlled 而非 eliminated，LLM-as-judge 且 judge 均为 OpenAI family 引入 systematic bias 风险 |
| Excitement | 3.5/5 | 因果研究设计在 agent safety 领域是新颖的，但 0.4% type variance 和 margin-dependent gradient 削弱了 taxonomy 的实用价值；Disambiguation Neglect 是对已有发现的 incremental extension |
| Reproducibility | 4/5 | 300 clause pairs、evaluation pipeline、analysis scripts 承诺发布；实验参数详尽（temperature=0, top_p=1, max_tokens=4096）；两个 replication models 增强可信度 |
| Confidence | 4/5 | 我熟悉 agent safety evaluation、NLP ambiguity、因果推断方法论 |

---

## 主要优势

**S1. 首个 matched-pair 因果设计.** 与 DRIP-R（correlational benchmark）不同，本文的 matched clause pairs + perturbation control 真正建立了 ambiguity → violation 的因果关系。Perturbation control（Δ = −0.67pp, CI containing zero; §4.5）排除了表面文本改变的干扰。这在 agent safety 文献中是方法论层面的贡献。

**S2. 统计分析极为详尽透明.** TOST equivalence testing、bootstrap cluster analysis、variance decomposition、Holm-Bonferroni 校正、SESOI 锚定在 domain-relevant threshold（±15pp）、seven-margin sensitivity analysis（Appendix A）。17 个 appendix 覆盖了几乎所有可能的 robustness check。C3 标注为 inconclusive、C4 标注为 exploratory——这种诚实标注在 NLP 论文中少见。

**S3. Systematic nocuity 概念有理论价值.** 41.3% 的 ambiguous clauses 触发多模型一致性违规（§6.3），扩展了 Berry & Kamsties (2004) 的 nocuous/innocuous 框架。这个发现对 policy auditing 有直接实践意义——如果多个模型在同一 clause 上都犯同样的错，说明问题在 clause 本身而非模型。

**S4. Replication 范围广.** 五个主模型 + 两个 replication 模型（Gemini 2.5 Flash, LLaMA 4 Scout），覆盖六家 provider（Appendix E），C1 在七个模型上均成立。

**S5. 与 concurrent work 的差异化清晰.** 与 DRIP-R 的三点差异（causality, safety violations vs decision quality, model×type interaction）准确且有据。Related Work 覆盖了 NLP ambiguity、RE、agent safety、psycholinguistics 四个方向，且引用了 2026 年 5 月的最新 concurrent work（DRIP-R, PolicyBank, AgentPex, MANTRA, ASPI）。

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] Taxonomy 解释力与论文叙事的根本张力
- 具体位置：§5.1 variance decomposition + Conclusion + Title
- 问题：论文标题 "Not All Policy Ambiguity Is Equal" 和核心叙事围绕六类 taxonomy 展开，但 variance decomposition 显示 **type 仅解释 0.4% 的 violation variance**（§5.1: "0.4% between types and 22.0% within types"）。Clause-level wording 解释 22.4%，model identity 解释 1.0%，residual 60.8%。这意味着：知道一个 ambiguous clause 属于哪个 type，几乎不增加对 violation risk 的预测力。
- 为什么影响接收：这不是一个"已知但无害"的 limitation——它从根本上削弱了论文的核心 contribution。如果 type 不重要，那么六类 taxonomy 的构建、TOST equivalence analysis、risk gradient 的发现，其实际价值都大打折扣。论文对此的讨论不够充分，仅在 §5.1 一句带过。
- 建议修改方向：(a) 在 Discussion 中专门讨论为什么 type 解释力低但 taxonomy 仍有价值（e.g., incompleteness 作为 consistent upper bound 的 screening 价值）；(b) 考虑将标题/framing 从 "type-specific risk" 调整为更准确的 "clause-level risk with type as a secondary predictor"；(c) 讨论 within-type variance 高意味着什么——是不是说 type 是必要但不充分的分类维度？

**N2** [critical] Incompleteness confound 未完全消除，且对 headline claims 影响过大
- 具体位置：§5.2, Appendix F, Abstract ("effects range from +18.7pp to +49.2pp")
- 问题：Incompleteness 的 unambiguous variant **必然添加新信息**（specifying what was missing），创造 information asymmetry。论文用 logistic regression 控制 token delta（Appendix H: p = 0.018, coefficient change < 8%），但 token count 是 information content 的粗糙代理。Paper 自己承认："finer-grained semantic measures (e.g., propositional content analysis) may reveal different confound structures"（Appendix F）。然而 Abstract 仍以 "+49.2pp" 作为 range 上限，Conclusion 重复此数字。
- 为什么影响接收：Incompleteness 驱动了论文的多个关键数字：(1) range 上限 49.2pp；(2) C2 gradient 的 upper bound；(3) 24% universal convergence（§6.3）；(4) bootstrap cluster 的 singleton。如果 confound 解释了 incompleteness effect 的一部分，这些数字的可信度都会下降。
- 建议修改方向：(a) 在 Abstract/Conclusion 中明确标注 incompleteness 效应为 "upper bound, conditional on information-addition confound"（目前只在 §5.2 后半段提及）；(b) 考虑在正文而非仅 Appendix 报告 confound-free 的 range（+18.7pp to +36.0pp，排除 incompleteness 后）；(c) 讨论 propositional content analysis 的可行性作为 future work。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Two-layer structure (linguistic vs specification) 缺乏经验支持
- 具体位置：§3 taxonomy design, §5.3 (C3)
- 问题：论文在 taxonomy 设计中突出两层结构（Table 1, Figure 1），且在 §3 末段提出假设："linguistic ambiguity can be partially resolved through tool responses or world knowledge, while specification ambiguity has no external resolution channel." 但 C3 结果是 inconclusive：effect 不survive Holm-Bonferroni 校正，controlling for token delta 还逆转方向。Cross-layer overlap 也很大（conditional precedence 36.8% vs scopal 39.4%）。
- 建议：要么降级两层结构为 "organizational convenience"（而非理论假设），要么在 Discussion 中深入分析为什么假设不成立。当前处理方式（§5.3 一段简短报告）不够充分。

**W2** [warning] LLM-as-judge + OpenAI-family bias
- 具体位置：§4.4, Limitations "Measurement" paragraph
- 问题：所有模型由 GPT-5.4 或 GPT-4.1 评判，均为 OpenAI family。§4.4 承认"systematic judge bias cancels in the same model-judge pairing"，但 cross-model 比较（C4）仍然受此影响。Limitations 提到 "cross-family judge evaluation (e.g., Claude judging GPT traces) would strengthen C4 conclusions"，但 C4 的 headline 发现（authorization scope 52pp range）已在正文中大量讨论。
- 建议：在 §5.4 中更明确地标注 C4 结论受 judge bias 限制，而非将此完全推到 Limitations section。

**W3** [warning] Error Analysis (§6) 的 LLM-coded 方法论
- 具体位置：§6, inter-coder reliability
- 问题：五种 failure mode 由 GPT-5.4 和 GPT-4.1 编码（而非人工），inter-coder κ = 0.52（moderate）。用 LLM 编码 LLM 的 failure modes 存在 circularity 风险——LLM coders 可能系统性地低估某些自己容易犯的错误。论文用 prevalence paradox 解释低 κ（三类占~90%），但 Gwet's AC₁ = 0.62 仍只是 substantial 而非 excellent。
- 建议：(a) 至少在一个 failure mode 类别上报告人工编码对照；(b) 讨论 LLM-coding 的 circularity 风险。

**W4** [warning] Disambiguation Neglect 的新颖性声称需要更准确定位
- 具体位置：§6.2, Introduction contribution (3)
- 问题：论文在 Introduction 第 21 行说 contribution (3) "extends LLM ambiguity-collapse findings (Liu et al., 2023; Hu et al., 2025) to agentic settings"。这个定位是诚实的，但 "extends to agentic settings" 的 novelty 需要更清楚地论证：**为什么 agentic settings 不同于 non-agentic settings？** §6.2 说 "agents process ambiguous input without meta-cognitive awareness but, unlike humans, lack social channels to recover"——但 non-agentic LLMs 同样缺乏 social channels。真正的差异应该是 **agentic setting 中 disambiguation neglect 有 real-world safety consequences**（执行动作 vs 仅生成文本），但这个论点没有被显式展开。
- 建议：在 §6.2 或 Discussion 中明确阐述 agentic vs non-agentic 的关键区别在于 consequentiality（行动后果），而非仅仅是 "extends to a new setting"。

**W5** [warning] Domain generalizability 的 framing
- 具体位置：Abstract ("policy-governed agent deployments"), Conclusion ("customer-service deployments")
- 问题：τ²-bench 仅覆盖 retail + airline customer service。Abstract 用 "policy-governed agent deployments" 这一宽泛措辞，但 Conclusion 正确收窄为 "customer-service deployments"。两处措辞不一致。此外，论文 Limitations 说 "within-study cross-domain consistency is encouraging"，但只有两个 domain（retail + airline），cross-domain consistency 的说服力有限。
- 建议：统一 Abstract 和 Conclusion 的 scope 措辞；避免在 Abstract 中暗示超出数据支持范围的 generality。

**W6** [warning] Margin-dependent gradient 的呈现
- 具体位置：§5.2, Figure 2
- 问题：risk gradient 的 TOST 等价结构在 ±15pp 处才完全稳定（6/6 mid-tier pairs equivalent），在 ±10pp 处只有 3/6。论文在 §5.2 中说 "the gradient is margin-dependent"，但 Figure 2（forest plot）和 headline 描述给读者的印象是一个稳定的三层结构（upper-mid-lower）。实际上，在不同 margin 下，结构会变化。
- 建议：在 Figure 2 caption 或正文中更突出 margin-dependency，避免给读者一个过于确定的 gradient 印象。

---

## 小问题（不影响接收）

- §1 开头的 motivating example（$200 scopal ambiguity）很生动，但后文的数据并没有给出 per-incident 的 monetary cost 估计——读者可能期待看到这个连接
- Table 2 caption 中 "Tier" 列的解释（U/M/L）写在 caption 里，但 caption 已经很长，考虑用 footnote
- §5.1 "Perturbation controls confirm specificity to semantic ambiguity (n = 300, Δ_perturb = −0.67pp, CI containing zero)"——应该给出 CI 的具体数值而非仅说 "containing zero"
- Appendix 标签从 A 到 Q（17 个），数量很大但组织清晰；考虑在正文中添加一个 "Appendix roadmap" 帮助读者导航
- §4.2 "reviewed by two independent annotators (both with NLP background)"——人工标注者应报告更多 demographics（experience level, training procedure）

---

## 缺失引用检查

### 已覆盖的关键方向
- NLP ambiguity: ✓ (Navigli 2009, Li et al. 2024, Liu et al. 2023, Hu et al. 2025)
- Requirements engineering: ✓ (Berry & Kamsties 2004, Massey et al. 2014, Dalpiaz et al. 2018, Ferrari et al. 2019)
- Agent safety: ✓ (τ-bench, τ²-bench, RJudge, ToolEmu, InjecAgent, SafeAgentBench, AgentAuditor, ShieldAgent)
- Concurrent work: ✓ (DRIP-R, PolicyBank, AgentPex, MANTRA, ASPI)
- Psycholinguistics: ✓ (Ferreira et al. 2002, Frazier & Rayner 1982)

### 可能遗漏
- **R-Judge (Wang et al., 2024)** 的后续工作或扩展（如果有）
- **Scope ambiguities in LLMs (Stengel-Eskin et al., TACL 2024)** — 关于 LLM 处理 scope ambiguity 的实证研究，与本文 scopal type 直接相关，目前未引用
- **"To Know or Not To Know" (2024)** — 关于 LLM self-consistency under ambiguity，与 Disambiguation Neglect 相关
- **Pragmatic competence 方向**: 论文讨论了 LLM 缺乏 pragmatic 推理能力，但未引用 LLM pragmatics 的相关工作（e.g., Hu et al. 2022 on implicature, Ruis et al. 2024 on pragmatic understanding）

---

## Questions for Authors

**Q1**: Variance decomposition 显示 type 仅解释 0.4% variance。如果一个 practitioner 想用你们的 taxonomy 做 policy auditing，具体的 workflow 是什么？是 binary detection（F1=0.81）就够了，还是需要 type-level classification（macro F1 仅 0.63，incompleteness F1=0.34）？

**Q2**: C4 interaction 完全集中在 authorization scope（Appendix N: 排除后 p=0.97）。这是否意味着 model×type interaction 实际上是一个 authorization-scope-specific 的现象，而非 general type-model interaction？如果是，C4 的 contribution 应该如何重新表述？

**Q3**: Mitigation experiment（§7, Appendix B）显示 incompleteness 在不同 prompt formulation 下效果方向相反（v1: −3.4pp, v2: +14pp）。作者如何解释这个 prompt sensitivity？这是否 undermine 了论文的 practical recommendation（type-specific mitigation）？

**Q4**: Systematic nocuity（41.3% ≥3/5 models）基于仅 5 个模型的 majority vote。如果加上 2 个 replication models（共 7 个），这个比例会如何变化？

**Q5**: 论文排除了 coreferential 在 mitigation 和 replication 实验中的参与，理由是 "benchmark-specific structural constraints"。这个 limitation 是否暗示 taxonomy 中某些 types 在操作上不如其他 types 稳健？

---

## 总结判断

本文方法论严谨，matched-pair 因果设计是 agent safety 领域的真正贡献。统计分析细致透明，appendix 详尽。但存在一个核心张力：**论文围绕 type-level taxonomy 构建叙事，但数据显示 type 的解释力极低（0.4%），clause wording 才是主要因素。** 这不是一个可以忽略的数字——它直接质疑了 taxonomy 作为 practical tool 的价值。加上 incompleteness confound 未完全消除、C3 inconclusive、domain 受限于两个 customer-service domain，我认为论文在当前 framing 下处于 Borderline Conference。如果能在 Discussion 中正面应对 0.4% variance 问题并调整 framing，强度可以提升到 Conference 级别。

**推荐**: 3.5 (Borderline Conference) — 方法论贡献值得认可，但 taxonomy 的实用价值需要更诚实的定位。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1168 · 2026-05-22T13:30:26.308496+00:00_

Reviewer 2 审稿意见已收到。等待 Reviewer 1 的报告，收齐后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 108

## Round 108

2 recorded events


### User

_source line 1169 · 2026-05-22T13:30:40.088505+00:00_

[Reviewer 2 审稿结果]:
Reviewer 2 审稿完成，报告已提交至 Review Director。

**评分**: Overall 3.5 (Borderline Conference)

**核心判断**: 方法论扎实（matched-pair 因果设计 + perturbation control 是真正贡献），但存在一个根本张力——**type 仅解释 0.4% variance**，与论文围绕 taxonomy 构建的叙事不匹配。

**两个 Must-Fix**:
1. Taxonomy 解释力（0.4%）与论文标题/framing 的矛盾需要正面讨论
2. Incompleteness 的 information-addition confound 在 Abstract/Conclusion 中应更显式标注为 upper bound

**六个 Should-Fix**: two-layer 结构缺乏经验支持（C3 inconclusive）、LLM-as-judge bias、Error Analysis 的 LLM-coding circularity、Disambiguation Neglect 新颖性定位、domain generalizability framing、margin-dependent gradient 呈现方式。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1170 · 2026-05-22T13:30:45.043421+00:00_

Reviewer 2 报告已收到。等待 Reviewer 1 的报告。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 109

## Round 109

8 recorded events


### User

_source line 1171 · 2026-05-22T13:31:12.403962+00:00_

[Reviewer 1 审稿意见]:
## 总体评分
**Overall**: 3.5/5 — Borderline Conference
**一句话总结**: 实验设计严谨、统计框架全面、claim 标定诚实，但 cross-judge confound 限制了跨模型结论的可信度，type 仅解释 0.4% 方差削弱了分类体系的实用价值，SESOI 论证需要加强。

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 主要 claims (C1, C2) 有充分支撑，C3 诚实标注 inconclusive，C4 标注 exploratory。但 cross-judge confound 和 incompleteness information-addition confound 部分削弱了结论强度 |
| Excitement | 3/5 | 匹配对设计在 LLM agent safety 领域属首创，Disambiguation Neglect 发现有价值。但核心发现（歧义增加违规）并不意外，type-level 方差极低限制了 taxonomy 的实用意义 |
| Reproducibility | 4/5 | 承诺开源 300 clause pairs、evaluation pipeline、analysis scripts。ICC=0.919，2-model replication，多 severity threshold 验证。缺失：未公开 prompt 模板和 judge prompt 的完整文本 |
| Overall | 3.5/5 | Borderline Conference — 方法学贡献扎实，但若干 confound 和 variance 问题需要 revision 中解决或更透明地承认 |
| Confidence | 4/5 | 对实验设计和统计方法较熟悉，仔细验证了各项数据 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] Cross-judge type ranking 近零相关性需在主文中正面讨论，而非仅放 Appendix

- 具体位置：Appendix P (§P, "Within-Judge-Group Type Rankings")；主文 Section 5.2 和 Limitations
- 问题：Appendix P 报告跨 judge 组的 type ranking Spearman ρ = −0.03 (p = 0.96)——两组对六种 ambiguity type 的严重程度排序几乎完全不一致。论文将此归因于 "agent composition"（GPT-4.1 组包含 auth scope 高危的 GPT-5.4 和 DeepSeek），但这恰好是 judge confound 的核心问题：judge bias 和 model composition 效应**无法分离**。在只有 2 models 的 GPT-4.1-judged 组中，两者碰巧都有高 auth scope 违规率，使得 judge effect 和 model effect 完全混淆。
- 这一发现直接关联 C2 (type risk gradient) 的可靠性：如果 pooled type ranking 在不同 judge 组下重现性为零，那么 Table 2 的 pooled 排序在多大程度上反映了真实的 type 差异而非 judge-weighted model 组成的偶然结果？
- 为什么影响接收：C2 是论文的核心 claim 之一——type 形成 risk gradient。如果此 gradient 的 cross-judge generalizability 为零（ρ = −0.03），reviewer 有理由质疑 gradient 的外部效度。当前仅在 Appendix P 用两句话处理，主文 Section 5.2 完全没有提及。
- 建议修改方向：(1) 在 Section 5.2 正文中正面讨论 ρ = −0.03 的含义，不仅归因于 agent composition，也承认 judge-level confound 无法排除；(2) 分别报告两组内的 type gradient 结构（是否都在 ±15pp 内等价？），明确说明 C2 的 pooled 结论在多大程度上依赖 GPT-5.4 组的 3:2 权重；(3) 考虑在 Limitations 中将此列为最主要的 measurement limitation 而非仅一句带过。

**N2** [critical] Type 仅解释 0.4% 方差与论文核心叙事的张力需要明确讨论

- 具体位置：Section 5.1, "This decomposes into 0.4% between types and 22.0% within types"
- 问题：论文标题 "Not All Policy Ambiguity Is Equal" 暗示 type 是强预测因子。但方差分解显示：clause identity 22.4%，model 1.0%，**type 0.4%**，residual 60.8%。Type 解释的方差是 clause 的 1/55。这意味着知道某个 clause 属于哪种 ambiguity type 几乎不能预测其违规概率——具体措辞远比 type 分类重要。
- 论文在统计显著性层面证明了 types 之间存在差异（χ² p < 10⁻⁵），但效应量（Cramér's V = 0.137, 0.4% variance explained）表明差异虽显著却很微弱。这产生一个实际问题：如果部署者根据 type 分类来优先修复歧义（论文 Section 7 "Practical implications" 暗示的应用方向），其效果将非常有限，因为 within-type 的 clause-level 变异远超 between-type 差异。
- 为什么影响接收：这是 claim 强度与证据强度之间的校准问题。论文需要明确区分 "types differ statistically" 和 "type is a useful predictor for deployment decisions"，否则读者可能高估 taxonomy 的实用价值。
- 建议修改方向：(1) 在 Section 5.1 讨论 0.4% variance 时，主动讨论这对 type-level interventions 实用性的含义；(2) 在 Discussion 或 Conclusion 中加入一段，明确说明 clause-level auditing 可能比 type-level prioritization 更有效；(3) 考虑调整标题或 framing 以更准确反映效应量级。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] SESOI ±15pp 的论证不足——TOST gradient 结构是 margin-dependent 的

- 具体位置：Section 4.6; Table 3 (Appendix A)
- 问题：论文承认 "No field-standard SESOI exists for agent policy compliance"，然后自定义 ±15pp 并论证其 "operationally meaningful"。但关键在于：C2 的 mid-tier equivalence cluster 结构高度依赖此 margin。Table 3 显示 ±10pp 时仅 3/6 mid-tier pairs equivalent，±12pp 时 5/6，±15pp 才达到 6/6。一位选择 ±10pp 的 reviewer（并非不合理——10pp 违规率差已可能影响审计决策）会看到一个远没那么清晰的 gradient。
- 论文用 bootstrap clustering 作为 margin-free 补充，这很好。但 bootstrap 在 k=2 时的重现率仅 34.3%（Appendix I），说明 incompleteness 的 singleton 分离也不稳健。
- 建议：(1) 在主文 Section 5.2 中显式提及 "the equivalence structure is margin-dependent" 而不仅仅放在 Appendix 中；(2) 报告 ±10pp 和 ±12pp 下的 gradient 结构作为 sensitivity check；(3) 更谨慎地描述 bootstrap 结果（"the most frequent partition" 而非暗示稳健）。

**W2** [warning] Authorization scope 的 judge 一致性最低 (κ=0.385) 却是 C4 interaction 的核心驱动

- 具体位置：Section 4.4 ("$\kappa = 0.385$ (authorization scope)"); Section 5.4 (C4); Appendix G (Table 9, κ=0.644 for auth scope human-LLM)
- 问题：Authorization scope 在三个层面的一致性都最低——cross-judge binary κ=0.385, human-LLM κ=0.644, 且是 Appendix P 中 type ranking 翻转的主因。但 C4 的 model×type interaction 完全集中在此 type（排除后 p=0.97, Appendix N）。论文在 Section 5.4 中标注 "suggestive rather than definitive" 并提到 prevalence paradox，这是对的，但问题在于：Figure 3 的 heatmap 作为主文 figure 给读者的视觉印象是 auth scope 有 52pp 的巨大 model 差异，而这 52pp range 中有多少归因于 measurement noise 而非真实 model 差异？
- 建议：(1) 在 Figure 3 caption 中更显著地标注 auth scope 的 reliability caveat；(2) 考虑在主文中计算 auth scope 的 measurement-noise-adjusted range（利用 κ=0.385 估算 disagreement band）。

**W3** [warning] Incompleteness confound control 使用 token count 作为 information delta 代理——粒度不足

- 具体位置：Appendix F (Section F); Appendix H (Table 10)
- 问题：Logistic regression 用 token count difference 控制 information addition confound，incompleteness 在控制后仍显著 (p=0.018/0.022)。但 token count 是 information content 的粗略代理——一个包含关键限制条件的 10-word 增补可能比一段 36-word 的补充描述提供更多决策关键信息。论文自己也承认 "Token count is a coarse proxy for information content"（Appendix F）。
- 额外数据点：Appendix O 显示 authorization scope 的 token delta (+36.1) 比 incompleteness (+34.6) 更大，但 auth scope 违规率更低——论文将此作为 counter-evidence against information-quantity explanation。然而，这忽略了 information *quality* 差异：authorization scope 的额外信息是边界限制（"only managers can issue refunds over $100"），而 incompleteness 的额外信息填补了之前完全缺失的内容。信息的*类型*不同，仅凭 quantity 对比不能排除 confound。
- 建议：在 Appendix F 的 caveat 之外，在主文 Section 5.2 的 incompleteness 讨论中也加入一句明确说明 token count 控制的局限性。

**W4** [warning] Human validation n=100 的 per-type 可靠性变异极大，部分 type 的 CI 过宽

- 具体位置：Section 4.4; Appendix G (Table 9)
- 问题：Overall human-LLM κ=0.735，但 per-type 变异从 0.904 (lexical) 到 0.479 (coreferential)。更重要的是 95% CI：scopal 的 CI 是 [0.00, 1.00]——完全无信息；coreferential 的 CI 是 [0.00, 0.84]。论文正确注明 "Per-type estimates are imprecise due to small cell sizes"，但影响在于：我们无法确认 automated judge 对各 type 同等可靠——这是 type-level 比较的一个假设。
- 建议：在 Limitations 中更明确地将 per-type reliability variation 列为 type-level comparison 的 caveat，并建议 future work 增加 per-type validation sample size。

**W5** [warning] Reproducibility ICC=0.919 仅在 OpenAI 家族内计算

- 具体位置：Section 4.5, "ICC is computed within the OpenAI family"
- 问题：ICC 基于 30 clause pairs × 2 models × 3 replicates，但两个 model 都是 OpenAI 的（GPT-5.4 和 GPT-4.1）。跨 provider 的 reproducibility 仅由 C1 在 7 个 model 上一致性间接推断。对于一篇声称 "across five models from four providers" 的论文，直接的跨 provider reproducibility 测试会更有说服力。
- 建议：在 Limitations 中明确 ICC 的 scope 限制，或在 replication study (Appendix E) 中增加 replication pair 的 ICC 计算。

---

## 小问题（不影响接收）

- Section 4.2: "Clause pairs are generated through a template-based pipeline"——但未详述 template 的具体结构。建议在 appendix 中加入 2-3 个不同 type 的 clause pair 示例（ambiguous + unambiguous），帮助读者判断 minimal edit 是否确实 minimal。
- Section 5.1: 方差分解使用了什么具体方法（nested ANOVA? Linear mixed model? Something else?）未明确说明。对于 binary outcome，标准 ANOVA 的假设不完全满足，论文应简要说明方法选择。
- Section 6: Error analysis 的 inter-coder reliability (Gwet's AC₁=0.62, Cohen's κ=0.52) 属于 moderate agreement。κ=0.52 在 coding 5 个 failure mode categories 时偏低。论文解释了 prevalence paradox，但 prevalence paradox 不能完全解释 moderate κ——它只解释了 κ 低于 raw agreement 的部分。论文应承认 failure mode coding 本身的可靠性限制对 Section 6 各结论的约束。
- Table 2: Tier 列（U/M/L）的含义在 caption 中已定义，但主文首次引用 tier 结构时（Section 5.2）应简要解释 U/M/L 代表什么。
- Section 1 contribution (2): "60.8% residual" 作为贡献列出有些奇怪——residual variance 通常不是贡献而是局限。建议重新 frame 为 "clause-level wording is the primary driver of within-type variation (22.4% vs. 0.4% for type), with substantial unexplained variance (60.8%)"。

---

## 主要优势

1. **Matched-pair 设计是该领域的方法学进步**：相比于前人对 ambiguity 影响的 observational 或 correlational 研究，within-clause 配对比较提供了更强的因果推断基础。Perturbation control (n=300, Δ=-0.67pp) 有效排除了 surface-level editing 的替代解释。

2. **Claim 标定极为诚实**：C3 (layer effect) 标注 inconclusive（未过 Holm-Bonferroni 校正且 token delta 控制后方向翻转），C4 标注 exploratory 并在低 κ 时明确 "suggestive rather than definitive"。这种审慎程度在同类实证研究中并不常见。

3. **统计框架全面且恰当**：McNemar (paired binary) → χ²/Fisher's exact (omnibus/per-type) → TOST (equivalence) → bootstrap clustering (margin-free) → Holm-Bonferroni (multiple comparison) → logistic regression (confound control) → variance decomposition。工具选择与研究问题匹配度高。

4. **Robustness checks 充分**：two severity thresholds (Table 5)，7 TOST margins (Table 3)，2-model replication (Appendix E)，perturbation control，incompleteness exclusion analysis，auth scope exclusion analysis for C4。

5. **Disambiguation Neglect 发现新颖且有实践意义**：4.6% 整体 awareness rate（最高 Claude 11%）加上 "systematic nocuity"（41.3% 多数模型趋同违规）概念，将 LLM ambiguity-collapse 文献扩展到了 consequential agentic settings。

6. **Type-specific failure mechanism 分析有深度**：三种机制（structural misparse / information gap-filling / boundary violation）crosscut layer boundary 的发现直接 undermines C3 的 layer distinction，论文诚实地在 Section 5.3 承认这一点。

---

## Questions for Authors

Q1: 是否考虑过对全部 2,997 episodes 进行 dual-judge evaluation（而非仅 100 episode calibration sample）？即使只在一个 type（如 auth scope）上做完整 dual-judge，也能直接量化该 type 的 judge disagreement 对 violation rate 的影响。当前 100 episode 样本对 per-type 分析的 power 不足（n=32-34/type）。

Q2: 方差分解中 60.8% residual 主要由什么构成？论文提到 "scenario-level variation, judge variability, and unmeasured clause features"。是否可以进一步分解——例如，τ²-bench 中 episode 的 user behavior 变异（不同 user prompt 可能触发不同的 agent 反应）占多大比例？

Q3: Appendix P 的 cross-judge-group type ranking ρ = -0.03——如果排除 authorization scope（已知 κ 最低），剩余 5 个 type 的 cross-judge ranking ρ 是多少？这能帮助区分 "auth scope 特有的 judge disagreement" 和 "系统性的 judge confound"。

Q4: Replication study (Appendix E) 排除了 coreferential，mitigation study 也排除了 coreferential——coreferential 因此在 3 个 robustness check 中都缺席。这是否影响 coreferential 作为 "confound-free lower bound" 的可信度？如果 coreferential 的 effect 在新 model 上不 replicate 怎么办？

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1172 · 2026-05-22T13:31:41.433038+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '检查论文资料完整性并调研 EMNLP 2026 venue 要求'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.7: 派发视觉审查', 'status': 'completed', 'activeForm': '派发视觉审查 Agent'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'completed', 'activeForm': '收集 Reviewer 独立审稿结果'}, {'content': 'Step 2: 交叉分享', 'status': 'in_progress', 'activeForm': 'Reviewer 交叉分享与回应'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断审稿意见收敛性'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'pending', 'activeForm': '汇总审稿报告并投递'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '检查论文资料完整性并调研 EMNLP 2026 venue 要求'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.7: 派发视觉审查', 'status': 'completed', 'activeForm': '派发视觉审查 Agent'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'completed', 'activeForm': '收集 Reviewer 独立审稿结果'}, {'content': 'Step 2: 交叉分享', 'status': 'in_progress', 'activeForm': 'Reviewer 交叉分享与回应'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断审稿意见收敛性'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'pending', 'activeForm': '汇总审稿报告并投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 1173 · 2026-05-22T13:31:41.483823+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "TodoWrite",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1174 · 2026-05-22T13:32:11.796128+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "policy_ambiguity_safety",
  "text": "## 交叉分享：以下是 Reviewer 2 的完整审稿意见\n\n请逐条回应：对每个 Must-Fix 和 Should-Fix，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n以下是 Reviewer 2 的原文：\n\n**评分**: 3.5/5 (Borderline Conference)\n\n**Must-Fix:**\n\n**N1** [critical] Taxonomy 解释力与论文叙事的根本张力\n- Type 仅解释 0.4% violation variance（§5.1），clause-level wording 解释 22.4%。标题 \"Not All Policy Ambiguity Is Equal\" 暗示 type 是强预测因子，但 0.4% 说明知道 type 几乎不增加预测力。\n- 建议：Discussion 专门讨论 type 解释力低但 taxonomy 仍有价值的原因；考虑调整标题/framing；讨论 within-type variance 高意味着什么。\n\n**N2** [critical] Incompleteness confound 未完全消除，且对 headline claims 影响过大\n- Incompleteness 的 unambiguous variant 必然添加新信息，token count 是粗糙代理。Abstract 仍以 \"+49.2pp\" 作为 range 上限。\n- 建议：Abstract/Conclusion 明确标注 upper bound + confound caveat；正文报告 confound-free range (+18.7 to +36.0)；讨论 propositional content analysis。\n\n**Should-Fix:**\n\n**W1** Two-layer structure (linguistic vs specification) 缺乏经验支持（C3 inconclusive，cross-layer overlap）\n**W2** LLM-as-judge + OpenAI-family bias（all models judged by GPT-5.4 or GPT-4.1）\n**W3** Error Analysis (§6) 的 LLM-coded 方法论（κ=0.52 moderate，circularity risk）\n**W4** Disambiguation Neglect 新颖性需要更准确定位（agentic vs non-agentic 区别在于 consequentiality）\n**W5** Domain generalizability framing（Abstract \"policy-governed agent deployments\" vs Conclusion \"customer-service deployments\" 不一致）\n**W6** Margin-dependent gradient 呈现（±15pp 才 6/6 equivalent，Figure 2 给出过于确定的印象）\n\n**缺失引用：**\n- Stengel-Eskin et al. (TACL 2024) — scope ambiguity in LLMs\n- \"To Know or Not To Know\" (2024) — LLM self-consistency under ambiguity\n- Hu et al. 2022 on implicature, Ruis et al. 2024 on pragmatic understanding\n\n**Questions:**\n- Q1: 0.4% type variance 下 practitioner 用 taxonomy 做 policy auditing 的具体 workflow？\n- Q2: C4 interaction 完全集中在 auth scope（排除后 p=0.97），是否是 auth-scope-specific 现象？\n- Q3: Mitigation incompleteness prompt sensitivity (v1: -3.4pp vs v2: +14pp) 如何解释？\n- Q4: Systematic nocuity 41.3% 基于 5 模型，加上 2 replication models 会变化吗？\n- Q5: Coreferential 在 mitigation 和 replication 都缺席，是否影响其作为 confound-free lower bound 的可信度？"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "policy_ambiguity_safety",
    "text": "## 交叉分享：以下是 Reviewer 2 的完整审稿意见\n\n请逐条回应：对每个 Must-Fix 和 Should-Fix，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n以下是 Reviewer 2 的原文：\n\n**评分**: 3.5/5 (Borderline Conference)\n\n**Must-Fix:**\n\n**N1** [critical] Taxonomy 解释力与论文叙事的根本张力\n- Type 仅解释 0.4% violation variance（§5.1），clause-level wording 解释 22.4%。标题 \"Not All Policy Ambiguity Is Equal\" 暗示 type 是强预测因子，但 0.4% 说明知道 type 几乎不增加预测力。\n- 建议：Discussion 专门讨论 type 解释力低但 taxonomy 仍有价值的原因；考虑调整标题/framing；讨论 within-type variance 高意味着什么。\n\n**N2** [critical] Incompleteness confound 未完全消除，且对 headline claims 影响过大\n- Incompleteness 的 unambiguous variant 必然添加新信息，token count 是粗糙代理。Abstract 仍以 \"+49.2pp\" 作为 range 上限。\n- 建议：Abstract/Conclusion 明确标注 upper bound + confound caveat；正文报告 confound-free range (+18.7 to +36.0)；讨论 propositional content analysis。\n\n**Should-Fix:**\n\n**W1** Two-layer structure (linguistic vs specification) 缺乏经验支持（C3 inconclusive，cross-layer overlap）\n**W2** LLM-as-judge + OpenAI-family bias（all models judged by GPT-5.4 or GPT-4.1）\n**W3** Error Analysis (§6) 的 LLM-coded 方法论（κ=0.52 moderate，circularity risk）\n**W4** Disambiguation Neglect 新颖性需要更准确定位（agentic vs non-agentic 区别在于 consequentiality）\n**W5** Domain generalizability framing（Abstract \"policy-governed agent deployments\" vs Conclusion \"customer-service deployments\" 不一致）\n**W6** Margin-dependent gradient 呈现（±15pp 才 6/6 equivalent，Figure 2 给出过于确定的印象）\n\n**缺失引用：**\n- Stengel-Eskin et al. (TACL 2024) — scope ambiguity in LLMs\n- \"To Know or Not To Know\" (2024) — LLM self-consistency under ambiguity\n- Hu et al. 2022 on implicature, Ruis et al. 2024 on pragmatic understanding\n\n**Questions:**\n- Q1: 0.4% type variance 下 practitioner 用 taxonomy 做 policy auditing 的具体 workflow？\n- Q2: C4 interaction 完全集中在 auth scope（排除后 p=0.97），是否是 auth-scope-specific 现象？\n- Q3: Mitigation incompleteness prompt sensitivity (v1: -3.4pp vs v2: +14pp) 如何解释？\n- Q4: Systematic nocuity 41.3% 基于 5 模型，加上 2 replication models 会变化吗？\n- Q5: Coreferential 在 mitigation 和 replication 都缺席，是否影响其作为 confound-free lower bound 的可信度？"
  }
}
```

</details>

---


### Tool result

_source line 1175 · 2026-05-22T13:32:35.002404+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 23206
}
```

</details>

---


### Tool call

_source line 1176 · 2026-05-22T13:32:35.756414+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "policy_ambiguity_safety",
  "text": "## 交叉分享：以下是 Reviewer 1 的完整审稿意见\n\n请逐条回应：对每个 Must-Fix 和 Should-Fix，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n以下是 Reviewer 1 的原文：\n\n**评分**: 3.5/5 (Borderline Conference)\n\n**Must-Fix:**\n\n**N1** [critical] Cross-judge type ranking 近零相关性（ρ=-0.03, p=0.96, Appendix P）需在主文正面讨论\n- 两个 judge 组对六种 type 的严重程度排序几乎完全不一致。Judge bias 和 model composition 效应无法分离（GPT-4.1 组仅 2 models）。\n- 直接关联 C2 (type risk gradient) 的可靠性：pooled type ranking 在不同 judge 组下重现性为零。\n- 建议：§5.2 正面讨论 ρ=-0.03；分别报告两组内的 type gradient 结构；明确 C2 对 GPT-5.4 组 3:2 权重的依赖。\n\n**N2** [critical] Type 仅解释 0.4% 方差与论文核心叙事张力\n- 标题暗示 type 是强预测因子，但方差分解显示 type 0.4% vs clause 22.4% vs model 1.0% vs residual 60.8%。\n- 知道 clause 属于哪种 type 几乎不增加预测力。Type-level interventions 实用性存疑。\n- 建议：§5.1 讨论 type 解释力低对实用性的含义；Discussion 明确 clause-level auditing 优于 type-level；考虑调整标题/framing。\n\n**Should-Fix:**\n\n**W1** SESOI ±15pp 论证不足——C2 gradient 在 ±10pp 时仅 3/6 equivalent，bootstrap k=2 重现率仅 34.3%\n**W2** Auth scope κ=0.385 最低却是 C4 核心驱动——Figure 3 视觉印象 vs reliability caveat 不匹配\n**W3** Incompleteness confound token count proxy 粒度不足——information quality vs quantity 差异未讨论\n**W4** Human validation per-type CI 过宽（scopal [0.00, 1.00]，coreferential [0.00, 0.84]）\n**W5** Reproducibility ICC=0.919 仅在 OpenAI 家族内计算\n\n**小问题:**\n- Clause pair 示例缺失（应在 appendix 加 2-3 例）\n- 方差分解具体方法未说明（nested ANOVA? LMM?）\n- Error analysis κ=0.52 的 prevalence paradox 解释不能完全覆盖 moderate agreement\n- 60.8% residual 作为贡献列出不太恰当\n- Contribution (2) 中 \"60.8% residual\" 应 reframe\n\n**Questions:**\n- Q1: 是否考虑对全部 2,997 episodes 做 dual-judge evaluation？\n- Q2: 60.8% residual 主要由什么构成？user behavior 变异占比？\n- Q3: 排除 auth scope 后，剩余 5 type 的 cross-judge ranking ρ 是多少？\n- Q4: Coreferential 在 3 个 robustness check 中缺席，是否影响其作为 confound-free lower bound？"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "policy_ambiguity_safety",
    "text": "## 交叉分享：以下是 Reviewer 1 的完整审稿意见\n\n请逐条回应：对每个 Must-Fix 和 Should-Fix，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n以下是 Reviewer 1 的原文：\n\n**评分**: 3.5/5 (Borderline Conference)\n\n**Must-Fix:**\n\n**N1** [critical] Cross-judge type ranking 近零相关性（ρ=-0.03, p=0.96, Appendix P）需在主文正面讨论\n- 两个 judge 组对六种 type 的严重程度排序几乎完全不一致。Judge bias 和 model composition 效应无法分离（GPT-4.1 组仅 2 models）。\n- 直接关联 C2 (type risk gradient) 的可靠性：pooled type ranking 在不同 judge 组下重现性为零。\n- 建议：§5.2 正面讨论 ρ=-0.03；分别报告两组内的 type gradient 结构；明确 C2 对 GPT-5.4 组 3:2 权重的依赖。\n\n**N2** [critical] Type 仅解释 0.4% 方差与论文核心叙事张力\n- 标题暗示 type 是强预测因子，但方差分解显示 type 0.4% vs clause 22.4% vs model 1.0% vs residual 60.8%。\n- 知道 clause 属于哪种 type 几乎不增加预测力。Type-level interventions 实用性存疑。\n- 建议：§5.1 讨论 type 解释力低对实用性的含义；Discussion 明确 clause-level auditing 优于 type-level；考虑调整标题/framing。\n\n**Should-Fix:**\n\n**W1** SESOI ±15pp 论证不足——C2 gradient 在 ±10pp 时仅 3/6 equivalent，bootstrap k=2 重现率仅 34.3%\n**W2** Auth scope κ=0.385 最低却是 C4 核心驱动——Figure 3 视觉印象 vs reliability caveat 不匹配\n**W3** Incompleteness confound token count proxy 粒度不足——information quality vs quantity 差异未讨论\n**W4** Human validation per-type CI 过宽（scopal [0.00, 1.00]，coreferential [0.00, 0.84]）\n**W5** Reproducibility ICC=0.919 仅在 OpenAI 家族内计算\n\n**小问题:**\n- Clause pair 示例缺失（应在 appendix 加 2-3 例）\n- 方差分解具体方法未说明（nested ANOVA? LMM?）\n- Error analysis κ=0.52 的 prevalence paradox 解释不能完全覆盖 moderate agreement\n- 60.8% residual 作为贡献列出不太恰当\n- Contribution (2) 中 \"60.8% residual\" 应 reframe\n\n**Questions:**\n- Q1: 是否考虑对全部 2,997 episodes 做 dual-judge evaluation？\n- Q2: 60.8% residual 主要由什么构成？user behavior 变异占比？\n- Q3: 排除 auth scope 后，剩余 5 type 的 cross-judge ranking ρ 是多少？\n- Q4: Coreferential 在 3 个 robustness check 中缺席，是否影响其作为 confound-free lower bound？"
  }
}
```

</details>

---


### Tool result

_source line 1177 · 2026-05-22T13:32:37.118348+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1361
}
```

</details>

---


### Assistant

_source line 1178 · 2026-05-22T13:32:41.280492+00:00_

交叉分享已发出，等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 110

## Round 110

2 recorded events


### User

_source line 1179 · 2026-05-22T13:32:43.887529+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

总结：评分 **Overall 3.5/5 (Borderline Conference)**，Soundness 3.5，Excitement 3。两个 Must-Fix：(1) Appendix P 的 cross-judge type ranking ρ=−0.03 需在主文正面讨论，当前仅埋在附录中，直接关系 C2 gradient 的可信度；(2) type 仅解释 0.4% 方差与论文 "Not All Policy Ambiguity Is Equal" 叙事之间的张力需要明确承认。五个 Should-Fix 涉及 SESOI margin-dependence、auth scope 低 κ 下的 C4 解读、incompleteness confound 控制粒度、per-type human validation CI 过宽、ICC 仅限 OpenAI 家族。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1180 · 2026-05-22T13:32:48.593592+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 111

## Round 111

2 recorded events


### User

_source line 1181 · 2026-05-22T13:33:58.889822+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 审稿意见的交叉回应

### Must-Fix

[AGREE] R2-N1: Type 仅解释 0.4% variance 与论文叙事的张力
- 与我的 N2 独立一致。补充：(1) Section 1 contribution (2) 将 60.8% residual 作为贡献列出在 framing 上有问题；(2) within-type clause variance (22.0%) 是 between-type (0.4%) 的 55 倍，type-level auditing 实用性存疑。两位 reviewer 独立发现同一问题，说明这是论文最需要在 revision 中解决的叙事问题。

[AGREE with nuance] R2-N2: Incompleteness confound 对 headline claims 影响过大
- 同意 Abstract 应加 confound caveat 或改用 confound-free range (+18.7 to +36.0)。但主文 Section 5.2 已标注 "upper bound—conditional on confound controls"，处理尚可。关键不足在 Abstract/Conclusion 的 framing 而非正文分析。Appendix O 的 authorization scope token delta (+36.1) > incompleteness (+34.6) 但违规率更低提供了有用的 counter-evidence，但论文未充分讨论 information *type* vs *quantity* 的区别。

### Should-Fix

[AGREE] R2-W1: Two-layer structure 缺乏经验支持——C3 inconclusive + Section 6 failure mechanisms crosscut layer boundary，layer 区分应降级为 "organizational convenience"。

[AGREE] R2-W2: OpenAI-family judge bias——与我的 N1 (cross-judge ρ = −0.03) 互补。补充：calibration sample 65% ambiguous 可能高估 judge 在 ambiguous condition 上的一致性。

[AGREE] R2-W3: Error Analysis κ=0.52——prevalence paradox 不提高 κ 本身可信度。R2 的 circularity risk 是好观点。Section 6 说 "LLM-coded traces" 但 reliability 基于 human coders——coding 中 LLM 的具体角色需澄清。

[AGREE] R2-W4: Disambiguation Neglect 定位——贡献在于扩展到 consequential agentic contexts，而非发现新的认知模式。

[AGREE] R2-W5: Domain generalizability framing 不一致——Abstract "policy-governed agent deployments" vs Conclusion "customer-service deployments" 应统一。

[AGREE] R2-W6: Margin-dependent gradient——与我的 W1 一致。Figure 2 给出过于确定的视觉印象。

### 缺失引用
四篇均认同相关，特别是 Stengel-Eskin et al. (TACL 2024) 对 scopal ambiguity 直接相关。

### R2 Questions
Q2 同意 C4 应重命名为 auth-scope-specific interaction。Q4 好问题，systematic nocuity 41.3% 可能在 7-model 下变化。Q5 与我的 Q4 一致——coreferential 作为 confound-free lower bound 的外部效度因 replication 缺席而受限。

### 两位 Reviewer 的共识
R1 和 R2 在以下问题上**完全独立一致**：
1. **0.4% type variance vs 论文叙事** (R1-N2 = R2-N1)
2. **SESOI/gradient margin dependence** (R1-W1 = R2-W6)  
3. **Cross-judge/OpenAI-family confound** (R1-N1 ≈ R2-W2)
4. **Incompleteness confound framing** (R1-W3 ≈ R2-N2)

这些共识性问题应是 revision 的优先事项。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1182 · 2026-05-22T13:34:08.566647+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 112

## Round 112

2 recorded events


### User

_source line 1183 · 2026-05-22T13:34:11.183407+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。总结：对 R2 的 2 个 Must-Fix 和 6 个 Should-Fix 全部标注 [AGREE]（N2 附带 nuance）。两位 Reviewer 在 4 个核心问题上完全独立一致：type variance 叙事张力、SESOI margin dependence、cross-judge confound、incompleteness confound framing。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1184 · 2026-05-22T13:34:15.199276+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 113

## Round 113

14 recorded events


### User

_source line 1185 · 2026-05-22T13:34:16.703042+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 交叉回应：Reviewer 1 审稿意见

---

### Must-Fix 回应

**[AGREE] R1-N1: Cross-judge type ranking ρ=−0.03 需在主文讨论**

同意这是一个 critical 问题。Appendix P 明确报告 "Type rankings show near-zero correlation across judge groups (Spearman ρ = −0.03, p = 0.96)"，并归因于 authorization scope 的 rank reversal（GPT-4.1-judged 组 rank 1 vs GPT-5.4-judged 组 rank 6）。论文的解释——agent composition 不同导致排序差异——虽然合理，但这恰恰说明 **C2 的 pooled type ranking 高度依赖 judge 组的 model 组成**。

补充我自己的发现：这个问题与我的 W2（LLM-as-judge + OpenAI-family bias）直接相关。当两个 judge 组对 type severity 的排序完全不一致时，pooled ranking 实际上是一个加权平均，其中 GPT-5.4 judged 3 个模型、GPT-4.1 judged 2 个模型，形成 3:2 权重。R1 指出的这个 weighting dependency 是准确的。

不过我要补充一个 nuance：Appendix P 同时指出 "Incompleteness ranks 1–2 in both groups"，说明 incompleteness 作为 upper bound 的结论在两个 judge 组内都成立。所以 C2 的 **核心发现**（incompleteness 最高）是 robust 的，但 **mid-tier 内部排序** 不稳定。建议作者在 §5.2 区分这两层结论的 robustness level。

---

**[AGREE] R1-N2: Type 仅解释 0.4% 方差与论文叙事张力**

完全同意。这与我自己的 N1 是同一问题——我在独立审查中也将其列为 Must-Fix #1。

两位 reviewer 独立识别出同一核心张力，进一步确认这不是 stylistic preference 而是 substantive concern。论文需要正面回答一个问题：如果 type 仅解释 0.4% variance，**taxonomy 的价值体现在哪里？**

我的建议与 R1 一致：(a) Discussion 需要正面处理这个张力；(b) 将 framing 从 "type predicts risk" 调整为更准确的定位，比如 "type identifies structural categories of risk, but clause-level wording dominates within-category variation"；(c) 强调 taxonomy 的价值可能不在于 prediction 而在于 **intervention design**（不同 type 需要不同的 mitigation strategy，§7 mitigation experiment 提供了初步证据）。

---

### Should-Fix 回应

**[AGREE] R1-W1: SESOI ±15pp 论证不足**

同意 bootstrap k=2 重现率 34.3% 较低，这意味着 incompleteness singleton 不是一个 overwhelmingly stable partition。但我对 R1 的批评做一个 partial rebut：

论文在 §4.6 确实提供了 domain anchoring："a 15 pp violation-rate increase on a policy type would trigger a different audit and remediation strategy, making this margin operationally meaningful"。这不是任意选择——±15pp 是一个合理的 practical significance threshold。问题不在于 ±15pp 本身，而在于论文没有充分讨论 **margin sensitivity**：在 ±10pp 时结构不稳定（3/6），在 ±15pp 才稳定（6/6）。Appendix A 的 sensitivity table 提供了完整数据，但正文对此讨论不够。

建议：在 §5.2 增加 1-2 句明确说明 gradient 结构的 margin-dependency，而非仅在 Appendix A 展示。

---

**[AGREE] R1-W2: Auth scope κ=0.385 驱动 C4 但 reliability 最低**

同意。这与我的 W2 一致。Figure 3 heatmap 中 authorization scope 的 52pp range 视觉上非常显眼，但 κ=0.385 意味着这个 type 的 violation classification 一致性最低。论文在 §5.4 确实提到了 "so absolute rates carry more uncertainty than for other types"，但这个 caveat 在 figure caption 中不可见，读者容易被 heatmap 的视觉印象误导。

补充：Appendix N 显示排除 auth scope 后 C4 interaction 完全消失（p=0.97），这进一步说明 C4 基本上是一个 auth-scope-specific 现象，而非 general model×type interaction。建议在 §5.4 明确将 C4 定位为 "authorization-scope-specific interaction" 而非一般性 model×type interaction。

---

**[AGREE] R1-W3: Incompleteness confound — information quality vs quantity**

同意。这与我的 N2 相关。Token count 只能衡量 information quantity，不能衡量 information quality（e.g., 一条高信息密度的 boundary clause 可能仅增加 10 tokens 但改变语义极大）。论文自己在 Appendix F 承认 "finer-grained semantic measures (e.g., propositional content analysis) may reveal different confound structures"。

不过我要 partially rebut R1：Appendix O（clause length analysis）提供了一个有说服力的反证——authorization scope 有最大的 token delta（+36.1 words）但 violation rate 低于 incompleteness（+34.6 words delta），说明 token count 不是 violation rate 的主要驱动因素。这个 counter-evidence 值得在正文提及，而非仅在 Appendix 中。

---

**[AGREE] R1-W4: Per-type CI 过宽**

同意这是一个事实性问题。Appendix G 的 scopal κ CI [0.00, 1.00] 确实 uninformative。但论文在 Appendix G 末段明确说 "Per-type estimates are imprecise due to small cell sizes (n = 32–34); they are descriptive statistics only and should not be used for type-level reliability ranking or inference"。

所以论文并未基于 per-type κ 做任何 inferential claim——这些数字是 descriptive reporting。问题在于报告了这些数字却没有充分讨论其含义。建议：要么不报告这些 uninformative CIs（如果不做推断），要么增加 sample size 使其有意义。

---

**[REBUT] R1-W5: Reproducibility ICC=0.919 仅在 OpenAI 家族内**

部分反驳。§4.5 的 ICC 测试是关于 **同一模型在相同输入上的 replicability**（run-to-run variance），不是 cross-provider 一致性。这个 ICC 的目的是验证实验本身是否可重复——即温度设置（temperature=0）是否有效消除了随机性。对于这个目的，在任意一组模型上测试即可。

但 R1 的 underlying concern 是合理的：如果 ICC 只在 OpenAI 模型上测试，我们不知道其他 provider 的模型（如 DeepSeek, Qwen3）是否有更高的 run-to-run variance。论文说 "cross-provider stability is 1.0\% for model identity"（§5.1），但这是 between-model variance，不是 within-model run-to-run variance。

建议：在 Limitations 中承认 ICC 的 scope 限制，或在 Appendix 报告 1-2 个非 OpenAI 模型的 replicability check。

---

### 小问题回应

- **Clause pair 示例缺失**：[AGREE] 这是一个易修复且高价值的改进。读者需要看到实际的 ambiguous/unambiguous clause pair 才能直观理解 taxonomy。建议 Appendix 加 Table 展示每种 type 一个示例对。
- **方差分解方法未说明**：[AGREE] 0.4% type / 22.4% clause / 1.0% model / 60.8% residual 的分解方法（nested ANOVA? random-effects LMM? ICC decomposition?）应在 §5.1 或 Appendix 明确说明。
- **Error analysis κ=0.52 的 prevalence paradox 解释**：[AGREE] 论文用 prevalence paradox 解释 κ 和 Gwet's AC₁ 的 gap，但 AC₁=0.62 仍只是 substantial，三个低频类别的 reliability 可能更低。
- **60.8% residual 作为 contribution**：[AGREE] §1 contribution (2) 中列出 "60.8% residual" 确实不太恰当——residual variance 是一个观测结果，不是 contribution。建议重新表述。
- **Contribution (2) reframe**：[AGREE] 同上。

---

### R1 Questions 的补充意见

**Q1（dual-judge evaluation）**：我认为 dual-judge 是 gold standard 但可能不 feasible（2,997 episodes × 2 judges = ~6000 API calls），可以先在 stratified sample 上做（论文已做了 100-episode human validation）。更实际的建议是 cross-family judge（e.g., Claude judging GPT traces）来解决 OpenAI-family bias。

**Q2（60.8% residual 构成）**：好问题。τ²-bench 的 conversational dynamics（user behavior 随机性、对话轮次差异、tool-call 顺序）可能贡献了大部分 residual。论文应讨论 residual 的可能组成。

**Q3（排除 auth scope 后 cross-judge ρ）**：这是一个 critical 的诊断性分析。如果排除 auth scope 后 ρ 显著提高，则进一步证实 auth scope 是 cross-judge inconsistency 的主要来源。

**Q4（Coreferential 在 robustness checks 中缺席）**：有效关切。Coreferential 被排除在 mitigation（Appendix B）和 replication（Appendix E）之外，但被用作 confound-free lower bound（Appendix F）。这意味着 lower bound 没有经过 replication 验证——是一个 gap。

---

### 总结

R1 和我的审稿在两个核心问题上完全一致：**(1) 0.4% type variance 与论文叙事的张力，(2) judge/measurement reliability 对 C2/C4 的影响。** R1 的 N1（cross-judge ρ=−0.03）是我审稿中没有独立提出的有力补充——它从另一个角度揭示了 C2 的 fragility。两份审稿共同指向一个建议：**论文的方法论贡献（matched-pair causal design）是扎实的，但 taxonomy 的叙事需要更谨慎的定位。**

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1186 · 2026-05-22T13:34:41.562790+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '检查论文资料完整性并调研 EMNLP 2026 venue 要求'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.7: 派发视觉审查', 'status': 'completed', 'activeForm': '派发视觉审查 Agent'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'completed', 'activeForm': '收集 Reviewer 独立审稿结果'}, {'content': 'Step 2: 交叉分享', 'status': 'completed', 'activeForm': 'Reviewer 交叉分享与回应'}, {'content': 'Step 3: 收敛判断', 'status': 'completed', 'activeForm': '判断审稿意见收敛性'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'in_progress', 'activeForm': '汇总审稿报告并投递'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '检查论文资料完整性并调研 EMNLP 2026 venue 要求'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.7: 派发视觉审查', 'status': 'completed', 'activeForm': '派发视觉审查 Agent'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'completed', 'activeForm': '收集 Reviewer 独立审稿结果'}, {'content': 'Step 2: 交叉分享', 'status': 'completed', 'activeForm': 'Reviewer 交叉分享与回应'}, {'content': 'Step 3: 收敛判断', 'status': 'completed', 'activeForm': '判断审稿意见收敛性'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'in_progress', 'activeForm': '汇总审稿报告并投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 1187 · 2026-05-22T13:34:41.613473+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "TodoWrite",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1188 · 2026-05-22T13:34:47.536317+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "policy_ambiguity_safety"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "policy_ambiguity_safety"
  }
}
```

</details>

---


### Tool result

_source line 1189 · 2026-05-22T13:34:47.687502+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-22T13:23:36.399947+00:00\", \"completed_at\": \"2026-05-22T13:26:10.627727+00:00\", \"findings\": [{\"severity\": \"info\", \"dimension\": \"page 1\", \"message\": \"首页为纯文本（Title + Abstract + Introduction），无视觉锚点。Figure 1 出现在第 2 页顶部，属于前 3 页内，可接受。\"}, {\"severity\": \"info\", \"dimension\": \"page 2\", \"message\": \"Figure 1（实验流程总览图）跨双栏全宽，caption 自包含，清晰传达三阶段实验设计。图内小方框文字（模型名、数字）偏小，约为正文字号 60%，在打印时可能需要细看。整体信息传达良好，作为审稿人第一视觉锚点合格。\"}, {\"severity\": \"info\", \"dimension\": \"page 3\", \"message\": \"Table 1（六类歧义分类）使用 booktabs 风格，格式规范。列头清晰，行间距合理。Layout 与 taxonomy 描述文字自然衔接。\"}, {\"severity\": \"warning\", \"dimension\": \"page 4-5\", \"message\": \"连续两页纯文本（Section 4 Method 全部 + Section 4.5-4.6 + Statistical Analysis 开头 + Section 5 Results 开头），无任何 display item。虽然是方法论描述，但插入一个公式展示（如 matched-pair design 的形式化定义或统计检验公式）可打破视觉单调。\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"Table 2（全宽，violation rates by type and model）+ Figure 2（右栏，type-specific effect sizes 热力图）同页出现，视觉密度良好。Table 2 使用 booktabs，最优值已加粗。Figure 2 热力图颜色区分度可接受，但 cell 内数字和 axis label 字号偏小。\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Figure 3（violation rates 热力图，含 5 模型 × 6 类型）位于左栏上方，右栏为文字分析。热力图 cell 内标注数字清晰可读，颜色从浅到深渐变合理。caption 自包含。\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"纯文本页（Section 6.2 Disambiguation Neglect, 6.3 Systematic Novelty, Section 7 Discussion, Section 8 Conclusion）。作为讨论+结论页，纯文本可接受，且前后页（p7 有 Figure 3，p9 开始 References）提供了视觉节奏缓冲。\"}, {\"severity\": \"info\", \"dimension\": \"page 9\", \"message\": \"Limitations 段落简短精炼（约 1/3 页），Data and Code Availability 含 GitHub 链接，References 从页面中部开始。符合 EMNLP 格式要求——主体正文在第 8 页结束，Limitations 不计入页数限制。\"}, {\"severity\": \"info\", \"dimension\": \"page 9-10\", \"message\": \"参考文献格式统一，未见 [?] 未解析引用，无明显 overfull hbox。作者名缩写风格一致。\"}, {\"severity\": \"info\", \"dimension\": \"page 11\", \"message\": \"Appendix A（Table
…[truncated 736 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 1190 · 2026-05-22T13:34:47.687865+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "policy_ambiguity_safety"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "policy_ambiguity_safety"
  }
}
```

</details>

---


### Tool result

_source line 1191 · 2026-05-22T13:34:47.738306+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1192 · 2026-05-22T13:37:14.658536+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "policy_ambiguity_safety",
  "issues_yaml": "## Review Issues Tracker — policy_ambiguity_safety\n## Paper: \"Not All Policy Ambiguity Is Equal: Type-Specific Safety Risks for LLM Agents\"\n## Venue: EMNLP 2026 via ARR May cycle\n## Latest Round: 13 (fresh review, both reviewers 3.5 Borderline Conference)\n\n# ============================================================\n# CRITICAL ISSUES\n# ============================================================\n\n- id: \"R11-C1\"\n  summary: \"Type 仅解释 0.4% variance 与论文标题/核心叙事的根本张力\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 11\n  last_seen_round: 13\n  mentions:\n    - round: 11\n      reviewers: [R2, R1]\n      note: \"W6. clause_within_type=22.0% vs ambiguity_type=0.4%\"\n    - round: 12\n      reviewers: [R2, R1]\n      note: \"MF-1. 22× 放在 contributions list 紧跟 C2, 读者误读为 taxonomy 解释力\"\n    - round: 13\n      reviewers: [R1, R2]\n      note: \"R13 fresh review: 两位 Reviewer 独立将此列为 Must-Fix #1。标题 'Not All Policy Ambiguity Is Equal' 暗示 type 是强预测因子，但 type 0.4% vs clause 22.4% (55×)。知道 clause 属于哪种 type 几乎不增加预测力。R1: type-level interventions 实用性存疑；R2: taxonomy 价值需重新定位为 intervention design 而非 prediction。两位 Reviewer 完全一致 [AGREE]。\"\n  action_items:\n    - round: 13\n      action: \"(1) §5.1 正面讨论 0.4% 对 taxonomy 实用价值的含义; (2) Discussion 加段落解释 taxonomy 价值在于 intervention design 而非 prediction; (3) 考虑调整标题/framing 更准确反映效应量级; (4) §1 contribution(2) 中 '60.8% residual' 不应作为贡献列出\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-C1\"\n  summary: \"Cross-judge type ranking ρ=−0.03 需在主文正面讨论，直接关系 C2 gradient 可信度\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [R1, R2]\n      note: \"R1 独立提出为 Must-Fix, R2 交叉回应 [AGREE]。Appendix P: Spearman ρ=−0.03 (p=0.96), 两个 judge 组对 type severity 排序完全不一致。Judge bias 和 model composition 无法分离。GPT-5.4 judged 3 models vs GPT-4.1 judged 2 models 形成 3:2 权重依赖。R2 补充: incompleteness ranks 1-2 in both groups (核心发现 robust), 但 mid-tier 内部排序不稳定。\"\n  action_items:\n    - round: 13\n      action: \"(1) §5.2 正文中正面讨论 ρ=−0.03; (2) 区分 C2 核心发现 (incompleteness upper bound, robust) vs mid-tier 排序 (不稳定); (3) 分别报告两组内的 type gradient 结构; (4) Limitations 中列为最主要 measurement limitation\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# WARNING ISSUES\n# ============================================================\n\n- id: \"R12-W1\"\n  summary: \"Incompleteness information-addition confound 在 Abstract/Conclusion 中应更显式标注为 upper bound\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 13\n  mentions:\n    - round: 12\n      reviewers: [R1, R2]\n      note: \"MF-4. token count OR=1.022/token, ~35 tokens 累积 ~2.15× odds multiplier\"\n    - round: 13\n      reviewers: [R1, R2]\n      note: \"R2 列为 Must-Fix, R1 [AGREE with nuance]: 主文 §5.2 已标注 upper bound, 但 Abstract/Conclusion 仍用 +49.2pp 无 caveat。Token count 是粗糙代理, information quality vs quantity 差异未讨论。Auth scope +36.1 words > incompleteness +34.6 但违规率更低是有力反证, 应提升到正文。\"\n  action_items:\n    - round: 13\n      action: \"(1) Abstract/Conclusion 明确标注 49.2pp 为 upper bound conditional on confound; (2) 正文报告 confound-free range (+18.7 to +36.0); (3) 讨论 information quality vs quantity 差异; (4) 将 auth scope token delta 反证提升到正文\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-C2\"\n  summary: \"C2 risk gradient margin-dependent — SESOI ±15pp 论证需加强，gradient 结构不稳定\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 13\n  mentions:\n    - round: 12\n      reviewers: [R1, R2]\n      note: \"MF-2. gradient 在 ±15pp 成立(6/6)但 ±10pp 仅 3/6\"\n    - round: 13\n      reviewers: [R1, R2]\n      note: \"R1 W1 + R2 W6, 交叉 [AGREE]。Bootstrap k=2 重现率仅 34.3%。Figure 2 给出过于确定的 gradient 印象。R2: ±15pp domain anchoring 合理, 但 margin sensitivity 在正文讨论不够。\"\n  action_items:\n    - round: 13\n      action: \"(1) §5.2 显式提及 gradient 结构 margin-dependent; (2) 报告 ±10pp/±12pp 下的结构作为 sensitivity check; (3) Figure 2 caption 标注 margin-dependency; (4) 更谨慎描述 bootstrap 结果\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-C1\"\n  summary: \"Authorization scope κ=0.385 + C4 interaction 完全集中于此 type\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 13\n  mentions:\n    - round: 12\n      reviewers: [R1, R2]\n      note: \"MF-3. within-judge range 34pp vs 4pp\"\n    - round: 13\n      reviewers: [R1, R2]\n      note: \"R1 W2 + R2 W2, 交叉 [AGREE]。Figure 3 heatmap 52pp range 视觉印象强, reliability caveat 不可见。排除 auth scope 后 C4 p=0.97 (Appendix N)。建议重定位 C4 为 auth-scope-specific interaction。\"\n  action_items:\n    - round: 13\n      action: \"(1) Figure 3 caption 显著标注 auth scope reliability caveat; (2) §5.4 将 C4 定位为 authorization-scope-specific interaction; (3) 考虑报告 measurement-noise-adjusted range\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-W1\"\n  summary: \"Two-layer structure (linguistic vs specification) 缺乏经验支持, 应降级为 organizational convenience\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 9\n  last_seen_round: 13\n  mentions:\n    - round: 12\n      reviewers: [R2, R1]\n      note: \"SF-1. §3 讨论充分但 scope 限定来得太晚\"\n    - round: 13\n      reviewers: [R2, R1]\n      note: \"R2 W1, R1 交叉 [AGREE]。C3 inconclusive + §6 failure mechanisms crosscut layer boundary。Layer 区分应降级为 organizational convenience 而非理论假设。\"\n  action_items:\n    - round: 13\n      action: \"降级 two-layer structure 为 organizational convenience; Discussion 分析为什么假设不成立\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-W6\"\n  summary: \"Cross-judge 设计 + judge family bias (both OpenAI) 对跨模型比较的系统性威胁\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 13\n  mentions:\n    - round: 12\n      reviewers: [R1, R2]\n      note: \"SF-5. Claude 30.3% 最低可能反映真实 robustness 或 judge bias\"\n    - round: 13\n      reviewers: [R1, R2]\n      note: \"R2 W2, R1 N1 互补。R1: calibration sample 65% ambiguous 可能高估一致性。与 R13-C1 (ρ=−0.03) 直接关联。\"\n  action_items:\n    - round: 13\n      action: \"(1) 讨论 judge family bias 可能方向; (2) Future Work 推荐 cross-family judge evaluation; (3) 标注 calibration sample 组成\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-W1\"\n  summary: \"Error Analysis §6 LLM-coded failure modes 存在 circularity risk, κ=0.52 moderate\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [R2, R1]\n      note: \"R2 W3, R1 交叉 [AGREE]。LLM 编码 LLM 的 failure modes 有 circularity risk。Gwet AC₁=0.62 仍只是 substantial。Prevalence paradox 不能完全解释 moderate κ。R1 补充: §6 说 'LLM-coded traces' 但 reliability 基于什么 coders 需澄清。\"\n  action_items:\n    - round: 13\n      action: \"(1) 讨论 LLM-coding circularity risk; (2) 至少一个 failure mode 类别报告人工编码对照; (3) 澄清 coding 中 LLM 的具体角色; (4) 承认 failure mode coding 可靠性限制\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-W4\"\n  summary: \"Disambiguation Neglect 新颖性定位需要更准确 — agentic vs non-agentic 区别在于 consequentiality\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 13\n  mentions:\n    - round: 12\n      reviewers: [R2, R1]\n      note: \"SF-3. 'revealing' → 'quantifying in consequential agentic settings'\"\n    - round: 13\n      reviewers: [R2, R1]\n      note: \"R2 W4, R1 交叉 [AGREE]。'extends to agentic settings' 的 novelty 需论证为什么 agentic settings 不同。关键区别在于 consequentiality (执行动作 vs 仅生成文本), 但论文未显式展开。\"\n  action_items:\n    - round: 13\n      action: \"§6.2 或 Discussion 明确阐述 agentic vs non-agentic 区别在于 consequentiality\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R12-W3\"\n  summary: \"Domain generalizability framing — Abstract vs Conclusion 措辞不一致\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 13\n  mentions:\n    - round: 12\n      reviewers: [R2, R1]\n      note: \"SF-8. Abstract 用 'LLM-based agents' 无 domain 限定\"\n    - round: 13\n      reviewers: [R2, R1]\n      note: \"R2 W5, R1 交叉 [AGREE]。Abstract 'policy-governed agent deployments' vs Conclusion 'customer-service deployments' 不一致。两个 domain (retail + airline) 不足以支撑 'cross-domain consistency' 声明。\"\n  action_items:\n    - round: 13\n      action: \"统一 Abstract 和 Conclusion 的 scope 措辞, 添加 domain qualifier\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-W5\"\n  summary: \"Per-type 人工验证 CI 过宽 (scopal [0.00, 1.00], coreferential [0.00, 0.84])\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 13\n  mentions:\n    - round: 12\n      reviewers: [R1, R2]\n      note: \"SF-4. Appendix G 仍报告 per-type κ 并得出 type-level 结论\"\n    - round: 13\n      reviewers: [R1, R2]\n      note: \"R1 W4, R2 交叉 [AGREE]。Per-type κ 应为 descriptive only, 但 Appendix G 仍做 type-level 推断。建议: 要么不报告 uninformative CIs, 要么增加 sample size。\"\n  action_items:\n    - round: 13\n      action: \"Appendix G 明确 per-type 结果仅为 descriptive, 不用于 type-level ranking\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-W2\"\n  summary: \"Reproducibility ICC=0.919 仅在 OpenAI 家族内计算, cross-provider replicability 未验证\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [R1, R2]\n      note: \"R1 W5, R2 partial [REBUT]: ICC 目的是 run-to-run replicability 而非 cross-provider consistency, 在任一模型组上测试即可。但 underlying concern 合理: 不知道非 OpenAI 模型的 run-to-run variance。\"\n  action_items:\n    - round: 13\n      action: \"Limitations 中承认 ICC scope 限制, 或报告 1-2 个非 OpenAI 模型的 replicability check\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# MINOR ISSUES\n# ============================================================\n\n- id: \"R12-M1\"\n  summary: \"4.6% vs ≤11% disambiguation awareness 数字交替使用\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 12\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [R2]\n      note: \"R2 小问题: §1 和 §6.2 交替出现。建议统一使用一个数字, 首次出现时注明另一个。\"\n  action_items:\n    - round: 13\n      action: \"统一使用, 首次出现时注明另一个\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-M1\"\n  summary: \"缺失引用: Stengel-Eskin et al. (TACL 2024) scope ambiguity, pragmatic competence 方向\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [R2, R1]\n      note: \"R2 识别, R1 交叉 [AGREE]。Stengel-Eskin et al. (TACL 2024) 对 scopal type 直接相关。另: 'To Know or Not To Know' (2024), Hu et al. 2022 on implicature, Ruis et al. 2024 on pragmatic understanding。\"\n  action_items:\n    - round: 13\n      action: \"补充 4 篇相关引用\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-M2\"\n  summary: \"Clause pair 示例缺失, 方差分解方法未说明, §1 contribution(2) residual 表述不当\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [R1, R2]\n      note: \"R1 小问题, R2 交叉全部 [AGREE]。(1) Appendix 应加每种 type 一个 clause pair 示例; (2) §5.1 方差分解方法 (nested ANOVA? LMM?) 未说明; (3) 60.8% residual 不应作为 contribution 列出。\"\n  action_items:\n    - round: 13\n      action: \"(1) Appendix 加 clause pair 示例表; (2) §5.1 说明方差分解方法; (3) Contribution(2) reframe residual\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-M6\"\n  summary: \"Pages 4-5 连续纯文本无 display item\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 9\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: []\n      note: \"Visual check R13: Page 4-5 连续两页纯文本 (§4 Method), 仍无 display item。低优先级, 页面预算紧张。\"\n  action_items:\n    - round: 13\n      action: \"低优先级——可考虑插入公式或 matched-pair design 简图\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R12-W4\"\n  summary: \"Mitigation 实验方向矛盾 — incompleteness prompt sensitivity (v1: -3.4pp vs v2: +14pp)\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 11\n  last_seen_round: 13\n  mentions:\n    - round: 12\n      reviewers: [R2, R1]\n      note: \"SF-2. 同模型同类型, 换 prompt 方向相反\"\n    - round: 13\n      reviewers: [R2]\n      note: \"R2 Q3: prompt sensitivity 是否 undermine practical recommendation (type-specific mitigation)?\"\n  action_items:\n    - round: 13\n      action: \"讨论 prompt sensitivity 本身作为 finding; 标注两个实验设计差异\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-M2\"\n  summary: \"引用问题: ferrari 作者不一致 + orphan entries\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 8\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: []\n      note: \"本轮未单独提及, 可能已修复, 待确认。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# PREVIOUSLY RESOLVED\n# ============================================================\n\n- id: \"R11-M13\"\n  summary: \"Coreferential 排除在 mitigation/replication 中已在 Limitations 提及\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 12\n  resolution: \"Limitations 已明确声明 coreferential exclusion 及原因\"\n  resolution_round: 12\n\n- id: \"R10-W4-resolved\"\n  summary: \"Disambiguation Deficit → Neglect 术语统一\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 11\n  resolution: \"Round 11 全文统一为 Disambiguation Neglect\"\n  resolution_round: 11\n\n- id: \"R8-W1-resolved\"\n  summary: \"缺少 API 超参数报告\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 10\n  resolution: \"§4.3 添加完整 API 超参数\"\n  resolution_round: 9\n\n- id: \"R8-W4-resolved\"\n  summary: \"无代码/数据可用性声明\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 10\n  resolution: \"添加 Data and Code Availability section\"\n  resolution_round: 9\n\n- id: \"R9-W7-resolved\"\n  summary: \"多重比较校正 three test families 未明确定义\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  resolution: \"Appendix L 新增 Multiple Comparison Correction 小节\"\n  resolution_round: 10\n\n- id: \"R9-W8-resolved\"\n  summary: \"与 DRIP-R 的 taxonomy type-level 映射缺失\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  resolution: \"Appendix L 有 DRIP-R mapping\"\n  resolution_round: 10\n\n- id: \"R9-M3-resolved\"\n  summary: \"Introduction 'seven models' 措辞应区分 main study (5) vs replication (2)\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  resolution: \"措辞已修正\"\n  resolution_round: 10\n\n- id: \"R9-M7-resolved\"\n  summary: \"§5.4 F(20) 缺少 denominator df\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  resolution: \"F(20) → F(20, 2976)\"\n  resolution_round: 10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "policy_ambiguity_safety",
    "issues_yaml": "## Review Issues Tracker — policy_ambiguity_safety\n## Paper: \"Not All Policy Ambiguity Is Equal: Type-Specific Safety Risks for LLM Agents\"\n## Venue: EMNLP 2026 via ARR May cycle\n## Latest Round: 13 (fresh review, both reviewers 3.5 Borderline Conference)\n\n# ============================================================\n# CRITICAL ISSUES\n# ============================================================\n\n- id: \"R11-C1\"\n  summary: \"Type 仅解释 0.4% variance 与论文标题/核心叙事的根本张力\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 11\n  last_seen_round: 13\n  mentions:\n    - round: 11\n      reviewers: [R2, R1]\n      note: \"W6. clause_within_type=22.0% vs ambiguity_type=0.4%\"\n    - round: 12\n      reviewers: [R2, R1]\n      note: \"MF-1. 22× 放在 contributions list 紧跟 C2, 读者误读为 taxonomy 解释力\"\n    - round: 13\n      reviewers: [R1, R2]\n      note: \"R13 fresh review: 两位 Reviewer 独立将此列为 Must-Fix #1。标题 'Not All Policy Ambiguity Is Equal' 暗示 type 是强预测因子，但 type 0.4% vs clause 22.4% (55×)。知道 clause 属于哪种 type 几乎不增加预测力。R1: type-level interventions 实用性存疑；R2: taxonomy 价值需重新定位为 intervention design 而非 prediction。两位 Reviewer 完全一致 [AGREE]。\"\n  action_items:\n    - round: 13\n      action: \"(1) §5.1 正面讨论 0.4% 对 taxonomy 实用价值的含义; (2) Discussion 加段落解释 taxonomy 价值在于 intervention design 而非 prediction; (3) 考虑调整标题/framing 更准确反映效应量级; (4) §1 contribution(2) 中 '60.8% residual' 不应作为贡献列出\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-C1\"\n  summary: \"Cross-judge type ranking ρ=−0.03 需在主文正面讨论，直接关系 C2 gradient 可信度\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [R1, R2]\n      note: \"R1 独立提出为 Must-Fix, R2 交叉回应 [AGREE]。Appendix P: Spearman ρ=−0.03 (p=0.96), 两个 judge 组对 type severity 排序完全不一致。Judge bias 和 model composition 无法分离。GPT-5.4 judged 3 models vs GPT-4.1 judged 2 models 形成 3:2 权重依赖。R2 补充: incompleteness ranks 1-2 in both groups (核心发现 robust), 但 mid-tier 内部排序不稳定。\"\n  action_items:\n    - round: 13\n      action: \"(1) §5.2 正文中正面讨论 ρ=−0.03; (2) 区分 C2 核心发现 (incompleteness upper bound, robust) vs mid-tier 排序 (不稳定); (3) 分别报告两组内的 type gradient 结构; (4) Limitations 中列为最主要 measurement limitation\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# WARNING ISSUES\n# ============================================================\n\n- id: \"R12-W1\"\n  summary: \"Incompleteness information-addition confound 在 Abstract/Conclusion 中应更显式标注为 upper bound\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 13\n  mentions:\n    - round: 12\n      reviewers: [R1, R2]\n      note: \"MF-4. token count OR=1.022/token, ~35 tokens 累积 ~2.15× odds multiplier\"\n    - round: 13\n      reviewers: [R1, R2]\n      note: \"R2 列为 Must-Fix, R1 [AGREE with nuance]: 主文 §5.2 已标注 upper bound, 但 Abstract/Conclusion 仍用 +49.2pp 无 caveat。Token count 是粗糙代理, information quality vs quantity 差异未讨论。Auth scope +36.1 words > incompleteness +34.6 但违规率更低是有力反证, 应提升到正文。\"\n  action_items:\n    - round: 13\n      action: \"(1) Abstract/Conclusion 明确标注 49.2pp 为 upper bound conditional on confound; (2) 正文报告 confound-free range (+18.7 to +36.0); (3) 讨论 information quality vs quantity 差异; (4) 将 auth scope token delta 反证提升到正文\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-C2\"\n  summary: \"C2 risk gradient margin-dependent — SESOI ±15pp 论证需加强，gradient 结构不稳定\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 13\n  mentions:\n    - round: 12\n      reviewers: [R1, R2]\n      note: \"MF-2. gradient 在 ±15pp 成立(6/6)但 ±10pp 仅 3/6\"\n    - round: 13\n      reviewers: [R1, R2]\n      note: \"R1 W1 + R2 W6, 交叉 [AGREE]。Bootstrap k=2 重现率仅 34.3%。Figure 2 给出过于确定的 gradient 印象。R2: ±15pp domain anchoring 合理, 但 margin sensitivity 在正文讨论不够。\"\n  action_items:\n    - round: 13\n      action: \"(1) §5.2 显式提及 gradient 结构 margin-dependent; (2) 报告 ±10pp/±12pp 下的结构作为 sensitivity check; (3) Figure 2 caption 标注 margin-dependency; (4) 更谨慎描述 bootstrap 结果\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-C1\"\n  summary: \"Authorization scope κ=0.385 + C4 interaction 完全集中于此 type\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 13\n  mentions:\n    - round: 12\n      reviewers: [R1, R2]\n      note: \"MF-3. within-judge range 34pp vs 4pp\"\n    - round: 13\n      reviewers: [R1, R2]\n      note: \"R1 W2 + R2 W2, 交叉 [AGREE]。Figure 3 heatmap 52pp range 视觉印象强, reliability caveat 不可见。排除 auth scope 后 C4 p=0.97 (Appendix N)。建议重定位 C4 为 auth-scope-specific interaction。\"\n  action_items:\n    - round: 13\n      action: \"(1) Figure 3 caption 显著标注 auth scope reliability caveat; (2) §5.4 将 C4 定位为 authorization-scope-specific interaction; (3) 考虑报告 measurement-noise-adjusted range\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-W1\"\n  summary: \"Two-layer structure (linguistic vs specification) 缺乏经验支持, 应降级为 organizational convenience\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 9\n  last_seen_round: 13\n  mentions:\n    - round: 12\n      reviewers: [R2, R1]\n      note: \"SF-1. §3 讨论充分但 scope 限定来得太晚\"\n    - round: 13\n      reviewers: [R2, R1]\n      note: \"R2 W1, R1 交叉 [AGREE]。C3 inconclusive + §6 failure mechanisms crosscut layer boundary。Layer 区分应降级为 organizational convenience 而非理论假设。\"\n  action_items:\n    - round: 13\n      action: \"降级 two-layer structure 为 organizational convenience; Discussion 分析为什么假设不成立\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-W6\"\n  summary: \"Cross-judge 设计 + judge family bias (both OpenAI) 对跨模型比较的系统性威胁\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 13\n  mentions:\n    - round: 12\n      reviewers: [R1, R2]\n      note: \"SF-5. Claude 30.3% 最低可能反映真实 robustness 或 judge bias\"\n    - round: 13\n      reviewers: [R1, R2]\n      note: \"R2 W2, R1 N1 互补。R1: calibration sample 65% ambiguous 可能高估一致性。与 R13-C1 (ρ=−0.03) 直接关联。\"\n  action_items:\n    - round: 13\n      action: \"(1) 讨论 judge family bias 可能方向; (2) Future Work 推荐 cross-family judge evaluation; (3) 标注 calibration sample 组成\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-W1\"\n  summary: \"Error Analysis §6 LLM-coded failure modes 存在 circularity risk, κ=0.52 moderate\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [R2, R1]\n      note: \"R2 W3, R1 交叉 [AGREE]。LLM 编码 LLM 的 failure modes 有 circularity risk。Gwet AC₁=0.62 仍只是 substantial。Prevalence paradox 不能完全解释 moderate κ。R1 补充: §6 说 'LLM-coded traces' 但 reliability 基于什么 coders 需澄清。\"\n  action_items:\n    - round: 13\n      action: \"(1) 讨论 LLM-coding circularity risk; (2) 至少一个 failure mode 类别报告人工编码对照; (3) 澄清 coding 中 LLM 的具体角色; (4) 承认 failure mode coding 可靠性限制\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-W4\"\n  summary: \"Disambiguation Neglect 新颖性定位需要更准确 — agentic vs non-agentic 区别在于 consequentiality\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 13\n  mentions:\n    - round: 12\n      reviewers: [R2, R1]\n      note: \"SF-3. 'revealing' → 'quantifying in consequential agentic settings'\"\n    - round: 13\n      reviewers: [R2, R1]\n      note: \"R2 W4, R1 交叉 [AGREE]。'extends to agentic settings' 的 novelty 需论证为什么 agentic settings 不同。关键区别在于 consequentiality (执行动作 vs 仅生成文本), 但论文未显式展开。\"\n  action_items:\n    - round: 13\n      action: \"§6.2 或 Discussion 明确阐述 agentic vs non-agentic 区别在于 consequentiality\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R12-W3\"\n  summary: \"Domain generalizability framing — Abstract vs Conclusion 措辞不一致\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 13\n  mentions:\n    - round: 12\n      reviewers: [R2, R1]\n      note: \"SF-8. Abstract 用 'LLM-based agents' 无 domain 限定\"\n    - round: 13\n      reviewers: [R2, R1]\n      note: \"R2 W5, R1 交叉 [AGREE]。Abstract 'policy-governed agent deployments' vs Conclusion 'customer-service deployments' 不一致。两个 domain (retail + airline) 不足以支撑 'cross-domain consistency' 声明。\"\n  action_items:\n    - round: 13\n      action: \"统一 Abstract 和 Conclusion 的 scope 措辞, 添加 domain qualifier\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-W5\"\n  summary: \"Per-type 人工验证 CI 过宽 (scopal [0.00, 1.00], coreferential [0.00, 0.84])\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 13\n  mentions:\n    - round: 12\n      reviewers: [R1, R2]\n      note: \"SF-4. Appendix G 仍报告 per-type κ 并得出 type-level 结论\"\n    - round: 13\n      reviewers: [R1, R2]\n      note: \"R1 W4, R2 交叉 [AGREE]。Per-type κ 应为 descriptive only, 但 Appendix G 仍做 type-level 推断。建议: 要么不报告 uninformative CIs, 要么增加 sample size。\"\n  action_items:\n    - round: 13\n      action: \"Appendix G 明确 per-type 结果仅为 descriptive, 不用于 type-level ranking\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-W2\"\n  summary: \"Reproducibility ICC=0.919 仅在 OpenAI 家族内计算, cross-provider replicability 未验证\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [R1, R2]\n      note: \"R1 W5, R2 partial [REBUT]: ICC 目的是 run-to-run replicability 而非 cross-provider consistency, 在任一模型组上测试即可。但 underlying concern 合理: 不知道非 OpenAI 模型的 run-to-run variance。\"\n  action_items:\n    - round: 13\n      action: \"Limitations 中承认 ICC scope 限制, 或报告 1-2 个非 OpenAI 模型的 replicability check\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# MINOR ISSUES\n# ============================================================\n\n- id: \"R12-M1\"\n  summary: \"4.6% vs ≤11% disambiguation awareness 数字交替使用\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 12\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [R2]\n      note: \"R2 小问题: §1 和 §6.2 交替出现。建议统一使用一个数字, 首次出现时注明另一个。\"\n  action_items:\n    - round: 13\n      action: \"统一使用, 首次出现时注明另一个\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-M1\"\n  summary: \"缺失引用: Stengel-Eskin et al. (TACL 2024) scope ambiguity, pragmatic competence 方向\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [R2, R1]\n      note: \"R2 识别, R1 交叉 [AGREE]。Stengel-Eskin et al. (TACL 2024) 对 scopal type 直接相关。另: 'To Know or Not To Know' (2024), Hu et al. 2022 on implicature, Ruis et al. 2024 on pragmatic understanding。\"\n  action_items:\n    - round: 13\n      action: \"补充 4 篇相关引用\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-M2\"\n  summary: \"Clause pair 示例缺失, 方差分解方法未说明, §1 contribution(2) residual 表述不当\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [R1, R2]\n      note: \"R1 小问题, R2 交叉全部 [AGREE]。(1) Appendix 应加每种 type 一个 clause pair 示例; (2) §5.1 方差分解方法 (nested ANOVA? LMM?) 未说明; (3) 60.8% residual 不应作为 contribution 列出。\"\n  action_items:\n    - round: 13\n      action: \"(1) Appendix 加 clause pair 示例表; (2) §5.1 说明方差分解方法; (3) Contribution(2) reframe residual\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-M6\"\n  summary: \"Pages 4-5 连续纯文本无 display item\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 9\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: []\n      note: \"Visual check R13: Page 4-5 连续两页纯文本 (§4 Method), 仍无 display item。低优先级, 页面预算紧张。\"\n  action_items:\n    - round: 13\n      action: \"低优先级——可考虑插入公式或 matched-pair design 简图\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R12-W4\"\n  summary: \"Mitigation 实验方向矛盾 — incompleteness prompt sensitivity (v1: -3.4pp vs v2: +14pp)\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 11\n  last_seen_round: 13\n  mentions:\n    - round: 12\n      reviewers: [R2, R1]\n      note: \"SF-2. 同模型同类型, 换 prompt 方向相反\"\n    - round: 13\n      reviewers: [R2]\n      note: \"R2 Q3: prompt sensitivity 是否 undermine practical recommendation (type-specific mitigation)?\"\n  action_items:\n    - round: 13\n      action: \"讨论 prompt sensitivity 本身作为 finding; 标注两个实验设计差异\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-M2\"\n  summary: \"引用问题: ferrari 作者不一致 + orphan entries\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 8\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: []\n      note: \"本轮未单独提及, 可能已修复, 待确认。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# PREVIOUSLY RESOLVED\n# ============================================================\n\n- id: \"R11-M13\"\n  summary: \"Coreferential 排除在 mitigation/replication 中已在 Limitations 提及\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 12\n  resolution: \"Limitations 已明确声明 coreferential exclusion 及原因\"\n  resolution_round: 12\n\n- id: \"R10-W4-resolved\"\n  summary: \"Disambiguation Deficit → Neglect 术语统一\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 11\n  resolution: \"Round 11 全文统一为 Disambiguation Neglect\"\n  resolution_round: 11\n\n- id: \"R8-W1-resolved\"\n  summary: \"缺少 API 超参数报告\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 10\n  resolution: \"§4.3 添加完整 API 超参数\"\n  resolution_round: 9\n\n- id: \"R8-W4-resolved\"\n  summary: \"无代码/数据可用性声明\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 10\n  resolution: \"添加 Data and Code Availability section\"\n  resolution_round: 9\n\n- id: \"R9-W7-resolved\"\n  summary: \"多重比较校正 three test families 未明确定义\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  resolution: \"Appendix L 新增 Multiple Comparison Correction 小节\"\n  resolution_round: 10\n\n- id: \"R9-W8-resolved\"\n  summary: \"与 DRIP-R 的 taxonomy type-level 映射缺失\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  resolution: \"Appendix L 有 DRIP-R mapping\"\n  resolution_round: 10\n\n- id: \"R9-M3-resolved\"\n  summary: \"Introduction 'seven models' 措辞应区分 main study (5) vs replication (2)\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  resolution: \"措辞已修正\"\n  resolution_round: 10\n\n- id: \"R9-M7-resolved\"\n  summary: \"§5.4 F(20) 缺少 denominator df\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  resolution: \"F(20) → F(20, 2976)\"\n  resolution_round: 10"
  }
}
```

</details>

---


### Tool result

_source line 1193 · 2026-05-22T13:37:14.709537+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_issues.yaml\", \"bytes\": 15366}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1194 · 2026-05-22T13:40:01.358743+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "policy_ambiguity_safety",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.5",
  "report": "# 审稿报告 — Round 13 (Fresh Review)\n\n**论文**: \"Not All Policy Ambiguity Is Equal: Type-Specific Safety Risks for LLM Agents\"\n**Venue**: EMNLP 2026 via ARR May cycle (deadline: 2026-05-25)\n**审稿模式**: Fresh（重新审稿，无历史上下文）\n**Reviewer 配置**: 2 人（R1: 方法严谨性+实验设计; R2: 新颖性+完整性）\n**圆桌轮次**: 1 轮（交叉后完全收敛，无需 Round 2）\n\n---\n\n## Summary\n\n本文在 τ²-bench 上对 LLM agent 的 policy ambiguity 安全影响进行了 matched-pair 因果研究。构建 300 个 clause pairs（六类 ambiguity taxonomy），在五个模型上评估 2,997 episodes。主要发现：(1) ambiguous clauses 增加违规率 34.0pp (OR=15.1)；(2) 六类形成 margin-dependent risk gradient（incompleteness 为 upper bound，coreferential 为 lower bound）；(3) agents 表现出 Disambiguation Neglect（≤11% awareness）和 systematic nocuity（41.3% 多模型一致违规）。\n\n---\n\n## Strengths\n\n**S1. 首个 matched-pair 因果设计** [R1, R2 共识]\n与 DRIP-R（correlational benchmark）不同，matched clause pairs + perturbation control（Δ=−0.67pp, CI containing zero; §4.5）建立了 ambiguity → violation 的因果关系。这在 agent safety 文献中是方法论层面的贡献。\n\n**S2. 统计分析极为详尽透明** [R1, R2 共识]\nTOST equivalence testing、bootstrap cluster analysis、variance decomposition、Holm-Bonferroni 校正、seven-margin sensitivity analysis、logistic regression confound control。17 个 appendix 覆盖了几乎所有 robustness check。C3 标注 inconclusive、C4 标注 exploratory——claim 标定诚实。\n\n**S3. Systematic nocuity 概念有理论价值** [R2]\n41.3% ambiguous clauses 触发多模型一致性违规（§6.3），扩展 Berry &amp; Kamsties (2004) 框架。对 policy auditing 有直接实践意义。\n\n**S4. Replication 范围广** [R1, R2 共识]\n五个主模型 + 两个 replication 模型（Gemini 2.5 Flash, LLaMA 4 Scout），覆盖六家 provider。C1 在七个模型上均成立。ICC=0.919 (within OpenAI family)。\n\n**S5. 与 concurrent work 差异化清晰** [R2]\n与 DRIP-R 的三点差异（causality, safety violations vs decision quality, model×type interaction）准确。Related Work 覆盖 NLP ambiguity、RE、agent safety、psycholinguistics 四个方向。\n\n**S6. Type-specific failure mechanism 分析有深度** [R1]\n三种机制（structural misparse / information gap-filling / boundary violation）crosscut layer boundary，直接 undermines C3 的 layer distinction，论文诚实承认。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF-1. Type 仅解释 0.4% variance 与论文核心叙事的根本张力** [R1-N2 + R2-N1, 完全共识]\n\n论文标题 \"Not All Policy Ambiguity Is Equal\" 和核心叙事围绕六类 taxonomy 展开，但 §5.1 variance decomposition 显示 **type 仅解释 0.4% violation variance**（clause identity 22.4%, model 1.0%, residual 60.8%）。Type 解释力是 clause 的 1/55。这意味着知道一个 ambiguous clause 属于哪种 type 几乎不增加对 violation risk 的预测力——具体措辞远比 type 分类重要。\n\n此外，§1 contribution (2) 将 \"60.8% residual\" 作为贡献列出不恰当——residual variance 是观测结果，不是贡献。\n\n**两位 Reviewer 独立将此列为 Must-Fix #1，交叉后完全一致**，确认这是 substantive concern 而非 stylistic preference。\n\n要求修改：\n- §5.1 正面讨论 0.4% 对 taxonomy 实用价值的含义\n- Discussion 加段落解释 taxonomy 价值在于 intervention design（不同 type 需要不同 mitigation strategy）而非 prediction\n- 考虑调整标题/framing 更准确反映效应量级（e.g., \"clause-level risk with type as secondary predictor\"）\n- §1 contribution (2) 中 \"60.8% residual\" reframe 为观测结果而非贡献\n\n**MF-2. Cross-judge type ranking ρ=−0.03 需在主文正面讨论** [R1-N1, R2 交叉 AGREE]\n\nAppendix P 报告跨 judge 组 type ranking Spearman ρ=−0.03 (p=0.96)——两组对六种 type 的严重程度排序完全不一致。论文归因于 agent composition（GPT-4.1 组包含高 auth scope 违规的模型），但 judge bias 和 model composition 效应无法分离。C2 的 pooled type ranking 实际上是 GPT-5.4 judged 3 models vs GPT-4.1 judged 2 models 的 3:2 加权平均。\n\nR2 补充：incompleteness ranks 1-2 in both groups（核心发现 robust），但 mid-tier 内部排序不稳定。\n\n要求修改：\n- §5.2 正文正面讨论 ρ=−0.03 及其含义\n- 区分 C2 核心发现（incompleteness upper bound, robust across judge groups）vs mid-tier 排序（不稳定）\n- 分别报告两组内的 type gradient 结构\n- Limitations 中将此列为最主要 measurement limitation\n\n**MF-3. Incompleteness information-addition confound 在 Abstract/Conclusion 应更显式标注** [R2-N2, R1 AGREE with nuance]\n\nIncompleteness 的 unambiguous variant 必然添加新信息，创造 information asymmetry。Token count 是粗糙代理（论文自己承认 \"finer-grained semantic measures may reveal different confound structures\"）。但 Abstract 仍以 \"+49.2pp\" 作为 range 上限无 caveat。R1 指出主文 §5.2 已标注 \"upper bound—conditional on confound controls\"，但 Abstract/Conclusion 缺失。\n\n此外，information quality vs quantity 的差异未讨论：auth scope +36.1 words > incompleteness +34.6 但违规率更低，是有力反证，应提升到正文而非仅在 Appendix O。\n\n要求修改：\n- Abstract/Conclusion 明确标注 49.2pp 为 \"upper bound, conditional on information-addition confound\"\n- 考虑在正文报告 confound-free range (+18.7 to +36.0pp)\n- 讨论 information quality vs quantity 差异\n\n### Should-Fix（影响评分但不一票否决）\n\n**SF-1. Two-layer structure 缺乏经验支持** [R2-W1, R1 AGREE]\nC3 inconclusive（不survive Holm-Bonferroni, controlling for token delta 逆转方向），§6 failure mechanisms crosscut layer boundary。Layer 区分应降级为 organizational convenience 而非理论假设。\n\n**SF-2. LLM-as-judge + OpenAI-family bias** [R2-W2, R1 AGREE]\n所有模型由 GPT-5.4 或 GPT-4.1 评判（均 OpenAI family）。C4 结论受此影响。应在 §5.4 而非仅 Limitations 标注此限制。Calibration sample 65% ambiguous 可能高估 judge 一致性。推荐 cross-family judge evaluation。\n\n**SF-3. Error Analysis §6 LLM-coding circularity risk** [R2-W3, R1 AGREE]\n五种 failure mode 由 LLM 编码，κ=0.52 (moderate)。用 LLM 编码 LLM 的 failure modes 存在 circularity 风险。Gwet's AC₁=0.62 仍只是 substantial。建议至少一个类别报告人工编码对照。\n\n**SF-4. Disambiguation Neglect 新颖性定位** [R2-W4, R1 AGREE]\n贡献在于扩展到 consequential agentic contexts，但论文未显式论证为什么 agentic settings 不同于 non-agentic——关键区别在于 consequentiality（执行动作 vs 仅生成文本），应明确展开。\n\n**SF-5. Domain generalizability framing 不一致** [R2-W5, R1 AGREE]\nAbstract \"policy-governed agent deployments\" vs Conclusion \"customer-service deployments\"。τ²-bench 仅覆盖 retail + airline。应统一 scope 措辞，添加 domain qualifier。\n\n**SF-6. Margin-dependent gradient 呈现** [R2-W6 + R1-W1, 共识]\nTOST gradient 在 ±15pp 才稳定（6/6），±10pp 仅 3/6。Bootstrap k=2 重现率仅 34.3%。Figure 2 给出过于确定的 gradient 印象。应在 §5.2 和 Figure 2 caption 中更突出 margin-dependency。\n\n**SF-7. Auth scope κ=0.385 驱动 C4 但 reliability 最低** [R1-W2, R2 AGREE]\nFigure 3 的 52pp range 视觉印象强，但 κ=0.385 最低。排除 auth scope 后 C4 p=0.97。应将 C4 重定位为 auth-scope-specific interaction，Figure 3 caption 标注 reliability caveat。\n\n**SF-8. Per-type human validation CI 过宽** [R1-W4, R2 AGREE]\nScopal κ CI [0.00, 1.00] 完全无信息。Appendix G 末段已注明 \"descriptive statistics only\"，但仍做 type-level 推断（\"Authorization scope has the lowest...\"）。\n\n**SF-9. ICC 仅在 OpenAI 家族内计算** [R1-W5, R2 partial REBUT]\nR2 指出 ICC 目的是 run-to-run replicability（非 cross-provider consistency），在任一模型组测试即可。但 underlying concern 合理：非 OpenAI 模型的 run-to-run variance 未知。建议 Limitations 中承认 scope 限制。\n\n---\n\n## Reviewer Consensus\n\n两位 Reviewer 在以下问题上**完全独立一致**（交叉后全部 [AGREE]）：\n\n1. **0.4% type variance vs 论文叙事** — 最高优先级修改项\n2. **Cross-judge ρ=−0.03 / OpenAI-family confound** — C2 gradient 和 C4 interaction 的可信度\n3. **Incompleteness confound framing** — Abstract/Conclusion 需加 caveat\n4. **SESOI/gradient margin dependence** — gradient 结构呈现过于确定\n\n---\n\n## Reviewer Divergence\n\n仅 1 处轻微分歧（R1-W5 ICC scope）：\n- R1 认为 ICC 仅 OpenAI 是缺陷\n- R2 partial [REBUT]：ICC 目的是 run-to-run replicability，scope 限制不影响核心结论\n- 共识：在 Limitations 中承认 scope 限制即可\n\n---\n\n## Questions（需要作者澄清）\n\n**Q1** [R2]: 0.4% type variance 下，practitioner 用 taxonomy 做 policy auditing 的具体 workflow 是什么？Binary detection (F1=0.81) 就够了，还是需要 type-level classification (macro F1 仅 0.63, incompleteness F1=0.34)？\n\n**Q2** [R2]: C4 interaction 完全集中在 authorization scope（排除后 p=0.97）。这是否是 auth-scope-specific 现象？C4 的 contribution 应如何重新表述？\n\n**Q3** [R1]: 60.8% residual 主要由什么构成？τ²-bench 中 episode 的 user behavior 变异占多大比例？\n\n**Q4** [R1]: 排除 auth scope 后，剩余 5 个 type 的 cross-judge ranking ρ 是多少？能否区分 \"auth scope 特有的 judge disagreement\" vs \"系统性 judge confound\"？\n\n**Q5** [R2]: Mitigation incompleteness prompt sensitivity (v1: −3.4pp vs v2: +14pp)——同模型同类型方向相反是否 undermine type-specific mitigation 的 practical recommendation？\n\n**Q6** [R1, R2]: Coreferential 在 mitigation 和 replication 都缺席，但被用作 confound-free lower bound。如果 coreferential effect 在新 model 上不 replicate，lower bound 结论如何修正？\n\n---\n\n## Missing References\n\nR2 识别，R1 交叉确认：\n- **Stengel-Eskin et al. (TACL 2024)** — LLM 处理 scope ambiguity 的实证研究，与 scopal type 直接相关\n- **\"To Know or Not To Know\" (2024)** — LLM self-consistency under ambiguity，与 Disambiguation Neglect 相关\n- **Hu et al. (2022)** — LLM implicature processing\n- **Ruis et al. (2024)** — LLM pragmatic understanding\n\n---\n\n## External Review\n\n**状态**：未请求（项目未配置 external review）\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**: done（0 critical, 1 warning, 13 info）\n\n主要发现：\n- **[warning] Pages 4-5**: 连续两页纯文本（§4 Method），无任何 display item。建议插入公式或 matched-pair design 简图打破视觉单调。\n- **[info] Page 1**: 首页纯文本（Title + Abstract + Introduction），Figure 1 在第 2 页顶部，可接受。\n- **[info] Page 2**: Figure 1 跨双栏全宽，信息传达良好。图内小方框文字偏小（约正文 60%）。\n- **[info] Page 3**: Table 1 booktabs 风格规范。\n- **[info] Page 6**: Table 2 + Figure 2 同页，视觉密度良好。\n- **[info] Page 7**: Figure 3 热力图清晰可读。\n- **[info] Page 8**: 纯文本页（§6.2-§8+Conclusion），作为讨论+结论页可接受。\n- **[info] Page 9**: Limitations 简短精炼（~1/3 页），References 从页面中部开始。正文在第 8 页结束，**符合 EMNLP 8 页限制**。\n- **[info] Appendix**: 高密度但组织清晰，所有表格使用 booktabs。\n\n---\n\n## Overall Assessment\n\n**评分**: 3.5 / 5 (Borderline Conference)\n**置信度**: 4/5\n\n| 维度 | R1 | R2 | 综合 |\n|------|----|----|------|\n| Soundness | 3.5 | 3.5 | 3.5 |\n| Excitement | 3.0 | 3.5 | 3.25 |\n| Reproducibility | 4.0 | 4.0 | 4.0 |\n\n**总体判断**：方法论贡献扎实——matched-pair 因果设计在 agent safety 领域是首创，统计分析全面透明，claim 标定诚实。但存在一个核心张力：**论文围绕 type-level taxonomy 构建叙事，但数据显示 type 仅解释 0.4% variance，clause wording 才是主要因素**。这从根本上削弱了 taxonomy 作为 practical tool 的定位。加上 cross-judge type ranking 近零相关性 (ρ=−0.03) 威胁 C2 gradient 的外部效度、incompleteness confound 在 headline claims 中标注不充分、domain 受限于两个 customer-service domain，论文在当前 framing 下处于 Borderline Conference。\n\n**升级路径**：如果在 revision 中 (1) 正面讨论 0.4% type variance 并将 taxonomy 价值重新定位为 intervention design 而非 prediction tool，(2) 在 §5.2 正文中讨论 cross-judge ρ=−0.03 并区分 robust vs fragile 结论，(3) Abstract/Conclusion 标注 incompleteness upper bound caveat，(4) 统一 domain scope 措辞——评分有望提升到 4.0 Conference。核心方法论贡献（matched-pair design + perturbation control + systematic nocuity）值得认可。\n\n---\n\n## Detailed Comments（逐节）\n\n### Abstract\n- \"+49.2pp (incompleteness)\" 应标注 \"upper bound reflecting an information-addition confound\"（当前版本已有此措辞，但位置在从句中不够显眼）\n- \"policy-governed agent deployments\" 过宽，应加 domain qualifier (\"in customer-service policy domains\")——当前版本 Conclusion 正确收窄但 Abstract 未统一\n- \"≤11% per-model awareness, 4.6% overall\" 两个数字同时出现尚可，但后文 §1 和 §6.2 交替使用时应统一\n\n### §1 Introduction\n- Contribution (2) 将 \"60.8% residual\" 列为贡献不恰当——应 reframe 为观测结果\n- Contribution (3) \"extending LLM ambiguity-collapse findings to agentic settings\" 定位诚实，但应显式论证 agentic settings 的关键区别在于 consequentiality\n\n### §3 Taxonomy\n- \"Scope of ambiguity\" 段落（§3 末段）对理论张力的讨论充分\n- Two-layer 假设应降级为 organizational convenience（C3 inconclusive + failure mechanisms crosscut）\n\n### §4 Method\n- Matched-pair design 严谨，perturbation control 有效\n- §4.4 cross-judge calibration：McNemar p=0.606, κ=0.653 报告规范，但应提及 calibration sample 65% ambiguous 的组成\n- §4.6 SESOI ±15pp：domain anchoring 合理，但应更明确讨论 margin-dependency 对 C2 结论的影响\n\n### §5 Results\n- §5.1 (C1)：34.0pp effect 强且 robust，方差分解是重要发现但需要正面讨论 0.4% type variance 的含义\n- §5.2 (C2)：应在正文讨论 Appendix P 的 ρ=−0.03，区分 robust 核心发现 vs fragile 排序\n- §5.3 (C3)：标注 inconclusive 是正确的——建议加 1 句解释 failure mechanisms 也不支持 layer distinction\n- §5.4 (C4)：应重定位为 auth-scope-specific interaction；Figure 3 caption 加 reliability caveat\n\n### §6 Error Analysis\n- Systematic nocuity 是新颖且有价值的概念\n- Failure mode coding reliability (κ=0.52) 应承认限制，讨论 LLM-coding circularity risk\n- Disambiguation Neglect：应展开 agentic vs non-agentic 的 consequentiality 区别\n\n### §7 Discussion\n- Differential nocuity 应定位为 hypothesis 而非 framework\n- Mitigation experiment 的 prompt sensitivity（同类型方向相反）是重要发现，应更充分讨论\n- Practical implications 应正面承认 type-level auditing 的局限性\n\n### §8 Conclusion\n- 数字准确，但应与 Abstract 统一 domain scope 措辞\n\n### Limitations\n- 覆盖了 scope、measurement、confounds 三个维度\n- 应将 cross-judge ρ=−0.03 列为最主要 measurement limitation\n- 应承认 ICC scope 限制（仅 OpenAI family）\n\n### Appendix\n- 17 个 appendix 组织清晰但缺少 clause pair 示例\n- Appendix G per-type κ 应明确标注 descriptive only\n- §5.1 方差分解方法（nested ANOVA? LMM?）应说明"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "policy_ambiguity_safety",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.5",
    "report": "# 审稿报告 — Round 13 (Fresh Review)\n\n**论文**: \"Not All Policy Ambiguity Is Equal: Type-Specific Safety Risks for LLM Agents\"\n**Venue**: EMNLP 2026 via ARR May cycle (deadline: 2026-05-25)\n**审稿模式**: Fresh（重新审稿，无历史上下文）\n**Reviewer 配置**: 2 人（R1: 方法严谨性+实验设计; R2: 新颖性+完整性）\n**圆桌轮次**: 1 轮（交叉后完全收敛，无需 Round 2）\n\n---\n\n## Summary\n\n本文在 τ²-bench 上对 LLM agent 的 policy ambiguity 安全影响进行了 matched-pair 因果研究。构建 300 个 clause pairs（六类 ambiguity taxonomy），在五个模型上评估 2,997 episodes。主要发现：(1) ambiguous clauses 增加违规率 34.0pp (OR=15.1)；(2) 六类形成 margin-dependent risk gradient（incompleteness 为 upper bound，coreferential 为 lower bound）；(3) agents 表现出 Disambiguation Neglect（≤11% awareness）和 systematic nocuity（41.3% 多模型一致违规）。\n\n---\n\n## Strengths\n\n**S1. 首个 matched-pair 因果设计** [R1, R2 共识]\n与 DRIP-R（correlational benchmark）不同，matched clause pairs + perturbation control（Δ=−0.67pp, CI containing zero; §4.5）建立了 ambiguity → violation 的因果关系。这在 agent safety 文献中是方法论层面的贡献。\n\n**S2. 统计分析极为详尽透明** [R1, R2 共识]\nTOST equivalence testing、bootstrap cluster analysis、variance decomposition、Holm-Bonferroni 校正、seven-margin sensitivity analysis、logistic regression confound control。17 个 appendix 覆盖了几乎所有 robustness check。C3 标注 inconclusive、C4 标注 exploratory——claim 标定诚实。\n\n**S3. Systematic nocuity 概念有理论价值** [R2]\n41.3% ambiguous clauses 触发多模型一致性违规（§6.3），扩展 Berry &amp; Kamsties (2004) 框架。对 policy auditing 有直接实践意义。\n\n**S4. Replication 范围广** [R1, R2 共识]\n五个主模型 + 两个 replication 模型（Gemini 2.5 Flash, LLaMA 4 Scout），覆盖六家 provider。C1 在七个模型上均成立。ICC=0.919 (within OpenAI family)。\n\n**S5. 与 concurrent work 差异化清晰** [R2]\n与 DRIP-R 的三点差异（causality, safety violations vs decision quality, model×type interaction）准确。Related Work 覆盖 NLP ambiguity、RE、agent safety、psycholinguistics 四个方向。\n\n**S6. Type-specific failure mechanism 分析有深度** [R1]\n三种机制（structural misparse / information gap-filling / boundary violation）crosscut layer boundary，直接 undermines C3 的 layer distinction，论文诚实承认。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF-1. Type 仅解释 0.4% variance 与论文核心叙事的根本张力** [R1-N2 + R2-N1, 完全共识]\n\n论文标题 \"Not All Policy Ambiguity Is Equal\" 和核心叙事围绕六类 taxonomy 展开，但 §5.1 variance decomposition 显示 **type 仅解释 0.4% violation variance**（clause identity 22.4%, model 1.0%, residual 60.8%）。Type 解释力是 clause 的 1/55。这意味着知道一个 ambiguous clause 属于哪种 type 几乎不增加对 violation risk 的预测力——具体措辞远比 type 分类重要。\n\n此外，§1 contribution (2) 将 \"60.8% residual\" 作为贡献列出不恰当——residual variance 是观测结果，不是贡献。\n\n**两位 Reviewer 独立将此列为 Must-Fix #1，交叉后完全一致**，确认这是 substantive concern 而非 stylistic preference。\n\n要求修改：\n- §5.1 正面讨论 0.4% 对 taxonomy 实用价值的含义\n- Discussion 加段落解释 taxonomy 价值在于 intervention design（不同 type 需要不同 mitigation strategy）而非 prediction\n- 考虑调整标题/framing 更准确反映效应量级（e.g., \"clause-level risk with type as secondary predictor\"）\n- §1 contribution (2) 中 \"60.8% residual\" reframe 为观测结果而非贡献\n\n**MF-2. Cross-judge type ranking ρ=−0.03 需在主文正面讨论** [R1-N1, R2 交叉 AGREE]\n\nAppendix P 报告跨 judge 组 type ranking Spearman ρ=−0.03 (p=0.96)——两组对六种 type 的严重程度排序完全不一致。论文归因于 agent composition（GPT-4.1 组包含高 auth scope 违规的模型），但 judge bias 和 model composition 效应无法分离。C2 的 pooled type ranking 实际上是 GPT-5.4 judged 3 models vs GPT-4.1 judged 2 models 的 3:2 加权平均。\n\nR2 补充：incompleteness ranks 1-2 in both groups（核心发现 robust），但 mid-tier 内部排序不稳定。\n\n要求修改：\n- §5.2 正文正面讨论 ρ=−0.03 及其含义\n- 区分 C2 核心发现（incompleteness upper bound, robust across judge groups）vs mid-tier 排序（不稳定）\n- 分别报告两组内的 type gradient 结构\n- Limitations 中将此列为最主要 measurement limitation\n\n**MF-3. Incompleteness information-addition confound 在 Abstract/Conclusion 应更显式标注** [R2-N2, R1 AGREE with nuance]\n\nIncompleteness 的 unambiguous variant 必然添加新信息，创造 information asymmetry。Token count 是粗糙代理（论文自己承认 \"finer-grained semantic measures may reveal different confound structures\"）。但 Abstract 仍以 \"+49.2pp\" 作为 range 上限无 caveat。R1 指出主文 §5.2 已标注 \"upper bound—conditional on confound controls\"，但 Abstract/Conclusion 缺失。\n\n此外，information quality vs quantity 的差异未讨论：auth scope +36.1 words > incompleteness +34.6 但违规率更低，是有力反证，应提升到正文而非仅在 Appendix O。\n\n要求修改：\n- Abstract/Conclusion 明确标注 49.2pp 为 \"upper bound, conditional on information-addition confound\"\n- 考虑在正文报告 confound-free range (+18.7 to +36.0pp)\n- 讨论 information quality vs quantity 差异\n\n### Should-Fix（影响评分但不一票否决）\n\n**SF-1. Two-layer structure 缺乏经验支持** [R2-W1, R1 AGREE]\nC3 inconclusive（不survive Holm-Bonferroni, controlling for token delta 逆转方向），§6 failure mechanisms crosscut layer boundary。Layer 区分应降级为 organizational convenience 而非理论假设。\n\n**SF-2. LLM-as-judge + OpenAI-family bias** [R2-W2, R1 AGREE]\n所有模型由 GPT-5.4 或 GPT-4.1 评判（均 OpenAI family）。C4 结论受此影响。应在 §5.4 而非仅 Limitations 标注此限制。Calibration sample 65% ambiguous 可能高估 judge 一致性。推荐 cross-family judge evaluation。\n\n**SF-3. Error Analysis §6 LLM-coding circularity risk** [R2-W3, R1 AGREE]\n五种 failure mode 由 LLM 编码，κ=0.52 (moderate)。用 LLM 编码 LLM 的 failure modes 存在 circularity 风险。Gwet's AC₁=0.62 仍只是 substantial。建议至少一个类别报告人工编码对照。\n\n**SF-4. Disambiguation Neglect 新颖性定位** [R2-W4, R1 AGREE]\n贡献在于扩展到 consequential agentic contexts，但论文未显式论证为什么 agentic settings 不同于 non-agentic——关键区别在于 consequentiality（执行动作 vs 仅生成文本），应明确展开。\n\n**SF-5. Domain generalizability framing 不一致** [R2-W5, R1 AGREE]\nAbstract \"policy-governed agent deployments\" vs Conclusion \"customer-service deployments\"。τ²-bench 仅覆盖 retail + airline。应统一 scope 措辞，添加 domain qualifier。\n\n**SF-6. Margin-dependent gradient 呈现** [R2-W6 + R1-W1, 共识]\nTOST gradient 在 ±15pp 才稳定（6/6），±10pp 仅 3/6。Bootstrap k=2 重现率仅 34.3%。Figure 2 给出过于确定的 gradient 印象。应在 §5.2 和 Figure 2 caption 中更突出 margin-dependency。\n\n**SF-7. Auth scope κ=0.385 驱动 C4 但 reliability 最低** [R1-W2, R2 AGREE]\nFigure 3 的 52pp range 视觉印象强，但 κ=0.385 最低。排除 auth scope 后 C4 p=0.97。应将 C4 重定位为 auth-scope-specific interaction，Figure 3 caption 标注 reliability caveat。\n\n**SF-8. Per-type human validation CI 过宽** [R1-W4, R2 AGREE]\nScopal κ CI [0.00, 1.00] 完全无信息。Appendix G 末段已注明 \"descriptive statistics only\"，但仍做 type-level 推断（\"Authorization scope has the lowest...\"）。\n\n**SF-9. ICC 仅在 OpenAI 家族内计算** [R1-W5, R2 partial REBUT]\nR2 指出 ICC 目的是 run-to-run replicability（非 cross-provider consistency），在任一模型组测试即可。但 underlying concern 合理：非 OpenAI 模型的 run-to-run variance 未知。建议 Limitations 中承认 scope 限制。\n\n---\n\n## Reviewer Consensus\n\n两位 Reviewer 在以下问题上**完全独立一致**（交叉后全部 [AGREE]）：\n\n1. **0.4% type variance vs 论文叙事** — 最高优先级修改项\n2. **Cross-judge ρ=−0.03 / OpenAI-family confound** — C2 gradient 和 C4 interaction 的可信度\n3. **Incompleteness confound framing** — Abstract/Conclusion 需加 caveat\n4. **SESOI/gradient margin dependence** — gradient 结构呈现过于确定\n\n---\n\n## Reviewer Divergence\n\n仅 1 处轻微分歧（R1-W5 ICC scope）：\n- R1 认为 ICC 仅 OpenAI 是缺陷\n- R2 partial [REBUT]：ICC 目的是 run-to-run replicability，scope 限制不影响核心结论\n- 共识：在 Limitations 中承认 scope 限制即可\n\n---\n\n## Questions（需要作者澄清）\n\n**Q1** [R2]: 0.4% type variance 下，practitioner 用 taxonomy 做 policy auditing 的具体 workflow 是什么？Binary detection (F1=0.81) 就够了，还是需要 type-level classification (macro F1 仅 0.63, incompleteness F1=0.34)？\n\n**Q2** [R2]: C4 interaction 完全集中在 authorization scope（排除后 p=0.97）。这是否是 auth-scope-specific 现象？C4 的 contribution 应如何重新表述？\n\n**Q3** [R1]: 60.8% residual 主要由什么构成？τ²-bench 中 episode 的 user behavior 变异占多大比例？\n\n**Q4** [R1]: 排除 auth scope 后，剩余 5 个 type 的 cross-judge ranking ρ 是多少？能否区分 \"auth scope 特有的 judge disagreement\" vs \"系统性 judge confound\"？\n\n**Q5** [R2]: Mitigation incompleteness prompt sensitivity (v1: −3.4pp vs v2: +14pp)——同模型同类型方向相反是否 undermine type-specific mitigation 的 practical recommendation？\n\n**Q6** [R1, R2]: Coreferential 在 mitigation 和 replication 都缺席，但被用作 confound-free lower bound。如果 coreferential effect 在新 model 上不 replicate，lower bound 结论如何修正？\n\n---\n\n## Missing References\n\nR2 识别，R1 交叉确认：\n- **Stengel-Eskin et al. (TACL 2024)** — LLM 处理 scope ambiguity 的实证研究，与 scopal type 直接相关\n- **\"To Know or Not To Know\" (2024)** — LLM self-consistency under ambiguity，与 Disambiguation Neglect 相关\n- **Hu et al. (2022)** — LLM implicature processing\n- **Ruis et al. (2024)** — LLM pragmatic understanding\n\n---\n\n## External Review\n\n**状态**：未请求（项目未配置 external review）\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**: done（0 critical, 1 warning, 13 info）\n\n主要发现：\n- **[warning] Pages 4-5**: 连续两页纯文本（§4 Method），无任何 display item。建议插入公式或 matched-pair design 简图打破视觉单调。\n- **[info] Page 1**: 首页纯文本（Title + Abstract + Introduction），Figure 1 在第 2 页顶部，可接受。\n- **[info] Page 2**: Figure 1 跨双栏全宽，信息传达良好。图内小方框文字偏小（约正文 60%）。\n- **[info] Page 3**: Table 1 booktabs 风格规范。\n- **[info] Page 6**: Table 2 + Figure 2 同页，视觉密度良好。\n- **[info] Page 7**: Figure 3 热力图清晰可读。\n- **[info] Page 8**: 纯文本页（§6.2-§8+Conclusion），作为讨论+结论页可接受。\n- **[info] Page 9**: Limitations 简短精炼（~1/3 页），References 从页面中部开始。正文在第 8 页结束，**符合 EMNLP 8 页限制**。\n- **[info] Appendix**: 高密度但组织清晰，所有表格使用 booktabs。\n\n---\n\n## Overall Assessment\n\n**评分**: 3.5 / 5 (Borderline Conference)\n**置信度**: 4/5\n\n| 维度 | R1 | R2 | 综合 |\n|------|----|----|------|\n| Soundness | 3.5 | 3.5 | 3.5 |\n| Excitement | 3.0 | 3.5 | 3.25 |\n| Reproducibility | 4.0 | 4.0 | 4.0 |\n\n**总体判断**：方法论贡献扎实——matched-pair 因果设计在 agent safety 领域是首创，统计分析全面透明，claim 标定诚实。但存在一个核心张力：**论文围绕 type-level taxonomy 构建叙事，但数据显示 type 仅解释 0.4% variance，clause wording 才是主要因素**。这从根本上削弱了 taxonomy 作为 practical tool 的定位。加上 cross-judge type ranking 近零相关性 (ρ=−0.03) 威胁 C2 gradient 的外部效度、incompleteness confound 在 headline claims 中标注不充分、domain 受限于两个 customer-service domain，论文在当前 framing 下处于 Borderline Conference。\n\n**升级路径**：如果在 revision 中 (1) 正面讨论 0.4% type variance 并将 taxonomy 价值重新定位为 intervention design 而非 prediction tool，(2) 在 §5.2 正文中讨论 cross-judge ρ=−0.03 并区分 robust vs fragile 结论，(3) Abstract/Conclusion 标注 incompleteness upper bound caveat，(4) 统一 domain scope 措辞——评分有望提升到 4.0 Conference。核心方法论贡献（matched-pair design + perturbation control + systematic nocuity）值得认可。\n\n---\n\n## Detailed Comments（逐节）\n\n### Abstract\n- \"+49.2pp (incompleteness)\" 应标注 \"upper bound reflecting an information-addition confound\"（当前版本已有此措辞，但位置在从句中不够显眼）\n- \"policy-governed agent deployments\" 过宽，应加 domain qualifier (\"in customer-service policy domains\")——当前版本 Conclusion 正确收窄但 Abstract 未统一\n- \"≤11% per-model awareness, 4.6% overall\" 两个数字同时出现尚可，但后文 §1 和 §6.2 交替使用时应统一\n\n### §1 Introduction\n- Contribution (2) 将 \"60.8% residual\" 列为贡献不恰当——应 reframe 为观测结果\n- Contribution (3) \"extending LLM ambiguity-collapse findings to agentic settings\" 定位诚实，但应显式论证 agentic settings 的关键区别在于 consequentiality\n\n### §3 Taxonomy\n- \"Scope of ambiguity\" 段落（§3 末段）对理论张力的讨论充分\n- Two-layer 假设应降级为 organizational convenience（C3 inconclusive + failure mechanisms crosscut）\n\n### §4 Method\n- Matched-pair design 严谨，perturbation control 有效\n- §4.4 cross-judge calibration：McNemar p=0.606, κ=0.653 报告规范，但应提及 calibration sample 65% ambiguous 的组成\n- §4.6 SESOI ±15pp：domain anchoring 合理，但应更明确讨论 margin-dependency 对 C2 结论的影响\n\n### §5 Results\n- §5.1 (C1)：34.0pp effect 强且 robust，方差分解是重要发现但需要正面讨论 0.4% type variance 的含义\n- §5.2 (C2)：应在正文讨论 Appendix P 的 ρ=−0.03，区分 robust 核心发现 vs fragile 排序\n- §5.3 (C3)：标注 inconclusive 是正确的——建议加 1 句解释 failure mechanisms 也不支持 layer distinction\n- §5.4 (C4)：应重定位为 auth-scope-specific interaction；Figure 3 caption 加 reliability caveat\n\n### §6 Error Analysis\n- Systematic nocuity 是新颖且有价值的概念\n- Failure mode coding reliability (κ=0.52) 应承认限制，讨论 LLM-coding circularity risk\n- Disambiguation Neglect：应展开 agentic vs non-agentic 的 consequentiality 区别\n\n### §7 Discussion\n- Differential nocuity 应定位为 hypothesis 而非 framework\n- Mitigation experiment 的 prompt sensitivity（同类型方向相反）是重要发现，应更充分讨论\n- Practical implications 应正面承认 type-level auditing 的局限性\n\n### §8 Conclusion\n- 数字准确，但应与 Abstract 统一 domain scope 措辞\n\n### Limitations\n- 覆盖了 scope、measurement、confounds 三个维度\n- 应将 cross-judge ρ=−0.03 列为最主要 measurement limitation\n- 应承认 ICC scope 限制（仅 OpenAI family）\n\n### Appendix\n- 17 个 appendix 组织清晰但缺少 clause pair 示例\n- Appendix G per-type κ 应明确标注 descriptive only\n- §5.1 方差分解方法（nested ANOVA? LMM?）应说明"
  }
}
```

</details>

---


### Tool result

_source line 1195 · 2026-05-22T13:40:05.576694+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_10fa2e89afc5e9b8a13613245e008dd9:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4217
}
```

</details>

---


### Tool call

_source line 1196 · 2026-05-22T13:40:20.342698+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '检查论文资料完整性并调研 EMNLP 2026 venue 要求'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.7: 派发视觉审查', 'status': 'completed', 'activeForm': '派发视觉审查 Agent'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'completed', 'activeForm': '收集 Reviewer 独立审稿结果'}, {'content': 'Step 2: 交叉分享', 'status': 'completed', 'activeForm': 'Reviewer 交叉分享与回应'}, {'content': 'Step 3: 收敛判断', 'status': 'completed', 'activeForm': '判断审稿意见收敛性'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'completed', 'activeForm': '汇总审稿报告并投递'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '检查论文资料完整性并调研 EMNLP 2026 venue 要求'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.7: 派发视觉审查', 'status': 'completed', 'activeForm': '派发视觉审查 Agent'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'completed', 'activeForm': '收集 Reviewer 独立审稿结果'}, {'content': 'Step 2: 交叉分享', 'status': 'completed', 'activeForm': 'Reviewer 交叉分享与回应'}, {'content': 'Step 3: 收敛判断', 'status': 'completed', 'activeForm': '判断审稿意见收敛性'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'completed', 'activeForm': '汇总审稿报告并投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 1197 · 2026-05-22T13:40:20.393324+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "TodoWrite",
  "elapsed_ms": 50
}
```

</details>

---


### Assistant

_source line 1198 · 2026-05-22T13:40:32.772119+00:00_

Round 13 审稿完成。

**审稿结果**：3.5 / 5 (Borderline Conference)

**核心发现**：
- **3 个 Must-Fix**：(1) type 0.4% variance 与论文叙事张力——两位 Reviewer 独立 #1 共识；(2) cross-judge type ranking ρ=−0.03 需在主文讨论；(3) incompleteness confound 在 Abstract/Conclusion 标注不充分
- **9 个 Should-Fix**：two-layer 降级、judge bias、LLM-coding circularity、Disambiguation Neglect 定位、domain framing 统一、margin-dependency 呈现、auth scope C4 重定位、per-type CI、ICC scope
- **升级路径**：正面处理 MF-1~3 + 统一 domain scope → 4.0 Conference

报告已投递至 Research Director，issue tracker 已同步更新。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 114

## Round 114

2 recorded events


### User

_source line 1199 · 2026-05-22T13:40:35.352529+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。对 R1 的 2 个 Must-Fix 和 5 个 Should-Fix 逐条给出了 AGREE/REBUT 判断：

- **N1 (cross-judge ρ=−0.03)**: AGREE，补充了 incompleteness 在两组内均 rank 最高的 nuance
- **N2 (0.4% type variance)**: AGREE，与我的 N1 完全一致，两位 reviewer 独立识别同一问题
- **W1 (SESOI ±15pp)**: AGREE，但 partial rebut 论文确实有 domain anchoring
- **W2 (auth scope κ=0.385)**: AGREE
- **W3 (incompleteness confound)**: AGREE，但 partial rebut 引用 Appendix O 的 counter-evidence
- **W4 (per-type CI)**: AGREE
- **W5 (ICC scope)**: REBUT — ICC 测的是 run-to-run variance，在任一模型组上测试即可，但建议补充非 OpenAI 模型数据

两份审稿核心共识：matched-pair 因果设计是扎实贡献，但 taxonomy 叙事需要更谨慎的定位。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1200 · 2026-05-22T13:40:43.892634+00:00_

Round 13 审稿已完成。

**最终结果**：3.5 / 5 (Borderline Conference)，两位 Reviewer 评分一致。

审稿报告和 issue tracker 均已提交/更新。报告包含 3 个 Must-Fix、9 个 Should-Fix、6 个 Questions、4 篇缺失引用、视觉审查结果，以及升级到 4.0 Conference 的具体路径。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 115

## Round 115

68 recorded events


### User

_source line 1201 · 2026-05-22T14:59:26.350205+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: policy_ambiguity_safety
- 论文路径: /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Long Paper (ARR)
- 截止日期: 2026-05-25
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 1202 · 2026-05-22T14:59:35.103058+00:00_

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
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 1203 · 2026-05-22T14:59:35.254522+00:00_

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
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 1204 · 2026-05-22T14:59:41.578601+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,director_post_to_reviewer,get_external_review_status,get_visual_check_status,submit_review_report_to_research_director,update_review_issues,read_project_file,WebSearch",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,director_post_to_reviewer,get_external_review_status,get_visual_check_status,submit_review_report_to_research_director,update_review_issues,read_project_file,WebSearch",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 1205 · 2026-05-22T14:59:41.579043+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1206 · 2026-05-22T14:59:44.841758+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,director_post_to_reviewer,get_external_review_status,get_visual_check_status,submit_review_report_to_research_director,update_review_issues,read_project_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,director_post_to_reviewer,get_external_review_status,get_visual_check_status,submit_review_report_to_research_director,update_review_issues,read_project_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 1207 · 2026-05-22T14:59:44.842102+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1208 · 2026-05-22T14:59:49.861674+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 1209 · 2026-05-22T14:59:49.862038+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1210 · 2026-05-22T14:59:55.333143+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "policy_ambiguity_safety"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "policy_ambiguity_safety"
  }
}
```

</details>

---


### Tool result

_source line 1211 · 2026-05-22T14:59:56.186808+00:00_

{"result":"# 项目 policy_ambiguity_safety 概况\n\n## 实验状态 (17 个)\n\n- **plan_014**: DONE (success) — \n- **plan_015**: DONE (success) — \n- **plan_013**: DONE (success) — \n- **plan_012**: DONE (success) — \n- **plan_011**: DONE (success) — \n- **plan_010**: DONE (success) — \n- **plan_004**: DONE (success) — \n- **plan_003b**: DONE (success) — \n- **plan_003a**: DONE (success) — \n- **plan_002c**: DONE (success) — \n- **plan_006**: DONE (success) — \n- **plan_005**: DONE (success) — \n- **plan_002**: DONE (negative) — \n- **diag_001**: DONE (negative) — \n- **mvp_001**: DONE (negative) — \n\n## 最新报告\n# Handover — 2026-05-22\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n（无）\n\n## 近期结论\n- **plan_016** (negative): Type-specific mitigation prompts reduce violations more effectively than generic awareness prompts for their targeted ambiguity types, supporting the practical contribution that type-aware triage is necessary for policy-governed deployments\n- **plan_009** (success): Cross-judge LLM agreement (gpt-5.4 vs gpt-4.1) achieves substantial agreement (weighted κ ≥ 0.60) on violation level classification. LLM-human agreement should be comparable, validating the cross-judge evaluation design.\n  [plan_009_annotation_guidelines](/api/workspace-files/projects/policy_ambiguity_safety/artifacts/plan_009/report/annotation_guidelines.md) | [plan_009_annotation_sheet](/api/workspace-files/projects/policy_ambiguity_safety/artifacts/plan_009/data/annotation_sheet.jsonl) | [plan_009_llm_agreement](/api/workspace-files/projects/policy_ambiguity_safety/artifacts/plan_009/report/llm_agreement.json) | [plan_009_annotation_sheet_clean](/api/workspace-files/projects/policy_ambiguity_safety/artifacts/plan_009/data/annotation_sheet_clean.jsonl)\n- **plan_014** (success): Expanding perturbation control from n=120 to n=300 will maintain non-significant Δ_perturb (CI containing zero) while narrowing CI upper bound from 13.3pp to ~8pp, strengthening SESOI justification for C
…[truncated 563 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 853
}
```

</details>

---


### Tool call

_source line 1212 · 2026-05-22T14:59:56.689002+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 1213 · 2026-05-22T14:59:57.091025+00:00_

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
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 1214 · 2026-05-22T14:59:57.091543+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers ARR submission guidelines author instructions site:aclweb.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers ARR submission guidelines author instructions site:aclweb.org"
  }
}
```

</details>

---


### Tool call

_source line 1215 · 2026-05-22T14:59:57.798242+00:00_

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
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
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

_source line 1216 · 2026-05-22T14:59:58.049588+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "ToolSearch",
  "elapsed_ms": 251
}
```

</details>

---


### Tool result

_source line 1217 · 2026-05-22T15:00:01.517776+00:00_

Web search results for query: "EMNLP 2026 call for papers ARR submission guidelines author instructions site:aclweb.org"

Links: [{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"5th Workshop on Evaluation and Comparison for NLP systems (Eval4NLP) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/5th-workshop-evaluation-and-comparison-nlp-systems-eval4nlp"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"First Call for Papers – EACL 2026 Student Research Workshop (SRW) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/first-call-papers-eacl-2026-student-research-workshop-srw"},{"title":"Main Conference - ACL 2025","url":"https://2025.aclweb.org/calls/main_conference_papers/"}]

Based on my web search, I found information about EMNLP 2025 rather than EMNLP 2026. The search 
…[truncated 1141 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "WebSearch",
  "elapsed_ms": 4426
}
```

</details>

---


### Tool call

_source line 1218 · 2026-05-22T15:00:08.199706+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 submission guidelines page limits long paper format"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 submission guidelines page limits long paper format"
  }
}
```

</details>

---


### Tool call

_source line 1219 · 2026-05-22T15:00:08.702823+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 conference call for papers deadline submission"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 conference call for papers deadline submission"
  }
}
```

</details>

---


### Tool call

_source line 1220 · 2026-05-22T15:00:09.507366+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_14/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"NO_PDF\"",
  "description": "Check if submitted PDF exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_14/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"NO_PDF\"",
    "description": "Check if submitted PDF exists"
  }
}
```

</details>

---


### Tool result

_source line 1221 · 2026-05-22T15:00:10.064197+00:00_

-rw-r--r-- 1 ubuntu ubuntu 429156 May 22 14:36 /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_14/submitted.pdf
PDF_EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Bash",
  "elapsed_ms": 556
}
```

</details>

---


### Tool call

_source line 1222 · 2026-05-22T15:00:10.120419+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1223 · 2026-05-22T15:00:10.175614+00:00_

1	## Review Issues Tracker — policy_ambiguity_safety
2	## Paper: "Not All Policy Ambiguity Is Equal: Type-Specific Safety Risks for LLM Agents"
3	## Venue: EMNLP 2026 via ARR May cycle
4	## Latest Round: 14 (in progress — addressing Round 13 fresh review findings)
5	
6	# ============================================================
7	# CRITICAL ISSUES
8	# ============================================================
9	
10	- id: "R11-C1"
11	  summary: "Type 仅解释 0.4% variance 与论文标题/核心叙事的根本张力"
12	  category: framing
13	  severity: critical
14	  status: in_progress
15	  first_raised_round: 11
16	  last_seen_round: 13
17	  mentions:
18	    - round: 11
19	      reviewers: [R2, R1]
20	      note: "W6. clause_within_type=22.0% vs ambiguity_type=0.4%"
21	    - round: 12
22	      reviewers: [R2, R1]
23	      note: "MF-1. 22× 放在 contributions list 紧跟 C2, 读者误读为 taxonomy 解释力"
24	    - round: 13
25	      reviewers: [R1, R2]
26	      note: "R13 fresh review: 两位 Reviewer 独立将此列为 Must-Fix #1。标题 'Not All Policy Ambiguity Is Equal' 暗示 type 是强预测因子，但 type 0.4% vs clause 22.4% (55×)。知道 clause 属于哪种 type 几乎不增加预测力。R1: type-level interventions 实用性存疑；R2: taxonomy 价值需重新定位为 intervention design 而非 prediction。两位 Reviewer 完全一致 [AGREE]。"
27	  action_items:
28	    - round: 14
29	      action: "(1) §5.1 正面讨论 0.4% 含义; (2) Discussion 加 'Taxonomy and intervention design' 段落; (3) Contribution(2) 删 '60.8% residual' 改为 intervention design framing; (4) 保留标题不变"
30	      assigned_to: agent
31	      status: in_progress
32	  resolution: ""
33	  resolution_round: null
34	
35	- id: "R13-C1"
36	  summary: "Cross-judge type ranking ρ=−0.03 需在主文正面讨论，直接关系 C2 gradient 可信度"
37	  category: method
38	  severity: critical
39	  status: in_progress
40	  first_raised_round: 13
41	  last_seen_round: 13
42	  mentions:
43	    - round: 13
44	      reviewers: [R1, R2]
45	      note: "R1 独立提出为 Must-Fix, R2 交叉回应 [AGREE]。Appendix P: Spearman ρ=−0.03 (p=0.96), 两个 judge 组对 type severity 排序完全不一致。Judge bias 和 model composition 无法分离。GPT-5.4
…[truncated 12652 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 55
}
```

</details>

---


### Tool result

_source line 1224 · 2026-05-22T15:00:14.848320+00:00_

Web search results for query: "ACL Rolling Review 2026 submission guidelines page limits long paper format"

Links: [{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"Paper formatting guidelines - ACLPUB","url":"https://acl-org.github.io/ACLPUB/formatting.html"},{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"}]

Based on the search results, here are the submission guidelines for ACL Rolling Review 2026 regarding page limits for long papers:

Review versions of long papers may have up to eight (8) pages of content plus unlimited pages for references. Upon acceptance, final versions of long papers will be given one additional page – up to nine (9) pages of content plus unlimited pages for acknowledgments and references – so that reviewers' comments can be taken into account.

Additionally, for both long and short papers, all figures and tables that are part of the main text must fit within these page limits.


REMINDER: You MUST incl
…[truncated 77 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "WebSearch",
  "elapsed_ms": 6648
}
```

</details>

---


### Tool result

_source line 1225 · 2026-05-22T15:00:14.950456+00:00_

Web search results for query: "EMNLP 2026 conference call for papers deadline submission"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"EMNLP 2026 Call for Papers — Official Deadlines & Important Dates | PaperPilot","url":"https://www.getpaperpilot.com/deadlines/emnlp-2026.html"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"Update EMNLP 2026 conference dates and deadlines · huggingface/ai-deadlines at 2754f67","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/2754f67c0550847973789522a0a082dd5443b5c0"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"EMNLP 2026 Conference | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FConference"}]

Based on the search results, here's 
…[truncated 1200 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "WebSearch",
  "elapsed_ms": 6247
}
```

</details>

---


### Tool call

_source line 1226 · 2026-05-22T15:00:41.726423+00:00_

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
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 1227 · 2026-05-22T15:00:41.726921+00:00_

1	\begin{abstract}
2	LLM-based agents operate under natural-language policy specifications that inevitably contain ambiguity, yet the causal relationship between ambiguity type and safety violations remains unmeasured. We present a matched-pair study on $\tau^2$-bench with 300 clause pairs spanning a six-type ambiguity taxonomy, evaluated across five models (2,997 episodes). Three findings emerge. First, ambiguous clauses increase violation rates by 34.0 percentage points (OR $= 15.1$), with a perturbation control supporting ambiguity-specific causation. Second, per-type effects range from $+$18.7\,pp (coreferential) to $+$49.2\,pp (incompleteness, upper bound including information-addition effects); five confound-controlled types span $+$18.7 to $+$36.0\,pp, forming a risk gradient rather than sharp tiers, with rankings partly margin-dependent. Third, error analysis of 614 violation traces reveals \emph{Disambiguation Neglect} ($\leq$11\% per-model awareness, 4.6\% overall) and \emph{systematic nocuity}---41.3\% of clauses triggering model-convergent violations---indicating clause-level rather than model-level risk factors. These results---observed in customer-service policy domains---motivate type-aware policy auditing and externalized ambiguity detection for policy-governed deployments.
3	\end{abstract}
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1228 · 2026-05-22T15:00:41.977872+00:00_

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
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 1229 · 2026-05-22T15:00:41.978327+00:00_

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
…[truncated 2310 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1230 · 2026-05-22T15:00:42.129184+00:00_

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
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 1231 · 2026-05-22T15:00:42.129758+00:00_

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
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1232 · 2026-05-22T15:00:42.130105+00:00_

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
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 1233 · 2026-05-22T15:00:42.231119+00:00_

1	\section{Results}
2	\label{sec:results}
3	
4	We organize results around four analyses of increasing specificity: the binary ambiguity effect (C1), the type risk gradient (C2), the aggregate layer effect (C3), and the model$\times$type interaction (C4). C1 and C2 constitute our primary claims; C3 is inconclusive; C4 is exploratory but provides the model$\times$type interaction analysis.
5	
6	\subsection{Binary Ambiguity Effect (C1)}
7	
8	Across all five models and six types, ambiguous clauses increase violation rates by 34.0 pp (41.0\% vs.\ 6.9\%, OR $= 15.1$, 95\% CI $[10.78, 21.17]$, $p < 10^{-105}$). All six types individually produce significant increases (all $p < 10^{-5}$), and all five models show large effects ($+25.7$ to $+39.0$ pp, all $p < 10^{-17}$). Perturbation controls confirm specificity to semantic ambiguity ($n = 300$, $\Delta_{\text{perturb}} = -0.67$\,pp, CI containing zero). A Type III sum-of-squares decomposition (model + type + condition + clause nested within type) on binary violation outcomes yields the following partition: Clause identity explains 22.4\% of variance versus 1.0\% for model identity. This decomposes into 0.4\% between types and 22.0\% within types, indicating that individual clause wording---not type membership---drives the bulk of clause-level variance. While type membership explains only 0.4\% of total variance---because type differences manifest only under ambiguous conditions---the omnibus test on ambiguous episodes confirms significant type heterogeneity ($\chi^2 = 28.02$, $V = 0.137$; Table~\ref{tab:main_results}). The taxonomy's primary value lies not in predicting individual clause risk but in predicting failure mechanisms (\S\ref{sec:discussion}). A replication on two additional model families (Appendix~\ref{app:model_expansion}) confirms the effect across seven models ($\Delta = +20.0$ to $+33.6$\,pp, both $p < 10^{-6}$); excluding incompleteness, it remains large ($\Delta = 31.0$\,pp; Appendix~\ref{app:sans_incomp
…[truncated 7679 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1234 · 2026-05-22T15:00:52.419300+00:00_

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
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/analysis.tex"
  }
}
```

</details>

---


### Tool result

_source line 1235 · 2026-05-22T15:00:52.921318+00:00_

1	\section{Error Analysis \emph{[Exploratory]}}
2	\label{sec:analysis}
3	
4	The following failure mode taxonomy emerges empirically from LLM-coded traces, distinct from the input ambiguity taxonomy (\S\ref{sec:taxonomy}).
5	
6	We analyze 614 violation traces across all five models, coded into five failure modes: unauthorized escalation, assumption-based action, scope misapplication, arbitrary rule selection, and conservative refusal. GPT-5.4 and GPT-4.1 serve as detailed annotation anchors because they span the judge boundary. Inter-coder reliability is substantial (Gwet's AC$_1$ $= 0.62$ \citep{gwet_2014}; Cohen's $\kappa = 0.52$ \citep{cohen_1960}; the gap partly reflects the prevalence paradox). Using LLMs to code LLM failure modes introduces a circularity risk that the moderate $\kappa$ may partly reflect; human-coded validation of at least one failure category would strengthen these findings.
7	
8	\subsection{Type-Specific Failure Mechanisms}
9	
10	The five-model data reveal three mechanistically distinct failure patterns that crosscut the specification/linguistic layer boundary.
11	
12	\emph{Structural misparse} (scope misapplication): the agent constructs an incorrect parse and follows it consistently, paralleling garden-path processing \citep{frazier_rayner_1982,ferreira_good_enough_2002} at a behavioral (not mechanistic) level. This dominates scopal (all 5 models), conditional precedence (all 5), and coreferential (3/5).
13	
14	\emph{Information gap-filling} (assumption-based action): the agent fills missing information with plausible but incorrect defaults. This dominates incompleteness (3/5) and lexical (3/5).
15	
16	\emph{Boundary violation} (unauthorized escalation): the agent exceeds permission boundaries when authorization scope is underspecified; 69.2\% of such violations involve unauthorized escalation with zero conservative refusals ($p < 10^{-4}$, binomial test), revealing systematic permissiveness bias. This dominates authorization scope exclusiv
…[truncated 1893 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1236 · 2026-05-22T15:00:52.921769+00:00_

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
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1237 · 2026-05-22T15:00:52.922050+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Differential nocuity.}
5	Building on \citet{berry_kamsties_2004}'s nocuous/innocuous distinction, our results are consistent with a \emph{differential nocuity} hypothesis \citep{willis_nocuous_2008}: risk depends on ambiguity type (base vulnerability), safety training (selective mitigation), and disambiguation channel availability. Types with explicit decision points (e.g., authorization scope) appear more amenable to both safety training and prompted intervention than gap-filling types (e.g., incompleteness), where mitigation attempts can backfire (see below).
6	
7	\paragraph{Taxonomy as intervention design.}
8	Type membership explains only 0.4\% of violation variance versus 22.4\% for individual clause wording. However, the taxonomy's value lies in predicting failure \emph{mechanisms}: each type maps to a mechanistically distinct failure pattern with cross-model consistency (\S\ref{sec:analysis}). Structural misparse dominates scopal and conditional precedence (5/5 models each), information gap-filling dominates incompleteness and lexical ($\geq$3/5), and boundary violation dominates authorization scope exclusively (5/5, with zero conservative refusals). This type$\to$mechanism mapping enables targeted intervention design even though type membership is a poor predictor of individual clause risk.
9	
10	\paragraph{Prompt-based mitigation.}
11	A matched-pair mitigation study on GPT-5.4 ($n = 50$ per type; Appendix~\ref{app:mitigation}) finds generic awareness prompting ineffective ($\Delta = +1.3$\,pp), with type-specific results mirroring the mechanism taxonomy: authorization scope improves ($-12$\,pp, $p = 0.070$) but incompleteness \emph{worsens} ($+14$\,pp, $p = 0.118$). Opposite directions under different prompt formulations (incompleteness: $-$3.4\,pp in v1 vs.\ $+$14\,pp in v2) reinforce policy-design-level solutions over prompt-level fixes.
12	
13	\paragraph{Practical implications.}
14	A proof-of
…[truncated 279 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1238 · 2026-05-22T15:00:53.373911+00:00_

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
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1239 · 2026-05-22T15:00:53.826511+00:00_

1	\section{Conclusion}
2	
3	Ambiguous policy clauses increase agent safety violations by 34.0\,pp (OR\,$=$\,15.1); clause-level wording drives 22.4\% of variance versus 0.4\% for type and 1.0\% for model. Effects range from $+$18.7\,pp (coreferential) to $+$36.0\,pp (authorization scope) among confound-controlled types, with incompleteness reaching $+$49.2\,pp (upper bound). With disambiguation neglect in $>$89\% of cases and 41.3\% model-convergent violations, type-aware auditing and externalized detection are critical for policy-governed deployments.
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1240 · 2026-05-22T15:00:53.877179+00:00_

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
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 1241 · 2026-05-22T15:00:54.279025+00:00_

1	\section*{Limitations}
2	\label{sec:limitations}
3	
4	\paragraph{Scope.} We evaluate seven API-accessible models from six providers (Appendix~\ref{app:model_expansion}); smaller open-source models (7B--70B) may exhibit different vulnerability patterns. $\tau^2$-bench covers retail and airline customer service only---effects in other domains remain untested, though within-study cross-domain consistency is encouraging. Our matched-pair design requires synthetic ambiguity construction, which may not capture the full distribution of naturally occurring ambiguities; realism validation (\S\ref{sec:method}) confirms lexical comparability but cannot rule out distributional gaps. Coreferential ambiguity was excluded from mitigation and replication experiments due to benchmark-specific structural constraints (Appendix~\ref{app:mitigation}).
5	
6	\paragraph{Measurement.} Each model is evaluated by a single cross-judge, confounding judge identity with model identity; within-judge-group analyses confirm C1 individually (both $p < 0.001$) but not C3 (Appendix~\ref{app:judge_group_ranking}), and cross-model type ranking concordance is only moderate (Appendix~\ref{app:kendall_w}). Most critically, cross-judge-group type rankings show near-zero correlation ($\rho = 0.09$, $p = 0.87$; Appendix~\ref{app:judge_group_ranking}), meaning that the C2 gradient's mid-tier ordering does not generalize across judge groups---though excluding authorization scope yields strong concordance ($\rho = 0.90$, $p = 0.037$), and incompleteness as the highest-risk type is robust to this variation. Per-type reliability varies---authorization scope has the lowest agreement ($\kappa = 0.385$) and per-type human--LLM estimates rest on small cell sizes with wide confidence intervals (Appendix~\ref{app:per_type_agreement})---while failure mode coding achieves moderate agreement ($\kappa = 0.52$), with minority categories less reliable. Both judges belong to the OpenAI model family, so systematic leniency tow
…[truncated 990 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 1242 · 2026-05-22T15:00:54.279435+00:00_

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
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 1243 · 2026-05-22T15:00:55.032386+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Ambiguity in NLP and requirements engineering.}
5	Ambiguity has been studied extensively in both computational linguistics and software engineering. Word sense disambiguation \citep{navigli_wsd_2009} addresses lexical ambiguity at the token level; our lexical type extends this to policy-specific polysemy. \citet{li_ambiguity_taxonomy_2024} propose an 11-type NLP taxonomy covering syntactic, semantic, and pragmatic ambiguity, from which we draw our linguistic-layer types. \citet{kamath_scope_2024} investigate scopal ambiguity in LLMs, finding systematic preferences for surface scope. In requirements engineering (RE), \citet{massey_ambiguity_re_2014} classify six ambiguity types in regulatory texts, and \citet{berry_kamsties_2004} introduce the distinction between nocuous ambiguity (where stakeholders diverge on interpretation) and innocuous ambiguity (where they converge). Computational detection of nocuous ambiguity has progressed from heuristic methods \citep{chantree_2006,willis_nocuous_2008} through NLP-based cross-domain detectors \citep{ferrari_ambiguity_2019,ferrari_defects_2018} to transformer-based approaches for anaphoric ambiguity \citep{ezzini_taphsir_2022,ezzini_anaphoric_2022}. \citet{zhao_nlp4re_2021} survey the broader NLP4RE landscape. Our work extends Berry and Kamsties' framework to LLM agents, where the absence of shared organizational context makes previously innocuous ambiguity nocuous.
6	
7	\paragraph{Psycholinguistics of ambiguity processing.}
8	\citet{ferreira_good_enough_2002} show that human comprehenders build shallow, ``good-enough'' representations rather than full parses, paralleling our observation that LLM agents adopt surface interpretations. \citet{frazier_rayner_1982} demonstrate early commitment to a single parse; \citet{li_garden_path_llm_2024} provide direct evidence that LLMs exhibit analogous garden-path effects. At the pragmatic level, \citet{hu_pragmatic_202
…[truncated 2894 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 752
}
```

</details>

---


### Tool call

_source line 1244 · 2026-05-22T15:00:55.083058+00:00_

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
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/taxonomy.tex"
  }
}
```

</details>

---


### Tool result

_source line 1245 · 2026-05-22T15:00:55.133686+00:00_

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
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1246 · 2026-05-22T15:01:00.053141+00:00_

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
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 1247 · 2026-05-22T15:01:00.204498+00:00_

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
…[truncated 23595 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 1248 · 2026-05-22T15:01:09.591590+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "policy_ambiguity_safety"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "policy_ambiguity_safety"
  }
}
```

</details>

---


### Tool result

_source line 1249 · 2026-05-22T15:01:10.947936+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 1356
}
```

</details>

---


### Tool call

_source line 1250 · 2026-05-22T15:01:11.099055+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "wc -l /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/*.tex",
  "description": "Count lines per section file"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Bash",
  "tool_args": {
    "command": "wc -l /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/*.tex",
    "description": "Count lines per section file"
  }
}
```

</details>

---


### Tool result

_source line 1251 · 2026-05-22T15:01:11.200180+00:00_

    3 /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/abstract.tex
   28 /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/analysis.tex
  316 /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/appendix.tex
    3 /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/conclusion.tex
   14 /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/discussion.tex
   66 /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/experiments.tex
   21 /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/introduction.tex
   11 /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/limitations.tex
   34 /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/method.tex
   13 /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/related_work.tex
   41 /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/taxonomy.tex
  550 total

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Bash",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1252 · 2026-05-22T15:01:16.470690+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/agent/config.yaml 2>/dev/null | head -80",
  "description": "Read project config for external review settings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/agent/config.yaml 2>/dev/null | head -80",
    "description": "Read project config for external review settings"
  }
}
```

</details>

---


### Tool result

_source line 1253 · 2026-05-22T15:01:16.521448+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1254 · 2026-05-22T15:01:19.785309+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/policy_ambiguity_safety/**/config*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/policy_ambiguity_safety/**/config*.yaml",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4"
  }
}
```

</details>

---


### Tool result

_source line 1255 · 2026-05-22T15:01:19.885946+00:00_

/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.venv/lib/python3.14/site-packages/configs/config.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Glob",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1256 · 2026-05-22T15:01:22.998317+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety -maxdepth 3 -name \"*.yaml\" -not -path \"*/.venv/*\" 2>/dev/null",
  "description": "Find YAML config files in project dir"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety -maxdepth 3 -name \"*.yaml\" -not -path \"*/.venv/*\" 2>/dev/null",
    "description": "Find YAML config files in project dir"
  }
}
```

</details>

---


### Tool result

_source line 1257 · 2026-05-22T15:01:23.099284+00:00_

/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/distill_tmp/phantompolicy_2026.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/distill_tmp/berry_kamsties_2004.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/distill_tmp/policybank_2026.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/distill_tmp/agentpex_2026.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/distill_tmp/drip_r_2026.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/distill_tmp/lhaw_2026.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/distill_tmp/shieldagent_2025.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/distill_tmp/li_ambiguity_taxonomy_2024.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/distill_tmp/chantree_2006.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/distill_tmp/massey_ambiguity_re_2014.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/distill_tmp/mantra_2026.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/distill_tmp/tau2_bench_2025.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/distill_tmp/agentauditor_2025.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/dream_registry.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/writing_plan.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/literature_map.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/registry.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects
…[truncated 463 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1258 · 2026-05-22T15:01:28.470501+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4 -maxdepth 2 -name \"*.yaml\" -not -path \"*/projects/*\" -not -path \"*/.venv/*\" 2>/dev/null | head -10",
  "description": "Find top-level config files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4 -maxdepth 2 -name \"*.yaml\" -not -path \"*/projects/*\" -not -path \"*/.venv/*\" 2>/dev/null | head -10",
    "description": "Find top-level config files"
  }
}
```

</details>

---


### Tool result

_source line 1259 · 2026-05-22T15:01:28.521205+00:00_

/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/idea_generator/ideas.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/global/approvals.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/config/approvals.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/config/backend.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/config/feishu.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/config/venue_registry.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/config/resources.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/workspace.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1260 · 2026-05-22T15:01:31.996343+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"external_review\" /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/config/ 2>/dev/null; grep -r \"external_review\" /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/workspace.yaml 2>/dev/null; grep -r \"paperreview\" /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/config/ 2>/dev/null",
  "description": "Search for external review config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -r \"external_review\" /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/config/ 2>/dev/null; grep -r \"external_review\" /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/workspace.yaml 2>/dev/null; grep -r \"paperreview\" /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/config/ 2>/dev/null",
    "description": "Search for external review config"
  }
}
```

</details>

---


### Tool result

_source line 1261 · 2026-05-22T15:01:32.097180+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1262 · 2026-05-22T15:01:48.608217+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "policy_ambiguity_safety",
  "review_chat_id": "oc_967344d166ba485ad606d14379e69d85"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "policy_ambiguity_safety",
    "review_chat_id": "oc_967344d166ba485ad606d14379e69d85"
  }
}
```

</details>

---


### Tool result

_source line 1263 · 2026-05-22T15:02:08.793052+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 20184
}
```

</details>

---


### Tool call

_source line 1264 · 2026-05-22T15:02:10.550106+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "你是 Reviewer 1，负责**方法严谨性**审查。\n\n## 投稿信息\n- **Venue**: EMNLP 2026 via ACL Rolling Review (ARR)\n- **类别**: Long Paper\n- **Deadline**: 2026-05-25\n- **格式**: ACL template (acl.sty), double-blind, 正文 8 页限制 + unlimited references\n- **Limitations**: 必选章节，不计页数\n- **论文路径**: `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_14/submitted.pdf`\n\n## 你的审查侧重\n\n**方法严谨性 + 实验设计 + 统计分析**，具体包括：\n\n1. **实验设计有效性**：matched-pair design 是否足够支撑因果推断？perturbation control 是否充分排除混淆？300 clause pairs 的样本量是否充足？\n2. **统计分析正确性**：McNemar's test / Fisher's exact / TOST 的使用是否恰当？多重比较校正是否充分？SESOI ±15pp 的论证是否合理？方差分解方法是否恰当？\n3. **Cross-judge 评估设计**：GPT-5.4 判 3 个模型、GPT-4.1 判 2 个模型——这种非对称设计是否引入系统性偏差？judge 都来自 OpenAI 家族是否构成严重威胁？cross-judge ρ=0.09 对 C2 gradient 可信度的影响？\n4. **Claims 与证据匹配度**：四个 claims (C1-C4) 的证据支撑是否充分？是否存在 overclaiming？特别关注：\n   - C1: perturbation control CI 上界 6.67pp 是否足够排除 surface perturbation 解释？\n   - C2: type 仅解释 0.4% variance，但论文标题和叙事暗示 type 是强预测因子——是否存在 framing-evidence 张力？\n   - C3: 作者自认 inconclusive，是否还需要保留？\n   - C4: 完全集中在 authorization scope (排除后 p=0.97)——是否 overclaimed？\n5. **Controls 充分性**：信息量混淆（incompleteness）的处理是否足够？token count 作为信息量代理是否过于粗糙？\n6. **Reproducibility**：ICC=0.919 仅在 OpenAI 家族内计算，cross-provider replicability 是否被高估？\n7. **Error Analysis 方法**：LLM 编码 LLM failure modes 的 circularity risk——κ=0.52 是否足够？\n\n请按照 ARR 审稿标准给出完整审稿意见，包括：Summary、Strengths、Weaknesses（按 Must-Fix / Should-Fix / Nice-to-Fix 分级）、Questions、Missing References、Overall Assessment（使用 EMNLP 2026 ARR 评分标准：1-5 分）。",
  "project": "policy_ambiguity_safety",
  "chat_id": "oc_967344d166ba485ad606d14379e69d85",
  "director_session_key": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "你是 Reviewer 1，负责**方法严谨性**审查。\n\n## 投稿信息\n- **Venue**: EMNLP 2026 via ACL Rolling Review (ARR)\n- **类别**: Long Paper\n- **Deadline**: 2026-05-25\n- **格式**: ACL template (acl.sty), double-blind, 正文 8 页限制 + unlimited references\n- **Limitations**: 必选章节，不计页数\n- **论文路径**: `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_14/submitted.pdf`\n\n## 你的审查侧重\n\n**方法严谨性 + 实验设计 + 统计分析**，具体包括：\n\n1. **实验设计有效性**：matched-pair design 是否足够支撑因果推断？perturbation control 是否充分排除混淆？300 clause pairs 的样本量是否充足？\n2. **统计分析正确性**：McNemar's test / Fisher's exact / TOST 的使用是否恰当？多重比较校正是否充分？SESOI ±15pp 的论证是否合理？方差分解方法是否恰当？\n3. **Cross-judge 评估设计**：GPT-5.4 判 3 个模型、GPT-4.1 判 2 个模型——这种非对称设计是否引入系统性偏差？judge 都来自 OpenAI 家族是否构成严重威胁？cross-judge ρ=0.09 对 C2 gradient 可信度的影响？\n4. **Claims 与证据匹配度**：四个 claims (C1-C4) 的证据支撑是否充分？是否存在 overclaiming？特别关注：\n   - C1: perturbation control CI 上界 6.67pp 是否足够排除 surface perturbation 解释？\n   - C2: type 仅解释 0.4% variance，但论文标题和叙事暗示 type 是强预测因子——是否存在 framing-evidence 张力？\n   - C3: 作者自认 inconclusive，是否还需要保留？\n   - C4: 完全集中在 authorization scope (排除后 p=0.97)——是否 overclaimed？\n5. **Controls 充分性**：信息量混淆（incompleteness）的处理是否足够？token count 作为信息量代理是否过于粗糙？\n6. **Reproducibility**：ICC=0.919 仅在 OpenAI 家族内计算，cross-provider replicability 是否被高估？\n7. **Error Analysis 方法**：LLM 编码 LLM failure modes 的 circularity risk——κ=0.52 是否足够？\n\n请按照 ARR 审稿标准给出完整审稿意见，包括：Summary、Strengths、Weaknesses（按 Must-Fix / Should-Fix / Nice-to-Fix 分级）、Questions、Missing References、Overall Assessment（使用 EMNLP 2026 ARR 评分标准：1-5 分）。",
    "project": "policy_ambiguity_safety",
    "chat_id": "oc_967344d166ba485ad606d14379e69d85",
    "director_session_key": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
  }
}
```

</details>

---


### Tool result

_source line 1265 · 2026-05-22T15:02:26.442476+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 15892
}
```

</details>

---


### Tool call

_source line 1266 · 2026-05-22T15:02:27.047394+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "你是 Reviewer 2，负责**新颖性/完整性**审查。\n\n## 投稿信息\n- **Venue**: EMNLP 2026 via ACL Rolling Review (ARR)\n- **类别**: Long Paper\n- **Deadline**: 2026-05-25\n- **格式**: ACL template (acl.sty), double-blind, 正文 8 页限制 + unlimited references\n- **Limitations**: 必选章节，不计页数\n- **论文路径**: `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_14/submitted.pdf`\n\n## 你的审查侧重\n\n**新颖性 + Related Work 覆盖 + Framing 质量 + 完整性**，具体包括：\n\n1. **新颖性评估**：这是否是对领域的实质性贡献？matched-pair causal study 在 policy ambiguity + agent safety 交叉领域是否确实是首次？与 DRIP-R (2026)、PolicyBank (2026)、AgentPex (2026) 等并行工作的区别是否足够清晰？\n2. **Related Work 覆盖**：是否遗漏重要相关工作？特别关注：\n   - Ambiguity in NLP / requirements engineering 方向的覆盖\n   - Agent safety evaluation 领域最新进展\n   - Psycholinguistics（garden-path、good-enough processing）引用是否恰当\n   - 是否有遗漏的 2025-2026 新论文？\n3. **Framing 一致性**：\n   - 标题 \"Not All Policy Ambiguity Is Equal\" 暗示 type 是强预测因子，但 type 仅解释 0.4% variance——framing 是否与结果一致？\n   - Abstract/Introduction 的 claims 是否在 Results/Discussion 中得到支撑？\n   - Contribution list 中的表述是否准确？\n   - \"taxonomy as intervention design\" 这个重新定位是否令人信服？\n4. **呈现质量**：\n   - 论文结构是否清晰，叙事是否连贯？\n   - Figures/Tables 是否有效支撑论述？\n   - 是否存在 hedging 不足或 overclaiming？\n   - 术语使用是否一致（\"Disambiguation Neglect\" 等新术语定义是否清晰）？\n5. **Taxonomy 设计**：六类分类是否合理？\"ambiguity\" 的宽泛定义（包括 incompleteness 和 conditional precedence）是否令人信服？两层结构（linguistic vs specification）的价值如何？\n6. **Domain generalizability**：研究仅覆盖 retail + airline customer service——generalizability claims 是否过度？Abstract 与 Conclusion 的 scope 措辞是否一致？\n7. **格式合规**：正文是否在 8 页以内？匿名是否到位？ACL 格式要求是否满足？\n\n请按照 ARR 审稿标准给出完整审稿意见，包括：Summary、Strengths、Weaknesses（按 Must-Fix / Should-Fix / Nice-to-Fix 分级）、Questions、Missing References、Overall Assessment（使用 EMNLP 2026 ARR 评分标准：1-5 分）。",
  "project": "policy_ambiguity_safety",
  "chat_id": "oc_967344d166ba485ad606d14379e69d85",
  "director_session_key": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "你是 Reviewer 2，负责**新颖性/完整性**审查。\n\n## 投稿信息\n- **Venue**: EMNLP 2026 via ACL Rolling Review (ARR)\n- **类别**: Long Paper\n- **Deadline**: 2026-05-25\n- **格式**: ACL template (acl.sty), double-blind, 正文 8 页限制 + unlimited references\n- **Limitations**: 必选章节，不计页数\n- **论文路径**: `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_14/submitted.pdf`\n\n## 你的审查侧重\n\n**新颖性 + Related Work 覆盖 + Framing 质量 + 完整性**，具体包括：\n\n1. **新颖性评估**：这是否是对领域的实质性贡献？matched-pair causal study 在 policy ambiguity + agent safety 交叉领域是否确实是首次？与 DRIP-R (2026)、PolicyBank (2026)、AgentPex (2026) 等并行工作的区别是否足够清晰？\n2. **Related Work 覆盖**：是否遗漏重要相关工作？特别关注：\n   - Ambiguity in NLP / requirements engineering 方向的覆盖\n   - Agent safety evaluation 领域最新进展\n   - Psycholinguistics（garden-path、good-enough processing）引用是否恰当\n   - 是否有遗漏的 2025-2026 新论文？\n3. **Framing 一致性**：\n   - 标题 \"Not All Policy Ambiguity Is Equal\" 暗示 type 是强预测因子，但 type 仅解释 0.4% variance——framing 是否与结果一致？\n   - Abstract/Introduction 的 claims 是否在 Results/Discussion 中得到支撑？\n   - Contribution list 中的表述是否准确？\n   - \"taxonomy as intervention design\" 这个重新定位是否令人信服？\n4. **呈现质量**：\n   - 论文结构是否清晰，叙事是否连贯？\n   - Figures/Tables 是否有效支撑论述？\n   - 是否存在 hedging 不足或 overclaiming？\n   - 术语使用是否一致（\"Disambiguation Neglect\" 等新术语定义是否清晰）？\n5. **Taxonomy 设计**：六类分类是否合理？\"ambiguity\" 的宽泛定义（包括 incompleteness 和 conditional precedence）是否令人信服？两层结构（linguistic vs specification）的价值如何？\n6. **Domain generalizability**：研究仅覆盖 retail + airline customer service——generalizability claims 是否过度？Abstract 与 Conclusion 的 scope 措辞是否一致？\n7. **格式合规**：正文是否在 8 页以内？匿名是否到位？ACL 格式要求是否满足？\n\n请按照 ARR 审稿标准给出完整审稿意见，包括：Summary、Strengths、Weaknesses（按 Must-Fix / Should-Fix / Nice-to-Fix 分级）、Questions、Missing References、Overall Assessment（使用 EMNLP 2026 ARR 评分标准：1-5 分）。",
    "project": "policy_ambiguity_safety",
    "chat_id": "oc_967344d166ba485ad606d14379e69d85",
    "director_session_key": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
  }
}
```

</details>

---


### Tool result

_source line 1267 · 2026-05-22T15:02:28.571716+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1524
}
```

</details>

---


### Assistant

_source line 1268 · 2026-05-22T15:02:39.041919+00:00_

Round 1 独立审稿已启动：

- **视觉审查 Agent**：已派发（fire-and-forget）
- **Reviewer 1**（方法严谨性）：已分配
- **Reviewer 2**（新颖性/完整性）：已分配
- **外部审稿**：项目未配置，跳过

等待两位 Reviewer 返回初审意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 116

## Round 116

2 recorded events


### User

_source line 1269 · 2026-05-22T15:08:53.309281+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 审稿意见（新颖性/完整性审查）

### Paper Summary

本文研究政策歧义类型与 LLM agent 安全违规之间的因果关系。作者构建了 300 对匹配子句对，覆盖六类歧义（语言层：词汇、辖域、共指；规格层：不完整性、授权范围、条件优先级），在 τ²-bench 上评估五个模型（2,997 episodes）。主要发现：(1) 歧义子句使违规率增加 34.0pp (OR=15.1)；(2) 类型效应从 +18.7pp（共指）到 +49.2pp（不完整性，含信息添加混淆）形成梯度；(3) 类型仅解释 0.4% 方差（子句措辞 22.4%，模型 1.0%）；(4) agent 在 >89% 情况下表现出 "消歧忽略"。

---

## 总体评分

**Overall**: 3.5 (Borderline Conference)

**一句话总结**: 方法论上严谨的匹配对因果研究，但论文标题/framing 与核心实证发现之间存在根本性张力——标题暗示类型是强区分因子，但类型仅解释 0.4% 方差，且 cross-judge type ranking 几乎为零相关（ρ=0.09）。

---

## 官方维度打分（基于 ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 匹配对设计和扰动控制方法论严谨；但不完整性混淆（信息添加）未完全消除，cross-judge ρ=0.09 实质削弱 C2 |
| Excitement | 3.5/5 | 首个因果量化"政策歧义→agent 安全违规"的研究，Disambiguation Neglect 概念有价值；但 0.4% 方差解释力使类型分级的实际意义受限 |
| Reproducibility | 4/5 | 实验细节充分，承诺开源代码和数据；ICC=0.919 的复现性令人满意 |
| Reviewer Confidence | 4/5 | 熟悉 agent safety evaluation、NLP ambiguity、requirements engineering 领域 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] **标题/Framing 与核心结果之间的根本张力**

- 具体位置：Title, Abstract, §5.1 (C1), §5.2 (C2), §7 Discussion "Taxonomy as intervention design"
- 问题：标题 "Not All Policy Ambiguity Is Equal" 强烈暗示类型是重要的差异化预测因子。但 §5.1 揭示类型仅解释 0.4% 的违规方差（vs. 子句措辞 22.4%，模型 1.0%）。论文在 §7 才将 taxonomy 重新定位为 "intervention design tool"（预测失败机制而非个体风险），但这种重新定位是事后的——标题、摘要（"per-type effects range from +18.7pp to +49.2pp"）和引言的贡献列表都以类型分级为核心叙事。
  
  更关键的是，cross-judge type ranking 的 Spearman ρ=0.09（§5.2, Limitations）意味着两个评判组无法就类型排序达成一致。虽然排除 authorization scope 后 ρ=0.90，但这本身就意味着 6 类中有 1 类的排名不稳定，削弱了"梯度"叙事的可靠性。
  
- 为什么影响接收：如果论文最重要的贡献是类型分级（C2），但类型解释的方差微乎其微且排名不稳定，reviewer 会质疑该工作的实质性贡献。如果最重要的贡献其实是 C1（歧义的因果效应）和 Disambiguation Neglect，则应当围绕这些重新组织叙事。
- 建议修改方向：(a) 修改标题以更准确反映核心发现——例如 "Policy Ambiguity Causes Systematic Safety Violations in LLM Agents" 或保留当前标题但在 Abstract 第一句就引入 0.4% variance 的 qualification；(b) 将 "taxonomy as intervention design" 的论证从 §7 前置到 §1 的贡献列表中，使读者从一开始就知道 taxonomy 的价值在于机制映射而非方差解释；(c) 在 Abstract 中明确区分 confound-free range (+18.7 to +36.0pp) 和 upper bound (+49.2pp)。

**N2** [critical] **不完整性（Incompleteness）作为"歧义"的概念正当性不足**

- 具体位置：§3 "Scope of ambiguity" 段落, Table 1
- 问题：论文自己承认不完整性"involves absent information rather than multiple readings"，条件优先级涉及"normative conflict rather than interpretive uncertainty"（§3, 第 41 行）。将这些纳入"歧义"分类法的依据是 LLM agent 在行为上无法区分它们，但这混淆了语言现象与行为效应。更重要的是，不完整性是效应量最大的类型（+49.2pp），也是最受混淆影响的类型（信息添加效应），且其 unambiguous variant 实际上是添加了新信息——这不是"消歧"而是"补全"。尽管 Appendix 的 logistic regression 控制了部分混淆，但信息量不对称是结构性的，无法完全通过统计控制消除。

  这意味着论文最引人注目的数字（49.2pp）同时也是概念上最脆弱的。
  
- 为什么影响接收：如果审稿人认为 incompleteness 不属于歧义，那么最大效应量就不可靠，整个梯度叙事也被削弱。
- 建议修改方向：(a) 更显著地在主文中承认这一概念张力，而不仅仅在 §3 的一个段落中轻描淡写；(b) 考虑在主结果中同时呈现"含不完整性"和"不含不完整性"的效应范围（目前仅在 Appendix Q 中给出 sans-incompleteness 分析）；(c) 或者重新命名为 "specification gaps" 而非 "ambiguity types"，统一术语。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] **领域泛化性声明过度**

- 具体位置：Abstract ("policy-governed deployments"), Conclusion ("policy-governed deployments"), §8
- 问题：研究仅覆盖 retail 和 airline customer service 两个密切相关的客户服务领域。Abstract 和 Conclusion 中的 "policy-governed deployments" 暗示了比实际证据范围更广的适用性。虽然 Limitations 提到了这一点，但 Abstract/Conclusion 的措辞应该更加收敛。τ²-bench 的两个 domain 都是低风险客户服务场景——金融合规、医疗协议、法律条款等高风险领域的歧义可能呈现完全不同的模式。
- 建议：在 Abstract 和 Conclusion 中显式限定为 "customer-service policy domains"，将泛化留给未来工作。

**W2** [warning] **Cross-judge 设计混淆 judge 和 model 效应**

- 具体位置：§4.4 Evaluation, §5.4 C4, Limitations
- 问题：GPT-5.4 评判 Claude/GPT-4.1/Qwen3，GPT-4.1 评判 GPT-5.4/DeepSeek。这意味着 C4（model×type interaction）中 authorization scope 的 52pp 跨模型差异可能部分反映 judge 差异而非真正的模型差异。论文承认这一点并指出 within-judge-group 分析支持 C1，但 C2 的类型排名实际上受 judge group 分割的影响——这就是 ρ=0.09 的根源。两个 judge 都属于 OpenAI 模型家族这一事实进一步加剧了同族偏好的担忧。
- 建议：(a) 在主文中更明确地讨论 judge-model confound 对 C2 的影响；(b) 考虑对至少一个子集进行双 judge 交叉验证。

**W3** [warning] **"Taxonomy as intervention design" 论证不完整**

- 具体位置：§7 Discussion, §6.1
- 问题：论文将 taxonomy 的价值重新定位为预测失败机制（structural misparse vs. information gap-filling vs. boundary violation），但这一论证的证据基础是 LLM-coded 的 614 条 violation traces（§6），coder 间可靠性中等（κ=0.52）。论文自己承认 "Using LLMs to code LLM failure modes introduces a circularity risk"。如果 intervention design 是 taxonomy 的核心价值主张，那么支撑这一主张的 error analysis 需要更强的信度保证——至少需要人工编码的部分验证。
- 建议：对至少 100 条 traces 进行人工 failure mode 编码验证，或者降低对这一主张的确信度。

**W4** [warning] **与 DRIP-R 的区分虽然明确但存在一个重要遗漏**

- 具体位置：§2 Related Work "Policy specification for agents" 段落
- 问题：论文在 §2 中清楚区分了与 DRIP-R 的三个差异（匹配对设计、安全违规 vs. 决策质量、两层 taxonomy + model×type interaction）。但 DRIP-R 的核心发现——"frontier models fundamentally disagree on identical policy-ambiguous scenarios"——实际上与本文的 Systematic Nocuity 发现（41.3% 子句触发多数模型趋同违规）存在有趣的张力：DRIP-R 发现模型间分歧，而本文发现模型间趋同。论文没有讨论这一差异的可能原因（任务设计差异？歧义类型差异？评估标准差异？）。
- 建议：在 §2 或 §7 中简要讨论为什么两个研究得出看似相反的模型一致性结论。

**W5** [warning] **Disambiguation Neglect 的新颖性边界需要更清晰**

- 具体位置：§6.2, §1 Contribution (3)
- 问题：论文将 Disambiguation Neglect 定位为将 LLM ambiguity-collapse findings (Liu et al., 2023; Hu et al., 2025) 扩展到 agentic settings。但 "LLMs commit to a single interpretation without flagging uncertainty" 已经是 Liu et al. (2023) 和 Sedova et al. (2024) 的核心发现。本文的增量贡献是什么？论文提到 "consequentiality" 是区分因素，但没有系统论证为什么 agentic 场景的消歧忽略比非 agentic 场景的更值得关注——直觉上显然如此，但论文应该更明确地说明。
- 建议：更清晰地说明 Disambiguation Neglect 相比 ambiguity collapse 的增量贡献——是定量测量（4.6%）本身？还是与不可逆行动的结合？还是在 multi-turn 对话场景中的表现？

---

## 小问题（不影响接收）

- §1 第二段开头 "LLM-based agents increasingly operate under..." 与第一段的叙事开头（具体场景）之间的过渡略显突兀
- §5.2 "statistical power = 0.993 at the observed effect" — 事后功效分析（observed effect power）几乎总是高的，因为它本质上重述了显著的 p 值。应删除或替换为先验 power 分析
- Table 2 的 caption 很长，可以考虑简化
- §6 标题标注为 [Exploratory]，但 §5.4 (C4) 也标注为 [Exploratory]——两者是否应该合并？
- Figure 2 的 y 轴标签 "Violation rate (percentage-point increase)" 中 "increase" 应该更明确为 "increase relative to unambiguous control"

---

## Missing References

1. **ATBench** (2026) — 最近的 agent trajectory safety evaluation benchmark，与本文的 trace-level error analysis 相关，值得在 §2 agent safety evaluation 段落中提及
2. **Risky-Bench** (2026) — probing agentic safety risks under real-world deployment，涵盖了 policy violation 场景
3. **ICSME 2025 industrial study** — requirements ambiguity detection and explanation with LLMs，直接相关于 §7 的 proof-of-concept classifier discussion
4. 建议确认 Sehwag et al. (2026) 引用（§2 psycholinguistics 段落末尾）的完整信息——这是一篇非常新的 preprint，确保引用准确

---

## 主要优势

1. **匹配对因果设计**：这是该交叉领域首个建立因果关系（而非仅相关性）的研究。扰动控制（Δperturb = -0.67pp, CI含零）有效排除了表面修改的效应。这一方法论贡献独立于结果也有价值。

2. **诚实的 claim 校准**：论文在方差分解（0.4% for type）、cross-judge ρ=0.09、不完整性混淆等方面表现出不常见的诚实度。C3 标记为 inconclusive，C4 标记为 exploratory——这种 calibration 在投稿中难得。

3. **系统性的统计框架**：TOST equivalence testing + bootstrap cluster analysis + 七个 margin 的灵敏度分析，避免了简单的 NHST 二分法。Holm-Bonferroni correction 在三个预注册检验族内应用。

4. **Practical implications 落地**：proof-of-concept classifier (F1=0.81 binary detection)、prompt-based mitigation 的反直觉发现（incompleteness 恶化+14pp）——这些让研究不仅停留在诊断层面。

5. **概念贡献**：Systematic Nocuity（41.3% 子句触发模型趋同违规）和 Disambiguation Neglect 为领域引入了有价值的分析框架。

6. **Related Work 覆盖充分**：准确定位了与 DRIP-R、PolicyBank、AgentPex 等并行工作的差异，psycholinguistics 的引用（Ferreira 2002, Frazier & Rayner 1982）恰当。

---

## Questions for Authors

1. 如果 taxonomy 的核心价值是 intervention design（预测失败机制），为什么不以此作为论文的主叙事，而是保留了一个暗示 type-level prediction power 的标题？
2. 是否考虑过对不完整性使用"信息等量"的实验设计——即 unambiguous variant 不添加新信息，而是重组现有信息使其更明确？这能否消除信息添加混淆？
3. Cross-judge ρ=0.09 的结果在投稿前是否考虑过对 C2 的影响？如果提前预注册了这一分析，这是否会改变 C2 作为 "primary claim" 的地位？
4. 614 条 violation traces 的 failure mode coding 是否有计划进行人工验证？这对 intervention design 主张至关重要。

---

**总结**：这是一篇方法论上认真的工作，matched-pair 因果设计和诚实的 claim calibration 值得肯定。但论文最大的问题是 framing——标题和叙事结构暗示了类型分级的重要性，而数据支持的故事其实是"歧义的因果效应很大（+34pp），但类型区分很弱（0.4%），真正有趣的是失败机制映射和消歧忽略"。如果能重新组织 framing 使其与数据对齐，这会是一篇更有说服力的论文。当前评分 3.5——framing 修正后有望提升至 4.0。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1270 · 2026-05-22T15:09:01.540497+00:00_

Reviewer 2 审稿意见已收到。等待 Reviewer 1 完成独立审稿后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 117

## Round 117

2 recorded events


### User

_source line 1271 · 2026-05-22T15:09:06.275446+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

**评分：Overall 3.5 (Borderline Conference)**

核心发现：

- **2 个 Must-Fix**：(1) 标题/framing 与 0.4% 方差解释力的根本张力——标题暗示类型是强预测因子，但数据不支持；(2) 不完整性作为"歧义"的概念正当性不足，且其 +49.2pp 效应受信息添加混淆。

- **5 个 Should-Fix**：领域泛化性声明过度、cross-judge 设计混淆、intervention design 论证信度不足、与 DRIP-R 的模型一致性张力未讨论、Disambiguation Neglect 的增量贡献边界模糊。

- **主要优势**：匹配对因果设计是该交叉领域首个、claim calibration 诚实（C3 标为 inconclusive, C4 标为 exploratory）、统计框架系统完整。framing 修正后有望提升至 4.0。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1272 · 2026-05-22T15:09:11.622261+00:00_

Reviewer 2 意见已收到。等待 Reviewer 1 返回后进行交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 118

## Round 118

6 recorded events
