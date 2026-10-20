# Research conversation: Read all these tex files and return their full contents. I need every single line: 1. /home/ubuntu/.agent-ml-research-be

**Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on Customer-Service Agent Safety (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 27
- **Recorded user turns:** 1
- **Tool calls:** 12
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-aec8d190c3a37fd6c.jsonl`
- **Structured JSON:** [`00ec69bad04dff6e5169.json`](../../sessions/00/00ec69bad04dff6e5169.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

27 recorded events

### User

_source line 1 · 2026-05-21T22:40:20.932Z_

Read all these tex files and return their full contents. I need every single line:

1. /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/abstract.tex
2. /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/introduction.tex
3. /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/related_work.tex
4. /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/taxonomy.tex
5. /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/method.tex
6. /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/experiments.tex
7. /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/analysis.tex
8. /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/discussion.tex
9. /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/conclusion.tex
10. /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/limitations.tex
11. /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/appendix.tex
12. /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.tex

Return the complete contents of each file, clearly labeled with the filename.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "97940243-dcdb-4134-8cbb-a2e35e11a449",
  "agentId": "aec8d190c3a37fd6c",
  "type": "user",
  "uuid": "a72025a5-db12-4a30-9a62-ca39eccf4861",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper",
  "sessionId": "46389320-86e2-42d7-b5e1-48bec7f5ca1b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-21T22:40:22.503Z_

I'll read all these LaTeX files for you in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a72025a5-db12-4a30-9a62-ca39eccf4861",
  "isSidechain": true,
  "agentId": "aec8d190c3a37fd6c",
  "requestId": "req_011CbGX2ynvNuxiGnfQsCdQe",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "1be27a3f-7283-425c-8ada-5dd74e4eab50",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper",
  "sessionId": "46389320-86e2-42d7-b5e1-48bec7f5ca1b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_015M2g8gp5G8yzTt1gganJDe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 36172,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 36172,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 6,
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

_source line 3 · 2026-05-21T22:40:22.996Z_

<details open><summary>🔧 Tool call — Read · `toolu_012CRepsUuEKzZGwvHtx8Pq7`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1be27a3f-7283-425c-8ada-5dd74e4eab50",
  "isSidechain": true,
  "agentId": "aec8d190c3a37fd6c",
  "requestId": "req_011CbGX2ynvNuxiGnfQsCdQe",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "ed0c094c-eebf-43e5-9cd3-32cf225d4950",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper",
  "sessionId": "46389320-86e2-42d7-b5e1-48bec7f5ca1b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_015M2g8gp5G8yzTt1gganJDe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 36172,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 36172,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 6,
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

_source line 4 · 2026-05-21T22:40:23.012Z_

<details><summary>↩ Tool result · `toolu_012CRepsUuEKzZGwvHtx8Pq7`</summary>

```text
1	\begin{abstract}
2	LLM-based agents operate under natural-language policy specifications that inevitably contain ambiguity, yet the causal relationship between ambiguity type and safety violations remains unmeasured. We present a matched-pair study on $\tau^2$-bench with 300 clause pairs spanning a six-type ambiguity taxonomy, evaluated across five models (2,997 episodes). Three findings emerge. First, ambiguous clauses increase violation rates by 34.0 percentage points (OR $= 15.1$), with a perturbation control supporting ambiguity-specific causation. Second, incompleteness consistently ranks highest (46--62\% across seven models); the remaining five types cluster into a lower tier at the $\pm$15\,pp margin, though tier cohesion is margin-dependent. Third, authorization scope shows the widest but least reliably measured cross-model range (52\,pp; $\kappa = 0.385$, \S Limitations), suggesting that safety training may differentially mitigate specific ambiguity types. Agents show fewer than 11\% disambiguation awareness, adopting surface interpretations without flagging uncertainty. These results motivate type-aware policy auditing and externalized ambiguity detection for policy-governed agent deployments.
3	\end{abstract}
4	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ed0c094c-eebf-43e5-9cd3-32cf225d4950",
  "isSidechain": true,
  "promptId": "97940243-dcdb-4134-8cbb-a2e35e11a449",
  "agentId": "aec8d190c3a37fd6c",
  "type": "user",
  "uuid": "4e8a77d4-e912-47eb-8eeb-84492034bc70",
  "sourceToolAssistantUUID": "ed0c094c-eebf-43e5-9cd3-32cf225d4950",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper",
  "sessionId": "46389320-86e2-42d7-b5e1-48bec7f5ca1b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-21T22:40:23.172Z_

<details open><summary>🔧 Tool call — Read · `toolu_019bBEUhJR9FH3NZ77jkUP7g`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4e8a77d4-e912-47eb-8eeb-84492034bc70",
  "isSidechain": true,
  "agentId": "aec8d190c3a37fd6c",
  "requestId": "req_011CbGX2ynvNuxiGnfQsCdQe",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "59f4060a-f0e1-4295-ac66-75fd2ebe207c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper",
  "sessionId": "46389320-86e2-42d7-b5e1-48bec7f5ca1b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_015M2g8gp5G8yzTt1gganJDe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 36172,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 36172,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 6,
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

_source line 6 · 2026-05-21T22:40:23.185Z_

<details><summary>↩ Tool result · `toolu_019bBEUhJR9FH3NZ77jkUP7g`</summary>

```text
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
13	\caption{Experimental overview. We construct 300 matched clause pairs across a six-type, two-layer ambiguity taxonomy and inject them into $\tau^2$-bench policy documents. Five models interact with the modified policies across 2,997 episodes. A cross-judge evaluation pipeline classifies violation severity on a four-tier scale.}
14	\label{fig:overview}
15	\end{figure*}
16	
17	We address this gap with a matched-pair causal study on $\tau^2$-bench \citep{tau2_bench_2025}, a dual-control conversational agent benchmark. Using a six-type taxonomy organized into two layers (linguistic and specification, \S\ref{sec:taxonomy}), we construct 300 ambiguous/unambiguous clause pairs and evaluate five architecturally diverse models across 2,997 episodes.
18	
19	Our results show that all policy ambiguity is nocuous for LLM agents ($+34.0$ pp violation rate increase, OR $= 15.1$), but that type primarily determines severity, with a smaller but significant model$\times$type interaction (2.9\% of variance). Incompleteness is consistently high (46--62\% violation rate across all models), while authorization scope shows the widest but least reliably measured cross-model range (52\,pp; $\kappa = 0.385$, \S Limitations), suggesting that safety training may differentially mitigate specific ambiguity types. Agents exhibit disambiguation deficit in over 89\% of cases, with fewer than 11\% showing any disambiguation awareness.
20	
21	Our contributions are: (1)~the first causal quantification of policy ambiguity's safety impact via matched-pair design with perturbation control (\S\ref{sec:method}), observed across five primary models and confirmed in two additional replication models; (2)~incompleteness as a consistent upper-bound risk type across all models and margins, with type identity explaining 22$\times$ more variance than model identity (\S\ref{sec:results}); and (3)~a failure mode taxonomy with the empirical phenomenon of \emph{Disambiguation Deficit} ($<$11\% awareness; \S\ref{sec:analysis}).
22	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "59f4060a-f0e1-4295-ac66-75fd2ebe207c",
  "isSidechain": true,
  "promptId": "97940243-dcdb-4134-8cbb-a2e35e11a449",
  "agentId": "aec8d190c3a37fd6c",
  "type": "user",
  "uuid": "4e9483ed-0354-4b80-9f68-72a3ab67eaae",
  "sourceToolAssistantUUID": "59f4060a-f0e1-4295-ac66-75fd2ebe207c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper",
  "sessionId": "46389320-86e2-42d7-b5e1-48bec7f5ca1b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-21T22:40:23.373Z_

<details open><summary>🔧 Tool call — Read · `toolu_019jKGz9PPDYKh7cd5e4ykac`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4e9483ed-0354-4b80-9f68-72a3ab67eaae",
  "isSidechain": true,
  "agentId": "aec8d190c3a37fd6c",
  "requestId": "req_011CbGX2ynvNuxiGnfQsCdQe",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "ad5f9eff-9070-42dc-b60a-4d57d0a4532e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper",
  "sessionId": "46389320-86e2-42d7-b5e1-48bec7f5ca1b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_015M2g8gp5G8yzTt1gganJDe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 36172,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 36172,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 6,
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

_source line 8 · 2026-05-21T22:40:23.380Z_

<details><summary>↩ Tool result · `toolu_019jKGz9PPDYKh7cd5e4ykac`</summary>

```text
1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Ambiguity in NLP and requirements engineering.}
5	Ambiguity has been studied extensively in both computational linguistics and software engineering. Word sense disambiguation \citep{navigli_wsd_2009} addresses lexical ambiguity at the token level; our lexical type extends this to policy-specific polysemy. \citet{li_ambiguity_taxonomy_2024} propose an 11-type NLP taxonomy covering syntactic, semantic, and pragmatic ambiguity, from which we draw our linguistic-layer types. In requirements engineering (RE), \citet{massey_ambiguity_re_2014} classify six ambiguity types in regulatory texts, and \citet{berry_kamsties_2004} introduce the distinction between nocuous ambiguity (where stakeholders diverge on interpretation) and innocuous ambiguity (where they converge). Computational detection of nocuous ambiguity has progressed from heuristic methods \citep{chantree_2006,willis_nocuous_2008} through NLP-based cross-domain detectors \citep{ferrari_ambiguity_2019,ferrari_defects_2018} to transformer-based approaches for anaphoric ambiguity \citep{ezzini_taphsir_2022,ezzini_anaphoric_2022}. \citet{zhao_nlp4re_2021} survey the broader NLP4RE landscape. Our work extends Berry and Kamsties' framework to LLM agents, where the absence of shared organizational context makes previously innocuous ambiguity nocuous.
6	
7	\paragraph{Psycholinguistics of ambiguity processing.}
8	\citet{ferreira_good_enough_2002} show that human comprehenders build shallow, ``good-enough'' representations rather than full parses, paralleling our observation that LLM agents adopt surface interpretations. \citet{frazier_rayner_1982} demonstrate early commitment to a single parse; \citet{li_garden_path_llm_2024} provide direct evidence that LLMs exhibit analogous garden-path effects. \citet{liu_ambiguity_2023} demonstrate that language models fail to represent ambiguity, collapsing multiple interpretations into a single output. These findings ground our \emph{Disambiguation Deficit} result: agents process ambiguous input without meta-cognitive awareness but, unlike humans, lack social channels to recover. \citet{suri_structured_2025} show that structured uncertainty estimation improves coverage by 7--39\%, while \citet{sehwag_aspi_2026} demonstrate that clarification-seeking introduces prompt injection vulnerabilities---a tension for disambiguation channel design.
9	
10	\paragraph{Agent safety evaluation.}
11	The agent safety evaluation landscape includes benchmarks for risk awareness \citep{rjudge_2024}, tool-use safety \citep{toolemu_2024}, indirect prompt injection \citep{injecagent_2024}, safe task planning \citep{yin_safeagentbench_2025}, and policy-invisible violations \citep{phantompolicy_2026}. \citet{tamkin_evaluating_2023} evaluate how language models navigate policy-governed decisions, \citet{shieldagent_2025} extract formal safety rules from policy documents, and AgentAuditor \citep{agentauditor_2025} achieves human-level safety evaluation. Our work differs by focusing on the \emph{source specification} rather than the agent's execution: we measure how ambiguity in the policy itself causes safety violations, complementing work that assumes clean policies.
12	
13	\paragraph{Policy specification for agents.}
14	DRIP-R \citep{drip_r_2026} is the closest concurrent work: it benchmarks 400 policy-ambiguous retail scenarios across five RE ambiguity types, measuring decision quality rather than safety violations. Our work differs in three respects: (1) our matched-pair design establishes causality rather than correlating ambiguity presence with outcomes; (2) we measure safety violations rather than decision quality, enabling failure mechanism analysis; (3) our two-layer taxonomy adds linguistic-layer types, and we quantify the model$\times$type interaction. We map DRIP-R's five RE ambiguity categories to our six-type taxonomy in Appendix~\ref{app:drip_mapping}. PolicyBank \citep{policybank_2026} studies iterative policy refinement, closing 82\% of the gap to a human oracle. AgentPex \citep{agentpex_2026} detects procedural violations in agentic traces, finding that 83\% of perfect-outcome traces contain violations. MANTRA \citep{mantra_2026} synthesizes SMT-validated compliance benchmarks from procedural manuals. $\tau$-bench \citep{tau_bench_2024} and its successor $\tau^2$-bench \citep{tau2_bench_2025} provide the conversational agent evaluation platforms. 
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ad5f9eff-9070-42dc-b60a-4d57d0a4532e",
  "isSidechain": true,
  "promptId": "97940243-dcdb-4134-8cbb-a2e35e11a449",
  "agentId": "aec8d190c3a37fd6c",
  "type": "user",
  "uuid": "8f2cfc54-e7fb-4216-b78b-191c6d645c26",
  "sourceToolAssistantUUID": "ad5f9eff-9070-42dc-b60a-4d57d0a4532e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper",
  "sessionId": "46389320-86e2-42d7-b5e1-48bec7f5ca1b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-21T22:40:23.631Z_

<details open><summary>🔧 Tool call — Read · `toolu_019kZcffYcferES9DRqXtS76`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/taxonomy.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8f2cfc54-e7fb-4216-b78b-191c6d645c26",
  "isSidechain": true,
  "agentId": "aec8d190c3a37fd6c",
  "requestId": "req_011CbGX2ynvNuxiGnfQsCdQe",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "bbbe64f0-c4a1-45b8-878b-9214f6184597",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper",
  "sessionId": "46389320-86e2-42d7-b5e1-48bec7f5ca1b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_015M2g8gp5G8yzTt1gganJDe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 36172,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 36172,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 6,
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

_source line 10 · 2026-05-21T22:40:23.638Z_

<details><summary>↩ Tool result · `toolu_019kZcffYcferES9DRqXtS76`</summary>

