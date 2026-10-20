# Research conversation: I need to read the current paper LaTeX files for the clkc_mech_interp project. The paper is located at /home/ubuntu/.age

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 27
- **Recorded user turns:** 1
- **Tool calls:** 10
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-aaf1b6ed15acad458.jsonl`
- **Structured JSON:** [`0e7e5838831a899f668f.json`](../../sessions/0e/0e7e5838831a899f668f.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

27 recorded events

### User

_source line 1 · 2026-05-23T21:17:48.081Z_

I need to read the current paper LaTeX files for the clkc_mech_interp project. The paper is located at /home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/

Find all .tex files in that directory and read the main content — especially:
1. The abstract and introduction (look for claim wording around "general cross-lingual property" or asymmetry)
2. The experiments/results section (check if DE/German results are included in any table or text)
3. The discussion section (check for limitations and steering discussion)
4. Any tables (Table 1, 2, 3) to see what data is presented

Search breadth: medium

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "24af2116-26a8-4ad8-8f9a-3e42600cacf7",
  "agentId": "aaf1b6ed15acad458",
  "type": "user",
  "uuid": "5742884d-1518-42eb-a0bc-cb5ea6a64953",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/.claude/sessions/reviewer_509ec47e",
  "sessionId": "cade2b8d-6973-474b-bb66-65fbfa4ea818",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-23T21:17:49.562Z_

I'll search for and read the LaTeX files in the paper directory, focusing on the content you specified.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5742884d-1518-42eb-a0bc-cb5ea6a64953",
  "isSidechain": true,
  "agentId": "aaf1b6ed15acad458",
  "requestId": "req_011CbLCMiS2h84LYCBJXgH4R",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "09e27f6f-c064-4b0f-b795-79b88c6950d8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/.claude/sessions/reviewer_509ec47e",
  "sessionId": "cade2b8d-6973-474b-bb66-65fbfa4ea818",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017h1S6ehqvJ4X1zwX8XPi9z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18827,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18827,
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

_source line 3 · 2026-05-23T21:17:49.651Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01W5NxkJnDBYEMUmRWBsPKjV`</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "09e27f6f-c064-4b0f-b795-79b88c6950d8",
  "isSidechain": true,
  "agentId": "aaf1b6ed15acad458",
  "requestId": "req_011CbLCMiS2h84LYCBJXgH4R",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "775fcec4-1229-41c0-bc5a-598d2a5d2fc6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/.claude/sessions/reviewer_509ec47e",
  "sessionId": "cade2b8d-6973-474b-bb66-65fbfa4ea818",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017h1S6ehqvJ4X1zwX8XPi9z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18827,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18827,
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

_source line 4 · 2026-05-23T21:17:49.674Z_

<details><summary>↩ Tool result · `toolu_01W5NxkJnDBYEMUmRWBsPKjV`</summary>

```text
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/acl_latex.tex
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/related_work.tex
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/limitations.tex
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/method.tex
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/sections/limitations.tex
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/sections/method.tex
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/sections/experiments.tex
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/discussion.tex
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/sections/discussion.tex
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/experiments.tex
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/main.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "775fcec4-1229-41c0-bc5a-598d2a5d2fc6",
  "isSidechain": true,
  "promptId": "24af2116-26a8-4ad8-8f9a-3e42600cacf7",
  "agentId": "aaf1b6ed15acad458",
  "type": "user",
  "uuid": "0834fdcd-73d3-435b-89e4-466bf774f709",
  "sourceToolAssistantUUID": "775fcec4-1229-41c0-bc5a-598d2a5d2fc6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/.claude/sessions/reviewer_509ec47e",
  "sessionId": "cade2b8d-6973-474b-bb66-65fbfa4ea818",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 5 · 2026-05-23T21:17:51.062Z_

Now let me read the main files that are most relevant to your inquiry, starting with the abstract, introduction, experiments, and discussion sections:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0834fdcd-73d3-435b-89e4-466bf774f709",
  "isSidechain": true,
  "agentId": "aaf1b6ed15acad458",
  "requestId": "req_011CbLCMqBLDUrEPjcHSTSHd",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "e00771e1-f6e2-47bb-8a8f-1adf0336e69d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/.claude/sessions/reviewer_509ec47e",
  "sessionId": "cade2b8d-6973-474b-bb66-65fbfa4ea818",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0161pBrufis3LuQ4mTZcKqtt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1585,
      "cache_read_input_tokens": 18827,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1585,
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

_source line 6 · 2026-05-23T21:17:51.286Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Do3KSyXJJSDWyorybMon2C`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e00771e1-f6e2-47bb-8a8f-1adf0336e69d",
  "isSidechain": true,
  "agentId": "aaf1b6ed15acad458",
  "requestId": "req_011CbLCMqBLDUrEPjcHSTSHd",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "bf6394c6-f7fb-42db-bcc4-34209ff9d7a3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/.claude/sessions/reviewer_509ec47e",
  "sessionId": "cade2b8d-6973-474b-bb66-65fbfa4ea818",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0161pBrufis3LuQ4mTZcKqtt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1585,
      "cache_read_input_tokens": 18827,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1585,
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

_source line 7 · 2026-05-23T21:17:51.301Z_

<details><summary>↩ Tool result · `toolu_01Do3KSyXJJSDWyorybMon2C`</summary>

