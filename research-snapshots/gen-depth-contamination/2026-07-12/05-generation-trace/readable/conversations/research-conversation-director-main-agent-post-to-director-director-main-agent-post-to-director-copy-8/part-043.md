# Research conversation: [系统提醒] 你刚才完成了 [Director 指令] 但没有调用 main_agent_post_to_director 汇报结果。Director 看不到你的文字回复。请立即调用 main_agent_post_to_director  — Part 43 of 107

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary (July export snapshot)** · Conversation logs

[← Part 42](part-042.md) · [Transcript overview](../research-conversation-director-main-agent-post-to-director-director-main-agent-post-to-director-copy-8.md) · [Part 44 →](part-044.md) · [Structured JSON](../../../sessions/30/305edc9fad05c89e2b3c.json)

## Round 388

### Tool result

_source line 8094 · 2026-05-18T06:22:33.014Z_

<details><summary>↩ Tool result · `toolu_01Qy7kZmB7rNVjZpxnSrGsp8`</summary>

```text
1	\section{Extended Discussion}
2	\label{sec:extended_discussion}
3	
4	\subsection{Theoretical Implications of \texorpdfstring{$\Kempirical = 2$}{K*=2}}
5	
6	The DPI guarantees a finite $\Ktheory$; for general web text, $\Kempirical \leq 2$ across all 8 configurations (1B--8B, 5 families), while structured domains (arXiv) yield $\Kempirical{=}3$, aligning with model collapse convergence~\cite{shumailov2024collapse, dohmatob2024model, alemohammad2024selfconsuming}.
7	Decoding strategy modestly affects signal strength (1v2 $\auc \in [0.6866, 0.7039]$) but does not shift the boundary.
8	
9	\subsection{Cross-Model Transfer Implications}
10	
11	Cross-model classification retains 80--92\% accuracy with scorer-invariant feature rankings ($\rho > 0.90$), enabling single-classifier deployment across generators.
12	Absolute discriminability at the $\Kempirical$ boundary is scorer-sensitive: alternative scorers reduce Qwen-continuation $\Kempirical$ from 2 to 1, while rewrite-mode $\Kempirical = 2$ is preserved.
13	Model family similarity modulates transfer (Pythia$\leftrightarrow$OLMo: 90--92\% vs.\ Qwen-cont$\leftrightarrow$OLMo: 80--85\%).
14	
15	\noindent\begin{minipage}{\columnwidth}
16	\centering
17	\captionof{table}{Cross-scorer validation on Qwen-generated text. Alternative scorers (Pythia-1.4B, OLMo-1B) preserve feature ranking ($\rho > 0.90$) and rewrite-mode $\Kempirical = 2$, but reduce continuation-mode $\Kempirical$ from 2 to 1.}
18	\label{tab:crossscorer}
19	\resizebox{\columnwidth}{!}{\input{tables/tab_crossscorer}}
20	\end{minipage}
21	
22	\begin{table}[h]
23	\centering
24	\small
25	\caption{Three-way ANOVA (Generator $\times$ Scorer $\times$ Depth-Pair) on per-fold pairwise $\auc$ values (Type~II SS). DV = per-fold AUC; $N{=}300$ (12 cells $\times$ 5 folds $\times$ 5 depth-pairs; 3 generators $\times$ 4 scorers). Scorer is statistically significant ($p < .001$) but has a small effect size ($\eta^2_p = 0.19$) relative to Depth-Pair ($\eta^2_p = 1.00$) and Generator ($\eta^2_p = 0.89$), indicating that scorer choice has a detectable but practically minor influence on depth discrimination.}
26	\label{tab:anova_crossscorer}
27	\begin{tabular}{lrrrr}
28	\toprule
29	\textbf{Source} & \textbf{df} & $F$ & $p$ & $\eta^2_p$ \\
30	\midrule
31	Generator     & 2  & 926.8  & ${<}.001$  & .885 \\
32	Scorer        & 3  & 19.02  & ${<}.001$  & .192 \\
33	Depth-Pair    & 4  & 24736  & ${<}.001$  & .998 \\
34	Gen$\times$Scorer & 6 & 8.16 & ${<}.001$ & .170 \\
35	Gen$\times$Depth  & 8 & 993.7 & ${<}.001$ & .971 \\
36	Scorer$\times$Depth & 12 & 2.45 & .005 & .109 \\
37	Residual      & 240 & & & \\
38	\bottomrule
39	\end{tabular}
40	\end{table}
41	
42	\subsection{Feature Importance Across Decoding Strategies}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9223f7c8-5e4d-4041-8e9f-ff9b65a7356d",
  "isSidechain": false,
  "promptId": "8dba7b96-5a22-445a-882e-3856dafbad00",
  "type": "user",
  "uuid": "891bf3ab-030d-4eb8-a682-7e3d4ac705d8",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex",
      "content": "\\section{Extended Discussion}\n\\label{sec:extended_discussion}\n\n\\subsection{Theoretical Implications of \\texorpdfstring{$\\Kempirical = 2$}{K*=2}}\n\nThe DPI guarantees a finite $\\Ktheory$; for general web text, $\\Kempirical \\leq 2$ across all 8 configurations (1B--8B, 5 families), while structured domains (arXiv) yield $\\Kempirical{=}3$, aligning with model collapse convergence~\\cite{shumailov2024collapse, dohmatob2024model, alemohammad2024selfconsuming}.\nDecoding strategy modestly affects signal strength (1v2 $\\auc \\in [0.6866, 0.7039]$) but does not shift the boundary.\n\n\\subsection{Cross-Model Transfer Implications}\n\nCross-model classification retains 80--92\\% accuracy with scorer-invariant feature rankings ($\\rho > 0.90$), enabling single-classifier deployment across generators.\nAbsolute discriminability at the $\\Kempirical$ boundary is scorer-sensitive: alternative scorers reduce Qwen-continuation $\\Kempirical$ from 2 to 1, while rewrite-mode $\\Kempirical = 2$ is preserved.\nModel family similarity modulates transfer (Pythia$\\leftrightarrow$OLMo: 90--92\\% vs.\\ Qwen-cont$\\leftrightarrow$OLMo: 80--85\\%).\n\n\\noindent\\begin{minipage}{\\columnwidth}\n\\centering\n\\captionof{table}{Cross-scorer validation on Qwen-generated text. Alternative scorers (Pythia-1.4B, OLMo-1B) preserve feature ranking ($\\rho > 0.90$) and rewrite-mode $\\Kempirical = 2$, but reduce continuation-mode $\\Kempirical$ from 2 to 1.}\n\\label{tab:crossscorer}\n\\resizebox{\\columnwidth}{!}{\\input{tables/tab_crossscorer}}\n\\end{minipage}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Three-way ANOVA (Generator $\\times$ Scorer $\\times$ Depth-Pair) on per-fold pairwise $\\auc$ values (Type~II SS). DV = per-fold AUC; $N{=}300$ (12 cells $\\times$ 5 folds $\\times$ 5 depth-pairs; 3 generators $\\times$ 4 scorers). Scorer is statistically significant ($p < .001$) but has a small effect size ($\\eta^2_p = 0.19$) relative to Depth-Pair ($\\eta^2_p = 1.00$) and Generator ($\\eta^2_p = 0.89$), indicating that scorer choice has a detectable but practically minor influence on depth discrimination.}\n\\label{tab:anova_crossscorer}\n\\begin{tabular}{lrrrr}\n\\toprule\n\\textbf{Source} & \\textbf{df} & $F$ & $p$ & $\\eta^2_p$ \\\\\n\\midrule\nGenerator     & 2  & 926.8  & ${<}.001$  & .885 \\\\\nScorer        & 3  & 19.02  & ${<}.001$  & .192 \\\\\nDepth-Pair    & 4  & 24736  & ${<}.001$  & .998 \\\\\nGen$\\times$Scorer & 6 & 8.16 & ${<}.001$ & .170 \\\\\nGen$\\times$Depth  & 8 & 993.7 & ${<}.001$ & .971 \\\\\nScorer$\\times$Depth & 12 & 2.45 & .005 & .109 \\\\\nResidual      & 240 & & & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Feature Importance Across Decoding Strategies}",
      "numLines": 42,
      "startLine": 1,
      "totalLines": 275
    }
  },
  "sourceToolAssistantUUID": "9223f7c8-5e4d-4041-8e9f-ff9b65a7356d",
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


### Runtime record

_source line 8095_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Director 指令] Reviewer visual review 发现 4 个排版问题：  **1. [必修] Page 11 feature ranking table 溢出** appendix.tex ~L26-35 (tab:top_features)，`\\texttt{}` feature 名过宽导致最右列侵入右栏。修复：`\\resizebox{\\columnwidth}{!}{…",
  "leafUuid": "891bf3ab-030d-4eb8-a682-7e3d4ac705d8",
  "sessionId": "952e4180-a1dd-4838-893f-04003731e881"
}
```

---


### Runtime record

_source line 8096_

```json
{
  "type": "ai-title",
  "aiTitle": "Report agent results to director",
  "sessionId": "952e4180-a1dd-4838-893f-04003731e881"
}
```

---


### Assistant

_source line 8097 · 2026-05-18T06:22:38.513Z_

<details><summary>Logged reasoning block</summary>

```text
Now I need to consolidate D.1-D.6 into a single opening paragraph (removing redundant subsection headers) while keeping the two tables (crossscorer and ANOVA) in place. Then D.7 (Extended Limitations) becomes the first subsection.

Here's my plan:
1. Replace D.1-D.6 with a brief introductory paragraph that sets context
2. Keep the crossscorer table and ANOVA table
3. D.7 (Extended Limitations) becomes the first subsection


4. Now I'm writing the replacement paragraph...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "891bf3ab-030d-4eb8-a682-7e3d4ac705d8",
  "isSidechain": false,
  "requestId": "req_011Cb9Z3aKGp5EvzqvQJReo3",
  "type": "assistant",
  "uuid": "eb278f59-e97a-48f1-a864-bb47aeee4090",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/paper_agent_e65ef40e",
  "sessionId": "952e4180-a1dd-4838-893f-04003731e881",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "frolicking-frolicking-dahl",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JEtvPGmvD7fWesz7NQEFRt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3604,
      "cache_read_input_tokens": 135518,
      "output_tokens": 2823,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3604,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2823,
          "cache_read_input_tokens": 135518,
          "cache_creation_input_tokens": 3604,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3604
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


### Tool call

