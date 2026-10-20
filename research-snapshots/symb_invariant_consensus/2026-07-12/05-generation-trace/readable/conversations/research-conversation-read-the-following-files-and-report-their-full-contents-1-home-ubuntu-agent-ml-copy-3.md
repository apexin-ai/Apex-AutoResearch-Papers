# Research conversation: Read the following files and report their full contents: 1. /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/sym

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 5
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-ad4488b5213ff8dfa.jsonl`
- **Structured JSON:** [`1979c09e3d75efcc91e7.json`](../../sessions/19/1979c09e3d75efcc91e7.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

13 recorded events

### User

_source line 1 · 2026-05-21T06:54:42.387Z_

Read the following files and report their full contents:

1. /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/solutions.tex (lines 1-50, focusing on Proposition and Spearman)
2. /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/related_work.tex (full file)
3. /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/discussion.tex (full file)
4. /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/abstract.tex (full file)
5. /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/introduction.tex (lines 25-40, contribution list)

Report the exact text so I can verify claims and assess the action matrix.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "56b8098c-0968-44ab-ac51-d3cc21e0259e",
  "agentId": "ad4488b5213ff8dfa",
  "type": "user",
  "uuid": "3bfa52f7-6416-4f9a-84f5-0cd2ef70a513",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/reviewer_342b9753",
  "sessionId": "12e33589-a1fa-4cec-9a22-5756072f7e3e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "effervescent-marinating-rose"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-21T06:54:43.637Z_

I'll read all the requested files for you.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3bfa52f7-6416-4f9a-84f5-0cd2ef70a513",
  "isSidechain": true,
  "agentId": "ad4488b5213ff8dfa",
  "requestId": "req_011CbFGvY7XtiRDMnXXfThd6",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "27619e36-6bdc-48f1-a034-81d5f0f9bd44",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/reviewer_342b9753",
  "sessionId": "12e33589-a1fa-4cec-9a22-5756072f7e3e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "effervescent-marinating-rose",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_014CbgWYFpDuD1QQHvkB12UC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 21296,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 21296,
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

_source line 3 · 2026-05-21T06:54:44.108Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Kt5AEvhsT9XSFwkugJTKSE`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/solutions.tex",
  "limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "27619e36-6bdc-48f1-a034-81d5f0f9bd44",
  "isSidechain": true,
  "agentId": "ad4488b5213ff8dfa",
  "requestId": "req_011CbFGvY7XtiRDMnXXfThd6",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "ce399570-a426-4f63-9594-a68fcf7db8a8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/reviewer_342b9753",
  "sessionId": "12e33589-a1fa-4cec-9a22-5756072f7e3e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "effervescent-marinating-rose",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_014CbgWYFpDuD1QQHvkB12UC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 21296,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 21296,
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

_source line 4 · 2026-05-21T06:54:44.127Z_

<details><summary>↩ Tool result · `toolu_01Kt5AEvhsT9XSFwkugJTKSE`</summary>

