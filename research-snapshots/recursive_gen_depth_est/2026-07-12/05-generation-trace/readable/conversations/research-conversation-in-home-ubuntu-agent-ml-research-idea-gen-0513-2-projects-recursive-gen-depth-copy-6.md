# Research conversation: In /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/, search for any sections

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 18
- **Recorded user turns:** 1
- **Tool calls:** 7
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a1343616d299e436c.jsonl`
- **Structured JSON:** [`46e794b2ffe8480d5652.json`](../../sessions/46/46e794b2ffe8480d5652.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

18 recorded events

### User

_source line 1 · 2026-05-15T23:42:04.992Z_

In /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/, search for any sections related to "curation" or "downstream" or "finetune" or "plan_013". Check all .tex files. I want to know if there's already a written section about the curation PoC experiment, and if so, what claims it makes. Report exact file paths and relevant content.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "b2d7dae8-7507-4c58-8d2e-f1f015a52cc1",
  "agentId": "a1343616d299e436c",
  "type": "user",
  "uuid": "5cff66f3-2593-4b55-9394-63b7d73eaaec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/reviewer_2647e3b4",
  "sessionId": "2e338b7d-5485-4031-acd3-bb1b0bb547ae",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-15T23:42:06.139Z_

I'll search through the .tex files in that directory for sections related to your specified keywords.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5cff66f3-2593-4b55-9394-63b7d73eaaec",
  "isSidechain": true,
  "agentId": "a1343616d299e436c",
  "requestId": "req_011Cb5EtXZiHUSat3Me6TxU8",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "157aa4ca-cf68-4939-9ef5-359a786c31cc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/reviewer_2647e3b4",
  "sessionId": "2e338b7d-5485-4031-acd3-bb1b0bb547ae",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HbdCUfHKg8UzdFtQTY5bxo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 529,
      "cache_read_input_tokens": 17818,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 529,
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

_source line 3 · 2026-05-15T23:42:06.383Z_

<details open><summary>🔧 Tool call — Glob · `toolu_018pfEvi6KJX1WJ45zbw8cZb`</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "157aa4ca-cf68-4939-9ef5-359a786c31cc",
  "isSidechain": true,
  "agentId": "a1343616d299e436c",
  "requestId": "req_011Cb5EtXZiHUSat3Me6TxU8",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f3d8fed4-32e9-462c-8e0a-e8daee1ec93a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/reviewer_2647e3b4",
  "sessionId": "2e338b7d-5485-4031-acd3-bb1b0bb547ae",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HbdCUfHKg8UzdFtQTY5bxo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 529,
      "cache_read_input_tokens": 17818,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 529,
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

_source line 4 · 2026-05-15T23:42:06.395Z_

<details><summary>↩ Tool result · `toolu_018pfEvi6KJX1WJ45zbw8cZb`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/generalization.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/related_work.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f3d8fed4-32e9-462c-8e0a-e8daee1ec93a",
  "isSidechain": true,
  "promptId": "b2d7dae8-7507-4c58-8d2e-f1f015a52cc1",
  "agentId": "a1343616d299e436c",
  "type": "user",
  "uuid": "264c1d60-65e2-4444-b2c3-51f5fef34bba",
  "sourceToolAssistantUUID": "f3d8fed4-32e9-462c-8e0a-e8daee1ec93a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/reviewer_2647e3b4",
  "sessionId": "2e338b7d-5485-4031-acd3-bb1b0bb547ae",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-15T23:42:06.878Z_

<details open><summary>🔧 Tool call — Grep · `toolu_0149W8EPU4iN12gCwBqA35Yu`</summary>

```json
{
  "pattern": "curation|downstream|finetune|plan_013",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper",
  "type": "tex",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "264c1d60-65e2-4444-b2c3-51f5fef34bba",
  "isSidechain": true,
  "agentId": "a1343616d299e436c",
  "requestId": "req_011Cb5EtXZiHUSat3Me6TxU8",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "41becef7-0122-4e87-b257-685c8842595c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/reviewer_2647e3b4",
  "sessionId": "2e338b7d-5485-4031-acd3-bb1b0bb547ae",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HbdCUfHKg8UzdFtQTY5bxo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 529,
      "cache_read_input_tokens": 17818,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 529,
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

_source line 6 · 2026-05-15T23:42:06.899Z_

<details><summary>↩ Tool result · `toolu_0149W8EPU4iN12gCwBqA35Yu`</summary>

```text
Found 5 files
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/generalization.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/method.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "41becef7-0122-4e87-b257-685c8842595c",
  "isSidechain": true,
  "promptId": "b2d7dae8-7507-4c58-8d2e-f1f015a52cc1",
  "agentId": "a1343616d299e436c",
  "type": "user",
  "uuid": "c32ae6eb-7def-468d-850d-49ca67f1196f",
  "sourceToolAssistantUUID": "41becef7-0122-4e87-b257-685c8842595c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/reviewer_2647e3b4",
  "sessionId": "2e338b7d-5485-4031-acd3-bb1b0bb547ae",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-15T23:42:08.199Z_

Now let me read the files that contain matches to see the exact content and context:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c32ae6eb-7def-468d-850d-49ca67f1196f",
  "isSidechain": true,
  "agentId": "a1343616d299e436c",
  "requestId": "req_011Cb5EtgRmb8tyvukFgcVzA",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "fe21610e-b902-4b5b-bb98-f605f9f98333",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/reviewer_2647e3b4",
  "sessionId": "2e338b7d-5485-4031-acd3-bb1b0bb547ae",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01BLnshzsxF8DRPeU44oNUXB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1718,
      "cache_read_input_tokens": 18347,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1718,
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

_source line 8 · 2026-05-15T23:42:08.655Z_

<details open><summary>🔧 Tool call — Read · `toolu_01DPC6kTaxND3mxpsErva9T6`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fe21610e-b902-4b5b-bb98-f605f9f98333",
  "isSidechain": true,
  "agentId": "a1343616d299e436c",
  "requestId": "req_011Cb5EtgRmb8tyvukFgcVzA",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "69c9b186-d25b-44c3-8b8c-403393c9591c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/reviewer_2647e3b4",
  "sessionId": "2e338b7d-5485-4031-acd3-bb1b0bb547ae",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01BLnshzsxF8DRPeU44oNUXB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1718,
      "cache_read_input_tokens": 18347,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1718,
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

_source line 9 · 2026-05-15T23:42:08.661Z_

<details><summary>↩ Tool result · `toolu_01DPC6kTaxND3mxpsErva9T6`</summary>

```text
1	\section{Discussion and Conclusion}
2	\label{sec:discussion}
3	
4	We formalized recursive generation depth estimation and showed that a compact feature set dominated by perplexity tail statistics achieves 70--85\% four-class accuracy ($\mathrm{EDD}_{0.75}{=}4$), with five features sufficing for 97.6\% of full performance and classifier-agnostic convergence within $\leq$0.4pp.
5	The dominant pair (\texttt{p90\_ppl} top-2 in 9/9 cells, \texttt{var\_surprisal} in 8/9 under SHAP) generalizes across model families without retraining, making depth estimation a measurable early warning for model collapse~\cite{shumailov2024_nature}.
6	Recent work corroborates this connection, identifying entropy decline as a measurable signal of recursive degradation that parallels the tail erosion our features capture~\cite{shi2025_closer_look}.
7	
8	Cross-strategy transfer remains the primary bottleneck (59.1\% vs.\ 66.4\% cross-model), with the temperature-induced d1/d2 AUC inversion making single-classifier deployment across unknown decoding strategies infeasible.
9	A two-stage pipeline---first identifying the decoding strategy, then applying a strategy-conditioned depth classifier---could address this, though automating strategy identification from text alone requires independent validation.
10	
11	\paragraph{Depth-graduated data curation.}
12	Current data curation operates on a binary human-vs-machine distinction~\cite{dsir2023,qurating2024}.
13	Depth estimation enables a finer-grained alternative: retain low-depth generations (d1) whose distributional properties remain close to the human source, while down-weighting or filtering high-depth text (d3+) where tail erosion has degraded quality.
14	The 70--85\% in-distribution accuracy and $\mathrm{EDD}_{0.75}{=}4$ suggest depth-graduated filtering is feasible within known model--strategy configurations, though the d1/d2 boundary inversion under cross-strategy transfer (\S\ref{sec:gen:crossstrategy}) means reliable curation requires either known decoding metadata or an upstream strategy-identification step.
15	Importance weighting~\cite{sugiyama2007_importance_weighting} could further enable continuous depth-aware data selection rather than discrete thresholding, and verification-guided retraining offers a complementary mitigation path~\cite{yi2026_escaping_collapse}.
16	The downstream effect on training quality remains to be validated empirically.
17	
18	\paragraph{Toward a provenance toolkit.}
19	Depth estimation complements existing provenance methods along orthogonal axes.
20	Watermarking~\cite{kirchenbauer2023_watermark} provides high-confidence attribution when the generator cooperates but is inapplicable to unwatermarked text.
21	Source attribution~\cite{uchendu2020_attribution} identifies the generating model but not the generation history.
22	Bevendorff et al.\ distinguish attribution from verification as two fundamental detection paradigms~\cite{bevendorff2025_two_paradigms}; depth estimation represents a complementary third axis that characterizes \emph{iterative reuse} regardless of generator cooperation or identity.
23	A layered provenance system combining watermark presence, source model, and recursive depth could support more nuanced data auditing than any single method.
24	
25	\paragraph{Limitations and future directions.}
26	Real-world documents may interleave passages at mixed recursive depths within a single document; our passage-level classifier assumes uniform depth, and extending to segment-level estimation introduces a granularity--statistical-power tradeoff that remains unexplored.
27	Web-crawl deployment requires model-specific calibration (C4 FPR: 4.7--22.4\%; Table~\ref{tab:calibration}), and all experiments use 1--1.5B models.
28	Future work should validate on mixed-domain corpora at larger scales and evaluate whether depth-graduated curation, with appropriate strategy conditioning, improves downstream training outcomes.
29	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "69c9b186-d25b-44c3-8b8c-403393c9591c",
  "isSidechain": true,
  "promptId": "b2d7dae8-7507-4c58-8d2e-f1f015a52cc1",
  "agentId": "a1343616d299e436c",
  "type": "user",
  "uuid": "0533ff2a-28a6-42c4-b694-015b7a913742",
  "sourceToolAssistantUUID": "69c9b186-d25b-44c3-8b8c-403393c9591c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/reviewer_2647e3b4",
  "sessionId": "2e338b7d-5485-4031-acd3-bb1b0bb547ae",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-15T23:42:08.894Z_

<details open><summary>🔧 Tool call — Read · `toolu_01MS21MB7aVGzfErPU5JLfQd`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/generalization.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0533ff2a-28a6-42c4-b694-015b7a913742",
  "isSidechain": true,
  "agentId": "a1343616d299e436c",
  "requestId": "req_011Cb5EtgRmb8tyvukFgcVzA",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "dfdb74d8-a6da-4428-98b3-2466c8b9f9d4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/reviewer_2647e3b4",
  "sessionId": "2e338b7d-5485-4031-acd3-bb1b0bb547ae",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01BLnshzsxF8DRPeU44oNUXB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1718,
      "cache_read_input_tokens": 18347,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1718,
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

_source line 11 · 2026-05-15T23:42:08.899Z_

<details><summary>↩ Tool result · `toolu_01MS21MB7aVGzfErPU5JLfQd`</summary>

```text
1	\section{Generalization and Robustness}
2	\label{sec:generalization}
3	
4	We test whether the atlas results (69.6--85.4\%) reflect genuine statistical regularities or training artifacts, evaluating four axes: classifier choice (\S\ref{sec:gen:baselines}), cross-model transfer (\S\ref{sec:gen:crossmodel}), cross-strategy transfer (\S\ref{sec:gen:crossstrategy}), and end-to-end learning (\S\ref{sec:gen:e2e}).
5	
6	\subsection{Baseline Comparison}
7	\label{sec:gen:baselines}
8	
9	Table~\ref{tab:baselines} evaluates three classifier families---bagging (RF), gradient boosting (XGBoost, LightGBM)---on the same 19 features across three atlas cells spanning the full accuracy range.
10	Per-cell spread is $\leq$0.4pp, establishing a feature-determined ceiling independent of the learning algorithm.
11	On Pythia nucleus, CORAL ordinal regression \cite{coral2020} (78.1\%) and DivEye \cite{diveye2026} (78.2\%) match the within-cell RF of Table~\ref{tab:main_matrix} within 0.1\,pp (bootstrap $p>0.05$, Bonferroni-corrected); all feature-based methods significantly outperform CE-MLP (74.9\%, $p<0.001$) and logistic regression (75.0\%).
12	Single-feature regression on mean perplexity performs at chance (25.1\%); a zero-shot LLM (DeepSeek V3.2) reaches only 36.2\% (95\% CI $[32.0, 40.4]$\%, 500 samples).
13	
14	\begin{table}[t]
15	\centering
16	\small
17	\caption{Classifier convergence: 4-class accuracy (\%) across three atlas cells. RF (bagging), XGBoost and LightGBM (gradient boosting) operate on the same 19 features; $\Delta_{\max}$: largest per-cell spread. Chance = 25\%. RF values differ from Table~\ref{tab:main_matrix} by $\leq$0.7pp due to matched-fold evaluation.}
18	\label{tab:baselines}
19	\begin{tabular}{@{}lcccc@{}}
20	\toprule
21	Cell & RF & XGB & LGBM & $\Delta_{\max}$ \\
22	\midrule
23	Pythia, nuc. & 78.8 & 79.0 & 78.9 & 0.2 \\
24	GPT-2~XL, $\tau$ & 85.8 & 86.2 & 86.2 & 0.4 \\
25	Pythia, top-$k$ & 68.9 & 68.9 & 68.7 & 0.2 \\
26	\bottomrule
27	\end{tabular}
28	\end{table}
29	
30	Convergence across five structurally different classifiers---spanning bagging, gradient boosting, ordinal regression, and ensemble detection---confirms the signal resides in the features, not the learning algorithm.
31	Figure~\ref{fig:confusion_matrix} shows d0 near-perfectly identified; errors concentrate at d2/d3 in-distribution and spread across d1--d3 under transfer.
32	
33	\begin{figure}[t]
34	\centering
35	\includegraphics[width=\columnwidth]{figures/fig_confusion_matrix.pdf}
36	\caption{Confusion matrices for the best in-distribution setting (GPT-2 XL, temp $\tau{=}0.9$, 85.4\%) and the best cross-model leave-one-out transfer (OLMo holdout, 69.2\%). d0 recall exceeds 99\% in both; errors spread across the d1--d3 range under transfer.}
37	\label{fig:confusion_matrix}
38	\end{figure}
39	
40	\subsection{Cross-Model Transfer}
41	\label{sec:gen:crossmodel}
42	
43	We perform leave-one-model-family-out evaluation: train on two families (nucleus only), test on the held-out third (Table~\ref{tab:cross_model}).
44	
45	\begin{table}[t]
46	\centering
47	\small
48	\caption{Cross-model transfer (leave-one-out, nucleus only). Chance = 25\% / 33\% (d1--d3). d1--d3 bal.\ acc: Pythia 49.9\%, OLMo 59.2\%, GPT-2~XL 57.2\% (mean 55.4\%).}
49	\label{tab:cross_model}
50	\begin{tabular}{lccccc}
51	\toprule
52	Holdout & Acc & d0 & d1 & d2 & d3 \\
53	 & (\%) & Rec. & Rec. & Rec. & Rec. \\
54	\midrule
55	Pythia & 62.4 & 100.0 & 49.3 & 26.8 & 73.6 \\
56	OLMo & \textbf{69.2} & 99.3 & 75.5 & 43.3 & 58.8 \\
57	GPT-2 XL & 67.6 & 98.5 & 74.7 & 52.6 & 44.5 \\
58	\midrule
59	Mean & 66.4 & 99.3 & 66.5 & 40.9 & 59.0 \\
60	\bottomrule
61	\end{tabular}
62	\end{table}
63	
64	Mean transfer accuracy is 66.4\% (2.7$\times$ chance); d0 recall ($>$98\%) inflates the headline while d2 drops to 26.8\% (Pythia holdout).
65	Excluding d0, d1--d3 balanced accuracy averages 55.4\% (chance = 33\%).
66	
67	\subsection{Cross-Strategy Transfer}
68	\label{sec:gen:crossstrategy}
69	
70	We train on two decoding strategies and test on the held-out third (Table~\ref{tab:cross_strategy}).
71	
72	\begin{table}[t]
73	\centering
74	\small
75	\caption{Cross-strategy transfer (leave-one-out). Chance = 25\% / 33\% (d1--d3). d0 recall $\geq$89\% inflates headline; d1--d3 mean: 45.9\%.}
76	\label{tab:cross_strategy}
77	\begin{tabular}{lccc}
78	\toprule
79	Holdout & Pythia & OLMo & GPT-2 XL \\
80	 & Acc (\%) & Acc (\%) & Acc (\%) \\
81	\midrule
82	nucleus & \textbf{69.4} & \textbf{65.4} & \textbf{59.9} \\
83	temp ($\tau{=}0.9$) & 62.8 & 58.2 & 56.1 \\
84	top-$k$ ($k{=}50$) & 51.5 & 54.9 & 53.6 \\
85	\bottomrule
86	\end{tabular}
87	\end{table}
88	
89	Mean cross-strategy accuracy (59.1\%) falls 7pp below cross-model transfer (66.4\%); excluding d0, d1--d3 accuracy drops to 45.9\% (chance = 33\%).
90	d2 recall varies sharply: nucleus holdouts retain 30--54\%, top-$k$ holdouts fall to 8--19\%, and temperature holdouts span 3.7--39.5\% (median 8.9\%).
91	Training on nucleus + top-$k$ and testing on temperature inverts the d1/d2 boundary (d1v2 AUC $<$ 0.5); per-strategy z-score normalization partially recovers it but leaves a residual gap (Limitations).
92	
93	\subsection{End-to-End Learning}
94	\label{sec:gen:e2e}
95	
96	DeBERTa-v3-base \cite{he2021_deberta_v3} and RoBERTa-base \cite{liu2019_roberta} finetuned end-to-end achieve 58.3\% ($\pm$4.7\%) and 59.5\% ($\pm$3.2\%) respectively---lagging the RF baseline (78.2\%) by 19.9pp and 18.7pp.
97	The 1.2pp inter-backbone gap rules out architecture bias; Table~\ref{tab:e2e_detail} shows both backbones share the same failure mode---high d0 F1 ($>$0.94) but collapsed d1/d2 performance (F1 $\leq$ 0.42)---while RF achieves 0.596 d2 recall, a $>$2$\times$ advantage at the hardest depth class.
98	
99	\begin{table}[t]
100	\centering
101	\small
102	\caption{Per-class performance for end-to-end PLM classifiers vs.\ RF baseline (Pythia-1.4B nucleus). PLM columns report F1; RF d2 column reports recall (the class with the largest PLM--RF gap). Both PLM backbones share the same failure pattern: collapsed d1/d2 scores despite adequate d0/d3.}
103	\label{tab:e2e_detail}
104	\begin{tabular}{@{}lccccc@{}}
105	\toprule
106	Method & Acc (\%) & d0 & d1 & d2 & d3 \\
107	\midrule
108	DeBERTa-v3 & 58.3\,$\pm$\,4.7 & .947 & .378 & .247 & .656 \\
109	RoBERTa-base & 59.5\,$\pm$\,3.2 & .958 & .416 & .261 & .647 \\
110	\midrule
111	RF (19 feat.) & 78.2 & --- & --- & .596$^\dagger$ & --- \\
112	\bottomrule
113	\multicolumn{6}{@{}l}{\footnotesize $^\dagger$Recall; shown for the depth class with the largest PLM--RF gap.}
114	\end{tabular}
115	\end{table}
116	
117	\paragraph{Feature space divergence.}
118	SHAP TreeExplainer analysis confirms that perplexity and surprisal features account for 88.8\% of RF's total contribution.
119	Three independent importance measures---SHAP, Gini, and permutation---show strong concordance (Kendall's $W{=}0.896$, $p{<}0.005$; pairwise Spearman $\rho$: SHAP--Gini $0.93$, SHAP--permutation $0.830$; Appendix~\ref{app:permutation}), with \texttt{p90\_ppl} appearing in the SHAP top-2 in 9/9 cells and \texttt{var\_surprisal} in 8/9.
120	Linear probing of PLM [CLS] representations yields negative $R^2$ for both \texttt{var\_surprisal} and \texttt{p90\_ppl} (Appendix~\ref{app:feature_overlap}), indicating that pretrained representations lack the linear structure needed to recover perplexity tail statistics---a systematic representational gap rather than a backbone-specific artifact.
121	
122	DCOL \cite{cloc2025} reached 64.5\% (Appendix~\ref{app:dcol_iterations}); all end-to-end approaches (58--65\%) underperform feature-based methods, suggesting depth estimation benefits from targeted statistical features that capture distributional tail properties absent from PLM representations.
123	This comparison is bounded by backbone scale ($\leq$125M parameters); whether larger PLMs (e.g., 7B+) can close the gap via richer internal representations remains an open question.
124	
125	\paragraph{Ecological validity.}
126	On WikiText-103 (546 editorial passages), all three model-specific RF classifiers achieve $\geq$98.5\% d0 accuracy despite $+$621\% domain shift in mean perplexity---partly an easy case, as WikiText's higher perplexity places it farther from d1--d3 in feature space.
127	On noisier web-crawl data (5{,}000 C4 passages), FPR ranges from 4.7\% (OLMo) to 22.4\% (GPT-2~XL), concentrated in template/SEO content with high n-gram repetition (Table~\ref{tab:calibration}); deployment on heterogeneous web data requires model-specific calibration.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dfdb74d8-a6da-4428-98b3-2466c8b9f9d4",
  "isSidechain": true,
  "promptId": "b2d7dae8-7507-4c58-8d2e-f1f015a52cc1",
  "agentId": "a1343616d299e436c",
  "type": "user",
  "uuid": "3a177d05-c9f7-4948-9d07-8d28aee6bcd6",
  "sourceToolAssistantUUID": "dfdb74d8-a6da-4428-98b3-2466c8b9f9d4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/reviewer_2647e3b4",
  "sessionId": "2e338b7d-5485-4031-acd3-bb1b0bb547ae",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-15T23:42:09.141Z_

<details open><summary>🔧 Tool call — Read · `toolu_014ZaQG43vbCPUtmnVkbPzFq`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3a177d05-c9f7-4948-9d07-8d28aee6bcd6",
  "isSidechain": true,
  "agentId": "a1343616d299e436c",
  "requestId": "req_011Cb5EtgRmb8tyvukFgcVzA",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "71551e48-acf2-41fb-a5b4-47064f10acad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/reviewer_2647e3b4",
  "sessionId": "2e338b7d-5485-4031-acd3-bb1b0bb547ae",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01BLnshzsxF8DRPeU44oNUXB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1718,
      "cache_read_input_tokens": 18347,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1718,
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

_source line 13 · 2026-05-15T23:42:09.146Z_

<details><summary>↩ Tool result · `toolu_014ZaQG43vbCPUtmnVkbPzFq`</summary>

```text
1	\section{The Depth Degradation Atlas}
2	\label{sec:atlas}
3	
4	We present the Depth Degradation Atlas: a systematic empirical map of how statistical fingerprints evolve across recursive generation depths, models, and decoding strategies.
5	The atlas spans $3 \times 3 = 9$ model--strategy cells evaluated at depths $d \in \{0, 1, 2, 3\}$, with depth extensions to $d{=}5$ for cross-model EDD validation (\S\ref{sec:atlas:edd}).
6	
7	%% ----------------------------------------------------------------
8	\subsection{In-Distribution Performance}
9	\label{sec:atlas:id}
10	
11	Table~\ref{tab:main_matrix} reports four-class Random Forest accuracy (5-fold CV, 200 trees) across all nine cells.
12	Accuracy ranges from 69.6\% (Pythia, top-$k$) to 85.4\% (GPT-2~XL, temperature), all exceeding the 25\% chance baseline by a wide margin.
13	Two axis effects emerge.
14	GPT-2~XL achieves the highest accuracy under every strategy (76.6--85.4\%), followed by OLMo (74.2--82.0\%) and Pythia (69.6--78.2\%).
15	Top-$k$ sampling yields the lowest accuracy in every model.
16	The mean within-model strategy gap is 8.4~pp, comparable to the 7.1~pp mean within-strategy model gap---decoding strategy and model family contribute roughly equally to performance variance.
17	
18	\begin{table}[t]
19	\centering
20	\small
21	\caption{Four-class RF accuracy (\%) across the $3 \times 3$ atlas, with d1--d3 three-class accuracy in parentheses (chance = 25\% / 33\%). Depth-0 recall exceeds 98\% in all cells.}
22	\label{tab:main_matrix}
23	\begin{tabular}{@{}lccc@{}}
24	\toprule
25	& Nucleus & Temp.\ $\tau{=}0.9$ & Top-$k$ \\
26	\midrule
27	Pythia-1.4B  & 78.2\,(71.2) & 76.3\,(70.6) & 69.6\,(58.8) \\
28	OLMo-1B     & 78.8\,(75.0) & 82.0\,(76.3) & 74.2\,(66.1) \\
29	GPT-2~XL    & 83.3\,(79.0) & 85.4\,(82.6) & 76.6\,(69.5) \\
30	\bottomrule
31	\end{tabular}
32	\end{table}
33	
34	\paragraph{Per-class recall distribution.}
35	Depth-0 recall exceeds 98\% in all 9 cells, confirming that human-written text is trivially separable from any generation depth.
36	Among generated depths, d2 consistently yields the lowest recall (46--73\% across cells), followed by d3 (58--82\%) and d1 (72--91\%).
37	For example, Pythia-1.4B nucleus achieves per-class recall of d0$\,{=}\,$99\%, d1$\,{=}\,$82\%, d2$\,{=}\,$59\%, d3$\,{=}\,$72\%.
38	The strongest d2 recall is obtained by GPT-2~XL nucleus (73\%).
39	The d2 trough reflects its position at the center of the depth gradient: d2 features overlap with both the d1 distribution above and d3 below, making it the most confusable class---consistent with the d2-vs-d3 pair being the EDD bottleneck (\S\ref{sec:atlas:edd}).
40	Full per-class recall for all cells appears in Appendix~\ref{app:per_class}.
41	
42	%% ----------------------------------------------------------------
43	\subsection{Feature Consistency Across the Grid}
44	\label{sec:atlas:features}
45	
46	Despite the 15.8~pp accuracy spread across cells, a small feature family dominates in every setting.
47	The 90th-percentile perplexity (\texttt{p90\_ppl}) ranks top-2 by Gini importance in all 9 cells; surprisal variance (\texttt{var\_surprisal}) in 8/9 under SHAP (7/9 under Gini; Appendix~\ref{app:permutation}).
48	Table~\ref{tab:feature_importance} shows the full per-cell ranking.
49	
50	Cross-model feature-rank Spearman correlation averages $\bar{\rho} = 0.868$ (range $[0.619, 0.954]$): models agree on which features carry depth information even when they differ in absolute accuracy.
51	Among strategies, top-$k$ yields the highest cross-model rank correlation ($\rho = 0.811$)---the deterministic vocabulary truncation imposes a more uniform feature landscape across architectures, at the cost of weaker overall signal (\S\ref{sec:atlas:strategy}).
52	
53	Percentile-based features outperform their moment-based counterparts.
54	Token-level perplexity distributions are heavy-tailed: individual outlier passages can dominate the arithmetic mean of their depth class, whereas \texttt{p90\_ppl} is robust to such extremes while still capturing the tail erosion that signals generation depth.
55	
56	Feature ablation confirms this concentration: the top-2 features (\texttt{p90\_ppl} + \texttt{var\_surprisal}) alone reach 91.1\% of full accuracy (71.5\%), and the top-5 features achieve 97.6\% (76.5\% vs.\ 78.4\%), with perplexity statistics alone reaching 76.6\% (vs.\ surprisal 73.2\%, other categories ${\leq}$47\%).
57	Variance inflation analysis reveals VIF${>}$10 for 14--16 of 19 features, placing the effective independent dimensionality at ${\approx}$4--5.
58	Forward selection independently confirms the dominant pair: \texttt{p90\_ppl} is selected first in 6/9 cells, \texttt{var\_surprisal} in 3/9.
59	
60	The feature hierarchy also shifts with depth.
61	At shallow boundaries (d1 vs.\ d2), \texttt{var\_surprisal} dominates importance; at deeper boundaries (d3 vs.\ d4, d4 vs.\ d5), tail perplexity statistics (\texttt{p90\_ppl}, \texttt{kurtosis\_ppl}) take over.
62	This transition aligns with model-collapse dynamics~\cite{shumailov2024_nature}: early recursion narrows the surprisal distribution (captured by its variance), while later steps erode the perplexity tail (captured by upper quantiles and kurtosis).
63	
64	\begin{table}[t]
65	\centering
66	\small
67	\caption{Top-5 features by Gini importance. \textbf{Bold}: top-2. \texttt{p90\_ppl} top-2 in 9/9; \texttt{var\_surprisal} 8/9 under SHAP (7/9 under Gini).}
68	\label{tab:feature_importance}
69	\begin{tabular}{@{}l l@{}}
70	\toprule
71	Cell & Top-5 features (Gini importance, ranked) \\
72	\midrule
73	Pythia, nuc.       & \textbf{var\_surp\,(.17)}, \textbf{p90\_ppl\,(.15)}, m\_ppl\,(.11), var\_ppl\,(.08), p75\,(.07) \\
74	Pythia, $\tau$     & \textbf{var\_surp\,(.17)}, \textbf{p90\_ppl\,(.14)}, m\_ppl\,(.11), p75\,(.07), m\_surp\,(.07) \\
75	Pythia, top-$k$    & \textbf{var\_surp\,(.16)}, \textbf{p90\_ppl\,(.12)}, m\_ppl\,(.11), var\_ppl\,(.07), m\_surp\,(.06) \\
76	GPT-2\,XL, nuc.    & \textbf{var\_surp\,(.21)}, \textbf{p90\_ppl\,(.21)}, p75\,(.10), m\_surp\,(.07), m\_ppl\,(.06) \\
77	GPT-2\,XL, $\tau$  & \textbf{p90\_ppl\,(.25)}, \textbf{p75\,(.15)}, m\_surp\,(.13), var\_surp\,(.12), p50\,(.05) \\
78	GPT-2\,XL, top-$k$ & \textbf{p90\_ppl\,(.24)}, \textbf{p75\,(.12)}, var\_surp\,(.10), m\_surp\,(.09), ttr\,(.04) \\
79	OLMo, nuc.         & \textbf{p90\_ppl\,(.18)}, \textbf{var\_surp\,(.15)}, p75\,(.11), m\_surp\,(.07), ttr\,(.06) \\
80	OLMo, $\tau$       & \textbf{p90\_ppl\,(.21)}, \textbf{var\_surp\,(.16)}, p75\,(.12), m\_surp\,(.09), ttr\,(.05) \\
81	OLMo, top-$k$      & \textbf{p90\_ppl\,(.20)}, \textbf{var\_surp\,(.17)}, p75\,(.10), m\_surp\,(.07), m\_ppl\,(.05) \\
82	\bottomrule
83	\end{tabular}
84	\end{table}
85	
86	\begin{figure}[t]
87	\centering
88	\includegraphics[width=\columnwidth]{figures/fig_atlas_heatmap.pdf}
89	\caption{Atlas feature importance heatmap. Rows: 19 features grouped by category (\S\ref{sec:method:features}); columns: 9 model--strategy cells. Color intensity encodes RF Gini importance. The perplexity-tail and surprisal-variance blocks maintain high importance across all cells.}
90	\label{fig:atlas_heatmap}
91	\end{figure}
92	
93	%% ----------------------------------------------------------------
94	\subsection{Monotonicity and Inter-Depth Distances}
95	\label{sec:atlas:monotonicity}
96	
97	Depth features exhibit strong monotonic trends: perplexity tail statistics (\texttt{p90\_ppl}, \texttt{mean\_surprisal}) decrease with depth (Spearman $\rho = -1.0$ across cell-level medians) while repetition features increase, reflecting the complementary narrowing and self-repetition of distribution collapse.
98	Inter-depth distances are non-uniform: d0-vs-d1 AUC exceeds 0.99 in all 9 cells, whereas d2-vs-d3 ranges from 0.69 to 0.89---separating adjacent deep generations requires the tail statistics identified in \S\ref{sec:atlas:features}.
99	
100	\begin{figure}[t]
101	\centering
102	\includegraphics[width=\columnwidth]{figures/fig_feature_trajectory.pdf}
103	\caption{Feature trajectories across depths $d{=}0$ to $d{=}3$, stratified by model (columns) and strategy (line style). Top row: \texttt{p90\_ppl} (monotonically decreasing). Middle: \texttt{var\_surprisal} (decreasing). Bottom: \texttt{rep\_3gram} (increasing). Shaded bands: interquartile range. The $d{=}0 \to d{=}1$ gap exceeds all subsequent inter-depth gaps.}
104	\label{fig:feature_trajectory}
105	\end{figure}
106	
107	%% ----------------------------------------------------------------
108	\subsection{EDD Analysis}
109	\label{sec:atlas:edd}
110	
111	We extend the benchmark to depth $d{=}5$ for all three models under nucleus sampling.
112	Each model's depth-3 LoRA checkpoint is used to finetune and generate depth-4 data, and the process repeats for depth~5; feature extraction uses the same reference model (GPT-2 base, 124M).
113	We train dedicated binary RF classifiers (500 trees) for each adjacent pair, as defined in Eq.~\ref{eq:edd}.
114	
115	\paragraph{AUC decay profile.}
116	Figure~\ref{fig:auc_decay} plots the binary pairwise AUC decay curves.
117	For Pythia-1.4B (nucleus), AUC decays monotonically: d0-vs-d1 $= 0.999$, d1-vs-d2 $= 0.925$, d2-vs-d3 $= 0.823$, d3-vs-d4 $= 0.784$, d4-vs-d5 $= 0.683$.
118	The steepest drop occurs between the d1-vs-d2 and d2-vs-d3 pairs; the curve then flattens as the system approaches an indistinguishable regime gradually rather than crossing a sharp boundary.
119	
120	\paragraph{Cross-model convergence at depth 4--5.}
121	The d3-vs-d4 AUC consistently clusters near the $T{=}0.75$ threshold across all three models (Pythia $0.784$, OLMo $0.765$, GPT-2~XL $0.750$), while d4-vs-d5 uniformly falls below $0.70$ ($0.681$--$0.684$).
122	The directional pattern is consistent, but statistical strength is stratified: bootstrap testing ($10{,}000$ resamples, $H_0{:}\, \mathrm{AUC} \leq 0.75$) yields $p = 0.001$ for Pythia (significant), $p = 0.091$ for OLMo (marginal), and $p = 0.505$ for GPT-2~XL (non-significant).
123	All three models cross the $T{=}0.75$ threshold within the d3--d4 region, establishing a consistent depth-4 decay boundary with graded confidence rather than uniform statistical significance.
124	The d4-vs-d5 saturation is unambiguous across models, supporting the interpretation of d3--d4 as a \emph{transition zone} from discriminable to indistinguishable regime.
125	
126	\paragraph{EDD threshold sensitivity.}
127	Table~\ref{tab:edd_sensitivity} reports $\mathrm{EDD}_T$ across the primary 9-cell benchmark (depths 0--3) at four threshold values.
128	At $T{=}0.65$, all 9 cells achieve $\mathrm{EDD} = 3$; at $T{=}0.75$, 7 of 9 cells maintain $\mathrm{EDD} \geq 3$; at $T{=}0.80$, the count drops to 5 of 9.
129	The cells losing $\mathrm{EDD}{=}3$ first are consistently the top-$k$ configurations (Pythia top-$k$ at $T{=}0.70$, then OLMo top-$k$ at $T{=}0.75$), where the d2-vs-d3 pair is the consistent bottleneck across all 9 cells.
130	
131	\begin{table}[t]
132	\centering
133	\small
134	\caption{Number of atlas cells achieving $\mathrm{EDD} \geq 3$ at each threshold $T$, across 9 model--strategy cells (depths 0--3). The d2-vs-d3 boundary is the bottleneck; top-$k$ cells drop first.}
135	\label{tab:edd_sensitivity}
136	\begin{tabular}{@{}lcccc@{}}
137	\toprule
138	& $T{=}0.65$ & $T{=}0.70$ & $T{=}0.75$ & $T{=}0.80$ \\
139	\midrule
140	Cells with $\mathrm{EDD} \geq 3$ & 9/9 & 8/9 & 7/9 & 5/9 \\
141	\bottomrule
142	\end{tabular}
143	\end{table}
144	
145	\begin{figure}[t]
146	\centering
147	\includegraphics[width=\columnwidth]{figures/fig_auc_decay.pdf}
148	\caption{Binary pairwise AUC decay curves for three models (nucleus sampling, depths 0--5). Horizontal dashed lines mark $T \in \{0.65, 0.70, 0.75, 0.80\}$. All three curves converge below 0.70 at d4-vs-d5, while d3-vs-d4 AUC clusters in the range 0.750--0.784. Shaded bands: bootstrap 95\% CIs.}
149	\label{fig:auc_decay}
150	\end{figure}
151	
152	\paragraph{Decision boundary dilution.}
153	\label{sec:atlas:edd:dilution}
154	EDD uses binary-pair classifiers to avoid \emph{decision boundary dilution}: in Pythia nucleus, d2\,vs.\,d3 AUC degrades from 0.804 (4-class) to 0.689 (6-class)---a 14.3\% relative decline despite identical data---because shared decision boundaries dilute per-pair capacity.
155	Binary classifiers eliminate this confound, isolating true adjacent-pair discriminability.
156	
157	%% ----------------------------------------------------------------
158	\subsection{Strategy-Dependent Trajectories}
159	\label{sec:atlas:strategy}
160	
161	The three decoding strategies induce qualitatively distinct degradation trajectories.
162	Nucleus ($p{=}0.95$) produces the most consistent accuracy (78.2--83.3\%) and serves as the reference trajectory.
163	Temperature ($\tau{=}0.9$) yields the highest accuracy in 2/3 models (GPT-2~XL 85.4\%, OLMo 82.0\%) because uniform logit scaling accelerates convergence to an attractor distribution~\cite{shumailov2024_nature}, amplifying the statistical fingerprint---but this acceleration creates a boundary reversal risk: temperature depth-$N$ features approximate nucleus/top-$k$ depth-$(N{+}1)$ features, causing cross-strategy classifiers to systematically overpredict depth (\S\ref{sec:generalization}).
164	Top-$k$ ($k{=}50$) produces the lowest accuracy (69.6--76.6\%) because hard vocabulary truncation removes depth-discriminative low-probability tokens, though feature direction is preserved (cross-model $\rho = 0.811$).
165	The strategy effect (8.4~pp range) exceeds the model effect (7.1~pp), indicating deployment-time knowledge of the decoding strategy matters at least as much as the generator model.
166	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "71551e48-acf2-41fb-a5b4-47064f10acad",
  "isSidechain": true,
  "promptId": "b2d7dae8-7507-4c58-8d2e-f1f015a52cc1",
  "agentId": "a1343616d299e436c",
  "type": "user",
  "uuid": "ebfdfe6b-16a7-4753-8a03-8f4c0c141b8c",
  "sourceToolAssistantUUID": "71551e48-acf2-41fb-a5b4-47064f10acad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/reviewer_2647e3b4",
  "sessionId": "2e338b7d-5485-4031-acd3-bb1b0bb547ae",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-15T23:42:09.318Z_

<details open><summary>🔧 Tool call — Read · `toolu_018nYbpciJ9DwnGNheVS2v4V`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ebfdfe6b-16a7-4753-8a03-8f4c0c141b8c",
  "isSidechain": true,
  "agentId": "a1343616d299e436c",
  "requestId": "req_011Cb5EtgRmb8tyvukFgcVzA",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "cb707590-173d-4046-a5bb-f64a49c13c06",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/reviewer_2647e3b4",
  "sessionId": "2e338b7d-5485-4031-acd3-bb1b0bb547ae",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01BLnshzsxF8DRPeU44oNUXB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1718,
      "cache_read_input_tokens": 18347,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1718,
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

_source line 15 · 2026-05-15T23:42:09.324Z_

<details><summary>↩ Tool result · `toolu_018nYbpciJ9DwnGNheVS2v4V`</summary>

```text
1	\section{Additional Results}
2	\label{app:additional}
3	
4	\subsection{Top-$k$ Feature Trajectories}
5	\label{app:topk_trajectories}
6	
7	Figure~\ref{fig:feature_trajectory} in the main text shows feature trajectories for nucleus ($p{=}0.95$) and temperature ($\tau{=}0.9$) sampling.
8	Top-$k$ ($k{=}50$) trajectories follow the same monotonically decreasing trend for all features but with compressed inter-depth spacing, consistent with the signal attenuation effect discussed in \S\ref{sec:atlas:strategy}.
9	Concretely, the d0$\to$d1 drop in \textsc{p90\_ppl} under top-$k$ is 78\% (vs.\ 87\% for nucleus), and the d2$\to$d3 reduction is 31\% (vs.\ 39\% for nucleus).
10	Despite the magnitude reduction, feature rank ordering across depths is preserved, which explains why ordinal classifiers maintain directionality even under top-$k$ conditions.
11	
12	\subsection{Permutation Importance}
13	\label{app:permutation}
14	
15	To verify that the Gini-based importance rankings in \S\ref{sec:atlas:features} are not an artifact of the impurity measure, we compute permutation importance (5-fold CV, 10 repeats) for all 9 atlas cells.
16	The top-2 features are stable across measures: \textsc{p90\_ppl} ranks in the top 2 in 9/9 cells under both Gini and permutation importance, and \textsc{var\_surprisal} in 8/9 (vs.\ 7/9 for Gini, with the additional cell being OLMo top-$k$; the single SHAP exception is GPT-2~XL top-$k$, where \textsc{p75\_ppl} displaces \textsc{var\_surprisal} to rank 3).
17	Kendall's $W{=}0.90$ across all three methods (Gini, permutation, SHAP) indicates strong concordance ($p{<}0.005$).
18	Pairwise Spearman correlations are: SHAP--Gini $\rho{=}0.93$, SHAP--permutation $\rho{=}0.83$, Gini--permutation $\rho{=}0.76$.
19	Per-cell top-5 overlap between SHAP and permutation importance is 3--4 out of 5 features; the aggregated (mean-across-cells) top-5 sets are identical, confirming that the top features are robust to the choice of importance measure at the aggregate level while per-cell rankings exhibit model-dependent variation.
20	
21	\subsection{Per-Class Recall}
22	\label{app:per_class}
23	
24	Table~\ref{tab:per_class_recall} reports per-class recall across all 9 atlas cells (4-class in-distribution, 5-fold CV).
25	Depth~0 recall exceeds 98\% uniformly.
26	Among generated depths, d2 is the hardest class in every cell; the deficit is most pronounced under top-$k$ sampling (46--53\%), where vocabulary truncation removes the tail tokens that carry depth-discriminative signal.
27	
28	\begin{table}[h]
29	\centering
30	\small
31	\caption{Per-class recall (\%) for all 9 atlas cells. d2 is the lowest-recall class in every cell. Boldface marks the highest d2 recall.}
32	\label{tab:per_class_recall}
33	\begin{tabular}{@{}lcccc@{}}
34	\toprule
35	Cell & d0 & d1 & d2 & d3 \\
36	\midrule
37	Pythia, nuc.       & 99.7 & 81.9 & 58.7 & 72.3 \\
38	Pythia, $\tau$     & 99.7 & 81.3 & 53.9 & 72.1 \\
39	Pythia, top-$k$    & 99.5 & 72.3 & 45.6 & 57.5 \\
40	OLMo, nuc.         & 98.8 & 80.5 & 61.5 & 74.3 \\
41	OLMo, $\tau$       & 99.7 & 87.7 & 66.1 & 77.2 \\
42	OLMo, top-$k$      & 99.5 & 78.5 & 51.2 & 65.6 \\
43	GPT-2~XL, nuc.     & 99.2 & 85.9 & \textbf{73.3} & 77.5 \\
44	GPT-2~XL, $\tau$   & 99.5 & 90.9 & 68.8 & 81.9 \\
45	GPT-2~XL, top-$k$  & 98.5 & 79.5 & 52.5 & 71.1 \\
46	\bottomrule
47	\end{tabular}
48	\end{table}
49	
50	\subsection{DCOL Iteration Details}
51	\label{app:dcol_iterations}
52	
53	Table~\ref{tab:dcol_iterations} summarizes all six DCOL iterations.
54	DeBERTa-v3-large exhibited systematic numerical instability across five configurations; RoBERTa-large resolved stability but could not close the accuracy gap with feature-based methods.
55	
56	\begin{table}[h]
57	\centering
58	\small
59	\caption{DCOL iteration summary. All experiments use Pythia-1.4B nucleus data. RF baseline: 78.2\%.}
60	\label{tab:dcol_iterations}
61	\begin{tabular}{@{}llp{2.2cm}p{2.8cm}@{}}
62	\toprule
63	Ver. & Backbone & Config & Outcome \\
64	\midrule
65	v1 & DeBERTa & FT, m\_lr $10^{-3}$ & Embed.\ collapse (31.5\%) \\
66	v2 & DeBERTa & FT, m\_lr $10^{-4}$ & OOM \\
67	v3 & DeBERTa & FT, m\_lr $10^{-4}$ & Forgetting + OOM \\
68	v4 & DeBERTa & LoRA, m\_lr $10^{-3}$ & Embed.\ collapse \\
69	v5 & DeBERTa & LoRA, m\_lr $10^{-4}$ & NaN gradients \\
70	v6 & RoBERTa & FT, grad clip 1.0 & Stable; 64.5\% ($-$13.7pp) \\
71	\bottomrule
72	\end{tabular}
73	\end{table}
74	
75	\subsection{Feature Overlap Analysis}
76	\label{app:feature_overlap}
77	
78	We probe whether end-to-end PLM representations capture the same depth signals as our statistical features via linear probing of [CLS] representations from DeBERTa-v3-base and RoBERTa-base.
79	PLM representations excel at surface lexical features (TTR: $R^2{=}0.85$, repeated bigrams) but fail to capture perplexity distribution statistics---\textsc{var\_surprisal} and \textsc{p90\_ppl} yield negative $R^2$ under linear probing, indicating these features are not linearly accessible in the pretrained representation space.
80	This confirms that the 19pp accuracy gap between feature-based and end-to-end methods (\S\ref{sec:gen:e2e}) stems from complementary---not redundant---representations: PLMs capture lexical patterns while the targeted statistical features capture distributional tail properties that constitute the dominant depth markers.
81	
82	\subsection{Domain Bias Analysis}
83	\label{app:domain_bias}
84	
85	To assess whether the classifier exploits depth-related features or memorizes stylistic cues from individual seed articles, we conduct three sub-experiments.
86	
87	\paragraph{Methodological note.}
88	An initial implementation assigned sample IDs with a global counter across depths, inadvertently correlating seed-group identity with depth (LOGO accuracy 64.0\%, seed-group prediction 20.8\%).
89	We discovered the issue during internal review, corrected to per-depth seed assignment ensuring each group contains equal samples per depth, and re-ran all sub-experiments.
90	The results below use the corrected pipeline; the initial (buggy) numbers are reported for transparency.
91	
92	\paragraph{Sub-A: Standard CV.}
93	Five-fold CV accuracy on 3-class (d1/d2/d3) classification ranges from 59\% to 82\% across the 9 atlas cells (up to 2.5$\times$ above the 33.3\% chance level), confirming that depth signal is the dominant classification factor.
94	
95	\paragraph{Sub-B: LOGO evaluation.}
96	We assign each passage to one of 10 seed-article groups (balanced: each group contains equal samples per depth) and perform leave-one-group-out CV.
97	LOGO mean accuracy is 72.1\% (range 59.5--81.6\%), matching standard CV (72.0\%) within noise (before fix: 64.0\%, reflecting the depth--group confound).
98	Per-cell fold standard deviations range from 0.4pp to 1.4pp, indicating that cross-group generalization is as reliable as within-group classification.
99	
100	\paragraph{Sub-C: Negative control.}
101	We train two classifiers on identical features: one predicting depth, the other predicting seed-group identity (10-class, chance = 10\%).
102	Depth prediction accuracy averages 72.0\%; seed-group prediction averages 10.2\%---indistinguishable from chance (before fix: 20.8\%, inflated by the depth--group confound).
103	The depth-to-seed-group accuracy ratio is 7.1$\times$, confirming that the feature representation encodes depth but not seed-article identity.
104	
105	Taken together, these results show that seed-article grouping has no measurable effect on depth estimation after correcting the group assignment: LOGO accuracy equals standard CV, and seed-group prediction is at chance.
106	
107	\subsection{Wild-Data Calibration}
108	\label{app:calibration}
109	
110	Table~\ref{tab:calibration} reports d0 accuracy and false positive rate (FPR) for all three model-specific nucleus RF classifiers on two out-of-distribution human-text corpora: WikiText-103 (546 editorial passages) and C4 (5{,}000 web-crawl passages).
111	
112	\begin{table}[h]
113	\centering
114	\small
115	\caption{Wild-data d0 accuracy and FPR for nucleus RF classifiers. All passages are human-written (true d0). FPR = fraction misclassified as d1+.}
116	\label{tab:calibration}
117	\begin{tabular}{@{}llrcc@{}}
118	\toprule
119	Model & Source & $n$ & d0 (\%) & FPR (\%) \\
120	\midrule
121	Pythia-1.4B & WikiText & 546 & 100.0 & 0.0 \\
122	 & C4 & 5{,}000 & 79.8 & 20.2 \\
123	\addlinespace
124	GPT-2~XL & WikiText & 546 & 99.3 & 0.7 \\
125	 & C4 & 5{,}000 & 77.6 & 22.4 \\
126	\addlinespace
127	OLMo-1B & WikiText & 546 & 98.5 & 1.5 \\
128	 & C4 & 5{,}000 & 95.3 & 4.7 \\
129	\bottomrule
130	\end{tabular}
131	\end{table}
132	
133	On WikiText-103, all three classifiers achieve $\geq$98.5\% d0 accuracy, confirming that editorial text is reliably distinguished from recursive generations across model families.
134	On C4, FPR varies sharply: OLMo (4.7\%) vs.\ Pythia (20.2\%) and GPT-2~XL (22.4\%).
135	C4 misclassifications concentrate in template and SEO content with elevated repetition features (\texttt{rep\_3gram} $+$37\%, \texttt{rep\_4gram} $+$75\% vs.\ correctly classified d0 passages), rather than in random noise.
136	The model gap likely reflects training data composition: OLMo (trained on Dolma, which includes diverse web data) produces d0 features more tolerant of web-crawl variation, while Pythia and GPT-2~XL (trained primarily on Wikipedia/WebText) map template-heavy content into the d1+ region.
137	Among C4 false positives for GPT-2~XL, predictions distribute as d1 (9.0\%), d2 (3.7\%), d3 (9.6\%); for OLMo, d1 (2.9\%), d2 (0.5\%), d3 (1.3\%)---the non-uniform depth distribution suggests the classifier maps specific repetition patterns to particular depth signatures rather than producing random misclassifications.
138	
139	\subsection{Extended Discussion}
140	\label{app:extended_discussion}
141	
142	\paragraph{Depth-graduated curation.}
143	Current data curation operates on a binary human-vs-machine distinction \cite{dsir2023,qurating2024}.
144	Recursive generation depth estimation enables a finer-grained alternative: retain low-depth generations (d1) whose distributional properties remain close to the human source, while down-weighting or filtering high-depth text (d3+) where tail erosion has degraded quality.
145	The 70--85\% in-distribution accuracy and $\mathrm{EDD}_{0.75}{=}4$ suggest depth-graduated filtering is feasible within known model--strategy configurations, though the d1/d2 boundary inversion under cross-strategy transfer (\S\ref{sec:gen:crossstrategy}) means reliable curation requires either known decoding strategy metadata or an upstream strategy-identification step; the downstream effect on training quality remains to be validated empirically.
146	Importance weighting \cite{sugiyama2007_importance_weighting} could further enable continuous depth-aware data selection rather than discrete thresholding.
147	
148	\paragraph{Toward a provenance toolkit.}
149	Depth estimation complements existing provenance methods along orthogonal axes.
150	Watermarking \cite{kirchenbauer2023_watermark} provides high-confidence attribution when the generator cooperates but is inapplicable to unwatermarked text.
151	Source attribution \cite{uchendu2020_attribution} identifies the generating model but not the generation history.
152	Depth estimation characterizes \emph{iterative reuse} regardless of generator cooperation or identity.
153	A layered provenance system combining these three signals---watermark presence, source model, and recursive generation depth---could support more nuanced data auditing than any single method.
154	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cb707590-173d-4046-a5bb-f64a49c13c06",
  "isSidechain": true,
  "promptId": "b2d7dae8-7507-4c58-8d2e-f1f015a52cc1",
  "agentId": "a1343616d299e436c",
  "type": "user",
  "uuid": "be1e3774-d906-43da-ad03-81e0897bddaf",
  "sourceToolAssistantUUID": "cb707590-173d-4046-a5bb-f64a49c13c06",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/reviewer_2647e3b4",
  "sessionId": "2e338b7d-5485-4031-acd3-bb1b0bb547ae",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-15T23:42:09.580Z_

<details open><summary>🔧 Tool call — Read · `toolu_01W8Ji5KkzUAkUzypWZpzS4Y`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "be1e3774-d906-43da-ad03-81e0897bddaf",
  "isSidechain": true,
  "agentId": "a1343616d299e436c",
  "requestId": "req_011Cb5EtgRmb8tyvukFgcVzA",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "dd95d502-3408-4ba5-be3e-f2f847eb7538",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/reviewer_2647e3b4",
  "sessionId": "2e338b7d-5485-4031-acd3-bb1b0bb547ae",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01BLnshzsxF8DRPeU44oNUXB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1718,
      "cache_read_input_tokens": 18347,
      "output_tokens": 399,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1718
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 399,
          "cache_read_input_tokens": 18347,
          "cache_creation_input_tokens": 1718,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1718,
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

_source line 17 · 2026-05-15T23:42:09.585Z_

<details><summary>↩ Tool result · `toolu_01W8Ji5KkzUAkUzypWZpzS4Y`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Problem Definition}
5	\label{sec:method:problem}
6	
7	Let $f_\theta$ denote a language model and $\mathcal{D}_0$ a corpus of human-written seed text.
8	We define a \emph{recursive generation chain} of depth $K$ as the sequence $\mathcal{D}_0, \mathcal{D}_1, \dots, \mathcal{D}_K$, where each $\mathcal{D}_k$ ($k \geq 1$) is produced by finetuning $f_\theta$ on $\mathcal{D}_{k-1}$ and sampling from the resulting model.
9	Depth $d{=}0$ denotes human-written text; depth $d{=}k$ ($k \geq 1$) denotes text generated by a model trained on depth-$(k{-}1)$ data.
10	
11	Given a text passage $x$, the task is to estimate its recursive generation depth $d \in \{0, 1, \dots, K\}$.
12	This is an ordinal classification problem: depths carry a natural ordering, and $d{=}1$ is structurally closer to $d{=}0$ than $d{=}3$ is, since each generation step compounds distributional drift.
13	
14	\subsection{Multi-Generational Benchmark Construction}
15	\label{sec:method:benchmark}
16	
17	We construct a benchmark spanning three axes: model family, decoding strategy, and generation depth.
18	
19	\paragraph{Model families.}
20	We select three 1--1.5B-parameter models with diverse pretraining corpora and architectures: Pythia-1.4B (EleutherAI), OLMo-1B (AI2), and GPT-2~XL (OpenAI, 1.5B).
21	Restricting to a narrow parameter range isolates the effect of architecture and training data from scale.
22	
23	\paragraph{Decoding strategies.}
24	Each model is paired with three decoding strategies: nucleus sampling ($p{=}0.95$) \cite{holtzman2020_nucleus}, temperature sampling ($\tau{=}0.9$), and top-$k$ sampling ($k{=}50$).
25	These span the dominant modes of open-ended generation and induce qualitatively different entropy profiles.
26	Our findings on feature importance and discriminability are limited to this grid; transfer to untested models, scales, or strategies is not established.
27	
28	\paragraph{Depth and scale.}
29	The primary benchmark covers depths d0--d3 across all $3 \times 3 = 9$ model--strategy cells, with 5{,}000 samples per depth per cell (180K samples total).
30	For depth extension experiments (\S\ref{sec:atlas}), we extend one pipeline (Pythia-1.4B, nucleus) to d0--d5.
31	
32	\paragraph{Generation pipeline.}
33	Starting from a Wikipedia subset as seed text ($\mathcal{D}_0$), each generation cycle proceeds in three steps: (1)~LoRA finetuning \cite{hu2022lora} on $\mathcal{D}_{k-1}$, freezing base model weights and training low-rank update matrices ($<$1\% additional parameters; $r{=}16$, $\alpha{=}32$, lr $2{\times}10^{-4}$, batch size 8, 3 epochs, dropout $0.05$, architecture-specific targets); (2)~sampling 5{,}000 passages from the LoRA-finetuned model (max 512 tokens, BOS-seeded, no prompt conditioning) under the specified decoding strategy; (3)~the generated corpus becomes $\mathcal{D}_k$ for the next cycle.
34	Each depth is produced by a model explicitly trained on the prior depth's data---not by sampling from the unmodified base model.
35	There is no per-passage lineage across depths, ensuring cross-validation splits do not introduce information leakage.
36	
37	\paragraph{Reference model.}
38	All statistical features (\S\ref{sec:method:features}) are computed using a fixed reference model---GPT-2 base (124M)---that is independent of the three generation models.
39	The reference model computes per-token perplexity for each passage, providing a consistent measurement frame across model families.
40	In cross-model leave-one-out evaluation (\S\ref{sec:generalization}), the reference model remains fixed even when GPT-2~XL is held out; the partial architectural overlap this introduces is discussed in Limitations.
41	
42	\subsection{Statistical Feature Design}
43	\label{sec:method:features}
44	
45	We extract a feature vector $\mathbf{f}(x)$ comprising 19 candidate features from the reference-model perplexity distribution over each passage $x$; ablation (\S\ref{sec:atlas:features}) shows the top 5 achieve 97.6\% of full-set performance, and variance inflation analysis reveals VIF${>}$10 for 14--16 features, placing the effective independent dimensionality at ${\approx}$4--5.
46	The features fall into four categories (Table~\ref{tab:features}).
47	
48	\begin{table}[t]
49	\centering
50	\small
51	\caption{The 19 statistical features comprising $\mathbf{f}(x)$, grouped by category. All perplexity and surprisal features are computed from the reference model (GPT-2 base, 124M).}
52	\label{tab:features}
53	\begin{tabular}{@{}llr@{}}
54	\toprule
55	Category & Features & $n$ \\
56	\midrule
57	Perplexity & mean, var, skewness, kurtosis, & 9 \\
58	statistics & p10, p25, p50, p75, p90 & \\
59	\addlinespace
60	Surprisal & mean, var, entropy & 3 \\
61	statistics & & \\
62	\addlinespace
63	Lexical & type--token ratio, hapax ratio, & 4 \\
64	diversity & bigram entropy, trigram entropy & \\
65	\addlinespace
66	Repetition & repeated 2/3/4-gram fractions & 3 \\
67	\bottomrule
68	\end{tabular}
69	\end{table}
70	
71	\emph{Perplexity statistics} (9 features) capture the per-token perplexity distribution via moments (mean, variance, skewness, kurtosis) and quantiles (p10--p90); tail quantiles prove especially informative as recursive finetuning erodes the high-perplexity tail (\S\ref{sec:atlas}).
72	\emph{Surprisal statistics} (3 features): mean, variance, and entropy of $-\log p(\text{token})$; surprisal variance captures second-order structure not redundant with perplexity moments.
73	\emph{Lexical diversity} (4 features): type--token ratio, hapax ratio, bigram/trigram entropy.
74	\emph{Repetition} (3 features): repeated $n$-gram fractions for $n \in \{2, 3, 4\}$.
75	
76	\subsection{Effective Discriminable Depth}
77	\label{sec:method:edd}
78	
79	Aggregate multi-class accuracy obscures whether discriminability degrades at specific depth boundaries.
80	We introduce the \emph{Effective Discriminable Depth} (EDD) to formalize the frontier beyond which adjacent depths become statistically indistinguishable.
81	
82	\paragraph{Pairwise discriminability.}
83	Let $\mathcal{D} = \{0, 1, \dots, K\}$ denote the depth set and $T \in (0.5, 1.0]$ a discrimination threshold.
84	For each adjacent pair $(d, d{+}1)$, we define the pairwise discriminability $\mathrm{AUC}(d, d{+}1)$ as the area under the ROC curve of a dedicated binary Random Forest classifier (500 trees, $\lfloor\sqrt{19}\rfloor$ candidate features per split) trained on class-balanced data from $\mathbf{f}(x)$ (\S\ref{sec:method:features}) to distinguish depth-$d$ from depth-$(d{+}1)$ samples, evaluated via 5-fold stratified cross-validation.
85	Each pair uses an independent classifier, avoiding the decision boundary dilution that arises in multi-class settings (\S\ref{sec:atlas:edd}).
86	
87	\begin{definition}[Effective Discriminable Depth]
88	\label{def:edd}
89	The \emph{Effective Discriminable Depth} at threshold $T$ is:
90	\begin{equation}
91	\mathrm{EDD}_T = \max \bigl\{ d^*{+}1 \,:\, \forall\, d' \leq d^*,\; \mathrm{AUC}(d', d'{+}1) \geq T \bigr\}
92	\label{eq:edd}
93	\end{equation}
94	where $d^* \in \{0, \dots, K{-}1\}$. If\, $\mathrm{AUC}(0,1) < T$, then $\mathrm{EDD}_T = 0$.
95	\end{definition}
96	
97	$\mathrm{EDD}_T$ is the deepest depth $d$ such that every adjacent pair from $(0,1)$ through $(d{-}1, d)$ remains discriminable at level $T$.
98	The universal quantifier ensures EDD reports the longest \emph{contiguous} discriminable prefix rather than an isolated high-AUC pair at greater depth.\footnote{Our AUC profiles are empirically monotonically decreasing (\S\ref{sec:atlas}), so in practice $\mathrm{EDD}_T = \max\{d'{+}1 : \mathrm{AUC}(d', d'{+}1) \geq T\}$. For non-monotonic profiles, the contiguous formulation is more conservative (see Limitations).}
99	We set $T{=}0.75$ as default; sensitivity at $T \in \{0.65, 0.70, 0.75, 0.80\}$ is reported in \S\ref{sec:atlas}.
100	
101	\paragraph{Classifiers.}
102	Our primary classifier is a Random Forest (200 trees, unconstrained depth, 5-fold stratified cross-validation).
103	We compare against CORAL ordinal regression \cite{coral2020}, DivEye \cite{diveye2026}, a 2-layer cross-entropy MLP, logistic regression, and a single-feature baseline using mean perplexity alone; results appear in \S\ref{sec:generalization}.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dd95d502-3408-4ba5-be3e-f2f847eb7538",
  "isSidechain": true,
  "promptId": "b2d7dae8-7507-4c58-8d2e-f1f015a52cc1",
  "agentId": "a1343616d299e436c",
  "type": "user",
  "uuid": "bbe73e4e-1433-4c45-b58e-4bbd3da3841f",
  "sourceToolAssistantUUID": "dd95d502-3408-4ba5-be3e-f2f847eb7538",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/reviewer_2647e3b4",
  "sessionId": "2e338b7d-5485-4031-acd3-bb1b0bb547ae",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-15T23:42:18.277Z_

Based on my search through all .tex files in the paper directory, I found **two written sections about data curation** that relate to the curation PoC experiment. Here's what I found:

## Files with Curation Content

### 1. **discussion.tex** (Lines 11-16)
File path: `/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/discussion.tex`

**Section Title:** "Depth-graduated data curation"

**Claims made:**
- Current data curation operates on a binary human-vs-machine distinction
- Depth estimation enables a **finer-grained alternative**: retain low-depth generations (d1) whose distributional properties remain close to the human source, while down-weighting or filtering high-depth text (d3+) where tail erosion has degraded quality
- The 70-85% in-distribution accuracy and EDD₀.₇₅=4 suggest **depth-graduated filtering is feasible within known model–strategy configurations**
- Cross-strategy transfer complications mean reliable curation requires either known decoding metadata or an upstream strategy-identification step
- **Key caveat:** "The downstream effect on training quality remains to be validated empirically"
- Importance weighting could enable continuous depth-aware data selection rather than discrete thresholding
- Verification-guided retraining offers a complementary mitigation path

### 2. **section_appendix.tex** (Lines 142-146)
File path: `/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex`

**Section Title:** "Depth-graduated curation" (Extended Discussion)

**Claims made (nearly identical to discussion.tex):**
- Enables finer-grained alternative to binary human-vs-machine distinction
- Retain d1, down-weight/filter d3+
- 70-85% in-distribution accuracy and EDD₀.₇₅=4 suggest feasibility within known configurations
- Cross-strategy transfer complications require known metadata or upstream strategy-identification
- **Same key caveat:** "the downstream effect on training quality remains to be validated empirically"
- Importance weighting could enable continuous selection

## Key Finding

**No mention of "plan_013" or any specific PoC experiment results.** The paper discusses curation as a **potential future application** but explicitly states that **validation has not been completed yet**. The downstream effect on training quality is listed as a remaining gap, not a finished experiment.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bbe73e4e-1433-4c45-b58e-4bbd3da3841f",
  "isSidechain": true,
  "agentId": "a1343616d299e436c",
  "requestId": "req_011Cb5EtsFPR5cYHhsp65ss6",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "34745d39-153c-426b-b4b2-762ce4d1031a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/reviewer_2647e3b4",
  "sessionId": "2e338b7d-5485-4031-acd3-bb1b0bb547ae",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_012sNW9QqWKM5gcsSnibAyFe",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 16839,
      "cache_read_input_tokens": 20065,
      "output_tokens": 601,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 16839
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 601,
          "cache_read_input_tokens": 20065,
          "cache_creation_input_tokens": 16839,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 16839,
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
