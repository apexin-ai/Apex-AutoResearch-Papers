# audit numbers group1 abstract intro method — Part 2 of 2

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Worker execution logs

[← Part 1](part-001.md) · [Transcript overview](../audit-numbers-group1-abstract-intro-method.md) · [Structured JSON](../../../sessions/02/02c3bcf5ede54ce3a99c.json)

## Round 1

### Tool result

_source line 142 · 2026-05-25T19:57:09.194Z_

<details><summary>↩ Tool result · `toolu_016dvHALgycG9JK1rwrgJ7Kv`</summary>

```text
1	\paragraph{Training Data.}
2	We sample a 132M-token subset of FineWeb~\citep{penedo2024fineweb} as the real-data source, comparable to typical domain-adaptive continued pretraining budgets~\citep{gururangan2020dont}.
3	To simulate web-scale synthetic contamination, we generate continuations with Qwen3-0.6B~\citep{yang2025qwen3}, the same architecture used for continued pretraining, and inject them at token-level ratio $\rho = 0.4$ via uniform random mixing.\footnote{$\rho$ denotes the token-level contamination ratio. Because synthetic documents are shorter on average (304 vs.\ 560 words), the document-level synthetic fraction is 55.6\% at $\rho{=}0.4$.}
4	This self-contamination design means generator and trainee share the same distribution, providing a controlled testbed with known ground-truth labels but limiting ecological validity; cross-model transfer results (Appendix~\ref{app:cross_model}) are mixed, and we discuss implications for detection difficulty in \S\ref{sec:limitations}.
5	
6	\paragraph{Detector.}
7	We train a TF-IDF + Logistic Regression classifier on a held-out labeled split (AUC\,=\,0.94, calibrated ECE\,=\,0.048 after temperature scaling with $T{=}0.204$).
8	The resulting $q$-scores have mean 0.60, standard deviation 0.37, and median 0.71, with 46.3\% of samples in the uncertain range $[0.2, 0.8]$.
9	We use this lightweight detector rather than neural alternatives (e.g., ModernBERT at AUC\,${\geq}$\,0.98 in \citealt{drayson2025detection}) to test whether score \emph{calibration} may matter as much as raw discrimination for reweighting.
10	To evaluate detector sensitivity, we additionally test two generative baselines: a GPT-2-based perplexity scorer (AUC\,=\,0.91) and an N-gram language model perplexity scorer (AUC\,=\,0.73); results are reported in \S\ref{sec:robustness} (implementation details in Appendix~\ref{app:detector_details}).
11	
12	\paragraph{Training.}
13	Table~\ref{tab:config} summarizes the training configuration.
14	We use $B{=}4$ as the default micro-batch size, reflecting memory constraints typical of continued pretraining setups; \S\ref{sec:sensitivity} demonstrates that larger batches amplify the adaptive advantage.
15	All main comparisons use three random seeds (42, 123, 456) trained from scratch (Appendix~\ref{app:resume_artifact}); the primary comparison is extended to five seeds (adding 789, 234).
16	
17	\begin{table}[t]
18	\centering
19	\small
20	\begin{tabular}{@{}ll@{\hspace{8pt}}ll@{}}
21	\toprule
22	Model & Qwen3-0.6B & Optimizer & AdamW \\
23	Steps & 6{,}103 & Peak LR & $5{\times}10^{-5}$ \\
24	Micro-batch & $B{=}4$ & Schedule & linear + warmup \\
25	Grad.\ accum. & 4 ($B_{\mathrm{eff}}{=}16$) & Seq.\ len. & 2048 \\
26	Precision & bf16 & GPU & 1$\times$ RTX PRO 6000 \\
27	\bottomrule
28	\end{tabular}
29	\caption{Training configuration for continued pretraining.}
30	\label{tab:config}
31	\end{table}
32	
33	\paragraph{Evaluation.}
34	We report held-out perplexity (PPL) on 5{,}000 documents from a FineWeb holdout set ($\sim$4M tokens) containing only human-authored text, via sliding-window evaluation (stride 1024).
35	All evaluations are post-hoc with a unified pipeline; training involves no inline evaluation.
36	
37	\paragraph{Methods.}
38	We compare six approaches:
39	\begin{itemize}[nosep,leftmargin=*]
40	  \item \textbf{Uniform}: $w_j = 1$ for all $j$ (no contamination handling).
41	  \item \textbf{Grid-$b$}: fixed $b \in \{0.1, 0.2, 0.3, 0.5, 1.0, 1.5, 2.0, 3.0, 5.0\}$ (nine candidates), best selected post-hoc by held-out PPL.
42	        Represents validation-based selection~\citep{drayson2025detection}.
43	  \item \textbf{ESS-only}: $\bstar = \max\{b : \mathrm{ESS}(b) \geq \nmin\}$, the maximum-intervention variant retaining only the stability constraint, ablating $\aeff$.
44	  \item \textbf{Golden Ratio}: $w = 1/\varphi \approx 0.618$ for synthetic ($q_j > 0.5$), $w = 1$ otherwise~\citep{he2025golden}.
45	        Requires known provenance labels (oracle).
46	  \item \textbf{Adaptive} (ours): per-batch $\bstar$ from the dual-constraint formulation (\S\ref{sec:method}), with $\tau = 0.7$ (default; $\tau{=}0.8$ comparable, \S\ref{sec:sensitivity}) and $\nmin = 2$ (half the micro-batch size).
47	  \item \textbf{Detect \& Remove}: hard filtering that discards samples with $q_j > 0.5$ and trains uniformly on the remainder.
48	        Requires a calibrated detection threshold; threshold sensitivity is analyzed in \S\ref{sec:main-results}.
49	\end{itemize}
50	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da",
  "uuid": "b605526f-8807-4285-a164-2f375a67c387",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/experiments.tex",
      "content": "\\paragraph{Training Data.}\nWe sample a 132M-token subset of FineWeb~\\citep{penedo2024fineweb} as the real-data source, comparable to typical domain-adaptive continued pretraining budgets~\\citep{gururangan2020dont}.\nTo simulate web-scale synthetic contamination, we generate continuations with Qwen3-0.6B~\\citep{yang2025qwen3}, the same architecture used for continued pretraining, and inject them at token-level ratio $\\rho = 0.4$ via uniform random mixing.\\footnote{$\\rho$ denotes the token-level contamination ratio. Because synthetic documents are shorter on average (304 vs.\\ 560 words), the document-level synthetic fraction is 55.6\\% at $\\rho{=}0.4$.}\nThis self-contamination design means generator and trainee share the same distribution, providing a controlled testbed with known ground-truth labels but limiting ecological validity; cross-model transfer results (Appendix~\\ref{app:cross_model}) are mixed, and we discuss implications for detection difficulty in \\S\\ref{sec:limitations}.\n\n\\paragraph{Detector.}\nWe train a TF-IDF + Logistic Regression classifier on a held-out labeled split (AUC\\,=\\,0.94, calibrated ECE\\,=\\,0.048 after temperature scaling with $T{=}0.204$).\nThe resulting $q$-scores have mean 0.60, standard deviation 0.37, and median 0.71, with 46.3\\% of samples in the uncertain range $[0.2, 0.8]$.\nWe use this lightweight detector rather than neural alternatives (e.g., ModernBERT at AUC\\,${\\geq}$\\,0.98 in \\citealt{drayson2025detection}) to test whether score \\emph{calibration} may matter as much as raw discrimination for reweighting.\nTo evaluate detector sensitivity, we additionally test two generative baselines: a GPT-2-based perplexity scorer (AUC\\,=\\,0.91) and an N-gram language model perplexity scorer (AUC\\,=\\,0.73); results are reported in \\S\\ref{sec:robustness} (implementation details in Appendix~\\ref{app:detector_details}).\n\n\\paragraph{Training.}\nTable~\\ref{tab:config} summarizes the training configuration.\nWe use $B{=}4$ as the default micro-batch size, reflecting memory constraints typical of continued pretraining setups; \\S\\ref{sec:sensitivity} demonstrates that larger batches amplify the adaptive advantage.\nAll main comparisons use three random seeds (42, 123, 456) trained from scratch (Appendix~\\ref{app:resume_artifact}); the primary comparison is extended to five seeds (adding 789, 234).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{@{}ll@{\\hspace{8pt}}ll@{}}\n\\toprule\nModel & Qwen3-0.6B & Optimizer & AdamW \\\\\nSteps & 6{,}103 & Peak LR & $5{\\times}10^{-5}$ \\\\\nMicro-batch & $B{=}4$ & Schedule & linear + warmup \\\\\nGrad.\\ accum. & 4 ($B_{\\mathrm{eff}}{=}16$) & Seq.\\ len. & 2048 \\\\\nPrecision & bf16 & GPU & 1$\\times$ RTX PRO 6000 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Training configuration for continued pretraining.}\n\\label{tab:config}\n\\end{table}\n\n\\paragraph{Evaluation.}\nWe report held-out perplexity (PPL) on 5{,}000 documents from a FineWeb holdout set ($\\sim$4M tokens) containing only human-authored text, via sliding-window evaluation (stride 1024).\nAll evaluations are post-hoc with a unified pipeline; training involves no inline evaluation.\n\n\\paragraph{Methods.}\nWe compare six approaches:\n\\begin{itemize}[nosep,leftmargin=*]\n  \\item \\textbf{Uniform}: $w_j = 1$ for all $j$ (no contamination handling).\n  \\item \\textbf{Grid-$b$}: fixed $b \\in \\{0.1, 0.2, 0.3, 0.5, 1.0, 1.5, 2.0, 3.0, 5.0\\}$ (nine candidates), best selected post-hoc by held-out PPL.\n        Represents validation-based selection~\\citep{drayson2025detection}.\n  \\item \\textbf{ESS-only}: $\\bstar = \\max\\{b : \\mathrm{ESS}(b) \\geq \\nmin\\}$, the maximum-intervention variant retaining only the stability constraint, ablating $\\aeff$.\n  \\item \\textbf{Golden Ratio}: $w = 1/\\varphi \\approx 0.618$ for synthetic ($q_j > 0.5$), $w = 1$ otherwise~\\citep{he2025golden}.\n        Requires known provenance labels (oracle).\n  \\item \\textbf{Adaptive} (ours): per-batch $\\bstar$ from the dual-constraint formulation (\\S\\ref{sec:method}), with $\\tau = 0.7$ (default; $\\tau{=}0.8$ comparable, \\S\\ref{sec:sensitivity}) and $\\nmin = 2$ (half the micro-batch size).\n  \\item \\textbf{Detect \\& Remove}: hard filtering that discards samples with $q_j > 0.5$ and trains uniformly on the remainder.\n        Requires a calibrated detection threshold; threshold sensitivity is analyzed in \\S\\ref{sec:main-results}.\n\\end{itemize}\n",
      "numLines": 50,
      "startLine": 1,
      "totalLines": 50
    }
  }
}
```

</details>

---


### Tool call

_source line 143_

<details open><summary>🔧 Tool call — Agent · `toolu_01AamVR2RZtHDNmSaawtTB6q`</summary>

```json
{
  "description": "Verify D&R threshold in results",
  "prompt": "I need to verify what threshold the paper uses for D&R results in the main results table. Read these files and find the main results table, looking specifically for what D&R PPL values are reported and at what thresholds:\n\n1. `/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/results.tex` (if it exists)\n2. Any file matching `*results*` or `*main*` in `/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/`\n\nAlso search for \"17.250\" and \"17.25\" across all .tex files in the paper directory to find all occurrences.\n\nAlso search for \"5.9\" across all .tex files to find where the 5.9x claim originates and how it might be computed.\n\nReport the exact text and line numbers.",
  "subagent_type": "Explore"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da",
  "uuid": "d85d744a-36f4-4b46-9bea-d0e8334d86be",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PcCDWZSJP7pbXzJqRBpXub",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1673,
      "cache_read_input_tokens": 41052,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1673
      },
      "output_tokens": 35,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### System

_source line 144_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "a77822597a2053a5c",
  "tool_use_id": "toolu_01AamVR2RZtHDNmSaawtTB6q",
  "description": "Verify D&R threshold in results",
  "task_type": "local_agent",
  "prompt": "I need to verify what threshold the paper uses for D&R results in the main results table. Read these files and find the main results table, looking specifically for what D&R PPL values are reported and at what thresholds:\n\n1. `/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/results.tex` (if it exists)\n2. Any file matching `*results*` or `*main*` in `/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/`\n\nAlso search for \"17.250\" and \"17.25\" across all .tex files in the paper directory to find all occurrences.\n\nAlso search for \"5.9\" across all .tex files to find where the 5.9x claim originates and how it might be computed.\n\nReport the exact text and line numbers.",
  "uuid": "b6be2299-3934-467b-aa9c-7270ab5c6653",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da"
}
```

---


## Round 2

## Round 2

42 recorded events


### User

_source line 145 · 2026-05-25T19:57:19.747Z_

I need to verify what threshold the paper uses for D&R results in the main results table. Read these files and find the main results table, looking specifically for what D&R PPL values are reported and at what thresholds:

1. `/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/results.tex` (if it exists)
2. Any file matching `*results*` or `*main*` in `/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/`

Also search for "17.250" and "17.25" across all .tex files in the paper directory to find all occurrences.

Also search for "5.9" across all .tex files to find where the 5.9x claim originates and how it might be computed.

Report the exact text and line numbers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01AamVR2RZtHDNmSaawtTB6q",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da",
  "uuid": "401e7c45-0981-4a88-8316-46cb3d527893"
}
```

</details>

---


### System

_source line 146_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a77822597a2053a5c",
  "tool_use_id": "toolu_01AamVR2RZtHDNmSaawtTB6q",
  "description": "Finding /home/ubuntu/.agent-ml-research-idea_gen_0509_10/…",
  "usage": {
    "total_tokens": 19419,
    "tool_uses": 1,
    "duration_ms": 2104
  },
  "last_tool_name": "Glob",
  "uuid": "c86bfdad-450d-41f2-beb6-90b0a5949353",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da"
}
```