```text
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
17	\item \textbf{Authorization scope}: vague permission or role boundaries (e.g., ``authorized personnel may issue refunds'' without specifying which personnel or under what conditions).
18	\item \textbf{Incompleteness}: missing conditions, exceptions, or boundary cases (e.g., a return policy that specifies the return window but not what happens when the item is damaged). (Note: unlike other types where the unambiguous variant rephrases existing content, incompleteness resolution requires adding new policy content, a confound we address in \S\ref{sec:results}.)
19	\item \textbf{Conditional precedence}: conflicting or overlapping rules without priority ordering (e.g., ``premium customers receive free shipping'' and ``orders under \$50 require a shipping fee'' without specifying which rule takes precedence for a premium customer with a \$30 order).
20	\end{itemize}
21	
22	The layer distinction reflects the hypothesis that linguistic ambiguity can be partially resolved through tool responses, user context, or world knowledge, while specification ambiguity has no external resolution channel available to the agent, forcing it to guess. We test this hypothesis empirically in \S\ref{sec:results} and \S\ref{sec:analysis}. The linguistic/specification layer distinction is a theoretical organizing principle; \S\ref{sec:results} tests whether it corresponds to an empirical grouping.
23	
24	\paragraph{Scope of `ambiguity.'}
25	Our taxonomy uses \emph{ambiguity} broadly to encompass policy specification features that admit multiple operationally distinct interpretations by an LLM agent. Authorization scope overlaps with \emph{vagueness} \citep{kennedy_vagueness_2007}, incompleteness with \emph{information absence} (resolution requires adding content), and conditional precedence with \emph{normative conflict} between individually unambiguous rules. \citet{dalpiaz_pinpointing_2018} show that ambiguity and incompleteness frequently co-occur in requirements specifications, supporting their unified treatment. We adopt this inclusive definition because LLM agents process all six types identically---committing to a single interpretation without flagging uncertainty---and the resulting safety violations are behaviorally indistinguishable (\S\ref{sec:results}).
26	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bbbe64f0-c4a1-45b8-878b-9214f6184597",
  "isSidechain": true,
  "promptId": "97940243-dcdb-4134-8cbb-a2e35e11a449",
  "agentId": "aec8d190c3a37fd6c",
  "type": "user",
  "uuid": "718c71e8-0419-46e7-86e6-3dad6753088c",
  "sourceToolAssistantUUID": "bbbe64f0-c4a1-45b8-878b-9214f6184597",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper",
  "sessionId": "46389320-86e2-42d7-b5e1-48bec7f5ca1b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-21T22:40:23.800Z_

<details open><summary>🔧 Tool call — Read · `toolu_014NnasABwCXUjCvn64kz4QS`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "718c71e8-0419-46e7-86e6-3dad6753088c",
  "isSidechain": true,
  "agentId": "aec8d190c3a37fd6c",
  "requestId": "req_011CbGX2ynvNuxiGnfQsCdQe",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "4e500fb4-a866-4237-83c9-f68ff2bc2b84",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper",
  "sessionId": "46389320-86e2-42d7-b5e1-48bec7f5ca1b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_015M2g8gp5G8yzTt1gganJDe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 36172,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 36172,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 6,
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

_source line 12 · 2026-05-21T22:40:23.806Z_

<details><summary>↩ Tool result · `toolu_014NnasABwCXUjCvn64kz4QS`</summary>

