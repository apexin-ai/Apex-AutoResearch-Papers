# Research conversation: I need you to do a thorough consistency audit of a LaTeX paper across multiple .tex files. The paper is at /home/ubuntu/

**Characterizing the Detectability Landscape of Iterative Model Collapse (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 78
- **Recorded user turns:** 1
- **Tool calls:** 31
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a0170d1e5ef70ae63.jsonl`
- **Structured JSON:** [`a6f62c77262965cc7936.json`](../../sessions/a6/a6f62c77262965cc7936.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

78 recorded events

### User

_source line 1 · 2026-05-20T19:54:25.501Z_

I need you to do a thorough consistency audit of a LaTeX paper across multiple .tex files. The paper is at /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/

Check these specific items and report ONLY inconsistencies:

1. **"framework" vs "lens"**: The S×R concept should be called "lens" everywhere, NOT "framework". Search all .tex files for "framework" near "S×R" or "Signal" or "Resolution".

2. **"phase transition"**: Our onset should NOT be called "phase transition" in our own claims (ok if citing others' work that uses the term). Search all .tex files.

3. **T=20 data consistency**: Everywhere T=20 is mentioned, verify:
   - α=0.50: PermG 6/8
   - α=0.60: PermG 0/8
   - α=0.75: PermG 6/8
   - α=1.0: PermG 6/8
   - F=449-2947 for diversity pairs, F<2 for mauve pairs

4. **Pythia-1.4B data**: Should be 3/8 (not 0/8) at α=0.50 everywhere, with ECE canary. At α=1.0: seed-dependent (s42: 2/8, s43: 6/8).

5. **Cross-architecture count**: Should be "13 of 15" or "13/15" consistently (87%).

6. **Cascade theory references**: §sec:cascade should be referenced from experiments.tex moment cascade sentence. Check that Theorem and Proposition labels resolve correctly.

7. **"sharp onset" not "phase transition"**: Verify our onset language.

8. **Prop 4 / ECE argument**: Should be described as "qualitative argument", NOT "proved" or "theorem".

9. **15/15 at α≥0.30**: The cascade ordering validation number should be 15/15, not 20/20 or any other number.

10. **TY footnotes**: All TY data should carry "directional assignment under verification" markers.

Read method.tex, experiments.tex, discussion.tex, appendix.tex, introduction.tex, abstract.tex, and conclusion.tex (if it exists and is included). Report each inconsistency with file:line and the problematic text.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "df7610aa-ce16-48cc-8465-cca12edac9f8",
  "agentId": "a0170d1e5ef70ae63",
  "type": "user",
  "uuid": "cb31ae62-214f-4a20-9880-903a850f5ba4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/paper_agent_73c709c0",
  "sessionId": "71c5797e-c964-4419-a009-2e487a4de1fc",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "ancient-greeting-comet"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-20T19:54:26.989Z_

I'll conduct a thorough consistency audit of the LaTeX paper. Let me start by reading all the relevant .tex files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cb31ae62-214f-4a20-9880-903a850f5ba4",
  "isSidechain": true,
  "agentId": "a0170d1e5ef70ae63",
  "requestId": "req_011CbEQaDD6sw6QCWKY9KJTk",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "3b89f0b5-c960-4795-a110-5dc45f32e3ab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/paper_agent_73c709c0",
  "sessionId": "71c5797e-c964-4419-a009-2e487a4de1fc",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "ancient-greeting-comet",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_015X3qZaj4ezAnUsJJ7TSQfM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 28203,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 28203,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
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

_source line 3 · 2026-05-20T19:54:27.107Z_

<details open><summary>🔧 Tool call — Glob · `toolu_0156TLGRW5SiKF1uzgD4ydKt`</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3b89f0b5-c960-4795-a110-5dc45f32e3ab",
  "isSidechain": true,
  "agentId": "a0170d1e5ef70ae63",
  "requestId": "req_011CbEQaDD6sw6QCWKY9KJTk",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "521e2031-0c62-4c90-a5d4-19cf7a36a87b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/paper_agent_73c709c0",
  "sessionId": "71c5797e-c964-4419-a009-2e487a4de1fc",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "ancient-greeting-comet",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_015X3qZaj4ezAnUsJJ7TSQfM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 28203,
      "cache_read_input_tokens": 0,
      "output_tokens": 113,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 28203
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 113,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 28203,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 28203,
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

_source line 4 · 2026-05-20T19:54:27.129Z_

<details><summary>↩ Tool result · `toolu_0156TLGRW5SiKF1uzgD4ydKt`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/ethics.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/background.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/discussion_reframe.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/intro_reframe.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments_reframe.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method_reframe.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/related_work_reframe.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "521e2031-0c62-4c90-a5d4-19cf7a36a87b",
  "isSidechain": true,
  "promptId": "df7610aa-ce16-48cc-8465-cca12edac9f8",
  "agentId": "a0170d1e5ef70ae63",
  "type": "user",
  "uuid": "7e082ca2-3880-467c-b69a-bdb1c60abd32",
  "sourceToolAssistantUUID": "521e2031-0c62-4c90-a5d4-19cf7a36a87b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/paper_agent_73c709c0",
  "sessionId": "71c5797e-c964-4419-a009-2e487a4de1fc",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "ancient-greeting-comet"
}
```

</details>

---

### Assistant

_source line 5 · 2026-05-20T19:54:28.336Z_

Now let me read the key .tex files in parallel:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7e082ca2-3880-467c-b69a-bdb1c60abd32",
  "isSidechain": true,
  "agentId": "a0170d1e5ef70ae63",
  "requestId": "req_011CbEQaKoUtsmgNdefgRCeK",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "877a9785-de15-4dac-b9bd-8f4fcecfb880",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/paper_agent_73c709c0",
  "sessionId": "71c5797e-c964-4419-a009-2e487a4de1fc",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "ancient-greeting-comet",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01FANF2saRyeceraWkZcxsuN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1624,
      "cache_read_input_tokens": 28203,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1624,
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

_source line 6 · 2026-05-20T19:54:28.586Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Y4z86fzPTUt2YbGWvS2YuS`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "877a9785-de15-4dac-b9bd-8f4fcecfb880",
  "isSidechain": true,
  "agentId": "a0170d1e5ef70ae63",
  "requestId": "req_011CbEQaKoUtsmgNdefgRCeK",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "da503516-1b87-4df2-a575-9869a0fa6356",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/paper_agent_73c709c0",
  "sessionId": "71c5797e-c964-4419-a009-2e487a4de1fc",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "ancient-greeting-comet",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01FANF2saRyeceraWkZcxsuN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1624,
      "cache_read_input_tokens": 28203,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1624,
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

_source line 7 · 2026-05-20T19:54:28.600Z_

<details><summary>↩ Tool result · `toolu_01Y4z86fzPTUt2YbGWvS2YuS`</summary>

```text
1	\begin{abstract}
2	In iterative training on synthetic data, Granger-causal detection of collapse undergoes a \emph{sharp detection onset}: permutation Granger causality (PermG) jumps from 0/8 to 6/8 FDR-significant canary-downstream pairs at a critical per-generation mixing ratio $\alpha_c{=}0.476$ (Fisher exact $p < 10^{-10}$), establishing that detectability is governed by per-generation mixing ratio, not cumulative contamination.
3	A signal-times-resolution ($S \times R$) interpretive lens explains the resulting non-monotonic dose-response through competing signal strength and temporal resolution.
4	A multi-method consensus test comparing five statistical methods reveals that method choice alone inflates null-control FPR to 75\%; first-differencing eliminates all canary$\to$perplexity associations while preserving canary$\to$diversity leads, scoping the canary claim to diversity metrics only.
5	Cross-architecture validation across six model families (345M--6.9B) confirms detection in 87\% of 15 conditions.
6	A proof-of-concept predictive cessation protocol reduces peak perplexity by 58\%.
7	\end{abstract}
8	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "da503516-1b87-4df2-a575-9869a0fa6356",
  "isSidechain": true,
  "promptId": "df7610aa-ce16-48cc-8465-cca12edac9f8",
  "agentId": "a0170d1e5ef70ae63",
  "type": "user",
  "uuid": "b68cec43-476e-4f8d-ae0c-2615f9723dea",
  "sourceToolAssistantUUID": "da503516-1b87-4df2-a575-9869a0fa6356",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/paper_agent_73c709c0",
  "sessionId": "71c5797e-c964-4419-a009-2e487a4de1fc",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "ancient-greeting-comet"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-20T19:54:28.792Z_

<details open><summary>🔧 Tool call — Read · `toolu_01ED6BeBGrkRn4jF97FMe5Yu`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b68cec43-476e-4f8d-ae0c-2615f9723dea",
  "isSidechain": true,
  "agentId": "a0170d1e5ef70ae63",
  "requestId": "req_011CbEQaKoUtsmgNdefgRCeK",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "a30cf41d-13d3-46f8-9b51-9267ccccc8d2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/paper_agent_73c709c0",
  "sessionId": "71c5797e-c964-4419-a009-2e487a4de1fc",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "ancient-greeting-comet",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01FANF2saRyeceraWkZcxsuN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1624,
      "cache_read_input_tokens": 28203,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1624,
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

_source line 9 · 2026-05-20T19:54:28.798Z_

<details><summary>↩ Tool result · `toolu_01ED6BeBGrkRn4jF97FMe5Yu`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	When language models train iteratively on their own output, the training distribution progressively loses its tail modes, a phenomenon termed model collapse~\cite{shumailov2024curse,alemohammad2024mad}.
5	Lexical diversity narrows, calibration deteriorates, and each generation inherits the systematic biases of its predecessors.
6	As machine-generated text becomes prevalent on the web, such feedback loops pose a growing and often invisible risk to production training pipelines.
7	By the time standard quality metrics register degradation, the underlying distribution may have already shifted irreversibly.
8	This threat motivates the search for cheap-to-compute \emph{canary metrics}: leading indicators that signal distributional degradation before expensive downstream measures reveal the full extent of collapse.
9	The concept parallels early-warning signals for critical transitions in ecological systems~\cite{scheffer2009early,scheffer2012anticipating}, where proxy indicators allow intervention before a tipping point.
10	
11	Yet a fundamental question remains unanswered: \emph{at what contamination level does Granger-causal detection (temporal predictive precedence, not true causation) of collapse become possible?}
12	Whether a candidate canary genuinely \emph{precedes} downstream degradation or merely correlates with it under shared non-stationary trends depends on contamination regime and statistical method in ways that existing analyses leave unresolved.
13	Iterative training produces short, noisy time series (often fewer than 15 points per generation sequence), where detection power drops sharply and false positive rates can be high~\cite{boettiger2012limits}.
14	
15	We identify four methodological gaps in existing detection and monitoring analyses of iterative collapse.
16	(1)~No differencing tests rule out spurious regression from shared non-stationary trends~\cite{granger1974spurious}.
17	(2)~Conclusions rest on a single statistical method whose assumptions about stationarity and directionality are rarely examined.
18	(3)~No FDR correction guards against spurious findings when testing many metric pairs simultaneously.
19	(4)~No regime-dependent analysis is performed, despite the possibility that the same test yields opposite conclusions at different contamination levels.
20	Theoretical characterizations of collapse mechanisms~\cite{shumailov2024curse,dohmatob2025strong} address complementary questions---when and why collapse occurs---rather than when it becomes statistically detectable from finite time-series data.
21	
22	We discover a \emph{sharp detection onset} in canary-based monitoring of iterative collapse---a steep transition in statistical detectability at a critical mixing ratio.
23	Using Pythia-410M~\cite{biderman2023pythia} across thirteen contamination levels ($\alpha \in [0, 1]$, thirteen values from 0.00 to 1.00) and up to four random seeds, we show that Granger-causal detectability undergoes a steep onset at per-generation mixing ratio $\alpha_c{=}0.476$ at $T{=}10$ generations (sigmoid $R^2{=}0.969$, $\Delta\alpha{\approx}0.02$): permutation Granger causality (PermG) jumps from 0/8 FDR-significant metric pairs at $\alpha{\leq}0.45$ to 6/8 at $\alpha{=}0.50$.
24	A signal-times-resolution ($S \times R$) interpretive lens explains this onset and the non-monotonic dose-response through competing signal strength and temporal resolution.
25	A multi-method consensus framework (MMCT) comparing five statistical methods reveals that method choice alone can shift conclusions on the same data from universal significance to complete null.
26	Cross-architecture validation across 15 model-seed combinations spanning six families (345M--6.9B) confirms PermG detection (${\geq}6/8$) in 13 cases (87\%).
27	Granger precedence in our framework establishes temporal predictive improvement, not true causality~\cite{shojaie2022granger}; our canary claim is scoped to diversity metrics (distinct-$n$~\cite{li2016diversity}), not model collapse broadly.
28	
29	Our contributions are:
30	\begin{enumerate}
31	    \item \textbf{Sharp detection onset} (\S\ref{sec:regime}).
32	    At $T{=}10$, PermG jumps from 0/8 FDR-significant pairs through $\alpha{=}0.45$ to 6/8 at $\alpha{=}0.50$ ($\alpha_c{=}0.476$, sigmoid $R^2{=}0.969$, $\Delta\alpha{\approx}0.02$), with a four-regime structure: \emph{blind}, \emph{onset}, \emph{synchronous dip}, and \emph{detection}.
33	    At $\alpha{=}0.10$, a canary blind spot emerges: diversity has already collapsed but canary metrics remain indistinguishable from the null.
34	    Cross-architecture validation across 15 model-seed combinations confirms detection in 13 cases (87\%).
35	
36	    \item \textbf{Signal-times-resolution interpretive lens} (\S\ref{sec:theory}).
37	    A power interpretation formalizes the onset as $\mathrm{Power}(\alpha, T) = \Phi(S \cdot R \cdot \sqrt{T}/\sigma)$; sub-threshold PermG $p$-values at $\alpha{=}0.45$ ($p{=}0.059$--$0.091$) are consistent with proximity to the power boundary. The resulting $T{=}20$ predictions are evaluated in \S\ref{sec:discussion}.
38	
39	    \item \textbf{Multi-method diagnostic toolkit} (\S\ref{sec:method}).
40	    The MMCT exposes three pitfalls: naive cross-correlation has 75\% null-control FPR ($\kappa{=}0.185$ inter-method), first-differencing eliminates canary$\to$perplexity associations entirely while preserving all canary$\to$diversity leads (24/24$\to$24/24), and regime dependence causes the same test to shift from 0--6/8 FDR-significant pairs per seed at $\alpha{\geq}0.75$ to 0/8 at $\alpha{\leq}0.45$.
41	    PermG identifies token entropy as a one-generation-ahead canary for diversity collapse (24/24 forward, 0/24 reverse).
42	
43	\end{enumerate}
44	We additionally present a proof-of-concept intervention protocol (\S\ref{sec:intervention}) illustrating how canary signals could be operationalized: predictive cessation reduces peak perplexity by 58\% (bootstrap 95\% CI: 29--64\%) and fires one generation earlier than reactive cessation.
45	
46	\begin{figure*}[t]
47	\centering
48	\includegraphics[width=0.9\textwidth]{figures/fig_dose_response.pdf}
49	\caption{PermG forward detection rate across 13 contamination levels (Pythia-410M, fp32, direction-checked). Four regimes emerge: blind ($\alpha \leq 0.45$, 0/8), onset ($\alpha{=}0.50$, 6/8), synchronous dip ($\alpha{=}0.60$, 0/8), and detection ($\alpha \geq 0.75$, 0--6/8). The steep onset at $\alpha_c{=}0.476$ is detailed in \S\ref{sec:dose_response}.}
50	\label{fig:regime_map}
51	\end{figure*}
52	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a30cf41d-13d3-46f8-9b51-9267ccccc8d2",
  "isSidechain": true,
  "promptId": "df7610aa-ce16-48cc-8465-cca12edac9f8",
  "agentId": "a0170d1e5ef70ae63",
  "type": "user",
  "uuid": "9321ebb2-4345-42a0-8e02-c45c9d19bf75",
  "sourceToolAssistantUUID": "a30cf41d-13d3-46f8-9b51-9267ccccc8d2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/paper_agent_73c709c0",
  "sessionId": "71c5797e-c964-4419-a009-2e487a4de1fc",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "ancient-greeting-comet"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-20T19:54:29.028Z_

<details open><summary>🔧 Tool call — Read · `toolu_01MatVL5oZUn28yy53qSmman`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9321ebb2-4345-42a0-8e02-c45c9d19bf75",
  "isSidechain": true,
  "agentId": "a0170d1e5ef70ae63",
  "requestId": "req_011CbEQaKoUtsmgNdefgRCeK",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "6fbce12c-e2ef-4db8-aae6-61702b99b8fa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/paper_agent_73c709c0",
  "sessionId": "71c5797e-c964-4419-a009-2e487a4de1fc",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "ancient-greeting-comet",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01FANF2saRyeceraWkZcxsuN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1624,
      "cache_read_input_tokens": 28203,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1624,
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

_source line 11 · 2026-05-20T19:54:29.033Z_

<details><summary>↩ Tool result · `toolu_01MatVL5oZUn28yy53qSmman`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	\paragraph{Methodological pitfalls.}
5	\label{sec:pitfalls}
6	Lead-lag analysis in iterative model collapse is fragile along three axes, each documented with data from \S\ref{sec:regime}--\ref{sec:dose_response}.
7	\emph{Method sensitivity}: five detection methods applied to identical data ($\alpha{=}1.0$, 8 validated canary$\to$downstream pairs, direction-checked) yield forward significance rates spanning 0\% to 75\%, with inter-method agreement at $\kappa{=}0.185$ and naive cross-correlation reaching 75\% null-control FPR.
8	\emph{Spurious regression}: first-differencing to remove shared trends~\cite{granger1974spurious} eliminates canary$\to$perplexity associations ($F{\approx}0$, $p{=}0.99$) while preserving canary$\to$diversity (24/24$\to$24/24), exposing an entire analysis channel as trend-driven rather than temporally precedent.
9	\emph{Regime dependence}: the same Granger test finds 0/8 pairs significant through $\alpha{=}0.45$ but 6/8 at $\alpha{=}0.50$, a categorical shift at a 5-percentage-point boundary that a single-$\alpha$ study would miss entirely.
10	These pitfalls motivate systematic method comparison rather than reliance on any single detection approach.
11	
12	\paragraph{Multi-Method Consensus Test (MMCT).}
13	\label{sec:mmct}
14	We compare five lead-lag detection methods through MMCT, a weighted consensus protocol~\cite{simonsohn2020specification,scheffer2009early} calibrated against null-control ($\alpha{=}0.0$) data where any detection is a false positive.
15	Each method receives FPR-inverse weight; the weighted score yields formal $p$-values from the empirical null distribution (Algorithm in Appendix~\ref{app:mmct}).
16	MMCT identifies PermG as the only method combining zero null-control FPR with consistent detection; this ranking holds under all four weight schemes tested, from equal weighting to FPR-inverse caps (Appendix~\ref{app:weight_robustness}).
17	
18	\paragraph{Permutation Granger causality.}
19	PermG tests whether past values of canary metric $X$ improve prediction of downstream metric $Y$ beyond $Y$'s own history; Granger precedence establishes temporal predictive improvement, not true causality~\cite{shojaie2022granger}.
20	We apply 5{,}000 permutations~\citep{phipson2010permutation} on first-differenced series with Benjamini--Hochberg FDR correction at $q{=}0.05$ across 8 validated canary$\to$downstream pairs (2 canaries $\times$ 4 downstream metrics).
21	Three properties distinguish PermG: a nonparametric null distribution robust to the short non-stationary series typical of iterative training~\cite{boettiger2012limits}, built-in directionality (forward and reverse tested separately), and a hyperparameter-free test statistic.
22	The remaining four methods each exhibit a specific limitation: naive cross-correlation has 75\% null-control FPR; differenced cross-correlation detects bidirectionally without directional separation; threshold onset is power-limited at $T{=}11$ under corrected $3\sigma$ calibration (0/8 significant in 8 of 12 cross-architecture conditions); Toda--Yamamoto~\cite{toda1995statistical} provides supplementary detection with reduced power from degree-of-freedom costs of lag augmentation (directional assignment under verification).
23	Per-method dose-response profiles, Shapley value analysis, and the full MMCT algorithm appear in the Appendix.
24	
25	\subsection{Signal-Times-Resolution Interpretive Lens}
26	\label{sec:theory}
27	
28	We apply standard statistical power scaling to PermG, interpreted through a Signal$\times$Resolution (S$\times$R) decomposition.
29	Detectability of canary$\to$downstream temporal precedence depends on two competing factors:
30	\begin{equation}
31	    \text{Detectability}(\alpha) \;\propto\; S(\alpha) \times R(\alpha),
32	    \label{eq:detectability}
33	\end{equation}
34	where $S(\alpha)$ is signal strength (magnitude of distributional shift, monotonically increasing with $\alpha$) and $R(\alpha)$ is temporal resolution (the generational gap between canary and downstream responses).
35	$R(\alpha)$ is non-monotonic: at low $\alpha$, entropy and diversity respond in different generations ($R$ large); at $\alpha{\approx}0.60$, relaxation time matching compresses both responses into a single generation ($R \to 0$); at high $\alpha$, the severity of entropy collapse outpaces the diversity cascade, restoring the generational offset.
36	The product $S \times R$ predicts four regimes: \emph{blind} ($\alpha \leq 0.45$; $S$ below detection floor), \emph{onset} ($\alpha \approx 0.50$; $S$ crosses threshold while $R$ remains high), \emph{synchronous dip} ($\alpha \approx 0.60$; $R \to 0$ suppresses detection despite rising $S$), and \emph{detection} ($\alpha \geq 0.75$; $S$ dominates).
37	Full empirical confirmation appears in \S\ref{sec:regime} and \S\ref{sec:dose_response}.
38	
39	Under a permutation test framework, detection power scales as $\mathrm{Power}(\alpha, T) = \Phi\bigl(S \cdot R \cdot \sqrt{T} / \sigma_{\mathrm{noise}}\bigr)$, where $\Phi$ is the standard normal CDF and the $\sqrt{T}$ scaling follows standard power analysis as a conservative lower bound.
40	The S$\times$R decomposition predicts that detection count is T-invariant when detected pairs are already saturated ($F \gg F_{\text{crit}}$) and undetected pairs are structural nulls ($F \approx 1$): increasing $T$ cannot flip either class.
41	The sharp detection onset at $\alpha_c$ (at $T{=}10$) is consistent with a power threshold: when $S \cdot R \cdot \sqrt{T}$ first exceeds the detection floor, power undergoes a steep onset from near-zero to near-one.
42	$T{=}20$ validates this prediction across four contamination levels: PermG yields 6/8 at $\alpha \in \{0.50, 0.75, 1.0\}$ and 0/8 at $\alpha{=}0.60$, all identical to $T{=}10$; six diversity-based pairs are consistently significant ($F{=}449$--$2947$) while two mauve-based pairs show $F{<}2$ regardless of sequence length (\S\ref{sec:dose_response}).
43	Sub-threshold FDR $p{=}0.059$--$0.091$ at $\alpha{=}0.45$ ($T{=}10$) is consistent with proximity to the power boundary.
44	
45	\subsection{Cascade Ordering Theory}
46	\label{sec:cascade}
47	
48	Under mode amplification---the assumption that MLE on peaked distributions concentrates probability toward high-frequency tokens~\cite{shumailov2024curse,dohmatob2024tale}---we derive a formal ordering of metric responses (proofs in Appendix~\ref{app:cascade_theory}).
49	
50	\begin{theorem}[Entropy leads diversity]\label{thm:entropy_leads}
51	Under mode amplification: \textup{(a)} entropy can decrease while the $\epsilon$-effective support $S_\epsilon(p) {=} |\{i: p_i > \epsilon\}|$ (hence distinct-$n$) is unchanged; \textup{(b)} if distinct-$n$ decreases, entropy has already decreased.
52	\end{theorem}
53	
54	The asymmetry arises because entropy responds to any mass redistribution (first-order), while diversity changes only when a token probability crosses the generation threshold~$\epsilon$.
55	The margin $\gamma = \min_{i: p_i > \epsilon}(p_i - \epsilon)$ quantifies how much shift diversity absorbs silently.
56	
57	\begin{proposition}[Diversity lag $\geq 1$ generation]\label{prop:div_lag}
58	If the per-generation perturbation satisfies $\alpha\|\mathcal{T}(p_t) - p_t\|_\infty < \gamma(p_t, \epsilon)$ through entropy onset $t_H$, then diversity onset $t_D \geq t_H + 1$.
59	\end{proposition}
60	
61	ECE co-moves with entropy at zero lag: under mode amplification, peakier conditionals simultaneously decrease per-token entropy and increase confidence; with accuracy approximately stationary in early collapse, $\Delta\mathrm{ECE} \approx \Delta C > 0$ whenever $\Delta\bar{H} < 0$ (qualitative argument; Appendix~\ref{app:cascade_theory}).
62	The predicted cascade $\{H, \mathrm{ECE}\} \to \mathrm{Distinct}$-$n$ is confirmed in 15/15 experiments at $\alpha \geq 0.30$ ($t_H{=}1$, $t_D{=}2$ uniformly; \S\ref{sec:regime}); five low-$\alpha$ experiments show no detectable onset, leaving the ordering undefined below the detection floor.
63	
64	\paragraph{Calibration.}
65	At $\alpha{=}0.0$ (null control), PermG yields 0\% FPR across 3~seeds (0/24 pairs; Rule-of-Three 95\% CI: [0\%, 12.5\%]); at $\alpha{=}1.0$, all 6 effect-size reference pairs are recovered (0\% FNR, 4~seeds).
66	Cross-architecture validation confirms PermG ${\geq}6/8$ in 13/15 conditions (\S\ref{sec:generalization}); full calibration details in the Appendix.
67	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6fbce12c-e2ef-4db8-aae6-61702b99b8fa",
  "isSidechain": true,
  "promptId": "df7610aa-ce16-48cc-8465-cca12edac9f8",
  "agentId": "a0170d1e5ef70ae63",
  "type": "user",
  "uuid": "10d8e56d-51ab-49ab-8945-4cce9784421d",
  "sourceToolAssistantUUID": "6fbce12c-e2ef-4db8-aae6-61702b99b8fa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/paper_agent_73c709c0",
  "sessionId": "71c5797e-c964-4419-a009-2e487a4de1fc",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "ancient-greeting-comet"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-20T19:54:29.352Z_

<details open><summary>🔧 Tool call — Read · `toolu_01RN71mC1iZFZ9GnLUxDo6V3`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "10d8e56d-51ab-49ab-8945-4cce9784421d",
  "isSidechain": true,
  "agentId": "a0170d1e5ef70ae63",
  "requestId": "req_011CbEQaKoUtsmgNdefgRCeK",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "68a78fc5-2d79-4c3c-af3f-8bdf0c411777",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/paper_agent_73c709c0",
  "sessionId": "71c5797e-c964-4419-a009-2e487a4de1fc",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "ancient-greeting-comet",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01FANF2saRyeceraWkZcxsuN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1624,
      "cache_read_input_tokens": 28203,
      "output_tokens": 318,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1624
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 318,
          "cache_read_input_tokens": 28203,
          "cache_creation_input_tokens": 1624,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1624,
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

_source line 13 · 2026-05-20T19:54:29.363Z_

<details><summary>↩ Tool result · `toolu_01RN71mC1iZFZ9GnLUxDo6V3`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	We study lead-lag analysis pitfalls in iterative training collapse using Pythia-410M \cite{biderman2023pythia}, a 410M-parameter decoder-only language model.
8	Pythia provides a controlled setting: small enough for multi-seed experiments across thirteen contamination levels, yet large enough to exhibit meaningful generation-over-generation degradation.
9	Cross-architecture validation uses GPT-2-medium (345M parameters, also decoder-only), a second transformer family of similar scale; results are reported in \S\ref{sec:regime} and \S\ref{sec:discussion}.
10	Training data is drawn from WikiText-103 \cite{merity2017pointer}, using 5{,}000-sample subsets per generation.
11	
12	Our protocol follows the replace paradigm of \citet{shumailov2024curse}, adapted for mixed synthetic-real training at $\alpha{<}1.0$.
13	Each generation $t$ proceeds in three steps: (1)~fine-tune the generation-$(t{-}1)$ model for 5{,}000 steps on a mixture of $\alpha$ fraction synthetic data and $(1{-}\alpha)$ fraction real data (AdamW optimizer, learning rate $5 \times 10^{-5}$, 500 warmup steps, weight decay $0.01$, batch size 4 for Pythia-410M, 32 for GPT-2-medium); (2)~generate 5{,}000 synthetic samples from the fine-tuned model (temperature $1.0$, top-$k{=}50$, max length 512 tokens); (3)~fully replace the synthetic pool.
14	We run $T{=}10$ generations across a 13-point $\alpha$ grid ($\{0.00, 0.05, 0.10, \ldots, 1.00\}$) with multi-seed replication (4 seeds at $\alpha{=}1.0$; 3 at primary levels; 1--2 at probing points).
15	
16	We track two \emph{canary metrics}---token entropy ($H(p_\theta | \text{context})$, 1{,}000 held-out samples) and ECE (15 bins)---and three \emph{downstream metrics}: distinct-1 and distinct-2~\cite{li2016diversity} and perplexity (evaluated on held-out real data).
17	Additional metrics (distinct-3, effective rank, Self-BLEU) appear in the Appendix.
18	Code and data will be released upon publication.
19	
20	All hypothesis tests apply Benjamini--Hochberg (BH) FDR correction at $q{=}0.05$.
21	Permutation Granger causality tests use 5{,}000 permutations on first-differenced series \cite{shojaie2022granger}.
22	Cross-correlation analysis uses a maximum lag of 5 generations.
23	Raw metric drift from generation~0 to generation~10 is summarized in Appendix Table~\ref{tab:drift_summary}.
24	
25	
26	\subsection{Sharp Detection Onset}
27	\label{sec:regime}
28	
29	Diversity collapse occurs at every contamination level: distinct-1 declines by $14.1\%$ at $\alpha{=}0.0$ (fine-tuning drift) and by $40.3{\pm}0.3\%$ at $\alpha{=}0.25$ (3-seed mean).
30	Despite this ubiquitous degradation, Granger-causal detectability is sharply regime-dependent.
31	The onset we report reflects PermG's statistical power curve crossing the detection floor at a critical contamination level, not the emergence of a new physical signal; this interpretation is confirmed by sub-threshold $p$-values at $\alpha{=}0.45$ (\S\ref{sec:theory}).
32	Permutation Granger (PermG) tests find 0/8 canary$\to$downstream pairs FDR-significant from $\alpha{=}0.00$ through $\alpha{=}0.45$, then jump to 6/8 at $\alpha{=}0.50$ (2~fp32 seeds, consistent).
33	This transition is striking because cumulative synthetic fraction barely changes across the boundary: $C = 1{-}(1{-}\alpha)^{10}$ yields $99.75\%$ at $\alpha{=}0.45$ versus $99.90\%$ at $\alpha{=}0.50$, a difference of 0.15 percentage points, yet detection jumps from null to reliable.
34	Sigmoid regression quantifies this onset: $\alpha_c = 0.476$ (bootstrap 95\% CI: [0.43, 0.56]), transition width $\Delta\alpha \approx 0.02$, $R^2 = 0.969$ (Figure~\ref{fig:regime_map}).
35	A Fisher exact test corroborates the categorical jump: 0/64 pairs FDR-significant at $\alpha \leq 0.45$ versus 18/32 at $\alpha \geq 0.50$ ($p = 3.45 \times 10^{-11}$); sub-threshold $p$-values at $\alpha{=}0.45$ ($p_{\mathrm{fdr}} = 0.059$--$0.091$) are consistent with proximity to the power boundary (\S\ref{sec:theory}).
36	A specification curve analysis (1{,}160 specifications) confirms specification-invariance of the onset.
37	
38	First-differencing scopes the canary claim precisely.
39	Canary$\to$diversity pairs retain unanimous FDR significance after first-differencing ($24/24 \to 24/24$ across 4~seeds at $\alpha{=}1.0$, 6 pairs per seed), while canary$\to$perplexity collapses entirely ($F \approx 0$, $p = 0.99$): the apparent perplexity association is a shared-trend artifact.
40	All canary claims are therefore scoped to diversity metrics only.
41	This scoping reflects a genuine temporal structure difference, not selective power loss from differencing: $|r|$ retention is ${\geq}95\%$ for both channels, but canary$\to$diversity correlations peak at lagged offsets (81\% at lag${<}0$, median${=}-1$) while canary$\to$perplexity correlations are contemporaneous (50\% at lag${=}0$), producing $20$--$28{\times}$ lower Granger $F$ for perplexity (Appendix~\ref{app:channel_effect_size}; perplexity $n{=}8$, limited sample).
42	At $\alpha{=}1.0$, all 24 canary$\to$diversity pairs (6 per seed $\times$ 4~seeds; mauve excluded) reach FDR significance in the forward direction with 0/24 reverse; directional asymmetry is robust across all WikiText conditions.
43	Independent of the Granger test, the degradation cascade confirms temporal precedence: entropy onset at generation~1 precedes distinct-$n$ onset at generation~2 in 16/18 WikiText conditions (Kendall $\tau{=}0.337$; \S\ref{sec:cascade}, Appendix~\ref{app:moment_cascade}).
44	The canary mechanism also exhibits a blind spot: at $\alpha{=}0.10$, distinct-1 has already dropped by $39.6\%$, yet token entropy is indistinguishable from the null ($-5.3\%$ versus $-4.6{\pm}0.4\%$ at $\alpha{=}0.0$).\footnote{Seed~43 at $\alpha{=}0.10$ shows 3/8 PermG FDR-significant pairs versus 0/8 for seed~42, consistent with stochastic variation at low signal rather than robust detection; no other below-threshold $\alpha$ level exhibits seed-dependent detection.}
45	Below $\alpha_c$ at $T{=}10$, diversity collapse proceeds without any detectable Granger-causal signal in the canary metrics.
46	
47	\begin{figure}[t]
48	\centering
49	\includegraphics[width=\linewidth]{figures/metric_trajectory.pdf}
50	\caption{Metric trajectories at $\alpha{=}1.0$ (Pythia-410M, 4~seeds). Token entropy drops at generation~1; distinct-1 declines from generations~2--3, with a consistent one-generation canary lead across all four seeds (shaded: inter-seed range). This pattern corresponds to 24/24 forward and 0/24 reverse FDR-significant canary$\to$diversity pairs (6 per seed, mauve excluded).}
51	\label{fig:metric_trajectory}
52	\end{figure}
53	
54	
55	\subsection{Dose-Response and the $S \times R$ Lens}
56	\label{sec:dose_response}
57	
58	The PermG dose-response profile (Figure~\ref{fig:regime_map}) reveals four detection regimes: \emph{blind} ($\alpha \leq 0.45$, 0/8 FDR-significant pairs), \emph{onset} ($\alpha \approx 0.50$, 6/8), \emph{synchronous dip} ($\alpha \approx 0.60$, 0/8 both seeds; dual-seed confirmed), and \emph{detection} ($\alpha{=}0.75$, 0--6/8 per seed, 2 of 3 seeds ${\geq}5/8$; $\alpha{=}1.0$, 6/8 across 4~seeds).
59	The non-monotonic dip at $\alpha{=}0.60$ is consistent with the $S \times R$ lens (\S\ref{sec:theory}): signal strength $S(\alpha)$ rises monotonically with contamination, but temporal resolution $R(\alpha)$ drops when relaxation time approaches the observation interval.
60	At $\alpha \approx 0.60$, this compression drives the canary-to-downstream lag toward zero, and the product $S \times R$ reaches a local minimum.
61	The synchronous zone differs from the blind zone: the latter shows canary drift indistinguishable from null; the former shows substantial drift in both channels but without temporal offset.
62	At $\alpha{=}0.55$, PermG returns 0/8 despite marginal $p$-values ($p_{\mathrm{fdr}}{=}0.062$--$0.092$); DiffXCorr detects 8/8 bidirectionally, confirming signal below PermG's directional threshold.
63	
64	Method choice is itself a major source of analytic variability: at $\alpha{=}1.0$, direction-checked forward significance rates span 0\% to 75\% (Table~\ref{tab:method_comparison}), with inter-method agreement at $\kappa{=}0.185$ (near chance); PermG is the only method combining zero null-control FPR with consistent detection at $\alpha \geq 0.50$.
65	
66	$T{=}20$ experiments validate the predict-then-verify framework: all four completed predictions fall within bootstrap confidence intervals, including both tight-CI falsifiable tests ($\alpha{=}0.75$ and $\alpha{=}1.0$, CI${=}$[6,8], observed 6/8 each).
67	PermG counts are uniformly T-invariant: $6/8 \to 6/8$ in the detection regime ($\alpha \in \{0.50, 0.75, 1.0\}$) and $0/8 \to 0/8$ in the synchronous-collapse regime ($\alpha{=}0.60$), reflecting a structural ceiling where six diversity-based pairs are consistently significant ($F{=}449$--$2947$) while two mauve-based pairs show $F{<}2$ regardless of sequence length.
68	PermG directional selectivity is equally T-invariant: forward 6/8 versus reverse 0/8 at $\alpha \in \{0.50, 0.75, 1.0\}$, while DiffXCorr detects bidirectionally (6/8 both directions).
69	$\alpha{=}0.45$ results are pending; this level serves as the Model~A (power-limited) vs.\ Model~B (structural ceiling) discrimination test.
70	
71	\begin{table}[t]
72	\centering
73	\small
74	\caption{Forward-direction FDR significance rates (\%) across contamination levels (Pythia-410M, seed~42, fp32; $3\sigma$ threshold calibration, lag-direction filtering for cross-correlation methods). Each cell: fraction of 8 validated pairs at BH-corrected significance ($q{=}0.05$). PermG is the only method combining zero null-control FPR with consistent detection at $\alpha \geq 0.50$.}
75	\label{tab:method_comparison}
76	\resizebox{\columnwidth}{!}{%
77	\begin{tabular}{lcccccc}
78	\toprule
79	Method & $\alpha{=}0.0$ & $\alpha{=}0.25$ & $\alpha{=}0.50$ & $\alpha{=}0.75$ & $\alpha{=}1.0$ & FPR$_\text{null}$ \\
80	\midrule
81	Naive XCorr          & 75   & 62.5 & 62.5 & 0    & 0    & 75  \\
82	Diff.\ XCorr         & 0    & 25   & 12.5 & 0    & 0    & 0   \\
83	Threshold ($3\sigma$) & 37.5 & 62.5 & 100  & 100  & 25   & 37.5 \\
84	Perm.\ Granger       & \textbf{0}    & \textbf{0}    & \textbf{75}   & \textbf{75}   & \textbf{75}   & \textbf{0}   \\
85	Toda--Yamamoto$^\S$  & 12.5 & 37.5 & 50   & 100  & 12.5 & 12.5 \\
86	\bottomrule
87	\multicolumn{7}{l}{\footnotesize $^\S$TY directional assignment under verification; row retained for completeness.} \\
88	\end{tabular}}
89	\end{table}
90	
91	
92	\subsection{Cross-Architecture Generalization}
93	\label{sec:generalization}
94	
95	We evaluate the sharp detection onset across 15 model-seed combinations spanning six families (Pythia, GPT-2, OPT, Qwen, SmolLM3, Padding-variant), scales from 345M to 6.9B parameters, and two training domains (WikiText-103, C4).
96	Table~\ref{tab:generalization} reports PermG forward detection at $\alpha{=}1.0$.
97	PermG forward significance reaches ${\geq}$6/8 in 13 of 15 conditions (87\%).
98	Two exceptions emerge.
99	SmolLM3-3B (3/8): token entropy exhibits non-monotonic oscillations, violating the monotonic decline that underlies Granger testing; only ECE$\to$downstream pairs reach significance (3/4, entropy 0/4), identifying canary metric selection as a key sensitivity dimension.
100	Pythia-1.4B exhibits seed dependence at $\alpha{=}1.0$ (s42: 2/8, s43: 6/8), not explained by capacity alone since the same architecture achieves 8/8 on C4 at both seeds.
101	At $\alpha{=}0.50$, Pythia-1.4B achieves PermG 3/8 (all three ECE-canary pairs; $K{\geq}3$ threshold met), weaker than Pythia-410M's 6/8 but above the detection threshold; token entropy pairs narrowly miss FDR correction ($p_{\mathrm{fdr}}{=}0.093$), suggesting that canary metric sensitivity---not model scale---drives cross-architecture variation.
102	The detection onset $\alpha_c \approx 0.50$ at $T{=}10$ is confirmed for both Pythia-410M (6/8) and Pythia-1.4B (3/8, ECE canary); onset is scale-robust, though detection power varies with canary metric choice.
103	
104	C4 yields the strongest detection: Pythia-1B reaches 8/8 (both seeds), and Pythia-1.4B recovers from 2/8 (WikiText) to 8/8 (C4) at the same scale; Pythia-6.9B (bf16) reaches 7/8 on WikiText.
105	Directional asymmetry is domain-dependent: one C4 condition ($\alpha{=}0.50$, s42) shows PermG reverse 7/8, but this is seed-dependent (s43: 1/8; \S\ref{sec:discussion}).
106	
107	\begin{table}[t]
108	\centering
109	\small
110	\caption{Cross-architecture PermG forward detection ($\alpha{=}1.0$). Detection (${\geq}$6/8) confirmed in 13/15 conditions (87\%) across six model families, scales from 345M to 6.9B, and two domains.}
111	\label{tab:generalization}
112	\begin{tabular}{lrcl}
113	\toprule
114	Model & Params & Domain & PermG fwd \\
115	\midrule
116	Pythia-410M    & 410M & Wiki & \textbf{6/8} \\
117	Pythia-1.4B    & 1.4B & Wiki & 2--6/8$^\dagger$ \\
118	Pythia-6.9B    & 6.9B & Wiki & \textbf{7/8}$^*$ \\
119	GPT-2-medium   & 345M & Wiki & \textbf{6/8} \\
120	OPT-1.3B       & 1.3B & Wiki & \textbf{6/8} \\
121	Qwen3.5-0.8B   & 0.8B & Wiki & \textbf{8/8} \\
122	SmolLM3-3B     & 3.0B & Wiki & 3/8$^\ddagger$ \\
123	Padding-410M   & 410M & Wiki & \textbf{6/8} \\
124	\addlinespace
125	Pythia-1B      & 1.0B & C4   & \textbf{8/8} \\
126	Pythia-1.4B    & 1.4B & C4   & \textbf{8/8} \\
127	\bottomrule
128	\multicolumn{4}{l}{\footnotesize $^\dagger$Seed-dependent (s42: 2/8, s43: 6/8).} \\
129	\multicolumn{4}{l}{\footnotesize $^*$bf16 (exceeds single-GPU fp32 capacity).} \\
130	\multicolumn{4}{l}{\footnotesize $^\ddagger$ECE-only canary (entropy 0/4).} \\
131	\multicolumn{4}{l}{\footnotesize Multi-seed (range shown): Pythia-410M, -1.4B Wiki,} \\
132	\multicolumn{4}{l}{\footnotesize GPT-2-med, OPT-1.3B, Pythia-1B C4 (2 seeds each).} \\
133	\multicolumn{4}{l}{\footnotesize Others: single seed. Total: 15 combinations.} \\
134	\end{tabular}
135	\end{table}
136	
137	
138	\subsection{Canary-Based Early Intervention}
139	\label{sec:intervention}
140	
141	We implement predictive cessation: at $\alpha{=}1.0$, training switches to pure real data when token entropy drops ${>}15\%$ from generation~0.
142	A reactive baseline triggers on distinct-1 drop ${>}10\%$.
143	The predictive trigger fires at generation~1 (one generation before reactive) in both Pythia-410M and Pythia-1.4B, reducing peak perplexity by 58\% ($56.99$ vs.\ $157.09$; bootstrap 95\% CI: 29--64\%) with recovery at generation~2 versus~4.
144	Trigger generation, recovery, and convergence are identical across the $3.4\times$ scale gap.
145	The 15\% threshold lies within a robust operating band $[10\%, 22\%]$: thresholds in this range produce zero false alarms on $\alpha{=}0.0$ while detecting $\alpha{\geq}0.50$ (Appendix~\ref{app:intervention_sensitivity}).
146	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "68a78fc5-2d79-4c3c-af3f-8bdf0c411777",
  "isSidechain": true,
  "promptId": "df7610aa-ce16-48cc-8465-cca12edac9f8",
  "agentId": "a0170d1e5ef70ae63",
  "type": "user",
  "uuid": "cd19c444-bd83-42cd-bbcb-02a43d68ac08",
  "sourceToolAssistantUUID": "68a78fc5-2d79-4c3c-af3f-8bdf0c411777",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/paper_agent_73c709c0",
  "sessionId": "71c5797e-c964-4419-a009-2e487a4de1fc",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "ancient-greeting-comet"
}
```

</details>

---

### Assistant

_source line 14 · 2026-05-20T19:54:31.358Z_

Now let me continue reading the remaining key files:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cd19c444-bd83-42cd-bbcb-02a43d68ac08",
  "isSidechain": true,
  "agentId": "a0170d1e5ef70ae63",
  "requestId": "req_011CbEQaVcb4yc6HnWVe86aP",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "4509d007-bcc8-4ebd-84fc-ffa08c21529f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/paper_agent_73c709c0",
  "sessionId": "71c5797e-c964-4419-a009-2e487a4de1fc",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "ancient-greeting-comet",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Tn9sEAyg7zPxmi8ejVudog",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 10749,
      "cache_read_input_tokens": 29827,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10749,
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

_source line 15 · 2026-05-20T19:54:32.011Z_

<details open><summary>🔧 Tool call — Read · `toolu_017f7evknjCiaFDg9YsEKet7`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4509d007-bcc8-4ebd-84fc-ffa08c21529f",
  "isSidechain": true,
  "agentId": "a0170d1e5ef70ae63",
  "requestId": "req_011CbEQaVcb4yc6HnWVe86aP",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "ff58d940-487f-4dca-b2a2-c72abe2c06a3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/paper_agent_73c709c0",
  "sessionId": "71c5797e-c964-4419-a009-2e487a4de1fc",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "ancient-greeting-comet",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Tn9sEAyg7zPxmi8ejVudog",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 10749,
      "cache_read_input_tokens": 29827,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10749,
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

_source line 16 · 2026-05-20T19:54:32.022Z_

<details><summary>↩ Tool result · `toolu_017f7evknjCiaFDg9YsEKet7`</summary>

```text
1	\section{Discussion and Conclusion}\label{sec:discussion}
2	
3	\paragraph{Granger precedence is not causation.}
4	Granger causality tests predictive improvement, not true causation~\cite{granger1969investigating,shojaie2022granger}: an unobserved process could independently drive both token entropy and diversity metrics.
5	Our central claim is scoped accordingly---``token entropy Granger-precedes diversity collapse''---and bivariate tests cannot exclude confounders.
6	
7	\paragraph{Entropy--diversity coupling.}
8	Token entropy and distinct-$n$ share mechanical coupling (distributional concentration constrains $n$-gram diversity), but this would produce \emph{synchronous} co-movement (lag~0), not the consistent one-generation temporal lead we observe (Figure~\ref{fig:metric_trajectory}).
9	First-differencing rules out shared trends: the canary$\to$diversity channel survives ($24/24 \to 24/24$) while canary$\to$perplexity vanishes entirely, scoping all canary claims to diversity metrics only (Appendix~\ref{app:channel_effect_size}).
10	The temporal lead likely reflects distinct sensitivity thresholds of continuous vs.\ discrete statistics; partial mechanical coupling cannot be fully excluded.
11	
12	\paragraph{Time-series sufficiency.}
13	With $T{=}10$ (11 data points), our analyses operate near the lower bound of standard methods~\cite{boettiger2012limits}.
14	Uniform T-invariance across four contamination levels ($\alpha{=}0.45$ pending) provides the strongest evidence that $T{=}10$ suffices: doubling to $T{=}20$ produces identical PermG outcomes at every tested $\alpha$, confirming that effective sample size is not the binding constraint (\S\ref{sec:theory}).
15	
16	\paragraph{Regime interpretation.}
17	The four-regime dose-response parallels hormetic patterns in toxicology~\cite{calabrese2003hormesis}, where opposing dose-dependent mechanisms produce non-monotonic responses.
18	At $\alpha{\approx}0.60$, temporal resolution $R \to 0$ suppresses detection despite rising signal, analogous to zero-lag Granger causality failure in synchronous systems.
19	A mutual information analysis (Appendix~\ref{app:mi_analysis}) confirms this: MI follows a V-shaped curve (minimum ${\approx}0.01$~bits near $\alpha{=}0.25$), remaining positive throughout the blind zone ($0.01$--$0.14$~bits at $\alpha \leq 0.45$) with no discontinuity at $\alpha_c$---the detection onset reflects power accumulation, not an abrupt coupling change.
20	
21	\paragraph{Cross-architecture scope.}
22	The two non-confirming conditions (SmolLM3-3B 3/8, Pythia-1.4B 2/8) reflect distinct failure modes: canary metric splitting (entropy 0/4 vs.\ ECE 3/4) and seed-dependent sensitivity (1.4B detects at $\alpha{=}0.50$ via ECE canary, suggesting canary metric choice mediates cross-scale sensitivity); C4 exhibits preliminary bidirectional coupling (\S\ref{sec:generalization}).
23	
24	\paragraph{Conclusion.}
25	Lead-lag analysis in iterative training collapse is far more fragile than assumed: method choice alone inflates spurious-signal rates to 75\% null-control FPR, and regime dependence causes the same test to shift from significant to null.
26	PermG identifies token entropy as a one-generation-ahead canary for diversity collapse, validated across 15 model-seed combinations spanning six families (345M--6.9B) with detection in 13 cases (87\%).
27	Canary-based predictive cessation reduces peak perplexity by 58\%; extended discussion in Appendix~\ref{app:extended_discussion}.
28	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ff58d940-487f-4dca-b2a2-c72abe2c06a3",
  "isSidechain": true,
  "promptId": "df7610aa-ce16-48cc-8465-cca12edac9f8",
  "agentId": "a0170d1e5ef70ae63",
  "type": "user",
  "uuid": "ebcbd889-8224-4381-be57-6daa68dddf26",
  "sourceToolAssistantUUID": "ff58d940-487f-4dca-b2a2-c72abe2c06a3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/paper_agent_73c709c0",
  "sessionId": "71c5797e-c964-4419-a009-2e487a4de1fc",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "ancient-greeting-comet"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-20T19:54:32.177Z_

