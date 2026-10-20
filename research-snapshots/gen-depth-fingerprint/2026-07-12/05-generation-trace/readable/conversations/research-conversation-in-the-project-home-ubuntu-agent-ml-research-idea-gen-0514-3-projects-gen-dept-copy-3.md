# Research conversation: In the project /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/,

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 19
- **Recorded user turns:** 1
- **Tool calls:** 7
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a7859a4de84d0a5b2.jsonl`
- **Structured JSON:** [`4a96273c19b311c9a728.json`](../../sessions/4a/4a96273c19b311c9a728.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

19 recorded events

### User

_source line 1 · 2026-05-23T19:41:03.189Z_

In the project /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/, search all .tex files for these specific numbers and their surrounding context:

1. "0.905" or "0.90" — related to QLoRA F1
2. "0.789" — related to XGBoost 3-class F1
3. "0.487" — related to instruct LOGO binary F1
4. "3-4" or "3--4" or "±3" or "batch" or "prevalence" — related to prevalence estimation error
5. "48" or ">48" or "48×" or "48\\times" — related to variance ratio

For each match, show the file path, line number, and 3 lines of context. Search breadth: very thorough.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "5c60df84-fcb8-462d-8f59-5098b0a96974",
  "agentId": "a7859a4de84d0a5b2",
  "type": "user",
  "uuid": "7d840168-cabb-44ee-86c5-f34107e5c898",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "727cbce6-9768-410b-9211-4635321ab6fe",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-23T19:41:04.457Z_

I'll search all .tex files in the paper directory for these specific numbers and their context.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7d840168-cabb-44ee-86c5-f34107e5c898",
  "isSidechain": true,
  "agentId": "a7859a4de84d0a5b2",
  "requestId": "req_011CbL4yp1CzN3w5CMSa3FT2",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "750222f2-5e4f-4eed-af45-97b3db9e87d5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "727cbce6-9768-410b-9211-4635321ab6fe",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01RSEv5uiF8VXSEceLMvREuB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18103,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18103,
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

_source line 3 · 2026-05-23T19:41:04.875Z_

<details open><summary>🔧 Tool call — Glob · `toolu_019LPQuyQ71L2zRL8WAk3rzs`</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/**/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "750222f2-5e4f-4eed-af45-97b3db9e87d5",
  "isSidechain": true,
  "agentId": "a7859a4de84d0a5b2",
  "requestId": "req_011CbL4yp1CzN3w5CMSa3FT2",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "bafe0ef4-4298-4fd7-bbb1-1cff00f8f536",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "727cbce6-9768-410b-9211-4635321ab6fe",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01RSEv5uiF8VXSEceLMvREuB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18103,
      "cache_read_input_tokens": 0,
      "output_tokens": 108,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 18103
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 108,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 18103,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 18103,
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

_source line 4 · 2026-05-23T19:41:04.908Z_

<details><summary>↩ Tool result · `toolu_019LPQuyQ71L2zRL8WAk3rzs`</summary>

```text
artifacts/_project/paper/appendix_9gen_scale.tex
artifacts/_project/paper/appendix_ablation.tex
artifacts/_project/paper/appendix_classifier.tex
artifacts/_project/paper/appendix_confusion_matrix.tex
artifacts/_project/paper/appendix_cross_model_detail.tex
artifacts/_project/paper/appendix_cross_temp.tex
artifacts/_project/paper/appendix_dataset_stats.tex
artifacts/_project/paper/appendix_ddr_causality.tex
artifacts/_project/paper/appendix_decoding_strategy.tex
artifacts/_project/paper/appendix_domain.tex
artifacts/_project/paper/appendix_downstream.tex
artifacts/_project/paper/appendix_feature_candidates.tex
artifacts/_project/paper/appendix_feature_correlation.tex
artifacts/_project/paper/appendix_finer_depth.tex
artifacts/_project/paper/appendix_generator_subsets.tex
artifacts/_project/paper/appendix_human_edit.tex
artifacts/_project/paper/appendix_instruct.tex
artifacts/_project/paper/appendix_length.tex
artifacts/_project/paper/appendix_nll_distribution.tex
artifacts/_project/paper/appendix_prompt_type.tex
artifacts/_project/paper/appendix_qualitative_examples.tex
artifacts/_project/paper/appendix_seed_control.tex
artifacts/_project/paper/appendix_temperature_stability.tex
artifacts/_project/paper/appendix_tost.tex
artifacts/_project/paper/appendix_tost_bootstrap.tex
artifacts/_project/paper/ethics.tex
artifacts/_project/paper/table1.tex
artifacts/_project/paper/table2.tex
artifacts/_project/paper/appendix_variance_decomposition.tex
artifacts/_project/paper/appendix_iterative_comparison.tex
artifacts/_project/paper/related_work.tex
artifacts/_project/paper/appendix_lofo.tex
artifacts/_project/paper/appendix_qlora.tex
artifacts/_project/paper/limitations.tex
artifacts/_project/paper/appendix_transfer.tex
artifacts/_project/paper/appendix_convergence.tex
artifacts/_project/paper/appendix_feature_distributions.tex
artifacts/_project/paper/per_family_cohens_d_table.tex
artifacts/_project/paper/main.tex
artifacts/_project/paper/per_family_ddr_table.tex
artifacts/_project/paper/appendix_error_analysis.tex
artifacts/_project/paper/appendix_ddr_validation.tex
artifacts/_project/paper/results.tex
artifacts/_project/paper/table4.tex
artifacts/_project/paper/abstract.tex
artifacts/_project/paper/introduction.tex
artifacts/_project/paper/discussion.tex
artifacts/_project/paper/conclusion.tex
artifacts/_project/paper/method.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bafe0ef4-4298-4fd7-bbb1-1cff00f8f536",
  "isSidechain": true,
  "promptId": "5c60df84-fcb8-462d-8f59-5098b0a96974",
  "agentId": "a7859a4de84d0a5b2",
  "type": "user",
  "uuid": "5b8310d0-9367-49d2-a8fc-5eb34527f993",
  "sourceToolAssistantUUID": "bafe0ef4-4298-4fd7-bbb1-1cff00f8f536",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "727cbce6-9768-410b-9211-4635321ab6fe",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 5 · 2026-05-23T19:41:06.394Z_

Now I'll search each .tex file for the specific numbers and patterns. Let me start with targeted grep searches for each of the five categories:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5b8310d0-9367-49d2-a8fc-5eb34527f993",
  "isSidechain": true,
  "agentId": "a7859a4de84d0a5b2",
  "requestId": "req_011CbL4ywb7WswXcf6jjA72Y",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "c88d7ef7-a68a-4168-a689-721ff5fdb2bc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "727cbce6-9768-410b-9211-4635321ab6fe",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HSoAsfMdSgZs6iCVRTHALD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1634,
      "cache_read_input_tokens": 18103,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1634,
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

_source line 6 · 2026-05-23T19:41:07.660Z_

<details open><summary>🔧 Tool call — Grep · `toolu_017SWNFo2WU4XWZJKHvm1uSh`</summary>