```text
1	When multilingual large language models (LLMs) encounter conflicting information across languages, the language of presentation can determine the model's answer. Behavioral studies attribute this to linguistic affinity, but the internal mechanism remains unknown: how is the conflict signal encoded, does it share structure with general cross-lingual representations, and does detectability imply causal influence on resolution?
2	
3	We probe residual stream representations in Llama-3.1-8B-Instruct, Qwen3-8B, and Gemma-2-9B-IT. Our analysis combines cross-lingual transfer, a non-conflict baseline on XNLI, confound exclusion for translation quality and token overlap, and representation steering. Conflict signals are linearly detectable across languages, and cross-lingual transfer exhibits a directional asymmetry: probes trained on Chinese transfer to English ${\sim}$7 percentage points more accurately than the reverse. This asymmetry matches the XNLI non-conflict baseline in both magnitude and direction, with overlapping confidence intervals; it inherits from the model's general multilingual structure rather than conflict-specific encoding. A dissociation emerges between detection and decision: in Llama, the probe signal peaks at late layers (88\% depth), but representation steering achieves causal influence only at a mid-layer (41\% depth); analogous Qwen and Gemma steering yields no significant effect. These findings demonstrate that linear detectability does not imply causal relevance, with direct implications for probe-based intervention research.
4	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bf6394c6-f7fb-42db-bcc4-34209ff9d7a3",
  "isSidechain": true,
  "promptId": "24af2116-26a8-4ad8-8f9a-3e42600cacf7",
  "agentId": "aaf1b6ed15acad458",
  "type": "user",
  "uuid": "43f44e88-97c6-4987-9b35-06a8ef705a3b",
  "sourceToolAssistantUUID": "bf6394c6-f7fb-42db-bcc4-34209ff9d7a3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/.claude/sessions/reviewer_509ec47e",
  "sessionId": "cade2b8d-6973-474b-bb66-65fbfa4ea818",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-23T21:17:51.489Z_

<details open><summary>🔧 Tool call — Read · `toolu_013muxyK8AeXqy6Snfyxu6y7`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "43f44e88-97c6-4987-9b35-06a8ef705a3b",
  "isSidechain": true,
  "agentId": "aaf1b6ed15acad458",
  "requestId": "req_011CbLCMqBLDUrEPjcHSTSHd",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "3df0e4e7-79d5-4909-a4e2-c57592f9ff65",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/.claude/sessions/reviewer_509ec47e",
  "sessionId": "cade2b8d-6973-474b-bb66-65fbfa4ea818",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0161pBrufis3LuQ4mTZcKqtt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1585,
      "cache_read_input_tokens": 18827,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1585,
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

_source line 9 · 2026-05-23T21:17:51.501Z_

<details><summary>↩ Tool result · `toolu_013muxyK8AeXqy6Snfyxu6y7`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	When multilingual large language models (LLMs) encounter conflicting information across languages, the language of presentation can determine which answer the model produces.
5	\citet{zhao2026when} showed that linguistic affinity dominates conflict resolution in entity-centric factual conflicts, with models preferring answers from linguistically closer sources.
6	Yet the internal mechanism behind this behavior remains opaque: how does the model encode the conflict signal?
7	Can it be detected from internal representations?
8	And if detectable, does the detected signal causally influence the model's resolution strategy?
9	These questions sit at the intersection of mechanistic interpretability and multilingual NLP, and answering them requires moving beyond behavioral observations to probe model internals directly.
10	
11	Existing work on probing knowledge conflict signals has been limited to monolingual settings.
12	\citet{zhao2024analysing} showed that residual stream representations carry linearly detectable conflict signals in English, and \citet{brink2026probing} performed knowledge attribution probing to localize factual associations within model parameters.
13	Extending these approaches cross-lingually introduces additional challenges.
14	Translation quality may confound probe transfer: a poor translation could alter conflict detection for reasons unrelated to the conflict signal itself.
15	Token overlap between languages, even when minimal, could provide a shortcut for cross-lingual probes.
16	Observed asymmetries in transfer accuracy may reflect general cross-lingual properties rather than conflict-specific phenomena, and disentangling these sources requires careful baseline comparisons.
17	Beyond detectability, a fundamental limitation of probing is that it establishes correlation, not causation \citep{hewitt2019designing}.
18	\citet{basu2026interpretability} demonstrated that even near-perfect probe accuracy does not guarantee that the detected direction can steer model behavior.
19	
20	We address these questions through a pipeline that combines residual stream probing with representation steering across three models of distinct architectures: Llama-3.1-8B-Instruct, Qwen3-8B, and Gemma-2-9B-IT.
21	Probes achieve 77.6\%, 75.0\%, and 76.2\% balanced accuracy on English within-language conflict detection, respectively, and all cross-lingual transfer directions exceed chance (binomial $p < 0.001$).
22	Cross-lingual transfer exhibits a directional asymmetry: probes trained on Chinese transfer to English approximately 7 percentage points (pp) more accurately than the reverse in all three models.
23	This asymmetry, however, is not conflict-specific.
24	XNLI entailment-versus-contradiction probes \citep{conneau2018xnli} show the same directional pattern at comparable magnitude (+6.0, +6.7, and +7.8 pp), with substantially overlapping confidence intervals.
25	The conflict asymmetry thus inherits from a general property of English-dominant models, where Chinese representations project more readily onto English representational space than the reverse.
26	Our causal analysis reveals a dissociation between detection and decision in Llama: the probe signal peaks at late layers (L28, 88\% depth), but representation steering succeeds only at a mid-layer (L13, 41\% depth; Fisher $p = 0.002$), with all late-layer interventions producing no significant behavioral change.
27	To ensure these findings are robust, we apply a confound exclusion pipeline that includes COMET-based translation quality stratification, token overlap analysis, and non-conflict baseline comparison.
28	
29	These results carry two methodological implications.
30	The layer dissociation between probing peak and causal influence demonstrates that the layer with highest probe accuracy is not necessarily where the model resolves the conflict.
31	This challenges the common practice of intervening at the probing peak layer, consistent with the warning from \citet{basu2026interpretability} that detectability and causal relevance can diverge.
32	The directional asymmetry in cross-lingual transfer reflects a structural property of English-dominant multilingual models, not a conflict-specific phenomenon.
33	Any cross-lingual probing study must account for this baseline asymmetry to correctly interpret transfer differences.
34	
35	Our contributions are as follows:
36	\begin{itemize}
37	    \item \textbf{Cross-lingual conflict detectability and asymmetry characterization.} We provide the first evidence that knowledge conflict signals are linearly detectable across languages in residual stream representations. The transfer asymmetry (ZH$\to$EN $>$ EN$\to$ZH by ${\sim}$7 pp) matches the XNLI non-conflict baseline in both magnitude and direction, establishing that it reflects the model's general cross-lingual structure rather than conflict-specific encoding.
38	    \item \textbf{Detection-decision layer dissociation.} In Llama-3.1-8B-Instruct, representation steering at the mid-layer (L13, 41\% depth) causally shifts conflict resolution (Fisher $p = 0.002$), while steering at the late-layer probing peak (L28, 88\% depth) produces no significant effect. This dissociation shows that linear detectability does not imply causal relevance, and that conflict resolution occurs upstream of where the outcome becomes linearly readable.
39	    \item \textbf{Confound exclusion pipeline for cross-lingual probing.} We design and validate a systematic pipeline of COMET translation quality ablation, token overlap analysis, and non-conflict task baseline comparison that excludes common confounds in cross-lingual probing studies.
40	\end{itemize}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3df0e4e7-79d5-4909-a4e2-c57592f9ff65",
  "isSidechain": true,
  "promptId": "24af2116-26a8-4ad8-8f9a-3e42600cacf7",
  "agentId": "aaf1b6ed15acad458",
  "type": "user",
  "uuid": "af5e6292-8b7e-41e5-9977-89f0362334c0",
  "sourceToolAssistantUUID": "3df0e4e7-79d5-4909-a4e2-c57592f9ff65",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/.claude/sessions/reviewer_509ec47e",
  "sessionId": "cade2b8d-6973-474b-bb66-65fbfa4ea818",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-23T21:17:51.702Z_

<details open><summary>🔧 Tool call — Read · `toolu_0136ViC4uQDX27XjfmMAzafs`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "af5e6292-8b7e-41e5-9977-89f0362334c0",
  "isSidechain": true,
  "agentId": "aaf1b6ed15acad458",
  "requestId": "req_011CbLCMqBLDUrEPjcHSTSHd",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "df4c62db-2918-4ba5-b93f-67cd83c3831e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/.claude/sessions/reviewer_509ec47e",
  "sessionId": "cade2b8d-6973-474b-bb66-65fbfa4ea818",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0161pBrufis3LuQ4mTZcKqtt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1585,
      "cache_read_input_tokens": 18827,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1585,
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

_source line 11 · 2026-05-23T21:17:51.707Z_

<details><summary>↩ Tool result · `toolu_0136ViC4uQDX27XjfmMAzafs`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	\paragraph{Models.}
8	We probe three instruction-tuned models with comparable parameter counts but distinct architectures: Llama-3.1-8B-Instruct (32 layers, hidden dimension 4096) \citep{grattafiori2024llama}, Qwen3-8B (36 layers, hidden dimension 4096) \citep{yang2024qwen25}, and Gemma-2-9B-IT (42 layers, hidden dimension 3584) \citep{team2024gemma}.
9	
10	\paragraph{Dataset.}
11	We use ConflictQA \citep{xie2024adaptive}, a benchmark of context-parametric knowledge conflicts where a provided context contradicts the model's parametric knowledge.
12	After verifying that each model can correctly answer the parametric-knowledge question without context, we retain 1{,}368 samples for Llama (1{,}096 train / 272 test), 966 for Qwen (773 train / 193 test), and 1{,}590 for Gemma (1{,}274 train / 316 test), split 80/20 with stratification.
13	
14	\paragraph{Translation.}
15	We translate all English contexts and questions into Chinese using a Qwen3-8B translation pipeline (EN$\to$ZH), with quality validated by COMET \citep{rei2020comet} back-translation scores.
16	
17	\paragraph{Probing.}
18	For each layer $l$, we train a logistic regression probe on the last-token residual stream representation $\mathbf{h}_l$, with binary labels indicating whether the model chose the contextual or parametric answer.
19	We report balanced accuracy to account for class imbalance.
20	All confidence intervals (CIs) are computed via bootstrap resampling with paired differences for asymmetry estimation.
21	
22	\paragraph{Non-conflict baseline.}
23	To test whether cross-lingual transfer patterns are specific to knowledge conflicts, we run the same probing pipeline on XNLI \citep{conneau2018xnli}, classifying entailment versus contradiction.
24	
25	\subsection{Within-Language Conflict Detection}
26	\label{sec:within_lang}
27	
28	Table~\ref{tab:main_results} reports balanced accuracy for all probe transfer directions.
29	All three models encode linearly detectable conflict signals in their residual streams.
30	Llama achieves 77.6\% on EN$\to$EN (peak at layer 28, 88\% depth) and 72.1\% on ZH$\to$ZH.
31	Qwen reaches 75.0\% on EN$\to$EN (peak at layer 24, 67\% depth) and 72.6\% on ZH$\to$ZH.
32	Gemma attains 76.2\% on EN$\to$EN (peak at layer 24, 57\% depth) and 71.0\% on ZH$\to$ZH.
33	All within-language accuracies are significantly above chance (binomial $p < 0.001$).
34	Figure~\ref{fig:layer_probe} shows the layer-wise probe accuracy curves for all three models.
35	These results confirm that knowledge conflict signals are linearly separable in the residual stream across all three architectures and both languages.
36	
37	%% Figure 2: Layer-wise probe accuracy
38	\begin{figure}[t]
39	\centering
40	\includegraphics[width=\columnwidth]{fig2_layerwise_probes.pdf}
41	\caption{Layer-wise probe balanced accuracy for Llama-3.1-8B (left), Qwen3-8B (center), and Gemma-2-9B-IT (right). Solid lines: residual stream probes; dashed lines (Llama and Qwen only): MLP sublayer probes. Stars mark peak layers. In the Llama panel, the vertical annotation at L13 marks the layer where steering produces significant causal influence (Fisher $p = 0.002$), coinciding with the ZH$\to$ZH probe peak but not the EN$\to$EN peak (L28). In the Gemma panel, L17 and L21 are annotated as steering-negative layers.}
42	\label{fig:layer_probe}
43	\end{figure}
44	
45	\subsection{Cross-Lingual Transfer and Asymmetry}
46	\label{sec:cross_lingual}
47	
48	All four cross-lingual transfer directions achieve balanced accuracy above chance (binomial $p < 0.001$; Table~\ref{tab:main_results}), confirming that conflict representations partially overlap across languages.
49	All three models show a consistent directional trend: probes trained on Chinese representations transfer to English (ZH$\to$EN) more accurately than the reverse direction (EN$\to$ZH).
50	For Llama, $\Delta_{\text{asym}} = +7.3$ percentage points (pp) with a 95\% bootstrap CI of [0.4, 14.0] ($p = 0.038$); for Qwen, $\Delta_{\text{asym}} = +7.2$ pp with CI [$-$0.6, 13.7]; for Gemma, $\Delta_{\text{asym}} = +6.6$ pp with CI [1.9, 11.1] ($p = 0.006$).
51	While the Qwen CI marginally includes zero, the direction is consistent across all three architectures.
52	The magnitude of this asymmetry closely matches the XNLI non-conflict baseline across all three architectures (\S\ref{sec:xnli_baseline}), and the consistent direction across all three models suggests a shared structural property rather than a model-specific artifact (Figure~\ref{fig:asymmetry_forest}).
53	
54	\begin{table}[t]
55	\centering
56	\caption{Single-seed balanced accuracy (\%) at each direction's optimal layer. $\Delta_{\text{asym}}$ and 95\% CIs from paired bootstrap ($n = 2{,}000$ resamples). Bold: best per-task direction.}
57	\label{tab:main_results}
58	\small
59	\resizebox{\columnwidth}{!}{%
60	\begin{tabular}{lccc}
61	\toprule
62	Direction & Llama-3.1-8B & Qwen3-8B & Gemma-2-9B \\
63	\midrule
64	\multicolumn{4}{l}{\textit{Conflict Task}} \\
65	EN $\to$ EN & \textbf{77.6} & \textbf{75.0} & \textbf{76.2} \\
66	ZH $\to$ ZH & 72.1 & 72.6 & 71.0 \\
67	EN $\to$ ZH & 59.6 & 67.3 & 62.9 \\
68	ZH $\to$ EN & 70.6 & 73.2 & 70.2 \\
69	$\Delta_{\text{asym}}$ & +7.3 [0.4, 14.0] & +7.2 [$-$0.6, 13.7] & +6.6 [1.9, 11.1] \\
70	\midrule
71	\multicolumn{4}{l}{\textit{XNLI Baseline}} \\
72	EN $\to$ EN & 94.0 & 96.6 & 95.6 \\
73	ZH $\to$ ZH & 87.5 & 89.5 & 89.0 \\
74	EN $\to$ ZH & 89.0 & 90.5 & 89.4 \\
75	ZH $\to$ EN & \textbf{94.9} & \textbf{97.2} & \textbf{97.5} \\
76	$\Delta_{\text{asym}}$ & +6.0 [0.9, 11.3] & +6.7 [2.4, 11.7] & +7.8 [5.7, 10.0] \\
77	\bottomrule
78	\end{tabular}%
79	}
80	\begin{flushleft}
81	\footnotesize Note: $\Delta_{\text{asym}}$ is the mean of paired bootstrap differences, not the arithmetic difference of the reported single-seed accuracies.
82	\end{flushleft}
83	\end{table}
84	
85	\subsection{Non-Conflict Baseline Comparison}
86	\label{sec:xnli_baseline}
87	
88	If the ZH$\to$EN transfer advantage were specific to knowledge conflicts, it should be absent or substantially reduced in a non-conflict semantic task.
89	We test this prediction using XNLI entailment-versus-contradiction probes.
90	All three models achieve high within-language accuracy on XNLI (Llama 94.0\% EN, 87.5\% ZH; Qwen 96.6\% EN, 89.5\% ZH; Gemma 95.6\% EN, 89.0\% ZH), confirming that the probing pipeline captures semantic distinctions beyond knowledge conflicts.
91	The XNLI probes exhibit the same directional asymmetry: Llama $\Delta_{\text{asym}} = +6.0$ pp, CI [0.9, 11.3]; Qwen $\Delta_{\text{asym}} = +6.7$ pp, CI [2.4, 11.7]; Gemma $\Delta_{\text{asym}} = +7.8$ pp, CI [5.7, 10.0] ($p < 0.001$).
92	All three XNLI CIs exclude zero and overlap substantially with the corresponding conflict-task CIs (Figure~\ref{fig:asymmetry_forest}).
93	The close match in asymmetry magnitude between conflict probes (Llama +7.3, Qwen +7.2, Gemma +6.6 pp) and XNLI probes (Llama +6.0, Qwen +6.7, Gemma +7.8 pp) indicates that the ZH$\to$EN transfer advantage is not specific to knowledge conflict representations.
94	Instead, it reflects a general cross-lingual property: Chinese-trained probes transfer to English more readily than the reverse, regardless of the downstream task.
95	
96	%% Figure 3: Asymmetry forest plot
97	\begin{figure}[t]
98	\centering
99	\includegraphics[width=\columnwidth]{fig3_asymmetry_forest.pdf}
100	\caption{Transfer asymmetry ($\Delta_{\text{asym}}$) with bootstrap 95\% CIs ($n = 2{,}000$) for conflict and XNLI tasks across all three architectures (six data points). Conflict and XNLI CIs overlap substantially within each model, indicating that the ZH$\to$EN advantage is a general cross-lingual property rather than conflict-specific. Grey band: $\pm$2~pp equivalence zone.}
101	\label{fig:asymmetry_forest}
102	\end{figure}
103	
104	\subsection{Confound Exclusion}
105	\label{sec:confounds}
106	
107	Two potential confounds could inflate cross-lingual probe accuracy: translation quality and lexical overlap between English and Chinese inputs.
108	
109	\paragraph{Translation quality.}
110	We stratify test samples by COMET score into terciles (high, medium, low) and compare EN$\to$ZH probe accuracy across strata.
111	If translation quality drove probe transfer, high-COMET samples would yield higher accuracy.
112	Table~\ref{tab:confound} shows no such pattern: Qwen exhibits a reversed direction ($\Delta = -5.6$ pp, Fisher $p = 0.695$), and Llama shows a negligible effect ($\Delta = +1.7$ pp, Fisher $p = 0.761$).
113	Translation quality does not confound the cross-lingual transfer results.
114	
115	\paragraph{Token overlap.}
116	Per-sample Jaccard similarity between English and Chinese tokenized inputs averages 3--4\%, consistent with the minimal lexical overlap between the two languages.
117	Neither model shows a positive correlation between token overlap and probe accuracy: Qwen yields no significant correlation ($p > 0.4$), and Llama shows a weak negative correlation ($r = -0.15$, $p = 0.012$), where higher overlap is associated with \emph{lower} accuracy.
118	Shared tokens do not drive cross-lingual transfer.
119	
120	\begin{table}[t]
121	\centering
122	\caption{Confound exclusion analysis. COMET tercile: $\Delta$ = balanced accuracy difference between high and low COMET score terciles for EN$\to$ZH probes (Fisher's exact test). Token overlap: Pearson correlation between per-sample Jaccard similarity and EN$\to$ZH probe accuracy.}
123	\label{tab:confound}
124	\begin{tabular}{llrl}
125	\toprule
126	Confound & Model & Result & $p$ \\
127	\midrule
128	COMET tercile & Qwen & $\Delta = -5.6$ pp & 0.695 \\
129	COMET tercile & Llama & $\Delta = +1.7$ pp & 0.761 \\
130	\midrule
131	Token overlap & Qwen & n.s. & $>$0.4 \\
132	Token overlap & Llama & $r = -0.15$ & 0.012 \\
133	\bottomrule
134	\end{tabular}
135	\end{table}
136	
137	\subsection{Causal Evidence via Representation Steering}
138	\label{sec:steering}
139	
140	The probing results establish that conflict signals are detectable, but detection does not imply causal relevance.
141	We test whether the probe weight direction $\mathbf{w}_{\text{probe}}$ causally influences conflict resolution by injecting $\alpha \cdot \mathbf{w}_{\text{probe}}$ into the last-token residual stream at a target layer during inference.
142	We measure the flip rate (fraction of samples that switch answer category) and compare against a random-direction control of equal magnitude via Fisher's exact test.
143	
144	\paragraph{L13 (mid-layer, 41\% depth).}
145	Steering at layer 13 produces bidirectional causal effects (Table~\ref{tab:steering}).
146	Positive steering ($\alpha = +5$) yields a flip rate of 19.9\% versus 6.6\% for the random control (Fisher $p = 0.002$; 4 p$\to$c flips), while negative steering ($\alpha = -20$) yields 36.0\% versus 17.6\% ($p < 0.001$; 5 c$\to$p flips); both survive Bonferroni correction.
147	All-position injection at L13 produces identical results, confirming that the causal signal is concentrated at the final token.
148	
149	\paragraph{Negative layers and coherence collapse.}
150	Steering at L28 (probe peak, 88\% depth) produces no significant effect with either last-token or all-position injection (all $p > 0.3$); L18 (MLP peak, 56\%) is similarly negative ($p > 0.44$).
151	At extreme magnitude ($\alpha = +20$), the control flip rate exceeds steering ($p = 0.053$), indicating coherence collapse.
152	
153	\paragraph{Detection $\neq$ Decision.}
154	The detectable conflict signal peaks at L28 (88\% depth), but causal influence is localized to L13 (41\% depth): late layers encode the outcome in a linearly readable form, while mid-layers host the computation that determines it.
155	
156	\paragraph{Cross-model steering.}
157	Qwen steering at L14 (39\%) and L23 (64\%) produced no significant effect (best $p = 0.682$), but was underpowered (9.5\% parametric baseline, $n = 8$).
158	Gemma-2-9B-IT L17 (40\% depth) provides a stronger test: with adequate power (16.5\% parametric, $n = 26$) and 75.3\% probe accuracy, steering produced no significant change at any $\alpha$ (best $p = 0.104$) and zero directional flips ($n_{\text{test}} = 158$).
159	Gemma's high ``neither'' baseline (34.8\% of test samples produced answers matching neither the parametric nor contextual option, versus 20.6\% for Llama) reduces the observable flip space, but does not explain the null result: the parametric and contextual classes remain large enough ($n = 26$ and $n = 45$) for directional shifts to be detectable.
160	A second Gemma layer (L21, 50\% depth; probe accuracy 76.3\%) also yielded no significant effect ($p \geq 0.623$).
161	This informative negative establishes that causal influence of the probe direction is architecture-specific.
162	
163	\begin{table}[t]
164	\centering
165	\caption{Representation steering results. Flip rate: fraction of test samples switching answer category. Control: random-direction perturbation of equal magnitude. Significant results ($p < 0.05$) in bold.$^{\dagger}$}
166	\label{tab:steering}
167	\small
168	\resizebox{\columnwidth}{!}{%
169	\begin{tabular}{lcrrrrl}
170	\toprule
171	Layer & Depth & $\alpha$ & Steer (\%) & Ctrl (\%) & Fisher $p$ & Dir. \\
172	\midrule
173	\textbf{L13} & \textbf{41\%} & $\mathbf{+5}$ & \textbf{19.9} & \textbf{6.6} & $\mathbf{0.002}$ & \textbf{4 p$\to$c} \\
174	\textbf{L13} & \textbf{41\%} & $\mathbf{-20}$ & \textbf{36.0} & \textbf{17.6} & $\mathbf{<0.001}$ & \textbf{5 c$\to$p} \\
175	L18 & 56\% & $+2$ & 3.7 & 1.5 & 0.447 & \\
176	L28 & 88\% & $-20$ & 14.7 & 16.9 & 0.740 & \\
177	L28 (all) & 88\% & $-20$ & 11.8 & 11.8 & 1.000 & \\
178	\midrule
179	\multicolumn{7}{l}{\textit{Qwen3-8B ($n_{\text{test}} = 84$; 9.5\% param.\ baseline)}} \\
180	L14 & 39\% & $-10$ & \multicolumn{2}{c}{n.s.} & 0.682 & 0 dir. \\
181	L23 & 64\% & best & \multicolumn{2}{c}{n.s.} & 1.000 & 0 dir. \\
182	\midrule
183	\multicolumn{7}{l}{\textit{Gemma-2-9B-IT ($n_{\text{test}} = 158$; 16.5\% param.\ baseline)}} \\
184	L17 & 40\% & $-20$ & 1.3 & 5.1 & 0.104 & 0 dir. \\
185	L21 & 50\% & best & \multicolumn{2}{c}{n.s.} & $\geq$0.623 & 0 dir. \\
186	\bottomrule
187	\end{tabular}%
188	}
189	\begin{flushleft}
190	\footnotesize $^{\dagger}$ At $\alpha = +20$, the control flip rate exceeds steering ($p = 0.053$), indicating coherence collapse at extreme perturbation magnitudes.
191	\end{flushleft}
192	\end{table}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "df4c62db-2918-4ba5-b93f-67cd83c3831e",
  "isSidechain": true,
  "promptId": "24af2116-26a8-4ad8-8f9a-3e42600cacf7",
  "agentId": "aaf1b6ed15acad458",
  "type": "user",
  "uuid": "3f2d1d4d-4422-4b55-9c86-0ee661957c7a",
  "sourceToolAssistantUUID": "df4c62db-2918-4ba5-b93f-67cd83c3831e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/.claude/sessions/reviewer_509ec47e",
  "sessionId": "cade2b8d-6973-474b-bb66-65fbfa4ea818",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-23T21:17:51.911Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Qo26FxAhvHBEBSqHtErEx9`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3f2d1d4d-4422-4b55-9c86-0ee661957c7a",
  "isSidechain": true,
  "agentId": "aaf1b6ed15acad458",
  "requestId": "req_011CbLCMqBLDUrEPjcHSTSHd",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d5e2e29e-1de4-4c2e-bed3-5212f9f2f7e2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/.claude/sessions/reviewer_509ec47e",
  "sessionId": "cade2b8d-6973-474b-bb66-65fbfa4ea818",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0161pBrufis3LuQ4mTZcKqtt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1585,
      "cache_read_input_tokens": 18827,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1585,
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