---


### Tool call

_source line 147_

<details open><summary>🔧 Tool call — Glob · `toolu_014K2pQev5SGTHoX27xq2e1n`</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/**/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01AamVR2RZtHDNmSaawtTB6q",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da",
  "uuid": "f5ab622c-e34f-477e-b524-6ab07e08a994",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01SH5u3KRiC4QhdQQBZZXzqR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 19402,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 19402,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 7,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### System

_source line 148_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a77822597a2053a5c",
  "tool_use_id": "toolu_01AamVR2RZtHDNmSaawtTB6q",
  "description": "Running find /home/ubuntu/.agent-ml-research-idea_gen_050…",
  "usage": {
    "total_tokens": 19426,
    "tool_uses": 2,
    "duration_ms": 2113
  },
  "last_tool_name": "Bash",
  "uuid": "d30fce8f-e6d2-477b-af7e-8b412520c1cb",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da"
}
```

---


### Tool call

_source line 149_

<details open><summary>🔧 Tool call — Bash · `toolu_014NQ7U5m2KRmEYU1qia3QRj`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper -type f -name \"*.tex\" | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01AamVR2RZtHDNmSaawtTB6q",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da",
  "uuid": "4d2f8f11-db4f-4a78-be4c-b14ea829d4b9",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01SH5u3KRiC4QhdQQBZZXzqR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 19402,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 19402,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 7,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 150 · 2026-05-25T19:57:21.874Z_

<details><summary>↩ Tool result · `toolu_014K2pQev5SGTHoX27xq2e1n`</summary>

```text
docs/paper/sections/checklist.tex
docs/paper/sections/introduction.tex
docs/paper/sections/experiments.tex
docs/paper/sections/abstract.tex
docs/paper/sections/method.tex
docs/paper/sections/limitations.tex
docs/paper/sections/conclusion.tex
docs/paper/sections/appendix.tex
docs/paper/sections/discussion.tex
docs/paper/sections/results.tex
docs/paper/sections/related_work.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01AamVR2RZtHDNmSaawtTB6q",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da",
  "uuid": "2bff2768-682d-4b9f-801a-169490b0ea83"
}
```

</details>

---


### Tool result

_source line 151 · 2026-05-25T19:57:21.919Z_

<details><summary>↩ Tool result · `toolu_014NQ7U5m2KRmEYU1qia3QRj`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/results.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/checklist.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01AamVR2RZtHDNmSaawtTB6q",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da",
  "uuid": "f36aef4a-2e7a-4f5e-8bb5-043ac98af44d"
}
```

</details>

---


### System

_source line 152_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a77822597a2053a5c",
  "tool_use_id": "toolu_01AamVR2RZtHDNmSaawtTB6q",
  "description": "Reading docs/paper/sections/results.tex",
  "usage": {
    "total_tokens": 21109,
    "tool_uses": 3,
    "duration_ms": 4145
  },
  "last_tool_name": "Read",
  "uuid": "fe78fcb9-3896-453e-8e45-ac90a801397d",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da"
}
```

---


### Tool call

_source line 153_

<details open><summary>🔧 Tool call — Read · `toolu_01HGG31JMSWsRUM6omVQjY5p`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01AamVR2RZtHDNmSaawtTB6q",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da",
  "uuid": "bce5907a-8f45-4ff7-8b30-c25f2b808b33",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01WLMioVnb3bzkaWm3Fwr1Dj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1677,
      "cache_read_input_tokens": 19402,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1677,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 154 · 2026-05-25T19:57:23.898Z_

<details><summary>↩ Tool result · `toolu_01HGG31JMSWsRUM6omVQjY5p`</summary>

```text
1	\begin{table}[t]
2	\centering
3	\small
4	\setlength{\tabcolsep}{3pt}
5	\resizebox{\columnwidth}{!}{%
6	\begin{tabular}{@{}lcccc@{}}
7	\toprule
8	\textbf{Method} & \textbf{Seed 42} & \textbf{Seed 123} & \textbf{Seed 456} & \textbf{Mean} \\
9	\midrule
10	Uniform                & 17.694 & 17.686 & 17.702 & 17.697 $\pm$ .008 \\
11	Adaptive $\bstar$ (ours) & \textbf{17.680} & \textbf{17.666} & \textbf{17.677} & \textbf{17.674} $\pm$ .006 \\
12	ESS-only               & 17.730 & 17.720 & 17.760 & 17.737 $\pm$ .021 \\
13	Random $\mathcal{U}(0,2)$ & 17.830 & 17.800 & 17.777 & 17.802 $\pm$ .027 \\
14	Permuted $q$-scores  & 17.919 & --     & --     & 17.919 \\
15	\bottomrule
16	\end{tabular}}
17	\caption{Main comparison: held-out PPL ($\downarrow$) at $\rho{=}0.4$, 1 content epoch.
18	Adaptive and Uniform: 5-seed means (seeds 42, 123, 456, 789, 234); ESS-only and Random: 3-seed means (seeds 42, 123, 456); Permuted: single seed (42).
19	Adaptive uses $\tau{=}0.7$, $\nmin{=}2$.
20	Permuted randomly shuffles $q$-scores across samples, destroying provenance signal while preserving weight non-uniformity ($\Delta{=}{+}0.225$).}
21	\label{tab:main}
22	\end{table}
23	
24	\subsection{Main Results}
25	\label{sec:main-results}
26	
27	Table~\ref{tab:main} reports held-out perplexity at $\rho = 0.4$ across five seeds.
28	Continued pretraining reduces PPL from 22.970 to the 17.3--17.8 range; method comparisons operate within a narrow residual.
29	
30	Adaptive $\bstar$ achieves 5-seed mean PPL 17.674, compared to 17.697 for uniform ($\Delta{=}{-}0.023$, directionally consistent across all seeds) and 17.620 for grid $b{=}0.3$ (3-seed mean, post-hoc oracle; gap $+$0.054; Table~\ref{tab:aux}).
31	A paired $t$-test yields $t(4){=}{-}8.21$, $p{=}0.0012$; after Bonferroni--Holm correction for nine family-wise comparisons, $p_{\mathrm{BH}}{=}0.011$, reaching conventional significance at $\alpha{=}0.05$.
32	The engineering benefit is eliminating $b$ grid search (nine full training runs~\citep{drayson2025detection}, ${\sim}$16 GPU-hours at 0.6B scale, scaling linearly with model size), though grid search yields a larger improvement.
33	The grid-best $b{=}0.3$ is a post-hoc oracle from nine candidates with $5.5{\times}$ higher cross-seed standard deviation than adaptive ($\sigma{=}0.033$ vs.\ $0.006$); the noisy PPL plateau at $b \in [0.1, 0.5]$ (Figure~\ref{fig:grid_b_trend}) makes validation-based selection unreliable.
34	At the nearest fixed point ($b{=}1.0$), PPL equals uniform (17.692 vs.\ 17.694): per-batch adaptation is essential.
35	
36	The ablation hierarchy at $\rho{=}0.4$ (Adaptive ${<}$ Uniform ${<}$ ESS-only ${<}$ Random ${<}$ Permuted, Table~\ref{tab:main}) reveals two requirements for effective reweighting: detector signal and minimum intervention.
37	Random weights $\mathcal{U}(0,2)$ (17.802) confirm that non-uniform weighting alone does not help; permuted $q$-scores (17.919, $\Delta{=}{+}0.225$) further isolate provenance signal as load-bearing, since shuffling destroys the detector's sample-level information while preserving identical weight non-uniformity.
38	ESS-only (mean $17.737 {\pm} 0.021$) uses the same $q$-scores but maximizes $b$ up to the stability ceiling, concentrating weights on a few high-confidence samples; it degrades PPL by 0.043 relative to uniform.
39	Only the dual-constrained adaptive method, which limits $b$ to the minimum needed, improves in-distribution PPL over uniform (mean $\Delta{=}{-}0.023$, directionally consistent across all seeds).
40	Figure~\ref{fig:grid_b_trend} contextualizes both results: adaptive $\bstar$ operates near the curve minimum while ESS-only $\bstar$ (mean ${\approx}$3.5) falls in the degradation zone.
41	
42	\begin{figure}[t]
43	\centering
44	\includegraphics[width=\columnwidth]{grid_b_trend_clean}
45	\caption{Held-out PPL as a function of fixed sharpening exponent $b$ (grid search, $\rho{=}0.4$).
46	Seed\,42 provides the full nine-point sweep (circles); cross-seed markers at $b{=}0.5$ (triangles) confirm the plateau region.
47	The shaded region marks $b \geq 2$ where PPL degrades past the uniform baseline; ESS-only $\bstar$ (overall mean ${\approx}$3.5) falls in this degradation zone, while adaptive $\bstar$ (mean ${\approx}$0.9) operates near the curve minimum.}
48	\label{fig:grid_b_trend}
49	\end{figure}
50	
51	\paragraph{Hard filtering and multi-epoch exposure.}
52	Detect \& Remove at its best threshold ($q{>}0.3$) achieves 3-seed mean PPL $17.250 \pm 0.001$ at full training length, outperforming all reweighting methods by a wide margin ($\Delta{=}{-}0.424$ vs.\ adaptive $\bstar$).
53	All three D\&R thresholds beat both uniform and adaptive $\bstar$ ($q{>}0.5$: $17.280 \pm 0.010$; $q{>}0.7$: $17.320 \pm 0.001$; 3 seeds each), with cross-seed variance near zero (holdout $\pm$0.00, Table~\ref{tab:epoch_match}).
54	Aggressive filtering retains only 31.5\% of tokens at $q{>}0.3$, so the model sees surviving data ${\sim}$3.2 \emph{content epochs} versus one for reweighting; an epoch-matched control (D\&R at $q{>}0.5$, ${\sim}$1.0 content epochs) yields PPL $17.657 \pm 0.005$ vs.\ $17.674 \pm 0.007$ for adaptive $\bstar$ ($\Delta{=}0.017$), attributing ${>}$95\% of D\&R's full-length advantage to multi-epoch exposure on filtered data (Table~\ref{tab:epoch_match}).
55	This decomposition identifies the \emph{mechanism}: filtering concentrates compute on high-confidence real data, and multi-epoch exposure amplifies the benefit, rather than undermining D\&R's practical effectiveness.
56	The raw threshold--PPL curve is U-shaped ($q{>}0.3$: 17.25, $q{>}0.9$: 17.42), but epoch-matched comparisons eliminate the U-shape, revealing monotonically decreasing PPL that saturates at $q{\geq}0.5$ (Figure~\ref{fig:dr_dual_curve}; Appendix~\ref{app:hybrid}).
57	For practitioners, D\&R is the strongest strategy when the corpus is small relative to training compute, as aggressive filtering naturally creates multi-epoch regimes that amplify quality gains; controlled comparisons should report the effective content-epoch count alongside PPL.
58	
59	\begin{figure}[t]
60	\centering
61	\includegraphics[width=\columnwidth]{dr_dual_curve}
62	\caption{D\&R threshold--PPL relationship ($\rho{=}0.4$, 3 seeds).
63	Blue: raw (multi-epoch) PPL with effective epoch counts annotated.
64	Orange: epoch-matched PPL (single content epoch), saturating at the adaptive $\bstar$ level (green dashed).}
65	\label{fig:dr_dual_curve}
66	\end{figure}
67	
68	\begin{figure}[t]
69	\centering
70	\includegraphics[width=\columnwidth]{delta_vs_rho}
71	\caption{Effect of contamination ratio on adaptive reweighting effectiveness.
72	$\Delta$ = adaptive $-$ uniform holdout PPL (lower is better).
73	Error bars show $\pm$1 SD across seeds.
74	The method transitions from harmful to beneficial between $\rho{=}0.3$ and $0.4$ (shaded).}
75	\label{fig:delta_vs_rho}
76	\end{figure}
77	
78	\subsection{Robustness and Boundary Conditions}
79	\label{sec:robustness}
80	
81	Across three seeds at $\rho = 0.6$, adaptive $\bstar$ ($17.731 \pm 0.004$) directionally outperforms uniform on in-distribution PPL ($17.763 \pm 0.008$, $\Delta{=}{-}0.032$, 3 seeds, paired $t{=}{-}9.95$, $p_{\mathrm{BH}}{=}0.064$), with a larger effect size than at $\rho{=}0.4$ ($\Delta{=}{-}0.023$).
82	The ablation hierarchy is preserved (Grid 17.634\footnote{Single seed; full per-seed results in Appendix~\ref{app:rho06}.} ${<}$ Adaptive 17.731 ${<}$ Uniform 17.763 ${\approx}$ ESS-only 17.763 ${<}$ Random 17.861), but the ESS-only/uniform gap collapses to effectively zero (three-seed means both $17.763$) as ESS binding rises to ${\sim}$49\%.
83	Random remains substantially worse than uniform (gap 0.098, $\sigma{=}0.025$): detector signal is load-bearing even when the stability constraint dominates; the adaptive method's continued advantage is driven by the $\aeff$ quality constraint, which operates independently of the ESS ceiling.
84	Three-seed paired comparison confirms $\tau{=}0.7$ outperforms $\tau{=}0.8$ on both holdout and out-of-distribution (OOD) metrics (\S\ref{sec:sensitivity}).
85	
86	\begin{table}[t]
87	\centering
88	\small
89	\setlength{\tabcolsep}{3pt}
90	\resizebox{\columnwidth}{!}{%
91	\begin{tabular}{@{}lccc@{}}
92	\toprule
93	\textbf{Method} & \textbf{Epochs} & \textbf{PPL (raw)} $\downarrow$ & \textbf{PPL (ep.-matched)} $\downarrow$ \\
94	\midrule
95	D\&R ($q{>}0.3$) & ${\sim}$3.2 & \textbf{17.250} $\pm$ .001 & 17.74 \\
96	D\&R ($q{>}0.5$) & ${\sim}$2.4 & 17.280 $\pm$ .010 & 17.657 $\pm$ .005 \\
97	D\&R ($q{>}0.7$) & ${\sim}$2.0 & 17.32 & 17.62 \\
98	\midrule
99	Adaptive $\bstar$ & ${\sim}$1.0 & \multicolumn{2}{c}{17.674 $\pm$ .007} \\
100	Uniform           & ${\sim}$1.0 & \multicolumn{2}{c}{17.697 $\pm$ .008} \\
101	\bottomrule
102	\end{tabular}}
103	\caption{D\&R threshold comparison ($\rho{=}0.4$).
104	Raw PPL traces a U-shape across thresholds; epoch-matched PPL (single content epoch) decreases monotonically and saturates near the adaptive $\bstar$ level.
105	D\&R's 0.424 PPL advantage (at $q{>}0.3$) shrinks to $\Delta{=}0.017$ when content epochs are equalized.
106	All raw PPL values are 3-seed means; epoch-matched values at $q{>}0.3$ and $q{>}0.7$ are single-seed.
107	Full 9-threshold sweep in Table~\ref{tab:dr_threshold}.}
108	\label{tab:epoch_match}
109	\end{table}
110	
111	\paragraph{Scale.}
112	At 1.7B parameters (Qwen3-1.7B, $\rho{=}0.4$, $\tau{=}0.8$, 3 seeds), the method scales without degradation but the benefit diminishes.
113	Adaptive $\bstar$ achieves holdout PPL $13.26$ vs.\ uniform $13.27$ ($\Delta{=}{-}0.013$); OOD results are mixed in direction across domains (OWT $\Delta{=}{-}0.008$, Wiki $\Delta{=}{+}0.013$) and downstream accuracy is unchanged ($\Delta{\approx}{+}0.002$).
114	The diminished effect is consistent with larger models being more robust to self-generated contamination: Qwen3-1.7B's own outputs are likely closer to its training distribution, reducing the distributional shift that reweighting corrects.
115	A preliminary Llama-3.2-3B cross-model result (Appendix~\ref{app:cross_model}) shows mixed downstream effects (MMLU $+$1.6 percentage points, HellaSwag $-$0.6 percentage points), leaving cross-architecture generalization as an open question.
116	\paragraph{Out-of-distribution evaluation.}
117	To test whether the in-distribution improvement reflects distribution matching, we evaluate all three from-scratch seeds on OpenWebText and Wikipedia.
118	At $\rho{=}0.4$, adaptive reweighting improves mean PPL on all three evaluation domains: FineWeb $\Delta{=}{-}0.023$ (5 seeds), OpenWebText $\Delta{=}{-}0.028$, Wikipedia $\Delta{=}{-}0.029$ (3 seeds each); downstream accuracy is identical (0.5414).
119	OOD improvements exceed the in-distribution gain, indicating genuine quality improvement rather than distribution matching toward the training mixture ($\tau{=}0.8$'s OOD effect is smaller; $\tau{=}0.7$'s advantage reflects active OOD improvement, \S\ref{sec:sensitivity}).
120	
121	\paragraph{Calibration, not just discrimination.}
122	Replacing TF-IDF+LR with generative perplexity detectors reverses the advantage across three seeds (GPT-2: AUC\,=\,0.91, ECE\,=\,0.131, $\Delta{=}{+}0.098$; N-gram: AUC\,=\,0.73, ECE\,=\,0.069, $\Delta{=}{+}0.129$; Figure~\ref{fig:overview}b; Appendix~\ref{app:detector}).
123	The TF-IDF vs.\ GPT-2 contrast (comparable AUC, $2.7{\times}$ ECE gap) isolates calibration as an empirically observed requirement in our self-contamination setting; N-gram's better ECE (0.069) does not compensate for insufficient AUC (0.73), indicating that both discrimination and calibration are jointly necessary (Figure~\ref{fig:overview}b).
124	
125	\begin{table}[t]
126	\centering
127	\small
128	\setlength{\tabcolsep}{3pt}
129	\resizebox{\columnwidth}{!}{%
130	\begin{tabular}{@{}lcccl@{}}
131	\toprule
132	\textbf{Method} & \textbf{Seeds} & \textbf{Oracle?} & \textbf{Epochs} & \textbf{Mean PPL} $\downarrow$ \\
133	\midrule
134	Grid ($b{=}0.3$) & 3 & post-hoc & 1 & \textbf{17.620} $\pm$ .033 \\
135	Golden Ratio     & 1 & known $\rho$ & 1 & 17.654 \\
136	D\&R ($q{>}0.3$) & 3 & post-hoc & ${\sim}$3.2 & \textbf{17.250} $\pm$ .001 \\
137	\bottomrule
138	\end{tabular}}
139	\caption{Auxiliary baselines at $\rho{=}0.4$. Grid-best selected post-hoc from nine candidates (Appendix~\ref{app:grid}). Golden Ratio requires known $\rho$~\citep{he2025golden}. D\&R uses ${\sim}$3.2 content epochs (Table~\ref{tab:epoch_match}).}
140	\label{tab:aux}
141	\end{table}
142	
143	\subsection{Hyperparameter Sensitivity}
144	\label{sec:sensitivity}
145	
146	\paragraph{Quality threshold $\tau$.}
147	$\tau{=}0.7$ outperforms $\tau{=}0.8$ on holdout at both contamination levels ($\rho{=}0.4$: 17.674 vs.\ 17.683; $\rho{=}0.6$: paired $t{=}{-}4.70$, $p{<}0.05$; \S\ref{sec:robustness}) and achieves larger OOD gains ($\rho{=}0.4$: $\Delta{=}{-}0.028$/$-$0.029 vs.\ $-$0.005/$-$0.009; Table~\ref{tab:tau}, Appendix~\ref{app:tau_rho}).
148	$\tau \in [0.5, 0.8]$ all improve holdout over uniform, while $\tau {>} 0.8$ degrades (Appendix~\ref{app:tau_sweep}).
149	We also tested per-batch adaptive $\tau$ clamping, which did not improve over fixed thresholds (Appendix~\ref{app:batch_adaptive}).
150	
151	\paragraph{ESS floor $\nmin$.}
152	The default $\nmin{=}2$ ($\nmin/B{=}0.5$) is optimal; extremes degrade ($\nmin{=}1$: PPL $17.742{\pm}0.009$, 3 seeds, worse than uniform; $\nmin{=}B$: recovers uniform).
153	Neither constraint alone improves over uniform ($\nmin{=}1$: $+$0.048; ESS-only: $+$0.043); both must act jointly for the method to outperform uniform training.
154	The coupling $\nmin{=}\lfloor B/2 \rfloor$ is also empirically motivated: at $B{=}8$, keeping $\nmin{=}2$ (ratio $0.25$) degrades PPL by $+$0.036 vs.\ uniform, whereas $\nmin{=}4$ (ratio $0.5$) yields $\Delta{=}{-}0.052{\pm}0.007$.
155	Under this coupling, the adaptive advantage monotonically increases across $B \in \{4, 8, 16\}$: $\Delta{=}{-}0.023{\pm}0.006$ (5 seeds), $-$0.052${\pm}$0.007 (3 seeds, $p{=}0.006$), and $-$0.068${\pm}$0.005 (3 seeds), corresponding to $1.0{\times}$, $2.3{\times}$, and $3.0{\times}$ amplification ($p{<}0.01$ at $B \geq 8$).
156	The gap to grid-best narrows from 0.040 ($B{=}4$) to 0.009 ($B{=}16$, seed\,42; Figure~\ref{fig:batch_amp}).
157	
158	\begin{figure}[t]
159	\centering
160	\includegraphics[width=\columnwidth]{batch_size_amplification}
161	\caption{Batch-size amplification of adaptive reweighting ($\nmin{=}\lfloor B/2 \rfloor$).
162	The adaptive advantage over uniform increases monotonically with micro-batch size, from $1.0{\times}$ ($B{=}4$) to $3.0{\times}$ ($B{=}16$); $\Delta$ values and $\pm$1\,SD shown above each bar.}
163	\label{fig:batch_amp}
164	\end{figure}
165	
166	\paragraph{Constraint regime.}
167	\label{sec:regime}
168	Over 24{,}412 micro-batches (seed\,42), 5.8\% are clean ($\aeff(0) \geq \tau$, $\bstar{=}0$), ${\sim}$50\% are $\aeff$-binding (quality constraint dominates), and ${\sim}$44\% are ESS-binding (stability constraint dominates); the distribution is stable across seeds (coefficient of variation ${<}2\%$; Figure~\ref{fig:regime_decomp}).
169	The $\aeff$-binding majority indicates that detector quality signal, not training stability, is the primary bottleneck, reinforcing the calibration requirement (\S\ref{sec:robustness}).
170	
171	\begin{figure}[t]
172	\centering
173	\includegraphics[width=\columnwidth]{constraint_regime_decomposition}
174	\caption{Constraint regime decomposition at two contamination levels (seed\,42).
175	At $\rho{=}0.4$, ${\sim}$50\% of batches are $\aeff$-binding and ${\sim}$44\% ESS-binding, with ${\sim}$6\% clean; at $\rho{=}0.6$, the constraints are nearly balanced (${\sim}$49\% ESS-binding, ${\sim}$47\% $\aeff$-binding).}
176	\label{fig:regime_decomp}
177	\end{figure}
178	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01AamVR2RZtHDNmSaawtTB6q",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da",
  "uuid": "fba92180-4cbd-4f9e-9f51-353a1b22272c"
}
```

</details>

---


### System

_source line 155_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a77822597a2053a5c",
  "tool_use_id": "toolu_01AamVR2RZtHDNmSaawtTB6q",
  "description": "Searching for 17\\.250|17\\.25",
  "usage": {
    "total_tokens": 21110,
    "tool_uses": 4,
    "duration_ms": 4985
  },
  "last_tool_name": "Grep",
  "uuid": "72fb8dc0-3c2b-4999-a381-99c812e2fe0a",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da"
}
```

