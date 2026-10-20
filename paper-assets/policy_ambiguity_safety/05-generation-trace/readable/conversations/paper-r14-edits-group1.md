# paper r14 edits group1

**Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on Customer-Service Agent Safety** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 31
- **Recorded user turns:** 0
- **Tool calls:** 15
- **Original source:** `logs/chats/worker_paper_r14_edits_group1_20260522T141222.jsonl`
- **Structured JSON:** [`12f44b88fca6c462c3fe.json`](../../sessions/12/12f44b88fca6c462c3fe.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

31 recorded events

### Tool call

_source line 1 · 2026-05-22T14:13:44.103469+00:00_

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
  "session": "worker_paper_r14_edits_group1_20260522T141222",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-22T14:13:44.103792+00:00_

1	\begin{abstract}
2	LLM-based agents operate under natural-language policy specifications that inevitably contain ambiguity, yet the causal relationship between ambiguity type and safety violations remains unmeasured. We present a matched-pair study on $\tau^2$-bench with 300 clause pairs spanning a six-type ambiguity taxonomy, evaluated across five models (2,997 episodes). Three findings emerge. First, ambiguous clauses increase violation rates by 34.0 percentage points (OR $= 15.1$), with a perturbation control supporting ambiguity-specific causation. Second, effects range from $+$18.7\,pp (coreferential, confound-free) to $+$49.2\,pp (incompleteness, upper bound reflecting an information-addition confound); the remaining five types form a risk gradient rather than sharp tiers, with rankings partly margin-dependent. Third, error analysis of 614 violation traces reveals \emph{Disambiguation Neglect} ($\leq$11\% per-model awareness, 4.6\% overall) and \emph{systematic nocuity}---41.3\% of clauses triggering model-convergent violations---indicating clause-level rather than model-level risk factors. These results---observed in customer-service policy domains---motivate type-aware policy auditing and externalized ambiguity detection for policy-governed agent deployments.
3	\end{abstract}
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r14_edits_group1_20260522T141222",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-22T14:13:44.103968+00:00_

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
  "session": "worker_paper_r14_edits_group1_20260522T141222",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-22T14:13:44.104128+00:00_

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
  "session": "worker_paper_r14_edits_group1_20260522T141222",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-22T14:13:44.104311+00:00_

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
  "session": "worker_paper_r14_edits_group1_20260522T141222",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-22T14:13:44.104446+00:00_

1	\section{Conclusion}
2	
3	Ambiguous policy clauses increase agent safety violations by 34.0\,pp (OR\,$=$\,15.1); clause-level wording drives 22.4\% of variance versus 0.4\% for type and 1.0\% for model (60.8\% residual). Effects range from $+$18.7\,pp (coreferential, confound-free) to $+$49.2\,pp (incompleteness, upper bound), forming a margin-dependent gradient across seven models. With disambiguation neglect in $>$89\% of cases and 41.3\% model-convergent violations, type-aware auditing and externalized detection are critical for customer-service deployments.
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r14_edits_group1_20260522T141222",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-22T14:13:44.104571+00:00_

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
  "session": "worker_paper_r14_edits_group1_20260522T141222",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-22T14:13:44.104704+00:00_

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
  "session": "worker_paper_r14_edits_group1_20260522T141222",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-22T14:13:44.104899+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/abstract.tex",
  "old_string": "effects range from $+$18.7\\,pp (coreferential, confound-free) to $+$49.2\\,pp (incompleteness, upper bound reflecting an information-addition confound)",
  "new_string": "effects range from $+$18.7\\,pp (coreferential) to $+$36.0\\,pp (authorization scope) among confound-controlled types; incompleteness reaches $+$49.2\\,pp but reflects an information-addition confound"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r14_edits_group1_20260522T141222",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/abstract.tex",
    "old_string": "effects range from $+$18.7\\,pp (coreferential, confound-free) to $+$49.2\\,pp (incompleteness, upper bound reflecting an information-addition confound)",
    "new_string": "effects range from $+$18.7\\,pp (coreferential) to $+$36.0\\,pp (authorization scope) among confound-controlled types; incompleteness reaches $+$49.2\\,pp but reflects an information-addition confound"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-22T14:13:44.105055+00:00_

The file /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/abstract.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r14_edits_group1_20260522T141222",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-22T14:13:44.105193+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/abstract.tex",
  "old_string": "for policy-governed agent deployments",
  "new_string": "for customer-service policy domains"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r14_edits_group1_20260522T141222",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/abstract.tex",
    "old_string": "for policy-governed agent deployments",
    "new_string": "for customer-service policy domains"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-22T14:13:44.105331+00:00_

The file /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/abstract.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r14_edits_group1_20260522T141222",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-22T14:13:44.105451+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/introduction.tex",
  "old_string": "(2)~incompleteness as a consistent upper-bound risk type across all models and margins, with clause-level wording---not type membership or model identity---driving the bulk of violation variance (22.4\\% vs.\\ 0.4\\% and 1.0\\%, respectively; 60.8\\% residual; \\S\\ref{sec:results})",
  "new_string": "(2)~incompleteness as a consistent upper-bound risk type across all models and margins, with a variance decomposition showing that individual clause wording (22.4\\%) dominates type membership (0.4\\%) and model identity (1.0\\%)---motivating clause-level auditing while the type taxonomy retains value for differential intervention design (\\S\\ref{sec:discussion})"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r14_edits_group1_20260522T141222",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/introduction.tex",
    "old_string": "(2)~incompleteness as a consistent upper-bound risk type across all models and margins, with clause-level wording---not type membership or model identity---driving the bulk of violation variance (22.4\\% vs.\\ 0.4\\% and 1.0\\%, respectively; 60.8\\% residual; \\S\\ref{sec:results})",
    "new_string": "(2)~incompleteness as a consistent upper-bound risk type across all models and margins, with a variance decomposition showing that individual clause wording (22.4\\%) dominates type membership (0.4\\%) and model identity (1.0\\%)---motivating clause-level auditing while the type taxonomy retains value for differential intervention design (\\S\\ref{sec:discussion})"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-22T14:13:44.105596+00:00_

The file /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/introduction.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r14_edits_group1_20260522T141222",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-22T14:13:44.105714+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/introduction.tex",
  "old_string": "with fewer than 11\\% showing any disambiguation awareness.",
  "new_string": "with fewer than 11\\% showing any disambiguation awareness (4.6\\% overall; \\S\\ref{sec:analysis})."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r14_edits_group1_20260522T141222",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/introduction.tex",
    "old_string": "with fewer than 11\\% showing any disambiguation awareness.",
    "new_string": "with fewer than 11\\% showing any disambiguation awareness (4.6\\% overall; \\S\\ref{sec:analysis})."
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-22T14:13:44.105854+00:00_

The file /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/introduction.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r14_edits_group1_20260522T141222",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-22T14:13:44.105972+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/conclusion.tex",
  "old_string": "Effects range from $+$18.7\\,pp (coreferential, confound-free) to $+$49.2\\,pp (incompleteness, upper bound)",
  "new_string": "Effects range from $+$18.7\\,pp (coreferential) to $+$36.0\\,pp (authorization scope) among confound-controlled types, with incompleteness reaching $+$49.2\\,pp (upper bound, conditional on an information-addition confound)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r14_edits_group1_20260522T141222",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/conclusion.tex",
    "old_string": "Effects range from $+$18.7\\,pp (coreferential, confound-free) to $+$49.2\\,pp (incompleteness, upper bound)",
    "new_string": "Effects range from $+$18.7\\,pp (coreferential) to $+$36.0\\,pp (authorization scope) among confound-controlled types, with incompleteness reaching $+$49.2\\,pp (upper bound, conditional on an information-addition confound)"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-22T14:13:44.106107+00:00_

The file /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/conclusion.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r14_edits_group1_20260522T141222",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-22T14:13:44.106247+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/discussion.tex",
  "old_string": "\\paragraph{Prompt-based mitigation.}",
  "new_string": "\\paragraph{Taxonomy as intervention design.}\nType membership explains only 0.4\\% of violation variance versus 22.4\\% for individual clause wording---knowing a clause's type adds negligible predictive power. However, the taxonomy's value lies not in prediction but in intervention design. Our mitigation experiments reveal type-specific asymmetries: authorization scope responds to prompted boundary checking ($-12$\\,pp, $p = 0.070$), while incompleteness resists or worsens under prompting ($+14$\\,pp), and the three failure mechanisms (\\S\\ref{sec:analysis}) map to distinct mitigation strategies---boundary enforcement for authorization scope, information supplementation for incompleteness, parse constraint for structural misparse types. The practical recommendation is therefore two-tiered: clause-level auditing for risk assessment, type-level guidance for intervention selection.\n\n\\paragraph{Prompt-based mitigation.}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r14_edits_group1_20260522T141222",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/discussion.tex",
    "old_string": "\\paragraph{Prompt-based mitigation.}",
    "new_string": "\\paragraph{Taxonomy as intervention design.}\nType membership explains only 0.4\\% of violation variance versus 22.4\\% for individual clause wording---knowing a clause's type adds negligible predictive power. However, the taxonomy's value lies not in prediction but in intervention design. Our mitigation experiments reveal type-specific asymmetries: authorization scope responds to prompted boundary checking ($-12$\\,pp, $p = 0.070$), while incompleteness resists or worsens under prompting ($+14$\\,pp), and the three failure mechanisms (\\S\\ref{sec:analysis}) map to distinct mitigation strategies---boundary enforcement for authorization scope, information supplementation for incompleteness, parse constraint for structural misparse types. The practical recommendation is therefore two-tiered: clause-level auditing for risk assessment, type-level guidance for intervention selection.\n\n\\paragraph{Prompt-based mitigation.}"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-22T14:13:44.106392+00:00_

The file /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/discussion.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r14_edits_group1_20260522T141222",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-22T14:13:44.106508+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/discussion.tex",
  "old_string": "A proof-of-concept classifier",
  "new_string": "Notably, authorization scope resolution adds more tokens ($+$36.1 words) than incompleteness ($+$34.6) yet triggers fewer violations, suggesting that information \\emph{quality}---not mere quantity---modulates the information-addition confound (Appendix~\\ref{app:confound}). A proof-of-concept classifier"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r14_edits_group1_20260522T141222",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/discussion.tex",
    "old_string": "A proof-of-concept classifier",
    "new_string": "Notably, authorization scope resolution adds more tokens ($+$36.1 words) than incompleteness ($+$34.6) yet triggers fewer violations, suggesting that information \\emph{quality}---not mere quantity---modulates the information-addition confound (Appendix~\\ref{app:confound}). A proof-of-concept classifier"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-22T14:13:44.106687+00:00_

The file /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/discussion.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r14_edits_group1_20260522T141222",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-22T14:13:44.106823+00:00_

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
  "session": "worker_paper_r14_edits_group1_20260522T141222",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-22T14:13:44.106944+00:00_

1	\begin{abstract}
2	LLM-based agents operate under natural-language policy specifications that inevitably contain ambiguity, yet the causal relationship between ambiguity type and safety violations remains unmeasured. We present a matched-pair study on $\tau^2$-bench with 300 clause pairs spanning a six-type ambiguity taxonomy, evaluated across five models (2,997 episodes). Three findings emerge. First, ambiguous clauses increase violation rates by 34.0 percentage points (OR $= 15.1$), with a perturbation control supporting ambiguity-specific causation. Second, effects range from $+$18.7\,pp (coreferential) to $+$36.0\,pp (authorization scope) among confound-controlled types; incompleteness reaches $+$49.2\,pp but reflects an information-addition confound; the remaining five types form a risk gradient rather than sharp tiers, with rankings partly margin-dependent. Third, error analysis of 614 violation traces reveals \emph{Disambiguation Neglect} ($\leq$11\% per-model awareness, 4.6\% overall) and \emph{systematic nocuity}---41.3\% of clauses triggering model-convergent violations---indicating clause-level rather than model-level risk factors. These results---observed in customer-service policy domains---motivate type-aware policy auditing and externalized ambiguity detection for customer-service policy domains.
3	\end{abstract}
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r14_edits_group1_20260522T141222",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-22T14:13:44.107072+00:00_

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
  "session": "worker_paper_r14_edits_group1_20260522T141222",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-22T14:13:44.107226+00:00_

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
  "session": "worker_paper_r14_edits_group1_20260522T141222",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-22T14:13:44.107368+00:00_

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
  "session": "worker_paper_r14_edits_group1_20260522T141222",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-22T14:13:44.107489+00:00_

1	\section{Conclusion}
2	
3	Ambiguous policy clauses increase agent safety violations by 34.0\,pp (OR\,$=$\,15.1); clause-level wording drives 22.4\% of variance versus 0.4\% for type and 1.0\% for model (60.8\% residual). Effects range from $+$18.7\,pp (coreferential) to $+$36.0\,pp (authorization scope) among confound-controlled types, with incompleteness reaching $+$49.2\,pp (upper bound, conditional on an information-addition confound), forming a margin-dependent gradient across seven models. With disambiguation neglect in $>$89\% of cases and 41.3\% model-convergent violations, type-aware auditing and externalized detection are critical for customer-service deployments.
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r14_edits_group1_20260522T141222",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-22T14:13:44.107612+00:00_

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
  "session": "worker_paper_r14_edits_group1_20260522T141222",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-22T14:13:44.107744+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Differential nocuity.}
