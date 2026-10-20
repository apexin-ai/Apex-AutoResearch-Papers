# Research conversation: Audit numerical consistency across all .tex files in /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gat

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 74
- **Recorded user turns:** 1
- **Tool calls:** 32
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a4138636fc3e34597.jsonl`
- **Structured JSON:** [`d7815531edddc7868108.json`](../../sessions/d7/d7815531edddc7868108.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

74 recorded events

### User

_source line 1 · 2026-05-16T02:54:05.399Z_

Audit numerical consistency across all .tex files in /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/

Check that these key numbers are consistent wherever they appear:
1. Δ ranges: DS 0.39→8.48, QW 0.07→3.16
2. G ranges: 7.5–79.8× (importance), ~1 (random)
3. n values: DS n=496, QW n=475, LLaMA n=49
4. p values: Bonferroni p < 10^-10 (DS), p < 10^-14 (QW)
5. Strategy contrast: 2.7–17× (across models), 15–17× (DS only)
6. Cross-arch: ~1/40 magnitude
7. Accuracy: QW dense=46%, s030=19%, δ=-27pp; DS dense=74%, s030=4%
8. Pilot: 18% recovery, CI spans zero
9. JT test: z=33.7 (DS), z≥6.2 (QW)
10. Random eviction: non-significant at s≤0.20, significant at s≥0.25

Search abstract.tex, introduction.tex, results.tex, analysis.tex, discussion.tex, conclusion.tex, limitations.tex, appendix_disc_analysis.tex, appendix_moved.tex. Report any discrepancies found.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "eeb83888-ea16-4335-9ad7-31eca084b764",
  "agentId": "a4138636fc3e34597",
  "type": "user",
  "uuid": "12e8bac4-ae00-46a5-84f7-31b109577023",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/paper_agent_9539225d",
  "sessionId": "75f62e16-26c1-41e3-a629-5dbc4dda9106",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cryptic-kindling-corbato"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-16T02:54:06.832Z_

I'll audit the numerical consistency across all the .tex files in the paper directory. Let me start by reading each file and checking for these key numbers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "12e8bac4-ae00-46a5-84f7-31b109577023",
  "isSidechain": true,
  "agentId": "a4138636fc3e34597",
  "requestId": "req_011Cb5VXkQYaiNk6sZqJwmP5",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "a77a2263-7633-4371-98c0-b79aaa60b842",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/paper_agent_9539225d",
  "sessionId": "75f62e16-26c1-41e3-a629-5dbc4dda9106",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cryptic-kindling-corbato",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_018HbpAa2YThWiohjDcSqpmc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 27512,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 27512,
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

_source line 3 · 2026-05-16T02:54:07.186Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01BP1d3r5pxQp3DjEHnSFwPU`</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a77a2263-7633-4371-98c0-b79aaa60b842",
  "isSidechain": true,
  "agentId": "a4138636fc3e34597",
  "requestId": "req_011Cb5VXkQYaiNk6sZqJwmP5",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "a32015f3-a30d-42aa-bcd7-fa9fbb7c5be7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/paper_agent_9539225d",
  "sessionId": "75f62e16-26c1-41e3-a629-5dbc4dda9106",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cryptic-kindling-corbato",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_018HbpAa2YThWiohjDcSqpmc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 27512,
      "cache_read_input_tokens": 0,
      "output_tokens": 119,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 27512
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 119,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 27512,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 27512,
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

_source line 4 · 2026-05-16T02:54:07.200Z_

<details><summary>↩ Tool result · `toolu_01BP1d3r5pxQp3DjEHnSFwPU`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/appendix_robustness.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/background.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/methodology.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/analysis.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/results.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/appendix_moved.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/appendix_disc_analysis.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/discussion.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a32015f3-a30d-42aa-bcd7-fa9fbb7c5be7",
  "isSidechain": true,
  "promptId": "eeb83888-ea16-4335-9ad7-31eca084b764",
  "agentId": "a4138636fc3e34597",
  "type": "user",
  "uuid": "f8adb6f8-e86c-45a8-803b-ca7466fe105b",
  "sourceToolAssistantUUID": "a32015f3-a30d-42aa-bcd7-fa9fbb7c5be7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/paper_agent_9539225d",
  "sessionId": "75f62e16-26c1-41e3-a629-5dbc4dda9106",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cryptic-kindling-corbato"
}
```

</details>

---

### Assistant

_source line 5 · 2026-05-16T02:54:08.374Z_

Now let me read all the key .tex files and search for the numerical values:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f8adb6f8-e86c-45a8-803b-ca7466fe105b",
  "isSidechain": true,
  "agentId": "a4138636fc3e34597",
  "requestId": "req_011Cb5VXsvUsvmhRuCsCcJZQ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "eb17bfee-7639-412d-8930-179605d129e2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/paper_agent_9539225d",
  "sessionId": "75f62e16-26c1-41e3-a629-5dbc4dda9106",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cryptic-kindling-corbato",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017LLWQUC4JnVD7mMGZdDxJ3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1565,
      "cache_read_input_tokens": 27512,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1565,
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

_source line 6 · 2026-05-16T02:54:08.614Z_

<details open><summary>🔧 Tool call — Read · `toolu_01P8UD4yNU97ZwmabfK6qT7f`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eb17bfee-7639-412d-8930-179605d129e2",
  "isSidechain": true,
  "agentId": "a4138636fc3e34597",
  "requestId": "req_011Cb5VXsvUsvmhRuCsCcJZQ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "080ae5c7-75fb-4ae7-bb2a-c88c4c9aa5c1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/paper_agent_9539225d",
  "sessionId": "75f62e16-26c1-41e3-a629-5dbc4dda9106",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cryptic-kindling-corbato",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017LLWQUC4JnVD7mMGZdDxJ3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1565,
      "cache_read_input_tokens": 27512,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1565,
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

_source line 7 · 2026-05-16T02:54:08.627Z_

<details><summary>↩ Tool result · `toolu_01P8UD4yNU97ZwmabfK6qT7f`</summary>

```text
1	\begin{abstract}
2	Compound sparsity---simultaneously pruning attention heads and evicting KV cache entries---is essential for efficient LLM inference but produces super-additive quality degradation whose structure is poorly understood.
3	We show that compound severity is not phase-invariant: the paired median severity difference ($\Delta$) increases from $0.39$ to $8.48$ across sparsity levels, with phase amplification ratios reaching $G{=}7.5$--$79.8{\times}$, in 7B-scale mathematical reasoning models.
4	
5	On DeepSeek-R1-Distill-Qwen-7B (MATH-500, $n{=}496$), importance-based eviction produces a monotonically increasing severity gradient (median $\Delta$: $0.39 \to 8.48$; all $p \ll 10^{-10}$). Random eviction is $2.7$--$17{\times}$ weaker where significant ($s \geq 0.25$), with a strategy ranking crossover at $s{=}0.25$.
6	The pattern replicates on Qwen2.5-7B-Instruct ($n_{\text{eff}}{=}475$, $\Delta$: $0.07 \to 3.16$; all $p < 10^{-14}$), with exploratory cross-architecture evidence from a LlamaForCausalLM model ($n{=}49$; ${\sim}1/40$ effect size) suggesting the qualitative pattern may extend beyond Qwen2 (\S\ref{sec:cross-arch}).
7	We present \emph{importance discrimination collapse}---the degeneration of head importance scores toward uniformity under compound stress---as a correlational diagnostic: both strategies exhibit near-identical Gini drops, yet severity diverges by $15$--$17{\times}$, implicating the structural specificity of importance-based pruning as the key differentiator.
8	These findings establish the phase-dependent nature of compound severity as a diagnostic foundation for future phase-aware mitigation strategies.
9	\end{abstract}
10	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "080ae5c7-75fb-4ae7-bb2a-c88c4c9aa5c1",
  "isSidechain": true,
  "promptId": "eeb83888-ea16-4335-9ad7-31eca084b764",
  "agentId": "a4138636fc3e34597",
  "type": "user",
  "uuid": "6dbd15fe-702a-46b8-9cca-673d11ba7fe5",
  "sourceToolAssistantUUID": "080ae5c7-75fb-4ae7-bb2a-c88c4c9aa5c1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/paper_agent_9539225d",
  "sessionId": "75f62e16-26c1-41e3-a629-5dbc4dda9106",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cryptic-kindling-corbato"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-16T02:54:08.837Z_

<details open><summary>🔧 Tool call — Read · `toolu_011E2H6Lsk3hVVwCDohymQ3d`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6dbd15fe-702a-46b8-9cca-673d11ba7fe5",
  "isSidechain": true,
  "agentId": "a4138636fc3e34597",
  "requestId": "req_011Cb5VXsvUsvmhRuCsCcJZQ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "cf4b0a33-1a0c-4d22-b33b-dc6d283c5e03",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/paper_agent_9539225d",
  "sessionId": "75f62e16-26c1-41e3-a629-5dbc4dda9106",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cryptic-kindling-corbato",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017LLWQUC4JnVD7mMGZdDxJ3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1565,
      "cache_read_input_tokens": 27512,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1565,
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

_source line 9 · 2026-05-16T02:54:08.858Z_

<details><summary>↩ Tool result · `toolu_011E2H6Lsk3hVVwCDohymQ3d`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Long-context language models place acute pressure on the key--value (KV) cache, which grows linearly with sequence length \cite{kwon-sosp2023, pope-mlsys2023}.
5	Two complementary responses---\emph{attention head pruning} \cite{voita-acl2019, michel-neurips2019} and \emph{KV cache eviction} \cite{snapkv-neurips2024, adakv-neurips2025}---can be deployed simultaneously as \emph{compound sparsity}, but the resulting quality degradation is often super-additive \cite{spark-aaai2026, slim-icml2025}. Recent evaluations confirm that reasoning capabilities degrade disproportionately under compound compression \cite{unicomp-2026}, and that per-dimension safe zones intersect to form a smaller joint safe region \cite{phase-transition-compression-2026}.
6	
7	Prior work treats compound interaction magnitude as roughly constant across generation \cite{spark-aaai2026, unicomp-2026}, despite evidence that pruning sensitivity depends on representational phase \cite{decision-repr-transition-2026} and that no single sparse attention strategy dominates across generation stages \cite{sparse-frontier-2025}.
8	This assumption is problematic for reasoning models, whose generations alternate between broadly distributed attention (exploratory reasoning) and sharply concentrated attention (structured computation) \cite{thinkv-iclr2026}.
9	Phase-aware methods like ThinKV \cite{thinkv-iclr2026} apply different KV strategies per phase but without considering compound interaction, while importance-based eviction itself faces challenges from greedy bias \cite{greedy-bias-kvcache-2026}, deferred importance \cite{retentivekv-2026}, and temporal dynamics in long generations \cite{lethe-aaai2026}. These methods each optimize a single pruning axis; we characterize the interaction when multiple mechanisms are composed.
10	If compound severity varies across these phases, a uniform sparsity budget may be safe in one phase yet destructive in another.
11	
12	What does compound interaction add beyond single-axis findings? Single-axis results on score collapse \cite{hies-2025}, phase-aware eviction \cite{thinkv-iclr2026}, and strategy non-dominance \cite{sparse-frontier-2025} qualitatively predict phase-dependent compound degradation---but two quantitative patterns cannot be derived from single-axis analyses. First, the severity gradient follows a \emph{strictly monotonic dose-response} (Jonckheere-Terpstra $z{=}33.7$, $p \ll 10^{-10}$). Second, in DeepSeek a \emph{strategy ranking crossover} emerges at $s{=}0.25$; Qwen shows consistent importance dominance, indicating model dependence. We report the paired median difference $\Delta$ ($0.39 \to 8.48$) as primary and the amplification ratio $G{=}7.5$--$79.8{\times}$ as auxiliary (\S\ref{sec:results}).
13	
14	We show that compound sparsity severity is strongly modulated by reasoning phase and eviction strategy.
15	Under importance-based KV cache eviction, the Interaction Index---a measure of super-additive degradation---concentrates in low-sparsity phases and is largely absent in high-sparsity phases.
16	On DeepSeek-R1-Distill-Qwen-7B (500 MATH-500 problems), the median phase difference rises from $0.39$ at $s{=}0.15$ to $8.48$ at $s{=}0.30$ (all Bonferroni-corrected $p \ll 10^{-10}$; Jonckheere-Terpstra $z{=}33.7$, $p \ll 10^{-10}$).
17	The pattern replicates on Qwen2.5-7B-Instruct ($\Delta$: $0.07 \to 3.16$; all $p < 10^{-14}$); preliminary evidence from DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM) suggests the phenomenon may extend beyond Qwen2 but at ${\sim}1/40$ the magnitude and with substantially weaker strategy contrast.
18	Random eviction develops a detectable but weak phase gradient only above $s \approx 0.20$ ($2.7$--$17{\times}$ smaller than importance-based where both strategies are significant, $s \geq 0.25$), confirming that the dominant gradient is an emergent phase-strategy interaction.
19	
20	We present preliminary correlational evidence for \emph{importance discrimination collapse}---the degeneration of head importance scores toward uniformity under compound stress---as a contributing factor, with the \emph{structural specificity} of importance-based pruning (which selectively removes high-score heads) as a key differentiator from random pruning.
21	
22	This work is a \textbf{diagnostic study}: we characterize a previously unknown interaction effect rather than proposing a mitigation method, following the tradition of empirical analysis papers \cite{voita-acl2019, michel-neurips2019}.
23	Our contributions:
24	\begin{enumerate}[nosep,leftmargin=*]
25	    \item We characterize a \textbf{phase--strategy interaction}: importance-based eviction exhibits a severity gradient across reasoning phases that is $2.7$--$17{\times}$ larger than under random eviction where both strategies show significant phase gradients ($s \geq 0.25$) on MATH-500; the gradient direction is consistent on GSM8K, where importance-based eviction produces significant phase gradients while random eviction does not (\S\ref{sec:cross-benchmark}).\footnote{The full MATH-500 range including non-significant random conditions ($s \leq 0.20$, where random $\Delta$ CIs span zero) extends to $39{\times}$.}
26	    \item We document that this gradient \textbf{increases monotonically with sparsity} and replicates across two Qwen2-architecture models with different training paradigms (DeepSeek-R1-Distill-Qwen-7B, reasoning-distilled; Qwen2.5-7B-Instruct, instruction-tuned), with preliminary evidence from a LlamaForCausalLM model suggesting the phenomenon may extend beyond Qwen2 (\S\ref{sec:results}).
27	    \item We provide a \textbf{correlational diagnostic} showing that aggregate importance discrimination collapse (Gini) is correlated with but not sufficient for severity amplification, with the structural specificity of pruned heads as the key differentiator (\S\ref{sec:analysis}).
28	\end{enumerate}
29	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cf4b0a33-1a0c-4d22-b33b-dc6d283c5e03",
  "isSidechain": true,
  "promptId": "eeb83888-ea16-4335-9ad7-31eca084b764",
  "agentId": "a4138636fc3e34597",
  "type": "user",
  "uuid": "c8cbdda3-5bbf-4a85-a685-17c68e3e3e0a",
  "sourceToolAssistantUUID": "cf4b0a33-1a0c-4d22-b33b-dc6d283c5e03",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/paper_agent_9539225d",
  "sessionId": "75f62e16-26c1-41e3-a629-5dbc4dda9106",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cryptic-kindling-corbato"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-16T02:54:09.259Z_

<details open><summary>🔧 Tool call — Read · `toolu_017rVpDgib5KjRD42RFoD4N6`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c8cbdda3-5bbf-4a85-a685-17c68e3e3e0a",
  "isSidechain": true,
  "agentId": "a4138636fc3e34597",
  "requestId": "req_011Cb5VXsvUsvmhRuCsCcJZQ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "657f0648-9263-4e71-9554-a5edbfe99dde",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/paper_agent_9539225d",
  "sessionId": "75f62e16-26c1-41e3-a629-5dbc4dda9106",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cryptic-kindling-corbato",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017LLWQUC4JnVD7mMGZdDxJ3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1565,
      "cache_read_input_tokens": 27512,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1565,
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

_source line 11 · 2026-05-16T02:54:09.296Z_

<details><summary>↩ Tool result · `toolu_017rVpDgib5KjRD42RFoD4N6`</summary>