_source line 13 · 2026-05-23T21:17:51.918Z_

<details><summary>↩ Tool result · `toolu_01Qo26FxAhvHBEBSqHtErEx9`</summary>

```text
1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Detection and decision occur at different layers.}
5	Our central mechanistic finding is a dissociation between where conflict signals become linearly readable and where they exert causal influence on model behavior.
6	In Llama, probe accuracy on EN$\to$EN peaks at layer~28 (88\% depth), yet representation steering succeeds only at layer~13 (41\% depth; Fisher $p = 0.002$), and all late-layer interventions produce no significant behavioral change ($p > 0.3$).
7	This dissociation has a cross-lingual counterpart: the Llama ZH$\to$ZH probe peaks at L13, the same layer where steering succeeds.
8	Mid-layers thus serve a dual role as the site of cross-lingual alignment \citep{muller2021first, wendler2024llamas} and the locus where conflict signals acquire causal force.
9	The EN$\to$EN peak at L28 is best understood as a diagnostic readout, a linearly readable trace of a decision that has already been made upstream.
10	A practical implication follows: the probe peak layer is not the causal layer, and intervention experiments that target only the highest-accuracy layer risk missing the computationally relevant site.
11	Cross-layer sweeps, as conducted here, are necessary to locate the true decision point.
12	Steering failed in both Qwen (L14, L23) and Gemma (L17).
13	The Qwen p$\to$c direction was underpowered (9.5\% parametric baseline, $n = 8$), but the c$\to$p direction had adequate power ($n = 76$ non-parametric samples) and also yielded zero directional flips; the Gemma L17 test had adequate power in both directions (16.5\% parametric, $n = 26$; 28.5\% contextual, $n = 45$) and 75.3\% probe accuracy at the same relative depth (40\%) yet produced zero directional flips.
14	This informative negative establishes that the causal influence of the probe direction is architecture-specific, not a general property of mid-layer computation.
15	
16	\paragraph{Conflict signals are encoded in a general cross-lingual space.}
17	The ZH$\to$EN transfer advantage is consistent across all three architectures ($+7.3$, $+7.2$, and $+6.6$~pp for Llama, Qwen, and Gemma respectively), and the XNLI baseline comparison ($+6.0$, $+6.7$, and $+7.8$~pp) closely matches the conflict task asymmetry across all three models.
18	The asymmetry is therefore not conflict-specific; conflict detection piggybacks on the model's pre-existing cross-lingual alignment structure.
19	This interpretation connects to the linguistic affinity effects reported by \citet{zhao2026when}: the CLEAR benchmark found that conflict resolution preferences vary by language pair, a pattern that may inherit from the quality of underlying representational alignment documented by \citet{kargaran2024mexa} and \citet{wendler2024llamas}.
20	Any cross-lingual probing study must account for this baseline asymmetry before attributing transfer differences to task-specific phenomena.
21	
22	\paragraph{Direct evidence for a shared cross-lingual subspace.}
23	The matching asymmetry magnitudes between conflict and XNLI tasks provide indirect evidence for a shared subspace; we test this directly via cross-task language probe transfer.
24	A language identity probe (EN vs.\ ZH) trained on conflict task activations and evaluated on XNLI activations achieves $\geq 0.96$ accuracy at most layers across all three models, with the reverse direction (XNLI$\to$conflict) reaching $\geq 0.98$, confirming that both tasks encode language identity in a common representational subspace.
25	At Llama L13---the layer where steering succeeds---conflict$\to$XNLI transfer is 0.998 [0.993, 1.000].
26	In Gemma, however, mid-layer transfer accuracy is reduced but not absent at layers 20--22, reaching a minimum of 0.730 [0.653, 0.828] at L21---still well above chance (0.5) but notably lower than surrounding layers.
27	This dip coincides with steering-negative layer L21 but notably does not extend to L17, where cross-task transfer remains near-perfect (0.994) despite steering failure---suggesting that cross-lingual subspace disruption is not the sole factor behind negative steering outcomes.
28	
29	\paragraph{Typological distance and asymmetry magnitude.}
30	The near-zero asymmetry for EN-DE ($\Delta = +1.2$~pp, CI [$-4.8$, $+8.1$], n.s.) contrasts with the consistent $+$6--8~pp for EN-ZH across all three models, consistent with the hypothesis that asymmetry magnitude reflects the degree of representational alignment between the source and target languages.
31	With only two language pairs, we report this as an observation rather than a tested claim.
32	Notably, EN-DE token overlap (per-sample Jaccard 14.8\%) is approximately $4\times$ higher than EN-ZH (3.8\%), yet the EN$\leftrightarrow$DE transfer is near-symmetric, further ruling out shared tokens as a driver of the observed EN-ZH asymmetry.
33	
34	\paragraph{Relation to interpretability without actionability.}
35	\citet{basu2026interpretability} reported that steering failed in clinical NLP tasks despite near-perfect probe accuracy (98.2\% AUROC).
36	Our results present a partial contrast: mid-layer steering in knowledge conflict tasks succeeds with a weaker probe signal.
37	A key difference is layer selection.
38	\citeauthor{basu2026interpretability} evaluated steering at layers selected for probe accuracy; our analysis shows that the layer with highest probe accuracy (L28) also fails to steer, and causal influence is found only at L13.
39	Task characteristics may also contribute: knowledge conflict resolution involves a discrete choice between two competing answer sources, which may concentrate causal structure at a single computational stage.
40	We frame this as a difference in causal influence rather than full causal control, since steering shifts resolution probabilities without fully determining the outcome.
41	
42	\paragraph{A suggestive MLP trend.}
43	MLP sublayer probes for EN$\to$ZH show positive conflict-task gains (Qwen $+3.84$~pp, Llama $+5.21$~pp) while the XNLI baseline yields negative or zero gains, but bootstrap CIs include zero---a suggestive trend awaiting confirmation.
44	
45	\paragraph{Scope and forward look.}
46	Our analysis covers one language pair (EN-ZH), three architectures for steering, and confirmed causal effects in Llama only (see \S\ref{sec:limitations}).
47	Future work should explore diverse language pairs and alternative steering methods that may capture non-linear causal structure missed by single-direction perturbation.
48	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d5e2e29e-1de4-4c2e-bed3-5212f9f2f7e2",
  "isSidechain": true,
  "promptId": "24af2116-26a8-4ad8-8f9a-3e42600cacf7",
  "agentId": "aaf1b6ed15acad458",
  "type": "user",
  "uuid": "de4b0ba7-e731-4f7c-8828-2dc212e16d61",
  "sourceToolAssistantUUID": "d5e2e29e-1de4-4c2e-bed3-5212f9f2f7e2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/.claude/sessions/reviewer_509ec47e",
  "sessionId": "cade2b8d-6973-474b-bb66-65fbfa4ea818",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-23T21:17:52.167Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Li3NVxAeob1QkrLyTmCxo3`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "de4b0ba7-e731-4f7c-8828-2dc212e16d61",
  "isSidechain": true,
  "agentId": "aaf1b6ed15acad458",
  "requestId": "req_011CbLCMqBLDUrEPjcHSTSHd",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f121a8dd-6cc2-48ba-83d5-9ba868f02302",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/.claude/sessions/reviewer_509ec47e",
  "sessionId": "cade2b8d-6973-474b-bb66-65fbfa4ea818",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0161pBrufis3LuQ4mTZcKqtt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1585,
      "cache_read_input_tokens": 18827,
      "output_tokens": 396,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1585
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 396,
          "cache_read_input_tokens": 18827,
          "cache_creation_input_tokens": 1585,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1585,
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