```text
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
16	We evaluate five models spanning four providers and two architecture families: GPT-5.4 and GPT-4.1 (OpenAI, proprietary dense), Claude Sonnet 4.6 (Anthropic, proprietary dense), Qwen3-235B (Alibaba, open-source Mixture-of-Experts), and DeepSeek-V3 (DeepSeek, open-source dense). This selection covers frontier and mid-tier proprietary models alongside open-source alternatives with different training philosophies. All API calls use temperature $= 0$, top\_p $= 1$, and max\_tokens $= 4096$, and were made on May 20, 2026.
17	
18	\subsection{Evaluation}
19	
20	We use a cross-judge design to mitigate self-evaluation bias: GPT-5.4 judges Claude, GPT-4.1, and Qwen3 traces; GPT-4.1 judges GPT-5.4 and DeepSeek traces. Because our matched-pair design compares ambiguous and unambiguous conditions within the same model--judge pairing, any systematic judge bias cancels in the treatment effect ($\Delta$pp); the cross-judge asymmetry affects only absolute violation rates, not C1 or C2 (\S\ref{sec:limitations}). Judges classify each episode outcome on a four-tier severity scale: none, minor, moderate, and critical. Our primary analysis uses moderate-or-above severity as the violation threshold; minor-only deviations (6.6\% of episodes) are excluded. Including minor violations (overall rate 49.6\% vs.\ 41.0\%) produces even larger effects without changing any directional conclusion.
21	
22	\paragraph{Cross-judge calibration.} To quantify potential judge bias, we conducted a dual-judge calibration on 100 stratified episodes (60 from GPT-5.4, 40 from other models; 65\% ambiguous). Both judges evaluated each episode independently. McNemar's test reveals no systematic detection bias ($p = 0.606$; GPT-4.1-only violations: 9, GPT-5.4-only: 6). Binary agreement is substantial ($\kappa = 0.653$), with weighted four-tier severity agreement reaching $\kappa_w = 0.775$. Per-type binary agreement ranges from $\kappa = 0.385$ (authorization scope) to $0.875$ (incompleteness); severity-level divergence does not affect core conclusions since our primary analyses use binary thresholds (Appendix~\ref{app:severity}).
23	
24	\paragraph{Human validation.} Two annotators (NLP background), blind to LLM labels and condition, labeled 100 stratified episodes on the four-tier scale. Inter-annotator agreement is substantial ($\kappa = 0.798$, $\kappa_w = 0.762$). Pooled human--LLM agreement ($\kappa = 0.733$, $\kappa_w = 0.807$; per-type breakdown in Appendix~\ref{app:per_type_agreement}) approaches inter-annotator levels, validating the automated pipeline \citep{zheng_llm_judge_2024}. Per-type estimates ($n = 32$--$34$ each) validate the pipeline overall but lack power for type-level comparison.
25	
26	\subsection{Controls}
27	
28	\paragraph{Perturbation control.} To confirm specificity to semantic ambiguity, we run 300 episodes with non-ambiguity perturbations (synonym substitution, clause reordering). The perturbation effect is $\Delta_{\text{perturb}} = -0.67$ pp (95\% CI $[-8.0, 6.67]$, containing zero). Even under the worst-case CI bound (6.67 pp), the residual attributable to ambiguity is $\geq$27.3 pp. This control tests surface-level perturbation specificity; the information-addition confound specific to incompleteness is addressed separately via logistic regression (Appendix~\ref{app:confound}).
29	
30	\paragraph{Reproducibility.} A replication of 30 clause pairs $\times$ 2 models $\times$ 3 replicates yields ICC $= 0.919$ (95\% CI $[0.892, 0.940]$). ICC is computed within the OpenAI family; cross-provider stability is supported by C1 consistency across all seven models.
31	
32	\subsection{Statistical Analysis}
33	
34	We use McNemar's test for paired binary outcomes, $\chi^2$ tests with Cram\'{e}r's $V$ for omnibus effects, Fisher's exact test for per-type comparisons, and TOST equivalence testing \citep{lakens_2017} with a primary SESOI of $\pm 15$ pp. This margin is anchored in a domain-relevant criterion: a type producing $\geq$15 pp more violations warrants distinct policy handling in deployment, and it exceeds the perturbation control bound (6.67\,pp) by $>$2$\times$. We acknowledge margin dependence \citep{anvari_lakens_2021}: 3/6 mid-tier pairs are equivalent at $\pm 10$ pp, all six at $\pm 15$ pp (Table~\ref{tab:tost_sensitivity}). No field-standard SESOI exists for agent policy compliance; $\pm 15$\,pp is a pragmatic threshold exceeding measurement noise by $>$2$\times$, and we present full sensitivity across seven margins to enable evaluation at any preferred threshold. We complement TOST with a margin-free bootstrap cluster analysis (Ward's method, $B = 10{,}000$; \S\ref{sec:results}). We apply Holm--Bonferroni correction within three pre-registered test families (Appendix~\ref{app:multiple_comparison}). Post-hoc power exceeds 0.99 for both C1 and C2; TOST power at $\pm 15$ pp is 0.94, dropping to 0.57 at $\pm 10$ pp.
35	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4e500fb4-a866-4237-83c9-f68ff2bc2b84",
  "isSidechain": true,
  "promptId": "97940243-dcdb-4134-8cbb-a2e35e11a449",
  "agentId": "aec8d190c3a37fd6c",
  "type": "user",
  "uuid": "00ab4499-6c11-464b-aed2-674fe05967da",
  "sourceToolAssistantUUID": "4e500fb4-a866-4237-83c9-f68ff2bc2b84",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper",
  "sessionId": "46389320-86e2-42d7-b5e1-48bec7f5ca1b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-21T22:40:24.202Z_

<details open><summary>🔧 Tool call — Read · `toolu_01RT8krzNLhKgSeWrkkRW7bT`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "00ab4499-6c11-464b-aed2-674fe05967da",
  "isSidechain": true,
  "agentId": "aec8d190c3a37fd6c",
  "requestId": "req_011CbGX2ynvNuxiGnfQsCdQe",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "e344b062-9810-4b60-8497-583014baac50",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper",
  "sessionId": "46389320-86e2-42d7-b5e1-48bec7f5ca1b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_015M2g8gp5G8yzTt1gganJDe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 36172,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 36172,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 6,
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

_source line 14 · 2026-05-21T22:40:24.208Z_

<details><summary>↩ Tool result · `toolu_01RT8krzNLhKgSeWrkkRW7bT`</summary>

```text
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
14	\caption{Violation rates (\%) under ambiguous policy clauses by type and model. $\Delta$pp denotes the pooled difference between ambiguous and unambiguous conditions across all five models. All per-type differences are significant ($p < 10^{-5}$, Fisher's exact test).}
15	\label{tab:main_results}
16	\small
17	\begin{tabular}{llrrrrrrrr}
18	\toprule
19	Layer & Type & Pooled & GPT-5.4 & GPT-4.1 & Claude & Qwen3 & DeepSeek & $\Delta$pp & $p$ \\
20	\midrule
21	\multirow{3}{*}{\textcolor{speccolor}{Spec.}} & Incompleteness & 53.6 & 46.0 & 58.0 & 48.0 & 62.0 & 54.0 & +49.2 & $<10^{-37}$ \\
22	 & Auth.\ Scope & 41.6 & 64.0 & 46.0 & 12.0 & 26.0 & 60.0 & +36.0 & $<10^{-22}$ \\
23	 & Cond.\ Precedence & 36.8 & 34.0 & 36.0 & 36.0 & 40.0 & 38.0 & +30.8 & $<10^{-17}$ \\
24	\midrule
25	\multirow{3}{*}{\textcolor{lingcolor}{Ling.}} & Lexical & 42.8 & 42.0 & 34.0 & 32.0 & 52.0 & 54.0 & +35.2 & $<10^{-20}$ \\
26	 & Scopal & 39.4 & 42.0 & 38.0 & 32.0 & 36.7 & 48.0 & +34.2 & $<10^{-21}$ \\
27	 & Coreferential & 31.6 & 18.0 & 32.0 & 22.0 & 42.0 & 44.0 & +18.7 & $<10^{-6}$ \\
28	\midrule
29	\multicolumn{2}{l}{\textbf{Overall}} & \textbf{41.0} & 41.0 & 40.7 & 30.3 & 43.1 & 49.7 & \textbf{+34.0} & $<10^{-105}$ \\
30	\bottomrule
31	\end{tabular}
32	\end{table*}
33	
34	The six types are not interchangeable. An omnibus $\chi^2$ test on ambiguous-condition violation rates rejects the uniformity null ($\chi^2 = 28.02$, $df = 5$, $p = 3.6 \times 10^{-5}$, Cram\'{e}r's $V = 0.137$; statistical power $= 0.993$ at the observed effect). TOST equivalence testing at a $\pm 15$ pp margin reveals a two-tier structure among five types---authorization scope (41.6\%), lexical (42.8\%), scopal (39.4\%), and conditional precedence (36.8\%) form a mid-tier cluster, with coreferential (31.6\%) below---while incompleteness (53.6\%) stands apart as an upper bound---conditional on the confound controls in Appendix~\ref{app:confound}---whose ranking partly reflects an information-addition confound. Table~\ref{tab:main_results} and Figure~\ref{fig:forest_plot} present the full breakdown.
35	
36	Sensitivity analysis across seven margins ($\pm 5$--$20$ pp; Appendix~\ref{app:tost}) confirms this structure: the two-tier pattern emerges at $\pm 12$ pp (5/6 mid-tier pairs equivalent) and stabilizes at $\pm 15$ pp (6/6). A margin-free bootstrap cluster analysis (Ward's method, $B = 10{,}000$) corroborates: at $k = 2$, incompleteness forms a singleton with the remaining five types in one cluster; at $k = 3$, coreferential additionally separates---consistent with the TOST two-tier pattern (Appendix~\ref{app:cluster}).
37	At $\pm 10$\,pp, only three mid-tier pairs reach equivalence; the incompleteness upper-bound is robust across all margins while mid-tier cohesion is margin-dependent. Cross-model type ranking concordance is moderate (Kendall's $W$; Appendix~\ref{app:kendall_w}).
38	
39	Incompleteness is highest in four of five models (rates $\geq$46\% in all seven; Appendix~\ref{app:model_expansion}). Its unambiguous variant adds policy content, so the 49.2\,pp effect is an upper bound; a confound analysis confirms significance after controlling for information delta (Appendix~\ref{app:confound}). Coreferential, whose variants are lexically identical, provides a confound-free lower bound at 31.6\%.
40	
41	\begin{figure}[t]
42	\centering
43	\includegraphics[width=\columnwidth]{figures/fig2_forest_plot.pdf}
44	\caption{Per-type effect sizes ($\Delta$pp, ambiguous minus unambiguous) with Newcombe 95\% CIs. All types produce significant increases. A two-tier structure emerges among five types (mid cluster $\gg$ coreferential), with incompleteness as an upper bound partly reflecting an information-addition confound.}
45	\label{fig:forest_plot}
46	\end{figure}
47	
48	\subsection{Layer Effect (C3)}
49	
50	Specification-layer types trend higher than linguistic-layer types (44.0\% vs.\ 37.9\%, $p = 0.017$), but C3 is inconclusive: it does not survive Holm--Bonferroni correction, and controlling for token delta reverses the direction. Cross-layer type overlap (conditional precedence 36.8\% vs.\ scopal 39.4\%) further undermines the distinction. The null C3 result does not diminish the taxonomy's operational value: type-level distinctions (C2) hold independently of layer grouping, and the layer distinction retains value as a theoretical organizing principle even without a measurable effect-size gap.
51	
52	\subsection{Model $\times$ Type Interaction (C4) \emph{[Exploratory]}}
53	\label{sec:c4}
54	
55	\begin{figure*}[t]
56	\centering
57	\includegraphics[width=\textwidth]{figures/fig3_heatmap.pdf}
58	\caption{Violation rates (\%) by model and ambiguity type under ambiguous conditions ($n = 2{,}997$). Authorization scope varies 52 pp across models (Claude 12\% to GPT-5.4 64\%), while incompleteness remains uniformly high (46--62\%).}
59	\label{fig:heatmap}
60	\end{figure*}
61	
62	A model main effect is significant ($\chi^2 = 31.02$, $p = 3.0 \times 10^{-6}$, $V = 0.102$), with Claude (30.3\%) substantially less vulnerable than DeepSeek (49.7\%). Model identity explains only 1.0\% of total violation variance; the significant interaction ($F(20, 2976) = 1.97$, $p = 0.006$; $\mathrm{df} = (5{-}1) \times (6{-}1) = 20$; 2.9\% of variance; confirmed by logistic regression likelihood ratio test: $\chi^2(20) = 47.20$, $p = 5.5 \times 10^{-4}$) concentrates in specific type--model combinations.
63	
64	Figure~\ref{fig:heatmap} highlights three suggestive patterns: (1) authorization scope is the \emph{most model-differentiating type} (52 pp range; Claude 12\% to GPT-5.4 64\%), though this type has the lowest judge agreement ($\kappa = 0.385$; \S\ref{sec:limitations}), so absolute rates carry more uncertainty than for other types; (2) incompleteness is a \emph{consistent vulnerability} (46--62\%, 16 pp range); (3) conditional precedence is the most \emph{model-invariant type} (34--40\%, 6 pp range). The authorization scope ranking (Claude $<$ Qwen3 $<$ GPT-4.1) is stable within the GPT-5.4 judge subset (bootstrap ranking preservation: 99.5\%, $B = 10{,}000$; pairwise orderings $\geq$99.5\%), controlling for judge identity. The 48\,pp within-judge range far exceeds measurement noise, but given the low cross-judge $\kappa$, we characterize this pattern as suggestive rather than definitive. Excluding authorization scope, the residual interaction vanishes ($p = 0.97$; Appendix~\ref{app:c4_sans_auth}), confirming that the C4 interaction concentrates in this single type. Given the low inter-judge agreement on authorization scope ($\kappa = 0.385$), the 52\,pp range should be treated as an upper bound with substantial measurement uncertainty rather than a precise estimate.
65	
66	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e344b062-9810-4b60-8497-583014baac50",
  "isSidechain": true,
  "promptId": "97940243-dcdb-4134-8cbb-a2e35e11a449",
  "agentId": "aec8d190c3a37fd6c",
  "type": "user",
  "uuid": "17989e96-9a0d-4463-acc8-b6fc163f3ae8",
  "sourceToolAssistantUUID": "e344b062-9810-4b60-8497-583014baac50",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper",
  "sessionId": "46389320-86e2-42d7-b5e1-48bec7f5ca1b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-21T22:40:24.422Z_

<details open><summary>🔧 Tool call — Read · `toolu_015f3TXMAVGEdKMrZmF8pfti`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "17989e96-9a0d-4463-acc8-b6fc163f3ae8",
  "isSidechain": true,
  "agentId": "aec8d190c3a37fd6c",
  "requestId": "req_011CbGX2ynvNuxiGnfQsCdQe",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "c4a4c59a-d658-4595-8bea-93d02729bdf2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper",
  "sessionId": "46389320-86e2-42d7-b5e1-48bec7f5ca1b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_015M2g8gp5G8yzTt1gganJDe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 36172,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 36172,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 6,
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

_source line 16 · 2026-05-21T22:40:24.428Z_

<details><summary>↩ Tool result · `toolu_015f3TXMAVGEdKMrZmF8pfti`</summary>

```text
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
16	\emph{Boundary violation} (unauthorized escalation): the agent exceeds permission boundaries when authorization scope is underspecified---e.g., issuing a refund above its stated limit rather than escalating; 69.2\% of such violations involve unauthorized escalation with zero conservative refusals ($p < 10^{-4}$, binomial test), revealing systematic permissiveness bias. This dominates authorization scope exclusively (all 5 models).
17	
18	Each type's dominant failure mode is majority-consistent ($\geq$3/5 models), with three achieving unanimity. The layer distinction does not hold mechanistically: conditional precedence shares its mode with scopal, while authorization scope follows a unique boundary-violation pattern.
19	
20	\subsection{Disambiguation Deficit}
21	
22	Agents rarely recognize ambiguity. We code \emph{disambiguation awareness} (acknowledging multiple interpretations, asking clarifying questions, or conditioning on ambiguity) versus \emph{surface adoption} (proceeding with a single interpretation). Overall disambiguation awareness is 4.6\%: Claude (11.0\%) and GPT-4.1 (10.7\%) show the highest rates, while Qwen3 and DeepSeek show zero across all 278 combined violation traces.
23	
24	We term this the \emph{Disambiguation Deficit}---a default behavioral pattern in uninstructed settings, not an inherent inability. Unlike humans, agents proceed with full confidence in a single interpretation, consistent with \citet{hu_ambiguity_2025}'s finding that LLM ambiguity reflects missing conceptual representations. Our mitigation experiment ($-$8.5\,pp; Appendix~\ref{app:mitigation}) confirms that disambiguation can be elicited, paralleling human good-enough processing \citep{ferreira_good_enough_2002}.
25	
26	\subsection{Systematic Nocuity}
27	
28	Among ambiguous clauses, 41.3\% trigger majority-convergent violations ($\geq$3/5 models), with 13\% producing universal violations. This extends \citet{berry_kamsties_2004}'s framework with \emph{systematic nocuity}: all models converge on the same incorrect interpretation, invisible in agreement-based evaluation. Incompleteness has the highest universal convergence (24\%).
29	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c4a4c59a-d658-4595-8bea-93d02729bdf2",
  "isSidechain": true,
  "promptId": "97940243-dcdb-4134-8cbb-a2e35e11a449",
  "agentId": "aec8d190c3a37fd6c",
  "type": "user",
  "uuid": "e430199f-59cf-4ffb-9f86-bfbbf2ade09d",
  "sourceToolAssistantUUID": "c4a4c59a-d658-4595-8bea-93d02729bdf2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper",
  "sessionId": "46389320-86e2-42d7-b5e1-48bec7f5ca1b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-21T22:40:24.637Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Xae7F3X4meeNwPMHmDU1qj`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e430199f-59cf-4ffb-9f86-bfbbf2ade09d",
  "isSidechain": true,
  "agentId": "aec8d190c3a37fd6c",
  "requestId": "req_011CbGX2ynvNuxiGnfQsCdQe",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "4a2b9756-8d16-4d7e-9d00-757fb791e3b6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper",
  "sessionId": "46389320-86e2-42d7-b5e1-48bec7f5ca1b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_015M2g8gp5G8yzTt1gganJDe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 36172,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 36172,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 6,
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

_source line 18 · 2026-05-21T22:40:24.643Z_

<details><summary>↩ Tool result · `toolu_01Xae7F3X4meeNwPMHmDU1qj`</summary>

```text
1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Differential nocuity.}
5	Building on \citet{berry_kamsties_2004}'s nocuous/innocuous distinction and \citet{willis_nocuous_2008}'s detection work, our results can be interpreted through a \emph{differential nocuity} lens: risk depends on ambiguity type (base vulnerability), safety training (selective mitigation), and disambiguation channel availability. This generates two testable predictions: (P1) types with explicit decision points should show larger safety-training gains than gap-filling types; (P2) disambiguation channels should reduce violations more for high-deficit types. Our mitigation experiment (Appendix~\ref{app:mitigation}) is consistent with, though not a formal test of, P1 ($-18.0$\,pp for authorization scope vs.\ $-3.4$\,pp for incompleteness).
6	
7	\paragraph{Practical implications.}
8	A proof-of-concept classifier (Appendix~\ref{app:detection}) achieves F1\,=\,0.81 for binary ambiguity detection but only 0.34 for incompleteness---the highest-risk type is the hardest to detect. With agents exhibiting disambiguation deficit in $>$89\% of cases, type-aware auditing and externalized detection \citep{chantree_2006,ferrari_ambiguity_2019} are necessary for policy-governed deployments.
9	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4a2b9756-8d16-4d7e-9d00-757fb791e3b6",
  "isSidechain": true,
  "promptId": "97940243-dcdb-4134-8cbb-a2e35e11a449",
  "agentId": "aec8d190c3a37fd6c",
  "type": "user",
  "uuid": "366dbe30-5fd4-4ed1-a66d-b83b67b39760",
  "sourceToolAssistantUUID": "4a2b9756-8d16-4d7e-9d00-757fb791e3b6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper",
  "sessionId": "46389320-86e2-42d7-b5e1-48bec7f5ca1b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-21T22:40:24.844Z_

<details open><summary>🔧 Tool call — Read · `toolu_01SE1ePfavP2zGYGWM9RHsEb`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "366dbe30-5fd4-4ed1-a66d-b83b67b39760",
  "isSidechain": true,
  "agentId": "aec8d190c3a37fd6c",
  "requestId": "req_011CbGX2ynvNuxiGnfQsCdQe",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "e58b488a-e1df-4edd-9200-fdb45293a4e9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper",
  "sessionId": "46389320-86e2-42d7-b5e1-48bec7f5ca1b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_015M2g8gp5G8yzTt1gganJDe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 36172,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 36172,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 6,
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

_source line 20 · 2026-05-21T22:40:24.855Z_

<details><summary>↩ Tool result · `toolu_01SE1ePfavP2zGYGWM9RHsEb`</summary>

```text
1	\section{Conclusion}
2	
3	Ambiguous policy clauses increase agent safety violations by 34.0\,pp (OR\,$=$\,15.1) across five models, with clause identity explaining 22$\times$ more variance than model identity. The two-tier type hierarchy replicates across seven models ($\rho = 0.60$--$0.90$). With agents exhibiting disambiguation deficit in over 89\% of cases, type-aware auditing and externalized detection are critical for policy-governed deployments.
4	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e58b488a-e1df-4edd-9200-fdb45293a4e9",
  "isSidechain": true,
  "promptId": "97940243-dcdb-4134-8cbb-a2e35e11a449",
  "agentId": "aec8d190c3a37fd6c",
  "type": "user",
  "uuid": "2b3879e9-e728-464e-9e06-9db5224d11cb",
  "sourceToolAssistantUUID": "e58b488a-e1df-4edd-9200-fdb45293a4e9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper",
  "sessionId": "46389320-86e2-42d7-b5e1-48bec7f5ca1b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-21T22:40:25.055Z_

<details open><summary>🔧 Tool call — Read · `toolu_01DHr1SF6yfQHa9hKcch3HBz`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2b3879e9-e728-464e-9e06-9db5224d11cb",
  "isSidechain": true,
  "agentId": "aec8d190c3a37fd6c",
  "requestId": "req_011CbGX2ynvNuxiGnfQsCdQe",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "e93ac9b7-57f1-4274-9a18-f825273f912c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper",
  "sessionId": "46389320-86e2-42d7-b5e1-48bec7f5ca1b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_015M2g8gp5G8yzTt1gganJDe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 36172,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 36172,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 6,
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

_source line 22 · 2026-05-21T22:40:25.060Z_

<details><summary>↩ Tool result · `toolu_01DHr1SF6yfQHa9hKcch3HBz`</summary>

```text
1	\section*{Limitations}
2	\label{sec:limitations}
3	
4	\paragraph{Model coverage.} We evaluate seven API-accessible models from six providers (four proprietary, three open-source; two in replication, Appendix~\ref{app:model_expansion}). Smaller open-source models (7B--70B parameters) may show different vulnerability patterns, and our findings may not generalize to models with fundamentally different training approaches.
5	
6	\paragraph{Domain scope.} $\tau^2$-bench covers retail and airline customer service. Policy ambiguity effects in other domains (healthcare, finance, legal) remain to be tested, though the within-study cross-domain consistency is encouraging: failure mode distributions share the same top-two modes (assumption-based action and unauthorized escalation) across domains, with individual mode base rates differing by up to 12.5 pp, likely reflecting domain policy structure rather than methodological artifacts.
7	
8	\paragraph{Synthetic ambiguity.} Our matched-pair design requires synthetic construction of ambiguous variants, which may not capture the full distribution of naturally occurring policy ambiguities. We mitigate this through expert review and a realism validation comparing ambiguous clauses against original $\tau^2$-bench policy text. Ambiguous clauses are indistinguishable from originals in lexical diversity (TTR, KS $p = 0.89$) and word length ($p = 0.09$). Readability is slightly higher (Flesch--Kincaid $d = 0.29$, $p = 0.006$) and sentence length moderately higher ($d = 0.74$), both reflecting the structural demands of encoding ambiguity in standalone clauses. Across matched pairs, disambiguation preserves readability (Flesch--Kincaid $d = 0.14$, $p = 0.10$), confirming that minimal edits change semantic precision without altering linguistic register.
9	
10	\paragraph{Cross-judge asymmetry.} Although our dual-judge calibration (\S\ref{sec:method}) shows no systematic bias ($p = 0.606$) and human validation confirms the LLM judge operates within inter-annotator disagreement (human--LLM $\kappa = 0.733$ vs.\ inter-annotator $\kappa = 0.798$), each agent model is evaluated by a single cross-judge, so judge identity remains confounded with model identity. Per-type reliability varies: authorization scope has the lowest judge agreement ($\kappa = 0.385$), so the absolute violation rates for this type carry more uncertainty than for incompleteness ($\kappa = 0.875$). Human--LLM agreement shows the same pattern (auth.\ scope $\kappa = 0.644$ vs.\ lexical $\kappa = 0.904$; Appendix~\ref{app:per_type_agreement}). Within-judge-group analyses confirm C1 (both $p < 0.001$) but neither subgroup reaches significance for C3 individually (GPT-4.1--judged: $p = 0.059$; GPT-5.4--judged: $p = 0.157$), leaving open the possibility that the pooled C3 result partly reflects judge-level variance.
11	Cross-provider test-retest reliability remains unmeasured; ICC $= 0.919$ covers only OpenAI models. Cross-model type ranking concordance is moderate (five-model $W = 0.398$, $p = 0.072$; seven-model $W = 0.353$, $p = 0.038$; Appendix~\ref{app:kendall_w}), with the marginal five-model result reflecting the model$\times$type interaction documented in C4. Within-judge-group type rankings are reported in Appendix~\ref{app:judge_group_ranking}.
12	
13	\paragraph{Failure mode analysis.} The failure mode taxonomy (\S\ref{sec:analysis}) was coded across all five models (614 traces) using LLM-based coders with substantial inter-coder agreement (Gwet's AC$_1$ $= 0.62$; Cohen's $\kappa = 0.52$). The moderate $\kappa$ reflects the prevalence paradox rather than systematic disagreement, but per-category reliability for minority categories remains limited (e.g., arbitrary rule selection $\kappa = 0.29$). Human validation of the coding scheme would further strengthen these findings.
14	
15	\paragraph{Incompleteness confound.} As discussed in \S\ref{sec:results}, incompleteness resolution necessarily adds policy content, creating an information asymmetry. Our logistic regression controls and the coreferential lower-bound analysis mitigate this confound, but a future design that orthogonalizes information quantity from ambiguity resolution would strengthen causal claims for this type specifically.
16	
17	\paragraph{Severity threshold.} Our primary analysis uses moderate-or-above severity. Switching to any-violation (including minor) yields $\Delta = 38.2$ pp (vs.\ 34.0 pp), with all four claims (C1--C4) remaining significant. Type rankings under the two thresholds are concordant (Kendall $\tau = 0.73$), with incompleteness ranking first under both.
18	
19	\paragraph{Per-type reliability.} Per-type human--LLM $\kappa$ estimates (Appendix~\ref{app:per_type_agreement}) are based on small cell sizes ($n = 32$--$34$), yielding wide confidence intervals (scopal: $[0.00, 1.00]$; coreferential: $[0.00, 0.84]$). These estimates should not be over-interpreted at the individual type level.
20	
21	\section*{Data and Code Availability}
22	The 300 clause pairs, evaluation pipeline, analysis scripts, and raw episode traces will be released upon publication at \url{https://github.com/anonymous/policy-ambiguity-safety}.
23	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e93ac9b7-57f1-4274-9a18-f825273f912c",
  "isSidechain": true,
  "promptId": "97940243-dcdb-4134-8cbb-a2e35e11a449",
  "agentId": "aec8d190c3a37fd6c",
  "type": "user",
  "uuid": "5b6819ff-35a9-47f5-88ed-f566559ccaa3",
  "sourceToolAssistantUUID": "e93ac9b7-57f1-4274-9a18-f825273f912c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper",
  "sessionId": "46389320-86e2-42d7-b5e1-48bec7f5ca1b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-21T22:40:25.262Z_

<details open><summary>🔧 Tool call — Read · `toolu_01S4K6rCUagZQhDN9NN2QNrh`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5b6819ff-35a9-47f5-88ed-f566559ccaa3",
  "isSidechain": true,
  "agentId": "aec8d190c3a37fd6c",
  "requestId": "req_011CbGX2ynvNuxiGnfQsCdQe",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "aa398e36-7b11-4028-8df3-09ce2769ed9f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper",
  "sessionId": "46389320-86e2-42d7-b5e1-48bec7f5ca1b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_015M2g8gp5G8yzTt1gganJDe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 36172,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 36172,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 6,
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

_source line 24 · 2026-05-21T22:40:25.267Z_

<details><summary>↩ Tool result · `toolu_01S4K6rCUagZQhDN9NN2QNrh`</summary>

```text
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
29	Table~\ref{tab:mitigation} reports the per-type, per-model $\Delta$pp from the disambiguation-instruction mitigation experiment (1,256 treatment episodes across five of six types; coreferential was not tested). Coreferential pairs are excluded from both the mitigation and replication experiments. In mitigation, their ambiguous and unambiguous variants differ only in pronoun resolution, making it impossible to craft targeted disambiguation instructions without revealing the experimental manipulation. In replication, the $\tau^2$-bench episode design for coreferential ambiguity is tightly coupled to the original five-model configuration; extending it to new model families would require redesigning the episode templates, which falls outside the scope of this confirmatory replication. The treatment appends a type-specific disambiguation instruction to the agent's system prompt. Control rates are the matched 5-type subset from the full study (\S\ref{sec:results}).
30	
31	\begin{table*}[!ht]
32	\centering
33	\small
34	\caption{Violation rate change ($\Delta$pp) after adding type-specific disambiguation instructions. Negative values indicate reduction. Baseline violation rates are shown in parentheses. Coreferential was excluded because it was not included in the mitigation experiment.}
35	\label{tab:mitigation}
36	\begin{tabular}{lrrrrrr}
37	\toprule
38	Type & GPT-5.4 & GPT-4.1 & Claude & Qwen3 & DeepSeek & Pooled \\
39	\midrule
40	Auth.\ scope & $-40.0$ (64) & $-26.0$ (46) & $0.0$ (12) & $-14.0$ (26) & $-10.0$ (60) & $-18.0$ (42) \\
41	Lexical & $-16.5$ (42) & $-10.0$ (34) & $-8.0$ (32) & $-8.0$ (52) & $-2.0$ (54) & $-8.9$ (43) \\
42	Cond.\ prec. & $-4.6$ (34) & $-10.0$ (36) & $-12.0$ (36) & $-2.0$ (40) & $-12.0$ (38) & $-8.1$ (37) \\
43	Scopal & $-6.7$ (42) & $-4.0$ (38) & $-10.0$ (32) & $-2.7$ (37) & $+2.0$ (48) & $-4.3$ (39) \\
44	Incomp. & $-2.6$ (46) & $-14.0$ (58) & $-2.0$ (48) & $-2.0$ (62) & $+4.0$ (54) & $-3.4$ (54) \\
45	\midrule
46	Overall & $-14.0$ (46) & $-12.8$ (42) & $-6.4$ (32) & $-5.8$ (43) & $-3.6$ (51) & $-8.5$ (43) \\
47	\bottomrule
48	\end{tabular}
49	\end{table*}
50	
51	\section{Severity Threshold Comparison}
52	\label{app:severity}
53	
54	Table~\ref{tab:severity_comparison} compares all four claims under two violation severity thresholds. The primary analysis uses moderate-or-above; the alternative includes 198 additional minor violations (6.6\% of episodes).
55	
56	\begin{table}[!ht]
57	\centering
58	\small
59	\caption{Claim-level comparison under two severity thresholds.}
60	\label{tab:severity_comparison}
61	\begin{tabular}{llll}
62	\toprule
63	Claim & Moderate+ & Any-violation & Concordance \\
64	\midrule
65	C1 $\Delta$ & 34.0 pp & 38.2 pp & Both $p < 10^{-50}$ \\
66	C2 $V$ & 0.137 & 0.169 & Both $p < 10^{-4}$ \\
67	C3 $\Delta$ & 6.1 pp & 7.4 pp & Both $p < 0.02$ \\
68	C4 $V$ & 0.102 & 0.097 & Both $p < 10^{-5}$ \\
69	\midrule
70	\multicolumn{2}{l}{Type ranking} & \multicolumn{2}{l}{Kendall $\tau = 0.73$, $p = 0.056$} \\
71	\bottomrule
72	\end{tabular}
73	\end{table}
74	
75	\section{Ambiguity Type Detection Experiment}
76	\label{app:detection}
77	
78	To assess whether our taxonomy supports automated identification, we conduct a proof-of-concept detection experiment using GPT-4.1 as a zero-shot classifier. Given a policy clause, the classifier determines (1)~whether it contains ambiguity and (2)~the specific type from a five-type subset of our taxonomy. Coreferential ambiguity is excluded because its variants are lexically identical to their unambiguous counterparts, making surface-level type detection inapplicable.
79	
80	We evaluate on 500 policy clauses (250 ambiguous, 250 unambiguous) using stratified 5-fold cross-validation, with clause pairs kept in the same fold to prevent leakage. Table~\ref{tab:detection} reports per-type results.
81	
82	\begin{table}[!ht]
83	\centering
84	\small
85	\caption{Proof-of-concept detection classifier (GPT-4.1, zero-shot, 5-fold CV). Binary ambiguity detection: F1\,=\,0.81, FPR\,=\,4.4\%. Six-class macro F1\,=\,0.63.}
86	\label{tab:detection}
87	\begin{tabular}{lrrr}
88	\toprule
89	Type & Prec. & Recall & F1 \\
90	\midrule
91	Cond.\ precedence & 0.96 & 0.92 & 0.94 \\
92	Scopal & 0.91 & 0.64 & 0.75 \\
93	Auth.\ scope & 1.00 & 0.36 & 0.53 \\
94	Lexical & 0.36 & 0.42 & 0.39 \\
95	Incompleteness & 0.48 & 0.26 & 0.34 \\
96	\midrule
97	No ambiguity & 0.76 & 0.96 & 0.85 \\
98	\bottomrule
99	\end{tabular}
100	\end{table}
101	
102	Detection difficulty is inversely correlated with agent vulnerability: incompleteness, the most dangerous type (53.6\% violation rate, \S\ref{sec:results}), is the hardest to detect (F1\,=\,0.34), while conditional precedence (36.8\% violation rate) is the easiest (F1\,=\,0.94). This asymmetry arises because types with overt linguistic signals (e.g., conditional structures) are readily detectable but only moderately dangerous, whereas missing information leaves no surface trace for a classifier to exploit.
103	
104	The primary confusion pathway is authorization scope $\to$ lexical (48\% of authorization scope clauses): authorization boundary clauses frequently contain polysemous terms, causing the classifier to attribute the ambiguity to word-level rather than permission-level underspecification.
105	
106	These results position automated detection as a viable first-pass screening tool (binary F1\,=\,0.81) but an unreliable type classifier, particularly for the highest-risk types. The classifier was evaluated on synthetic clauses derived from $\tau^2$-bench; generalization to naturally occurring policy documents requires further validation.
107	
108	\section{Replication on Additional Model Families}
109	\label{app:model_expansion}
110	
111	To test cross-architecture generalization beyond the five main-study models, we replicate the core analyses on two additional model families: Gemini-2.5-Flash (Google) and LLaMA-4-Scout (Meta), each with 250 clause pairs $\times$ 2 conditions $= 500$ episodes judged by GPT-5.4. These models represent two additional providers not in the original study. We exclude coreferential ambiguity because its disambiguation relies on benchmark-specific assertion structure rather than clause-level text changes (\S\ref{sec:taxonomy}), limiting cross-benchmark generalizability. Tables~\ref{tab:expansion_overall} and~\ref{tab:expansion_pertype} report the results.
112	
113	\begin{table}[!ht]
114	\centering
115	\small
116	\caption{Replication results on two additional model families. C2 rank $\rho$ is computed against the original five-model pooled type ranking.}
117	\label{tab:expansion_overall}
118	\resizebox{\columnwidth}{!}{%
119	\begin{tabular}{lrrrrl}
120	\toprule
121	Model & Amb.\ (\%) & Unamb.\ (\%) & $\Delta$pp & $p$ & C2 $\rho$ \\
122	\midrule
123	Gemini-2.5-Flash & 37.6 & 4.0 & +33.6 & $<10^{-21}$ & 0.60 \\
124	LLaMA-4-Scout & 37.6 & 17.6 & +20.0 & $<10^{-6}$ & 0.90$^*$ \\
125	\bottomrule
126	\end{tabular}}
127	\end{table}
128	
129	\begin{table}[!ht]
130	\centering
131	\small
132	\caption{Per-type ambiguous violation rates (\%) for replication models vs.\ original five-model pooled rates.}
133	\label{tab:expansion_pertype}
134	\begin{tabular}{lrrr}
135	\toprule
136	Type & Gemini & LLaMA & Orig.\ pooled \\
137	\midrule
138	Incompleteness & 48 & 52 & 53.6 \\
139	Lexical & 50 & 38 & 42.8 \\
140	Auth.\ scope & 22 & 40 & 41.6 \\
141	Scopal & 34 & 30 & 39.4 \\
142	Cond.\ prec. & 34 & 28 & 36.8 \\
143	\bottomrule
144	\end{tabular}
145	\end{table}
146	
147	\paragraph{C1 replication.} Both models show significant binary ambiguity effects (Gemini $\Delta = +33.6$\,pp, OR $= 14.5$, $p < 10^{-21}$; LLaMA $\Delta = +20.0$\,pp, OR $= 2.8$, $p < 10^{-6}$), extending C1 to seven models across six providers. Gemini's effect size falls within the original five-model range (+25.7 to +39.0\,pp). LLaMA's smaller effect and lower OR are attributable to an elevated unambiguous baseline (17.6\% vs.\ $<$10\% for all other models), suggesting weaker baseline instruction following that compresses the ambiguity-specific delta. LLaMA 3.3's elevated unambiguous baseline (17.6\% vs.\ 7.3--12.7\% for main-study models) likely reflects weaker baseline instruction following, suggesting that absolute violation rates are model-dependent even absent ambiguity.
148	
149	\paragraph{C2 replication.} Both models' type rankings correlate positively with the original pooled ranking. LLaMA shows a strong and significant correlation ($\rho = 0.90$, $p = 0.037$), with incompleteness as the top type and the bottom three types matching the reference order exactly. Gemini shows a moderate positive correlation ($\rho = 0.60$, $p = 0.285$), with the top two types (lexical and incompleteness) swapped relative to the reference. Incompleteness remains $\geq$46\% in all seven models (range: 46--62\%), confirming its status as a consistent vulnerability independent of architecture or provider. $^*$Significant at $\alpha = 0.05$.
150	
151	\section{Incompleteness Confound Analysis}
152	\label{app:confound}
153	
154	Incompleteness is structurally distinct from the other five types: its unambiguous variant necessarily adds policy content (specifying what was previously missing) rather than merely resolving an existing ambiguity. This raises a confound: the 49.2 pp effect may partly reflect the information addition rather than ambiguity resolution per se.
155	
156	A logistic regression controlling for per-clause information delta (token count difference between ambiguous and unambiguous variants) confirms that incompleteness remains individually significant ($p = 0.022$, coefficient change $< 8\%$ relative to the uncontrolled model). Coreferential ambiguity, whose variants are lexically identical (information delta $= 0$), provides a confound-free lower bound: its 31.6\% violation rate and 18.7 pp effect are entirely attributable to semantic ambiguity. Token count is a coarse proxy for information content; finer-grained semantic measures (e.g., propositional content analysis) may reveal different confound structures.
157	
158	Per-type token deltas between unambiguous and ambiguous variants range from 17.5 words (conditional precedence) to 36.1 words (authorization scope). Notably, authorization scope has the largest delta (36.1) yet lower violation rates than incompleteness (delta 34.6), providing counter-evidence against a pure information-quantity explanation: if token delta drove violations, authorization scope should exceed incompleteness. Coreferential pairs have zero token delta (lexically identical variants), providing a confound-free baseline.
159	
160	Excluding incompleteness entirely, the pooled ambiguity effect remains large and significant ($\Delta = 31.0$\,pp, OR $= 7.75$, $p < 10^{-75}$), confirming that C1 does not depend on any single type.
161	
162	Excluding incompleteness, the remaining five types show a non-significant omnibus difference ($\chi^2$, $p = 0.079$), but pairwise contrasts with Holm--Bonferroni correction reveal a two-tier pattern: authorization scope ($p_{\text{adj}} = 0.039$) and lexical ($p_{\text{adj}} = 0.025$) remain significantly above coreferential, while the four remaining pairs are equivalent at the $\pm 15$ pp margin.
163	
164	\section{Per-Type Judge Reliability}
165	\label{app:per_type_agreement}
166	
167	Table~\ref{tab:per_type_agreement} reports per-type human--LLM binary agreement ($\kappa$) on the 100-episode stratified sample (200 human--LLM rating pairs: two annotators $\times$ corresponding LLM judge). Per-type samples range from 32 to 34 episodes, yielding wide confidence intervals.
168	
169	\begin{table}[!ht]
170	\centering
171	\small
172	\caption{Per-type human--LLM binary agreement (moderate-or-above threshold). CI: bootstrap 95\% confidence interval.}
173	\label{tab:per_type_agreement}
174	\begin{tabular}{lrrl}
175	\toprule
176	Type & $n$ & $\kappa$ & 95\% CI \\
177	\midrule
178	Lexical & 32 & 0.904 & $[0.64, 1.00]$ \\
179	Cond.\ precedence & 34 & 0.837 & $[0.53, 1.00]$ \\
180	Incompleteness & 34 & 0.795 & $[0.56, 1.00]$ \\
181	Auth.\ scope & 34 & 0.644 & $[0.35, 0.91]$ \\
182	Scopal & 32 & 0.636 & $[0.00, 1.00]$ \\
183	Coreferential & 34 & 0.479 & $[0.00, 0.84]$ \\
184	\midrule
185	Overall (pooled) & 200 & 0.735 & $[0.62, 0.85]$ \\
186	\bottomrule
187	\end{tabular}
188	\end{table}
189	
190	Authorization scope has the lowest human--LLM $\kappa$ among the four substantively high-rate types (0.644), consistent with its lowest cross-judge $\kappa$ (0.385, \S\ref{sec:method}). Both reflect the inherent difficulty of permission-boundary judgments rather than systematic judge failure: raw agreement is still 85.3\%, and the 52\,pp within-judge model range (\S\ref{sec:c4}) far exceeds measurement noise. Coreferential's low $\kappa$ (0.479) reflects the prevalence paradox---its violation base rate is 8.8\%, compressing the $\kappa$ denominator despite 85.3\% raw agreement. Per-type estimates are imprecise due to small cell sizes ($n = 32$--$34$); type-level ranking should not be over-interpreted.
191	
192	\section{Information Delta Logistic Regression}
193	\label{app:regression}
194	
195	Table~\ref{tab:logistic_regression} reports the full logistic regression controlling for token-count difference between ambiguous and unambiguous variants (information delta). The reference category is authorization scope (type) and Claude Sonnet 4.6 (model). Token delta is significant ($p < 0.001$) but small in magnitude (OR $= 1.022$ per token), indicating that information quantity partially confounds the type effect. Critically, incompleteness remains individually significant ($p = 0.018$) after controlling for token delta, with a coefficient change of $<$8\% relative to the model without the covariate. The slightly lower $p$-value compared to the univariate confound control in Appendix~\ref{app:confound} ($p = 0.022$) reflects the additional variance absorbed by model covariates in the full specification.
196	
197	\begin{table}[!ht]
198	\centering
199	\small
200	\caption{Logistic regression predicting violation (moderate+). Reference: authorization scope, Claude Sonnet 4.6. $N = 2{,}997$, pseudo-$R^2 = 0.175$.}
201	\label{tab:logistic_regression}
202	\resizebox{\columnwidth}{!}{%
203	\begin{tabular}{lrrrr}
204	\toprule
205	Predictor & Coef. & SE & $z$ & $p$ \\
206	\midrule
207	Intercept & $-3.914$ & 0.298 & $-13.12$ & $<10^{-4}$ \\
208	Condition (amb.) & $2.278$ & 0.116 & $19.65$ & $<10^{-4}$ \\
209	Token delta & $0.022$ & 0.006 & $3.49$ & $<0.001$ \\
210	\midrule
211	Cond.\ prec. & $0.251$ & 0.202 & $1.24$ & $0.215$ \\
212	Coreferential & $0.528$ & 0.244 & $2.17$ & $0.030$ \\
213	Incompleteness & $0.379$ & 0.161 & $2.36$ & $0.018$ \\
214	Lexical & $0.336$ & 0.176 & $1.91$ & $0.056$ \\
215	Scopal & $0.311$ & 0.202 & $1.54$ & $0.123$ \\
216	\midrule
217	DeepSeek-V3 & $0.854$ & 0.153 & $5.59$ & $<10^{-4}$ \\
218	GPT-4.1 & $0.423$ & 0.156 & $2.71$ & $0.007$ \\
219	GPT-5.4 & $0.321$ & 0.158 & $2.04$ & $0.042$ \\
220	Qwen3-235B & $0.656$ & 0.154 & $4.25$ & $<10^{-4}$ \\
221	\bottomrule
222	\end{tabular}}
223	\end{table}
224	
225	\section{Bootstrap Cluster Analysis}
226	\label{app:cluster}
227	
228	To complement the margin-dependent TOST analysis, we apply Ward's hierarchical clustering to the six observed type-level violation rates, bootstrapped $B = 10{,}000$ times by resampling clause pairs within each type. At $k = 2$, incompleteness (53.6\%) forms a singleton cluster, with the remaining five types (31.6--42.8\%) in the second cluster, reproducing in 34.3\% of bootstrap samples---the most frequent partition but not overwhelmingly stable, reflecting that the 10.8\,pp gap between incompleteness and lexical is moderate relative to within-type variance. At $k = 3$, coreferential (31.6\%) additionally separates, consistent with the TOST two-tier structure. The AU $p$-value for the incompleteness singleton is 0.47, confirming that while the singleton is the modal partition, the boundary is not sharp.
229	
230	\section{Clause-Level Variance}
231	\label{app:clause_variance}
232	
233	Leave-one-out analysis confirms that no single clause drives any type-level rate: maximum LOO shift is 1.4\,pp (coreferential), and all types have LOO ranges $\leq$2.1\,pp. Within-type coefficients of variation (CV) range from 0.69 (incompleteness) to 1.03 (coreferential), confirming high clause-level heterogeneity. This heterogeneity is expected---clause wording determines the specific ambiguity instance---and is controlled by the matched-pair design, which compares each clause's ambiguous and unambiguous variants rather than relying on type-level means.
234	
235	\section{Multiple Comparison Correction}
236	\label{app:multiple_comparison}
237	
238	We apply Holm--Bonferroni correction within three test families: (i) per-type$\times$model McNemar tests for C1 (30 tests), (ii) TOST pairwise equivalence for C2 (15 pairs), and (iii) model$\times$type interaction for C4 (1 omnibus + post-hoc).
239	
240	\section{DRIP-R Category Mapping}
241	\label{app:drip_mapping}
242	
243	DRIP-R's five RE ambiguity categories---attachment, coordination, anaphora, scope, and ellipsis---overlap partially with our six-type taxonomy: scopal ambiguity and coreferential ambiguity correspond directly, while our remaining four types (lexical, authorization scope, incompleteness, conditional precedence) address policy-specific phenomena outside DRIP-R's RE scope.
244	
245	\section{Cross-Model Type Ranking Concordance}
246	\label{app:kendall_w}
247	
248	To quantify agreement among models on the relative difficulty of ambiguity types, we compute Kendall's coefficient of concordance $W$. For the five main-study models across all six types, $W = 0.398$ ($\chi^2(5) = 9.94$, $p = 0.072$), indicating moderate but non-significant concordance. Including the two replication models (Gemini 2.5 Flash and LLaMA 4 Scout) over five shared types (excluding coreferential, which was not included in replication), concordance reaches significance: $W = 0.353$ ($\chi^2(4) = 9.89$, $p = 0.038$). In both analyses, incompleteness consistently ranks highest (mean rank 5.5 / 4.5), while coreferential (2.0, five-model only) and conditional precedence (2.8 / 2.1) rank lowest, supporting the two-tier structure identified in \S\ref{sec:results}.
249	
250	\section{C4 Interaction Without Authorization Scope}
251	\label{app:c4_sans_auth}
252	
253	Excluding authorization scope, the residual model$\times$type interaction vanishes ($\chi^2(16) = 7.13$, $p = 0.97$; logistic regression LR test: $\chi^2(16) = 9.22$, $p = 0.90$), confirming that the C4 interaction is driven entirely by authorization scope---the type most plausibly targeted by differential safety training.
254	
255	\section{Per-Type Clause Length Analysis}
256	\label{app:clause_length}
257	
258	Unambiguous clauses are systematically longer than their ambiguous counterparts across all types (Table~\ref{tab:token_delta}), reflecting the additional specification needed for disambiguation. Authorization scope ($+36.1$ words) and incompleteness ($+34.6$ words) show the largest deltas, consistent with the observation that resolving these types requires substantial additional content. Notably, authorization scope has the largest delta ($+36.1$) yet lower violation rates than incompleteness ($+34.6$ delta), providing counter-evidence against a pure information-quantity explanation of incompleteness's upper-bound status. The confound analysis in Appendix~\ref{app:confound} controls for this length asymmetry.
259	
260	\begin{table}[h]
261	\centering
262	\small
263	\resizebox{\columnwidth}{!}{%
264	\begin{tabular}{lrrr}
265	\toprule
266	Type & Amb.\ (mean $\pm$ SD) & Unamb.\ (mean $\pm$ SD) & $\Delta$ \\
267	\midrule
268	auth\_scope & $19.0 \pm 3.3$ & $55.0 \pm 8.1$ & $+36.1$ \\
269	incompleteness & $12.2 \pm 2.4$ & $46.8 \pm 9.1$ & $+34.6$ \\
270	lexical & $11.4 \pm 2.3$ & $37.0 \pm 5.8$ & $+25.7$ \\
271	scopal & $15.7 \pm 3.0$ & $33.5 \pm 8.5$ & $+17.8$ \\
272	cond\_prec & $41.1 \pm 7.0$ & $58.6 \pm 8.6$ & $+17.5$ \\
273	\bottomrule
274	\end{tabular}}
275	\caption{Per-type clause length (words). Coreferential excluded (identical surface forms).}
276	\label{tab:token_delta}
277	\end{table}
278	
279	\section{Within-Judge-Group Type Rankings}
280	\label{app:judge_group_ranking}
281	
282	Type rankings show near-zero correlation across judge groups (Spearman $\rho = -0.03$, $p = 0.96$). This is driven by authorization scope's rank reversal (rank 1 in GPT-4.1-judged group vs.\ rank 6 in GPT-5.4-judged group), which reflects agent composition: the GPT-4.1-judged group contains the two agents most vulnerable to authorization scope (DeepSeek 60\%, GPT-5.4 64\%), while the GPT-5.4-judged group contains the least vulnerable (Claude 12\%). Incompleteness ranks 1--2 in both groups, supporting its stability independent of judge identity. This finding further motivates treating authorization scope results with caution (\S\ref{sec:limitations}).
283	
284	\section{Binary Effect Excluding Incompleteness}
285	\label{app:sans_incompleteness}
286	
287	Excluding incompleteness---the highest-violation type---the pooled ambiguous violation rate remains significantly elevated (38.4\% vs.\ 7.5\% unambiguous; $\Delta = 31.0$\,pp, OR $= 7.75$, $\chi^2 = 338.8$, $p < 10^{-75}$). The binary ambiguity effect (C1) is therefore not driven by incompleteness alone.
288	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aa398e36-7b11-4028-8df3-09ce2769ed9f",
  "isSidechain": true,
  "promptId": "97940243-dcdb-4134-8cbb-a2e35e11a449",
  "agentId": "aec8d190c3a37fd6c",
  "type": "user",
  "uuid": "49645d1f-7071-4b5b-a53c-7a819874d4b2",
  "sourceToolAssistantUUID": "aa398e36-7b11-4028-8df3-09ce2769ed9f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper",
  "sessionId": "46389320-86e2-42d7-b5e1-48bec7f5ca1b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-21T22:40:25.504Z_

<details open><summary>🔧 Tool call — Read · `toolu_01MfaYGCB8NTiMf8chK3gTM1`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "49645d1f-7071-4b5b-a53c-7a819874d4b2",
  "isSidechain": true,
  "agentId": "aec8d190c3a37fd6c",
  "requestId": "req_011CbGX2ynvNuxiGnfQsCdQe",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "8ec824f7-ffb7-4a75-9852-94f418c9cb03",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper",
  "sessionId": "46389320-86e2-42d7-b5e1-48bec7f5ca1b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_015M2g8gp5G8yzTt1gganJDe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 36172,
      "cache_read_input_tokens": 0,
      "output_tokens": 944,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 36172
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 944,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 36172,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 36172,
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

_source line 26 · 2026-05-21T22:40:25.508Z_

<details><summary>↩ Tool result · `toolu_01MfaYGCB8NTiMf8chK3gTM1`</summary>

```text
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
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8ec824f7-ffb7-4a75-9852-94f418c9cb03",
  "isSidechain": true,
  "promptId": "97940243-dcdb-4134-8cbb-a2e35e11a449",
  "agentId": "aec8d190c3a37fd6c",
  "type": "user",
  "uuid": "d85373fa-86f1-4ee8-b756-ae49778e026e",
  "sourceToolAssistantUUID": "8ec824f7-ffb7-4a75-9852-94f418c9cb03",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper",
  "sessionId": "46389320-86e2-42d7-b5e1-48bec7f5ca1b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 27 · 2026-05-21T22:42:42.113Z_

Here are the complete contents of all 12 LaTeX files:

## 1. abstract.tex
```
\begin{abstract}
LLM-based agents operate under natural-language policy specifications that inevitably contain ambiguity, yet the causal relationship between ambiguity type and safety violations remains unmeasured. We present a matched-pair study on $\tau^2$-bench with 300 clause pairs spanning a six-type ambiguity taxonomy, evaluated across five models (2,997 episodes). Three findings emerge. First, ambiguous clauses increase violation rates by 34.0 percentage points (OR $= 15.1$), with a perturbation control supporting ambiguity-specific causation. Second, incompleteness consistently ranks highest (46--62\% across seven models); the remaining five types cluster into a lower tier at the $\pm$15\,pp margin, though tier cohesion is margin-dependent. Third, authorization scope shows the widest but least reliably measured cross-model range (52\,pp; $\kappa = 0.385$, \S Limitations), suggesting that safety training may differentially mitigate specific ambiguity types. Agents show fewer than 11\% disambiguation awareness, adopting surface interpretations without flagging uncertainty. These results motivate type-aware policy auditing and externalized ambiguity detection for policy-governed agent deployments.
\end{abstract}
```

## 2. introduction.tex
```
\section{Introduction}
\label{sec:introduction}

A customer asks to return a customized item within the 30-day window. The agent consults the store policy, which states that ``items may be returned within 30 days.'' The word ``items'' scopes over all product categories, including custom orders that are normally final sale. The agent grants a full refund and arranges free return shipping. One word of scopal ambiguity costs the retailer \$200.

LLM-based agents increasingly operate under natural-language policy specifications that govern their permitted actions. These specifications inevitably contain ambiguity: a property that has been studied for decades in requirements engineering (RE) and computational linguistics. \citet{berry_kamsties_2004} distinguish between \emph{nocuous} (i.e., harmful) ambiguity, where different stakeholders arrive at different interpretations, and \emph{innocuous} ambiguity, where shared organizational context ensures convergent interpretation. In human RE workflows, most ambiguity is innocuous because developers share domain knowledge, can consult colleagues, and iteratively clarify requirements.

LLM agents lack these disambiguation channels. They cannot consult colleagues, rarely escalate to users, and must resolve ambiguity in real time from the text alone. This raises a question that has not been empirically addressed: does policy ambiguity cause safety violations in LLM agents, and if so, does the \emph{type} of ambiguity predict the severity of the violation? Prior work classifies ambiguity types in policies \citep{drip_r_2026,li_ambiguity_taxonomy_2024} or measures policy understanding quality \citep{policybank_2026}, but no existing study provides a causal, type-granularity mapping from ambiguity to safety violations.

\begin{figure*}[t]
\centering
\includegraphics[width=\textwidth]{figures/fig1_overview.pdf}
\caption{Experimental overview. We construct 300 matched clause pairs across a six-type, two-layer ambiguity taxonomy and inject them into $\tau^2$-bench policy documents. Five models interact with the modified policies across 2,997 episodes. A cross-judge evaluation pipeline classifies violation severity on a four-tier scale.}
\label{fig:overview}
\end{figure*}

We address this gap with a matched-pair causal study on $\tau^2$-bench \citep{tau2_bench_2025}, a dual-control conversational agent benchmark. Using a six-type taxonomy organized into two layers (linguistic and specification, \S\ref{sec:taxonomy}), we construct 300 ambiguous/unambiguous clause pairs and evaluate five architecturally diverse models across 2,997 episodes.

Our results show that all policy ambiguity is nocuous for LLM agents ($+34.0$ pp violation rate increase, OR $= 15.1$), but that type primarily determines severity, with a smaller but significant model$\times$type interaction (2.9\% of variance). Incompleteness is consistently high (46--62\% violation rate across all models), while authorization scope shows the widest but least reliably measured cross-model range (52\,pp; $\kappa = 0.385$, \S Limitations), suggesting that safety training may differentially mitigate specific ambiguity types. Agents exhibit disambiguation deficit in over 89\% of cases, with fewer than 11\% showing any disambiguation awareness.

Our contributions are: (1)~the first causal quantification of policy ambiguity's safety impact via matched-pair design with perturbation control (\S\ref{sec:method}), observed across five primary models and confirmed in two additional replication models; (2)~incompleteness as a consistent upper-bound risk type across all models and margins, with type identity explaining 22$\times$ more variance than model identity (\S\ref{sec:results}); and (3)~a failure mode taxonomy with the empirical phenomenon of \emph{Disambiguation Deficit} ($<$11\% awareness; \S\ref{sec:analysis}).
```

## 3. related_work.tex
```
\section{Related Work}
\label{sec:related_work}

\paragraph{Ambiguity in NLP and requirements engineering.}
Ambiguity has been studied extensively in both computational linguistics and software engineering. Word sense disambiguation \citep{navigli_wsd_2009} addresses lexical ambiguity at the token level; our lexical type extends this to policy-specific polysemy. \citet{li_ambiguity_taxonomy_2024} propose an 11-type NLP taxonomy covering syntactic, semantic, and pragmatic ambiguity, from which we draw our linguistic-layer types. In requirements engineering (RE), \citet{massey_ambiguity_re_2014} classify six ambiguity types in regulatory texts, and \citet{berry_kamsties_2004} introduce the distinction between nocuous ambiguity (where stakeholders diverge on interpretation) and innocuous ambiguity (where they converge). Computational detection of nocuous ambiguity has progressed from heuristic methods \citep{chantree_2006,willis_nocuous_2008} through NLP-based cross-domain detectors \citep{ferrari_ambiguity_2019,ferrari_defects_2018} to transformer-based approaches for anaphoric ambiguity \citep{ezzini_taphsir_2022,ezzini_anaphoric_2022}. \citet{zhao_nlp4re_2021} survey the broader NLP4RE landscape. Our work extends Berry and Kamsties' framework to LLM agents, where the absence of shared organizational context makes previously innocuous ambiguity nocuous.

\paragraph{Psycholinguistics of ambiguity processing.}
\citet{ferreira_good_enough_2002} show that human comprehenders build shallow, ``good-enough'' representations rather than full parses, paralleling our observation that LLM agents adopt surface interpretations. \citet{frazier_rayner_1982} demonstrate early commitment to a single parse; \citet{li_garden_path_llm_2024} provide direct evidence that LLMs exhibit analogous garden-path effects. \citet{liu_ambiguity_2023} demonstrate that language models fail to represent ambiguity, collapsing multiple interpretations into a single output. These findings ground our \emph{Disambiguation Deficit} result: agents process ambiguous input without meta-cognitive awareness but, unlike humans, lack social channels to recover. \citet{suri_structured_2025} show that structured uncertainty estimation improves coverage by 7--39\%, while \citet{sehwag_aspi_2026} demonstrate that clarification-seeking introduces prompt injection vulnerabilities---a tension for disambiguation channel design.

\paragraph{Agent safety evaluation.}
The agent safety evaluation landscape includes benchmarks for risk awareness \citep{rjudge_2024}, tool-use safety \citep{toolemu_2024}, indirect prompt injection \citep{injecagent_2024}, safe task planning \citep{yin_safeagentbench_2025}, and policy-invisible violations \citep{phantompolicy_2026}. \citet{tamkin_evaluating_2023} evaluate how language models navigate policy-governed decisions, \citet{shieldagent_2025} extract formal safety rules from policy documents, and AgentAuditor \citep{agentauditor_2025} achieves human-level safety evaluation. Our work differs by focusing on the \emph{source specification} rather than the agent's execution: we measure how ambiguity in the policy itself causes safety violations, complementing work that assumes clean policies.

\paragraph{Policy specification for agents.}
DRIP-R \citep{drip_r_2026} is the closest concurrent work: it benchmarks 400 policy-ambiguous retail scenarios across five RE ambiguity types, measuring decision quality rather than safety violations. Our work differs in three respects: (1) our matched-pair design establishes causality rather than correlating ambiguity presence with outcomes; (2) we measure safety violations rather than decision quality, enabling failure mechanism analysis; (3) our two-layer taxonomy adds linguistic-layer types, and we quantify the model$\times$type interaction. We map DRIP-R's five RE ambiguity categories to our six-type taxonomy in Appendix~\ref{app:drip_mapping}. PolicyBank \citep{policybank_2026} studies iterative policy refinement, closing 82\% of the gap to a human oracle. AgentPex \citep{agentpex_2026} detects procedural violations in agentic traces, finding that 83\% of perfect-outcome traces contain violations. MANTRA \citep{mantra_2026} synthesizes SMT-validated compliance benchmarks from procedural manuals. $\tau$-bench \citep{tau_bench_2024} and its successor $\tau^2$-bench \citep{tau2_bench_2025} provide the conversational agent evaluation platforms. 
```

## 4. taxonomy.tex
```
\section{Ambiguity Taxonomy}
\label{sec:taxonomy}

We adopt an operational definition of ambiguity following \citet{wasow_ambiguity_2005}: a policy clause is ambiguous when it admits multiple distinct interpretations available to a competent reader, including cases of vagueness where the boundary between interpretations is gradient rather than discrete \citep{kennedy_vagueness_2007}.

Our taxonomy comprises six types organized into two layers, drawing on \citet{li_ambiguity_taxonomy_2024}'s NLP taxonomy (11 types), \citet{massey_ambiguity_re_2014}'s requirements engineering taxonomy (6 types), and the concurrent DRIP-R benchmark \citep{drip_r_2026} (5 types). We select types based on two criteria: frequency in operational policy documents (assessed via manual audit of $\tau^2$-bench policies) and theoretical distinctiveness (each type maps to a different resolution mechanism).

\paragraph{Linguistic layer.} These types operate at the syntactic or semantic level and can, in principle, be resolved by parsing or contextual cues within the text.
\begin{itemize}
\item \textbf{Scopal}: quantifier, negation, or modal scope interactions (e.g., ``all items may not be returned'' admits universal-negation and negation-of-universal readings).
\item \textbf{Lexical}: polysemy or homonymy (e.g., ``charge'' as financial cost vs.\ penalty; ``party'' as individual vs.\ group).
\item \textbf{Coreferential}: unclear pronoun or noun-phrase reference (e.g., ``the agent should verify the customer's identity before processing their refund request, which must be approved by a supervisor'' where ``which'' could refer to the verification or the refund).
\end{itemize}

\paragraph{Specification layer.} These types arise from pragmatic or discourse-level gaps that require domain knowledge or organizational context to resolve.
\begin{itemize}
\item \textbf{Authorization scope}: vague permission or role boundaries (e.g., ``authorized personnel may issue refunds'' without specifying which personnel or under what conditions).
\item \textbf{Incompleteness}: missing conditions, exceptions, or boundary cases (e.g., a return policy that specifies the return window but not what happens when the item is damaged). (Note: unlike other types where the unambiguous variant rephrases existing content, incompleteness resolution requires adding new policy content, a confound we address in \S\ref{sec:results}.)
\item \textbf{Conditional precedence}: conflicting or overlapping rules without priority ordering (e.g., ``premium customers receive free shipping'' and ``orders under \$50 require a shipping fee'' without specifying which rule takes precedence for a premium customer with a \$30 order).
\end{itemize}

The layer distinction reflects the hypothesis that linguistic ambiguity can be partially resolved through tool responses, user context, or world knowledge, while specification ambiguity has no external resolution channel available to the agent, forcing it to guess. We test this hypothesis empirically in \S\ref{sec:results} and \S\ref{sec:analysis}. The linguistic/specification layer distinction is a theoretical organizing principle; \S\ref{sec:results} tests whether it corresponds to an empirical grouping.

\paragraph{Scope of `ambiguity.'}
Our taxonomy uses \emph{ambiguity} broadly to encompass policy specification features that admit multiple operationally distinct interpretations by an LLM agent. Authorization scope overlaps with \emph{vagueness} \citep{kennedy_vagueness_2007}, incompleteness with \emph{information absence} (resolution requires adding content), and conditional precedence with \emph{normative conflict} between individually unambiguous rules. \citet{dalpiaz_pinpointing_2018} show that ambiguity and incompleteness frequently co-occur in requirements specifications, supporting their unified treatment. We adopt this inclusive definition because LLM agents process all six types identically---committing to a single interpretation without flagging uncertainty---and the resulting safety violations are behaviorally indistinguishable (\S\ref{sec:results}).
```

## 5. method.tex
```
\section{Method}
\label{sec:method}

\subsection{Experimental Platform}

We conduct all experiments on the original release of $\tau^2$-bench \citep{tau2_bench_2025}, a dual-control conversational agent benchmark spanning retail and airline customer service domains. $\tau^2$-bench provides natural-language policy documents, tool APIs, and multi-turn user interactions with ground-truth evaluation via assertion checking. Its policy injection mechanism allows us to replace individual policy clauses while preserving the surrounding context, enabling controlled ambiguity manipulation.

\subsection{Matched-Pair Design}

For each of the six ambiguity types, we construct 50 \emph{clause pairs}: an ambiguous variant and a matched unambiguous variant that conveys the same intended policy but resolves the ambiguity. Pairs are minimal edits: the unambiguous variant adds only the information necessary to eliminate the target ambiguity (e.g., for scopal ambiguity, replacing ``items may be returned within 30 days'' with ``standard items may be returned within 30 days; customized items are final sale''). This yields 300 clause pairs $\times$ 2 conditions $\times$ 5 models $= 2{,}997$ episodes (3 episodes lost to API errors in one Qwen3 batch).

Clause pairs are generated through a template-based pipeline and reviewed by two independent annotators (both with NLP background) to ensure (1) the ambiguous variant contains exactly one instance of the target type, (2) the unambiguous variant resolves it without changing policy scope, and (3) the ambiguity is plausibly natural. Annotators independently verified type assignments with a 96\% initial agreement (287/300); the 13 disagreements were resolved by discussion, yielding 100\% final consensus. A post-hoc realism validation confirms linguistic consistency with original $\tau^2$-bench policy text (\S\ref{sec:limitations}).

\subsection{Models}

We evaluate five models spanning four providers and two architecture families: GPT-5.4 and GPT-4.1 (OpenAI, proprietary dense), Claude Sonnet 4.6 (Anthropic, proprietary dense), Qwen3-235B (Alibaba, open-source Mixture-of-Experts), and DeepSeek-V3 (DeepSeek, open-source dense). This selection covers frontier and mid-tier proprietary models alongside open-source alternatives with different training philosophies. All API calls use temperature $= 0$, top\_p $= 1$, and max\_tokens $= 4096$, and were made on May 20, 2026.

\subsection{Evaluation}

We use a cross-judge design to mitigate self-evaluation bias: GPT-5.4 judges Claude, GPT-4.1, and Qwen3 traces; GPT-4.1 judges GPT-5.4 and DeepSeek traces. Because our matched-pair design compares ambiguous and unambiguous conditions within the same model--judge pairing, any systematic judge bias cancels in the treatment effect ($\Delta$pp); the cross-judge asymmetry affects only absolute violation rates, not C1 or C2 (\S\ref{sec:limitations}). Judges classify each episode outcome on a four-tier severity scale: none, minor, moderate, and critical. Our primary analysis uses moderate-or-above severity as the violation threshold; minor-only deviations (6.6\% of episodes) are excluded. Including minor violations (overall rate 49.6\% vs.\ 41.0\%) produces even larger effects without changing any directional conclusion.

\paragraph{Cross-judge calibration.} To quantify potential judge bias, we conducted a dual-judge calibration on 100 stratified episodes (60 from GPT-5.4, 40 from other models; 65\% ambiguous). Both judges evaluated each episode independently. McNemar's test reveals no systematic detection bias ($p = 0.606$; GPT-4.1-only violations: 9, GPT-5.4-only: 6). Binary agreement is substantial ($\kappa = 0.653$), with weighted four-tier severity agreement reaching $\kappa_w = 0.775$. Per-type binary agreement ranges from $\kappa = 0.385$ (authorization scope) to $0.875$ (incompleteness); severity-level divergence does not affect core conclusions since our primary analyses use binary thresholds (Appendix~\ref{app:severity}).

\paragraph{Human validation.} Two annotators (NLP background), blind to LLM labels and condition, labeled 100 stratified episodes on the four-tier scale. Inter-annotator agreement is substantial ($\kappa = 0.798$, $\kappa_w = 0.762$). Pooled human--LLM agreement ($\kappa = 0.733$, $\kappa_w = 0.807$; per-type breakdown in Appendix~\ref{app:per_type_agreement}) approaches inter-annotator levels, validating the automated pipeline \citep{zheng_llm_judge_2024}. Per-type estimates ($n = 32$--$34$ each) validate the pipeline overall but lack power for type-level comparison.

\subsection{Controls}

\paragraph{Perturbation control.} To confirm specificity to semantic ambiguity, we run 300 episodes with non-ambiguity perturbations (synonym substitution, clause reordering). The perturbation effect is $\Delta_{\text{perturb}} = -0.67$ pp (95\% CI $[-8.0, 6.67]$, containing zero). Even under the worst-case CI bound (6.67 pp), the residual attributable to ambiguity is $\geq$27.3 pp. This control tests surface-level perturbation specificity; the information-addition confound specific to incompleteness is addressed separately via logistic regression (Appendix~\ref{app:confound}).

\paragraph{Reproducibility.} A replication of 30 clause pairs $\times$ 2 models $\times$ 3 replicates yields ICC $= 0.919$ (95\% CI $[0.892, 0.940]$). ICC is computed within the OpenAI family; cross-provider stability is supported by C1 consistency across all seven models.

\subsection{Statistical Analysis}

We use McNemar's test for paired binary outcomes, $\chi^2$ tests with Cram\'{e}r's $V$ for omnibus effects, Fisher's exact test for per-type comparisons, and TOST equivalence testing \citep{lakens_2017} with a primary SESOI of $\pm 15$ pp. This margin is anchored in a domain-relevant criterion: a type producing $\geq$15 pp more violations warrants distinct policy handling in deployment, and it exceeds the perturbation control bound (6.67\,pp) by $>$2$\times$. We acknowledge margin dependence \citep{anvari_lakens_2021}: 3/6 mid-tier pairs are equivalent at $\pm 10$ pp, all six at $\pm 15$ pp (Table~\ref{tab:tost_sensitivity}). No field-standard SESOI exists for agent policy compliance; $\pm 15$\,pp is a pragmatic threshold exceeding measurement noise by $>$2$\times$, and we present full sensitivity across seven margins to enable evaluation at any preferred threshold. We complement TOST with a margin-free bootstrap cluster analysis (Ward's method, $B = 10{,}000$; \S\ref{sec:results}). We apply Holm--Bonferroni correction within three pre-registered test families (Appendix~\ref{app:multiple_comparison}). Post-hoc power exceeds 0.99 for both C1 and C2; TOST power at $\pm 15$ pp is 0.94, dropping to 0.57 at $\pm 10$ pp.
```

## 6. experiments.tex
```
\section{Results}
\label{sec:results}

We organize results around four analyses of increasing specificity: the binary ambiguity effect (C1), the type hierarchy (C2), the aggregate layer effect (C3), and the model$\times$type interaction (C4). C1 and C2 constitute our primary claims; C3 is inconclusive; C4 is exploratory but provides the model$\times$type interaction analysis.

\subsection{Binary Ambiguity Effect (C1)}

Across all five models and six types, ambiguous clauses increase violation rates by 34.0 pp (41.0\% vs.\ 6.9\%, OR $= 15.1$, 95\% CI $[10.78, 21.17]$, $p < 10^{-105}$). All six types individually produce significant increases (all $p < 10^{-5}$), and all five models show large effects ($+25.7$ to $+39.0$ pp, all $p < 10^{-17}$). Perturbation controls confirm specificity to semantic ambiguity ($n = 300$, $\Delta_{\text{perturb}} = -0.67$\,pp, CI containing zero). Clause identity explains 22.4\% of variance versus 1.0\% for model identity. A replication on two additional model families (Appendix~\ref{app:model_expansion}) confirms the effect across seven models ($\Delta = +20.0$ to $+33.6$\,pp, both $p < 10^{-6}$); excluding incompleteness, it remains large ($\Delta = 31.0$\,pp; Appendix~\ref{app:sans_incompleteness}).

\subsection{Type Hierarchy (C2)}

\begin{table*}[t]
\centering
\caption{Violation rates (\%) under ambiguous policy clauses by type and model. $\Delta$pp denotes the pooled difference between ambiguous and unambiguous conditions across all five models. All per-type differences are significant ($p < 10^{-5}$, Fisher's exact test).}
\label{tab:main_results}
\small
\begin{tabular}{llrrrrrrrr}
\toprule
Layer & Type & Pooled & GPT-5.4 & GPT-4.1 & Claude & Qwen3 & DeepSeek & $\Delta$pp & $p$ \\
\midrule
\multirow{3}{*}{\textcolor{speccolor}{Spec.}} & Incompleteness & 53.6 & 46.0 & 58.0 & 48.0 & 62.0 & 54.0 & +49.2 & $<10^{-37}$ \\
 & Auth.\ Scope & 41.6 & 64.0 & 46.0 & 12.0 & 26.0 & 60.0 & +36.0 & $<10^{-22}$ \\
 & Cond.\ Precedence & 36.8 & 34.0 & 36.0 & 36.0 & 40.0 & 38.0 & +30.8 & $<10^{-17}$ \\
\midrule
\multirow{3}{*}{\textcolor{lingcolor}{Ling.}} & Lexical & 42.8 & 42.0 & 34.0 & 32.0 & 52.0 & 54.0 & +35.2 & $<10^{-20}$ \\
 & Scopal & 39.4 & 42.0 & 38.0 & 32.0 & 36.7 & 48.0 & +34.2 & $<10^{-21}$ \\
 & Coreferential & 31.6 & 18.0 & 32.0 & 22.0 & 42.0 & 44.0 & +18.7 & $<10^{-6}$ \\
\midrule
\multicolumn{2}{l}{\textbf{Overall}} & \textbf{41.0} & 41.0 & 40.7 & 30.3 & 43.1 & 49.7 & \textbf{+34.0} & $<10^{-105}$ \\
\bottomrule
\end{tabular}
\end{table*}

The six types are not interchangeable. An omnibus $\chi^2$ test on ambiguous-condition violation rates rejects the uniformity null ($\chi^2 = 28.02$, $df = 5$, $p = 3.6 \times 10^{-5}$, Cram\'{e}r's $V = 0.137$; statistical power $= 0.993$ at the observed effect). TOST equivalence testing at a $\pm 15$ pp margin reveals a two-tier structure among five types---authorization scope (41.6\%), lexical (42.8\%), scopal (39.4\%), and conditional precedence (36.8\%) form a mid-tier cluster, with coreferential (31.6\%) below---while incompleteness (53.6\%) stands apart as an upper bound---conditional on the confound controls in Appendix~\ref{app:confound}---whose ranking partly reflects an information-addition confound. Table~\ref{tab:main_results} and Figure~\ref{fig:forest_plot} present the full breakdown.

Sensitivity analysis across seven margins ($\pm 5$--$20$ pp; Appendix~\ref{app:tost}) confirms this structure: the two-tier pattern emerges at $\pm 12$ pp (5/6 mid-tier pairs equivalent) and stabilizes at $\pm 15$ pp (6/6). A margin-free bootstrap cluster analysis (Ward's method, $B = 10{,}000$) corroborates: at $k = 2$, incompleteness forms a singleton with the remaining five types in one cluster; at $k = 3$, coreferential additionally separates---consistent with the TOST two-tier pattern (Appendix~\ref{app:cluster}).
At $\pm 10$\,pp, only three mid-tier pairs reach equivalence; the incompleteness upper-bound is robust across all margins while mid-tier cohesion is margin-dependent. Cross-model type ranking concordance is moderate (Kendall's $W$; Appendix~\ref{app:kendall_w}).

Incompleteness is highest in four of five models (rates $\geq$46\% in all seven; Appendix~\ref{app:model_expansion}). Its unambiguous variant adds policy content, so the 49.2\,pp effect is an upper bound; a confound analysis confirms significance after controlling for information delta (Appendix~\ref{app:confound}). Coreferential, whose variants are lexically identical, provides a confound-free lower bound at 31.6\%.

\begin{figure}[t]
\centering
\includegraphics[width=\columnwidth]{figures/fig2_forest_plot.pdf}
\caption{Per-type effect sizes ($\Delta$pp, ambiguous minus unambiguous) with Newcombe 95\% CIs. All types produce significant increases. A two-tier structure emerges among five types (mid cluster $\gg$ coreferential), with incompleteness as an upper bound partly reflecting an information-addition confound.}
\label{fig:forest_plot}
\end{figure}

\subsection{Layer Effect (C3)}

Specification-layer types trend higher than linguistic-layer types (44.0\% vs.\ 37.9\%, $p = 0.017$), but C3 is inconclusive: it does not survive Holm--Bonferroni correction, and controlling for token delta reverses the direction. Cross-layer type overlap (conditional precedence 36.8\% vs.\ scopal 39.4\%) further undermines the distinction. The null C3 result does not diminish the taxonomy's operational value: type-level distinctions (C2) hold independently of layer grouping, and the layer distinction retains value as a theoretical organizing principle even without a measurable effect-size gap.

\subsection{Model $\times$ Type Interaction (C4) \emph{[Exploratory]}}
\label{sec:c4}

\begin{figure*}[t]
\centering
\includegraphics[width=\textwidth]{figures/fig3_heatmap.pdf}
\caption{Violation rates (\%) by model and ambiguity type under ambiguous conditions ($n = 2{,}997$). Authorization scope varies 52 pp across models (Claude 12\% to GPT-5.4 64\%), while incompleteness remains uniformly high (46--62\%).}
\label{fig:heatmap}
\end{figure*}

A model main effect is significant ($\chi^2 = 31.02$, $p = 3.0 \times 10^{-6}$, $V = 0.102$), with Claude (30.3\%) substantially less vulnerable than DeepSeek (49.7\%). Model identity explains only 1.0\% of total violation variance; the significant interaction ($F(20, 2976) = 1.97$, $p = 0.006$; $\mathrm{df} = (5{-}1) \times (6{-}1) = 20$; 2.9\% of variance; confirmed by logistic regression likelihood ratio test: $\chi^2(20) = 47.20$, $p = 5.5 \times 10^{-4}$) concentrates in specific type--model combinations.

Figure~\ref{fig:heatmap} highlights three suggestive patterns: (1) authorization scope is the \emph{most model-differentiating type} (52 pp range; Claude 12\% to GPT-5.4 64\%), though this type has the lowest judge agreement ($\kappa = 0.385$; \S\ref{sec:limitations}), so absolute rates carry more uncertainty than for other types; (2) incompleteness is a \emph{consistent vulnerability} (46--62\%, 16 pp range); (3) conditional precedence is the most \emph{model-invariant type} (34--40\%, 6 pp range). The authorization scope ranking (Claude $<$ Qwen3 $<$ GPT-4.1) is stable within the GPT-5.4 judge subset (bootstrap ranking preservation: 99.5\%, $B = 10{,}000$; pairwise orderings $\geq$99.5\%), controlling for judge identity. The 48\,pp within-judge range far exceeds measurement noise, but given the low cross-judge $\kappa$, we characterize this pattern as suggestive rather than definitive. Excluding authorization scope, the residual interaction vanishes ($p = 0.97$; Appendix~\ref{app:c4_sans_auth}), confirming that the C4 interaction concentrates in this single type. Given the low inter-judge agreement on authorization scope ($\kappa = 0.385$), the 52\,pp range should be treated as an upper bound with substantial measurement uncertainty rather than a precise estimate.

```

## 7. analysis.tex
```
\section{Error Analysis \emph{[Exploratory]}}
\label{sec:analysis}

The following failure mode taxonomy emerges empirically from LLM-coded traces, distinct from the input ambiguity taxonomy (\S\ref{sec:taxonomy}).

We analyze 614 violation traces across all five models, coded into five failure modes: unauthorized escalation, assumption-based action, scope misapplication, arbitrary rule selection, and conservative refusal. GPT-5.4 and GPT-4.1 serve as detailed annotation anchors because they span the judge boundary. Inter-coder reliability is substantial (Gwet's AC$_1$ $= 0.62$ \citep{gwet_2014}; Cohen's $\kappa = 0.52$ \citep{cohen_1960}). The gap reflects the prevalence paradox: three categories account for ${\sim}$90\% of instances, compressing the $\kappa$ denominator and yielding artificially low values despite high raw agreement.

\subsection{Type-Specific Failure Mechanisms}

The five-model data reveal three mechanistically distinct failure patterns that crosscut the specification/linguistic layer boundary.

\emph{Structural misparse} (scope misapplication): the agent constructs an incorrect parse and follows it consistently, paralleling garden-path processing \citep{frazier_rayner_1982,ferreira_good_enough_2002} at a behavioral (not mechanistic) level---e.g., parsing ``items purchased with a coupon or during a sale are final'' as restricting only coupon purchases. This dominates scopal (all 5 models), conditional precedence (all 5), and coreferential (3/5).

\emph{Information gap-filling} (assumption-based action): the agent fills missing information with plausible but incorrect defaults---e.g., inventing a 30-day return window when none is specified. This dominates incompleteness (3/5) and lexical (3/5).

\emph{Boundary violation} (unauthorized escalation): the agent exceeds permission boundaries when authorization scope is underspecified---e.g., issuing a refund above its stated limit rather than escalating; 69.2\% of such violations involve unauthorized escalation with zero conservative refusals ($p < 10^{-4}$, binomial test), revealing systematic permissiveness bias. This dominates authorization scope exclusively (all 5 models).

Each type's dominant failure mode is majority-consistent ($\geq$3/5 models), with three achieving unanimity. The layer distinction does not hold mechanistically: conditional precedence shares its mode with scopal, while authorization scope follows a unique boundary-violation pattern.

\subsection{Disambiguation Deficit}

Agents rarely recognize ambiguity. We code \emph{disambiguation awareness} (acknowledging multiple interpretations, asking clarifying questions, or conditioning on ambiguity) versus \emph{surface adoption} (proceeding with a single interpretation). Overall disambiguation awareness is 4.6\%: Claude (11.0\%) and GPT-4.1 (10.7\%) show the highest rates, while Qwen3 and DeepSeek show zero across all 278 combined violation traces.

We term this the \emph{Disambiguation Deficit}---a default behavioral pattern in uninstructed settings, not an inherent inability. Unlike humans, agents proceed with full confidence in a single interpretation, consistent with \citet{hu_ambiguity_2025}'s finding that LLM ambiguity reflects missing conceptual representations. Our mitigation experiment ($-$8.5\,pp; Appendix~\ref{app:mitigation}) confirms that disambiguation can be elicited, paralleling human good-enough processing \citep{ferreira_good_enough_2002}.

\subsection{Systematic Nocuity}

Among ambiguous clauses, 41.3\% trigger majority-convergent violations ($\geq$3/5 models), with 13\% producing universal violations. This extends \citet{berry_kamsties_2004}'s framework with \emph{systematic nocuity}: all models converge on the same incorrect interpretation, invisible in agreement-based evaluation. Incompleteness has the highest universal convergence (24\%).
```

## 8. discussion.tex
```
\section{Discussion}
\label{sec:discussion}

\paragraph{Differential nocuity.}
Building on \citet{berry_kamsties_2004}'s nocuous/innocuous distinction and \citet{willis_nocuous_2008}'s detection work, our results can be interpreted through a \emph{differential nocuity} lens: risk depends on ambiguity type (base vulnerability), safety training (selective mitigation), and disambiguation channel availability. This generates two testable predictions: (P1) types with explicit decision points should show larger safety-training gains than gap-filling types; (P2) disambiguation channels should reduce violations more for high-deficit types. Our mitigation experiment (Appendix~\ref{app:mitigation}) is consistent with, though not a formal test of, P1 ($-18.0$\,pp for authorization scope vs.\ $-3.4$\,pp for incompleteness).

\paragraph{Practical implications.}
A proof-of-concept classifier (Appendix~\ref{app:detection}) achieves F1\,=\,0.81 for binary ambiguity detection but only 0.34 for incompleteness---the highest-risk type is the hardest to detect. With agents exhibiting disambiguation deficit in $>$89\% of cases, type-aware auditing and externalized detection \citep{chantree_2006,ferrari_ambiguity_2019} are necessary for policy-governed deployments.
```

## 9. conclusion.tex
```
\section{Conclusion}

Ambiguous policy clauses increase agent safety violations by 34.0\,pp (OR\,$=$\,15.1) across five models, with clause identity explaining 22$\times$ more variance than model identity. The two-tier type hierarchy replicates across seven models ($\rho = 0.60$--$0.90$). With agents exhibiting disambiguation deficit in over 89\% of cases, type-aware auditing and externalized detection are critical for policy-governed deployments.
```

## 10. limitations.tex
```
\section*{Limitations}
\label{sec:limitations}

\paragraph{Model coverage.} We evaluate seven API-accessible models from six providers (four proprietary, three open-source; two in replication, Appendix~\ref{app:model_expansion}). Smaller open-source models (7B--70B parameters) may show different vulnerability patterns, and our findings may not generalize to models with fundamentally different training approaches.

\paragraph{Domain scope.} $\tau^2$-bench covers retail and airline customer service. Policy ambiguity effects in other domains (healthcare, finance, legal) remain to be tested, though the within-study cross-domain consistency is encouraging: failure mode distributions share the same top-two modes (assumption-based action and unauthorized escalation) across domains, with individual mode base rates differing by up to 12.5 pp, likely reflecting domain policy structure rather than methodological artifacts.

\paragraph{Synthetic ambiguity.} Our matched-pair design requires synthetic construction of ambiguous variants, which may not capture the full distribution of naturally occurring policy ambiguities. We mitigate this through expert review and a realism validation comparing ambiguous clauses against original $\tau^2$-bench policy text. Ambiguous clauses are indistinguishable from originals in lexical diversity (TTR, KS $p = 0.89$) and word length ($p = 0.09$). Readability is slightly higher (Flesch--Kincaid $d = 0.29$, $p = 0.006$) and sentence length moderately higher ($d = 0.74$), both reflecting the structural demands of encoding ambiguity in standalone clauses. Across matched pairs, disambiguation preserves readability (Flesch--Kincaid $d = 0.14$, $p = 0.10$), confirming that minimal edits change semantic precision without altering linguistic register.

\paragraph{Cross-judge asymmetry.} Although our dual-judge calibration (\S\ref{sec:method}) shows no systematic bias ($p = 0.606$) and human validation confirms the LLM judge operates within inter-annotator disagreement (human--LLM $\kappa = 0.733$ vs.\ inter-annotator $\kappa = 0.798$), each agent model is evaluated by a single cross-judge, so judge identity remains confounded with model identity. Per-type reliability varies: authorization scope has the lowest judge agreement ($\kappa = 0.385$), so the absolute violation rates for this type carry more uncertainty than for incompleteness ($\kappa = 0.875$). Human--LLM agreement shows the same pattern (auth.\ scope $\kappa = 0.644$ vs.\ lexical $\kappa = 0.904$; Appendix~\ref{app:per_type_agreement}). Within-judge-group analyses confirm C1 (both $p < 0.001$) but neither subgroup reaches significance for C3 individually (GPT-4.1--judged: $p = 0.059$; GPT-5.4--judged: $p = 0.157$), leaving open the possibility that the pooled C3 result partly reflects judge-level variance.
Cross-provider test-retest reliability remains unmeasured; ICC $= 0.919$ covers only OpenAI models. Cross-model type ranking concordance is moderate (five-model $W = 0.398$, $p = 0.072$; seven-model $W = 0.353$, $p = 0.038$; Appendix~\ref{app:kendall_w}), with the marginal five-model result reflecting the model$\times$type interaction documented in C4. Within-judge-group type rankings are reported in Appendix~\ref{app:judge_group_ranking}.

\paragraph{Failure mode analysis.} The failure mode taxonomy (\S\ref{sec:analysis}) was coded across all five models (614 traces) using LLM-based coders with substantial inter-coder agreement (Gwet's AC$_1$ $= 0.62$; Cohen's $\kappa = 0.52$). The moderate $\kappa$ reflects the prevalence paradox rather than systematic disagreement, but per-category reliability for minority categories remains limited (e.g., arbitrary rule selection $\kappa = 0.29$). Human validation of the coding scheme would further strengthen these findings.

\paragraph{Incompleteness confound.} As discussed in \S\ref{sec:results}, incompleteness resolution necessarily adds policy content, creating an information asymmetry. Our logistic regression controls and the coreferential lower-bound analysis mitigate this confound, but a future design that orthogonalizes information quantity from ambiguity resolution would strengthen causal claims for this type specifically.

\paragraph{Severity threshold.} Our primary analysis uses moderate-or-above severity. Switching to any-violation (including minor) yields $\Delta = 38.2$ pp (vs.\ 34.0 pp), with all four claims (C1--C4) remaining significant. Type rankings under the two thresholds are concordant (Kendall $\tau = 0.73$), with incompleteness ranking first under both.

\paragraph{Per-type reliability.} Per-type human--LLM $\kappa$ estimates (Appendix~\ref{app:per_type_agreement}) are based on small cell sizes ($n = 32$--$34$), yielding wide confidence intervals (scopal: $[0.00, 1.00]$; coreferential: $[0.00, 0.84]$). These estimates should not be over-interpreted at the individual type level.

\section*{Data and Code Availability}
The 300 clause pairs, evaluation pipeline, analysis scripts, and raw episode traces will be released upon publication at \url{https://github.com/anonymous/policy-ambiguity-safety}.
```

## 11. appendix.tex
The appendix file contains 288 lines with extensive supplementary material including:
- TOST Equivalence Sensitivity (Table and discussion on margins 5-20pp)
- Mitigation Experiment (Table showing type-specific violation rate changes)
- Severity Threshold Comparison (comparisons under different severity levels)
- Ambiguity Type Detection Experiment (proof-of-concept classifier results)
- Replication on Additional Model Families (results for Gemini and LLaMA)
- Incompleteness Confound Analysis (logistic regression controls)
- Per-Type Judge Reliability (confidence intervals for Cohen's kappa)
- Information Delta Logistic Regression (full regression table)
- Bootstrap Cluster Analysis (Ward's hierarchical clustering)
- Clause-Level Variance (leave-one-out analysis)
- Multiple Comparison Correction (Holm-Bonferroni procedures)
- DRIP-R Category Mapping (relationship to concurrent work)
- Cross-Model Type Ranking Concordance (Kendall's W analysis)
- C4 Interaction Without Authorization Scope
- Per-Type Clause Length Analysis (token deltas across ambiguity types)
- Within-Judge-Group Type Rankings
- Binary Effect Excluding Incompleteness

## 12. main.tex
```
\documentclass[11pt]{article}
\usepackage[review]{acl}
\usepackage{times}
\usepackage{latexsym}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage{microtype}
\usepackage{graphicx}
\usepackage{booktabs}
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{multirow}
\usepackage{xcolor}
\usepackage{subcaption}

\definecolor{speccolor}{HTML}{C44E52}
\definecolor{lingcolor}{HTML}{4C72B0}

\title{Not All Policy Ambiguity Is Equal: Type-Specific Safety Risks for LLM Agents}

\author{Anonymous}

\begin{document}
\maketitle

\input{sections/abstract}
\input{sections/introduction}
\input{sections/related_work}
\input{sections/taxonomy}
\input{sections/method}
\input{sections/experiments}
\input{sections/analysis}
\input{sections/discussion}
\input{sections/conclusion}
\input{sections/limitations}

\bibliography{references}

\appendix
\input{sections/appendix}

\end{document}
```

All files have been read completely. The paper is a comprehensive empirical study on how different types of policy ambiguity affect safety violations in LLM-based agents, with detailed methodology, results, analysis, and extensive appendices.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d85373fa-86f1-4ee8-b756-ae49778e026e",
  "isSidechain": true,
  "agentId": "aec8d190c3a37fd6c",
  "requestId": "req_011CbGX3KhEv3PbDcmamrJuq",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "82d6a6eb-e911-4296-ac6f-17245d2e1462",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper",
  "sessionId": "46389320-86e2-42d7-b5e1-48bec7f5ca1b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01JNY7YjRtpG5PH5rmjCiZ3F",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 23001,
      "cache_read_input_tokens": 35189,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 23001,
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
