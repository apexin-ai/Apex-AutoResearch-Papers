# Research conversation: I need to verify that all R17 review fixes were properly implemented in the paper. Read the following files and check ea

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 56
- **Recorded user turns:** 1
- **Tool calls:** 23
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-ad6a42899911fc70c.jsonl`
- **Structured JSON:** [`bef03c4f1f8abefed858.json`](../../sessions/be/bef03c4f1f8abefed858.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

56 recorded events

### User

_source line 1 · 2026-05-22T12:01:01.542Z_

I need to verify that all R17 review fixes were properly implemented in the paper. Read the following files and check each item:

**Files to read:**
1. /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract.tex
2. /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_runtime.tex
3. /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex
4. /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_crossmodel_draft.tex
5. /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_method.tex (or similar method section)
6. /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/limitations.tex (or wherever limitations are)

**Check each R17 fix:**

MF1: DR range — should be consistent across abstract and body. Previously abstract said "45-99%" but crossmodel said "76-99% SciERC, 42-90% DocRED". Check what they say now and whether they're consistent.

MF2: CF bound — previously "≤1.3%" but 70B has 1.33%. Should be updated to ≤1.4% or similar. Check abstract and section5_scierc_draft.

MF3: CF narrative — ZS CF worst case (12.02% Llama DocRED) should be prominently mentioned. Abstract should distinguish ZS/FT. Check.

MF4: "five" LMs → should be "four". Check abstract.

MF5: GCD equivalence argument — should be explicitly stated somewhere that grammar-only ablation = GCD-equivalent. Find where this argument is made and assess its strength.

SF1: κ̄ n=3 — should have caveat about small sample. Find and check.
SF2: WikiEvents n=20 — should have "preliminary" and CI. Check.
SF3: "deployment-grade" — should be softened. Check.
SF4: "enabling dependency" — should note SciERC-only scope. Check.
SF5: Entity registry order — should have quantified Limitations sentence. Check.
SF6: S2 description — should match evaluation. Check.

M1-M7: Check for any obvious remaining issues.

Also look for any NEW inconsistencies introduced by the fixes.

Report each item with: location (file:line), current text, and whether it's properly fixed (PASS/FAIL/PARTIAL).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "14fc01a8-031f-4ceb-ad2f-39c6c6b967ca",
  "agentId": "ad6a42899911fc70c",
  "type": "user",
  "uuid": "c4c9f28d-0d56-4ca5-ade3-460ea63896c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/reviewer_17ad4b4d",
  "sessionId": "99513a19-7109-43ba-90b7-1799724932fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cached-moseying-feather"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-22T12:01:01.546Z_

```json
{
  "parentUuid": "c4c9f28d-0d56-4ca5-ade3-460ea63896c2",
  "isSidechain": true,
  "agentId": "ad6a42899911fc70c",
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterWorktree",
      "ExitWorktree",
      "ListMcpResourcesTool",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "ReadMcpResourceTool",
      "RemoteTrigger",
      "TaskStop",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__check_figures_and_layout",
      "mcp__agent-ml-research__cleanup_pdf_images",
      "mcp__agent-ml-research__compute_coverage_matrix",
      "mcp__agent-ml-research__fetch_wandb_metrics",
      "mcp__agent-ml-research__get_gpu_health",
      "mcp__agent-ml-research__get_project_resource_usage",
      "mcp__agent-ml-research__list_constraints",
      "mcp__agent-ml-research__pdf_to_images",
      "mcp__agent-ml-research__read_experiment_plan_with_status",
      "mcp__agent-ml-research__read_matrix",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__read_roadmap",
      "mcp__agent-ml-research__reviewer_post_to_director",
      "mcp__agent-ml-research__ssh_read_only",
      "mcp__agent-ml-research__tail_training_logs"
    ],
    "addedLines": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterWorktree",
      "ExitWorktree",
      "ListMcpResourcesTool",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "ReadMcpResourceTool",
      "RemoteTrigger",
      "TaskStop",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__check_figures_and_layout",
      "mcp__agent-ml-research__cleanup_pdf_images",
      "mcp__agent-ml-research__compute_coverage_matrix",
      "mcp__agent-ml-research__fetch_wandb_metrics",
      "mcp__agent-ml-research__get_gpu_health",
      "mcp__agent-ml-research__get_project_resource_usage",
      "mcp__agent-ml-research__list_constraints",
      "mcp__agent-ml-research__pdf_to_images",
      "mcp__agent-ml-research__read_experiment_plan_with_status",
      "mcp__agent-ml-research__read_matrix",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__read_roadmap",
      "mcp__agent-ml-research__reviewer_post_to_director",
      "mcp__agent-ml-research__ssh_read_only",
      "mcp__agent-ml-research__tail_training_logs"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "1a1401cf-2d24-4415-959e-284d0f7c083c",
  "timestamp": "2026-05-22T12:01:01.546Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/reviewer_17ad4b4d",
  "sessionId": "99513a19-7109-43ba-90b7-1799724932fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cached-moseying-feather"
}
```

---

### Assistant

_source line 3 · 2026-05-22T12:01:04.213Z_



I'll read all the relevant files to verify the R17 fixes.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1a1401cf-2d24-4415-959e-284d0f7c083c",
  "isSidechain": true,
  "agentId": "ad6a42899911fc70c",
  "requestId": "req_011CbHa6G69359H5hikpTsTQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4cedb9ab-7c33-4bc7-8807-bf812013fa89",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/reviewer_17ad4b4d",
  "sessionId": "99513a19-7109-43ba-90b7-1799724932fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cached-moseying-feather",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012L8bkfd7m4gkEEApM2yZew",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 25762,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 25762,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
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

_source line 4 · 2026-05-22T12:01:04.808Z_

<details open><summary>🔧 Tool call — Read · `toolu_01KoZ24UdwJUTgV7eDn3AuNJ`</summary>

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
  "parentUuid": "4cedb9ab-7c33-4bc7-8807-bf812013fa89",
  "isSidechain": true,
  "agentId": "ad6a42899911fc70c",
  "requestId": "req_011CbHa6G69359H5hikpTsTQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5e8aabaf-40b0-4f02-b8f8-6cf4acec5fa4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/reviewer_17ad4b4d",
  "sessionId": "99513a19-7109-43ba-90b7-1799724932fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cached-moseying-feather",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012L8bkfd7m4gkEEApM2yZew",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 25762,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 25762,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
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

_source line 5 · 2026-05-22T12:01:04.819Z_

<details><summary>↩ Tool result · `toolu_01KoZ24UdwJUTgV7eDn3AuNJ`</summary>

```text
1	\begin{abstract}
2	We present \textsc{OntoCoDec}, a framework that translates Information Extraction (IE) ontologies into composable token-level decoding constraints via a decidability-guided architecture: a \emph{grammar layer} (context-free) compiles ontology constraints into grammars ensuring JSON validity and vocabulary membership; a \emph{semantic layer} (prefix-decidable with state) interprets type constraints at runtime via stateful token masking over a dynamic entity registry, with grammar-first fallback when constraints conflict.
3	Without constraints, Large Language Model (LLM) based IE produces systematic domain/range (DR) violations that persist after fine-tuning, with rates characterized by \emph{constraint tightness} ($\bar{\kappa}$), a descriptive metric correlating schema restrictiveness with enforcement outcomes ($n{=}3$ schemas).
4	The two layers exhibit an empirical enabling dependency (Proposition~1): neither achieves this reduction alone.
5	% exp_ids: w5_lora_scierc_constrained_eval, w5_qwen_docred_lora_constrained_eval, w5_llama_lora_scierc_constrained_eval, w5_llama_docred_lora_constrained_eval
6	Composed with LoRA fine-tuning, \textsc{OntoCoDec} achieves near-complete DR elimination: DR\,$\leq$\,0.09\% at R-F1 43--46\% ($\pm$0.8\,pp, $<$0.5\% true-positive loss); residual CF ($\leq$1.4\% fine-tuned; up to 12\% zero-shot) represents \emph{violation conversion}---ontologically invalid triples (DR) are replaced by individually valid but type-inconsistent ones---resolved by beam search on SciERC (\S\ref{sec:beam-results}).
7	Zero-shot evaluation serves as a diagnostic, revealing dataset- and calibration-dependent effectiveness (42--99\% DR reduction, total violation reduction 31\%; \S\ref{sec:experiments}) and characterizing constraint tightness ($\bar{\kappa}$) as a descriptive correlate ($n{=}3$ schemas).
8	The framework is validated on RE (SciERC, DocRED) with preliminary event extraction results on WikiEvents, across four autoregressive LMs (7--70B; 70B zero-shot and LoRA in \S\ref{sec:70b-results}) with logits access and three tokenizer families (up to 96 relation types).
9	\end{abstract}
10	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5e8aabaf-40b0-4f02-b8f8-6cf4acec5fa4",
  "isSidechain": true,
  "promptId": "14fc01a8-031f-4ceb-ad2f-39c6c6b967ca",
  "agentId": "ad6a42899911fc70c",
  "type": "user",
  "uuid": "00205fe9-aba1-446e-95fd-55a759e96ae8",
  "sourceToolAssistantUUID": "5e8aabaf-40b0-4f02-b8f8-6cf4acec5fa4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/reviewer_17ad4b4d",
  "sessionId": "99513a19-7109-43ba-90b7-1799724932fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cached-moseying-feather"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-22T12:01:05.773Z_

<details open><summary>🔧 Tool call — Read · `toolu_01UPWbMWRVvybFMsHH7jrojj`</summary>

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
  "parentUuid": "00205fe9-aba1-446e-95fd-55a759e96ae8",
  "isSidechain": true,
  "agentId": "ad6a42899911fc70c",
  "requestId": "req_011CbHa6G69359H5hikpTsTQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bc57f1c9-4aee-4e1a-9529-1fb7329518c4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/reviewer_17ad4b4d",
  "sessionId": "99513a19-7109-43ba-90b7-1799724932fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cached-moseying-feather",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012L8bkfd7m4gkEEApM2yZew",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 25762,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 25762,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
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

_source line 7 · 2026-05-22T12:01:05.839Z_

<details><summary>↩ Tool result · `toolu_01UPWbMWRVvybFMsHH7jrojj`</summary>

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
10	With LoRA, beam search ($k{=}4$)~\cite{anderson2017guided} eliminates all four violation types on SciERC (R-F1 44--46); zero-shot beam achieves DR${=}$0\% on both datasets (CF response is model-dependent; Appendix~\ref{app:beam-search}).
11	Total latency: 1.54$\times$ (beam 1.32$\times$ $+$ constraint 1.17$\times$; Table~\ref{tab:beam-latency}).
12	
13	% exp_ids: r16_70b_scierc_zs_s1, r16_70b_docred_zs_s1, 70b_lora_scierc, 70b_lora_docred_200
14	\paragraph{70B evaluation.}
15	\label{sec:70b-results}
16	On Llama-3.3-70B-Instruct (AWQ INT4), zero-shot S1 eliminates DR on both datasets: SciERC 6.41\%\,$\to$\,0\% (R-F1 11.24), DocRED 14.98\%\,$\to$\,0\% (R-F1 13.05); CF rises to 3.50--7.01\%, comparable to 8B zero-shot CF.
17	% exp_ids: eval_70b_lora_scierc_s1_constrained, eval_70b_lora_docred_200_s1_constrained
18	LoRA fine-tuning confirms scale-independent composability: SciERC DR 1.50\%\,$\to$\,0\% (R-F1 44.53, $-$0.20\,pp); DocRED (200-document subset; Appendix~\ref{app:power-analysis}) DR 0.22\%\,$\to$\,0\% (R-F1 43.95, $+$0.15\,pp); CF drops from 3.50\% (zero-shot) to 0.18--1.33\% (LoRA), consistent with the 8B pattern (9.90\%\,$\to$\,1.18\%; \S\ref{sec:composability}).
19	
20	% exp_ids: trie_qwen_ft_scierc, trie_qwen_zs_scierc, trie_llama_ft_scierc, trie_llama_zs_scierc
21	\paragraph{Comparison with grammar-constrained approaches.}
22	\label{sec:constrained-baselines}
23	Our grammar-only ablation (Table~\ref{tab:scierc-ablation}, row~2) implements the same token-level constraints as GCD~\cite{geng2023gcd} and BoostCD~\cite{boostcd2025}---CFG-based JSON structure enforcement plus vocabulary membership masking---providing a direct head-to-head comparison: RV/ET$\to$0\% but only 3\% DR reduction, vs.\ S1's 94\%, confirming that CFG enforcement alone is insufficient for type-valid IE.
24	Without JSON structural enforcement, trie-only vocabulary constraints yield R-F1 19.95--41.16 on SciERC LoRA (vs.\ OntoCoDec's 43.77--45.47) with 9.1--50.8\% parse failure (Appendix~\ref{app:trie-baseline}); the model-dependent disparity confirms grammar enforcement provides a model-independent structural guarantee.
25	BoostCD's~\cite{boostcd2025} boosting is potentially integrable with OntoCoDec.
26	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bc57f1c9-4aee-4e1a-9529-1fb7329518c4",
  "isSidechain": true,
  "promptId": "14fc01a8-031f-4ceb-ad2f-39c6c6b967ca",
  "agentId": "ad6a42899911fc70c",
  "type": "user",
  "uuid": "1e66a52d-575a-49b2-907b-8919a35b780b",
  "sourceToolAssistantUUID": "bc57f1c9-4aee-4e1a-9529-1fb7329518c4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/reviewer_17ad4b4d",
  "sessionId": "99513a19-7109-43ba-90b7-1799724932fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cached-moseying-feather"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-22T12:01:06.102Z_

<details open><summary>🔧 Tool call — Read · `toolu_012g7VtwPjdzCxd6ZPkSXBDc`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1e66a52d-575a-49b2-907b-8919a35b780b",
  "isSidechain": true,
  "agentId": "ad6a42899911fc70c",
  "requestId": "req_011CbHa6G69359H5hikpTsTQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9350cc64-abb2-41ce-af9f-0d2c47d6e084",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/reviewer_17ad4b4d",
  "sessionId": "99513a19-7109-43ba-90b7-1799724932fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cached-moseying-feather",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012L8bkfd7m4gkEEApM2yZew",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 25762,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 25762,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
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

_source line 9 · 2026-05-22T12:01:06.113Z_

<details><summary>↩ Tool result · `toolu_012g7VtwPjdzCxd6ZPkSXBDc`</summary>

```text
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
45	S1
46	  & \textbf{0.93} & $\downarrow$\textbf{94\%}
47	  & \textbf{0} & \textbf{0}
48	  & 9.90  & \textbf{10.83}
49	  & \textbf{8.36} & 30.98 \\
50	S2
51	  & 0.97  & $\downarrow$94\%
52	  & \textbf{0} & \textbf{0}
53	  & 8.03  & \textbf{9.00}
54	  & 8.03  & \textbf{31.90} \\
55	\bottomrule
56	\end{tabular}}%
57	\caption{Five-way ablation on SciERC (551 docs, Qwen3-8B, zero-shot).
58	$\Delta$DR: relative change vs.\ unconstrained.
59	Tot.\ = DR + CF (total type-violation burden).
60	Best per column in \textbf{bold} (CF excluded; Tot.\ included).
61	F1 $\times$100. Bootstrap: 10{,}000 iterations.
62	CF: same entity assigned conflicting types across triples.
63	S1 = single-pass (\S\ref{sec:strategies}), S2 = two-pass (\S\ref{sec:s2}).
64	Grammar-only represents the ceiling of grammar-constrained decoding~\cite{geng2023gcd}: vocabulary membership is enforced but cross-field semantic constraints are not.}
65	\label{tab:scierc-ablation}
66	\end{table}
67	
68	% ──────────────────────────────────────────
69	%  (a) Core result
70	% ──────────────────────────────────────────
71	\paragraph{Zero-shot diagnostic.}
72	% phase2_scierc_unconstrained: DR=0.1537; phase2_scierc_full_s1: DR=0.0093
73	% phase2_scierc_unconstrained: R-F1=0.0823; phase2_scierc_full_s1: R-F1=0.0836
74	% bootstrap: delta=+0.13pp, CI=[-0.24,+0.58], p=0.5824
75	S1 reduces DR from 15.37\% to 0.93\% ($\downarrow$94\%) while R-F1 is unchanged (8.23\,$\to$\,8.36, $p{=}0.58$).
76	Per-relation DR drops to $\leq$2.82\%, reaching 0\% on 4/7 relations (Appendix~\ref{app:per-relation-landscape}).
77	Post-hoc filtering discards up to 48\% of predictions rather than correcting them (Appendix~\ref{app:posthoc-extended}).
78	Total type-violation burden (Tot.\,=\,DR+CF) decreases from 15.45\% to 10.83\% ($\downarrow$30\%), reflecting \emph{violation conversion}: DR enforcement replaces ontologically invalid triples with individually valid but type-inconsistent ones (CF 0.08\%\,$\to$\,9.90\%); under fine-tuning, Tot.\ drops to 1.18\% with CF\,$\leq$\,1.4\% (Table~\ref{tab:composability}).
79	
80	% ──────────────────────────────────────────
81	%  (b) Grammar layer
82	% ──────────────────────────────────────────
83	\paragraph{Layer contributions.}
84	% phase2_scierc_grammar_only: RV=0, ET=0, DR=0.1484, R-F1=0.0823
85	Grammar-only eliminates RV and ET with no F1 impact while DR remains at 14.84\%, the ceiling of grammar-based decoding~\cite{geng2023gcd}; grammar-only CF is near-zero (0.08\%), so CF originates from the semantic layer.
86	Semantic-only reduces DR by only 24\% and cannot eliminate RV or ET; this is the \emph{empirical enabling dependency}: adding the grammar layer yields a further 92\% reduction (11.65\%\,$\to$\,0.93\%).
87	
88	
89	% ──────────────────────────────────────────
90	%  (d) S1 vs S2
91	% ──────────────────────────────────────────
92	\paragraph{S1 vs.\ S2.}
93	S2 achieves comparable DR (0.97\%) but lower R-F1 and CF; we adopt S1.
94	% phase2_scierc_full_s2: DR=0.0097, R-F1=0.0803, CF=0.0803, triples=1644
95	
96	% ──────────────────────────────────────────
97	%  (e) Composability with Fine-Tuning
98	%  exp_ids: w5_lora_scierc_unconstrained_eval, w5_lora_scierc_constrained_eval,
99	%           w5_llama_lora_scierc_unconstrained_eval, w5_llama_lora_scierc_constrained_eval,
100	%           w5_qwen_docred_lora_unconstrained_eval, w5_qwen_docred_lora_constrained_eval,
101	%           w5_llama_docred_lora_unconstrained_eval, w5_llama_docred_lora_constrained_eval
102	% ──────────────────────────────────────────
103	\paragraph{Composability with fine-tuning.}
104	\label{sec:composability}
105	% exp_ids: bootstrap_ci_ft_composability.json
106	Fine-tuning alone reduces DR to 1--2\% but leaves residual violations (Table~\ref{tab:composability}); adding S1 yields DR\,$\leq$\,0.09\% with no significant $\Delta$R-F1 after Bonferroni correction (min.\ $p{=}0.014$; 95\% CIs $\subseteq [-0.76, {+}0.22]$\,pp; removed triples are 97.6--100\% false positives).
107	CF drops from $+$9.82\,pp (zero-shot) to $+$1.18\,pp (fine-tuned; Appendix~\ref{app:cf-distribution}); beam ($k{=}4$) with LoRA eliminates all four violation types on SciERC (R-F1 43.60, 46.18; \S\ref{sec:beam-results}).
108	
109	\begin{table}[t]
110	\centering
111	\small
112	\setlength{\tabcolsep}{3pt}
113	\resizebox{\columnwidth}{!}{%
114	\begin{tabular}{@{}lll rrrr r@{}}
115	\toprule
116	\textbf{Model} & \textbf{Dataset} & \textbf{Mode}
117	  & \textbf{DR\,$\downarrow$} & \textbf{CF}
118	  & \textbf{R-F1\,$\uparrow$} & \textbf{E-F1\,$\uparrow$}
119	  & \textbf{$\Delta$DR} \\
120	\midrule
121	\multirow{4}{*}{Qwen3-8B}
122	  & \multirow{2}{*}{SciERC}
123	    & Unconstr.\ &  1.95 & 0    & 43.86 & 67.05 & --- \\
124	  & & S1    & \textbf{0} & 1.18 & 43.77 & 67.05 & $\downarrow$100\% \\
125	\cmidrule(l){2-8}
126	  & \multirow{2}{*}{DocRED}
127	    & Unconstr.\ &  0.56 & 0.08 & 40.89 & 82.35 & --- \\
128	  & & S1    & \textbf{0.00} & 0.22 & 40.79 & 81.87 & $\downarrow$100\% \\
129	\midrule
130	\multirow{4}{*}{\shortstack[l]{Llama\\3.1-8B}}
131	  & \multirow{2}{*}{SciERC}
132	    & Unconstr.\ &  1.11 & 0    & 45.45 & 67.76 & --- \\
133	  & & S1    &  0.09 & 0.46 & 45.47 & 67.76 & $\downarrow$92\% \\
134	\cmidrule(l){2-8}
135	  & \multirow{2}{*}{DocRED}
136	    & Unconstr.\ &  0.49 & 0.08 & 44.55 & 84.77 & --- \\
137	  & & S1    &  0.00 & 0.26 & 44.70 & 84.71 & $\downarrow$100\% \\
138	\bottomrule
139	\end{tabular}}%
140	\caption{Fine-tuning composability: LoRA $\times$ unconstrained vs.\ S1 on SciERC (551 docs) and DocRED (998 dev docs).
141	F1\,$\times$100. No $\Delta$R-F1 is significant (Bonferroni-corrected; details in text); all DR reductions are ($p{<}0.001$).
142	E-F1 includes parse-failure documents (Qwen PF: 7--8\%; Llama PF: 2--3\%).}
143	\label{tab:composability}
144	\end{table}
145	
146	% ──────────────────────────────────────────
147	%  (f) Downstream impact of DR elimination
148	%  exp_ids: task_e_lucky_violation_analysis
149	% ──────────────────────────────────────────
150	\paragraph{Downstream impact.}
151	\label{sec:downstream-impact}
152	Among constraint-removed triples, only 0.49\% match gold labels on average (``lucky violations''), confirming $<$0.5\% recall cost; on Llama SciERC all five are recovered via legal type paths (zero churn; Appendix~\ref{app:lucky-violations}).
153	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9350cc64-abb2-41ce-af9f-0d2c47d6e084",
  "isSidechain": true,
  "promptId": "14fc01a8-031f-4ceb-ad2f-39c6c6b967ca",
  "agentId": "ad6a42899911fc70c",
  "type": "user",
  "uuid": "559e5e1a-e2d0-4a28-b119-2f2a9dadfe49",
  "sourceToolAssistantUUID": "9350cc64-abb2-41ce-af9f-0d2c47d6e084",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/reviewer_17ad4b4d",
  "sessionId": "99513a19-7109-43ba-90b7-1799724932fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cached-moseying-feather"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-22T12:01:06.384Z_

<details open><summary>🔧 Tool call — Read · `toolu_01WRZSXKqgaAdrhRVYh3Bb8d`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_crossmodel_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "559e5e1a-e2d0-4a28-b119-2f2a9dadfe49",
  "isSidechain": true,
  "agentId": "ad6a42899911fc70c",
  "requestId": "req_011CbHa6G69359H5hikpTsTQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7af0abb1-8a09-44ab-a493-3be92db058c5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/reviewer_17ad4b4d",
  "sessionId": "99513a19-7109-43ba-90b7-1799724932fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cached-moseying-feather",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012L8bkfd7m4gkEEApM2yZew",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 25762,
      "cache_read_input_tokens": 0,
      "output_tokens": 350,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 25762
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 350,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 25762,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 25762,
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

_source line 11 · 2026-05-22T12:01:06.393Z_

<details><summary>↩ Tool result · `toolu_01WRZSXKqgaAdrhRVYh3Bb8d`</summary>

```text
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
49	$^\dagger$Mistral: poor zero-shot calibration causes pervasive type inconsistencies.
50	F1 $\times$100.}
51	\label{tab:cross-model}
52	\end{table}
53	
54	% exp_ids: phase2_scierc_full_s1, llama_scierc_full_s1, phase2_docred_full_s1, llama_docred_full_s1, mistral_scierc, mistral_docred
55	\paragraph{Results.}
56	RV and ET reach $\leq$0.03\% for all models on both datasets.
57	DR drops 76--99\% on SciERC and 42--90\% on DocRED; R-F1 improves in 5/6 settings.
58	CF direction depends on calibration: S1 introduces CF for calibrated models (up to 12.02\%; \S\ref{sec:discussion}) but reduces it for Mistral (56.87\%\,$\to$\,1.27\%; poor entity typing limits DR reduction to 42\%); fine-tuning resolves both (\S\ref{sec:composability}).
59	
60	\paragraph{Post-hoc filtering comparison.}
61	Post-hoc filtering achieves DR${=}$0\% but with 15--74\% rejection rates (DocRED Qwen: 48\% discarded); under fine-tuning, both achieve comparable F1 (Appendix~\ref{app:posthoc-extended}).
62	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7af0abb1-8a09-44ab-a493-3be92db058c5",
  "isSidechain": true,
  "promptId": "14fc01a8-031f-4ceb-ad2f-39c6c6b967ca",
  "agentId": "ad6a42899911fc70c",
  "type": "user",
  "uuid": "ad252e64-9d51-4f8d-9200-6bfddc39c1df",
  "sourceToolAssistantUUID": "7af0abb1-8a09-44ab-a493-3be92db058c5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/reviewer_17ad4b4d",
  "sessionId": "99513a19-7109-43ba-90b7-1799724932fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cached-moseying-feather"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-22T12:01:09.301Z_

