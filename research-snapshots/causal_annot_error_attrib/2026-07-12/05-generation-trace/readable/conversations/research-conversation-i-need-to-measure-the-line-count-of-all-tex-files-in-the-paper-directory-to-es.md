# Research conversation: I need to measure the line count of all .tex files in the paper directory to estimate content volume. Read each of these

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 20
- **Recorded user turns:** 1
- **Tool calls:** 8
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a1b64ac8a57b00a7e.jsonl`
- **Structured JSON:** [`fced0f6e258ab2e0182b.json`](../../sessions/fc/fced0f6e258ab2e0182b.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

20 recorded events

### User

_source line 1 · 2026-05-21T01:08:09.636Z_

I need to measure the line count of all .tex files in the paper directory to estimate content volume. Read each of these files and report just the line count and a rough word estimate:

1. /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/abstract.tex
2. /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/introduction.tex
3. /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/related_work.tex
4. /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/method.tex
5. /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/experiments.tex
6. /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/conclusion.tex
7. /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex

For each file, report: filename, line count, approximate word count (excluding LaTeX commands).

Also check: does experiments.tex use `algpseudocode` or `algorithmic` environments? This matters because AAAI template uses `algorithmic` not `algpseudocode`.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "ae2d0870-295e-4835-a3f0-f41f20bd6a21",
  "agentId": "a1b64ac8a57b00a7e",
  "type": "user",
  "uuid": "79eff245-dd3d-4874-8e38-f1e4f2c22d00",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/paper_agent_20baa82f",
  "sessionId": "35fb04f7-d2db-441f-a3b1-35490ca0d54b",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "eventual-sniffing-crane"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-21T01:08:11.440Z_

I'll read each of these files to get the line count and word estimates.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "79eff245-dd3d-4874-8e38-f1e4f2c22d00",
  "isSidechain": true,
  "agentId": "a1b64ac8a57b00a7e",
  "requestId": "req_011CbEpVpAD78wtoMigK6pYJ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "5bfe56fc-0904-414e-863c-38ab93728a4d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/paper_agent_20baa82f",
  "sessionId": "35fb04f7-d2db-441f-a3b1-35490ca0d54b",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "eventual-sniffing-crane",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017rF6omLVaGRTAAP3Wggu86",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 28018,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 28018,
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

_source line 3 · 2026-05-21T01:08:11.838Z_

<details open><summary>🔧 Tool call — Read · `toolu_0156nN3Bs8d7P8crjXrMYRD9`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5bfe56fc-0904-414e-863c-38ab93728a4d",
  "isSidechain": true,
  "agentId": "a1b64ac8a57b00a7e",
  "requestId": "req_011CbEpVpAD78wtoMigK6pYJ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d2487581-60dc-44dd-b301-2d3f5ce9c68b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/paper_agent_20baa82f",
  "sessionId": "35fb04f7-d2db-441f-a3b1-35490ca0d54b",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "eventual-sniffing-crane",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017rF6omLVaGRTAAP3Wggu86",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 28018,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 28018,
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

_source line 4 · 2026-05-21T01:08:11.847Z_

<details><summary>↩ Tool result · `toolu_0156nN3Bs8d7P8crjXrMYRD9`</summary>

```text
1	\begin{abstract}
2	Large language models (LLMs) are increasingly used as annotators in computational social science, yet annotation errors propagate into downstream causal estimates in ways that binary measurement error theory cannot predict. We present the first systematic framework characterizing how $K$-class confusion matrix structure interacts with DAG topology to determine bias direction and magnitude. We derive bias expressions for seven canonical DAG topologies under multi-class non-differential misclassification (closed-form for confounding, exposure, and mediation; numerically validated for all seven) and establish a structural sign-flip guarantee (with formal proofs for three topologies and Monte Carlo validation for all seven): five topologies (confounding, mediation, collider, M-bias, front-door) never produce sign reversal regardless of the confusion matrix, while exposure and instrumental variable topologies can. In the exposure DAG, 83.4\% of $K{=}3$ confusion matrices cause sign reversal, a failure that persists at 13.7\% violation rate (2.1\% sign reversal, 11.7\% amplification) even with classifier accuracy above 70\%. We introduce Annotation Sensitivity Values (ASVs), a sensitivity analysis framework with three complementary measures that reveal a topology-dependent vulnerability spectrum: IV estimates are maximally vulnerable (52.6\% sign reversal; sign-flip ASV $= 1.1$--$6.7$) while M-bias adjustment is immune (ASV $= \infty$). We evaluate five correction methods across all topologies and prove a Frisch--Waugh--Lovell invariance result: matrix-based corrections achieve 0\% bias reduction on the target coefficient for four topologies, while PPI++ achieves 93.8\% reduction but requires gold labels. Binarization from multi-class to binary introduces additional bias varying 147$\times$ across topologies. Neither classification $F_1$ nor correction method choice alone determines downstream safety; topology-aware analysis is necessary for valid causal inference with LLM-generated annotations.
3	\end{abstract}
4	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d2487581-60dc-44dd-b301-2d3f5ce9c68b",
  "isSidechain": true,
  "promptId": "ae2d0870-295e-4835-a3f0-f41f20bd6a21",
  "agentId": "a1b64ac8a57b00a7e",
  "type": "user",
  "uuid": "40535a03-fb04-431a-8243-1f89720b5683",
  "sourceToolAssistantUUID": "d2487581-60dc-44dd-b301-2d3f5ce9c68b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/paper_agent_20baa82f",
  "sessionId": "35fb04f7-d2db-441f-a3b1-35490ca0d54b",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "eventual-sniffing-crane"
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-21T01:08:11.886Z_

<details open><summary>🔧 Tool call — Read · `toolu_01T6ZUj3pSKFot3n1sTuwQap`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "40535a03-fb04-431a-8243-1f89720b5683",
  "isSidechain": true,
  "agentId": "a1b64ac8a57b00a7e",
  "requestId": "req_011CbEpVpAD78wtoMigK6pYJ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "ac5393e9-f0e3-4b77-bb2b-4da53e1dafe0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/paper_agent_20baa82f",
  "sessionId": "35fb04f7-d2db-441f-a3b1-35490ca0d54b",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "eventual-sniffing-crane",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017rF6omLVaGRTAAP3Wggu86",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 28018,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 28018,
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

_source line 6 · 2026-05-21T01:08:11.901Z_

<details><summary>↩ Tool result · `toolu_01T6ZUj3pSKFot3n1sTuwQap`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Large language models are rapidly replacing human annotators in computational social science, with researchers using LLM-generated labels for tasks ranging from sentiment classification to political stance detection~\cite{egami_hinck_stewart_wei2023, baumann2025}. This shift promises dramatic cost reduction, but introduces a critical validity gap: annotation errors from imperfect classifiers propagate into downstream causal estimates in ways that depend on both the error structure and the causal design. \citet{baumann2025} demonstrate that across 37 annotation tasks, 31\% of hypotheses yield incorrect conclusions with state-of-the-art LLMs, rising to 50\% for smaller models. Even classifiers achieving $F_1 > 0.93$ produce over 50\% downstream error risk.
5	
6	The consequences can be catastrophic. Under $K{=}3$ non-differential exposure misclassification, 83.4\% of confusion matrices cause \emph{sign reversal} of the estimated treatment effect, where the estimated direction of the causal relationship is opposite to the truth. This failure breaks the classical binary guarantee that non-differential misclassification biases estimates ``toward the null''~\cite{brenner1993}, a guarantee that many applied researchers implicitly rely upon. The breakdown is not an edge case: it persists even when classifier accuracy exceeds 70\% (13.7\% violation rate at diagonal $\geq 0.7$, comprising 2.1\% sign reversal and 11.7\% amplification).
7	
8	Why does the multi-class setting behave so differently? For binary classification, non-differential error can only attenuate the effect because the $2{\times}2$ stochastic confusion matrix preserves coefficient signs. With $K \geq 3$ categories, the confusion matrix can assign negative effective weights to categories with opposite-sign coefficients, enabling sign reversal~\cite{veirod_laake2001}. This fundamental asymmetry between binary and multi-class annotation error has received limited systematic treatment. \citet{brenner1993} identified the possibility of polytomous reversal but did not characterize it across causal designs. \citet{lee_wood_doughty2024} extended classifier error analysis to categorical variables and LLM classifiers, but covered only one DAG topology (unobserved confounding). No existing framework addresses how the same confusion matrix produces qualitatively different bias across different causal identification strategies.
9	
10	Compounding this gap, \citet{kim_garg2025} show that LLM errors are highly correlated across models (60\% agreement when both err), undermining the common assumption that ensembling multiple LLMs can mitigate annotation error. This finding strengthens the case that analyzing the \emph{structure} of annotation error, rather than simply reducing its magnitude, is essential for valid downstream inference.
11	
12	We address these gaps with three contributions:
13	
14	\begin{enumerate}
15	\item \textbf{Multi-class bias taxonomy.} We derive bias expressions for seven canonical DAG topologies (Figure~\ref{fig:dag_taxonomy}) under $K$-class non-differential misclassification (closed-form for confounding, exposure, and mediation; numerically validated for all seven). We establish that five topologies maintain a structural sign-flip guarantee (with formal proofs for three topologies and Monte Carlo validation for all seven) ($\tau_{\text{sign\_flip}} = 0$), while exposure and IV topologies can produce sign reversal. This taxonomy reveals that bias direction is determined by the \emph{interaction} between the confusion matrix and the DAG topology, not by either alone.
16	
17	\item \textbf{Annotation Sensitivity Values (ASVs).} We propose a unified sensitivity analysis framework with three complementary measures: magnitude ASV (E-value analogue for annotation error), significance ASV (hypothesis test filter for attenuating topologies), and sign-flip ASV (for exposure and IV). ASVs reveal a vulnerability spectrum from IV (maximally fragile, 52.6\% sign reversal; sign-flip ASV $= 1.1$--$6.7$) to M-bias (immune, ASV $= \infty$), providing practitioners with topology-aware robustness diagnostics.
18	
19	\item \textbf{Topology-aware correction guidance.} We evaluate five correction methods (naive plug-in, MLA, DSL, MC-SIMEX, PPI++) across all seven topologies and show that correction effectiveness is itself topology-dependent. A Frisch--Waugh--Lovell invariance result proves that matrix-based corrections achieve exactly 0\% bias reduction on the target coefficient for four topologies, while PPI++ achieves 93.8\% bias reduction but requires gold-standard labels. We further show that collapsing $K{=}3$ annotations to binary introduces additional bias varying 147$\times$ across topologies.
20	\end{enumerate}
21	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ac5393e9-f0e3-4b77-bb2b-4da53e1dafe0",
  "isSidechain": true,
  "promptId": "ae2d0870-295e-4835-a3f0-f41f20bd6a21",
  "agentId": "a1b64ac8a57b00a7e",
  "type": "user",
  "uuid": "47d8c08d-c581-47bd-9cc7-77c930abb714",
  "sourceToolAssistantUUID": "ac5393e9-f0e3-4b77-bb2b-4da53e1dafe0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/paper_agent_20baa82f",
  "sessionId": "35fb04f7-d2db-441f-a3b1-35490ca0d54b",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "eventual-sniffing-crane"
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-21T01:08:12.085Z_

<details open><summary>🔧 Tool call — Read · `toolu_01S22xwLMrTugr4rFZm477vh`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "47d8c08d-c581-47bd-9cc7-77c930abb714",
  "isSidechain": true,
  "agentId": "a1b64ac8a57b00a7e",
  "requestId": "req_011CbEpVpAD78wtoMigK6pYJ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "b250c85b-1c94-4df6-9705-3ede6961e453",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/paper_agent_20baa82f",
  "sessionId": "35fb04f7-d2db-441f-a3b1-35490ca0d54b",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "eventual-sniffing-crane",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017rF6omLVaGRTAAP3Wggu86",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 28018,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 28018,
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

_source line 8 · 2026-05-21T01:08:12.091Z_

<details><summary>↩ Tool result · `toolu_01S22xwLMrTugr4rFZm477vh`</summary>

