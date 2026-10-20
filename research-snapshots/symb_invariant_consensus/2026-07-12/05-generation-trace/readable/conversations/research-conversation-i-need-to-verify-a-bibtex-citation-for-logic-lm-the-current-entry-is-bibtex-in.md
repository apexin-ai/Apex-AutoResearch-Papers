# Research conversation: I need to verify a BibTeX citation for Logic-LM. The current entry is: ```bibtex @inproceedings{pan2023logiclm, title={L

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 22
- **Recorded user turns:** 1
- **Tool calls:** 8
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-acc61023d8167708b.jsonl`
- **Structured JSON:** [`0648633044e6d347ffb0.json`](../../sessions/06/0648633044e6d347ffb0.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

22 recorded events

### User

_source line 1 · 2026-05-26T04:37:00.394Z_

I need to verify a BibTeX citation for Logic-LM. The current entry is:

```bibtex
@inproceedings{pan2023logiclm,
  title={Logic-{LM}: Empowering Large Language Models with Symbolic Solvers for Faithful Logical Reasoning},
  author={Pan, Liangming and Alber, Alon and Xu, Wenhu and Deng, Yixin and Chen, Huan and Ji, Heng},
  booktitle={EMNLP Findings},
  year={2023}
}
```

The claim is that the correct authors are "Liangming Pan, Alon Albalak, Xinyi Wang, William Wang" per ACL Anthology (https://aclanthology.org/2023.findings-emnlp.248/).

The current author list has "Alber, Alon" (should be "Albalak, Alon"), "Xu, Wenhu" (should be "Wang, Xinyi"), "Deng, Yixin" and "Chen, Huan" and "Ji, Heng" (should just be "Wang, William Yang").

Search for all in-text citations of "pan2023logiclm" in .tex files under /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "88a2bcb6-a784-4ef7-b4e3-429a2c5e0517",
  "agentId": "acc61023d8167708b",
  "type": "user",
  "uuid": "e2e83d3c-4bc2-4fe7-aaa9-46a3d0830ac1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/director_909d512a",
  "sessionId": "8f3db67b-bd86-4ccb-8f1e-4ba0a20486fe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "humming-wondering-willow"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-26T04:37:02.124Z_

I'll search for all in-text citations of "pan2023logiclm" in the paper's LaTeX files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e2e83d3c-4bc2-4fe7-aaa9-46a3d0830ac1",
  "isSidechain": true,
  "agentId": "acc61023d8167708b",
  "requestId": "req_011CbQZU63fYnM9BfJRK94XQ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "2cfc9f7a-0fc4-4f40-986c-37a481f2feb1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/director_909d512a",
  "sessionId": "8f3db67b-bd86-4ccb-8f1e-4ba0a20486fe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "humming-wondering-willow",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01LU2ikYxHynDVnavfVPkn4B",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 769,
      "cache_read_input_tokens": 36738,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 769,
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

_source line 3 · 2026-05-26T04:37:02.381Z_

<details open><summary>🔧 Tool call — Glob · `toolu_018GP2hLLPJDbtGHeB1kP3e9`</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/**/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2cfc9f7a-0fc4-4f40-986c-37a481f2feb1",
  "isSidechain": true,
  "agentId": "acc61023d8167708b",
  "requestId": "req_011CbQZU63fYnM9BfJRK94XQ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "8e83bda1-9410-4f05-8e4c-90da621134c0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/director_909d512a",
  "sessionId": "8f3db67b-bd86-4ccb-8f1e-4ba0a20486fe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "humming-wondering-willow",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01LU2ikYxHynDVnavfVPkn4B",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 769,
      "cache_read_input_tokens": 36738,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 769,
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

_source line 4 · 2026-05-26T04:37:02.402Z_

<details><summary>↩ Tool result · `toolu_018GP2hLLPJDbtGHeB1kP3e9`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/solutions.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/figures/fig3_causal_dag_v11.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/limitations_content.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/diagnosis.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/analysis.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8e83bda1-9410-4f05-8e4c-90da621134c0",
  "isSidechain": true,
  "promptId": "88a2bcb6-a784-4ef7-b4e3-429a2c5e0517",
  "agentId": "acc61023d8167708b",
  "type": "user",
  "uuid": "75895a11-d8d1-4df2-9fd5-9001505ae969",
  "sourceToolAssistantUUID": "8e83bda1-9410-4f05-8e4c-90da621134c0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/director_909d512a",
  "sessionId": "8f3db67b-bd86-4ccb-8f1e-4ba0a20486fe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "humming-wondering-willow"
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-26T04:37:02.888Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01LX2qWh4VzYgVKbb96rLRL5`</summary>