---


### Tool call

_source line 156_

<details open><summary>🔧 Tool call — Grep · `toolu_011ikFaioFzamsdD6QjkDcYF`</summary>

```json
{
  "pattern": "17\\.250|17\\.25",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper",
  "type": "tex",
  "output_mode": "content",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01AamVR2RZtHDNmSaawtTB6q",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da",
  "uuid": "f8d751b2-5a0b-45b8-8c88-0ac60fa545c5",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01WLMioVnb3bzkaWm3Fwr1Dj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1677,
      "cache_read_input_tokens": 19402,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1677,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 157 · 2026-05-25T19:57:24.745Z_

<details><summary>↩ Tool result · `toolu_011ikFaioFzamsdD6QjkDcYF`</summary>

```text
docs/paper/sections/appendix.tex:159:Raw PPL traces a U-shaped curve with a minimum at $q{>}0.3$ (17.250, 3 seeds), but this curve conflates filtering quality with multi-epoch exposure: aggressive thresholds retain less data and repeat it more often.
docs/paper/sections/appendix.tex:174:Detect \& Remove ($q{>}0.3$) & 17.250 & -- \\
docs/paper/sections/appendix.tex:192:$q > 0.3$ & 31.5\% & ${\sim}$3.2 & \textbf{17.250}$^\dagger$ & 17.74 \\
docs/paper/sections/appendix.tex:203:$^\dagger$\,3-seed mean $17.250 \pm 0.001$.}
docs/paper/sections/introduction.tex:26:D\&R outperforms all reweighting methods in our setting (PPL $17.250$ vs.\ $17.674$, 3 seeds); epoch-matched controls attribute ${>}$95\% of the advantage to multi-epoch exposure on filtered data, reducing the gap to $\Delta{=}0.017$ (Table~\ref{tab:epoch_match}).
docs/paper/sections/results.tex:52:Detect \& Remove at its best threshold ($q{>}0.3$) achieves 3-seed mean PPL $17.250 \pm 0.001$ at full training length, outperforming all reweighting methods by a wide margin ($\Delta{=}{-}0.424$ vs.\ adaptive $\bstar$).
docs/paper/sections/results.tex:56:The raw threshold--PPL curve is U-shaped ($q{>}0.3$: 17.25, $q{>}0.9$: 17.42), but epoch-matched comparisons eliminate the U-shape, revealing monotonically decreasing PPL that saturates at $q{\geq}0.5$ (Figure~\ref{fig:dr_dual_curve}; Appendix~\ref{app:hybrid}).
docs/paper/sections/results.tex:95:D\&R ($q{>}0.3$) & ${\sim}$3.2 & \textbf{17.250} $\pm$ .001 & 17.74 \\
docs/paper/sections/results.tex:136:D\&R ($q{>}0.3$) & 3 & post-hoc & ${\sim}$3.2 & \textbf{17.250} $\pm$ .001 \\
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01AamVR2RZtHDNmSaawtTB6q",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da",
  "uuid": "65e3854f-3018-406f-bc48-a4874ef52eb9"
}
```

</details>

---


### System

_source line 158_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a77822597a2053a5c",
  "tool_use_id": "toolu_01AamVR2RZtHDNmSaawtTB6q",
  "description": "Searching for 5\\.9",
  "usage": {
    "total_tokens": 21111,
    "tool_uses": 5,
    "duration_ms": 5406
  },
  "last_tool_name": "Grep",
  "uuid": "d4306b91-a534-49db-91c5-3bc436b4d985",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da"
}
```

---


### Tool call

_source line 159_

<details open><summary>🔧 Tool call — Grep · `toolu_01AuaBXsWodSiVkkmvqQpxm6`</summary>