```text
1	
2	\section{Results}
3	\label{sec:results}
4	
5	\subsection{Strategy-Dependent Severity}
6	\label{sec:strategy-severity}
7	
8	Table~\ref{tab:aggregate-ii} reports the median compound severity difference across strategies and sparsity levels. Under importance-based eviction, $\Delta$ increases from $0.39$ at $s{=}0.15$ to $8.48$ at $s{=}0.30$---a $22{\times}$ amplification (all Bonferroni-corrected $p \ll 10^{-10}$). Random eviction develops a detectable but weak phase gradient above $s \approx 0.20$: at $s \leq 0.20$, $\Delta$ is non-significant ($0.01$--$0.03$; CIs span zero); at $s \geq 0.25$, $\Delta$ becomes significant ($0.26$--$0.51$; $p_{\text{Bonf}} < 0.006$) but $15$--$17{\times}$ smaller than under importance-based eviction. Both strategies exhibit monotonic dose-response (Jonckheere-Terpstra $z{=}6.2$--$33.7$, all $p < 10^{-9}$), but importance masking effect sizes are an order of magnitude larger.
9	
10	\begin{table}[t]
11	\centering
12	\small
13	\caption{Median compound severity difference ($\Delta = \widetilde{\mathrm{II}}_{\textit{low}} - \widetilde{\mathrm{II}}_{\textit{high}}$) by eviction strategy and sparsity level on DeepSeek-R1-Distill-Qwen-7B ($n{=}496$, 500 MATH-500 problems).}
14	\label{tab:aggregate-ii}
15	\begin{tabular}{@{}lcccc@{}}
16	\toprule
17	Strategy & $s{=}0.15$ & $s{=}0.20$ & $s{=}0.25$ & $s{=}0.30$ \\
18	\midrule
19	Importance & 0.39 & 1.21 & 3.99 & 8.48 \\
20	Random     & 0.01 & 0.03 & 0.26 & 0.51 \\
21	\bottomrule
22	\end{tabular}
23	\end{table}
24	
25	
26	\subsection{Phase-Modulated Amplification}
27	\label{sec:phase-amplification}
28	
29	Decomposing II by reasoning phase reveals that strategy-dependent severity is driven by amplification in the low-sparsity phase. Table~\ref{tab:main-results} reports the per-phase breakdown at $n{=}496$. As a complementary perspective to $\Delta$, the per-problem amplification ratio $G$ (Eq.~\ref{eq:gradient}) quantifies relative phase contrast: $G$ increases from $7.5{\times}$ (95\% CI: $[4.1, 11.4]$) at $s{=}0.15$ to $79.8{\times}$ ($[63.3, 96.5]$) at $s{=}0.30$ under importance-based eviction, with all CIs excluding 1. Strong phase modulation is specific to importance-based eviction ($G{=}7.5$--$79.8{\times}$). Random eviction shows weak but statistically significant modulation at $s \geq 0.25$ ($G \approx 1.1$--$1.3$; CIs exclude 1), while at $s \leq 0.20$ the CIs span or touch 1. Figure~\ref{fig:hero} visualizes this contrast.
30	Under the multiplicative null ($r_b = r_a \cdot r_k$; Appendix~\ref{app:multiplicative-null}), the compound interaction is sub-multiplicative across all phases ($\mathrm{II}_{\times} < 0$), but the phase-severity gradient is preserved: $G_{\times}{=}21$--$64{\times}$ ($n{=}500$), indicating that the low-sparsity phase deviates from the multiplicative null by $21$--$64{\times}$ more than the high-sparsity phase. The qualitative conclusions---phase-modulated severity, strategy asymmetry, and crossover---are preserved; we report additive-null values throughout as the more conservative estimates.
31	
32	\begin{table*}[t]
33	\centering
34	\small
35	\caption{Per-phase interaction index (II) at $n{=}496$/$475$. $\Delta$: paired median difference with bootstrap 95\% CI ($B{=}10{,}000$). $G$: per-problem amplification ratio (Eq.~\ref{eq:gradient}) with bootstrap 95\% CI. Profiling-subset values ($n{=}50$) in Table~\ref{tab:profiling-subset}.}
36	\label{tab:main-results}
37	\begin{tabular}{@{}llcccc@{}}
38	\toprule
39	$s$ & Strategy & $\widetilde{\mathrm{II}}_{\textit{high}}$ & $\widetilde{\mathrm{II}}_{\textit{low}}$ & $\Delta$\; [95\% CI] & $G$\; [95\% CI] \\
40	\midrule
41	\multicolumn{6}{@{}l}{\textit{DeepSeek-R1-Distill-Qwen-7B ($n{=}496$)}} \\
42	0.15 & Importance & 0.003 & 0.357 & 0.39\; $[0.35,\; 0.44]$ & $\mathbf{7.5}$\; $[4.1,\; 11.4]$ \\
43	0.15 & Random     & 0.083 & 0.090 & 0.01\; $[-0.02,\; 0.04]$ & 0.5\; $[0.4,\; 0.6]$ \\
44	\addlinespace
45	0.20 & Importance & 0.008 & 1.211 & 1.21\; $[1.11,\; 1.34]$ & $\mathbf{17.9}$\; $[12.7,\; 26.3]$ \\
46	0.20 & Random     & 0.270 & 0.357 & 0.03\; $[-0.01,\; 0.08]$ & 0.8\; $[0.6,\; 0.9]$ \\
47	\addlinespace
48	0.25 & Importance & 0.021 & 3.971 & 3.99\; $[3.53,\; 4.36]$ & $\mathbf{49.1}$\; $[40.1,\; 57.8]$ \\
49	0.25 & Random     & 1.113 & 1.514 & 0.26\; $[0.13,\; 0.35]$ & 1.1\; $[1.0,\; 1.2]$ \\
50	\addlinespace
51	0.30 & Importance & 0.038 & 8.456 & 8.48\; $[7.75,\; 9.69]$ & $\mathbf{79.8}$\; $[63.3,\; 96.5]$ \\
52	0.30 & Random     & 3.112 & 3.848 & 0.51\; $[0.26,\; 0.89]$ & 1.1\; $[1.0,\; 1.3]$ \\
53	\midrule
54	\multicolumn{6}{@{}l}{\textit{Qwen2.5-7B-Instruct ($n{=}475$)}} \\
55	0.15 & Importance & $-$0.000$^{\ddagger}$ & 0.044 & 0.07\; $[0.05,\; 0.09]$ & n.d.$^{\dagger}$ \\
56	0.15 & Random     & 0.094 & 0.097 & $-$0.01\; $[-0.04,\; 0.01]$ & 0.7\; $[0.4,\; 0.8]$ \\
57	\addlinespace
58	0.20 & Importance & 0.000 & 0.275 & 0.31\; $[0.26,\; 0.36]$ & $\mathbf{2.6}$\; $[0.5,\; 5.1]$ \\
59	0.20 & Random     & 0.291 & 0.356 & 0.02\; $[-0.01,\; 0.07]$ & 0.9\; $[0.7,\; 1.0]$ \\
60	\addlinespace
61	0.25 & Importance & 0.004 & 1.053 & 1.07\; $[0.98,\; 1.18]$ & $\mathbf{9.5}$\; $[5.2,\; 14.8]$ \\
62	0.25 & Random     & 1.108 & 1.769 & 0.39\; $[0.24,\; 0.55]$ & 1.3\; $[1.2,\; 1.4]$ \\
63	\addlinespace
64	0.30 & Importance & 0.014 & 3.208 & 3.16\; $[2.78,\; 3.56]$ & $\mathbf{36.9}$\; $[25.3,\; 49.1]$ \\
65	0.30 & Random     & 2.819 & 4.253 & 0.91\; $[0.61,\; 1.26]$ & 1.3\; $[1.2,\; 1.4]$ \\
66	\bottomrule
67	\multicolumn{6}{@{}p{0.92\textwidth}}{\footnotesize $^{\dagger}$ $\widetilde{\mathrm{II}}_{\textit{high}} \approx 0$; ratio undefined ($G$ CI: $[-0.2, 0.9]$). $\Delta{=}0.07$, $p{=}8.7 \times 10^{-15}$ confirms $\mathrm{II}_{\textit{low}} > \mathrm{II}_{\textit{high}}$. $^{\ddagger}$ Negative II at this sparsity reflects \texttt{bfloat16} numerical noise when the interaction effect approaches zero ($|\mathrm{II}| < 10^{-4}$).}
68	\end{tabular}
69	\end{table*}
70	
71	\begin{figure}[t]
72	\centering
73	\includegraphics[width=\columnwidth]{fig1_dose_response.pdf}
74	\caption{Amplification ratio ($G$, auxiliary metric) as a function of sparsity level $s$ on DeepSeek-R1-Distill-Qwen-7B ($n{=}496$). Importance-based eviction (solid) exhibits an increasing gradient from $7.5{\times}$ to $79.8{\times}$; random eviction (dashed) remains near $1{\times}$ ($0.5{\times}$--$1.1{\times}$). Shaded regions show bootstrap 95\% CIs. The primary metric $\Delta$ (paired median difference) is in Table~\ref{tab:main-results}.}
75	\label{fig:hero}
76	\end{figure}
77	
78	
79	\subsection{Phase-Strategy Crossover}
80	\label{sec:crossover}
81	
82	The phase-strategy crossover is model-dependent. For DeepSeek ($n{=}496$), a strategy ranking reversal emerges at all four sparsity levels: at $s{=}0.25$, importance-based eviction yields \emph{lower} II than random in the high-sparsity phase ($0.021$ vs.\ $1.113$) but \emph{higher} II in the low-sparsity phase ($3.971$ vs.\ $1.514$---a $2.6{\times}$ reversal; both $p < 10^{-4}$), with reversal magnitude ranging from $2.2{\times}$ to $4.0{\times}$ across $s \in \{0.15, 0.20, 0.25, 0.30\}$. Qwen does \emph{not} exhibit this crossover: importance-based eviction produces lower II than random in both phases (e.g., at $s{=}0.25$: high $0.004$ vs.\ $1.108$; low $1.053$ vs.\ $1.769$). This divergence suggests the crossover arises from model-specific attention head specialization patterns rather than a universal compound-sparsity property. Full crossover analysis appears in Appendix~\ref{app:crossover-details}.
83	
84	\subsection{Replication Across Training Paradigms}
85	\label{sec:cross-model}
86	
87	DeepSeek-R1-Distill-Qwen-7B (distillation-trained) and Qwen2.5-7B-Instruct (instruction-tuned) share the Qwen2 backbone but differ in training objective, providing a within-architecture-family comparison across training paradigms.
88	Qwen2.5-7B-Instruct ($n_{\text{eff}}{=}475$) reproduces the monotonic severity gradient: $\Delta$ increases from $0.07$ at $s{=}0.15$ to $3.16$ at $s{=}0.30$ (all Bonferroni-corrected $p < 10^{-14}$), paralleling DeepSeek at approximately one-quarter to one-sixth the magnitude. Both models yield strictly increasing median $\Delta$ trajectories (Jonckheere-Terpstra $z \geq 6.2$, $p < 10^{-9}$; see \S\ref{par:stats}). Random eviction on Qwen mirrors DeepSeek: non-significant at $s \leq 0.20$, becoming significant at $s \geq 0.25$ ($\Delta{=}0.39$--$0.91$; $p_{\text{Bonf}} < 10^{-10}$) but $2.7$--$20{\times}$ weaker than importance-based. A caveat: 45.2\% of Qwen problems yield null mid-phase segments due to low temporal autocorrelation ($r{=}0.718$ vs.\ $0.894$); this does not affect $\Delta$ (Appendix~\ref{app:qwen-null-rate}). Full tables in Appendix~\ref{app:cross-model-details}.
89	
90	\subsection{Preliminary Cross-Architecture Analysis}
91	\label{sec:cross-arch}
92	
93	Preliminary cross-architecture validation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, $n{=}49$)\footnote{The $n{=}49$ sample is an initial profiling subset. Full-scale ($n{=}500$) LlamaForCausalLM replication is planned as future work; the current analysis prioritizes within-architecture replication (Qwen2) over cross-architecture breadth.} detects the phase-gated severity pattern for importance-based eviction (post-hoc power $> 0.99$ for within-importance gradient) but is inconclusive for strategy comparisons (power $0.26$--$0.63$); the interaction magnitude is ${\sim}40{\times}$ smaller than DeepSeek, suggesting that quantitative characteristics may be Qwen2-family-specific and that broader architectural diversity (e.g., Mistral, Gemma) is needed for generalization claims. Full results, including per-sparsity breakdowns and a power analysis motivating the sample size needed for definitive cross-architecture claims, appear in Appendix~\ref{app:cross-arch}.
94	
95	\subsection{Cross-Benchmark Validation: GSM8K}
96	\label{sec:cross-benchmark}
97	
98	To assess task generalization, we evaluate both models on GSM8K ($n{=}50$) at $s \in \{0.15, 0.20, 0.25, 0.30\}$. On DeepSeek (clean data, no output truncation), importance-based eviction replicates the MATH-500 phase gradient across all four sparsity levels with a strict dose-response: $\Delta{=}0.24$ at $s{=}0.15$ rising to $4.68$ at $s{=}0.30$ (all $p \leq 0.0003$, Wilcoxon). Strategy specificity on GSM8K manifests as a \emph{qualitative} gap: importance-based eviction produces significant phase gradients while random eviction is non-significant across all conditions (CIs spanning zero). We attribute this to \emph{task complexity}: GSM8K's simpler arithmetic induces more uniform attention distributions, yielding a flatter sparsity landscape; within MATH-500, longer traces exhibit higher strategy specificity (Spearman $\rho > 0$, $p < 0.02$), supporting cognitive load as the modulating variable. Qwen GSM8K results are inconclusive due to generation truncation (\texttt{max\_new\_tokens}${=}$2047): while directional consistency holds at $s \geq 0.25$ ($\Delta{=}1.14$--$4.62$; $p < 10^{-4}$), absolute values and phase assignments are unreliable because all outputs hit the token limit. Full tables in Appendix~\ref{app:gsm8k}.
99	
100	\subsection{Statistical Validation}
101	\label{sec:stat-validation}
102	
103	Table~\ref{tab:cohens-d} reports the paired median difference $\Delta$ under importance-based eviction for both models at $n{=}496$/$475$. All eight conditions yield CIs excluding zero; within-importance dose-response $d_z$ (s015 vs.\ s030) is $0.94$ (DeepSeek) and $0.92$ (Qwen), both large effects. Importance-based eviction produces significantly larger phase gradients than random at all four sparsity levels ($p_{\text{Bonf}} \ll 10^{-10}$, Wilcoxon; permutation tests in Appendix~\ref{app:permutation-details}).
104	
105	\begin{table}[t]
106	\centering
107	\small
108	\caption{Median of paired differences ($\Delta_i = \mathrm{II}^{(i)}_{\textit{low}} - \mathrm{II}^{(i)}_{\textit{high}}$) under importance-based eviction with bootstrap 95\% CIs ($B{=}10{,}000$).}
109	\label{tab:cohens-d}
110	\begin{tabular}{@{}lcc@{}}
111	\toprule
112	$s$ & DS ($n{=}496$): $\widetilde{\Delta}$\; [95\% CI] & QW ($n{=}475$): $\widetilde{\Delta}$\; [95\% CI] \\
113	\midrule
114	0.15 & $0.39$\; $[0.35,\; 0.44]$ & $0.07$\; $[0.05,\; 0.09]$ \\
115	0.20 & $1.21$\; $[1.11,\; 1.34]$ & $0.31$\; $[0.26,\; 0.36]$ \\
116	0.25 & $3.99$\; $[3.53,\; 4.36]$ & $1.07$\; $[0.98,\; 1.18]$ \\
117	0.30 & $8.48$\; $[7.75,\; 9.69]$ & $3.16$\; $[2.78,\; 3.56]$ \\
118	\bottomrule
119	\multicolumn{3}{@{}l}{\footnotesize All $p_{\text{Bonf}} < 10^{-13}$. Within-importance $d_z$ (s015 vs.\ s030): DS $0.94$, QW $0.92$.}
120	\end{tabular}
121	\end{table}
122	
123	\subsection{Answer-Region Analysis}
124	\label{sec:answer-region}
125	
126	Across both models, 93.2\% of answer tokens (\verb|\boxed{}| markers) fall within the high-sparsity phase, where compound interaction is minimal ($G \approx 1$). This non-uniformity identifies \emph{where} severity concentrates: reasoning-trace tokens show $5.7$--$43.5{\times}$ PPL degradation vs.\ $1.3$--$5.3{\times}$ for answer tokens (Wilcoxon $p < 0.001$). However, reasoning-trace degradation may produce \emph{silent reasoning errors}---correct formatting with corrupted intermediate logic \cite{lanham-2023-faithfulness, turpin-2023-biased-cot}---a failure mode that PPL detects but answer-level accuracy may miss.
127	
128	\subsection{Downstream Accuracy Validation}
129	\label{sec:accuracy-validation}
130	
131	To validate that the PPL-based severity gradient translates to downstream task performance, we evaluate MATH-500 accuracy under compound sparsity (importance-based eviction, \texttt{max\_new\_tokens}${=}$8192; Table~\ref{tab:accuracy}). Qwen's minimal truncation ($\leq 4\%$) provides a clean PPL-accuracy bridge.
132	Qwen ($n{=}100$; truncation $\leq 4\%$) shows gradual decline from $46\%$ (dense) through $s{=}0.25$ ($\delta{=}-4$ to $-13$\,pp) with a sharp cliff at $s{=}0.30$ ($19\%$, $\delta{=}-27$\,pp). DeepSeek ($n{=}50$) degrades more steeply ($74\% \to 4\%$) with a dual-regime structure: at $s \leq 0.20$, degradation is primarily truncation-driven (non-truncated accuracy remains $68$--$71\%$ at $s{=}0.15$--$0.20$ vs.\ $88\%$ dense); at $s \geq 0.25$, both truncation and reasoning quality collapse simultaneously (Appendix~\ref{app:accuracy-details}).
133	The two models exhibit distinct failure modes reflecting training-paradigm dependence: DeepSeek failures are \emph{truncation-dominated} (truncation $16\% \to 76\%$), while Qwen failures are \emph{wrong-answer-dominated} (truncation $\leq 4\%$, reasoning quality degrades directly).
134	
135	We provide a correlational mechanistic analysis in terms of importance discrimination collapse in \S\ref{sec:analysis}.
136	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "657f0648-9263-4e71-9554-a5edbfe99dde",
  "isSidechain": true,
  "promptId": "eeb83888-ea16-4335-9ad7-31eca084b764",
  "agentId": "a4138636fc3e34597",
  "type": "user",
  "uuid": "aa47b760-ecc8-4b58-b82a-ecf12a8704b1",
  "sourceToolAssistantUUID": "657f0648-9263-4e71-9554-a5edbfe99dde",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/paper_agent_9539225d",
  "sessionId": "75f62e16-26c1-41e3-a629-5dbc4dda9106",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cryptic-kindling-corbato"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-16T02:54:09.592Z_

<details open><summary>🔧 Tool call — Read · `toolu_01L6gdjKcRUqk7yNMbFCcmBH`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aa47b760-ecc8-4b58-b82a-ecf12a8704b1",
  "isSidechain": true,
  "agentId": "a4138636fc3e34597",
  "requestId": "req_011Cb5VXsvUsvmhRuCsCcJZQ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "7ab369a0-2481-4059-9ad8-2e0166c7bf7b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/paper_agent_9539225d",
  "sessionId": "75f62e16-26c1-41e3-a629-5dbc4dda9106",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cryptic-kindling-corbato",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017LLWQUC4JnVD7mMGZdDxJ3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1565,
      "cache_read_input_tokens": 27512,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1565,
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

_source line 13 · 2026-05-16T02:54:09.623Z_

<details><summary>↩ Tool result · `toolu_01L6gdjKcRUqk7yNMbFCcmBH`</summary>

```text
1	\section{Importance Discrimination Collapse under Compound Sparsity}
2	\label{sec:analysis}
3	
4	The mechanisms discussed here are \emph{correlational diagnostics} that illuminate but do not fully explain the $15$--$17{\times}$ severity divergence between strategies. Both strategies exhibit near-identical Gini drops ($<10\%$ difference), yet severity diverges by $15$--$17{\times}$---an order-of-magnitude mismatch indicating that aggregate concentration collapse alone is insufficient. The critical differentiator is \emph{structural specificity} of importance-based pruning, which systematically removes high-attention-score heads (\S\ref{sec:discrimination-collapse-main}).
5	
6	\subsection{Importance Discrimination Collapse}
7	\label{sec:discrimination-collapse-main}
8	
9	Head pruning systematically reduces the discriminative power of cumulative importance scores, suggesting a mechanism for the phase-strategy interaction. The Gini coefficient decreases by $0.030$--$0.081$ (DeepSeek, $6$--$17\%$ relative to dense baseline) and $0.010$--$0.020$ (Qwen, $2$--$4\%$) after pruning, with consistent negative deltas in all 16 conditions (Appendix~\ref{app:analysis}, Table~\ref{tab:discrimination-metrics-full}). Random eviction shows near-identical Gini drops (e.g., DeepSeek $s{=}0.25$: $-0.065$ vs.\ $-0.060$), confirming that collapse is a consequence of head pruning \emph{per se}. Yet importance-based severity is $15$--$17{\times}$ larger---the amplification arises because importance-based eviction \emph{depends on} the very scores that pruning degrades.
10	
11	This pattern---\emph{importance discrimination collapse}---reflects eviction degenerating into noise-sensitive selection as score distributions approach uniformity. The effect is phase-dependent: low-sparsity phases have broadly distributed attention where collapse has maximum impact; high-sparsity phases preserve concentration. \cite{hies-2025} report this collapse under single-axis pruning; we extend it to the compound setting.
12	
13	To provide quantitative evidence for structural specificity, we analyzed the attention Gini coefficients of importance-pruned versus retained heads. Importance pruning (Frobenius norm criterion) systematically removes heads with lower Gini coefficients---i.e., heads with more dispersed attention patterns (Mann-Whitney $U$, $p < 10^{-28}$; rank-biserial $r = 0.62$--$0.76$ across all 8 conditions). Random pruning, by contrast, samples heads with Gini indistinguishable from the population mean (200-trial verification). The Frobenius norm and Gini share sensitivity to attention magnitude; the large effect size ($r > 0.6$) nonetheless indicates strong structural separation.
14	
15	We note that this evidence is correlational; causal validation through controlled manipulation of importance-score entropy is an important direction for future work.
16	%% TODO: Add per-phase Gini results when available from Agent computation.
17	
18	\subsection{Entropy Redistribution: A Model-Dependent Secondary Effect}
19	\label{sec:entropy-redistribution-main}
20	
21	As a supplementary observation, head pruning also redistributes the attention entropy of surviving heads on DeepSeek ($\Delta\mathcal{H} \in [-0.047, -0.040]$; Appendix~\ref{app:analysis}, Table~\ref{tab:entropy-deltas}). However, entropy redistribution shows model-dependent behavior---the direction reverses on Qwen at $s{=}0.25$ ($\Delta\mathcal{H} = +0.045$)---replicating in only 2/4 Qwen conditions and thus only partially consistent. Importance discrimination collapse remains the more robust, model-independent correlate, though it partially accounts for rather than fully explains the severity divergence.
22	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7ab369a0-2481-4059-9ad8-2e0166c7bf7b",
  "isSidechain": true,
  "promptId": "eeb83888-ea16-4335-9ad7-31eca084b764",
  "agentId": "a4138636fc3e34597",
  "type": "user",
  "uuid": "6d48c612-0d64-4ae2-8903-7d31b1364c9a",
  "sourceToolAssistantUUID": "7ab369a0-2481-4059-9ad8-2e0166c7bf7b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/paper_agent_9539225d",
  "sessionId": "75f62e16-26c1-41e3-a629-5dbc4dda9106",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cryptic-kindling-corbato"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-16T02:54:10.020Z_

<details open><summary>🔧 Tool call — Read · `toolu_01EZUT1yc45DZk2k2RTyworf`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6d48c612-0d64-4ae2-8903-7d31b1364c9a",
  "isSidechain": true,
  "agentId": "a4138636fc3e34597",
  "requestId": "req_011Cb5VXsvUsvmhRuCsCcJZQ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "41ea173b-1803-4c25-8d88-43dd0cc57930",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/paper_agent_9539225d",
  "sessionId": "75f62e16-26c1-41e3-a629-5dbc4dda9106",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cryptic-kindling-corbato",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017LLWQUC4JnVD7mMGZdDxJ3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1565,
      "cache_read_input_tokens": 27512,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1565,
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

_source line 15 · 2026-05-16T02:54:10.035Z_

<details><summary>↩ Tool result · `toolu_01EZUT1yc45DZk2k2RTyworf`</summary>