_source line 15 · 2026-05-23T21:17:52.172Z_

<details><summary>↩ Tool result · `toolu_01Li3NVxAeob1QkrLyTmCxo3`</summary>

```text
1	\section*{Limitations}
2	\label{sec:limitations}
3	
4	Our study has three main limitations.
5	First, we evaluate only one language pair (English-Chinese).
6	While the consistent patterns across three architecturally distinct models are encouraging, typologically diverse language pairs (e.g., English-German, English-Japanese) are needed to assess the generality of our findings.
7	Second, causal steering succeeded only in Llama at L13.
8	Gemma L17 steering failed despite adequate statistical power (16.5\% parametric baseline, $n = 26$) and comparable probe accuracy (75.3\%), constituting an informative negative that confirms the architecture-specificity of the effect.
9	Qwen L14/L23 steering was additionally negative; the p$\to$c direction was underpowered (9.5\% parametric baseline, $n = 8$), leaving it uninformative, but the c$\to$p direction had adequate power ($n = 76$ non-parametric samples) and also yielded zero directional flips.
10	Third, the effective dataset size (966 to 1,590 samples per model after parametric knowledge verification) is constrained by the requirement that each model must correctly answer the question without context.
11	This verification step is necessary to ensure genuine knowledge conflicts, but it limits the statistical power of our analyses, particularly for stratified comparisons such as the COMET tercile ablation.
12	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f121a8dd-6cc2-48ba-83d5-9ba868f02302",
  "isSidechain": true,
  "promptId": "24af2116-26a8-4ad8-8f9a-3e42600cacf7",
  "agentId": "aaf1b6ed15acad458",
  "type": "user",
  "uuid": "594f45bc-c0cc-4e65-bdc4-d1dcff44e485",
  "sourceToolAssistantUUID": "f121a8dd-6cc2-48ba-83d5-9ba868f02302",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/.claude/sessions/reviewer_509ec47e",
  "sessionId": "cade2b8d-6973-474b-bb66-65fbfa4ea818",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 16 · 2026-05-23T21:17:54.186Z_

Now let me check the main.tex file to see how these sections are organized, and also search for any mention of German/DE results to verify what the current paper contains:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "594f45bc-c0cc-4e65-bdc4-d1dcff44e485",
  "isSidechain": true,
  "agentId": "aaf1b6ed15acad458",
  "requestId": "req_011CbLCN1wycNBX3AyFAZGx8",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "09dee410-5441-4846-bace-1916551a71c8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/.claude/sessions/reviewer_509ec47e",
  "sessionId": "cade2b8d-6973-474b-bb66-65fbfa4ea818",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Jd5dbUohZy4an9WcVC6oNZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 9577,
      "cache_read_input_tokens": 20412,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9577,
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

_source line 17 · 2026-05-23T21:17:55.050Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01DJBztRdw6dy8K1GMMD3uv6`</summary>