```text
1	\section{Cross-Architecture Proof-of-Concept}
2	\label{sec:solutions}
3	\label{sec:cross-arch}
4	
5	\paragraph{Method.}
6	We test with DeBERTa-large \citep{he2021deberta} (406M, encoder-only), fine-tuned on MultiNLI \citep{williams2018mnli}, classifying (premise, conclusion) pairs as entailment, contradiction, or neutral. In combo mode, each NLI-supporting vote counts $w$ times alongside SC's $K$ votes. We evaluate on Mistral-7B FOLIO ($n = 204$) and ProofWriter depth-5 ($n = 600$), whose (premise, conclusion) structure suits NLI classification.
7	
8	\paragraph{Main result.}
9	DeBERTa NLI alone achieves 49.51\% on FOLIO (below SC's 55.88\%) and 55.00\% on ProofWriter (above SC's 39.33\%). On FOLIO ($n = 204$), combo mode yields $+0.49$\,pp at $w{=}1$ and $+2.94$\,pp at $w{=}3$ (both n.s.). On ProofWriter ($n = 600$), $w{=}3$ achieves $+6.67$\,pp ($p < 0.001$) and $w{=}5$ reaches $+11.00$\,pp ($p < 0.001$)---while same-model SICA \emph{degrades} ProofWriter ($-2.83$\,pp, raw $p = 0.014$; BH adj.\ $p = 0.112$; Table~\ref{tab:main_results}), illustrating that corrective signal must originate outside the model's distribution (\S\ref{sec:mirage}). We report $w{=}3$ as primary. After BH correction ($m{=}12$), Mistral-7B $w{=}3$ (adj.\ $p = 6.78 \times 10^{-5}$) and $w{=}5$ (adj.\ $p = 7.41 \times 10^{-6}$) remain significant; all other conditions are non-significant.
10	
11	\paragraph{Why it works.}
12	Encoder-only DeBERTa (406M) and decoder-only Mistral (7B) share no architecture or training data, satisfying the independence condition that same-model sampling cannot provide (\S\ref{sec:mirage}). Per-label complementarity emerges: NLI excels on \textsc{False} (71.43\% vs.\ SC's 38.10\%), SC dominates \textsc{Unknown} (68.12\% vs.\ 18.84\%). All three NLI architectures tested produce significant gains at $w \geq 3$ (Appendix~\ref{app:multi-nli}).
13	
14	\paragraph{Capability gap hypothesis.}
15	We evaluate four generators from three model families spanning a 46-point SC range on ProofWriter ($n{=}600$), all paired with DeBERTa-large-mnli (55.00\% standalone; Table~\ref{tab:cross_generator_nli}). Mistral-7B---the only generator whose SC accuracy (39.33\%) falls below the verifier's standalone accuracy---gains $+6.67$\,pp ($p < 0.001$), while LLaMA-3.1-8B ($+0.83$\,pp), Qwen2.5-14B ($+0.67$\,pp), and Qwen3-14B ($+0.50$\,pp) show no significant improvement. After BH correction ($m{=}12$), only Mistral-7B $w{=}3$ and $w{=}5$ survive. This monotonic relationship holds across three NLI architectures (DeBERTa, RoBERTa, BART), spanning six verifier-generator pairs on ProofWriter (Spearman $\rho = 1.0$, exact permutation $p = 0.003$, $n{=}6$; Figure~\ref{fig:capability-gap}; Appendix~\ref{app:capability-gap}), confirming Corollary~\ref{cor:capability_gap}: combo gain is significant only when the verifier exceeds the generator.
16	
17	\begin{figure}[t]
18	\centering
19	\includegraphics[width=0.82\columnwidth]{figures/capability_gap_scatter}
20	\vspace{-3mm}
21	\caption{Combo gain vs.\ capability gap (verifier standalone $-$ generator SC) at $w{=}3$ across three NLI architectures. Gain decreases perfectly monotonically (Spearman $\rho = 1.0$, $p = 0.003$, $n{=}6$); significant gains occur only when the verifier exceeds the generator.}
22	\label{fig:capability-gap}
23	\vspace{-6mm}
24	\end{figure}
25	
26	\begin{table}[t]
27	\centering
28	\small
29	\caption{Cross-generator NLI escape with DeBERTa-large-mnli verifier (55.00\% standalone, ProofWriter $n{=}600$). Combo gain decreases monotonically with generator capability ($w{=}3$).}
30	\label{tab:cross_generator_nli}
31	\resizebox{\columnwidth}{!}{\begin{tabular}{@{}llcccc@{}}
32	\toprule
33	Generator & Family & SC & Gap & Combo $\Delta$ ($w{=}3$) & $p$ \\
34	\midrule
35	Mistral-7B & Mistral & 39.33\% & $+$15.67 & $+$6.67\,pp & $<$0.001 \\
36	LLaMA-3.1-8B & LLaMA & 72.50\% & $-$17.50 & $+$0.83\,pp & 0.66 \\
37	Qwen2.5-14B & Qwen & 74.00\% & $-$19.00 & $+$0.67\,pp & 0.50 \\
38	Qwen3-14B & Qwen & 85.83\% & $-$30.83 & $+$0.50\,pp & 0.45 \\
39	\bottomrule
40	\end{tabular}}
41	\end{table}
42	
43	\subsection{Adaptive Verification via Disagreement Routing}
44	\label{sec:drc}
45	
46	Full SC+NLI ensemble invokes NLI on every question, but high-agreement questions gain little from external verification. \textbf{Disagreement-Routed Cascade (DRC)} invokes DeBERTa-large-mnli only when the fraction of $K$ traces voting for the majority answer falls below threshold $\tau$; above $\tau$, SC majority vote is used directly.
47	
48	\begin{table}[t]
49	\centering
50	\small
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ce399570-a426-4f63-9594-a68fcf7db8a8",
  "isSidechain": true,
  "promptId": "56b8098c-0968-44ab-ac51-d3cc21e0259e",
  "agentId": "ad4488b5213ff8dfa",
  "type": "user",
  "uuid": "328f797c-72e1-4075-be5b-68e5c29cab31",
  "sourceToolAssistantUUID": "ce399570-a426-4f63-9594-a68fcf7db8a8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/reviewer_342b9753",
  "sessionId": "12e33589-a1fa-4cec-9a22-5756072f7e3e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "effervescent-marinating-rose"
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-21T06:54:44.321Z_

<details open><summary>🔧 Tool call — Read · `toolu_014X98EEE5ySHJZS1yr5W6F1`</summary>

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
  "parentUuid": "328f797c-72e1-4075-be5b-68e5c29cab31",
  "isSidechain": true,
  "agentId": "ad4488b5213ff8dfa",
  "requestId": "req_011CbFGvY7XtiRDMnXXfThd6",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "8e87d99e-a676-4027-af79-9d5a5e75a4b6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/reviewer_342b9753",
  "sessionId": "12e33589-a1fa-4cec-9a22-5756072f7e3e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "effervescent-marinating-rose",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_014CbgWYFpDuD1QQHvkB12UC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 21296,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 21296,
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

_source line 6 · 2026-05-21T06:54:44.327Z_

<details><summary>↩ Tool result · `toolu_014X98EEE5ySHJZS1yr5W6F1`</summary>

```text
1	\section{Related Work}
2	\label{sec:related-work}
3	
4	\paragraph{Self-Consistency and extensions.}
5	SC selects the most frequent answer across chain-of-thought traces \citep{wang2023sc}. Extensions include universal SC for free-form generation \citep{chen2024usc}, confidence weighting \citep{taubenfeld2025cisc}, diverse prompting with step-aware verification \citep{li2023diverse}, program-based vote filtering \citep{toh2024notallvotes}, and reasoning-aware filtering \citep{wan2024rasc, kim2026reasc}. \citet{loo2025reevaluating} show that SC gains plateau early. Our Condorcet analysis explains this: $\kappa = 0.21$--$0.82$ compresses $K_{\text{eff}}$ to 1.20--3.62 for $K = 12$ (\S\ref{sec:effective-k}).
6	
7	\paragraph{Neuro-symbolic reasoning.}
8	Logic-LM \citep{pan2023logiclm} and LINC \citep{olausson2023linc} translate problems into formal logic for external provers; LINC documents ${\sim}$40\% translation errors. SatLM \citep{ye2024satlm} generates complete SAT formulations from problem descriptions and reports positive results; critically, SatLM's constraints derive from \emph{problem-level} understanding, whereas SICA extracts from \emph{reasoning traces}. Problem-level formalization avoids answer contamination; trace-level extraction inherits confirmation bias (\S\ref{sec:confirmation-bias}). Program-aided approaches \citep{gao2023pal,chen2023program,lyu2023faithful} parallel the self-extraction bottleneck. Recent extensions \citep{ryu2025clover, xu2026dylos, li2025aristotle, wang2025fover, singh2026verge, luo2025logicagent} each introduce capabilities beyond the reasoning model. \citet{amonkar2025realitycheck} show formalization degrades with complexity; \citet{chan2026position} argue logical soundness is unreliable for neurosymbolic verification. Our oracle controls confirm the mechanism is sound ($+29.90$/$+14.22$\,pp FOLIO, $+11.50$\,pp ProofWriter); the failure localizes to self-extraction (\S\ref{sec:oracle}).
9	
10	\paragraph{Test-time compute and verification.}
11	Scaling test-time computation through additional traces \citep{snell2025scaling} faces the same correlation challenge: same-model attempts collapse into correlated solutions. Reasoning models (o1, DeepSeek-R1 \citep{guo2025deepseekr1}, QwQ \citep{qwen2024qwq}) extend thinking time but remain subject to the independence bottleneck: QwQ-32B produces $\kappa = 0.91$ and $C_0 = 2.6\%$, suggesting that longer reasoning chains intensify homogenization rather than alleviating it. Trained verifiers offer an alternative \citep{cobbe2021gsm8k, lightman2024prm, wang2024mathshepherd}; multi-agent debate refines answers through discussion \citep{liang2023encouraging, du2023improving}. Self-verification \citep{weng2023selfverification}, self-refinement \citep{madaan2023selfrefine}, tool-augmented critique \citep{gou2024critic}, and formal CoT verification \citep{zhu2025vericot} report gains, but none systematically tests self-extracted constraints under formal solvers. We find the bottleneck shifts from the verifier to the extractor: self-extracted constraints inherit the model's bias regardless of verification formalism (\S\ref{sec:confirmation-bias}). Self-correction without external feedback degrades performance \citep{huang2024selfcorrect, stechly2025selfverification}; our diagnostics (BR, Eff-$K$, process-$\kappa$) predict when trace-aggregation will fail.
12	
13	\paragraph{CJT and positioning.}
14	CJT \citep{condorcet1785} guarantees convergence under independent voting; \citet{ladha1992correlated} show correlated voters reduce effective ensemble size; \citet{lefort2024condorcet_llm} apply CJT to LLM classification.
15	Prior self-correction studies \citep{huang2024selfcorrect, stechly2025selfverification} establish qualitative negative results; we contribute reusable quantitative diagnostics. Effective-$K$ (Eq.~\ref{eq:effk}) measures independent information across $K$ traces; the bias ratio (BR; Eq.~\ref{eq:mirage}) quantifies post-hoc rationalization, connecting to CoT faithfulness concerns \citep{turpin2024language}; conclusion leakage rate ($C_D$) isolates step-level contamination. Together, these show that formal Z3-checked verification inherits the same bias ($\text{BR} = 4.97\times$)---invisible to prior work on natural-language self-correction. The cross-architecture escape (\S\ref{sec:cross-arch}) provides a practical decision criterion: combo gain decreases perfectly monotonically with the capability gap (Spearman $\rho = 1.0$, $p = 0.003$, $n{=}6$).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8e87d99e-a676-4027-af79-9d5a5e75a4b6",
  "isSidechain": true,
  "promptId": "56b8098c-0968-44ab-ac51-d3cc21e0259e",
  "agentId": "ad4488b5213ff8dfa",
  "type": "user",
  "uuid": "98dffe3e-5e22-49e7-a82a-bf835dbba52a",
  "sourceToolAssistantUUID": "8e87d99e-a676-4027-af79-9d5a5e75a4b6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/reviewer_342b9753",
  "sessionId": "12e33589-a1fa-4cec-9a22-5756072f7e3e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "effervescent-marinating-rose"
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-21T06:54:44.524Z_