```json
{
  "pattern": "5\\.9",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper",
  "type": "tex",
  "output_mode": "content",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01AamVR2RZtHDNmSaawtTB6q",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da",
  "uuid": "6b52fa0e-f2c3-4136-87c7-72ae1fd69ab6",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01WLMioVnb3bzkaWm3Fwr1Dj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1677,
      "cache_read_input_tokens": 19402,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1677,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 160 · 2026-05-25T19:57:25.172Z_

<details><summary>↩ Tool result · `toolu_01AuaBXsWodSiVkkmvqQpxm6`</summary>

```text
docs/paper/sections/appendix.tex:313:456 & 0.8006 & 0.8749 & 5.9 \\
docs/paper/sections/introduction.tex:32:An $\aeff$ quality constraint binds in ${\sim}$50\% of batches at ${\approx}5.9{\times}$ lower sharpening exponents than an ESS-only alternative (\S\ref{sec:regime}); at $\rho{=}0.6$, ESS-only collapses toward uniform while the dual constraint maintains its advantage.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01AamVR2RZtHDNmSaawtTB6q",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da",
  "uuid": "dc2eedbe-babd-4c86-bbe2-988663c512e8"
}
```

</details>

---


### System

_source line 161_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a77822597a2053a5c",
  "tool_use_id": "toolu_01AamVR2RZtHDNmSaawtTB6q",
  "description": "Reading docs/paper/sections/appendix.tex",
  "usage": {
    "total_tokens": 28498,
    "tool_uses": 6,
    "duration_ms": 9172
  },
  "last_tool_name": "Read",
  "uuid": "4ebf6bfa-68a0-44d3-8e34-0407ada7c7fd",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da"
}
```

---


### Tool call

_source line 162_

<details open><summary>🔧 Tool call — Read · `toolu_01Ejpm6MCr1kCcosroLCtdxV`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/appendix.tex",
  "offset": 150,
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01AamVR2RZtHDNmSaawtTB6q",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da",
  "uuid": "657b321a-e228-4c7e-8696-f817dfa860cc",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01FAHN15fAf1mmN1Df1nFm6i",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 7379,
      "cache_read_input_tokens": 21079,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7379,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 163 · 2026-05-25T19:57:28.924Z_

<details><summary>↩ Tool result · `toolu_01Ejpm6MCr1kCcosroLCtdxV`</summary>

```text
150	(b) Normalized PPL gap relative to uniform at shared $\tau$ values.}
151	\label{fig:tau_rho_rank}
152	\end{figure}
153	
154	\section{Hybrid and Threshold Comparison}
155	\label{app:hybrid}
156	
157	Table~\ref{tab:hybrid} compares method families across contamination levels.
158	Table~\ref{tab:dr_threshold} shows D\&R sensitivity to the detection threshold at both full training length and epoch-matched settings.
159	Raw PPL traces a U-shaped curve with a minimum at $q{>}0.3$ (17.250, 3 seeds), but this curve conflates filtering quality with multi-epoch exposure: aggressive thresholds retain less data and repeat it more often.
160	Epoch-matched comparisons (rightmost column of Table~\ref{tab:dr_threshold}) remove the multi-epoch confound: the U-shape vanishes and PPL decreases monotonically, saturating near the adaptive $\bstar$ level at $q{\geq}0.5$.
161	Figure~\ref{fig:dr_dual_curve} visualizes the two curves.
162	
163	\begin{table}[h]
164	\centering
165	\small
166	\begin{tabular}{@{}lcc@{}}
167	\toprule
168	\textbf{Method} & $\rho{=}0.4$ & $\rho{=}0.6$ \\
169	\midrule
170	Uniform & 17.694 & 17.766 \\
171	Adaptive $\bstar$ & 17.689 & 17.740 \\
172	Hybrid ($q{>}0.95$ + adaptive) & 17.514 & 17.530$^*$ \\
173	Detect \& Remove ($q{>}0.5$) & 17.285 & -- \\
174	Detect \& Remove ($q{>}0.3$) & 17.250 & -- \\
175	\bottomrule
176	\end{tabular}
177	\caption{Method comparison across contamination levels (seed\,42, $\tau{=}0.8$).
178	$^*$Hybrid at $\rho{=}0.6$ filters high-confidence synthetic ($q{>}0.95$), reducing effective $\rho$ to ${\approx}0.4$; PPL is not directly comparable to $\rho{=}0.6$ baselines.}
179	\label{tab:hybrid}
180	\end{table}
181	
182	\begin{table}[h]
183	\centering
184	\small
185	\setlength{\tabcolsep}{3pt}
186	\begin{tabular}{@{}ccccc@{}}
187	\toprule
188	\textbf{Thresh.} & \textbf{Ret.\ \%} & \textbf{Epochs} & \textbf{Raw PPL} $\downarrow$ & \textbf{Ep.-matched} $\downarrow$ \\
189	\midrule
190	$q > 0.1$ & 15.0\% & ${\sim}$10.0 & 17.40 & 18.04 \\
191	$q > 0.2$ & ${\sim}$23\% & ${\sim}$5.0 & 17.27 & -- \\
192	$q > 0.3$ & 31.5\% & ${\sim}$3.2 & \textbf{17.250}$^\dagger$ & 17.74 \\
193	$q > 0.4$ & ${\sim}$38\% & ${\sim}$2.8 & 17.26 & -- \\
194	$q > 0.5$ & 41.4\% & ${\sim}$2.4 & 17.28 & 17.65 \\
195	$q > 0.6$ & ${\sim}$46\% & ${\sim}$1.7 & 17.30 & -- \\
196	$q > 0.7$ & 49.8\% & ${\sim}$2.0 & 17.32 & 17.62 \\
197	$q > 0.8$ & ${\sim}$56\% & ${\sim}$1.3 & 17.34 & -- \\
198	$q > 0.9$ & 61.6\% & ${\sim}$1.1 & 17.42 & 17.628 \\
199	\bottomrule
200	\end{tabular}
201	\caption{D\&R threshold sensitivity ($\rho{=}0.4$, seed\,42 unless noted).
202	Raw PPL traces a U-shaped curve (minimum at $q{>}0.3$); epoch-matched PPL (single content epoch) decreases monotonically and saturates near the adaptive $\bstar$ level (${\approx}$17.65) at $q{\geq}0.5$; the U-shape is thus a multi-epoch artifact.
203	$^\dagger$\,3-seed mean $17.250 \pm 0.001$.}
204	\label{tab:dr_threshold}
205	\end{table}
206	
207	See Figure~\ref{fig:dr_dual_curve} (\S\ref{sec:main-results}) for the dual-curve visualization.
208	
209	\section{Downstream Task Evaluation}
210	\label{app:downstream}
211	
212	Table~\ref{tab:downstream} reports downstream benchmark accuracy for adaptive vs.\ uniform training at $\rho{=}0.4$ (seed\,42, Qwen3-0.6B).
213	Across multiple seeds, downstream differences are mixed in direction and uniformly within standard error, indicating that adaptive reweighting has no meaningful downstream impact.
214	
215	\begin{table}[h]
216	\centering
217	\small
218	\resizebox{\columnwidth}{!}{%
219	\begin{tabular}{@{}llccc@{}}
220	\toprule
221	\textbf{Benchmark} & \textbf{Metric} & \textbf{Adaptive} & \textbf{Uniform} & $\boldsymbol{\Delta}$ \\
222	\midrule
223	\multicolumn{5}{@{}l}{\textit{Seed 42 (checkpoint resume)}} \\
224	ARC-Challenge & acc\_norm & 0.343 & 0.348 & $-$0.005 \\
225	ARC-Easy & acc & 0.650 & 0.657 & $-$0.007 \\
226	HellaSwag & acc\_norm & 0.479 & 0.484 & $-$0.005 \\
227	PIQA & acc & 0.687 & 0.686 & $+$0.001 \\
228	WinoGrande & acc & 0.578 & 0.586 & $-$0.008 \\
229	\midrule
230	\multicolumn{5}{@{}l}{\textit{From-scratch 2-seed mean (seeds 123, 456)}} \\
231	\multicolumn{3}{@{}l}{Mean $\Delta$ across 5 tasks} & & $+$0.001 \\
232	\multicolumn{3}{@{}l}{Direction} & \multicolumn{2}{c}{mixed (seed 123: 3/5$-$; seed 456: 3/5$+$)} \\
233	\bottomrule
234	\end{tabular}}
235	\caption{Downstream benchmarks (Qwen3-0.6B, $\rho{=}0.4$).
236	Seed\,42 used a checkpoint-resumed adaptive model; from-scratch seeds (123, 456) show mixed direction with mean $|\Delta| \leq 0.01$.
237	All differences within standard error ($\pm 0.01$).
238	Models use $\tau{=}0.8$; $\tau{=}0.7$ yields identical 3-seed means (0.5414).}
239	\label{tab:downstream}
240	\end{table}
241	
242	\section{Higher Contamination Details}
243	\label{app:rho06}
244	
245	Table~\ref{tab:rho06} reports results at $\rho{=}0.6$.
246	The full five-method ablation preserves the hierarchy from $\rho{=}0.4$ across all three seeds: Grid ${<}$ Adaptive ${<}$ Uniform ${\approx}$ ESS-only ${<}$ Random.
247	
248	\begin{table}[h]
249	\centering
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01AamVR2RZtHDNmSaawtTB6q",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da",
  "uuid": "cf6e2e9c-4489-4a34-b5fe-e30e7ef3b1dc"
}
```

</details>

---


### System

_source line 164_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a77822597a2053a5c",
  "tool_use_id": "toolu_01AamVR2RZtHDNmSaawtTB6q",
  "description": "Reading docs/paper/sections/appendix.tex",
  "usage": {
    "total_tokens": 28502,
    "tool_uses": 7,
    "duration_ms": 9392
  },
  "last_tool_name": "Read",
  "uuid": "60b7ec30-a065-429e-b543-9828780a358f",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da"
}
```

---


### Tool call

_source line 165_

<details open><summary>🔧 Tool call — Read · `toolu_01A4xJMDBhwhN2aYTc6VBZ11`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/appendix.tex",
  "offset": 300,
  "limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01AamVR2RZtHDNmSaawtTB6q",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da",
  "uuid": "f638d7d6-c4dc-4f4a-a620-c931db72757a",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01FAHN15fAf1mmN1Df1nFm6i",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 7379,
      "cache_read_input_tokens": 21079,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7379,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 166 · 2026-05-25T19:57:29.143Z_

<details><summary>↩ Tool result · `toolu_01A4xJMDBhwhN2aYTc6VBZ11`</summary>

```text
300	
301	\paragraph{Cross-seed stability.}
302	Table~\ref{tab:alpha_corr_perseed} reports the correlation between $\aeff$ and the batch mean $q$-score ($\bar{q}$, computed from known labels) across all three seeds.
303	
304	\begin{table}[h]
305	\centering
306	\small
307	\begin{tabular}{@{}cccc@{}}
308	\toprule
309	\textbf{Seed} & Pearson $r(\aeff, \bar{q})$ & Spearman $\rho_s$ & $\bstar{=}0$ (\%) \\
310	\midrule
311	42  & 0.8019 & 0.8761 & 5.8 \\
312	123 & 0.7994 & 0.8692 & 5.7 \\
313	456 & 0.8006 & 0.8749 & 5.9 \\
314	\midrule
315	\textbf{Spread} & 0.0025 & 0.0069 & 0.2 \\
316	\bottomrule
317	\end{tabular}
318	\caption{Per-seed $\aeff$--$\bar{q}$ correlation ($\rho{=}0.4$, $B{=}4$).
319	Cross-seed spread is $<$0.003 for Pearson $r$ and $<$0.007 for Spearman $\rho_s$, indicating stable proxy fidelity across random seeds.
320	$r(\aeff, \bar{q}) = 0.80$ measures the proxy's fidelity to batch composition; the ground-truth correlation $r(\aeff, \text{true real fraction}) \approx 0.79$ (\S\ref{sec:discussion}) is slightly lower due to detector noise.
321	The per-seed table demonstrates cross-seed stability rather than superseding the ground-truth estimate.}
322	\label{tab:alpha_corr_perseed}
323	\end{table}
324	
325	\section{Detector Comparison}
326	\label{app:detector}
327	
328	See Figure~\ref{fig:overview}b (\S\ref{sec:robustness}) for the detector requirements visualization.
329	
330	Table~\ref{tab:detector} compares three detector families for adaptive reweighting.
331	The discriminative TF-IDF+LR detector (ECE\,=\,0.048) produces the only improvement over uniform.
332	The TF-IDF vs.\ GPT-2 contrast (comparable AUC: 0.94 vs.\ 0.91, but $2.7{\times}$ ECE gap: 0.048 vs.\ 0.131) isolates calibration as an empirically observed requirement; however, N-gram's better ECE (0.069) does not compensate for its low AUC (0.73); both sufficient discrimination and good calibration are jointly necessary in our setting.
333	TF-IDF+LR's $q$-scores have reliable probabilistic semantics, so the $\aeff$ proxy accurately tracks batch quality.
334	Generative detectors assign high $q$-scores to fluent, predictable human text (false positives concentrated among high-quality samples), systematically inflating $\aeff$ for clean batches and deflating it for contaminated ones, which inverts the minimum-intervention logic.
335	
336	\begin{table}[h]
337	\centering
338	\small
339	\resizebox{\columnwidth}{!}{%
340	\begin{tabular}{@{}llccccc@{}}
341	\toprule
342	\textbf{Detector} & \textbf{Type} & \textbf{AUC} & \textbf{ECE} & \textbf{Mean PPL} & $\boldsymbol{\Delta}$ \\
343	\midrule
344	TF-IDF+LR & Discriminative & 0.94 & 0.048 & 17.650{\tiny$\pm$.010} & $-$0.044 \\
345	GPT-2 PPL & Generative & 0.91 & 0.131 & 17.792{\tiny$\pm$.005} & $+$0.098 \\
346	N-gram PPL & Generative & 0.73 & 0.069 & 17.823{\tiny$\pm$.003} & $+$0.129 \\
347	\bottomrule
348	\end{tabular}}
349	\caption{Detector comparison for adaptive reweighting ($\rho{=}0.4$, $\tau{=}0.8$, 3 seeds).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01AamVR2RZtHDNmSaawtTB6q",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da",
  "uuid": "3e92f02a-4ec2-4b53-aa72-128164a3b25a"
}
```

</details>

---


### System

_source line 167_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a77822597a2053a5c",
  "tool_use_id": "toolu_01AamVR2RZtHDNmSaawtTB6q",
  "description": "Searching for sharpening exponent|constraint regime|5\\.8|5\\.9|5…",
  "usage": {
    "total_tokens": 32408,
    "tool_uses": 8,
    "duration_ms": 12153
  },
  "last_tool_name": "Grep",
  "uuid": "4c39cd6e-53e6-4c4f-b2f8-6cb0dc85f85d",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da"
}
```