_source line 8098 · 2026-05-18T06:23:13.961Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01XQWUiQi5Ra8PJCEMvJ5rpd`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex",
  "old_string": "\\section{Extended Discussion}\n\\label{sec:extended_discussion}\n\n\\subsection{Theoretical Implications of \\texorpdfstring{$\\Kempirical = 2$}{K*=2}}\n\nThe DPI guarantees a finite $\\Ktheory$; for general web text, $\\Kempirical \\leq 2$ across all 8 configurations (1B--8B, 5 families), while structured domains (arXiv) yield $\\Kempirical{=}3$, aligning with model collapse convergence~\\cite{shumailov2024collapse, dohmatob2024model, alemohammad2024selfconsuming}.\nDecoding strategy modestly affects signal strength (1v2 $\\auc \\in [0.6866, 0.7039]$) but does not shift the boundary.\n\n\\subsection{Cross-Model Transfer Implications}\n\nCross-model classification retains 80--92\\% accuracy with scorer-invariant feature rankings ($\\rho > 0.90$), enabling single-classifier deployment across generators.\nAbsolute discriminability at the $\\Kempirical$ boundary is scorer-sensitive: alternative scorers reduce Qwen-continuation $\\Kempirical$ from 2 to 1, while rewrite-mode $\\Kempirical = 2$ is preserved.\nModel family similarity modulates transfer (Pythia$\\leftrightarrow$OLMo: 90--92\\% vs.\\ Qwen-cont$\\leftrightarrow$OLMo: 80--85\\%).\n\n\\noindent\\begin{minipage}{\\columnwidth}\n\\centering\n\\captionof{table}{Cross-scorer validation on Qwen-generated text. Alternative scorers (Pythia-1.4B, OLMo-1B) preserve feature ranking ($\\rho > 0.90$) and rewrite-mode $\\Kempirical = 2$, but reduce continuation-mode $\\Kempirical$ from 2 to 1.}\n\\label{tab:crossscorer}\n\\resizebox{\\columnwidth}{!}{\\input{tables/tab_crossscorer}}\n\\end{minipage}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Three-way ANOVA (Generator $\\times$ Scorer $\\times$ Depth-Pair) on per-fold pairwise $\\auc$ values (Type~II SS). DV = per-fold AUC; $N{=}300$ (12 cells $\\times$ 5 folds $\\times$ 5 depth-pairs; 3 generators $\\times$ 4 scorers). Scorer is statistically significant ($p < .001$) but has a small effect size ($\\eta^2_p = 0.19$) relative to Depth-Pair ($\\eta^2_p = 1.00$) and Generator ($\\eta^2_p = 0.89$), indicating that scorer choice has a detectable but practically minor influence on depth discrimination.}\n\\label{tab:anova_crossscorer}\n\\begin{tabular}{lrrrr}\n\\toprule\n\\textbf{Source} & \\textbf{df} & $F$ & $p$ & $\\eta^2_p$ \\\\\n\\midrule\nGenerator     & 2  & 926.8  & ${<}.001$  & .885 \\\\\nScorer        & 3  & 19.02  & ${<}.001$  & .192 \\\\\nDepth-Pair    & 4  & 24736  & ${<}.001$  & .998 \\\\\nGen$\\times$Scorer & 6 & 8.16 & ${<}.001$ & .170 \\\\\nGen$\\times$Depth  & 8 & 993.7 & ${<}.001$ & .971 \\\\\nScorer$\\times$Depth & 12 & 2.45 & .005 & .109 \\\\\nResidual      & 240 & & & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Feature Importance Across Decoding Strategies}\n\nFeature importance ordering varies across decoding strategies: greedy and $T{=}0.7$ share highly correlated rankings ($\\rho = 0.914$), while greedy vs.\\ $T{=}1.2$ yields lower correlation ($\\rho = 0.53$, nonsignificant after Bonferroni).\nThe depth boundary is robust but the optimal feature subset is strategy-dependent.\n\n\\subsection{Scale and Neural Probe}\n\\label{sec:extended_neural_probe}\n\nCross-scale validation supports $\\Kempirical = 2$ from 1.5B through 8B: Qwen-7B (1v2 $\\auc = 0.6168$ $[0.608, 0.626]$) and LLaMA-3.1-8B (1v2 $\\auc = 0.6123$, 0v1 $= 0.9225$) both exceed $\\theta$, with progressively lower 0v1 signal consistent with larger models generating more human-like text. Scaling to 13B+ remains open.\n\nThe neural probe yields model-dependent $\\Kempirical^{\\text{neural}}$: $3$ for Qwen (self-familiarity effect from instruction-tuned representations) but $2$ for Pythia and OLMo, matching the 15D boundary.\nThe 15D model-free features yield $\\Kempirical = 2$ consistently across all three model families, supporting their role as a robust lower bound.\n\n\\subsection{LLM Zero-Shot Baseline}\n\\label{sec:extended_llm}\n\nGPT-5.5 achieves 33.2\\% accuracy (MAE = 1.10) and Claude Opus~4.6 33.1\\% (MAE = 1.15) on a balanced 500-sample test set, comparable to OBD-LightGBM's 38.0\\% (95\\% CI: $[0.340, 0.422]$; McNemar $p = 0.081$, $0.069$; Table~\\ref{tab:s3_llm_zeroshot}).\nPer-depth recall confirms convergent failure at depths $\\geq 2$ (Section~\\ref{sec:why_kstar}).\nWhen 6-class probabilities are marginalized to 5 classes ($P(d{\\geq}4)$), accuracy rises to 44.4\\% but concentrates in depth-4 (recall: 22\\%$\\to$80\\%) while depths 2--3 collapse to 2--8\\%; we report raw 6-class results.\n\n\\subsection{Practical Considerations}\n\nAll filtering strategies degrade general capabilities (MMLU: 0.6018 $\\to$ 0.5865--0.5941; HellaSwag: 0.6821 $\\to$ 0.6638--0.6701); our 100\\% synthetic setting is an upper bound; in mixed corpora, degradation scales with contamination fraction~\\cite{shumailov2024collapse, dohmatob2024model}.\n$\\Kstar$-aware binary filtering reduces MMLU degradation by ${\\sim}$50\\% ($-$1.53\\,pp $\\to$ $-$0.77\\,pp), requires no per-model calibration, and is combinable with distribution-matching methods (DSIR, DoReMi).",
  "new_string": "\\section{Extended Analysis and Limitations}\n\\label{sec:extended_discussion}\n\nThis section provides supporting tables for cross-scorer validation (Tables~\\ref{tab:crossscorer}--\\ref{tab:anova_crossscorer}), followed by extended limitations, ablation studies, and domain-specific analyses.\n\n\\noindent\\begin{minipage}{\\columnwidth}\n\\centering\n\\captionof{table}{Cross-scorer validation on Qwen-generated text. Alternative scorers (Pythia-1.4B, OLMo-1B) preserve feature ranking ($\\rho > 0.90$) and rewrite-mode $\\Kempirical = 2$, but reduce continuation-mode $\\Kempirical$ from 2 to 1.}\n\\label{tab:crossscorer}\n\\resizebox{\\columnwidth}{!}{\\input{tables/tab_crossscorer}}\n\\end{minipage}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Three-way ANOVA (Generator $\\times$ Scorer $\\times$ Depth-Pair) on per-fold pairwise $\\auc$ values (Type~II SS). DV = per-fold AUC; $N{=}300$ (12 cells $\\times$ 5 folds $\\times$ 5 depth-pairs; 3 generators $\\times$ 4 scorers). Scorer is statistically significant ($p < .001$) but has a small effect size ($\\eta^2_p = 0.19$) relative to Depth-Pair ($\\eta^2_p = 1.00$) and Generator ($\\eta^2_p = 0.89$), indicating that scorer choice has a detectable but practically minor influence on depth discrimination.}\n\\label{tab:anova_crossscorer}\n\\begin{tabular}{lrrrr}\n\\toprule\n\\textbf{Source} & \\textbf{df} & $F$ & $p$ & $\\eta^2_p$ \\\\\n\\midrule\nGenerator     & 2  & 926.8  & ${<}.001$  & .885 \\\\\nScorer        & 3  & 19.02  & ${<}.001$  & .192 \\\\\nDepth-Pair    & 4  & 24736  & ${<}.001$  & .998 \\\\\nGen$\\times$Scorer & 6 & 8.16 & ${<}.001$ & .170 \\\\\nGen$\\times$Depth  & 8 & 993.7 & ${<}.001$ & .971 \\\\\nScorer$\\times$Depth & 12 & 2.45 & .005 & .109 \\\\\nResidual      & 240 & & & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eb278f59-e97a-48f1-a864-bb47aeee4090",
  "isSidechain": false,
  "requestId": "req_011Cb9Z3aKGp5EvzqvQJReo3",
  "type": "assistant",
  "uuid": "28572707-9dd2-48b9-a1da-01de1b6addaf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/paper_agent_e65ef40e",
  "sessionId": "952e4180-a1dd-4838-893f-04003731e881",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "frolicking-frolicking-dahl",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JEtvPGmvD7fWesz7NQEFRt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3604,
      "cache_read_input_tokens": 135518,
      "output_tokens": 2823,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3604,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2823,
          "cache_read_input_tokens": 135518,
          "cache_creation_input_tokens": 3604,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3604
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

_source line 8099 · 2026-05-18T06:23:13.989Z_

<details><summary>↩ Tool result · `toolu_01XQWUiQi5Ra8PJCEMvJ5rpd`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "28572707-9dd2-48b9-a1da-01de1b6addaf",
  "isSidechain": false,
  "promptId": "8dba7b96-5a22-445a-882e-3856dafbad00",
  "type": "user",
  "uuid": "856394d5-cfeb-49c5-a563-ed33ec42f504",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex",
    "oldString": "\\section{Extended Discussion}\n\\label{sec:extended_discussion}\n\n\\subsection{Theoretical Implications of \\texorpdfstring{$\\Kempirical = 2$}{K*=2}}\n\nThe DPI guarantees a finite $\\Ktheory$; for general web text, $\\Kempirical \\leq 2$ across all 8 configurations (1B--8B, 5 families), while structured domains (arXiv) yield $\\Kempirical{=}3$, aligning with model collapse convergence~\\cite{shumailov2024collapse, dohmatob2024model, alemohammad2024selfconsuming}.\nDecoding strategy modestly affects signal strength (1v2 $\\auc \\in [0.6866, 0.7039]$) but does not shift the boundary.\n\n\\subsection{Cross-Model Transfer Implications}\n\nCross-model classification retains 80--92\\% accuracy with scorer-invariant feature rankings ($\\rho > 0.90$), enabling single-classifier deployment across generators.\nAbsolute discriminability at the $\\Kempirical$ boundary is scorer-sensitive: alternative scorers reduce Qwen-continuation $\\Kempirical$ from 2 to 1, while rewrite-mode $\\Kempirical = 2$ is preserved.\nModel family similarity modulates transfer (Pythia$\\leftrightarrow$OLMo: 90--92\\% vs.\\ Qwen-cont$\\leftrightarrow$OLMo: 80--85\\%).\n\n\\noindent\\begin{minipage}{\\columnwidth}\n\\centering\n\\captionof{table}{Cross-scorer validation on Qwen-generated text. Alternative scorers (Pythia-1.4B, OLMo-1B) preserve feature ranking ($\\rho > 0.90$) and rewrite-mode $\\Kempirical = 2$, but reduce continuation-mode $\\Kempirical$ from 2 to 1.}\n\\label{tab:crossscorer}\n\\resizebox{\\columnwidth}{!}{\\input{tables/tab_crossscorer}}\n\\end{minipage}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Three-way ANOVA (Generator $\\times$ Scorer $\\times$ Depth-Pair) on per-fold pairwise $\\auc$ values (Type~II SS). DV = per-fold AUC; $N{=}300$ (12 cells $\\times$ 5 folds $\\times$ 5 depth-pairs; 3 generators $\\times$ 4 scorers). Scorer is statistically significant ($p < .001$) but has a small effect size ($\\eta^2_p = 0.19$) relative to Depth-Pair ($\\eta^2_p = 1.00$) and Generator ($\\eta^2_p = 0.89$), indicating that scorer choice has a detectable but practically minor influence on depth discrimination.}\n\\label{tab:anova_crossscorer}\n\\begin{tabular}{lrrrr}\n\\toprule\n\\textbf{Source} & \\textbf{df} & $F$ & $p$ & $\\eta^2_p$ \\\\\n\\midrule\nGenerator     & 2  & 926.8  & ${<}.001$  & .885 \\\\\nScorer        & 3  & 19.02  & ${<}.001$  & .192 \\\\\nDepth-Pair    & 4  & 24736  & ${<}.001$  & .998 \\\\\nGen$\\times$Scorer & 6 & 8.16 & ${<}.001$ & .170 \\\\\nGen$\\times$Depth  & 8 & 993.7 & ${<}.001$ & .971 \\\\\nScorer$\\times$Depth & 12 & 2.45 & .005 & .109 \\\\\nResidual      & 240 & & & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Feature Importance Across Decoding Strategies}\n\nFeature importance ordering varies across decoding strategies: greedy and $T{=}0.7$ share highly correlated rankings ($\\rho = 0.914$), while greedy vs.\\ $T{=}1.2$ yields lower correlation ($\\rho = 0.53$, nonsignificant after Bonferroni).\nThe depth boundary is robust but the optimal feature subset is strategy-dependent.\n\n\\subsection{Scale and Neural Probe}\n\\label{sec:extended_neural_probe}\n\nCross-scale validation supports $\\Kempirical = 2$ from 1.5B through 8B: Qwen-7B (1v2 $\\auc = 0.6168$ $[0.608, 0.626]$) and LLaMA-3.1-8B (1v2 $\\auc = 0.6123$, 0v1 $= 0.9225$) both exceed $\\theta$, with progressively lower 0v1 signal consistent with larger models generating more human-like text. Scaling to 13B+ remains open.\n\nThe neural probe yields model-dependent $\\Kempirical^{\\text{neural}}$: $3$ for Qwen (self-familiarity effect from instruction-tuned representations) but $2$ for Pythia and OLMo, matching the 15D boundary.\nThe 15D model-free features yield $\\Kempirical = 2$ consistently across all three model families, supporting their role as a robust lower bound.\n\n\\subsection{LLM Zero-Shot Baseline}\n\\label{sec:extended_llm}\n\nGPT-5.5 achieves 33.2\\% accuracy (MAE = 1.10) and Claude Opus~4.6 33.1\\% (MAE = 1.15) on a balanced 500-sample test set, comparable to OBD-LightGBM's 38.0\\% (95\\% CI: $[0.340, 0.422]$; McNemar $p = 0.081$, $0.069$; Table~\\ref{tab:s3_llm_zeroshot}).\nPer-depth recall confirms convergent failure at depths $\\geq 2$ (Section~\\ref{sec:why_kstar}).\nWhen 6-class probabilities are marginalized to 5 classes ($P(d{\\geq}4)$), accuracy rises to 44.4\\% but concentrates in depth-4 (recall: 22\\%$\\to$80\\%) while depths 2--3 collapse to 2--8\\%; we report raw 6-class results.\n\n\\subsection{Practical Considerations}\n\nAll filtering strategies degrade general capabilities (MMLU: 0.6018 $\\to$ 0.5865--0.5941; HellaSwag: 0.6821 $\\to$ 0.6638--0.6701); our 100\\% synthetic setting is an upper bound; in mixed corpora, degradation scales with contamination fraction~\\cite{shumailov2024collapse, dohmatob2024model}.\n$\\Kstar$-aware binary filtering reduces MMLU degradation by ${\\sim}$50\\% ($-$1.53\\,pp $\\to$ $-$0.77\\,pp), requires no per-model calibration, and is combinable with distribution-matching methods (DSIR, DoReMi).",
    "newString": "\\section{Extended Analysis and Limitations}\n\\label{sec:extended_discussion}\n\nThis section provides supporting tables for cross-scorer validation (Tables~\\ref{tab:crossscorer}--\\ref{tab:anova_crossscorer}), followed by extended limitations, ablation studies, and domain-specific analyses.\n\n\\noindent\\begin{minipage}{\\columnwidth}\n\\centering\n\\captionof{table}{Cross-scorer validation on Qwen-generated text. Alternative scorers (Pythia-1.4B, OLMo-1B) preserve feature ranking ($\\rho > 0.90$) and rewrite-mode $\\Kempirical = 2$, but reduce continuation-mode $\\Kempirical$ from 2 to 1.}\n\\label{tab:crossscorer}\n\\resizebox{\\columnwidth}{!}{\\input{tables/tab_crossscorer}}\n\\end{minipage}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Three-way ANOVA (Generator $\\times$ Scorer $\\times$ Depth-Pair) on per-fold pairwise $\\auc$ values (Type~II SS). DV = per-fold AUC; $N{=}300$ (12 cells $\\times$ 5 folds $\\times$ 5 depth-pairs; 3 generators $\\times$ 4 scorers). Scorer is statistically significant ($p < .001$) but has a small effect size ($\\eta^2_p = 0.19$) relative to Depth-Pair ($\\eta^2_p = 1.00$) and Generator ($\\eta^2_p = 0.89$), indicating that scorer choice has a detectable but practically minor influence on depth discrimination.}\n\\label{tab:anova_crossscorer}\n\\begin{tabular}{lrrrr}\n\\toprule\n\\textbf{Source} & \\textbf{df} & $F$ & $p$ & $\\eta^2_p$ \\\\\n\\midrule\nGenerator     & 2  & 926.8  & ${<}.001$  & .885 \\\\\nScorer        & 3  & 19.02  & ${<}.001$  & .192 \\\\\nDepth-Pair    & 4  & 24736  & ${<}.001$  & .998 \\\\\nGen$\\times$Scorer & 6 & 8.16 & ${<}.001$ & .170 \\\\\nGen$\\times$Depth  & 8 & 993.7 & ${<}.001$ & .971 \\\\\nScorer$\\times$Depth & 12 & 2.45 & .005 & .109 \\\\\nResidual      & 240 & & & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 17,
        "newStart": 1,
        "newLines": 8,
        "lines": [
          "-\\section{Extended Discussion}",
          "+\\section{Extended Analysis and Limitations}",
          " \\label{sec:extended_discussion}",
          " ",
          "-\\subsection{Theoretical Implications of \\texorpdfstring{$\\Kempirical = 2$}{K*=2}}",
          "+This section provides supporting tables for cross-scorer validation (Tables~\\ref{tab:crossscorer}--\\ref{tab:anova_crossscorer}), followed by extended limitations, ablation studies, and domain-specific analyses.",
          " ",
          "-The DPI guarantees a finite $\\Ktheory$; for general web text, $\\Kempirical \\leq 2$ across all 8 configurations (1B--8B, 5 families), while structured domains (arXiv) yield $\\Kempirical{=}3$, aligning with model collapse convergence~\\cite{shumailov2024collapse, dohmatob2024model, alemohammad2024selfconsuming}.",
          "-Decoding strategy modestly affects signal strength (1v2 $\\auc \\in [0.6866, 0.7039]$) but does not shift the boundary.",
          "-",
          "-\\subsection{Cross-Model Transfer Implications}",
          "-",
          "-Cross-model classification retains 80--92\\% accuracy with scorer-invariant feature rankings ($\\rho > 0.90$), enabling single-classifier deployment across generators.",
          "-Absolute discriminability at the $\\Kempirical$ boundary is scorer-sensitive: alternative scorers reduce Qwen-continuation $\\Kempirical$ from 2 to 1, while rewrite-mode $\\Kempirical = 2$ is preserved.",
          "-Model family similarity modulates transfer (Pythia$\\leftrightarrow$OLMo: 90--92\\% vs.\\ Qwen-cont$\\leftrightarrow$OLMo: 80--85\\%).",
          "-",
          " \\noindent\\begin{minipage}{\\columnwidth}",
          " \\centering",
          " \\captionof{table}{Cross-scorer validation on Qwen-generated text. Alternative scorers (Pythia-1.4B, OLMo-1B) preserve feature ranking ($\\rho > 0.90$) and rewrite-mode $\\Kempirical = 2$, but reduce continuation-mode $\\Kempirical$ from 2 to 1.}"
        ]
      },
      {
        "oldStart": 39,
        "oldLines": 31,
        "newStart": 30,
        "newLines": 6,
        "lines": [
          " \\end{tabular}",
          " \\end{table}",
          " ",
          "-\\subsection{Feature Importance Across Decoding Strategies}",
          "-",
          "-Feature importance ordering varies across decoding strategies: greedy and $T{=}0.7$ share highly correlated rankings ($\\rho = 0.914$), while greedy vs.\\ $T{=}1.2$ yields lower correlation ($\\rho = 0.53$, nonsignificant after Bonferroni).",
          "-The depth boundary is robust but the optimal feature subset is strategy-dependent.",
          "-",
          "-\\subsection{Scale and Neural Probe}",
          "-\\label{sec:extended_neural_probe}",
          "-",
          "-Cross-scale validation supports $\\Kempirical = 2$ from 1.5B through 8B: Qwen-7B (1v2 $\\auc = 0.6168$ $[0.608, 0.626]$) and LLaMA-3.1-8B (1v2 $\\auc = 0.6123$, 0v1 $= 0.9225$) both exceed $\\theta$, with progressively lower 0v1 signal consistent with larger models generating more human-like text. Scaling to 13B+ remains open.",
          "-",
          "-The neural probe yields model-dependent $\\Kempirical^{\\text{neural}}$: $3$ for Qwen (self-familiarity effect from instruction-tuned representations) but $2$ for Pythia and OLMo, matching the 15D boundary.",
          "-The 15D model-free features yield $\\Kempirical = 2$ consistently across all three model families, supporting their role as a robust lower bound.",
          "-",
          "-\\subsection{LLM Zero-Shot Baseline}",
          "-\\label{sec:extended_llm}",
          "-",
          "-GPT-5.5 achieves 33.2\\% accuracy (MAE = 1.10) and Claude Opus~4.6 33.1\\% (MAE = 1.15) on a balanced 500-sample test set, comparable to OBD-LightGBM's 38.0\\% (95\\% CI: $[0.340, 0.422]$; McNemar $p = 0.081$, $0.069$; Table~\\ref{tab:s3_llm_zeroshot}).",
          "-Per-depth recall confirms convergent failure at depths $\\geq 2$ (Section~\\ref{sec:why_kstar}).",
          "-When 6-class probabilities are marginalized to 5 classes ($P(d{\\geq}4)$), accuracy rises to 44.4\\% but concentrates in depth-4 (recall: 22\\%$\\to$80\\%) while depths 2--3 collapse to 2--8\\%; we report raw 6-class results.",
          "-",
          "-\\subsection{Practical Considerations}",
          "-",
          "-All filtering strategies degrade general capabilities (MMLU: 0.6018 $\\to$ 0.5865--0.5941; HellaSwag: 0.6821 $\\to$ 0.6638--0.6701); our 100\\% synthetic setting is an upper bound; in mixed corpora, degradation scales with contamination fraction~\\cite{shumailov2024collapse, dohmatob2024model}.",
          "-$\\Kstar$-aware binary filtering reduces MMLU degradation by ${\\sim}$50\\% ($-$1.53\\,pp $\\to$ $-$0.77\\,pp), requires no per-model calibration, and is combinable with distribution-matching methods (DSIR, DoReMi).",
          "-",
          " \\subsection{Extended Limitations}",
          " \\label{sec:extended_limitations}",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "28572707-9dd2-48b9-a1da-01de1b6addaf",
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


### Runtime record

_source line 8100 · 2026-05-18T06:23:13.995Z_

```json
{
  "parentUuid": "856394d5-cfeb-49c5-a563-ed33ec42f504",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "f68979a6-44db-40f1-a5d1-500f510082d0",
  "timestamp": "2026-05-18T06:23:13.995Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/paper_agent_e65ef40e",
  "sessionId": "952e4180-a1dd-4838-893f-04003731e881",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "frolicking-frolicking-dahl"
}
```

---


### Assistant

_source line 8101 · 2026-05-18T06:23:18.413Z_

Now fix issue #2 (Page 12 whitespace). The per-depth recall table floats to bottom. Change placement from `[!htbp]` to `[t]`.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f68979a6-44db-40f1-a5d1-500f510082d0",
  "isSidechain": false,
  "requestId": "req_011Cb9Z6b8UTmvcxfUSbaaPy",
  "type": "assistant",
  "uuid": "90fbbc1b-a1dd-4c25-8db2-cbe8c90455b8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/paper_agent_e65ef40e",
  "sessionId": "952e4180-a1dd-4838-893f-04003731e881",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "frolicking-frolicking-dahl",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SgbJUov5H9gHQBNotnMks1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2984,
      "cache_read_input_tokens": 139122,
      "output_tokens": 382,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2984,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 382,
          "cache_read_input_tokens": 139122,
          "cache_creation_input_tokens": 2984,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2984
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


### Tool call

_source line 8102 · 2026-05-18T06:23:21.722Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01KVH8r19feGFEsi26ZPjqFr`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex",
  "old_string": "\\begin{table}[!htbp]\n  \\centering\n  \\small\n  \\caption{Per-depth recall (\\%) on balanced $N{=}500$ test set. OBD's nominal overall accuracy gap originates from depth-0; all methods fail at depths $\\geq 2$, consistent with $\\Kempirical = 2$.}\n  \\label{tab:s3c_perdepth}",
  "new_string": "\\begin{table}[t]\n  \\centering\n  \\small\n  \\caption{Per-depth recall (\\%) on balanced $N{=}500$ test set. OBD's nominal overall accuracy gap originates from depth-0; all methods fail at depths $\\geq 2$, consistent with $\\Kempirical = 2$.}\n  \\label{tab:s3c_perdepth}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "90fbbc1b-a1dd-4c25-8db2-cbe8c90455b8",
  "isSidechain": false,
  "requestId": "req_011Cb9Z6b8UTmvcxfUSbaaPy",
  "type": "assistant",
  "uuid": "c6dbd2ec-f3cc-4c94-8927-026a492b07f3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/paper_agent_e65ef40e",
  "sessionId": "952e4180-a1dd-4838-893f-04003731e881",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "frolicking-frolicking-dahl",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SgbJUov5H9gHQBNotnMks1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2984,
      "cache_read_input_tokens": 139122,
      "output_tokens": 382,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2984,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 382,
          "cache_read_input_tokens": 139122,
          "cache_creation_input_tokens": 2984,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2984
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

