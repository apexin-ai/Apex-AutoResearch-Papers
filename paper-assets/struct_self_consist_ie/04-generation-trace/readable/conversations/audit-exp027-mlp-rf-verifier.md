# audit exp027 mlp rf verifier

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 31
- **Recorded user turns:** 0
- **Tool calls:** 15
- **Original source:** `logs/chats/worker_audit_exp027-mlp-rf-verifier_20260519T220906.jsonl`
- **Structured JSON:** [`96e15e9088b89aa81366.json`](../../sessions/96/96e15e9088b89aa81366.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

31 recorded events

### Tool call

_source line 1 · 2026-05-19T22:10:41.476589+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex",
  "offset": "160",
  "limit": "40"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_exp027-mlp-rf-verifier_20260519T220906",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex",
    "offset": "160",
    "limit": "40"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-19T22:10:41.476933+00:00_

160	CoNLL & SJ & .436 & .422 & $-$.014 \\
161	      & FK & .400 & .418 & $+$.018 \\
162	SciERC & SJ & .360 & .422 & $+$.062 \\
163	       & FK & .267 & .326 & $+$.059 \\
164	\bottomrule
165	\end{tabular}
166	\end{table}
167	
168	\paragraph{Scale robustness.}
169	With Qwen3-4B (Table~\ref{tab:scale_ablation}), QE is comparable (mean $|\Delta\rho|{=}0.042$), yet selection remains below greedy despite 13.0~pp headroom. Task difficulty is a stronger predictor than model scale within the 3B--8B range (Appendix~\ref{app:llama3b}).
170	Degeneracy scales with capability: 8B shows 17.8\% vs.\ 4B's 10.4\% on SciERC (Table~\ref{tab:degeneracy}).
171	
172	\paragraph{LoRA-rank ablation.}
173	LoRA rank${=}8$ (vs.\ 32) lowers degeneracy to 7.2\% but LP remains below greedy ($\rho(\text{LP}, \text{F1}){\approx}0.24$); temperature manipulation ($T{=}1.2$; \S\ref{sec:discussion}) confirms that low degeneracy and adequate alignment are independently necessary.
174	
175	\paragraph{Supervised signal combination and hidden probes.}
176	Supervised classifiers (LR, MLP, RF; 5-fold CV, $N{=}16$) and a DeBERTa-v3-base verifier all fail to close the selection gap (Appendix~\ref{app:supervised_combination}).
177	Hidden state probes improve correlation ($+37$\% on SciERC) but not selection (gap closure $-5.1$\%; Appendix~\ref{app:hidden_probe}); the bottleneck extends to model-internal representations.
178	
179	%% ============================================================
180	\subsection{Scaling Behavior}
181	\label{sec:scaling}
182	
183	We evaluate Qwen2.5-72B-Instruct in a zero-shot setting to test whether the gap persists at larger scale without fine-tuning.
184	
185	\begin{table}[t]
186	\centering
187	\small
188	\caption{Fine-tuned 8B vs.\ zero-shot 72B ($N{=}8$, $T{=}1.0$). Hdr.\ = oracle $-$ greedy (pp). Degen.: instance degeneracy (\%).}
189	\label{tab:scale_comparison}
190	\resizebox{\columnwidth}{!}{%
191	\begin{tabular}{@{}llccccccc@{}}
192	\toprule
193	Dataset & Regime & Greedy & H
…[truncated 347 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_exp027-mlp-rf-verifier_20260519T220906",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-19T22:10:41.477159+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_exp027-mlp-rf-verifier_20260519T220906",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-19T22:10:41.477324+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_exp027-mlp-rf-verifier_20260519T220906",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-19T22:10:41.477489+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "supervised_combination",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_exp027-mlp-rf-verifier_20260519T220906",
  "tool": "Grep",
  "tool_args": {
    "pattern": "supervised_combination",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper",
    "output_mode": "files_with_matches"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-19T22:10:41.477618+00:00_

Found 3 files
docs/paper/main.aux
docs/paper/sections/appendix.tex
docs/paper/sections/experiments.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_exp027-mlp-rf-verifier_20260519T220906",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-19T22:10:41.477743+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "find /root/autodl-tmp/struct_self_consist_ie/ -path \"*verifier*\" -o -path \"*mlp*\" -o -path \"*random_forest*\" -o -path \"*rf_*\" -o -path \"*supervised*\" | grep -v __pycache__",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_exp027-mlp-rf-verifier_20260519T220906",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "find /root/autodl-tmp/struct_self_consist_ie/ -path \"*verifier*\" -o -path \"*mlp*\" -o -path \"*random_forest*\" -o -path \"*rf_*\" -o -path \"*supervised*\" | grep -v __pycache__",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-19T22:10:41.477882+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_exp027-mlp-rf-verifier_20260519T220906",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-19T22:10:41.478009+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "supervised_combination",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "output_mode": "content",
  "-n": "True",
  "-C": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_exp027-mlp-rf-verifier_20260519T220906",
  "tool": "Grep",
  "tool_args": {
    "pattern": "supervised_combination",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "output_mode": "content",
    "-n": "True",
    "-C": "3"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-19T22:10:41.478162+00:00_

430-(c)~Ensemble or mixture-of-experts settings generate structurally diverse candidates by design, reducing instance degeneracy below the levels observed in our single-model sampling.
431-(d)~Tasks where the model exhibits systematic overconfidence (e.g., hallucination-prone generation) may benefit from consensus filtering, as disagreement among samples would carry more discriminative signal than in our well-calibrated fine-tuned regime.
432-
433:\section{Supervised and Model-Internal Signal Analysis}\label{app:supervised_combination}
434-
435-\subsection{Supervised Signal Combination}
436-

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_exp027-mlp-rf-verifier_20260519T220906",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-19T22:10:41.478311+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "find /root/autodl-tmp/struct_self_consist_ie/ -path \"*verifier*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_exp027-mlp-rf-verifier_20260519T220906",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "find /root/autodl-tmp/struct_self_consist_ie/ -path \"*verifier*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-19T22:10:41.478439+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "find /root/autodl-tmp/struct_self_consist_ie/ -path \"*supervised*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_exp027-mlp-rf-verifier_20260519T220906",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "find /root/autodl-tmp/struct_self_consist_ie/ -path \"*supervised*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-19T22:10:41.478613+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_019_trained_verifier\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_019_trained_verifier/train_verifier.py\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_019_trained_verifier/results.json\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_019_trained_verifier/feature_importance.json\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_019_trained_verifier/report.md\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_027_mlp_verifier\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_027_mlp_verifier/train_mlp_verifier.py\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_027_mlp_verifier/results.json\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_027_mlp_verifier/report.md\\n/root/autodl-tmp/struct_self_consist_ie/output/r17_analyses/mlp_verifier_comparison.json\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_027v2_mlp_verifier\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_027v2_mlp_verifier/train_mlp_verifier_v2.py\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_027v2_mlp_verifier/run.log\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_027v2_mlp_verifier/results.json\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_027v2_mlp_verifier/report.md\\n/root/autodl-tmp/struct_self_consist_ie/output/deberta_verifier\\n/root/autodl-tmp/struct_self_consist_ie/output/deberta_verifier/scierc_train.log\\n/root/autodl-tmp/struct_self_consist_ie/output/deberta_verifier/fewnerd_train.log\\n/root/autodl-tmp/struct_self_consist_ie/output/deberta_verifier/scierc_model.pt\\n/root/autodl-tmp/struct_self_consist_ie/output/deberta_verifier/scierc_model_results.json\\n/root/autodl-tmp/struct_self_consist_ie/output/deberta_verifier/fewnerd_model.pt\\n/root/autodl-tmp/struct_self_consist_ie/output/deberta_verifier/fewnerd_model_results.json\\n/root/autodl-tmp/struct_self_consist_ie/output/deberta_verifier_5fold\\n/root/autodl-tmp/struc
…[truncated 3990 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_exp027-mlp-rf-verifier_20260519T220906",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-19T22:10:41.478776+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/struct_self_consist_ie/output/supervised_verifier_upgrade.log\\n/root/autodl-tmp/struct_self_consist_ie/output/supervised_verifier_upgrade\\n/root/autodl-tmp/struct_self_consist_ie/output/supervised_verifier_upgrade/results.json\\n/root/autodl-tmp/struct_self_consist_ie/code/supervised_verifier_upgrade.py\\n/root/autodl-tmp/struct_self_consist_ie/train_supervised_verifier.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.42}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_exp027-mlp-rf-verifier_20260519T220906",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-19T22:10:41.478906+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "find /root/autodl-tmp/struct_self_consist_ie/ -name \"*mlp*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_exp027-mlp-rf-verifier_20260519T220906",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "find /root/autodl-tmp/struct_self_consist_ie/ -name \"*mlp*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-19T22:10:41.479038+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_027_mlp_verifier\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_027_mlp_verifier/train_mlp_verifier.py\\n/root/autodl-tmp/struct_self_consist_ie/output/r17_analyses/mlp_verifier_comparison.json\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_027v2_mlp_verifier\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_027v2_mlp_verifier/train_mlp_verifier_v2.py\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_027_mlp_v2\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_027_mlp_v2/train_mlp_verifier_v2.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_exp027-mlp-rf-verifier_20260519T220906",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-19T22:10:41.479183+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "find /root/autodl-tmp/struct_self_consist_ie/ -name \"*random_forest*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_exp027-mlp-rf-verifier_20260519T220906",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "find /root/autodl-tmp/struct_self_consist_ie/ -name \"*random_forest*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-19T22:10:41.479316+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_exp027-mlp-rf-verifier_20260519T220906",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-19T22:10:41.479472+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": "433",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_exp027-mlp-rf-verifier_20260519T220906",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "offset": "433",
    "limit": "80"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-19T22:10:41.479648+00:00_

433	\section{Supervised and Model-Internal Signal Analysis}\label{app:supervised_combination}
434	
435	\subsection{Supervised Signal Combination}
436	
437	Supervised classifiers (logistic regression, MLP, random forest) trained on all five signals (5-fold CV, 3-seed mean, SciERC, $N{=}16$, $+17.9$~pp headroom) all perform at or below greedy (F1${=}0.644$; LR: $-0.4$~pp; MLP: $-1.6$~pp; RF: $-3.1$~pp).
438	Adding pairwise interaction features does not help (AUROC 0.634 vs.\ 0.638).
439	To test whether richer representations could close the gap, we train a DeBERTa-v3-base verifier that encodes input-output pairs and predicts per-sample F1.
440	DeBERTa achieves $\rho{=}0.329{\pm}0.087$ (5-fold CV, 3 seeds). Despite moderate quality prediction, selection utility is poor: on SciERC, DeBERTa closes $-26.5{\pm}26.5$\% of the oracle gap (13 of 15 runs negative; vs.\ LP's $+4.2{\pm}10.7$\%); on Few-NERD, DeBERTa recovers only $+3.5$\% (single 80/20 split; vs.\ LP's $+16.3$\%).
441	Cross-dataset transfer fails entirely ($-27$\% to $-72$\% gap closure).
442	Neither handcrafted signal combinations nor learned text representations close the selection gap; only model-internal log-probability provides meaningful selection signal, consistent with an information asymmetry between the generating model and external observers.
443	
444	\subsection{Hidden State Probes}\label{app:hidden_probe}
445	
446	The preceding negative results suggest the bottleneck is model-internal rather than a feature engineering problem.
447	We test this directly by training probes on the generating model's hidden representations.
448	
449	\paragraph{Setup.}
450	For each of $N{=}8$ samples per instance, we extract the mean-pooled final-layer hidden state ($d{=}4096$) from the generating Qwen3-8B model and train a linear probe and a two-layer MLP (hidden dim${=}256$) to predict per-sample F1 (5-fold CV, 3 seeds).
451	
452	\begin{table}[t]
453	\centering
454	\small
455	\caption{Hidden state probes vs.\ LP for sa
…[truncated 4131 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_exp027-mlp-rf-verifier_20260519T220906",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-19T22:10:41.479803+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/supervised_verifier_upgrade/results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_exp027-mlp-rf-verifier_20260519T220906",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/supervised_verifier_upgrade/results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-19T22:10:41.480034+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"scierc\\\": {\\n    \\\"n_instances\\\": 477,\\n    \\\"n_features\\\": 5,\\n    \\\"features\\\": [\\n      \\\"soft_jaccard\\\",\\n      \\\"fleiss_kappa\\\",\\n      \\\"logprob\\\",\\n      \\\"exact_match\\\",\\n      \\\"voting_confidence\\\"\\n    ],\\n    \\\"binarize_method\\\": \\\"above_median\\\",\\n    \\\"threshold\\\": 0.6667,\\n    \\\"auroc\\\": {\\n      \\\"LR\\\": {\\n        \\\"mean_auroc\\\": 0.6713,\\n        \\\"std_auroc\\\": 0.0308\\n      },\\n      \\\"MLP\\\": {\\n        \\\"mean_auroc\\\": 0.6447,\\n        \\\"std_auroc\\\": 0.0179\\n      },\\n      \\\"RF\\\": {\\n        \\\"mean_auroc\\\": 0.5981,\\n        \\\"std_auroc\\\": 0.0243\\n      }\\n    },\\n    \\\"feature_importance\\\": {\\n      \\\"RF_gini\\\": {\\n        \\\"soft_jaccard\\\": 0.2176,\\n        \\\"fleiss_kappa\\\": 0.2224,\\n        \\\"logprob\\\": 0.3206,\\n        \\\"exact_match\\\": 0.1363,\\n        \\\"voting_confidence\\\": 0.103\\n      },\\n      \\\"MLP_permutation\\\": {\\n        \\\"soft_jaccard\\\": 0.035,\\n        \\\"fleiss_kappa\\\": 0.0163,\\n        \\\"logprob\\\": 0.0321,\\n        \\\"exact_match\\\": 0.0615,\\n        \\\"voting_confidence\\\": 0.0097\\n      },\\n      \\\"LR_abs_coef\\\": {\\n        \\\"soft_jaccard\\\": 0.3404,\\n        \\\"fleiss_kappa\\\": 0.0897,\\n        \\\"logprob\\\": 0.0597,\\n        \\\"exact_match\\\": 0.4346,\\n        \\\"voting_confidence\\\": 0.0572\\n      }\\n    },\\n    \\\"selection\\\": {\\n      \\\"greedy\\\": 0.7144,\\n      \\\"random_avg\\\": 0.6622,\\n      \\\"oracle\\\": 0.8231,\\n      \\\"LR\\\": {\\n        \\\"selection_f1\\\": 0.6876,\\n        \\\"delta_vs_greedy\\\": -0.0268\\n      },\\n      \\\"MLP\\\": {\\n        \\\"selection_f1\\\": 0.6895,\\n        \\\"delta_vs_greedy\\\": -0.0249\\n      },\\n      \\\"RF\\\": {\\n        \\\"selection_f1\\\": 0.6804,\\n        \\\"delta_vs_greedy\\\": -0.034\\n      }\\
…[truncated 4047 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_exp027-mlp-rf-verifier_20260519T220906",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-19T22:10:41.480221+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/exp_027v2_mlp_verifier/results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_exp027-mlp-rf-verifier_20260519T220906",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/exp_027v2_mlp_verifier/results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-19T22:10:41.480490+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"per_seed\\\": {\\n    \\\"42\\\": {\\n      \\\"LR_5feat\\\": {\\n        \\\"auroc\\\": 0.6634,\\n        \\\"selection_f1\\\": 0.6396\\n      },\\n      \\\"MLP_5feat\\\": {\\n        \\\"auroc\\\": 0.6389,\\n        \\\"selection_f1\\\": 0.619\\n      },\\n      \\\"RF_5feat\\\": {\\n        \\\"auroc\\\": 0.6042,\\n        \\\"selection_f1\\\": 0.6154\\n      },\\n      \\\"MLP_15feat\\\": {\\n        \\\"auroc\\\": 0.6502,\\n        \\\"selection_f1\\\": 0.6244\\n      },\\n      \\\"single_signal_aurocs\\\": {\\n        \\\"SJ\\\": 0.5838,\\n        \\\"FK\\\": 0.4915,\\n        \\\"LP\\\": 0.5618,\\n        \\\"EM\\\": 0.6509,\\n        \\\"VC\\\": 0.5676\\n      },\\n      \\\"unsup_selection_f1\\\": {\\n        \\\"SJ\\\": 0.646,\\n        \\\"FK\\\": 0.6469,\\n        \\\"LP\\\": 0.6453,\\n        \\\"EM\\\": 0.6317,\\n        \\\"VC\\\": 0.589\\n      },\\n      \\\"greedy_f1\\\": 0.6442,\\n      \\\"oracle_f1\\\": 0.8247,\\n      \\\"rf_importance_15\\\": {\\n        \\\"SJ\\\": 0.0581,\\n        \\\"FK\\\": 0.0622,\\n        \\\"LP\\\": 0.0802,\\n        \\\"EM\\\": 0.0427,\\n        \\\"VC\\\": 0.0501,\\n        \\\"SJxFK\\\": 0.0641,\\n        \\\"SJxLP\\\": 0.0755,\\n        \\\"SJxEM\\\": 0.0752,\\n        \\\"SJxVC\\\": 0.0542,\\n        \\\"FKxLP\\\": 0.0885,\\n        \\\"FKxEM\\\": 0.0695,\\n        \\\"FKxVC\\\": 0.0568,\\n        \\\"LPxEM\\\": 0.0839,\\n        \\\"LPxVC\\\": 0.0702,\\n        \\\"EMxVC\\\": 0.0688\\n      },\\n      \\\"ablation_mlp\\\": {\\n        \\\"SJ\\\": {\\n          \\\"auroc_without\\\": 0.6496,\\n          \\\"delta\\\": -0.0107\\n        },\\n        \\\"FK\\\": {\\n          \\\"auroc_without\\\": 0.6346,\\n          \\\"delta\\\": 0.0043\\n        },\\n        \\\"LP\\\": {\\n          \\\"auroc_without\\\": 0.6649,\\n          \\\"delta\\\": -0.026\\n        },\\n        \\\"EM\\\": {\\n          \\\"auroc_without\\\": 0.6067,\\n          \\\"de
…[truncated 5759 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_exp027-mlp-rf-verifier_20260519T220906",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-19T22:10:41.480654+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/exp_027_mlp_verifier/results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_exp027-mlp-rf-verifier_20260519T220906",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/exp_027_mlp_verifier/results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-19T22:10:41.480946+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"per_seed\\\": {\\n    \\\"42\\\": {\\n      \\\"LR_5feat\\\": {\\n        \\\"auroc\\\": 0.6634,\\n        \\\"selection_f1\\\": 0.6396\\n      },\\n      \\\"MLP_5feat\\\": {\\n        \\\"auroc\\\": 0.6629,\\n        \\\"selection_f1\\\": 0.6357\\n      },\\n      \\\"RF_5feat\\\": {\\n        \\\"auroc\\\": 0.6042,\\n        \\\"selection_f1\\\": 0.6196\\n      },\\n      \\\"MLP_15feat\\\": {\\n        \\\"auroc\\\": 0.6434,\\n        \\\"selection_f1\\\": 0.6282\\n      },\\n      \\\"RF_15feat\\\": {\\n        \\\"auroc\\\": 0.6267,\\n        \\\"selection_f1\\\": 0.6121\\n      },\\n      \\\"single_signal_aurocs\\\": {\\n        \\\"SJ\\\": 0.5838,\\n        \\\"FK\\\": 0.4915,\\n        \\\"LP\\\": 0.5618,\\n        \\\"EM\\\": 0.6509,\\n        \\\"VC\\\": 0.5676\\n      },\\n      \\\"unsup_selection_f1\\\": {\\n        \\\"SJ\\\": 0.646,\\n        \\\"FK\\\": 0.6469,\\n        \\\"LP\\\": 0.6453,\\n        \\\"EM\\\": 0.6317,\\n        \\\"VC\\\": 0.589\\n      },\\n      \\\"greedy_f1\\\": 0.6442,\\n      \\\"oracle_f1\\\": 0.8247,\\n      \\\"rf_feature_importance_15\\\": {\\n        \\\"SJ\\\": 0.0581,\\n        \\\"FK\\\": 0.0622,\\n        \\\"LP\\\": 0.0802,\\n        \\\"EM\\\": 0.0427,\\n        \\\"VC\\\": 0.0501,\\n        \\\"SJxFK\\\": 0.0641,\\n        \\\"SJxLP\\\": 0.0755,\\n        \\\"SJxEM\\\": 0.0752,\\n        \\\"SJxVC\\\": 0.0542,\\n        \\\"FKxLP\\\": 0.0885,\\n        \\\"FKxEM\\\": 0.0695,\\n        \\\"FKxVC\\\": 0.0568,\\n        \\\"LPxEM\\\": 0.0839,\\n        \\\"LPxVC\\\": 0.0702,\\n        \\\"EMxVC\\\": 0.0688\\n      },\\n      \\\"rf_feature_importance_5\\\": {\\n        \\\"SJ\\\": 0.1894,\\n        \\\"FK\\\": 0.2324,\\n        \\\"LP\\\": 0.2728,\\n        \\\"EM\\\": 0.1338,\\n        \\\"VC\\\": 0.1717\\n      },\\n      \\\"ablation_mlp\\\": {\\n        \\\"SJ\\\": {\\n          \\\"auroc_without\\\": 0.6558,\\n          \\\"delta_from_full_5\\\"
…[truncated 7119 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_exp027-mlp-rf-verifier_20260519T220906",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-19T22:10:41.481117+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/r17_analyses/mlp_verifier_comparison.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_exp027-mlp-rf-verifier_20260519T220906",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/r17_analyses/mlp_verifier_comparison.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-19T22:10:41.481410+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"experiment\\\": \\\"exp-027 MLP Verifier Comparison\\\",\\n  \\\"data\\\": \\\"SciERC NER, N=16, 3 seeds (42, 123, 456)\\\",\\n  \\\"data_source\\\": \\\"exp_001_seed{42,123,456}_v2\\\",\\n  \\\"n_instances_per_seed\\\": 551,\\n  \\\"baselines\\\": {\\n    \\\"greedy_f1\\\": 0.6441,\\n    \\\"oracle_f1\\\": 0.8231,\\n    \\\"oracle_greedy_gap\\\": 0.179,\\n    \\\"best_single_signal\\\": \\\"EM\\\",\\n    \\\"best_single_signal_auroc\\\": 0.6476,\\n    \\\"best_unsup_signal\\\": \\\"LP\\\",\\n    \\\"best_unsup_selection_f1\\\": 0.647\\n  },\\n  \\\"model_comparison\\\": [\\n    {\\n      \\\"model\\\": \\\"LR_5feat\\\",\\n      \\\"auroc_mean\\\": 0.6522,\\n      \\\"auroc_std\\\": 0.013,\\n      \\\"selection_f1_mean\\\": 0.6407,\\n      \\\"selection_f1_std\\\": 0.001,\\n      \\\"delta_vs_greedy\\\": -0.0034,\\n      \\\"oracle_gap_closed_pct\\\": -1.9\\n    },\\n    {\\n      \\\"model\\\": \\\"MLP_5feat\\\",\\n      \\\"auroc_mean\\\": 0.6393,\\n      \\\"auroc_std\\\": 0.0209,\\n      \\\"selection_f1_mean\\\": 0.6386,\\n      \\\"selection_f1_std\\\": 0.0029,\\n      \\\"delta_vs_greedy\\\": -0.0055,\\n      \\\"oracle_gap_closed_pct\\\": -3.1\\n    },\\n    {\\n      \\\"model\\\": \\\"RF_5feat\\\",\\n      \\\"auroc_mean\\\": 0.5868,\\n      \\\"auroc_std\\\": 0.0208,\\n      \\\"selection_f1_mean\\\": 0.6154,\\n      \\\"selection_f1_std\\\": 0.0076,\\n      \\\"delta_vs_greedy\\\": -0.0287,\\n      \\\"oracle_gap_closed_pct\\\": -16.0\\n    },\\n    {\\n      \\\"model\\\": \\\"MLP_15feat\\\",\\n      \\\"auroc_mean\\\": 0.6322,\\n      \\\"auroc_std\\\": 0.0165,\\n      \\\"selection_f1_mean\\\": 0.6339,\\n      \\\"selection_f1_std\\\": 0.005,\\n      \\\"delta_vs_greedy\\\": -0.0102,\\n      \\\"oracle_gap_closed_pct\\\": -5.7\\n    },\\n    {\\n      \\\"model\\\": \\\"RF_15feat\\\",\\n      \\\"auroc_mean\\\": 0.6043,\\n      \\\"auroc_std\\\": 0.0314,\\n      \\\"selection_f1_mean\\\
…[truncated 5295 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_exp027-mlp-rf-verifier_20260519T220906",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-19T22:10:41.481576+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/exp_019_trained_verifier/results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_exp027-mlp-rf-verifier_20260519T220906",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/exp_019_trained_verifier/results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-19T22:10:41.481869+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"per_seed\\\": {\\n    \\\"42\\\": {\\n      \\\"n_instances\\\": 529,\\n      \\\"n_samples\\\": 8,\\n      \\\"greedy_f1\\\": 0.6439,\\n      \\\"oracle_f1\\\": 0.7758,\\n      \\\"unsup_selection_f1\\\": {\\n        \\\"SJ\\\": 0.645,\\n        \\\"FK\\\": 0.6448,\\n        \\\"LP\\\": 0.6501,\\n        \\\"EM\\\": 0.6362,\\n        \\\"VC\\\": 0.6256\\n      },\\n      \\\"lr_selection_f1_loo\\\": 0.6484,\\n      \\\"lr_selection_f1_5fold\\\": 0.6475,\\n      \\\"lr_auroc_loo\\\": 0.6795,\\n      \\\"lr_auroc_5fold\\\": 0.6794,\\n      \\\"single_signal_aurocs\\\": {\\n        \\\"SJ\\\": 0.6715,\\n        \\\"FK\\\": 0.6154,\\n        \\\"LP\\\": 0.6116,\\n        \\\"EM\\\": 0.6472,\\n        \\\"VC\\\": 0.6879\\n      },\\n      \\\"feature_importance\\\": {\\n        \\\"SJ\\\": -0.1739,\\n        \\\"FK\\\": 0.0925,\\n        \\\"LP\\\": 0.1161,\\n        \\\"EM\\\": 0.1913,\\n        \\\"VC\\\": 0.6455\\n      },\\n      \\\"ablation\\\": {\\n        \\\"SJ\\\": {\\n          \\\"auroc_without\\\": 0.6814,\\n          \\\"delta\\\": -0.0019\\n        },\\n        \\\"FK\\\": {\\n          \\\"auroc_without\\\": 0.6802,\\n          \\\"delta\\\": -0.0007\\n        },\\n        \\\"LP\\\": {\\n          \\\"auroc_without\\\": 0.6788,\\n          \\\"delta\\\": 0.0007\\n        },\\n        \\\"EM\\\": {\\n          \\\"auroc_without\\\": 0.678,\\n          \\\"delta\\\": 0.0015\\n        },\\n        \\\"VC\\\": {\\n          \\\"auroc_without\\\": 0.6577,\\n          \\\"delta\\\": 0.0218\\n        }\\n      },\\n      \\\"learning_curve\\\": {\\n        \\\"0.1\\\": {\\n          \\\"mean_auroc\\\": 0.6201,\\n          \\\"std_auroc\\\": 0.0755,\\n          \\\"n_train\\\": 52\\n        },\\n        \\\"0.25\\\": {\\n          \\\"mean_auroc\\\": 0.6682,\\n          \\\"std_auroc\\\": 0.0384,\\n          \\\"n_train\\\": 132\\n        },\\n        \\\"0.5\\\": {\\n          \\\"mean_auroc\\\"
…[truncated 7138 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_exp027-mlp-rf-verifier_20260519T220906",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 31 · 2026-05-19T22:10:41.482113+00:00_

## 结论：✅ 数据存在，论文数值匹配

### 数据源路径

| 文件 | 说明 |
|------|------|
| `/root/autodl-tmp/struct_self_consist_ie/output/exp_027_mlp_verifier/results.json` | **论文引用的主数据源**（SciERC, N=16, 3 seeds: 42/123/456, 5-fold CV） |
| `/root/autodl-tmp/struct_self_consist_ie/output/exp_027v2_mlp_verifier/results.json` | v2 版本（MLP 有 hyperparameter 调整，数值略不同） |
| `/root/autodl-tmp/struct_self_consist_ie/output/supervised_verifier_upgrade/results.json` | 3 数据集全量结果（SciERC/CoNLL/Few-NERD） |
| `/root/autodl-tmp/struct_self_consist_ie/output/r17_analyses/mlp_verifier_comparison.json` | 汇总对比（含 diagnosis） |

### 数值比对（appendix L437 vs `exp_027_mlp_verifier`）

| 指标 | 论文声称 | 数据实际值 | 匹配 |
|------|---------|-----------|------|
| Greedy F1 | 0.644 | 0.6441 | ✓ |
| LR Δ vs greedy | −0.4 pp | −0.35 pp (0.6406) | ✓ (四舍五入) |
| MLP Δ vs greedy | −1.6 pp | −1.63 pp (0.6278) | ✓ |
| RF Δ vs greedy | −3.1 pp | −3.08 pp (0.6133) | ✓ |
| AUROC (interaction vs base) | 0.634 vs 0.638 | MLP_15feat 0.6341 vs MLP_5feat 0.6381 | ✓ |

所有数值一致。experiment_plan 标记为 planned 应更新为 completed。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_audit_exp027-mlp-rf-verifier_20260519T220906"
}
```

</details>

---