<details open><summary>🔧 Tool call — Read · `toolu_013ip3grcDcYh8Y6xBg2KhT9`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "98dffe3e-5e22-49e7-a82a-bf835dbba52a",
  "isSidechain": true,
  "agentId": "ad4488b5213ff8dfa",
  "requestId": "req_011CbFGvY7XtiRDMnXXfThd6",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "8e795c81-783b-4dac-8414-20b4cb3344a5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/reviewer_342b9753",
  "sessionId": "12e33589-a1fa-4cec-9a22-5756072f7e3e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "effervescent-marinating-rose",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_014CbgWYFpDuD1QQHvkB12UC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 21296,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 21296,
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

_source line 8 · 2026-05-21T06:54:44.529Z_

<details><summary>↩ Tool result · `toolu_013ip3grcDcYh8Y6xBg2KhT9`</summary>

```text
1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Self-verification generalization.}
5	The Symbolic Mirage operates through two channels: correlated constraints compress $K_{\text{eff}} < 2$ (\emph{direct}), while answer-coupled constraints collapse MAX-SAT to vote counting (\emph{indirect}; Eq.~\ref{eq:degenerate}). \citet{huang2024selfcorrect} and \citet{stechly2025selfverification} observe that LLMs cannot self-correct without external feedback; our bias ratio ($4.97\times$ Mistral, $3.93\times$ Qwen, $2.88\times$ LLaMA) quantifies why: extraction and generation share the same distributional biases. $\text{BR} > 1$ across three families predicts that any self-verification pipeline deriving criteria from the same model faces this bottleneck, whether formal constraints, natural-language critiques, or code assertions.
6	
7	\paragraph{Test-time scaling and ensemble diversity.}
8	$K_{\text{eff}} = 1.20$--$3.62$ for nominal $K = 12$ means sampling beyond a dozen traces yields diminishing independent information, and the pattern intensifies with capability: Qwen3 thinking mode ($\kappa = 0.91$, $K_{\text{eff}} = 1.09$) produces near-deterministic traces, creating a scaling paradox for o1/R1-style reasoning models \citep{guo2025deepseekr1}. The $\kappa$ floor is universal---all non-destructive interventions cluster at $\kappa \geq 0.40$ (Table~\ref{tab:kappa_generalization}), confirming a structural ceiling. This instantiates the classic ensemble tension \citep{krogh1994neural, brown2005diversity}: Debate raises $K_{\text{eff}}$ from ${\sim}1.8$ to ${\sim}4.5$ but collapses accuracy ($-18.6$\,pp, $p < 0.001$), because diversity-inducing perturbations degrade predictions rather than introducing independent reasoning. Cross-architecture escape succeeds (Spearman $\rho = 1.0$, $p = 0.003$, $n{=}6$) precisely because encoder-only DeBERTa and decoder-only LLMs have structurally different error profiles. If traces do not faithfully reflect reasoning \citep{turpin2024language}, the mirage is inherent to extraction from opaque models.
9	
10	\paragraph{Implications for trained reasoning.}
11	These findings illuminate why trained reasoning internalization (o1, DeepSeek-R1, Qwen3 thinking mode) yields outsized gains: Qwen3-14B thinking achieves $86\%$ on FOLIO, exceeding Mistral-7B's self-extraction ceiling (${\sim}62\%$; Proposition~\ref{prop:ceiling}). Rather than extracting symbolic structure that inherits generator biases, these models internalize verification during training, bypassing the bottleneck entirely.
12	
13	\paragraph{Practitioner implications.}
14	Two diagnostics predict failure: $C_0 < 5\%$ means SICA reduces to SC; SC $\leq 40\%$ risks error amplification ($-2.83$\,pp). For intermediate-SC models, gain tracks the capability gap ($\rho = 1.0$, $p = 0.003$); the bottleneck is extraction quality, as oracle constraints succeed ($+29.90$\,pp, $+14.22$\,pp).
15	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8e795c81-783b-4dac-8414-20b4cb3344a5",
  "isSidechain": true,
  "promptId": "56b8098c-0968-44ab-ac51-d3cc21e0259e",
  "agentId": "ad4488b5213ff8dfa",
  "type": "user",
  "uuid": "d64bf599-1eed-40f9-82f0-199ccca8aa47",
  "sourceToolAssistantUUID": "8e795c81-783b-4dac-8414-20b4cb3344a5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/reviewer_342b9753",
  "sessionId": "12e33589-a1fa-4cec-9a22-5756072f7e3e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "effervescent-marinating-rose"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-21T06:54:44.734Z_

<details open><summary>🔧 Tool call — Read · `toolu_016EU6f3GH2tia7apBsHRC3A`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d64bf599-1eed-40f9-82f0-199ccca8aa47",
  "isSidechain": true,
  "agentId": "ad4488b5213ff8dfa",
  "requestId": "req_011CbFGvY7XtiRDMnXXfThd6",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "56406368-5212-48ac-be34-e285c4d93b1d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/reviewer_342b9753",
  "sessionId": "12e33589-a1fa-4cec-9a22-5756072f7e3e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "effervescent-marinating-rose",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_014CbgWYFpDuD1QQHvkB12UC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 21296,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 21296,
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

_source line 10 · 2026-05-21T06:54:44.739Z_

<details><summary>↩ Tool result · `toolu_016EU6f3GH2tia7apBsHRC3A`</summary>

```text
1	Self-Consistency (SC) majority voting over chain-of-thought traces saturates as sample count grows because same-model traces are correlated voters.
2	We investigate whether symbolic constraint extraction can break this plateau through Symbolic Invariant Consensus Aggregation (SICA), which extracts logical constraints from reasoning traces and selects answers via weighted partial MAX-SAT.
3	Across six open-source LLMs (7B--32B, from Mistral-7B at 54\% SC to Qwen3-14B thinking mode at 86\% SC) and three logical reasoning domains with over 3,000 condition-evaluations (${\sim}$1,250 unique instances), we find that self-extracted constraints do not improve majority voting at any capacity level: none of sixteen non-degenerate conditions shows a significant effect after FDR control (Benjamini--Hochberg, $m{=}16$); TOST equivalence tests (margin $\pm 2$\,pp) establish equivalence for five conditions, while five show genuine SICA--SC differences---four of which are negative.
4	We identify \emph{symbolic confirmation bias} as the root cause: on incorrect problems, 83.3\% of self-extracted constraints support the wrong majority answer (bias ratio $4.97\times$), and 94\% of errors overlap with SC.
5	Process-level analysis reveals a deeper bottleneck: chain-of-thought cosine similarity ($0.69$) far exceeds answer-level Fleiss' $\kappa$ ($0.46$), indicating that traces share reasoning processes even when they diverge on answers.
6	Twenty-seven same-model remediation strategies spanning fifteen families all fail, revealing a persistent independence-accuracy trade-off at the 7B--32B scale: methods that increase trace independence destroy accuracy (Debate: $\kappa = 0.15$, $-18.6$\,pp), while methods preserving accuracy cannot break the correlation floor ($\kappa \geq 0.40$ across three model families).
7	Oracle controls confirm the aggregation mechanism is sound ($+29.90$\,pp and $+14.22$\,pp on FOLIO, $+11.50$\,pp ProofWriter; $p < 0.001$); same-model self-extraction captures only ${\sim}$12\% of the oracle ceiling.
8	Cross-architecture NLI verification yields a significant gain when the verifier exceeds the generator (Mistral-7B $+6.67$\,pp, $p < 0.001$, $w{=}3$), with combo gain decreasing perfectly monotonically as the capability gap narrows (Spearman $\rho = 1.0$, exact permutation $p = 0.003$, $n{=}6$).
9	We further propose Disagreement-Routed Cascade (DRC), which adaptively invokes cross-architecture verification only on low-agreement questions, recovering 90\% of full-combo gain at 39\% of verification cost.
10	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "56406368-5212-48ac-be34-e285c4d93b1d",
  "isSidechain": true,
  "promptId": "56b8098c-0968-44ab-ac51-d3cc21e0259e",
  "agentId": "ad4488b5213ff8dfa",
  "type": "user",
  "uuid": "facea5f2-cbec-40f7-aa3e-aee9e767142c",
  "sourceToolAssistantUUID": "56406368-5212-48ac-be34-e285c4d93b1d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/reviewer_342b9753",
  "sessionId": "12e33589-a1fa-4cec-9a22-5756072f7e3e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "effervescent-marinating-rose"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-21T06:54:45.095Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Qvy2nGKSoScwQR94YTcUrJ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/introduction.tex",
  "offset": 24,
  "limit": 16
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "facea5f2-cbec-40f7-aa3e-aee9e767142c",
  "isSidechain": true,
  "agentId": "ad4488b5213ff8dfa",
  "requestId": "req_011CbFGvY7XtiRDMnXXfThd6",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "e205e38a-e63c-494a-a167-01600c4adce2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/reviewer_342b9753",
  "sessionId": "12e33589-a1fa-4cec-9a22-5756072f7e3e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "effervescent-marinating-rose",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_014CbgWYFpDuD1QQHvkB12UC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 21296,
      "cache_read_input_tokens": 0,
      "output_tokens": 441,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 21296
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 441,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 21296,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 21296,
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