_source line 8103 · 2026-05-18T06:23:21.734Z_

<details><summary>↩ Tool result · `toolu_01KVH8r19feGFEsi26ZPjqFr`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c6dbd2ec-f3cc-4c94-8927-026a492b07f3",
  "isSidechain": false,
  "promptId": "8dba7b96-5a22-445a-882e-3856dafbad00",
  "type": "user",
  "uuid": "b40eac25-b260-4403-84c8-a657d6778641",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex",
    "oldString": "\\begin{table}[!htbp]\n  \\centering\n  \\small\n  \\caption{Per-depth recall (\\%) on balanced $N{=}500$ test set. OBD's nominal overall accuracy gap originates from depth-0; all methods fail at depths $\\geq 2$, consistent with $\\Kempirical = 2$.}\n  \\label{tab:s3c_perdepth}",
    "newString": "\\begin{table}[t]\n  \\centering\n  \\small\n  \\caption{Per-depth recall (\\%) on balanced $N{=}500$ test set. OBD's nominal overall accuracy gap originates from depth-0; all methods fail at depths $\\geq 2$, consistent with $\\Kempirical = 2$.}\n  \\label{tab:s3c_perdepth}",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 173,
        "oldLines": 7,
        "newStart": 173,
        "newLines": 7,
        "lines": [
          "   \\end{subtable}",
          " \\end{table*}",
          " ",
          "-\\begin{table}[!htbp]",
          "+\\begin{table}[t]",
          "   \\centering",
          "   \\small",
          "   \\caption{Per-depth recall (\\%) on balanced $N{=}500$ test set. OBD's nominal overall accuracy gap originates from depth-0; all methods fail at depths $\\geq 2$, consistent with $\\Kempirical = 2$.}"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "c6dbd2ec-f3cc-4c94-8927-026a492b07f3",
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

_source line 8104 · 2026-05-18T06:23:25.828Z_

Also fix Page 17 whitespace: remove `\clearpage` before "Supplementary Details" and change table placement.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b40eac25-b260-4403-84c8-a657d6778641",
  "isSidechain": false,
  "requestId": "req_011Cb9Z7AK1CspvEK2qpx4dn",
  "type": "assistant",
  "uuid": "2ba691de-4941-4ef7-ad41-a1246d4902b6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/paper_agent_e65ef40e",
  "sessionId": "952e4180-a1dd-4838-893f-04003731e881",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "frolicking-frolicking-dahl",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018o233RGgo54A8Ddcvnbr66",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 437,
      "cache_read_input_tokens": 142106,
      "output_tokens": 151,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 437,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 151,
          "cache_read_input_tokens": 142106,
          "cache_creation_input_tokens": 437,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 437
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


### Tool call

_source line 8105 · 2026-05-18T06:23:26.319Z_

<details open><summary>🔧 Tool call — Read · `toolu_01ALeBhw8RRhtUnvxPc79mVN`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex",
  "offset": 218,
  "limit": 10
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2ba691de-4941-4ef7-ad41-a1246d4902b6",
  "isSidechain": false,
  "requestId": "req_011Cb9Z7AK1CspvEK2qpx4dn",
  "type": "assistant",
  "uuid": "105181fd-9422-4d16-8d58-c34f838ed53e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/paper_agent_e65ef40e",
  "sessionId": "952e4180-a1dd-4838-893f-04003731e881",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "frolicking-frolicking-dahl",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018o233RGgo54A8Ddcvnbr66",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 437,
      "cache_read_input_tokens": 142106,
      "output_tokens": 151,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 437,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 151,
          "cache_read_input_tokens": 142106,
          "cache_creation_input_tokens": 437,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 437
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

_source line 8106 · 2026-05-18T06:23:26.325Z_

<details><summary>↩ Tool result · `toolu_01ALeBhw8RRhtUnvxPc79mVN`</summary>

```text
218	
219	  \vspace{4pt}
220	  \footnotesize
221	  EOS truncation rate: percentage of depth~1+ samples where generation terminated via EOS before reaching the 256-token limit. Ranges span depths 1--5.
222	\end{table*}
223	
224	\clearpage
225	\section{Supplementary Details}
226	
227	%%% Table S4: Dataset Statistics
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "105181fd-9422-4d16-8d58-c34f838ed53e",
  "isSidechain": false,
  "promptId": "8dba7b96-5a22-445a-882e-3856dafbad00",
  "type": "user",
  "uuid": "3322b2fb-52c7-4a8a-ba3f-c236dbfffa94",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex",
      "content": "\n  \\vspace{4pt}\n  \\footnotesize\n  EOS truncation rate: percentage of depth~1+ samples where generation terminated via EOS before reaching the 256-token limit. Ranges span depths 1--5.\n\\end{table*}\n\n\\clearpage\n\\section{Supplementary Details}\n\n%%% Table S4: Dataset Statistics",
      "numLines": 10,
      "startLine": 218,
      "totalLines": 500
    }
  },
  "sourceToolAssistantUUID": "105181fd-9422-4d16-8d58-c34f838ed53e",
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


### Runtime record

_source line 8107_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Director 指令] Reviewer visual review 发现 4 个排版问题：  **1. [必修] Page 11 feature ranking table 溢出** appendix.tex ~L26-35 (tab:top_features)，`\\texttt{}` feature 名过宽导致最右列侵入右栏。修复：`\\resizebox{\\columnwidth}{!}{…",
  "leafUuid": "3322b2fb-52c7-4a8a-ba3f-c236dbfffa94",
  "sessionId": "952e4180-a1dd-4838-893f-04003731e881"
}
```

---


### Runtime record

_source line 8108_

```json
{
  "type": "ai-title",
  "aiTitle": "Report agent results to director",
  "sessionId": "952e4180-a1dd-4838-893f-04003731e881"
}
```

---


### Tool call

_source line 8109 · 2026-05-18T06:23:29.834Z_

<details open><summary>🔧 Tool call — Edit · `toolu_017L8fqrcxBkmD6VbnneCKBQ`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex",
  "old_string": "\\clearpage\n\\section{Supplementary Details}",
  "new_string": "\\section{Supplementary Details}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3322b2fb-52c7-4a8a-ba3f-c236dbfffa94",
  "isSidechain": false,
  "requestId": "req_011Cb9Z7W2utBzzWV4nVd6xm",
  "type": "assistant",
  "uuid": "18bb8d8f-d068-4291-9f0a-16a7eac3539f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/paper_agent_e65ef40e",
  "sessionId": "952e4180-a1dd-4838-893f-04003731e881",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "frolicking-frolicking-dahl",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Kp4DedtJTe79catQktQdYv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 268,
      "cache_read_input_tokens": 142543,
      "output_tokens": 162,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 268,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 162,
          "cache_read_input_tokens": 142543,
          "cache_creation_input_tokens": 268,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 268
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

_source line 8110 · 2026-05-18T06:23:29.849Z_

<details><summary>↩ Tool result · `toolu_017L8fqrcxBkmD6VbnneCKBQ`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "18bb8d8f-d068-4291-9f0a-16a7eac3539f",
  "isSidechain": false,
  "promptId": "8dba7b96-5a22-445a-882e-3856dafbad00",
  "type": "user",
  "uuid": "68ff2b9d-305c-45ea-b0f4-8b05d3963569",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex",
    "oldString": "\\clearpage\n\\section{Supplementary Details}",
    "newString": "\\section{Supplementary Details}",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 221,
        "oldLines": 7,
        "newStart": 221,
        "newLines": 6,
        "lines": [
          "   EOS truncation rate: percentage of depth~1+ samples where generation terminated via EOS before reaching the 256-token limit. Ranges span depths 1--5.",
          " \\end{table*}",
          " ",
          "-\\clearpage",
          " \\section{Supplementary Details}",
          " ",
          " %%% Table S4: Dataset Statistics"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "18bb8d8f-d068-4291-9f0a-16a7eac3539f",
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

_source line 8111 · 2026-05-18T06:23:33.357Z_

Now compile to check the results.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "68ff2b9d-305c-45ea-b0f4-8b05d3963569",
  "isSidechain": false,
  "requestId": "req_011Cb9Z7mHBtALcpBVHyuJeV",
  "type": "assistant",
  "uuid": "efaa5787-bdd8-4296-bb55-10b22429631d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/paper_agent_e65ef40e",
  "sessionId": "952e4180-a1dd-4838-893f-04003731e881",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "frolicking-frolicking-dahl",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01APuV2GbR7PA5yy7tCq3s3p",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 217,
      "cache_read_input_tokens": 142811,
      "output_tokens": 96,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 217,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 96,
          "cache_read_input_tokens": 142811,
          "cache_creation_input_tokens": 217,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 217
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


### Tool call

_source line 8112 · 2026-05-18T06:23:33.748Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__paper_compile_and_check · `toolu_017y14PTzLfycWt35U5gFBRV`</summary>

```json
{
  "project": "gen-depth-contamination",
  "clean": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "efaa5787-bdd8-4296-bb55-10b22429631d",
  "isSidechain": false,
  "requestId": "req_011Cb9Z7mHBtALcpBVHyuJeV",
  "type": "assistant",
  "uuid": "602a6a99-fd43-423a-81fb-ccf1ec42bb4f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/paper_agent_e65ef40e",
  "sessionId": "952e4180-a1dd-4838-893f-04003731e881",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "frolicking-frolicking-dahl",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01APuV2GbR7PA5yy7tCq3s3p",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 217,
      "cache_read_input_tokens": 142811,
      "output_tokens": 96,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 217,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 96,
          "cache_read_input_tokens": 142811,
          "cache_creation_input_tokens": 217,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 217
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

_source line 8113 · 2026-05-18T06:23:38.438Z_

<details><summary>↩ Tool result · `toolu_017y14PTzLfycWt35U5gFBRV`</summary>

```text
{"result":"{\"success\": true, \"passed\": true, \"compiled\": {\"success\": true, \"pdf_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.pdf\", \"paper_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper\", \"main_tex\": \"main.tex\", \"log_tail\": \"\\nUnderfull \\\\hbox (badness 10000) in paragraph at lines 217--220\\n []\\\\T1/ptm/b/n/10.95 (+20) Per-fold trans-parency.[] \\\\T1/ptm/m/n/10.95 (+20) Fo\\nr Qwen-1.5B,\\n []\\n\\n\\nUnderfull \\\\hbox (badness 10000) in paragraph at lines 217--220\\n\\\\T1/ptm/m/n/10.95 (+20) cross-family scor-ing (Pythia-1.4B) yields\\n []\\n\\n\\nUnderfull \\\\hbox (badness 3623) in paragraph at lines 217--220\\n[]$\\\\T1/ptm/m/n/10.95 (+20) (1v2) $\\\\OT1/cmr/m/n/10.95 = 0\\\\OML/cmm/m/it/10.95 :\\\\O\\nT1/cmr/m/n/10.95 5994$\\\\T1/ptm/m/n/10.95 (+20) , with per-fold val-ues\\n []\\n\\n\\nUnderfull \\\\hbox (badness 10000) in paragraph at lines 217--220\\n\\\\OT1/cmr/m/n/10.95 [0\\\\OML/cmm/m/it/10.95 :\\\\OT1/cmr/m/n/10.95 596\\\\OML/cmm/m/it/1\\n0.95 ; \\\\OT1/cmr/m/n/10.95 0\\\\OML/cmm/m/it/10.95 :\\\\OT1/cmr/m/n/10.95 606\\\\OML/cmm/\\nm/it/10.95 ; \\\\OT1/cmr/m/n/10.95 0\\\\OML/cmm/m/it/10.95 :\\\\OT1/cmr/m/n/10.95 600\\\\OM\\nL/cmm/m/it/10.95 ; \\\\OT1/cmr/m/n/10.95 0\\\\OML/cmm/m/it/10.95 :\\\\OT1/cmr/m/n/10.95 \\n603\\\\OML/cmm/m/it/10.95 ; \\\\OT1/cmr/m/n/10.95 0\\\\OML/cmm/m/it/10.95 :\\\\OT1/cmr/m/n/\\n10.95 592]$ \\\\T1/ptm/m/n/10.95 (+20) (2/5 folds\\n []\\n\\n[22]) [23\\n\\n] (./main.aux)\\n ***********\\nLaTeX2e <2025-11-01>\\nL3 programming layer <2026-01-19>\\n ***********\\nPackage rerunfilecheck Info: File `main.out' has not changed.\\n(rerunfilecheck)             Checksum: 70778F638ABCE1F2FB926BAACEEE54B2;4475.\\n ) \\nHere is how much of TeX's memory you used:\\n 16717 strings out of 469438\\n 263744 string characters out of 5468411\\n 753651 words of memory out of 5000000\\n 44496 multiletter control sequences out of 15000+600000\\n 722430 words of font info for 431 fonts, out of 8000000 for 9000\\n 59 hyphenation exceptions out of 8191\\n 84i,16n,93p,1001b,662s stack positions out of 10000i,1000n,20000p,200000b,200000s\\n&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cmextra/cmbsy6.pfb\\n>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr\\n/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx9.pfb>&lt;/usr/share/\\ntexlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texliv\\ne/texmf-dist/fonts/type1/public/amsfonts/cmextra/cmex9.pfb>&lt;/usr/share/texlive/\\ntexmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-\\ndist/fonts/type1/public/amsfonts/cm/cmmi12.pfb>&lt;/usr/share/texlive/texmf-dist/f\\nonts/type1/public/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\\npe1/public/amsfonts/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub\\nlic/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams\\nfonts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/c\\nmextra/cmmib9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm\\n/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr6.p\\nfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr\\n/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/t\\nexlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/share/texlive/t\\nexmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-d\\nist/fonts/type1/public/amsfonts/cm/cmsy6.pfb>&lt;/usr/share/texlive/texmf-dist/fon\\nts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type\\n1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publi\\nc/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfo\\nnts/symbols/msam10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfon\\nts/symbols/msbm10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/courier/uc\\nrb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/courier/ucrr8a.pfb>&lt;/us\\nr/share/texlive/texmf-dist/fonts/type1/urw/helvetic/uhvb8a.pfb>&lt;/usr/share/texl\\nive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/\\nfonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw\\n/times/utmri8a.pfb>\\nOutput written on main.pdf (23 pages, 564351 bytes).\\nPDF statistics:\\n 1264 PDF objects out of 1440 (max. 8388607)\\n 742 compressed objects within 8 object streams\\n 145 named destinations out of 1000 (max. 500000)\\n 86260 words of extra memory for PDF output out of 89155 (max. 10000000)\\n\", \"error\": \"\", \"pages\": 23, \"warnings\": [\"The option `hypcap=true' will be ignored for this\", \"The option `hypcap=true' will be ignored for this\", \"The option `hypcap=true' will be ignored for this\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\"]}, \"pages\": 23, \"page_status\": \"ok\", \"max_pages\": null, \"min_pages\": null, \"critical_warnings\": [], \"minor_warnings\": [\"The option `hypcap=true' will be ignored for this\", \"The option `hypcap=true' will be ignored for this\", \"The option `hypcap=true' will be ignored for this\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 10--13\", \"Underfull \\\\hbox (badness 1137) in paragraph at lines 10--13\", \"Underfull \\\\hbox (badness 3579) in paragraph at lines 10--13\", \"Underfull \\\\hbox (badness 1895) in paragraph at lines 10--13\", \"Underfull \\\\hbox (badness 1383) in paragraph at lines 10--13\", \"Underfull \\\\hbox (badness 6808) in paragraph at lines 15--16\", \"Underfull \\\\hbox (badness 6725) in paragraph at lines 38--43\", \"Underfull \\\\hbox (badness 8170) in paragraph at lines 50--55\", \"Underfull \\\\vbox (badness 10000) has occurred while \\\\output is active []\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 49--51\", \"Underfull \\\\hbox (badness 2951) in paragraph at lines 49--51\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 74--76\", \"Underfull \\\\hbox (badness 3029) in paragraph at lines 74--76\", \"Underfull \\\\hbox (badness 6204) in paragraph at lines 74--76\", \"Underfull \\\\hbox (badness 2376) in paragraph at lines 74--76\", \"Underfull \\\\hbox (badness 1478) in paragraph at lines 78--85\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 128--132\", \"Underfull \\\\hbox (badness 5446) in paragraph at lines 128--132\", \"Underfull \\\\hbox (badness 1057) in paragraph at lines 128--132\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 128--132\", \"Underfull \\\\hbox (badness 2393) in paragraph at lines 134--138\", \"Underfull \\\\hbox (badness 1253) in paragraph at lines 134--138\", \"Underfull \\\\hbox (badness 1715) in paragraph at lines 16--56\", \"Underfull \\\\hbox (badness 1057) in paragraph at lines 13--13\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 40--43\", \"Underfull \\\\hbox (badness 4556) in paragraph at lines 40--43\", \"Underfull \\\\hbox (badness 4291) in paragraph at lines 40--43\", \"Underfull \\\\hbox (badness 4765) in paragraph at lines 40--43\", \"Underfull \\\\hbox (badness 5036) in paragraph at lines 40--43\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 51--59\", \"Underfull \\\\hbox (badness 1796) in paragraph at lines 51--59\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 51--59\", \"Underfull \\\\hbox (badness 7613) in paragraph at lines 51--59\", \"Underfull \\\\hbox (badness 1122) in paragraph at lines 51--59\", \"Underfull \\\\hbox (badness 7944) in paragraph at lines 61--65\", \"Underfull \\\\hbox (badness 2452) in paragraph at lines 61--65\", \"Underfull \\\\hbox (badness 1484) in paragraph at lines 61--65\", \"Underfull \\\\hbox (badness 1533) in paragraph at lines 61--65\", \"Underfull \\\\hbox (badness 1762) in paragraph at lines 67--59\", \"Underfull \\\\hbox (badness 2351) in paragraph at lines 76--84\", \"Underfull \\\\hbox (badness 8189) in paragraph at lines 94--98\", \"Underfull \\\\hbox (badness 1178) in paragraph at lines 94--98\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 276--276\", \"Underfull \\\\hbox (badness 1400) in paragraph at lines 36--40\", \"Underfull \\\\hbox (badness 1571) in paragraph at lines 36--40\", \"Underfull \\\\hbox (badness 1067) in paragraph at lines 96--100\", \"Underfull \\\\vbox (badness 1412) has occurred while \\\\output is active []\", \"Overfull \\\\hbox (1.31956pt too wide) in paragraph at lines 142--153\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 217--220\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 217--220\", \"Underfull \\\\hbox (badness 3623) in paragraph at lines 217--220\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 217--220\"], \"issues\": [], \"summary\": \"PASS\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "602a6a99-fd43-423a-81fb-ccf1ec42bb4f",
  "isSidechain": false,
  "promptId": "8dba7b96-5a22-445a-882e-3856dafbad00",
  "type": "user",
  "uuid": "c427453e-b726-4f6b-894a-46ac0f4cb73a",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"passed\\\": true, \\\"compiled\\\": {\\\"success\\\": true, \\\"pdf_path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.pdf\\\", \\\"paper_dir\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper\\\", \\\"main_tex\\\": \\\"main.tex\\\", \\\"log_tail\\\": \\\"\\\\nUnderfull \\\\\\\\hbox (badness 10000) in paragraph at lines 217--220\\\\n []\\\\\\\\T1/ptm/b/n/10.95 (+20) Per-fold trans-parency.[] \\\\\\\\T1/ptm/m/n/10.95 (+20) Fo\\\\nr Qwen-1.5B,\\\\n []\\\\n\\\\n\\\\nUnderfull \\\\\\\\hbox (badness 10000) in paragraph at lines 217--220\\\\n\\\\\\\\T1/ptm/m/n/10.95 (+20) cross-family scor-ing (Pythia-1.4B) yields\\\\n []\\\\n\\\\n\\\\nUnderfull \\\\\\\\hbox (badness 3623) in paragraph at lines 217--220\\\\n[]$\\\\\\\\T1/ptm/m/n/10.95 (+20) (1v2) $\\\\\\\\OT1/cmr/m/n/10.95 = 0\\\\\\\\OML/cmm/m/it/10.95 :\\\\\\\\O\\\\nT1/cmr/m/n/10.95 5994$\\\\\\\\T1/ptm/m/n/10.95 (+20) , with per-fold val-ues\\\\n []\\\\n\\\\n\\\\nUnderfull \\\\\\\\hbox (badness 10000) in paragraph at lines 217--220\\\\n\\\\\\\\OT1/cmr/m/n/10.95 [0\\\\\\\\OML/cmm/m/it/10.95 :\\\\\\\\OT1/cmr/m/n/10.95 596\\\\\\\\OML/cmm/m/it/1\\\\n0.95 ; \\\\\\\\OT1/cmr/m/n/10.95 0\\\\\\\\OML/cmm/m/it/10.95 :\\\\\\\\OT1/cmr/m/n/10.95 606\\\\\\\\OML/cmm/\\\\nm/it/10.95 ; \\\\\\\\OT1/cmr/m/n/10.95 0\\\\\\\\OML/cmm/m/it/10.95 :\\\\\\\\OT1/cmr/m/n/10.95 600\\\\\\\\OM\\\\nL/cmm/m/it/10.95 ; \\\\\\\\OT1/cmr/m/n/10.95 0\\\\\\\\OML/cmm/m/it/10.95 :\\\\\\\\OT1/cmr/m/n/10.95 \\\\n603\\\\\\\\OML/cmm/m/it/10.95 ; \\\\\\\\OT1/cmr/m/n/10.95 0\\\\\\\\OML/cmm/m/it/10.95 :\\\\\\\\OT1/cmr/m/n/\\\\n10.95 592]$ \\\\\\\\T1/ptm/m/n/10.95 (+20) (2/5 folds\\\\n []\\\\n\\\\n[22]) [23\\\\n\\\\n] (./main.aux)\\\\n ***********\\\\nLaTeX2e <2025-11-01>\\\\nL3 programming layer <2026-01-19>\\\\n ***********\\\\nPackage rerunfilecheck Info: File `main.out' has not changed.\\\\n(rerunfilecheck)             Checksum: 70778F638ABCE1F2FB926BAACEEE54B2;4475.\\\\n ) \\\\nHere is how much of TeX's memory you used:\\\\n 16717 strings out of 469438\\\\n 263744 string characters out of 5468411\\\\n 753651 words of memory out of 5000000\\\\n 44496 multiletter control sequences out of 15000+600000\\\\n 722430 words of font info for 431 fonts, out of 8000000 for 9000\\\\n 59 hyphenation exceptions out of 8191\\\\n 84i,16n,93p,1001b,662s stack positions out of 10000i,1000n,20000p,200000b,200000s\\\\n&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cmextra/cmbsy6.pfb\\\\n>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr\\\\n/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx9.pfb>&lt;/usr/share/\\\\ntexlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texliv\\\\ne/texmf-dist/fonts/type1/public/amsfonts/cmextra/cmex9.pfb>&lt;/usr/share/texlive/\\\\ntexmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-\\\\ndist/fonts/type1/public/amsfonts/cm/cmmi12.pfb>&lt;/usr/share/texlive/texmf-dist/f\\\\nonts/type1/public/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\\\\npe1/public/amsfonts/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub\\\\nlic/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams\\\\nfonts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/c\\\\nmextra/cmmib9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm\\\\n/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr6.p\\\\nfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr\\\\n/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/t\\\\nexlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/share/texlive/t\\\\nexmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-d\\\\nist/fonts/type1/public/amsfonts/cm/cmsy6.pfb>&lt;/usr/share/texlive/texmf-dist/fon\\\\nts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type\\\\n1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publi\\\\nc/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfo\\\\nnts/symbols/msam10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfon\\\\nts/symbols/msbm10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/courier/uc\\\\nrb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/courier/ucrr8a.pfb>&lt;/us\\\\nr/share/texlive/texmf-dist/fonts/type1/urw/helvetic/uhvb8a.pfb>&lt;/usr/share/texl\\\\nive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/\\\\nfonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw\\\\n/times/utmri8a.pfb>\\\\nOutput written on main.pdf (23 pages, 564351 bytes).\\\\nPDF statistics:\\\\n 1264 PDF objects out of 1440 (max. 8388607)\\\\n 742 compressed objects within 8 object streams\\\\n 145 named destinations out of 1000 (max. 500000)\\\\n 86260 words of extra memory for PDF output out of 89155 (max. 10000000)\\\\n\\\", \\\"error\\\": \\\"\\\", \\\"pages\\\": 23, \\\"warnings\\\": [\\\"The option `hypcap=true' will be ignored for this\\\", \\\"The option `hypcap=true' will be ignored for this\\\", \\\"The option `hypcap=true' will be ignored for this\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\"]}, \\\"pages\\\": 23, \\\"page_status\\\": \\\"ok\\\", \\\"max_pages\\\": null, \\\"min_pages\\\": null, \\\"critical_warnings\\\": [], \\\"minor_warnings\\\": [\\\"The option `hypcap=true' will be ignored for this\\\", \\\"The option `hypcap=true' will be ignored for this\\\", \\\"The option `hypcap=true' will be ignored for this\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"Underfull \\\\\\\\hbox (badness 10000) in paragraph at lines 10--13\\\", \\\"Underfull \\\\\\\\hbox (badness 1137) in paragraph at lines 10--13\\\", \\\"Underfull \\\\\\\\hbox (badness 3579) in paragraph at lines 10--13\\\", \\\"Underfull \\\\\\\\hbox (badness 1895) in paragraph at lines 10--13\\\", \\\"Underfull \\\\\\\\hbox (badness 1383) in paragraph at lines 10--13\\\", \\\"Underfull \\\\\\\\hbox (badness 6808) in paragraph at lines 15--16\\\", \\\"Underfull \\\\\\\\hbox (badness 6725) in paragraph at lines 38--43\\\", \\\"Underfull \\\\\\\\hbox (badness 8170) in paragraph at lines 50--55\\\", \\\"Underfull \\\\\\\\vbox (badness 10000) has occurred while \\\\\\\\output is active []\\\", \\\"Underfull \\\\\\\\hbox (badness 10000) in paragraph at lines 49--51\\\", \\\"Underfull \\\\\\\\hbox (badness 2951) in paragraph at lines 49--51\\\", \\\"Underfull \\\\\\\\hbox (badness 10000) in paragraph at lines 74--76\\\", \\\"Underfull \\\\\\\\hbox (badness 3029) in paragraph at lines 74--76\\\", \\\"Underfull \\\\\\\\hbox (badness 6204) in paragraph at lines 74--76\\\", \\\"Underfull \\\\\\\\hbox (badness 2376) in paragraph at lines 74--76\\\", \\\"Underfull \\\\\\\\hbox (badness 1478) in paragraph at lines 78--85\\\", \\\"Underfull \\\\\\\\hbox (badness 10000) in paragraph at lines 128--132\\\", \\\"Underfull \\\\\\\\hbox (badness 5446) in paragraph at lines 128--132\\\", \\\"Underfull \\\\\\\\hbox (badness 1057) in paragraph at lines 128--132\\\", \\\"Underfull \\\\\\\\hbox (badness 10000) in paragraph at lines 128--132\\\", \\\"Underfull \\\\\\\\hbox (badness 2393) in paragraph at lines 134--138\\\", \\\"Underfull \\\\\\\\hbox (badness 1253) in paragraph at lines 134--138\\\", \\\"Underfull \\\\\\\\hbox (badness 1715) in paragraph at lines 16--56\\\", \\\"Underfull \\\\\\\\hbox (badness 1057) in paragraph at lines 13--13\\\", \\\"Underfull \\\\\\\\hbox (badness 10000) in paragraph at lines 40--43\\\", \\\"Underfull \\\\\\\\hbox (badness 4556) in paragraph at lines 40--43\\\", \\\"Underfull \\\\\\\\hbox (badness 4291) in paragraph at lines 40--43\\\", \\\"Underfull \\\\\\\\hbox (badness 4765) in paragraph at lines 40--43\\\", \\\"Underfull \\\\\\\\hbox (badness 5036) in paragraph at lines 40--43\\\", \\\"Underfull \\\\\\\\hbox (badness 10000) in paragraph at lines 51--59\\\", \\\"Underfull \\\\\\\\hbox (badness 1796) in paragraph at lines 51--59\\\", \\\"Underfull \\\\\\\\hbox (badness 10000) in paragraph at lines 51--59\\\", \\\"Underfull \\\\\\\\hbox (badness 7613) in paragraph at lines 51--59\\\", \\\"Underfull \\\\\\\\hbox (badness 1122) in paragraph at lines 51--59\\\", \\\"Underfull \\\\\\\\hbox (badness 7944) in paragraph at lines 61--65\\\", \\\"Underfull \\\\\\\\hbox (badness 2452) in paragraph at lines 61--65\\\", \\\"Underfull \\\\\\\\hbox (badness 1484) in paragraph at lines 61--65\\\", \\\"Underfull \\\\\\\\hbox (badness 1533) in paragraph at lines 61--65\\\", \\\"Underfull \\\\\\\\hbox (badness 1762) in paragraph at lines 67--59\\\", \\\"Underfull \\\\\\\\hbox (badness 2351) in paragraph at lines 76--84\\\", \\\"Underfull \\\\\\\\hbox (badness 8189) in paragraph at lines 94--98\\\", \\\"Underfull \\\\\\\\hbox (badness 1178) in paragraph at lines 94--98\\\", \\\"Underfull \\\\\\\\hbox (badness 10000) in paragraph at lines 276--276\\\", \\\"Underfull \\\\\\\\hbox (badness 1400) in paragraph at lines 36--40\\\", \\\"Underfull \\\\\\\\hbox (badness 1571) in paragraph at lines 36--40\\\", \\\"Underfull \\\\\\\\hbox (badness 1067) in paragraph at lines 96--100\\\", \\\"Underfull \\\\\\\\vbox (badness 1412) has occurred while \\\\\\\\output is active []\\\", \\\"Overfull \\\\\\\\hbox (1.31956pt too wide) in paragraph at lines 142--153\\\", \\\"Underfull \\\\\\\\hbox (badness 10000) in paragraph at lines 217--220\\\", \\\"Underfull \\\\\\\\hbox (badness 10000) in paragraph at lines 217--220\\\", \\\"Underfull \\\\\\\\hbox (badness 3623) in paragraph at lines 217--220\\\", \\\"Underfull \\\\\\\\hbox (badness 10000) in paragraph at lines 217--220\\\"], \\\"issues\\\": [], \\\"summary\\\": \\\"PASS\\\"}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"passed\": true, \"compiled\": {\"success\": true, \"pdf_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.pdf\", \"paper_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper\", \"main_tex\": \"main.tex\", \"log_tail\": \"\\nUnderfull \\\\hbox (badness 10000) in paragraph at lines 217--220\\n []\\\\T1/ptm/b/n/10.95 (+20) Per-fold trans-parency.[] \\\\T1/ptm/m/n/10.95 (+20) Fo\\nr Qwen-1.5B,\\n []\\n\\n\\nUnderfull \\\\hbox (badness 10000) in paragraph at lines 217--220\\n\\\\T1/ptm/m/n/10.95 (+20) cross-family scor-ing (Pythia-1.4B) yields\\n []\\n\\n\\nUnderfull \\\\hbox (badness 3623) in paragraph at lines 217--220\\n[]$\\\\T1/ptm/m/n/10.95 (+20) (1v2) $\\\\OT1/cmr/m/n/10.95 = 0\\\\OML/cmm/m/it/10.95 :\\\\O\\nT1/cmr/m/n/10.95 5994$\\\\T1/ptm/m/n/10.95 (+20) , with per-fold val-ues\\n []\\n\\n\\nUnderfull \\\\hbox (badness 10000) in paragraph at lines 217--220\\n\\\\OT1/cmr/m/n/10.95 [0\\\\OML/cmm/m/it/10.95 :\\\\OT1/cmr/m/n/10.95 596\\\\OML/cmm/m/it/1\\n0.95 ; \\\\OT1/cmr/m/n/10.95 0\\\\OML/cmm/m/it/10.95 :\\\\OT1/cmr/m/n/10.95 606\\\\OML/cmm/\\nm/it/10.95 ; \\\\OT1/cmr/m/n/10.95 0\\\\OML/cmm/m/it/10.95 :\\\\OT1/cmr/m/n/10.95 600\\\\OM\\nL/cmm/m/it/10.95 ; \\\\OT1/cmr/m/n/10.95 0\\\\OML/cmm/m/it/10.95 :\\\\OT1/cmr/m/n/10.95 \\n603\\\\OML/cmm/m/it/10.95 ; \\\\OT1/cmr/m/n/10.95 0\\\\OML/cmm/m/it/10.95 :\\\\OT1/cmr/m/n/\\n10.95 592]$ \\\\T1/ptm/m/n/10.95 (+20) (2/5 folds\\n []\\n\\n[22]) [23\\n\\n] (./main.aux)\\n ***********\\nLaTeX2e <2025-11-01>\\nL3 programming layer <2026-01-19>\\n ***********\\nPackage rerunfilecheck Info: File `main.out' has not changed.\\n(rerunfilecheck)             Checksum: 70778F638ABCE1F2FB926BAACEEE54B2;4475.\\n ) \\nHere is how much of TeX's memory you used:\\n 16717 strings out of 469438\\n 263744 string characters out of 5468411\\n 753651 words of memory out of 5000000\\n 44496 multiletter control sequences out of 15000+600000\\n 722430 words of font info for 431 fonts, out of 8000000 for 9000\\n 59 hyphenation exceptions out of 8191\\n 84i,16n,93p,1001b,662s stack positions out of 10000i,1000n,20000p,200000b,200000s\\n&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cmextra/cmbsy6.pfb\\n>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr\\n/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx9.pfb>&lt;/usr/share/\\ntexlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texliv\\ne/texmf-dist/fonts/type1/public/amsfonts/cmextra/cmex9.pfb>&lt;/usr/share/texlive/\\ntexmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-\\ndist/fonts/type1/public/amsfonts/cm/cmmi12.pfb>&lt;/usr/share/texlive/texmf-dist/f\\nonts/type1/public/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\\npe1/public/amsfonts/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub\\nlic/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams\\nfonts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/c\\nmextra/cmmib9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm\\n/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr6.p\\nfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr\\n/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/t\\nexlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/share/texlive/t\\nexmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-d\\nist/fonts/type1/public/amsfonts/cm/cmsy6.pfb>&lt;/usr/share/texlive/texmf-dist/fon\\nts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type\\n1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publi\\nc/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfo\\nnts/symbols/msam10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfon\\nts/symbols/msbm10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/courier/uc\\nrb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/courier/ucrr8a.pfb>&lt;/us\\nr/share/texlive/texmf-dist/fonts/type1/urw/helvetic/uhvb8a.pfb>&lt;/usr/share/texl\\nive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/\\nfonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw\\n/times/utmri8a.pfb>\\nOutput written on main.pdf (23 pages, 564351 bytes).\\nPDF statistics:\\n 1264 PDF objects out of 1440 (max. 8388607)\\n 742 compressed objects within 8 object streams\\n 145 named destinations out of 1000 (max. 500000)\\n 86260 words of extra memory for PDF output out of 89155 (max. 10000000)\\n\", \"error\": \"\", \"pages\": 23, \"warnings\": [\"The option `hypcap=true' will be ignored for this\", \"The option `hypcap=true' will be ignored for this\", \"The option `hypcap=true' will be ignored for this\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\"]}, \"pages\": 23, \"page_status\": \"ok\", \"max_pages\": null, \"min_pages\": null, \"critical_warnings\": [], \"minor_warnings\": [\"The option `hypcap=true' will be ignored for this\", \"The option `hypcap=true' will be ignored for this\", \"The option `hypcap=true' will be ignored for this\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 10--13\", \"Underfull \\\\hbox (badness 1137) in paragraph at lines 10--13\", \"Underfull \\\\hbox (badness 3579) in paragraph at lines 10--13\", \"Underfull \\\\hbox (badness 1895) in paragraph at lines 10--13\", \"Underfull \\\\hbox (badness 1383) in paragraph at lines 10--13\", \"Underfull \\\\hbox (badness 6808) in paragraph at lines 15--16\", \"Underfull \\\\hbox (badness 6725) in paragraph at lines 38--43\", \"Underfull \\\\hbox (badness 8170) in paragraph at lines 50--55\", \"Underfull \\\\vbox (badness 10000) has occurred while \\\\output is active []\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 49--51\", \"Underfull \\\\hbox (badness 2951) in paragraph at lines 49--51\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 74--76\", \"Underfull \\\\hbox (badness 3029) in paragraph at lines 74--76\", \"Underfull \\\\hbox (badness 6204) in paragraph at lines 74--76\", \"Underfull \\\\hbox (badness 2376) in paragraph at lines 74--76\", \"Underfull \\\\hbox (badness 1478) in paragraph at lines 78--85\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 128--132\", \"Underfull \\\\hbox (badness 5446) in paragraph at lines 128--132\", \"Underfull \\\\hbox (badness 1057) in paragraph at lines 128--132\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 128--132\", \"Underfull \\\\hbox (badness 2393) in paragraph at lines 134--138\", \"Underfull \\\\hbox (badness 1253) in paragraph at lines 134--138\", \"Underfull \\\\hbox (badness 1715) in paragraph at lines 16--56\", \"Underfull \\\\hbox (badness 1057) in paragraph at lines 13--13\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 40--43\", \"Underfull \\\\hbox (badness 4556) in paragraph at lines 40--43\", \"Underfull \\\\hbox (badness 4291) in paragraph at lines 40--43\", \"Underfull \\\\hbox (badness 4765) in paragraph at lines 40--43\", \"Underfull \\\\hbox (badness 5036) in paragraph at lines 40--43\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 51--59\", \"Underfull \\\\hbox (badness 1796) in paragraph at lines 51--59\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 51--59\", \"Underfull \\\\hbox (badness 7613) in paragraph at lines 51--59\", \"Underfull \\\\hbox (badness 1122) in paragraph at lines 51--59\", \"Underfull \\\\hbox (badness 7944) in paragraph at lines 61--65\", \"Underfull \\\\hbox (badness 2452) in paragraph at lines 61--65\", \"Underfull \\\\hbox (badness 1484) in paragraph at lines 61--65\", \"Underfull \\\\hbox (badness 1533) in paragraph at lines 61--65\", \"Underfull \\\\hbox (badness 1762) in paragraph at lines 67--59\", \"Underfull \\\\hbox (badness 2351) in paragraph at lines 76--84\", \"Underfull \\\\hbox (badness 8189) in paragraph at lines 94--98\", \"Underfull \\\\hbox (badness 1178) in paragraph at lines 94--98\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 276--276\", \"Underfull \\\\hbox (badness 1400) in paragraph at lines 36--40\", \"Underfull \\\\hbox (badness 1571) in paragraph at lines 36--40\", \"Underfull \\\\hbox (badness 1067) in paragraph at lines 96--100\", \"Underfull \\\\vbox (badness 1412) has occurred while \\\\output is active []\", \"Overfull \\\\hbox (1.31956pt too wide) in paragraph at lines 142--153\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 217--220\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 217--220\", \"Underfull \\\\hbox (badness 3623) in paragraph at lines 217--220\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 217--220\"], \"issues\": [], \"summary\": \"PASS\"}"
    }
  },
  "sourceToolAssistantUUID": "602a6a99-fd43-423a-81fb-ccf1ec42bb4f",
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