```json
{
  "pattern": "pan2023logiclm",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper",
  "type": "tex",
  "output_mode": "content",
  "context": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "75895a11-d8d1-4df2-9fd5-9001505ae969",
  "isSidechain": true,
  "agentId": "acc61023d8167708b",
  "requestId": "req_011CbQZU63fYnM9BfJRK94XQ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "35299892-829a-4449-8047-c7a3445007d8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/director_909d512a",
  "sessionId": "8f3db67b-bd86-4ccb-8f1e-4ba0a20486fe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "humming-wondering-willow",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01LU2ikYxHynDVnavfVPkn4B",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 769,
      "cache_read_input_tokens": 36738,
      "output_tokens": 258,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 769
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 258,
          "cache_read_input_tokens": 36738,
          "cache_creation_input_tokens": 769,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 769,
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

_source line 6 · 2026-05-26T04:37:02.907Z_

<details><summary>↩ Tool result · `toolu_01LX2qWh4VzYgVKbb96rLRL5`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/related_work.tex-7-
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/related_work.tex-8-\looseness=-1
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/related_work.tex-9-\paragraph{Neuro-symbolic reasoning.}
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/related_work.tex:10:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/related_work.tex-11-
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/related_work.tex-12-\looseness=-1
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/related_work.tex-13-\paragraph{Verification and test-time scaling.}
--
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex-1476-[Omitted long context line]
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex-1477-
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex-1478-\paragraph{Implications for neuro-symbolic practitioners.}
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex:1479:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex-1480-
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex-1481-\paragraph{Test-time scaling implications.}
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex-1482-[Omitted long context line]
--
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/introduction.tex-1-\section{Introduction}\label{sec:introduction}
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/introduction.tex-2-
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/introduction.tex-3-\looseness=-1
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/introduction.tex:4:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/introduction.tex-5-
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/introduction.tex-6-\begin{figure*}[t!]
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/introduction.tex-7-\centering
--
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/references.bib-111-
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/references.bib-112-%%% Neuro-Symbolic Reasoning %%%
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/references.bib-113-
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/references.bib:114:@inproceedings{pan2023logiclm,
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/references.bib-115-  title={Logic-{LM}: Empowering Large Language Models with Symbolic Solvers for Faithful Logical Reasoning},
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/references.bib-116-  author={Pan, Liangming and Alber, Alon and Xu, Wenhu and Deng, Yixin and Chen, Huan and Ji, Heng},
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/references.bib-117-  booktitle={EMNLP Findings},
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "35299892-829a-4449-8047-c7a3445007d8",
  "isSidechain": true,
  "promptId": "88a2bcb6-a784-4ef7-b4e3-429a2c5e0517",
  "agentId": "acc61023d8167708b",
  "type": "user",
  "uuid": "4efab6c6-b0e3-4f8c-9e27-9e841aad9393",
  "sourceToolAssistantUUID": "35299892-829a-4449-8047-c7a3445007d8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/director_909d512a",
  "sessionId": "8f3db67b-bd86-4ccb-8f1e-4ba0a20486fe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "humming-wondering-willow"
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-26T04:37:04.913Z_

The grep output shows there are matches but some lines were omitted. Let me read the specific files that contain citations to get the exact context.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4efab6c6-b0e3-4f8c-9e27-9e841aad9393",
  "isSidechain": true,
  "agentId": "acc61023d8167708b",
  "requestId": "req_011CbQZUGu2dKjqp6orzhQRk",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "cec3ba6b-01eb-41df-aef4-a242ae398d8f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/director_909d512a",
  "sessionId": "8f3db67b-bd86-4ccb-8f1e-4ba0a20486fe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "humming-wondering-willow",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_014CgkU3mcN4nqVmZNQGzXyE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 3121,
      "cache_read_input_tokens": 37507,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3121,
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

_source line 8 · 2026-05-26T04:37:05.169Z_

<details open><summary>🔧 Tool call — Read · `toolu_01A8EhBNmaiVR4M1s12mwKZr`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cec3ba6b-01eb-41df-aef4-a242ae398d8f",
  "isSidechain": true,
  "agentId": "acc61023d8167708b",
  "requestId": "req_011CbQZUGu2dKjqp6orzhQRk",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "3d0b4f87-5170-4448-8898-e2c789775308",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/director_909d512a",
  "sessionId": "8f3db67b-bd86-4ccb-8f1e-4ba0a20486fe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "humming-wondering-willow",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_014CgkU3mcN4nqVmZNQGzXyE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 3121,
      "cache_read_input_tokens": 37507,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3121,
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

_source line 9 · 2026-05-26T04:37:05.189Z_

<details><summary>↩ Tool result · `toolu_01A8EhBNmaiVR4M1s12mwKZr`</summary>

```text
1	\section{Related Work}
2	\label{sec:related-work}
3	
4	\looseness=-1
5	\paragraph{Self-consistency and ensemble theory.}
6	Self-consistency (SC) selects the majority answer across chain-of-thought traces \citep{wang2023sc}, with extensions for free-form generation \citep{chen2024usc}, confidence weighting \citep{taubenfeld2025cisc}, diverse prompting \citep{li2023diverse}, and reasoning-aware filtering \citep{wan2024rasc, toh2024notallvotes, kim2026reasc}. SC gains plateau early \citep{loo2025reevaluating, byerly2025selfconsistency}. The Condorcet Jury Theorem \citep{condorcet1785} guarantees majority-vote convergence under independence; ensemble theory \citep{dietterich2000ensemble, krogh1994neural} requires error diversity. \citet{ladha1992correlated} show correlated voters reduce effective ensemble size; our $K_\text{eff}$ adapts Fleiss' $\kappa$ from diversity metrics \citep{kuncheva2003measures, brown2005diversity} to quantify this (\S\ref{sec:pipeline}). \citet{kim2025correlated} demonstrate correlated LLM errors; \citet{kuai2026independent} propose cross-model independence auditing.
7	
8	\looseness=-1
9	\paragraph{Neuro-symbolic reasoning.}
10	Three paradigms exist: \emph{specification-generation} \citep{pan2023logiclm, olausson2023linc, ye2024satlm} and \emph{program-generation} \citep{gao2023pal, chen2023program, lyu2023faithful} formalize before answer generation; \emph{trace-extraction} (this work) operates post-hoc, inheriting confirmation bias (\S\ref{sec:confirmation-bias}). Recent work extends symbolic planning and verified reasoning \citep{ryu2025clover, xu2026dylos, xu2025aristotle, pei2025fover, singh2026verge, luo2025logicagent, miya2025eidoku}; \citet{amonkar2025realitycheck} show formalization quality degrades with complexity; \citet{chan2026position} argue logical soundness alone is unreliable. Prior studies note high formalization error rates but treat them as quality problems; we show they are \emph{systematically biased} toward the model's answer (Observation~1). This reveals a mechanism underlying \citet{huang2024selfcorrect}'s finding that LLMs cannot self-correct without external feedback: we formalize the failure via the $M{\to}T{\to}(A,C)$ generation structure and provide three lightweight diagnostics that predict failure modes before deployment. Our symbolic confirmation bias (SCB) is distinct from CoT-level confirmation bias \citep{wan2025unveiling, turpin2023language, jhaveri2026failing}: CoT bias concerns trace-level faithfulness, while SCB shows the \emph{collection} of self-extracted constraints mirrors the answer distribution even when individual traces are locally faithful.
11	
12	\looseness=-1
13	\paragraph{Verification and test-time scaling.}
14	Scaling test-time compute via additional traces \citep{snell2025scaling}, structured search \citep{yao2023tree}, or extended reasoning \citep{guo2025deepseekr1, qwen2024qwq} faces the same correlation challenge when traces share a model's biases. Self-verification methods, including multi-agent debate \citep{liang2023encouraging, du2023improving}, self-evaluation \citep{xie2023selfevaluation, weng2023selfverification, madaan2023selfrefine, dhuliawala2023chainofverification}, iterative improvement \citep{shinn2023reflexion, zhou2023lats}, tool-augmented critique \citep{gou2024critic}, formal CoT verification \citep{feng2025vericot, chen2025sets}, and multi-agent verification \citep{lifshitz2025mav}, report gains but none tests self-extracted constraints under formal solvers \citep[cf.][]{kamoi2024selfcorrect}; the bottleneck lies in constraint extraction, not verification (\S\ref{sec:confirmation-bias}). Trained verifiers can escape this bottleneck through external reward signals: outcome and process reward models \citep{cobbe2021gsm8k, lightman2024prm, wang2024mathshepherd}, discriminator-guided decoding \citep{khalifa2023grace}, RL-based self-verification \citep{zeng2025s2r}, dual preference optimization \citep{dupo2025}, and execution-based filtering \citep{li2022alphacode, chen2023codet}. These operate outside Observation~1's pipeline and may overcome the information-theoretic bottleneck. The failure modes differ: SICA's bottleneck is extraction fidelity, whereas PRM/ORM's is reward model generalization \citep{wang2024mathshepherd}.
15	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3d0b4f87-5170-4448-8898-e2c789775308",
  "isSidechain": true,
  "promptId": "88a2bcb6-a784-4ef7-b4e3-429a2c5e0517",
  "agentId": "acc61023d8167708b",
  "type": "user",
  "uuid": "9e91db54-4274-4aa0-8eed-10a24163e593",
  "sourceToolAssistantUUID": "3d0b4f87-5170-4448-8898-e2c789775308",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/director_909d512a",
  "sessionId": "8f3db67b-bd86-4ccb-8f1e-4ba0a20486fe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "humming-wondering-willow"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-26T04:37:05.369Z_