---


### Tool call

_source line 168_

<details open><summary>🔧 Tool call — Grep · `toolu_01WYWfSquRCjb4D7wmyfBUWH`</summary>

```json
{
  "pattern": "sharpening exponent|constraint regime|5\\.8|5\\.9|5\\.7",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper",
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
  "type": "assistant",
  "parent_tool_use_id": "toolu_01AamVR2RZtHDNmSaawtTB6q",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da",
  "uuid": "1154a9b2-0bf9-4b5b-84c9-12b8f7f168d2",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_013t1nUiAo9AHiM3tT9NJ4L4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3892,
      "cache_read_input_tokens": 28458,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3892,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 7,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 169 · 2026-05-25T19:57:31.935Z_

<details><summary>↩ Tool result · `toolu_01WYWfSquRCjb4D7wmyfBUWH`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/method.tex-6-\end{figure}
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/method.tex-7-
docs/paper/sections/method.tex-8-Figure~\ref{fig:pipeline} illustrates the pipeline. Let $\mathcal{D}$ denote a pretraining corpus with unknown synthetic contamination ratio $\rho$~\citep{cheng2025contamination}.
docs/paper/sections/method.tex:9:A detector assigns each sample $x$ a synthetic probability $q(x) \in [0,1]$; following \citet{drayson2025detection}, we weight each sample as $w(x) = (1 - q(x))^{b}$, where $b \geq 0$ is a sharpening exponent ($b{=}0$ recovers uniform training).
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/method.tex-10-Rather than selecting $b$ via grid search, we derive $b$ per-batch from the batch's $q$-score distribution using two opposing constraints.
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/method.tex-11-
docs/paper/sections/method.tex-12-Given a batch $\mathcal{B} = \{x_1, \ldots, x_B\}$ with scores $q_i = q(x_i)$ and weights $w_i(b) = (1 - q_i)^{b}$:
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/results.tex-42-\begin{figure}[t]
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/results.tex-43-\centering
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/results.tex-44-\includegraphics[width=\columnwidth]{grid_b_trend_clean}
docs/paper/sections/results.tex:45:\caption{Held-out PPL as a function of fixed sharpening exponent $b$ (grid search, $\rho{=}0.4$).
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/results.tex-46-Seed\,42 provides the full nine-point sweep (circles); cross-seed markers at $b{=}0.5$ (triangles) confirm the plateau region.
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/results.tex-47-The shaded region marks $b \geq 2$ where PPL degrades past the uniform baseline; ESS-only $\bstar$ (overall mean ${\approx}$3.5) falls in this degradation zone, while adaptive $\bstar$ (mean ${\approx}$0.9) operates near the curve minimum.}
docs/paper/sections/results.tex-48-\label{fig:grid_b_trend}
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/results.tex-165-
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/results.tex-166-\paragraph{Constraint regime.}
docs/paper/sections/results.tex-167-\label{sec:regime}
docs/paper/sections/results.tex:168:Over 24{,}412 micro-batches (seed\,42), 5.8\% are clean ($\aeff(0) \geq \tau$, $\bstar{=}0$), ${\sim}$50\% are $\aeff$-binding (quality constraint dominates), and ${\sim}$44\% are ESS-binding (stability constraint dominates); the distribution is stable across seeds (coefficient of variation ${<}2\%$; Figure~\ref{fig:regime_decomp}).
docs/paper/sections/results.tex-169-The $\aeff$-binding majority indicates that detector quality signal, not training stability, is the primary bottleneck, reinforcing the calibration requirement (\S\ref{sec:robustness}).
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/results.tex-170-
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/results.tex-171-\begin{figure}[t]
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/introduction.tex-1-The detect-and-reweight paradigm~\citep{drayson2025detection} has emerged as a response to synthetic contamination in web corpora, now estimated at 20--60\% of crawled data~\citep{cheng2025contamination}.
docs/paper/sections/introduction.tex:2:Training on such data risks model collapse~\citep{shumailov2024model,dohmatob2025strong}, motivating methods that downweight likely-synthetic samples via $w(x) = (1 - q(x))^b$, where $q(x)$ is a detector's synthetic probability and $b$ is a sharpening exponent.
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/introduction.tex-3-An alternative, Detect and Remove (D\&R), hard-filters samples above a threshold~\citep{feng2025beyond}.
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/introduction.tex-4-
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/introduction.tex-5-\begin{figure*}[t]
--
docs/paper/sections/introduction.tex-29-Both sufficient discrimination (area under the ROC curve; AUC) and good calibration (expected calibration error; ECE) are empirically observed requirements in our self-contamination setting; a high-AUC but poorly calibrated detector degrades performance below uniform (3 detectors, 3 seeds; \S\ref{sec:robustness}).
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/introduction.tex-30-
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/introduction.tex-31-\item \textbf{Minimum intervention outperforms maximization.}
docs/paper/sections/introduction.tex:32:An $\aeff$ quality constraint binds in ${\sim}$50\% of batches at ${\approx}5.9{\times}$ lower sharpening exponents than an ESS-only alternative (\S\ref{sec:regime}); at $\rho{=}0.6$, ESS-only collapses toward uniform while the dual constraint maintains its advantage.
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/introduction.tex-33-\end{itemize}
docs/paper/sections/introduction.tex-34-To demonstrate the minimum-intervention principle, we derive a dual-constrained adaptive $\bstar$ that eliminates per-model grid search ($\Delta{=}{-}0.023$ at $\rho{=}0.4$, $-$0.032 at $\rho{=}0.6$; Table~\ref{tab:main}), with transferable defaults ($\tau{=}0.7$, $\nmin{=}\lfloor B/2 \rfloor$).
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/introduction.tex-35-The method fails at $\rho{=}0.2$; at 1.7B it shows no degradation but the benefit diminishes.
--
docs/paper/sections/appendix.tex-52-\label{alg:bstar}
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/appendix.tex-53-\begin{algorithmic}[1]
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/appendix.tex-54-\REQUIRE Batch scores $\{q_i\}_{i=1}^{B}$, threshold~$\tau$, ESS floor~$n_{\min}$, bound~$b_{\max}$, tol.~$\varepsilon$
docs/paper/sections/appendix.tex:55:\ENSURE Optimal sharpening exponent $b^{*}$
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/appendix.tex-56-\IF{$\alpha_{\mathrm{eff}}(0) \geq \tau$}
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/appendix.tex-57-  \STATE \textbf{return} $0$ \COMMENT{clean batch}
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/appendix.tex-58-\ENDIF
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/appendix.tex-308-\toprule
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/appendix.tex-309-\textbf{Seed} & Pearson $r(\aeff, \bar{q})$ & Spearman $\rho_s$ & $\bstar{=}0$ (\%) \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/appendix.tex-310-\midrule
docs/paper/sections/appendix.tex:311:42  & 0.8019 & 0.8761 & 5.8 \\
docs/paper/sections/appendix.tex:312:123 & 0.7994 & 0.8692 & 5.7 \\
docs/paper/sections/appendix.tex:313:456 & 0.8006 & 0.8749 & 5.9 \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/appendix.tex-314-\midrule
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/appendix.tex-315-\textbf{Spread} & 0.0025 & 0.0069 & 0.2 \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/appendix.tex-316-\bottomrule
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01AamVR2RZtHDNmSaawtTB6q",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da",
  "uuid": "75c1f17f-8c68-4a82-8d26-4e1eb3956f18"
}
```

</details>

---


### System

_source line 170_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a77822597a2053a5c",
  "tool_use_id": "toolu_01AamVR2RZtHDNmSaawtTB6q",
  "description": "Searching for ESS-only.*mean|ratio|amplification.*exponent|bsta…",
  "usage": {
    "total_tokens": 35694,
    "tool_uses": 9,
    "duration_ms": 14664
  },
  "last_tool_name": "Grep",
  "uuid": "14a1442d-a45e-481c-8ae8-2e1813fc5473",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da"
}
```

---


### Tool call

_source line 171_

<details open><summary>🔧 Tool call — Grep · `toolu_01CGHLXoSea93WDBuguCfv6p`</summary>

```json
{
  "pattern": "ESS-only.*mean|ratio|amplification.*exponent|bstar.*ESS|lower.*exponent",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper",
  "type": "tex",
  "output_mode": "content",
  "context": 5
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01AamVR2RZtHDNmSaawtTB6q",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da",
  "uuid": "be1769d4-eff9-44c4-aaff-fabe38a5b14a",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_014SjnQm61sWzqBTdU57dPCA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 3285,
      "cache_read_input_tokens": 32350,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3285,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 172 · 2026-05-25T19:57:34.444Z_

<details><summary>↩ Tool result · `toolu_01CGHLXoSea93WDBuguCfv6p`</summary>

```text
&lt;persisted-output>
Output too large (44.8KB). Full output saved to: /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/3aaca442-e705-47db-9f84-980fe61c25da/tool-results/toolu_01CGHLXoSea93WDBuguCfv6p.txt

Preview (first 2KB):
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/related_work.tex-1-\paragraph{Synthetic Contamination and Model Collapse.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/related_work.tex-2-Training on recursively generated data leads to irreversible quality degradation (\emph{model collapse})~\citep{shumailov2024model}.
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/related_work.tex-3-\citet{alemohammad2024mad} formalize this as Model Autophagy Disorder, showing that quality inevitably degrades without fresh real data.
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/related_work.tex-4-More critically, \citet{dohmatob2025strong} prove under scaling-law regimes that even a vanishingly small synthetic fraction suffices to trigger collapse, ruling out data scaling as a remedy.
docs/paper/sections/related_work.tex:5:\citet{cheng2025contamination} confirm that synthetic content now constitutes an estimated 20--60\% of web corpora, though accumulating real data avoids divergence~\citep{kazdan2025collapse} and even minimal curation suffices~\citep{amin2025escaping}.
docs/paper/sections/related_work.tex:6:Not all synthetic data is harmful: the Phi series~\citep{gunasekar2023textbooks,li2023textbooks2} demonstrates that curated synthetic data can improve training efficiency, but this assumes intentional generation with quality control, unlike the uncontrolled web contamination we address.
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/related_work.tex-7-
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/related_work.tex-8-\paragraph{Detection, Filtering, and Data Reweighting.}
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01AamVR2RZtHDNmSaawtTB6q",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da",
  "uuid": "9a55ebcc-2f0d-4db0-8bdd-5fb8fd1a9102"
}
```

</details>

---


### System

_source line 173_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a77822597a2053a5c",
  "tool_use_id": "toolu_01AamVR2RZtHDNmSaawtTB6q",
  "description": "Searching for adaptive.*mean.*0\\.9|ESS-only.*mean.*3\\.5|3\\.5.*E…",
  "usage": {
    "total_tokens": 36616,
    "tool_uses": 10,
    "duration_ms": 17287
  },
  "last_tool_name": "Grep",
  "uuid": "03082155-d176-4547-aa97-a77033713cc9",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da"
}
```

---


### Tool call

_source line 174_

<details open><summary>🔧 Tool call — Grep · `toolu_01PQ3mdm7nMTj99QidyU1fJi`</summary>

```json
{
  "pattern": "adaptive.*mean.*0\\.9|ESS-only.*mean.*3\\.5|3\\.5.*ESS|0\\.9.*adaptive",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper",
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
  "type": "assistant",
  "parent_tool_use_id": "toolu_01AamVR2RZtHDNmSaawtTB6q",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da",
  "uuid": "a8a9e7ba-abd1-439c-9b21-9f60b5b89787",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01PfmaFPMVfFPypQyFR4somx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 921,
      "cache_read_input_tokens": 35635,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 921,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 175 · 2026-05-25T19:57:37.064Z_

<details><summary>↩ Tool result · `toolu_01PQ3mdm7nMTj99QidyU1fJi`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/appendix.tex-169-\midrule
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/appendix.tex-170-Uniform & 17.694 & 17.766 \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/appendix.tex-171-Adaptive $\bstar$ & 17.689 & 17.740 \\
docs/paper/sections/appendix.tex:172:Hybrid ($q{>}0.95$ + adaptive) & 17.514 & 17.530$^*$ \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/appendix.tex-173-Detect \& Remove ($q{>}0.5$) & 17.285 & -- \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/appendix.tex-174-Detect \& Remove ($q{>}0.3$) & 17.250 & -- \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/appendix.tex-175-\bottomrule
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/results.tex-37-Random weights $\mathcal{U}(0,2)$ (17.802) confirm that non-uniform weighting alone does not help; permuted $q$-scores (17.919, $\Delta{=}{+}0.225$) further isolate provenance signal as load-bearing, since shuffling destroys the detector's sample-level information while preserving identical weight non-uniformity.
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/results.tex-38-ESS-only (mean $17.737 {\pm} 0.021$) uses the same $q$-scores but maximizes $b$ up to the stability ceiling, concentrating weights on a few high-confidence samples; it degrades PPL by 0.043 relative to uniform.
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/results.tex-39-Only the dual-constrained adaptive method, which limits $b$ to the minimum needed, improves in-distribution PPL over uniform (mean $\Delta{=}{-}0.023$, directionally consistent across all seeds).
docs/paper/sections/results.tex:40:Figure~\ref{fig:grid_b_trend} contextualizes both results: adaptive $\bstar$ operates near the curve minimum while ESS-only $\bstar$ (mean ${\approx}$3.5) falls in the degradation zone.
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/results.tex-41-
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/results.tex-42-\begin{figure}[t]
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/results.tex-43-\centering
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/results.tex-44-\includegraphics[width=\columnwidth]{grid_b_trend_clean}
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/results.tex-45-\caption{Held-out PPL as a function of fixed sharpening exponent $b$ (grid search, $\rho{=}0.4$).
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/results.tex-46-Seed\,42 provides the full nine-point sweep (circles); cross-seed markers at $b{=}0.5$ (triangles) confirm the plateau region.
docs/paper/sections/results.tex:47:The shaded region marks $b \geq 2$ where PPL degrades past the uniform baseline; ESS-only $\bstar$ (overall mean ${\approx}$3.5) falls in this degradation zone, while adaptive $\bstar$ (mean ${\approx}$0.9) operates near the curve minimum.}
docs/paper/sections/results.tex-48-\label{fig:grid_b_trend}
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/results.tex-49-\end{figure}
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/results.tex-50-
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01AamVR2RZtHDNmSaawtTB6q",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da",
  "uuid": "ad66142b-f544-4ff2-a16e-1c5b6a92700f"
}
```

</details>

---


### System

_source line 176_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a77822597a2053a5c",
  "tool_use_id": "toolu_01AamVR2RZtHDNmSaawtTB6q",
  "description": "Reading docs/paper/sections/results.tex",
  "usage": {
    "total_tokens": 38211,
    "tool_uses": 11,
    "duration_ms": 19605
  },
  "last_tool_name": "Read",
  "uuid": "ef910d1d-1c36-4665-b06b-9eccbb8e245c",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da"
}
```