### Runtime record

_source line 8114_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Director 指令] Reviewer visual review 发现 4 个排版问题：  **1. [必修] Page 11 feature ranking table 溢出** appendix.tex ~L26-35 (tab:top_features)，`\\texttt{}` feature 名过宽导致最右列侵入右栏。修复：`\\resizebox{\\columnwidth}{!}{…",
  "leafUuid": "c427453e-b726-4f6b-894a-46ac0f4cb73a",
  "sessionId": "952e4180-a1dd-4838-893f-04003731e881"
}
```

---


### Runtime record

_source line 8115_

```json
{
  "type": "ai-title",
  "aiTitle": "Report agent results to director",
  "sessionId": "952e4180-a1dd-4838-893f-04003731e881"
}
```

---


### Assistant

_source line 8116 · 2026-05-18T06:23:50.709Z_

<details><summary>Logged reasoning block</summary>

```text
Compilation passed. Let me check the results:

1. **0 overfull >10pt** — only 1.32pt remains (appendix_extended.tex L142-153)
2. **0 critical warnings**
3. **23 pages** (same)
4. **4 "`h' float specifier changed to `ht'"** warnings — these come from tables in appendix_extended.tex that use `[h]` which LaTeX auto-converts. Not a problem.
5. No hyperref "Token not allowed" warnings — the \texorpdfstring fixes worked


