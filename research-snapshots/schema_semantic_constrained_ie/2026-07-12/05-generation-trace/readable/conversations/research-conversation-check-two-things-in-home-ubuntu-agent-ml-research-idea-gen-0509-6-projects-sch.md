# Research conversation: Check two things in /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_p

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 7
- **Recorded user turns:** 1
- **Tool calls:** 2
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-ab1cdc73b714a8d92.jsonl`
- **Structured JSON:** [`a481534a537f102bff16.json`](../../sessions/a4/a481534a537f102bff16.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

7 recorded events

### User

_source line 1 · 2026-05-25T20:50:30.172Z_

Check two things in /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/:

1. In abstract.tex: verify the latency claim says "unconstrained latency" (not just "latency"). Look for the ~1.5× text.

2. In appendix_discussion.tex: verify that the post-hoc filtering table (around the \label{tab:posthoc-extended} area) has:
   - A $^\ddagger$ marker on the Qwen DocRED FT row
   - A footnote in the caption explaining "4096-context LoRA variant"

Report pass/fail for each.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "3c296d38-0878-4eb6-acb2-f95c59b3b113",
  "agentId": "ab1cdc73b714a8d92",
  "type": "user",
  "uuid": "7a8c628a-97b2-4a7c-b1c7-9674651eac01",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "fa54a58a-15c0-4802-9034-a220e6d2d3d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "wild-sauteeing-hare"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-25T20:50:31.518Z_

I'll check both files for the specified details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7a8c628a-97b2-4a7c-b1c7-9674651eac01",
  "isSidechain": true,
  "agentId": "ab1cdc73b714a8d92",
  "requestId": "req_011CbPwtovZBajh2CFnodsQD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2bb79a69-1965-4086-945c-7d1494c90763",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "fa54a58a-15c0-4802-9034-a220e6d2d3d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "wild-sauteeing-hare",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01M8DebJJC1Nrcz2yPYpDajU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 20183,
      "cache_read_input_tokens": 33755,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 20183,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-25T20:50:31.972Z_

<details open><summary>🔧 Tool call — Read · `toolu_01EJaSdKULHNS7t54nPJrMj7`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2bb79a69-1965-4086-945c-7d1494c90763",
  "isSidechain": true,
  "agentId": "ab1cdc73b714a8d92",
  "requestId": "req_011CbPwtovZBajh2CFnodsQD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1093bcde-9336-4391-b3cc-bd60e1b05e46",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "fa54a58a-15c0-4802-9034-a220e6d2d3d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "wild-sauteeing-hare",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01M8DebJJC1Nrcz2yPYpDajU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 20183,
      "cache_read_input_tokens": 33755,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 20183,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-25T20:50:31.981Z_

<details><summary>↩ Tool result · `toolu_01EJaSdKULHNS7t54nPJrMj7`</summary>

```text
1	\begin{abstract}
2	Large language models for information extraction generate structurally valid but ontologically invalid triples: entity types that violate the schema's domain/range constraints for the predicted relation.
3	These domain/range violations (DR) persist even after fine-tuning and cannot be resolved by grammar-constrained decoding, which lacks cross-field type awareness.
4	We present \textsc{OntoCoDec} (\textbf{Onto}logy-\textbf{Co}mpiled \textbf{Dec}oding), a two-layer constrained decoding framework that compiles IE ontologies into token-level masks: a grammar layer enforces structural validity; a semantic layer enforces type constraints at runtime via stateful masking over a dynamic entity registry.
5	% exp_ids: w5_lora_scierc_constrained_eval, w5_qwen_docred_lora_constrained_eval, w5_llama_lora_scierc_constrained_eval, w5_llama_docred_lora_constrained_eval
6	The two layers interact non-additively: grammar-only reduces DR by 3\% and semantic-only by 24\%, yet their composition achieves 94\%.
7	Composed with LoRA fine-tuning across three model families and two relation extraction datasets (up to 96 relations), OntoCoDec reduces DR to $\leq$\,0.21\% with minimal F1 impact ($\pm$0.3\,pp), converting irrecoverable type errors into correctable cross-field inconsistencies; beam search ($k{=}4$) achieves near-zero violations at ${\sim}$1.5$\times$ unconstrained latency.
8	Validation on a 70B model shows the semantic layer's independent effectiveness grows from 24\% to 84\% DR reduction with scale\footnote{Code and data are available at \url{https://anonymous.4open.science/r/schema_semantic_constrained_ie-FE20/}.}.
9	\end{abstract}
10	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1093bcde-9336-4391-b3cc-bd60e1b05e46",
  "isSidechain": true,
  "promptId": "3c296d38-0878-4eb6-acb2-f95c59b3b113",
  "agentId": "ab1cdc73b714a8d92",
  "type": "user",
  "uuid": "d9579d6e-5526-4999-bbd4-af52b70716a9",
  "sourceToolAssistantUUID": "1093bcde-9336-4391-b3cc-bd60e1b05e46",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "fa54a58a-15c0-4802-9034-a220e6d2d3d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "wild-sauteeing-hare"
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-25T20:50:32.125Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Xk3ZrmiWTEWDGyoCWZfm4n`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d9579d6e-5526-4999-bbd4-af52b70716a9",
  "isSidechain": true,
  "agentId": "ab1cdc73b714a8d92",
  "requestId": "req_011CbPwtovZBajh2CFnodsQD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "017bb23e-94ae-48c3-a3c4-26f2df288c29",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "fa54a58a-15c0-4802-9034-a220e6d2d3d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "wild-sauteeing-hare",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01M8DebJJC1Nrcz2yPYpDajU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 20183,
      "cache_read_input_tokens": 33755,
      "output_tokens": 181,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 20183
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 181,
          "cache_read_input_tokens": 33755,
          "cache_creation_input_tokens": 20183,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 20183,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-25T20:50:32.472Z_

<details><summary>↩ Tool result · `toolu_01Xk3ZrmiWTEWDGyoCWZfm4n`</summary>

```text
1	% Appendix B — Extended Discussion
2	% Contains discussion paragraphs moved from the main text during compression.
3	
4	\section{Extended Discussion}\label{app:discussion}
5	
6	%%% CF Dual Mechanism %%%
7	% exp_ids: phase2_scierc_full_s1, llama_scierc_full_s1, llama_docred_full_s1
8	
9	\paragraph{CF Dual Mechanism.}
10	CF violations arise from two distinct mechanisms:
11	(1)~\emph{Registry override}: the semantic constraint forces a domain-compatible type that conflicts with the entity's previously registered type.
12	The entity appears in multiple relations with different type requirements, and the per-relation mask selects the locally valid type without consulting prior assignments.
13	(2)~\emph{Grammar-first fallback} (\S\ref{sec:interaction}): when the semantic mask conflicts with all grammar-valid tokens, the semantic layer is dropped entirely, allowing the grammar layer to generate any structurally valid type, which may differ from the entity's registered type.
14	
15	These mechanisms have sharply different model profiles.
16	Qwen3-8B triggers zero grammar-first fallbacks across all experiments, attributing 100\% of its CF violations to registry override.
17	Llama-3.1-8B, by contrast, triggers 5{,}882 fallbacks on SciERC (10.7 per document) and 57{,}825 on DocRED (63.8 per document), making grammar-first fallback the dominant CF source.
18	This asymmetry is consistent with the cross-model CF gap: Qwen achieves CF\,=\,2.57\% on DocRED vs.\ Llama's 12.02\%, despite both using identical constraint configurations.
19	The difference traces to Llama's less calibrated type predictions, which more frequently conflict with the semantic mask's valid set, triggering fallback.
20	
21	%%% Fallback Behavior and Effective Coverage %%%
22	% exp_ids: cf_fallback_ablation_scierc (final data)
23	
24	\paragraph{Fallback Behavior and Effective Coverage.}
25	\label{app:fallback-coverage}
26	The two-layer architecture produces two distinct fallback mechanisms with different semantic consequences.
27	\emph{Grammar-first fallback} occurs when $S(t) \cap G(t) = \emptyset$: the semantic layer deactivates as a safety valve, preserving structural validity at the cost of potential type violations.
28	The token-level fallback rate (36.6\% on SciERC Llama) is inflated by continuation tokens of multi-token type names (e.g., \textsc{OtherScientificTerm}, averaging 2.87 BPE tokens); at semantically meaningful first-token positions, the rate is 0.04--5.7\% (zero-shot) and drops to $\leq$\,0.11\% under fine-tuning.
29	These events account for the residual DR that persists after constraint enforcement.
30	\emph{Registry-consistent fallback} (4.5\%) occurs when the entity's registered type conflicts with domain/range constraints; the system defaults to the registered type for cross-triple consistency.
31	Together, these mechanisms produce the characteristic profile of composable constraint systems: residual DR traces to grammar-first fallback events, while CF violations arise from registry override events where per-relation enforcement assigns conflicting types.
32	
33	We define \emph{effective semantic constraint coverage} as $1 - f_{\text{gf}}$, where $f_{\text{gf}}$ is the grammar-first fallback rate.
34	On SciERC, Llama-3.1-8B shows $f_{\text{gf}} = 36.6\%$ (6{,}237 of 17{,}024 mask calls), yielding 63.4\% effective coverage.
35	On DocRED, by contrast, Qwen3-8B shows $f_{\text{gf}} = 0.08\%$ (46 of 54{,}859), yielding 99.9\% coverage.
36	The large discrepancy is primarily a tokenization artifact: SciERC entity types are multi-token (e.g., \textsc{OtherScientificTerm}, averaging 2.87 mask calls per type field), and continuation tokens necessarily conflict with the semantic mask, inflating the per-mask-call fallback rate.
37	DocRED types (\textsc{PER}, \textsc{ORG}, \textsc{LOC}, \textsc{TIME}, \textsc{NUM}, \textsc{MISC}) are all single-token, eliminating this inflation.
38	This metric directly quantifies the layer interaction (\S\ref{sec:interaction}): it measures the fraction of decoding steps where both constraint layers are jointly active, providing a fine-grained view beyond aggregate violation rates.
39	Qwen3-8B, with zero grammar-first fallbacks, achieves 100\% effective coverage on SciERC, consistent with its lower residual DR (0.93\% vs.\ Llama's 0.08\%).
40	
41	%%% Fallback Causal Tracing %%%
42	% exp_ids: Task C causal tracing (Qwen/Llama × ZS/FT × S1)
43	
44	\paragraph{Fallback Causal Tracing.}
45	\label{app:causal-tracing}
46	
47	To establish that grammar-first fallback is the \emph{sole} mechanism producing residual DR violations, we instrument the constraint processor to log, for each violation, whether the semantic mask was active ($S(t) \cap G(t) \neq \emptyset$) or bypassed via fallback ($S(t) \cap G(t) = \emptyset$) at the type-bearing position.
48	Table~\ref{tab:causal-tracing} reports the results across four SciERC configurations.
49	
50	\begin{table}[t]
51	\centering
52	\small
53	\setlength{\tabcolsep}{4pt}
54	\resizebox{\columnwidth}{!}{%
55	\begin{tabular}{@{}ll rrr@{}}
56	\toprule
57	\textbf{Model} & \textbf{Setting} & \textbf{Fallback Rate} & \textbf{DR} & \textbf{From FB} \\
58	\midrule
59	Qwen3-8B  & FT S1 & 0/2256 (0\%)    & 0  & N/A \\
60	Qwen3-8B  & ZS S1 & 16/3458 (0.46\%) & 16 & 100\% \\
61	Llama-3.1-8B & FT S1 & 1/2162 (0.05\%) & 1  & 100\% \\
62	Llama-3.1-8B & ZS S1 & 1/2630 (0.04\%) & 1  & 100\% \\
63	\bottomrule
64	\end{tabular}}
65	\caption{Fallback causal tracing on SciERC (551 documents). Fallback Rate: type-bearing positions where $S(t) \cap G(t) = \emptyset$ triggers grammar-first fallback. DR: residual domain/range violations. From FB: fraction of DR violations occurring at fallback positions. All violations occur exclusively at tail\_type positions (range constraints are tighter than domain constraints).}
66	\label{tab:causal-tracing}
67	\end{table}
68	
69	When the semantic mask is active, $\text{DR}_{\text{independent}} = 0$: the type constraint processor structurally prevents domain/range violations.
70	All 18 residual DR violations across four configurations occur exclusively at fallback positions, confirming that grammar-first fallback is a necessary condition for residual DR.
71	Fine-tuning reduces fallback to near-zero ($\leq$0.05\%), effectively eliminating the sole source of residual violations.
72	All fallback events occur at tail\_type positions, where $|\operatorname{range}(r, \tau^h)|$ is smaller than $|\operatorname{dom}(r)|$, making the intersection $S(t) \cap G(t)$ more likely to be empty.
73	
74	%%% Enabling Dependency: Confound Analysis %%%
75	
76	\paragraph{Enabling Dependency: Confound Analysis.}
77	\label{app:enabling-confound}
78	
79	The scale-dependent layer interaction (\S\ref{sec:method}) shows that the semantic layer achieves only 24\% DR reduction without the grammar layer (Table~\ref{tab:scierc-ablation}).
80	A potential confound is that the semantic layer depends not only on grammar-enforced vocabulary membership but also on structural enforcement for positional awareness: the semantic layer identifies type-bearing positions by pattern-matching the decoded prefix against the JSON schema, which is reliable only when the grammar layer guarantees valid JSON structure.
81	Without grammar enforcement, malformed structure can cause the semantic layer to misidentify type-bearing positions, reducing effective coverage.
82	We quantify this via the semantic-only ablation (Table~\ref{tab:scierc-ablation}, row~3): CF rises from 0.08\% to 2.71\%, indicating that 2.63\,pp of additional violations trace to structural ambiguity.
83	However, the dominant enabling mechanism remains vocabulary membership: the semantic layer's domain/range lookup requires $r_j \in \mathcal{R}$, which only the grammar layer ensures; without it, OOV relation names produce null constraint lookups.
84	The confound reinforces rather than undermines this interaction: both vocabulary and structural contributions of the grammar layer are prerequisites for effective semantic enforcement.
85	
86	%%% CF-DR Trade-off Analysis %%%
87	% exp_ids: cf_fallback_ablation_scierc (CF fallback vs full_s1 baseline)
88	
89	\paragraph{CF-DR Trade-off Analysis.}
90	\label{app:cf-dr-tradeoff}
91	
92	CF violations are the most prominent residual limitation of OntoCoDec under zero-shot decoding (9.90\% on SciERC, up to 12.02\% on Llama DocRED).
93	We treat this honestly: per-relation independent enforcement cannot eliminate CF without trading it against DR.
94	Table~\ref{tab:cf-dr-tradeoff} reports a pilot ablation in which we replace the grammar-first fallback with a CF-priority fallback that forces the entity's registered type when it conflicts with $\sigma(r)$.
95	
96	\begin{table}[t]
97	\centering
98	\small
99	\begin{tabular}{@{}l rrrr@{}}
100	\toprule
101	\textbf{Configuration} & \textbf{DR\,(\%)} & \textbf{CF\,(\%)} & \textbf{DR+CF} & \textbf{$f_{\text{gf}}$\,(\%)} \\
102	\midrule
103	S1 (baseline) & 0.93 & 9.90 & 10.83 & --- \\
104	CF fallback        & 14.78 & 0.04 & 14.82 & 36.64 \\
105	\midrule
106	$\Delta$ & $+$13.85 & $-$9.86 & $+$3.99 & --- \\
107	\bottomrule
108	\end{tabular}
109	\caption{CF-DR trade-off pilot on SciERC (Qwen3-8B, 551 documents; \texttt{w1\_cf\_fallback\_scierc\_pilot}). CF fallback eliminates CF but re-routes violations to DR, increasing total violations (DR+CF) by 3.99\,pp. $f_{\text{gf}}$: token-level grammar-first fallback rate at type-bearing positions (includes continuation tokens of multi-token type names; first-token position fallback rate is 0.46\% for SciERC Qwen; \S\ref{sec:greedy-limitation}).}
110	\label{tab:cf-dr-tradeoff}
111	\end{table}
112	
113	The CF fallback variant nearly eliminates CF (9.90\%\,$\to$\,0.04\%, $-$9.86\,pp) but at the cost of a 15.9$\times$ increase in DR (0.93\%\,$\to$\,14.78\%, $+$13.85\,pp).
114	% exp_id: w1_cf_fallback_scierc_pilot: DR=0.1478, CF=0.0004, f_gf=0.3664
115	This is not a net improvement: total violations (DR+CF) rise from 10.83\% to 14.82\% ($+$3.99\,pp), so the change \emph{re-routes} violations rather than reducing them.
116	The mechanism is mechanical: each token position with conflicting masks must commit to one violation type; when the CF fallback forces the system to emit the entity's registered type even though it lies outside $\sigma(r)$, the resulting triple satisfies cross-entity consistency but violates domain/range.
117	The token-level grammar-first fallback is triggered at 36.64\% of type-bearing positions (0.46\% at first-token positions; \S\ref{sec:greedy-limitation}); this conflict is structural, not a tunable hyperparameter.
118	
119	We interpret this as a fundamental tension in composable constraint systems with \emph{per-relation independent} enforcement: enforcement priority can be allocated between DR and CF but cannot independently minimize both.
120	Within this design, the current S1 configuration sits near the Pareto frontier of the trade-off, achieving 0.93\% DR at the cost of 9.90\% CF.
121	The direction of the trade-off is consistent beyond SciERC/Qwen3-8B: across all six zero-shot configurations (3 models $\times$ 2 datasets), DR and CF are descriptively inversely associated, with no setting showing both high DR and high CF simultaneously (Table~\ref{tab:cross-model}); however, $n{=}6$ is insufficient for statistical inference on this correlation.
122	The pattern is a structural consequence of per-relation enforcement with grammar-first fallback, not a model- or dataset-specific artifact; we select SciERC/Qwen3-8B for detailed ablation because it exhibits the highest CF (9.90\%), making the trade-off most visible.
123	While the inverse association holds across all configurations, the absolute trade-off magnitude may differ in settings with higher baseline CF, such as Llama DocRED (CF = 12.02\%), where the larger CF headroom could yield proportionally larger shifts under alternative fallback priorities.
124	The CF residual is concentrated in schema ambiguity rather than enforcement failure: 63.3\% of CF violations on SciERC involve the catch-all \textsc{Generic} type (Table~\ref{tab:cf-distribution}), which competes with every content type depending on anaphoric vs.\ referential use, a distinction the per-slot decoder cannot resolve without document-level coreference.
125	
126	Two complementary paths can lower CF without re-routing it to DR.
127	(i)~\emph{Reduce the baseline conflict rate.} Composing OntoCoDec with LoRA fine-tuning on SciERC reduces CF by 88\% relative to the zero-shot setting (9.90\%\,$\to$\,1.18\%; Table~\ref{tab:composability}), because the fine-tuned model's per-slot type predictions agree more often with the entity registry, so the per-relation mask and the registry intersect more frequently.
128	% exp_id: w5_lora_scierc_constrained_eval: CF=0.0118
129	The remaining 1.18\% still traces to \textsc{Generic}$\leftrightarrow$X schema ambiguity, so this path is empirically validated on one dataset and one fine-tuning method but does not generalize without further evidence.
130	(ii)~\emph{Replace per-relation enforcement with global entity-level type consensus during decoding.} This is outside the scope of OntoCoDec's forward-only autoregressive design and is left to future work.
131	
132	%%% Dual-Factor Quantitative Analysis %%%
133	% exp_ids: phase2_scierc_full_s1, phase2_docred_full_s1,
134	%          llama_scierc_full_s1, llama_docred_full_s1
135	
136	\paragraph{Dual-Factor Quantitative Analysis.}
137	\label{app:dual-factor}
138	
139	Figure~\ref{fig:dual-factor-scatter} plots residual DR against the product $\bar{\kappa} \times \text{RV}_{\text{baseline}}$ for model$\times$dataset configurations.
140	For \emph{calibrated} models (Qwen3-8B, Llama-3.1-8B; unconstrained ET${<}$3\% on both datasets), a linear fit yields $y = 0.366x - 0.138$ with $R^2 = 0.886$ ($n{=}4$, $F(1,2) = 15.54$, $p \approx 0.058$); with only four data points (df $= 2$) and $p > 0.05$, this constitutes a descriptive characterization rather than a confirmatory statistical test.
141	The strong fit supports the dual-factor pattern from \S\ref{sec:composition}: residual DR is governed by the product of schema tightness and baseline violation rate.
142	Mistral-7B (unconstrained ET${=}$7.58\% on DocRED) deviates from this pattern: its residual DR on DocRED (33.21\%) substantially exceeds the linear prediction. When model calibration is insufficient (ET${>}$5\% on either dataset), residual DR is dominated by entity misclassification rather than constraint-search failure.
143	This motivates a principled exclusion criterion: models with unconstrained ET${>}$5\% on either dataset fall outside the regime where the tightness$\times$RV product is the primary DR driver.
144	The two DocRED points (high $\bar{\kappa}{=}0.842$) separate cleanly from the two SciERC points (low $\bar{\kappa}{=}0.333$), and within each dataset the model with higher baseline RV shows higher residual DR.
145	
146	% Dual-factor scatter moved to main text (Figure~\ref{fig:dual-factor-scatter}).
147	
148	%%% Dataset-Dependent F1 Impact (moved from §7) %%%
149	% exp_ids: d012_bootstrap_ci (DocRED +0.49pp p<0.001, SciERC +0.13pp p=0.58),
150	%          phase0_docred_unconstrained (RV=29.66%), phase0_scierc_unconstrained (RV=1.39%)
151	
152	\paragraph{Dataset-Dependent F1 Impact.}
153	The divergence in F1 significance between DocRED ($+$0.49\,pp, $p < 0.001$) and SciERC ($+$0.13\,pp, $p = 0.58$) traces to a single mechanism: grammar-layer elimination of out-of-vocabulary relation names.
154	DocRED's baseline RV of 29.66\% produces 5{,}189 OOV predictions counted as false positives; eliminating them yields a significant precision gain.
155	SciERC's baseline RV is only 1.39\% (24 OOV predictions), too few to produce a detectable F1 effect.
156	Llama-3.1-8B's lower baseline RV (16.03\%) yields a smaller but directionally consistent improvement ($+$0.29\,pp vs.\ $+$0.49\,pp); F1 gain magnitude is proportional to baseline OOV rate.
157	% exp_ids: phase0_docred_unconstrained, phase0_scierc_unconstrained
158	% exp_ids: llama_docred_unconstrained (RV=16.03%), llama_docred_full_s1 (R-F1 delta=+0.29pp)
159	
160	%%% Bootstrap CIs and Effect Sizes %%%
161	% exp_ids: bootstrap_ci_ft_composability, r12_table2_bootstrap_ci
162	
163	\paragraph{Bootstrap Confidence Intervals and Effect Sizes.}
164	\label{app:bootstrap-effect-sizes}
165	
166	Table~\ref{tab:bootstrap-effect-sizes} reports per-configuration bootstrap CIs and Cohen's $d$ effect sizes (10{,}000 iterations, document-level resampling, seed=42) for the fine-tuning composability results (Table~\ref{tab:composability}).
167	After Bonferroni correction for $k{=}4$ comparisons ($\alpha_{\text{adj}}{=}0.0125$), no R-F1 difference reaches significance; all R-F1 effect sizes are negligible to small ($|d| \leq 0.37$; Cohen, 1988).
168	Per-configuration corrected $p$-values: Qwen3-8B/SciERC $p_B{=}1.00$, Qwen3-8B/DocRED $p_B{=}0.224$, Llama-3.1-8B/SciERC $p_B{=}1.00$, Llama-3.1-8B/DocRED $p_B{=}1.00$.
169	Constraint enforcement thus preserves extraction quality while achieving large, highly significant reductions in domain-range violations ($|d| \geq 3.0$, all $p_{\text{Bonf}} < 0.005$).
170	
171	\begin{table}[t]
172	\centering
173	\small
174	\setlength{\tabcolsep}{3pt}
175	\resizebox{\columnwidth}{!}{%
176	\begin{tabular}{@{}ll rrrr@{}}
177	\toprule
178	\textbf{Model} & \textbf{Dataset} & $\Delta$\textbf{(pp)} & \textbf{95\% CI} & $p$ & $d$ \\
179	\midrule
180	\multicolumn{6}{@{}l}{\textbf{R-F1 difference (S1 $-$ unconstrained):}} \\
181	Qwen3-8B & SciERC & $-$0.10 & [$-$0.30, 0.00] & .726 & $-$0.05 \\
182	Qwen3-8B & DocRED & $-$0.31 & [$-$0.69, $+$0.01] & .056 & $-$0.37 \\
183	Llama-3.1-8B & SciERC & $+$0.02 & [0.00, $+$0.07] & .736 & $+$0.01 \\
184	Llama-3.1-8B & DocRED & $+$0.06 & [$-$0.11, $+$0.25] & .535 & $+$0.07 \\
185	\midrule
186	\multicolumn{6}{@{}l}{\textbf{DR\% reduction:}} \\
187	Qwen3-8B & SciERC & $-$1.95 & [$-$2.87, $-$1.11] & $<$.001 & $-$6.15 \\
188	Qwen3-8B & DocRED & $-$0.75 & [$-$1.07, $-$0.48] & $<$.001 & $-$7.00 \\
189	Llama-3.1-8B & SciERC & $-$1.02 & [$-$1.98, $-$0.29] & $<$.001 & $-$3.17 \\
190	Llama-3.1-8B & DocRED & $-$0.29 & [$-$0.53, $-$0.10] & $<$.001 & $-$3.02 \\
191	\bottomrule
192	\end{tabular}}
193	\caption{Bootstrap CIs and Cohen's $d$ for Table~\ref{tab:composability} (10{,}000 iterations, document-level resampling, seed=42).
194	$d$: Cohen's $d$ from pooled bootstrap SD.
195	Top: R-F1 (S1 $-$ unconstrained); no comparison significant after Bonferroni correction ($k{=}4$, $\alpha_{\text{adj}}{=}0.0125$); $|d| \leq 0.37$ (negligible--small).
196	Bottom: DR\% reduction; all $p_{\text{Bonf}} < 0.005$, $|d| \geq 3.0$ (large).}
197	\label{tab:bootstrap-effect-sizes}
198	\end{table}
199	
200	%%% Paragraph 1: Low F1 Practical Significance %%%
201	% exp_ids: phase2_scierc_full_s1 (R-F1=8.36%), phase2_docred_full_s1 (R-F1=8.23%),
202	%          phase0_scierc_unconstrained (DR=15.37%), phase2_docred_unconstrained (DR=18.46%)
203	
204	\paragraph{Practical Significance of Zero-Shot F1.}
205	Our reported relation F1 of approximately 8\% on both SciERC and DocRED reflects the inherent difficulty of zero-shot closed IE, where the model receives no task-specific training examples.
206	For reference, supervised state-of-the-art systems on SciERC achieve approximately 49--53\% relation F1 with full training data~\citep{zhong2021frustratingly,ye2022packed}.
207	Constraint enforcement operates largely independently of the extraction model's intrinsic capability: it restricts the output space to ontologically valid triples regardless of the underlying model's accuracy.
208	Even after LoRA fine-tuning, residual DR of 1--2\% persists on tight-constraint relations (Table~\ref{tab:composability}); constraints remain necessary at deployment-grade quality.
209	% exp_ids: w5_lora_scierc_unconstrained_eval, w5_llama_lora_scierc_unconstrained_eval
210	In our evaluation, F1 serves as a \emph{control variable} verifying that constraint enforcement does not degrade extraction quality, not as an optimization target.
211	The contribution of this work is the constraint enforcement method itself; the zero-shot setting stress-tests constraint robustness under maximum model uncertainty, while composability with fine-tuning (\S\ref{sec:composability}) validates practical deployment value.
212	
213	%%% Paragraph 4: Decoding-Time vs. Post-Hoc Enforcement %%%
214	% exp_ids: posthoc_filtering_baseline, phase2_scierc_full_s1 (R-F1=8.36%),
215	%          phase2_docred_full_s1 (R-F1=8.23%, ET=0%)
216	
217	\paragraph{Decoding-Time vs.\ Post-Hoc Enforcement.}
218	Post-hoc filtering (generating triples without constraints, then removing schema-violating predictions) yields higher precision and consequently higher F1 than OntoCoDec on both datasets (SciERC 8.63 vs.\ 8.36; DocRED 9.61 vs.\ 8.23).
219	% posthoc: SciERC F1=8.63, DocRED F1=9.61; OntoCoDec: SciERC R-F1=8.36, DocRED R-F1=8.23
220	However, this precision gain comes at substantial cost.
221	On DocRED, post-hoc filtering discards 48.1\% of all predicted triples, including 127 true positives (11.2\% of correct predictions); recall drops from 9.46\% to 8.40\%.
222	% posthoc_docred: rejection=48.1%, tp_lost=127/1137, R: 9.46→8.40
223	Entity type violations remain unresolved (ET\,=\,2.47\% vs.\ OntoCoDec's 0\%), as filtering targets only domain/range and vocabulary violations.
224	% posthoc_docred: ET_residual=2.47%; phase2_docred_full_s1: ET=0%
225	OntoCoDec's decoding-time approach avoids this information loss by guiding generation toward compliant outputs rather than discarding non-compliant ones, preserving both recall and entity type validity.
226	The two strategies are complementary: post-hoc filtering can serve as an additional safety net for residual violations that decoding-time enforcement does not fully resolve.
227	
228	%%% CF Violation Distribution %%%
229	% exp_ids: phase2_scierc_full_s1 (CF=245), llama_scierc_full_s1 (CF=162),
230	%          phase2_docred_full_s1 (CF=2670), llama_docred_full_s1 (CF=3824)
231	
232	\paragraph{Cross-Field Violation Distribution.}
233	\label{app:cf-distribution}
234	
235	Table~\ref{tab:cf-distribution} reports the complete distribution of conflicting-type pairs for SciERC zero-shot S1 (248 CF violations across 245 unique entity-document pairs; no mention triggered $\geq$3 types).
236	Conflicts involving the \textsc{Generic} type account for 63.3\% (155/245) of all violations.
237	\textsc{Generic} is SciERC's anaphoric/placeholder label (``this approach'', ``the method''), which competes with every content type depending on whether the mention is used anaphorically or referentially, a distinction the per-slot constrained decoder cannot resolve without document-level coreference.
238	
239	The pattern generalizes across models and datasets: on Llama-3.1-8B SciERC, \textsc{Generic}$\leftrightarrow$\textsc{OtherScientificTerm} remains the top pair (53/162, 32.7\%); on DocRED, the analogous catch-all type \textsc{MISC} drives 76.6\% of Qwen's CF violations.
240	Under unconstrained decoding, CF rates collapse to $\leq$1\% on both datasets; CF violations are a side-effect of per-slot type commitment rather than a model deficiency.
241	
242	\begin{table}[t]
243	\centering
244	\small
245	\begin{tabular}{@{}lr r@{}}
246	\toprule
247	\textbf{Conflicting Type Pair} & \textbf{Count} & \textbf{\%} \\
248	\midrule
249	Generic $\leftrightarrow$ OtherScientificTerm & 85 & 34.7 \\
250	Generic $\leftrightarrow$ Material & 35 & 14.3 \\
251	Generic $\leftrightarrow$ Metric & 30 & 12.2 \\
252	Method $\leftrightarrow$ Task & 20 & 8.2 \\
253	Material $\leftrightarrow$ Method & 17 & 6.9 \\
254	OtherScientificTerm $\leftrightarrow$ Task & 12 & 4.9 \\
255	\midrule
256	10 further pairs (each $\leq$3.3\%) & 46 & 18.8 \\
257	\midrule
258	\textbf{Total} & \textbf{245} & 100.0 \\
259	\bottomrule
260	\end{tabular}
261	\caption{CF violation distribution on SciERC zero-shot S1 (Qwen3-8B, 551 documents).
262	All 245 unique entity-document pairs involve pairwise conflicts.
263	Conflicts involving \textsc{Generic} account for 63.3\%.}
264	\label{tab:cf-distribution}
265	\end{table}
266	
267	%%% Cascade Error Analysis %%%
268	% exp_ids: phase2_scierc_full_s1 (ZS: CF=248), w5_lora_scierc_full_s1_eval (FT: CF=22)
269	
270	\paragraph{Cascade Error Analysis.}
271	\label{app:cascade-analysis}
272	
273	Table~\ref{tab:cascade-breakdown} decomposes zero-shot CF violations by source mechanism.
274	The dominant source is hallucinated entities (58.1\%): the model generates entity names absent from the input document, and the entity registry assigns a type based on the first occurrence that may conflict with a subsequent valid entity sharing the same surface form.
275	True cascade errors---where first-seen type registration for a \emph{real} entity locks an incorrect type that blocks a subsequent valid assignment---account for only 7.3\% (18/248).
276	Correct type locks (first-seen type is correct and prevents an incorrect subsequent assignment) are 2.5$\times$ more frequent (18.1\%, 45/248), indicating that the first-seen registration mechanism provides a net benefit for type consistency.
277	
278	Under fine-tuning (22 CF violations, 20 documents), cascade errors are completely eliminated (0/22): LoRA training calibrates entity typing sufficiently that first-seen registrations are consistently correct.
279	This confirms that cascade errors are a model calibration issue exposed by the constraint mechanism, not an inherent deficiency of first-seen registration.
280	
281	\begin{table}[h]
282	\centering
283	\small
284	\begin{tabular}{@{}l rr@{}}
285	\toprule
286	\textbf{CF Source Category} & \textbf{Count} & \textbf{\%} \\
287	\midrule
288	Hallucinated entity & 144 & 58.1 \\
289	Correct type lock & 45 & 18.1 \\
290	True cascade error & 18 & 7.3 \\
291	Other / ambiguous & 41 & 16.5 \\
292	\midrule
293	\textbf{Total} & \textbf{248} & 100.0 \\
294	\bottomrule
295	\end{tabular}
296	\caption{CF violation source breakdown on SciERC zero-shot S1 (Qwen3-8B, 551 documents; exp\_id: phase2\_scierc\_full\_s1).
297	``Hallucinated entity'': generated entity absent from input.
298	``True cascade error'': first-seen lock on incorrect type blocks valid subsequent assignment.
299	``Correct type lock'': first-seen type correct, prevents incorrect subsequent type.
300	Under fine-tuning, cascade errors are completely eliminated (0/22 CF violations; exp\_id: w5\_lora\_scierc\_full\_s1\_eval).}
301	\label{tab:cascade-breakdown}
302	\end{table}
303	
304	%%% Per-Relation DR Elimination under Fine-Tuning %%%
305	% exp_ids: lora_scierc_unconstrained, lora_scierc_full_s1
306	
307	\paragraph{Per-Relation DR Elimination under Fine-Tuning.}
308	\label{app:lora-per-relation}
309	
310	Table~\ref{tab:lora-per-relation} presents the per-relation breakdown of DR elimination when OntoCoDec is composed with LoRA fine-tuning on SciERC.
311	Fine-tuning alone eliminates DR on four of seven relations but leaves non-zero violations on the three tightest-constraint relations: \textsc{Evaluate-for} ($\kappa{=}0.361$, 13.13\%), \textsc{Part-of} ($\kappa{=}0.417$, 5.77\%), and \textsc{Compare} ($\kappa{=}0.528$, 5.00\%).
312	Adding OntoCoDec constraints eliminates all remaining violations across all relations.
313	One \textsc{Evaluate-for} triple (99\,$\to$\,98) is redirected to \textsc{Used-for} (634\,$\to$\,635) by token-level masking: the head entity's registered type falls outside \textsc{Evaluate-for}'s domain, and the semantic mask steers generation to the nearest valid relation.
314	
315	\begin{table}[t]
316	\centering
317	\small
318	\begin{tabular}{@{}l r rr rr@{}}
319	\toprule
320	& & \multicolumn{2}{c}{\textbf{LoRA Unconstr.}} & \multicolumn{2}{c}{\textbf{LoRA + S1}} \\
321	\cmidrule(lr){3-4} \cmidrule(l){5-6}
322	\textbf{Relation} & $\kappa$ & DR\,(\%) & $n$ & DR\,(\%) & $n$ \\
323	\midrule
324	Evaluate-for & 0.361 & 13.13 & 99 & \textbf{0} & 98 \\
325	Part-of      & 0.417 & 5.77  & 52 & \textbf{0} & 52 \\
326	Compare      & 0.528 & 5.00  & 40 & \textbf{0} & 40 \\
327	Conjunction  & 0.306 & 1.31  & 153 & \textbf{0} & 153 \\
328	Feature-of   & 0.278 & 1.35  & 74 & \textbf{0} & 74 \\
329	Used-for     & 0.028 & 0.16  & 634 & \textbf{0} & 635 \\
330	Hyponym-of   & 0.417 & 0     & --- & \textbf{0} & --- \\
331	\bottomrule
332	\end{tabular}
333	\caption{Per-relation DR elimination on SciERC with LoRA fine-tuning (Qwen3-8B).
334	$\kappa$: constraint tightness; $n$: predicted triple count.
335	Used-for gains one triple from Evaluate-for redirection.}
336	\label{tab:lora-per-relation}
337	\end{table}
338	
339	%%% Fine-Tuned Four-Way Ablation %%%
340	% exp_ids: w5_lora_scierc_*, w5_llama_lora_scierc_*, w5_qwen_docred_*, w5_llama_docred_*, w8_*
341	
342	\paragraph{Fine-Tuned Four-Way Ablation.}
343	\label{app:ft-ablation}
344	
345	Table~\ref{tab:ft-ablation} presents the four-way constraint ablation on fine-tuned models across both datasets, isolating each layer's contribution when the base model has already internalized schema knowledge.
346	
347	\begin{table}[t]
348	\centering
349	\small
350	\setlength{\tabcolsep}{3pt}
351	\resizebox{\columnwidth}{!}{%
352	\begin{tabular}{@{}lll rrrrr rr@{}}
353	\toprule
354	\textbf{Dataset} & \textbf{Model} & \textbf{Mode} & \textbf{DR\,$\downarrow$} & \textbf{RV\,$\downarrow$} & \textbf{ET\,$\downarrow$} & \textbf{CF} & \textbf{PF} & \textbf{E-F1\,$\uparrow$} & \textbf{R-F1\,$\uparrow$} \\
355	\midrule
356	\multirow{8}{*}{SciERC}
357	  & \multirow{4}{*}{Qwen3-8B}
358	    & Unconstrained & 1.95 & 0.00 & 0.00 & 0.00 & 0.00 & 67.05 & 43.86 \\
359	  & & Grammar       & 1.90 & 0.00 & 0.00 & 0.00 & 0.00 & 67.05 & 43.86 \\
360	  & & Semantic      & 0.60 & 0.00 & 0.00 & 0.18 & 0.00 & 67.05 & 43.69 \\
361	  & & S1       & \textbf{0}    & 0.00 & 0.00 & 1.18 & 0.00 & 67.05 & 43.77 \\
362	  \cmidrule(l){2-10}
363	  & \multirow{4}{*}{Llama-3.1-8B}
364	    & Unconstrained & 1.11 & 0.00 & 0.00 & 0.00 & 0.00 & 67.76 & 45.45 \\
365	  & & Grammar       & 1.11 & 0.00 & 0.00 & 0.00 & 0.00 & 67.76 & 45.45 \\
366	  & & Semantic      & 0.65 & 0.00 & 0.00 & 0.10 & 0.00 & 67.76 & 45.47 \\
367	  & & S1       & \textbf{0.09} & 0.00 & 0.00 & 0.46 & 0.00 & 67.76 & 45.47 \\
368	\midrule
369	\multirow{8}{*}{DocRED}
370	  & \multirow{4}{*}{Qwen3-8B}
371	    & Unconstrained & 0.76 & 0.27 & 0.00 & 0.12 & 7.11 & 82.15 & 40.86 \\
372	  & & Grammar       & 0.61 & 0.00 & 0.00 & 0.11 & 7.01 & 82.19 & 40.85 \\
373	  & & Semantic      & 0.19 & 0.23 & 0.00 & 0.27 & 7.52 & 82.15 & 40.85 \\
374	  & & S1       & \textbf{0.01} & 0.00 & 0.00 & 0.41 & 8.52 & 81.43 & 40.56 \\
375	  \cmidrule(l){2-10}
376	  & \multirow{4}{*}{Llama-3.1-8B}
377	    & Unconstrained & 0.49 & 0.15 & 0.00 & 0.08 & 2.30 & 83.93 & 43.72 \\
378	  & & Grammar       & 0.51 & 0.00 & 0.00 & 0.12 & 2.30 & 84.04 & 43.72 \\
379	  & & Semantic      & 0.48 & 0.15 & 0.00 & 0.16 & 2.40 & 84.02 & 43.85 \\
380	  & & S1       & \textbf{0.21} & 0.00 & 0.00 & 0.21 & 2.51 & 83.94 & 43.78 \\
381	\bottomrule
382	\end{tabular}}%
383	\caption{Four-way constraint ablation on fine-tuned models (LoRA, 2 models $\times$ 2 datasets).
384	DR/RV/ET: violation rates (\%) over predicted relations; CF: over predicted entities; PF: parse failure rate (\%); F1 $\times$100.
385	Grammar layer is a no-op post-fine-tuning (DR change $<$0.2\,pp in all 4 settings; RV and ET already 0\% without constraints).
386	Semantic layer is the sole effective DR defense (41--69\% on SciERC, 2--75\% on DocRED); the near-zero Llama DocRED reduction reflects a near-floor baseline (DR${=}$0.49\%).
387	F1 cost is negligible: max $\Delta$R-F1 = $-$0.30\,pp (Qwen DocRED, full vs.\ unconstrained).}
388	\label{tab:ft-ablation}
389	\end{table}
390	
391	The grammar layer is effectively a no-op for fine-tuned models across all four settings: RV and ET are already 0\% without constraints, and grammar-only DR change is $<$0.2\,pp (4/4 settings).
392	The semantic layer is the sole effective DR defense under fine-tuning, independently reducing DR by 41--69\% on SciERC (Qwen $-$69\%, Llama $-$41\%) and 2--75\% on DocRED (Qwen $-$75\%, Llama $-$2\%); the near-zero Llama DocRED reduction reflects a near-floor baseline (DR${=}$0.49\%, 80 violations in 16{,}074 triples), where the semantic layer has minimal room to improve.
393	Adding both layers achieves near-complete elimination (DR\,$\leq$\,0.21\% in all 4 settings): even after fine-tuning, the semantic layer's pair-based enforcement captures violations that training alone cannot eliminate, specifically on tight-constraint relations where the valid type-pair space is small.
394	F1 cost is negligible: the maximum R-F1 decrease across S1 vs.\ unconstrained is $-$0.30\,pp (Qwen DocRED).
395	
396	%%% DocRED Zero-Shot Ablation (moved from main text) %%%
397	% exp_ids: phase2_docred_unconstrained, phase2_docred_grammar_only,
398	%          phase2_docred_semantic_only, phase2_docred_full_s1
399	
400	\paragraph{DocRED Zero-Shot Ablation.}
401	\label{app:docred-zs-ablation}
402	
403	Table~\ref{tab:docred-ablation} presents the four-way constraint ablation on DocRED under zero-shot decoding, parallel to the SciERC ablation in Table~\ref{tab:scierc-ablation}.
404	
405	\begin{table}[t]
406	\centering
407	\small
408	\setlength{\tabcolsep}{3.6pt}
409	\resizebox{\columnwidth}{!}{%
410	\begin{tabular}{@{}l rrrrrr rr@{}}
411	\toprule
412	& \multicolumn{6}{c}{\textbf{Violation Rates (\%)}}
413	& \multicolumn{2}{c}{\textbf{F1}} \\
414	\cmidrule(lr){2-7} \cmidrule(l){8-9}
415	\textbf{Mode}
416	  & DR\,$\downarrow$ & $\Delta$DR
417	  & RV\,$\downarrow$ & ET\,$\downarrow$ & CF & Tot.\,$\downarrow$
418	  & Rel.\,$\uparrow$ & Ent.\,$\uparrow$ \\
419	\midrule
420	Unconstrained
421	  & 18.46 & ---
422	  & 29.66 & 2.48
423	  & 0.10  & 18.56
424	  & 7.74  & 58.15 \\
425	Grammar
426	  & 26.17 & $\uparrow$42\%
427	  & \textbf{0.03} & \textbf{0}
428	  & 0.07  & 26.24
429	  & \textbf{8.31}  & \textbf{59.38} \\
430	Semantic
431	  & 13.84 & $\downarrow$25\%
432	  & 29.87 & 4.22
433	  & 1.05  & 14.89
434	  & 7.70  & 57.81 \\
435	S1
436	  & \textbf{10.21} & $\downarrow$\textbf{45\%}
437	  & \textbf{0.03} & \textbf{0}
438	  & 2.57  & \textbf{12.78}
439	  & 8.23  & 59.37 \\
440	\bottomrule
441	\end{tabular}}%
442	\caption{Four-way ablation on DocRED (998 documents, Qwen3-8B, zero-shot).
443	$\Delta$DR: relative change vs.\ unconstrained.
444	Tot.\ = DR + CF (total type-violation burden).
445	Best per column in \textbf{bold} (CF excluded; Tot.\ included).
446	F1 $\times$100. Bootstrap significance: R-F1 $+$0.49\,pp ($p < 0.001$).
447	Grammar-only $\uparrow$DR: vocabulary enforcement makes OOV outputs evaluable, exposing latent violations (see \S\ref{sec:docred-results}).}
448	\label{tab:docred-ablation}
449	\end{table}
450	
451	%%% Residual DR Error Analysis (Fine-Tuned) %%%
452	% exp_ids: w5_qwen_docred_*, w5_llama_docred_*, w5_lora_scierc_*, w5_llama_lora_scierc_*
453	
454	\paragraph{Residual DR Error Analysis.}
455	\label{app:residual-dr-analysis}
456	
457	Across all fine-tuned settings (2 models $\times$ 2 datasets $\times$ S1), only 36 domain/range violations remain.
458	Manual inspection reveals four root causes:
459	
460	\begin{enumerate}[nosep,leftmargin=*]
461	\item \emph{Entity type errors} (39\%): the LLM assigns an incorrect entity type (e.g., labeling a geographic entity as \textsc{LOC} when the gold standard requires \textsc{MISC}), causing the semantic mask to permit a domain/range-incompatible relation.
462	\item \emph{Schema coverage gaps} (33\%): the frequency-based constraint table, constructed from training-set co-occurrence statistics, does not cover long-tail type pairs that are ontologically valid but rare. These violations are irreducible by decoding-time constraints alone.
463	\item \emph{Incorrect relation selection} (17\%): the model selects a semantically inappropriate relation whose domain/range constraints are incompatible with the correctly typed entities.
464	\item \emph{Direction reversal} (11\%): the model assigns the correct relation but inverts head/tail roles, placing entities in positions that violate the relation's asymmetric domain/range specification.
465	\end{enumerate}
466	
467	Two dataset-specific patterns emerge.
468	Outside Llama DocRED, all residual violations (3 of 36, spanning Llama SciERC and Qwen DocRED) trace exclusively to schema coverage gaps: the model's entity typing is accurate, and the constraint system has reached its theoretical ceiling given the frequency-based constraint table.
469	On DocRED, Llama-3.1-8B contributes 33 of 36 residual violations (92\%), with entity type errors as the dominant cause (14/33, 42\%).
470	This asymmetry reflects Llama's weaker fine-tuned entity typing on DocRED's larger ontology (96 relations, 6 entity types) compared to Qwen, which achieves near-zero residual.
471	The implication is twofold: (i)~the irreducible floor from schema gaps is small ($\sim$3 violations across 4 settings), so the constraint system operates near its theoretical optimum; (ii)~residual violations from entity typing errors are addressable through stronger base models or improved entity typing modules, without modifying the constraint architecture.
472	
473	%%% Post-Hoc Filtering Comparison (Extended) %%%
474	% exp_ids: posthoc_*_zs, posthoc_*_ft
475	
476	\paragraph{Post-Hoc Filtering: Extended Comparison.}
477	\label{app:posthoc-extended}
478	
479	Table~\ref{tab:posthoc-extended} presents the full comparison across all six zero-shot and four fine-tuned configurations.
480	
481	\begin{table}[t]
482	\centering
483	\small
484	\setlength{\tabcolsep}{3pt}
485	\resizebox{\columnwidth}{!}{%
486	\begin{tabular}{@{}lll rrr l@{}}
487	\toprule
488	\textbf{Setting} & \textbf{Model} & \textbf{Dataset} & \textbf{Reject\%} & \textbf{R-F1$_{\text{ph}}$} & \textbf{R-F1$_{\text{cd}}$} & \textbf{Winner} \\
489	\midrule
490	\multirow{6}{*}{ZS}
491	  & Qwen    & SciERC & 16.8 & 8.63  & 8.36  & ph \\
492	  & Llama   & SciERC & 13.9 & 2.71  & 2.54  & ph \\
493	  & Mistral & SciERC & 20.3 & 3.94  & 3.67  & ph \\
494	  & Qwen    & DocRED & 48.1 & 9.61  & 8.23  & ph \\
495	  & Llama   & DocRED & 42.2 & 7.44  & 6.27  & ph \\
496	  & Mistral & DocRED & \textbf{73.7} & 3.85  & \textbf{5.52} & cd \\
497	\midrule
498	\multirow{4}{*}{FT}
499	  & Qwen    & SciERC & 1.95 & 43.94 & 43.77 & ph \\
500	  & Llama   & SciERC & 1.11 & 45.23 & 45.47 & cd \\
501	  & Qwen    & DocRED$^\ddagger$ & 1.03 & 41.11 & 40.79 & ph \\
502	  & Llama   & DocRED & 0.64 & 43.92 & 43.78 & cd \\
503	\bottomrule
504	\end{tabular}}%
505	\caption{Post-hoc filtering (ph) vs.\ constrained decoding (cd).
506	In zero-shot settings, post-hoc F1 is higher in 5/6 groups (precision-dominated), but constrained decoding preserves higher recall in all 6/6 groups.
507	At reject rate $>$70\% (Mistral DocRED), post-hoc F1 collapses below constrained.
508	Under fine-tuning, rejection rates drop to 0.6--2.0\% and the two strategies are equivalent ($\Delta \leq 0.55$\,pp; each wins two groups).
509	F1 $\times$100.
510	$^\ddagger$Uses 4096-context LoRA variant; R-F1 differs from Table~\ref{tab:composability}'s standard LoRA configuration.}
511	\label{tab:posthoc-extended}
512	\end{table}
513	
514	The crossover point occurs when post-hoc rejection exceeds $\sim$70\%: Mistral DocRED rejects 73.7\% of predicted triples, discarding enough true positives that constrained decoding's recall advantage dominates ($+$1.67\,pp).
515	OntoCoDec's advantage thus scales with violation severity: precisely when constraints are most needed, post-hoc filtering is most destructive.
516	Under fine-tuning, both strategies converge because few violations remain to filter or constrain ($\Delta \leq 0.55$\,pp across all four FT groups, with each strategy winning two).
517	
518	%%% Zero-Shot Runtime Profiling %%%
519	
520	\paragraph{Zero-Shot Runtime Profiling.}
521	\label{app:runtime}
522	
523	On SciERC (Qwen3-8B, zero-shot greedy, NVIDIA RTX PRO 6000 Blackwell Server Edition), unconstrained inference averages 4.163\,s/doc and S1 constrained decoding averages 4.710\,s/doc ($+$13.1\% overhead).
524	On DocRED (same configuration), relative overhead is lower due to amortization: the fixed per-token constraint cost is spread over longer generation sequences.
525	XGrammar automaton compilation takes 0.044\,s; the full constraint pipeline (schema parsing, JSON Schema generation, grammar compilation) takes 0.33\,s on SciERC (Table~\ref{tab:scalability}), amortized to zero over the evaluation set.
526	
527	% exp_id: p8c_ft_scierc_latency — Reviewer Report #23 verified
528	\paragraph{Fine-Tuned Latency Profiling.}
529	\label{app:ft-latency}
530	Under LoRA fine-tuning (same hardware and dataset), unconstrained inference averages 2.612\,s/doc and S1 constrained decoding averages 2.873\,s/doc ($+$10.0\% overhead, $n{=}551$).
531	Fine-tuned models generate shorter, more structured outputs than zero-shot models (2.612\,s vs.\ 4.163\,s/doc unconstrained); absolute generation time drops by 37\%.
532	The relative overhead ($+$10.0\%) is slightly lower than zero-shot ($+$13.1\%), consistent with shorter sequences requiring fewer constraint checks per document.
533	
534	%%% Fuzzy Relation Matching %%%
535	
536	\paragraph{Relation Matching Protocol.}
537	\label{app:fuzzy-matching}
538	Relation F1 evaluation uses fuzzy normalization to handle model-specific formatting variants (e.g., underscores vs.\ spaces, abbreviations).
539	A predicted relation $r_p$ matches gold relation $r_g$ if: (1)~exact string match after case-insensitive normalization, or (2)~token overlap $>$80\% \emph{and} edit distance $\leq 2$.
540	This protocol affects primarily Mistral, which produces underscore-separated variants (e.g., ``head\_of\_government'' for ``head of government'').
541	On Mistral DocRED, fuzzy matching contributes 98 additional TPs ($+$0.84\,pp R-F1; strict R-F1\,=\,3.50\% vs.\ fuzzy 4.34\%).
542	For Qwen and Llama under grammar constraints, the grammar layer enforces exact relation names, making fuzzy matching irrelevant (0 additional matches).
543	All F1 figures in the main text use fuzzy normalization consistently across all models and conditions.
544	
545	%%% Per-Relation Violation Landscape %%%
546	
547	\paragraph{Per-Relation Violation Landscape.}
548	\label{app:per-relation-landscape}
549	
550	Table~\ref{tab:prompt_comparison} compares violation rates under unconstrained and schema-informed prompting.
551	Figure~\ref{fig:per_relation_dr} shows the per-relation DR distribution on SciERC.
552	
553	\begin{table}[t]
554	\centering
555	\small
556	\caption{Violation rates (\%) under unconstrained and schema-informed prompting (Qwen3-8B, zero-shot).}
557	\label{tab:prompt_comparison}
558	\resizebox{\columnwidth}{!}{%
559	\begin{tabular}{ll cccc}
560	\toprule
561	Dataset & Prompt & DR$\downarrow$ & RV$\downarrow$ & ET$\downarrow$ & CF$\downarrow$ \\
562	\midrule
563	\multirow{2}{*}{SciERC} & Unconstrained & 15.4 & 1.4 & 0.4 & 0.1 \\
564	 & Schema-informed & 5.8 & 0.3 & \textbf{0.0} & --- \\
565	\midrule
566	\multirow{2}{*}{DocRED} & Unconstrained & 18.5 & 29.7 & 2.5 & 0.1 \\
567	 & Schema-informed & 12.8 & 18.4 & 0.2 & 0.2 \\
568	\bottomrule
569	\end{tabular}}
570	\end{table}
571	
572	%%% WikiEvents Extended %%%
573	
574	\paragraph{WikiEvents Dataset Details.}
575	\label{app:wikievents}
576	WikiEvents~\cite{li2021document} is a document-level event argument extraction benchmark grounded in the DARPA KAIROS ontology.
577	It defines 56 event types, 80 argument roles, and 27 entity types, with 245 (event\_type, role)$\to$allowed\_entity\_types constraints.
578	The grammar layer targets EV (event vocabulary), RoV (role vocabulary), and ET; the semantic layer enforces AC (argument constraint) via role-conditioned masking, analogous to RE domain/range enforcement.
579	
580	\paragraph{Constraint Tightness in WikiEvents.}
581	\label{app:wikievents-kappa}
582	% Data source: artifacts/w1c_wikievents_kappa_results.md
583	WikiEvents role-level tightness (with $|\mathcal{E}|{=}27$) has mean $\bar{\kappa}{=}0.82$ and median 0.89; 84\% of roles have $\kappa \geq 0.80$ (4 or fewer valid entity types out of 27).
584	The tightness-violation pattern extends to event extraction: roles with $\kappa \geq 0.90$ exhibit the highest AC rate (50\%), compared to 21\% for medium-tightness ($0.80 \leq \kappa < 0.90$) and 30\% for loose ($\kappa < 0.80$) roles; this is consistent with the RE observation that constraint tightness correlates with violation frequency.
585	However, the correlation is modulated by entity type prototypicality: semantically intuitive roles (e.g., Transportation.Vehicle$\to$VEH) show 0\% AC despite $\kappa{=}0.963$, while roles that require rare KAIROS-specific types (e.g., Crime$\to$CRM, Sentence$\to$SEN) show near-100\% AC because LLMs default to common types (PER, ORG).
586	The loose group's elevated rate (30\%) is driven by high-frequency roles such as Attack.Target (126 args, 34\% AC, $\kappa{=}0.59$), where systematic model errors outweigh the permissive constraint space.
587	
588	%%% Lucky Violation Analysis %%%
589	% exp_ids: task_e_lucky_violation_analysis
590	
591	\paragraph{Lucky Violation Analysis.}
592	\label{app:lucky-violations}
593	Table~\ref{tab:lucky-violations} quantifies the recall cost of DR elimination.
594	A ``lucky violation'' is a constraint-removed triple that happens to match a gold label---an ontologically invalid prediction that is nonetheless correct.
595	Across four fine-tuned configurations, lucky violations average 0.24\% of gold triples (range 0.01--0.51\%), confirming that nearly all removed DR violations are false positives.
596	On Llama SciERC, all five lucky violations are recovered as legal type paths under constrained decoding (zero churn): the model finds an ontology-compliant route to the same prediction.
597	
598	\begin{table}[h]
599	\centering
600	\small
601	\resizebox{\columnwidth}{!}{%
602	\begin{tabular}{@{}llrrrr@{}}
603	\toprule
604	\textbf{Model} & \textbf{Dataset} & \textbf{DR (\%)} & \textbf{Lucky} & \textbf{$\Delta$Recall} & \textbf{Churn} \\
605	& & \textbf{unc$\to$con} & \textbf{(\% gold)} & \textbf{(pp)} & \textbf{(\%)} \\
606	\midrule
607	Qwen3-8B  & SciERC & 1.95$\to$0    & 4 (0.41\%) & $-$0.10 & 0.22 \\
608	Llama-8B  & SciERC & 1.11$\to$0.09 & 5 (0.51\%) & $\pm$0.00 & 0 \\
609	Qwen3-8B  & DocRED & 1.03$\to$0.01 & 1 (0.01\%) & $-$0.84 & 2.05 \\
610	Llama-8B  & DocRED & 0.64$\to$0.21 & 1 (0.01\%) & $-$0.10 & 0.86 \\
611	\midrule
612	\multicolumn{2}{@{}l}{\textit{Average}} & & \textit{0.24\%} & $-$0.26 & 0.78 \\
613	\bottomrule
614	\end{tabular}}
615	\caption{Lucky violation analysis across four LoRA fine-tuned configurations.
616	Lucky: count (and \% of gold triples) of constraint-removed violations matching gold labels.
617	$\Delta$Recall: recall change from unconstrained to constrained.
618	Churn: fraction of gold-matching triples whose predictions change (including recovery via legal type paths).}
619	\label{tab:lucky-violations}
620	\end{table}
621	
622	%%% Trie-Only Baseline %%%
623	% exp_ids: trie_qwen_ft_scierc, trie_qwen_zs_scierc, trie_llama_ft_scierc, trie_llama_zs_scierc
624	
625	\paragraph{Trie-Only Baseline (GCD-Equivalent).}
626	\label{app:trie-baseline}
627	Table~\ref{tab:trie-baseline} isolates the effect of vocabulary membership constraints without JSON structural enforcement.
628	The trie constrains entity type and relation tokens to schema-valid values (achieving ET${=}$0\%, RV${=}$0\% across all configurations), functionally equivalent to GCD's~\cite{geng2023gcd} constrained decoding.
629	However, without grammar-level JSON enforcement, models systematically omit entity type fields (83\% of triples) or produce malformed JSON (0--51\% parse failure), causing DR to rise to 15--96\%---far worse than unconstrained baselines.
630	The effect is most dramatic for Llama-8B LoRA: 50.8\% parse failure causes R-F1 to collapse from 45.47 (OntoCoDec S1) to 19.95, demonstrating that the grammar layer is not merely helpful but a structural prerequisite---vocabulary constraints require JSON scaffolding to reach the positions where they apply.
631	
632	\begin{table}[h]
633	\centering
634	\small
635	\resizebox{\columnwidth}{!}{%
636	\begin{tabular}{@{}ll rrrr rr@{}}
637	\toprule
638	\textbf{Model} & \textbf{Setting}
639	  & \textbf{ET\,$\downarrow$} & \textbf{RV\,$\downarrow$} & \textbf{DR\,$\downarrow$} & \textbf{CF}
640	  & \textbf{R-F1\,$\uparrow$} & \textbf{PF\,(\%)} \\
641	\midrule
642	\multirow{2}{*}{Qwen3-8B}
643	  & LoRA  & 0 & 0 & 95.5  & 0.09 & 41.16 & 9.1 \\
644	  & ZS    & 0 & 0 & 29.3  & 0    & 8.64  & 0 \\
645	\multirow{2}{*}{Llama-8B}
646	  & LoRA  & 0 & 0 & 15.2$^\dagger$  & 0    & 19.95 & 50.8 \\
647	  & ZS    & 0 & 0 & 84.4  & 0.36 & 2.90  & 0 \\
648	\midrule
649	\multicolumn{8}{@{}l}{\textit{Comparison with OntoCoDec S1:}} \\
650	\midrule
651	& & \multicolumn{2}{c}{\textbf{S1 DR\,(\%)}} & \textbf{Trie DR\,(\%)} & \multicolumn{2}{c}{\textbf{DR Gap (pp)}} & \\
652	\cmidrule(lr){3-4} \cmidrule(lr){5-5} \cmidrule(lr){6-7}
653	Qwen3-8B  & LoRA  & \multicolumn{2}{c}{0}    & 95.5  & \multicolumn{2}{c}{95.5}  & \\
654	Qwen3-8B  & ZS    & \multicolumn{2}{c}{0.93} & 29.3  & \multicolumn{2}{c}{28.4}  & \\
655	Llama-8B  & LoRA  & \multicolumn{2}{c}{0.09} & 15.2  & \multicolumn{2}{c}{15.1}  & \\
656	Llama-8B  & ZS    & \multicolumn{2}{c}{0.08} & 84.4  & \multicolumn{2}{c}{84.3}  & \\
657	\bottomrule
658	\end{tabular}}
659	\caption{Trie-only baseline (GCD-equivalent, vocabulary membership without JSON grammar) on SciERC.
660	Top: full trie-only metrics (ET/RV/DR/CF: violation rates \%; R-F1 $\times$100; PF: parse failure rate).
661	Trie achieves ET${=}$0\%, RV${=}$0\% but DR rises to 15--96\% because models omit type fields without structural enforcement.
662	Bottom: DR gap between OntoCoDec S1 and trie-only, quantifying the grammar layer's contribution.
663	$^\dagger$50.8\% parse failure rate.}
664	\label{tab:trie-baseline}
665	\end{table}
666	
667	%%% GCD/BoostCD Equivalence Comparison %%%
668	
669	\paragraph{Comparison with Grammar-Based Constrained Decoding.}
670	\label{app:gcd-comparison}
671	
672	The trie-only results above isolate vocabulary constraints in the absence of structural enforcement.
673	Table~\ref{tab:gcd-comparison} places this finding in the broader context of grammar-based constrained decoding methods, comparing the constraint class, enforcement level, and DR reduction achieved by each approach---including OntoCoDec's grammar layer, which is analytically equivalent to GCD-family methods.
674	
675	\begin{table*}[t]
676	\centering
677	\small
678	\begin{tabular}{@{}l l l l l l@{}}
679	\toprule
680	\textbf{Method} & \textbf{Constraint Type} & \textbf{Level} & \textbf{DR Red.} & \textbf{CF} & \textbf{State} \\
681	\midrule
682	GCD~\cite{geng2023gcd} & CFG (JSON schema) & Grammar & ${\sim}$3\% & N/A & Stateless \\
683	BoostCD~\cite{boostcd2025} & CFG + beam rerank & Grammar & ${\sim}$3\%$^\dagger$ & N/A & Stateless \\
684	Trie-Only (Tab.~\ref{tab:trie-baseline}) & Prefix trie & Vocab & 0\%$^\ddagger$ & N/A & Stateless \\
685	\midrule
686	vLLM \texttt{guided\_json}~\cite{kwon2023vllm} & JSON Schema & Grammar & ${\sim}$3\%$^\S$ & N/A & Stateless \\
687	\midrule
688	OntoCoDec Grammar & CFG (XGrammar) & Grammar & ${\sim}$3\% & N/A & Stateless \\
689	OntoCoDec S1 & CFG + type constr. & Gram.+Sem. & 94--100\% (FT) & ${\leq}$1.4\% (FT) & Entity reg. \\
690	\bottomrule
691	\end{tabular}
692	\caption{Comparison with grammar-based constrained decoding methods.
693	$^\dagger$Equivalent mechanism; BoostCD adds beam-level reranking but the CFG enforcement is identical.
694	$^\ddagger$Vocabulary-only constraints without JSON structure cause DR to \emph{increase} (15--96\%; Table~\ref{tab:trie-baseline}).
695	$^\S$Experimentally verified: DR${=}$15.26\% vs.\ grammar-only 14.84\% ($\Delta{<}$0.5\,pp; Table~\ref{tab:vllm-verification}).
696	Grammar-only results are analytically equivalent to GCD/BoostCD (same CFG enforcement; \S\ref{sec:related_work}).}
697	\label{tab:gcd-comparison}
698	\end{table*}
699	
700	Our grammar layer implements the same CFG-based token masking as GCD and BoostCD---the mechanisms are formally identical (JSON schema $\to$ pushdown automaton $\to$ per-step allowed token set).
701	Table~\ref{tab:scierc-ablation} row~2 therefore constitutes a direct comparison: grammar-only enforcement achieves RV/ET$\to$0\% but only ${\sim}$3\% DR reduction, identical to what GCD-family methods would achieve on IE tasks.
702	
703	% exp_id: vllm_guided_json_scierc_zs
704	\paragraph{External verification via vLLM.}
705	To confirm this equivalence experimentally, we evaluated vLLM's \texttt{guided\_json} mode~\cite{kwon2023vllm}---an independent CFG enforcement implementation---on SciERC under identical conditions (Qwen3-8B, zero-shot, 551 documents).
706	
707	\begin{table}[h]
708	\centering
709	\small
710	\resizebox{\columnwidth}{!}{%
711	\begin{tabular}{@{}l rrrr r@{}}
712	\toprule
713	\textbf{Method} & \textbf{DR\,$\downarrow$} & \textbf{RV\,$\downarrow$} & \textbf{ET\,$\downarrow$} & \textbf{CF} & \textbf{R-F1\,$\uparrow$} \\
714	\midrule
715	Grammar-Only (XGrammar) & 14.84 & 0 & 0 & 9.90 & 8.23 \\
716	vLLM \texttt{guided\_json} & 15.26 & 0 & 0 & --- & 8.75 \\
717	\midrule
718	$\Delta$ & $+$0.42 & 0 & 0 & --- & $+$0.52 \\
719	\bottomrule
720	\end{tabular}}
721	\caption{GCD-equivalence verification: OntoCoDec grammar-only vs.\ vLLM \texttt{guided\_json} on SciERC (Qwen3-8B, zero-shot, 551 documents). All differences $<$0.5\,pp, confirming that CFG-based approaches---regardless of implementation---leave ${\sim}$15\% DR violations unaddressed.}
722	\label{tab:vllm-verification}
723	\end{table}
724	
725	All metrics differ by $<$0.5\,pp (Table~\ref{tab:vllm-verification}), confirming that any CFG-based constrained decoding tool---whether GCD, BoostCD, or vLLM---enforces the same constraint class and leaves the same ${\sim}$15\% DR gap.
726	The critical gap these methods cannot address is cross-field type consistency (Level~2), which requires the stateful semantic layer that maintains an entity registry across relation slots and enforces per-relation domain/range constraints at each type-bearing position.
727	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "017bb23e-94ae-48c3-a3c4-26f2df288c29",
  "isSidechain": true,
  "promptId": "3c296d38-0878-4eb6-acb2-f95c59b3b113",
  "agentId": "ab1cdc73b714a8d92",
  "type": "user",
  "uuid": "1b629256-a4d7-4dea-9236-ec384f9d645b",
  "sourceToolAssistantUUID": "017bb23e-94ae-48c3-a3c4-26f2df288c29",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "fa54a58a-15c0-4802-9034-a220e6d2d3d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "wild-sauteeing-hare"
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-25T20:50:36.140Z_

**Check 1: Abstract latency claim**
✓ PASS — Line 7 correctly states "1.5× unconstrained latency"

**Check 2: Post-hoc filtering table markers**

Looking at the table starting at line 481 (`\label{tab:posthoc-extended}`):
- Row for "Qwen | DocRED$^\ddagger$" at line 501 has the marker `$^\ddagger$` ✓
- Line 510 footnote explains: "Uses 4096-context LoRA variant; R-F1 differs from Table~\ref{tab:composability}'s standard LoRA configuration." ✓

Both checks **PASS**.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1b629256-a4d7-4dea-9236-ec384f9d645b",
  "isSidechain": true,
  "agentId": "ab1cdc73b714a8d92",
  "requestId": "req_011CbPwtyfhJY54xeZrfTbx3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a1cfba1c-672f-414f-8378-a37006809d1c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "fa54a58a-15c0-4802-9034-a220e6d2d3d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "wild-sauteeing-hare",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Dv3Cg2jbHfiPoqLPKHF74j",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 21774,
      "cache_read_input_tokens": 53938,
      "output_tokens": 167,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 21774
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 167,
          "cache_read_input_tokens": 53938,
          "cache_creation_input_tokens": 21774,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 21774,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---