```json
{
  "pattern": "EN.*DE|DE.*EN|German|english-german|en-de|english-\\s*german",
  "path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "09dee410-5441-4846-bace-1916551a71c8",
  "isSidechain": true,
  "agentId": "aaf1b6ed15acad458",
  "requestId": "req_011CbLCN1wycNBX3AyFAZGx8",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "29b5e850-1882-4e40-9784-6792cba57f1c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/.claude/sessions/reviewer_509ec47e",
  "sessionId": "cade2b8d-6973-474b-bb66-65fbfa4ea818",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Jd5dbUohZy4an9WcVC6oNZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 9577,
      "cache_read_input_tokens": 20412,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9577,
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

_source line 18 · 2026-05-23T21:17:55.090Z_

<details><summary>↩ Tool result · `toolu_01DJBztRdw6dy8K1GMMD3uv6`</summary>

```text
Found 5 files
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/experiments.tex
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/sections/discussion.tex
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/discussion.tex
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/sections/limitations.tex
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/limitations.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "29b5e850-1882-4e40-9784-6792cba57f1c",
  "isSidechain": true,
  "promptId": "24af2116-26a8-4ad8-8f9a-3e42600cacf7",
  "agentId": "aaf1b6ed15acad458",
  "type": "user",
  "uuid": "2d0d78bd-47ac-4ec7-8754-ab1ebbdd9e06",
  "sourceToolAssistantUUID": "29b5e850-1882-4e40-9784-6792cba57f1c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/.claude/sessions/reviewer_509ec47e",
  "sessionId": "cade2b8d-6973-474b-bb66-65fbfa4ea818",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-23T21:17:55.264Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Bawxg79EM48o3vdHbwz7nx`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2d0d78bd-47ac-4ec7-8754-ab1ebbdd9e06",
  "isSidechain": true,
  "agentId": "aaf1b6ed15acad458",
  "requestId": "req_011CbLCN1wycNBX3AyFAZGx8",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d19c9764-9fce-4904-be3d-2ca3ad49864c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/.claude/sessions/reviewer_509ec47e",
  "sessionId": "cade2b8d-6973-474b-bb66-65fbfa4ea818",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Jd5dbUohZy4an9WcVC6oNZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 9577,
      "cache_read_input_tokens": 20412,
      "output_tokens": 225,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 9577
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 225,
          "cache_read_input_tokens": 20412,
          "cache_creation_input_tokens": 9577,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 9577,
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

_source line 20 · 2026-05-23T21:17:55.270Z_

<details><summary>↩ Tool result · `toolu_01Bawxg79EM48o3vdHbwz7nx`</summary>

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
12	\usepackage{amsmath}
13	\usepackage{amssymb}
14	\usepackage{multirow}
15	\usepackage{xcolor}
16	\usepackage{subcaption}
17	
18	\title{Cross-Lingual Knowledge Conflict Signals Inherit Directional Asymmetries from General Multilingual Representations}
19	
20	\author{Anonymous ACL submission}
21	
22	\begin{document}
23	\maketitle
24	
25	\begin{abstract}
26	\input{abstract}
27	\end{abstract}
28	
29	\input{introduction}
30	
31	\input{related_work}
32	
33	\input{method}
34	
35	\input{experiments}
36	
37	\input{discussion}
38	
39	\input{conclusion}
40	
41	\input{limitations}
42	
43	\appendix
44	
45	\section{Use of AI Assistants}
46	\label{app:ai-assistants}
47	
48	We used Claude (Anthropic) as an AI coding and writing assistant
49	throughout this work. Specifically:
50	\begin{itemize}
51	    \item \textbf{Code:} drafting experiment scripts, data-processing
52	    pipelines, and analysis utilities; debugging and refactoring.
53	    \item \textbf{Writing:} drafting and revising paper sections,
54	    polishing prose, and reformatting \LaTeX{}.
55	    \item \textbf{Literature:} summarizing related papers to inform
56	    related-work section.
57	\end{itemize}
58	
59	\bibliography{references}
60	
61	\end{document}
62	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d19c9764-9fce-4904-be3d-2ca3ad49864c",
  "isSidechain": true,
  "promptId": "24af2116-26a8-4ad8-8f9a-3e42600cacf7",
  "agentId": "aaf1b6ed15acad458",
  "type": "user",
  "uuid": "790bd016-151c-4601-93a9-52b0d6316682",
  "sourceToolAssistantUUID": "d19c9764-9fce-4904-be3d-2ca3ad49864c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/.claude/sessions/reviewer_509ec47e",
  "sessionId": "cade2b8d-6973-474b-bb66-65fbfa4ea818",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-23T21:17:56.424Z_

Perfect. Now let me also read the method section to understand the complete methodology:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "790bd016-151c-4601-93a9-52b0d6316682",
  "isSidechain": true,
  "agentId": "aaf1b6ed15acad458",
  "requestId": "req_011CbLCNFBTbPKjJ9vwSqFtJ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "68234bd8-799e-40a4-9137-a303be26e5c3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/.claude/sessions/reviewer_509ec47e",
  "sessionId": "cade2b8d-6973-474b-bb66-65fbfa4ea818",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01H9ontoheTyGMqBjW41kLaG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 1032,
      "cache_read_input_tokens": 29989,
      "output_tokens": 104,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1032
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 104,
          "cache_read_input_tokens": 29989,
          "cache_creation_input_tokens": 1032,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1032,
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

### Tool call

_source line 22 · 2026-05-23T21:17:56.499Z_

<details open><summary>🔧 Tool call — Read · `toolu_01KmPECVh3ZP2LKtncf48VkC`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "68234bd8-799e-40a4-9137-a303be26e5c3",
  "isSidechain": true,
  "agentId": "aaf1b6ed15acad458",
  "requestId": "req_011CbLCNFBTbPKjJ9vwSqFtJ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "12972d2d-0e0a-4bf7-a2c1-bb469110b795",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/.claude/sessions/reviewer_509ec47e",
  "sessionId": "cade2b8d-6973-474b-bb66-65fbfa4ea818",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01H9ontoheTyGMqBjW41kLaG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 1032,
      "cache_read_input_tokens": 29989,
      "output_tokens": 104,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1032
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 104,
          "cache_read_input_tokens": 29989,
          "cache_creation_input_tokens": 1032,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1032,
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

_source line 23 · 2026-05-23T21:17:56.506Z_

<details><summary>↩ Tool result · `toolu_01KmPECVh3ZP2LKtncf48VkC`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	Our pipeline proceeds from data construction through probing and steering, formalized below.
5	
6	\subsection{Task Formulation}
7	\label{sec:task}
8	
9	Given a context passage $c$ and question $q$, the model produces an answer that is either \emph{contextual} (derived from $c$) or \emph{parametric} (from pre-trained knowledge).
10	When $c$ contradicts parametric knowledge, the choice constitutes a knowledge conflict.
11	We train a logistic regression probe $f_\theta(\mathbf{h}_l) = \sigma(\mathbf{w}_l^\top \mathbf{h}_l + b_l)$ on the last-token residual stream representation $\mathbf{h}_l \in \mathbb{R}^d$ at layer $l$ to predict a binary label $y \in \{\text{contextual}, \text{parametric}\}$.
12	
13	\subsection{Data Construction}
14	\label{sec:data}
15	
16	We build on ConflictQA \citep{xie2024adaptive}, which pairs questions with context passages contradicting the model's parametric knowledge.
17	We filter samples by querying each model without context and retaining only those answered correctly, yielding 1{,}368 samples for Llama \citep{grattafiori2024llama}, 966 for Qwen \citep{yang2024qwen25}, and 1{,}590 for Gemma \citep{team2024gemma} (80/20 train/test split with stratification).
18	For cross-lingual transfer, we translate all inputs into Chinese using a Qwen3-8B pipeline, with quality validated by COMET \citep{rei2020comet} back-translation scores used in confound analysis (\S\ref{sec:confound_method}).
19	
20	\subsection{Activation Extraction and Probing}
21	\label{sec:extraction}
22	
23	For each input, we construct English and Chinese versions and extract the last-token residual stream $\mathbf{h}_l \in \mathbb{R}^d$ at every layer $l$ ($L = 32$ for Llama, $36$ for Qwen, $42$ for Gemma; $d = 4096$ for Llama/Qwen, $3584$ for Gemma), following the last-token aggregation principle \citep{belinkov2022probing}.
24	We record the model's answer and assign binary labels (contextual vs.\ parametric).
25	
26	\label{sec:probing}
27	At each layer, we train an $L_2$-regularized logistic regression probe \citep{belinkov2022probing, hewitt2019designing} and evaluate with balanced accuracy.
28	We report peak-layer accuracy (maximum across layers) as the primary metric.
29	Confidence intervals are estimated via bootstrap resampling ($n = 2{,}000$) \citep{ulmer2022deep}.
30	
31	\subsection{Cross-Lingual Transfer Protocol}
32	\label{sec:transfer}
33	
34	We evaluate probes in four directions: EN$\to$EN, ZH$\to$ZH (within-language upper bounds), EN$\to$ZH, and ZH$\to$EN (cross-lingual transfer).
35	We quantify directional asymmetry as $\Delta_{\text{asym}} = \text{acc}(\text{ZH}{\to}\text{EN}) - \text{acc}(\text{EN}{\to}\text{ZH})$, computed via paired bootstrap (same resampled indices for both directions).
36	
37	\subsection{Confound Exclusion}
38	\label{sec:confound_method}
39	
40	We exclude two artifacts: (1)~\emph{translation quality}---we stratify test samples by COMET score into terciles and compare probe accuracy (Fisher's exact test); (2)~\emph{token overlap}---we compute per-sample Jaccard similarity between English and Chinese token sets and test for correlation with accuracy (Pearson's $r$).
41	As a \emph{non-conflict baseline}, we apply the same pipeline to XNLI entailment-versus-contradiction \citep{conneau2018xnli}; if $\Delta_{\text{asym}} > 0$ also appears there, the asymmetry reflects a general cross-lingual property.
42	
43	\subsection{Representation Steering}
44	\label{sec:steering_method}
45	
46	To test whether the probe direction is causally relevant \citep{hewitt2019designing}, we inject $\alpha \cdot \mathbf{w}_{\text{probe}}$ into the last-token residual stream at layer $l$ during inference \citep{li2023iti, zou2023representation}:
47	$\mathbf{h}'_l = \mathbf{h}_l + \alpha \cdot \mathbf{w}_{\text{probe}}$,
48	where positive $\alpha$ pushes toward the contextual direction and negative toward the parametric.
49	As control, we inject a random vector of equal norm.
50	We measure the flip rate (fraction of samples switching answer category) and compare via Fisher's exact test with Bonferroni correction applied per model as an independent family; for Llama, $k = 10$ $\alpha$ values tested at L13 (the layer showing causal effects) yield a corrected threshold of $0.05/10 = 0.005$.
51	For last-token injection, we sweep $\alpha \in \{\pm 20, \pm 10, \pm 5, \pm 2, \pm 1\}$ ($k = 10$) at three Llama layers (L13, L18, L28) spanning 41--88\% depth; all-position and cross-model experiments use a reduced 6-value grid ($\alpha \in \{\pm 20, \pm 10, \pm 5\}$).
52	Steering evaluation uses only the conflict-condition subset of the English test data, yielding $n_{\text{test}}$ smaller than the full probe test set (e.g., 136 vs.\ 272 for Llama).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "12972d2d-0e0a-4bf7-a2c1-bb469110b795",
  "isSidechain": true,
  "promptId": "24af2116-26a8-4ad8-8f9a-3e42600cacf7",
  "agentId": "aaf1b6ed15acad458",
  "type": "user",
  "uuid": "e6fd881b-1ff6-4427-852e-8f1d6df81e22",
  "sourceToolAssistantUUID": "12972d2d-0e0a-4bf7-a2c1-bb469110b795",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/.claude/sessions/reviewer_509ec47e",
  "sessionId": "cade2b8d-6973-474b-bb66-65fbfa4ea818",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-23T21:17:57.894Z_

Excellent. Now let me check the exact location of the EN-DE result mentioned in the discussion to get the full context:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e6fd881b-1ff6-4427-852e-8f1d6df81e22",
  "isSidechain": true,
  "agentId": "aaf1b6ed15acad458",
  "requestId": "req_011CbLCNLPk2t4ow2djZiZ97",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "831e72f1-0053-470c-b427-5d4d27a031a5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/.claude/sessions/reviewer_509ec47e",
  "sessionId": "cade2b8d-6973-474b-bb66-65fbfa4ea818",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01NpS51ZWqEcy2Q9sUwNje79",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1684,
      "cache_read_input_tokens": 31021,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1684,
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

_source line 25 · 2026-05-23T21:17:58.918Z_

<details open><summary>🔧 Tool call — Grep · `toolu_016rjggCyn7Pyk2ttKJJ5t8g`</summary>

```json
{
  "pattern": "near-zero|EN-DE|1\\.2",
  "path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/sections/discussion.tex",
  "output_mode": "content",
  "context": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "831e72f1-0053-470c-b427-5d4d27a031a5",
  "isSidechain": true,
  "agentId": "aaf1b6ed15acad458",
  "requestId": "req_011CbLCNLPk2t4ow2djZiZ97",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "4f2a7474-ffda-479c-8ace-348dd5b1427d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/.claude/sessions/reviewer_509ec47e",
  "sessionId": "cade2b8d-6973-474b-bb66-65fbfa4ea818",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01NpS51ZWqEcy2Q9sUwNje79",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1684,
      "cache_read_input_tokens": 31021,
      "output_tokens": 176,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1684
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 176,
          "cache_read_input_tokens": 31021,
          "cache_creation_input_tokens": 1684,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1684,
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

_source line 26 · 2026-05-23T21:17:58.939Z_

<details><summary>↩ Tool result · `toolu_016rjggCyn7Pyk2ttKJJ5t8g`</summary>

```text
27-This dip coincides with steering-negative layer L21 but notably does not extend to L17, where cross-task transfer remains near-perfect (0.994) despite steering failure---suggesting that cross-lingual subspace disruption is not the sole factor behind negative steering outcomes.
28-
29-\paragraph{Typological distance and asymmetry magnitude.}
30:The near-zero asymmetry for EN-DE ($\Delta = +1.2$~pp, CI [$-4.8$, $+8.1$], n.s.) contrasts with the consistent $+$6--8~pp for EN-ZH across all three models, consistent with the hypothesis that asymmetry magnitude reflects the degree of representational alignment between the source and target languages.
31-With only two language pairs, we report this as an observation rather than a tested claim.
32:Notably, EN-DE token overlap (per-sample Jaccard 14.8\%) is approximately $4\times$ higher than EN-ZH (3.8\%), yet the EN$\leftrightarrow$DE transfer is near-symmetric, further ruling out shared tokens as a driver of the observed EN-ZH asymmetry.
33-
34-\paragraph{Relation to interpretability without actionability.}
35-\citet{basu2026interpretability} reported that steering failed in clinical NLP tasks despite near-perfect probe accuracy (98.2\% AUROC).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4f2a7474-ffda-479c-8ace-348dd5b1427d",
  "isSidechain": true,
  "promptId": "24af2116-26a8-4ad8-8f9a-3e42600cacf7",
  "agentId": "aaf1b6ed15acad458",
  "type": "user",
  "uuid": "f79a6437-fdca-4f8c-9a6d-5743923597f8",
  "sourceToolAssistantUUID": "4f2a7474-ffda-479c-8ace-348dd5b1427d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/.claude/sessions/reviewer_509ec47e",
  "sessionId": "cade2b8d-6973-474b-bb66-65fbfa4ea818",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 27 · 2026-05-23T21:18:11.355Z_

Perfect! Now I have a comprehensive view of the paper. Let me compile my findings:

## Summary of Paper Content Analysis

I've read the current LaTeX files for the clkc_mech_interp paper. Here are my findings across the key sections you requested:

### 1. **Abstract and Introduction - Claims about Cross-Lingual Properties**

The paper makes explicit claims about "general cross-lingual properties":
- **Abstract** (line 3): States the asymmetry "inherits from the model's general multilingual structure rather than conflict-specific encoding"
- **Introduction** (lines 23-26): Directly states: "This asymmetry, however, is not conflict-specific... The conflict asymmetry thus inherits from a general property of English-dominant models"

The asymmetry being discussed is directional: Chinese→English probes transfer ~7 percentage points more accurately than English→Chinese across all three models tested.

### 2. **Experiments/Results Section - Language Coverage**

**Current language pairs in the paper:**
- **Primary**: English-Chinese (EN-ZH) - extensively evaluated
- **Secondary**: English-German (EN-DE) - mentioned ONLY in the Discussion section

**German/DE Results Location:**
The only mention of German results is in the Discussion section, "Typological distance and asymmetry magnitude" subsection:
- EN-DE shows near-zero asymmetry: Δ = +1.2 pp, CI [-4.8, +8.1], not significant
- This is presented as an **observation rather than a tested claim** ("With only two language pairs, we report this as an observation")
- NO German results appear in any tables or main experiments
- No German results in the experiments section itself

**What's actually in the tables:**
- Table 1 (tab:main_results): Shows ConflictQA task results for Llama-3.1-8B, Qwen3-8B, and Gemma-2-9B across EN↔EN, ZH↔ZH, EN↔ZH, ZH↔EN
- Table 1 also includes XNLI baseline for the same language pairs
- Table 2 (tab:confound): Confound exclusion analysis (COMET terciles, token overlap) - EN-ZH only
- Table 3 (tab:steering): Representation steering results - primarily Llama L13, with some Qwen and Gemma layers

### 3. **Discussion Section - Limitations and Steering Discussion**

Key limitations explicitly stated in the Discussion:
- **Line 29-33**: The EN-DE result is introduced as a "typological distance" observation that is under-powered ("With only two language pairs")
- **Steering architecture-specificity** (lines 12-14): Causal effects (steering) succeeded only in Llama at L13; failed in both Qwen and Gemma despite adequate power
- **Cross-task language probe** (lines 22-27): Discussion of whether language identity encodes in a shared subspace - finds near-perfect transfer for conflict↔XNLI except a dip at Gemma L21

### 4. **Limitations Section - Formal Statement**

Three main limitations explicitly documented:
1. **Single language pair**: "We evaluate only one language pair (English-Chinese)" - describes EN-ZH as the primary study
2. **Steering architecture-specificity**: Causal effects only confirmed in Llama; failures in Qwen (underpowered p→c direction) and Gemma (adequate power, zero flips)
3. **Dataset size constraints**: 966-1,590 samples per model limit statistical power for stratified comparisons

### Key Finding for Reviewers

**The EN-DE result is parenthetical, not central to the paper's claims:**
- It appears only in Discussion (not Experiments)
- Authors explicitly label it as an "observation rather than a tested claim"
- It's not in any main table
- The paper's core evidence is EN-ZH only
- This actually strengthens the paper's caution about generalization - they acknowledge the limitation directly

The paper's main contribution about asymmetry inheriting from "general cross-lingual structure" is supported primarily by the EN-ZH→XNLI baseline comparison, which shows matching asymmetry patterns across tasks, rather than cross-linguistic evidence.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f79a6437-fdca-4f8c-9a6d-5743923597f8",
  "isSidechain": true,
  "agentId": "aaf1b6ed15acad458",
  "requestId": "req_011CbLCNWqntBejUW3HFjLob",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d9dee210-83b4-42a7-990b-aeff5106b870",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/.claude/sessions/reviewer_509ec47e",
  "sessionId": "cade2b8d-6973-474b-bb66-65fbfa4ea818",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01MPLMP4UXFdQCb6w9w7xo4T",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 521,
      "cache_read_input_tokens": 32705,
      "output_tokens": 1002,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 521
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 1002,
          "cache_read_input_tokens": 32705,
          "cache_creation_input_tokens": 521,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 521,
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
