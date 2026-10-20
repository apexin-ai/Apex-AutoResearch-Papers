# Research conversation: In the file /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extende

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 24
- **Recorded user turns:** 1
- **Tool calls:** 8
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a607af18e46530ec2.jsonl`
- **Structured JSON:** [`76cc7f8dd094498a196e.json`](../../sessions/76/76cc7f8dd094498a196e.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

24 recorded events

### User

_source line 1 · 2026-05-19T06:56:47.953Z_

In the file /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex, find the section about "Code Domain Results" (likely labeled C.17 or similar). Show me the exact content of that section (about 30-50 lines around it). Also find any section about cross-scorer validation or scorer robustness in appendix_extended.tex or appendix.tex. Report the line numbers and content.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "fe30cb6b-b8ab-449c-aa9f-b880df3655f4",
  "agentId": "a607af18e46530ec2",
  "type": "user",
  "uuid": "c2e2626c-1814-4cb4-95af-2086bf077a68",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/paper_agent_e65ef40e",
  "sessionId": "952e4180-a1dd-4838-893f-04003731e881",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "frolicking-frolicking-dahl"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-19T06:56:49.541Z_

I'll search for these sections in the appendix files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c2e2626c-1814-4cb4-95af-2086bf077a68",
  "isSidechain": true,
  "agentId": "a607af18e46530ec2",
  "requestId": "req_011CbBVTxoLYNRo7Dj4sC42A",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "600b30fb-bfe5-42f5-89ee-f3dbd6c33006",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/paper_agent_e65ef40e",
  "sessionId": "952e4180-a1dd-4838-893f-04003731e881",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "frolicking-frolicking-dahl",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01GRWqfp3XaNUfioJthhkNmM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 27268,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 27268,
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

_source line 3 · 2026-05-19T06:56:49.971Z_

<details open><summary>🔧 Tool call — Glob · `toolu_018tUMkm4bfvbKPdeoARFXik`</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "600b30fb-bfe5-42f5-89ee-f3dbd6c33006",
  "isSidechain": true,
  "agentId": "a607af18e46530ec2",
  "requestId": "req_011CbBVTxoLYNRo7Dj4sC42A",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "3fe325c0-78ed-48fd-8560-be2e478a4d22",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/paper_agent_e65ef40e",
  "sessionId": "952e4180-a1dd-4838-893f-04003731e881",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "frolicking-frolicking-dahl",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01GRWqfp3XaNUfioJthhkNmM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 27268,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 27268,
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

_source line 4 · 2026-05-19T06:56:49.991Z_

<details><summary>↩ Tool result · `toolu_018tUMkm4bfvbKPdeoARFXik`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3fe325c0-78ed-48fd-8560-be2e478a4d22",
  "isSidechain": true,
  "promptId": "fe30cb6b-b8ab-449c-aa9f-b880df3655f4",
  "agentId": "a607af18e46530ec2",
  "type": "user",
  "uuid": "295e6505-e7bc-4225-be9f-577683efba2a",
  "sourceToolAssistantUUID": "3fe325c0-78ed-48fd-8560-be2e478a4d22",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/paper_agent_e65ef40e",
  "sessionId": "952e4180-a1dd-4838-893f-04003731e881",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "frolicking-frolicking-dahl"
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-19T06:56:50.484Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01GttPfRo6YU8BC9jq7kQZBy`</summary>