6. Now I'm visually inspecting pages 12 and 17 to see if the whitespace issues have improved.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c427453e-b726-4f6b-894a-46ac0f4cb73a",
  "isSidechain": false,
  "requestId": "req_011Cb9Z8Q23LRR9FSkhrpezo",
  "type": "assistant",
  "uuid": "4f4955cb-58ce-4bf4-b3ab-83c8085489e0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/paper_agent_e65ef40e",
  "sessionId": "952e4180-a1dd-4838-893f-04003731e881",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "frolicking-frolicking-dahl",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XfNTPt7NeFcHsFPU4Pf2jn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4184,
      "cache_read_input_tokens": 143028,
      "output_tokens": 340,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4184,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 340,
          "cache_read_input_tokens": 143028,
          "cache_creation_input_tokens": 4184,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4184
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


### Assistant

_source line 8117 · 2026-05-18T06:23:50.725Z_

Compilation passed with 0 overfull >10pt. Let me check the visual impact on pages 12 and 17.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4f4955cb-58ce-4bf4-b3ab-83c8085489e0",
  "isSidechain": false,
  "requestId": "req_011Cb9Z8Q23LRR9FSkhrpezo",
  "type": "assistant",
  "uuid": "71011f9f-e588-4ae8-8ef6-cbed07443303",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/paper_agent_e65ef40e",
  "sessionId": "952e4180-a1dd-4838-893f-04003731e881",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "frolicking-frolicking-dahl",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XfNTPt7NeFcHsFPU4Pf2jn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4184,
      "cache_read_input_tokens": 143028,
      "output_tokens": 340,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4184,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 340,
          "cache_read_input_tokens": 143028,
          "cache_creation_input_tokens": 4184,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4184
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


### Tool call

_source line 8118 · 2026-05-18T06:23:50.874Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images · `toolu_01DPTxN5tfQV4oW4LLebgA9Z`</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.pdf",
  "pages": "12",
  "dpi": 150
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "71011f9f-e588-4ae8-8ef6-cbed07443303",
  "isSidechain": false,
  "requestId": "req_011Cb9Z8Q23LRR9FSkhrpezo",
  "type": "assistant",
  "uuid": "746b858e-14e1-4f00-95c9-75b99e10082a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/paper_agent_e65ef40e",
  "sessionId": "952e4180-a1dd-4838-893f-04003731e881",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "frolicking-frolicking-dahl",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XfNTPt7NeFcHsFPU4Pf2jn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4184,
      "cache_read_input_tokens": 143028,
      "output_tokens": 340,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4184,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 340,
          "cache_read_input_tokens": 143028,
          "cache_creation_input_tokens": 4184,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4184
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

_source line 8119 · 2026-05-18T06:23:51.794Z_

<details><summary>↩ Tool result · `toolu_01DPTxN5tfQV4oW4LLebgA9Z`</summary>

