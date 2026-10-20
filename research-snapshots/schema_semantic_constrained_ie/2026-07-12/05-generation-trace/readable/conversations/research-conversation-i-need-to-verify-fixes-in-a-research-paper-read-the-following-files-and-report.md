# Research conversation: I need to verify fixes in a research paper. Read the following files and report their FULL content (or at least the key 

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 34
- **Recorded user turns:** 1
- **Tool calls:** 13
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-ac3a68eece0ee652a.jsonl`
- **Structured JSON:** [`e2678d35e3cb62559578.json`](../../sessions/e2/e2678d35e3cb62559578.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

34 recorded events

### User

_source line 1 · 2026-05-23T11:40:07.021Z_

I need to verify fixes in a research paper. Read the following files and report their FULL content (or at least the key sections I specify):

1. `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section1_introduction_draft.tex` — Full file. Look for: C2 contribution (WikiEvents mentions?), C3 contribution (beam4 "eliminates all"?), F1 range claims ("40--46%" or "41--46%" or "41--47%"?), DR claims.

2. `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_runtime.tex` — Full file. Look for: beam4 "eliminates all" claim, DR claims.

3. `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion_compressed.tex` — Full file. Look for: TCR "18--92%" or updated claim, beam4 "eliminates all", F1 range.

4. `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract.tex` — Full file. Look for: F1 range, DR claims, WikiEvents mentions.

5. `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_discussion.tex` — Full file or first 100 lines. Look for: GoLLIE paragraph, complementarity narrative.

For each file, report the exact lines (with line numbers) containing: "WikiEvents", "GoLLIE", "eliminates all", "40--46", "41--46", "41--47", "F1", "DR", "0.21", "TCR", "18--92", "cross-field", any beam4 claims about violation elimination.

Be thorough — report every match, not just the first one.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "857bc242-0da2-40fe-8377-411f2acddc00",
  "agentId": "ac3a68eece0ee652a",
  "type": "user",
  "uuid": "fc4c3c1a-2a63-4873-91c5-3d00981b3666",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/reviewer_17ad4b4d",
  "sessionId": "9485bf07-277e-42ea-88c3-c883a57507b5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "zany-marinating-cherny"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-23T11:40:08.623Z_

I'll read all five files and search for the specific claims you mentioned. Let me start by reading them in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fc4c3c1a-2a63-4873-91c5-3d00981b3666",
  "isSidechain": true,
  "agentId": "ac3a68eece0ee652a",
  "requestId": "req_011CbKSJhYVR3CyKS5SsLQfp",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "5ec4e928-8fbe-41b2-be11-fb78db9355cb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/reviewer_17ad4b4d",
  "sessionId": "9485bf07-277e-42ea-88c3-c883a57507b5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "zany-marinating-cherny",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Sn1F8rEFrKLUjfmjYsCvaF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 21556,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 21556,
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

_source line 3 · 2026-05-23T11:40:08.996Z_

<details open><summary>🔧 Tool call — Read · `toolu_01TWJk3qqagsTAD2zACxZ5pX`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section1_introduction_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5ec4e928-8fbe-41b2-be11-fb78db9355cb",
  "isSidechain": true,
  "agentId": "ac3a68eece0ee652a",
  "requestId": "req_011CbKSJhYVR3CyKS5SsLQfp",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "42fc05d1-b933-4926-a751-06afa42c1734",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/reviewer_17ad4b4d",
  "sessionId": "9485bf07-277e-42ea-88c3-c883a57507b5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "zany-marinating-cherny",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Sn1F8rEFrKLUjfmjYsCvaF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 21556,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 21556,
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

_source line 4 · 2026-05-23T11:40:09.007Z_

<details><summary>↩ Tool result · `toolu_01TWJk3qqagsTAD2zACxZ5pX`</summary>

```text
1	% Section 1: Introduction (compressed, 669→~550 words)
2	
3	\section{Introduction}
4	\label{sec:introduction}
5	
6	Large language models are increasingly used for information extraction~\cite{li2023codeie,sainz2024gollie,wei2023zeroshot}, but when generating relation triples $(h, r, t)$, neither entity necessarily carries a type consistent with the ontology's domain/range constraints for $r$.
7	We call such outputs \emph{domain/range violations}: structurally valid triples that are ontologically invalid.
8	Violations persist across the capability spectrum: 15.4\% of triples on SciERC~\cite{luan2018scierc} and 18.5\% on DocRED~\cite{yao2019docred} under zero-shot decoding, and 0.5--2\% even after LoRA fine-tuning; rates follow an observed pattern consistent with schema restrictiveness (few valid type pairs per relation) rather than ontology or model scale.
9	At competitive quality (R-F1 40--46\%), even 1--2\% residual violations compound across thousands of documents into systematic knowledge graph corruption, making reliable constraint enforcement necessary.
10	
11	Existing approaches leave a fundamental gap.
12	Schema-informed prompting reduces violations by 62\% on average but is per-relation unreliable (violations for \textsc{Evaluate-for} actually \emph{increase} by 5.8\,pp).
13	Grammar-constrained decoding~\cite{dong2025xgrammar,willard2023outlines,beurer-kellner2023lmql} ensures syntactic well-formedness but cannot encode cross-field semantic constraints.
14	Post-hoc filtering discards up to 48\% of predictions including true positives (Appendix~\ref{app:cross-model-zs}).
15	Training-based approaches~\cite{sainz2024gollie,lu2022uie} internalize schema knowledge but provide only soft guidance without runtime enforcement.
16	
17	We propose \textbf{OntoCoDec}, a framework that translates IE ontologies into composable layers of decoding-time constraints.
18	A decidability analysis of IE type constraints (\S\ref{sec:decidability}) yields a two-layer architecture: the \emph{grammar layer} compiles ontology constraints into context-free grammars (JSON structure, vocabulary membership) via XGrammar; the \emph{semantic layer} interprets type constraints at runtime via dynamic logit masking over an entity registry, with a scale-dependent layer interaction: at 8B, the semantic layer achieves only 24\% independent DR reduction (near-complete when combined), while at 70B it reaches 84\% independently.
19	OntoCoDec compiles constraints automatically from IE ontologies, requires no constraint-specific training, and is applicable to autoregressive LMs with logits access; we validate on three English datasets (up to 96 relation types), three 8B-class models across three tokenizer families, with 70B-class validation (\S\ref{sec:70b-results}).
20	LoRA + greedy S1 reduces DR to near-zero: DR\,$\leq$\,0.21\% at R-F1 40--46\% ($\pm$0.3\,pp, $+$10\% latency); beam ($k{=}4$) eliminates all violation types on both RE datasets under fine-tuning (1.39$\times$ latency).
21	DR enforcement converts ontologically invalid violations to individually valid but type-inconsistent ones (CF\,$\leq$\,1.4\% fine-tuned); zero-shot DR drops 76--99\% on SciERC and 42--90\% on DocRED, with total violations decreasing $\sim$31\% (Appendix~\ref{app:cross-model-zs}).
22	
23	OntoCoDec is a constraint enforcement method, orthogonal and complementary to training-based schema-aware approaches such as GoLLIE~\cite{sainz2024gollie} and KnowCoder~\cite{knowcoder_acl2024}; it can be composed with any generative IE system to improve schema compliance without retraining.
24	
25	Our contributions:
26	\begin{enumerate}[leftmargin=*,itemsep=2pt]
27	    \item A two-layer constrained decoding framework grounded in the observation that domain/range type constraints require stateful enforcement beyond context-free grammars---grammar-only approaches face state spaces of $6^{17}$--$6^{19}$ for typical IE schemas (Proposition~1; \S\ref{sec:decidability}). Constraints compile automatically from IE ontologies, validated on schemas with up to 96 relation types.
28	    \item Systematic ablation across 3 model families (Qwen3-8B, Llama-3.1-8B, Mistral-7B) and 2 datasets (SciERC, DocRED) under both zero-shot and LoRA fine-tuned settings, demonstrating DR reduction to $\leq$0.21\% with R-F1 within $\pm$0.3\,pp; DR enforcement introduces CF as a correctable side effect (\S\ref{sec:scierc-results}).
29	    \item Preliminary single-family scale exploration on Llama-3.1-70B (AWQ INT4), revealing a scale-dependent layer interaction: the semantic layer alone achieves 84\% DR reduction at 70B vs.\ 24\% at 8B (\S\ref{sec:70b-results}). Beam $k{=}2$ is Pareto-optimal (R-F1 44.60, CF 0.11\%, 1.18$\times$ latency); $k{=}4$ achieves DR${=}$0\% with near-zero CF at 1.39$\times$.
30	\end{enumerate}
31	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "42fc05d1-b933-4926-a751-06afa42c1734",
  "isSidechain": true,
  "promptId": "857bc242-0da2-40fe-8377-411f2acddc00",
  "agentId": "ac3a68eece0ee652a",
  "type": "user",
  "uuid": "1e8371b4-32cc-4d5c-8eea-ac2eef37c430",
  "sourceToolAssistantUUID": "42fc05d1-b933-4926-a751-06afa42c1734",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/reviewer_17ad4b4d",
  "sessionId": "9485bf07-277e-42ea-88c3-c883a57507b5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "zany-marinating-cherny"
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-23T11:40:09.270Z_

<details open><summary>🔧 Tool call — Read · `toolu_018LDuwfpaPjQeDvWScM2Xpa`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_runtime.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1e8371b4-32cc-4d5c-8eea-ac2eef37c430",
  "isSidechain": true,
  "agentId": "ac3a68eece0ee652a",
  "requestId": "req_011CbKSJhYVR3CyKS5SsLQfp",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "6f7ff948-66a8-4fab-976d-211d678b632e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/reviewer_17ad4b4d",
  "sessionId": "9485bf07-277e-42ea-88c3-c883a57507b5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "zany-marinating-cherny",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Sn1F8rEFrKLUjfmjYsCvaF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 21556,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 21556,
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

_source line 6 · 2026-05-23T11:40:09.276Z_

<details><summary>↩ Tool result · `toolu_018LDuwfpaPjQeDvWScM2Xpa`</summary>

```text
1	% Runtime overhead (inline paragraph, no subsection header to save space)
2	
3	\paragraph{Runtime overhead.}
4	\label{sec:runtime}
5	S1 overhead is $+$13.1\% on SciERC, lower on DocRED due to amortization over longer sequences; under LoRA, $+$10.0\% with 37\% lower absolute latency.
6	Constraint compilation is one-time $<$0.5\,s; scaling benchmarks confirm constant overhead (2--3\%) up to 200 entity types and 1{,}000 relations (Appendix~\ref{app:scalability}).
7	
8	\paragraph{Beam search compatibility.}
9	\label{sec:beam-results}
10	% exp_id: d066_beam_sweep
11	With LoRA, beam search~\cite{anderson2017guided} eliminates all four violation types at 8B on both SciERC and DocRED; at 70B, beam $k{=}4$ achieves DR${=}$RV${=}$ET${=}$0\% with one residual CF on SciERC (Appendix~\ref{app:beam-search}).
12	A beam-width sweep ($k \in \{1,2,4,8\}$) on SciERC reveals $k{=}2$ as Pareto-optimal: R-F1 44.60 (highest), CF 0.11\%, at only 1.18$\times$ greedy S1 latency; $k{=}4$ achieves CF${=}$0\% but lower R-F1 (43.60) at 1.39$\times$ (Table~\ref{tab:beam-sweep}; latencies relative to greedy S1).
13	This yields three deployment tiers: greedy S1 ($+$10\% latency, DR${\leq}$0.21\%, CF${\leq}$1.4\%), beam $k{=}2$ (1.18$\times$, near-zero CF), and beam $k{=}4$ (1.39$\times$, all violations${\to}$0\%).
14	Per-beam memory overhead is $O(k \times |\text{entities}| \times |\text{types}|)$ for independent entity registry copies, negligible at typical document scales.
15	
16	% exp_ids: r16_70b_scierc_zs_s1, r16_70b_docred_zs_s1, 70b_lora_scierc, 70b_lora_docred_200
17	\paragraph{70B-class validation (single-family).}
18	\label{sec:70b-results}
19	The following results constitute a preliminary single-family scale exploration on Llama-3.1-70B-Instruct (AWQ INT4); cross-family verification (e.g., Qwen-72B) remains future work.
20	All 70B experiments use Llama-3.1-70B-Instruct under AWQ INT4 quantization; an 8B ablation confirms constraint enforcement is unaffected by quantization (Appendix~\ref{app:quantization}).
21	Zero-shot S1 eliminates DR on both datasets (SciERC 6.41\%\,$\to$\,0\%, DocRED 14.98\%\,$\to$\,0\%; R-F1 11--13).
22	% exp_ids: r16_70b_scierc_zs_ablation (grammar_only, semantic_only, full_s1)
23	A four-way ablation reveals scale-dependent layer interaction: semantic-only achieves 84\% DR reduction vs.\ 8B's 24\% (Table~\ref{tab:scierc-ablation}), though grammar remains necessary for RV elimination and CF control (semantic-only CF${=}$76).
24	% exp_ids: eval_70b_lora_scierc_s1_constrained, eval_70b_lora_docred_200_s1_constrained
25	LoRA confirms composability: DR\,$\to$\,0\% on both datasets (R-F1 44.53, 43.95; $|\Delta| \leq 0.20$\,pp; CF 0.18--1.33\%); cross-family generalization at 70B scale remains to be verified.
26	% exp_ids: eval_70b_lora_docred_200_beam4_s1
27	Beam ($k{=}4$) reduces DocRED parse failures (12.5\%\,$\to$\,0.5\%, R-F1 $+$4.19\,pp); SciERC controlled comparison isolates pure beam gain at $+$0.28\,pp (Appendix~\ref{app:70b-ablation}).
28	
29	% exp_ids: trie_qwen_ft_scierc, trie_qwen_zs_scierc, trie_llama_ft_scierc, trie_llama_zs_scierc
30	\paragraph{Comparison with grammar-constrained approaches.}
31	\label{sec:constrained-baselines}
32	Our grammar-only ablation (Table~\ref{tab:scierc-ablation}, row~2) implements the same constraints as GCD~\cite{geng2023gcd} and BoostCD~\cite{boostcd2025}; vLLM \texttt{guided\_json}~\cite{kwon2023vllm} confirms equivalence on Qwen3-8B (DR${=}$15.26\%; other models use the same backend; Appendix~\ref{app:gcd-comparison}).
33	The ${\sim}$15\% residual DR is the gap our semantic layer addresses (94\% total reduction); trie-only constraints without JSON enforcement yield 9--51\% parse failure (Appendix~\ref{app:trie-baseline}).
34	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6f7ff948-66a8-4fab-976d-211d678b632e",
  "isSidechain": true,
  "promptId": "857bc242-0da2-40fe-8377-411f2acddc00",
  "agentId": "ac3a68eece0ee652a",
  "type": "user",
  "uuid": "d3b8a0ff-88f8-4d3b-bf80-03748440f525",
  "sourceToolAssistantUUID": "6f7ff948-66a8-4fab-976d-211d678b632e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/reviewer_17ad4b4d",
  "sessionId": "9485bf07-277e-42ea-88c3-c883a57507b5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "zany-marinating-cherny"
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-23T11:40:09.482Z_

<details open><summary>🔧 Tool call — Read · `toolu_01YDYCX5L26du6eVjNv3hPT1`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion_compressed.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d3b8a0ff-88f8-4d3b-bf80-03748440f525",
  "isSidechain": true,
  "agentId": "ac3a68eece0ee652a",
  "requestId": "req_011CbKSJhYVR3CyKS5SsLQfp",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "4e747921-5e93-4ee0-81c3-7fce57eea0ad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/reviewer_17ad4b4d",
  "sessionId": "9485bf07-277e-42ea-88c3-c883a57507b5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "zany-marinating-cherny",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Sn1F8rEFrKLUjfmjYsCvaF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 21556,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 21556,
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

_source line 8 · 2026-05-23T11:40:09.486Z_

<details><summary>↩ Tool result · `toolu_01YDYCX5L26du6eVjNv3hPT1`</summary>

```text
1	% Section 7 — Discussion and Conclusion
2	
3	OntoCoDec compiles IE ontologies into composable token-level constraints, validated across 3 datasets, 3+ models, and 2 tasks.
4	Because IE type constraints exceed context-free expressiveness (Proposition~1), the semantic layer bridges the gap grammar-only enforcement cannot address (3\% vs.\ 94\% DR reduction at 8B), using constructive forward masking over a dynamic entity registry.
5	This scale-dependent interaction (\S\ref{sec:70b-results})---likely reflecting improved vocabulary calibration at larger scale, where 70B models assign higher probability to ontology-valid tokens (Appendix~\ref{app:causal-tracing})---suggests grammar-constrained decoding is necessary but increasingly insufficient as models improve; constraint enforcement is preserved under INT4 quantization (4$\times$ compression; Appendix~\ref{app:quantization}).
6	
7	\paragraph{DR$\leftrightarrow$CF trade-off.}
8	Greedy S1 reduces DR to $\leq$\,0.21\% but introduces CF (zero-shot $+$9.82\,pp, fine-tuned $+$1.18\,pp)---an architectural consequence of per-triple independent enforcement.
9	Among 248 zero-shot CF violations, 58.1\% involve hallucinated entities (absent from gold) and only 7.3\% are true cascade errors (\S\ref{sec:scierc-results}); fine-tuned CF drops to $\leq$1.4\%.
10	Beam $k{=}2$ reduces CF to 0.11\% at 1.18$\times$ latency (Pareto-optimal; recommended for zero-shot deployment); $k{=}4$ eliminates all violations at 8B (1 residual CF at 70B) at 1.39$\times$ (\S\ref{sec:beam-results}).
11	Net effect: total violations decrease ${\sim}$31\% in zero-shot and ${>}$90\% under fine-tuning; DR is irrecoverable while CF is amenable to post-hoc resolution (TCR; Appendix~\ref{app:tcr}).
12	
13	\paragraph{Complementarity and deployment.}
14	GoLLIE and KnowCoder internalize schema knowledge via training but lack runtime guarantees; LoRA + S1 shows the two are complementary (DR 1--2\%\,$\to$\,$\leq$0.21\%; neither alone achieves both high R-F1 and near-zero DR).
15	S2 (two-pass) exhibits scale-sensitive behavior: comparable to S1 at 8B but $-$8\,pp R-F1 at 70B, consistent with CRANE's~\cite{banerjee2025crane} finding that aggressive constraint enforcement can interfere with well-calibrated reasoning; we recommend S1 as the default configuration.
16	
17	\paragraph{Per-triple vs.\ global enforcement.}
18	Per-triple enforcement cannot coordinate cross-triple type assignments---the source of CF (Level~3; \S\ref{sec:decidability}); global entity-level type consensus exceeds online per-token masking.
19	Beam search and TCR approximate this; integrating consensus into decoding remains future work.
20	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4e747921-5e93-4ee0-81c3-7fce57eea0ad",
  "isSidechain": true,
  "promptId": "857bc242-0da2-40fe-8377-411f2acddc00",
  "agentId": "ac3a68eece0ee652a",
  "type": "user",
  "uuid": "653a8513-5123-4fe4-b330-77770db631cb",
  "sourceToolAssistantUUID": "4e747921-5e93-4ee0-81c3-7fce57eea0ad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/reviewer_17ad4b4d",
  "sessionId": "9485bf07-277e-42ea-88c3-c883a57507b5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "zany-marinating-cherny"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-23T11:40:09.718Z_