```text
1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Measurement error in causal inference.}
5	The epidemiology literature has long studied misclassification bias through causal diagrams~\cite{gustafson2004}. \citet{hernan_cole2009} formalized the starred-node DAG framework for reasoning about measurement bias, distinguishing differential from non-differential error. For binary variables, \citet{ogburn_vanderweele2012} proved that non-differential confounder misclassification produces adjusted estimates between the crude and true values, precluding sign reversal. \citet{brenner1993} showed this guarantee breaks for polytomous confounders, and \citet{veirod_laake2001} derived bias expressions for multi-category exposure misclassification in Poisson regression. \citet{edwards_lessler_naimi2021} further demonstrated that dependent misclassification of covariate and exposure can bias in either direction. Our work extends this line by providing a systematic taxonomy across seven DAG topologies with closed-form expressions for the $K$-class case, identifying which topologies preserve and which break the sign-flip guarantee.
6	
7	\paragraph{Text classifier errors in causal studies.}
8	\citet{wood_doughty2018} first applied DAG reasoning to text classifier measurement error, noting matrix adjustment correction but without formal bias theorems. \citet{teblunthuis2024} provided the most complete binary treatment: four DAG scenarios with testable conditions and a Maximum Likelihood Adjustment method, but restricted to binary classification. \citet{yang_adomavicius2018} formalized the two-stage pipeline problem (data mining followed by econometric analysis) and proved that ML-generated variables systematically bias downstream regression. \citet{keith_jensen_oconnor2020} surveyed the text-and-causal-inference landscape, identifying classifier measurement error as a key open challenge. \citet{lee_wood_doughty2024} extended to categorical LLM classifiers on clinical data but covered only one topology (unobserved confounding). \citet{chen_bhattacharya_keith2024} used zero-shot NLP models as proxies in proximal causal inference, proving identification conditions for one DAG structure. We generalize across all seven topologies with multi-class confusion matrices, providing both bias expressions and sensitivity analysis tools absent from prior work.
9	
10	\paragraph{LLM annotation quality.}
11	Recent work has quantified the downstream risks of LLM annotation. \citet{baumann2025} demonstrated across 37 tasks that 31\% of hypotheses yield incorrect conclusions with LLM annotations. \citet{kim_garg2025} showed that LLM errors are 60\% correlated across models, undermining ensemble-based mitigation. \citet{messing2026} decomposed LLM pipeline variance via linear mixed models but explicitly excluded causal identification. \citet{stolwijk_boukes_trilling2025} found that LLM annotations differ from human annotations in prevalence even when per-sample accuracy is adequate, and \citet{cheng_mayya_sedoc2024} decomposed annotation measurement error into four source types. These works diagnose the annotation quality problem; our contribution provides the causal-analytic bridge connecting annotation error structure to downstream causal estimate validity.
12	
13	\paragraph{Sensitivity analysis for observational studies.}
14	Our ASV framework draws on the tradition of sensitivity analysis for unmeasured confounding~\cite{rosenbaum2002}. \citet{vanderweele_ding2017} introduced E-values as interpretable sensitivity measures, and \citet{ding_vanderweele2016} developed assumption-free sensitivity bounds. \citet{vanderweele_li2019} extended sensitivity analysis to differential measurement error but only for binary settings. \citet{smith_vanderweele2021} proposed bounds for multiple bias sources including misclassification. Our ASVs adapt the E-value philosophy (``how much bias would be needed to explain away the finding?'') to annotation-induced bias, with three complementary measures tailored to different topology-dependent failure modes.
15	
16	\paragraph{Correction methods.}
17	Prediction-powered inference~\cite{angelopoulos2023} and design-based supervised learning~\cite{egami_hinck_stewart_wei2023, gligoric2025} provide general frameworks for valid inference with ML-generated labels, combining predicted labels with small gold-standard samples. \citet{zrnic_candes2024} extended PPI via cross-prediction for improved efficiency. \citet{audinet2025} benchmarked these methods across datasets. These correction methods are complementary to our framework: our topology-dependent ASV analysis identifies \emph{when} correction is needed and \emph{which} failure mode to address, while PPI/DSL provide the \emph{how}.
18	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b250c85b-1c94-4df6-9705-3ede6961e453",
  "isSidechain": true,
  "promptId": "ae2d0870-295e-4835-a3f0-f41f20bd6a21",
  "agentId": "a1b64ac8a57b00a7e",
  "type": "user",
  "uuid": "8dc24af7-f3a6-4227-9a3c-72064edca541",
  "sourceToolAssistantUUID": "b250c85b-1c94-4df6-9705-3ede6961e453",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/paper_agent_20baa82f",
  "sessionId": "35fb04f7-d2db-441f-a3b1-35490ca0d54b",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "eventual-sniffing-crane"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-21T01:08:12.402Z_

<details open><summary>🔧 Tool call — Read · `toolu_0126WR1EHqvaSonQYVsMPsAw`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8dc24af7-f3a6-4227-9a3c-72064edca541",
  "isSidechain": true,
  "agentId": "a1b64ac8a57b00a7e",
  "requestId": "req_011CbEpVpAD78wtoMigK6pYJ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "ce2fa80d-6a14-4df6-a00c-4b8fdbcf14fc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/paper_agent_20baa82f",
  "sessionId": "35fb04f7-d2db-441f-a3b1-35490ca0d54b",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "eventual-sniffing-crane",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017rF6omLVaGRTAAP3Wggu86",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 28018,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 28018,
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

_source line 10 · 2026-05-21T01:08:12.427Z_

<details><summary>↩ Tool result · `toolu_0126WR1EHqvaSonQYVsMPsAw`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Setup and Notation}
5	\label{sec:notation}
6	
7	Let $A$ denote a true $K$-class categorical variable (e.g., sentiment with $K{=}3$ levels) and $A^*$ its observed, potentially misclassified version produced by an LLM annotator. The misclassification process is characterized by a $K{\times}K$ confusion matrix $C$ with entries $C_{jk} = P(A^*{=}j \mid A{=}k)$, where each column sums to one. Following \citet{hernan_cole2009}, we represent this measurement process using \emph{starred-node} DAGs: the true variable $A$ is latent, and the observed $A^*$ is connected to $A$ via a dashed measurement edge.
8	
9	\begin{definition}[Non-differential misclassification]
10	\label{def:nondiff}
11	Misclassification of $A$ is non-differential with respect to outcome $Y$ and covariates $\mathbf{Z}$ if $P(A^*{=}j \mid A{=}k, Y, \mathbf{Z}) = P(A^*{=}j \mid A{=}k) = C_{jk}$ for all $j,k$.
12	\end{definition}
13	
14	We study seven canonical DAG topologies (Figure~\ref{fig:dag_taxonomy})~\cite{pearl2009} in which $A$ occupies structurally distinct causal roles: confounder, exposure, mediator, collider, M-bias variable, front-door mediator, and instrument. Each role induces a different functional relationship between $C$ and the probability limit of the standard causal estimator, yielding topology-dependent bias.
15	
16	\subsection{Multi-Class Bias Expressions}
17	\label{sec:bias_expressions}
18	
19	For each topology, we derive the probability limit of the naive estimator that substitutes $A^*$ for $A$. Let $\tau$ denote the target causal parameter and $\hat{\tau}(A^*)$ the estimator using misclassified annotations.
20	
21	\paragraph{Confounding ($A$ = confounder).}
22	When $A$ confounds the $X{\to}Y$ relationship, the OLS estimator controlling for $A^*$ has probability limit
23	\begin{equation}
24	\label{eq:confounding}
25	\text{plim}\;\hat{\tau}(A^*) = \bigl(\mathbb{E}[Z^{\prime}Z]\bigr)^{-1}\mathbb{E}[Z^{\prime}X]\,\boldsymbol{\beta},
26	\end{equation}
27	where $Z = [X, \text{dummies}(A^*)]$, $\boldsymbol{\beta}$ contains the true coefficients, and the target parameter $\tau$ is the coefficient on $X$. Misclassification produces residual confounding that monotonically approaches the omitted variable bias, but the sign of $\hat{\tau}$ is preserved: $\tau_{\text{sign\_flip}} = 0$ structurally.
28	
29	\paragraph{Exposure ($A$ = treatment variable).}
30	When $A$ is the exposure of interest, the biased coefficient for category $j$ becomes a weighted combination of true coefficients:
31	\begin{equation}
32	\label{eq:exposure}
33	\text{plim}\;\hat{\beta}_j(A^*) = \sum_{k=1}^{K} w_{jk}\,\beta_k,
34	\end{equation}
35	where $w_{jk}$ depends on the confusion matrix $C$ and the marginal distribution of $A$. Unlike the binary case, where non-differential misclassification guarantees attenuation toward the null~\cite{brenner1993}, the $K{\geq}3$ case permits $w_{jk}$ to assign negative weight to categories with opposite-sign coefficients, producing \emph{sign reversal}. A near-permutation confusion matrix effectively swaps category labels, making sign reversal the dominant outcome (83.4\% under uniform Dirichlet prior). This failure mode is structurally impossible at $K{=}2$ because a $2{\times}2$ stochastic matrix with positive diagonal cannot reverse the sign of a single coefficient.
36	
37	\paragraph{Mediation ($A$ = mediator).}
38	When $A$ mediates the $X{\to}Y$ relationship, the direct effect estimator controlling for $A^*$ has probability limit
39	\begin{equation}
40	\label{eq:mediation}
41	\text{plim}\;\hat{\tau}_{\text{direct}}(A^*) = \tau_{\text{direct}} + \bigl(1 - \lambda(C)\bigr)\,\tau_{\text{indirect}},
42	\end{equation}
43	where $\lambda(C) \in [0,1]$ summarizes the weighted attenuation structure (see Appendix~\ref{app:proof}, Proposition~3 for the general multi-dimensional form), with $\lambda(I) = 1$ under perfect classification. Misclassification compresses the mediator's explanatory power ($\lambda(C) < 1$), causing the residual indirect effect $(1{-}\lambda)\tau_{\text{indirect}}$ to be absorbed into the direct path estimate. This produces upward bias in $|\hat{\tau}_{\text{direct}}|$ but preserves the sign ($\tau_{\text{sign\_flip}} = 0$).
44	
45	\paragraph{Collider ($A$ = collider, conditioned on $A^*$).}
46	Conditioning on a collider $A$ of $X$ and $Y$ opens a spurious path. When we condition on $A^*$ instead, misclassification attenuates this spurious association because $A^*$ is a noisy proxy for $A$. The collider topology thus exhibits a \emph{protective} property: annotation error reduces rather than amplifies the bias from collider stratification, with $\tau_{\text{sign\_flip}} = 0$.
47	
48	\paragraph{M-bias ($A$ = intermediate collider).}
49	In the M-shaped DAG ($U_1 \to X$, $U_1 \to A$, $U_2 \to A$, $U_2 \to Y$, $X \to Y$), adjusting for $A$ introduces a small spurious association via the M-bias path~\cite{greenland2003}. Misclassifying $A$ weakens this adjustment, reducing the M-bias. This topology is \emph{immune}: $\hat{\tau}(A^*)$ is closer to $\tau$ than $\hat{\tau}(A)$ for all non-trivial confusion matrices, yielding $\text{ASV} = \infty$.
50	
51	\paragraph{Front-door ($A$ = front-door mediator).}
52	In the front-door DAG ($X \to A \to Y$ with unmeasured $U \to X$, $U \to Y$), the front-door estimator~\cite{bellemare_bloem2024} uses $A$ to identify the causal effect of $X$ on $Y$ despite unmeasured confounding. Misclassification of $A$ attenuates the estimated $X \to A$ and $A \to Y$ relationships, producing moderate bias. The sign of the causal effect is preserved ($\tau_{\text{sign\_flip}} = 0$).
53	
54	\paragraph{Instrumental variable ($A$ = instrument).}
55	The Wald estimator~\cite{angrist_imbens1995} in the binary instrument case takes the form $\hat{\tau}_{\text{IV}} = \hat{\text{cov}}(A^*, Y) / \hat{\text{cov}}(A^*, X)$. For $K{\geq}3$, the multi-class analog replaces the scalar first-stage coefficient with a vector of category-specific coefficients, but the core vulnerability persists: $C$ enters the denominator directly, so misclassification can drive individual first-stage coefficients toward zero or reverse their sign, causing the ratio estimator to diverge or flip. Under random Dirichlet confusion matrices, 52.6\% produce $\tau$-specific sign reversal, making IV the most fragile topology.
56	
57	\paragraph{Structural sign-flip guarantee.}
58	\begin{proposition}
59	\label{prop:signflip}
60	Under non-differential misclassification with $C_{kk} > 0$ for all $k$ (no category has zero self-classification probability), and provided the true effect and the omitted-variable bias share the same sign (a condition satisfied under standard DGP parameterizations), the following topologies satisfy $\tau_{\text{sign\_flip}} = 0$: confounding, mediation, collider, M-bias, and front-door. Sign reversal is possible only in the exposure and IV topologies.
61	\end{proposition}
62	
63	\emph{Proof sketch.}
64	For confounding, a Frisch--Waugh--Lovell decomposition shows the bias is $B(C) = R(C)/D(C)$, where $D(C)>0$ and $|R(C)|$ is bounded by the Cauchy--Schwarz inequality. The bound ensures $|B(C)| < |\tau|$ whenever the true effect and the omitted-variable bias share the same sign, guaranteeing sign preservation for all column-stochastic $C$. This sign-alignment condition is parameter-dependent but holds generically: it is satisfied whenever the confounder's effect on the treatment and outcome have the same direction, which is the standard assumption motivating adjustment in the first place. For the collider, we prove algebraically that conditioning on $A^*$ instead of $A$ strictly attenuates the spurious collider association, so $|\hat{\tau}(A^*)| < |\hat{\tau}(A)|$ for all non-trivial $C$, precluding sign reversal. Mediation and M-bias sign preservation is validated numerically with zero violations across 100{,}000 random matrices. For exposure, we construct an explicit $K{=}3$ counterexample with diagonal-dominant $C$ ($C_{kk}{>}0.5$) yielding sign reversal. Full proofs and the counterexample are in Appendix~\ref{app:proof}.
65	
66	\subsection{Annotation Sensitivity Values}
67	\label{sec:asv}
68	
69	We introduce Annotation Sensitivity Values (ASVs) as a unified sensitivity analysis framework, analogous to E-values for unmeasured confounding~\cite{vanderweele_ding2017} but designed for annotation-induced bias.
70	
71	\paragraph{Parameterization.}
72	We parameterize the confusion matrix as $C(\delta) = (1{-}\delta)I + \delta C_0$, where $C_0$ is a reference confusion matrix (e.g., estimated from a validation set) and $\delta \in [0, \infty)$ controls the severity of misclassification. At $\delta{=}0$, classification is perfect; at $\delta{=}1$, classification matches $C_0$; for $\delta{>}1$, misclassification exceeds the reference level.
73	
74	\paragraph{Three ASV types.}
75	We define three complementary sensitivity measures, each answering a distinct practical question:
76	
77	\begin{enumerate}
78	\item \textbf{Magnitude ASV}: $\delta^*_{\text{mag}} = \min\{\delta : |\text{plim}\;\hat{\tau}(C(\delta)) - \tau| > \epsilon\}$, the minimum misclassification level at which bias exceeds a threshold $\epsilon$. This is directly analogous to the E-value and applies to all topologies.
79	
80	\item \textbf{Significance ASV}: $\delta^*_{\text{sig}} = \min\{\delta : |\text{plim}\;\hat{\tau}(C(\delta))| < z_{\alpha/2} \cdot SE(N)\}$, the minimum misclassification level at which the effect becomes statistically non-significant. This is relevant for attenuating topologies (confounding, mediation, collider) where bias reduces the observed effect.
81	
82	\item \textbf{Sign-flip ASV}: $\delta^*_{\text{sf}} = \min\{\delta : \text{sign}(\text{plim}\;\hat{\tau}(C(\delta))) \neq \text{sign}(\tau)\}$, the minimum misclassification level at which the estimated effect changes sign. This applies only to exposure and IV topologies.
83	\end{enumerate}
84	
85	\begin{theorem}[Envelope monotonicity]
86	\label{thm:monotone}
87	For confounding, exposure, and mediation topologies, the bias envelope $|\text{plim}\;\hat{\tau}(C(\delta)) - \tau|$ is monotonically non-decreasing in $\delta$ for $\delta \geq 0$.
88	\end{theorem}
89	
90	Monotonicity is verified numerically for all seven topologies with zero violations across 500 scenarios per topology.
91	
92	\paragraph{$N$-sensitivity.}
93	The significance ASV depends on sample size through $SE(N)$. We define the critical sample size $N^*$ as the smallest $N$ at which $z_{\alpha/2} \cdot SE(N) < |\tau|$. For $N < N^*$, the significance ASV equals zero (all rejections blocked); for $N > N^*$, the ASV jumps to infinity (no rejections blocked). This sharp phase transition provides practitioners with a concrete minimum sample size for their topology.
94	
95	\subsection{Binarization Collapse}
96	\label{sec:binarization_method}
97	
98	A common simplification in applied work is to collapse $K$-class annotations to binary before analysis. We quantify the additional bias from this ``binarization collapse'' as $\Delta = |\text{bias}_{K} - \text{bias}_{K \to 2}|$, where $\text{bias}_K$ is the bias under the original $K$-class confusion matrix and $\text{bias}_{K \to 2}$ is the bias after folding categories into two groups with the corresponding collapsed $2{\times}2$ confusion matrix. This quantity captures the information lost by discarding the multi-class error structure.
99	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ce2fa80d-6a14-4df6-a00c-4b8fdbcf14fc",
  "isSidechain": true,
  "promptId": "ae2d0870-295e-4835-a3f0-f41f20bd6a21",
  "agentId": "a1b64ac8a57b00a7e",
  "type": "user",
  "uuid": "d1347c91-cbf4-4352-b782-e8c3f681acb8",
  "sourceToolAssistantUUID": "ce2fa80d-6a14-4df6-a00c-4b8fdbcf14fc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/paper_agent_20baa82f",
  "sessionId": "35fb04f7-d2db-441f-a3b1-35490ca0d54b",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "eventual-sniffing-crane"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-21T01:08:12.489Z_

<details open><summary>🔧 Tool call — Read · `toolu_01XrEurgUc3NTJBT84p2xiom`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d1347c91-cbf4-4352-b782-e8c3f681acb8",
  "isSidechain": true,
  "agentId": "a1b64ac8a57b00a7e",
  "requestId": "req_011CbEpVpAD78wtoMigK6pYJ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d5da3c94-f765-41f8-941c-ccbcb610c154",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/paper_agent_20baa82f",
  "sessionId": "35fb04f7-d2db-441f-a3b1-35490ca0d54b",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "eventual-sniffing-crane",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017rF6omLVaGRTAAP3Wggu86",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 28018,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 28018,
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

_source line 12 · 2026-05-21T01:08:12.497Z_

<details><summary>↩ Tool result · `toolu_01XrEurgUc3NTJBT84p2xiom`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We evaluate the multi-class bias taxonomy and ASV framework through analytical derivations validated by Monte Carlo simulation, covering seven canonical DAG topologies under $K{=}3$ non-differential misclassification.
5	
6	\subsection{Setup}
7	\label{sec:setup}
8	
9	We study seven DAG topologies where annotation variable $A$ enters at structurally distinct positions: confounding, exposure, mediation, collider, M-bias, front-door, and instrumental variable (IV). For each topology, we sample $K{\times}K$ confusion matrices from a Dirichlet$(1,1,1)$ prior (each column independently), generating 100{,}000 random matrices per configuration. Each matrix defines a non-differential misclassification mechanism $C_{jk} = P(A^*{=}j \mid A{=}k)$.
10	
11	For every sampled $C$, we compute the analytical probability limit of the causal estimator and validate it against Monte Carlo simulation with $N{=}10{,}000$ samples per replication. ASV experiments use the parameterization $C(\delta) = (1{-}\delta)I + \delta C_0$, where $\delta{=}0$ recovers perfect classification and $\delta{=}1$ yields the reference matrix $C_0$.
12	
13	\subsection{Bias Taxonomy}
14	\label{sec:taxonomy_results}
15	
16	\paragraph{Theory-MC agreement.}
17	Analytical probability limits match Monte Carlo estimates within 95\% confidence intervals across all seven topologies and all sampled confusion matrices, confirming the closed-form bias expressions derived in Section~\ref{sec:method}.
18	
19	\paragraph{Exposure DAG: catastrophic sign reversal.}
20	Under the full Dirichlet$(1,1,1)$ prior, 85\% of $K{=}3$ confusion matrices produce bias that violates the binary ``toward-null'' guarantee. More critically, 83.4\% of matrices cause \emph{sign reversal} of at least one coefficient. The two failure modes are distinct: for a coefficient with true value $\beta_1{=}1.0$, a near-permutation $C$ produces $\hat{\gamma}_1{=}{-}0.84$ (sign reversal, magnitude $0.84{\times}$); for $\beta_2{=}{-}0.5$, the same $C$ yields $\hat{\gamma}_2{=}{-}1.41$ (same-sign amplification, $2.83{\times}$).
21	
22	This finding persists in practically relevant subspaces. When restricting to confusion matrices with diagonal entries $\geq 0.7$ (typical of current LLM classifiers achieving $F_1 > 0.8$), the violation rate remains 13.7\% with 2.1\% sign reversal and 11.7\% amplification. Even at diagonal $\geq 0.9$, violation persists at 11.9\%. In contrast, the $K{=}2$ control confirms that all six tested binary confusion matrices maintain the classical bias-toward-null guarantee~\cite{brenner1993}, establishing that the multi-class failure is structurally distinct from the binary case.
23	
24	\paragraph{Structural guarantee for non-exposure topologies.}
25	Five of seven topologies exhibit a structural guarantee: $\tau$-specific sign flip rate equals exactly zero across all sampled confusion matrices (Table~\ref{tab:taxonomy}). Confounding, mediation, and front-door topologies show 100\% violation and amplification rates but never reverse the sign of the target causal parameter. Collider misclassification attenuates the spurious association induced by conditioning, providing a form of protection. M-bias shows the weakest sensitivity overall (53.2\% violation, 10.4\% amplification) because annotation error on a collider variable reduces, rather than amplifies, the spurious M-bias path.
26	
27	\paragraph{IV: Wald estimator instability.}
28	The instrumental variable topology is the sole exception among non-exposure DAGs. The Wald estimator's first stage involves $C$ directly in the denominator, and 52.6\% of random confusion matrices cause the denominator to change sign, producing $\tau$-specific sign reversal. This rate remains stable across $K{=}3,5,7$, indicating that IV fragility is a structural property of the Wald estimator rather than a finite-$K$ artifact.
29	
30	\paragraph{Cross-$K$ robustness.}
31	Experiments at $K{=}5$ and $K{=}7$ (100{,}000 random matrices per topology) confirm that all structural patterns from $K{=}3$ persist. The sign-flip guarantee holds for the same five topologies, and IV sign-flip rates remain within 51--53\%. Worst-case bias magnitudes decrease modestly with $K$ for most topologies but increase for IV at low accuracy (worst case 14.0$\times$ at $K{=}3$ diagonal $\geq 0.5$).
32	
33	\begin{table}[t]
34	\centering
35	\caption{Bias characteristics of $K{=}3$ non-differential misclassification across 7 DAG topologies. Violation: $|\hat{\tau}| > |\tau|$; Sign flip: $\text{sign}(\hat{\tau}) \neq \text{sign}(\tau)$; Amplification: $|\hat{\tau}| > |\tau|$ with same sign. Rates computed over 100{,}000 Dirichlet$(1,1,1)$ random confusion matrices with $N{=}10{,}000$.}
36	\label{tab:taxonomy}
37	\small
38	\begin{tabular}{lcccc}
39	\toprule
40	\textbf{Topology} & \textbf{Violation} & \textbf{Sign Flip} & \textbf{Amplif.} & $\tau_{\text{sf}}{=}0$? \\
41	\midrule
42	Confounding & 100\% & 0\% & 100\% & \checkmark \\
43	Exposure & 85\% & 83.4\% & 14.1\% & \ding{55} \\
44	Mediation & 100\% & 0\% & 100\% & \checkmark \\
45	Front-door & 100\% & 0\% & 100\% & \checkmark \\
46	Collider & 100\% & 0\% & 100\% & \checkmark \\
47	M-bias & 53.2\% & 0\% & 10.4\% & \checkmark \\
48	IV & 100\% & 52.6\% & 100\% & \ding{55} \\
49	\bottomrule
50	\end{tabular}
51	\end{table}
52	
53	The bias distributions across topologies are visualized in Figure~\ref{fig:bias_distribution}, where the exposure panel's dominant red region (sign reversal) contrasts with the symmetric attenuation patterns of other topologies.
54	
55	\subsection{ASV Framework Validation}
56	\label{sec:asv_results}
57	
58	\paragraph{Envelope monotonicity.}
59	The ASV envelope (bias magnitude as a function of $\delta$) is monotonically non-decreasing for all seven topologies, with zero violations across all tested scenarios. This validates the theoretical monotonicity property and confirms that $\delta$ serves as a meaningful ``dial'' controlling annotation error severity.
60	
61	\paragraph{Magnitude ASV.}
62	Table~\ref{tab:asv_grid} reports magnitude ASV ranges at $\tau{=}0.5$ with a 10\% bias threshold. The ranking from most fragile to most robust is: front-door (0.064--0.387) $<$ mediation (0.076--0.454) $<$ confounding (0.081--0.487) $<$ IV (0.101--0.607) $<$ collider (0.338--2.028) $<$ M-bias ($\infty$). The collider's high ASV reflects its protective nature: misclassification attenuates the spurious association rather than amplifying it. M-bias achieves infinite ASV because annotation error on the collider variable $A$ only reduces the already-small bias from the M-shaped confounding path.
63	
64	\paragraph{Significance power.}
65	At $\tau{=}0.05$, the significance ASV filter achieves 100\% power for confounding, front-door, and M-bias (96--100\%). Power drops to 0\% for mediation, collider, and IV. For mediation and collider, this is correct behavior: these are attenuating topologies where the biased effect at small $\tau$ falls below the detection threshold $z_{\alpha/2} \cdot SE$, and the ASV filter correctly blocks all rejections. For IV, the Wald estimator is immediately fragile ($\text{signif\_ASV} \approx 0$), reflecting its extreme sensitivity to any annotation error. Type~I error is 0\% across all topologies.
66	
67	\paragraph{Sign-flip ASV.}
68	For exposure, 83.4\% of reference matrices $C_0$ yield $\tau_{\text{sign\_flip}} < 1$, indicating catastrophic sensitivity to annotation error. For IV, sign-flip ASV ranges from 1.1 to 6.7, indicating moderate-to-high sensitivity depending on the reference matrix structure. All other topologies have undefined sign-flip ASV (no sign reversal is possible).
69	
70	The complete sensitivity ranking across ASV types is shown in Figure~\ref{fig:asv_ranking}, which reveals that different ASV types can yield different vulnerability orderings across topologies.
71	
72	\begin{table}[t]
73	\centering
74	\caption{ASV type applicability and sensitivity across DAG topologies. Magnitude ASV at $\tau{=}0.5$, 10\% threshold. Power at $\tau{=}0.05$ significance filter. \checkmark: effective and recommended; ($\checkmark$): applicable but less informative; ---: not applicable.}
75	\label{tab:asv_grid}
76	\small
77	\begin{tabular}{lcccl}
78	\toprule
79	\textbf{Topology} & \textbf{Mag. ASV} & \textbf{Signif.} & \textbf{Sign-flip} & \textbf{Rank} \\
80	\midrule
81	IV & 0.101--0.607 & 0\% & 1.1--6.7 & 1 (fragile) \\
82	Front-door & 0.064--0.387 & 100\% & --- & 2 \\
83	Confounding & 0.081--0.487 & 100\% & --- & 3 \\
84	Mediation & 0.076--0.454 & 0\% & --- & 4 \\
85	Collider & 0.338--2.028 & 0\% & --- & 5 \\
86	M-bias & $\infty$ & 96--100\% & --- & 6 (immune) \\
87	Exposure & --- & --- & 83.4\%$^*$ & --- \\
88	\bottomrule
89	\multicolumn{5}{l}{\scriptsize $^*$Fraction of $C_0$ with $\tau_{\text{sign\_flip}} < 1$. Exposure uses sign-flip ASV exclusively.}
90	\end{tabular}
91	\end{table}
92	
93	\subsection{$N$-Sensitivity}
94	\label{sec:n_sensitivity}
95	
96	The significance ASV exhibits a sharp phase transition as a function of sample size. For mediation at $\tau{=}0.05$ with a symmetric mild reference matrix $C_0$: at $N{=}1{,}000$, naive power reaches 0.89 while ASV-filtered power is exactly 0 (the filter blocks all rejections because $1.96 \cdot SE > \tau$). This pattern persists through $N{=}5{,}000$ (naive power 1.0, ASV power 0). At $N{=}10{,}000$, a sharp transition occurs: ASV power jumps to 1.0, matching naive power with zero extra conservatism.
97	
98	This binary behavior (block-all below $N^*$, pass-all above $N^*$) arises because the significance ASV depends on whether $\tau$ exceeds the critical value $z_{\alpha/2} \cdot SE(N)$. The critical sample size $N^* \approx 6{,}000$--$10{,}000$ for this configuration is analytically computable, providing practitioners with a concrete minimum sample size requirement for their specific topology and effect size.
99	
100	\subsection{Binarization Collapse}
101	\label{sec:binarization}
102	
103	Collapsing $K{=}3$ annotations to binary introduces additional bias $\Delta = |\text{bias}_{K=3} - \text{bias}_{K \to 2}|$ that varies by 147$\times$ across topologies (Figure~\ref{fig:binarization}). Under 100{,}000 Dirichlet samples, M-bias shows negligible collapse ($\bar{\Delta}{=}0.006$, with 0\% of matrices exceeding $\Delta{>}0.05$), while IV exhibits severe collapse ($\bar{\Delta}{=}0.926$, 100\% exceeding the threshold). Exposure ($\bar{\Delta}{=}0.516$) and IV also introduce sign flips during binarization (14\% and 17.5\% respectively), a phenomenon absent in the other four topologies.
104	
105	These results demonstrate that binarization is not a safe simplification. For exposure and IV topologies, collapsing multi-class annotations to binary can introduce bias comparable to, or exceeding, the original misclassification bias.
106	
107	\subsection{Empirical Validation}
108	\label{sec:empirical}
109	
110	We validate the theoretical framework using real LLM confusion matrices estimated from HumAID~\cite{alam2021humaid}, a 10-class disaster response classification task ($K{=}10$). Three frontier LLMs (Llama-4-Maverick, Qwen3-235B, DeepSeek-Chat) annotate HumAID samples under zero-shot and few-shot prompting, yielding 8 usable model$\times$prompt configurations (one configuration excluded due to API failure). Each configuration produces a $10{\times}10$ confusion matrix $C$, which we plug into the analytical bias expressions from Section~\ref{sec:method} for all seven topologies.
111	
112	\paragraph{Theory--practice alignment.}
113	The empirical bias ranking across topologies matches the theoretical predictions from the random-matrix analysis. IV produces the largest bias (12.4--42.1\% relative bias across configurations), followed by exposure (9.0--17.4\%), mediation and front-door (10.7--14.8\% each), while collider (4.1--5.6\%), confounding (4.9--6.2\%), and M-bias (5.1--6.5\%) remain below 10\%. This ordering is consistent with the ASV vulnerability spectrum from Section~\ref{sec:asv_results}: IV is maximally fragile and collider is near-immune. Zero sign reversals occur across all 56 topology$\times$configuration combinations ($8 \times 7$), consistent with the diagonal dominance of all estimated confusion matrices (mean diagonal 0.671--0.724).
114	
115	\paragraph{ASV diagnostic results.}
116	Of 63 scenario-level ASV evaluations ($9 \times 7$; the failed configuration contributes 7 trivially-safe entries), 49.2\% (31/63) are flagged as ASV-unsafe, indicating that roughly half of LLM annotation scenarios require correction or sensitivity reporting. Magnitude ASV values are triggered for four topologies: IV (0.31--0.83), mediation (0.62--0.90), front-door (0.62--0.91), and exposure (0.65--1.11). The remaining three topologies (confounding, collider, M-bias) produce bias below the 10\% threshold across all configurations, requiring no ASV report (Figure~\ref{fig:asv_heatmap}). Sign-flip ASV is undefined for all configurations, consistent with the zero observed sign reversals at $K{=}10$ with diagonal-dominant $C$.
117	
118	\paragraph{Confusion matrix structure.}
119	Across models, DeepSeek-Chat achieves the highest mean diagonal accuracy (0.724), followed by Qwen3-235B (0.710) and Llama-4-Maverick (0.678). Macro $F_1$ ranges from 0.614 to 0.690, reflecting the difficulty of 10-class classification. Critically, $F_1$ does not predict downstream causal bias: within the narrow $F_1$ range of 0.614--0.690, relative bias varies by an order of magnitude across topologies---from 4.1\% (collider) to 42.1\% (IV)---demonstrating that topology, not annotator quality, determines downstream risk (Figure~\ref{fig:f1_vs_bias}). All three models share a common failure mode: class 6 (``other relevant information'') is the dominant off-diagonal confusion target, absorbing misclassifications from multiple substantive categories. Inter-model error correlations are low (0.051--0.157 across model pairs), indicating that the three LLMs make largely independent errors. This low correlation is favorable for multi-annotator correction strategies such as PPI++ with model-diverse gold-label subsets.
120	
121	\paragraph{Scope and ongoing work.}
122	The HumAID results ($K{=}10$) validate the framework at high $K$ where confusion matrices are large and classification is challenging. Validation at $K{=}3$ (VAST stance detection) and $K{=}2$ (CivilComments toxicity) is in progress and will extend coverage to the regime where sign reversal is theoretically possible (exposure at $K{=}3$) and where comparison with the classical binary guarantee~\cite{brenner1993} is direct ($K{=}2$).
123	
124	\begin{figure}[t]
125	\centering
126	\includegraphics[width=\columnwidth]{fig5_f1_vs_bias.pdf}
127	\caption{Topology determines downstream causal bias, not F1. Each point represents one LLM annotator $\times$ topology combination from HumAID ($K{=}10$, 8 configurations $\times$ 7 topologies $=$ 56 points). Within a narrow $F_1$ range (0.614--0.690), relative bias varies $10{\times}$: IV reaches 42.1\% while collider stays below 5.6\%.}
128	\label{fig:f1_vs_bias}
129	\end{figure}
130	
131	\begin{figure}[t]
132	\centering
133	\includegraphics[width=\columnwidth]{fig6_asv_heatmap.pdf}
134	\caption{ASV magnitude ranges across topologies for HumAID ($K{=}10$). Left: magnitude ASV ($\delta^*$) range across 8 LLM configurations; lower values indicate greater fragility. ``Safe'' topologies never exceed the 10\% bias threshold. Right: percentage of configurations flagged as ASV-unsafe.}
135	\label{fig:asv_heatmap}
136	\end{figure}
137	
138	\subsection{Correction Guidance}
139	\label{sec:correction}
140	
141	We evaluate five correction methods across all seven topologies under six error structures (210 configurations total): naive plug-in (replace $A$ with $A^*$ after applying $C^{-1}$), maximum likelihood adjustment (MLA), design-based supervised learning (DSL)~\cite{egami_hinck_stewart_wei2023}, MC-SIMEX, and prediction-powered inference (PPI++)~\cite{angelopoulos2023}.
142	
143	\paragraph{Frisch--Waugh--Lovell invariance.}
144	For four topologies where $A$ enters as a covariate rather than the estimand (confounding, mediation, collider, M-bias), the Frisch--Waugh--Lovell theorem implies that applying $C^{-1}$ to the dummy variables cannot change the coefficient on $T$: the column space of the design matrix is invariant to invertible transformations of the regressors. Naive plug-in and MLA achieve exactly 0.0\% bias reduction on the $T$ coefficient across all four topologies, confirming this theoretical prediction.
145	
146	\paragraph{Method ranking.}
147	PPI++ achieves the highest grand-mean bias reduction (93.8\%) and is the only method to reach nominal coverage (96.8\%). MC-SIMEX provides moderate correction (20.9\% bias reduction) without requiring gold-standard labels but achieves only 37.6\% coverage. DSL, naive plug-in, and MLA produce negative grand-mean bias reduction ($-$144.8\%, $-$20.0\%, $-$37.4\% respectively), indicating that on average these methods increase bias across topologies.
148	
149	\begin{table}[t]
150	\centering
151	\caption{Bias reduction (\%) by correction method and DAG topology (mean across 6 error structures). Positive = reduced bias; negative = increased bias. Naive/MLA show 0.0\% for FWL-invariant topologies because $C^{-1}$ cannot change the $T$ coefficient. \textbf{Bold}: best method per topology; \underline{underline}: best gold-free method.}
152	\label{tab:correction}
153	\small
154	\begin{tabular}{lccccc}
155	\toprule
156	\textbf{Topology} & \textbf{Naive} & \textbf{MLA} & \textbf{DSL} & \textbf{SIMEX} & \textbf{PPI++} \\
157	\midrule
158	Confounding & 0.0 & 0.0 & \underline{49.8} & 35.9 & \textbf{99.3} \\
159	Mediation & 0.0 & 0.0 & \underline{70.3} & 42.4 & \textbf{98.8} \\
160	Collider & 0.0 & 0.0 & $-$89.2 & \underline{37.1} & \textbf{97.0} \\
161	M-bias & 0.0 & 0.0 & $-$768 & \underline{25.7} & \textbf{63.7} \\
162	\midrule
163	Front-door & $-$53.5 & $-$112.5 & \underline{$-$29.2} & $-$55.7 & \textbf{99.3} \\
164	Exposure & $-$45.6 & $-$89.9 & $-$59.6 & \underline{$-$3.8} & \textbf{98.8} \\
165	IV & $-$40.9 & $-$59.2 & $-$187.4 & \underline{64.7} & \textbf{99.5} \\
166	\midrule
167	Grand mean & $-$20.0 & $-$37.4 & $-$144.8 & 20.9 & \textbf{93.8} \\
168	\bottomrule
169	\end{tabular}
170	\end{table}
171	
172	\paragraph{DSL topology sensitivity.}
173	DSL corrects bias only where the misclassified variable enters as a confounder or mediator: confounding (49.8\%) and mediation (70.3\%). For the remaining five topologies, DSL increases bias, with M-bias exhibiting catastrophic amplification ($-$768\%, worst single scenario $-$2537\% under realistic LLM error). The mechanism is structural: DSL's EM procedure assumes annotation error is the sole source of misspecification, but in topologies with additional bias sources (the spurious M-bias path, collider conditioning bias, Wald denominator instability), DSL's reweighting amplifies these pre-existing biases rather than correcting them.
174	
175	\paragraph{PPI++ dominance and limitations.}
176	PPI++ wins 40 of 42 topology$\times$error-structure configurations (95.2\%). However, it requires a gold-standard labeled subset, and M-bias is its sole weak topology: mean bias reduction drops to 63.7\% (vs.\ 97.0--99.5\% for other topologies), with worst-case $-$25.1\% under realistic LLM errors. Coverage remains high (99\%) even when bias reduction is negative, indicating that PPI++ widens confidence intervals enough to maintain validity but at the cost of precision. The likely mechanism is that M-bias produces inherently small bias ($\bar{\Delta}{<}0.03$), so the variance from the gold-label subset dominates the correction signal.
177	
178	\paragraph{MC-SIMEX as gold-free fallback.}
179	MC-SIMEX provides the only positive bias reduction without gold labels for the IV topology (64.7\%), where PPI++ also performs well but requires gold labels that may be unavailable for instrument validation. For practitioners without access to gold-standard annotations, MC-SIMEX offers a viable correction path, particularly for IV designs where the Wald estimator is most vulnerable.
180	
181	\paragraph{Topology-dependent guidance.}
182	Correction method effectiveness is itself topology-dependent: no single method dominates across all causal designs. For FWL-invariant topologies (confounding, mediation, collider, M-bias), matrix-based corrections are provably ineffective on the target coefficient; only PPI++ or MC-SIMEX can reduce bias. For exposure and IV, where sign reversal is possible, PPI++ with gold labels is the recommended first-line correction. When gold labels are unavailable, MC-SIMEX provides moderate correction for IV (64.7\%), but no gold-free method reliably corrects exposure sign reversal. DSL should be restricted to confounding and mediation designs; applying it to other topologies risks catastrophic bias amplification. Algorithm~\ref{alg:correction} summarizes this guidance as a decision procedure.
183	
184	\begin{algorithm}[t]
185	\caption{Correction method selection for LLM-annotated causal inference.}
186	\label{alg:correction}
187	\small
188	\begin{algorithmic}[1]
189	\Require DAG topology $\mathcal{T}$, gold-label availability $G \in \{\textsc{yes}, \textsc{no}\}$
190	\Ensure Recommended method $M$, risk level $R$
191	\Statex
192	\Statex \textbf{Step 1: Assess risk level}
193	\If{$\mathcal{T} \in \{\text{M-bias}\}$}
194	    \State $R \gets \textsc{Low}$ \Comment{$|\text{bias}| < 0.04$ for all $C$}
195	\ElsIf{$\mathcal{T} \in \{\text{Conf., Med., Coll., Front-door}\}$}
196	    \State $R \gets \textsc{Medium}$ \Comment{bounded bias, no sign reversal}
197	\Else \Comment{Exposure, IV}
198	    \State $R \gets \textsc{High}$ \Comment{sign reversal: 83.4\% / 52.6\%}
199	\EndIf
200	\Statex
201	\Statex \textbf{Step 2: Select correction method}
202	\If{$G = \textsc{yes}$}
203	    \If{$\mathcal{T} = \text{M-bias}$}
204	        \State $M \gets \textsc{None}$ \Comment{PPI++ only 63.7\%; no correction preferred}
205	    \Else
206	        \State $M \gets \text{PPI++}$ \Comment{93.8\% mean bias red., 96.8\% coverage}
207	    \EndIf
208	\Else \Comment{no gold labels}
209	    \If{$\mathcal{T} \in \{\text{Confounding, Mediation}\}$}
210	        \State $M \gets \text{DSL}$ \Comment{49.8\% / 70.3\% bias reduction}
211	    \ElsIf{$\mathcal{T} = \text{IV}$}
212	        \State $M \gets \text{MC-SIMEX}$ \Comment{64.7\% bias reduction}
213	    \ElsIf{$\mathcal{T} \in \{\text{Collider, M-bias}\}$}
214	        \State $M \gets \text{MC-SIMEX}$ \Comment{37.1\% / 25.7\% bias reduction}
215	    \Else
216	        \State $M \gets \emptyset$; flag: acquire gold labels \Comment{no reliable gold-free method}
217	    \EndIf
218	\EndIf
219	\Statex
220	\Statex \textbf{Step 3: FWL invariance warning}
221	\If{$\mathcal{T} \in \{\text{Conf., Med., Coll., M-bias}\}$}
222	    \State Skip Naive plug-in and MLA \Comment{0\% bias red.\ on $T$ coeff.}
223	\EndIf
224	\State \Return $(M, R)$
225	\end{algorithmic}
226	\end{algorithm}
227	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d5da3c94-f765-41f8-941c-ccbcb610c154",
  "isSidechain": true,
  "promptId": "ae2d0870-295e-4835-a3f0-f41f20bd6a21",
  "agentId": "a1b64ac8a57b00a7e",
  "type": "user",
  "uuid": "1cf04012-d1d4-4573-ac30-9dc91aa2a172",
  "sourceToolAssistantUUID": "d5da3c94-f765-41f8-941c-ccbcb610c154",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/paper_agent_20baa82f",
  "sessionId": "35fb04f7-d2db-441f-a3b1-35490ca0d54b",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "eventual-sniffing-crane"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-21T01:08:12.916Z_

<details open><summary>🔧 Tool call — Read · `toolu_0165q2CP26GEvG7BtvHyQQ7y`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1cf04012-d1d4-4573-ac30-9dc91aa2a172",
  "isSidechain": true,
  "agentId": "a1b64ac8a57b00a7e",
  "requestId": "req_011CbEpVpAD78wtoMigK6pYJ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "df821a77-f249-4533-827d-7dd83bc2bc1c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/paper_agent_20baa82f",
  "sessionId": "35fb04f7-d2db-441f-a3b1-35490ca0d54b",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "eventual-sniffing-crane",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017rF6omLVaGRTAAP3Wggu86",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 28018,
      "cache_read_input_tokens": 0,
      "output_tokens": 537,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 28018
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 537,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 28018,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 28018,
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

_source line 14 · 2026-05-21T01:08:12.922Z_

<details><summary>↩ Tool result · `toolu_0165q2CP26GEvG7BtvHyQQ7y`</summary>

```text
1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We presented the first systematic characterization of how multi-class annotation errors interact with causal DAG topology. Our bias taxonomy across seven topologies reveals that the classical binary guarantee of bias toward the null breaks for $K \geq 3$: exposure and IV topologies can produce sign reversal (83.4\% and 52.6\% respectively), while five topologies maintain a structural guarantee of no sign flip. The ASV framework provides topology-aware sensitivity diagnostics, revealing a vulnerability spectrum from IV (maximally fragile) to M-bias (immune). Our correction guidance analysis reveals that correction method effectiveness is itself topology-dependent: a Frisch--Waugh--Lovell invariance result proves matrix-based corrections are ineffective for four topologies, while PPI++ achieves 93.8\% bias reduction at the cost of gold-standard labels. Binarization collapse analysis further demonstrates that simplifying multi-class annotations to binary introduces additional bias varying 147$\times$ across topologies.
5	
6	\paragraph{Limitations.}
7	Our framework assumes non-differential misclassification: $P(A^*|A, Y, \mathbf{Z}) = P(A^*|A)$. This assumption is reasonable when the LLM annotator has no access to the outcome variable $Y$ (e.g., classifying text sentiment without observing a downstream behavioral outcome) and when prompt variation is independent of sample characteristics. However, it may be violated when few-shot examples are selected conditional on $Y$, when the model's chain-of-thought reasoning incorporates contextual features correlated with $Y$, or when annotation difficulty itself varies with the outcome. Under differential error, the bias expressions in Section~\ref{sec:method} no longer hold, and the ASV framework provides an upper bound on sensitivity rather than an exact characterization. Extending the framework to differential misclassification is a priority for future work.
8	
9	Our closed-form bias expressions are derived for $K{=}3$ and verified numerically at $K{=}5,7$; closed-form expressions for arbitrary $K$ remain open. For large $K$ (e.g., $K{\geq}10$ as in disaster response taxonomies), the $K{\times}K$ confusion matrix has $K(K{-}1)$ free parameters, making both estimation from validation data and interpretation of ASV results increasingly challenging. The computational cost of Monte Carlo validation scales as $O(K^2)$ per matrix sample but remains tractable through $K{=}7$.
10	
11	The framework assumes a single annotator characterized by one confusion matrix $C$. When multiple LLM annotators are used, their errors may be highly correlated~\cite{kim_garg2025}, and the effective confusion matrix of an ensemble is not simply the product of individual matrices. Extending the bias taxonomy and ASV framework to correlated multi-annotator settings is an open problem.
12	
13	Formal sharpness proofs for the monotonicity theorem cover three topologies; the remaining four are validated numerically. The empirical validation uses real LLM confusion matrices from HumAID ($K{=}10$, three frontier models), confirming the theoretical bias ranking and ASV vulnerability spectrum; validation at $K{=}3$ and $K{=}2$ is ongoing.
14	
15	\paragraph{Future work.}
16	Four directions are immediate. First, extending the framework to differential misclassification, which arises when LLM annotation quality varies with context. Second, incorporating the correlated error structure documented by \citet{kim_garg2025} into multi-LLM correction strategies. Third, extending the correction guidance framework to differential misclassification settings where PPI++ and DSL may interact differently with topology. Fourth, developing a practitioner toolkit that computes ASVs from estimated confusion matrices, routes to the appropriate correction method based on the researcher's causal design, and provides confidence intervals via PPI++ when gold-standard labels are available.
17	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "df821a77-f249-4533-827d-7dd83bc2bc1c",
  "isSidechain": true,
  "promptId": "ae2d0870-295e-4835-a3f0-f41f20bd6a21",
  "agentId": "a1b64ac8a57b00a7e",
  "type": "user",
  "uuid": "309fc8c3-2db9-472a-ae9a-93dc46b784aa",
  "sourceToolAssistantUUID": "df821a77-f249-4533-827d-7dd83bc2bc1c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/paper_agent_20baa82f",
  "sessionId": "35fb04f7-d2db-441f-a3b1-35490ca0d54b",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "eventual-sniffing-crane"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-21T01:08:12.975Z_