```text
Error: result (219,445 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination--claude-sessions-paper-agent-e65ef40e/952e4180-a1dd-4838-893f-04003731e881/tool-results/mcp-agent-ml-research-pdf_to_images-1779085431790.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination--claude-sessions-paper-agent-e65ef40e/952e4180-a1dd-4838-893f-04003731e881/tool-results/mcp-agent-ml-research-pdf_to_images-1779085431790.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination--claude-sessions-paper-agent-e65ef40e/952e4180-a1dd-4838-893f-04003731e881/tool-results/mcp-agent-ml-research-pdf_to_images-1779085431790.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "746b858e-14e1-4f00-95c9-75b99e10082a",
  "isSidechain": false,
  "promptId": "8dba7b96-5a22-445a-882e-3856dafbad00",
  "type": "user",
  "uuid": "ed398025-c207-4b13-992d-374ae80bd105",
  "toolUseResult": "Error: result (219,445 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination--claude-sessions-paper-agent-e65ef40e/952e4180-a1dd-4838-893f-04003731e881/tool-results/mcp-agent-ml-research-pdf_to_images-1779085431790.txt.\nFormat: JSON with schema: {result: string}\n- For targeted queries (find a value, filter by field): use jq on the file directly.\n- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination--claude-sessions-paper-agent-e65ef40e/952e4180-a1dd-4838-893f-04003731e881/tool-results/mcp-agent-ml-research-pdf_to_images-1779085431790.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.\n- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. \"/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination--claude-sessions-paper-agent-e65ef40e/952e4180-a1dd-4838-893f-04003731e881/tool-results/mcp-agent-ml-research-pdf_to_images-1779085431790.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim.\" A vague \"summarize this\" may lose detail.\n",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"images\": [{\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/_pdf_images/main_p12.png\", \"base64\": \"iVBORw0KGgoAAAANSUhEUgAABNkAAAbaCAIAAAB3QTY3AAAACXBIWXMAABcSAAAXEgFnn9JSAAKBJUlEQVR4nOy9BXgVRxv2H4o7FGiBQilQirdIcVqKtEVbUiRAcQgQ3F9S5PpIcXeXIi9aNDjFNUiAF/dgwSVAsJSc7/7O82f+0z0nGzssnPT+Xbly7c7Ozs7OPrP73GfMw0YIIYQQQgghhFiLx7vOACGEEEIIIYSQfx3UooQQQgghhBBCrIZalBBCCCGEEEKI1VCLEkIIIYQQQgixGmpRQgghhBBCCCFWQy1KCCGEEEIIIcRqqEUJIYQQQgghhFgNtSghhBBCCCGEEKuhFiWEEEIIIYQQYjXUooQQQgghhBBCrIZalBBCCCGEEEKI1VCLEkIIIYQQQgixGmpRQgghhBBCCCFWQy1KCCGEEEIIIcRqqEUJIYQQQgghhFgNtSghhBBCCCGEEKuhFiWEEEIIIYQQYjXUooQQQgghhBBCrIZalBBCCCGEEEKI1VCLEkIIIYQQQgixGmpRQgghhBBCCCFWQy1KCCGEEEIIIcRqqEUJIYQQQgghhFgNtSghhBBCCCGEEKuhFiWEEEIIIYQQYjXUooQQQgghhBBCrIZalBBCCCGEEEKI1VCLEkIIIYQQQgixGmpRQgghhBBCCCFWQy1KCCGEEEIIIcRqqEUJIYQQQgghhFgNtSghhBBCCCGEEKuhFiWEEEIIIYQQYjXUooQQQgghhBBCrIZalBBCCCGEEEKI1VCLEkIIIYQQQgixGmpRQgghhBBCCCFWQy1KCCGEEEIIIcRqqEUJIYQQQgghhFgNtSghhBBCCCGEEKuhFiWEEEIIIYQQYjXUooQQQgghhBBCrIZalBBCCCGEEEKI1VCLEkIIIYQQQgixGmpRQgghhBBCCCFWQy1KCCGEEEIIIcRqqEUJIYQQQgghhFgNtSghhBBCCCGEEKuhFiWEEEIIIYQQYjXUooQQQgghhBBCrIZalBBCCCGEEEKI1VCLEkIIIYQQQgixGmpRQgghhBBCCCFWQy1KCCGEEEIIIcRqqEUJIYQQQgghhFgNtSghhBBCCCGEEKuhFiWEEEIIIYQQYjXUooQQQgghhBBCrIZalBBCCCGEEEKI1VCLEkIIIYQQQgixGmpRQgghhBBCCCFWQy1KCCGEEEIIIcRqqEUJIYQQQgghhFgNtSghhBBCCCGEEKuhFiWEEEIIIYQQYjXUooQQQgghhBBCrIZalBBCCCGEEEKI1VCLEkIIIYQQQgixGmpRQgghhBBCCCFWQy1KCCGEEEIIIcRqqEUJIYQQQgghhFgNtSghhBBCCCGEEKuhFiWEEEIIIYQQYjXUooQQQgghhBBCrIZalBBCCCGEEEKI1VCLEkIIIYQQQgixGmpRQgghhBBCCCFWQy1KCCGEEEIIIcRqqEUJIYQQQgghhFgNtSghhBBCCCGEEKuhFiWEEEIIIYQQYjXUooQQQgghhBBCrIZalBBCCCGEEEKI1VCLEkIIIYQQQgixGmpRQgghhBBCCCFWQy1KCCGEEEIIIcRqqEUJIYQQQgghhFgNtSghhBBCCCGEEKuhFiWEEEIIIYQQYjXUooQQQgghhBBCrIZalBBCCCGEEEKI1VCLEkIIIYQQQgixGmpRQgghhBBCCCFWQy1KCCGEEEIIIcRqqEUJIYQQQgghhFgNtSghhBBCCCGEEKuhFiWEEEIIIYQQYjXUooQQQgghhBBCrIZalBBCCCGEEEKI1VCLEkIIIYQQQgixGmpRQgghhBBCCCFWQy1KCCGEEEIIIcRqqEUJIYQQQgghhFgNtSghhBBCCCGEEKuhFiWEEEIIIYQQYjXUooQQQgghhBBCrIZalBBCCCGEEEKI1VCLEkIIIYQQQgixGmpRQgghhBBCCCFWQy1KCCGEEEIIIcRqqEUJIYQQQgghhFgNtSghhBBCCCGEEKuhFiWEEEIIIYQQYjXUooQQQgghhBBCrIZalBBCCCGEEEKI1VCLEkIIIYQQQgixGmpRQgghhBBCCCFWQy1KCCGEEEIIIcRqqEUJIYQQQgghhFgNtSghhBBCCCGEEKuhFiWEEEIIIYQQYjXUooQQQgghhBBCrIZalBBCCCGEEEKI1VCLEkIIIYQQQgixGmpRQgghhBBCCCFWQy1KCCGEEEIIIcRqqEUJIYQQQgghhFgNtSghhBBCCCGEEKuhFiWEEEIIIYQQYjXUooQQQgghhBBCrIZalBBCCCGEEEKI1VCLEkIIIYQQQgixGmpRQgghhBBCCCFWQy1KCCGEEEIIIcRqqEUJIYQQQgghhFgNtSghhBBCCCGEEKuhFiWEEEIIIYQQYjXUooQQQgghhBBCrIZalBBCCCGEEEKI1VCLEkIIIYQQQgixGmpRQggh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lKHV/fbbb8behiVMuii9Di1PPLazs2vevDltP3jw4E8J8b0chmEYhmESGnbR5I3aRamHh94bzXnLmTOn4pTatWtbxExM/R4XpW6x/H0Rdfy7d++6uLisW7cOvXPFkI4xFwVOTk64KfRrfXx8xACOMSgdmogLlYIK2traNmvWDLtdu3b19f3/2LsTcJvK/+/jx6xE6ocyJclUJBlKZIyokKJ+DZpE0YBSKvR/UMoYipJKThENCJGMKSQZMytC5szz1H4+//193M/6rb3PPudwzuL4vV9XV9de97732mvd697nuj/WWvf6zdWMnUUbNWqUM2fO2N/i3VqtWSX9+vWLvXle27dvV3J79T/ZVdbeJ6/ocNiAPur4++WXX3Zhb+zYsVbTjbmTyE6oep/kkWgWTUp3isyikidPHkVQe71z587GjRvbNuvoRE0soWhZ9OTJk+oSZcuWDYVPfce+m9GbRe1krCKit4KtzZ0LXbNmjfvnj27dun3wwQc1a9bUSo4dO6au+8477yT0RU899VS+fPnc4sGDB3PkyOFuoE0Ndo+x8pK30O7rjnpHq1167ZuIyE7g20+jTJkyvrlt1esiT4knUcpmUdGe2k3Il19+eYy5wRLNoqHwM2CVwO1098aNG/XanXjXxzN73HLLLcnecwAAcFrIomlbZBadNGmSBmHx8fGh8Khdr92soeamm27SiNlen0kWtWFx8+bNvSv31lcszJo1q3uwYdKz6Ndff623nn766Xbt2k2ZMiV2CygAKHxqCLtw4UIbQD/55JMaaGqoXaNGDW/N2FlUuSIu4tbNUDhOR91aBUuV3H777b76mzZtctPe+HTu3Llr166+QjsPrORz+PBhV2hnd9euXRu5kscff3zy5Mn2+tChQ1ZT8SnqNyakdevW+pT3psREs2goCd0pahbNkiWLHRcXrbXLNiORcnXUzYvMopbP7araEiVK5MyZ0zcB8vHjx11zebPokiVL9EHfLZFHjx6NC9/X6krUVbSdW7ZsUdzVmi3BKghVqVLF7lmNqmXLluXLl3eL6h7q8OoYCdVXBlZubJEENjV0JDtn7n2oTyjcJfQTiPo4zf3796dLl857dUAoPNOvVmKXAevHoubyvmunEH3/xpREKZtFrcOov7Vt21Z7obZN6FgkJYvq99WwYUMdX61NDaKUfho7CAAAUhZZNG2LzKK9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/vnnH62zZ8+evXv3/uGHH3wf/O23377++mu9WLVq1dtvv/3JJ5/Y/C5a4bffftu1a9fvvvvOW3/u3LmTJ0/Wfk2cOPH111/XZ48fP+7ejZpFt27d+tFHH3Xp0uWbb745efKkKz948ODw4cM3bdqkNYwaNerNN990l/CpcbQjffr0sYtgvRJqE22YNlgvfvzxxzfeeEOt4d4aP3581qxZM2fObC1vG3zkyJGhQ4e+9dZbOkCzZs1KqGETyqLugIoSqbZ//fr13gobNmzQRmpL9O3aUysMoD/s3HnIV9Klywxl0dmzNyT0kTVr1lgfMMeOHRs3btzixYvtuKgPzJ49O6HPduzYUe1z/fXXaxcmTZoU8iQcfVwl+riOsu9Tany1QOfOnePj42NMaaPeol22b9dh1b6rMa0LqWNotWpedWDvR9TCo0ePVs9UZ164cKH3rcjDtG7duiFDhoTC/U2dTQ3rjpSPKlx11VXaL22D9tSdD4+6IzNmzBhxivrP0qVL7bX2Re/u379f0V2reuCBB1To20jjsuiBAwf0Wrs5bdo0e2v37t1u5epLOlgq/OOPP6xEL6Juv/4mvPPOO/oLoP62ZMkSK0zKkUror4fq2zeqSbWovwluq6wnb9y40RZ37txpH9GvTN+YrMbXH4Tu3bvrUOqD3j8dAAAgSGTRNEyjwwsvvDB9+vS2qJHos88+6056KA5deeWVWlTqqFKlSrp06fLlyxcK3zN27733Khlq/Pfggw9myZJFo7qEvkKDvMqVK48dO1b5RwNcVf7+++/tLY28b7nlFg3mNBhVYYECBW699VaFQ721du3af//73/rq2rVrazB99913P/744xkyZKhbt662uUmTJk8++eTNN9+sCsOGDQuFR66lSpXSoqrVq1evfPnyuXLl0mLVqlXdIDIyi2qk3rx58+nTp2uYe+mll2of1QK243ny5FHlwYMH33XXXS1atChTpox2f86cOf369dPG6NuzZctWvHhxNwZNqE1Wrlx52223aVUPPfTQU0891ahRowoVKmjxlVdesQ8qWRUuXFj1vwrTyFtJ+7rrrtPHtXKNqjNlypRQ20bNoooiaoHQqctTc+bMqTrecbaORYkSJRTv58+ff8UVV2i/ihUrpm/U9wbQH3wee2x07tzdjx+PMpRXa1vT1axZ00oUKq6++mqV9OjR44477lAP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wQV58uQJhWfftXeLFSumAb026Y477tBirVq13Br0kSeeeOK5557Trk2fPj1Dhgyq4wb6L7zwgob+GmGrKfTBl156KRQOSNpT1bzuuut69+6trdVbyhi+RoixXxp/t2jRImPGjEr+9kWqU6RIEX1cqez222//97//XaBAgfTp02sNofCksp999pneveGGG7TyadOmqf3btm2rEsU21zIKHtokb751FCkVb1S/WrVqdnwtESnjVa5cWY2jo/Pdd9/lzZtX367kqbcU4K+88kp9RCH25ptvTpcu3VVXXRW170VtJYnR2WL3B8ui2uVKlSo9+OCDF154ofrhtm3bIr9aGUz9UMciR44cqt+gQYOWLVv+61//uuKKK5Q2mzdv/thjjzVs2FBr886g8/nnn6v9dbj1ER2gGjVquDuidUALFSqkZlEgVFvddNNN7l9wFPNUc+vWrXv27FGf1C6rULt24403ut+IOqSCohbvvffehLqKvjShRju93VGmbdy4sbKijmDp0qW1/StXrky0U0X+bH1t+9NPP5UqVUoV9L367VSoUEFbokX96rWbVidG/4n8I/DOO+9ky5ZNJYqa1atX1/bop6peYXPtJro9AADgPEYWTcN27NihMZyGpLaoFDFjxgx7rfSiobyrqWGoavbt29cWH330USUidxrNV1keeughbxbVyPiuu+6y1wps7ubD8ePH25DXfVCjcF8WVQIcMGCAvT5+/LjGoBra2qIGphp82+sNGzbogxqRuw/GvkZXQ3CXRU3RokUtixp9iwK2O1N6//33q/7q1attsWvXrvfcc4+rrNG/3lXYDoUTi9rHvaWNdE2h6KIxffbs2ZXxNC4fNmzYzp07Ixsh9n4pYLgsKu+++64qaPhu57XWrFmjRY3X7V27wtZ7ja7CpFaudOHOU6mkePHiUVspFJ6UWGt4+OGHXYmOYMWKFZs1a+ZKFi5cqDoKkLb48ssva1HhRyl36dKlEydOjFxtjFaK3dli9AfLoooutvjJJ59Y2k9o18qVK6cKY8aMcZtkuV2/CytRltbBsoZS5ilTpoxrtC5durj+o93UEVEfsLcsVU6dOtUWS5Ys2b9/f3ut/Ny5c2d7rYDt/Y0olbksGkqgq8RotOTujv0DxPr16+0ta3P3u4vdqSJ7rM8PP/ygCtdee62d0texUz5XibVDov0n8o+A3lLJ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2b9///z585944on06dOr5Jtvvkl0hceOHcufP7+toWrVqjFqnjcHFAAAAGTRNO/SSy91SeDvv/+2QoVSV/jkk0+mxvd+9tlnWnnu3Ll95Tt27MiXL985kkWlZMmSaT26TJ06NV26dImeYAzMnXfeeckll2zatMkWf/31V28WddXeeecdlYwePTop66xXr15SsmjovDigAAAACJFFzwN58uSJzKJr1651hZFxMUXcc889WnnBggUj3xo/fvy5k0WVjtJ0dFm3bp39c8O5k0Xr1q3bp08ft5hQFg2Fc+PXX3+dlHXefvvtScyiaf2AAgAAwJBF07yoWXTnzp2uMH369MeOHUvx7y1evLitf8iQIZHvXnnllWTRM7d27dpChQrZ9p87WfTWW2/1XjAcI4u2adPGrhtPFFkUAADgv03KZ9F9+/YtWrRo5syZP/zww4IFC/bs2RNZZ82aNRq/ektOnjz5559/zpkzZ/r06bNnz/79999PnDiR4tt2XoqaRRUVXGGVKlVS43vLli3rvuKRRx7566+/vO9u3LjR5tGdOHHi6x6HDx/WsfaWdOvWzT7y008/ecsVw37++ef77ruvZs2a7dq1mz9/vlu5PuKqffLJJ0eOHOnatauqqfKAAQN8wTuh6HL8+PEPP/zw8ccfr127dtu2bd36Dx486N0Mu8T0888/v+uuuxSTWrZsqV2zmvHx8XfccUedOnU6d+586NAhX/sktP7I7VfJhAkTGjdurF1o3br11q1brdqqVavsamfz2GOPqb7a061nyZIlzz//fIMGDapVq3b//ff37Nlz586d7l01oHdH9IvTb6pPnz61atV69NFHt23b5js0Mm7cOH1Qm22LPXr0iHro9VP1LsbIort37967d68OutbZtGnTGjVqqMVatWo1bdo03zq9WXTXrl0dO3asW7euDpka2VczoQO6ePHiTp06aT3//ve/33nnHV83OHr0qPZdB1HboMMxZsyYVLp2HQAAAEmUwln0wIEDM2bMmB7mXvji6ObNmzUSVbn3mR/Lli2zykqw9kKBNmW37XwVNYu2adPGSkqWLKlgnxrfq9QU55E5c2blNHcPoaOMqojl28J58+a506rp06e3mnrr6aefdjVfeeUVJbHbbrvtggsu0GKmTJkstsmPP/6YK1cuq1axYsV69erdfPPN1157rZVUqlRpx44d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AACcFWRRAAAAAEDQyKIAAAAAgKCRRQEAAAAAQSOLAgAAAACCRhYFAAAAAASNLAoAAAAACBpZFAAAAAAQNLIoAAAAACBoZFEAAAAAQNDIogAAAACAoJFFAQAAAABBI4sCAAAAAIJGFgUAAAAABI0sCgAAAAAIGlkUAAAAABA0sigAAAAAIGhkUQAAAABA0MiiAAAAAICgkUUBAAAAAEEjiwIAAAAAgkYWBQAAAAAEjSwKAAAAAAgaWRQAAAAAEDSyKAAAAAAgaGRRAAAAAEDQyKIAAAAAgKCRRQEAAAAAQSOLAgAAAACCRhYFAAAAAASNLAoAAAAACBpZFAAAAAAQNLIoAAAAACBoZFEAAAAAQNDIogAAAACAoJFFAQAAAABBI4sCAAAAAIJGFgUAAAAABI0sCgAAAAAIGlkUAAAAABA0sigAAAAAIGhkUQAAAABA0MiiAAAAAICgkUUBAAAAAEEjiwIAAAAAgkYWBQAAAAAEjSwKAAAAAAgaWRQAAAAAEDSyKAAAAAAgaGRRAAAAAEDQyKIAAAAAgKCRRQEAAAAAQSOLAgAAAACCRhYFAAAAAASNLAoAAAAACBpZFAAAAAAQNLIoAAAAACBoZFEAAAAAQNDIogAAAACAoJFFAQAAAABBI4sCAAAAAIJGFgUAAAAABI0sCgAAAAAIGlkUAAAAABA0sigAAAAAIGhkUQAAAABA0MiiAAAAAICgkUUBAAAAAEEjiwIAAAAAgkYWBQAAAAAEjSwKAAAAAAgaWRQAAAAAEDSyKAAAAAAgaGRRAAAAAEDQyKIAAAAAgKCRRQEAAAAAQSOLAgAAAACCRhYFAAAAAASNLAoAAAAACBpZFAAAAAAQNLIoAAAAACBoZFEAAAAAQNDIogAAAACAoJFFAQAAAABBI4sCAAAAAIJGFgUAAAAABI0sCgAAAAAIGlkUAAAAABA0sigAAAAAIGhkUQAAAABA0MiiAAAAAICgkUUBAAAAAEEjiwIAAAAAgkYWBQAAAAAEjSwKAAAAAAgaWRQAAAAAEDSyKAAAAAAgaGRRAAAAAEDQyKIAAAAAgKCRRQEAAAAAQSOLAgAAAACCRhYFAAAAAASNLAoAAAAACBpZFAAAAAAQNLIoAAAAACBoZFEAAAAAQNDIogAAAACAoJFFAQAAAABBI4sCAAAAAIJGFgUAAAAABI0sCgAAAAAIGlkUAAAAABA0sigAAAAAIGhkUQAAAABA0MiiAAAAAICgkUUBAAAAAEEjiwIAAAAAgkYWBQAAAAAEjSwKAAAAAAgaWRQAAAAAEDSyKAAAAAAgaGRRAAAAAEDQyKIAAAAAgKCRRQEAAAAAQSOLAgAAAACCRhYFAAAAAASNLAoAAAAACBpZFAAAAAAQNLIoAAAAACBoZFEAAAAAQNDIogAAAACAoJFFAQAAAABBI4sCAAAAAIJGFgUAAAAABI0sCgAAAAAIGlkUAAAAABA0sigAAAAAIGhkUQAAAABA0MiiAAAAAICgkUUBAAAAAEEjiwIAAAAAgkYWBQAAAAAEjSwKAAAAAAgaWRQAAAAAEDSyKAAAAAAgaGRRAAAAAEDQyKIAAAAAgKCRRQEAAAAAQSOLAgAAAACCRhYFAAAAAASNLAoAAAAACBpZFAAAAAAQNLIoAAAAACBoZFEAAAAAQNDIogAAAACAoJFFAQAAAABBI4sCAAAAAIJGFgUAAAAABI0sCgAAAAAIGlkUAAAAABA0sigAAAAAIGhkUQAAAABA0MiiAAAAAICgkUUBAAAAAEEjiwIAAAAAgkYWBQAAAAAEjSwKAAAAAAgaWRQAAAAAEDSyKAAAAAAgaGRRAAAAAEDQyKIAAAAAgKCRRQEAAAAAQSOLAgAAAACCRhYFAAAAAASNLAoAAAAACBpZFAAAAAAQNLIoAAAAACBoZFEAAAAAQNDIogAAAACAoJFFAQAAAABBI4sCAAAAAIJGFgUAAAAABI0sCgAAAAAIGlkUAAAAABA0sigAAAAAIGhkUQAAAABA0MiiAAAAAICgkUUBAAAAAEEjiwIAAAAAgkYWBQAAAAAEjSwKAAAAAAgaWRQAAAAAEDSyKAAAAAAgaGRRAAAAAEDQyKIAAAAAgKCRRQEAAAAAQSOLAgAAAACCRhYFAAAAAASNLAoAAAAACBpZFAAAAAAQNLIoAAAAACBoZFEAAAAAQNDIogAAAACAoJFFAQAAAABBI4sCAAAAAIJGFgUAAAAABI0sCgAAAAAIGlkUAAAAABA0sigAAAAAIGhkUQAAAABA0MiiAAAAAICgkUUBAAAAAEEjiwIAAAAAgkYWBQAAAAAEjSwKAAAAAAgaWRQAAAAAEDSyKAAAAAAgaGRRAAAAAEDQyKIAAAAAgKCRRQEAAAAAQSOLAgAAAACCRhYFAAAAAASNLAoAAAAACBpZFAAAAAAQNLIoAAAAACBoZFEAAAAAQNDIogAAAACAoJFFAQAAAABBI4sCAAAAAIJGFgUAAAAABI0sCgAAAAAIGlkUAAAAABA0sigAAAAAIGhkUQAAAABA0MiiAAAAAICgkUUBAADwf9u7Y5Ys9ziOwy3RFEmB0Frtbjk0GMfX0lRD2KIk7rq0NLTUUPQCBEfB5jICkbCGiHoBBRHkIJwH4hwOKt4ufTw3XNf23P/f8F0/0wNQ06IAAADUtCgAAAA1LQoAAEBNiwIAAFDTogAAANS0KAAAADUtCgAAQE2LAgAAUNOiAAAA1LQoAAAANS0KAABATYsCAABQ06IAAADUtCgAAAA1LQoAAEBNiwIAAFDTogAAANS0KAAAADUtCgAAQE2LAgAAUNOiAAAA1LQoAAAANS0KAABATYsCAABQ06IAAADUtCgAAAA1LQoAAEBNiwIAAFDTogAAANS0KAAAADUtCgAAQE2LAgAAUNOiAAAA1LQoAAAANS0KAABATYsCAABQ06IAAADUtCgAAAA1LQoAAEBNiwIAAFDTogAAANS0KAAAADUtCgAAQE2LAgAAUNOiAAAA1LQoAAAANS0KAABATYsCAABQ06IAAADUtCgAAAA1LQoAAEBNiwIAAFDTogAAANS0KAAAADUtCgAAQE2LAgAAUNOiAAAA1LQoAAAANS0KAABATYsCAABQ06IAAADUtCgAAAA1LQoAAEBNiwIAAFDTogAAANS0KAAAADUtCgAAQE2LAgAAUNOiAAAA1LQoAAAANS0KAABATYsCAABQ06IAAADUtCgAAAA1LQoAAEBNiwIAAFDTogAAANS0KAAAADUtCgAAQE2LAgAAUNOiAAAA1LQoAAAANS0KAABATYsCAABQ06IAAADUtCgAAAA1LQoAAEBNiwIAAFDTogAAANS0KAAAADUtCgAAQE2LAgAAUNOiAAAA1LQoAAAANS0KAABATYsCAABQ06IAAADUtCgAAAA1LQoAAEBNiwIAAFDTogAAANS0KAAAADUtCgAAQE2LAgAAUNOiAAAA1LQoAAAANS0KAABATYsCAABQ06IAAADUtCgAAAA1LQoAAEBNiwIAAFDTogAAANS0KAAAADUtCgAAQE2LAgAAUNOiAAAA1LQoAAAANS0KAABATYsCAABQ06IAAADUtCgAAAA1LQoAAEBNiwIAAFDTogAAANS0KAAAADUtCgAAQE2LAgAAUNOiAAAA1LQoAAAANS0KAABATYsCAABQ06IAAADUtCgAAAA1LQoAAEBNiwIAAFDTogAAANS0KAAAADUtCgAAQE2LAgAAUNOiAAAA1LQoAAAANS0KAABATYsCAABQ06IAAADUtCgAAAA1LQoAAEBNiwIAAFDTogAAANS0KAAAADUtCgAAQE2LAgAAUNOiAAAA1LQoAAAANS0KAABATYsCAABQ06IAAADUtCgAAAA1LQoAAEBNiwIAAFDTogAAANS0KAAAADUtCgAAQE2LAgAAUNOiAAAA1LQoAAAANS0KAABATYsCAABQ06IAAADUtCgAAAA1LQoAAEBNiwIAAFDTogAAANS0KAAAADUtCgAAQE2LAgAAUNOiAAAA1LQoAAAANS0KAABATYsCAABQ06IAAADUtCgAAAA1LQoAAEBNiwIAAFDTogAAANS0KAAAADUtCgAAQE2LAgAAUNOiAAAA1LQoAAAANS0KAABATYsCAABQ06IAAADUtCgAAAA1LQoAAEBNiwIAAFDTogAAANS0KAAAADUtCgAAQE2LAgAAUNOiAAAA1LQoAAAANS0KAABATYsCAABQ06IAAADUtCgAAAA1LQoAAEBNiwIAAFDTogAAANS0KAAAADUtCgAAQE2LAgAAUNOiAAAA1LQoAAAANS0KAABATYsCAABQ06IAAADUtCgAAAA1LQoAAEBNiwIAAFDTogAAANS0KAAAADUtCgAAQE2LAgAAUNOiAAAA1LQoAAAANS0KAABATYsCAABQ06IAAADUtCgAAAA1LQoAAEBNiwIAAFDTogAAANS0KAAAADUtCgAAQE2LAgAAUNOiAAAA1LQoAAAANS0KAABATYsCAABQ06IAAADUtCgAAAA1LQoAAEBNiwIAAFDTogAAANS0KAAAADUtCgAAQE2LAgAAUNOiAAAA1LQoAAAANS0KAABATYsCAABQ06IAAADUtCgAAAA1LQoAAEBNiwIAAFDTogAAANS0KAAAADUtCgAAQE2LAgAAUNOiAAAA1LQoAAAANS0KAABATYsCAABQ06IAAADUtCgAAAA1LQoAAEBNiwIAAFDTogAAANS0KAAAADUtCgAAQE2LAgAAUNOiAAAA1LQoAAAANS0KAABATYsCAABQ06IAAADUtCgAAAA1LQoAAEBNiwIAAFDTogAAANS0KAAAADUtCgAAQE2LAgAAUNOiAAAA1LQoAAAANS0KAABATYsCAABQ06IAAADUtCgAAAA1LQoAAEBNiwIAAFDTogAAANS0KAAAADUtCgAAQE2LAgAAUNOiAAAA1LQoAAAANS0KAABATYsCAABQ06IAAADUtCgAAAA1LQoAAEBNiwIAAFDTogAAANS0KAAAADUtCgAAQE2LAgAAUNOiAAAA1LQoAAAANS0KAABATYsCAABQ06IAAADUtCgAAAA1LQoAAEBNiwIAAFDTogAAANS0KAAAADUtCgAAQE2LAgAAUNOiAAAA1LQoAAAANS0KAABATYsCAABQ06IAAADUtCgAAAA1LQoAAEBNiwIAAFDTogAAANS0KAAAADUtCgAAQE2LAgAAUNOiAAAA1LQoAAAANS0KAABATYsCAABQ06IAAADUtCgAAAA1LQoAAEBNiwIAAFDTogBwKr9+/drb2zv26eDgYHd3d319/f379/EqABgpLQoAA/b39x8/fnz16tWFhYWjr69fv75x48a5f8zOzn748KEfCQDjokUB4CSbm5uLi4vXrl2bdObRFt3Z2Zmenl5ZWXnx4sXS0tLU1NTk7Pr16z9//jyTtQAwFloUAIY9evTo2Badn59/9+7dvz+/fv36O0efPXvWDgSAkdGiADDsyZMnR1v0y5cv9+/fP3S5uLg4ubx37164DgDGR4sCwLBjW/THjx/fvn07dPn8+fPJ5cOHD8N1ADA+WhQAhh3bosdaW1ubXG5tbf35UQAwYloUAIadvkXn5uZmZmaCSQAwaloUAIadskV3dnbOnz//9u3bZhUAjJcWBYBhp2zRW7duPX36tJkEAKOmRQFg2GladHl5eWVlJZsEAKOmRQFg2GCLvnz58sGDB+UkABg1LQoAw05u0Y2NjaN/KPr9+/c/vwsAxkqLAsCwE1r01atXd+7cOfTx8+fPq6uryTQAGCUtCgDDlpeXJy169+7dQ9/fvHlz8eLFubm5v/7j5s2bFy5c+Pjx45lMBYBR0KIAcJLt7e3V1dVLly5NWvTKlStra2tbW1u/nz59+nT58uVzx7l9+/aZrgaA/zstCgAAQE2LAgAAUNOiAAAA1LQoAAAANS0KAABATYsCAABQ06IAAADUtCgAAAA1LQoAAEBNiwIAAFDTogAAANS0KAAAADUtCgAAQE2LAgAAUNOiAAAA1LQoAAAANS0KAABATYsCAABQ06IAAADUtCgAAAA1LQoAAEBNiwIAAFDTogAAANS0KAAAADUtCgAAQE2LAgAAUNOiAAAA1LQoAAAANS0KAABATYsCAABQ06IAAADUtCgAAAA1LQoAAEBNiwIAAFDTogAAANS0KAAAADUtCgAAQE2LAgAAUNOiAAAA1LQoAAAANS0KAABATYsCAABQ06IAAADUtCgAAAA1LQoAAEBNiwIAAFDTogAAANS0KAAAADUtCgAAQE2LAgAAUNOiAAAA1LQoAAAANS0KAABATYsCAABQ06IAAADUtCgAAAA1LQoAAEBNiwIAAFDTogAAANS0KAAAADUtCgAAQE2LAgAAUNOiAAAA1LQoAAAANS0KAABATYsCAABQ06IAAADUtCgAAAA1LQoAAEBNiwIAAFDTogAAANS0KAAAADUtCgAAQE2LAgAAUNOiAAAA1LQoAAAANS0KAABATYsCAABQ06IAAADUtCgAAAA1LQoAAEBNiwIAAFD7G3NJ0sia12beAAAAAElFTkSuQmCC\", \"width\": 1241, \"height\": 1754, \"size_kb\": 160.4}], \"total_pages\": 23, \"rendered_pages\": 1, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/_pdf_images\"}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "746b858e-14e1-4f00-95c9-75b99e10082a",
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


### Runtime record

_source line 8120_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Director 指令] Reviewer visual review 发现 4 个排版问题：  **1. [必修] Page 11 feature ranking table 溢出** appendix.tex ~L26-35 (tab:top_features)，`\\texttt{}` feature 名过宽导致最右列侵入右栏。修复：`\\resizebox{\\columnwidth}{!}{…",
  "leafUuid": "ed398025-c207-4b13-992d-374ae80bd105",
  "sessionId": "952e4180-a1dd-4838-893f-04003731e881"
}
```

---


### Runtime record

_source line 8121_

```json
{
  "type": "ai-title",
  "aiTitle": "Report agent results to director",
  "sessionId": "952e4180-a1dd-4838-893f-04003731e881"
}
```

---


### Tool call

_source line 8122 · 2026-05-18T06:23:55.447Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Kzfqq3gFKCDkPrxKagxcsE`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/_pdf_images/main_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ed398025-c207-4b13-992d-374ae80bd105",
  "isSidechain": false,
  "requestId": "req_011Cb9Z9NntydrHVUAQG7ysV",
  "type": "assistant",
  "uuid": "873ec939-d277-4370-9563-452abf02941e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/paper_agent_e65ef40e",
  "sessionId": "952e4180-a1dd-4838-893f-04003731e881",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "frolicking-frolicking-dahl",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y7xqkGXnpEG2yGiLGsE7pe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 884,
      "cache_read_input_tokens": 147212,
      "output_tokens": 95,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 884,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 95,
          "cache_read_input_tokens": 147212,
          "cache_creation_input_tokens": 884,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 884
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