---


### Tool call

_source line 177_

<details open><summary>🔧 Tool call — Read · `toolu_01Fod1m8kbPFRC6eEutdMcPQ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/results.tex",
  "offset": 1,
  "limit": 60
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01AamVR2RZtHDNmSaawtTB6q",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da",
  "uuid": "2a2a66cb-169a-449f-b17c-b00fba844d5d",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_015k7JmhiVNdtr8EtfYjm2EU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1587,
      "cache_read_input_tokens": 36556,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1587,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 178 · 2026-05-25T19:57:39.358Z_

<details><summary>↩ Tool result · `toolu_01Fod1m8kbPFRC6eEutdMcPQ`</summary>

```text
1	\begin{table}[t]
2	\centering
3	\small
4	\setlength{\tabcolsep}{3pt}
5	\resizebox{\columnwidth}{!}{%
6	\begin{tabular}{@{}lcccc@{}}
7	\toprule
8	\textbf{Method} & \textbf{Seed 42} & \textbf{Seed 123} & \textbf{Seed 456} & \textbf{Mean} \\
9	\midrule
10	Uniform                & 17.694 & 17.686 & 17.702 & 17.697 $\pm$ .008 \\
11	Adaptive $\bstar$ (ours) & \textbf{17.680} & \textbf{17.666} & \textbf{17.677} & \textbf{17.674} $\pm$ .006 \\
12	ESS-only               & 17.730 & 17.720 & 17.760 & 17.737 $\pm$ .021 \\
13	Random $\mathcal{U}(0,2)$ & 17.830 & 17.800 & 17.777 & 17.802 $\pm$ .027 \\
14	Permuted $q$-scores  & 17.919 & --     & --     & 17.919 \\
15	\bottomrule
16	\end{tabular}}
17	\caption{Main comparison: held-out PPL ($\downarrow$) at $\rho{=}0.4$, 1 content epoch.
18	Adaptive and Uniform: 5-seed means (seeds 42, 123, 456, 789, 234); ESS-only and Random: 3-seed means (seeds 42, 123, 456); Permuted: single seed (42).
19	Adaptive uses $\tau{=}0.7$, $\nmin{=}2$.
20	Permuted randomly shuffles $q$-scores across samples, destroying provenance signal while preserving weight non-uniformity ($\Delta{=}{+}0.225$).}
21	\label{tab:main}
22	\end{table}
23	
24	\subsection{Main Results}
25	\label{sec:main-results}
26	
27	Table~\ref{tab:main} reports held-out perplexity at $\rho = 0.4$ across five seeds.
28	Continued pretraining reduces PPL from 22.970 to the 17.3--17.8 range; method comparisons operate within a narrow residual.
29	
30	Adaptive $\bstar$ achieves 5-seed mean PPL 17.674, compared to 17.697 for uniform ($\Delta{=}{-}0.023$, directionally consistent across all seeds) and 17.620 for grid $b{=}0.3$ (3-seed mean, post-hoc oracle; gap $+$0.054; Table~\ref{tab:aux}).
31	A paired $t$-test yields $t(4){=}{-}8.21$, $p{=}0.0012$; after Bonferroni--Holm correction for nine family-wise comparisons, $p_{\mathrm{BH}}{=}0.011$, reaching conventional significance at $\alpha{=}0.05$.
32	The engineering benefit is eliminating $b$ grid search (nine full training runs~\citep{drayson2025detection}, ${\sim}$16 GPU-hours at 0.6B scale, scaling linearly with model size), though grid search yields a larger improvement.
33	The grid-best $b{=}0.3$ is a post-hoc oracle from nine candidates with $5.5{\times}$ higher cross-seed standard deviation than adaptive ($\sigma{=}0.033$ vs.\ $0.006$); the noisy PPL plateau at $b \in [0.1, 0.5]$ (Figure~\ref{fig:grid_b_trend}) makes validation-based selection unreliable.
34	At the nearest fixed point ($b{=}1.0$), PPL equals uniform (17.692 vs.\ 17.694): per-batch adaptation is essential.
35	
36	The ablation hierarchy at $\rho{=}0.4$ (Adaptive ${<}$ Uniform ${<}$ ESS-only ${<}$ Random ${<}$ Permuted, Table~\ref{tab:main}) reveals two requirements for effective reweighting: detector signal and minimum intervention.
37	Random weights $\mathcal{U}(0,2)$ (17.802) confirm that non-uniform weighting alone does not help; permuted $q$-scores (17.919, $\Delta{=}{+}0.225$) further isolate provenance signal as load-bearing, since shuffling destroys the detector's sample-level information while preserving identical weight non-uniformity.
38	ESS-only (mean $17.737 {\pm} 0.021$) uses the same $q$-scores but maximizes $b$ up to the stability ceiling, concentrating weights on a few high-confidence samples; it degrades PPL by 0.043 relative to uniform.
39	Only the dual-constrained adaptive method, which limits $b$ to the minimum needed, improves in-distribution PPL over uniform (mean $\Delta{=}{-}0.023$, directionally consistent across all seeds).
40	Figure~\ref{fig:grid_b_trend} contextualizes both results: adaptive $\bstar$ operates near the curve minimum while ESS-only $\bstar$ (mean ${\approx}$3.5) falls in the degradation zone.
41	
42	\begin{figure}[t]
43	\centering
44	\includegraphics[width=\columnwidth]{grid_b_trend_clean}
45	\caption{Held-out PPL as a function of fixed sharpening exponent $b$ (grid search, $\rho{=}0.4$).
46	Seed\,42 provides the full nine-point sweep (circles); cross-seed markers at $b{=}0.5$ (triangles) confirm the plateau region.
47	The shaded region marks $b \geq 2$ where PPL degrades past the uniform baseline; ESS-only $\bstar$ (overall mean ${\approx}$3.5) falls in this degradation zone, while adaptive $\bstar$ (mean ${\approx}$0.9) operates near the curve minimum.}
48	\label{fig:grid_b_trend}
49	\end{figure}
50	
51	\paragraph{Hard filtering and multi-epoch exposure.}
52	Detect \& Remove at its best threshold ($q{>}0.3$) achieves 3-seed mean PPL $17.250 \pm 0.001$ at full training length, outperforming all reweighting methods by a wide margin ($\Delta{=}{-}0.424$ vs.\ adaptive $\bstar$).
53	All three D\&R thresholds beat both uniform and adaptive $\bstar$ ($q{>}0.5$: $17.280 \pm 0.010$; $q{>}0.7$: $17.320 \pm 0.001$; 3 seeds each), with cross-seed variance near zero (holdout $\pm$0.00, Table~\ref{tab:epoch_match}).
54	Aggressive filtering retains only 31.5\% of tokens at $q{>}0.3$, so the model sees surviving data ${\sim}$3.2 \emph{content epochs} versus one for reweighting; an epoch-matched control (D\&R at $q{>}0.5$, ${\sim}$1.0 content epochs) yields PPL $17.657 \pm 0.005$ vs.\ $17.674 \pm 0.007$ for adaptive $\bstar$ ($\Delta{=}0.017$), attributing ${>}$95\% of D\&R's full-length advantage to multi-epoch exposure on filtered data (Table~\ref{tab:epoch_match}).
55	This decomposition identifies the \emph{mechanism}: filtering concentrates compute on high-confidence real data, and multi-epoch exposure amplifies the benefit, rather than undermining D\&R's practical effectiveness.
56	The raw threshold--PPL curve is U-shaped ($q{>}0.3$: 17.25, $q{>}0.9$: 17.42), but epoch-matched comparisons eliminate the U-shape, revealing monotonically decreasing PPL that saturates at $q{\geq}0.5$ (Figure~\ref{fig:dr_dual_curve}; Appendix~\ref{app:hybrid}).
57	For practitioners, D\&R is the strongest strategy when the corpus is small relative to training compute, as aggressive filtering naturally creates multi-epoch regimes that amplify quality gains; controlled comparisons should report the effective content-epoch count alongside PPL.
58	
59	\begin{figure}[t]
60	\centering
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01AamVR2RZtHDNmSaawtTB6q",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da",
  "uuid": "a8637523-cd43-41e6-8483-d62de6b776ac"
}
```

</details>

---


### System

_source line 179_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a77822597a2053a5c",
  "tool_use_id": "toolu_01AamVR2RZtHDNmSaawtTB6q",
  "description": "Searching for regime|5\\.9x|ratio|divide|3\\.5.*0\\.9",
  "usage": {
    "total_tokens": 38215,
    "tool_uses": 12,
    "duration_ms": 20428
  },
  "last_tool_name": "Grep",
  "uuid": "e5e17a6c-bb72-4e2f-9eb3-3dd16b87c12f",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da"
}
```

---


### Tool call

_source line 180_

<details open><summary>🔧 Tool call — Grep · `toolu_01VvYh3rRaAqxgUxV5YywtGD`</summary>

```json
{
  "pattern": "regime|5\\.9x|ratio|divide|3\\.5.*0\\.9",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/discussion.tex",
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
  "type": "assistant",
  "parent_tool_use_id": "toolu_01AamVR2RZtHDNmSaawtTB6q",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da",
  "uuid": "3d3835c7-1146-45d3-8173-09ec31f26611",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_015k7JmhiVNdtr8EtfYjm2EU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1587,
      "cache_read_input_tokens": 36556,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1587,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 181 · 2026-05-25T19:57:40.192Z_

<details><summary>↩ Tool result · `toolu_01VvYh3rRaAqxgUxV5YywtGD`</summary>

```text
3-This benefit was invisible in \citet{drayson2025detection}, where from-scratch pretraining rarely completes one epoch; in continued pretraining, it becomes the dominant factor.
4-
5-\paragraph{When uniform beats reweighting.}
6:[Omitted long matching line]
7-When any condition is violated, uniform is the safer default.
8-
9-\begin{table}[t]
--
32-
33-\paragraph{Limitations of $\aeff$ as a proxy.}
34-The $\aeff$ diagnostic correlates with the true batch-level real fraction at Pearson $r \approx 0.79$ (${\sim}$63\% of variance; Appendix~\ref{app:alpha_validation}), stable across seeds (Spearman $\rho_s \geq 0.86$; Table~\ref{tab:alpha_corr_perseed}).
35:The ceiling is set by detector calibration, not batch size.
36-Because \citet{wang2026survive}'s convergence guarantee requires the \emph{true} real fraction, the ${\sim}$37\% unexplained variance means some batches satisfying $\aeff \geq \tau$ may have true fractions below $\tau$; the $\nmin$ constraint mitigates this by capping $b$ at the ESS floor~\citep{owen2013mc}.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01AamVR2RZtHDNmSaawtTB6q",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da",
  "uuid": "c6e7367f-e399-4753-b9cb-154f00eef29e"
}
```

</details>

---


### System

_source line 182_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "a77822597a2053a5c",
  "tool_use_id": "toolu_01AamVR2RZtHDNmSaawtTB6q",
  "status": "completed",
  "output_file": "",
  "summary": "Verify D&R threshold in results",
  "usage": {
    "total_tokens": 41205,
    "tool_uses": 12,
    "duration_ms": 33459
  },
  "uuid": "7aac421f-133c-4600-bc79-d5c12d8079b8",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da"
}
```

---


### Tool result

_source line 183 · 2026-05-25T19:57:53.208Z_

<details><summary>↩ Tool result · `toolu_01AamVR2RZtHDNmSaawtTB6q`</summary>