<details open><summary>🔧 Tool call — Read · `toolu_015dW5bKPkAGaJ2axVe5J2vd`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "309fc8c3-2db9-472a-ae9a-93dc46b784aa",
  "isSidechain": true,
  "agentId": "a1b64ac8a57b00a7e",
  "requestId": "req_011CbEpVpAD78wtoMigK6pYJ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d691594f-3561-40c6-840c-f96be110356e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/paper_agent_20baa82f",
  "sessionId": "35fb04f7-d2db-441f-a3b1-35490ca0d54b",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "eventual-sniffing-crane",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017rF6omLVaGRTAAP3Wggu86",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 28018,
      "cache_read_input_tokens": 0,
      "output_tokens": 537,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 28018
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 537,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 28018,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 28018,
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

_source line 16 · 2026-05-21T01:08:13.267Z_

<details><summary>↩ Tool result · `toolu_015dW5bKPkAGaJ2axVe5J2vd`</summary>

```text
1	\section{Proof of Proposition~\ref{prop:signflip}}
2	\label{app:proof}
3	
4	We provide algebraic proofs of sign preservation for the confounding, collider, mediation, and front-door topologies, and an explicit counterexample for the exposure topology.
5	Throughout, $A\in\{0,1,\dots,K{-}1\}$ with prior $p_k=P(A{=}k)$, and $C$ is a $K{\times}K$ column-stochastic confusion matrix with $C_{jk}=P(A^*{=}j\mid A{=}k)$.
6	We use category~0 as the reference and let $D_j=\mathbf{1}(A{=}j)$, $D_j^*=\mathbf{1}(A^*{=}j)$ for $j=1,\dots,K{-}1$.
7	
8	\subsection{Notation and Key Identities}
9	\label{app:notation}
10	
11	Under non-differential misclassification, the misclassified moments factor linearly through $C$.
12	Define the population vectors:
13	\begin{align}
14	  q_j &= P(A^*{=}j) = \textstyle\sum_k C_{jk}\,p_k, \label{eq:q}\\
15	  \mathrm{ct}_j &= \mathbb{E}[T\cdot D_j^*] = \textstyle\sum_k C_{jk}\,\mathbb{E}[T\cdot D_k], \label{eq:ct}\\
16	  \mathrm{cy}_j &= \mathbb{E}[Y\cdot D_j^*] = \textstyle\sum_k C_{jk}\,\mathbb{E}[Y\cdot D_k]. \label{eq:cy}
17	\end{align}
18	Write $q = Cp$, $\mathrm{ct} = C\,\mathbb{E}[T\cdot D]$, and $\mathrm{cy} = C\,\mathbb{E}[Y\cdot D]$, where $D=(D_0,\dots,D_{K-1})^\top$.
19	
20	\subsection{Frisch--Waugh--Lovell Decomposition}
21	\label{app:fwl}
22	
23	For topologies where $T$ is directly observed (confounding, mediation, collider, M-bias, front-door), the estimator regresses $Y$ on $Z^*=(1,T,D_1^*,\dots,D_{K-1}^*)$.
24	By the Frisch--Waugh--Lovell (FWL) theorem, the coefficient on $T$ satisfies:
25	\begin{equation}
26	  \operatorname{plim}\hat{\tau}(C)
27	  = \frac{\mathbb{E}[\tilde{T}\,\tilde{Y}]}{\mathbb{E}[\tilde{T}^2]},
28	  \label{eq:fwl}
29	\end{equation}
30	where $\tilde{T}=T-\mathbb{E}[T\mid A^*]$ and $\tilde{Y}=Y-\mathbb{E}[Y\mid A^*]$ are residuals from projecting onto $(1,D_1^*,\dots,D_{K-1}^*)$.
31	
32	\begin{lemma}[Bias decomposition]
33	\label{lem:bias_decomp}
34	Suppose $Y = \tau T + f(A) + \varepsilon_Y$ with $\varepsilon_Y \perp (T, A, A^*)$.
35	Then
36	\begin{equation}
37	  \operatorname{plim}\hat\tau(C) = \tau + \frac{R(C)}{D(C)},
38	  \label{eq:bias_decomp}
39	\end{equation}
40	where
41	\begin{align}
42	  R(C) &= \mathbb{E}\bigl[\operatorname{Cov}(T,\,f(A)\mid A^*)\bigr], \label{eq:R}\\
43	  D(C) &= \mathbb{E}\bigl[\operatorname{Var}(T\mid A^*)\bigr] > 0. \label{eq:D}
44	\end{align}
45	\end{lemma}
46	
47	\begin{proof}
48	Expand $\tilde{Y}$ using $Y=\tau T + f(A) + \varepsilon_Y$:
49	\[
50	  \tilde{Y} = \tau\,\tilde{T} + \bigl(f(A) - \mathbb{E}[f(A)\mid A^*]\bigr) + \varepsilon_Y.
51	\]
52	Since $\tilde{T}$ is measurable w.r.t.\ $(T,A^*)$ and $\varepsilon_Y\perp(T,A,A^*)$:
53	\[
54	  \mathbb{E}[\tilde{T}\,\tilde{Y}]
55	  = \tau\,\mathbb{E}[\tilde{T}^2]
56	  + \mathbb{E}\bigl[\tilde{T}\,\bigl(f(A)-\mathbb{E}[f(A)\mid A^*]\bigr)\bigr].
57	\]
58	The numerator residual is $R(C) = \mathbb{E}[\tilde{T}(f(A)-\mathbb{E}[f(A)\mid A^*])]$, and the denominator is $D(C) = \mathbb{E}[\tilde{T}^2]$.
59	
60	By the law of total covariance:
61	\[
62	  R(C) = \sum_{j=0}^{K-1} q_j\,\operatorname{Cov}(T,\,f(A)\mid A^*{=}j)
63	  = \mathbb{E}[\operatorname{Cov}(T,f(A)\mid A^*)].
64	\]
65	For $D(C)>0$: decompose $T = g(A) + \varepsilon_T$ where $g(A)=\mathbb{E}[T\mid A]$ (for confounding) or simply note that $T$ has exogenous variation independent of $A^*$ (for mediation).
66	In both cases, $\tilde{T}=\bigl(g(A)-\mathbb{E}[g(A)\mid A^*]\bigr)+\varepsilon_T'$, where $\varepsilon_T'$ is the component of $T$ independent of $(A,A^*)$.
67	Hence $D(C)\geq\operatorname{Var}(\varepsilon_T')>0$.
68	\end{proof}
69	
70	\subsection{Confounding Topology ($A$ = Confounder)}
71	\label{app:confounding}
72	
73	\paragraph{Data-generating process.}
74	$A\to T$, $A\to Y$, $T\to Y$.
75	Using dummy coding with category 0 as reference:
76	\begin{align*}
77	  T &= \sum_{j=1}^{K-1}\alpha_j D_j + \varepsilon_T,\quad
78	  \varepsilon_T\sim\mathcal{N}(0,\sigma_T^2),\;\varepsilon_T\perp A,\\
79	  Y &= \tau\, T + \sum_{j=1}^{K-1}\beta_j^{(A)} D_j + \varepsilon_Y,\quad
80	  \varepsilon_Y\sim\mathcal{N}(0,1),\;\varepsilon_Y\perp(T,A).
81	\end{align*}
82	Define $g(k)=\sum_{j}\alpha_j\mathbf{1}(k{=}j)$ and $f(k)=\sum_{j}\beta_j^{(A)}\mathbf{1}(k{=}j)$, so $g(0)=f(0)=0$.
83	
84	\paragraph{Closed-form plim.}
85	Using the FWL decomposition, the coefficient on $T$ is:
86	\begin{equation}
87	  \operatorname{plim}\hat\tau(C)
88	  = \frac{\mu_{TY} - \sum_{j=0}^{K-1}\frac{\mathrm{ct}_j\,\mathrm{cy}_j}{q_j}}
89	  {s_T - \sum_{j=0}^{K-1}\frac{\mathrm{ct}_j^2}{q_j}},
90	  \label{eq:plim_conf}
91	\end{equation}
92	where $s_T=\mathbb{E}[T^2]$, $\mu_{TY}=\mathbb{E}[TY]$, and $\mathrm{ct}_j$, $\mathrm{cy}_j$, $q_j$ are defined in~\eqref{eq:q}--\eqref{eq:cy}.
93	
94	\begin{proof}[Derivation]
95	By FWL, $\operatorname{plim}\hat\tau = \mathbb{E}[\tilde{T}Y]/\mathbb{E}[\tilde{T}^2]$ where $\tilde{T}=T-\mathbb{E}[T\mid A^*]$.
96	Since $\mathbb{E}[T\mid A^*{=}j]=\mathrm{ct}_j/q_j$:
97	\begin{align*}
98	  \mathbb{E}[\tilde{T}^2]
99	  &= \mathbb{E}[T^2] - \sum_j q_j\bigl(\mathrm{ct}_j/q_j\bigr)^2
100	  = s_T - \sum_j \mathrm{ct}_j^2/q_j,\\
101	  \mathbb{E}[\tilde{T}\,Y]
102	  &= \mathbb{E}[TY] - \sum_j \bigl(\mathrm{ct}_j/q_j\bigr)\,\mathbb{E}[Y\cdot D_j^*]
103	  = \mu_{TY} - \sum_j \mathrm{ct}_j\,\mathrm{cy}_j/q_j.
104	\end{align*}
105	\end{proof}
106	
107	\paragraph{Verification at $C=I$.}
108	When $C=I$: $q_j=p_j$, $\mathrm{ct}_j=\mathbb{E}[T D_j]=\alpha_j p_j$, $\mathrm{cy}_j=\mathbb{E}[Y D_j]=p_j(\tau\alpha_j+\beta_j^{(A)})$.
109	Direct substitution yields numerator $= \tau\sigma_T^2$ and denominator $= \sigma_T^2$, giving $\operatorname{plim}\hat\tau = \tau$.
110	
111	\paragraph{Bias structure.}
112	By Lemma~\ref{lem:bias_decomp}:
113	\begin{equation}
114	  \operatorname{plim}\hat\tau(C) = \tau + B(C),\quad
115	  B(C) = \frac{\mathbb{E}[\operatorname{Cov}(g(A),\,f(A)\mid A^*)]}{D(C)}.
116	  \label{eq:bias_conf}
117	\end{equation}
118	By the law of total covariance:
119	\begin{equation}
120	  \mathbb{E}[\operatorname{Cov}(g,f\mid A^*)]
121	  = \operatorname{Cov}(g(A),f(A))
122	  - \operatorname{Cov}\bigl(\mathbb{E}[g(A)\mid A^*],\;\mathbb{E}[f(A)\mid A^*]\bigr).
123	  \label{eq:lotc}
124	\end{equation}
125	
126	At $C=I$: $\mathbb{E}[g\mid A^*]=g(A)$, so the between-group covariance equals $\operatorname{Cov}(g,f)$ and $B(I)=0$.
127	
128	At $C=\frac{1}{K}\mathbf{1}\mathbf{1}^\top$ (uniform, $A^*\perp A$): $\mathbb{E}[g\mid A^*]$ is constant, so the between-group covariance is zero and
129	\begin{equation}
130	  B_{\mathrm{OV}} \;\equiv\; B\bigl(\tfrac{1}{K}\mathbf{1}\mathbf{1}^\top\bigr)
131	  = \frac{\operatorname{Cov}(g(A),\,f(A))}{\operatorname{Var}(T)},
132	  \label{eq:bov}
133	\end{equation}
134	which equals the classical omitted-variable bias (no control for $A$).
135	
136	\paragraph{Sign preservation condition.}
137	Since $D(C)>0$, sign$(\operatorname{plim}\hat\tau) = $ sign$(\tau\cdot D(C) + R(C))$.
138	For sign preservation, it suffices that $R(C)$ does not overwhelm $\tau\cdot D(C)$.
139	
140	\begin{proposition}[Confounding sign preservation --- proportional case]
141	\label{prop:conf_prop}
142	If $f(A) = \lambda\,g(A)$ for some constant $\lambda$ (i.e., the confounder effects on $T$ and $Y$ are proportional), then
143	\begin{equation}
144	  B(C) = \bigl(1-\eta(C)\bigr)\,B_{\mathrm{OV}},
145	  \label{eq:convex}
146	\end{equation}
147	where
148	\[
149	  \eta(C) = \frac{\operatorname{Var}(\mathbb{E}[g(A)\mid A^*])\;\sigma_T^2}
150	  {\operatorname{Var}(g(A))\bigl(\operatorname{Var}(g(A))-\operatorname{Var}(\mathbb{E}[g(A)\mid A^*])+\sigma_T^2\bigr)}
151	  \;\in\;[0,1].
152	\]
153	Consequently, $B(C)$ lies between $0$ and $B_{\mathrm{OV}}$, and $\operatorname{sign}(\operatorname{plim}\hat\tau)=\operatorname{sign}(\tau)$ whenever $\operatorname{sign}(\tau)=\operatorname{sign}(\tau+B_{\mathrm{OV}})$.
154	\end{proposition}
155	
156	\begin{proof}
157	When $f=\lambda g$: the between-group covariance in~\eqref{eq:lotc} becomes $\lambda\,\operatorname{Var}(\mathbb{E}[g\mid A^*])$, and $\operatorname{Cov}(g,f)=\lambda\,\operatorname{Var}(g)$.
158	So $R(C)=\lambda\bigl(\operatorname{Var}(g)-\operatorname{Var}(\mathbb{E}[g\mid A^*])\bigr)=\lambda\,V_W$, where $V_W=\operatorname{Var}(g)-V_B$ with $V_B=\operatorname{Var}(\mathbb{E}[g\mid A^*])$.
159	Similarly, $D(C)=V_W+\sigma_T^2$.
160	Hence
161	\[
162	  B(C) = \frac{\lambda\,V_W}{V_W+\sigma_T^2},\qquad
163	  B_{\mathrm{OV}} = \frac{\lambda\,V}{V+\sigma_T^2},
164	\]
165	where $V=\operatorname{Var}(g)=V_B+V_W$.
166	The ratio
167	\[
168	  \frac{B(C)}{B_{\mathrm{OV}}} = \frac{V_W(V+\sigma_T^2)}{V(V_W+\sigma_T^2)} = 1 - \eta(C)
169	\]
170	is a decreasing function of $V_B\in[0,V]$.
171	At $V_B=0$ (no classification, $C$ uniform): $\eta=0$, $B=B_{\mathrm{OV}}$.
172	At $V_B=V$ (perfect classification, $C=I$): $\eta=1$, $B=0$.
173	Since $0\leq V_B\leq V$, we have $\eta\in[0,1]$ and $B(C)\in[0,B_{\mathrm{OV}}]$ (with the sign of $B_{\mathrm{OV}}$).
174	\end{proof}
175	
176	\begin{proposition}[Confounding sign preservation --- general case]
177	\label{prop:conf_gen}
178	For general $g$ and $f$ (not necessarily proportional), define the worst-case bias bound
179	\begin{equation}
180	  \bar{B} \;=\; \frac{\sqrt{\operatorname{Var}(g(A))\,\operatorname{Var}(f(A))}}{\sigma_T^2}.
181	  \label{eq:bbar}
182	\end{equation}
183	If $|\tau| > \bar{B}$, then $\operatorname{sign}(\operatorname{plim}\hat\tau(C))=\operatorname{sign}(\tau)$ for \emph{all} column-stochastic $C$.
184	\end{proposition}
185	
186	\begin{proof}
187	We need $\operatorname{sign}(\tau\cdot D(C)+R(C))=\operatorname{sign}(\tau)$, which holds if $|R(C)|<|\tau|\cdot D(C)$.
188	Since $D(C)\geq\sigma_T^2$ (shown in Lemma~\ref{lem:bias_decomp}), it suffices to show $|R(C)|<|\tau|\,\sigma_T^2$.
189	
190	\emph{Step 1: Bound $|R(C)|$.}
191	$R(C)=\mathbb{E}[\operatorname{Cov}(g(A),f(A)\mid A^*)]$.
192	By the Cauchy--Schwarz inequality applied to each within-group covariance:
193	\[
194	  |\operatorname{Cov}(g,f\mid A^*{=}j)|
195	  \leq \sqrt{\operatorname{Var}(g\mid A^*{=}j)\,\operatorname{Var}(f\mid A^*{=}j)}.
196	\]
197	Taking expectations and applying Cauchy--Schwarz again:
198	\begin{align*}
199	  |R(C)|
200	  &\leq \mathbb{E}\bigl[\sqrt{\operatorname{Var}(g\mid A^*)\,\operatorname{Var}(f\mid A^*)}\bigr]\\
201	  &\leq \sqrt{\mathbb{E}[\operatorname{Var}(g\mid A^*)]\;\mathbb{E}[\operatorname{Var}(f\mid A^*)]}\\
202	  &\leq \sqrt{\operatorname{Var}(g(A))\;\operatorname{Var}(f(A))},
203	\end{align*}
204	where the last step uses $\mathbb{E}[\operatorname{Var}(X\mid Y)]\leq\operatorname{Var}(X)$ (law of total variance).
205	
206	\emph{Step 2: Conclude.}
207	The bias satisfies
208	\[
209	  |B(C)| = \frac{|R(C)|}{D(C)} \leq \frac{\sqrt{\operatorname{Var}(g)\,\operatorname{Var}(f)}}{\sigma_T^2} = \bar{B}.
210	\]
211	When $|\tau|>\bar{B}$, the bias cannot cancel $\tau$, so $\operatorname{sign}(\operatorname{plim}\hat\tau)=\operatorname{sign}(\tau)$ for all $C$.
212	\end{proof}
213	
214	\paragraph{Relationship to the omitted-variable condition.}
215	A weaker (necessary) condition for sign preservation is $\operatorname{sign}(\tau)=\operatorname{sign}(\tau_{\mathrm{OV}})$ where $\tau_{\mathrm{OV}}=\tau+\operatorname{Cov}(g,f)/\operatorname{Var}(T)$.
216	If this fails, then $C=\frac{1}{K}\mathbf{1}\mathbf{1}^\top$ (uniform noise) already flips the sign.
217	The rigorous sufficient condition $|\tau|>\bar{B}$ implies the weaker condition, since $|B_{\mathrm{OV}}|=|\operatorname{Cov}(g,f)|/\operatorname{Var}(T)\leq\bar{B}$ by Cauchy--Schwarz and $\operatorname{Var}(T)\geq\sigma_T^2$.
218	
219	\paragraph{Verification for paper parameters ($K{=}3$).}
220	With $\tau{=}2.0$, $\boldsymbol{\alpha}{=}(1.5,{-}1.0)$, $\boldsymbol{\beta}^{(A)}{=}(1.0,{-}0.5)$, $\sigma_T{=}1.0$, $\mathbf{p}{=}(0.40,0.35,0.25)$:
221	\begin{align*}
222	  \operatorname{Var}(g) &= \sum_k p_k\alpha_k^2 - \bigl(\textstyle\sum_k p_k\alpha_k\bigr)^2 = 0.962,\\
223	  \operatorname{Var}(f) &= \sum_k p_k(\beta_k^{(A)})^2 - \bigl(\textstyle\sum_k p_k\beta_k^{(A)}\bigr)^2 = 0.362,\\
224	  \bar{B} &= \sqrt{0.962\times 0.362}\;/\;1.0^2 = 0.590.
225	\end{align*}
226	Since $|\tau|{=}2.0 > \bar{B}{=}0.590$, sign preservation is guaranteed for \emph{all} column-stochastic $C$ by Proposition~\ref{prop:conf_gen}.
227	Additionally, $B_{\mathrm{OV}}=\operatorname{Cov}(g,f)/\operatorname{Var}(T)=0.588/1.962={+}0.300$, giving $\tau_{\mathrm{OV}}{=}2.300>0$, confirming that both the necessary and sufficient conditions are satisfied.
228	
229	\subsection{Mediation Topology ($A$ = Mediator)}
230	\label{app:mediation}
231	
232	\paragraph{Data-generating process.}
233	$T\to A\to Y$, $T\to Y$.
234	\begin{align*}
235	  T &\sim \operatorname{Bernoulli}(0.5),\\
236	  A\mid T &\sim \operatorname{Categorical}\bigl(\operatorname{softmax}(\boldsymbol{\gamma}+\boldsymbol{\delta}\,T)\bigr),\\
237	  Y &= \tau_{\mathrm{dir}}\,T + f(A) + \varepsilon_Y.
238	\end{align*}
239	
240	\paragraph{Bias decomposition.}
241	By Lemma~\ref{lem:bias_decomp}, the direct-effect estimator satisfies:
242	\begin{equation}
243	  \operatorname{plim}\hat\tau_{\mathrm{dir}}(C) = \tau_{\mathrm{dir}} + \frac{\mathbb{E}[\operatorname{Cov}(T,\,f(A)\mid A^*)]}{D(C)}.
244	  \label{eq:med_bias}
245	\end{equation}
246	
247	The key structural difference from confounding: $T$ \emph{causes} $A$, so the residual covariance $\operatorname{Cov}(T,f(A)\mid A^*)$ captures the indirect effect of $T$ on $Y$ through $A$ that is not absorbed by conditioning on $A^*$.
248	
249	\paragraph{Endpoint analysis.}
250	
251	At $C=I$ ($A^*{=}A$): conditioning on $A$ blocks the mediated path $T\to A\to Y$, so $\operatorname{Cov}(T,f(A)\mid A)=0$ and $\operatorname{plim}\hat\tau=\tau_{\mathrm{dir}}$.
252	
253	At $C=\frac{1}{K}\mathbf{1}\mathbf{1}^\top$ ($A^*\perp A$): no information about $A$ is used, and
254	\begin{align*}
255	  \mathbb{E}[\operatorname{Cov}(T,f(A)\mid A^*)] &= \operatorname{Cov}(T,f(A)),\\
256	  D(C) &= \operatorname{Var}(T) = 0.25.
257	\end{align*}
258	The indirect effect is $\tau_{\mathrm{ind}}=\mathbb{E}[f(A)\mid T{=}1]-\mathbb{E}[f(A)\mid T{=}0]$, and
259	\[
260	  \operatorname{Cov}(T,f(A)) = 0.25\,\tau_{\mathrm{ind}}.
261	\]
262	Hence at $C$ uniform: $\operatorname{plim}\hat\tau = \tau_{\mathrm{dir}}+\tau_{\mathrm{ind}} = \tau_{\mathrm{total}}$.
263	
264	\paragraph{Empirical Finding (Mediation sign preservation).}
265	\label{find:med_sign}
266	$\operatorname{sign}(\operatorname{plim}\hat\tau_{\mathrm{dir}})=\operatorname{sign}(\tau_{\mathrm{dir}})$ whenever $\operatorname{sign}(\tau_{\mathrm{dir}})=\operatorname{sign}(\tau_{\mathrm{total}})$, where $\tau_{\mathrm{total}}=\tau_{\mathrm{dir}}+\tau_{\mathrm{ind}}$.
267	This result is verified numerically for $100{,}000$ independently sampled column-stochastic matrices $C$; a closed-form proof for general $K$ remains open.
268	
269	\begin{proof}
270	Let $R(C)=\mathbb{E}[\operatorname{Cov}(T,f(A)\mid A^*)]$ and $D(C)=\mathbb{E}[\operatorname{Var}(T\mid A^*)]>0$.
271	
272	\emph{Endpoints.}
273	At $C{=}I$: $f(A)$ is constant given $A{=}A^*$, so $R(I)=0$ and $B(I)=0$.
274	At $C=\frac{1}{K}\mathbf{1}\mathbf{1}^\top$: $R=\operatorname{Cov}(T,f(A))=0.25\,\tau_{\mathrm{ind}}$ and $D=\operatorname{Var}(T)=0.25$, giving $B=\tau_{\mathrm{ind}}$.
275	
276	\emph{Within-group structure for binary $T$.}
277	Since $T\in\{0,1\}$, the within-$A^*$-group bias admits a revealing decomposition.
278	Let $p_j=P(T{=}1\mid A^*{=}j)$.
279	Then $\operatorname{Var}(T\mid A^*{=}j)=p_j(1{-}p_j)$ and
280	\[
281	  \operatorname{Cov}(T,f(A)\mid A^*{=}j)
282	  = p_j(1{-}p_j)\bigl[\mathbb{E}[f(A)\mid T{=}1,A^*{=}j]-\mathbb{E}[f(A)\mid T{=}0,A^*{=}j]\bigr].
283	\]
284	Define $\delta_j=\mathbb{E}[f(A)\mid T{=}1,A^*{=}j]-\mathbb{E}[f(A)\mid T{=}0,A^*{=}j]$ as the \emph{conditional indirect effect} in the $A^*{=}j$ subpopulation.
285	Then
286	\[
287	  B(C)=\frac{R(C)}{D(C)}
288	  =\frac{\sum_j q_j\,p_j(1{-}p_j)\,\delta_j}{\sum_j q_j\,p_j(1{-}p_j)}
289	  =\sum_j w_j\,\delta_j,
290	\]
291	a weighted average of the conditional indirect effects, with weights $w_j=q_j p_j(1{-}p_j)/\sum_\ell q_\ell p_\ell(1{-}p_\ell)\geq 0$ summing to 1.
292	
293	At $C{=}I$: each $A^*{=}j$ group has $A{=}j$ a.s., so $\delta_j=f(j)-f(j)=0$ and $B=0$.
294	At $C$ uniform: $\delta_j=\tau_{\mathrm{ind}}$ for all $j$ and $B=\tau_{\mathrm{ind}}$.
295	
296	\emph{Sign preservation.}
297	When $\operatorname{Cov}(g(A),f(A))>0$ (the indirect effect reinforces the direct effect, i.e., $\tau_{\mathrm{dir}}$ and $\tau_{\mathrm{ind}}$ have the same sign), the bias $B(C)\geq 0$ cannot oppose $\tau_{\mathrm{dir}}$, so sign is preserved trivially.
298	
299	When $\tau_{\mathrm{dir}}$ and $\tau_{\mathrm{ind}}$ have opposite signs but $|\tau_{\mathrm{ind}}|<|\tau_{\mathrm{dir}}|$ (i.e., $\operatorname{sign}(\tau_{\mathrm{dir}})=\operatorname{sign}(\tau_{\mathrm{total}})$), sign reversal requires some $|\delta_j|>|\tau_{\mathrm{dir}}|$ with the opposing sign.
300	Since each $\delta_j$ is a difference of weighted averages of $f$ values (with weights $P(A{=}k\mid T{=}t,A^*{=}j)$), and $B(C)$ is a convex combination of $\delta_j$, the bound $|B(C)|\leq\max_j|\delta_j|$ holds.
301	We verify numerically that $\max_j|\delta_j|\leq|\tau_{\mathrm{ind}}|$ for all 100{,}000 random $C$ matrices in our experiments, confirming sign preservation.
302	\end{proof}
303	
304	\paragraph{Verification for paper parameters ($K{=}3$).}
305	With $\tau_{\mathrm{dir}}{=}0.5$, $\boldsymbol{\gamma}{=}(0,0,0)$, $\boldsymbol{\delta}{=}(0,0.8,{-}0.6)$, $\boldsymbol{\beta}{=}(0,1.0,{-}0.5)$:
306	
307	$\tau_{\mathrm{ind}}=\mathbb{E}[f(A)\mid T{=}1]-\mathbb{E}[f(A)\mid T{=}0]=0.351$ (computed from the softmax class probabilities).
308	$\tau_{\mathrm{total}}=0.5+0.351=0.851>0$.
309	Since $\tau_{\mathrm{dir}}{>}0$ and $\tau_{\mathrm{total}}{>}0$, sign preservation holds for all $C$.
310	
311	\subsection{Collider Topology ($A$ = Collider)}
312	\label{app:collider}
313	
314	\paragraph{Data-generating process.}
315	$T\to A\leftarrow Y$, $T\to Y$.
316	The treatment effect is unconfounded:
317	\begin{align*}
318	  T &\sim \mathcal{N}(0,1),\quad
319	  Y = \tau\,T + \varepsilon_Y,\quad \varepsilon_Y\sim\mathcal{N}(0,1),\;\varepsilon_Y\perp T,\\
320	  A\mid T,Y &\sim \operatorname{Categorical}\bigl(\operatorname{softmax}(\boldsymbol{\delta}_T\,T + \boldsymbol{\delta}_Y\,Y)\bigr).
321	\end{align*}
322	The collider $A$ is a common \emph{effect} of $T$ and $Y$.
323	The no-control estimator (regressing $Y$ on $T$ alone) is consistent: $\operatorname{plim}\hat\tau_{\mathrm{nc}}=\tau$.
324	The researcher erroneously controls for $A^*$, inducing Berkson's bias.
325	
326	\paragraph{Bias decomposition.}
327	Unlike confounding, $\varepsilon_Y$ is not independent of $A$ (since $A$ depends on $Y=\tau T+\varepsilon_Y$), so Lemma~\ref{lem:bias_decomp} does not apply directly.
328	Instead, we derive the bias from the FWL identity~\eqref{eq:fwl}.
329	Writing $\tilde{Y}=\tau\tilde{T}+(\varepsilon_Y-\mathbb{E}[\varepsilon_Y\mid A^*])$ and noting that $\mathbb{E}[\tilde{T}\,\varepsilon_Y]=\mathbb{E}[\operatorname{Cov}(T,\varepsilon_Y\mid A^*)]$ (since $T\perp\varepsilon_Y$ unconditionally):
330	\begin{equation}
331	  \operatorname{plim}\hat\tau(C) = \tau + B(C),\quad
332	  B(C) = \frac{\mathbb{E}[\operatorname{Cov}(T,\,\varepsilon_Y\mid A^*)]}{\mathbb{E}[\operatorname{Var}(T\mid A^*)]}.
333	  \label{eq:bias_col}
334	\end{equation}
335	Under non-differential misclassification ($A^*\perp(T,\varepsilon_Y)\mid A$), define $g(k)=\mathbb{E}[T\mid A{=}k]$ and $h(k)=\mathbb{E}[\varepsilon_Y\mid A{=}k]$.
336	By the tower property, $\mathbb{E}[T\mid A^*]=\mathbb{E}[g(A)\mid A^*]$ and $\mathbb{E}[\varepsilon_Y\mid A^*]=\mathbb{E}[h(A)\mid A^*]$.
337	Since $\operatorname{Cov}(T,\varepsilon_Y)=0$, the law of total covariance gives:
338	\[
339	  B(C) = \frac{-\operatorname{Cov}\bigl(\mathbb{E}[g(A)\mid A^*],\;\mathbb{E}[h(A)\mid A^*]\bigr)}{\mathbb{E}[\operatorname{Var}(T\mid A^*)]}.
340	\]
341	
342	\paragraph{Endpoint analysis.}
343	At $C=I$ ($A^*{=}A$):
344	$B(I) = -\operatorname{Cov}(g(A),h(A))\,/\,\mathbb{E}[\operatorname{Var}(T\mid A)] = B_{\mathrm{Berkson}}$,
345	the full Berkson's bias from conditioning on the collider.
346	
347	At $C=\frac{1}{K}\mathbf{1}\mathbf{1}^\top$ ($A^*\perp A$):
348	$\mathbb{E}[g(A)\mid A^*]$ and $\mathbb{E}[h(A)\mid A^*]$ are constant, so $B=0$ and $\operatorname{plim}\hat\tau=\tau$.
349	
350	This is the structural reverse of confounding: misclassification attenuates the collider-induced bias toward zero, rather than growing bias from zero toward $B_{\mathrm{OV}}$.
351	
352	\begin{proposition}[Collider sign preservation --- proportional case]
353	\label{prop:col_prop}
354	If $h(A)=\lambda\,g(A)$ for some constant $\lambda$, then $|B(C)|\leq|B(I)|$ for all column-stochastic $C$, and $B(C)$ has the same sign as $B(I)$.
355	Consequently, $\operatorname{sign}(\operatorname{plim}\hat\tau)=\operatorname{sign}(\tau)$ whenever $\operatorname{sign}(\tau)=\operatorname{sign}(\tau+B_{\mathrm{Berkson}})$.
356	\end{proposition}
357	
358	\begin{proof}
359	When $h=\lambda g$, the numerator becomes $-\lambda\,\operatorname{Var}(\mathbb{E}[g(A)\mid A^*])$ and the denominator is $\operatorname{Var}(T)-\operatorname{Var}(\mathbb{E}[g(A)\mid A^*])$.
360	Let $V^*=\operatorname{Var}(\mathbb{E}[g(A)\mid A^*])\in[0,V_g]$ where $V_g=\operatorname{Var}(g(A))$.
361	Then
362	\[
363	  |B(C)| = |\lambda|\,\frac{V^*}{\operatorname{Var}(T)-V^*}.
364	\]
365	The function $x\mapsto x/(a-x)$ is increasing on $[0,a)$.
366	With $a=\operatorname{Var}(T)>V_g\geq V^*$:
367	$|B(C)|\leq|\lambda|\,V_g/(\operatorname{Var}(T)-V_g)=|B(I)|$.
368	At $V^*{=}0$ (uniform $C$): $B{=}0$.  At $V^*{=}V_g$ ($C{=}I$): $B{=}B(I)$.
369	\end{proof}
370	
371	\begin{proposition}[Collider sign preservation --- general case]
372	\label{prop:col_gen}
373	Define
374	\begin{equation}
375	  \bar{B}_{\mathrm{col}} = \frac{\sqrt{\operatorname{Var}(g(A))\,\operatorname{Var}(h(A))}}{\mathbb{E}[\operatorname{Var}(T\mid A)]}.
376	  \label{eq:bbar_col}
377	\end{equation}
378	If $|\tau|>\bar{B}_{\mathrm{col}}$, then $\operatorname{sign}(\operatorname{plim}\hat\tau(C))=\operatorname{sign}(\tau)$ for all column-stochastic $C$.
379	\end{proposition}
380	
381	\begin{proof}
382	\emph{Step~1: Bound the numerator.}
383	By Cauchy--Schwarz:
384	$|\operatorname{Cov}(\mathbb{E}[g\mid A^*],\mathbb{E}[h\mid A^*])|\leq\sqrt{\operatorname{Var}(\mathbb{E}[g\mid A^*])\,\operatorname{Var}(\mathbb{E}[h\mid A^*])}$.
385	Since conditional expectation reduces variance: $\operatorname{Var}(\mathbb{E}[g\mid A^*])\leq\operatorname{Var}(g(A))$ and likewise for $h$.
386	
387	\emph{Step~2: Bound the denominator.}
388	$\mathbb{E}[\operatorname{Var}(T\mid A^*)]=\operatorname{Var}(T)-\operatorname{Var}(\mathbb{E}[T\mid A^*])\geq\operatorname{Var}(T)-\operatorname{Var}(g(A))=\mathbb{E}[\operatorname{Var}(T\mid A)]$.
389	
390	\emph{Step~3: Conclude.}
391	$|B(C)|\leq\sqrt{\operatorname{Var}(g)\,\operatorname{Var}(h)}\,/\,\mathbb{E}[\operatorname{Var}(T\mid A)]=\bar{B}_{\mathrm{col}}$.
392	When $|\tau|>\bar{B}_{\mathrm{col}}$, the bias cannot overwhelm $\tau$.
393	\end{proof}
394	
395	\paragraph{Verification for paper parameters ($K{=}3$).}
396	With $\tau{=}1.0$, $\boldsymbol{\delta}_T{=}(0,\,0.5,\,{-}0.3)$, $\boldsymbol{\delta}_Y{=}(0,\,0.8,\,0.6)$, from $5{\times}10^6$-sample Monte Carlo:
397	\begin{align*}
398	  \operatorname{Var}(g(A)) &= 0.187,\quad
399	  \operatorname{Var}(h(A)) = 0.076,\quad
400	  \mathbb{E}[\operatorname{Var}(T\mid A)] = 0.813,\\
401	  \bar{B}_{\mathrm{col}} &= \sqrt{0.187\times 0.076}\;/\;0.813 = 0.147.
402	\end{align*}
403	Since $|\tau|{=}1.0\gg\bar{B}_{\mathrm{col}}{=}0.147$, Proposition~\ref{prop:col_gen} guarantees sign preservation.
404	Additionally, $B_{\mathrm{Berkson}}{=}{-}0.114$, giving $\tau+B_{\mathrm{Berkson}}{=}0.886{>}0$.
405	Verified across $100{,}000$ random column-stochastic $C$: $\tau_{\mathrm{sign\,flip}}{=}0\%$, and $|B(C)|\leq|B_{\mathrm{Berkson}}|$ in all cases.
406	
407	\subsection{Front-door Topology ($A$ = Mediator under Confounding)}
408	\label{app:frontdoor}
409	
410	\paragraph{Data-generating process.}
411	$T\to A\to Y$, $U\to T$, $U\to Y$.
412	An unobserved confounder $U$ affects both treatment and outcome:
413	\begin{align*}
414	  U &\sim \mathcal{N}(0,1),\quad
415	  T = \alpha_U\,U + \eta,\quad \eta\sim\mathcal{N}(0,1),\;\eta\perp U,\\
416	  A\mid T &\sim \operatorname{Categorical}\bigl(\operatorname{softmax}(\boldsymbol{\gamma}+\boldsymbol{\delta}\,T)\bigr),\\
417	  Y &= f(A) + \lambda\,U + \varepsilon_Y,\quad \varepsilon_Y\perp(T,A,U).
418	\end{align*}
419	There is no direct $T{\to}Y$ edge; the causal effect of $T$ on $Y$ operates entirely through $A$.
420	The researcher controls for $A^*$ in $Y\sim 1+T+D_1^*+\cdots+D_{K-1}^*$.
421	
422	\paragraph{Bias decomposition.}
423	Since the direct effect is zero, the FWL coefficient on $T$ captures only bias:
424	\[
425	  \operatorname{plim}\hat\tau(C) = \frac{\mathbb{E}[\operatorname{Cov}(T,\,Y\mid A^*)]}{\mathbb{E}[\operatorname{Var}(T\mid A^*)]}.
426	\]
427	Substituting $Y=f(A)+\lambda U+\varepsilon_Y$ and using $\varepsilon_Y\perp(T,A,A^*)$:
428	\begin{equation}
429	  \operatorname{plim}\hat\tau(C)
430	  = \underbrace{\frac{\lambda\,\alpha_U}{\operatorname{Var}(T)}}_{\text{confounding (constant)}}
431	  \;+\; \underbrace{\frac{\mathbb{E}[\operatorname{Cov}(T,\,f(A)\mid A^*)]}{D(C)}}_{\displaystyle B_{\mathrm{med}}(C)},
432	  \label{eq:fd_decomp}
433	\end{equation}
434	where $D(C)=\mathbb{E}[\operatorname{Var}(T\mid A^*)]$.
435	
436	\begin{proof}[Derivation of~\eqref{eq:fd_decomp}]
437	Expand the numerator as
438	$\mathbb{E}[\operatorname{Cov}(T,f(A)\mid A^*)] + \lambda\,\mathbb{E}[\operatorname{Cov}(T,U\mid A^*)]$.
439	For the confounding term: since $T=\alpha_U U+\eta$ with $(U,\eta)$ jointly Gaussian, the regression residual $\xi=U-\frac{\alpha_U}{\operatorname{Var}(T)}T$ satisfies $\xi\perp T$.
440	Because $A$ is a function of $T$ (plus independent softmax noise) and $A^*$ is a function of $A$ (plus independent misclassification noise), $\xi\perp(T,A,A^*)$.
441	Therefore
442	\[
443	  \operatorname{Cov}(T,U\mid A^*{=}j)
444	  = \frac{\alpha_U}{\operatorname{Var}(T)}\,\operatorname{Var}(T\mid A^*{=}j)
445	  \quad\forall\;j,
446	\]
447	and $\lambda\,\mathbb{E}[\operatorname{Cov}(T,U\mid A^*)]=\frac{\lambda\alpha_U}{\operatorname{Var}(T)}\,D(C)$, yielding the constant first term after division by $D(C)$.
448	\end{proof}
449	
450	This decomposition reveals that \emph{misclassification does not affect the confounding component}.
451	The confusion matrix $C$ modulates only the mediation-type leakage $B_{\mathrm{med}}(C)$, which has the same structure as in~§\ref{app:mediation}.
452	
453	\paragraph{Endpoint analysis.}
454	At $C=I$: $B_{\mathrm{med}}(I)=0$ (controlling $A$ blocks the $T\to A\to Y$ path), and $\operatorname{plim}\hat\tau(I)=\lambda\alpha_U/\operatorname{Var}(T)$ (pure confounding residual).
455	
456	At $C=\frac{1}{K}\mathbf{1}\mathbf{1}^\top$: $B_{\mathrm{med}}=\operatorname{Cov}(T,f(A))/\operatorname{Var}(T)$, and $\operatorname{plim}\hat\tau_{\mathrm{nc}}=[\operatorname{Cov}(T,f(A))+\lambda\alpha_U]/\operatorname{Var}(T)$, the naive regression coefficient with no controls.
457	
458	\paragraph{Empirical Finding (Front-door sign preservation).}
459	\label{find:fd_sign}
460	Since $B_{\mathrm{med}}(C)$ has the same structure as the mediation bias (§\ref{app:mediation})---interpolating between $0$ at $C{=}I$ and $\operatorname{Cov}(T,f(A))/\operatorname{Var}(T)$ at $C$ uniform---sign preservation holds whenever the two endpoints have the same sign:
461	\[
462	  \operatorname{sign}\!\bigl(\lambda\alpha_U\bigr)
463	  = \operatorname{sign}\!\bigl(\lambda\alpha_U + \operatorname{Cov}(T,f(A))\bigr).
464	\]
465	This result is verified numerically for $100{,}000$ independently sampled column-stochastic matrices $C$.
466	
467	\paragraph{Verification for paper parameters ($K{=}3$).}
468	With $\alpha_U{=}1.0$, $\lambda{=}1.0$, $\boldsymbol{\beta}{=}(0,1.0,{-}0.5)$, $\boldsymbol{\gamma}{=}(0,0.5,{-}0.3)$, $\boldsymbol{\delta}{=}(0,1.0,{-}0.8)$:
469	\begin{align*}
470	  \lambda\alpha_U/\operatorname{Var}(T) &= 1.0\times 1.0\,/\,2.0 = 0.500,\\
471	  \operatorname{Cov}(T,f(A))/\operatorname{Var}(T) &= 0.594\,/\,2.0 = 0.297.
472	\end{align*}
473	Both components are positive, so $\operatorname{plim}\hat\tau(C)\in[0.500,\,0.797]>0$ for all $C$.
474	
475	\subsection{Exposure Topology: Sign Reversal Counterexample}
476	\label{app:exposure}
477	
478	\begin{proposition}[Exposure sign reversal]
479	\label{prop:exp_counter}
480	For $K{=}3$ with $A$ as the treatment variable, there exist a marginal distribution $\mathbf{p}$, treatment effects $\boldsymbol{\beta}$, and a column-stochastic $C$ with $C_{kk}>0.5$ for all $k$, such that $\operatorname{sign}(\operatorname{plim}\hat\beta_1)\neq\operatorname{sign}(\beta_1)$.
481	\end{proposition}
482	
483	\begin{proof}[Construction]
484	Consider the exposure DGP $Y = \beta_1 D_1 + \beta_2 D_2 + \varepsilon_Y$ with:
485	\begin{itemize}
486	  \item Uniform prior: $\mathbf{p}=(1/3,\,1/3,\,1/3)$.
487	  \item True effects: $\beta_1=1$,\; $\beta_2=-10$.
488	\end{itemize}
489	Choose the confusion matrix
490	\[
491	  C = \begin{pmatrix}
492	    0.60 & 0.10 & 0.10\\
493	    0.10 & 0.60 & 0.39\\
494	    0.30 & 0.30 & 0.51
495	  \end{pmatrix},\qquad
496	  C_{kk}\in\{0.60,\,0.60,\,0.51\},\;\text{all}>0.5.
497	\]
498	Column sums are $1$ (verifiable by inspection).
499	
500	The OLS estimator regresses $Y$ on $(1,D_1^*,D_2^*)$.
501	The plim of $\hat\beta_j$ equals $\mathbb{E}[Y\mid A^*{=}j]-\mathbb{E}[Y\mid A^*{=}0]$, where
502	\[
503	  \mathbb{E}[Y\mid A^*{=}j] = \sum_{k=0}^{2} P(A{=}k\mid A^*{=}j)\,\beta_k
504	  = \sum_{k=1}^{2}\frac{C_{jk}\,p_k}{q_j}\,\beta_k.
505	\]
506	
507	\emph{Marginal distribution of $A^*$:}
508	\begin{align*}
509	  q_0 &= \tfrac{1}{3}(0.60+0.10+0.10)=0.267,\\
510	  q_1 &= \tfrac{1}{3}(0.10+0.60+0.39)=0.363,\\
511	  q_2 &= \tfrac{1}{3}(0.30+0.30+0.51)=0.370.
512	\end{align*}
513	
514	\emph{Conditional means:}
515	\begin{align*}
516	  \mathbb{E}[Y\mid A^*{=}0]
517	  &= \frac{0.10\times\tfrac{1}{3}\times 1 + 0.10\times\tfrac{1}{3}\times({-}10)}{0.267}
518	  = \frac{0.0333-0.3333}{0.267} = -1.125,\\[4pt]
519	  \mathbb{E}[Y\mid A^*{=}1]
520	  &= \frac{0.60\times\tfrac{1}{3}\times 1 + 0.39\times\tfrac{1}{3}\times({-}10)}{0.363}
521	  = \frac{0.200-1.300}{0.363} = -3.028,\\[4pt]
522	  \mathbb{E}[Y\mid A^*{=}2]
523	  &= \frac{0.30\times\tfrac{1}{3}\times 1 + 0.51\times\tfrac{1}{3}\times({-}10)}{0.370}
524	  = \frac{0.100-1.700}{0.370} = -4.324.
525	\end{align*}
526	
527	\emph{Estimated coefficient:}
528	\[
529	  \operatorname{plim}\hat\beta_1 = \mathbb{E}[Y\mid A^*{=}1]-\mathbb{E}[Y\mid A^*{=}0]
530	  = -3.028-(-1.125) = \mathbf{-1.903}.
531	\]
532	The true $\beta_1=+1>0$ but $\operatorname{plim}\hat\beta_1=-1.903<0$: \textbf{sign reversal}.
533	
534	\emph{Mechanism.}
535	The large off-diagonal entry $C_{12}=0.39$ (probability of classifying true category~2 as $A^*{=}1$) routes substantial probability mass from category~2 ($\beta_2=-10$) into the $A^*{=}1$ bin.
536	Despite $C_{11}=0.60>0.5$, the contamination from the strongly negative $\beta_2$ overwhelms the positive $\beta_1$, reversing the sign of the estimated effect for category~1.
537	This failure mode is structurally impossible at $K{=}2$: a $2{\times}2$ column-stochastic matrix with $C_{kk}>0.5$ has the form $C=\bigl(\begin{smallmatrix}a&1{-}b\\1{-}a&b\end{smallmatrix}\bigr)$ with $a,b>0.5$, and the single coefficient $\hat\beta_1$ is a positive-weighted average of $\beta_1$, preserving sign.
538	For $K{\geq}3$, the additional degrees of freedom in $C$ permit cross-contamination between categories with opposite-sign effects.
539	\end{proof}
540	
541	\subsection{Summary of Conditions}
542	\label{app:conditions}
543	
544	\begin{table}[h]
545	\centering
546	\small
547	\begin{tabular}{lcc}
548	\toprule
549	\textbf{Topology} & \textbf{Sign preservation condition} & \textbf{Paper DGP} \\
550	\midrule
551	Confounding & $\operatorname{sign}(\tau)=\operatorname{sign}(\tau_{\mathrm{OV}})$ & $\checkmark$ ($2.0$ vs $2.3$)\\
552	Mediation & $\operatorname{sign}(\tau_{\mathrm{dir}})=\operatorname{sign}(\tau_{\mathrm{total}})$ & $\checkmark$ ($0.5$ vs $0.85$)\\
553	Collider & $|\tau|>\bar{B}_{\mathrm{col}}$ (Prop.~\ref{prop:col_gen}) & $\checkmark$ ($1.0$ vs $0.15$)\\
554	M-bias & Bias is attenuating (toward $\tau$) & $\checkmark$ \\
555	Front-door & $\operatorname{sign}(\tau)=\operatorname{sign}(\tau_{\mathrm{OV}})$ (§\ref{app:frontdoor}) & $\checkmark$ ($0.50$ vs $0.80$)\\
556	\midrule
557	Exposure & Not guaranteed for $K\geq 3$ & Counterexample above \\
558	IV & Not guaranteed (denominator instability) & --- \\
559	\bottomrule
560	\end{tabular}
561	\caption{Sufficient conditions for sign preservation under non-differential misclassification.
562	For confounding, mediation, and front-door, the condition requires the true (or clean-control) effect and the no-control effect to have the same sign.
563	For the collider, the condition bounds the Berkson's bias magnitude relative to $|\tau|$.
564	All conditions are verified for our DGP parameters.}
565	\label{tab:sign_conditions}
566	\end{table}
567	
568	\paragraph{Structural argument for M-bias topology.}
569	\emph{M-bias:} The M-structure creates a backdoor path through two latent common causes.
570	Misclassification of $A$ weakens the statistical association along this backdoor path, reducing the spurious correlation rather than amplifying it.
571	The bias therefore interpolates between zero (perfect classification) and the full backdoor bias (no classification information), preserving sign under the same sufficient condition as confounding.
572	
573	\paragraph{Remark.}
574	The sign preservation conditions for confounding, mediation, collider, and front-door are conditions on the DGP parameters (the relative strength of the causal effect versus the confounding, indirect, or collider-induced bias), not on the confusion matrix $C$.
575	Once the condition is satisfied, sign preservation holds for \emph{all} column-stochastic $C$ with $C_{kk}>0$---no diagonal-dominance restriction is needed.
576	Conversely, if the condition fails (i.e., the omitted-variable or total-effect estimate has the opposite sign from $\tau$), then there exist confusion matrices that produce sign reversal.
577	For the DGP parameters used throughout our experiments, the conditions are comfortably satisfied.
578	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d691594f-3561-40c6-840c-f96be110356e",
  "isSidechain": true,
  "promptId": "ae2d0870-295e-4835-a3f0-f41f20bd6a21",
  "agentId": "a1b64ac8a57b00a7e",
  "type": "user",
  "uuid": "93c934c2-49c2-41a3-bb71-92236a3ed84e",
  "sourceToolAssistantUUID": "d691594f-3561-40c6-840c-f96be110356e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/paper_agent_20baa82f",
  "sessionId": "35fb04f7-d2db-441f-a3b1-35490ca0d54b",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "eventual-sniffing-crane"
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-21T01:08:15.393Z_

Now let me check the experiments.tex file for algorithmic environment usage:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "93c934c2-49c2-41a3-bb71-92236a3ed84e",
  "isSidechain": true,
  "agentId": "a1b64ac8a57b00a7e",
  "requestId": "req_011CbEpW5f7SBDYLqpEK8jpK",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "5249783d-bf14-4d92-b486-a5cca792a659",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/paper_agent_20baa82f",
  "sessionId": "35fb04f7-d2db-441f-a3b1-35490ca0d54b",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "eventual-sniffing-crane",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01LhztZTNZgASLceqnGsaErq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 32919,
      "cache_read_input_tokens": 28018,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 32919,
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

_source line 18 · 2026-05-21T01:08:16.201Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01Qca1HenhR5SXKE9YmzLp7z`</summary>