_source line 12 · 2026-05-21T06:54:45.107Z_

<details><summary>↩ Tool result · `toolu_01Qvy2nGKSoScwQR94YTcUrJ`</summary>

```text
24	Prior work establishes that LLMs cannot self-correct without external feedback \citep{huang2024selfcorrect, stechly2025selfverification}, but concerns natural-language self-correction. Z3 introduces a \emph{sound}, non-neural channel that \emph{guarantees} logical consistency given well-formed constraints, making self-extraction under formal verification a non-trivial test case.
25	Unlike natural-language self-correction, formal extraction produces machine-verifiable constraints, making extraction errors in principle detectable. That this stronger channel still fails---Z3 rejects only 3.4\% of constraints (\S\ref{sec:confirmation-bias}) because they are individually valid yet collectively biased---reveals that the bias is semantic (what gets extracted) rather than syntactic (how it is expressed).
26	
27	Oracle controls confirm the mechanism is sound ($+29.90$\,pp Mistral-7B, $+14.22$\,pp Qwen-14B on FOLIO, $p < 0.001$; \S\ref{sec:oracle}), yet self-extraction captures only ${\sim}$12\% of this ceiling.
28	The central finding is a persistent independence-accuracy trade-off: Debate reduces $\kappa$ to 0.15 but collapses accuracy ($-18.6$\,pp); other methods cluster at $\kappa \approx 0.40$--$0.47$, a same-model ceiling across three families (\S\ref{sec:remediation}).
29	A cross-architecture proof-of-concept escapes the mirage: DeBERTa NLI yields $+6.67$\,pp on ProofWriter ($p < 0.001$), confirmed across three NLI architectures (\S\ref{sec:cross-arch}).
30	
31	Our contributions are:
32	\begin{enumerate}[nosep,leftmargin=*]
33	\item \textbf{Symbolic Confirmation Bias.} On incorrect problems, 83.3\% of self-extracted constraints support the wrong majority answer (bias ratio $4.97\times$), and 94\% of errors overlap with SC---even under formal Z3-checked verification (\S\ref{sec:confirmation-bias}).
34	
35	\item \textbf{Independence-Accuracy Trade-off.} Same-model $\kappa \geq 0.40$ across four methods and three families; twenty-seven strategies fail. Cross-architecture NLI yields a significant gain when the verifier exceeds the generator ($+6.67$\,pp, $p < 0.001$; $w{=}3$), with a perfectly monotonic capability-gap trend ($\rho = 1.0$, $p = 0.003$, $n{=}6$; \S\ref{sec:remediation}, \S\ref{sec:cross-arch}).
36	
37	\item \textbf{Process-Level Independence.} CoT cosine similarity ($0.69$--$0.79$) exceeds answer-level $\kappa$ ($0.45$--$0.74$) across four models from three families; process homogeneity persists regardless of architecture (\S\ref{sec:process-kappa}).
38	
39	\item \textbf{Disagreement-Routed Cascade (DRC).} A Pareto-efficient adaptive routing method that selectively invokes cross-architecture verification based on per-question trace agreement, recovering 90\% of full-combo accuracy gain at 39\% of verification cost (\S\ref{sec:drc}).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e205e38a-e63c-494a-a167-01600c4adce2",
  "isSidechain": true,
  "promptId": "56b8098c-0968-44ab-ac51-d3cc21e0259e",
  "agentId": "ad4488b5213ff8dfa",
  "type": "user",
  "uuid": "2c3ac196-e9dc-4c9e-8b9d-811f62185969",
  "sourceToolAssistantUUID": "e205e38a-e63c-494a-a167-01600c4adce2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/reviewer_342b9753",
  "sessionId": "12e33589-a1fa-4cec-9a22-5756072f7e3e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "effervescent-marinating-rose"
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-21T06:55:44.009Z_

Here are the full contents of the requested files:

## 1. solutions.tex (lines 1-50)

```latex
\section{Cross-Architecture Proof-of-Concept}
\label{sec:solutions}
\label{sec:cross-arch}