5	Building on \citet{berry_kamsties_2004}'s nocuous/innocuous distinction, our results are consistent with a \emph{differential nocuity} hypothesis \citep{willis_nocuous_2008}: risk depends on ambiguity type (base vulnerability), safety training (selective mitigation), and disambiguation channel availability. Types with explicit decision points (e.g., authorization scope) appear more amenable to both safety training and prompted intervention than gap-filling types (e.g., incompleteness), where mitigation attempts can backfire (see below).
6	
7	\paragraph{Taxonomy as intervention design.}
8	Type membership explains only 0.4\% of violation variance versus 22.4\% for individual clause wording---knowing a clause's type adds negligible predictive power. However, the taxonomy's value lies not in prediction but in intervention design. Our mitigation experiments reveal type-specific asymmetries: authorization scope responds to prompted boundary checking ($-12$\,pp, $p = 0.070$), while incompleteness resists or worsens under prompting ($+14$\,pp), and the three failure mechanisms (\S\ref{sec:analysis}) map to distinct mitigation strategies---boundary enforcement for authorization scope, information supplementation for incompleteness, parse constraint for structural misparse types. The practical recommendation is therefore two-tiered: clause-level auditing for risk assessment, type-level guidance for intervention selection.
9	
10	\paragraph{Prompt-based mitigation.}
11	Building on the five-model type-specific mitigation study ($-$8.5\,pp pooled, unpaired design; Appendix~\ref{app:mitigation}), we test whether disambiguation can be prompted at finer granularity using a matched-pair design. We evaluate generic awareness prompting (``the policy may contain ambiguous clauses; ask for clarification'') and type-specific prompting (targeting incompleteness, authorization scope, and lexical ambigui
…[truncated 1726 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r14_edits_group1_20260522T141222",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 31 · 2026-05-22T14:13:44.107926+00:00_

全部 8 处编辑完成，验证通过：

1. **abstract.tex** — confound-free range 改为 confound-controlled 表述；domain scope 改为 "for customer-service policy domains"
2. **introduction.tex** — Contribution (2) 重写为 variance decomposition + taxonomy value 表述；L19 添加了 "(4.6\% overall; \S\ref{sec:analysis})"
3. **conclusion.tex** — range 同步更新，incompleteness 标注 conditional on confound
4. **discussion.tex** — 插入 "Taxonomy as intervention design" 新段落；"Practical implications" 段前添加 info quality vs quantity 句

LaTeX 语法、括号配对均正确，无重复句子。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_r14_edits_group1_20260522T141222"
}
```

</details>

---