```json
{
  "pattern": "0\\.90[5]?|0\\.9\\.0",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
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
  "parentUuid": "c88d7ef7-a68a-4168-a689-721ff5fdb2bc",
  "isSidechain": true,
  "agentId": "a7859a4de84d0a5b2",
  "requestId": "req_011CbL4ywb7WswXcf6jjA72Y",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "a6d70e92-d219-418b-aa14-79c5ae3edec9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "727cbce6-9768-410b-9211-4635321ab6fe",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HSoAsfMdSgZs6iCVRTHALD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1634,
      "cache_read_input_tokens": 18103,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1634,
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

_source line 7 · 2026-05-23T19:41:07.675Z_

<details><summary>↩ Tool result · `toolu_017SWNFo2WU4XWZJKHvm1uSh`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_cross_model_detail.tex-19-\end{table}
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_cross_model_detail.tex-20-
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_cross_model_detail.tex-21-\paragraph{Variance decomposition.}
artifacts/_project/paper/appendix_cross_model_detail.tex:22:A two-way ANOVA (generator $\times$ depth) on cross-model chain features ($n{=}3{,}778$, depths 1--4) confirms that generator identity contributes negligible variance: partial $\eta^2_{\text{gen}} < 1\%$ for all seven features (range 0.05\%--0.90\%, mean 0.37\%), while depth accounts for 15.3\%--29.9\% of variance in drifting features.
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_cross_model_detail.tex-23-The generator$\times$depth interaction is also $< 1\%$.
artifacts/_project/paper/appendix_cross_model_detail.tex-24-This confirms that the F1\,=\,0.830 cross-model advantage reflects depth signal rather than generator diversity accumulation: mixing generators across chain steps does not introduce a confounding generator-identity cue.
--
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_qlora.tex-16-\textbf{Method} & \textbf{5-class F1} & \textbf{3-class F1} & \textbf{Per-class F1 (5-class)} \\
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_qlora.tex-17-\midrule
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_qlora.tex-18-XGBoost (7 features) & 0.501 $\pm$ 0.038 & 0.789 & --- \\
artifacts/_project/paper/appendix_qlora.tex:19:QLoRA (Qwen3-0.6B)   & 0.583 $\pm$ 0.010 & 0.905 $\pm$ 0.003 & 0.999\,/\,0.796\,/\,0.413\,/\,0.259\,/\,0.447 \\
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_qlora.tex-20-\bottomrule
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_qlora.tex-21-\end{tabular}}
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_qlora.tex-22-\end{table}
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_qlora.tex-23-
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_qlora.tex-24-\paragraph{Results.}
artifacts/_project/paper/appendix_qlora.tex:25:QLoRA achieves 3-class LOGO F1\,=\,0.905 ($\pm$0.003) under 6-generator LOGO, a +11.6\,pp improvement over the same-subset XGBoost baseline (0.789).
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_qlora.tex-26-On 5-class evaluation, QLoRA reaches F1\,=\,0.583 ($\pm$0.010) vs.\ 0.501 for XGBoost (+8.2\,pp), with the largest gains at gen-1 (0.796 vs.\ 0.634) and gen-2 (0.413 vs.\ 0.268).
artifacts/_project/paper/appendix_qlora.tex-27-The gen-2/gen-3 boundary remains the primary failure mode (gen-3 F1\,=\,0.259), consistent with the feature-level analysis in \S\ref{sec:discussion}.
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_qlora.tex-28-
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_qlora.tex-29-\paragraph{Hyperparameter robustness.}
artifacts/_project/paper/appendix_qlora.tex:30:A second run with LoRA rank 32 and seed 123 yields 5-class F1\,=\,0.587 ($\pm$0.005) and 3-class F1\,=\,0.905 ($\pm$0.004), which confirms stability across hyperparameter and seed variation ($\Delta < 1$\,pp on both metrics).
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_qlora.tex-31-
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_qlora.tex-32-\paragraph{Implications.}
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_qlora.tex-33-The substantial 3-class improvement demonstrates that raw token embeddings contain depth signal beyond what summary statistics capture; the seven handcrafted features are a strong but lossy compression of the full distributional information.
--
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_cross_temp.tex-17-
artifacts/_project/paper/appendix_cross_temp.tex-18-\item \textbf{Generator-specific vulnerability}: Qwen3-1.7B, the only generator with temperature-mismatched test data, drops to F1\,=\,0.418 under cross-temperature conditions while all other generators maintain F1 $>$ 0.76. This confirms that depth features are calibrated to the specific decoding regime.
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_cross_temp.tex-19-
artifacts/_project/paper/appendix_cross_temp.tex:20:\item \textbf{Binary transfer for the mismatched generator}: For Qwen3-1.7B (the only generator with actual temperature mismatch), binary F1 drops from 0.948 to 0.713 under 0.7$\rightarrow$1.0 transfer but recovers in the reverse direction (1.0$\rightarrow$0.7: 0.948), consistent with the asymmetric pattern in Item 2. The aggregate binary range (0.900--0.958) is inflated by five generators whose data is identical across conditions.
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_cross_temp.tex-21-\end{enumerate}
--
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_feature_candidates.tex-13-\midrule
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_feature_candidates.tex-14-median    & 0.685 & 0.794 & $+$0.008 & 0.960 & entropy\_mean \\
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_feature_candidates.tex-15-p90       & 0.693 & 0.960 & $+$0.000 & 0.937 & entropy\_mean \\
artifacts/_project/paper/appendix_feature_candidates.tex:16:IQR       & 0.708 & 1.079 & $+$0.007 & 0.908 & entropy\_std \\
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_feature_candidates.tex-17-CV        & 0.633 & 0.980 & $-$0.000 & 0.761 & entropy\_mean \\
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_feature_candidates.tex-18-skewness  & 0.651 & 0.940 & $+$0.010 & 0.780 & entropy\_mean \\
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_feature_candidates.tex-19-kurtosis  & 0.635 & 0.769 & $-$0.003 & 0.650 & entropy\_mean \\
--
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_instruct.tex-84-\textbf{Model} & XGB & QLoRA & $\boldsymbol{\Delta}$ & \textbf{$N$} \\
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_instruct.tex-85-\midrule
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_instruct.tex-86-OLMo-2-1B-Inst   & 0.575 & 0.888\,$\pm$\,0.007 & $+$31.3\,pp & 4{,}429 \\
artifacts/_project/paper/appendix_instruct.tex:87:Qwen3-1.7B-Inst  & 0.732 & 0.907\,$\pm$\,0.008 & $+$17.5\,pp & 4{,}963 \\
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_instruct.tex-88-\midrule
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_instruct.tex-89-OLMo-2-1B (base) &       & 0.859\,$\pm$\,0.004 &             & 2{,}379 \\
artifacts/_project/paper/appendix_instruct.tex:90:Qwen3-1.7B (base)&       & 0.904\,$\pm$\,0.009 &             & 2{,}291 \\
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_instruct.tex-91-\bottomrule
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_instruct.tex-92-\end{tabular}}
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_instruct.tex-93-\end{table}
--
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_temperature_stability.tex-25-
artifacts/_project/paper/appendix_temperature_stability.tex-26-The partition anchors are robust: entropy mean remains drifting in all 12 conditions, TTR in 10/12, and hapax ratio in 9/12; entropy min and entropy max stay near-stationary in 10/12 and 9/12 conditions, respectively.
artifacts/_project/paper/appendix_temperature_stability.tex-27-The two boundary features are more temperature-sensitive: entropy std is drifting at $\tau{=}0.5$ for all generators but falls to intermediate at $\tau{=}0.9$ for three of four, while tail decay fluctuates between near-stationary and intermediate across generators.
artifacts/_project/paper/appendix_temperature_stability.tex:28:Effect sizes compress monotonically with temperature: for the fixed drifting set (entropy mean, TTR, hapax ratio), mean $|d|$ drops from 1.09 at $\tau{=}0.5$ to 0.90 at $\tau{=}0.7$ to 0.48 at $\tau{=}0.9$, shifting individual features across partition boundaries at high temperature without altering the qualitative hierarchy: lexical diversity features drift fastest, entropy extrema remain stable across all conditions tested.
--
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_qualitative_examples.tex-9-\caption{Example text chain from seed 120 (Pythia-2.8B, continuation prompt). Gen-0 is the original Wikipedia passage; gen-1 and gen-2 are successive LLM continuations. Text is truncated for space.}
artifacts/_project/paper/appendix_qualitative_examples.tex-10-\label{tab:qualitative-text}
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_qualitative_examples.tex-11-\small
artifacts/_project/paper/appendix_qualitative_examples.tex:12:\begin{tabular}{p{0.90\columnwidth}}
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_qualitative_examples.tex-13-\toprule
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_qualitative_examples.tex-14-\textbf{Gen-0 (Wikipedia seed)} \\
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_qualitative_examples.tex-15-\midrule
--
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/abstract.tex-2-\begin{abstract}
artifacts/_project/paper/abstract.tex-3-As LLM outputs re-enter training corpora and seed further generation, understanding how recursive generation reshapes text distributions is critical for data provenance and corpus curation---yet existing detectors answer only the binary human-or-machine question, ignoring \emph{generation depth}: we introduce \emph{depth profiling} to address this gap.
artifacts/_project/paper/abstract.tex-4-We decompose distributional drift under recursive generation into location and shape components, revealing an asymmetry we term \emph{differential depth response} (DDR): across eight base-model generators from five families, NLL location features drift monotonically with depth (effect size $d{=}0.74$--$1.05$) while three shape features remain near-stationary ($d < 0.10$), with entropy std intermediate ($d{=}0.46$)---a ${\geq}8{\times}$ effect-size gap.
artifacts/_project/paper/abstract.tex:5:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/abstract.tex-6-Instruction tuning compresses DDR, bounding current applicability to base models.
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/abstract.tex-7-\end{abstract}
--
artifacts/_project/paper/results.tex-21-Cross-model chains (randomly selected generator per step) yield binary F1\,=\,0.830 (95\% CI [.818, .841]; Appendix~\ref{app:cross-model-detail}) under 5-generator LOGO.\footnote{Pythia-2.8B/1B, OLMo-2-1B, Qwen3-0.6B/1.7B; generator-level LOGO with bootstrap CIs ($n$\,=\,1{,}000). Not directly comparable to 8-generator LOGO due to differing subsets.}
artifacts/_project/paper/results.tex-22-Single-generator transfer (Appendix~\ref{app:transfer}) confirms the signal is not a mixed-chain artifact (mean transfer F1\,=\,0.810, Figure~\ref{fig:transfer-heatmap}; LOFO\,=\,0.686); the cross-model advantage is only 2\,pp; ANOVA variance decomposition confirms generator identity contributes ${<}1$\% of feature variance ($\eta^2_{\text{gen}} \leq 0.009$; Appendix~\ref{app:cross-model-detail}).
artifacts/_project/paper/results.tex-23-A scale effect emerges: smaller models achieve higher F1 (Pythia-2.8B: 0.724 vs.\ Mistral-7B: 0.633), partly reflecting same-family affinity with the Pythia-410M reference (spread $\leq$0.013; \S\ref{sec:results-differential}).
artifacts/_project/paper/results.tex:24:An end-to-end QLoRA classifier reaches 3-class F1\,=\,0.905 ($+$11.6\,pp; Appendix~\ref{app:qlora}), confirming additional depth signal in token-level representations; on instruct data, QLoRA recovers to 0.89--0.91 (Appendix~\ref{app:instruct}), establishing the decomposition as DDR's primary contribution.
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/results.tex-25-
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/results.tex-26-\paragraph{Confound controls.}
artifacts/_project/paper/results.tex-27-Length-matched subsampling yields binary F1\,=\,0.724 (vs.\ 0.770; Appendix~\ref{app:length}); independent-seed evaluation with disjoint pools (F1\,=\,0.680; Appendix~\ref{app:seed-control}) confirms the classifier captures generative degradation, not seed-specific content.
--
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_decoding_strategy.tex-93-independent of sampling truncation.
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_decoding_strategy.tex-94-Top-$k$ sampling ($k{=}50$) partially attenuates the partition.
artifacts/_project/paper/appendix_decoding_strategy.tex-95-Shape features show boundary violations in 4/8 generators under top-$k$; however, these generators exhibit comparable or higher violations under nucleus sampling (Pythia entropy\_max: 0.21--0.25 nucleus vs.\ 0.26--0.27 top-$k$; OLMo tail\_decay: 0.22 under both), indicating model-intrinsic boundary effects rather than strategy-induced degradation.
artifacts/_project/paper/appendix_decoding_strategy.tex:96:Core drifting effect sizes weaken (mean $d{=}$\textbf{0.67} vs.\ \textbf{0.90} under nucleus).
artifacts/_project/paper/appendix_decoding_strategy.tex-97-This modulation is consistent with the mechanistic account in \S\ref{sec:discussion}:
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_decoding_strategy.tex-98-top-$k$ truncation introduces a fixed-width selection window that interacts differently
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_decoding_strategy.tex-99-with depth-compressed distributions than nucleus sampling's probability-mass truncation,
--
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/introduction.tex-18-\end{figure*}
artifacts/_project/paper/introduction.tex-19-We focus on base (pretrained) models; instruction tuning degrades depth signal (Appendix~\ref{app:instruct}).
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/introduction.tex-20-
artifacts/_project/paper/introduction.tex:21:As a proof of concept, a lightweight 7-feature ensemble informed by DDR achieves leak-free binary F1\,=\,0.694 under leave-one-generator-out evaluation, matching multi-detector ensembles at ${\sim}2.4\times$ lower cost; an end-to-end QLoRA classifier reaches 3-class F1\,=\,0.905 (6-gen LOGO; Appendix~\ref{app:qlora}), confirming that the depth signal extends well beyond handcrafted features.
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/introduction.tex-22-
artifacts/_project/paper/introduction.tex-23-Our contributions:
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/introduction.tex-24-\begin{enumerate}[nosep,leftmargin=*]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a6d70e92-d219-418b-aa14-79c5ae3edec9",
  "isSidechain": true,
  "promptId": "5c60df84-fcb8-462d-8f59-5098b0a96974",
  "agentId": "a7859a4de84d0a5b2",
  "type": "user",
  "uuid": "aa591ef0-4441-4746-a6b9-9d1f7c981544",
  "sourceToolAssistantUUID": "a6d70e92-d219-418b-aa14-79c5ae3edec9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "727cbce6-9768-410b-9211-4635321ab6fe",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-23T19:41:08.091Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01Vwi6jQ5ffT8qDgoJdPHbuZ`</summary>