```json
{
  "pattern": "algpseudocode|algorithmic",
  "path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/experiments.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5249783d-bf14-4d92-b486-a5cca792a659",
  "isSidechain": true,
  "agentId": "a1b64ac8a57b00a7e",
  "requestId": "req_011CbEpW5f7SBDYLqpEK8jpK",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "e12862cc-5bbf-434a-a8bb-d0bf2b942452",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/paper_agent_20baa82f",
  "sessionId": "35fb04f7-d2db-441f-a3b1-35490ca0d54b",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "eventual-sniffing-crane",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01LhztZTNZgASLceqnGsaErq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 32919,
      "cache_read_input_tokens": 28018,
      "output_tokens": 147,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 32919
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 147,
          "cache_read_input_tokens": 28018,
          "cache_creation_input_tokens": 32919,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 32919,
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

_source line 19 · 2026-05-21T01:08:16.215Z_

<details><summary>↩ Tool result · `toolu_01Qca1HenhR5SXKE9YmzLp7z`</summary>

```text
188:\begin{algorithmic}[1]
225:\end{algorithmic}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e12862cc-5bbf-434a-a8bb-d0bf2b942452",
  "isSidechain": true,
  "promptId": "ae2d0870-295e-4835-a3f0-f41f20bd6a21",
  "agentId": "a1b64ac8a57b00a7e",
  "type": "user",
  "uuid": "480b7200-2cb1-4a1c-9b05-e08deefcb3bc",
  "sourceToolAssistantUUID": "e12862cc-5bbf-434a-a8bb-d0bf2b942452",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/paper_agent_20baa82f",
  "sessionId": "35fb04f7-d2db-441f-a3b1-35490ca0d54b",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "eventual-sniffing-crane"
}
```

</details>

---

### Assistant

_source line 20 · 2026-05-21T01:08:21.330Z_

Perfect! Now I'll calculate line counts and word estimates. Here's my analysis:

## Paper Content Volume Report

| File | Line Count | Approx. Word Count |
|------|------------|-------------------|
| abstract.tex | 4 | 180 words |
| introduction.tex | 20 | 450 words |
| related_work.tex | 18 | 500 words |
| method.tex | 99 | 1,850 words |
| experiments.tex | 226 | 2,900 words |
| conclusion.tex | 17 | 350 words |
| appendix_proofs.tex | 578 | 5,500 words |

**Total: 962 lines, ~11,730 words**

### Key Findings:

1. **File Distribution**: The appendix_proofs dominates with ~60% of total line count. The main paper body (abstract through experiments) comprises ~30% of lines.

2. **Content Balance**: 
   - Main matter: abstract + intro + related + method + experiments + conclusion = 384 lines (~6,230 words)
   - Appendix: 578 lines (~5,500 words)

3. **Algorithmic Environment**: **experiments.tex uses `\begin{algorithmic}[1]...\end{algorithmic}`** (found on lines 188-225). This is the correct package for AAAI templates. The `algorithmic` environment (from the `algorithmicx` package) is standard for AAAI; `algpseudocode` is not mentioned anywhere in the paper.

### Page Estimate:
With typical paper formatting (~250-300 words per page), this content volume suggests roughly 40-47 pages total, which is substantial. The appendix_proofs section is particularly dense with mathematical content, so actual page count may run higher due to equation spacing and proof formatting.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "480b7200-2cb1-4a1c-9b05-e08deefcb3bc",
  "isSidechain": true,
  "agentId": "a1b64ac8a57b00a7e",
  "requestId": "req_011CbEpWJLrYjXP4Jf4VrYfH",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "b3eb5b18-6c57-46fa-a8f9-3efdf4fbc7ce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/paper_agent_20baa82f",
  "sessionId": "35fb04f7-d2db-441f-a3b1-35490ca0d54b",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "eventual-sniffing-crane",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01AjjBc4v73AuAcTRE9ZQk2j",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 282,
      "cache_read_input_tokens": 60937,
      "output_tokens": 442,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 282
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4,
          "output_tokens": 442,
          "cache_read_input_tokens": 60937,
          "cache_creation_input_tokens": 282,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 282,
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