```json
{
  "pattern": "Code Domain Results|cross-scorer|scorer robustness",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper",
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
  "parentUuid": "295e6505-e7bc-4225-be9f-577683efba2a",
  "isSidechain": true,
  "agentId": "a607af18e46530ec2",
  "requestId": "req_011CbBVTxoLYNRo7Dj4sC42A",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "93096881-fafe-4c45-a716-2a0b1b894a4a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/paper_agent_e65ef40e",
  "sessionId": "952e4180-a1dd-4838-893f-04003731e881",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "frolicking-frolicking-dahl",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01GRWqfp3XaNUfioJthhkNmM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 27268,
      "cache_read_input_tokens": 0,
      "output_tokens": 248,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 27268
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 248,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 27268,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 27268,
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

_source line 6 · 2026-05-19T06:56:50.515Z_

<details><summary>↩ Tool result · `toolu_01GttPfRo6YU8BC9jq7kQZBy`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-1-\section{Extended Analysis and Limitations}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-2-\label{sec:extended_discussion}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-3-
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex:4:This section provides supporting tables for cross-scorer validation (Tables~\ref{tab:crossscorer}--\ref{tab:anova_crossscorer}), followed by extended limitations, ablation studies, and domain-specific analyses.
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-5-
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-6-\noindent\begin{minipage}{\columnwidth}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-7-\centering
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-71-We therefore report fold-based 95\% CIs for retrain-chain experiments, computed as $\bar{x} \pm 1.96 \cdot s / \sqrt{K}$ from the $K{=}5$ GroupKFold AUC values.
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-72-
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-73-\emph{Threshold sensitivity.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex:74:Table~\ref{tab:theta_sensitivity} reports $\Kempirical$ across $\theta \in [0.55, 0.70]$ for representative configurations including arXiv and cross-scorer conditions.
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-75-Qwen-continuation's 1v2 CI lower bound exceeds $\theta$ by only 0.2\,pp; all ten boundary comparisons yield permutation $p < 0.001$.
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-76-
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-77-\begin{table}[h]
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-78-\centering
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-79-\small
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex:80:\caption{$\Kempirical$ as a function of $\theta$ across conditions. The \textbf{domain ordering} (arXiv $>$ web $\geq$ cross-scorer) and \textbf{bounded range} ($\Kempirical{\leq}4$) are preserved across $\theta \in [0.55, 0.70]$. The headline result (web $\Kempirical{=}2$, arXiv $\Kempirical{=}3$) holds for $\theta \in [0.575, 0.625]$.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-81-\label{tab:theta_sensitivity}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-82-\resizebox{\columnwidth}{!}{%
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-83-\begin{tabular}{llcccc}
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-271-\begin{table}[h]
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-272-\centering
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-273-\small
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex:274:\caption{Bootstrap 95\% CI for arXiv cross-scorer (Pythia-1.4B) 2v3 boundary $\auc$ (10{,}000 resamples). Point estimates classify 3/4 generators as $\Kempirical{=}3$; strict CI lower-bound criterion confirms 2/4.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-275-\label{tab:arxiv_crossscorer_ci}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-276-\resizebox{\columnwidth}{!}{%
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-277-\begin{tabular}{lccc}
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-311-\label{sec:boundary_extended}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-312-
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-313-Of 9 tested model configurations on C4, 8 yield $\Kempirical{=}2$; Mistral-7B is the only sub-2 exception ($\Kempirical{=}1$; 1v2 $\auc = 0.594$, CI $[0.584, 0.603]$), validating $\theta{=}0.60$ as an effective discriminator (gap: $0.594$ vs.\ $0.611$--$0.696$).
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex:314:Mistral's cross-domain profile reinforces the domain-governed interpretation: despite $\Kempirical{=}1$ on both C4 and Wikipedia, it yields $\Kempirical{=}3$ on arXiv (1v2 $\auc = 0.820$, 2v3 $= 0.628$), and this profile persists under cross-scorer validation (Pythia-1.4B scorer: C4 $\Kempirical{=}1$, arXiv $\Kempirical{=}3$ (2v3 $\auc = 0.608$, CI $[0.593, 0.622]$)), domain lexical diversity can therefore rescue even web-text one-wash generators (Table~\ref{tab:domain_kstar}).
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-315-Larger models produce more human-like text, reducing 0v1 JSD: 0.16--0.29 at $\leq$1.5B, 0.077--0.13 at 7--14B.
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-316-However, Qwen-14B still yields $\Kempirical{=}2$ (1v2 $\auc = 0.621$, CI $[0.612, 0.630]$), with 0v1 $\auc = 0.960$ comparable to Qwen-7B ($0.964$), scale in the 1B--14B range therefore does not shift the discrimination boundary.
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-317-
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-560-\end{tabular}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-561-\end{table*}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-562-
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex:563:\subsection{Code Domain Results}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-564-\label{sec:code_domain}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-565-
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-566-\begin{table}[h]
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex-39-We measure the discrimination boundary $\Kempirical$ (the maximum depth at which adjacent generations remain distinguishable) using 15 statistical features and an OBD-LightGBM classifier.
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex-40-Across five architecture families (1B--14B), four source domains (three text, one code), and four decoding strategies at $\theta{=}0.60$ (AUC decision threshold), $\Kempirical{=}2$ for general web text (8/9 model configurations), $\Kempirical{=}1$--$2$ for code (Python, model-dependent), and $\Kempirical{=}3$ for structured academic text (arXiv).
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex-41-A single additional generation pass suffices to render first-generation synthetic web text indistinguishable from deeper synthetic content, a \emph{one-wash laundering} effect.
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex:42:Largely generator-independent statistical features, computed via a fixed reference scorer, enable 80--92\% accuracy retention among continuation-mode generators, and cross-scorer validation confirms that $\Kempirical$ is largely robust to scorer choice.
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex-43-Downstream, $\Kempirical$ characterizes discriminability boundaries that inform, but do not directly determine, filtering strategy; for web text ($\Kempirical{=}2$), binary filtering aligns with the two-level discriminability structure.
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex-44-\end{abstract}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex-45-
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex-72-[Omitted long context line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex-73-(2)~\emph{Protocol}: all main experiments use prompt-chain, which isolates text-intrinsic degradation from training dynamics; real-world contamination involves both prompting and retraining, and retrain-chain yields $\Kempirical{=}7$ (both Qwen-1.5B and Pythia-1.4B LoRA; Appendix~\ref{sec:extended_limitations}), so prompt-chain $\Kempirical$ may underestimate discriminability in mixed settings.
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex-74-(3)~\emph{Threshold}: $\Kempirical$ ranges from 2--3 at $\theta{=}0.55$ to 1 at $\theta{=}0.70$; 8/9 configurations yield $\Kempirical{=}2$ at $\theta{=}0.60$ (Mistral-7B: $\Kempirical{=}1$).
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex:75:(4)~\emph{Marginal boundary}: Qwen-continuation's 1v2 CI lower bound exceeds $\theta$ by only 0.002; cross-scorer validation drops this to $\Kempirical{=}1$ (Section~\ref{sec:transfer}). LLaMA-3.1-8B represents the most marginal $\Kempirical{=}2$ assignment, with the 1v2 CI lower bound within 0.3 percentage points of $\theta$.
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex-76-(5)~\emph{Feature set}: the 15D features yield a feature-set-specific lower bound ($\Ktheory$ may be strictly higher); neural probe $\Kempirical$ is model-dependent ($3$ for Qwen, $2$ for Pythia/OLMo).
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex-77-(6)~\emph{Segment length}: $\Kempirical{=}2$ confirmed for 128 and 256 tokens (CI lower $> \theta$); 512 tokens yields point estimate $\Kempirical{=}2$ but CI lower marginally below $\theta$ ($0.5979$); the boundary weakens at longer generation lengths.
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex-78-(7)~\emph{Curation applicability}: the filtering evaluation is validated on two architectures (Qwen2.5-1.5B-Instruct and Pythia-1.4B) with consistent strategy ordering (Appendix~\ref{sec:pythia_filtering}), though absolute improvement remains small and effect sizes diminish at lower contamination ratios (10--50\%; Appendix~\ref{sec:dose_response}).
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-57-\end{figure}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-58-
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-59-Figure~\ref{fig:kstar_theta} shows $\Kempirical$ as a function of $\theta$: web text $\Kempirical{=}2$ is stable across a 5\,pp window ($\theta \in [0.575, 0.625]$), with a gradual transition to $\Kempirical{=}3$ at $\theta{=}0.55$ (two Qwen configurations) and $\Kempirical{=}1$ at $\theta{=}0.70$.
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex:60:The domain ordering (arXiv $>$ web $\geq$ cross-scorer) is preserved across the full $\theta$ range (Table~\ref{tab:theta_sensitivity}; Figure~\ref{fig:theta_sensitivity} in Appendix shows the complete model $\times$ domain $\theta$ sensitivity).
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-61-All four decoding strategies likewise yield $\Kempirical = 2$ at $\theta{=}0.60$ (1v2 $\auc \in [0.687, 0.704]$; Table~\ref{tab:s2_decoding}).
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-62-
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-63-%% ====================================================================
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-76-
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-77-\paragraph{Cross-scorer validation.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-78-Replacing the self-scorer with Pythia-1.4B or OLMo-1B preserves feature rankings ($\rho > 0.90$; Table~\ref{tab:crossscorer}).
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex:79:$\Kempirical$ is largely robust to scorer choice: across 22 cross-scorer configurations on C4 and arXiv, $\Kempirical$ was preserved in 20 cases; the two exceptions (Qwen-cont scored by Pythia on C4, Qwen-7B cross-scored on arXiv) are borderline, with AUC within 0.002 of $\theta$.
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-80-Qwen-cont is the most scorer-sensitive continuation-mode configuration: its self-scored 1v2 CI lower bound exceeds $\theta$ by only 0.2\,pp (Table~\ref{tab:kstar_ci}), and cross-family scoring pushes it below $\theta$.
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-81-For arXiv, cross-scoring with Pythia-1.4B preserves $\Kempirical{=}3$ for three of four generators (Qwen-1.5B, LLaMA-8B, Mistral-7B; 2v3 $\auc$ range: 0.608--0.632).
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-82-Qwen-7B exhibits a borderline decrease to $\Kempirical{=}2$ (2v3 $\auc = 0.599$ vs.\ $0.626$ self-scored, $\Delta = -2.7$\,pp; 3/5 folds above $\theta$), consistent with the Qwen family's scorer sensitivity observed on C4 and Wikipedia.
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/discussion.tex-10-\begin{figure}[t]
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/discussion.tex-11-\centering
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/discussion.tex-12-\includegraphics[width=\columnwidth]{figures/fig_jsd_decay.pdf}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/discussion.tex:13:\caption{Token-level JSD between adjacent depth pairs on log scale. Blue band: min-max range across 8 C4 models (1B--14B) with $\Kempirical{=}2$; dashed purple: Mistral-7B ($\Kempirical{=}1$, cross-scorer validated); green: arXiv Pythia ($\Kempirical{=}3$); dotted red: retrain-chain ($\Kempirical{=}7$). C4 models exhibit a sharp cliff ($\lambda \approx 2.2$--$3.5$), while arXiv decays gradually ($\lambda \approx 1.0$) and retrain-chain shows no cliff ($\lambda = 0.285$).}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/discussion.tex-14-\label{fig:jsd_decay}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/discussion.tex-15-\end{figure}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/discussion.tex-16-
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/method.tex-21-  \Kempirical = \max\{k \geq 1 : \mathrm{CI}_{\mathrm{low}}(\auc_{k-1,k}) > \theta\},
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/method.tex-22-  \label{eq:kstar}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/method.tex-23-\end{equation}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/method.tex:24:where $\mathrm{CI}_{\mathrm{low}}(\auc_{k-1,k})$ is the lower bound of a 95\% bootstrap confidence interval (1{,}000 resamples\footnote{Boundary-pair results in Table~\ref{tab:kstar_ci} use 1{,}000 resamples; arXiv cross-scorer CIs (Table~\ref{tab:arxiv_crossscorer_ci}) use 10{,}000 for tighter bounds at the margin.}) over the pairwise AUC (Area Under the ROC Curve) between depths $k{-}1$ and $k$, and $\theta = 0.60$ is a post-hoc operational threshold (motivated below).
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/method.tex-25-This criterion ensures that $\Kempirical$ reflects statistically robust discriminability rather than sampling noise.
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/method.tex-26-We additionally verify that non-boundary-pair CI upper bounds fall below $\theta$ (Section~\ref{sec:kstar_boundary}).
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/method.tex-27-
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex-441-\begin{table*}[t]
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex-442-  \centering
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex-443-  \small
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex:444:  \caption{Scorer sensitivity: $\Kempirical$ under self-scoring vs.\ cross-scoring. Self-scorer uses the generator's own model family for feature extraction; cross-scorer uses alternative models (Pythia-1.4B, OLMo-1B). $\Kempirical$ agreement across scorer conditions indicates the boundary is governed by the generation process. Cross-scoring reduces $\Kempirical$ only for the most marginal self-scorer condition (Qwen-continuation).}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex-445-  \label{tab:s13_scorer_sensitivity}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex-446-  \begin{tabular}{lccccc}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex-447-    \toprule
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "93096881-fafe-4c45-a716-2a0b1b894a4a",
  "isSidechain": true,
  "promptId": "fe30cb6b-b8ab-449c-aa9f-b880df3655f4",
  "agentId": "a607af18e46530ec2",
  "type": "user",
  "uuid": "b0cf0326-5ca7-4d15-b946-642568c1eef8",
  "sourceToolAssistantUUID": "93096881-fafe-4c45-a716-2a0b1b894a4a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/paper_agent_e65ef40e",
  "sessionId": "952e4180-a1dd-4838-893f-04003731e881",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "frolicking-frolicking-dahl"
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-19T06:56:52.566Z_

Great! I found the "Code Domain Results" section. Now let me read the full content around that section to get the complete 30-50 lines.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b0cf0326-5ca7-4d15-b946-642568c1eef8",
  "isSidechain": true,
  "agentId": "a607af18e46530ec2",
  "requestId": "req_011CbBVU9qbxpe5pUXvq6PxG",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "dda02512-25b0-410b-ab9e-1946b04a97c3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/paper_agent_e65ef40e",
  "sessionId": "952e4180-a1dd-4838-893f-04003731e881",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "frolicking-frolicking-dahl",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01T9qvSo8eYf8djCn346muqf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 8354,
      "cache_read_input_tokens": 27268,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8354,
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

_source line 8 · 2026-05-19T06:56:53.073Z_

<details open><summary>🔧 Tool call — Read · `toolu_019ANZNVbZHuJEJTySEuBbf1`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex",
  "offset": 563,
  "limit": 60
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dda02512-25b0-410b-ab9e-1946b04a97c3",
  "isSidechain": true,
  "agentId": "a607af18e46530ec2",
  "requestId": "req_011CbBVU9qbxpe5pUXvq6PxG",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "554f6a61-e227-40a4-991f-8a6324421967",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/paper_agent_e65ef40e",
  "sessionId": "952e4180-a1dd-4838-893f-04003731e881",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "frolicking-frolicking-dahl",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01T9qvSo8eYf8djCn346muqf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 8354,
      "cache_read_input_tokens": 27268,
      "output_tokens": 159,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8354
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 159,
          "cache_read_input_tokens": 27268,
          "cache_creation_input_tokens": 8354,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8354,
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

_source line 9 · 2026-05-19T06:56:53.088Z_

<details><summary>↩ Tool result · `toolu_019ANZNVbZHuJEJTySEuBbf1`</summary>

```text
563	\subsection{Code Domain Results}
564	\label{sec:code_domain}
565	
566	\begin{table}[h]
567	\centering
568	\small
569	\caption{Code domain (Python, CodeSearchNet~\cite{husain2019codesearchnet}) pairwise AUC for Qwen2.5-1.5B. $\Kempirical{=}2$: 1v2 exceeds $\theta{=}0.60$; 2v3 drops to chance. JSD ratio (1v2/2v3) $= 11.7\times$, comparable to C4's cliff structure.}
570	\label{tab:code_domain_qwen}
571	\begin{tabular}{l c c c}
572	\toprule
573	Pair & AUC & 95\% CI & JSD \\
574	\midrule
575	0 vs 1 & 0.9388 & [0.929, 0.949] & 0.0814 \\
576	1 vs 2 & 0.7382 & [0.709, 0.767] & 0.0443 \\
577	2 vs 3 & 0.5300 & [0.514, 0.546] & 0.0038 \\
578	3 vs 4 & 0.5022 & [0.486, 0.518] & 0.0033 \\
579	4 vs 5 & 0.5219 & [0.510, 0.534] & 0.0030 \\
580	\midrule
581	\multicolumn{4}{l}{$\Kempirical = 2$ ($\theta = 0.60$)} \\
582	\bottomrule
583	\end{tabular}
584	\end{table}
585	
586	\begin{table}[h]
587	\centering
588	\small
589	\caption{Code domain (Python, CodeSearchNet) cross-model pairwise AUC with 5-fold cross-validated 95\% CIs. Qwen2.5-1.5B yields $\Kempirical{=}2$; Pythia-1.4B yields borderline $\Kempirical{=}1$ (1v2 CI upper $= 0.603 > \theta$). Additional models pending completion.}
590	\label{tab:code_crossmodel_kstar}
591	\begin{tabular}{l cc cc}
592	\toprule
593	 & \multicolumn{2}{c}{Qwen2.5-1.5B} & \multicolumn{2}{c}{Pythia-1.4B} \\
594	\cmidrule(lr){2-3}\cmidrule(lr){4-5}
595	 & AUC & 95\% CI & AUC & 95\% CI \\
596	\midrule
597	0v1 & .9388 & [.929,\,.949] & \textbf{.9592} & [.956,\,.963] \\
598	1v2 & \textbf{.7382} & [.709,\,.767]\rlap{$^*$} & .5983 & [.593,\,.603] \\
599	2v3 & .5300 & [.514,\,.546] & .5215 & --- \\
600	3v4 & .5022 & --- & .5152 & --- \\
601	4v5 & .5219 & --- & .5046 & --- \\
602	\midrule
603	$K^*$ & \multicolumn{2}{c}{\textbf{2}} & \multicolumn{2}{c}{1} \\
604	\bottomrule
605	\multicolumn{5}{@{}p{\linewidth}@{}}{\footnotesize $^*$Permutation $p < 0.001$. $K^*$: max $k$ where $k$v$(k{+}1)$ CI lower bound $> \theta = 0.60$ (Eq.~\ref{eq:kstar}).}
606	\end{tabular}
607	\end{table}
608	
609	\subsection{Borderline Feature Analysis}
610	\label{sec:borderline_analysis}
611	
612	To understand why Mistral-7B yields $\Kempirical{=}1$ while other C4 models yield $\Kempirical{=}2$, we compute per-feature Cohen's $d$ (depth-1 vs.\ depth-2) and LightGBM feature importances across six C4 configurations spanning the full 1v2 AUC range (0.594--0.884).
613	
614	Mistral-7B exhibits the lowest depth-0 mean surprisal (2.32 vs.\ 2.90--3.02 for other models), the scorer model therefore already finds Mistral's output highly predictable.
615	This compressed baseline limits the dynamic range available for detecting inter-generational degradation: all 15 Cohen's $d$ values are weak ($\bar{|d|} = 0.112$; Table~\ref{tab:cohens_d_full}), and no single feature exceeds 13\% of total classifier importance.
616	The borderline models (LLaMA-8B, Pythia at $T{=}1.2$) show a similar pattern at slightly higher effect sizes.
617	
618	Greedy decoding is qualitatively distinct: Pythia-greedy achieves 0.884 AUC via lexical collapse (hapax ratio $d = -1.056$, capturing 47\% of importance), a signal absent under sampling-based generation where all non-greedy models rely on surprisal variability features.
619	
620	\begin{table*}[h]
621	\centering
622	\small
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "554f6a61-e227-40a4-991f-8a6324421967",
  "isSidechain": true,
  "promptId": "fe30cb6b-b8ab-449c-aa9f-b880df3655f4",
  "agentId": "a607af18e46530ec2",
  "type": "user",
  "uuid": "ff05cd69-799d-415b-a589-76b4a17f7eff",
  "sourceToolAssistantUUID": "554f6a61-e227-40a4-991f-8a6324421967",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/paper_agent_e65ef40e",
  "sessionId": "952e4180-a1dd-4838-893f-04003731e881",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "frolicking-frolicking-dahl"
}
```

</details>

---

### Assistant

_source line 10 · 2026-05-19T06:56:54.572Z_

Perfect! Now let me get more content around the cross-scorer validation section that was mentioned in the grep results.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ff05cd69-799d-415b-a589-76b4a17f7eff",
  "isSidechain": true,
  "agentId": "a607af18e46530ec2",
  "requestId": "req_011CbBVULiCptmJvC1gqTUYy",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "9249c472-75cc-4a31-abfa-3655f0200a12",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/paper_agent_e65ef40e",
  "sessionId": "952e4180-a1dd-4838-893f-04003731e881",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "frolicking-frolicking-dahl",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01BpMHmN1hafsBV9Ktu7acHT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 1666,
      "cache_read_input_tokens": 35622,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1666,
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

_source line 11 · 2026-05-19T06:56:55.771Z_

<details open><summary>🔧 Tool call — Read · `toolu_018mjmzfa6xV2zZFZNxAywKQ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex",
  "offset": 1,
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9249c472-75cc-4a31-abfa-3655f0200a12",
  "isSidechain": true,
  "agentId": "a607af18e46530ec2",
  "requestId": "req_011CbBVULiCptmJvC1gqTUYy",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "4b4f0f25-4281-4083-aef4-47b37fe159ab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/paper_agent_e65ef40e",
  "sessionId": "952e4180-a1dd-4838-893f-04003731e881",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "frolicking-frolicking-dahl",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01BpMHmN1hafsBV9Ktu7acHT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 1666,
      "cache_read_input_tokens": 35622,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1666,
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