Now let me read the method section and limitations.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ad252e64-9d51-4f8d-9200-6bfddc39c1df",
  "isSidechain": true,
  "agentId": "ad6a42899911fc70c",
  "requestId": "req_011CbHa6cxFWxhdaL8V4BYW2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c7e77824-6777-4a66-b408-16d495d37d76",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/reviewer_17ad4b4d",
  "sessionId": "99513a19-7109-43ba-90b7-1799724932fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cached-moseying-feather",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014CyQoJXaJHL6ZGN3h8xe64",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8070,
      "cache_read_input_tokens": 25762,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8070,
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

_source line 13 · 2026-05-22T12:01:10.905Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01PT5XwKy4YyUdboxAzcoh8c`</summary>

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
  "recorded_role": "assistant",
  "parentUuid": "c7e77824-6777-4a66-b408-16d495d37d76",
  "isSidechain": true,
  "agentId": "ad6a42899911fc70c",
  "requestId": "req_011CbHa6cxFWxhdaL8V4BYW2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7d261f14-4c08-47e3-b334-c7c2b5918652",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/reviewer_17ad4b4d",
  "sessionId": "99513a19-7109-43ba-90b7-1799724932fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cached-moseying-feather",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014CyQoJXaJHL6ZGN3h8xe64",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8070,
      "cache_read_input_tokens": 25762,
      "output_tokens": 117,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8070
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 117,
          "cache_read_input_tokens": 25762,
          "cache_creation_input_tokens": 8070,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8070,
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

_source line 14 · 2026-05-22T12:01:10.930Z_

<details><summary>↩ Tool result · `toolu_01PT5XwKy4YyUdboxAzcoh8c`</summary>

```text
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
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_full_ft.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_scalability.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/case_study_kappa_dr.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_pumping_lemma.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section2_background.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_method_draft.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_violation_landscape.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section4_composition_draft.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_kappa_case_study.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_tcr.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_prompt_sensitivity.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_case_studies.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/fig1_framework.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/checklist.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_crossmodel_draft.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section1_introduction_draft.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion_compressed.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_reproducibility.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_llama_per_relation.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_sampling_table.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_doc_length.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_beam_search.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_wikievents_draft.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_runtime.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7d261f14-4c08-47e3-b334-c7c2b5918652",
  "isSidechain": true,
  "promptId": "14fc01a8-031f-4ceb-ad2f-39c6c6b967ca",
  "agentId": "ad6a42899911fc70c",
  "type": "user",
  "uuid": "fb5b60af-fa97-4bd8-adae-4bb874bd4825",
  "sourceToolAssistantUUID": "7d261f14-4c08-47e3-b334-c7c2b5918652",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/reviewer_17ad4b4d",
  "sessionId": "99513a19-7109-43ba-90b7-1799724932fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cached-moseying-feather"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-22T12:01:14.566Z_

<details open><summary>🔧 Tool call — Read · `toolu_016ZkU6QmeA2oMo9Kba9Ango`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_method_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fb5b60af-fa97-4bd8-adae-4bb874bd4825",
  "isSidechain": true,
  "agentId": "ad6a42899911fc70c",
  "requestId": "req_011CbHa6xffiquNBqtffYLDQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "54645a80-25b9-41ed-9ec3-a839307f2b89",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/reviewer_17ad4b4d",
  "sessionId": "99513a19-7109-43ba-90b7-1799724932fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cached-moseying-feather",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WxqZvFpCWkX6MyJM3xsPYm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2216,
      "cache_read_input_tokens": 33832,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2216,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 72,
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

_source line 16 · 2026-05-22T12:01:14.572Z_

<details><summary>↩ Tool result · `toolu_016ZkU6QmeA2oMo9Kba9Ango`</summary>

```text
1	% Section 3 — Method (Draft)
2	% OntoCoDec: Type-Valid Information Extraction
3	% via Compiled Ontology Constraints
4	
5	\section{Method}
6	\label{sec:method}
7	
8	\input{fig1_framework}
9	
10	We present OntoCoDec, a framework that translates IE ontologies into token-level constraints enforced during autoregressive generation.
11	The design is guided by a decidability analysis of IE type constraints.
12	
13	\paragraph{Constraint decidability taxonomy.}
14	\label{sec:decidability}
15	We classify IE type constraints into three levels: (1)~\emph{context-free}: vocabulary membership and JSON structure; (2)~\emph{prefix-decidable with state}: domain/range type validity, determined at each type-bearing position given the decoded relation type and entity registry; (3)~\emph{non-local}: cross-entity type consistency, which depends on the full output.
16	Unlike code generation where types are statically declared, IE constraints fall into level~2: entity types are inferred from text, the registry is built dynamically, and constraint targets depend on the co-occurring relation.
17	OntoCoDec enforces levels 1--2 (grammar and semantic layers, respectively); level~3 is addressed by beam search or post-hoc resolution (Appendix~\ref{app:tcr}).
18	
19	\smallskip
20	\noindent
21	Existing grammar-constrained decoding frameworks (e.g., XGrammar) enforce level~1 constraints---structural validity and vocabulary membership---but IE domain/range rules require cross-position entity-type state that context-free grammars cannot express.
22	We formalize this gap:
23	
24	\smallskip
25	\noindent\textbf{Proposition 1} (Level 2 $\not\subseteq$ Level 1)\textbf{.}
26	\textit{Domain/range type constraints for IE with unbounded entity sets are not context-free.}
27	
28	\smallskip
29	\noindent\textit{Proof sketch.}
30	Consider $\mathcal{E} = \{\tau_A, \tau_B\}$ and a relation $r$ with $\operatorname{dom}(r) = \{\tau_A\}$.
31	An output contains $n$ entities with independently chosen types, followed by a relation referencing head $e_k$ for arbitrary $k \leq n$.
32	A PDA's LIFO stack cannot retrieve position $k < n$ without destroying entries above it; since both $n$ and $k$ are independently unbounded, no PDA can enforce this constraint.
33	OntoCoDec's semantic layer addresses this with a runtime entity registry $\mathcal{D}$ (a finite map enabling random-access type lookups).
34	For finite entity sets, the valid language is technically regular but the corresponding DFA requires $O(|\mathcal{E}|^{|\text{entities}|})$ states---exceeding $10^{17}$ for DocRED (7 entity types, 20+ entities per document)---making direct DFA construction infeasible and motivating the grammar-based approach (Appendix~\ref{app:pumping-lemma}).\hfill$\square$
35	
36	\noindent\textbf{Corollary} (empirical enabling dependency: a constraint whose satisfaction is a prerequisite for evaluating subsequent constraints)\textbf{.} The empirical enabling dependency is necessary: the grammar layer alone cannot enforce domain/range constraints (Proposition~1), while the semantic layer alone achieves only 24\% DR reduction without grammar-enforced vocabulary membership (\S\ref{sec:scierc-results}, Table~\ref{tab:scierc-ablation}).
37	\smallskip
38	
39	We describe the problem formulation (\S\ref{sec:formulation}), each layer, and two decoding strategies (\S\ref{sec:strategies}); formal analysis of constraint composition is in Section~\ref{sec:composition}.
40	
41	
42	\subsection{Problem Formulation}
43	\label{sec:formulation}
44	
45	\paragraph{IE as structured generation.}
46	Given an input text $x$, a language model generates a structured JSON output $y$:
47	%
48	\begin{equation}\label{eq:output-schema}
49	\resizebox{.88\columnwidth}{!}{$\displaystyle
50	  y = \bigl\{\texttt{entities}: [\{n_i, \tau_i\}],\; \texttt{relations}: [\{h_j, t_j, r_j, \tau^h_j, \tau^t_j\}]\bigr\}
51	$}
52	\end{equation}
53	%
54	where each entity has a name $n_i$ and type $\tau_i \in \mathcal{E}$, and each relation specifies head $h_j$, tail $t_j$, relation type $r_j \in \mathcal{R}$, and head/tail entity types $\tau^h_j, \tau^t_j$.
55	The output JSON Schema (\S\ref{sec:grammar}) enforces a fixed field ordering (head $\to$ tail $\to$ relation $\to$ head\_type $\to$ tail\_type) via deterministic grammar compilation, ensuring the relation type $r_j$ is known before entity type fields and enabling sequential domain/range lookups (\S\ref{sec:dynamic-masking}).
56	The grammar structurally enforces entity-before-relation ordering (100\% preservation across all configurations), ensuring the entity registry (\S\ref{sec:entity-registry}) is populated before relation-level type constraints are evaluated; unregistered entities trigger domain-only filtering.
57	
58	\paragraph{Ontology compliance.}
59	Using the ontology $\mathcal{O} = (\mathcal{E}, \mathcal{R}, \sigma)$ defined in \S\ref{sec:background}, we write $\operatorname{dom}(r) = \{\tau^h : \exists \tau^t,\, (\tau^h, \tau^t) \in \sigma(r)\}$ for domain-valid head types and $\operatorname{range}(r, \tau^h) = \{\tau^t : (\tau^h, \tau^t) \in \sigma(r)\}$ for the conditional range given head type $\tau^h$.
60	Our enforcement target is \emph{pair-based} type validity: $(\tau^h, \tau^t) \in \sigma(r)$ for every triple.
61	The decoder enforces this sequentially: $\tau^h \in \operatorname{dom}(r)$ at head position, then $\tau^t \in \operatorname{range}(r, \tau^h)$ at tail position, achieving best-effort pair-based enforcement (pair validity ensured when no fallback is triggered; domain-only filtering otherwise) strictly stronger than independent domain/range checks (which over-permit 33--37\% spurious pairs on SciERC/DocRED; \S\ref{sec:rectangularity}).
62	
63	
64	\subsection{Grammar Layer}
65	\label{sec:grammar}
66	
67	A JSON Schema encoding Eq.~\eqref{eq:output-schema} with \texttt{enum} constraints ($\mathcal{E}$, $\mathcal{R}$) is compiled into a pushdown automaton via XGrammar~\cite{dong2025xgrammar}.
68	At step $t$, grammar-valid tokens $G(t) \subseteq V$ pass; all others receive logits $-\infty$, enforcing structural validity, vocabulary membership ($r_j \in \mathcal{R}$, $\tau_i \in \mathcal{E}$), but not domain/range constraints (which depend on entity types within each triple).
69	
70	\subsection{Semantic Layer}
71	\label{sec:semantic}
72	
73	The semantic layer enforces domain/range constraints through a stateful logits processor maintaining an entity registry during generation.
74	
75	\paragraph{Entity registry.}
76	\label{sec:entity-registry}
77	The semantic layer builds a registry $\mathcal{D}: \text{name} \to \text{type}$ incrementally during entity generation: each completed entry $\{n_i, \tau_i\}$ adds $(n_i, \tau_i)$ to $\mathcal{D}$, which is consulted during relation generation for type lookups.
78	At each step $t$, the processor pattern-matches the decoded prefix to identify the current field position; semantic masks activate only at type-bearing positions (\textsc{HeadType}, \textsc{TailType}).
79	\label{sec:position-detection}
80	
81	\paragraph{Dynamic masking.}
82	\label{sec:dynamic-masking}
83	At type-bearing positions, the processor computes a semantic mask $S(t) \subseteq V$.
84	At a \textsc{HeadType} position, if $h_j \in \mathcal{D}$ and $\mathcal{D}[h_j] \in \operatorname{dom}(r_j)$, the mask allows only the registered type; otherwise it falls back to all domain-valid types $\operatorname{dom}(r_j)$.
85	At a \textsc{TailType} position, the mask restricts to $\operatorname{range}(r_j, \tau^h_j)$ conditioned on the already-determined head type, further narrowing to the registered type when $t_j \in \mathcal{D}$.
86	This sequential check achieves best-effort pair-based enforcement (\S\ref{sec:formulation}), strictly tighter than independent domain/range checking; ``best-effort'' reflects the grammar-first fallback (\S\ref{sec:composition}), which prioritizes JSON integrity over type validity when constraints conflict.
87	
88	\paragraph{Tokenizer-agnostic type masking.}
89	We use \emph{continuation masking} to handle context-dependent tokenizations and prefix-shared types (e.g., \textsc{Sen}/\textsc{Sid}/\textsc{Side} in WikiEvents): a compile-time prefix map identifies valid continuations for each type name, disambiguating over multiple steps across byte-level BPE (Qwen, Llama) and SentencePiece (Mistral).
90	
91	\paragraph{Grammar-semantic interaction.}
92	\label{sec:interaction}
93	The final mask is $G(t) \cap S(t)$; when empty, grammar-first fallback applies (\S\ref{sec:composition}), embodying the empirical enabling dependency: semantic constraints reduce DR by only 24\% without grammar-enforced vocabulary.
94	
95	
96	\subsection{Decoding Strategies}
97	\label{sec:strategies}
98	
99	\paragraph{S1 (joint extraction): Single-pass decoding.}
100	Both layers are active throughout generation; the entity registry populates during entity decoding and is immediately available for relation-level type checking.
101	
102	\paragraph{S2 (two-pass pipeline): Two-pass decoding.}\label{sec:s2}
103	A first pass extracts entities; these compile an input-dependent grammar for the second pass.
104	S1 achieves higher R-F1 at comparable DR (\S\ref{sec:scierc-results}) and is the primary configuration.
105	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "54645a80-25b9-41ed-9ec3-a839307f2b89",
  "isSidechain": true,
  "promptId": "14fc01a8-031f-4ceb-ad2f-39c6c6b967ca",
  "agentId": "ad6a42899911fc70c",
  "type": "user",
  "uuid": "7e5942d5-dc55-4566-bc34-1caadc1dbbde",
  "sourceToolAssistantUUID": "54645a80-25b9-41ed-9ec3-a839307f2b89",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/reviewer_17ad4b4d",
  "sessionId": "99513a19-7109-43ba-90b7-1799724932fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cached-moseying-feather"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-22T12:01:15.093Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Qd8zGWE5fnCSsEnqQAnW49`</summary>

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
  "parentUuid": "7e5942d5-dc55-4566-bc34-1caadc1dbbde",
  "isSidechain": true,
  "agentId": "ad6a42899911fc70c",
  "requestId": "req_011CbHa6xffiquNBqtffYLDQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "332d7107-e266-4687-835b-3477f85f31e1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/reviewer_17ad4b4d",
  "sessionId": "99513a19-7109-43ba-90b7-1799724932fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cached-moseying-feather",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WxqZvFpCWkX6MyJM3xsPYm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2216,
      "cache_read_input_tokens": 33832,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2216,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 72,
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

_source line 18 · 2026-05-22T12:01:15.101Z_

<details><summary>↩ Tool result · `toolu_01Qd8zGWE5fnCSsEnqQAnW49`</summary>