<details open><summary>🔧 Tool call — Read · `toolu_016JUtcj4uAvhAVJ8tx54Vqq`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9e91db54-4274-4aa0-8eed-10a24163e593",
  "isSidechain": true,
  "agentId": "acc61023d8167708b",
  "requestId": "req_011CbQZUGu2dKjqp6orzhQRk",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "b779e693-57e0-4d87-abfa-64f6fcd0e60c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/director_909d512a",
  "sessionId": "8f3db67b-bd86-4ccb-8f1e-4ba0a20486fe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "humming-wondering-willow",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_014CgkU3mcN4nqVmZNQGzXyE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 3121,
      "cache_read_input_tokens": 37507,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3121,
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

_source line 11 · 2026-05-26T04:37:05.381Z_

<details><summary>↩ Tool result · `toolu_016JUtcj4uAvhAVJ8tx54Vqq`</summary>

```text
1	\section{Introduction}\label{sec:introduction}
2	
3	\looseness=-1
4	Self-Consistency (SC) \citep{wang2023sc} selects the majority answer across $K$ chain-of-thought traces, a strategy grounded in the Condorcet Jury Theorem: independent voters converge to truth \citep{condorcet1785, ladha1992correlated}. In practice, SC's gains plateau for strong models \citep{loo2025reevaluating, byerly2025selfconsistency}, and correlated LLM errors \citep{kim2025correlated} reduce the effective ensemble size \citep{dietterich2000ensemble}. A natural remedy is to move beyond simple vote-counting: extract logical constraints from the traces, as in neuro-symbolic approaches \citep{pan2023logiclm, olausson2023linc, ye2024satlm}, and let a provably sound solver adjudicate. If the solver can filter contradictions and enforce logical consistency, it should recover information that raw majority voting discards.
5	
6	\begin{figure*}[t!]
7	\centering
8	\includegraphics[width=0.88\textwidth]{figures/fig1_pipeline_v11.pdf}
9	\caption{The SICA pipeline. SC selects the majority answer from $K$ traces. SICA extracts logical constraints, deduplicates, and solves MAX-SAT via Z3. Red dashed box: the independence bottleneck. Dashed arrow: oracle variant with gold FOL.}
10	\label{fig:pipeline}
11	\end{figure*}
12	
13	\looseness=-1
14	We test this intuition through Symbolic Invariant Consensus Aggregation (SICA), which extracts logical constraints from reasoning traces, deduplicates them, and selects answers via weighted partial MAX-SAT (\S\ref{sec:pipeline}; Figure~\ref{fig:pipeline}). Across six models (7B--32B), four benchmarks, and multi-seed replication, SICA produces answers identical to majority voting on most problems; no condition shows a significant positive effect after FDR control (Table~\ref{tab:main_results}). The failure lies not in the solver but in the constraints it operates on: self-extracted constraints systematically support the model's majority answer, a robust empirical regularity we term \emph{symbolic confirmation bias} (\S\ref{sec:confirmation-bias}), distinct from trace-level unfaithfulness \citep{turpin2023language, wan2025unveiling}. Because each trace determines both an answer and its constraints, the formal verification channel approximately reduces to a weighted echo of the majority vote under the degeneration condition (Observation~1).
15	
16	\looseness=-1
17	This bias is not confined to a single model or task. Symbolic confirmation bias holds across nine models from 7B to frontier scale, and 27 training-free remediation strategies spanning four categories (prompt diversity, constraint filtering, multi-agent debate, and cross-model extraction) all produce neutral-to-negative results (\S\ref{sec:remediation}). A persistent independence--accuracy trade-off emerges: methods that break trace correlation (e.g., multi-agent debate; \citealp{liang2023encouraging, du2023improving}) destroy accuracy, while methods that preserve accuracy fail to achieve independence. Prior work demonstrates that LLMs cannot self-correct reasoning without external feedback \citep{huang2024selfcorrect, kamoi2024selfcorrect}; our analysis provides a concrete mechanism for these findings via the $M{\to}T{\to}(A,C)$ generation structure, where constraints are downstream of the same generative process that produces the answers they are meant to check.
18	
19	\looseness=-1
20	The bottleneck lies in self-extraction itself, not in solver capability or model scale. Cross-architecture verification provides preliminary evidence of escape ($n{=}6$ generator--verifier pairs, exploratory): a structurally independent verifier yields significant gains when it exceeds the generator's accuracy, with benefit governed by a capability-gap pattern between verifier and generator (\S\ref{sec:cross-arch}). This result parallels test-time compute scaling \citep{snell2025scaling}, where additional inference budget faces diminishing returns once effective ensemble diversity saturates. Three lightweight diagnostics derived from a pilot run enable practitioners to predict a priori whether a self-extraction-based aggregation method will improve over SC (\S\ref{sec:diagnostic-framework}).
21	
22	Our contributions are:
23	\begin{enumerate}[nosep,leftmargin=*]
24	\item \textbf{The symbolic mirage.} Provably sound Z3 verification becomes vacuous under self-extraction. We diagnose the underlying mechanism: self-extracted constraints inherit the generating model's distributional prior (symbolic confirmation bias), reducing SICA to majority vote under source-attribution scoring (Observation~1). The pattern holds across nine models and 27 training-free variants (\S\ref{sec:confirmation-bias}, \S\ref{sec:remediation}).
25	
26	\item \textbf{Diagnostic framework.} Three lightweight diagnostics characterize failure modes across all tested conditions within the self-extraction paradigm, with prospective validation on held-out model families; these give practitioners a priori failure-mode diagnosis from a pilot run (\S\ref{sec:diagnostic-framework}).
27	
28	\item \textbf{Cross-architecture escape.} Preliminary evidence ($n{=}6$ generator--verifier pairs) that structurally independent verification can break the bottleneck, with gain governed by an exploratory capability-gap pattern between verifier and generator (\S\ref{sec:cross-arch}).
29	\end{enumerate}
30	
31	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b779e693-57e0-4d87-abfa-64f6fcd0e60c",
  "isSidechain": true,
  "promptId": "88a2bcb6-a784-4ef7-b4e3-429a2c5e0517",
  "agentId": "acc61023d8167708b",
  "type": "user",
  "uuid": "12923a0d-1730-498c-9545-f30063dce239",
  "sourceToolAssistantUUID": "b779e693-57e0-4d87-abfa-64f6fcd0e60c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/director_909d512a",
  "sessionId": "8f3db67b-bd86-4ccb-8f1e-4ba0a20486fe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "humming-wondering-willow"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-26T04:37:05.741Z_

<details open><summary>🔧 Tool call — Read · `toolu_0119Nhm9FZdXaKYWSZ931u18`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex",
  "limit": 1500
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "12923a0d-1730-498c-9545-f30063dce239",
  "isSidechain": true,
  "agentId": "acc61023d8167708b",
  "requestId": "req_011CbQZUGu2dKjqp6orzhQRk",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "406f76a0-7054-47bb-af92-eddb0ceef102",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/director_909d512a",
  "sessionId": "8f3db67b-bd86-4ccb-8f1e-4ba0a20486fe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "humming-wondering-willow",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_014CgkU3mcN4nqVmZNQGzXyE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 3121,
      "cache_read_input_tokens": 37507,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3121,
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

_source line 13 · 2026-05-26T04:37:06.031Z_

<details><summary>↩ Tool result · reported error · `toolu_0119Nhm9FZdXaKYWSZ931u18`</summary>

```text
File content (38661 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "406f76a0-7054-47bb-af92-eddb0ceef102",
  "isSidechain": true,
  "promptId": "88a2bcb6-a784-4ef7-b4e3-429a2c5e0517",
  "agentId": "acc61023d8167708b",
  "type": "user",
  "uuid": "a9b2088a-8e4e-43bb-b1c7-b2c2e683825b",
  "toolUseResult": "Error: File content (38661 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.",
  "sourceToolAssistantUUID": "406f76a0-7054-47bb-af92-eddb0ceef102",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/director_909d512a",
  "sessionId": "8f3db67b-bd86-4ccb-8f1e-4ba0a20486fe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "humming-wondering-willow"
}
```

</details>

---

### Assistant

_source line 14 · 2026-05-26T04:37:07.924Z_

Now let me search for specific line numbers in the appendix that contain the citation:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a9b2088a-8e4e-43bb-b1c7-b2c2e683825b",
  "isSidechain": true,
  "agentId": "acc61023d8167708b",
  "requestId": "req_011CbQZUX6JTGLpg5hU1JU6d",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "449b7518-212a-430e-b8fc-028810e9ddc9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/director_909d512a",
  "sessionId": "8f3db67b-bd86-4ccb-8f1e-4ba0a20486fe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "humming-wondering-willow",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01TfCxfeEHA7rtpRY67E6EPx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 3034,
      "cache_read_input_tokens": 40628,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3034,
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

_source line 15 · 2026-05-26T04:37:09.017Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01G31Rgucyd7VGcQD4GHG1no`</summary>