```json
{
  "pattern": "0\\.789",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
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
  "parentUuid": "aa591ef0-4441-4746-a6b9-9d1f7c981544",
  "isSidechain": true,
  "agentId": "a7859a4de84d0a5b2",
  "requestId": "req_011CbL4ywb7WswXcf6jjA72Y",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "53a51fc4-655e-43fa-a155-7dae035797cf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "727cbce6-9768-410b-9211-4635321ab6fe",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HSoAsfMdSgZs6iCVRTHALD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1634,
      "cache_read_input_tokens": 18103,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1634,
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

_source line 9 · 2026-05-23T19:41:08.106Z_

<details><summary>↩ Tool result · `toolu_01Vwi6jQ5ffT8qDgoJdPHbuZ`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_cross_model_detail.tex-3-\begin{table}[ht]
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_cross_model_detail.tex-4-\centering
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_cross_model_detail.tex-5-\footnotesize
artifacts/_project/paper/appendix_cross_model_detail.tex:6:\caption{Cross-model chain per-class performance (generator-level leave-one-out, $N$\,=\,2{,}964, $n_{\text{generators}}$\,=\,5: Pythia-2.8B/1B, OLMo-2-1B, Qwen3-0.6B/1.7B). Macro F1\,=\,0.831 under class balancing; under natural class distribution, macro F1\,=\,0.789. Binary F1 (gen-1 vs.\ gen-2+)\,=\,0.830 (95\% CI [.818, .841], case-level bootstrap, $n$\,=\,2{,}000). Cross-model chains avoid the gen-0 seed sharing issue present in single-generator LOGO.}
artifacts/_project/paper/appendix_cross_model_detail.tex-7-\label{tab:cross-model-perclass}
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_cross_model_detail.tex-8-\begin{tabular}{lcccc}
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_cross_model_detail.tex-9-\toprule
--
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_cross_model_detail.tex-11-\midrule
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_cross_model_detail.tex-12-gen-0   & 0.921 & 0.948 & 0.935 & [.923, .946] \\
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_cross_model_detail.tex-13-gen-1   & 0.737 & 0.803 & 0.768 & [.748, .788] \\
artifacts/_project/paper/appendix_cross_model_detail.tex:14:gen-2+  & 0.842 & 0.742 & 0.789 & [.768, .809] \\
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_cross_model_detail.tex-15-\midrule
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_cross_model_detail.tex-16-\textbf{Macro} & --- & --- & \textbf{0.831} & [.817, .844] \\
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_cross_model_detail.tex-17-\bottomrule
--
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_qlora.tex-1-To assess whether depth signal extends beyond handcrafted features, we fine-tune a pretrained language model end-to-end as a depth classifier using QLoRA \cite{qlora}.
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_qlora.tex-2-
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_qlora.tex-3-\paragraph{Setup.}
artifacts/_project/paper/appendix_qlora.tex:4:We fine-tune Qwen3-0.6B-Base with LoRA rank 16, learning rate $2 \times 10^{-4}$, and 3 epochs, framing depth estimation as 5-class sequence classification (gen-0 through gen-4).\footnote{Evaluated on the original 6-generator subset; XGBoost 3-class F1\,=\,0.789. We expect 8-generator training to further improve given additional diversity; the comparison direction is preserved.}
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_qlora.tex-5-For 3-class evaluation, we collapse predictions into gen-0\,/\,gen-1\,/\,gen-2+ post hoc.
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_qlora.tex-6-All results use the same LOGO protocol as the main experiments.
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_qlora.tex-7-
--
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_qlora.tex-15-\toprule
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_qlora.tex-16-\textbf{Method} & \textbf{5-class F1} & \textbf{3-class F1} & \textbf{Per-class F1 (5-class)} \\
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_qlora.tex-17-\midrule
artifacts/_project/paper/appendix_qlora.tex:18:XGBoost (7 features) & 0.501 $\pm$ 0.038 & 0.789 & --- \\
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_qlora.tex-19-QLoRA (Qwen3-0.6B)   & 0.583 $\pm$ 0.010 & 0.905 $\pm$ 0.003 & 0.999\,/\,0.796\,/\,0.413\,/\,0.259\,/\,0.447 \\
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_qlora.tex-20-\bottomrule
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_qlora.tex-21-\end{tabular}}
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_qlora.tex-22-\end{table}
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_qlora.tex-23-
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_qlora.tex-24-\paragraph{Results.}
artifacts/_project/paper/appendix_qlora.tex:25:QLoRA achieves 3-class LOGO F1\,=\,0.905 ($\pm$0.003) under 6-generator LOGO, a +11.6\,pp improvement over the same-subset XGBoost baseline (0.789).
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_qlora.tex-26-On 5-class evaluation, QLoRA reaches F1\,=\,0.583 ($\pm$0.010) vs.\ 0.501 for XGBoost (+8.2\,pp), with the largest gains at gen-1 (0.796 vs.\ 0.634) and gen-2 (0.413 vs.\ 0.268).
artifacts/_project/paper/appendix_qlora.tex-27-The gen-2/gen-3 boundary remains the primary failure mode (gen-3 F1\,=\,0.259), consistent with the feature-level analysis in \S\ref{sec:discussion}.
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_qlora.tex-28-
--
artifacts/_project/paper/appendix_cross_temp.tex-11-Key observations from the cross-temperature analysis:
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_cross_temp.tex-12-
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_cross_temp.tex-13-\begin{enumerate}[nosep]
artifacts/_project/paper/appendix_cross_temp.tex:14:\item \textbf{Matched-temperature robustness}: Both $t{=}0.7$ and $t{=}1.0$ matched conditions yield comparable performance (3-class F1: 0.789 vs.\ 0.726), with the gap attributable to weaker depth signal at high temperature rather than classifier degradation.
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_cross_temp.tex-15-
artifacts/_project/paper/appendix_cross_temp.tex-16-\item \textbf{Asymmetric transfer}: Training at $t{=}1.0$ and testing at $t{=}0.7$ (F1\,=\,0.791) transfers well, but the reverse (0.7$\rightarrow$1.0, F1\,=\,0.723) degrades. This asymmetry reflects the information structure: features learned from high-variance (high-temperature) data generalize to low-variance settings, but not vice versa.
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_cross_temp.tex-17-
--
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_classifier.tex-14-\toprule
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_classifier.tex-15-Classifier & Avg F1 & OLMo-2 & Py-1B & Py-2.8B & Qw-0.6B & Qw-1.7B & Qw-8B \\
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_classifier.tex-16-\midrule
artifacts/_project/paper/appendix_classifier.tex:17:XGBoost          & 0.789 & 0.764 & 0.856 & 0.804 & 0.824 & 0.806 & 0.683 \\
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_classifier.tex-18-Random Forest    & 0.790 & 0.764 & 0.856 & 0.804 & 0.825 & 0.807 & 0.684 \\
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_classifier.tex-19-Logistic Regr.   & 0.725 & 0.719 & 0.781 & 0.740 & 0.745 & 0.743 & 0.624 \\
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_classifier.tex-20-\bottomrule
--
artifacts/_project/paper/appendix_lofo.tex:1:We complement the permutation importance analysis (\S\ref{sec:results-differential}) with a leave-one-feature-out ablation. Each row drops one of the seven features and re-evaluates the full 6-gen LOGO protocol; $\Delta$ is the change relative to the full 7-feature ensemble (F1\,=\,0.789).
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_lofo.tex-2-
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_lofo.tex-3-\begin{table}[ht]
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_lofo.tex-4-\centering
--
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_lofo.tex-15-hapax\_ratio    & 0.785 & $-$0.42\,pp \\
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_lofo.tex-16-tail\_decay     & 0.786 & $-$0.33\,pp \\
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_lofo.tex-17-entropy\_std    & 0.786 & $-$0.29\,pp \\
artifacts/_project/paper/appendix_lofo.tex:18:entropy\_min    & 0.789 & $+$0.01\,pp \\
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_lofo.tex-19-\midrule
artifacts/_project/paper/appendix_lofo.tex:20:Full (7 features) & 0.789 & --- \\
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_lofo.tex-21-\bottomrule
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_lofo.tex-22-\end{tabular}
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_lofo.tex-23-\end{table}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "53a51fc4-655e-43fa-a155-7dae035797cf",
  "isSidechain": true,
  "promptId": "5c60df84-fcb8-462d-8f59-5098b0a96974",
  "agentId": "a7859a4de84d0a5b2",
  "type": "user",
  "uuid": "c1a5174f-b74f-47cb-a8aa-5100963b438e",
  "sourceToolAssistantUUID": "53a51fc4-655e-43fa-a155-7dae035797cf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "727cbce6-9768-410b-9211-4635321ab6fe",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-23T19:41:08.715Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01EqLfz61PWaSMt1FARt37ho`</summary>