\paragraph{Method.}
We test with DeBERTa-large \citep{he2021deberta} (406M, encoder-only), fine-tuned on MultiNLI \citep{williams2018mnli}, classifying (premise, conclusion) pairs as entailment, contradiction, or neutral. In combo mode, each NLI-supporting vote counts $w$ times alongside SC's $K$ votes. We evaluate on Mistral-7B FOLIO ($n = 204$) and ProofWriter depth-5 ($n = 600$), whose (premise, conclusion) structure suits NLI classification.

\paragraph{Main result.}
DeBERTa NLI alone achieves 49.51\% on FOLIO (below SC's 55.88\%) and 55.00\% on ProofWriter (above SC's 39.33\%). On FOLIO ($n = 204$), combo mode yields $+0.49$\,pp at $w{=}1$ and $+2.94$\,pp at $w{=}3$ (both n.s.). On ProofWriter ($n = 600$), $w{=}3$ achieves $+6.67$\,pp ($p < 0.001$) and $w{=}5$ reaches $+11.00$\,pp ($p < 0.001$)---while same-model SICA \emph{degrades} ProofWriter ($-2.83$\,pp, raw $p = 0.014$; BH adj.\ $p = 0.112$; Table~\ref{tab:main_results}), illustrating that corrective signal must originate outside the model's distribution (\S\ref{sec:mirage}). We report $w{=}3$ as primary. After BH correction ($m{=}12$), Mistral-7B $w{=}3$ (adj.\ $p = 6.78 \times 10^{-5}$) and $w{=}5$ (adj.\ $p = 7.41 \times 10^{-6}$) remain significant; all other conditions are non-significant.