<details open><summary>🔧 Tool call — Read · `toolu_01FLtZ2EKeo8uo1pRjixnjoa`</summary>

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
  "parentUuid": "653a8513-5123-4fe4-b330-77770db631cb",
  "isSidechain": true,
  "agentId": "ac3a68eece0ee652a",
  "requestId": "req_011CbKSJhYVR3CyKS5SsLQfp",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f9f464bf-aed0-4083-a30f-2a1d847b4c21",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/reviewer_17ad4b4d",
  "sessionId": "9485bf07-277e-42ea-88c3-c883a57507b5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "zany-marinating-cherny",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Sn1F8rEFrKLUjfmjYsCvaF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 21556,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 21556,
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

_source line 10 · 2026-05-23T11:40:09.723Z_

<details><summary>↩ Tool result · `toolu_01FLtZ2EKeo8uo1pRjixnjoa`</summary>

```text
1	\begin{abstract}
2	Large language models for information extraction generate structurally valid but ontologically invalid triples---where entity types violate the ontology's domain/range constraints.
3	These violations persist across the capability spectrum and cannot be addressed by grammar-constrained decoding (which lacks cross-field type awareness) or post-hoc filtering (which discards valid predictions).
4	
5	We present \textsc{OntoCoDec}, a framework that compiles information extraction ontologies into composable token-level decoding constraints.
6	A decidability analysis shows that domain/range constraints exceed context-free expressiveness, yielding a two-layer architecture: a grammar layer enforces structural validity and vocabulary membership; a semantic layer enforces type constraints at runtime through stateful masking over a dynamic entity registry, with grammar-first fallback when constraints conflict.
7	
8	% exp_ids: w5_lora_scierc_constrained_eval, w5_qwen_docred_lora_constrained_eval, w5_llama_lora_scierc_constrained_eval, w5_llama_docred_lora_constrained_eval
9	Evaluated across three 8B-class models and two relation extraction datasets (up to 96 relations), OntoCoDec composed with LoRA fine-tuning reduces domain/range violations to near-zero ($\leq$\,0.21\%) at F1 40--46\%, but introduces cross-field type inconsistencies ($\leq$1.4\%) as the dominant residual---an architectural consequence of per-triple independent enforcement; net total violations decrease ${\sim}$31\% in zero-shot and ${>}$90\% under fine-tuning.
10	Beam search ($k{=}2$) reduces CF to 0.11\% at 1.18$\times$ latency; $k{=}4$ eliminates all violation types at 1.39$\times$.
11	In zero-shot settings, cross-field rates are higher (up to 12\%) but decrease with model calibration.
12	Zero-shot domain/range reductions span 76--99\% on SciERC and 42--90\% on DocRED; violation rates follow an observed pattern consistent with schema restrictiveness across our three evaluation schemas ($n{=}3$; insufficient for statistical inference), with a scale-dependent relationship between the two layers.
13	\end{abstract}
14	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f9f464bf-aed0-4083-a30f-2a1d847b4c21",
  "isSidechain": true,
  "promptId": "857bc242-0da2-40fe-8377-411f2acddc00",
  "agentId": "ac3a68eece0ee652a",
  "type": "user",
  "uuid": "09e5d3b6-d58d-493a-8dc7-a13b92e9433c",
  "sourceToolAssistantUUID": "f9f464bf-aed0-4083-a30f-2a1d847b4c21",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/reviewer_17ad4b4d",
  "sessionId": "9485bf07-277e-42ea-88c3-c883a57507b5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "zany-marinating-cherny"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-23T11:40:09.957Z_

<details open><summary>🔧 Tool call — Read · `toolu_01WFYUkT5QJffpfBCHVNyS1U`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_discussion.tex",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "09e5d3b6-d58d-493a-8dc7-a13b92e9433c",
  "isSidechain": true,
  "agentId": "ac3a68eece0ee652a",
  "requestId": "req_011CbKSJhYVR3CyKS5SsLQfp",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "efb61e57-782b-4e81-afdc-8856c7aff5c6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/reviewer_17ad4b4d",
  "sessionId": "9485bf07-277e-42ea-88c3-c883a57507b5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "zany-marinating-cherny",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Sn1F8rEFrKLUjfmjYsCvaF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 21556,
      "cache_read_input_tokens": 0,
      "output_tokens": 450,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 21556
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 450,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 21556,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 21556,
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

_source line 12 · 2026-05-23T11:40:09.967Z_

<details><summary>↩ Tool result · reported error · `toolu_01WFYUkT5QJffpfBCHVNyS1U`</summary>

```text
File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/reviewer_17ad4b4d.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "efb61e57-782b-4e81-afdc-8856c7aff5c6",
  "isSidechain": true,
  "promptId": "857bc242-0da2-40fe-8377-411f2acddc00",
  "agentId": "ac3a68eece0ee652a",
  "type": "user",
  "uuid": "539d4b83-2d5c-4413-9dd7-5c0100f6c2b6",
  "toolUseResult": "Error: File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/reviewer_17ad4b4d.",
  "sourceToolAssistantUUID": "efb61e57-782b-4e81-afdc-8856c7aff5c6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/reviewer_17ad4b4d",
  "sessionId": "9485bf07-277e-42ea-88c3-c883a57507b5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "zany-marinating-cherny"
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-23T11:40:12.406Z_

The fifth file (section6_discussion.tex) does not exist. Let me search for all .tex files in that directory to see what's available.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "539d4b83-2d5c-4413-9dd7-5c0100f6c2b6",
  "isSidechain": true,
  "agentId": "ac3a68eece0ee652a",
  "requestId": "req_011CbKSJvCkC3sP16aTBkP79",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "8ea13169-1a8c-4ae1-9038-67044a12d45a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/reviewer_17ad4b4d",
  "sessionId": "9485bf07-277e-42ea-88c3-c883a57507b5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "zany-marinating-cherny",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01RGhja9ir7tA72TDdxBEBMY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 5822,
      "cache_read_input_tokens": 21556,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5822,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
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

_source line 14 · 2026-05-23T11:40:12.880Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01KoVW8ioLrTS244ymMCq45s`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper -name \"*.tex\" -type f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8ea13169-1a8c-4ae1-9038-67044a12d45a",
  "isSidechain": true,
  "agentId": "ac3a68eece0ee652a",
  "requestId": "req_011CbKSJvCkC3sP16aTBkP79",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "c395fe5e-5194-4ebb-905a-427d5684d442",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/reviewer_17ad4b4d",
  "sessionId": "9485bf07-277e-42ea-88c3-c883a57507b5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "zany-marinating-cherny",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01RGhja9ir7tA72TDdxBEBMY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 5822,
      "cache_read_input_tokens": 21556,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5822,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
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

_source line 15 · 2026-05-23T11:40:13.141Z_

<details><summary>↩ Tool result · `toolu_01KoVW8ioLrTS244ymMCq45s`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_case_studies.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_runtime.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion_compressed.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_gollie_comparison.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/case_study_kappa_dr.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract_fd4b26.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract_d3264e.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_wikievents_draft.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/paper_tables_draft.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft_4796e8.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_power_analysis_523cc9.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_scalability.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_zs_crossmodel.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/discussion_paragraphs.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_llama_per_relation.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_prompt_sensitivity.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section4_composition_draft.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_violation_landscape.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_order_invariance.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_beam_search.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/p3_case_studies.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion_DEPRECATED.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_downstream_analysis.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_relwork_outline.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_relwork_additions.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_wikievents_pilot.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion_550cbf_DEPRECATED.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_kappa_case_study.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_tcr.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_method_draft.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_high_kappa_analysis.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_quantization.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_power_analysis.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_crossmodel_draft.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_prompts.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/checklist.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_reproducibility.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_doc_length.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_full_ft.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section2_background.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section1_introduction_draft.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_pumping_lemma.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/p3_case_studies_861a0d.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft_9b84f1.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_70b_ablation.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/discussion_paragraphs_cf83d1.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/fig1_framework.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_sampling_table.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c395fe5e-5194-4ebb-905a-427d5684d442",
  "isSidechain": true,
  "promptId": "857bc242-0da2-40fe-8377-411f2acddc00",
  "agentId": "ac3a68eece0ee652a",
  "type": "user",
  "uuid": "9e715974-96ef-4258-94b2-9332c3709f69",
  "sourceToolAssistantUUID": "c395fe5e-5194-4ebb-905a-427d5684d442",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/reviewer_17ad4b4d",
  "sessionId": "9485bf07-277e-42ea-88c3-c883a57507b5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "zany-marinating-cherny"
}
```

</details>

---

### Assistant

_source line 16 · 2026-05-23T11:40:15.121Z_

The section6_discussion.tex doesn't exist. There is section6_related_work.tex and appendix_discussion.tex. Let me read the appendix_discussion.tex since you asked about GoLLIE and complementarity narrative.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9e715974-96ef-4258-94b2-9332c3709f69",
  "isSidechain": true,
  "agentId": "ac3a68eece0ee652a",
  "requestId": "req_011CbKSK9i6W4jbcUCByFd9C",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d472e837-ca82-498a-a4b0-6b95a3fe6569",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/reviewer_17ad4b4d",
  "sessionId": "9485bf07-277e-42ea-88c3-c883a57507b5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "zany-marinating-cherny",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01NRhHAjce5AgCbdwsvMQqYV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 2704,
      "cache_read_input_tokens": 27378,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2704,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
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

_source line 17 · 2026-05-23T11:40:15.558Z_

<details open><summary>🔧 Tool call — Read · `toolu_01ESTbotRuu1aW6LvTQPnETR`</summary>

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
  "parentUuid": "d472e837-ca82-498a-a4b0-6b95a3fe6569",
  "isSidechain": true,
  "agentId": "ac3a68eece0ee652a",
  "requestId": "req_011CbKSK9i6W4jbcUCByFd9C",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "2cd55f77-de77-4aab-b1d7-c5a028a0db84",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/reviewer_17ad4b4d",
  "sessionId": "9485bf07-277e-42ea-88c3-c883a57507b5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "zany-marinating-cherny",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01NRhHAjce5AgCbdwsvMQqYV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 2704,
      "cache_read_input_tokens": 27378,
      "output_tokens": 149,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2704
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 149,
          "cache_read_input_tokens": 27378,
          "cache_creation_input_tokens": 2704,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2704,
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

_source line 18 · 2026-05-23T11:40:15.869Z_

