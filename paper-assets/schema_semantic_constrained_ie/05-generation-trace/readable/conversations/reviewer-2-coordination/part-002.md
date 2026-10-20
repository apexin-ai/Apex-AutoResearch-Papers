# Reviewer 2 coordination — Part 2 of 5

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Conversation logs

[← Part 1](part-001.md) · [Transcript overview](../reviewer-2-coordination.md) · [Part 3 →](part-003.md) · [Structured JSON](../../../sessions/16/16fda77cba37e7ffdcac.json)

## Round 12

### Tool call

_source line 500 · 2026-05-19T06:24:59.100027+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_runtime.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_runtime.tex"
  }
}
```

</details>

---


### Tool result

_source line 501 · 2026-05-19T06:24:59.100554+00:00_

1	% Runtime overhead (inline paragraph, no subsection header to save space)
2	
3	\paragraph{Runtime overhead.}
4	\label{sec:runtime}
5	S1 overhead is $+$13.1\% on SciERC and $+$2.43\% on DocRED (amortized over longer sequences); under LoRA, $+$10.0\% with 37\% lower absolute latency.
6	Grammar compile: one-time 44\,ms (Appendix~\ref{app:runtime}).
7	Scaling benchmarks confirm constant overhead (2--3\%) up to 200 entity types and 1{,}000 relations (Appendix~\ref{app:scalability}).
8	
9	\paragraph{Beam search compatibility.}
10	\label{sec:beam-results}
11	Under greedy S1, the grammar-first fallback resolves DR$\leftrightarrow$CF conflicts one token at a time; beam search ($k{=}4$) explores paths that satisfy both layers jointly, reducing DR and CF simultaneously.
12	With LoRA, beam S1 eliminates all four violation types on SciERC for both Qwen and Llama (R-F1 44.23, 46.11; Table~\ref{tab:beam-search}).
13	Under zero-shot, beam reduces DR to 0\% for calibrated models (Qwen, Llama) and CF substantially (9.90\%\,$\to$\,0.53\% Qwen; 6.56\%\,$\to$\,0.93\% Llama); Mistral remains a boundary condition (DR 7.99\%, CF 1.27\%) due to high baseline violations (Appendix~\ref{app:beam-search}).
14	Total latency overhead is 1.54$\times$ (beam 1.32$\times$ $+$ constraint 1.17$\times$; Table~\ref{tab:beam-latency}).
15	
16	% exp_ids: 70b_scierc_unconstrained, 70b_scierc_constrained, 70b_docred_unconstrained, 70b_docred_constrained
17	\paragraph{Cross-scale generalizability.}
18	\label{sec:70b-results}
19	On Llama-3.1-70B (AWQ INT4), OntoCoDec achieves DR$\to$0\% on SciERC (R-F1 $-$0.03\,pp) and \textbf{0\%} across ET, RV, and DR on the full DocRED 998-document set (R-F1 $+$0.04\,pp), the only configuration to completely eliminate DR on DocRED.
20	CF rises to 7.01\% (from 0.07\%); the low baseline reflects under-measurement (malformed outputs bypass the checker), while constrained decoding exposes more triples to the consistency check (\S\ref{sec:discussion}).
21	Model scale reduces b
…[truncated 37 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 502 · 2026-05-19T06:24:59.151167+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 503 · 2026-05-19T06:24:59.151659+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	We provide a detailed survey in Appendix~\ref{app:related_work}; here we position OntoCoDec.
5	Grammar-constrained decoding~\cite{dong2025xgrammar,willard2023outlines,beurer-kellner2023lmql,ugare2024syncode,park2024grammar,beurer-kellner2024domino,jsonschemabench2025} guarantees format validity but cannot enforce cross-field semantic constraints; type-constrained code generation~\cite{synchromesh_iclr2022,scholak2021picard,pldi2025_type_constrained_codegen} compiles type systems into token-level masks but operates on static type declarations, whereas IE requires a dynamic entity registry built during generation.
6	Vocabulary-constrained IE methods~\cite{geng2023gcd,sainz2024gollie,josifoski2022genie,guidex2025,vukovic2024dore,boostcd2025} restrict which tokens can appear but not which type combinations are valid per relation; EnriCo~\cite{zaratiana2024enrico} enforces structural constraints via ASP but requires supervised training and hand-crafted rules; IterGen~\cite{ugare2025itergen} supports semantic constraints via backtracking but requires manual implementation per constraint.
7	Training-based methods~\cite{paolini2021tanl,cabot2021rebel,lu2022uie,knowcoder_acl2024,li2023codeie,schema_rl2025} provide soft guidance; post-hoc approaches~\cite{khorshidi2025odke,spires_2024,ontologx_2025,slot2025} validate outputs after generation.
8	OntoCoDec prevents violations during decoding, is training-free, and compiles constraints automatically from ontology schemas.
9	Recent work shows constrained decoding can degrade reasoning~\cite{banerjee2025crane,grammar_aligned_2024,schall2025hiddencost,formattax2026,dccd2026}; however, extraction tasks are robust to format constraints~\cite{tam2024letmespeak}, and OntoCoDec constrains only type tokens while leaving entity spans unconstrained.
10	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 504 · 2026-05-19T06:24:59.352937+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion_compressed.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion_compressed.tex"
  }
}
```

</details>

---


### Tool result

_source line 505 · 2026-05-19T06:24:59.403727+00:00_

1	% Section 7 — Discussion and Conclusion (maximally compressed)
2	% Full discussion in Appendix; Mistral boundary condition in app:dual-factor.
3	
4	OntoCoDec compiles IE ontology schemas into composable token-level decoding constraints that compose losslessly with standard fine-tuning across both RE and EE: DR reaches $\leq$\,0.20\% with R-F1 within $\pm$0.6\,pp on RE (R-F1 40--46), RoV$\to$0\% and AC$\leq$0.8\% on EE, and beam search ($k{=}4$) eliminates all four RE violation types under fine-tuned decoding for calibrated models (\S\ref{sec:beam-results}).
5	Under zero-shot decoding, which stress-tests constraint robustness at R-F1 2--8\%, DR drops by 42--99\% across three models $\times$ three datasets with no significant F1 cost; constraint effectiveness holds across the full quality spectrum.
6	CF remains an open challenge for per-slot enforcement; global entity-level type consensus during decoding offers the most direct resolution path.
7	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 506 · 2026-05-19T06:25:06.791977+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 507 · 2026-05-19T06:25:07.244898+00:00_

1	\section{Extended Related Work}
2	\label{app:related_work}
3	
4	% ===========================================================================
5	% Paradigm 1: Grammar-Constrained Decoding
6	% ===========================================================================
7	\paragraph{Grammar-Constrained Decoding.}
8	Recent work has established efficient algorithms for restricting LLM outputs to conform to context-free grammars, making grammar-constrained decoding the de facto standard for obtaining structured output from language models.
9	XGrammar~\cite{dong2025xgrammar} partitions the vocabulary into context-independent and context-dependent tokens and maintains persistent pushdown automata across decoding steps, achieving up to 100$\times$ speedup over prior CFG-constrained decoding methods.
10	Outlines~\cite{willard2023outlines} reformulates constrained generation as finite-state machine transitions with offline vocabulary indexing, enabling efficient enforcement of regular-expression and JSON-schema constraints without runtime overhead per token.
11	LMQL~\cite{beurer-kellner2023lmql} introduces a declarative query language that compiles type, length, and regex constraints into token-level masks, providing a programmable interface for specifying multi-variable output structures.
12	These systems ensure that every generated token belongs to a grammar-valid continuation, but they do not address the \emph{distribution distortion} introduced by naive token masking.
13	A parallel line of work tackles this problem directly: DOMINO~\cite{beurer-kellner2024domino} minimizes distributional divergence during CFG enforcement by formulating mask selection as an optimization problem, and ASAp~\cite{park2024grammar} provides a provably unbiased sampling algorithm that preserves the original LM distribution under grammar constraints.
14	Together, these advances have made grammar-constrained decoding both fast and statistically principled, establishing a robust foundation for stru
…[truncated 19788 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 508 · 2026-05-19T06:25:07.296201+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 509 · 2026-05-19T06:25:08.053894+00:00_

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
26	The two-layer architecture produces two distinct fallback mechanisms with different semant
…[truncated 30822 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 757
}
```

</details>

---


### Tool call

_source line 510 · 2026-05-19T06:25:08.155066+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/relwork_new_entries.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/relwork_new_entries.bib"
  }
}
```

</details>

---


### Tool result

_source line 511 · 2026-05-19T06:25:08.408452+00:00_

1	% ============================================================
2	% Merged authoritative BibTeX references (9 entries)
3	% Merged 2026-05-14 from relwork_new_entries.bib + new_references.bib
4	% ============================================================
5	
6	% Confirmed via: Semantic Scholar, arXiv:2201.11227, OpenReview
7	% Venue: ICLR 2022 (cite key corrected from synchromesh_neurips2022)
8	@inproceedings{synchromesh_iclr2022,
9	  title     = {Synchromesh: Reliable Code Generation from Pre-trained Language Models},
10	  author    = {Poesia, Gabriel and Polozov, Oleksandr and Le, Vu and Tiwari, Ashish and Soares, Gustavo and Meek, Christopher and Gulwani, Sumit},
11	  booktitle = {International Conference on Learning Representations},
12	  year      = {2022},
13	  url       = {https://openreview.net/forum?id=KmtVD97J43e}
14	}
15	
16	% Confirmed via: NeurIPS 2023 proceedings, microsoft/monitors4codegen GitHub
17	@inproceedings{mgd_neurips2023,
18	  title     = {Monitor-Guided Decoding of Code {LMs} with Static Analysis of Repository Context},
19	  author    = {Agrawal, Lakshya A. and Kanade, Aditya and Goyal, Navin and Lahiri, Shuvendu K. and Rajamani, Sriram K.},
20	  booktitle = {Advances in Neural Information Processing Systems},
21	  volume    = {36},
22	  year      = {2023},
23	  url       = {https://proceedings.neurips.cc/paper_files/paper/2023/hash/662b1774ba8845fc1fa3d1fc0177ceeb-Abstract-Conference.html}
24	}
25	
26	% Confirmed via: ACM DL doi:10.1145/3729274, arXiv:2504.09246, SRI Lab ETH
27	@article{pldi2025_type_constrained_codegen,
28	  title     = {Type-Constrained Code Generation with Language Models},
29	  author    = {M\"{u}ndler, Niels and He, Jingxuan and Wang, Hao and Sen, Koushik and Song, Dawn and Vechev, Martin},
30	  journal   = {Proceedings of the ACM on Programming Languages},
31	  volume    = {9},
32	  number    = {PLDI},
33	  year      = {2025},
34	  doi       = {10.1145/3729274},
35	  url       = {https://dl.acm.org/doi/10.1145/372927
…[truncated 30256 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 253
}
```

</details>

---


### Tool call

_source line 512 · 2026-05-19T06:25:13.439445+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_prompts.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_prompts.tex"
  }
}
```

</details>

---


### Tool result

_source line 513 · 2026-05-19T06:25:14.445342+00:00_

1	% Appendix — Prompt Templates
2	% W10: Extraction prompts used in all experiments.
3	
4	\section{Prompt Templates}
5	\label{app:prompts}
6	
7	All experiments use the same prompts across constrained and unconstrained decoding; constraints are applied at the logit level, not through prompt modification.
8	Table~\ref{tab:prompts} shows the system and user prompts for each dataset.
9	
10	\begin{table*}[t]
11	\centering
12	\small
13	\begin{tabular}{@{}p{0.95\textwidth}@{}}
14	\toprule
15	\textbf{SciERC --- System Prompt (Unconstrained \& Constrained)} \\
16	\midrule
17	\texttt{You are an expert information extraction system for scientific texts. Extract entities and relations from the given text.} \\[4pt]
18	\texttt{Entity types: Task, Method, Material, Metric, OtherScientificTerm, Generic} \\
19	\texttt{Relation types: Used-for, Feature-of, Hyponym-of, Part-of, Compare, Conjunction, Evaluate-for} \\[4pt]
20	\texttt{Output a JSON object with:} \\
21	\texttt{- "entities": list of \{"text": "...", "type": "..."\}} \\
22	\texttt{- "relations": list of \{"head": "...", "tail": "...", "type": "...", "head\_type": "...", "tail\_type": "..."\}} \\[4pt]
23	\texttt{Output ONLY valid JSON, no explanation.} \\
24	\midrule
25	\textbf{SciERC --- User Prompt} \\
26	\midrule
27	\texttt{Extract all entities and relations from this scientific text:} \\
28	\texttt{"\{text\}"} \\
29	\texttt{Output JSON:} \\
30	\midrule
31	\midrule
32	\textbf{DocRED --- System Prompt (Unconstrained \& Constrained)} \\
33	\midrule
34	\texttt{You are an information extraction system. Extract all entities and relations from the following document.} \\[4pt]
35	\texttt{Entity types: PER, ORG, LOC, TIME, NUM, MISC} \\[4pt]
36	\texttt{Relation types: country, instance of, performer, ...\ (96 Wikidata relation types; full list omitted for space)} \\[4pt]
37	\texttt{Output a JSON object with exactly this structure:} \\
38	\texttt{\{"entities": [\{"text": "entity name", "type": "ENTITY\_TYPE"\}],} \\
39	\texttt{\ "
…[truncated 770 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1005
}
```

</details>

---


### Tool call

_source line 514 · 2026-05-19T06:25:14.445966+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_scalability.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_scalability.tex"
  }
}
```

</details>

---


### Tool result

_source line 515 · 2026-05-19T06:25:14.948890+00:00_

1	\section{Ontology Scalability}
2	\label{app:scalability}
3	
4	\begin{table}[h]
5	\centering
6	\small
7	\resizebox{\columnwidth}{!}{%
8	\begin{tabular}{@{}lrrrr@{}}
9	\toprule
10	\textbf{Scale} & \textbf{Types} & \textbf{Rels} & \textbf{Compile (s)} & \textbf{Overhead} \\
11	\midrule
12	Small (SciERC) & 6 & 7 & 0.33 & 1.02$\times$ \\
13	Medium (DocRED) & 6 & 96 & 0.32 & 1.03$\times$ \\
14	Large (synth.) & 100 & 500 & 0.35 & 1.03$\times$ \\
15	XLarge (synth.) & 200 & 1{,}000 & 0.42 & 1.03$\times$ \\
16	\bottomrule
17	\end{tabular}}
18	\caption{Compilation time (one-time) and per-token inference overhead across ontology scales. Small and Medium use real ontologies; Large and XLarge use synthetic ontologies with random domain/range constraints. Overhead measured on Qwen3-8B, 10 documents per scale.}
19	\label{tab:scalability}
20	\end{table}
21	
22	Grammar compilation scales sub-linearly (0.33\,s to 0.37\,s for 7$\to$1{,}000 relations); semantic constraint compilation grows linearly but remains negligible (0.4\,ms to 17\,ms).
23	Inference overhead is constant at 2--3\% because XGrammar uses precompiled bitmasks ($O(1)$ per token) and the semantic layer checks only the active relation's domain/range set rather than the full ontology.
24	The practical limit is first-token uniqueness: when entity types exceed $\sim$200, prefix collisions in the tokenizer vocabulary may require fallback to multi-token disambiguation (\S\ref{sec:dynamic-masking}).
25	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 516 · 2026-05-19T06:25:14.949250+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_beam_search.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_beam_search.tex"
  }
}
```

</details>

---


### Tool result

_source line 517 · 2026-05-19T06:25:15.401558+00:00_

1	\section{Beam Search Compatibility}
2	\label{app:beam-search}
3	
4	OntoCoDec's constraint enforcement is designed to be decoding-strategy agnostic.
5	The main experiments (\S\ref{sec:experiments}) use greedy decoding; Appendix~\ref{app:sampling} validates nucleus sampling.
6	Here we verify compatibility with beam search, completing coverage of the three standard decoding strategies.
7	
8	\paragraph{Implementation challenges.}
9	Two stateful components require adaptation for beam search.
10	(1)~The grammar layer (XGrammar) maintains an internal \texttt{GrammarMatcher} state that tracks the generated token sequence; beam reordering invalidates this state because beams are permuted across steps.
11	Our solution instantiates a fresh \texttt{GrammarMatcher} per beam per step and replays the beam's current token sequence through XGrammar's stateless accept API (64 lines of code).
12	(2)~The semantic layer's \texttt{TypeConstraintProcessor} accumulates entity and relation registries that assume a single generation path.
13	Our solution isolates state per beam by calling \texttt{detect()} on the full partial output at each step, reconstructing all entity/relation state from scratch for each beam independently (61 lines of code).
14	Both adaptations add ${\sim}125$ lines total without modifying the existing greedy/sampling logic.
15	
16	\paragraph{Results.}
17	Table~\ref{tab:beam-search} compares beam search ($k{=}4$, \texttt{early\_stopping=True}) against greedy decoding under full S1 constraints across six model-dataset combinations.
18	
19	\begin{table}[h]
20	\centering
21	\small
22	\caption{Beam search ($k{=}4$) vs.\ greedy decoding under full S1 constraints.
23	SciERC evaluated on full test set (551 documents); DocRED evaluated on matched 50-document subsets (same documents for greedy and beam).
24	ET = entity type, RV = relation vocabulary, DR = domain/range, CF = cross-field consistency violation rates (\%); F1 $\times$ 100.}
25	\label{tab:beam-search}
26	\begin{tab
…[truncated 7979 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 518 · 2026-05-19T06:25:15.402021+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_sampling_table.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_sampling_table.tex"
  }
}
```

</details>

---


### Tool result

_source line 519 · 2026-05-19T06:25:15.954765+00:00_

1	\section{Sampling Robustness}\label{app:sampling}
2	
3	\begin{table}[h]
4	\centering
5	\caption{Constraint robustness under nucleus sampling ($T$=0.7, $p$=0.9) vs.\ greedy decoding (Qwen3-8B, full S1 constraints).}
6	\label{tab:sampling-robustness}
7	\begin{tabular}{llcccccc}
8	\toprule
9	Dataset & Decoding & ET\% & RV\% & DR\% & CF\% & E-F1 & R-F1 \\
10	\midrule
11	\multirow{2}{*}{SciERC (551)} & Greedy & 0 & 0 & 0.93 & 9.90 & 30.98 & 8.36 \\
12	& Sampling & 0 & 0 & 0.75 & 9.90 & 31.28 & 7.42 \\
13	\midrule
14	\multirow{2}{*}{DocRED (114$^\dagger$)} & Greedy & 0 & 0.03 & 10.21 & 2.57 & 59.37 & 8.23 \\
15	& Sampling & 0 & 0 & 10.31 & 12.63 & 57.05 & 7.92 \\
16	\bottomrule
17	\end{tabular}
18	\par\smallskip\footnotesize $^\dagger$Subset of 114 documents; full DocRED sampling requires ${\sim}300$h due to extended generation under high-temperature sampling with complex schemas.
19	\end{table}
20	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 520 · 2026-05-19T06:25:15.955147+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_reproducibility.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_reproducibility.tex"
  }
}
```

</details>

---


### Tool result

_source line 521 · 2026-05-19T06:25:16.005652+00:00_

1	\section{Reproducibility Details}
2	\label{app:reproducibility}
3	
4	\paragraph{Fine-tuning configuration.}
5	All four fine-tuned models (Qwen3-8B and Llama-3.1-8B-Instruct on SciERC and DocRED) use identical LoRA hyperparameters: rank $r{=}16$, $\alpha{=}32$, dropout $0.05$, no bias, targeting all attention and MLP projection layers (\texttt{q\_proj}, \texttt{k\_proj}, \texttt{v\_proj}, \texttt{o\_proj}, \texttt{gate\_proj}, \texttt{up\_proj}, \texttt{down\_proj}).
6	Training uses AdamW with learning rate $2{\times}10^{-4}$, cosine schedule, warmup ratio $0.1$, effective batch size $16$, bf16 precision, gradient checkpointing, and completion-only loss for 3 epochs.
7	SciERC trains on 1,762 examples (260 dev) for 333 steps; DocRED trains on 3,053 examples (998 dev) for 573 steps.
8	Maximum sequence length is 2,048 (SciERC) and 4,096 (DocRED).
9	All runs use seed 42.
10	
11	\paragraph{Hardware and software.}
12	Training runs on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (98\,GB VRAM).
13	SciERC fine-tuning takes approximately 11 minutes per model; DocRED takes approximately 1.5 hours.
14	Software versions: PyTorch 2.10, Transformers 4.57, PEFT 0.19, TRL 1.1, Accelerate 1.13.
15	
16	\paragraph{Inference time.}
17	Inference timing is reported in Appendix~\ref{app:runtime} (NVIDIA RTX PRO 6000 Blackwell Server Edition GPU, same hardware as training).
18	Full S1 constrained decoding adds $+$13.1\% wall-clock overhead on SciERC and $+$2.43\% on DocRED (Qwen3-8B, zero-shot greedy); under LoRA fine-tuning, overhead is $+$10.0\% on SciERC.
19	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 522 · 2026-05-19T06:25:21.296864+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_llama_per_relation.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_llama_per_relation.tex"
  }
}
```

</details>

---


### Tool result

_source line 523 · 2026-05-19T06:25:22.260986+00:00_

1	% Appendix C — Per-Relation Violation Analysis (Llama-3.1-8B)
2	% exp_ids: llama_docred_unconstrained, llama_docred_full_s1
3	
4	\section{Per-Relation Violation Analysis (Llama-3.1-8B)}\label{app:llama-per-relation}
5	
6	Table~\ref{tab:llama-per-relation-dr} presents the per-relation domain--range violation breakdown for Llama-3.1-8B on DocRED under full S1 constraints.
7	The Llama baseline exhibits an RV rate of 16.03\%, substantially lower than Qwen's 29.66\%, indicating stronger baseline vocabulary compliance.
8	% exp_ids: llama_docred_unconstrained (RV=16.03%), qwen_docred_unconstrained (RV=29.66%)
9	Full S1 completely eliminates RV violations and reduces the residual DR rate to 2.55\% (418/16{,}368 triples), with only three relations exceeding 10\%.
10	% exp_ids: llama_docred_full_s1 (DR=2.6%, 418/16368)
11	
12	\begin{table}[h]
13	\centering
14	\caption{Top 10 per-relation DR violation rates for Llama-3.1-8B on DocRED under full S1 constraints. Relations with $>$20 triples and 0\% DR (e.g., P131, P206, P361, P170, P86) are omitted.}
15	\label{tab:llama-per-relation-dr}
16	\resizebox{\columnwidth}{!}{%
17	\begin{tabular}{@{}llrrr@{}}
18	\toprule
19	Relation & PID & Triples & DR Violations & DR Rate (\%) \\
20	\midrule
21	dissolved/demolished & P576 & 73 & 24 & 32.9 \\
22	followed by          & P156 & 117 & 24 & 20.5 \\
23	unemployment rate    & P1198 & 15 & 3 & 20.0 \\
24	end time             & P582 & 130 & 21 & 16.2 \\
25	instance of          & P31  & 290 & 37 & 12.8 \\
26	product/material produced & P1056 & 98 & 11 & 11.2 \\
27	location of formation & P740 & 81 & 8 & 9.9 \\
28	head of state        & P35  & 41  & 3  & 7.3 \\
29	applies to jurisdiction & P1001 & 637 & 45 & 7.1 \\
30	conflict             & P607 & 453 & 30 & 6.6 \\
31	\bottomrule
32	\end{tabular}}
33	\end{table}
34	% exp_ids: llama_docred_full_s1
35	
36	Compared with Qwen, which retains a 10.21\% residual DR under full S1 concentrated in P1198 (83\% fallback) and P171 (78\% fallback), Llama's re
…[truncated 523 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 964
}
```

</details>

---


### Tool call

_source line 524 · 2026-05-19T06:25:22.312486+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_doc_length.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_doc_length.tex"
  }
}
```

</details>

---


### Tool result

_source line 525 · 2026-05-19T06:25:22.764573+00:00_

1	\section{Effect of Document Length on Constraint Effectiveness}
2	\label{app:doc-length}
3	
4	To examine whether OntoCoDec's constraint effectiveness varies with document complexity, we partition test documents into three length bins (tertile split by word count) and report per-bin violation counts and F1.
5	
6	\begin{table}[h]
7	\centering
8	\small
9	\caption{Document length breakdown on SciERC (Qwen3-8B). Tertile boundaries: Short $\leq$ 19 words, Medium $\leq$ 27, Long $>$ 27.}
10	\label{tab:doc-length-scierc}
11	\begin{tabular}{ll rrrrr rr}
12	\toprule
13	\textbf{Bin} & \textbf{Mode} & \textbf{ET} & \textbf{RV} & \textbf{DR} & \textbf{CF} & \textbf{Total} & \textbf{E-F1} & \textbf{R-F1} \\
14	\midrule
15	Short (196)  & Uncon. &  1 &  5 &  57 & 0 &  63 & 32.4 &  8.9 \\
16	             & Const. &  0 &  0 &   5 & 5 &  10 & 32.4 &  8.9 \\
17	\midrule
18	Medium (180) & Uncon. &  6 &  9 & 104 & 0 & 119 & 27.8 &  6.7 \\
19	             & Const. &  0 &  0 &   7 & 15 & 22 & 27.8 &  6.7 \\
20	\midrule
21	Long (175)   & Uncon. &  3 & 10 & 104 & 1 & 118 & 29.9 &  7.0 \\
22	             & Const. &  0 &  0 &   4 & 20 & 24 & 30.0 &  7.3 \\
23	\bottomrule
24	\end{tabular}
25	\end{table}
26	
27	\begin{table}[h]
28	\centering
29	\small
30	\caption{Document length breakdown on DocRED (Qwen3-8B). Tertile boundaries: Short $\leq$ 160 words, Medium $\leq$ 208, Long $>$ 208.}
31	\label{tab:doc-length-docred}
32	\begin{tabular}{ll rrrrr rr}
33	\toprule
34	\textbf{Bin} & \textbf{Mode} & \textbf{ET} & \textbf{RV} & \textbf{DR} & \textbf{CF} & \textbf{Total} & \textbf{E-F1} & \textbf{R-F1} \\
35	\midrule
36	Short (336)  & Uncon. & 177 & 1238 & 1021 &   9 & 2445 & 61.1 &  9.3 \\
37	             & Const. &   0 &    0 &  495 & 138 &  633 & 62.6 &  9.6 \\
38	\midrule
39	Medium (332) & Uncon. & 147 & 1742 & 1047 &   5 & 2941 & 59.3 &  7.9 \\
40	             & Const. &   0 &    5 &  544 & 180 &  729 & 60.7 &  8.5 \\
41	\midrule
42	Long (330)   & Uncon. & 176 & 2209 & 1162 &   3 & 3550 & 53.9 
…[truncated 1448 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 526 · 2026-05-19T06:25:22.765067+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_prompt_sensitivity.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_prompt_sensitivity.tex"
  }
}
```

</details>

---


### Tool result

_source line 527 · 2026-05-19T06:25:22.765317+00:00_

1	\section{Prompt Sensitivity Analysis}
2	\label{app:prompt-sensitivity}
3	
4	To verify that OntoCoDec's constraint enforcement is robust to prompt variation, we evaluate three prompt variants on SciERC using Qwen3-8B (551 test documents): \textbf{Default} (the prompt used in all main experiments), \textbf{Minimal} (a shortened version listing only entity/relation types), and \textbf{Detailed} (an extended version with type definitions and extraction guidelines). All three variants share the same output JSON schema; only the instruction text differs. Each variant is decoded in both unconstrained and constrained (full Stage~1) modes.
5	
6	\begin{table}[h]
7	\centering
8	\small
9	\caption{Prompt sensitivity results on SciERC (Qwen3-8B, 551 documents). ET, RV, DR denote entity-type, relation-vocabulary, and domain-range violation rates (\%), respectively. $\Delta$DR shows the relative reduction from unconstrained to constrained decoding.}
10	\label{tab:prompt-sensitivity}
11	\begin{tabular}{llcccccc}
12	\toprule
13	\textbf{Prompt} & \textbf{Mode} & \textbf{ET\%} & \textbf{RV\%} & \textbf{DR\%} & \textbf{$\Delta$DR} & \textbf{E-F1} & \textbf{R-F1} \\
14	\midrule
15	\multirow{2}{*}{Default}
16	  & Unconstrained & 0.40 & 1.39 & 15.37 & \multirow{2}{*}{94.0\%} & 31.01 & 8.23 \\
17	  & Constrained   & 0.00 & 0.00 &  0.93 &                         & 30.98 & 8.36 \\
18	\midrule
19	\multirow{2}{*}{Minimal}
20	  & Unconstrained & 0.58 & 1.16 & 16.91 & \multirow{2}{*}{94.6\%} & 31.98 & 7.91 \\
21	  & Constrained   & 0.00 & 0.00 &  0.92 &                         & 31.99 & 7.85 \\
22	\midrule
23	\multirow{2}{*}{Detailed}
24	  & Unconstrained & 0.22 & 0.45 & 11.07 & \multirow{2}{*}{94.2\%} & 33.55 & 10.48 \\
25	  & Constrained   & 0.00 & 0.00 &  0.64 &                         & 33.56 & 10.48 \\
26	\bottomrule
27	\end{tabular}
28	\end{table}
29	
30	Table~\ref{tab:prompt-sensitivity} shows that constrained decoding eliminates entity-type and relation-vocabulary violations entirely (E
…[truncated 967 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 528 · 2026-05-19T06:25:23.719252+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_case_studies.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_case_studies.tex"
  }
}
```

</details>

---


### Tool result

_source line 529 · 2026-05-19T06:25:23.920705+00:00_

1	% Appendix — Error Analysis and Case Studies
2	
3	\section{Error Analysis and Case Studies}
4	\label{app:case-studies}
5	
6	\definecolor{violation}{RGB}{220,50,50}
7	\definecolor{fixed}{RGB}{34,139,34}
8	\definecolor{cfwarn}{RGB}{200,120,0}
9	
10	We present four representative cases illustrating constraint behavior across violation types. Cases 1--3 demonstrate OntoCoDec's corrective mechanisms; Case 4 illustrates a limitation.
11	
12	\subsection{Domain-Range Correction}
13	\label{app:case-dr}
14	
15	\noindent\textbf{Input (SciERC, Qwen3-8B):} \textit{``We present a novel model-based approach to recover the shapes and the poses of transparent objects from known motion.''}
16	
17	The unconstrained model assigns \textsc{OtherScientificTerm} to ``shapes'' and ``poses,'' producing \textsc{Feature-of}(\textsc{Task}, \textsc{OtherScientificTerm}) triples that violate domain/range constraints. The semantic layer redirects the tail type to \textsc{Task}, yielding schema-compliant triples (Table~\ref{tab:case1}).
18	
19	\begin{table}[h]
20	\centering
21	\small
22	\caption{OntoCoDec corrects three Feature-of DR violations. \textcolor{violation}{Red} = violation; \textcolor{fixed}{green} = corrected.}
23	\label{tab:case1}
24	\begin{tabular}{@{}p{3.2cm}lll@{}}
25	\toprule
26	\textbf{Triple} & \textbf{Head} & \textbf{Tail} & \textbf{DR} \\
27	\midrule
28	\multicolumn{4}{@{}l}{\textit{Unconstrained (3 violations)}} \\
29	\midrule
30	Feature-of(recover, shapes) & Task & \textcolor{violation}{OtherSciTerm} & \textcolor{violation}{\ding{55}} \\
31	Feature-of(recover, poses) & Task & \textcolor{violation}{OtherSciTerm} & \textcolor{violation}{\ding{55}} \\
32	Feature-of(recover, transp.\ obj.) & Task & \textcolor{violation}{OtherSciTerm} & \textcolor{violation}{\ding{55}} \\
33	Used-for(model approach, recover) & Method & Task & \ding{51} \\
34	\midrule
35	\multicolumn{4}{@{}l}{\textit{OntoCoDec (0 violations)}} \\
36	\midrule
37	Feature-of(recover, shapes) & Task & \textcolor{fixe
…[truncated 5951 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 530 · 2026-05-19T06:25:23.971655+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_full_ft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_full_ft.tex"
  }
}
```

</details>

---


### Tool result

_source line 531 · 2026-05-19T06:25:24.022424+00:00_

1	\section{Full Fine-Tuning Baseline}
2	\label{app:full-ft}
3	
4	To verify that constraint effectiveness generalizes beyond LoRA, we evaluate Qwen3-8B with full-parameter fine-tuning on SciERC (same data, 3 epochs, lr=$2{\times}10^{-4}$, seed 42).
5	
6	\begin{table}[h]
7	\centering
8	\small
9	\begin{tabular}{@{}lrrrr@{}}
10	\toprule
11	& \textbf{E-F1} & \textbf{R-F1} & \textbf{DR\%} & \textbf{CF\%} \\
12	\midrule
13	Full FT unconstrained & 64.78 & 37.89 & 2.74 & 0 \\
14	Full FT + S1 & 64.78 & 37.89 & \textbf{0} & 1.31 \\
15	\midrule
16	LoRA unconstrained & 66.86 & 43.65 & 0.31 & 0 \\
17	LoRA + S1 & 67.05 & 43.77 & \textbf{0} & 1.18 \\
18	\bottomrule
19	\end{tabular}
20	\caption{Full fine-tuning vs.\ LoRA on SciERC (Qwen3-8B, 551 docs). Constraints eliminate DR under both methods. Full FT underperforms LoRA, likely due to an untuned learning rate ($2{\times}10^{-4}$, standard for LoRA but high for full FT). F1 is unaffected by constraints in both cases.}
21	\label{tab:full-ft}
22	\end{table}
23	
24	Full fine-tuning retains 2.74\% DR violations (30 triples), concentrated in Part-of (14.6\%), Hyponym-of (9.6\%), and Evaluate-for (8.4\%). S1 eliminates all 30 violations with no F1 cost, confirming that constraint enforcement is effective regardless of the fine-tuning method. The CF$\leftrightarrow$DR trade-off persists (CF 0\%$\to$1.31\%), consistent with the LoRA pattern (1.18\%).
25	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 532 · 2026-05-19T06:25:35.236485+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "—",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "—",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
    "output_mode": "content",
    "glob": "*.tex"
  }
}
```

</details>

---


### Tool result

_source line 533 · 2026-05-19T06:25:35.739154+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft_9b84f1.tex:1:% Section 5 — DocRED Results (Draft)
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_prompts.tex:1:% Appendix — Prompt Templates
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_crossmodel_draft.tex:1:% Section 5 — Cross-Model Validation (compressed, 830→~400 words)
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_method_draft.tex:1:% Section 3 — Method (Draft)
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion_550cbf_DEPRECATED.tex:1:% Section 7 — Conclusion
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex:1:% Appendix B — Extended Discussion
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex:354:% exp_id: p8c_ft_scierc_latency — Reviewer Report #23 verified
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_relwork_additions.tex:2:% Related Work Additions — compiled 2026-05-14
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_relwork_additions.tex:60:% STATUS: VERIFIED — paper exists and description is accurate
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion_DEPRECATED.tex:1:% Section 7 — Conclusion
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_llama_per
…[truncated 1632 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 534 · 2026-05-19T06:25:36.191376+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": " – ",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": " – ",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
    "output_mode": "content",
    "glob": "*.tex"
  }
}
```

</details>

---


### Tool result

_source line 535 · 2026-05-19T06:25:36.926270+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 734
}
```

</details>

---


### Tool call

_source line 536 · 2026-05-19T06:25:37.612237+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "ing,|ing\\.",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
  "output_mode": "content",
  "glob": "*.tex",
  "head_limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "ing,|ing\\.",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
    "output_mode": "content",
    "glob": "*.tex",
    "head_limit": "50"
  }
}
```

</details>

---


### Tool result

_source line 537 · 2026-05-19T06:25:38.231088+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/discussion_paragraphs_cf83d1.tex:16:The contribution of this work is the constraint enforcement method itself; the zero-shot setting isolates its effect from confounds introduced by task-specific fine-tuning.
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft_9b84f1.tex:161:\paragraph{Constraint tightness governs enforcement ceiling.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section1_introduction_draft.tex:8:Violations persist across the capability spectrum: 15.4\% of triples on SciERC~\cite{luan2018scierc} and 18.5\% on DocRED~\cite{yao2019docred} under zero-shot decoding, and 1--2\% even after LoRA fine-tuning, driven by \emph{constraint tightness} (few valid type pairs per relation) rather than ontology or model scale.
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section1_introduction_draft.tex:24:Composed with LoRA fine-tuning, OntoCoDec reduces DR to $\leq$\,0.20\% at $<$0.6\,pp F1 cost (R-F1 40--46); under zero-shot decoding (R-F1 2--8\%), which stress-tests constraint robustness, DR drops by 94\% on SciERC while remaining F1-neutral.
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section2_background.tex:12:\paragraph{Grammar-Constrained Decoding.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_doc_length.tex:69:F1 scores are preserved or slightly improved under constrained decoding, with DocRED showing +0.9--1.5 E-F1 and +0.2--0.6 R-F1 improvement in the constrained setting.
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appe
…[truncated 13704 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 618
}
```

</details>

---


### Tool call

_source line 538 · 2026-05-19T06:25:38.734087+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "leverage|utilize|facilitate|delve",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "leverage|utilize|facilitate|delve",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
    "output_mode": "content",
    "glob": "*.tex"
  }
}
```

</details>

---


### Tool result

_source line 539 · 2026-05-19T06:25:38.784789+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 540 · 2026-05-19T06:25:47.577795+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "---",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
  "output_mode": "content",
  "glob": "*.tex",
  "head_limit": "30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "---",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
    "output_mode": "content",
    "glob": "*.tex",
    "head_limit": "30"
  }
}
```

</details>

---


### Tool result

_source line 541 · 2026-05-19T06:25:48.130700+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/discussion_paragraphs_cf83d1.tex:13:When applied to fine-tuned models that reach competitive F1 levels, the same constraints remain necessary---Phase~0 analysis confirms that even well-prompted models exhibit non-trivial violation rates (15.37\% DR on SciERC).
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/discussion_paragraphs_cf83d1.tex:23:Domain/range (DR) violations produce structurally invalid triples---a triple asserting that a \emph{Task} entity fills the \emph{domain} slot of \textsc{Part-of}, which requires \emph{Method}, cannot be consumed by any downstream system without error.
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/discussion_paragraphs_cf83d1.tex:26:The dominant conflict pattern---\emph{Generic}$\leftrightarrow$\emph{OtherScientificTerm} (60 of 245~affected entities on SciERC)---reflects genuine semantic ambiguity in the type system rather than a systematic method failure.
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/discussion_paragraphs_cf83d1.tex:41:The DocRED baseline exhibits a relation-vocabulary (RV) violation rate of 29.66\%---5{,}189 predictions with OOV relation names---all of which become false positives under this protocol.
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft_9b84f1.tex:13:types---14$\times$ the ontology size of SciERC
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft_9b84f1.tex:40:  & 18.46 & ---
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft_9b84f1.tex:48:  
…[truncated 7157 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 542 · 2026-05-19T06:25:48.885924+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": ", demonstrating|, highlighting|, showcasing|, enabling|, establishing|, confirming|, indicating|, revealing|, suggesting",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
  "output_mode": "content",
  "glob": "*.tex",
  "head_limit": "40"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": ", demonstrating|, highlighting|, showcasing|, enabling|, establishing|, confirming|, indicating|, revealing|, suggesting",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
    "output_mode": "content",
    "glob": "*.tex",
    "head_limit": "40"
  }
}
```

</details>

---


### Tool result

_source line 543 · 2026-05-19T06:25:48.936832+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft_9b84f1.tex:179:for the model to redirect probability mass toward, enabling
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_full_ft.tex:24:Full fine-tuning retains 2.74\% DR violations (30 triples), concentrated in Part-of (14.6\%), Hyponym-of (9.6\%), and Evaluate-for (8.4\%). S1 eliminates all 30 violations with no F1 cost, confirming that constraint enforcement is effective regardless of the fine-tuning method. The CF$\leftrightarrow$DR trade-off persists (CF 0\%$\to$1.31\%), consistent with the LoRA pattern (1.18\%).
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_doc_length.tex:67:Longer documents produce more violations in the unconstrained setting (e.g., DocRED long-bin: 3,550 vs.\ short-bin: 2,445), yet OntoCoDec achieves proportionally similar reduction, confirming that the constraint framework scales reliably with document complexity.
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_related_work.tex:10:Outlines~\cite{willard2023outlines} reformulates constrained generation as finite-state machine transitions with offline vocabulary indexing, enabling efficient enforcement of regular-expression and JSON-schema constraints without runtime overhead per token.
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_related_work.tex:14:Together, these advances have made grammar-constrained decoding both fast and statistically principled, establishing a robust foundation for structured generation.
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_related_work.tex:22:In programmi
…[truncated 9006 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 544 · 2026-05-19T06:26:11.872970+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "Furthermore|Moreover|Additionally|Notably|It is worth noting",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "Furthermore|Moreover|Additionally|Notably|It is worth noting",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
    "output_mode": "content",
    "glob": "*.tex"
  }
}
```

</details>

---


### Tool result

_source line 545 · 2026-05-19T06:26:12.074343+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_prompt_sensitivity.tex:32:[Omitted long matching line]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 546 · 2026-05-19T06:26:12.125228+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": ", confirming",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
  "output_mode": "count",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": ", confirming",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
    "output_mode": "count",
    "glob": "*.tex"
  }
}
```

</details>

---


### Tool result

_source line 547 · 2026-05-19T06:26:12.125854+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_full_ft.tex:1
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_doc_length.tex:1
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion_550cbf_DEPRECATED.tex:1
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex:6
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion_DEPRECATED.tex:2
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_prompt_sensitivity.tex:1
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/discussion_paragraphs.tex:1
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft_4796e8.tex:1

Found 14 total occurrences across 8 files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 548 · 2026-05-19T06:26:16.347196+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
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

_source line 549 · 2026-05-19T06:26:16.397871+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 550 · 2026-05-19T06:26:20.064272+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR 2025 2026 reviewer guidelines review form criteria dimensions scoring"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2025 2026 reviewer guidelines review form criteria dimensions scoring"
  }
}
```

</details>

---


### Tool call

_source line 551 · 2026-05-19T06:26:20.265777+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 ARR review form soundness excitement novelty reproducibility scoring rubric"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 ARR review form soundness excitement novelty reproducibility scoring rubric"
  }
}
```

</details>

---


### Tool result

_source line 552 · 2026-05-19T06:26:27.095661+00:00_

Web search results for query: "ACL ARR 2025 2026 reviewer guidelines review form criteria dimensions scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"https://aclrollingreview.org/"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"}]

Based on the search results, here's what I found about ACL/ARR 2025-2026 reviewer guidelines:

## Reviewer Guidelines Overview

The ARR peer review guidelines are a work-in-progress and will be updated as ARR evolves, and reviewers should always check whether the version they are familiar with is still the current one before starting an assignment.

## Review Requirements

All reviewers must familiarize themselves with the latest version of the ARR reviewer guidelines and perform the reviews on time and in line with ARR requirements.

## Recent Policy Updates (2025-2026)

Starting from May 2025, ACL introdu
…[truncated 983 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7031
}
```

</details>

---


### Tool result

_source line 553 · 2026-05-19T06:26:27.648562+00:00_

Web search results for query: "EMNLP 2026 ARR review form soundness excitement novelty reproducibility scoring rubric"

Links: [{"title":"ARR Reviewer Guidelines","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Program Chairs’ Report on Peer Review at ACL 2023 Anna Rogers}","url":"https://aclanthology.org/2023.acl-long.report.pdf"},{"title":"Review Form","url":"http://aclrollingreview.org/reviewform"},{"title":"FAQ - EMNLP 2026","url":"https://2026.emnlp.org/faq/"},{"title":"Correction: Measuring novelty in science with word embedding","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12857975/"},{"title":"Development and Validation of a Scoring Rubric for Editorial Evaluation of Peer-review Quality: A Pilot Study","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11000557/"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"}]

Based on the search results, I found relevant information about the ARR (ACL Rolling Review) scoring rubric that applies to EMNLP submissions. Here's what I found:

## Scoring Dimensions

Excitement scores are separate from the assessment of soundness and are more subjective, reflecting personal taste. The Overall assessment score is an explicit recommendation for the outcome of a paper if it were committed to an *ACL venue, and is a composite score reflecting assessment of soundness and excitement.

## Soundness Evaluation

Reviewers assess whether a paper is sufficiently sound and thorough, whether it clearly states scientific claims and provides adequate support, and for experimental papers, they consider the depth/breadth of research questions, technical soundness of experiments, and methodological validity.

If a reviewer gives a low Sou
…[truncated 703 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7382
}
```

</details>

---


### Tool call

_source line 554 · 2026-05-19T06:26:30.260982+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
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

_source line 555 · 2026-05-19T06:26:30.312039+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 556 · 2026-05-19T06:26:34.380892+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form: all scoring dimensions, their scales (1-5 etc.), and descriptions of each score level. Focus on: Overall Assessment, Soundness, Excitement/Novelty, Reproducibility, and any other scored dimensions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form: all scoring dimensions, their scales (1-5 etc.), and descriptions of each score level. Focus on: Overall Assessment, Soundness, Excitement/Novelty, Reproducibility, and any other scored dimensions."
  }
}
```

</details>

---


### Tool call

_source line 557 · 2026-05-19T06:26:35.638636+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the reviewer guidelines: what dimensions reviewers are asked to evaluate, scoring rubrics, what counts as a strong/weak paper, specific criteria for soundness, novelty/excitement, and overall assessment."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the reviewer guidelines: what dimensions reviewers are asked to evaluate, scoring rubrics, what counts as a strong/weak paper, specific criteria for soundness, novelty/excitement, and overall assessment."
  }
}
```

</details>

---


### Tool result

_source line 558 · 2026-05-19T06:26:38.899383+00:00_

# ACL Rolling Review Form - Scoring Dimensions

## Overall Assessment
**Scale: 1-5**
- **5**: Consider for Award (top 2.5% papers)
- **4.5**: Borderline Award
- **4**: Conference acceptance
- **3.5**: Borderline Conference
- **3**: Findings acceptance
- **2.5**: Borderline Findings
- **2**: Resubmit next cycle
- **1.5**: Resubmit after next cycle
- **1**: Do not resubmit

## Soundness
**Scale: 1-5**
- **5**: Excellent thoroughness for its type
- **4**: Strong with "sufficient support for all claims"
- **3**: Acceptable with main claims supported
- **2**: Poor with unsupported claims
- **1**: Major issues preventing publication

## Excitement
**Scale: 1-5**
- **5**: Highly Exciting (would recommend presentation)
- **4**: Exciting (would mention to others)
- **3**: Interesting (might attend if available)
- **2**: Potentially Interesting but not resonant
- **1**: Not Exciting (limited community appeal)

## Reproducibility
**Scale: 1-5**
- **5**: Results easily reproducible
- **4**: Mostly reproducible with minor variations
- **3**: Reproducible with difficulty
- **2**: Hard to reproduce; unavailable data/details
- **1**: Cannot reproduce

## Additional Scored Dimensions
- **Reviewer Confidence** (1-5)
- **Datasets** (1-5): value to other researchers
- **Software** (1-5): utility for other researchers

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 4518
}
```

</details>

---


### Tool result

_source line 559 · 2026-05-19T06:26:42.013458+00:00_

# ARR Reviewer Guidelines: Evaluation Dimensions and Scoring

## Evaluation Dimensions

ARR reviewers assess papers on three primary dimensions:

1. **Soundness**: Technical validity and methodological rigor
2. **Excitement**: Personal interest and perceived contribution value
3. **Overall Recommendation**: Composite judgment for acceptance consideration

## Scoring Rubrics

### Soundness Assessment
Reviewers must justify low soundness scores through explicit review text. The guidelines emphasize that "if you give a low Soundness score without finding any major faults, this means that your review is not a faithful explanation."

### Excitement vs. Soundness
These dimensions are intentionally orthogonal. A paper may be technically sound but personally unexciting, or vice versa. "Such preferences are more subjective and should be reflected in a separate excitement score."

### Overall Recommendation
This composite score weighs soundness, excitement, novelty, and potential impact. Papers for main conferences must be "sufficiently sound and reproducible," though editors may accept technically sound work lacking personal excitement if it offers significant community value.

## Strong Paper Characteristics

- Clear research questions addressing identified knowledge gaps
- Appropriate claim scoping relative to evidence presented
- Technical soundness with valid proofs and sound argumentation
- Sufficient evidence supporting stated claims without excessive additional experiments
- Professional, constructive tone

## Common Weaknesses to Avoid Citing

The guidelines identify seventeen heuristics (H1-H17) representing flawed reasoning, including:
- Dismissing findings as "obvious in retrospect"
- Requiring SOTA results unnecessarily
- Penalizing simplicity, negative results, or non-English work
- Demanding experiments beyond claim requirements

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 6374
}
```

</details>

---


### Tool call

_source line 560 · 2026-05-19T06:29:04.254617+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
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

_source line 561 · 2026-05-19T06:29:04.305306+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 562 · 2026-05-19T06:30:51.361867+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 — Round 1 审稿意见\n\n**论文**: OntoCoDec: Type-Constrained Information Extraction via Compiled Ontology Constraints\n**Venue**: EMNLP 2026 (ARR May 2026)\n**审查侧重**: 新颖性 + 完整性 + 写作质量\n\n---\n\n## Summary（2-3 句）\n\n本文提出 OntoCoDec，将 IE ontology schema 编译为两层 token-level 解码约束：grammar 层保证 JSON 结构和词汇有效性（通过 XGrammar CFG），semantic 层通过有状态 entity registry 和动态 logit masking 在生成时强制 domain/range type 约束。在 SciERC、DocRED（RE）和 WikiEvents（EE）上跨 4 个模型评估，zero-shot DR 降低 42-99%，与 LoRA fine-tuning 组合后 DR ≤ 0.20% 且 R-F1 波动 < 0.6pp。论文实验非常全面，但核心技术新颖性有限（code domain 类型约束解码的迁移），且 CF trade-off 削弱了 zero-shot 场景下的整体故事。\n\n---\n\n## Strengths（逐条）\n\n**S1. 问题定义清晰且有实际价值。** 论文系统量化了 LLM-based IE 中的 ontological type violations（SciERC 15.37%, DocRED 18.46%），并证明 fine-tuning 后仍有 1-2% 残留（Table 2），为方法的必要性提供了有力论据。violation 分类体系（DR/RV/ET/CF 四类）清晰完整。\n\n**S2. Two-layer architecture 的 enabling dependency 有实验支撑。** Semantic-only 仅降低 DR 24%，加上 grammar 层后达到 94%（Table 1, §5.1）——这个 ablation 清楚地证明了两层组合的必要性，不仅是设计选择，而是经验验证的架构需求。\n\n**S3. Composability with fine-tuning 是最强贡献。** Table 2 显示 LoRA + S1 在 SciERC 和 DocRED 上 DR ≤ 0.20%，R-F1 在 ±0.6pp 内（R-F1 40-46 的部署级质量），CF 降至 ≤1.18%。这是真正有实用价值的结果：在 deployment-grade 质量下近乎无损地消除 type violations。\n\n**S4. 实验覆盖面异常全面。** 3 个数据集 × 4 个模型（含 70B）× 多种 decoding 策略（greedy/beam/sampling）× zero-shot 和 fine-tuned settings × 四向 ablation。beam search 消除所有四类 violation 的结果（Appendix F, Table 7）令人信服。cross-task generalization 到 EE（WikiEvents, 56 event types, 80 roles）无需架构修改也是亮点。\n\n**S5. 对 limitations 的处理诚实透明。** CF↔DR trade-off 通过专门的 fallback ablation（Appendix B, Table 5）分析，CF violation 分布的 Generic↔X 归因（Table 6）有说服力。论文没有隐藏 CF 上升的事实，而是提供了机理解释和两条解决路径。\n\n**S6. 可复现性极佳。** 完整的 LoRA 超参（Appendix G）、prompts（Appendix A）、硬件规格、软件版本、experiment IDs 均提供。承诺 acceptance 后开源。\n\n---\n\n## Weaknesses（逐条）\n\n**W1 [Should-Fix] 核心技术相对 code domain type-constrained decoding 的增量贡献有限。**\n\n核心机制——将类型约束编译为 token-level masks——已在代码生成领域由 PICARD（Scholak et al., 2021）、Synchromesh（Poesia et al., 2022）、MGD（Agrawal et al., 2023）和 Mündler et al.（PLDI 2025）充分验证。论文在 §6 和 Appendix B 中明确承认这一点，并将贡献定位为\"migrating the paradigm from code to IE\"。\n\nIE 特有的技术贡献是：(1) 生成过程中动态构建的 entity registry（vs. 代码中的静态类型声明），(2) pair-based sequential masking 利用 non-rectangular type signatures。这些是真实的工程贡献，但属于对已有范式的适配而非根本性的算法创新。\"Enabling dependency\"（grammar 层使能 semantic 层）本质上是一个架构设计选择——当然需要先保证词汇有效性才能查 domain/range 规则——将其作为\"发现\"来呈现有些过度包装。\n\n**建议**: 在 Introduction 中更明确地将增量贡献定位为 \"domain adaptation + novel engineering for IE-specific challenges\"，降低对 enabling dependency 作为 scientific insight 的强调。\n\n**W2 [Should-Fix] Constraint tightness 公式 (κ) 的分析价值被高估。**\n\nκ(r) = 1 - |V(r)|/|E|²（Eq. 2）是 valid type-pair fraction 的直接归一化。\"Dual-factor\" 分析（Appendix B, Figure 1）在仅 4 个数据点上拟合线性模型（R²=0.886, p≈0.058），论文坦诚这是\"descriptive rather than confirmatory\"。\n\n但在 Contribution #1 中将 \"rates are driven by constraint tightness rather than ontology scale\" 作为核心发现来宣传，与这个受限的统计支撑之间存在张力。SciERC 和 DocRED 的 DR 率恰好相近（15.37% vs 18.46%）可能是巧合而非 κ 的预测力——论文没有在其他数据集上验证这个 claim。\n\n**建议**: 弱化 Contribution #1 中的 causal language，改为\"constraint tightness correlates with enforcement difficulty\"。或增加更多数据集验证这个 pattern。\n\n**W3 [Should-Fix] Zero-shot framing 与论文实际价值不一致。**\n\n论文将 zero-shot 定位为 \"stress test for constraint robustness\"（§1, §7），但实验正文（§5.1-5.4）的主要内容是 zero-shot 结果，fine-tuning composability 仅作为补充段落出现。这创造了一个叙事矛盾：\n\n- 如果 practical value 在 fine-tuned quality（R-F1 40-46），论文应该以此为主线\n- 当前结构将最强结果（DR→0%, F1 neutral with LoRA）埋在了 R-F1 2-8% 的 zero-shot 分析之后\n- Zero-shot R-F1 = 2-8% 意味着模型几乎不能正确提取 relations，此时 type violation rate 的实际意义有限\n\n此外，zero-shot 下 CF 大幅上升（SciERC 0.08%→9.90%, WikiEvents 0→21%），总 violation burden (DR+CF) 从 15.45% 降到 10.83%（SciERC），净减少仅 ~30%——远不如 \"94% DR reduction\" 的标题数字那样令人印象深刻。\n\n**建议**: 重构叙事，以 fine-tuning composability 为主线（\"OntoCoDec 在 deployment-grade IE 中消除残留 type violations\"），zero-shot 作为 robustness/generalization 证据的补充角色。\n\n**W4 [Should-Fix] Appendix 扩展 Related Work 中 AI 写作痕迹密集。**\n\nAppendix B (Extended Related Work) 中 -ing 分词短语结尾模式密集出现，这是 AI 生成文本最显著的标志之一：\n\n- \"establishing a robust foundation for structured generation\"（App. B, line 14）\n- \"demonstrating that richer-than-CFG constraints can be compiled into token-level filtering\"（line 22）\n- \"establishing that semantic constraints can be expressed as dynamic token masks\"（line 26）\n- \"establishing the foundational principle that relational type compatibility should be a hard constraint\"（line 40）\n- \"enabling dynamic constraint evaluation that depends on previously decoded content\"（line 107）\n\n仅 Extended Related Work 中这个模式就出现 10+ 次。此外，\", confirming that\" 模式在各附录中出现 14 次（grep 统计），密度异常高。\n\n正文（§1-§7）相对干净，但附录是审稿人会阅读的内容，这些模式一旦被注意到会严重影响对论文的信任度。\n\n**建议**: 全文 grep `\", establishing\"`, `\", demonstrating\"`, `\", enabling\"`, `\", confirming\"` 并逐一改写为独立句子或用其他句式替代。\n\n**W5 [Should-Fix] WikiEvents fine-tuning 评估样本量过小。**\n\n§5.4 fine-tuning composability 段报告在仅 20 个文档上评估。Trigger F1 出现 \"-5.4/-0.6 pp shifts with wide confidence intervals at this sample size\"。20 个文档不足以支撑 \"fine-tuning composability extends to EE\" 的 claim。这是论文最薄弱的实验支撑。\n\n**建议**: 至少增加到 100+ 文档的评估，或显著弱化 EE composability 的 claim 表述。\n\n**W6 [Should-Fix] Abstract 信息密度过高，数字堆砌。**\n\nAbstract ~250 words（上限区域），包含至少 15 个具体数字：\"15.37%\", \"18.46%\", \"42-99%\", \"±0.6pp\", \"R-F1 40-46\", \"R-F1 2-8%\", \"0.20%\", \"12.02%\", \"0→12-18%\", \"21%\", \"≤1.2%\", \"8B to 70B\" 等。审稿人 30 秒内无法从中提取核心 insight，因为数字淹没了叙事。\n\n按照 CLAUDE.md 写作规范 §2.2：\"禁止堆砌数据：Abstract 不是 Results 的缩写。最多引用 2-3 个关键数字。\"\n\n**建议**: 精简到 3-4 个关键数字（例如：baseline DR rate, DR reduction under fine-tuning, F1 cost），其余用定性描述替代。\n\n**W7 [Minor] Contribution 列表冗余。**\n\n§1 列出 4 条 contributions，其中 #3 和 #4 高度重叠（均关于 constraint behavior across settings）。#1 (violation study) 和 #2 (method) 是核心，#3-#4 可合并为一条关于 composability 和 trade-off 分析的贡献。\n\n**W8 [Minor] Table 3 (DocRED ablation) Grammar-only 行 bold 标记逻辑混淆。**\n\nGrammar-only 的 R-F1 (8.31) 和 E-F1 (59.38) 标粗，因为它们确实是列最优，但 Full S1 才是论文推荐的配置。这可能误导读者以为 grammar-only 是更好的选择。Caption 中 \"Best per column in bold\" 虽然技术正确，但叙事上产生矛盾。\n\n**W9 [Minor] DocRED beam search 仅在 50 文档子集上评估。**\n\nAppendix F Table 7 中 DocRED beam search 使用 50 个匹配文档而非完整 998 个。\"Beam search eliminates DR for calibrated models on both RE datasets\" 的 claim 在 DocRED 上的统计支撑较弱。\n\n---\n\n## Questions（需要作者回答）\n\n**Q1.** CF↔DR trade-off 的量化：在 zero-shot 下，total violation burden (DR+CF) 的净变化是多少？能否提供 Pareto 分析而非分别报告 DR 和 CF？\n\n**Q2.** WikiEvents fine-tuning 为什么只在 20 文档上评估？是数据集限制还是计算限制？如果是后者，能否至少扩展到 50-100 文档？\n\n**Q3.** 能否设想一个 single integrated layer 直接在 type-bearing positions 同时强制 vocabulary membership 和 domain/range constraints，从而避免 \"enabling dependency\"？这样的设计相比两层方案有什么 trade-off？\n\n**Q4.** Constraint tightness (κ) 是否在 WikiEvents 的 EE setting 中也展现出类似的预测力？论文目前没有报告 WikiEvents 的 κ 值。\n\n**Q5.** Schema coverage gaps（fine-tuning 残留 DR 的 33%）是基于 training-set co-occurrence statistics 构建的——如果使用 ontology 的完整 domain/range 规范（而非 frequency-based）来构建约束表，能否消除这部分残留？\n\n---\n\n## Missing References\n\n引用数量（~56 条）符合 EMNLP 长文标准。覆盖了直接相关方法、baseline 论文、评测 benchmark 和理论基础。\n\n以下引用可选但非必须：\n- **Hokamp & Liu (2017)**, \"Lexically Constrained Decoding for Sequence Generation\"——constrained decoding 的早期基础工作，当前仅通过 NeuroLogic (Lu et al., 2021) 间接覆盖\n- **DEGREE (Hsu et al., 2022)**, 基于 prompt 的 event extraction，与 WikiEvents 评估相关\n- **Roth & Yih (2004)** 在正文 §6 中缺失——这是 IE 中 hard type constraints 的奠基性工作，目前仅在 Appendix B 中讨论，建议移入正文\n\n---\n\n## Overall Assessment\n\n### 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| **Soundness** | 4/5 | 实验方法论扎实，ablation 全面，统计检验规范（bootstrap CI, p-values）。CF trade-off 分析诚实但可更好地整合到主叙事。Fine-tuning 残留 DR 的 error analysis（Appendix B）尤其出色。 |\n| **Excitement** | 3/5 | 问题真实且有实用价值，但核心技术是已有 code-domain 范式向 IE 的工程迁移。Dynamic entity registry 和 pair-based sequential masking 是有价值的工程贡献，但不构成 algorithmic breakthrough。Composability 结果有 practical impact。 |\n| **Reproducibility** | 5/5 | 所有超参、prompt templates、硬件规格、软件版本、experiment IDs 均提供。一次性编译成本和推理开销有详细报告。承诺开源。 |\n\n### Overall Assessment\n\n**Overall: 3.5（Borderline Conference）**\n\n**置信度: 4/5**（熟悉 constrained decoding、information extraction 和相关工作）\n\n**理由**: 论文技术上 sound，实验异常全面，composability with fine-tuning 结果有真正的实用价值（DR ≤0.20%, F1 neutral）。可复现性接近完美。\n\n然而，核心技术新颖性有限——type constraints → token masks 的范式在 code domain 已有充分先例，IE-specific adaptation（dynamic registry, sequential masking）是有价值的工程贡献但不够 exciting。Constraint tightness 分析统计支撑不足。Zero-shot 为主的叙事结构不利于展现论文最强的贡献（fine-tuning composability），且 CF trade-off 使得 zero-shot 故事远不如 DR reduction 标题数字那样有说服力。Appendix 中 AI 写作痕迹密集，可能影响审稿人信任。\n\n**提升到 4.0 (Conference) 的路径**:\n1. 重构叙事以 fine-tuning composability 为主线\n2. 弱化 constraint tightness 的 causal claim 或增加数据集验证\n3. 扩大 WikiEvents fine-tuning 评估规模\n4. 精简 Abstract 中的数字堆砌\n5. 清除 Appendix 中的 AI 写作标志（-ing phrases, \", confirming\" pattern）",
  "reviewer_id": "2",
  "project": "schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 — Round 1 审稿意见\n\n**论文**: OntoCoDec: Type-Constrained Information Extraction via Compiled Ontology Constraints\n**Venue**: EMNLP 2026 (ARR May 2026)\n**审查侧重**: 新颖性 + 完整性 + 写作质量\n\n---\n\n## Summary（2-3 句）\n\n本文提出 OntoCoDec，将 IE ontology schema 编译为两层 token-level 解码约束：grammar 层保证 JSON 结构和词汇有效性（通过 XGrammar CFG），semantic 层通过有状态 entity registry 和动态 logit masking 在生成时强制 domain/range type 约束。在 SciERC、DocRED（RE）和 WikiEvents（EE）上跨 4 个模型评估，zero-shot DR 降低 42-99%，与 LoRA fine-tuning 组合后 DR ≤ 0.20% 且 R-F1 波动 < 0.6pp。论文实验非常全面，但核心技术新颖性有限（code domain 类型约束解码的迁移），且 CF trade-off 削弱了 zero-shot 场景下的整体故事。\n\n---\n\n## Strengths（逐条）\n\n**S1. 问题定义清晰且有实际价值。** 论文系统量化了 LLM-based IE 中的 ontological type violations（SciERC 15.37%, DocRED 18.46%），并证明 fine-tuning 后仍有 1-2% 残留（Table 2），为方法的必要性提供了有力论据。violation 分类体系（DR/RV/ET/CF 四类）清晰完整。\n\n**S2. Two-layer architecture 的 enabling dependency 有实验支撑。** Semantic-only 仅降低 DR 24%，加上 grammar 层后达到 94%（Table 1, §5.1）——这个 ablation 清楚地证明了两层组合的必要性，不仅是设计选择，而是经验验证的架构需求。\n\n**S3. Composability with fine-tuning 是最强贡献。** Table 2 显示 LoRA + S1 在 SciERC 和 DocRED 上 DR ≤ 0.20%，R-F1 在 ±0.6pp 内（R-F1 40-46 的部署级质量），CF 降至 ≤1.18%。这是真正有实用价值的结果：在 deployment-grade 质量下近乎无损地消除 type violations。\n\n**S4. 实验覆盖面异常全面。** 3 个数据集 × 4 个模型（含 70B）× 多种 decoding 策略（greedy/beam/sampling）× zero-shot 和 fine-tuned settings × 四向 ablation。beam search 消除所有四类 violation 的结果（Appendix F, Table 7）令人信服。cross-task generalization 到 EE（WikiEvents, 56 event types, 80 roles）无需架构修改也是亮点。\n\n**S5. 对 limitations 的处理诚实透明。** CF↔DR trade-off 通过专门的 fallback ablation（Appendix B, Table 5）分析，CF violation 分布的 Generic↔X 归因（Table 6）有说服力。论文没有隐藏 CF 上升的事实，而是提供了机理解释和两条解决路径。\n\n**S6. 可复现性极佳。** 完整的 LoRA 超参（Appendix G）、prompts（Appendix A）、硬件规格、软件版本、experiment IDs 均提供。承诺 acceptance 后开源。\n\n---\n\n## Weaknesses（逐条）\n\n**W1 [Should-Fix] 核心技术相对 code domain type-constrained decoding 的增量贡献有限。**\n\n核心机制——将类型约束编译为 token-level masks——已在代码生成领域由 PICARD（Scholak et al., 2021）、Synchromesh（Poesia et al., 2022）、MGD（Agrawal et al., 2023）和 Mündler et al.（PLDI 2025）充分验证。论文在 §6 和 Appendix B 中明确承认这一点，并将贡献定位为\"migrating the paradigm from code to IE\"。\n\nIE 特有的技术贡献是：(1) 生成过程中动态构建的 entity registry（vs. 代码中的静态类型声明），(2) pair-based sequential masking 利用 non-rectangular type signatures。这些是真实的工程贡献，但属于对已有范式的适配而非根本性的算法创新。\"Enabling dependency\"（grammar 层使能 semantic 层）本质上是一个架构设计选择——当然需要先保证词汇有效性才能查 domain/range 规则——将其作为\"发现\"来呈现有些过度包装。\n\n**建议**: 在 Introduction 中更明确地将增量贡献定位为 \"domain adaptation + novel engineering for IE-specific challenges\"，降低对 enabling dependency 作为 scientific insight 的强调。\n\n**W2 [Should-Fix] Constraint tightness 公式 (κ) 的分析价值被高估。**\n\nκ(r) = 1 - |V(r)|/|E|²（Eq. 2）是 valid type-pair fraction 的直接归一化。\"Dual-factor\" 分析（Appendix B, Figure 1）在仅 4 个数据点上拟合线性模型（R²=0.886, p≈0.058），论文坦诚这是\"descriptive rather than confirmatory\"。\n\n但在 Contribution #1 中将 \"rates are driven by constraint tightness rather than ontology scale\" 作为核心发现来宣传，与这个受限的统计支撑之间存在张力。SciERC 和 DocRED 的 DR 率恰好相近（15.37% vs 18.46%）可能是巧合而非 κ 的预测力——论文没有在其他数据集上验证这个 claim。\n\n**建议**: 弱化 Contribution #1 中的 causal language，改为\"constraint tightness correlates with enforcement difficulty\"。或增加更多数据集验证这个 pattern。\n\n**W3 [Should-Fix] Zero-shot framing 与论文实际价值不一致。**\n\n论文将 zero-shot 定位为 \"stress test for constraint robustness\"（§1, §7），但实验正文（§5.1-5.4）的主要内容是 zero-shot 结果，fine-tuning composability 仅作为补充段落出现。这创造了一个叙事矛盾：\n\n- 如果 practical value 在 fine-tuned quality（R-F1 40-46），论文应该以此为主线\n- 当前结构将最强结果（DR→0%, F1 neutral with LoRA）埋在了 R-F1 2-8% 的 zero-shot 分析之后\n- Zero-shot R-F1 = 2-8% 意味着模型几乎不能正确提取 relations，此时 type violation rate 的实际意义有限\n\n此外，zero-shot 下 CF 大幅上升（SciERC 0.08%→9.90%, WikiEvents 0→21%），总 violation burden (DR+CF) 从 15.45% 降到 10.83%（SciERC），净减少仅 ~30%——远不如 \"94% DR reduction\" 的标题数字那样令人印象深刻。\n\n**建议**: 重构叙事，以 fine-tuning composability 为主线（\"OntoCoDec 在 deployment-grade IE 中消除残留 type violations\"），zero-shot 作为 robustness/generalization 证据的补充角色。\n\n**W4 [Should-Fix] Appendix 扩展 Related Work 中 AI 写作痕迹密集。**\n\nAppendix B (Extended Related Work) 中 -ing 分词短语结尾模式密集出现，这是 AI 生成文本最显著的标志之一：\n\n- \"establishing a robust foundation for structured generation\"（App. B, line 14）\n- \"demonstrating that richer-than-CFG constraints can be compiled into token-level filtering\"（line 22）\n- \"establishing that semantic constraints can be expressed as dynamic token masks\"（line 26）\n- \"establishing the foundational principle that relational type compatibility should be a hard constraint\"（line 40）\n- \"enabling dynamic constraint evaluation that depends on previously decoded content\"（line 107）\n\n仅 Extended Related Work 中这个模式就出现 10+ 次。此外，\", confirming that\" 模式在各附录中出现 14 次（grep 统计），密度异常高。\n\n正文（§1-§7）相对干净，但附录是审稿人会阅读的内容，这些模式一旦被注意到会严重影响对论文的信任度。\n\n**建议**: 全文 grep `\", establishing\"`, `\", demonstrating\"`, `\", enabling\"`, `\", confirming\"` 并逐一改写为独立句子或用其他句式替代。\n\n**W5 [Should-Fix] WikiEvents fine-tuning 评估样本量过小。**\n\n§5.4 fine-tuning composability 段报告在仅 20 个文档上评估。Trigger F1 出现 \"-5.4/-0.6 pp shifts with wide confidence intervals at this sample size\"。20 个文档不足以支撑 \"fine-tuning composability extends to EE\" 的 claim。这是论文最薄弱的实验支撑。\n\n**建议**: 至少增加到 100+ 文档的评估，或显著弱化 EE composability 的 claim 表述。\n\n**W6 [Should-Fix] Abstract 信息密度过高，数字堆砌。**\n\nAbstract ~250 words（上限区域），包含至少 15 个具体数字：\"15.37%\", \"18.46%\", \"42-99%\", \"±0.6pp\", \"R-F1 40-46\", \"R-F1 2-8%\", \"0.20%\", \"12.02%\", \"0→12-18%\", \"21%\", \"≤1.2%\", \"8B to 70B\" 等。审稿人 30 秒内无法从中提取核心 insight，因为数字淹没了叙事。\n\n按照 CLAUDE.md 写作规范 §2.2：\"禁止堆砌数据：Abstract 不是 Results 的缩写。最多引用 2-3 个关键数字。\"\n\n**建议**: 精简到 3-4 个关键数字（例如：baseline DR rate, DR reduction under fine-tuning, F1 cost），其余用定性描述替代。\n\n**W7 [Minor] Contribution 列表冗余。**\n\n§1 列出 4 条 contributions，其中 #3 和 #4 高度重叠（均关于 constraint behavior across settings）。#1 (violation study) 和 #2 (method) 是核心，#3-#4 可合并为一条关于 composability 和 trade-off 分析的贡献。\n\n**W8 [Minor] Table 3 (DocRED ablation) Grammar-only 行 bold 标记逻辑混淆。**\n\nGrammar-only 的 R-F1 (8.31) 和 E-F1 (59.38) 标粗，因为它们确实是列最优，但 Full S1 才是论文推荐的配置。这可能误导读者以为 grammar-only 是更好的选择。Caption 中 \"Best per column in bold\" 虽然技术正确，但叙事上产生矛盾。\n\n**W9 [Minor] DocRED beam search 仅在 50 文档子集上评估。**\n\nAppendix F Table 7 中 DocRED beam search 使用 50 个匹配文档而非完整 998 个。\"Beam search eliminates DR for calibrated models on both RE datasets\" 的 claim 在 DocRED 上的统计支撑较弱。\n\n---\n\n## Questions（需要作者回答）\n\n**Q1.** CF↔DR trade-off 的量化：在 zero-shot 下，total violation burden (DR+CF) 的净变化是多少？能否提供 Pareto 分析而非分别报告 DR 和 CF？\n\n**Q2.** WikiEvents fine-tuning 为什么只在 20 文档上评估？是数据集限制还是计算限制？如果是后者，能否至少扩展到 50-100 文档？\n\n**Q3.** 能否设想一个 single integrated layer 直接在 type-bearing positions 同时强制 vocabulary membership 和 domain/range constraints，从而避免 \"enabling dependency\"？这样的设计相比两层方案有什么 trade-off？\n\n**Q4.** Constraint tightness (κ) 是否在 WikiEvents 的 EE setting 中也展现出类似的预测力？论文目前没有报告 WikiEvents 的 κ 值。\n\n**Q5.** Schema coverage gaps（fine-tuning 残留 DR 的 33%）是基于 training-set co-occurrence statistics 构建的——如果使用 ontology 的完整 domain/range 规范（而非 frequency-based）来构建约束表，能否消除这部分残留？\n\n---\n\n## Missing References\n\n引用数量（~56 条）符合 EMNLP 长文标准。覆盖了直接相关方法、baseline 论文、评测 benchmark 和理论基础。\n\n以下引用可选但非必须：\n- **Hokamp & Liu (2017)**, \"Lexically Constrained Decoding for Sequence Generation\"——constrained decoding 的早期基础工作，当前仅通过 NeuroLogic (Lu et al., 2021) 间接覆盖\n- **DEGREE (Hsu et al., 2022)**, 基于 prompt 的 event extraction，与 WikiEvents 评估相关\n- **Roth & Yih (2004)** 在正文 §6 中缺失——这是 IE 中 hard type constraints 的奠基性工作，目前仅在 Appendix B 中讨论，建议移入正文\n\n---\n\n## Overall Assessment\n\n### 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| **Soundness** | 4/5 | 实验方法论扎实，ablation 全面，统计检验规范（bootstrap CI, p-values）。CF trade-off 分析诚实但可更好地整合到主叙事。Fine-tuning 残留 DR 的 error analysis（Appendix B）尤其出色。 |\n| **Excitement** | 3/5 | 问题真实且有实用价值，但核心技术是已有 code-domain 范式向 IE 的工程迁移。Dynamic entity registry 和 pair-based sequential masking 是有价值的工程贡献，但不构成 algorithmic breakthrough。Composability 结果有 practical impact。 |\n| **Reproducibility** | 5/5 | 所有超参、prompt templates、硬件规格、软件版本、experiment IDs 均提供。一次性编译成本和推理开销有详细报告。承诺开源。 |\n\n### Overall Assessment\n\n**Overall: 3.5（Borderline Conference）**\n\n**置信度: 4/5**（熟悉 constrained decoding、information extraction 和相关工作）\n\n**理由**: 论文技术上 sound，实验异常全面，composability with fine-tuning 结果有真正的实用价值（DR ≤0.20%, F1 neutral）。可复现性接近完美。\n\n然而，核心技术新颖性有限——type constraints → token masks 的范式在 code domain 已有充分先例，IE-specific adaptation（dynamic registry, sequential masking）是有价值的工程贡献但不够 exciting。Constraint tightness 分析统计支撑不足。Zero-shot 为主的叙事结构不利于展现论文最强的贡献（fine-tuning composability），且 CF trade-off 使得 zero-shot 故事远不如 DR reduction 标题数字那样有说服力。Appendix 中 AI 写作痕迹密集，可能影响审稿人信任。\n\n**提升到 4.0 (Conference) 的路径**:\n1. 重构叙事以 fine-tuning composability 为主线\n2. 弱化 constraint tightness 的 causal claim 或增加数据集验证\n3. 扩大 WikiEvents fine-tuning 评估规模\n4. 精简 Abstract 中的数字堆砌\n5. 清除 Appendix 中的 AI 写作标志（-ing phrases, \", confirming\" pattern）",
    "reviewer_id": "2",
    "project": "schema_semantic_constrained_ie"
  }
}
```

</details>

---


### Tool result

_source line 563 · 2026-05-19T06:30:56.186234+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_01fc90ae186a4ed432770f7601995139:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4824
}
```

</details>

---


### Assistant

_source line 564 · 2026-05-19T06:31:04.927914+00:00_

审稿意见已提交给 Review Director。

总结：我以 Reviewer 2 身份完成了 Round 1 审稿，侧重新颖性、完整性和写作质量。Overall 评分 **3.5（Borderline Conference）**。主要发现：

- **优势**：问题定义清晰、实验极其全面（3 数据集 × 4 模型 × 多解码策略）、fine-tuning composability 结果强（DR ≤0.20%, F1 neutral）、对 CF trade-off 的处理诚实透明、可复现性极佳
- **关键问题**：核心技术相对 code-domain type-constrained decoding 增量有限（W1）、zero-shot 为主的叙事结构不利于展示最强贡献（W3）、Abstract 数字堆砌（W6）、Appendix related work 中 AI 写作痕迹密集（W4）、WikiEvents fine-tuning 仅 20 文档评估（W5）、constraint tightness 分析统计支撑不足（W2）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2"
}
```

</details>

---


## Round 13

## Round 13

4 recorded events


### User

_source line 565 · 2026-05-19T06:31:50.460213+00:00_

[Round 1 审稿请求]:
## Step 2 — 交叉分享：请回应 Reviewer 1 的审稿意见

以下是 Reviewer 1 的完整审稿意见。请逐条回应，对每条 Weakness 标注 [AGREE] 或 [REBUT]，并给出理由。如果你同意，说明为什么；如果你反驳，请引用论文中的具体 Section/Table/Figure 作为证据。

---

### Reviewer 1 审稿意见原文

**Overall: 3.5（Borderline Conference）| Soundness 3.5/5 | Excitement 3/5 | Confidence 4/5**

**一句话总结**: 核心两层约束架构设计合理、实验覆盖面广、limitation 讨论诚实，但关键统计声明基于极小样本（n=4/6）、EE composability 验证仅 20 篇 test set、缺少与 schema-aware IE baseline 的直接对比。

**Must-Fix（2 条）**:

**W1** dual-factor pattern R²=0.886 基于 n=4（p≈0.058 不显著），Spearman ρ=-0.77 基于 n=6（临界值~0.886），正文用词"predicts"过强。需降级措辞或增加数据点。

**W2** WikiEvents fine-tuning composability test set 仅 20 篇，trigger F1 shift -5.4pp 可能纯粹是噪声，但支撑了 Abstract/Contribution 中的 EE composability claim。需报告 CI/p-value 并说明为何不用更大 test set。

**Should-Fix（5 条）**:

**W3** 无 schema-aware IE baseline（GoLLIE/KnowCoder/BoostCD/GCD）的实验对比。

**W4** Abstract "DR drops by 42-99%" 可能误导——42% 对应 Mistral DocRED 仍残留 33% violation。

**W5** EE fine-tuned CF 率未报告。

**W6** DocRED beam search 仅 50 doc 子集。

**W7** 约束表基于频率统计而非完整 ontology schema 导致不可消除的 coverage gap，需解释原因。

**Minor（2 条）**:

**W8** bib 有 8 个 orphan 条目（duplicate keys）。

**W9** Limitations section 需分条/分段提高可读性。

**主要优势**: 清晰的问题定义和形式化；pair-based enforcement 的非矩形分析；跨模型×跨任务×跨规模验证覆盖面广；CF trade-off 诚实讨论和 beam search 缓解路径。

---

请逐条回应每个 Weakness（W1-W9），对每条标注 **[AGREE]** 或 **[REBUT]**。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 566 · 2026-05-19T06:33:15.546616+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 交叉回应 — 对 Reviewer 1 (R1) 审稿意见逐条回应\n\n---\n\n**[AGREE] R1-W1: dual-factor pattern 统计支撑不足，\"predicts\" 措辞过强**\n\n完全同意。我在自己的审稿中也独立提出了相同问题（R2-W2）。论文自身在 Appendix B 中承认\"descriptive characterization rather than an independently confirmatory statistical test\"（Appendix B, app:dual-factor 段），但 §4 正文仍使用\"predicts the cross-dataset results\"这一因果性措辞，Introduction Contribution #1 也将\"rates are driven by constraint tightness\"作为核心发现宣传。4 个数据点、p≈0.058 不足以支撑 causal claim。\n\n补充：即使 SciERC (κ̄=0.333) 和 DocRED (κ̄=0.842) 的 baseline DR 恰好相近（15.37% vs 18.46%），这也不能排除是巧合——论文没有在 WikiEvents 或其他数据集上验证 κ 的预测力。WikiEvents 有 245 个约束，完全可以计算 κ 并检验。\n\n**建议与 R1 一致**: 降级措辞为 \"correlates with\" / \"is associated with\"，或增加 WikiEvents 等数据集的验证。\n\n---\n\n**[AGREE] R1-W2: WikiEvents fine-tuning test set 仅 20 篇，不足以支撑 EE composability claim**\n\n完全同意，这也是我审稿中的独立发现（R2-W5）。§5.4 fine-tuning 段原文承认 \"with wide confidence intervals at this sample size\"，但 Abstract 和 Contribution #3 仍然宣称 \"Fine-tuning composability extends to EE: LoRA + S1 eliminates RoV and reduces AC to ≤0.8% on WikiEvents\"，没有任何 qualification。20 个文档上的 trigger F1 shift -5.4pp 完全可能是噪声，这使得 EE composability 成为论文最薄弱的实验支撑。\n\n补充一个 R1 未提到的问题：论文 zero-shot WikiEvents 评估用了 246 个文档（Table 4），但 fine-tuning 评估仅用 20 个——为什么 fine-tuning setting 不能用相同规模的 test set？如果是数据分割限制（train/test split），应该在正文中解释。\n\n---\n\n**[AGREE] R1-W3: 缺少与 schema-aware IE baseline 的直接实验对比**\n\n同意这是一个 gap，但我认为严重程度需要 nuance。\n\n论文的 positioning 是 \"training-free, decoding-time enforcement\"，与 GoLLIE/KnowCoder 这类 training-based 方法不在同一 axes 上竞争——后者是提升 extraction quality (F1)，前者是在给定 F1 下保证 type safety。§6 明确指出两者是 complementary：\"a system like GoLLIE could be combined with OntoCoDec's constraint layers\"。\n\n然而，缺少实验验证这个 complementarity claim 是遗憾的。如果能展示 GoLLIE + OntoCoDec > GoLLIE alone（在 violation rate 上），论文的 practical value story 会更有说服力。GCD (Geng et al., 2023) 作为最接近的 grammar-constrained IE 方法，在论文中实际上有隐式对比——Table 1 Grammar-only 行本质上就是 GCD 的 ceiling（§5.1: \"DR remains at 14.84%, the ceiling of grammar-based decoding\"），但这应该更明确地标注。\n\n**部分同意**: GCD 的隐式对比已存在但应显式化；GoLLIE/KnowCoder 对比是 nice-to-have 但不是同一赛道。\n\n---\n\n**[AGREE] R1-W4: Abstract \"DR drops by 42-99%\" 可能误导**\n\n同意。42% 对应 Mistral DocRED（Table 3: 57.42%→33.20%），仍残留 33.20% violations——这不是一个令人印象深刻的结果。Abstract 使用 \"42-99%\" 的 range 给读者留下的印象偏向 99% 那端。\n\n我在 R2-W6 中也指出了 Abstract 数字堆砌的更广泛问题。将 Mistral 作为 \"boundary condition\"（§5.3 原文用语）是合理的，但 Abstract 中将其与 calibrated models 的结果混在同一个 range 里，模糊了这个重要区分。\n\n**建议**: Abstract 中分开报告 calibrated models (76-99%) 和 boundary condition (42%)，或者直接只报告 calibrated models 的结果。\n\n---\n\n**[AGREE] R1-W5: EE fine-tuned CF 率未报告**\n\n同意。§5.4 fine-tuning 段报告了 RoV→0% 和 AC≤0.8%，但没有报告 CF。考虑到 zero-shot EE 下 CF 高达 15-21%（Table 4），fine-tuning 后 CF 是否同样大幅降低是一个关键问题。如果 EE fine-tuned CF 仍然很高，这会进一步削弱 EE composability claim。遗漏这个数字让人怀疑结果可能不理想。\n\n---\n\n**[REBUT] R1-W6: DocRED beam search 仅 50 doc 子集**\n\n部分反驳。R1 标注为 Should-Fix，但我认为这是 Minor 级别。\n\n理由：(1) beam search 在 SciERC 上使用了完整 551 文档 test set（Appendix F, Table 7 标题明确标注 \"SciERC (551)\"），DR→0% 的结果在完整集上是确认的；(2) DocRED 50 文档子集使用 matched documents（相同文档在 greedy 和 beam 间比较），这是方法论上合理的控制实验；(3) beam search 的计算成本是 greedy 的 1.54× （Table 8），在 998 个 DocRED 文档（平均 19.81s/doc）上运行 beam search 需要约 8.5 小时——可以做但成本不低。\n\n不过，50 个文档上的 DR=0% 确实统计功效有限。如果 base rate 是 ~10%（greedy S1 下 DocRED DR=10.21%），50 个文档中预期约 5 个 DR violation，DR→0% 的 95% CI 上界约 5.8%（Clopper-Pearson）。这比 R1 暗示的要弱。\n\n**建议**: 这是 minor issue，但如果作者有计算资源，扩展到 200+ 文档会增强 claim。\n\n---\n\n**[AGREE] R1-W7: 约束表基于频率统计而非完整 ontology schema，导致 coverage gap**\n\n同意这是需要解释的设计选择。Appendix B residual DR error analysis（app:residual-dr-analysis）明确指出 33% 的残留 violations 来自 \"schema coverage gaps: the frequency-based constraint table does not cover long-tail type pairs that are ontologically valid but rare\"。\n\n这引出一个自然问题：SciERC 和 DocRED 都有完整的 ontology schema 定义（SciERC 论文 Table 3, DocRED 的 Wikidata properties），为什么不直接使用完整 schema 而要用 frequency-based 近似？\n\n可能的原因：DocRED 的 96 个 Wikidata relations 的完整 domain/range 规范可能不容易从原始数据中干净提取（Wikidata property constraints 不总是完整或一致的）。但如果是这样，论文应该解释这个工程决策。\n\n这也与我 R2-Q5 中的问题一致。如果使用完整 ontology schema，那 33% 的 coverage gap 可能被消除，fine-tuned DR 可以进一步降低。\n\n---\n\n**[REBUT] R1-W8: bib 有 8 个 orphan 条目**\n\n无法从论文内容角度判断这个问题的严重性。LaTeX 编译时 orphan bib entries（未被 \\cite 引用的条目）不会出现在输出 PDF 中，因此不影响读者或审稿人体验。如果 R1 指的是 duplicate keys（同一工作有两个不同 cite key），那可能导致引用混乱，但需要具体指出哪些条目重复。\n\n从我对 bib 文件的阅读来看，`grammar_aligned_2024` 和 `park2024grammar` 确实指向同一篇论文（Park et al., Grammar-Aligned Decoding, NeurIPS 2024）——这是一个真实的 duplicate。但这属于格式清理问题，不影响学术判断。\n\n**判定**: Minor，但 duplicate keys 确实应该清理。\n\n---\n\n**[AGREE] R1-W9: Limitations section 需分条/分段**\n\n同意。当前 Limitations section（main.tex lines 67-80）是一个连续的密集段落，包含了至少 10 个不同的 limitation points，混在一起难以阅读。fine-tuning scope、CF trade-off、scalability、zero-shot coverage、beam search、full fine-tuning 等 limitations 交织在一起。\n\nARR 要求 Limitations section 存在且实质性——当前内容是实质性的，但格式严重影响可读性。分成 3-4 个带标题的子段（如 \"Constraint Scope\", \"Evaluation Coverage\", \"Scalability\"）会大幅改善。\n\n---\n\n## 总结\n\n与 R1 的 9 条 Weaknesses 中：\n- **[AGREE] 7 条**: W1, W2, W3 (部分), W4, W5, W7, W9\n- **[REBUT] 2 条**: W6 (应降为 Minor), W8 (编译层面不影响输出)\n\nR1 和 R2 独立发现了 3 个相同的核心问题：\n1. **Dual-factor 统计支撑不足** (R1-W1 = R2-W2)\n2. **WikiEvents fine-tuning 20 文档过小** (R1-W2 = R2-W5)\n3. **Abstract 数字表述可能误导** (R1-W4 ⊂ R2-W6)\n\n两位 reviewer 均给出 **3.5 (Borderline Conference)**，核心共识是：实验全面、执行扎实，但技术新颖性有限且关键 claims 的统计支撑不足。",
  "reviewer_id": "2",
  "project": "schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 交叉回应 — 对 Reviewer 1 (R1) 审稿意见逐条回应\n\n---\n\n**[AGREE] R1-W1: dual-factor pattern 统计支撑不足，\"predicts\" 措辞过强**\n\n完全同意。我在自己的审稿中也独立提出了相同问题（R2-W2）。论文自身在 Appendix B 中承认\"descriptive characterization rather than an independently confirmatory statistical test\"（Appendix B, app:dual-factor 段），但 §4 正文仍使用\"predicts the cross-dataset results\"这一因果性措辞，Introduction Contribution #1 也将\"rates are driven by constraint tightness\"作为核心发现宣传。4 个数据点、p≈0.058 不足以支撑 causal claim。\n\n补充：即使 SciERC (κ̄=0.333) 和 DocRED (κ̄=0.842) 的 baseline DR 恰好相近（15.37% vs 18.46%），这也不能排除是巧合——论文没有在 WikiEvents 或其他数据集上验证 κ 的预测力。WikiEvents 有 245 个约束，完全可以计算 κ 并检验。\n\n**建议与 R1 一致**: 降级措辞为 \"correlates with\" / \"is associated with\"，或增加 WikiEvents 等数据集的验证。\n\n---\n\n**[AGREE] R1-W2: WikiEvents fine-tuning test set 仅 20 篇，不足以支撑 EE composability claim**\n\n完全同意，这也是我审稿中的独立发现（R2-W5）。§5.4 fine-tuning 段原文承认 \"with wide confidence intervals at this sample size\"，但 Abstract 和 Contribution #3 仍然宣称 \"Fine-tuning composability extends to EE: LoRA + S1 eliminates RoV and reduces AC to ≤0.8% on WikiEvents\"，没有任何 qualification。20 个文档上的 trigger F1 shift -5.4pp 完全可能是噪声，这使得 EE composability 成为论文最薄弱的实验支撑。\n\n补充一个 R1 未提到的问题：论文 zero-shot WikiEvents 评估用了 246 个文档（Table 4），但 fine-tuning 评估仅用 20 个——为什么 fine-tuning setting 不能用相同规模的 test set？如果是数据分割限制（train/test split），应该在正文中解释。\n\n---\n\n**[AGREE] R1-W3: 缺少与 schema-aware IE baseline 的直接实验对比**\n\n同意这是一个 gap，但我认为严重程度需要 nuance。\n\n论文的 positioning 是 \"training-free, decoding-time enforcement\"，与 GoLLIE/KnowCoder 这类 training-based 方法不在同一 axes 上竞争——后者是提升 extraction quality (F1)，前者是在给定 F1 下保证 type safety。§6 明确指出两者是 complementary：\"a system like GoLLIE could be combined with OntoCoDec's constraint layers\"。\n\n然而，缺少实验验证这个 complementarity claim 是遗憾的。如果能展示 GoLLIE + OntoCoDec > GoLLIE alone（在 violation rate 上），论文的 practical value story 会更有说服力。GCD (Geng et al., 2023) 作为最接近的 grammar-constrained IE 方法，在论文中实际上有隐式对比——Table 1 Grammar-only 行本质上就是 GCD 的 ceiling（§5.1: \"DR remains at 14.84%, the ceiling of grammar-based decoding\"），但这应该更明确地标注。\n\n**部分同意**: GCD 的隐式对比已存在但应显式化；GoLLIE/KnowCoder 对比是 nice-to-have 但不是同一赛道。\n\n---\n\n**[AGREE] R1-W4: Abstract \"DR drops by 42-99%\" 可能误导**\n\n同意。42% 对应 Mistral DocRED（Table 3: 57.42%→33.20%），仍残留 33.20% violations——这不是一个令人印象深刻的结果。Abstract 使用 \"42-99%\" 的 range 给读者留下的印象偏向 99% 那端。\n\n我在 R2-W6 中也指出了 Abstract 数字堆砌的更广泛问题。将 Mistral 作为 \"boundary condition\"（§5.3 原文用语）是合理的，但 Abstract 中将其与 calibrated models 的结果混在同一个 range 里，模糊了这个重要区分。\n\n**建议**: Abstract 中分开报告 calibrated models (76-99%) 和 boundary condition (42%)，或者直接只报告 calibrated models 的结果。\n\n---\n\n**[AGREE] R1-W5: EE fine-tuned CF 率未报告**\n\n同意。§5.4 fine-tuning 段报告了 RoV→0% 和 AC≤0.8%，但没有报告 CF。考虑到 zero-shot EE 下 CF 高达 15-21%（Table 4），fine-tuning 后 CF 是否同样大幅降低是一个关键问题。如果 EE fine-tuned CF 仍然很高，这会进一步削弱 EE composability claim。遗漏这个数字让人怀疑结果可能不理想。\n\n---\n\n**[REBUT] R1-W6: DocRED beam search 仅 50 doc 子集**\n\n部分反驳。R1 标注为 Should-Fix，但我认为这是 Minor 级别。\n\n理由：(1) beam search 在 SciERC 上使用了完整 551 文档 test set（Appendix F, Table 7 标题明确标注 \"SciERC (551)\"），DR→0% 的结果在完整集上是确认的；(2) DocRED 50 文档子集使用 matched documents（相同文档在 greedy 和 beam 间比较），这是方法论上合理的控制实验；(3) beam search 的计算成本是 greedy 的 1.54× （Table 8），在 998 个 DocRED 文档（平均 19.81s/doc）上运行 beam search 需要约 8.5 小时——可以做但成本不低。\n\n不过，50 个文档上的 DR=0% 确实统计功效有限。如果 base rate 是 ~10%（greedy S1 下 DocRED DR=10.21%），50 个文档中预期约 5 个 DR violation，DR→0% 的 95% CI 上界约 5.8%（Clopper-Pearson）。这比 R1 暗示的要弱。\n\n**建议**: 这是 minor issue，但如果作者有计算资源，扩展到 200+ 文档会增强 claim。\n\n---\n\n**[AGREE] R1-W7: 约束表基于频率统计而非完整 ontology schema，导致 coverage gap**\n\n同意这是需要解释的设计选择。Appendix B residual DR error analysis（app:residual-dr-analysis）明确指出 33% 的残留 violations 来自 \"schema coverage gaps: the frequency-based constraint table does not cover long-tail type pairs that are ontologically valid but rare\"。\n\n这引出一个自然问题：SciERC 和 DocRED 都有完整的 ontology schema 定义（SciERC 论文 Table 3, DocRED 的 Wikidata properties），为什么不直接使用完整 schema 而要用 frequency-based 近似？\n\n可能的原因：DocRED 的 96 个 Wikidata relations 的完整 domain/range 规范可能不容易从原始数据中干净提取（Wikidata property constraints 不总是完整或一致的）。但如果是这样，论文应该解释这个工程决策。\n\n这也与我 R2-Q5 中的问题一致。如果使用完整 ontology schema，那 33% 的 coverage gap 可能被消除，fine-tuned DR 可以进一步降低。\n\n---\n\n**[REBUT] R1-W8: bib 有 8 个 orphan 条目**\n\n无法从论文内容角度判断这个问题的严重性。LaTeX 编译时 orphan bib entries（未被 \\cite 引用的条目）不会出现在输出 PDF 中，因此不影响读者或审稿人体验。如果 R1 指的是 duplicate keys（同一工作有两个不同 cite key），那可能导致引用混乱，但需要具体指出哪些条目重复。\n\n从我对 bib 文件的阅读来看，`grammar_aligned_2024` 和 `park2024grammar` 确实指向同一篇论文（Park et al., Grammar-Aligned Decoding, NeurIPS 2024）——这是一个真实的 duplicate。但这属于格式清理问题，不影响学术判断。\n\n**判定**: Minor，但 duplicate keys 确实应该清理。\n\n---\n\n**[AGREE] R1-W9: Limitations section 需分条/分段**\n\n同意。当前 Limitations section（main.tex lines 67-80）是一个连续的密集段落，包含了至少 10 个不同的 limitation points，混在一起难以阅读。fine-tuning scope、CF trade-off、scalability、zero-shot coverage、beam search、full fine-tuning 等 limitations 交织在一起。\n\nARR 要求 Limitations section 存在且实质性——当前内容是实质性的，但格式严重影响可读性。分成 3-4 个带标题的子段（如 \"Constraint Scope\", \"Evaluation Coverage\", \"Scalability\"）会大幅改善。\n\n---\n\n## 总结\n\n与 R1 的 9 条 Weaknesses 中：\n- **[AGREE] 7 条**: W1, W2, W3 (部分), W4, W5, W7, W9\n- **[REBUT] 2 条**: W6 (应降为 Minor), W8 (编译层面不影响输出)\n\nR1 和 R2 独立发现了 3 个相同的核心问题：\n1. **Dual-factor 统计支撑不足** (R1-W1 = R2-W2)\n2. **WikiEvents fine-tuning 20 文档过小** (R1-W2 = R2-W5)\n3. **Abstract 数字表述可能误导** (R1-W4 ⊂ R2-W6)\n\n两位 reviewer 均给出 **3.5 (Borderline Conference)**，核心共识是：实验全面、执行扎实，但技术新颖性有限且关键 claims 的统计支撑不足。",
    "reviewer_id": "2",
    "project": "schema_semantic_constrained_ie"
  }
}
```

</details>

---


### Tool result

_source line 567 · 2026-05-19T06:33:20.069811+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_01fc90ae186a4ed432770f7601995139:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4523
}
```

</details>

---


### Assistant

_source line 568 · 2026-05-19T06:33:24.740968+00:00_

交叉回应已提交。与 R1 的 9 条 Weakness 中同意 7 条、反驳 2 条（W6 应降级为 Minor，W8 不影响编译输出）。两位 reviewer 独立发现了三个相同核心问题：dual-factor 统计支撑不足、WikiEvents 20 文档评估过小、Abstract 数字误导性。两位均给出 3.5 (Borderline Conference)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2"
}
```

</details>

---


## Round 14

## Round 14

84 recorded events


### User

_source line 569 · 2026-05-19T07:08:28.535883+00:00_

[Round 1 审稿请求]:
## Round 1 审稿任务 — Reviewer 2

**你的审查侧重：新颖性与贡献 + 写作质量 + 相关工作覆盖 + 格式合规**

### 论文信息
- **标题**: OntoCoDec: Type-Constrained Information Extraction via Compiled Ontology Constraints
- **目标 venue**: EMNLP 2026 (ARR May 2026 cycle)
- **截止日期**: 2026-05-25
- **论文路径**: `projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex`
- **论文目录**: `projects/schema_semantic_constrained_ie/artifacts/_project/paper/`

### Venue 格式要求
- Long paper: 8 页正文 + unlimited references + Limitations section（不计页数）
- 模板: ACL style (`\usepackage[review]{acl}`)
- 匿名规则: Double-blind
- 附录: double-column format
- 必须包含: Limitations section, Responsible NLP Research Checklist
- EMNLP 2026 评分标准: 5=Consider for Award, 4.5=Borderline Award, 4=Conference（主会议接收）, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit

### 你的审查重点

请按以下维度深入评估：

1. **新颖性与贡献评估**
   - 核心 idea（将 ontology 约束编译为 constrained decoding）的新颖程度
   - 相对于已有 constrained decoding 工作（如 grammar-constrained decoding, PICARD, SynCode 等）和 schema-aware IE 工作（如 GoLLIE, KnowCoder, CodeIE 等）的增量贡献是否足够
   - Contribution list 中每条 claim 是否成立、是否有过度宣传
   - 该工作对 NLP/IE 社区的实际影响力评估

2. **写作质量**
   - 叙事主线是否清晰一致（Abstract → Intro → Method → Results → Conclusion 是否讲同一个故事）
   - 是否存在 AI 写作痕迹（dash 滥用、-ing phrases、过度分段、formulaic transitions）
   - 专有名词/缩写是否都有定义
   - 数据呈现是否服务于叙事（vs 数据堆砌）
   - 图表的信息密度和可读性
   - Abstract 是否在 150-250 words 内回答四个核心问题

3. **相关工作覆盖**
   - 是否覆盖所有直接相关方法、baseline 论文、评测 benchmark 论文、理论基础
   - 定位是否清晰（本文相对已有工作的真实增量）
   - 是否有明显遗漏的重要工作
   - 引用数量是否达到 EMNLP 录用论文的一般水平

4. **格式合规**
   - 页数是否符合 8 页限制
   - 是否使用正确的 ACL review 模板
   - 匿名化是否完整（无作者信息泄露）
   - Limitations section 是否存在且有实质内容
   - Ethics Statement 是否存在
   - 参考文献格式是否一致
   - 附录是否 double-column

### 输出格式

请按 ACL/ARR 标准审稿格式输出：
- **Summary**: 2-3 句论文概述
- **Strengths**: 优点逐条列出（S1, S2, ...）
- **Weaknesses**: 缺点逐条列出（W1, W2, ...），区分 Must-Fix / Should-Fix / Minor
- **Questions**: 需要作者回答的问题（Q1, Q2, ...）
- **Missing References**: 遗漏的重要相关工作
- **Overall Assessment**: 评分（使用 EMNLP 2026 评分标准 1-5）+ 置信度（1-5）+ 简要理由
- **Detailed Comments**: 逐节详细意见（§1-§7 + Limitations + Appendix + 格式检查）

### 特别注意
- 用 grep 检查全文 em-dash（—）和 en-dash（–）使用情况
- 检查 -ing phrase 结尾模式
- 检查 Abstract word count
- 检查页数（编译 PDF 或估算）
- 检查 bib 文件的引用完整性和格式一致性

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 570 · 2026-05-19T07:08:37.743922+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 571 · 2026-05-19T07:08:38.046517+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/review_reviewer_2_cbe93d98.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 302
}
```

</details>

---


### Tool call

_source line 572 · 2026-05-19T07:08:38.047004+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 573 · 2026-05-19T07:08:38.952561+00:00_

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
12	\usepackage{multirow}
13	\usepackage{amsmath}
14	\usepackage{amssymb}
15	\usepackage{enumitem}
16	\usepackage{xcolor}
17	\usepackage{pifont}
18	
19	\title{OntoCoDec: Type-Constrained Information Extraction\\via Compiled Ontology Constraints}
20	
21	\author{Anonymous ACL submission}
22	
23	\begin{document}
24	\maketitle
25	
26	% === Abstract ===
27	\input{abstract}
28	
29	% === §1 Introduction ===
30	\input{section1_introduction_draft}
31	
32	% === §2 Background ===
33	\input{section2_background}
34	
35	% === §3 Method ===
36	\input{section3_method_draft}
37	
38	% === §4 Constraint Composition ===
39	\section{Constraint Composition}
40	\label{sec:composition}
41	\input{section4_composition_draft}
42	
43	% === §5 Experiments ===
44	\section{Experiments}
45	\label{sec:experiments}
46	
47	\input{section3_violation_landscape}
48	
49	\input{section5_scierc_draft}
50	\input{section5_docred_draft}
51	\input{section5_crossmodel_draft}
52	\input{section5_wikievents_draft}
53	\input{section5_runtime}
54	
55	% === §6 Related Work ===
56	\input{section6_related_work}
57	
58	% === §7 Discussion and Conclusion ===
59	\section{Discussion and Conclusion}
60	\label{sec:discussion}
61	\input{section7_conclusion_compressed}
62	
63	% === Limitations (ARR requirement: standalone section, does not count toward page limit) ===
64	\clearpage
65	\section*{Limitations}
66	
67	\paragraph{Constraint scope.}
68	CF impact is model-dependent: for well-calibrated models (Qwen, Llama), S1 introduces CF violations (up to 12.02\%) as a consequence of per-relation independent enforcement; for poorly-calibrated models (Mistral), S1 substantially reduces CF (56.87\%\,$\to$\,1.27\%) by constraining type assignments to schema-valid values.
69	CF fallback ablation sh
…[truncated 4385 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 905
}
```

</details>

---


### Tool call

_source line 574 · 2026-05-19T07:08:39.104356+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
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

_source line 575 · 2026-05-19T07:08:39.104884+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 576 · 2026-05-19T07:08:46.099329+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper"
  }
}
```

</details>

---


### Tool result

_source line 577 · 2026-05-19T07:08:46.501534+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft_4796e8.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract_fd4b26.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract_d3264e.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion_550cbf_DEPRECATED.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/discussion_paragraphs_cf83d1.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_relwork_additions.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/discussion_paragraphs.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_relwork_outline.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion_DEPRECATED.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/paper_tables_draft.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_prompts.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft_9b84f1.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/p3_case_studies.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/p3_case_studies_861a0d.tex
/home/ubuntu/.agent-ml-re
…[truncated 3453 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 578 · 2026-05-19T07:08:47.108440+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.bib",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper"
  }
}
```

</details>

---


### Tool result

_source line 579 · 2026-05-19T07:08:47.310541+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/new_citations.bib
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/relwork_new_entries.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 202
}
```

</details>

---


### Tool call

_source line 580 · 2026-05-19T07:08:47.310999+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool result

_source line 581 · 2026-05-19T07:08:55.062302+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"https://aclrollingreview.org/"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"}]

Based on the search results, here's information about ACL ARR 2026 reviewer guidelines and review form criteria:

## Reviewer Guidelines Overview

The workflow recommended includes: (1) read the paper and get the first impression, (2) search for relate
…[truncated 1373 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7751
}
```

</details>

---


### Tool call

_source line 582 · 2026-05-19T07:09:00.846897+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete ARR review form with all scoring dimensions, their scales, and descriptions. Include: Overall Assessment, Soundness, Excitement/Novelty, Reproducibility, and any other dimensions with their full scoring rubrics."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete ARR review form with all scoring dimensions, their scales, and descriptions. Include: Overall Assessment, Soundness, Excitement/Novelty, Reproducibility, and any other dimensions with their full scoring rubrics."
  }
}
```

</details>

---


### Tool call

_source line 583 · 2026-05-19T07:09:01.349773+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 584 · 2026-05-19T07:09:02.103575+00:00_

1	\begin{abstract}
2	We present \textsc{OntoCoDec}, which compiles Information Extraction (IE) ontology schemas into two composable token-level decoding constraints:
3	(1)~a \emph{grammar layer} (XGrammar) that guarantees JSON structural validity and vocabulary membership; and
4	(2)~a \emph{semantic layer} that enforces per-triple domain/range type constraints via a stateful entity registry and dynamic logit masking, with grammar-first fallback when constraints conflict.
5	Without constraints, Large Language Model (LLM) based IE produces systematic domain/range (DR) violations that persist even after fine-tuning; violation rates correlate with \emph{constraint tightness} rather than ontology or model scale.
6	Composed with Low-Rank Adaptation (LoRA), \textsc{OntoCoDec} reduces DR to $\leq$\,0.20\% with R-F1 within $\pm$0.6\,pp of unconstrained baselines: near-lossless composability at deployment-grade extraction quality.
7	% exp_ids: w5_lora_scierc_constrained_eval, w5_qwen_docred_lora_constrained_eval, w5_llama_lora_scierc_constrained_eval, w5_llama_docred_lora_constrained_eval
8	Under zero-shot decoding, DR drops by 76--99\% for calibrated models (Qwen3-8B, Llama-3.1-8B); Mistral-7B, a boundary condition, shows 42\% reduction.
9	Beam search ($k{=}4$) with LoRA eliminates all four violation types on SciERC (both Qwen3-8B and Llama-3.1-8B).
10	The framework generalizes to event extraction on WikiEvents (56 event types, 80 roles) without modification, eliminating vocabulary violations ($\to$\,0\%); fine-tuning composability extends to EE (preliminary, 20-document test set).
11	Per-slot enforcement introduces a cross-field consistency trade-off (resolved to $\leq$1.2\% by fine-tuning on both RE and EE).
12	OntoCoDec composes losslessly with standard fine-tuning across four models (8B--70B), three tokenizer families, and three IE tasks.
13	\end{abstract}
14	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 753
}
```

</details>

---


### Tool call

_source line 585 · 2026-05-19T07:09:02.255015+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section1_introduction_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section1_introduction_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 586 · 2026-05-19T07:09:02.607072+00:00_

1	% Section 1: Introduction (compressed, 669→~550 words)
2	
3	\section{Introduction}
4	\label{sec:introduction}
5	
6	Large language models are increasingly used for information extraction~\cite{li2023codeie,sainz2024gollie,wei2023zeroshot}, but when generating relation triples $(h, r, t)$, neither entity is guaranteed to carry a type consistent with the ontology's domain/range constraints for $r$.
7	We call such outputs \emph{domain/range violations}: structurally valid triples that are ontologically invalid.
8	Violations persist across the capability spectrum: 15.4\% of triples on SciERC~\cite{luan2018scierc} and 18.5\% on DocRED~\cite{yao2019docred} under zero-shot decoding, and 1--2\% even after LoRA fine-tuning; rates correlate with \emph{constraint tightness} (few valid type pairs per relation) rather than ontology or model scale.
9	Constraint enforcement matters most at deployment-grade quality (R-F1 40--46\%): at this level, residual type violations propagate directly into knowledge graphs and decision-support pipelines; reliable type-safety enforcement is needed.
10	
11	Existing approaches leave a fundamental gap.
12	Schema-informed prompting reduces violations by 62\% on average but is per-relation unreliable (violations for \textsc{Evaluate-for} actually \emph{increase} by 5.8\,pp).
13	Grammar-constrained decoding~\cite{dong2025xgrammar,willard2023outlines,beurer-kellner2023lmql} guarantees syntactic well-formedness but cannot encode cross-field semantic constraints.
14	Post-hoc filtering achieves higher F1 in most zero-shot settings via precision gains, but at the cost of discarding up to 48\% of predictions including true positives; at high rejection rates (e.g., Mistral DocRED 73.7\%), it discards the majority of outputs and becomes impractical.
15	OntoCoDec preserves recall by enforcing constraints during generation rather than discarding non-compliant outputs.
16	Training-based approaches~\cite{sainz2024gollie,lu2022uie} provide only soft guidance tha
…[truncated 2561 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 587 · 2026-05-19T07:09:02.607717+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section2_background.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section2_background.tex"
  }
}
```

</details>

---


### Tool result

_source line 588 · 2026-05-19T07:09:02.909544+00:00_

1	% Section 2: Background (compressed)
2	
3	\section{Background}
4	\label{sec:background}
5	
6	\paragraph{IE Ontology Structure.}
7	\label{sec:bg:ontology}
8	An IE ontology $\mathcal{O} = (\mathcal{E}, \mathcal{R}, \sigma)$ defines entity types $\mathcal{E}$, relation types $\mathcal{R}$, and a mapping $\sigma: \mathcal{R} \to \mathcal{P}(\mathcal{E} \times \mathcal{E})$ specifying valid (head type, tail type) pairs per relation.
9	A triple $(h, r, t)$ is \emph{type-valid} if $(\mathrm{type}(h), \mathrm{type}(t)) \in \sigma(r)$.
10	We define the \emph{constraint tightness} of $r$ as $1 - |\sigma(r)| / |\mathcal{E}|^2$: tighter constraints leave fewer valid options, increasing violation likelihood.
11	
12	\paragraph{Grammar-Constrained Decoding.}
13	\label{sec:bg:gcd}
14	Grammar-constrained decoding restricts each token $y_t$ to a mask $M_g \in \{0, 1\}^{|V|}$ derived from a target grammar.
15	XGrammar~\citep{dong2025xgrammar} compiles JSON Schemas into pushdown automata for efficient enforcement of structural constraints; Outlines~\citep{willard2023outlines} and SGLang~\citep{zheng2024sglang} offer similar capabilities.
16	However, these methods are limited to context-free constraints and cannot enforce cross-field semantic rules (e.g., ``if $r$ = \textsc{Feature-of}, then $\mathrm{type}(h) \in \{\textsc{Method}, \textsc{OtherScientificTerm}\}$''), which depend on previously generated field values.
17	
18	\paragraph{Problem Statement.}
19	\label{sec:bg:problem}
20	Given $\mathcal{O}$ and an autoregressive LM $\mathcal{M}$, we seek constraints $\mathcal{C}$ ensuring: (a)~\textbf{structural validity}, i.e., well-formed JSON with $\mathcal{E}$/$\mathcal{R}$ membership; and (b)~\textbf{type validity}, i.e., $(\mathrm{type}(h), \mathrm{type}(t)) \in \sigma(r)$ for every triple.
21	Condition (a) is context-free; (b) is context-sensitive but \emph{prefix-decidable}: at the point where a type token is generated, all information needed (relation type, entity registry) is ava
…[truncated 149 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 589 · 2026-05-19T07:09:02.909978+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_method_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_method_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 590 · 2026-05-19T07:09:02.960562+00:00_

1	% Section 3 — Method (Draft)
2	% OntoCoDec: Type-Valid Information Extraction
3	% via Compiled Ontology Constraints
4	
5	\section{Method}
6	\label{sec:method}
7	
8	We present OntoCoDec, a two-layer constrained decoding framework that compiles ontology schemas into token-level masks enforced during autoregressive generation.
9	Unlike type-constrained code generation, IE presents three distinct challenges: (1)~entity types are inferred from free text rather than declared annotations, (2)~the entity registry is built dynamically during generation, and (3)~constraint targets are context-dependent type assignments rather than fixed grammar productions.
10	The grammar layer (\S\ref{sec:grammar}) guarantees structural validity (well-formed JSON with ontology-vocabulary membership), while the semantic layer (\S\ref{sec:semantic}) enforces domain/range type constraints via a stateful entity registry.
11	We describe the problem formulation (\S\ref{sec:formulation}), each layer, and two decoding strategies (\S\ref{sec:strategies}).
12	Formal analysis of constraint composition is deferred to Section~\ref{sec:composition}.
13	
14	
15	\subsection{Problem Formulation}
16	\label{sec:formulation}
17	
18	\paragraph{IE as structured generation.}
19	Given an input text $x$, a language model generates a structured JSON output $y$:
20	%
21	\begin{equation}\label{eq:output-schema}
22	\resizebox{.88\columnwidth}{!}{$\displaystyle
23	  y = \bigl\{\texttt{entities}: [\{n_i, \tau_i\}],\; \texttt{relations}: [\{h_j, t_j, r_j, \tau^h_j, \tau^t_j\}]\bigr\}
24	$}
25	\end{equation}
26	%
27	where each entity has a name $n_i$ and type $\tau_i \in \mathcal{E}$, and each relation specifies head $h_j$, tail $t_j$, relation type $r_j \in \mathcal{R}$, and head/tail entity types $\tau^h_j, \tau^t_j$.
28	The output JSON Schema (\S\ref{sec:grammar}) enforces a fixed field ordering (head $\to$ tail $\to$ relation $\to$ head\_type $\to$ tail\_type) via deterministic grammar compilation.
29	This ordering en
…[truncated 6610 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 591 · 2026-05-19T07:09:09.496021+00:00_

# ACL Rolling Review Form – Complete Scoring Dimensions

## 1. **Reviewer Confidence**
Scale: 1–5
- **5**: "Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work."
- **4**: Quite sure; unlikely but conceivable to miss important details
- **3**: Pretty sure; possibly missed details in math or experimental design
- **2**: Willing to defend evaluation; fairly likely missed details or novelty assessment
- **1**: "Not my area, or paper is very hard to understand"

## 2. **Soundness**
Scale: 1–5 (with half-point increments)
- **5**: "Excellent: This study is one of the most thorough I have seen"
- **4**: Strong; sufficient support with room for optional extra experiments
- **3**: Acceptable; supports main claims with minor gaps
- **2**: Poor; main claims lack sufficient support; major technical issues
- **1**: "Major Issues: This study is not yet sufficiently thorough to warrant publication"

## 3. **Excitement**
Scale: 1–5 (with half-point increments)
Evaluates subjective interest through conceptual breakthroughs, challenging assumptions, community impact, and personal relevance.
- **5**: "Highly Exciting: I would recommend this paper to others and/or attend its presentation"
- **4**: Would mention to others; effort to attend presentation
- **3**: Might mention points; attend if time permits
- **2**: "Potentially Interesting: does not resonate with me, but it might with others"
- **1**: Not relevant to computational linguistics community

## 4. **Overall Assessment**
Scale: 1–5 (with half-point increments)
- **5**: "Consider for Award" (top 2.5%)
- **4**: Conference acceptance recommended
- **3**: "Findings" track acceptance
- **2**: "Resubmit next cycle" (needs substantial revisions)
- **1**: "Do not resubmit" or not relevant to field

## 5. **Reproducibility**
Scale: 1–5
- **5**: "They could easily reproduce the results"
- **4**: Mostly reproducible; minor variations possible
- **3**: Reproducible with difficulty; und
…[truncated 964 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 8649
}
```

</details>

---


### Tool call

_source line 592 · 2026-05-19T07:09:15.385078+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section4_composition_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section4_composition_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 593 · 2026-05-19T07:09:15.737459+00:00_

1	% Section: Constraint Composition (compressed, 787→~500 words)
2	
3	At each decoding step $t$, let $G(t) \subseteq V$ and $S(t) \subseteq V$ denote the tokens permitted by the grammar and semantic layers, respectively.
4	The final mask is their conjunction:
5	%
6	\begin{equation}\label{eq:composition}
7	  M_{\text{final}}(t) = M_{\text{grammar}}(t) \;\wedge\; M_{\text{semantic}}(t),
8	\end{equation}
9	%
10	so a token is allowed only if it satisfies \emph{both} structural and type-level constraints.
11	The conjunction is asymmetric: $S(t)$ is defined only over $G(t)$. This reflects the enabling dependency (\S\ref{sec:method}): the semantic layer requires the relation type to belong to $\mathcal{R}$, a property guaranteed only by the grammar layer.
12	
13	\paragraph{Grammar-First Fallback.}
14	When $S(t) \cap G(t) = \emptyset$ (tight constraints leave no token that is both grammar-valid and semantically valid), na\"{\i}ve masking would force selection of a grammar-invalid token, breaking JSON structure.
15	We enforce a \emph{grammar-first fallback}: if no semantically valid token survives grammar filtering, semantic masking is skipped and the grammar layer alone controls selection.
16	Structural integrity is a hard constraint; a type violation is a soft error detectable by downstream validation.
17	Among type violations, DR and CF differ in severity: a DR violation renders the triple ontologically invalid (the entity type lies outside the relation's domain or range), whereas a CF violation means each triple is individually schema-valid but the same entity receives different type assignments across triples.
18	
19	\paragraph{Constraint Tightness.}
20	We define the tightness of relation $r$ as:
21	%
22	\begin{equation}\label{eq:tightness}
23	  \kappa(r) = 1 - \frac{|\mathcal{V}(r)|}{|\mathcal{E}|^2},
24	\end{equation}
25	%
26	where $\mathcal{V}(r)$ is the set of valid type pairs and $\mathcal{E}$ the entity type vocabulary.
27	The mean tightness $\bar{\kappa} = \frac{
…[truncated 1385 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 594 · 2026-05-19T07:09:15.788773+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_violation_landscape.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_violation_landscape.tex"
  }
}
```

</details>

---


### Tool result

_source line 595 · 2026-05-19T07:09:16.442296+00:00_

1	% §5 Setup (compressed from Violation Landscape)
2	% exp_ids: mvp_phase0_violation_rate, mvp_phase0_scierc_schema,
3	%          mvp_phase0_violation_rate_docred, mvp_phase0_docred_schema
4	
5	\label{sec:violation_landscape}
6	
7	We evaluate OntoCoDec in two complementary regimes.
8	Fine-tuning composability (\S\ref{sec:composability}) tests whether constraints compose losslessly with standard training at deployment-grade quality (R-F1 40--46).
9	Zero-shot evaluation stress-tests constraint robustness when the model has no task-specific supervision (R-F1 2--8).
10	
11	\paragraph{Setup.}
12	We evaluate on SciERC~\cite{luan2018scierc} (551 test sentences, 7 relations, $\bar{\kappa}{=}0.333$) and DocRED~\cite{yao2019docred} (998 dev documents,\footnote{DocRED test annotations are not publicly available; we evaluate on the development set.} 96 relations, $\bar{\kappa}{=}0.842$).
13	RE type constraints are extracted automatically from observed type pairs in training data (neither dataset provides a formal ontology); EE constraints on WikiEvents (\S\ref{sec:wikievents}) are derived from the KAIROS ontology.
14	The framework handles both sources without modification.
15	Primary model: Qwen3-8B~\cite{qwen2025qwen3}, zero-shot greedy decoding; cross-model validation in \S\ref{sec:cross-model}, composability with fine-tuning in \S\ref{sec:composability}.
16	We measure four violation categories: \textbf{DR} (domain/range type pair $\notin \sigma(r)$), \textbf{RV} (relation $\notin \mathcal{R}$), \textbf{ET} (entity type $\notin \mathcal{E}$), and \textbf{CF} (same entity assigned conflicting types across triples).
17	Baseline DR violations are 15.37\% (SciERC) and 18.46\% (DocRED), comparable rates associated with constraint tightness rather than ontology scale (\S\ref{sec:introduction}); schema-informed prompting reduces DR by 62\% on SciERC but is per-relation unreliable (Appendix~\ref{app:per-relation-landscape}).
18	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 653
}
```

</details>

---


### Tool call

_source line 596 · 2026-05-19T07:09:16.442822+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 597 · 2026-05-19T07:09:16.845183+00:00_

1	% Section 5 — SciERC Results (Draft)
2	% Data source: Phase 2 SciERC registry experiments
3	% exp_ids: phase2_scierc_unconstrained, phase2_scierc_grammar_only,
4	%          phase2_scierc_semantic_only, phase2_scierc_full_s1, phase2_scierc_full_s2
5	% All numbers verified against registry 2026-05-14.
6	
7	\subsection{Ablation and Composability with Fine-Tuning}
8	\label{sec:scierc-results}
9	
10	Table~\ref{tab:scierc-ablation} presents the five-way ablation on SciERC (Qwen3-8B, zero-shot, 551 documents); only the active constraint layers differ across rows.
11	
12	% ──────────────────────────────────────────
13	%  Table: SciERC five-way ablation
14	% ──────────────────────────────────────────
15	\begin{table}[t]
16	\centering
17	\small
18	\setlength{\tabcolsep}{3.6pt}
19	\resizebox{\columnwidth}{!}{%
20	\begin{tabular}{@{}l rrrrrr rr@{}}
21	\toprule
22	& \multicolumn{6}{c}{\textbf{Violation Rates (\%)}}
23	& \multicolumn{2}{c}{\textbf{F1}} \\
24	\cmidrule(lr){2-7} \cmidrule(l){8-9}
25	\textbf{Mode}
26	  & DR\,$\downarrow$ & $\Delta$DR
27	  & RV\,$\downarrow$ & ET\,$\downarrow$ & CF & Tot.\,$\downarrow$
28	  & Rel.\,$\uparrow$ & Ent.\,$\uparrow$ \\
29	\midrule
30	Unconstrained
31	  & 15.37 & ---
32	  & 1.39  & 0.40
33	  & 0.08  & 15.45
34	  & 8.23  & 31.01 \\
35	Grammar
36	  & 14.84 & $\downarrow$3\%
37	  & \textbf{0} & \textbf{0}
38	  & 0.08  & 14.92
39	  & 8.23  & 30.98 \\
40	Semantic
41	  & 11.65 & $\downarrow$24\%
42	  & 1.51  & 0.40
43	  & 2.71  & 14.36
44	  & 8.15  & 31.01 \\
45	Full (S1)
46	  & \textbf{0.93} & $\downarrow$\textbf{94\%}
47	  & \textbf{0} & \textbf{0}
48	  & 9.90  & \textbf{10.83}
49	  & \textbf{8.36} & 30.98 \\
50	Full (S2)
51	  & 0.97  & $\downarrow$94\%
52	  & \textbf{0} & \textbf{0}
53	  & 8.03  & \textbf{9.00}
54	  & 8.03  & \textbf{31.90} \\
55	\bottomrule
56	\end{tabular}}%
57	\caption{Five-way ablation on SciERC (551 docs, Qwen3-8B, zero-shot).
58	$\Delta$DR: relative change vs.\ unconstrained.
59	Tot.\ = DR + CF (total type-violation b
…[truncated 5095 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 598 · 2026-05-19T07:09:16.845718+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 599 · 2026-05-19T07:09:17.599865+00:00_

1	% Section 5 — DocRED Results (compressed, 1450→~600 words)
2	% exp_ids: phase2_docred_unconstrained, phase2_docred_grammar_only,
3	%          phase2_docred_semantic_only, phase2_docred_full_s1
4	% All numbers verified against registry 2026-05-14.
5	
6	\subsection{Cross-Dataset Validation on DocRED}
7	\label{sec:docred-results}
8	
9	Table~\ref{tab:docred-ablation} presents the four-way ablation on DocRED (96 Wikidata relation types, 14$\times$ SciERC; Qwen3-8B, zero-shot, 998 documents).
10	
11	% ──────────────────────────────────────────
12	%  Table: DocRED four-way ablation
13	% ──────────────────────────────────────────
14	\begin{table}[t]
15	\centering
16	\small
17	\setlength{\tabcolsep}{3.6pt}
18	\resizebox{\columnwidth}{!}{%
19	\begin{tabular}{@{}l rrrrrr rr@{}}
20	\toprule
21	& \multicolumn{6}{c}{\textbf{Violation Rates (\%)}}
22	& \multicolumn{2}{c}{\textbf{F1}} \\
23	\cmidrule(lr){2-7} \cmidrule(l){8-9}
24	\textbf{Mode}
25	  & DR\,$\downarrow$ & $\Delta$DR
26	  & RV\,$\downarrow$ & ET\,$\downarrow$ & CF & Tot.\,$\downarrow$
27	  & Rel.\,$\uparrow$ & Ent.\,$\uparrow$ \\
28	\midrule
29	Unconstrained
30	  & 18.46 & ---
31	  & 29.66 & 2.48
32	  & 0.10  & 18.56
33	  & 7.74  & 58.15 \\
34	Grammar
35	  & 26.17 & $\uparrow$42\%
36	  & \textbf{0.03} & \textbf{0}
37	  & 0.07  & 26.24
38	  & \textbf{8.31}  & \textbf{59.38} \\
39	Semantic
40	  & 13.84 & $\downarrow$25\%
41	  & 29.87 & 4.22
42	  & 1.05  & 14.89
43	  & 7.70  & 57.81 \\
44	Full (S1)
45	  & \textbf{10.21} & $\downarrow$\textbf{45\%}
46	  & \textbf{0.03} & \textbf{0}
47	  & 2.57  & \textbf{12.78}
48	  & 8.23  & 59.37 \\
49	\bottomrule
50	\end{tabular}}%
51	\caption{Four-way ablation on DocRED (998 documents, Qwen3-8B, zero-shot).
52	$\Delta$DR: relative change vs.\ unconstrained.
53	Tot.\ = DR + CF (total type-violation burden).
54	Best per column in \textbf{bold} (CF excluded; Tot.\ included).
55	F1 $\times$100. Bootstrap significance: R-F1 $+$0.50\,pp ($p < 0.001$).}
56	\label{tab:docred-ablation}
57	\en
…[truncated 1553 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 754
}
```

</details>

---


### Tool call

_source line 600 · 2026-05-19T07:09:17.600355+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_crossmodel_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_crossmodel_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 601 · 2026-05-19T07:09:17.651039+00:00_

1	% Section 5 — Cross-Model Validation (compressed, 830→~400 words)
2	% exp_ids: phase2_scierc_unconstrained, phase2_scierc_full_s1,
3	%          phase2_docred_unconstrained, phase2_docred_full_s1,
4	%          llama_scierc_unconstrained, llama_scierc_full_s1,
5	%          llama_docred_unconstrained, llama_docred_full_s1
6	
7	\subsection{Cross-Model Validation}
8	\label{sec:cross-model}
9	
10	Table~\ref{tab:cross-model} replicates S1 with Llama-3.1-8B and Mistral-7B under identical prompts.
11	
12	\begin{table}[t]
13	\centering
14	\small
15	\setlength{\tabcolsep}{3.4pt}
16	\resizebox{\columnwidth}{!}{%
17	\begin{tabular}{@{}ll rrrr r@{}}
18	\toprule
19	& & \multicolumn{4}{c}{\textbf{Violation Rates (\%)}}
20	& \textbf{R-F1} \\
21	\cmidrule(lr){3-6} \cmidrule(l){7-7}
22	\textbf{Dataset} & \textbf{Model}
23	  & DR\,$\downarrow$ & RV\,$\downarrow$ & ET\,$\downarrow$ & CF
24	  & $\uparrow$ \\
25	\midrule
26	\multirow{6}{*}{SciERC}
27	  & Qwen (U)    & 15.37 & 1.39  & 0.40 & 0.08 & 8.23 \\
28	  & Qwen (S1)   &  0.93 & 0     & 0    & 9.90 & 8.36 \\
29	  \cmidrule(l){2-7}
30	  & Llama (U)   & 13.34 & 0.55  & 0    & 0.24 & 2.68 \\
31	  & Llama (S1)  &  0.08 & 0     & 0    & 6.56 & 2.54 \\
32	  \cmidrule(l){2-7}
33	  & Mistral (U) & 56.94 & 0     & 1.50 & 56.87$^\dagger$ & 3.66 \\
34	  & Mistral (S1)& 13.40 & 0     & 0    & 1.27  & 3.67 \\
35	\midrule
36	\multirow{6}{*}{DocRED}
37	  & Qwen (U)    & 18.46 & 29.66 & 2.48 & 0.10 & 7.74 \\
38	  & Qwen (S1)   & 10.21 &  0.03 & 0    & 2.57 & 8.23 \\
39	  \cmidrule(l){2-7}
40	  & Llama (U)   & 26.07 & 16.03 & 0.13 & 0.17 & 5.98 \\
41	  & Llama (S1)  &  2.55 &  0    & 0    & 12.02& 6.27 \\
42	  \cmidrule(l){2-7}
43	  & Mistral (U) & 57.42 & 42.35 & 7.58 & 24.78 & 4.34 \\
44	  & Mistral (S1)& 33.20 &  0    & 0    & 0.19  & 5.52 \\
45	\bottomrule
46	\end{tabular}}%
47	\caption{Three-model zero-shot validation. U: unconstrained; S1: full two-layer.
48	Parse failures: Llama DocRED 9.1\%; others $\leq$1.1\%.
49	$^\dagger$Mistral: poor ze
…[truncated 799 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 602 · 2026-05-19T07:09:23.730474+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_wikievents_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_wikievents_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 603 · 2026-05-19T07:09:24.132988+00:00_

1	% Section 5 — Event Extraction on WikiEvents (compact, inline)
2	% exp_ids: ee_qwen_wikievents_unconstrained, ee_llama_wikievents_unconstrained,
3	%          ee_mistral_wikievents_unconstrained, ee_qwen_wikievents_constrained,
4	%          ee_llama_wikievents_constrained, ee_mistral_wikievents_constrained_v2
5	% v3 final data confirmed by Director 2026-05-18.
6	
7	\subsection{Cross-Task Validation: Event Extraction}
8	\label{sec:wikievents}
9	
10	We apply OntoCoDec to event extraction (EE) on WikiEvents~\cite{li2021document} (56 event types, 80 roles, 27 entity types, 245 constraints; Appendix~\ref{app:wikievents}) without modification.
11	Violations extend to EV (event vocabulary), RoV (role vocabulary), and AC (argument constraint, analogous to DR).
12	
13	% ──────────────────────────────────────────
14	%  Table: WikiEvents three-model comparison (v3 final)
15	%  exp_ids: ee_{qwen,llama,mistral}_wikievents_{unconstrained,grammar_only,constrained_v3}
16	% ──────────────────────────────────────────
17	\begin{table}[t]
18	\centering
19	\small
20	\setlength{\tabcolsep}{2.8pt}
21	\resizebox{\columnwidth}{!}{%
22	\begin{tabular}{@{}ll rrrr rr@{}}
23	\toprule
24	& & \multicolumn{4}{c}{\textbf{Violation Rates (\%)}}
25	& \multicolumn{2}{c}{\textbf{F1}} \\
26	\cmidrule(lr){3-6} \cmidrule(l){7-8}
27	\textbf{Model} & \textbf{Mode}
28	  & EV\,$\downarrow$ & RoV\,$\downarrow$ & AC & CF
29	  & Trig.\,$\uparrow$ & Ent.\,$\uparrow$ \\
30	\midrule
31	\multirow{3}{*}{Qwen3-8B}
32	  & Unconstr.\ & 24.0 & 74.9 & 0.3 & 0 & 11.8 & 0 \\
33	  & Grammar    & \textbf{0} & 76.1 & 8.2 & --- & --- & --- \\
34	  & Full S1    & \textbf{0} & \textbf{0} & 2.1 & 21.1 & 13.4 & 14.1 \\
35	\midrule
36	\multirow{3}{*}{\shortstack[l]{Llama\\3.1-8B}}
37	  & Unconstr.\ & 10.5 & 88.8 & 0.1 & 0 & 5.7 & 0 \\
38	  & Grammar    & \textbf{0} & 77.0 & 8.8 & --- & --- & --- \\
39	  & Full S1    & \textbf{0} & \textbf{0} & 3.8 & 17.2 & 7.5 & 17.6 \\
40	\midrule
41	\multirow{3}{*}{\shortstack[l]{Mistral\\7B}}
42
…[truncated 2360 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 604 · 2026-05-19T07:09:24.133468+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_runtime.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_runtime.tex"
  }
}
```

</details>

---


### Tool result

_source line 605 · 2026-05-19T07:09:24.284317+00:00_

1	% Runtime overhead (inline paragraph, no subsection header to save space)
2	
3	\paragraph{Runtime overhead.}
4	\label{sec:runtime}
5	S1 overhead is $+$13.1\% on SciERC and $+$2.43\% on DocRED (amortized over longer sequences); under LoRA, $+$10.0\% with 37\% lower absolute latency.
6	Grammar compile: one-time 44\,ms (Appendix~\ref{app:runtime}).
7	Scaling benchmarks confirm constant overhead (2--3\%) up to 200 entity types and 1{,}000 relations (Appendix~\ref{app:scalability}).
8	
9	\paragraph{Beam search compatibility.}
10	\label{sec:beam-results}
11	Under greedy S1, the grammar-first fallback resolves DR$\leftrightarrow$CF conflicts one token at a time; beam search ($k{=}4$) explores paths that satisfy both layers jointly and reduces DR and CF simultaneously.
12	With LoRA, beam S1 eliminates all four violation types on SciERC for both Qwen and Llama (R-F1 44.23, 46.11; Table~\ref{tab:beam-search}).
13	Under zero-shot, beam reduces DR to 0\% for calibrated models (Qwen, Llama) and CF substantially (9.90\%\,$\to$\,0.53\% Qwen; 6.56\%\,$\to$\,0.93\% Llama); Mistral remains a boundary condition (DR 7.99\%, CF 1.27\%) due to high baseline violations (Appendix~\ref{app:beam-search}).
14	Total latency overhead is 1.54$\times$ (beam 1.32$\times$ $+$ constraint 1.17$\times$; Table~\ref{tab:beam-latency}).
15	
16	% exp_ids: 70b_scierc_unconstrained, 70b_scierc_constrained, 70b_docred_unconstrained, 70b_docred_constrained
17	\paragraph{Cross-scale generalizability.}
18	\label{sec:70b-results}
19	On Llama-3.1-70B (AWQ INT4), OntoCoDec achieves DR$\to$0\% on SciERC (R-F1 $-$0.03\,pp) and \textbf{0\%} across ET, RV, and DR on the full DocRED 998-document set (R-F1 $+$0.04\,pp), the only configuration to completely eliminate DR on DocRED.
20	CF rises to 7.01\% (from 0.07\%); the low baseline reflects under-measurement (malformed outputs bypass the checker), while constrained decoding exposes more triples to the consistency check (\S\ref{sec:discussion}).
21	Model scale reduces
…[truncated 39 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 606 · 2026-05-19T07:09:24.586781+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 607 · 2026-05-19T07:09:25.189648+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	We provide a detailed survey in Appendix~\ref{app:related_work}; here we position OntoCoDec.
5	Grammar-constrained decoding~\cite{dong2025xgrammar,willard2023outlines,beurer-kellner2023lmql,ugare2024syncode,park2024grammar,beurer-kellner2024domino,jsonschemabench2025} guarantees format validity but cannot enforce cross-field semantic constraints; type-constrained code generation~\cite{synchromesh_iclr2022,scholak2021picard,pldi2025_type_constrained_codegen} compiles type systems into token-level masks but operates on static type declarations, whereas IE requires a dynamic entity registry built during generation.
6	Vocabulary-constrained IE methods~\cite{geng2023gcd,sainz2024gollie,josifoski2022genie,guidex2025,vukovic2024dore,boostcd2025} restrict which tokens can appear but not which type combinations are valid per relation; EnriCo~\cite{zaratiana2024enrico} enforces structural constraints via ASP but requires supervised training and hand-crafted rules; IterGen~\cite{ugare2025itergen} supports semantic constraints via backtracking but requires manual implementation per constraint.
7	Training-based methods~\cite{paolini2021tanl,cabot2021rebel,lu2022uie,knowcoder_acl2024,li2023codeie,schema_rl2025} provide soft guidance; post-hoc approaches~\cite{khorshidi2025odke,spires_2024,ontologx_2025,slot2025} validate outputs after generation.
8	OntoCoDec prevents violations during decoding, is training-free, and compiles constraints automatically from ontology schemas.
9	\citet{roth_yih_2004} first introduced hard type constraints in IE via integer linear programming for global inference; OntoCoDec achieves analogous type enforcement within autoregressive decoding.
10	Schema-aware training methods~\cite{sainz2024gollie,knowcoder_acl2024} internalize type constraints via training; OntoCoDec enforces them at decoding time without retraining, and the two approaches are complementary.
11	Recent work shows constrained decodi
…[truncated 283 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 602
}
```

</details>

---


### Tool call

_source line 608 · 2026-05-19T07:09:25.190097+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion_compressed.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion_compressed.tex"
  }
}
```

</details>

---


### Tool result

_source line 609 · 2026-05-19T07:09:25.240573+00:00_

1	% Section 7 — Discussion and Conclusion (maximally compressed)
2	% Full discussion in Appendix; Mistral boundary condition in app:dual-factor.
3	
4	OntoCoDec compiles IE ontology schemas into composable token-level decoding constraints that compose losslessly with standard fine-tuning across both RE and EE: DR reaches $\leq$\,0.20\% with R-F1 within $\pm$0.6\,pp on RE (R-F1 40--46), RoV$\to$0\% and AC$\leq$0.8\% on EE, and beam search ($k{=}4$) eliminates all four RE violation types under fine-tuned decoding for calibrated models (\S\ref{sec:beam-results}).
5	Under zero-shot decoding, which stress-tests constraint robustness at R-F1 2--8\%, DR drops by 42--99\% across three models $\times$ three datasets with no significant F1 cost; constraint effectiveness holds across the full quality spectrum.
6	CF remains an open challenge for per-slot enforcement; global entity-level type consensus during decoding offers the most direct resolution path.
7	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 610 · 2026-05-19T07:09:37.409399+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "—",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
  "glob": "*.tex",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "—",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
    "glob": "*.tex",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---


### Tool result

_source line 611 · 2026-05-19T07:09:37.911873+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft_9b84f1.tex:1:% Section 5 — DocRED Results (Draft)
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft_4796e8.tex:1:% Section 5 — SciERC Results (Draft)
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/paper_tables_draft.tex:2:% Paper Tables Draft — Schema-Semantic Constrained IE
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/paper_tables_draft.tex:78:% Table 3: DocRED Phase 0 — Prompt-level Intervention
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_wikievents_draft.tex:1:% Section 5 — Event Extraction on WikiEvents (compact, inline)
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft.tex:1:% Section 5 — DocRED Results (compressed, 1450→~600 words)
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion_compressed.tex:1:% Section 7 — Discussion and Conclusion (maximally compressed)
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_case_studies.tex:1:% Appendix — Error Analysis and Case Studies
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion_DEPRECATED.tex:1:% Section 7 — Conclusion
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_llama_per_relation.tex:1:% Appendix C — Per-Relation Violation Analysis (Llama-3.1-8B)
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projec
…[truncated 1632 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 612 · 2026-05-19T07:09:38.417111+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": " – ",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
  "glob": "*.tex",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": " – ",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
    "glob": "*.tex",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---


### Tool result

_source line 613 · 2026-05-19T07:09:38.870110+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 614 · 2026-05-19T07:09:40.276795+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "ing,|ing\\.|ing;|ing\\s+",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
  "glob": "*.tex",
  "output_mode": "count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "ing,|ing\\.|ing;|ing\\s+",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
    "glob": "*.tex",
    "output_mode": "count"
  }
}
```

</details>

---


### Tool result

_source line 615 · 2026-05-19T07:09:40.779620+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_sampling_table.tex:6
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/discussion_paragraphs_cf83d1.tex:8
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft_9b84f1.tex:22
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/p3_case_studies_861a0d.tex:9
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section1_introduction_draft.tex:12
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section2_background.tex:4
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex:14
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_full_ft.tex:4
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_doc_length.tex:2
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_reproducibility.tex:7
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_prompts.tex:3
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_related_work.tex:70
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_crossmodel_draft.tex:1
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_method_draft.tex:27
/home/ubuntu/.agent-ml
…[truncated 3451 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 616 · 2026-05-19T07:09:41.232347+00:00_

called mcp__agent-ml-research__verify_references

<details open><summary>🔧 Tool call — mcp__agent-ml-research__verify_references</summary>

```json
{
  "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
  "project": "schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__verify_references",
  "tool_args": {
    "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
    "project": "schema_semantic_constrained_ie"
  }
}
```

</details>

---


### Tool call

_source line 617 · 2026-05-19T07:09:43.241372+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper && cat abstract.tex | sed 's/\\\\[a-zA-Z]*{[^}]*}//g; s/\\\\[a-zA-Z]*//g; s/[{}%~$]//g; s/\\\\,//g' | wc -w",
  "description": "Count words in abstract"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper && cat abstract.tex | sed 's/\\\\[a-zA-Z]*{[^}]*}//g; s/\\\\[a-zA-Z]*//g; s/[{}%~$]//g; s/\\\\,//g' | wc -w",
    "description": "Count words in abstract"
  }
}
```

</details>

---


### Tool result

_source line 618 · 2026-05-19T07:10:47.513964+00:00_

&lt;persisted-output>
Output too large (53.3KB). Full output saved to: /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie--claude-sessions-review-reviewer-2-cbe93d98/d0e11d99-ef9c-4bcb-b747-b66260360e25/tool-results/toolu_017gJr1fsAdH1DCuMECefY5A.txt

Preview (first 2KB):
{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 64, \"total_citations\": 97, \"unique_cited_keys\": 55, \"orphan_bib\": 8, \"missing_bib\": 0, \"duplicate_keys\": 1, \"online_verified\": 48, \"online_not_found\": 4, \"online_mismatch\": 11}, \"cross_check\": {\"orphan_bib\": [\"delafuente2025guidex\", \"geng2025jsonschemabench\", \"lee2026formattax\", \"lu2025schemarl\", \"park2024grammaraligned\", \"reddy2026dccd\", \"sakota2025boostcd\", \"shen2025slot\"], \"missing_bib\": [], \"orphan_count\": 8, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"synchromesh_iclr2022\", \"type\": \"inproceedings\", \"title\": \"Synchromesh: Reliable Code Generation from Pre-trained Language Models\", \"authors\": \"Poesia, Gabriel and Polozov, Oleksandr and Le, Vu and Tiwari, Ashish and Soares,...\", \"year\": \"2022\", \"venue\": \"International Conference on Learning Representations\"}, {\"key\": \"mgd_neurips2023\", \"type\": \"inproceedings\", \"title\": \"Monitor-Guided Decoding of Code LMs with Static Analysis of Repository Context\", \"authors\": \"Agrawal, Lakshya A. and Kanade, Aditya and Goyal, Navin and Lahiri, Shuvendu K. ...\", \"year\": \"2023\", \"venue\": \"Advances in Neural Information Processing Systems\"}, {\"key\": \"pldi2025_type_constrained_codegen\", \"type\": \"article\", \"title\": \"Type-Constrained Code Generation with Language Models\", \"authors\": \"M\\\\\\\"undler, Niels and He, Jingxuan and Wang, Hao and Sen, Koushik and Song, Dawn ...\", \"year\": \"2025\", \"venue\": \"Proceedings of the ACM on Programming Languages\"}, {\"key\": \"roth_yih_2004\", \"type\": \"inproceeding
…[truncated 371 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__verify_references",
  "elapsed_ms": 66281
}
```

</details>

---


### Tool result

_source line 619 · 2026-05-19T07:10:47.667229+00:00_

201
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/review_reviewer_2_cbe93d98

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Bash",
  "elapsed_ms": 64425
}
```

</details>

---


### Tool call

_source line 620 · 2026-05-19T07:10:55.459535+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie--claude-sessions-review-reviewer-2-cbe93d98/d0e11d99-ef9c-4bcb-b747-b66260360e25/tool-results/toolu_017gJr1fsAdH1DCuMECefY5A.txt",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie--claude-sessions-review-reviewer-2-cbe93d98/d0e11d99-ef9c-4bcb-b747-b66260360e25/tool-results/toolu_017gJr1fsAdH1DCuMECefY5A.txt",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 621 · 2026-05-19T07:10:56.415086+00:00_

1	{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 64, \"total_citations\": 97, \"unique_cited_keys\": 55, \"orphan_bib\": 8, \"missing_bib\": 0, \"duplicate_keys\": 1, \"online_verified\": 48, \"online_not_found\": 4, \"online_mismatch\": 11}, \"cross_check\": {\"orphan_bib\": [\"delafuente2025guidex\", \"geng2025jsonschemabench\", \"lee2026formattax\", \"lu2025schemarl\", \"park2024grammaraligned\", \"reddy2026dccd\", \"sakota2025boostcd\", \"shen2025slot\"], \"missing_bib\": [], \"orphan_count\": 8, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"synchromesh_iclr2022\", \"type\": \"inproceedings\", \"title\": \"Synchromesh: Reliable Code Generation from Pre-trained Language Models\", \"authors\": \"Poesia, Gabriel and Polozov, Oleksandr and Le, Vu and Tiwari, Ashish and Soares,...\", \"year\": \"2022\", \"venue\": \"International Conference on Learning Representations\"}, {\"key\": \"mgd_neurips2023\", \"type\": \"inproceedings\", \"title\": \"Monitor-Guided Decoding of Code LMs with Static Analysis of Repository Context\", \"authors\": \"Agrawal, Lakshya A. and Kanade, Aditya and Goyal, Navin and Lahiri, Shuvendu K. ...\", \"year\": \"2023\", \"venue\": \"Advances in Neural Information Processing Systems\"}, {\"key\": \"pldi2025_type_constrained_codegen\", \"type\": \"article\", \"title\": \"Type-Constrained Code Generation with Language Models\", \"authors\": \"M\\\\\\\"undler, Niels and He, Jingxuan and Wang, Hao and Sen, Koushik and Song, Dawn ...\", \"year\": \"2025\", \"venue\": \"Proceedings of the ACM on Programming Languages\"}, {\"key\": \"roth_yih_2004\", \"type\": \"inproceedings\", \"title\": \"A Linear Programming Formulation for Global Inference in Natural Language Tasks\", \"authors\": \"Roth, Dan and Yih, Wen-tau\", \"year\": \"2004\", \"venue\": \"Proceedings of the Eighth Conference on Computational Natural Language Learning ...\"}, {\"key\": \"adakgc_emnlp2023\", \"type\": \"inproceedings\", \"title\": \"Sche
…[truncated 52597 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 955
}
```

</details>

---


### Tool call

_source line 622 · 2026-05-19T07:10:56.415590+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 623 · 2026-05-19T07:10:57.320281+00:00_

1	\section{Extended Related Work}
2	\label{app:related_work}
3	
4	% ===========================================================================
5	% Paradigm 1: Grammar-Constrained Decoding
6	% ===========================================================================
7	\paragraph{Grammar-Constrained Decoding.}
8	Recent work has established efficient algorithms for restricting LLM outputs to conform to context-free grammars, making grammar-constrained decoding the de facto standard for obtaining structured output from language models.
9	XGrammar~\cite{dong2025xgrammar} partitions the vocabulary into context-independent and context-dependent tokens and maintains persistent pushdown automata across decoding steps, achieving up to 100$\times$ speedup over prior CFG-constrained decoding methods.
10	Outlines~\cite{willard2023outlines} reformulates constrained generation as finite-state machine transitions with offline vocabulary indexing, which enables efficient enforcement of regular-expression and JSON-schema constraints without runtime overhead per token.
11	LMQL~\cite{beurer-kellner2023lmql} introduces a declarative query language that compiles type, length, and regex constraints into token-level masks, providing a programmable interface for specifying multi-variable output structures.
12	These systems ensure that every generated token belongs to a grammar-valid continuation, but they do not address the \emph{distribution distortion} introduced by naive token masking.
13	A parallel line of work tackles this problem directly: DOMINO~\cite{beurer-kellner2024domino} minimizes distributional divergence during CFG enforcement by formulating mask selection as an optimization problem, and ASAp~\cite{park2024grammar} provides a provably unbiased sampling algorithm that preserves the original LM distribution under grammar constraints.
14	Together, these advances have made grammar-constrained decoding both fast and statistically principled, and provide a robust foundation for 
…[truncated 19750 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 904
}
```

</details>

---


### Tool call

_source line 624 · 2026-05-19T07:11:01.350318+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": ", highlighting| demonstrating| enabling| leveraging| facilitating| showcasing| suggesting| indicating| confirming",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
  "glob": "*.tex",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": ", highlighting| demonstrating| enabling| leveraging| facilitating| showcasing| suggesting| indicating| confirming",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
    "glob": "*.tex",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---


### Tool result

_source line 625 · 2026-05-19T07:11:01.501523+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft_9b84f1.tex:147:replicating the enabling dependency observed on SciERC:
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft_9b84f1.tex:154:that the grammar$\to$semantic enabling dependency is a general
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft_9b84f1.tex:179:for the model to redirect probability mass toward, enabling
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_related_work.tex:110:The two constraint layers, grammar (structural) and semantic (relational), compose via bitwise AND with an enabling dependency: the grammar layer ensures every generated type token belongs to the valid vocabulary, which enables the semantic layer to look up and enforce domain/range rules for that type.
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion_550cbf_DEPRECATED.tex:16:The grammar layer serves as an enabling prerequisite for the semantic layer; the two compose via bitwise AND over candidate token sets.
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion_550cbf_DEPRECATED.tex:26:The grammar layer alone does not elevate CF (0.08\%, matching the unconstrained baseline), confirming that CF is entirely attributable to the semantic layer. % exp_id: phase2_scierc_grammar_only
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex:36:This metric directly quantifies the enabling dependency (\S\ref{sec:interaction}): it measures the fraction of decoding steps where both 
…[truncated 4286 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 626 · 2026-05-19T07:11:15.703229+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper && which pdflatex && pdflatex -interaction=nonstopmode main.tex 2>&1 | tail -20",
  "description": "Compile LaTeX paper to check page count",
  "timeout": "60000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper && which pdflatex && pdflatex -interaction=nonstopmode main.tex 2>&1 | tail -20",
    "description": "Compile LaTeX paper to check page count",
    "timeout": "60000"
  }
}
```

</details>

---


### Tool call

_source line 627 · 2026-05-19T07:11:15.703808+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool call

_source line 628 · 2026-05-19T07:11:16.356820+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_reproducibility.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_reproducibility.tex"
  }
}
```

</details>

---


### Tool result

_source line 629 · 2026-05-19T07:11:17.314510+00:00_

/usr/bin/pdflatex
nts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty
pe1/public/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub
lic/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams
fonts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/c
m/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.
pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/us
r/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/share/
texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texliv
e/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy6.pfb>&lt;/usr/share/texlive/texmf
-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/f
onts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty
pe1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub
lic/amsfonts/symbols/msbm10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/
courier/ucrr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/helvetic/uhvb
8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/sh
are/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/tex
mf-dist/fonts/type1/urw/times/utmri8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/
type1/urw/zapfding/uzdr.pfb>
Output written on main.pdf (28 pages, 447595 bytes).
Transcript written on main.log.
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/review_reviewer_2_cbe93d98

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Bash",
  "elapsed_ms": 1611
}
```

</details>

---


### Tool result

_source line 630 · 2026-05-19T07:11:17.365353+00:00_

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
26	The two-layer architecture produces two distinct fallback mechanisms with different semant
…[truncated 8640 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1661
}
```

</details>

---


### Tool result

_source line 631 · 2026-05-19T07:11:17.365944+00:00_

1	\section{Reproducibility Details}
2	\label{app:reproducibility}
3	
4	\paragraph{Fine-tuning configuration.}
5	All four fine-tuned models (Qwen3-8B and Llama-3.1-8B-Instruct on SciERC and DocRED) use identical LoRA hyperparameters: rank $r{=}16$, $\alpha{=}32$, dropout $0.05$, no bias, targeting all attention and MLP projection layers (\texttt{q\_proj}, \texttt{k\_proj}, \texttt{v\_proj}, \texttt{o\_proj}, \texttt{gate\_proj}, \texttt{up\_proj}, \texttt{down\_proj}).
6	Training uses AdamW with learning rate $2{\times}10^{-4}$, cosine schedule, warmup ratio $0.1$, effective batch size $16$, bf16 precision, gradient checkpointing, and completion-only loss for 3 epochs.
7	SciERC trains on 1,762 examples (260 dev) for 333 steps; DocRED trains on 3,053 examples (998 dev) for 573 steps.
8	Maximum sequence length is 2,048 (SciERC) and 4,096 (DocRED).
9	All runs use seed 42.
10	
11	\paragraph{Hardware and software.}
12	Training runs on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (98\,GB VRAM).
13	SciERC fine-tuning takes approximately 11 minutes per model; DocRED takes approximately 1.5 hours.
14	Software versions: PyTorch 2.10, Transformers 4.57, PEFT 0.19, TRL 1.1, Accelerate 1.13.
15	
16	\paragraph{Inference time.}
17	Inference timing is reported in Appendix~\ref{app:runtime} (NVIDIA RTX PRO 6000 Blackwell Server Edition GPU, same hardware as training).
18	Full S1 constrained decoding adds $+$13.1\% wall-clock overhead on SciERC and $+$2.43\% on DocRED (Qwen3-8B, zero-shot greedy); under LoRA fine-tuning, overhead is $+$10.0\% on SciERC.
19	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1009
}
```

</details>

---


### Tool call

_source line 632 · 2026-05-19T07:11:24.942873+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.pdf",
  "pages": "7-10",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.pdf",
    "pages": "7-10",
    "dpi": "150"
  }
}
```

</details>

---


### Tool call

_source line 633 · 2026-05-19T07:11:25.746302+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex",
  "offset": "100",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex",
    "offset": "100",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 634 · 2026-05-19T07:11:26.325439+00:00_

Error: result (2,520,767 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie--claude-sessions-review-reviewer-2-cbe93d98/d0e11d99-ef9c-4bcb-b747-b66260360e25/tool-results/mcp-agent-ml-research-pdf_to_images-1779174686237.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie--claude-sessions-review-reviewer-2-cbe93d98/d0e11d99-ef9c-4bcb-b747-b66260360e25/tool-results/mcp-agent-ml-research-pdf_to_images-1779174686237.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1382
}
```

</details>

---


### Tool result

_source line 635 · 2026-05-19T07:11:26.326330+00:00_

100	\centering
101	\includegraphics[width=0.75\columnwidth]{figures/dual_factor_scatter.pdf}
102	\caption{Residual DR vs.\ $\bar{\kappa} \times \text{RV}_{\text{baseline}}$ across four model$\times$dataset configurations.
103	Linear fit (calibrated models): $y = 0.366x - 0.138$, $R^2 = 0.886$; Mistral deviates due to entity misclassification.}
104	\label{fig:dual-factor-scatter}
105	\end{figure}
106	
107	%%% Dataset-Dependent F1 Impact (moved from §7) %%%
108	% exp_ids: d012_bootstrap_ci (DocRED +0.50pp p<0.001, SciERC +0.13pp p=0.58),
109	%          phase0_docred_unconstrained (RV=29.66%), phase0_scierc_unconstrained (RV=1.39%)
110	
111	\paragraph{Dataset-Dependent F1 Impact.}
112	The divergence in F1 significance between DocRED ($+$0.50\,pp, $p < 0.001$) and SciERC ($+$0.13\,pp, $p = 0.58$) traces to a single mechanism: grammar-layer elimination of out-of-vocabulary relation names.
113	DocRED's baseline RV of 29.66\% produces 5{,}189 OOV predictions counted as false positives; eliminating them yields a significant precision gain.
114	SciERC's baseline RV is only 1.39\% (24 OOV predictions), too few to produce a detectable F1 effect.
115	Llama-3.1-8B's lower baseline RV (16.03\%) yields a smaller but directionally consistent improvement ($+$0.29\,pp vs.\ $+$0.50\,pp); F1 gain magnitude is proportional to baseline OOV rate.
116	% exp_ids: phase0_docred_unconstrained, phase0_scierc_unconstrained
117	% exp_ids: llama_docred_unconstrained (RV=16.03%), llama_docred_full_s1 (R-F1 delta=+0.29pp)
118	
119	%%% Paragraph 1: Low F1 Practical Significance %%%
120	% exp_ids: phase2_scierc_full_s1 (R-F1=8.36%), phase2_docred_full_s1 (R-F1=8.23%),
121	%          phase0_scierc_unconstrained (DR=15.37%), phase2_docred_unconstrained (DR=18.46%)
122	
123	\paragraph{Practical Significance of Zero-Shot F1.}
124	Our reported relation F1 of approximately 8\% on both SciERC and DocRED reflects the inherent difficulty of zero-shot closed IE, where the model receives no task-specific traini
…[truncated 5968 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 580
}
```

</details>

---


### Tool call

_source line 636 · 2026-05-19T07:11:31.757504+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.pdf",
  "pages": "8",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.pdf",
    "pages": "8",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 637 · 2026-05-19T07:11:32.109648+00:00_

Error: result (151,569 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie--claude-sessions-review-reviewer-2-cbe93d98/d0e11d99-ef9c-4bcb-b747-b66260360e25/tool-results/mcp-agent-ml-research-pdf_to_images-1779174692077.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie--claude-sessions-review-reviewer-2-cbe93d98/d0e11d99-ef9c-4bcb-b747-b66260360e25/tool-results/mcp-agent-ml-research-pdf_to_images-1779174692077.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 638 · 2026-05-19T07:11:38.393864+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper && grep -E \"clearpage|\\\\\\\\section|\\\\\\\\appendix\" main.log 2>/dev/null | head -30 ; echo \"---\" ; grep \"Output written\" main.log ; echo \"---\" ; grep -c \"\\\\[\" main.log ; echo \"---\" ; grep \"\\\\[8\\\\]\\\\|\\\\[9\\\\]\\\\|\\\\[10\\\\]\" main.log | head -10",
  "description": "Check page boundaries from LaTeX log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper && grep -E \"clearpage|\\\\\\\\section|\\\\\\\\appendix\" main.log 2>/dev/null | head -30 ; echo \"---\" ; grep \"Output written\" main.log ; echo \"---\" ; grep -c \"\\\\[\" main.log ; echo \"---\" ; grep \"\\\\[8\\\\]\\\\|\\\\[9\\\\]\\\\|\\\\[10\\\\]\" main.log | head -10",
    "description": "Check page boundaries from LaTeX log"
  }
}
```

</details>

---


### Tool result

_source line 639 · 2026-05-19T07:11:38.494887+00:00_

---
Output written on main.pdf (28 pages, 447595 bytes).
---
177
---
[10]
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/review_reviewer_2_cbe93d98

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Bash",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 640 · 2026-05-19T07:11:41.761096+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper && grep -n \"\\\\[\" main.log | grep -E \"^\\d+:\\[\" | head -30",
  "description": "Find page markers in LaTeX log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper && grep -n \"\\\\[\" main.log | grep -E \"^\\d+:\\[\" | head -30",
    "description": "Find page markers in LaTeX log"
  }
}
```

</details>

---


### Tool result

_source line 641 · 2026-05-19T07:11:41.862083+00:00_

Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/review_reviewer_2_cbe93d98

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 642 · 2026-05-19T07:11:45.079989+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper && grep -oP '\\[\\d+\\]' main.log | sort -t'[' -k1 -n | uniq",
  "description": "Extract page numbers from LaTeX log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper && grep -oP '\\[\\d+\\]' main.log | sort -t'[' -k1 -n | uniq",
    "description": "Extract page numbers from LaTeX log"
  }
}
```

</details>

---


### Tool result

_source line 643 · 2026-05-19T07:11:45.183912+00:00_

[10]
[11]
[12]
[13]
[14]
[15]
[16]
[17]
[18]
[20]
[21]
[23]
[24]
[25]
[26]
[27]
[2]
[3]
[4]
[5]
[6]
[7]
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/review_reviewer_2_cbe93d98

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Bash",
  "elapsed_ms": 103
}
```

</details>

---


### Tool call

_source line 644 · 2026-05-19T07:11:50.079755+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper && python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdftotext', 'main.pdf', '-'], capture_output=True, text=True)\npages = result.stdout.split('\\f')\nfor i, page in enumerate(pages[:15], 1):\n    # Find section headers\n    lines = [l.strip() for l in page.split('\\n') if l.strip()]\n    first_lines = lines[:5] if lines else []\n    print(f'Page {i}: {first_lines[:3]}')\n\" 2>&1",
  "description": "Extract page content headers"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper && python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdftotext', 'main.pdf', '-'], capture_output=True, text=True)\npages = result.stdout.split('\\f')\nfor i, page in enumerate(pages[:15], 1):\n    # Find section headers\n    lines = [l.strip() for l in page.split('\\n') if l.strip()]\n    first_lines = lines[:5] if lines else []\n    print(f'Page {i}: {first_lines[:3]}')\n\" 2>&1",
    "description": "Extract page content headers"
  }
}
```

</details>

---


### Tool result

_source line 645 · 2026-05-19T07:11:50.504794+00:00_

Page 1: ['OntoCoDec: Type-Constrained Information Extraction', 'via Compiled Ontology Constraints', 'Anonymous ACL submission']
Page 2: ['085', '086', '087']
Page 3: ['181', '3.1', '182']
Page 4: ['272', '273', '274']
Page 5: ['Violation Rates (%)', 'Mode', 'DR ↓']
Page 6: ['Violation Rates (%)', 'Mode', 'DR ↓']
Page 7: ['482', '483', '484']
Page 8: ['582', '7', '583']
Page 9: ['599', 'Limitations', '600']
Page 10: ['700', '701', '702']
Page 11: ['812', '813', '814']
Page 12: ['922', '923', '924']
Page 13: ['SciERC — System Prompt (Unconstrained & Constrained)', 'You are an expert information extraction system for scientific texts.', 'entities and relations from the given text.']
Page 14: ['1068', '1069', '1070']
Page 15: ['1170', '1171', '1172']
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/review_reviewer_2_cbe93d98

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Bash",
  "elapsed_ms": 425
}
```

</details>

---


### Tool call

_source line 646 · 2026-05-19T07:12:54.303011+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "checklist|Checklist|responsible|Responsible",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
  "glob": "*.tex",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "checklist|Checklist|responsible|Responsible",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
    "glob": "*.tex",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---


### Tool result

_source line 647 · 2026-05-19T07:12:56.914621+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 2611
}
```

</details>

---


### Tool call

_source line 648 · 2026-05-19T07:12:57.065728+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper && python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdftotext', 'main.pdf', '-'], capture_output=True, text=True)\npages = result.stdout.split('\\f')\n# Check page 8-9 content to confirm main body ends at page 8\nfor i in [7, 8, 9]:  # 0-indexed\n    if i < len(pages):\n        lines = [l.strip() for l in pages[i].split('\\n') if l.strip()]\n        print(f'=== Page {i+1} ===')\n        for l in lines[:15]:\n            print(l)\n        print('...')\n        print()\n\" 2>&1",
  "description": "Check main body end page content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper && python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdftotext', 'main.pdf', '-'], capture_output=True, text=True)\npages = result.stdout.split('\\f')\n# Check page 8-9 content to confirm main body ends at page 8\nfor i in [7, 8, 9]:  # 0-indexed\n    if i < len(pages):\n        lines = [l.strip() for l in pages[i].split('\\n') if l.strip()]\n        print(f'=== Page {i+1} ===')\n        for l in lines[:15]:\n            print(l)\n        print('...')\n        print()\n\" 2>&1",
    "description": "Check main body end page content"
  }
}
```

</details>

---


### Tool result

_source line 649 · 2026-05-19T07:12:57.419325+00:00_

=== Page 8 ===
582
7
583
OntoCoDec compiles IE ontology schemas into
composable token-level decoding constraints that
compose losslessly with standard fine-tuning across
both RE and EE: DR reaches ≤ 0.20% with R-F1
within ±0.6 pp on RE (R-F1 40–46), RoV→0%
and AC≤0.8% on EE, and beam search (k=4) eliminates all four RE violation types under fine-tuned
decoding for calibrated models (§5.4). Under zeroshot decoding, which stress-tests constraint robustness at R-F1 2–8%, DR drops by 42–99% across
three models × three datasets with no significant F1
cost; constraint effectiveness holds across the full
quality spectrum. CF remains an open challenge
for per-slot enforcement; global entity-level type
consensus during decoding offers the most direct
...

=== Page 9 ===
599
Limitations
600
Constraint scope. CF impact is modeldependent: for well-calibrated models (Qwen,
Llama), S1 introduces CF violations (up to
12.02%) as a consequence of per-relation independent enforcement; for poorly-calibrated
models (Mistral), S1 substantially reduces CF
(56.87% → 1.27%) by constraining type assignments to schema-valid values. CF fallback ablation
shows that eliminating CF re-routes violations
to DR (+13.85 pp). CF↔DR thus represents a
fundamental trade-off in composable constraint
systems rather than an independently resolvable
limitation (Appendix C). Global entity-level type
consensus during decoding offers the most direct
path to resolving CF violations. CF type inconsistencies may propagate to downstream tasks that
...

=== Page 10 ===
700
701
702
703
704
Luca Beurer-Kellner, Marc Fischer, and Martin Vechev.
2024. Guiding LLMs the right way: Fast, noninvasive constrained generation. In Proceedings of
the 41st International Conference on Machine Learning (ICML), volume 235 of PMLR, pages 3658–3673.
705
706
707
708
709
710
711
...
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/review_reviewer_2_cbe93d98

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Bash",
  "elapsed_ms": 353
}
```

</details>

---


### Tool call

_source line 650 · 2026-05-19T07:15:54.449929+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 — Round 1 完整审稿意见\n\n**论文**: OntoCoDec: Type-Constrained Information Extraction via Compiled Ontology Constraints\n**审查侧重**: 新颖性与贡献 + 写作质量 + 相关工作覆盖 + 格式合规\n\n---\n\n## 总体评分\n**Overall**: 3.0 (Findings)\n**Confidence**: 4/5\n**一句话总结**: 技术执行扎实、实验覆盖充分，但核心新颖性为已有范式的工程组合，CF trade-off 未解决，限制了实际贡献深度。\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 双层约束设计技术合理，ablation 充分；但 CF trade-off 在 zero-shot 下将总违规率仅从 15.45% 降至 10.83%（SciERC），\"near-lossless\" claim 需更多限定 |\n| Excitement | 2.5/5 | 将 grammar-constrained decoding 从语法扩展到语义对 IE 社区有实用价值，但核心技术是 XGrammar + stateful logit processor 的工程组合，缺乏范式级突破 |\n| Reproducibility | 4/5 | 详细超参数、硬件、seed，承诺开源；代码当前不可获取 |\n\n---\n\n## Must-Fix 问题\n\n**N1** [critical] CF trade-off 与 \"near-lossless composability\" claim 不一致\n- 位置：Abstract L6, §1 Contribution 3, §7 结论第一句\n- Abstract 声称 \"near-lossless composability\" 但仅报告 DR 下降，忽略 CF 从 0→9.90%（SciERC zero-shot）甚至 12.02%（Llama DocRED）。SciERC 上 total type-violation burden（DR+CF）从 15.45% 降至 10.83%，即总违规仅减少约 30%，而非 Abstract 暗示的 94%。\"near-lossless\" 在 zero-shot 场景下不成立。\n- 建议：区分 zero-shot 与 fine-tuned 场景，\"near-lossless\" 仅限定于 fine-tuned 场景，Abstract 中提及 CF trade-off。\n\n**N2** [critical] WikiEvents 评估过于初步但在 Abstract/Contributions 中占较大权重\n- 位置：Abstract L10-11, §1 Contribution 3, §5.5\n- 仅 20 个测试文档的 fine-tuning composability 评估，论文自称 \"preliminary\"，但 Abstract 和 Contribution 中将 EE 结果与 RE 并列呈现。Trigger F1 波动 -5.4pp，confidence interval 极宽。\n- 建议：Abstract 中明确标注 EE 结果为 preliminary，降低在 Contribution list 中的权重。\n\n**N3** [critical] 缺少 Responsible NLP Research Checklist\n- 全文搜索 \"checklist\"/\"Responsible\" 均无结果。ARR 2026 要求该 checklist，缺失可能导致 desk reject。\n\n---\n\n## Should-Fix 问题\n\n**W1** Related Work 主体过于压缩（§6 仅 12 行正文，一个段落）\n- 30+ 篇引用压缩成连续 citation cluster。虽然 Appendix A 有详细 survey，但审稿人评估正文质量。\n- 建议：扩展为 2-3 段，分别覆盖 grammar-constrained decoding、schema-aware IE、post-hoc validation。\n\n**W2** Abstract 数据密度过高\n- 201 词含约 15 个数字/百分比、7 个缩写。Beam search 和 WikiEvents 细节不应出现在 Abstract 中。\n\n**W3** Contribution 3 信息过载\n- 单条 contribution 包含 5+ 个独立 claim（composability, CF↔DR trade-off, zero-shot robustness, WikiEvents EE, beam search），应拆分。\n\n**W4** Dual-factor pattern 统计支撑不足\n- 仅 n=4 数据点，p≈0.058（>0.05），排除 Mistral。主文表述可能让读者误认为 confirmed finding。\n\n**W5** DocRED grammar-only DR 增加（18.46%→26.17%）解释不充分\n- 反直觉结果仅一句话解释。\n\n**W6** §7 Discussion and Conclusion 过于简短（6 行正文，1 段）\n\n---\n\n## 小问题\n\n- Bib 有 8 个 orphan entries（重复 key）和 1 个 duplicate key（schall2025hiddencost）\n- 3 篇引用在 OpenAlex 中未找到完全匹配（regino2025kgcurator, vukovic2024dore, formattax2026）\n- Constraint tightness 在 §2 和 §4 重复定义\n- Table 1 caption 含不必要的 claim\n\n## Questions\n\nQ1: CF↔DR Pareto 前沿是否意味着 per-slot enforcement 框架内无法同时降低两者？有理论论证吗？\nQ2: Qwen LoRA DR=0% vs Llama LoRA DR=0.09% 是否统计显著？\nQ3: 从 training data 提取的 constraint table coverage gap 对 DR 和 F1 的影响有多大？\nQ4: Mistral 排除在 dual-factor 分析外但保留在 cross-model validation 中，适用范围如何框定？\nQ5: Beam search + LoRA 消除所有 violation 的结果在 DocRED 上是否成立？\n\n## Missing References\n\n1. InstructUIE (Wang et al., 2023) - instruction-tuned IE\n2. UniversalNER (Zhou et al., 2024) - universal NER with LLMs\n3. Wadhwa et al. (2023) \"Revisiting Relation Extraction in the era of LLMs\"\n4. DeepStruct (Wang et al., 2022)\n5. BioREx (Luo et al., 2022)\n\n## 主要优势\n\nS1: 问题定义清晰有价值，用具体数字量化了 DR violation 问题规模\nS2: 实验覆盖面广（3 模型 × 3 数据集 × 2 regime + ablation + beam search + runtime + scalability）\nS3: CF trade-off 诚实讨论（fallback ablation, CF distribution, Pareto 前沿）\nS4: 跨 tokenizer 通用设计（continuation masking, 三个 tokenizer family 验证）\nS5: Composability with fine-tuning 有部署实际意义\n\n## 格式检查结果\n\n- ✅ \\usepackage[review]{acl}\n- ✅ 匿名化完整\n- ✅ 主体 8 页\n- ✅ Limitations section 存在且有实质内容\n- ✅ Ethics Statement 存在\n- ❌ Responsible NLP Research Checklist 缺失\n- ✅ Abstract ~201 词\n- ✅ 无 em-dash/en-dash 滥用\n- ⚠️ Bib 有 orphan/duplicate entries",
  "reviewer_id": "2",
  "project": "schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 — Round 1 完整审稿意见\n\n**论文**: OntoCoDec: Type-Constrained Information Extraction via Compiled Ontology Constraints\n**审查侧重**: 新颖性与贡献 + 写作质量 + 相关工作覆盖 + 格式合规\n\n---\n\n## 总体评分\n**Overall**: 3.0 (Findings)\n**Confidence**: 4/5\n**一句话总结**: 技术执行扎实、实验覆盖充分，但核心新颖性为已有范式的工程组合，CF trade-off 未解决，限制了实际贡献深度。\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 双层约束设计技术合理，ablation 充分；但 CF trade-off 在 zero-shot 下将总违规率仅从 15.45% 降至 10.83%（SciERC），\"near-lossless\" claim 需更多限定 |\n| Excitement | 2.5/5 | 将 grammar-constrained decoding 从语法扩展到语义对 IE 社区有实用价值，但核心技术是 XGrammar + stateful logit processor 的工程组合，缺乏范式级突破 |\n| Reproducibility | 4/5 | 详细超参数、硬件、seed，承诺开源；代码当前不可获取 |\n\n---\n\n## Must-Fix 问题\n\n**N1** [critical] CF trade-off 与 \"near-lossless composability\" claim 不一致\n- 位置：Abstract L6, §1 Contribution 3, §7 结论第一句\n- Abstract 声称 \"near-lossless composability\" 但仅报告 DR 下降，忽略 CF 从 0→9.90%（SciERC zero-shot）甚至 12.02%（Llama DocRED）。SciERC 上 total type-violation burden（DR+CF）从 15.45% 降至 10.83%，即总违规仅减少约 30%，而非 Abstract 暗示的 94%。\"near-lossless\" 在 zero-shot 场景下不成立。\n- 建议：区分 zero-shot 与 fine-tuned 场景，\"near-lossless\" 仅限定于 fine-tuned 场景，Abstract 中提及 CF trade-off。\n\n**N2** [critical] WikiEvents 评估过于初步但在 Abstract/Contributions 中占较大权重\n- 位置：Abstract L10-11, §1 Contribution 3, §5.5\n- 仅 20 个测试文档的 fine-tuning composability 评估，论文自称 \"preliminary\"，但 Abstract 和 Contribution 中将 EE 结果与 RE 并列呈现。Trigger F1 波动 -5.4pp，confidence interval 极宽。\n- 建议：Abstract 中明确标注 EE 结果为 preliminary，降低在 Contribution list 中的权重。\n\n**N3** [critical] 缺少 Responsible NLP Research Checklist\n- 全文搜索 \"checklist\"/\"Responsible\" 均无结果。ARR 2026 要求该 checklist，缺失可能导致 desk reject。\n\n---\n\n## Should-Fix 问题\n\n**W1** Related Work 主体过于压缩（§6 仅 12 行正文，一个段落）\n- 30+ 篇引用压缩成连续 citation cluster。虽然 Appendix A 有详细 survey，但审稿人评估正文质量。\n- 建议：扩展为 2-3 段，分别覆盖 grammar-constrained decoding、schema-aware IE、post-hoc validation。\n\n**W2** Abstract 数据密度过高\n- 201 词含约 15 个数字/百分比、7 个缩写。Beam search 和 WikiEvents 细节不应出现在 Abstract 中。\n\n**W3** Contribution 3 信息过载\n- 单条 contribution 包含 5+ 个独立 claim（composability, CF↔DR trade-off, zero-shot robustness, WikiEvents EE, beam search），应拆分。\n\n**W4** Dual-factor pattern 统计支撑不足\n- 仅 n=4 数据点，p≈0.058（>0.05），排除 Mistral。主文表述可能让读者误认为 confirmed finding。\n\n**W5** DocRED grammar-only DR 增加（18.46%→26.17%）解释不充分\n- 反直觉结果仅一句话解释。\n\n**W6** §7 Discussion and Conclusion 过于简短（6 行正文，1 段）\n\n---\n\n## 小问题\n\n- Bib 有 8 个 orphan entries（重复 key）和 1 个 duplicate key（schall2025hiddencost）\n- 3 篇引用在 OpenAlex 中未找到完全匹配（regino2025kgcurator, vukovic2024dore, formattax2026）\n- Constraint tightness 在 §2 和 §4 重复定义\n- Table 1 caption 含不必要的 claim\n\n## Questions\n\nQ1: CF↔DR Pareto 前沿是否意味着 per-slot enforcement 框架内无法同时降低两者？有理论论证吗？\nQ2: Qwen LoRA DR=0% vs Llama LoRA DR=0.09% 是否统计显著？\nQ3: 从 training data 提取的 constraint table coverage gap 对 DR 和 F1 的影响有多大？\nQ4: Mistral 排除在 dual-factor 分析外但保留在 cross-model validation 中，适用范围如何框定？\nQ5: Beam search + LoRA 消除所有 violation 的结果在 DocRED 上是否成立？\n\n## Missing References\n\n1. InstructUIE (Wang et al., 2023) - instruction-tuned IE\n2. UniversalNER (Zhou et al., 2024) - universal NER with LLMs\n3. Wadhwa et al. (2023) \"Revisiting Relation Extraction in the era of LLMs\"\n4. DeepStruct (Wang et al., 2022)\n5. BioREx (Luo et al., 2022)\n\n## 主要优势\n\nS1: 问题定义清晰有价值，用具体数字量化了 DR violation 问题规模\nS2: 实验覆盖面广（3 模型 × 3 数据集 × 2 regime + ablation + beam search + runtime + scalability）\nS3: CF trade-off 诚实讨论（fallback ablation, CF distribution, Pareto 前沿）\nS4: 跨 tokenizer 通用设计（continuation masking, 三个 tokenizer family 验证）\nS5: Composability with fine-tuning 有部署实际意义\n\n## 格式检查结果\n\n- ✅ \\usepackage[review]{acl}\n- ✅ 匿名化完整\n- ✅ 主体 8 页\n- ✅ Limitations section 存在且有实质内容\n- ✅ Ethics Statement 存在\n- ❌ Responsible NLP Research Checklist 缺失\n- ✅ Abstract ~201 词\n- ✅ 无 em-dash/en-dash 滥用\n- ⚠️ Bib 有 orphan/duplicate entries",
    "reviewer_id": "2",
    "project": "schema_semantic_constrained_ie"
  }
}
```

</details>

---


### Tool result

_source line 651 · 2026-05-19T07:15:58.518015+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_01fc90ae186a4ed432770f7601995139:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4068
}
```

</details>

---


### Assistant

_source line 652 · 2026-05-19T07:16:07.576566+00:00_

审稿完成，已通过 `review_reviewer_post_to_director` 提交给 Review Director。

**审稿结果摘要**：
- **Overall**: 3.0 (Findings) / Confidence 4/5
- **3 个 Must-Fix**：(1) "near-lossless" claim 与 CF trade-off 不一致，(2) WikiEvents 评估过于初步但 claim 权重过高，(3) 缺少 Responsible NLP Research Checklist
- **6 个 Should-Fix**：Related Work 压缩、Abstract 数据密度、Contribution 3 过载、dual-factor 统计不足、DocRED grammar-only DR 增加解释不充分、Conclusion 过短
- **5 个优势**：问题定义清晰、实验覆盖广、CF trade-off 诚实讨论、跨 tokenizer 通用性、composability 实用价值

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2"
}
```

</details>

---


## Round 15

## Round 15

14 recorded events


### User

_source line 653 · 2026-05-19T07:16:43.697308+00:00_

[Round 1 审稿请求]:
## Step 2 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见

以下是 Reviewer 1 的完整审稿原文。请逐条回应：对每个 Weakness/Question，标注 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

### Reviewer 1 的 Must-Fix 问题

**W1 [critical] Constraint table 来源于训练数据，非形式本体，与标题/framing 不符。**
- 论文标题为 "Compiled Ontology Constraints"，但 SciERC/DocRED 的约束表从训练集共现统计提取，非正式本体。导致：约束表不完整（33% 残留 violation 源于 coverage gaps）；约束质量取决于训练集统计；未报告覆盖率。只有 WikiEvents 用了真正的形式本体（KAIROS），但结果 "preliminary"。

**W2 [critical] CF 副作用严重且为结构性问题，削弱核心贡献。**
- OntoCoDec 解决 DR 的同时引入 CF（zero-shot 下达 12.02-21.1%）。CF fallback ablation 证实结构性：消除 CF 则 DR +13.85pp。Total violation burden 仅降 30%，远不如 "94% DR reduction" 暗示的效果。Fine-tuning 将 CF 降至 ~1%，但与 "training-free" 定位有张力。

**W3 [warning] 缺少关键 baseline 对比。**
- 缺 GoLLIE、EnriCo、GCD 实验对比。Post-hoc filtering 在 5/6 zero-shot settings 下 F1 更高。

**W4 [warning] 多个关键实验的样本量不足。**
- Dual-factor n=4 p≈0.058；DocRED sampling 114/998 docs；WikiEvents FT 20 docs；Beam DocRED 50 docs。

**W5 [warning] Zero-shot R-F1 过低（2-8%），violation rate 分析指导意义有限。**
- 叙事重心放 zero-shot（§5.1-5.3 占 ~60%），但 F1 几乎无法正确抽取。

**W6 [warning] Mistral 结果显著弱，"boundary condition" 定义不充分。**
- Mistral SciERC 仅 42% DR reduction。ET>5% 排除准则是 post-hoc 且无理论依据。

**W7 [warning] 未评估下游影响。**
- Introduction 以 KG/pipeline violation propagation 为动机，但无任何下游评估。

### Reviewer 1 的 Minor 问题

**M1.** Table 2 caption "DR ≤ 0.09%" 但 DocRED 数据不在表中。
**M2.** §3.2 logit $-\infty$ 的 numerical stability 未讨论。
**M3.** Appendix B fuzzy matching threshold 无 justification。
**M4.** §4 LaTeX 源码残留内部 artifact 路径注释。
**M5.** Grammar layer DocRED RV 残留 0.03%（XGrammar edge case）。

### Reviewer 1 的 Questions

**Q1.** Constraint table 对 test set 的覆盖率是多少？unseen type pairs 会被错误标记为 DR violation 吗？
**Q2.** CF 对下游 KG construction 的影响？
**Q3.** OntoCoDec 相对 post-hoc filtering 的实际优势在哪？
**Q4.** Beam search 为什么不是默认推荐配置？
**Q5.** Sequential masking 的固定字段顺序是否限制 prompt 灵活性？

### Reviewer 1 的 Missing References
InstructUIE, DeepStruct, USM, REBEL, MarkupLM/GraphIE

---

请对以上每条 W1-W7、M1-M5、Q1-Q5 逐条给出 [AGREE] 或 [REBUT]，并简述理由。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 654 · 2026-05-19T07:17:36.620833+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_violation_landscape.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_violation_landscape.tex"
  }
}
```

</details>

---


### Tool result

_source line 655 · 2026-05-19T07:17:37.475391+00:00_

1	% §5 Setup (compressed from Violation Landscape)
2	% exp_ids: mvp_phase0_violation_rate, mvp_phase0_scierc_schema,
3	%          mvp_phase0_violation_rate_docred, mvp_phase0_docred_schema
4	
5	\label{sec:violation_landscape}
6	
7	We evaluate OntoCoDec in two complementary regimes.
8	Fine-tuning composability (\S\ref{sec:composability}) tests whether constraints compose losslessly with standard training at deployment-grade quality (R-F1 40--46).
9	Zero-shot evaluation stress-tests constraint robustness when the model has no task-specific supervision (R-F1 2--8).
10	
11	\paragraph{Setup.}
12	We evaluate on SciERC~\cite{luan2018scierc} (551 test sentences, 7 relations, $\bar{\kappa}{=}0.333$) and DocRED~\cite{yao2019docred} (998 dev documents,\footnote{DocRED test annotations are not publicly available; we evaluate on the development set.} 96 relations, $\bar{\kappa}{=}0.842$).
13	RE type constraints are extracted automatically from observed type pairs in training data (neither dataset provides a formal ontology); EE constraints on WikiEvents (\S\ref{sec:wikievents}) are derived from the KAIROS ontology.
14	The framework handles both sources without modification.
15	Primary model: Qwen3-8B~\cite{qwen2025qwen3}, zero-shot greedy decoding; cross-model validation in \S\ref{sec:cross-model}, composability with fine-tuning in \S\ref{sec:composability}.
16	We measure four violation categories: \textbf{DR} (domain/range type pair $\notin \sigma(r)$), \textbf{RV} (relation $\notin \mathcal{R}$), \textbf{ET} (entity type $\notin \mathcal{E}$), and \textbf{CF} (same entity assigned conflicting types across triples).
17	Baseline DR violations are 15.37\% (SciERC) and 18.46\% (DocRED), comparable rates associated with constraint tightness rather than ontology scale (\S\ref{sec:introduction}); schema-informed prompting reduces DR by 62\% on SciERC but is per-relation unreliable (Appendix~\ref{app:per-relation-landscape}).
18	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 854
}
```

</details>

---


### Tool call

_source line 656 · 2026-05-19T07:17:37.978501+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex",
  "offset": "130",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex",
    "offset": "130",
    "limit": "80"
  }
}
```

</details>

---


### Tool result

_source line 657 · 2026-05-19T07:17:38.532937+00:00_

130	The contribution of this work is the constraint enforcement method itself; the zero-shot setting stress-tests constraint robustness under maximum model uncertainty, while composability with fine-tuning (\S\ref{sec:composability}) validates practical deployment value.
131	
132	%%% Paragraph 4: Decoding-Time vs. Post-Hoc Enforcement %%%
133	% exp_ids: posthoc_filtering_baseline, phase2_scierc_full_s1 (R-F1=8.36%),
134	%          phase2_docred_full_s1 (R-F1=8.23%, ET=0%)
135	
136	\paragraph{Decoding-Time vs.\ Post-Hoc Enforcement.}
137	Post-hoc filtering (generating triples without constraints, then removing schema-violating predictions) yields higher precision and consequently higher F1 than OntoCoDec on both datasets (SciERC 8.63 vs.\ 8.36; DocRED 9.61 vs.\ 8.23).
138	% posthoc: SciERC F1=8.63, DocRED F1=9.61; OntoCoDec: SciERC R-F1=8.36, DocRED R-F1=8.23
139	However, this precision gain comes at substantial cost.
140	On DocRED, post-hoc filtering discards 48.1\% of all predicted triples, including 127 true positives (11.2\% of correct predictions); recall drops from 9.46\% to 8.40\%.
141	% posthoc_docred: rejection=48.1%, tp_lost=127/1137, R: 9.46→8.40
142	Entity type violations remain unresolved (ET\,=\,2.47\% vs.\ OntoCoDec's 0\%), as filtering targets only domain/range and vocabulary violations.
143	% posthoc_docred: ET_residual=2.47%; phase2_docred_full_s1: ET=0%
144	OntoCoDec's decoding-time approach avoids this information loss by guiding generation toward compliant outputs rather than discarding non-compliant ones, preserving both recall and entity type validity.
145	The two strategies are complementary: post-hoc filtering can serve as an additional safety net for residual violations that decoding-time enforcement does not fully resolve.
146	
147	%%% CF Violation Distribution %%%
148	% exp_ids: phase2_scierc_full_s1 (CF=245), llama_scierc_full_s1 (CF=162),
149	%          phase2_docred_full_s1 (CF=2670), llama_docred_full_s1 (CF=3824)
150	
151	\paragraph{C
…[truncated 3629 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 554
}
```

</details>

---


### Tool call

_source line 658 · 2026-05-19T07:17:39.490896+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "post.hoc|posthoc|Post-hoc|filtering",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
  "glob": "*.tex",
  "output_mode": "content",
  "-n": "True",
  "head_limit": "30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "post.hoc|posthoc|Post-hoc|filtering",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
    "glob": "*.tex",
    "output_mode": "content",
    "-n": "True",
    "head_limit": "30"
  }
}
```

</details>

---


### Tool result

_source line 659 · 2026-05-19T07:17:39.592037+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section1_introduction_draft.tex:14:Post-hoc filtering achieves higher F1 in most zero-shot settings via precision gains, but at the cost of discarding up to 48\% of predictions including true positives; at high rejection rates (e.g., Mistral DocRED 73.7\%), it discards the majority of outputs and becomes impractical.
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_related_work.tex:22:In programming-language generation, constrained decoding has been extended beyond syntax to enforce semantic properties such as type correctness; this work demonstrates that richer-than-CFG constraints can be compiled into token-level filtering.
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_related_work.tex:24:While mechanistically similar to OntoCoDec's token-level filtering, PICARD operates over a \emph{fixed, fully enumerated} schema (database table and column names known before decoding begins).
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_related_work.tex:48:While Roth \& Yih's ILP formulation shares the same type-compatibility motivation, it operates as a post-hoc reranker over discrete candidates; OntoCoDec integrates enforcement directly into autoregressive decoding, preventing violations rather than filtering them.
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_related_work.tex:70:\paragraph{Post-hoc Ontology Validation.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_related_work.tex:83:Post-hoc validation detects violations after generation and requires rejection or correction cycles that waste 
…[truncated 6628 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 660 · 2026-05-19T07:17:45.326836+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "rebel|REBEL|cabot2021",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
  "glob": "*.tex",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "rebel|REBEL|cabot2021",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
    "glob": "*.tex",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---


### Tool result

_source line 661 · 2026-05-19T07:17:46.232259+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_related_work.tex:7:Training-based methods~\cite{paolini2021tanl,cabot2021rebel,lu2022uie,knowcoder_acl2024,li2023codeie,schema_rl2025} provide soft guidance; post-hoc approaches~\cite{khorshidi2025odke,spires_2024,ontologx_2025,slot2025} validate outputs after generation.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 905
}
```

</details>

---


### Tool call

_source line 662 · 2026-05-19T07:17:46.232796+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex",
  "offset": "295",
  "limit": "60"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex",
    "offset": "295",
    "limit": "60"
  }
}
```

</details>

---


### Tool result

_source line 663 · 2026-05-19T07:17:46.285017+00:00_

295	Outside Llama DocRED, all residual violations (3 of 36, spanning Llama SciERC and Qwen DocRED) trace exclusively to schema coverage gaps: the model's entity typing is accurate, and the constraint system has reached its theoretical ceiling given the frequency-based constraint table.
296	On DocRED, Llama-3.1-8B contributes 33 of 36 residual violations (92\%), with entity type errors as the dominant cause (14/33, 42\%).
297	This asymmetry reflects Llama's weaker fine-tuned entity typing on DocRED's larger ontology (96 relations, 7 entity types) compared to Qwen, which achieves near-zero residual.
298	The implication is twofold: (i)~the irreducible floor from schema gaps is small ($\sim$3 violations across 4 settings), so the constraint system operates near its theoretical optimum; (ii)~residual violations from entity typing errors are addressable through stronger base models or improved entity typing modules, without modifying the constraint architecture.
299	
300	%%% Post-Hoc Filtering Comparison (Extended) %%%
301	% exp_ids: posthoc_*_zs, posthoc_*_ft
302	
303	\paragraph{Post-Hoc Filtering: Extended Comparison.}
304	\label{app:posthoc-extended}
305	
306	Table~\ref{tab:posthoc-extended} presents the full comparison across all six zero-shot and four fine-tuned configurations.
307	
308	\begin{table}[t]
309	\centering
310	\small
311	\setlength{\tabcolsep}{3pt}
312	\resizebox{\columnwidth}{!}{%
313	\begin{tabular}{@{}lll rrr l@{}}
314	\toprule
315	\textbf{Setting} & \textbf{Model} & \textbf{Dataset} & \textbf{Reject\%} & \textbf{R-F1$_{\text{ph}}$} & \textbf{R-F1$_{\text{cd}}$} & \textbf{Winner} \\
316	\midrule
317	\multirow{6}{*}{ZS}
318	  & Qwen    & SciERC & 16.8 & 8.63  & 8.36  & ph \\
319	  & Llama   & SciERC & 13.9 & 2.71  & 2.54  & ph \\
320	  & Mistral & SciERC & 20.3 & 3.94  & 3.67  & ph \\
321	  & Qwen    & DocRED & 48.1 & 9.61  & 8.23  & ph \\
322	  & Llama   & DocRED & 42.2 & 7.44  & 6.27  & ph \\
323	  & Mistral & DocRED & \textbf{73.7} & 3.85  & \textbf{
…[truncated 2161 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 52
}
```

</details>

---


### Tool call

_source line 664 · 2026-05-19T07:20:05.703773+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 — 交叉回应 Reviewer 1 审稿意见\n\n### Must-Fix\n\n**[AGREE] R1-W1: Constraint table 来源于训练数据，与标题 \"Compiled Ontology Constraints\" framing 不符**\n同意这是重要的 framing 问题。§5 setup 明确承认 SciERC/DocRED 的 constraints 从训练数据提取。标题中 \"Ontology\" 一词与实际操作存在张力。补充：WikiEvents 确实使用了 KAIROS 形式本体，且框架对两种来源统一处理（§5 L14）。但 SciERC/DocRED 作为主要实验数据集，constraint table 不完整性会高估 reported violation rates（unseen-but-valid type pairs 被错误计为 violation）。覆盖率未报告是一个关键缺失。\n\n**[AGREE] R1-W2: CF 副作用严重且为结构性问题**\n完全同意，与我的 N1 一致。补充证据：WikiEvents EE 场景下 CF 更严重（15-21%, Table 5），意味着 CF 随 task 复杂度恶化。\"training-free\" 定位与实际需要 fine-tuning 控制 CF 之间确实存在张力。\n\n**[PARTIALLY AGREE] R1-W3: 缺少关键 baseline 对比**\nGCD 事实上已被隐式对比——Table 1 caption 明确写道 \"Grammar-only represents the ceiling of grammar-constrained decoding (Geng et al., 2023)\"。但论文应更显式 frame 这一点。GoLLIE/EnriCo 是 training-based 方法，zero-shot 不直接可比，但 fine-tuned 场景对比（OntoCoDec+LoRA vs GoLLIE）确实缺失。Post-hoc filtering 已在 Appendix B Table 11 系统对比（10 settings），但关键数据应纳入主文。\n\n**[AGREE] R1-W4: 多个关键实验样本量不足**\n同意。Dual-factor n=4、WikiEvents FT 20 docs、beam DocRED 50 docs 均为有效关切。WikiEvents 的 20-doc 是数据集约束但不免除需要更大 EE benchmark 的责任。\n\n**[PARTIALLY AGREE] R1-W5: Zero-shot R-F1 过低**\n部分同意。Appendix B 已回应此关切（F1 是 control variable，zero-shot 是 stress-test），有一定合理性。但同意叙事权重批评：§5.1-5.3 占 ~60% 篇幅却对应最低实用价值的 regime，fine-tuned composability 应为叙事主角。\n\n**[AGREE] R1-W6: Mistral boundary condition 定义不充分**\n同意。ET>5% 排除准则是 post-hoc 的，无先验理论依据。\n\n**[AGREE] R1-W7: 未评估下游影响**\n同意。§1 动机与验证之间存在 gap。Limitations 承认此局限但未弥补。\n\n### Minor\n\n**[AGREE] R1-M1**: Table 2 caption \"DR ≤ 0.09%\" 仅限 SciERC，DocRED Llama DR=0.20% 超出该上界。\n**[PARTIALLY AGREE] R1-M2**: logit -∞ 是标准做法，加脚注即可。\n**[AGREE] R1-M3**: 阈值应有 justification。\n**[REBUT] R1-M4**: exp_ids 等为 LaTeX 注释，编译 PDF 中不可见，不影响 blind review。Source hygiene 问题，camera-ready 时清理即可。\n**[AGREE] R1-M5**: XGrammar edge case 已在脚注诚实报告，严重程度低。\n\n### Questions\n\n**[AGREE] R1-Q1**: Constraint table 覆盖率应报告（observed/possible type pair coverage），unseen pairs 被误计为 DR violation 会高估效果。\n**[AGREE] R1-Q2**: CF 下游影响应量化，至少做简单 KG 导入模拟。\n**[PARTIALLY AGREE] R1-Q3**: Post-hoc 对比已在 Appendix B Table 11 系统呈现（OntoCoDec 赢 recall 6/6 ZS, ET elimination, crossover at 73.7% reject rate），但应在主文更突出。\n**[PARTIALLY AGREE] R1-Q4**: Beam search 未设为默认因 1.54× latency（§5.4 L14），但主文缺乏明确的 greedy vs beam 推荐讨论。\n**[AGREE] R1-Q5**: 固定字段顺序（§3.1 L28）确实限制 prompt 灵活性，应在 Limitations 提及。\n\n### Missing References\n\n**[AGREE]** InstructUIE, DeepStruct, USM\n**[REBUT]** REBEL：已引用（section6_related_work.tex L7, cabot2021rebel）\n**[PARTIALLY AGREE]** MarkupLM/GraphIE：与 ontology-constrained decoding 关联度较低，非必需\n\n### 补充发现\n\nR1 的审稿意见整体准确且与我的独立评估高度一致。我们在以下关键点完全独立地得出相同结论：\n1. CF trade-off 与 \"near-lossless\" claim 不一致（R1-W2 = 我的 N1）\n2. WikiEvents 评估初步（R1-W4 WikiEvents 部分 = 我的 N2）\n3. Dual-factor 统计不足（R1-W4 = 我的 W4）\n4. InstructUIE/DeepStruct 缺失（R1 Missing Refs = 我的 Missing Refs）\n\nR1 的 W1（ontology framing）和 W7（downstream eval）是我未充分强调但完全认同的重要问题。R1 对 post-hoc filtering 优势的分析（W3）也有力——论文需要更诚实地承认 post-hoc 在多数 zero-shot settings 下 F1 更高的事实。",
  "reviewer_id": "2",
  "project": "schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 — 交叉回应 Reviewer 1 审稿意见\n\n### Must-Fix\n\n**[AGREE] R1-W1: Constraint table 来源于训练数据，与标题 \"Compiled Ontology Constraints\" framing 不符**\n同意这是重要的 framing 问题。§5 setup 明确承认 SciERC/DocRED 的 constraints 从训练数据提取。标题中 \"Ontology\" 一词与实际操作存在张力。补充：WikiEvents 确实使用了 KAIROS 形式本体，且框架对两种来源统一处理（§5 L14）。但 SciERC/DocRED 作为主要实验数据集，constraint table 不完整性会高估 reported violation rates（unseen-but-valid type pairs 被错误计为 violation）。覆盖率未报告是一个关键缺失。\n\n**[AGREE] R1-W2: CF 副作用严重且为结构性问题**\n完全同意，与我的 N1 一致。补充证据：WikiEvents EE 场景下 CF 更严重（15-21%, Table 5），意味着 CF 随 task 复杂度恶化。\"training-free\" 定位与实际需要 fine-tuning 控制 CF 之间确实存在张力。\n\n**[PARTIALLY AGREE] R1-W3: 缺少关键 baseline 对比**\nGCD 事实上已被隐式对比——Table 1 caption 明确写道 \"Grammar-only represents the ceiling of grammar-constrained decoding (Geng et al., 2023)\"。但论文应更显式 frame 这一点。GoLLIE/EnriCo 是 training-based 方法，zero-shot 不直接可比，但 fine-tuned 场景对比（OntoCoDec+LoRA vs GoLLIE）确实缺失。Post-hoc filtering 已在 Appendix B Table 11 系统对比（10 settings），但关键数据应纳入主文。\n\n**[AGREE] R1-W4: 多个关键实验样本量不足**\n同意。Dual-factor n=4、WikiEvents FT 20 docs、beam DocRED 50 docs 均为有效关切。WikiEvents 的 20-doc 是数据集约束但不免除需要更大 EE benchmark 的责任。\n\n**[PARTIALLY AGREE] R1-W5: Zero-shot R-F1 过低**\n部分同意。Appendix B 已回应此关切（F1 是 control variable，zero-shot 是 stress-test），有一定合理性。但同意叙事权重批评：§5.1-5.3 占 ~60% 篇幅却对应最低实用价值的 regime，fine-tuned composability 应为叙事主角。\n\n**[AGREE] R1-W6: Mistral boundary condition 定义不充分**\n同意。ET>5% 排除准则是 post-hoc 的，无先验理论依据。\n\n**[AGREE] R1-W7: 未评估下游影响**\n同意。§1 动机与验证之间存在 gap。Limitations 承认此局限但未弥补。\n\n### Minor\n\n**[AGREE] R1-M1**: Table 2 caption \"DR ≤ 0.09%\" 仅限 SciERC，DocRED Llama DR=0.20% 超出该上界。\n**[PARTIALLY AGREE] R1-M2**: logit -∞ 是标准做法，加脚注即可。\n**[AGREE] R1-M3**: 阈值应有 justification。\n**[REBUT] R1-M4**: exp_ids 等为 LaTeX 注释，编译 PDF 中不可见，不影响 blind review。Source hygiene 问题，camera-ready 时清理即可。\n**[AGREE] R1-M5**: XGrammar edge case 已在脚注诚实报告，严重程度低。\n\n### Questions\n\n**[AGREE] R1-Q1**: Constraint table 覆盖率应报告（observed/possible type pair coverage），unseen pairs 被误计为 DR violation 会高估效果。\n**[AGREE] R1-Q2**: CF 下游影响应量化，至少做简单 KG 导入模拟。\n**[PARTIALLY AGREE] R1-Q3**: Post-hoc 对比已在 Appendix B Table 11 系统呈现（OntoCoDec 赢 recall 6/6 ZS, ET elimination, crossover at 73.7% reject rate），但应在主文更突出。\n**[PARTIALLY AGREE] R1-Q4**: Beam search 未设为默认因 1.54× latency（§5.4 L14），但主文缺乏明确的 greedy vs beam 推荐讨论。\n**[AGREE] R1-Q5**: 固定字段顺序（§3.1 L28）确实限制 prompt 灵活性，应在 Limitations 提及。\n\n### Missing References\n\n**[AGREE]** InstructUIE, DeepStruct, USM\n**[REBUT]** REBEL：已引用（section6_related_work.tex L7, cabot2021rebel）\n**[PARTIALLY AGREE]** MarkupLM/GraphIE：与 ontology-constrained decoding 关联度较低，非必需\n\n### 补充发现\n\nR1 的审稿意见整体准确且与我的独立评估高度一致。我们在以下关键点完全独立地得出相同结论：\n1. CF trade-off 与 \"near-lossless\" claim 不一致（R1-W2 = 我的 N1）\n2. WikiEvents 评估初步（R1-W4 WikiEvents 部分 = 我的 N2）\n3. Dual-factor 统计不足（R1-W4 = 我的 W4）\n4. InstructUIE/DeepStruct 缺失（R1 Missing Refs = 我的 Missing Refs）\n\nR1 的 W1（ontology framing）和 W7（downstream eval）是我未充分强调但完全认同的重要问题。R1 对 post-hoc filtering 优势的分析（W3）也有力——论文需要更诚实地承认 post-hoc 在多数 zero-shot settings 下 F1 更高的事实。",
    "reviewer_id": "2",
    "project": "schema_semantic_constrained_ie"
  }
}
```

</details>

---


### Tool result

_source line 665 · 2026-05-19T07:20:10.589783+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_01fc90ae186a4ed432770f7601995139:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4886
}
```

</details>

---


### Assistant

_source line 666 · 2026-05-19T07:20:19.802079+00:00_

交叉回应已提交给 Review Director。

总结：Reviewer 1 的 7 个 Weakness 中，我完全同意 5 个（W1, W2, W4, W6, W7），部分同意 2 个（W3 因 GCD 已隐式对比, W5 因 stress-test framing 有一定合理性）。5 个 Minor 中同意 3 个，部分同意 1 个，反驳 1 个（M4 源码注释不影响 PDF）。5 个 Question 均为合理关切。Missing References 中 REBEL 已被引用，其余同意缺失。两位 Reviewer 在 CF trade-off、WikiEvents 初步性、统计不足等核心问题上独立得出了一致判断。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2"
}
```

</details>

---


## Round 16

## Round 16

100 recorded events


### User

_source line 667 · 2026-05-19T07:52:25.276108+00:00_

[Round 10 审稿请求]:
## Round 10 审稿任务 — Reviewer 2（新颖性 + 完整性 + 写作 + 格式）

### 论文信息
- **标题**: OntoCoDec: Type-Constrained Information Extraction via Compiled Ontology Constraints
- **路径**: `projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex`
- **目标 venue**: EMNLP 2026 via ACL Rolling Review (ARR)
- **Deadline**: 2026-05-25

### Venue 格式要求（实时搜索确认）
- **页数**: Long paper ≤ 8 页正文（Limitations/Ethics/References/Appendix 不计）
- **模板**: ACL 官方模板，`\usepackage[review]{acl}`
- **匿名**: Double-blind（作者信息不得出现）
- **必须包含**: Limitations section（缺失 = desk reject）
- **Checklist**: Responsible NLP Research checklist 必须填写
- **评分标准**: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next, 1=Do not resubmit

### 你的审查侧重

**主要职责：新颖性 + 论文完整性 + 写作质量 + 格式合规**

请重点审查以下方面：

1. **新颖性评估**：
   - 相对于现有 grammar-constrained decoding (XGrammar, Outlines, GCD) 的技术增量是多少？
   - 相对于 schema-aware IE (GoLLIE, KnowCoder, EnriCo) 的增量？
   - "Semantic layer + entity registry" 的核心创新点是否清晰且具有显著性？
   - Constraint tightness 分析和 dual-factor pattern 是否构成独立贡献？

2. **论文完整性**：
   - Related Work 是否充分覆盖了所有相关领域？引用密度是否匹配 EMNLP 水平？
   - Limitations 是否诚实且全面？
   - 是否缺少重要的讨论（如 CF 的解决路径、downstream evaluation）？
   - Ethics Statement 是否符合 ARR 要求？
   - Appendix 内容是否在正文中有引用？是否有信息堆砌？

3. **写作质量**（按论文写作规范严格审查）：
   - Abstract 是否在 150-250 words 内回答四个必答问题？数据密度是否过高？
   - Introduction 是否遵循"背景→问题→不足→方法→贡献"结构？叙事是否连贯？
   - 全文主线是否统一（Abstract→Intro→Method→Results→Discussion 讲的是同一个故事）？
   - 是否有 AI 写作痕迹（em-dash, -ing phrases, 过度分段, 用词黑名单）？
   - 专有名词/缩写是否首次出现时有定义？
   - §7 Discussion and Conclusion 长度和深度是否合适？

4. **格式合规**：
   - 页数是否在 8 页限制内？
   - 表格/图标是否遵循视觉规范（信息密度、字体大小、caption 自包含）？
   - 引用格式是否正确？是否有 orphan/duplicate bib entries？
   - 是否缺少 Responsible NLP checklist？

### 输出格式

请按以下结构输出审稿意见：

```
## Summary
[2-3 句概述]

## Strengths
[S1] ...
[S2] ...

## Weaknesses
[W1] [Must-Fix / Should-Fix / Minor] ...
[W2] ...

## Questions
[Q1] ...

## Missing References
...

## Overall Assessment
Score: X.X (按 EMNLP 2026 ARR 评分标准)
Confidence: X/5
[简短总评]
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 668 · 2026-05-19T07:53:26.861862+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 669 · 2026-05-19T07:53:28.420719+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/review_reviewer_2_cbe93d98.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1558
}
```

</details>

---


### Tool call

_source line 670 · 2026-05-19T07:53:28.471520+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
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

_source line 671 · 2026-05-19T07:53:28.472043+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 672 · 2026-05-19T07:53:34.685018+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 673 · 2026-05-19T07:53:35.388868+00:00_

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
12	\usepackage{multirow}
13	\usepackage{amsmath}
14	\usepackage{amssymb}
15	\usepackage{enumitem}
16	\usepackage{xcolor}
17	\usepackage{pifont}
18	
19	\title{OntoCoDec: Type-Constrained Information Extraction\\via Compiled Ontology Constraints}
20	
21	\author{Anonymous ACL submission}
22	
23	\begin{document}
24	\maketitle
25	
26	% === Abstract ===
27	\input{abstract}
28	
29	% === §1 Introduction ===
30	\input{section1_introduction_draft}
31	
32	% === §2 Background ===
33	\input{section2_background}
34	
35	% === §3 Method ===
36	\input{section3_method_draft}
37	
38	% === §4 Constraint Composition ===
39	\section{Constraint Composition}
40	\label{sec:composition}
41	\input{section4_composition_draft}
42	
43	% === §5 Experiments ===
44	\section{Experiments}
45	\label{sec:experiments}
46	
47	\input{section3_violation_landscape}
48	
49	\input{section5_scierc_draft}
50	\input{section5_docred_draft}
51	\input{section5_crossmodel_draft}
52	\input{section5_wikievents_draft}
53	\input{section5_runtime}
54	
55	% === §6 Related Work ===
56	\input{section6_related_work}
57	
58	% === §7 Discussion and Conclusion ===
59	\section{Discussion and Conclusion}
60	\label{sec:discussion}
61	\input{section7_conclusion_compressed}
62	
63	% === Limitations (ARR requirement: standalone section, does not count toward page limit) ===
64	\clearpage
65	\section*{Limitations}
66	
67	\paragraph{Constraint scope.}
68	CF impact is model-dependent: for well-calibrated models (Qwen, Llama), S1 introduces CF violations (up to 12.02\%) as a consequence of per-relation independent enforcement; for poorly-calibrated models (Mistral), S1 substantially reduces CF (56.87\%\,$\to$\,1.27\%) by constraining type assignments to schema-valid values.
69	CF fallback ablation sh
…[truncated 4385 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 703
}
```

</details>

---


### Tool call

_source line 674 · 2026-05-19T07:53:35.439591+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria scoring"
  }
}
```

</details>

---


### Tool result

_source line 675 · 2026-05-19T07:53:42.927982+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"https://aclrollingreview.org/"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"}]

Based on the search results, here's information about the ACL ARR 2026 reviewer guidelines, review form criteria, and scoring:

## Scoring System

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

## Overall Recommendation Score

The Overall assessment score is an explicit recommendation for the outcome of this pap
…[truncated 1092 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7488
}
```

</details>

---


### Tool call

_source line 676 · 2026-05-19T07:53:48.804833+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form: all scoring dimensions, their scales, and descriptions. Include soundness, excitement, overall assessment, confidence, and any other fields."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form: all scoring dimensions, their scales, and descriptions. Include soundness, excitement, overall assessment, confidence, and any other fields."
  }
}
```

</details>

---


### Tool call

_source line 677 · 2026-05-19T07:53:51.217085+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/paper/abstract.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/paper/abstract.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie"
  }
}
```

</details>

---


### Tool result

_source line 678 · 2026-05-19T07:53:51.669541+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 679 · 2026-05-19T07:53:51.720243+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/paper/section*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/paper/section*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie"
  }
}
```

</details>

---


### Tool result

_source line 680 · 2026-05-19T07:53:52.122662+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft_4796e8.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion_550cbf_DEPRECATED.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_relwork_additions.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_relwork_outline.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion_DEPRECATED.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft_9b84f1.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_method_draft.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_runtime.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_wikievents_draft.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_violation_landscape.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion_compressed.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section4_compositi
…[truncated 576 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 681 · 2026-05-19T07:53:52.173382+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/paper/appendix*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/paper/appendix*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie"
  }
}
```

</details>

---


### Tool result

_source line 682 · 2026-05-19T07:53:52.224030+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_prompts.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_reproducibility.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_sampling_table.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_scalability.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_beam_search.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_full_ft.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_doc_length.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_prompt_sensitivity.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_llama_per_relation.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_case_studies.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 683 · 2026-05-19T07:53:55.915232+00:00_

# ACL Rolling Review Form - Complete Scoring Dimensions

## 1. **Reviewer Confidence**
Scale: 1-5
- 5: "Positive that my evaluation is correct. I read the paper very carefully"
- 4: "Quite sure. I tried to check the important points carefully"
- 3: "Pretty sure, but there's a chance I missed something"
- 2: "Willing to defend my evaluation, but it is fairly likely that I missed some details"
- 1: "Not my area, or paper is very hard to understand"

## 2. **Soundness**
Scale: 1-5 (with half-point increments)
- 5: "Excellent: This study is one of the most thorough"
- 4: "Strong: This study provides sufficient support for all claims"
- 3: "Acceptable: This study provides sufficient support for main claims"
- 2: "Poor: Some main claims not sufficiently supported"
- 1: "Major Issues: not sufficiently thorough to warrant publication"

## 3. **Excitement**
Scale: 1-5 (with half-point increments)
- 5: "Highly Exciting: I would recommend this paper to others"
- 4: "Exciting: I would mention this paper to others"
- 3: "Interesting: I might mention some points of this paper"
- 2: "Potentially Interesting: does not resonate with me"
- 1: "Not Exciting: does not resonate with me"

## 4. **Overall Assessment**
Scale: 1-5 (with half-point increments)
- 5: "Consider for Award: outstanding paper award consideration"
- 4: "Conference: could be accepted to an ACL conference"
- 3: "Findings: could be accepted to Findings of ACL"
- 2: "Resubmit next cycle: needs substantial revisions"
- 1: "Do not resubmit: must be fully redone"

## 5. **Additional Dimensions**

**Reproducibility** (1-5 scale): Assesses sufficiency of details for replicating results

**Datasets** (1-5 scale): Rates value of released datasets to research community

**Software** (1-5 scale): Evaluates utility of released software to others

**Author Identity Knowledge** (1-5 scale): Tracks reviewer's knowledge of author(s)

**Ethical Review Requirement**: Binary determination of need for in-depth ethics assessment

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 7110
}
```

</details>

---


### Tool call

_source line 684 · 2026-05-19T07:54:00.895771+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 685 · 2026-05-19T07:54:01.820938+00:00_

1	\begin{abstract}
2	We present \textsc{OntoCoDec}, which compiles Information Extraction (IE) ontology schemas into two composable token-level decoding constraints:
3	(1)~a \emph{grammar layer} (XGrammar) that guarantees JSON structural validity and vocabulary membership; and
4	(2)~a \emph{semantic layer} that enforces per-triple domain/range type constraints via a stateful entity registry and dynamic logit masking, with grammar-first fallback when constraints conflict.
5	Without constraints, Large Language Model (LLM) based IE produces systematic domain/range (DR) violations that persist after fine-tuning; violation rates correlate with \emph{constraint tightness} rather than ontology or model scale.
6	% exp_ids: w5_lora_scierc_constrained_eval, w5_qwen_docred_lora_constrained_eval, w5_llama_lora_scierc_constrained_eval, w5_llama_docred_lora_constrained_eval
7	Composed with Low-Rank Adaptation (LoRA), \textsc{OntoCoDec} achieves near-lossless composability under fine-tuning: DR\,$\leq$\,0.20\% with R-F1 within $\pm$0.6\,pp.
8	Under zero-shot decoding, DR drops by 76--99\% for calibrated models, with an accompanying cross-field consistency (CF) increase (9--21\% zero-shot, resolved to $\leq$1.2\% by fine-tuning on both RE and EE).
9	Beam search with LoRA eliminates all four violation types on SciERC.
10	The framework extends to event extraction without modification (preliminary, 20-document test set).
11	OntoCoDec is training-free and applies to any autoregressive LM across four models (8B--70B) and three tokenizer families.
12	\end{abstract}
13	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 925
}
```

</details>

---


### Tool call

_source line 686 · 2026-05-19T07:54:01.972393+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section1_introduction_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section1_introduction_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 687 · 2026-05-19T07:54:02.274376+00:00_

1	% Section 1: Introduction (compressed, 669→~550 words)
2	
3	\section{Introduction}
4	\label{sec:introduction}
5	
6	Large language models are increasingly used for information extraction~\cite{li2023codeie,sainz2024gollie,wei2023zeroshot}, but when generating relation triples $(h, r, t)$, neither entity is guaranteed to carry a type consistent with the ontology's domain/range constraints for $r$.
7	We call such outputs \emph{domain/range violations}: structurally valid triples that are ontologically invalid.
8	Violations persist across the capability spectrum: 15.4\% of triples on SciERC~\cite{luan2018scierc} and 18.5\% on DocRED~\cite{yao2019docred} under zero-shot decoding, and 1--2\% even after LoRA fine-tuning; rates correlate with \emph{constraint tightness} (few valid type pairs per relation) rather than ontology or model scale.
9	Type violations are ontologically invalid regardless of downstream application: a triple whose head or tail type lies outside the relation's domain/range specification contradicts the schema definition.
10	At deployment-grade quality (R-F1 40--46\%), where extracted triples feed directly into knowledge graphs, reliable type-safety enforcement is needed.
11	
12	Existing approaches leave a fundamental gap.
13	Schema-informed prompting reduces violations by 62\% on average but is per-relation unreliable (violations for \textsc{Evaluate-for} actually \emph{increase} by 5.8\,pp).
14	Grammar-constrained decoding~\cite{dong2025xgrammar,willard2023outlines,beurer-kellner2023lmql} guarantees syntactic well-formedness but cannot encode cross-field semantic constraints.
15	Post-hoc filtering achieves higher F1 in most zero-shot settings via precision gains, but at the cost of discarding up to 48\% of predictions including true positives; at high rejection rates (e.g., Mistral DocRED 73.7\%), it discards the majority of outputs and becomes impractical.
16	OntoCoDec preserves recall by enforcing constraints during generation rather than discardi
…[truncated 2815 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 688 · 2026-05-19T07:54:02.425418+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section2_background.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section2_background.tex"
  }
}
```

</details>

---


### Tool result

_source line 689 · 2026-05-19T07:54:02.727082+00:00_

1	% Section 2: Background (compressed)
2	
3	\section{Background}
4	\label{sec:background}
5	
6	\paragraph{IE Ontology Structure.}
7	\label{sec:bg:ontology}
8	An IE ontology $\mathcal{O} = (\mathcal{E}, \mathcal{R}, \sigma)$ defines entity types $\mathcal{E}$, relation types $\mathcal{R}$, and a mapping $\sigma: \mathcal{R} \to \mathcal{P}(\mathcal{E} \times \mathcal{E})$ specifying valid (head type, tail type) pairs per relation.
9	A triple $(h, r, t)$ is \emph{type-valid} if $(\mathrm{type}(h), \mathrm{type}(t)) \in \sigma(r)$.
10	We quantify constraint restrictiveness via \emph{constraint tightness} $\kappa(r)$ (Eq.~\ref{eq:tightness}, \S\ref{sec:composition}): tighter constraints leave fewer valid type pairs per relation.
11	We define ontology constraints broadly to encompass both formal ontology specifications (e.g., the KAIROS event ontology with explicit role-entity type mappings) and empirically derived type-pair constraints extracted from annotated training data.
12	The latter applies when datasets lack a formal ontology but provide typed annotations (SciERC, DocRED); OntoCoDec compiles both sources into the same constraint representation without modification.
13	Empirical constraints achieve 99\%+ instance-level coverage on held-out data (SciERC 99.0\%, DocRED 99.4\%); uncovered type pairs trigger grammar-first fallback (\S\ref{sec:composition}), ensuring no valid triples are blocked.
14	
15	\paragraph{Grammar-Constrained Decoding.}
16	\label{sec:bg:gcd}
17	Grammar-constrained decoding restricts each token $y_t$ to a mask $M_g \in \{0, 1\}^{|V|}$ derived from a target grammar.
18	XGrammar~\citep{dong2025xgrammar} compiles JSON Schemas into pushdown automata for efficient enforcement of structural constraints; Outlines~\citep{willard2023outlines} and SGLang~\citep{zheng2024sglang} offer similar capabilities.
19	However, these methods are limited to context-free constraints and cannot enforce cross-field semantic rules (e.g., ``if $r$ = \textsc{Feature-of}, t
…[truncated 859 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 690 · 2026-05-19T07:54:02.777764+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_method_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_method_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 691 · 2026-05-19T07:54:02.878868+00:00_

1	% Section 3 — Method (Draft)
2	% OntoCoDec: Type-Valid Information Extraction
3	% via Compiled Ontology Constraints
4	
5	\section{Method}
6	\label{sec:method}
7	
8	We present OntoCoDec, a two-layer constrained decoding framework that compiles ontology schemas into token-level masks enforced during autoregressive generation.
9	Unlike type-constrained code generation, IE presents three distinct challenges: (1)~entity types are inferred from free text rather than declared annotations, (2)~the entity registry is built dynamically during generation, and (3)~constraint targets are context-dependent type assignments rather than fixed grammar productions.
10	The grammar layer (\S\ref{sec:grammar}) guarantees structural validity (well-formed JSON with ontology-vocabulary membership), while the semantic layer (\S\ref{sec:semantic}) enforces domain/range type constraints via a stateful entity registry.
11	We describe the problem formulation (\S\ref{sec:formulation}), each layer, and two decoding strategies (\S\ref{sec:strategies}).
12	Formal analysis of constraint composition is deferred to Section~\ref{sec:composition}.
13	
14	
15	\subsection{Problem Formulation}
16	\label{sec:formulation}
17	
18	\paragraph{IE as structured generation.}
19	Given an input text $x$, a language model generates a structured JSON output $y$:
20	%
21	\begin{equation}\label{eq:output-schema}
22	\resizebox{.88\columnwidth}{!}{$\displaystyle
23	  y = \bigl\{\texttt{entities}: [\{n_i, \tau_i\}],\; \texttt{relations}: [\{h_j, t_j, r_j, \tau^h_j, \tau^t_j\}]\bigr\}
24	$}
25	\end{equation}
26	%
27	where each entity has a name $n_i$ and type $\tau_i \in \mathcal{E}$, and each relation specifies head $h_j$, tail $t_j$, relation type $r_j \in \mathcal{R}$, and head/tail entity types $\tau^h_j, \tau^t_j$.
28	The output JSON Schema (\S\ref{sec:grammar}) enforces a fixed field ordering (head $\to$ tail $\to$ relation $\to$ head\_type $\to$ tail\_type) via deterministic grammar compilation.
29	This ordering en
…[truncated 6610 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 692 · 2026-05-19T07:54:11.722146+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section4_composition_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section4_composition_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 693 · 2026-05-19T07:54:11.722730+00:00_

1	% Section: Constraint Composition (compressed, 787→~500 words)
2	
3	At each decoding step $t$, let $G(t) \subseteq V$ and $S(t) \subseteq V$ denote the tokens permitted by the grammar and semantic layers, respectively.
4	The final mask is their conjunction:
5	%
6	\begin{equation}\label{eq:composition}
7	  M_{\text{final}}(t) = M_{\text{grammar}}(t) \;\wedge\; M_{\text{semantic}}(t),
8	\end{equation}
9	%
10	so a token is allowed only if it satisfies \emph{both} structural and type-level constraints.
11	The conjunction is asymmetric: $S(t)$ is defined only over $G(t)$. This reflects the enabling dependency (\S\ref{sec:method}): the semantic layer requires the relation type to belong to $\mathcal{R}$, a property guaranteed only by the grammar layer.
12	
13	\paragraph{Grammar-First Fallback.}
14	When $S(t) \cap G(t) = \emptyset$ (tight constraints leave no token that is both grammar-valid and semantically valid), na\"{\i}ve masking would force selection of a grammar-invalid token, breaking JSON structure.
15	We enforce a \emph{grammar-first fallback}: if no semantically valid token survives grammar filtering, semantic masking is skipped and the grammar layer alone controls selection.
16	Structural integrity is a hard constraint; a type violation is a soft error detectable by downstream validation.
17	Among type violations, DR and CF differ in severity: a DR violation renders the triple ontologically invalid (the entity type lies outside the relation's domain or range), whereas a CF violation means each triple is individually schema-valid but the same entity receives different type assignments across triples.
18	
19	\paragraph{Constraint Tightness.}
20	Recall the tightness of relation $r$ (\S\ref{sec:bg:ontology}):
21	%
22	\begin{equation}\label{eq:tightness}
23	  \kappa(r) = 1 - \frac{|\sigma(r)|}{|\mathcal{E}|^2},
24	\end{equation}
25	%
26	The mean tightness $\bar{\kappa} = \frac{1}{|\mathcal{R}|}\sum_{r} \kappa(r)$ characterizes ontology restrictiveness.
27	Tighter 
…[truncated 1297 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 694 · 2026-05-19T07:54:11.823599+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_violation_landscape.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_violation_landscape.tex"
  }
}
```

</details>

---


### Tool result

_source line 695 · 2026-05-19T07:54:11.974796+00:00_

1	% §5 Setup (compressed from Violation Landscape)
2	% exp_ids: mvp_phase0_violation_rate, mvp_phase0_scierc_schema,
3	%          mvp_phase0_violation_rate_docred, mvp_phase0_docred_schema
4	
5	\label{sec:violation_landscape}
6	
7	We evaluate OntoCoDec in two complementary regimes.
8	Fine-tuning composability (\S\ref{sec:composability}) demonstrates deployment readiness: constraints compose losslessly with standard LoRA training at R-F1 40--46, our recommended configuration.
9	Zero-shot evaluation stress-tests constraint robustness under adversarial conditions (no task supervision, R-F1 2--8), where CF trade-offs are expected and documented (\S\ref{sec:cross-model}).
10	
11	\paragraph{Setup.}
12	We evaluate on SciERC~\cite{luan2018scierc} (551 test sentences, 7 relations, $\bar{\kappa}{=}0.333$) and DocRED~\cite{yao2019docred} (998 dev documents,\footnote{DocRED test annotations are not publicly available; we evaluate on the development set.} 96 relations, $\bar{\kappa}{=}0.842$).
13	RE type constraints are extracted automatically from observed type pairs in training data (neither dataset provides a formal ontology); EE constraints on WikiEvents (\S\ref{sec:wikievents}) are derived from the KAIROS ontology.
14	The framework handles both sources without modification.
15	Primary model: Qwen3-8B~\cite{qwen2025qwen3}, zero-shot greedy decoding; cross-model validation in \S\ref{sec:cross-model}, composability with fine-tuning in \S\ref{sec:composability}.
16	We measure four violation categories: \textbf{DR} (domain/range type pair $\notin \sigma(r)$), \textbf{RV} (relation $\notin \mathcal{R}$), \textbf{ET} (entity type $\notin \mathcal{E}$), and \textbf{CF} (same entity assigned conflicting types across triples).
17	Baseline DR violations are 15.37\% (SciERC) and 18.46\% (DocRED), comparable rates associated with constraint tightness rather than ontology scale (\S\ref{sec:introduction}); schema-informed prompting reduces DR by 62\% on SciERC but is per-relation unreliab
…[truncated 51 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 696 · 2026-05-19T07:54:12.025580+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 697 · 2026-05-19T07:54:12.679210+00:00_

1	% Section 5 — SciERC Results (Draft)
2	% Data source: Phase 2 SciERC registry experiments
3	% exp_ids: phase2_scierc_unconstrained, phase2_scierc_grammar_only,
4	%          phase2_scierc_semantic_only, phase2_scierc_full_s1, phase2_scierc_full_s2
5	% All numbers verified against registry 2026-05-14.
6	
7	\subsection{Ablation and Composability with Fine-Tuning}
8	\label{sec:scierc-results}
9	
10	Table~\ref{tab:scierc-ablation} presents the five-way ablation on SciERC (Qwen3-8B, zero-shot, 551 documents); only the active constraint layers differ across rows.
11	
12	% ──────────────────────────────────────────
13	%  Table: SciERC five-way ablation
14	% ──────────────────────────────────────────
15	\begin{table}[t]
16	\centering
17	\small
18	\setlength{\tabcolsep}{3.6pt}
19	\resizebox{\columnwidth}{!}{%
20	\begin{tabular}{@{}l rrrrrr rr@{}}
21	\toprule
22	& \multicolumn{6}{c}{\textbf{Violation Rates (\%)}}
23	& \multicolumn{2}{c}{\textbf{F1}} \\
24	\cmidrule(lr){2-7} \cmidrule(l){8-9}
25	\textbf{Mode}
26	  & DR\,$\downarrow$ & $\Delta$DR
27	  & RV\,$\downarrow$ & ET\,$\downarrow$ & CF & Tot.\,$\downarrow$
28	  & Rel.\,$\uparrow$ & Ent.\,$\uparrow$ \\
29	\midrule
30	Unconstrained
31	  & 15.37 & ---
32	  & 1.39  & 0.40
33	  & 0.08  & 15.45
34	  & 8.23  & 31.01 \\
35	Grammar
36	  & 14.84 & $\downarrow$3\%
37	  & \textbf{0} & \textbf{0}
38	  & 0.08  & 14.92
39	  & 8.23  & 30.98 \\
40	Semantic
41	  & 11.65 & $\downarrow$24\%
42	  & 1.51  & 0.40
43	  & 2.71  & 14.36
44	  & 8.15  & 31.01 \\
45	Full (S1)
46	  & \textbf{0.93} & $\downarrow$\textbf{94\%}
47	  & \textbf{0} & \textbf{0}
48	  & 9.90  & \textbf{10.83}
49	  & \textbf{8.36} & 30.98 \\
50	Full (S2)
51	  & 0.97  & $\downarrow$94\%
52	  & \textbf{0} & \textbf{0}
53	  & 8.03  & \textbf{9.00}
54	  & 8.03  & \textbf{31.90} \\
55	\bottomrule
56	\end{tabular}}%
57	\caption{Five-way ablation on SciERC (551 docs, Qwen3-8B, zero-shot).
58	$\Delta$DR: relative change vs.\ unconstrained.
59	Tot.\ = DR + CF (total type-violation b
…[truncated 5095 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 653
}
```

</details>

---


### Tool call

_source line 698 · 2026-05-19T07:54:12.679666+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 699 · 2026-05-19T07:54:12.731002+00:00_

1	% Section 5 — DocRED Results (compressed, 1450→~600 words)
2	% exp_ids: phase2_docred_unconstrained, phase2_docred_grammar_only,
3	%          phase2_docred_semantic_only, phase2_docred_full_s1
4	% All numbers verified against registry 2026-05-14.
5	
6	\subsection{Cross-Dataset Validation on DocRED}
7	\label{sec:docred-results}
8	
9	Table~\ref{tab:docred-ablation} presents the four-way ablation on DocRED (96 Wikidata relation types, 14$\times$ SciERC; Qwen3-8B, zero-shot, 998 documents).
10	
11	% ──────────────────────────────────────────
12	%  Table: DocRED four-way ablation
13	% ──────────────────────────────────────────
14	\begin{table}[t]
15	\centering
16	\small
17	\setlength{\tabcolsep}{3.6pt}
18	\resizebox{\columnwidth}{!}{%
19	\begin{tabular}{@{}l rrrrrr rr@{}}
20	\toprule
21	& \multicolumn{6}{c}{\textbf{Violation Rates (\%)}}
22	& \multicolumn{2}{c}{\textbf{F1}} \\
23	\cmidrule(lr){2-7} \cmidrule(l){8-9}
24	\textbf{Mode}
25	  & DR\,$\downarrow$ & $\Delta$DR
26	  & RV\,$\downarrow$ & ET\,$\downarrow$ & CF & Tot.\,$\downarrow$
27	  & Rel.\,$\uparrow$ & Ent.\,$\uparrow$ \\
28	\midrule
29	Unconstrained
30	  & 18.46 & ---
31	  & 29.66 & 2.48
32	  & 0.10  & 18.56
33	  & 7.74  & 58.15 \\
34	Grammar
35	  & 26.17 & $\uparrow$42\%
36	  & \textbf{0.03} & \textbf{0}
37	  & 0.07  & 26.24
38	  & \textbf{8.31}  & \textbf{59.38} \\
39	Semantic
40	  & 13.84 & $\downarrow$25\%
41	  & 29.87 & 4.22
42	  & 1.05  & 14.89
43	  & 7.70  & 57.81 \\
44	Full (S1)
45	  & \textbf{10.21} & $\downarrow$\textbf{45\%}
46	  & \textbf{0.03} & \textbf{0}
47	  & 2.57  & \textbf{12.78}
48	  & 8.23  & 59.37 \\
49	\bottomrule
50	\end{tabular}}%
51	\caption{Four-way ablation on DocRED (998 documents, Qwen3-8B, zero-shot).
52	$\Delta$DR: relative change vs.\ unconstrained.
53	Tot.\ = DR + CF (total type-violation burden).
54	Best per column in \textbf{bold} (CF excluded; Tot.\ included).
55	F1 $\times$100. Bootstrap significance: R-F1 $+$0.50\,pp ($p < 0.001$).}
56	\label{tab:docred-ablation}
57	\en
…[truncated 1553 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 700 · 2026-05-19T07:54:19.565649+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_crossmodel_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_crossmodel_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 701 · 2026-05-19T07:54:19.616508+00:00_

1	% Section 5 — Cross-Model Validation (compressed, 830→~400 words)
2	% exp_ids: phase2_scierc_unconstrained, phase2_scierc_full_s1,
3	%          phase2_docred_unconstrained, phase2_docred_full_s1,
4	%          llama_scierc_unconstrained, llama_scierc_full_s1,
5	%          llama_docred_unconstrained, llama_docred_full_s1
6	
7	\subsection{Cross-Model Validation}
8	\label{sec:cross-model}
9	
10	Table~\ref{tab:cross-model} replicates S1 with Llama-3.1-8B and Mistral-7B under identical prompts.
11	
12	\begin{table}[t]
13	\centering
14	\small
15	\setlength{\tabcolsep}{3.4pt}
16	\resizebox{\columnwidth}{!}{%
17	\begin{tabular}{@{}ll rrrr r@{}}
18	\toprule
19	& & \multicolumn{4}{c}{\textbf{Violation Rates (\%)}}
20	& \textbf{R-F1} \\
21	\cmidrule(lr){3-6} \cmidrule(l){7-7}
22	\textbf{Dataset} & \textbf{Model}
23	  & DR\,$\downarrow$ & RV\,$\downarrow$ & ET\,$\downarrow$ & CF
24	  & $\uparrow$ \\
25	\midrule
26	\multirow{6}{*}{SciERC}
27	  & Qwen (U)    & 15.37 & 1.39  & 0.40 & 0.08 & 8.23 \\
28	  & Qwen (S1)   &  0.93 & 0     & 0    & 9.90 & 8.36 \\
29	  \cmidrule(l){2-7}
30	  & Llama (U)   & 13.34 & 0.55  & 0    & 0.24 & 2.68 \\
31	  & Llama (S1)  &  0.08 & 0     & 0    & 6.56 & 2.54 \\
32	  \cmidrule(l){2-7}
33	  & Mistral (U) & 56.94 & 0     & 1.50 & 56.87$^\dagger$ & 3.66 \\
34	  & Mistral (S1)& 13.40 & 0     & 0    & 1.27  & 3.67 \\
35	\midrule
36	\multirow{6}{*}{DocRED}
37	  & Qwen (U)    & 18.46 & 29.66 & 2.48 & 0.10 & 7.74 \\
38	  & Qwen (S1)   & 10.21 &  0.03 & 0    & 2.57 & 8.23 \\
39	  \cmidrule(l){2-7}
40	  & Llama (U)   & 26.07 & 16.03 & 0.13 & 0.17 & 5.98 \\
41	  & Llama (S1)  &  2.55 &  0    & 0    & 12.02& 6.27 \\
42	  \cmidrule(l){2-7}
43	  & Mistral (U) & 57.42 & 42.35 & 7.58 & 24.78 & 4.34 \\
44	  & Mistral (S1)& 33.20 &  0    & 0    & 0.19  & 5.52 \\
45	\bottomrule
46	\end{tabular}}%
47	\caption{Three-model zero-shot validation. U: unconstrained; S1: full two-layer.
48	Parse failures: Llama DocRED 9.1\%; others $\leq$1.1\%.
49	$^\dagger$Mistral: poor ze
…[truncated 1797 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 702 · 2026-05-19T07:54:19.616979+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_wikievents_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_wikievents_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 703 · 2026-05-19T07:54:19.617246+00:00_

1	% Section 5 — Event Extraction on WikiEvents (compact, inline)
2	% exp_ids: ee_qwen_wikievents_unconstrained, ee_llama_wikievents_unconstrained,
3	%          ee_mistral_wikievents_unconstrained, ee_qwen_wikievents_constrained,
4	%          ee_llama_wikievents_constrained, ee_mistral_wikievents_constrained_v2
5	% v3 final data confirmed by Director 2026-05-18.
6	
7	\subsection{Cross-Task Validation: Event Extraction}
8	\label{sec:wikievents}
9	
10	We apply OntoCoDec to event extraction (EE) on WikiEvents~\cite{li2021document} (56 event types, 80 roles, 27 entity types, 245 constraints; Appendix~\ref{app:wikievents}) without modification.
11	Violations extend to EV (event vocabulary), RoV (role vocabulary), and AC (argument constraint, analogous to DR).
12	
13	% ──────────────────────────────────────────
14	%  Table: WikiEvents three-model comparison (v3 final)
15	%  exp_ids: ee_{qwen,llama,mistral}_wikievents_{unconstrained,grammar_only,constrained_v3}
16	% ──────────────────────────────────────────
17	\begin{table}[t]
18	\centering
19	\small
20	\setlength{\tabcolsep}{2.8pt}
21	\resizebox{\columnwidth}{!}{%
22	\begin{tabular}{@{}ll rrrr rr@{}}
23	\toprule
24	& & \multicolumn{4}{c}{\textbf{Violation Rates (\%)}}
25	& \multicolumn{2}{c}{\textbf{F1}} \\
26	\cmidrule(lr){3-6} \cmidrule(l){7-8}
27	\textbf{Model} & \textbf{Mode}
28	  & EV\,$\downarrow$ & RoV\,$\downarrow$ & AC & CF
29	  & Trig.\,$\uparrow$ & Ent.\,$\uparrow$ \\
30	\midrule
31	\multirow{3}{*}{Qwen3-8B}
32	  & Unconstr.\ & 24.0 & 74.9 & 0.3 & 0 & 11.8 & 0 \\
33	  & Grammar    & \textbf{0} & 76.1 & 8.2 & --- & --- & --- \\
34	  & Full S1    & \textbf{0} & \textbf{0} & 2.1 & 21.1 & 13.4 & 14.1 \\
35	\midrule
36	\multirow{3}{*}{\shortstack[l]{Llama\\3.1-8B}}
37	  & Unconstr.\ & 10.5 & 88.8 & 0.1 & 0 & 5.7 & 0 \\
38	  & Grammar    & \textbf{0} & 77.0 & 8.8 & --- & --- & --- \\
39	  & Full S1    & \textbf{0} & \textbf{0} & 3.8 & 17.2 & 7.5 & 17.6 \\
40	\midrule
41	\multirow{3}{*}{\shortstack[l]{Mistral\\7B}}
42
…[truncated 2360 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 704 · 2026-05-19T07:54:19.717956+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_runtime.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_runtime.tex"
  }
}
```

</details>

---


### Tool result

_source line 705 · 2026-05-19T07:54:19.919608+00:00_

1	% Runtime overhead (inline paragraph, no subsection header to save space)
2	
3	\paragraph{Runtime overhead.}
4	\label{sec:runtime}
5	S1 overhead is $+$13.1\% on SciERC and $+$2.43\% on DocRED (amortized over longer sequences); under LoRA, $+$10.0\% with 37\% lower absolute latency.
6	Grammar compile: one-time 44\,ms (Appendix~\ref{app:runtime}).
7	Scaling benchmarks confirm constant overhead (2--3\%) up to 200 entity types and 1{,}000 relations (Appendix~\ref{app:scalability}).
8	
9	\paragraph{Beam search compatibility.}
10	\label{sec:beam-results}
11	Under greedy S1, the grammar-first fallback resolves DR$\leftrightarrow$CF conflicts one token at a time; beam search ($k{=}4$) explores paths that satisfy both layers jointly and reduces DR and CF simultaneously.
12	With LoRA, beam S1 eliminates all four violation types on SciERC for both Qwen and Llama (R-F1 44.23, 46.11; Table~\ref{tab:beam-search}).
13	Under zero-shot, beam reduces DR to 0\% for calibrated models (Qwen, Llama) and CF substantially (9.90\%\,$\to$\,0.53\% Qwen; 6.56\%\,$\to$\,0.93\% Llama); Mistral remains a boundary condition (DR 7.99\%, CF 1.27\%) due to high baseline violations (Appendix~\ref{app:beam-search}).
14	Total latency overhead is 1.54$\times$ (beam 1.32$\times$ $+$ constraint 1.17$\times$; Table~\ref{tab:beam-latency}).
15	
16	% exp_ids: 70b_scierc_unconstrained, 70b_scierc_constrained, 70b_docred_unconstrained, 70b_docred_constrained
17	\paragraph{Cross-scale generalizability.}
18	\label{sec:70b-results}
19	On Llama-3.1-70B (AWQ INT4), OntoCoDec achieves DR$\to$0\% on SciERC (R-F1 $-$0.03\,pp) and \textbf{0\%} across ET, RV, and DR on the full DocRED 998-document set (R-F1 $+$0.04\,pp), the only configuration to completely eliminate DR on DocRED.
20	CF rises to 7.01\% (from 0.07\%); the low baseline reflects under-measurement (malformed outputs bypass the checker), while constrained decoding exposes more triples to the consistency check (\S\ref{sec:discussion}).
21	Model scale reduces
…[truncated 39 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 706 · 2026-05-19T07:54:19.920307+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 707 · 2026-05-19T07:54:19.970862+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	We provide a detailed survey in Appendix~\ref{app:related_work}; here we position OntoCoDec along three axes.
5	
6	\paragraph{Grammar-constrained decoding.}
7	XGrammar~\cite{dong2025xgrammar}, Outlines~\cite{willard2023outlines}, LMQL~\cite{beurer-kellner2023lmql}, SynCode~\cite{ugare2024syncode}, and Grammar-Aligned Decoding~\cite{park2024grammar} guarantee format validity via CFG-based token masking; JSONSchemaBench~\cite{jsonschemabench2025} benchmarks these systems.
8	GCD~\cite{geng2023gcd} applies grammar constraints to IE tasks.
9	In code generation, PICARD~\cite{scholak2021picard} and Synchromesh~\cite{synchromesh_iclr2022} enforce type constraints via incremental parsing, and \citet{pldi2025_type_constrained_codegen} compile full type systems into prefix automata.
10	These methods ensure syntactic or type-level validity but operate on static type declarations; IE requires a dynamic entity registry built during generation, where constraint targets depend on the co-occurring relation type.
11	OntoCoDec's grammar layer builds on XGrammar; its semantic layer extends constrained decoding from syntax to ontology-level type enforcement.
12	
13	\paragraph{Schema-aware IE.}
14	GoLLIE~\cite{sainz2024gollie} and KnowCoder~\cite{knowcoder_acl2024} encode ontology structure as Python dataclasses and train models to generate typed code.
15	InstructUIE~\cite{wang2023instructuie}, DeepStruct~\cite{wang2022deepstruct}, UIE~\cite{lu2022uie}, and USM~\cite{lou2023usm} unify extraction tasks via structured output formats with task-specific training.
16	UniversalNER~\cite{zhou2024universalner} achieves strong zero-shot NER via targeted distillation.
17	\citet{wadhwa2023revisiting} benchmark LLM-based RE and find persistent schema compliance gaps.
18	These methods internalize constraints through training; OntoCoDec enforces them at decoding time without retraining, and the two approaches are complementary (a GoLLIE-trained 
…[truncated 1203 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 708 · 2026-05-19T07:54:25.548988+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion_compressed.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion_compressed.tex"
  }
}
```

</details>

---


### Tool result

_source line 709 · 2026-05-19T07:54:26.554932+00:00_

1	% Section 7 — Discussion and Conclusion (maximally compressed)
2	% Full discussion in Appendix; Mistral boundary condition in app:dual-factor.
3	
4	OntoCoDec compiles IE ontology schemas into composable token-level decoding constraints.
5	The core finding is that ontology type constraints can be compiled into token-level masks that compose near-losslessly with standard fine-tuning: DR reaches $\leq$\,0.20\% with R-F1 within $\pm$0.6\,pp on RE (R-F1 40--46), RoV$\to$0\% and AC$\leq$0.8\% on EE, and beam search ($k{=}4$) eliminates all four RE violation types for calibrated models (\S\ref{sec:beam-results}).
6	Under zero-shot decoding (R-F1 2--8\%), DR drops by 42--99\% across three models and three datasets with no significant F1 cost.
7	
8	CF remains an open challenge for per-slot enforcement: the current architecture enforces type constraints independently per relation slot, so the same entity can receive different type assignments across triples.
9	Global entity-level type consensus during decoding, where all slots referencing the same entity must agree on its type, offers the most direct resolution path.
10	
11	The framework applies to any autoregressive IE system without model modification or additional training: the constraint compiler takes an ontology schema as input and produces token-level masks compatible with any LM vocabulary.
12	This generality is validated across four models (8B--70B), three tokenizer families, and two IE tasks (RE, EE).
13	The interaction between constraint tightness and model calibration is consistent across three datasets but would benefit from validation on a broader range of ontologies and model scales.
14	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1005
}
```

</details>

---


### Tool call

_source line 710 · 2026-05-19T07:54:26.555341+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 711 · 2026-05-19T07:54:26.957663+00:00_

1	\section{Extended Related Work}
2	\label{app:related_work}
3	
4	% ===========================================================================
5	% Paradigm 1: Grammar-Constrained Decoding
6	% ===========================================================================
7	\paragraph{Grammar-Constrained Decoding.}
8	Recent work has established efficient algorithms for restricting LLM outputs to conform to context-free grammars, making grammar-constrained decoding the de facto standard for obtaining structured output from language models.
9	XGrammar~\cite{dong2025xgrammar} partitions the vocabulary into context-independent and context-dependent tokens and maintains persistent pushdown automata across decoding steps, achieving up to 100$\times$ speedup over prior CFG-constrained decoding methods.
10	Outlines~\cite{willard2023outlines} reformulates constrained generation as finite-state machine transitions with offline vocabulary indexing, which enables efficient enforcement of regular-expression and JSON-schema constraints without runtime overhead per token.
11	LMQL~\cite{beurer-kellner2023lmql} introduces a declarative query language that compiles type, length, and regex constraints into token-level masks, providing a programmable interface for specifying multi-variable output structures.
12	These systems ensure that every generated token belongs to a grammar-valid continuation, but they do not address the \emph{distribution distortion} introduced by naive token masking.
13	A parallel line of work tackles this problem directly: DOMINO~\cite{beurer-kellner2024domino} minimizes distributional divergence during CFG enforcement by formulating mask selection as an optimization problem, and ASAp~\cite{park2024grammar} provides a provably unbiased sampling algorithm that preserves the original LM distribution under grammar constraints.
14	Together, these advances have made grammar-constrained decoding both fast and statistically principled, and provide a robust foundation for 
…[truncated 19750 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 712 · 2026-05-19T07:54:26.958130+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 713 · 2026-05-19T07:54:27.260559+00:00_

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
26	The two-layer architecture produces two distinct fallback mechanisms with different semant
…[truncated 31971 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 302
}
```

</details>

---


### Tool call

_source line 714 · 2026-05-19T07:54:35.934909+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_prompts.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_prompts.tex"
  }
}
```

</details>

---


### Tool result

_source line 715 · 2026-05-19T07:54:36.337352+00:00_

1	% Appendix — Prompt Templates
2	% W10: Extraction prompts used in all experiments.
3	
4	\section{Prompt Templates}
5	\label{app:prompts}
6	
7	All experiments use the same prompts across constrained and unconstrained decoding; constraints are applied at the logit level, not through prompt modification.
8	Table~\ref{tab:prompts} shows the system and user prompts for each dataset.
9	
10	\begin{table*}[t]
11	\centering
12	\small
13	\begin{tabular}{@{}p{0.95\textwidth}@{}}
14	\toprule
15	\textbf{SciERC --- System Prompt (Unconstrained \& Constrained)} \\
16	\midrule
17	\texttt{You are an expert information extraction system for scientific texts. Extract entities and relations from the given text.} \\[4pt]
18	\texttt{Entity types: Task, Method, Material, Metric, OtherScientificTerm, Generic} \\
19	\texttt{Relation types: Used-for, Feature-of, Hyponym-of, Part-of, Compare, Conjunction, Evaluate-for} \\[4pt]
20	\texttt{Output a JSON object with:} \\
21	\texttt{- "entities": list of \{"text": "...", "type": "..."\}} \\
22	\texttt{- "relations": list of \{"head": "...", "tail": "...", "type": "...", "head\_type": "...", "tail\_type": "..."\}} \\[4pt]
23	\texttt{Output ONLY valid JSON, no explanation.} \\
24	\midrule
25	\textbf{SciERC --- User Prompt} \\
26	\midrule
27	\texttt{Extract all entities and relations from this scientific text:} \\
28	\texttt{"\{text\}"} \\
29	\texttt{Output JSON:} \\
30	\midrule
31	\midrule
32	\textbf{DocRED --- System Prompt (Unconstrained \& Constrained)} \\
33	\midrule
34	\texttt{You are an information extraction system. Extract all entities and relations from the following document.} \\[4pt]
35	\texttt{Entity types: PER, ORG, LOC, TIME, NUM, MISC} \\[4pt]
36	\texttt{Relation types: country, instance of, performer, ...\ (96 Wikidata relation types; full list omitted for space)} \\[4pt]
37	\texttt{Output a JSON object with exactly this structure:} \\
38	\texttt{\{"entities": [\{"text": "entity name", "type": "ENTITY\_TYPE"\}],} \\
39	\texttt{\ "
…[truncated 770 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 716 · 2026-05-19T07:54:36.488447+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_reproducibility.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_reproducibility.tex"
  }
}
```

</details>

---


### Tool result

_source line 717 · 2026-05-19T07:54:37.794713+00:00_

1	\section{Reproducibility Details}
2	\label{app:reproducibility}
3	
4	\paragraph{Fine-tuning configuration.}
5	All four fine-tuned models (Qwen3-8B and Llama-3.1-8B-Instruct on SciERC and DocRED) use identical LoRA hyperparameters: rank $r{=}16$, $\alpha{=}32$, dropout $0.05$, no bias, targeting all attention and MLP projection layers (\texttt{q\_proj}, \texttt{k\_proj}, \texttt{v\_proj}, \texttt{o\_proj}, \texttt{gate\_proj}, \texttt{up\_proj}, \texttt{down\_proj}).
6	Training uses AdamW with learning rate $2{\times}10^{-4}$, cosine schedule, warmup ratio $0.1$, effective batch size $16$, bf16 precision, gradient checkpointing, and completion-only loss for 3 epochs.
7	SciERC trains on 1,762 examples (260 dev) for 333 steps; DocRED trains on 3,053 examples (998 dev) for 573 steps.
8	Maximum sequence length is 2,048 (SciERC) and 4,096 (DocRED).
9	All runs use seed 42.
10	
11	\paragraph{Hardware and software.}
12	Training runs on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (98\,GB VRAM).
13	SciERC fine-tuning takes approximately 11 minutes per model; DocRED takes approximately 1.5 hours.
14	Software versions: PyTorch 2.10, Transformers 4.57, PEFT 0.19, TRL 1.1, Accelerate 1.13.
15	
16	\paragraph{Inference time.}
17	Inference timing is reported in Appendix~\ref{app:runtime} (NVIDIA RTX PRO 6000 Blackwell Server Edition GPU, same hardware as training).
18	Full S1 constrained decoding adds $+$13.1\% wall-clock overhead on SciERC and $+$2.43\% on DocRED (Qwen3-8B, zero-shot greedy); under LoRA fine-tuning, overhead is $+$10.0\% on SciERC.
19	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1306
}
```

</details>

---


### Tool call

_source line 718 · 2026-05-19T07:54:37.795257+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_case_studies.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_case_studies.tex"
  }
}
```

</details>

---


### Tool result

_source line 719 · 2026-05-19T07:54:38.248375+00:00_

1	% Appendix — Error Analysis and Case Studies
2	
3	\section{Error Analysis and Case Studies}
4	\label{app:case-studies}
5	
6	\definecolor{violation}{RGB}{220,50,50}
7	\definecolor{fixed}{RGB}{34,139,34}
8	\definecolor{cfwarn}{RGB}{200,120,0}
9	
10	We present four representative cases illustrating constraint behavior across violation types. Cases 1--3 demonstrate OntoCoDec's corrective mechanisms; Case 4 illustrates a limitation.
11	
12	\subsection{Domain-Range Correction}
13	\label{app:case-dr}
14	
15	\noindent\textbf{Input (SciERC, Qwen3-8B):} \textit{``We present a novel model-based approach to recover the shapes and the poses of transparent objects from known motion.''}
16	
17	The unconstrained model assigns \textsc{OtherScientificTerm} to ``shapes'' and ``poses,'' producing \textsc{Feature-of}(\textsc{Task}, \textsc{OtherScientificTerm}) triples that violate domain/range constraints. The semantic layer redirects the tail type to \textsc{Task}, yielding schema-compliant triples (Table~\ref{tab:case1}).
18	
19	\begin{table}[h]
20	\centering
21	\small
22	\caption{OntoCoDec corrects three Feature-of DR violations. \textcolor{violation}{Red} = violation; \textcolor{fixed}{green} = corrected.}
23	\label{tab:case1}
24	\begin{tabular}{@{}p{3.2cm}lll@{}}
25	\toprule
26	\textbf{Triple} & \textbf{Head} & \textbf{Tail} & \textbf{DR} \\
27	\midrule
28	\multicolumn{4}{@{}l}{\textit{Unconstrained (3 violations)}} \\
29	\midrule
30	Feature-of(recover, shapes) & Task & \textcolor{violation}{OtherSciTerm} & \textcolor{violation}{\ding{55}} \\
31	Feature-of(recover, poses) & Task & \textcolor{violation}{OtherSciTerm} & \textcolor{violation}{\ding{55}} \\
32	Feature-of(recover, transp.\ obj.) & Task & \textcolor{violation}{OtherSciTerm} & \textcolor{violation}{\ding{55}} \\
33	Used-for(model approach, recover) & Method & Task & \ding{51} \\
34	\midrule
35	\multicolumn{4}{@{}l}{\textit{OntoCoDec (0 violations)}} \\
36	\midrule
37	Feature-of(recover, shapes) & Task & \textcolor{fixe
…[truncated 5952 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 720 · 2026-05-19T07:54:38.399948+00:00_

called mcp__agent-ml-research__verify_references

<details open><summary>🔧 Tool call — mcp__agent-ml-research__verify_references</summary>

```json
{
  "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
  "project": "schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__verify_references",
  "tool_args": {
    "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
    "project": "schema_semantic_constrained_ie"
  }
}
```

</details>

---


### Tool result

_source line 721 · 2026-05-19T07:55:31.449870+00:00_

&lt;persisted-output>
Output too large (56KB). Full output saved to: /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie--claude-sessions-review-reviewer-2-cbe93d98/76a9ff9b-369a-49db-b121-ef5b7390ec30/tool-results/toolu_01DGNTnKKt7GvAE8kSixBZGK.txt

Preview (first 2KB):
{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 69, \"total_citations\": 90, \"unique_cited_keys\": 54, \"orphan_bib\": 14, \"missing_bib\": 0, \"duplicate_keys\": 1, \"online_verified\": 53, \"online_not_found\": 4, \"online_mismatch\": 11}, \"cross_check\": {\"orphan_bib\": [\"cabot2021rebel\", \"dccd2026\", \"delafuente2025guidex\", \"geng2025jsonschemabench\", \"guidex2025\", \"lee2026formattax\", \"lu2025schemarl\", \"paolini2021tanl\", \"park2024grammaraligned\", \"reddy2026dccd\", \"sakota2025boostcd\", \"schema_rl2025\", \"shen2025slot\", \"vukovic2024dore\"], \"missing_bib\": [], \"orphan_count\": 14, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"synchromesh_iclr2022\", \"type\": \"inproceedings\", \"title\": \"Synchromesh: Reliable Code Generation from Pre-trained Language Models\", \"authors\": \"Poesia, Gabriel and Polozov, Oleksandr and Le, Vu and Tiwari, Ashish and Soares,...\", \"year\": \"2022\", \"venue\": \"International Conference on Learning Representations\"}, {\"key\": \"mgd_neurips2023\", \"type\": \"inproceedings\", \"title\": \"Monitor-Guided Decoding of Code LMs with Static Analysis of Repository Context\", \"authors\": \"Agrawal, Lakshya A. and Kanade, Aditya and Goyal, Navin and Lahiri, Shuvendu K. ...\", \"year\": \"2023\", \"venue\": \"Advances in Neural Information Processing Systems\"}, {\"key\": \"pldi2025_type_constrained_codegen\", \"type\": \"article\", \"title\": \"Type-Constrained Code Generation with Language Models\", \"authors\": \"M\\\\\\\"undler, Niels and He, Jingxuan and Wang, Hao and Sen, Koushik and Song, Dawn ...\", \"year\": \"2025\", \"venue
…[truncated 369 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__verify_references",
  "elapsed_ms": 53049
}
```

</details>

---


### Tool call

_source line 722 · 2026-05-19T07:55:36.934849+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie--claude-sessions-review-reviewer-2-cbe93d98/76a9ff9b-369a-49db-b121-ef5b7390ec30/tool-results/toolu_01DGNTnKKt7GvAE8kSixBZGK.txt",
  "offset": "0",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie--claude-sessions-review-reviewer-2-cbe93d98/76a9ff9b-369a-49db-b121-ef5b7390ec30/tool-results/toolu_01DGNTnKKt7GvAE8kSixBZGK.txt",
    "offset": "0",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 723 · 2026-05-19T07:55:38.344967+00:00_

0	{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 69, \"total_citations\": 90, \"unique_cited_keys\": 54, \"orphan_bib\": 14, \"missing_bib\": 0, \"duplicate_keys\": 1, \"online_verified\": 53, \"online_not_found\": 4, \"online_mismatch\": 11}, \"cross_check\": {\"orphan_bib\": [\"cabot2021rebel\", \"dccd2026\", \"delafuente2025guidex\", \"geng2025jsonschemabench\", \"guidex2025\", \"lee2026formattax\", \"lu2025schemarl\", \"paolini2021tanl\", \"park2024grammaraligned\", \"reddy2026dccd\", \"sakota2025boostcd\", \"schema_rl2025\", \"shen2025slot\", \"vukovic2024dore\"], \"missing_bib\": [], \"orphan_count\": 14, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"synchromesh_iclr2022\", \"type\": \"inproceedings\", \"title\": \"Synchromesh: Reliable Code Generation from Pre-trained Language Models\", \"authors\": \"Poesia, Gabriel and Polozov, Oleksandr and Le, Vu and Tiwari, Ashish and Soares,...\", \"year\": \"2022\", \"venue\": \"International Conference on Learning Representations\"}, {\"key\": \"mgd_neurips2023\", \"type\": \"inproceedings\", \"title\": \"Monitor-Guided Decoding of Code LMs with Static Analysis of Repository Context\", \"authors\": \"Agrawal, Lakshya A. and Kanade, Aditya and Goyal, Navin and Lahiri, Shuvendu K. ...\", \"year\": \"2023\", \"venue\": \"Advances in Neural Information Processing Systems\"}, {\"key\": \"pldi2025_type_constrained_codegen\", \"type\": \"article\", \"title\": \"Type-Constrained Code Generation with Language Models\", \"authors\": \"M\\\\\\\"undler, Niels and He, Jingxuan and Wang, Hao and Sen, Koushik and Song, Dawn ...\", \"year\": \"2025\", \"venue\": \"Proceedings of the ACM on Programming Languages\"}, {\"key\": \"roth_yih_2004\", \"type\": \"inproceedings\", \"title\": \"A Linear Programming Formulation for Global Inference in Natural Language Tasks\", \"authors\": \"Roth, Dan and Yih, Wen-tau\", \"year\": \"2004\", \"venue\": \"Proceedings of the Eighth Conference on Computational
…[truncated 55395 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1410
}
```

</details>

---


### Tool call

_source line 724 · 2026-05-19T07:55:38.450927+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_scalability.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_scalability.tex"
  }
}
```

</details>

---


### Tool result

_source line 725 · 2026-05-19T07:55:38.804101+00:00_

1	\section{Ontology Scalability}
2	\label{app:scalability}
3	
4	\begin{table}[h]
5	\centering
6	\small
7	\resizebox{\columnwidth}{!}{%
8	\begin{tabular}{@{}lrrrr@{}}
9	\toprule
10	\textbf{Scale} & \textbf{Types} & \textbf{Rels} & \textbf{Compile (s)} & \textbf{Overhead} \\
11	\midrule
12	Small (SciERC) & 6 & 7 & 0.33 & 1.02$\times$ \\
13	Medium (DocRED) & 6 & 96 & 0.32 & 1.03$\times$ \\
14	Large (synth.) & 100 & 500 & 0.35 & 1.03$\times$ \\
15	XLarge (synth.) & 200 & 1{,}000 & 0.42 & 1.03$\times$ \\
16	\bottomrule
17	\end{tabular}}
18	\caption{Compilation time (one-time) and per-token inference overhead across ontology scales. Small and Medium use real ontologies; Large and XLarge use synthetic ontologies with random domain/range constraints. Overhead measured on Qwen3-8B, 10 documents per scale.}
19	\label{tab:scalability}
20	\end{table}
21	
22	Grammar compilation scales sub-linearly (0.33\,s to 0.37\,s for 7$\to$1{,}000 relations); semantic constraint compilation grows linearly but remains negligible (0.4\,ms to 17\,ms).
23	Inference overhead is constant at 2--3\% because XGrammar uses precompiled bitmasks ($O(1)$ per token) and the semantic layer checks only the active relation's domain/range set rather than the full ontology.
24	The practical limit is first-token uniqueness: when entity types exceed $\sim$200, prefix collisions in the tokenizer vocabulary may require fallback to multi-token disambiguation (\S\ref{sec:dynamic-masking}).
25	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 353
}
```

</details>

---


### Tool call

_source line 726 · 2026-05-19T07:55:38.955411+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_beam_search.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_beam_search.tex"
  }
}
```

</details>

---


### Tool result

_source line 727 · 2026-05-19T07:55:39.358633+00:00_

1	\section{Beam Search Compatibility}
2	\label{app:beam-search}
3	
4	OntoCoDec's constraint enforcement is designed to be decoding-strategy agnostic.
5	The main experiments (\S\ref{sec:experiments}) use greedy decoding; Appendix~\ref{app:sampling} validates nucleus sampling.
6	Here we verify compatibility with beam search, completing coverage of the three standard decoding strategies.
7	
8	\paragraph{Implementation challenges.}
9	Two stateful components require adaptation for beam search.
10	(1)~The grammar layer (XGrammar) maintains an internal \texttt{GrammarMatcher} state that tracks the generated token sequence; beam reordering invalidates this state because beams are permuted across steps.
11	Our solution instantiates a fresh \texttt{GrammarMatcher} per beam per step and replays the beam's current token sequence through XGrammar's stateless accept API (64 lines of code).
12	(2)~The semantic layer's \texttt{TypeConstraintProcessor} accumulates entity and relation registries that assume a single generation path.
13	Our solution isolates state per beam by calling \texttt{detect()} on the full partial output at each step, reconstructing all entity/relation state from scratch for each beam independently (61 lines of code).
14	Both adaptations add ${\sim}125$ lines total without modifying the existing greedy/sampling logic.
15	
16	\paragraph{Results.}
17	Table~\ref{tab:beam-search} compares beam search ($k{=}4$, \texttt{early\_stopping=True}) against greedy decoding under full S1 constraints across six model-dataset combinations.
18	
19	\begin{table}[h]
20	\centering
21	\small
22	\caption{Beam search ($k{=}4$) vs.\ greedy decoding under full S1 constraints.
23	SciERC evaluated on full test set (551 documents); DocRED evaluated on matched 50-document subsets (same documents for greedy and beam).
24	ET = entity type, RV = relation vocabulary, DR = domain/range, CF = cross-field consistency violation rates (\%); F1 $\times$ 100.}
25	\label{tab:beam-search}
26	\begin{tab
…[truncated 8172 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 403
}
```

</details>

---


### Tool call

_source line 728 · 2026-05-19T07:55:39.359218+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_full_ft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_full_ft.tex"
  }
}
```

</details>

---


### Tool result

_source line 729 · 2026-05-19T07:55:39.460193+00:00_

1	\section{Full Fine-Tuning Baseline}
2	\label{app:full-ft}
3	
4	To verify that constraint effectiveness generalizes beyond LoRA, we evaluate Qwen3-8B with full-parameter fine-tuning on SciERC (same data, 3 epochs, lr=$2{\times}10^{-4}$, seed 42).
5	
6	\begin{table}[h]
7	\centering
8	\small
9	\begin{tabular}{@{}lrrrr@{}}
10	\toprule
11	& \textbf{E-F1} & \textbf{R-F1} & \textbf{DR\%} & \textbf{CF\%} \\
12	\midrule
13	Full FT unconstrained & 64.78 & 37.89 & 2.74 & 0 \\
14	Full FT + S1 & 64.78 & 37.89 & \textbf{0} & 1.31 \\
15	\midrule
16	LoRA unconstrained & 66.86 & 43.65 & 0.31 & 0 \\
17	LoRA + S1 & 67.05 & 43.77 & \textbf{0} & 1.18 \\
18	\bottomrule
19	\end{tabular}
20	\caption{Full fine-tuning vs.\ LoRA on SciERC (Qwen3-8B, 551 docs). Constraints eliminate DR under both methods. Full FT underperforms LoRA, likely due to an untuned learning rate ($2{\times}10^{-4}$, standard for LoRA but high for full FT). F1 is unaffected by constraints in both cases.}
21	\label{tab:full-ft}
22	\end{table}
23	
24	Full fine-tuning retains 2.74\% DR violations (30 triples), concentrated in Part-of (14.6\%), Hyponym-of (9.6\%), and Evaluate-for (8.4\%). S1 eliminates all 30 violations with no F1 cost, which confirms that constraint enforcement is effective regardless of the fine-tuning method. The CF$\leftrightarrow$DR trade-off persists (CF 0\%$\to$1.31\%), consistent with the LoRA pattern (1.18\%).
25	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 730 · 2026-05-19T07:55:46.753746+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "—",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "—",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
    "output_mode": "content",
    "glob": "*.tex"
  }
}
```

</details>

---


### Tool result

_source line 731 · 2026-05-19T07:55:47.155994+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft_9b84f1.tex:1:% Section 5 — DocRED Results (Draft)
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_prompts.tex:1:% Appendix — Prompt Templates
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_crossmodel_draft.tex:1:% Section 5 — Cross-Model Validation (compressed, 830→~400 words)
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_method_draft.tex:1:% Section 3 — Method (Draft)
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion_550cbf_DEPRECATED.tex:1:% Section 7 — Conclusion
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex:1:% Appendix B — Extended Discussion
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex:354:% exp_id: p8c_ft_scierc_latency — Reviewer Report #23 verified
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_relwork_additions.tex:2:% Related Work Additions — compiled 2026-05-14
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_relwork_additions.tex:60:% STATUS: VERIFIED — paper exists and description is accurate
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion_DEPRECATED.tex:1:% Section 7 — Conclusion
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_llama_per
…[truncated 1632 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 732 · 2026-05-19T07:55:47.658559+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": " – ",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": " – ",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
    "output_mode": "content",
    "glob": "*.tex"
  }
}
```

</details>

---


### Tool result

_source line 733 · 2026-05-19T07:55:48.564916+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 906
}
```

</details>

---


### Tool call

_source line 734 · 2026-05-19T07:55:48.616010+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_sampling_table.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_sampling_table.tex"
  }
}
```

</details>

---


### Tool result

_source line 735 · 2026-05-19T07:55:49.068297+00:00_

1	\section{Sampling Robustness}\label{app:sampling}
2	
3	\begin{table}[h]
4	\centering
5	\caption{Constraint robustness under nucleus sampling ($T$=0.7, $p$=0.9) vs.\ greedy decoding (Qwen3-8B, full S1 constraints).}
6	\label{tab:sampling-robustness}
7	\begin{tabular}{llcccccc}
8	\toprule
9	Dataset & Decoding & ET\% & RV\% & DR\% & CF\% & E-F1 & R-F1 \\
10	\midrule
11	\multirow{2}{*}{SciERC (551)} & Greedy & 0 & 0 & 0.93 & 9.90 & 30.98 & 8.36 \\
12	& Sampling & 0 & 0 & 0.75 & 9.90 & 31.28 & 7.42 \\
13	\midrule
14	\multirow{2}{*}{DocRED (114$^\dagger$)} & Greedy & 0 & 0.03 & 10.21 & 2.57 & 59.37 & 8.23 \\
15	& Sampling & 0 & 0 & 10.31 & 12.63 & 57.05 & 7.92 \\
16	\bottomrule
17	\end{tabular}
18	\par\smallskip\footnotesize $^\dagger$Subset of 114 documents; full DocRED sampling requires ${\sim}300$h due to extended generation under high-temperature sampling with complex schemas.
19	\end{table}
20	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 736 · 2026-05-19T07:55:49.068716+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_doc_length.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_doc_length.tex"
  }
}
```

</details>

---


### Tool result

_source line 737 · 2026-05-19T07:55:49.622389+00:00_

1	\section{Effect of Document Length on Constraint Effectiveness}
2	\label{app:doc-length}
3	
4	To examine whether OntoCoDec's constraint effectiveness varies with document complexity, we partition test documents into three length bins (tertile split by word count) and report per-bin violation counts and F1.
5	
6	\begin{table}[h]
7	\centering
8	\small
9	\caption{Document length breakdown on SciERC (Qwen3-8B). Tertile boundaries: Short $\leq$ 19 words, Medium $\leq$ 27, Long $>$ 27.}
10	\label{tab:doc-length-scierc}
11	\begin{tabular}{ll rrrrr rr}
12	\toprule
13	\textbf{Bin} & \textbf{Mode} & \textbf{ET} & \textbf{RV} & \textbf{DR} & \textbf{CF} & \textbf{Total} & \textbf{E-F1} & \textbf{R-F1} \\
14	\midrule
15	Short (196)  & Uncon. &  1 &  5 &  57 & 0 &  63 & 32.4 &  8.9 \\
16	             & Const. &  0 &  0 &   5 & 5 &  10 & 32.4 &  8.9 \\
17	\midrule
18	Medium (180) & Uncon. &  6 &  9 & 104 & 0 & 119 & 27.8 &  6.7 \\
19	             & Const. &  0 &  0 &   7 & 15 & 22 & 27.8 &  6.7 \\
20	\midrule
21	Long (175)   & Uncon. &  3 & 10 & 104 & 1 & 118 & 29.9 &  7.0 \\
22	             & Const. &  0 &  0 &   4 & 20 & 24 & 30.0 &  7.3 \\
23	\bottomrule
24	\end{tabular}
25	\end{table}
26	
27	\begin{table}[h]
28	\centering
29	\small
30	\caption{Document length breakdown on DocRED (Qwen3-8B). Tertile boundaries: Short $\leq$ 160 words, Medium $\leq$ 208, Long $>$ 208.}
31	\label{tab:doc-length-docred}
32	\begin{tabular}{ll rrrrr rr}
33	\toprule
34	\textbf{Bin} & \textbf{Mode} & \textbf{ET} & \textbf{RV} & \textbf{DR} & \textbf{CF} & \textbf{Total} & \textbf{E-F1} & \textbf{R-F1} \\
35	\midrule
36	Short (336)  & Uncon. & 177 & 1238 & 1021 &   9 & 2445 & 61.1 &  9.3 \\
37	             & Const. &   0 &    0 &  495 & 138 &  633 & 62.6 &  9.6 \\
38	\midrule
39	Medium (332) & Uncon. & 147 & 1742 & 1047 &   5 & 2941 & 59.3 &  7.9 \\
40	             & Const. &   0 &    5 &  544 & 180 &  729 & 60.7 &  8.5 \\
41	\midrule
42	Long (330)   & Uncon. & 176 & 2209 & 1162 &   3 & 3550 & 53.9 
…[truncated 1432 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 553
}
```

</details>

---


### Tool call

_source line 738 · 2026-05-19T07:55:49.673106+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_prompt_sensitivity.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_prompt_sensitivity.tex"
  }
}
```

</details>

---


### Tool result

_source line 739 · 2026-05-19T07:55:49.774919+00:00_

1	\section{Prompt Sensitivity Analysis}
2	\label{app:prompt-sensitivity}
3	
4	To verify that OntoCoDec's constraint enforcement is robust to prompt variation, we evaluate three prompt variants on SciERC using Qwen3-8B (551 test documents): \textbf{Default} (the prompt used in all main experiments), \textbf{Minimal} (a shortened version listing only entity/relation types), and \textbf{Detailed} (an extended version with type definitions and extraction guidelines). All three variants share the same output JSON schema; only the instruction text differs. Each variant is decoded in both unconstrained and constrained (full Stage~1) modes.
5	
6	\begin{table}[h]
7	\centering
8	\small
9	\caption{Prompt sensitivity results on SciERC (Qwen3-8B, 551 documents). ET, RV, DR denote entity-type, relation-vocabulary, and domain-range violation rates (\%), respectively. $\Delta$DR shows the relative reduction from unconstrained to constrained decoding.}
10	\label{tab:prompt-sensitivity}
11	\begin{tabular}{llcccccc}
12	\toprule
13	\textbf{Prompt} & \textbf{Mode} & \textbf{ET\%} & \textbf{RV\%} & \textbf{DR\%} & \textbf{$\Delta$DR} & \textbf{E-F1} & \textbf{R-F1} \\
14	\midrule
15	\multirow{2}{*}{Default}
16	  & Unconstrained & 0.40 & 1.39 & 15.37 & \multirow{2}{*}{94.0\%} & 31.01 & 8.23 \\
17	  & Constrained   & 0.00 & 0.00 &  0.93 &                         & 30.98 & 8.36 \\
18	\midrule
19	\multirow{2}{*}{Minimal}
20	  & Unconstrained & 0.58 & 1.16 & 16.91 & \multirow{2}{*}{94.6\%} & 31.98 & 7.91 \\
21	  & Constrained   & 0.00 & 0.00 &  0.92 &                         & 31.99 & 7.85 \\
22	\midrule
23	\multirow{2}{*}{Detailed}
24	  & Unconstrained & 0.22 & 0.45 & 11.07 & \multirow{2}{*}{94.2\%} & 33.55 & 10.48 \\
25	  & Constrained   & 0.00 & 0.00 &  0.64 &                         & 33.56 & 10.48 \\
26	\bottomrule
27	\end{tabular}
28	\end{table}
29	
30	Table~\ref{tab:prompt-sensitivity} shows that constrained decoding eliminates entity-type and relation-vocabulary violations entirely (E
…[truncated 954 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 740 · 2026-05-19T07:56:00.562900+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "ing,",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
  "output_mode": "content",
  "glob": "*.tex",
  "head_limit": "30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "ing,",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
    "output_mode": "content",
    "glob": "*.tex",
    "head_limit": "30"
  }
}
```

</details>

---


### Tool result

_source line 741 · 2026-05-19T07:56:01.065401+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section1_introduction_draft.tex:8:Violations persist across the capability spectrum: 15.4\% of triples on SciERC~\cite{luan2018scierc} and 18.5\% on DocRED~\cite{yao2019docred} under zero-shot decoding, and 1--2\% even after LoRA fine-tuning; rates correlate with \emph{constraint tightness} (few valid type pairs per relation) rather than ontology or model scale.
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_doc_length.tex:69:F1 scores are preserved or slightly improved under constrained decoding, with DocRED showing +0.9--1.5 E-F1 and +0.2--0.6 R-F1 improvement in the constrained setting.
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_reproducibility.tex:6:Training uses AdamW with learning rate $2{\times}10^{-4}$, cosine schedule, warmup ratio $0.1$, effective batch size $16$, bf16 precision, gradient checkpointing, and completion-only loss for 3 epochs.
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_reproducibility.tex:18:Full S1 constrained decoding adds $+$13.1\% wall-clock overhead on SciERC and $+$2.43\% on DocRED (Qwen3-8B, zero-shot greedy); under LoRA fine-tuning, overhead is $+$10.0\% on SciERC.
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_related_work.tex:10:Outlines~\cite{willard2023outlines} reformulates constrained generation as finite-state machine transitions with offline vocabulary indexing, which enables efficient enforcement of regular-expression and JSON-schema constraints without runtime overhead per token.
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_related_wor
…[truncated 9454 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 742 · 2026-05-19T07:56:02.070267+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "checklist|responsib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
  "output_mode": "content",
  "glob": "*.tex",
  "-i": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "checklist|responsib",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
    "output_mode": "content",
    "glob": "*.tex",
    "-i": "True"
  }
}
```

</details>

---


### Tool result

_source line 743 · 2026-05-19T07:56:03.049305+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 979
}
```

</details>

---


### Tool call

_source line 744 · 2026-05-19T07:56:03.808925+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "leverage|delve|utilize|facilitate|myriad|plethora|paradigm shift|in the realm of",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
  "output_mode": "content",
  "glob": "*.tex",
  "-i": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "leverage|delve|utilize|facilitate|myriad|plethora|paradigm shift|in the realm of",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
    "output_mode": "content",
    "glob": "*.tex",
    "-i": "True"
  }
}
```

</details>

---


### Tool result

_source line 745 · 2026-05-19T07:56:03.859827+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 746 · 2026-05-19T07:56:15.313537+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/paper/*.pdf",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/paper/*.pdf",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie"
  }
}
```

</details>

---


### Tool result

_source line 747 · 2026-05-19T07:56:16.218861+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/figures/paper/fig1_overview.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/figures/paper/fig2_per_relation_dr.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/figures/paper/fig3_ablation_layers.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/ontocodec_paper_r9_final.pdf

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 905
}
```

</details>

---


### Tool call

_source line 748 · 2026-05-19T07:56:16.319782+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_llama_per_relation.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_llama_per_relation.tex"
  }
}
```

</details>

---


### Tool result

_source line 749 · 2026-05-19T07:56:16.320323+00:00_

1	% Appendix C — Per-Relation Violation Analysis (Llama-3.1-8B)
2	% exp_ids: llama_docred_unconstrained, llama_docred_full_s1
3	
4	\section{Per-Relation Violation Analysis (Llama-3.1-8B)}\label{app:llama-per-relation}
5	
6	Table~\ref{tab:llama-per-relation-dr} presents the per-relation domain--range violation breakdown for Llama-3.1-8B on DocRED under full S1 constraints.
7	The Llama baseline exhibits an RV rate of 16.03\%, substantially lower than Qwen's 29.66\%, which indicates stronger baseline vocabulary compliance.
8	% exp_ids: llama_docred_unconstrained (RV=16.03%), qwen_docred_unconstrained (RV=29.66%)
9	Full S1 completely eliminates RV violations and reduces the residual DR rate to 2.55\% (418/16{,}368 triples), with only three relations exceeding 10\%.
10	% exp_ids: llama_docred_full_s1 (DR=2.6%, 418/16368)
11	
12	\begin{table}[h]
13	\centering
14	\caption{Top 10 per-relation DR violation rates for Llama-3.1-8B on DocRED under full S1 constraints. Relations with $>$20 triples and 0\% DR (e.g., P131, P206, P361, P170, P86) are omitted.}
15	\label{tab:llama-per-relation-dr}
16	\resizebox{\columnwidth}{!}{%
17	\begin{tabular}{@{}llrrr@{}}
18	\toprule
19	Relation & PID & Triples & DR Violations & DR Rate (\%) \\
20	\midrule
21	dissolved/demolished & P576 & 73 & 24 & 32.9 \\
22	followed by          & P156 & 117 & 24 & 20.5 \\
23	unemployment rate    & P1198 & 15 & 3 & 20.0 \\
24	end time             & P582 & 130 & 21 & 16.2 \\
25	instance of          & P31  & 290 & 37 & 12.8 \\
26	product/material produced & P1056 & 98 & 11 & 11.2 \\
27	location of formation & P740 & 81 & 8 & 9.9 \\
28	head of state        & P35  & 41  & 3  & 7.3 \\
29	applies to jurisdiction & P1001 & 637 & 45 & 7.1 \\
30	conflict             & P607 & 453 & 30 & 6.6 \\
31	\bottomrule
32	\end{tabular}}
33	\end{table}
34	% exp_ids: llama_docred_full_s1
35	
36	Compared with Qwen, which retains a 10.21\% residual DR under full S1 concentrated in P1198 (83\% fallback) and P171 (78\% fallback), Llama
…[truncated 528 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 750 · 2026-05-19T07:56:24.214415+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.pdf",
  "pages": "1-10",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.pdf",
    "pages": "1-10",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 751 · 2026-05-19T07:56:27.628669+00:00_

Error: result (7,066,960 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie--claude-sessions-review-reviewer-2-cbe93d98/76a9ff9b-369a-49db-b121-ef5b7390ec30/tool-results/mcp-agent-ml-research-pdf_to_images-1779177387364.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie--claude-sessions-review-reviewer-2-cbe93d98/76a9ff9b-369a-49db-b121-ef5b7390ec30/tool-results/mcp-agent-ml-research-pdf_to_images-1779177387364.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 3414
}
```

</details>

---


### Tool call

_source line 752 · 2026-05-19T07:56:46.350893+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "pdfinfo /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.pdf 2>/dev/null | grep Pages || python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdfinfo', '/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.pdf'], capture_output=True, text=True)\nprint(result.stdout)\nprint(result.stderr)\n\" 2>/dev/null || python3 -c \"\nfrom PyPDF2 import PdfReader\nr = PdfReader('/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.pdf')\nprint(f'Pages: {len(r.pages)}')\n\"",
  "description": "Check PDF page count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Bash",
  "tool_args": {
    "command": "pdfinfo /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.pdf 2>/dev/null | grep Pages || python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdfinfo', '/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.pdf'], capture_output=True, text=True)\nprint(result.stdout)\nprint(result.stderr)\n\" 2>/dev/null || python3 -c \"\nfrom PyPDF2 import PdfReader\nr = PdfReader('/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.pdf')\nprint(f'Pages: {len(r.pages)}')\n\"",
    "description": "Check PDF page count"
  }
}
```

</details>

---


### Tool result

_source line 753 · 2026-05-19T07:56:46.553491+00:00_

Pages:           27

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Bash",
  "elapsed_ms": 202
}
```

</details>

---


### Tool call

_source line 754 · 2026-05-19T07:56:55.144989+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.pdf",
  "pages": "7-9",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.pdf",
    "pages": "7-9",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 755 · 2026-05-19T07:56:56.271005+00:00_

Error: result (2,143,129 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie--claude-sessions-review-reviewer-2-cbe93d98/76a9ff9b-369a-49db-b121-ef5b7390ec30/tool-results/mcp-agent-ml-research-pdf_to_images-1779177416202.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie--claude-sessions-review-reviewer-2-cbe93d98/76a9ff9b-369a-49db-b121-ef5b7390ec30/tool-results/mcp-agent-ml-research-pdf_to_images-1779177416202.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1126
}
```

</details>

---


### Tool call

_source line 756 · 2026-05-19T07:57:00.906788+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nfrom PyPDF2 import PdfReader\nr = PdfReader('/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.pdf')\nfor i, page in enumerate(r.pages[:15], 1):\n    text = page.extract_text()[:200] if page.extract_text() else ''\n    print(f'Page {i}: {text[:150]}...')\n\"",
  "description": "Extract page text headers to identify section boundaries"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nfrom PyPDF2 import PdfReader\nr = PdfReader('/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.pdf')\nfor i, page in enumerate(r.pages[:15], 1):\n    text = page.extract_text()[:200] if page.extract_text() else ''\n    print(f'Page {i}: {text[:150]}...')\n\"",
    "description": "Extract page text headers to identify section boundaries"
  }
}
```

</details>

---


### Tool result

_source line 757 · 2026-05-19T07:57:01.158368+00:00_

Exit code 1
Traceback (most recent call last):
  File "&lt;string>", line 2, in &lt;module>
    from PyPDF2 import PdfReader
ModuleNotFoundError: No module named 'PyPDF2'

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Bash",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 758 · 2026-05-19T07:57:07.074912+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport fitz  # PyMuPDF\ndoc = fitz.open('/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.pdf')\nfor i in range(min(15, len(doc))):\n    text = doc[i].get_text()[:200]\n    print(f'Page {i+1}: {text[:150].replace(chr(10), \\\" | \\\")}')\n\" 2>/dev/null || pip install pymupdf -q && python3 -c \"\nimport fitz\ndoc = fitz.open('/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.pdf')\nfor i in range(min(15, len(doc))):\n    text = doc[i].get_text()[:200]\n    print(f'Page {i+1}: {text[:150].replace(chr(10), \\\" | \\\")}')\n\"",
  "description": "Extract page headers to find section boundaries"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport fitz  # PyMuPDF\ndoc = fitz.open('/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.pdf')\nfor i in range(min(15, len(doc))):\n    text = doc[i].get_text()[:200]\n    print(f'Page {i+1}: {text[:150].replace(chr(10), \\\" | \\\")}')\n\" 2>/dev/null || pip install pymupdf -q && python3 -c \"\nimport fitz\ndoc = fitz.open('/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.pdf')\nfor i in range(min(15, len(doc))):\n    text = doc[i].get_text()[:200]\n    print(f'Page {i+1}: {text[:150].replace(chr(10), \\\" | \\\")}')\n\"",
    "description": "Extract page headers to find section boundaries"
  }
}
```

</details>

---


### Tool result

_source line 759 · 2026-05-19T07:57:08.029035+00:00_

Page 1: OntoCoDec: Type-Constrained Information Extraction | via Compiled Ontology Constraints | Anonymous ACL submission | Abstract | 001 | We present ONTOCODEC, which
Page 2: mantic layer maintains a stateful entity registry | 084 | during generation: as entities are decoded, the | 085 | registry records type assignments; when rela
Page 3: (1) entity types are inferred from free text rather | 181 | than declared annotations, (2) the entity registry is | 182 | built dynamically during generation,
Page 4: Tail type masking. | At a TAILTYPE position, | 272 | the head type τ h | j | is already determined from | 273 | the decoded prefix. | The processor computes | 274 | range
Page 5: grammar layer becomes a no-op and the seman- | 365 | tic layer alone reduces residual DR by 39–72% | 366 | (§5.1). | 367 | 5 | Experiments | 368 | We evaluate OntoCoDec
Page 6: Model | Setting | Mode | DR ↓ | CF R-F1 ↑E-F1 ↑ | ∆DR | Qwen3-8B | Zero-shot Unconstr. 15.37 0.08 | 8.23 | 31.01 | — | Full S1 | 0.93 9.90 | 8.36 | 30.98 | ↓94% | LoRA | Unconstr. | 1.95
Page 7: Violation Rates (%) | F1 | Model | Mode | EV ↓RoV ↓ | AC | CF Trig. ↑Ent. ↑ | Qwen3-8B | Unconstr. | 24.0 | 74.9 | 0.3 | 0 | 11.8 | 0 | Grammar | 0 | 76.1 | 8.2 | — | — | — | Full S1 | 0 | 0 | 2.1 21.
Page 8: masking; JSONSchemaBench (Geng et al., 2025) | 576 | benchmarks these systems. | GCD (Geng et al., | 577 | 2023) applies grammar constraints to IE tasks. In | 578
Page 9: Limitations | 663 | Constraint | scope. | CF | impact | is | model- | 664 | dependent: | for well-calibrated models (Qwen, | 665 | Llama), S1 introduces CF violations (up to | 
Page 10: Luca Beurer-Kellner, Marc Fischer, and Martin Vechev. | 764 | 2024. | Guiding LLMs the right way: Fast, non- | 765 | invasive constrained generation. In Proceed
Page 11: Lecture Notes in Computer Science, pages 382–398. | 877 | Springer. | 878 | Niels Mündler, Jingxuan He, Hao Wang, Koushik | 879 | Sen, Dawn Song, and Martin Veche
Page 12: Yufeng Chen, Meishan Zhang, Yo
…[truncated 3265 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Bash",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 760 · 2026-05-19T07:57:35.205508+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/paper/*checklist*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/paper/*checklist*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie"
  }
}
```

</details>

---


### Tool result

_source line 761 · 2026-05-19T07:57:35.257047+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 762 · 2026-05-19T07:57:35.357865+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/paper/*responsible*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/paper/*responsible*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie"
  }
}
```

</details>

---


### Tool result

_source line 763 · 2026-05-19T07:57:35.458811+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 764 · 2026-05-19T08:00:25.557029+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 审稿意见 — Round 10\n\n**论文**: OntoCoDec: Type-Constrained Information Extraction via Compiled Ontology Constraints\n**Venue**: EMNLP 2026 via ACL Rolling Review\n**审查侧重**: 新颖性 + 论文完整性 + 写作质量 + 格式合规\n\n---\n\n## Summary\n\n本文提出 OntoCoDec，一个将 IE 本体 schema 编译为两层 token-level 解码约束的框架：grammar layer（基于 XGrammar）保证 JSON 结构和词汇合法性，semantic layer 通过有状态 entity registry 和动态 logit masking 强制 domain/range 类型约束。在 3 个数据集（SciERC、DocRED、WikiEvents）、4 个模型（8B-70B）上进行了全面评估，展示了 zero-shot 下 DR 降低 42-99%（校准模型）和 fine-tuning 下近无损组合性（DR ≤ 0.20%，R-F1 ± 0.6pp）的结果。论文实验设计扎实、分析诚实（尤其是 CF trade-off 的处理），但新颖性偏增量、CF 限制削弱了核心承诺、且缺少 Responsible NLP Checklist。\n\n---\n\n## Strengths\n\n**[S1] 清晰的问题定义与系统化的违规分类学**\n四类违规（DR/RV/ET/CF）的定义和测量体系清晰完备，constraint tightness κ(r) 提供了跨数据集可比较的分析框架。问题本身有实际意义：即使 LoRA 微调后仍存在 1-2% 的残余 DR 违规（Table 2），说明仅靠训练无法完全消除类型错误。\n\n**[S2] 实验覆盖面广、方法论严谨**\n3 个 IE 任务/数据集、4 个模型（3 个 tokenizer 家族）、3 种解码策略（greedy/sampling/beam）、zero-shot + fine-tuning 两种范式的全面评估。Bootstrap 显著性检验（10,000 iterations）用于所有 F1 比较。消融实验（five-way on SciERC，four-way on DocRED，fine-tuned four-way）充分隔离了各层贡献。\n\n**[S3] 诚实的局限性分析**\nCF trade-off 的处理非常透明：Table 8（CF fallback ablation）清楚展示了 CF↔DR 的 Pareto 关系，论文没有回避 zero-shot 下 CF 从 0.08% 升至 9.90% 的事实。对 Mistral 作为 boundary condition 的处理也是恰当的——承认模型校准不足时约束效果有限。\n\n**[S4] Fine-tuning 组合性结果清晰有力**\nLoRA + S1 在所有 4 个 model×dataset 组合上达到 DR ≤ 0.20%、R-F1 ± 0.6pp 的近无损组合（Table 2），这是论文最强的贡献点。Beam search + LoRA 在 SciERC 上消除所有四类违规（Appendix G）进一步强化了这一结论。\n\n**[S5] 写作质量良好**\n主文无 em-dash、无 AI 黑名单用词，段落结构自然，不过度分段。Abstract 在 ~190 words 内回答了四个必答问题。Introduction 遵循\"背景→问题→不足→方法→贡献\"结构，叙事连贯。\n\n---\n\n## Weaknesses\n\n**[W1] [Must-Fix] 缺少 Responsible NLP Research Checklist**\nARR 要求所有提交必须包含 Responsible NLP Research Checklist（已在全部 .tex 文件中搜索 \"checklist\" 和 \"responsib\"，结果为空）。这是格式合规的硬性要求，缺失可能导致 desk reject。\n\n**[W2] [Should-Fix] Zero-shot 下 CF trade-off 削弱核心 claim**\n论文标题和 Abstract 宣称 \"type-constrained IE\"，但在 zero-shot 设置下，总类型违规 (DR+CF) 改善有限：SciERC 从 15.45% 降至 10.83%（Table 1），DocRED 从 18.56% 降至 12.78%（Table 3）。CF 从近零升至 9.90%（SciERC）和 12.02%（Llama DocRED），意味着约束系统\"解决\"了一种违规但\"引入\"了另一种。虽然 fine-tuning 下 CF 降至 ≤1.18%，但论文需要更明确地在 Abstract 和 Introduction 中框架化 zero-shot 仅为 stress test 而非目标部署配置。当前 Abstract 第 3-4 句对 zero-shot CF 的提及 (\"with an accompanying CF increase (9-21% zero-shot, resolved to ≤1.2% by fine-tuning)\") 读起来像是在解释局限，而非讲故事。\n\n**[W3] [Should-Fix] 新颖性偏增量**\n- Grammar layer 直接复用 XGrammar，无技术贡献；\n- Semantic layer 的核心机制（prefix-conditioned logit masking + entity registry）虽然在 IE 语境下是新的，但从 constrained decoding 文献（Synchromesh, PICARD, PLDI 2025 type-constrained codegen）来看，是已有范式向新领域的移植；\n- 论文自身的 Extended Related Work（Appendix B）承认 PLDI 2025 work \"is the closest mechanistic analog to OntoCoDec, applying the same 'type system → automaton → logits mask' pipeline\"，区别仅在于 IE 需要动态 entity registry 而非静态类型声明。这个区分是否构成足够的新颖性？我认为是有实际贡献的，但整体是增量性的。\n\n**[W4] [Should-Fix] WikiEvents 评估过于初步**\n20-document test set 产生的置信区间极宽：trigger F1 shift -5.4pp（Qwen LoRA + S1 vs. LoRA unconstrained）在如此小的样本上不具统计意义。论文将此列入 Contribution 4 (\"Preliminary extension to event extraction\")，但如果结果不稳定，放入贡献列表可能误导审稿人。建议降级为 Discussion 中的 exploratory 结果，或增加 dev set 评估。\n\n**[W5] [Should-Fix] 缺少下游任务评估**\nLimitations section 提到 \"CF type inconsistencies may propagate to downstream tasks... the impact of such propagation has not been evaluated\"。对于一个以 type safety 为核心卖点的论文，缺少 KG construction 或 QA 等下游任务的端到端评估是明显的缺口。至少需要一个 ablation 展示 type-valid triples vs. all triples 在 downstream 的差异。\n\n**[W6] [Should-Fix] §7 Discussion and Conclusion 过短**\n仅约 150 words、3 段，更像 Summary 而非 Discussion。缺少：(1) 与 supervised SOTA（R-F1 49-53% on SciERC, 来自 Appendix B 引用的 Zhong 2021 和 Ye 2022）的 R-F1 对比讨论；(2) 对 constraint tightness 作为设计指导的讨论（何时应/不应使用 OntoCoDec）；(3) 对 training-free vs. training-based 方法组合的更具体路线图。EMNLP 长论文读者期望在 Discussion 中看到更深入的洞察。\n\n**[W7] [Minor] Abstract 数据密度过高**\nAbstract 在 ~190 words 中嵌入了至少 10 个数字/百分比（DR ≤ 0.20%、R-F1 ± 0.6pp、76-99%、9-21%、≤1.2%、$k=4$、8B-70B 等）。审稿人在 30 秒内难以消化这些数字。建议精简到 3-4 个关键数字，将其余移入 Introduction。\n\n**[W8] [Minor] BibTeX 有 14 个 orphan 条目和多个重复**\n引用审计发现 14 个未被 cite 的 bib 条目（包括 cabot2021rebel、dccd2026、guidex2025 等），且存在重复条目（formattax2026/lee2026formattax、boostcd2025/sakota2025boostcd、slot2025/shen2025slot 等为同一论文的重复 key）。1 个 duplicate key (schall2025hiddencost)。regino2025kgcurator 在 OpenAlex 上未找到匹配。这些不影响接收决定但应清理。\n\n**[W9] [Minor] Dual-factor pattern 的统计基础薄弱**\n线性拟合 $y = 0.366x - 0.138$ 基于仅 4 个数据点（df=2），$p ≈ 0.058 > 0.05$（Appendix B, Figure 1）。论文正确标注为 \"descriptive characterization\"，但在 §4 和 Abstract 中仍较突出地引用 \"constraint tightness\" 作为 violation rate 的 predictor。考虑到证据强度，应降低措辞的确定性。\n\n---\n\n## Questions\n\n**[Q1]** Constraint tightness $\\kappa(r) = 1 - |\\sigma(r)|/|\\mathcal{E}|^2$（Eq. 2）将分母设为 $|\\mathcal{E}|^2$，包括 self-pair 和反向 pair。这是否是正确的归一化？对于有方向性的关系，$|\\mathcal{E}|^2$ 是合适的上界；但对于对称关系（如 Conjunction），$|\\mathcal{E}| \\times (|\\mathcal{E}|+1)/2$ 可能更精确。这会影响 tightness 值和 dual-factor pattern 的拟合吗？\n\n**[Q2]** Table 2 Composability 部分报告 DocRED 的结果仅以文字形式给出（\"Qwen DR −99%, Llama DR −59%\"），但 DocRED fine-tuning 的完整 ablation（包括 CF 和 F1）只出现在 Appendix B Table 11。为什么不在主表中包含 DocRED fine-tuning 行？当前的 caption (\"DocRED: Qwen DR −99%, Llama DR −59%\") 不够 self-contained。\n\n**[Q3]** Entity F1 在 Limitations 中被报告为 model-dependent（Qwen +1.22pp vs. Llama -0.64pp on DocRED），且部分归因于 parse failure 增加（Llama: 9.1% vs 6.8%）。约束为什么会增加 parse failure？这是 grammar layer 和 LM logits 之间的冲突导致的退化生成吗？\n\n**[Q4]** WikiEvents fine-tuning 中 Qwen trigger F1 下降 5.4pp 的原因是什么？如果约束不影响 trigger extraction（trigger 是事件类型分配，非实体类型），这个下降不应该由 OntoCoDec 引起。是否有 confound（如不同的 LoRA 训练 run）？\n\n---\n\n## Missing References\n\n- **SchemaRL** (Lu et al., ACL 2025) — 在 bib 中但未 cite，与 schema-constrained generation 直接相关\n- **GUIDEX** (De La Fuente et al., ACL 2025 Findings) — 在 bib 中但未 cite，zero-shot IE 的 schema-aware 数据增强\n- **DCCD** (Reddy et al., 2026) — draft-conditioned constrained decoding，与方法直接相关\n- **REBEL** (Cabot & Navigli, EMNLP 2021 Findings) — 经典 end-to-end RE 工作，Related Work 中未引用但在 bib 中存在\n- 考虑引用 **Li et al. (NeurIPS 2023) \"GPT-RE\"** 或类似 LLM-based RE 的近期 benchmark 工作\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 方法论扎实，实验设计严谨，但 CF trade-off 部分削弱了 \"type-constrained\" 的核心 claim；zero-shot 下总违规仅降低约 30%（15.45→10.83 on SciERC）。Fine-tuning 组合性结果是可靠的。 |\n| Excitement | 3.0/5 | 填补了 grammar-constrained decoding 和 schema-aware IE 之间的空白，有实际应用价值，但核心技术是已有范式的领域移植，增量性较强。 |\n| Reproducibility | 4.5/5 | 提供了完整的 LoRA 超参数、硬件配置、prompt templates、runtime profiling。代码承诺在接收后释放。唯一扣分：未提供 constraint compilation 代码的伪代码或算法描述。 |\n| Confidence | 4/5 | 我仔细阅读了全文含所有附录，验证了引用，熟悉 constrained decoding 和 IE 文献。 |\n\n---\n\n## Overall Assessment\n\n**Score: 3.5 (Borderline Conference)**\n**Confidence: 4/5**\n\n本文解决了一个真实存在的问题（LLM-based IE 中的本体类型违规），方案设计合理、实验全面、分析诚实。Fine-tuning 组合性结果（DR ≤ 0.20%，R-F1 ± 0.6pp）是有说服力的，beam search 消除所有违规类型的发现也令人印象深刻。然而，几个因素阻止了我给出更高评分：\n\n1. **新颖性偏增量**：核心机制是已有 constrained decoding 技术向 IE 的移植，grammar layer 完全复用 XGrammar；\n2. **CF trade-off 在 zero-shot 下显著**：总违规改善有限，削弱了标题中 \"type-constrained\" 的承诺；\n3. **WikiEvents 评估过于初步**，但已列入贡献；\n4. **缺少 Responsible NLP Checklist**（格式硬伤，需立即修复）；\n5. **Discussion 过短**，缺乏与 supervised SOTA 的 R-F1 对比和更深入的方法论洞察。\n\n如果作者能 (a) 补充 checklist，(b) 在 Abstract/Intro 中更明确地将 fine-tuning 定位为主要贡献、zero-shot 为 stress test，(c) 扩展 Discussion，(d) 将 WikiEvents 降级为 exploratory，该论文可以达到 Conference 水平。当前版本更适合 Findings。",
  "reviewer_id": "2",
  "project": "schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 审稿意见 — Round 10\n\n**论文**: OntoCoDec: Type-Constrained Information Extraction via Compiled Ontology Constraints\n**Venue**: EMNLP 2026 via ACL Rolling Review\n**审查侧重**: 新颖性 + 论文完整性 + 写作质量 + 格式合规\n\n---\n\n## Summary\n\n本文提出 OntoCoDec，一个将 IE 本体 schema 编译为两层 token-level 解码约束的框架：grammar layer（基于 XGrammar）保证 JSON 结构和词汇合法性，semantic layer 通过有状态 entity registry 和动态 logit masking 强制 domain/range 类型约束。在 3 个数据集（SciERC、DocRED、WikiEvents）、4 个模型（8B-70B）上进行了全面评估，展示了 zero-shot 下 DR 降低 42-99%（校准模型）和 fine-tuning 下近无损组合性（DR ≤ 0.20%，R-F1 ± 0.6pp）的结果。论文实验设计扎实、分析诚实（尤其是 CF trade-off 的处理），但新颖性偏增量、CF 限制削弱了核心承诺、且缺少 Responsible NLP Checklist。\n\n---\n\n## Strengths\n\n**[S1] 清晰的问题定义与系统化的违规分类学**\n四类违规（DR/RV/ET/CF）的定义和测量体系清晰完备，constraint tightness κ(r) 提供了跨数据集可比较的分析框架。问题本身有实际意义：即使 LoRA 微调后仍存在 1-2% 的残余 DR 违规（Table 2），说明仅靠训练无法完全消除类型错误。\n\n**[S2] 实验覆盖面广、方法论严谨**\n3 个 IE 任务/数据集、4 个模型（3 个 tokenizer 家族）、3 种解码策略（greedy/sampling/beam）、zero-shot + fine-tuning 两种范式的全面评估。Bootstrap 显著性检验（10,000 iterations）用于所有 F1 比较。消融实验（five-way on SciERC，four-way on DocRED，fine-tuned four-way）充分隔离了各层贡献。\n\n**[S3] 诚实的局限性分析**\nCF trade-off 的处理非常透明：Table 8（CF fallback ablation）清楚展示了 CF↔DR 的 Pareto 关系，论文没有回避 zero-shot 下 CF 从 0.08% 升至 9.90% 的事实。对 Mistral 作为 boundary condition 的处理也是恰当的——承认模型校准不足时约束效果有限。\n\n**[S4] Fine-tuning 组合性结果清晰有力**\nLoRA + S1 在所有 4 个 model×dataset 组合上达到 DR ≤ 0.20%、R-F1 ± 0.6pp 的近无损组合（Table 2），这是论文最强的贡献点。Beam search + LoRA 在 SciERC 上消除所有四类违规（Appendix G）进一步强化了这一结论。\n\n**[S5] 写作质量良好**\n主文无 em-dash、无 AI 黑名单用词，段落结构自然，不过度分段。Abstract 在 ~190 words 内回答了四个必答问题。Introduction 遵循\"背景→问题→不足→方法→贡献\"结构，叙事连贯。\n\n---\n\n## Weaknesses\n\n**[W1] [Must-Fix] 缺少 Responsible NLP Research Checklist**\nARR 要求所有提交必须包含 Responsible NLP Research Checklist（已在全部 .tex 文件中搜索 \"checklist\" 和 \"responsib\"，结果为空）。这是格式合规的硬性要求，缺失可能导致 desk reject。\n\n**[W2] [Should-Fix] Zero-shot 下 CF trade-off 削弱核心 claim**\n论文标题和 Abstract 宣称 \"type-constrained IE\"，但在 zero-shot 设置下，总类型违规 (DR+CF) 改善有限：SciERC 从 15.45% 降至 10.83%（Table 1），DocRED 从 18.56% 降至 12.78%（Table 3）。CF 从近零升至 9.90%（SciERC）和 12.02%（Llama DocRED），意味着约束系统\"解决\"了一种违规但\"引入\"了另一种。虽然 fine-tuning 下 CF 降至 ≤1.18%，但论文需要更明确地在 Abstract 和 Introduction 中框架化 zero-shot 仅为 stress test 而非目标部署配置。当前 Abstract 第 3-4 句对 zero-shot CF 的提及 (\"with an accompanying CF increase (9-21% zero-shot, resolved to ≤1.2% by fine-tuning)\") 读起来像是在解释局限，而非讲故事。\n\n**[W3] [Should-Fix] 新颖性偏增量**\n- Grammar layer 直接复用 XGrammar，无技术贡献；\n- Semantic layer 的核心机制（prefix-conditioned logit masking + entity registry）虽然在 IE 语境下是新的，但从 constrained decoding 文献（Synchromesh, PICARD, PLDI 2025 type-constrained codegen）来看，是已有范式向新领域的移植；\n- 论文自身的 Extended Related Work（Appendix B）承认 PLDI 2025 work \"is the closest mechanistic analog to OntoCoDec, applying the same 'type system → automaton → logits mask' pipeline\"，区别仅在于 IE 需要动态 entity registry 而非静态类型声明。这个区分是否构成足够的新颖性？我认为是有实际贡献的，但整体是增量性的。\n\n**[W4] [Should-Fix] WikiEvents 评估过于初步**\n20-document test set 产生的置信区间极宽：trigger F1 shift -5.4pp（Qwen LoRA + S1 vs. LoRA unconstrained）在如此小的样本上不具统计意义。论文将此列入 Contribution 4 (\"Preliminary extension to event extraction\")，但如果结果不稳定，放入贡献列表可能误导审稿人。建议降级为 Discussion 中的 exploratory 结果，或增加 dev set 评估。\n\n**[W5] [Should-Fix] 缺少下游任务评估**\nLimitations section 提到 \"CF type inconsistencies may propagate to downstream tasks... the impact of such propagation has not been evaluated\"。对于一个以 type safety 为核心卖点的论文，缺少 KG construction 或 QA 等下游任务的端到端评估是明显的缺口。至少需要一个 ablation 展示 type-valid triples vs. all triples 在 downstream 的差异。\n\n**[W6] [Should-Fix] §7 Discussion and Conclusion 过短**\n仅约 150 words、3 段，更像 Summary 而非 Discussion。缺少：(1) 与 supervised SOTA（R-F1 49-53% on SciERC, 来自 Appendix B 引用的 Zhong 2021 和 Ye 2022）的 R-F1 对比讨论；(2) 对 constraint tightness 作为设计指导的讨论（何时应/不应使用 OntoCoDec）；(3) 对 training-free vs. training-based 方法组合的更具体路线图。EMNLP 长论文读者期望在 Discussion 中看到更深入的洞察。\n\n**[W7] [Minor] Abstract 数据密度过高**\nAbstract 在 ~190 words 中嵌入了至少 10 个数字/百分比（DR ≤ 0.20%、R-F1 ± 0.6pp、76-99%、9-21%、≤1.2%、$k=4$、8B-70B 等）。审稿人在 30 秒内难以消化这些数字。建议精简到 3-4 个关键数字，将其余移入 Introduction。\n\n**[W8] [Minor] BibTeX 有 14 个 orphan 条目和多个重复**\n引用审计发现 14 个未被 cite 的 bib 条目（包括 cabot2021rebel、dccd2026、guidex2025 等），且存在重复条目（formattax2026/lee2026formattax、boostcd2025/sakota2025boostcd、slot2025/shen2025slot 等为同一论文的重复 key）。1 个 duplicate key (schall2025hiddencost)。regino2025kgcurator 在 OpenAlex 上未找到匹配。这些不影响接收决定但应清理。\n\n**[W9] [Minor] Dual-factor pattern 的统计基础薄弱**\n线性拟合 $y = 0.366x - 0.138$ 基于仅 4 个数据点（df=2），$p ≈ 0.058 > 0.05$（Appendix B, Figure 1）。论文正确标注为 \"descriptive characterization\"，但在 §4 和 Abstract 中仍较突出地引用 \"constraint tightness\" 作为 violation rate 的 predictor。考虑到证据强度，应降低措辞的确定性。\n\n---\n\n## Questions\n\n**[Q1]** Constraint tightness $\\kappa(r) = 1 - |\\sigma(r)|/|\\mathcal{E}|^2$（Eq. 2）将分母设为 $|\\mathcal{E}|^2$，包括 self-pair 和反向 pair。这是否是正确的归一化？对于有方向性的关系，$|\\mathcal{E}|^2$ 是合适的上界；但对于对称关系（如 Conjunction），$|\\mathcal{E}| \\times (|\\mathcal{E}|+1)/2$ 可能更精确。这会影响 tightness 值和 dual-factor pattern 的拟合吗？\n\n**[Q2]** Table 2 Composability 部分报告 DocRED 的结果仅以文字形式给出（\"Qwen DR −99%, Llama DR −59%\"），但 DocRED fine-tuning 的完整 ablation（包括 CF 和 F1）只出现在 Appendix B Table 11。为什么不在主表中包含 DocRED fine-tuning 行？当前的 caption (\"DocRED: Qwen DR −99%, Llama DR −59%\") 不够 self-contained。\n\n**[Q3]** Entity F1 在 Limitations 中被报告为 model-dependent（Qwen +1.22pp vs. Llama -0.64pp on DocRED），且部分归因于 parse failure 增加（Llama: 9.1% vs 6.8%）。约束为什么会增加 parse failure？这是 grammar layer 和 LM logits 之间的冲突导致的退化生成吗？\n\n**[Q4]** WikiEvents fine-tuning 中 Qwen trigger F1 下降 5.4pp 的原因是什么？如果约束不影响 trigger extraction（trigger 是事件类型分配，非实体类型），这个下降不应该由 OntoCoDec 引起。是否有 confound（如不同的 LoRA 训练 run）？\n\n---\n\n## Missing References\n\n- **SchemaRL** (Lu et al., ACL 2025) — 在 bib 中但未 cite，与 schema-constrained generation 直接相关\n- **GUIDEX** (De La Fuente et al., ACL 2025 Findings) — 在 bib 中但未 cite，zero-shot IE 的 schema-aware 数据增强\n- **DCCD** (Reddy et al., 2026) — draft-conditioned constrained decoding，与方法直接相关\n- **REBEL** (Cabot & Navigli, EMNLP 2021 Findings) — 经典 end-to-end RE 工作，Related Work 中未引用但在 bib 中存在\n- 考虑引用 **Li et al. (NeurIPS 2023) \"GPT-RE\"** 或类似 LLM-based RE 的近期 benchmark 工作\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 方法论扎实，实验设计严谨，但 CF trade-off 部分削弱了 \"type-constrained\" 的核心 claim；zero-shot 下总违规仅降低约 30%（15.45→10.83 on SciERC）。Fine-tuning 组合性结果是可靠的。 |\n| Excitement | 3.0/5 | 填补了 grammar-constrained decoding 和 schema-aware IE 之间的空白，有实际应用价值，但核心技术是已有范式的领域移植，增量性较强。 |\n| Reproducibility | 4.5/5 | 提供了完整的 LoRA 超参数、硬件配置、prompt templates、runtime profiling。代码承诺在接收后释放。唯一扣分：未提供 constraint compilation 代码的伪代码或算法描述。 |\n| Confidence | 4/5 | 我仔细阅读了全文含所有附录，验证了引用，熟悉 constrained decoding 和 IE 文献。 |\n\n---\n\n## Overall Assessment\n\n**Score: 3.5 (Borderline Conference)**\n**Confidence: 4/5**\n\n本文解决了一个真实存在的问题（LLM-based IE 中的本体类型违规），方案设计合理、实验全面、分析诚实。Fine-tuning 组合性结果（DR ≤ 0.20%，R-F1 ± 0.6pp）是有说服力的，beam search 消除所有违规类型的发现也令人印象深刻。然而，几个因素阻止了我给出更高评分：\n\n1. **新颖性偏增量**：核心机制是已有 constrained decoding 技术向 IE 的移植，grammar layer 完全复用 XGrammar；\n2. **CF trade-off 在 zero-shot 下显著**：总违规改善有限，削弱了标题中 \"type-constrained\" 的承诺；\n3. **WikiEvents 评估过于初步**，但已列入贡献；\n4. **缺少 Responsible NLP Checklist**（格式硬伤，需立即修复）；\n5. **Discussion 过短**，缺乏与 supervised SOTA 的 R-F1 对比和更深入的方法论洞察。\n\n如果作者能 (a) 补充 checklist，(b) 在 Abstract/Intro 中更明确地将 fine-tuning 定位为主要贡献、zero-shot 为 stress test，(c) 扩展 Discussion，(d) 将 WikiEvents 降级为 exploratory，该论文可以达到 Conference 水平。当前版本更适合 Findings。",
    "reviewer_id": "2",
    "project": "schema_semantic_constrained_ie"
  }
}
```

</details>

---


### Tool result

_source line 765 · 2026-05-19T08:00:30.188470+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_01fc90ae186a4ed432770f7601995139:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4631
}
```

</details>

---


### Assistant

_source line 766 · 2026-05-19T08:00:38.050408+00:00_

审稿意见已提交给 Review Director。

**审稿结论**：Score 3.5 (Borderline Conference)，Confidence 4/5。

核心判断：
- 论文解决真实问题，实验覆盖全面、分析诚实，fine-tuning 组合性结果有力（DR ≤ 0.20%，R-F1 ± 0.6pp）
- 主要问题：新颖性偏增量（已有 constrained decoding 的领域移植）、zero-shot CF trade-off 削弱核心 claim、缺少 Responsible NLP Checklist（格式硬伤）、WikiEvents 评估过于初步、Discussion 过短
- Must-Fix：补充 ARR 要求的 checklist
- 建议修改方向：明确 fine-tuning 为主要贡献/zero-shot 为 stress test、扩展 Discussion、清理 BibTeX 冗余条目

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2"
}
```

</details>

---


## Round 17

## Round 17

4 recorded events


### User

_source line 767 · 2026-05-19T08:01:09.653115+00:00_

[Round 10 审稿请求]:
## 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见

以下是 Reviewer 1 的完整审稿意见。请逐条回应每个 Weakness 和 Question：
- **[AGREE]** 同意并说明理由
- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）

---

### Reviewer 1 Weaknesses:

**[W1] [Must-Fix] "Ontology Constraints" framing 与实际实现不匹配。**
SciERC/DocRED 的约束表从训练数据类型对共现提取，非形式本体。只有 WikiEvents 用 KAIROS。标题 "Compiled Ontology Constraints" 是 overclaim。§2 承认了但标题/Abstract 措辞暗示形式本体。建议替换术语或明确区分两种约束来源。

**[W2] [Must-Fix] Dual-factor pattern 统计支撑不足。**
n=4, df=2, p≈0.058。作为 Contribution #1 的 "systematic study" 统计上不严谨。建议增加数据点或降低 claim 强度。

**[W3] [Must-Fix] WikiEvents EE "preliminary" 但在 Abstract/Contribution 中权重过高。**
20-doc test set，trigger F1 CI 很宽。标注 "preliminary" 但列为 Contribution #4。建议降级或重新定位。

**[W4] [Should-Fix] 缺少关键 baseline 对比。**
(a) GoLLIE/KnowCoder 无实验验证互补性；(b) Grammar-only ≠ GCD 官方实现；(c) Post-hoc filtering 在 5/6 ZS 设置中 F1 更高但仅在附录。

**[W5] [Should-Fix] "Near-lossless composability" claim 在考虑 CF 后需重新审视。**
CF 从 0% 升至 1.18%（FT）或 9.90%（ZS）。Tot. 15.45%→10.83%。"Near-lossless" 应限定范围。

**[W6] [Should-Fix] DocRED beam search 仅 50 docs。**
Clopper-Pearson 95% CI 上限 5.8%。§5.6 措辞可能被误读为包含 DocRED。

**[W7] [Should-Fix] Zero-shot 占据大量实验空间但实用价值有限。**
ZS R-F1 2-8%。§5 中 3/4 subsection 主要展示 ZS。FT composability 应更突出。

**[W8] [Minor] Bootstrap CI 未在主表报告。**

**[W9] [Minor] BibTeX orphan/duplicate entries。**

### Reviewer 1 Questions:

**[Q1]** Entity registry 错误传播的频率和影响未系统量化。
**[Q2]** 对多义类型实体，entity registry 是否过于刚性？
**[Q3]** κ(r) 归一化方式是否合适（|E|² 包括不出现的组合）？
**[Q4]** GoLLIE 在 SciERC 上的残余违约率？互补性的实验证据？

---

请对每条 Weakness 和 Question 给出 [AGREE] 或 [REBUT] 回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 768 · 2026-05-19T08:03:07.874402+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 交叉回应 — Reviewer 1 审稿意见\n\n---\n\n### Weaknesses 回应\n\n**[AGREE] R1-W1: \"Ontology Constraints\" framing 与实际实现不匹配**\n\n同意这是一个需要修复的 framing 问题。§2 Background 第一段明确承认：\"We define ontology constraints broadly to encompass both formal ontology specifications (e.g., the KAIROS event ontology) and empirically derived type-pair constraints extracted from annotated training data\"，并指出 \"The latter applies when datasets lack a formal ontology but provide typed annotations (SciERC, DocRED)\"。这说明作者自己知道两种来源的区别，但标题 \"Compiled Ontology Constraints\" 确实暗示了形式本体。\n\n补充发现：SciERC/DocRED 的经验约束覆盖率数据在 §2 中报告为 \"99%+ instance-level coverage on held-out data (SciERC 99.0%, DocRED 99.4%)\"，且 Limitations 提到 \"Schema coverage gaps (one-third of residual violations) arise because RE constraints are extracted from training-data type pairs, which may not cover all valid combinations\"。这进一步证实了经验约束的有限性——真正的形式本体不会有 coverage gaps。建议标题改为 \"Schema-Constrained\" 或 \"Type-Constrained\"（后者已在标题副标题中使用），并在 §2 更突出地区分两种约束来源。\n\n---\n\n**[AGREE] R1-W2: Dual-factor pattern 统计支撑不足**\n\n完全同意。Appendix B (Figure 1, §app:dual-factor) 自己标注 \"with only four data points (df=2) and p > 0.05, this constitutes a descriptive characterization rather than a confirmatory statistical test\"。但问题在于，这个 pattern 在 §4 Constraint Composition 中被表述为核心发现 (\"This dual-factor pattern... is consistent with the cross-dataset results\")，且 Contribution #1 声称 \"A systematic study of ontological constraint violations in LLM-based IE: rates correlate with constraint tightness\"。n=4 的描述性观察不应作为 Contribution 级别的 claim。\n\n我的审稿中也独立指出了这个问题（W9），但 R1 的表述更到位——将其与 Contribution #1 直接关联。建议将 Contribution #1 改为聚焦于违规分类学本身（DR/RV/ET/CF 的定义和测量），constraint tightness 降为 observational finding。\n\n---\n\n**[AGREE] R1-W3: WikiEvents \"preliminary\" 但在 Abstract/Contribution 权重过高**\n\n同意。我的审稿 W4 也独立指出了这个问题。Abstract 第 4 句 \"The framework extends to event extraction without modification (preliminary, 20-document test set)\" 和 Contribution #4 \"Preliminary extension to event extraction (WikiEvents, 20-document test set)\" 将其列为正式贡献，但 §5.4 fine-tuning 段自己承认 \"the 20-document test set is a dataset constraint, not a design choice\"，且 trigger F1 shift -5.4pp 的置信区间在此样本量下极宽。\n\n补充：Table 5（WikiEvents 结果）中 Grammar-only 行的 F1 列标注 \"---: not applicable\"，但 grammar-only 模式是有 F1 输出的（它只消除了 EV），标注为 \"not applicable\" 可能是因为 grammar-only 后 RoV 仍高达 64-77% 导致大部分输出不可评估。这个逻辑应在 caption 中说明而非简单标 ---。\n\n---\n\n**[REBUT] R1-W4: 缺少关键 baseline 对比**\n\n部分反驳。\n\n(a) GoLLIE/KnowCoder 互补性：R1 要求实验验证互补性，但这超出了论文的 scope。论文明确定位为 training-free decoding-time constraint enforcement（§6 Related Work: \"OntoCoDec enforces them at decoding time without retraining, and the two approaches are complementary (a GoLLIE-trained model could use OntoCoDec to eliminate residual violations)\"）。要求在 GoLLIE 上叠加 OntoCoDec 实验需要复现 GoLLIE 的训练流程，这对一篇方法论文来说是合理的 future work 而非必须的 baseline。不过，如果能在 Discussion 中量化 GoLLIE 的已知残余违规率（从原论文引用），会大大增强互补性的论证。\n\n(b) Grammar-only ≠ GCD 官方实现：同意这是一个 fair point。论文在 Table 1 caption 中声称 \"Grammar-only represents the ceiling of grammar-constrained decoding (Geng et al., 2023)\"，但使用的是 XGrammar 而非 GCD 的官方实现。然而，两者的机制本质相同（CFG-based logit masking enforcing JSON/enum constraints），差异主要在工程实现而非约束能力。论文应注明这一替代关系。\n\n(c) Post-hoc filtering 仅在附录：这个反驳比较弱。§5.1 和 §5.3 主文中均讨论了 post-hoc filtering（§5.1: \"Post-hoc filtering achieves slightly higher F1 via precision gains but discards up to 48% of predictions\"；§5.3: 专设一段 \"Post-hoc filtering comparison\"），只是完整的 10 配置比较表（Table 12）在 Appendix B。考虑到 post-hoc 在 5/6 ZS 设置中 F1 更高，这确实应在主表中有更显著的呈现。\n\n---\n\n**[AGREE] R1-W5: \"Near-lossless composability\" claim 在考虑 CF 后需重新审视**\n\n同意，且我的审稿 W2 也独立提出了相同问题。\"Near-lossless\" 仅对 DR+F1 成立，不适用于 CF 维度。SciERC zero-shot 总违规从 15.45% 降至 10.83%（Table 1, Tot. 列），改善仅 30%。Fine-tuning 下 CF 升至 1.18%（Table 2），虽然不大但不是零。\n\n论文应将 \"near-lossless composability\" 限定为 \"near-lossless DR composability\"，或明确将 CF 作为已知 cost。Abstract 当前表述 \"achieves near-lossless composability under fine-tuning: DR ≤ 0.20% with R-F1 within ±0.6 pp\" 技术上只涵盖 DR 和 F1，但 \"composability\" 一词暗示了全面的约束满足。\n\n---\n\n**[AGREE] R1-W6: DocRED beam search 仅 50 docs**\n\n同意。Appendix G (Table 14) 明确标注 \"SciERC evaluated on full test set (551 documents); DocRED evaluated on matched 50-document subsets\"。但 §5.6 主文中的表述 \"beam S1 eliminates all four violation types on SciERC for both Qwen and Llama (R-F1 44.23, 46.11; Table 14)\" 可能让读者以为 DocRED 也是全集评估。Clopper-Pearson 95% CI 上限 5.8% 在 Appendix G 中已给出，但主文应明确注明 DocRED beam 结果的 50-doc 限制。\n\n补充：§5.6 的措辞 \"With LoRA, beam S1 eliminates all four violation types on SciERC\" 是准确的（仅限 SciERC），但紧接着的 \"Under zero-shot, beam reduces DR to 0% for calibrated models\" 在上下文中可能被误读为包含 DocRED。建议加注 \"(SciERC full set; DocRED 50-doc subset)\"。\n\n---\n\n**[REBUT] R1-W7: Zero-shot 占据大量实验空间但实用价值有限**\n\n部分反驳。论文在 §5 开头明确框架化了两种评估范式：\"Fine-tuning composability (§5.1) demonstrates deployment readiness... Zero-shot evaluation stress-tests constraint robustness under adversarial conditions (no task supervision, R-F1 2-8)\"。这个框架是合理的：zero-shot 评估的目的不是展示实用价值，而是验证约束机制在最恶劣条件下的行为。\n\n然而，R1 的批评有道理的部分是：主文 §5 的 4 个 subsection 中，§5.1 (SciERC ablation，含 composability) 和 §5.2 (DocRED) 主要展示 zero-shot 数据，§5.3 (Cross-model) 全部 zero-shot，§5.4 (WikiEvents) 也以 zero-shot 为主。Fine-tuning composability 被压缩到 §5.1 的一个段落和 Table 2 中。如果论文的主要贡献是 fine-tuning composability（DR ≤ 0.20%，R-F1 ± 0.6pp），那么实验节的组织结构确实未能反映这个优先级。\n\n建议：将 fine-tuning composability 提升为独立 subsection（§5.2 或 §5.3），把 zero-shot ablation 和 cross-model 作为 supplementary evidence，而非反过来。\n\n---\n\n**[AGREE] R1-W8: Bootstrap CI 未在主表报告**\n\n同意，这是一个 minor 但合理的批评。Table 1 和 Table 3 仅在 caption 中注明 \"Bootstrap: 10,000 iterations\"，但未报告 CI。对于 R-F1 差异在 0.1-0.5pp 量级的比较，CI 对判断是否有实际差异很重要。建议至少在 composability table (Table 2) 中为 R-F1 添加 CI。\n\n---\n\n**[AGREE] R1-W9: BibTeX orphan/duplicate entries**\n\n同意。我的审稿 W8 也独立报告了相同问题（14 orphan entries，包括 formattax2026/lee2026formattax、boostcd2025/sakota2025boostcd 等重复对）。这是提交前清理问题，不影响接收决定但应修复。\n\n---\n\n### Questions 回应\n\n**[AGREE] R1-Q1: Entity registry 错误传播的频率和影响未系统量化**\n\n这是一个重要的技术问题。§3.2 Semantic Layer 描述了 entity registry 的工作机制：entity list 中的类型赋值传播到 relation 的 type field。如果 entity list 中的类型错误，所有引用该 entity 的 relation triple 都会继承错误类型。Appendix K (Case Study §app:case-cf) 展示了一个具体例子（\"MT evaluation methods\" 被错误类型为 Method 而非 Metric），但这是个案而非系统量化。\n\n论文在 Limitations 中提到了 residual DR 的 error decomposition（entity type errors 39%，schema coverage gaps 33%，model generation errors 28%，Appendix B §app:residual-dr-analysis），这间接涉及了 registry 错误传播，但未直接量化 registry 错误到 relation violations 的传播链。合理的 future work 而非 must-fix，但一个简单的统计（\"X% of residual DR violations trace to incorrect entity-list type assignments\"）会大大增强论文的分析深度。\n\n---\n\n**[AGREE] R1-Q2: 对多义类型实体，entity registry 是否过于刚性？**\n\n同意这是一个有意义的问题。Entity registry 采用 first-assignment-wins 策略（§3.2: \"each completed entry {n_i, τ_i} adds (n_i, τ_i) to D\"），不支持同一 entity 在不同上下文中有不同类型。这正是 CF violations 的根源之一——§app:cf-distribution (Table 9) 显示 63.3% 的 CF 违规涉及 Generic 类型，即 \"this approach\" 在引用时应为 Generic 但在实际关系中应为 Method/Task。\n\n论文自己在 §7 和 Appendix B 中识别了这个限制 (\"Global entity-level type consensus during decoding offers the most direct resolution path\")，但没有讨论多义类型的具体处理。一个 soft registry（允许多个类型并基于当前 relation 选择最兼容的类型）可能比 hard first-assignment 更好，这值得在 Discussion 中提及。\n\n---\n\n**[AGREE] R1-Q3: κ(r) 归一化方式是否合适**\n\n我的审稿 Q1 也独立提出了非常相似的问题。$\\kappa(r) = 1 - |\\sigma(r)|/|\\mathcal{E}|^2$ 用 $|\\mathcal{E}|^2$ 作为分母，包括了实际中不可能出现的类型对（如 SciERC 的 Generic×Generic 作为 Hyponym-of 的 domain/range）。对于方向性关系 $|\\mathcal{E}|^2$ 是正确的上界，但对称关系（Conjunction, Compare）理论上应只考虑 $|\\mathcal{E}| \\times (|\\mathcal{E}|+1)/2$。\n\n不过，实际影响可能有限：SciERC 有 6 个 entity types，$|\\mathcal{E}|^2 = 36$ vs. $6 \\times 7/2 = 21$，差异在 κ 值上约 0.1-0.2。DocRED 的 6 个 entity types 同样。这不会根本改变 dual-factor pattern 的方向，但在 n=4 的拟合中可能影响 R² 值。建议作者在附录中报告替代归一化下的敏感性分析。\n\n---\n\n**[AGREE] R1-Q4: GoLLIE 在 SciERC 上的残余违约率？互补性的实验证据？**\n\n同意这是一个有价值的问题，但需要区分 \"nice to have\" 和 \"must have\"。§6 Related Work 声称 \"a GoLLIE-trained model could use OntoCoDec to eliminate residual violations\"，但这是一个未经验证的 hypothesis。GoLLIE 原论文（Sainz et al., ICLR 2024）报告的是 F1 而非违规率，所以从原文无法直接获取残余 DR 数据。\n\n如果作者能在 GoLLIE 的公开输出上运行违规检测（不需要训练 GoLLIE，只需对其预测做 type checking），就能用一行统计证明互补性。这比完整复现 GoLLIE + OntoCoDec 管线要可行得多，且极具说服力。这属于 low-effort high-impact 的修改建议。",
  "reviewer_id": "2",
  "project": "schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 交叉回应 — Reviewer 1 审稿意见\n\n---\n\n### Weaknesses 回应\n\n**[AGREE] R1-W1: \"Ontology Constraints\" framing 与实际实现不匹配**\n\n同意这是一个需要修复的 framing 问题。§2 Background 第一段明确承认：\"We define ontology constraints broadly to encompass both formal ontology specifications (e.g., the KAIROS event ontology) and empirically derived type-pair constraints extracted from annotated training data\"，并指出 \"The latter applies when datasets lack a formal ontology but provide typed annotations (SciERC, DocRED)\"。这说明作者自己知道两种来源的区别，但标题 \"Compiled Ontology Constraints\" 确实暗示了形式本体。\n\n补充发现：SciERC/DocRED 的经验约束覆盖率数据在 §2 中报告为 \"99%+ instance-level coverage on held-out data (SciERC 99.0%, DocRED 99.4%)\"，且 Limitations 提到 \"Schema coverage gaps (one-third of residual violations) arise because RE constraints are extracted from training-data type pairs, which may not cover all valid combinations\"。这进一步证实了经验约束的有限性——真正的形式本体不会有 coverage gaps。建议标题改为 \"Schema-Constrained\" 或 \"Type-Constrained\"（后者已在标题副标题中使用），并在 §2 更突出地区分两种约束来源。\n\n---\n\n**[AGREE] R1-W2: Dual-factor pattern 统计支撑不足**\n\n完全同意。Appendix B (Figure 1, §app:dual-factor) 自己标注 \"with only four data points (df=2) and p > 0.05, this constitutes a descriptive characterization rather than a confirmatory statistical test\"。但问题在于，这个 pattern 在 §4 Constraint Composition 中被表述为核心发现 (\"This dual-factor pattern... is consistent with the cross-dataset results\")，且 Contribution #1 声称 \"A systematic study of ontological constraint violations in LLM-based IE: rates correlate with constraint tightness\"。n=4 的描述性观察不应作为 Contribution 级别的 claim。\n\n我的审稿中也独立指出了这个问题（W9），但 R1 的表述更到位——将其与 Contribution #1 直接关联。建议将 Contribution #1 改为聚焦于违规分类学本身（DR/RV/ET/CF 的定义和测量），constraint tightness 降为 observational finding。\n\n---\n\n**[AGREE] R1-W3: WikiEvents \"preliminary\" 但在 Abstract/Contribution 权重过高**\n\n同意。我的审稿 W4 也独立指出了这个问题。Abstract 第 4 句 \"The framework extends to event extraction without modification (preliminary, 20-document test set)\" 和 Contribution #4 \"Preliminary extension to event extraction (WikiEvents, 20-document test set)\" 将其列为正式贡献，但 §5.4 fine-tuning 段自己承认 \"the 20-document test set is a dataset constraint, not a design choice\"，且 trigger F1 shift -5.4pp 的置信区间在此样本量下极宽。\n\n补充：Table 5（WikiEvents 结果）中 Grammar-only 行的 F1 列标注 \"---: not applicable\"，但 grammar-only 模式是有 F1 输出的（它只消除了 EV），标注为 \"not applicable\" 可能是因为 grammar-only 后 RoV 仍高达 64-77% 导致大部分输出不可评估。这个逻辑应在 caption 中说明而非简单标 ---。\n\n---\n\n**[REBUT] R1-W4: 缺少关键 baseline 对比**\n\n部分反驳。\n\n(a) GoLLIE/KnowCoder 互补性：R1 要求实验验证互补性，但这超出了论文的 scope。论文明确定位为 training-free decoding-time constraint enforcement（§6 Related Work: \"OntoCoDec enforces them at decoding time without retraining, and the two approaches are complementary (a GoLLIE-trained model could use OntoCoDec to eliminate residual violations)\"）。要求在 GoLLIE 上叠加 OntoCoDec 实验需要复现 GoLLIE 的训练流程，这对一篇方法论文来说是合理的 future work 而非必须的 baseline。不过，如果能在 Discussion 中量化 GoLLIE 的已知残余违规率（从原论文引用），会大大增强互补性的论证。\n\n(b) Grammar-only ≠ GCD 官方实现：同意这是一个 fair point。论文在 Table 1 caption 中声称 \"Grammar-only represents the ceiling of grammar-constrained decoding (Geng et al., 2023)\"，但使用的是 XGrammar 而非 GCD 的官方实现。然而，两者的机制本质相同（CFG-based logit masking enforcing JSON/enum constraints），差异主要在工程实现而非约束能力。论文应注明这一替代关系。\n\n(c) Post-hoc filtering 仅在附录：这个反驳比较弱。§5.1 和 §5.3 主文中均讨论了 post-hoc filtering（§5.1: \"Post-hoc filtering achieves slightly higher F1 via precision gains but discards up to 48% of predictions\"；§5.3: 专设一段 \"Post-hoc filtering comparison\"），只是完整的 10 配置比较表（Table 12）在 Appendix B。考虑到 post-hoc 在 5/6 ZS 设置中 F1 更高，这确实应在主表中有更显著的呈现。\n\n---\n\n**[AGREE] R1-W5: \"Near-lossless composability\" claim 在考虑 CF 后需重新审视**\n\n同意，且我的审稿 W2 也独立提出了相同问题。\"Near-lossless\" 仅对 DR+F1 成立，不适用于 CF 维度。SciERC zero-shot 总违规从 15.45% 降至 10.83%（Table 1, Tot. 列），改善仅 30%。Fine-tuning 下 CF 升至 1.18%（Table 2），虽然不大但不是零。\n\n论文应将 \"near-lossless composability\" 限定为 \"near-lossless DR composability\"，或明确将 CF 作为已知 cost。Abstract 当前表述 \"achieves near-lossless composability under fine-tuning: DR ≤ 0.20% with R-F1 within ±0.6 pp\" 技术上只涵盖 DR 和 F1，但 \"composability\" 一词暗示了全面的约束满足。\n\n---\n\n**[AGREE] R1-W6: DocRED beam search 仅 50 docs**\n\n同意。Appendix G (Table 14) 明确标注 \"SciERC evaluated on full test set (551 documents); DocRED evaluated on matched 50-document subsets\"。但 §5.6 主文中的表述 \"beam S1 eliminates all four violation types on SciERC for both Qwen and Llama (R-F1 44.23, 46.11; Table 14)\" 可能让读者以为 DocRED 也是全集评估。Clopper-Pearson 95% CI 上限 5.8% 在 Appendix G 中已给出，但主文应明确注明 DocRED beam 结果的 50-doc 限制。\n\n补充：§5.6 的措辞 \"With LoRA, beam S1 eliminates all four violation types on SciERC\" 是准确的（仅限 SciERC），但紧接着的 \"Under zero-shot, beam reduces DR to 0% for calibrated models\" 在上下文中可能被误读为包含 DocRED。建议加注 \"(SciERC full set; DocRED 50-doc subset)\"。\n\n---\n\n**[REBUT] R1-W7: Zero-shot 占据大量实验空间但实用价值有限**\n\n部分反驳。论文在 §5 开头明确框架化了两种评估范式：\"Fine-tuning composability (§5.1) demonstrates deployment readiness... Zero-shot evaluation stress-tests constraint robustness under adversarial conditions (no task supervision, R-F1 2-8)\"。这个框架是合理的：zero-shot 评估的目的不是展示实用价值，而是验证约束机制在最恶劣条件下的行为。\n\n然而，R1 的批评有道理的部分是：主文 §5 的 4 个 subsection 中，§5.1 (SciERC ablation，含 composability) 和 §5.2 (DocRED) 主要展示 zero-shot 数据，§5.3 (Cross-model) 全部 zero-shot，§5.4 (WikiEvents) 也以 zero-shot 为主。Fine-tuning composability 被压缩到 §5.1 的一个段落和 Table 2 中。如果论文的主要贡献是 fine-tuning composability（DR ≤ 0.20%，R-F1 ± 0.6pp），那么实验节的组织结构确实未能反映这个优先级。\n\n建议：将 fine-tuning composability 提升为独立 subsection（§5.2 或 §5.3），把 zero-shot ablation 和 cross-model 作为 supplementary evidence，而非反过来。\n\n---\n\n**[AGREE] R1-W8: Bootstrap CI 未在主表报告**\n\n同意，这是一个 minor 但合理的批评。Table 1 和 Table 3 仅在 caption 中注明 \"Bootstrap: 10,000 iterations\"，但未报告 CI。对于 R-F1 差异在 0.1-0.5pp 量级的比较，CI 对判断是否有实际差异很重要。建议至少在 composability table (Table 2) 中为 R-F1 添加 CI。\n\n---\n\n**[AGREE] R1-W9: BibTeX orphan/duplicate entries**\n\n同意。我的审稿 W8 也独立报告了相同问题（14 orphan entries，包括 formattax2026/lee2026formattax、boostcd2025/sakota2025boostcd 等重复对）。这是提交前清理问题，不影响接收决定但应修复。\n\n---\n\n### Questions 回应\n\n**[AGREE] R1-Q1: Entity registry 错误传播的频率和影响未系统量化**\n\n这是一个重要的技术问题。§3.2 Semantic Layer 描述了 entity registry 的工作机制：entity list 中的类型赋值传播到 relation 的 type field。如果 entity list 中的类型错误，所有引用该 entity 的 relation triple 都会继承错误类型。Appendix K (Case Study §app:case-cf) 展示了一个具体例子（\"MT evaluation methods\" 被错误类型为 Method 而非 Metric），但这是个案而非系统量化。\n\n论文在 Limitations 中提到了 residual DR 的 error decomposition（entity type errors 39%，schema coverage gaps 33%，model generation errors 28%，Appendix B §app:residual-dr-analysis），这间接涉及了 registry 错误传播，但未直接量化 registry 错误到 relation violations 的传播链。合理的 future work 而非 must-fix，但一个简单的统计（\"X% of residual DR violations trace to incorrect entity-list type assignments\"）会大大增强论文的分析深度。\n\n---\n\n**[AGREE] R1-Q2: 对多义类型实体，entity registry 是否过于刚性？**\n\n同意这是一个有意义的问题。Entity registry 采用 first-assignment-wins 策略（§3.2: \"each completed entry {n_i, τ_i} adds (n_i, τ_i) to D\"），不支持同一 entity 在不同上下文中有不同类型。这正是 CF violations 的根源之一——§app:cf-distribution (Table 9) 显示 63.3% 的 CF 违规涉及 Generic 类型，即 \"this approach\" 在引用时应为 Generic 但在实际关系中应为 Method/Task。\n\n论文自己在 §7 和 Appendix B 中识别了这个限制 (\"Global entity-level type consensus during decoding offers the most direct resolution path\")，但没有讨论多义类型的具体处理。一个 soft registry（允许多个类型并基于当前 relation 选择最兼容的类型）可能比 hard first-assignment 更好，这值得在 Discussion 中提及。\n\n---\n\n**[AGREE] R1-Q3: κ(r) 归一化方式是否合适**\n\n我的审稿 Q1 也独立提出了非常相似的问题。$\\kappa(r) = 1 - |\\sigma(r)|/|\\mathcal{E}|^2$ 用 $|\\mathcal{E}|^2$ 作为分母，包括了实际中不可能出现的类型对（如 SciERC 的 Generic×Generic 作为 Hyponym-of 的 domain/range）。对于方向性关系 $|\\mathcal{E}|^2$ 是正确的上界，但对称关系（Conjunction, Compare）理论上应只考虑 $|\\mathcal{E}| \\times (|\\mathcal{E}|+1)/2$。\n\n不过，实际影响可能有限：SciERC 有 6 个 entity types，$|\\mathcal{E}|^2 = 36$ vs. $6 \\times 7/2 = 21$，差异在 κ 值上约 0.1-0.2。DocRED 的 6 个 entity types 同样。这不会根本改变 dual-factor pattern 的方向，但在 n=4 的拟合中可能影响 R² 值。建议作者在附录中报告替代归一化下的敏感性分析。\n\n---\n\n**[AGREE] R1-Q4: GoLLIE 在 SciERC 上的残余违约率？互补性的实验证据？**\n\n同意这是一个有价值的问题，但需要区分 \"nice to have\" 和 \"must have\"。§6 Related Work 声称 \"a GoLLIE-trained model could use OntoCoDec to eliminate residual violations\"，但这是一个未经验证的 hypothesis。GoLLIE 原论文（Sainz et al., ICLR 2024）报告的是 F1 而非违规率，所以从原文无法直接获取残余 DR 数据。\n\n如果作者能在 GoLLIE 的公开输出上运行违规检测（不需要训练 GoLLIE，只需对其预测做 type checking），就能用一行统计证明互补性。这比完整复现 GoLLIE + OntoCoDec 管线要可行得多，且极具说服力。这属于 low-effort high-impact 的修改建议。",
    "reviewer_id": "2",
    "project": "schema_semantic_constrained_ie"
  }
}
```

</details>

---


### Tool result

_source line 769 · 2026-05-19T08:03:13.507869+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_01fc90ae186a4ed432770f7601995139:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 5633
}
```

</details>

---


### Assistant

_source line 770 · 2026-05-19T08:03:34.286703+00:00_

交叉回应已提交。

**回应总结**：

| R1 条目 | 判定 | 要点 |
|---------|------|------|
| W1 Ontology framing | AGREE | §2 自己承认两种来源的区别，标题应改为 Schema/Type-Constrained |
| W2 Dual-factor 统计 | AGREE | n=4, p≈0.058，不应作为 Contribution 级别 claim |
| W3 WikiEvents 权重 | AGREE | 20-doc test set 置信区间极宽，应降级为 exploratory |
| W4 Baseline 对比 | REBUT(部分) | GoLLIE 实验超出 scope，但 post-hoc 比较确实应更突出 |
| W5 Near-lossless claim | AGREE | 应限定为 "near-lossless DR composability" |
| W6 DocRED beam 50 docs | AGREE | 主文应明确注明样本限制 |
| W7 ZS 占比过大 | REBUT(部分) | ZS 作为 stress test 有价值，但结构上 FT 应更突出 |
| W8 Bootstrap CI | AGREE | Minor，composability table 应添加 CI |
| W9 BibTeX 清理 | AGREE | 与我的 W8 一致 |
| Q1-Q4 | 全部 AGREE | 均为有价值的技术问题，尤其 Q4 GoLLIE 残余违规检测是 low-effort high-impact 建议 |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2"
}
```

</details>

---


## Round 18

## Round 18

68 recorded events


### User

_source line 771 · 2026-05-19T08:42:59.283598+00:00_

[Round 1 审稿请求]:
## Round 1 审稿任务 — Reviewer 2

### Venue 信息
- **目标会议**: EMNLP 2026 via ACL Rolling Review (ARR) May cycle
- **截止日期**: 2026-05-25
- **格式要求**: ACL 两栏模板（`\usepackage[review]{acl}`），Long paper 8 页正文，附录/参考文献不计页数
- **匿名规则**: Double-blind（作者信息匿名）
- **其他要求**: Limitations section（必须，不计页数）、Ethics Statement、ARR Responsible NLP Research Checklist
- **评分标准**: EMNLP 2026 通过 ARR 统一审稿，Overall Assessment 评分：5=Consider for Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1=Do not resubmit

### 论文路径
`projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex`
（main.tex 通过 \input 引入各 section 和 appendix 文件，同目录下有 abstract.tex, section1-7, appendix_*.tex, checklist.tex 等）

### 你的审查侧重：新颖性 + 完整性 + 写作质量 + 格式合规

请重点审查以下方面：

1. **新颖性评估**：
   - 核心贡献（将 IE schema 编译为两层 token-level 约束）相对已有工作的增量是否足够
   - grammar-constrained decoding（XGrammar/Outlines/GCD）已有，semantic layer 的增量贡献是什么
   - 与 GoLLIE、KnowCoder、REBEL 等 schema-aware IE 方法的定位是否清晰
   - entity registry + dynamic masking 是否构成足够的技术创新
   - constraint tightness 分析是否提供了有价值的 insight

2. **完整性**：
   - Related Work 覆盖是否充分（constrained decoding, schema-aware IE, constraint enforcement 三条线）
   - 是否有重要的 missing baseline（如 GoLLIE 直接对比、其他 constrained decoding for IE 方法）
   - 论文叙事主线是否统一（Abstract → Intro → Method → Results → Discussion 逻辑一致性）
   - Contribution claim 是否每条都有对应实验支撑
   - 附录内容是否在正文中被合理引用

3. **写作质量**：
   - Abstract 是否在 30 秒内传达问题/方法/贡献/结果
   - Introduction 叙事是否从 problem → gap → insight → method → evidence 展开
   - 专有名词（DR, CF, RV, ET, κ, S1, S2）首次使用时是否有定义
   - 是否存在 AI 写作痕迹（em-dash, -ing phrases, 过度分段, 过渡词堆砌）
   - 图表知识密度和视觉质量
   - 数据密度是否合适（特别是 Abstract 中数字过多的问题）

4. **格式合规**：
   - 正文是否在 8 页内
   - ACL 模板使用是否正确（[review] 选项、匿名化）
   - 引用格式（natbib/ACL style）
   - ARR Responsible NLP Research Checklist 填写质量
   - BibTeX 条目完整性（是否有 orphan entries、格式错误）
   - Limitations section 和 Ethics Statement 是否符合 ARR 要求

请以 ARR reviewer 标准输出完整审稿意见，包含：Strengths（逐条）、Weaknesses（逐条，带严重程度 Must-Fix/Should-Fix/Minor）、Questions、Missing References、Overall Assessment（按 EMNLP 2026 评分标准给分）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 772 · 2026-05-19T08:43:08.736904+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
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

_source line 773 · 2026-05-19T08:43:08.787918+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 774 · 2026-05-19T08:43:13.387280+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 775 · 2026-05-19T08:43:15.295769+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 776 · 2026-05-19T08:43:15.598419+00:00_

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
12	\usepackage{multirow}
13	\usepackage{amsmath}
14	\usepackage{amssymb}
15	\usepackage{enumitem}
16	\usepackage{xcolor}
17	\usepackage{pifont}
18	
19	\title{OntoCoDec: Type-Constrained Information Extraction\\via Compiled Schema Constraints}
20	
21	\author{Anonymous ACL submission}
22	
23	\begin{document}
24	\maketitle
25	
26	% === Abstract ===
27	\input{abstract}
28	
29	% === §1 Introduction ===
30	\input{section1_introduction_draft}
31	
32	% === §2 Background ===
33	\input{section2_background}
34	
35	% === §3 Method ===
36	\input{section3_method_draft}
37	
38	% === §4 Constraint Composition ===
39	\section{Constraint Composition}
40	\label{sec:composition}
41	\input{section4_composition_draft}
42	
43	% === §5 Experiments ===
44	\section{Experiments}
45	\label{sec:experiments}
46	
47	\input{section3_violation_landscape}
48	
49	\input{section5_scierc_draft}
50	\input{section5_docred_draft}
51	\input{section5_crossmodel_draft}
52	\input{section5_wikievents_draft}
53	\input{section5_runtime}
54	
55	% === §6 Related Work ===
56	\input{section6_related_work}
57	
58	% === §7 Discussion and Conclusion ===
59	\section{Discussion and Conclusion}
60	\label{sec:discussion}
61	\input{section7_conclusion_compressed}
62	
63	% === Limitations (ARR requirement: standalone section, does not count toward page limit) ===
64	\clearpage
65	\section*{Limitations}
66	
67	\paragraph{Constraint scope.}
68	CF impact is model-dependent: for well-calibrated models (Qwen, Llama), S1 introduces CF violations (up to 12.02\%) as a consequence of per-relation independent enforcement; for poorly-calibrated models (Mistral), S1 substantially reduces CF (56.87\%\,$\to$\,1.27\%) by constraining type assignments to schema-valid values.
69	CF fallback ablation show
…[truncated 4463 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 302
}
```

</details>

---


### Tool call

_source line 777 · 2026-05-19T08:43:15.598960+00:00_

called mcp__agent-ml-research__verify_references

<details open><summary>🔧 Tool call — mcp__agent-ml-research__verify_references</summary>

```json
{
  "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
  "project": "schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__verify_references",
  "tool_args": {
    "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
    "project": "schema_semantic_constrained_ie"
  }
}
```

</details>

---


### Tool result

_source line 778 · 2026-05-19T08:43:26.202627+00:00_

Web search results for query: "ACL Rolling Review 2026 reviewer guidelines review form criteria"

Links: [{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"https://aclrollingreview.org/"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"}]

I've found information about the ACL Rolling Review 2026. Here's what I found regarding reviewer guidelines, review form criteria, and related information:

## Reviewer Guidelines

Reviewers are asked to read the paper and get a first impression, then search for related work. If you feel qualified to review some aspects but not others (e.g., experimental results but not formal proofs), you should state in the review if you did not check some major parts, such as proofs.

Reviewers should check for academic conflicts of interest
…[truncated 1156 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 12815
}
```

</details>

---


### Tool result

_source line 779 · 2026-05-19T08:44:19.426178+00:00_

&lt;persisted-output>
Output too large (56.7KB). Full output saved to: /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie--claude-sessions-review-reviewer-2-cbe93d98/636186fc-ce2c-43f5-94cc-f52bf1a930a5/tool-results/toolu_01HPTV8RzmiXX9r7PRFeoDN7.txt

Preview (first 2KB):
{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 69, \"total_citations\": 97, \"unique_cited_keys\": 58, \"orphan_bib\": 10, \"missing_bib\": 0, \"duplicate_keys\": 1, \"online_verified\": 53, \"online_not_found\": 4, \"online_mismatch\": 11}, \"cross_check\": {\"orphan_bib\": [\"delafuente2025guidex\", \"geng2025jsonschemabench\", \"lee2026formattax\", \"lu2025schemarl\", \"paolini2021tanl\", \"park2024grammaraligned\", \"reddy2026dccd\", \"sakota2025boostcd\", \"shen2025slot\", \"vukovic2024dore\"], \"missing_bib\": [], \"orphan_count\": 10, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"synchromesh_iclr2022\", \"type\": \"inproceedings\", \"title\": \"Synchromesh: Reliable Code Generation from Pre-trained Language Models\", \"authors\": \"Poesia, Gabriel and Polozov, Oleksandr and Le, Vu and Tiwari, Ashish and Soares,...\", \"year\": \"2022\", \"venue\": \"International Conference on Learning Representations\"}, {\"key\": \"mgd_neurips2023\", \"type\": \"inproceedings\", \"title\": \"Monitor-Guided Decoding of Code LMs with Static Analysis of Repository Context\", \"authors\": \"Agrawal, Lakshya A. and Kanade, Aditya and Goyal, Navin and Lahiri, Shuvendu K. ...\", \"year\": \"2023\", \"venue\": \"Advances in Neural Information Processing Systems\"}, {\"key\": \"pldi2025_type_constrained_codegen\", \"type\": \"article\", \"title\": \"Type-Constrained Code Generation with Language Models\", \"authors\": \"M\\\\\\\"undler, Niels and He, Jingxuan and Wang, Hao and Sen, Koushik and Song, Dawn ...\", \"year\": \"2025\", \"venue\": \"Proceedings of the ACM on Programming Languages\"}, {\"key\":
…[truncated 371 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__verify_references",
  "elapsed_ms": 63827
}
```

</details>

---


### Tool call

_source line 780 · 2026-05-19T08:44:25.303057+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form criteria, all scoring dimensions, their scales, and descriptions. Include Overall Assessment, Soundness, Excitement/Novelty, Reproducibility, and any other dimensions with their exact rating scales."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form criteria, all scoring dimensions, their scales, and descriptions. Include Overall Assessment, Soundness, Excitement/Novelty, Reproducibility, and any other dimensions with their exact rating scales."
  }
}
```

</details>

---


### Tool call

_source line 781 · 2026-05-19T08:44:26.256765+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 782 · 2026-05-19T08:44:27.161953+00:00_

1	\begin{abstract}
2	We present \textsc{OntoCoDec}, which compiles Information Extraction (IE) schemas into two composable token-level decoding constraints:
3	(1)~a \emph{grammar layer} (XGrammar) that guarantees JSON structural validity and vocabulary membership; and
4	(2)~a \emph{semantic layer} that enforces per-triple domain/range type constraints via a stateful entity registry and dynamic logit masking, with grammar-first fallback when constraints conflict.
5	Without constraints, Large Language Model (LLM) based IE produces systematic domain/range (DR) violations that persist after fine-tuning; violation rates correlate with \emph{constraint tightness} rather than ontology or model scale.
6	% exp_ids: w5_lora_scierc_constrained_eval, w5_qwen_docred_lora_constrained_eval, w5_llama_lora_scierc_constrained_eval, w5_llama_docred_lora_constrained_eval
7	Composed with Low-Rank Adaptation (LoRA), \textsc{OntoCoDec} achieves near-lossless DR composability under fine-tuning: DR\,$\leq$\,0.20\% with R-F1 within $\pm$0.6\,pp, CF\,$\leq$\,1.2\%.
8	Under zero-shot decoding, DR drops by 76--99\% for calibrated models, with an accompanying cross-field consistency (CF) increase (9--21\% zero-shot, resolved to $\leq$1.2\% by fine-tuning on both RE and EE).
9	Beam search with LoRA eliminates all four violation types on SciERC.
10	The framework extends to event extraction without modification (preliminary, 20-document test set).
11	OntoCoDec is training-free and applies to any autoregressive LM across four models (8B--70B) and three tokenizer families.
12	\end{abstract}
13	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 905
}
```

</details>

---


### Tool call

_source line 783 · 2026-05-19T08:44:27.162412+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section1_introduction_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section1_introduction_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 784 · 2026-05-19T08:44:27.614241+00:00_

1	% Section 1: Introduction (compressed, 669→~550 words)
2	
3	\section{Introduction}
4	\label{sec:introduction}
5	
6	Large language models are increasingly used for information extraction~\cite{li2023codeie,sainz2024gollie,wei2023zeroshot}, but when generating relation triples $(h, r, t)$, neither entity is guaranteed to carry a type consistent with the ontology's domain/range constraints for $r$.
7	We call such outputs \emph{domain/range violations}: structurally valid triples that are ontologically invalid.
8	Violations persist across the capability spectrum: 15.4\% of triples on SciERC~\cite{luan2018scierc} and 18.5\% on DocRED~\cite{yao2019docred} under zero-shot decoding, and 1--2\% even after LoRA fine-tuning; rates correlate with \emph{constraint tightness} (few valid type pairs per relation) rather than ontology or model scale.
9	Type violations are ontologically invalid regardless of downstream application: a triple whose head or tail type lies outside the relation's domain/range specification contradicts the schema definition.
10	At deployment-grade quality (R-F1 40--46\%), where extracted triples feed directly into knowledge graphs, reliable type-safety enforcement is needed.
11	
12	Existing approaches leave a fundamental gap.
13	Schema-informed prompting reduces violations by 62\% on average but is per-relation unreliable (violations for \textsc{Evaluate-for} actually \emph{increase} by 5.8\,pp).
14	Grammar-constrained decoding~\cite{dong2025xgrammar,willard2023outlines,beurer-kellner2023lmql} guarantees syntactic well-formedness but cannot encode cross-field semantic constraints.
15	Post-hoc filtering achieves higher F1 in most zero-shot settings via precision gains, but at the cost of discarding up to 48\% of predictions including true positives; at high rejection rates (e.g., Mistral DocRED 73.7\%), it discards the majority of outputs and becomes impractical.
16	OntoCoDec preserves recall by enforcing constraints during generation rather than discardi
…[truncated 2670 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 785 · 2026-05-19T08:44:27.614716+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section2_background.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section2_background.tex"
  }
}
```

</details>

---


### Tool result

_source line 786 · 2026-05-19T08:44:28.218582+00:00_

1	% Section 2: Background (compressed)
2	
3	\section{Background}
4	\label{sec:background}
5	
6	\paragraph{IE Ontology Structure.}
7	\label{sec:bg:ontology}
8	An IE ontology $\mathcal{O} = (\mathcal{E}, \mathcal{R}, \sigma)$ defines entity types $\mathcal{E}$, relation types $\mathcal{R}$, and a mapping $\sigma: \mathcal{R} \to \mathcal{P}(\mathcal{E} \times \mathcal{E})$ specifying valid (head type, tail type) pairs per relation.
9	A triple $(h, r, t)$ is \emph{type-valid} if $(\mathrm{type}(h), \mathrm{type}(t)) \in \sigma(r)$.
10	We quantify constraint restrictiveness via \emph{constraint tightness} $\kappa(r)$ (Eq.~\ref{eq:tightness}, \S\ref{sec:composition}): tighter constraints leave fewer valid type pairs per relation.
11	We define ontology constraints broadly to encompass both formal ontology specifications (e.g., the KAIROS event ontology with explicit role-entity type mappings) and empirically derived type-pair constraints extracted from annotated training data.
12	The latter applies when datasets lack a formal ontology but provide typed annotations (SciERC, DocRED); OntoCoDec compiles both sources into the same constraint representation without modification.
13	Empirical constraints achieve 99\%+ instance-level coverage on held-out data (SciERC 99.0\%, DocRED 99.4\%); uncovered type pairs trigger grammar-first fallback (\S\ref{sec:composition}), ensuring no valid triples are blocked.
14	
15	\paragraph{Grammar-Constrained Decoding.}
16	\label{sec:bg:gcd}
17	Grammar-constrained decoding restricts each token $y_t$ to a mask $M_g \in \{0, 1\}^{|V|}$ derived from a target grammar.
18	XGrammar~\citep{dong2025xgrammar} compiles JSON Schemas into pushdown automata for efficient enforcement of structural constraints; Outlines~\citep{willard2023outlines} and SGLang~\citep{zheng2024sglang} offer similar capabilities.
19	However, these methods are limited to context-free constraints and cannot enforce cross-field semantic rules (e.g., ``if $r$ = \textsc{Feature-of}, t
…[truncated 859 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 603
}
```

</details>

---


### Tool call

_source line 787 · 2026-05-19T08:44:28.219697+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_method_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_method_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 788 · 2026-05-19T08:44:28.270783+00:00_

1	% Section 3 — Method (Draft)
2	% OntoCoDec: Type-Valid Information Extraction
3	% via Compiled Ontology Constraints
4	
5	\section{Method}
6	\label{sec:method}
7	
8	We present OntoCoDec, a two-layer constrained decoding framework that compiles IE schemas into token-level masks enforced during autoregressive generation.
9	Unlike type-constrained code generation, IE presents three distinct challenges: (1)~entity types are inferred from free text rather than declared annotations, (2)~the entity registry is built dynamically during generation, and (3)~constraint targets are context-dependent type assignments rather than fixed grammar productions.
10	The grammar layer (\S\ref{sec:grammar}) guarantees structural validity (well-formed JSON with ontology-vocabulary membership), while the semantic layer (\S\ref{sec:semantic}) enforces domain/range type constraints via a stateful entity registry.
11	We describe the problem formulation (\S\ref{sec:formulation}), each layer, and two decoding strategies (\S\ref{sec:strategies}).
12	Formal analysis of constraint composition is deferred to Section~\ref{sec:composition}.
13	
14	
15	\subsection{Problem Formulation}
16	\label{sec:formulation}
17	
18	\paragraph{IE as structured generation.}
19	Given an input text $x$, a language model generates a structured JSON output $y$:
20	%
21	\begin{equation}\label{eq:output-schema}
22	\resizebox{.88\columnwidth}{!}{$\displaystyle
23	  y = \bigl\{\texttt{entities}: [\{n_i, \tau_i\}],\; \texttt{relations}: [\{h_j, t_j, r_j, \tau^h_j, \tau^t_j\}]\bigr\}
24	$}
25	\end{equation}
26	%
27	where each entity has a name $n_i$ and type $\tau_i \in \mathcal{E}$, and each relation specifies head $h_j$, tail $t_j$, relation type $r_j \in \mathcal{R}$, and head/tail entity types $\tau^h_j, \tau^t_j$.
28	The output JSON Schema (\S\ref{sec:grammar}) enforces a fixed field ordering (head $\to$ tail $\to$ relation $\to$ head\_type $\to$ tail\_type) via deterministic grammar compilation.
29	This ordering ensures 
…[truncated 6604 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool result

_source line 789 · 2026-05-19T08:44:32.592017+00:00_

# ACL Rolling Review Form Criteria

## 1. **Reviewer Confidence**
Scale: 1-5
- 5: Positive evaluation is correct; very careful reading; familiar with related work
- 4: Quite sure; checked important points carefully
- 3: Pretty sure; good general knowledge but didn't verify details thoroughly
- 2: Can defend evaluation but likely missed details or novelty assessment uncertain
- 1: "Not my area, or paper is very hard to understand"

## 2. **Soundness**
Scale: 1-5 (with .5 increments)
- 5: "one of the most thorough I have seen, given its type"
- 4: Sufficient support for claims; extra experiments optional
- 3: Adequate support for main claims; minor details need work
- 2: Main claims lack sufficient support; major technical problems
- 1: "not yet sufficiently thorough to warrant publication"

## 3. **Excitement**
Scale: 1-5 (with .5 increments)
- 5: "I would recommend this paper to others and/or attend its presentation"
- 4: Would mention to others or attend presentation
- 3: Might mention points or attend if time permits
- 2: Doesn't resonate personally but may interest others
- 1: "does not resonate with me, and I don't think it would with others"

## 4. **Overall Assessment**
Scale: 1-5 (with .5 increments)
- 5: Consider for Award (top 2.5%)
- 4: Conference acceptance
- 3: Findings track acceptance
- 2: Resubmit next cycle
- 1: Do not resubmit

## 5. **Reproducibility**
Scale: 1-5
- 5: Results easily reproducible
- 4: Mostly reproducible despite minor variations
- 3: Reproducible with difficulty; underspecified parameters
- 2: "hard pressed to reproduce"; unavailable data or missing details
- 1: "would not be able to reproduce the results"

## 6. **Datasets & Software**
Scale: 1-5 (separate dimensions)
- 5: Enabling for future research choices
- 4: Useful for ongoing work
- 3: Potentially useful
- 2: Documentary value only
- 1: None released

## 7. **Author Anonymity Knowledge**
Scale: 1-5
- 5: Author identity known from double-blind violation
- 4: Known from prepri
…[truncated 117 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 7288
}
```

</details>

---


### Tool call

_source line 790 · 2026-05-19T08:44:37.514700+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section4_composition_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section4_composition_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 791 · 2026-05-19T08:44:38.520384+00:00_

1	% Section: Constraint Composition (compressed, 787→~500 words)
2	
3	At each decoding step $t$, let $G(t) \subseteq V$ and $S(t) \subseteq V$ denote the tokens permitted by the grammar and semantic layers, respectively.
4	The final mask is their conjunction:
5	%
6	\begin{equation}\label{eq:composition}
7	  M_{\text{final}}(t) = M_{\text{grammar}}(t) \;\wedge\; M_{\text{semantic}}(t),
8	\end{equation}
9	%
10	so a token is allowed only if it satisfies \emph{both} structural and type-level constraints.
11	The conjunction is asymmetric: $S(t)$ is defined only over $G(t)$. This reflects the enabling dependency (\S\ref{sec:method}): the semantic layer requires the relation type to belong to $\mathcal{R}$, a property guaranteed only by the grammar layer.
12	
13	\paragraph{Grammar-First Fallback.}
14	When $S(t) \cap G(t) = \emptyset$ (tight constraints leave no token that is both grammar-valid and semantically valid), na\"{\i}ve masking would force selection of a grammar-invalid token, breaking JSON structure.
15	We enforce a \emph{grammar-first fallback}: if no semantically valid token survives grammar filtering, semantic masking is skipped and the grammar layer alone controls selection.
16	Structural integrity is a hard constraint; a type violation is a soft error detectable by downstream validation.
17	Among type violations, DR and CF differ in severity: a DR violation renders the triple ontologically invalid (the entity type lies outside the relation's domain or range), whereas a CF violation means each triple is individually schema-valid but the same entity receives different type assignments across triples.
18	
19	\paragraph{Constraint Tightness.}
20	Recall the tightness of relation $r$ (\S\ref{sec:bg:ontology}):\footnote{For symmetric relations, $|\sigma(r)|$ counts ordered pairs; the normalization $|\mathcal{E}|^2$ remains appropriate since we evaluate on directed triples.}
21	%
22	\begin{equation}\label{eq:tightness}
23	  \kappa(r) = 1 - \frac{|\sigma(r)|}{|\mathc
…[truncated 1461 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1005
}
```

</details>

---


### Tool call

_source line 792 · 2026-05-19T08:44:38.671659+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_violation_landscape.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_violation_landscape.tex"
  }
}
```

</details>

---


### Tool result

_source line 793 · 2026-05-19T08:44:38.973509+00:00_

1	% §5 Setup (compressed from Violation Landscape)
2	% exp_ids: mvp_phase0_violation_rate, mvp_phase0_scierc_schema,
3	%          mvp_phase0_violation_rate_docred, mvp_phase0_docred_schema
4	
5	\label{sec:violation_landscape}
6	
7	We evaluate OntoCoDec in two regimes.
8	Fine-tuning composability (\S\ref{sec:composability}) tests the recommended deployment configuration: LoRA + S1 constraints at R-F1 40--46.
9	Zero-shot evaluation (\S\ref{sec:scierc-results}--\S\ref{sec:cross-model}) isolates layer contributions and stress-tests constraint robustness without task supervision; R-F1 2--8 reflects the absence of task-specific training, not method failure.
10	
11	\paragraph{Setup.}
12	We evaluate on SciERC~\cite{luan2018scierc} (551 test sentences, 7 relations, $\bar{\kappa}{=}0.333$) and DocRED~\cite{yao2019docred} (998 dev documents,\footnote{DocRED test annotations are not publicly available; we evaluate on the development set.} 96 relations, $\bar{\kappa}{=}0.842$).
13	RE type constraints are extracted automatically from observed type pairs in training data (neither dataset provides a formal ontology); EE constraints on WikiEvents (\S\ref{sec:wikievents}) are derived from the KAIROS ontology.
14	The framework handles both sources without modification.
15	Primary model: Qwen3-8B~\cite{qwen2025qwen3}, zero-shot greedy decoding; cross-model validation in \S\ref{sec:cross-model}, composability with fine-tuning in \S\ref{sec:composability}.
16	We measure four violation categories: \textbf{DR} (domain/range type pair $\notin \sigma(r)$), \textbf{RV} (relation $\notin \mathcal{R}$), \textbf{ET} (entity type $\notin \mathcal{E}$), and \textbf{CF} (same entity assigned conflicting types across triples).
17	Baseline DR violations are 15.37\% (SciERC) and 18.46\% (DocRED), comparable rates associated with constraint tightness rather than ontology scale (\S\ref{sec:introduction}); schema-informed prompting reduces DR by 62\% on SciERC but is per-relation unreliable (Appendix~\re
…[truncated 35 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 794 · 2026-05-19T08:44:38.973979+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 795 · 2026-05-19T08:44:39.931377+00:00_

1	% Section 5 — SciERC Results (Draft)
2	% Data source: Phase 2 SciERC registry experiments
3	% exp_ids: phase2_scierc_unconstrained, phase2_scierc_grammar_only,
4	%          phase2_scierc_semantic_only, phase2_scierc_full_s1, phase2_scierc_full_s2
5	% All numbers verified against registry 2026-05-14.
6	
7	\subsection{Ablation and Composability with Fine-Tuning}
8	\label{sec:scierc-results}
9	
10	Table~\ref{tab:scierc-ablation} presents the five-way ablation on SciERC (Qwen3-8B, zero-shot, 551 documents); only the active constraint layers differ across rows.
11	
12	% ──────────────────────────────────────────
13	%  Table: SciERC five-way ablation
14	% ──────────────────────────────────────────
15	\begin{table}[t]
16	\centering
17	\small
18	\setlength{\tabcolsep}{3.6pt}
19	\resizebox{\columnwidth}{!}{%
20	\begin{tabular}{@{}l rrrrrr rr@{}}
21	\toprule
22	& \multicolumn{6}{c}{\textbf{Violation Rates (\%)}}
23	& \multicolumn{2}{c}{\textbf{F1}} \\
24	\cmidrule(lr){2-7} \cmidrule(l){8-9}
25	\textbf{Mode}
26	  & DR\,$\downarrow$ & $\Delta$DR
27	  & RV\,$\downarrow$ & ET\,$\downarrow$ & CF & Tot.\,$\downarrow$
28	  & Rel.\,$\uparrow$ & Ent.\,$\uparrow$ \\
29	\midrule
30	Unconstrained
31	  & 15.37 & ---
32	  & 1.39  & 0.40
33	  & 0.08  & 15.45
34	  & 8.23  & 31.01 \\
35	Grammar
36	  & 14.84 & $\downarrow$3\%
37	  & \textbf{0} & \textbf{0}
38	  & 0.08  & 14.92
39	  & 8.23  & 30.98 \\
40	Semantic
41	  & 11.65 & $\downarrow$24\%
42	  & 1.51  & 0.40
43	  & 2.71  & 14.36
44	  & 8.15  & 31.01 \\
45	Full (S1)
46	  & \textbf{0.93} & $\downarrow$\textbf{94\%}
47	  & \textbf{0} & \textbf{0}
48	  & 9.90  & \textbf{10.83}
49	  & \textbf{8.36} & 30.98 \\
50	Full (S2)
51	  & 0.97  & $\downarrow$94\%
52	  & \textbf{0} & \textbf{0}
53	  & 8.03  & \textbf{9.00}
54	  & 8.03  & \textbf{31.90} \\
55	\bottomrule
56	\end{tabular}}%
57	\caption{Five-way ablation on SciERC (551 docs, Qwen3-8B, zero-shot).
58	$\Delta$DR: relative change vs.\ unconstrained.
59	Tot.\ = DR + CF (total type-violation b
…[truncated 5798 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 957
}
```

</details>

---


### Tool call

_source line 796 · 2026-05-19T08:44:40.082634+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 797 · 2026-05-19T08:44:40.133330+00:00_

1	% Section 5 — DocRED Results (compressed, 1450→~600 words)
2	% exp_ids: phase2_docred_unconstrained, phase2_docred_grammar_only,
3	%          phase2_docred_semantic_only, phase2_docred_full_s1
4	% All numbers verified against registry 2026-05-14.
5	
6	\subsection{Cross-Dataset Validation on DocRED}
7	\label{sec:docred-results}
8	
9	Table~\ref{tab:docred-ablation} presents the four-way ablation on DocRED (96 Wikidata relation types, 14$\times$ SciERC; Qwen3-8B, zero-shot, 998 documents).
10	
11	% ──────────────────────────────────────────
12	%  Table: DocRED four-way ablation
13	% ──────────────────────────────────────────
14	\begin{table}[t]
15	\centering
16	\small
17	\setlength{\tabcolsep}{3.6pt}
18	\resizebox{\columnwidth}{!}{%
19	\begin{tabular}{@{}l rrrrrr rr@{}}
20	\toprule
21	& \multicolumn{6}{c}{\textbf{Violation Rates (\%)}}
22	& \multicolumn{2}{c}{\textbf{F1}} \\
23	\cmidrule(lr){2-7} \cmidrule(l){8-9}
24	\textbf{Mode}
25	  & DR\,$\downarrow$ & $\Delta$DR
26	  & RV\,$\downarrow$ & ET\,$\downarrow$ & CF & Tot.\,$\downarrow$
27	  & Rel.\,$\uparrow$ & Ent.\,$\uparrow$ \\
28	\midrule
29	Unconstrained
30	  & 18.46 & ---
31	  & 29.66 & 2.48
32	  & 0.10  & 18.56
33	  & 7.74  & 58.15 \\
34	Grammar
35	  & 26.17 & $\uparrow$42\%
36	  & \textbf{0.03} & \textbf{0}
37	  & 0.07  & 26.24
38	  & \textbf{8.31}  & \textbf{59.38} \\
39	Semantic
40	  & 13.84 & $\downarrow$25\%
41	  & 29.87 & 4.22
42	  & 1.05  & 14.89
43	  & 7.70  & 57.81 \\
44	Full (S1)
45	  & \textbf{10.21} & $\downarrow$\textbf{45\%}
46	  & \textbf{0.03} & \textbf{0}
47	  & 2.57  & \textbf{12.78}
48	  & 8.23  & 59.37 \\
49	\bottomrule
50	\end{tabular}}%
51	\caption{Four-way ablation on DocRED (998 documents, Qwen3-8B, zero-shot).
52	$\Delta$DR: relative change vs.\ unconstrained.
53	Tot.\ = DR + CF (total type-violation burden).
54	Best per column in \textbf{bold} (CF excluded; Tot.\ included).
55	F1 $\times$100. Bootstrap significance: R-F1 $+$0.50\,pp ($p < 0.001$).}
56	\label{tab:docred-ablation}
57	\en
…[truncated 1793 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 798 · 2026-05-19T08:44:40.133743+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_crossmodel_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_crossmodel_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 799 · 2026-05-19T08:44:40.184397+00:00_

1	% Section 5 — Cross-Model Validation (compressed, 830→~400 words)
2	% exp_ids: phase2_scierc_unconstrained, phase2_scierc_full_s1,
3	%          phase2_docred_unconstrained, phase2_docred_full_s1,
4	%          llama_scierc_unconstrained, llama_scierc_full_s1,
5	%          llama_docred_unconstrained, llama_docred_full_s1
6	
7	\subsection{Cross-Model Validation}
8	\label{sec:cross-model}
9	
10	Table~\ref{tab:cross-model} replicates S1 with Llama-3.1-8B and Mistral-7B under identical prompts.
11	
12	\begin{table}[t]
13	\centering
14	\small
15	\setlength{\tabcolsep}{3.4pt}
16	\resizebox{\columnwidth}{!}{%
17	\begin{tabular}{@{}ll rrrr r@{}}
18	\toprule
19	& & \multicolumn{4}{c}{\textbf{Violation Rates (\%)}}
20	& \textbf{R-F1} \\
21	\cmidrule(lr){3-6} \cmidrule(l){7-7}
22	\textbf{Dataset} & \textbf{Model}
23	  & DR\,$\downarrow$ & RV\,$\downarrow$ & ET\,$\downarrow$ & CF
24	  & $\uparrow$ \\
25	\midrule
26	\multirow{6}{*}{SciERC}
27	  & Qwen (U)    & 15.37 & 1.39  & 0.40 & 0.08 & 8.23 \\
28	  & Qwen (S1)   &  0.93 & 0     & 0    & 9.90 & 8.36 \\
29	  \cmidrule(l){2-7}
30	  & Llama (U)   & 13.34 & 0.55  & 0    & 0.24 & 2.68 \\
31	  & Llama (S1)  &  0.08 & 0     & 0    & 6.56 & 2.54 \\
32	  \cmidrule(l){2-7}
33	  & Mistral (U) & 56.94 & 0     & 1.50 & 56.87$^\dagger$ & 3.66 \\
34	  & Mistral (S1)& 13.40 & 0     & 0    & 1.27  & 3.67 \\
35	\midrule
36	\multirow{6}{*}{DocRED}
37	  & Qwen (U)    & 18.46 & 29.66 & 2.48 & 0.10 & 7.74 \\
38	  & Qwen (S1)   & 10.21 &  0.03 & 0    & 2.57 & 8.23 \\
39	  \cmidrule(l){2-7}
40	  & Llama (U)   & 26.07 & 16.03 & 0.13 & 0.17 & 5.98 \\
41	  & Llama (S1)  &  2.55 &  0    & 0    & 12.02& 6.27 \\
42	  \cmidrule(l){2-7}
43	  & Mistral (U) & 57.42 & 42.35 & 7.58 & 24.78 & 4.34 \\
44	  & Mistral (S1)& 33.20 &  0    & 0    & 0.19  & 5.52 \\
45	\bottomrule
46	\end{tabular}}%
47	\caption{Three-model zero-shot validation. U: unconstrained; S1: full two-layer.
48	Parse failures: Llama DocRED 9.1\%; others $\leq$1.1\%.
49	$^\dagger$Mistral: poor ze
…[truncated 1797 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 800 · 2026-05-19T08:44:45.454942+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_wikievents_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_wikievents_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 801 · 2026-05-19T08:44:45.455723+00:00_

1	% Section 5 — Event Extraction on WikiEvents (compact, inline)
2	% exp_ids: ee_qwen_wikievents_unconstrained, ee_llama_wikievents_unconstrained,
3	%          ee_mistral_wikievents_unconstrained, ee_qwen_wikievents_constrained,
4	%          ee_llama_wikievents_constrained, ee_mistral_wikievents_constrained_v2
5	% v3 final data confirmed by Director 2026-05-18.
6	
7	\subsection{Preliminary Extension: Event Extraction}
8	\label{sec:wikievents}
9	
10	We apply OntoCoDec to event extraction (EE) on WikiEvents~\cite{li2021document} (56 event types, 80 roles, 27 entity types, 245 constraints; Appendix~\ref{app:wikievents}) without modification.
11	Violations extend to EV (event vocabulary), RoV (role vocabulary), and AC (argument constraint, analogous to DR).
12	
13	% ──────────────────────────────────────────
14	%  Table: WikiEvents three-model comparison (v3 final)
15	%  exp_ids: ee_{qwen,llama,mistral}_wikievents_{unconstrained,grammar_only,constrained_v3}
16	% ──────────────────────────────────────────
17	\begin{table}[t]
18	\centering
19	\small
20	\setlength{\tabcolsep}{2.8pt}
21	\resizebox{\columnwidth}{!}{%
22	\begin{tabular}{@{}ll rrrr rr@{}}
23	\toprule
24	& & \multicolumn{4}{c}{\textbf{Violation Rates (\%)}}
25	& \multicolumn{2}{c}{\textbf{F1}} \\
26	\cmidrule(lr){3-6} \cmidrule(l){7-8}
27	\textbf{Model} & \textbf{Mode}
28	  & EV\,$\downarrow$ & RoV\,$\downarrow$ & AC & CF
29	  & Trig.\,$\uparrow$ & Ent.\,$\uparrow$ \\
30	\midrule
31	\multirow{3}{*}{Qwen3-8B}
32	  & Unconstr.\ & 24.0 & 74.9 & 0.3 & 0 & 11.8 & 0 \\
33	  & Grammar    & \textbf{0} & 76.1 & 8.2 & --- & --- & --- \\
34	  & Full S1    & \textbf{0} & \textbf{0} & 2.1 & 21.1 & 13.4 & 14.1 \\
35	\midrule
36	\multirow{3}{*}{\shortstack[l]{Llama\\3.1-8B}}
37	  & Unconstr.\ & 10.5 & 88.8 & 0.1 & 0 & 5.7 & 0 \\
38	  & Grammar    & \textbf{0} & 77.0 & 8.8 & --- & --- & --- \\
39	  & Full S1    & \textbf{0} & \textbf{0} & 3.8 & 17.2 & 7.5 & 17.6 \\
40	\midrule
41	\multirow{3}{*}{\shortstack[l]{Mistral\\7B}}
42
…[truncated 2360 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 802 · 2026-05-19T08:44:46.460568+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_runtime.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_runtime.tex"
  }
}
```

</details>

---


### Tool result

_source line 803 · 2026-05-19T08:44:46.862697+00:00_

1	% Runtime overhead (inline paragraph, no subsection header to save space)
2	
3	\paragraph{Runtime overhead.}
4	\label{sec:runtime}
5	S1 overhead is $+$13.1\% on SciERC and $+$2.43\% on DocRED (amortized over longer sequences); under LoRA, $+$10.0\% with 37\% lower absolute latency.
6	Grammar compile: one-time 44\,ms (Appendix~\ref{app:runtime}).
7	Scaling benchmarks confirm constant overhead (2--3\%) up to 200 entity types and 1{,}000 relations (Appendix~\ref{app:scalability}).
8	
9	\paragraph{Beam search compatibility.}
10	\label{sec:beam-results}
11	Under greedy S1, the grammar-first fallback resolves DR$\leftrightarrow$CF conflicts one token at a time; beam search ($k{=}4$) explores paths that satisfy both layers jointly and reduces DR and CF simultaneously.
12	With LoRA, beam S1 eliminates all four violation types on SciERC (551 docs) for both Qwen and Llama (R-F1 44.23, 46.11; Table~\ref{tab:beam-search}).
13	Under zero-shot, beam reduces DR to 0\% for calibrated models on SciERC (551 docs) and a DocRED 50-document subset, and CF substantially (9.90\%\,$\to$\,0.53\% Qwen; 6.56\%\,$\to$\,0.93\% Llama on SciERC); Mistral remains a boundary condition (DR 7.99\%, CF 1.27\%) due to high baseline violations (Appendix~\ref{app:beam-search}).
14	Total latency overhead is 1.54$\times$ (beam 1.32$\times$ $+$ constraint 1.17$\times$; Table~\ref{tab:beam-latency}).
15	
16	% exp_ids: 70b_scierc_unconstrained, 70b_scierc_constrained, 70b_docred_unconstrained, 70b_docred_constrained
17	\paragraph{Cross-scale generalizability.}
18	\label{sec:70b-results}
19	On Llama-3.1-70B (AWQ INT4), OntoCoDec achieves DR$\to$0\% on SciERC (R-F1 $-$0.03\,pp) and \textbf{0\%} across ET, RV, and DR on the full DocRED 998-document set (R-F1 $+$0.04\,pp), the only configuration to completely eliminate DR on DocRED.
20	CF rises to 7.01\% (from 0.07\%); the low baseline reflects under-measurement (malformed outputs bypass the checker), while constrained decoding exposes more triples to the consi
…[truncated 100 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 804 · 2026-05-19T08:44:46.863081+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 805 · 2026-05-19T08:44:47.917667+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	We provide a detailed survey in Appendix~\ref{app:related_work}; here we position OntoCoDec along three axes.
5	
6	\paragraph{Grammar-constrained decoding.}
7	XGrammar~\cite{dong2025xgrammar}, Outlines~\cite{willard2023outlines}, LMQL~\cite{beurer-kellner2023lmql}, SynCode~\cite{ugare2024syncode}, and Grammar-Aligned Decoding~\cite{park2024grammar} guarantee format validity via CFG-based token masking; JSONSchemaBench~\cite{jsonschemabench2025} benchmarks these systems.
8	GCD~\cite{geng2023gcd} applies grammar constraints to IE tasks.
9	In code generation, PICARD~\cite{scholak2021picard} and Synchromesh~\cite{synchromesh_iclr2022} enforce type constraints via incremental parsing, and \citet{pldi2025_type_constrained_codegen} compile full type systems into prefix automata.
10	These methods ensure syntactic or type-level validity but operate on static type declarations; IE requires a dynamic entity registry built during generation, where constraint targets depend on the co-occurring relation type.
11	OntoCoDec's grammar layer builds on XGrammar; its semantic layer extends constrained decoding from syntax to ontology-level type enforcement.
12	
13	\paragraph{Schema-aware IE.}
14	GoLLIE~\cite{sainz2024gollie}, GUIDEX~\cite{guidex2025}, and KnowCoder~\cite{knowcoder_acl2024} encode ontology structure as Python dataclasses and train models to generate typed code.
15	REBEL~\cite{cabot2021rebel}, InstructUIE~\cite{wang2023instructuie}, DeepStruct~\cite{wang2022deepstruct}, UIE~\cite{lu2022uie}, and USM~\cite{lou2023usm} unify extraction tasks via structured output formats with task-specific training.
16	UniversalNER~\cite{zhou2024universalner} achieves strong zero-shot NER via targeted distillation.
17	\citet{wadhwa2023revisiting} benchmark LLM-based RE and find persistent schema compliance gaps.
18	These methods internalize constraints through training; OntoCoDec enforces them at decoding time without retraining, and
…[truncated 1444 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1054
}
```

</details>

---


### Tool call

_source line 806 · 2026-05-19T08:44:47.918200+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion_compressed.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion_compressed.tex"
  }
}
```

</details>

---


### Tool result

_source line 807 · 2026-05-19T08:44:48.271824+00:00_

1	% Section 7 — Discussion and Conclusion
2	% Full discussion in Appendix; Mistral boundary condition in app:dual-factor.
3	
4	OntoCoDec compiles IE schemas into composable token-level decoding constraints that achieve near-lossless DR composability under fine-tuning: DR\,$\leq$\,0.20\% with R-F1 within $\pm$0.6\,pp (R-F1 40--46), CF\,$\leq$\,1.2\% on RE, RoV$\to$0\% and AC$\leq$0.8\% on EE, and beam search ($k{=}4$) eliminates all four RE violation types (\S\ref{sec:beam-results}).
5	Under zero-shot decoding, DR drops by 42--99\% across three models and three datasets with no significant F1 cost.
6	The R-F1 gap with supervised systems (49--53~\citep{zhong2021frustratingly,ye2022packed}) traces to base model IE ability, not constraint overhead; a GoLLIE-trained model could use OntoCoDec to eliminate residual violations.
7	
8	CF remains an open challenge: per-slot enforcement can assign different types to the same entity across triples. Global entity-level type consensus during decoding offers the most direct resolution path; registry type errors and grammar-first fallback partially mitigate but do not eliminate this.
9	The framework applies to any autoregressive IE system without modification, validated across four models (8B--70B), three tokenizer families, and two tasks.
10	Evaluating type-safety impact on downstream tasks and validating the tightness-calibration interaction on broader schemas remain future work.
11	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 353
}
```

</details>

---


### Tool call

_source line 808 · 2026-05-19T08:44:48.272413+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/checklist.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/checklist.tex"
  }
}
```

</details>

---


### Tool result

_source line 809 · 2026-05-19T08:44:48.323001+00:00_

1	% ARR Responsible NLP Research Checklist
2	% Sections A--E, per https://aclrollingreview.org/responsibleNLPresearch/
3	
4	\section*{Responsible NLP Research Checklist}
5	
6	\subsection*{A \hspace{0.5em} For Every Submission}
7	
8	\begin{enumerate}[label=\textbf{A\arabic*.},leftmargin=2.5em]
9	\item \textbf{Did you describe the limitations of your work?}
10	\\ Yes. See the Limitations section (after \S7), which covers constraint scope (CF trade-off, residual DR decomposition), evaluation coverage (model scales, decoding configurations), and engineering considerations (scalability bounds, tokenizer dependency).
11	
12	\item \textbf{Did you discuss any potential risks of your work?}
13	\\ Yes. See the Ethics Statement. The method operates on model outputs using publicly available datasets with no PII. Constrained decoding does not introduce new privacy or safety risks beyond those of base LMs.
14	
15	\item \textbf{Do the abstract and introduction summarize the paper's main claims?}
16	\\ Yes. The abstract states three main contributions; \S1 elaborates each with supporting evidence and section pointers.
17	\end{enumerate}
18	
19	\subsection*{B \hspace{0.5em} Did you use or create scientific artifacts?}
20	Yes. We use existing datasets (SciERC, DocRED, WikiEvents), pre-trained models (Qwen3-8B, Llama-3.1-8B, Mistral-7B, Llama-3.1-70B), and software libraries (XGrammar, vLLM, PEFT).
21	
22	\begin{enumerate}[label=\textbf{B\arabic*.},leftmargin=2.5em]
23	\item \textbf{Did you cite the creators of artifacts you used?}
24	\\ Yes. All datasets, models, and libraries are cited in \S2, \S5, and Appendix~\ref{app:reproducibility}.
25	
26	\item \textbf{Did you discuss the license or terms for use and/or distribution of any artifacts?}
27	\\ Yes. SciERC (Apache 2.0), DocRED (MIT), WikiEvents (publicly released by \citet{li2021document}). Model licenses are noted in Appendix~\ref{app:reproducibility}.
28	
29	\item \textbf{Did you discuss if your use of existing artifacts was con
…[truncated 3197 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 810 · 2026-05-19T08:44:54.006156+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 811 · 2026-05-19T08:44:54.910610+00:00_

1	\section{Extended Related Work}
2	\label{app:related_work}
3	
4	% ===========================================================================
5	% Paradigm 1: Grammar-Constrained Decoding
6	% ===========================================================================
7	\paragraph{Grammar-Constrained Decoding.}
8	Recent work has established efficient algorithms for restricting LLM outputs to conform to context-free grammars, making grammar-constrained decoding the de facto standard for obtaining structured output from language models.
9	XGrammar~\cite{dong2025xgrammar} partitions the vocabulary into context-independent and context-dependent tokens and maintains persistent pushdown automata across decoding steps, achieving up to 100$\times$ speedup over prior CFG-constrained decoding methods.
10	Outlines~\cite{willard2023outlines} reformulates constrained generation as finite-state machine transitions with offline vocabulary indexing, which enables efficient enforcement of regular-expression and JSON-schema constraints without runtime overhead per token.
11	LMQL~\cite{beurer-kellner2023lmql} introduces a declarative query language that compiles type, length, and regex constraints into token-level masks, providing a programmable interface for specifying multi-variable output structures.
12	These systems ensure that every generated token belongs to a grammar-valid continuation, but they do not address the \emph{distribution distortion} introduced by naive token masking.
13	A parallel line of work tackles this problem directly: DOMINO~\cite{beurer-kellner2024domino} minimizes distributional divergence during CFG enforcement by formulating mask selection as an optimization problem, and ASAp~\cite{park2024grammar} provides a provably unbiased sampling algorithm that preserves the original LM distribution under grammar constraints.
14	Together, these advances have made grammar-constrained decoding both fast and statistically principled, and provide a robust foundation for 
…[truncated 19735 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 904
}
```

</details>

---


### Tool call

_source line 812 · 2026-05-19T08:44:54.911175+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 813 · 2026-05-19T08:44:58.327953+00:00_

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
26	The two-layer architecture produces two distinct fallback mechanisms with different semant
…[truncated 31971 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 3416
}
```

</details>

---


### Tool call

_source line 814 · 2026-05-19T08:44:58.479422+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie--claude-sessions-review-reviewer-2-cbe93d98/636186fc-ce2c-43f5-94cc-f52bf1a930a5/tool-results/toolu_01HPTV8RzmiXX9r7PRFeoDN7.txt",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie--claude-sessions-review-reviewer-2-cbe93d98/636186fc-ce2c-43f5-94cc-f52bf1a930a5/tool-results/toolu_01HPTV8RzmiXX9r7PRFeoDN7.txt",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 815 · 2026-05-19T08:44:58.732586+00:00_

1	{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 69, \"total_citations\": 97, \"unique_cited_keys\": 58, \"orphan_bib\": 10, \"missing_bib\": 0, \"duplicate_keys\": 1, \"online_verified\": 53, \"online_not_found\": 4, \"online_mismatch\": 11}, \"cross_check\": {\"orphan_bib\": [\"delafuente2025guidex\", \"geng2025jsonschemabench\", \"lee2026formattax\", \"lu2025schemarl\", \"paolini2021tanl\", \"park2024grammaraligned\", \"reddy2026dccd\", \"sakota2025boostcd\", \"shen2025slot\", \"vukovic2024dore\"], \"missing_bib\": [], \"orphan_count\": 10, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"synchromesh_iclr2022\", \"type\": \"inproceedings\", \"title\": \"Synchromesh: Reliable Code Generation from Pre-trained Language Models\", \"authors\": \"Poesia, Gabriel and Polozov, Oleksandr and Le, Vu and Tiwari, Ashish and Soares,...\", \"year\": \"2022\", \"venue\": \"International Conference on Learning Representations\"}, {\"key\": \"mgd_neurips2023\", \"type\": \"inproceedings\", \"title\": \"Monitor-Guided Decoding of Code LMs with Static Analysis of Repository Context\", \"authors\": \"Agrawal, Lakshya A. and Kanade, Aditya and Goyal, Navin and Lahiri, Shuvendu K. ...\", \"year\": \"2023\", \"venue\": \"Advances in Neural Information Processing Systems\"}, {\"key\": \"pldi2025_type_constrained_codegen\", \"type\": \"article\", \"title\": \"Type-Constrained Code Generation with Language Models\", \"authors\": \"M\\\\\\\"undler, Niels and He, Jingxuan and Wang, Hao and Sen, Koushik and Song, Dawn ...\", \"year\": \"2025\", \"venue\": \"Proceedings of the ACM on Programming Languages\"}, {\"key\": \"roth_yih_2004\", \"type\": \"inproceedings\", \"title\": \"A Linear Programming Formulation for Global Inference in Natural Language Tasks\", \"authors\": \"Roth, Dan and Yih, Wen-tau\", \"year\": \"2004\", \"venue\": \"Proceedings of the Eighth Conference on Computational Natural Language Learning ...\"}, {\"key\": \"adakgc_emnlp2023\", \"
…[truncated 56091 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 253
}
```

</details>

---


### Tool call

_source line 816 · 2026-05-19T08:45:07.686166+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_prompts.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_prompts.tex"
  }
}
```

</details>

---


### Tool result

_source line 817 · 2026-05-19T08:45:08.138910+00:00_

1	% Appendix — Prompt Templates
2	% W10: Extraction prompts used in all experiments.
3	
4	\section{Prompt Templates}
5	\label{app:prompts}
6	
7	All experiments use the same prompts across constrained and unconstrained decoding; constraints are applied at the logit level, not through prompt modification.
8	Table~\ref{tab:prompts} shows the system and user prompts for each dataset.
9	
10	\begin{table*}[t]
11	\centering
12	\small
13	\begin{tabular}{@{}p{0.95\textwidth}@{}}
14	\toprule
15	\textbf{SciERC --- System Prompt (Unconstrained \& Constrained)} \\
16	\midrule
17	\texttt{You are an expert information extraction system for scientific texts. Extract entities and relations from the given text.} \\[4pt]
18	\texttt{Entity types: Task, Method, Material, Metric, OtherScientificTerm, Generic} \\
19	\texttt{Relation types: Used-for, Feature-of, Hyponym-of, Part-of, Compare, Conjunction, Evaluate-for} \\[4pt]
20	\texttt{Output a JSON object with:} \\
21	\texttt{- "entities": list of \{"text": "...", "type": "..."\}} \\
22	\texttt{- "relations": list of \{"head": "...", "tail": "...", "type": "...", "head\_type": "...", "tail\_type": "..."\}} \\[4pt]
23	\texttt{Output ONLY valid JSON, no explanation.} \\
24	\midrule
25	\textbf{SciERC --- User Prompt} \\
26	\midrule
27	\texttt{Extract all entities and relations from this scientific text:} \\
28	\texttt{"\{text\}"} \\
29	\texttt{Output JSON:} \\
30	\midrule
31	\midrule
32	\textbf{DocRED --- System Prompt (Unconstrained \& Constrained)} \\
33	\midrule
34	\texttt{You are an information extraction system. Extract all entities and relations from the following document.} \\[4pt]
35	\texttt{Entity types: PER, ORG, LOC, TIME, NUM, MISC} \\[4pt]
36	\texttt{Relation types: country, instance of, performer, ...\ (96 Wikidata relation types; full list omitted for space)} \\[4pt]
37	\texttt{Output a JSON object with exactly this structure:} \\
38	\texttt{\{"entities": [\{"text": "entity name", "type": "ENTITY\_TYPE"\}],} \\
39	\texttt{\ "
…[truncated 770 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 818 · 2026-05-19T08:45:08.139317+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_reproducibility.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_reproducibility.tex"
  }
}
```

</details>

---


### Tool result

_source line 819 · 2026-05-19T08:45:09.045923+00:00_

1	\section{Reproducibility Details}
2	\label{app:reproducibility}
3	
4	\paragraph{Fine-tuning configuration.}
5	All four fine-tuned models (Qwen3-8B and Llama-3.1-8B-Instruct on SciERC and DocRED) use identical LoRA hyperparameters: rank $r{=}16$, $\alpha{=}32$, dropout $0.05$, no bias, targeting all attention and MLP projection layers (\texttt{q\_proj}, \texttt{k\_proj}, \texttt{v\_proj}, \texttt{o\_proj}, \texttt{gate\_proj}, \texttt{up\_proj}, \texttt{down\_proj}).
6	Training uses AdamW with learning rate $2{\times}10^{-4}$, cosine schedule, warmup ratio $0.1$, effective batch size $16$, bf16 precision, gradient checkpointing, and completion-only loss for 3 epochs.
7	SciERC trains on 1,762 examples (260 dev) for 333 steps; DocRED trains on 3,053 examples (998 dev) for 573 steps.
8	Maximum sequence length is 2,048 (SciERC) and 4,096 (DocRED).
9	All runs use seed 42.
10	
11	\paragraph{Hardware and software.}
12	Training runs on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (98\,GB VRAM).
13	SciERC fine-tuning takes approximately 11 minutes per model; DocRED takes approximately 1.5 hours.
14	Software versions: PyTorch 2.10, Transformers 4.57, PEFT 0.19, TRL 1.1, Accelerate 1.13.
15	
16	\paragraph{Inference time.}
17	Inference timing is reported in Appendix~\ref{app:runtime} (NVIDIA RTX PRO 6000 Blackwell Server Edition GPU, same hardware as training).
18	Full S1 constrained decoding adds $+$13.1\% wall-clock overhead on SciERC and $+$2.43\% on DocRED (Qwen3-8B, zero-shot greedy); under LoRA fine-tuning, overhead is $+$10.0\% on SciERC.
19	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 906
}
```

</details>

---


### Tool call

_source line 820 · 2026-05-19T08:45:09.197082+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_sampling_table.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_sampling_table.tex"
  }
}
```

</details>

---


### Tool result

_source line 821 · 2026-05-19T08:45:09.600221+00:00_

1	\section{Sampling Robustness}\label{app:sampling}
2	
3	\begin{table}[h]
4	\centering
5	\caption{Constraint robustness under nucleus sampling ($T$=0.7, $p$=0.9) vs.\ greedy decoding (Qwen3-8B, full S1 constraints).}
6	\label{tab:sampling-robustness}
7	\begin{tabular}{llcccccc}
8	\toprule
9	Dataset & Decoding & ET\% & RV\% & DR\% & CF\% & E-F1 & R-F1 \\
10	\midrule
11	\multirow{2}{*}{SciERC (551)} & Greedy & 0 & 0 & 0.93 & 9.90 & 30.98 & 8.36 \\
12	& Sampling & 0 & 0 & 0.75 & 9.90 & 31.28 & 7.42 \\
13	\midrule
14	\multirow{2}{*}{DocRED (114$^\dagger$)} & Greedy & 0 & 0.03 & 10.21 & 2.57 & 59.37 & 8.23 \\
15	& Sampling & 0 & 0 & 10.31 & 12.63 & 57.05 & 7.92 \\
16	\bottomrule
17	\end{tabular}
18	\par\smallskip\footnotesize $^\dagger$Subset of 114 documents; full DocRED sampling requires ${\sim}300$h due to extended generation under high-temperature sampling with complex schemas.
19	\end{table}
20	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 403
}
```

</details>

---


### Tool call

_source line 822 · 2026-05-19T08:45:09.600583+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_beam_search.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_beam_search.tex"
  }
}
```

</details>

---


### Tool result

_source line 823 · 2026-05-19T08:45:09.903245+00:00_

1	\section{Beam Search Compatibility}
2	\label{app:beam-search}
3	
4	OntoCoDec's constraint enforcement is designed to be decoding-strategy agnostic.
5	The main experiments (\S\ref{sec:experiments}) use greedy decoding; Appendix~\ref{app:sampling} validates nucleus sampling.
6	Here we verify compatibility with beam search, completing coverage of the three standard decoding strategies.
7	
8	\paragraph{Implementation challenges.}
9	Two stateful components require adaptation for beam search.
10	(1)~The grammar layer (XGrammar) maintains an internal \texttt{GrammarMatcher} state that tracks the generated token sequence; beam reordering invalidates this state because beams are permuted across steps.
11	Our solution instantiates a fresh \texttt{GrammarMatcher} per beam per step and replays the beam's current token sequence through XGrammar's stateless accept API (64 lines of code).
12	(2)~The semantic layer's \texttt{TypeConstraintProcessor} accumulates entity and relation registries that assume a single generation path.
13	Our solution isolates state per beam by calling \texttt{detect()} on the full partial output at each step, reconstructing all entity/relation state from scratch for each beam independently (61 lines of code).
14	Both adaptations add ${\sim}125$ lines total without modifying the existing greedy/sampling logic.
15	
16	\paragraph{Results.}
17	Table~\ref{tab:beam-search} compares beam search ($k{=}4$, \texttt{early\_stopping=True}) against greedy decoding under full S1 constraints across six model-dataset combinations.
18	
19	\begin{table}[h]
20	\centering
21	\small
22	\caption{Beam search ($k{=}4$) vs.\ greedy decoding under full S1 constraints.
23	SciERC evaluated on full test set (551 documents); DocRED evaluated on matched 50-document subsets (same documents for greedy and beam).
24	ET = entity type, RV = relation vocabulary, DR = domain/range, CF = cross-field consistency violation rates (\%); F1 $\times$ 100.}
25	\label{tab:beam-search}
26	\begin{tab
…[truncated 8172 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 302
}
```

</details>

---


### Tool call

_source line 824 · 2026-05-19T08:45:09.903804+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_scalability.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_scalability.tex"
  }
}
```

</details>

---


### Tool result

_source line 825 · 2026-05-19T08:45:09.954492+00:00_

1	\section{Ontology Scalability}
2	\label{app:scalability}
3	
4	\begin{table}[h]
5	\centering
6	\small
7	\resizebox{\columnwidth}{!}{%
8	\begin{tabular}{@{}lrrrr@{}}
9	\toprule
10	\textbf{Scale} & \textbf{Types} & \textbf{Rels} & \textbf{Compile (s)} & \textbf{Overhead} \\
11	\midrule
12	Small (SciERC) & 6 & 7 & 0.33 & 1.02$\times$ \\
13	Medium (DocRED) & 6 & 96 & 0.32 & 1.03$\times$ \\
14	Large (synth.) & 100 & 500 & 0.35 & 1.03$\times$ \\
15	XLarge (synth.) & 200 & 1{,}000 & 0.42 & 1.03$\times$ \\
16	\bottomrule
17	\end{tabular}}
18	\caption{Compilation time (one-time) and per-token inference overhead across ontology scales. Small and Medium use real ontologies; Large and XLarge use synthetic ontologies with random domain/range constraints. Overhead measured on Qwen3-8B, 10 documents per scale.}
19	\label{tab:scalability}
20	\end{table}
21	
22	Grammar compilation scales sub-linearly (0.33\,s to 0.37\,s for 7$\to$1{,}000 relations); semantic constraint compilation grows linearly but remains negligible (0.4\,ms to 17\,ms).
23	Inference overhead is constant at 2--3\% because XGrammar uses precompiled bitmasks ($O(1)$ per token) and the semantic layer checks only the active relation's domain/range set rather than the full ontology.
24	The practical limit is first-token uniqueness: when entity types exceed $\sim$200, prefix collisions in the tokenizer vocabulary may require fallback to multi-token disambiguation (\S\ref{sec:dynamic-masking}).
25	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 826 · 2026-05-19T08:45:14.391617+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_case_studies.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_case_studies.tex"
  }
}
```

</details>

---


### Tool result

_source line 827 · 2026-05-19T08:45:14.693406+00:00_

1	% Appendix — Error Analysis and Case Studies
2	
3	\section{Error Analysis and Case Studies}
4	\label{app:case-studies}
5	
6	\definecolor{violation}{RGB}{220,50,50}
7	\definecolor{fixed}{RGB}{34,139,34}
8	\definecolor{cfwarn}{RGB}{200,120,0}
9	
10	We present four representative cases illustrating constraint behavior across violation types. Cases 1--3 demonstrate OntoCoDec's corrective mechanisms; Case 4 illustrates a limitation.
11	
12	\subsection{Domain-Range Correction}
13	\label{app:case-dr}
14	
15	\noindent\textbf{Input (SciERC, Qwen3-8B):} \textit{``We present a novel model-based approach to recover the shapes and the poses of transparent objects from known motion.''}
16	
17	The unconstrained model assigns \textsc{OtherScientificTerm} to ``shapes'' and ``poses,'' producing \textsc{Feature-of}(\textsc{Task}, \textsc{OtherScientificTerm}) triples that violate domain/range constraints. The semantic layer redirects the tail type to \textsc{Task}, yielding schema-compliant triples (Table~\ref{tab:case1}).
18	
19	\begin{table}[h]
20	\centering
21	\small
22	\caption{OntoCoDec corrects three Feature-of DR violations. \textcolor{violation}{Red} = violation; \textcolor{fixed}{green} = corrected.}
23	\label{tab:case1}
24	\begin{tabular}{@{}p{3.2cm}lll@{}}
25	\toprule
26	\textbf{Triple} & \textbf{Head} & \textbf{Tail} & \textbf{DR} \\
27	\midrule
28	\multicolumn{4}{@{}l}{\textit{Unconstrained (3 violations)}} \\
29	\midrule
30	Feature-of(recover, shapes) & Task & \textcolor{violation}{OtherSciTerm} & \textcolor{violation}{\ding{55}} \\
31	Feature-of(recover, poses) & Task & \textcolor{violation}{OtherSciTerm} & \textcolor{violation}{\ding{55}} \\
32	Feature-of(recover, transp.\ obj.) & Task & \textcolor{violation}{OtherSciTerm} & \textcolor{violation}{\ding{55}} \\
33	Used-for(model approach, recover) & Method & Task & \ding{51} \\
34	\midrule
35	\multicolumn{4}{@{}l}{\textit{OntoCoDec (0 violations)}} \\
36	\midrule
37	Feature-of(recover, shapes) & Task & \textcolor{fixe
…[truncated 5952 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 828 · 2026-05-19T08:45:14.693874+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_doc_length.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_doc_length.tex"
  }
}
```

</details>

---


### Tool result

_source line 829 · 2026-05-19T08:45:15.798991+00:00_

1	\section{Effect of Document Length on Constraint Effectiveness}
2	\label{app:doc-length}
3	
4	To examine whether OntoCoDec's constraint effectiveness varies with document complexity, we partition test documents into three length bins (tertile split by word count) and report per-bin violation counts and F1.
5	
6	\begin{table}[h]
7	\centering
8	\small
9	\caption{Document length breakdown on SciERC (Qwen3-8B). Tertile boundaries: Short $\leq$ 19 words, Medium $\leq$ 27, Long $>$ 27.}
10	\label{tab:doc-length-scierc}
11	\begin{tabular}{ll rrrrr rr}
12	\toprule
13	\textbf{Bin} & \textbf{Mode} & \textbf{ET} & \textbf{RV} & \textbf{DR} & \textbf{CF} & \textbf{Total} & \textbf{E-F1} & \textbf{R-F1} \\
14	\midrule
15	Short (196)  & Uncon. &  1 &  5 &  57 & 0 &  63 & 32.4 &  8.9 \\
16	             & Const. &  0 &  0 &   5 & 5 &  10 & 32.4 &  8.9 \\
17	\midrule
18	Medium (180) & Uncon. &  6 &  9 & 104 & 0 & 119 & 27.8 &  6.7 \\
19	             & Const. &  0 &  0 &   7 & 15 & 22 & 27.8 &  6.7 \\
20	\midrule
21	Long (175)   & Uncon. &  3 & 10 & 104 & 1 & 118 & 29.9 &  7.0 \\
22	             & Const. &  0 &  0 &   4 & 20 & 24 & 30.0 &  7.3 \\
23	\bottomrule
24	\end{tabular}
25	\end{table}
26	
27	\begin{table}[h]
28	\centering
29	\small
30	\caption{Document length breakdown on DocRED (Qwen3-8B). Tertile boundaries: Short $\leq$ 160 words, Medium $\leq$ 208, Long $>$ 208.}
31	\label{tab:doc-length-docred}
32	\begin{tabular}{ll rrrrr rr}
33	\toprule
34	\textbf{Bin} & \textbf{Mode} & \textbf{ET} & \textbf{RV} & \textbf{DR} & \textbf{CF} & \textbf{Total} & \textbf{E-F1} & \textbf{R-F1} \\
35	\midrule
36	Short (336)  & Uncon. & 177 & 1238 & 1021 &   9 & 2445 & 61.1 &  9.3 \\
37	             & Const. &   0 &    0 &  495 & 138 &  633 & 62.6 &  9.6 \\
38	\midrule
39	Medium (332) & Uncon. & 147 & 1742 & 1047 &   5 & 2941 & 59.3 &  7.9 \\
40	             & Const. &   0 &    5 &  544 & 180 &  729 & 60.7 &  8.5 \\
41	\midrule
42	Long (330)   & Uncon. & 176 & 2209 & 1162 &   3 & 3550 & 53.9 
…[truncated 1432 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1105
}
```

</details>

---


### Tool call

_source line 830 · 2026-05-19T08:45:15.900083+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_prompt_sensitivity.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_prompt_sensitivity.tex"
  }
}
```

</details>

---


### Tool result

_source line 831 · 2026-05-19T08:45:15.950885+00:00_

1	\section{Prompt Sensitivity Analysis}
2	\label{app:prompt-sensitivity}
3	
4	To verify that OntoCoDec's constraint enforcement is robust to prompt variation, we evaluate three prompt variants on SciERC using Qwen3-8B (551 test documents): \textbf{Default} (the prompt used in all main experiments), \textbf{Minimal} (a shortened version listing only entity/relation types), and \textbf{Detailed} (an extended version with type definitions and extraction guidelines). All three variants share the same output JSON schema; only the instruction text differs. Each variant is decoded in both unconstrained and constrained (full Stage~1) modes.
5	
6	\begin{table}[h]
7	\centering
8	\small
9	\caption{Prompt sensitivity results on SciERC (Qwen3-8B, 551 documents). ET, RV, DR denote entity-type, relation-vocabulary, and domain-range violation rates (\%), respectively. $\Delta$DR shows the relative reduction from unconstrained to constrained decoding.}
10	\label{tab:prompt-sensitivity}
11	\begin{tabular}{llcccccc}
12	\toprule
13	\textbf{Prompt} & \textbf{Mode} & \textbf{ET\%} & \textbf{RV\%} & \textbf{DR\%} & \textbf{$\Delta$DR} & \textbf{E-F1} & \textbf{R-F1} \\
14	\midrule
15	\multirow{2}{*}{Default}
16	  & Unconstrained & 0.40 & 1.39 & 15.37 & \multirow{2}{*}{94.0\%} & 31.01 & 8.23 \\
17	  & Constrained   & 0.00 & 0.00 &  0.93 &                         & 30.98 & 8.36 \\
18	\midrule
19	\multirow{2}{*}{Minimal}
20	  & Unconstrained & 0.58 & 1.16 & 16.91 & \multirow{2}{*}{94.6\%} & 31.98 & 7.91 \\
21	  & Constrained   & 0.00 & 0.00 &  0.92 &                         & 31.99 & 7.85 \\
22	\midrule
23	\multirow{2}{*}{Detailed}
24	  & Unconstrained & 0.22 & 0.45 & 11.07 & \multirow{2}{*}{94.2\%} & 33.55 & 10.48 \\
25	  & Constrained   & 0.00 & 0.00 &  0.64 &                         & 33.56 & 10.48 \\
26	\bottomrule
27	\end{tabular}
28	\end{table}
29	
30	Table~\ref{tab:prompt-sensitivity} shows that constrained decoding eliminates entity-type and relation-vocabulary violations entirely (E
…[truncated 954 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 832 · 2026-05-19T08:45:16.403145+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_full_ft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_full_ft.tex"
  }
}
```

</details>

---


### Tool result

_source line 833 · 2026-05-19T08:45:16.704832+00:00_

1	\section{Full Fine-Tuning Baseline}
2	\label{app:full-ft}
3	
4	To verify that constraint effectiveness generalizes beyond LoRA, we evaluate Qwen3-8B with full-parameter fine-tuning on SciERC (same data, 3 epochs, lr=$2{\times}10^{-4}$, seed 42).
5	
6	\begin{table}[h]
7	\centering
8	\small
9	\begin{tabular}{@{}lrrrr@{}}
10	\toprule
11	& \textbf{E-F1} & \textbf{R-F1} & \textbf{DR\%} & \textbf{CF\%} \\
12	\midrule
13	Full FT unconstrained & 64.78 & 37.89 & 2.74 & 0 \\
14	Full FT + S1 & 64.78 & 37.89 & \textbf{0} & 1.31 \\
15	\midrule
16	LoRA unconstrained & 66.86 & 43.65 & 0.31 & 0 \\
17	LoRA + S1 & 67.05 & 43.77 & \textbf{0} & 1.18 \\
18	\bottomrule
19	\end{tabular}
20	\caption{Full fine-tuning vs.\ LoRA on SciERC (Qwen3-8B, 551 docs). Constraints eliminate DR under both methods. Full FT underperforms LoRA, likely due to an untuned learning rate ($2{\times}10^{-4}$, standard for LoRA but high for full FT). F1 is unaffected by constraints in both cases.}
21	\label{tab:full-ft}
22	\end{table}
23	
24	Full fine-tuning retains 2.74\% DR violations (30 triples), concentrated in Part-of (14.6\%), Hyponym-of (9.6\%), and Evaluate-for (8.4\%). S1 eliminates all 30 violations with no F1 cost, which confirms that constraint enforcement is effective regardless of the fine-tuning method. The CF$\leftrightarrow$DR trade-off persists (CF 0\%$\to$1.31\%), consistent with the LoRA pattern (1.18\%).
25	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 834 · 2026-05-19T08:45:16.755464+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_llama_per_relation.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_llama_per_relation.tex"
  }
}
```

</details>

---


### Tool result

_source line 835 · 2026-05-19T08:45:16.806290+00:00_

1	% Appendix C — Per-Relation Violation Analysis (Llama-3.1-8B)
2	% exp_ids: llama_docred_unconstrained, llama_docred_full_s1
3	
4	\section{Per-Relation Violation Analysis (Llama-3.1-8B)}\label{app:llama-per-relation}
5	
6	Table~\ref{tab:llama-per-relation-dr} presents the per-relation domain--range violation breakdown for Llama-3.1-8B on DocRED under full S1 constraints.
7	The Llama baseline exhibits an RV rate of 16.03\%, substantially lower than Qwen's 29.66\%, which indicates stronger baseline vocabulary compliance.
8	% exp_ids: llama_docred_unconstrained (RV=16.03%), qwen_docred_unconstrained (RV=29.66%)
9	Full S1 completely eliminates RV violations and reduces the residual DR rate to 2.55\% (418/16{,}368 triples), with only three relations exceeding 10\%.
10	% exp_ids: llama_docred_full_s1 (DR=2.6%, 418/16368)
11	
12	\begin{table}[h]
13	\centering
14	\caption{Top 10 per-relation DR violation rates for Llama-3.1-8B on DocRED under full S1 constraints. Relations with $>$20 triples and 0\% DR (e.g., P131, P206, P361, P170, P86) are omitted.}
15	\label{tab:llama-per-relation-dr}
16	\resizebox{\columnwidth}{!}{%
17	\begin{tabular}{@{}llrrr@{}}
18	\toprule
19	Relation & PID & Triples & DR Violations & DR Rate (\%) \\
20	\midrule
21	dissolved/demolished & P576 & 73 & 24 & 32.9 \\
22	followed by          & P156 & 117 & 24 & 20.5 \\
23	unemployment rate    & P1198 & 15 & 3 & 20.0 \\
24	end time             & P582 & 130 & 21 & 16.2 \\
25	instance of          & P31  & 290 & 37 & 12.8 \\
26	product/material produced & P1056 & 98 & 11 & 11.2 \\
27	location of formation & P740 & 81 & 8 & 9.9 \\
28	head of state        & P35  & 41  & 3  & 7.3 \\
29	applies to jurisdiction & P1001 & 637 & 45 & 7.1 \\
30	conflict             & P607 & 453 & 30 & 6.6 \\
31	\bottomrule
32	\end{tabular}}
33	\end{table}
34	% exp_ids: llama_docred_full_s1
35	
36	Compared with Qwen, which retains a 10.21\% residual DR under full S1 concentrated in P1198 (83\% fallback) and P171 (78\% fallback), Llama
…[truncated 528 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 836 · 2026-05-19T08:48:01.870461+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 — Round 1 审稿意见\n\n**论文**: OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints\n**Venue**: EMNLP 2026 via ACL Rolling Review (ARR)\n**审查侧重**: 新颖性 + 完整性 + 写作质量 + 格式合规\n\n---\n\n## 总体评分\n**Overall Assessment**: 3.0 — Findings\n**一句话总结**: 工程完成度高、实验全面的 schema 约束解码系统，但核心技术贡献（entity registry + dynamic masking）的算法新颖性有限，且 CF 副作用是未解决的根本性缺陷。\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 主要 claim 有实验支撑，但 dual-factor 分析仅 n=4、p=0.058；CF trade-off 削弱\"type-safe\"核心叙事 |\n| Excitement | 2.5/5 | 问题定义清晰且实用，但 semantic layer 的技术方案（字典查找 + logit masking）概念上较直接，增量贡献集中于工程实现而非算法创新 |\n| Reproducibility | 4/5 | LoRA 超参、prompt 模板、硬件信息、软件版本均有详细报告；代码承诺 release |\n| Reviewer Confidence | 4/5 | 对 constrained decoding 和 IE 领域熟悉，仔细检查了核心技术和实验 |\n\n---\n\n## 主要优势 (Strengths)\n\n**S1. 全面且诚实的实验评估。** 论文覆盖 3 个数据集（SciERC/DocRED/WikiEvents）、4 个模型（8B-70B）、3 种 tokenizer 家族、3 种解码策略（greedy/sampling/beam），配合 bootstrap 显著性检验，实验覆盖度远超同类工作。对 Mistral 作为 boundary condition 的诚实分析（§5.3）和 CF trade-off 的坦率承认（Limitations, Appendix B）尤其值得肯定。\n\n**S2. Constraint tightness 分析提供有价值的 insight。** κ(r) 指标（Eq. 2）将违规率与 schema 结构量化关联，为理解约束有效性提供了可解释的框架。per-relation 分析（Table 6, Appendix C）展示了 tightness 与残余 DR 的一致性关系。\n\n**S3. 实用性强的部署配置。** LoRA + S1 的推荐配置（DR≤0.20%, R-F1 ±0.6pp, +10% latency）在实际部署中具有明确价值。beam search 进一步消除所有四类违规（Table 8, SciERC）是一个有说服力的结果。\n\n**S4. 与 fine-tuning 的可组合性验证充分。** Table 2 和 Appendix B Table 5 的四向消融清晰展示了每层的独立贡献：fine-tuning 后 grammar 层成为 no-op，semantic 层独立贡献 39-72% DR 降低。这个分析对理解方法的长期价值很有帮助。\n\n**S5. 附录信息密度高。** 14 个附录覆盖 error analysis、prompt sensitivity、document length、scalability 等维度，每个都服务于正文中的特定 claim。CF-DR trade-off 的 pilot ablation（Table 4）尤其有说服力地证明了这是结构性限制而非可调参数。\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] 核心技术新颖性不足，相对已有工作的增量需要更清晰的论证\n\n- 具体位置：§3 Method, §6 Related Work\n- 问题：Grammar 层完全复用 XGrammar（§3.2 明确承认）；semantic 层的核心机制是 entity registry（一个字典 D: name→type，§3.3）+ 动态 logit masking（在 type-bearing position 对 logit 做 mask），这在概念上是直接的查找+过滤操作。论文与 type-constrained code generation（PLDI 2025, Synchromesh, PICARD）的区别被定义为\"动态 entity registry\"——即类型从文本推断而非从声明中读取。但这个区别在实现层面仅体现为：在解码时维护一个字典并在特定 position 查询它，而不需要复杂的类型推导或推理。\n- 论文在 §6 related work 和 Appendix A 中花了大量篇幅论证定位，但未能充分回答：为什么字典查找+条件 masking 构成足够的算法贡献，而不仅是已有范式的工程适配？\n- 为什么影响接收：ARR Excitement 维度要求方法有足够的技术深度。当 grammar 层是现成的、semantic 层是概念直接的，论文的主要贡献实质上是对已有 constrained decoding 范式的 IE 特定适配和全面的工程验证。\n- 建议修改方向：（1）更明确地将贡献定位为\"系统性实证研究+工程框架\"而非方法论创新；（2）深化 constraint tightness 分析使其成为独立的理论贡献（目前 n=4 不够）；（3）或增加在实际 pipeline 中的 end-to-end 验证（如下游 KG construction 的影响）\n\n**N2** [critical] CF trade-off 是未解决的根本缺陷，削弱了\"type-safe\"核心叙事\n\n- 具体位置：Abstract (line 8), §1 Introduction (line 25), §5.1 (line 76), Limitations\n- 问题：Abstract 声称\"near-lossless DR composability\"，但 zero-shot CF 从 0.08% 升至 9.90%（SciERC）和从 0.17% 升至 12.02%（Llama DocRED, Table 3）。CF 违规意味着同一实体在不同三元组中被分配了不同类型——对于 KG 构建来说，这同样是严重的一致性问题。Table 4 (Appendix B) 的 pilot ablation 表明 CF 优先化会将 DR 从 0.93% 推回到 14.78%，证明这是结构性的、不可调和的 trade-off。\n- 论文的回应策略是\"fine-tuning resolves both\"（CF≤1.2%），但这将方法的实用性完全绑定在 fine-tuning 上，而论文用大量篇幅（§5.1-5.3, 占正文约 40%）讨论 zero-shot 场景。如果 zero-shot 场景不可用（因 CF），那正文应当重新分配比例。\n- 为什么影响接收：核心叙事声称的 \"type-safe\" 和 \"violation reduction\" 在 zero-shot 下被 CF 显著抵消。Total type-violation burden（DR+CF, Table 1: 15.45%→10.83%）仅减少 30%，远低于单看 DR 的 94%。\n- 建议修改方向：（1）在 Abstract 和 Introduction 中更前置地讨论 CF trade-off，而非仅在 zero-shot 数据后以括号形式提及；（2）重新定义评价指标为 total violation burden（DR+CF）而非仅 DR；（3）将正文主线调整为 LoRA+S1（CF 已解决），zero-shot 降级为 diagnostic/stress test。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] Zero-shot R-F1 过低（2-8%），实验主体的实际意义有限\n\n- 具体位置：§5.1-5.3, Table 1-3\n- 问题：正文约 40% 内容围绕 zero-shot 评估展开，但 R-F1 仅 2-8%。论文在 Appendix B 辩护这是\"control variable\"，但这个辩护出现在附录而非正文。审稿人首先看到的是 R-F1=8.36 的结果，会立即质疑实际意义。\n- 建议：在正文 §5 开头更早、更明确地说明 zero-shot 评估的定位（stress test for constraint robustness, not deployment scenario），并确保 fine-tuning composability 结果（Table 2）获得更多正文篇幅。\n\n**W2** [warning] 缺少 GoLLIE 直接对比实验\n\n- 具体位置：§6 Related Work (line 18)\n- 问题：论文多次提到 GoLLIE 并声称\"complementary\"（§6: \"a GoLLIE-trained model could use OntoCoDec to eliminate residual violations\"），但未提供 GoLLIE+OntoCoDec 的实验。这是最自然的消融：如果 training-based 方法已经大幅降低违规率，OntoCoDec 的边际贡献是多少？目前仅有 LoRA fine-tuning 的组合验证，未涵盖 schema-aware 训练方法。\n- 建议：至少用 GoLLIE（公开模型和代码）在 SciERC 上跑一组对比，展示 OntoCoDec 的边际贡献。\n\n**W3** [warning] Dual-factor 分析统计效力不足\n\n- 具体位置：Appendix B (Figure 3, line 93)\n- 问题：linear fit 仅 n=4 数据点，df=2，p≈0.058。论文正确地标注为\"descriptive characterization\"，但在正文 §4（line 28）和 Abstract（line 5）中将 constraint tightness 作为核心 insight 推销（\"violation rates correlate with constraint tightness\"），给人的印象超过了统计证据的支撑力度。\n- 建议：（1）增加更多 model×dataset 点以增强统计效力，或（2）在正文中弱化\"correlate\"的措辞，改为\"consistent with\"。\n\n**W4** [warning] WikiEvents 结果以\"preliminary\"呈现但在 Abstract 中占显著位置\n\n- 具体位置：Abstract (line 10), §5.4\n- 问题：WikiEvents 使用 20 文档测试集（数据集本身的限制，非作者选择），但 Abstract 第 10 行\"The framework extends to event extraction without modification\"给出的印象是这已经是经过验证的结论。20 文档的 trigger F1 置信区间极宽（论文承认），这个 claim 的证据基础不足。\n- 建议：Abstract 中加上 \"(preliminary)\" 已有，但应更明确地在正文 §5.4 标题或首段说明样本量限制。目前标题\"Preliminary Extension: Event Extraction\"是好的，但内容叙述的 confidence 可能偏高。\n\n**W5** [warning] Abstract 数字密度过高\n\n- 具体位置：Abstract 全文（12 行）\n- 问题：Abstract 包含约 15 个具体数字（DR≤0.20%, R-F1 ±0.6pp, CF≤1.2%, 76-99%, 9-21%, ≤1.2%, 8B-70B 等），审稿人在 30 秒内无法消化。核心 message 被数据淹没。\n- 建议：保留 3-4 个最关键数字，其余移至正文。例如：\"near-zero DR with negligible F1 cost under fine-tuning\" 比 \"DR≤0.20% with R-F1 within ±0.6pp\" 在 Abstract 中更有效。\n\n**W6** [warning] entity registry 的 correctness 依赖于生成顺序假设\n\n- 具体位置：§3.3 (Entity registry, line 59), §3.1 (line 28)\n- 问题：semantic layer 依赖固定字段顺序（head→tail→relation→head_type→tail_type, §3.1 line 28）来确保 relation type 在 entity type 之前生成。这个设计被呈现为自然选择，但实际上是一个重要的架构约束。如果 LLM 的生成顺序不遵循 JSON schema 的字段顺序（即使有 grammar 约束，某些 schema 也允许字段重排），系统会 fail silently。论文假设 XGrammar 强制字段顺序，但未明确讨论这一依赖。\n- 建议：在 §3.1 或 §3.2 中明确说明字段顺序是通过 JSON Schema 的 `additionalProperties: false` + 特定 property order 强制的，而非仅是\"deterministic grammar compilation\"。\n\n---\n\n## 小问题（不影响接收）\n\n- **BibTeX 清理**: 10 个 orphan entries（在 .bib 中但未被引用），包括 `paolini2021tanl`, `vukovic2024dore` 等。1 个 duplicate key（`schall2025hiddencost` 出现两次）。应在提交前清理。\n- **DocRED 评估说明**: §5 脚注提到\"dev set\"评估，但正文 Table 2 caption 说\"998 docs\"未标明是 dev set。应在 Table 2 caption 或正文中明确标注。\n- **S1/S2 命名**: \"S1\" 和 \"S2\" 作为策略名在 §3.5 定义，但在 §5 之前较少使用，导致读者在 Table 1 看到时需要回翻。建议在 Table 1 caption 中简要定义。\n- **Scalability table (Appendix K)**: compile time 从 0.33s (SciERC, 7 rels) 到 0.42s (1000 rels) 变化非常小，但正文 §5 runtime 段说\"one-time 44ms\"，与 Appendix K 的 0.33s 不一致。应统一。\n- **\"Training-free\" 措辞**: Abstract line 11 和 §6 多处声称 \"training-free\"，但推荐配置是 LoRA+S1（需要 fine-tuning）。应区分框架本身是 training-free 和推荐部署需要 fine-tuning。\n\n---\n\n## Missing References\n\n1. **TANL** (Paolini et al., 2021) — 已在 .bib 中但未被引用。作为 structured prediction as text generation 的早期工作，应在 Related Work §6 schema-aware IE 段落引用。\n2. **BoostCD** (Sakota et al., 2025) — 已在 Related Work 引用但无实验对比。作为直接将 constrained decoding 应用于 IE 的最新工作，应是最重要的 baseline 之一。\n\n---\n\n## Overall Assessment 详细理由\n\n**给分 3.0（Findings）的依据：**\n\n论文解决了一个清晰且实际的问题（LLM IE 中的 type violation），提供了全面的实验验证，写作质量总体良好。Constraint tightness 分析和 composability 验证都有价值。\n\n但三个因素阻止了 Conference 级别的评分：\n1. **技术新颖性有限**：grammar 层复用 XGrammar，semantic 层是字典查找+条件 masking 的直接实现，主要贡献是工程适配和实证验证，而非算法创新。\n2. **CF trade-off 未解决**：方法在减少 DR 的同时引入了显著的 CF 违规（zero-shot 最高 12%），总违规 burden 的降低远不如单看 DR 那么引人注目。\n3. **最强结果依赖 fine-tuning**：推荐配置（LoRA+S1）需要 task-specific training，削弱了 \"training-free\" 的核心叙事。\n\n适合 Findings track 的理由：solid engineering contribution with thorough evaluation, practical value for IE deployment, honest treatment of limitations, and a useful analytical framework (constraint tightness)。但作为 Conference paper，缺少足够的算法深度或 surprising insight。",
  "reviewer_id": "2",
  "project": "schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 — Round 1 审稿意见\n\n**论文**: OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints\n**Venue**: EMNLP 2026 via ACL Rolling Review (ARR)\n**审查侧重**: 新颖性 + 完整性 + 写作质量 + 格式合规\n\n---\n\n## 总体评分\n**Overall Assessment**: 3.0 — Findings\n**一句话总结**: 工程完成度高、实验全面的 schema 约束解码系统，但核心技术贡献（entity registry + dynamic masking）的算法新颖性有限，且 CF 副作用是未解决的根本性缺陷。\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 主要 claim 有实验支撑，但 dual-factor 分析仅 n=4、p=0.058；CF trade-off 削弱\"type-safe\"核心叙事 |\n| Excitement | 2.5/5 | 问题定义清晰且实用，但 semantic layer 的技术方案（字典查找 + logit masking）概念上较直接，增量贡献集中于工程实现而非算法创新 |\n| Reproducibility | 4/5 | LoRA 超参、prompt 模板、硬件信息、软件版本均有详细报告；代码承诺 release |\n| Reviewer Confidence | 4/5 | 对 constrained decoding 和 IE 领域熟悉，仔细检查了核心技术和实验 |\n\n---\n\n## 主要优势 (Strengths)\n\n**S1. 全面且诚实的实验评估。** 论文覆盖 3 个数据集（SciERC/DocRED/WikiEvents）、4 个模型（8B-70B）、3 种 tokenizer 家族、3 种解码策略（greedy/sampling/beam），配合 bootstrap 显著性检验，实验覆盖度远超同类工作。对 Mistral 作为 boundary condition 的诚实分析（§5.3）和 CF trade-off 的坦率承认（Limitations, Appendix B）尤其值得肯定。\n\n**S2. Constraint tightness 分析提供有价值的 insight。** κ(r) 指标（Eq. 2）将违规率与 schema 结构量化关联，为理解约束有效性提供了可解释的框架。per-relation 分析（Table 6, Appendix C）展示了 tightness 与残余 DR 的一致性关系。\n\n**S3. 实用性强的部署配置。** LoRA + S1 的推荐配置（DR≤0.20%, R-F1 ±0.6pp, +10% latency）在实际部署中具有明确价值。beam search 进一步消除所有四类违规（Table 8, SciERC）是一个有说服力的结果。\n\n**S4. 与 fine-tuning 的可组合性验证充分。** Table 2 和 Appendix B Table 5 的四向消融清晰展示了每层的独立贡献：fine-tuning 后 grammar 层成为 no-op，semantic 层独立贡献 39-72% DR 降低。这个分析对理解方法的长期价值很有帮助。\n\n**S5. 附录信息密度高。** 14 个附录覆盖 error analysis、prompt sensitivity、document length、scalability 等维度，每个都服务于正文中的特定 claim。CF-DR trade-off 的 pilot ablation（Table 4）尤其有说服力地证明了这是结构性限制而非可调参数。\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] 核心技术新颖性不足，相对已有工作的增量需要更清晰的论证\n\n- 具体位置：§3 Method, §6 Related Work\n- 问题：Grammar 层完全复用 XGrammar（§3.2 明确承认）；semantic 层的核心机制是 entity registry（一个字典 D: name→type，§3.3）+ 动态 logit masking（在 type-bearing position 对 logit 做 mask），这在概念上是直接的查找+过滤操作。论文与 type-constrained code generation（PLDI 2025, Synchromesh, PICARD）的区别被定义为\"动态 entity registry\"——即类型从文本推断而非从声明中读取。但这个区别在实现层面仅体现为：在解码时维护一个字典并在特定 position 查询它，而不需要复杂的类型推导或推理。\n- 论文在 §6 related work 和 Appendix A 中花了大量篇幅论证定位，但未能充分回答：为什么字典查找+条件 masking 构成足够的算法贡献，而不仅是已有范式的工程适配？\n- 为什么影响接收：ARR Excitement 维度要求方法有足够的技术深度。当 grammar 层是现成的、semantic 层是概念直接的，论文的主要贡献实质上是对已有 constrained decoding 范式的 IE 特定适配和全面的工程验证。\n- 建议修改方向：（1）更明确地将贡献定位为\"系统性实证研究+工程框架\"而非方法论创新；（2）深化 constraint tightness 分析使其成为独立的理论贡献（目前 n=4 不够）；（3）或增加在实际 pipeline 中的 end-to-end 验证（如下游 KG construction 的影响）\n\n**N2** [critical] CF trade-off 是未解决的根本缺陷，削弱了\"type-safe\"核心叙事\n\n- 具体位置：Abstract (line 8), §1 Introduction (line 25), §5.1 (line 76), Limitations\n- 问题：Abstract 声称\"near-lossless DR composability\"，但 zero-shot CF 从 0.08% 升至 9.90%（SciERC）和从 0.17% 升至 12.02%（Llama DocRED, Table 3）。CF 违规意味着同一实体在不同三元组中被分配了不同类型——对于 KG 构建来说，这同样是严重的一致性问题。Table 4 (Appendix B) 的 pilot ablation 表明 CF 优先化会将 DR 从 0.93% 推回到 14.78%，证明这是结构性的、不可调和的 trade-off。\n- 论文的回应策略是\"fine-tuning resolves both\"（CF≤1.2%），但这将方法的实用性完全绑定在 fine-tuning 上，而论文用大量篇幅（§5.1-5.3, 占正文约 40%）讨论 zero-shot 场景。如果 zero-shot 场景不可用（因 CF），那正文应当重新分配比例。\n- 为什么影响接收：核心叙事声称的 \"type-safe\" 和 \"violation reduction\" 在 zero-shot 下被 CF 显著抵消。Total type-violation burden（DR+CF, Table 1: 15.45%→10.83%）仅减少 30%，远低于单看 DR 的 94%。\n- 建议修改方向：（1）在 Abstract 和 Introduction 中更前置地讨论 CF trade-off，而非仅在 zero-shot 数据后以括号形式提及；（2）重新定义评价指标为 total violation burden（DR+CF）而非仅 DR；（3）将正文主线调整为 LoRA+S1（CF 已解决），zero-shot 降级为 diagnostic/stress test。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] Zero-shot R-F1 过低（2-8%），实验主体的实际意义有限\n\n- 具体位置：§5.1-5.3, Table 1-3\n- 问题：正文约 40% 内容围绕 zero-shot 评估展开，但 R-F1 仅 2-8%。论文在 Appendix B 辩护这是\"control variable\"，但这个辩护出现在附录而非正文。审稿人首先看到的是 R-F1=8.36 的结果，会立即质疑实际意义。\n- 建议：在正文 §5 开头更早、更明确地说明 zero-shot 评估的定位（stress test for constraint robustness, not deployment scenario），并确保 fine-tuning composability 结果（Table 2）获得更多正文篇幅。\n\n**W2** [warning] 缺少 GoLLIE 直接对比实验\n\n- 具体位置：§6 Related Work (line 18)\n- 问题：论文多次提到 GoLLIE 并声称\"complementary\"（§6: \"a GoLLIE-trained model could use OntoCoDec to eliminate residual violations\"），但未提供 GoLLIE+OntoCoDec 的实验。这是最自然的消融：如果 training-based 方法已经大幅降低违规率，OntoCoDec 的边际贡献是多少？目前仅有 LoRA fine-tuning 的组合验证，未涵盖 schema-aware 训练方法。\n- 建议：至少用 GoLLIE（公开模型和代码）在 SciERC 上跑一组对比，展示 OntoCoDec 的边际贡献。\n\n**W3** [warning] Dual-factor 分析统计效力不足\n\n- 具体位置：Appendix B (Figure 3, line 93)\n- 问题：linear fit 仅 n=4 数据点，df=2，p≈0.058。论文正确地标注为\"descriptive characterization\"，但在正文 §4（line 28）和 Abstract（line 5）中将 constraint tightness 作为核心 insight 推销（\"violation rates correlate with constraint tightness\"），给人的印象超过了统计证据的支撑力度。\n- 建议：（1）增加更多 model×dataset 点以增强统计效力，或（2）在正文中弱化\"correlate\"的措辞，改为\"consistent with\"。\n\n**W4** [warning] WikiEvents 结果以\"preliminary\"呈现但在 Abstract 中占显著位置\n\n- 具体位置：Abstract (line 10), §5.4\n- 问题：WikiEvents 使用 20 文档测试集（数据集本身的限制，非作者选择），但 Abstract 第 10 行\"The framework extends to event extraction without modification\"给出的印象是这已经是经过验证的结论。20 文档的 trigger F1 置信区间极宽（论文承认），这个 claim 的证据基础不足。\n- 建议：Abstract 中加上 \"(preliminary)\" 已有，但应更明确地在正文 §5.4 标题或首段说明样本量限制。目前标题\"Preliminary Extension: Event Extraction\"是好的，但内容叙述的 confidence 可能偏高。\n\n**W5** [warning] Abstract 数字密度过高\n\n- 具体位置：Abstract 全文（12 行）\n- 问题：Abstract 包含约 15 个具体数字（DR≤0.20%, R-F1 ±0.6pp, CF≤1.2%, 76-99%, 9-21%, ≤1.2%, 8B-70B 等），审稿人在 30 秒内无法消化。核心 message 被数据淹没。\n- 建议：保留 3-4 个最关键数字，其余移至正文。例如：\"near-zero DR with negligible F1 cost under fine-tuning\" 比 \"DR≤0.20% with R-F1 within ±0.6pp\" 在 Abstract 中更有效。\n\n**W6** [warning] entity registry 的 correctness 依赖于生成顺序假设\n\n- 具体位置：§3.3 (Entity registry, line 59), §3.1 (line 28)\n- 问题：semantic layer 依赖固定字段顺序（head→tail→relation→head_type→tail_type, §3.1 line 28）来确保 relation type 在 entity type 之前生成。这个设计被呈现为自然选择，但实际上是一个重要的架构约束。如果 LLM 的生成顺序不遵循 JSON schema 的字段顺序（即使有 grammar 约束，某些 schema 也允许字段重排），系统会 fail silently。论文假设 XGrammar 强制字段顺序，但未明确讨论这一依赖。\n- 建议：在 §3.1 或 §3.2 中明确说明字段顺序是通过 JSON Schema 的 `additionalProperties: false` + 特定 property order 强制的，而非仅是\"deterministic grammar compilation\"。\n\n---\n\n## 小问题（不影响接收）\n\n- **BibTeX 清理**: 10 个 orphan entries（在 .bib 中但未被引用），包括 `paolini2021tanl`, `vukovic2024dore` 等。1 个 duplicate key（`schall2025hiddencost` 出现两次）。应在提交前清理。\n- **DocRED 评估说明**: §5 脚注提到\"dev set\"评估，但正文 Table 2 caption 说\"998 docs\"未标明是 dev set。应在 Table 2 caption 或正文中明确标注。\n- **S1/S2 命名**: \"S1\" 和 \"S2\" 作为策略名在 §3.5 定义，但在 §5 之前较少使用，导致读者在 Table 1 看到时需要回翻。建议在 Table 1 caption 中简要定义。\n- **Scalability table (Appendix K)**: compile time 从 0.33s (SciERC, 7 rels) 到 0.42s (1000 rels) 变化非常小，但正文 §5 runtime 段说\"one-time 44ms\"，与 Appendix K 的 0.33s 不一致。应统一。\n- **\"Training-free\" 措辞**: Abstract line 11 和 §6 多处声称 \"training-free\"，但推荐配置是 LoRA+S1（需要 fine-tuning）。应区分框架本身是 training-free 和推荐部署需要 fine-tuning。\n\n---\n\n## Missing References\n\n1. **TANL** (Paolini et al., 2021) — 已在 .bib 中但未被引用。作为 structured prediction as text generation 的早期工作，应在 Related Work §6 schema-aware IE 段落引用。\n2. **BoostCD** (Sakota et al., 2025) — 已在 Related Work 引用但无实验对比。作为直接将 constrained decoding 应用于 IE 的最新工作，应是最重要的 baseline 之一。\n\n---\n\n## Overall Assessment 详细理由\n\n**给分 3.0（Findings）的依据：**\n\n论文解决了一个清晰且实际的问题（LLM IE 中的 type violation），提供了全面的实验验证，写作质量总体良好。Constraint tightness 分析和 composability 验证都有价值。\n\n但三个因素阻止了 Conference 级别的评分：\n1. **技术新颖性有限**：grammar 层复用 XGrammar，semantic 层是字典查找+条件 masking 的直接实现，主要贡献是工程适配和实证验证，而非算法创新。\n2. **CF trade-off 未解决**：方法在减少 DR 的同时引入了显著的 CF 违规（zero-shot 最高 12%），总违规 burden 的降低远不如单看 DR 那么引人注目。\n3. **最强结果依赖 fine-tuning**：推荐配置（LoRA+S1）需要 task-specific training，削弱了 \"training-free\" 的核心叙事。\n\n适合 Findings track 的理由：solid engineering contribution with thorough evaluation, practical value for IE deployment, honest treatment of limitations, and a useful analytical framework (constraint tightness)。但作为 Conference paper，缺少足够的算法深度或 surprising insight。",
    "reviewer_id": "2",
    "project": "schema_semantic_constrained_ie"
  }
}
```

</details>

---


### Tool result

_source line 837 · 2026-05-19T08:48:07.158991+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_01fc90ae186a4ed432770f7601995139:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 5288
}
```

</details>

---


### Assistant

_source line 838 · 2026-05-19T08:48:17.702862+00:00_

审稿意见已提交给 Review Director。

**总结**: 给出 Overall 3.0（Findings），主要基于三点判断：

1. **技术新颖性有限** — grammar 层完全复用 XGrammar，semantic 层的 entity registry + dynamic masking 在概念上是直接的字典查找+过滤操作，主要贡献偏工程适配
2. **CF trade-off 未解决** — zero-shot 下 CF 最高 12%，总违规 burden（DR+CF）仅降 30%，远低于单看 DR 的 94%
3. **正文比例失衡** — 约 40% 篇幅给 zero-shot（R-F1 仅 2-8%），最强结果（LoRA+S1）反而篇幅不足

优势方面：实验覆盖度极高（3 数据集×4 模型×3 解码策略）、constraint tightness 分析有价值、limitations 诚实透明。适合 Findings track。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2"
}
```

</details>

---


## Round 19

## Round 19

4 recorded events


### User

_source line 839 · 2026-05-19T08:49:16.934515+00:00_

[Round 1 审稿请求]:
## Step 2 — 交叉分享：Reviewer 1 的完整审稿意见

以下是 Reviewer 1 的完整审稿原文，请逐条回应：对每个 Strength/Weakness/Question，标注 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

**Reviewer 1 评分**: 3.5 (Borderline Conference)
**一句话总结**: 方法设计清晰、实验分析诚实透彻，但"near-lossless"叙事被CF trade-off削弱，缺少与schema-aware IE系统的直接对比，部分统计声明证据不足。

**官方维度打分**: Soundness 3.5/5, Excitement 3/5, Reproducibility 4/5, Confidence 4/5

### Strengths
**S1.** 问题定义精确且实用（DR/RV/ET/CF四类violation分类清晰）
**S2.** 两层架构设计合理（enabling dependency通过消融有力验证，semantic-only 24%→加grammar后94%）
**S3.** 分析诚实透彻（CF↔DR pilot ablation, Mistral boundary condition, residual DR root cause分解, Case Study 4失败案例）
**S4.** 实验覆盖面广（3数据集×4模型×3解码策略）
**S5.** 工程贡献扎实（tokenizer-agnostic continuation masking, beam search 125行, runtime 2-13%）

### Must-Fix
**N1** [critical] "near-lossless"叙事未充分呈现CF代价——Abstract声称"near-lossless DR composability"仅限LoRA+S1，zero-shot CF从0.08%升至9.90%(SciERC)/12.02%(Llama DocRED)。Total violation burden(DR+CF) SciERC zero-shot从15.45%降至10.83%，仅降30%。建议：Abstract明确"near-lossless"仅指LoRA+S1；Introduction contribution列表加入CF trade-off；考虑报告total violation(DR+CF)。

**N2** [critical] 缺少与schema-aware IE系统的直接对比——GoLLIE/KnowCoder等在SciERC/DocRED上的violation rates未比较。Baseline仅为ablation变体（unconstrained/grammar-only/semantic-only/post-hoc），无外部竞争方法。建议：至少报告GoLLIE的violation rates或说明为何不可比。

### Should-Fix
**W1** [warning] Dual-factor pattern仅n=4，p≈0.058，正文使用"consistent with""supports"措辞过强
**W2** [warning] WikiEvents 20-doc test set证据不足支撑"extends to EE without modification"
**W3** [warning] Beam search DocRED仅50-doc subset，推广性受限
**W4** [warning] Fine-tuning composability仅验证LoRA，full FT用了untuned learning rate不是fair comparison
**W5** [warning] Checklist WikiEvents文档数不一致（194+20+20=234≠246）

### Minor
- §2 P(E×E)幂集符号未说明
- entity list在relation list之前生成的隐含假设需显式说明
- Table 2 DocRED Grammar-only DR上升至26.17%的counter-intuitive结果需在caption加注
- DocRED CF"---"值需统一处理
- Qwen vs Llama SciERC semantic coverage差异巨大（100% vs 63.4%）值得正文提及
- Compile time不一致（0.044s vs 0.33s）

### Questions
**Q1.** LoRA+S1下total violation burden(DR+CF)净变化数据？
**Q2.** 为何不比较GoLLIE的violation rates？
**Q3.** Entity registry如何处理relation中首次出现的未知实体？
**Q4.** Beam search DocRED全量998 docs结果？
**Q5.** κ(r)归一化：SciERC和DocRED均有6个entity types，κ差异完全来自|σ(r)|？

### Missing References
- Wadhwa et al. (2023) violation rate数据作为baseline参考
- GenIE (Josifoski et al., 2022)
- Paolini et al. (2021) TANL
- TANL/DeepStruct violation rates

---

请对以上每个要点逐条回应 [AGREE] 或 [REBUT]，特别关注：
1. R1 给 3.5（Borderline Conference），你给 3.0（Findings），0.5分差距的核心分歧是什么？
2. R1 认为"两层架构设计合理"（S2），你认为"技术新颖性不足"（N1），这两个判断的矛盾如何调和？
3. R1 的 Q1（total violation burden）你认为是否应成为论文核心指标？

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 840 · 2026-05-19T08:51:35.224907+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 交叉回应 — 对 Reviewer 1 完整审稿的逐条回应\n\n---\n\n### Strengths 回应\n\n**[AGREE] R1-S1**: 问题定义精确且实用。DR/RV/ET/CF 四类分类在 §5 setup 段有清晰定义，且每类对应不同 enforcement 机制，分类是功能性的而非形式化的。\n\n**[AGREE] R1-S2**: 两层架构设计合理，enabling dependency 消融验证有力（Table 1 semantic-only 24%→加 grammar 后 94%；Table 5 fine-tuned 下 grammar 为 no-op、semantic 独立贡献 39-72%）。但\"设计合理\"和\"有足够新颖性\"是不同维度——见后文分歧分析。\n\n**[AGREE] R1-S3**: 强烈同意。CF-DR pilot ablation（Table 4）、Mistral boundary condition（§5.3）、residual DR 四类归因（Appendix B, 36 violations）、Case Study 4 失败案例（Appendix J）——这种自我批判在同行投稿中不常见。\n\n**[AGREE] R1-S4**: 3 数据集 × 4 模型 × 3 解码策略，加上 prompt sensitivity、document length、scalability、full FT baseline 等附加验证，覆盖面是论文最强维度。\n\n**[AGREE] R1-S5**: Continuation masking（§3.3）、beam search 状态隔离（Appendix E, 125 行）、runtime 2-13% 都是非 trivial 的工程贡献。但这恰好支持我的判断：论文主要贡献是工程性的。\n\n---\n\n### Must-Fix 回应\n\n**[AGREE] R1-N1**: 强烈同意，与我的 N2 一致。补充证据：Abstract line 7 将 CF 放在同一句末尾作为附加信息，但 zero-shot total violation burden（Table 1: DR+CF = 15.45%→10.83%）仅降 30%，与 DR 单独的 94% 形成巨大反差。R1 建议报告 total violation (DR+CF) 作为核心指标——我认为完全合理（详见三个专项分歧分析 Q3）。\n\n**[AGREE] R1-N2**: 同意，与我的 W2 呼应。GoLLIE 代码和模型公开可用，论文 §6 line 18 声称\"complementary\"但未实验验证。GoLLIE 本身的 violation rate 和 GoLLIE+OntoCoDec 的边际贡献是最自然的对比实验。\n\n---\n\n### Should-Fix 回应\n\n**[AGREE] R1-W1**: 与我的 W3 一致。n=4, p≈0.058 下 Appendix B line 93 \"strong fit\" 措辞过强。\n\n**[AGREE] R1-W2**: 与我的 W4 一致。20 文档不足以支撑 Abstract line 10 \"extends to EE without modification\" 的 confidence。\n\n**[AGREE] R1-W3**: Table 8 (Appendix E) 标注 \"50-document subsets\"，Clopper-Pearson 95% CI 上界 5.8%，但正文未提及不确定性。\n\n**[REBUT] R1-W4**: 部分不同意。Appendix L 实验目的是验证 \"constraint effectiveness generalizes beyond LoRA\"（DR 2.74%→0%），非证明 full FT 优于 LoRA。Learning rate untuned 影响的是 extraction quality，不是 constraint effectiveness——DR 消除和 F1 不变均已达成。但理想情况下确应 tune 好 LR 再对比。\n\n**[AGREE] R1-W5**: 194+20+20=234≠246，数值不一致需核实。246 可能是零shot全集，234 是 fine-tuning split，但 Checklist 未区分说明。\n\n---\n\n### Minor 回应\n\n**[AGREE]** P(E×E) 幂集符号未定义。\n**[AGREE]** Entity list→relation list 宏观生成顺序假设需显式说明（与我的 W6 一致）。\n**[AGREE]** Table 2 DocRED grammar-only DR 26.17% 需在 caption 加注（§5.2 有解释但 caption 缺失）。\n**[AGREE]** DocRED CF \"---\" 值处理不一致。\n**[REBUT→部分 AGREE]** Qwen vs Llama semantic coverage 100% vs 63.4%：Appendix B line 26-37 有详细分析（tokenization artifact），但同意正文应至少用一句话提及原因。\n**[AGREE]** Compile time 0.044s vs 0.33s 不一致。\n\n---\n\n### Questions 回应\n\n**[AGREE] R1-Q1**: 从 Table 2 计算 LoRA+S1 total burden: SciERC Qwen 1.95%→1.18% (-0.77pp), SciERC Llama 1.11%→0.55% (-0.56pp), DocRED Qwen 0.88%→0.42% (-0.46pp), DocRED Llama 0.49%→0.46% (-0.03pp)。Llama DocRED 边际极小。应在正文明确报告。\n\n**[AGREE] R1-Q2**: 与 N2 一致。\n\n**[AGREE] R1-Q3**: §3.3 line 71 的 fallback 行为（退化为 dom(r) 全集约束）未被充分强调。意味着未知实体的 pair-based 约束退化为粗粒度 domain-only 约束。\n\n**[AGREE] R1-Q4**: 与 W3 一致，应解释未跑全量原因。\n\n**[REBUT] R1-Q5**: SciERC 和 DocRED 均有 6 个 entity types，|E|²=36 相同，κ 差异确实完全来自 |σ(r)|。但 Eq. 2 已清晰定义，这是确认性问题，不构成 weakness。\n\n---\n\n### Missing References 回应\n\n**[AGREE]** Wadhwa et al. (2023): 已在 §6 引用但未引其 violation rate 数据，应作为 external baseline。\n**[REBUT]** GenIE: 已在 Appendix A line 42 引用，R1 可能遗漏。\n**[AGREE]** TANL: 在 .bib 中但未引用（orphan），应在 §6 引用。\n**[AGREE]** 报告 TANL/DeepStruct violation rates 作为 baseline。\n\n---\n\n### 三个专项分歧分析\n\n**1. R1 给 3.5 vs 我给 3.0 的核心分歧**\n\n0.5 分差距主要来自 Excitement 维度（R1: 3/5, 我: 2.5/5）。R1 认为两层架构的 enabling dependency 是有价值的设计 insight，工程贡献值得认可。我的判断更严格：grammar 层完全复用 XGrammar，semantic 层核心机制（字典 + 条件 masking）概念直接，主要复杂性在工程而非算法。分歧本质上是对\"工程贡献 + 全面实验验证\"在 ARR 中应获得多少 credit 的阈值不同。\n\n如果补充 GoLLIE baseline 后 OntoCoDec 展示显著 incremental value，我愿意将分数上调至 3.5。\n\n**2. \"设计合理\" (R1-S2) vs \"新颖性不足\" (我的 N1)**\n\n两个判断不矛盾。\"设计合理\"是工程评价（层间依赖通过消融验证，fallback 有理论动机）；\"新颖性不足\"是学术评价（核心操作是字典查找 + logit masking，不需要新算法或理论工具）。一个系统可以设计合理但缺乏新颖性——Findings track 正是为此类工作设计的：technically sound, practically valuable, but incrementally novel。\n\n**3. Total violation burden (DR+CF) 是否应成为核心指标**\n\n应该。三个理由：\n(a) DR 和 CF 对下游的危害可比。论文 §4 line 17 自己承认 DR \"renders the triple ontologically invalid\"；CF 使同一实体在 KG 中有矛盾类型，对 entity linking/reasoning 同样有害。单独报告 DR 94% 降低而不报告 CF 上升是选择性呈现。\n(b) 论文自己在 Table 1 定义 \"Tot. = DR + CF\" 并纳入 bold 标记——说明作者已有此概念，但正文叙事未以此为主线。\n(c) Fine-tuned 下 total burden 也在改善，将其纳入核心指标对论文有利——使 LoRA+S1 叙事更可信，同时使 zero-shot 叙事更诚实。",
  "reviewer_id": "2",
  "project": "schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 交叉回应 — 对 Reviewer 1 完整审稿的逐条回应\n\n---\n\n### Strengths 回应\n\n**[AGREE] R1-S1**: 问题定义精确且实用。DR/RV/ET/CF 四类分类在 §5 setup 段有清晰定义，且每类对应不同 enforcement 机制，分类是功能性的而非形式化的。\n\n**[AGREE] R1-S2**: 两层架构设计合理，enabling dependency 消融验证有力（Table 1 semantic-only 24%→加 grammar 后 94%；Table 5 fine-tuned 下 grammar 为 no-op、semantic 独立贡献 39-72%）。但\"设计合理\"和\"有足够新颖性\"是不同维度——见后文分歧分析。\n\n**[AGREE] R1-S3**: 强烈同意。CF-DR pilot ablation（Table 4）、Mistral boundary condition（§5.3）、residual DR 四类归因（Appendix B, 36 violations）、Case Study 4 失败案例（Appendix J）——这种自我批判在同行投稿中不常见。\n\n**[AGREE] R1-S4**: 3 数据集 × 4 模型 × 3 解码策略，加上 prompt sensitivity、document length、scalability、full FT baseline 等附加验证，覆盖面是论文最强维度。\n\n**[AGREE] R1-S5**: Continuation masking（§3.3）、beam search 状态隔离（Appendix E, 125 行）、runtime 2-13% 都是非 trivial 的工程贡献。但这恰好支持我的判断：论文主要贡献是工程性的。\n\n---\n\n### Must-Fix 回应\n\n**[AGREE] R1-N1**: 强烈同意，与我的 N2 一致。补充证据：Abstract line 7 将 CF 放在同一句末尾作为附加信息，但 zero-shot total violation burden（Table 1: DR+CF = 15.45%→10.83%）仅降 30%，与 DR 单独的 94% 形成巨大反差。R1 建议报告 total violation (DR+CF) 作为核心指标——我认为完全合理（详见三个专项分歧分析 Q3）。\n\n**[AGREE] R1-N2**: 同意，与我的 W2 呼应。GoLLIE 代码和模型公开可用，论文 §6 line 18 声称\"complementary\"但未实验验证。GoLLIE 本身的 violation rate 和 GoLLIE+OntoCoDec 的边际贡献是最自然的对比实验。\n\n---\n\n### Should-Fix 回应\n\n**[AGREE] R1-W1**: 与我的 W3 一致。n=4, p≈0.058 下 Appendix B line 93 \"strong fit\" 措辞过强。\n\n**[AGREE] R1-W2**: 与我的 W4 一致。20 文档不足以支撑 Abstract line 10 \"extends to EE without modification\" 的 confidence。\n\n**[AGREE] R1-W3**: Table 8 (Appendix E) 标注 \"50-document subsets\"，Clopper-Pearson 95% CI 上界 5.8%，但正文未提及不确定性。\n\n**[REBUT] R1-W4**: 部分不同意。Appendix L 实验目的是验证 \"constraint effectiveness generalizes beyond LoRA\"（DR 2.74%→0%），非证明 full FT 优于 LoRA。Learning rate untuned 影响的是 extraction quality，不是 constraint effectiveness——DR 消除和 F1 不变均已达成。但理想情况下确应 tune 好 LR 再对比。\n\n**[AGREE] R1-W5**: 194+20+20=234≠246，数值不一致需核实。246 可能是零shot全集，234 是 fine-tuning split，但 Checklist 未区分说明。\n\n---\n\n### Minor 回应\n\n**[AGREE]** P(E×E) 幂集符号未定义。\n**[AGREE]** Entity list→relation list 宏观生成顺序假设需显式说明（与我的 W6 一致）。\n**[AGREE]** Table 2 DocRED grammar-only DR 26.17% 需在 caption 加注（§5.2 有解释但 caption 缺失）。\n**[AGREE]** DocRED CF \"---\" 值处理不一致。\n**[REBUT→部分 AGREE]** Qwen vs Llama semantic coverage 100% vs 63.4%：Appendix B line 26-37 有详细分析（tokenization artifact），但同意正文应至少用一句话提及原因。\n**[AGREE]** Compile time 0.044s vs 0.33s 不一致。\n\n---\n\n### Questions 回应\n\n**[AGREE] R1-Q1**: 从 Table 2 计算 LoRA+S1 total burden: SciERC Qwen 1.95%→1.18% (-0.77pp), SciERC Llama 1.11%→0.55% (-0.56pp), DocRED Qwen 0.88%→0.42% (-0.46pp), DocRED Llama 0.49%→0.46% (-0.03pp)。Llama DocRED 边际极小。应在正文明确报告。\n\n**[AGREE] R1-Q2**: 与 N2 一致。\n\n**[AGREE] R1-Q3**: §3.3 line 71 的 fallback 行为（退化为 dom(r) 全集约束）未被充分强调。意味着未知实体的 pair-based 约束退化为粗粒度 domain-only 约束。\n\n**[AGREE] R1-Q4**: 与 W3 一致，应解释未跑全量原因。\n\n**[REBUT] R1-Q5**: SciERC 和 DocRED 均有 6 个 entity types，|E|²=36 相同，κ 差异确实完全来自 |σ(r)|。但 Eq. 2 已清晰定义，这是确认性问题，不构成 weakness。\n\n---\n\n### Missing References 回应\n\n**[AGREE]** Wadhwa et al. (2023): 已在 §6 引用但未引其 violation rate 数据，应作为 external baseline。\n**[REBUT]** GenIE: 已在 Appendix A line 42 引用，R1 可能遗漏。\n**[AGREE]** TANL: 在 .bib 中但未引用（orphan），应在 §6 引用。\n**[AGREE]** 报告 TANL/DeepStruct violation rates 作为 baseline。\n\n---\n\n### 三个专项分歧分析\n\n**1. R1 给 3.5 vs 我给 3.0 的核心分歧**\n\n0.5 分差距主要来自 Excitement 维度（R1: 3/5, 我: 2.5/5）。R1 认为两层架构的 enabling dependency 是有价值的设计 insight，工程贡献值得认可。我的判断更严格：grammar 层完全复用 XGrammar，semantic 层核心机制（字典 + 条件 masking）概念直接，主要复杂性在工程而非算法。分歧本质上是对\"工程贡献 + 全面实验验证\"在 ARR 中应获得多少 credit 的阈值不同。\n\n如果补充 GoLLIE baseline 后 OntoCoDec 展示显著 incremental value，我愿意将分数上调至 3.5。\n\n**2. \"设计合理\" (R1-S2) vs \"新颖性不足\" (我的 N1)**\n\n两个判断不矛盾。\"设计合理\"是工程评价（层间依赖通过消融验证，fallback 有理论动机）；\"新颖性不足\"是学术评价（核心操作是字典查找 + logit masking，不需要新算法或理论工具）。一个系统可以设计合理但缺乏新颖性——Findings track 正是为此类工作设计的：technically sound, practically valuable, but incrementally novel。\n\n**3. Total violation burden (DR+CF) 是否应成为核心指标**\n\n应该。三个理由：\n(a) DR 和 CF 对下游的危害可比。论文 §4 line 17 自己承认 DR \"renders the triple ontologically invalid\"；CF 使同一实体在 KG 中有矛盾类型，对 entity linking/reasoning 同样有害。单独报告 DR 94% 降低而不报告 CF 上升是选择性呈现。\n(b) 论文自己在 Table 1 定义 \"Tot. = DR + CF\" 并纳入 bold 标记——说明作者已有此概念，但正文叙事未以此为主线。\n(c) Fine-tuned 下 total burden 也在改善，将其纳入核心指标对论文有利——使 LoRA+S1 叙事更可信，同时使 zero-shot 叙事更诚实。",
    "reviewer_id": "2",
    "project": "schema_semantic_constrained_ie"
  }
}
```

</details>

---


### Tool result

_source line 841 · 2026-05-19T08:51:39.295855+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_01fc90ae186a4ed432770f7601995139:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4070
}
```

</details>

---


### Assistant

_source line 842 · 2026-05-19T08:51:47.446383+00:00_

交叉回应已提交。核心结论：

- 与 R1 在 13/17 个要点上 **[AGREE]**，尤其在 CF trade-off（N1）和缺少 GoLLIE 对比（N2）两个 critical issues 上完全一致
- 仅在 3 个点上 **[REBUT]**：full FT 实验目的（W4, 部分反驳）、GenIE 引用已存在（Missing Refs）、κ 归一化问题是确认性的（Q5）
- 0.5 分差距（3.0 vs 3.5）的核心分歧在 Excitement 维度：我对"字典查找 + 条件 masking"的算法新颖性阈值更严格，但如果补充 GoLLIE baseline 证明 incremental value，愿意上调至 3.5

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2"
}
```

</details>

---


## Round 20

## Round 20

108 recorded events


### User

_source line 843 · 2026-05-20T17:09:21.606565+00:00_

[Round 1 审稿请求]:
你是 Reviewer 2，负责**新颖性 + 完整性 + 写作质量**。

## 论文信息
- **标题**: OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints
- **论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex`
- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.pdf`

## Venue 要求
- **目标**: EMNLP 2026 via ARR May 2026
- **截止**: 2026-05-25
- **格式**: ACL 模板 [review] 模式，Long paper 正文 8 页，参考文献不限
- **匿名**: Double-blind（不得透露作者身份）
- **必需**: Limitations section（不计页数）+ ARR Responsible NLP Research Checklist
- **附录**: 允许，但审稿人无义务阅读

## 你的审查侧重

### 1. 新颖性评估
- OntoCoDec 相对于 XGrammar/Outlines/GCD 的技术增量——是否仅是工程集成？
- Semantic layer（entity registry + dynamic masking）的学术新颖性——类似机制是否已存在于其他领域？
- Constraint tightness κ̄ 作为分析框架的理论贡献——是否超越简单的描述性统计？
- 与 GoLLIE/KnowCoder 等 schema-aware 方法的本质区别——论文是否充分论证？
- 对比近期工作 CRANE、BoostCD、DCCD 等——论文是否遗漏了关键竞争者？

### 2. 完整性
- Contribution 列表是否与实验证据匹配？是否有 overclaim？
- Related Work 覆盖是否完整？是否遗漏 2025-2026 关键文献？
- Limitations section 是否诚实全面——是否回避了关键弱点？
- 论文自述的 "ontology-agnostic" 声称——WikiEvents 验证是否足以支撑？
- CF trade-off 的讨论是否充分——这是方法的核心局限

### 3. 写作质量与格式
- Abstract 信息密度是否合适？是否过于数字堆砌？
- Introduction 叙事结构——problem → gap → solution → evidence 链是否连贯？
- 表格和图的设计质量——信息呈现是否清晰高效？
- 术语一致性（S1/S2、DR/CF/RV/ET、constraint tightness 等）
- 8 页正文限制内信息密度是否合理——是否有关键内容被挤到附录？
- 双盲合规性——是否有泄露身份的线索？
- Checklist 完整性和准确性

请以 ARR reviewer 标准完成审稿，输出包含：Summary、Strengths（逐条）、Weaknesses（逐条，按 Must-Fix / Should-Fix / Minor 分级）、Questions、Missing References、Overall Assessment（评分 + 置信度）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 844 · 2026-05-20T17:09:29.947719+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/review_reviewer_2_cbe93d98/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/review_reviewer_2_cbe93d98/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 845 · 2026-05-20T17:09:30.702933+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/review_reviewer_2_cbe93d98.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 755
}
```

</details>

---


### Tool call

_source line 846 · 2026-05-20T17:09:30.703334+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
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

_source line 847 · 2026-05-20T17:09:30.753958+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 848 · 2026-05-20T17:09:35.845909+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"
  }
}
```

</details>

---


### Tool call

_source line 849 · 2026-05-20T17:09:37.202540+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.pdf",
  "project": "schema_semantic_constrained_ie",
  "pages": "1-10",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.pdf",
    "project": "schema_semantic_constrained_ie",
    "pages": "1-10",
    "dpi": "150"
  }
}
```

</details>

---


### Tool call

_source line 850 · 2026-05-20T17:09:37.604497+00:00_

called mcp__agent-ml-research__verify_references

<details open><summary>🔧 Tool call — mcp__agent-ml-research__verify_references</summary>

```json
{
  "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
  "project": "schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__verify_references",
  "tool_args": {
    "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
    "project": "schema_semantic_constrained_ie"
  }
}
```

</details>

---


### Tool result

_source line 851 · 2026-05-20T17:09:42.325930+00:00_

Web search results for query: "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"}]

Based on the search results, here's information about the ACL Rolling Review (ARR) reviewer guidelines for 2025-2026:

## Scoring Criteria

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

### Soundness Score
Soundness scores must be justified by the text of the review. If you give a low Soundness score without finding any major faults, this means that your review is not a faithful explanation of your recommendation, and you need to revise it.

### Excitement Score
Sometimes you may find the work sound, but not something that is interesting for you personally. Such preferences are more subjective and should be reflected in a separate excitement score, which is orthogonal to the assessment of the soundness of the paper.

### Area Chair Metareview Scoring
The ARR metareview score has changed in February 2025 to be more aligned with reviewer scores. Like with reviews, the score should be backed up by the meta-review text. The new options include: 5 = Co
…[truncated 336 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6480
}
```

</details>

---


### Tool result

_source line 852 · 2026-05-20T17:09:43.683833+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 467.1}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 520.6}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 510.3}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 512.3}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 531.0}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 527.2}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 481.1}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 506.5}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p9.png\", \"w
…[truncated 520 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 6481
}
```

</details>

---


### Tool result

_source line 853 · 2026-05-20T17:10:37.417867+00:00_

&lt;persisted-output>
Output too large (54.9KB). Full output saved to: /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie--claude-sessions-review-reviewer-2-cbe93d98/51aa1c45-4c20-49a9-8209-d0a0240af647/tool-results/toolu_01QtAY5A76MAWe27k2g7yrUP.txt

Preview (first 2KB):
{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 67, \"total_citations\": 93, \"unique_cited_keys\": 56, \"orphan_bib\": 10, \"missing_bib\": 0, \"duplicate_keys\": 1, \"online_verified\": 52, \"online_not_found\": 3, \"online_mismatch\": 11}, \"cross_check\": {\"orphan_bib\": [\"delafuente2025guidex\", \"geng2025jsonschemabench\", \"lee2026formattax\", \"lu2025schemarl\", \"park2024grammaraligned\", \"reddy2026dccd\", \"sakota2025boostcd\", \"schema_rl2025\", \"shen2025slot\", \"slot2025\"], \"missing_bib\": [], \"orphan_count\": 10, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"synchromesh_iclr2022\", \"type\": \"inproceedings\", \"title\": \"Synchromesh: Reliable Code Generation from Pre-trained Language Models\", \"authors\": \"Poesia, Gabriel and Polozov, Oleksandr and Le, Vu and Tiwari, Ashish and Soares,...\", \"year\": \"2022\", \"venue\": \"International Conference on Learning Representations\"}, {\"key\": \"mgd_neurips2023\", \"type\": \"inproceedings\", \"title\": \"Monitor-Guided Decoding of Code LMs with Static Analysis of Repository Context\", \"authors\": \"Agrawal, Lakshya A. and Kanade, Aditya and Goyal, Navin and Lahiri, Shuvendu K. ...\", \"year\": \"2023\", \"venue\": \"Advances in Neural Information Processing Systems\"}, {\"key\": \"pldi2025_type_constrained_codegen\", \"type\": \"article\", \"title\": \"Type-Constrained Code Generation with Language Models\", \"authors\": \"M\\\\\\\"undler, Niels and He, Jingxuan and Wang, Hao and Sen, Koushik and Song, Dawn ...\", \"year\": \"2025\", \"venue\": \"Proceedings of the ACM on Programming Languages\"}, {\"key\": \"roth_y
…[truncated 371 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__verify_references",
  "elapsed_ms": 59813
}
```

</details>

---


### Tool call

_source line 854 · 2026-05-20T17:10:43.345868+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the complete review form criteria, scoring dimensions, score scales (1-5 for each dimension), and any specific instructions for reviewers. Include the exact wording for each score level if available."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the complete review form criteria, scoring dimensions, score scales (1-5 for each dimension), and any specific instructions for reviewers. Include the exact wording for each score level if available."
  }
}
```

</details>

---


### Tool call

_source line 855 · 2026-05-20T17:10:43.798912+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p1.png"
  }
}
```

</details>

---


### Tool result

_source line 856 · 2026-05-20T17:10:44.608541+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 809
}
```

</details>

---


### Tool call

_source line 857 · 2026-05-20T17:10:44.759892+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p2.png"
  }
}
```

</details>

---


### Tool call

_source line 858 · 2026-05-20T17:10:45.313794+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p3.png"
  }
}
```

</details>

---


### Tool call

_source line 859 · 2026-05-20T17:10:45.722118+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 860 · 2026-05-20T17:10:46.779577+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2019
}
```

</details>

---


### Tool call

_source line 861 · 2026-05-20T17:10:46.782170+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p5.png"
  }
}
```

</details>

---


### Tool call

_source line 862 · 2026-05-20T17:10:47.237736+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p6.png"
  }
}
```

</details>

---


### Tool call

_source line 863 · 2026-05-20T17:10:47.539198+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 864 · 2026-05-20T17:10:48.044444+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2730
}
```

</details>

---


### Tool call

_source line 865 · 2026-05-20T17:10:48.044919+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 866 · 2026-05-20T17:10:49.004895+00:00_

# ARR Review Form Criteria and Scoring

Based on the provided guidelines, the ARR review form (as of February 2025) includes **three main scoring dimensions**:

## Scoring Dimensions

1. **Soundness**
   - Assesses technical validity and methodological rigor
   - Scores must be justified by review text
   - Low scores require explicit explanation of identified faults

2. **Excitement**
   - Captures subjective personal interest and engagement
   - Orthogonal to soundness assessment
   - Reflects reviewer preferences without requiring detailed justification

3. **Overall Assessment**
   - Composite recommendation integrating soundness, excitement, novelty, and potential impact
   - Explicit recommendation for paper outcome if committed to an ACL venue
   - Papers accepted to main venues must demonstrate sufficient soundness and reproducibility

## Score Scale

The guidelines reference a **1-5 scale** but do not provide explicit wording for each level in the extracted content. The document states reviewers should "provide three scores" but specific numerical anchors are not detailed in this section.

## Key Instructions

- Soundness and reproducibility scores require textual justification
- Excitement reflects personal taste and may stand independently from soundness judgments
- Overall assessment considers impact potential for target communities, not merely novelty or reviewer enthusiasm

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 5659
}
```

</details>

---


### Tool result

_source line 867 · 2026-05-20T17:10:49.006167+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 3284
}
```

</details>

---


### Tool call

_source line 868 · 2026-05-20T17:10:49.009174+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p9.png"
  }
}
```

</details>

---


### Tool call

_source line 869 · 2026-05-20T17:10:49.816098+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 870 · 2026-05-20T17:10:50.778022+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 3995
}
```

</details>

---


### Tool call

_source line 871 · 2026-05-20T17:10:50.784254+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie--claude-sessions-review-reviewer-2-cbe93d98/51aa1c45-4c20-49a9-8209-d0a0240af647/tool-results/toolu_01QtAY5A76MAWe27k2g7yrUP.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie--claude-sessions-review-reviewer-2-cbe93d98/51aa1c45-4c20-49a9-8209-d0a0240af647/tool-results/toolu_01QtAY5A76MAWe27k2g7yrUP.txt"
  }
}
```

</details>

---


### Tool result

_source line 872 · 2026-05-20T17:10:51.187347+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 3648
}
```

</details>

---


### Tool result

_source line 873 · 2026-05-20T17:10:51.339186+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 4101
}
```

</details>

---


### Tool result

_source line 874 · 2026-05-20T17:10:51.744940+00:00_

1	{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 67, \"total_citations\": 93, \"unique_cited_keys\": 56, \"orphan_bib\": 10, \"missing_bib\": 0, \"duplicate_keys\": 1, \"online_verified\": 52, \"online_not_found\": 3, \"online_mismatch\": 11}, \"cross_check\": {\"orphan_bib\": [\"delafuente2025guidex\", \"geng2025jsonschemabench\", \"lee2026formattax\", \"lu2025schemarl\", \"park2024grammaraligned\", \"reddy2026dccd\", \"sakota2025boostcd\", \"schema_rl2025\", \"shen2025slot\", \"slot2025\"], \"missing_bib\": [], \"orphan_count\": 10, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"synchromesh_iclr2022\", \"type\": \"inproceedings\", \"title\": \"Synchromesh: Reliable Code Generation from Pre-trained Language Models\", \"authors\": \"Poesia, Gabriel and Polozov, Oleksandr and Le, Vu and Tiwari, Ashish and Soares,...\", \"year\": \"2022\", \"venue\": \"International Conference on Learning Representations\"}, {\"key\": \"mgd_neurips2023\", \"type\": \"inproceedings\", \"title\": \"Monitor-Guided Decoding of Code LMs with Static Analysis of Repository Context\", \"authors\": \"Agrawal, Lakshya A. and Kanade, Aditya and Goyal, Navin and Lahiri, Shuvendu K. ...\", \"year\": \"2023\", \"venue\": \"Advances in Neural Information Processing Systems\"}, {\"key\": \"pldi2025_type_constrained_codegen\", \"type\": \"article\", \"title\": \"Type-Constrained Code Generation with Language Models\", \"authors\": \"M\\\\\\\"undler, Niels and He, Jingxuan and Wang, Hao and Sen, Koushik and Song, Dawn ...\", \"year\": \"2025\", \"venue\": \"Proceedings of the ACM on Programming Languages\"}, {\"key\": \"roth_yih_2004\", \"type\": \"inproceedings\", \"title\": \"A Linear Programming Formulation for Global Inference in Natural Language Tasks\", \"authors\": \"Roth, Dan and Yih, Wen-tau\", \"year\": \"2004\", \"venue\": \"Proceedings of the Eighth Conference on Computational Natural Language Learning ...\"}, {\"key\": \"adakgc_emnlp2023\", \"type\": \
…[truncated 54221 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 960
}
```

</details>

---


### Tool result

_source line 875 · 2026-05-20T17:10:51.746184+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 3701
}
```

</details>

---


### Tool result

_source line 876 · 2026-05-20T17:10:52.100923+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 3091
}
```

</details>

---


### Tool result

_source line 877 · 2026-05-20T17:10:52.252501+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2436
}
```

</details>

---


### Tool call

_source line 878 · 2026-05-20T17:11:05.113119+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.pdf",
  "project": "schema_semantic_constrained_ie",
  "pages": "11-20",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.pdf",
    "project": "schema_semantic_constrained_ie",
    "pages": "11-20",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 879 · 2026-05-20T17:11:07.903058+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 603.6}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 620.7}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 585.5}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 369.3}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 564.4}, {\"page\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p16.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 540.9}, {\"page\": 17, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p17.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 555.3}, {\"page\": 18, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p18.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 569.3}, {\"page\": 19, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/m
…[truncated 538 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 2789
}
```

</details>

---


### Tool call

_source line 880 · 2026-05-20T17:11:07.953639+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the COMPLETE review form with ALL scoring dimensions, their exact score scales, and detailed descriptions for each score level. Include: soundness scale (1-5 with descriptions), excitement scale (1-5 with descriptions), overall assessment scale (1-5 with descriptions), confidence scale, any other dimensions. I need the exact wording for each numeric score."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the COMPLETE review form with ALL scoring dimensions, their exact score scales, and detailed descriptions for each score level. Include: soundness scale (1-5 with descriptions), excitement scale (1-5 with descriptions), overall assessment scale (1-5 with descriptions), confidence scale, any other dimensions. I need the exact wording for each numeric score."
  }
}
```

</details>

---


### Tool result

_source line 881 · 2026-05-20T17:11:12.683052+00:00_

# ARR Review Form Scoring Dimensions

Based on the provided guidelines, the document references a review form but **does not provide the complete scoring scales with exact numeric descriptions**.

## What the Guidelines Confirm Exists:

The document states: "Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation."

It also mentions a **confidence score** and **reproducibility score**, but specific numeric scales and their exact wording are not included in this content.

## Available Guidance:

The guidelines explain that:
- **Soundness scores** must be justified by review text
- **Excitement scores** reflect personal taste and don't require explicit justification
- **Overall assessment** is a composite reflecting soundness, excitement, novelty, and impact

## Where to Find Complete Details:

The document directs reviewers to: "We also have a post describing the ARR review form in detail" at https://aclrollingreview.org/reviewform, which would contain the actual scoring rubrics and numeric scales you need.

The current guidelines page does not reproduce the full review form structure with complete 1-5 scale definitions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 4729
}
```

</details>

---


### Tool call

_source line 882 · 2026-05-20T17:11:17.710042+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the COMPLETE review form with ALL scoring dimensions and their exact score scales. I need: soundness (1-5 with exact descriptions for each level), excitement (1-5 with exact descriptions), overall assessment (1-5 with exact descriptions), confidence scale, reproducibility. Give me the exact wording for every score level."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the COMPLETE review form with ALL scoring dimensions and their exact score scales. I need: soundness (1-5 with exact descriptions for each level), excitement (1-5 with exact descriptions), overall assessment (1-5 with exact descriptions), confidence scale, reproducibility. Give me the exact wording for every score level."
  }
}
```

</details>

---


### Tool call

_source line 883 · 2026-05-20T17:11:18.167299+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p11.png"
  }
}
```

</details>

---


### Tool call

_source line 884 · 2026-05-20T17:11:18.871851+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 885 · 2026-05-20T17:11:19.727485+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1560
}
```

</details>

---


### Tool call

_source line 886 · 2026-05-20T17:11:19.728008+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p13.png"
  }
}
```

</details>

---


### Tool call

_source line 887 · 2026-05-20T17:11:20.080900+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p14.png"
  }
}
```

</details>

---


### Tool result

_source line 888 · 2026-05-20T17:11:20.790071+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1918
}
```

</details>

---


### Tool call

_source line 889 · 2026-05-20T17:11:20.790529+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p15.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p15.png"
  }
}
```

</details>

---


### Tool result

_source line 890 · 2026-05-20T17:11:21.296753+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/review_reviewer_2_cbe93d98.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 506
}
```

</details>

---


### Tool call

_source line 891 · 2026-05-20T17:11:21.297183+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p16.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p16.png"
  }
}
```

</details>

---


### Tool result

_source line 892 · 2026-05-20T17:11:23.583616+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 3855
}
```

</details>

---


### Tool result

_source line 893 · 2026-05-20T17:11:23.586134+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 3505
}
```

</details>

---


### Tool result

_source line 894 · 2026-05-20T17:11:23.609066+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/review_reviewer_2_cbe93d98.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2311
}
```

</details>

---


### Tool call

_source line 895 · 2026-05-20T17:11:23.786177+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p17.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p17.png"
  }
}
```

</details>

---


### Tool result

_source line 896 · 2026-05-20T17:11:23.822916+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/review_reviewer_2_cbe93d98.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 36
}
```

</details>

---


### Tool result

_source line 897 · 2026-05-20T17:11:23.940106+00:00_

# ACL Rolling Review Form - Scoring Dimensions

## Soundness (1-5 scale)

- **5**: "Excellent: This study is one of the most thorough I have seen, given its type."
- **4**: "Strong: This study provides sufficient support for all of its claims."
- **3**: "Acceptable: This study provides sufficient support for its main claims."
- **2**: "Poor: Some of the main claims are not sufficiently supported."
- **1**: "Major Issues: This study is not yet sufficiently thorough to warrant publication."

## Excitement (1-5 scale)

- **5**: "Highly Exciting: I would recommend this paper to others and/or attend its presentation."
- **4**: "Exciting: I would mention this paper to others and/or make an effort to attend."
- **3**: "Interesting: I might mention some points of this paper to others."
- **2**: "Potentially Interesting: this paper does not resonate with me, but it might with others."
- **1**: "Not Exciting: this paper does not resonate with me, and I don't think it would with others."

## Overall Assessment (1-5 scale)

- **5**: "Consider for Award: top 2.5% papers"
- **4**: "Conference: I think this paper could be accepted to an *ACL conference."
- **3**: "Findings: I think this paper could be accepted to the Findings of the ACL."
- **2**: "Resubmit next cycle: substantial revisions needed"
- **1**: "Do not resubmit: fully redone or not relevant"

## Reviewer Confidence (1-5 scale)

- **5**: "Positive that my evaluation is correct"
- **4**: "Quite sure" with unlikely but possible gaps
- **3**: "Pretty sure, but there's a chance I missed something"
- **2**: "Willing to defend my evaluation, but fairly likely gaps exist"
- **1**: "Not my area, or paper is very hard to understand"

## Reproducibility (1-5 scale)

- **5**: "They could easily reproduce the results."
- **4**: "They could mostly reproduce the results" with minor variations
- **3**: "They could reproduce the results with some difficulty"
- **2**: "They would be hard pressed to reproduce the results"
- **1**: "They
…[truncated 44 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 6230
}
```

</details>

---


### Tool call

_source line 898 · 2026-05-20T17:11:24.182559+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p18.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p18.png"
  }
}
```

</details>

---


### Tool result

_source line 899 · 2026-05-20T17:11:24.233107+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/review_reviewer_2_cbe93d98.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 900 · 2026-05-20T17:11:24.266044+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p19.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p19.png"
  }
}
```

</details>

---


### Tool result

_source line 901 · 2026-05-20T17:11:24.332824+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/review_reviewer_2_cbe93d98.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 66
}
```

</details>

---


### Tool call

_source line 902 · 2026-05-20T17:11:24.516797+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p20.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p20.png"
  }
}
```

</details>

---


### Tool result

_source line 903 · 2026-05-20T17:11:24.573946+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/review_reviewer_2_cbe93d98.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 57
}
```

</details>

---


### Tool call

_source line 904 · 2026-05-20T17:11:45.921876+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.pdf",
  "project": "schema_semantic_constrained_ie",
  "pages": "15-20",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.pdf",
    "project": "schema_semantic_constrained_ie",
    "pages": "15-20",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 905 · 2026-05-20T17:11:46.676231+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 564.4}, {\"page\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p16.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 540.9}, {\"page\": 17, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p17.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 555.3}, {\"page\": 18, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p18.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 569.3}, {\"page\": 19, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p19.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 524.9}, {\"page\": 20, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p20.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 509.9}], \"total_pages\": 31, \"rendered_pages\": 6, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 754
}
```

</details>

---


### Tool call

_source line 906 · 2026-05-20T17:11:49.741478+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p15.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p15.png"
  }
}
```

</details>

---


### Tool call

_source line 907 · 2026-05-20T17:11:50.200179+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p16.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p16.png"
  }
}
```

</details>

---


### Tool result

_source line 908 · 2026-05-20T17:11:51.106946+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1365
}
```

</details>

---


### Tool result

_source line 909 · 2026-05-20T17:11:51.108517+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 908
}
```

</details>

---


### Tool call

_source line 910 · 2026-05-20T17:11:51.159178+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p17.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p17.png"
  }
}
```

</details>

---


### Tool call

_source line 911 · 2026-05-20T17:11:51.613863+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p18.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p18.png"
  }
}
```

</details>

---


### Tool result

_source line 912 · 2026-05-20T17:11:52.069775+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 910
}
```

</details>

---


### Tool call

_source line 913 · 2026-05-20T17:11:52.070214+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p19.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p19.png"
  }
}
```

</details>

---


### Tool result

_source line 914 · 2026-05-20T17:11:52.528818+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 914
}
```

</details>

---


### Tool call

_source line 915 · 2026-05-20T17:11:52.529295+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p20.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p20.png"
  }
}
```

</details>

---


### Tool result

_source line 916 · 2026-05-20T17:11:53.186800+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1116
}
```

</details>

---


### Tool result

_source line 917 · 2026-05-20T17:11:53.489831+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 960
}
```

</details>

---


### Tool call

_source line 918 · 2026-05-20T17:11:58.458346+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.pdf",
  "project": "schema_semantic_constrained_ie",
  "pages": "21-31",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.pdf",
    "project": "schema_semantic_constrained_ie",
    "pages": "21-31",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 919 · 2026-05-20T17:11:59.765501+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 21, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p21.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 483.5}, {\"page\": 22, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p22.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 539.3}, {\"page\": 23, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p23.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 498.0}, {\"page\": 24, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p24.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 465.9}, {\"page\": 25, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p25.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 452.5}, {\"page\": 26, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p26.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 525.4}, {\"page\": 27, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p27.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 494.5}, {\"page\": 28, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p28.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 496.7}, {\"page\": 29, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/m
…[truncated 762 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1307
}
```

</details>

---


### Tool call

_source line 920 · 2026-05-20T17:12:03.485315+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p21.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p21.png"
  }
}
```

</details>

---


### Tool result

_source line 921 · 2026-05-20T17:12:04.088270+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 602
}
```

</details>

---


### Tool call

_source line 922 · 2026-05-20T17:12:04.139008+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p22.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p22.png"
  }
}
```

</details>

---


### Tool result

_source line 923 · 2026-05-20T17:12:04.842222+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 703
}
```

</details>

---


### Tool call

_source line 924 · 2026-05-20T17:12:04.892824+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p23.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p23.png"
  }
}
```

</details>

---


### Tool call

_source line 925 · 2026-05-20T17:12:05.399850+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p24.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p24.png"
  }
}
```

</details>

---


### Tool result

_source line 926 · 2026-05-20T17:12:05.848867+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 956
}
```

</details>

---


### Tool call

_source line 927 · 2026-05-20T17:12:05.901394+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p25.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p25.png"
  }
}
```

</details>

---


### Tool call

_source line 928 · 2026-05-20T17:12:06.406065+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p26.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p26.png"
  }
}
```

</details>

---


### Tool result

_source line 929 · 2026-05-20T17:12:07.211749+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1811
}
```

</details>

---


### Tool result

_source line 930 · 2026-05-20T17:12:07.212874+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1311
}
```

</details>

---


### Tool result

_source line 931 · 2026-05-20T17:12:07.264272+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 858
}
```

</details>

---


### Tool call

_source line 932 · 2026-05-20T17:12:07.264976+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p27.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p27.png"
  }
}
```

</details>

---


### Tool call

_source line 933 · 2026-05-20T17:12:07.717599+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p28.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p28.png"
  }
}
```

</details>

---


### Tool result

_source line 934 · 2026-05-20T17:12:08.222585+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 957
}
```

</details>

---


### Tool call

_source line 935 · 2026-05-20T17:12:08.223052+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p29.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p29.png"
  }
}
```

</details>

---


### Tool result

_source line 936 · 2026-05-20T17:12:09.079857+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1362
}
```

</details>

---


### Tool result

_source line 937 · 2026-05-20T17:12:09.132265+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 909
}
```

</details>

---


### Tool call

_source line 938 · 2026-05-20T17:12:09.132623+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p30.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p30.png"
  }
}
```

</details>

---


### Tool call

_source line 939 · 2026-05-20T17:12:09.284808+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p31.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p31.png"
  }
}
```

</details>

---


### Tool result

_source line 940 · 2026-05-20T17:12:10.040814+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 908
}
```

</details>

---


### Tool result

_source line 941 · 2026-05-20T17:12:10.044025+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 759
}
```

</details>

---


### Tool call

_source line 942 · 2026-05-20T17:14:41.268420+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "constrained decoding information extraction ontology 2025 2026 structured generation type constraints"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "constrained decoding information extraction ontology 2025 2026 structured generation type constraints"
  }
}
```

</details>

---


### Tool call

_source line 943 · 2026-05-20T17:14:41.369341+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "IterGen semantic-aware structured LLM generation backtracking Ugare 2025 comparison grammar semantic constraints"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "IterGen semantic-aware structured LLM generation backtracking Ugare 2025 comparison grammar semantic constraints"
  }
}
```

</details>

---


### Tool result

_source line 944 · 2026-05-20T17:14:47.147156+00:00_

Web search results for query: "IterGen semantic-aware structured LLM generation backtracking Ugare 2025 comparison grammar semantic constraints"

Links: [{"title":"[PDF] IterGen: Iterative Semantic-aware Structured LLM Generation with Backtracking | Semantic Scholar","url":"https://www.semanticscholar.org/paper/8f918a87d0f1bc090fca1dbdfbc4d06a9dc88a66"},{"title":"ICLR Poster IterGen: Iterative Semantic-aware Structured LLM Generation with Backtracking","url":"https://iclr.cc/virtual/2025/poster/29157"},{"title":"[2410.07295] IterGen: Iterative Semantic-aware Structured LLM Generation with Backtracking","url":"https://arxiv.org/abs/2410.07295"},{"title":"Shubham Ugare","url":"https://shubhamugare.github.io/"},{"title":"IterGen: Iterative Semantic-aware Structured LLM ...","url":"https://iclr.cc/media/iclr-2025/Slides/29157.pdf"},{"title":"ITERGEN: ITERATIVE SEMANTIC-AWARE STRUCTURED ...","url":"https://openreview.net/pdf?id=ac93gRzxxV"},{"title":"CodeARC: Benchmarking Reasoning Capabilities of LLM ...","url":"https://arxiv.org/pdf/2503.23145"},{"title":"[Literature Review] IterGen: Iterative Semantic-aware Structured LLM Generation with Backtracking","url":"https://www.themoonlight.io/en/review/itergen-iterative-semantic-aware-structured-llm-generation-with-backtracking"},{"title":"IterGen: Iterative Semantic-aware Structured LLM Generation with   Backtracking","url":"https://arxiv.org/pdf/2410.07295"},{"title":"IterGen: Iterative Semantic-aware Structured LLM Generation with Backtracking | OpenReview","url":"https://openreview.net/forum?id=ac93gRzxxV"}]

Based on the search results, here's what I found about IterGen and related research:

## IterGen Overview

IterGen is a user-friendly library for iterative, grammar-guided LLM generation that enables users to move both forward and backward within the generated output based on grammar symbols. It leverages a symbol-to-position mapping and maintains the key-value (KV) cache state to ensure efficient and structured gen
…[truncated 1073 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 5777
}
```

</details>

---


### Tool result

_source line 945 · 2026-05-20T17:14:52.218596+00:00_

Web search results for query: "constrained decoding information extraction ontology 2025 2026 structured generation type constraints"

Links: [{"title":"Grammar-constrained decoding for structured information extraction with fine-tuned generative models applied to clinical trial abstracts - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC11747381/"},{"title":"Frontiers | Grammar-constrained decoding for structured information extraction with fine-tuned generative models applied to clinical trial abstracts","url":"https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2024.1406857/full"},{"title":"Grammar-constrained decoding for structured information extraction with fine-tuned generative models applied to clinical trial abstracts","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11747381/"},{"title":"How Structured Outputs and Constrained Decoding Work | Let's Data Science","url":"https://letsdatascience.com/blog/structured-outputs-making-llms-return-reliable-json"},{"title":"Draft-Conditioned Constrained Decoding for Structured Generation in LLMs","url":"https://arxiv.org/pdf/2603.03305"},{"title":"Combining Constrained and Unconstrained Decoding via Boosting: BoostCD and Its Application to Information Extraction","url":"https://arxiv.org/pdf/2506.14901"},{"title":"From text to task: Constrained generation for structured extraction in R1","url":"https://fireworks.ai/blog/constrained-generation-with-reasoning"}]

I've found several highly relevant results on constrained decoding for information extraction. Here's what the search uncovered:

## Key Research Findings

**Grammar-Constrained Decoding for Structured IE:**
In structured information extraction, there are typically semantic and syntactic constraints on IE system outputs, leading to the development of constrained decoding approaches that allow specifying constraints in form of context-free grammars. A recent publication from January 2025 explores this topic in the context
…[truncated 1105 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 10950
}
```

</details>

---


### Tool call

_source line 946 · 2026-05-20T17:15:20.312015+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 947 · 2026-05-20T17:15:20.362707+00:00_

{"result":"{\"success\": true, \"data\": {\"deleted\": 17, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 948 · 2026-05-20T17:17:35.087537+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 2 审稿意见：OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints\n\n**审查侧重：新颖性 + 完整性 + 写作质量**\n\n---\n\n## Summary\n\n本文提出 OntoCoDec，一个将 IE 本体约束编译为双层解码约束的框架：语法层（S1）通过 XGrammar 保证 JSON 结构合法性和词汇成员关系；语义层（S2）通过运行时 entity registry 和 dynamic masking 强制 domain/range 类型兼容性。论文在 Proposition 1 中证明带无界实体集的类型约束不属于 context-free，从而为语义层的必要性提供了形式化论证。引入 constraint tightness κ̄ 作为 schema 限制性的描述性度量。在 SciERC（551篇）、DocRED（998篇）、WikiEvents（246篇）三个数据集上，使用 Qwen3-8B、Llama-3.1-8B、Mistral-7B 等模型进行了系统的消融实验。\n\n---\n\n## 总体评分\n\n**Overall**: 3.5 — Borderline Conference\n\n**一句话总结**: 技术执行和实验设计高质量，但核心新颖性——语义层 dynamic masking——与已有工作（IterGen、PICARD 等）的概念差异阐述不足，κ̄ 作为\"分析框架\"的贡献被过度声称。\n\n---\n\n## 官方维度打分（来自 ACL ARR review form, Feb 2025+）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 4/5 | 主要 claim 均有充分实验支撑；Proposition 1 形式化论证严谨；消融研究系统完整；论文坦诚承认 κ̄ 的统计局限性 |\n| Excitement | 3/5 | 解决真实问题（LLM-IE 中的类型违规），实用价值明确；但核心技术增量（entity registry + dynamic masking）概念上较直接，κ̄ 更接近描述性统计而非深层理论贡献 |\n| Reproducibility | 4/5 | 提供了详细的 prompt 模板（Appendix A）、超参数配置（Appendix F）、硬件信息、随机种子验证（Appendix F）；代码承诺开源但提交时未附 |\n| Confidence | 4/5 | 熟悉 constrained decoding 和 structured IE 领域，仔细阅读了全部 31 页（含附录） |\n\n---\n\n## 主要优势\n\n**S1. 形式化论证严谨且有实际意义。** Proposition 1（§3.1, p3）证明带无界实体集的 IE 类型约束不属于 context-free 语言，这为双层架构提供了不可跳过的理论基础。Corollary 进一步推导出 enabling dependency 的必要性。这不仅是学术优雅——它直接解释了为什么 XGrammar/Outlines 等纯 grammar 方案在 IE 场景下必然不足。\n\n**S2. 违规分类法和消融设计极为系统。** 论文将输出违规分解为 DR（domain/range）、CF（cross-field）、RV（relation vocabulary）、ET（entity typing）四类（§5, Table 1），然后在每个消融配置下逐项报告。这种精细度远超同领域多数论文的二元\"valid/invalid\"评估，允许读者精确理解每层约束的贡献和代价。\n\n**S3. 实验覆盖面广且诚实。** 三个数据集（sentence-level RE、document-level RE、event extraction）× 四个模型 × 多种配置（zero-shot / fine-tuned / beam search / S1 vs S2）。Limitations section（p9）明确承认：CF 是模型相关的、评估仅限一种微调方法（LoRA）、模型规模限于 7-8B。这种诚实度值得肯定。\n\n**S4. Fine-tuning composability 论证有价值。** Table 2（p6）展示 LoRA fine-tuning + OntoCoDec 约束是可组合的：fine-tuning 减少 DR 至 1-2%，加入 S1 后进一步消除或接近消除 DR（< 0.09%），同时 R-F1 保持稳定。这回答了一个重要的部署问题——约束系统是否与参数优化兼容。\n\n**S5. κ̄ 与违规率的关联分析提供实用的部署指导。** 尽管统计上不够confirmatory（论文自己承认 df=2, p>0.05），但 κ̄ × RV_baseline 作为 DR 的预测因子（Appendix C, Figure 1, p20）为实际部署中选择约束策略提供了直觉：κ > 0.5 的 schema 可在 zero-shot 下实现近零 DR，低 κ schema 需要 fine-tuning。\n\n**S6. WikiEvents 扩展验证了跨本体泛化。** §5.4（p7）将框架扩展到事件抽取（KAIROS 本体，56 event types, 80 argument roles），无需修改即可应用。虽然只是 zero-shot 评估，但展示了框架在正式本体（vs. 经验衍生类型集）上的适用性。\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] 语义层核心机制（entity registry + dynamic masking）与 IterGen 的概念区分不充分\n\n- 具体位置：§6 Related Work（p8）, Appendix B（p13-17）\n- 问题：IterGen（Ugare et al., 2025, ICLR 2025）同样在 grammar 层之上叠加语义约束，在生成过程中检测违规并通过 backtracking 修正。OntoCoDec 的 dynamic masking 与 IterGen 的 semantic check + backtracking 是解决同一类问题（grammar-valid 但 semantically-invalid 输出）的两种机制。论文在 §6 和 Appendix B 中仅将 IterGen 列为相关工作之一，未深入对比两者在机制设计（preventive masking vs. corrective backtracking）、效率特性（OntoCoDec 无需回退 vs. IterGen 需要 KV cache 管理）、和约束表达能力（OntoCoDec 限于 domain/range vs. IterGen 支持任意 semantic predicate）上的差异。类似地，PICARD（Scholak et al., 2021）的 incremental parsing monitor 与 OntoCoDec 的 runtime entity registry 在概念上高度相似——均为在解码过程中维护状态以检查上下文相关约束。\n- 为什么影响接收：新颖性是接收决定的关键维度。如果审稿人认为核心机制是已有方法（preventive masking / runtime monitor）在 IE 场景的 application，而非方法论创新，则难以达到 main conference 标准。\n- 建议修改方向：在 §6 中增加一段显式的机制对比表（OntoCoDec vs. IterGen vs. PICARD），明确阐述：(1) OntoCoDec 的 forward-only masking 的效率优势及其 one-step-lookahead 的局限；(2) IterGen 的 backtracking 允许任意 semantic predicate 但引入 KV cache overhead 和 non-monotonic generation；(3) PICARD 的 token-level filtering 与 OntoCoDec entity registry 的粒度差异。\n\n**N2** [critical] κ̄ 作为 Contribution 2（\"analytical linking framework\"）被过度声称\n\n- 具体位置：Abstract（p1, \"an analytical linking constraint tightness to enforcement outcomes\"）, §1 Contributions 列表 item 2（p2）, §4（p4-5）\n- 问题：κ̄ 的定义（§4, Eq. 3: κ = 1 − |S(r)|/|E|）本质上是每个 relation 的类型集合大小相对于总实体类型数的归一化比例——这是一个描述性统计量，而非一个分析框架。论文自身在 Appendix C（p20）承认回归分析\"constitutes a descriptive characterization rather than a confirmatory statistical test\"（df=2, p>0.05）。然而，Abstract 和 Contribution 列表仍将其定位为\"analytical linking framework\"，这与论文自身的谨慎表述不一致。\n- 为什么影响接收：Contribution 列表的每一项都应与论文实际提供的证据水平匹配。将描述性统计提升为\"分析框架\"属于 overclaim，可能导致审稿人对整篇论文的 claim 可信度产生质疑。\n- 建议修改方向：将 Contribution 2 重新表述为\"a descriptive metric, constraint tightness κ̄, that correlates with enforcement outcomes and provides deployment guidance\"，去掉\"analytical framework\"的措辞。在 Abstract 中也相应调整。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] 无直接实验对比最接近的 IE 基线 BoostCD\n\n- 具体位置：§5（p5-7）, §6（p8）\n- 问题：BoostCD（Sakota et al., 2025）是唯一同样将 constrained decoding 应用于 IE 的已发表工作（EMNLP 2025），且使用了 SciERC 和 DocRED 作为评估数据集。论文引用了 BoostCD 但未进行任何实验对比。即使两者的 setting 不完全相同（BoostCD boosting 无约束/有约束解码；OntoCoDec 使用两层约束），也应提供同一数据集上的结果对比，或至少详细讨论为何直接比较不可行。\n- 建议：(1) 如果 BoostCD 代码可用，在 SciERC 上运行对比实验；(2) 若不可行，在 §5 或 §6 中增加一段定性分析，引用 BoostCD 报告的数字并讨论方法论差异导致的预期性能差异。\n\n**W2** [warning] \"Ontology-agnostic\" 声称的实验支撑不充分\n\n- 具体位置：Abstract（p1）, §1 Contribution 3（p2）, §7（p8）\n- 问题：三个评估数据集中，SciERC 和 DocRED 的类型约束来自训练数据的经验统计（\"type pairs extracted from annotated training data\"，§2, p2），并非形式化本体。仅 WikiEvents 使用了正式本体（KAIROS）。且 WikiEvents 评估仅为 zero-shot（246 篇），无 fine-tuning 验证。声称框架 \"ontology-agnostic\" 需要更强的证据——至少应在 2+ 个正式本体上验证，或明确限定 claim 的范围。\n- 建议：将 \"ontology-agnostic\" 限定为 \"applicable to both formal ontologies and empirically-derived type constraints\"，并在 Limitations 中明确指出仅在一个正式本体上验证。\n\n**W3** [warning] 正文 Related Work（§6）过于压缩\n\n- 具体位置：§6（p8，约 15 行正文）\n- 问题：正文 Related Work 仅覆盖三个轴各一小段，实质性讨论全部推迟到 Appendix B（p13-17, 约 2.5 页）。虽然 ARR 规则不禁止这种安排，但审稿人无义务阅读附录。正文中未充分讨论与关键竞争者（BoostCD、IterGen、CRANE、GoLLIE）的差异，使得审稿人难以仅从正文评判新颖性。\n- 建议：在 8 页限制内，将 §6 扩展至至少半页，将 IterGen/BoostCD 的机制对比从附录移入正文。可通过压缩 §5.4（WikiEvents 细节可移入附录）来腾出空间。\n\n**W4** [warning] Abstract 信息密度过高，关键 message 被数字淹没\n\n- 具体位置：Abstract（p1）\n- 问题：Abstract 中包含大量具体数字（\"DR 40-46%\"、\"R-F1 0.099\"、\"76-99%\"、\"88-70B\" 等），阅读体验接近结果表格的自然语言复述，而非对核心贡献的提炼。关键 insight（为什么 grammar 层不够、语义层如何补足、这对 IE 部署意味着什么）被数字细节遮蔽。\n- 建议：保留 1-2 个最关键的数字（如 DR 减少幅度和 R-F1 保持稳定），其余推至 Introduction。Abstract 应更侧重 conceptual framing。\n\n**W5** [warning] 模型规模限于 7-8B，对 claim 泛化性的影响在正文中未充分 hedge\n\n- 具体位置：§5（p5-7）, §7（p8）\n- 问题：所有实验使用 7-8B 参数模型。Limitations（p9）提到 \"scaling to smaller models has not been verified\"，但更值得关注的是向上的 scaling——70B+ 模型通常 baseline 违规率更低，OntoCoDec 的边际增益可能不同。§7 的结论 \"drops by 76-99% for calibrated models\" 未 hedge 模型规模。\n- 建议：在 §7 结论中增加 \"across 7-8B parameter models\" 的限定词。\n\n**W6** [warning] CF 代价在 Abstract/Contribution 中不够透明\n\n- 具体位置：Abstract（p1）, §4（p4）\n- 问题：Grammar-first fallback 在解决 DR 的同时引入 CF 违规（cross-field inconsistency）。Table 1 显示 Full S1 在 SciERC 上 CF 从 0 增至 ~0.33%。虽然 §4 和 Appendix C 详细讨论了这一 trade-off，但 Abstract 仅轻描淡写地提到 \"grammar-first fallback when constraints conflict\"，未量化其代价。审稿人可能认为论文在选择性地突出优势、淡化局限。\n- 建议：在 Abstract 中增加一句简短的 trade-off 说明，如 \"with modest cross-field consistency costs (≤0.33% on SciERC) resolvable via beam search or fine-tuning\"。\n\n---\n\n## 小问题（不影响接收）\n\n- **M1**: .bib 文件中有 10 个 orphan entries（在 bib 中但未在论文中引用），包括 `sakota2025boostcd`（与 `boostcd2025` 重复）、`lee2026formattax`（与 `formattax2026` 重复）等。应清理 bib 文件。\n- **M2**: `schall2025hiddencost` bib key 重复出现两次。\n- **M3**: §3.4 的 S1/S2 命名（Single-pass / Two-pass）与 §5 中的层级编号（S1 语法层、S2 语义层）初读时易混淆，虽然定义清晰但建议重命名为 SP/TP 或类似标记以避免歧义。\n- **M4**: Table 5（p7, WikiEvents）的 \"—\" 标记（\"not applicable\"）缺少表注解释。\n- **M5**: Appendix F（p26-27）提供了详细的复现细节，但 random seed 验证（seeds 123, 456）仅在 greedy decoding 下进行，beam search 的 non-determinism 仅报告了 variance < 0.5pp 而未提供具体 seed 信息。\n\n---\n\n## Questions for Authors\n\n**Q1**: IterGen 的 backtracking 机制理论上可以处理任意 semantic predicate，而 OntoCoDec 的 dynamic masking 限于 domain/range 类型兼容。是否考虑过将 OntoCoDec 扩展到更一般的语义约束（如 cardinality constraints、temporal ordering）？如果有，主要技术障碍是什么？\n\n**Q2**: Table 9（Appendix D, p21）显示 per-relation DR elimination 在 EVALUATE-FOR 关系上效果最好（κ=0.361）但在 COMPARE 关系上（κ=0.528）反而未完全消除。能否解释为什么更高的 κ 在此关系上未能完全消除 DR？\n\n**Q3**: 在 DocRED 上 fine-tuning 后 R-F1 仅提升约 0.5pp（Table 2），但 DR 大幅下降。这是否意味着被消除的 DR violations 原本对 F1 的影响微乎其微（即它们主要出现在 precision 端的 false positives 中）？\n\n**Q4**: 论文提到 entity registry 在 S1 模式下\"populates dynamically\"（§3.4），意味着在生成第一个 triple 时 registry 为空。如何处理第一个 triple 的 domain/range 约束？是否退化为纯 grammar 层？\n\n---\n\n## Missing References\n\n1. **Grammar-constrained decoding for structured information extraction with fine-tuned generative models applied to clinical trial abstracts** (Koldehoff et al., Frontiers in AI, 2025) — 将 grammar-constrained decoding + 本体约束应用于临床试验 IE，与 OntoCoDec 的方法论高度相关但在不同领域。\n2. **Schema RL** (Lu et al., ACL 2025) — 论文 bib 中存在但未在正文中引用（orphan entry `schema_rl2025`）。该工作提出通过 RL 学习生成符合 schema 约束的结构化输出，应在 Related Work 中讨论。\n\n---\n\n## Overall Assessment\n\n**评分: 3.5 (Borderline Conference)**  \n**置信度: 4/5 (Quite sure)**\n\n**理由**: 本文解决了一个真实且重要的问题（LLM-based IE 中的类型违规），提供了严格的形式化论证（Proposition 1）和系统的实验验证。实验设计质量高：四类违规分类法、三数据集四模型的消融矩阵、fine-tuning composability 验证。论文在 Limitations 中的自我批评也令人赞赏。\n\n主要顾虑在新颖性和 claim 校准两方面：(1) 语义层的核心机制（runtime state tracking + preventive masking）在 constrained decoding 文献中并非全新——IterGen、PICARD 等已在其他领域建立了 grammar + semantic 的双层范式，OntoCoDec 的主要增量是将其专门化到 IE 本体约束；(2) κ̄ 在 contribution 列表中被过度包装为 \"analytical framework\"，与论文自身承认的描述性本质不一致。如果作者能更精确地定位新颖性（IE-specific compilation + dynamic masking 的效率优势）并降低 κ̄ 的声称级别，论文更可能达到 Conference 水平。目前的 claim 校准问题使其落在 Conference/Findings 的边界上。\n",
  "reviewer_id": "2",
  "project": "schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 2 审稿意见：OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints\n\n**审查侧重：新颖性 + 完整性 + 写作质量**\n\n---\n\n## Summary\n\n本文提出 OntoCoDec，一个将 IE 本体约束编译为双层解码约束的框架：语法层（S1）通过 XGrammar 保证 JSON 结构合法性和词汇成员关系；语义层（S2）通过运行时 entity registry 和 dynamic masking 强制 domain/range 类型兼容性。论文在 Proposition 1 中证明带无界实体集的类型约束不属于 context-free，从而为语义层的必要性提供了形式化论证。引入 constraint tightness κ̄ 作为 schema 限制性的描述性度量。在 SciERC（551篇）、DocRED（998篇）、WikiEvents（246篇）三个数据集上，使用 Qwen3-8B、Llama-3.1-8B、Mistral-7B 等模型进行了系统的消融实验。\n\n---\n\n## 总体评分\n\n**Overall**: 3.5 — Borderline Conference\n\n**一句话总结**: 技术执行和实验设计高质量，但核心新颖性——语义层 dynamic masking——与已有工作（IterGen、PICARD 等）的概念差异阐述不足，κ̄ 作为\"分析框架\"的贡献被过度声称。\n\n---\n\n## 官方维度打分（来自 ACL ARR review form, Feb 2025+）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 4/5 | 主要 claim 均有充分实验支撑；Proposition 1 形式化论证严谨；消融研究系统完整；论文坦诚承认 κ̄ 的统计局限性 |\n| Excitement | 3/5 | 解决真实问题（LLM-IE 中的类型违规），实用价值明确；但核心技术增量（entity registry + dynamic masking）概念上较直接，κ̄ 更接近描述性统计而非深层理论贡献 |\n| Reproducibility | 4/5 | 提供了详细的 prompt 模板（Appendix A）、超参数配置（Appendix F）、硬件信息、随机种子验证（Appendix F）；代码承诺开源但提交时未附 |\n| Confidence | 4/5 | 熟悉 constrained decoding 和 structured IE 领域，仔细阅读了全部 31 页（含附录） |\n\n---\n\n## 主要优势\n\n**S1. 形式化论证严谨且有实际意义。** Proposition 1（§3.1, p3）证明带无界实体集的 IE 类型约束不属于 context-free 语言，这为双层架构提供了不可跳过的理论基础。Corollary 进一步推导出 enabling dependency 的必要性。这不仅是学术优雅——它直接解释了为什么 XGrammar/Outlines 等纯 grammar 方案在 IE 场景下必然不足。\n\n**S2. 违规分类法和消融设计极为系统。** 论文将输出违规分解为 DR（domain/range）、CF（cross-field）、RV（relation vocabulary）、ET（entity typing）四类（§5, Table 1），然后在每个消融配置下逐项报告。这种精细度远超同领域多数论文的二元\"valid/invalid\"评估，允许读者精确理解每层约束的贡献和代价。\n\n**S3. 实验覆盖面广且诚实。** 三个数据集（sentence-level RE、document-level RE、event extraction）× 四个模型 × 多种配置（zero-shot / fine-tuned / beam search / S1 vs S2）。Limitations section（p9）明确承认：CF 是模型相关的、评估仅限一种微调方法（LoRA）、模型规模限于 7-8B。这种诚实度值得肯定。\n\n**S4. Fine-tuning composability 论证有价值。** Table 2（p6）展示 LoRA fine-tuning + OntoCoDec 约束是可组合的：fine-tuning 减少 DR 至 1-2%，加入 S1 后进一步消除或接近消除 DR（< 0.09%），同时 R-F1 保持稳定。这回答了一个重要的部署问题——约束系统是否与参数优化兼容。\n\n**S5. κ̄ 与违规率的关联分析提供实用的部署指导。** 尽管统计上不够confirmatory（论文自己承认 df=2, p>0.05），但 κ̄ × RV_baseline 作为 DR 的预测因子（Appendix C, Figure 1, p20）为实际部署中选择约束策略提供了直觉：κ > 0.5 的 schema 可在 zero-shot 下实现近零 DR，低 κ schema 需要 fine-tuning。\n\n**S6. WikiEvents 扩展验证了跨本体泛化。** §5.4（p7）将框架扩展到事件抽取（KAIROS 本体，56 event types, 80 argument roles），无需修改即可应用。虽然只是 zero-shot 评估，但展示了框架在正式本体（vs. 经验衍生类型集）上的适用性。\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] 语义层核心机制（entity registry + dynamic masking）与 IterGen 的概念区分不充分\n\n- 具体位置：§6 Related Work（p8）, Appendix B（p13-17）\n- 问题：IterGen（Ugare et al., 2025, ICLR 2025）同样在 grammar 层之上叠加语义约束，在生成过程中检测违规并通过 backtracking 修正。OntoCoDec 的 dynamic masking 与 IterGen 的 semantic check + backtracking 是解决同一类问题（grammar-valid 但 semantically-invalid 输出）的两种机制。论文在 §6 和 Appendix B 中仅将 IterGen 列为相关工作之一，未深入对比两者在机制设计（preventive masking vs. corrective backtracking）、效率特性（OntoCoDec 无需回退 vs. IterGen 需要 KV cache 管理）、和约束表达能力（OntoCoDec 限于 domain/range vs. IterGen 支持任意 semantic predicate）上的差异。类似地，PICARD（Scholak et al., 2021）的 incremental parsing monitor 与 OntoCoDec 的 runtime entity registry 在概念上高度相似——均为在解码过程中维护状态以检查上下文相关约束。\n- 为什么影响接收：新颖性是接收决定的关键维度。如果审稿人认为核心机制是已有方法（preventive masking / runtime monitor）在 IE 场景的 application，而非方法论创新，则难以达到 main conference 标准。\n- 建议修改方向：在 §6 中增加一段显式的机制对比表（OntoCoDec vs. IterGen vs. PICARD），明确阐述：(1) OntoCoDec 的 forward-only masking 的效率优势及其 one-step-lookahead 的局限；(2) IterGen 的 backtracking 允许任意 semantic predicate 但引入 KV cache overhead 和 non-monotonic generation；(3) PICARD 的 token-level filtering 与 OntoCoDec entity registry 的粒度差异。\n\n**N2** [critical] κ̄ 作为 Contribution 2（\"analytical linking framework\"）被过度声称\n\n- 具体位置：Abstract（p1, \"an analytical linking constraint tightness to enforcement outcomes\"）, §1 Contributions 列表 item 2（p2）, §4（p4-5）\n- 问题：κ̄ 的定义（§4, Eq. 3: κ = 1 − |S(r)|/|E|）本质上是每个 relation 的类型集合大小相对于总实体类型数的归一化比例——这是一个描述性统计量，而非一个分析框架。论文自身在 Appendix C（p20）承认回归分析\"constitutes a descriptive characterization rather than a confirmatory statistical test\"（df=2, p>0.05）。然而，Abstract 和 Contribution 列表仍将其定位为\"analytical linking framework\"，这与论文自身的谨慎表述不一致。\n- 为什么影响接收：Contribution 列表的每一项都应与论文实际提供的证据水平匹配。将描述性统计提升为\"分析框架\"属于 overclaim，可能导致审稿人对整篇论文的 claim 可信度产生质疑。\n- 建议修改方向：将 Contribution 2 重新表述为\"a descriptive metric, constraint tightness κ̄, that correlates with enforcement outcomes and provides deployment guidance\"，去掉\"analytical framework\"的措辞。在 Abstract 中也相应调整。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] 无直接实验对比最接近的 IE 基线 BoostCD\n\n- 具体位置：§5（p5-7）, §6（p8）\n- 问题：BoostCD（Sakota et al., 2025）是唯一同样将 constrained decoding 应用于 IE 的已发表工作（EMNLP 2025），且使用了 SciERC 和 DocRED 作为评估数据集。论文引用了 BoostCD 但未进行任何实验对比。即使两者的 setting 不完全相同（BoostCD boosting 无约束/有约束解码；OntoCoDec 使用两层约束），也应提供同一数据集上的结果对比，或至少详细讨论为何直接比较不可行。\n- 建议：(1) 如果 BoostCD 代码可用，在 SciERC 上运行对比实验；(2) 若不可行，在 §5 或 §6 中增加一段定性分析，引用 BoostCD 报告的数字并讨论方法论差异导致的预期性能差异。\n\n**W2** [warning] \"Ontology-agnostic\" 声称的实验支撑不充分\n\n- 具体位置：Abstract（p1）, §1 Contribution 3（p2）, §7（p8）\n- 问题：三个评估数据集中，SciERC 和 DocRED 的类型约束来自训练数据的经验统计（\"type pairs extracted from annotated training data\"，§2, p2），并非形式化本体。仅 WikiEvents 使用了正式本体（KAIROS）。且 WikiEvents 评估仅为 zero-shot（246 篇），无 fine-tuning 验证。声称框架 \"ontology-agnostic\" 需要更强的证据——至少应在 2+ 个正式本体上验证，或明确限定 claim 的范围。\n- 建议：将 \"ontology-agnostic\" 限定为 \"applicable to both formal ontologies and empirically-derived type constraints\"，并在 Limitations 中明确指出仅在一个正式本体上验证。\n\n**W3** [warning] 正文 Related Work（§6）过于压缩\n\n- 具体位置：§6（p8，约 15 行正文）\n- 问题：正文 Related Work 仅覆盖三个轴各一小段，实质性讨论全部推迟到 Appendix B（p13-17, 约 2.5 页）。虽然 ARR 规则不禁止这种安排，但审稿人无义务阅读附录。正文中未充分讨论与关键竞争者（BoostCD、IterGen、CRANE、GoLLIE）的差异，使得审稿人难以仅从正文评判新颖性。\n- 建议：在 8 页限制内，将 §6 扩展至至少半页，将 IterGen/BoostCD 的机制对比从附录移入正文。可通过压缩 §5.4（WikiEvents 细节可移入附录）来腾出空间。\n\n**W4** [warning] Abstract 信息密度过高，关键 message 被数字淹没\n\n- 具体位置：Abstract（p1）\n- 问题：Abstract 中包含大量具体数字（\"DR 40-46%\"、\"R-F1 0.099\"、\"76-99%\"、\"88-70B\" 等），阅读体验接近结果表格的自然语言复述，而非对核心贡献的提炼。关键 insight（为什么 grammar 层不够、语义层如何补足、这对 IE 部署意味着什么）被数字细节遮蔽。\n- 建议：保留 1-2 个最关键的数字（如 DR 减少幅度和 R-F1 保持稳定），其余推至 Introduction。Abstract 应更侧重 conceptual framing。\n\n**W5** [warning] 模型规模限于 7-8B，对 claim 泛化性的影响在正文中未充分 hedge\n\n- 具体位置：§5（p5-7）, §7（p8）\n- 问题：所有实验使用 7-8B 参数模型。Limitations（p9）提到 \"scaling to smaller models has not been verified\"，但更值得关注的是向上的 scaling——70B+ 模型通常 baseline 违规率更低，OntoCoDec 的边际增益可能不同。§7 的结论 \"drops by 76-99% for calibrated models\" 未 hedge 模型规模。\n- 建议：在 §7 结论中增加 \"across 7-8B parameter models\" 的限定词。\n\n**W6** [warning] CF 代价在 Abstract/Contribution 中不够透明\n\n- 具体位置：Abstract（p1）, §4（p4）\n- 问题：Grammar-first fallback 在解决 DR 的同时引入 CF 违规（cross-field inconsistency）。Table 1 显示 Full S1 在 SciERC 上 CF 从 0 增至 ~0.33%。虽然 §4 和 Appendix C 详细讨论了这一 trade-off，但 Abstract 仅轻描淡写地提到 \"grammar-first fallback when constraints conflict\"，未量化其代价。审稿人可能认为论文在选择性地突出优势、淡化局限。\n- 建议：在 Abstract 中增加一句简短的 trade-off 说明，如 \"with modest cross-field consistency costs (≤0.33% on SciERC) resolvable via beam search or fine-tuning\"。\n\n---\n\n## 小问题（不影响接收）\n\n- **M1**: .bib 文件中有 10 个 orphan entries（在 bib 中但未在论文中引用），包括 `sakota2025boostcd`（与 `boostcd2025` 重复）、`lee2026formattax`（与 `formattax2026` 重复）等。应清理 bib 文件。\n- **M2**: `schall2025hiddencost` bib key 重复出现两次。\n- **M3**: §3.4 的 S1/S2 命名（Single-pass / Two-pass）与 §5 中的层级编号（S1 语法层、S2 语义层）初读时易混淆，虽然定义清晰但建议重命名为 SP/TP 或类似标记以避免歧义。\n- **M4**: Table 5（p7, WikiEvents）的 \"—\" 标记（\"not applicable\"）缺少表注解释。\n- **M5**: Appendix F（p26-27）提供了详细的复现细节，但 random seed 验证（seeds 123, 456）仅在 greedy decoding 下进行，beam search 的 non-determinism 仅报告了 variance < 0.5pp 而未提供具体 seed 信息。\n\n---\n\n## Questions for Authors\n\n**Q1**: IterGen 的 backtracking 机制理论上可以处理任意 semantic predicate，而 OntoCoDec 的 dynamic masking 限于 domain/range 类型兼容。是否考虑过将 OntoCoDec 扩展到更一般的语义约束（如 cardinality constraints、temporal ordering）？如果有，主要技术障碍是什么？\n\n**Q2**: Table 9（Appendix D, p21）显示 per-relation DR elimination 在 EVALUATE-FOR 关系上效果最好（κ=0.361）但在 COMPARE 关系上（κ=0.528）反而未完全消除。能否解释为什么更高的 κ 在此关系上未能完全消除 DR？\n\n**Q3**: 在 DocRED 上 fine-tuning 后 R-F1 仅提升约 0.5pp（Table 2），但 DR 大幅下降。这是否意味着被消除的 DR violations 原本对 F1 的影响微乎其微（即它们主要出现在 precision 端的 false positives 中）？\n\n**Q4**: 论文提到 entity registry 在 S1 模式下\"populates dynamically\"（§3.4），意味着在生成第一个 triple 时 registry 为空。如何处理第一个 triple 的 domain/range 约束？是否退化为纯 grammar 层？\n\n---\n\n## Missing References\n\n1. **Grammar-constrained decoding for structured information extraction with fine-tuned generative models applied to clinical trial abstracts** (Koldehoff et al., Frontiers in AI, 2025) — 将 grammar-constrained decoding + 本体约束应用于临床试验 IE，与 OntoCoDec 的方法论高度相关但在不同领域。\n2. **Schema RL** (Lu et al., ACL 2025) — 论文 bib 中存在但未在正文中引用（orphan entry `schema_rl2025`）。该工作提出通过 RL 学习生成符合 schema 约束的结构化输出，应在 Related Work 中讨论。\n\n---\n\n## Overall Assessment\n\n**评分: 3.5 (Borderline Conference)**  \n**置信度: 4/5 (Quite sure)**\n\n**理由**: 本文解决了一个真实且重要的问题（LLM-based IE 中的类型违规），提供了严格的形式化论证（Proposition 1）和系统的实验验证。实验设计质量高：四类违规分类法、三数据集四模型的消融矩阵、fine-tuning composability 验证。论文在 Limitations 中的自我批评也令人赞赏。\n\n主要顾虑在新颖性和 claim 校准两方面：(1) 语义层的核心机制（runtime state tracking + preventive masking）在 constrained decoding 文献中并非全新——IterGen、PICARD 等已在其他领域建立了 grammar + semantic 的双层范式，OntoCoDec 的主要增量是将其专门化到 IE 本体约束；(2) κ̄ 在 contribution 列表中被过度包装为 \"analytical framework\"，与论文自身承认的描述性本质不一致。如果作者能更精确地定位新颖性（IE-specific compilation + dynamic masking 的效率优势）并降低 κ̄ 的声称级别，论文更可能达到 Conference 水平。目前的 claim 校准问题使其落在 Conference/Findings 的边界上。\n",
    "reviewer_id": "2",
    "project": "schema_semantic_constrained_ie"
  }
}
```

</details>

---


### Tool result

_source line 949 · 2026-05-20T17:17:38.998004+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_01fc90ae186a4ed432770f7601995139:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3910
}
```

</details>

---


### Assistant

_source line 950 · 2026-05-20T17:17:48.423465+00:00_

审稿意见已提交给 Review Director。

**审稿结论摘要**：

- **Overall: 3.5（Borderline Conference）**，Soundness 4/5，Excitement 3/5
- **2个 Must-Fix**：(1) 语义层核心机制与 IterGen/PICARD 的概念区分不足，新颖性论证需要加强；(2) κ̄ 作为"analytical framework"被过度声称，应降级为"descriptive metric"
- **6个 Should-Fix**：无 BoostCD 直接实验对比、"ontology-agnostic"支撑不足、正文 Related Work 过于压缩、Abstract 数字过载、模型规模 hedge 不足、CF 代价透明度不够
- **5个 Minor**：bib 清理（10个 orphan + 1个 duplicate key）、S1/S2 命名歧义、表注缺失、seed 信息不完整
- **核心判断**：技术执行和实验设计是高质量的，但 claim 校准问题（κ̄ overclaim + 新颖性定位不精确）使论文落在 Conference/Findings 边界

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2"
}
```

</details>

---


## Round 21

## Round 21

24 recorded events


### User

_source line 951 · 2026-05-20T17:20:43.884157+00:00_

[Round 1 审稿请求]:
以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每个 Must-Fix、Should-Fix、Minor 问题标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

## Reviewer 1 审稿意见（方法严谨性 + 实验设计）

**Overall: 3.5 Borderline Conference | Soundness 3.5/5 | Excitement 3.5/5 | Reproducibility 4/5 | Confidence 4/5**

### Must-Fix

**N1** [critical] Proposition 1 证明不严格，与论文的形式化定位不匹配
- Section 3, §3.1, "Proof sketch"
- 论文核心贡献之一是"可判定性引导的约束分类"，Proposition 1（Level 2 ⊄ Level 1）仅给出 proof sketch，缺少：(a) 到已知不可判定性结果的形式化归约；(b) "independently unbound" 的精确定义；(c) 完整数学证明。
- 建议：附录中提供完整形式化证明（pumping lemma / 闭包性质），或降低形式化声称力度。

**N2** [critical] "Exact enforcement" 声称与 36.64% CF fallback rate 存在根本矛盾
- Abstract, §3.3 ("exact pair-based enforcement"), §4, Appendix C Table 7-8
- Appendix C 显示 grammar-first fallback 在 36.64% 的 type-bearing positions 被触发。当 fallback 时语义约束被完全丢弃。论文未分析级联失败（cascading failures）的可能性——一次 fallback 的错误类型赋值是否影响后续 entity registry 状态。
- 建议：将 "exact" 改为 "best-effort pair-based enforcement with grammar-first fallback"；分析 fallback 级联行为。

**N3** [critical] WikiEvents fine-tuning 评估仅 20 文档测试集，统计效力严重不足
- §5.4, Table 5, Limitations (page 9)
- 20 篇文档上 bootstrap p-values 不可靠，置信区间极宽，但 Table 5 与 SciERC/DocRED 并列暗示同等可信度。
- 建议：正文中明确标注规模限制，报告 95% bootstrap CI，考虑 cross-validation。

### Should-Fix

**W1** [warning] 缺少与最相关并发工作的直接实验对比
- 未与 BoostCD、CRANE、IterGen、GCD 直接对比数字。

**W2** [warning] 跨模型验证局限于 7-8B 参数规模
- Abstract "applies to any autoregressive LM" 未加限定。

**W3** [warning] 零样本 R-F1（0.08-8%）场景下 violation rate 分析的实际意义需要更明确讨论
- 论文定位为 "diagnostic" 是恰当的，但表格中零样本和微调结果并排呈现可能误导读者。

**W4** [warning] Entity registry 的顺序依赖可能导致 globally suboptimal type assignment
- 贪心策略局部最优但全局次优，TCR 是事后修复而非生成时 exact enforcement。

**W5** [warning] DocRED beam search 实验仅使用 50 文档子集
- SciERC 用了完整 551 文档，DocRED 仅 50 文档。DocRED 文档更长、关系类型更多。

### Minor
- §4 Eq.(2) conjunction 是逐位 AND 应明确说明
- CF 列含义首次出现时未充分解释
- Figure 1 x 轴 label 不直观
- Appendix G LoRA 3 epochs 是否充分
- §6 末尾一段更像 contribution 声称

### Questions
Q1: Proposition 1 能否通过 pumping lemma 完整证明？schema 对 entity 数量设上限时是否仍成立？
Q2: Grammar-first fallback 的级联行为——一次 fallback 的错误类型赋值是否触发更多 fallback？
Q3: S2 的 DR 反而高于 S1——two-pass 是否引入额外错误来源？
Q4: LoRA 统一超参数（r=16, α=32）是否做过敏感性分析？
Q5: 对称关系的 κ 计算是否低估了实际约束紧度？

### Missing References
1. BoostCD (Sakota et al., 2025) — 已引用但未实验对比
2. GCD (Geng et al., 2023) — 应明确展示 baseline 数字
3. Schema-RL (Lu et al., 2025) — bib 中未被引用

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 952 · 2026-05-20T17:21:27.390694+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.pdf",
  "project": "schema_semantic_constrained_ie",
  "pages": "1-8",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.pdf",
    "project": "schema_semantic_constrained_ie",
    "pages": "1-8",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 953 · 2026-05-20T17:21:28.546094+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 467.1}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 520.6}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 510.3}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 512.3}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 531.0}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 527.2}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 481.1}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 506.5}], \"total_pages\": 31, \"rendered_pages\": 8, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/arti
…[truncated 73 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1155
}
```

</details>

---


### Tool call

_source line 954 · 2026-05-20T17:21:34.438875+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p3.png"
  }
}
```

</details>

---


### Tool call

_source line 955 · 2026-05-20T17:21:35.093869+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 956 · 2026-05-20T17:21:35.397710+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 958
}
```

</details>

---


### Tool call

_source line 957 · 2026-05-20T17:21:35.398186+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 958 · 2026-05-20T17:21:36.003334+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 909
}
```

</details>

---


### Tool result

_source line 959 · 2026-05-20T17:21:36.255663+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 857
}
```

</details>

---


### Tool call

_source line 960 · 2026-05-20T17:22:25.660401+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.pdf",
  "project": "schema_semantic_constrained_ie",
  "pages": "9,21,24,25",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.pdf",
    "project": "schema_semantic_constrained_ie",
    "pages": "9,21,24,25",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 961 · 2026-05-20T17:22:26.162635+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p9.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 521.6}, {\"page\": 21, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p21.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 483.5}, {\"page\": 24, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p24.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 465.9}, {\"page\": 25, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p25.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 452.5}], \"total_pages\": 31, \"rendered_pages\": 4, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 962 · 2026-05-20T17:22:30.230262+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p9.png"
  }
}
```

</details>

---


### Tool result

_source line 963 · 2026-05-20T17:22:30.934311+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 704
}
```

</details>

---


### Tool call

_source line 964 · 2026-05-20T17:22:30.934833+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p21.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p21.png"
  }
}
```

</details>

---


### Tool result

_source line 965 · 2026-05-20T17:22:31.640464+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 705
}
```

</details>

---


### Tool call

_source line 966 · 2026-05-20T17:22:31.640965+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p24.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p24.png"
  }
}
```

</details>

---


### Tool call

_source line 967 · 2026-05-20T17:22:31.942379+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p25.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p25.png"
  }
}
```

</details>

---


### Tool result

_source line 968 · 2026-05-20T17:22:32.397486+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 756
}
```

</details>

---


### Tool result

_source line 969 · 2026-05-20T17:22:32.803659+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 861
}
```

</details>

---


### Tool call

_source line 970 · 2026-05-20T17:22:55.177132+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 971 · 2026-05-20T17:22:55.227795+00:00_

{"result":"{\"success\": true, \"data\": {\"deleted\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 972 · 2026-05-20T17:24:39.389964+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 2 交叉回应 Reviewer 1 审稿意见\n\n---\n\n## Must-Fix 回应\n\n### [REBUT] R1-N1: Proposition 1 证明不严格\n\nR1 的批评混淆了两个不同的概念。R1 要求 \"(a) 到已知不可判定性结果的形式化归约\"——但 Proposition 1 声称的是 **non-context-freeness**（Level 2 ⊄ Level 1），不是 undecidability。这两者的证明方法完全不同：non-CF 通常用 pumping lemma 或闭包性质，而非不可判定性归约。R1 混淆了 Chomsky 层级中的\"不属于 CFL\"和\"不可判定\"，前者是 Proposition 1 的实际声称。\n\n关于证明本身：§3.1（p3）的 proof sketch 使用 PDA stack 论证——当实体集无界时，识别合法的类型约束输出需要在任意位置间维护 entity-type binding，这超出了 PDA 的能力（pushdown automaton 只有一个 stack，无法同时追踪无界数量的 entity-type 对应关系）。这个论证的核心机制与经典的 {a^n b^n c^n ∉ CFL} 结果同构，在形式语言理论中是标准的。\n\n不过我**部分同意** R1 的关切：论文将此定位为核心贡献之一（\"decidability-guided constraint classification\"），那么形式化水平应与声称力度匹配。当前的 proof sketch 对于经验性 NLP 论文是可接受的，但对于声称\"形式化分类\"的贡献来说偏弱。\n\n**建议**：在附录中补充完整的 pumping lemma 证明（约半页），或将 contribution 表述从 \"formal classification\" 降级为 \"a classification motivated by formal language-theoretic observations\"。但 R1 要求的\"不可判定性归约\"是不恰当的——Proposition 1 的目标不是证明不可判定性。\n\n---\n\n### [AGREE] R1-N2: \"Exact enforcement\" 声称与 CF fallback 的矛盾\n\nR1 的观察精确且有力。§3.3（p3）使用 \"exact pair-based enforcement\"，但 §4（p4）的 grammar-first fallback 机制意味着当 S(t)∩G(t)=∅ 时语义约束被完全放弃。Table 8（Appendix C, p21）证实 SciERC 上 245 个 CF violations 中 GENERIC 实体类型占 63.3%（155/245），总共 345 个冲突 type pairs。这不是边缘情况。\n\n**R1 关于级联失败的追问特别重要**：我验证了 §3.3（p3）的 entity registry 设计——registry 在生成过程中增量填充（\"each completed entity (n_i, τ_i) adds (n_i, τ_i) to P\"）。因此，一次 fallback 导致的错误类型赋值**确实**会写入 registry，影响后续所有涉及该实体的 relation 的 domain/range 检查。论文未分析这种级联效应。\n\n补充一个数据点：Table 9（p21）显示 per-relation DR elimination 在 EVALUATE-FOR（κ=0.361）上完全成功但在 COMPARE（κ=0.528, 5.00%）上仍有残留——这可能部分归因于 fallback 级联：COMPARE 涉及更多 ambiguous entity types（Table 8 的 GENERIC→Metric 和 GENERIC→Method 各占 12.2% 和 6.9% 的 CF），而 fallback 后的错误类型可能导致后续 DR 无法消除。\n\n**建议**：同意 R1——将 \"exact\" 改为 \"best-effort\" 或 \"targeted\"，并增加 fallback 级联分析。这是一个 must-fix 级别的术语校准问题。\n\n---\n\n### [AGREE] R1-N3: WikiEvents fine-tuning 20 文档测试集统计效力不足\n\n**部分同意，但需要校正 R1 的指向范围。**\n\nTable 5（p7）标题明确区分了两种评估：zero-shot 使用 **完整 246 文档**；fine-tuning 使用 **194/20/20 split**（20 文档测试集）。WikiEvents 的主要验证是 zero-shot（246 docs），不是 fine-tuning。R1 的批评对 fine-tuning 行完全成立——20 文档上的 bootstrap 统计确实不可靠——但不应否定 zero-shot 行（246 docs）的有效性。\n\n然而，Table 5 确实将两种设定的结果**并列呈现**，且未在表格内部标注样本量差异。这使得读者可能将 20-doc fine-tuning 结果的可信度等同于 246-doc zero-shot 结果。\n\n**建议**：(1) Table 5 内标注测试集大小（n=246 / n=20）；(2) fine-tuning 行报告 95% bootstrap CI；(3) 在正文中明确指出 fine-tuning 评估是 **preliminary** 的，主要验证是 zero-shot 设定。这样既保留了有用信息，又不误导读者。\n\n---\n\n## Should-Fix 回应\n\n### [AGREE] R1-W1: 缺少与 BoostCD/CRANE/IterGen/GCD 的直接实验对比\n\n与我的 W1 一致。BoostCD（Sakota et al., 2025）在 SciERC 和 DocRED 上有结果，是最直接的对比对象。即使 setting 不完全相同（BoostCD 的 boosting 策略 vs. OntoCoDec 的确定性约束），同一数据集上的数字对比对审稿人判断边际贡献至关重要。\n\n---\n\n### [AGREE] R1-W2: 模型规模限于 7-8B，Abstract 声称 \"any autoregressive LM\" 未加限定\n\n与我的 W5 一致。Abstract（p1）说 \"applies to any autoregressive LM across four models (8B-70B)\"——但实际测试的模型参数量范围仅为 7B-8B（Qwen3-8B, Llama-3.1-8B, Mistral-7B, Llama-3.1-8B）。\"8B-70B\" 的表述来自何处不明——可能是计划中的实验但未执行？正文中应删除或修正此声称。\n\n---\n\n### [REBUT] R1-W3: 零样本 R-F1（0.08-8%）场景下违规率分析的实际意义\n\nR1 认为在极低 R-F1 下分析违规率实际意义存疑。我**不完全同意**。\n\n论文明确将零样本设定定位为 **diagnostic**（§5, p5: \"Zero-shot evaluation (§5.1-§5.3) isolates layer contributions as a diagnostic\"）。违规率分析的价值独立于任务性能：它揭示 LLM 在无任务特定训练时的**结构输出模式**——哪些类型的约束违规最频繁、违规与 schema 属性（κ̄）的关系等。这些 insight 对理解 LLM 的本体感知能力有独立价值，不因 R-F1 低而失效。\n\n类比：分析一个未经训练的代码 LLM 生成代码的 type errors 分布，即使代码无法编译运行，对理解模型的类型系统感知能力仍有诊断意义。\n\n**但我同意一点**：Table 1（p5）中 zero-shot 和 fine-tuned 结果并排呈现，可能使读者对零样本结果的实用性产生过高预期。建议在 Table 1 中增加视觉分隔（如水平线）或在 caption 中强调诊断性质。\n\n---\n\n### [AGREE] R1-W4: Entity registry 顺序依赖导致全局次优类型赋值\n\n这是一个有洞察力的观察。§3.3（p3）的 entity registry 按生成顺序增量填充，第一次出现的 entity 的类型赋值锁定所有后续引用。如果一个 entity 在第一个 triple 中被赋予次优类型（因为第一个 triple 的 relation 对该 entity type 的约束较宽松），后续更紧约束的 relation 就无法修正。\n\n§3.4（p4）提到的 TCR（Type Consistency Repair）是事后修复（beam search 或 post-hoc re-scoring），不是生成时的 exact enforcement——这进一步支持 R1-N2 的 \"exact\" 术语批评。\n\n补充证据：Table 10（Appendix D, p21）的 four-way ablation 显示 \"Semantic layer is the sole effective DR defense, providing 39-69% reduction\"——但这个 reduction 的上限可能受限于顺序依赖导致的次优赋值。如果 entity registry 能全局优化（如 ILP），DR reduction 可能更高。这是论文未讨论的理论上限。\n\n---\n\n### [AGREE] R1-W5: DocRED beam search 仅 50 文档子集\n\nTable 15（Appendix E, p24）确认 DocRED beam search 在 \"matched 50-document subsets\" 上评估。DocRED 有 96 个 relation types（vs. SciERC 的 7 个），50 文档可能无法覆盖足够多的 relation types 来验证 beam search 的普适效果。\n\nAppendix E 解释了原因：\"~300h due to extended generation under high-temperature sampling with complex schemas\"——这是合理的计算资源限制，但应在正文中标注，并讨论子集代表性（如覆盖的 relation type 比例）。\n\n---\n\n## Minor 回应\n\n- **Eq.(2) conjunction 是逐位 AND**：[AGREE] §4（p4）Eq. 2 的 M_final(t) = M_grammar(t) ∧ M_semantic(t) 确实是逐 token 的逐位 AND，应在正文中明确说明\"element-wise conjunction over the vocabulary\"。\n\n- **CF 列含义首次出现时未充分解释**：[AGREE] Table 1（p5）首次引入 CF 列时，caption 仅说 \"CF = cross-field consistency violations\"，但 CF 的具体含义（同一 entity 在不同 triple 中被赋予不同类型）需要回溯到 §2（p2）才能理解。建议在 Table 1 caption 中增加一句解释。\n\n- **Figure 1 (Appendix C, p20) x 轴 label 不直观**：[AGREE] x 轴是 κ × RV_baseline 的乘积，物理含义不直观。建议增加轴标签注释。\n\n- **Appendix G LoRA 3 epochs 是否充分**：[REBUT] 3 epochs 是 LoRA fine-tuning 的常见设定（Hu et al., 2022 原始论文使用 3-5 epochs）。Appendix G（p26-27）报告了 completion-only loss，且 SciERC 有 1,762 训练样本、DocRED 有 3,053 样本，3 epochs 下梯度更新分别为 333/573 steps（batch size 16, gradient accumulation 4），对于 LoRA rank=16 的小参数量是合理的。若 R1 怀疑 underfitting，应指出具体证据（如 training loss 未收敛）。\n\n- **§6 末尾一段更像 contribution 声称**：[AGREE] §6（p8）最后一段确实从 related work positioning 滑向了 contribution recapping，建议修改为更明确的 differentiation 表述。\n\n---\n\n## R1 Questions 评价\n\n**Q1（Pumping lemma + 有界 entity 数量）**：好问题。如果 schema 对 entity 数量设上限 k，则有效输出集变为有限语言（有限语言都是正则的，因此也是 CF 的）。Proposition 1 的 \"unbounded\" 前提至关重要——论文应讨论 bounded entity set 的退化情况。\n\n**Q2（Fallback 级联行为）**：最关键的问题，与 N2 直接相关。如上分析，级联确实可能发生。\n\n**Q3（S2 的 DR 高于 S1）**：有价值。Table 1 显示 S2 在某些配置下 DR 确实高于 S1。可能原因：two-pass 的第一次 pass 提取的 entity 集合不完全，导致第二次 pass 的 registry 缺失部分 entity，fallback 更频繁。\n\n**Q4（LoRA 超参数敏感性）**：合理关切，但优先级低于 N1-N3。\n\n**Q5（对称关系 κ 计算）**：技术上有趣。对称关系的 head/tail type set 相同，κ_head = κ_tail，但 §4 脚注 1（p4）已说明\"we evaluate on directed triples\"——因此对称关系的 κ 不存在 head/tail 不对称导致的低估问题。但 R1 可能在问更细微的点：对称关系是否使得有效类型对比非对称关系更多（因为 head 和 tail 可互换），从而 κ 低估了 constraint 的实际宽松度。这值得作者回应。\n\n---\n\n## 综合评价\n\nR1 的审稿在方法严谨性维度上非常深入。N2（\"exact\" vs fallback 矛盾 + 级联失败）和 W4（顺序依赖全局次优）是本轮审稿中最有技术深度的发现，两者联合起来构成了对论文核心声称的实质性挑战。N1 的方向正确但论证有误（混淆了 non-CF 与 undecidability）。N3 的范围应限定在 fine-tuning 行（20 docs）而非全部 WikiEvents 结果（246 docs）。\n\n两位 Reviewer 的共识问题：(1) 缺少与 BoostCD 的直接实验对比（R1-W1, R2-W1）；(2) 模型规模声称过宽（R1-W2, R2-W5）；(3) κ̄/形式化贡献的声称力度与证据不匹配（R1-N1, R2-N2）。\n",
  "reviewer_id": "2",
  "project": "schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 2 交叉回应 Reviewer 1 审稿意见\n\n---\n\n## Must-Fix 回应\n\n### [REBUT] R1-N1: Proposition 1 证明不严格\n\nR1 的批评混淆了两个不同的概念。R1 要求 \"(a) 到已知不可判定性结果的形式化归约\"——但 Proposition 1 声称的是 **non-context-freeness**（Level 2 ⊄ Level 1），不是 undecidability。这两者的证明方法完全不同：non-CF 通常用 pumping lemma 或闭包性质，而非不可判定性归约。R1 混淆了 Chomsky 层级中的\"不属于 CFL\"和\"不可判定\"，前者是 Proposition 1 的实际声称。\n\n关于证明本身：§3.1（p3）的 proof sketch 使用 PDA stack 论证——当实体集无界时，识别合法的类型约束输出需要在任意位置间维护 entity-type binding，这超出了 PDA 的能力（pushdown automaton 只有一个 stack，无法同时追踪无界数量的 entity-type 对应关系）。这个论证的核心机制与经典的 {a^n b^n c^n ∉ CFL} 结果同构，在形式语言理论中是标准的。\n\n不过我**部分同意** R1 的关切：论文将此定位为核心贡献之一（\"decidability-guided constraint classification\"），那么形式化水平应与声称力度匹配。当前的 proof sketch 对于经验性 NLP 论文是可接受的，但对于声称\"形式化分类\"的贡献来说偏弱。\n\n**建议**：在附录中补充完整的 pumping lemma 证明（约半页），或将 contribution 表述从 \"formal classification\" 降级为 \"a classification motivated by formal language-theoretic observations\"。但 R1 要求的\"不可判定性归约\"是不恰当的——Proposition 1 的目标不是证明不可判定性。\n\n---\n\n### [AGREE] R1-N2: \"Exact enforcement\" 声称与 CF fallback 的矛盾\n\nR1 的观察精确且有力。§3.3（p3）使用 \"exact pair-based enforcement\"，但 §4（p4）的 grammar-first fallback 机制意味着当 S(t)∩G(t)=∅ 时语义约束被完全放弃。Table 8（Appendix C, p21）证实 SciERC 上 245 个 CF violations 中 GENERIC 实体类型占 63.3%（155/245），总共 345 个冲突 type pairs。这不是边缘情况。\n\n**R1 关于级联失败的追问特别重要**：我验证了 §3.3（p3）的 entity registry 设计——registry 在生成过程中增量填充（\"each completed entity (n_i, τ_i) adds (n_i, τ_i) to P\"）。因此，一次 fallback 导致的错误类型赋值**确实**会写入 registry，影响后续所有涉及该实体的 relation 的 domain/range 检查。论文未分析这种级联效应。\n\n补充一个数据点：Table 9（p21）显示 per-relation DR elimination 在 EVALUATE-FOR（κ=0.361）上完全成功但在 COMPARE（κ=0.528, 5.00%）上仍有残留——这可能部分归因于 fallback 级联：COMPARE 涉及更多 ambiguous entity types（Table 8 的 GENERIC→Metric 和 GENERIC→Method 各占 12.2% 和 6.9% 的 CF），而 fallback 后的错误类型可能导致后续 DR 无法消除。\n\n**建议**：同意 R1——将 \"exact\" 改为 \"best-effort\" 或 \"targeted\"，并增加 fallback 级联分析。这是一个 must-fix 级别的术语校准问题。\n\n---\n\n### [AGREE] R1-N3: WikiEvents fine-tuning 20 文档测试集统计效力不足\n\n**部分同意，但需要校正 R1 的指向范围。**\n\nTable 5（p7）标题明确区分了两种评估：zero-shot 使用 **完整 246 文档**；fine-tuning 使用 **194/20/20 split**（20 文档测试集）。WikiEvents 的主要验证是 zero-shot（246 docs），不是 fine-tuning。R1 的批评对 fine-tuning 行完全成立——20 文档上的 bootstrap 统计确实不可靠——但不应否定 zero-shot 行（246 docs）的有效性。\n\n然而，Table 5 确实将两种设定的结果**并列呈现**，且未在表格内部标注样本量差异。这使得读者可能将 20-doc fine-tuning 结果的可信度等同于 246-doc zero-shot 结果。\n\n**建议**：(1) Table 5 内标注测试集大小（n=246 / n=20）；(2) fine-tuning 行报告 95% bootstrap CI；(3) 在正文中明确指出 fine-tuning 评估是 **preliminary** 的，主要验证是 zero-shot 设定。这样既保留了有用信息，又不误导读者。\n\n---\n\n## Should-Fix 回应\n\n### [AGREE] R1-W1: 缺少与 BoostCD/CRANE/IterGen/GCD 的直接实验对比\n\n与我的 W1 一致。BoostCD（Sakota et al., 2025）在 SciERC 和 DocRED 上有结果，是最直接的对比对象。即使 setting 不完全相同（BoostCD 的 boosting 策略 vs. OntoCoDec 的确定性约束），同一数据集上的数字对比对审稿人判断边际贡献至关重要。\n\n---\n\n### [AGREE] R1-W2: 模型规模限于 7-8B，Abstract 声称 \"any autoregressive LM\" 未加限定\n\n与我的 W5 一致。Abstract（p1）说 \"applies to any autoregressive LM across four models (8B-70B)\"——但实际测试的模型参数量范围仅为 7B-8B（Qwen3-8B, Llama-3.1-8B, Mistral-7B, Llama-3.1-8B）。\"8B-70B\" 的表述来自何处不明——可能是计划中的实验但未执行？正文中应删除或修正此声称。\n\n---\n\n### [REBUT] R1-W3: 零样本 R-F1（0.08-8%）场景下违规率分析的实际意义\n\nR1 认为在极低 R-F1 下分析违规率实际意义存疑。我**不完全同意**。\n\n论文明确将零样本设定定位为 **diagnostic**（§5, p5: \"Zero-shot evaluation (§5.1-§5.3) isolates layer contributions as a diagnostic\"）。违规率分析的价值独立于任务性能：它揭示 LLM 在无任务特定训练时的**结构输出模式**——哪些类型的约束违规最频繁、违规与 schema 属性（κ̄）的关系等。这些 insight 对理解 LLM 的本体感知能力有独立价值，不因 R-F1 低而失效。\n\n类比：分析一个未经训练的代码 LLM 生成代码的 type errors 分布，即使代码无法编译运行，对理解模型的类型系统感知能力仍有诊断意义。\n\n**但我同意一点**：Table 1（p5）中 zero-shot 和 fine-tuned 结果并排呈现，可能使读者对零样本结果的实用性产生过高预期。建议在 Table 1 中增加视觉分隔（如水平线）或在 caption 中强调诊断性质。\n\n---\n\n### [AGREE] R1-W4: Entity registry 顺序依赖导致全局次优类型赋值\n\n这是一个有洞察力的观察。§3.3（p3）的 entity registry 按生成顺序增量填充，第一次出现的 entity 的类型赋值锁定所有后续引用。如果一个 entity 在第一个 triple 中被赋予次优类型（因为第一个 triple 的 relation 对该 entity type 的约束较宽松），后续更紧约束的 relation 就无法修正。\n\n§3.4（p4）提到的 TCR（Type Consistency Repair）是事后修复（beam search 或 post-hoc re-scoring），不是生成时的 exact enforcement——这进一步支持 R1-N2 的 \"exact\" 术语批评。\n\n补充证据：Table 10（Appendix D, p21）的 four-way ablation 显示 \"Semantic layer is the sole effective DR defense, providing 39-69% reduction\"——但这个 reduction 的上限可能受限于顺序依赖导致的次优赋值。如果 entity registry 能全局优化（如 ILP），DR reduction 可能更高。这是论文未讨论的理论上限。\n\n---\n\n### [AGREE] R1-W5: DocRED beam search 仅 50 文档子集\n\nTable 15（Appendix E, p24）确认 DocRED beam search 在 \"matched 50-document subsets\" 上评估。DocRED 有 96 个 relation types（vs. SciERC 的 7 个），50 文档可能无法覆盖足够多的 relation types 来验证 beam search 的普适效果。\n\nAppendix E 解释了原因：\"~300h due to extended generation under high-temperature sampling with complex schemas\"——这是合理的计算资源限制，但应在正文中标注，并讨论子集代表性（如覆盖的 relation type 比例）。\n\n---\n\n## Minor 回应\n\n- **Eq.(2) conjunction 是逐位 AND**：[AGREE] §4（p4）Eq. 2 的 M_final(t) = M_grammar(t) ∧ M_semantic(t) 确实是逐 token 的逐位 AND，应在正文中明确说明\"element-wise conjunction over the vocabulary\"。\n\n- **CF 列含义首次出现时未充分解释**：[AGREE] Table 1（p5）首次引入 CF 列时，caption 仅说 \"CF = cross-field consistency violations\"，但 CF 的具体含义（同一 entity 在不同 triple 中被赋予不同类型）需要回溯到 §2（p2）才能理解。建议在 Table 1 caption 中增加一句解释。\n\n- **Figure 1 (Appendix C, p20) x 轴 label 不直观**：[AGREE] x 轴是 κ × RV_baseline 的乘积，物理含义不直观。建议增加轴标签注释。\n\n- **Appendix G LoRA 3 epochs 是否充分**：[REBUT] 3 epochs 是 LoRA fine-tuning 的常见设定（Hu et al., 2022 原始论文使用 3-5 epochs）。Appendix G（p26-27）报告了 completion-only loss，且 SciERC 有 1,762 训练样本、DocRED 有 3,053 样本，3 epochs 下梯度更新分别为 333/573 steps（batch size 16, gradient accumulation 4），对于 LoRA rank=16 的小参数量是合理的。若 R1 怀疑 underfitting，应指出具体证据（如 training loss 未收敛）。\n\n- **§6 末尾一段更像 contribution 声称**：[AGREE] §6（p8）最后一段确实从 related work positioning 滑向了 contribution recapping，建议修改为更明确的 differentiation 表述。\n\n---\n\n## R1 Questions 评价\n\n**Q1（Pumping lemma + 有界 entity 数量）**：好问题。如果 schema 对 entity 数量设上限 k，则有效输出集变为有限语言（有限语言都是正则的，因此也是 CF 的）。Proposition 1 的 \"unbounded\" 前提至关重要——论文应讨论 bounded entity set 的退化情况。\n\n**Q2（Fallback 级联行为）**：最关键的问题，与 N2 直接相关。如上分析，级联确实可能发生。\n\n**Q3（S2 的 DR 高于 S1）**：有价值。Table 1 显示 S2 在某些配置下 DR 确实高于 S1。可能原因：two-pass 的第一次 pass 提取的 entity 集合不完全，导致第二次 pass 的 registry 缺失部分 entity，fallback 更频繁。\n\n**Q4（LoRA 超参数敏感性）**：合理关切，但优先级低于 N1-N3。\n\n**Q5（对称关系 κ 计算）**：技术上有趣。对称关系的 head/tail type set 相同，κ_head = κ_tail，但 §4 脚注 1（p4）已说明\"we evaluate on directed triples\"——因此对称关系的 κ 不存在 head/tail 不对称导致的低估问题。但 R1 可能在问更细微的点：对称关系是否使得有效类型对比非对称关系更多（因为 head 和 tail 可互换），从而 κ 低估了 constraint 的实际宽松度。这值得作者回应。\n\n---\n\n## 综合评价\n\nR1 的审稿在方法严谨性维度上非常深入。N2（\"exact\" vs fallback 矛盾 + 级联失败）和 W4（顺序依赖全局次优）是本轮审稿中最有技术深度的发现，两者联合起来构成了对论文核心声称的实质性挑战。N1 的方向正确但论证有误（混淆了 non-CF 与 undecidability）。N3 的范围应限定在 fine-tuning 行（20 docs）而非全部 WikiEvents 结果（246 docs）。\n\n两位 Reviewer 的共识问题：(1) 缺少与 BoostCD 的直接实验对比（R1-W1, R2-W1）；(2) 模型规模声称过宽（R1-W2, R2-W5）；(3) κ̄/形式化贡献的声称力度与证据不匹配（R1-N1, R2-N2）。\n",
    "reviewer_id": "2",
    "project": "schema_semantic_constrained_ie"
  }
}
```

</details>

---


### Tool result

_source line 973 · 2026-05-20T17:24:43.154942+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_01fc90ae186a4ed432770f7601995139:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3764
}
```

</details>

---


### Assistant

_source line 974 · 2026-05-20T17:24:51.576469+00:00_

已提交交叉回应。总结关键判断：

**与 R1 的共识**：
- N2（"exact enforcement" 术语矛盾 + fallback 级联）和 W4（entity registry 顺序依赖）是最有力的技术批评
- W1（缺 BoostCD 对比）、W2（模型规模声称过宽）两位 reviewer 独立提出

**对 R1 的反驳**：
- N1 的论证有方向性错误——将 non-context-freeness 混淆为 undecidability，要求的证明方法不匹配 Proposition 1 的实际声称
- W3（零样本违规率意义）——论文的 diagnostic 定位是合理的
- LoRA 3 epochs 在该参数量和数据规模下是标准设定

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2"
}
```

</details>

---


## Round 22

## Round 22

74 recorded events


### User

_source line 975 · 2026-05-20T18:37:09.036525+00:00_

[Round 1 审稿请求]:
你是 Reviewer 2，负责**新颖性 + 完整性 + 写作质量**。

## 论文信息
- 标题: OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints
- 论文路径: `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex`
- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.pdf`
- 目标 venue: EMNLP 2026（via ARR May cycle）
- Deadline: 2026-05-25

## Venue 要求
- 长文正文 ≤ 8 页，参考文献无限制
- Limitations 必须有，不计入页数
- ACL 模板，double-blind 审稿
- 附录不要求审稿人审查

## 你的审查侧重

### A. 新颖性与贡献定位
1. 与最接近工作（PICARD、IterGen、BoostCD、GoLLIE、GCD、DCCD）的技术区分是否清晰？
2. "Preventive forward-only masking" vs "corrective backtracking" 的 novelty 论证是否站得住脚？
3. 三个 contribution 是否都成立？是否有过度声称？
4. κ̄ 作为 "descriptive metric" 的定位是否合适？是否被过度包装为 contribution？
5. "formally compiles" 的声称——与 code generation 领域的 type-constrained decoding 有何本质区别？

### B. Related Work 覆盖与定位
1. 是否遗漏了重要的相关工作？特别是：
   - IE-specific constrained decoding（BoostCD、IterGen、EnriCo、DCCD）
   - Schema-aware IE（GoLLIE、KnowCoder、GUIDEX、InstructUIE）
   - Constrained decoding 对推理的影响（CRANE、HiddenCost、FormatTax）
2. 引用格式和完整性
3. 自引比例是否合理？

### C. 写作质量与清晰度
1. Abstract 信息密度是否合适？关键 message 是否清晰？
2. Introduction 的 motivation 是否 compelling？gap 论证是否充分？
3. §3 Method 描述是否清晰？Figure 1 是否 informative？
4. 实验结果叙述是否平衡？CF 代价是否在 Abstract/Introduction 中透明呈现？
5. 命名一致性：S1/S2 命名是否清晰？术语是否前后一致？
6. 模型规模声称（"any autoregressive LM" vs 实际仅 7-8B 主测试）是否准确？

### D. 格式合规
1. 正文是否 ≤ 8 页？（检查 Limitations 前的页数）
2. 匿名性：是否有泄露作者身份的信息？
3. 表格/图形是否清晰可读？字体是否过小？
4. 引用格式是否正确？
5. ARR Responsible NLP Research Checklist 是否存在？

### E. 输出格式
请按以下结构输出审稿意见：
1. **Summary** (2-3 句)
2. **Strengths** (逐条 S1, S2, ...)
3. **Weaknesses** (逐条 W1, W2, ... 区分 Must-Fix / Should-Fix / Minor)
4. **Questions** (需要作者澄清的)
5. **Missing References**
6. **Scores**: Novelty (1-5), Clarity (1-5), Overall (1-5, 按 EMNLP 2026 ARR 评分标准: 5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit), Confidence (1-5)

严格评审，不留情面。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 976 · 2026-05-20T18:37:16.704312+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
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

_source line 977 · 2026-05-20T18:37:16.755874+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 978 · 2026-05-20T18:37:21.730876+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria scoring"
  }
}
```

</details>

---


### Tool call

_source line 979 · 2026-05-20T18:37:23.233763+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.pdf",
  "project": "schema_semantic_constrained_ie",
  "pages": "1-13",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.pdf",
    "project": "schema_semantic_constrained_ie",
    "pages": "1-13",
    "dpi": "150"
  }
}
```

</details>

---


### Tool call

_source line 980 · 2026-05-20T18:37:23.785953+00:00_

called mcp__agent-ml-research__verify_references

<details open><summary>🔧 Tool call — mcp__agent-ml-research__verify_references</summary>

```json
{
  "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
  "project": "schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__verify_references",
  "tool_args": {
    "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
    "project": "schema_semantic_constrained_ie"
  }
}
```

</details>

---


### Tool call

_source line 981 · 2026-05-20T18:37:24.237644+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 982 · 2026-05-20T18:37:35.541124+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"}]

Based on the search results, here's what I found about ACL ARR 2026 reviewer guidelines, review form criteria, and scoring:

## Review Scoring System

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

## Review Form Criteria

The main criteria for Findings papers are soundness and reproducibility, while conference recommendations may also
…[truncated 1054 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 13810
}
```

</details>

---


### Tool result

_source line 983 · 2026-05-20T18:37:37.197495+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 464.8}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 525.2}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 491.5}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 489.5}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 539.6}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 518.9}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 477.4}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 565.9}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p9.png\", \"w
…[truncated 1191 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 13963
}
```

</details>

---


### Tool result

_source line 984 · 2026-05-20T18:38:15.329239+00:00_

{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 57, \"total_citations\": 94, \"unique_cited_keys\": 56, \"orphan_bib\": 1, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 47, \"online_not_found\": 2, \"online_mismatch\": 8}, \"cross_check\": {\"orphan_bib\": [\"schmidt2025grammar\"], \"missing_bib\": [], \"orphan_count\": 1, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"synchromesh_iclr2022\", \"type\": \"inproceedings\", \"title\": \"Synchromesh: Reliable Code Generation from Pre-trained Language Models\", \"authors\": \"Poesia, Gabriel and Polozov, Oleksandr and Le, Vu and Tiwari, Ashish and Soares,...\", \"year\": \"2022\", \"venue\": \"International Conference on Learning Representations\"}, {\"key\": \"mgd_neurips2023\", \"type\": \"inproceedings\", \"title\": \"Monitor-Guided Decoding of Code LMs with Static Analysis of Repository Context\", \"authors\": \"Agrawal, Lakshya A. and Kanade, Aditya and Goyal, Navin and Lahiri, Shuvendu K. ...\", \"year\": \"2023\", \"venue\": \"Advances in Neural Information Processing Systems\"}, {\"key\": \"pldi2025_type_constrained_codegen\", \"type\": \"article\", \"title\": \"Type-Constrained Code Generation with Language Models\", \"authors\": \"M\\\\\\\"undler, Niels and He, Jingxuan and Wang, Hao and Sen, Koushik and Song, Dawn ...\", \"year\": \"2025\", \"venue\": \"Proceedings of the ACM on Programming Languages\"}, {\"key\": \"roth_yih_2004\", \"type\": \"inproceedings\", \"title\": \"A Linear Programming Formulation for Global Inference in Natural Language Tasks\", \"authors\": \"Roth, Dan and Yih, Wen-tau\", \"year\": \"2004\", \"venue\": \"Proceedings of the Eighth Conference on Computational Natural Language Learning ...\"}, {\"key\": \"adakgc_emnlp2023\", \"type\": \"inproceedings\", \"title\": \"Schema-adaptable Knowledge Graph Construction\", \"authors\": \"Ye, Hongbin and Gui, Honghao and Xu, Xin and Chen, Xi and Chen, Huajun and Zhang...\", \"year\": \"2023\
…[truncated 47786 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__verify_references",
  "elapsed_ms": 51543
}
```

</details>

---


### Tool result

_source line 985 · 2026-05-20T18:38:15.329761+00:00_

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
12	\usepackage{multirow}
13	\usepackage[table]{xcolor}
14	\usepackage{amsmath}
15	\usepackage{amssymb}
16	\usepackage{amsthm}
17	\usepackage{enumitem}
18	\usepackage{pifont}
19	\usepackage{tikz}
20	\usetikzlibrary{arrows.meta,positioning,shapes.geometric,fit,backgrounds,calc}
21	\newcommand{\TBD}[1]{\textcolor{red}{#1}}
22	
23	\title{OntoCoDec: Type-Constrained Information Extraction\\via Compiled Schema Constraints}
24	
25	\author{Anonymous ACL submission}
26	
27	\begin{document}
28	\maketitle
29	
30	% === Abstract ===
31	\input{abstract}
32	
33	% === §1 Introduction ===
34	\input{section1_introduction_draft}
35	
36	% === §2 Background ===
37	\input{section2_background}
38	
39	% === §3 Method ===
40	\input{section3_method_draft}
41	
42	% === §4 Constraint Composition ===
43	\section{Constraint Composition}
44	\label{sec:composition}
45	\input{section4_composition_draft}
46	
47	% === §5 Experiments ===
48	\section{Experiments}
49	\label{sec:experiments}
50	
51	\input{section3_violation_landscape}
52	
53	\input{section5_scierc_draft}
54	\input{section5_docred_draft}
55	\input{section5_crossmodel_draft}
56	\input{section5_wikievents_draft}
57	\input{section5_runtime}
58	
59	% === §6 Related Work ===
60	\input{section6_related_work}
61	
62	% === §7 Discussion and Conclusion ===
63	\section{Discussion and Conclusion}
64	\label{sec:discussion}
65	\input{section7_conclusion_compressed}
66	
67	% === Limitations (ARR requirement: standalone section, does not count toward page limit) ===
68	\clearpage
69	\section*{Limitations}
70	
71	\paragraph{Constraint scope.}
72	CF impact is model-dependent: for well-calibrated models (Qwen, Llama), S1 introduces CF violations (up to 12.02\%) as a consequence of per-relation independent enforcement; 
…[truncated 5614 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 51092
}
```

</details>

---


### Tool call

_source line 986 · 2026-05-20T18:38:23.493256+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form: all scoring dimensions, their scales, and descriptions. Especially: Soundness, Excitement/Novelty, Overall Assessment scale, Confidence scale, and any other dimensions reviewers must score."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form: all scoring dimensions, their scales, and descriptions. Especially: Soundness, Excitement/Novelty, Overall Assessment scale, Confidence scale, and any other dimensions reviewers must score."
  }
}
```

</details>

---


### Tool call

_source line 987 · 2026-05-20T18:38:25.761895+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 988 · 2026-05-20T18:38:26.223852+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p2.png"
  }
}
```

</details>

---


### Tool result

_source line 989 · 2026-05-20T18:38:27.282462+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1520
}
```

</details>

---


### Tool result

_source line 990 · 2026-05-20T18:38:27.283742+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1059
}
```

</details>

---


### Tool call

_source line 991 · 2026-05-20T18:38:27.736618+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p3.png"
  }
}
```

</details>

---


### Tool call

_source line 992 · 2026-05-20T18:38:28.138564+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 993 · 2026-05-20T18:38:28.491641+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 755
}
```

</details>

---


### Tool call

_source line 994 · 2026-05-20T18:38:28.794878+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 995 · 2026-05-20T18:38:29.097648+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 959
}
```

</details>

---


### Tool result

_source line 996 · 2026-05-20T18:38:29.098191+00:00_

# ACL Rolling Review Form: Scoring Dimensions

## 1. **Reviewer Confidence**
Scale: 1-5
- 5 = "Positive that my evaluation is correct"
- 4 = Quite sure with unlikely missed details
- 3 = Pretty sure but chance of missing something
- 2 = Willing to defend but likely missed details
- 1 = Outside expertise area or incomprehensible paper

## 2. **Soundness**
Scale: 1-5 (with half-point increments)
- 5 = Most thorough study of its type
- 4 = Sufficient support for claims
- 3 = Adequate support for main claims
- 2 = Major claims lack sufficient support
- 1 = "Not yet sufficiently thorough to warrant publication"

## 3. **Excitement**
Scale: 1-5 (with half-point increments)
- 5 = Would recommend to others/attend presentation
- 4 = Would mention to others/make effort to attend
- 3 = Might mention points/attend if time permits
- 2 = Doesn't resonate but may interest others
- 1 = Lacks resonance; irrelevant to NLP community

## 4. **Overall Assessment**
Scale: 1-5 (with half-point increments)
- 5 = Award consideration candidate
- 4 = Conference acceptance recommended
- 3 = Findings track acceptance
- 2 = Substantial revisions needed
- 1 = "Not relevant to *ACL community"

## 5. **Reproducibility**
Scale: 1-5
- 5 = Results easily reproducible
- 4 = Mostly reproducible with minor variations
- 3 = Reproducible with difficulty
- 2 = Hard to reproduce; unavailable data
- 1 = Cannot reproduce

## 6. **Datasets & Software**
Scale: 1-5 each
- 5 = Enabling for other research
- 4 = Useful for others
- 3 = Potentially useful
- 2 = Documentary value only
- 1 = None released

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 5604
}
```

</details>

---


### Tool result

_source line 997 · 2026-05-20T18:38:29.551466+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 756
}
```

</details>

---


### Tool call

_source line 998 · 2026-05-20T18:38:29.602451+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p6.png"
  }
}
```

</details>

---


### Tool result

_source line 999 · 2026-05-20T18:38:30.256484+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 654
}
```

</details>

---


### Tool call

_source line 1000 · 2026-05-20T18:38:30.507888+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p7.png"
  }
}
```

</details>

---


### Tool call

_source line 1001 · 2026-05-20T18:38:31.062958+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 1002 · 2026-05-20T18:38:31.416977+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 909
}
```

</details>

---


### Tool result

_source line 1003 · 2026-05-20T18:38:31.669840+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 606
}
```

</details>

---


### Tool call

_source line 1004 · 2026-05-20T18:38:37.797482+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p9.png"
  }
}
```

</details>

---


### Tool result

_source line 1005 · 2026-05-20T18:38:38.302566+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 505
}
```

</details>

---


### Tool call

_source line 1006 · 2026-05-20T18:38:38.303076+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p10.png"
  }
}
```

</details>

---


### Tool call

_source line 1007 · 2026-05-20T18:38:38.808867+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p11.png"
  }
}
```

</details>

---


### Tool result

_source line 1008 · 2026-05-20T18:38:39.264736+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 961
}
```

</details>

---


### Tool call

_source line 1009 · 2026-05-20T18:38:39.265205+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 1010 · 2026-05-20T18:38:39.919900+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1111
}
```

</details>

---


### Tool call

_source line 1011 · 2026-05-20T18:38:39.920355+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p13.png"
  }
}
```

</details>

---


### Tool result

_source line 1012 · 2026-05-20T18:38:40.073779+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 808
}
```

</details>

---


### Tool result

_source line 1013 · 2026-05-20T18:38:40.626733+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 706
}
```

</details>

---


### Tool call

_source line 1014 · 2026-05-20T18:38:45.847920+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 1015 · 2026-05-20T18:38:46.300085+00:00_

1	\begin{abstract}
2	We present \textsc{OntoCoDec}, a framework that formally compiles Information Extraction (IE) ontologies into composable token-level decoding constraints via a decidability-guided architecture: a \emph{grammar layer} (context-free) guarantees JSON validity and vocabulary membership; a \emph{semantic layer} (prefix-decidable with state) enforces best-effort pair-based domain/range type constraints via a stateful entity registry, with grammar-first fallback when constraints conflict.
3	Without constraints, Large Language Model (LLM) based IE produces systematic domain/range (DR) violations that persist after fine-tuning, with rates characterized by \emph{constraint tightness} ($\bar{\kappa}$), a descriptive metric that correlates schema restrictiveness with enforcement outcomes and provides deployment guidance.
4	The two layers exhibit a formal enabling dependency (Proposition~1): neither achieves this reduction alone.
5	% exp_ids: w5_lora_scierc_constrained_eval, w5_qwen_docred_lora_constrained_eval, w5_llama_lora_scierc_constrained_eval, w5_llama_docred_lora_constrained_eval
6	Composed with Low-Rank Adaptation (LoRA), \textsc{OntoCoDec} reduces DR by 94--100\% with negligible R-F1 impact ($\pm$0.6\,pp), with modest cross-field (CF) costs resolvable via beam search.
7	The framework extends to event extraction without modification, applicable to both formal ontologies and empirically-derived type constraints.
8	\textsc{OntoCoDec} compiles constraints automatically at inference time, requires no constraint-specific training, and is validated primarily on 7--8B parameter models with preliminary 70B evaluation across three tokenizer families.
9	\end{abstract}
10	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1016 · 2026-05-20T18:38:46.300482+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section1_introduction_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section1_introduction_draft.tex"
  }
}
```

</details>

---