```json
{
  "command": "grep -n \"pan2023logiclm\" /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "449b7518-212a-430e-b8fc-028810e9ddc9",
  "isSidechain": true,
  "agentId": "acc61023d8167708b",
  "requestId": "req_011CbQZUX6JTGLpg5hU1JU6d",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "a6730188-cff1-48c4-b888-7e08066efe2c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/director_909d512a",
  "sessionId": "8f3db67b-bd86-4ccb-8f1e-4ba0a20486fe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "humming-wondering-willow",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01TfCxfeEHA7rtpRY67E6EPx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 3034,
      "cache_read_input_tokens": 40628,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3034,
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

_source line 16 · 2026-05-26T04:37:09.076Z_

<details><summary>↩ Tool result · `toolu_01G31Rgucyd7VGcQD4GHG1no`</summary>

```text
1479:Our results do not imply that neuro-symbolic methods are inherently flawed; they imply that \emph{self-extracted} constraints cannot provide independent verification. The key distinction is \emph{when} formalization occurs relative to answer generation. Specification-generation approaches (e.g., SatLM \citep{ye2024satlm}, Logic-LM \citep{pan2023logiclm}) formalize the problem \emph{before} generating candidate answers, avoiding the extraction bottleneck; SatLM's success confirms that the formal verification mechanism is sound when constraints are independently derived. Trace-extraction (this work) operates post-hoc on reasoning traces that already contain candidates, inheriting the distributional prior that generates SCB. When post-hoc verification is unavoidable, practitioners should employ external verifiers from a different architecture family (\S\ref{sec:cross-arch}) and use the diagnostic framework in \S\ref{sec:discussion} to assess feasibility before deployment. The SCB diagnostic toolkit (below) provides detailed computation methods and threshold recommendations.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a6730188-cff1-48c4-b888-7e08066efe2c",
  "isSidechain": true,
  "promptId": "88a2bcb6-a784-4ef7-b4e3-429a2c5e0517",
  "agentId": "acc61023d8167708b",
  "type": "user",
  "uuid": "5401a23c-a9bc-41e9-9b70-77c047c9a5e8",
  "sourceToolAssistantUUID": "a6730188-cff1-48c4-b888-7e08066efe2c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/director_909d512a",
  "sessionId": "8f3db67b-bd86-4ccb-8f1e-4ba0a20486fe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "humming-wondering-willow"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-26T04:37:09.131Z_