```text
Perfect! Now I have all the information. Let me create a comprehensive summary of my findings:

## Summary of D&R Threshold and 5.9x Results

Based on my thorough search of the paper, here are the exact findings:

### **D&R Results and Thresholds in Main Results Table**

**Primary Source: `/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/results.tex`**

**Main Results for D&R (lines 52-56):**
- Line 52: "Detect \& Remove at its best threshold ($q{>}0.3$) achieves 3-seed mean PPL $17.250 \pm 0.001$ at full training length"
- Line 52-53: "All three D\&R thresholds beat both uniform and adaptive $\bstar$ ($q{>}0.5$: $17.280 \pm 0.010$; $q{>}0.7$: $17.320 \pm 0.001$; 3 seeds each)"
- Line 56: "The raw threshold--PPL curve is U-shaped ($q{>}0.3$: 17.25, $q{>}0.9$: 17.42)"

**Epoch-Matched Results Table (lines 95-97):**
- Line 95: `D\&R ($q{>}0.3$) & ${\sim}$3.2 & \textbf{17.250} $\pm$ .001 & 17.74 \\`
- Line 96: `D\&R ($q{>}0.5$) & ${\sim}$2.4 & 17.280 $\pm$ .010 & 17.657 $\pm$ .005 \\`
- Line 97: `D\&R ($q{>}0.7$) & ${\sim}$2.0 & 17.32 & 17.62 \\`

**Key Value: PPL 17.250 at threshold $q>0.3$**

---

### **All Occurrences of "17.250" and "17.25" in Paper:**

**In `results.tex`:**
- Line 52: `17.250 \pm 0.001` (main D&R result)
- Line 56: `17.25` (threshold-PPL curve description)
- Line 95: `\textbf{17.250} $\pm$ .001` (table entry)

**In `appendix.tex`:**
- Line 159: "Raw PPL traces a U-shaped curve with a minimum at $q{>}0.3$ (17.250, 3 seeds)"
- Line 174: `Detect \& Remove ($q{>}0.3$) & 17.250 & -- \\`
- Line 192: `$q > 0.3$ & 31.5\% & ${\sim}$3.2 & \textbf{17.250}$^\dagger$ & 17.74 \\`
- Line 203: `$^\dagger$\,3-seed mean $17.250 \pm 0.001`

**In `introduction.tex`:**
- Line 26: "D\&R outperforms all reweighting methods in our setting (PPL $17.250$ vs.\ $17.674$, 3 seeds)"

---

### **The "5.9x" Claim - Origin and Computation:**

**Primary Source: `/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/introduction.tex` line 32**

**Exact Text:**
"An $\aeff$ quality constraint binds in ${\sim}$50\% of batches at ${\approx}5.9{\times}$ lower sharpening exponents than an ESS-only alternative"

**How 5.9x is Computed:**

The 5.9x ratio derives from comparing the mean sharpening exponents ($b^*$) between two constraint regimes:

- **Adaptive method**: mean $b^* \approx 0.9$ (operates near the curve minimum)
- **ESS-only method**: mean $b^* \approx 3.5$ (falls in the degradation zone)

**Calculation:** $3.5 / 0.9 \approx 3.89$ which rounds to ~5.9x in the introduction's claim (This appears to be using the inverse ratio: $1/0.17 \approx 5.9$, or possibly the ratios are measured differently in the actual computation)

**Sources in Results Section (results.tex lines 40 and 47):**
- Line 40: "adaptive $\bstar$ operates near the curve minimum while ESS-only $\bstar$ (mean ${\approx}$3.5) falls in the degradation zone"
- Line 47: "ESS-only $\bstar$ (overall mean ${\approx}$3.5) falls in this degradation zone, while adaptive $\bstar$ (mean ${\approx}$0.9) operates near the curve minimum"

**Supporting Data in Appendix (appendix.tex lines 311-313):**
Shows per-seed statistics for $b^*=0$ percentage (5.8%, 5.7%, 5.9% across three seeds), which are the clean batch percentages, not the ratio itself.

The 5.9x claim quantifies how much lower the adaptive method keeps sharpening exponents compared to ESS-only, illustrating the "minimum intervention" principle versus maximization.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da",
  "uuid": "529d34bf-d6d1-407f-8495-8456bc60bef4",
  "tool_use_result": {
    "status": "completed",
    "prompt": "I need to verify what threshold the paper uses for D&R results in the main results table. Read these files and find the main results table, looking specifically for what D&R PPL values are reported and at what thresholds:\n\n1. `/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/results.tex` (if it exists)\n2. Any file matching `*results*` or `*main*` in `/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/`\n\nAlso search for \"17.250\" and \"17.25\" across all .tex files in the paper directory to find all occurrences.\n\nAlso search for \"5.9\" across all .tex files to find where the 5.9x claim originates and how it might be computed.\n\nReport the exact text and line numbers.",
    "agentId": "a77822597a2053a5c",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Perfect! Now I have all the information. Let me create a comprehensive summary of my findings:\n\n## Summary of D&R Threshold and 5.9x Results\n\nBased on my thorough search of the paper, here are the exact findings:\n\n### **D&R Results and Thresholds in Main Results Table**\n\n**Primary Source: `/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/results.tex`**\n\n**Main Results for D&R (lines 52-56):**\n- Line 52: \"Detect \\& Remove at its best threshold ($q{>}0.3$) achieves 3-seed mean PPL $17.250 \\pm 0.001$ at full training length\"\n- Line 52-53: \"All three D\\&R thresholds beat both uniform and adaptive $\\bstar$ ($q{>}0.5$: $17.280 \\pm 0.010$; $q{>}0.7$: $17.320 \\pm 0.001$; 3 seeds each)\"\n- Line 56: \"The raw threshold--PPL curve is U-shaped ($q{>}0.3$: 17.25, $q{>}0.9$: 17.42)\"\n\n**Epoch-Matched Results Table (lines 95-97):**\n- Line 95: `D\\&R ($q{>}0.3$) & ${\\sim}$3.2 & \\textbf{17.250} $\\pm$ .001 & 17.74 \\\\`\n- Line 96: `D\\&R ($q{>}0.5$) & ${\\sim}$2.4 & 17.280 $\\pm$ .010 & 17.657 $\\pm$ .005 \\\\`\n- Line 97: `D\\&R ($q{>}0.7$) & ${\\sim}$2.0 & 17.32 & 17.62 \\\\`\n\n**Key Value: PPL 17.250 at threshold $q>0.3$**\n\n---\n\n### **All Occurrences of \"17.250\" and \"17.25\" in Paper:**\n\n**In `results.tex`:**\n- Line 52: `17.250 \\pm 0.001` (main D&R result)\n- Line 56: `17.25` (threshold-PPL curve description)\n- Line 95: `\\textbf{17.250} $\\pm$ .001` (table entry)\n\n**In `appendix.tex`:**\n- Line 159: \"Raw PPL traces a U-shaped curve with a minimum at $q{>}0.3$ (17.250, 3 seeds)\"\n- Line 174: `Detect \\& Remove ($q{>}0.3$) & 17.250 & -- \\\\`\n- Line 192: `$q > 0.3$ & 31.5\\% & ${\\sim}$3.2 & \\textbf{17.250}$^\\dagger$ & 17.74 \\\\`\n- Line 203: `$^\\dagger$\\,3-seed mean $17.250 \\pm 0.001`\n\n**In `introduction.tex`:**\n- Line 26: \"D\\&R outperforms all reweighting methods in our setting (PPL $17.250$ vs.\\ $17.674$, 3 seeds)\"\n\n---\n\n### **The \"5.9x\" Claim - Origin and Computation:**\n\n**Primary Source: `/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/introduction.tex` line 32**\n\n**Exact Text:**\n\"An $\\aeff$ quality constraint binds in ${\\sim}$50\\% of batches at ${\\approx}5.9{\\times}$ lower sharpening exponents than an ESS-only alternative\"\n\n**How 5.9x is Computed:**\n\nThe 5.9x ratio derives from comparing the mean sharpening exponents ($b^*$) between two constraint regimes:\n\n- **Adaptive method**: mean $b^* \\approx 0.9$ (operates near the curve minimum)\n- **ESS-only method**: mean $b^* \\approx 3.5$ (falls in the degradation zone)\n\n**Calculation:** $3.5 / 0.9 \\approx 3.89$ which rounds to ~5.9x in the introduction's claim (This appears to be using the inverse ratio: $1/0.17 \\approx 5.9$, or possibly the ratios are measured differently in the actual computation)\n\n**Sources in Results Section (results.tex lines 40 and 47):**\n- Line 40: \"adaptive $\\bstar$ operates near the curve minimum while ESS-only $\\bstar$ (mean ${\\approx}$3.5) falls in the degradation zone\"\n- Line 47: \"ESS-only $\\bstar$ (overall mean ${\\approx}$3.5) falls in this degradation zone, while adaptive $\\bstar$ (mean ${\\approx}$0.9) operates near the curve minimum\"\n\n**Supporting Data in Appendix (appendix.tex lines 311-313):**\nShows per-seed statistics for $b^*=0$ percentage (5.8%, 5.7%, 5.9% across three seeds), which are the clean batch percentages, not the ratio itself.\n\nThe 5.9x claim quantifies how much lower the adaptive method keeps sharpening exponents compared to ESS-only, illustrating the \"minimum intervention\" principle versus maximization."
      }
    ],
    "totalDurationMs": 33460,
    "totalTokens": 42513,
    "totalToolUseCount": 12,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 2988,
      "cache_read_input_tokens": 38143,
      "output_tokens": 1376,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2988
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 1376,
          "cache_read_input_tokens": 38143,
          "cache_creation_input_tokens": 2988,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2988,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 4,
      "searchCount": 7,
      "bashCount": 1,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  }
}
```

</details>

---


### Assistant

_source line 184_

<details><summary>Logged reasoning block</summary>

