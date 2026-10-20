# Research conversation: I need to extract ALL citation keys from ALL .tex files in /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/dist

**Characterizing the Detectability Landscape of Iterative Model Collapse (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 44
- **Recorded user turns:** 1
- **Tool calls:** 19
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a338a02a4cec945c1.jsonl`
- **Structured JSON:** [`568d0f205000ca0d5d3f.json`](../../sessions/56/568d0f205000ca0d5d3f.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

44 recorded events

### User

_source line 1 · 2026-05-20T13:21:05.460Z_

I need to extract ALL citation keys from ALL .tex files in /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/. 

Search for all citation commands: \cite, \citep, \citet, \citealt, \citealp, \citeauthor, \citeyear, and any other \cite* variants. Note that a single cite command can contain multiple keys separated by commas like \cite{key1, key2, key3}.

Use grep with a broad pattern like `\\cite` to find ALL citation usages across all .tex files. Report every unique citation key found, and which file(s) each key appears in. Be very thorough - search "very thorough" breadth.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "2667bad6-65ed-4e74-8e43-0c340597a9b8",
  "agentId": "a338a02a4cec945c1",
  "type": "user",
  "uuid": "0fd37424-6df3-4796-afee-b5176e5d69b8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "8c4ca842-c198-44f4-8734-f3be30b2ad4c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-20T13:21:08.544Z_

I'll help you extract all citation keys from the .tex files in that directory. Let me start by finding all .tex files and then searching for citation commands.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0fd37424-6df3-4796-afee-b5176e5d69b8",
  "isSidechain": true,
  "agentId": "a338a02a4cec945c1",
  "requestId": "req_011CbDtaYgPU8FTKvjDPYJxG",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "c5c0f4ad-1532-4a5c-8fc7-5ab3ddd4767d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "8c4ca842-c198-44f4-8734-f3be30b2ad4c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01A9buhRNr1sgqAqnFEzmhtf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17933,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17933,
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

_source line 3 · 2026-05-20T13:21:08.789Z_

<details open><summary>🔧 Tool call — Glob · `toolu_016cXMFowcHxczafybZCiUig`</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/**/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c5c0f4ad-1532-4a5c-8fc7-5ab3ddd4767d",
  "isSidechain": true,
  "agentId": "a338a02a4cec945c1",
  "requestId": "req_011CbDtaYgPU8FTKvjDPYJxG",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "1c64fed2-a5d2-43f6-9926-fd6b4f6caf13",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "8c4ca842-c198-44f4-8734-f3be30b2ad4c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01A9buhRNr1sgqAqnFEzmhtf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17933,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17933,
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

_source line 4 · 2026-05-20T13:21:08.812Z_

<details><summary>↩ Tool result · `toolu_016cXMFowcHxczafybZCiUig`</summary>

```text
docs/paper/ethics.tex
docs/paper/background.tex
docs/paper/conclusion.tex
docs/paper/related_work_reframe.tex
docs/paper/discussion_reframe.tex
docs/paper/abstract.tex
docs/paper/discussion.tex
docs/paper/limitations.tex
docs/paper/related_work.tex
docs/paper/intro_reframe.tex
docs/paper/method.tex
docs/paper/method_reframe.tex
docs/paper/experiments_reframe.tex
docs/paper/main.tex
docs/paper/introduction.tex
docs/paper/experiments.tex
docs/paper/appendix.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1c64fed2-a5d2-43f6-9926-fd6b4f6caf13",
  "isSidechain": true,
  "promptId": "2667bad6-65ed-4e74-8e43-0c340597a9b8",
  "agentId": "a338a02a4cec945c1",
  "type": "user",
  "uuid": "578e3fcd-662f-4e4e-970b-698b39fcad96",
  "sourceToolAssistantUUID": "1c64fed2-a5d2-43f6-9926-fd6b4f6caf13",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "8c4ca842-c198-44f4-8734-f3be30b2ad4c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-20T13:21:09.359Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01E4xe8SANR3pg2ogKXeN8mZ`</summary>

```json
{
  "pattern": "\\\\cite",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/",
  "type": "tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "578e3fcd-662f-4e4e-970b-698b39fcad96",
  "isSidechain": true,
  "agentId": "a338a02a4cec945c1",
  "requestId": "req_011CbDtaYgPU8FTKvjDPYJxG",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "7ca51645-6f11-4930-826a-c5ed937625c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "8c4ca842-c198-44f4-8734-f3be30b2ad4c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01A9buhRNr1sgqAqnFEzmhtf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17933,
      "cache_read_input_tokens": 0,
      "output_tokens": 243,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 17933
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 243,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 17933,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 17933,
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

_source line 6 · 2026-05-20T13:21:09.381Z_

<details><summary>↩ Tool result · `toolu_01E4xe8SANR3pg2ogKXeN8mZ`</summary>

```text
docs/paper/related_work.tex:5:Iterative training collapse was formalized by \citet{shumailov2024curse} and \citet{alemohammad2024mad}, who showed that recursively replacing real data with model-generated text causes progressive tail erosion.
docs/paper/related_work.tex:6:Theoretical analyses have sharpened these results: \citet{dohmatob2024tale} recast collapse as a change in scaling-law exponents, and \citet{dohmatob2025strong} proved that collapse can occur even at vanishingly small synthetic fractions.
docs/paper/related_work.tex:7:Several works have proposed monitoring metrics: \citet{du2026geometric} observe that calibration error rises before accuracy degrades, \citet{du2025scales} report ECE increases at 30\% contamination before accuracy drops, and \citet{gambetta2024surplexity} introduces surplexity as a collapse detector.
docs/paper/related_work.tex:8:We differ from the closest predecessor, \citet{du2026geometric}, in four respects: (i)~we compare an entire family of canary metrics; (ii)~we cross-validate across five statistical methods; (iii)~we map detectability as a function of contamination regime; and (iv)~we treat method-selection sensitivity itself as a primary finding.
docs/paper/related_work.tex:11:\citet{gu2024cmr} establish a scaling law for critical mixture ratios in continual pre-training, and \citet{gu2025datamixing} show that data mixing can induce phase transitions in knowledge acquisition---a direct theoretical analogue to our detection phase transition, where a critical mixing ratio separates qualitatively different detection regimes.
docs/paper/related_work.tex:14:\citet{scheffer2009early} established that systems approaching tipping points exhibit generic early-warning signals (rising autocorrelation and variance), while \citet{boettiger2012limits} quantified detection limits in short time series---directly relevant to iterative training where $T{=}5$--$20$.
docs/paper/related_work.tex:15:The standard framework for testing temporal precedence is Granger causality~\cite{granger1969investigating}; however, non-stationary series inflate rejection rates~\cite{granger1974spurious}, and the Toda--Yamamoto procedure~\cite{toda1995statistical} addresses this at reduced degrees of freedom severe in short series.
docs/paper/related_work.tex:19:\citet{bell2022modeling} introduced multiverse analysis to ML, \citet{coretta2023multidimensional} demonstrated that 46 teams reached different conclusions on identical data, and \citet{kapoor2024reforms} synthesized these concerns into a consensus checklist.
docs/paper/discussion_reframe.tex:4:Granger causality tests predictive improvement, not true causation~\cite{granger1969investigating,shojaie2022granger}: an unobserved process could independently drive both token entropy and diversity metrics.
docs/paper/discussion_reframe.tex:20:Layers~1 and~3 are established; Layers~2 and~4 require longer generation protocols ($T{\geq}50$; \citealt{dakos2012methods}).
docs/paper/experiments.tex:7:We study lead-lag analysis pitfalls in iterative training collapse using Pythia-410M \cite{biderman2023pythia}, a 410M-parameter decoder-only language model.
docs/paper/experiments.tex:10:Training data is drawn from WikiText-103 \cite{merity2017pointer}, using 5{,}000-sample subsets per generation.
docs/paper/experiments.tex:12:Our protocol follows the replace paradigm of \citet{shumailov2024curse}, adapted for mixed synthetic-real training at $\alpha{<}1.0$.
docs/paper/experiments.tex:17:We track two \emph{canary metrics} (cheap-to-compute statistics hypothesized to precede downstream degradation, inspired by early-warning signals in dynamical systems \cite{scheffer2009early}) and three \emph{downstream metrics}.
docs/paper/experiments.tex:19:Downstream metrics are distinct-1 and distinct-2 ($n$-gram diversity \cite{li2016diversity}, computed over all 5{,}000 generated samples per generation) and perplexity (evaluated on held-out real data).
docs/paper/experiments.tex:26:Permutation Granger causality tests use 5{,}000 permutations on first-differenced series \cite{shojaie2022granger}.
docs/paper/acl.sty:188:% \citep, \citet, and \citeyearpar for compatibility with natbib, or
docs/paper/acl.sty:189:% \cite, \newcite, and \shortcite for compatibility with older ACL .sty files
docs/paper/acl.sty:190:\renewcommand\cite{\citep}  % to get "(Author Year)" with natbib
docs/paper/acl.sty:191:\newcommand\shortcite{\citeyearpar}% to get "(Year)" with natbib
docs/paper/acl.sty:192:\newcommand\newcite{\citet} % to get "Author (Year)" with natbib
docs/paper/acl.sty:193:\newcommand{\citeposs}[1]{\citeauthor{#1}'s (\citeyear{#1})} % to get "Author's (Year)"
docs/paper/discussion.tex:4:Granger causality tests predictive improvement, not true causation~\cite{granger1969investigating,shojaie2022granger}: an unobserved process could independently drive both token entropy and diversity metrics.
docs/paper/discussion.tex:12:With $T{=}10$ (11 data points per series), our analyses operate near the lower bound of what standard methods require~\cite{boettiger2012limits}; threshold onset and Toda--Yamamoto are power-limited at this length (\S\ref{sec:method}).
docs/paper/discussion.tex:16:The four-regime dose-response---blind, onset, synchronous dip, detection---parallels hormetic patterns in toxicology~\cite{calabrese2003hormesis}, where opposing dose-dependent mechanisms produce non-monotonic responses.
docs/paper/related_work_reframe.tex:6:Iterative training collapse was formalized by \citet{shumailov2024curse} for language models and by \citet{alemohammad2024mad} for image generation, establishing that recursive self-training erodes tail modes and reduces output diversity.
docs/paper/related_work_reframe.tex:7:Theoretical analyses have since shown that even small synthetic fractions alter effective scaling-law exponents \cite{dohmatob2024tale}.
docs/paper/related_work_reframe.tex:8:Several metrics have been proposed as early collapse indicators: calibration error \cite{du2026geometric,du2025scales}, surplexity \cite{gambetta2024surplexity}, spectral divergence \cite{sigma2026spectral}, topological persistence \cite{kalinowski2026topology}, and center-edge dynamics \cite{dces2026counter}.
docs/paper/related_work_reframe.tex:13:The concept of early-warning indicators originates in ecology, where \citet{scheffer2009early} showed that systems approaching tipping points exhibit rising autocorrelation and variance independent of system-specific mechanisms.
docs/paper/related_work_reframe.tex:14:\citet{boettiger2012limits} quantified the detection limits of such signals in short time series, a constraint directly relevant to iterative training where generation counts rarely exceed 20.
docs/paper/related_work_reframe.tex:15:Granger causality \cite{granger1969investigating} provides the standard test for temporal precedence but produces spurious rejections on non-stationary series \cite{granger1974spurious}; the Toda--Yamamoto procedure \cite{toda1995statistical} restores valid inference at the cost of degrees of freedom \cite{shojaie2022granger}, a severe trade-off when $T{\leq}20$.
docs/paper/related_work_reframe.tex:20:Researcher degrees of freedom in ML have received increasing attention through multiverse analysis \cite{bell2022modeling}, many-analysts designs showing that independent teams reach divergent conclusions on identical data \cite{coretta2023multidimensional}, and the REFORMS checklist \cite{kapoor2024reforms}.
docs/paper/related_work_reframe.tex:22:We differ from the closest predecessor \cite{du2026geometric} in four respects: we compare an entire family of canary metrics rather than a single pair, cross-validate each relationship across five statistical methods, apply FDR correction across all tested pairs, and map detectability as a function of contamination regime.
docs/paper/method.tex:8:\emph{Spurious regression}: first-differencing to remove shared trends~\cite{granger1974spurious} eliminates canary$\to$perplexity associations ($F{\approx}0$, $p{=}0.99$) while preserving canary$\to$diversity (24/24$\to$24/24), exposing an entire analysis channel as trend-driven rather than temporally precedent.
docs/paper/method.tex:14:We apply the Multi-Method Consensus Test, a weighted consensus framework in the specification curve~\cite{simonsohn2020specification} and multi-method early-warning~\cite{scheffer2009early,bell2022modeling} traditions, adapted to the constraints of iterative training analysis: short series ($T{=}5$--$20$), non-stationarity by design, and heterogeneous method sensitivities.
docs/paper/method.tex:21:PermG tests whether past values of canary metric $X$ improve prediction of downstream metric $Y$ beyond $Y$'s own history; Granger precedence establishes temporal predictive improvement, not true causality~\cite{shojaie2022granger}.
docs/paper/method.tex:23:Three properties distinguish PermG: a nonparametric null distribution robust to the short non-stationary series typical of iterative training~\cite{boettiger2012limits}, built-in directionality (forward and reverse tested separately), and a hyperparameter-free test statistic.
docs/paper/method.tex:24:[Omitted long matching line]
docs/paper/limitations.tex:9:Canary claims are scoped to distinct-$n$ diversity~\cite{li2016diversity}, not model collapse broadly~\cite{schaeffer2025position}; replace-only protocol means accumulate-mode dynamics~\cite{dey2024breaking} are untested.
docs/paper/background.tex:14:At $\alpha{=}1.0$, this reduces to the full-replacement paradigm of \citet{shumailov2024curse}, where each generation trains exclusively on the previous generation's output.
docs/paper/background.tex:19:\emph{Canary metrics} are cheap-to-compute statistics on the model's output distribution, hypothesized to change before downstream quality degrades, analogous to early-warning indicators studied in the context of critical transitions in dynamical systems \cite{scheffer2009early}.
docs/paper/background.tex:22:We use \emph{distinct-$n$} ($n \in \{1, 2, 3\}$), the ratio of unique $n$-grams to total $n$-grams in generated text \cite{li2016diversity}, as a measure of lexical diversity, and \emph{perplexity} on a held-out set as a measure of language modeling quality.
docs/paper/background.tex:28:The classical framework for testing temporal predictive precedence is Granger causality \cite{granger1969investigating}, which asks whether past values of $X$ improve prediction of $Y$ beyond $Y$'s own history.
docs/paper/background.tex:29:We note that Granger precedence tests predictive improvement, not true causality \cite{shojaie2022granger}; this distinction is discussed further in \S\ref{sec:method}.
docs/paper/background.tex:36:(4)~\emph{permutation Granger causality}, a non-parametric Granger test using 5{,}000 permutations on first-differenced series \cite{shojaie2022granger}; and
docs/paper/background.tex:37:(5)~\emph{Toda--Yamamoto Granger causality}, an augmented VAR approach that tests Granger precedence without requiring prior differencing \cite{toda1995statistical}.
docs/paper/method_reframe.tex:8:\emph{Spurious regression}: first-differencing to remove shared trends~\cite{granger1974spurious} eliminates canary$\to$perplexity associations ($F{\approx}0$, $p{=}0.99$) while preserving canary$\to$diversity (24/24$\to$24/24), exposing an entire analysis channel as trend-driven rather than temporally precedent.
docs/paper/method_reframe.tex:14:We apply the Multi-Method Consensus Test, a weighted consensus framework in the specification curve~\cite{simonsohn2020specification} and multi-method early-warning~\cite{scheffer2009early,bell2022modeling} traditions, adapted to the constraints of iterative training analysis: short series ($T{=}5$--$20$), non-stationarity by design, and heterogeneous method sensitivities.
docs/paper/method_reframe.tex:21:PermG tests whether past values of canary metric $X$ improve prediction of downstream metric $Y$ beyond $Y$'s own history; Granger precedence establishes temporal predictive improvement, not true causality~\cite{shojaie2022granger}.
docs/paper/method_reframe.tex:23:Three properties distinguish PermG: a nonparametric null distribution robust to the short non-stationary series typical of iterative training~\cite{boettiger2012limits}, built-in directionality (forward and reverse tested separately), and a hyperparameter-free test statistic.
docs/paper/method_reframe.tex:24:[Omitted long matching line]
docs/paper/appendix.tex:336:At $\alpha{=}1.0$, this reduces to the full-replacement paradigm of \citet{shumailov2024curse}.
docs/paper/appendix.tex:340:\emph{Downstream metrics}: distinct-$n$ ($n \in \{1, 2, 3\}$)~\cite{li2016diversity} and perplexity.
docs/paper/appendix.tex:345:We employ five methods spanning permissive to conservative: naive cross-correlation, differenced cross-correlation, threshold onset detection, permutation Granger causality~\cite{shojaie2022granger}, and Toda--Yamamoto Granger causality~\cite{toda1995statistical}.
docs/paper/appendix.tex:363:\citet{shumailov2024curse}     & $\times$   & $\times$   & $\times$   & $\circ$    & \checkmark & \checkmark & PPL \\
docs/paper/appendix.tex:364:\citet{du2025scales}           & $\times$   & $\times$   & \checkmark & \checkmark & \checkmark & $\times$   & ECE, Acc, Dist-$n$ \\
docs/paper/appendix.tex:365:\citet{gambetta2024surplexity} & $\times$   & $\times$   & $\times$   & \checkmark & \checkmark & \checkmark & Surplexity, Ent \\
docs/paper/appendix.tex:366:SIGMA~\cite{sigma2026spectral} & $\times$   & $\times$   & $\times$   & $\times$   & $\times$   & $\times$   & Spectral \\
docs/paper/appendix.tex:367:DCES~\cite{dces2026counter}    & $\times$   & $\times$   & $\times$   & $\times$   & $\times$   & \checkmark & ECE, Ent, PPL \\
docs/paper/appendix.tex:404:Extensions include multivariate VAR models for confounder testing, multi-seed replication across all six architecture families, longer training runs ($T{\geq}20$), online monitoring within training pipelines, and accumulate-mode experiments~\cite{dey2024breaking}.
docs/paper/appendix.tex:405:The sigmoid onset boundary ($\alpha_c{=}0.476$) invites connection to the critical mixture ratio scaling law of \citet{gu2024cmr} and the data-mixing phase transitions of \citet{gu2025datamixing}.
docs/paper/intro_reframe.tex:4:When language models train iteratively on their own output, the training distribution progressively loses its tail modes, a phenomenon termed model collapse~\cite{shumailov2024curse,alemohammad2024mad}.
docs/paper/intro_reframe.tex:9:The concept parallels early-warning signals for critical transitions in ecological systems~\cite{scheffer2009early,scheffer2012anticipating}, where proxy indicators allow intervention before a tipping point.
docs/paper/intro_reframe.tex:13:Iterative training produces short, noisy time series (often fewer than 15 points per generation sequence), where detection power drops sharply and false positive rates can be high~\cite{boettiger2012limits}.
docs/paper/intro_reframe.tex:16:(1)~No differencing tests rule out spurious regression from shared non-stationary trends~\cite{granger1974spurious}.
docs/paper/intro_reframe.tex:22:[Omitted long matching line]
docs/paper/intro_reframe.tex:26:Granger precedence in our framework establishes temporal predictive improvement, not true causality~\cite{shojaie2022granger}; our canary claim is scoped to diversity metrics (distinct-$n$~\cite{li2016diversity}), not model collapse broadly.
docs/paper/introduction.tex:4:When language models train iteratively on their own output, the training distribution progressively loses its tail modes, a phenomenon termed model collapse~\cite{shumailov2024curse,alemohammad2024mad}.
docs/paper/introduction.tex:9:The concept parallels early-warning signals for critical transitions in ecological systems~\cite{scheffer2009early,scheffer2012anticipating}, where proxy indicators allow intervention before a tipping point.
docs/paper/introduction.tex:13:Iterative training produces short, noisy time series (often fewer than 15 points per generation sequence), where detection power drops sharply and false positive rates can be high~\cite{boettiger2012limits}.
docs/paper/introduction.tex:16:(1)~No differencing tests rule out spurious regression from shared non-stationary trends~\cite{granger1974spurious}.
docs/paper/introduction.tex:22:Using Pythia-410M~\cite{biderman2023pythia} across thirteen contamination levels ($\alpha \in [0, 1]$, thirteen values from 0.00 to 1.00) and up to four random seeds, we show that causal detectability undergoes a steep onset at per-generation mixing ratio $\alpha_c{=}0.476$ at $T{=}10$ generations (sigmoid $R^2{=}0.969$, $\Delta\alpha{\approx}0.02$): permutation Granger causality (PermG) jumps from 0/8 FDR-significant metric pairs at $\alpha{\leq}0.45$ to 6/8 at $\alpha{=}0.50$.
docs/paper/introduction.tex:26:Granger precedence in our framework establishes temporal predictive improvement, not true causality~\cite{shojaie2022granger}; our canary claim is scoped to diversity metrics (distinct-$n$~\cite{li2016diversity}), not model collapse broadly.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7ca51645-6f11-4930-826a-c5ed937625c2",
  "isSidechain": true,
  "promptId": "2667bad6-65ed-4e74-8e43-0c340597a9b8",
  "agentId": "a338a02a4cec945c1",
  "type": "user",
  "uuid": "ca3d6a33-a8fb-4978-8cc1-201dc09d60a3",
  "sourceToolAssistantUUID": "7ca51645-6f11-4930-826a-c5ed937625c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "8c4ca842-c198-44f4-8734-f3be30b2ad4c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-20T13:21:10.668Z_

Now let me read each .tex file to extract all citation keys systematically:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ca3d6a33-a8fb-4978-8cc1-201dc09d60a3",
  "isSidechain": true,
  "agentId": "a338a02a4cec945c1",
  "requestId": "req_011CbDtaqRxHz9jg25ofJj17",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "4644e0ea-16e8-459c-87b4-c44afa48d699",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "8c4ca842-c198-44f4-8734-f3be30b2ad4c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01U31JWTt1BepDMGsQzbWbsZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 6196,
      "cache_read_input_tokens": 17933,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6196,
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

_source line 8 · 2026-05-20T13:21:11.522Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Too4jGhqfyNFWNXFXPvxcf`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4644e0ea-16e8-459c-87b4-c44afa48d699",
  "isSidechain": true,
  "agentId": "a338a02a4cec945c1",
  "requestId": "req_011CbDtaqRxHz9jg25ofJj17",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "b60bcb41-6597-4d88-a62b-c9b5bfe30a4d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "8c4ca842-c198-44f4-8734-f3be30b2ad4c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01U31JWTt1BepDMGsQzbWbsZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 6196,
      "cache_read_input_tokens": 17933,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6196,
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

_source line 9 · 2026-05-20T13:21:11.530Z_

<details><summary>↩ Tool result · `toolu_01Too4jGhqfyNFWNXFXPvxcf`</summary>

```text
1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Model collapse and canary metrics.}
5	Iterative training collapse was formalized by \citet{shumailov2024curse} and \citet{alemohammad2024mad}, who showed that recursively replacing real data with model-generated text causes progressive tail erosion.
6	Theoretical analyses have sharpened these results: \citet{dohmatob2024tale} recast collapse as a change in scaling-law exponents, and \citet{dohmatob2025strong} proved that collapse can occur even at vanishingly small synthetic fractions.
7	Several works have proposed monitoring metrics: \citet{du2026geometric} observe that calibration error rises before accuracy degrades, \citet{du2025scales} report ECE increases at 30\% contamination before accuracy drops, and \citet{gambetta2024surplexity} introduces surplexity as a collapse detector.
8	We differ from the closest predecessor, \citet{du2026geometric}, in four respects: (i)~we compare an entire family of canary metrics; (ii)~we cross-validate across five statistical methods; (iii)~we map detectability as a function of contamination regime; and (iv)~we treat method-selection sensitivity itself as a primary finding.
9	
10	\paragraph{Data mixing phase transitions.}
11	\citet{gu2024cmr} establish a scaling law for critical mixture ratios in continual pre-training, and \citet{gu2025datamixing} show that data mixing can induce phase transitions in knowledge acquisition---a direct theoretical analogue to our detection phase transition, where a critical mixing ratio separates qualitatively different detection regimes.
12	
13	\paragraph{Critical transitions and lead-lag methodology.}
14	\citet{scheffer2009early} established that systems approaching tipping points exhibit generic early-warning signals (rising autocorrelation and variance), while \citet{boettiger2012limits} quantified detection limits in short time series---directly relevant to iterative training where $T{=}5$--$20$.
15	The standard framework for testing temporal precedence is Granger causality~\cite{granger1969investigating}; however, non-stationary series inflate rejection rates~\cite{granger1974spurious}, and the Toda--Yamamoto procedure~\cite{toda1995statistical} addresses this at reduced degrees of freedom severe in short series.
16	These methods are largely absent from the model collapse literature.
17	
18	\paragraph{Analytical robustness.}
19	\citet{bell2022modeling} introduced multiverse analysis to ML, \citet{coretta2023multidimensional} demonstrated that 46 teams reached different conclusions on identical data, and \citet{kapoor2024reforms} synthesized these concerns into a consensus checklist.
20	Our work applies this perspective to model collapse: five methods across multiple contamination regimes produce conclusions ranging from universal significance to complete null.
21	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b60bcb41-6597-4d88-a62b-c9b5bfe30a4d",
  "isSidechain": true,
  "promptId": "2667bad6-65ed-4e74-8e43-0c340597a9b8",
  "agentId": "a338a02a4cec945c1",
  "type": "user",
  "uuid": "b0d62daa-d780-4c0a-9db6-607fa2fa7e2e",
  "sourceToolAssistantUUID": "b60bcb41-6597-4d88-a62b-c9b5bfe30a4d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "8c4ca842-c198-44f4-8734-f3be30b2ad4c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-20T13:21:11.734Z_

<details open><summary>🔧 Tool call — Read · `toolu_01T1pYpTrE65Gk9gnYEdKCBP`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/discussion_reframe.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b0d62daa-d780-4c0a-9db6-607fa2fa7e2e",
  "isSidechain": true,
  "agentId": "a338a02a4cec945c1",
  "requestId": "req_011CbDtaqRxHz9jg25ofJj17",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f86aa554-f75c-433d-96ea-68db6a290ea3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "8c4ca842-c198-44f4-8734-f3be30b2ad4c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01U31JWTt1BepDMGsQzbWbsZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 6196,
      "cache_read_input_tokens": 17933,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6196,
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

_source line 11 · 2026-05-20T13:21:11.743Z_

<details><summary>↩ Tool result · `toolu_01T1pYpTrE65Gk9gnYEdKCBP`</summary>

```text
1	\section{Discussion and Conclusion}\label{sec:discussion}
2	
3	\paragraph{Granger precedence is not causation.}
4	Granger causality tests predictive improvement, not true causation~\cite{granger1969investigating,shojaie2022granger}: an unobserved process could independently drive both token entropy and diversity metrics.
5	Our central claim is scoped accordingly---``token entropy Granger-precedes diversity collapse''---and bivariate tests cannot exclude confounders; multivariate VAR models would be required to test for confounders directly.
6	
7	\paragraph{Practical utility paradox.}
8	The framework works best where it is least needed: at $\alpha{\geq}0.75$, PermG reliably detects canary precedence, but degradation is already severe; at $\alpha{\leq}0.45$, where early warning would be most valuable, detection remains null.
9	However, in realistic pipelines, contamination $\alpha$ is unknown and typically increases over time as web-scraped corpora accumulate machine-generated text.
10	A continuous monitoring dashboard would trigger when $\alpha$ crosses the detectability threshold, converting the static limitation into a temporal advantage.
11	The regime map itself is actionable: practitioners who know $\alpha{<}0.25$ should invest in data provenance rather than metric monitoring.
12	
13	\paragraph{Four-layer detection taxonomy.}
14	Our results suggest a layered taxonomy ordered by onset threshold:
15	(1)~distributional dimensionality (effective rank, onset $\alpha{\approx}0.10$);
16	(2)~distributional instability (entropy variance, suggestive at $\alpha{\approx}0.25$);
17	(3)~causal coupling (Granger-type, onset $\alpha_c{\approx}0.50$); and
18	(4)~dynamical stability (AC1, suggestive but not conclusive at $T{=}11$).
19	The 40-percentage-point gap between structural distortion (Layer~1) and causal evidence (Layer~3) constitutes the detection phase transition.
20	Layers~1 and~3 are established; Layers~2 and~4 require longer generation protocols ($T{\geq}50$; \citealt{dakos2012methods}).
21	
22	\paragraph{Synchronous collapse at $\alpha{=}0.60$.}
23	The non-monotonic dip at $\alpha{=}0.60$ (PermG fwd below both $\alpha{=}0.50$ and $\alpha{=}0.75$) is consistent with the $S \times R$ prediction (\S\ref{sec:theory}): relaxation time matching drives $R \to 0$, so entropy and diversity respond within the same generation despite rising signal strength.
24	This creates a four-regime structure---blind, onset, synchronous dip, detection---rather than the binary boundary assumed by simpler models.
25	
26	\paragraph{Method recommendation.}
27	The primary value of the multi-method framework is the systematic comparison it enables.
28	By applying five methods with different inductive biases, the framework reveals why each succeeds or fails: naive cross-correlation inflates FPR via reverse-directional associations; differenced cross-correlation cannot separate forward from reverse; threshold onset lacks power at $T{=}11$; Toda--Yamamoto achieves moderate detection (3--4/8) but is sensitive to augmentation order.
29	This process of elimination converges on PermG as the recommended method: zero null-control FPR, consistent detection at $\alpha{\geq}0.50$, and clean directional separation (24/24 forward, 0/24 reverse at $\alpha{=}1.0$ on WikiText).
30	
31	\paragraph{Conclusion.}
32	Lead-lag analysis in iterative training collapse is far more fragile than assumed: method choice alone inflates spurious-signal rates to 75\% null-control FPR, first-differencing exposes canary$\to$perplexity associations as entirely spurious, and regime dependence causes the same test to shift from significant to null.
33	PermG identifies token entropy as a one-generation-ahead canary for diversity collapse, validated across 15 model-seed combinations spanning six families (345M--6.9B) with detection in 13 cases (87\%).
34	Directional asymmetry is domain-dependent (unidirectional on WikiText, bidirectional on C4), and canary-based predictive cessation reduces peak perplexity by 58\%.
35	Extended discussion of cross-architecture generalization, domain-dependent directionality, token entropy versus perplexity, NLP-specific constraints, and future directions appears in Appendix~\ref{app:extended_discussion}.
36	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f86aa554-f75c-433d-96ea-68db6a290ea3",
  "isSidechain": true,
  "promptId": "2667bad6-65ed-4e74-8e43-0c340597a9b8",
  "agentId": "a338a02a4cec945c1",
  "type": "user",
  "uuid": "86e28f0a-5cbb-464f-ae67-5816b2457d97",
  "sourceToolAssistantUUID": "f86aa554-f75c-433d-96ea-68db6a290ea3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "8c4ca842-c198-44f4-8734-f3be30b2ad4c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-20T13:21:12.148Z_

<details open><summary>🔧 Tool call — Read · `toolu_0119zY4dRWTzj3hviHzJe9V9`</summary>

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
  "parentUuid": "86e28f0a-5cbb-464f-ae67-5816b2457d97",
  "isSidechain": true,
  "agentId": "a338a02a4cec945c1",
  "requestId": "req_011CbDtaqRxHz9jg25ofJj17",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "6e391a97-cdd5-4553-a94b-1ca31e017817",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "8c4ca842-c198-44f4-8734-f3be30b2ad4c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01U31JWTt1BepDMGsQzbWbsZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 6196,
      "cache_read_input_tokens": 17933,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6196,
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

_source line 13 · 2026-05-20T13:21:12.154Z_

<details><summary>↩ Tool result · `toolu_0119zY4dRWTzj3hviHzJe9V9`</summary>

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
14	We run $T{=}10$ generations (11 time points including the generation-0 baseline) across six primary contamination levels $\alpha \in \{0.00, 0.10, 0.25, 0.50, 0.75, 1.00\}$ with multi-seed replication, plus seven single-seed probing points ($\alpha \in \{0.05, 0.30, 0.35, 0.40, 0.45, 0.55, 0.60\}$) to resolve the onset boundary, yielding a 13-point $\alpha$ grid.
15	The $\alpha{=}1.0$ condition uses four random seeds $\{42, 43, 44, 45\}$; $\alpha \in \{0.00, 0.25, 0.50, 0.75\}$ each use three seeds $\{42, 43, 44\}$; remaining levels use a single seed (42).
16	
17	We track two \emph{canary metrics} (cheap-to-compute statistics hypothesized to precede downstream degradation, inspired by early-warning signals in dynamical systems \cite{scheffer2009early}) and three \emph{downstream metrics}.
18	Canary metrics are token entropy (next-token prediction entropy averaged over held-out samples) and expected calibration error (ECE).
19	Downstream metrics are distinct-1 and distinct-2 ($n$-gram diversity \cite{li2016diversity}, computed over all 5{,}000 generated samples per generation) and perplexity (evaluated on held-out real data).
20	Token entropy is the mean next-token prediction entropy $H(p_\theta | \text{context})$ averaged over 1{,}000 held-out samples; ECE uses 15 equal-width bins.
21	We additionally evaluate effective rank and Self-BLEU as candidate canaries (Appendix).
22	Results for distinct-3 are reported in Appendix~\ref{app:distinct3}.
23	Code and data will be released upon publication.
24	
25	All hypothesis tests apply Benjamini--Hochberg (BH) FDR correction at $q{=}0.05$.
26	Permutation Granger causality tests use 5{,}000 permutations on first-differenced series \cite{shojaie2022granger}.
27	Cross-correlation analysis uses a maximum lag of 5 generations.
28	Raw metric drift from generation~0 to generation~10 is summarized in Appendix Table~\ref{tab:drift_summary}.
29	
30	
31	\subsection{Detection Phase Transition}
32	\label{sec:regime}
33	
34	Diversity collapse occurs at every contamination level: distinct-1 declines by $14.1\%$ at $\alpha{=}0.0$ (fine-tuning drift) and by $40.3{\pm}0.3\%$ at $\alpha{=}0.25$ (3-seed mean).
35	Despite this ubiquitous degradation, causal detectability is sharply regime-dependent.
36	Permutation Granger (PermG) tests find 0/8 canary$\to$downstream pairs FDR-significant from $\alpha{=}0.00$ through $\alpha{=}0.45$, then jump to 6/8 at $\alpha{=}0.50$ (2~fp32 seeds, consistent).
37	This transition is striking because cumulative synthetic fraction barely changes across the boundary: $C = 1{-}(1{-}\alpha)^{10}$ yields $99.75\%$ at $\alpha{=}0.45$ versus $99.90\%$ at $\alpha{=}0.50$, a difference of 0.15 percentage points, yet detection jumps from null to reliable.
38	Sigmoid regression across the 13-point $\alpha$ grid quantifies this steep onset: $\alpha_c = 0.476$ (bootstrap 95\% CI: [0.43, 0.56]), steepness $k \geq 200$, transition width $\Delta\alpha \approx 0.02$ (CI: [0.008, 0.060]), $R^2 = 0.969$ (versus power-law $R^2 = 0.808$, $\Delta\mathrm{AIC} = 18.2$; Figure~\ref{fig:regime_map}).
39	The transition width is $6{\times}$ narrower than the estimation uncertainty in $\alpha_c$'s position, confirming a genuinely steep onset rather than an artifact of sparse sampling.
40	A model-free Fisher exact test corroborates the categorical jump: 0/64 pairs FDR-significant at $\alpha \leq 0.45$ versus 18/32 at $\alpha \geq 0.50$ ($p = 3.45 \times 10^{-11}$).
41	At $\alpha{=}0.45$, PermG $p$-values reveal sub-threshold signal ($p_{\mathrm{fdr}} = 0.059$ for seed~43, $0.091$ for seed~42), consistent with the power-threshold interpretation of $\alpha_c$ at $T{=}10$ (\S\ref{sec:theory}): the onset reflects PermG's power curve crossing the detection floor, not the emergence of a new physical signal.
42	A specification curve analysis spanning 1{,}160 analytical specifications confirms that the detection phase transition is specification-invariant.
43	
44	First-differencing scopes the canary claim precisely.
45	Canary$\to$diversity pairs retain unanimous FDR significance after first-differencing ($24/24 \to 24/24$ across 4~seeds at $\alpha{=}1.0$, 6 pairs per seed), while canary$\to$perplexity collapses entirely ($F \approx 0$, $p = 0.99$): the apparent perplexity association is a shared-trend artifact.
46	All canary claims are therefore scoped to diversity metrics only.
47	At $\alpha{=}1.0$, all 24 canary$\to$diversity pairs (6 per seed $\times$ 4~seeds; mauve excluded) reach FDR significance in the forward direction with 0/24 reverse; directional asymmetry is robust across all WikiText conditions.
48	The canary mechanism also exhibits a blind spot: at $\alpha{=}0.10$, distinct-1 has already dropped by $39.6\%$, yet token entropy is indistinguishable from the null ($-5.3\%$ versus $-4.6{\pm}0.4\%$ at $\alpha{=}0.0$).
49	Below $\alpha_c$ at $T{=}10$, diversity collapse proceeds without any detectable causal signal in the canary metrics.
50	
51	\begin{figure}[t]
52	\centering
53	\includegraphics[width=\linewidth]{figures/metric_trajectory.pdf}
54	\caption{Metric trajectories at $\alpha{=}1.0$ (Pythia-410M, 4~seeds). Token entropy drops at generation~1; distinct-1 declines from generations~2--3, with a consistent one-generation canary lead across all four seeds (shaded: inter-seed range). This pattern corresponds to 24/24 forward and 0/24 reverse FDR-significant canary$\to$diversity pairs (6 per seed, mauve excluded).}
55	\label{fig:metric_trajectory}
56	\end{figure}
57	
58	
59	\subsection{Dose-Response and the $S \times R$ Framework}
60	\label{sec:dose_response}
61	
62	The PermG dose-response profile (Figure~\ref{fig:regime_map}) reveals four detection regimes: \emph{blind} ($\alpha \leq 0.45$, 0/8 FDR-significant pairs), \emph{onset} ($\alpha \approx 0.50$, 6/8), \emph{synchronous dip} ($\alpha \approx 0.60$, 0/8 both seeds; dual-seed confirmed), and \emph{detection} ($\alpha \geq 0.75$, 5--6/8 per seed across 3~seeds; $\alpha{=}1.0$, 6/8 across 4~seeds).
63	The non-monotonic dip at $\alpha{=}0.60$ is consistent with the $S \times R$ framework (\S\ref{sec:theory}): signal strength $S(\alpha)$ rises monotonically with contamination, but temporal resolution $R(\alpha)$ drops when relaxation time approaches the observation interval.
64	At $\alpha \approx 0.60$, this compression drives the canary-to-downstream lag toward zero, and the product $S \times R$ reaches a local minimum.
65	The synchronous zone is mechanistically distinct from the blind spot: in the blind zone, canary drift is indistinguishable from the null; in the synchronous zone, both canary and downstream metrics drift substantially but without temporal offset.
66	
67	Method choice is itself a major source of analytic variability.
68	At $\alpha{=}1.0$, direction-checked forward significance rates span 0\% to 75\%: naive and differenced cross-correlation fall to 0/8 after lag-direction filtering (all significant correlations peak at negative lags), while PermG achieves 6/8 (Table~\ref{tab:method_comparison}). Inter-method agreement is $\kappa{=}0.185$ (near chance).
69	PermG is the only method that combines zero null-control FPR with consistent detection at $\alpha \geq 0.50$ (Table~\ref{tab:method_comparison}); its nonparametric null distribution, built-in directionality, and hyperparameter-free design explain this advantage.
70	The $S \times R$ framework generates three testable predictions for $T{=}20$ via $\mathrm{Power}(\alpha, T) = \Phi(S \cdot R \cdot \sqrt{T}/\sigma)$: (i)~$\alpha_c$ at $T{=}10$ should left-shift, (ii)~the transition should smooth, and (iii)~different methods should exhibit different $\alpha_c$ values.
71	These predictions are under empirical verification.
72	
73	\begin{figure}[t]
74	\centering
75	\includegraphics[width=\linewidth]{figures/fig_dose_response.pdf}
76	\caption{PermG forward detection rate across 13 contamination levels (Pythia-410M, fp32, direction-checked). Four regimes: blind ($\alpha \leq 0.45$, 0/8), onset ($\alpha{=}0.50$, 6/8), synchronous dip ($\alpha{=}0.60$, 0/8), and detection ($\alpha \geq 0.75$, 5--6/8).}
77	\label{fig:regime_map}
78	\end{figure}
79	
80	\begin{table}[t]
81	\centering
82	\small
83	\caption{Forward-direction FDR significance rates (\%) across contamination levels (Pythia-410M, seed~42, fp32; $3\sigma$ threshold calibration, lag-direction filtering for cross-correlation methods). Each cell: fraction of 8 validated pairs at BH-corrected significance ($q{=}0.05$). PermG is the only method combining zero null-control FPR with consistent detection at $\alpha \geq 0.50$.}
84	\label{tab:method_comparison}
85	\resizebox{\columnwidth}{!}{%
86	\begin{tabular}{lcccccc}
87	\toprule
88	Method & $\alpha{=}0.0$ & $\alpha{=}0.25$ & $\alpha{=}0.50$ & $\alpha{=}0.75$ & $\alpha{=}1.0$ & FPR$_\text{null}$ \\
89	\midrule
90	Naive XCorr          & 75   & 62.5 & 62.5 & 0    & 0    & 75  \\
91	Diff.\ XCorr         & 0    & 25   & 12.5 & 0    & 0    & 0   \\
92	Threshold ($3\sigma$) & 37.5 & 62.5 & 100  & 100  & 25   & 37.5 \\
93	Perm.\ Granger       & 0    & 0    & 75   & 75   & 75   & 0   \\
94	Toda--Yamamoto       & 12.5 & 37.5 & 50   & 100  & 12.5 & 12.5 \\
95	\bottomrule
96	\end{tabular}}
97	\end{table}
98	
99	
100	\subsection{Cross-Architecture Generalization}
101	\label{sec:generalization}
102	
103	We evaluate the detection phase transition across 15 model-seed combinations spanning six families (Pythia, GPT-2, OPT, Qwen, SmolLM3, Padding-variant), scales from 345M to 6.9B parameters, and two training domains (WikiText-103, C4).
104	Table~\ref{tab:generalization} reports PermG forward detection at $\alpha{=}1.0$.
105	PermG forward significance reaches ${\geq}$6/8 in 13 of 15 conditions (87\%).
106	Two exceptions emerge: Pythia-1.4B seed~42 on WikiText (2/8), a seed-dependent outlier that recovers to 6/8 in seed~43, and SmolLM3-3B (3/8), where only ECE$\to$downstream pairs reach significance while entropy$\to$downstream pairs fail entirely (0/4; details in Appendix).
107	SmolLM3's token entropy exhibits non-monotonic oscillations across generations; this pattern violates the monotonic decline that Granger tests require.
108	The onset boundary $\alpha_c \approx 0.50$ at $T{=}10$ is architecture-independent: every family that achieves detection does so at or above this threshold, and none achieves reliable detection below it.
109	
110	Replacing WikiText-103 with C4 yields the strongest detection observed: Pythia-1B reaches PermG fwd 8/8 (both seeds), and Pythia-1.4B reaches 8/8 on C4 versus 2/8 on WikiText at the same scale.
111	At Pythia-6.9B (bf16), detection recovers to 7/8 on WikiText.
112	Dataset characteristics modulate detection power independently of model capacity.
113	Directional asymmetry shows preliminary domain variation: in one C4 seed-condition pair ($\alpha{=}0.50$, s42), PermG reverse reaches 7/8, but this is seed-dependent (s43: 1/8) and we note it as a preliminary observation requiring further investigation (\S\ref{sec:discussion}).
114	
115	\begin{table}[t]
116	\centering
117	\small
118	\caption{Cross-architecture PermG forward detection ($\alpha{=}1.0$). Detection (${\geq}$6/8) confirmed in 13/15 conditions (87\%) across six model families, scales from 345M to 6.9B, and two domains.}
119	\label{tab:generalization}
120	\begin{tabular}{lrcl}
121	\toprule
122	Model & Params & Domain & PermG fwd \\
123	\midrule
124	Pythia-410M    & 410M & Wiki & 6/8 \\
125	Pythia-1.4B    & 1.4B & Wiki & 2--6/8$^\dagger$ \\
126	Pythia-6.9B    & 6.9B & Wiki & 7/8$^*$ \\
127	GPT-2-medium   & 345M & Wiki & 6/8 \\
128	OPT-1.3B       & 1.3B & Wiki & 6/8 \\
129	Qwen3.5-0.8B   & 0.8B & Wiki & 8/8 \\
130	SmolLM3-3B     & 3.0B & Wiki & 3/8$^\ddagger$ \\
131	Padding-410M   & 410M & Wiki & 6/8 \\
132	\addlinespace
133	Pythia-1B      & 1.0B & C4   & 8/8 \\
134	Pythia-1.4B    & 1.4B & C4   & 8/8 \\
135	\bottomrule
136	\multicolumn{4}{l}{\footnotesize $^\dagger$Seed-dependent (s42: 2/8, s43: 6/8).} \\
137	\multicolumn{4}{l}{\footnotesize $^*$bf16 (exceeds single-GPU fp32 capacity).} \\
138	\multicolumn{4}{l}{\footnotesize $^\ddagger$ECE-only canary (entropy 0/4).} \\
139	\multicolumn{4}{l}{\footnotesize Multi-seed (range shown): Pythia-410M, -1.4B Wiki,} \\
140	\multicolumn{4}{l}{\footnotesize GPT-2-med, OPT-1.3B, Pythia-1B C4 (2 seeds each).} \\
141	\multicolumn{4}{l}{\footnotesize Others: single seed. Total: 15 combinations.} \\
142	\end{tabular}
143	\end{table}
144	
145	
146	\subsection{Canary-Based Early Intervention}
147	\label{sec:intervention}
148	
149	We implement a predictive cessation protocol: training with synthetic data ($\alpha{=}1.0$) continues until token entropy drops ${>}15\%$ relative to generation~0, at which point $\alpha$ switches to $0.0$ (pure real data).
150	A reactive baseline triggers when distinct-1 drops ${>}10\%$.
151	The predictive trigger fires at generation~1 in both Pythia-410M and Pythia-1.4B (s42 fp32), one generation before the reactive baseline (generation~2).
152	Peak perplexity under predictive intervention is $56.99$ versus $157.09$ under reactive (s42 fp32), a 58\% reduction (bootstrap 95\% CI: 29--64\%).
153	Recovery occurs at generation~2 under predictive cessation versus generation~4 under reactive.
154	Both models converge to the $\alpha{=}0.0$ baseline by generation~10.
155	
156	The trigger generation, recovery timeline, and convergence behavior are identical across the $3.4\times$ scale gap from 410M to 1.4B, and the 15\% entropy threshold generalizes without recalibration.
157	These results position canary-based detection within a four-layer taxonomy of collapse monitoring: (1)~dimensionality collapse, detectable at $\alpha \geq 0.10$ via $n$-gram diversity decline; (2)~distributional variance, detectable at $\alpha \geq 0.25$ via calibration drift; (3)~causal coupling, detectable at $\alpha \geq 0.50$ via Granger precedence; and (4)~dynamical stability, assessable at $\alpha \geq 0.50$ via lag structure.
158	Each layer captures a distinct aspect of collapse, and lower layers activate at lower contamination thresholds.
159	The practical implication is that canary monitoring should combine multiple detection layers rather than rely on any single statistical test.
160	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6e391a97-cdd5-4553-a94b-1ca31e017817",
  "isSidechain": true,
  "promptId": "2667bad6-65ed-4e74-8e43-0c340597a9b8",
  "agentId": "a338a02a4cec945c1",
  "type": "user",
  "uuid": "6eaffcc5-0267-4e7b-acf0-abb32fc0a0f2",
  "sourceToolAssistantUUID": "6e391a97-cdd5-4553-a94b-1ca31e017817",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "8c4ca842-c198-44f4-8734-f3be30b2ad4c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-20T13:21:12.360Z_

<details open><summary>🔧 Tool call — Read · `toolu_01DzYDfLiSsJuydFFyo7NsBA`</summary>

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
  "parentUuid": "6eaffcc5-0267-4e7b-acf0-abb32fc0a0f2",
  "isSidechain": true,
  "agentId": "a338a02a4cec945c1",
  "requestId": "req_011CbDtaqRxHz9jg25ofJj17",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "c2fe7b86-bbad-45f6-8095-702f743011cd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "8c4ca842-c198-44f4-8734-f3be30b2ad4c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01U31JWTt1BepDMGsQzbWbsZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 6196,
      "cache_read_input_tokens": 17933,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6196,
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

_source line 15 · 2026-05-20T13:21:12.365Z_

<details><summary>↩ Tool result · `toolu_01DzYDfLiSsJuydFFyo7NsBA`</summary>

```text
1	\section{Discussion and Conclusion}\label{sec:discussion}
2	
3	\paragraph{Granger precedence is not causation.}
4	Granger causality tests predictive improvement, not true causation~\cite{granger1969investigating,shojaie2022granger}: an unobserved process could independently drive both token entropy and diversity metrics.
5	Our central claim is scoped accordingly---``token entropy Granger-precedes diversity collapse''---and bivariate tests cannot exclude confounders; multivariate VAR models would be required for confounder testing.
6	
7	\paragraph{Calibration scope.}
8	First-differencing exposes canary$\to$perplexity associations as entirely spurious ($F{\approx}0$, $p{=}0.99$) while preserving canary$\to$diversity leads (24/24$\to$24/24), confirming that the apparent perplexity association is a shared-trend artifact.
9	All canary claims are therefore scoped to diversity metrics only.
10	
11	\paragraph{Short time-series constraint.}
12	With $T{=}10$ (11 data points per series), our analyses operate near the lower bound of what standard methods require~\cite{boettiger2012limits}; threshold onset and Toda--Yamamoto are power-limited at this length (\S\ref{sec:method}).
13	Longer generation chains ($T{\geq}20$) are predicted by the $S \times R$ framework to left-shift $\alpha_c$ and smooth the transition; these predictions are under empirical verification.
14	
15	\paragraph{Regime interpretation.}
16	The four-regime dose-response---blind, onset, synchronous dip, detection---parallels hormetic patterns in toxicology~\cite{calabrese2003hormesis}, where opposing dose-dependent mechanisms produce non-monotonic responses.
17	At $\alpha{\approx}0.60$, temporal resolution $R \to 0$ (entropy and diversity respond within the same generation), suppressing detection despite rising signal, analogous to zero-lag Granger causality failure in synchronous systems.
18	Exploratory CSD analysis reveals a consistent pattern---canary metrics show rising autocorrelation (Kendall $\tau{=}0.79$--$0.82$) while downstream metrics show none ($\tau{=}0.03$--$0.30$)---but this does not survive multiple testing correction (2/10 post-BH).
19	
20	\paragraph{Cross-architecture scope.}
21	Directional asymmetry is domain-dependent: C4 exhibits seed-sensitive bidirectional coupling (s42: 7/8 reverse vs.\ s43: 1/8; preliminary observation, \S\ref{sec:generalization}).
22	SmolLM3-3B reveals architecture-dependent canary sensitivity: token entropy exhibits non-monotonic oscillations (0/4 significant), while ECE maintains monotonic growth (3/4 significant, PermG fwd 3/8).
23	
24	\paragraph{Conclusion.}
25	Lead-lag analysis in iterative training collapse is far more fragile than assumed: method choice alone inflates spurious-signal rates to 75\% null-control FPR, and regime dependence causes the same test to shift from significant to null.
26	PermG identifies token entropy as a one-generation-ahead canary for diversity collapse, validated across 15 model-seed combinations spanning six families (345M--6.9B) with detection in 13 cases (87\%).
27	Canary-based predictive cessation reduces peak perplexity by 58\%.
28	Extended discussion of token entropy versus perplexity, NLP-specific constraints, the four-layer detection taxonomy, and future directions appears in Appendix~\ref{app:extended_discussion}.
29	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c2fe7b86-bbad-45f6-8095-702f743011cd",
  "isSidechain": true,
  "promptId": "2667bad6-65ed-4e74-8e43-0c340597a9b8",
  "agentId": "a338a02a4cec945c1",
  "type": "user",
  "uuid": "df971f49-632d-4fee-8295-8375586dc12d",
  "sourceToolAssistantUUID": "c2fe7b86-bbad-45f6-8095-702f743011cd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "8c4ca842-c198-44f4-8734-f3be30b2ad4c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-20T13:21:12.590Z_

<details open><summary>🔧 Tool call — Read · `toolu_0192wMBWiD1pC2fMgbyGpWch`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/related_work_reframe.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "df971f49-632d-4fee-8295-8375586dc12d",
  "isSidechain": true,
  "agentId": "a338a02a4cec945c1",
  "requestId": "req_011CbDtaqRxHz9jg25ofJj17",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "ce36812f-c486-47be-97ac-b118d8cf7b71",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "8c4ca842-c198-44f4-8734-f3be30b2ad4c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01U31JWTt1BepDMGsQzbWbsZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 6196,
      "cache_read_input_tokens": 17933,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6196,
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

_source line 17 · 2026-05-20T13:21:12.596Z_

<details><summary>↩ Tool result · `toolu_0192wMBWiD1pC2fMgbyGpWch`</summary>

```text
1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Model collapse and canary metrics.}
5	
6	Iterative training collapse was formalized by \citet{shumailov2024curse} for language models and by \citet{alemohammad2024mad} for image generation, establishing that recursive self-training erodes tail modes and reduces output diversity.
7	Theoretical analyses have since shown that even small synthetic fractions alter effective scaling-law exponents \cite{dohmatob2024tale}.
8	Several metrics have been proposed as early collapse indicators: calibration error \cite{du2026geometric,du2025scales}, surplexity \cite{gambetta2024surplexity}, spectral divergence \cite{sigma2026spectral}, topological persistence \cite{kalinowski2026topology}, and center-edge dynamics \cite{dces2026counter}.
9	Yet none of these analyses apply differencing tests to rule out spurious co-trending, cross-validate across multiple statistical methods, or apply false discovery rate correction when testing multiple metric pairs.
10	
11	\paragraph{Early-warning signals and lead-lag methodology.}
12	
13	The concept of early-warning indicators originates in ecology, where \citet{scheffer2009early} showed that systems approaching tipping points exhibit rising autocorrelation and variance independent of system-specific mechanisms.
14	\citet{boettiger2012limits} quantified the detection limits of such signals in short time series, a constraint directly relevant to iterative training where generation counts rarely exceed 20.
15	Granger causality \cite{granger1969investigating} provides the standard test for temporal precedence but produces spurious rejections on non-stationary series \cite{granger1974spurious}; the Toda--Yamamoto procedure \cite{toda1995statistical} restores valid inference at the cost of degrees of freedom \cite{shojaie2022granger}, a severe trade-off when $T{\leq}20$.
16	Yet these ecological and econometric tools have not been combined for model collapse; existing canary studies rely on visual inspection or naive correlation that cannot distinguish temporal precedence from shared trends.
17	
18	\paragraph{Analytical robustness.}
19	
20	Researcher degrees of freedom in ML have received increasing attention through multiverse analysis \cite{bell2022modeling}, many-analysts designs showing that independent teams reach divergent conclusions on identical data \cite{coretta2023multidimensional}, and the REFORMS checklist \cite{kapoor2024reforms}.
21	Our work applies this perspective to collapse monitoring.
22	We differ from the closest predecessor \cite{du2026geometric} in four respects: we compare an entire family of canary metrics rather than a single pair, cross-validate each relationship across five statistical methods, apply FDR correction across all tested pairs, and map detectability as a function of contamination regime.
23	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ce36812f-c486-47be-97ac-b118d8cf7b71",
  "isSidechain": true,
  "promptId": "2667bad6-65ed-4e74-8e43-0c340597a9b8",
  "agentId": "a338a02a4cec945c1",
  "type": "user",
  "uuid": "8eaeb5dc-8a07-4b5e-952b-0367e8253453",
  "sourceToolAssistantUUID": "ce36812f-c486-47be-97ac-b118d8cf7b71",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "8c4ca842-c198-44f4-8734-f3be30b2ad4c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-20T13:21:12.858Z_

<details open><summary>🔧 Tool call — Read · `toolu_014kn2icWn44hgomDgXXi67N`</summary>

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
  "parentUuid": "8eaeb5dc-8a07-4b5e-952b-0367e8253453",
  "isSidechain": true,
  "agentId": "a338a02a4cec945c1",
  "requestId": "req_011CbDtaqRxHz9jg25ofJj17",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "39c4447c-c93c-4cbd-bf86-157a884d9a3c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "8c4ca842-c198-44f4-8734-f3be30b2ad4c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01U31JWTt1BepDMGsQzbWbsZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 6196,
      "cache_read_input_tokens": 17933,
      "output_tokens": 476,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6196
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 476,
          "cache_read_input_tokens": 17933,
          "cache_creation_input_tokens": 6196,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6196,
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

_source line 19 · 2026-05-20T13:21:12.872Z_

<details><summary>↩ Tool result · `toolu_014kn2icWn44hgomDgXXi67N`</summary>

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
14	We apply the Multi-Method Consensus Test, a weighted consensus framework in the specification curve~\cite{simonsohn2020specification} and multi-method early-warning~\cite{scheffer2009early,bell2022modeling} traditions, adapted to the constraints of iterative training analysis: short series ($T{=}5$--$20$), non-stationarity by design, and heterogeneous method sensitivities.
15	MMCT is a consensus testing protocol, not a novel statistical method.
16	It compares five lead-lag detection methods through FPR-inverse weighted consensus, calibrated against null-control ($\alpha{=}0.0$) data where any detection is a false positive.
17	Each method $m_k$ receives weight $w_k = 1/\max(\hat{\text{FPR}}_k, \epsilon)$ with $\epsilon{=}0.01$; the weighted score $W(X \to Y) = \sum_k w_k d_k / \sum_k w_k$ yields formal $p$-values from the empirical null distribution (Appendix).
18	MMCT identifies permutation Granger (PermG) as the only method combining zero null-control FPR with consistent detection across contamination levels, and we recommend it as the primary detection method based on this systematic comparison.
19	
20	\paragraph{Permutation Granger causality.}
21	PermG tests whether past values of canary metric $X$ improve prediction of downstream metric $Y$ beyond $Y$'s own history; Granger precedence establishes temporal predictive improvement, not true causality~\cite{shojaie2022granger}.
22	We apply 5{,}000 permutations on first-differenced series with Benjamini--Hochberg FDR correction at $q{=}0.05$ across 8 validated canary$\to$downstream pairs (2 canaries $\times$ 4 downstream metrics).
23	Three properties distinguish PermG: a nonparametric null distribution robust to the short non-stationary series typical of iterative training~\cite{boettiger2012limits}, built-in directionality (forward and reverse tested separately), and a hyperparameter-free test statistic.
24	The remaining four methods each exhibit a specific limitation: naive cross-correlation has 75\% null-control FPR; differenced cross-correlation detects bidirectionally without directional separation; threshold onset is power-limited at $T{=}11$ under corrected $3\sigma$ calibration (0/8 significant in 8 of 12 cross-architecture conditions); Toda--Yamamoto~\cite{toda1995statistical} achieves moderate supplementary detection (3--4/8 at $\alpha{\geq}0.50$) with reduced power from degree-of-freedom costs of lag augmentation.
25	Per-method dose-response profiles, Shapley value analysis, and the full MMCT algorithm appear in the Appendix.
26	
27	\subsection{Signal-Times-Resolution Framework}
28	\label{sec:theory}
29	
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
42	The detection phase transition at $\alpha_c$ (at $T{=}10$) is consistent with a power threshold: when $S \cdot R \cdot \sqrt{T}$ first exceeds the detection floor, power undergoes a steep onset from near-zero to near-one.
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
  "parentUuid": "39c4447c-c93c-4cbd-bf86-157a884d9a3c",
  "isSidechain": true,
  "promptId": "2667bad6-65ed-4e74-8e43-0c340597a9b8",
  "agentId": "a338a02a4cec945c1",
  "type": "user",
  "uuid": "f9e3575f-5689-4633-aa02-9f831cfbd5ce",
  "sourceToolAssistantUUID": "39c4447c-c93c-4cbd-bf86-157a884d9a3c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "8c4ca842-c198-44f4-8734-f3be30b2ad4c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 20 · 2026-05-20T13:21:14.375Z_

Now let me read the remaining files:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f9e3575f-5689-4633-aa02-9f831cfbd5ce",
  "isSidechain": true,
  "agentId": "a338a02a4cec945c1",
  "requestId": "req_011CbDtb6Va8VHvQQBrds6JL",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "98472a06-ccc4-4a4f-a389-73d867d2fa18",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "8c4ca842-c198-44f4-8734-f3be30b2ad4c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HM715txuCLVstHvUBP1VcL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 11995,
      "cache_read_input_tokens": 24129,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11995,
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

_source line 21 · 2026-05-20T13:21:15.016Z_

<details open><summary>🔧 Tool call — Read · `toolu_01SBRwMTE3w7nWhpxSjQai6K`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "98472a06-ccc4-4a4f-a389-73d867d2fa18",
  "isSidechain": true,
  "agentId": "a338a02a4cec945c1",
  "requestId": "req_011CbDtb6Va8VHvQQBrds6JL",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "319b22ba-b8c9-49e5-b128-7ff92a03a828",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "8c4ca842-c198-44f4-8734-f3be30b2ad4c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HM715txuCLVstHvUBP1VcL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 11995,
      "cache_read_input_tokens": 24129,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11995,
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

_source line 22 · 2026-05-20T13:21:15.030Z_

<details><summary>↩ Tool result · `toolu_01SBRwMTE3w7nWhpxSjQai6K`</summary>

```text
1	\section*{Limitations}
2	\label{sec:limitations}
3	
4	Our experiments are validated at scales ${\leq}6.9$B parameters across six decoder-only transformer families; whether the temporal lead persists at frontier scale is open.
5	Training data is drawn from WikiText-103 and C4 subsets, three orders of magnitude smaller than production corpora; C4 results carry a pre-training data confound (Pythia was pre-trained on Pile, which overlaps with C4).
6	With $T{=}10$ (11 data points), threshold onset and Toda--Yamamoto are power-limited; $T{\geq}20$ validation is pending.
7	PermG requires null-control ($\alpha{=}0.0$) calibration data, which may not be available in all deployment settings.
8	The $\alpha{=}0.60$ results use bf16 precision from a single seed; fp32 multi-seed confirmation is needed.
9	Canary claims are scoped to distinct-$n$ diversity~\cite{li2016diversity}, not model collapse broadly~\cite{schaeffer2025position}; replace-only protocol means accumulate-mode dynamics~\cite{dey2024breaking} are untested.
10	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "319b22ba-b8c9-49e5-b128-7ff92a03a828",
  "isSidechain": true,
  "promptId": "2667bad6-65ed-4e74-8e43-0c340597a9b8",
  "agentId": "a338a02a4cec945c1",
  "type": "user",
  "uuid": "253e9fff-21de-4f4b-b642-a31200ecd7c5",
  "sourceToolAssistantUUID": "319b22ba-b8c9-49e5-b128-7ff92a03a828",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "8c4ca842-c198-44f4-8734-f3be30b2ad4c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-20T13:21:15.256Z_

<details open><summary>🔧 Tool call — Read · `toolu_01E9wKaEfb9bfxnCgXX469re`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/background.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "253e9fff-21de-4f4b-b642-a31200ecd7c5",
  "isSidechain": true,
  "agentId": "a338a02a4cec945c1",
  "requestId": "req_011CbDtb6Va8VHvQQBrds6JL",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "9146f92d-5bc3-4d34-8efb-2f97292c6cc3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "8c4ca842-c198-44f4-8734-f3be30b2ad4c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HM715txuCLVstHvUBP1VcL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 11995,
      "cache_read_input_tokens": 24129,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11995,
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

_source line 24 · 2026-05-20T13:21:15.261Z_

<details><summary>↩ Tool result · `toolu_01E9wKaEfb9bfxnCgXX469re`</summary>

```text
1	\section{Background}
2	\label{sec:background}
3	
4	This section establishes the formal setup and notation used throughout the paper.
5	
6	\paragraph{Iterative training loop.}
7	Let $M_0$ denote a pretrained language model and $\mathcal{D}_\text{real}$ a fixed corpus of human-written text.
8	At each generation $t \geq 1$, the model $M_{t-1}$ generates a synthetic corpus $\mathcal{D}_\text{synth}^{(t-1)}$, and the next-generation model $M_t$ is fine-tuned on a mixture of $\alpha$ fraction synthetic data and $(1{-}\alpha)$ fraction real data:
9	\begin{equation}
10	    \mathcal{D}_\text{train}^{(t)} = \alpha \cdot \mathcal{D}_\text{synth}^{(t-1)} \;+\; (1{-}\alpha) \cdot \mathcal{D}_\text{real}, \quad \alpha \in [0, 1].
11	    \label{eq:mixing}
12	\end{equation}
13	The contamination level $\alpha$ controls the fraction of machine-generated text in each training round.
14	At $\alpha{=}1.0$, this reduces to the full-replacement paradigm of \citet{shumailov2024curse}, where each generation trains exclusively on the previous generation's output.
15	Iterating this process for $T$ generations yields a trajectory $M_0 \to M_1 \to \cdots \to M_T$.
16	
17	\paragraph{Metric families.}
18	We distinguish two families of metrics evaluated at each generation~$t$.
19	\emph{Canary metrics} are cheap-to-compute statistics on the model's output distribution, hypothesized to change before downstream quality degrades, analogous to early-warning indicators studied in the context of critical transitions in dynamical systems \cite{scheffer2009early}.
20	We consider two canary metrics: \emph{token entropy}, the average next-token prediction entropy over held-out samples, and \emph{expected calibration error} (ECE), which measures the discrepancy between predicted token probabilities and empirical correctness frequencies.
21	\emph{Downstream metrics} capture generation quality directly.
22	We use \emph{distinct-$n$} ($n \in \{1, 2, 3\}$), the ratio of unique $n$-grams to total $n$-grams in generated text \cite{li2016diversity}, as a measure of lexical diversity, and \emph{perplexity} on a held-out set as a measure of language modeling quality.
23	Each metric produces a time series of $T{+}1$ observations (generations $0$ through $T$).
24	
25	\paragraph{The lead-lag testing problem.}
26	Given two such time series $X = (x_0, \ldots, x_T)$ and $Y = (y_0, \ldots, y_T)$ (for instance, a canary metric and a downstream metric), the central question is whether changes in $X$ temporally precede changes in $Y$.
27	This requires more than measuring correlation: the test must establish \emph{directionality} ($X \to Y$ rather than $Y \to X$) and account for confounders such as shared non-stationary trends that can produce spurious associations.
28	The classical framework for testing temporal predictive precedence is Granger causality \cite{granger1969investigating}, which asks whether past values of $X$ improve prediction of $Y$ beyond $Y$'s own history.
29	We note that Granger precedence tests predictive improvement, not true causality \cite{shojaie2022granger}; this distinction is discussed further in \S\ref{sec:method}.
30	
31	\paragraph{Five detection methods.}
32	We employ five lead-lag detection methods spanning a spectrum from permissive to conservative:
33	(1)~\emph{naive cross-correlation}, which computes Pearson correlation on undifferenced series at lags up to~5;
34	(2)~\emph{differenced cross-correlation}, which applies the same procedure to first-differenced series, removing shared linear trends;
35	(3)~\emph{threshold onset detection}, which compares the generation at which each metric first exceeds a predefined deviation threshold;
36	(4)~\emph{permutation Granger causality}, a non-parametric Granger test using 5{,}000 permutations on first-differenced series \cite{shojaie2022granger}; and
37	(5)~\emph{Toda--Yamamoto Granger causality}, an augmented VAR approach that tests Granger precedence without requiring prior differencing \cite{toda1995statistical}.
38	These methods differ in their assumptions about stationarity, their sensitivity to shared trends, and their statistical power at short time-series lengths.
39	Their joint application forms the basis of the multi-method consensus framework developed in \S\ref{sec:method}.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9146f92d-5bc3-4d34-8efb-2f97292c6cc3",
  "isSidechain": true,
  "promptId": "2667bad6-65ed-4e74-8e43-0c340597a9b8",
  "agentId": "a338a02a4cec945c1",
  "type": "user",
  "uuid": "95662f37-ddb5-424d-8462-393b57e3b5da",
  "sourceToolAssistantUUID": "9146f92d-5bc3-4d34-8efb-2f97292c6cc3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "8c4ca842-c198-44f4-8734-f3be30b2ad4c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-20T13:21:15.704Z_

<details open><summary>🔧 Tool call — Read · `toolu_0196vuBZ9MeaLqfYwEfLmJwe`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method_reframe.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "95662f37-ddb5-424d-8462-393b57e3b5da",
  "isSidechain": true,
  "agentId": "a338a02a4cec945c1",
  "requestId": "req_011CbDtb6Va8VHvQQBrds6JL",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "5c1740cc-2009-4e24-8ef0-d585882f992d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "8c4ca842-c198-44f4-8734-f3be30b2ad4c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HM715txuCLVstHvUBP1VcL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 11995,
      "cache_read_input_tokens": 24129,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11995,
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

_source line 26 · 2026-05-20T13:21:15.713Z_

<details><summary>↩ Tool result · `toolu_0196vuBZ9MeaLqfYwEfLmJwe`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	\paragraph{Methodological pitfalls.}
5	\label{sec:pitfalls}
6	Lead-lag analysis in iterative model collapse is fragile along three axes, each documented with data from \S\ref{sec:regime}--\ref{sec:dose_response}.
7	\emph{Method sensitivity}: five detection methods applied to identical data ($\alpha{=}1.0$, 16 canary$\to$downstream pairs) yield significance rates from 100\% (naive cross-correlation) to 37.5\% (permutation Granger), with inter-method agreement at $\kappa{=}0.185$ and a spurious-signal rate ${\geq}62.5\%$.
8	\emph{Spurious regression}: first-differencing to remove shared trends~\cite{granger1974spurious} eliminates canary$\to$perplexity associations ($F{\approx}0$, $p{=}0.99$) while preserving canary$\to$diversity (24/24$\to$24/24), exposing an entire analysis channel as trend-driven rather than temporally precedent.
9	\emph{Regime dependence}: the same Granger test finds 0/8 pairs significant through $\alpha{=}0.45$ but 6/8 at $\alpha{=}0.50$, a categorical shift at a 5-percentage-point boundary that a single-$\alpha$ study would miss entirely.
10	These pitfalls motivate systematic method comparison rather than reliance on any single detection approach.
11	
12	\paragraph{Multi-Method Consensus Test (MMCT).}
13	\label{sec:mmct}
14	We apply the Multi-Method Consensus Test, a weighted consensus framework in the specification curve~\cite{simonsohn2020specification} and multi-method early-warning~\cite{scheffer2009early,bell2022modeling} traditions, adapted to the constraints of iterative training analysis: short series ($T{=}5$--$20$), non-stationarity by design, and heterogeneous method sensitivities.
15	MMCT is a consensus testing protocol, not a novel statistical method.
16	It compares five lead-lag detection methods through FPR-inverse weighted consensus, calibrated against null-control ($\alpha{=}0.0$) data where any detection is a false positive.
17	Each method $m_k$ receives weight $w_k = 1/\max(\hat{\text{FPR}}_k, \epsilon)$ with $\epsilon{=}0.01$; the weighted score $W(X \to Y) = \sum_k w_k d_k / \sum_k w_k$ yields formal $p$-values from the empirical null distribution (Algorithm~\ref{alg:mmct}; Appendix).
18	MMCT identifies permutation Granger (PermG) as the only method combining zero null-control FPR with consistent detection across contamination levels, and we recommend it as the primary detection method based on this systematic comparison.
19	
20	\paragraph{Permutation Granger causality.}
21	PermG tests whether past values of canary metric $X$ improve prediction of downstream metric $Y$ beyond $Y$'s own history; Granger precedence establishes temporal predictive improvement, not true causality~\cite{shojaie2022granger}.
22	We apply 5{,}000 permutations on first-differenced series with Benjamini--Hochberg FDR correction at $q{=}0.05$ across 8 validated canary$\to$downstream pairs (2 canaries $\times$ 4 downstream metrics).
23	Three properties distinguish PermG: a nonparametric null distribution robust to the short non-stationary series typical of iterative training~\cite{boettiger2012limits}, built-in directionality (forward and reverse tested separately), and a hyperparameter-free test statistic.
24	The remaining four methods each exhibit a specific limitation: naive cross-correlation has 75\% null-control FPR; differenced cross-correlation detects bidirectionally without directional separation; threshold onset is power-limited at $T{=}11$ under corrected $3\sigma$ calibration (0/8 significant in 8 of 12 cross-architecture conditions); Toda--Yamamoto~\cite{toda1995statistical} achieves moderate supplementary detection (3--4/8 at $\alpha{\geq}0.50$) with reduced power from degree-of-freedom costs of lag augmentation.
25	Per-method dose-response profiles, Shapley value analysis, and the full MMCT algorithm appear in the Appendix.
26	
27	\subsection{Signal-Times-Resolution Framework}
28	\label{sec:theory}
29	
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
42	The detection phase transition at $\alpha_c$ (at $T{=}10$) is consistent with a power threshold: when $S \cdot R \cdot \sqrt{T}$ first exceeds the detection floor, power undergoes a steep onset from near-zero to near-one.
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
  "parentUuid": "5c1740cc-2009-4e24-8ef0-d585882f992d",
  "isSidechain": true,
  "promptId": "2667bad6-65ed-4e74-8e43-0c340597a9b8",
  "agentId": "a338a02a4cec945c1",
  "type": "user",
  "uuid": "0ca8b0f4-ffc8-4c18-9997-ae4b5633064a",
  "sourceToolAssistantUUID": "5c1740cc-2009-4e24-8ef0-d585882f992d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "8c4ca842-c198-44f4-8734-f3be30b2ad4c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-20T13:21:15.948Z_

<details open><summary>🔧 Tool call — Read · `toolu_01JjseWhW6TyCBLVGYiGUteE`</summary>

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
  "parentUuid": "0ca8b0f4-ffc8-4c18-9997-ae4b5633064a",
  "isSidechain": true,
  "agentId": "a338a02a4cec945c1",
  "requestId": "req_011CbDtb6Va8VHvQQBrds6JL",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "040f7cfb-8c1b-4e00-bc3f-3d54fdba220a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "8c4ca842-c198-44f4-8734-f3be30b2ad4c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HM715txuCLVstHvUBP1VcL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 11995,
      "cache_read_input_tokens": 24129,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11995,
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

_source line 28 · 2026-05-20T13:21:16.169Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Bndrn9tRRi2KcKyUXD22NN`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/intro_reframe.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "040f7cfb-8c1b-4e00-bc3f-3d54fdba220a",
  "isSidechain": true,
  "agentId": "a338a02a4cec945c1",
  "requestId": "req_011CbDtb6Va8VHvQQBrds6JL",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "1e882d46-0263-4a5d-b747-4ef974af5201",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "8c4ca842-c198-44f4-8734-f3be30b2ad4c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HM715txuCLVstHvUBP1VcL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 11995,
      "cache_read_input_tokens": 24129,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11995,
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

_source line 29 · 2026-05-20T13:21:16.288Z_

<details><summary>↩ Tool result · `toolu_01JjseWhW6TyCBLVGYiGUteE`</summary>

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
69	Toda--Yamamoto is the only method exhibiting window-dependent sensitivity: after correcting the statsmodels API incompatibility (\S\ref{sec:method}), TY consensus stabilizes at $T_{\min}{\geq}6$, slightly later than the primary methods, reflecting the additional degrees of freedom consumed by the augmentation order $d_{\max}$.
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
85	TY pairs (/6)        & $\dagger$ & $\dagger$ & 3--6 & 3--6 & 3--6 & 3--6 & 3--6 & 6 \\
86	Stable               & ---       & ---       & \checkmark & \checkmark & \checkmark & \checkmark & \checkmark & \checkmark \\
87	\bottomrule
88	\multicolumn{9}{l}{\footnotesize $\dagger$~Insufficient degrees of freedom for Granger-type tests ($<6$ data points).}
89	\end{tabular}}
90	\end{table}
91	
92	
93	\section{Robustness Checks}
94	\label{app:robustness}
95	
96	\paragraph{Permutation count stability.}
97	Table~\ref{tab:nperm_stability} compares permutation Granger $p$-values at 5{,}000 versus 10{,}000 permutations across all canary$\to$downstream pairs at $\alpha{=}0.75$ (3~seeds, 24~pairs).
98	Permutation Granger $p$-values are stable to within 0.002 between 5{,}000 and 10{,}000 permutations, with zero significance decisions affected.
99	
100	\begin{table}[h]
101	\centering
102	\small
103	\caption{Permutation count stability analysis ($\alpha{=}0.75$, 3~seeds, 24 canary$\to$downstream pairs). $p$-values from permutation Granger tests at $n_{\text{perm}}{=}5{,}000$ versus $n_{\text{perm}}{=}10{,}000$.}
104	\label{tab:nperm_stability}
105	\begin{tabular}{lc}
106	\toprule
107	Metric & Value \\
108	\midrule
109	Max $|\Delta p|$ & 0.010 \\
110	Mean $|\Delta p|$ & 0.002 \\
111	Significance flips & 0 / 24 \\
112	\bottomrule
113	\end{tabular}
114	\end{table}
115	
116	\paragraph{FDR threshold sensitivity.}
117	Table~\ref{tab:fdr_sensitivity} reports the effect of varying the BH FDR threshold $q$ on treatment ($\alpha{=}0.75$, 3~seeds) versus null ($\alpha{=}0.0$, 3~seeds) separation for permutation Granger tests.
118	Treatment/null separation is qualitatively robust to FDR threshold choice; the null control remains at 0/24 across all thresholds.
119	
120	\begin{table}[h]
121	\centering
122	\small
123	\caption{FDR threshold sensitivity for permutation Granger significance. Treatment: $\alpha{=}0.75$ (3~seeds, 24 forward-direction pairs). Null: $\alpha{=}0.0$ (3~seeds, 24 pairs). The null control produces zero false positives at all thresholds tested.}
124	\label{tab:fdr_sensitivity}
125	\resizebox{\columnwidth}{!}{%
126	\begin{tabular}{lccc}
127	\toprule
128	$q$ & Null FDR-sig (/24) & Treatment FDR-sig (/24) & Separation \\
129	\midrule
130	0.01 & 0 & 0  & Clean (underpowered) \\
131	0.05 & 0 & 19 & Clean \\
132	0.10 & 0 & 24 & Clean \\
133	\bottomrule
134	\end{tabular}}
135	\end{table}
136	
137	\paragraph{PermG $p$-value gradient at the onset boundary ($\alpha{=}0.45$).}
138	At the onset boundary, PermG operates near its detection limit, and marginal $p$-values exhibit seed-dependent variation consistent with the statistical power interpretation (\S\ref{sec:theory}).
139	Table~\ref{tab:fdr_gradient_a045} reports BH-corrected $p$-values for all 8 canary$\to$downstream pairs across two seeds at $\alpha{=}0.45$.
140	Seed~43 reaches a minimum FDR-corrected $p{=}0.059$ (18\% above the $q{=}0.05$ threshold), while seed~42 reaches $p{=}0.091$ (82\% above threshold).
141	No pair crosses the significance threshold at either seed, yielding the aggregate 0/8 detection rate reported in \S\ref{sec:regime}.
142	The gradient is consistent with a continuous power transition rather than a binary absence of signal: PermG operates near its detection limit at $\alpha{=}0.45$, with seed-dependent variation in marginal $p$-values.
143	
144	\begin{table}[h]
145	\centering
146	\small
147	\caption{BH-corrected PermG $p$-values at $\alpha{=}0.45$ (8 canary$\to$downstream pairs $\times$ 2 seeds). Min $p_{\mathrm{fdr}}$ per seed shown. All pairs remain above the $q{=}0.05$ threshold, yielding 0/8 aggregate detection.}
148	\label{tab:fdr_gradient_a045}
149	\begin{tabular}{lcc}
150	\toprule
151	 & Seed 42 & Seed 43 \\
152	\midrule
153	Min FDR $p$ & 0.091 & 0.059 \\
154	Gap to $q{=}0.05$ & 82\% & 18\% \\
155	PermG fwd sig (/8) & 0 & 0 \\
156	\bottomrule
157	\end{tabular}
158	\end{table}
159	
160	\section{Transfer Entropy Analysis}
161	\label{app:transfer_entropy}
162	
163	Table~\ref{tab:te_results} reports Transfer Entropy (TE) results aggregated across all baseline conditions.
164	TE was estimated using 3-bin discretization with permutation testing ($n{=}5{,}000$).
165	No pair reaches BH-corrected significance ($q{=}0.05$) in any condition, confirming that non-parametric information-theoretic methods lack detection power at $T{=}11$.
166	
167	\begin{table}[h]
168	\centering
169	\small
170	\caption{Transfer Entropy results (12 runs across all $\alpha$ levels). TE\textsubscript{fwd}: canary$\to$downstream; TE\textsubscript{rev}: downstream$\to$canary. Mean uncorrected permutation $p$-values ($n{=}5{,}000$). No pair reaches BH-corrected $q{<}0.05$ in any run.}
171	\label{tab:te_results}
172	\resizebox{\columnwidth}{!}{%
173	\begin{tabular}{llcccc}
174	\toprule
175	Canary & Downstream & TE\textsubscript{fwd} (mean) & $p$\textsubscript{fwd} (mean) & TE\textsubscript{rev} (mean) & $p$\textsubscript{rev} (mean) \\
176	\midrule
177	token\_entropy & distinct-1 & 0.289 & 0.559 & 0.480 & 0.490 \\
178	token\_entropy & distinct-2 & 0.300 & 0.529 & 0.496 & 0.447 \\
179	token\_entropy & distinct-3 & 0.255 & 0.645 & 0.484 & 0.459 \\
180	token\_entropy & perplexity & 0.257 & 0.676 & 0.386 & 0.626 \\
181	ECE & distinct-1 & 0.185 & 0.720 & 0.184 & 0.891 \\
182	ECE & distinct-2 & 0.208 & 0.683 & 0.216 & 0.846 \\
183	ECE & distinct-3 & 0.209 & 0.689 & 0.227 & 0.807 \\
184	ECE & perplexity & 0.296 & 0.572 & 0.263 & 0.747 \\
185	\bottomrule
186	\end{tabular}}
187	\end{table}
188	
189	\section{Change-Point Detection Analysis}
190	\label{app:change_point}
191	
192	We apply a max-split change-point test with bootstrap significance assessment ($n{=}5{,}000$, $p{<}0.05$) to each metric's generation-level time series ($T{=}11$).
193	
194	Under the null control ($\alpha{=}0.00$, 3~seeds), downstream diversity metrics (distinct-1, distinct-2, distinct-3) produce significant change-points at generation~2 in all seeds (9/9 tests). With additional significant tests from ECE (2/3 seeds) and token entropy (1/3 seeds), the overall false positive rate reaches 66.7\% (12/18 tests; Table~\ref{tab:cp_null}). The monotonic drift inherent in iterative self-training is sufficient to trigger change-point detection even without canary contamination. Individual change-point significance therefore cannot serve as standalone evidence for a canary-specific effect.
195	
196	Although individual significance is unreliable as a discriminator, the temporal ordering of detected change-points reverses between null and treatment conditions. In the null ($\alpha{=}0.00$), downstream metrics show the earliest significant breaks at generation~2 (all seeds), while significant canary breaks appear later (ECE at generations~4--8). Under treatment conditions ($\alpha{\geq}0.75$), this ordering flips: canary metrics place their best splits at generation~1, followed by downstream diversity metrics at generations~2--4 and perplexity at generation~4 (Table~\ref{tab:cp_results}). This ordering reversal provides complementary evidence from a distinct statistical framework, consistent with the Granger causality analysis in \S\ref{sec:experiments}.
197	
198	Several caveats apply. The 18 individual tests per condition were not corrected for multiple comparisons (BH or Bonferroni); primary inference rests on the cross-metric temporal ordering rather than on individual significance tests. Under treatment conditions, token entropy places its best split at generation~1 with large effect sizes ($|d|{>}2.5$) in all seeds, but the pre-change segment at a generation-1 split contains only a single data point, reducing bootstrap power (1/3 seeds significant at $\alpha{=}0.75$). The short series length ($T{=}11$) further limits overall detection power.
199	
200	\begin{table}[h]
201	\centering
202	\small
203	\caption{Change-point detection under null control ($\alpha{=}0.00$, 3 seeds). CP: detected change-point generation (mean across significant seeds); $|d|$: Cohen's $d$ effect size (mean across all seeds); Sig.\ rate: fraction of seeds where $p{<}0.05$. Overall FPR: 12/18 = 66.7\%.}
204	\label{tab:cp_null}
205	\resizebox{\columnwidth}{!}{%
206	\begin{tabular}{lcccc}
207	\toprule
208	Metric & CP gen (mean) & $|d|$ (mean) & Sig.\ rate & Type \\
209	\midrule
210	token\_entropy & 1.0 & 2.94 & 1/3 & canary \\
211	ECE & 6.0 & 1.62 & 2/3 & canary \\
212	distinct-1 & 2.0 & 2.27 & 3/3 & downstream \\
213	distinct-2 & 2.0 & 2.40 & 3/3 & downstream \\
214	distinct-3 & 2.0 & 2.27 & 3/3 & downstream \\
215	perplexity & --- & 3.11 & 0/3 & downstream \\
216	\bottomrule
217	\end{tabular}}
218	\end{table}
219	
220	\begin{table}[h]
221	\centering
222	\small
223	\caption{Change-point detection at $\alpha{=}0.75$ (3 seeds). CP: detected change-point generation; $|d|$: Cohen's $d$ effect size between pre- and post-change segments. Sig.\ rate: fraction of seeds where $p{<}0.05$.}
224	\label{tab:cp_results}
225	\resizebox{\columnwidth}{!}{%
226	\begin{tabular}{lcccc}
227	\toprule
228	Metric & CP gen (mean) & $|d|$ (mean) & Sig.\ rate & Type \\
229	\midrule
230	token\_entropy & 1.0 & 3.21 & 1/3 & canary \\
231	ECE & 1.0 & 3.10 & 1/3 & canary \\
232	distinct-1 & 2.3 & 2.18 & 3/3 & downstream \\
233	distinct-2 & 3.0 & 1.97 & 3/3 & downstream \\
234	distinct-3 & 3.7 & 1.86 & 3/3 & downstream \\
235	perplexity & 4.0 & 1.70 & 3/3 & downstream \\
236	\bottomrule
237	\end{tabular}}
238	\end{table}
239	
240	\paragraph{Dose-response ordering pattern.}
241	Table~\ref{tab:cp_ordering} summarizes the ordering pattern across contamination levels.
242	The canary-to-downstream gap shifts monotonically from negative (downstream first) under the null to positive (canary first) under treatment, ruling out a methodological artifact in which canary metrics would systematically appear earlier regardless of condition.
243	The $\alpha{=}1.0$ analysis is limited to a single seed (s42); all other conditions use 3 seeds.
244	
245	\begin{table}[h]
246	\centering
247	\small
248	\resizebox{\columnwidth}{!}{%
249	\begin{tabular}{lcccl}
250	\toprule
251	$\alpha$ & Canary cp & Downstream cp & Gap & Direction \\
252	\midrule
253	0.00 & gen 4--8 & gen 2 & $-$2.5 & Downstream first \\
254	0.25 & gen 3--4 & gen 3--4 & $\approx$0 & Simultaneous \\
255	0.75 & gen 1 & gen 2--4 & $+$2.25 & Canary first \\
256	1.00 & gen 2 & gen 2--5 & $+$1.0 & Canary first \\
257	\bottomrule
258	\end{tabular}}
259	\caption{Change-point ordering reversal across contamination levels. Under the null ($\alpha{=}0.00$), downstream metrics break before canary metrics; this ordering reverses monotonically as $\alpha$ increases, consistent with the Granger-causal precedence analysis.}
260	\label{tab:cp_ordering}
261	\end{table}
262	
263	
264	\section{Sequential Monitoring: CUSUM vs Calibrated Threshold}
265	\label{app:csmp}
266	
267	We translate the Granger-precedence finding into a deployable monitoring protocol using CUSUM (cumulative sum) sequential testing, calibrated against the $\alpha{=}0.0$ null control.
268	The null-calibration procedure sets the alarm threshold $h$ such that the false alarm rate (FAR) is 0\% on null data (3~seeds, $T{=}10$), providing controlled Type~I error guarantees.
269	
270	\paragraph{Method.}
271	CUSUM monitors the cumulative deviation of token entropy from its null-control baseline: $S_t = \max(0,\; S_{t-1} + (\mu_0 - x_t) - k)$, where $\mu_0$ is the null-control mean, $k$ is the allowance parameter, and the alarm triggers when $S_t > h$.
272	We calibrate $h$ for each $k$ from the $\alpha{=}0.0$ null data (Table~\ref{tab:csmp_calibration}).
273	As a baseline, we compare against a simple calibrated threshold: alarm when the metric crosses $\mu_0 - 2\sigma_0$ for $n{\geq}1$ or $n{\geq}2$ consecutive generations.
274	
275	\begin{table}[h]
276	\centering
277	\small
278	\caption{CUSUM calibration parameters from $\alpha{=}0.0$ null control (3~seeds). $h$: alarm threshold calibrated to achieve FAR${=}$0\%. For $k{\geq}0.25$, the null CUSUM statistic remains at zero, yielding $h \approx 0$.}
279	\label{tab:csmp_calibration}
280	\begin{tabular}{lcc}
281	\toprule
282	$k$ & $h$ & FAR \\
283	\midrule
284	0.05 & 1.530 & 0\% \\
285	0.10 & 1.005 & 0\% \\
286	0.25 & $\approx$0 & 0\% \\
287	0.50 & $\approx$0 & 0\% \\
288	1.00 & $\approx$0 & 0\% \\
289	\bottomrule
290	\end{tabular}
291	\end{table}
292	
293	\paragraph{Results.}
294	Table~\ref{tab:csmp_comparison} compares CUSUM and simple threshold detection times across gradual contamination levels.
295	At the recommended operating point ($k{=}0.25$), CUSUM and the simple threshold ($n{\geq}1$) produce identical alarm times (generation~1) across all seeds and contamination levels.
296	More conservative CUSUM settings ($k{=}0.1$, $k{=}0.05$) delay detection to match the $n{\geq}2$ threshold or later.
297	At $k{=}1.0$ with $\alpha{=}0.50$, CUSUM fails entirely ($S_t \equiv 0$ for all seeds), demonstrating sensitivity to the allowance parameter.
298	No CUSUM configuration outperforms the simple calibrated threshold at any operating point tested.
299	
300	\begin{table}[h]
301	\centering
302	\small
303	\caption{CUSUM vs simple calibrated threshold: alarm generation across contamination levels (3~seeds each; all seeds agree on the alarm generation shown). Threshold: metric crosses $\mu_0 - 2\sigma_0$. No CUSUM configuration outperforms the simple threshold at any operating point.}
304	\label{tab:csmp_comparison}
305	\resizebox{\columnwidth}{!}{%
306	\begin{tabular}{lccccc}
307	\toprule
308	$\alpha$ & CUSUM $k{=}0.25$ & CUSUM $k{=}0.1$ & CUSUM $k{=}0.05$ & Thresh $n{\geq}1$ & Thresh $n{\geq}2$ \\
309	\midrule
310	0.50 & gen 1 & gen 2 & gen 3 & gen 1 & gen 2 \\
311	0.75 & gen 1 & gen 2 & gen 2 & gen 1 & gen 2 \\
312	\bottomrule
313	\multicolumn{6}{l}{\footnotesize CUSUM $k{=}1.0$ at $\alpha{=}0.50$: $S_t \equiv 0$ for all seeds (complete detection failure).} \\
314	\end{tabular}}
315	\end{table}
316	
317	\paragraph{Interpretation.}
318	The equivalence arises because the generation-0$\to$1 entropy drop is large ($|\Delta x| > 0.7$ for $\alpha{=}0.50$, $> 1.0$ for $\alpha{=}0.75$) relative to the null-control variability ($\sigma_0 \approx 0.03$).
319	Any detector with a near-zero or small threshold triggers at generation~1; CUSUM's cumulative memory provides no advantage when the initial shift already exceeds the control limit.
320	This result extends Claim~3 (method sensitivity) beyond lead-lag detection to the monitoring domain: even a sequential testing procedure with stronger theoretical properties (optimal expected detection delay under continuous monitoring) does not improve over a calibrated baseline when the initial contamination signal dominates the allowance parameter.
321	The contribution of the null-calibrated monitoring framework is the calibration procedure itself (setting alarm boundaries from $\alpha{=}0.0$ data to guarantee FAR${=}$0\%), not the CUSUM algorithm.
322	
323	\section{Background and Notation}
324	\label{app:background}
325	\label{sec:background}
326	
327	This section establishes the formal setup and notation used throughout the paper.
328	
329	\paragraph{Iterative training loop.}
330	Let $M_0$ denote a pretrained language model and $\mathcal{D}_\text{real}$ a fixed corpus of human-written text.
331	At each generation $t \geq 1$, the model $M_{t-1}$ generates a synthetic corpus $\mathcal{D}_\text{synth}^{(t-1)}$, and the next-generation model $M_t$ is fine-tuned on a mixture of $\alpha$ fraction synthetic data and $(1{-}\alpha)$ fraction real data:
332	\begin{equation}
333	    \mathcal{D}_\text{train}^{(t)} = \alpha \cdot \mathcal{D}_\text{synth}^{(t-1)} \;+\; (1{-}\alpha) \cdot \mathcal{D}_\text{real}, \quad \alpha \in [0, 1].
334	    \label{eq:mixing}
335	\end{equation}
336	At $\alpha{=}1.0$, this reduces to the full-replacement paradigm of \citet{shumailov2024curse}.
337	
338	\paragraph{Metric families.}
339	\emph{Canary metrics}: token entropy ($H(p_\theta | \text{context})$ on held-out samples) and expected calibration error (ECE).
340	\emph{Downstream metrics}: distinct-$n$ ($n \in \{1, 2, 3\}$)~\cite{li2016diversity} and perplexity.
341	Each metric produces a time series of $T{+}1$ observations.
342	
343	\paragraph{Lead-lag testing.}
344	Given canary series $X$ and downstream series $Y$, the central question is whether changes in $X$ temporally precede changes in $Y$, requiring directionality and confounder control beyond simple correlation.
345	We employ five methods spanning permissive to conservative: naive cross-correlation, differenced cross-correlation, threshold onset detection, permutation Granger causality~\cite{shojaie2022granger}, and Toda--Yamamoto Granger causality~\cite{toda1995statistical}.
346	
347	\section{Methodological Comparison Table}
348	\label{app:method_comparison}
349	
350	Table~\ref{tab:method-comparison} summarizes the methodological coverage of existing canary and monitoring analyses across the diagnostic dimensions identified in \S\ref{sec:method}.
351	No prior work combines all six dimensions.
352	
353	\begin{table}[h]
354	\centering
355	\small
356	\caption{Methodological comparison of canary and monitoring analyses. \checkmark\ = present, $\times$ = absent, $\circ$ = partial (${\leq}2$ levels or limited replication). Diff.\ = differencing/stationarity controls. Multi-M.\ = ${\geq}2$ independent statistical methods. MTC = multiple testing correction. Regime = systematic variation of $\alpha$. Seeds = ${\geq}3$ independent seeds. Arch.\ = ${\geq}2$ architecturally distinct model families.}
357	\label{tab:method-comparison}
358	\resizebox{\columnwidth}{!}{%
359	\begin{tabular}{lccccccl}
360	\toprule
361	Work & Diff. & Multi-M. & MTC & Regime & Seeds & Arch. & Metrics \\
362	\midrule
363	\citet{shumailov2024curse}     & $\times$   & $\times$   & $\times$   & $\circ$    & \checkmark & \checkmark & PPL \\
364	\citet{du2025scales}           & $\times$   & $\times$   & \checkmark & \checkmark & \checkmark & $\times$   & ECE, Acc, Dist-$n$ \\
365	\citet{gambetta2024surplexity} & $\times$   & $\times$   & $\times$   & \checkmark & \checkmark & \checkmark & Surplexity, Ent \\
366	SIGMA~\cite{sigma2026spectral} & $\times$   & $\times$   & $\times$   & $\times$   & $\times$   & $\times$   & Spectral \\
367	DCES~\cite{dces2026counter}    & $\times$   & $\times$   & $\times$   & $\times$   & $\times$   & \checkmark & ECE, Ent, PPL \\
368	\midrule
369	\textbf{Ours}                  & \checkmark & \checkmark & \checkmark & \checkmark & \checkmark & \checkmark & Ent, ECE, PPL, Dist-$n$ \\
370	\bottomrule
371	\end{tabular}%
372	}
373	\end{table}
374	
375	\section{Extended Discussion}
376	\label{app:extended_discussion}
377	
378	\paragraph{Calibration scope and generalization.}
379	All FPR and FNR calibration results are specific to our experimental setup: Pythia-410M, WikiText-103 subset, $T{=}10$, and six contamination levels.
380	Cross-architecture validation across 15 confirmed conditions spanning six model families confirms that the entropy-leads-diversity pattern generalizes: PermG forward significance reaches ${\geq}6/8$ in 13 of 15 architecture-seed combinations (Table~\ref{tab:generalization}); SmolLM3-3B (3/8) diverges due to canary metric splitting.
381	
382	\paragraph{Domain-dependent directionality.}
383	The unidirectional forward causation observed on WikiText (PermG reverse${=}$0/8 across all conditions) does not hold universally.
384	On C4 at $\alpha{=}0.50$ (s42 fp32), PermG reverse reaches 7/8, indicating near-symmetric bidirectional coupling; however, this is seed-dependent (s43: 1/8) and noted as preliminary.
385	The practical implication is that directional asymmetry should be verified per domain.
386	
387	\paragraph{Token entropy versus perplexity.}
388	The distinction lies in the evaluation domain: token entropy is $H(p_\theta | \text{context})$ on held-out real data, while perplexity is $\exp(H_\text{cross})$ on model-generated text.
389	First-differencing removes their shared downward trend: the canary$\to$diversity channel survives because entropy leads diversity by one generation, whereas the canary$\to$perplexity channel vanishes because both co-move synchronously.
390	
391	\paragraph{NLP-specific constraints.}
392	Our application of Granger-type methods faces constraints absent in econometrics: (i)~observation length ($T{=}5$--$20$ vs.\ $T{=}100$--$1000$); (ii)~non-stationarity by design rather than incidental; (iii)~small multiplicity for FDR correction (8--32 pairs per regime).
393	Transfer entropy (0/192 FDR-significant results) confirms that method sensitivity extends beyond the five-method panel.
394	
395	\paragraph{Prevention paradox.}
396	Effective intervention truncates the collapse trajectory that established Granger precedence.
397	Differenced cross-correlation retains significance under intervention (31/32 pairs), while threshold onset fails entirely (0/8), reinforcing the multi-method rationale.
398	
399	\paragraph{Canary metric choice.}
400	SmolLM3-3B reveals that canary metric selection constitutes a sensitivity dimension beyond the five statistical methods: token entropy exhibits non-monotonic oscillations (0/4 significant pairs), while ECE maintains monotonic growth (3/4 pairs).
401	No single canary metric is universally optimal.
402	
403	\paragraph{Future work.}
404	Extensions include multivariate VAR models for confounder testing, multi-seed replication across all six architecture families, longer training runs ($T{\geq}20$), online monitoring within training pipelines, and accumulate-mode experiments~\cite{dey2024breaking}.
405	The sigmoid onset boundary ($\alpha_c{=}0.476$) invites connection to the critical mixture ratio scaling law of \citet{gu2024cmr} and the data-mixing phase transitions of \citet{gu2025datamixing}.
406	
407	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "040f7cfb-8c1b-4e00-bc3f-3d54fdba220a",
  "isSidechain": true,
  "promptId": "2667bad6-65ed-4e74-8e43-0c340597a9b8",
  "agentId": "a338a02a4cec945c1",
  "type": "user",
  "uuid": "c3eea91f-67d8-4006-8c85-1a18ca0bfeda",
  "sourceToolAssistantUUID": "040f7cfb-8c1b-4e00-bc3f-3d54fdba220a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "8c4ca842-c198-44f4-8734-f3be30b2ad4c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-20T13:21:16.182Z_

<details><summary>↩ Tool result · `toolu_01Bndrn9tRRi2KcKyUXD22NN`</summary>

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
11	Yet a fundamental question remains unanswered: \emph{at what contamination level does causal detection of collapse become possible?}
12	Whether a candidate canary genuinely \emph{precedes} downstream degradation or merely correlates with it under shared non-stationary trends depends on contamination regime and statistical method in ways that existing analyses leave unresolved.
13	Iterative training produces short, noisy time series (often fewer than 15 points per generation sequence), where detection power drops sharply and false positive rates can be high~\cite{boettiger2012limits}.
14	
15	We identify four deficiencies in existing lead-lag analyses of iterative training collapse.
16	(1)~No differencing tests rule out spurious regression from shared non-stationary trends~\cite{granger1974spurious}.
17	(2)~Conclusions rest on a single statistical method whose assumptions about stationarity and directionality are rarely examined.
18	(3)~No FDR correction guards against spurious findings when testing many metric pairs simultaneously.
19	(4)~No regime-dependent analysis is performed, despite the possibility that the same test yields opposite conclusions at different contamination levels.
20	
21	We discover a \emph{detection phase transition} in canary-based monitoring of iterative collapse.
22	Using Pythia-410M~\cite{biderman2023pythia} across thirteen contamination levels ($\alpha \in \{0.00, 0.05, 0.10, 0.25, 0.30, 0.35, 0.40, 0.45, 0.50, 0.55, 0.60, 0.75, 1.00\}$) and up to four random seeds, we show that causal detectability undergoes a steep onset at per-generation mixing ratio $\alpha_c{=}0.476$ at $T{=}10$ generations (sigmoid $R^2{=}0.969$, $\Delta\alpha{\approx}0.02$): permutation Granger causality (PermG) jumps from 0/8 FDR-significant metric pairs at $\alpha{\leq}0.45$ to 6/8 at $\alpha{=}0.50$.
23	A signal-times-resolution ($S \times R$) framework explains this onset and the non-monotonic dose-response through competing signal strength and temporal resolution.
24	A multi-method consensus framework (MMCT) comparing five statistical methods reveals that method choice alone can shift conclusions on the same data from universal significance to complete null.
25	Cross-architecture validation across 15 model-seed combinations spanning six families (345M--6.9B) confirms PermG detection (${\geq}6/8$) in 13 cases (87\%).
26	Granger precedence in our framework establishes temporal predictive improvement, not true causality~\cite{shojaie2022granger}; our canary claim is scoped to diversity metrics (distinct-$n$~\cite{li2016diversity}), not model collapse broadly.
27	
28	Our contributions are:
29	\begin{enumerate}
30	    \item \textbf{Detection phase transition} (\S\ref{sec:regime}).
31	    At $T{=}10$, PermG jumps from 0/8 FDR-significant pairs through $\alpha{=}0.45$ to 6/8 at $\alpha{=}0.50$ ($\alpha_c{=}0.476$, sigmoid $R^2{=}0.969$, $\Delta\alpha{\approx}0.02$), with a four-regime structure: \emph{blind}, \emph{onset}, \emph{synchronous dip}, and \emph{detection}.
32	    At $\alpha{=}0.10$, a canary blind spot emerges: diversity has already collapsed but canary metrics remain indistinguishable from the null.
33	    Cross-architecture validation across 15 model-seed combinations confirms detection in 13 cases (87\%).
34	
35	    \item \textbf{Signal-times-resolution theory} (\S\ref{sec:theory}).
36	    A power interpretation formalizes the onset as $\mathrm{Power}(\alpha, T) = \Phi(S \cdot R \cdot \sqrt{T}/\sigma)$, generating three testable predictions for $T{=}20$; sub-threshold PermG $p$-values at $\alpha{=}0.45$ ($p{=}0.059$--$0.091$) are consistent with proximity to the power boundary.
37	
38	    \item \textbf{Multi-method diagnostic toolkit} (\S\ref{sec:method}).
39	    The MMCT exposes three pitfalls: method choice alone inflates spurious-signal rates to 75\% ($\kappa{=}0.185$), first-differencing eliminates canary$\to$perplexity associations entirely while preserving all canary$\to$diversity leads (24/24$\to$24/24), and regime dependence causes the same test to shift from 5--6/8 FDR-significant pairs per seed at $\alpha{\geq}0.75$ to 0/8 at $\alpha{\leq}0.45$.
40	    PermG identifies token entropy as a one-generation-ahead canary for diversity collapse (24/24 forward, 0/24 reverse).
41	
42	    \item \textbf{Canary-based early detection} (\S\ref{sec:intervention}).
43	    Predictive cessation reduces peak perplexity by 58\% (bootstrap 95\% CI: 29--64\%) and fires one generation earlier than reactive cessation.
44	    A four-layer detection taxonomy provides regime-appropriate diagnostics from $\alpha{\geq}0.10$ to $\alpha{\geq}0.50$.
45	\end{enumerate}
46	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1e882d46-0263-4a5d-b747-4ef974af5201",
  "isSidechain": true,
  "promptId": "2667bad6-65ed-4e74-8e43-0c340597a9b8",
  "agentId": "a338a02a4cec945c1",
  "type": "user",
  "uuid": "272b0143-9d3c-4b5f-9749-b70415c45c72",
  "sourceToolAssistantUUID": "1e882d46-0263-4a5d-b747-4ef974af5201",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "8c4ca842-c198-44f4-8734-f3be30b2ad4c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-20T13:21:16.481Z_

<details open><summary>🔧 Tool call — Read · `toolu_013GdvCavTQ6m5tdYEk1hSaA`</summary>

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
  "parentUuid": "272b0143-9d3c-4b5f-9749-b70415c45c72",
  "isSidechain": true,
  "agentId": "a338a02a4cec945c1",
  "requestId": "req_011CbDtb6Va8VHvQQBrds6JL",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "a577418a-92a0-43d9-8780-c25dc2b550fe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "8c4ca842-c198-44f4-8734-f3be30b2ad4c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HM715txuCLVstHvUBP1VcL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 11995,
      "cache_read_input_tokens": 24129,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11995,
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

_source line 32 · 2026-05-20T13:21:16.489Z_

<details><summary>↩ Tool result · `toolu_013GdvCavTQ6m5tdYEk1hSaA`</summary>

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
11	Yet a fundamental question remains unanswered: \emph{at what contamination level does causal detection of collapse become possible?}
12	Whether a candidate canary genuinely \emph{precedes} downstream degradation or merely correlates with it under shared non-stationary trends depends on contamination regime and statistical method in ways that existing analyses leave unresolved.
13	Iterative training produces short, noisy time series (often fewer than 15 points per generation sequence), where detection power drops sharply and false positive rates can be high~\cite{boettiger2012limits}.
14	
15	We identify four deficiencies in existing lead-lag analyses of iterative training collapse.
16	(1)~No differencing tests rule out spurious regression from shared non-stationary trends~\cite{granger1974spurious}.
17	(2)~Conclusions rest on a single statistical method whose assumptions about stationarity and directionality are rarely examined.
18	(3)~No FDR correction guards against spurious findings when testing many metric pairs simultaneously.
19	(4)~No regime-dependent analysis is performed, despite the possibility that the same test yields opposite conclusions at different contamination levels.
20	
21	We discover a \emph{detection phase transition} in canary-based monitoring of iterative collapse.
22	Using Pythia-410M~\cite{biderman2023pythia} across thirteen contamination levels ($\alpha \in [0, 1]$, thirteen values from 0.00 to 1.00) and up to four random seeds, we show that causal detectability undergoes a steep onset at per-generation mixing ratio $\alpha_c{=}0.476$ at $T{=}10$ generations (sigmoid $R^2{=}0.969$, $\Delta\alpha{\approx}0.02$): permutation Granger causality (PermG) jumps from 0/8 FDR-significant metric pairs at $\alpha{\leq}0.45$ to 6/8 at $\alpha{=}0.50$.
23	A signal-times-resolution ($S \times R$) framework explains this onset and the non-monotonic dose-response through competing signal strength and temporal resolution.
24	A multi-method consensus framework (MMCT) comparing five statistical methods reveals that method choice alone can shift conclusions on the same data from universal significance to complete null.
25	Cross-architecture validation across 15 model-seed combinations spanning six families (345M--6.9B) confirms PermG detection (${\geq}6/8$) in 13 cases (87\%).
26	Granger precedence in our framework establishes temporal predictive improvement, not true causality~\cite{shojaie2022granger}; our canary claim is scoped to diversity metrics (distinct-$n$~\cite{li2016diversity}), not model collapse broadly.
27	
28	Our contributions are:
29	\begin{enumerate}
30	    \item \textbf{Detection phase transition} (\S\ref{sec:regime}).
31	    At $T{=}10$, PermG jumps from 0/8 FDR-significant pairs through $\alpha{=}0.45$ to 6/8 at $\alpha{=}0.50$ ($\alpha_c{=}0.476$, sigmoid $R^2{=}0.969$, $\Delta\alpha{\approx}0.02$), with a four-regime structure: \emph{blind}, \emph{onset}, \emph{synchronous dip}, and \emph{detection}.
32	    At $\alpha{=}0.10$, a canary blind spot emerges: diversity has already collapsed but canary metrics remain indistinguishable from the null.
33	    Cross-architecture validation across 15 model-seed combinations confirms detection in 13 cases (87\%).
34	
35	    \item \textbf{Signal-times-resolution theory} (\S\ref{sec:theory}).
36	    A power interpretation formalizes the onset as $\mathrm{Power}(\alpha, T) = \Phi(S \cdot R \cdot \sqrt{T}/\sigma)$, generating three testable predictions for $T{=}20$; sub-threshold PermG $p$-values at $\alpha{=}0.45$ ($p{=}0.059$--$0.091$) are consistent with proximity to the power boundary.
37	
38	    \item \textbf{Multi-method diagnostic toolkit} (\S\ref{sec:method}).
39	    The MMCT exposes three pitfalls: naive cross-correlation has 75\% null-control FPR ($\kappa{=}0.185$ inter-method), first-differencing eliminates canary$\to$perplexity associations entirely while preserving all canary$\to$diversity leads (24/24$\to$24/24), and regime dependence causes the same test to shift from 5--6/8 FDR-significant pairs per seed at $\alpha{\geq}0.75$ to 0/8 at $\alpha{\leq}0.45$.
40	    PermG identifies token entropy as a one-generation-ahead canary for diversity collapse (24/24 forward, 0/24 reverse).
41	
42	    \item \textbf{Canary-based early detection} (\S\ref{sec:intervention}).
43	    Predictive cessation reduces peak perplexity by 58\% (bootstrap 95\% CI: 29--64\%) and fires one generation earlier than reactive cessation.
44	    A four-layer detection taxonomy provides regime-appropriate diagnostics from $\alpha{\geq}0.10$ to $\alpha{\geq}0.50$.
45	\end{enumerate}
46	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a577418a-92a0-43d9-8780-c25dc2b550fe",
  "isSidechain": true,
  "promptId": "2667bad6-65ed-4e74-8e43-0c340597a9b8",
  "agentId": "a338a02a4cec945c1",
  "type": "user",
  "uuid": "07dd4d5b-b4f3-4bd8-9162-07760dd49e9a",
  "sourceToolAssistantUUID": "a577418a-92a0-43d9-8780-c25dc2b550fe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "8c4ca842-c198-44f4-8734-f3be30b2ad4c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 33 · 2026-05-20T13:21:18.992Z_

Now let me read the remaining .tex files (experiments_reframe.tex, ethics.tex, conclusion.tex, abstract.tex, main.tex) and check for any other files:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "07dd4d5b-b4f3-4bd8-9162-07760dd49e9a",
  "isSidechain": true,
  "agentId": "a338a02a4cec945c1",
  "requestId": "req_011CbDtbMzEMgifYZdwqKq45",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "b829589b-6f42-4589-b985-9c68a7f54a6d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "8c4ca842-c198-44f4-8734-f3be30b2ad4c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01H7HmQq5UTAmmRBqLY9A1dc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 18009,
      "cache_read_input_tokens": 36124,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18009,
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

_source line 34 · 2026-05-20T13:21:19.636Z_

<details open><summary>🔧 Tool call — Read · `toolu_0177PbpPN5PJ7nUKBRgGpgUt`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments_reframe.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b829589b-6f42-4589-b985-9c68a7f54a6d",
  "isSidechain": true,
  "agentId": "a338a02a4cec945c1",
  "requestId": "req_011CbDtbMzEMgifYZdwqKq45",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d776b140-13af-49ec-afdd-1850608b0286",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "8c4ca842-c198-44f4-8734-f3be30b2ad4c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01H7HmQq5UTAmmRBqLY9A1dc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 18009,
      "cache_read_input_tokens": 36124,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18009,
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

_source line 35 · 2026-05-20T13:21:19.649Z_

<details><summary>↩ Tool result · `toolu_0177PbpPN5PJ7nUKBRgGpgUt`</summary>

```text
1	\subsection{Detection Phase Transition}
2	\label{sec:regime}
3	
4	Diversity collapse occurs at every contamination level: distinct-1 declines by $14.1\%$ at $\alpha{=}0.0$ (fine-tuning drift) and by $40.3{\pm}0.3\%$ at $\alpha{=}0.25$ (3-seed mean).
5	Despite this ubiquitous degradation, causal detectability is sharply regime-dependent.
6	Permutation Granger (PermG) tests find 0/8 canary$\to$downstream pairs FDR-significant from $\alpha{=}0.00$ through $\alpha{=}0.45$, then jump to 6/8 at $\alpha{=}0.50$ (2~fp32 seeds, consistent).
7	This transition is striking because cumulative synthetic fraction barely changes across the boundary: $C = 1{-}(1{-}\alpha)^{10}$ yields $99.75\%$ at $\alpha{=}0.45$ versus $99.90\%$ at $\alpha{=}0.50$, a difference of 0.15 percentage points, yet detection jumps from null to reliable.
8	Sigmoid regression across the 13-point $\alpha$ grid quantifies this steep onset: $\alpha_c = 0.476$ at $T{=}10$, steepness $k \geq 200$, transition width $\Delta\alpha \approx 0.02$, $R^2 = 0.969$ (versus power-law $R^2 = 0.808$, $\Delta\mathrm{AIC} = 18.2$; Figure~\ref{fig:phase_transition}).
9	At $\alpha{=}0.45$, PermG $p$-values reveal sub-threshold signal ($p_{\mathrm{fdr}} = 0.059$ for seed~43, $0.091$ for seed~42), consistent with the power-threshold interpretation of $\alpha_c$ at $T{=}10$ (\S\ref{sec:theory}): the onset reflects PermG's power curve crossing the detection floor, not the emergence of a new physical signal.
10	A specification curve analysis spanning 1{,}160 analytical specifications confirms that the detection phase transition is specification-invariant.
11	
12	First-differencing scopes the canary claim precisely.
13	Canary$\to$diversity pairs retain unanimous FDR significance after first-differencing ($24/24 \to 24/24$ across 4~seeds at $\alpha{=}1.0$), while canary$\to$perplexity collapses entirely ($F \approx 0$, $p = 0.99$): the apparent perplexity association is a shared-trend artifact.
14	All canary claims are therefore scoped to diversity metrics only.
15	At $\alpha{=}1.0$, 24/24 forward-direction pairs reach FDR significance with 0/24 reverse (4~seeds); directional asymmetry is robust across all WikiText conditions.
16	The canary mechanism also exhibits a blind spot: at $\alpha{=}0.10$, distinct-1 has already dropped by $39.6\%$, yet token entropy is indistinguishable from the null ($-5.3\%$ versus $-4.6{\pm}0.4\%$ at $\alpha{=}0.0$).
17	Below $\alpha_c$ at $T{=}10$, diversity collapse proceeds without any detectable causal signal in the canary metrics.
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
30	The PermG dose-response profile (Figure~\ref{fig:regime_map}) reveals four detection regimes: \emph{blind} ($\alpha \leq 0.45$, 0/8 FDR-significant pairs), \emph{onset} ($\alpha \approx 0.50$, 6/8), \emph{synchronous dip} ($\alpha \approx 0.60$, 0/8 both seeds; dual-seed confirmed), and \emph{detection} ($\alpha \geq 0.75$, 5--6/8 per seed across 3~seeds; $\alpha{=}1.0$, 6/8 across 4~seeds).
31	The non-monotonic dip at $\alpha{=}0.60$ is consistent with the $S \times R$ framework (\S\ref{sec:theory}): signal strength $S(\alpha)$ rises monotonically with contamination, but temporal resolution $R(\alpha)$ drops when relaxation time approaches the observation interval.
32	At $\alpha \approx 0.60$, this compression drives the canary-to-downstream lag toward zero, and the product $S \times R$ reaches a local minimum.
33	The synchronous zone is mechanistically distinct from the blind spot: in the blind zone, canary drift is indistinguishable from the null; in the synchronous zone, both canary and downstream metrics drift substantially but without temporal offset.
34	
35	Method choice is itself a major source of analytic variability.
36	At $\alpha{=}1.0$, forward-direction significance rates range from 100\% (naive cross-correlation) to 37.5\% (PermG), with inter-method $\kappa = 0.185$ (near chance) and a spurious rate of at least 62.5\%.
37	PermG is the only method that combines zero null-control FPR with consistent detection at $\alpha \geq 0.50$ (Table~\ref{tab:method_comparison}); its nonparametric null distribution, built-in directionality, and hyperparameter-free design explain this advantage.
38	The $S \times R$ framework generates three testable predictions for $T{=}20$ via $\mathrm{Power}(\alpha, T) = \Phi(S \cdot R \cdot \sqrt{T}/\sigma)$: (i)~$\alpha_c$ at $T{=}10$ should left-shift, (ii)~the transition should smooth, and (iii)~different methods should exhibit different $\alpha_c$ values.
39	These predictions are under empirical verification.
40	
41	\begin{figure}[t]
42	\centering
43	\includegraphics[width=\linewidth]{figures/fig_dose_response.pdf}
44	\caption{PermG forward detection rate across 13 contamination levels (Pythia-410M, fp32, direction-checked). Four regimes: blind ($\alpha \leq 0.45$, 0/8), onset ($\alpha{=}0.50$, 6/8), synchronous dip ($\alpha{=}0.60$, 0/8), and detection ($\alpha \geq 0.75$, 5--6/8).}
45	\label{fig:regime_map}
46	\end{figure}
47	
48	\begin{table}[t]
49	\centering
50	\small
51	\caption{Forward-direction FDR significance rates (\%) across contamination levels (Pythia-410M, seed~42, fp32, direction-checked). Each cell: fraction of 8 validated pairs at BH-corrected significance ($q{=}0.05$). PermG achieves zero null-control FPR with consistent detection at $\alpha \geq 0.50$.}
52	\label{tab:method_comparison}
53	\begin{tabular}{lcccccc}
54	\toprule
55	Method & $\alpha{=}0.0$ & $\alpha{=}0.25$ & $\alpha{=}0.50$ & $\alpha{=}0.75$ & $\alpha{=}1.0$ & FPR$_\text{null}$ \\
56	\midrule
57	Naive XCorr          & 75   & 12.5 & 37.5 & 87.5 & 0    & 75  \\
58	Diff.\ XCorr         & 0    & 37.5 & 87.5 & 75   & 75   & 0   \\
59	Threshold ($3\sigma$) & ---  & 0    & 50   & 0    & 0    & --- \\
60	Perm.\ Granger       & 0    & 0    & 75   & 75   & 75   & 0   \\
61	Toda--Yamamoto       & ---  & 0    & 37.5 & 37.5 & 50   & --- \\
62	\bottomrule
63	\end{tabular}
64	\end{table}
65	
66	
67	\subsection{Cross-Architecture Generalization}
68	\label{sec:generalization}
69	
70	We evaluate the detection phase transition across 15 model-seed combinations spanning six families (Pythia, GPT-2, OPT, Qwen, SmolLM3, Padding-variant), scales from 345M to 6.9B parameters, and two training domains (WikiText-103, C4).
71	Table~\ref{tab:generalization} reports PermG forward detection at $\alpha{=}1.0$.
72	PermG forward significance reaches ${\geq}$6/8 in 13 of 15 conditions (87\%).
73	Two exceptions emerge: Pythia-1.4B seed~42 on WikiText (2/8), a seed-dependent outlier that recovers to 6/8 in seed~43, and SmolLM3-3B (3/8), where only ECE$\to$downstream pairs reach significance while entropy$\to$downstream pairs fail entirely (0/4; details in Appendix).
74	SmolLM3's token entropy exhibits non-monotonic oscillations across generations; this pattern violates the monotonic decline that Granger tests require.
75	The onset boundary $\alpha_c \approx 0.50$ at $T{=}10$ is architecture-independent: every family that achieves detection does so at or above this threshold, and none achieves reliable detection below it.
76	
77	Replacing WikiText-103 with C4 yields the strongest detection observed: Pythia-1B reaches PermG~fwd 8/8 (2~seeds), and Pythia-1.4B reaches 8/8 on C4 versus 2/8 on WikiText at the same scale.
78	At Pythia-6.9B (bf16), detection recovers to 7/8 on WikiText.
79	Dataset characteristics modulate detection power independently of model capacity.
80	Directional asymmetry also varies by domain: at $\alpha{=}0.50$ on C4, PermG reverse reaches 7/8, compared to 0/24 across all WikiText conditions.
81	This domain-dependent bidirectionality suggests that the unidirectional forward causation observed on WikiText may partly reflect domain-specific dynamics (\S\ref{sec:discussion}).
82	
83	\begin{table}[t]
84	\centering
85	\small
86	\caption{Cross-architecture PermG forward detection ($\alpha{=}1.0$). Detection (${\geq}$6/8) confirmed in 13/15 conditions (87\%) across six model families, scales from 345M to 6.9B, and two domains.}
87	\label{tab:generalization}
88	\begin{tabular}{lrcl}
89	\toprule
90	Model & Params & Domain & PermG fwd \\
91	\midrule
92	Pythia-410M    & 410M & Wiki & 6/8 \\
93	Pythia-1.4B    & 1.4B & Wiki & 2--6/8$^\dagger$ \\
94	Pythia-6.9B    & 6.9B & Wiki & 7/8$^*$ \\
95	GPT-2-medium   & 345M & Wiki & 6/8 \\
96	OPT-1.3B       & 1.3B & Wiki & 6/8 \\
97	Qwen3.5-0.8B   & 0.8B & Wiki & 8/8 \\
98	SmolLM3-3B     & 3.0B & Wiki & 3/8$^\ddagger$ \\
99	Padding-410M   & 410M & Wiki & 6/8 \\
100	\addlinespace
101	Pythia-1B      & 1.0B & C4   & 7--8/8 \\
102	Pythia-1.4B    & 1.4B & C4   & 8/8 \\
103	\bottomrule
104	\multicolumn{4}{l}{\footnotesize $^\dagger$Seed-dependent (s42: 2/8, s43: 6/8).} \\
105	\multicolumn{4}{l}{\footnotesize $^*$bf16 (exceeds single-GPU fp32 capacity).} \\
106	\multicolumn{4}{l}{\footnotesize $^\ddagger$ECE-only canary (entropy 0/4).} \\
107	\multicolumn{4}{l}{\footnotesize Multi-seed (range shown): Pythia-410M, -1.4B Wiki,} \\
108	\multicolumn{4}{l}{\footnotesize GPT-2-med, OPT-1.3B, Pythia-1B C4 (2 seeds each).} \\
109	\multicolumn{4}{l}{\footnotesize Others: single seed. Total: 15 combinations.} \\
110	\end{tabular}
111	\end{table}
112	
113	
114	\subsection{Canary-Based Early Intervention}
115	\label{sec:intervention}
116	
117	We implement a predictive cessation protocol: training with synthetic data ($\alpha{=}1.0$) continues until token entropy drops ${>}15\%$ relative to generation~0, at which point $\alpha$ switches to $0.0$ (pure real data).
118	A reactive baseline triggers when distinct-1 drops ${>}10\%$.
119	The predictive trigger fires at generation~1 in both Pythia-410M and Pythia-1.4B (s42 fp32), one generation before the reactive baseline (generation~2).
120	Peak perplexity under predictive intervention is $56.99$ versus $157.09$ under reactive (s42 fp32), a 58\% reduction (bootstrap 95\% CI: 29--64\%).
121	Recovery occurs at generation~2 under predictive cessation versus generation~4 under reactive.
122	Both models converge to the $\alpha{=}0.0$ baseline by generation~10.
123	
124	The trigger generation, recovery timeline, and convergence behavior are identical across the $3.4\times$ scale gap from 410M to 1.4B, and the 15\% entropy threshold generalizes without recalibration.
125	These results position canary-based detection within a four-layer taxonomy of collapse monitoring: (1)~dimensionality collapse, detectable at $\alpha \geq 0.10$ via $n$-gram diversity decline; (2)~distributional variance, detectable at $\alpha \geq 0.25$ via calibration drift; (3)~causal coupling, detectable at $\alpha \geq 0.50$ via Granger precedence; and (4)~dynamical stability, assessable at $\alpha \geq 0.50$ via lag structure.
126	Each layer captures a distinct aspect of collapse, and lower layers activate at lower contamination thresholds.
127	The practical implication is that canary monitoring should combine multiple detection layers rather than rely on any single statistical test.
128	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d776b140-13af-49ec-afdd-1850608b0286",
  "isSidechain": true,
  "promptId": "2667bad6-65ed-4e74-8e43-0c340597a9b8",
  "agentId": "a338a02a4cec945c1",
  "type": "user",
  "uuid": "07540575-0d2a-4e56-8051-95e7aa6a551b",
  "sourceToolAssistantUUID": "d776b140-13af-49ec-afdd-1850608b0286",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "8c4ca842-c198-44f4-8734-f3be30b2ad4c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-20T13:21:20.061Z_

<details open><summary>🔧 Tool call — Read · `toolu_01YF7TVbwho9o3ET2ZGXqwZn`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/ethics.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "07540575-0d2a-4e56-8051-95e7aa6a551b",
  "isSidechain": true,
  "agentId": "a338a02a4cec945c1",
  "requestId": "req_011CbDtbMzEMgifYZdwqKq45",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "1d5a6aa0-53a1-4024-ac9d-fb8bf5f21ef7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "8c4ca842-c198-44f4-8734-f3be30b2ad4c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01H7HmQq5UTAmmRBqLY9A1dc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 18009,
      "cache_read_input_tokens": 36124,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18009,
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

_source line 37 · 2026-05-20T13:21:20.074Z_

<details><summary>↩ Tool result · `toolu_01YF7TVbwho9o3ET2ZGXqwZn`</summary>

```text
1	\section*{Ethics Statement and AI Writing Disclosure}
2	
3	\paragraph{AI writing assistance.}
4	This paper was drafted with assistance from Claude (Anthropic), used for LaTeX formatting, literature search, and iterative revision.
5	All scientific claims, experimental design decisions, data analysis, and interpretations are the sole responsibility of the authors.
6	The AI assistant did not design experiments, run code, or make editorial judgments about which results to include or exclude.
7	
8	\paragraph{Responsible NLP considerations.}
9	This work studies degradation in iterative language model training.
10	We do not release models trained on synthetic data, as they exhibit reduced diversity and calibration.
11	Our findings highlight a failure mode relevant to the responsible deployment of language models: unmonitored iterative training on web-crawled data (which increasingly contains LLM outputs) may degrade model quality in ways detectable only through the multi-method framework we propose.
12	We encourage practitioners to implement canary monitoring in production training pipelines as a safeguard against silent quality degradation.
13	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1d5a6aa0-53a1-4024-ac9d-fb8bf5f21ef7",
  "isSidechain": true,
  "promptId": "2667bad6-65ed-4e74-8e43-0c340597a9b8",
  "agentId": "a338a02a4cec945c1",
  "type": "user",
  "uuid": "78218bb1-5159-4b81-829a-8207a8fede84",
  "sourceToolAssistantUUID": "1d5a6aa0-53a1-4024-ac9d-fb8bf5f21ef7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "8c4ca842-c198-44f4-8734-f3be30b2ad4c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-20T13:21:20.264Z_

<details open><summary>🔧 Tool call — Read · `toolu_01ChemqbU2APiz3qaZvfx1a1`</summary>

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
  "parentUuid": "78218bb1-5159-4b81-829a-8207a8fede84",
  "isSidechain": true,
  "agentId": "a338a02a4cec945c1",
  "requestId": "req_011CbDtbMzEMgifYZdwqKq45",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "59759178-ea27-4e39-9a83-835523f96438",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "8c4ca842-c198-44f4-8734-f3be30b2ad4c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01H7HmQq5UTAmmRBqLY9A1dc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 18009,
      "cache_read_input_tokens": 36124,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18009,
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

_source line 39 · 2026-05-20T13:21:20.270Z_

<details><summary>↩ Tool result · `toolu_01ChemqbU2APiz3qaZvfx1a1`</summary>

```text
1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	Lead-lag analysis in iterative training collapse is far more fragile than the current literature assumes.
5	Method choice alone inflates spurious-signal rates to at least 62.5\%, first-differencing exposes canary$\to$perplexity associations as entirely spurious, and regime dependence causes the same Granger test to shift from 24/24 to 0/8 significant pairs across contamination levels.
6	These pitfalls establish that single-method, single-regime analyses (the current default) cannot reliably distinguish genuine temporal precedence from statistical artifacts.
7	
8	Our systematic five-method comparison through the Multi-Method Consensus Test (MMCT) identifies permutation Granger causality as the recommended detection method: it is the only one combining zero null-control FPR with high sensitivity, exhibiting a clean step-function dose-response from 0/8 (blind spot, $\alpha{\leq}0.45$) to 6/8 (onset, $\alpha{=}0.50$) with reliable detection at $\alpha{\geq}0.75$.
9	The other four methods each fail in characteristic ways: naive cross-correlation inflates FPR to 75\%, differenced cross-correlation cannot separate forward from reverse precedence, threshold onset is power-limited at $T{=}10$ under $3\sigma$ calibration, and Toda--Yamamoto Granger achieves moderate detection (3--4/8 at $\alpha{\geq}0.50$) as a supplementary method.
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
  "parentUuid": "59759178-ea27-4e39-9a83-835523f96438",
  "isSidechain": true,
  "promptId": "2667bad6-65ed-4e74-8e43-0c340597a9b8",
  "agentId": "a338a02a4cec945c1",
  "type": "user",
  "uuid": "0658478d-1e2e-4d2e-80c1-b58cb4a2971c",
  "sourceToolAssistantUUID": "59759178-ea27-4e39-9a83-835523f96438",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "8c4ca842-c198-44f4-8734-f3be30b2ad4c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-20T13:21:20.478Z_

<details open><summary>🔧 Tool call — Read · `toolu_01QH7GRmN51h6GcuVVZksuRj`</summary>

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
  "parentUuid": "0658478d-1e2e-4d2e-80c1-b58cb4a2971c",
  "isSidechain": true,
  "agentId": "a338a02a4cec945c1",
  "requestId": "req_011CbDtbMzEMgifYZdwqKq45",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "6297de70-7069-481d-a700-c9b5bd1ac82f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "8c4ca842-c198-44f4-8734-f3be30b2ad4c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01H7HmQq5UTAmmRBqLY9A1dc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 18009,
      "cache_read_input_tokens": 36124,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18009,
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

_source line 41 · 2026-05-20T13:21:20.482Z_

<details><summary>↩ Tool result · `toolu_01QH7GRmN51h6GcuVVZksuRj`</summary>

```text
1	\begin{abstract}
2	In iterative training on synthetic data, causal detection of collapse does not track cumulative contamination: at 99.75\% total synthetic exposure, no canary-downstream metric pair shows significant Granger precedence (0/8); at 99.90\%---a mere 0.15 percentage points more---detection jumps to 6/8 (dual-seed confirmed).
3	This \emph{detection phase transition} at $T{=}10$ (sigmoid $R^2{=}0.969$, $\alpha_c{=}0.476$, $\Delta\alpha{\approx}0.02$; transition steepness predicted T-dependent by the statistical power interpretation below) reveals that detectability is governed by per-generation mixing ratio, not cumulative contamination, and establishes a four-regime dose-response: blind ($\alpha{\leq}0.45$), onset ($\alpha{\approx}0.50$), synchronous dip ($\alpha{\approx}0.60$), and detection ($\alpha{\geq}0.75$).
4	A signal-times-resolution ($S \times R$) framework explains the non-monotonic pattern---signal strength rises monotonically but temporal resolution drops when relaxation time matches the observation interval---and a statistical power interpretation predicts three testable consequences for longer chains ($T{=}20$): left-shift of $\alpha_c$, transition smoothing, and method-dependent thresholds.
5	The discovery is enabled by a multi-method consensus framework (MMCT) comparing five statistical methods, which reveals that method choice alone inflates spurious-signal rates to 75\% and first-differencing eliminates all canary$\to$perplexity associations while preserving canary$\to$diversity leads (24/24$\to$24/24).
6	Permutation Granger causality (PermG) is the only method combining zero null-control FPR with high sensitivity; applied to Pythia-410M and validated across 15 model-seed combinations spanning six families (345M--6.9B), it identifies token entropy as a one-generation-ahead canary for diversity collapse (24/24 forward, 0/24 reverse at $\alpha{=}1.0$).
7	Canary-based predictive cessation reduces peak perplexity by 58\% compared to reactive cessation.
8	\end{abstract}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6297de70-7069-481d-a700-c9b5bd1ac82f",
  "isSidechain": true,
  "promptId": "2667bad6-65ed-4e74-8e43-0c340597a9b8",
  "agentId": "a338a02a4cec945c1",
  "type": "user",
  "uuid": "0df58636-8dbc-4c90-849f-e7724f425e38",
  "sourceToolAssistantUUID": "6297de70-7069-481d-a700-c9b5bd1ac82f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "8c4ca842-c198-44f4-8734-f3be30b2ad4c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-20T13:21:20.589Z_

<details open><summary>🔧 Tool call — Read · `toolu_01EsDWgRTU9FuTA2QxgpBQxt`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0df58636-8dbc-4c90-849f-e7724f425e38",
  "isSidechain": true,
  "agentId": "a338a02a4cec945c1",
  "requestId": "req_011CbDtbMzEMgifYZdwqKq45",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "e96c6c34-e78c-49fc-ac1e-0fe7f51c71fb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "8c4ca842-c198-44f4-8734-f3be30b2ad4c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01H7HmQq5UTAmmRBqLY9A1dc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 18009,
      "cache_read_input_tokens": 36124,
      "output_tokens": 421,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 18009
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 421,
          "cache_read_input_tokens": 36124,
          "cache_creation_input_tokens": 18009,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 18009,
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

_source line 43 · 2026-05-20T13:21:20.593Z_

<details><summary>↩ Tool result · `toolu_01EsDWgRTU9FuTA2QxgpBQxt`</summary>

```text
1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	
4	\usepackage{times}
5	\usepackage{latexsym}
6	\usepackage[T1]{fontenc}
7	\usepackage[utf8]{inputenc}
8	\usepackage{microtype}
9	
10	\usepackage{amsmath}
11	\usepackage{amssymb}
12	\usepackage{graphicx}
13	\usepackage{booktabs}
14	\usepackage{subcaption}
15	\usepackage{algorithm}
16	\usepackage{algpseudocode}
17	
18	\title{A Detection Phase Transition in Iterative Model Collapse}
19	
20	\author{Anonymous}
21	
22	\begin{document}
23	\maketitle
24	
25	\input{abstract}
26	\input{introduction}
27	\input{related_work}
28	\input{method}
29	\input{experiments}
30	\input{discussion}
31	\input{limitations}
32	\input{ethics}
33	
34	\bibliography{references}
35	
36	\input{appendix}
37	
38	\end{document}
39	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e96c6c34-e78c-49fc-ac1e-0fe7f51c71fb",
  "isSidechain": true,
  "promptId": "2667bad6-65ed-4e74-8e43-0c340597a9b8",
  "agentId": "a338a02a4cec945c1",
  "type": "user",
  "uuid": "8aa30b00-8fa8-4b9c-8571-309c2837a3eb",
  "sourceToolAssistantUUID": "e96c6c34-e78c-49fc-ac1e-0fe7f51c71fb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "8c4ca842-c198-44f4-8734-f3be30b2ad4c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 44 · 2026-05-20T13:21:33.179Z_

Perfect! Now I have extracted all the content from all .tex files. Let me compile a comprehensive list of all unique citation keys found in the paper. Based on my thorough analysis of all .tex files, here is the complete extraction of citation keys:

## COMPLETE CITATION KEY EXTRACTION

Below are ALL unique citation keys found across ALL .tex files in `/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/`:

### Unique Citation Keys (Alphabetically Sorted):

1. **alemohammad2024mad** - Found in: introduction.tex, intro_reframe.tex, related_work.tex, related_work_reframe.tex
2. **bell2022modeling** - Found in: related_work.tex, related_work_reframe.tex, method.tex, method_reframe.tex
3. **biderman2023pythia** - Found in: experiments.tex, introduction.tex, intro_reframe.tex
4. **boettiger2012limits** - Found in: background.tex, introduction.tex, intro_reframe.tex, method.tex, method_reframe.tex, related_work.tex, related_work_reframe.tex
5. **calabrese2003hormesis** - Found in: discussion.tex
6. **coretta2023multidimensional** - Found in: related_work.tex, related_work_reframe.tex
7. **dakos2012methods** - Found in: discussion_reframe.tex
8. **dces2026counter** - Found in: appendix.tex, related_work_reframe.tex
9. **dey2024breaking** - Found in: appendix.tex, limitations.tex
10. **dohmatob2024tale** - Found in: related_work.tex
11. **dohmatob2025strong** - Found in: related_work.tex
12. **du2025scales** - Found in: appendix.tex, related_work.tex, related_work_reframe.tex
13. **du2026geometric** - Found in: appendix.tex, related_work.tex, related_work_reframe.tex
14. **gambetta2024surplexity** - Found in: appendix.tex, related_work.tex, related_work_reframe.tex
15. **granger1969investigating** - Found in: background.tex, discussion.tex, discussion_reframe.tex, method.tex, method_reframe.tex, related_work.tex, related_work_reframe.tex
16. **granger1974spurious** - Found in: background.tex, discussion.tex, discussion_reframe.tex, introduction.tex, intro_reframe.tex, method.tex, method_reframe.tex, related_work.tex, related_work_reframe.tex
17. **gu2024cmr** - Found in: appendix.tex, related_work.tex
18. **gu2025datamixing** - Found in: appendix.tex, related_work.tex
19. **kalinowski2026topology** - Found in: related_work_reframe.tex
20. **kapoor2024reforms** - Found in: related_work.tex, related_work_reframe.tex
21. **li2016diversity** - Found in: background.tex, experiments.tex, introduction.tex, intro_reframe.tex, limitations.tex, appendix.tex
22. **merity2017pointer** - Found in: experiments.tex
23. **schaeffer2025position** - Found in: limitations.tex
24. **scheffer2009early** - Found in: background.tex, experiments.tex, introduction.tex, intro_reframe.tex, method.tex, method_reframe.tex, related_work.tex, related_work_reframe.tex
25. **scheffer2012anticipating** - Found in: introduction.tex, intro_reframe.tex
26. **shojaie2022granger** - Found in: background.tex, discussion.tex, discussion_reframe.tex, experiments.tex, method.tex, method_reframe.tex, appendix.tex
27. **sigma2026spectral** - Found in: appendix.tex, related_work_reframe.tex
28. **shumailov2024curse** - Found in: appendix.tex, background.tex, experiments.tex, introduction.tex, intro_reframe.tex, limitations.tex, related_work.tex, related_work_reframe.tex
29. **simonsohn2020specification** - Found in: method.tex, method_reframe.tex
30. **toda1995statistical** - Found in: background.tex, method.tex, method_reframe.tex, related_work.tex, related_work_reframe.tex, appendix.tex

### Total Count:
- **30 unique citation keys**
- **Distribution across files**: Most keys appear in multiple files, with core methodology and baseline papers cited frequently across sections

### Most Frequently Cited Keys:
1. **scheffer2009early** - 8 files
2. **boettiger2012limits** - 7 files
3. **granger1969investigating** - 7 files
4. **granger1974spurious** - 9 files
5. **li2016diversity** - 6 files
6. **shumailov2024curse** - 8 files

All citation keys have been extracted from the following files:
- /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/abstract.tex
- /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/introduction.tex
- /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/intro_reframe.tex
- /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/related_work.tex
- /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/related_work_reframe.tex
- /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/background.tex
- /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method.tex
- /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method_reframe.tex
- /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex
- /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments_reframe.tex
- /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/discussion.tex
- /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/discussion_reframe.tex
- /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/limitations.tex
- /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8aa30b00-8fa8-4b9c-8571-309c2837a3eb",
  "isSidechain": true,
  "agentId": "a338a02a4cec945c1",
  "requestId": "req_011CbDtbfSxoNT6g1m7BL1yb",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "5c9e4827-b821-42a7-a39a-9faa1fd58ed4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "8c4ca842-c198-44f4-8734-f3be30b2ad4c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011bXfGXnsARRY7JfBkurZ9m",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 6713,
      "cache_read_input_tokens": 54133,
      "output_tokens": 1854,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6713
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 1854,
          "cache_read_input_tokens": 54133,
          "cache_creation_input_tokens": 6713,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6713,
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
