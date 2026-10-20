# Research conversation: I need to find two things in the paper at /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/d

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 22
- **Recorded user turns:** 1
- **Tool calls:** 7
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a217013802bf0fe69.jsonl`
- **Structured JSON:** [`10d3b1ec6d76702d4fba.json`](../../sessions/10/10d3b1ec6d76702d4fba.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

22 recorded events

### User

_source line 1 · 2026-05-22T05:42:22.245Z_

I need to find two things in the paper at /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/:

1. The exact content of §5.5 "Multi-LLM Validation" or similar section in the main .tex files. Search for "multilm" or "Multi-LLM" or "open.source" patterns across all .tex files.

2. The appendix structure — specifically what sections exist in appendix.tex, especially around "multilm_opensource" label, and the last appendix section (so I know where to add a new one).

Read the relevant sections fully. For the main text §5.5, I need the complete section content. For the appendix, I need to see the section near "multilm_opensource" and the very end of the file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "410c5182-a00d-45c3-a02c-4785eb40bb89",
  "agentId": "a217013802bf0fe69",
  "type": "user",
  "uuid": "5ac24874-7890-401c-b242-5e450d895ab1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/paper_agent_8babce27",
  "sessionId": "6ae78efb-2b23-4404-a761-5afc621a128d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "zazzy-giggling-simon"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-22T05:42:24.703Z_

I'll help you find these two things. Let me start by searching for the Multi-LLM related content and exploring the paper structure.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5ac24874-7890-401c-b242-5e450d895ab1",
  "isSidechain": true,
  "agentId": "a217013802bf0fe69",
  "requestId": "req_011CbH5DXGm7QP7iANijnZXD",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d29d9b59-430a-4c03-a655-742a73a4e7b2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/paper_agent_8babce27",
  "sessionId": "6ae78efb-2b23-4404-a761-5afc621a128d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "zazzy-giggling-simon",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Y4VAJQpBjXmTmJG6MJzbeZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 27803,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 27803,
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

_source line 3 · 2026-05-22T05:42:24.854Z_

<details open><summary>🔧 Tool call — Glob · `toolu_016wzs63gTet9Rii413VppYD`</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d29d9b59-430a-4c03-a655-742a73a4e7b2",
  "isSidechain": true,
  "agentId": "a217013802bf0fe69",
  "requestId": "req_011CbH5DXGm7QP7iANijnZXD",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "6017db3f-8517-410f-bfca-30d33db85e1f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/paper_agent_8babce27",
  "sessionId": "6ae78efb-2b23-4404-a761-5afc621a128d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "zazzy-giggling-simon",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Y4VAJQpBjXmTmJG6MJzbeZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 27803,
      "cache_read_input_tokens": 0,
      "output_tokens": 116,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 27803
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 116,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 27803,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 27803,
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

_source line 4 · 2026-05-22T05:42:24.874Z_

<details><summary>↩ Tool result · `toolu_016wzs63gTet9Rii413VppYD`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/theory.tex
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/checklist.tex
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6017db3f-8517-410f-bfca-30d33db85e1f",
  "isSidechain": true,
  "promptId": "410c5182-a00d-45c3-a02c-4785eb40bb89",
  "agentId": "a217013802bf0fe69",
  "type": "user",
  "uuid": "23d54ffd-3572-4146-9bd2-1b276ac49780",
  "sourceToolAssistantUUID": "6017db3f-8517-410f-bfca-30d33db85e1f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/paper_agent_8babce27",
  "sessionId": "6ae78efb-2b23-4404-a761-5afc621a128d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "zazzy-giggling-simon"
}
```

</details>

---

### Assistant

_source line 5 · 2026-05-22T05:42:26.845Z_

Now let me search for the Multi-LLM content in the .tex files:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "23d54ffd-3572-4146-9bd2-1b276ac49780",
  "isSidechain": true,
  "agentId": "a217013802bf0fe69",
  "requestId": "req_011CbH5DiZfWiFvs8s2GbW2Q",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "7410a09d-4813-4919-8552-b6f6ff83c609",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/paper_agent_8babce27",
  "sessionId": "6ae78efb-2b23-4404-a761-5afc621a128d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "zazzy-giggling-simon",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01CqT85mZbsEWYsXmNfQoYjW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1383,
      "cache_read_input_tokens": 27803,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1383,
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