_source line 8123 · 2026-05-18T06:23:55.836Z_

<details><summary>↩ Tool result · `toolu_01Kzfqq3gFKCDkPrxKagxcsE`</summary>

````text
```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "data": "[ATTACHMENT_DATA_REDACTED]",
    "media_type": "image/png"
  }
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "873ec939-d277-4370-9563-452abf02941e",
  "isSidechain": false,
  "promptId": "8dba7b96-5a22-445a-882e-3856dafbad00",
  "type": "user",
  "uuid": "178302e9-7b7c-4d9d-8b79-ab9dba3a0353",
  "toolUseResult": {
    "type": "image",
    "file": {
      "base64": "[ATTACHMENT_DATA_REDACTED]",
      "type": "image/png",
      "originalSize": 164211
    }
  },
  "sourceToolAssistantUUID": "873ec939-d277-4370-9563-452abf02941e",
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


### Runtime record

_source line 8124 · 2026-05-18T06:23:55.841Z_

```json
{
  "parentUuid": "178302e9-7b7c-4d9d-8b79-ab9dba3a0353",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "1b6e2927-a1bd-448a-a424-87c9ba394a00",
  "timestamp": "2026-05-18T06:23:55.841Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/paper_agent_e65ef40e",
  "sessionId": "952e4180-a1dd-4838-893f-04003731e881",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "frolicking-frolicking-dahl"
}
```

---


### Runtime record

_source line 8125_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Director 指令] Reviewer visual review 发现 4 个排版问题：  **1. [必修] Page 11 feature ranking table 溢出** appendix.tex ~L26-35 (tab:top_features)，`\\texttt{}` feature 名过宽导致最右列侵入右栏。修复：`\\resizebox{\\columnwidth}{!}{…",
  "leafUuid": "1b6e2927-a1bd-448a-a424-87c9ba394a00",
  "sessionId": "952e4180-a1dd-4838-893f-04003731e881"
}
```

---


### Runtime record

_source line 8126_

```json
{
  "type": "ai-title",
  "aiTitle": "Report agent results to director",
  "sessionId": "952e4180-a1dd-4838-893f-04003731e881"
}
```

---


### Assistant

_source line 8127 · 2026-05-18T06:24:01.401Z_

<details><summary>Logged reasoning block</summary>

```text
Page 12 now shows the figures and "B Supplementary Tables" header at the bottom. The per-depth recall table (Table 9) has moved. Let me check where it ended up. The whitespace at the bottom of page 12 is much less now — it's just the section header "B Supplementary Tables" with some space below.