_source line 12 · 2026-05-19T06:56:55.785Z_

<details><summary>↩ Tool result · `toolu_018mjmzfa6xV2zZFZNxAywKQ`</summary>

```text
1	\section{Extended Analysis and Limitations}
2	\label{sec:extended_discussion}
3	
4	This section provides supporting tables for cross-scorer validation (Tables~\ref{tab:crossscorer}--\ref{tab:anova_crossscorer}), followed by extended limitations, ablation studies, and domain-specific analyses.
5	
6	\noindent\begin{minipage}{\columnwidth}
7	\centering
8	\captionof{table}{Cross-scorer validation on Qwen-generated text. Alternative scorers (Pythia-1.4B, OLMo-1B) preserve feature ranking ($\rho > 0.90$) and rewrite-mode $\Kempirical = 2$, but reduce continuation-mode $\Kempirical$ from 2 to 1.}
9	\label{tab:crossscorer}
10	\resizebox{\columnwidth}{!}{\input{tables/tab_crossscorer}}
11	\end{minipage}
12	
13	\begin{table}[h]
14	\centering
15	\small
16	\caption{Three-way ANOVA (Generator $\times$ Scorer $\times$ Depth-Pair) on per-fold pairwise $\auc$ values (Type~II SS). DV = per-fold AUC; $N{=}300$ (12 cells $\times$ 5 folds $\times$ 5 depth-pairs; 3 generators $\times$ 4 scorers). Scorer is statistically significant ($p < .001$) but has a small effect size ($\eta^2_p = 0.19$) relative to Depth-Pair ($\eta^2_p = 1.00$) and Generator ($\eta^2_p = 0.89$), indicating that scorer choice has a detectable but practically minor influence on depth discrimination (Scorer $\eta^2_p$ is approximately 5$\times$ smaller than Generator and dwarfed by Depth-Pair). Per-fold AUC values within the same generator share seed documents across folds and are not fully independent; we therefore rely on effect-size ratios rather than $p$-values for interpretation.}
17	\label{tab:anova_crossscorer}
18	\begin{tabular}{lrrrr}
19	\toprule
20	\textbf{Source} & \textbf{df} & $F$ & $p$ & $\eta^2_p$ \\
21	\midrule
22	Generator     & 2  & 926.8  & ${<}.001$  & .885 \\
23	Scorer        & 3  & 19.02  & ${<}.001$  & .192 \\
24	Depth-Pair    & 4  & 24736  & ${<}.001$  & .998 \\
25	Gen$\times$Scorer & 6 & 8.16 & ${<}.001$ & .170 \\
26	Gen$\times$Depth  & 8 & 993.7 & ${<}.001$ & .971 \\
27	Scorer$\times$Depth & 12 & 2.45 & .005 & .109 \\
28	Residual      & 240 & & & \\
29	\bottomrule
30	\end{tabular}
31	\end{table}
32	
33	\subsection{Extended Limitations}
34	\label{sec:extended_limitations}
35	
36	\emph{Prompt-chain versus retrain-chain.}
37	Both Qwen2.5-1.5B and Pythia-1.4B yield $\Kempirical{=}7$ under retrain-chain LoRA fine-tuning (Table~\ref{tab:retrain_ci}), extending detectable depth by 5 additional generations beyond prompt-chain $\Kempirical{=}2$.
38	Cumulative model-adaptation artifacts (vocabulary narrowing, repetition bias) make each retrained generation highly distinguishable.
39	The two models exhibit different decay profiles: Pythia achieves higher early-pair AUC (1v2: 0.947 vs.\ 0.897) but drops more steeply at deeper pairs (4v5: 0.691 vs.\ 0.746), yet both converge to $\Kempirical{=}7$ (6v7: Qwen 0.641, Pythia 0.634; both CI lower bounds $> \theta$).
40	This convergence despite differences in effective LoRA adaptation capacity (Pythia uses fused QKV attention with rank-16 vs.\ Qwen's separate Q/K/V projections) indicates robustness to LoRA parameterization.
41	The extended discriminability under retraining aligns with theoretical analyses of iterative retraining instability on synthetic data~\cite{bertrand2024stability, gerstgrasser2024model}, where each retraining cycle amplifies distributional artifacts beyond the text-intrinsic degradation observed in prompt-chains.
42	Extrapolating yields 7v8 $\approx 0.57 < \theta$ for both models, suggesting $\Kempirical{=}7$ is near the ceiling.
43	Prompt-chain $\Kempirical$ represents the operationally relevant boundary for data curation (text-intrinsic information loss); retrain-chain $\Kempirical$ represents the upper bound achievable via model archaeology (known training pipeline).
44	
45	\begin{table}[h]
46	\centering
47	\small
48	\caption{Retrain-chain pairwise $\auc$ with 5-fold CV 95\% CIs. Both models yield $\Kempirical{=}7$; all CI lower bounds $> \theta{=}0.60$. Retrain-chain CIs use fold-level estimates (Section~\ref{sec:retrain_ci_note}).}
49	\label{tab:retrain_ci}
50	\begin{tabular}{lcccc}
51	\toprule
52	 & \multicolumn{2}{c}{\textbf{Qwen-1.5B}} & \multicolumn{2}{c}{\textbf{Pythia-1.4B}} \\
53	\cmidrule(lr){2-3}\cmidrule(lr){4-5}
54	\textbf{Pair} & $\auc$ & 95\% CI & $\auc$ & 95\% CI \\
55	\midrule
56	0v1 & 0.9837 & $[.982,\,.985]$ & 0.9844 & $[.983,\,.986]$ \\
57	1v2 & 0.8971 & $[.895,\,.899]$ & 0.9470 & $[.942,\,.952]$ \\
58	2v3 & 0.8098 & $[.805,\,.814]$ & 0.8891 & $[.882,\,.896]$ \\
59	3v4 & 0.7600 & $[.753,\,.767]$ & 0.7999 & $[.795,\,.805]$ \\
60	4v5 & 0.7459 & $[.738,\,.754]$ & 0.6907 & $[.688,\,.693]$ \\
61	5v6 & 0.7017 & $[.696,\,.708]$ & 0.6497 & $[.643,\,.657]$ \\
62	6v7 & 0.6410 & $[.638,\,.645]$ & 0.6340 & $[.628,\,.641]$ \\
63	\bottomrule
64	\end{tabular}
65	\end{table}
66	
67	\paragraph{CI methodology note.}
68	\label{sec:retrain_ci_note}
69	The main pipeline reports bootstrap 95\% CIs (1{,}000 or 10{,}000 resamples), which are valid because each bootstrap sample preserves the GroupKFold document structure: resampling operates on documents, and all depths of a given document remain together.
70	In the retrain-chain setting, each generation's training corpus is the \emph{output} of the previous generation's fine-tuned model. This creates inter-generation dependencies that standard bootstrap resampling cannot preserve, and naive resampling would inflate AUC estimates.
71	We therefore report fold-based 95\% CIs for retrain-chain experiments, computed as $\bar{x} \pm 1.96 \cdot s / \sqrt{K}$ from the $K{=}5$ GroupKFold AUC values.
72	
73	\emph{Threshold sensitivity.}
74	Table~\ref{tab:theta_sensitivity} reports $\Kempirical$ across $\theta \in [0.55, 0.70]$ for representative configurations including arXiv and cross-scorer conditions.
75	Qwen-continuation's 1v2 CI lower bound exceeds $\theta$ by only 0.2\,pp; all ten boundary comparisons yield permutation $p < 0.001$.
76	
77	\begin{table}[h]
78	\centering
79	\small
80	\caption{$\Kempirical$ as a function of $\theta$ across conditions. The \textbf{domain ordering} (arXiv $>$ web $\geq$ cross-scorer) and \textbf{bounded range} ($\Kempirical{\leq}4$) are preserved across $\theta \in [0.55, 0.70]$. The headline result (web $\Kempirical{=}2$, arXiv $\Kempirical{=}3$) holds for $\theta \in [0.575, 0.625]$.}
81	\label{tab:theta_sensitivity}
82	\resizebox{\columnwidth}{!}{%
83	\begin{tabular}{llcccc}
84	\toprule
85	\textbf{Condition} & \textbf{Config} & $\theta{=}0.55$ & $\theta{=}0.60$ & $\theta{=}0.625$ & $\theta{=}0.70$ \\
86	\midrule
87	C4 (web) & Qwen-rw      & 3 & 2 & 2 & 1 \\
88	C4 (web) & Pythia       & 2 & 2 & 2 & 1 \\
89	C4 (web) & OLMo         & 2 & 2 & 1 & 1 \\
90	C4 (web) & Qwen-cont    & 3 & 2 & 2 & 1 \\
91	C4 (web) & Qwen-7B      & 2 & 2 & 2 & 1 \\
92	C4 (web) & Mistral-7B   & 1 & 1 & 1 & 1 \\
93	\midrule
94	arXiv    & Qwen-1.5B-base (cont.) & 4 & 3 & 3 & 2 \\
95	arXiv    & Pythia-1.4B (cont.)    & 4 & 3 & 3 & 2 \\
96	\midrule
97	Cross-scorer & Qwen-cont/Pythia-scored & 2 & 1 & 1 & 1 \\
98	Cross-scorer & Qwen-cont/OLMo-scored   & 2 & 1 & 1 & 1 \\
99	\bottomrule
100	\end{tabular}}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4b4f0f25-4281-4083-aef4-47b37fe159ab",
  "isSidechain": true,
  "promptId": "fe30cb6b-b8ab-449c-aa9f-b880df3655f4",
  "agentId": "a607af18e46530ec2",
  "type": "user",
  "uuid": "4079176d-854e-4964-becc-d4a0bd74848b",
  "sourceToolAssistantUUID": "4b4f0f25-4281-4083-aef4-47b37fe159ab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/paper_agent_e65ef40e",
  "sessionId": "952e4180-a1dd-4838-893f-04003731e881",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "frolicking-frolicking-dahl"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-19T06:56:55.991Z_

<details open><summary>🔧 Tool call — Read · `toolu_01NLGkV176A642iZowuKG4dF`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex",
  "offset": 441,
  "limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4079176d-854e-4964-becc-d4a0bd74848b",
  "isSidechain": true,
  "agentId": "a607af18e46530ec2",
  "requestId": "req_011CbBVULiCptmJvC1gqTUYy",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "a3cf8fd2-150e-4127-bc98-0674a9d73ab3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/paper_agent_e65ef40e",
  "sessionId": "952e4180-a1dd-4838-893f-04003731e881",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "frolicking-frolicking-dahl",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01BpMHmN1hafsBV9Ktu7acHT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 1666,
      "cache_read_input_tokens": 35622,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1666,
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

_source line 14 · 2026-05-19T06:56:56.002Z_

<details><summary>↩ Tool result · `toolu_01NLGkV176A642iZowuKG4dF`</summary>

```text
441	\begin{table*}[t]
442	  \centering
443	  \small
444	  \caption{Scorer sensitivity: $\Kempirical$ under self-scoring vs.\ cross-scoring. Self-scorer uses the generator's own model family for feature extraction; cross-scorer uses alternative models (Pythia-1.4B, OLMo-1B). $\Kempirical$ agreement across scorer conditions indicates the boundary is governed by the generation process. Cross-scoring reduces $\Kempirical$ only for the most marginal self-scorer condition (Qwen-continuation).}
445	  \label{tab:s13_scorer_sensitivity}
446	  \begin{tabular}{lccccc}
447	    \toprule
448	    & & \multicolumn{3}{c}{\textbf{Scorer}} & \\
449	    \cmidrule(lr){3-5}
450	    \textbf{Generator} & \textbf{Mode} & \textbf{Self} & \textbf{Pythia} & \textbf{OLMo} & \textbf{Agreement} \\
451	    \midrule
452	    Qwen-1.5B-Instruct & Rewrite      & 2 (.696) & 2 & 2 & \checkmark \\
453	    Qwen-1.5B-Instruct & Continuation & 2 (.611) & 1 & 1 & $\times$ \\
454	    Qwen-1.5B (base)   & Continuation & 2 (.626) & 2 & 2 & \checkmark \\
455	    Pythia-1.4B         & Continuation & 2 (.654) & 2 & 2 & \checkmark \\
456	    OLMo-1B             & Continuation & 2 (.615) & 2 & 2 & \checkmark \\
457	    Qwen-7B             & Continuation & 2 (.618) & 2 & 2 & \checkmark \\
458	    Mistral-7B          & Continuation & 1 (.594) & 1 & 1 & \checkmark \\
459	    \bottomrule
460	  \end{tabular}
461	\end{table*}
462	
463	\clearpage
464	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a3cf8fd2-150e-4127-bc98-0674a9d73ab3",
  "isSidechain": true,
  "promptId": "fe30cb6b-b8ab-449c-aa9f-b880df3655f4",
  "agentId": "a607af18e46530ec2",
  "type": "user",
  "uuid": "93ca3e4a-14d8-438b-85ad-2f74b098cb5e",
  "sourceToolAssistantUUID": "a3cf8fd2-150e-4127-bc98-0674a9d73ab3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/paper_agent_e65ef40e",
  "sessionId": "952e4180-a1dd-4838-893f-04003731e881",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "frolicking-frolicking-dahl"
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-19T06:56:57.610Z_

Perfect! Now let me search for any additional sections related to scorer robustness or cross-scorer analysis in both files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "93ca3e4a-14d8-438b-85ad-2f74b098cb5e",
  "isSidechain": true,
  "agentId": "a607af18e46530ec2",
  "requestId": "req_011CbBVUZGG9kyFTxa23hzkY",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "490c5984-e9c5-4e8b-9f8a-33199c86130c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/paper_agent_e65ef40e",
  "sessionId": "952e4180-a1dd-4838-893f-04003731e881",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "frolicking-frolicking-dahl",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_014C4QUSQ9b7k5NbnuYSXThS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3882,
      "cache_read_input_tokens": 37288,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3882,
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

_source line 16 · 2026-05-19T06:56:58.734Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01EYkAmRuPWnjMeqWAq8gCtA`</summary>

```json
{
  "pattern": "section\\{|subsection\\{.*[Ss]corer|section\\{.*[Cc]ross",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper",
  "type": "tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "490c5984-e9c5-4e8b-9f8a-33199c86130c",
  "isSidechain": true,
  "agentId": "a607af18e46530ec2",
  "requestId": "req_011CbBVUZGG9kyFTxa23hzkY",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "7f27a59b-6d45-44dc-89e9-1224b8ca58d4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/paper_agent_e65ef40e",
  "sessionId": "952e4180-a1dd-4838-893f-04003731e881",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "frolicking-frolicking-dahl",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_014C4QUSQ9b7k5NbnuYSXThS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3882,
      "cache_read_input_tokens": 37288,
      "output_tokens": 186,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3882
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 186,
          "cache_read_input_tokens": 37288,
          "cache_creation_input_tokens": 3882,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3882,
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

_source line 17 · 2026-05-19T06:56:58.764Z_

<details><summary>↩ Tool result · `toolu_01EYkAmRuPWnjMeqWAq8gCtA`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/related_work.tex:1:\section{Related Work}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c3.tex:1:\section{Downstream Filtering Validation}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/acl.sty:234:\def\section{\@startsection {section}{1}{\z@}{-2.0ex plus
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/acl.sty:236:\def\subsection{\@startsection{subsection}{2}{\z@}{-1.8ex plus
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/acl.sty:239:\def\subsubsection{\@startsection{subsubsection}{3}{\z@}{-1.5ex plus
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/acl.sty:241:\def\paragraph{\@startsection{paragraph}{4}{\z@}{1.5ex plus
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/acl.sty:243:\def\subparagraph{\@startsection{subparagraph}{5}{\parindent}{1.5ex plus
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex:1:\section{Extended Analysis and Limitations}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex:33:\subsection{Extended Limitations}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex:123:\subsection{Dose-Response: Contamination Ratio Effect}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex:154:\subsection{Cross-Model Filtering Replication}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex:179:\subsection{Feature Subset Stability}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex:205:\subsection{self\_BLEU Feature Independence}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex:231:\subsection{Wikipedia Domain: Scorer Confound Resolution}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex:268:\subsection{ArXiv Cross-Scorer Bootstrap CIs}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex:289:\subsection{JSD Decay Analysis}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex:310:\subsection{Boundary Cases and Scale Effect}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex:322:\subsection{LaTeX Markup Ablation (arXiv)}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex:350:\subsection{Statistical Power Analysis}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex:385:\subsection{Feature Group Ablation}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex:424:\subsection{Classifier Choice: McNemar Test}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex:466:\subsection{Domain Lexical Statistics}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex:505:\subsection{Leave-One-Family-Out Threshold Validation}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex:563:\subsection{Code Domain Results}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex:609:\subsection{Borderline Feature Analysis}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/conclusion.tex:1:\section{Conclusion}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex:1:\section{Experiments}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex:9:\subsection{\texorpdfstring{$\Kempirical \leq 2$}{K*<=2} Across Model Configurations (C4)}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex:64:\subsection{Largely Generator-Independent Transfer}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex:87:\subsection{Feature Ordering and Generation Mode}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex:98:\subsection{Neural Probe}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex:122:\subsection{Cross-Domain Variation}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex:171:\subsection{Binary Detector Confidence}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/discussion.tex:1:\section{Discussion}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/method.tex:1:\section{Method}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/method.tex:11:\subsection{Problem Formulation}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/method.tex:38:\subsection{Features and Classifier}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/method.tex:50:\subsection{Experimental Setup}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex:2:\section{Supplementary Figures}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex:18:\section{Supplementary Tables}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/introduction.tex:1:\section{Introduction}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7f27a59b-6d45-44dc-89e9-1224b8ca58d4",
  "isSidechain": true,
  "promptId": "fe30cb6b-b8ab-449c-aa9f-b880df3655f4",
  "agentId": "a607af18e46530ec2",
  "type": "user",
  "uuid": "343269de-3b06-44c0-84a6-cb9edcaf23ee",
  "sourceToolAssistantUUID": "7f27a59b-6d45-44dc-89e9-1224b8ca58d4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/paper_agent_e65ef40e",
  "sessionId": "952e4180-a1dd-4838-893f-04003731e881",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "frolicking-frolicking-dahl"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-19T06:57:00.601Z_

Excellent! I found the "ArXiv Cross-Scorer Bootstrap CIs" section. Let me read that section as well.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "343269de-3b06-44c0-84a6-cb9edcaf23ee",
  "isSidechain": true,
  "agentId": "a607af18e46530ec2",
  "requestId": "req_011CbBVUkyDcij35C5fmmA6u",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "22d8e411-f2a7-4cb6-b62b-f9b88d4acab0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/paper_agent_e65ef40e",
  "sessionId": "952e4180-a1dd-4838-893f-04003731e881",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "frolicking-frolicking-dahl",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01RRs6FzabaBApqe1M7zSWsC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 2507,
      "cache_read_input_tokens": 41170,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2507,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
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

_source line 19 · 2026-05-19T06:57:01.019Z_

<details open><summary>🔧 Tool call — Read · `toolu_01PLVHewnEpnxmP2Jyg4x95E`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex",
  "offset": 268,
  "limit": 35
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "22d8e411-f2a7-4cb6-b62b-f9b88d4acab0",
  "isSidechain": true,
  "agentId": "a607af18e46530ec2",
  "requestId": "req_011CbBVUkyDcij35C5fmmA6u",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "a3ca6bce-c77b-46e9-928e-b3dd241abaf1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/paper_agent_e65ef40e",
  "sessionId": "952e4180-a1dd-4838-893f-04003731e881",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "frolicking-frolicking-dahl",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01RRs6FzabaBApqe1M7zSWsC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 2507,
      "cache_read_input_tokens": 41170,
      "output_tokens": 154,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2507
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 154,
          "cache_read_input_tokens": 41170,
          "cache_creation_input_tokens": 2507,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2507,
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

_source line 20 · 2026-05-19T06:57:01.144Z_

<details><summary>↩ Tool result · `toolu_01PLVHewnEpnxmP2Jyg4x95E`</summary>

```text
268	\subsection{ArXiv Cross-Scorer Bootstrap CIs}
269	\label{sec:arxiv_crossscorer_ci}
270	
271	\begin{table}[h]
272	\centering
273	\small
274	\caption{Bootstrap 95\% CI for arXiv cross-scorer (Pythia-1.4B) 2v3 boundary $\auc$ (10{,}000 resamples). Point estimates classify 3/4 generators as $\Kempirical{=}3$; strict CI lower-bound criterion confirms 2/4.}
275	\label{tab:arxiv_crossscorer_ci}
276	\resizebox{\columnwidth}{!}{%
277	\begin{tabular}{lccc}
278	\toprule
279	\textbf{Generator} & \textbf{2v3 $\auc$} & \textbf{95\% CI} & \textbf{CI lower $> \theta$} \\
280	\midrule
281	Qwen-1.5B    & 0.632 & $[0.617,\,0.646]$ & Yes \\
282	LLaMA-3.1-8B & 0.620 & $[0.605,\,0.636]$ & Yes (0.5\,pp margin) \\
283	Mistral-7B   & 0.608 & $[0.593,\,0.622]$ & No \\
284	Qwen-7B      & 0.599 & $[0.584,\,0.613]$ & No \\
285	\bottomrule
286	\end{tabular}}
287	\end{table}
288	
289	\subsection{JSD Decay Analysis}
290	\label{sec:jsd_extended}
291	
292	The token-level JSD between adjacent generations reveals two distinct decay regimes (Figure~\ref{fig:jsd_decay}).
293	For C4 web text, 0v1 JSD exceeds 1v2 by 6--56$\times$ across all 8 models (1B--14B) with $\Kempirical{=}2$ (median cliff ratio ${\sim}$15$\times$), and subsequent pairs converge to a noise floor of ${\sim}$0.003--0.005.
294	Fitting $\jsd(k, k{+}1) \propto e^{-\lambda k}$ yields $\lambda \approx 2.2$--$3.5$ for C4 (mean ${\approx}\,2.9$), consistent with rapid mixing of $G_\delta$ toward its stationary distribution.
295	These decay rates represent qualitative characterizations from 5-point curves rather than precise estimates.
296	The empirical decay rate $\lambda$ is consistent within each domain but varies across domains: C4 yields $\lambda \approx 2.9$, Wikipedia $\lambda \approx 3.1$ (excluding OLMo, whose $\lambda = 6.3$ reflects a capacity-limited collapse: 0v1 $\jsd = 0.169$ with near-complete information loss at the first step, the exponential fit is therefore unreliable), and arXiv $\lambda \approx 1.0$.
297	This cross-model consistency indicates that the contraction rate of $G_\delta$ is governed primarily by the structure of the input domain rather than the model architecture.
298	ArXiv text decays ${\sim}$3$\times$ slower than C4 ($\lambda \approx 1.0$ vs.\ $2.9$), with a correspondingly higher convergence floor (${\sim}$0.007--0.009 vs.\ ${\sim}$0.003--0.004).
299	Formulaic structural features (LaTeX formatting, citation patterns, section templates) degrade more slowly under autoregressive generation and supply persistent depth-distinguishing signal, this accounts for the elevated $\Kempirical{=}3$.
300	The retrain-chain exhibits a fundamentally different profile: $\lambda = 0.285$ with a cliff ratio of only 1.31$\times$ and no sharp drop between adjacent pairs (Figure~\ref{fig:retrain_decay}).
301	This gradual, sustained divergence reflects cumulative model-adaptation artifacts rather than text-intrinsic information loss, further supporting the distinction between prompt-chain and retrain-chain $\Kempirical$ (Appendix~\ref{sec:boundary_extended}).
302	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a3ca6bce-c77b-46e9-928e-b3dd241abaf1",
  "isSidechain": true,
  "promptId": "fe30cb6b-b8ab-449c-aa9f-b880df3655f4",
  "agentId": "a607af18e46530ec2",
  "type": "user",
  "uuid": "05ddd853-382c-472c-87e5-0b30718cb707",
  "sourceToolAssistantUUID": "a3ca6bce-c77b-46e9-928e-b3dd241abaf1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/paper_agent_e65ef40e",
  "sessionId": "952e4180-a1dd-4838-893f-04003731e881",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "frolicking-frolicking-dahl"
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-19T06:57:02.896Z_

Perfect! Now let me get the content from the main paper about cross-scorer validation to provide complete context.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "05ddd853-382c-472c-87e5-0b30718cb707",
  "isSidechain": true,
  "agentId": "a607af18e46530ec2",
  "requestId": "req_011CbBVUwF6k1AhF44DpkQb9",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "dbdef3f2-c3e8-4826-b1f6-08defc08e5bf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/paper_agent_e65ef40e",
  "sessionId": "952e4180-a1dd-4838-893f-04003731e881",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "frolicking-frolicking-dahl",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_018Fu4UKs5uxoVp2DvSuGwQ6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1277,
      "cache_read_input_tokens": 43677,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1277,
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

_source line 22 · 2026-05-19T06:57:03.735Z_

<details open><summary>🔧 Tool call — Read · `toolu_01MsJFmhs2j6iMigDuto1iYG`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex",
  "offset": 77,
  "limit": 25
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dbdef3f2-c3e8-4826-b1f6-08defc08e5bf",
  "isSidechain": true,
  "agentId": "a607af18e46530ec2",
  "requestId": "req_011CbBVUwF6k1AhF44DpkQb9",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "e0471493-62aa-4bd8-ba3d-c00628589dc2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/paper_agent_e65ef40e",
  "sessionId": "952e4180-a1dd-4838-893f-04003731e881",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "frolicking-frolicking-dahl",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_018Fu4UKs5uxoVp2DvSuGwQ6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1277,
      "cache_read_input_tokens": 43677,
      "output_tokens": 148,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1277
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 148,
          "cache_read_input_tokens": 43677,
          "cache_creation_input_tokens": 1277,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1277,
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

_source line 23 · 2026-05-19T06:57:03.743Z_

<details><summary>↩ Tool result · `toolu_01MsJFmhs2j6iMigDuto1iYG`</summary>

```text
77	\paragraph{Cross-scorer validation.}
78	Replacing the self-scorer with Pythia-1.4B or OLMo-1B preserves feature rankings ($\rho > 0.90$; Table~\ref{tab:crossscorer}).
79	$\Kempirical$ is largely robust to scorer choice: across 22 cross-scorer configurations on C4 and arXiv, $\Kempirical$ was preserved in 20 cases; the two exceptions (Qwen-cont scored by Pythia on C4, Qwen-7B cross-scored on arXiv) are borderline, with AUC within 0.002 of $\theta$.
80	Qwen-cont is the most scorer-sensitive continuation-mode configuration: its self-scored 1v2 CI lower bound exceeds $\theta$ by only 0.2\,pp (Table~\ref{tab:kstar_ci}), and cross-family scoring pushes it below $\theta$.
81	For arXiv, cross-scoring with Pythia-1.4B preserves $\Kempirical{=}3$ for three of four generators (Qwen-1.5B, LLaMA-8B, Mistral-7B; 2v3 $\auc$ range: 0.608--0.632).
82	Qwen-7B exhibits a borderline decrease to $\Kempirical{=}2$ (2v3 $\auc = 0.599$ vs.\ $0.626$ self-scored, $\Delta = -2.7$\,pp; 3/5 folds above $\theta$), consistent with the Qwen family's scorer sensitivity observed on C4 and Wikipedia.
83	Bootstrap CIs (10{,}000 resamples) confirm $\Kempirical{=}3$ for Qwen-1.5B (CI lower $= 0.617$) and LLaMA-8B (CI lower $= 0.605$); for Mistral-7B (CI: $[0.593, 0.622]$) and Qwen-7B (CI: $[0.584, 0.613]$), the CI straddles $\theta$; their $\Kempirical{=}3$ assignment is sensitive to resampling variance (Table~\ref{tab:arxiv_crossscorer_ci}).
84	A three-way ANOVA (Generator $\times$ Scorer $\times$ Depth-Pair; $N{=}300$; Table~\ref{tab:anova_crossscorer}) confirms that Depth-Pair dominates variance ($\eta^2_p = 0.998$); Scorer is statistically significant ($p < .001$) but practically minor ($\eta^2_p = 0.192$), consistent with a detectable but small scorer influence on absolute discriminability.
85	
86	%% ====================================================================
87	\subsection{Feature Ordering and Generation Mode}
88	\label{sec:feature_degradation}
89	\label{sec:generation_mode}
90	
91	Among continuation-mode models, single-feature $\auc$ rankings are highly correlated ($\rho \geq 0.85$; Table~\ref{tab:top_features}).
92	The top-3 features (\texttt{surp\_d1\_std}, \texttt{surp\_std}, \texttt{surp\_d2\_std}) are shared across all three families: autoregressive generation progressively damps surprisal variability; however, no single feature subset of size ${<}8$ reliably sustains $\Kempirical{=}2$ (Appendix~\ref{sec:feature_subset}).
93	A feature group ablation (Appendix~\ref{sec:feature_ablation}) confirms that surprisal (base) dominates on arXiv (single AUC $= 0.809$, LOO $\Delta = 0.031$); on C4 and Wikipedia, all LOO drops fall within fold variance ($\leq 0.007$).
94	Qwen-rewrite diverges (\texttt{freq\_entropy} dominates), consistent with its poor cross-model transfer (61--63\%).
95	Within Qwen, rewrite yields 1v2 $\auc = 0.6955$ vs.\ continuation's $0.6112$ ($\Delta = +8.4$\,pp); continuation mode is therefore recommended as the canonical condition.
96	
97	%% ====================================================================
98	\subsection{Neural Probe}
99	\label{sec:neural_probe}
100	
101	Replacing the 15D features with frozen encoder hidden states (MLP probe, 5{,}000 texts per depth; Table~\ref{tab:neural_probe_crossmodel}), Qwen achieves $\Kempirical^{\text{neural}} = 3$ (2v3 $\auc = 0.6159$), while Pythia and OLMo remain at $\Kempirical^{\text{neural}} = 2$ ($\auc_{2v3}$: 0.5963, 0.5892).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e0471493-62aa-4bd8-ba3d-c00628589dc2",
  "isSidechain": true,
  "promptId": "fe30cb6b-b8ab-449c-aa9f-b880df3655f4",
  "agentId": "a607af18e46530ec2",
  "type": "user",
  "uuid": "4a24f718-02c1-4d5d-a76f-308288e59ae4",
  "sourceToolAssistantUUID": "e0471493-62aa-4bd8-ba3d-c00628589dc2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/paper_agent_e65ef40e",
  "sessionId": "952e4180-a1dd-4838-893f-04003731e881",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "frolicking-frolicking-dahl"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-19T06:57:18.663Z_

Excellent! Now I have comprehensive information. Let me compile my findings.

## Summary of Findings

I've located and extracted the requested sections from your paper. Here are the exact locations and content:

### 1. **Code Domain Results** (Section C.18)
**Location:** `/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex`, lines 563-607

**Content (45 lines):**
```
\subsection{Code Domain Results}
\label{sec:code_domain}

\begin{table}[h]
\centering
\small
\caption{Code domain (Python, CodeSearchNet~\cite{husain2019codesearchnet}) pairwise AUC for Qwen2.5-1.5B. $\Kempirical{=}2$: 1v2 exceeds $\theta{=}0.60$; 2v3 drops to chance. JSD ratio (1v2/2v3) $= 11.7\times$, comparable to C4's cliff structure.}
\label{tab:code_domain_qwen}
\begin{tabular}{l c c c}
\toprule
Pair & AUC & 95\% CI & JSD \\
\midrule
0 vs 1 & 0.9388 & [0.929, 0.949] & 0.0814 \\
1 vs 2 & 0.7382 & [0.709, 0.767] & 0.0443 \\
2 vs 3 & 0.5300 & [0.514, 0.546] & 0.0038 \\
3 vs 4 & 0.5022 & [0.486, 0.518] & 0.0033 \\
4 vs 5 & 0.5219 & [0.510, 0.534] & 0.0030 \\
\midrule
\multicolumn{4}{l}{$\Kempirical = 2$ ($\theta = 0.60$)} \\
\bottomrule
\end{tabular}
\end{table}

\begin{table}[h]
\centering
\small
\caption{Code domain (Python, CodeSearchNet) cross-model pairwise AUC with 5-fold cross-validated 95\% CIs. Qwen2.5-1.5B yields $\Kempirical{=}2$; Pythia-1.4B yields borderline $\Kempirical{=}1$ (1v2 CI upper $= 0.603 > \theta$). Additional models pending completion.}
\label{tab:code_crossmodel_kstar}
\begin{tabular}{l cc cc}
\toprule
 & \multicolumn{2}{c}{Qwen2.5-1.5B} & \multicolumn{2}{c}{Pythia-1.4B} \\
\cmidrule(lr){2-3}\cmidrule(lr){4-5}
 & AUC & 95\% CI & AUC & 95\% CI \\
\midrule
0v1 & .9388 & [.929,\,.949] & \textbf{.9592} & [.956,\,.963] \\
1v2 & \textbf{.7382} & [.709,\,.767]\rlap{$^*$} & .5983 & [.593,\,.603] \\
2v3 & .5300 & [.514,\,.546] & .5215 & --- \\
3v4 & .5022 & --- & .5152 & --- \\
4v5 & .5219 & --- & .5046 & --- \\
\midrule
$K^*$ & \multicolumn{2}{c}{\textbf{2}} & \multicolumn{2}{c}{1} \\
\bottomrule
\multicolumn{5}{@{}p{\linewidth}@{}}{\footnotesize $^*$Permutation $p < 0.001$. $K^*$: max $k$ where $k$v$(k{+}1)$ CI lower bound $> \theta = 0.60$ (Eq.~\ref{eq:kstar}).}
\end{tabular}
\end{table}
```

### 2. **Cross-Scorer Validation and Robustness Sections**

**A) Main paper section (experiments_c1.tex, lines 77-85):** Paragraph titled "Cross-scorer validation" with comprehensive results about scorer robustness across 22 configurations.

**B) Appendix cross-scorer validation tables:**

- **appendix_extended.tex, lines 1-31** - Opening section with inline table reference to `tab:crossscorer` and ANOVA analysis table `tab:anova_crossscorer`
- **appendix_extended.tex, lines 74-100** - Threshold sensitivity section (line 74) showing cross-scorer conditions are preserved across θ ∈ [0.55, 0.70]
- **appendix_extended.tex, lines 268-287** - **"ArXiv Cross-Scorer Bootstrap CIs"** (Section C.9) with Table tab:arxiv_crossscorer_ci showing 10,000-resample bootstrap CIs for Pythia-1.4B scorer on arXiv
- **appendix.tex, lines 441-461** - **Table tab:s13_scorer_sensitivity** showing $\Kempirical$ under self-scoring vs. cross-scoring with Pythia-1.4B and OLMo-1B

**Key Findings on Scorer Robustness:**
- 20 out of 22 cross-scorer configurations preserve $\Kempirical$
- Only 2 exceptions are borderline (Qwen-cont on C4 and Qwen-7B on arXiv), both with AUC within 0.002 of θ
- ANOVA shows scorer is statistically significant (p<0.001) but practically minor (η²p = 0.192 vs. Depth-Pair η²p = 0.998)
- Feature rankings highly preserved across scorers (ρ > 0.90)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4a24f718-02c1-4d5d-a76f-308288e59ae4",
  "isSidechain": true,
  "agentId": "a607af18e46530ec2",
  "requestId": "req_011CbBVV8L6ZAszGsqYzdD6v",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "8db219bc-8d13-46aa-bc06-76df8ab1bf86",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/paper_agent_e65ef40e",
  "sessionId": "952e4180-a1dd-4838-893f-04003731e881",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "frolicking-frolicking-dahl",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01NUqMQ8e3TpRonyiGvq5CVz",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1417,
      "cache_read_input_tokens": 44954,
      "output_tokens": 1565,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1417
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 1565,
          "cache_read_input_tokens": 44954,
          "cache_creation_input_tokens": 1417,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1417,
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