_source line 6 · 2026-05-22T05:42:27.646Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01Dj3q5AkMUdkryXEsmHHjjC`</summary>

```json
{
  "pattern": "(?i)(multi.llm|multilm|open.source)",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7410a09d-4813-4919-8552-b6f6ff83c609",
  "isSidechain": true,
  "agentId": "a217013802bf0fe69",
  "requestId": "req_011CbH5DiZfWiFvs8s2GbW2Q",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "48f7d8ed-78e1-4d8f-9670-ebc3d0e7a817",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/paper_agent_8babce27",
  "sessionId": "6ae78efb-2b23-4404-a761-5afc621a128d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "zazzy-giggling-simon",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01CqT85mZbsEWYsXmNfQoYjW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1383,
      "cache_read_input_tokens": 27803,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1383,
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

_source line 7 · 2026-05-22T05:42:27.704Z_

<details><summary>↩ Tool result · `toolu_01Dj3q5AkMUdkryXEsmHHjjC`</summary>

```text
Found 8 files
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/main.aux
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/checklist.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "48f7d8ed-78e1-4d8f-9670-ebc3d0e7a817",
  "isSidechain": true,
  "promptId": "410c5182-a00d-45c3-a02c-4785eb40bb89",
  "agentId": "a217013802bf0fe69",
  "type": "user",
  "uuid": "fdc68af8-1a82-4b5d-986f-511c144f6578",
  "sourceToolAssistantUUID": "48f7d8ed-78e1-4d8f-9670-ebc3d0e7a817",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/paper_agent_8babce27",
  "sessionId": "6ae78efb-2b23-4404-a761-5afc621a128d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "zazzy-giggling-simon"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-22T05:42:28.251Z_

<details open><summary>🔧 Tool call — Read · `toolu_015SJzGdu8T5gZmf7ULtg7KL`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fdc68af8-1a82-4b5d-986f-511c144f6578",
  "isSidechain": true,
  "agentId": "a217013802bf0fe69",
  "requestId": "req_011CbH5DiZfWiFvs8s2GbW2Q",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "66569921-b021-4e63-b34f-5a57ace8a070",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/paper_agent_8babce27",
  "sessionId": "6ae78efb-2b23-4404-a761-5afc621a128d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "zazzy-giggling-simon",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01CqT85mZbsEWYsXmNfQoYjW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1383,
      "cache_read_input_tokens": 27803,
      "output_tokens": 229,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1383
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 229,
          "cache_read_input_tokens": 27803,
          "cache_creation_input_tokens": 1383,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1383,
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

_source line 9 · 2026-05-22T05:42:28.513Z_

<details><summary>↩ Tool result · `toolu_015SJzGdu8T5gZmf7ULtg7KL`</summary>

```text
1	\section{EC-HTE Procedure}
2	\label{app:algorithm}
3	
4	\begin{algorithm}[t]
5	\caption{EC-HTE: Error-Corrected Heterogeneous Treatment Effects}
6	\label{alg:echte}
7	\begin{algorithmic}[1]
8	\Require Observations $\{(Y_i, W_i, \hat{Z}_i, X_i)\}_{i=1}^N$; expert labels $\{Z_j^*\}_{j=1}^{n_{\text{expert}}}$; subgroup map $S: \mathcal{X} \to \{1,\ldots,K\}$
9	\Ensure Corrected CATE estimates $\hat{\tau}(z)$ with variance-adjusted CIs
10	\Statex
11	\State \textbf{Step 1: Estimate per-subgroup confusion matrices (HB)}
12	\For{$s = 1, \ldots, K$}
13	    \State $C_s[j,\cdot] \sim \mathrm{Dir}(\alpha_0 \cdot \mathbf{e}_j)$, \; $\alpha_0 \sim \mathrm{Gamma}(3,1)$
14	    \State Gibbs sampler (4 chains, 4000 iter) on $\{(\hat{Z}_j, Z_j^*) : S_j = s\}$
15	    \State $\hat{C}_s \gets$ posterior mean; verify $\hat{R} < 1.01$
16	\EndFor
17	\Statex
18	\State \textbf{Step 2: Correct observed outcome moments}
19	\For{$s = 1, \ldots, K$}
20	    \If{$\kappa(\hat{C}_s) > 100$} $\hat{C}_s \gets \bar{C}$ \Comment{singularity guard}
21	    \EndIf
22	    \State $\tilde{\boldsymbol{\mu}}_s \gets \hat{C}_s^{-1} \hat{\boldsymbol{\mu}}_s$
23	\EndFor
24	\Statex
25	\State \textbf{Step 3: CausalForestDML with variance-adjusted SEs}
26	\State Train CausalForest (honest splitting) on corrected labels
27	\State $\mathrm{se}_{\mathrm{adj},i} \gets \sqrt{\mathrm{diag}(\hat{C}_{S_i}^{-1}\, \mathrm{diag}(\mathrm{se}_i^2)\, \hat{C}_{S_i}^{-\top})}$
28	\State \Return $\hat{\tau}(z)$ with 95\% CIs from $\mathrm{se}_{\mathrm{adj}}$
29	\end{algorithmic}
30	\end{algorithm}
31	
32	\section{Full Proof of Theorem~\ref{thm:bias_identity}}
33	\label{app:derivation}
34	
35	\paragraph{Setup.}
36	Under assumptions (A1)--(A4), the observed CATE in subgroup $s$ at effect-modifier level $z$ is
37	\begin{equation}
38	\tau_{\text{obs}}(z, s) = \sum_{z'} M_s[z, z'] \cdot \tau(z'),
39	\end{equation}
40	where $M_s[z, z'] = P(Z{=}z' \mid \hat{Z}{=}z, S{=}s)$ is the mixing matrix.
41	Under (A2)--(A3), $M_s = \bigl[\begin{smallmatrix} 1-\pi_s & \pi_s \\ \pi_s & 1-\pi_s \end{smallmatrix}\bigr]$.
42	
43	\paragraph{Global correction.}
44	The pooled mixing matrix is $M_{\text{global}} = \sum_s w_s M_s = \bigl[\begin{smallmatrix} 1-\bar{\pi} & \bar{\pi} \\ \bar{\pi} & 1-\bar{\pi} \end{smallmatrix}\bigr]$, with $\bar{\pi} = \sum_s w_s \pi_s$.
45	
46	Global correction applies $M_{\text{global}}^{-1}$ to $\tau_{\text{obs}}(\cdot, s)$:
47	\begin{equation}
48	\hat{\tau}_{\text{global}}(z, s) = [M_{\text{global}}^{-1} M_s \cdot \boldsymbol{\tau}]_z,
49	\end{equation}
50	where $\boldsymbol{\tau} = [\tau(0), \tau(1)]^\top$.
51	
52	\paragraph{Bias computation.}
53	The bias is $\hat{\tau}_{\text{global}}(z, s) - \tau(z) = [(M_{\text{global}}^{-1} M_s - I) \boldsymbol{\tau}]_z$.
54	
55	Direct computation gives:
56	\begin{equation}
57	M_{\text{global}}^{-1} = \frac{1}{1 - 2\bar{\pi}} \begin{bmatrix} 1-\bar{\pi} & -\bar{\pi} \\ -\bar{\pi} & 1-\bar{\pi} \end{bmatrix}.
58	\end{equation}
59	Multiplying by $M_s$:
60	\begin{equation}
61	\resizebox{.88\columnwidth}{!}{$\displaystyle
62	M_{\text{global}}^{-1} M_s = \frac{1}{1-2\bar{\pi}} \begin{bmatrix} (1{-}\bar{\pi})(1{-}\pi_s) - \bar{\pi}\pi_s & (1{-}\bar{\pi})\pi_s - \bar{\pi}(1{-}\pi_s) \\ -\bar{\pi}(1{-}\pi_s) + (1{-}\bar{\pi})\pi_s & -\bar{\pi}\pi_s + (1{-}\bar{\pi})(1{-}\pi_s) \end{bmatrix}.
63	$}
64	\end{equation}
65	
66	Define $\delta_s = \pi_s - \bar{\pi}$. The $(1,1)$ entry simplifies:
67	{\small
68	\begin{align}
69	(1{-}\bar{\pi})(1{-}\pi_s) - \bar{\pi}\pi_s &= 1 - \bar{\pi} - \pi_s + 2\bar{\pi}\pi_s \nonumber\\
70	&= (1 - 2\bar{\pi}) + (\bar{\pi} - \pi_s) + 2\bar{\pi}\pi_s \nonumber\\
71	&= (1 - 2\bar{\pi}) - \delta_s.
72	\end{align}
73	}
74	
75	More directly, substituting $\pi_s = \bar{\pi} + \delta_s$:
76	\begin{equation}
77	M_{\text{global}}^{-1} M_s - I = \frac{\delta_s}{1-2\bar{\pi}} \begin{bmatrix} -1 & 1 \\ 1 & -1 \end{bmatrix}.
78	\end{equation}
79	
80	To verify: the $(1,1)$ entry of $M_{\text{global}}^{-1} M_s$ is
81	{\small
82	\begin{align}
83	&\frac{(1{-}\bar{\pi})(1{-}\bar{\pi}{-}\delta_s) - \bar{\pi}(\bar{\pi}{+}\delta_s)}{1-2\bar{\pi}} \nonumber\\
84	&= \frac{(1{-}\bar{\pi})^2 - (1{-}\bar{\pi})\delta_s - \bar{\pi}^2 - \bar{\pi}\delta_s}{1-2\bar{\pi}} \nonumber\\
85	&= \frac{1 - 2\bar{\pi} - \delta_s}{1-2\bar{\pi}} = 1 - \frac{\delta_s}{1-2\bar{\pi}}.
86	\end{align}
87	}
88	
89	Applying $(M_{\text{global}}^{-1} M_s - I)$ to $\boldsymbol{\tau}$:
90	{\small
91	\begin{align}
92	\text{bias}(z{=}0, s) &= \tfrac{\delta_s}{1-2\bar{\pi}}(-\tau(0) + \tau(1)) = +\tfrac{\delta_s \cdot \Delta\tau}{1-2\bar{\pi}}, \\
93	\text{bias}(z{=}1, s) &= \tfrac{\delta_s}{1-2\bar{\pi}}(\tau(0) - \tau(1)) = -\tfrac{\delta_s \cdot \Delta\tau}{1-2\bar{\pi}},
94	\end{align}
95	}
96	where $\Delta\tau = \tau(1) - \tau(0)$. \qed
97	
98	\section{Multi-class Extension and Proof}
99	\label{app:multiclass}
100	
101	\begin{corollary}[Multi-class Extension]
102	\label{cor:multiclass}
103	For $K > 2$ subgroups with $J$ effect-modifier levels, the subgroup bias of global correction generalizes to
104	\begin{equation}
105	\mathrm{bias}_{\mathrm{global}}(z, s) = \sum_{j=1}^{J} \bigl(\bar{\pi}_j - \pi_{s,j}\bigr) \cdot \bigl(\tau(j) - \bar{\tau}\bigr) \cdot g(\bar{\pi}),
106	\label{eq:multiclass}
107	\end{equation}
108	where $g(\bar{\pi})$ collects the matrix-inversion amplification terms.\footnote{For $J=3$ with symmetric misclassification (off-diagonal errors uniform), $g(\bar{\pi}) = 1/(1 - 3\bar{\pi}/2)$, generalizing the $J{=}2$ factor $1/(1-2\bar{\pi})$. In general, $g(\bar{\pi}) = 1/(1 - J\bar{\pi}/(J-1))$.}
109	The essential structure, $\sum_s w_s (\bar{\pi}_j - \pi_{s,j}) = 0$, ensures that bias redistributes across subgroups rather than vanishing in aggregate.
110	\end{corollary}
111	
112	\paragraph{Proof.}
113	For $K > 2$ subgroups with $J$ effect-modifier levels, the subgroup-specific mixing matrix $M_s$ is $J \times J$ with entries $M_s[j, j'] = P(Z{=}j' \mid \hat{Z}{=}j, S{=}s)$.
114	The global mixing matrix is $M_{\text{global}} = \sum_s w_s M_s$.
115	
116	The bias of global correction in subgroup $s$ at level $z$ is:
117	\begin{equation}
118	\text{bias}_{\text{global}}(z, s) = [(M_{\text{global}}^{-1} M_s - I) \boldsymbol{\tau}]_z.
119	\end{equation}
120	
121	Write $M_s = M_{\text{global}} + \Delta_s$ where $\Delta_s = M_s - M_{\text{global}}$ satisfies $\sum_s w_s \Delta_s = 0$.
122	Then $M_{\text{global}}^{-1} M_s = I + M_{\text{global}}^{-1} \Delta_s$, so:
123	\begin{equation}
124	\text{bias}_{\text{global}}(z, s) = [M_{\text{global}}^{-1} \Delta_s \cdot \boldsymbol{\tau}]_z.
125	\end{equation}
126	
127	For symmetric misclassification with per-class error rates $\pi_{s,j}$ and pooled rates $\bar{\pi}_j$, the entries of $\Delta_s$ have the form $\Delta_s[j,j'] = (\bar{\pi}_j - \pi_{s,j}) \cdot h(j, j')$ for a function $h$ determined by the off-diagonal redistribution pattern.
128	Expanding the matrix-vector product and collecting terms yields:
129	\begin{equation}
130	\text{bias}_{\text{global}}(z, s) = \sum_{j=1}^{J} (\bar{\pi}_j - \pi_{s,j}) \cdot (\tau(j) - \bar{\tau}) \cdot g(\bar{\pi}),
131	\end{equation}
132	where $g(\bar{\pi})$ collects the matrix-inversion amplification terms and $\bar{\tau} = \sum_j P(Z{=}j) \tau(j)$.
133	
134	The essential structure $\sum_s w_s (\bar{\pi}_j - \pi_{s,j}) = 0$ ensures that the weighted bias across subgroups sums to zero: global correction redistributes bias rather than creating or eliminating it in aggregate. \qed
135	
136	\section{Proof of Proposition~\ref{prop:debiasing_hurts}}
137	\label{app:debiasing_hurts}
138	
139	The naive estimator has bias $\tau_{\text{obs}}(z,s) - \tau(z)$.
140	Under (A2)--(A3), $\tau_{\text{obs}}(0,s) = (1-\pi_s)\tau(0) + \pi_s\tau(1)$, so $\text{bias}_{\text{naive}}(0,s) = \pi_s \cdot \Delta\tau$.
141	
142	Global correction produces larger absolute bias when $|\text{bias}_{\text{global}}(0,s)| > |\text{bias}_{\text{naive}}(0,s)|$:
143	\begin{equation}
144	\frac{|\delta_s| \cdot |\Delta\tau|}{|1-2\bar{\pi}|} > \pi_s \cdot |\Delta\tau|.
145	\end{equation}
146	Since $\Delta\tau \neq 0$ (otherwise both biases are zero), dividing through gives:
147	\begin{equation}
148	\frac{|\delta_s|}{(1-2\bar{\pi}) \cdot \pi_s} > 1,
149	\end{equation}
150	where we use $1-2\bar{\pi} > 0$ from (A4).
151	
152	For high-error subgroups ($\pi_s > \bar{\pi}$, so $\delta_s > 0$): the condition becomes $(\pi_s - \bar{\pi}) / ((1-2\bar{\pi})\pi_s) > 1$, which simplifies to $\pi_s(1 - 1 + 2\bar{\pi}) > \bar{\pi}$, i.e., $2\bar{\pi}\pi_s > \bar{\pi}$, i.e., $\pi_s > 0.5$.
153	This is excluded by (A4), so global correction always reduces bias in high-error subgroups.
154	
155	For low-error subgroups ($\pi_s < \bar{\pi}$, so $\delta_s < 0$): the condition becomes $(\bar{\pi} - \pi_s) / ((1-2\bar{\pi})\pi_s) > 1$, which gives $\pi_s < \bar{\pi} / (1 - 2\bar{\pi} + 1) = \bar{\pi} / (2(1-\bar{\pi}))$.
156	When $\bar{\pi} = 0.15$, any subgroup with $\pi_s < 0.088$ experiences increased bias from global correction. \qed
157	
158	\section{Semi-Synthetic Data Generating Process}
159	\label{app:dgp}
160	
161	\paragraph{Synthetic DGP (Sections~\ref{sec:bias_mechanism}--\ref{sec:diagnostic} and Appendix~\ref{sec:budget}).}
162	We generate $N = 5000$ observations.
163	Each observation belongs to one of $K \in \{2, 4\}$ subgroups $S \in \{1, \ldots, K\}$ with equal weights $w_s = 1/K$.
164	The binary effect modifier $Z \in \{0, 1\}$ is drawn with $P(Z{=}1) = 0.5$.
165	Treatment assignment is $T \sim \text{Bernoulli}(0.5)$, independent of $Z$ and $S$.
166	
167	The outcome is generated as:
168	\begin{equation}
169	Y = \tau(Z) \cdot T + \varepsilon, \quad \varepsilon \sim \mathcal{N}(0, 1),
170	\end{equation}
171	where the CATE function is $\tau(z) = \bar{\tau} + \Delta\tau \cdot (z - 0.5)$ with $\bar{\tau} = 0.5$.
172	The CATE heterogeneity $\Delta\tau \in \{0, 0.2, 0.5, 1.0\}$ controls the strength of treatment effect variation across levels of $Z$.
173	
174	Misclassification is symmetric: $\hat{Z} \neq Z$ with probability $\pi_s$ depending on subgroup.
175	For $K{=}2$: $\pi_1 = \bar{\pi} - \Delta_c/2$, $\pi_2 = \bar{\pi} + \Delta_c/2$, with $\bar{\pi} \in \{0.1, 0.2\}$ and $\Delta_c \in \{0, 0.05, 0.1, 0.15\}$.
176	For $K{=}4$, extreme regime: $\pi \in \{0.05, 0.10, 0.15, 0.25\}$; moderate regime: $\pi \in \{0.08, 0.12, 0.16, 0.20\}$.
177	
178	Expert labels are drawn as a simple random sample of size $n_{\text{expert}} \in \{50, 100, 250, 500, 1000, 2000\}$ from the full dataset, with true $Z$ observed for these observations.
179	
180	\paragraph{Semi-synthetic DGP (Section~\ref{sec:ec_hte_eval}).}
181	We sample $N = 5000$ tweets from the TweetEval sentiment corpus ($N_{\text{pool}} = 57{,}899$).
182	Subgroups are defined by crossing \texttt{has\_hashtag} $\times$ \texttt{text\_length\_bin} (short/medium/long), yielding $K = 4$ subgroups with empirical sizes: $S_0 \approx 38\%$, $S_1 \approx 38\%$, $S_2 \approx 12\%$, $S_3 \approx 12\%$.
183	Misclassification rates in the extreme regime are $\pi_{S_0} = 0.05$, $\pi_{S_1} = 0.10$, $\pi_{S_2} = 0.15$, $\pi_{S_3} = 0.25$, reflecting empirical evidence that hashtag-heavy text degrades LLM classifier accuracy.
184	The outcome DGP follows the same structure as the synthetic case, with CATE injected onto the real text-derived subgroup structure.
185	
186	\paragraph{PPCI DGPs (Appendix~\ref{sec:ppci}).}
187	Four DGPs isolate error types: (A) covariate error only ($\sigma_{\text{outcome}} = 0$), (B) outcome error only ($\sigma_{\text{outcome}} = 0.5$), (C) both errors ($\sigma_{\text{outcome}} = 0.5$), (D) no error ($\sigma_{\text{outcome}} = 0$).
188	Outcome-side error is additive Gaussian noise on $Y$.
189	
190	\section{Extended Related Work}
191	\label{app:related}
192	
193	\paragraph{Measurement error details.}
194	\citet{fuller1987measurement} establish the foundational theory showing that naive regression with mismeasured covariates yields attenuated coefficient estimates.
195	\citet{carroll2006measurement} extend this to nonlinear models.
196	\citet{gustafson2003measurement} develops Bayesian treatments modeling measurement jointly with outcomes.
197	\citet{hu2008nonparametric} provide nonparametric identification using repeated measurements or instruments.
198	
199	\paragraph{Annotation model extensions.}
200	Beyond the foundational \citet{dawid1979maximum} model, \citet{passonneau2014benefits} incorporate item difficulty, \citet{hovy2013learning} learn annotator competence, and \citet{paun2018comparing} introduce hierarchical priors sharing information across annotators with varying expertise.
201	
202	\paragraph{PPI extensions and text-as-data methods.}
203	\citet{zrnic2024cross} extend PPI via cross-prediction; their active inference framework~\citep{zrnic2024active} achieves $>$80\% expert budget savings through adaptive allocation, complementary to our fixed-budget analysis.
204	\citet{grimmer2022text} and \citet{audinet2025benchmarking} provide broader methodological guidance for text-as-data pipelines without specific correction for causal heterogeneity.
205	
206	\paragraph{Treatment vs.\ effect-modifier misclassification.}
207	\citet{imai2010causal} study treatment misclassification where errors change which arm a unit is assigned to, requiring instrumental variables or partial identification because the fundamental treated-vs-control contrast is corrupted.
208	Our problem preserves the treatment contrast ($T$ is observed correctly) but corrupts the heterogeneity structure ($\hat{Z} \neq Z$).
209	The ATE remains identified; only conditional effects are biased, which makes exact correction through confusion matrix inversion feasible.
210	
211	\section{MCMC Convergence Diagnostics}
212	\label{app:mcmc}
213	
214	Table~\ref{tab:mcmc} reports convergence diagnostics for the hierarchical Bayesian confusion matrix estimator across all experimental configurations.
215	All runs use 4 chains with 4000 iterations (2000 warmup) and a $\text{Gamma}(3, 1)$ hyperprior on the Dirichlet concentration $\alpha_0$.
216	
217	\begin{table}[h]
218	\centering
219	\small
220	\begin{tabular}{lcc}
221	\toprule
222	Diagnostic & Threshold & Achieved \\
223	\midrule
224	$\hat{R}$ (max across all params) & $< 1.01$ & $< 1.0034$ \\
225	ESS (min across all params) & $> 845$ & $> 1618$ \\
226	Divergent transitions & $= 0$ & $0$ \\
227	Singularity guard triggers & --- & extreme/$n{=}50$ only \\
228	\bottomrule
229	\end{tabular}
230	\caption{MCMC convergence diagnostics for the hierarchical Bayesian estimator. All configurations satisfy convergence criteria with substantial margin.}
231	\label{tab:mcmc}
232	\end{table}
233	
234	\paragraph{Hyperprior sensitivity.}
235	Scaling the $\text{Gamma}(3, 1)$ hyperprior by factors of $0.5\times$ to $2\times$ produces $<$1\% RMSE variation for $K{=}2$ and $\sim$4--5\% for $K{=}4$.
236	Coverage remains invariant across the sensitivity range.
237	These results confirm that the hierarchical estimator is robust to prior specification within a reasonable range.
238	
239	\section{Diagnostic ROC Curves}
240	\label{app:roc}
241	
242	\begin{figure}[t]
243	\centering
244	\includegraphics[width=\columnwidth]{figures/fig4_roc.png}
245	\caption{ROC curves for the $\Delta\tau$-free diagnostic (Proposition~\ref{prop:debiasing_hurts}): $|\delta_s|/((1{-}2\bar\pi)\cdot\pi_s)>1$. (A)~Setting-level ROC (AUC $= 0.89$), compared with the $|\Delta\pi \times \Delta\tau|$ product (AUC $= 0.89$) and $\mathrm{CV}(\pi_s)$ (AUC $= 0.97$). (B)~Subgroup-level ROC: the $\Delta\pi$-only condition (AUC $= 0.86$) substantially outperforms the $|\Delta\pi \times \Delta\tau|$ product (AUC $= 0.73$). The $\Delta\tau$-free diagnostic depends only on estimable misclassification rates, breaking the circular dependency that would arise if CATE heterogeneity were required.}
246	\label{fig:roc}
247	\end{figure}
248	
249	\section{Expert Budget Crossover Curves}
250	\label{app:budget}
251	\label{sec:budget}
252	
253	The crossover point at which EC-HTE achieves lower RMSE than global correction is $n_{\text{expert}} = 250$ for $K{=}2$/extreme and $n_{\text{expert}} = 1000$ for $K{=}4$/extreme (Figure~\ref{fig:budget}).
254	Under moderate heterogeneity ($K{=}2$), EC-HTE never achieves lower RMSE than global at any budget.
255	HB partial pooling improves over stratified MLE in 21 of 24 configurations, with the two estimators converging by $n_{\text{expert}} \geq 1000$.
256	
257	\begin{figure*}[t]
258	\centering
259	\includegraphics[width=\textwidth]{figures/fig3_budget.pdf}
260	\caption{RMSE vs.\ expert budget ($n_{\text{expert}}$) across four regime$\times K$ combinations. Dashed vertical lines mark crossover points where EC-HTE achieves lower RMSE than global correction: $n{=}250$ ($K{=}2$, extreme), $n{=}1000$ ($K{=}4$, extreme). Under moderate heterogeneity ($K{=}2$), global correction dominates at all budgets. Shaded bands show $\pm 1$ SD across subgroups within each configuration.}
261	\label{fig:budget}
262	\end{figure*}
263	
264	\section{Asymmetric Misclassification Extension}
265	\label{app:asymmetric}
266	
267	Assumption~(A2) imposes symmetric misclassification ($\text{FPR}_s = \text{FNR}_s = \pi_s$), which simplifies the bias decomposition but is not necessary for it.
268	Real LLM annotators typically exhibit asymmetric confusion patterns; we show here that the product structure generalizes.
269	
270	\paragraph{General bias formula.}
271	For asymmetric confusion matrices $C_s = \bigl(\begin{smallmatrix} 1{-}\text{FPR}_s & \text{FPR}_s \\ \text{FNR}_s & 1{-}\text{FNR}_s \end{smallmatrix}\bigr)$, define the mixing matrix $M_s$ via Bayesian inversion and the residual matrix $B_s = M_{\text{global}}^{-1} M_s - I$.
272	Since both $M_s$ and $M_{\text{global}}$ are row-stochastic, $B_s \mathbf{1} = \mathbf{0}$.
273	Decomposing $\boldsymbol{\tau} = \tau(0)\mathbf{1} + \Delta\tau \, \mathbf{e}_1$ gives:
274	\begin{equation}
275	\text{bias}(z, s) = \Delta\tau \cdot [B_s]_{z,1},
276	\end{equation}
277	where $[B_s]_{z,1}$ depends only on $\{\text{FPR}_k, \text{FNR}_k, w_k\}$, not on $\Delta\tau$.
278	Under~(A2), this reduces to $\delta_s \Delta\tau / (1 - 2\bar{\pi})$ (Theorem~\ref{thm:bias_identity}).
279	
280	\paragraph{Empirical validation.}
281	We test three asymmetric configurations ($K{=}2$, $n_{\text{expert}}{=}250$, 100 MC runs each): \emph{Cross} (FPR/FNR = 0.10/0.20 vs.\ 0.25/0.10), \emph{Co-directional} (0.05/0.15 vs.\ 0.20/0.30), and \emph{Extreme} (0.03/0.25 vs.\ 0.30/0.05).
282	Regressing analytic predictions on MC bias yields $R^2 = 0.991$ across all configurations, confirming the product structure under asymmetry.
283	Table~\ref{tab:asymmetric} reports correction performance averaged over subgroups, $z$-levels, and $\Delta\tau \in \{0.1, \ldots, 0.5\}$.
284	EC-HTE reduces $|\text{bias}|$ from 0.025 (global) to 0.006, a $4\times$ improvement, with lower RMSE (0.033 vs.\ 0.040) and substantially better coverage (0.90 vs.\ 0.78).
285	
286	\begin{table}[t]
287	\centering
288	\caption{Asymmetric misclassification results ($K{=}2$, $n_{\text{expert}}{=}250$, 100 MC runs). Values averaged over subgroups, $z$-levels, and $\Delta\tau$.}
289	\label{tab:asymmetric}
290	\small
291	\begin{tabular}{l ccc}
292	\toprule
293	Method & $|\text{Bias}| \downarrow$ & RMSE $\downarrow$ & Coverage $\uparrow$ \\
294	\midrule
295	Naive & 0.047 & 0.053 & 0.48 \\
296	Global & 0.025 & 0.040 & 0.78 \\
297	HB EC-HTE & \textbf{0.006} & \textbf{0.033} & \textbf{0.90} \\
298	\bottomrule
299	\end{tabular}
300	\end{table}
301	
302	\section{Supplementary Main Results}
303	\label{app:main_supp}
304	
305	\begin{table}[t]
306	\centering
307	\caption{Additional configurations from the main experiment. $|\text{Bias}|$ and RMSE averaged over subgroups, $z$-levels, and 100 MC runs. $^\dagger$RMSE exceeds Global.}
308	\label{tab:main_supp}
309	\small
310	\begin{tabular}{ll ccc}
311	\toprule
312	Configuration & Method & $|\text{Bias}|$ & RMSE & Cov. \\
313	\midrule
314	\multirow{4}{*}{\shortstack[l]{Synthetic DIM\\$K{=}2$, moderate, $n{=}250$}}
315	 & Naive & 0.018 & 0.064 & 0.95 \\
316	 & Global & 0.009 & 0.074 & 0.96 \\
317	 & Strat.\ MLE & \textbf{0.005} & 0.075$^\dagger$ & 0.97 \\
318	 & HB EC-HTE & \textbf{0.005} & 0.075$^\dagger$ & 0.97 \\
319	\midrule
320	\multirow{4}{*}{\shortstack[l]{Semi-synthetic\\TweetEval, extreme, $n{=}250$}}
321	 & Naive & 0.027 & 0.103 & 0.93 \\
322	 & Global & \textbf{0.023} & 0.124 & 0.92 \\
323	 & Strat.\ MLE & 0.032 & 0.248$^\dagger$ & 0.91 \\
324	 & HB EC-HTE & 0.027 & 0.225$^\dagger$ & 0.91 \\
325	\bottomrule
326	\end{tabular}
327	\end{table}
328	
329	\section{PPCI Complementarity Results}
330	\label{app:ppci}
331	\label{sec:ppci}
332	
333	EC-HTE composes with PPCI~\cite{sui2026ppci} for settings where both covariate misclassification and outcome model error are present: EC-HTE+PPCI reduces $|\text{bias}|$ from 0.179 to 0.007 ($z{=}0$, DGP~C), and the corrected pseudo-outcomes are compatible with other CATE estimators (R-learner bias reduction: 89\%; Appendix~\ref{app:rlearner}).
334	
335	\begin{table*}[t]
336	\centering
337	\caption{PPCI complementarity experiment ($K{=}2$, extreme, $n_{\text{expert}}{=}250$). DGP~A: covariate error only; B: outcome error only ($\sigma{=}0.5$); C: both errors; D: no error. Values are $|\text{bias}|$ and RMSE averaged over two subgroups. $^\star$EC-HTE+PPCI achieves near-zero bias when both error types are present.}
338	\label{tab:ppci}
339	\small
340	\begin{tabular}{ll cccc}
341	\toprule
342	DGP & Method & $|\text{Bias}|_{z=0}$ & $|\text{Bias}|_{z=1}$ & RMSE$_{z=0}$ & RMSE$_{z=1}$ \\
343	\midrule
344	\multirow{5}{*}{A: Covariate}
345	 & Naive & 0.053 & 0.063 & 0.087 & 0.093 \\
346	 & Global & 0.063 & 0.055 & 0.101 & 0.102 \\
347	 & EC-HTE & 0.017 & \textbf{0.013} & 0.097 & 0.108 \\
348	 & PPCI & \textbf{0.015} & 0.020 & 0.162 & 0.168 \\
349	 & EC-HTE+PPCI & 0.017 & \textbf{0.013} & 0.097 & 0.108 \\
350	\midrule
351	\multirow{5}{*}{B: Outcome}
352	 & Naive & 0.189 & 0.197 & 0.206 & 0.212 \\
353	 & Global & 0.185 & 0.208 & 0.204 & 0.228 \\
354	 & EC-HTE & 0.181 & 0.215 & 0.202 & 0.237 \\
355	 & PPCI & 0.015 & \textbf{0.020} & 0.171 & 0.176 \\
356	 & EC-HTE+PPCI & \textbf{0.012} & 0.023 & 0.171 & 0.186 \\
357	\midrule
358	\multirow{5}{*}{C: Both}
359	 & Naive & 0.251 & 0.135 & 0.267 & 0.155 \\
360	 & Global & 0.182 & 0.209 & 0.233 & 0.235 \\
361	 & EC-HTE & 0.179 & 0.216 & 0.224 & 0.262 \\
362	 & PPCI & 0.017 & 0.007 & 0.241 & 0.232 \\
363	 & EC-HTE+PPCI$^\star$ & \textbf{0.007} & \textbf{0.008} & 0.209 & 0.223 \\
364	\midrule
365	\multirow{5}{*}{D: None}
366	 & Naive & \textbf{0.007} & 0.003 & 0.060 & 0.065 \\
367	 & Global & 0.010 & \textbf{0.002} & 0.061 & 0.071 \\
368	 & EC-HTE & 0.013 & 0.007 & 0.062 & 0.079 \\
369	 & PPCI & \textbf{0.007} & \textbf{0.003} & 0.060 & 0.065 \\
370	 & EC-HTE+PPCI & 0.013 & 0.007 & 0.062 & 0.079 \\
371	\bottomrule
372	\end{tabular}
373	\end{table*}
374	
375	The orthogonality of EC-HTE and PPCI follows from the distinct error sources they correct: EC-HTE addresses misclassification in the effect modifier $Z$ (covariate space), while PPCI corrects specification error in the outcome model $f(X)$ (prediction space).
376	Since covariate misclassification and outcome model error are algebraically independent in the potential outcomes framework, their corrections compose without interference---confirmed by the 4-DGP orthogonal design (Table~\ref{tab:ppci}), where DGP~C (both errors present) yields the largest bias reduction from the combined approach.
377	Under covariate error only, PPCI adds nothing; under no error, all methods perform equivalently.
378	
379	\section{Real-Data Case Study: Hate Speech Detection}
380	\label{app:hatespeech}
381	
382	We apply EC-HTE to the UC Berkeley Measuring Hate Speech corpus~\cite{kennedy2020constructing}, annotating 2{,}496 comments for dehumanization using GPT-4.1.
383	Four text-feature subgroups are defined by crossing platform (Reddit/Gab vs.\ Twitter/YouTube) and text length (above/below median), yielding balanced groups ($n \approx 624$ each).
384	
385	\paragraph{Positive finding: real-world heterogeneity.}
386	Per-subgroup misclassification rates range from 0.266 to 0.383, confirming heterogeneity ($\Delta\pi = 0.117$) in a real annotation setting.
387	At the error-type level, FPR ranges from 8.5\% to 21.3\% across text-feature subgroups, demonstrating that subgroup-varying misclassification is not an artifact of synthetic design but arises naturally in real NLP annotation tasks.
388	
389	\paragraph{Boundary condition: statistical power at extreme FNR.}
390	Correction results are inconclusive: all corrected confidence intervals contain zero, and point estimate differences between methods are not statistically significant.
391	The high baseline FNR (53.3\%) amplifies variance through matrix inversion (variance amplification factor up to 15.7$\times$), rendering the comparison underpowered.
392	When $P(\hat{Z}{=}1 \mid Z{=}1) \approx 0.5$, the confusion matrix approaches singularity, and inversion amplifies estimation noise regardless of stratification strategy.
393	This complements the expert budget threshold identified in Appendix~\ref{sec:budget}: EC-HTE requires \emph{both} sufficient expert labels \emph{and} sufficient baseline classifier quality.
394	
395	\paragraph{Diagnostic connection.}
396	The diagnostic criterion ($\Delta\pi \times \Delta\tau$, Section~\ref{sec:diagnostic}) identifies when correction is worthwhile under moderate baseline accuracy.
397	This case study illustrates that even when $\Delta\pi$ is large, extreme baseline error renders correction underpowered rather than beneficial.
398	A practical prerequisite is that the per-subgroup confusion matrix condition number $\kappa(\hat{C}_s)$ remain moderate; when $\kappa > 50$, as observed here, practitioners should prioritize improving annotation quality before applying any matrix-inversion-based correction.
399	
400	\section{Cross-Model Consistency}
401	\label{app:multilm}
402	
403	We evaluate whether misclassification heterogeneity is model-specific by annotating 500 TweetEval sentiment tweets with six OpenAI models spanning three generations.
404	Six text-feature subgroups are defined by crossing hashtag presence and text length.
405	Spearman rank correlations of per-subgroup error rates across all six subgroups range from $\rho = 0.82$ to $1.00$, indicating that the subgroup error structure is consistent across architectures.
406	Two subgroups with $n \leq 6$ exhibit zero misclassification across all models; excluding these yields four-point correlations that are directionally consistent but underpowered.%
407	\footnote{The filtered $\Delta\pi$ values in Table~\ref{tab:multilm} serve as a robustness check independent of rank-order testing: all six models exceed $\Delta\pi > 0.05$ on the four retained subgroups.}
408	
409	\begin{table}[t]
410	\centering
411	\caption{Effective misclassification heterogeneity ($\Delta\pi$) across six OpenAI models on TweetEval sentiment (500 tweets, filtered to 4 subgroups with $n \geq 10$).}
412	\label{tab:multilm}
413	\small
414	\begin{tabular}{lcc}
415	\toprule
416	Model & Effective $\Delta\pi$ & $> 0.05$? \\
417	\midrule
418	GPT-3.5-Turbo & 0.198 & \checkmark \\
419	GPT-4-Turbo & 0.149 & \checkmark \\
420	GPT-4o-mini & 0.136 & \checkmark \\
421	GPT-5.4 & 0.114 & \checkmark \\
422	GPT-4.1 & 0.098 & \checkmark \\
423	GPT-4o & 0.080 & \checkmark \\
424	\bottomrule
425	\end{tabular}
426	\end{table}
427	
428	All six models exhibit effective $\Delta\pi > 0.05$ on the four retained subgroups (Table~\ref{tab:multilm}), and 5 of 6 share the same worst subgroup (\texttt{True\_medium}: tweets with hashtags and medium text length).
429	Newer models reduce absolute error rates but do not eliminate subgroup heterogeneity: GPT-5.4 achieves $\Delta\pi = 0.114$ compared to GPT-3.5-Turbo's $0.198$.
430	These results were obtained with a single API provider; open-source model validation appears in Appendix~\ref{app:multilm_opensource}.
431	
432	\section{Open-Source Multi-LLM Validation}
433	\label{app:multilm_opensource}
434	
435	We evaluate four open-source LLMs (7B--9B parameter range) on 490 TweetEval sentiment tweets with $K{=}4$ subgroups defined by crossing hashtag presence and text length.
436	Table~\ref{tab:multilm_cm} reports the confusion matrix heterogeneity profile.
437	All four models exhibit $\Delta\pi > 0.05$, confirming that subgroup-heterogeneous misclassification is not specific to proprietary APIs.
438	Subgroup error rankings are consistent across architectures: \texttt{True\_short} (short tweets with hashtags) has the lowest $\pi_s$ in 3 of 4 models, while \texttt{False\_medium} (medium tweets without hashtags) has the highest.
439	
440	\begin{table}[t]
441	\centering
442	\caption{Confusion matrix heterogeneity across four open-source LLMs ($K{=}4$, $N{=}490$ TweetEval tweets). $\Delta\pi$: max--min per-subgroup misclassification rate. Prop2: number of subgroups where the $\Delta\tau$-free diagnostic (Proposition~\ref{prop:debiasing_hurts}) triggers.}
443	\label{tab:multilm_cm}
444	\small
445	\begin{tabular}{lcccl}
446	\toprule
447	Model & Acc.\ & $\Delta\pi$ & Prop2 & Strongest \\
448	\midrule
449	Llama-3.1-8B & 0.755 & 0.141 & 1/4 & True\_short \\
450	Qwen-2.5-7B & 0.798 & 0.165 & 1/4 & True\_short \\
451	Gemma-2-9B & 0.763 & 0.125 & 4/4 & True\_medium \\
452	Mistral-7B & 0.802 & 0.134 & 0/4 & --- \\
453	\bottomrule
454	\end{tabular}
455	\end{table}
456	
457	\paragraph{Semi-synthetic budget sweep.}
458	We run the full EC-HTE pipeline with $K{=}2$ subgroups and $\Delta\tau{=}0.3$, using each model's empirical confusion matrices.
459	Table~\ref{tab:multilm_budget} reports coverage and RMSE crossover points.
460	EC-HTE restores near-nominal coverage from 0.714 (naive average) to 0.939 ($+$22.5 percentage points) at $n_{\text{expert}}{=}1{,}000$, consistent across all four models.
461	Global correction achieves comparable or lower RMSE than HB at all budgets under these moderate $\Delta\pi$ values, and the $K{=}4$ RMSE crossover never occurs---confirming the budget guidelines in Appendix~\ref{sec:budget}.
462	
463	\begin{table}[t]
464	\centering
465	\caption{Semi-synthetic budget sweep ($K{=}2$, $\Delta\tau{=}0.3$, 50 MC runs). Coverage at selected expert budgets; RMSE crossover denotes the minimum expert budget at which HB EC-HTE achieves lower RMSE than the naive (uncorrected) estimator.}
466	\label{tab:multilm_budget}
467	\small
468	\begin{tabular}{lcccc}
469	\toprule
470	Model & $\Delta\pi_{K{=}2}$ & Naive Cov.\ & HB Cov.\ ($n{=}1000$) & Crossover \\
471	\midrule
472	Llama-3.1-8B & 0.051 & 0.675 & 0.940 & $n{=}1000$ \\
473	Qwen-2.5-7B & 0.080 & 0.715 & 0.925 & $n{=}1000$ \\
474	Gemma-2-9B & 0.100 & 0.705 & 0.945 & $n{=}1000$ \\
475	Mistral-7B & 0.070 & 0.760 & 0.945 & $n{=}1000$ \\
476	\midrule
477	\textit{Average} & --- & \textit{0.714} & \textit{0.939} & --- \\
478	\bottomrule
479	\end{tabular}
480	\end{table}
481	
482	\paragraph{Gemma boundary case.}
483	Gemma-2-9B triggers the Proposition~\ref{prop:debiasing_hurts} diagnostic in all four $K{=}4$ subgroups due to extreme FPR--FNR asymmetry (\texttt{False\_medium} FNR $= 0.437$).
484	At small budgets ($K{=}4$, $n{=}100$), EC-HTE RMSE reaches 1.229 ($3.1\times$ naive), illustrating the budget guideline from Appendix~\ref{sec:budget}: when per-subgroup cell counts fall below 25, the variance cost of stratified correction dominates.
485	At $n \geq 500$, EC-HTE coverage recovers to $>$0.90, consistent with the synthetic experiments.
486	
487	\paragraph{Heterogeneous-$\tau$ DGP.}
488	To assess whether the constant-$\tau$ DGP understates EC-HTE's advantage, we run a supplementary experiment using Llama's empirical confusion matrices with heterogeneous treatment effects across subgroups ($\Delta\tau \in [0.1, 0.6]$, $K{=}2$, 50 MC runs).
489	EC-HTE achieves lower $|\text{bias}|$ than global correction at all budgets ($n{=}500$: 0.010 vs.\ 0.031, a 68\% reduction).
490	In the high-$\Delta\tau$ subgroup (\texttt{True\_short}, $\Delta\tau{=}0.6$), EC-HTE also achieves lower RMSE ($n{=}1{,}000$: 0.212 vs.\ 0.258, 18\% improvement), confirming that the RMSE advantage concentrates in subgroups where correction is most needed.
491	Aggregate RMSE remains comparable to global correction because low-$\Delta\tau$ subgroups incur stratification variance without commensurate bias reduction, consistent with the budget guidelines in Appendix~\ref{sec:budget}.
492	
493	\section{Robustness to Subgroup Misspecification}
494	\label{app:robustness}
495	
496	EC-HTE requires pre-defined subgroup labels, which may be noisy in practice.
497	We test robustness by randomly flipping each observation's subgroup assignment with probability $p_{\text{flip}} \in \{0, 0.10, 0.25, 0.50\}$, across $K \in \{2, 4\}$ (extreme regime, $n_{\text{expert}} = 500$, $\Delta\tau = 0.3$, 100 MC runs).
498	
499	\begin{table}[t]
500	\centering
501	\caption{95\% CI coverage under subgroup misspecification noise. EC-HTE maintains near-nominal coverage across all noise levels.}
502	\label{tab:robustness}
503	\small
504	\begin{tabular}{lcccc}
505	\toprule
506	& \multicolumn{4}{c}{$p_{\text{flip}}$} \\
507	\cmidrule(lr){2-5}
508	Method & 0.00 & 0.10 & 0.25 & 0.50 \\
509	\midrule
510	\multicolumn{5}{l}{\textit{$K{=}2$, extreme}} \\
511	\quad Naive & 0.875 & 0.877 & 0.890 & 0.897 \\
512	\quad Global & 0.925 & 0.935 & 0.932 & 0.945 \\
513	\quad HB EC-HTE & 0.958 & 0.948 & 0.950 & 0.945 \\
514	\midrule
515	\multicolumn{5}{l}{\textit{$K{=}4$, extreme}} \\
516	\quad Naive & 0.904 & 0.916 & 0.909 & 0.919 \\
517	\quad Global & 0.930 & 0.953 & 0.948 & 0.944 \\
518	\quad HB EC-HTE & 0.956 & 0.958 & 0.960 & 0.946 \\
519	\bottomrule
520	\end{tabular}
521	\end{table}
522	
523	EC-HTE maintains coverage $\geq 0.945$ across all configurations (Table~\ref{tab:robustness}), while the naive estimator is systematically below nominal (0.875--0.919).
524	At $p_{\text{flip}} = 0.50$, subgroup structure is effectively destroyed; EC-HTE converges to global correction (coverage and RMSE within 0.1\%), confirming that hierarchical Bayesian shrinkage provides a built-in safety mechanism.
525	For $K{=}4$ at $p_{\text{flip}} = 0.50$, a small residual RMSE gap persists ($p < 0.01$), reflecting the variance cost of estimating four confusion matrices even when they carry no signal.
526	
527	\section{Monte Carlo Standard Errors}
528	\label{app:mcse}
529	
530	All experiments use 100 independent Monte Carlo replications per configuration.
531	All simulation results were verified with 100 MC seeds; the median RMSE variation between 50-seed and 100-seed estimates is below 3.2\%, confirming the stability of reported figures.
532	We report Monte Carlo standard errors to assess whether observed differences between methods are statistically reliable.
533	For exp-001 (synthetic DGP, no per-seed pairing across methods), we use conservative two-sample $z$-tests on the 100-run means.
534	For exp-003 (semi-synthetic TweetEval, shared seeds across methods), we use paired $t$-tests, which are more powerful because they control for seed-level variation.
535	
536	Table~\ref{tab:mcse} reports paired comparisons for representative configurations.
537	Of 1{,}020 total pairwise comparisons across all configurations, 742 (72.7\%) are statistically significant at $\alpha = 0.05$.
538	
539	\begin{table}[t]
540	\centering
541	\caption{Paired comparisons for representative configurations. $\Delta$ = method A $-$ method B (negative favors A for $|\text{bias}|$). Two-sample $z$-tests for synthetic (exp-001); paired $t$-tests for semi-synthetic (exp-003). Bold $p$-values indicate significance at $\alpha = 0.05$.}
542	\label{tab:mcse}
543	\small
544	\begin{tabular}{llrr}
545	\toprule
546	Configuration & Comparison & $\Delta$ & $p$ \\
547	\midrule
548	\multicolumn{4}{l}{\textit{HB EC-HTE vs.\ Global ($|\text{bias}|$)}} \\
549	\quad $K{=}2$/ext/$n{=}500$ & & $-0.046$ & $\mathbf{<0.001}$ \\
550	\quad $K{=}4$/ext/$n{=}500$ & & $-0.078$ & $\mathbf{<0.001}$ \\
551	\quad $K{=}4$/mod/$n{=}250$ & & $-0.017$ & $0.288$ \\
552	\quad TweetEval/ext/$n{=}250$ & & $+0.001$ & $0.395$ \\
553	\midrule
554	\multicolumn{4}{l}{\textit{HB EC-HTE vs.\ Global (RMSE)}} \\
555	\quad $K{=}2$/ext/$n{=}500$ & & $+0.015$ & $0.179$ \\
556	\quad $K{=}4$/ext/$n{=}500$ & & $+0.048$ & $\mathbf{0.011}$ \\
557	\midrule
558	\multicolumn{4}{l}{\textit{HB EC-HTE vs.\ Naive ($|\text{bias}|$)}} \\
559	\quad $K{=}2$/ext/$n{=}500$ & & $-0.089$ & $\mathbf{<0.001}$ \\
560	\quad $K{=}4$/ext/$n{=}500$ & & $-0.113$ & $\mathbf{<0.001}$ \\
561	\quad $K{=}4$/mod/$n{=}250$ & & $-0.031$ & $\mathbf{0.038}$ \\
562	\quad TweetEval/ext/$n{=}250$ & & $+0.005$ & $\mathbf{0.030}$ \\
563	\bottomrule
564	\end{tabular}
565	\end{table}
566	
567	Under extreme heterogeneity, HB EC-HTE's bias advantage over global correction is highly significant ($p < 0.001$ for both $K{=}2$ and $K{=}4$).
568	The RMSE penalty of stratification is not significant at $K{=}2$ ($p = 0.179$) but reaches significance at $K{=}4$ ($p = 0.011$), consistent with the higher variance cost of estimating four confusion matrices.
569	Under moderate heterogeneity ($K{=}4$, $n{=}250$), the bias difference between HB and global is not significant ($p = 0.288$), confirming that EC-HTE's advantage requires sufficient error heterogeneity.
570	In the semi-synthetic TweetEval experiment, HB EC-HTE does not significantly improve over global ($p = 0.395$), consistent with moderate $\Delta\pi$ and unbalanced subgroup sizes.
571	The HB vs.\ naive comparison in TweetEval is significant ($p = 0.030$) but favors naive, reflecting the variance cost of stratification when bias reduction is marginal.
572	
573	\section{Semi-Real Confusion Matrix Validation}
574	\label{app:semireal}
575	
576	We test EC-HTE with empirical asymmetric confusion matrices from the GPT-4.1 TweetEval pilot.
577	Four text-feature subgroups ($K{=}4$) retain the real per-subgroup FPR and FNR from pilot annotations (Table~\ref{tab:semireal_cm}); CATE heterogeneity is injected synthetically ($\tau(z{=}0,s) = 0.3 + 0.1s$, $\tau(z{=}1,s) = 0.8 - 0.15s$).
578	$N{=}5{,}000$, $P(Z{=}1){=}0.18$, 100 MC seeds per $n_{\text{expert}}$ level.
579	
580	\begin{table}[t]
581	\centering
582	\caption{Empirical confusion matrices from GPT-4.1 TweetEval pilot.
583	S0 exhibits FNR $= 0.526$, approaching chance-level classification.}
584	\label{tab:semireal_cm}
585	\small
586	\begin{tabular}{lcccc}
587	\toprule
588	Subgroup & Weight & FPR & FNR & $\kappa(\hat{C}_s)$ \\
589	\midrule
590	S0 & 0.38 & 0.054 & 0.526 & high \\
591	S1 & 0.22 & 0.101 & 0.300 & moderate \\
592	S2 & 0.14 & 0.143 & 0.308 & moderate \\
593	S3 & 0.25 & 0.194 & 0.222 & low \\
594	\bottomrule
595	\end{tabular}
596	\end{table}
597	
598	\begin{table}[t]
599	\centering
600	\caption{Semi-real confusion matrix results. RMSE and coverage averaged over subgroups and $z$-levels (100 MC runs). HB EC-HTE underperforms global at all budgets; S0's near-chance FNR drives the failure.}
601	\label{tab:semireal}
602	\small
603	\begin{tabular}{llcc}
604	\toprule
605	$n_{\text{expert}}$ & Method & RMSE $\downarrow$ & Coverage $\uparrow$ \\
606	\midrule
607	\multirow{4}{*}{100}
608	 & Oracle & 0.101 & 0.957 \\
609	 & Naive & 0.123 & 0.879 \\
610	 & Global & 0.263 & 0.885 \\
611	 & HB EC-HTE & 0.784 & 0.744 \\
612	\midrule
613	\multirow{4}{*}{250}
614	 & Oracle & 0.101 & 0.957 \\
615	 & Naive & 0.123 & 0.879 \\
616	 & Global & 0.232 & 0.909 \\
617	 & HB EC-HTE & 0.411 & 0.834 \\
618	\midrule
619	\multirow{4}{*}{500}
620	 & Oracle & 0.101 & 0.957 \\
621	 & Naive & 0.123 & 0.879 \\
622	 & Global & 0.196 & 0.922 \\
623	 & HB EC-HTE & 0.260 & 0.890 \\
624	\bottomrule
625	\end{tabular}
626	\end{table}
627	
628	HB EC-HTE produces higher RMSE and lower coverage than global correction at all expert budgets (Table~\ref{tab:semireal}).
629	The root cause is S0's FNR $= 0.526$: when a confusion matrix row approaches a uniform distribution ($P(\hat{Z}{=}1 \mid Z{=}1) \approx 0.5$), inversion amplifies estimation noise regardless of the expert budget.
630	This converges with the hate speech case study (Appendix~\ref{app:hatespeech}, FNR $= 53.3$\%) and confirms that EC-HTE requires \emph{both} sufficient expert labels \emph{and} sufficient baseline classifier quality per subgroup.
631	The singularity guard ($\kappa > 100$, Section~\ref{sec:method}) mitigates catastrophic failure by falling back to global correction for near-degenerate subgroups, but does not recover the bias reduction that motivates stratification.
632	At $n_{\text{expert}} = 500$, HB EC-HTE narrows the gap (RMSE 0.260 vs.\ 0.196) as confusion matrix estimates stabilize for the three well-classified subgroups, but the S0 bottleneck persists.
633	
634	A second semi-real experiment using GPT-3.5-Turbo confusion matrices (worst-subgroup FPR $= 0.39$, FNR $= 0.21$) yields similar results: HB RMSE exceeds global by 1.3--3.5$\times$ at all budgets.
635	Here the failure stems from high false-positive rates compounded by class imbalance ($P(Z{=}1) = 0.18$), which leaves insufficient expert observations in the positive class for reliable per-subgroup confusion matrix estimation.
636	Together, these experiments identify three applicability conditions for EC-HTE: (1)~sufficient effective expert budget ($n_{\text{expert}} \times P(Z_{\text{minority}}) / K \geq 25$), (2)~no near-chance subgroup error rate ($\max(\text{FPR}_s, \text{FNR}_s) < 0.5$), and (3)~adequate class balance in the effect modifier.
637	
638	\paragraph{Diagnostic rule.}
639	A logistic regression over all 368 semi-real experiment--budget cells (dependent variable: HB EC-HTE $<$ Global RMSE) identifies two sufficient statistics: the worst-subgroup confusion matrix condition number $\kappa(\hat{M}_s) \leq 1.25$ and the effective minority-class expert count $n_{\text{expert}} \times P(Z_{\text{minority}}) / K \geq 25$.
640	When both conditions hold, HB outperforms global in 93.3\% of cells; when either is violated, global is preferred in 94.7\% of cells.
641	Both exp-015 ($\kappa = 2.38$, effective $n = 2.5$) and exp-016 ($\kappa = 1.55$, effective $n = 2.5$) violate both conditions, and the diagnostic correctly predicts 100\% of their failure cells.
642	Subgroup-average metrics can mask cell-level heterogeneity: in exp-015, HB EC-HTE substantially reduces bias for the three well-classified subgroups (S1--S3) but amplifies variance in the near-degenerate subgroup (S0, FNR $= 0.526$), and the S0 penalty dominates the aggregate RMSE.
643	
644	\begin{figure}[t]
645	\centering
646	\includegraphics[width=\columnwidth]{figures/applicability_frontier.pdf}
647	\caption{Applicability frontier of EC-HTE. Green region: EC-HTE reduces bias vs.\ global correction. Yellow: comparable performance. Red: EC-HTE underperforms. Dashed lines mark the expert budget threshold ($n_{\text{expert}}/K = 25$) and classifier quality threshold (worst-subgroup error rate $= 0.5$). Red diamonds show semi-real experiments with actual GPT-4.1 and GPT-3.5-Turbo confusion matrices.}
648	\label{fig:applicability}
649	\end{figure}
650	
651	\section{Robustness: Estimator Choice and Treatment Effect Specification}
652	\label{app:rlearner}
653	
654	We verify that EC-HTE's corrected pseudo-outcomes are compatible with downstream estimators beyond CausalForest by replacing it with the R-learner~\citep{nie2021quasi}.
655	The experiment uses $K{=}2$, extreme heterogeneity, $n_{\text{expert}} = 500$, and 50 MC seeds; the R-learner uses 5-fold cross-fitting with gradient-boosted trees as the base learner.
656	
657	\begin{table}[t]
658	\centering
659	\caption{R-learner vs.\ CausalForest with EC-HTE correction ($K{=}2$, extreme, $n{=}500$). $|\text{Bias}|$ and RMSE averaged over subgroups, $z$-levels, and seeds.}
660	\label{tab:rlearner}
661	\small
662	\begin{tabular}{llccc}
663	\toprule
664	Estimator & Correction & $|\text{Bias}|$ & RMSE & Cov. \\
665	\midrule
666	\multirow{4}{*}{R-learner}
667	 & Oracle & 0.006 & 0.056 & 0.94 \\
668	 & Naive & 0.121 & 0.139 & 0.47 \\
669	 & Global & 0.098 & 0.123 & 0.72 \\
670	 & EC-HTE & \textbf{0.013} & 0.080 & 0.92 \\
671	\midrule
672	\multirow{2}{*}{CausalForest}
673	 & Naive & 0.058 & 0.090 & 0.82 \\
674	 & EC-HTE & \textbf{0.010} & 0.093 & 0.95 \\
675	\bottomrule
676	\end{tabular}
677	\end{table}
678	
679	EC-HTE reduces R-learner $|\text{bias}|$ by 89\% (0.121 $\to$ 0.013) and restores coverage from 0.47 to 0.92 (Table~\ref{tab:rlearner}).
680	The bias reduction and coverage gains are comparable to those achieved with CausalForest, confirming that EC-HTE functions as an estimator-agnostic upstream correction.
681	
682	\paragraph{Multiplicative treatment effects.}
683	We further test robustness to the functional form of treatment effects by replacing the additive DGP with a multiplicative specification: $Y(1) = Y(0) \times \exp(\tau(Z))$, using $K{=}2$, extreme heterogeneity, $n_{\text{expert}} = 500$, and 50 MC seeds.
684	
685	\begin{table}[t]
686	\centering
687	\caption{Multiplicative DGP results ($K{=}2$, extreme, $n{=}500$, 50 seeds). EC-HTE achieves comparable bias reduction and nominal coverage under non-additive treatment effects.}
688	\label{tab:multiplicative}
689	\small
690	\begin{tabular}{lccc}
691	\toprule
692	Method & $|\text{Bias}|$ & RMSE & Cov. \\
693	\midrule
694	Oracle & 0.003 & 0.038 & 0.96 \\
695	Naive & 0.135 & 0.142 & 0.44 \\
696	Global & 0.110 & 0.124 & 0.54 \\
697	EC-HTE & \textbf{0.054} & 0.068 & 0.955 \\
698	\bottomrule
699	\end{tabular}
700	\end{table}
701	
702	EC-HTE reduces RMSE by 52\% relative to naive (0.068 vs.\ 0.142) and restores coverage to the nominal level (0.955; Table~\ref{tab:multiplicative}).
703	EC-HTE's bias correction operates at the confusion matrix level, independent of the downstream CATE estimator and functional form of treatment effects.
704	
705	\section{Robustness to Class Imbalance}
706	\label{app:classimbalance}
707	
708	Assumption (A3) requires $P(Z{=}1) = 0.5$, but real-world effect modifiers are often imbalanced.
709	We sweep $P(Z{=}1) \in \{0.1, 0.2, 0.3, 0.4, 0.5\}$ with $K \in \{2,4\}$, extreme misclassification heterogeneity, $n_{\text{expert}}{=}250$, and 100 MC seeds (Table~\ref{tab:pz1_sweep}).
710	
711	\begin{table}[t]
712	\centering
713	\caption{Robustness to class imbalance ($n_{\text{expert}}{=}250$, extreme heterogeneity). R$^2$: Theorem~\ref{thm:bias_identity} fit. Ratio: HB/Global RMSE ($<1$ = HB wins). Cov.: HB EC-HTE 95\% CI coverage.}
714	\label{tab:pz1_sweep}
715	\small
716	\begin{tabular}{cc ccc}
717	\toprule
718	$P(Z{=}1)$ & $K$ & R$^2$ & Ratio & Cov. \\
719	\midrule
720	0.1 & 2 & 0.998 & 0.92 & 0.94 \\
721	0.2 & 2 & 0.989 & 0.76 & 0.94 \\
722	0.3 & 2 & 0.994 & 0.78 & 0.94 \\
723	0.4 & 2 & 0.995 & 0.87 & 0.94 \\
724	0.5 & 2 & 0.995 & 0.86 & 0.93 \\
725	\midrule
726	0.1 & 4 & 0.984 & 1.54 & 0.92 \\
727	0.2 & 4 & 0.976 & 1.68 & 0.93 \\
728	0.3 & 4 & 0.985 & 1.12 & 0.92 \\
729	0.4 & 4 & 0.984 & 1.08 & 0.93 \\
730	0.5 & 4 & 0.992 & 1.06 & 0.92 \\
731	\bottomrule
732	\end{tabular}
733	\end{table}
734	
735	Theorem~\ref{thm:bias_identity}'s product form remains accurate across all imbalance levels: $R^2 \geq 0.976$ even at $P(Z{=}1) = 0.1$, confirming that the bias identity derives from confusion matrix structure rather than class balance.
736	For $K{=}2$, EC-HTE outperforms global correction at all $P(Z{=}1)$ levels (RMSE ratio 0.76--0.92), degrading gracefully under severe imbalance.
737	For $K{=}4$, EC-HTE underperforms global at $n_{\text{expert}}{=}250$ (ratio 1.06--1.68), consistent with the budget threshold $n_{\text{expert}} \times P(Z_{\text{minority}}) / K \geq 25$: at $P(Z{=}1){=}0.1$, $K{=}4$, each subgroup receives only ${\sim}6$ minority-class labels.
738	The gap narrows as $P(Z{=}1)$ increases (1.54 $\to$ 1.06), and coverage remains stable at 0.92--0.94 across all configurations.
739	
740	\section{Comparison with PPI Correction}
741	\label{app:ppi_comparison}
742	
743	PPI~\cite{angelopoulos2023ppi} constructs confidence intervals by combining a large set of ML predictions with a smaller set of gold-standard labels, using the gold labels to debias the ML-based estimator.
744	Applied to our setting, PPI treats the LLM-annotated effect modifier as the ML prediction and the expert labels as the gold standard.
745	Two variants arise naturally: \emph{PPI-global} pools all expert labels to estimate a single rectifier (analogous to our Global baseline), and \emph{PPI-subgroup} estimates per-subgroup rectifiers (analogous to Stratified MLE).
746	
747	Under the confusion-matrix parameterization we adopt, DSL's measurement error correction reduces to confusion matrix inversion.
748	Pooled DSL applies a single estimated confusion matrix to all subgroups, producing the same corrected label distribution as our Global baseline; per-subgroup DSL estimates a separate confusion matrix for each subgroup and inverts it independently, equivalent to our Stratified MLE.
749	EC-HTE's contribution over both PPI-subgroup and per-subgroup DSL is hierarchical partial pooling: rather than estimating each subgroup's confusion matrix in isolation, EC-HTE places a shared prior across subgroups, borrowing strength to reduce variance while preserving subgroup-specific bias correction.
750	This mechanism is outside both the PPI and DSL frameworks.
751	
752	The key difference between PPI and confusion-matrix inversion is that PPI does not invert the confusion matrix; instead, it uses the gold labels to directly debias the estimand.
753	This avoids the matrix inversion step that can amplify noise at small $n_{\text{expert}}$, but it also means PPI cannot exploit the structure of the misclassification process to reduce bias.
754	PPI-global inherits the same $\Delta\pi \times \Delta\tau$ bias amplification as Global correction (Theorem~\ref{thm:bias_identity}), confirming that the ``debiasing hurts'' mechanism operates regardless of the inference framework.
755	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "66569921-b021-4e63-b34f-5a57ace8a070",
  "isSidechain": true,
  "promptId": "410c5182-a00d-45c3-a02c-4785eb40bb89",
  "agentId": "a217013802bf0fe69",
  "type": "user",
  "uuid": "ec6863dc-390c-4434-bcb5-526ce3cf17c6",
  "sourceToolAssistantUUID": "66569921-b021-4e63-b34f-5a57ace8a070",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/paper_agent_8babce27",
  "sessionId": "6ae78efb-2b23-4404-a761-5afc621a128d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "zazzy-giggling-simon"
}
```

</details>

---

### Assistant

_source line 10 · 2026-05-22T05:42:30.528Z_

Now let me search for section 5.5 in the main papers to find the Multi-LLM content:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ec6863dc-390c-4434-bcb5-526ce3cf17c6",
  "isSidechain": true,
  "agentId": "a217013802bf0fe69",
  "requestId": "req_011CbH5Dz1r1QGvwYWoUQDkp",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "437ed032-aa7d-442b-857d-27290fffc567",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/paper_agent_8babce27",
  "sessionId": "6ae78efb-2b23-4404-a761-5afc621a128d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "zazzy-giggling-simon",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01C9T9ziYxnxSLPNHpSEyJVC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 20663,
      "cache_read_input_tokens": 29186,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 20663,
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

_source line 11 · 2026-05-22T05:42:31.688Z_

<details open><summary>🔧 Tool call — Bash · `toolu_017bjXgcj9KRXpQ1ZAmcYmwL`</summary>

```json
{
  "command": "grep -n \"§5.5\\|\\\\\\\\section.*5\\.5\\|\\\\\\\\section.*[Mm]ulti\" /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/*.tex 2>/dev/null | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "437ed032-aa7d-442b-857d-27290fffc567",
  "isSidechain": true,
  "agentId": "a217013802bf0fe69",
  "requestId": "req_011CbH5Dz1r1QGvwYWoUQDkp",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "00509757-cdb3-4fa8-8625-c978be6ac920",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/paper_agent_8babce27",
  "sessionId": "6ae78efb-2b23-4404-a761-5afc621a128d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "zazzy-giggling-simon",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01C9T9ziYxnxSLPNHpSEyJVC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 20663,
      "cache_read_input_tokens": 29186,
      "output_tokens": 152,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 20663
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 152,
          "cache_read_input_tokens": 29186,
          "cache_creation_input_tokens": 20663,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 20663,
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

_source line 12 · 2026-05-22T05:42:31.851Z_

<details><summary>↩ Tool result · `toolu_017bjXgcj9KRXpQ1ZAmcYmwL`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex:98:\section{Multi-class Extension and Proof}
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex:432:\section{Open-Source Multi-LLM Validation}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "00509757-cdb3-4fa8-8625-c978be6ac920",
  "isSidechain": true,
  "promptId": "410c5182-a00d-45c3-a02c-4785eb40bb89",
  "agentId": "a217013802bf0fe69",
  "type": "user",
  "uuid": "d9e17e8b-443b-419a-ab76-f7663aba2bcc",
  "sourceToolAssistantUUID": "00509757-cdb3-4fa8-8625-c978be6ac920",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/paper_agent_8babce27",
  "sessionId": "6ae78efb-2b23-4404-a761-5afc621a128d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "zazzy-giggling-simon"
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-22T05:42:34.312Z_

Good! I found the "Open-Source Multi-LLM Validation" section. Now let me search for section 5.5 in the experiments file:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d9e17e8b-443b-419a-ab76-f7663aba2bcc",
  "isSidechain": true,
  "agentId": "a217013802bf0fe69",
  "requestId": "req_011CbH5EEJ5prNKX4i4qijpP",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "ad39e492-4038-45f8-bb35-fa1256eb34df",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/paper_agent_8babce27",
  "sessionId": "6ae78efb-2b23-4404-a761-5afc621a128d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "zazzy-giggling-simon",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01JuQ6GJuZcSKHs1nGf7FEgc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 270,
      "cache_read_input_tokens": 49849,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 270,
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

_source line 14 · 2026-05-22T05:42:34.641Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01ATFu5wsmvH7jBQn1Ud1GHb`</summary>

```json
{
  "command": "grep -n \"\\\\\\\\section\\|\\\\\\\\subsection\" /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/experiments.tex | head -30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ad39e492-4038-45f8-bb35-fa1256eb34df",
  "isSidechain": true,
  "agentId": "a217013802bf0fe69",
  "requestId": "req_011CbH5EEJ5prNKX4i4qijpP",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "c969203b-4a3c-40b9-853e-1a96ee6340a9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/paper_agent_8babce27",
  "sessionId": "6ae78efb-2b23-4404-a761-5afc621a128d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "zazzy-giggling-simon",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01JuQ6GJuZcSKHs1nGf7FEgc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 270,
      "cache_read_input_tokens": 49849,
      "output_tokens": 142,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 270
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4,
          "output_tokens": 142,
          "cache_read_input_tokens": 49849,
          "cache_creation_input_tokens": 270,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 270,
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

_source line 15 · 2026-05-22T05:42:34.713Z_

<details><summary>↩ Tool result · `toolu_01ATFu5wsmvH7jBQn1Ud1GHb`</summary>

```text
1:\section{Experiments}
3:\subsection{Setup}
20:\subsection{Bias Mechanism Verification}
38:\subsection{EC-HTE Evaluation}
82:\subsection{Diagnostic Criterion}
100:\subsection{Open-Source Multi-LLM Validation}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c969203b-4a3c-40b9-853e-1a96ee6340a9",
  "isSidechain": true,
  "promptId": "410c5182-a00d-45c3-a02c-4785eb40bb89",
  "agentId": "a217013802bf0fe69",
  "type": "user",
  "uuid": "68b1e630-d56a-4742-b1e0-e52c9bccc277",
  "sourceToolAssistantUUID": "c969203b-4a3c-40b9-853e-1a96ee6340a9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/paper_agent_8babce27",
  "sessionId": "6ae78efb-2b23-4404-a761-5afc621a128d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "zazzy-giggling-simon"
}
```

</details>

---

### Assistant

_source line 16 · 2026-05-22T05:42:43.183Z_

Perfect! Now let me read the experiments.tex file to get the full section on "Open-Source Multi-LLM Validation":

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "68b1e630-d56a-4742-b1e0-e52c9bccc277",
  "isSidechain": true,
  "agentId": "a217013802bf0fe69",
  "requestId": "req_011CbH5ESczoZURXrenPk3RC",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "74b53580-6e50-4387-ae1d-0dcb75e42cb8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/paper_agent_8babce27",
  "sessionId": "6ae78efb-2b23-4404-a761-5afc621a128d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "zazzy-giggling-simon",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01FSvh5KBruneEHwG1R3zd9B",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 223,
      "cache_read_input_tokens": 50119,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 223,
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

_source line 17 · 2026-05-22T05:42:43.315Z_

<details open><summary>🔧 Tool call — Read · `toolu_01St7SLc69MRE3tFXW9H4Fhy`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "74b53580-6e50-4387-ae1d-0dcb75e42cb8",
  "isSidechain": true,
  "agentId": "a217013802bf0fe69",
  "requestId": "req_011CbH5ESczoZURXrenPk3RC",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "e3ca5928-af5c-4cd8-8543-4c735d6cc926",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/paper_agent_8babce27",
  "sessionId": "6ae78efb-2b23-4404-a761-5afc621a128d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "zazzy-giggling-simon",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01FSvh5KBruneEHwG1R3zd9B",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 223,
      "cache_read_input_tokens": 50119,
      "output_tokens": 119,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 223
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 119,
          "cache_read_input_tokens": 50119,
          "cache_creation_input_tokens": 223,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 223,
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

_source line 18 · 2026-05-22T05:42:43.328Z_

<details><summary>↩ Tool result · `toolu_01St7SLc69MRE3tFXW9H4Fhy`</summary>

```text
1	\section{Experiments}
2	
3	\subsection{Setup}
4	
5	We evaluate on synthetic and semi-synthetic data generating processes (DGPs); full specifications appear in Appendix~\ref{app:dgp}.
6	The synthetic DGP generates $N{=}5{,}000$ observations from a randomized trial with $K \in \{2, 4\}$ subgroups, controlled CATE heterogeneity $\Delta\tau$, and subgroup-specific symmetric misclassification rates with heterogeneity $\Delta\pi$.
7	Expert labels ($n_{\text{expert}} \in \{50, \ldots, 2000\}$) are a simple random sample with true $Z$ observed; each configuration is repeated for 100 Monte Carlo runs.
8	The semi-synthetic DGP samples $N{=}5{,}000$ tweets from TweetEval sentiment~\cite{barbieri2020tweeteval}, defining $K{=}4$ subgroups by crossing hashtag presence and text length (unbalanced: 39\%/38\%/12\%/11\%), with misclassification rates $\pi \in \{0.05, 0.10, 0.15, 0.25\}$ reflecting empirical evidence that text features degrade LLM accuracy~\cite{ashwin2025bias}.
9	
10	We compare: (1) \textit{Naive} (no correction), (2) \textit{Global} (pooled confusion matrix), (3) \textit{Stratified MLE} (per-subgroup MLE without pooling), (4) \textit{HB EC-HTE} (our method), (5) \textit{PPCI}~\cite{sui2026ppci}, and (6) \textit{EC-HTE+PPCI}.
11	For CausalForest~\cite{wager2018causal}, we compare naive, global, and EC-HTE variants.
12	Our Global baseline is equivalent to PPI/DSL~\cite{angelopoulos2023ppi,egami2024dsl} applied with a pooled (homogeneous) error rate; Stratified MLE corresponds to per-subgroup DSL without hierarchical shrinkage.
13	EC-HTE extends this by borrowing strength across subgroups via hierarchical Bayesian estimation.
14	Primary metrics are $|\text{bias}|$, RMSE, and 95\% CI coverage, averaged across subgroups and 100 MC runs.
15	Real-data validation on hate speech detection confirms $\Delta\pi = 0.117$ across text-feature subgroups (Appendix~\ref{app:hatespeech}).
16	The heterogeneity pattern persists across six OpenAI models spanning three generations (Appendix~\ref{app:multilm}) and four open-source LLMs in the 7B--9B parameter range (Section~\ref{sec:multilm_opensource}).
17	EC-HTE maintains $\geq$94.5\% coverage under up to 50\% subgroup misspecification noise (Appendix~\ref{app:robustness}).
18	When empirical asymmetric confusion matrices from the GPT-4.1 pilot are used directly, a subgroup with FNR~$\approx 0.5$ causes EC-HTE to underperform global correction at all budgets (Appendix~\ref{app:semireal}).
19	
20	\subsection{Bias Mechanism Verification}
21	\label{sec:bias_mechanism}
22	
23	The bias decomposition identity (Theorem~\ref{thm:bias_identity}) predicts that global correction introduces bias proportional to $\Delta\pi \times \Delta\tau$ at the subgroup level.
24	We verify this identity empirically across 520 configurations spanning $K \in \{2,4\}$, two misclassification regimes, and six expert budget levels.
25	Regressing observed subgroup bias on the predicted $\Delta\pi \times \Delta\tau$ product yields $R^2 = 0.994$ for $K{=}2$ and $R^2 = 0.974$ for $K{=}4$; the residual variance reflects MC sampling noise rather than model misspecification, since Theorem~\ref{thm:bias_identity} is an exact identity at the population level ($R^2 \geq 0.976$ even at $P(Z{=}1) = 0.1$; Appendix~\ref{app:classimbalance}).
26	In 50\% of configurations (260/520, excluding $\Delta_c{=}0$ rows where bias is zero by construction), global correction produces larger absolute bias than the naive estimator.
27	The damage concentrates in low-$\pi$ subgroups: among subgroups where $\pi_s < \bar{\pi}$, global correction increases bias in 84.6\% of cases.
28	Maximum observed amplification reaches 2.86$\times$ (K=2) and 2.41$\times$ (K=4) relative to the naive estimator.
29	Figure~\ref{fig:heatmap} visualizes the $\Delta\pi \times \Delta\tau$ amplification surface across the parameter grid.
30	
31	\begin{figure*}[t]
32	\centering
33	\includegraphics[width=\textwidth]{figures/fig2_heatmap.pdf}
34	\caption{Bias amplification under global correction across the $\Delta\pi \times \Delta\tau$ parameter grid ($K{=}2$). (a) Low-error subgroup: global correction always helps (ratio $< 1$). (b) High-error subgroup: when $\Delta\pi > 0.12$ (dashed line), global correction \emph{increases} bias relative to the naive estimator (hatched region), with amplification reaching 2.86$\times$.}
35	\label{fig:heatmap}
36	\end{figure*}
37	
38	\subsection{EC-HTE Evaluation}
39	\label{sec:ec_hte_eval}
40	
41	Table~\ref{tab:main_results} presents the main results across representative configurations.
42	In the synthetic DGP with $K{=}2$ subgroups and extreme misclassification heterogeneity, HB EC-HTE reduces $|\text{bias}|$ from 0.059 (global) to 0.010 (a 5.9$\times$ reduction) while maintaining nominal coverage (0.95) and comparable RMSE (0.093 vs.\ 0.099).
43	The advantage persists at $K{=}4$: EC-HTE achieves $|\text{bias}|{=}0.008$ versus 0.056 for global (7.0$\times$ reduction), though with a small RMSE penalty (0.126 vs.\ 0.125).
44	Under moderate heterogeneity ($K{=}2$), methods converge: EC-HTE and global achieve comparable bias ($p > 0.05$; Table~\ref{tab:main_supp}).
45	In the semi-synthetic TweetEval experiment ($N{=}5{,}000$, $K{=}4$), global correction achieves the lowest $|\text{bias}|$ (0.023), while EC-HTE attains 0.027 with higher RMSE (0.225 vs.\ 0.124), consistent with moderate $\Delta\pi{=}0.20$ and unbalanced subgroup sizes (Table~\ref{tab:main_supp}).
46	
47	\paragraph{CausalForest K-dependence.}
48	When the downstream estimator is a CausalForest~\cite{wager2018causal}, the bias mechanism operates with amplified magnitude.
49	At $K{=}4$/extreme/$n{=}500$, EC-HTE Forest reduces $|\text{bias}|$ from 0.191 (global) to 0.040, a 4.8$\times$ improvement with dramatically better coverage (0.91 vs.\ 0.58).
50	The debiasing-hurts phenomenon intensifies: global correction amplifies naive bias by up to 5.9$\times$ in the worst subgroup, because the forest's sensitivity to covariate noise magnifies the effect of label errors.
51	At $K{=}4$/$n{=}100$, EC-HTE Forest RMSE reaches 1.43 (3.5$\times$ naive), underscoring the budget guidelines in Appendix~\ref{sec:budget}.
52	
53	\begin{table}[t]
54	\centering
55	\caption{Main results under extreme misclassification heterogeneity. $|\text{Bias}|$ and RMSE averaged over subgroups, $z$-levels, and 100 MC runs. Bold marks lowest $|\text{bias}|$ per block. $^\dagger$RMSE exceeds Global, reflecting stratification variance cost. Additional configurations (moderate heterogeneity, semi-synthetic TweetEval) in Table~\ref{tab:main_supp}. MC standard errors: Appendix~\ref{app:mcse}.}
56	\label{tab:main_results}
57	\resizebox{\columnwidth}{!}{%
58	\begin{tabular}{ll ccc}
59	\toprule
60	Configuration & Method & $|\text{Bias}|$ & RMSE & Cov. \\
61	\midrule
62	\multirow{4}{*}{\shortstack[l]{DIM\\$K{=}2$, $n{=}250$}}
63	 & Naive & 0.058 & 0.090 & 0.82 \\
64	 & Global & 0.059 & 0.099 & 0.87 \\
65	 & Strat.\ MLE & 0.012 & 0.094 & 0.95 \\
66	 & HB EC-HTE & \textbf{0.010} & 0.093 & 0.95 \\
67	\midrule
68	\multirow{4}{*}{\shortstack[l]{DIM\\$K{=}4$, $n{=}500$}}
69	 & Naive & 0.062 & 0.113 & 0.88 \\
70	 & Global & 0.056 & 0.125 & 0.91 \\
71	 & Strat.\ MLE & 0.010 & 0.127$^\dagger$ & 0.95 \\
72	 & HB EC-HTE & \textbf{0.008} & 0.126$^\dagger$ & 0.95 \\
73	\midrule
74	\multirow{3}{*}{\shortstack[l]{CausalForest\\$K{=}4$, $n{=}500$}}
75	 & Naive & 0.208 & 0.231 & 0.44 \\
76	 & Global & 0.191 & 0.244 & 0.58 \\
77	 & EC-HTE Forest & \textbf{0.040} & 0.224 & 0.91 \\
78	\bottomrule
79	\end{tabular}}
80	\end{table}
81	
82	\subsection{Diagnostic Criterion}
83	\label{sec:diagnostic}
84	
85	Proposition~\ref{prop:debiasing_hurts} provides a $\Delta\tau$-free diagnostic: global correction increases bias in subgroup $s$ if and only if $|\delta_s| / ((1-2\bar{\pi}) \cdot \pi_s) > 1$, where $\delta_s = \pi_s - \bar{\pi}$.
86	This condition depends only on per-subgroup misclassification rates estimable from a pilot sample, breaking the circular dependency that would arise if the diagnostic required CATE estimates.
87	Since the Proposition~\ref{prop:debiasing_hurts} score is a deterministic function of per-subgroup misclassification rates, a threshold classifier achieves AUC = 0.86 at the subgroup level for predicting whether global correction increases bias relative to the naive estimator, outperforming the $\Delta\pi \times \Delta\tau$ product (AUC = 0.73) which requires unobservable CATE heterogeneity.
88	At the setting level, the condition achieves AUC = 0.89 because it identifies settings where \emph{any} subgroup is harmed.
89	Figure~\ref{fig:roc} (Appendix) shows the ROC curve.
90	
91	\paragraph{Recommended workflow.}
92	\begin{enumerate}[nosep,leftmargin=*]
93	\item Collect $n \geq 25K / P(Z_{\text{minority}})$ stratified expert labels (e.g., $n \geq 500$ for $K{=}4$, $P(Z{=}1){=}0.2$); compute per-subgroup $\pi_s$ and $\bar{\pi}$.
94	\item Verify (a)~$n_{\text{expert}} \times P(Z_{\text{minority}}) / K \geq 25$ and (b)~worst-subgroup $\max(\text{FPR}, \text{FNR}) < 0.5$; if either fails, use global correction.
95	\item If any subgroup satisfies $|\delta_s| / ((1-2\bar{\pi}) \cdot \pi_s) > 1$ (Proposition~\ref{prop:debiasing_hurts}), apply EC-HTE; apply PPCI regardless for outcome error (Appendix~\ref{sec:ppci}).
96	\end{enumerate}
97	
98	Expert budget crossover analysis and PPCI composition results appear in Appendix~\ref{app:budget} and~\ref{app:ppci}, respectively.
99	
100	\subsection{Open-Source Multi-LLM Validation}
101	\label{sec:multilm_opensource}
102	
103	To verify that misclassification heterogeneity and EC-HTE's correction generalize beyond proprietary APIs, we annotate 500 TweetEval sentiment tweets with four open-source LLMs: Llama-3.1-8B-Instruct, Qwen2.5-7B-Instruct, Mistral-7B-Instruct-v0.3, and Gemma-2-9B-IT.
104	Each model independently classifies tweets using a 3-class prompt (positive/neutral/negative); we define a balanced binary label $Z{=}1$ if the true label $\geq 1$ (neutral or positive vs.\ negative), yielding $P(Z{=}1) \approx 0.65$.
105	Per-subgroup confusion matrices are estimated directly from each model's annotations against gold labels.
106	The EC-HTE pipeline---HB confusion matrix estimation followed by CausalForestDML---is identical to the synthetic experiments in Table~\ref{tab:main_results}.
107	All four models exhibit subgroup-heterogeneous misclassification ($\Delta\pi \in [0.125, 0.165]$, $K{=}4$), with consistent subgroup error rankings across architectures (Table~\ref{tab:multilm_cm}).
108	Correction improves 95\% CI coverage from 0.714 (naive average) to 0.939 ($+$22.5 percentage points, $K{=}2$, $n_{\text{expert}}{=}1{,}000$), restoring near-nominal inference across all four models.
109	Under the moderate $\Delta\pi$ observed in these real LLM annotations, global correction suffices for RMSE.
110	Stratified correction achieves lower RMSE than the naive estimator only at $n_{\text{expert}} \geq 1{,}000$ ($K{=}2$); global correction achieves comparable or lower RMSE than HB EC-HTE at all budgets under this moderate heterogeneity, consistent with the budget guidelines in Appendix~\ref{sec:budget}.
111	Full per-model results appear in Appendix~\ref{app:multilm_opensource}.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e3ca5928-af5c-4cd8-8543-4c735d6cc926",
  "isSidechain": true,
  "promptId": "410c5182-a00d-45c3-a02c-4785eb40bb89",
  "agentId": "a217013802bf0fe69",
  "type": "user",
  "uuid": "7cc82cb5-3168-4714-b3e8-a396c8f7211a",
  "sourceToolAssistantUUID": "e3ca5928-af5c-4cd8-8543-4c735d6cc926",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/paper_agent_8babce27",
  "sessionId": "6ae78efb-2b23-4404-a761-5afc621a128d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "zazzy-giggling-simon"
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-22T05:42:46.507Z_

Perfect! Now let me check the appendix structure again more carefully, particularly around the multilm_opensource label and looking for the end of the file:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7cc82cb5-3168-4714-b3e8-a396c8f7211a",
  "isSidechain": true,
  "agentId": "a217013802bf0fe69",
  "requestId": "req_011CbH5F5Xm7HEv6ohavQzM2",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "fa9ad3a6-00c9-4750-a3d2-1eb747544ca3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/paper_agent_8babce27",
  "sessionId": "6ae78efb-2b23-4404-a761-5afc621a128d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "zazzy-giggling-simon",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01KE1Eu22JzmxLcYL5msofmF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 4306,
      "cache_read_input_tokens": 50342,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4306,
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

_source line 20 · 2026-05-22T05:42:47.363Z_

<details open><summary>🔧 Tool call — Read · `toolu_01N9aJko8JhXymzu8kLH2DfU`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex",
  "offset": 400,
  "limit": 370
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fa9ad3a6-00c9-4750-a3d2-1eb747544ca3",
  "isSidechain": true,
  "agentId": "a217013802bf0fe69",
  "requestId": "req_011CbH5F5Xm7HEv6ohavQzM2",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "9546f562-3bab-4a7b-823b-8ebd5edc7c78",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/paper_agent_8babce27",
  "sessionId": "6ae78efb-2b23-4404-a761-5afc621a128d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "zazzy-giggling-simon",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01KE1Eu22JzmxLcYL5msofmF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 4306,
      "cache_read_input_tokens": 50342,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4306,
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

_source line 21 · 2026-05-22T05:42:47.401Z_

<details><summary>↩ Tool result · `toolu_01N9aJko8JhXymzu8kLH2DfU`</summary>

```text
400	\section{Cross-Model Consistency}
401	\label{app:multilm}
402	
403	We evaluate whether misclassification heterogeneity is model-specific by annotating 500 TweetEval sentiment tweets with six OpenAI models spanning three generations.
404	Six text-feature subgroups are defined by crossing hashtag presence and text length.
405	Spearman rank correlations of per-subgroup error rates across all six subgroups range from $\rho = 0.82$ to $1.00$, indicating that the subgroup error structure is consistent across architectures.
406	Two subgroups with $n \leq 6$ exhibit zero misclassification across all models; excluding these yields four-point correlations that are directionally consistent but underpowered.%
407	\footnote{The filtered $\Delta\pi$ values in Table~\ref{tab:multilm} serve as a robustness check independent of rank-order testing: all six models exceed $\Delta\pi > 0.05$ on the four retained subgroups.}
408	
409	\begin{table}[t]
410	\centering
411	\caption{Effective misclassification heterogeneity ($\Delta\pi$) across six OpenAI models on TweetEval sentiment (500 tweets, filtered to 4 subgroups with $n \geq 10$).}
412	\label{tab:multilm}
413	\small
414	\begin{tabular}{lcc}
415	\toprule
416	Model & Effective $\Delta\pi$ & $> 0.05$? \\
417	\midrule
418	GPT-3.5-Turbo & 0.198 & \checkmark \\
419	GPT-4-Turbo & 0.149 & \checkmark \\
420	GPT-4o-mini & 0.136 & \checkmark \\
421	GPT-5.4 & 0.114 & \checkmark \\
422	GPT-4.1 & 0.098 & \checkmark \\
423	GPT-4o & 0.080 & \checkmark \\
424	\bottomrule
425	\end{tabular}
426	\end{table}
427	
428	All six models exhibit effective $\Delta\pi > 0.05$ on the four retained subgroups (Table~\ref{tab:multilm}), and 5 of 6 share the same worst subgroup (\texttt{True\_medium}: tweets with hashtags and medium text length).
429	Newer models reduce absolute error rates but do not eliminate subgroup heterogeneity: GPT-5.4 achieves $\Delta\pi = 0.114$ compared to GPT-3.5-Turbo's $0.198$.
430	These results were obtained with a single API provider; open-source model validation appears in Appendix~\ref{app:multilm_opensource}.
431	
432	\section{Open-Source Multi-LLM Validation}
433	\label{app:multilm_opensource}
434	
435	We evaluate four open-source LLMs (7B--9B parameter range) on 490 TweetEval sentiment tweets with $K{=}4$ subgroups defined by crossing hashtag presence and text length.
436	Table~\ref{tab:multilm_cm} reports the confusion matrix heterogeneity profile.
437	All four models exhibit $\Delta\pi > 0.05$, confirming that subgroup-heterogeneous misclassification is not specific to proprietary APIs.
438	Subgroup error rankings are consistent across architectures: \texttt{True\_short} (short tweets with hashtags) has the lowest $\pi_s$ in 3 of 4 models, while \texttt{False\_medium} (medium tweets without hashtags) has the highest.
439	
440	\begin{table}[t]
441	\centering
442	\caption{Confusion matrix heterogeneity across four open-source LLMs ($K{=}4$, $N{=}490$ TweetEval tweets). $\Delta\pi$: max--min per-subgroup misclassification rate. Prop2: number of subgroups where the $\Delta\tau$-free diagnostic (Proposition~\ref{prop:debiasing_hurts}) triggers.}
443	\label{tab:multilm_cm}
444	\small
445	\begin{tabular}{lcccl}
446	\toprule
447	Model & Acc.\ & $\Delta\pi$ & Prop2 & Strongest \\
448	\midrule
449	Llama-3.1-8B & 0.755 & 0.141 & 1/4 & True\_short \\
450	Qwen-2.5-7B & 0.798 & 0.165 & 1/4 & True\_short \\
451	Gemma-2-9B & 0.763 & 0.125 & 4/4 & True\_medium \\
452	Mistral-7B & 0.802 & 0.134 & 0/4 & --- \\
453	\bottomrule
454	\end{tabular}
455	\end{table}
456	
457	\paragraph{Semi-synthetic budget sweep.}
458	We run the full EC-HTE pipeline with $K{=}2$ subgroups and $\Delta\tau{=}0.3$, using each model's empirical confusion matrices.
459	Table~\ref{tab:multilm_budget} reports coverage and RMSE crossover points.
460	EC-HTE restores near-nominal coverage from 0.714 (naive average) to 0.939 ($+$22.5 percentage points) at $n_{\text{expert}}{=}1{,}000$, consistent across all four models.
461	Global correction achieves comparable or lower RMSE than HB at all budgets under these moderate $\Delta\pi$ values, and the $K{=}4$ RMSE crossover never occurs---confirming the budget guidelines in Appendix~\ref{sec:budget}.
462	
463	\begin{table}[t]
464	\centering
465	\caption{Semi-synthetic budget sweep ($K{=}2$, $\Delta\tau{=}0.3$, 50 MC runs). Coverage at selected expert budgets; RMSE crossover denotes the minimum expert budget at which HB EC-HTE achieves lower RMSE than the naive (uncorrected) estimator.}
466	\label{tab:multilm_budget}
467	\small
468	\begin{tabular}{lcccc}
469	\toprule
470	Model & $\Delta\pi_{K{=}2}$ & Naive Cov.\ & HB Cov.\ ($n{=}1000$) & Crossover \\
471	\midrule
472	Llama-3.1-8B & 0.051 & 0.675 & 0.940 & $n{=}1000$ \\
473	Qwen-2.5-7B & 0.080 & 0.715 & 0.925 & $n{=}1000$ \\
474	Gemma-2-9B & 0.100 & 0.705 & 0.945 & $n{=}1000$ \\
475	Mistral-7B & 0.070 & 0.760 & 0.945 & $n{=}1000$ \\
476	\midrule
477	\textit{Average} & --- & \textit{0.714} & \textit{0.939} & --- \\
478	\bottomrule
479	\end{tabular}
480	\end{table}
481	
482	\paragraph{Gemma boundary case.}
483	Gemma-2-9B triggers the Proposition~\ref{prop:debiasing_hurts} diagnostic in all four $K{=}4$ subgroups due to extreme FPR--FNR asymmetry (\texttt{False\_medium} FNR $= 0.437$).
484	At small budgets ($K{=}4$, $n{=}100$), EC-HTE RMSE reaches 1.229 ($3.1\times$ naive), illustrating the budget guideline from Appendix~\ref{sec:budget}: when per-subgroup cell counts fall below 25, the variance cost of stratified correction dominates.
485	At $n \geq 500$, EC-HTE coverage recovers to $>$0.90, consistent with the synthetic experiments.
486	
487	\paragraph{Heterogeneous-$\tau$ DGP.}
488	To assess whether the constant-$\tau$ DGP understates EC-HTE's advantage, we run a supplementary experiment using Llama's empirical confusion matrices with heterogeneous treatment effects across subgroups ($\Delta\tau \in [0.1, 0.6]$, $K{=}2$, 50 MC runs).
489	EC-HTE achieves lower $|\text{bias}|$ than global correction at all budgets ($n{=}500$: 0.010 vs.\ 0.031, a 68\% reduction).
490	In the high-$\Delta\tau$ subgroup (\texttt{True\_short}, $\Delta\tau{=}0.6$), EC-HTE also achieves lower RMSE ($n{=}1{,}000$: 0.212 vs.\ 0.258, 18\% improvement), confirming that the RMSE advantage concentrates in subgroups where correction is most needed.
491	Aggregate RMSE remains comparable to global correction because low-$\Delta\tau$ subgroups incur stratification variance without commensurate bias reduction, consistent with the budget guidelines in Appendix~\ref{sec:budget}.
492	
493	\section{Robustness to Subgroup Misspecification}
494	\label{app:robustness}
495	
496	EC-HTE requires pre-defined subgroup labels, which may be noisy in practice.
497	We test robustness by randomly flipping each observation's subgroup assignment with probability $p_{\text{flip}} \in \{0, 0.10, 0.25, 0.50\}$, across $K \in \{2, 4\}$ (extreme regime, $n_{\text{expert}} = 500$, $\Delta\tau = 0.3$, 100 MC runs).
498	
499	\begin{table}[t]
500	\centering
501	\caption{95\% CI coverage under subgroup misspecification noise. EC-HTE maintains near-nominal coverage across all noise levels.}
502	\label{tab:robustness}
503	\small
504	\begin{tabular}{lcccc}
505	\toprule
506	& \multicolumn{4}{c}{$p_{\text{flip}}$} \\
507	\cmidrule(lr){2-5}
508	Method & 0.00 & 0.10 & 0.25 & 0.50 \\
509	\midrule
510	\multicolumn{5}{l}{\textit{$K{=}2$, extreme}} \\
511	\quad Naive & 0.875 & 0.877 & 0.890 & 0.897 \\
512	\quad Global & 0.925 & 0.935 & 0.932 & 0.945 \\
513	\quad HB EC-HTE & 0.958 & 0.948 & 0.950 & 0.945 \\
514	\midrule
515	\multicolumn{5}{l}{\textit{$K{=}4$, extreme}} \\
516	\quad Naive & 0.904 & 0.916 & 0.909 & 0.919 \\
517	\quad Global & 0.930 & 0.953 & 0.948 & 0.944 \\
518	\quad HB EC-HTE & 0.956 & 0.958 & 0.960 & 0.946 \\
519	\bottomrule
520	\end{tabular}
521	\end{table}
522	
523	EC-HTE maintains coverage $\geq 0.945$ across all configurations (Table~\ref{tab:robustness}), while the naive estimator is systematically below nominal (0.875--0.919).
524	At $p_{\text{flip}} = 0.50$, subgroup structure is effectively destroyed; EC-HTE converges to global correction (coverage and RMSE within 0.1\%), confirming that hierarchical Bayesian shrinkage provides a built-in safety mechanism.
525	For $K{=}4$ at $p_{\text{flip}} = 0.50$, a small residual RMSE gap persists ($p < 0.01$), reflecting the variance cost of estimating four confusion matrices even when they carry no signal.
526	
527	\section{Monte Carlo Standard Errors}
528	\label{app:mcse}
529	
530	All experiments use 100 independent Monte Carlo replications per configuration.
531	All simulation results were verified with 100 MC seeds; the median RMSE variation between 50-seed and 100-seed estimates is below 3.2\%, confirming the stability of reported figures.
532	We report Monte Carlo standard errors to assess whether observed differences between methods are statistically reliable.
533	For exp-001 (synthetic DGP, no per-seed pairing across methods), we use conservative two-sample $z$-tests on the 100-run means.
534	For exp-003 (semi-synthetic TweetEval, shared seeds across methods), we use paired $t$-tests, which are more powerful because they control for seed-level variation.
535	
536	Table~\ref{tab:mcse} reports paired comparisons for representative configurations.
537	Of 1{,}020 total pairwise comparisons across all configurations, 742 (72.7\%) are statistically significant at $\alpha = 0.05$.
538	
539	\begin{table}[t]
540	\centering
541	\caption{Paired comparisons for representative configurations. $\Delta$ = method A $-$ method B (negative favors A for $|\text{bias}|$). Two-sample $z$-tests for synthetic (exp-001); paired $t$-tests for semi-synthetic (exp-003). Bold $p$-values indicate significance at $\alpha = 0.05$.}
542	\label{tab:mcse}
543	\small
544	\begin{tabular}{llrr}
545	\toprule
546	Configuration & Comparison & $\Delta$ & $p$ \\
547	\midrule
548	\multicolumn{4}{l}{\textit{HB EC-HTE vs.\ Global ($|\text{bias}|$)}} \\
549	\quad $K{=}2$/ext/$n{=}500$ & & $-0.046$ & $\mathbf{<0.001}$ \\
550	\quad $K{=}4$/ext/$n{=}500$ & & $-0.078$ & $\mathbf{<0.001}$ \\
551	\quad $K{=}4$/mod/$n{=}250$ & & $-0.017$ & $0.288$ \\
552	\quad TweetEval/ext/$n{=}250$ & & $+0.001$ & $0.395$ \\
553	\midrule
554	\multicolumn{4}{l}{\textit{HB EC-HTE vs.\ Global (RMSE)}} \\
555	\quad $K{=}2$/ext/$n{=}500$ & & $+0.015$ & $0.179$ \\
556	\quad $K{=}4$/ext/$n{=}500$ & & $+0.048$ & $\mathbf{0.011}$ \\
557	\midrule
558	\multicolumn{4}{l}{\textit{HB EC-HTE vs.\ Naive ($|\text{bias}|$)}} \\
559	\quad $K{=}2$/ext/$n{=}500$ & & $-0.089$ & $\mathbf{<0.001}$ \\
560	\quad $K{=}4$/ext/$n{=}500$ & & $-0.113$ & $\mathbf{<0.001}$ \\
561	\quad $K{=}4$/mod/$n{=}250$ & & $-0.031$ & $\mathbf{0.038}$ \\
562	\quad TweetEval/ext/$n{=}250$ & & $+0.005$ & $\mathbf{0.030}$ \\
563	\bottomrule
564	\end{tabular}
565	\end{table}
566	
567	Under extreme heterogeneity, HB EC-HTE's bias advantage over global correction is highly significant ($p < 0.001$ for both $K{=}2$ and $K{=}4$).
568	The RMSE penalty of stratification is not significant at $K{=}2$ ($p = 0.179$) but reaches significance at $K{=}4$ ($p = 0.011$), consistent with the higher variance cost of estimating four confusion matrices.
569	Under moderate heterogeneity ($K{=}4$, $n{=}250$), the bias difference between HB and global is not significant ($p = 0.288$), confirming that EC-HTE's advantage requires sufficient error heterogeneity.
570	In the semi-synthetic TweetEval experiment, HB EC-HTE does not significantly improve over global ($p = 0.395$), consistent with moderate $\Delta\pi$ and unbalanced subgroup sizes.
571	The HB vs.\ naive comparison in TweetEval is significant ($p = 0.030$) but favors naive, reflecting the variance cost of stratification when bias reduction is marginal.
572	
573	\section{Semi-Real Confusion Matrix Validation}
574	\label{app:semireal}
575	
576	We test EC-HTE with empirical asymmetric confusion matrices from the GPT-4.1 TweetEval pilot.
577	Four text-feature subgroups ($K{=}4$) retain the real per-subgroup FPR and FNR from pilot annotations (Table~\ref{tab:semireal_cm}); CATE heterogeneity is injected synthetically ($\tau(z{=}0,s) = 0.3 + 0.1s$, $\tau(z{=}1,s) = 0.8 - 0.15s$).
578	$N{=}5{,}000$, $P(Z{=}1){=}0.18$, 100 MC seeds per $n_{\text{expert}}$ level.
579	
580	\begin{table}[t]
581	\centering
582	\caption{Empirical confusion matrices from GPT-4.1 TweetEval pilot.
583	S0 exhibits FNR $= 0.526$, approaching chance-level classification.}
584	\label{tab:semireal_cm}
585	\small
586	\begin{tabular}{lcccc}
587	\toprule
588	Subgroup & Weight & FPR & FNR & $\kappa(\hat{C}_s)$ \\
589	\midrule
590	S0 & 0.38 & 0.054 & 0.526 & high \\
591	S1 & 0.22 & 0.101 & 0.300 & moderate \\
592	S2 & 0.14 & 0.143 & 0.308 & moderate \\
593	S3 & 0.25 & 0.194 & 0.222 & low \\
594	\bottomrule
595	\end{tabular}
596	\end{table}
597	
598	\begin{table}[t]
599	\centering
600	\caption{Semi-real confusion matrix results. RMSE and coverage averaged over subgroups and $z$-levels (100 MC runs). HB EC-HTE underperforms global at all budgets; S0's near-chance FNR drives the failure.}
601	\label{tab:semireal}
602	\small
603	\begin{tabular}{llcc}
604	\toprule
605	$n_{\text{expert}}$ & Method & RMSE $\downarrow$ & Coverage $\uparrow$ \\
606	\midrule
607	\multirow{4}{*}{100}
608	 & Oracle & 0.101 & 0.957 \\
609	 & Naive & 0.123 & 0.879 \\
610	 & Global & 0.263 & 0.885 \\
611	 & HB EC-HTE & 0.784 & 0.744 \\
612	\midrule
613	\multirow{4}{*}{250}
614	 & Oracle & 0.101 & 0.957 \\
615	 & Naive & 0.123 & 0.879 \\
616	 & Global & 0.232 & 0.909 \\
617	 & HB EC-HTE & 0.411 & 0.834 \\
618	\midrule
619	\multirow{4}{*}{500}
620	 & Oracle & 0.101 & 0.957 \\
621	 & Naive & 0.123 & 0.879 \\
622	 & Global & 0.196 & 0.922 \\
623	 & HB EC-HTE & 0.260 & 0.890 \\
624	\bottomrule
625	\end{tabular}
626	\end{table}
627	
628	HB EC-HTE produces higher RMSE and lower coverage than global correction at all expert budgets (Table~\ref{tab:semireal}).
629	The root cause is S0's FNR $= 0.526$: when a confusion matrix row approaches a uniform distribution ($P(\hat{Z}{=}1 \mid Z{=}1) \approx 0.5$), inversion amplifies estimation noise regardless of the expert budget.
630	This converges with the hate speech case study (Appendix~\ref{app:hatespeech}, FNR $= 53.3$\%) and confirms that EC-HTE requires \emph{both} sufficient expert labels \emph{and} sufficient baseline classifier quality per subgroup.
631	The singularity guard ($\kappa > 100$, Section~\ref{sec:method}) mitigates catastrophic failure by falling back to global correction for near-degenerate subgroups, but does not recover the bias reduction that motivates stratification.
632	At $n_{\text{expert}} = 500$, HB EC-HTE narrows the gap (RMSE 0.260 vs.\ 0.196) as confusion matrix estimates stabilize for the three well-classified subgroups, but the S0 bottleneck persists.
633	
634	A second semi-real experiment using GPT-3.5-Turbo confusion matrices (worst-subgroup FPR $= 0.39$, FNR $= 0.21$) yields similar results: HB RMSE exceeds global by 1.3--3.5$\times$ at all budgets.
635	Here the failure stems from high false-positive rates compounded by class imbalance ($P(Z{=}1) = 0.18$), which leaves insufficient expert observations in the positive class for reliable per-subgroup confusion matrix estimation.
636	Together, these experiments identify three applicability conditions for EC-HTE: (1)~sufficient effective expert budget ($n_{\text{expert}} \times P(Z_{\text{minority}}) / K \geq 25$), (2)~no near-chance subgroup error rate ($\max(\text{FPR}_s, \text{FNR}_s) < 0.5$), and (3)~adequate class balance in the effect modifier.
637	
638	\paragraph{Diagnostic rule.}
639	A logistic regression over all 368 semi-real experiment--budget cells (dependent variable: HB EC-HTE $<$ Global RMSE) identifies two sufficient statistics: the worst-subgroup confusion matrix condition number $\kappa(\hat{M}_s) \leq 1.25$ and the effective minority-class expert count $n_{\text{expert}} \times P(Z_{\text{minority}}) / K \geq 25$.
640	When both conditions hold, HB outperforms global in 93.3\% of cells; when either is violated, global is preferred in 94.7\% of cells.
641	Both exp-015 ($\kappa = 2.38$, effective $n = 2.5$) and exp-016 ($\kappa = 1.55$, effective $n = 2.5$) violate both conditions, and the diagnostic correctly predicts 100\% of their failure cells.
642	Subgroup-average metrics can mask cell-level heterogeneity: in exp-015, HB EC-HTE substantially reduces bias for the three well-classified subgroups (S1--S3) but amplifies variance in the near-degenerate subgroup (S0, FNR $= 0.526$), and the S0 penalty dominates the aggregate RMSE.
643	
644	\begin{figure}[t]
645	\centering
646	\includegraphics[width=\columnwidth]{figures/applicability_frontier.pdf}
647	\caption{Applicability frontier of EC-HTE. Green region: EC-HTE reduces bias vs.\ global correction. Yellow: comparable performance. Red: EC-HTE underperforms. Dashed lines mark the expert budget threshold ($n_{\text{expert}}/K = 25$) and classifier quality threshold (worst-subgroup error rate $= 0.5$). Red diamonds show semi-real experiments with actual GPT-4.1 and GPT-3.5-Turbo confusion matrices.}
648	\label{fig:applicability}
649	\end{figure}
650	
651	\section{Robustness: Estimator Choice and Treatment Effect Specification}
652	\label{app:rlearner}
653	
654	We verify that EC-HTE's corrected pseudo-outcomes are compatible with downstream estimators beyond CausalForest by replacing it with the R-learner~\citep{nie2021quasi}.
655	The experiment uses $K{=}2$, extreme heterogeneity, $n_{\text{expert}} = 500$, and 50 MC seeds; the R-learner uses 5-fold cross-fitting with gradient-boosted trees as the base learner.
656	
657	\begin{table}[t]
658	\centering
659	\caption{R-learner vs.\ CausalForest with EC-HTE correction ($K{=}2$, extreme, $n{=}500$). $|\text{Bias}|$ and RMSE averaged over subgroups, $z$-levels, and seeds.}
660	\label{tab:rlearner}
661	\small
662	\begin{tabular}{llccc}
663	\toprule
664	Estimator & Correction & $|\text{Bias}|$ & RMSE & Cov. \\
665	\midrule
666	\multirow{4}{*}{R-learner}
667	 & Oracle & 0.006 & 0.056 & 0.94 \\
668	 & Naive & 0.121 & 0.139 & 0.47 \\
669	 & Global & 0.098 & 0.123 & 0.72 \\
670	 & EC-HTE & \textbf{0.013} & 0.080 & 0.92 \\
671	\midrule
672	\multirow{2}{*}{CausalForest}
673	 & Naive & 0.058 & 0.090 & 0.82 \\
674	 & EC-HTE & \textbf{0.010} & 0.093 & 0.95 \\
675	\bottomrule
676	\end{tabular}
677	\end{table}
678	
679	EC-HTE reduces R-learner $|\text{bias}|$ by 89\% (0.121 $\to$ 0.013) and restores coverage from 0.47 to 0.92 (Table~\ref{tab:rlearner}).
680	The bias reduction and coverage gains are comparable to those achieved with CausalForest, confirming that EC-HTE functions as an estimator-agnostic upstream correction.
681	
682	\paragraph{Multiplicative treatment effects.}
683	We further test robustness to the functional form of treatment effects by replacing the additive DGP with a multiplicative specification: $Y(1) = Y(0) \times \exp(\tau(Z))$, using $K{=}2$, extreme heterogeneity, $n_{\text{expert}} = 500$, and 50 MC seeds.
684	
685	\begin{table}[t]
686	\centering
687	\caption{Multiplicative DGP results ($K{=}2$, extreme, $n{=}500$, 50 seeds). EC-HTE achieves comparable bias reduction and nominal coverage under non-additive treatment effects.}
688	\label{tab:multiplicative}
689	\small
690	\begin{tabular}{lccc}
691	\toprule
692	Method & $|\text{Bias}|$ & RMSE & Cov. \\
693	\midrule
694	Oracle & 0.003 & 0.038 & 0.96 \\
695	Naive & 0.135 & 0.142 & 0.44 \\
696	Global & 0.110 & 0.124 & 0.54 \\
697	EC-HTE & \textbf{0.054} & 0.068 & 0.955 \\
698	\bottomrule
699	\end{tabular}
700	\end{table}
701	
702	EC-HTE reduces RMSE by 52\% relative to naive (0.068 vs.\ 0.142) and restores coverage to the nominal level (0.955; Table~\ref{tab:multiplicative}).
703	EC-HTE's bias correction operates at the confusion matrix level, independent of the downstream CATE estimator and functional form of treatment effects.
704	
705	\section{Robustness to Class Imbalance}
706	\label{app:classimbalance}
707	
708	Assumption (A3) requires $P(Z{=}1) = 0.5$, but real-world effect modifiers are often imbalanced.
709	We sweep $P(Z{=}1) \in \{0.1, 0.2, 0.3, 0.4, 0.5\}$ with $K \in \{2,4\}$, extreme misclassification heterogeneity, $n_{\text{expert}}{=}250$, and 100 MC seeds (Table~\ref{tab:pz1_sweep}).
710	
711	\begin{table}[t]
712	\centering
713	\caption{Robustness to class imbalance ($n_{\text{expert}}{=}250$, extreme heterogeneity). R$^2$: Theorem~\ref{thm:bias_identity} fit. Ratio: HB/Global RMSE ($<1$ = HB wins). Cov.: HB EC-HTE 95\% CI coverage.}
714	\label{tab:pz1_sweep}
715	\small
716	\begin{tabular}{cc ccc}
717	\toprule
718	$P(Z{=}1)$ & $K$ & R$^2$ & Ratio & Cov. \\
719	\midrule
720	0.1 & 2 & 0.998 & 0.92 & 0.94 \\
721	0.2 & 2 & 0.989 & 0.76 & 0.94 \\
722	0.3 & 2 & 0.994 & 0.78 & 0.94 \\
723	0.4 & 2 & 0.995 & 0.87 & 0.94 \\
724	0.5 & 2 & 0.995 & 0.86 & 0.93 \\
725	\midrule
726	0.1 & 4 & 0.984 & 1.54 & 0.92 \\
727	0.2 & 4 & 0.976 & 1.68 & 0.93 \\
728	0.3 & 4 & 0.985 & 1.12 & 0.92 \\
729	0.4 & 4 & 0.984 & 1.08 & 0.93 \\
730	0.5 & 4 & 0.992 & 1.06 & 0.92 \\
731	\bottomrule
732	\end{tabular}
733	\end{table}
734	
735	Theorem~\ref{thm:bias_identity}'s product form remains accurate across all imbalance levels: $R^2 \geq 0.976$ even at $P(Z{=}1) = 0.1$, confirming that the bias identity derives from confusion matrix structure rather than class balance.
736	For $K{=}2$, EC-HTE outperforms global correction at all $P(Z{=}1)$ levels (RMSE ratio 0.76--0.92), degrading gracefully under severe imbalance.
737	For $K{=}4$, EC-HTE underperforms global at $n_{\text{expert}}{=}250$ (ratio 1.06--1.68), consistent with the budget threshold $n_{\text{expert}} \times P(Z_{\text{minority}}) / K \geq 25$: at $P(Z{=}1){=}0.1$, $K{=}4$, each subgroup receives only ${\sim}6$ minority-class labels.
738	The gap narrows as $P(Z{=}1)$ increases (1.54 $\to$ 1.06), and coverage remains stable at 0.92--0.94 across all configurations.
739	
740	\section{Comparison with PPI Correction}
741	\label{app:ppi_comparison}
742	
743	PPI~\cite{angelopoulos2023ppi} constructs confidence intervals by combining a large set of ML predictions with a smaller set of gold-standard labels, using the gold labels to debias the ML-based estimator.
744	Applied to our setting, PPI treats the LLM-annotated effect modifier as the ML prediction and the expert labels as the gold standard.
745	Two variants arise naturally: \emph{PPI-global} pools all expert labels to estimate a single rectifier (analogous to our Global baseline), and \emph{PPI-subgroup} estimates per-subgroup rectifiers (analogous to Stratified MLE).
746	
747	Under the confusion-matrix parameterization we adopt, DSL's measurement error correction reduces to confusion matrix inversion.
748	Pooled DSL applies a single estimated confusion matrix to all subgroups, producing the same corrected label distribution as our Global baseline; per-subgroup DSL estimates a separate confusion matrix for each subgroup and inverts it independently, equivalent to our Stratified MLE.
749	EC-HTE's contribution over both PPI-subgroup and per-subgroup DSL is hierarchical partial pooling: rather than estimating each subgroup's confusion matrix in isolation, EC-HTE places a shared prior across subgroups, borrowing strength to reduce variance while preserving subgroup-specific bias correction.
750	This mechanism is outside both the PPI and DSL frameworks.
751	
752	The key difference between PPI and confusion-matrix inversion is that PPI does not invert the confusion matrix; instead, it uses the gold labels to directly debias the estimand.
753	This avoids the matrix inversion step that can amplify noise at small $n_{\text{expert}}$, but it also means PPI cannot exploit the structure of the misclassification process to reduce bias.
754	PPI-global inherits the same $\Delta\pi \times \Delta\tau$ bias amplification as Global correction (Theorem~\ref{thm:bias_identity}), confirming that the ``debiasing hurts'' mechanism operates regardless of the inference framework.
755	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9546f562-3bab-4a7b-823b-8ebd5edc7c78",
  "isSidechain": true,
  "promptId": "410c5182-a00d-45c3-a02c-4785eb40bb89",
  "agentId": "a217013802bf0fe69",
  "type": "user",
  "uuid": "c20afbc8-10cb-410f-8194-b746f85991c4",
  "sourceToolAssistantUUID": "9546f562-3bab-4a7b-823b-8ebd5edc7c78",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/paper_agent_8babce27",
  "sessionId": "6ae78efb-2b23-4404-a761-5afc621a128d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "zazzy-giggling-simon"
}
```

</details>

---

### Assistant

_source line 22 · 2026-05-22T05:42:57.184Z_

Perfect! Now I have all the information you need. Let me create a comprehensive summary of my findings.

## Summary of Findings

I've found both items you requested. Here are the exact locations and content:

### 1. Main Text §5.5 "Open-Source Multi-LLM Validation"

**File:** `/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/experiments.tex`

**Lines:** 100-111

This section in the main experiments is titled `\subsection{Open-Source Multi-LLM Validation}` with label `\label{sec:multilm_opensource}` and contains:

- Evaluation on 500 TweetEval sentiment tweets with four open-source LLMs (Llama-3.1-8B, Qwen2.5-7B, Mistral-7B, Gemma-2-9B)
- All four models exhibit subgroup-heterogeneous misclassification with $\Delta\pi \in [0.125, 0.165]$ at $K=4$
- Coverage improvement from 0.714 (naive) to 0.939 at $n_{expert}=1,000$ with $K=2$
- Discussion of budget guidelines and consistency with appendix results

### 2. Appendix Structure Around multilm_opensource

**File:** `/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex`

**Key sections in order:**

- **Line 400:** `\section{Cross-Model Consistency}` `\label{app:multilm}` - This is the PRECEDING section (tests six OpenAI models)

- **Line 432-491:** `\section{Open-Source Multi-LLM Validation}` `\label{app:multilm_opensource}` - The main appendix section you're interested in. Contains:
  - Line 435-455: Evaluation details and Table tab:multilm_cm with four open-source models
  - Line 457-480: Semi-synthetic budget sweep subsection with Table tab:multilm_budget
  - Line 482-491: Three subsections on Gemma boundary case, Heterogeneous-tau DGP

- **Line 493:** `\section{Robustness to Subgroup Misspecification}` `\label{app:robustness}` - The NEXT section after multilm_opensource

**End of appendix:** The file continues to line 755 with the last section being `\section{Comparison with PPI Correction}` at line 740 with `\label{app:ppi_comparison}`.

You can safely add a new appendix section after line 754 (the very end of the file) if you need to insert additional content.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c20afbc8-10cb-410f-8194-b746f85991c4",
  "isSidechain": true,
  "agentId": "a217013802bf0fe69",
  "requestId": "req_011CbH5FRGf7WRXEGpGr1KTE",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "af69d0a5-60f1-4ebd-a5cc-54b30e15e833",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/paper_agent_8babce27",
  "sessionId": "6ae78efb-2b23-4404-a761-5afc621a128d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "zazzy-giggling-simon",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_019W5Fw9xQGpUevL3pKD8fYP",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 9443,
      "cache_read_input_tokens": 54648,
      "output_tokens": 676,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 9443
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 676,
          "cache_read_input_tokens": 54648,
          "cache_creation_input_tokens": 9443,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 9443,
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