<details open><summary>🔧 Tool call — Read · `toolu_01PSMQX8jVuzYZ6hFMnWTL8T`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ebcbd889-8224-4381-be57-6daa68dddf26",
  "isSidechain": true,
  "agentId": "a0170d1e5ef70ae63",
  "requestId": "req_011CbEQaVcb4yc6HnWVe86aP",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "8f1d713b-d5d7-4d42-865c-4049c29291e8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/paper_agent_73c709c0",
  "sessionId": "71c5797e-c964-4419-a009-2e487a4de1fc",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "ancient-greeting-comet",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Tn9sEAyg7zPxmi8ejVudog",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 10749,
      "cache_read_input_tokens": 29827,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10749,
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

_source line 18 · 2026-05-20T19:54:32.302Z_

<details open><summary>🔧 Tool call — Read · `toolu_016uB4rWHTRgdhaaKTgC3x3n`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8f1d713b-d5d7-4d42-865c-4049c29291e8",
  "isSidechain": true,
  "agentId": "a0170d1e5ef70ae63",
  "requestId": "req_011CbEQaVcb4yc6HnWVe86aP",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "6a19fca8-a9d1-47ae-8a63-188795d1f57e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/paper_agent_73c709c0",
  "sessionId": "71c5797e-c964-4419-a009-2e487a4de1fc",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "ancient-greeting-comet",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Tn9sEAyg7zPxmi8ejVudog",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 10749,
      "cache_read_input_tokens": 29827,
      "output_tokens": 245,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 10749
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 245,
          "cache_read_input_tokens": 29827,
          "cache_creation_input_tokens": 10749,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 10749,
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

_source line 19 · 2026-05-20T19:54:32.307Z_

<details><summary>↩ Tool result · `toolu_016uB4rWHTRgdhaaKTgC3x3n`</summary>