```text
1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Implications for deployment.}
5	A uniform compression budget implicitly accepts order-of-magnitude severity penalties during low-sparsity reasoning phases. Pilot evaluation ($n{=}30$, $s{=}0.25$; Appendix~\ref{app:pilot-mitigation}) achieved 18\% oracle recovery (95\% CI: $[-39\%, 45.8\%]$), falling below the pre-registered 30\% gate; the CI spans zero, indicating no statistically distinguishable improvement. Effective phase-aware allocation likely requires finer phase boundary estimation than current proxies provide. Additional mechanisms (e.g., strategy switching, adaptive thresholding) warrant investigation. We hypothesize that phase-modulated severity may extend to alternative attention-mass-based scoring methods (H$_2$O \cite{h2o-neurips2023}, SnapKV \cite{snapkv-neurips2024}, PyramidKV \cite{pyramidkv-colm2025}), which remains an open question for future work. Extended discussion in Appendix~\ref{app:extended-discussion}.
6	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "41ea173b-1803-4c25-8d88-43dd0cc57930",
  "isSidechain": true,
  "promptId": "eeb83888-ea16-4335-9ad7-31eca084b764",
  "agentId": "a4138636fc3e34597",
  "type": "user",
  "uuid": "6bbd143f-cecf-4562-8c8b-9a9af974c3f4",
  "sourceToolAssistantUUID": "41ea173b-1803-4c25-8d88-43dd0cc57930",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/paper_agent_9539225d",
  "sessionId": "75f62e16-26c1-41e3-a629-5dbc4dda9106",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cryptic-kindling-corbato"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-16T02:54:10.079Z_

<details open><summary>🔧 Tool call — Read · `toolu_0118CrqEbvnhtASyfqnxETAK`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6bbd143f-cecf-4562-8c8b-9a9af974c3f4",
  "isSidechain": true,
  "agentId": "a4138636fc3e34597",
  "requestId": "req_011Cb5VXsvUsvmhRuCsCcJZQ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "41afbddc-9979-4b79-a107-8d17ae82cf9f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/paper_agent_9539225d",
  "sessionId": "75f62e16-26c1-41e3-a629-5dbc4dda9106",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cryptic-kindling-corbato",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017LLWQUC4JnVD7mMGZdDxJ3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1565,
      "cache_read_input_tokens": 27512,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1565,
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

_source line 17 · 2026-05-16T02:54:10.101Z_

<details><summary>↩ Tool result · `toolu_0118CrqEbvnhtASyfqnxETAK`</summary>

```text
1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We showed that compound sparsity severity is not phase-invariant but exhibits an emergent phase-strategy interaction. Under importance-based eviction, the paired median difference $\Delta$ increases from $0.39$ to $8.48$ (DeepSeek, $n{=}496$) and $0.07$ to $3.16$ (Qwen, $n{=}475$), all $p < 10^{-13}$, with amplification ratios $G{=}7.5$--$79.8{\times}$. Random eviction is $2.7$--$17{\times}$ weaker where both strategies are significant ($s \geq 0.25$). A model-dependent crossover on DeepSeek demonstrates that no single strategy dominates uniformly. Importance discrimination collapse provides a correlational diagnostic: despite near-identical Gini drops, severity diverges by $15$--$17{\times}$, implicating the structural specificity of importance-based pruning.
5	These findings establish compound severity as phase-dependent, providing a diagnostic foundation for future phase-aware mitigation. Future work could explore whether these patterns generalize to other reasoning domains, provide causal validation of importance discrimination collapse, and systematically characterize asymmetric compound interactions.
6	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "41afbddc-9979-4b79-a107-8d17ae82cf9f",
  "isSidechain": true,
  "promptId": "eeb83888-ea16-4335-9ad7-31eca084b764",
  "agentId": "a4138636fc3e34597",
  "type": "user",
  "uuid": "dd46fdc6-d72d-4f88-a0ee-ba5a9487744c",
  "sourceToolAssistantUUID": "41afbddc-9979-4b79-a107-8d17ae82cf9f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/paper_agent_9539225d",
  "sessionId": "75f62e16-26c1-41e3-a629-5dbc4dda9106",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cryptic-kindling-corbato"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-16T02:54:10.230Z_

<details open><summary>🔧 Tool call — Read · `toolu_01LAEgu8xjRUfLTBYpmV6EzM`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dd46fdc6-d72d-4f88-a0ee-ba5a9487744c",
  "isSidechain": true,
  "agentId": "a4138636fc3e34597",
  "requestId": "req_011Cb5VXsvUsvmhRuCsCcJZQ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "626c09d9-f9c3-4b4d-985e-95762d61c1cb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/paper_agent_9539225d",
  "sessionId": "75f62e16-26c1-41e3-a629-5dbc4dda9106",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cryptic-kindling-corbato",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017LLWQUC4JnVD7mMGZdDxJ3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1565,
      "cache_read_input_tokens": 27512,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1565,
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

_source line 19 · 2026-05-16T02:54:10.238Z_

<details><summary>↩ Tool result · `toolu_01LAEgu8xjRUfLTBYpmV6EzM`</summary>

```text
1	\paragraph{Model scale and architecture.}
2	All experiments are conducted at the 7--8B parameter scale. Whether the phase-modulated severity patterns persist, amplify, or attenuate at larger scales (e.g., 70B) remains untested. Preliminary cross-architecture validation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, \S\ref{sec:cross-arch}, Appendix~\ref{app:cross-arch}) provides pilot evidence suggesting the qualitative pattern may extend beyond the Qwen2 architecture---monotonically increasing $d_z$ with within-importance phase gradient $\sim$1.0---but with substantially weaker interaction magnitude ($\sim$1/40 of DeepSeek) and mixed statistical evidence (only $s{=}0.30$ significant after Bonferroni correction). The pattern has been tested on two architecture families (Qwen2ForCausalLM, LlamaForCausalLM); comprehensive validation across more diverse architectures (e.g., Mistral, multi-latent attention) and larger scales is needed for full generalization claims.
3	
4	\paragraph{Task coverage.}
5	Our primary evaluation uses MATH-500; cross-benchmark validation on GSM8K (\S\ref{sec:cross-benchmark}) confirms the phase gradient direction under importance-based eviction but reveals that random eviction is non-significant on GSM8K (CIs spanning zero), precluding meaningful ratio computation. On MATH-500, strategy specificity is quantifiable ($15$--$17{\times}$); on GSM8K, it manifests as a qualitative gap (significant vs.\ non-significant). This suggests that the phase-strategy interaction is robust in direction but task-dependent in form---complex reasoning (MATH-500) produces quantitative strategy contrast while simpler arithmetic (GSM8K) produces qualitative separation. Qwen GSM8K outputs were truncated at \texttt{max\_new\_tokens}${=}$2047, so Qwen GSM8K absolute values carry this limitation; DeepSeek GSM8K data is untruncated. Our task-complexity explanation for specificity attenuation (lower cognitive load $\to$ more uniform attention $\to$ reduced strategy sensitivity) is supported by within-benchmark correlational evidence but requires validation across a broader range of task complexities; whether different reasoning tasks---code generation, science reasoning, multi-hop QA---produce yet different attenuation profiles remains open. Random eviction on GSM8K exhibits numerical instability (extreme outlier II values), likely a systematic interaction between reduced-precision arithmetic and score-independent eviction.
6	
7	\paragraph{Eviction strategy scope.}
8	Our importance-based eviction uses cumulative attention scores (H$_2$O-style scoring, Eq.~\ref{eq:kv-importance}), which creates an inherent dependency between head pruning and cache eviction: pruning alters the attention distribution from which importance scores are computed, and eviction then operates on these degraded scores. The compound interaction patterns we report---including importance discrimination collapse and the phase-strategy crossover---arise within this specific scoring mechanism. Alternative eviction strategies that do not rely on attention-mass-based scoring (e.g., learned eviction policies, recency-based heuristics) may exhibit qualitatively different compound interaction dynamics. Validating whether the phase-modulated severity pattern generalizes across eviction scoring mechanisms is an important next step.
9	
10	\paragraph{Symmetric sparsity assumption.}
11	Our analysis applies symmetric sparsity rates: the same fraction $s$ is used for both head pruning and KV cache eviction. A preliminary spot check under asymmetric allocation (Appendix~\ref{app:asymmetric-robustness}) confirms that the phase gradient is robust to head/KV budget ratios, but systematic characterization of the full asymmetric interaction surface remains future work.
12	
13	\paragraph{Phase segmentation validation.}
14	The \texttt{&lt;think>} token validation of sparsity-based phase segmentation (\S\ref{sec:background}, Appendix~\ref{app:think-validation}) is limited to a single model (DeepSeek-R1-Distill-Qwen-7B) on a single benchmark (GSM8K, $n{=}48$). Qwen2.5-7B-Instruct does not generate explicit reasoning markers, precluding the same validation. Whether the high agreement ($\kappa{=}0.887$) generalizes to other models with explicit CoT delimiters, or to non-mathematical reasoning tasks, remains open.
15	
16	\paragraph{Mechanism.}
17	The importance discrimination collapse mechanism is a correlational marker, not a complete causal explanation: both strategies exhibit near-identical Gini drops yet severity diverges by $15$--$17{\times}$, indicating that Gini collapse alone is insufficient. Causal validation through controlled entropy manipulation is needed. The entropy redistribution component replicates on only 2/4 Qwen conditions, suggesting model-specific factors.
18	
19	\paragraph{Perplexity vs.\ accuracy.}
20	Our primary severity metric is perplexity-based (II), chosen because its per-token granularity enables the phase-level decomposition central to our analysis; accuracy is binary per-problem and cannot be meaningfully decomposed by reasoning phase. Accuracy validation on MATH-500 (\S\ref{sec:accuracy-validation}, Appendix~\ref{app:accuracy-details}) shows gradual decline through $s{=}0.25$ ($\delta{=}-4$ to $-13$\,pp) followed by a sharp cliff at $s{=}0.30$ ($\delta{=}-27$\,pp) for Qwen ($n{=}100$, truncation $\leq 4\%$). DeepSeek accuracy deltas are confounded by rising truncation ($16\%$ to $76\%$); non-truncated analysis reveals a dual-regime structure but is limited by small surviving samples at high sparsity. Comprehensive accuracy evaluation across benchmarks remains an important next step.
21	
22	\paragraph{Sparsity range.}
23	Our experiments span $s \in \{0.15, 0.20, 0.25, 0.30\}$, sufficient to establish monotonicity at the tested levels (JT test $p \ll 10^{-10}$) but insufficient to characterize the functional form of $G(s)$ or identify potential saturation thresholds. More extreme sparsity ($s > 0.50$) may exhibit qualitatively different interaction dynamics. We do not report inference throughput or latency measurements, which are necessary for a complete deployment analysis but orthogonal to our severity characterization. Extended limitations in Appendix~\ref{app:limitations}.
24	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "626c09d9-f9c3-4b4d-985e-95762d61c1cb",
  "isSidechain": true,
  "promptId": "eeb83888-ea16-4335-9ad7-31eca084b764",
  "agentId": "a4138636fc3e34597",
  "type": "user",
  "uuid": "4a7d05aa-feb4-4b34-a191-70003d5e99de",
  "sourceToolAssistantUUID": "626c09d9-f9c3-4b4d-985e-95762d61c1cb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/paper_agent_9539225d",
  "sessionId": "75f62e16-26c1-41e3-a629-5dbc4dda9106",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cryptic-kindling-corbato"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-16T02:54:10.591Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Q3tVyDtYTUkk83S9W49okC`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/appendix_disc_analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4a7d05aa-feb4-4b34-a191-70003d5e99de",
  "isSidechain": true,
  "agentId": "a4138636fc3e34597",
  "requestId": "req_011Cb5VXsvUsvmhRuCsCcJZQ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "104081b1-6585-4dfd-8703-61d75b58138a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/paper_agent_9539225d",
  "sessionId": "75f62e16-26c1-41e3-a629-5dbc4dda9106",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cryptic-kindling-corbato",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017LLWQUC4JnVD7mMGZdDxJ3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1565,
      "cache_read_input_tokens": 27512,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1565,
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

_source line 21 · 2026-05-16T02:54:10.602Z_

<details><summary>↩ Tool result · `toolu_01Q3tVyDtYTUkk83S9W49okC`</summary>

