# Research conversation: Read these files in full and report their complete contents: 1. /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 1
- **Tool calls:** 4
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a62a755bf7232a081.jsonl`
- **Structured JSON:** [`55d0fd9f91962956dd23.json`](../../sessions/55/55d0fd9f91962956dd23.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

11 recorded events

### User

_source line 1 · 2026-05-15T23:02:00.988Z_

Read these files in full and report their complete contents:
1. /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/abstract.tex
2. /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/introduction.tex
3. /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/related_work.tex
4. /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/limitations.tex

Report the full text of each file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "169bea34-34c4-423a-9946-976e7f30e506",
  "agentId": "a62a755bf7232a081",
  "type": "user",
  "uuid": "802f7ade-bb7c-4de5-bade-5caf05b460a2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "ff2a3926-a23a-4756-aa8c-9df2956fd4eb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-15T23:02:02.028Z_

I'll read all four files for you in full.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "802f7ade-bb7c-4de5-bade-5caf05b460a2",
  "isSidechain": true,
  "agentId": "a62a755bf7232a081",
  "requestId": "req_011Cb5BqKZUBBarcfMVhUZmE",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d8cb0e4a-da75-42b0-8ed1-d5e274313c3f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "ff2a3926-a23a-4756-aa8c-9df2956fd4eb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01SrXxViaWpeMquEDZJNXqaa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15560,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15560,
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

_source line 3 · 2026-05-15T23:02:02.236Z_

<details open><summary>🔧 Tool call — Read · `toolu_01M7WCzMi5cDUowc7LDUZ2Dv`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d8cb0e4a-da75-42b0-8ed1-d5e274313c3f",
  "isSidechain": true,
  "agentId": "a62a755bf7232a081",
  "requestId": "req_011Cb5BqKZUBBarcfMVhUZmE",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "263b8d18-0184-4759-a7b9-f3ad66e42b61",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "ff2a3926-a23a-4756-aa8c-9df2956fd4eb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01SrXxViaWpeMquEDZJNXqaa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15560,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15560,
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

_source line 4 · 2026-05-15T23:02:02.248Z_

<details><summary>↩ Tool result · `toolu_01M7WCzMi5cDUowc7LDUZ2Dv`</summary>

```text
1	\begin{abstract}
2	GRPO-trained neurosymbolic formalizers achieve high prove rates---93\% on FOLIO---yet 87\% of proved outputs embed the conclusion verbatim among the premises, a degenerate shortcut invisible to execution reward.
3	We introduce \emph{Solver Trace Ablation} (STA), a diagnostic that applies leave-one-out component necessity testing to solver inputs.
4	The fraction of components whose removal causes proof failure yields the \emph{Intensional Structural Reward} (ISR): ISR$=$1 indicates full necessity; ISR$=$0 complete redundancy.
5	ISR is uncorrelated with downstream NLI accuracy ($\rho{=}{-}0.049$), confirming it measures structural---not semantic---integrity.
6	As a diagnostic, ISR exposes a collapse trajectory hidden from PR: over 100--1000 GRPO steps (Qwen3-4B), ISR falls $0.642{\to}0.003$ while PR rises $32\%{\to}96\%$; an SFT baseline reaches 92.3\% non-hacking on identical data (3-seed pooled), localizing the failure to RL.
7	As a reward, $r = r_{\text{exec}}\cdot(1{+}\beta\,\text{ISR})$ at $\beta{=}0.1$ induces \emph{meta-level Goodhart's Law}: 70.6\% conclusion duplication (H7) versus 13.7\% under matched random (Fisher $p{=}1.3{\times}10^{-39}$; random H7 is seed-dependent, driven by one of three seeds); ISR amplifies H7 frequency ${\sim}5{\times}$ rather than exclusively causing it; the sole apparent ISR improvement reduces to $1.06\times$ after controlling for a premise-count confound; $\beta{=}0.3$ destabilizes training regardless of signal source (ISR: PR $66{\pm}42\%$; random: $54{\pm}35\%$), with individual seeds collapsing to as low as $18\%$.
8	Cross-logic transfer to Prolog yields universal Goodhart: 3/3 seeds gaming via distinct mechanisms, 0\% non-hacking.
9	Across 6 reward conditions, 2 logic types, 3 seeds, we catalog 8 hacking modes---including query-as-fact gaming that bypasses text-match classifiers---documenting ISR's fundamental asymmetry: reliable as a diagnostic, unreliable as an optimization target.\footnote{Code and data: \url{[anonymized]}}
10	\end{abstract}
11	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "263b8d18-0184-4759-a7b9-f3ad66e42b61",
  "isSidechain": true,
  "promptId": "169bea34-34c4-423a-9946-976e7f30e506",
  "agentId": "a62a755bf7232a081",
  "type": "user",
  "uuid": "b86bfd2d-fc7d-4796-9413-057588190c52",
  "sourceToolAssistantUUID": "263b8d18-0184-4759-a7b9-f3ad66e42b61",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "ff2a3926-a23a-4756-aa8c-9df2956fd4eb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-15T23:02:02.702Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Rs9uWygiCxzfzBEU9pX6vs`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b86bfd2d-fc7d-4796-9413-057588190c52",
  "isSidechain": true,
  "agentId": "a62a755bf7232a081",
  "requestId": "req_011Cb5BqKZUBBarcfMVhUZmE",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d2fc6260-d011-4538-8a0f-f56a21873c05",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "ff2a3926-a23a-4756-aa8c-9df2956fd4eb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01SrXxViaWpeMquEDZJNXqaa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15560,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15560,
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

_source line 6 · 2026-05-15T23:02:02.711Z_

<details><summary>↩ Tool result · `toolu_01Rs9uWygiCxzfzBEU9pX6vs`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	A GRPO-trained formalizer achieves a 93\% prove rate on first-order logic problems---yet 87\% of its proved outputs embed the conclusion verbatim among the premises.
5	The solver succeeds not because the model has learned to reason, but because the formalization trivially entails any conclusion already appearing as a premise.
6	This structural shortcut is invisible to execution-based evaluation: prove rate registers success regardless of whether the proof reflects genuine derivation or degenerate circular embedding.
7	
8	\paragraph{The execution-only blind spot.}
9	Prove rate---the dominant evaluation metric for neurosymbolic formalizers~\citep{logic-lm, linc, satlm}---conflates faithful reasoning with degenerate shortcuts, a gap especially consequential under RL, where the optimizer exploits any shortcut the reward fails to penalize~\citep{skalse-reward-hacking, reward-hacking-survey}.
10	Recent work applies GRPO~\citep{deepseekmath} to train LLMs that generate solver-verified formal programs~\citep{mellgren-prolog-grpo, logic-rl} using binary execution feedback; this drives rapid PR gains but gives no gradient on structural quality.
11	Process reward models~\citep{lightman-verify-step, math-shepherd} require expensive annotations and do not transfer to arbitrary solver-backed settings.
12	A separate line documents that LLMs already game logical formalization at inference time~\citep{kim-game-formalization, bondarenko-spec-gaming}; what is missing is an annotation-free \emph{diagnostic} for structural integrity in neurosymbolic outputs.
13	
14	\paragraph{Component necessity testing.}
15	We address this gap with \emph{Solver Trace Ablation} (STA), a diagnostic applying \emph{component necessity testing}---leave-one-out (LOO) ablation on solver inputs---to quantify structural integrity (Figure~\ref{fig:sta-overview}).
16	For each proved formalization, STA removes each component individually and re-runs the solver; the fraction of components whose removal causes proof failure yields the \emph{Intensional Structural Reward} (ISR), with $\text{ISR}{=}1$ indicating full necessity and $\text{ISR}{=}0$ complete redundancy.
17	LOO ablation itself is standard~\citep{demillo1978, jia-harman-survey}; novelty lies in its application as a GRPO-hacking diagnostic and in the empirical phenomena it surfaces.
18	ISR captures structural rather than semantic integrity (downstream NLI: $\rho{=}{-}0.049$, $p{=}0.187$).
19	
20	\paragraph{ISR as diagnostic.}
21	As a post-hoc diagnostic on a GRPO formalizer trained with FOLIO~\citep{folio}, ISR reveals a structural collapse trajectory invisible to PR: $\text{ISR}^{*}{:}\,0.642\to 0.132\to 0.003$ over 100--1000 steps (99.5\% degradation) while PR rises $32\%{\to}96\%$.
22	Three seeds diverge radically (PR $\sigma{=}47$\,pp), each converging to a qualitatively different mode: conclusion embedding, repetition collapse, and tautological collapse.
23	An SFT baseline on identical data reaches $\text{PR}{=}13.0\%$ with 92.3\% non-hacking (3-seed pooled, 1000 steps), localizing the failure to RL optimization, not data or capacity.
24	
25	\paragraph{Meta-level Goodhart.}
26	Repurposed as a training signal, $r = r_{\text{exec}} \cdot (1 + \beta\,\text{ISR})$, ISR is gamed at its own definition---\emph{meta-level Goodhart's Law}~\citep{manheim-goodhart-taxonomy, karwowski-goodhart-rl, gao-reward-overoptimization}.
27	At $\beta{=}0.1$, 70.6\% of proved samples exhibit conclusion duplication (H7)---versus 13.7\% under matched random (Fisher $p{<}10^{-38}$; random H7 is highly seed-dependent), showing ISR amplifies tautological collapse by ${\sim}5{\times}$; the one seed with non-trivial residual reduces to $1.06\times$ random after controlling for a premise-count confound.
28	At $\beta{=}0.3$, both ISR and random produce extreme cross-seed instability (PR $66{\pm}42\%$ and $54{\pm}35\%$ respectively), confirming high-dose proxy weighting is harmful regardless of signal content; ISR seeds diverge into three distinct pathways (reward collapse, shortcut dominance, pure metric gaming) while random converges uniformly to H1.
29	The effect transfers and intensifies in Prolog: 3/3 seeds yield 0\% non-hacking via distinct mechanisms, including \emph{query-as-fact gaming} that bypasses text-match classifiers.
30	ISR's asymmetry is the central finding: \emph{reliable as observer, unreliable as optimizer.}
31	
32	\paragraph{Contributions.}
33	Across 6 reward conditions, 3 seeds, 2 logic types, and up to 1000 steps, we contribute: (\textbf{C1}) ISR as a diagnostic for GRPO reward hacking, with a 99.5\% collapse trajectory invisible to PR and an SFT control localizing the failure to RL (\S\ref{sec:diagnostic}); (\textbf{C2}) empirical meta-level Goodhart, with a random control showing ISR amplifies H7 gaming ${\sim}5{\times}$ (70.6\% vs.\ 13.7\%, Fisher $p{<}10^{-38}$; random H7 is seed-dependent) and a premise-count-matched analysis showing the sole apparent gain is an LOO artifact (\S\ref{sec:goodhart}); (\textbf{C3}) cross-logic transfer to Prolog with universal Goodhart (\S\ref{sec:crosslogic}); (\textbf{C4}) an eight-mode hacking taxonomy including query-as-fact gaming and obfuscated tautology, motivating functional cross-validation of diagnostics (\S\ref{sec:taxonomy}).
34	These are cautionary results for any work treating a structural proxy as a training signal.
35	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d2fc6260-d011-4538-8a0f-f56a21873c05",
  "isSidechain": true,
  "promptId": "169bea34-34c4-423a-9946-976e7f30e506",
  "agentId": "a62a755bf7232a081",
  "type": "user",
  "uuid": "859d7017-ebaf-4f9e-9651-daa3bd804787",
  "sourceToolAssistantUUID": "d2fc6260-d011-4538-8a0f-f56a21873c05",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "ff2a3926-a23a-4756-aa8c-9df2956fd4eb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-15T23:02:02.873Z_

<details open><summary>🔧 Tool call — Read · `toolu_01JLcMFTB26YTYU5igbCfxAZ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "859d7017-ebaf-4f9e-9651-daa3bd804787",
  "isSidechain": true,
  "agentId": "a62a755bf7232a081",
  "requestId": "req_011Cb5BqKZUBBarcfMVhUZmE",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "e66422d3-e440-4813-955a-1d8621b9011a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "ff2a3926-a23a-4756-aa8c-9df2956fd4eb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01SrXxViaWpeMquEDZJNXqaa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15560,
      "cache_read_input_tokens": 0,
      "output_tokens": 307,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 15560
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 307,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 15560,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 15560,
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

_source line 8 · 2026-05-15T23:02:02.879Z_

<details><summary>↩ Tool result · `toolu_01JLcMFTB26YTYU5igbCfxAZ`</summary>

```text
1	\section{Related Work}
2	\label{sec:related-work}
3	
4	\paragraph{Neurosymbolic reasoning.}
5	LLM-solver pipelines~\citep{satlm, logic-lm, linc, fover-pei2025, lorp} and RL methods trained on solver feedback~\citep{mellgren-prolog-grpo, logic-rl, deepseek-prover-v15} evaluate execution accuracy alone, with no diagnostic for structural quality.
6	We use FOLIO~\citep{folio}, the only public NLI benchmark with both FOL and Prolog annotations.
7	
8	\paragraph{Process rewards and reward shaping.}
9	Learned PRMs~\citep{lightman-verify-step, math-shepherd} provide step-level feedback but suffer from reward-model noise and distribution shift~\citep{processbench}: \citet{gao-effective-rl-reward} show that auxiliary process/outcome rewards can \emph{hurt} RL training relative to success-only reward, a finding our ISR-as-reward results corroborate.
10	Symbolic feedback approaches~\citep{rlsf} use solver certificates as token-level rewards, achieving gains on program synthesis; ISR differs in operating at the component level (LOO ablation) rather than the token level, and our results show this structural signal is gamed when optimized.
11	Rubric-grounded GRPO~\citep{rubric-grpo} uses structured LLM-judge rewards to improve generalization; ISR is solver-derived and deterministic rather than judge-based, but both represent structured alternatives to scalar execution reward.
12	The shared lesson across these approaches is that reward augmentation introduces proxy risk---our contribution is demonstrating the \emph{meta}-level variant where the diagnostic itself becomes the target.
13	
14	\paragraph{Reward hacking and Goodhart's Law.}
15	Goodhart's Law is established theoretically~\citep{manheim-goodhart-taxonomy, skalse-reward-hacking, karwowski-goodhart-rl} and empirically in RLHF and frontier models~\citep{gao-reward-overoptimization, bondarenko-spec-gaming, kim-game-formalization}.
16	\citet{kwa-catastrophic-goodhart} show that heavy-tailed reward misspecification causes \emph{catastrophic} Goodhart where KL regularization provably fails, offering a theoretical lens for why GRPO's KL penalty does not prevent the ISR collapse we observe.
17	Recent work further documents spurious reward signals in RLVR~\citep{spurious-rewards} and reward hacking in frontier models~\citep{metr-reward-hacking}.
18	Our setting differs in three ways: ISR is deterministic and solver-derived rather than learned; gaming \emph{emerges during RL training} rather than at inference time; and the effect operates at a \emph{meta} level---the diagnostic for gaming itself becomes gamed when optimized---a phenomenon, to our knowledge, not previously documented.
19	
20	\paragraph{Mutation testing.}
21	STA adapts the LOO mutation paradigm~\citep{demillo1978, jia-harman-survey} to solver inputs; novelty lies in application and findings, not in the perturbation primitive.
22	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e66422d3-e440-4813-955a-1d8621b9011a",
  "isSidechain": true,
  "promptId": "169bea34-34c4-423a-9946-976e7f30e506",
  "agentId": "a62a755bf7232a081",
  "type": "user",
  "uuid": "9321e72e-d8bd-4165-b129-f071b629c83d",
  "sourceToolAssistantUUID": "e66422d3-e440-4813-955a-1d8621b9011a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "ff2a3926-a23a-4756-aa8c-9df2956fd4eb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-15T23:02:02.934Z_

<details open><summary>🔧 Tool call — Read · `toolu_0111p2EkE6AGcJaMhi4gY6ZQ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9321e72e-d8bd-4165-b129-f071b629c83d",
  "isSidechain": true,
  "agentId": "a62a755bf7232a081",
  "requestId": "req_011Cb5BqKZUBBarcfMVhUZmE",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d279e287-ee70-4dfb-8d2f-aaa635b8eb11",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "ff2a3926-a23a-4756-aa8c-9df2956fd4eb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01SrXxViaWpeMquEDZJNXqaa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15560,
      "cache_read_input_tokens": 0,
      "output_tokens": 307,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 15560
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 307,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 15560,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 15560,
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

_source line 10 · 2026-05-15T23:02:02.939Z_

<details><summary>↩ Tool result · `toolu_0111p2EkE6AGcJaMhi4gY6ZQ`</summary>

```text
1	\section{Limitations}
2	\label{sec:limitations}
3	
4	Experiments use a single base model (Qwen3-4B) and dataset family (FOLIO); generalization remains untested.
5	ISR quantifies syntactic component necessity, not semantic faithfulness: a downstream NLI evaluation finds ISR and task accuracy uncorrelated (Spearman $\rho{=}{-}0.049$, $p{=}0.187$; Appendix~\ref{app:extended-discussion}).
6	Three seeds demonstrate qualitative divergence but limit statistical power.
7	STA requires solvers supporting component-level input manipulation.
8	
9	\paragraph{Data scale.}
10	Our experiments use 500 training examples and 100 evaluation examples, drawn from FOLIO~\citep{folio}.
11	The training subset is selected via stratified sampling (seed 42) and held constant across all conditions.
12	While our findings are consistent across seeds and logic types, the effect of training data scale on hacking prevalence and mode distribution remains an open question for future work.
13	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d279e287-ee70-4dfb-8d2f-aaa635b8eb11",
  "isSidechain": true,
  "promptId": "169bea34-34c4-423a-9946-976e7f30e506",
  "agentId": "a62a755bf7232a081",
  "type": "user",
  "uuid": "b7b3d125-f41b-4d0c-b1f5-a20844d033da",
  "sourceToolAssistantUUID": "d279e287-ee70-4dfb-8d2f-aaa635b8eb11",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "ff2a3926-a23a-4756-aa8c-9df2956fd4eb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-15T23:02:43.094Z_

Here are the complete contents of all four files:

## 1. abstract.tex

```
\begin{abstract}
GRPO-trained neurosymbolic formalizers achieve high prove rates---93\% on FOLIO---yet 87\% of proved outputs embed the conclusion verbatim among the premises, a degenerate shortcut invisible to execution reward.
We introduce \emph{Solver Trace Ablation} (STA), a diagnostic that applies leave-one-out component necessity testing to solver inputs.
The fraction of components whose removal causes proof failure yields the \emph{Intensional Structural Reward} (ISR): ISR$=$1 indicates full necessity; ISR$=$0 complete redundancy.
ISR is uncorrelated with downstream NLI accuracy ($\rho{=}{-}0.049$), confirming it measures structural---not semantic---integrity.
As a diagnostic, ISR exposes a collapse trajectory hidden from PR: over 100--1000 GRPO steps (Qwen3-4B), ISR falls $0.642{\to}0.003$ while PR rises $32\%{\to}96\%$; an SFT baseline reaches 92.3\% non-hacking on identical data (3-seed pooled), localizing the failure to RL.
As a reward, $r = r_{\text{exec}}\cdot(1{+}\beta\,\text{ISR})$ at $\beta{=}0.1$ induces \emph{meta-level Goodhart's Law}: 70.6\% conclusion duplication (H7) versus 13.7\% under matched random (Fisher $p{=}1.3{\times}10^{-39}$; random H7 is seed-dependent, driven by one of three seeds); ISR amplifies H7 frequency ${\sim}5{\times}$ rather than exclusively causing it; the sole apparent ISR improvement reduces to $1.06\times$ after controlling for a premise-count confound; $\beta{=}0.3$ destabilizes training regardless of signal source (ISR: PR $66{\pm}42\%$; random: $54{\pm}35\%$), with individual seeds collapsing to as low as $18\%$.
Cross-logic transfer to Prolog yields universal Goodhart: 3/3 seeds gaming via distinct mechanisms, 0\% non-hacking.
Across 6 reward conditions, 2 logic types, 3 seeds, we catalog 8 hacking modes---including query-as-fact gaming that bypasses text-match classifiers---documenting ISR's fundamental asymmetry: reliable as a diagnostic, unreliable as an optimization target.\footnote{Code and data: \url{[anonymized]}}
\end{abstract}
```

## 2. introduction.tex

```
\section{Introduction}
\label{sec:introduction}

A GRPO-trained formalizer achieves a 93\% prove rate on first-order logic problems---yet 87\% of its proved outputs embed the conclusion verbatim among the premises.
The solver succeeds not because the model has learned to reason, but because the formalization trivially entails any conclusion already appearing as a premise.
This structural shortcut is invisible to execution-based evaluation: prove rate registers success regardless of whether the proof reflects genuine derivation or degenerate circular embedding.

\paragraph{The execution-only blind spot.}
Prove rate---the dominant evaluation metric for neurosymbolic formalizers~\citep{logic-lm, linc, satlm}---conflates faithful reasoning with degenerate shortcuts, a gap especially consequential under RL, where the optimizer exploits any shortcut the reward fails to penalize~\citep{skalse-reward-hacking, reward-hacking-survey}.
Recent work applies GRPO~\citep{deepseekmath} to train LLMs that generate solver-verified formal programs~\citep{mellgren-prolog-grpo, logic-rl} using binary execution feedback; this drives rapid PR gains but gives no gradient on structural quality.
Process reward models~\citep{lightman-verify-step, math-shepherd} require expensive annotations and do not transfer to arbitrary solver-backed settings.
A separate line documents that LLMs already game logical formalization at inference time~\citep{kim-game-formalization, bondarenko-spec-gaming}; what is missing is an annotation-free \emph{diagnostic} for structural integrity in neurosymbolic outputs.

\paragraph{Component necessity testing.}
We address this gap with \emph{Solver Trace Ablation} (STA), a diagnostic applying \emph{component necessity testing}---leave-one-out (LOO) ablation on solver inputs---to quantify structural integrity (Figure~\ref{fig:sta-overview}).
For each proved formalization, STA removes each component individually and re-runs the solver; the fraction of components whose removal causes proof failure yields the \emph{Intensional Structural Reward} (ISR), with $\text{ISR}{=}1$ indicating full necessity and $\text{ISR}{=}0$ complete redundancy.
LOO ablation itself is standard~\citep{demillo1978, jia-harman-survey}; novelty lies in its application as a GRPO-hacking diagnostic and in the empirical phenomena it surfaces.
ISR captures structural rather than semantic integrity (downstream NLI: $\rho{=}{-}0.049$, $p{=}0.187$).

\paragraph{ISR as diagnostic.}
As a post-hoc diagnostic on a GRPO formalizer trained with FOLIO~\citep{folio}, ISR reveals a structural collapse trajectory invisible to PR: $\text{ISR}^{*}{:}\,0.642\to 0.132\to 0.003$ over 100--1000 steps (99.5\% degradation) while PR rises $32\%{\to}96\%$.
Three seeds diverge radically (PR $\sigma{=}47\,pp$), each converging to a qualitatively different mode: conclusion embedding, repetition collapse, and tautological collapse.
An SFT baseline on identical data reaches $\text{PR}{=}13.0\%$ with 92.3\% non-hacking (3-seed pooled, 1000 steps), localizing the failure to RL optimization, not data or capacity.

\paragraph{Meta-level Goodhart.}
Repurposed as a training signal, $r = r_{\text{exec}} \cdot (1 + \beta\,\text{ISR})$, ISR is gamed at its own definition---\emph{meta-level Goodhart's Law}~\citep{manheim-goodhart-taxonomy, karwowski-goodhart-rl, gao-reward-overoptimization}.
At $\beta{=}0.1$, 70.6\% of proved samples exhibit conclusion duplication (H7)---versus 13.7\% under matched random (Fisher $p{<}10^{-38}$; random H7 is highly seed-dependent), showing ISR amplifies tautological collapse by ${\sim}5{\times}$; the one seed with non-trivial residual reduces to $1.06\times$ random after controlling for a premise-count confound.
At $\beta{=}0.3$, both ISR and random produce extreme cross-seed instability (PR $66{\pm}42\%$ and $54{\pm}35\%$ respectively), confirming high-dose proxy weighting is harmful regardless of signal content; ISR seeds diverge into three distinct pathways (reward collapse, shortcut dominance, pure metric gaming) while random converges uniformly to H1.
The effect transfers and intensifies in Prolog: 3/3 seeds yield 0\% non-hacking via distinct mechanisms, including \emph{query-as-fact gaming} that bypasses text-match classifiers.
ISR's asymmetry is the central finding: \emph{reliable as observer, unreliable as optimizer.}

\paragraph{Contributions.}
Across 6 reward conditions, 3 seeds, 2 logic types, and up to 1000 steps, we contribute: (\textbf{C1}) ISR as a diagnostic for GRPO reward hacking, with a 99.5\% collapse trajectory invisible to PR and an SFT control localizing the failure to RL (\S\ref{sec:diagnostic}); (\textbf{C2}) empirical meta-level Goodhart, with a random control showing ISR amplifies H7 gaming ${\sim}5{\times}$ (70.6\% vs.\ 13.7\%, Fisher $p{<}10^{-38}$; random H7 is seed-dependent) and a premise-count-matched analysis showing the sole apparent gain is an LOO artifact (\S\ref{sec:goodhart}); (\textbf{C3}) cross-logic transfer to Prolog with universal Goodhart (\S\ref{sec:crosslogic}); (\textbf{C4}) an eight-mode hacking taxonomy including query-as-fact gaming and obfuscated tautology, motivating functional cross-validation of diagnostics (\S\ref{sec:taxonomy}).
These are cautionary results for any work treating a structural proxy as a training signal.
```

## 3. related_work.tex

```
\section{Related Work}
\label{sec:related-work}

\paragraph{Neurosymbolic reasoning.}
LLM-solver pipelines~\citep{satlm, logic-lm, linc, fover-pei2025, lorp} and RL methods trained on solver feedback~\citep{mellgren-prolog-grpo, logic-rl, deepseek-prover-v15} evaluate execution accuracy alone, with no diagnostic for structural quality.
We use FOLIO~\citep{folio}, the only public NLI benchmark with both FOL and Prolog annotations.

\paragraph{Process rewards and reward shaping.}
Learned PRMs~\citep{lightman-verify-step, math-shepherd} provide step-level feedback but suffer from reward-model noise and distribution shift~\citep{processbench}: \citet{gao-effective-rl-reward} show that auxiliary process/outcome rewards can \emph{hurt} RL training relative to success-only reward, a finding our ISR-as-reward results corroborate.
Symbolic feedback approaches~\citep{rlsf} use solver certificates as token-level rewards, achieving gains on program synthesis; ISR differs in operating at the component level (LOO ablation) rather than the token level, and our results show this structural signal is gamed when optimized.
Rubric-grounded GRPO~\citep{rubric-grpo} uses structured LLM-judge rewards to improve generalization; ISR is solver-derived and deterministic rather than judge-based, but both represent structured alternatives to scalar execution reward.
The shared lesson across these approaches is that reward augmentation introduces proxy risk---our contribution is demonstrating the \emph{meta}-level variant where the diagnostic itself becomes the target.

\paragraph{Reward hacking and Goodhart's Law.}
Goodhart's Law is established theoretically~\citep{manheim-goodhart-taxonomy, skalse-reward-hacking, karwowski-goodhart-rl} and empirically in RLHF and frontier models~\citep{gao-reward-overoptimization, bondarenko-spec-gaming, kim-game-formalization}.
\citet{kwa-catastrophic-goodhart} show that heavy-tailed reward misspecification causes \emph{catastrophic} Goodhart where KL regularization provably fails, offering a theoretical lens for why GRPO's KL penalty does not prevent the ISR collapse we observe.
Recent work further documents spurious reward signals in RLVR~\citep{spurious-rewards} and reward hacking in frontier models~\citep{metr-reward-hacking}.
Our setting differs in three ways: ISR is deterministic and solver-derived rather than learned; gaming \emph{emerges during RL training} rather than at inference time; and the effect operates at a \emph{meta} level---the diagnostic for gaming itself becomes gamed when optimized---a phenomenon, to our knowledge, not previously documented.

\paragraph{Mutation testing.}
STA adapts the LOO mutation paradigm~\citep{demillo1978, jia-harman-survey} to solver inputs; novelty lies in application and findings, not in the perturbation primitive.
```

## 4. limitations.tex

```
\section{Limitations}
\label{sec:limitations}

Experiments use a single base model (Qwen3-4B) and dataset family (FOLIO); generalization remains untested.
ISR quantifies syntactic component necessity, not semantic faithfulness: a downstream NLI evaluation finds ISR and task accuracy uncorrelated (Spearman $\rho{=}{-}0.049$, $p{=}0.187$; Appendix~\ref{app:extended-discussion}).
Three seeds demonstrate qualitative divergence but limit statistical power.
STA requires solvers supporting component-level input manipulation.

\paragraph{Data scale.}
Our experiments use 500 training examples and 100 evaluation examples, drawn from FOLIO~\citep{folio}.
The training subset is selected via stratified sampling (seed 42) and held constant across all conditions.
While our findings are consistent across seeds and logic types, the effect of training data scale on hacking prevalence and mode distribution remains an open question for future work.
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b7b3d125-f41b-4d0c-b1f5-a20844d033da",
  "isSidechain": true,
  "agentId": "a62a755bf7232a081",
  "requestId": "req_011Cb5BqTs3ARJhPhWL2k5de",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "b864189c-1d39-4e3c-a722-69a39bb2a8d5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "ff2a3926-a23a-4756-aa8c-9df2956fd4eb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_016FJtCAJEJmZUD3BzAH79mr",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 4609,
      "cache_read_input_tokens": 15560,
      "output_tokens": 3254,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4609
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 3254,
          "cache_read_input_tokens": 15560,
          "cache_creation_input_tokens": 4609,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4609,
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