<details><summary>↩ Tool result · `toolu_01ESTbotRuu1aW6LvTQPnETR`</summary>

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
53	\begin{tabular}{@{}ll rrr@{}}
54	\toprule
55	\textbf{Model} & \textbf{Setting} & \textbf{Fallback Rate} & \textbf{DR} & \textbf{From FB} \\
56	\midrule
57	Qwen3-8B  & FT S1 & 0/2256 (0\%)    & 0  & N/A \\
58	Qwen3-8B  & ZS S1 & 16/3458 (0.46\%) & 16 & 100\% \\
59	Llama-3.1-8B & FT S1 & 1/2162 (0.05\%) & 1  & 100\% \\
60	Llama-3.1-8B & ZS S1 & 1/2630 (0.04\%) & 1  & 100\% \\
61	\bottomrule
62	\end{tabular}
63	\caption{Fallback causal tracing on SciERC (551 documents). Fallback Rate: type-bearing positions where $S(t) \cap G(t) = \emptyset$ triggers grammar-first fallback. DR: residual domain/range violations. From FB: fraction of DR violations occurring at fallback positions. All violations occur exclusively at tail\_type positions (range constraints are tighter than domain constraints).}
64	\label{tab:causal-tracing}
65	\end{table}
66	
67	When the semantic mask is active, $\text{DR}_{\text{independent}} = 0$: the type constraint processor structurally prevents domain/range violations.
68	All 18 residual DR violations across four configurations occur exclusively at fallback positions, confirming that grammar-first fallback is a necessary condition for residual DR.
69	Fine-tuning reduces fallback to near-zero ($\leq$0.05\%), effectively eliminating the sole source of residual violations.
70	All fallback events occur at tail\_type positions, where $|\operatorname{range}(r, \tau^h)|$ is smaller than $|\operatorname{dom}(r)|$, making the intersection $S(t) \cap G(t)$ more likely to be empty.
71	
72	%%% Enabling Dependency: Confound Analysis %%%
73	
74	\paragraph{Enabling Dependency: Confound Analysis.}
75	\label{app:enabling-confound}
76	
77	The scale-dependent layer interaction (\S\ref{sec:method}) shows that the semantic layer achieves only 24\% DR reduction without the grammar layer (Table~\ref{tab:scierc-ablation}).
78	A potential confound is that the semantic layer depends not only on grammar-enforced vocabulary membership but also on structural enforcement for positional awareness: the semantic layer identifies type-bearing positions by pattern-matching the decoded prefix against the JSON schema, which is reliable only when the grammar layer guarantees valid JSON structure.
79	Without grammar enforcement, malformed structure can cause the semantic layer to misidentify type-bearing positions, reducing effective coverage.
80	We quantify this via the semantic-only ablation (Table~\ref{tab:scierc-ablation}, row~3): CF rises from 0.08\% to 2.71\%, indicating that 2.63\,pp of additional violations trace to structural ambiguity.
81	However, the dominant enabling mechanism remains vocabulary membership: the semantic layer's domain/range lookup requires $r_j \in \mathcal{R}$, which only the grammar layer ensures; without it, OOV relation names produce null constraint lookups.
82	The confound reinforces rather than undermines this interaction: both vocabulary and structural contributions of the grammar layer are prerequisites for effective semantic enforcement.
83	
84	%%% CF-DR Trade-off Analysis %%%
85	% exp_ids: cf_fallback_ablation_scierc (CF fallback vs full_s1 baseline)
86	
87	\paragraph{CF-DR Trade-off Analysis.}
88	\label{app:cf-dr-tradeoff}
89	
90	CF violations are the most prominent residual limitation of OntoCoDec under zero-shot decoding (9.90\% on SciERC, up to 12.02\% on Llama DocRED).
91	We treat this honestly: per-relation independent enforcement cannot eliminate CF without trading it against DR.
92	Table~\ref{tab:cf-dr-tradeoff} reports a pilot ablation in which we replace the grammar-first fallback with a CF-priority fallback that forces the entity's registered type when it conflicts with $\sigma(r)$.
93	
94	\begin{table}[t]
95	\centering
96	\small
97	\begin{tabular}{@{}l rrrr@{}}
98	\toprule
99	\textbf{Configuration} & \textbf{DR\,(\%)} & \textbf{CF\,(\%)} & \textbf{DR+CF} & \textbf{$f_{\text{gf}}$\,(\%)} \\
100	\midrule
101	S1 (baseline) & 0.93 & 9.90 & 10.83 & --- \\
102	CF fallback        & 14.78 & 0.04 & 14.82 & 36.64 \\
103	\midrule
104	$\Delta$ & $+$13.85 & $-$9.86 & $+$3.99 & --- \\
105	\bottomrule
106	\end{tabular}
107	\caption{CF-DR trade-off pilot on SciERC (Qwen3-8B, 551 documents; \texttt{w1\_cf\_fallback\_scierc\_pilot}). CF fallback eliminates CF but re-routes violations to DR, increasing total violations (DR+CF) by 3.99\,pp. $f_{\text{gf}}$: token-level grammar-first fallback rate at type-bearing positions (includes continuation tokens of multi-token type names; first-token position fallback rate is 0.46\% for SciERC Qwen; \S\ref{sec:greedy-limitation}).}
108	\label{tab:cf-dr-tradeoff}
109	\end{table}
110	
111	The CF fallback variant nearly eliminates CF (9.90\%\,$\to$\,0.04\%, $-$9.86\,pp) but at the cost of a 15.9$\times$ increase in DR (0.93\%\,$\to$\,14.78\%, $+$13.85\,pp).
112	% exp_id: w1_cf_fallback_scierc_pilot: DR=0.1478, CF=0.0004, f_gf=0.3664
113	This is not a net improvement: total violations (DR+CF) rise from 10.83\% to 14.82\% ($+$3.99\,pp), so the change \emph{re-routes} violations rather than reducing them.
114	The mechanism is mechanical: each token position with conflicting masks must commit to one violation type; when the CF fallback forces the system to emit the entity's registered type even though it lies outside $\sigma(r)$, the resulting triple satisfies cross-entity consistency but violates domain/range.
115	The token-level grammar-first fallback is triggered at 36.64\% of type-bearing positions (0.46\% at first-token positions; \S\ref{sec:greedy-limitation}); this conflict is structural, not a tunable hyperparameter.
116	
117	We interpret this as a fundamental tension in composable constraint systems with \emph{per-relation independent} enforcement: enforcement priority can be allocated between DR and CF but cannot independently minimize both.
118	Within this design, the current S1 configuration sits near the Pareto frontier of the trade-off, achieving 0.93\% DR at the cost of 9.90\% CF.
119	The direction of the trade-off is consistent beyond SciERC/Qwen3-8B: across all six zero-shot configurations (3 models $\times$ 2 datasets), DR and CF are descriptively inversely associated, with no setting showing both high DR and high CF simultaneously (Table~\ref{tab:cross-model}); however, $n{=}6$ is insufficient for statistical inference on this correlation.
120	The pattern is a structural consequence of per-relation enforcement with grammar-first fallback, not a model- or dataset-specific artifact; we select SciERC/Qwen3-8B for detailed ablation because it exhibits the highest CF (9.90\%), making the trade-off most visible.
121	While the inverse association holds across all configurations, the absolute trade-off magnitude may differ in settings with higher baseline CF, such as Llama DocRED (CF = 12.02\%), where the larger CF headroom could yield proportionally larger shifts under alternative fallback priorities.
122	The CF residual is concentrated in schema ambiguity rather than enforcement failure: 63.3\% of CF violations on SciERC involve the catch-all \textsc{Generic} type (Table~\ref{tab:cf-distribution}), which competes with every content type depending on anaphoric vs.\ referential use, a distinction the per-slot decoder cannot resolve without document-level coreference.
123	
124	Two complementary paths can lower CF without re-routing it to DR.
125	(i)~\emph{Reduce the baseline conflict rate.} Composing OntoCoDec with LoRA fine-tuning on SciERC reduces CF by 88\% relative to the zero-shot setting (9.90\%\,$\to$\,1.18\%; Table~\ref{tab:composability}), because the fine-tuned model's per-slot type predictions agree more often with the entity registry, so the per-relation mask and the registry intersect more frequently.
126	% exp_id: w5_lora_scierc_constrained_eval: CF=0.0118
127	The remaining 1.18\% still traces to \textsc{Generic}$\leftrightarrow$X schema ambiguity, so this path is empirically validated on one dataset and one fine-tuning method but does not generalize without further evidence.
128	(ii)~\emph{Replace per-relation enforcement with global entity-level type consensus during decoding.} This is outside the scope of OntoCoDec's forward-only autoregressive design and is left to future work.
129	
130	%%% Dual-Factor Quantitative Analysis %%%
131	% exp_ids: phase2_scierc_full_s1, phase2_docred_full_s1,
132	%          llama_scierc_full_s1, llama_docred_full_s1
133	
134	\paragraph{Dual-Factor Quantitative Analysis.}
135	\label{app:dual-factor}
136	
137	Figure~\ref{fig:dual-factor-scatter} plots residual DR against the product $\bar{\kappa} \times \text{RV}_{\text{baseline}}$ for model$\times$dataset configurations.
138	For \emph{calibrated} models (Qwen3-8B, Llama-3.1-8B; unconstrained ET${<}$3\% on both datasets), a linear fit yields $y = 0.366x - 0.138$ with $R^2 = 0.886$ ($n{=}4$, $F(1,2) = 15.54$, $p \approx 0.058$); with only four data points (df $= 2$) and $p > 0.05$, this constitutes a descriptive characterization rather than a confirmatory statistical test.
139	The strong fit supports the dual-factor pattern from \S\ref{sec:composition}: residual DR is governed by the product of schema tightness and baseline violation rate.
140	Mistral-7B (unconstrained ET${=}$7.58\% on DocRED) deviates from this pattern: its residual DR on DocRED (33.21\%) substantially exceeds the linear prediction. When model calibration is insufficient (ET${>}$5\% on either dataset), residual DR is dominated by entity misclassification rather than constraint-search failure.
141	This motivates a principled exclusion criterion: models with unconstrained ET${>}$5\% on either dataset fall outside the regime where the tightness$\times$RV product is the primary DR driver.
142	The two DocRED points (high $\bar{\kappa}{=}0.842$) separate cleanly from the two SciERC points (low $\bar{\kappa}{=}0.333$), and within each dataset the model with higher baseline RV shows higher residual DR.
143	
144	\begin{figure}[t]
145	\centering
146	\includegraphics[width=0.75\columnwidth]{figures/dual_factor_scatter.pdf}
147	\caption{Residual DR vs.\ Schema Restrictiveness $\times$ Baseline Violation Rate ($\bar{\kappa} \times \text{RV}_{\text{baseline}}$) across four model$\times$dataset configurations ($n{=}3$ schemas; descriptive only).
148	Linear fit (calibrated models): $y = 0.366x - 0.138$, $R^2 = 0.886$, $p{=}0.058$ ($n{=}4$, df${=}2$; not significant); Mistral deviates due to entity misclassification.}
149	\label{fig:dual-factor-scatter}
150	\end{figure}
151	
152	%%% Dataset-Dependent F1 Impact (moved from §7) %%%
153	% exp_ids: d012_bootstrap_ci (DocRED +0.50pp p<0.001, SciERC +0.13pp p=0.58),
154	%          phase0_docred_unconstrained (RV=29.66%), phase0_scierc_unconstrained (RV=1.39%)
155	
156	\paragraph{Dataset-Dependent F1 Impact.}
157	The divergence in F1 significance between DocRED ($+$0.50\,pp, $p < 0.001$) and SciERC ($+$0.13\,pp, $p = 0.58$) traces to a single mechanism: grammar-layer elimination of out-of-vocabulary relation names.
158	DocRED's baseline RV of 29.66\% produces 5{,}189 OOV predictions counted as false positives; eliminating them yields a significant precision gain.
159	SciERC's baseline RV is only 1.39\% (24 OOV predictions), too few to produce a detectable F1 effect.
160	Llama-3.1-8B's lower baseline RV (16.03\%) yields a smaller but directionally consistent improvement ($+$0.29\,pp vs.\ $+$0.50\,pp); F1 gain magnitude is proportional to baseline OOV rate.
161	% exp_ids: phase0_docred_unconstrained, phase0_scierc_unconstrained
162	% exp_ids: llama_docred_unconstrained (RV=16.03%), llama_docred_full_s1 (R-F1 delta=+0.29pp)
163	
164	%%% Bootstrap CIs and Effect Sizes %%%
165	% exp_ids: bootstrap_ci_ft_composability, r12_table2_bootstrap_ci
166	
167	\paragraph{Bootstrap Confidence Intervals and Effect Sizes.}
168	\label{app:bootstrap-effect-sizes}
169	
170	Table~\ref{tab:bootstrap-effect-sizes} reports per-configuration bootstrap CIs and Cohen's $d$ effect sizes (10{,}000 iterations, document-level resampling, seed=42) for the fine-tuning composability results (Table~\ref{tab:composability}).
171	After Bonferroni correction for $k{=}4$ comparisons ($\alpha_{\text{adj}}{=}0.0125$), no R-F1 difference reaches significance; all R-F1 effect sizes are negligible to small ($|d| \leq 0.37$; Cohen, 1988).
172	Per-configuration corrected $p$-values: Qwen3-8B/SciERC $p_B{=}1.00$, Qwen3-8B/DocRED $p_B{=}0.224$, Llama-3.1-8B/SciERC $p_B{=}1.00$, Llama-3.1-8B/DocRED $p_B{=}1.00$.
173	Constraint enforcement thus preserves extraction quality while achieving large, highly significant reductions in domain-range violations ($|d| \geq 3.0$, all $p_{\text{Bonf}} < 0.005$).
174	
175	\begin{table}[t]
176	\centering
177	\small
178	\setlength{\tabcolsep}{3pt}
179	\begin{tabular}{@{}ll rrrr@{}}
180	\toprule
181	\textbf{Model} & \textbf{Dataset} & $\Delta$\textbf{(pp)} & \textbf{95\% CI} & $p$ & $d$ \\
182	\midrule
183	\multicolumn{6}{@{}l}{\textbf{R-F1 difference (S1 $-$ unconstrained):}} \\
184	Qwen3-8B & SciERC & $-$0.10 & [$-$0.30, 0.00] & .726 & $-$0.05 \\
185	Qwen3-8B & DocRED & $-$0.31 & [$-$0.69, $+$0.01] & .056 & $-$0.37 \\
186	Llama-3.1-8B & SciERC & $+$0.02 & [0.00, $+$0.07] & .736 & $+$0.01 \\
187	Llama-3.1-8B & DocRED & $+$0.06 & [$-$0.11, $+$0.25] & .535 & $+$0.07 \\
188	\midrule
189	\multicolumn{6}{@{}l}{\textbf{DR\% reduction:}} \\
190	Qwen3-8B & SciERC & $-$1.95 & [$-$2.87, $-$1.11] & $<$.001 & $-$6.15 \\
191	Qwen3-8B & DocRED & $-$0.75 & [$-$1.07, $-$0.48] & $<$.001 & $-$7.00 \\
192	Llama-3.1-8B & SciERC & $-$1.02 & [$-$1.98, $-$0.29] & $<$.001 & $-$3.17 \\
193	Llama-3.1-8B & DocRED & $-$0.29 & [$-$0.53, $-$0.10] & $<$.001 & $-$3.02 \\
194	\bottomrule
195	\end{tabular}
196	\caption{Bootstrap CIs and Cohen's $d$ for Table~\ref{tab:composability} (10{,}000 iterations, document-level resampling, seed=42).
197	$d$: Cohen's $d$ from pooled bootstrap SD.
198	Top: R-F1 (S1 $-$ unconstrained); no comparison significant after Bonferroni correction ($k{=}4$, $\alpha_{\text{adj}}{=}0.0125$); $|d| \leq 0.37$ (negligible--small).
199	Bottom: DR\% reduction; all $p_{\text{Bonf}} < 0.005$, $|d| \geq 3.0$ (large).}
200	\label{tab:bootstrap-effect-sizes}
201	\end{table}
202	
203	%%% Paragraph 1: Low F1 Practical Significance %%%
204	% exp_ids: phase2_scierc_full_s1 (R-F1=8.36%), phase2_docred_full_s1 (R-F1=8.23%),
205	%          phase0_scierc_unconstrained (DR=15.37%), phase2_docred_unconstrained (DR=18.46%)
206	
207	\paragraph{Practical Significance of Zero-Shot F1.}
208	Our reported relation F1 of approximately 8\% on both SciERC and DocRED reflects the inherent difficulty of zero-shot closed IE, where the model receives no task-specific training examples.
209	For reference, supervised state-of-the-art systems on SciERC achieve approximately 49--53\% relation F1 with full training data~\citep{zhong2021frustratingly,ye2022packed}.
210	Constraint enforcement operates largely independently of the extraction model's intrinsic capability: it restricts the output space to ontologically valid triples regardless of the underlying model's accuracy.
211	Even after LoRA fine-tuning, residual DR of 1--2\% persists on tight-constraint relations (Table~\ref{tab:composability}); constraints remain necessary at deployment-grade quality.
212	% exp_ids: w5_lora_scierc_unconstrained_eval, w5_llama_lora_scierc_unconstrained_eval
213	In our evaluation, F1 serves as a \emph{control variable} verifying that constraint enforcement does not degrade extraction quality, not as an optimization target.
214	The contribution of this work is the constraint enforcement method itself; the zero-shot setting stress-tests constraint robustness under maximum model uncertainty, while composability with fine-tuning (\S\ref{sec:composability}) validates practical deployment value.
215	
216	%%% Paragraph 4: Decoding-Time vs. Post-Hoc Enforcement %%%
217	% exp_ids: posthoc_filtering_baseline, phase2_scierc_full_s1 (R-F1=8.36%),
218	%          phase2_docred_full_s1 (R-F1=8.23%, ET=0%)
219	
220	\paragraph{Decoding-Time vs.\ Post-Hoc Enforcement.}
221	Post-hoc filtering (generating triples without constraints, then removing schema-violating predictions) yields higher precision and consequently higher F1 than OntoCoDec on both datasets (SciERC 8.63 vs.\ 8.36; DocRED 9.61 vs.\ 8.23).
222	% posthoc: SciERC F1=8.63, DocRED F1=9.61; OntoCoDec: SciERC R-F1=8.36, DocRED R-F1=8.23
223	However, this precision gain comes at substantial cost.
224	On DocRED, post-hoc filtering discards 48.1\% of all predicted triples, including 127 true positives (11.2\% of correct predictions); recall drops from 9.46\% to 8.40\%.
225	% posthoc_docred: rejection=48.1%, tp_lost=127/1137, R: 9.46→8.40
226	Entity type violations remain unresolved (ET\,=\,2.47\% vs.\ OntoCoDec's 0\%), as filtering targets only domain/range and vocabulary violations.
227	% posthoc_docred: ET_residual=2.47%; phase2_docred_full_s1: ET=0%
228	OntoCoDec's decoding-time approach avoids this information loss by guiding generation toward compliant outputs rather than discarding non-compliant ones, preserving both recall and entity type validity.
229	The two strategies are complementary: post-hoc filtering can serve as an additional safety net for residual violations that decoding-time enforcement does not fully resolve.
230	
231	%%% CF Violation Distribution %%%
232	% exp_ids: phase2_scierc_full_s1 (CF=245), llama_scierc_full_s1 (CF=162),
233	%          phase2_docred_full_s1 (CF=2670), llama_docred_full_s1 (CF=3824)
234	
235	\paragraph{Cross-Field Violation Distribution.}
236	\label{app:cf-distribution}
237	
238	Table~\ref{tab:cf-distribution} reports the complete distribution of conflicting-type pairs for SciERC zero-shot S1 (248 CF violations across 245 unique entity-document pairs; no mention triggered $\geq$3 types).
239	Conflicts involving the \textsc{Generic} type account for 63.3\% (155/245) of all violations.
240	\textsc{Generic} is SciERC's anaphoric/placeholder label (``this approach'', ``the method''), which competes with every content type depending on whether the mention is used anaphorically or referentially, a distinction the per-slot constrained decoder cannot resolve without document-level coreference.
241	
242	The pattern generalizes across models and datasets: on Llama-3.1-8B SciERC, \textsc{Generic}$\leftrightarrow$\textsc{OtherScientificTerm} remains the top pair (53/162, 32.7\%); on DocRED, the analogous catch-all type \textsc{MISC} drives 76.6\% of Qwen's CF violations.
243	Under unconstrained decoding, CF rates collapse to $\leq$1\% on both datasets; CF violations are a side-effect of per-slot type commitment rather than a model deficiency.
244	
245	\begin{table}[t]
246	\centering
247	\small
248	\begin{tabular}{@{}lr r@{}}
249	\toprule
250	\textbf{Conflicting Type Pair} & \textbf{Count} & \textbf{\%} \\
251	\midrule
252	Generic $\leftrightarrow$ OtherScientificTerm & 85 & 34.7 \\
253	Generic $\leftrightarrow$ Material & 35 & 14.3 \\
254	Generic $\leftrightarrow$ Metric & 30 & 12.2 \\
255	Method $\leftrightarrow$ Task & 20 & 8.2 \\
256	Material $\leftrightarrow$ Method & 17 & 6.9 \\
257	OtherScientificTerm $\leftrightarrow$ Task & 12 & 4.9 \\
258	\midrule
259	10 further pairs (each $\leq$3.3\%) & 46 & 18.8 \\
260	\midrule
261	\textbf{Total} & \textbf{245} & 100.0 \\
262	\bottomrule
263	\end{tabular}
264	\caption{CF violation distribution on SciERC zero-shot S1 (Qwen3-8B, 551 documents).
265	All 245 unique entity-document pairs involve pairwise conflicts.
266	Conflicts involving \textsc{Generic} account for 63.3\%.}
267	\label{tab:cf-distribution}
268	\end{table}
269	
270	%%% Cascade Error Analysis %%%
271	% exp_ids: phase2_scierc_full_s1 (ZS: CF=248), w5_lora_scierc_full_s1_eval (FT: CF=22)
272	
273	\paragraph{Cascade Error Analysis.}
274	\label{app:cascade-analysis}
275	
276	Table~\ref{tab:cascade-breakdown} decomposes zero-shot CF violations by source mechanism.
277	The dominant source is hallucinated entities (58.1\%): the model generates entity names absent from the input document, and the entity registry assigns a type based on the first occurrence that may conflict with a subsequent valid entity sharing the same surface form.
278	True cascade errors---where first-seen type registration for a \emph{real} entity locks an incorrect type that blocks a subsequent valid assignment---account for only 7.3\% (18/248).
279	Correct type locks (first-seen type is correct and prevents an incorrect subsequent assignment) are 2.5$\times$ more frequent (18.1\%, 45/248), indicating that the first-seen registration mechanism provides a net benefit for type consistency.
280	
281	Under fine-tuning (22 CF violations, 20 documents), cascade errors are completely eliminated (0/22): LoRA training calibrates entity typing sufficiently that first-seen registrations are consistently correct.
282	This confirms that cascade errors are a model calibration issue exposed by the constraint mechanism, not an inherent deficiency of first-seen registration.
283	
284	\begin{table}[h]
285	\centering
286	\small
287	\begin{tabular}{@{}l rr@{}}
288	\toprule
289	\textbf{CF Source Category} & \textbf{Count} & \textbf{\%} \\
290	\midrule
291	Hallucinated entity & 144 & 58.1 \\
292	Correct type lock & 45 & 18.1 \\
293	True cascade error & 18 & 7.3 \\
294	Other / ambiguous & 41 & 16.5 \\
295	\midrule
296	\textbf{Total} & \textbf{248} & 100.0 \\
297	\bottomrule
298	\end{tabular}
299	\caption{CF violation source breakdown on SciERC zero-shot S1 (Qwen3-8B, 551 documents; exp\_id: phase2\_scierc\_full\_s1).
300	``Hallucinated entity'': generated entity absent from input.
301	``True cascade error'': first-seen lock on incorrect type blocks valid subsequent assignment.
302	``Correct type lock'': first-seen type correct, prevents incorrect subsequent type.
303	Under fine-tuning, cascade errors are completely eliminated (0/22 CF violations; exp\_id: w5\_lora\_scierc\_full\_s1\_eval).}
304	\label{tab:cascade-breakdown}
305	\end{table}
306	
307	%%% Per-Relation DR Elimination under Fine-Tuning %%%
308	% exp_ids: lora_scierc_unconstrained, lora_scierc_full_s1
309	
310	\paragraph{Per-Relation DR Elimination under Fine-Tuning.}
311	\label{app:lora-per-relation}
312	
313	Table~\ref{tab:lora-per-relation} presents the per-relation breakdown of DR elimination when OntoCoDec is composed with LoRA fine-tuning on SciERC.
314	Fine-tuning alone eliminates DR on four of seven relations but leaves non-zero violations on the three tightest-constraint relations: \textsc{Evaluate-for} ($\kappa{=}0.361$, 13.13\%), \textsc{Part-of} ($\kappa{=}0.417$, 5.77\%), and \textsc{Compare} ($\kappa{=}0.528$, 5.00\%).
315	Adding OntoCoDec constraints eliminates all remaining violations across all relations.
316	One \textsc{Evaluate-for} triple (99\,$\to$\,98) is redirected to \textsc{Used-for} (634\,$\to$\,635) by token-level masking: the head entity's registered type falls outside \textsc{Evaluate-for}'s domain, and the semantic mask steers generation to the nearest valid relation.
317	
318	\begin{table}[t]
319	\centering
320	\small
321	\begin{tabular}{@{}l r rr rr@{}}
322	\toprule
323	& & \multicolumn{2}{c}{\textbf{LoRA Unconstr.}} & \multicolumn{2}{c}{\textbf{LoRA + S1}} \\
324	\cmidrule(lr){3-4} \cmidrule(l){5-6}
325	\textbf{Relation} & $\kappa$ & DR\,(\%) & $n$ & DR\,(\%) & $n$ \\
326	\midrule
327	Evaluate-for & 0.361 & 13.13 & 99 & \textbf{0} & 98 \\
328	Part-of      & 0.417 & 5.77  & 52 & \textbf{0} & 52 \\
329	Compare      & 0.528 & 5.00  & 40 & \textbf{0} & 40 \\
330	Conjunction  & 0.306 & 1.31  & 153 & \textbf{0} & 153 \\
331	Feature-of   & 0.278 & 1.35  & 74 & \textbf{0} & 74 \\
332	Used-for     & 0.028 & 0.16  & 634 & \textbf{0} & 635 \\
333	Hyponym-of   & 0.417 & 0     & --- & \textbf{0} & --- \\
334	\bottomrule
335	\end{tabular}
336	\caption{Per-relation DR elimination on SciERC with LoRA fine-tuning (Qwen3-8B).
337	$\kappa$: constraint tightness; $n$: predicted triple count.
338	Used-for gains one triple from Evaluate-for redirection.}
339	\label{tab:lora-per-relation}
340	\end{table}
341	
342	%%% Fine-Tuned Four-Way Ablation %%%
343	% exp_ids: w5_lora_scierc_*, w5_llama_lora_scierc_*, w5_qwen_docred_*, w5_llama_docred_*, w8_*
344	
345	\paragraph{Fine-Tuned Four-Way Ablation.}
346	\label{app:ft-ablation}
347	
348	Table~\ref{tab:ft-ablation} presents the four-way constraint ablation on fine-tuned models across both datasets, isolating each layer's contribution when the base model has already internalized schema knowledge.
349	
350	\begin{table}[t]
351	\centering
352	\small
353	\setlength{\tabcolsep}{3pt}
354	\resizebox{\columnwidth}{!}{%
355	\begin{tabular}{@{}lll rrrrr rr@{}}
356	\toprule
357	\textbf{Dataset} & \textbf{Model} & \textbf{Mode} & \textbf{DR\,$\downarrow$} & \textbf{RV\,$\downarrow$} & \textbf{ET\,$\downarrow$} & \textbf{CF} & \textbf{PF} & \textbf{E-F1\,$\uparrow$} & \textbf{R-F1\,$\uparrow$} \\
358	\midrule
359	\multirow{8}{*}{SciERC}
360	  & \multirow{4}{*}{Qwen3-8B}
361	    & Unconstrained & 1.95 & 0.00 & 0.00 & 0.00 & 0.00 & 67.05 & 43.86 \\
362	  & & Grammar       & 1.90 & 0.00 & 0.00 & 0.00 & 0.00 & 67.05 & 43.86 \\
363	  & & Semantic      & 0.60 & 0.00 & 0.00 & 0.18 & 0.00 & 67.05 & 43.69 \\
364	  & & S1       & \textbf{0}    & 0.00 & 0.00 & 1.18 & 0.00 & 67.05 & 43.77 \\
365	  \cmidrule(l){2-10}
366	  & \multirow{4}{*}{Llama-3.1-8B}
367	    & Unconstrained & 1.11 & 0.00 & 0.00 & 0.00 & 0.00 & 67.76 & 45.45 \\
368	  & & Grammar       & 1.11 & 0.00 & 0.00 & 0.00 & 0.00 & 67.76 & 45.45 \\
369	  & & Semantic      & 0.65 & 0.00 & 0.00 & 0.10 & 0.00 & 67.76 & 45.47 \\
370	  & & S1       & \textbf{0.09} & 0.00 & 0.00 & 0.46 & 0.00 & 67.76 & 45.47 \\
371	\midrule
372	\multirow{8}{*}{DocRED}
373	  & \multirow{4}{*}{Qwen3-8B}
374	    & Unconstrained & 0.76 & 0.27 & 0.00 & 0.12 & 7.11 & 82.15 & 40.86 \\
375	  & & Grammar       & 0.61 & 0.00 & 0.00 & 0.11 & 7.01 & 82.19 & 40.85 \\
376	  & & Semantic      & 0.21 & 0.23 & 0.00 & 0.27 & 7.52 & 82.15 & 40.85 \\
377	  & & S1       & \textbf{0.01} & 0.00 & 0.00 & 0.41 & 8.52 & 81.43 & 40.56 \\
378	  \cmidrule(l){2-10}
379	  & \multirow{4}{*}{Llama-3.1-8B}
380	    & Unconstrained & 0.49 & 0.15 & 0.00 & 0.08 & 2.30 & 83.93 & 43.72 \\
381	  & & Grammar       & 0.51 & 0.00 & 0.00 & 0.12 & 2.30 & 84.04 & 43.72 \\
382	  & & Semantic      & 0.30 & 0.15 & 0.00 & 0.16 & 2.40 & 84.02 & 43.85 \\
383	  & & S1       & \textbf{0.21} & 0.00 & 0.00 & 0.21 & 2.51 & 83.94 & 43.78 \\
384	\bottomrule
385	\end{tabular}}%
386	\caption{Four-way constraint ablation on fine-tuned models (LoRA, 2 models $\times$ 2 datasets).
387	DR/RV/ET: violation rates (\%) over predicted relations; CF: over predicted entities; PF: parse failure rate (\%); F1 $\times$100.
388	Grammar layer is a no-op post-fine-tuning (DR change $<$0.2\,pp in all 4 settings; RV and ET already 0\% without constraints).
389	Semantic layer is the sole effective DR defense, providing 39--72\% reduction.
390	F1 cost is negligible: max $\Delta$R-F1 = $-$0.30\,pp (Qwen DocRED, full vs.\ unconstrained).}
391	\label{tab:ft-ablation}
392	\end{table}
393	
394	The grammar layer is effectively a no-op for fine-tuned models across all four settings: RV and ET are already 0\% without constraints, and grammar-only DR change is $<$0.2\,pp (4/4 settings).
395	The semantic layer is the sole effective DR defense under fine-tuning, independently reducing DR by 39--72\% across all settings (SciERC: Qwen $-$69\%, Llama $-$41\%; DocRED: Qwen $-$72\%, Llama $-$39\%).
396	Adding both layers achieves near-complete elimination (DR\,$\leq$\,0.21\% in all 4 settings): even after fine-tuning, the semantic layer's pair-based enforcement captures violations that training alone cannot eliminate, specifically on tight-constraint relations where the valid type-pair space is small.
397	F1 cost is negligible: the maximum R-F1 decrease across S1 vs.\ unconstrained is $-$0.30\,pp (Qwen DocRED).
398	
399	%%% DocRED Zero-Shot Ablation (moved from main text) %%%
400	% exp_ids: phase2_docred_unconstrained, phase2_docred_grammar_only,
401	%          phase2_docred_semantic_only, phase2_docred_full_s1
402	
403	\paragraph{DocRED Zero-Shot Ablation.}
404	\label{app:docred-zs-ablation}
405	
406	Table~\ref{tab:docred-ablation} presents the four-way constraint ablation on DocRED under zero-shot decoding, parallel to the SciERC ablation in Table~\ref{tab:scierc-ablation}.
407	
408	\begin{table}[t]
409	\centering
410	\small
411	\setlength{\tabcolsep}{3.6pt}
412	\resizebox{\columnwidth}{!}{%
413	\begin{tabular}{@{}l rrrrrr rr@{}}
414	\toprule
415	& \multicolumn{6}{c}{\textbf{Violation Rates (\%)}}
416	& \multicolumn{2}{c}{\textbf{F1}} \\
417	\cmidrule(lr){2-7} \cmidrule(l){8-9}
418	\textbf{Mode}
419	  & DR\,$\downarrow$ & $\Delta$DR
420	  & RV\,$\downarrow$ & ET\,$\downarrow$ & CF & Tot.\,$\downarrow$
421	  & Rel.\,$\uparrow$ & Ent.\,$\uparrow$ \\
422	\midrule
423	Unconstrained
424	  & 18.46 & ---
425	  & 29.66 & 2.48
426	  & 0.10  & 18.56
427	  & 7.74  & 58.15 \\
428	Grammar
429	  & 26.17 & $\uparrow$42\%
430	  & \textbf{0.03} & \textbf{0}
431	  & 0.07  & 26.24
432	  & \textbf{8.31}  & \textbf{59.38} \\
433	Semantic
434	  & 13.84 & $\downarrow$25\%
435	  & 29.87 & 4.22
436	  & 1.05  & 14.89
437	  & 7.70  & 57.81 \\
438	S1
439	  & \textbf{10.21} & $\downarrow$\textbf{45\%}
440	  & \textbf{0.03} & \textbf{0}
441	  & 2.57  & \textbf{12.78}
442	  & 8.23  & 59.37 \\
443	\bottomrule
444	\end{tabular}}%
445	\caption{Four-way ablation on DocRED (998 documents, Qwen3-8B, zero-shot).
446	$\Delta$DR: relative change vs.\ unconstrained.
447	Tot.\ = DR + CF (total type-violation burden).
448	Best per column in \textbf{bold} (CF excluded; Tot.\ included).
449	F1 $\times$100. Bootstrap significance: R-F1 $+$0.49\,pp ($p < 0.001$).
450	Grammar-only $\uparrow$DR: vocabulary enforcement makes OOV outputs evaluable, exposing latent violations (see \S\ref{sec:docred-results}).}
451	\label{tab:docred-ablation}
452	\end{table}
453	
454	%%% Residual DR Error Analysis (Fine-Tuned) %%%
455	% exp_ids: w5_qwen_docred_*, w5_llama_docred_*, w5_lora_scierc_*, w5_llama_lora_scierc_*
456	
457	\paragraph{Residual DR Error Analysis.}
458	\label{app:residual-dr-analysis}
459	
460	Across all fine-tuned settings (2 models $\times$ 2 datasets $\times$ S1), only 36 domain/range violations remain.
461	Manual inspection reveals four root causes:
462	
463	\begin{enumerate}[nosep,leftmargin=*]
464	\item \emph{Entity type errors} (39\%): the LLM assigns an incorrect entity type (e.g., labeling a geographic entity as \textsc{LOC} when the gold standard requires \textsc{MISC}), causing the semantic mask to permit a domain/range-incompatible relation.
465	\item \emph{Schema coverage gaps} (33\%): the frequency-based constraint table, constructed from training-set co-occurrence statistics, does not cover long-tail type pairs that are ontologically valid but rare. These violations are irreducible by decoding-time constraints alone.
466	\item \emph{Incorrect relation selection} (17\%): the model selects a semantically inappropriate relation whose domain/range constraints are incompatible with the correctly typed entities.
467	\item \emph{Direction reversal} (11\%): the model assigns the correct relation but inverts head/tail roles, placing entities in positions that violate the relation's asymmetric domain/range specification.
468	\end{enumerate}
469	
470	Two dataset-specific patterns emerge.
471	Outside Llama DocRED, all residual violations (3 of 36, spanning Llama SciERC and Qwen DocRED) trace exclusively to schema coverage gaps: the model's entity typing is accurate, and the constraint system has reached its theoretical ceiling given the frequency-based constraint table.
472	On DocRED, Llama-3.1-8B contributes 33 of 36 residual violations (92\%), with entity type errors as the dominant cause (14/33, 42\%).
473	This asymmetry reflects Llama's weaker fine-tuned entity typing on DocRED's larger ontology (96 relations, 6 entity types) compared to Qwen, which achieves near-zero residual.
474	The implication is twofold: (i)~the irreducible floor from schema gaps is small ($\sim$3 violations across 4 settings), so the constraint system operates near its theoretical optimum; (ii)~residual violations from entity typing errors are addressable through stronger base models or improved entity typing modules, without modifying the constraint architecture.
475	
476	%%% Post-Hoc Filtering Comparison (Extended) %%%
477	% exp_ids: posthoc_*_zs, posthoc_*_ft
478	
479	\paragraph{Post-Hoc Filtering: Extended Comparison.}
480	\label{app:posthoc-extended}
481	
482	Table~\ref{tab:posthoc-extended} presents the full comparison across all six zero-shot and four fine-tuned configurations.
483	
484	\begin{table}[t]
485	\centering
486	\small
487	\setlength{\tabcolsep}{3pt}
488	\resizebox{\columnwidth}{!}{%
489	\begin{tabular}{@{}lll rrr l@{}}
490	\toprule
491	\textbf{Setting} & \textbf{Model} & \textbf{Dataset} & \textbf{Reject\%} & \textbf{R-F1$_{\text{ph}}$} & \textbf{R-F1$_{\text{cd}}$} & \textbf{Winner} \\
492	\midrule
493	\multirow{6}{*}{ZS}
494	  & Qwen    & SciERC & 16.8 & 8.63  & 8.36  & ph \\
495	  & Llama   & SciERC & 13.9 & 2.71  & 2.54  & ph \\
496	  & Mistral & SciERC & 20.3 & 3.94  & 3.67  & ph \\
497	  & Qwen    & DocRED & 48.1 & 9.61  & 8.23  & ph \\
498	  & Llama   & DocRED & 42.2 & 7.44  & 6.27  & ph \\
499	  & Mistral & DocRED & \textbf{73.7} & 3.85  & \textbf{5.52} & cd \\
500	\midrule
501	\multirow{4}{*}{FT}
502	  & Qwen    & SciERC & 1.95 & 43.94 & 43.77 & ph \\
503	  & Llama   & SciERC & 1.11 & 45.23 & 45.47 & cd \\
504	  & Qwen    & DocRED & 1.03 & 41.11 & 40.79 & ph \\
505	  & Llama   & DocRED & 0.64 & 43.92 & 43.78 & cd \\
506	\bottomrule
507	\end{tabular}}%
508	\caption{Post-hoc filtering (ph) vs.\ constrained decoding (cd).
509	In zero-shot settings, post-hoc F1 is higher in 5/6 groups (precision-dominated), but constrained decoding preserves higher recall in all 6/6 groups.
510	At reject rate $>$70\% (Mistral DocRED), post-hoc F1 collapses below constrained.
511	Under fine-tuning, rejection rates drop to 0.6--2.0\% and the two strategies are equivalent ($\Delta \leq 0.55$\,pp; each wins two groups).
512	F1 $\times$100.}
513	\label{tab:posthoc-extended}
514	\end{table}
515	
516	The crossover point occurs when post-hoc rejection exceeds $\sim$70\%: Mistral DocRED rejects 73.7\% of predicted triples, discarding enough true positives that constrained decoding's recall advantage dominates ($+$1.67\,pp).
517	OntoCoDec's advantage thus scales with violation severity: precisely when constraints are most needed, post-hoc filtering is most destructive.
518	Under fine-tuning, both strategies converge because few violations remain to filter or constrain ($\Delta \leq 0.55$\,pp across all four FT groups, with each strategy winning two).
519	
520	%%% Zero-Shot Runtime Profiling %%%
521	
522	\paragraph{Zero-Shot Runtime Profiling.}
523	\label{app:runtime}
524	
525	On SciERC (Qwen3-8B, zero-shot greedy, NVIDIA RTX PRO 6000 Blackwell Server Edition), unconstrained inference averages 4.163\,s/doc and S1 constrained decoding averages 4.710\,s/doc ($+$13.1\% overhead).
526	On DocRED (same configuration), relative overhead is lower due to amortization: the fixed per-token constraint cost is spread over longer generation sequences.
527	XGrammar automaton compilation takes 0.044\,s; the full constraint pipeline (schema parsing, JSON Schema generation, grammar compilation) takes 0.33\,s on SciERC (Table~\ref{tab:scalability}), amortized to zero over the evaluation set.
528	
529	% exp_id: p8c_ft_scierc_latency — Reviewer Report #23 verified
530	\paragraph{Fine-Tuned Latency Profiling.}
531	\label{app:ft-latency}
532	Under LoRA fine-tuning (same hardware and dataset), unconstrained inference averages 2.612\,s/doc and S1 constrained decoding averages 2.873\,s/doc ($+$10.0\% overhead, $n{=}551$).
533	Fine-tuned models generate shorter, more structured outputs than zero-shot models (2.612\,s vs.\ 4.163\,s/doc unconstrained); absolute generation time drops by 37\%.
534	The relative overhead ($+$10.0\%) is slightly lower than zero-shot ($+$13.1\%), consistent with shorter sequences requiring fewer constraint checks per document.
535	
536	%%% Fuzzy Relation Matching %%%
537	
538	\paragraph{Relation Matching Protocol.}
539	\label{app:fuzzy-matching}
540	Relation F1 evaluation uses fuzzy normalization to handle model-specific formatting variants (e.g., underscores vs.\ spaces, abbreviations).
541	A predicted relation $r_p$ matches gold relation $r_g$ if: (1)~exact string match after case-insensitive normalization, or (2)~token overlap $>$80\% \emph{and} edit distance $\leq 2$.
542	This protocol affects primarily Mistral, which produces underscore-separated variants (e.g., ``head\_of\_government'' for ``head of government'').
543	On Mistral DocRED, fuzzy matching contributes 98 additional TPs ($+$0.84\,pp R-F1; strict R-F1\,=\,3.50\% vs.\ fuzzy 4.34\%).
544	For Qwen and Llama under grammar constraints, the grammar layer enforces exact relation names, making fuzzy matching irrelevant (0 additional matches).
545	All F1 figures in the main text use fuzzy normalization consistently across all models and conditions.
546	
547	%%% Per-Relation Violation Landscape %%%
548	
549	\paragraph{Per-Relation Violation Landscape.}
550	\label{app:per-relation-landscape}
551	
552	Table~\ref{tab:prompt_comparison} compares violation rates under unconstrained and schema-informed prompting.
553	Figure~\ref{fig:per_relation_dr} shows the per-relation DR distribution on SciERC.
554	
555	\begin{table}[t]
556	\centering
557	\small
558	\caption{Violation rates (\%) under unconstrained and schema-informed prompting (Qwen3-8B, zero-shot).}
559	\label{tab:prompt_comparison}
560	\resizebox{\columnwidth}{!}{%
561	\begin{tabular}{ll cccc}
562	\toprule
563	Dataset & Prompt & DR$\downarrow$ & RV$\downarrow$ & ET$\downarrow$ & CF$\downarrow$ \\
564	\midrule
565	\multirow{2}{*}{SciERC} & Unconstrained & 15.4 & 1.4 & 0.4 & 0.1 \\
566	 & Schema-informed & 5.8 & 0.3 & \textbf{0.0} & --- \\
567	\midrule
568	\multirow{2}{*}{DocRED} & Unconstrained & 18.5 & 29.7 & 2.5 & 0.1 \\
569	 & Schema-informed & 12.8 & 18.4 & 0.2 & 0.2 \\
570	\bottomrule
571	\end{tabular}}
572	\end{table}
573	
574	\begin{figure}[t]
575	\centering
576	\includegraphics[width=\columnwidth]{figures/fig2_per_relation_dr.pdf}
577	\caption{Per-relation DR violation rates on SciERC (Qwen3-8B, unconstrained). Rates correlate with constraint tightness $\kappa(r)$. Llama-3.1-8B shows similar per-relation patterns (Appendix~\ref{app:llama-per-relation}).}
578	\label{fig:per_relation_dr}
579	\end{figure}
580	
581	%%% WikiEvents Extended %%%
582	
583	\paragraph{WikiEvents Dataset Details.}
584	\label{app:wikievents}
585	WikiEvents~\cite{li2021document} is a document-level event argument extraction benchmark grounded in the DARPA KAIROS ontology.
586	It defines 56 event types, 80 argument roles, and 27 entity types, with 245 (event\_type, role)$\to$allowed\_entity\_types constraints.
587	The grammar layer targets EV (event vocabulary), RoV (role vocabulary), and ET; the semantic layer enforces AC (argument constraint) via role-conditioned masking, analogous to RE domain/range enforcement.
588	
589	\paragraph{Constraint Tightness in WikiEvents.}
590	\label{app:wikievents-kappa}
591	% Data source: artifacts/w1c_wikievents_kappa_results.md
592	WikiEvents role-level tightness (with $|\mathcal{E}|{=}27$) has mean $\bar{\kappa}{=}0.82$ and median 0.89; 84\% of roles have $\kappa \geq 0.80$ (4 or fewer valid entity types out of 27).
593	The tightness-violation pattern extends to event extraction: roles with $\kappa \geq 0.90$ exhibit the highest AC rate (50\%), compared to 21\% for medium-tightness ($0.80 \leq \kappa < 0.90$) and 30\% for loose ($\kappa < 0.80$) roles; this is consistent with the RE observation that constraint tightness correlates with violation frequency.
594	However, the correlation is modulated by entity type prototypicality: semantically intuitive roles (e.g., Transportation.Vehicle$\to$VEH) show 0\% AC despite $\kappa{=}0.963$, while roles that require rare KAIROS-specific types (e.g., Crime$\to$CRM, Sentence$\to$SEN) show near-100\% AC because LLMs default to common types (PER, ORG).
595	The loose group's elevated rate (30\%) is driven by high-frequency roles such as Attack.Target (126 args, 34\% AC, $\kappa{=}0.59$), where systematic model errors outweigh the permissive constraint space.
596	
597	%%% Lucky Violation Analysis %%%
598	% exp_ids: task_e_lucky_violation_analysis
599	
600	\paragraph{Lucky Violation Analysis.}
601	\label{app:lucky-violations}
602	Table~\ref{tab:lucky-violations} quantifies the recall cost of DR elimination.
603	A ``lucky violation'' is a constraint-removed triple that happens to match a gold label---an ontologically invalid prediction that is nonetheless correct.
604	Across four fine-tuned configurations, lucky violations average 0.49\% of gold triples (range 0.01--0.51\%), confirming that nearly all removed DR violations are false positives.
605	On Llama SciERC, all five lucky violations are recovered as legal type paths under constrained decoding (zero churn): the model finds an ontology-compliant route to the same prediction.
606	
607	\begin{table}[h]
608	\centering
609	\small
610	\resizebox{\columnwidth}{!}{%
611	\begin{tabular}{@{}llrrrr@{}}
612	\toprule
613	\textbf{Model} & \textbf{Dataset} & \textbf{DR (\%)} & \textbf{Lucky} & \textbf{$\Delta$Recall} & \textbf{Churn} \\
614	& & \textbf{unc$\to$con} & \textbf{(\% gold)} & \textbf{(pp)} & \textbf{(\%)} \\
615	\midrule
616	Qwen3-8B  & SciERC & 1.95$\to$0    & 4 (0.41\%) & $-$0.10 & 0.22 \\
617	Llama-8B  & SciERC & 1.11$\to$0.09 & 5 (0.51\%) & $\pm$0.00 & 0 \\
618	Qwen3-8B  & DocRED & 1.03$\to$0.01 & 1 (0.01\%) & $-$0.84 & 2.05 \\
619	Llama-8B  & DocRED & 0.64$\to$0.21 & 1 (0.01\%) & $-$0.10 & 0.86 \\
620	\midrule
621	\multicolumn{2}{@{}l}{\textit{Average}} & & \textit{0.49\%} & $-$0.26 & 0.78 \\
622	\bottomrule
623	\end{tabular}}
624	\caption{Lucky violation analysis across four LoRA fine-tuned configurations.
625	Lucky: count (and \% of gold triples) of constraint-removed violations matching gold labels.
626	$\Delta$Recall: recall change from unconstrained to constrained.
627	Churn: fraction of gold-matching triples whose predictions change (including recovery via legal type paths).}
628	\label{tab:lucky-violations}
629	\end{table}
630	
631	%%% Trie-Only Baseline %%%
632	% exp_ids: trie_qwen_ft_scierc, trie_qwen_zs_scierc, trie_llama_ft_scierc, trie_llama_zs_scierc
633	
634	\paragraph{Trie-Only Baseline (GCD-Equivalent).}
635	\label{app:trie-baseline}
636	Table~\ref{tab:trie-baseline} isolates the effect of vocabulary membership constraints without JSON structural enforcement.
637	The trie constrains entity type and relation tokens to schema-valid values (achieving ET${=}$0\%, RV${=}$0\% across all configurations), functionally equivalent to GCD's~\cite{geng2023gcd} constrained decoding.
638	However, without grammar-level JSON enforcement, models systematically omit entity type fields (83\% of triples) or produce malformed JSON (0--51\% parse failure), causing DR to rise to 15--96\%---far worse than unconstrained baselines.
639	The effect is most dramatic for Llama-8B LoRA: 50.8\% parse failure causes R-F1 to collapse from 45.47 (OntoCoDec S1) to 19.95, demonstrating that the grammar layer is not merely helpful but a structural prerequisite---vocabulary constraints require JSON scaffolding to reach the positions where they apply.
640	
641	\begin{table}[h]
642	\centering
643	\small
644	\resizebox{\columnwidth}{!}{%
645	\begin{tabular}{@{}ll rrrr rr@{}}
646	\toprule
647	\textbf{Model} & \textbf{Setting}
648	  & \textbf{ET\,$\downarrow$} & \textbf{RV\,$\downarrow$} & \textbf{DR\,$\downarrow$} & \textbf{CF}
649	  & \textbf{R-F1\,$\uparrow$} & \textbf{PF\,(\%)} \\
650	\midrule
651	\multirow{2}{*}{Qwen3-8B}
652	  & LoRA  & 0 & 0 & 95.5  & 0.09 & 41.16 & 9.1 \\
653	  & ZS    & 0 & 0 & 29.3  & 0    & 8.64  & 0 \\
654	\multirow{2}{*}{Llama-8B}
655	  & LoRA  & 0 & 0 & 15.2$^\dagger$  & 0    & 19.95 & 50.8 \\
656	  & ZS    & 0 & 0 & 84.4  & 0.36 & 2.90  & 0 \\
657	\midrule
658	\multicolumn{8}{@{}l}{\textit{Comparison with OntoCoDec S1:}} \\
659	\midrule
660	& & \multicolumn{2}{c}{\textbf{S1 DR\,(\%)}} & \textbf{Trie DR\,(\%)} & \multicolumn{2}{c}{\textbf{DR Gap (pp)}} & \\
661	\cmidrule(lr){3-4} \cmidrule(lr){5-5} \cmidrule(lr){6-7}
662	Qwen3-8B  & LoRA  & \multicolumn{2}{c}{0}    & 95.5  & \multicolumn{2}{c}{95.5}  & \\
663	Qwen3-8B  & ZS    & \multicolumn{2}{c}{0.93} & 29.3  & \multicolumn{2}{c}{28.4}  & \\
664	Llama-8B  & LoRA  & \multicolumn{2}{c}{0.09} & 15.2  & \multicolumn{2}{c}{15.1}  & \\
665	Llama-8B  & ZS    & \multicolumn{2}{c}{0.08} & 84.4  & \multicolumn{2}{c}{84.3}  & \\
666	\bottomrule
667	\end{tabular}}
668	\caption{Trie-only baseline (GCD-equivalent, vocabulary membership without JSON grammar) on SciERC.
669	Top: full trie-only metrics (ET/RV/DR/CF: violation rates \%; R-F1 $\times$100; PF: parse failure rate).
670	Trie achieves ET${=}$0\%, RV${=}$0\% but DR rises to 15--96\% because models omit type fields without structural enforcement.
671	Bottom: DR gap between OntoCoDec S1 and trie-only, quantifying the grammar layer's contribution.
672	$^\dagger$50.8\% parse failure rate.}
673	\label{tab:trie-baseline}
674	\end{table}
675	
676	%%% GCD/BoostCD Equivalence Comparison %%%
677	
678	\paragraph{Comparison with Grammar-Based Constrained Decoding.}
679	\label{app:gcd-comparison}
680	
681	Table~\ref{tab:gcd-comparison} summarizes the relationship between OntoCoDec's constraint layers and existing grammar-based constrained decoding methods.
682	
683	\begin{table}[h]
684	\centering
685	\small
686	\resizebox{\columnwidth}{!}{%
687	\begin{tabular}{@{}l l l l l l@{}}
688	\toprule
689	\textbf{Method} & \textbf{Constraint Type} & \textbf{Level} & \textbf{DR Red.} & \textbf{CF} & \textbf{State} \\
690	\midrule
691	GCD~\cite{geng2023gcd} & CFG (JSON schema) & Grammar & ${\sim}$3\% & N/A & Stateless \\
692	BoostCD~\cite{boostcd2025} & CFG + beam rerank & Grammar & ${\sim}$3\%$^\dagger$ & N/A & Stateless \\
693	Trie-Only (Tab.~\ref{tab:trie-baseline}) & Prefix trie & Vocab & 0\%$^\ddagger$ & N/A & Stateless \\
694	\midrule
695	vLLM \texttt{guided\_json}~\cite{kwon2023vllm} & JSON Schema & Grammar & ${\sim}$3\%$^\S$ & N/A & Stateless \\
696	\midrule
697	OntoCoDec Grammar & CFG (XGrammar) & Grammar & ${\sim}$3\% & N/A & Stateless \\
698	OntoCoDec S1 & CFG + type constr. & Gram.+Sem. & 94--100\% (FT) & ${\leq}$1.4\% (FT) & Entity reg. \\
699	\bottomrule
700	\end{tabular}}
701	\caption{Comparison with grammar-based constrained decoding methods.
702	$^\dagger$Equivalent mechanism; BoostCD adds beam-level reranking but the CFG enforcement is identical.
703	$^\ddagger$Vocabulary-only constraints without JSON structure cause DR to \emph{increase} (15--96\%; Table~\ref{tab:trie-baseline}).
704	$^\S$Experimentally verified: DR${=}$15.26\% vs.\ grammar-only 14.84\% ($\Delta{<}$0.5\,pp; Table~\ref{tab:vllm-verification}).
705	Grammar-only results are analytically equivalent to GCD/BoostCD (same CFG enforcement; \S\ref{sec:related_work}).}
706	\label{tab:gcd-comparison}
707	\end{table}
708	
709	Our grammar layer implements the same CFG-based token masking as GCD and BoostCD---the mechanisms are formally identical (JSON schema $\to$ pushdown automaton $\to$ per-step allowed token set).
710	Table~\ref{tab:scierc-ablation} row~2 therefore constitutes a direct comparison: grammar-only enforcement achieves RV/ET$\to$0\% but only ${\sim}$3\% DR reduction, identical to what GCD-family methods would achieve on IE tasks.
711	
712	% exp_id: vllm_guided_json_scierc_zs
713	\paragraph{External verification via vLLM.}
714	To confirm this equivalence experimentally, we evaluated vLLM's \texttt{guided\_json} mode~\cite{kwon2023vllm}---an independent CFG enforcement implementation---on SciERC under identical conditions (Qwen3-8B, zero-shot, 551 documents).
715	
716	\begin{table}[h]
717	\centering
718	\small
719	\begin{tabular}{@{}l rrrr r@{}}
720	\toprule
721	\textbf{Method} & \textbf{DR\,$\downarrow$} & \textbf{RV\,$\downarrow$} & \textbf{ET\,$\downarrow$} & \textbf{CF} & \textbf{R-F1\,$\uparrow$} \\
722	\midrule
723	Grammar-Only (XGrammar) & 14.84 & 0 & 0 & 9.90 & 8.23 \\
724	vLLM \texttt{guided\_json} & 15.26 & 0 & 0 & --- & 8.75 \\
725	\midrule
726	$\Delta$ & $+$0.42 & 0 & 0 & --- & $+$0.52 \\
727	\bottomrule
728	\end{tabular}
729	\caption{GCD-equivalence verification: OntoCoDec grammar-only vs.\ vLLM \texttt{guided\_json} on SciERC (Qwen3-8B, zero-shot, 551 documents). All differences $<$0.5\,pp, confirming that CFG-based approaches---regardless of implementation---leave ${\sim}$15\% DR violations unaddressed.}
730	\label{tab:vllm-verification}
731	\end{table}
732	
733	All metrics differ by $<$0.5\,pp (Table~\ref{tab:vllm-verification}), confirming that any CFG-based constrained decoding tool---whether GCD, BoostCD, or vLLM---enforces the same constraint class and leaves the same ${\sim}$15\% DR gap.
734	The critical gap these methods cannot address is cross-field type consistency (Level~2), which requires the stateful semantic layer that maintains an entity registry across relation slots and enforces per-relation domain/range constraints at each type-bearing position.
735	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2cd55f77-de77-4aab-b1d7-c5a028a0db84",
  "isSidechain": true,
  "promptId": "857bc242-0da2-40fe-8377-411f2acddc00",
  "agentId": "ac3a68eece0ee652a",
  "type": "user",
  "uuid": "2c9250a5-95ec-4c1a-b956-0e34431412a8",
  "sourceToolAssistantUUID": "2cd55f77-de77-4aab-b1d7-c5a028a0db84",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/reviewer_17ad4b4d",
  "sessionId": "9485bf07-277e-42ea-88c3-c883a57507b5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "zany-marinating-cherny"
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-23T11:40:19.737Z_

Now let me use grep to systematically search all five files for the specific claims you mentioned.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2c9250a5-95ec-4c1a-b956-0e34431412a8",
  "isSidechain": true,
  "agentId": "ac3a68eece0ee652a",
  "requestId": "req_011CbKSKMV23qUpotC7aXAiW",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "2e34d4d7-c7c7-49ed-87a5-5c854683276d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/reviewer_17ad4b4d",
  "sessionId": "9485bf07-277e-42ea-88c3-c883a57507b5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "zany-marinating-cherny",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01QMgiNdF4VnMR6TWH2GZBjz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 20567,
      "cache_read_input_tokens": 30082,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 20567,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
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

_source line 20 · 2026-05-23T11:40:21.097Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01BrXpVYGvhTT92q4uGsbypu`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper && grep -n \"WikiEvents\\|GoLLIE\\|eliminates all\\|40--46\\|41--46\\|41--47\\|DR\\|0.21\\|TCR\\|18--92\\|cross-field\" section1_introduction_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2e34d4d7-c7c7-49ed-87a5-5c854683276d",
  "isSidechain": true,
  "agentId": "ac3a68eece0ee652a",
  "requestId": "req_011CbKSKMV23qUpotC7aXAiW",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "3db678d4-da36-4968-9163-d8164ff8aeb8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/reviewer_17ad4b4d",
  "sessionId": "9485bf07-277e-42ea-88c3-c883a57507b5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "zany-marinating-cherny",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01QMgiNdF4VnMR6TWH2GZBjz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 20567,
      "cache_read_input_tokens": 30082,
      "output_tokens": 173,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 20567
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 173,
          "cache_read_input_tokens": 30082,
          "cache_creation_input_tokens": 20567,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 20567,
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

_source line 21 · 2026-05-23T11:40:21.172Z_

<details><summary>↩ Tool result · `toolu_01BrXpVYGvhTT92q4uGsbypu`</summary>

```text
9:At competitive quality (R-F1 40--46\%), even 1--2\% residual violations compound across thousands of documents into systematic knowledge graph corruption, making reliable constraint enforcement necessary.
13:Grammar-constrained decoding~\cite{dong2025xgrammar,willard2023outlines,beurer-kellner2023lmql} ensures syntactic well-formedness but cannot encode cross-field semantic constraints.
18:A decidability analysis of IE type constraints (\S\ref{sec:decidability}) yields a two-layer architecture: the \emph{grammar layer} compiles ontology constraints into context-free grammars (JSON structure, vocabulary membership) via XGrammar; the \emph{semantic layer} interprets type constraints at runtime via dynamic logit masking over an entity registry, with a scale-dependent layer interaction: at 8B, the semantic layer achieves only 24\% independent DR reduction (near-complete when combined), while at 70B it reaches 84\% independently.
20:LoRA + greedy S1 reduces DR to near-zero: DR\,$\leq$\,0.21\% at R-F1 40--46\% ($\pm$0.3\,pp, $+$10\% latency); beam ($k{=}4$) eliminates all violation types on both RE datasets under fine-tuning (1.39$\times$ latency).
21:DR enforcement converts ontologically invalid violations to individually valid but type-inconsistent ones (CF\,$\leq$\,1.4\% fine-tuned); zero-shot DR drops 76--99\% on SciERC and 42--90\% on DocRED, with total violations decreasing $\sim$31\% (Appendix~\ref{app:cross-model-zs}).
23:OntoCoDec is a constraint enforcement method, orthogonal and complementary to training-based schema-aware approaches such as GoLLIE~\cite{sainz2024gollie} and KnowCoder~\cite{knowcoder_acl2024}; it can be composed with any generative IE system to improve schema compliance without retraining.
28:    \item Systematic ablation across 3 model families (Qwen3-8B, Llama-3.1-8B, Mistral-7B) and 2 datasets (SciERC, DocRED) under both zero-shot and LoRA fine-tuned settings, demonstrating DR reduction to $\leq$0.21\% with R-F1 within $\pm$0.3\,pp; DR enforcement introduces CF as a correctable side effect (\S\ref{sec:scierc-results}).
29:    \item Preliminary single-family scale exploration on Llama-3.1-70B (AWQ INT4), revealing a scale-dependent layer interaction: the semantic layer alone achieves 84\% DR reduction at 70B vs.\ 24\% at 8B (\S\ref{sec:70b-results}). Beam $k{=}2$ is Pareto-optimal (R-F1 44.60, CF 0.11\%, 1.18$\times$ latency); $k{=}4$ achieves DR${=}$0\% with near-zero CF at 1.39$\times$.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3db678d4-da36-4968-9163-d8164ff8aeb8",
  "isSidechain": true,
  "promptId": "857bc242-0da2-40fe-8377-411f2acddc00",
  "agentId": "ac3a68eece0ee652a",
  "type": "user",
  "uuid": "af153bf7-01c0-4556-b3fe-6d96e725cd04",
  "sourceToolAssistantUUID": "3db678d4-da36-4968-9163-d8164ff8aeb8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/reviewer_17ad4b4d",
  "sessionId": "9485bf07-277e-42ea-88c3-c883a57507b5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "zany-marinating-cherny"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-23T11:40:23.219Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01YMFJBLE9vJ7yGbHKVewSc7`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper && grep -n \"WikiEvents\\|GoLLIE\\|eliminates all\\|40--46\\|41--46\\|41--47\\|DR\\|0.21\\|TCR\\|18--92\\|cross-field\" section5_runtime.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "af153bf7-01c0-4556-b3fe-6d96e725cd04",
  "isSidechain": true,
  "agentId": "ac3a68eece0ee652a",
  "requestId": "req_011CbKSKjzrmUhqnjgYbsfMi",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "8fe9fe4b-e743-4698-8505-f07906201ae0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/reviewer_17ad4b4d",
  "sessionId": "9485bf07-277e-42ea-88c3-c883a57507b5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "zany-marinating-cherny",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01VCoxGSRXfeXT93bMngpzpH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 977,
      "cache_read_input_tokens": 50649,
      "output_tokens": 151,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 977
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 151,
          "cache_read_input_tokens": 50649,
          "cache_creation_input_tokens": 977,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 977,
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

_source line 23 · 2026-05-23T11:40:23.277Z_

<details><summary>↩ Tool result · `toolu_01YMFJBLE9vJ7yGbHKVewSc7`</summary>

```text
11:With LoRA, beam search~\cite{anderson2017guided} eliminates all four violation types at 8B on both SciERC and DocRED; at 70B, beam $k{=}4$ achieves DR${=}$RV${=}$ET${=}$0\% with one residual CF on SciERC (Appendix~\ref{app:beam-search}).
13:This yields three deployment tiers: greedy S1 ($+$10\% latency, DR${\leq}$0.21\%, CF${\leq}$1.4\%), beam $k{=}2$ (1.18$\times$, near-zero CF), and beam $k{=}4$ (1.39$\times$, all violations${\to}$0\%).
21:Zero-shot S1 eliminates DR on both datasets (SciERC 6.41\%\,$\to$\,0\%, DocRED 14.98\%\,$\to$\,0\%; R-F1 11--13).
23:A four-way ablation reveals scale-dependent layer interaction: semantic-only achieves 84\% DR reduction vs.\ 8B's 24\% (Table~\ref{tab:scierc-ablation}), though grammar remains necessary for RV elimination and CF control (semantic-only CF${=}$76).
25:LoRA confirms composability: DR\,$\to$\,0\% on both datasets (R-F1 44.53, 43.95; $|\Delta| \leq 0.20$\,pp; CF 0.18--1.33\%); cross-family generalization at 70B scale remains to be verified.
32:Our grammar-only ablation (Table~\ref{tab:scierc-ablation}, row~2) implements the same constraints as GCD~\cite{geng2023gcd} and BoostCD~\cite{boostcd2025}; vLLM \texttt{guided\_json}~\cite{kwon2023vllm} confirms equivalence on Qwen3-8B (DR${=}$15.26\%; other models use the same backend; Appendix~\ref{app:gcd-comparison}).
33:The ${\sim}$15\% residual DR is the gap our semantic layer addresses (94\% total reduction); trie-only constraints without JSON enforcement yield 9--51\% parse failure (Appendix~\ref{app:trie-baseline}).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8fe9fe4b-e743-4698-8505-f07906201ae0",
  "isSidechain": true,
  "promptId": "857bc242-0da2-40fe-8377-411f2acddc00",
  "agentId": "ac3a68eece0ee652a",
  "type": "user",
  "uuid": "584b884e-7448-4117-9841-bf3febc4f03c",
  "sourceToolAssistantUUID": "8fe9fe4b-e743-4698-8505-f07906201ae0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/reviewer_17ad4b4d",
  "sessionId": "9485bf07-277e-42ea-88c3-c883a57507b5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "zany-marinating-cherny"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-23T11:40:25.149Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01Q7wE83zy3hTUuwySaGt8do`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper && grep -n \"WikiEvents\\|GoLLIE\\|eliminates all\\|40--46\\|41--46\\|41--47\\|DR\\|0.21\\|TCR\\|18--92\\|cross-field\" section7_conclusion_compressed.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "584b884e-7448-4117-9841-bf3febc4f03c",
  "isSidechain": true,
  "agentId": "ac3a68eece0ee652a",
  "requestId": "req_011CbKSKtybxADRVZCsozpW5",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "6b79d666-8a7e-49cd-88f7-323423b2eb67",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/reviewer_17ad4b4d",
  "sessionId": "9485bf07-277e-42ea-88c3-c883a57507b5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "zany-marinating-cherny",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_015LHdbb6kavovoLopDZ47n1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 770,
      "cache_read_input_tokens": 51626,
      "output_tokens": 153,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 770
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 153,
          "cache_read_input_tokens": 51626,
          "cache_creation_input_tokens": 770,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 770,
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

_source line 25 · 2026-05-23T11:40:25.206Z_

<details><summary>↩ Tool result · `toolu_01Q7wE83zy3hTUuwySaGt8do`</summary>

```text
4:Because IE type constraints exceed context-free expressiveness (Proposition~1), the semantic layer bridges the gap grammar-only enforcement cannot address (3\% vs.\ 94\% DR reduction at 8B), using constructive forward masking over a dynamic entity registry.
7:\paragraph{DR$\leftrightarrow$CF trade-off.}
8:Greedy S1 reduces DR to $\leq$\,0.21\% but introduces CF (zero-shot $+$9.82\,pp, fine-tuned $+$1.18\,pp)---an architectural consequence of per-triple independent enforcement.
10:Beam $k{=}2$ reduces CF to 0.11\% at 1.18$\times$ latency (Pareto-optimal; recommended for zero-shot deployment); $k{=}4$ eliminates all violations at 8B (1 residual CF at 70B) at 1.39$\times$ (\S\ref{sec:beam-results}).
11:Net effect: total violations decrease ${\sim}$31\% in zero-shot and ${>}$90\% under fine-tuning; DR is irrecoverable while CF is amenable to post-hoc resolution (TCR; Appendix~\ref{app:tcr}).
14:GoLLIE and KnowCoder internalize schema knowledge via training but lack runtime guarantees; LoRA + S1 shows the two are complementary (DR 1--2\%\,$\to$\,$\leq$0.21\%; neither alone achieves both high R-F1 and near-zero DR).
19:Beam search and TCR approximate this; integrating consensus into decoding remains future work.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6b79d666-8a7e-49cd-88f7-323423b2eb67",
  "isSidechain": true,
  "promptId": "857bc242-0da2-40fe-8377-411f2acddc00",
  "agentId": "ac3a68eece0ee652a",
  "type": "user",
  "uuid": "bd657ae7-292b-4ada-98b5-ee9fea602dcd",
  "sourceToolAssistantUUID": "6b79d666-8a7e-49cd-88f7-323423b2eb67",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/reviewer_17ad4b4d",
  "sessionId": "9485bf07-277e-42ea-88c3-c883a57507b5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "zany-marinating-cherny"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-23T11:40:26.778Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01WndgdipE1EYMWcgx5aYNau`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper && grep -n \"WikiEvents\\|GoLLIE\\|eliminates all\\|40--46\\|41--46\\|41--47\\|DR\\|0.21\\|TCR\\|18--92\\|cross-field\" abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bd657ae7-292b-4ada-98b5-ee9fea602dcd",
  "isSidechain": true,
  "agentId": "ac3a68eece0ee652a",
  "requestId": "req_011CbKSL3ESSMKBpT8jjauTL",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "0916d878-bacc-4082-96b6-63a88149f90b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/reviewer_17ad4b4d",
  "sessionId": "9485bf07-277e-42ea-88c3-c883a57507b5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "zany-marinating-cherny",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01RBHiraBWgryW1TdhewUzCQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 574,
      "cache_read_input_tokens": 52396,
      "output_tokens": 148,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 574
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4,
          "output_tokens": 148,
          "cache_read_input_tokens": 52396,
          "cache_creation_input_tokens": 574,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 574,
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

_source line 27 · 2026-05-23T11:40:26.841Z_

<details><summary>↩ Tool result · `toolu_01WndgdipE1EYMWcgx5aYNau`</summary>

```text
3:These violations persist across the capability spectrum and cannot be addressed by grammar-constrained decoding (which lacks cross-field type awareness) or post-hoc filtering (which discards valid predictions).
9:Evaluated across three 8B-class models and two relation extraction datasets (up to 96 relations), OntoCoDec composed with LoRA fine-tuning reduces domain/range violations to near-zero ($\leq$\,0.21\%) at F1 40--46\%, but introduces cross-field type inconsistencies ($\leq$1.4\%) as the dominant residual---an architectural consequence of per-triple independent enforcement; net total violations decrease ${\sim}$31\% in zero-shot and ${>}$90\% under fine-tuning.
10:Beam search ($k{=}2$) reduces CF to 0.11\% at 1.18$\times$ latency; $k{=}4$ eliminates all violation types at 1.39$\times$.
11:In zero-shot settings, cross-field rates are higher (up to 12\%) but decrease with model calibration.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0916d878-bacc-4082-96b6-63a88149f90b",
  "isSidechain": true,
  "promptId": "857bc242-0da2-40fe-8377-411f2acddc00",
  "agentId": "ac3a68eece0ee652a",
  "type": "user",
  "uuid": "e495cbde-ef1f-4e05-865e-cc84cda39d4d",
  "sourceToolAssistantUUID": "0916d878-bacc-4082-96b6-63a88149f90b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/reviewer_17ad4b4d",
  "sessionId": "9485bf07-277e-42ea-88c3-c883a57507b5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "zany-marinating-cherny"
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-23T11:40:29.369Z_

Perfect. Now let me also check for any additional mentions in the files I haven't searched in detail yet. Let me search discussion_paragraphs.tex as well since section6_discussion.tex doesn't exist:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e495cbde-ef1f-4e05-865e-cc84cda39d4d",
  "isSidechain": true,
  "agentId": "ac3a68eece0ee652a",
  "requestId": "req_011CbKSLAns2D4Ry1G5SBqUB",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "5d490606-3393-47be-a7f1-2fe794d59c71",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/reviewer_17ad4b4d",
  "sessionId": "9485bf07-277e-42ea-88c3-c883a57507b5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "zany-marinating-cherny",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01T9ZBajrWNQA9EikejTjCrH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 422,
      "cache_read_input_tokens": 52970,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 422,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
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

_source line 29 · 2026-05-23T11:40:29.831Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01SgJjUALm935zmWjbF3o1t6`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper && grep -n \"WikiEvents\\|GoLLIE\\|eliminates all\\|40--46\\|41--46\\|41--47\\|DR\\|0.21\\|TCR\\|18--92\\|cross-field\" discussion_paragraphs.tex | head -50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5d490606-3393-47be-a7f1-2fe794d59c71",
  "isSidechain": true,
  "agentId": "ac3a68eece0ee652a",
  "requestId": "req_011CbKSLAns2D4Ry1G5SBqUB",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "a05acd8c-b6d7-46d6-8978-9786f54535cd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/reviewer_17ad4b4d",
  "sessionId": "9485bf07-277e-42ea-88c3-c883a57507b5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "zany-marinating-cherny",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01T9ZBajrWNQA9EikejTjCrH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 422,
      "cache_read_input_tokens": 52970,
      "output_tokens": 202,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 422
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 202,
          "cache_read_input_tokens": 52970,
          "cache_creation_input_tokens": 422,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 422,
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

_source line 30 · 2026-05-23T11:40:29.906Z_

<details><summary>↩ Tool result · `toolu_01SgJjUALm935zmWjbF3o1t6`</summary>

```text
8:%          phase0_scierc_unconstrained (DR=15.37%), phase2_docred_unconstrained (DR=18.46%)
14:When applied to fine-tuned models that reach competitive F1 levels, the same constraints remain necessary---Phase~0 analysis confirms that even well-prompted models exhibit non-trivial violation rates (15.37\% DR on SciERC, 18.46\% on DocRED).
24:Domain/range (DR) violations produce structurally invalid triples---a triple asserting that a \emph{Task} entity fills the \emph{domain} slot of \textsc{Part-of}, which requires \emph{Method}, cannot be consumed by any downstream system without error.
25:DR violations are therefore hard constraints.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a05acd8c-b6d7-46d6-8978-9786f54535cd",
  "isSidechain": true,
  "promptId": "857bc242-0da2-40fe-8377-411f2acddc00",
  "agentId": "ac3a68eece0ee652a",
  "type": "user",
  "uuid": "19534480-abdd-47f8-a4d9-a180d0db48b5",
  "sourceToolAssistantUUID": "a05acd8c-b6d7-46d6-8978-9786f54535cd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/reviewer_17ad4b4d",
  "sessionId": "9485bf07-277e-42ea-88c3-c883a57507b5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "zany-marinating-cherny"
}
```

</details>

---

### Assistant

_source line 31 · 2026-05-23T11:40:31.632Z_

Now let me compile the complete findings. Let me verify the exact line numbers and context for all key claims:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "19534480-abdd-47f8-a4d9-a180d0db48b5",
  "isSidechain": true,
  "agentId": "ac3a68eece0ee652a",
  "requestId": "req_011CbKSLPLRBpA5hVE3FGWgJ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "fabe2cee-fdee-4efc-a791-46407df1e87e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/reviewer_17ad4b4d",
  "sessionId": "9485bf07-277e-42ea-88c3-c883a57507b5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "zany-marinating-cherny",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01UA2g5ug4X6r6UNcAh51pxx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 395,
      "cache_read_input_tokens": 53392,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 395,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
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

_source line 32 · 2026-05-23T11:40:35.304Z_

<details open><summary>🔧 Tool call — Read · `toolu_0139oZ6nN5sjBKqmUxftENK4`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section1_introduction_draft.tex",
  "offset": 1,
  "limit": 31
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fabe2cee-fdee-4efc-a791-46407df1e87e",
  "isSidechain": true,
  "agentId": "ac3a68eece0ee652a",
  "requestId": "req_011CbKSLPLRBpA5hVE3FGWgJ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "28a52065-5f49-45eb-b5d2-d66383b7492b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/reviewer_17ad4b4d",
  "sessionId": "9485bf07-277e-42ea-88c3-c883a57507b5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "zany-marinating-cherny",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01UA2g5ug4X6r6UNcAh51pxx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 395,
      "cache_read_input_tokens": 53392,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 395,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
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

_source line 33 · 2026-05-23T11:40:35.328Z_

<details><summary>↩ Tool result · `toolu_0139oZ6nN5sjBKqmUxftENK4`</summary>

```text
1	% Section 1: Introduction (compressed, 669→~550 words)
2	
3	\section{Introduction}
4	\label{sec:introduction}
5	
6	Large language models are increasingly used for information extraction~\cite{li2023codeie,sainz2024gollie,wei2023zeroshot}, but when generating relation triples $(h, r, t)$, neither entity necessarily carries a type consistent with the ontology's domain/range constraints for $r$.
7	We call such outputs \emph{domain/range violations}: structurally valid triples that are ontologically invalid.
8	Violations persist across the capability spectrum: 15.4\% of triples on SciERC~\cite{luan2018scierc} and 18.5\% on DocRED~\cite{yao2019docred} under zero-shot decoding, and 0.5--2\% even after LoRA fine-tuning; rates follow an observed pattern consistent with schema restrictiveness (few valid type pairs per relation) rather than ontology or model scale.
9	At competitive quality (R-F1 40--46\%), even 1--2\% residual violations compound across thousands of documents into systematic knowledge graph corruption, making reliable constraint enforcement necessary.
10	
11	Existing approaches leave a fundamental gap.
12	Schema-informed prompting reduces violations by 62\% on average but is per-relation unreliable (violations for \textsc{Evaluate-for} actually \emph{increase} by 5.8\,pp).
13	Grammar-constrained decoding~\cite{dong2025xgrammar,willard2023outlines,beurer-kellner2023lmql} ensures syntactic well-formedness but cannot encode cross-field semantic constraints.
14	Post-hoc filtering discards up to 48\% of predictions including true positives (Appendix~\ref{app:cross-model-zs}).
15	Training-based approaches~\cite{sainz2024gollie,lu2022uie} internalize schema knowledge but provide only soft guidance without runtime enforcement.
16	
17	We propose \textbf{OntoCoDec}, a framework that translates IE ontologies into composable layers of decoding-time constraints.
18	A decidability analysis of IE type constraints (\S\ref{sec:decidability}) yields a two-layer architecture: the \emph{grammar layer} compiles ontology constraints into context-free grammars (JSON structure, vocabulary membership) via XGrammar; the \emph{semantic layer} interprets type constraints at runtime via dynamic logit masking over an entity registry, with a scale-dependent layer interaction: at 8B, the semantic layer achieves only 24\% independent DR reduction (near-complete when combined), while at 70B it reaches 84\% independently.
19	OntoCoDec compiles constraints automatically from IE ontologies, requires no constraint-specific training, and is applicable to autoregressive LMs with logits access; we validate on three English datasets (up to 96 relation types), three 8B-class models across three tokenizer families, with 70B-class validation (\S\ref{sec:70b-results}).
20	LoRA + greedy S1 reduces DR to near-zero: DR\,$\leq$\,0.21\% at R-F1 40--46\% ($\pm$0.3\,pp, $+$10\% latency); beam ($k{=}4$) eliminates all violation types on both RE datasets under fine-tuning (1.39$\times$ latency).
21	DR enforcement converts ontologically invalid violations to individually valid but type-inconsistent ones (CF\,$\leq$\,1.4\% fine-tuned); zero-shot DR drops 76--99\% on SciERC and 42--90\% on DocRED, with total violations decreasing $\sim$31\% (Appendix~\ref{app:cross-model-zs}).
22	
23	OntoCoDec is a constraint enforcement method, orthogonal and complementary to training-based schema-aware approaches such as GoLLIE~\cite{sainz2024gollie} and KnowCoder~\cite{knowcoder_acl2024}; it can be composed with any generative IE system to improve schema compliance without retraining.
24	
25	Our contributions:
26	\begin{enumerate}[leftmargin=*,itemsep=2pt]
27	    \item A two-layer constrained decoding framework grounded in the observation that domain/range type constraints require stateful enforcement beyond context-free grammars---grammar-only approaches face state spaces of $6^{17}$--$6^{19}$ for typical IE schemas (Proposition~1; \S\ref{sec:decidability}). Constraints compile automatically from IE ontologies, validated on schemas with up to 96 relation types.
28	    \item Systematic ablation across 3 model families (Qwen3-8B, Llama-3.1-8B, Mistral-7B) and 2 datasets (SciERC, DocRED) under both zero-shot and LoRA fine-tuned settings, demonstrating DR reduction to $\leq$0.21\% with R-F1 within $\pm$0.3\,pp; DR enforcement introduces CF as a correctable side effect (\S\ref{sec:scierc-results}).
29	    \item Preliminary single-family scale exploration on Llama-3.1-70B (AWQ INT4), revealing a scale-dependent layer interaction: the semantic layer alone achieves 84\% DR reduction at 70B vs.\ 24\% at 8B (\S\ref{sec:70b-results}). Beam $k{=}2$ is Pareto-optimal (R-F1 44.60, CF 0.11\%, 1.18$\times$ latency); $k{=}4$ achieves DR${=}$0\% with near-zero CF at 1.39$\times$.
30	\end{enumerate}
31	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "28a52065-5f49-45eb-b5d2-d66383b7492b",
  "isSidechain": true,
  "promptId": "857bc242-0da2-40fe-8377-411f2acddc00",
  "agentId": "ac3a68eece0ee652a",
  "type": "user",
  "uuid": "73feea66-0e07-4054-b1fa-8fa6defbf350",
  "sourceToolAssistantUUID": "28a52065-5f49-45eb-b5d2-d66383b7492b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/reviewer_17ad4b4d",
  "sessionId": "9485bf07-277e-42ea-88c3-c883a57507b5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "zany-marinating-cherny"
}
```

</details>

---

### Assistant

_source line 34 · 2026-05-23T11:40:57.729Z_

Perfect. Now let me create a comprehensive summary report with all the findings:

## VERIFICATION REPORT: Paper Claim Locations and Content

### FILE 1: section1_introduction_draft.tex
**Status:** EXISTS, 31 lines total

**Key Claims Found:**

1. **F1 Range Claims:**
   - Line 9: `At competitive quality (R-F1 40--46\%), even 1--2\% residual violations...`
   - Line 20: `DR\,$\leq$\,0.21\% at R-F1 40--46\% ($\pm$0.3\,pp, $+$10\% latency)`
   - Line 29: `Beam $k{=}2$ is Pareto-optimal (R-F1 44.60, CF 0.11\%, 1.18$\times$ latency)`
   - **FINDING:** Range is consistently **"40--46%"**, not "41--46%" or "41--47%"

2. **DR (Domain/Range) Claims:**
   - Line 20: `DR\,$\leq$\,0.21\%` (multiple instances throughout)
   - Line 28: `demonstrating DR reduction to $\leq$0.21\%`
   - Line 21: `zero-shot DR drops 76--99\% on SciERC and 42--90\% on DocRED`
   - Line 18: `semantic layer achieves only 24\% independent DR reduction...while at 70B it reaches 84\%`

3. **Beam4 "Eliminates All" Claims:**
   - Line 20: `beam ($k{=}4$) eliminates all violation types on both RE datasets under fine-tuning`
   - Line 29: `$k{=}4$ achieves DR${=}$0\% with near-zero CF at 1.39$\times`

4. **Cross-Field Claims:**
   - Line 13: `cannot encode cross-field semantic constraints`
   - Line 21: `DR enforcement converts ontologically invalid violations to individually valid but type-inconsistent ones (CF\,$\leq$\,1.4\% fine-tuned)`

5. **GoLLIE Mentions:**
   - Line 23: `such as GoLLIE~\cite{sainz2024gollie} and KnowCoder`
   - Line 15: `Training-based approaches~\cite{sainz2024gollie,lu2022uie}`

6. **0.21 Mentions:**
   - Line 20: `DR\,$\leq$\,0.21\%`
   - Line 28: `$\leq$0.21\%`

---

### FILE 2: section5_runtime.tex
**Status:** EXISTS, 34 lines total

**Key Claims Found:**

1. **Beam4 "Eliminates All" Claims:**
   - Line 11: `With LoRA, beam search~\cite{anderson2017guided} eliminates all four violation types at 8B on both SciERC and DocRED; at 70B, beam $k{=}4$ achieves DR${=}$RV${=}$ET${=}$0\%`
   - Line 13: `beam $k{=}4$ (1.39$\times$, all violations${\to}$0\%)`
   - Line 10: `$k{=}4$ eliminates all violation types at 8B` (from line 11)

2. **DR Claims:**
   - Line 13: `greedy S1 ($+$10\% latency, DR${\leq}$0.21\%, CF${\leq}$1.4\%)`
   - Line 21: `Zero-shot S1 eliminates DR on both datasets (SciERC 6.41\%\,$\to$\,0\%, DocRED 14.98\%\,$\to$\,0\%)`
   - Line 25: `LoRA confirms composability: DR\,$\to$\,0\%`
   - Line 23: `semantic-only achieves 84\% DR reduction vs.\ 8B's 24\%`
   - Line 32: `DR${=}$15.26\%`
   - Line 33: `residual DR is the gap our semantic layer addresses (94\% total reduction)`

3. **Cross-Field Mentions:**
   - Line 25: `cross-family generalization at 70B scale`

---

### FILE 3: section7_conclusion_compressed.tex
**Status:** EXISTS, 20 lines total

**Key Claims Found:**

1. **Beam4 "Eliminates All" Claims:**
   - Line 10: `$k{=}4$ eliminates all violations at 8B (1 residual CF at 70B) at 1.39$\times$`

2. **DR Claims:**
   - Line 4: `3\% vs.\ 94\% DR reduction at 8B`
   - Line 8: `Greedy S1 reduces DR to $\leq$\,0.21\%`
   - Line 11: `DR is irrecoverable while CF is amenable to post-hoc resolution (TCR; Appendix~\ref{app:tcr})`

3. **TCR (Type Cascade Resolution) Mentions:**
   - Line 11: `(TCR; Appendix~\ref{app:tcr})`
   - Line 19: `Beam search and TCR approximate this`
   - **NOTE:** No "18--92%" range mentioned. Section refers readers to Appendix~\ref{app:tcr} for details.

4. **GoLLIE Mentions:**
   - Line 14: `GoLLIE and KnowCoder internalize schema knowledge via training but lack runtime guarantees; LoRA + S1 shows the two are complementary (DR 1--2\%\,$\to$\,$\leq$0.21\%`

5. **Cross-Field Mentions:**
   - Line 7: `\paragraph{DR$\leftrightarrow$CF trade-off.}`
   - Line 18: `Per-triple vs.\ global enforcement` (section on CF issues)

---

### FILE 4: abstract.tex
**Status:** EXISTS, 13 lines total

**Key Claims Found:**

1. **F1 Range Claims:**
   - Line 9: `at F1 40--46\%, but introduces cross-field type inconsistencies`
   - **CONSISTENT:** "40--46%"

2. **Cross-Field Claims:**
   - Line 3: `(which lacks cross-field type awareness)`
   - Line 9: `cross-field type inconsistencies ($\leq$1.4\%)`
   - Line 10: `Beam search ($k{=}2$) reduces CF to 0.11\% at 1.18$\times$ latency; $k{=}4$ eliminates all violation types at 1.39$\times$`
   - Line 11: `In zero-shot settings, cross-field rates are higher (up to 12\%)`

3. **DR Claims:**
   - Line 9: `reduces domain/range violations to near-zero ($\leq$\,0.21\%)`
   - Line 12: `Zero-shot domain/range reductions span 76--99\% on SciERC and 42--90\% on DocRED`

4. **"Eliminates All" Claim:**
   - Line 10: `$k{=}4$ eliminates all violation types at 1.39$\times$`

---

### FILE 5: section6_discussion.tex
**Status:** DOES NOT EXIST

The file `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_discussion.tex` does not exist.

However, related discussion content is located in:
- `/appendix_discussion.tex` (extended discussion, 735 lines, includes GoLLIE and complementarity narrative)
- `/discussion_paragraphs.tex` (discussion paragraphs, 25+ lines)

**GoLLIE mention in appendix_discussion.tex:**
- Line 739: `OntoCoDec's advantage thus scales with violation severity: precisely when constraints are most needed, post-hoc filtering is most destructive.`
- Lines discussing complementarity throughout the appendix (e.g., line 734-735 on grammar-based approaches)

---

## SUMMARY OF KEY FINDINGS:

### VERIFIED CLAIMS:
✓ **F1 Range:** Consistently **"40--46%"** (NOT "41--46%" or "41--47%")
✓ **DR Claims (0.21%):** Consistently `DR\,$\leq$\,0.21\%` across files
✓ **Beam4 "Eliminates All":** Multiple confirmations across 3 files:
  - section1_introduction_draft.tex (line 20, 29)
  - section5_runtime.tex (line 11, 13)
  - section7_conclusion_compressed.tex (line 10)
  - abstract.tex (line 10)
✓ **GoLLIE Mentions:** Found in section1 (line 23, 15) and section7 (line 14)
✓ **Cross-Field Claims:** Multiple mentions in all files (section1 line 13, 21; section5 line 25; abstract line 3, 9, 10, 11)

### MISSING/AMBIGUOUS CLAIMS:
- **TCR "18--92%":** No such range found in section7_conclusion_compressed.tex. The file references TCR in Appendix only (line 11, 19). The appendix_discussion.tex file (735 lines) would need examination for TCR details.
- **WikiEvents:** NOT found in any of the five requested files.
- **Section6 Discussion:** File does not exist; content may be in appendix_discussion.tex or discussion_paragraphs.tex instead.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "73feea66-0e07-4054-b1fa-8fa6defbf350",
  "isSidechain": true,
  "agentId": "ac3a68eece0ee652a",
  "requestId": "req_011CbKSLoGajqMYRVYeJdpvM",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "eb4dc2e8-6877-4b4d-86bf-35fc3dc4efd0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/reviewer_17ad4b4d",
  "sessionId": "9485bf07-277e-42ea-88c3-c883a57507b5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "zany-marinating-cherny",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01P6DxRpayutkCnK53RbVtoJ",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 1628,
      "cache_read_input_tokens": 53787,
      "output_tokens": 2463,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1628
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 2463,
          "cache_read_input_tokens": 53787,
          "cache_creation_input_tokens": 1628,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1628,
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