```text
1	% Section 7 — Discussion and Conclusion
2	
3	OntoCoDec translates IE ontologies into composable token-level constraints via a two-layer architecture: LoRA + greedy S1 achieves DR\,$\leq$\,0.09\% ($<$0.5\% recall cost), CF\,$\leq$\,1.4\%; beam ($k{=}4$) eliminates all violations on SciERC (1.54$\times$ latency); zero-shot DR drops 42--99\% across models and datasets (7--8B; 70B LoRA in \S\ref{sec:70b-results}); triple validity analysis (\S\ref{sec:downstream-impact}) confirms 100\% schema compliance.
4	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "332d7107-e266-4687-835b-3477f85f31e1",
  "isSidechain": true,
  "promptId": "14fc01a8-031f-4ceb-ad2f-39c6c6b967ca",
  "agentId": "ad6a42899911fc70c",
  "type": "user",
  "uuid": "6b1f8658-c5d6-4613-a5c6-2a50c061257f",
  "sourceToolAssistantUUID": "332d7107-e266-4687-835b-3477f85f31e1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/reviewer_17ad4b4d",
  "sessionId": "99513a19-7109-43ba-90b7-1799724932fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cached-moseying-feather"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-22T12:01:16.032Z_

<details open><summary>🔧 Tool call — Read · `toolu_01GiAZAAruPLbzkTpk4UzWZM`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section4_composition_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6b1f8658-c5d6-4613-a5c6-2a50c061257f",
  "isSidechain": true,
  "agentId": "ad6a42899911fc70c",
  "requestId": "req_011CbHa6xffiquNBqtffYLDQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3b3c6ea8-05d7-4066-a0f7-44c1d1a38af5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/reviewer_17ad4b4d",
  "sessionId": "99513a19-7109-43ba-90b7-1799724932fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cached-moseying-feather",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WxqZvFpCWkX6MyJM3xsPYm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2216,
      "cache_read_input_tokens": 33832,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2216,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 72,
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

_source line 20 · 2026-05-22T12:01:16.039Z_

<details><summary>↩ Tool result · `toolu_01GiAZAAruPLbzkTpk4UzWZM`</summary>

```text
1	% Section: Constraint Composition (compressed, 787→~500 words)
2	
3	At each decoding step $t$, let $G(t) \subseteq V$ and $S(t) \subseteq V$ denote the tokens permitted by the grammar and semantic layers, respectively.
4	The final mask is their conjunction:
5	%
6	\begin{equation}\label{eq:composition}
7	  M_{\text{final}}(t) = M_{\text{grammar}}(t) \;\wedge\; M_{\text{semantic}}(t),
8	\end{equation}
9	%
10	where $\wedge$ denotes element-wise AND over the vocabulary $V$; a token is allowed only if it satisfies \emph{both} structural and type-level constraints.
11	The conjunction is asymmetric: $S(t)$ is defined only over $G(t)$. This reflects the empirical enabling dependency (\S\ref{sec:method}): the semantic layer requires the relation type to belong to $\mathcal{R}$, a property enforced only by the grammar layer.
12	
13	\paragraph{Grammar-First Fallback.}
14	When $S(t) \cap G(t) = \emptyset$ (tight constraints leave no token that is both grammar-valid and semantically valid), na\"{\i}ve masking would force selection of a grammar-invalid token, breaking JSON structure.
15	We enforce a \emph{grammar-first fallback}: semantic masking is skipped and the grammar layer alone controls selection.
16	Structural integrity is a hard constraint; type violations are soft errors detectable by downstream validation, with DR (ontologically invalid type pair) more severe than CF (individually valid triples with cross-triple type inconsistency).
17	
18	\paragraph{Constraint Tightness.}
19	\label{eq:tightness}
20	We define per-relation constraint tightness $\kappa(r) = 1 - |\sigma(r)|/|\mathcal{E}|^2$ and the schema-level mean $\bar{\kappa} = \frac{1}{|\mathcal{R}|}\sum_{r} \kappa(r)$.
21	Across three schemas---WikiEvents ($\bar{\kappa}{=}0.029$), SciERC ($\bar{\kappa}{=}0.333$), DocRED ($\bar{\kappa}{=}0.842$)---DR reduction ranges from 94--99\% (low $\bar{\kappa}$) to 42--90\% (high $\bar{\kappa}$); entity type confusability is a critical co-factor (Appendix~\ref{app:kappa-case-study},~\ref{app:tcr}).
22	
23	\paragraph{Greedy limitation and fallback cascade.}
24	\label{sec:greedy-limitation}
25	The semantic layer commits entity types greedily---an instance of Level~3 (non-local) constraints (\S\ref{sec:decidability})---so CF violations arise when the same entity receives different types across triples; beam search mitigates this in favorable configurations (\S\ref{sec:beam-results}).
26	Grammar-first fallback triggers on 0.5--5.7\% of type-bearing positions under zero-shot decoding, correlating with $\bar{\kappa}$; fine-tuning virtually eliminates fallback ($\leq$\,0.11\%), transitioning the semantic layer from primary enforcer to safety net.
27	Causal tracing confirms all residual DR occurs exclusively at fallback positions (Appendix~\ref{app:causal-tracing}).
28	
29	\paragraph{Non-rectangularity and independent enforcement.}
30	\label{sec:rectangularity}
31	Type signatures are non-rectangular (0/7 SciERC, 23/96 DocRED rectangular); independent enforcement is a sound over-approximation admitting 33--37\% spurious pairs; fine-tuning eliminates all residual DR (Table~\ref{tab:composability}).
32	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3b3c6ea8-05d7-4066-a0f7-44c1d1a38af5",
  "isSidechain": true,
  "promptId": "14fc01a8-031f-4ceb-ad2f-39c6c6b967ca",
  "agentId": "ad6a42899911fc70c",
  "type": "user",
  "uuid": "7bfc039c-1fa8-4a71-b67a-1e8bc6b303bc",
  "sourceToolAssistantUUID": "3b3c6ea8-05d7-4066-a0f7-44c1d1a38af5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/reviewer_17ad4b4d",
  "sessionId": "99513a19-7109-43ba-90b7-1799724932fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cached-moseying-feather"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-22T12:01:16.266Z_

<details open><summary>🔧 Tool call — Read · `toolu_01UbW1uTMioEg2q33c41zEdi`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_wikievents_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7bfc039c-1fa8-4a71-b67a-1e8bc6b303bc",
  "isSidechain": true,
  "agentId": "ad6a42899911fc70c",
  "requestId": "req_011CbHa6xffiquNBqtffYLDQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4ef9af3c-d7c5-487d-905d-cfd2318d22cb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/reviewer_17ad4b4d",
  "sessionId": "99513a19-7109-43ba-90b7-1799724932fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cached-moseying-feather",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WxqZvFpCWkX6MyJM3xsPYm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2216,
      "cache_read_input_tokens": 33832,
      "output_tokens": 339,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2216
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 339,
          "cache_read_input_tokens": 33832,
          "cache_creation_input_tokens": 2216,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2216,
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

_source line 22 · 2026-05-22T12:01:16.273Z_

<details><summary>↩ Tool result · `toolu_01UbW1uTMioEg2q33c41zEdi`</summary>