<details open><summary>🔧 Tool call — Bash · `toolu_011pK266MNZoXXyNfCd59pRc`</summary>

```json
{
  "command": "grep -n \"pan2023logiclm\" /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5401a23c-a9bc-41e9-9b70-77c047c9a5e8",
  "isSidechain": true,
  "agentId": "acc61023d8167708b",
  "requestId": "req_011CbQZUX6JTGLpg5hU1JU6d",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "6153d882-bac4-4ea8-9b58-08d0630db399",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/director_909d512a",
  "sessionId": "8f3db67b-bd86-4ccb-8f1e-4ba0a20486fe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "humming-wondering-willow",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01TfCxfeEHA7rtpRY67E6EPx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 3034,
      "cache_read_input_tokens": 40628,
      "output_tokens": 200,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3034
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 200,
          "cache_read_input_tokens": 40628,
          "cache_creation_input_tokens": 3034,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3034,
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

_source line 18 · 2026-05-26T04:37:09.196Z_

<details><summary>↩ Tool result · `toolu_011pK266MNZoXXyNfCd59pRc`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex:1479:Our results do not imply that neuro-symbolic methods are inherently flawed; they imply that \emph{self-extracted} constraints cannot provide independent verification. The key distinction is \emph{when} formalization occurs relative to answer generation. Specification-generation approaches (e.g., SatLM \citep{ye2024satlm}, Logic-LM \citep{pan2023logiclm}) formalize the problem \emph{before} generating candidate answers, avoiding the extraction bottleneck; SatLM's success confirms that the formal verification mechanism is sound when constraints are independently derived. Trace-extraction (this work) operates post-hoc on reasoning traces that already contain candidates, inheriting the distributional prior that generates SCB. When post-hoc verification is unavoidable, practitioners should employ external verifiers from a different architecture family (\S\ref{sec:cross-arch}) and use the diagnostic framework in \S\ref{sec:discussion} to assess feasibility before deployment. The SCB diagnostic toolkit (below) provides detailed computation methods and threshold recommendations.
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/introduction.tex:4:Self-Consistency (SC) \citep{wang2023sc} selects the majority answer across $K$ chain-of-thought traces, a strategy grounded in the Condorcet Jury Theorem: independent voters converge to truth \citep{condorcet1785, ladha1992correlated}. In practice, SC's gains plateau for strong models \citep{loo2025reevaluating, byerly2025selfconsistency}, and correlated LLM errors \citep{kim2025correlated} reduce the effective ensemble size \citep{dietterich2000ensemble}. A natural remedy is to move beyond simple vote-counting: extract logical constraints from the traces, as in neuro-symbolic approaches \citep{pan2023logiclm, olausson2023linc, ye2024satlm}, and let a provably sound solver adjudicate. If the solver can filter contradictions and enforce logical consistency, it should recover information that raw majority voting discards.
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/related_work.tex:10:Three paradigms exist: \emph{specification-generation} \citep{pan2023logiclm, olausson2023linc, ye2024satlm} and \emph{program-generation} \citep{gao2023pal, chen2023program, lyu2023faithful} formalize before answer generation; \emph{trace-extraction} (this work) operates post-hoc, inheriting confirmation bias (\S\ref{sec:confirmation-bias}). Recent work extends symbolic planning and verified reasoning \citep{ryu2025clover, xu2026dylos, xu2025aristotle, pei2025fover, singh2026verge, luo2025logicagent, miya2025eidoku}; \citet{amonkar2025realitycheck} show formalization quality degrades with complexity; \citet{chan2026position} argue logical soundness alone is unreliable. Prior studies note high formalization error rates but treat them as quality problems; we show they are \emph{systematically biased} toward the model's answer (Observation~1). This reveals a mechanism underlying \citet{huang2024selfcorrect}'s finding that LLMs cannot self-correct without external feedback: we formalize the failure via the $M{\to}T{\to}(A,C)$ generation structure and provide three lightweight diagnostics that predict failure modes before deployment. Our symbolic confirmation bias (SCB) is distinct from CoT-level confirmation bias \citep{wan2025unveiling, turpin2023language, jhaveri2026failing}: CoT bias concerns trace-level faithfulness, while SCB shows the \emph{collection} of self-extracted constraints mirrors the answer distribution even when individual traces are locally faithful.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6153d882-bac4-4ea8-9b58-08d0630db399",
  "isSidechain": true,
  "promptId": "88a2bcb6-a784-4ef7-b4e3-429a2c5e0517",
  "agentId": "acc61023d8167708b",
  "type": "user",
  "uuid": "c892a777-1525-459c-9199-4142270c6eb4",
  "sourceToolAssistantUUID": "6153d882-bac4-4ea8-9b58-08d0630db399",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/director_909d512a",
  "sessionId": "8f3db67b-bd86-4ccb-8f1e-4ba0a20486fe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "humming-wondering-willow"
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-26T04:37:10.818Z_

Perfect! Now let me verify the BibTeX entry itself:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c892a777-1525-459c-9199-4142270c6eb4",
  "isSidechain": true,
  "agentId": "acc61023d8167708b",
  "requestId": "req_011CbQZUjeMbFLGSy8Lhy3Cn",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "cf4fd685-65fd-4c9e-a652-fef23a8de150",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/director_909d512a",
  "sessionId": "8f3db67b-bd86-4ccb-8f1e-4ba0a20486fe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "humming-wondering-willow",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01R9fvDJSrfs7e3C3L8DF5VY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 1493,
      "cache_read_input_tokens": 43662,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1493,
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

_source line 20 · 2026-05-26T04:37:11.128Z_

<details open><summary>🔧 Tool call — Read · `toolu_01LGsoAL4oRtxPayVbnNsTnC`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/references.bib",
  "offset": 110,
  "limit": 15
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cf4fd685-65fd-4c9e-a652-fef23a8de150",
  "isSidechain": true,
  "agentId": "acc61023d8167708b",
  "requestId": "req_011CbQZUjeMbFLGSy8Lhy3Cn",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "0a664e6a-f92a-42eb-a866-ec8a5a924d1e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/director_909d512a",
  "sessionId": "8f3db67b-bd86-4ccb-8f1e-4ba0a20486fe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "humming-wondering-willow",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01R9fvDJSrfs7e3C3L8DF5VY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 1493,
      "cache_read_input_tokens": 43662,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1493,
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

_source line 21 · 2026-05-26T04:37:11.143Z_

<details><summary>↩ Tool result · `toolu_01LGsoAL4oRtxPayVbnNsTnC`</summary>

```text
110	}
111	
112	%%% Neuro-Symbolic Reasoning %%%
113	
114	@inproceedings{pan2023logiclm,
115	  title={Logic-{LM}: Empowering Large Language Models with Symbolic Solvers for Faithful Logical Reasoning},
116	  author={Pan, Liangming and Alber, Alon and Xu, Wenhu and Deng, Yixin and Chen, Huan and Ji, Heng},
117	  booktitle={EMNLP Findings},
118	  year={2023}
119	}
120	
121	@inproceedings{olausson2023linc,
122	  title={{LINC}: A Neurosymbolic Approach for Logical Reasoning by Combining Language Models with First-Order Logic Provers},
123	  author={Olausson, Theo X. and Gu, Alex and Lipkin, Benjamin and Zhang, Cedegao E. and Solar-Lezama, Armando and Tenenbaum, Joshua B. and Levy, Roger},
124	  booktitle={EMNLP},
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0a664e6a-f92a-42eb-a866-ec8a5a924d1e",
  "isSidechain": true,
  "promptId": "88a2bcb6-a784-4ef7-b4e3-429a2c5e0517",
  "agentId": "acc61023d8167708b",
  "type": "user",
  "uuid": "abf88d89-124a-4c58-9f14-1728ce05280c",
  "sourceToolAssistantUUID": "0a664e6a-f92a-42eb-a866-ec8a5a924d1e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/director_909d512a",
  "sessionId": "8f3db67b-bd86-4ccb-8f1e-4ba0a20486fe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "humming-wondering-willow"
}
```

</details>

---

### Assistant

_source line 22 · 2026-05-26T04:37:15.744Z_

Excellent! I've found all the in-text citations and the BibTeX entry. Here's my report:

## Summary

I found **three in-text citations** of `pan2023logiclm` in the paper:

1. **introduction.tex (line 4)**: `\citep{pan2023logiclm, olausson2023linc, ye2024satlm}` - cited as an example of neuro-symbolic approaches for constraint extraction
2. **related_work.tex (line 10)**: `\citep{pan2023logiclm, olausson2023linc, ye2024satlm}` - cited as a "specification-generation" paradigm example
3. **appendix.tex (line 1479)**: `\citep{pan2023logiclm}` - cited as Logic-LM example of specification-generation approaches

## BibTeX Entry Status

The current BibTeX entry in `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/references.bib` (lines 114-119) contains the **incorrect author list**:

```bibtex
@inproceedings{pan2023logiclm,
  title={Logic-{LM}: Empowering Large Language Models with Symbolic Solvers for Faithful Logical Reasoning},
  author={Pan, Liangming and Alber, Alon and Xu, Wenhu and Deng, Yixin and Chen, Huan and Ji, Heng},
  booktitle={EMNLP Findings},
  year={2023}
}
```

As you noted, the errors are:
- "Alber, Alon" should be "Albalak, Alon"
- "Xu, Wenhu" should be "Wang, Xinyi"
- "Deng, Yixin and Chen, Huan and Ji, Heng" should be replaced with "Wang, William Yang"

The correct author list according to ACL Anthology should be: **Liangming Pan, Alon Albalak, Xinyi Wang, William Yang Wang**

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "abf88d89-124a-4c58-9f14-1728ce05280c",
  "isSidechain": true,
  "agentId": "acc61023d8167708b",
  "requestId": "req_011CbQZUtApXqYmJdsEtrMP9",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "a4395147-8c11-4d9c-9e33-e417cb3b607f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/director_909d512a",
  "sessionId": "8f3db67b-bd86-4ccb-8f1e-4ba0a20486fe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "humming-wondering-willow",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01CNhZyMypQ3zLUpEErA4ULx",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 437,
      "cache_read_input_tokens": 45155,
      "output_tokens": 521,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 437
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 521,
          "cache_read_input_tokens": 45155,
          "cache_creation_input_tokens": 437,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 437,
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