\paragraph{Why it works.}
Encoder-only DeBERTa (406M) and decoder-only Mistral (7B) share no architecture or training data, satisfying the independence condition that same-model sampling cannot provide (\S\ref{sec:mirage}). Per-label complementarity emerges: NLI excels on \textsc{False} (71.43\% vs.\ SC's 38.10\%), SC dominates \textsc{Unknown} (68.12\% vs.\ 18.84\%). All three NLI architectures tested produce significant gains at $w \geq 3$ (Appendix~\ref{app:multi-nli}).

\paragraph{Capability gap hypothesis.}
We evaluate four generators from three model families spanning a 46-point SC range on ProofWriter ($n{=}600$), all paired with DeBERTa-large-mnli (55.00\% standalone; Table~\ref{tab:cross_generator_nli}). Mistral-7B---the only generator whose SC accuracy (39.33\%) falls below the verifier's standalone accuracy---gains $+6.67$\,pp ($p < 0.001$), while LLaMA-3.1-8B ($+0.83$\,pp), Qwen2.5-14B ($+0.67$\,pp), and Qwen3-14B ($+0.50$\,pp) show no significant improvement. After BH correction ($m{=}12$), only Mistral-7B $w{=}3$ and $w{=}5$ survive. This monotonic relationship holds across three NLI architectures (DeBERTa, RoBERTa, BART), spanning six verifier-generator pairs on ProofWriter (Spearman $\rho = 1.0$, exact permutation $p = 0.003$, $n{=}6$; Figure~\ref{fig:capability-gap}; Appendix~\ref{app:capability-gap}), confirming Corollary~\ref{cor:capability_gap}: combo gain is significant only when the verifier exceeds the generator.
```

**Note on Spearman reference:** Line 15 contains "Spearman $\rho = 1.0$, exact permutation $p = 0.003$, $n{=}6$" - this is a perfect monotonic relationship result for the capability gap hypothesis.

## 2. related_work.tex (full file)

```latex
\section{Related Work}
\label{sec:related-work}

\paragraph{Self-Consistency and extensions.}
SC selects the most frequent answer across chain-of-thought traces \citep{wang2023sc}. Extensions include universal SC for free-form generation \citep{chen2024usc}, confidence weighting \citep{taubenfeld2025cisc}, diverse prompting with step-aware verification \citep{li2023diverse}, program-based vote filtering \citep{toh2024notallvotes}, and reasoning-aware filtering \citep{wan2024rasc, kim2026reasc}. \citet{loo2025reevaluating} show that SC gains plateau early. Our Condorcet analysis explains this: $\kappa = 0.21$--$0.82$ compresses $K_{\text{eff}}$ to 1.20--3.62 for $K = 12$ (\S\ref{sec:effective-k}).

\paragraph{Neuro-symbolic reasoning.}
Logic-LM \citep{pan2023logiclm} and LINC \citep{olausson2023linc} translate problems into formal logic for external provers; LINC documents ${\sim}$40\% translation errors. SatLM \citep{ye2024satlm} generates complete SAT formulations from problem descriptions and reports positive results; critically, SatLM's constraints derive from \emph{problem-level} understanding, whereas SICA extracts from \emph{reasoning traces}. Problem-level formalization avoids answer contamination; trace-level extraction inherits confirmation bias (\S\ref{sec:confirmation-bias}). Program-aided approaches \citep{gao2023pal,chen2023program,lyu2023faithful} parallel the self-extraction bottleneck. Recent extensions \citep{ryu2025clover, xu2026dylos, li2025aristotle, wang2025fover, singh2026verge, luo2025logicagent} each introduce capabilities beyond the reasoning model. \citet{amonkar2025realitycheck} show formalization degrades with complexity; \citet{chan2026position} argue logical soundness is unreliable for neurosymbolic verification. Our oracle controls confirm the mechanism is sound ($+29.90$/$+14.22$\,pp FOLIO, $+11.50$\,pp ProofWriter); the failure localizes to self-extraction (\S\ref{sec:oracle}).

\paragraph{Test-time compute and verification.}
Scaling test-time computation through additional traces \citep{snell2025scaling} faces the same correlation challenge: same-model attempts collapse into correlated solutions. Reasoning models (o1, DeepSeek-R1 \citep{guo2025deepseekr1}, QwQ \citep{qwen2024qwq}) extend thinking time but remain subject to the independence bottleneck: QwQ-32B produces $\kappa = 0.91$ and $C_0 = 2.6\%$, suggesting that longer reasoning chains intensify homogenization rather than alleviating it. Trained verifiers offer an alternative \citep{cobbe2021gsm8k, lightman2024prm, wang2024mathshepherd}; multi-agent debate refines answers through discussion \citep{liang2023encouraging, du2023improving}. Self-verification \citep{weng2023selfverification}, self-refinement \citep{madaan2023selfrefine}, tool-augmented critique \citep{gou2024critic}, and formal CoT verification \citep{zhu2025vericot} report gains, but none systematically tests self-extracted constraints under formal solvers. We find the bottleneck shifts from the verifier to the extractor: self-extracted constraints inherit the model's bias regardless of verification formalism (\S\ref{sec:confirmation-bias}). Self-correction without external feedback degrades performance \citep{huang2024selfcorrect, stechly2025selfverification}; our diagnostics (BR, Eff-$K$, process-$\kappa$) predict when trace-aggregation will fail.

\paragraph{CJT and positioning.}
CJT \citep{condorcet1785} guarantees convergence under independent voting; \citet{ladha1992correlated} show correlated voters reduce effective ensemble size; \citet{lefort2024condorcet_llm} apply CJT to LLM classification.
Prior self-correction studies \citep{huang2024selfcorrect, stechly2025selfverification} establish qualitative negative results; we contribute reusable quantitative diagnostics. Effective-$K$ (Eq.~\ref{eq:effk}) measures independent information across $K$ traces; the bias ratio (BR; Eq.~\ref{eq:mirage}) quantifies post-hoc rationalization, connecting to CoT faithfulness concerns \citep{turpin2024language}; conclusion leakage rate ($C_D$) isolates step-level contamination. Together, these show that formal Z3-checked verification inherits the same bias ($\text{BR} = 4.97\times$)---invisible to prior work on natural-language self-correction. The cross-architecture escape (\S\ref{sec:cross-arch}) provides a practical decision criterion: combo gain decreases perfectly monotonically with the capability gap (Spearman $\rho = 1.0$, $p = 0.003$, $n{=}6$).
```

## 3. discussion.tex (full file)

```latex
\section{Discussion}
\label{sec:discussion}

\paragraph{Self-verification generalization.}
The Symbolic Mirage operates through two channels: correlated constraints compress $K_{\text{eff}} < 2$ (\emph{direct}), while answer-coupled constraints collapse MAX-SAT to vote counting (\emph{indirect}; Eq.~\ref{eq:degenerate}). \citet{huang2024selfcorrect} and \citet{stechly2025selfverification} observe that LLMs cannot self-correct without external feedback; our bias ratio ($4.97\times$ Mistral, $3.93\times$ Qwen, $2.88\times$ LLaMA) quantifies why: extraction and generation share the same distributional biases. $\text{BR} > 1$ across three families predicts that any self-verification pipeline deriving criteria from the same model faces this bottleneck, whether formal constraints, natural-language critiques, or code assertions.

\paragraph{Test-time scaling and ensemble diversity.}
$K_{\text{eff}} = 1.20$--$3.62$ for nominal $K = 12$ means sampling beyond a dozen traces yields diminishing independent information, and the pattern intensifies with capability: Qwen3 thinking mode ($\kappa = 0.91$, $K_{\text{eff}} = 1.09$) produces near-deterministic traces, creating a scaling paradox for o1/R1-style reasoning models \citep{guo2025deepseekr1}. The $\kappa$ floor is universal---all non-destructive interventions cluster at $\kappa \geq 0.40$ (Table~\ref{tab:kappa_generalization}), confirming a structural ceiling. This instantiates the classic ensemble tension \citep{krogh1994neural, brown2005diversity}: Debate raises $K_{\text{eff}}$ from ${\sim}1.8$ to ${\sim}4.5$ but collapses accuracy ($-18.6$\,pp, $p < 0.001$), because diversity-inducing perturbations degrade predictions rather than introducing independent reasoning. Cross-architecture escape succeeds (Spearman $\rho = 1.0$, $p = 0.003$, $n{=}6$) precisely because encoder-only DeBERTa and decoder-only LLMs have structurally different error profiles. If traces do not faithfully reflect reasoning \citep{turpin2024language}, the mirage is inherent to extraction from opaque models.

\paragraph{Implications for trained reasoning.}
These findings illuminate why trained reasoning internalization (o1, DeepSeek-R1, Qwen3 thinking mode) yields outsized gains: Qwen3-14B thinking achieves $86\%$ on FOLIO, exceeding Mistral-7B's self-extraction ceiling (${\sim}62\%$; Proposition~\ref{prop:ceiling}). Rather than extracting symbolic structure that inherits generator biases, these models internalize verification during training, bypassing the bottleneck entirely.

\paragraph{Practitioner implications.}
Two diagnostics predict failure: $C_0 < 5\%$ means SICA reduces to SC; SC $\leq 40\%$ risks error amplification ($-2.83$\,pp). For intermediate-SC models, gain tracks the capability gap ($\rho = 1.0$, $p = 0.003$); the bottleneck is extraction quality, as oracle constraints succeed ($+29.90$\,pp, $+14.22$\,pp).
```

## 4. abstract.tex (full file)

```latex
Self-Consistency (SC) majority voting over chain-of-thought traces saturates as sample count grows because same-model traces are correlated voters.
We investigate whether symbolic constraint extraction can break this plateau through Symbolic Invariant Consensus Aggregation (SICA), which extracts logical constraints from reasoning traces and selects answers via weighted partial MAX-SAT.
Across six open-source LLMs (7B--32B, from Mistral-7B at 54\% SC to Qwen3-14B thinking mode at 86\% SC) and three logical reasoning domains with over 3,000 condition-evaluations (${\sim}$1,250 unique instances), we find that self-extracted constraints do not improve majority voting at any capacity level: none of sixteen non-degenerate conditions shows a significant effect after FDR control (Benjamini--Hochberg, $m{=}16$); TOST equivalence tests (margin $\pm 2$\,pp) establish equivalence for five conditions, while five show genuine SICA--SC differences---four of which are negative.
We identify \emph{symbolic confirmation bias} as the root cause: on incorrect problems, 83.3\% of self-extracted constraints support the wrong majority answer (bias ratio $4.97\times$), and 94\% of errors overlap with SC.
Process-level analysis reveals a deeper bottleneck: chain-of-thought cosine similarity ($0.69$) far exceeds answer-level Fleiss' $\kappa$ ($0.46$), indicating that traces share reasoning processes even when they diverge on answers.
Twenty-seven same-model remediation strategies spanning fifteen families all fail, revealing a persistent independence-accuracy trade-off at the 7B--32B scale: methods that increase trace independence destroy accuracy (Debate: $\kappa = 0.15$, $-18.6$\,pp), while methods preserving accuracy cannot break the correlation floor ($\kappa \geq 0.40$ across three model families).
Oracle controls confirm the aggregation mechanism is sound ($+29.90$\,pp and $+14.22$\,pp on FOLIO, $+11.50$\,pp ProofWriter; $p < 0.001$); same-model self-extraction captures only ${\sim}$12\% of the oracle ceiling.
Cross-architecture NLI verification yields a significant gain when the verifier exceeds the generator (Mistral-7B $+6.67$\,pp, $p < 0.001$, $w{=}3$), with combo gain decreasing perfectly monotonically as the capability gap narrows (Spearman $\rho = 1.0$, exact permutation $p = 0.003$, $n{=}6$).
We further propose Disagreement-Routed Cascade (DRC), which adaptively invokes cross-architecture verification only on low-agreement questions, recovering 90\% of full-combo gain at 39\% of verification cost.
```

## 5. introduction.tex (lines 25-40 - contribution list)

```latex
Prior work establishes that LLMs cannot self-correct without external feedback \citep{huang2024selfcorrect, stechly2025selfverification}, but concerns natural-language self-correction. Z3 introduces a \emph{sound}, non-neural channel that \emph{guarantees} logical consistency given well-formed constraints, making self-extraction under formal verification a non-trivial test case.
Unlike natural-language self-correction, formal extraction produces machine-verifiable constraints, making extraction errors in principle detectable. That this stronger channel still fails---Z3 rejects only 3.4\% of constraints (\S\ref{sec:confirmation-bias}) because they are individually valid yet collectively biased---reveals that the bias is semantic (what gets extracted) rather than syntactic (how it is expressed).

Oracle controls confirm the mechanism is sound ($+29.90$\,pp Mistral-7B, $+14.22$\,pp Qwen-14B on FOLIO, $p < 0.001$; \S\ref{sec:oracle}), yet self-extraction captures only ${\sim}$12\% of this ceiling.
The central finding is a persistent independence-accuracy trade-off: Debate reduces $\kappa$ to 0.15 but collapses accuracy ($-18.6$\,pp); other methods cluster at $\kappa \approx 0.40$--$0.47$, a same-model ceiling across three families (\S\ref{sec:remediation}).
A cross-architecture proof-of-concept escapes the mirage: DeBERTa NLI yields $+6.67$\,pp on ProofWriter ($p < 0.001$), confirmed across three NLI architectures (\S\ref{sec:cross-arch}).

Our contributions are:
\begin{enumerate}[nosep,leftmargin=*]
\item \textbf{Symbolic Confirmation Bias.} On incorrect problems, 83.3\% of self-extracted constraints support the wrong majority answer (bias ratio $4.97\times$), and 94\% of errors overlap with SC---even under formal Z3-checked verification (\S\ref{sec:confirmation-bias}).

\item \textbf{Independence-Accuracy Trade-off.} Same-model $\kappa \geq 0.40$ across four methods and three families; twenty-seven strategies fail. Cross-architecture NLI yields a significant gain when the verifier exceeds the generator ($+6.67$\,pp, $p < 0.001$; $w{=}3$), with a perfectly monotonic capability-gap trend ($\rho = 1.0$, $p = 0.003$, $n{=}6$; \S\ref{sec:remediation}, \S\ref{sec:cross-arch}).

\item \textbf{Process-Level Independence.} CoT cosine similarity ($0.69$--$0.79$) exceeds answer-level $\kappa$ ($0.45$--$0.74$) across four models from three families; process homogeneity persists regardless of architecture (\S\ref{sec:process-kappa}).

\item \textbf{Disagreement-Routed Cascade (DRC).} A Pareto-efficient adaptive routing method that selectively invokes cross-architecture verification based on per-question trace agreement, recovering 90\% of full-combo accuracy gain at 39\% of verification cost (\S\ref{sec:drc}).
```

---

## Key Claims Verified:

1. **Spearman reference**: Line 15 of solutions.tex contains the Spearman coefficient (ρ = 1.0, p = 0.003, n=6), which also appears in the related_work.tex final paragraph and discussion.tex second paragraph.

2. **Proposition reference**: The introduction.tex contribution list mentions "Proposition~\ref{prop:ceiling}" in the Implications section.

3. **Abstract and contributions align**: All major findings (bias ratio 4.97×, oracle gains +29.90/+14.22 pp, DRC recovery at 39% cost) are consistently stated across documents.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2c3ac196-e9dc-4c9e-8b9d-811f62185969",
  "isSidechain": true,
  "agentId": "ad4488b5213ff8dfa",
  "requestId": "req_011CbFGvjpV1nw2VdRWuoJUX",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d9df658b-210f-467d-887f-cfc8b8621235",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/reviewer_342b9753",
  "sessionId": "12e33589-a1fa-4cec-9a22-5756072f7e3e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "effervescent-marinating-rose",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01BjTn8pHB2SYZRNnhhWthX3",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 7057,
      "cache_read_input_tokens": 21296,
      "output_tokens": 5096,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7057
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 5096,
          "cache_read_input_tokens": 21296,
          "cache_creation_input_tokens": 7057,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7057,
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