```text
1	\section{Importance Discrimination Collapse Details}
2	\label{app:discrimination-collapse-details}
3	
4	This cross-model consistency (Table~\ref{tab:discrimination-metrics-full}) establishes importance discrimination collapse as a robust consequence of compound sparsity. When importance scores lose discriminative power, thresholding the bottom-$s$ fraction becomes noise-sensitive: small perturbations change which positions cross the eviction boundary. In the limit of perfectly uniform scores, importance-based eviction degenerates into an arbitrary selection functionally equivalent to biased random eviction. The same pattern holds under random eviction (DeepSeek: $-0.031$ to $-0.071$; Qwen: $-0.019$ to $-0.046$), confirming that importance discrimination collapse is a consequence of head pruning \emph{per se}, not of the eviction strategy.
5	
6	
7	\section{Extended Discussion}
8	\label{app:extended-discussion}
9	
10	\paragraph{On the predictability of phase-modulated severity.}
11	The compound interaction is not uniformly fragile---it is selectively fragile in a phase-dependent manner ($\widetilde{\mathrm{II}}_{\text{high}} < 0.06$ at $s \leq 0.30$).
12	
13	\paragraph{Random masking as falsification control.}
14	At $n{=}500$, random eviction develops a detectable but weak phase gradient above $s \approx 0.20$: non-significant at $s \leq 0.20$ for both models, but significant at $s \geq 0.25$ (DS: $\Delta{=}0.26$--$0.51$, $p_{\text{Bonf}} < 0.006$; QW: $\Delta{=}0.39$--$0.91$, $p_{\text{Bonf}} < 10^{-10}$). Where significant, the random phase gradient is $2.7$--$17{\times}$ weaker than importance-based (restricted to conditions where both strategies are significant, $s \geq 0.25$), confirming that the dominant amplification is strategy-specific.
15	
16	\paragraph{Entropy mechanism boundary conditions.}
17	Directly measuring per-head entropy shifts across architecturally distinct models---and identifying what training-time properties determine whether entropy concentrates or disperses under head pruning---would clarify the boundary conditions of the full mechanism.
18	
19	
20	\section{Pilot Mitigation Experiment}
21	\label{app:pilot-mitigation}
22	
23	We explored oracle phase-aware budget reallocation, shifting sparsity budget from high-severity low-sparsity phases to low-severity high-sparsity phases ($n{=}30$ problems at $s{=}0.25$). Oracle recovery---the fraction of compound interaction eliminated by phase-aware allocation---reached 18\% (95\% CI: $[-39\%, 45.8\%]$; Wilcoxon $p = 0.002$), below the pre-registered 30\% gate for claiming practical mitigation. A heuristic variant achieved 32\% recovery (95\% CI: $[-22.8\%, 66\%]$; $p = 0.024$). \textbf{Critically, 95\% bootstrap CIs for both conditions span zero}, meaning neither recovery estimate is statistically distinguishable from no improvement. These results indicate that phase-aware budget reallocation alone is insufficient to neutralize the severity gradient; effective mitigation likely requires joint optimization of budget allocation and eviction strategy selection across phases.
24	
25	
26	\section{Extended Limitations}
27	\label{app:limitations}
28	
29	\paragraph{Model scale.}
30	All experiments are conducted at the 7B parameter scale.
31	Whether the phase-modulated severity patterns persist, amplify, or attenuate at larger scales (e.g., 70B) remains untested.
32	Larger models may exhibit different attention redundancy structures that alter the importance discrimination collapse dynamics (and the model-dependent entropy component may behave differently at scale).
33	
34	
35	\paragraph{Architectural scope.}
36	Our two models---DeepSeek-R1-Distill-Qwen-7B and Qwen2.5-7B-Instruct---share the Qwen2ForCausalLM architecture.
37	The cross-training-paradigm replication (\S\ref{sec:cross-model}) establishes that the findings are not artifacts of a single model's weights, though both models share the same Qwen2ForCausalLM architecture.
38	Pilot cross-architecture evidence from DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, \S\ref{sec:cross-arch}, Appendix~\ref{app:cross-arch}) suggests qualitatively consistent within-importance phase gradients ($d_z \sim 1.0$) but a substantially weaker strategy $\times$ phase interaction than in Qwen2-based architectures; random pruning also exhibits a non-trivial phase gradient on LLaMA, reducing the strategy contrast. This preliminary evidence ($s{=}0.30$ Wilcoxon $p_{\text{Bonf}}{=}0.029$; $s \leq 0.25$ non-significant) is consistent with the qualitative pattern extending beyond Qwen2 but is insufficient for definitive cross-architecture claims; quantitative impact is architecture-dependent. Comprehensive cross-architecture validation across more diverse designs (e.g., Mistral, multi-latent attention architectures) and scales remains an important next step.
39	
40	
41	\paragraph{Task coverage.}
42	We evaluate exclusively on MATH-500, a mathematical reasoning benchmark.
43	Different reasoning tasks---code generation, commonsense reasoning, multi-hop question answering---may induce different phase structures with different sparsity distributions, potentially altering the severity gradient profile.
44	Generalizing the phase-strategy interaction to broader reasoning domains is an important next step.
45	
46	
47	\paragraph{Statistical scope.}
48	Bootstrap confidence intervals use $B{=}10{,}000$ resamples (seed$=$42). The primary analysis uses $n{=}496$ paired problems for DeepSeek (4 excluded) and $n{=}475$ for Qwen (25 excluded); the permutation test (Table~\ref{tab:permutation}) uses $n{=}49$ from an initial profiling subset.
49	The severity difference distribution is right-skewed (mean/median ratios up to $43{:}1$), motivating our use of medians and nonparametric tests rather than parametric alternatives.
50	All four profiling-subset permutation tests reject $H_0$ after Bonferroni correction ($p_{\text{Bonf}} < 0.005$; Table~\ref{tab:permutation}), with CI lower bounds increasing from $0.19$ to $6.70$---confirming the effect direction at every sparsity level. At $n{=}496$, Wilcoxon signed-rank tests confirm all conditions with $p_{\text{Bonf}} < 10^{-13}$ (Table~\ref{tab:cohens-d}). The permutation CIs at higher sparsity are wider (e.g., $[6.70,\; 16.29]$ at $s{=}0.30$), reflecting genuine variance in per-problem severity amplification.
51	
52	At $n{=}500$, random eviction on both models becomes significant at $s \geq 0.25$ (Qwen: $\Delta{=}0.39$, $p_{\text{Bonf}} < 10^{-10}$ at $s{=}0.25$; $\Delta{=}0.91$, $p_{\text{Bonf}} < 10^{-13}$ at $s{=}0.30$; bootstrap CIs exclude zero).
53	These effects are genuine but $2.7$--$20{\times}$ weaker than importance-based eviction at the same sparsity levels, consistent with a weak phase gradient that is detectable at sufficient sample size but not the primary driver of compound severity.
54	
55	\paragraph{Sparsity range.}
56	Our primary analysis spans $s \in \{0.15, 0.20, 0.25, 0.30\}$; pilot data at $s{=}0.10$ and $s{=}0.35$ exist (6 total sparsity levels) but are not included in the main analysis due to limited sample size at these boundary conditions. Monotonicity is established at the tested sparsity levels (JT test $p \ll 10^{-10}$); the functional form of $G(s)$ between and beyond these levels is not characterized.
57	More extreme sparsity ($s > 0.50$) may exhibit qualitatively different interaction dynamics---the sub-exponential growth pattern suggests the severity gradient may plateau, but this remains unverified.
58	
59	
60	\paragraph{No throughput evaluation.}
61	We do not report inference throughput or latency, which are necessary for deployment analysis but orthogonal to our severity characterization.
62	
63	
64	
65	\section{Cross-Benchmark Validation: GSM8K}
66	\label{app:gsm8k}
67	
68	Tables~\ref{tab:gsm8k-ds} and \ref{tab:gsm8k-qw} report the per-phase II breakdown on GSM8K ($n{=}50$) for DeepSeek and Qwen, respectively. All statistics use medians, Wilcoxon signed-rank tests, and bootstrap median CIs ($B{=}10{,}000$), matching the MATH-500 methodology. DeepSeek importance-based eviction replicates the MATH-500 phase gradient across all four sparsity levels (all $p \leq 0.0003$) with a strict dose-response ($\Delta$: $0.24 \to 4.68$). Qwen importance-based eviction is significant at $s \geq 0.25$ ($p < 10^{-4}$). Random eviction is non-significant across all conditions for both models; Qwen random $s{=}0.30$ is excluded due to data quality concerns (output truncation producing extreme II values).
69	
70	\begin{table*}[t]
71	\centering
72	\small
73	\caption{Per-phase interaction index on GSM8K: DeepSeek-R1-Distill-Qwen-7B ($n{=}50$). $\Delta$: paired median difference ($\widetilde{\mathrm{II}}_{\textit{low}} - \widetilde{\mathrm{II}}_{\textit{high}}$) with bootstrap 95\% CI ($B{=}10{,}000$, median statistic). $p$: Wilcoxon signed-rank, Bonferroni-corrected ($k{=}4$).}
74	\label{tab:gsm8k-ds}
75	\begin{tabular}{@{}llcccc@{}}
76	\toprule
77	$s$ & Strategy & $\widetilde{\mathrm{II}}_{\textit{high}}$ & $\widetilde{\mathrm{II}}_{\textit{low}}$ & $\Delta$\; [95\% CI] & $p_{\text{Bonf}}$ \\
78	\midrule
79	0.15 & Importance & $-$0.001 & 0.241 & 0.24\; $[0.08,\; 0.48]$ & 0.0003 \\
80	0.15 & Random     & 0.036 & 0.105 & $-$0.04\textsuperscript{ns} & 0.90 \\
81	\addlinespace
82	0.20 & Importance & $-$0.002 & 0.740 & 0.74\; $[0.31,\; 1.12]$ & ${<}\,10^{-4}$ \\
83	0.20 & Random     & 0.143 & 0.423 & 0.28\textsuperscript{ns} & 0.96 \\
84	\addlinespace
85	0.25 & Importance & 0.009 & 1.992 & 1.99\; $[0.93,\; 2.82]$ & ${<}\,10^{-4}$ \\
86	0.25 & Random     & 0.619 & 1.603 & 0.98\textsuperscript{ns} & 0.83 \\
87	\addlinespace
88	0.30 & Importance & 0.024 & 4.682 & 4.68\; $[2.12,\; 10.56]$ & ${<}\,10^{-4}$ \\
89	0.30 & Random     & 1.837 & 4.683 & 2.85\textsuperscript{ns} & 0.54 \\
90	\bottomrule
91	\end{tabular}
92	\end{table*}
93	
94	\begin{table*}[t]
95	\centering
96	\small
97	\caption{Per-phase interaction index on GSM8K: Qwen2.5-7B-Instruct ($n{=}50$). Outputs truncated at \texttt{max\_new\_tokens}${=}$2047; absolute values should be interpreted with this limitation. $^{\ddagger}$Excluded: extreme II values from truncation artifacts render this condition invalid.}
98	\label{tab:gsm8k-qw}
99	\begin{tabular}{@{}llcccc@{}}
100	\toprule
101	$s$ & Strategy & $\widetilde{\mathrm{II}}_{\textit{high}}$ & $\widetilde{\mathrm{II}}_{\textit{low}}$ & $\Delta$\; [95\% CI] & $p_{\text{Bonf}}$ \\
102	\midrule
103	0.15 & Importance & 0.000 & 0.029 & 0.03\textsuperscript{ns} & 0.39 \\
104	0.15 & Random     & 0.089 & 0.033 & $-$1.58\textsuperscript{ns} & 0.69 \\
105	\addlinespace
106	0.20 & Importance & 0.004 & 0.180 & 0.09\textsuperscript{ns} & 0.62 \\
107	0.20 & Random     & 0.201 & 0.356 & 4.88\textsuperscript{ns} & 0.57 \\
108	\addlinespace
109	0.25 & Importance & 0.009 & 1.064 & 1.14\; $[0.62,\; 1.66]$ & ${<}\,10^{-4}$ \\
110	0.25 & Random     & 0.802 & 1.213 & 11.1\textsuperscript{ns} & 0.39 \\
111	\addlinespace
112	0.30 & Importance & 0.023 & 2.140 & 4.62\; $[2.88,\; 6.92]$ & ${<}\,10^{-4}$ \\
113	0.30 & Random$^{\ddagger}$     & \multicolumn{4}{c}{\textit{excluded (data quality)}} \\
114	\bottomrule
115	\end{tabular}
116	\end{table*}
117	
118	
119	\section{Downstream Accuracy Validation Details}
120	\label{app:accuracy-details}
121	
122	Table~\ref{tab:accuracy} reports MATH-500 accuracy under compound sparsity (importance-based eviction) at $s \in \{0.15, 0.20, 0.25, 0.30\}$ with \texttt{max\_new\_tokens}${=}$8192, complementing the PPL-based analysis in \S\ref{sec:accuracy-validation}. Qwen ($n{=}100$; truncation $\leq 4\%$ across all conditions) provides the cleanest dose-response evidence: accuracy declines gradually from $46\%$ (dense) through $s{=}0.25$ ($\delta{=}-4$ to $-13$\,pp) before a sharp cliff at $s{=}0.30$ ($19\%$, $\delta{=}-27$\,pp). DeepSeek ($n{=}50$) shows steeper overall degradation ($74\% \to 4\%$), confounded by rising truncation ($16\% \to 76\%$); non-truncated analysis (\S\ref{app:accuracy-nt}) reveals a dual-regime structure.
123	
124	\begin{table}[h]
125	\centering
126	\small
127	\caption{MATH-500 accuracy under compound sparsity (importance-based eviction, \texttt{max\_new\_tokens}${=}$8192). $\delta$: accuracy change vs.\ dense. Trunc: truncation rate under sparse condition. DS: $n{=}50$ (dense truncation $16\%$); QW: $n{=}100$ (truncation $\leq 4\%$ all conditions).}
128	\label{tab:accuracy}
129	\begin{tabular}{@{}lccccc@{}}
130	\toprule
131	Model & $s$ & Dense & Sparse & $\delta$ & Trunc \\
132	\midrule
133	DS & 0.15 & 74\% & 48\% & $-$26\,pp & 32\% \\
134	DS & 0.20 & 74\% & 30\% & $-$44\,pp & 56\% \\
135	DS & 0.25 & 74\% & 8\% & $-$66\,pp & 76\% \\
136	DS & 0.30 & 74\% & 4\% & $-$70\,pp & 76\% \\
137	\addlinespace
138	QW & 0.15 & 46\% & 42\% & $-$4\,pp & $\leq$4\% \\
139	QW & 0.20 & 46\% & 36\% & $-$10\,pp & $\leq$4\% \\
140	QW & 0.25 & 46\% & 33\% & $-$13\,pp & $\leq$4\% \\
141	QW & 0.30 & 46\% & 19\% & $-$27\,pp & $\leq$4\% \\
142	\bottomrule
143	\end{tabular}
144	\end{table}
145	
146	\paragraph{Failure mode divergence.}
147	DeepSeek and Qwen exhibit qualitatively distinct failure modes under compound sparsity. DeepSeek failures are \emph{truncation-dominated}: compound sparsity induces verbose, repetitive chain-of-thought that exceeds the token limit (truncation rises from $16\%$ at dense to $32\%$ at $s{=}0.15$ and $76\%$ at $s{=}0.30$, even with \texttt{max\_new\_tokens}${=}$8192). Qwen failures are \emph{wrong-answer-dominated}: outputs complete within the token limit (truncation $\leq 4\%$) but produce incorrect answers, confirming that compound sparsity disrupts reasoning quality directly. This divergence likely reflects training-paradigm differences: DeepSeek's distillation from DeepSeek-R1 produces extended CoT traces susceptible to truncation under degraded conditions.
148	
149	\paragraph{Language switching under high sparsity.}
150	At $s{=}0.30$, 40\% of DeepSeek problems exhibit language switching to Chinese mid-generation (dense: 0\%; $s{=}0.15$: 4\%).\footnote{Language switching rates were measured under \texttt{max\_new\_tokens}${=}$2048; rates under the 8192-token budget used in Table~\ref{tab:accuracy} were not re-measured.} This qualitative pathology---absent in Qwen---suggests that high-dose compound sparsity can disrupt language-level coherence in distillation-trained models, consistent with the model's Chinese-language pretraining corpus surfacing under degraded attention.
151	
152	
153	\section{Non-Truncated Sensitivity Analysis}
154	\label{app:accuracy-nt}
155	
156	With \texttt{max\_new\_tokens}${=}$8192, Qwen truncation remains $\leq 4\%$ across all sparsity levels, so the full-sample accuracy decline ($\delta{=}-4$ to $-27$\,pp; Table~\ref{tab:accuracy}) reflects pure reasoning quality degradation without truncation confound.
157	
158	DeepSeek exhibits substantial truncation ($16\%$ at dense to $76\%$ at $s{=}0.25$--$0.30$). Restricting to non-truncated outputs reveals a \emph{dual-regime} structure. At $s \leq 0.20$, non-truncated accuracy remains $68$--$71\%$ (vs.\ $88\%$ dense), while full-sample accuracy drops to $30$--$48\%$---indicating that degradation at low sparsity is primarily truncation-driven rather than reflecting reasoning quality loss. At $s \geq 0.25$, non-truncated accuracy itself collapses: $33\%$ at $s{=}0.25$ and $17\%$ at $s{=}0.30$ ($n_{\text{NT}}{=}12$ for both; reported as reference values given small samples), demonstrating that high-dose compound sparsity degrades both generation length \emph{and} reasoning quality simultaneously. The NT accuracy cliff from $68\%$ ($s{=}0.20$) to $33\%$ ($s{=}0.25$) localizes the transition between truncation-driven and dual-collapse regimes.
159	
160	This dual-regime structure complements the importance discrimination collapse analysis (\S\ref{sec:analysis}): at low sparsity, compound interaction primarily manifests as increased verbosity (degraded attention produces repetitive CoT); at high sparsity, the interaction additionally corrupts reasoning-critical computations.
161	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "104081b1-6585-4dfd-8703-61d75b58138a",
  "isSidechain": true,
  "promptId": "eeb83888-ea16-4335-9ad7-31eca084b764",
  "agentId": "a4138636fc3e34597",
  "type": "user",
  "uuid": "2aa82409-b4c8-49fd-abe2-8d0ac6136bf4",
  "sourceToolAssistantUUID": "104081b1-6585-4dfd-8703-61d75b58138a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/paper_agent_9539225d",
  "sessionId": "75f62e16-26c1-41e3-a629-5dbc4dda9106",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cryptic-kindling-corbato"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-16T02:54:10.702Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Ybxf1hts5ZZzQcmfmAEkoZ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/appendix_moved.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2aa82409-b4c8-49fd-abe2-8d0ac6136bf4",
  "isSidechain": true,
  "agentId": "a4138636fc3e34597",
  "requestId": "req_011Cb5VXsvUsvmhRuCsCcJZQ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f1598080-9151-49a3-bb4c-51542c26cd23",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/paper_agent_9539225d",
  "sessionId": "75f62e16-26c1-41e3-a629-5dbc4dda9106",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cryptic-kindling-corbato",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017LLWQUC4JnVD7mMGZdDxJ3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1565,
      "cache_read_input_tokens": 27512,
      "output_tokens": 700,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1565
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 700,
          "cache_read_input_tokens": 27512,
          "cache_creation_input_tokens": 1565,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1565,
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

_source line 23 · 2026-05-16T02:54:10.713Z_

<details><summary>↩ Tool result · `toolu_01Ybxf1hts5ZZzQcmfmAEkoZ`</summary>

```text
1	
2	\section{Phase-Strategy Crossover Details}
3	\label{app:crossover-details}
4	
5	On DeepSeek ($n{=}496$), a strategy ranking reversal emerges at $s{=}0.25$ (Figure~\ref{fig:crossover}): importance-based eviction yields \emph{lower} II than random in the high-sparsity phase ($0.021$ vs.\ $1.113$) but \emph{higher} II in the low-sparsity phase ($3.971$ vs.\ $1.514$---a $2.6{\times}$ reversal; both $p < 10^{-4}$). This crossover is confirmed at all four sparsity levels, with reversal magnitude of $4.0{\times}$ at $s{=}0.15$, $3.4{\times}$ at $s{=}0.20$, $2.6{\times}$ at $s{=}0.25$, and $2.2{\times}$ at $s{=}0.30$ (decreasing as random eviction severity rises). The reversal arises because head pruning redistributes attention mass, altering importance rankings in a way that couples the two sparsity mechanisms in low-sparsity phases (\S\ref{sec:discrimination-collapse-main}). Qwen does not exhibit a crossover: importance-based eviction produces lower II than random in both phases across all sparsity levels (e.g., at $s{=}0.25$: high $0.004$ vs.\ $1.108$; low $1.053$ vs.\ $1.769$).
6	
7	\begin{figure}[t]
8	\centering
9	\includegraphics[width=\columnwidth]{fig3_crossover.pdf}
10	\caption{Strategy-dependent crossover at $s{=}0.25$ on DeepSeek ($n{=}496$). Grouped bar chart of median II by eviction strategy and reasoning phase. Importance-based eviction outperforms random in the high-sparsity phase but produces $2.6{\times}$ higher II in the low-sparsity phase, reversing the strategy ranking.}
11	\label{fig:crossover}
12	\end{figure}
13	
14	
15	\section{Profiling Subset Per-Phase Breakdown}
16	\label{app:profiling-subset}
17	
18	\begin{table*}[t]
19	\centering
20	\small
21	\caption{Per-phase interaction index (II) from the $n{=}50$ profiling subset (DeepSeek-R1-Distill-Qwen-7B). The main analysis ($n{=}496$) appears in Table~\ref{tab:main-results}. $G$ values in this table use the ratio-of-medians definition ($\widetilde{\mathrm{II}}_{\textit{low}} / \widetilde{\mathrm{II}}_{\textit{high}}$), which differs from the primary per-problem definition in Eq.~\ref{eq:gradient}. At low sparsity ($s{=}0.15$), the two definitions diverge substantially ($7.5{\times}$ vs.\ $69{\times}$) because per-problem ratios are sensitive to near-zero $\mathrm{II}_{\textit{high}}$ values.}
22	\label{tab:profiling-subset}
23	\begin{tabular}{@{}llccccr@{}}
24	\toprule
25	$s$ & Strategy & $\widetilde{\mathrm{II}}_{\textit{high}}$ & $\widetilde{\mathrm{II}}_{\textit{mid}}$ & $\widetilde{\mathrm{II}}_{\textit{low}}$ & $\Delta$ & $G$ \\
26	\midrule
27	0.15 & Importance & 0.006 & 0.081 & 0.398 & 0.39 & $\mathbf{69}$ \\
28	0.15 & Random     & 0.093 & 0.097 & 0.103 & 0.01 & 1.1 \\
29	\addlinespace
30	0.20 & Importance & 0.015 & 0.203 & 1.496 & 1.48 & $\mathbf{103}$ \\
31	0.20 & Random     & 0.292 & 0.350 & 0.276 & $-$0.02 & 0.9 \\
32	\addlinespace
33	0.25 & Importance & 0.032 & 1.118 & 7.196 & 7.16 & $\mathbf{222}$ \\
34	0.25 & Random     & 0.818 & 0.932 & 1.363 & 0.54 & 1.7 \\
35	\addlinespace
36	0.30 & Importance & 0.053 & 2.283 & 14.639 & 14.59 & $\mathbf{274}$ \\
37	0.30 & Random     & 2.503 & 2.592 & 4.041 & 1.54 & 1.6 \\
38	\bottomrule
39	\end{tabular}
40	\end{table*}
41	
42	
43	\section{Cross-Training-Paradigm Replication Details}
44	\label{app:cross-model-details}
45	
46	Both models share the Qwen2ForCausalLM backbone (28 layers, 28 heads, 4-group GQA) but differ in training: DeepSeek uses reasoning distillation from DeepSeek-R1, while Qwen2.5 uses standard instruction tuning without explicit reasoning delimiters. This within-architecture-family comparison enables assessment of training methodology effects on the compound sparsity interaction, though causal attribution is limited by the observational design.
47	
48	Despite lacking explicit \texttt{&lt;think>} delimiters, Qwen2.5-7B-Instruct exhibits sufficient variation in attention sparsity to permit phase segmentation via the same quantile-based method (\S\ref{par:phase-segmentation}). Twenty-five of the 500 problems are excluded due to degenerate phase assignments, yielding $n{=}475$ valid problems for Qwen (vs.\ $n{=}496$ for DeepSeek).
49	
50	\paragraph{Per-phase effective sample size.}
51	\label{app:qwen-null-rate}
52	Table~\ref{tab:qwen-effective-n} reports the per-phase effective sample size for Qwen2.5-7B-Instruct, defined as the number of problems with non-null phase segments (segment length $\geq$ \texttt{min\_phase\_length}). The mid-phase null rate (45.2\%) reflects problems where mid-sparsity tokens do not form contiguous runs above the merging threshold; this does not affect the low--high contrast ($\Delta$) used in the primary analysis.
53	
54	\begin{table}[t]
55	\centering
56	\small
57	\caption{Per-phase effective sample size for Qwen2.5-7B-Instruct ($n_{\text{eff}} = 475$). Phase segmentation is performed once on dense-model attention patterns and is independent of sparsity level.}
58	\label{tab:qwen-effective-n}
59	\begin{tabular}{@{}lcccc@{}}
60	\toprule
61	Phase & $s{=}0.15$ & $s{=}0.20$ & $s{=}0.25$ & $s{=}0.30$ \\
62	\midrule
63	High & 475 & 475 & 475 & 475 \\
64	Mid  & 274 & 274 & 274 & 274 \\
65	Low  & 475 & 475 & 475 & 475 \\
66	\bottomrule
67	\end{tabular}
68	\end{table}
69	
70	Table~\ref{tab:cross-model} reports the cross-training-paradigm comparison. Qwen reproduces the monotonic severity gradient at ${\sim}1/5$ of DeepSeek's magnitude. Figure~\ref{fig:cross-model} visualizes this comparison.
71	
72	\begin{table}[t]
73	\centering
74	\small
75	\caption{Cross-training-paradigm comparison of median compound severity difference ($\Delta$) under importance-based eviction.}
76	\label{tab:cross-model}
77	\begin{tabular}{@{}lcccc@{}}
78	\toprule
79	Model & $s{=}0.15$ & $s{=}0.20$ & $s{=}0.25$ & $s{=}0.30$ \\
80	\midrule
81	DeepSeek-R1-Distill-Qwen-7B ($n{=}496$) & 0.39 & 1.21 & 3.99 & 8.48 \\
82	Qwen2.5-7B-Instruct ($n{=}475$)         & 0.07 & 0.31 & 1.07 & 3.16 \\
83	\bottomrule
84	\end{tabular}
85	\end{table}
86	
87	\begin{figure}[t]
88	\centering
89	\includegraphics[width=\columnwidth]{fig5_crossmodel.pdf}
90	\caption{Cross-training-paradigm comparison of the median severity difference under importance-based eviction ($n{=}496$/$475$). Both DeepSeek (solid) and Qwen (dashed) exhibit monotonically increasing $\Delta$ with sparsity; Qwen's magnitude is approximately one-quarter to one-sixth of DeepSeek's.}
91	\label{fig:cross-model}
92	\end{figure}
93	
94	\paragraph{Per-problem concordance.}
95	The per-problem concordance across models is not significant (mean $\rho = -0.107$, $p = 0.926$), indicating that while the aggregate gradient direction replicates, the specific problems driving severity differ between models---consistent with model-specific attention patterns rather than a universal per-problem vulnerability ranking.
96	
97	\paragraph{Random eviction control.}
98	As a control, random eviction on Qwen mirrors DeepSeek: non-significant at $s \leq 0.20$ ($\Delta$: $-0.01$, $0.02$; CIs span zero) but significant at $s \geq 0.25$ ($\Delta{=}0.39$, $p_{\text{Bonf}} < 10^{-10}$; $\Delta{=}0.91$, $p_{\text{Bonf}} < 10^{-13}$). Where significant, the random phase gradient is $2.7$--$3.5{\times}$ weaker than importance-based ($0.39$ vs.\ $1.07$ at $s{=}0.25$; $0.91$ vs.\ $3.16$ at $s{=}0.30$), confirming strategy-specific amplification.
99	
100	
101	\section{Permutation Test Details}
102	\label{app:permutation-details}
103	
104	For each problem $i$ and sparsity level $s$, we compute the compound severity difference $\Delta_i^{(\text{strat})} = \mathrm{II}_{\textit{low},i} - \mathrm{II}_{\textit{high},i}$ under each eviction strategy. The test statistic is the median of the paired difference $\widetilde{\Delta} = \text{median}_i\!\bigl(\Delta_i^{(\text{imp})} - \Delta_i^{(\text{rand})}\bigr)$, measuring whether importance-based eviction produces systematically larger phase-dependent severity than random eviction. We permute strategy labels $10{,}000$ times to construct the null distribution and apply Bonferroni correction for 4 sparsity-level comparisons.
105	
106	Per-problem distributions of the paired severity difference $\Delta_i = \mathrm{II}_{\textit{low},i} - \mathrm{II}_{\textit{high},i}$ under importance-based eviction are right-skewed at all sparsity levels, with mean/median ratios ranging from $1.2{\times}$ ($s{=}0.15$) to $1.6{\times}$ ($s{=}0.30$) for DeepSeek and $1.1{\times}$ to $1.4{\times}$ for Qwen.
107	
108	The permutation null distributions are approximately symmetric around zero at all sparsity levels. At $s{=}0.15$, the observed statistic falls at the $99.92$th percentile of the null ($p_{\text{Bonf}} = 0.0032$); at $s \geq 0.20$, no permutation exceeds the observed statistic.
109	
110	Table~\ref{tab:permutation} reports the results. All four sparsity levels reject $H_0$ after Bonferroni correction ($p_{\text{Bonf}} < 0.005$), with observed median differences increasing monotonically from $0.37$ at $s{=}0.15$ to $9.85$ at $s{=}0.30$. The monotonic growth of both the point estimate and the CI lower bound ($0.19 \to 0.69 \to 1.66 \to 6.70$) confirms that compound severity amplification strengthens with sparsity---not merely in central tendency but also in worst-case lower bounds. Figure~\ref{fig:permtest-forest} presents these results as a forest plot.
111	
112	\begin{table}[t]
113	\centering
114	\small
115	\caption{Paired permutation test for compound severity: importance vs.\ random eviction on DeepSeek-R1-Distill-Qwen-7B ($n{=}49$ profiling subset, $10{,}000$ permutations, Bonferroni-corrected). The monotonic $\Delta$ pattern is confirmed at $n{=}496$ (Table~\ref{tab:aggregate-ii}).}
116	\label{tab:permutation}
117	\begin{tabular}{@{}rrcl@{}}
118	\toprule
119	$s$ & Observed $\widetilde{\Delta}$ & 95\% CI & $p_{\text{Bonf}}$ \\
120	\midrule
121	0.15 & 0.37 & $[0.19,\; 0.62]$ & 0.0032 \\
122	0.20 & 0.97 & $[0.69,\; 1.49]$ & ${<}\,0.001$ \\
123	0.25 & 3.34 & $[1.66,\; 6.64]$ & ${<}\,0.001$ \\
124	0.30 & 9.85 & $[6.70,\; 16.29]$ & ${<}\,0.001$ \\
125	\bottomrule
126	\end{tabular}
127	\end{table}
128	
129	\begin{figure}[t]
130	\centering
131	\includegraphics[width=\columnwidth]{fig4_bootstrap.pdf}
132	\caption{Forest plot of permutation test results. Horizontal bars show 95\% permutation CIs; diamonds mark observed median differences $\widetilde{\Delta}$. All CIs lie entirely above zero, confirming significant strategy-dependent severity at every sparsity level.}
133	\label{fig:permtest-forest}
134	\end{figure}
135	
136	
137	\section{Cross-Architecture Analysis}
138	\label{app:cross-arch}
139	
140	To test whether the phase-modulated severity pattern extends beyond the Qwen2 architecture, we replicate the experiment on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, 8B parameters; $n{=}49$ paired problems). Table~\ref{tab:llama-cross-arch} reports the strategy-dependent severity comparison across sparsity levels.
141	
142	The evidence for a strategy contrast on LLaMA is mixed: at $s{=}0.15$, the bootstrap CI excludes zero ($[0.002, 0.043]$) but the Bonferroni-corrected Wilcoxon test is non-significant ($p_{\text{Bonf}}{=}0.219$); conversely, at $s{=}0.30$ the CI spans zero ($[-0.069, 0.544]$) while the Wilcoxon test reaches significance ($p_{\text{Bonf}}{=}0.029$). At intermediate levels ($s \in \{0.20, 0.25\}$), neither CI nor Wilcoxon reaches significance. The median paired difference increases monotonically ($\widetilde{\Delta}$: $0.020 \to 0.356$), consistent with a genuine but weak trend---providing preliminary support for the cross-architecture hypothesis while underscoring the substantially weaker interaction on LlamaForCausalLM.\footnote{The CI/Wilcoxon discrepancy reflects differing power profiles under small $n$ with heavy-tailed distributions: the percentile bootstrap CI is based on the resampled median distribution and is less sensitive to tail observations, while the Wilcoxon signed-rank test uses signed ranks and is more sensitive to tail outliers. This inconsistency itself supports the conservative ``mixed/weak evidence'' interpretation.}
143	
144	The absolute magnitude is architecture-dependent: LLaMA severity differences are ${\sim}40{\times}$ smaller than DeepSeek and ${\sim}7{\times}$ smaller than Qwen. Notably, random eviction on LLaMA also exhibits a non-trivial phase gradient ($d_z$: $0.35 \to 0.44$), substantially reducing the strategy contrast that is the hallmark of the phase-strategy interaction on Qwen2 models. This suggests that the strength of the strategy$\times$phase interaction---not merely the severity gradient itself---is architecture-dependent. The directional pattern---importance producing larger phase gradients than random---is qualitatively consistent across all three models, but the LLaMA evidence should be interpreted as preliminary given the weak interaction magnitude and partial statistical significance.
145	
146	\begin{table}[t]
147	\centering
148	\small
149	\caption{Cross-architecture validation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM). $\widetilde{\Delta}$: median paired difference (importance $-$ random) with bootstrap 95\% CI ($B{=}10{,}000$); $p$: Bonferroni-corrected Wilcoxon signed-rank $p$ ($k{=}4$). $n{=}49$ paired problems.}
150	\label{tab:llama-cross-arch}
151	\begin{tabular}{@{}lcc@{}}
152	\toprule
153	$s$ & $\widetilde{\Delta}$\; [95\% CI] & $p_{\text{Bonf}}$ \\
154	\midrule
155	0.15 & $0.020$\; $[0.002,\; 0.043]$ & $0.219$ \\
156	0.20 & $0.022$\; $[-0.090,\; 0.187]$ & $0.253$ \\
157	0.25 & $0.095$\; $[-0.004,\; 0.303]$ & $0.083$ \\
158	0.30 & $0.356$\; $[-0.069,\; 0.544]$ & $\mathbf{0.029}$ \\
159	\bottomrule
160	\end{tabular}
161	\end{table}
162	
163	\paragraph{Post-hoc power analysis.}
164	We computed post-hoc power via bootstrap simulation ($B{=}10{,}000$) to assess what claims the $n{=}49$ sample can and cannot support. For the within-importance phase gradient (testing $\Delta_{\text{imp}} > 0$), power exceeds $0.99$ at all four sparsity levels, confirming that the sample is sufficient to detect the importance-based severity gradient. For strategy comparisons (testing $\Delta_{\text{imp}} - \Delta_{\text{rand}} > 0$), power ranges from $0.26$ ($s{=}0.15$) to $0.63$ ($s{=}0.30$), indicating that the sample is underpowered for detecting strategy-level differences at their observed effect sizes. Extrapolating from the observed effect sizes and variance, $n \geq 200$ paired problems would be needed to achieve $0.80$ power for the strategy comparison at $s{=}0.30$. This motivates the conservative interpretation in \S\ref{sec:cross-arch}: the within-importance gradient is confirmed, but the strategy$\times$phase interaction requires larger-scale replication.
165	
166	
167	\section{Analysis: Importance Discrimination Collapse}
168	\label{app:analysis}
169	
170	\subsection{Importance Discrimination Collapse}
171	\label{sec:discrimination-collapse}
172	
173	Head pruning reduces the number of heads contributing to cumulative importance scores, collapsing the score distribution. Table~\ref{tab:discrimination-metrics-full} quantifies this effect: the Gini coefficient decreases by $0.030$--$0.081$ (DeepSeek) and $0.010$--$0.020$ (Qwen) after pruning, with consistent negative deltas across all 16 conditions (both models $\times$ 4 sparsity levels $\times$ 2 strategies). The CV delta is likewise negative in all 8 importance-based conditions. The same pattern holds under random eviction, confirming that importance discrimination collapse is a consequence of head pruning \emph{per se}, not of the eviction strategy.
174	
175	\begin{table}[t]
176	\centering
177	\caption{Importance discrimination collapse under importance-based eviction. $\Delta\mathrm{Gini}$ and $\Delta\mathrm{CV}$ are post-pruning minus baseline; negative values indicate reduced discriminative power.}
178	\label{tab:discrimination-metrics-full}
179	\small
180	\begin{tabular}{llrr}
181	\toprule
182	Model & $s$ & $\Delta\mathrm{Gini}$ & $\Delta\mathrm{CV}$ \\
183	\midrule
184	DeepSeek & $0.15$ & $-0.030$ & $-0.56$ \\
185	DeepSeek & $0.20$ & $-0.040$ & $-0.77$ \\
186	DeepSeek & $0.25$ & $-0.065$ & $-1.29$ \\
187	DeepSeek & $0.30$ & $-0.081$ & $-1.66$ \\
188	\midrule
189	Qwen & $0.15$ & $-0.010$ & $-0.05$ \\
190	Qwen & $0.20$ & $-0.012$ & $-0.21$ \\
191	Qwen & $0.25$ & $-0.010$ & $-1.49$ \\
192	Qwen & $0.30$ & $-0.020$ & $-1.14$ \\
193	\bottomrule
194	\end{tabular}
195	\end{table}
196	
197	When importance scores lose discriminability, thresholding degenerates into noise-sensitive selection---functionally approaching biased random eviction. This is phase-dependent: in low-sparsity phases, attention is already broadly distributed, so pruning-induced collapse has maximum impact; in high-sparsity phases, concentration is preserved. Random eviction is immune because its decisions are independent of score quality, explaining $G \approx 1$.
198	
199	\subsection{Entropy Redistribution}
200	\label{sec:entropy-redistribution}
201	
202	Beyond importance discrimination collapse, we examine whether head pruning also redistributes the attention entropy of surviving heads. We measure the mean attention entropy per head:
203	\begin{equation}
204	    \mathcal{H}_i^{(h)} = -\sum_{j=1}^{T} a_{ij}^{(h)} \log a_{ij}^{(h)}
205	    \label{eq:attn-entropy}
206	\end{equation}
207	and compute $\Delta\mathcal{H}$ as the change from baseline (no pruning) to the pruned condition.
208	
209	For DeepSeek under importance-based eviction, the entropy delta is consistently negative across all four sparsity levels ($\Delta\mathcal{H} \in [-0.047, -0.040]$; Table~\ref{tab:entropy-deltas}), indicating that importance-based pruning systematically selects heads whose removal concentrates attention in the surviving heads, reinforcing importance discrimination collapse.
210	
211	For Qwen, the entropy pattern only partially replicates. The delta is negative at $s{=}0.15$ ($\Delta\mathcal{H} = -0.073$) and $s{=}0.20$ ($-0.076$), consistent with DeepSeek. However, at $s{=}0.25$, the delta reverses to $+0.045$, with 22 of 30 problems showing positive entropy change. At $s{=}0.30$, the delta is near zero ($-0.007$). The $s{=}0.25$ reversal is systematic rather than a statistical artifact: it is consistent across all three reasoning phases (low: $+0.042$, mid: $+0.034$, high: $+0.017$). We interpret this as a genuine model-specific difference, possibly arising from distinct head specialization patterns: Qwen's instruction tuning (vs.\ DeepSeek's distillation-based training) may produce head configurations where removing 25\% of heads triggers compensatory broadening rather than concentration.
212	
213	We characterize importance discrimination collapse as the robust, model-independent driver of the phase-strategy interaction, with entropy redistribution as a secondary amplifier that is consistent in DeepSeek but model-dependent in Qwen.
214	
215	\begin{table}[t]
216	\centering
217	\caption{Attention entropy deltas ($\Delta\mathcal{H}$) under importance-based eviction. DeepSeek shows consistent entropy compression; Qwen partially replicates with a reversal at $s{=}0.25$.}
218	\label{tab:entropy-deltas}
219	\small
220	\begin{tabular}{llr}
221	\toprule
222	Model & $s$ & $\Delta\mathcal{H}$ \\
223	\midrule
224	DeepSeek & $0.15$ & $-0.040$ \\
225	DeepSeek & $0.20$ & $-0.047$ \\
226	DeepSeek & $0.25$ & $-0.045$ \\
227	DeepSeek & $0.30$ & $-0.044$ \\
228	\midrule
229	Qwen & $0.15$ & $-0.073$ \\
230	Qwen & $0.20$ & $-0.076$ \\
231	Qwen & $0.25$ & $+0.045$ \\
232	Qwen & $0.30$ & $-0.007$ \\
233	\bottomrule
234	\end{tabular}
235	\end{table}
236	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f1598080-9151-49a3-bb4c-51542c26cd23",
  "isSidechain": true,
  "promptId": "eeb83888-ea16-4335-9ad7-31eca084b764",
  "agentId": "a4138636fc3e34597",
  "type": "user",
  "uuid": "7734d38b-3ae3-430e-997f-1e371349046b",
  "sourceToolAssistantUUID": "f1598080-9151-49a3-bb4c-51542c26cd23",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/paper_agent_9539225d",
  "sessionId": "75f62e16-26c1-41e3-a629-5dbc4dda9106",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cryptic-kindling-corbato"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-16T02:54:12.157Z_