```json
{
  "pattern": "0\\.487",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
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
  "parentUuid": "c1a5174f-b74f-47cb-a8aa-5100963b438e",
  "isSidechain": true,
  "agentId": "a7859a4de84d0a5b2",
  "requestId": "req_011CbL4ywb7WswXcf6jjA72Y",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "35904a44-feb4-4243-a077-83d19899d122",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "727cbce6-9768-410b-9211-4635321ab6fe",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HSoAsfMdSgZs6iCVRTHALD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1634,
      "cache_read_input_tokens": 18103,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1634,
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

_source line 11 · 2026-05-23T19:41:08.726Z_

<details><summary>↩ Tool result · `toolu_01EqLfz61PWaSMt1FARt37ho`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_instruct.tex-47-\end{table}
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_instruct.tex-48-
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_instruct.tex-49-Retraining recovers substantial within-model performance ($+$6.8--26.9\,pp), but the retrained F1 (0.590--0.660) remains below base-model levels (0.69--0.72).
artifacts/_project/paper/appendix_instruct.tex:50:Three-generator instruct LOGO yields binary F1\,=\,0.487, indicating weak cross-generator transfer under instruction tuning.
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_instruct.tex-51-
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_instruct.tex-52-\paragraph{DDR structure under instruction tuning.}
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_instruct.tex-53-$k{=}2$ clustering in $(|\rho|, d)$ space on pooled instruct features yields silhouette\,=\,0.372 (vs.\ 0.660 for base models), indicating that the clean drifting/non-drifting partition is substantially compressed.
--
artifacts/_project/paper/limitations.tex-3-\label{sec:limitations}
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/limitations.tex-4-\vspace{-1mm}
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/limitations.tex-5-
artifacts/_project/paper/limitations.tex:6:\looseness=-1 All eight generators are base (pretrained) models with $\leq$8.2B parameters; instruction-tuned variants show substantially degraded depth signal (LOGO binary F1\,=\,0.487; Appendix~\ref{app:instruct}), though QLoRA partially recovers (F1\,=\,0.89--0.91), suggesting the signal is compressed rather than eliminated.
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/limitations.tex-7-The evaluation assumes English Wikipedia seeds, a fixed decoding regime ($t{=}0.7$, nucleus $p{=}0.9$), and an English-centric reference model (Pythia-410M); cross-temperature and cross-lingual transfer remain untested.
artifacts/_project/paper/limitations.tex-8-Depth resolution is bounded at three classes (gen-0\,/\,gen-1\,/\,gen-2+); finer-grained 5-class classification yields F1\,$\approx$\,0.50 with deeper depths mutually indistinguishable (Appendix~\ref{app:finer-depth}).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "35904a44-feb4-4243-a077-83d19899d122",
  "isSidechain": true,
  "promptId": "5c60df84-fcb8-462d-8f59-5098b0a96974",
  "agentId": "a7859a4de84d0a5b2",
  "type": "user",
  "uuid": "8a7bc1d5-0c84-4410-8ce8-4fd2282f36d1",
  "sourceToolAssistantUUID": "35904a44-feb4-4243-a077-83d19899d122",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "727cbce6-9768-410b-9211-4635321ab6fe",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-23T19:41:09.586Z_

<details open><summary>🔧 Tool call — Grep · `toolu_015gm2MBmQtxGH8LKYAzpjQA`</summary>

```json
{
  "pattern": "3-4|3--4|±3|batch|prevalence",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
  "type": "tex",
  "output_mode": "content",
  "context": 3,
  "head_limit": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8a7bc1d5-0c84-4410-8ce8-4fd2282f36d1",
  "isSidechain": true,
  "agentId": "a7859a4de84d0a5b2",
  "requestId": "req_011CbL4ywb7WswXcf6jjA72Y",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "20f242ce-ee9d-4063-a3b9-9effcf949354",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "727cbce6-9768-410b-9211-4635321ab6fe",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HSoAsfMdSgZs6iCVRTHALD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1634,
      "cache_read_input_tokens": 18103,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1634,
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

_source line 13 · 2026-05-23T19:41:09.598Z_

<details><summary>↩ Tool result · `toolu_015gm2MBmQtxGH8LKYAzpjQA`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/conclusion.tex-5-
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/conclusion.tex-6-\looseness=-2 Recursive generation produces a decomposable depth response---location features drift while shape is approximately preserved---enabling cross-generator depth classification (F1\,=\,0.694--0.762) within the base-model scope.
artifacts/_project/paper/conclusion.tex-7-Cross-model chains confirm generalization across architectures (F1\,=\,0.830; ANOVA: depth explains ${>}48{\times}$ more variance than generator identity).
artifacts/_project/paper/conclusion.tex:8:QLoRA recovery (F1\,=\,0.89--0.91) suggests tractable extension to instruct models; DDR connects depth profiling to model collapse analysis and corpus auditing (${\pm}3$--$4$\% batch estimation; Appendix~\ref{app:error-analysis}).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "20f242ce-ee9d-4063-a3b9-9effcf949354",
  "isSidechain": true,
  "promptId": "5c60df84-fcb8-462d-8f59-5098b0a96974",
  "agentId": "a7859a4de84d0a5b2",
  "type": "user",
  "uuid": "53b7e426-0022-4efb-a9b3-c1070f28eb5e",
  "sourceToolAssistantUUID": "20f242ce-ee9d-4063-a3b9-9effcf949354",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "727cbce6-9768-410b-9211-4635321ab6fe",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-23T19:41:10.136Z_

<details open><summary>🔧 Tool call — Grep · `toolu_018Km2dzHHeHvc9AmJimBmYW`</summary>

```json
{
  "pattern": "48|>48|48×|48\\\\times",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
  "type": "tex",
  "output_mode": "content",
  "context": 3,
  "head_limit": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "53b7e426-0022-4efb-a9b3-c1070f28eb5e",
  "isSidechain": true,
  "agentId": "a7859a4de84d0a5b2",
  "requestId": "req_011CbL4ywb7WswXcf6jjA72Y",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "c9a5d6f7-6b00-4458-ab5e-d52a1f66928d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "727cbce6-9768-410b-9211-4635321ab6fe",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HSoAsfMdSgZs6iCVRTHALD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1634,
      "cache_read_input_tokens": 18103,
      "output_tokens": 815,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1634
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 815,
          "cache_read_input_tokens": 18103,
          "cache_creation_input_tokens": 1634,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1634,
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

_source line 15 · 2026-05-23T19:41:10.155Z_

<details><summary>↩ Tool result · `toolu_018Km2dzHHeHvc9AmJimBmYW`</summary>

```text
&lt;persisted-output>
Output too large (27KB). Full output saved to: /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-3-projects-gen-depth-fingerprint/727cbce6-9768-410b-9211-4635321ab6fe/tool-results/toolu_018Km2dzHHeHvc9AmJimBmYW.txt

Preview (first 2KB):
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_cross_model_detail.tex-9-\toprule
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_cross_model_detail.tex-10-\textbf{Class} & \textbf{Prec.} & \textbf{Rec.} & \textbf{F1} & \textbf{95\% CI} \\
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_cross_model_detail.tex-11-\midrule
artifacts/_project/paper/appendix_cross_model_detail.tex:12:gen-0   & 0.921 & 0.948 & 0.935 & [.923, .946] \\
artifacts/_project/paper/appendix_cross_model_detail.tex:13:gen-1   & 0.737 & 0.803 & 0.768 & [.748, .788] \\
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_cross_model_detail.tex-14-gen-2+  & 0.842 & 0.742 & 0.789 & [.768, .809] \\
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_cross_model_detail.tex-15-\midrule
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_cross_model_detail.tex-16-\textbf{Macro} & --- & --- & \textbf{0.831} & [.817, .844] \\
--
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_cross_temp.tex-17-
artifacts/_project/paper/appendix_cross_temp.tex-18-\item \textbf{Generator-specific vulnerability}: Qwen3-1.7B, the only generator with temperature-mismatched test data, drops to F1\,=\,0.418 under cross-temperature conditions while all other generators maintain F1 $>$ 0.76. This confirms that depth features are calibrated to the specific decoding regime.
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_cross_temp.tex-19-
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c9a5d6f7-6b00-4458-ab5e-d52a1f66928d",
  "isSidechain": true,
  "promptId": "5c60df84-fcb8-462d-8f59-5098b0a96974",
  "agentId": "a7859a4de84d0a5b2",
  "type": "user",
  "uuid": "e9176d67-448d-4cf8-8346-bc0d0598c7ca",
  "sourceToolAssistantUUID": "c9a5d6f7-6b00-4458-ab5e-d52a1f66928d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "727cbce6-9768-410b-9211-4635321ab6fe",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 16 · 2026-05-23T19:41:11.398Z_

Let me read the full output from the large grep result to get the prevalence and variance ratio matches:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e9176d67-448d-4cf8-8346-bc0d0598c7ca",
  "isSidechain": true,
  "agentId": "a7859a4de84d0a5b2",
  "requestId": "req_011CbL4zKmcPWNTftaE2pVYk",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d5c50c8d-a508-4277-a230-9854495b81f1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "727cbce6-9768-410b-9211-4635321ab6fe",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_014Kyn9mpKyK2svUNnZpXgrW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 13110,
      "cache_read_input_tokens": 19737,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 13110,
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

_source line 17 · 2026-05-23T19:41:11.816Z_

<details open><summary>🔧 Tool call — Read · `toolu_012roGbvLcdf18mFigmreZfa`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-3-projects-gen-depth-fingerprint/727cbce6-9768-410b-9211-4635321ab6fe/tool-results/toolu_018Km2dzHHeHvc9AmJimBmYW.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d5c50c8d-a508-4277-a230-9854495b81f1",
  "isSidechain": true,
  "agentId": "a7859a4de84d0a5b2",
  "requestId": "req_011CbL4zKmcPWNTftaE2pVYk",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "caee0341-21a9-49c5-a10a-63e3e2fe1ab3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "727cbce6-9768-410b-9211-4635321ab6fe",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_014Kyn9mpKyK2svUNnZpXgrW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 13110,
      "cache_read_input_tokens": 19737,
      "output_tokens": 162,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 13110
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 162,
          "cache_read_input_tokens": 19737,
          "cache_creation_input_tokens": 13110,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 13110,
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

_source line 18 · 2026-05-23T19:41:12.089Z_

<details><summary>↩ Tool result · `toolu_012roGbvLcdf18mFigmreZfa`</summary>

```text
1	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_cross_model_detail.tex-9-\toprule
2	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_cross_model_detail.tex-10-\textbf{Class} & \textbf{Prec.} & \textbf{Rec.} & \textbf{F1} & \textbf{95\% CI} \\
3	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_cross_model_detail.tex-11-\midrule
4	artifacts/_project/paper/appendix_cross_model_detail.tex:12:gen-0   & 0.921 & 0.948 & 0.935 & [.923, .946] \\
5	artifacts/_project/paper/appendix_cross_model_detail.tex:13:gen-1   & 0.737 & 0.803 & 0.768 & [.748, .788] \\
6	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_cross_model_detail.tex-14-gen-2+  & 0.842 & 0.742 & 0.789 & [.768, .809] \\
7	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_cross_model_detail.tex-15-\midrule
8	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_cross_model_detail.tex-16-\textbf{Macro} & --- & --- & \textbf{0.831} & [.817, .844] \\
9	--
10	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_cross_temp.tex-17-
11	artifacts/_project/paper/appendix_cross_temp.tex-18-\item \textbf{Generator-specific vulnerability}: Qwen3-1.7B, the only generator with temperature-mismatched test data, drops to F1\,=\,0.418 under cross-temperature conditions while all other generators maintain F1 $>$ 0.76. This confirms that depth features are calibrated to the specific decoding regime.
12	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_cross_temp.tex-19-
13	artifacts/_project/paper/appendix_cross_temp.tex:20:\item \textbf{Binary transfer for the mismatched generator}: For Qwen3-1.7B (the only generator with actual temperature mismatch), binary F1 drops from 0.948 to 0.713 under 0.7$\rightarrow$1.0 transfer but recovers in the reverse direction (1.0$\rightarrow$0.7: 0.948), consistent with the asymmetric pattern in Item 2. The aggregate binary range (0.900--0.958) is inflated by five generators whose data is identical across conditions.
14	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_cross_temp.tex-21-\end{enumerate}
15	--
16	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/conclusion.tex-4-\vspace{-3mm}
17	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/conclusion.tex-5-
18	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/conclusion.tex-6-\looseness=-2 Recursive generation produces a decomposable depth response---location features drift while shape is approximately preserved---enabling cross-generator depth classification (F1\,=\,0.694--0.762) within the base-model scope.
19	artifacts/_project/paper/conclusion.tex:7:Cross-model chains confirm generalization across architectures (F1\,=\,0.830; ANOVA: depth explains ${>}48{\times}$ more variance than generator identity).
20	artifacts/_project/paper/conclusion.tex-8-QLoRA recovery (F1\,=\,0.89--0.91) suggests tractable extension to instruct models; DDR connects depth profiling to model collapse analysis and corpus auditing (${\pm}3$--$4$\% batch estimation; Appendix~\ref{app:error-analysis}).
21	--
22	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_9gen_scale.tex-14-\toprule
23	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_9gen_scale.tex-15-\textbf{Generator} & \textbf{Family} & \textbf{Params} & \textbf{3-class F1} & \textbf{95\% CI} & \textbf{Binary F1} & \textbf{95\% CI} \\
24	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_9gen_scale.tex-16-\midrule
25	artifacts/_project/paper/appendix_9gen_scale.tex:17:Pythia-1B       & Pythia  & 1.0B & 0.857 & [0.848, 0.866] & 0.785 & --- \\
26	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_9gen_scale.tex-18-Qwen3-0.6B      & Qwen    & 0.6B & 0.819 & [0.807, 0.830] & 0.743 & --- \\
27	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_9gen_scale.tex-19-Pythia-2.8B     & Pythia  & 2.8B & 0.812 & [0.801, 0.822] & 0.728 & --- \\
28	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_9gen_scale.tex-20-Qwen3-1.7B      & Qwen    & 1.7B & 0.811 & [0.800, 0.823] & 0.746 & --- \\
29	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_9gen_scale.tex-21-OLMo-2-1B       & OLMo    & 1.5B & 0.773 & [0.762, 0.784] & 0.692 & --- \\
30	artifacts/_project/paper/appendix_9gen_scale.tex:22:Llama-3.2-3B    & Llama   & 3.2B & 0.759 & [0.748, 0.770] & 0.680 & --- \\
31	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_9gen_scale.tex-23-Qwen3-8B        & Qwen    & 8.2B & 0.696 & [0.683, 0.709] & 0.647 & [0.631, 0.664] \\
32	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_9gen_scale.tex-24-Gemma-2-2B      & Gemma   & 2.6B & 0.628 & [0.622, 0.634] & 0.440 & [0.432, 0.449] \\
33	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_9gen_scale.tex-25-Mistral-7B      & Mistral & 7.0B & 0.605 & [0.593, 0.617] & 0.534 & --- \\
34	--
35	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/discussion.tex-5-\paragraph{Mechanistic interpretation.}
36	artifacts/_project/paper/discussion.tex-6-\looseness=-1 DDR reflects an empirical regularity of base-model autoregressive generation: recursive inputs compress the token-level NLL distribution monotonically (Appendix~\ref{app:nll-distribution}), shifting location features independently of the token-selection mechanism.
37	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/discussion.tex-7-Shape features resist this compression because they are architecturally bounded---entropy max is capped by $\log|V|$, and tail decay reflects softmax long-tail geometry rather than input statistics---explaining their near-stationarity across generators and depths.
38	artifacts/_project/paper/discussion.tex:8:[Omitted long matching line]
39	artifacts/_project/paper/discussion.tex-9-DDR is distinct from model collapse \cite{curse_of_recursion,strong_model_collapse}---retraining erodes tail via weight updates, while DDR shifts only location---and complements concurrent iterative-generation studies (Appendix~\ref{app:iterative-comparison}).
40	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/discussion.tex-10-
41	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/discussion.tex-11-\paragraph{Failure modes and practical scope.}
42	artifacts/_project/paper/discussion.tex:12:\looseness=-2 The gen-1$\to$gen-2 boundary is the primary classification failure point (depth-2 error rate\,=\,48.4\%; Appendix~\ref{app:error-analysis}): the gen-0$\to$gen-1 transition produces the largest distributional shift, so depth-2 texts carry insufficient accumulated drift beyond gen-1 for reliable separation.
43	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/discussion.tex-13-Deeper generations ($\geq$gen-3) show monotonically decreasing error rates ($\leq$29.2\%), confirming that DDR signal strengthens with chain length.
44	artifacts/_project/paper/discussion.tex-14-Instruction tuning compresses DDR (QLoRA: F1\,=\,0.89--0.91; Appendix~\ref{app:instruct}), while cross-domain signal persists (F1\,=\,0.74--0.75; Appendix~\ref{app:domain}).
45	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/discussion.tex-15-\vspace{-2mm}
46	--
47	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/per_family_cohens_d_table.tex-10-\cmidrule(lr){3-5} \cmidrule(lr){6-6} \cmidrule(lr){7-9}
48	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/per_family_cohens_d_table.tex-11-Family & $n$ & $H_{\mathrm{mean}}$ & TTR & Hapax & $H_{\mathrm{std}}$ & $H_{\mathrm{max}}$ & $H_{\mathrm{min}}$ & $\beta_{\mathrm{tail}}$ \\
49	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/per_family_cohens_d_table.tex-12-\midrule
50	artifacts/_project/paper/per_family_cohens_d_table.tex:13:Pythia & 2 & 1.29\tiny{$\pm$0.17} & 1.48\tiny{$\pm$0.13} & 1.50\tiny{$\pm$0.13} & 0.04\tiny{$\pm$0.01} & 0.10\tiny{$\pm$0.03} & 0.06\tiny{$\pm$0.01} & 0.27\tiny{$\pm$0.05} \\
51	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/per_family_cohens_d_table.tex-14-OLMo & 1 & 1.13 & 1.72 & 1.83 & 0.29 & 0.19 & 0.08 & 0.24 \\
52	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/per_family_cohens_d_table.tex-15-Qwen & 3 & 0.99\tiny{$\pm$0.18} & 1.49\tiny{$\pm$0.28} & 1.55\tiny{$\pm$0.29} & 0.13\tiny{$\pm$0.06} & 0.22\tiny{$\pm$0.01} & 0.12\tiny{$\pm$0.02} & 0.17\tiny{$\pm$0.04} \\
53	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/per_family_cohens_d_table.tex-16-Llama & 1 & 1.05 & 1.56 & 1.67 & 0.02 & 0.24 & 0.08 & 0.07 \\
54	--
55	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_instruct.tex-15-\cmidrule(lr){2-3} \cmidrule(lr){4-5} \cmidrule(lr){6-7}
56	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_instruct.tex-16-\textbf{Model} & Base & Instruct & Base & Instruct & Base & Instruct & \textbf{Rev.} \\
57	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_instruct.tex-17-\midrule
58	artifacts/_project/paper/appendix_instruct.tex:18:OLMo-2-1B       & 0.754 & 0.575 & 0.845 & 0.813 & $-$0.64 & $+$0.48 & 6/7 \\
59	artifacts/_project/paper/appendix_instruct.tex:19:Qwen3-1.7B      & 0.769 & 0.732 & 0.861 & 0.875 & $-$0.60 & $+$0.48 & 6/7 \\
60	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_instruct.tex-20-Llama-3.2-3B    & 0.742 & 0.544 & 0.849 & 0.838 & $-$0.63 & $+$0.23 & 3/7 \\
61	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_instruct.tex-21-\bottomrule
62	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_instruct.tex-22-\end{tabular}}
63	--
64	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_instruct.tex-24-
65	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_instruct.tex-25-Instruction tuning degrades 3-class F1 by 3.7--19.9\,pp across all three families, while binary F1 (gen-1 vs.\ gen-2+) changes remain small ($|\Delta| \leq 3.2$\,pp).
66	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_instruct.tex-26-The asymmetry indicates that instruction tuning primarily disrupts the gen-0/gen-1 boundary (human vs.\ first-generation), consistent with RLHF shifting the output distribution away from human-like text.
67	artifacts/_project/paper/appendix_instruct.tex:27:Entropy-mean $\rho$ reverses sign for all three models ($-0.60$--$-0.64$ base $\rightarrow$ $+0.23$--$+0.48$ instruct), and 6 of 7 features reverse for OLMo and Qwen vs.\ 3 of 7 for Llama.
68	artifacts/_project/paper/appendix_instruct.tex-28-This pattern is consistent with instruction tuning shifting the generation attractor rather than eliminating iterative dynamics (\S\ref{sec:discussion}).
69	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_instruct.tex-29-
70	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_instruct.tex-30-\paragraph{Retraining on instruction-tuned data.}
71	--
72	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_instruct.tex-47-\end{table}
73	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_instruct.tex-48-
74	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_instruct.tex-49-Retraining recovers substantial within-model performance ($+$6.8--26.9\,pp), but the retrained F1 (0.590--0.660) remains below base-model levels (0.69--0.72).
75	artifacts/_project/paper/appendix_instruct.tex:50:Three-generator instruct LOGO yields binary F1\,=\,0.487, indicating weak cross-generator transfer under instruction tuning.
76	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_instruct.tex-51-
77	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_instruct.tex-52-\paragraph{DDR structure under instruction tuning.}
78	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_instruct.tex-53-$k{=}2$ clustering in $(|\rho|, d)$ space on pooled instruct features yields silhouette\,=\,0.372 (vs.\ 0.660 for base models), indicating that the clean drifting/non-drifting partition is substantially compressed.
79	artifacts/_project/paper/appendix_instruct.tex:54:The compression is model-dependent: OLMo-Instruct shows near-zero $|\rho|$ for TTR and hapax (0.006, 0.025), while Qwen instruct models retain moderate correlations ($|\rho|{=}0.48$--$0.53$).
80	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_instruct.tex-55-Cross-condition transfer is near chance in both directions (base$\rightarrow$instruct binary F1\,=\,0.490; instruct$\rightarrow$base F1\,=\,0.454), with the asymmetry ($-$0.036) suggesting that instruct-trained features generalize even less to base distributions than the reverse.
81	artifacts/_project/paper/appendix_instruct.tex-56-These results indicate that instruction tuning compresses the feature-space structure underlying DDR rather than simply reversing feature directions (Figure~\ref{fig:instruct-ddr}).
82	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_instruct.tex-57-
83	--
84	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_temperature_stability.tex-25-
85	artifacts/_project/paper/appendix_temperature_stability.tex-26-The partition anchors are robust: entropy mean remains drifting in all 12 conditions, TTR in 10/12, and hapax ratio in 9/12; entropy min and entropy max stay near-stationary in 10/12 and 9/12 conditions, respectively.
86	artifacts/_project/paper/appendix_temperature_stability.tex-27-The two boundary features are more temperature-sensitive: entropy std is drifting at $\tau{=}0.5$ for all generators but falls to intermediate at $\tau{=}0.9$ for three of four, while tail decay fluctuates between near-stationary and intermediate across generators.
87	artifacts/_project/paper/appendix_temperature_stability.tex:28:Effect sizes compress monotonically with temperature: for the fixed drifting set (entropy mean, TTR, hapax ratio), mean $|d|$ drops from 1.09 at $\tau{=}0.5$ to 0.90 at $\tau{=}0.7$ to 0.48 at $\tau{=}0.9$, shifting individual features across partition boundaries at high temperature without altering the qualitative hierarchy: lexical diversity features drift fastest, entropy extrema remain stable across all conditions tested.
88	--
89	artifacts/_project/paper/limitations.tex-3-\label{sec:limitations}
90	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/limitations.tex-4-\vspace{-1mm}
91	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/limitations.tex-5-
92	artifacts/_project/paper/limitations.tex:6:\looseness=-1 All eight generators are base (pretrained) models with $\leq$8.2B parameters; instruction-tuned variants show substantially degraded depth signal (LOGO binary F1\,=\,0.487; Appendix~\ref{app:instruct}), though QLoRA partially recovers (F1\,=\,0.89--0.91), suggesting the signal is compressed rather than eliminated.
93	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/limitations.tex-7-The evaluation assumes English Wikipedia seeds, a fixed decoding regime ($t{=}0.7$, nucleus $p{=}0.9$), and an English-centric reference model (Pythia-410M); cross-temperature and cross-lingual transfer remain untested.
94	artifacts/_project/paper/limitations.tex-8-Depth resolution is bounded at three classes (gen-0\,/\,gen-1\,/\,gen-2+); finer-grained 5-class classification yields F1\,$\approx$\,0.50 with deeper depths mutually indistinguishable (Appendix~\ref{app:finer-depth}).
95	--
96	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_qualitative_examples.tex-13-\toprule
97	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_qualitative_examples.tex-14-\textbf{Gen-0 (Wikipedia seed)} \\
98	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_qualitative_examples.tex-15-\midrule
99	artifacts/_project/paper/appendix_qualitative_examples.tex:16:[Omitted long matching line]
100	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_qualitative_examples.tex-17-\midrule
101	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_qualitative_examples.tex-18-\textbf{Gen-1} \\
102	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_qualitative_examples.tex-19-\midrule
103	--
104	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_transfer.tex-17-Py-1B    & 0.834 & \underline{0.987} & 0.828 & 0.821 & 0.704 & 0.778 & 0.764 & 0.620 \\
105	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_transfer.tex-18-Qw-0.6B  & 0.786 & 0.846 & \underline{0.991} & 0.851 & 0.786 & 0.795 & 0.760 & 0.680 \\
106	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_transfer.tex-19-Qw-1.7B  & 0.794 & 0.839 & 0.859 & \underline{0.989} & 0.790 & 0.817 & 0.798 & 0.717 \\
107	artifacts/_project/paper/appendix_transfer.tex:20:Qw-8B   & 0.811 & 0.836 & 0.853 & 0.855 & \underline{0.984} & 0.848 & 0.839 & 0.790 \\
108	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_transfer.tex-21-OLMo-1B  & 0.811 & 0.827 & 0.837 & 0.852 & 0.803 & \underline{0.988} & 0.828 & 0.763 \\
109	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_transfer.tex-22-Ll-3B    & 0.856 & 0.860 & 0.845 & 0.851 & 0.798 & 0.851 & \underline{0.987} & 0.787 \\
110	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_transfer.tex-23-Mi-7B    & 0.834 & 0.837 & 0.837 & 0.845 & 0.817 & 0.849 & 0.851 & \underline{0.969} \\
111	--
112	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_error_analysis.tex-29-\end{table}
113	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_error_analysis.tex-30-
114	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_error_analysis.tex-31-\paragraph{Per-depth error rates.}
115	artifacts/_project/paper/appendix_error_analysis.tex:32:Error rates decrease monotonically with depth (Table~\ref{tab:error-depth}): depth-2 samples are the primary failure point (48.4\% error rate), followed by depth-3 (29.2\%) and depth-4 (20.3\%).
116	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_error_analysis.tex-33-The monotonic decrease confirms that deeper generations accumulate progressively stronger depth signatures; the gen-1$\to$gen-2 transition is the hardest boundary.
117	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_error_analysis.tex-34-
118	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_error_analysis.tex-35-\begin{table}[H]
119	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_error_analysis.tex-36-\centering
120	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_error_analysis.tex-37-\small
121	artifacts/_project/paper/appendix_error_analysis.tex:38:\caption{Error rate by generation depth in binary classification. Depth-2 exhibits the highest misclassification rate (48.4\%), confirming the gen-1$\to$gen-2 transition as the primary confusion boundary.}
122	artifacts/_project/paper/appendix_error_analysis.tex-39-\label{tab:error-depth}
123	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_error_analysis.tex-40-\begin{tabular}{crrrl}
124	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_error_analysis.tex-41-\toprule
125	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_error_analysis.tex-42-\textbf{Depth} & $N$ & \textbf{Errors} & \textbf{Rate (\%)} & \textbf{Type} \\
126	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_error_analysis.tex-43-\midrule
127	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_error_analysis.tex-44-1 & 7896 & 1130 & 14.3 & FP \\
128	artifacts/_project/paper/appendix_error_analysis.tex:45:2 & 7512 & 3637 & 48.4 & FN \\
129	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_error_analysis.tex-46-3 & 7032 & 2051 & 29.2 & FN \\
130	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_error_analysis.tex-47-4 & 6655 & 1352 & 20.3 & FN \\
131	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_error_analysis.tex-48-\bottomrule
132	--
133	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_finer_depth.tex-10-\toprule
134	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_finer_depth.tex-11-\textbf{Held-out Generator} & \textbf{Macro F1} & \textbf{Weighted F1} & \textbf{Accuracy} \\
135	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_finer_depth.tex-12-\midrule
136	artifacts/_project/paper/appendix_finer_depth.tex:13:OLMo-2-1B       & 0.484 & 0.506 & 0.524 \\
137	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_finer_depth.tex-14-Pythia-1B        & 0.543 & 0.568 & 0.575 \\
138	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_finer_depth.tex-15-Pythia-2.8B      & 0.523 & 0.540 & 0.560 \\
139	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_finer_depth.tex-16-Qwen3-0.6B      & 0.513 & 0.521 & 0.546 \\
140	artifacts/_project/paper/appendix_finer_depth.tex:17:Qwen3-1.7B      & 0.510 & 0.536 & 0.548 \\
141	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_finer_depth.tex-18-Qwen3-8B        & 0.434 & 0.455 & 0.493 \\
142	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_finer_depth.tex-19-\midrule
143	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_finer_depth.tex-20-\textbf{Average} & \textbf{0.501 $\pm$ 0.038} & \textbf{0.521} & \textbf{0.541} \\
144	--
145	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_classifier.tex-70-\midrule
146	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_classifier.tex-71-Pythia-2.8B$^{\dagger}$ & 0.5  & \textbf{0.814} & [.798, .828] & $-0.58$ \\
147	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_classifier.tex-72-Pythia-2.8B$^{\dagger}$ & 0.7  & 0.740 & [.725, .755] & $-0.60$ \\
148	artifacts/_project/paper/appendix_classifier.tex:73:Pythia-2.8B$^{\dagger}$ & 0.9  & 0.480 & [.465, .498] & $-0.30$ \\
149	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_classifier.tex-74-\midrule
150	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_classifier.tex-75-OLMo-2-1B & 0.5  & \textbf{0.783} & [.768, .798] & $-0.72$ \\
151	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_classifier.tex-76-OLMo-2-1B & 0.7  & 0.695 & [.679, .711] & $-0.60$ \\
152	--
153	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/results.tex-43-OLMo-2-1B      & OLMo    & 1.5B & 0.695 & [.679, .711] & 0.781 \\
154	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/results.tex-44-Qwen3-8B       & Qwen    & 8.2B & 0.692 & [.674, .708] & 0.714 \\
155	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/results.tex-45-Qwen3-0.6B     & Qwen    & 0.6B & 0.691 & [.673, .709] & 0.780 \\
156	artifacts/_project/paper/results.tex:46:Mistral-7B     & Mistral & 7.0B & 0.633 & [.617, .648] & 0.682 \\
157	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/results.tex-47-\midrule
158	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/results.tex-48-\multicolumn{3}{l}{\textbf{Average (8-gen LOGO)}} & \textbf{0.694} & [.688, .700] & \textbf{0.762} \\
159	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/results.tex-49-\multicolumn{3}{l}{\textbf{LOFO (family-level)}} & 0.686 & --- & --- \\
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "caee0341-21a9-49c5-a10a-63e3e2fe1ab3",
  "isSidechain": true,
  "promptId": "5c60df84-fcb8-462d-8f59-5098b0a96974",
  "agentId": "a7859a4de84d0a5b2",
  "type": "user",
  "uuid": "bf0172bf-15f7-47fa-99af-8cfdd2d30f8e",
  "sourceToolAssistantUUID": "caee0341-21a9-49c5-a10a-63e3e2fe1ab3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "727cbce6-9768-410b-9211-4635321ab6fe",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-23T19:41:33.509Z_

Perfect! Now let me compile and organize all the findings from my searches:

## Summary of Search Results

I found all five categories of numbers in the .tex files. Here's a comprehensive report:

---

### 1. **0.905 or 0.90** — QLoRA F1

**File:** `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_qlora.tex`

- **Line 19:** `QLoRA (Qwen3-0.6B)   & 0.583 $\pm$ 0.010 & 0.905 $\pm$ 0.003 & 0.999\,/\,0.796\,/\,0.413\,/\,0.259\,/\,0.447 \\`
  - Context (3 lines):
    ```
    \textbf{Method} & \textbf{5-class F1} & \textbf{3-class F1} & \textbf{Per-class F1 (5-class)} \\
    \midrule
    XGBoost (7 features) & 0.501 $\pm$ 0.038 & 0.789 & --- \\
    QLoRA (Qwen3-0.6B)   & 0.583 $\pm$ 0.010 & 0.905 $\pm$ 0.003 & 0.999\,/\,0.796\,/\,0.413\,/\,0.259\,/\,0.447 \\
    ```

- **Line 25:** `QLoRA achieves 3-class LOGO F1\,=\,0.905 ($\pm$0.003) under 6-generator LOGO, a +11.6\,pp improvement over the same-subset XGBoost baseline (0.789).`
  - Context:
    ```
    \end{tabular}}
    \end{table}
    
    \paragraph{Results.}
    QLoRA achieves 3-class LOGO F1\,=\,0.905 ($\pm$0.003) under 6-generator LOGO, a +11.6\,pp improvement over the same-subset XGBoost baseline (0.789).
    On 5-class evaluation, QLoRA reaches F1\,=\,0.583 ($\pm$0.010) vs.\ 0.501 for XGBoost (+8.2\,pp), with the largest gains at gen-1 (0.796 vs.\ 0.634) and gen-2 (0.413 vs.\ 0.268).
    ```

- **Line 30:** `A second run with LoRA rank 32 and seed 123 yields 5-class F1\,=\,0.587 ($\pm$0.005) and 3-class F1\,=\,0.905 ($\pm$0.004), which confirms stability across hyperparameter and seed variation ($\Delta < 1$\,pp on both metrics).`
  - Context:
    ```
    The gen-2/gen-3 boundary remains the primary failure mode (gen-3 F1\,=\,0.259), consistent with the feature-level analysis in \S\ref{sec:discussion}.
    
    \paragraph{Hyperparameter robustness.}
    A second run with LoRA rank 32 and seed 123 yields 5-class F1\,=\,0.587 ($\pm$0.005) and 3-class F1\,=\,0.905 ($\pm$0.004), which confirms stability across hyperparameter and seed variation ($\Delta < 1$\,pp on both metrics).
    ```

**Additional 0.90x matches:**
- **appendix_instruct.tex, Line 87:** `Qwen3-1.7B-Inst  & 0.732 & 0.907\,$\pm$\,0.008 & $+$17.5\,pp & 4{,}963 \\`
- **appendix_instruct.tex, Line 90:** `Qwen3-1.7B (base)&       & 0.904\,$\pm$\,0.009 &             & 2{,}291 \\`
- **appendix_cross_temp.tex, Line 20:** Range `(0.900--0.958)` mentioned for binary F1

---

### 2. **0.789** — XGBoost 3-class F1

**File:** `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_qlora.tex`

- **Line 18:** `XGBoost (7 features) & 0.501 $\pm$ 0.038 & 0.789 & --- \\`
  - Context:
    ```
    \textbf{Method} & \textbf{5-class F1} & \textbf{3-class F1} & \textbf{Per-class F1 (5-class)} \\
    \midrule
    XGBoost (7 features) & 0.501 $\pm$ 0.038 & 0.789 & --- \\
    QLoRA (Qwen3-0.6B)   & 0.583 $\pm$ 0.010 & 0.905 $\pm$ 0.003 & 0.999\,/\,0.796\,/\,0.413\,/\,0.259\,/\,0.447 \\
    ```

- **Line 25:** `QLoRA achieves 3-class LOGO F1\,=\,0.905 ($\pm$0.003) under 6-generator LOGO, a +11.6\,pp improvement over the same-subset XGBoost baseline (0.789).`

**Additional 0.789 matches:**
- **appendix_cross_model_detail.tex, Line 6:** Caption mentions `macro F1\,=\,0.789` (under natural class distribution)
- **appendix_cross_model_detail.tex, Line 14:** `gen-2+  & 0.842 & 0.742 & 0.789 & [.768, .809] \\`
- **appendix_classifier.tex, Line 17:** `XGBoost          & 0.789 & 0.764 & ...`
- **appendix_lofo.tex, Line 20:** `Full (7 features) & 0.789 & ---`

---

### 3. **0.487** — Instruct LOGO Binary F1

**File:** `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_instruct.tex`

- **Line 50:** `Three-generator instruct LOGO yields binary F1\,=\,0.487, indicating weak cross-generator transfer under instruction tuning.`
  - Context:
    ```
    Retraining recovers substantial within-model performance ($+$6.8--26.9\,pp), but the retrained F1 (0.590--0.660) remains below base-model levels (0.69--0.72).
    Three-generator instruct LOGO yields binary F1\,=\,0.487, indicating weak cross-generator transfer under instruction tuning.
    
    \paragraph{DDR structure under instruction tuning.}
    ```

**Also in limitations.tex, Line 6:** `LOGO binary F1\,=\,0.487`

---

### 4. **3-4, 3--4, ±3, batch, prevalence** — Prevalence Estimation Error

**File:** `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/conclusion.tex`

- **Line 8:** `QLoRA recovery (F1\,=\,0.89--0.91) suggests tractable extension to instruct models; DDR connects depth profiling to model collapse analysis and corpus auditing (${\pm}3$--$4$\% batch estimation; Appendix~\ref{app:error-analysis}).`
  - Context:
    ```
    \looseness=-2 Recursive generation produces a decomposable depth response---location features drift while shape is approximately preserved---enabling cross-generator depth classification (F1\,=\,0.694--0.762) within the base-model scope.
    Cross-model chains confirm generalization across architectures (F1\,=\,0.830; ANOVA: depth explains ${>}48{\times}$ more variance than generator identity).
    QLoRA recovery (F1\,=\,0.89--0.91) suggests tractable extension to instruct models; DDR connects depth profiling to model collapse analysis and corpus auditing (${\pm}3$--$4$\% batch estimation; Appendix~\ref{app:error-analysis}).
    ```

---

### 5. **48, >48, 48×, 48\\times** — Variance Ratio

**File:** `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/conclusion.tex`

- **Line 7:** `Cross-model chains confirm generalization across architectures (F1\,=\,0.830; ANOVA: depth explains ${>}48{\times}$ more variance than generator identity).`
  - Context:
    ```
    \looseness=-2 Recursive generation produces a decomposable depth response---location features drift while shape is approximately preserved---enabling cross-generator depth classification (F1\,=\,0.694--0.762) within the base-model scope.
    Cross-model chains confirm generalization across architectures (F1\,=\,0.830; ANOVA: depth explains ${>}48{\times}$ more variance than generator identity).
    QLoRA recovery (F1\,=\,0.89--0.91) suggests tractable extension to instruct models; DDR connects depth profiling to model collapse analysis and corpus auditing (${\pm}3$--$4$\% batch estimation; Appendix~\ref{app:error-analysis}).
    ```

**Additional match related to error rates:**
- **appendix_error_analysis.tex, Line 45:** `2 & 7512 & 3637 & 48.4 & FN \\` (depth-2 error rate of 48.4%)

---

All five categories have been located with full context. The key metrics are concentrated in the appendices (QLoRA, instruct models, and error analysis) and in the conclusion section.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bf0172bf-15f7-47fa-99af-8cfdd2d30f8e",
  "isSidechain": true,
  "agentId": "a7859a4de84d0a5b2",
  "requestId": "req_011CbL4zU3wYmPxkcQHoJwq9",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "fff32ed7-8102-4608-8a24-f9915c773835",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "727cbce6-9768-410b-9211-4635321ab6fe",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01YLuuEfbe2zknPZZJV1esVe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 11097,
      "cache_read_input_tokens": 32847,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11097,
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