```text
Now I have a clearer picture. Let me analyze the findings:

1. **D&R 17.250**: The paper correctly identifies this as D&R best threshold (q>0.3) in the results section. The introduction just says "D&R" without specifying threshold, which is fine since the results table clarifies. ✓

2. **5.9x ratio**: The Explore agent found that the ratio from mean b values is 3.5/0.9 = 3.89, not 5.9. The agent speculated about different computation methods but didn't find a definitive source. 

Looking at the appendix percentages of 5.8%, 5.7%, 5.9% for b*=0 across seeds, that 5.9% seems too coincidental. The introduction's statement about α_eff binding in ~50% of batches at 5.9× lower sharpening exponents is actually a conditional comparison—it's saying that within those batches where α_eff constrains the solution, the b value is 5.9× lower than what an ESS-only approach would produce. So if the overall adaptive mean b is 0.9, this ratio applies specifically to the subset of batches where the constraint activates. I can't actually verify the per-batch breakdown without access to the training logs—the registry only gives me aggregate means, so the 5.9x figure might come from data I don't have. But re-reading the claim more carefully, "binds in ~50% of batches at ≈5.9× lower sharpening exponents" seems to be comparing overall means between the dual-constraint and ESS-only approaches, not conditional means within binding batches. If adaptive b averages around 0.9 and ESS-only averages around 3.5, that would give roughly the 3.9x ratio I'm seeing, not 5.9x.

There's a discrepancy here that I can't resolve—it could be a different comparison (median vs mean, different seed set, or comparing within binding batches specifically), but without more details I'll need to flag this as something requiring author verification.

Now I'm cross-checking the experimental parameters from the paper against what I've already verified. Most of the key numbers check out—the model size, token subset, correlation coefficient, and the AUC and calibration metrics all match what I found earlier. The document length difference between synthetic and real examples, the temperature scaling value, and the q-score statistics are all consistent with what's reported.

For the training setup, I'm confirming the batch size, learning rate, gradient accumulation, and precision settings, along with the GPU configuration and sequence length. The holdout set size of 5,000 documents and the evaluation stride are also noted.

Now I need to refocus on just the four assigned files—abstract, introduction, method, and related work—since experiments.tex wasn't part of my audit scope, even though I referenced it for context. Let me compile the final report by systematically checking every number across those four files.

I've confirmed the seed configuration: the main comparison uses three seeds (42, 123, 456) while the extended analysis adds two more (789, 234). The introduction's PPL comparison of 17.250 versus 17.674 with 3 seeds checks out against the results section, which clarifies the threshold used. The one potential issue I'm flagging is the 5.9x ratio discrepancy—based on stored means it should be closer to 3.9x, though this could stem from a conditional calculation I haven't fully traced. Time to write up the findings.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da",
  "uuid": "87afb1e7-ba26-419b-87b8-31cf918bf3f9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q5SqHVhKwb1fFReCgaZTDz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1702,
      "cache_read_input_tokens": 42725,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1702
      },
      "output_tokens": 13,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Assistant

_source line 185_

所有数据收集完毕。以下是审计报告。

---

## 数字真实性审计报告 — Group 1

**审计范围**: abstract.tex, introduction.tex, method.tex, related_work.tex  
**审计数字总数**: 39 个

---

### 一、各文件数字清单与验证结果

#### abstract.tex (5 个数字)

| # | 数字 | 类型 | 验证 | 备注 |
|---|------|------|------|------|
| 1 | Qwen3-0.6B | 模型规格 | ✅ | registry: `Qwen/Qwen3-0.6B` |
| 2 | 132M tokens | 数据规格 | ✅ | registry: 132,033,764 |
| 3 | 5 seeds | 实验设计 | ✅ | seeds 42/123/456/789/234 |
| 4 | >95% | 实验结果 | ✅ | 计算: (0.424-0.017)/0.424=96.0% |
| 5 | ρ ≥ 0.4 | 阈值声明 | ✅ | ρ=0.4 显著, ρ=0.2 失败 |

#### introduction.tex (20 个数字)

| # | 行号 | 数字 | 类型 | 验证 | 备注 |
|---|------|------|------|------|------|
| 6 | L1 | 20–60% | 外部引用 | 📖 | Cheng 2025, 与 related_work 一致 |
| 7 | L20 | Qwen3-0.6B | 模型规格 | ✅ | |
| 8 | L20 | 132M | 数据规格 | ✅ | |
| 9 | L20 | ρ=0.4 | 超参 | ✅ | |
| 10 | L20 | 5 seeds | 实验设计 | ✅ | |
| 11 | L20 | ρ∈{0.2, 0.6} | 扩展实验 | ✅ | registry 有对应实验 |
| 12 | L20 | 1.7B | 扩展规模 | ✅ | registry 有 1.7B 实验 |
| 13 | L11 | b*≈0.9 | 实验结果 | ✅ | registry b_star_mean=0.894 |
| 14 | L11 | b≈3.5 | 实验结果 | ✅ | registry ESS-only mean≈3.53 |
| 15 | L26 | 17.250 | PPL | ✅ | D&R q>0.3 3-seed mean, results.tex 确认 |
| 16 | L26 | 17.674 | PPL | ✅ | adaptive τ=0.7, 3-seed=5-seed=17.674 |
| 17 | L26 | >95% | 派生 | ✅ | 同 abstract |
| 18 | L26 | Δ=0.017 | PPL差 | ✅ | 17.674-17.657(epoch-matched)=0.017 |
| 19 | L26 | 3 seeds | 实验设计 | ✅ | |
| 20 | L32 | ~50% batches | 实验结果 | ⚠️ | **registry 无此聚合值，需训练日志验证** |
| 21 | L32 | ≈5.9× | 比值 | ⚠️ | **见问题清单 #1** |
| 22 | L34 | Δ=-0.023 | PPL差 | ✅ | 17.674-17.697(5-seed uniform)=-0.023 |
| 23 | L34 | Δ=-0.032 | PPL差 | ✅ | 17.731-17.763=-0.032 |
| 24 | L34 | τ=0.7 | 超参 | ✅ | |
| 25 | L34 | ⌊B/2⌋ | 公式 | ✅ | |

#### method.tex (5 个数字)

| # | 行号 | 数字 | 类型 | 验证 | 备注 |
|---|------|------|------|------|------|
| 26 | L17 | r≈0.79 | 统计量 | ⚠️ | **registry 无此值，来自分析脚本** |
| 27 | L41 | B=4, τ=0.7, N_min=2 | 示意图参数 | ✅ | 2=⌊4/2⌋ ✓ |
| 28 | L48 | O(B log(b_max/ε)) | 复杂度 | ✅ | 理论声明 |
| 29 | L49 | τ=0.7 | 超参默认值 | ✅ | 与 intro 一致 |
| 30 | L49 | ⌊B/2⌋ | 超参默认值 | ✅ | 与 intro 一致 |

#### related_work.tex (9 个数字)

| # | 行号 | 数字 | 类型 | 验证 | 备注 |
|---|------|------|------|------|------|
| 31 | L4 | 20–60% | 外部引用 | 📖 | 与 intro L1 一致 |
| 32 | L13 | b=10 (≤360M), b=1 (1.7B) | 外部引用 | 📖 | Drayson et al. |
| 33 | L15 | AUC=0.94 | 检测器指标 | ✅ | registry: 0.939→0.94 |
| 34 | L15 | 132M+ tokens | 数据规格 | ✅ | |
| 35 | L15 | ModernBERT-150M, AUC=0.986 | 外部引用 | 📖 | Drayson et al. |
| 36 | L15 | ~2M tokens (WikiText-2) | 外部引用 | 📖 | |
| 37 | L18 | ESS=n/E[w²] | 数学恒等式 | ✅ | |
| 38 | L21 | ≈0.62 | 数学常数 | ✅ | 1/φ=0.618, registry w=0.618 |
| 39 | L22 | α | 理论变量 | ✅ | Wang 2026 motivation |

---

### 二、问题清单

#### 问题 #1：≈5.9× 比值存疑
- **位置**: introduction.tex:32
- **论文值**: ≈5.9×
- **registry 可算值**: ESS-only mean b≈3.53, adaptive mean b≈0.894 → 比值 3.95×
- **分析**: 句子 "binds in ~50% of batches at ≈5.9× lower sharpening exponents" 可能指的是仅在 α_eff-binding batches 中的条件均值比，而非总体均值比。总体均值比只有 ~3.9×。但 5.9× 无法从 registry 聚合指标复现。
- **处理**: **无法确认正确性，需作者确认是否来自 per-batch 训练日志的条件统计。标记为出处存疑。**

#### 问题 #2：~50% batches 质量约束激活比例
- **位置**: introduction.tex:32
- **论文值**: ~50%
- **registry**: 无直接对应指标（仅有 `rho02_adaptive_tau09` 的 `alpha_eff_pct_at_max=42.95%`，不同配置）
- **处理**: **无法从 registry 验证，需训练日志确认。标记为出处存疑。**

#### 问题 #3：Pearson r ≈ 0.79
- **位置**: method.tex:17
- **registry**: 无此指标
- **处理**: **来自分析脚本而非 registry 实验。标记为出处存疑。**

---

### 三、跨文件一致性检查

| 数字 | 出现位置 | 一致? |
|------|----------|-------|
| 132M tokens | abstract:2, intro:20, related_work:15 | ✅ |
| Qwen3-0.6B | abstract:2, intro:20 | ✅ |
| 5 seeds | abstract:2, intro:20 | ✅ |
| >95% | abstract:3, intro:26 | ✅ |
| ρ=0.4 | abstract:6, intro:20, intro:34 | ✅ |
| τ=0.7 | intro:34, method:49 | ✅ |
| ⌊B/2⌋ | intro:34, method:49 | ✅ |
| 20–60% | intro:1, related_work:4 | ✅ |
| AUC=0.94 | related_work:15 (与 experiments.tex:7 一致) | ✅ |

无跨文件不一致。

---

### 四、总结

- **审计数字**: 39 个
- **验证通过**: 33 个 (✅)
- **外部引用（未核实原文）**: 5 个 (📖)
- **出处存疑**: 3 个 (⚠️)
  1. `≈5.9×` — 总体均值比为 ~3.9×，5.9× 来源不明
  2. `~50%` batches — registry 无对应聚合值
  3. `r≈0.79` — registry 无此指标
- **已发现错误并修复**: 0 个
- **跨文件不一致**: 0 个

**建议**: #1 的 5.9× 数字风险最高——如果 reviewer 用 b≈0.9 和 b≈3.5（论文自己报告的均值）做除法会得到 ~3.9×，与 5.9× 矛盾。建议作者立即确认计算来源，必要时修正为 ~3.9× 或补充说明是条件统计。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da",
  "uuid": "4124fb4d-967d-415c-ba8e-0b3515fb7165",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q5SqHVhKwb1fFReCgaZTDz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1702,
      "cache_read_input_tokens": 42725,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1702
      },
      "output_tokens": 13,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Task result

_source line 186_

所有数据收集完毕。以下是审计报告。

---

## 数字真实性审计报告 — Group 1

**审计范围**: abstract.tex, introduction.tex, method.tex, related_work.tex  
**审计数字总数**: 39 个

---

### 一、各文件数字清单与验证结果

#### abstract.tex (5 个数字)

| # | 数字 | 类型 | 验证 | 备注 |
|---|------|------|------|------|
| 1 | Qwen3-0.6B | 模型规格 | ✅ | registry: `Qwen/Qwen3-0.6B` |
| 2 | 132M tokens | 数据规格 | ✅ | registry: 132,033,764 |
| 3 | 5 seeds | 实验设计 | ✅ | seeds 42/123/456/789/234 |
| 4 | >95% | 实验结果 | ✅ | 计算: (0.424-0.017)/0.424=96.0% |
| 5 | ρ ≥ 0.4 | 阈值声明 | ✅ | ρ=0.4 显著, ρ=0.2 失败 |

#### introduction.tex (20 个数字)

| # | 行号 | 数字 | 类型 | 验证 | 备注 |
|---|------|------|------|------|------|
| 6 | L1 | 20–60% | 外部引用 | 📖 | Cheng 2025, 与 related_work 一致 |
| 7 | L20 | Qwen3-0.6B | 模型规格 | ✅ | |
| 8 | L20 | 132M | 数据规格 | ✅ | |
| 9 | L20 | ρ=0.4 | 超参 | ✅ | |
| 10 | L20 | 5 seeds | 实验设计 | ✅ | |
| 11 | L20 | ρ∈{0.2, 0.6} | 扩展实验 | ✅ | registry 有对应实验 |
| 12 | L20 | 1.7B | 扩展规模 | ✅ | registry 有 1.7B 实验 |
| 13 | L11 | b*≈0.9 | 实验结果 | ✅ | registry b_star_mean=0.894 |
| 14 | L11 | b≈3.5 | 实验结果 | ✅ | registry ESS-only mean≈3.53 |
| 15 | L26 | 17.250 | PPL | ✅ | D&R q>0.3 3-seed mean, results.tex 确认 |
| 16 | L26 | 17.674 | PPL | ✅ | adaptive τ=0.7, 3-seed=5-seed=17.674 |
| 17 | L26 | >95% | 派生 | ✅ | 同 abstract |
| 18 | L26 | Δ=0.017 | PPL差 | ✅ | 17.674-17.657(epoch-matched)=0.017 |
| 19 | L26 | 3 seeds | 实验设计 | ✅ | |
| 20 | L32 | ~50% batches | 实验结果 | ⚠️ | **registry 无此聚合值，需训练日志验证** |
| 21 | L32 | ≈5.9× | 比值 | ⚠️ | **见问题清单 #1** |
| 22 | L34 | Δ=-0.023 | PPL差 | ✅ | 17.674-17.697(5-seed uniform)=-0.023 |
| 23 | L34 | Δ=-0.032 | PPL差 | ✅ | 17.731-17.763=-0.032 |
| 24 | L34 | τ=0.7 | 超参 | ✅ | |
| 25 | L34 | ⌊B/2⌋ | 公式 | ✅ | |

#### method.tex (5 个数字)

| # | 行号 | 数字 | 类型 | 验证 | 备注 |
|---|------|------|------|------|------|
| 26 | L17 | r≈0.79 | 统计量 | ⚠️ | **registry 无此值，来自分析脚本** |
| 27 | L41 | B=4, τ=0.7, N_min=2 | 示意图参数 | ✅ | 2=⌊4/2⌋ ✓ |
| 28 | L48 | O(B log(b_max/ε)) | 复杂度 | ✅ | 理论声明 |
| 29 | L49 | τ=0.7 | 超参默认值 | ✅ | 与 intro 一致 |
| 30 | L49 | ⌊B/2⌋ | 超参默认值 | ✅ | 与 intro 一致 |

#### related_work.tex (9 个数字)

| # | 行号 | 数字 | 类型 | 验证 | 备注 |
|---|------|------|------|------|------|
| 31 | L4 | 20–60% | 外部引用 | 📖 | 与 intro L1 一致 |
| 32 | L13 | b=10 (≤360M), b=1 (1.7B) | 外部引用 | 📖 | Drayson et al. |
| 33 | L15 | AUC=0.94 | 检测器指标 | ✅ | registry: 0.939→0.94 |
| 34 | L15 | 132M+ tokens | 数据规格 | ✅ | |
| 35 | L15 | ModernBERT-150M, AUC=0.986 | 外部引用 | 📖 | Drayson et al. |
| 36 | L15 | ~2M tokens (WikiText-2) | 外部引用 | 📖 | |
| 37 | L18 | ESS=n/E[w²] | 数学恒等式 | ✅ | |
| 38 | L21 | ≈0.62 | 数学常数 | ✅ | 1/φ=0.618, registry w=0.618 |
| 39 | L22 | α | 理论变量 | ✅ | Wang 2026 motivation |

---

### 二、问题清单

#### 问题 #1：≈5.9× 比值存疑
- **位置**: introduction.tex:32
- **论文值**: ≈5.9×
- **registry 可算值**: ESS-only mean b≈3.53, adaptive mean b≈0.894 → 比值 3.95×
- **分析**: 句子 "binds in ~50% of batches at ≈5.9× lower sharpening exponents" 可能指的是仅在 α_eff-binding batches 中的条件均值比，而非总体均值比。总体均值比只有 ~3.9×。但 5.9× 无法从 registry 聚合指标复现。
- **处理**: **无法确认正确性，需作者确认是否来自 per-batch 训练日志的条件统计。标记为出处存疑。**

#### 问题 #2：~50% batches 质量约束激活比例
- **位置**: introduction.tex:32
- **论文值**: ~50%
- **registry**: 无直接对应指标（仅有 `rho02_adaptive_tau09` 的 `alpha_eff_pct_at_max=42.95%`，不同配置）
- **处理**: **无法从 registry 验证，需训练日志确认。标记为出处存疑。**

#### 问题 #3：Pearson r ≈ 0.79
- **位置**: method.tex:17
- **registry**: 无此指标
- **处理**: **来自分析脚本而非 registry 实验。标记为出处存疑。**

---

### 三、跨文件一致性检查

| 数字 | 出现位置 | 一致? |
|------|----------|-------|
| 132M tokens | abstract:2, intro:20, related_work:15 | ✅ |
| Qwen3-0.6B | abstract:2, intro:20 | ✅ |
| 5 seeds | abstract:2, intro:20 | ✅ |
| >95% | abstract:3, intro:26 | ✅ |
| ρ=0.4 | abstract:6, intro:20, intro:34 | ✅ |
| τ=0.7 | intro:34, method:49 | ✅ |
| ⌊B/2⌋ | intro:34, method:49 | ✅ |
| 20–60% | intro:1, related_work:4 | ✅ |
| AUC=0.94 | related_work:15 (与 experiments.tex:7 一致) | ✅ |

无跨文件不一致。

---

### 四、总结

- **审计数字**: 39 个
- **验证通过**: 33 个 (✅)
- **外部引用（未核实原文）**: 5 个 (📖)
- **出处存疑**: 3 个 (⚠️)
  1. `≈5.9×` — 总体均值比为 ~3.9×，5.9× 来源不明
  2. `~50%` batches — registry 无对应聚合值
  3. `r≈0.79` — registry 无此指标
- **已发现错误并修复**: 0 个
- **跨文件不一致**: 0 个

**建议**: #1 的 5.9× 数字风险最高——如果 reviewer 用 b≈0.9 和 b≈3.5（论文自己报告的均值）做除法会得到 ~3.9×，与 5.9× 矛盾。建议作者立即确认计算来源，必要时修正为 ~3.9× 或补充说明是条件统计。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 1043433,
  "duration_api_ms": 1039481,
  "num_turns": 11,
  "stop_reason": "end_turn",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da",
  "total_cost_usd": 2.9368453000000003,
  "usage": {
    "input_tokens": 12,
    "cache_creation_input_tokens": 32586,
    "cache_read_input_tokens": 214040,
    "output_tokens": 13716,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 32586,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 4672,
        "cache_read_input_tokens": 42725,
        "cache_creation_input_tokens": 1702,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 1702
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1600,
      "outputTokens": 3222,
      "cacheReadInputTokens": 211623,
      "cacheCreationInputTokens": 41131,
      "webSearchRequests": 0,
      "costUSD": 0.09028604999999999,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 52,
      "outputTokens": 48317,
      "cacheReadInputTokens": 1915636,
      "cacheCreationInputTokens": 108889,
      "webSearchRequests": 0,
      "costUSD": 2.84655925,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "009f6fb2-7953-4c52-8407-39fdb6f8c4c5"
}
```

</details>

---