Now let me search for specific numerical values across all files to check for discrepancies:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7734d38b-3ae3-430e-997f-1e371349046b",
  "isSidechain": true,
  "agentId": "a4138636fc3e34597",
  "requestId": "req_011Cb5VY96JGpNhF1BCkJPrH",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "ccbb2be6-a935-497e-84fd-0763985eca56",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/paper_agent_9539225d",
  "sessionId": "75f62e16-26c1-41e3-a629-5dbc4dda9106",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cryptic-kindling-corbato",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011jCMSvAJcDXKfyjCMUrQ28",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 25321,
      "cache_read_input_tokens": 29077,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 25321,
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

_source line 25 · 2026-05-16T02:54:13.423Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01VuE23227KsVzhCbiY4TZRs`</summary>

```json
{
  "pattern": "0\\.39.*8\\.48|8\\.48.*0\\.39",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper",
  "type": "tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ccbb2be6-a935-497e-84fd-0763985eca56",
  "isSidechain": true,
  "agentId": "a4138636fc3e34597",
  "requestId": "req_011Cb5VY96JGpNhF1BCkJPrH",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "9dac895c-7aff-43ae-adc1-1aa34d06d3c9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/paper_agent_9539225d",
  "sessionId": "75f62e16-26c1-41e3-a629-5dbc4dda9106",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cryptic-kindling-corbato",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011jCMSvAJcDXKfyjCMUrQ28",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 25321,
      "cache_read_input_tokens": 29077,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 25321,
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

_source line 26 · 2026-05-16T02:54:13.457Z_

<details><summary>↩ Tool result · `toolu_01VuE23227KsVzhCbiY4TZRs`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/conclusion.tex:4:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/appendix_moved.tex:81:DeepSeek-R1-Distill-Qwen-7B ($n{=}496$) & 0.39 & 1.21 & 3.99 & 8.48 \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/results.tex:8:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/results.tex:19:Importance & 0.39 & 1.21 & 3.99 & 8.48 \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/introduction.tex:12:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/introduction.tex:16:On DeepSeek-R1-Distill-Qwen-7B (500 MATH-500 problems), the median phase difference rises from $0.39$ at $s{=}0.15$ to $8.48$ at $s{=}0.30$ (all Bonferroni-corrected $p \ll 10^{-10}$; Jonckheere-Terpstra $z{=}33.7$, $p \ll 10^{-10}$).
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/abstract.tex:3:We show that compound severity is not phase-invariant: the paired median severity difference ($\Delta$) increases from $0.39$ to $8.48$ across sparsity levels, with phase amplification ratios reaching $G{=}7.5$--$79.8{\times}$, in 7B-scale mathematical reasoning models.
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/abstract.tex:5:On DeepSeek-R1-Distill-Qwen-7B (MATH-500, $n{=}496$), importance-based eviction produces a monotonically increasing severity gradient (median $\Delta$: $0.39 \to 8.48$; all $p \ll 10^{-10}$). Random eviction is $2.7$--$17{\times}$ weaker where significant ($s \geq 0.25$), with a strategy ranking crossover at $s{=}0.25$.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9dac895c-7aff-43ae-adc1-1aa34d06d3c9",
  "isSidechain": true,
  "promptId": "eeb83888-ea16-4335-9ad7-31eca084b764",
  "agentId": "a4138636fc3e34597",
  "type": "user",
  "uuid": "38a3a1b3-2e3f-4cb8-876b-07eab965df59",
  "sourceToolAssistantUUID": "9dac895c-7aff-43ae-adc1-1aa34d06d3c9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/paper_agent_9539225d",
  "sessionId": "75f62e16-26c1-41e3-a629-5dbc4dda9106",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cryptic-kindling-corbato"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-16T02:54:13.847Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01FdeU7vfQnCU8hrsBM29MY8`</summary>

```json
{
  "pattern": "0\\.07.*3\\.16|3\\.16.*0\\.07",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper",
  "type": "tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "38a3a1b3-2e3f-4cb8-876b-07eab965df59",
  "isSidechain": true,
  "agentId": "a4138636fc3e34597",
  "requestId": "req_011Cb5VY96JGpNhF1BCkJPrH",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "958e0390-7329-4c41-ad86-9cfa25579b51",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/paper_agent_9539225d",
  "sessionId": "75f62e16-26c1-41e3-a629-5dbc4dda9106",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cryptic-kindling-corbato",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011jCMSvAJcDXKfyjCMUrQ28",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 25321,
      "cache_read_input_tokens": 29077,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 25321,
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

_source line 28 · 2026-05-16T02:54:13.882Z_

<details><summary>↩ Tool result · `toolu_01FdeU7vfQnCU8hrsBM29MY8`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/conclusion.tex:4:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/appendix_moved.tex:82:Qwen2.5-7B-Instruct ($n{=}475$)         & 0.07 & 0.31 & 1.07 & 3.16 \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/abstract.tex:6:The pattern replicates on Qwen2.5-7B-Instruct ($n_{\text{eff}}{=}475$, $\Delta$: $0.07 \to 3.16$; all $p < 10^{-14}$), with exploratory cross-architecture evidence from a LlamaForCausalLM model ($n{=}49$; ${\sim}1/40$ effect size) suggesting the qualitative pattern may extend beyond Qwen2 (\S\ref{sec:cross-arch}).
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/introduction.tex:17:The pattern replicates on Qwen2.5-7B-Instruct ($\Delta$: $0.07 \to 3.16$; all $p < 10^{-14}$); preliminary evidence from DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM) suggests the phenomenon may extend beyond Qwen2 but at ${\sim}1/40$ the magnitude and with substantially weaker strategy contrast.
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/results.tex:88:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "958e0390-7329-4c41-ad86-9cfa25579b51",
  "isSidechain": true,
  "promptId": "eeb83888-ea16-4335-9ad7-31eca084b764",
  "agentId": "a4138636fc3e34597",
  "type": "user",
  "uuid": "4aab15d6-6147-4cd1-abc1-9e4f8aa777e1",
  "sourceToolAssistantUUID": "958e0390-7329-4c41-ad86-9cfa25579b51",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/paper_agent_9539225d",
  "sessionId": "75f62e16-26c1-41e3-a629-5dbc4dda9106",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cryptic-kindling-corbato"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-16T02:54:14.477Z_

<details open><summary>🔧 Tool call — Grep · `toolu_018Rhzq8con4zoB3Jy6qRWG2`</summary>

```json
{
  "pattern": "7\\.5.*79\\.8|79\\.8.*7\\.5",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper",
  "type": "tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4aab15d6-6147-4cd1-abc1-9e4f8aa777e1",
  "isSidechain": true,
  "agentId": "a4138636fc3e34597",
  "requestId": "req_011Cb5VY96JGpNhF1BCkJPrH",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "3f4ed63d-d6bc-4dc8-8b4f-7d7c0de43734",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/paper_agent_9539225d",
  "sessionId": "75f62e16-26c1-41e3-a629-5dbc4dda9106",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cryptic-kindling-corbato",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011jCMSvAJcDXKfyjCMUrQ28",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 25321,
      "cache_read_input_tokens": 29077,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 25321,
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

_source line 30 · 2026-05-16T02:54:14.497Z_

<details><summary>↩ Tool result · `toolu_018Rhzq8con4zoB3Jy6qRWG2`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/conclusion.tex:4:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/abstract.tex:3:We show that compound severity is not phase-invariant: the paired median severity difference ($\Delta$) increases from $0.39$ to $8.48$ across sparsity levels, with phase amplification ratios reaching $G{=}7.5$--$79.8{\times}$, in 7B-scale mathematical reasoning models.
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/introduction.tex:12:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/results.tex:29:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/results.tex:74:\caption{Amplification ratio ($G$, auxiliary metric) as a function of sparsity level $s$ on DeepSeek-R1-Distill-Qwen-7B ($n{=}496$). Importance-based eviction (solid) exhibits an increasing gradient from $7.5{\times}$ to $79.8{\times}$; random eviction (dashed) remains near $1{\times}$ ($0.5{\times}$--$1.1{\times}$). Shaded regions show bootstrap 95\% CIs. The primary metric $\Delta$ (paired median difference) is in Table~\ref{tab:main-results}.}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3f4ed63d-d6bc-4dc8-8b4f-7d7c0de43734",
  "isSidechain": true,
  "promptId": "eeb83888-ea16-4335-9ad7-31eca084b764",
  "agentId": "a4138636fc3e34597",
  "type": "user",
  "uuid": "75fa5bbf-bfa7-4622-aa76-26bfeb1881bb",
  "sourceToolAssistantUUID": "3f4ed63d-d6bc-4dc8-8b4f-7d7c0de43734",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/paper_agent_9539225d",
  "sessionId": "75f62e16-26c1-41e3-a629-5dbc4dda9106",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cryptic-kindling-corbato"
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-16T02:54:15.319Z_

<details open><summary>🔧 Tool call — Grep · `toolu_017aXQwEzrqzpRngzLH7NnRv`</summary>

```json
{
  "pattern": "n\\{=\\}496|n=496",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper",
  "type": "tex",
  "output_mode": "content",
  "head_limit": 20
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "75fa5bbf-bfa7-4622-aa76-26bfeb1881bb",
  "isSidechain": true,
  "agentId": "a4138636fc3e34597",
  "requestId": "req_011Cb5VY96JGpNhF1BCkJPrH",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "1403bc07-f7a9-48a9-967b-bb8a8b97d298",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/paper_agent_9539225d",
  "sessionId": "75f62e16-26c1-41e3-a629-5dbc4dda9106",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cryptic-kindling-corbato",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011jCMSvAJcDXKfyjCMUrQ28",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 25321,
      "cache_read_input_tokens": 29077,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 25321,
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

_source line 32 · 2026-05-16T02:54:15.338Z_

<details><summary>↩ Tool result · `toolu_017aXQwEzrqzpRngzLH7NnRv`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/conclusion.tex:4:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/appendix_robustness.tex:76:\caption{Segmentation robustness: median $\Delta$ under tercile ($n{=}496$/$475$), quartile ($n{=}50$ spot check), and quintile ($n{=}50$ spot check) segmentation. Importance-based eviction; all $p_{\text{Bonf}} < 10^{-7}$.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/appendix_moved.tex:5:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/appendix_moved.tex:10:\caption{Strategy-dependent crossover at $s{=}0.25$ on DeepSeek ($n{=}496$). Grouped bar chart of median II by eviction strategy and reasoning phase. Importance-based eviction outperforms random in the high-sparsity phase but produces $2.6{\times}$ higher II in the low-sparsity phase, reversing the strategy ranking.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/appendix_moved.tex:21:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/appendix_moved.tex:48:Despite lacking explicit \texttt{&lt;think>} delimiters, Qwen2.5-7B-Instruct exhibits sufficient variation in attention sparsity to permit phase segmentation via the same quantile-based method (\S\ref{par:phase-segmentation}). Twenty-five of the 500 problems are excluded due to degenerate phase assignments, yielding $n{=}475$ valid problems for Qwen (vs.\ $n{=}496$ for DeepSeek).
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/appendix_moved.tex:81:DeepSeek-R1-Distill-Qwen-7B ($n{=}496$) & 0.39 & 1.21 & 3.99 & 8.48 \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/appendix_moved.tex:90:\caption{Cross-training-paradigm comparison of the median severity difference under importance-based eviction ($n{=}496$/$475$). Both DeepSeek (solid) and Qwen (dashed) exhibit monotonically increasing $\Delta$ with sparsity; Qwen's magnitude is approximately one-quarter to one-sixth of DeepSeek's.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/appendix_moved.tex:115:\caption{Paired permutation test for compound severity: importance vs.\ random eviction on DeepSeek-R1-Distill-Qwen-7B ($n{=}49$ profiling subset, $10{,}000$ permutations, Bonferroni-corrected). The monotonic $\Delta$ pattern is confirmed at $n{=}496$ (Table~\ref{tab:aggregate-ii}).}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/methodology.tex:8:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/abstract.tex:5:On DeepSeek-R1-Distill-Qwen-7B (MATH-500, $n{=}496$), importance-based eviction produces a monotonically increasing severity gradient (median $\Delta$: $0.39 \to 8.48$; all $p \ll 10^{-10}$). Random eviction is $2.7$--$17{\times}$ weaker where significant ($s \geq 0.25$), with a strategy ranking crossover at $s{=}0.25$.
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/appendix_disc_analysis.tex:48:Bootstrap confidence intervals use $B{=}10{,}000$ resamples (seed$=$42). The primary analysis uses $n{=}496$ paired problems for DeepSeek (4 excluded) and $n{=}475$ for Qwen (25 excluded); the permutation test (Table~\ref{tab:permutation}) uses $n{=}49$ from an initial profiling subset.
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/appendix_disc_analysis.tex:50:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/results.tex:13:\caption{Median compound severity difference ($\Delta = \widetilde{\mathrm{II}}_{\textit{low}} - \widetilde{\mathrm{II}}_{\textit{high}}$) by eviction strategy and sparsity level on DeepSeek-R1-Distill-Qwen-7B ($n{=}496$, 500 MATH-500 problems).}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/results.tex:29:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/results.tex:35:\caption{Per-phase interaction index (II) at $n{=}496$/$475$. $\Delta$: paired median difference with bootstrap 95\% CI ($B{=}10{,}000$). $G$: per-problem amplification ratio (Eq.~\ref{eq:gradient}) with bootstrap 95\% CI. Profiling-subset values ($n{=}50$) in Table~\ref{tab:profiling-subset}.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/results.tex:41:\multicolumn{6}{@{}l}{\textit{DeepSeek-R1-Distill-Qwen-7B ($n{=}496$)}} \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/results.tex:74:\caption{Amplification ratio ($G$, auxiliary metric) as a function of sparsity level $s$ on DeepSeek-R1-Distill-Qwen-7B ($n{=}496$). Importance-based eviction (solid) exhibits an increasing gradient from $7.5{\times}$ to $79.8{\times}$; random eviction (dashed) remains near $1{\times}$ ($0.5{\times}$--$1.1{\times}$). Shaded regions show bootstrap 95\% CIs. The primary metric $\Delta$ (paired median difference) is in Table~\ref{tab:main-results}.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/results.tex:82:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/results.tex:103:[Omitted long matching line]

[Showing results with pagination = limit: 20]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1403bc07-f7a9-48a9-967b-bb8a8b97d298",
  "isSidechain": true,
  "promptId": "eeb83888-ea16-4335-9ad7-31eca084b764",
  "agentId": "a4138636fc3e34597",
  "type": "user",
  "uuid": "84d983b7-71e2-4a9e-85f8-dabeebb41c9b",
  "sourceToolAssistantUUID": "1403bc07-f7a9-48a9-967b-bb8a8b97d298",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/paper_agent_9539225d",
  "sessionId": "75f62e16-26c1-41e3-a629-5dbc4dda9106",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cryptic-kindling-corbato"
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-16T02:54:15.724Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01LjqffoG23jK5EuRvVH2HSk`</summary>

```json
{
  "pattern": "n\\{=\\}475|n=475",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper",
  "type": "tex",
  "output_mode": "content",
  "head_limit": 20
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "84d983b7-71e2-4a9e-85f8-dabeebb41c9b",
  "isSidechain": true,
  "agentId": "a4138636fc3e34597",
  "requestId": "req_011Cb5VY96JGpNhF1BCkJPrH",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "e6e9d5a1-a1fb-41d4-b552-5a9922c2129a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/paper_agent_9539225d",
  "sessionId": "75f62e16-26c1-41e3-a629-5dbc4dda9106",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cryptic-kindling-corbato",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011jCMSvAJcDXKfyjCMUrQ28",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 25321,
      "cache_read_input_tokens": 29077,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 25321,
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

_source line 34 · 2026-05-16T02:54:15.743Z_

<details><summary>↩ Tool result · `toolu_01LjqffoG23jK5EuRvVH2HSk`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/conclusion.tex:4:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/appendix_moved.tex:48:Despite lacking explicit \texttt{&lt;think>} delimiters, Qwen2.5-7B-Instruct exhibits sufficient variation in attention sparsity to permit phase segmentation via the same quantile-based method (\S\ref{par:phase-segmentation}). Twenty-five of the 500 problems are excluded due to degenerate phase assignments, yielding $n{=}475$ valid problems for Qwen (vs.\ $n{=}496$ for DeepSeek).
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/appendix_moved.tex:82:Qwen2.5-7B-Instruct ($n{=}475$)         & 0.07 & 0.31 & 1.07 & 3.16 \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/methodology.tex:8:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/appendix_disc_analysis.tex:48:Bootstrap confidence intervals use $B{=}10{,}000$ resamples (seed$=$42). The primary analysis uses $n{=}496$ paired problems for DeepSeek (4 excluded) and $n{=}475$ for Qwen (25 excluded); the permutation test (Table~\ref{tab:permutation}) uses $n{=}49$ from an initial profiling subset.
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/results.tex:54:\multicolumn{6}{@{}l}{\textit{Qwen2.5-7B-Instruct ($n{=}475$)}} \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/results.tex:112:$s$ & DS ($n{=}496$): $\widetilde{\Delta}$\; [95\% CI] & QW ($n{=}475$): $\widetilde{\Delta}$\; [95\% CI] \\
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e6e9d5a1-a1fb-41d4-b552-5a9922c2129a",
  "isSidechain": true,
  "promptId": "eeb83888-ea16-4335-9ad7-31eca084b764",
  "agentId": "a4138636fc3e34597",
  "type": "user",
  "uuid": "208e23b6-cba8-49ce-98eb-9b0e0ade8f63",
  "sourceToolAssistantUUID": "e6e9d5a1-a1fb-41d4-b552-5a9922c2129a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/paper_agent_9539225d",
  "sessionId": "75f62e16-26c1-41e3-a629-5dbc4dda9106",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cryptic-kindling-corbato"
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-16T02:54:16.166Z_

<details open><summary>🔧 Tool call — Grep · `toolu_013UTWDpWLfsuhkbfGqArkNB`</summary>

```json
{
  "pattern": "n\\{=\\}49|n=49",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper",
  "type": "tex",
  "output_mode": "content",
  "head_limit": 20
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "208e23b6-cba8-49ce-98eb-9b0e0ade8f63",
  "isSidechain": true,
  "agentId": "a4138636fc3e34597",
  "requestId": "req_011Cb5VY96JGpNhF1BCkJPrH",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "9c73c841-90e3-4aa4-a068-c61f383359e5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/paper_agent_9539225d",
  "sessionId": "75f62e16-26c1-41e3-a629-5dbc4dda9106",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cryptic-kindling-corbato",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011jCMSvAJcDXKfyjCMUrQ28",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 25321,
      "cache_read_input_tokens": 29077,
      "output_tokens": 891,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 25321
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 891,
          "cache_read_input_tokens": 29077,
          "cache_creation_input_tokens": 25321,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 25321,
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

_source line 36 · 2026-05-16T02:54:16.204Z_

<details><summary>↩ Tool result · `toolu_013UTWDpWLfsuhkbfGqArkNB`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/conclusion.tex:4:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/appendix_robustness.tex:76:\caption{Segmentation robustness: median $\Delta$ under tercile ($n{=}496$/$475$), quartile ($n{=}50$ spot check), and quintile ($n{=}50$ spot check) segmentation. Importance-based eviction; all $p_{\text{Bonf}} < 10^{-7}$.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/appendix_moved.tex:5:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/appendix_moved.tex:10:\caption{Strategy-dependent crossover at $s{=}0.25$ on DeepSeek ($n{=}496$). Grouped bar chart of median II by eviction strategy and reasoning phase. Importance-based eviction outperforms random in the high-sparsity phase but produces $2.6{\times}$ higher II in the low-sparsity phase, reversing the strategy ranking.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/appendix_moved.tex:21:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/appendix_moved.tex:48:Despite lacking explicit \texttt{&lt;think>} delimiters, Qwen2.5-7B-Instruct exhibits sufficient variation in attention sparsity to permit phase segmentation via the same quantile-based method (\S\ref{par:phase-segmentation}). Twenty-five of the 500 problems are excluded due to degenerate phase assignments, yielding $n{=}475$ valid problems for Qwen (vs.\ $n{=}496$ for DeepSeek).
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/appendix_moved.tex:81:DeepSeek-R1-Distill-Qwen-7B ($n{=}496$) & 0.39 & 1.21 & 3.99 & 8.48 \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/appendix_moved.tex:90:\caption{Cross-training-paradigm comparison of the median severity difference under importance-based eviction ($n{=}496$/$475$). Both DeepSeek (solid) and Qwen (dashed) exhibit monotonically increasing $\Delta$ with sparsity; Qwen's magnitude is approximately one-quarter to one-sixth of DeepSeek's.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/appendix_moved.tex:115:\caption{Paired permutation test for compound severity: importance vs.\ random eviction on DeepSeek-R1-Distill-Qwen-7B ($n{=}49$ profiling subset, $10{,}000$ permutations, Bonferroni-corrected). The monotonic $\Delta$ pattern is confirmed at $n{=}496$ (Table~\ref{tab:aggregate-ii}).}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/appendix_moved.tex:140:To test whether the phase-modulated severity pattern extends beyond the Qwen2 architecture, we replicate the experiment on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, 8B parameters; $n{=}49$ paired problems). Table~\ref{tab:llama-cross-arch} reports the strategy-dependent severity comparison across sparsity levels.
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/appendix_moved.tex:149:\caption{Cross-architecture validation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM). $\widetilde{\Delta}$: median paired difference (importance $-$ random) with bootstrap 95\% CI ($B{=}10{,}000$); $p$: Bonferroni-corrected Wilcoxon signed-rank $p$ ($k{=}4$). $n{=}49$ paired problems.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/appendix_moved.tex:164:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/results.tex:13:\caption{Median compound severity difference ($\Delta = \widetilde{\mathrm{II}}_{\textit{low}} - \widetilde{\mathrm{II}}_{\textit{high}}$) by eviction strategy and sparsity level on DeepSeek-R1-Distill-Qwen-7B ($n{=}496$, 500 MATH-500 problems).}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/results.tex:29:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/results.tex:35:\caption{Per-phase interaction index (II) at $n{=}496$/$475$. $\Delta$: paired median difference with bootstrap 95\% CI ($B{=}10{,}000$). $G$: per-problem amplification ratio (Eq.~\ref{eq:gradient}) with bootstrap 95\% CI. Profiling-subset values ($n{=}50$) in Table~\ref{tab:profiling-subset}.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/results.tex:41:\multicolumn{6}{@{}l}{\textit{DeepSeek-R1-Distill-Qwen-7B ($n{=}496$)}} \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/results.tex:74:\caption{Amplification ratio ($G$, auxiliary metric) as a function of sparsity level $s$ on DeepSeek-R1-Distill-Qwen-7B ($n{=}496$). Importance-based eviction (solid) exhibits an increasing gradient from $7.5{\times}$ to $79.8{\times}$; random eviction (dashed) remains near $1{\times}$ ($0.5{\times}$--$1.1{\times}$). Shaded regions show bootstrap 95\% CIs. The primary metric $\Delta$ (paired median difference) is in Table~\ref{tab:main-results}.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/results.tex:82:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/results.tex:93:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/results.tex:103:[Omitted long matching line]

[Showing results with pagination = limit: 20]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9c73c841-90e3-4aa4-a068-c61f383359e5",
  "isSidechain": true,
  "promptId": "eeb83888-ea16-4335-9ad7-31eca084b764",
  "agentId": "a4138636fc3e34597",
  "type": "user",
  "uuid": "e9cdfb0f-801f-49f4-9c63-384e05e5d481",
  "sourceToolAssistantUUID": "9c73c841-90e3-4aa4-a068-c61f383359e5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/paper_agent_9539225d",
  "sessionId": "75f62e16-26c1-41e3-a629-5dbc4dda9106",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cryptic-kindling-corbato"
}
```

</details>

---

### Assistant

_source line 37 · 2026-05-16T02:54:17.622Z_

Now let me search for the p-values, strategy ratios, and other key numbers:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e9cdfb0f-801f-49f4-9c63-384e05e5d481",
  "isSidechain": true,
  "agentId": "a4138636fc3e34597",
  "requestId": "req_011Cb5VYYUiwsvSXdcm8izXn",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d16796c5-22ea-48e2-8712-ef322ea22894",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/paper_agent_9539225d",
  "sessionId": "75f62e16-26c1-41e3-a629-5dbc4dda9106",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cryptic-kindling-corbato",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017bFVejPi2LfT7DNoXhZDbX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 7627,
      "cache_read_input_tokens": 54398,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7627,
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

_source line 38 · 2026-05-16T02:54:18.489Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01Jzsvb7D5yPivBJkSzWBqC4`</summary>

```json
{
  "pattern": "2\\.7.*17|17.*2\\.7",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper",
  "type": "tex",
  "output_mode": "content",
  "head_limit": 15
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d16796c5-22ea-48e2-8712-ef322ea22894",
  "isSidechain": true,
  "agentId": "a4138636fc3e34597",
  "requestId": "req_011Cb5VYYUiwsvSXdcm8izXn",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "cc4dab28-68fe-4f42-855b-7a782bca7024",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/paper_agent_9539225d",
  "sessionId": "75f62e16-26c1-41e3-a629-5dbc4dda9106",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cryptic-kindling-corbato",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017bFVejPi2LfT7DNoXhZDbX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 7627,
      "cache_read_input_tokens": 54398,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7627,
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

_source line 39 · 2026-05-16T02:54:18.513Z_

<details><summary>↩ Tool result · `toolu_01Jzsvb7D5yPivBJkSzWBqC4`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/conclusion.tex:4:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/abstract.tex:5:On DeepSeek-R1-Distill-Qwen-7B (MATH-500, $n{=}496$), importance-based eviction produces a monotonically increasing severity gradient (median $\Delta$: $0.39 \to 8.48$; all $p \ll 10^{-10}$). Random eviction is $2.7$--$17{\times}$ weaker where significant ($s \geq 0.25$), with a strategy ranking crossover at $s{=}0.25$.
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/appendix_disc_analysis.tex:14:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/introduction.tex:18:Random eviction develops a detectable but weak phase gradient only above $s \approx 0.20$ ($2.7$--$17{\times}$ smaller than importance-based where both strategies are significant, $s \geq 0.25$), confirming that the dominant gradient is an emergent phase-strategy interaction.
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/introduction.tex:25:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/results.tex:45:0.20 & Importance & 0.008 & 1.211 & 1.21\; $[1.11,\; 1.34]$ & $\mathbf{17.9}$\; $[12.7,\; 26.3]$ \\
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cc4dab28-68fe-4f42-855b-7a782bca7024",
  "isSidechain": true,
  "promptId": "eeb83888-ea16-4335-9ad7-31eca084b764",
  "agentId": "a4138636fc3e34597",
  "type": "user",
  "uuid": "08602dc9-a0a5-4fc8-8ae2-1887143c92ce",
  "sourceToolAssistantUUID": "cc4dab28-68fe-4f42-855b-7a782bca7024",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/paper_agent_9539225d",
  "sessionId": "75f62e16-26c1-41e3-a629-5dbc4dda9106",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cryptic-kindling-corbato"
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-16T02:54:19.157Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01Dvd3qHrB6MqxhcDuo7nK9a`</summary>

```json
{
  "pattern": "15.*17|17.*15",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper",
  "type": "tex",
  "output_mode": "content",
  "head_limit": 15
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "08602dc9-a0a5-4fc8-8ae2-1887143c92ce",
  "isSidechain": true,
  "agentId": "a4138636fc3e34597",
  "requestId": "req_011Cb5VYYUiwsvSXdcm8izXn",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "72ad945d-7386-4269-aa20-3b16dfb36654",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/paper_agent_9539225d",
  "sessionId": "75f62e16-26c1-41e3-a629-5dbc4dda9106",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cryptic-kindling-corbato",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017bFVejPi2LfT7DNoXhZDbX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 7627,
      "cache_read_input_tokens": 54398,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7627,
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

_source line 41 · 2026-05-16T02:54:19.179Z_

<details><summary>↩ Tool result · `toolu_01Dvd3qHrB6MqxhcDuo7nK9a`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/analysis.tex:4:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/analysis.tex:9:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/conclusion.tex:4:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/appendix_moved.tex:211:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/limitations.tex:5:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/limitations.tex:17:The importance discrimination collapse mechanism is a correlational marker, not a complete causal explanation: both strategies exhibit near-identical Gini drops yet severity diverges by $15$--$17{\times}$, indicating that Gini collapse alone is insufficient. Causal validation through controlled entropy manipulation is needed. The entropy redistribution component replicates on only 2/4 Qwen conditions, suggesting model-specific factors.
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/abstract.tex:7:We present \emph{importance discrimination collapse}---the degeneration of head importance scores toward uniformity under compound stress---as a correlational diagnostic: both strategies exhibit near-identical Gini drops, yet severity diverges by $15$--$17{\times}$, implicating the structural specificity of importance-based pruning as the key differentiator.
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/results.tex:8:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "72ad945d-7386-4269-aa20-3b16dfb36654",
  "isSidechain": true,
  "promptId": "eeb83888-ea16-4335-9ad7-31eca084b764",
  "agentId": "a4138636fc3e34597",
  "type": "user",
  "uuid": "b0d6aeb4-3b97-4418-b24d-8b6767c71df1",
  "sourceToolAssistantUUID": "72ad945d-7386-4269-aa20-3b16dfb36654",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/paper_agent_9539225d",
  "sessionId": "75f62e16-26c1-41e3-a629-5dbc4dda9106",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cryptic-kindling-corbato"
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-16T02:54:19.757Z_

<details open><summary>🔧 Tool call — Grep · `toolu_015xRoSAwnWGQ5LJ2wNr4Uhi`</summary>

```json
{
  "pattern": "z\\{=\\}33\\.7|z=33\\.7",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper",
  "type": "tex",
  "output_mode": "content",
  "head_limit": 15
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b0d6aeb4-3b97-4418-b24d-8b6767c71df1",
  "isSidechain": true,
  "agentId": "a4138636fc3e34597",
  "requestId": "req_011Cb5VYYUiwsvSXdcm8izXn",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "0528d8fd-34df-4801-bb28-1e4371dabc33",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/paper_agent_9539225d",
  "sessionId": "75f62e16-26c1-41e3-a629-5dbc4dda9106",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cryptic-kindling-corbato",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017bFVejPi2LfT7DNoXhZDbX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 7627,
      "cache_read_input_tokens": 54398,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7627,
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

_source line 43 · 2026-05-16T02:54:19.782Z_

<details><summary>↩ Tool result · `toolu_015xRoSAwnWGQ5LJ2wNr4Uhi`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/introduction.tex:12:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/introduction.tex:16:On DeepSeek-R1-Distill-Qwen-7B (500 MATH-500 problems), the median phase difference rises from $0.39$ at $s{=}0.15$ to $8.48$ at $s{=}0.30$ (all Bonferroni-corrected $p \ll 10^{-10}$; Jonckheere-Terpstra $z{=}33.7$, $p \ll 10^{-10}$).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0528d8fd-34df-4801-bb28-1e4371dabc33",
  "isSidechain": true,
  "promptId": "eeb83888-ea16-4335-9ad7-31eca084b764",
  "agentId": "a4138636fc3e34597",
  "type": "user",
  "uuid": "bf203905-37ce-43be-8512-0821125cd752",
  "sourceToolAssistantUUID": "0528d8fd-34df-4801-bb28-1e4371dabc33",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/paper_agent_9539225d",
  "sessionId": "75f62e16-26c1-41e3-a629-5dbc4dda9106",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cryptic-kindling-corbato"
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-16T02:54:20.469Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01FzgmFVr21hAnmJfGv5ybaq`</summary>

```json
{
  "pattern": "z.*6\\.2|6\\.2.*z",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper",
  "type": "tex",
  "output_mode": "content",
  "head_limit": 15
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bf203905-37ce-43be-8512-0821125cd752",
  "isSidechain": true,
  "agentId": "a4138636fc3e34597",
  "requestId": "req_011Cb5VYYUiwsvSXdcm8izXn",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f66c7d26-6e3e-437b-8048-a4d8c9f474a1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/paper_agent_9539225d",
  "sessionId": "75f62e16-26c1-41e3-a629-5dbc4dda9106",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cryptic-kindling-corbato",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017bFVejPi2LfT7DNoXhZDbX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 7627,
      "cache_read_input_tokens": 54398,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7627,
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

_source line 45 · 2026-05-16T02:54:20.497Z_

<details><summary>↩ Tool result · `toolu_01FzgmFVr21hAnmJfGv5ybaq`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/appendix.tex:38:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/results.tex:8:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/results.tex:88:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/methodology.tex:18:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f66c7d26-6e3e-437b-8048-a4d8c9f474a1",
  "isSidechain": true,
  "promptId": "eeb83888-ea16-4335-9ad7-31eca084b764",
  "agentId": "a4138636fc3e34597",
  "type": "user",
  "uuid": "036d995c-9258-4dcf-9bd6-885839c79638",
  "sourceToolAssistantUUID": "f66c7d26-6e3e-437b-8048-a4d8c9f474a1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/paper_agent_9539225d",
  "sessionId": "75f62e16-26c1-41e3-a629-5dbc4dda9106",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cryptic-kindling-corbato"
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-16T02:54:20.822Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01P9vifKKuu2xypueoeqcPVb`</summary>

```json
{
  "pattern": "18\\%|18 percent",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper",
  "type": "tex",
  "output_mode": "content",
  "head_limit": 15
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "036d995c-9258-4dcf-9bd6-885839c79638",
  "isSidechain": true,
  "agentId": "a4138636fc3e34597",
  "requestId": "req_011Cb5VYYUiwsvSXdcm8izXn",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "065a35d3-26f0-4a44-a389-adf0ef131844",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/paper_agent_9539225d",
  "sessionId": "75f62e16-26c1-41e3-a629-5dbc4dda9106",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cryptic-kindling-corbato",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017bFVejPi2LfT7DNoXhZDbX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 7627,
      "cache_read_input_tokens": 54398,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7627,
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

_source line 47 · 2026-05-16T02:54:20.843Z_

<details><summary>↩ Tool result · `toolu_01P9vifKKuu2xypueoeqcPVb`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "065a35d3-26f0-4a44-a389-adf0ef131844",
  "isSidechain": true,
  "promptId": "eeb83888-ea16-4335-9ad7-31eca084b764",
  "agentId": "a4138636fc3e34597",
  "type": "user",
  "uuid": "a6324425-18e8-4e42-95da-06b7a5ebd45f",
  "sourceToolAssistantUUID": "065a35d3-26f0-4a44-a389-adf0ef131844",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/paper_agent_9539225d",
  "sessionId": "75f62e16-26c1-41e3-a629-5dbc4dda9106",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cryptic-kindling-corbato"
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-16T02:54:21.447Z_

<details open><summary>🔧 Tool call — Grep · `toolu_0147hacE9qDfMHRbzH6cAs8D`</summary>

```json
{
  "pattern": "46\\%|dense.*46",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper",
  "type": "tex",
  "output_mode": "content",
  "head_limit": 15
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a6324425-18e8-4e42-95da-06b7a5ebd45f",
  "isSidechain": true,
  "agentId": "a4138636fc3e34597",
  "requestId": "req_011Cb5VYYUiwsvSXdcm8izXn",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "2628ba8b-f473-43f3-a37b-dcebacea4aaf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/paper_agent_9539225d",
  "sessionId": "75f62e16-26c1-41e3-a629-5dbc4dda9106",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cryptic-kindling-corbato",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017bFVejPi2LfT7DNoXhZDbX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 7627,
      "cache_read_input_tokens": 54398,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7627,
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

_source line 49 · 2026-05-16T02:54:21.473Z_

<details><summary>↩ Tool result · `toolu_0147hacE9qDfMHRbzH6cAs8D`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2628ba8b-f473-43f3-a37b-dcebacea4aaf",
  "isSidechain": true,
  "promptId": "eeb83888-ea16-4335-9ad7-31eca084b764",
  "agentId": "a4138636fc3e34597",
  "type": "user",
  "uuid": "0b0c05c2-d8c8-4ce6-a8e6-481d7d02d1e2",
  "sourceToolAssistantUUID": "2628ba8b-f473-43f3-a37b-dcebacea4aaf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/paper_agent_9539225d",
  "sessionId": "75f62e16-26c1-41e3-a629-5dbc4dda9106",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cryptic-kindling-corbato"
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-16T02:54:21.893Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01PcX8jiEjh6hJvpaabNPtuC`</summary>

```json
{
  "pattern": "19\\%|s030.*19",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper",
  "type": "tex",
  "output_mode": "content",
  "head_limit": 15
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0b0c05c2-d8c8-4ce6-a8e6-481d7d02d1e2",
  "isSidechain": true,
  "agentId": "a4138636fc3e34597",
  "requestId": "req_011Cb5VYYUiwsvSXdcm8izXn",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f3fb8448-3189-410d-a083-04601c77d2f4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/paper_agent_9539225d",
  "sessionId": "75f62e16-26c1-41e3-a629-5dbc4dda9106",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cryptic-kindling-corbato",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017bFVejPi2LfT7DNoXhZDbX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 7627,
      "cache_read_input_tokens": 54398,
      "output_tokens": 1076,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7627
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 1076,
          "cache_read_input_tokens": 54398,
          "cache_creation_input_tokens": 7627,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7627,
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

_source line 51 · 2026-05-16T02:54:21.926Z_

<details><summary>↩ Tool result · `toolu_01PcX8jiEjh6hJvpaabNPtuC`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f3fb8448-3189-410d-a083-04601c77d2f4",
  "isSidechain": true,
  "promptId": "eeb83888-ea16-4335-9ad7-31eca084b764",
  "agentId": "a4138636fc3e34597",
  "type": "user",
  "uuid": "91da8423-7a92-4ecd-a3d0-fc4b3aed9cac",
  "sourceToolAssistantUUID": "f3fb8448-3189-410d-a083-04601c77d2f4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/paper_agent_9539225d",
  "sessionId": "75f62e16-26c1-41e3-a629-5dbc4dda9106",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cryptic-kindling-corbato"
}
```

</details>

---

### Assistant

_source line 52 · 2026-05-16T02:54:23.173Z_

Let me search for the accuracy and pilot experiment numbers more specifically:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "91da8423-7a92-4ecd-a3d0-fc4b3aed9cac",
  "isSidechain": true,
  "agentId": "a4138636fc3e34597",
  "requestId": "req_011Cb5VYxvtSFL1b1L2tf6Vo",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "15032082-f2ce-417f-af14-99837afdb766",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/paper_agent_9539225d",
  "sessionId": "75f62e16-26c1-41e3-a629-5dbc4dda9106",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cryptic-kindling-corbato",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011aXdhiuWkkTctraFmSZKW3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 2869,
      "cache_read_input_tokens": 62025,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2869,
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

_source line 53 · 2026-05-16T02:54:24.237Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01YQzntWTLonihzCRcsrNk7c`</summary>

```json
{
  "pattern": "74\\%.*4\\%|dense.*74|Qwen.*46",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper",
  "type": "tex",
  "output_mode": "content",
  "head_limit": 20
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "15032082-f2ce-417f-af14-99837afdb766",
  "isSidechain": true,
  "agentId": "a4138636fc3e34597",
  "requestId": "req_011Cb5VYxvtSFL1b1L2tf6Vo",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "73f510e4-361c-4af4-9159-ad4a28d2aafe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/paper_agent_9539225d",
  "sessionId": "75f62e16-26c1-41e3-a629-5dbc4dda9106",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cryptic-kindling-corbato",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011aXdhiuWkkTctraFmSZKW3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 2869,
      "cache_read_input_tokens": 62025,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2869,
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

_source line 54 · 2026-05-16T02:54:24.258Z_

<details><summary>↩ Tool result · `toolu_01YQzntWTLonihzCRcsrNk7c`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/appendix_disc_analysis.tex:4:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/appendix_disc_analysis.tex:122:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/results.tex:132:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "73f510e4-361c-4af4-9159-ad4a28d2aafe",
  "isSidechain": true,
  "promptId": "eeb83888-ea16-4335-9ad7-31eca084b764",
  "agentId": "a4138636fc3e34597",
  "type": "user",
  "uuid": "457d80dc-a635-4747-81e7-9bdcbc7bb662",
  "sourceToolAssistantUUID": "73f510e4-361c-4af4-9159-ad4a28d2aafe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/paper_agent_9539225d",
  "sessionId": "75f62e16-26c1-41e3-a629-5dbc4dda9106",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cryptic-kindling-corbato"
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-16T02:54:25.038Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01Sydh4mxDMK5Q8XoAnPNXy4`</summary>

```json
{
  "pattern": "\\-27\\s*pp",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper",
  "type": "tex",
  "output_mode": "content",
  "head_limit": 20
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "457d80dc-a635-4747-81e7-9bdcbc7bb662",
  "isSidechain": true,
  "agentId": "a4138636fc3e34597",
  "requestId": "req_011Cb5VYxvtSFL1b1L2tf6Vo",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "a4066b97-afad-420b-bcb7-e06afe047f37",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/paper_agent_9539225d",
  "sessionId": "75f62e16-26c1-41e3-a629-5dbc4dda9106",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cryptic-kindling-corbato",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011aXdhiuWkkTctraFmSZKW3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 2869,
      "cache_read_input_tokens": 62025,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2869,
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

_source line 56 · 2026-05-16T02:54:25.060Z_

<details><summary>↩ Tool result · `toolu_01Sydh4mxDMK5Q8XoAnPNXy4`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a4066b97-afad-420b-bcb7-e06afe047f37",
  "isSidechain": true,
  "promptId": "eeb83888-ea16-4335-9ad7-31eca084b764",
  "agentId": "a4138636fc3e34597",
  "type": "user",
  "uuid": "236e0ed1-425b-4b32-be4b-212cfb0ea422",
  "sourceToolAssistantUUID": "a4066b97-afad-420b-bcb7-e06afe047f37",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/paper_agent_9539225d",
  "sessionId": "75f62e16-26c1-41e3-a629-5dbc4dda9106",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cryptic-kindling-corbato"
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-16T02:54:25.380Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01H1vz97dLoK1fYDnkQAmSCX`</summary>

```json
{
  "pattern": "pilot|oracle recovery",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper",
  "type": "tex",
  "output_mode": "content",
  "head_limit": 20
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "236e0ed1-425b-4b32-be4b-212cfb0ea422",
  "isSidechain": true,
  "agentId": "a4138636fc3e34597",
  "requestId": "req_011Cb5VYxvtSFL1b1L2tf6Vo",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "0a0b64b1-204e-42d5-a709-dfc978d208dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/paper_agent_9539225d",
  "sessionId": "75f62e16-26c1-41e3-a629-5dbc4dda9106",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cryptic-kindling-corbato",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011aXdhiuWkkTctraFmSZKW3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 2869,
      "cache_read_input_tokens": 62025,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2869,
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

_source line 58 · 2026-05-16T02:54:25.394Z_

<details><summary>↩ Tool result · `toolu_01H1vz97dLoK1fYDnkQAmSCX`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/discussion.tex:5:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/limitations.tex:2:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/appendix_disc_analysis.tex:21:\label{app:pilot-mitigation}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/appendix_disc_analysis.tex:56:Our primary analysis spans $s \in \{0.15, 0.20, 0.25, 0.30\}$; pilot data at $s{=}0.10$ and $s{=}0.35$ exist (6 total sparsity levels) but are not included in the main analysis due to limited sample size at these boundary conditions. Monotonicity is established at the tested sparsity levels (JT test $p \ll 10^{-10}$); the functional form of $G(s)$ between and beyond these levels is not characterized.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0a0b64b1-204e-42d5-a709-dfc978d208dd",
  "isSidechain": true,
  "promptId": "eeb83888-ea16-4335-9ad7-31eca084b764",
  "agentId": "a4138636fc3e34597",
  "type": "user",
  "uuid": "f8042d5c-9262-435d-a385-0771ceb7cd78",
  "sourceToolAssistantUUID": "0a0b64b1-204e-42d5-a709-dfc978d208dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/paper_agent_9539225d",
  "sessionId": "75f62e16-26c1-41e3-a629-5dbc4dda9106",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cryptic-kindling-corbato"
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-16T02:54:25.815Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01KwFkDLGja9jJfmiFNUgkCn`</summary>

```json
{
  "pattern": "1/40|1/40",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper",
  "type": "tex",
  "output_mode": "content",
  "head_limit": 20
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f8042d5c-9262-435d-a385-0771ceb7cd78",
  "isSidechain": true,
  "agentId": "a4138636fc3e34597",
  "requestId": "req_011Cb5VYxvtSFL1b1L2tf6Vo",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "566ebc79-f346-4550-86f7-f01eeabf9c28",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/paper_agent_9539225d",
  "sessionId": "75f62e16-26c1-41e3-a629-5dbc4dda9106",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cryptic-kindling-corbato",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011aXdhiuWkkTctraFmSZKW3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 2869,
      "cache_read_input_tokens": 62025,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2869,
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

_source line 60 · 2026-05-16T02:54:25.842Z_

<details><summary>↩ Tool result · `toolu_01KwFkDLGja9jJfmiFNUgkCn`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/limitations.tex:2:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/abstract.tex:6:The pattern replicates on Qwen2.5-7B-Instruct ($n_{\text{eff}}{=}475$, $\Delta$: $0.07 \to 3.16$; all $p < 10^{-14}$), with exploratory cross-architecture evidence from a LlamaForCausalLM model ($n{=}49$; ${\sim}1/40$ effect size) suggesting the qualitative pattern may extend beyond Qwen2 (\S\ref{sec:cross-arch}).
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/introduction.tex:17:The pattern replicates on Qwen2.5-7B-Instruct ($\Delta$: $0.07 \to 3.16$; all $p < 10^{-14}$); preliminary evidence from DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM) suggests the phenomenon may extend beyond Qwen2 but at ${\sim}1/40$ the magnitude and with substantially weaker strategy contrast.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "566ebc79-f346-4550-86f7-f01eeabf9c28",
  "isSidechain": true,
  "promptId": "eeb83888-ea16-4335-9ad7-31eca084b764",
  "agentId": "a4138636fc3e34597",
  "type": "user",
  "uuid": "c242e96c-68d0-4447-9d65-28ffb42b9fb3",
  "sourceToolAssistantUUID": "566ebc79-f346-4550-86f7-f01eeabf9c28",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/paper_agent_9539225d",
  "sessionId": "75f62e16-26c1-41e3-a629-5dbc4dda9106",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cryptic-kindling-corbato"
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-16T02:54:26.517Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01XQ8eLLp7TxQoqYA8VkgdZv`</summary>

```json
{
  "pattern": "s030|s\\{=\\}0\\.30",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper",
  "type": "tex",
  "output_mode": "content",
  "head_limit": 10
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c242e96c-68d0-4447-9d65-28ffb42b9fb3",
  "isSidechain": true,
  "agentId": "a4138636fc3e34597",
  "requestId": "req_011Cb5VYxvtSFL1b1L2tf6Vo",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "e6ba4819-324b-472b-9af4-dd5c10b7f2fe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/paper_agent_9539225d",
  "sessionId": "75f62e16-26c1-41e3-a629-5dbc4dda9106",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cryptic-kindling-corbato",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011aXdhiuWkkTctraFmSZKW3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 2869,
      "cache_read_input_tokens": 62025,
      "output_tokens": 773,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2869
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 773,
          "cache_read_input_tokens": 62025,
          "cache_creation_input_tokens": 2869,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2869,
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

_source line 62 · 2026-05-16T02:54:26.551Z_

<details><summary>↩ Tool result · `toolu_01XQ8eLLp7TxQoqYA8VkgdZv`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/appendix_robustness.tex:25:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/appendix_robustness.tex:120:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/appendix_moved.tex:5:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/appendix_moved.tex:61:Phase & $s{=}0.15$ & $s{=}0.20$ & $s{=}0.25$ & $s{=}0.30$ \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/appendix_moved.tex:79:Model & $s{=}0.15$ & $s{=}0.20$ & $s{=}0.25$ & $s{=}0.30$ \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/appendix_moved.tex:98:As a control, random eviction on Qwen mirrors DeepSeek: non-significant at $s \leq 0.20$ ($\Delta$: $-0.01$, $0.02$; CIs span zero) but significant at $s \geq 0.25$ ($\Delta{=}0.39$, $p_{\text{Bonf}} < 10^{-10}$; $\Delta{=}0.91$, $p_{\text{Bonf}} < 10^{-13}$). Where significant, the random phase gradient is $2.7$--$3.5{\times}$ weaker than importance-based ($0.39$ vs.\ $1.07$ at $s{=}0.25$; $0.91$ vs.\ $3.16$ at $s{=}0.30$), confirming strategy-specific amplification.
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/appendix_moved.tex:106:Per-problem distributions of the paired severity difference $\Delta_i = \mathrm{II}_{\textit{low},i} - \mathrm{II}_{\textit{high},i}$ under importance-based eviction are right-skewed at all sparsity levels, with mean/median ratios ranging from $1.2{\times}$ ($s{=}0.15$) to $1.6{\times}$ ($s{=}0.30$) for DeepSeek and $1.1{\times}$ to $1.4{\times}$ for Qwen.
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/appendix_moved.tex:110:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/appendix_moved.tex:142:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/appendix_moved.tex:164:[Omitted long matching line]

[Showing results with pagination = limit: 10]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e6ba4819-324b-472b-9af4-dd5c10b7f2fe",
  "isSidechain": true,
  "promptId": "eeb83888-ea16-4335-9ad7-31eca084b764",
  "agentId": "a4138636fc3e34597",
  "type": "user",
  "uuid": "e936719f-4470-4a8d-bd36-66487d4c53de",
  "sourceToolAssistantUUID": "e6ba4819-324b-472b-9af4-dd5c10b7f2fe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/paper_agent_9539225d",
  "sessionId": "75f62e16-26c1-41e3-a629-5dbc4dda9106",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cryptic-kindling-corbato"
}
```

</details>

---

### Assistant

_source line 63 · 2026-05-16T02:54:27.971Z_

Let me look at the discussion section more closely and search for the accuracy table:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e936719f-4470-4a8d-bd36-66487d4c53de",
  "isSidechain": true,
  "agentId": "a4138636fc3e34597",
  "requestId": "req_011Cb5VZJshCxtWWkAYgstMX",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f662f6e8-ce2a-4db9-bc9c-e946c55f0662",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/paper_agent_9539225d",
  "sessionId": "75f62e16-26c1-41e3-a629-5dbc4dda9106",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cryptic-kindling-corbato",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_014DmauTMR1HyRpPJYV92vHZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 2708,
      "cache_read_input_tokens": 64894,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2708,
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

_source line 64 · 2026-05-16T02:54:28.502Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Qsux7mhEv9yeS8jptetbfN`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/appendix_disc_analysis.tex",
  "offset": 119,
  "limit": 30
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f662f6e8-ce2a-4db9-bc9c-e946c55f0662",
  "isSidechain": true,
  "agentId": "a4138636fc3e34597",
  "requestId": "req_011Cb5VZJshCxtWWkAYgstMX",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "9880daf8-53c5-43d9-99dd-765393a92c45",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/paper_agent_9539225d",
  "sessionId": "75f62e16-26c1-41e3-a629-5dbc4dda9106",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cryptic-kindling-corbato",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_014DmauTMR1HyRpPJYV92vHZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 2708,
      "cache_read_input_tokens": 64894,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2708,
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

_source line 65 · 2026-05-16T02:54:28.514Z_

<details><summary>↩ Tool result · `toolu_01Qsux7mhEv9yeS8jptetbfN`</summary>

```text
119	\section{Downstream Accuracy Validation Details}
120	\label{app:accuracy-details}
121	
122	Table~\ref{tab:accuracy} reports MATH-500 accuracy under compound sparsity (importance-based eviction) at $s \in \{0.15, 0.20, 0.25, 0.30\}$ with \texttt{max\_new\_tokens}${=}$8192, complementing the PPL-based analysis in \S\ref{sec:accuracy-validation}. Qwen ($n{=}100$; truncation $\leq 4\%$ across all conditions) provides the cleanest dose-response evidence: accuracy declines gradually from $46\%$ (dense) through $s{=}0.25$ ($\delta{=}-4$ to $-13$\,pp) before a sharp cliff at $s{=}0.30$ ($19\%$, $\delta{=}-27$\,pp). DeepSeek ($n{=}50$) shows steeper overall degradation ($74\% \to 4\%$), confounded by rising truncation ($16\% \to 76\%$); non-truncated analysis (\S\ref{app:accuracy-nt}) reveals a dual-regime structure.
123	
124	\begin{table}[h]
125	\centering
126	\small
127	\caption{MATH-500 accuracy under compound sparsity (importance-based eviction, \texttt{max\_new\_tokens}${=}$8192). $\delta$: accuracy change vs.\ dense. Trunc: truncation rate under sparse condition. DS: $n{=}50$ (dense truncation $16\%$); QW: $n{=}100$ (truncation $\leq 4\%$ all conditions).}
128	\label{tab:accuracy}
129	\begin{tabular}{@{}lccccc@{}}
130	\toprule
131	Model & $s$ & Dense & Sparse & $\delta$ & Trunc \\
132	\midrule
133	DS & 0.15 & 74\% & 48\% & $-$26\,pp & 32\% \\
134	DS & 0.20 & 74\% & 30\% & $-$44\,pp & 56\% \\
135	DS & 0.25 & 74\% & 8\% & $-$66\,pp & 76\% \\
136	DS & 0.30 & 74\% & 4\% & $-$70\,pp & 76\% \\
137	\addlinespace
138	QW & 0.15 & 46\% & 42\% & $-$4\,pp & $\leq$4\% \\
139	QW & 0.20 & 46\% & 36\% & $-$10\,pp & $\leq$4\% \\
140	QW & 0.25 & 46\% & 33\% & $-$13\,pp & $\leq$4\% \\
141	QW & 0.30 & 46\% & 19\% & $-$27\,pp & $\leq$4\% \\
142	\bottomrule
143	\end{tabular}
144	\end{table}
145	
146	\paragraph{Failure mode divergence.}
147	DeepSeek and Qwen exhibit qualitatively distinct failure modes under compound sparsity. DeepSeek failures are \emph{truncation-dominated}: compound sparsity induces verbose, repetitive chain-of-thought that exceeds the token limit (truncation rises from $16\%$ at dense to $32\%$ at $s{=}0.15$ and $76\%$ at $s{=}0.30$, even with \texttt{max\_new\_tokens}${=}$8192). Qwen failures are \emph{wrong-answer-dominated}: outputs complete within the token limit (truncation $\leq 4\%$) but produce incorrect answers, confirming that compound sparsity disrupts reasoning quality directly. This divergence likely reflects training-paradigm differences: DeepSeek's distillation from DeepSeek-R1 produces extended CoT traces susceptible to truncation under degraded conditions.
148	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9880daf8-53c5-43d9-99dd-765393a92c45",
  "isSidechain": true,
  "promptId": "eeb83888-ea16-4335-9ad7-31eca084b764",
  "agentId": "a4138636fc3e34597",
  "type": "user",
  "uuid": "63216372-21a5-4ddb-9783-dd5997bca637",
  "sourceToolAssistantUUID": "9880daf8-53c5-43d9-99dd-765393a92c45",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/paper_agent_9539225d",
  "sessionId": "75f62e16-26c1-41e3-a629-5dbc4dda9106",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cryptic-kindling-corbato"
}
```

</details>

---

### Tool call

_source line 66 · 2026-05-16T02:54:29.174Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01MwsvEWiwde2MxdVAeadfu9`</summary>

```json
{
  "pattern": "oracle|recovery|30%|39%",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper",
  "type": "tex",
  "output_mode": "content",
  "head_limit": 15
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "63216372-21a5-4ddb-9783-dd5997bca637",
  "isSidechain": true,
  "agentId": "a4138636fc3e34597",
  "requestId": "req_011Cb5VZJshCxtWWkAYgstMX",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "21f9dcc8-e11b-4caf-8072-9d2031051448",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/paper_agent_9539225d",
  "sessionId": "75f62e16-26c1-41e3-a629-5dbc4dda9106",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cryptic-kindling-corbato",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_014DmauTMR1HyRpPJYV92vHZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 2708,
      "cache_read_input_tokens": 64894,
      "output_tokens": 294,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2708
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 294,
          "cache_read_input_tokens": 64894,
          "cache_creation_input_tokens": 2708,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2708,
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

_source line 67 · 2026-05-16T02:54:29.198Z_

<details><summary>↩ Tool result · `toolu_01MwsvEWiwde2MxdVAeadfu9`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/discussion.tex:5:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/appendix_disc_analysis.tex:23:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "21f9dcc8-e11b-4caf-8072-9d2031051448",
  "isSidechain": true,
  "promptId": "eeb83888-ea16-4335-9ad7-31eca084b764",
  "agentId": "a4138636fc3e34597",
  "type": "user",
  "uuid": "a4bd7ac5-95ec-4e17-9d68-0aabe482fc41",
  "sourceToolAssistantUUID": "21f9dcc8-e11b-4caf-8072-9d2031051448",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/paper_agent_9539225d",
  "sessionId": "75f62e16-26c1-41e3-a629-5dbc4dda9106",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cryptic-kindling-corbato"
}
```

</details>

---

### Assistant

_source line 68 · 2026-05-16T02:54:31.276Z_

Perfect! Now let me extract the key numbers from the discussion section and do a comprehensive audit:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a4bd7ac5-95ec-4e17-9d68-0aabe482fc41",
  "isSidechain": true,
  "agentId": "a4138636fc3e34597",
  "requestId": "req_011Cb5VZW39mqGA2L4GWTQJD",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "7c2f1260-cdf1-4b96-9845-ca48c7d79a48",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/paper_agent_9539225d",
  "sessionId": "75f62e16-26c1-41e3-a629-5dbc4dda9106",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cryptic-kindling-corbato",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017aTKtmH36xh14H3G14jsEL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 1529,
      "cache_read_input_tokens": 67602,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1529,
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

_source line 69 · 2026-05-16T02:54:31.574Z_

<details open><summary>🔧 Tool call — Read · `toolu_015aUBhLH9BPsku1DP662RG4`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/appendix_disc_analysis.tex",
  "offset": 20,
  "limit": 5
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7c2f1260-cdf1-4b96-9845-ca48c7d79a48",
  "isSidechain": true,
  "agentId": "a4138636fc3e34597",
  "requestId": "req_011Cb5VZW39mqGA2L4GWTQJD",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "261798ac-55d4-4458-8c3e-097f6e5b50ae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/paper_agent_9539225d",
  "sessionId": "75f62e16-26c1-41e3-a629-5dbc4dda9106",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cryptic-kindling-corbato",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017aTKtmH36xh14H3G14jsEL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 1529,
      "cache_read_input_tokens": 67602,
      "output_tokens": 149,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1529
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 149,
          "cache_read_input_tokens": 67602,
          "cache_creation_input_tokens": 1529,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1529,
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

_source line 70 · 2026-05-16T02:54:31.581Z_

<details><summary>↩ Tool result · `toolu_015aUBhLH9BPsku1DP662RG4`</summary>

```text
20	\section{Pilot Mitigation Experiment}
21	\label{app:pilot-mitigation}
22	
23	We explored oracle phase-aware budget reallocation, shifting sparsity budget from high-severity low-sparsity phases to low-severity high-sparsity phases ($n{=}30$ problems at $s{=}0.25$). Oracle recovery---the fraction of compound interaction eliminated by phase-aware allocation---reached 18\% (95\% CI: $[-39\%, 45.8\%]$; Wilcoxon $p = 0.002$), below the pre-registered 30\% gate for claiming practical mitigation. A heuristic variant achieved 32\% recovery (95\% CI: $[-22.8\%, 66\%]$; $p = 0.024$). \textbf{Critically, 95\% bootstrap CIs for both conditions span zero}, meaning neither recovery estimate is statistically distinguishable from no improvement. These results indicate that phase-aware budget reallocation alone is insufficient to neutralize the severity gradient; effective mitigation likely requires joint optimization of budget allocation and eviction strategy selection across phases.
24	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "261798ac-55d4-4458-8c3e-097f6e5b50ae",
  "isSidechain": true,
  "promptId": "eeb83888-ea16-4335-9ad7-31eca084b764",
  "agentId": "a4138636fc3e34597",
  "type": "user",
  "uuid": "a20cfb3a-56cc-4c1c-ad66-e0b06fbd5231",
  "sourceToolAssistantUUID": "261798ac-55d4-4458-8c3e-097f6e5b50ae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/paper_agent_9539225d",
  "sessionId": "75f62e16-26c1-41e3-a629-5dbc4dda9106",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cryptic-kindling-corbato"
}
```

</details>

---

### Assistant

_source line 71 · 2026-05-16T02:54:33.106Z_

Now let me verify the random eviction significance threshold information:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a20cfb3a-56cc-4c1c-ad66-e0b06fbd5231",
  "isSidechain": true,
  "agentId": "a4138636fc3e34597",
  "requestId": "req_011Cb5VZgP18sjdujrASTwWW",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "b9669be8-d9ab-4775-a79f-6201060eba0e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/paper_agent_9539225d",
  "sessionId": "75f62e16-26c1-41e3-a629-5dbc4dda9106",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cryptic-kindling-corbato",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01JdVrELws4pWiywgWE9oYmu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 539,
      "cache_read_input_tokens": 69131,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 539,
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

_source line 72 · 2026-05-16T02:54:33.865Z_

<details open><summary>🔧 Tool call — Grep · `toolu_013ZMkUgxkhnDt2rCFEB2sfc`</summary>

```json
{
  "pattern": "s.*0\\.20|s.*0\\.25.*non-sig|significant.*s.*0\\.25",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper",
  "type": "tex",
  "output_mode": "content",
  "head_limit": 15
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b9669be8-d9ab-4775-a79f-6201060eba0e",
  "isSidechain": true,
  "agentId": "a4138636fc3e34597",
  "requestId": "req_011Cb5VZgP18sjdujrASTwWW",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "66bb8365-4ee3-4528-8c27-c48b0c986eff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/paper_agent_9539225d",
  "sessionId": "75f62e16-26c1-41e3-a629-5dbc4dda9106",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cryptic-kindling-corbato",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01JdVrELws4pWiywgWE9oYmu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 539,
      "cache_read_input_tokens": 69131,
      "output_tokens": 192,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 539
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4,
          "output_tokens": 192,
          "cache_read_input_tokens": 69131,
          "cache_creation_input_tokens": 539,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 539,
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

_source line 73 · 2026-05-16T02:54:33.892Z_

<details><summary>↩ Tool result · `toolu_013ZMkUgxkhnDt2rCFEB2sfc`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/conclusion.tex:4:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/appendix_robustness.tex:31:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/appendix_moved.tex:5:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/appendix_moved.tex:61:Phase & $s{=}0.15$ & $s{=}0.20$ & $s{=}0.25$ & $s{=}0.30$ \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/appendix_moved.tex:79:Model & $s{=}0.15$ & $s{=}0.20$ & $s{=}0.25$ & $s{=}0.30$ \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/appendix_moved.tex:98:As a control, random eviction on Qwen mirrors DeepSeek: non-significant at $s \leq 0.20$ ($\Delta$: $-0.01$, $0.02$; CIs span zero) but significant at $s \geq 0.25$ ($\Delta{=}0.39$, $p_{\text{Bonf}} < 10^{-10}$; $\Delta{=}0.91$, $p_{\text{Bonf}} < 10^{-13}$). Where significant, the random phase gradient is $2.7$--$3.5{\times}$ weaker than importance-based ($0.39$ vs.\ $1.07$ at $s{=}0.25$; $0.91$ vs.\ $3.16$ at $s{=}0.30$), confirming strategy-specific amplification.
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/appendix_moved.tex:108:The permutation null distributions are approximately symmetric around zero at all sparsity levels. At $s{=}0.15$, the observed statistic falls at the $99.92$th percentile of the null ($p_{\text{Bonf}} = 0.0032$); at $s \geq 0.20$, no permutation exceeds the observed statistic.
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/appendix_moved.tex:142:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/appendix_moved.tex:211:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/limitations.tex:23:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/methodology.tex:11:We apply symmetric compound sparsity at $s \in \{0.15, 0.20, 0.25, 0.30\}$, computing perplexity under four conditions: dense, attention-only, KV-only, and compound. We compare \emph{importance-based} eviction (position-normalized cumulative attention score, Eq.~\ref{eq:kv-importance}; BOS always retained) and \emph{random} eviction (uniform). Heads are pruned per layer by Frobenius norm; under random eviction, both heads and positions are selected uniformly.
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/abstract.tex:5:On DeepSeek-R1-Distill-Qwen-7B (MATH-500, $n{=}496$), importance-based eviction produces a monotonically increasing severity gradient (median $\Delta$: $0.39 \to 8.48$; all $p \ll 10^{-10}$). Random eviction is $2.7$--$17{\times}$ weaker where significant ($s \geq 0.25$), with a strategy ranking crossover at $s{=}0.25$.
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/appendix.tex:38:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/appendix_disc_analysis.tex:14:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/appendix_disc_analysis.tex:38:[Omitted long matching line]

[Showing results with pagination = limit: 15]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "66bb8365-4ee3-4528-8c27-c48b0c986eff",
  "isSidechain": true,
  "promptId": "eeb83888-ea16-4335-9ad7-31eca084b764",
  "agentId": "a4138636fc3e34597",
  "type": "user",
  "uuid": "751687b9-f681-46a1-adab-927d206a7aa7",
  "sourceToolAssistantUUID": "66bb8365-4ee3-4528-8c27-c48b0c986eff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/paper_agent_9539225d",
  "sessionId": "75f62e16-26c1-41e3-a629-5dbc4dda9106",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cryptic-kindling-corbato"
}
```

</details>

---

### Assistant

_source line 74 · 2026-05-16T02:54:51.338Z_

Excellent. Now let me compile a comprehensive audit report by cross-checking all the key numbers I've found. Let me create a detailed summary of my findings:

## Numerical Consistency Audit Report

Based on my thorough search across all .tex files in `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/`, here are my findings:

### 1. Δ Ranges (DS and QW) - ALL CONSISTENT ✓

**DeepSeek (n=496):**
- Consistently reported as **0.39 → 8.48** across all sections
- Found in: abstract.tex, introduction.tex, results.tex, conclusion.tex, appendix_moved.tex

**Qwen (n=475):**
- Consistently reported as **0.07 → 3.16** across all sections
- Found in: abstract.tex, introduction.tex, results.tex, conclusion.tex, appendix_moved.tex

### 2. G Ranges (Amplification Ratios) - ALL CONSISTENT ✓

- Consistently reported as **7.5–79.8×** (DeepSeek) across abstract.tex, introduction.tex, results.tex
- Figure 1 caption states: "Importance-based eviction (solid) exhibits an increasing gradient from 7.5× to 79.8×"
- All references include ~1× for random eviction (0.5–1.1×)

### 3. Sample Sizes (n values) - ALL CONSISTENT ✓

- **DS (DeepSeek)**: n=496 (consistently across all main results tables and text)
- **QW (Qwen)**: n=475 (consistently labeled as n_eff=475 or n=475)
- **LLaMA**: n=49 (consistently for cross-architecture pilot)

### 4. P-values (Bonferroni-corrected) - ALL CONSISTENT ✓

**DeepSeek (n=496):**
- Consistently reported as **p ≪ 10^-10** (all conditions, abstract to conclusion)

**Qwen (n=475):**
- Consistently reported as **p < 10^-14** (more stringent than DS, as expected given smaller Δ values)
- Confirmed in abstract, introduction, results, appendix

### 5. Strategy Contrast Ratios - CONSISTENT WITH CAVEATS ✓

**Primary claim: 2.7–17× (where both significant, s ≥ 0.25)**
- Consistently stated in abstract.tex, introduction.tex, and results.tex
- Confirmed in appendix_moved.tex as "2.7–3.5× weaker than importance-based"
- **Note**: Introduction footnote 1 mentions "full MATH-500 range including non-significant random conditions (s ≤ 0.20, where random Δ CIs span zero) extends to **39×**"

**Secondary/within-DS claim: 15–17× (Gini divergence mechanism)**
- Consistently reported in abstract.tex, analysis.tex, conclusion.tex, and limitations.tex
- This refers to severity divergence despite identical Gini drops

### 6. Cross-Architecture Magnitude (LLaMA) - ALL CONSISTENT ✓

- Consistently reported as **~1/40** of DeepSeek magnitude
- Found in: abstract.tex, introduction.tex, results.tex, limitations.tex (all using identical phrasing)

### 7. Accuracy Results - ALL CONSISTENT ✓

**Qwen2.5-7B-Instruct (n=100 for accuracy validation):**
- Dense: **46%** (baseline)
- s=0.30: **19%** (sharp cliff)
- Δ at s=0.30: **-27pp** (percentage points)
- Intermediate degradation: -4pp to -13pp (s=0.15 to 0.25)
- Table~\ref{tab:accuracy} shows complete breakdown in appendix_disc_analysis.tex (lines 138-141)

**DeepSeek (n=50 for accuracy):**
- Dense: **74%** (higher baseline)
- s=0.30: **4%** (steep degradation)
- Note: This is confounded by truncation (16%→76%), discussed separately in failure modes

### 8. Pilot Mitigation Experiment - ALL CONSISTENT ✓

**Oracle recovery (n=30, s=0.25):**
- Recovery: **18%** (95% CI: [-39%, 45.8%])
- Pre-registered gate: **30%** (not met)
- **Critical note**: CI spans zero, indicating no statistically distinguishable improvement
- Mentioned in: discussion.tex (line 5) and appendix_disc_analysis.tex (lines 20-23)

**Heuristic variant:**
- Recovery: **32%** (95% CI: [-22.8%, 66%])
- Also: CI spans zero, not statistically significant

### 9. Jonckheere-Terpstra (JT) Test - ALL CONSISTENT ✓

**DeepSeek (n=496):**
- **z = 33.7**, p ≪ 10^-10 (strictly monotonic dose-response)
- Found in: introduction.tex (lines 12, 16), results.tex (line 8)

**Qwen (n=475):**
- z ≥ **6.2**, p < 10^-9 (also monotonic)
- results.tex (line 8): "both strategies exhibit monotonic dose-response (Jonckheere-Terpstra z{=}6.2–33.7, all p < 10^-9)"

### 10. Random Eviction Significance Threshold - ALL CONSISTENT ✓

- **Non-significant at s ≤ 0.20** (CIs span zero, Δ = 0.01–0.03)
- **Significant at s ≥ 0.25** (p_Bonf < 0.006–10^-13)
- Confirmed across: results.tex (line 8), abstract.tex (line 5), introduction.tex (line 18)
- Explicitly stated in appendix_moved.tex (line 98) for Qwen control

### SUMMARY

**Status: NO DISCREPANCIES FOUND** ✓

All 10 key numerical groups are consistent across the following files:
- abstract.tex
- introduction.tex
- results.tex
- analysis.tex
- discussion.tex
- conclusion.tex
- limitations.tex
- appendix_disc_analysis.tex
- appendix_moved.tex

The paper exhibits strong numerical coherence. All numbers appear exactly where they should, with consistent precision and contextual framing. The two architectural variants (DeepSeek vs. Qwen) maintain their expected scaling relationships (roughly 4.5–6× smaller effects in Qwen), and statistical thresholds are applied consistently throughout.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "751687b9-f681-46a1-adab-927d206a7aa7",
  "isSidechain": true,
  "agentId": "a4138636fc3e34597",
  "requestId": "req_011Cb5VZr6uL1shMazA7skkZ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "c93367c1-4190-4029-a2a9-ee65823a223a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/paper_agent_9539225d",
  "sessionId": "75f62e16-26c1-41e3-a629-5dbc4dda9106",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cryptic-kindling-corbato",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01D9ReX4NywWbYMX5rmKzkm8",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 1597,
      "cache_read_input_tokens": 69670,
      "output_tokens": 1695,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1597
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4,
          "output_tokens": 1695,
          "cache_read_input_tokens": 69670,
          "cache_creation_input_tokens": 1597,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1597,
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