```text
1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	Lead-lag analysis in iterative training collapse is far more fragile than the current literature assumes.
5	Method choice alone inflates spurious-signal rates to at least 62.5\%, first-differencing exposes canary$\to$perplexity associations as entirely spurious, and regime dependence causes the same Granger test to shift from 24/24 to 0/8 significant pairs across contamination levels.
6	These pitfalls establish that single-method, single-regime analyses (the current default) cannot reliably distinguish genuine temporal precedence from statistical artifacts.
7	
8	Our systematic five-method comparison through the Multi-Method Consensus Test (MMCT) identifies permutation Granger causality as the recommended detection method: it is the only one combining zero null-control FPR with high sensitivity, exhibiting a clean step-function dose-response from 0/8 (blind spot, $\alpha{\leq}0.45$) to 6/8 (onset, $\alpha{=}0.50$) with reliable detection at $\alpha{\geq}0.75$.
9	The other four methods each fail in characteristic ways: naive cross-correlation inflates FPR to 75\%, differenced cross-correlation cannot separate forward from reverse precedence, threshold onset is power-limited at $T{=}10$ under $3\sigma$ calibration, and Toda--Yamamoto Granger provides supplementary detection at reduced power (directional assignment under verification).
10	
11	Applying permutation Granger, token entropy exhibits robust one-generation-ahead precedence over diversity collapse at $\alpha{=}1.0$ on WikiText-103 (24/24 forward, 0/24 reverse across 4~seeds, replicated on GPT-2-medium and OPT-1.3B), with cross-architecture validation confirming detection (${\geq}6/8$) in 13 of 15 model-seed combinations spanning six families (345M--6.9B).
12	Directional asymmetry is domain-dependent: consistent unidirectionality holds on WikiText across all regimes, while C4 exhibits near-symmetric bidirectional coupling at $\alpha{=}0.50$ (PermG reverse 7/8), though forward detection remains robust in both domains.
13	This finding is deliberately scoped to lexical diversity, not model collapse broadly, since the perplexity channel proved entirely spurious under differencing.
14	
15	The methodological pitfalls we expose arise from generic properties of short, non-stationary time series.
16	Cross-architecture (six families, 345M--6.9B), cross-scale ($3.4\times$ within Pythia), and cross-domain (C4) validation confirms that both the pitfalls and the method recommendation are not specific to a single experimental configuration; evaluation on models at ${>}$7B parameters remains an open direction.
17	Limitations are detailed in \S\ref{sec:limitations}; future directions are discussed in \S\ref{sec:discussion}.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6a19fca8-a9d1-47ae-8a63-188795d1f57e",
  "isSidechain": true,
  "promptId": "df7610aa-ce16-48cc-8465-cca12edac9f8",
  "agentId": "a0170d1e5ef70ae63",
  "type": "user",
  "uuid": "a96ba1c7-7afa-47f4-acd0-f2190f0b0509",
  "sourceToolAssistantUUID": "6a19fca8-a9d1-47ae-8a63-188795d1f57e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/paper_agent_73c709c0",
  "sessionId": "71c5797e-c964-4419-a009-2e487a4de1fc",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "ancient-greeting-comet"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-20T19:54:32.505Z_

<details><summary>↩ Tool result · `toolu_01PSMQX8jVuzYZ6hFMnWTL8T`</summary>

```text
1	\appendix
2	
3	\section{Metric Drift Summary}
4	\label{app:drift}
5	
6	\begin{table}[h]
7	\centering
8	\small
9	\caption{Metric drift (\%, generation~0$\to$10) for Pythia-410M across contamination levels. Diversity collapse occurs at all $\alpha$ levels, with the strongest decline at low-to-moderate contamination ($\alpha{=}0.25$: distinct-1 $-40.3{\pm}0.3\%$) rather than full replacement ($\alpha{=}1.0$: $-27.8{\pm}1.6\%$). $^\dagger$$\alpha{=}0.10$: single seed (seed~42, preliminary). $\alpha{=}0.00$, $\alpha{=}0.25$, $\alpha{=}0.50$, $\alpha{=}0.75$: 3-seed mean${\pm}$std (seeds 42, 43, 44); $\alpha{=}1.0$: 4-seed mean${\pm}$std (seeds 42, 43, 44, 45).}
10	\label{tab:drift_summary}
11	\resizebox{\columnwidth}{!}{%
12	\begin{tabular}{lccccc}
13	\toprule
14	$\alpha$ & Entropy & ECE & Distinct-1 & Distinct-2 & Perplexity \\
15	\midrule
16	0.00 & $-4.6{\pm}0.4$ & $+37.6{\pm}14$ & $-14.1{\pm}0.4$ & $-9.6{\pm}0.4$ & $-20.6{\pm}1.0$ \\
17	0.10$^\dagger$ & $-5.3$ & $+57$ & $-39.6$ & $-56.4$ & $-21.0$ \\
18	0.25 & $-4.7{\pm}0.5$ & $+81.8{\pm}15.9$ & $-40.3{\pm}0.3$ & $-56.4{\pm}0.7$ & $-18.1{\pm}0.8$ \\
19	0.50 & $-18.0{\pm}0.5$ & $+822.6{\pm}18.3$ & $-37.1{\pm}0.4$ & $-50.4{\pm}1.0$ & $+21.0{\pm}0.1$ \\
20	0.75 & $-27.6{\pm}0.2$ & $+1791{\pm}18$ & $-32.3{\pm}0.5$ & $-41.0{\pm}1.0$ & $+182.6{\pm}0.7$ \\
21	1.00 & $-60.8{\pm}1.2$ & $+3780{\pm}30$ & $-27.8{\pm}1.6$ & $-34.0{\pm}3.3$ & $+3674{\pm}45$ \\
22	\bottomrule
23	\end{tabular}}
24	\end{table}
25	
26	
27	\section{Distinct-3 Results}
28	\label{app:distinct3}
29	
30	Table~\ref{tab:distinct3_drift} reports distinct-3 drift across all contamination levels.
31	Distinct-3 exhibits the largest absolute decline among diversity metrics at low contamination ($-58.9{\pm}0.9\%$ at $\alpha{=}0.25$) but attenuates at higher levels ($-30.5\%$ at $\alpha{=}1.0$), consistent with the diversity--calibration dissociation discussed in \S\ref{sec:discussion}.
32	
33	\begin{table}[h]
34	\centering
35	\small
36	\caption{Distinct-3 drift (\%, generation~0$\to$10) across contamination levels. $\alpha{=}0.00$, $\alpha{=}0.25$, $\alpha{=}0.75$: 3-seed mean${\pm}$std; $\alpha{=}1.0$: 4-seed mean${\pm}$std; $\alpha{=}0.50$: single seed.}
37	\label{tab:distinct3_drift}
38	\begin{tabular}{lc}
39	\toprule
40	$\alpha$ & Distinct-3 drift (\%) \\
41	\midrule
42	0.00 & $-4.4{\pm}0.5$ \\
43	0.25 & $-58.9{\pm}0.9$ \\
44	0.50 & $-52.4$ \\
45	0.75 & $-38.6{\pm}1.3$ \\
46	1.00 & $-30.5{\pm}4.0$ \\
47	\bottomrule
48	\end{tabular}
49	\end{table}
50	
51	\paragraph{Lead-lag analysis.}
52	At $\alpha{=}1.0$, token entropy Granger-precedes distinct-3 at the same consensus level as distinct-1 and distinct-2: $K{\geq}4/5$ methods, $S{\geq}3/4$ seeds (Tier~3).
53	However, the optimal lag is less stable than for distinct-1/2: at max\_lag${=}7$, the lag standard deviation across seeds exceeds 1.5 generations, compared to $<0.5$ for distinct-1/2.
54	This instability reflects bimodal lag distributions (modes at lag~1 and lag~3--4), suggesting that distinct-3 captures two temporally distinct diversity loss mechanisms: rapid n-gram homogenization (lag~1) and slower distributional narrowing (lag~3--4).
55	
56	\paragraph{Sensitivity to sequence length.}
57	Higher-order $n$-gram diversity metrics are more sensitive to generation length and random sampling variability.
58	With our 512-token generation length, distinct-3 has a smaller effective denominator (number of possible unique trigrams observed) than distinct-1 or distinct-2, amplifying stochastic fluctuations.
59	This partially explains the higher lag instability: the signal-to-noise ratio for temporal precedence is lower for distinct-3, requiring more observations (longer $T$ or more seeds) to achieve stable estimates.
60	For this reason, we report distinct-3 in this appendix rather than in the main text, where distinct-1 and distinct-2 provide cleaner evidence of the entropy-leads-diversity pattern.
61	
62	
63	\section{Observation Window Sensitivity}
64	\label{app:window_sensitivity}
65	
66	Table~\ref{tab:window_sensitivity} reports how the Tier~3 consensus classification ($K{\geq}4/5$ methods) varies as a function of the minimum observation window $T_{\min}$, where analysis uses only generations $0$ through $T_{\min}$.
67	The consensus classification stabilizes at $T_{\min}{\geq}5$ (6 data points), well below our full observation window of $T{=}10$: all six effect-size reference pairs (token entropy and ECE $\to$ distinct-1, distinct-2, distinct-3) reach $K{\geq}4/5$ agreement at every window length from $T_{\min}{=}5$ through $T_{\min}{=}10$, with no spurious pairs (canary$\to$perplexity) admitted.
68	
69	Toda--Yamamoto is the only method exhibiting window-dependent sensitivity (note: TY directional assignment is under verification; these counts are retained for completeness): TY consensus stabilizes at $T_{\min}{\geq}6$, slightly later than the primary methods, reflecting the additional degrees of freedom consumed by the augmentation order $d_{\max}$.
70	This does not affect the consensus classification because the remaining four methods provide stable $K{\geq}4/5$ agreement independently of Toda--Yamamoto's vote.
71	
72	\begin{table}[h]
73	\centering
74	\small
75	\caption{Observation window sensitivity for Tier~3 consensus ($K{\geq}4/5$) at $\alpha{=}1.0$ (Pythia-410M, 4~seeds). Tier~3 pairs: number of canary$\to$downstream pairs (out of 8 validated) reaching $K{\geq}4/5$ method agreement. TY pairs: number of effect-size reference pairs (out of 6) reaching Toda--Yamamoto significance (moderate supplementary method; \S\ref{sec:method}). Consensus stabilizes at $T_{\min}{\geq}5$; TY stabilizes at $T_{\min}{\geq}6$.}
76	\label{tab:window_sensitivity}
77	\resizebox{\columnwidth}{!}{%
78	\begin{tabular}{lccccccccc}
79	\toprule
80	& \multicolumn{8}{c}{Minimum observation window $T_{\min}$} \\
81	\cmidrule(lr){2-9}
82	& 3 & 4 & 5 & 6 & 7 & 8 & 9 & 10 \\
83	\midrule
84	Tier~3 pairs (/8)    & $\dagger$ & $\dagger$ & 6 & 6 & 6 & 6 & 6 & 6 \\
85	TY pairs$^\S$ (/6)   & $\dagger$ & $\dagger$ & 3--6 & 3--6 & 3--6 & 3--6 & 3--6 & 6 \\
86	Stable               & ---       & ---       & \checkmark & \checkmark & \checkmark & \checkmark & \checkmark & \checkmark \\
87	\bottomrule
88	\multicolumn{9}{l}{\footnotesize $\dagger$~Insufficient degrees of freedom for Granger-type tests ($<6$ data points).} \\
89	\multicolumn{9}{l}{\footnotesize $^\S$~TY directional assignment under verification.}
90	\end{tabular}}
91	\end{table}
92	
93	
94	\section{Robustness Checks}
95	\label{app:robustness}
96	
97	\paragraph{Permutation count stability.}
98	Table~\ref{tab:nperm_stability} compares permutation Granger $p$-values at 5{,}000 versus 10{,}000 permutations across all canary$\to$downstream pairs at $\alpha{=}0.75$ (3~seeds, 24~pairs).
99	Permutation Granger $p$-values are stable to within 0.002 between 5{,}000 and 10{,}000 permutations, with zero significance decisions affected.
100	
101	\begin{table}[h]
102	\centering
103	\small
104	\caption{Permutation count stability analysis ($\alpha{=}0.75$, 3~seeds, 24 canary$\to$downstream pairs). $p$-values from permutation Granger tests at $n_{\text{perm}}{=}5{,}000$ versus $n_{\text{perm}}{=}10{,}000$.}
105	\label{tab:nperm_stability}
106	\begin{tabular}{lc}
107	\toprule
108	Metric & Value \\
109	\midrule
110	Max $|\Delta p|$ & 0.010 \\
111	Mean $|\Delta p|$ & 0.002 \\
112	Significance flips & 0 / 24 \\
113	\bottomrule
114	\end{tabular}
115	\end{table}
116	
117	\paragraph{FDR threshold sensitivity.}
118	Table~\ref{tab:fdr_sensitivity} reports the effect of varying the BH FDR threshold $q$ on treatment ($\alpha{=}0.75$, 3~seeds) versus null ($\alpha{=}0.0$, 3~seeds) separation for permutation Granger tests.
119	Treatment/null separation is qualitatively robust to FDR threshold choice; the null control remains at 0/24 across all thresholds.
120	
121	\begin{table}[h]
122	\centering
123	\small
124	\caption{FDR threshold sensitivity for permutation Granger significance. Treatment: $\alpha{=}0.75$ (3~seeds, 24 forward-direction pairs). Null: $\alpha{=}0.0$ (3~seeds, 24 pairs). The null control produces zero false positives at all thresholds tested.}
125	\label{tab:fdr_sensitivity}
126	\resizebox{\columnwidth}{!}{%
127	\begin{tabular}{lccc}
128	\toprule
129	$q$ & Null FDR-sig (/24) & Treatment FDR-sig (/24) & Separation \\
130	\midrule
131	0.01 & 0 & 0  & Clean (underpowered) \\
132	0.05 & 0 & 19 & Clean \\
133	0.10 & 0 & 24 & Clean \\
134	\bottomrule
135	\end{tabular}}
136	\end{table}
137	
138	\paragraph{PermG $p$-value gradient at the onset boundary ($\alpha{=}0.45$).}
139	At the onset boundary, PermG operates near its detection limit, and marginal $p$-values exhibit seed-dependent variation consistent with the statistical power interpretation (\S\ref{sec:theory}).
140	Table~\ref{tab:fdr_gradient_a045} reports BH-corrected $p$-values for all 8 canary$\to$downstream pairs across two seeds at $\alpha{=}0.45$.
141	Seed~43 reaches a minimum FDR-corrected $p{=}0.059$ (18\% above the $q{=}0.05$ threshold), while seed~42 reaches $p{=}0.091$ (82\% above threshold).
142	No pair crosses the significance threshold at either seed, yielding the aggregate 0/8 detection rate reported in \S\ref{sec:regime}.
143	The gradient is consistent with a continuous power transition rather than a binary absence of signal: PermG operates near its detection limit at $\alpha{=}0.45$, with seed-dependent variation in marginal $p$-values.
144	
145	\begin{table}[h]
146	\centering
147	\small
148	\caption{BH-corrected PermG $p$-values at $\alpha{=}0.45$ (8 canary$\to$downstream pairs $\times$ 2 seeds). Min $p_{\mathrm{fdr}}$ per seed shown. All pairs remain above the $q{=}0.05$ threshold, yielding 0/8 aggregate detection.}
149	\label{tab:fdr_gradient_a045}
150	\begin{tabular}{lcc}
151	\toprule
152	 & Seed 42 & Seed 43 \\
153	\midrule
154	Min FDR $p$ & 0.091 & 0.059 \\
155	Gap to $q{=}0.05$ & 82\% & 18\% \\
156	PermG fwd sig (/8) & 0 & 0 \\
157	\bottomrule
158	\end{tabular}
159	\end{table}
160	
161	\section{Specification Curve Analysis}
162	\label{app:spec_curve}
163	
164	The sharp detection onset reported in \S\ref{sec:regime} could in principle depend on specific analytical choices (pair selection, seed, $\alpha$ level, method parameters).
165	We assess robustness via specification curve analysis~\cite{simonsohn2020specification}, systematically varying analytical degrees of freedom to test whether the 0/8$\to$6/8 transition is specification-invariant.
166	Our specification curve varies data subsets and pair selections while holding the detection method (PermG) and its hyperparameters fixed, more closely resembling a systematic subset analysis than a full specification curve in the sense of \citet{simonsohn2020specification}.
167	
168	We construct 1{,}160 analytical specifications from the combinatorial space of: 13 contamination levels ($\alpha$ grid), seed selection ($\{42, 43, 44, 45\}$ where available), 8 canonical canary$\to$downstream pairs (\{token entropy, ECE\} $\times$ \{distinct-1, distinct-2, distinct-3, mauve\}), and method parameters (all PermG with $n_\text{perm}{=}5{,}000$, BH FDR $q{=}0.05$).
169	All specifications use the D120-canonical analysis pipeline with $3\sigma$ threshold calibration (D105) as a hard filter.
170	
171	\begin{table}[h]
172	\centering
173	\small
174	\caption{Specification curve summary (1{,}160 specifications, D120-compliant). The blind$\to$onset jump is robust across specifications: 0\% significance rate through $\alpha{=}0.45$, rising to 75\% at $\alpha{=}0.50$.}
175	\label{tab:spec_curve}
176	\begin{tabular}{lc}
177	\toprule
178	Metric & Value \\
179	\midrule
180	Total specifications & 1{,}160 \\
181	Significant (FDR $q{<}0.05$) & 536 (46.2\%) \\
182	\midrule
183	\emph{By regime} & \\
184	\quad Blind ($\alpha \leq 0.45$) & 0\% \\
185	\quad Onset ($\alpha{=}0.50$) & 75\% \\
186	\quad Detection ($\alpha \geq 0.75$) & 62--75\% \\
187	\bottomrule
188	\end{tabular}
189	\end{table}
190	
191	The specification curve confirms that the sharp detection onset is not an artifact of particular analytical choices: the categorical jump from 0\% to ${\geq}75\%$ significance at $\alpha_c{\approx}0.50$ holds across the vast majority of specifications, supporting the main text claim (\S\ref{sec:regime}).
192	
193	
194	\section{Transfer Entropy Analysis}
195	\label{app:transfer_entropy}
196	
197	Table~\ref{tab:te_results} reports transfer entropy (TE; \citealp{schreiber2000measuring}) results aggregated across all baseline conditions.
198	TE was estimated using 3-bin discretization with permutation testing ($n{=}5{,}000$).
199	No pair reaches BH-corrected significance ($q{=}0.05$) in any condition, confirming that non-parametric information-theoretic methods lack detection power at $T{=}11$.
200	
201	\begin{table}[h]
202	\centering
203	\small
204	\caption{Transfer Entropy results (12 runs across all $\alpha$ levels). TE\textsubscript{fwd}: canary$\to$downstream; TE\textsubscript{rev}: downstream$\to$canary. Mean uncorrected permutation $p$-values ($n{=}5{,}000$). No pair reaches BH-corrected $q{<}0.05$ in any run.}
205	\label{tab:te_results}
206	\resizebox{\columnwidth}{!}{%
207	\begin{tabular}{llcccc}
208	\toprule
209	Canary & Downstream & TE\textsubscript{fwd} (mean) & $p$\textsubscript{fwd} (mean) & TE\textsubscript{rev} (mean) & $p$\textsubscript{rev} (mean) \\
210	\midrule
211	token\_entropy & distinct-1 & 0.289 & 0.559 & 0.480 & 0.490 \\
212	token\_entropy & distinct-2 & 0.300 & 0.529 & 0.496 & 0.447 \\
213	token\_entropy & distinct-3 & 0.255 & 0.645 & 0.484 & 0.459 \\
214	token\_entropy & perplexity & 0.257 & 0.676 & 0.386 & 0.626 \\
215	ECE & distinct-1 & 0.185 & 0.720 & 0.184 & 0.891 \\
216	ECE & distinct-2 & 0.208 & 0.683 & 0.216 & 0.846 \\
217	ECE & distinct-3 & 0.209 & 0.689 & 0.227 & 0.807 \\
218	ECE & perplexity & 0.296 & 0.572 & 0.263 & 0.747 \\
219	\bottomrule
220	\end{tabular}}
221	\end{table}
222	
223	\section{Change-Point Detection Analysis}
224	\label{app:change_point}
225	
226	We apply a max-split change-point test with bootstrap significance assessment ($n{=}5{,}000$, $p{<}0.05$) to each metric's generation-level time series ($T{=}11$).
227	
228	Under the null control ($\alpha{=}0.00$, 3~seeds), downstream diversity metrics (distinct-1, distinct-2, distinct-3) produce significant change-points at generation~2 in all seeds (9/9 tests). With additional significant tests from ECE (2/3 seeds) and token entropy (1/3 seeds), the overall false positive rate reaches 66.7\% (12/18 tests; Table~\ref{tab:cp_null}). The monotonic drift inherent in iterative self-training is sufficient to trigger change-point detection even without canary contamination. Individual change-point significance therefore cannot serve as standalone evidence for a canary-specific effect.
229	
230	Although individual significance is unreliable as a discriminator, the temporal ordering of detected change-points reverses between null and treatment conditions. In the null ($\alpha{=}0.00$), downstream metrics show the earliest significant breaks at generation~2 (all seeds), while significant canary breaks appear later (ECE at generations~4--8). Under treatment conditions ($\alpha{\geq}0.75$), this ordering flips: canary metrics place their best splits at generation~1, followed by downstream diversity metrics at generations~2--4 and perplexity at generation~4 (Table~\ref{tab:cp_results}). This ordering reversal provides complementary evidence from a distinct statistical framework, consistent with the Granger causality analysis in \S\ref{sec:experiments}.
231	
232	Several caveats apply. The 18 individual tests per condition were not corrected for multiple comparisons (BH or Bonferroni); primary inference rests on the cross-metric temporal ordering rather than on individual significance tests. Under treatment conditions, token entropy places its best split at generation~1 with large effect sizes ($|d|{>}2.5$) in all seeds, but the pre-change segment at a generation-1 split contains only a single data point, reducing bootstrap power (1/3 seeds significant at $\alpha{=}0.75$). The short series length ($T{=}11$) further limits overall detection power.
233	
234	\begin{table}[h]
235	\centering
236	\small
237	\caption{Change-point detection under null control ($\alpha{=}0.00$, 3 seeds). CP: detected change-point generation (mean across significant seeds); $|d|$: Cohen's $d$ effect size (mean across all seeds); Sig.\ rate: fraction of seeds where $p{<}0.05$. Overall FPR: 12/18 = 66.7\%.}
238	\label{tab:cp_null}
239	\resizebox{\columnwidth}{!}{%
240	\begin{tabular}{lcccc}
241	\toprule
242	Metric & CP gen (mean) & $|d|$ (mean) & Sig.\ rate & Type \\
243	\midrule
244	token\_entropy & 1.0 & 2.94 & 1/3 & canary \\
245	ECE & 6.0 & 1.62 & 2/3 & canary \\
246	distinct-1 & 2.0 & 2.27 & 3/3 & downstream \\
247	distinct-2 & 2.0 & 2.40 & 3/3 & downstream \\
248	distinct-3 & 2.0 & 2.27 & 3/3 & downstream \\
249	perplexity & --- & 3.11 & 0/3 & downstream \\
250	\bottomrule
251	\end{tabular}}
252	\end{table}
253	
254	\begin{table}[h]
255	\centering
256	\small
257	\caption{Change-point detection at $\alpha{=}0.75$ (3 seeds). CP: detected change-point generation; $|d|$: Cohen's $d$ effect size between pre- and post-change segments. Sig.\ rate: fraction of seeds where $p{<}0.05$.}
258	\label{tab:cp_results}
259	\resizebox{\columnwidth}{!}{%
260	\begin{tabular}{lcccc}
261	\toprule
262	Metric & CP gen (mean) & $|d|$ (mean) & Sig.\ rate & Type \\
263	\midrule
264	token\_entropy & 1.0 & 3.21 & 1/3 & canary \\
265	ECE & 1.0 & 3.10 & 1/3 & canary \\
266	distinct-1 & 2.3 & 2.18 & 3/3 & downstream \\
267	distinct-2 & 3.0 & 1.97 & 3/3 & downstream \\
268	distinct-3 & 3.7 & 1.86 & 3/3 & downstream \\
269	perplexity & 4.0 & 1.70 & 3/3 & downstream \\
270	\bottomrule
271	\end{tabular}}
272	\end{table}
273	
274	\paragraph{Dose-response ordering pattern.}
275	Table~\ref{tab:cp_ordering} summarizes the ordering pattern across contamination levels.
276	The canary-to-downstream gap shifts monotonically from negative (downstream first) under the null to positive (canary first) under treatment, ruling out a methodological artifact in which canary metrics would systematically appear earlier regardless of condition.
277	The $\alpha{=}1.0$ analysis is limited to a single seed (s42); all other conditions use 3 seeds.
278	
279	\begin{table}[h]
280	\centering
281	\small
282	\resizebox{\columnwidth}{!}{%
283	\begin{tabular}{lcccl}
284	\toprule
285	$\alpha$ & Canary cp & Downstream cp & Gap & Direction \\
286	\midrule
287	0.00 & gen 4--8 & gen 2 & $-$2.5 & Downstream first \\
288	0.25 & gen 3--4 & gen 3--4 & $\approx$0 & Simultaneous \\
289	0.75 & gen 1 & gen 2--4 & $+$2.25 & Canary first \\
290	1.00 & gen 2 & gen 2--5 & $+$1.0 & Canary first \\
291	\bottomrule
292	\end{tabular}}
293	\caption{Change-point ordering reversal across contamination levels. Under the null ($\alpha{=}0.00$), downstream metrics break before canary metrics; this ordering reverses monotonically as $\alpha$ increases, consistent with the Granger-causal precedence analysis.}
294	\label{tab:cp_ordering}
295	\end{table}
296	
297	
298	\section{Sequential Monitoring: CUSUM vs Calibrated Threshold}
299	\label{app:csmp}
300	
301	We translate the Granger-precedence finding into a deployable monitoring protocol using CUSUM (cumulative sum) sequential testing~\cite{page1954continuous}, calibrated against the $\alpha{=}0.0$ null control.
302	The null-calibration procedure sets the alarm threshold $h$ such that the false alarm rate (FAR) is 0\% on null data (3~seeds, $T{=}10$), providing controlled Type~I error guarantees.
303	
304	\paragraph{Method.}
305	CUSUM monitors the cumulative deviation of token entropy from its null-control baseline: $S_t = \max(0,\; S_{t-1} + (\mu_0 - x_t) - k)$, where $\mu_0$ is the null-control mean, $k$ is the allowance parameter, and the alarm triggers when $S_t > h$.
306	We calibrate $h$ for each $k$ from the $\alpha{=}0.0$ null data (Table~\ref{tab:csmp_calibration}).
307	As a baseline, we compare against a simple calibrated threshold: alarm when the metric crosses $\mu_0 - 2\sigma_0$ for $n{\geq}1$ or $n{\geq}2$ consecutive generations.
308	
309	\begin{table}[h]
310	\centering
311	\small
312	\caption{CUSUM calibration parameters from $\alpha{=}0.0$ null control (3~seeds). $h$: alarm threshold calibrated to achieve FAR${=}$0\%. For $k{\geq}0.25$, the null CUSUM statistic remains at zero, yielding $h \approx 0$.}
313	\label{tab:csmp_calibration}
314	\begin{tabular}{lcc}
315	\toprule
316	$k$ & $h$ & FAR \\
317	\midrule
318	0.05 & 1.530 & 0\% \\
319	0.10 & 1.005 & 0\% \\
320	0.25 & $\approx$0 & 0\% \\
321	0.50 & $\approx$0 & 0\% \\
322	1.00 & $\approx$0 & 0\% \\
323	\bottomrule
324	\end{tabular}
325	\end{table}
326	
327	\paragraph{Results.}
328	Table~\ref{tab:csmp_comparison} compares CUSUM and simple threshold detection times across gradual contamination levels.
329	At the recommended operating point ($k{=}0.25$), CUSUM and the simple threshold ($n{\geq}1$) produce identical alarm times (generation~1) across all seeds and contamination levels.
330	More conservative CUSUM settings ($k{=}0.1$, $k{=}0.05$) delay detection to match the $n{\geq}2$ threshold or later.
331	At $k{=}1.0$ with $\alpha{=}0.50$, CUSUM fails entirely ($S_t \equiv 0$ for all seeds), demonstrating sensitivity to the allowance parameter.
332	No CUSUM configuration outperforms the simple calibrated threshold at any operating point tested.
333	
334	\begin{table}[h]
335	\centering
336	\small
337	\caption{CUSUM vs simple calibrated threshold: alarm generation across contamination levels (3~seeds each; all seeds agree on the alarm generation shown). Threshold: metric crosses $\mu_0 - 2\sigma_0$. No CUSUM configuration outperforms the simple threshold at any operating point.}
338	\label{tab:csmp_comparison}
339	\resizebox{\columnwidth}{!}{%
340	\begin{tabular}{lccccc}
341	\toprule
342	$\alpha$ & CUSUM $k{=}0.25$ & CUSUM $k{=}0.1$ & CUSUM $k{=}0.05$ & Thresh $n{\geq}1$ & Thresh $n{\geq}2$ \\
343	\midrule
344	0.50 & gen 1 & gen 2 & gen 3 & gen 1 & gen 2 \\
345	0.75 & gen 1 & gen 2 & gen 2 & gen 1 & gen 2 \\
346	\bottomrule
347	\multicolumn{6}{l}{\footnotesize CUSUM $k{=}1.0$ at $\alpha{=}0.50$: $S_t \equiv 0$ for all seeds (complete detection failure).} \\
348	\end{tabular}}
349	\end{table}
350	
351	\paragraph{Interpretation.}
352	The equivalence arises because the generation-0$\to$1 entropy drop is large ($|\Delta x| > 0.7$ for $\alpha{=}0.50$, $> 1.0$ for $\alpha{=}0.75$) relative to the null-control variability ($\sigma_0 \approx 0.03$).
353	Any detector with a near-zero or small threshold triggers at generation~1; CUSUM's cumulative memory provides no advantage when the initial shift already exceeds the control limit.
354	This result extends Claim~3 (method sensitivity) beyond lead-lag detection to the monitoring domain: even a sequential testing procedure with stronger theoretical properties (optimal expected detection delay under continuous monitoring) does not improve over a calibrated baseline when the initial contamination signal dominates the allowance parameter.
355	The contribution of the null-calibrated monitoring framework is the calibration procedure itself (setting alarm boundaries from $\alpha{=}0.0$ data to guarantee FAR${=}$0\%), not the CUSUM algorithm.
356	
357	\section{Background and Notation}
358	\label{app:background}
359	\label{sec:background}
360	
361	This section establishes the formal setup and notation used throughout the paper.
362	
363	\paragraph{Iterative training loop.}
364	Let $M_0$ denote a pretrained language model and $\mathcal{D}_\text{real}$ a fixed corpus of human-written text.
365	At each generation $t \geq 1$, the model $M_{t-1}$ generates a synthetic corpus $\mathcal{D}_\text{synth}^{(t-1)}$, and the next-generation model $M_t$ is fine-tuned on a mixture of $\alpha$ fraction synthetic data and $(1{-}\alpha)$ fraction real data:
366	\begin{equation}
367	    \mathcal{D}_\text{train}^{(t)} = \alpha \cdot \mathcal{D}_\text{synth}^{(t-1)} \;+\; (1{-}\alpha) \cdot \mathcal{D}_\text{real}, \quad \alpha \in [0, 1].
368	    \label{eq:mixing}
369	\end{equation}
370	At $\alpha{=}1.0$, this reduces to the full-replacement paradigm of \citet{shumailov2024curse}.
371	
372	\paragraph{Metric families.}
373	\emph{Canary metrics}: token entropy ($H(p_\theta | \text{context})$ on held-out samples) and expected calibration error (ECE).
374	\emph{Downstream metrics}: distinct-$n$ ($n \in \{1, 2, 3\}$)~\cite{li2016diversity} and perplexity.
375	Each metric produces a time series of $T{+}1$ observations.
376	
377	\paragraph{Lead-lag testing.}
378	Given canary series $X$ and downstream series $Y$, the central question is whether changes in $X$ temporally precede changes in $Y$, requiring directionality and confounder control beyond simple correlation.
379	We employ five methods spanning permissive to conservative: naive cross-correlation, differenced cross-correlation, threshold onset detection, permutation Granger causality~\cite{shojaie2022granger}, and Toda--Yamamoto Granger causality~\cite{toda1995statistical}.
380	
381	\section{MMCT Algorithm}
382	\label{app:mmct}
383	
384	Algorithm~\ref{alg:mmct} describes the Multi-Method Consensus Test (MMCT) introduced in \S\ref{sec:mmct}.
385	
386	\begin{algorithm}[h]
387	\caption{Multi-Method Consensus Test (MMCT)}
388	\label{alg:mmct}
389	\begin{algorithmic}[1]
390	\Require Time series pair $(X, Y)$; methods $\{m_1, \ldots, m_K\}$ ($K{=}5$); null-control data $\mathcal{N}$ (from $\alpha{=}0.0$); tolerance $\epsilon{=}0.01$
391	\Ensure $p$-value, consensus level $\hat{K}$
392	\For{each method $m_k$}
393	    \State Compute empirical FPR: $\widehat{\mathrm{FPR}}_k \gets$ fraction of null-control pairs where $m_k$ rejects $H_0$
394	    \State Compute weight: $w_k \gets 1 / \max(\widehat{\mathrm{FPR}}_k,\; \epsilon)$
395	    \State Apply $m_k$ to $(X, Y)$: $d_k \gets \mathbf{1}[m_k \text{ rejects } H_0]$
396	\EndFor
397	\State Weighted consensus: $W(X {\to} Y) \gets \sum_{k} w_k \, d_k \;/\; \sum_{k} w_k$
398	\State Build empirical null distribution of $W$ from all null-control pairs in $\mathcal{N}$
399	\State Compute $p$-value from empirical null: $p \gets \Pr_{\mathcal{N}}(W \geq W_{\mathrm{obs}})$
400	\State Consensus level: $\hat{K} \gets \sum_{k} d_k$
401	\State \Return $p$, $\hat{K}$
402	\end{algorithmic}
403	\end{algorithm}
404	
405	\paragraph{Design rationale.}
406	FPR-inverse weighting penalizes methods with high false positive rates on null-control data: naive cross-correlation (FPR${=}75\%$) receives weight $w{=}1.33$, while PermG (FPR${=}0\%$) receives $w{=}100$ (capped by $\epsilon$).
407	The empirical null distribution avoids parametric assumptions that are unreliable for short ($T{=}5$--$20$), non-stationary series typical of iterative training.
408	MMCT is a consensus testing protocol, not a novel statistical method; its value lies in systematic method comparison and the identification of method-dependent conclusions.
409	
410	
411	\section{Methodological Comparison Table}
412	\label{app:method_comparison}
413	
414	Table~\ref{tab:method-comparison} summarizes the methodological coverage of existing canary and monitoring analyses across the diagnostic dimensions identified in \S\ref{sec:method}.
415	No prior work combines all six dimensions.
416	
417	\begin{table}[h]
418	\centering
419	\small
420	\caption{Methodological comparison of canary and monitoring analyses. \checkmark\ = present, $\times$ = absent, $\circ$ = partial (${\leq}2$ levels or limited replication). Diff.\ = differencing/stationarity controls. Multi-M.\ = ${\geq}2$ independent statistical methods. MTC = multiple testing correction. Regime = systematic variation of $\alpha$. Seeds = ${\geq}3$ independent seeds. Arch.\ = ${\geq}2$ architecturally distinct model families.}
421	\label{tab:method-comparison}
422	\resizebox{\columnwidth}{!}{%
423	\begin{tabular}{lccccccl}
424	\toprule
425	Work & Diff. & Multi-M. & MTC & Regime & Seeds & Arch. & Metrics \\
426	\midrule
427	\citet{shumailov2024curse}     & $\times$   & $\times$   & $\times$   & $\circ$    & \checkmark & \checkmark & PPL \\
428	\citet{du2025scales}           & $\times$   & $\times$   & \checkmark & \checkmark & \checkmark & $\times$   & ECE, Acc, Dist-$n$ \\
429	\citet{gambetta2024surplexity} & $\times$   & $\times$   & $\times$   & \checkmark & \checkmark & \checkmark & Surplexity, Ent \\
430	SIGMA~\cite{sigma2026spectral} & $\times$   & $\times$   & $\times$   & $\times$   & $\times$   & $\times$   & Spectral \\
431	DCES~\cite{dces2026counter}    & $\times$   & $\times$   & $\times$   & $\times$   & $\times$   & \checkmark & ECE, Ent, PPL \\
432	\midrule
433	\textbf{Ours}                  & \checkmark & \checkmark & \checkmark & \checkmark & \checkmark & \checkmark & Ent, ECE, PPL, Dist-$n$ \\
434	\bottomrule
435	\end{tabular}%
436	}
437	\end{table}
438	
439	\section{Extended Discussion}
440	\label{app:extended_discussion}
441	
442	\paragraph{Calibration scope and generalization.}
443	All FPR and FNR calibration results are specific to our experimental setup: Pythia-410M, WikiText-103 subset, $T{=}10$, and six contamination levels.
444	Cross-architecture validation across 15 confirmed conditions spanning six model families confirms that the entropy-leads-diversity pattern generalizes: PermG forward significance reaches ${\geq}6/8$ in 13 of 15 architecture-seed combinations (Table~\ref{tab:generalization}); SmolLM3-3B (3/8) diverges due to canary metric splitting.
445	
446	\paragraph{Domain-dependent directionality.}
447	The unidirectional forward causation observed on WikiText (PermG reverse${=}$0/8 across all conditions) does not hold universally.
448	On C4 at $\alpha{=}0.50$ (s42 fp32), PermG reverse reaches 7/8, indicating near-symmetric bidirectional coupling; however, this is seed-dependent (s43: 1/8) and noted as preliminary.
449	The practical implication is that directional asymmetry should be verified per domain.
450	
451	\paragraph{Token entropy versus perplexity.}
452	The distinction lies in the evaluation domain: token entropy is $H(p_\theta | \text{context})$ on held-out real data, while perplexity is $\exp(H_\text{cross})$ on model-generated text.
453	First-differencing removes their shared downward trend: the canary$\to$diversity channel survives because entropy leads diversity by one generation, whereas the canary$\to$perplexity channel vanishes because both co-move synchronously.
454	
455	\paragraph{NLP-specific constraints.}
456	Our application of Granger-type methods faces constraints absent in econometrics: (i)~observation length ($T{=}5$--$20$ vs.\ $T{=}100$--$1000$); (ii)~non-stationarity by design rather than incidental; (iii)~small multiplicity for FDR correction (8--32 pairs per regime).
457	Transfer entropy (0/192 FDR-significant results) confirms that method sensitivity extends beyond the five-method panel.
458	
459	\paragraph{Prevention paradox.}
460	Effective intervention truncates the collapse trajectory that established Granger precedence.
461	Differenced cross-correlation retains significance under intervention (31/32 pairs), while threshold onset fails entirely (0/8), reinforcing the multi-method rationale.
462	
463	\paragraph{Canary metric choice.}
464	SmolLM3-3B reveals that canary metric selection constitutes a sensitivity dimension beyond the five statistical methods: token entropy exhibits non-monotonic oscillations (0/4 significant pairs), while ECE maintains monotonic growth (3/4 pairs).
465	No single canary metric is universally optimal.
466	
467	\paragraph{Exploratory CSD analysis.}
468	Canary metrics show rising autocorrelation consistent with critical slowing down (Kendall $\tau{=}0.79$--$0.82$) while downstream metrics show none ($\tau{=}0.03$--$0.30$), but this pattern does not survive multiple testing correction (2/10 post-BH) and remains exploratory.
469	
470	\paragraph{Future work.}
471	Extensions include multivariate VAR models for confounder testing, multi-seed replication across all six architecture families, longer training runs ($T{\geq}20$), online monitoring within training pipelines, and accumulate-mode experiments~\cite{dey2024breaking}.
472	The sigmoid onset boundary ($\alpha_c{=}0.476$) invites connection to the critical mixture ratio scaling law of \citet{gu2024cmr} and the data-mixing transitions of \citet{gu2025datamixing}.
473	
474	
475	\section{Per-Method Dose-Response Profiles}
476	\label{app:dose_response}
477	
478	Table~\ref{tab:dose_response_full} reports FDR significance counts (/8 validated pairs) for all five detection methods across 12 contamination levels (seed~42, Pythia-410M, WikiText, fp32).
479	PermG exhibits a sharp 0$\to$6 jump at $\alpha{=}0.50$ with a return to 0 at $\alpha{=}0.55$--$0.60$ (synchronous dip), while other methods show diffuse profiles: naive cross-correlation saturates at 7--8/8 across all levels including the null, and Toda--Yamamoto fluctuates without a clear onset.
480	
481	\begin{table}[h]
482	\centering
483	\small
484	\caption{Per-method FDR significance (/8 pairs) across contamination levels (Pythia-410M, seed~42, WikiText, fp32). PermG and Diff.\ XCorr use BH-corrected FDR ($q{=}0.05$); Naive XCorr, Threshold, and TY use uncorrected $p{<}0.05$ (no FDR field in pipeline). $\alpha{=}1.0$ from Pythia-410M cross-architecture condition (same seed/domain/precision).}
485	\label{tab:dose_response_full}
486	\resizebox{\columnwidth}{!}{%
487	\begin{tabular}{lccccc}
488	\toprule
489	$\alpha$ & Naive & Diff.\ XCorr & Threshold & PermG & TY$^\S$ \\
490	\midrule
491	0.00 & 8 & 4 & 3 & \textbf{0} & 1 \\
492	0.10 & 7 & 6 & 0 & \textbf{0} & 0 \\
493	0.25 & 8 & 3 & 0 & \textbf{0} & 2 \\
494	0.30 & 8 & 4 & 0 & \textbf{0} & 3 \\
495	0.35 & 8 & 4 & 0 & \textbf{0} & 1 \\
496	0.40 & 8 & 3 & 0 & \textbf{0} & 4 \\
497	0.45 & 8 & 6 & 0 & \textbf{0} & 1 \\
498	0.50 & 8 & 7 & 4 & \textbf{6} & 3 \\
499	0.55 & 8 & 8 & 0 & \textbf{0} & 1 \\
500	0.60 & 8 & 6 & 0 & \textbf{0} & 0 \\
501	0.75 & 7 & 6 & 0 & \textbf{6} & 3 \\
502	1.00 & 8 & 6 & 2 & \textbf{6} & 1 \\
503	\bottomrule
504	\multicolumn{6}{l}{\footnotesize $^\S$TY directional assignment under verification; column retained for completeness.} \\
505	\end{tabular}}
506	\end{table}
507	
508	The table highlights PermG's unique combination of zero null-control detection (0/8 at $\alpha{=}0.00$), sharp onset (0$\to$6 at $\alpha{=}0.50$), and non-monotonic synchronous dip (0 at $\alpha{=}0.55$--$0.60$), confirming it as the only method whose dose-response profile cleanly separates detection regimes.
509	Naive cross-correlation's persistently high counts (7--8/8 even at $\alpha{=}0.00$) demonstrate the 75\% null-control FPR reported in \S\ref{sec:method}.
510	
511	
512	\section{PermG Power Analysis}
513	\label{app:power_analysis}
514	
515	We characterize PermG detection power via simulation under a controlled data-generating process (DGP) that matches the structure of our iterative training time series.
516	
517	\paragraph{DGP.}
518	For each trial, we generate a bivariate system $(X_t, Y_t)$ for $t = 1, \ldots, T$ where $X_t = \mu + \epsilon_t^X$ and $Y_t = \mu + \beta X_{t-1} + \epsilon_t^Y$, with $\epsilon \sim \mathcal{N}(0, \sigma^2)$ and $\sigma{=}1$.
519	The coupling parameter $\beta$ controls signal strength; $\beta{=}0$ is the null.
520	We sweep $\beta \in [0, 2]$ across $T \in \{6, 8, 10, 15, 20\}$, running 100 replications per $(\beta, T)$ cell with 5{,}000 permutations each and BH FDR correction at $q{=}0.05$ across 8 hypothetical pairs (matching the experimental setup).
521	
522	\paragraph{Results.}
523	Table~\ref{tab:beta50} reports $\beta_{50}$, the coupling strength required for 50\% detection power, at each observation length $T$.
524	Under $\sqrt{T}$ scaling, the product $\beta_{50} \cdot \sqrt{T}$ should be constant; the observed decrease from 5.09 ($T{=}8$) to 2.68 ($T{=}20$) indicates that power grows faster than $\sqrt{T}$, with the empirical scaling closer to $T^{-1.1}$.
525	The $\sqrt{T}$ formula in \S\ref{sec:theory} thus provides a conservative lower bound on detection power: actual power at $T{=}20$ exceeds the $\sqrt{T}$ prediction.
526	False positive rates under FDR correction remain at or below 2\% across all $T$ values (raw: 1--9\%; Table~\ref{tab:beta50}).
527	
528	\begin{table}[h]
529	\centering
530	\small
531	\caption{PermG power analysis: $\beta_{50}$ (coupling for 50\% power) under BH-FDR correction ($q{=}0.05$, 8 pairs). $\beta_{50} \cdot \sqrt{T}$ decreases with $T$, indicating power grows faster than $\sqrt{T}$. FPR: false positive rate at $\beta{=}0$ (raw / FDR-corrected). Dashes indicate $<$50\% power not reached within $\beta \leq 2.0$.}
532	\label{tab:beta50}
533	\begin{tabular}{lcccc}
534	\toprule
535	$T$ & $\beta_{50}$ & $\beta_{50} \cdot \sqrt{T}$ & FPR (raw) & FPR (FDR) \\
536	\midrule
537	6  & ---  & ---  & 1\% & 0\% \\
538	8  & ---  & ---  & 6\% & 2\% \\
539	10 & 2.0  & 6.32 & 9\% & 2\% \\
540	15 & 1.2  & 4.65 & 6\% & 2\% \\
541	20 & 0.9  & 4.02 & 5\% & 1\% \\
542	\bottomrule
543	\end{tabular}
544	\end{table}
545	
546	\begin{figure}[h]
547	\centering
548	\includegraphics[width=\linewidth]{figures/permg_power_curve.png}
549	\caption{PermG detection power as a function of coupling strength $\beta$ for five observation lengths ($T{=}6$--$20$; 100 replications $\times$ 5{,}000 permutations, BH FDR $q{=}0.05$). Power increases with both $\beta$ and $T$; at $T{=}6$--$8$, PermG remains underpowered ($<$20\%) even at $\beta{=}2.0$, consistent with the $T{=}10$ minimum required for reliable detection in our experimental setting.}
550	\label{fig:permg_power}
551	\end{figure}
552	
553	At $T{=}6$ and $T{=}8$, 50\% power is not reached within $\beta \leq 2.0$ under FDR correction, explaining why PermG is fundamentally underpowered for very short series.
554	The practical implication for our $T{=}10$ setting: $\beta_{50}{=}2.0$ means that only strong coupling produces reliable detection, consistent with the sharp onset at $\alpha_c{\approx}0.50$ where signal strength first exceeds this threshold.
555	At $T{=}20$, $\beta_{50}$ drops to 0.9, predicting a left-shift of $\alpha_c$ and broader detection coverage, as formalized in the $S \times R$ lens (\S\ref{sec:theory}).
556	
557	
558	\section{Shapley Value Analysis}
559	\label{app:shapley}
560	
561	We quantify each method's marginal contribution to the MMCT ensemble using Shapley values~\cite{shapley1953value}, computed via exact enumeration over all $2^5{=}32$ coalitions of the five detection methods.
562	For a coalition $S \subseteq \{m_1, \ldots, m_5\}$, we define two performance metrics: the false positive rate FPR($S$), computed from 3 null experiments ($\alpha{=}0.0$, seeds 42/43/44; 24 null pairs total), and the false negative rate FNR($S$), computed from 45 signal experiments across all non-null $\alpha$ levels (270 signal pairs for the 6-pair variant excluding mauve).
563	The Shapley value $\phi_k$ for method $m_k$ is the weighted average of its marginal contribution across all coalitions; positive FPR-Shapley indicates the method \emph{increases} false positives, while negative FNR-Shapley indicates it \emph{reduces} false negatives.
564	The combined Shapley value $\phi_k^{\text{comb}} = \phi_k^{\text{FPR}} + \phi_k^{\text{FNR}}$ balances both error types, with more negative values indicating greater net benefit.
565	
566	Table~\ref{tab:shapley_6pair} reports the 6-pair analysis (excluding mauve).
567	PermG achieves the lowest (best) combined Shapley ($-0.180$), driven entirely by FNR reduction with zero FPR contribution---the only method with this property.
568	Naive cross-correlation is the worst contributor ($+0.203$), with its massive FPR Shapley ($+0.622$) overwhelming its FNR benefit ($-0.419$): adding naive cross-correlation to any coalition increases false positives far more than it reduces false negatives.
569	Threshold onset contributes almost nothing useful ($+0.074$ combined; FPR $+0.101$, FNR $-0.027$), confirming the near-zero detection power reported in Table~\ref{tab:method_comparison}.
570	Figure~\ref{fig:shapley} visualizes the decomposition.
571	
572	\begin{table}[h]
573	\centering
574	\small
575	\caption{Shapley value decomposition (6-pair, mauve excluded). FPR-Shapley: marginal FPR contribution (positive = increases false positives). FNR-Shapley: marginal FNR contribution (negative = reduces false negatives). Combined = FPR + FNR (more negative = better). 48 experiments, $2^5{=}32$ coalitions, exact enumeration.}
576	\label{tab:shapley_6pair}
577	\begin{tabular}{lccc}
578	\toprule
579	Method & $\phi^{\text{FPR}}$ & $\phi^{\text{FNR}}$ & $\phi^{\text{comb}}$ \\
580	\midrule
581	Naive XCorr          & $+0.622$ & $-0.419$ & $+0.203$ \\
582	Diff.\ XCorr         & $+0.163$ & $-0.306$ & $-0.142$ \\
583	Threshold ($3\sigma$) & $+0.101$ & $-0.027$ & $+0.074$ \\
584	\textbf{Perm.\ Granger} & $\mathbf{0.000}$ & $\mathbf{-0.180}$ & $\mathbf{-0.180}$ \\
585	Toda--Yamamoto       & $+0.031$ & $-0.069$ & $-0.038$ \\
586	\bottomrule
587	\end{tabular}
588	\end{table}
589	
590	\begin{figure}[h]
591	\centering
592	\includegraphics[width=\linewidth]{figures/shapley_method_contribution.pdf}
593	\caption{Shapley value decomposition of each method's marginal contribution to FPR (positive bars) and FNR (negative bars). PermG is the only method with zero FPR contribution; naive cross-correlation's FPR dominates its FNR benefit.}
594	\label{fig:shapley}
595	\end{figure}
596	
597	The 8-pair variant (including mauve) yields qualitatively identical rankings: PermG remains the best contributor ($\phi^{\text{comb}}{=}-0.152$), naive cross-correlation the worst ($+0.170$), and threshold onset near-zero ($+0.063$).
598	
599	\paragraph{FDR correction scope.}
600	This analysis applies BH-corrected significance (\texttt{significant\_fdr}) uniformly across all five methods, including naive cross-correlation and Toda--Yamamoto.
601	In contrast, the per-method dose-response profiles (Table~\ref{tab:dose_response_full}) use uncorrected significance for naive cross-correlation, threshold onset, and Toda--Yamamoto because FDR-corrected fields are not available in the per-experiment pipeline output for these methods.
602	The Shapley analysis recomputes significance from raw $p$-values with BH correction applied post hoc, ensuring a fair comparison across methods within the coalition framework.
603	
604	
605	\section{MMCT Weight Robustness Ablation}
606	\label{app:weight_robustness}
607	
608	To verify that PermG's top ranking is not an artifact of the FPR-inverse weighting scheme, we recompute Shapley values under four weight specifications (Table~\ref{tab:weight_robustness}).
609	Equal weighting ($w{=}1$ for all methods) eliminates any FPR-based advantage; PermG still ranks first ($\phi^{\text{comb}}{=}-0.152$), though its margin over naive cross-correlation narrows to 0.015.
610	Under cap-5, the margin widens to 0.043 as the FPR penalty begins to differentiate high-FPR methods.
611	Cap-10 and original cap-100 yield identical Shapley values because the consensus threshold ($K{\geq}3$) is determined by the three smallest method weights ($w_{\text{naive}}{+}w_{\text{diff}}{+}w_{\text{thresh}} = 7.76$), which are invariant to further increases in the PermG or TY cap; this saturation confirms that the original $w{=}100$ does not artificially inflate PermG's contribution.
612	Across all schemes, PermG's advantage derives from the same structural property: zero FPR ($\phi^{\text{FPR}}{=}0$) combined with moderate FNR reduction ($\phi^{\text{FNR}}{=}-0.152$ to $-0.426$).
613	
614	\begin{table}[h]
615	\centering
616	\small
617	\caption{MMCT weight robustness: PermG combined Shapley under four weighting schemes. PermG ranks first in all cases. Gap = $|\phi^{\text{comb}}_{\text{PermG}} - \phi^{\text{comb}}_{\text{runner-up}}|$. 48 experiments (3 null + 45 signal), exact Shapley enumeration ($2^5{=}32$ coalitions).}
618	\label{tab:weight_robustness}
619	\begin{tabular}{lrcrc}
620	\toprule
621	Scheme & $w_{\text{PermG}}$ & $\phi^{\text{comb}}_{\text{PermG}}$ & Runner-up & Gap \\
622	\midrule
623	Equal ($w{=}1$)     & 1   & $-0.152$ & NaiveXCorr ($-0.137$) & 0.015 \\
624	Cap-5               & 5   & $-0.165$ & NaiveXCorr ($-0.123$) & 0.043 \\
625	Cap-10              & 10  & $-0.426$ & TY ($-0.067$)         & 0.359 \\
626	FPR-inv.\ (cap-100) & 100 & $-0.426$ & TY ($-0.067$)         & 0.359 \\
627	\bottomrule
628	\end{tabular}
629	\end{table}
630	
631	
632	\section{Intervention Threshold Sensitivity}
633	\label{app:intervention_sensitivity}
634	
635	\paragraph{Within-$\alpha$ sensitivity at $\alpha{=}1.0$.}
636	Table~\ref{tab:threshold_sensitivity} reports the predictive cessation outcome under five entropy-drop thresholds (5\%--25\%) at $\alpha{=}1.0$ (Pythia-410M, seed~42).
637	All five thresholds produce identical outcomes: token entropy drops 40.7\% at generation~1, far exceeding even the most conservative threshold (25\%), so every threshold triggers at the same generation.
638	The intervention conclusion---peak perplexity 57.0, recovery in one generation, final perplexity 21.3---is invariant to threshold choice within this range.
639	
640	\begin{table}[h]
641	\centering
642	\small
643	\caption{Threshold sensitivity at $\alpha{=}1.0$ (Pythia-410M, s42, fp32). All thresholds trigger at generation~1 (entropy drop 40.7\%$\gg$threshold), producing identical recovery trajectories.}
644	\label{tab:threshold_sensitivity}
645	\begin{tabular}{rccr}
646	\toprule
647	Threshold & Trigger gen & Peak PPL & Final PPL \\
648	\midrule
649	5\%  & 1 & 56.99 & 21.29 \\
650	10\% & 1 & 56.99 & 21.29 \\
651	15\% & 1 & 56.99 & 21.29 \\
652	20\% & 1 & 56.99 & 21.29 \\
653	25\% & 1 & 56.99 & 21.29 \\
654	\bottomrule
655	\end{tabular}
656	\end{table}
657	
658	\paragraph{Cross-$\alpha$ operating band.}
659	The within-$\alpha$ analysis establishes threshold invariance at $\alpha{=}1.0$ but does not address whether thresholds generalize across contamination levels.
660	We examine observed entropy trajectories from the alpha sweep (not actual intervention experiments at $\alpha{<}1.0$) to characterize the operating band.
661	The maximum entropy drop across 10 generations varies by contamination level: 7.5\% at $\alpha{=}0.0$ (fine-tuning drift only), 7.7\% at $\alpha{=}0.10$, 7.8\% at $\alpha{=}0.25$, 22.4\% at $\alpha{=}0.50$, 35.3\% at $\alpha{=}0.75$, and 62.1\% at $\alpha{=}1.0$.
662	Thresholds below 7.5\% (e.g., 5\%) trigger on clean training data---a false alarm.
663	Thresholds above 22.4\% (e.g., 25\%) miss $\alpha{=}0.50$, the lowest contamination level with meaningful entropy signal.
664	The safe operating band is therefore $[10\%, 22\%]$: any threshold in this range produces zero false alarms on $\alpha{=}0.0$ while detecting contamination at $\alpha{\geq}0.50$.
665	The reported 15\% threshold sits near the center of this band.
666	This analysis is based on entropy trajectories from non-intervention training runs; whether actual intervention at $\alpha{<}1.0$ would produce the same triggering behavior remains unvalidated.
667	
668	
669	\section{Channel Effect Size Analysis}
670	\label{app:channel_effect_size}
671	
672	First-differencing eliminates all canary$\to$perplexity Granger associations while preserving canary$\to$diversity leads (\S\ref{sec:regime}).
673	We present three lines of evidence that this asymmetry reflects a genuine temporal structure difference rather than selective power loss from differencing.
674	
675	\paragraph{Correlation retention parity.}
676	First-differencing retains comparable correlation magnitude for both channel types (Table~\ref{tab:channel_retention}).
677	Diversity channels ($n{=}243$ pairs across all non-null experiments) retain a median $|r|$ of 0.952 after differencing, while perplexity channels ($n{=}8$ pairs; limited sample) retain 1.00.
678	This parity rules out a blanket power-loss explanation: if differencing selectively destroyed perplexity signal, $|r|$ retention would be substantially lower for perplexity than for diversity.
679	
680	\begin{table}[h]
681	\centering
682	\small
683	\caption{First-differencing effect by channel type. $|r|$ retention = diff $|r|$ / naive $|r|$. Despite comparable $|r|$ retention, Granger $F$ differs by an order of magnitude. Perplexity channel has limited sample ($n{=}8$); all paired comparisons are from bf16 experiments.}
684	\label{tab:channel_retention}
685	\begin{tabular}{lrccrc}
686	\toprule
687	Channel & $n$ & Naive $|r|$ & Diff $|r|$ & Retention & Med.\ $F$ \\
688	\midrule
689	Diversity   & 243 & 0.943 & 0.921 & 0.952 & 67.8 \\
690	Perplexity  & 8   & 0.924 & 0.900 & 1.002 & 11.5 \\
691	\bottomrule
692	\end{tabular}
693	\end{table}
694	
695	\paragraph{Granger $F$-statistic asymmetry.}
696	Within matched experiments (same model, seed, $\alpha$, precision), the Granger $F$-statistic is $20$--$28{\times}$ higher for diversity than perplexity channels.
697	At $\alpha{=}0.60$ (s42, bf16): diversity mean $F{=}229.4$ versus perplexity mean $F{=}8.3$ (ratio $27.8{\times}$).
698	At $\alpha{=}1.0$ reactive (s43, bf16): diversity mean $F{=}236.4$ versus perplexity mean $F{=}11.5$ (ratio $20.6{\times}$).
699	Since $|r|$ retention is comparable across channels, this $F$-statistic gap cannot be attributed to differencing-induced signal loss; it must reflect a difference in the temporal structure that Granger tests evaluate.
700	
701	\paragraph{Temporal structure: lagged vs.\ contemporaneous.}
702	The lag distribution of peak differenced cross-correlations reveals the structural difference.
703	For diversity channels, 81\% of peak correlations occur at canary-leading lags (lag${<}0$), with a median lag of $-1$ generation---consistent with the one-generation temporal precedence visible in Figure~\ref{fig:metric_trajectory}.
704	For perplexity channels, 50\% of peak correlations occur at lag${=}0$ (contemporaneous co-movement), with a median lag of $0$.
705	Granger causality tests lagged predictive improvement; contemporaneous co-movement produces low $F$-statistics regardless of signal magnitude, which is the correct behavior for a test designed to detect temporal precedence.
706	The perplexity channel sample is limited ($n{=}8$ pairs from bf16 experiments), and these lag distributions should not be generalized to fp32 conditions without further validation.
707	
708	
709	\section{Mutual Information Analysis}
710	\label{app:mi_analysis}
711	
712	We estimate the Gaussian mutual information lower bound between token entropy (canary) and each diversity metric across contamination levels, using $T{=}11$ data points per series ($T{=}10$ for two conditions).
713	The Gaussian estimator $\hat{I}_G = -\frac{1}{2}\log_2(1 - r^2)$, where $r$ is the Pearson correlation, provides a conservative lower bound on MI; we do not report KSG nonparametric estimates due to uncorrected positive bias at $T{=}11$.
714	The $\alpha{=}0.05$ data point is excluded because it uses an experiment excluded from the dose-response analysis.
715	
716	Table~\ref{tab:mi_bounds} reports the mean Gaussian MI across the three distinct-$n$ metrics for each $\alpha$ level.
717	MI follows a V-shaped curve: it drops from 0.112~bits at $\alpha{=}0.10$ to a minimum of 0.010~bits at $\alpha{=}0.25$, then rises monotonically to 0.270~bits at $\alpha{=}0.75$.
718	MI remains positive throughout the blind zone ($\alpha \leq 0.45$; range 0.010--0.141~bits), confirming that canary--diversity coupling exists below the detection threshold but falls below PermG's statistical power floor at $T{=}10$.
719	There is no discontinuity at $\alpha_c \approx 0.50$: the detection onset reflects power accumulation, not an abrupt change in information coupling.
720	Bootstrap 95\% CIs span 1--3 orders of magnitude at $T{=}11$, so individual point estimates should be interpreted cautiously.
721	
722	\begin{table}[h]
723	\centering
724	\small
725	\caption{Gaussian MI lower bound (bits) between token entropy and distinct-$n$ diversity metrics ($T{=}11$, Pythia-410M, fp32). Mean across distinct-1/2/3; $\alpha{=}0.05$ excluded (see text). CIs omitted due to width at $T{=}11$.}
726	\label{tab:mi_bounds}
727	\begin{tabular}{rrc}
728	\toprule
729	$\alpha$ & Seeds & MI (bits) \\
730	\midrule
731	0.10 & 2 & 0.112 \\
732	0.25 & 3 & 0.010 \\
733	0.30 & 1 & 0.062 \\
734	0.35 & 1 & 0.098 \\
735	0.40 & 1 & 0.119 \\
736	0.45 & 2 & 0.141 \\
737	0.50 & 3 & 0.107 \\
738	0.60 & 2 & 0.209 \\
739	0.75 & 1 & 0.270 \\
740	\bottomrule
741	\end{tabular}
742	\end{table}
743	
744	
745	\section{Moment Cascade Analysis}
746	\label{app:moment_cascade}
747	
748	We analyze the temporal ordering of metric degradation onset across 6 WikiText seed${\times}\alpha$ conditions (2 seeds $\times$ 3 non-trivial $\alpha$ levels each) to test whether token entropy consistently degrades before diversity metrics.
749	Onset is defined as the first generation where a metric's cumulative change exceeds 5\% of its generation-0 value.
750	
751	Table~\ref{tab:moment_cascade} reports the onset generation for each metric across conditions.
752	Token entropy reaches onset at generation~1 in all 6 conditions; distinct-$n$ metrics reach onset at generation~2 in all 18 pairwise comparisons (6 conditions $\times$ 3 distinct-$n$ metrics).
753	Across these 18 comparisons, entropy degrades first in 16 cases (Kendall $\tau{=}0.337$, consistent with a weak but reliable temporal ordering).
754	
755	\begin{table}[h]
756	\centering
757	\small
758	\caption{Degradation onset generation (5\% threshold) by metric and condition (Pythia-410M, WikiText, fp32). Token entropy reaches onset at generation~1 in all non-null conditions; distinct-$n$ metrics follow at generation~2.}
759	\label{tab:moment_cascade}
760	\begin{tabular}{llcccccc}
761	\toprule
762	Seed & $\alpha$ & Entropy & Dist-1 & Dist-2 & Dist-3 & ECE & PPL \\
763	\midrule
764	42 & 0.10 & 1 & 2 & 2 & 2 & 2 & --- \\
765	42 & 0.50 & 1 & 2 & 2 & 2 & 1 & 4 \\
766	42 & 0.75 & 1 & 2 & 2 & 2 & 1 & 1 \\
767	43 & 0.25 & 1 & 2 & 2 & 2 & 4 & --- \\
768	43 & 0.50 & 1 & 2 & 2 & 2 & 1 & 4 \\
769	43 & 0.75 & 1 & 2 & 2 & 2 & 1 & 1 \\
770	\bottomrule
771	\multicolumn{8}{l}{\footnotesize ---: onset not reached within $T{=}10$ generations.} \\
772	\end{tabular}
773	\end{table}
774	
775	The cascade ordering provides evidence for the canary mechanism independent of Granger-type tests: it does not depend on first-differencing, lag selection, or the permutation null distribution.
776	ECE shows onset at generation~1 at $\alpha{\geq}0.50$ (both seeds), consistent with its role as a secondary canary metric.
777	At low contamination ($\alpha{=}0.10$ and $\alpha{=}0.25$), perplexity never reaches the 5\% onset threshold within $T{=}10$ generations, while entropy already shows generation-1 onset---consistent with entropy's higher sensitivity to distributional shifts.
778	
779	
780	\section{Cascade Ordering Theory: Proofs}
781	\label{app:cascade_theory}
782	
783	This section provides the full proofs for Theorem~\ref{thm:entropy_leads} and Proposition~\ref{prop:div_lag} from \S\ref{sec:cascade}, plus supporting results.
784	
785	\begin{assumption}[Mode Amplification]\label{ass:mode_amp}
786	The training map $\mathcal{T}$ redistributes probability mass from low-probability to high-probability tokens: there exists a threshold $\bar{p}$ such that $\mathcal{T}(p)_i > p_i \Rightarrow p_i \geq \bar{p}$ and $\mathcal{T}(p)_j < p_j \Rightarrow p_j \leq \bar{p}$.
787	\end{assumption}
788	
789	This captures the standard finite-capacity approximation effect: MLE on finite samples from a peaked distribution amplifies modes and suppresses the tail~\cite{shumailov2024curse,dohmatob2024tale}.
790	
791	\begin{proposition}[Entropy is a first-order indicator]\label{prop:entropy_first}
792	Let $p \in \Delta^{V-1}$ and $\delta = \alpha(\mathcal{T}(p) - p)$ be a mode-amplifying perturbation with $\sum_i \delta_i = 0$. Then $\Delta H = H(p+\delta) - H(p) = -\sum_i \delta_i \log p_i + O(\|\delta\|^2) < 0$.
793	\end{proposition}
794	
795	\begin{proof}
796	Taylor-expanding $H$ around $p$:
797	$H(p+\delta) = H(p) - \sum_i \delta_i \log p_i - \sum_i \delta_i - \frac{1}{2}\sum_i \delta_i^2/p_i + O(\|\delta\|^3)$.
798	Since $\sum_i \delta_i = 0$: $\Delta H = -\sum_i \delta_i \log p_i - \frac{1}{2}\sum_i \delta_i^2/p_i + O(\|\delta\|^3)$.
799	Under mode amplification, tokens gaining mass ($\delta_i > 0$) have $p_i \geq \bar{p}$ (hence $\log p_i \geq \log \bar{p}$) and tokens losing mass ($\delta_j < 0$) have $p_j \leq \bar{p}$ (hence $\log p_j \leq \log \bar{p}$).
800	Writing $m = \sum_{i:\delta_i > 0} \delta_i$: $-\sum_i \delta_i \log p_i = -m[\overline{\log p}^{+} - \overline{\log p}^{-}] < 0$, where $\overline{\log p}^{\pm}$ are the $|\delta|$-weighted means over gaining/losing tokens.
801	The second-order Fisher information term $-\frac{1}{2}\sum_i \delta_i^2/p_i$ is always negative, reinforcing the decrease.
802	\end{proof}
803	
804	\begin{proposition}[Diversity is a threshold indicator]\label{prop:div_threshold}
805	Define the $\epsilon$-effective support $S_\epsilon(p) = |\{i \in [V]: p_i > \epsilon\}|$, where $\epsilon \approx c/N$ is the generation threshold for sample size $N$.
806	Under the same perturbation $\delta$: $\Delta S_\epsilon = -|\{i: p_i > \epsilon \text{ and } p_i + \delta_i \leq \epsilon\}|$.
807	This equals zero whenever $\|\delta\|_\infty < \gamma(p,\epsilon) := \min_{i: p_i > \epsilon}(p_i - \epsilon)$.
808	\end{proposition}
809	
810	\begin{proof}
811	Token $i$ exits the effective support iff $p_i > \epsilon$ and $p_i + \delta_i \leq \epsilon$, requiring $|\delta_i| \geq p_i - \epsilon$.
812	If $\|\delta\|_\infty < \gamma$, no token satisfies this condition.
813	\end{proof}
814	
815	\paragraph{Proof of Theorem~\ref{thm:entropy_leads}.}
816	\emph{Part (a):} Take any mode-amplifying $\delta$ with $\|\delta\|_\infty < \gamma(p,\epsilon)$.
817	By Proposition~\ref{prop:div_threshold}, $\Delta S_\epsilon = 0$.
818	By Proposition~\ref{prop:entropy_first}, $\Delta H < 0$.
819	Such $\delta$ exists for all $\alpha < \gamma / \max_i |\mathcal{T}(p)_i - p_i|$.
820	\emph{Part (b):} If $\Delta S_\epsilon < 0$, some token $k$ has $p_k > \epsilon$ but $p_k + \delta_k \leq \epsilon$, so $\delta_k < 0$.
821	Under mode amplification, this implies $p_k \leq \bar{p}$; the total mass transferred to high-probability tokens ensures $\overline{\log p}^+ > \overline{\log p}^-$.
822	By Proposition~\ref{prop:entropy_first}, $\Delta H < 0$. $\square$
823	
824	\paragraph{Proof of Proposition~\ref{prop:div_lag}.}
825	By the margin condition, at every generation $s \leq t_H$ the perturbation norm $\alpha\|\mathcal{T}(p_s) - p_s\|_\infty$ is less than $\gamma(p_s, \epsilon)$.
826	By Proposition~\ref{prop:div_threshold}, no token exits the effective support at any $s \leq t_H$, so $\Delta S_\epsilon = 0$ for all $s \leq t_H$.
827	Since time is discrete, $t_D \geq t_H + 1$. $\square$
828	
829	\paragraph{ECE co-movement (qualitative argument).}
830	Under conditional mode amplification (peakier $q_\theta(\cdot|x)$ at each generation), per-token conditional entropy $h(x) = H(q_\theta(\cdot|x))$ decreases while confidence $c(x) = \max_y q_\theta(y|x) \geq \exp(-h(x))$ increases.
831	Averaging: $\bar{H}_t$ decreases, $C_t$ increases.
832	With accuracy approximately stationary in early collapse ($A_t \approx A_0$), $\Delta\mathrm{ECE} \approx \Delta C_t > 0$ whenever $\Delta\bar{H}_t < 0$.
833	This argument establishes the direction of co-movement; the quantitative relationship depends on distribution geometry.
834	$\bar{H}_t$ denotes mean conditional entropy $\mathbb{E}_{x \sim p_{\text{eval}}}[h(x)]$, which differs from the marginal entropy $H_t = -\sum_i p_t(i)\log p_t(i)$ used in Theorem~\ref{thm:entropy_leads}; under mode amplification, both decrease monotonically, so the cascade ordering is consistent across both formulations.
835	
836	\paragraph{MAUVE ordering (conjecture).}
837	MAUVE measures divergence in a discretized embedding space via $k$-means quantization.
838	MAUVE onset requires token-level shifts (detected by entropy) to propagate through $n$-gram distributions (detected by distinct-$n$) to aggregate embedding distributions.
839	Empirically, MAUVE onset lags diversity by 0--1 generations on WikiText; however, on C4, MAUVE onset occurs at generation~1 (simultaneous with entropy), suggesting this lag is corpus-dependent.
840	
841	\paragraph{Empirical validation.}
842	Among 15 experiments at $\alpha \geq 0.30$ (where entropy perturbation exceeds the detection threshold), cascade ordering $t_H \leq t_D$ holds in 15/15 cases ($t_H{=}1$, $t_D{=}2$ uniformly).
843	ECE onset co-occurs with entropy at generation~1 at $\alpha \geq 0.50$ (zero lag, consistent with Proposition~4).
844	Five low-$\alpha$ experiments ($\alpha \leq 0.25$) show entropy perturbation below the detection threshold; cascade ordering is neither confirmed nor refuted in this regime.
845	
846	
847	\section{T=20 Predict-then-Verify Comparison}
848	\label{app:t20_comparison}
849	
850	Table~\ref{tab:t20_comparison} reports the predict-then-verify results for the $T{=}20$ extension experiments.
851	Predictions are derived from the $S \times R$ lens (\S\ref{sec:theory}): detected pairs at $T{=}10$ are predicted to remain detected (saturated $F$-statistics), and undetected pairs are predicted to remain undetected (structural nulls or synchronous collapse).
852	
853	\begin{table}[h]
854	\centering
855	\small
856	\caption{T=20 predict-then-verify comparison (Pythia-410M, seed~42, WikiText, fp32). All four completed predictions match observations, including both tight-CI falsifiable tests ($\alpha{=}0.75$ and $\alpha{=}1.0$). $\alpha{=}0.45$ pending.}
857	\label{tab:t20_comparison}
858	\begin{tabular}{lcccc}
859	\toprule
860	$\alpha$ & $T{=}10$ & Predicted $T{=}20$ & Observed $T{=}20$ & Match \\
861	\midrule
862	0.45 & 0/8 & 0/8 (power-limited) & \emph{pending} & --- \\
863	0.50 & 6/8 & 6/8 (saturated) & 6/8 & \checkmark \\
864	0.60 & 0/8 & 0/8 (synchronous) & 0/8 & \checkmark \\
865	0.75 & 6/8 & 6/8 (saturated) & 6/8 & \checkmark \\
866	1.00 & 6/8 & 6/8 (saturated) & 6/8 & \checkmark \\
867	\bottomrule
868	\end{tabular}
869	\end{table}
870	
871	The uniform T-invariance confirms the $S \times R$ prediction: PermG counts are determined by signal structure (which pairs are genuine canary$\to$downstream leads vs.\ structural nulls), not by observation length.
872	Six diversity-based pairs show $F{=}449$--$2947$ at $T{=}20$ (all $\gg F_{\text{crit}}$); two mauve-based pairs show $F{<}2$ regardless of $T$, confirming the structural ceiling interpretation.
873	PermG directional selectivity is equally T-invariant: forward 6/8 versus reverse 0/8 at $\alpha \in \{0.50, 0.75, 1.0\}$.
874	
875	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8f1d713b-d5d7-4d42-865c-4049c29291e8",
  "isSidechain": true,
  "promptId": "df7610aa-ce16-48cc-8465-cca12edac9f8",
  "agentId": "a0170d1e5ef70ae63",
  "type": "user",
  "uuid": "46c4678d-4403-4261-8c9e-1b4333007ce6",
  "sourceToolAssistantUUID": "8f1d713b-d5d7-4d42-865c-4049c29291e8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/paper_agent_73c709c0",
  "sessionId": "71c5797e-c964-4419-a009-2e487a4de1fc",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "ancient-greeting-comet"
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-20T19:54:34.175Z_

Now let me perform targeted searches for each consistency check item using grep:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "46c4678d-4403-4261-8c9e-1b4333007ce6",
  "isSidechain": true,
  "agentId": "a0170d1e5ef70ae63",
  "requestId": "req_011CbEQaioLcGuY8JvdUfome",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "3c8099fb-226e-41b9-82e6-e27f8172b6be",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/paper_agent_73c709c0",
  "sessionId": "71c5797e-c964-4419-a009-2e487a4de1fc",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "ancient-greeting-comet",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01N9Yi2ARkseHfZzpdS48vyd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 762,
      "cache_creation_input_tokens": 24509,
      "cache_read_input_tokens": 40576,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 24509,
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

_source line 22 · 2026-05-20T19:54:35.494Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01WBDuRJSTN4YF48zXdqpGdt`</summary>

```json
{
  "pattern": "framework.*Signal|framework.*Resolution|framework.*S.*R|interpretive framework",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3c8099fb-226e-41b9-82e6-e27f8172b6be",
  "isSidechain": true,
  "agentId": "a0170d1e5ef70ae63",
  "requestId": "req_011CbEQaioLcGuY8JvdUfome",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "fd93eb1b-a308-4871-9203-ea9a2ba97722",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/paper_agent_73c709c0",
  "sessionId": "71c5797e-c964-4419-a009-2e487a4de1fc",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "ancient-greeting-comet",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01N9Yi2ARkseHfZzpdS48vyd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 762,
      "cache_creation_input_tokens": 24509,
      "cache_read_input_tokens": 40576,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 24509,
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

_source line 23 · 2026-05-20T19:54:35.532Z_

<details><summary>↩ Tool result · `toolu_01WBDuRJSTN4YF48zXdqpGdt`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments_reframe.tex:31:The non-monotonic dip at $\alpha{=}0.60$ is consistent with the $S \times R$ framework (\S\ref{sec:theory}): signal strength $S(\alpha)$ rises monotonically with contamination, but temporal resolution $R(\alpha)$ drops when relaxation time approaches the observation interval.
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments_reframe.tex:39:The $S \times R$ framework generates three testable predictions for $T{=}20$ via $\mathrm{Power}(\alpha, T) = \Phi(S \cdot R \cdot \sqrt{T}/\sigma)$: (i)~$\alpha_c$ at $T{=}10$ should left-shift, (ii)~the transition should smooth, and (iii)~different methods should exhibit different $\alpha_c$ values.
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method.tex:39:Under a permutation test framework, detection power scales as $\mathrm{Power}(\alpha, T) = \Phi\bigl(S \cdot R \cdot \sqrt{T} / \sigma_{\mathrm{noise}}\bigr)$, where $\Phi$ is the standard normal CDF and the $\sqrt{T}$ scaling follows standard power analysis as a conservative lower bound.
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method_reframe.tex:41:Under a permutation test framework, detection power scales as $\mathrm{Power}(\alpha, T) = \Phi\bigl(S \cdot R \cdot \sqrt{T} / \sigma_{\mathrm{noise}}\bigr)$, where $\Phi$ is the standard normal CDF and the $\sqrt{T}$ scaling follows standard power analysis.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fd93eb1b-a308-4871-9203-ea9a2ba97722",
  "isSidechain": true,
  "promptId": "df7610aa-ce16-48cc-8465-cca12edac9f8",
  "agentId": "a0170d1e5ef70ae63",
  "type": "user",
  "uuid": "3e1d6004-4772-4afc-9da5-ffa20ced34a4",
  "sourceToolAssistantUUID": "fd93eb1b-a308-4871-9203-ea9a2ba97722",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/paper_agent_73c709c0",
  "sessionId": "71c5797e-c964-4419-a009-2e487a4de1fc",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "ancient-greeting-comet"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-20T19:54:35.917Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01AQzjeuShZjqUcSM41V5BeE`</summary>

```json
{
  "pattern": "phase transition",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3e1d6004-4772-4afc-9da5-ffa20ced34a4",
  "isSidechain": true,
  "agentId": "a0170d1e5ef70ae63",
  "requestId": "req_011CbEQaioLcGuY8JvdUfome",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "9be20d22-5e8a-4c99-b885-d3b3ae4766c6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/paper_agent_73c709c0",
  "sessionId": "71c5797e-c964-4419-a009-2e487a4de1fc",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "ancient-greeting-comet",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01N9Yi2ARkseHfZzpdS48vyd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 762,
      "cache_creation_input_tokens": 24509,
      "cache_read_input_tokens": 40576,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 24509,
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

_source line 25 · 2026-05-20T19:54:35.931Z_

<details><summary>↩ Tool result · `toolu_01AQzjeuShZjqUcSM41V5BeE`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/related_work.tex:10:\paragraph{Data mixing phase transitions.}
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/related_work.tex:11:\citet{kazdan2025collapse} map the conditions under which synthetic data triggers collapse versus improves performance, \citet{gu2024cmr} establish a scaling law for critical mixture ratios in continual pre-training, and \citet{gu2025datamixing} show that data mixing can induce phase transitions in knowledge acquisition---a direct theoretical analogue to our sharp detection onset, where a critical mixing ratio separates qualitatively different detection regimes.
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/main.aux:215:\@writefile{toc}{\contentsline {paragraph}{Data mixing phase transitions.}{2}{section*.3}\protected@file@percent }
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/main.bbl:144:  phase transitions in knowledge acquisition}.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9be20d22-5e8a-4c99-b885-d3b3ae4766c6",
  "isSidechain": true,
  "promptId": "df7610aa-ce16-48cc-8465-cca12edac9f8",
  "agentId": "a0170d1e5ef70ae63",
  "type": "user",
  "uuid": "af88d405-4da6-4e9f-8db1-620421749f55",
  "sourceToolAssistantUUID": "9be20d22-5e8a-4c99-b885-d3b3ae4766c6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/paper_agent_73c709c0",
  "sessionId": "71c5797e-c964-4419-a009-2e487a4de1fc",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "ancient-greeting-comet"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-20T19:54:36.130Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01CpQjsiwmdM1u2Vo6GWBL7u`</summary>

```json
{
  "pattern": "sharp onset",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "af88d405-4da6-4e9f-8db1-620421749f55",
  "isSidechain": true,
  "agentId": "a0170d1e5ef70ae63",
  "requestId": "req_011CbEQaioLcGuY8JvdUfome",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "60f35d46-66fe-44d3-a2fd-f407be3e0a68",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/paper_agent_73c709c0",
  "sessionId": "71c5797e-c964-4419-a009-2e487a4de1fc",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "ancient-greeting-comet",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01N9Yi2ARkseHfZzpdS48vyd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 762,
      "cache_creation_input_tokens": 24509,
      "cache_read_input_tokens": 40576,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 24509,
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

_source line 27 · 2026-05-20T19:54:36.141Z_

<details><summary>↩ Tool result · `toolu_01CpQjsiwmdM1u2Vo6GWBL7u`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex:508:The table highlights PermG's unique combination of zero null-control detection (0/8 at $\alpha{=}0.00$), sharp onset (0$\to$6 at $\alpha{=}0.50$), and non-monotonic synchronous dip (0 at $\alpha{=}0.55$--$0.60$), confirming it as the only method whose dose-response profile cleanly separates detection regimes.
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex:554:The practical implication for our $T{=}10$ setting: $\beta_{50}{=}2.0$ means that only strong coupling produces reliable detection, consistent with the sharp onset at $\alpha_c{\approx}0.50$ where signal strength first exceeds this threshold.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "60f35d46-66fe-44d3-a2fd-f407be3e0a68",
  "isSidechain": true,
  "promptId": "df7610aa-ce16-48cc-8465-cca12edac9f8",
  "agentId": "a0170d1e5ef70ae63",
  "type": "user",
  "uuid": "bffef9a1-3273-4b04-a41d-256fa437fc09",
  "sourceToolAssistantUUID": "60f35d46-66fe-44d3-a2fd-f407be3e0a68",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/paper_agent_73c709c0",
  "sessionId": "71c5797e-c964-4419-a009-2e487a4de1fc",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "ancient-greeting-comet"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-20T19:54:36.567Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01JWcMiQ6D7iRZMVH25HWi5o`</summary>

```json
{
  "pattern": "13.*15|13/15",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bffef9a1-3273-4b04-a41d-256fa437fc09",
  "isSidechain": true,
  "agentId": "a0170d1e5ef70ae63",
  "requestId": "req_011CbEQaioLcGuY8JvdUfome",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f7f6d564-ede1-4c38-8e31-fe95dad2932f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/paper_agent_73c709c0",
  "sessionId": "71c5797e-c964-4419-a009-2e487a4de1fc",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "ancient-greeting-comet",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01N9Yi2ARkseHfZzpdS48vyd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 762,
      "cache_creation_input_tokens": 24509,
      "cache_read_input_tokens": 40576,
      "output_tokens": 468,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 24509
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 762,
          "output_tokens": 468,
          "cache_read_input_tokens": 40576,
          "cache_creation_input_tokens": 24509,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 24509,
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

_source line 29 · 2026-05-20T19:54:36.593Z_

<details><summary>↩ Tool result · `toolu_01JWcMiQ6D7iRZMVH25HWi5o`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex:97:PermG forward significance reaches ${\geq}$6/8 in 13 of 15 conditions (87\%).
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex:110:\caption{Cross-architecture PermG forward detection ($\alpha{=}1.0$). Detection (${\geq}$6/8) confirmed in 13/15 conditions (87\%) across six model families, scales from 345M to 6.9B, and two domains.}
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/conclusion.tex:11:Applying permutation Granger, token entropy exhibits robust one-generation-ahead precedence over diversity collapse at $\alpha{=}1.0$ on WikiText-103 (24/24 forward, 0/24 reverse across 4~seeds, replicated on GPT-2-medium and OPT-1.3B), with cross-architecture validation confirming detection (${\geq}6/8$) in 13 of 15 model-seed combinations spanning six families (345M--6.9B).
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/main.log:725:Underfull \hbox (badness 1137) in paragraph at lines 13--15
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/main.fdb_latexmk:18:  "/usr/share/texlive/texmf-dist/fonts/tfm/adobe/times/ptmb8r.tfm" 1136768653 4524 6bce29db5bc272ba5f332261583fee9c ""
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/main.fdb_latexmk:35:  "/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmbx6.tfm" 1136768653 1344 8a0be4fe4d376203000810ad4dc81558 ""
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/main.fdb_latexmk:40:  "/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmmi10.tfm" 1136768653 1528 abec98dbc43e172678c11b3b9031252a ""
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/main.fdb_latexmk:41:  "/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmmi12.tfm" 1136768653 1524 4414a8315f39513458b80dfc63bff03a ""
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/main.fdb_latexmk:42:  "/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmmi6.tfm" 1136768653 1512 f21f83efb36853c0b70002322c1ab3ad ""
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/main.fdb_latexmk:43:  "/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmmi8.tfm" 1136768653 1520 eccf95517727cb11801f4f1aee3a21b4 ""
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/main.fdb_latexmk:44:  "/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmmi9.tfm" 1136768653 1524 d89e2d087a9828407a196f428428ef4a ""
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/main.fdb_latexmk:47:  "/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmr6.tfm" 1136768653 1300 b62933e007d01cfd073f79b963c01526 ""
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/main.fdb_latexmk:62:  "/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmex10.pfb" 1248133631 30251 6afa5cb1d0204815a708a080681d4674 ""
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/main.fdb_latexmk:65:  "/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi7.pfb" 1248133631 36281 c355509802a035cadc5f15869451dcee ""
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/main.fdb_latexmk:80:  "/usr/share/texlive/texmf-dist/fonts/type1/urw/courier/ucrr8a.pfb" 1136849748 45758 19968a0990191524e34e1994d4a31cb6 ""
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/main.fdb_latexmk:83:  "/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb" 1136849748 46026 6dab18b61c907687b520c72847215a68 ""
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/main.fdb_latexmk:86:  "/usr/share/texlive/texmf-dist/fonts/vf/adobe/helvetic/phvb.vf" 1136768653 1516 a73c15525916e6e96ff30639f5ddb11b ""
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/main.fdb_latexmk:106:  "/usr/share/texlive/texmf-dist/tex/latex/algorithms/algorithm.sty" 1251330371 3249 15763257e50278eef5db1952ccde229c ""
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/main.fdb_latexmk:126:  "/usr/share/texlive/texmf-dist/tex/latex/caption/subcaption.sty" 1690576852 12494 0c0cdb824278a4d51cefeb2e79901315 ""
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/main.fdb_latexmk:129:  "/usr/share/texlive/texmf-dist/tex/latex/float/float.sty" 1137110151 6749 16d2656a1984957e674b149555f1ea1d ""
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/main.fdb_latexmk:147:  "/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty" 1665067230 13815 760b0c02f691ea230f5359c4e1de23a7 ""
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/main.fdb_latexmk:174:  "ethics.tex" 1778912394.85475 1128 0a7250a006613bc115f319359c6335f6 ""
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method_reframe.tex:53:PermG matches consensus performance at all tested contamination levels, with cross-architecture validation confirming PermG forward significance ${\geq}6/8$ in 13 of 15 conditions (\S\ref{sec:generalization}).
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments_reframe.tex:73:PermG forward significance reaches ${\geq}$6/8 in 13 of 15 conditions (87\%).
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments_reframe.tex:87:\caption{Cross-architecture PermG forward detection ($\alpha{=}1.0$). Detection (${\geq}$6/8) confirmed in 13/15 conditions (87\%) across six model families, scales from 345M to 6.9B, and two domains.}
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex:444:Cross-architecture validation across 15 confirmed conditions spanning six model families confirms that the entropy-leads-diversity pattern generalizes: PermG forward significance reaches ${\geq}6/8$ in 13 of 15 architecture-seed combinations (Table~\ref{tab:generalization}); SmolLM3-3B (3/8) diverges due to canary metric splitting.
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex:623:Equal ($w{=}1$)     & 1   & $-0.152$ & NaiveXCorr ($-0.137$) & 0.015 \\
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method.tex:66:Cross-architecture validation confirms PermG ${\geq}6/8$ in 13/15 conditions (\S\ref{sec:generalization}); full calibration details in the Appendix.
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/main.aux:644:\@writefile{lot}{\contentsline {table}{\numberline {2}{\ignorespaces Cross-architecture PermG forward detection ($\alpha {=}1.0$). Detection (${\geq }$6/8) confirmed in 13/15 conditions (87\%) across six model families, scales from 345M to 6.9B, and two domains.}}{7}{table.caption.12}\protected@file@percent }
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/main.aux:645:\newlabel{tab:generalization}{{2}{7}{Cross-architecture PermG forward detection ($\alpha {=}1.0$). Detection (${\geq }$6/8) confirmed in 13/15 conditions (87\%) across six model families, scales from 345M to 6.9B, and two domains}{table.caption.12}{}}
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/main.aux:1493:\@LN{1213}{15}
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/main.aux:1617:\@LN{1315}{17}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f7f6d564-ede1-4c38-8e31-fe95dad2932f",
  "isSidechain": true,
  "promptId": "df7610aa-ce16-48cc-8465-cca12edac9f8",
  "agentId": "a0170d1e5ef70ae63",
  "type": "user",
  "uuid": "e3bba409-6cbd-4f13-968a-db334a3584f0",
  "sourceToolAssistantUUID": "f7f6d564-ede1-4c38-8e31-fe95dad2932f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/paper_agent_73c709c0",
  "sessionId": "71c5797e-c964-4419-a009-2e487a4de1fc",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "ancient-greeting-comet"
}
```

</details>

---

### Assistant

_source line 30 · 2026-05-20T19:54:38.202Z_

I found some issues. Let me continue searching for more specific items:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e3bba409-6cbd-4f13-968a-db334a3584f0",
  "isSidechain": true,
  "agentId": "a0170d1e5ef70ae63",
  "requestId": "req_011CbEQb2LXgRLLjsf8kB6BH",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "53c9cf61-1db5-4bc1-9678-5df8f36ef656",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/paper_agent_73c709c0",
  "sessionId": "71c5797e-c964-4419-a009-2e487a4de1fc",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "ancient-greeting-comet",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01K4Mi7U2w9UrBqeS1K7P8gy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 5699,
      "cache_read_input_tokens": 65085,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5699,
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

_source line 31 · 2026-05-20T19:54:39.257Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01P8gCBJiGfhqiFVZVTCWx8f`</summary>

```json
{
  "pattern": "T=20.*α=0\\.50|α=0\\.50.*PermG|Pythia-1\\.4B.*α=0\\.50",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "53c9cf61-1db5-4bc1-9678-5df8f36ef656",
  "isSidechain": true,
  "agentId": "a0170d1e5ef70ae63",
  "requestId": "req_011CbEQb2LXgRLLjsf8kB6BH",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "da5fba8e-cd58-45df-bb0a-4a10dd2ed478",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/paper_agent_73c709c0",
  "sessionId": "71c5797e-c964-4419-a009-2e487a4de1fc",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "ancient-greeting-comet",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01K4Mi7U2w9UrBqeS1K7P8gy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 5699,
      "cache_read_input_tokens": 65085,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5699,
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

_source line 32 · 2026-05-20T19:54:39.276Z_

<details><summary>↩ Tool result · `toolu_01P8gCBJiGfhqiFVZVTCWx8f`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "da5fba8e-cd58-45df-bb0a-4a10dd2ed478",
  "isSidechain": true,
  "promptId": "df7610aa-ce16-48cc-8465-cca12edac9f8",
  "agentId": "a0170d1e5ef70ae63",
  "type": "user",
  "uuid": "2583f2d2-d2df-4997-828e-1a512f09e48d",
  "sourceToolAssistantUUID": "da5fba8e-cd58-45df-bb0a-4a10dd2ed478",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/paper_agent_73c709c0",
  "sessionId": "71c5797e-c964-4419-a009-2e487a4de1fc",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "ancient-greeting-comet"
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-20T19:54:39.726Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01K2hqcXwGxoejq1GbptmERj`</summary>

```json
{
  "pattern": "Pythia-1\\.4B.*ECE|Pythia-1\\.4B.*3/8",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2583f2d2-d2df-4997-828e-1a512f09e48d",
  "isSidechain": true,
  "agentId": "a0170d1e5ef70ae63",
  "requestId": "req_011CbEQb2LXgRLLjsf8kB6BH",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "6f44ad49-25b1-469c-aa9c-f3c62dfb6d7b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/paper_agent_73c709c0",
  "sessionId": "71c5797e-c964-4419-a009-2e487a4de1fc",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "ancient-greeting-comet",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01K4Mi7U2w9UrBqeS1K7P8gy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 5699,
      "cache_read_input_tokens": 65085,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5699,
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

_source line 34 · 2026-05-20T19:54:39.744Z_

<details><summary>↩ Tool result · `toolu_01K2hqcXwGxoejq1GbptmERj`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex:101:At $\alpha{=}0.50$, Pythia-1.4B achieves PermG 3/8 (all three ECE-canary pairs; $K{\geq}3$ threshold met), weaker than Pythia-410M's 6/8 but above the detection threshold; token entropy pairs narrowly miss FDR correction ($p_{\mathrm{fdr}}{=}0.093$), suggesting that canary metric sensitivity---not model scale---drives cross-architecture variation.
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex:102:The detection onset $\alpha_c \approx 0.50$ at $T{=}10$ is confirmed for both Pythia-410M (6/8) and Pythia-1.4B (3/8, ECE canary); onset is scale-robust, though detection power varies with canary metric choice.
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments_reframe.tex:74:Two exceptions emerge: Pythia-1.4B seed~42 on WikiText (2/8), a seed-dependent outlier that recovers to 6/8 in seed~43, and SmolLM3-3B (3/8), where only ECE$\to$downstream pairs reach significance while entropy$\to$downstream pairs fail entirely (0/4; details in Appendix).
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/discussion.tex:22:The two non-confirming conditions (SmolLM3-3B 3/8, Pythia-1.4B 2/8) reflect distinct failure modes: canary metric splitting (entropy 0/4 vs.\ ECE 3/4) and seed-dependent sensitivity (1.4B detects at $\alpha{=}0.50$ via ECE canary, suggesting canary metric choice mediates cross-scale sensitivity); C4 exhibits preliminary bidirectional coupling (\S\ref{sec:generalization}).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6f44ad49-25b1-469c-aa9c-f3c62dfb6d7b",
  "isSidechain": true,
  "promptId": "df7610aa-ce16-48cc-8465-cca12edac9f8",
  "agentId": "a0170d1e5ef70ae63",
  "type": "user",
  "uuid": "d0e6b466-2a02-41c3-ad9e-43f9fce1da13",
  "sourceToolAssistantUUID": "6f44ad49-25b1-469c-aa9c-f3c62dfb6d7b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/paper_agent_73c709c0",
  "sessionId": "71c5797e-c964-4419-a009-2e487a4de1fc",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "ancient-greeting-comet"
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-20T19:54:40.400Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01JFUEoc9QViBxsxrcUxcQ6B`</summary>

```json
{
  "pattern": "qualitative argument|Prop.*4|ECE.*argument",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d0e6b466-2a02-41c3-ad9e-43f9fce1da13",
  "isSidechain": true,
  "agentId": "a0170d1e5ef70ae63",
  "requestId": "req_011CbEQb2LXgRLLjsf8kB6BH",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "7eb0a404-163e-464a-8d66-7332d7f30d6b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/paper_agent_73c709c0",
  "sessionId": "71c5797e-c964-4419-a009-2e487a4de1fc",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "ancient-greeting-comet",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01K4Mi7U2w9UrBqeS1K7P8gy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 5699,
      "cache_read_input_tokens": 65085,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5699,
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

_source line 36 · 2026-05-20T19:54:40.421Z_

<details><summary>↩ Tool result · `toolu_01JFUEoc9QViBxsxrcUxcQ6B`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method.tex:61:ECE co-moves with entropy at zero lag: under mode amplification, peakier conditionals simultaneously decrease per-token entropy and increase confidence; with accuracy approximately stationary in early collapse, $\Delta\mathrm{ECE} \approx \Delta C > 0$ whenever $\Delta\bar{H} < 0$ (qualitative argument; Appendix~\ref{app:cascade_theory}).
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex:829:\paragraph{ECE co-movement (qualitative argument).}
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex:843:ECE onset co-occurs with entropy at generation~1 at $\alpha \geq 0.50$ (zero lag, consistent with Proposition~4).
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/main.aux:1875:\@writefile{toc}{\contentsline {paragraph}{ECE co-movement (qualitative argument).}{20}{section*.79}\protected@file@percent }
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7eb0a404-163e-464a-8d66-7332d7f30d6b",
  "isSidechain": true,
  "promptId": "df7610aa-ce16-48cc-8465-cca12edac9f8",
  "agentId": "a0170d1e5ef70ae63",
  "type": "user",
  "uuid": "58dd19d0-d3d8-4e6a-b275-422d1513b140",
  "sourceToolAssistantUUID": "7eb0a404-163e-464a-8d66-7332d7f30d6b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/paper_agent_73c709c0",
  "sessionId": "71c5797e-c964-4419-a009-2e487a4de1fc",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "ancient-greeting-comet"
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-20T19:54:40.812Z_

<details open><summary>🔧 Tool call — Grep · `toolu_011zexraCCk9ozabSG8DSCdg`</summary>

```json
{
  "pattern": "15/15.*α|α.*15/15|cascade.*15/15",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "58dd19d0-d3d8-4e6a-b275-422d1513b140",
  "isSidechain": true,
  "agentId": "a0170d1e5ef70ae63",
  "requestId": "req_011CbEQb2LXgRLLjsf8kB6BH",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f0e09e56-d631-45c0-af4b-56bc5bee5021",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/paper_agent_73c709c0",
  "sessionId": "71c5797e-c964-4419-a009-2e487a4de1fc",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "ancient-greeting-comet",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01K4Mi7U2w9UrBqeS1K7P8gy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 5699,
      "cache_read_input_tokens": 65085,
      "output_tokens": 528,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5699
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 528,
          "cache_read_input_tokens": 65085,
          "cache_creation_input_tokens": 5699,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5699,
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

_source line 38 · 2026-05-20T19:54:40.832Z_

<details><summary>↩ Tool result · `toolu_011zexraCCk9ozabSG8DSCdg`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method.tex:62:The predicted cascade $\{H, \mathrm{ECE}\} \to \mathrm{Distinct}$-$n$ is confirmed in 15/15 experiments at $\alpha \geq 0.30$ ($t_H{=}1$, $t_D{=}2$ uniformly; \S\ref{sec:regime}); five low-$\alpha$ experiments show no detectable onset, leaving the ordering undefined below the detection floor.
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex:842:Among 15 experiments at $\alpha \geq 0.30$ (where entropy perturbation exceeds the detection threshold), cascade ordering $t_H \leq t_D$ holds in 15/15 cases ($t_H{=}1$, $t_D{=}2$ uniformly).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f0e09e56-d631-45c0-af4b-56bc5bee5021",
  "isSidechain": true,
  "promptId": "df7610aa-ce16-48cc-8465-cca12edac9f8",
  "agentId": "a0170d1e5ef70ae63",
  "type": "user",
  "uuid": "5a2845fd-41c0-42da-9173-5c7f1d12d382",
  "sourceToolAssistantUUID": "f0e09e56-d631-45c0-af4b-56bc5bee5021",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/paper_agent_73c709c0",
  "sessionId": "71c5797e-c964-4419-a009-2e487a4de1fc",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "ancient-greeting-comet"
}
```

</details>

---

### Assistant

_source line 39 · 2026-05-20T19:54:42.167Z_

Now let me search for the T=20 and directional verification markers:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5a2845fd-41c0-42da-9173-5c7f1d12d382",
  "isSidechain": true,
  "agentId": "a0170d1e5ef70ae63",
  "requestId": "req_011CbEQbLThV1fNvXNKkRXdH",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "518242d5-6c21-4388-8ef6-683aebbc6fb4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/paper_agent_73c709c0",
  "sessionId": "71c5797e-c964-4419-a009-2e487a4de1fc",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "ancient-greeting-comet",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01KWvN4JKbA65UXk2iZuVxqA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 1916,
      "cache_read_input_tokens": 70784,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1916,
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

_source line 40 · 2026-05-20T19:54:42.804Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01RFXZnmKMe2Hd81WxjNRHch`</summary>

```json
{
  "pattern": "T=20|T{=}20",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper",
  "output_mode": "content",
  "head_limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "518242d5-6c21-4388-8ef6-683aebbc6fb4",
  "isSidechain": true,
  "agentId": "a0170d1e5ef70ae63",
  "requestId": "req_011CbEQbLThV1fNvXNKkRXdH",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "e0e3ab9e-21b5-4712-bf00-906a49f08e6c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/paper_agent_73c709c0",
  "sessionId": "71c5797e-c964-4419-a009-2e487a4de1fc",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "ancient-greeting-comet",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01KWvN4JKbA65UXk2iZuVxqA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 1916,
      "cache_read_input_tokens": 70784,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1916,
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

_source line 41 · 2026-05-20T19:54:42.816Z_

<details><summary>↩ Tool result · `toolu_01RFXZnmKMe2Hd81WxjNRHch`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e0e3ab9e-21b5-4712-bf00-906a49f08e6c",
  "isSidechain": true,
  "promptId": "df7610aa-ce16-48cc-8465-cca12edac9f8",
  "agentId": "a0170d1e5ef70ae63",
  "type": "user",
  "uuid": "e44b92ea-d7b8-4eeb-8c6a-bda5d3691838",
  "sourceToolAssistantUUID": "e0e3ab9e-21b5-4712-bf00-906a49f08e6c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/paper_agent_73c709c0",
  "sessionId": "71c5797e-c964-4419-a009-2e487a4de1fc",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "ancient-greeting-comet"
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-20T19:54:43.224Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01X6x2LtCTzp3ibHFhyAUqgz`</summary>

```json
{
  "pattern": "directional assignment under verification",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e44b92ea-d7b8-4eeb-8c6a-bda5d3691838",
  "isSidechain": true,
  "agentId": "a0170d1e5ef70ae63",
  "requestId": "req_011CbEQbLThV1fNvXNKkRXdH",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d8e13122-369c-4eed-a024-9f31dc75e491",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/paper_agent_73c709c0",
  "sessionId": "71c5797e-c964-4419-a009-2e487a4de1fc",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "ancient-greeting-comet",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01KWvN4JKbA65UXk2iZuVxqA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 1916,
      "cache_read_input_tokens": 70784,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1916,
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

_source line 43 · 2026-05-20T19:54:43.239Z_

<details><summary>↩ Tool result · `toolu_01X6x2LtCTzp3ibHFhyAUqgz`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex:87:\multicolumn{7}{l}{\footnotesize $^\S$TY directional assignment under verification; row retained for completeness.} \\
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/conclusion.tex:9:The other four methods each fail in characteristic ways: naive cross-correlation inflates FPR to 75\%, differenced cross-correlation cannot separate forward from reverse precedence, threshold onset is power-limited at $T{=}10$ under $3\sigma$ calibration, and Toda--Yamamoto Granger provides supplementary detection at reduced power (directional assignment under verification).
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method.tex:22:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex:89:\multicolumn{9}{l}{\footnotesize $^\S$~TY directional assignment under verification.}
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex:504:\multicolumn{6}{l}{\footnotesize $^\S$TY directional assignment under verification; column retained for completeness.} \\
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d8e13122-369c-4eed-a024-9f31dc75e491",
  "isSidechain": true,
  "promptId": "df7610aa-ce16-48cc-8465-cca12edac9f8",
  "agentId": "a0170d1e5ef70ae63",
  "type": "user",
  "uuid": "179ee583-f8a0-4eff-8f12-d71ecfc98b36",
  "sourceToolAssistantUUID": "d8e13122-369c-4eed-a024-9f31dc75e491",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/paper_agent_73c709c0",
  "sessionId": "71c5797e-c964-4419-a009-2e487a4de1fc",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "ancient-greeting-comet"
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-20T19:54:43.938Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01RtFzk8ZWxEhy49GHRmwFCm`</summary>

```json
{
  "pattern": "sec:cascade.*referenced|cascade.*moment cascade|experiments.*cascade",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "179ee583-f8a0-4eff-8f12-d71ecfc98b36",
  "isSidechain": true,
  "agentId": "a0170d1e5ef70ae63",
  "requestId": "req_011CbEQbLThV1fNvXNKkRXdH",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "4d8c0ef8-7890-4e55-912f-ae64f0a1b4fd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/paper_agent_73c709c0",
  "sessionId": "71c5797e-c964-4419-a009-2e487a4de1fc",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "ancient-greeting-comet",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01KWvN4JKbA65UXk2iZuVxqA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 1916,
      "cache_read_input_tokens": 70784,
      "output_tokens": 387,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1916
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 387,
          "cache_read_input_tokens": 70784,
          "cache_creation_input_tokens": 1916,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1916,
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

_source line 45 · 2026-05-20T19:54:43.960Z_

<details><summary>↩ Tool result · `toolu_01RtFzk8ZWxEhy49GHRmwFCm`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex:842:Among 15 experiments at $\alpha \geq 0.30$ (where entropy perturbation exceeds the detection threshold), cascade ordering $t_H \leq t_D$ holds in 15/15 cases ($t_H{=}1$, $t_D{=}2$ uniformly).
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex:844:Five low-$\alpha$ experiments ($\alpha \leq 0.25$) show entropy perturbation below the detection threshold; cascade ordering is neither confirmed nor refuted in this regime.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4d8c0ef8-7890-4e55-912f-ae64f0a1b4fd",
  "isSidechain": true,
  "promptId": "df7610aa-ce16-48cc-8465-cca12edac9f8",
  "agentId": "a0170d1e5ef70ae63",
  "type": "user",
  "uuid": "a70dda23-4641-4dc9-8baa-81e3013f548e",
  "sourceToolAssistantUUID": "4d8c0ef8-7890-4e55-912f-ae64f0a1b4fd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/paper_agent_73c709c0",
  "sessionId": "71c5797e-c964-4419-a009-2e487a4de1fc",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "ancient-greeting-comet"
}
```

</details>

---

### Assistant

_source line 46 · 2026-05-20T19:54:45.003Z_

Let me search more specifically for cascade references in experiments.tex:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a70dda23-4641-4dc9-8baa-81e3013f548e",
  "isSidechain": true,
  "agentId": "a0170d1e5ef70ae63",
  "requestId": "req_011CbEQbZq7s64WZhDhZpWJr",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "5d5d04be-7eba-4e2d-a2c4-f927db402cfb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/paper_agent_73c709c0",
  "sessionId": "71c5797e-c964-4419-a009-2e487a4de1fc",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "ancient-greeting-comet",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01TrxyrRcM13dAV3ntxsB8r7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 1058,
      "cache_read_input_tokens": 72700,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1058,
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

_source line 47 · 2026-05-20T19:54:45.620Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01B7jqtpgPHAZ8KMruHx8WAJ`</summary>

```json
{
  "pattern": "moment cascade|cascade.*generation|entropy onset",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5d5d04be-7eba-4e2d-a2c4-f927db402cfb",
  "isSidechain": true,
  "agentId": "a0170d1e5ef70ae63",
  "requestId": "req_011CbEQbZq7s64WZhDhZpWJr",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "a598b34d-4273-4dbc-adff-f82541b414f3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/paper_agent_73c709c0",
  "sessionId": "71c5797e-c964-4419-a009-2e487a4de1fc",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "ancient-greeting-comet",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01TrxyrRcM13dAV3ntxsB8r7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 1058,
      "cache_read_input_tokens": 72700,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1058,
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

_source line 48 · 2026-05-20T19:54:45.632Z_

<details><summary>↩ Tool result · `toolu_01B7jqtpgPHAZ8KMruHx8WAJ`</summary>

```text
43:Independent of the Granger test, the degradation cascade confirms temporal precedence: entropy onset at generation~1 precedes distinct-$n$ onset at generation~2 in 16/18 WikiText conditions (Kendall $\tau{=}0.337$; \S\ref{sec:cascade}, Appendix~\ref{app:moment_cascade}).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a598b34d-4273-4dbc-adff-f82541b414f3",
  "isSidechain": true,
  "promptId": "df7610aa-ce16-48cc-8465-cca12edac9f8",
  "agentId": "a0170d1e5ef70ae63",
  "type": "user",
  "uuid": "510d04e3-3082-4062-80a5-6585af19ee66",
  "sourceToolAssistantUUID": "a598b34d-4273-4dbc-adff-f82541b414f3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/paper_agent_73c709c0",
  "sessionId": "71c5797e-c964-4419-a009-2e487a4de1fc",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "ancient-greeting-comet"
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-20T19:54:46.128Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01648JuTGTSm1AupQ97GXyVD`</summary>

```json
{
  "pattern": "F=449|F.*2947|F.*diversity|mauve.*F",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "510d04e3-3082-4062-80a5-6585af19ee66",
  "isSidechain": true,
  "agentId": "a0170d1e5ef70ae63",
  "requestId": "req_011CbEQbZq7s64WZhDhZpWJr",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "9dc86972-e5b4-492d-8c53-5bee2c479b98",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/paper_agent_73c709c0",
  "sessionId": "71c5797e-c964-4419-a009-2e487a4de1fc",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "ancient-greeting-comet",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01TrxyrRcM13dAV3ntxsB8r7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 1058,
      "cache_read_input_tokens": 72700,
      "output_tokens": 265,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1058
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 265,
          "cache_read_input_tokens": 72700,
          "cache_creation_input_tokens": 1058,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1058,
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

_source line 50 · 2026-05-20T19:54:46.149Z_

<details><summary>↩ Tool result · `toolu_01648JuTGTSm1AupQ97GXyVD`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex:42:At $\alpha{=}1.0$, all 24 canary$\to$diversity pairs (6 per seed $\times$ 4~seeds; mauve excluded) reach FDR significance in the forward direction with 0/24 reverse; directional asymmetry is robust across all WikiText conditions.
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex:50:\caption{Metric trajectories at $\alpha{=}1.0$ (Pythia-410M, 4~seeds). Token entropy drops at generation~1; distinct-1 declines from generations~2--3, with a consistent one-generation canary lead across all four seeds (shaded: inter-seed range). This pattern corresponds to 24/24 forward and 0/24 reverse FDR-significant canary$\to$diversity pairs (6 per seed, mauve excluded).}
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex:67:PermG counts are uniformly T-invariant: $6/8 \to 6/8$ in the detection regime ($\alpha \in \{0.50, 0.75, 1.0\}$) and $0/8 \to 0/8$ in the synchronous-collapse regime ($\alpha{=}0.60$), reflecting a structural ceiling where six diversity-based pairs are consistently significant ($F{=}449$--$2947$) while two mauve-based pairs show $F{<}2$ regardless of sequence length.
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/discussion.tex:9:First-differencing rules out shared trends: the canary$\to$diversity channel survives ($24/24 \to 24/24$) while canary$\to$perplexity vanishes entirely, scoping all canary claims to diversity metrics only (Appendix~\ref{app:channel_effect_size}).
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method.tex:8:\emph{Spurious regression}: first-differencing to remove shared trends~\cite{granger1974spurious} eliminates canary$\to$perplexity associations ($F{\approx}0$, $p{=}0.99$) while preserving canary$\to$diversity (24/24$\to$24/24), exposing an entire analysis channel as trend-driven rather than temporally precedent.
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method.tex:42:$T{=}20$ validates this prediction across four contamination levels: PermG yields 6/8 at $\alpha \in \{0.50, 0.75, 1.0\}$ and 0/8 at $\alpha{=}0.60$, all identical to $T{=}10$; six diversity-based pairs are consistently significant ($F{=}449$--$2947$) while two mauve-based pairs show $F{<}2$ regardless of sequence length (\S\ref{sec:dose_response}).
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method_reframe.tex:8:\emph{Spurious regression}: first-differencing to remove shared trends~\cite{granger1974spurious} eliminates canary$\to$perplexity associations ($F{\approx}0$, $p{=}0.99$) while preserving canary$\to$diversity (24/24$\to$24/24), exposing an entire analysis channel as trend-driven rather than temporally precedent.
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method_reframe.tex:52:False negative rate: at $\alpha{=}1.0$, all 6 effect-size reference pairs (2 canaries $\times$ 3 diversity metrics, selected by criteria independent of the detection methods) are recovered at 0\% FNR across 4 seeds.
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/abstract.tex:4:A multi-method consensus test comparing five statistical methods reveals that method choice alone inflates null-control FPR to 75\%; first-differencing eliminates all canary$\to$perplexity associations while preserving canary$\to$diversity leads, scoping the canary claim to diversity metrics only.
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex:60:For this reason, we report distinct-3 in this appendix rather than in the main text, where distinct-1 and distinct-2 provide cleaner evidence of the entropy-leads-diversity pattern.
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex:168:We construct 1{,}160 analytical specifications from the combinatorial space of: 13 contamination levels ($\alpha$ grid), seed selection ($\{42, 43, 44, 45\}$ where available), 8 canonical canary$\to$downstream pairs (\{token entropy, ECE\} $\times$ \{distinct-1, distinct-2, distinct-3, mauve\}), and method parameters (all PermG with $n_\text{perm}{=}5{,}000$, BH FDR $q{=}0.05$).
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex:453:First-differencing removes their shared downward trend: the canary$\to$diversity channel survives because entropy leads diversity by one generation, whereas the canary$\to$perplexity channel vanishes because both co-move synchronously.
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex:575:\caption{Shapley value decomposition (6-pair, mauve excluded). FPR-Shapley: marginal FPR contribution (positive = increases false positives). FNR-Shapley: marginal FNR contribution (negative = reduces false negatives). Combined = FPR + FNR (more negative = better). 48 experiments, $2^5{=}32$ coalitions, exact enumeration.}
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex:672:First-differencing eliminates all canary$\to$perplexity Granger associations while preserving canary$\to$diversity leads (\S\ref{sec:regime}).
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex:696:Within matched experiments (same model, seed, $\alpha$, precision), the Granger $F$-statistic is $20$--$28{\times}$ higher for diversity than perplexity channels.
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex:703:For diversity channels, 81\% of peak correlations occur at canary-leading lags (lag${<}0$), with a median lag of $-1$ generation---consistent with the one-generation temporal precedence visible in Figure~\ref{fig:metric_trajectory}.
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex:872:Six diversity-based pairs show $F{=}449$--$2947$ at $T{=}20$ (all $\gg F_{\text{crit}}$); two mauve-based pairs show $F{<}2$ regardless of $T$, confirming the structural ceiling interpretation.
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/introduction.tex:40:    The MMCT exposes three pitfalls: naive cross-correlation has 75\% null-control FPR ($\kappa{=}0.185$ inter-method), first-differencing eliminates canary$\to$perplexity associations entirely while preserving all canary$\to$diversity leads (24/24$\to$24/24), and regime dependence causes the same test to shift from 0--6/8 FDR-significant pairs per seed at $\alpha{\geq}0.75$ to 0/8 at $\alpha{\leq}0.45$.
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/main.aux:569:\@writefile{lof}{\contentsline {figure}{\numberline {2}{\ignorespaces Metric trajectories at $\alpha {=}1.0$ (Pythia-410M, 4~seeds). Token entropy drops at generation~1; distinct-1 declines from generations~2--3, with a consistent one-generation canary lead across all four seeds (shaded: inter-seed range). This pattern corresponds to 24/24 forward and 0/24 reverse FDR-significant canary$\to $diversity pairs (6 per seed, mauve excluded).}}{6}{figure.caption.10}\protected@file@percent }
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/main.aux:570:\newlabel{fig:metric_trajectory}{{2}{6}{Metric trajectories at $\alpha {=}1.0$ (Pythia-410M, 4~seeds). Token entropy drops at generation~1; distinct-1 declines from generations~2--3, with a consistent one-generation canary lead across all four seeds (shaded: inter-seed range). This pattern corresponds to 24/24 forward and 0/24 reverse FDR-significant canary$\to $diversity pairs (6 per seed, mauve excluded)}{figure.caption.10}{}}
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/main.aux:1598:\@writefile{lot}{\contentsline {table}{\numberline {19}{\ignorespaces Shapley value decomposition (6-pair, mauve excluded). FPR-Shapley: marginal FPR contribution (positive = increases false positives). FNR-Shapley: marginal FNR contribution (negative = reduces false negatives). Combined = FPR + FNR (more negative = better). 48 experiments, $2^5{=}32$ coalitions, exact enumeration.}}{17}{table.caption.64}\protected@file@percent }
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/main.aux:1599:\newlabel{tab:shapley_6pair}{{19}{17}{Shapley value decomposition (6-pair, mauve excluded). FPR-Shapley: marginal FPR contribution (positive = increases false positives). FNR-Shapley: marginal FNR contribution (negative = reduces false negatives). Combined = FPR + FNR (more negative = better). 48 experiments, $2^5{=}32$ coalitions, exact enumeration}{table.caption.64}{}}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9dc86972-e5b4-492d-8c53-5bee2c479b98",
  "isSidechain": true,
  "promptId": "df7610aa-ce16-48cc-8465-cca12edac9f8",
  "agentId": "a0170d1e5ef70ae63",
  "type": "user",
  "uuid": "343141fc-59d8-467f-b1d7-30cc6a3075aa",
  "sourceToolAssistantUUID": "9dc86972-e5b4-492d-8c53-5bee2c479b98",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/paper_agent_73c709c0",
  "sessionId": "71c5797e-c964-4419-a009-2e487a4de1fc",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "ancient-greeting-comet"
}
```

</details>

---

### Assistant

_source line 51 · 2026-05-20T19:54:47.750Z_

Perfect! I found the reference. Now let me check the concrete references between introduction and method sections for the S×R lens naming issue:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "343141fc-59d8-467f-b1d7-30cc6a3075aa",
  "isSidechain": true,
  "agentId": "a0170d1e5ef70ae63",
  "requestId": "req_011CbEQbj9x8nKZBYCWVJ4kp",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "0e94302a-b1fb-47a4-be38-f3308654c2f6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/paper_agent_73c709c0",
  "sessionId": "71c5797e-c964-4419-a009-2e487a4de1fc",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "ancient-greeting-comet",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Co9fgpXNMES2U5MKBx36eh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 3406,
      "cache_read_input_tokens": 73758,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3406,
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

_source line 52 · 2026-05-20T19:54:48.599Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01SrpaSvWzp49vfMnR4FnD3v`</summary>

```json
{
  "pattern": "S.*R.*interpretive|Signal.*Resolution.*interpretive|Signal-times-resolution|lens.*S.*R",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/introduction.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0e94302a-b1fb-47a4-be38-f3308654c2f6",
  "isSidechain": true,
  "agentId": "a0170d1e5ef70ae63",
  "requestId": "req_011CbEQbj9x8nKZBYCWVJ4kp",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "86ff11c1-f885-448e-9a44-93cf8f8d182e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/paper_agent_73c709c0",
  "sessionId": "71c5797e-c964-4419-a009-2e487a4de1fc",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "ancient-greeting-comet",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Co9fgpXNMES2U5MKBx36eh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 3406,
      "cache_read_input_tokens": 73758,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3406,
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

_source line 53 · 2026-05-20T19:54:48.646Z_

<details><summary>↩ Tool result · `toolu_01SrpaSvWzp49vfMnR4FnD3v`</summary>

```text
24:A signal-times-resolution ($S \times R$) interpretive lens explains this onset and the non-monotonic dose-response through competing signal strength and temporal resolution.
36:    \item \textbf{Signal-times-resolution interpretive lens} (\S\ref{sec:theory}).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "86ff11c1-f885-448e-9a44-93cf8f8d182e",
  "isSidechain": true,
  "promptId": "df7610aa-ce16-48cc-8465-cca12edac9f8",
  "agentId": "a0170d1e5ef70ae63",
  "type": "user",
  "uuid": "83928968-a4eb-4607-b46b-9c0287124e68",
  "sourceToolAssistantUUID": "86ff11c1-f885-448e-9a44-93cf8f8d182e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/paper_agent_73c709c0",
  "sessionId": "71c5797e-c964-4419-a009-2e487a4de1fc",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "ancient-greeting-comet"
}
```

</details>

---

### Tool call

_source line 54 · 2026-05-20T19:54:48.957Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01SuHDEZ74reNkKgqTAKhPsY`</summary>

```json
{
  "pattern": "framework.*Signal",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/introduction.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "83928968-a4eb-4607-b46b-9c0287124e68",
  "isSidechain": true,
  "agentId": "a0170d1e5ef70ae63",
  "requestId": "req_011CbEQbj9x8nKZBYCWVJ4kp",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "1ded5e1a-077d-4f02-9d29-42f73dfb8b81",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/paper_agent_73c709c0",
  "sessionId": "71c5797e-c964-4419-a009-2e487a4de1fc",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "ancient-greeting-comet",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Co9fgpXNMES2U5MKBx36eh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 3406,
      "cache_read_input_tokens": 73758,
      "output_tokens": 286,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3406
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 286,
          "cache_read_input_tokens": 73758,
          "cache_creation_input_tokens": 3406,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3406,
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

_source line 55 · 2026-05-20T19:54:48.974Z_

<details><summary>↩ Tool result · `toolu_01SuHDEZ74reNkKgqTAKhPsY`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1ded5e1a-077d-4f02-9d29-42f73dfb8b81",
  "isSidechain": true,
  "promptId": "df7610aa-ce16-48cc-8465-cca12edac9f8",
  "agentId": "a0170d1e5ef70ae63",
  "type": "user",
  "uuid": "ab4081b1-9783-42f7-b7ee-60b8dc419f92",
  "sourceToolAssistantUUID": "1ded5e1a-077d-4f02-9d29-42f73dfb8b81",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/paper_agent_73c709c0",
  "sessionId": "71c5797e-c964-4419-a009-2e487a4de1fc",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "ancient-greeting-comet"
}
```

</details>

---

### Assistant

_source line 56 · 2026-05-20T19:54:50.196Z_

Great! Now I found one issue. Let me check the reframe files that had inconsistencies:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ab4081b1-9783-42f7-b7ee-60b8dc419f92",
  "isSidechain": true,
  "agentId": "a0170d1e5ef70ae63",
  "requestId": "req_011CbEQbwHhd9gSYMN8KXp8D",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "67323d56-b97f-45e0-88e1-51c9342324b2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/paper_agent_73c709c0",
  "sessionId": "71c5797e-c964-4419-a009-2e487a4de1fc",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "ancient-greeting-comet",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01GH2D4fvMVhMmqrZeEXWyFM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 521,
      "cache_read_input_tokens": 77164,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 521,
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

_source line 57 · 2026-05-20T19:54:50.637Z_

<details open><summary>🔧 Tool call — Read · `toolu_01D3GHcHSfqinJDMHSrDWEeg`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments_reframe.tex",
  "offset": 1,
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "67323d56-b97f-45e0-88e1-51c9342324b2",
  "isSidechain": true,
  "agentId": "a0170d1e5ef70ae63",
  "requestId": "req_011CbEQbwHhd9gSYMN8KXp8D",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "809fbaf5-29f9-4d81-b713-ef6d7fa0b1e9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/paper_agent_73c709c0",
  "sessionId": "71c5797e-c964-4419-a009-2e487a4de1fc",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "ancient-greeting-comet",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01GH2D4fvMVhMmqrZeEXWyFM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 521,
      "cache_read_input_tokens": 77164,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 521,
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

_source line 58 · 2026-05-20T19:54:50.651Z_

<details><summary>↩ Tool result · `toolu_01D3GHcHSfqinJDMHSrDWEeg`</summary>

```text
1	\subsection{Sharp Detection Onset}
2	\label{sec:regime}
3	
4	Diversity collapse occurs at every contamination level: distinct-1 declines by $14.1\%$ at $\alpha{=}0.0$ (fine-tuning drift) and by $40.3{\pm}0.3\%$ at $\alpha{=}0.25$ (3-seed mean).
5	Despite this ubiquitous degradation, Granger-causal detectability is sharply regime-dependent.
6	Permutation Granger (PermG) tests find 0/8 canary$\to$downstream pairs FDR-significant from $\alpha{=}0.00$ through $\alpha{=}0.45$, then jump to 6/8 at $\alpha{=}0.50$ (2~fp32 seeds, consistent).
7	This transition is striking because cumulative synthetic fraction barely changes across the boundary: $C = 1{-}(1{-}\alpha)^{10}$ yields $99.75\%$ at $\alpha{=}0.45$ versus $99.90\%$ at $\alpha{=}0.50$, a difference of 0.15 percentage points, yet detection jumps from null to reliable.
8	Sigmoid regression across the 13-point $\alpha$ grid quantifies this steep onset: $\alpha_c = 0.476$ at $T{=}10$, steepness $k \geq 200$, transition width $\Delta\alpha \approx 0.02$, $R^2 = 0.969$ (versus power-law $R^2 = 0.808$, $\Delta\mathrm{AIC} = 18.2$; Figure~\ref{fig:phase_transition}).
9	At $\alpha{=}0.45$, PermG $p$-values reveal sub-threshold signal ($p_{\mathrm{fdr}} = 0.059$ for seed~43, $0.091$ for seed~42), consistent with the power-threshold interpretation of $\alpha_c$ at $T{=}10$ (\S\ref{sec:theory}): the onset reflects PermG's power curve crossing the detection floor, not the emergence of a new physical signal.
10	A specification curve analysis spanning 1{,}160 analytical specifications confirms that the sharp detection onset is specification-invariant.
11	
12	First-differencing scopes the canary claim precisely.
13	Canary$\to$diversity pairs retain unanimous FDR significance after first-differencing ($24/24 \to 24/24$ across 4~seeds at $\alpha{=}1.0$), while canary$\to$perplexity collapses entirely ($F \approx 0$, $p = 0.99$): the apparent perplexity association is a shared-trend artifact.
14	All canary claims are therefore scoped to diversity metrics only.
15	At $\alpha{=}1.0$, 24/24 forward-direction pairs reach FDR significance with 0/24 reverse (4~seeds); directional asymmetry is robust across all WikiText conditions.
16	The canary mechanism also exhibits a blind spot: at $\alpha{=}0.10$, distinct-1 has already dropped by $39.6\%$, yet token entropy is indistinguishable from the null ($-5.3\%$ versus $-4.6{\pm}0.4\%$ at $\alpha{=}0.0$).\footnote{Seed~43 at $\alpha{=}0.10$ shows 3/8 PermG FDR-significant pairs versus 0/8 for seed~42, consistent with stochastic variation at low signal rather than robust detection; no other below-threshold $\alpha$ level exhibits seed-dependent detection.}
17	Below $\alpha_c$ at $T{=}10$, diversity collapse proceeds without any detectable Granger-causal signal in the canary metrics.
18	
19	\begin{figure}[t]
20	\centering
21	\includegraphics[width=\linewidth]{figures/metric_trajectory.pdf}
22	\caption{Metric trajectories at $\alpha{=}1.0$ (Pythia-410M, 4~seeds). Token entropy drops at generation~1; distinct-1 declines from generations~2--3, with a consistent one-generation canary lead across all four seeds (shaded: inter-seed range). This pattern corresponds to 24/24 forward and 0/24 reverse FDR-significant pairs.}
23	\label{fig:metric_trajectory}
24	\end{figure}
25	
26	
27	\subsection{Dose-Response and the $S \times R$ Framework}
28	\label{sec:dose_response}
29	
30	The PermG dose-response profile (Figure~\ref{fig:regime_map}) reveals four detection regimes: \emph{blind} ($\alpha \leq 0.45$, 0/8 FDR-significant pairs), \emph{onset} ($\alpha \approx 0.50$, 6/8), \emph{synchronous dip} ($\alpha \approx 0.60$, 0/8 both seeds; dual-seed confirmed), and \emph{detection} ($\alpha{=}0.75$, 0--6/8 per seed, 2 of 3 seeds ${\geq}5/8$; $\alpha{=}1.0$, 6/8 across 4~seeds).
31	The non-monotonic dip at $\alpha{=}0.60$ is consistent with the $S \times R$ framework (\S\ref{sec:theory}): signal strength $S(\alpha)$ rises monotonically with contamination, but temporal resolution $R(\alpha)$ drops when relaxation time approaches the observation interval.
32	At $\alpha \approx 0.60$, this compression drives the canary-to-downstream lag toward zero, and the product $S \times R$ reaches a local minimum.
33	The synchronous zone is mechanistically distinct from the blind spot: in the blind zone, canary drift is indistinguishable from the null; in the synchronous zone, both canary and downstream metrics drift substantially but without temporal offset.
34	At $\alpha{=}0.55$, PermG returns 0/8 FDR-significant pairs despite marginal $p$-values ($p_{\mathrm{fdr}}{=}0.062$--$0.092$), consistent with power-limited non-detection between onset and synchronous dip; differenced cross-correlation detects 8/8 bidirectionally at this level, confirming that a lead-lag signal exists but falls below PermG's directional detection threshold.
35	
36	Method choice is itself a major source of analytic variability.
37	At $\alpha{=}1.0$, forward-direction significance rates range from 100\% (naive cross-correlation) to 37.5\% (PermG), with inter-method $\kappa = 0.185$ (near chance) and a spurious rate of at least 62.5\%.
38	PermG is the only method that combines zero null-control FPR with consistent detection at $\alpha \geq 0.50$ (Table~\ref{tab:method_comparison}); its nonparametric null distribution, built-in directionality, and hyperparameter-free design explain this advantage.
39	The $S \times R$ framework generates three testable predictions for $T{=}20$ via $\mathrm{Power}(\alpha, T) = \Phi(S \cdot R \cdot \sqrt{T}/\sigma)$: (i)~$\alpha_c$ at $T{=}10$ should left-shift, (ii)~the transition should smooth, and (iii)~different methods should exhibit different $\alpha_c$ values.
40	These predictions are under empirical verification.
41	
42	\begin{figure}[t]
43	\centering
44	\includegraphics[width=\linewidth]{figures/fig_dose_response.pdf}
45	\caption{PermG forward detection rate across 13 contamination levels (Pythia-410M, fp32, direction-checked). Four regimes: blind ($\alpha \leq 0.45$, 0/8), onset ($\alpha{=}0.50$, 6/8), synchronous dip ($\alpha{=}0.60$, 0/8), and detection ($\alpha \geq 0.75$, 0--6/8).}
46	\label{fig:regime_map}
47	\end{figure}
48	
49	\begin{table}[t]
50	\centering
51	\small
52	\caption{Forward-direction FDR significance rates (\%) across contamination levels (Pythia-410M, seed~42, fp32, direction-checked). Each cell: fraction of 8 validated pairs at BH-corrected significance ($q{=}0.05$). PermG achieves zero null-control FPR with consistent detection at $\alpha \geq 0.50$.}
53	\label{tab:method_comparison}
54	\begin{tabular}{lcccccc}
55	\toprule
56	Method & $\alpha{=}0.0$ & $\alpha{=}0.25$ & $\alpha{=}0.50$ & $\alpha{=}0.75$ & $\alpha{=}1.0$ & FPR$_\text{null}$ \\
57	\midrule
58	Naive XCorr          & 75   & 12.5 & 37.5 & 87.5 & 0    & 75  \\
59	Diff.\ XCorr         & 0    & 37.5 & 87.5 & 75   & 75   & 0   \\
60	Threshold ($3\sigma$) & ---  & 0    & 50   & 0    & 0    & --- \\
61	Perm.\ Granger       & 0    & 0    & 75   & 75   & 75   & 0   \\
62	Toda--Yamamoto       & ---  & 0    & 37.5 & 37.5 & 50   & --- \\
63	\bottomrule
64	\end{tabular}
65	\end{table}
66	
67	
68	\subsection{Cross-Architecture Generalization}
69	\label{sec:generalization}
70	
71	We evaluate the sharp detection onset across 15 model-seed combinations spanning six families (Pythia, GPT-2, OPT, Qwen, SmolLM3, Padding-variant), scales from 345M to 6.9B parameters, and two training domains (WikiText-103, C4).
72	Table~\ref{tab:generalization} reports PermG forward detection at $\alpha{=}1.0$.
73	PermG forward significance reaches ${\geq}$6/8 in 13 of 15 conditions (87\%).
74	Two exceptions emerge: Pythia-1.4B seed~42 on WikiText (2/8), a seed-dependent outlier that recovers to 6/8 in seed~43, and SmolLM3-3B (3/8), where only ECE$\to$downstream pairs reach significance while entropy$\to$downstream pairs fail entirely (0/4; details in Appendix).
75	SmolLM3's token entropy exhibits non-monotonic oscillations across generations; this pattern violates the monotonic decline that Granger tests require.
76	The onset boundary $\alpha_c \approx 0.50$ at $T{=}10$ is architecture-independent: every family that achieves detection does so at or above this threshold, and none achieves reliable detection below it.
77	
78	Replacing WikiText-103 with C4 yields the strongest detection observed: Pythia-1B reaches PermG~fwd 8/8 (2~seeds), and Pythia-1.4B reaches 8/8 on C4 versus 2/8 on WikiText at the same scale.
79	At Pythia-6.9B (bf16), detection recovers to 7/8 on WikiText.
80	Dataset characteristics modulate detection power independently of model capacity.
81	Directional asymmetry also varies by domain: at $\alpha{=}0.50$ on C4, PermG reverse reaches 7/8, compared to 0/24 across all WikiText conditions.
82	This domain-dependent bidirectionality suggests that the unidirectional forward causation observed on WikiText may partly reflect domain-specific dynamics (\S\ref{sec:discussion}).
83	
84	\begin{table}[t]
85	\centering
86	\small
87	\caption{Cross-architecture PermG forward detection ($\alpha{=}1.0$). Detection (${\geq}$6/8) confirmed in 13/15 conditions (87\%) across six model families, scales from 345M to 6.9B, and two domains.}
88	\label{tab:generalization}
89	\begin{tabular}{lrcl}
90	\toprule
91	Model & Params & Domain & PermG fwd \\
92	\midrule
93	Pythia-410M    & 410M & Wiki & 6/8 \\
94	Pythia-1.4B    & 1.4B & Wiki & 2--6/8$^\dagger$ \\
95	Pythia-6.9B    & 6.9B & Wiki & 7/8$^*$ \\
96	GPT-2-medium   & 345M & Wiki & 6/8 \\
97	OPT-1.3B       & 1.3B & Wiki & 6/8 \\
98	Qwen3.5-0.8B   & 0.8B & Wiki & 8/8 \\
99	SmolLM3-3B     & 3.0B & Wiki & 3/8$^\ddagger$ \\
100	Padding-410M   & 410M & Wiki & 6/8 \\
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "809fbaf5-29f9-4d81-b713-ef6d7fa0b1e9",
  "isSidechain": true,
  "promptId": "df7610aa-ce16-48cc-8465-cca12edac9f8",
  "agentId": "a0170d1e5ef70ae63",
  "type": "user",
  "uuid": "5cb119de-9793-43c2-b285-c5cdc2491311",
  "sourceToolAssistantUUID": "809fbaf5-29f9-4d81-b713-ef6d7fa0b1e9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/paper_agent_73c709c0",
  "sessionId": "71c5797e-c964-4419-a009-2e487a4de1fc",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "ancient-greeting-comet"
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-20T19:54:51.062Z_

<details open><summary>🔧 Tool call — Read · `toolu_01UZS6PTciQGk9m4X7YcWR8T`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method_reframe.tex",
  "offset": 30,
  "limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5cb119de-9793-43c2-b285-c5cdc2491311",
  "isSidechain": true,
  "agentId": "a0170d1e5ef70ae63",
  "requestId": "req_011CbEQbwHhd9gSYMN8KXp8D",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "cf4829a6-a29a-4048-975b-4d2b0910d8e5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/paper_agent_73c709c0",
  "sessionId": "71c5797e-c964-4419-a009-2e487a4de1fc",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "ancient-greeting-comet",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01GH2D4fvMVhMmqrZeEXWyFM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 521,
      "cache_read_input_tokens": 77164,
      "output_tokens": 257,
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
          "input_tokens": 6,
          "output_tokens": 257,
          "cache_read_input_tokens": 77164,
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

### Tool result

_source line 60 · 2026-05-20T19:54:51.067Z_

<details><summary>↩ Tool result · `toolu_01UZS6PTciQGk9m4X7YcWR8T`</summary>

```text
30	We apply standard statistical power scaling to PermG under the Signal$\times$Resolution (S$\times$R) framework.
31	Detectability of canary$\to$downstream temporal precedence depends on two competing factors:
32	\begin{equation}
33	    \text{Detectability}(\alpha) \;\propto\; S(\alpha) \times R(\alpha),
34	    \label{eq:detectability}
35	\end{equation}
36	where $S(\alpha)$ is signal strength (magnitude of distributional shift, monotonically increasing with $\alpha$) and $R(\alpha)$ is temporal resolution (the generational gap between canary and downstream responses).
37	$R(\alpha)$ is non-monotonic: at low $\alpha$, entropy and diversity respond in different generations ($R$ large); at $\alpha{\approx}0.60$, relaxation time matching compresses both responses into a single generation ($R \to 0$); at high $\alpha$, the severity of entropy collapse outpaces the diversity cascade, restoring the generational offset.
38	The product $S \times R$ predicts four regimes: \emph{blind} ($\alpha \leq 0.45$; $S$ below detection floor), \emph{onset} ($\alpha \approx 0.50$; $S$ crosses threshold while $R$ remains high), \emph{synchronous dip} ($\alpha \approx 0.60$; $R \to 0$ suppresses detection despite rising $S$), and \emph{detection} ($\alpha \geq 0.75$; $S$ dominates).
39	Full empirical confirmation appears in \S\ref{sec:regime} and \S\ref{sec:dose_response}.
40	
41	Under a permutation test framework, detection power scales as $\mathrm{Power}(\alpha, T) = \Phi\bigl(S \cdot R \cdot \sqrt{T} / \sigma_{\mathrm{noise}}\bigr)$, where $\Phi$ is the standard normal CDF and the $\sqrt{T}$ scaling follows standard power analysis.
42	The sharp detection onset at $\alpha_c$ (at $T{=}10$) is consistent with a power threshold: when $S \cdot R \cdot \sqrt{T}$ first exceeds the detection floor, power undergoes a steep onset from near-zero to near-one.
43	This generates three predictions for $T{=}20$: (i)~$\alpha_c$ left-shifts as increased $T$ raises power at all $\alpha$; (ii)~the transition smooths as $\sqrt{T}$ broadens the power curve; (iii)~different methods exhibit different $\alpha_c$ values due to method-specific power curves.
44	Bootstrap calibration ($N{=}10{,}000$) yields clean falsifiable tests at $\alpha{\geq}0.75$: predicted 7/8 (95\% CI: [6,8]); results below 6/8 would falsify $\sqrt{T}$ power scaling.
45	At $\alpha{=}0.45$, the point prediction is 0/8, but the bootstrap CI spans [0,7] reflecting $\alpha_c$ uncertainty---both detection and non-detection are informative for constraining the phase boundary location.
46	At $\alpha{=}0.50$, the prediction is inherently uncertain at the transition (CI: [0,7]).
47	Sub-threshold FDR $p{=}0.059$--$0.091$ at $\alpha{=}0.45$ is consistent with proximity to the power boundary.
48	
49	\paragraph{Calibration.}
50	We validate error rates with built-in experimental controls.
51	False positive rate: at $\alpha{=}0.0$ (null control, no synthetic contamination), PermG and MMCT weighted consensus both yield 0\% FPR across 3 seeds (0/24 pairs at consensus $K{\geq}3$).
52	False negative rate: at $\alpha{=}1.0$, all 6 effect-size reference pairs (2 canaries $\times$ 3 diversity metrics, selected by criteria independent of the detection methods) are recovered at 0\% FNR across 4 seeds.
53	PermG matches consensus performance at all tested contamination levels, with cross-architecture validation confirming PermG forward significance ${\geq}6/8$ in 13 of 15 conditions (\S\ref{sec:generalization}).
54	Full calibration details, practical guidance tiers, and method-level breakdown appear in the Appendix.
55	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cf4829a6-a29a-4048-975b-4d2b0910d8e5",
  "isSidechain": true,
  "promptId": "df7610aa-ce16-48cc-8465-cca12edac9f8",
  "agentId": "a0170d1e5ef70ae63",
  "type": "user",
  "uuid": "68ad78f0-529e-46d5-837e-fa6a4b12628e",
  "sourceToolAssistantUUID": "cf4829a6-a29a-4048-975b-4d2b0910d8e5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/paper_agent_73c709c0",
  "sessionId": "71c5797e-c964-4419-a009-2e487a4de1fc",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "ancient-greeting-comet"
}
```

</details>

---

### Assistant

_source line 61 · 2026-05-20T19:54:52.750Z_

Excellent! I found another issue. Now let me check the abstract and introduction for consistency on T=20 data:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "68ad78f0-529e-46d5-837e-fa6a4b12628e",
  "isSidechain": true,
  "agentId": "a0170d1e5ef70ae63",
  "requestId": "req_011CbEQc6QdVrVbmmH5KinwT",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "418b1d81-dfbe-43b0-a6be-2db88a15365c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/paper_agent_73c709c0",
  "sessionId": "71c5797e-c964-4419-a009-2e487a4de1fc",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "ancient-greeting-comet",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011mMpbvUaXLCZCG9vRf2jJg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 4975,
      "cache_read_input_tokens": 77685,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4975,
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

_source line 62 · 2026-05-20T19:54:53.808Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01QKbMNoxKGH2kCEiL4Wi4UR`</summary>

```json
{
  "pattern": "T=20|T{=}20",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/abstract.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "418b1d81-dfbe-43b0-a6be-2db88a15365c",
  "isSidechain": true,
  "agentId": "a0170d1e5ef70ae63",
  "requestId": "req_011CbEQc6QdVrVbmmH5KinwT",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d20baf83-b862-439f-b50e-cc2874f3b483",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/paper_agent_73c709c0",
  "sessionId": "71c5797e-c964-4419-a009-2e487a4de1fc",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "ancient-greeting-comet",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011mMpbvUaXLCZCG9vRf2jJg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 4975,
      "cache_read_input_tokens": 77685,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4975,
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

_source line 63 · 2026-05-20T19:54:53.817Z_

<details><summary>↩ Tool result · `toolu_01QKbMNoxKGH2kCEiL4Wi4UR`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d20baf83-b862-439f-b50e-cc2874f3b483",
  "isSidechain": true,
  "promptId": "df7610aa-ce16-48cc-8465-cca12edac9f8",
  "agentId": "a0170d1e5ef70ae63",
  "type": "user",
  "uuid": "a2b576b9-0d58-4202-a364-397bf9f42b40",
  "sourceToolAssistantUUID": "d20baf83-b862-439f-b50e-cc2874f3b483",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/paper_agent_73c709c0",
  "sessionId": "71c5797e-c964-4419-a009-2e487a4de1fc",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "ancient-greeting-comet"
}
```

</details>

---

### Tool call

_source line 64 · 2026-05-20T19:54:54.019Z_

<details open><summary>🔧 Tool call — Grep · `toolu_019ghmFd8skk2p6UgbmpUUzX`</summary>

```json
{
  "pattern": "T=20|T{=}20",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/introduction.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a2b576b9-0d58-4202-a364-397bf9f42b40",
  "isSidechain": true,
  "agentId": "a0170d1e5ef70ae63",
  "requestId": "req_011CbEQc6QdVrVbmmH5KinwT",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "7241c0a9-18ec-4302-9fa8-615b87dfe19d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/paper_agent_73c709c0",
  "sessionId": "71c5797e-c964-4419-a009-2e487a4de1fc",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "ancient-greeting-comet",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011mMpbvUaXLCZCG9vRf2jJg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 4975,
      "cache_read_input_tokens": 77685,
      "output_tokens": 273,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4975
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 273,
          "cache_read_input_tokens": 77685,
          "cache_creation_input_tokens": 4975,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4975,
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

_source line 65 · 2026-05-20T19:54:54.028Z_

<details><summary>↩ Tool result · `toolu_019ghmFd8skk2p6UgbmpUUzX`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7241c0a9-18ec-4302-9fa8-615b87dfe19d",
  "isSidechain": true,
  "promptId": "df7610aa-ce16-48cc-8465-cca12edac9f8",
  "agentId": "a0170d1e5ef70ae63",
  "type": "user",
  "uuid": "52fbd03f-33f2-4751-ad33-d9239c105fac",
  "sourceToolAssistantUUID": "7241c0a9-18ec-4302-9fa8-615b87dfe19d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/paper_agent_73c709c0",
  "sessionId": "71c5797e-c964-4419-a009-2e487a4de1fc",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "ancient-greeting-comet"
}
```

</details>

---

### Assistant

_source line 66 · 2026-05-20T19:54:55.626Z_

Let me search for the T=20 predictions specifically in method.tex more carefully:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "52fbd03f-33f2-4751-ad33-d9239c105fac",
  "isSidechain": true,
  "agentId": "a0170d1e5ef70ae63",
  "requestId": "req_011CbEQcJyvpeT2vNB9V4xTr",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "0553c179-0760-4e45-9222-9d40b4117a6f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/paper_agent_73c709c0",
  "sessionId": "71c5797e-c964-4419-a009-2e487a4de1fc",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "ancient-greeting-comet",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_019zH8N1BuiVamYgGmB6K196",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 340,
      "cache_read_input_tokens": 82660,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 340,
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

_source line 67 · 2026-05-20T19:54:55.728Z_

<details open><summary>🔧 Tool call — Bash · `toolu_013Ew2X1YGfmMRF523V5mTFk`</summary>

```json
{
  "command": "grep -n \"T{=}20\\|T=20\" /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0553c179-0760-4e45-9222-9d40b4117a6f",
  "isSidechain": true,
  "agentId": "a0170d1e5ef70ae63",
  "requestId": "req_011CbEQcJyvpeT2vNB9V4xTr",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "89dbc008-e514-43d0-be81-7df3a1d4a0a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/paper_agent_73c709c0",
  "sessionId": "71c5797e-c964-4419-a009-2e487a4de1fc",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "ancient-greeting-comet",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_019zH8N1BuiVamYgGmB6K196",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 340,
      "cache_read_input_tokens": 82660,
      "output_tokens": 122,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 340
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 122,
          "cache_read_input_tokens": 82660,
          "cache_creation_input_tokens": 340,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 340,
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

_source line 68 · 2026-05-20T19:54:55.784Z_

<details><summary>↩ Tool result · `toolu_013Ew2X1YGfmMRF523V5mTFk`</summary>

```text
42:$T{=}20$ validates this prediction across four contamination levels: PermG yields 6/8 at $\alpha \in \{0.50, 0.75, 1.0\}$ and 0/8 at $\alpha{=}0.60$, all identical to $T{=}10$; six diversity-based pairs are consistently significant ($F{=}449$--$2947$) while two mauve-based pairs show $F{<}2$ regardless of sequence length (\S\ref{sec:dose_response}).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "89dbc008-e514-43d0-be81-7df3a1d4a0a4",
  "isSidechain": true,
  "promptId": "df7610aa-ce16-48cc-8465-cca12edac9f8",
  "agentId": "a0170d1e5ef70ae63",
  "type": "user",
  "uuid": "7b39f4d2-c922-44c5-b0b4-ded5d19638b3",
  "sourceToolAssistantUUID": "89dbc008-e514-43d0-be81-7df3a1d4a0a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/paper_agent_73c709c0",
  "sessionId": "71c5797e-c964-4419-a009-2e487a4de1fc",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "ancient-greeting-comet"
}
```

</details>

---

### Assistant

_source line 69 · 2026-05-20T19:54:57.237Z_

Good. Now let me create a comprehensive summary. Let me verify a few more items systematically by checking the original vs reframed files to see if both versions are present:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7b39f4d2-c922-44c5-b0b4-ded5d19638b3",
  "isSidechain": true,
  "agentId": "a0170d1e5ef70ae63",
  "requestId": "req_011CbEQcSJxQ3oTQ9CzCKCNi",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "1f60ec42-1ba8-4ef7-b89c-03c9f2847ffb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/paper_agent_73c709c0",
  "sessionId": "71c5797e-c964-4419-a009-2e487a4de1fc",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "ancient-greeting-comet",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01WSDQBdYyEpVjKykWRiQbv6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 267,
      "cache_read_input_tokens": 83000,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 267,
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

_source line 70 · 2026-05-20T19:54:57.524Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01U6dbbKaBQdEYMpdKvVhrV9`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper && ls -la *.tex | grep -E \"(experiment|method|intro|discussion)\" | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1f60ec42-1ba8-4ef7-b89c-03c9f2847ffb",
  "isSidechain": true,
  "agentId": "a0170d1e5ef70ae63",
  "requestId": "req_011CbEQcSJxQ3oTQ9CzCKCNi",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "bf8a5048-4db7-4dca-bc2f-fc513f1b9e2d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/paper_agent_73c709c0",
  "sessionId": "71c5797e-c964-4419-a009-2e487a4de1fc",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "ancient-greeting-comet",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01WSDQBdYyEpVjKykWRiQbv6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 267,
      "cache_read_input_tokens": 83000,
      "output_tokens": 146,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 267
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 146,
          "cache_read_input_tokens": 83000,
          "cache_creation_input_tokens": 267,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 267,
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

_source line 71 · 2026-05-20T19:54:57.591Z_

<details><summary>↩ Tool result · `toolu_01U6dbbKaBQdEYMpdKvVhrV9`</summary>

```text
-rw-r--r-- 1 ubuntu ubuntu  3417 May 20 18:36 discussion.tex
-rw-r--r-- 1 ubuntu ubuntu  4146 May 20 15:35 discussion_reframe.tex
-rw-r--r-- 1 ubuntu ubuntu 14443 May 20 19:50 experiments.tex
-rw-r--r-- 1 ubuntu ubuntu 11741 May 20 15:36 experiments_reframe.tex
-rw-r--r-- 1 ubuntu ubuntu  5611 May 20 15:36 intro_reframe.tex
-rw-r--r-- 1 ubuntu ubuntu  6459 May 20 15:38 introduction.tex
-rw-r--r-- 1 ubuntu ubuntu  8263 May 20 19:53 method.tex
-rw-r--r-- 1 ubuntu ubuntu  7377 May 20 15:36 method_reframe.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bf8a5048-4db7-4dca-bc2f-fc513f1b9e2d",
  "isSidechain": true,
  "promptId": "df7610aa-ce16-48cc-8465-cca12edac9f8",
  "agentId": "a0170d1e5ef70ae63",
  "type": "user",
  "uuid": "a1d0a436-8408-4d89-b90d-c816070390c5",
  "sourceToolAssistantUUID": "bf8a5048-4db7-4dca-bc2f-fc513f1b9e2d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/paper_agent_73c709c0",
  "sessionId": "71c5797e-c964-4419-a009-2e487a4de1fc",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "ancient-greeting-comet"
}
```

</details>

---

### Assistant

_source line 72 · 2026-05-20T19:54:58.898Z_

Now I understand the structure. Let me check for all instances of "framework" vs "lens" in the main files that are actually included:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a1d0a436-8408-4d89-b90d-c816070390c5",
  "isSidechain": true,
  "agentId": "a0170d1e5ef70ae63",
  "requestId": "req_011CbEQca5XSRVaAfKLGFYWB",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "6afef58c-d0f0-424d-a8f2-e85761089a90",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/paper_agent_73c709c0",
  "sessionId": "71c5797e-c964-4419-a009-2e487a4de1fc",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "ancient-greeting-comet",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01REhZGoqAbFUrjbtJpPppsL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 505,
      "cache_read_input_tokens": 83267,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 505,
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

_source line 73 · 2026-05-20T19:54:59.585Z_

<details open><summary>🔧 Tool call — Bash · `toolu_0123n3yzVpMMFM69GDLbUHyR`</summary>

```json
{
  "command": "grep -n \"\\\\$S.*R\\\\$.*framework\\|S.*R.*framework\\|framework.*S.*R\" /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/{abstract,introduction,method,experiments,discussion,conclusion}.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6afef58c-d0f0-424d-a8f2-e85761089a90",
  "isSidechain": true,
  "agentId": "a0170d1e5ef70ae63",
  "requestId": "req_011CbEQca5XSRVaAfKLGFYWB",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "98d18045-6cec-4e5c-91cb-363afd28c6f0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/paper_agent_73c709c0",
  "sessionId": "71c5797e-c964-4419-a009-2e487a4de1fc",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "ancient-greeting-comet",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01REhZGoqAbFUrjbtJpPppsL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 505,
      "cache_read_input_tokens": 83267,
      "output_tokens": 156,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 505
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4,
          "output_tokens": 156,
          "cache_read_input_tokens": 83267,
          "cache_creation_input_tokens": 505,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 505,
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

_source line 74 · 2026-05-20T19:54:59.680Z_

<details><summary>↩ Tool result · `toolu_0123n3yzVpMMFM69GDLbUHyR`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method.tex:39:Under a permutation test framework, detection power scales as $\mathrm{Power}(\alpha, T) = \Phi\bigl(S \cdot R \cdot \sqrt{T} / \sigma_{\mathrm{noise}}\bigr)$, where $\Phi$ is the standard normal CDF and the $\sqrt{T}$ scaling follows standard power analysis as a conservative lower bound.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "98d18045-6cec-4e5c-91cb-363afd28c6f0",
  "isSidechain": true,
  "promptId": "df7610aa-ce16-48cc-8465-cca12edac9f8",
  "agentId": "a0170d1e5ef70ae63",
  "type": "user",
  "uuid": "a39c836d-5779-45d2-bfdf-ff74f60d348b",
  "sourceToolAssistantUUID": "98d18045-6cec-4e5c-91cb-363afd28c6f0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/paper_agent_73c709c0",
  "sessionId": "71c5797e-c964-4419-a009-2e487a4de1fc",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "ancient-greeting-comet"
}
```

</details>

---

### Assistant

_source line 75 · 2026-05-20T19:55:01.247Z_

That's correct - that usage is fine (it says "permutation test framework" not "S×R framework"). Now let me check specifically for S×R and framework together:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a39c836d-5779-45d2-bfdf-ff74f60d348b",
  "isSidechain": true,
  "agentId": "a0170d1e5ef70ae63",
  "requestId": "req_011CbEQcj2XyY3tNpnmxDeDH",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "beb24547-d834-481b-8cee-5dce4b12c773",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/paper_agent_73c709c0",
  "sessionId": "71c5797e-c964-4419-a009-2e487a4de1fc",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "ancient-greeting-comet",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01KcDhpJPeMHbuSkv5zYXCHL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 301,
      "cache_read_input_tokens": 83772,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 301,
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

_source line 76 · 2026-05-20T19:55:01.526Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01J7pxRikrFmdkgpVK82dV28`</summary>

```json
{
  "command": "grep -i \"s.*r\" /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/{abstract,introduction,method,experiments,discussion,conclusion}.tex | grep -i \"framework\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "beb24547-d834-481b-8cee-5dce4b12c773",
  "isSidechain": true,
  "agentId": "a0170d1e5ef70ae63",
  "requestId": "req_011CbEQcj2XyY3tNpnmxDeDH",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "79fa6416-cf00-47ac-aff5-46f5f6fefd24",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/paper_agent_73c709c0",
  "sessionId": "71c5797e-c964-4419-a009-2e487a4de1fc",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "ancient-greeting-comet",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01KcDhpJPeMHbuSkv5zYXCHL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 301,
      "cache_read_input_tokens": 83772,
      "output_tokens": 151,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 301
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 151,
          "cache_read_input_tokens": 83772,
          "cache_creation_input_tokens": 301,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 301,
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

_source line 77 · 2026-05-20T19:55:01.582Z_

<details><summary>↩ Tool result · `toolu_01J7pxRikrFmdkgpVK82dV28`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/introduction.tex:A multi-method consensus framework (MMCT) comparing five statistical methods reveals that method choice alone can shift conclusions on the same data from universal significance to complete null.
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/introduction.tex:Granger precedence in our framework establishes temporal predictive improvement, not true causality~\cite{shojaie2022granger}; our canary claim is scoped to diversity metrics (distinct-$n$~\cite{li2016diversity}), not model collapse broadly.
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method.tex:Under a permutation test framework, detection power scales as $\mathrm{Power}(\alpha, T) = \Phi\bigl(S \cdot R \cdot \sqrt{T} / \sigma_{\mathrm{noise}}\bigr)$, where $\Phi$ is the standard normal CDF and the $\sqrt{T}$ scaling follows standard power analysis as a conservative lower bound.
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex:$T{=}20$ experiments validate the predict-then-verify framework: all four completed predictions fall within bootstrap confidence intervals, including both tight-CI falsifiable tests ($\alpha{=}0.75$ and $\alpha{=}1.0$, CI${=}$[6,8], observed 6/8 each).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "79fa6416-cf00-47ac-aff5-46f5f6fefd24",
  "isSidechain": true,
  "promptId": "df7610aa-ce16-48cc-8465-cca12edac9f8",
  "agentId": "a0170d1e5ef70ae63",
  "type": "user",
  "uuid": "d1b1b70b-befc-44af-8c8c-86614f1b8778",
  "sourceToolAssistantUUID": "79fa6416-cf00-47ac-aff5-46f5f6fefd24",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/paper_agent_73c709c0",
  "sessionId": "71c5797e-c964-4419-a009-2e487a4de1fc",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "ancient-greeting-comet"
}
```

</details>

---

### Assistant

_source line 78 · 2026-05-20T19:55:22.453Z_

Good - none of those are the problematic "S×R framework" reference. Now let me compile the full report:

## CONSISTENCY AUDIT REPORT

I have completed a thorough consistency audit of the LaTeX paper. Below are the **inconsistencies found**, reported with file:line and problematic text:

### **ISSUE 1: "S×R Framework" vs "S×R Lens" Inconsistency**

**Files with WRONG terminology ("framework"):**
- **experiments_reframe.tex:27**: `\subsection{Dose-Response and the $S \times R$ Framework}`
- **experiments_reframe.tex:31**: `The non-monotonic dip at $\alpha{=}0.60$ is consistent with the $S \times R$ framework (\S\ref{sec:theory})`
- **experiments_reframe.tex:39**: `The $S \times R$ framework generates three testable predictions for $T{=}20$`

**Files with CORRECT terminology ("lens"):**
- **abstract.tex:3**: `A signal-times-resolution ($S \times R$) interpretive lens explains...`
- **introduction.tex:24**: `A signal-times-resolution ($S \times R$) interpretive lens explains this onset...`
- **introduction.tex:36**: `\item \textbf{Signal-times-resolution interpretive lens} (\S\ref{sec:theory}).`
- **method.tex:28-29**: `\subsection{Signal-Times-Resolution Interpretive Lens}` and `We apply standard statistical power scaling to PermG, interpreted through a Signal$\times$Resolution (S$\times$R) decomposition.`

**Status**: The main paper files (experiments.tex, method.tex) correctly use "lens"; the reframe files use "framework" which is inconsistent. The authoritative source should be "lens" per the abstract and introduction.

---

### **ISSUE 2: Cross-Architecture Count Phrasing Inconsistency**

The paper correctly reports "13 of 15" or "13/15" (87%) in most places, but the phrasing varies slightly:

- **experiments.tex:97**: `PermG forward significance reaches ${\geq}$6/8 in 13 of 15 conditions (87\%).`
- **conclusion.tex:11**: `cross-architecture validation confirming detection (${\geq}6/8$) in 13 of 15 model-seed combinations`
- **method.tex:66**: `Cross-architecture validation confirms PermG ${\geq}6/8$ in 13/15 conditions`

All versions are correct (all use "13 of 15" or "13/15" with 87%). **No inconsistency here** — confirmed consistent.

---

### **ISSUE 3: 15/15 Cascade Ordering Reference - CORRECT**

- **method.tex:62**: `The predicted cascade $\{H, \mathrm{ECE}\} \to \mathrm{Distinct}$-$n$ is confirmed in 15/15 experiments at $\alpha \geq 0.30$...`

This is referenced properly. **No inconsistency.**

---

### **ISSUE 4: Pythia-1.4B at α=0.50 - CORRECT (but with caveat)**

- **experiments.tex:101-102**: `At $\alpha{=}0.50$, Pythia-1.4B achieves PermG 3/8 (all three ECE-canary pairs; $K{\geq}3$ threshold met)...`

The paper correctly states **3/8 (ECE-only)**, not 0/8. This is accurate and consistent with requirements. **No inconsistency.**

---

### **ISSUE 5: T=20 Data Consistency - PARTIALLY VERIFIED**

- **method.tex:42**: `$T{=}20$ validates this prediction across four contamination levels: PermG yields 6/8 at $\alpha \in \{0.50, 0.75, 1.0\}$ and 0/8 at $\alpha{=}0.60$, all identical to $T{=}10$; six diversity-based pairs are consistently significant ($F{=}449$--$2947$) while two mauve-based pairs show $F{<}2$ regardless of sequence length`

✓ α=0.50: 6/8 ✓ correct
✓ α=0.60: 0/8 ✓ correct  
✓ α=0.75: 6/8 ✓ correct
✓ α=1.0: 6/8 ✓ correct
✓ F=449–2947 for diversity ✓ correct
✓ F<2 for mauve ✓ correct

**No inconsistency.**

---

### **ISSUE 6: Cascade Theory References - CORRECT**

- **experiments.tex:43**: `...entropy onset at generation~1 precedes distinct-$n$ onset at generation~2 in 16/18 WikiText conditions (Kendall $\tau{=}0.337$; \S\ref{sec:cascade}, Appendix~\ref{app:moment_cascade}).`

The reference to `\S\ref{sec:cascade}` correctly points to **method.tex:45-46** where `\subsection{Cascade Ordering Theory}` and `\label{sec:cascade}` are defined. **No inconsistency.**

---

### **ISSUE 7: "Sharp Onset" vs "Phase Transition" - CORRECT**

The paper appropriately:
- **Uses "sharp onset" for our own findings** (abstract, introduction, conclusion, experiments)
- **Uses "phase transition" only when discussing others' theoretical work** (related_work.tex:10-11 references prior work by Gu et al. on "phase transitions in knowledge acquisition")

**No inconsistency — correct usage.**

---

### **ISSUE 8: Prop 4 / ECE as "Qualitative Argument" - CORRECT**

- **method.tex:61**: `ECE co-moves with entropy at zero lag: under mode amplification, peakier conditionals simultaneously decrease per-token entropy and increase confidence; with accuracy approximately stationary in early collapse, $\Delta\mathrm{ECE} \approx \Delta C > 0$ whenever $\Delta\bar{H} < 0$ (qualitative argument; Appendix~\ref{app:cascade_theory}).`

✓ Correctly labeled as "qualitative argument" NOT "proved" or "theorem"

**No inconsistency.**

---

### **ISSUE 9: TY Footnotes - Directional Assignment Under Verification**

All TY (Toda-Yamamoto) data correctly carry the "directional assignment under verification" marker:
- **experiments.tex:87**: Footnote in Table 1
- **method.tex:22**: Inline note
- **appendix.tex:89, 504**: Footnotes
- **conclusion.tex:9**: Text reference

✓ **Consistent across all mentions.**

---

## SUMMARY OF INCONSISTENCIES FOUND

**ONLY ONE SUBSTANTIVE INCONSISTENCY DETECTED:**

1. **experiments_reframe.tex (lines 27, 31, 39)** uses `$S \times R$ framework` instead of `$S \times R$ lens`
   - This file is a reframe version (not the primary file in use)
   - Main files (experiments.tex, method.tex, abstract.tex, introduction.tex) all correctly use "lens"
   - **Recommendation**: Update experiments_reframe.tex:27, 31, 39 to say "lens" instead of "framework" for consistency

All other 9 items checked are **consistent and correct** across the paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d1b1b70b-befc-44af-8c8c-86614f1b8778",
  "isSidechain": true,
  "agentId": "a0170d1e5ef70ae63",
  "requestId": "req_011CbEQcsE9nYAPH4Db8FbxY",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "6d73adad-982b-41fa-a732-2bf538246e89",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/paper_agent_73c709c0",
  "sessionId": "71c5797e-c964-4419-a009-2e487a4de1fc",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "ancient-greeting-comet",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01T1sb6zpv6tnB7sf1FaZ7dH",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 583,
      "cache_read_input_tokens": 84073,
      "output_tokens": 1874,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 583
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1874,
          "cache_read_input_tokens": 84073,
          "cache_creation_input_tokens": 583,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 583,
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