Let me check pages 13 and 17 to see the overall layout.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1b6e2927-a1bd-448a-a424-87c9ba394a00",
  "isSidechain": false,
  "requestId": "req_011Cb9Z9fzkXZer1Gomgi44Y",
  "type": "assistant",
  "uuid": "1cea02ba-f0bf-4e0c-afd9-6afd36e60e41",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/paper_agent_e65ef40e",
  "sessionId": "952e4180-a1dd-4838-893f-04003731e881",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "frolicking-frolicking-dahl",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QWQL3BnfGGVRTMystqDQPy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 419,
      "cache_read_input_tokens": 148096,
      "output_tokens": 205,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 419,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 205,
          "cache_read_input_tokens": 148096,
          "cache_creation_input_tokens": 419,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 419
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


### Tool call

_source line 8128 · 2026-05-18T06:24:01.968Z_

<details open><summary>🔧 Tool call — Read · `toolu_01RsFeWAEcDkuiJBfMopSRM6`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/_pdf_images/main_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1cea02ba-f0bf-4e0c-afd9-6afd36e60e41",
  "isSidechain": false,
  "requestId": "req_011Cb9Z9fzkXZer1Gomgi44Y",
  "type": "assistant",
  "uuid": "46685f34-7dc9-4745-83dd-9050909c7042",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/paper_agent_e65ef40e",
  "sessionId": "952e4180-a1dd-4838-893f-04003731e881",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "frolicking-frolicking-dahl",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QWQL3BnfGGVRTMystqDQPy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 419,
      "cache_read_input_tokens": 148096,
      "output_tokens": 205,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 419,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 205,
          "cache_read_input_tokens": 148096,
          "cache_creation_input_tokens": 419,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 419
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

_source line 8129 · 2026-05-18T06:24:02.566Z_

<details><summary>↩ Tool result · `toolu_01RsFeWAEcDkuiJBfMopSRM6`</summary>

````text
```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "data": "[ATTACHMENT_DATA_REDACTED]",
    "media_type": "image/jpeg"
  }
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "46685f34-7dc9-4745-83dd-9050909c7042",
  "isSidechain": false,
  "promptId": "8dba7b96-5a22-445a-882e-3856dafbad00",
  "type": "user",
  "uuid": "a7288a0a-f70f-4f26-a739-58873544a237",
  "toolUseResult": {
    "type": "image",
    "file": {
      "base64": "[ATTACHMENT_DATA_REDACTED]",
      "type": "image/jpeg",
      "originalSize": 527683
    }
  },
  "sourceToolAssistantUUID": "46685f34-7dc9-4745-83dd-9050909c7042",
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


### Runtime record

_source line 8130_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Director 指令] Reviewer visual review 发现 4 个排版问题：  **1. [必修] Page 11 feature ranking table 溢出** appendix.tex ~L26-35 (tab:top_features)，`\\texttt{}` feature 名过宽导致最右列侵入右栏。修复：`\\resizebox{\\columnwidth}{!}{…",
  "leafUuid": "a7288a0a-f70f-4f26-a739-58873544a237",
  "sessionId": "952e4180-a1dd-4838-893f-04003731e881"
}
```

---


### Runtime record

_source line 8131_

```json
{
  "type": "ai-title",
  "aiTitle": "Report agent results to director",
  "sessionId": "952e4180-a1dd-4838-893f-04003731e881"
}
```

---


### Assistant

_source line 8132 · 2026-05-18T06:24:12.491Z_

<details><summary>Logged reasoning block</summary>

```text
Hmm, page 13 now shows "C Supplementary Details" (with Table 10 - dataset stats) in the right column, and "D Extended Discussion" in the left column starting with D.1 and D.2. 

Wait — I removed D.1-D.6 in my edit, but the PDF still shows them? Let me check... Actually, looking more carefully at the PDF image:

Left column shows:
- "D Extended Discussion"
- "D.1 Theoretical Implications of K*=2" with substantial text (more than the 2 sentences I thought were there)


- Right column shows "C Supplementary Details" with Table 10

This is strange — the D.1-D.6 sections are still appearing even though I edited them out, so either my changes didn't apply or the compilation is pulling from cached files. Let me double-check the appendix_extended.tex file to see if my edits actually went through.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a7288a0a-f70f-4f26-a739-58873544a237",
  "isSidechain": false,
  "requestId": "req_011Cb9ZAAorKxLhC8YLX5YDq",
  "type": "assistant",
  "uuid": "69df46bd-9d3d-4f2a-980f-f1febc45e268",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/paper_agent_e65ef40e",
  "sessionId": "952e4180-a1dd-4838-893f-04003731e881",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "frolicking-frolicking-dahl",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R4exvYFLT65EcDwVFrYXma",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 585,
      "cache_read_input_tokens": 148515,
      "output_tokens": 394,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 585,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 394,
          "cache_read_input_tokens": 148515,
          "cache_creation_input_tokens": 585,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 585
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


### Assistant

_source line 8133 · 2026-05-18T06:24:12.493Z_

The D.1-D.6 content still appears on page 13. Let me verify my edit applied correctly.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "69df46bd-9d3d-4f2a-980f-f1febc45e268",
  "isSidechain": false,
  "requestId": "req_011Cb9ZAAorKxLhC8YLX5YDq",
  "type": "assistant",
  "uuid": "f2578c06-68ae-4b1c-9c61-c2485add6a91",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/paper_agent_e65ef40e",
  "sessionId": "952e4180-a1dd-4838-893f-04003731e881",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "frolicking-frolicking-dahl",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R4exvYFLT65EcDwVFrYXma",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 585,
      "cache_read_input_tokens": 148515,
      "output_tokens": 394,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 585,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 394,
          "cache_read_input_tokens": 148515,
          "cache_creation_input_tokens": 585,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 585
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


### Tool call

_source line 8134 · 2026-05-18T06:24:12.626Z_

<details open><summary>🔧 Tool call — Read · `toolu_01VRAN7cDsB4rG92a5RNxLHE`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex",
  "offset": 1,
  "limit": 20
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f2578c06-68ae-4b1c-9c61-c2485add6a91",
  "isSidechain": false,
  "requestId": "req_011Cb9ZAAorKxLhC8YLX5YDq",
  "type": "assistant",
  "uuid": "40562bf8-0cf4-4a09-b9fd-5e366466b7ea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/paper_agent_e65ef40e",
  "sessionId": "952e4180-a1dd-4838-893f-04003731e881",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "frolicking-frolicking-dahl",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R4exvYFLT65EcDwVFrYXma",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 585,
      "cache_read_input_tokens": 148515,
      "output_tokens": 394,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 585,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 394,
          "cache_read_input_tokens": 148515,
          "cache_creation_input_tokens": 585,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 585
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

_source line 8135 · 2026-05-18T06:24:12.635Z_

<details><summary>↩ Tool result · `toolu_01VRAN7cDsB4rG92a5RNxLHE`</summary>

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
16	\caption{Three-way ANOVA (Generator $\times$ Scorer $\times$ Depth-Pair) on per-fold pairwise $\auc$ values (Type~II SS). DV = per-fold AUC; $N{=}300$ (12 cells $\times$ 5 folds $\times$ 5 depth-pairs; 3 generators $\times$ 4 scorers). Scorer is statistically significant ($p < .001$) but has a small effect size ($\eta^2_p = 0.19$) relative to Depth-Pair ($\eta^2_p = 1.00$) and Generator ($\eta^2_p = 0.89$), indicating that scorer choice has a detectable but practically minor influence on depth discrimination.}
17	\label{tab:anova_crossscorer}
18	\begin{tabular}{lrrrr}
19	\toprule
20	\textbf{Source} & \textbf{df} & $F$ & $p$ & $\eta^2_p$ \\
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "40562bf8-0cf4-4a09-b9fd-5e366466b7ea",
  "isSidechain": false,
  "promptId": "8dba7b96-5a22-445a-882e-3856dafbad00",
  "type": "user",
  "uuid": "0ed0453b-401b-4eda-a84e-c3c77934cd55",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex",
      "content": "\\section{Extended Analysis and Limitations}\n\\label{sec:extended_discussion}\n\nThis section provides supporting tables for cross-scorer validation (Tables~\\ref{tab:crossscorer}--\\ref{tab:anova_crossscorer}), followed by extended limitations, ablation studies, and domain-specific analyses.\n\n\\noindent\\begin{minipage}{\\columnwidth}\n\\centering\n\\captionof{table}{Cross-scorer validation on Qwen-generated text. Alternative scorers (Pythia-1.4B, OLMo-1B) preserve feature ranking ($\\rho > 0.90$) and rewrite-mode $\\Kempirical = 2$, but reduce continuation-mode $\\Kempirical$ from 2 to 1.}\n\\label{tab:crossscorer}\n\\resizebox{\\columnwidth}{!}{\\input{tables/tab_crossscorer}}\n\\end{minipage}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Three-way ANOVA (Generator $\\times$ Scorer $\\times$ Depth-Pair) on per-fold pairwise $\\auc$ values (Type~II SS). DV = per-fold AUC; $N{=}300$ (12 cells $\\times$ 5 folds $\\times$ 5 depth-pairs; 3 generators $\\times$ 4 scorers). Scorer is statistically significant ($p < .001$) but has a small effect size ($\\eta^2_p = 0.19$) relative to Depth-Pair ($\\eta^2_p = 1.00$) and Generator ($\\eta^2_p = 0.89$), indicating that scorer choice has a detectable but practically minor influence on depth discrimination.}\n\\label{tab:anova_crossscorer}\n\\begin{tabular}{lrrrr}\n\\toprule\n\\textbf{Source} & \\textbf{df} & $F$ & $p$ & $\\eta^2_p$ \\\\",
      "numLines": 20,
      "startLine": 1,
      "totalLines": 241
    }
  },
  "sourceToolAssistantUUID": "40562bf8-0cf4-4a09-b9fd-5e366466b7ea",
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

_source line 8136 · 2026-05-18T06:24:19.158Z_

<details><summary>Logged reasoning block</summary>

```text
My edit applied correctly — the file now starts with "Extended Analysis and Limitations" and the intro paragraph, followed directly by the crossscorer and ANOVA tables. D.1-D.6 are gone.

But the PDF page 13 still shows "D.1 Theoretical Implications..." — this must be from the OLD cached images. The pdf_to_images command generated new images but only for the pages I requested (12), and the page 13 image I viewed was from the OLD generation (before my edits).

Let me regenerate page 13 specifically to verify.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0ed0453b-401b-4eda-a84e-c3c77934cd55",
  "isSidechain": false,
  "requestId": "req_011Cb9ZAuoysQo9qFV8knSJg",
  "type": "assistant",
  "uuid": "65bb5980-9622-471d-b31d-3bd75c4deacb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/paper_agent_e65ef40e",
  "sessionId": "952e4180-a1dd-4838-893f-04003731e881",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "frolicking-frolicking-dahl",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NeFoJfvhUonxXjE4Hr2fsT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 940,
      "cache_read_input_tokens": 149100,
      "output_tokens": 304,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 940,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 304,
          "cache_read_input_tokens": 149100,
          "cache_creation_input_tokens": 940,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 940
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


### Assistant

_source line 8137 · 2026-05-18T06:24:19.296Z_

The old page 13 image was cached. Let me regenerate to check the actual new layout.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "65bb5980-9622-471d-b31d-3bd75c4deacb",
  "isSidechain": false,
  "requestId": "req_011Cb9ZAuoysQo9qFV8knSJg",
  "type": "assistant",
  "uuid": "f222abc7-ebba-41cb-978d-008fc4e0ec26",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/paper_agent_e65ef40e",
  "sessionId": "952e4180-a1dd-4838-893f-04003731e881",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "frolicking-frolicking-dahl",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NeFoJfvhUonxXjE4Hr2fsT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 940,
      "cache_read_input_tokens": 149100,
      "output_tokens": 304,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 940,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 304,
          "cache_read_input_tokens": 149100,
          "cache_creation_input_tokens": 940,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 940
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


### Tool call

_source line 8138 · 2026-05-18T06:24:20.166Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images · `toolu_01LnyVrwtBWYvuzPBNs63MDR`</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.pdf",
  "pages": "12-13",
  "dpi": 150
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f222abc7-ebba-41cb-978d-008fc4e0ec26",
  "isSidechain": false,
  "requestId": "req_011Cb9ZAuoysQo9qFV8knSJg",
  "type": "assistant",
  "uuid": "2b7c254f-5723-4851-87bf-a80c8bc4b1ef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/paper_agent_e65ef40e",
  "sessionId": "952e4180-a1dd-4838-893f-04003731e881",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "frolicking-frolicking-dahl",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NeFoJfvhUonxXjE4Hr2fsT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 940,
      "cache_read_input_tokens": 149100,
      "output_tokens": 304,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 940,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 304,
          "cache_read_input_tokens": 149100,
          "cache_creation_input_tokens": 940,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 940
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