```text
1	% Section 5 — Event Extraction on WikiEvents (compact, inline)
2	% exp_ids: ee_qwen_wikievents_unconstrained, ee_llama_wikievents_unconstrained,
3	%          ee_mistral_wikievents_unconstrained, ee_qwen_wikievents_constrained,
4	%          ee_llama_wikievents_constrained, ee_mistral_wikievents_constrained_v2
5	% v3 final data confirmed by Director 2026-05-18.
6	
7	\subsection{Extension to Event Extraction}
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
34	  & S1    & \textbf{0} & \textbf{0} & 2.1 & 21.1 & 13.4 & 14.1 \\
35	\midrule
36	\multirow{3}{*}{\shortstack[l]{Llama\\3.1-8B}}
37	  & Unconstr.\ & 10.5 & 88.8 & 0.1 & 0 & 5.7 & 0 \\
38	  & Grammar    & \textbf{0} & 77.0 & 8.8 & --- & --- & --- \\
39	  & S1    & \textbf{0} & \textbf{0} & 3.8 & 17.2 & 7.5 & 17.6 \\
40	\midrule
41	\multirow{3}{*}{\shortstack[l]{Mistral\\7B}}
42	  & Unconstr.\ & 37.3 & 63.9 & 0 & 0 & 2.4 & 0 \\
43	  & Grammar    & \textbf{0} & 64.0 & 13.8 & --- & --- & --- \\
44	  & S1    & \textbf{0} & \textbf{0} & 1.3 & 14.9 & 3.9 & 11.7 \\
45	\bottomrule
46	\end{tabular}}%
47	\caption{WikiEvents EE results. Zero-shot rows (n$=$246): full WikiEvents corpus; fine-tuning (\S\ref{sec:wikievents}, n$=$20): standard 194/20/20 split~\cite{li2021document}.
48	Violation rates over parsed documents.
49	\textemdash{} indicates not applicable (grammar-only has no semantic-layer metrics).
50	F1 $\times$ 100. Fine-tuning results are preliminary given the small test set ($n{=}20$); bootstrap 95\% CIs for argument F1 span approximately $\pm$3--5\,pp.}
51	\label{tab:wikievents}
52	\end{table}
53	
54	\paragraph{Results.}
55	Unconstrained EE produces extreme vocabulary violations (EV+RoV $>$85\%; Table~\ref{tab:wikievents}), with entity F1\,=\,0 because the parser cannot process off-schema output.
56	S1 eliminates EV and RoV across all models, which validates the tokenizer-agnostic design across byte-level BPE and SentencePiece.
57	Grammar-only eliminates EV but leaves RoV at 64--77\% and surfaces latent AC (8--14\%), consistent with DocRED's pattern (\S\ref{sec:docred-results}); S1 drives RoV to 0\%.
58	Residual AC (1.3--3.8\%) traces to semantically similar types (e.g., SID vs.\ SEN).
59	CF rises to 15--21\%, exceeding RE levels (10--12\%) because EE's multi-argument structures increase entity reuse across slots.
60	Post-hoc filtering is impractical ($<$0.5\% arguments retained).
61	Unlike RE, EE shows measurable F1 gains: entity F1 0\%\,$\to$\,12--18\%, trigger F1 $+$1.5--1.8\,pp.
62	
63	% exp_ids: p1_ee_ft_qwen_wikievents_r5, p1_ee_ft_llama_wikievents_r5
64	\paragraph{Composability with fine-tuning (preliminary, $n{=}20$).}
65	On the full official test split (20 documents; 194/20/20~\cite{li2021document}), LoRA + S1 eliminates RoV (Qwen 38.31\%\,$\to$\,0\%, Llama 8.8\%\,$\to$\,0\%) and reduces AC to $\leq$0.8\%, with argument F1 within $\pm$1.1\,pp; trigger F1 shifts ($-$5.4/$-$0.6\,pp) have wide CIs consistent with n${=}$20.
66	CF remains low (0.77--1.18\%); per-document variance is high (Arg-F1 std/mean ${>}$\,0.5), confirming sufficient power to detect violation elimination but not small F1 differences.
67	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4ef9af3c-d7c5-487d-905d-cfd2318d22cb",
  "isSidechain": true,
  "promptId": "14fc01a8-031f-4ceb-ad2f-39c6c6b967ca",
  "agentId": "ad6a42899911fc70c",
  "type": "user",
  "uuid": "b2298835-9e6d-4369-8fb1-9d6f69bf5cfb",
  "sourceToolAssistantUUID": "4ef9af3c-d7c5-487d-905d-cfd2318d22cb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/reviewer_17ad4b4d",
  "sessionId": "99513a19-7109-43ba-90b7-1799724932fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cached-moseying-feather"
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-22T12:01:19.716Z_

Now let me read the discussion/limitations, introduction, and the DocRED section for additional context.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b2298835-9e6d-4369-8fb1-9d6f69bf5cfb",
  "isSidechain": true,
  "agentId": "ad6a42899911fc70c",
  "requestId": "req_011CbHa7MBW7qLRMBivsVuGn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2d070307-dbc2-45ed-aff9-b0ebd267206a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/reviewer_17ad4b4d",
  "sessionId": "99513a19-7109-43ba-90b7-1799724932fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cached-moseying-feather",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DmRhJqzD2GP6Don3T62bBR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6390,
      "cache_read_input_tokens": 36048,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6390,
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

_source line 24 · 2026-05-22T12:01:21.734Z_

<details open><summary>🔧 Tool call — Read · `toolu_01PEMxtXNKRp17itpyYdGjHK`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/discussion_paragraphs.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2d070307-dbc2-45ed-aff9-b0ebd267206a",
  "isSidechain": true,
  "agentId": "ad6a42899911fc70c",
  "requestId": "req_011CbHa7MBW7qLRMBivsVuGn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "183f77f5-bb45-417d-9680-932714648d18",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/reviewer_17ad4b4d",
  "sessionId": "99513a19-7109-43ba-90b7-1799724932fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cached-moseying-feather",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DmRhJqzD2GP6Don3T62bBR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6390,
      "cache_read_input_tokens": 36048,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6390,
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

_source line 25 · 2026-05-22T12:01:21.742Z_

<details><summary>↩ Tool result · `toolu_01PEMxtXNKRp17itpyYdGjHK`</summary>

```text
1	% Discussion paragraphs for §7
2	% Three standalone paragraphs: (1) Low F1 practical significance,
3	% (2) CF severity argument, (3) F1 significance difference explanation.
4	% All quantitative claims traced to registry exp_ids.
5	
6	%%% Paragraph 1: Low F1 Practical Significance %%%
7	% exp_ids: phase2_scierc_full_s1 (R-F1=8.36%), phase2_docred_full_s1 (R-F1=8.23%),
8	%          phase0_scierc_unconstrained (DR=15.37%), phase2_docred_unconstrained (DR=18.46%)
9	
10	\paragraph{Practical Significance of Zero-Shot F1.}
11	Our reported relation F1 of approximately 8\% on both SciERC and DocRED reflects the inherent difficulty of zero-shot closed IE, where the model receives no task-specific training examples.
12	For reference, supervised state-of-the-art systems on SciERC achieve approximately 49--53\% relation F1 with full training data~\citep{zhong2021frustratingly,ye2022packed}.
13	Constraint enforcement operates largely independently of the extraction model's intrinsic capability: it restricts the output space to ontologically valid triples regardless of the underlying model's accuracy.
14	When applied to fine-tuned models that reach competitive F1 levels, the same constraints remain necessary---Phase~0 analysis confirms that even well-prompted models exhibit non-trivial violation rates (15.37\% DR on SciERC, 18.46\% on DocRED).
15	% exp_ids: phase0_scierc_unconstrained, phase2_docred_unconstrained
16	In our evaluation, F1 serves as a \emph{control variable} verifying that constraint enforcement does not degrade extraction quality, not as an optimization target.
17	The contribution of this work is the constraint enforcement method itself; the zero-shot setting isolates its effect from confounds introduced by task-specific fine-tuning.
18	
19	%%% Paragraph 2: CF Severity Argument %%%
20	% exp_ids: phase2_scierc_full_s1 (CF=9.90%), phase2_scierc_grammar_only (CF=0.08%),
21	%          phase2_docred_full_s1 (CF=2.57%)
22	
23	\paragraph{Severity of Cross-Field Violations.}
24	Domain/range (DR) violations produce structurally invalid triples---a triple asserting that a \emph{Task} entity fills the \emph{domain} slot of \textsc{Part-of}, which requires \emph{Method}, cannot be consumed by any downstream system without error.
25	DR violations are therefore hard constraints.
26	Cross-field consistency (CF) violations are qualitatively different: each individual triple remains type-valid with respect to its own relation's domain/range rules; only cross-triple consistency is broken when the same entity receives different types across relations.
27	The dominant conflict pattern---\emph{Generic}$\leftrightarrow$\emph{OtherScientificTerm} (60 of 245~affected entities on SciERC)---reflects genuine semantic ambiguity in the type system rather than a systematic method failure.
28	% exp_id: phase2_scierc_full_s1
29	Ablation evidence cleanly attributes CF to the semantic layer: grammar-only decoding yields CF\,=\,0.08\%, matching the unconstrained baseline, while the full system reaches 9.90\% on SciERC and 2.57\% on DocRED
30	(Qwen3-8B; Llama-3.1-8B exhibits 12.02\% on DocRED, the highest across all configurations).
31	% exp_ids: phase2_scierc_grammar_only, phase2_docred_full_s1
32	% llama_docred_full_s1: CF=0.1202
33	This arises from per-relation independent enforcement, where each relation's constraint mask is computed without access to type decisions made for other relations.
34	A natural extension is a global entity-level type consensus pass that resolves entity types before relation-specific enforcement.
35	
36	%%% Paragraph 3: F1 Significance Difference Explanation %%%
37	% exp_ids: d012_bootstrap_ci (DocRED +0.50pp p<0.001, SciERC +0.13pp p=0.58),
38	%          phase0_docred_unconstrained (RV=29.66%), phase0_scierc_unconstrained (RV=1.39%)
39	
40	\paragraph{Dataset-Dependent F1 Impact.}
41	The divergence in F1 significance between DocRED ($+$0.50\,pp, $p < 0.001$, 95\% CI [$+$0.23, $+$0.81]) and SciERC ($+$0.13\,pp, $p = 0.58$, 95\% CI [$-$0.24, $+$0.58]) traces to a single mechanism: grammar-layer elimination of out-of-vocabulary (OOV) relation names.
42	% exp_id: d012_bootstrap_ci
43	Under the all-valid-set evaluation protocol, a predicted triple whose relation name does not appear in the ontology is counted as a false positive.
44	The DocRED baseline exhibits a relation-vocabulary (RV) violation rate of 29.66\%---5{,}189 predictions with OOV relation names---all of which become false positives under this protocol.
45	% exp_id: phase0_docred_unconstrained
46	The grammar layer eliminates these OOV predictions, removing a substantial source of false positives and yielding a statistically significant precision gain.
47	On SciERC, the baseline RV rate is only 1.39\% (24~OOV predictions), too few to produce a detectable F1 effect.
48	% exp_id: phase0_scierc_unconstrained
49	The F1 improvement on DocRED is thus a direct, mechanistically transparent consequence of vocabulary enforcement at scale, not an artifact of constraint-induced distribution shift.
50	Llama-3.1-8B's lower baseline RV (16.03\% vs.\ Qwen's 29.66\%)
51	results in fewer OOV predictions eliminated by the grammar layer,
52	yielding a smaller but directionally consistent R-F1 improvement
53	($+$0.29\,pp vs.\ $+$0.50\,pp), confirming that the magnitude of
54	F1 gain is proportional to the baseline OOV rate.
55	% llama_docred_unconstrained: RV=0.1603, R-F1=5.98
56	% llama_docred_full_s1: RV=0, R-F1=6.27, delta=+0.29pp
57	% qwen_docred: RV=0.2966, R-F1 delta=+0.50pp
58	
59	%%% Paragraph 4: Decoding-Time vs. Post-Hoc Enforcement %%%
60	% exp_ids: posthoc_filtering_baseline, phase2_scierc_full_s1 (R-F1=8.36%),
61	%          phase2_docred_full_s1 (R-F1=8.23%, ET=0%)
62	
63	\paragraph{Decoding-Time vs.\ Post-Hoc Enforcement.}
64	Post-hoc filtering---generating triples without constraints, then removing schema-violating predictions---yields higher precision and consequently higher F1 than OntoCoDec on both datasets (SciERC 8.63 vs.\ 8.36; DocRED 9.61 vs.\ 8.23).
65	% posthoc: SciERC F1=8.63, DocRED F1=9.61; OntoCoDec: SciERC R-F1=8.36, DocRED R-F1=8.23
66	However, this precision gain comes at substantial cost.
67	On DocRED, post-hoc filtering discards 48.1\% of all predicted triples, including 127 true positives (11.2\% of correct predictions), reducing recall from 9.46\% to 8.40\%.
68	% posthoc_docred: rejection=48.1%, tp_lost=127/1137, R: 9.46→8.40
69	Entity type violations remain unresolved (ET\,=\,2.47\% vs.\ OntoCoDec's 0\%), as filtering targets only domain/range and vocabulary violations.
70	% posthoc_docred: ET_residual=2.47%; phase2_docred_full_s1: ET=0%
71	OntoCoDec's decoding-time approach avoids this information loss by guiding generation toward compliant outputs rather than discarding non-compliant ones, preserving both recall and entity type validity.
72	The two strategies are complementary: post-hoc filtering can serve as an additional safety net for residual violations that decoding-time enforcement does not fully resolve.
73	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "183f77f5-bb45-417d-9680-932714648d18",
  "isSidechain": true,
  "promptId": "14fc01a8-031f-4ceb-ad2f-39c6c6b967ca",
  "agentId": "ad6a42899911fc70c",
  "type": "user",
  "uuid": "388c831f-1b27-4464-904a-905a71e809b7",
  "sourceToolAssistantUUID": "183f77f5-bb45-417d-9680-932714648d18",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/reviewer_17ad4b4d",
  "sessionId": "99513a19-7109-43ba-90b7-1799724932fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cached-moseying-feather"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-22T12:01:22.632Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Vg4cPJBetxt2pWekST4Prx`</summary>

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
  "parentUuid": "388c831f-1b27-4464-904a-905a71e809b7",
  "isSidechain": true,
  "agentId": "ad6a42899911fc70c",
  "requestId": "req_011CbHa7MBW7qLRMBivsVuGn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c4f13112-3617-4d93-8feb-0fee98200854",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/reviewer_17ad4b4d",
  "sessionId": "99513a19-7109-43ba-90b7-1799724932fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cached-moseying-feather",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DmRhJqzD2GP6Don3T62bBR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6390,
      "cache_read_input_tokens": 36048,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6390,
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

_source line 27 · 2026-05-22T12:01:22.639Z_

<details><summary>↩ Tool result · `toolu_01Vg4cPJBetxt2pWekST4Prx`</summary>

```text
1	% Section 1: Introduction (compressed, 669→~550 words)
2	
3	\section{Introduction}
4	\label{sec:introduction}
5	
6	Large language models are increasingly used for information extraction~\cite{li2023codeie,sainz2024gollie,wei2023zeroshot}, but when generating relation triples $(h, r, t)$, neither entity necessarily carries a type consistent with the ontology's domain/range constraints for $r$.
7	We call such outputs \emph{domain/range violations}: structurally valid triples that are ontologically invalid.
8	Violations persist across the capability spectrum: 15.4\% of triples on SciERC~\cite{luan2018scierc} and 18.5\% on DocRED~\cite{yao2019docred} under zero-shot decoding, and 0.5--2\% even after LoRA fine-tuning; rates correlate with schema restrictiveness (few valid type pairs per relation) rather than ontology or model scale.
9	At deployment-grade quality (R-F1 40--46\%), even 1--2\% residual violations compound across thousands of documents into systematic knowledge graph corruption, making reliable constraint enforcement necessary.
10	
11	Existing approaches leave a fundamental gap.
12	Schema-informed prompting reduces violations by 62\% on average but is per-relation unreliable (violations for \textsc{Evaluate-for} actually \emph{increase} by 5.8\,pp).
13	Grammar-constrained decoding~\cite{dong2025xgrammar,willard2023outlines,beurer-kellner2023lmql} ensures syntactic well-formedness but cannot encode cross-field semantic constraints.
14	Post-hoc filtering improves precision but discards up to 48\% of predictions including true positives (\S\ref{sec:cross-model}); at high rejection rates (e.g., Mistral DocRED 73.7\%), it becomes impractical.
15	Training-based approaches~\cite{sainz2024gollie,lu2022uie} internalize schema knowledge but provide only soft guidance without runtime enforcement; no method provides both semantic awareness and hard constraint enforcement.
16	
17	We propose \textbf{OntoCoDec}, a framework that translates IE ontologies into composable layers of decoding-time constraints.
18	A decidability analysis of IE type constraints (\S\ref{sec:decidability}) yields a two-layer architecture: the \emph{grammar layer} compiles ontology constraints into context-free grammars (JSON structure, vocabulary membership) via XGrammar; the \emph{semantic layer} interprets type constraints at runtime via dynamic logit masking over an entity registry, with an \emph{empirical enabling dependency} between layers.
19	OntoCoDec compiles constraints automatically from IE ontologies, requires no constraint-specific training, and is applicable to autoregressive LMs with logits access; we validate on three English datasets (up to 96 relation types), four models (7--70B), and three tokenizer families (Llama, Qwen, Mistral).
20	LoRA + greedy S1 achieves near-complete DR elimination: DR\,$\leq$\,0.09\% at R-F1 43--46\% ($\pm$0.8\,pp, $+$10\% latency); beam ($k{=}4$) eliminates all violation types on SciERC (1.54$\times$ latency).
21	DR enforcement converts ontologically invalid violations to individually valid but type-inconsistent ones (CF\,$\leq$\,1.4\% fine-tuned; \S\ref{sec:scierc-results}); zero-shot evaluation (7--70B) reveals DR drops 42--99\% across models and datasets, with 88--99\% on SciERC, but total violations (DR+CF) decrease by $\sim$31\%, reflecting conversion that fine-tuning resolves (\S\ref{sec:cross-model}).
22	
23	We make a systematic engineering contribution with theoretical grounding:
24	\begin{enumerate}[leftmargin=*,itemsep=2pt]
25	    \item A two-layer constrained decoding framework: we formalize a well-known intuition that cross-field type constraints require runtime state beyond context-free expressiveness (Proposition~1), yielding pair-based sequential enforcement at each level (\S\ref{sec:decidability}). Constraints compile automatically from IE ontologies, validated on schemas of varying restrictiveness with up to 96 relation types.
26	    \item A comprehensive evaluation across 3 IE datasets, 4 models (7--70B), and 2 tasks: under fine-tuning, DR\,$\leq$\,0.09\% at R-F1 43--46\% with CF\,$\leq$\,1.4\%; zero-shot ablation reveals an enabling dependency where on SciERC neither layer alone exceeds 24\% DR reduction (\S\ref{sec:scierc-results}); event extraction on WikiEvents validates applicability beyond RE (\S\ref{sec:wikievents}).
27	\end{enumerate}
28	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c4f13112-3617-4d93-8feb-0fee98200854",
  "isSidechain": true,
  "promptId": "14fc01a8-031f-4ceb-ad2f-39c6c6b967ca",
  "agentId": "ad6a42899911fc70c",
  "type": "user",
  "uuid": "4e86f762-0bf9-489f-816e-8d003d9b1420",
  "sourceToolAssistantUUID": "c4f13112-3617-4d93-8feb-0fee98200854",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/reviewer_17ad4b4d",
  "sessionId": "99513a19-7109-43ba-90b7-1799724932fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cached-moseying-feather"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-22T12:01:22.875Z_

<details open><summary>🔧 Tool call — Read · `toolu_01TANJFAinZmmZi6eBhyeXkM`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4e86f762-0bf9-489f-816e-8d003d9b1420",
  "isSidechain": true,
  "agentId": "ad6a42899911fc70c",
  "requestId": "req_011CbHa7MBW7qLRMBivsVuGn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bb4d7375-84c0-409b-8586-12280769e627",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/reviewer_17ad4b4d",
  "sessionId": "99513a19-7109-43ba-90b7-1799724932fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cached-moseying-feather",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DmRhJqzD2GP6Don3T62bBR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6390,
      "cache_read_input_tokens": 36048,
      "output_tokens": 279,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6390
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 279,
          "cache_read_input_tokens": 36048,
          "cache_creation_input_tokens": 6390,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6390,
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

_source line 29 · 2026-05-22T12:01:22.893Z_

<details><summary>↩ Tool result · `toolu_01TANJFAinZmmZi6eBhyeXkM`</summary>

```text
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
44	S1
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
55	F1 $\times$100. Bootstrap significance: R-F1 $+$0.50\,pp ($p < 0.001$).
56	Grammar-only $\uparrow$DR: vocabulary enforcement makes OOV outputs evaluable, exposing latent violations (see text).}
57	\label{tab:docred-ablation}
58	\end{table}
59	
60	% exp_ids: phase2_docred_unconstrained, phase2_docred_full_s1
61	\paragraph{Zero-shot diagnostic.}
62	S1 reduces DR from 18.46\% to 10.21\% ($\downarrow$45\%), eliminates ET ($\to$\,0\%), and eliminates RV (29.66\%\,$\to$\,0.03\%).\footnote{Residual 0.03\% RV traces to a rare XGrammar automaton edge case (chimeric subword tokens across enum entries); reported upstream.}
63	R-F1 improves from 7.74 to 8.23 ($+$0.50\,pp; $p < 0.001$), attributable to elimination of 5{,}189 OOV relation predictions.
64	CF increases from 0.10\% to 2.57\%, consistent with the CF$\leftrightarrow$DR trade-off (\S\ref{sec:discussion}).
65	Residual zero-shot DR (10.21\%) traces to grammar-first fallback under tight constraints ($\bar{\kappa}{=}0.842$; \S\ref{sec:greedy-limitation}); causal tracing confirms all residual DR occurs at fallback positions (Appendix~\ref{app:causal-tracing}).
66	
67	% exp_ids: phase2_docred_grammar_only, phase2_docred_semantic_only, phase2_docred_full_s1
68	\paragraph{Layer contributions.}
69	Grammar-only eliminates RV and ET but \emph{increases} DR to 26.17\%: vocabulary restriction makes OOV outputs evaluable, exposing latent type incompatibilities.
70	Semantic-only reduces DR by 25\% but cannot eliminate RV or ET, the same empirical enabling dependency observed on SciERC.
71	Residual DR (10.21\% vs.\ 0.93\% on SciERC) reflects high $\bar{\kappa}$ (0.842) and \textsc{Generic}$\leftrightarrow$X ambiguity; fine-tuning narrows DR to $\leq$\,0.09\% (Table~\ref{tab:composability}; residual decomposition in Appendix~\ref{app:residual-dr-analysis}).
72	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bb4d7375-84c0-409b-8586-12280769e627",
  "isSidechain": true,
  "promptId": "14fc01a8-031f-4ceb-ad2f-39c6c6b967ca",
  "agentId": "ad6a42899911fc70c",
  "type": "user",
  "uuid": "fdec30ef-0df1-4edf-b148-19ed2bc5faa0",
  "sourceToolAssistantUUID": "bb4d7375-84c0-409b-8586-12280769e627",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/reviewer_17ad4b4d",
  "sessionId": "99513a19-7109-43ba-90b7-1799724932fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cached-moseying-feather"
}
```

</details>

---

### Assistant

_source line 30 · 2026-05-22T12:01:26.353Z_

Now let me also check the checklist.tex and main.tex for limitations section:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fdec30ef-0df1-4edf-b148-19ed2bc5faa0",
  "isSidechain": true,
  "agentId": "ad6a42899911fc70c",
  "requestId": "req_011CbHa7qXpmkhfsC5zS8a6y",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9ba40ea2-d204-4f16-a61d-828c5684ac65",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/reviewer_17ad4b4d",
  "sessionId": "99513a19-7109-43ba-90b7-1799724932fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cached-moseying-feather",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MRKhmRJY2SBVrQTuPRWfZn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5524,
      "cache_read_input_tokens": 42438,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5524,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
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

_source line 31 · 2026-05-22T12:01:28.375Z_

<details open><summary>🔧 Tool call — Read · `toolu_01R6LTuYaFSEpR2Hq1RP85ju`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/checklist.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9ba40ea2-d204-4f16-a61d-828c5684ac65",
  "isSidechain": true,
  "agentId": "ad6a42899911fc70c",
  "requestId": "req_011CbHa7qXpmkhfsC5zS8a6y",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1e877e95-b5e4-4590-8f9b-9cfdd7d27aeb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/reviewer_17ad4b4d",
  "sessionId": "99513a19-7109-43ba-90b7-1799724932fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cached-moseying-feather",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MRKhmRJY2SBVrQTuPRWfZn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5524,
      "cache_read_input_tokens": 42438,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5524,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
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

_source line 32 · 2026-05-22T12:01:28.383Z_

<details><summary>↩ Tool result · `toolu_01R6LTuYaFSEpR2Hq1RP85ju`</summary>

```text
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
20	Yes. We use existing datasets (SciERC, DocRED, WikiEvents), pre-trained models (Qwen3-8B, Llama-3.1-8B, Mistral-7B, Llama-3.3-70B, Llama-3.1-70B), and software libraries (XGrammar, vLLM, PEFT).
21	
22	\begin{enumerate}[label=\textbf{B\arabic*.},leftmargin=2.5em]
23	\item \textbf{Did you cite the creators of artifacts you used?}
24	\\ Yes. All datasets, models, and libraries are cited in \S2, \S5, and Appendix~\ref{app:reproducibility}.
25	
26	\item \textbf{Did you discuss the license or terms for use and/or distribution of any artifacts?}
27	\\ Yes. SciERC (Apache 2.0), DocRED (MIT), WikiEvents (publicly released by \citet{li2021document}). Model licenses are noted in Appendix~\ref{app:reproducibility}.
28	
29	\item \textbf{Did you discuss if your use of existing artifacts was consistent with their intended use?}
30	\\ Yes. All datasets are used for their intended NLP evaluation purpose. Pre-trained models are used for inference and fine-tuning, consistent with their release terms.
31	
32	\item \textbf{Did you discuss the steps taken to check whether the data contains information that names or uniquely identifies individual people or offensive content?}
33	\\ N/A. We use established public benchmarks that have undergone prior review. No new data was collected.
34	
35	\item \textbf{Did you provide documentation of the artifacts?}
36	\\ Yes. Dataset statistics (relation/entity type counts, document counts, constraint tightness) are reported in \S2, \S5, and Appendix~\ref{app:wikievents}.
37	
38	\item \textbf{Did you report relevant statistics like the number of examples, details of train/test/dev splits, etc.?}
39	\\ Yes. SciERC: 551 test documents (\S\ref{sec:scierc-results}). DocRED: 998 dev documents (\S\ref{sec:docred-results}). WikiEvents: 246 documents (full corpus for zero-shot; 194/20/20 split for fine-tuning; \S\ref{sec:wikievents}).
40	\end{enumerate}
41	
42	\subsection*{C \hspace{0.5em} Did you run computational experiments?}
43	Yes.
44	
45	\begin{enumerate}[label=\textbf{C\arabic*.},leftmargin=2.5em]
46	\item \textbf{Did you report the number of parameters in the models used, the total computational budget, and computing infrastructure used?}
47	\\ Yes. Model sizes (7B--70B) in \S5. GPU infrastructure, LoRA configuration, and runtime overhead in \S\ref{sec:runtime} and Appendix~\ref{app:reproducibility}.
48	
49	\item \textbf{Did you discuss the experimental setup, including hyperparameter search and best-found hyperparameter values?}
50	\\ Yes. LoRA rank, learning rate, training epochs, and batch size are reported in Appendix~\ref{app:reproducibility}. Prompt templates are in Appendix~\ref{app:prompts}.
51	
52	\item \textbf{Did you report descriptive statistics about your results?}
53	\\ Yes. Bootstrap significance tests ($p$-values, 10{,}000 iterations) are reported for key comparisons (\S\ref{sec:scierc-results}, \S\ref{sec:docred-results}). Tables report F1, precision, recall, and violation rates across all configurations.
54	
55	\item \textbf{If you used existing packages, did you report the implementation, model, and parameter settings used?}
56	\\ Yes. XGrammar (grammar-constrained decoding), vLLM (inference engine), PEFT/LoRA (fine-tuning) are cited with version information in Appendix~\ref{app:reproducibility}.
57	\end{enumerate}
58	
59	\subsection*{D \hspace{0.5em} Did you use human annotators or research with human subjects?}
60	No. All evaluations are automatic. No human annotation or human subjects research was conducted.
61	
62	\subsection*{E \hspace{0.5em} Did you use AI assistants (e.g., ChatGPT, Copilot) in your research, coding, or writing?}
63	Yes.
64	
65	\begin{enumerate}[label=\textbf{E\arabic*.},leftmargin=2.5em]
66	\item \textbf{Did you include information about your use of AI assistants?}
67	\\ Yes. Claude (Anthropic) was used for code development assistance and manuscript drafting. All experimental results, analyses, and scientific claims were independently verified by the authors.
68	\end{enumerate}
69	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1e877e95-b5e4-4590-8f9b-9cfdd7d27aeb",
  "isSidechain": true,
  "promptId": "14fc01a8-031f-4ceb-ad2f-39c6c6b967ca",
  "agentId": "ad6a42899911fc70c",
  "type": "user",
  "uuid": "e1cca952-14d3-47c2-a6cf-8f703e85a756",
  "sourceToolAssistantUUID": "1e877e95-b5e4-4590-8f9b-9cfdd7d27aeb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/reviewer_17ad4b4d",
  "sessionId": "99513a19-7109-43ba-90b7-1799724932fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cached-moseying-feather"
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-22T12:01:28.803Z_

<details open><summary>🔧 Tool call — Read · `toolu_01VTVmmwjN8dhVrsmtdN9mor`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e1cca952-14d3-47c2-a6cf-8f703e85a756",
  "isSidechain": true,
  "agentId": "ad6a42899911fc70c",
  "requestId": "req_011CbHa7qXpmkhfsC5zS8a6y",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1988eebd-957e-4cee-afb1-04ee8b189abc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/reviewer_17ad4b4d",
  "sessionId": "99513a19-7109-43ba-90b7-1799724932fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cached-moseying-feather",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MRKhmRJY2SBVrQTuPRWfZn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5524,
      "cache_read_input_tokens": 42438,
      "output_tokens": 187,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5524
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 187,
          "cache_read_input_tokens": 42438,
          "cache_creation_input_tokens": 5524,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5524,
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

_source line 34 · 2026-05-22T12:01:28.811Z_

<details><summary>↩ Tool result · `toolu_01VTVmmwjN8dhVrsmtdN9mor`</summary>

```text
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
19	\usepackage{soul}
20	\usepackage{tikz}
21	\usetikzlibrary{arrows.meta,positioning,shapes.geometric,fit,backgrounds,calc}
22	\newcommand{\TBD}[1]{\textcolor{red}{#1}}
23	
24	\title{OntoCoDec: Type-Constrained Information Extraction\\via Compiled Schema Constraints}
25	
26	\author{Anonymous ACL submission}
27	
28	\begin{document}
29	\maketitle
30	
31	% === Abstract ===
32	\input{abstract}
33	
34	% === §1 Introduction ===
35	\input{section1_introduction_draft}
36	
37	% === §2 Background ===
38	\input{section2_background}
39	
40	% === §3 Method ===
41	\input{section3_method_draft}
42	
43	% === §4 Constraint Composition ===
44	\section{Constraint Composition}
45	\label{sec:composition}
46	\input{section4_composition_draft}
47	
48	% === §5 Experiments ===
49	\section{Experiments}
50	\label{sec:experiments}
51	
52	\input{section3_violation_landscape}
53	
54	\input{section5_scierc_draft}
55	\input{section5_docred_draft}
56	\input{section5_crossmodel_draft}
57	\input{section5_wikievents_draft}
58	\input{section5_runtime}
59	
60	% === §6 Related Work ===
61	\input{section6_related_work}
62	
63	% === §7 Discussion and Conclusion ===
64	\section{Discussion and Conclusion}
65	\label{sec:discussion}
66	\input{section7_conclusion_compressed}
67	
68	% === Limitations (ARR requirement: standalone section, does not count toward page limit) ===
69	\clearpage
70	\section*{Limitations}
71	
72	\paragraph{Constraint scope.}
73	CF impact is model-dependent: for well-calibrated models (Qwen, Llama; DR\,$\leq$\,1\% under greedy constrained decoding), S1 introduces CF violations (up to 12.02\%) as a consequence of per-relation independent enforcement; for poorly-calibrated models (Mistral), S1 substantially reduces CF (56.87\%\,$\to$\,1.27\%) by constraining type assignments to schema-valid values.
74	CF fallback ablation shows that eliminating CF re-routes violations to DR ($+$13.85\,pp). CF$\leftrightarrow$DR thus represents a fundamental trade-off in composable constraint systems rather than an independently resolvable limitation (Appendix~\ref{app:cf-dr-tradeoff}).
75	Global entity-level type consensus during decoding offers the most direct path to resolving CF violations.
76	CF type inconsistencies may propagate to downstream tasks that consume extracted triples (e.g., knowledge graph construction, question answering); the impact of such propagation has not been evaluated.
77	Entity F1 impact is model-dependent ($+$1.22\,pp for Qwen vs.\ $-$0.64\,pp for Llama on DocRED), partially confounded by increased parse failures under constraints (Llama: 9.1\% vs.\ 6.8\%).
78	On 70B DocRED LoRA, parse failure rises modestly under S1 (10.0\%\,$\to$\,12.5\%) due to generation timeouts on long documents rather than JSON format errors; SciERC (shorter documents) shows 0\% parse failure in both settings.
79	Residual DR under fine-tuning (36 violations across all fine-tuned settings, both models and both datasets) decomposes into entity type errors (39\%), schema coverage gaps (33\%), and model generation errors correctly caught by constraints (28\%); Llama DocRED alone accounts for 33 of 36 residual violations (92\%), reflecting weaker entity typing (Appendix~\ref{app:residual-dr-analysis}).
80	Schema coverage gaps (one-third of residual violations) arise because RE constraints are extracted from training-data type pairs, which may not cover all valid combinations; larger training sets or manual constraint table completion can reduce this gap.
81	Post-hoc type consensus re-voting (Appendix~\ref{app:tcr}) reduces CF violations by 18--92\% depending on model and dataset, confirming that first-assignment ordering sensitivity is a primary CF source; however, integrating consensus into the decoding loop remains future work.
82	
83	\paragraph{Evaluation coverage.}
84	Zero-shot results cover three 7--8B-class models, where relation F1 remains around 4--8\% compared to $\sim$45\% for fine-tuned systems.
85	Zero-shot evaluation covers three 8B-class and one 70B-class model; fine-tuning composability is validated on 8B-class (two models, full datasets) and 70B-class models (one model; SciERC full, DocRED 200-document subset).
86	Scaling to smaller models has not been verified, and the dual-factor pattern's predictive scope may differ at other scales.
87	Composability with fine-tuned models is validated on SciERC, DocRED, and WikiEvents with Qwen3-8B and Llama-3.1-8B (RE: DR\,$\leq$\,0.09\%, R-F1 within $\pm$0.8\,pp; EE: RoV$\to$0\%, AC$\leq$0.8\%), but evaluation is limited to one fine-tuning method (LoRA); residual CF (Qwen 1.18\%, Llama 0.46\% on SciERC) traces to schema-level type ambiguity (\textsc{Generic}$\leftrightarrow$X) rather than enforcement failure.
88	WikiEvents fine-tuning composability is preliminary (20-document test set, the full official split).
89	All main experiments use greedy decoding; our evaluation of beam search on the full SciERC (551 documents) and DocRED (998 documents) test sets across three models confirms compatibility (Appendices~\ref{app:sampling},~\ref{app:beam-search}), but comprehensive evaluation across all decoding configurations remains future work.
90	
91	\paragraph{Engineering considerations.}
92	Scalability benchmarks up to 200 entity types and 1,000 relations show constant 2--3\% inference overhead and sub-second compilation ($<$0.5\,s; Appendix~\ref{app:scalability}); however, the first-token uniqueness requirement for continuation masking may become a tokenizer-dependent bottleneck beyond this scale.
93	Our approach requires access to model logits for token-level masking, which excludes API-only models (e.g., GPT-4, Claude) where only output text is available; extending to API-only settings would require alternative enforcement mechanisms such as constrained sampling APIs or output reranking.
94	Continuation masking assumes each entity type name maps to a distinguishable token prefix sequence.
95	This assumption holds for our evaluation ontologies but may be challenged by ontologies with morphologically similar type names (e.g., \texttt{Protein} vs.\ \texttt{Protein\_Complex} vs.\ \texttt{Protein\_Domain}); when type names share a common prefix longer than one token, masking granularity depends on the tokenizer's subword segmentation.
96	70B experiments use AWQ INT4 quantization, which may alter logit distributions at mask boundaries; the impact on constraint enforcement precision has not been isolated.
97	Our evaluation is limited to English-language datasets; the continuation masking mechanism may behave differently for languages without whitespace-delimited tokenization (e.g., Chinese, Japanese), which we leave to future work.
98	Fine-tuning composability was validated exclusively with LoRA; full fine-tuning with an untuned learning rate underperforms LoRA (R-F1 37.89 vs.\ 43.77 on SciERC) but confirms that constraints remain effective (DR 2.74\%\,$\to$\,0\%; Appendix~\ref{app:full-ft}); other fine-tuning methods may exhibit different constraint interaction patterns and warrant further investigation.
99	
100	
101	% === Ethics Statement ===
102	\section*{Ethics Statement}
103	
104	This work uses publicly available benchmark datasets (SciERC, DocRED, and WikiEvents) with no personally identifiable information.
105	No human subjects were involved in the experiments.
106	The constrained decoding method operates on model outputs and does not introduce new privacy or safety risks beyond those inherent in the base language models.
107	Code and data will be released upon acceptance.
108	
109	% === ARR Responsible NLP Research Checklist ===
110	\input{checklist}
111	
112	% === Bibliography ===
113	\bibliography{relwork_new_entries}
114	
115	% === Appendix ===
116	\appendix
117	
118	\input{appendix_prompts}
119	\input{appendix_related_work}
120	\input{appendix_discussion}
121	\input{appendix_llama_per_relation}
122	\input{appendix_sampling_table}
123	\input{appendix_beam_search}
124	\input{appendix_reproducibility}
125	\input{appendix_doc_length}
126	\input{appendix_prompt_sensitivity}
127	\input{appendix_case_studies}
128	\input{appendix_scalability}
129	\input{appendix_full_ft}
130	\input{appendix_tcr}
131	\input{appendix_kappa_case_study}
132	\input{appendix_pumping_lemma}
133	
134	\end{document}
135	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1988eebd-957e-4cee-afb1-04ee8b189abc",
  "isSidechain": true,
  "promptId": "14fc01a8-031f-4ceb-ad2f-39c6c6b967ca",
  "agentId": "ad6a42899911fc70c",
  "type": "user",
  "uuid": "6fbf7f8c-c0a3-4d86-9216-4d3665532870",
  "sourceToolAssistantUUID": "1988eebd-957e-4cee-afb1-04ee8b189abc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/reviewer_17ad4b4d",
  "sessionId": "99513a19-7109-43ba-90b7-1799724932fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cached-moseying-feather"
}
```

</details>

---

### Assistant

_source line 35 · 2026-05-22T12:01:32.606Z_

Now I have all the necessary files. Let me do one more search for the S2 description mentioned in SF6, and check the κ̄ n=3 caveat (SF1).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6fbf7f8c-c0a3-4d86-9216-4d3665532870",
  "isSidechain": true,
  "agentId": "ad6a42899911fc70c",
  "requestId": "req_011CbHa8GZieXFiapNXfuKsQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "151afef6-320c-4147-bf77-45bb708b1b4d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/reviewer_17ad4b4d",
  "sessionId": "99513a19-7109-43ba-90b7-1799724932fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cached-moseying-feather",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017oPVE5cT8fgGfyGpcGKGGN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4582,
      "cache_read_input_tokens": 47962,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4582,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
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

_source line 36 · 2026-05-22T12:01:35.030Z_

<details open><summary>🔧 Tool call — Grep · `toolu_017SJTRPZXtR6ymTePrTSvd5`</summary>

```json
{
  "pattern": "deployment.grade|deployment-grade",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
  "output_mode": "content",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "151afef6-320c-4147-bf77-45bb708b1b4d",
  "isSidechain": true,
  "agentId": "ad6a42899911fc70c",
  "requestId": "req_011CbHa8GZieXFiapNXfuKsQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d2031d70-5fa4-492a-a1cd-769499336594",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/reviewer_17ad4b4d",
  "sessionId": "99513a19-7109-43ba-90b7-1799724932fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cached-moseying-feather",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017oPVE5cT8fgGfyGpcGKGGN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4582,
      "cache_read_input_tokens": 47962,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4582,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
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

_source line 37 · 2026-05-22T12:01:35.048Z_

<details><summary>↩ Tool result · `toolu_017SJTRPZXtR6ymTePrTSvd5`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section1_introduction_draft.tex:9:At deployment-grade quality (R-F1 40--46\%), even 1--2\% residual violations compound across thousands of documents into systematic knowledge graph corruption, making reliable constraint enforcement necessary.
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex:160:Even after LoRA fine-tuning, residual DR of 1--2\% persists on tight-constraint relations (Table~\ref{tab:composability}); constraints remain necessary at deployment-grade quality.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d2031d70-5fa4-492a-a1cd-769499336594",
  "isSidechain": true,
  "promptId": "14fc01a8-031f-4ceb-ad2f-39c6c6b967ca",
  "agentId": "ad6a42899911fc70c",
  "type": "user",
  "uuid": "5819f7ce-bc13-4aa2-98f3-507ac20ca5c9",
  "sourceToolAssistantUUID": "d2031d70-5fa4-492a-a1cd-769499336594",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/reviewer_17ad4b4d",
  "sessionId": "99513a19-7109-43ba-90b7-1799724932fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cached-moseying-feather"
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-22T12:01:36.194Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01PaifHA298P4bJf2jy5ArLz`</summary>

```json
{
  "pattern": "enabling dependency",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
  "output_mode": "content",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5819f7ce-bc13-4aa2-98f3-507ac20ca5c9",
  "isSidechain": true,
  "agentId": "ad6a42899911fc70c",
  "requestId": "req_011CbHa8GZieXFiapNXfuKsQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3a6efe0e-75b4-45b1-93a4-4892f2791cfb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/reviewer_17ad4b4d",
  "sessionId": "99513a19-7109-43ba-90b7-1799724932fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cached-moseying-feather",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017oPVE5cT8fgGfyGpcGKGGN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4582,
      "cache_read_input_tokens": 47962,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4582,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
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

_source line 39 · 2026-05-22T12:01:36.217Z_

<details><summary>↩ Tool result · `toolu_01PaifHA298P4bJf2jy5ArLz`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft_9b84f1.tex:147:replicating the enabling dependency observed on SciERC:
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft_9b84f1.tex:154:that the grammar$\to$semantic enabling dependency is a general
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section1_introduction_draft.tex:18:A decidability analysis of IE type constraints (\S\ref{sec:decidability}) yields a two-layer architecture: the \emph{grammar layer} compiles ontology constraints into context-free grammars (JSON structure, vocabulary membership) via XGrammar; the \emph{semantic layer} interprets type constraints at runtime via dynamic logit masking over an entity registry, with an \emph{empirical enabling dependency} between layers.
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section1_introduction_draft.tex:26:    \item A comprehensive evaluation across 3 IE datasets, 4 models (7--70B), and 2 tasks: under fine-tuning, DR\,$\leq$\,0.09\% at R-F1 43--46\% with CF\,$\leq$\,1.4\%; zero-shot ablation reveals an enabling dependency where on SciERC neither layer alone exceeds 24\% DR reduction (\S\ref{sec:scierc-results}); event extraction on WikiEvents validates applicability beyond RE (\S\ref{sec:wikievents}).
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_related_work.tex:110:The two constraint layers, grammar (structural) and semantic (relational), compose via bitwise AND with an empirical enabling dependency: the grammar layer ensures every generated type token belongs to the valid vocabulary, which enables the semantic layer to look up and enforce domain/range rules for that type.
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_method_draft.tex:36:\noindent\textbf{Corollary} (empirical enabling dependency: a constraint whose satisfaction is a prerequisite for evaluating subsequent constraints)\textbf{.} The empirical enabling dependency is necessary: the grammar layer alone cannot enforce domain/range constraints (Proposition~1), while the semantic layer alone achieves only 24\% DR reduction without grammar-enforced vocabulary membership (\S\ref{sec:scierc-results}, Table~\ref{tab:scierc-ablation}).
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_method_draft.tex:93:The final mask is $G(t) \cap S(t)$; when empty, grammar-first fallback applies (\S\ref{sec:composition}), embodying the empirical enabling dependency: semantic constraints reduce DR by only 24\% without grammar-enforced vocabulary.
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex:38:This metric directly quantifies the empirical enabling dependency (\S\ref{sec:interaction}): it measures the fraction of decoding steps where both constraint layers are jointly active, providing a fine-grained view beyond aggregate violation rates.
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section4_composition_draft.tex:11:The conjunction is asymmetric: $S(t)$ is defined only over $G(t)$. This reflects the empirical enabling dependency (\S\ref{sec:method}): the semantic layer requires the relation type to belong to $\mathcal{R}$, a property enforced only by the grammar layer.
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex:86:Semantic-only reduces DR by only 24\% and cannot eliminate RV or ET; this is the \emph{empirical enabling dependency}: adding the grammar layer yields a further 92\% reduction (11.65\%\,$\to$\,0.93\%).
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract.tex:4:The two layers exhibit an empirical enabling dependency (Proposition~1): neither achieves this reduction alone.
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft_4796e8.tex:128:This demonstrates an \emph{enabling dependency} rather than mere
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract_d3264e.tex:12:The two layers compose via bitwise AND on token-level masks, with an enabling dependency: the grammar layer guarantees well-formed output, upon which the semantic layer enforces relational type rules.
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract_fd4b26.tex:12:The two layers compose via bitwise AND on token-level masks, with an enabling dependency: the grammar layer guarantees well-formed output, upon which the semantic layer enforces relational type rules.
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft.tex:70:Semantic-only reduces DR by 25\% but cannot eliminate RV or ET, the same empirical enabling dependency observed on SciERC.
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/figures/iterative_fig1.py:73:- CRITICAL: Vertical dashed arrow from Grammar Layer down to Semantic Layer, with label "enabling" rotated 90°, bold italic, dark blue text, with a light blue badge/background box around the text. This represents the key enabling dependency.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3a6efe0e-75b4-45b1-93a4-4892f2791cfb",
  "isSidechain": true,
  "promptId": "14fc01a8-031f-4ceb-ad2f-39c6c6b967ca",
  "agentId": "ad6a42899911fc70c",
  "type": "user",
  "uuid": "1922de01-bc4c-4c2a-ada5-8e468f0b1674",
  "sourceToolAssistantUUID": "3a6efe0e-75b4-45b1-93a4-4892f2791cfb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/reviewer_17ad4b4d",
  "sessionId": "99513a19-7109-43ba-90b7-1799724932fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cached-moseying-feather"
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-22T12:01:37.284Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01DEiqR3EcKfEooKN56xwrkN`</summary>

```json
{
  "pattern": "n\\{?=\\}?3|n=3",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
  "output_mode": "content",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1922de01-bc4c-4c2a-ada5-8e468f0b1674",
  "isSidechain": true,
  "agentId": "ad6a42899911fc70c",
  "requestId": "req_011CbHa8GZieXFiapNXfuKsQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "964f7c81-53d3-406d-8c69-7165f49e5916",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/reviewer_17ad4b4d",
  "sessionId": "99513a19-7109-43ba-90b7-1799724932fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cached-moseying-feather",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017oPVE5cT8fgGfyGpcGKGGN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4582,
      "cache_read_input_tokens": 47962,
      "output_tokens": 452,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4582
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 452,
          "cache_read_input_tokens": 47962,
          "cache_creation_input_tokens": 4582,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4582,
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

_source line 41 · 2026-05-22T12:01:37.306Z_

<details><summary>↩ Tool result · `toolu_01DEiqR3EcKfEooKN56xwrkN`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex:135:\caption{Residual DR vs.\ Schema Restrictiveness $\times$ Baseline Violation Rate ($\bar{\kappa} \times \text{RV}_{\text{baseline}}$) across four model$\times$dataset configurations ($n{=}3$ schemas; descriptive only).
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract.tex:3:Without constraints, Large Language Model (LLM) based IE produces systematic domain/range (DR) violations that persist after fine-tuning, with rates characterized by \emph{constraint tightness} ($\bar{\kappa}$), a descriptive metric correlating schema restrictiveness with enforcement outcomes ($n{=}3$ schemas).
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract.tex:7:Zero-shot evaluation serves as a diagnostic, revealing dataset- and calibration-dependent effectiveness (42--99\% DR reduction, total violation reduction 31\%; \S\ref{sec:experiments}) and characterizing constraint tightness ($\bar{\kappa}$) as a descriptive correlate ($n{=}3$ schemas).
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.aux:2118:\@writefile{lof}{\contentsline {figure}{\numberline {2}{\ignorespaces Residual DR vs.\ Schema Restrictiveness $\times $ Baseline Violation Rate ($\bar  {\kappa } \times \text  {RV}_{\text  {baseline}}$) across four model$\times $dataset configurations ($n{=}3$ schemas; descriptive only). Linear fit (calibrated models): $y = 0.366x - 0.138$, $R^2 = 0.886$; Mistral deviates due to entity misclassification.}}{21}{figure.caption.69}\protected@file@percent }
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.aux:2119:\newlabel{fig:dual-factor-scatter}{{2}{21}{Residual DR vs.\ Schema Restrictiveness $\times $ Baseline Violation Rate ($\bar {\kappa } \times \text {RV}_{\text {baseline}}$) across four model$\times $dataset configurations ($n{=}3$ schemas; descriptive only). Linear fit (calibrated models): $y = 0.366x - 0.138$, $R^2 = 0.886$; Mistral deviates due to entity misclassification}{figure.caption.69}{}}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "964f7c81-53d3-406d-8c69-7165f49e5916",
  "isSidechain": true,
  "promptId": "14fc01a8-031f-4ceb-ad2f-39c6c6b967ca",
  "agentId": "ad6a42899911fc70c",
  "type": "user",
  "uuid": "06c1601b-3ad8-4da8-b275-801a3ac0dee8",
  "sourceToolAssistantUUID": "964f7c81-53d3-406d-8c69-7165f49e5916",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/reviewer_17ad4b4d",
  "sessionId": "99513a19-7109-43ba-90b7-1799724932fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cached-moseying-feather"
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-22T12:01:41.291Z_

<details open><summary>🔧 Tool call — Grep · `toolu_013FvUcBE6E2bfmruGjk8pgR`</summary>

```json
{
  "pattern": "entity registry.*order|ordering.*entity|first.*assignment|first-assignment",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
  "output_mode": "content",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "06c1601b-3ad8-4da8-b275-801a3ac0dee8",
  "isSidechain": true,
  "agentId": "ad6a42899911fc70c",
  "requestId": "req_011CbHa8u4gThkEcyMunaMZb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2b781a41-5772-47bf-969d-c17bedb60fbe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/reviewer_17ad4b4d",
  "sessionId": "99513a19-7109-43ba-90b7-1799724932fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cached-moseying-feather",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LfUn2D7APffTtnMVeufsXU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3131,
      "cache_read_input_tokens": 52544,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3131,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 41,
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

_source line 43 · 2026-05-22T12:01:41.321Z_

<details><summary>↩ Tool result · `toolu_013FvUcBE6E2bfmruGjk8pgR`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex:81:Post-hoc type consensus re-voting (Appendix~\ref{app:tcr}) reduces CF violations by 18--92\% depending on model and dataset, confirming that first-assignment ordering sensitivity is a primary CF source; however, integrating consensus into the decoding loop remains future work.
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_method_draft.tex:55:The output JSON Schema (\S\ref{sec:grammar}) enforces a fixed field ordering (head $\to$ tail $\to$ relation $\to$ head\_type $\to$ tail\_type) via deterministic grammar compilation, ensuring the relation type $r_j$ is known before entity type fields and enabling sequential domain/range lookups (\S\ref{sec:dynamic-masking}).
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_method_draft.tex:56:The grammar structurally enforces entity-before-relation ordering (100\% preservation across all configurations), ensuring the entity registry (\S\ref{sec:entity-registry}) is populated before relation-level type constraints are evaluated; unregistered entities trigger domain-only filtering.
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/figures/run_20260522_080526_d079d6/planning.json:3:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/figures/iterative_fig1.py:72:    - Dashed box at very bottom: "$\mathcal{D}$: entity registry (runtime state)" (light orange bg, dashed orange border)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2b781a41-5772-47bf-969d-c17bedb60fbe",
  "isSidechain": true,
  "promptId": "14fc01a8-031f-4ceb-ad2f-39c6c6b967ca",
  "agentId": "ad6a42899911fc70c",
  "type": "user",
  "uuid": "a71bd748-8e9c-4574-b1d7-90d69ee625f3",
  "sourceToolAssistantUUID": "2b781a41-5772-47bf-969d-c17bedb60fbe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/reviewer_17ad4b4d",
  "sessionId": "99513a19-7109-43ba-90b7-1799724932fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cached-moseying-feather"
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-22T12:01:42.679Z_

<details open><summary>🔧 Tool call — Grep · `toolu_0173zdfk2nhL9jBUibw3oByN`</summary>

```json
{
  "pattern": "SciERC.only|SciERC only|on SciERC",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex",
  "output_mode": "content",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a71bd748-8e9c-4574-b1d7-90d69ee625f3",
  "isSidechain": true,
  "agentId": "ad6a42899911fc70c",
  "requestId": "req_011CbHa8u4gThkEcyMunaMZb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "97611a2d-0e3b-4b4c-be72-180e330c27f5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/reviewer_17ad4b4d",
  "sessionId": "99513a19-7109-43ba-90b7-1799724932fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cached-moseying-feather",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LfUn2D7APffTtnMVeufsXU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3131,
      "cache_read_input_tokens": 52544,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3131,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 41,
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

_source line 45 · 2026-05-22T12:01:42.694Z_

<details><summary>↩ Tool result · `toolu_0173zdfk2nhL9jBUibw3oByN`</summary>

```text
87:Composability with fine-tuned models is validated on SciERC, DocRED, and WikiEvents with Qwen3-8B and Llama-3.1-8B (RE: DR\,$\leq$\,0.09\%, R-F1 within $\pm$0.8\,pp; EE: RoV$\to$0\%, AC$\leq$0.8\%), but evaluation is limited to one fine-tuning method (LoRA); residual CF (Qwen 1.18\%, Llama 0.46\% on SciERC) traces to schema-level type ambiguity (\textsc{Generic}$\leftrightarrow$X) rather than enforcement failure.
98:Fine-tuning composability was validated exclusively with LoRA; full fine-tuning with an untuned learning rate underperforms LoRA (R-F1 37.89 vs.\ 43.77 on SciERC) but confirms that constraints remain effective (DR 2.74\%\,$\to$\,0\%; Appendix~\ref{app:full-ft}); other fine-tuning methods may exhibit different constraint interaction patterns and warrant further investigation.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "97611a2d-0e3b-4b4c-be72-180e330c27f5",
  "isSidechain": true,
  "promptId": "14fc01a8-031f-4ceb-ad2f-39c6c6b967ca",
  "agentId": "ad6a42899911fc70c",
  "type": "user",
  "uuid": "33baf2c7-64b2-4c9c-a6b9-99424e2d04ae",
  "sourceToolAssistantUUID": "97611a2d-0e3b-4b4c-be72-180e330c27f5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/reviewer_17ad4b4d",
  "sessionId": "99513a19-7109-43ba-90b7-1799724932fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cached-moseying-feather"
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-22T12:01:42.911Z_

<details open><summary>🔧 Tool call — Read · `toolu_01EsRQrM219DATUVP4vfqqyx`</summary>

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
  "parentUuid": "33baf2c7-64b2-4c9c-a6b9-99424e2d04ae",
  "isSidechain": true,
  "agentId": "ad6a42899911fc70c",
  "requestId": "req_011CbHa8u4gThkEcyMunaMZb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dde3a1fa-68be-4845-9f96-fca73d1de4f3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/reviewer_17ad4b4d",
  "sessionId": "99513a19-7109-43ba-90b7-1799724932fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cached-moseying-feather",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LfUn2D7APffTtnMVeufsXU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3131,
      "cache_read_input_tokens": 52544,
      "output_tokens": 379,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3131
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 379,
          "cache_read_input_tokens": 52544,
          "cache_creation_input_tokens": 3131,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3131,
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

_source line 47 · 2026-05-22T12:01:43.256Z_

<details><summary>↩ Tool result · `toolu_01EsRQrM219DATUVP4vfqqyx`</summary>

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
38	This metric directly quantifies the empirical enabling dependency (\S\ref{sec:interaction}): it measures the fraction of decoding steps where both constraint layers are jointly active, providing a fine-grained view beyond aggregate violation rates.
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
72	%%% CF-DR Trade-off Analysis %%%
73	% exp_ids: cf_fallback_ablation_scierc (CF fallback vs full_s1 baseline)
74	
75	\paragraph{CF-DR Trade-off Analysis.}
76	\label{app:cf-dr-tradeoff}
77	
78	CF violations are the most prominent residual limitation of OntoCoDec under zero-shot decoding (9.90\% on SciERC, up to 12.02\% on Llama DocRED).
79	We treat this honestly: per-relation independent enforcement cannot eliminate CF without trading it against DR.
80	Table~\ref{tab:cf-dr-tradeoff} reports a pilot ablation in which we replace the grammar-first fallback with a CF-priority fallback that forces the entity's registered type when it conflicts with $\sigma(r)$.
81	
82	\begin{table}[t]
83	\centering
84	\small
85	\begin{tabular}{@{}l rrrr@{}}
86	\toprule
87	\textbf{Configuration} & \textbf{DR\,(\%)} & \textbf{CF\,(\%)} & \textbf{DR+CF} & \textbf{$f_{\text{gf}}$\,(\%)} \\
88	\midrule
89	S1 (baseline) & 0.93 & 9.90 & 10.83 & --- \\
90	CF fallback        & 14.78 & 0.04 & 14.82 & 36.64 \\
91	\midrule
92	$\Delta$ & $+$13.85 & $-$9.86 & $+$3.99 & --- \\
93	\bottomrule
94	\end{tabular}
95	\caption{CF-DR trade-off pilot on SciERC (Qwen3-8B, 551 documents; \texttt{w1\_cf\_fallback\_scierc\_pilot}). CF fallback eliminates CF but re-routes violations to DR, increasing total violations (DR+CF) by 3.99\,pp. $f_{\text{gf}}$: token-level grammar-first fallback rate at type-bearing positions (includes continuation tokens of multi-token type names; first-token position fallback rate is 0.46\% for SciERC Qwen; \S\ref{sec:greedy-limitation}).}
96	\label{tab:cf-dr-tradeoff}
97	\end{table}
98	
99	The CF fallback variant nearly eliminates CF (9.90\%\,$\to$\,0.04\%, $-$9.86\,pp) but at the cost of a 15.9$\times$ increase in DR (0.93\%\,$\to$\,14.78\%, $+$13.85\,pp).
100	% exp_id: w1_cf_fallback_scierc_pilot: DR=0.1478, CF=0.0004, f_gf=0.3664
101	This is not a net improvement: total violations (DR+CF) rise from 10.83\% to 14.82\% ($+$3.99\,pp), so the change \emph{re-routes} violations rather than reducing them.
102	The mechanism is mechanical: each token position with conflicting masks must commit to one violation type; when the CF fallback forces the system to emit the entity's registered type even though it lies outside $\sigma(r)$, the resulting triple satisfies cross-entity consistency but violates domain/range.
103	The token-level grammar-first fallback is triggered at 36.64\% of type-bearing positions (0.46\% at first-token positions; \S\ref{sec:greedy-limitation}); this conflict is structural, not a tunable hyperparameter.
104	
105	We interpret this as a fundamental tension in composable constraint systems with \emph{per-relation independent} enforcement: enforcement priority can be allocated between DR and CF but cannot independently minimize both.
106	Within this design, the current S1 configuration sits near the Pareto frontier of the trade-off, achieving 0.93\% DR at the cost of 9.90\% CF.
107	The direction of the trade-off is consistent beyond SciERC/Qwen3-8B: across all six zero-shot configurations (3 models $\times$ 2 datasets), DR and CF are descriptively inversely associated, with no setting showing both high DR and high CF simultaneously (Table~\ref{tab:cross-model}); however, $n{=}6$ is insufficient for statistical inference on this correlation.
108	The pattern is a structural consequence of per-relation enforcement with grammar-first fallback, not a model- or dataset-specific artifact; we select SciERC/Qwen3-8B for detailed ablation because it exhibits the highest CF (9.90\%), making the trade-off most visible.
109	While the inverse association holds across all configurations, the absolute trade-off magnitude may differ in settings with higher baseline CF, such as Llama DocRED (CF = 12.02\%), where the larger CF headroom could yield proportionally larger shifts under alternative fallback priorities.
110	The CF residual is concentrated in schema ambiguity rather than enforcement failure: 63.3\% of CF violations on SciERC involve the catch-all \textsc{Generic} type (Table~\ref{tab:cf-distribution}), which competes with every content type depending on anaphoric vs.\ referential use, a distinction the per-slot decoder cannot resolve without document-level coreference.
111	
112	Two complementary paths can lower CF without re-routing it to DR.
113	(i)~\emph{Reduce the baseline conflict rate.} Composing OntoCoDec with LoRA fine-tuning on SciERC reduces CF by 88\% relative to the zero-shot setting (9.90\%\,$\to$\,1.18\%; Table~\ref{tab:composability}), because the fine-tuned model's per-slot type predictions agree more often with the entity registry, so the per-relation mask and the registry intersect more frequently.
114	% exp_id: w5_lora_scierc_constrained_eval: CF=0.0118
115	The remaining 1.18\% still traces to \textsc{Generic}$\leftrightarrow$X schema ambiguity, so this path is empirically validated on one dataset and one fine-tuning method but does not generalize without further evidence.
116	(ii)~\emph{Replace per-relation enforcement with global entity-level type consensus during decoding.} This is outside the scope of OntoCoDec's forward-only autoregressive design and is left to future work.
117	
118	%%% Dual-Factor Quantitative Analysis %%%
119	% exp_ids: phase2_scierc_full_s1, phase2_docred_full_s1,
120	%          llama_scierc_full_s1, llama_docred_full_s1
121	
122	\paragraph{Dual-Factor Quantitative Analysis.}
123	\label{app:dual-factor}
124	
125	Figure~\ref{fig:dual-factor-scatter} plots residual DR against the product $\bar{\kappa} \times \text{RV}_{\text{baseline}}$ for model$\times$dataset configurations.
126	For \emph{calibrated} models (Qwen3-8B, Llama-3.1-8B; unconstrained ET${<}$3\% on both datasets), a linear fit yields $y = 0.366x - 0.138$ with $R^2 = 0.886$ ($n{=}4$, $F(1,2) = 15.54$, $p \approx 0.058$); with only four data points (df $= 2$) and $p > 0.05$, this constitutes a descriptive characterization rather than a confirmatory statistical test.
127	The strong fit supports the dual-factor pattern from \S\ref{sec:composition}: residual DR is governed by the product of schema tightness and baseline violation rate.
128	Mistral-7B (unconstrained ET${=}$7.58\% on DocRED) deviates from this pattern: its residual DR on DocRED (33.21\%) substantially exceeds the linear prediction. When model calibration is insufficient (ET${>}$5\% on either dataset), residual DR is dominated by entity misclassification rather than constraint-search failure.
129	This motivates a principled exclusion criterion: models with unconstrained ET${>}$5\% on either dataset fall outside the regime where the tightness$\times$RV product is the primary DR driver.
130	The two DocRED points (high $\bar{\kappa}{=}0.842$) separate cleanly from the two SciERC points (low $\bar{\kappa}{=}0.333$), and within each dataset the model with higher baseline RV shows higher residual DR.
131	
132	\begin{figure}[t]
133	\centering
134	\includegraphics[width=0.75\columnwidth]{figures/dual_factor_scatter.pdf}
135	\caption{Residual DR vs.\ Schema Restrictiveness $\times$ Baseline Violation Rate ($\bar{\kappa} \times \text{RV}_{\text{baseline}}$) across four model$\times$dataset configurations ($n{=}3$ schemas; descriptive only).
136	Linear fit (calibrated models): $y = 0.366x - 0.138$, $R^2 = 0.886$; Mistral deviates due to entity misclassification.}
137	\label{fig:dual-factor-scatter}
138	\end{figure}
139	
140	%%% Dataset-Dependent F1 Impact (moved from §7) %%%
141	% exp_ids: d012_bootstrap_ci (DocRED +0.50pp p<0.001, SciERC +0.13pp p=0.58),
142	%          phase0_docred_unconstrained (RV=29.66%), phase0_scierc_unconstrained (RV=1.39%)
143	
144	\paragraph{Dataset-Dependent F1 Impact.}
145	The divergence in F1 significance between DocRED ($+$0.50\,pp, $p < 0.001$) and SciERC ($+$0.13\,pp, $p = 0.58$) traces to a single mechanism: grammar-layer elimination of out-of-vocabulary relation names.
146	DocRED's baseline RV of 29.66\% produces 5{,}189 OOV predictions counted as false positives; eliminating them yields a significant precision gain.
147	SciERC's baseline RV is only 1.39\% (24 OOV predictions), too few to produce a detectable F1 effect.
148	Llama-3.1-8B's lower baseline RV (16.03\%) yields a smaller but directionally consistent improvement ($+$0.29\,pp vs.\ $+$0.50\,pp); F1 gain magnitude is proportional to baseline OOV rate.
149	% exp_ids: phase0_docred_unconstrained, phase0_scierc_unconstrained
150	% exp_ids: llama_docred_unconstrained (RV=16.03%), llama_docred_full_s1 (R-F1 delta=+0.29pp)
151	
152	%%% Paragraph 1: Low F1 Practical Significance %%%
153	% exp_ids: phase2_scierc_full_s1 (R-F1=8.36%), phase2_docred_full_s1 (R-F1=8.23%),
154	%          phase0_scierc_unconstrained (DR=15.37%), phase2_docred_unconstrained (DR=18.46%)
155	
156	\paragraph{Practical Significance of Zero-Shot F1.}
157	Our reported relation F1 of approximately 8\% on both SciERC and DocRED reflects the inherent difficulty of zero-shot closed IE, where the model receives no task-specific training examples.
158	For reference, supervised state-of-the-art systems on SciERC achieve approximately 49--53\% relation F1 with full training data~\citep{zhong2021frustratingly,ye2022packed}.
159	Constraint enforcement operates largely independently of the extraction model's intrinsic capability: it restricts the output space to ontologically valid triples regardless of the underlying model's accuracy.
160	Even after LoRA fine-tuning, residual DR of 1--2\% persists on tight-constraint relations (Table~\ref{tab:composability}); constraints remain necessary at deployment-grade quality.
161	% exp_ids: w5_lora_scierc_unconstrained_eval, w5_llama_lora_scierc_unconstrained_eval
162	In our evaluation, F1 serves as a \emph{control variable} verifying that constraint enforcement does not degrade extraction quality, not as an optimization target.
163	The contribution of this work is the constraint enforcement method itself; the zero-shot setting stress-tests constraint robustness under maximum model uncertainty, while composability with fine-tuning (\S\ref{sec:composability}) validates practical deployment value.
164	
165	%%% Paragraph 4: Decoding-Time vs. Post-Hoc Enforcement %%%
166	% exp_ids: posthoc_filtering_baseline, phase2_scierc_full_s1 (R-F1=8.36%),
167	%          phase2_docred_full_s1 (R-F1=8.23%, ET=0%)
168	
169	\paragraph{Decoding-Time vs.\ Post-Hoc Enforcement.}
170	Post-hoc filtering (generating triples without constraints, then removing schema-violating predictions) yields higher precision and consequently higher F1 than OntoCoDec on both datasets (SciERC 8.63 vs.\ 8.36; DocRED 9.61 vs.\ 8.23).
171	% posthoc: SciERC F1=8.63, DocRED F1=9.61; OntoCoDec: SciERC R-F1=8.36, DocRED R-F1=8.23
172	However, this precision gain comes at substantial cost.
173	On DocRED, post-hoc filtering discards 48.1\% of all predicted triples, including 127 true positives (11.2\% of correct predictions); recall drops from 9.46\% to 8.40\%.
174	% posthoc_docred: rejection=48.1%, tp_lost=127/1137, R: 9.46→8.40
175	Entity type violations remain unresolved (ET\,=\,2.47\% vs.\ OntoCoDec's 0\%), as filtering targets only domain/range and vocabulary violations.
176	% posthoc_docred: ET_residual=2.47%; phase2_docred_full_s1: ET=0%
177	OntoCoDec's decoding-time approach avoids this information loss by guiding generation toward compliant outputs rather than discarding non-compliant ones, preserving both recall and entity type validity.
178	The two strategies are complementary: post-hoc filtering can serve as an additional safety net for residual violations that decoding-time enforcement does not fully resolve.
179	
180	%%% CF Violation Distribution %%%
181	% exp_ids: phase2_scierc_full_s1 (CF=245), llama_scierc_full_s1 (CF=162),
182	%          phase2_docred_full_s1 (CF=2670), llama_docred_full_s1 (CF=3824)
183	
184	\paragraph{Cross-Field Violation Distribution.}
185	\label{app:cf-distribution}
186	
187	Table~\ref{tab:cf-distribution} reports the complete distribution of conflicting-type pairs for SciERC S1 (245 CF violations, all pairwise; no mention triggered $\geq$3 types).
188	Conflicts involving the \textsc{Generic} type account for 63.3\% (155/245) of all violations.
189	\textsc{Generic} is SciERC's anaphoric/placeholder label (``this approach'', ``the method''), which competes with every content type depending on whether the mention is used anaphorically or referentially, a distinction the per-slot constrained decoder cannot resolve without document-level coreference.
190	
191	The pattern generalizes across models and datasets: on Llama-3.1-8B SciERC, \textsc{Generic}$\leftrightarrow$\textsc{OtherScientificTerm} remains the top pair (53/162, 32.7\%); on DocRED, the analogous catch-all type \textsc{MISC} drives 76.6\% of Qwen's CF violations.
192	Under unconstrained decoding, CF rates collapse to $\leq$1\% on both datasets; CF violations are a side-effect of per-slot type commitment rather than a model deficiency.
193	
194	\begin{table}[t]
195	\centering
196	\small
197	\begin{tabular}{@{}lr r@{}}
198	\toprule
199	\textbf{Conflicting Type Pair} & \textbf{Count} & \textbf{\%} \\
200	\midrule
201	Generic $\leftrightarrow$ OtherScientificTerm & 85 & 34.7 \\
202	Generic $\leftrightarrow$ Material & 35 & 14.3 \\
203	Generic $\leftrightarrow$ Metric & 30 & 12.2 \\
204	Method $\leftrightarrow$ Task & 20 & 8.2 \\
205	Material $\leftrightarrow$ Method & 17 & 6.9 \\
206	OtherScientificTerm $\leftrightarrow$ Task & 12 & 4.9 \\
207	\midrule
208	10 further pairs (each $\leq$3.3\%) & 46 & 18.8 \\
209	\midrule
210	\textbf{Total} & \textbf{245} & 100.0 \\
211	\bottomrule
212	\end{tabular}
213	\caption{CF violation distribution on SciERC S1 (Qwen3-8B, 551 documents).
214	All 245 violations are pairwise conflicts.
215	Conflicts involving \textsc{Generic} account for 63.3\%.}
216	\label{tab:cf-distribution}
217	\end{table}
218	
219	%%% Per-Relation DR Elimination under Fine-Tuning %%%
220	% exp_ids: lora_scierc_unconstrained, lora_scierc_full_s1
221	
222	\paragraph{Per-Relation DR Elimination under Fine-Tuning.}
223	\label{app:lora-per-relation}
224	
225	Table~\ref{tab:lora-per-relation} presents the per-relation breakdown of DR elimination when OntoCoDec is composed with LoRA fine-tuning on SciERC.
226	Fine-tuning alone eliminates DR on four of seven relations but leaves non-zero violations on the three tightest-constraint relations: \textsc{Evaluate-for} ($\kappa{=}0.361$, 13.13\%), \textsc{Part-of} ($\kappa{=}0.417$, 5.77\%), and \textsc{Compare} ($\kappa{=}0.528$, 5.00\%).
227	Adding OntoCoDec constraints eliminates all remaining violations across all relations.
228	One \textsc{Evaluate-for} triple (99\,$\to$\,98) is redirected to \textsc{Used-for} (634\,$\to$\,635) by token-level masking: the head entity's registered type falls outside \textsc{Evaluate-for}'s domain, and the semantic mask steers generation to the nearest valid relation.
229	
230	\begin{table}[t]
231	\centering
232	\small
233	\begin{tabular}{@{}l r rr rr@{}}
234	\toprule
235	& & \multicolumn{2}{c}{\textbf{LoRA Unconstr.}} & \multicolumn{2}{c}{\textbf{LoRA + S1}} \\
236	\cmidrule(lr){3-4} \cmidrule(l){5-6}
237	\textbf{Relation} & $\kappa$ & DR\,(\%) & $n$ & DR\,(\%) & $n$ \\
238	\midrule
239	Evaluate-for & 0.361 & 13.13 & 99 & \textbf{0} & 98 \\
240	Part-of      & 0.417 & 5.77  & 52 & \textbf{0} & 52 \\
241	Compare      & 0.528 & 5.00  & 40 & \textbf{0} & 40 \\
242	Conjunction  & 0.306 & 1.31  & 153 & \textbf{0} & 153 \\
243	Feature-of   & 0.278 & 1.35  & 74 & \textbf{0} & 74 \\
244	Used-for     & 0.028 & 0.16  & 634 & \textbf{0} & 635 \\
245	Hyponym-of   & 0.417 & 0     & --- & \textbf{0} & --- \\
246	\bottomrule
247	\end{tabular}
248	\caption{Per-relation DR elimination on SciERC with LoRA fine-tuning (Qwen3-8B).
249	$\kappa$: constraint tightness; $n$: predicted triple count.
250	Used-for gains one triple from Evaluate-for redirection.}
251	\label{tab:lora-per-relation}
252	\end{table}
253	
254	%%% Fine-Tuned Four-Way Ablation %%%
255	% exp_ids: w5_lora_scierc_*, w5_llama_lora_scierc_*, w5_qwen_docred_*, w5_llama_docred_*, w8_*
256	
257	\paragraph{Fine-Tuned Four-Way Ablation.}
258	\label{app:ft-ablation}
259	
260	Table~\ref{tab:ft-ablation} presents the four-way constraint ablation on fine-tuned models across both datasets, isolating each layer's contribution when the base model has already internalized schema knowledge.
261	
262	\begin{table}[t]
263	\centering
264	\small
265	\setlength{\tabcolsep}{3pt}
266	\resizebox{\columnwidth}{!}{%
267	\begin{tabular}{@{}lll rrrrr rr@{}}
268	\toprule
269	\textbf{Dataset} & \textbf{Model} & \textbf{Mode} & \textbf{DR\,$\downarrow$} & \textbf{RV\,$\downarrow$} & \textbf{ET\,$\downarrow$} & \textbf{CF} & \textbf{PF} & \textbf{E-F1\,$\uparrow$} & \textbf{R-F1\,$\uparrow$} \\
270	\midrule
271	\multirow{8}{*}{SciERC}
272	  & \multirow{4}{*}{Qwen3-8B}
273	    & Unconstrained & 1.95 & 0.00 & 0.00 & 0.00 & 0.00 & 67.05 & 43.86 \\
274	  & & Grammar       & 1.90 & 0.00 & 0.00 & 0.00 & 0.00 & 67.05 & 43.86 \\
275	  & & Semantic      & 0.60 & 0.00 & 0.00 & 0.18 & 0.00 & 67.05 & 43.69 \\
276	  & & S1       & \textbf{0}    & 0.00 & 0.00 & 1.18 & 0.00 & 67.05 & 43.77 \\
277	  \cmidrule(l){2-10}
278	  & \multirow{4}{*}{Llama-3.1-8B}
279	    & Unconstrained & 1.11 & 0.00 & 0.00 & 0.00 & 0.00 & 67.76 & 45.45 \\
280	  & & Grammar       & 1.11 & 0.00 & 0.00 & 0.00 & 0.00 & 67.76 & 45.45 \\
281	  & & Semantic      & 0.65 & 0.00 & 0.00 & 0.10 & 0.00 & 67.76 & 45.47 \\
282	  & & S1       & \textbf{0.09} & 0.00 & 0.00 & 0.46 & 0.00 & 67.76 & 45.47 \\
283	\midrule
284	\multirow{8}{*}{DocRED}
285	  & \multirow{4}{*}{Qwen3-8B}
286	    & Unconstrained & 0.56 & 0.27 & 0.00 & 0.08 & 7.11 & 82.35 & 40.89 \\
287	  & & Grammar       & 0.61 & 0.00 & 0.00 & 0.11 & 7.01 & 82.19 & 40.85 \\
288	  & & Semantic      & 0.21 & 0.23 & 0.00 & 0.27 & 7.52 & 82.15 & 40.89 \\
289	  & & S1       & \textbf{0.00} & 0.00 & 0.00 & 0.22 & 8.52 & 81.87 & 40.79 \\
290	  \cmidrule(l){2-10}
291	  & \multirow{4}{*}{Llama-3.1-8B}
292	    & Unconstrained & 0.49 & 0.15 & 0.00 & 0.08 & 2.30 & 84.77 & 44.55 \\
293	  & & Grammar       & 0.51 & 0.00 & 0.00 & 0.12 & 2.30 & 84.04 & 43.77 \\
294	  & & Semantic      & 0.30 & 0.15 & 0.00 & 0.16 & 2.40 & 84.02 & 43.90 \\
295	  & & S1       & \textbf{0.00} & 0.00 & 0.00 & 0.26 & 2.51 & 84.71 & 44.70 \\
296	\bottomrule
297	\end{tabular}}%
298	\caption{Four-way constraint ablation on fine-tuned models (LoRA, 2 models $\times$ 2 datasets).
299	DR/RV/ET/CF: violation rates (\%); PF: parse failure rate (\%); F1 $\times$100.
300	Grammar layer is a no-op post-fine-tuning (DR change $<$0.2\,pp in all 4 settings; RV and ET already 0\% without constraints).
301	Semantic layer is the sole effective DR defense, providing 39--69\% reduction.
302	F1 cost is negligible: max $\Delta$R-F1 = $-$0.10\,pp (Qwen DocRED, full vs.\ unconstrained).}
303	\label{tab:ft-ablation}
304	\end{table}
305	
306	The grammar layer is effectively a no-op for fine-tuned models across all four settings: RV and ET are already 0\% without constraints, and grammar-only DR change is $<$0.2\,pp (4/4 settings).
307	The semantic layer is the sole effective DR defense under fine-tuning, independently reducing DR by 39--69\% across all settings (SciERC: Qwen $-$69\%, Llama $-$41\%; DocRED: Qwen $-$63\%, Llama $-$39\%).
308	Adding both layers achieves near-complete elimination (DR\,$\leq$\,0.09\% in all 4 settings): even after fine-tuning, the semantic layer's pair-based enforcement captures violations that training alone cannot eliminate, specifically on tight-constraint relations where the valid type-pair space is small.
309	F1 cost is negligible: the maximum R-F1 decrease across S1 vs.\ unconstrained is $-$0.10\,pp (Qwen DocRED).
310	
311	%%% Residual DR Error Analysis (Fine-Tuned) %%%
312	% exp_ids: w5_qwen_docred_*, w5_llama_docred_*, w5_lora_scierc_*, w5_llama_lora_scierc_*
313	
314	\paragraph{Residual DR Error Analysis.}
315	\label{app:residual-dr-analysis}
316	
317	Across all fine-tuned settings (2 models $\times$ 2 datasets $\times$ S1), only 36 domain/range violations remain.
318	Manual inspection reveals four root causes:
319	
320	\begin{enumerate}[nosep,leftmargin=*]
321	\item \emph{Entity type errors} (39\%): the LLM assigns an incorrect entity type (e.g., labeling a geographic entity as \textsc{LOC} when the gold standard requires \textsc{MISC}), causing the semantic mask to permit a domain/range-incompatible relation.
322	\item \emph{Schema coverage gaps} (33\%): the frequency-based constraint table, constructed from training-set co-occurrence statistics, does not cover long-tail type pairs that are ontologically valid but rare. These violations are irreducible by decoding-time constraints alone.
323	\item \emph{Incorrect relation selection} (17\%): the model selects a semantically inappropriate relation whose domain/range constraints are incompatible with the correctly typed entities.
324	\item \emph{Direction reversal} (11\%): the model assigns the correct relation but inverts head/tail roles, placing entities in positions that violate the relation's asymmetric domain/range specification.
325	\end{enumerate}
326	
327	Two dataset-specific patterns emerge.
328	Outside Llama DocRED, all residual violations (3 of 36, spanning Llama SciERC and Qwen DocRED) trace exclusively to schema coverage gaps: the model's entity typing is accurate, and the constraint system has reached its theoretical ceiling given the frequency-based constraint table.
329	On DocRED, Llama-3.1-8B contributes 33 of 36 residual violations (92\%), with entity type errors as the dominant cause (14/33, 42\%).
330	This asymmetry reflects Llama's weaker fine-tuned entity typing on DocRED's larger ontology (96 relations, 7 entity types) compared to Qwen, which achieves near-zero residual.
331	The implication is twofold: (i)~the irreducible floor from schema gaps is small ($\sim$3 violations across 4 settings), so the constraint system operates near its theoretical optimum; (ii)~residual violations from entity typing errors are addressable through stronger base models or improved entity typing modules, without modifying the constraint architecture.
332	
333	%%% Post-Hoc Filtering Comparison (Extended) %%%
334	% exp_ids: posthoc_*_zs, posthoc_*_ft
335	
336	\paragraph{Post-Hoc Filtering: Extended Comparison.}
337	\label{app:posthoc-extended}
338	
339	Table~\ref{tab:posthoc-extended} presents the full comparison across all six zero-shot and four fine-tuned configurations.
340	
341	\begin{table}[t]
342	\centering
343	\small
344	\setlength{\tabcolsep}{3pt}
345	\resizebox{\columnwidth}{!}{%
346	\begin{tabular}{@{}lll rrr l@{}}
347	\toprule
348	\textbf{Setting} & \textbf{Model} & \textbf{Dataset} & \textbf{Reject\%} & \textbf{R-F1$_{\text{ph}}$} & \textbf{R-F1$_{\text{cd}}$} & \textbf{Winner} \\
349	\midrule
350	\multirow{6}{*}{ZS}
351	  & Qwen    & SciERC & 16.8 & 8.63  & 8.36  & ph \\
352	  & Llama   & SciERC & 13.9 & 2.71  & 2.54  & ph \\
353	  & Mistral & SciERC & 20.3 & 3.94  & 3.67  & ph \\
354	  & Qwen    & DocRED & 48.1 & 9.61  & 8.23  & ph \\
355	  & Llama   & DocRED & 42.2 & 7.44  & 6.27  & ph \\
356	  & Mistral & DocRED & \textbf{73.7} & 3.85  & \textbf{5.52} & cd \\
357	\midrule
358	\multirow{4}{*}{FT}
359	  & Qwen    & SciERC & 1.95 & 43.94 & 43.77 & ph \\
360	  & Llama   & SciERC & 1.11 & 45.23 & 45.47 & cd \\
361	  & Qwen    & DocRED & 1.03 & 41.11 & 40.79 & ph \\
362	  & Llama   & DocRED & 0.64 & 43.92 & 44.70 & cd \\
363	\bottomrule
364	\end{tabular}}%
365	\caption{Post-hoc filtering (ph) vs.\ constrained decoding (cd).
366	In zero-shot settings, post-hoc F1 is higher in 5/6 groups (precision-dominated), but constrained decoding preserves higher recall in all 6/6 groups.
367	At reject rate $>$70\% (Mistral DocRED), post-hoc F1 collapses below constrained.
368	Under fine-tuning, rejection rates drop to 0.6--2.0\% and the two strategies are equivalent ($\Delta \leq 0.55$\,pp; each wins two groups).
369	F1 $\times$100.}
370	\label{tab:posthoc-extended}
371	\end{table}
372	
373	The crossover point occurs when post-hoc rejection exceeds $\sim$70\%: Mistral DocRED rejects 73.7\% of predicted triples, discarding enough true positives that constrained decoding's recall advantage dominates ($+$1.67\,pp).
374	OntoCoDec's advantage thus scales with violation severity: precisely when constraints are most needed, post-hoc filtering is most destructive.
375	Under fine-tuning, both strategies converge because few violations remain to filter or constrain ($\Delta \leq 0.55$\,pp across all four FT groups, with each strategy winning two).
376	
377	%%% Zero-Shot Runtime Profiling %%%
378	
379	\paragraph{Zero-Shot Runtime Profiling.}
380	\label{app:runtime}
381	
382	On SciERC (Qwen3-8B, zero-shot greedy, NVIDIA RTX PRO 6000 Blackwell Server Edition), unconstrained inference averages 4.163\,s/doc and S1 constrained decoding averages 4.710\,s/doc ($+$13.1\% overhead).
383	On DocRED (same configuration), relative overhead is lower due to amortization: the fixed per-token constraint cost is spread over longer generation sequences.
384	XGrammar automaton compilation takes 0.044\,s; the full constraint pipeline (schema parsing, JSON Schema generation, grammar compilation) takes 0.33\,s on SciERC (Table~\ref{tab:scalability}), amortized to zero over the evaluation set.
385	
386	% exp_id: p8c_ft_scierc_latency — Reviewer Report #23 verified
387	\paragraph{Fine-Tuned Latency Profiling.}
388	\label{app:ft-latency}
389	Under LoRA fine-tuning (same hardware and dataset), unconstrained inference averages 2.612\,s/doc and S1 constrained decoding averages 2.873\,s/doc ($+$10.0\% overhead, $n{=}551$).
390	Fine-tuned models generate shorter, more structured outputs than zero-shot models (2.612\,s vs.\ 4.163\,s/doc unconstrained); absolute generation time drops by 37\%.
391	The relative overhead ($+$10.0\%) is slightly lower than zero-shot ($+$13.1\%), consistent with shorter sequences requiring fewer constraint checks per document.
392	
393	%%% Fuzzy Relation Matching %%%
394	
395	\paragraph{Relation Matching Protocol.}
396	\label{app:fuzzy-matching}
397	Relation F1 evaluation uses fuzzy normalization to handle model-specific formatting variants (e.g., underscores vs.\ spaces, abbreviations).
398	A predicted relation $r_p$ matches gold relation $r_g$ if: (1)~exact string match after case-insensitive normalization, or (2)~token overlap $>$80\% \emph{and} edit distance $\leq 2$.
399	This protocol affects primarily Mistral, which produces underscore-separated variants (e.g., ``head\_of\_government'' for ``head of government'').
400	On Mistral DocRED, fuzzy matching contributes 98 additional TPs ($+$0.84\,pp R-F1; strict R-F1\,=\,3.50\% vs.\ fuzzy 4.34\%).
401	For Qwen and Llama under grammar constraints, the grammar layer enforces exact relation names, making fuzzy matching irrelevant (0 additional matches).
402	All F1 figures in the main text use fuzzy normalization consistently across all models and conditions.
403	
404	%%% Per-Relation Violation Landscape %%%
405	
406	\paragraph{Per-Relation Violation Landscape.}
407	\label{app:per-relation-landscape}
408	
409	Table~\ref{tab:prompt_comparison} compares violation rates under unconstrained and schema-informed prompting.
410	Figure~\ref{fig:per_relation_dr} shows the per-relation DR distribution on SciERC.
411	
412	\begin{table}[t]
413	\centering
414	\small
415	\caption{Violation rates (\%) under unconstrained and schema-informed prompting (Qwen3-8B, zero-shot).}
416	\label{tab:prompt_comparison}
417	\resizebox{\columnwidth}{!}{%
418	\begin{tabular}{ll cccc}
419	\toprule
420	Dataset & Prompt & DR$\downarrow$ & RV$\downarrow$ & ET$\downarrow$ & CF$\downarrow$ \\
421	\midrule
422	\multirow{2}{*}{SciERC} & Unconstrained & 15.4 & 1.4 & 0.4 & 0.1 \\
423	 & Schema-informed & 5.8 & 0.3 & \textbf{0.0} & --- \\
424	\midrule
425	\multirow{2}{*}{DocRED} & Unconstrained & 18.5 & 29.7 & 2.5 & 0.1 \\
426	 & Schema-informed & 12.8 & 18.4 & 0.2 & 0.2 \\
427	\bottomrule
428	\end{tabular}}
429	\end{table}
430	
431	\begin{figure}[t]
432	\centering
433	\includegraphics[width=\columnwidth]{figures/fig2_per_relation_dr.pdf}
434	\caption{Per-relation DR violation rates on SciERC (Qwen3-8B, unconstrained). Rates correlate with constraint tightness $\kappa(r)$. Llama-3.1-8B shows similar per-relation patterns (Appendix~\ref{app:llama-per-relation}).}
435	\label{fig:per_relation_dr}
436	\end{figure}
437	
438	%%% WikiEvents Extended %%%
439	
440	\paragraph{WikiEvents Dataset Details.}
441	\label{app:wikievents}
442	WikiEvents~\cite{li2021document} is a document-level event argument extraction benchmark grounded in the DARPA KAIROS ontology.
443	It defines 56 event types, 80 argument roles, and 27 entity types, with 245 (event\_type, role)$\to$allowed\_entity\_types constraints.
444	The grammar layer targets EV (event vocabulary), RoV (role vocabulary), and ET; the semantic layer enforces AC (argument constraint) via role-conditioned masking, analogous to RE domain/range enforcement.
445	
446	\paragraph{Constraint Tightness in WikiEvents.}
447	\label{app:wikievents-kappa}
448	% Data source: artifacts/w1c_wikievents_kappa_results.md
449	WikiEvents role-level tightness (with $|\mathcal{E}|{=}27$) has mean $\bar{\kappa}{=}0.82$ and median 0.89; 84\% of roles have $\kappa \geq 0.80$ (4 or fewer valid entity types out of 27).
450	The tightness-violation pattern extends to event extraction: roles with $\kappa \geq 0.90$ exhibit the highest AC rate (50\%), compared to 21\% for medium-tightness ($0.80 \leq \kappa < 0.90$) and 30\% for loose ($\kappa < 0.80$) roles; this is consistent with the RE observation that constraint tightness correlates with violation frequency.
451	However, the correlation is modulated by entity type prototypicality: semantically intuitive roles (e.g., Transportation.Vehicle$\to$VEH) show 0\% AC despite $\kappa{=}0.963$, while roles that require rare KAIROS-specific types (e.g., Crime$\to$CRM, Sentence$\to$SEN) show near-100\% AC because LLMs default to common types (PER, ORG).
452	The loose group's elevated rate (30\%) is driven by high-frequency roles such as Attack.Target (126 args, 34\% AC, $\kappa{=}0.59$), where systematic model errors outweigh the permissive constraint space.
453	
454	%%% Lucky Violation Analysis %%%
455	% exp_ids: task_e_lucky_violation_analysis
456	
457	\paragraph{Lucky Violation Analysis.}
458	\label{app:lucky-violations}
459	Table~\ref{tab:lucky-violations} quantifies the recall cost of DR elimination.
460	A ``lucky violation'' is a constraint-removed triple that happens to match a gold label---an ontologically invalid prediction that is nonetheless correct.
461	Across four fine-tuned configurations, lucky violations average 0.49\% of gold triples (range 0.01--0.51\%), confirming that nearly all removed DR violations are false positives.
462	On Llama SciERC, all five lucky violations are recovered as legal type paths under constrained decoding (zero churn): the model finds an ontology-compliant route to the same prediction.
463	
464	\begin{table}[h]
465	\centering
466	\small
467	\resizebox{\columnwidth}{!}{%
468	\begin{tabular}{@{}llrrrr@{}}
469	\toprule
470	\textbf{Model} & \textbf{Dataset} & \textbf{DR (\%)} & \textbf{Lucky} & \textbf{$\Delta$Recall} & \textbf{Churn} \\
471	& & \textbf{unc$\to$con} & \textbf{(\% gold)} & \textbf{(pp)} & \textbf{(\%)} \\
472	\midrule
473	Qwen3-8B  & SciERC & 1.95$\to$0    & 4 (0.41\%) & $-$0.10 & 0.22 \\
474	Llama-8B  & SciERC & 1.11$\to$0.09 & 5 (0.51\%) & $\pm$0.00 & 0 \\
475	Qwen3-8B  & DocRED & 1.03$\to$0.01 & 1 (0.01\%) & $-$0.84 & 2.05 \\
476	Llama-8B  & DocRED & 0.64$\to$0.21 & 1 (0.01\%) & $-$0.10 & 0.86 \\
477	\midrule
478	\multicolumn{2}{@{}l}{\textit{Average}} & & \textit{0.49\%} & $-$0.26 & 0.78 \\
479	\bottomrule
480	\end{tabular}}
481	\caption{Lucky violation analysis across four LoRA fine-tuned configurations.
482	Lucky: count (and \% of gold triples) of constraint-removed violations matching gold labels.
483	$\Delta$Recall: recall change from unconstrained to constrained.
484	Churn: fraction of gold-matching triples whose predictions change (including recovery via legal type paths).}
485	\label{tab:lucky-violations}
486	\end{table}
487	
488	%%% Trie-Only Baseline %%%
489	% exp_ids: trie_qwen_ft_scierc, trie_qwen_zs_scierc, trie_llama_ft_scierc, trie_llama_zs_scierc
490	
491	\paragraph{Trie-Only Baseline (GCD-Equivalent).}
492	\label{app:trie-baseline}
493	Table~\ref{tab:trie-baseline} isolates the effect of vocabulary membership constraints without JSON structural enforcement.
494	The trie constrains entity type and relation tokens to schema-valid values (achieving ET${=}$0\%, RV${=}$0\% across all configurations), functionally equivalent to GCD's~\cite{geng2023gcd} constrained decoding.
495	However, without grammar-level JSON enforcement, models systematically omit entity type fields (83\% of triples) or produce malformed JSON (0--51\% parse failure), causing DR to rise to 15--96\%---far worse than unconstrained baselines.
496	The effect is most dramatic for Llama-8B LoRA: 50.8\% parse failure causes R-F1 to collapse from 45.47 (OntoCoDec S1) to 19.95, demonstrating that the grammar layer is not merely helpful but a structural prerequisite---vocabulary constraints require JSON scaffolding to reach the positions where they apply.
497	
498	\begin{table}[h]
499	\centering
500	\small
501	\resizebox{\columnwidth}{!}{%
502	\begin{tabular}{@{}ll rrrr rr@{}}
503	\toprule
504	\textbf{Model} & \textbf{Setting}
505	  & \textbf{ET\,$\downarrow$} & \textbf{RV\,$\downarrow$} & \textbf{DR\,$\downarrow$} & \textbf{CF}
506	  & \textbf{R-F1\,$\uparrow$} & \textbf{PF\,(\%)} \\
507	\midrule
508	\multirow{2}{*}{Qwen3-8B}
509	  & LoRA  & 0 & 0 & 95.5  & 0.09 & 41.16 & 9.1 \\
510	  & ZS    & 0 & 0 & 29.3  & 0    & 8.64  & 0 \\
511	\multirow{2}{*}{Llama-8B}
512	  & LoRA  & 0 & 0 & 15.2$^\dagger$  & 0    & 19.95 & 50.8 \\
513	  & ZS    & 0 & 0 & 84.4  & 0.36 & 2.90  & 0 \\
514	\midrule
515	\multicolumn{8}{@{}l}{\textit{Comparison with OntoCoDec S1:}} \\
516	\midrule
517	& & \multicolumn{2}{c}{\textbf{S1 DR\,(\%)}} & \textbf{Trie DR\,(\%)} & \multicolumn{2}{c}{\textbf{DR Gap (pp)}} & \\
518	\cmidrule(lr){3-4} \cmidrule(lr){5-5} \cmidrule(lr){6-7}
519	Qwen3-8B  & LoRA  & \multicolumn{2}{c}{0}    & 95.5  & \multicolumn{2}{c}{95.5}  & \\
520	Qwen3-8B  & ZS    & \multicolumn{2}{c}{0.93} & 29.3  & \multicolumn{2}{c}{28.4}  & \\
521	Llama-8B  & LoRA  & \multicolumn{2}{c}{0.09} & 15.2  & \multicolumn{2}{c}{15.1}  & \\
522	Llama-8B  & ZS    & \multicolumn{2}{c}{0.08} & 84.4  & \multicolumn{2}{c}{84.3}  & \\
523	\bottomrule
524	\end{tabular}}
525	\caption{Trie-only baseline (GCD-equivalent, vocabulary membership without JSON grammar) on SciERC.
526	Top: full trie-only metrics (ET/RV/DR/CF: violation rates \%; R-F1 $\times$100; PF: parse failure rate).
527	Trie achieves ET${=}$0\%, RV${=}$0\% but DR rises to 15--96\% because models omit type fields without structural enforcement.
528	Bottom: DR gap between OntoCoDec S1 and trie-only, quantifying the grammar layer's contribution.
529	$^\dagger$50.8\% parse failure rate.}
530	\label{tab:trie-baseline}
531	\end{table}
532	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dde3a1fa-68be-4845-9f96-fca73d1de4f3",
  "isSidechain": true,
  "promptId": "14fc01a8-031f-4ceb-ad2f-39c6c6b967ca",
  "agentId": "ad6a42899911fc70c",
  "type": "user",
  "uuid": "70e31137-9332-46d7-a41b-d2b529488786",
  "sourceToolAssistantUUID": "dde3a1fa-68be-4845-9f96-fca73d1de4f3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/reviewer_17ad4b4d",
  "sessionId": "99513a19-7109-43ba-90b7-1799724932fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cached-moseying-feather"
}
```

</details>

---

### Assistant

_source line 48 · 2026-05-22T12:01:49.645Z_

Now let me search for the "enabling dependency" SciERC-only scope issue (SF4) and check for any mention of entity registry order in the limitations:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "70e31137-9332-46d7-a41b-d2b529488786",
  "isSidechain": true,
  "agentId": "ad6a42899911fc70c",
  "requestId": "req_011CbHa9LSubSRWedTQWmEFN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "16a16c41-4074-4e38-9c78-665804f6cd90",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/reviewer_17ad4b4d",
  "sessionId": "99513a19-7109-43ba-90b7-1799724932fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cached-moseying-feather",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FhTueUuxA38WW3g3J596Ja",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16639,
      "cache_read_input_tokens": 55675,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16639,
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

_source line 49 · 2026-05-22T12:01:52.919Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01E4epQnp36MuxKqVTrHePTR`</summary>

```json
{
  "pattern": "entity.*(order|sensitivity|first-come|first.come|ordering.*order)",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex",
  "output_mode": "content",
  "-n": true,
  "-i": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "16a16c41-4074-4e38-9c78-665804f6cd90",
  "isSidechain": true,
  "agentId": "ad6a42899911fc70c",
  "requestId": "req_011CbHa9LSubSRWedTQWmEFN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e4cf7cd7-791a-4aad-b634-c9bf5cc28bc6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/reviewer_17ad4b4d",
  "sessionId": "99513a19-7109-43ba-90b7-1799724932fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cached-moseying-feather",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FhTueUuxA38WW3g3J596Ja",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16639,
      "cache_read_input_tokens": 55675,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16639,
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

_source line 50 · 2026-05-22T12:01:52.967Z_

<details><summary>↩ Tool result · `toolu_01E4epQnp36MuxKqVTrHePTR`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e4cf7cd7-791a-4aad-b634-c9bf5cc28bc6",
  "isSidechain": true,
  "promptId": "14fc01a8-031f-4ceb-ad2f-39c6c6b967ca",
  "agentId": "ad6a42899911fc70c",
  "type": "user",
  "uuid": "a3acedbb-dafc-4474-a809-170fb45b956b",
  "sourceToolAssistantUUID": "e4cf7cd7-791a-4aad-b634-c9bf5cc28bc6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/reviewer_17ad4b4d",
  "sessionId": "99513a19-7109-43ba-90b7-1799724932fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cached-moseying-feather"
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-22T12:01:54.049Z_

<details open><summary>🔧 Tool call — Grep · `toolu_012GDwzxNbia8FmPNkZT7rp3`</summary>

```json
{
  "pattern": "ordering|order.*sensitiv|first-come|generation order",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
  "output_mode": "content",
  "-n": true,
  "-i": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a3acedbb-dafc-4474-a809-170fb45b956b",
  "isSidechain": true,
  "agentId": "ad6a42899911fc70c",
  "requestId": "req_011CbHa9LSubSRWedTQWmEFN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0b7d8e2a-491c-4a3e-838c-bbc89cda5340",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/reviewer_17ad4b4d",
  "sessionId": "99513a19-7109-43ba-90b7-1799724932fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cached-moseying-feather",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FhTueUuxA38WW3g3J596Ja",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16639,
      "cache_read_input_tokens": 55675,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16639,
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

_source line 52 · 2026-05-22T12:01:54.076Z_

<details><summary>↩ Tool result · `toolu_012GDwzxNbia8FmPNkZT7rp3`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex:81:Post-hoc type consensus re-voting (Appendix~\ref{app:tcr}) reduces CF violations by 18--92\% depending on model and dataset, confirming that first-assignment ordering sensitivity is a primary CF source; however, integrating consensus into the decoding loop remains future work.
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_method_draft.tex:55:The output JSON Schema (\S\ref{sec:grammar}) enforces a fixed field ordering (head $\to$ tail $\to$ relation $\to$ head\_type $\to$ tail\_type) via deterministic grammar compilation, ensuring the relation type $r_j$ is known before entity type fields and enabling sequential domain/range lookups (\S\ref{sec:dynamic-masking}).
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_method_draft.tex:56:The grammar structurally enforces entity-before-relation ordering (100\% preservation across all configurations), ensuring the entity registry (\S\ref{sec:entity-registry}) is populated before relation-level type constraints are evaluated; unregistered entities trigger domain-only filtering.
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_beam_search.tex:10:(1)~The grammar layer (XGrammar) maintains an internal \texttt{GrammarMatcher} state that tracks the generated token sequence; beam reordering invalidates this state because beams are permuted across steps.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0b7d8e2a-491c-4a3e-838c-bbc89cda5340",
  "isSidechain": true,
  "promptId": "14fc01a8-031f-4ceb-ad2f-39c6c6b967ca",
  "agentId": "ad6a42899911fc70c",
  "type": "user",
  "uuid": "13b212ae-45b8-4f6a-ba76-35384684f0a2",
  "sourceToolAssistantUUID": "0b7d8e2a-491c-4a3e-838c-bbc89cda5340",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/reviewer_17ad4b4d",
  "sessionId": "99513a19-7109-43ba-90b7-1799724932fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cached-moseying-feather"
}
```

</details>

---

### Assistant

_source line 53 · 2026-05-22T12:01:58.969Z_

Now let me check the R17 review report to see exactly what was requested:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "13b212ae-45b8-4f6a-ba76-35384684f0a2",
  "isSidechain": true,
  "agentId": "ad6a42899911fc70c",
  "requestId": "req_011CbHaAFqNGZ5GzqteQrKuD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0114b870-4a46-4564-8fd9-41ae89dd26e9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/reviewer_17ad4b4d",
  "sessionId": "99513a19-7109-43ba-90b7-1799724932fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cached-moseying-feather",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WkhambcgKWs6xspPY1XKzZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 886,
      "cache_read_input_tokens": 72314,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 886,
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

_source line 54 · 2026-05-22T12:02:00.366Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01WkUiW4S3dEfBhqwbtcy7Cr`</summary>

```json
{
  "pattern": "S2.*description|S2.*match|two-pass|S2.*evaluat",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
  "output_mode": "content",
  "-n": true,
  "-i": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0114b870-4a46-4564-8fd9-41ae89dd26e9",
  "isSidechain": true,
  "agentId": "ad6a42899911fc70c",
  "requestId": "req_011CbHaAFqNGZ5GzqteQrKuD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b40fdd03-a488-4568-85c6-10a0564b27c1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/reviewer_17ad4b4d",
  "sessionId": "99513a19-7109-43ba-90b7-1799724932fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cached-moseying-feather",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WkhambcgKWs6xspPY1XKzZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 886,
      "cache_read_input_tokens": 72314,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 886,
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

_source line 55 · 2026-05-22T12:02:00.395Z_

<details><summary>↩ Tool result · `toolu_01WkUiW4S3dEfBhqwbtcy7Cr`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_related_work.tex:100:A two-pass variant (S2), explored in ablation (Section~5), separates extraction and constraint enforcement into distinct passes, analogous to CRANE's alternating strategy; however, our primary single-pass approach already avoids reasoning interference by constraining only type tokens while leaving free-text spans unconstrained.
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_method_draft.tex:102:\paragraph{S2 (two-pass pipeline): Two-pass decoding.}\label{sec:s2}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.aux:382:\newlabel{sec:s2}{{3.4}{4}{S2 (two-pass pipeline): Two-pass decoding}{section*.13}{}}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.aux:383:\@writefile{toc}{\contentsline {paragraph}{S2 (two-pass pipeline): Two-pass decoding.}{4}{section*.13}\protected@file@percent }
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.aux:524:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.aux:525:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex:63:S1 = single-pass (\S\ref{sec:strategies}), S2 = two-pass (\S\ref{sec:s2}).
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft_4796e8.tex:140:The two-pass strategy (S2) achieves comparable DR
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft_4796e8.tex:148:unconstrained baseline (0.08\%), indicating that two-pass decoding
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft_4796e8.tex:152:The two-pass separation offers no clear advantage over single-pass
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b40fdd03-a488-4568-85c6-10a0564b27c1",
  "isSidechain": true,
  "promptId": "14fc01a8-031f-4ceb-ad2f-39c6c6b967ca",
  "agentId": "ad6a42899911fc70c",
  "type": "user",
  "uuid": "43dad2b4-b605-4be5-9d16-032301dd03df",
  "sourceToolAssistantUUID": "b40fdd03-a488-4568-85c6-10a0564b27c1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/reviewer_17ad4b4d",
  "sessionId": "99513a19-7109-43ba-90b7-1799724932fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cached-moseying-feather"
}
```

</details>

---

### Assistant

_source line 56 · 2026-05-22T12:03:18.842Z_

Now I have comprehensive coverage. Let me compile the verification report.

---

## R17 Fix Verification Report

### MF1: DR Range Consistency

**Abstract** (`abstract.tex:7`): "42--99% DR reduction"
**Cross-model** (`section5_crossmodel_draft.tex:57`): "DR drops 76--99% on SciERC and 42--90% on DocRED"
**Introduction** (`section1_introduction_draft.tex:21`): "DR drops 42--99% across models and datasets, with 88--99% on SciERC"

**Verdict: PARTIAL**. The abstract says "42--99%" which is the union range. The body breaks it down by dataset (76--99% SciERC, 42--90% DocRED). But the introduction says "88--99% on SciERC" while the cross-model section says "76--99% on SciERC" -- these are inconsistent. Checking Table 3: Qwen SciERC DR drops 15.37->0.93 (94%), Llama SciERC 13.34->0.08 (99%), Mistral SciERC 56.94->13.40 (76%). So "76--99%" is correct for SciERC (3 models). The introduction's "88--99%" is wrong unless it excludes Mistral, but no such exclusion is stated. **NEW inconsistency introduced by fixes: intro line 21 says "88--99% on SciERC" vs cross-model "76--99% on SciERC"**.

### MF2: CF Bound ≤1.4%

**Abstract** (`abstract.tex:6`): "CF ($\leq$1.4\% fine-tuned; up to 12\% zero-shot)"
**Section 5 SciERC** (`section5_scierc_draft.tex:78`): "CF\,$\leq$\,1.4\% (Table~\ref{tab:composability})"
**Introduction** (`section1_introduction_draft.tex:21`): "CF\,$\leq$\,1.4\% fine-tuned"
**Conclusion** (`section7_conclusion_compressed.tex:3`): "CF\,$\leq$\,1.4\%"

Checking Table 2: Qwen SciERC CF=1.18, Llama SciERC CF=0.46, Qwen DocRED CF=0.22, Llama DocRED CF=0.26. All ≤1.18%. But 70B results (`section5_runtime.tex:18`): "CF drops from 3.50% (zero-shot) to 0.18--1.33% (LoRA)". So 70B LoRA CF max = 1.33%. The 8B max is 1.18%.

The max across all fine-tuned settings is 1.33% (70B). Claiming "≤1.4%" covers this. Previously it was "≤1.3%" which was wrong (1.33% > 1.3%). Now "≤1.4%" is correct.

**Verdict: PASS**.

### MF3: CF Narrative — ZS worst case and ZS/FT distinction

**Abstract** (`abstract.tex:6`): "CF ($\leq$1.4\% fine-tuned; up to 12\% zero-shot)" — clearly distinguishes ZS vs FT, and "up to 12%" covers the 12.02% Llama DocRED worst case.
**Cross-model** (`section5_crossmodel_draft.tex:58`): "CF direction depends on calibration: S1 introduces CF for calibrated models (up to 12.02%; \S\ref{sec:discussion})"
**Discussion** (`discussion_paragraphs.tex:30`): "Qwen3-8B; Llama-3.1-8B exhibits 12.02% on DocRED, the highest across all configurations"

**Verdict: PASS**. ZS/FT are clearly distinguished in abstract, and the 12.02% worst case is prominently mentioned in cross-model and discussion.

### MF4: "five" LMs → "four"

**Abstract** (`abstract.tex:8`): "four autoregressive LMs (7--70B; 70B zero-shot and LoRA in \S\ref{sec:70b-results})"
**Introduction** (`section1_introduction_draft.tex:19`): "four models (7--70B)"

**Verdict: PASS**.

### MF5: GCD Equivalence Argument

**Section 5 runtime** (`section5_runtime.tex:21-24`): "Our grammar-only ablation (Table~\ref{tab:scierc-ablation}, row~2) implements the same token-level constraints as GCD~\cite{geng2023gcd} and BoostCD~\cite{boostcd2025}---CFG-based JSON structure enforcement plus vocabulary membership masking---providing a direct head-to-head comparison: RV/ET$\to$0\% but only 3\% DR reduction, vs.\ S1's 94\%, confirming that CFG enforcement alone is insufficient for type-valid IE."
**Appendix** (`appendix_discussion.tex:491-496`): "Trie-Only Baseline (GCD-Equivalent)" with detailed table showing trie-only = GCD's approach.

**Verdict: PASS**. The argument is explicitly stated: grammar-only ablation = GCD-equivalent, with quantitative comparison.

### SF1: κ̄ n=3 Caveat

**Abstract** (`abstract.tex:3`): "a descriptive metric correlating schema restrictiveness with enforcement outcomes ($n{=}3$ schemas)"
**Abstract** (`abstract.tex:7`): "characterizing constraint tightness ($\bar{\kappa}$) as a descriptive correlate ($n{=}3$ schemas)"
**Section 4** (`section4_composition_draft.tex:21`): "Across three schemas" with explicit κ̄ values.
**Appendix** (`appendix_discussion.tex:126`): "with only four data points (df $= 2$) and $p > 0.05$, this constitutes a descriptive characterization rather than a confirmatory statistical test"

**Verdict: PASS**. The n=3 limitation is marked twice in the abstract with "descriptive" framing, and the appendix explicitly notes the statistical insufficiency.

### SF2: WikiEvents n=20 — "preliminary" and CI

**WikiEvents** (`section5_wikievents_draft.tex:47-48`): Table caption: "Fine-tuning results are preliminary given the small test set ($n{=}20$); bootstrap 95\% CIs for argument F1 span approximately $\pm$3--5\,pp."
**WikiEvents** (`section5_wikievents_draft.tex:64`): "\paragraph{Composability with fine-tuning (preliminary, $n{=}20$).}"
**WikiEvents** (`section5_wikievents_draft.tex:66`): "trigger F1 shifts ($-$5.4/$-$0.6\,pp) have wide CIs consistent with n${=}$20"

**Verdict: PASS**. "Preliminary" is in both the paragraph heading and table caption, CIs are reported.

### SF3: "deployment-grade" Softened

**Introduction** (`section1_introduction_draft.tex:9`): "At deployment-grade quality (R-F1 40--46\%)"
**Appendix** (`appendix_discussion.tex:160`): "constraints remain necessary at deployment-grade quality"

**Verdict: FAIL**. "Deployment-grade" is still used in the introduction (line 9) without qualification. The term implies production readiness, but R-F1 of 40-46% (even fine-tuned) is well below supervised SOTA (49-53% per the discussion). This term should be softened to something like "competitive" or "practical" or qualified with a comparison to SOTA.

### SF4: "Enabling dependency" — SciERC-only scope noted

The enabling dependency claim appears in:
- **Abstract** (`abstract.tex:4`): "The two layers exhibit an empirical enabling dependency (Proposition~1): neither achieves this reduction alone." — no dataset scope.
- **Method** (`section3_method_draft.tex:36`): "the semantic layer alone achieves only 24\% DR reduction without grammar-enforced vocabulary membership (\S\ref{sec:scierc-results}, Table~\ref{tab:scierc-ablation})" — references SciERC explicitly.
- **SciERC results** (`section5_scierc_draft.tex:86`): "this is the \emph{empirical enabling dependency}" — SciERC data.
- **DocRED results** (`section5_docred_draft.tex:70`): "Semantic-only reduces DR by 25\% but cannot eliminate RV or ET, the same empirical enabling dependency observed on SciERC" — explicitly validates on DocRED too.

**Verdict: PASS**. The enabling dependency is established on SciERC (24% DR reduction alone) and then verified on DocRED (25% DR reduction alone). The cross-dataset replication is noted. The "neither achieves this reduction alone" claim in the abstract is supported by both datasets.

### SF5: Entity Registry Order — Quantified Limitations sentence

**Limitations** (`main.tex:81`): "Post-hoc type consensus re-voting (Appendix~\ref{app:tcr}) reduces CF violations by 18--92\% depending on model and dataset, confirming that first-assignment ordering sensitivity is a primary CF source"

This is quantified (18--92%), explicitly names the issue (first-assignment ordering sensitivity), and is in the Limitations section.

**Verdict: PASS**.

### SF6: S2 Description Matches Evaluation

**Method** (`section3_method_draft.tex:102-104`): "S2 (two-pass pipeline): Two-pass decoding. A first pass extracts entities; these compile an input-dependent grammar for the second pass. S1 achieves higher R-F1 at comparable DR (\S\ref{sec:scierc-results}) and is the primary configuration."
**Table 1 caption** (`section5_scierc_draft.tex:63`): "S2 = two-pass (\S\ref{sec:s2})"
**Results** (`section5_scierc_draft.tex:93`): "S2 achieves comparable DR (0.97\%) but lower R-F1 and CF; we adopt S1."

The description says "two-pass pipeline: first pass extracts entities, second pass uses input-dependent grammar." The evaluation shows S2 row in Table 1 with DR=0.97%, R-F1=8.03. The description matches: S2 is a two-pass strategy that is evaluated and found inferior to S1.

**Verdict: PASS**.

### M1-M7: Other Issues Scan

**M1 (Checklist in PDF)**: The checklist.tex is included via `\input{checklist}` in main.tex (line 110). Per user rules, "ARR Responsible NLP Checklist在OpenReview的submission form里面（由用户手动填写），而不是在论文pdf里面". Including it in the PDF is a **rule violation**. However, this is about the ARR Responsible NLP Checklist, not the standard limitations/ethics — checking the checklist content, it appears to be structured as an A-E section checklist matching the ARR format. **This checklist should NOT be in the PDF per user rules.**

**M2 (Limitations length)**: Per user rules, "Limitations 章节只需要写一小段，覆盖 3 个点左右就可以了". The current Limitations section (`main.tex:72-98`) spans ~27 lines of dense text with 3 paragraphs (Constraint scope, Evaluation coverage, Engineering considerations) — 3 points as required. However, the content is extensive (likely >400 words). Per the rule, it should be short. This is borderline but technically covers only 3 points.

**M3 (Page limit)**: Cannot verify without compiling, but the Limitations section starts after `\clearpage` which is proper for not counting toward page limit.

### NEW Inconsistency Found

**Introduction line 21** says "88--99% on SciERC" but Table 3 shows Mistral SciERC drops 56.94->13.40 which is 76% reduction. Cross-model section correctly says "76--99% on SciERC". The introduction's "88--99%" appears to exclude Mistral without saying so, creating an inconsistency with the cross-model table.

---

## Summary

| Item | Status | Location | Issue |
|------|--------|----------|-------|
| MF1 | **PARTIAL** | `section1_introduction_draft.tex:21` | Intro says "88--99% on SciERC" vs cross-model "76--99%" — new inconsistency |
| MF2 | **PASS** | abstract/scierc/intro/conclusion | ≤1.4% correctly covers 1.33% 70B max |
| MF3 | **PASS** | abstract/crossmodel/discussion | ZS/FT clearly distinguished, 12.02% mentioned |
| MF4 | **PASS** | abstract/intro | "four" LMs |
| MF5 | **PASS** | section5_runtime/appendix | GCD equivalence explicitly argued |
| SF1 | **PASS** | abstract (×2)/appendix | n=3 caveat with "descriptive" framing |
| SF2 | **PASS** | wikievents heading/caption/text | "preliminary", CIs reported |
| SF3 | **FAIL** | `section1_introduction_draft.tex:9` | "deployment-grade" still unsoftened |
| SF4 | **PASS** | method/scierc/docred | Cross-dataset replication noted |
| SF5 | **PASS** | `main.tex:81` | Quantified 18--92% with "first-assignment ordering sensitivity" |
| SF6 | **PASS** | method/scierc | S2 description matches evaluation |
| NEW | **FAIL** | `section1_introduction_draft.tex:21` | "88--99% on SciERC" contradicts Table 3 (76--99%) |
| M1 | **WARNING** | `main.tex:110` | ARR Responsible NLP Checklist in PDF violates user rule |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "43dad2b4-b605-4be5-9d16-032301dd03df",
  "isSidechain": true,
  "agentId": "ad6a42899911fc70c",
  "requestId": "req_011CbHaAcYZUed3JG2BKG5K4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "952367a2-120e-4c3a-8a38-f4917529ae62",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/reviewer_17ad4b4d",
  "sessionId": "99513a19-7109-43ba-90b7-1799724932fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cached-moseying-feather",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PCjB51QzAVH3NLN3Bt8poy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 961,
      "cache_read_input_tokens": 73200,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 961,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---
