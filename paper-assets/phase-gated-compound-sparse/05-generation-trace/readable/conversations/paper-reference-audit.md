# paper reference audit

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 179
- **Recorded user turns:** 0
- **Tool calls:** 89
- **Original source:** `logs/chats/worker_paper_reference_audit_20260514T094550.jsonl`
- **Structured JSON:** [`c7f728c5747cebdd982c.json`](../../sessions/c7/c7f728c5747cebdd982c.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

179 recorded events

### Tool call

_source line 1 · 2026-05-14T09:53:45.716691+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Extract all citation keys",
  "subagent_type": "Explore",
  "prompt": "Search all .tex files in /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/ for \\cite commands. I need every unique citation key from these files ONLY (ignore files with suffixes like _fc6d1d.tex, _4cc5f3.tex, _46fb53.tex, results_5_1.tex):\n- introduction.tex\n- related_work.tex\n- background.tex\n- methodology.tex\n- results.tex\n- analysis.tex\n- discussion.tex\n- conclusion.tex\n- abstract.tex\n\nUse Grep with pattern \"\\\\\\\\cite[tp]?\\\\{[^}]+\\\\}\" to find all cite commands, then list every unique citation key. Be very thorough - check all variants like \\cite, \\citep, \\citet, \\citealt, etc."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "Agent",
  "tool_args": {
    "description": "Extract all citation keys",
    "subagent_type": "Explore",
    "prompt": "Search all .tex files in /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/ for \\cite commands. I need every unique citation key from these files ONLY (ignore files with suffixes like _fc6d1d.tex, _4cc5f3.tex, _46fb53.tex, results_5_1.tex):\n- introduction.tex\n- related_work.tex\n- background.tex\n- methodology.tex\n- results.tex\n- analysis.tex\n- discussion.tex\n- conclusion.tex\n- abstract.tex\n\nUse Grep with pattern \"\\\\\\\\cite[tp]?\\\\{[^}]+\\\\}\" to find all cite commands, then list every unique citation key. Be very thorough - check all variants like \\cite, \\citep, \\citet, \\citealt, etc."
  }
}
```

</details>

---

### Tool call

_source line 2 · 2026-05-14T09:53:45.717157+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/ | grep -E \"\\.tex$\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/ | grep -E \"\\.tex$\""
  }
}
```

</details>

---

### Tool result

_source line 3 · 2026-05-14T09:53:45.717451+00:00_

-rw-r--r-- 1 ubuntu ubuntu  2379 May 14 09:44 abstract.tex
-rw-r--r-- 1 ubuntu ubuntu  9444 May 14 09:33 analysis.tex
-rw-r--r-- 1 ubuntu ubuntu  8122 May 14 05:42 background.tex
-rw-r--r-- 1 ubuntu ubuntu  7131 May 14 05:30 background_fc6d1d.tex
-rw-r--r-- 1 ubuntu ubuntu  3989 May 14 09:44 conclusion.tex
-rw-r--r-- 1 ubuntu ubuntu 15491 May 14 09:46 discussion.tex
-rw-r--r-- 1 ubuntu ubuntu  5537 May 14 09:35 introduction.tex
-rw-r--r-- 1 ubuntu ubuntu  8540 May 14 05:48 methodology.tex
-rw-r--r-- 1 ubuntu ubuntu  8515 May 14 05:42 methodology_4cc5f3.tex
-rw-r--r-- 1 ubuntu ubuntu  5710 May 14 06:38 related_work.tex
-rw-r--r-- 1 ubuntu ubuntu  5259 May 14 05:30 related_work_46fb53.tex
-rw-r--r-- 1 ubuntu ubuntu 21068 May 14 09:45 results.tex
-rw-r--r-- 1 ubuntu ubuntu  7670 May 14 06:02 results_5_1.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-14T09:53:45.717694+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\cite[p|t|alt|author|year|alp|num]*\\{[^}]+\\}",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/introduction.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\cite[p|t|alt|author|year|alp|num]*\\{[^}]+\\}",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/introduction.tex",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-14T09:53:45.717897+00:00_

4:Long-context language models place acute pressure on the key--value (KV) cache, which grows linearly with sequence length and dominates inference memory at scale \cite{kwon2023vllm, pope2023efficiently}.
5:Two complementary responses have emerged: \emph{attention head pruning}, which removes structurally redundant heads \cite{voita2019heads, michel2019sixteen}, and \emph{KV cache eviction}, which discards low-importance token positions from the cache \cite{snapkv-neurips2024, adakv-neurips2025}.
6:Deploying both simultaneously---\emph{compound sparsity}---is attractive because the compression gains multiply, but the resulting quality degradation can be super-additive: the joint loss exceeds the sum of individual losses \cite{spark-aaai2026, slim-icml2025}.
8:Prior work has characterized compound interaction as a property of the sparsity level---higher sparsity yields more interaction---but treats the interaction magnitude as roughly constant across the generation process \cite{spark-aaai2026, unicomp-2026}.
9:This assumption is problematic for reasoning-capable models, whose generations are structurally heterogeneous: a single chain-of-thought trace alternates between phases of broadly distributed attention (exploratory reasoning) and phases of sharply concentrated attention (structured computation) \cite{thinkv-iclr2026, decision-repr-transition-2026}.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-14T09:53:45.718125+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\cite[p|t|alt|author|year|alp|num]*\\{[^}]+\\}",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/related_work.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\cite[p|t|alt|author|year|alp|num]*\\{[^}]+\\}",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/related_work.tex",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-14T09:53:45.718324+00:00_

7:\cite{spark-aaai2026} report super-additive degradation when combining channel pruning with token eviction, with up to 65\% quality loss exceeding individual component effects---the first explicit measurement of this phenomenon in KV cache sparsity.
8:\cite{slim-icml2025} formalize compound error for quantization and sparsity, deriving an invertible saliency function for low-rank compensation and confirming that aggregated error is strictly non-additive.
9:\cite{unicomp-2026} evaluate compound compression across 40+ benchmarks, revealing that reasoning and multilingual capabilities degrade disproportionately relative to factual recall.
10:The order of compression stages is itself consequential: \cite{compression-ordering-2025} show that early quantization causes irreversible information loss, making P$\to$KD$\to$Q strictly preferable.
11:At a more fundamental level, \cite{phase-transition-compression-2026} characterize independent phase transition points per compression dimension, implying that the joint safe region is the intersection---not the union---of per-dimension safe zones.
12:On the structural side, GRASPrune~\cite{graspune-acl2026} learns global budget-constrained gates to jointly prune FFN channels and attention heads, but treats the pruning decision as static across generation.
19:Ada-KV~\cite{adakv-neurips2025} introduce per-head adaptive budget allocation, outperforming uniform distribution but assuming stable importance across generation.
20:SnapKV~\cite{snapkv-neurips2024} identifies important KV positions per head from an observation window at the end of the prompt, compressing the cache before generation begins---effective for long contexts but committing to a fixed importance snapshot that cannot adapt across reasoning phases.
21:\cite{defensivekv-iclr2026} show that standard mean-based importance aggregation is fragile, with worst-case quality loss 2.3--4.3$\times$ higher than expected; their defensive aggregation mitigates but does not elimina
…[truncated 2225 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-14T09:53:45.718572+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\cite[p|t|alt|author|year|alp|num]*\\{[^}]+\\}",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/background.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\cite[p|t|alt|author|year|alp|num]*\\{[^}]+\\}",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/background.tex",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-14T09:53:45.718758+00:00_

17:For each layer $\ell$, heads are ranked by Frobenius norm importance $w_j^{(\ell)} = \|\mathbf{A}_j^{(\ell)}\|_F$, where $\mathbf{A}_j^{(\ell)} \in \mathbb{R}^{T \times T}$ is the attention matrix for head $j$ \cite{voita2019heads, michel2019sixteen}.
38:    where the denominator compensates for causal bias---earlier positions are attended to by more queries \cite{thinkv-iclr2026, defensivekv-iclr2026}.
45:Prior analyses of compound compression \cite{spark-aaai2026} report that the joint effect is generally super-additive but treat the interaction magnitude as a fixed property of $s$.
91:We partition each generated sequence into three phases based on the local \emph{attention sparsity profile}, adapting the phase-aware methodology of ThinKV \cite{thinkv-iclr2026}.
111:This phase structure arises naturally during extended chain-of-thought reasoning, where the model alternates between focused retrieval of specific facts (high sparsity) and integrative reasoning across many context positions (low sparsity) \cite{phase-transition-compression-2026}.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-14T09:53:45.718965+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\cite[p|t|alt|author|year|alp|num]*\\{[^}]+\\}",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/methodology.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\cite[p|t|alt|author|year|alp|num]*\\{[^}]+\\}",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/methodology.tex",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-14T09:53:45.719141+00:00_

9:\paragraph{DeepSeek-R1-Distill-Qwen-7B} serves as our primary evaluation target. This model was distilled from DeepSeek-R1 \cite{deepseek-r1} and produces explicit chain-of-thought traces delimited by \texttt{&lt;think>}$\cdots$\texttt{&lt;/think>} tags, yielding sequences with pronounced phase structure---extended reasoning followed by a concise solution. The structured generation pattern makes it well-suited for studying how sparsity interacts with distinct reasoning phases.
11:\paragraph{Qwen2.5-7B-Instruct} \cite{qwen2.5} provides a cross-model replication. Although it shares the same backbone family, its instruction tuning does not enforce explicit reasoning delimiters, producing a different distribution of attention sparsity across the generation trajectory. Replication on this model tests whether our findings generalize beyond distillation-induced phase structure.
19:[Omitted long matching line]
78:All confidence intervals and significance tests are computed via the nonparametric bootstrap with $B = 10{,}000$ resamples \cite{efron1993bootstrap}.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-14T09:53:45.719328+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\cite[p|t|alt|author|year|alp|num]*\\{[^}]+\\}",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/results.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\cite[p|t|alt|author|year|alp|num]*\\{[^}]+\\}",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/results.tex",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-14T09:53:45.719515+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-14T09:53:45.719694+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\cite[p|t|alt|author|year|alp|num]*\\{[^}]+\\}",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/analysis.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\cite[p|t|alt|author|year|alp|num]*\\{[^}]+\\}",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/analysis.tex",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-14T09:53:45.719874+00:00_

90:[Omitted long matching line]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-14T09:53:45.720062+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\cite[p|t|alt|author|year|alp|num]*\\{[^}]+\\}",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/discussion.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\cite[p|t|alt|author|year|alp|num]*\\{[^}]+\\}",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/discussion.tex",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-14T09:53:45.720237+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-14T09:53:45.720400+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\cite[p|t|alt|author|year|alp|num]*\\{[^}]+\\}",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/conclusion.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\cite[p|t|alt|author|year|alp|num]*\\{[^}]+\\}",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/conclusion.tex",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-14T09:53:45.720600+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-14T09:53:45.720787+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\cite[p|t|alt|author|year|alp|num]*\\{[^}]+\\}",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/abstract.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\cite[p|t|alt|author|year|alp|num]*\\{[^}]+\\}",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/abstract.tex",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-14T09:53:45.720919+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-14T09:53:45.721041+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/discussion.tex"
  }
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-14T09:53:45.721164+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/analysis.tex"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-14T09:53:45.721329+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{On the predictability of phase-modulated severity.}
5	One might argue that the qualitative direction of our findings is intuitive: in low-sparsity phases, attention distributes broadly across many tokens, so importance scores carry less discriminative signal, and importance-based eviction should degrade.
6	We do not dispute this intuition.
7	The surprise lies in the quantitative structure of the interaction, which is not predictable from first principles alone.
8	
9	First, the \emph{magnitude} of the severity gradient---$69$--$274{\times}$ amplification across sparsity levels (Table~\ref{tab:main-results})---far exceeds what a naive ``less discriminative $\Rightarrow$ somewhat worse'' argument would predict. % exp_id: bf16_importance_s015..s030; source: experiment_summary_table.json; G=low/high=69,103,222,274.
10	A reviewer expecting a $2$--$3\times$ effect would find two-orders-of-magnitude amplification difficult to anticipate without measurement.
11	Second, the gradient is \emph{phase-specific}: compound interaction concentrates in low-sparsity phases while high-sparsity phases exhibit near-zero compound interaction ($\widetilde{\mathrm{II}}_{\text{high}} < 0.06$ at $s \leq 0.30$; at $s = 0.35$, high-phase II rises to 0.105, indicating the onset of compound interaction even in high-sparsity phases at extreme pruning rates). % exp_id: bf16_importance_s015..s030; high-phase medians: 0.006, 0.015, 0.032, 0.053
12	This asymmetry means that importance-based eviction is not uniformly fragile---it is selectively fragile in a phase-dependent manner.
13	Third, and most strikingly, a \emph{crossover} emerges: at $s{=}0.25$, importance-based eviction \emph{outperforms} random eviction in high-sparsity phases (median severity $0.032$ vs.\ $0.818$) yet \emph{underperforms} in low-sparsity phases ($7.196$ vs.\ $1.363$---a ${>}5{\times}$ severity inflation relative to random). % exp_id: bf16_importance_s025, bf16_d
…[truncated 13783 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-14T09:53:45.721572+00:00_

1	
2	\section{Analysis: Mechanisms of Phase-Modulated Severity}
3	\label{sec:analysis}
4	
5	The results in \S\ref{sec:results} reveal a striking asymmetry: importance-based eviction exhibits $69$--$274{\times}$ severity amplification in low-sparsity phases (Table~\ref{tab:main-results}), while random eviction remains flat at ${\sim}1{\times}$ across all phases. % exp_id: bf16_importance_s015..s030; G=69,103,222,274
6	Why is compound severity phase-modulated for one strategy but not the other? We identify two mechanisms. \emph{Discrimination collapse}---a systematic reduction in the discriminative power of KV importance scores under head pruning---is the primary mechanism, robustly observed across both models and all tested conditions. A secondary \emph{entropy redistribution} pattern is consistent for DeepSeek but only partially replicates on Qwen, indicating model-dependent modulation.
7	
8	\subsection{Discrimination Collapse Under Head Pruning}
9	\label{sec:discrimination-collapse}
10	
11	The KV importance score (Eq.~\ref{eq:kv-importance}) aggregates attention mass across surviving heads. When head pruning reduces the number of contributing heads, the cumulative importance distribution becomes more uniform: the gap between highly-attended and rarely-attended positions shrinks. We quantify this effect through two complementary metrics applied to the per-position importance distribution.
12	
13	The \textbf{Gini coefficient} measures inequality in the importance distribution ($\mathrm{Gini}{=}0$: perfectly uniform; $\mathrm{Gini}{=}1$: maximally concentrated). The \textbf{coefficient of variation} (CV) captures relative dispersion. A decrease in either metric after pruning indicates reduced discriminative power.
14	
15	We observe discrimination collapse across both models in all tested conditions (Table~\ref{tab:discrimination-metrics}). Under importance-based eviction, the Gini delta is negative at every sparsity level for both DeepSeek ($-0.030$ to $-0.081$) and Q
…[truncated 7720 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-14T09:53:45.721755+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/introduction.tex | grep -o '\\\\cite[a-z]*{[^}]*}' | sed 's/\\\\cite[a-z]*{\\([^}]*\\)}/\\1/' | tr ',' '\\n' | sed 's/^[[:space:]]*//;s/[[:space:]]*$//' | sort -u"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/introduction.tex | grep -o '\\\\cite[a-z]*{[^}]*}' | sed 's/\\\\cite[a-z]*{\\([^}]*\\)}/\\1/' | tr ',' '\\n' | sed 's/^[[:space:]]*//;s/[[:space:]]*$//' | sort -u"
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-14T09:53:45.721882+00:00_

adakv-neurips2025
decision-repr-transition-2026
kwon2023vllm
michel2019sixteen
pope2023efficiently
slim-icml2025
snapkv-neurips2024
spark-aaai2026
thinkv-iclr2026
unicomp-2026
voita2019heads

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-14T09:53:45.722011+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/related_work.tex | grep -o '\\\\cite[a-z]*{[^}]*}' | sed 's/\\\\cite[a-z]*{\\([^}]*\\)}/\\1/' | tr ',' '\\n' | sed 's/^[[:space:]]*//;s/[[:space:]]*$//' | sort -u"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/related_work.tex | grep -o '\\\\cite[a-z]*{[^}]*}' | sed 's/\\\\cite[a-z]*{\\([^}]*\\)}/\\1/' | tr ',' '\\n' | sed 's/^[[:space:]]*//;s/[[:space:]]*$//' | sort -u"
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-14T09:53:45.722130+00:00_

adakv-neurips2025
compression-ordering-2025
decision-repr-transition-2026
defensivekv-iclr2026
doing-more-with-less-2026
graspune-acl2026
greedy-bias-kvcache-2026
mustafar-neurips2025
nacl-acl2024
obcache-2025
pagedeviction-eacl2026
phase-transition-compression-2026
raas-acl2025
retentivekv-2026
slim-icml2025
snapkv-neurips2024
spark-aaai2026
sparse-frontier-2025
thinkv-iclr2026
unicomp-2026

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-14T09:53:45.722332+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/background.tex | grep -o '\\\\cite[a-z]*{[^}]*}' | sed 's/\\\\cite[a-z]*{\\([^}]*\\)}/\\1/' | tr ',' '\\n' | sed 's/^[[:space:]]*//;s/[[:space:]]*$//' | sort -u"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/background.tex | grep -o '\\\\cite[a-z]*{[^}]*}' | sed 's/\\\\cite[a-z]*{\\([^}]*\\)}/\\1/' | tr ',' '\\n' | sed 's/^[[:space:]]*//;s/[[:space:]]*$//' | sort -u"
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-14T09:53:45.722551+00:00_

defensivekv-iclr2026
michel2019sixteen
phase-transition-compression-2026
spark-aaai2026
thinkv-iclr2026
voita2019heads

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-14T09:53:45.722734+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/methodology.tex | grep -o '\\\\cite[a-z]*{[^}]*}' | sed 's/\\\\cite[a-z]*{\\([^}]*\\)}/\\1/' | tr ',' '\\n' | sed 's/^[[:space:]]*//;s/[[:space:]]*$//' | sort -u"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/methodology.tex | grep -o '\\\\cite[a-z]*{[^}]*}' | sed 's/\\\\cite[a-z]*{\\([^}]*\\)}/\\1/' | tr ',' '\\n' | sed 's/^[[:space:]]*//;s/[[:space:]]*$//' | sort -u"
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-14T09:53:45.722887+00:00_

deepseek-r1
efron1993bootstrap
math500
qwen2.5

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-14T09:53:45.723032+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/results.tex | grep -o '\\\\cite[a-z]*{[^}]*}' | sed 's/\\\\cite[a-z]*{\\([^}]*\\)}/\\1/' | tr ',' '\\n' | sed 's/^[[:space:]]*//;s/[[:space:]]*$//' | sort -u"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/results.tex | grep -o '\\\\cite[a-z]*{[^}]*}' | sed 's/\\\\cite[a-z]*{\\([^}]*\\)}/\\1/' | tr ',' '\\n' | sed 's/^[[:space:]]*//;s/[[:space:]]*$//' | sort -u"
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-14T09:53:45.723172+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-14T09:53:45.723323+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/analysis.tex | grep -o '\\\\cite[a-z]*{[^}]*}' | sed 's/\\\\cite[a-z]*{\\([^}]*\\)}/\\1/' | tr ',' '\\n' | sed 's/^[[:space:]]*//;s/[[:space:]]*$//' | sort -u"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/analysis.tex | grep -o '\\\\cite[a-z]*{[^}]*}' | sed 's/\\\\cite[a-z]*{\\([^}]*\\)}/\\1/' | tr ',' '\\n' | sed 's/^[[:space:]]*//;s/[[:space:]]*$//' | sort -u"
  }
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-14T09:53:45.723486+00:00_

h2o2024
pyramidkv2024
snapkv2024

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-14T09:53:45.723658+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/discussion.tex | grep -o '\\\\cite[a-z]*{[^}]*}' | sed 's/\\\\cite[a-z]*{\\([^}]*\\)}/\\1/' | tr ',' '\\n' | sed 's/^[[:space:]]*//;s/[[:space:]]*$//' | sort -u"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/discussion.tex | grep -o '\\\\cite[a-z]*{[^}]*}' | sed 's/\\\\cite[a-z]*{\\([^}]*\\)}/\\1/' | tr ',' '\\n' | sed 's/^[[:space:]]*//;s/[[:space:]]*$//' | sort -u"
  }
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-14T09:53:45.723793+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-14T09:53:45.723949+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/conclusion.tex | grep -o '\\\\cite[a-z]*{[^}]*}' | sed 's/\\\\cite[a-z]*{\\([^}]*\\)}/\\1/' | tr ',' '\\n' | sed 's/^[[:space:]]*//;s/[[:space:]]*$//' | sort -u"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/conclusion.tex | grep -o '\\\\cite[a-z]*{[^}]*}' | sed 's/\\\\cite[a-z]*{\\([^}]*\\)}/\\1/' | tr ',' '\\n' | sed 's/^[[:space:]]*//;s/[[:space:]]*$//' | sort -u"
  }
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-14T09:53:45.724067+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-14T09:53:45.724207+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/abstract.tex | grep -o '\\\\cite[a-z]*{[^}]*}' | sed 's/\\\\cite[a-z]*{\\([^}]*\\)}/\\1/' | tr ',' '\\n' | sed 's/^[[:space:]]*//;s/[[:space:]]*$//' | sort -u"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/abstract.tex | grep -o '\\\\cite[a-z]*{[^}]*}' | sed 's/\\\\cite[a-z]*{\\([^}]*\\)}/\\1/' | tr ',' '\\n' | sed 's/^[[:space:]]*//;s/[[:space:]]*$//' | sort -u"
  }
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-14T09:53:45.724389+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-14T09:53:45.724594+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/results.tex",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/results.tex",
    "limit": "50"
  }
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-14T09:53:45.724805+00:00_

1	
2	\section{Results}
3	\label{sec:results}
4	
5	We present our empirical findings in five parts: strategy-dependent compound severity (\S\ref{sec:strategy-severity}), phase-modulated amplification (\S\ref{sec:phase-amplification}), the phase-strategy crossover (\S\ref{sec:crossover}), cross-model replication (\S\ref{sec:cross-model}), and statistical validation (\S\ref{sec:stat-validation}).
6	
7	
8	\subsection{Experimental Overview}
9	\label{sec:exp-overview}
10	
11	We evaluate compound sparsity on DeepSeek-R1-Distill-Qwen-7B using a 50-problem stratified subset of MATH-500 (\S\ref{sec:dataset}). For each problem, we measure perplexity under four conditions---dense, attention-only pruning, KV-only eviction, and compound (both)---at sparsity levels $s \in \{0.15, 0.20, 0.25, 0.30\}$. We compare importance-based and random eviction strategies (\S\ref{sec:sparsity-config}), and segment each generated sequence into high-, mid-, and low-sparsity reasoning phases via quantile-based attention sparsity partitioning (\S\ref{sec:phase-seg}). The interaction index (II, Eq.~\ref{eq:ii}) quantifies compound super-additivity, and the severity gradient ($G$, Eq.~\ref{eq:gradient}) captures phase-dependent amplification.
12	Models are evaluated in \texttt{bfloat16} precision (\S\ref{sec:experimental-setup}). Full experimental details appear therein.
13	
14	
15	\subsection{Strategy-Dependent Severity (C1)}
16	\label{sec:strategy-severity}
17	
18	The compound severity difference reveals a stark dependence on eviction strategy. Table~\ref{tab:aggregate-ii} reports the median compound severity difference $\Delta = \widetilde{\mathrm{II}}_{\textit{low}} - \widetilde{\mathrm{II}}_{\textit{high}}$ across 50 problems for each strategy and sparsity level. Under importance-based eviction, compound sparsity produces substantial super-additive degradation that grows with sparsity: $\Delta$ increases from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$, a $37{\times}$ amplification. Under rand
…[truncated 3151 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-14T09:53:45.725046+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat << 'EOF' > /tmp/all_citations.txt\nadakv-neurips2025\ncompression-ordering-2025\ndecision-repr-transition-2026\ndefensivekv-iclr2026\ndeepseek-r1\ndoing-more-with-less-2026\nefron1993bootstrap\ngraspune-acl2026\ngreedy-bias-kvcache-2026\nh2o2024\nmath500\nmichel2019sixteen\nmustafar-neurips2025\nnacl-acl2024\nobcache-2025\npagedeviction-eacl2026\nphase-transition-compression-2026\npope2023efficiently\npyramidkv2024\nqwen2.5\nraas-acl2025\nretentivekv-2026\nslim-icml2025\nsnapkv-neurips2024\nsnapkv2024\nspark-aaai2026\nsparse-frontier-2025\nthinkv-iclr2026\nunicomp-2026\nvoita2019heads\nkwon2023vllm\nEOF\nsort -u /tmp/all_citations.txt\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "Bash",
  "tool_args": {
    "command": "cat << 'EOF' > /tmp/all_citations.txt\nadakv-neurips2025\ncompression-ordering-2025\ndecision-repr-transition-2026\ndefensivekv-iclr2026\ndeepseek-r1\ndoing-more-with-less-2026\nefron1993bootstrap\ngraspune-acl2026\ngreedy-bias-kvcache-2026\nh2o2024\nmath500\nmichel2019sixteen\nmustafar-neurips2025\nnacl-acl2024\nobcache-2025\npagedeviction-eacl2026\nphase-transition-compression-2026\npope2023efficiently\npyramidkv2024\nqwen2.5\nraas-acl2025\nretentivekv-2026\nslim-icml2025\nsnapkv-neurips2024\nsnapkv2024\nspark-aaai2026\nsparse-frontier-2025\nthinkv-iclr2026\nunicomp-2026\nvoita2019heads\nkwon2023vllm\nEOF\nsort -u /tmp/all_citations.txt\n"
  }
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-14T09:53:45.725236+00:00_

adakv-neurips2025
compression-ordering-2025
decision-repr-transition-2026
deepseek-r1
defensivekv-iclr2026
doing-more-with-less-2026
efron1993bootstrap
graspune-acl2026
greedy-bias-kvcache-2026
h2o2024
kwon2023vllm
math500
michel2019sixteen
mustafar-neurips2025
nacl-acl2024
obcache-2025
pagedeviction-eacl2026
phase-transition-compression-2026
pope2023efficiently
pyramidkv2024
qwen2.5
raas-acl2025
retentivekv-2026
slim-icml2025
snapkv-neurips2024
snapkv2024
spark-aaai2026
sparse-frontier-2025
thinkv-iclr2026
unicomp-2026
voita2019heads

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-14T09:53:45.725495+00:00_

Perfect! Now let me create a comprehensive final list with the citation sources organized by file:

## Complete List of Unique Citation Keys from Specified .tex Files

I extracted all unique citation keys from the nine specified .tex files in `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/`. Here are the **32 unique citation keys**:

1. adakv-neurips2025
2. compression-ordering-2025
3. decision-repr-transition-2026
4. deepseek-r1
5. defensivekv-iclr2026
6. doing-more-with-less-2026
7. efron1993bootstrap
8. graspune-acl2026
9. greedy-bias-kvcache-2026
10. h2o2024
11. kwon2023vllm
12. math500
13. michel2019sixteen
14. mustafar-neurips2025
15. nacl-acl2024
16. obcache-2025
17. pagedeviction-eacl2026
18. phase-transition-compression-2026
19. pope2023efficiently
20. pyramidkv2024
21. qwen2.5
22. raas-acl2025
23. retentivekv-2026
24. slim-icml2025
25. snapkv-neurips2024
26. snapkv2024
27. spark-aaai2026
28. sparse-frontier-2025
29. thinkv-iclr2026
30. unicomp-2026
31. voita2019heads

**Distribution across files:**
- **introduction.tex**: 11 citations
- **related_work.tex**: 20 citations
- **background.tex**: 6 citations
- **methodology.tex**: 4 citations
- **results.tex**: 0 citations
- **analysis.tex**: 3 citations
- **discussion.tex**: 0 citations
- **conclusion.tex**: 0 citations
- **abstract.tex**: 0 citations

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "Agent",
  "elapsed_ms": 8
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-14T09:53:45.725726+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-14T09:53:45.725952+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Long-context language models place acute pressure on the key--value (KV) cache, which grows linearly with sequence length and dominates inference memory at scale \cite{kwon2023vllm, pope2023efficiently}.
5	Two complementary responses have emerged: \emph{attention head pruning}, which removes structurally redundant heads \cite{voita2019heads, michel2019sixteen}, and \emph{KV cache eviction}, which discards low-importance token positions from the cache \cite{snapkv-neurips2024, adakv-neurips2025}.
6	Deploying both simultaneously---\emph{compound sparsity}---is attractive because the compression gains multiply, but the resulting quality degradation can be super-additive: the joint loss exceeds the sum of individual losses \cite{spark-aaai2026, slim-icml2025}.
7	
8	Prior work has characterized compound interaction as a property of the sparsity level---higher sparsity yields more interaction---but treats the interaction magnitude as roughly constant across the generation process \cite{spark-aaai2026, unicomp-2026}.
9	This assumption is problematic for reasoning-capable models, whose generations are structurally heterogeneous: a single chain-of-thought trace alternates between phases of broadly distributed attention (exploratory reasoning) and phases of sharply concentrated attention (structured computation) \cite{thinkv-iclr2026, decision-repr-transition-2026}.
10	If compound interaction severity varies across these phases, then a uniform sparsity budget---the standard deployment practice---may be safe in one phase yet destructive in another.
11	
12	We investigate whether compound sparsity severity is modulated by reasoning phase and eviction strategy.
13	Our central finding is that it is, and strongly so: under importance-based KV cache eviction, the Interaction Index---a measure of super-additive compound degradation---is concentrated in the low-sparsity phase (where attention distributes broadly) and largely abs
…[truncated 3629 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-14T09:53:45.726166+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-14T09:53:45.726389+00:00_

1	\section{Related Work}
2	\label{sec:related}
3	
4	\subsection{Compound and Joint Compression}
5	
6	Combining multiple compression axes produces non-additive errors.
7	\cite{spark-aaai2026} report super-additive degradation when combining channel pruning with token eviction, with up to 65\% quality loss exceeding individual component effects---the first explicit measurement of this phenomenon in KV cache sparsity.
8	\cite{slim-icml2025} formalize compound error for quantization and sparsity, deriving an invertible saliency function for low-rank compensation and confirming that aggregated error is strictly non-additive.
9	\cite{unicomp-2026} evaluate compound compression across 40+ benchmarks, revealing that reasoning and multilingual capabilities degrade disproportionately relative to factual recall.
10	The order of compression stages is itself consequential: \cite{compression-ordering-2025} show that early quantization causes irreversible information loss, making P$\to$KD$\to$Q strictly preferable.
11	At a more fundamental level, \cite{phase-transition-compression-2026} characterize independent phase transition points per compression dimension, implying that the joint safe region is the intersection---not the union---of per-dimension safe zones.
12	On the structural side, GRASPrune~\cite{graspune-acl2026} learns global budget-constrained gates to jointly prune FFN channels and attention heads, but treats the pruning decision as static across generation.
13	These works establish that compound interaction produces non-additive errors, but share an implicit assumption: the interaction magnitude is either constant across the generation process or varies only by task---not by reasoning phase or eviction strategy.
14	How compound severity shifts across reasoning phases within a single generation remains unexamined.
15	
16	\subsection{KV Cache Eviction}
17	
18	Most eviction methods rely on importance scoring, yet accumulating evidence questions its reliability.
19	Ada-KV
…[truncated 3821 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-14T09:53:45.726630+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/background.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/background.tex"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-14T09:53:45.726900+00:00_

1	% Section 3: Background and Problem Setup
2	% Note: eq:ii and eq:gradient are the canonical definitions.
3	% Methodology.tex should reference these via \eqref rather than redefining.
4	
5	\section{Background and Problem Setup}
6	\label{sec:background}
7	
8	We formalize compound sparsity as the simultaneous application of attention head pruning and KV cache eviction, define the Interaction Index to quantify their non-additive coupling, and introduce phase segmentation to localize the analysis across reasoning stages.
9	
10	\subsection{Compound Sparsity Formulation}
11	\label{sec:compound-sparsity}
12	
13	Consider a Transformer language model with $L$ layers, each containing $H$ attention heads.
14	Let $s \in (0,1)$ denote a unified sparsity budget applied to both compression axes.
15	
16	\paragraph{Attention head pruning.}
17	For each layer $\ell$, heads are ranked by Frobenius norm importance $w_j^{(\ell)} = \|\mathbf{A}_j^{(\ell)}\|_F$, where $\mathbf{A}_j^{(\ell)} \in \mathbb{R}^{T \times T}$ is the attention matrix for head $j$ \cite{voita2019heads, michel2019sixteen}.
18	A binary mask $m_j^{(\ell)} \in \{0,1\}$ retains the top-$(1{-}s)\cdot H$ heads, zeroing the output of pruned heads:
19	\begin{equation}
20	    \tilde{\mathbf{o}}_j^{(\ell)} = m_j^{(\ell)} \cdot \mathbf{o}_j^{(\ell)}.
21	    \label{eq:head-mask}
22	\end{equation}
23	
24	\paragraph{KV cache eviction.}
25	For a sequence of length $T$, a position mask $\mathbf{m}_k \in \{0,1\}^T$ retains the top-$(1{-}s)\cdot T$ positions, with the BOS token always preserved.
26	Evicted positions are blocked via attention masking:
27	\begin{equation}
28	    \tilde{a}_{ij} = a_{ij} \cdot m_{k,j}, \quad \forall\, i, j.
29	    \label{eq:kv-mask}
30	\end{equation}
31	We compare two strategies for constructing $\mathbf{m}_k$:
32	\begin{itemize}[nosep,leftmargin=*]
33	    \item \textbf{Importance-based:} Each position $j$ is scored by its cumulative attention mass with position normalization:
34	    \begin{equation}
35
…[truncated 6466 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-14T09:53:45.727135+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/methodology.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/methodology.tex"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-14T09:53:45.727395+00:00_

1	\section{Experimental Setup}
2	\label{sec:experimental-setup}
3	
4	\subsection{Models}
5	\label{sec:models}
6	
7	We conduct experiments on two 7B-parameter instruction-tuned models that share the Qwen2 backbone architecture (28 Transformer layers, 28 attention heads with 4-group GQA):
8	
9	\paragraph{DeepSeek-R1-Distill-Qwen-7B} serves as our primary evaluation target. This model was distilled from DeepSeek-R1 \cite{deepseek-r1} and produces explicit chain-of-thought traces delimited by \texttt{&lt;think>}$\cdots$\texttt{&lt;/think>} tags, yielding sequences with pronounced phase structure---extended reasoning followed by a concise solution. The structured generation pattern makes it well-suited for studying how sparsity interacts with distinct reasoning phases.
10	
11	\paragraph{Qwen2.5-7B-Instruct} \cite{qwen2.5} provides a cross-model replication. Although it shares the same backbone family, its instruction tuning does not enforce explicit reasoning delimiters, producing a different distribution of attention sparsity across the generation trajectory. Replication on this model tests whether our findings generalize beyond distillation-induced phase structure.
12	
13	Both models are loaded in \texttt{bfloat16} precision with eager attention (i.e., without FlashAttention) to permit direct manipulation of attention weight matrices during sparsity intervention.\footnote{An earlier \texttt{float16} configuration produced sporadic NaN values in Layer~27 of DeepSeek-R1-Distill-Qwen-7B, affecting ${\sim}$8\% of logit positions. Switching to \texttt{bfloat16} eliminated all NaN occurrences; we additionally apply NaN-guarded filtering as a safety net.}
14	
15	
16	\subsection{Dataset}
17	\label{sec:dataset}
18	
19	We evaluate on a 50-problem stratified subset of the MATH-500 benchmark \cite{math500}, sampling uniformly across problem categories (algebra, geometry, number theory, combinatorics, etc.) with a fixed seed for reproducibility. Mathematical reasoning tasks are a natural
…[truncated 6792 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-14T09:53:45.727634+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/analysis.tex"
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-14T09:53:45.727916+00:00_

1	
2	\section{Analysis: Mechanisms of Phase-Modulated Severity}
3	\label{sec:analysis}
4	
5	The results in \S\ref{sec:results} reveal a striking asymmetry: importance-based eviction exhibits $69$--$274{\times}$ severity amplification in low-sparsity phases (Table~\ref{tab:main-results}), while random eviction remains flat at ${\sim}1{\times}$ across all phases. % exp_id: bf16_importance_s015..s030; G=69,103,222,274
6	Why is compound severity phase-modulated for one strategy but not the other? We identify two mechanisms. \emph{Discrimination collapse}---a systematic reduction in the discriminative power of KV importance scores under head pruning---is the primary mechanism, robustly observed across both models and all tested conditions. A secondary \emph{entropy redistribution} pattern is consistent for DeepSeek but only partially replicates on Qwen, indicating model-dependent modulation.
7	
8	\subsection{Discrimination Collapse Under Head Pruning}
9	\label{sec:discrimination-collapse}
10	
11	The KV importance score (Eq.~\ref{eq:kv-importance}) aggregates attention mass across surviving heads. When head pruning reduces the number of contributing heads, the cumulative importance distribution becomes more uniform: the gap between highly-attended and rarely-attended positions shrinks. We quantify this effect through two complementary metrics applied to the per-position importance distribution.
12	
13	The \textbf{Gini coefficient} measures inequality in the importance distribution ($\mathrm{Gini}{=}0$: perfectly uniform; $\mathrm{Gini}{=}1$: maximally concentrated). The \textbf{coefficient of variation} (CV) captures relative dispersion. A decrease in either metric after pruning indicates reduced discriminative power.
14	
15	We observe discrimination collapse across both models in all tested conditions (Table~\ref{tab:discrimination-metrics}). Under importance-based eviction, the Gini delta is negative at every sparsity level for both DeepSeek ($-0.030$ to $-0.081$) and Q
…[truncated 7720 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-14T09:53:45.728129+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/results.tex"
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-14T09:53:45.728491+00:00_

1	
2	\section{Results}
3	\label{sec:results}
4	
5	We present our empirical findings in five parts: strategy-dependent compound severity (\S\ref{sec:strategy-severity}), phase-modulated amplification (\S\ref{sec:phase-amplification}), the phase-strategy crossover (\S\ref{sec:crossover}), cross-model replication (\S\ref{sec:cross-model}), and statistical validation (\S\ref{sec:stat-validation}).
6	
7	
8	\subsection{Experimental Overview}
9	\label{sec:exp-overview}
10	
11	We evaluate compound sparsity on DeepSeek-R1-Distill-Qwen-7B using a 50-problem stratified subset of MATH-500 (\S\ref{sec:dataset}). For each problem, we measure perplexity under four conditions---dense, attention-only pruning, KV-only eviction, and compound (both)---at sparsity levels $s \in \{0.15, 0.20, 0.25, 0.30\}$. We compare importance-based and random eviction strategies (\S\ref{sec:sparsity-config}), and segment each generated sequence into high-, mid-, and low-sparsity reasoning phases via quantile-based attention sparsity partitioning (\S\ref{sec:phase-seg}). The interaction index (II, Eq.~\ref{eq:ii}) quantifies compound super-additivity, and the severity gradient ($G$, Eq.~\ref{eq:gradient}) captures phase-dependent amplification.
12	Models are evaluated in \texttt{bfloat16} precision (\S\ref{sec:experimental-setup}). Full experimental details appear therein.
13	
14	
15	\subsection{Strategy-Dependent Severity (C1)}
16	\label{sec:strategy-severity}
17	
18	The compound severity difference reveals a stark dependence on eviction strategy. Table~\ref{tab:aggregate-ii} reports the median compound severity difference $\Delta = \widetilde{\mathrm{II}}_{\textit{low}} - \widetilde{\mathrm{II}}_{\textit{high}}$ across 50 problems for each strategy and sparsity level. Under importance-based eviction, compound sparsity produces substantial super-additive degradation that grows with sparsity: $\Delta$ increases from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$, a $37{\times}$ amplification. Under rand
…[truncated 19756 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-14T09:53:45.728763+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/discussion.tex"
  }
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-14T09:53:45.729068+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{On the predictability of phase-modulated severity.}
5	One might argue that the qualitative direction of our findings is intuitive: in low-sparsity phases, attention distributes broadly across many tokens, so importance scores carry less discriminative signal, and importance-based eviction should degrade.
6	We do not dispute this intuition.
7	The surprise lies in the quantitative structure of the interaction, which is not predictable from first principles alone.
8	
9	First, the \emph{magnitude} of the severity gradient---$69$--$274{\times}$ amplification across sparsity levels (Table~\ref{tab:main-results})---far exceeds what a naive ``less discriminative $\Rightarrow$ somewhat worse'' argument would predict. % exp_id: bf16_importance_s015..s030; source: experiment_summary_table.json; G=low/high=69,103,222,274.
10	A reviewer expecting a $2$--$3\times$ effect would find two-orders-of-magnitude amplification difficult to anticipate without measurement.
11	Second, the gradient is \emph{phase-specific}: compound interaction concentrates in low-sparsity phases while high-sparsity phases exhibit near-zero compound interaction ($\widetilde{\mathrm{II}}_{\text{high}} < 0.06$ at $s \leq 0.30$; at $s = 0.35$, high-phase II rises to 0.105, indicating the onset of compound interaction even in high-sparsity phases at extreme pruning rates). % exp_id: bf16_importance_s015..s030; high-phase medians: 0.006, 0.015, 0.032, 0.053
12	This asymmetry means that importance-based eviction is not uniformly fragile---it is selectively fragile in a phase-dependent manner.
13	Third, and most strikingly, a \emph{crossover} emerges: at $s{=}0.25$, importance-based eviction \emph{outperforms} random eviction in high-sparsity phases (median severity $0.032$ vs.\ $0.818$) yet \emph{underperforms} in low-sparsity phases ($7.196$ vs.\ $1.363$---a ${>}5{\times}$ severity inflation relative to random). % exp_id: bf16_importance_s025, bf16_d
…[truncated 13783 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-14T09:53:45.729293+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/conclusion.tex"
  }
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-14T09:53:45.729532+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We presented an empirical investigation of how compound sparsity severity---the super-additive interaction between attention head pruning and KV cache eviction---varies across reasoning phases and eviction strategies in 7B-parameter language models. Our central finding is that compound severity is not a fixed property of the sparsity level but an emergent phase-strategy interaction whose magnitude spans over an order of magnitude within a single generation.
5	
6	Our contributions, mapped to confirmed claims, are:
7	\begin{enumerate}[nosep,leftmargin=*]
8	    \item \textbf{Strategy dependence (C1).} Compound severity depends qualitatively on the eviction strategy: importance-based eviction produces phase-modulated interaction (median phase difference $0.39$--$14.59$), while random eviction shows no significant phase modulation in 7/8 conditions (the sole exception---Qwen $s{=}0.30$, $p{=}0.012$, $d{=}{-}0.04$---has negligible effect size).
9	
10	    \item \textbf{Phase modulation (C2).} Under importance-based eviction, the median Interaction Index difference between low- and high-sparsity phases increases monotonically with sparsity (Bonferroni-corrected $p < 0.005$ at all four levels), with paired effect sizes growing from $d{=}0.44$ (small) to $d{=}0.80$ (large).
11	
12	    \item \textbf{Phase-strategy crossover (C3).} At $s{=}0.25$, importance-based eviction simultaneously outperforms random in high-sparsity phases ($\widetilde{\mathrm{II}} = 0.032$ vs.\ $0.818$) and underperforms in low-sparsity phases ($\widetilde{\mathrm{II}} = 7.196$ vs.\ $1.363$)---a qualitative reversal in strategy ranking.
13	
14	    \item \textbf{Sub-exponential growth (C6).} The severity gradient grows with sparsity but at a decelerating rate, suggesting a natural ceiling on phase-dependent amplification.
15	
16	    \item \textbf{Cross-model replication (C5).} The monotonic gradient replicates on Qwen2.5-7B-Instruct at $s \geq 0.20$ ($d
…[truncated 2073 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-14T09:53:45.729753+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/abstract.tex"
  }
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-14T09:53:45.729949+00:00_

1	\begin{abstract}
2	Compound sparsity---simultaneously pruning attention heads and evicting KV cache entries---is essential for efficient LLM inference but produces super-additive quality degradation whose structure is poorly understood.
3	Prior work treats compound interaction magnitude as approximately constant across the generation process.
4	We show that this assumption is wrong: compound sparsity severity is an emergent phase-strategy interaction that varies by over an order of magnitude across reasoning phases.
5	
6	We evaluate compound sparsity on DeepSeek-R1-Distill-Qwen-7B and Qwen2.5-7B-Instruct (both Qwen2 architecture, 7B parameters) using 50 MATH-500 problems, measuring the Interaction Index---a super-additivity metric---across quantile-segmented reasoning phases at sparsity levels $s \in \{0.15, 0.20, 0.25, 0.30\}$.
7	Under importance-based KV cache eviction, the median Interaction Index difference between low-sparsity and high-sparsity reasoning phases increases monotonically from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$, with Cohen's $d$ growing from $0.44$ (small) to $0.80$ (large); Bonferroni-corrected permutation tests yield $p < 0.005$ at all four sparsity levels.
8	Random eviction produces no significant phase modulation in 7/8 conditions; the single exception (Qwen $s{=}0.30$, $p{=}0.012$) shows negligible effect size ($d{=}{-}0.04$), confirming that the severity gradient is strategy-specific, not an inherent property of compound sparsity.
9	At $s{=}0.25$, a crossover emerges: importance-based eviction outperforms random in high-sparsity phases ($\widetilde{\mathrm{II}} = 0.032$ vs.\ $0.818$) yet underperforms in low-sparsity phases ($\widetilde{\mathrm{II}} = 7.196$ vs.\ $1.363$)---a qualitative reversal in strategy ranking.
10	The pattern replicates on Qwen2.5-7B-Instruct at $s \geq 0.20$ (Cohen's $d \geq 0.55$; Spearman $\rho = 1.0$ across sparsity levels; gradient permutation $p = 0.043$).
11	
12	We propose entropy-discrimination coll
…[truncated 412 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 67 · 2026-05-14T09:53:45.730150+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.bib",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper"
  }
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-14T09:53:45.730315+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-14T09:53:45.730584+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-14T09:53:45.730785+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 71 · 2026-05-14T09:53:45.731021+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "SnapKV efficient KV cache compression NeurIPS 2024 paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "WebSearch",
  "tool_args": {
    "query": "SnapKV efficient KV cache compression NeurIPS 2024 paper"
  }
}
```

</details>

---

### Tool call

_source line 72 · 2026-05-14T09:53:45.731205+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Ada-KV adaptive KV cache budget allocation NeurIPS 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Ada-KV adaptive KV cache budget allocation NeurIPS 2025"
  }
}
```

</details>

---

### Tool call

_source line 73 · 2026-05-14T09:53:45.731380+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "H2O Heavy-Hitter Oracle KV cache eviction 2024 paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "WebSearch",
  "tool_args": {
    "query": "H2O Heavy-Hitter Oracle KV cache eviction 2024 paper"
  }
}
```

</details>

---

### Tool call

_source line 74 · 2026-05-14T09:53:45.731574+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "PyramidKV KV cache compression 2024 paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "WebSearch",
  "tool_args": {
    "query": "PyramidKV KV cache compression 2024 paper"
  }
}
```

</details>

---

### Tool call

_source line 75 · 2026-05-14T09:53:45.731744+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "NaCl proxy token eviction random eviction attention bias ACL 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "WebSearch",
  "tool_args": {
    "query": "NaCl proxy token eviction random eviction attention bias ACL 2024"
  }
}
```

</details>

---

### Tool call

_source line 76 · 2026-05-14T09:53:45.731905+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "MATH-500 benchmark dataset paper citation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "WebSearch",
  "tool_args": {
    "query": "MATH-500 benchmark dataset paper citation"
  }
}
```

</details>

---

### Tool result

_source line 77 · 2026-05-14T09:53:45.732072+00:00_

Web search results for query: "SnapKV efficient KV cache compression NeurIPS 2024 paper"

Links: [{"title":"SnapKV: LLM Knows What You Are Looking for before Generation Yuhong Li1∗","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/28ab418242603e0f7323e54185d19bde-Paper-Conference.pdf"},{"title":"SnapKV: LLM Knows What You are Looking for Before Generation | OpenReview","url":"https://openreview.net/forum?id=poE54GOq2l"},{"title":"NeurIPS Poster SnapKV: LLM Knows What You are Looking for Before Generation","url":"https://neurips.cc/virtual/2024/poster/93531"},{"title":"SnapKV: LLM Knows What You are Looking for Before Generation [Quick Review]","url":"https://liner.com/review/snapkv-llm-knows-what-you-are-looking-for-before-generation"},{"title":"Paper page - SnapKV: LLM Knows What You are Looking for Before Generation","url":"https://huggingface.co/papers/2404.14469"},{"title":"SnapKV : LLM Knows What You are Looking for Before Generation","url":"https://arxiv.org/html/2404.14469v1"},{"title":"GitHub - FFY0/AdaKV: The Official Implementation of Ada-KV [NeurIPS 2025] · GitHub","url":"https://github.com/FFY0/AdaKV"},{"title":"NeurIPS Poster ChunkKV: Semantic-Preserving KV Cache Compression for Efficient Long-Context LLM Inference","url":"https://neurips.cc/virtual/2025/poster/120181"},{"title":"NeurIPS A Simple and Effective L2 Norm-Based Strategy for KV Cache Compression","url":"https://neurips.cc/virtual/2024/106481"},{"title":"SnapKV: LLM Knows What You are Looking for Before Generation Yuhong Li1∗","url":"https://arxiv.org/pdf/2404.14469"}]

I found comprehensive information about SnapKV. Here's what I found:

## SnapKV: LLM Knows What You are Looking for Before Generation

SnapKV is an innovative and fine-tuning-free approach that efficiently minimizes KV cache size while still delivering comparable performance in real-world applications.

### Key Insight
The paper discovers that each attention head in the model consistently focuses on specific p
…[truncated 976 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 78 · 2026-05-14T09:53:45.732274+00:00_

Web search results for query: "PyramidKV KV cache compression 2024 paper"

Links: [{"title":"[2406.02069] PyramidKV: Dynamic KV Cache Compression based on Pyramidal Information Funneling","url":"https://arxiv.org/abs/2406.02069"},{"title":"PyramidKV: Dynamic KV Cache Compression based on Pyramidal Information Funneling | OpenReview","url":"https://openreview.net/forum?id=jZVNmDiU86"},{"title":"PyramidInfer: Pyramid KV Cache Compression for High-throughput LLM Inference - ACL Anthology","url":"https://aclanthology.org/2024.findings-acl.195/"},{"title":"GitHub - Zefan-Cai/KVCache-Factory: Unified KV Cache Compression Methods for Auto-Regressive Models · GitHub","url":"https://github.com/Zefan-Cai/KVCache-Factory"},{"title":"Pyramid KV Cache Compression for High-throughput LLM ...","url":"https://aclanthology.org/2024.findings-acl.195.pdf"},{"title":"PyramidKV","url":"https://zefan-cai.github.io/PyramidKV.github.io/"},{"title":"[2406.02069v3] PyramidKV: Dynamic KV Cache Compression based on Pyramidal Information Funneling","url":"https://arxiv.org/abs/2406.02069v3"},{"title":"PyramidKV: Dynamic KV Cache Compression based on Pyramidal Information Funneling","url":"https://arxiv.org/html/2406.02069v1"},{"title":"GitHub - October2001/Awesome-KV-Cache-Compression: 📰 Must-read papers on KV Cache Compression (constantly updating 🤗).","url":"https://github.com/October2001/Awesome-KV-Cache-Compression"},{"title":"[2406.02069v1] PyramidKV: Dynamic KV Cache Compression based on Pyramidal Information Funneling","url":"https://arxiv.org/abs/2406.02069v1"}]

I found comprehensive information about the PyramidKV KV cache compression paper from 2024. Here are the key details:

## Paper Overview

PyramidKV: Dynamic KV Cache Compression based on Pyramidal Information Funneling was submitted on June 4, 2024, and was submitted to ICLR 2025.

## Core Concept

The paper reveals that LLMs aggregate information through Pyramidal Information Funneling where attention is scattering widely in l
…[truncated 1214 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 79 · 2026-05-14T09:53:45.732497+00:00_

Web search results for query: "MATH-500 benchmark dataset paper citation"

Links: [{"title":"HuggingFaceH4/MATH-500 · Datasets at Hugging Face","url":"https://huggingface.co/datasets/HuggingFaceH4/MATH-500"},{"title":"MATH-500 Benchmark Leaderboard | Artificial Analysis","url":"https://artificialanalysis.ai/evaluations/math-500"},{"title":"\\method: Optimizing Mathematical Reasoning through Stepwise Binary Feedback","url":"https://arxiv.org/html/2501.10799v1"},{"title":"Measuring Mathematical Problem Solving With the MATH Dataset Dan Hendrycks","url":"https://datasets-benchmarks-proceedings.neurips.cc/paper/2021/file/be83ab3ecd0db773eb2dc1b0a17836a1-Paper-round2.pdf"},{"title":"GitHub - hendrycks/math: The MATH Dataset (NeurIPS 2021) · GitHub","url":"https://github.com/hendrycks/math"},{"title":"MATH-500 Leaderboard","url":"https://llm-stats.com/benchmarks/math-500"},{"title":"HARDMATH: A Benchmark Dataset for Challenging Problems in Applied Mathematics","url":"https://openreview.net/pdf?id=gt6prlTEGL"},{"title":"Math500 Dataset","url":"https://paperswithcode.com/dataset/math500-1"},{"title":"MATH 500 Benchmark","url":"https://www.vals.ai/benchmarks/math500-03-11-2025"},{"title":"MATH-500 Leaderboard | Kaggle","url":"https://www.kaggle.com/benchmarks/open-benchmarks/math-500"}]

Based on the search results, here's the paper citation information for the MATH-500 benchmark dataset:

## Citation

The original MATH dataset paper is "Measuring Mathematical Problem Solving With the MATH Dataset" by Dan Hendrycks, Collin Burns, Saurav Kadavath, Akul Arora, Steven Basart, Eric Tang, Dawn Song, and Jacob Steinhardt, published in NeurIPS 2021.

### BibTeX Format:
```
@article{hendrycksmath2021,
  title={Measuring Mathematical Problem Solving With the MATH Dataset},
  author={Dan Hendrycks and Collin Burns and Saurav Kadavath and Akul Arora and Steven Basart and Eric Tang and Dawn Song and Jacob Steinhardt},
  journal={NeurIPS},
  year={2021}
}
```

The MATH-500 is a 500-probl
…[truncated 311 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 80 · 2026-05-14T09:53:45.732700+00:00_

Web search results for query: "H2O Heavy-Hitter Oracle KV cache eviction 2024 paper"

Links: [{"title":"[2306.14048] H$_2$O: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models","url":"https://arxiv.org/abs/2306.14048"},{"title":"H2O: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models | OpenReview","url":"https://openreview.net/forum?id=RkRrPp7GKO"},{"title":"H2O: Heavy-Hitter Oracle for Efficient Generative Inference ...","url":"https://proceedings.neurips.cc/paper_files/paper/2023/file/6ceefa7b15572587b78ecfcebb2827f8-Paper-Conference.pdf"},{"title":"Paper page - H_2O: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models","url":"https://huggingface.co/papers/2306.14048"},{"title":"H2O: Heavy-Hitter Oracle for Efficient Generative Inference ...","url":"https://github.com/vllm-project/vllm/issues/3532"},{"title":"H 2 O: heavy-hitter oracle for efficient generative inference ...","url":"https://dl.acm.org/doi/abs/10.5555/3666122.3667628"},{"title":"Q-Hitter: A Better Token Oracle for Efficient LLM Inference ...","url":"https://proceedings.mlsys.org/paper_files/paper/2024/file/bbb7506579431a85861a05fff048d3e1-Paper-Conference.pdf"},{"title":"\"H\"₂⁢\"O\": Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models","url":"https://arxiv.org/html/2306.14048v3"},{"title":"[PDF] H2O: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/H2O:-Heavy-Hitter-Oracle-for-Efficient-Generative-Zhang-Sheng/e586a4591ba0303b769f2c07cbddaf1899cb72e4"},{"title":"NACL: A General and Effective KV Cache Eviction ...","url":"https://aclanthology.org/2024.acl-long.428.pdf"}]

I found comprehensive information about the H2O Heavy-Hitter Oracle paper. Here's what I found:

## Overview

H₂O: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models is a research paper that addres
…[truncated 1059 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 81 · 2026-05-14T09:53:45.732878+00:00_

Web search results for query: "Ada-KV adaptive KV cache budget allocation NeurIPS 2025"

Links: [{"title":"GitHub - FFY0/AdaKV: The Official Implementation of Ada-KV [NeurIPS 2025] · GitHub","url":"https://github.com/FFY0/AdaKV"},{"title":"Ada-KV: Optimizing KV Cache Eviction by Adaptive Budget ...","url":"https://arxiv.org/pdf/2407.11550"},{"title":"NeurIPS Poster Ada-KV: Optimizing KV Cache Eviction by Adaptive Budget Allocation for Efficient LLM Inference","url":"https://neurips.cc/virtual/2025/poster/115578"},{"title":"[2407.11550] Ada-KV: Optimizing KV Cache Eviction by Adaptive Budget Allocation for Efficient LLM Inference","url":"https://arxiv.org/abs/2407.11550"},{"title":"Ada-KV: Optimizing KV Cache Eviction by Adaptive Budget Allocation for Efficient LLM Inference | OpenReview","url":"https://openreview.net/forum?id=tcisuhGsQZ"},{"title":"Ada-KV: Optimizing KV Cache Eviction by Adaptive Budget Allocation for Efficient LLM Inference - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv240711550F/abstract"},{"title":"AdaKV/README.md at main · FFY0/AdaKV","url":"https://github.com/FFY0/AdaKV/blob/main/README.md"},{"title":"[2407.11550v5] Ada-KV: Optimizing KV Cache Eviction by Adaptive Budget Allocation for Efficient LLM Inference","url":"https://arxiv.org/abs/2407.11550v5"},{"title":"FFY0 (Yuan Feng) · GitHub","url":"https://github.com/FFY0"},{"title":"Ada-KV: Optimizing KV Cache Eviction by Adaptive Budget Allocation for Efficient LLM Inference","url":"https://arxiv.org/html/2407.11550v3"}]

I found comprehensive information about Ada-KV. Here are the search results:

## Ada-KV Overview

Ada-KV has been accepted at NeurIPS 2025. It is the first head-wise adaptive budget allocation strategy that offers plug-and-play benefits, enabling seamless integration with prior cache eviction methods.

## Problem and Solution

Large Language Models face efficiency challenges due to the growing Key-Value (KV) cache required for long-sequence inference. Recent efforts
…[truncated 1112 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 82 · 2026-05-14T09:53:45.733056+00:00_

Web search results for query: "NaCl proxy token eviction random eviction attention bias ACL 2024"

Links: [{"title":"NACL: A General and Effective KV Cache Eviction Framework for LLM at Inference Time - ACL Anthology","url":"https://aclanthology.org/2024.acl-long.428/"},{"title":"NACL: A General and Effective KV Cache Eviction ...","url":"https://aclanthology.org/2024.acl-long.428.pdf"},{"title":"NaCl: A General and Effective KV Cache Eviction Framework for LLMs at Inference Time","url":"https://arxiv.org/html/2408.03675v2"},{"title":"NACL: A General and Effective KV Cache Eviction Framework for LLMs","url":"https://arxiv.org/pdf/2408.03675"},{"title":"[2408.03675] NACL: A General and Effective KV Cache Eviction Framework for LLMs at Inference Time","url":"https://arxiv.org/abs/2408.03675"},{"title":"Paper page - NACL: A General and Effective KV Cache Eviction Framework for LLMs at Inference Time","url":"https://huggingface.co/papers/2408.03675"},{"title":"Research/NLP/ACL2024-NACL at master · PaddlePaddle/Research","url":"https://github.com/PaddlePaddle/Research/tree/master/NLP/ACL2024-NACL"},{"title":"NACL: A Robust KV Cache Eviction Framework for Efficient Long-Text Processing in LLMs - MarkTechPost","url":"https://www.marktechpost.com/2024/08/12/nacl-a-robust-kv-cache-eviction-framework-for-efficient-long-text-processing-in-llms/"},{"title":"[Quick Review] NACL: A General and Effective KV Cache Eviction Framework for LLM at Inference Time","url":"https://liner.com/review/nacl-general-and-effective-kv-cache-eviction-framework-for-llm"},{"title":"NACL: A General and Effective KV Cache Eviction ...","url":"https://www.emergentmind.com/papers/2408.03675"}]

Based on the search results, here's an overview of the research on NaCl:

## NaCl: A General and Effective KV Cache Eviction Framework for LLMs

NaCl is a general framework for long-context KV cache eviction that achieves more optimal and efficient eviction in a single operation during the encoding phase.

### Ke
…[truncated 1459 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 83 · 2026-05-14T09:53:45.733239+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "SPark compound sparsity channel pruning token eviction AAAI 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "WebSearch",
  "tool_args": {
    "query": "SPark compound sparsity channel pruning token eviction AAAI 2026"
  }
}
```

</details>

---

### Tool call

_source line 84 · 2026-05-14T09:53:45.733365+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "SLIM compound error quantization sparsity saliency ICML 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "WebSearch",
  "tool_args": {
    "query": "SLIM compound error quantization sparsity saliency ICML 2025"
  }
}
```

</details>

---

### Tool call

_source line 85 · 2026-05-14T09:53:45.733528+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ThinKV phase-aware KV cache reasoning ICLR 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ThinKV phase-aware KV cache reasoning ICLR 2026"
  }
}
```

</details>

---

### Tool call

_source line 86 · 2026-05-14T09:53:45.733649+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "DefensiveKV defensive aggregation KV cache importance ICLR 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "WebSearch",
  "tool_args": {
    "query": "DefensiveKV defensive aggregation KV cache importance ICLR 2026"
  }
}
```

</details>

---

### Tool call

_source line 87 · 2026-05-14T09:53:45.733764+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "UniComp unified compound compression LLM benchmark 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "WebSearch",
  "tool_args": {
    "query": "UniComp unified compound compression LLM benchmark 2026"
  }
}
```

</details>

---

### Tool call

_source line 88 · 2026-05-14T09:53:45.733873+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "GRASPrune global budget constrained gates prune FFN attention ACL 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "WebSearch",
  "tool_args": {
    "query": "GRASPrune global budget constrained gates prune FFN attention ACL 2026"
  }
}
```

</details>

---

### Tool result

_source line 89 · 2026-05-14T09:53:45.734021+00:00_

Web search results for query: "SPark compound sparsity channel pruning token eviction AAAI 2026"

Links: [{"title":"SPARK: Query-Aware Unstructured Sparsity with","url":"https://arxiv.org/pdf/2508.15212"},{"title":"SparK: Query-Aware Unstructured Sparsity with Recoverable KV Cache Channel Pruning — ROCm Blogs","url":"https://rocm.blogs.amd.com/artificial-intelligence/spark-blog/README.html"},{"title":"GitHub - Xnhyacinth/SparK: [AAAI 2026] SparK: Query-Aware Unstructured Sparsity with Recoverable KV Cache Channel Pruning","url":"https://github.com/Xnhyacinth/SparK"},{"title":"SparK: Query-Aware Unstructured Sparsity with Recoverable KV Cache Channel Pruning","url":"https://arxiv.org/html/2508.15212"},{"title":"[2508.15212] SparK: Query-Aware Unstructured Sparsity with Recoverable KV Cache Channel Pruning","url":"https://arxiv.org/abs/2508.15212"},{"title":"GitHub - ZLKong/Awesome-Collection-Token-Reduction: A collection of token reduction (token pruning, merging, clustering, etc.) techniques for ML/AI · GitHub","url":"https://github.com/ZLKong/Awesome-Collection-Token-Reduction"},{"title":"Sparse-dLLM: Accelerating Diffusion LLMs with Dynamic Cache Eviction | Proceedings of the AAAI Conference on Artificial Intelligence","url":"https://ojs.aaai.org/index.php/AAAI/article/view/40586"},{"title":"Token Pruning","url":"https://www.aussieai.com/research/token-pruning"},{"title":"sparsity-in-deep-learning/index.html at master · spcl/sparsity-in-deep-learning","url":"https://github.com/spcl/sparsity-in-deep-learning/blob/master/index.html"},{"title":"ToaSt: Token Channel Selection and Structured Pruning for Efficient ViT","url":"https://arxiv.org/pdf/2602.15720"}]

Based on the search results, I found relevant information about SparK, which appears to be the paper matching your query:

## SparK: Query-Aware Unstructured Sparsity with Recoverable KV Cache Channel Pruning

This work has been accepted to AAAI 2026.

### Overview

Long-context inference in large language model
…[truncated 1453 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 90 · 2026-05-14T09:53:45.734201+00:00_

Web search results for query: "SLIM compound error quantization sparsity saliency ICML 2025"

Links: [{"title":"ICML Poster SLiM: One-shot Quantization and Sparsity with Low-rank Approximation for LLM Weight Compression","url":"https://icml.cc/virtual/2025/poster/46479"},{"title":"SLIM: One-shot Quantization and Sparsity with Low-rank Approximation for LLM Weight Compression | Research","url":"https://research.nvidia.com/publication/2025-06_slim-one-shot-quantization-and-sparsity-low-rank-approximation-llm-weight"},{"title":"ICML Poster SliM-LLM: Salience-Driven Mixed-Precision Quantization for Large Language Models","url":"https://icml.cc/virtual/2025/poster/45388"},{"title":"SLiM: One-shot Quantization and Sparsity with Low-rank Approximation for LLM Weight Compression","url":"https://arxiv.org/html/2410.09615"},{"title":"SliM-LLM: Salience-Driven Mixed-Precision Quantization for Large Language Models | OpenReview","url":"https://openreview.net/forum?id=PO9bBEPNWy"},{"title":"GitHub - Paramathic/slim: SLiM: One-shot Quantized Sparse Plus Low-rank Approximation of LLMs (ICML 2025) · GitHub","url":"https://github.com/Paramathic/slim"},{"title":"SLiM: One-shot Quantized Sparse Plus Low-rank Approximation of LLMs | OpenReview","url":"https://openreview.net/forum?id=Usa4pF1e5I"},{"title":"SLiM: One-shot Quantization and Sparsity with Low-rank Approximation for LLM Weight Compression | OpenReview","url":"https://openreview.net/forum?id=4UfRP8MopP"},{"title":"SLiM: One-shot Quantization and Sparsity with Low-rank ...","url":"https://arxiv.org/pdf/2410.09615"},{"title":"SLiM: One-shot Quantization and Sparsity","url":"https://icml.cc/media/icml-2025/Slides/46479.pdf"}]

Based on the search results, here's information about SLIM presented at ICML 2025:

## SLIM: One-shot Quantization and Sparsity with Low-rank Approximation

SLIM is a new one-shot compression framework that holistically integrates hardware-friendly quantization, sparsity, and low-rank approximation into a 
…[truncated 1317 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 91 · 2026-05-14T09:53:45.734382+00:00_

Web search results for query: "UniComp unified compound compression LLM benchmark 2026"

Links: [{"title":"[2602.09130] UniComp: A Unified Evaluation of Large Language Model Compression via Pruning, Quantization and Distillation","url":"https://arxiv.org/abs/2602.09130"},{"title":"UniComp: A Unified Evaluation of Large Language Model Compression via Pruning, Quantization, and Distillation","url":"https://arxiv.org/html/2602.09130"},{"title":"GitHub - TimeMarker-LLM/UniComp: [CVPR 2026] Official repository for \"UniComp: Rethinking Video Compression Through Informational Uniqueness\" · GitHub","url":"https://github.com/TimeMarker-LLM/UniComp"},{"title":"UniComp: Rethinking Video Compression Through Informational Uniqueness","url":"https://arxiv.org/html/2512.03575"},{"title":"[2602.09130v2] UniComp: A Unified Evaluation of Large Language Model Compression via Pruning, Quantization and Distillation","url":"https://arxiv.org/abs/2602.09130v2"},{"title":"UNICOMP: A Unified Evaluation of Large Language Model Compression","url":"https://arxiv.org/pdf/2602.09130"},{"title":"(PDF) UniComp: A Unified Evaluation of Large Language Model Compression via Pruning, Quantization and Distillation","url":"https://www.researchgate.net/publication/400660606_UniComp_A_Unified_Evaluation_of_Large_Language_Model_Compression_via_Pruning_Quantization_and_Distillation"},{"title":"LLM Benchmarks 2026 - Compare AI Benchmarks and Tests","url":"https://llm-stats.com/benchmarks"},{"title":"Best LLM for Coding in 2026: Ranked by Real Benchmarks | WhatLLM.org","url":"https://whatllm.org/best-llm-for-coding"},{"title":"LLM Leaderboard 2026 — Compare Top AI Models - Vellum","url":"https://www.vellum.ai/llm-leaderboard"}]

Based on the search results, I found relevant information about UniComp in the context of LLM compression benchmarking:

## UniComp: A Unified Evaluation of Large Language Model Compression

UniComp is a unified evaluation framework for comparing pruning, quantization, and knowledge
…[truncated 1319 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 92 · 2026-05-14T09:53:45.734588+00:00_

Web search results for query: "ThinKV phase-aware KV cache reasoning ICLR 2026"

Links: [{"title":"ThinKV: Thought-Adaptive KV Cache Compression for Efficient Reasoning Models | OpenReview","url":"https://openreview.net/forum?id=M3CeHnZKNC"},{"title":"ICLR Oral ThinKV: Thought-Adaptive KV Cache Compression for Efficient Reasoning Models","url":"https://iclr.cc/virtual/2026/oral/10009981"},{"title":"ThinKV: Thought-Adaptive KV Cache Compression for Efficient Reasoning Models","url":"https://arxiv.org/html/2510.01290v1"},{"title":"Utilizing KV Cache for Sampling and Reasoning","url":"https://arxiv.org/pdf/2601.20326"},{"title":"[2510.01290] ThinKV: Thought-Adaptive KV Cache Compression for Efficient Reasoning Models","url":"https://arxiv.org/abs/2510.01290"},{"title":"Published as a conference paper at ICLR 2026 KV CACHE TRANSFORM CODING","url":"https://openreview.net/pdf/1cef9774f0f0cf7bb9e4b167882e3ad3ef8cde16.pdf"},{"title":"KV Cache as a Reasoning Primitive for Long Context Reasoning | OpenReview","url":"https://openreview.net/forum?id=vs2qwVfU2C"},{"title":"Which Heads Matter for Reasoning? RL-Guided KV Cache Compression | OpenReview","url":"https://openreview.net/forum?id=HGdg76iVo6"},{"title":"PM-KVQ: Progressive Mixed-precision KV Cache Quantization for Long-CoT LLMs | OpenReview","url":"https://openreview.net/forum?id=Vem6FQvRvq"},{"title":"Top 10 KV Cache Compression Techniques for LLM Inference: Reducing Memory Overhead Across Eviction, Quantization, and Low-Rank Methods - MarkTechPost","url":"https://www.marktechpost.com/2026/04/29/top-10-kv-cache-compression-techniques-for-llm-inference-reducing-memory-overhead-across-eviction-quantization-and-low-rank-methods/"}]

Based on the search results, I found detailed information about ThinKV:

## ThinKV: Thought-Adaptive KV Cache Compression

ThinKV is a thought-adaptive KV cache compression framework that addresses the memory challenges of large reasoning models. The long-output context generation of large reas
…[truncated 1169 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 93 · 2026-05-14T09:53:45.734768+00:00_

Web search results for query: "DefensiveKV defensive aggregation KV cache importance ICLR 2026"

Links: [{"title":"GitHub - FFY0/DefensiveKV: Official Implementation for [ICLR26] DefensiveKV: Taming the Fragility of KV Cache Eviction in LLM Inference · GitHub","url":"https://github.com/FFY0/DefensiveKV"},{"title":"DEFENSIVEKV: TAMING THE FRAGILITY OF KV CACHE ...","url":"https://openreview.net/pdf?id=nJgS06sX3O"},{"title":"DefensiveKV: Taming the Fragility of KV Cache Eviction in LLM Inference | OpenReview","url":"https://openreview.net/forum?id=nJgS06sX3O"},{"title":"Taming the Fragility of KV Cache Eviction in LLM Inference","url":"https://arxiv.org/html/2510.13334"},{"title":"TAMING THE FRAGILITY OF KV CACHE EVICTION","url":"https://openreview.net/pdf/2d8c7805c4fcdb477dd04f7b60dd05bd9551c246.pdf"},{"title":"Expected Attention: KV Cache Compression by Estimating Attention From Future Queries Distribution | OpenReview","url":"https://openreview.net/forum?id=VmojW15eRc"},{"title":"ICLR Poster Mixing Importance with Diversity: Joint Optimization for KV Cache Compression in Large Vision-Language Models","url":"https://iclr.cc/virtual/2026/poster/10010980"},{"title":"Mitigating the Echo Chamber Effect in KV Cache Compression via Coverage Optimization | OpenReview","url":"https://openreview.net/forum?id=W6aYwEA7i3"},{"title":"Published as a conference paper at ICLR 2026 ADAPTIVE KV-CACHE COMPRESSION","url":"https://www.arxiv.org/pdf/2509.03136"},{"title":"CAKE: Cascading and Adaptive KV Cache Eviction with Layer Preferences | OpenReview","url":"https://openreview.net/forum?id=EQgEMAD4kv"}]

I found detailed information about DefensiveKV. Here's what the research shows:

## Overview

DefensiveKV addresses the memory and runtime overhead of transformer Key-Value caches in large language models by employing a scoring-aggregation framework to evict unimportant cache entries based on the "stability assumption"—that a fixed subset of entries remains consistently important dur
…[truncated 1511 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 94 · 2026-05-14T09:53:45.734947+00:00_

Web search results for query: "GRASPrune global budget constrained gates prune FFN attention ACL 2026"

Links: [{"title":"GitHub - ZiY-Wang/GRASPrune: Official implementation of GRASPrune, ACL 2026 Main: global gating for budgeted structured pruning of LLMs. · GitHub","url":"https://github.com/ZiY-Wang/GRASPrune"},{"title":"GRASPrune: Global Gating for Budgeted Structured Pruning of Large Language Models","url":"https://arxiv.org/html/2604.19398"},{"title":"[2604.19398] GRASPrune: Global Gating for Budgeted Structured Pruning of Large Language Models","url":"https://arxiv.org/abs/2604.19398"},{"title":"LLM-Pruner: On the Structural Pruning of Large Language Models | Request PDF","url":"https://www.researchgate.net/publication/401447462_LLM-Pruner_On_the_Structural_Pruning_of_Large_Language_Models"},{"title":"CFSP: An Efficient Structured Pruning Framework for LLMs ...","url":"https://aclanthology.org/2025.coling-main.626.pdf"},{"title":"A Survey on Deep Neural Network Pruning","url":"https://www.computer.org/csdl/journal/tp/2024/12/10643325/1ZAxlmvgXzG"},{"title":"Structured Pruning for Efficient Generative Pre-trained ...","url":"https://aclanthology.org/2023.findings-acl.692.pdf"},{"title":"Budget 2026: Crises Management - AICD","url":"https://www.aicd.com.au/economic-news/world/outlook/federal-budget-2026-crises-management.html"},{"title":"Budgeted Broadcast: An Activity-Dependent Pruning Rule for Neural Network Efficiency","url":"https://arxiv.org/html/2510.01263v1"},{"title":"GitHub - JarvisPei/CMoE: [ACL 2026 Main] Analytical FFN-to-MoE Restructuring via Activation Pattern Analysis · GitHub","url":"https://github.com/JarvisPei/CMoE"}]

Based on the search results, here's what I found about GRASPrune:

## GRASPrune Overview

GRASPrune is a post-training structured pruning toolkit for decoder-only LLMs. It's the official implementation of a paper accepted to ACL 2026 Main on global gating for budgeted structured pruning of LLMs.

## How It Works

GRASPrune is a 
…[truncated 1333 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 95 · 2026-05-14T09:53:45.735181+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "MuSTAFar per-token magnitude pruning KV sparsity NeurIPS 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "WebSearch",
  "tool_args": {
    "query": "MuSTAFar per-token magnitude pruning KV sparsity NeurIPS 2025"
  }
}
```

</details>

---

### Tool call

_source line 96 · 2026-05-14T09:53:45.735354+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "OBCache optimal brain damage KV saliency score key value pruning 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "WebSearch",
  "tool_args": {
    "query": "OBCache optimal brain damage KV saliency score key value pruning 2025"
  }
}
```

</details>

---

### Tool call

_source line 97 · 2026-05-14T09:53:45.735536+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "RetentiveKV deferred importance token salience KV cache 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "WebSearch",
  "tool_args": {
    "query": "RetentiveKV deferred importance token salience KV cache 2026"
  }
}
```

</details>

---

### Tool call

_source line 98 · 2026-05-14T09:53:45.735673+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"greedy bias\" KV cache importance metric 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"greedy bias\" KV cache importance metric 2026"
  }
}
```

</details>

---

### Tool call

_source line 99 · 2026-05-14T09:53:45.735815+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "page-level eviction block-wise KV cache prefill decode EACL 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "WebSearch",
  "tool_args": {
    "query": "page-level eviction block-wise KV cache prefill decode EACL 2026"
  }
}
```

</details>

---

### Tool call

_source line 100 · 2026-05-14T09:53:45.735946+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"doing more with less\" unstructured pruning test-time scaling 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"doing more with less\" unstructured pruning test-time scaling 2026"
  }
}
```

</details>

---

### Tool result

_source line 101 · 2026-05-14T09:53:45.736098+00:00_

Web search results for query: "MuSTAFar per-token magnitude pruning KV sparsity NeurIPS 2025"

Links: [{"title":"NeurIPS Poster MUSTAFAR: Promoting Unstructured Sparsity for KV Cache Pruning in LLM Inference","url":"https://neurips.cc/virtual/2025/loc/san-diego/poster/119320"},{"title":"MUSTAFAR: Promoting Unstructured Sparsity for KV Cache Pruning in LLM Inference","url":"https://openreview.net/pdf?id=C69741fMFX"},{"title":"[2505.22913] Mustafar: Promoting Unstructured Sparsity for KV Cache Pruning in LLM Inference","url":"https://arxiv.org/abs/2505.22913"},{"title":"MUSTAFAR: Promoting Unstructured Sparsity for KV Cache Pruning in LLM Inference","url":"https://arxiv.org/html/2505.22913v1"},{"title":"GitHub - dhjoo98/mustafar: codebase for MUSTAFAR:Promoting Unstructured Sparsity for KV Pruning in LLM Inference","url":"https://github.com/dhjoo98/mustafar"},{"title":"[PDF] Mustafar: Promoting Unstructured Sparsity for KV Cache Pruning in LLM Inference | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Mustafar:-Promoting-Unstructured-Sparsity-for-KV-in-Joo-Hosseini/643c287adfaccc9d5c06496c9711beb96b2b4d3c"},{"title":"Mustafar: Promoting Unstructured Sparsity for KV Cache Pruning ...","url":"https://neurips.cc/media/neurips-2025/Slides/119320.pdf"},{"title":"Paper page - Mustafar: Promoting Unstructured Sparsity for KV Cache Pruning in LLM Inference","url":"https://huggingface.co/papers/2505.22913"},{"title":"(PDF) Mustafar: Promoting Unstructured Sparsity for KV Cache Pruning in LLM Inference","url":"https://www.researchgate.net/publication/392204576_Mustafar_Promoting_Unstructured_Sparsity_for_KV_Cache_Pruning_in_LLM_Inference"},{"title":"[Literature Review] Mustafar: Promoting Unstructured Sparsity for KV Cache Pruning in LLM Inference","url":"https://www.themoonlight.io/en/review/mustafar-promoting-unstructured-sparsity-for-kv-cache-pruning-in-llm-inference"}]

I found relevant information about MUSTAFAR. Here's a summary of the search results:

## 
…[truncated 1401 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 102 · 2026-05-14T09:53:45.736270+00:00_

Web search results for query: "OBCache optimal brain damage KV saliency score key value pruning 2025"

Links: [{"title":"[2510.07651] OBCache: Optimal Brain KV Cache Pruning for Efficient Long-Context LLM Inference","url":"https://arxiv.org/abs/2510.07651"},{"title":"OBCache: Optimal Brain KV Cache Pruning for Efficient Long-Context LLM Inference","url":"https://arxiv.org/html/2510.07651"},{"title":"OBCache: Optimal Brain KV Cache Pruning for Efficient Long-Context LLM Inference | OpenReview","url":"https://openreview.net/forum?id=JLfky7RakB"},{"title":"OBCACHE: OPTIMAL BRAIN KV CACHE PRUNING","url":"https://openreview.net/pdf/0d93ba99551baa503e09d14f51a1fde9c899638f.pdf"},{"title":"KV Cache Pruning in Transformers","url":"https://www.emergentmind.com/topics/kv-cache-pruning"},{"title":"Leveraging KV Similarity for Online Structured Pruning in LLMs","url":"https://www.arxiv.org/pdf/2512.07090"},{"title":"Optimal Brain Compression: A Framework for Accurate ...","url":"https://openreview.net/pdf?spm=a2c6h.13046898.publish-article.15.65286ffaa2V6mQ&id=ksVGCOlOEba"},{"title":"(PDF) Optimal Brain Damage","url":"https://www.researchgate.net/publication/221618539_Optimal_Brain_Damage"},{"title":"GitHub - NVIDIA/kvpress: LLM KV cache compression made easy · GitHub","url":"https://github.com/NVIDIA/kvpress"},{"title":"Optimal Brain Compression: A Framework for Accurate Post-Training Quantization and Pruning | Request PDF","url":"https://www.researchgate.net/publication/401461533_Optimal_Brain_Compression_A_Framework_for_Accurate_Post-Training_Quantization_and_Pruning"}]

Based on the search results, I found comprehensive information about OBCache and its approach to KV cache pruning:

## OBCache Overview

OBCache (Optimal Brain Cache) is a principled framework that formulates cache eviction as a layer-wise structured pruning problem.

## Saliency Score and KV Pruning

Building upon the Optimal Brain Damage (OBD) theory, OBCache quantifies token saliency by measuring the pert
…[truncated 1115 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 103 · 2026-05-14T09:53:45.736466+00:00_

Web search results for query: ""doing more with less" unstructured pruning test-time scaling 2026"

Links: [{"title":"Doing More With Less: Revisiting the Effectiveness of LLM Pruning for Test-Time Scaling","url":"https://arxiv.org/html/2604.25098"},{"title":"[2604.25098] Doing More With Less: Revisiting the Effectiveness of LLM Pruning for Test-Time Scaling","url":"https://arxiv.org/abs/2604.25098"}]

I found the research paper! "Doing More With Less: Revisiting the Effectiveness of LLM Pruning for Test-Time Scaling" is a recent paper from arXiv (posted April 28, 2026).

The paper's key findings are:

The authors conducted extensive experiments across four reasoning benchmarks on two reasoning LLMs: s1.1-7B and Qwen3-8B, and found that unstructured pruning augments TTS performance compared to structured pruning, and can even outperform the unpruned full-weight LLMs.

While prior work showed that structured pruning (methods which remove entire layer blocks) significantly degrades test-time scaling reasoning performance, this work investigates whether unstructured pruning (methods that carefully remove only certain redundant/detrimental weights) exhibits similar limitations.

These findings challenge the conventional notion that pruning always reduces TTS performance and suggest that carefully undertaken pruning can improve TTS effectiveness even further. The paper also empirically studies the impact of different layer-wise sparsity allocation strategies for unstructured pruning methods.

The research was conducted at the University of South Florida and appears to be a significant contribution to understanding how pruning techniques interact with test-time scaling in large language models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 104 · 2026-05-14T09:53:45.736699+00:00_

Web search results for query: "RetentiveKV deferred importance token salience KV cache 2026"

Links: [{"title":"RetentiveKV: State-Space Memory for Uncertainty-Aware Multimodal KV Cache Eviction","url":"https://arxiv.org/html/2605.04075"},{"title":"[2605.04075] RetentiveKV: State-Space Memory for Uncertainty-Aware Multimodal KV Cache Eviction","url":"https://arxiv.org/abs/2605.04075"},{"title":"Past- and Future-Informed KV Cache Policy with Salience Estimation in Autoregressive Video Diffusion","url":"https://arxiv.org/html/2601.21896"},{"title":"[2601.21896] Past- and Future-Informed KV Cache Policy with Salience Estimation in Autoregressive Video Diffusion","url":"https://arxiv.org/abs/2601.21896"},{"title":"[2512.03324] Cache What Lasts: Token Retention for Memory-Bounded KV Cache in LLMs","url":"https://arxiv.org/abs/2512.03324"},{"title":"Cache What Lasts: Token Retention for Memory-Bounded KV Cache in LLMs","url":"https://arxiv.org/html/2512.03324v1"},{"title":"Cache What Lasts: Token Retention for Memory-Bounded KV Cache in LLMs | OpenReview","url":"https://openreview.net/forum?id=qCaq3jGb0S"},{"title":"LookaheadKV: Fast and Accurate KV Cache Eviction by ...","url":"https://arxiv.org/pdf/2603.10899"},{"title":"[2601.14279] On the Limits of Learned Importance Scoring for KV Cache Compression","url":"https://arxiv.org/abs/2601.14279"},{"title":"PaFu-KV: Past & Future-Informed Cache Policy","url":"https://www.emergentmind.com/topics/past-and-future-informed-kv-cache-policy-pafu-kv"}]

Based on the web search results, I found relevant information about RetentiveKV and related KV cache optimization techniques. Here's what I found:

## RetentiveKV

RetentiveKV is a method for multimodal large language models that addresses challenges in computational efficiency and memory consumption due to visual KV cache expansion when processing long visual contexts.

### Key Problem: Deferred Importance

Visual tokens display "deferred importance," initially exhibiting low sali
…[truncated 1339 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 105 · 2026-05-14T09:53:45.736897+00:00_

Web search results for query: ""greedy bias" KV cache importance metric 2026"

Links: [{"title":"[2602.02199] More Than a Quick Glance: Overcoming the Greedy Bias in KV-Cache Compression","url":"https://arxiv.org/abs/2602.02199"},{"title":"More Than a Quick Glance: Overcoming the Greedy Bias in KV-Cache Compression","url":"https://arxiv.org/html/2602.02199v1"},{"title":"Top 10 KV Cache Compression Techniques for LLM Inference: Reducing Memory Overhead Across Eviction, Quantization, and Low-Rank Methods - MarkTechPost","url":"https://www.marktechpost.com/2026/04/29/top-10-kv-cache-compression-techniques-for-llm-inference-reducing-memory-overhead-across-eviction-quantization-and-low-rank-methods/"},{"title":"Expected Attention: KV Cache Compression by Estimating Attention From Future Queries Distribution | OpenReview","url":"https://openreview.net/forum?id=VmojW15eRc"},{"title":"KV Cache Optimization Strategies for Scalable and Efficient LLM Inference","url":"https://arxiv.org/html/2603.20397v1"},{"title":"Expected Attention: KV Cache Compression by Estimating Attention from Future Queries Distribution","url":"https://arxiv.org/html/2510.00636v1"},{"title":"Is 3-Bit KV Cache the Holy Grail? A Reality Check on Google’s TurboQuant | Towards AI","url":"https://towardsai.net/p/machine-learning/is-3-bit-kv-cache-the-holy-grail-a-reality-check-on-googles-turboquant"},{"title":"Cache What Lasts: Token Retention for Memory-Bounded KV Cache in LLMs","url":"https://arxiv.org/html/2512.03324v2"},{"title":"Expected Attention: KV Cache Compression by Estimating Attention","url":"https://arxiv.org/pdf/2510.00636"},{"title":"Is KV Cache Quantization Sabotaging Your Context? — We test the impact of quantizing caches on long-horizon agentic coding workloads.","url":"https://dasroot.net/posts/2026/05/kv-cache-quantization-agentic-coding-long-horizon/"}]

I've found relevant information about "greedy bias" in KV cache compression. Here are the key findings from the 2026 research:

## Ma
…[truncated 1453 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 106 · 2026-05-14T09:53:45.737075+00:00_

Web search results for query: "page-level eviction block-wise KV cache prefill decode EACL 2026"

Links: [{"title":"PagedEviction: Structured Block-wise KV Cache Pruning ...","url":"https://aclanthology.org/2026.findings-eacl.168.pdf"},{"title":"PagedEviction: Structured Block-wise KV Cache Pruning for Efficient Large Language Model Inference","url":"https://arxiv.org/html/2509.04377"},{"title":"PagedEviction: Structured Block-wise KV Cache Pruning ...","url":"https://arxiv.org/pdf/2509.04377"},{"title":"PagedEviction: Block-Aligned KV Cache Management","url":"https://www.emergentmind.com/topics/pagedeviction"},{"title":"EpiCache: Episodic KV Cache Management for Long ...","url":"https://arxiv.org/pdf/2509.17396"},{"title":"Published as a conference paper at ICLR 2026 KV CACHE TRANSFORM CODING","url":"https://openreview.net/pdf/1cef9774f0f0cf7bb9e4b167882e3ad3ef8cde16.pdf"},{"title":"Fast KVzip: Efficient and Accurate LLM Inference with Gated KV Eviction","url":"https://janghyun1230.github.io/paper/fastkvzip26.pdf"},{"title":"LMCACHE: AN EFFICIENT KV CACHE LAYER FOR ENTERPRISE-SCALE LLM INFERENCE","url":"https://lmcache.ai/tech_report.pdf"},{"title":"SABlock: Semantic-Aware KV Cache Eviction with Adaptive Compression Block Size","url":"https://arxiv.org/html/2510.22556v1"},{"title":"(PDF) PagedEviction: Structured Block-wise KV Cache Pruning for Efficient Large Language Model Inference","url":"https://www.researchgate.net/publication/395270805_PagedEviction_Structured_Block-wise_KV_Cache_Pruning_for_Efficient_Large_Language_Model_Inference"}]

Based on the search results, I found information about **PagedEviction**, a paper that matches your query about page-level eviction, block-wise KV cache, and prefill/decode operations. Here's what I found:

## PagedEviction: Structured Block-wise KV Cache Pruning

PagedEviction is a novel and structured KV cache pruning algorithm designed for vLLM's PagedAttention. The method adopts a coarse-grained eviction strategy wherein e
…[truncated 1044 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 107 · 2026-05-14T09:53:45.737258+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"compression ordering\" early quantization information loss pruning knowledge distillation 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"compression ordering\" early quantization information loss pruning knowledge distillation 2025"
  }
}
```

</details>

---

### Tool call

_source line 108 · 2026-05-14T09:53:45.737386+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"phase transition\" compression dimension LLM safe zone 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"phase transition\" compression dimension LLM safe zone 2026"
  }
}
```

</details>

---

### Tool call

_source line 109 · 2026-05-14T09:53:45.737571+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"decision representation transition\" layer pruning silent decisive phase 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"decision representation transition\" layer pruning silent decisive phase 2026"
  }
}
```

</details>

---

### Tool call

_source line 110 · 2026-05-14T09:53:45.737698+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "RaAS non-monotonic token importance decoding steps ACL 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "WebSearch",
  "tool_args": {
    "query": "RaAS non-monotonic token importance decoding steps ACL 2025"
  }
}
```

</details>

---

### Tool call

_source line 111 · 2026-05-14T09:53:45.737814+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"sparse frontier\" sparse attention strategy tasks generation stages 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"sparse frontier\" sparse attention strategy tasks generation stages 2025"
  }
}
```

</details>

---

### Tool call

_source line 112 · 2026-05-14T09:53:45.737927+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "DeepSeek-R1 reinforcement learning reasoning LLM paper 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "WebSearch",
  "tool_args": {
    "query": "DeepSeek-R1 reinforcement learning reasoning LLM paper 2025"
  }
}
```

</details>

---

### Tool result

_source line 113 · 2026-05-14T09:53:45.738070+00:00_

Web search results for query: "RaAS non-monotonic token importance decoding steps ACL 2025"

Links: [{"title":"Accepted Findings Papers - ACL 2025","url":"https://2025.aclweb.org/program/find_papers/"},{"title":"Non-Monotonic Plasticity in Large Language Models","url":"https://2025.ccneuro.org/abstract_pdf/Kolling_2025_Non-Monotonic_Plasticity_Large_Language_Models.pdf"},{"title":"Retrofitting Large Language Models with Dynamic ...","url":"https://aclanthology.org/2025.acl-long.1444.pdf"},{"title":"Turning Trash into Treasure: Accelerating Inference of ...","url":"https://aclanthology.org/2025.acl-long.338.pdf"},{"title":"TRIAL: Token Relations and Importance Aware Late-interaction for Accurate Text Retrieval - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-main.854/"},{"title":"TETRIS: Optimal Draft Token Selection for Batch ...","url":"https://aclanthology.org/2025.acl-long.1598.pdf"},{"title":"RASD: Retrieval-Augmented Speculative Decoding","url":"https://aclanthology.org/2025.findings-acl.320.pdf"},{"title":"ActionPiece: Contextually Tokenizing Action Sequences for ...","url":"https://arxiv.org/pdf/2502.13581"},{"title":"GitHub - iLearn-Lab/ACL26-EvoSparse: [ACL 2026 main] Official Implementation for Evolving Sparsity: Leveraging Token Importance Dynamics for Efficient LLM Decoding with Sparse Attention · GitHub","url":"https://github.com/iLearn-Lab/ACL26-EvoSparse"},{"title":"Beyond Decoder-only: Large Language Models Can be ...","url":"https://aclanthology.org/2025.findings-acl.490.pdf"}]

Based on the web search results, I found a relevant paper at ACL 2025:

**RaaS: Reasoning-Aware Attention Sparsity for Efficient LLM Inference with Long Decoding Chains** by Junhao Hu, Wenrui Huang, Weidong Wang, Zhenwen Li, and others, is an accepted Findings paper at ACL 2025.

This paper appears to address efficient LLM inference during decoding processes. While the search results don't provide detailed information about the specific mechanisms related to "non-
…[truncated 457 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 114 · 2026-05-14T09:53:45.738265+00:00_

Web search results for query: ""compression ordering" early quantization information loss pruning knowledge distillation 2025"

Links: [{"title":"A Systematic Study of Compression Ordering for Large Language Models","url":"https://arxiv.org/html/2511.19495"},{"title":"Frontiers | A survey of model compression techniques: past, present, and future","url":"https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2025.1518965/full"},{"title":"A review of state-of-the-art techniques for large language model compression | Complex & Intelligent Systems | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s40747-025-02019-z"},{"title":"Comparative analysis of model compression techniques for achieving carbon efficient AI | Scientific Reports","url":"https://www.nature.com/articles/s41598-025-07821-w"},{"title":"Prune-Quantize-Distill: An Ordered Pipeline for Efficient Neural Network Compression","url":"https://arxiv.org/html/2604.04988v1"},{"title":"Iterative knowledge distillation and pruning for model compression in unsupervised domain adaptation - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0031320325001724"},{"title":"A comprehensive review of model compression techniques in machine learning | Applied Intelligence | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10489-024-05747-w"},{"title":"Model Compression, Quantization & Distillation | by Akanksha Sinha | Medium","url":"https://medium.com/@akankshasinha247/model-compression-quantization-distillation-b5006cf41546"},{"title":"Model Compression Techniques: The Ultimate 2025 Guide","url":"https://createbytes.com/insights/model-compression-techniques-guide"},{"title":"A Survey on Model Compression for Large Language Models | Transactions of the Association for Computational Linguistics | MIT Press","url":"https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00704/125482/A-Survey-on-Model-Compression-for-Large-Language"}]


…[truncated 1840 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 115 · 2026-05-14T09:53:45.738542+00:00_

Web search results for query: ""phase transition" compression dimension LLM safe zone 2026"

Links: [{"title":"Phase transitions in large language model compression | npj Artificial Intelligence","url":"https://www.nature.com/articles/s44387-026-00072-8"},{"title":"GitHub - whucs21Mzy/Model-Phase-Transitions: Navigating Model Phase Transitions to Enable Extreme Lossless Compression: A Perspective","url":"https://github.com/whucs21Mzy/Model-Phase-Transitions"},{"title":"Understanding LLM Behaviors via Compression: Data","url":"https://openreview.net/pdf/95f61a66375ba3e46803c24b0ddc45e0df29334d.pdf"},{"title":"The Illusion of Power Capping in LLM Decode: A Phase-Aware Energy Characterisation Across Attention Architectures","url":"https://arxiv.org/html/2605.11999v1"},{"title":"Top 10 KV Cache Compression Techniques for LLM Inference: Reducing Memory Overhead Across Eviction, Quantization, and Low-Rank Methods - MarkTechPost","url":"https://www.marktechpost.com/2026/04/29/top-10-kv-cache-compression-techniques-for-llm-inference-reducing-memory-overhead-across-eviction-quantization-and-low-rank-methods/"},{"title":"GitHub - ModelTC/LightCompress: [EMNLP 2024 & AAAI 2026] A powerful toolkit for compressing large models including LLMs, VLMs, and video generative models. · GitHub","url":"https://github.com/ModelTC/LightCompress"},{"title":"Unweight: Lossless MLP Weight Compression for LLM Inference","url":"https://research.cloudflare.com/papers/unweight-2026.pdf"},{"title":"Google TurboQuant: 2026 LLM Compression Guide | Articles","url":"https://o-mega.ai/articles/google-turboquant-the-2026-llm-compression-guide"},{"title":"Paper Review - “Experience Compression” and Safe Operation of LLM Agents | Rick-Brick","url":"https://oct-rick-brick.com/en/articles/2026-04-27-paper-review-2026-04-27/"},{"title":"Densing law of LLMs | Nature Machine Intelligence","url":"https://www.nature.com/articles/s42256-025-01137-0"}]

Based on the search results, I found highly relevant research
…[truncated 1602 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 116 · 2026-05-14T09:53:45.738750+00:00_

Web search results for query: ""decision representation transition" layer pruning silent decisive phase 2026"

Links: [{"title":"Understanding Performance Collapse in Layer-Pruned Large Language Models via Decision Representation Transitions","url":"https://arxiv.org/html/2605.07271"},{"title":"A Survey on Deep Neural Network Pruning","url":"https://www.computer.org/csdl/journal/tp/2024/12/10643325/1ZAxlmvgXzG"},{"title":"An Introduction to Decision Diagrams for Optimization","url":"https://www.andrew.cmu.edu/user/vanhoeve/papers/DD_TutORial.pdf"},{"title":"A Fast Framework for Post-training Structured Pruning Without Retraining | OpenReview","url":"https://openreview.net/forum?id=KksPo0zXId"},{"title":"Decision Tree Pruning - an overview | ScienceDirect Topics","url":"https://www.sciencedirect.com/topics/computer-science/decision-tree-pruning"},{"title":"Decision Tree Pruning: The Hows and Whys - KDnuggets","url":"https://www.kdnuggets.com/2022/09/decision-tree-pruning-hows-whys.html"},{"title":"Neural network compression for reinforcement learning tasks | Scientific Reports","url":"https://www.nature.com/articles/s41598-025-93955-w"},{"title":"Pruning Decision Trees - GeeksforGeeks","url":"https://www.geeksforgeeks.org/machine-learning/pruning-decision-trees/"},{"title":"Comparative analysis of model compression techniques for achieving carbon efficient AI | Scientific Reports","url":"https://www.nature.com/articles/s41598-025-07821-w"},{"title":"Complex Decision Trees? How Pruning keeps the ML Tool organized » Lamarr-Blog","url":"https://lamarr-institute.org/blog/decision-trees-pruning/"}]

Based on the search results, I found highly relevant information about decision representation transition during layer pruning. Here are the key findings:

## Decision Representation Transitions in Layer Pruning

The research identifies two distinct phases as pruning rate increases: the Silent Phase and Decisive Phase. This framework helps explain why large language models exp
…[truncated 1248 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 117 · 2026-05-14T09:53:45.738930+00:00_

Web search results for query: ""sparse frontier" sparse attention strategy tasks generation stages 2025"

Links: [{"title":"The Sparse Frontier: Sparse Attention Trade-offs in Transformer LLMs","url":"https://arxiv.org/pdf/2504.17768"},{"title":"[2504.17768] The Sparse Frontier: Sparse Attention Trade-offs in Transformer LLMs","url":"https://arxiv.org/abs/2504.17768"},{"title":"Optimizing Native Sparse Attention with Latent Attention and Local Global Alternating Strategies","url":"https://arxiv.org/html/2511.00819v1"},{"title":"Track: Session 7: Quantization and Sparsity","url":"https://mlsys.org/virtual/2025/session/3153"},{"title":"Native Sparse Attention: Hardware-Aligned and Natively Trainable Sparse Attention","url":"https://arxiv.org/html/2502.11089v1"},{"title":"Sparse Attention","url":"https://www.aussieai.com/research/sparse-attention"},{"title":"Inference-Time Hyper-Scaling with KV Cache Compression","url":"https://arxiv.org/html/2506.05345v1"},{"title":"Sparse Attention Post-Training for Mechanistic Interpretability","url":"https://arxiv.org/html/2512.05865v1"},{"title":"Sparse Attention Variants Overview","url":"https://www.emergentmind.com/topics/sparse-attention-variants"},{"title":"Hardware-Aligned and Natively Trainable Sparse Attention","url":"https://aclanthology.org/2025.acl-long.1126.pdf"}]

Based on the search results, here's what I found about "Sparse Frontier" and sparse attention strategies:

## The Sparse Frontier: Overview

"The Sparse Frontier" is a research paper that addresses sparse attention's efficiency-accuracy trade-offs through the largest-scale empirical analysis to date of training-free sparse attention, evaluating six methods across multiple model families and sizes, sequences up to 128K tokens, and sparsity levels up to 0.95 on nine diverse tasks.

## Key Findings on Strategy Trade-offs

The research reveals several important insights about sparse attention strategies across different stages of LLM generation:

1. **Stage-Speci
…[truncated 1110 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 118 · 2026-05-14T09:53:45.739108+00:00_

Web search results for query: "DeepSeek-R1 reinforcement learning reasoning LLM paper 2025"

Links: [{"title":"[2501.12948] DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning","url":"https://arxiv.org/abs/2501.12948"},{"title":"DeepSeek-R1 incentivizes reasoning in LLMs through reinforcement learning | Nature","url":"https://www.nature.com/articles/s41586-025-09422-z"},{"title":"DeepSeek-R1 incentivizes reasoning in LLMs through reinforcement learning - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025Natur.645..633G/abstract"},{"title":"Paper page - DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning","url":"https://huggingface.co/papers/2501.12948"},{"title":"GitHub - deepseek-ai/DeepSeek-R1 · GitHub","url":"https://github.com/deepseek-ai/DeepSeek-R1"},{"title":"DeepSeek-R1 Paper Explained – A New RL LLMs Era in AI? - AI Papers Academy","url":"https://aipapersacademy.com/deepseek-r1/"},{"title":"DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning","url":"https://arxiv.org/html/2501.12948v1"},{"title":"(PDF) DeepSeek-R1 incentivizes reasoning in LLMs through reinforcement learning","url":"https://www.researchgate.net/publication/395582429_DeepSeek-R1_incentivizes_reasoning_in_LLMs_through_reinforcement_learning"},{"title":"DeepSeek-R1: Incentivizing reasoning capability in LLMs via reinforcement learning · Pablo Stafforini","url":"https://stafforini.com/works/deepseek-ai-2025-deepseek-r-1-incentivizing/"},{"title":"DeepSeek-R1 incentivizes reasoning in LLMs through reinforcement learning | Nature · HUMAN TECHNOLOGY eXCELLENCE","url":"https://ht-x.com/en/posts/2025/09/deepseek-r1-incentivizes-reasoning-in-llms-through/"}]

I've found comprehensive information about the DeepSeek-R1 paper. Here's what I found:

## Paper Overview

The paper is titled "DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning" and was first submitted on January 22, 202
…[truncated 1564 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 119 · 2026-05-14T09:53:45.739310+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Qwen2.5 technical report Yang et al 2024 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Qwen2.5 technical report Yang et al 2024 arXiv"
  }
}
```

</details>

---

### Tool call

_source line 120 · 2026-05-14T09:53:45.739465+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2511.19495 \"systematic study\" compression ordering LLM authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2511.19495 \"systematic study\" compression ordering LLM authors"
  }
}
```

</details>

---

### Tool call

_source line 121 · 2026-05-14T09:53:45.739612+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2605.07271 \"decision representation transitions\" layer pruning authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2605.07271 \"decision representation transitions\" layer pruning authors"
  }
}
```

</details>

---

### Tool call

_source line 122 · 2026-05-14T09:53:45.739806+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2504.17768 \"sparse frontier\" sparse attention trade-offs authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2504.17768 \"sparse frontier\" sparse attention trade-offs authors"
  }
}
```

</details>

---

### Tool call

_source line 123 · 2026-05-14T09:53:45.740002+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "RaaS reasoning-aware attention sparsity ACL 2025 findings arxiv authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "WebSearch",
  "tool_args": {
    "query": "RaaS reasoning-aware attention sparsity ACL 2025 findings arxiv authors"
  }
}
```

</details>

---

### Tool call

_source line 124 · 2026-05-14T09:53:45.740178+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"phase transitions\" LLM compression npj artificial intelligence 2026 authors model phase transition points"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"phase transitions\" LLM compression npj artificial intelligence 2026 authors model phase transition points"
  }
}
```

</details>

---

### Tool result

_source line 125 · 2026-05-14T09:53:45.740405+00:00_

Web search results for query: "arxiv 2605.07271 "decision representation transitions" layer pruning authors"

Links: [{"title":"[2605.07271] Understanding Performance Collapse in Layer-Pruned Large Language Models via Decision Representation Transitions","url":"https://arxiv.org/abs/2605.07271"},{"title":"Understanding Performance Collapse in Layer-Pruned Large Language Models via Decision Representation Transitions","url":"https://arxiv.org/html/2605.07271"},{"title":"[2405.17081] Effective Layer Pruning Through Similarity Metric Perspective","url":"https://arxiv.org/abs/2405.17081"},{"title":"Effective Layer Pruning Through Similarity Metric Perspective","url":"https://arxiv.org/html/2405.17081v1"},{"title":"Pruning Everything, Everywhere, All at Once","url":"https://arxiv.org/html/2506.04513"},{"title":"State Canonization and Early Pruning in Width-Based Automated Theorem Proving","url":"https://arxiv.org/html/2605.11025"},{"title":"Sharp feature-learning transitions and Bayes-optimal neural scaling laws in extensive-width networks","url":"https://arxiv.org/html/2605.10395"},{"title":"Automated Large-scale CVRP Solver Design via LLM-assisted Flexible MCTS","url":"https://arxiv.org/html/2605.03339"},{"title":"Layer Pruning with Consensus: A Triple-Win Solution","url":"https://arxiv.org/html/2411.14345v1"},{"title":"Prune-OPD: Efficient and Reliable On-Policy Distillation for Long-Horizon Reasoning","url":"https://arxiv.org/html/2605.07804v1"}]

Based on the search results, I found the paper you're looking for. Here are the details:

**Paper:** Understanding Performance Collapse in Layer-Pruned Large Language Models via Decision Representation Transitions (arXiv:2605.07271)

**Authors:** Boyu Shi, Chang Liu, ChuanBao Gao, Xu Yang, and Xin Geng

**Summary:** The paper studies layer pruning through decision representation, introducing two metrics called Decision Margin and Option Frequency, and an Iterative Pruning method to analyze layer-wise decision dynamics. The 
…[truncated 368 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 126 · 2026-05-14T09:53:45.740732+00:00_

Web search results for query: "Qwen2.5 technical report Yang et al 2024 arXiv"

Links: [{"title":"[2412.15115] Qwen2.5 Technical Report","url":"https://arxiv.org/abs/2412.15115"},{"title":"2025-01-06 Qwen2.5 Technical Report Qwen Team https://huggingface.co/Qwen","url":"https://arxiv.org/pdf/2412.15115"},{"title":"[PDF] Qwen2.5 Technical Report | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Qwen2.5-Technical-Report-Yang-Yang/88aa6b1f37d1fd8e0a40499ce9bb87873f03aaa8"},{"title":"2025-01-26 Qwen2.5-1M Technical Report","url":"https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen2.5-1M/Qwen2_5_1M_Technical_Report.pdf"},{"title":"2025-05-15 Qwen3 Technical Report Qwen Team https://huggingface.co/Qwen","url":"https://arxiv.org/pdf/2505.09388"},{"title":"2024-12-20 Qwen2.5 Technical Report Qwen Team https://huggingface.co/Qwen","url":"https://arxiv.org/pdf/2412.15115v1"},{"title":"[2409.12122] Qwen2.5-Math Technical Report: Toward Mathematical Expert Model via Self-Improvement","url":"https://arxiv.org/abs/2409.12122"},{"title":"[2409.12186] Qwen2.5-Coder Technical Report","url":"https://arxiv.org/abs/2409.12186"},{"title":"Qwen2.5-Coder Technical Report","url":"https://arxiv.org/html/2409.12186v3"},{"title":"Google Scholar","url":"https://scholar.google.com/scholar?q=A.+Yang+et+al.%2C+Qwen2.+5+technical+report.+arXiv+%5BPreprint%5D+%282024%29.+https%3A%2F%2Farxiv.org%2Fabs%2F2412.15115+%28Accessed+1+June+2024%29."}]

I found the Qwen2.5 Technical Report by Yang et al. 2024 on arXiv. Here are the key details:

**Paper Information:**
- Title: Qwen2.5 Technical Report
- Authors: An Yang, Baosong Yang, Beichen Zhang, Binyuan Hui, Bo Zheng, Bowen Yu, and 35+ additional authors
- arXiv ID: 2412.15115, with versions released December 19, 2024 and January 3, 2025

**Paper Overview:**
- The report introduces Qwen2.5, a comprehensive series of large language models (LLMs) designed to meet diverse needs
- Qwen2.5 has demonstrated top-tier performance on a wide range
…[truncated 695 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 127 · 2026-05-14T09:53:45.741004+00:00_

Web search results for query: "arxiv 2511.19495 "systematic study" compression ordering LLM authors"

Links: [{"title":"[2511.19495] A Systematic Study of Compression Ordering for Large Language Models","url":"https://arxiv.org/abs/2511.19495"},{"title":"A Systematic Study of Compression Ordering for Large Language Models","url":"https://arxiv.org/html/2511.19495"},{"title":"Computer Science Nov 2025","url":"https://arxiv.org/list/cs/2025-11?skip=9500&show=100"},{"title":"Exploiting the Experts: Unauthorized Compression in MoE-LLMs","url":"https://arxiv.org/html/2511.19480"},{"title":"A Comprehensive Survey of Compression Algorithms for Language Models","url":"https://arxiv.org/html/2401.15347v1"},{"title":"Understanding LLM Behaviors via Compression: Data Generation, Knowledge Acquisition and Scaling Laws","url":"https://arxiv.org/html/2504.09597v3"},{"title":"Ranking LLMs by compression","url":"https://arxiv.org/html/2406.14171v1"},{"title":"[2510.23632] LLMComp: A Language Modeling Paradigm for Error-Bounded Scientific Data Compression","url":"https://arxiv.org/abs/2510.23632"},{"title":"Entropy Law: The Story Behind Data Compression and LLM Performance","url":"https://arxiv.org/html/2407.06645v1"},{"title":"GitHub - HuangOwen/Awesome-LLM-Compression: Awesome LLM compression research papers and tools. · GitHub","url":"https://github.com/HuangOwen/Awesome-LLM-Compression"}]

Based on the search results, here's the information about arXiv paper 2511.19495:

## Paper Details

**Title:** A Systematic Study of Compression Ordering for Large Language Models

**Authors:** Shivansh Chhawri, Rahul Mahadik, Suparna Rooj

**Submission Date:** Submitted on 23 Nov 2025

## Overview

The paper addresses how Large Language Models require substantial computational resources, making model compression essential for efficient deployment in constrained environments. Among the dominant compression techniques—knowledge distillation, structured pruning, and low-bit quantization—their i
…[truncated 892 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 128 · 2026-05-14T09:53:45.741267+00:00_

Web search results for query: "arxiv 2504.17768 "sparse frontier" sparse attention trade-offs authors"

Links: [{"title":"[2504.17768] The Sparse Frontier: Sparse Attention Trade-offs in Transformer LLMs","url":"https://arxiv.org/abs/2504.17768"},{"title":"The Sparse Frontier: Sparse Attention Trade-offs in Transformer LLMs","url":"https://arxiv.org/pdf/2504.17768"},{"title":"[2504.17768v1] The Sparse Frontier: Sparse Attention Trade-offs in Transformer LLMs","url":"https://arxiv.org/abs/2504.17768v1"},{"title":"[PDF] The Sparse Frontier: Sparse Attention Trade-offs in Transformer LLMs | Semantic Scholar","url":"https://www.semanticscholar.org/paper/42ed331d09a32215c7061a56b3659fa4500675c1"},{"title":"Paper page - The Sparse Frontier: Sparse Attention Trade-offs in Transformer LLMs","url":"https://huggingface.co/papers/2504.17768"},{"title":"Detecting Contextual Hallucinations in Large Language Models with Frequency-Aware Attention","url":"https://arxiv.org/html/2602.18145v1"},{"title":"Inference-Time Hyper-Scaling with KV Cache Compression","url":"https://arxiv.org/html/2506.05345v1"},{"title":"Kinetics: Rethinking Test-Time Scaling Laws","url":"https://arxiv.org/html/2506.05333v1/"},{"title":"[Literature Review] The Sparse Frontier: Sparse Attention Trade-offs in Transformer LLMs","url":"https://www.themoonlight.io/en/review/the-sparse-frontier-sparse-attention-trade-offs-in-transformer-llms"},{"title":"LoLA: Low-Rank Linear Attention with Sparse Caching","url":"https://arxiv.org/html/2505.23666v2"}]

Based on the search results, I found comprehensive information about arxiv paper 2504.17768:

## Paper Details

**Title:** The Sparse Frontier: Sparse Attention Trade-offs in Transformer LLMs

**Authors:** Piotr Nawrot, Robert Li, Renjie Huang, Sebastian Ruder, Kelly Marchisio, Edoardo M. Ponti

## Overview

Sparse attention offers a promising strategy to extend long-context capabilities in Transformer LLMs, yet its efficiency-accuracy trade-offs remain unclear due t
…[truncated 1060 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 129 · 2026-05-14T09:53:45.741554+00:00_

Web search results for query: ""phase transitions" LLM compression npj artificial intelligence 2026 authors model phase transition points"

Links: [{"title":"Phase transitions in large language model compression | npj Artificial Intelligence","url":"https://www.nature.com/articles/s44387-026-00072-8"},{"title":"Phase transitions in large language model compression – DOAJ","url":"https://doaj.org/article/06b2d6b18f08424a9f7778c269597d3c"},{"title":"GitHub - whucs21Mzy/Model-Phase-Transitions: Navigating Model Phase Transitions to Enable Extreme Lossless Compression: A Perspective","url":"https://github.com/whucs21Mzy/Model-Phase-Transitions"},{"title":"A review of state-of-the-art techniques for large language model compression | Complex & Intelligent Systems | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s40747-025-02019-z"},{"title":"AI Model Compression: Key to Efficient LLM Deployment | StartupHub.ai","url":"https://startuphub.ai/ai-news/artificial-intelligence/2026/ai-model-compression-key-to-efficient-llm-deployment"},{"title":"Understanding LLM Behaviors via Compression: Data Generation,","url":"https://arxiv.org/pdf/2504.09597"},{"title":"Understanding LLM Behaviors via Compression: Data","url":"https://openreview.net/pdf/95f61a66375ba3e46803c24b0ddc45e0df29334d.pdf"},{"title":"Artificial Intelligence","url":"https://arxiv.org/list/cs.AI/recent"},{"title":"Lossless data compression by large models | Nature Machine Intelligence","url":"https://www.nature.com/articles/s42256-025-01033-7"},{"title":"Phase Transitions in the Output Distribution of Large Language Models","url":"https://arxiv.org/html/2405.17088v1"}]

I found the research paper you're looking for. Here are the key details about the publication:

## Paper Information

The paper "Phase transitions in large language model compression" published in npj Artificial Intelligence volume 2, Article number 21 (2026) argues that Large Language Models exhibit Model Phase Transitions: 
…[truncated 1152 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 130 · 2026-05-14T09:53:45.741837+00:00_

Web search results for query: "RaaS reasoning-aware attention sparsity ACL 2025 findings arxiv authors"

Links: [{"title":"[2502.11147] RaaS: Reasoning-Aware Attention Sparsity for Efficient LLM Reasoning","url":"https://arxiv.org/abs/2502.11147"},{"title":"RaaS: Reasoning-Aware Attention Sparsity for Efficient LLM Reasoning","url":"https://arxiv.org/html/2502.11147v2"},{"title":"RaaS: Reasoning-Aware Attention Sparsity for Efficient ...","url":"https://aclanthology.org/2025.findings-acl.131.pdf"},{"title":"ThinKV: Thought-Adaptive KV Cache Compression for Efficient Reasoning Models","url":"https://arxiv.org/html/2510.01290v1"},{"title":"Sparse Attention across Multiple-context KV Cache","url":"https://arxiv.org/html/2508.11661v1"},{"title":"Computer Science Feb 2025","url":"https://www.arxiv.org/list/cs/2025-02?skip=5575&show=25"},{"title":"Artificial Intelligence Feb 2025","url":"https://arxiv.org/list/cs.AI/2025-02?skip=2100&show=25"},{"title":"Accepted Findings Papers - ACL 2025","url":"https://2025.aclweb.org/program/find_papers/"},{"title":"Machine Learning Feb 2025","url":"https://www.arxiv.org/list/cs.LG/2025-02?skip=1375&show=50"},{"title":"Hardware-Aligned and Natively Trainable Sparse Attention","url":"https://aclanthology.org/2025.acl-long.1126.pdf"}]

Based on the search results, here are the key findings about the RaaS paper:

## Overview

RaaS: Reasoning-Aware Attention Sparsity for Efficient LLM Reasoning was accepted as a Findings paper at ACL 2025.

## Authors

The authors are: Junhao Hu, Wenrui Huang, Weidong Wang, Zhenwen Li, Tiancheng Hu, Zhixia Liu, Xusheng Chen, Tao Xie, and Yizhou Shan.

## Key Findings

The paper addresses the challenge that solving reasoning tasks often requires LLMs to generate long sequences with O(N) time and memory complexities per token, and existing sparsity-based algorithms propose retaining Key-Value (KV) vectors for only the most critical tokens.

The paper identifies two important attention patterns:

1. **Milesto
…[truncated 844 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 131 · 2026-05-14T09:53:45.742111+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2605.04075 RetentiveKV state-space memory multimodal KV cache authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2605.04075 RetentiveKV state-space memory multimodal KV cache authors"
  }
}
```

</details>

---

### Tool call

_source line 132 · 2026-05-14T09:53:45.742308+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2602.02199 \"more than a quick glance\" greedy bias KV cache authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2602.02199 \"more than a quick glance\" greedy bias KV cache authors"
  }
}
```

</details>

---

### Tool call

_source line 133 · 2026-05-14T09:53:45.742515+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2604.25098 \"doing more with less\" pruning test-time scaling authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2604.25098 \"doing more with less\" pruning test-time scaling authors"
  }
}
```

</details>

---

### Tool call

_source line 134 · 2026-05-14T09:53:45.742715+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2509.04377 PagedEviction block-wise KV cache pruning authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2509.04377 PagedEviction block-wise KV cache pruning authors"
  }
}
```

</details>

---

### Tool call

_source line 135 · 2026-05-14T09:53:45.742898+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2510.07651 OBCache optimal brain KV cache pruning authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2510.07651 OBCache optimal brain KV cache pruning authors"
  }
}
```

</details>

---

### Tool call

_source line 136 · 2026-05-14T09:53:45.743071+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2602.09130 UniComp unified evaluation LLM compression authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2602.09130 UniComp unified evaluation LLM compression authors"
  }
}
```

</details>

---

### Tool result

_source line 137 · 2026-05-14T09:53:45.743278+00:00_

Web search results for query: "arxiv 2605.04075 RetentiveKV state-space memory multimodal KV cache authors"

Links: [{"title":"[2605.04075] RetentiveKV: State-Space Memory for Uncertainty-Aware Multimodal KV Cache Eviction","url":"https://arxiv.org/abs/2605.04075"},{"title":"RetentiveKV: State-Space Memory for Uncertainty-Aware Multimodal KV Cache Eviction","url":"https://arxiv.org/html/2605.04075"},{"title":"Make Your LVLM KV Cache More Lightweight","url":"https://arxiv.org/html/2605.00789"},{"title":"Revisiting Multimodal KV Cache Compression: A Frequency-Domain-Guided Outlier-KV-Aware Approach","url":"https://arxiv.org/html/2511.16786"},{"title":"[2511.16786] Revisiting Multimodal KV Cache Compression: A Frequency-Domain-Guided Outlier-KV-Aware Approach","url":"https://arxiv.org/abs/2511.16786"},{"title":"KEEP: A KV-Cache-Centric Memory Management System for Efficient Embodied Planning","url":"https://arxiv.org/html/2602.23592v2"},{"title":"Hold Onto That Thought: Assessing KV Cache Compression On Reasoning","url":"https://arxiv.org/html/2512.12008v1"},{"title":"Predictive Multi-Tier Memory Management for KV Cache in Large-Scale GPU Inference","url":"https://arxiv.org/html/2604.26968"},{"title":"[2605.00789] Make Your LVLM KV Cache More Lightweight","url":"https://arxiv.org/abs/2605.00789"},{"title":"Cache What Lasts: Token Retention for Memory-Bounded KV Cache in LLMs","url":"https://arxiv.org/html/2512.03324v2"}]

Based on the search results, here is the information about arxiv paper 2605.04075:

**Title:** RetentiveKV: State-Space Memory for Uncertainty-Aware Multimodal KV Cache Eviction

**Authors:** Sihao Liu, YuFan Xiong, Zhonghua Jiang, Zhaode Wang, chengfei lv, and Shengyu Zhang

**Overview:** RetentiveKV is an entropy-driven KV cache optimization method that reformulates KV eviction from "discrete context truncation" to "continuous memory evolution" based on State Space Models.

**Key Problem Addressed:** Visual tokens display "deferred importance," init
…[truncated 395 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 138 · 2026-05-14T09:53:45.743537+00:00_

Web search results for query: "arxiv 2602.02199 "more than a quick glance" greedy bias KV cache authors"

Links: [{"title":"[2602.02199] More Than a Quick Glance: Overcoming the Greedy Bias in KV-Cache Compression","url":"https://arxiv.org/abs/2602.02199"},{"title":"More Than a Quick Glance: Overcoming the Greedy Bias in KV-Cache Compression","url":"https://arxiv.org/html/2602.02199"},{"title":"Fast KV Compaction via Attention Matching","url":"https://arxiv.org/html/2602.16284"},{"title":"Predicting Future Utility: Global Combinatorial Optimization for Task-Agnostic KV Cache Eviction","url":"https://arxiv.org/html/2602.08585v1"},{"title":"[2602.16284] Fast KV Compaction via Attention Matching","url":"https://arxiv.org/abs/2602.16284"},{"title":"KEEP: A KV-Cache-Centric Memory Management System for Efficient Embodied Planning","url":"https://arxiv.org/html/2602.23592"},{"title":"DeltaKV: Residual-Based KV Cache Compression via Long-Range Similarity","url":"https://arxiv.org/html/2602.08005"},{"title":"Preprint THE PITFALLS OF KV CACHE COMPRESSION","url":"https://arxiv.org/pdf/2510.00231"},{"title":"[2602.23200] InnerQ: Hardware-aware Tuning-free Quantization of KV Cache for Large Language Models","url":"https://arxiv.org/abs/2602.23200"},{"title":"[2602.22603] SideQuest: Model-Driven KV Cache Management for Long-Horizon Agentic Reasoning","url":"https://arxiv.org/abs/2602.22603"}]

Based on the search results, I found the paper you're looking for. Here are the key details:

**Paper:** "More Than a Quick Glance: Overcoming the Greedy Bias in KV-Cache Compression"

**Authors:** Aryan Sood and 2 other authors

**ArXiv ID:** 2602.02199

**Publication Date:** February 2, 2026

**Main Contribution:** The paper presents LASER-KV (Layer Accumulated Selection with Exact-LSH Recall), a framework designed to test the limits of KV compression under a strict accumulative budgeting policy. The findings challenge the prevailing assumption that attention scores alone are a sufficien
…[truncated 315 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 139 · 2026-05-14T09:53:45.743807+00:00_

Web search results for query: "arxiv 2604.25098 "doing more with less" pruning test-time scaling authors"

Links: [{"title":"[2604.25098] Doing More With Less: Revisiting the Effectiveness of LLM Pruning for Test-Time Scaling","url":"https://arxiv.org/abs/2604.25098"},{"title":"Doing More With Less: Revisiting the Effectiveness of LLM Pruning for Test-Time Scaling","url":"https://arxiv.org/html/2604.25098"},{"title":"LLMs Improving LLMs: Agentic Discovery for Test-Time Scaling","url":"https://arxiv.org/html/2605.08083"},{"title":"Stream-T1: Test-Time Scaling for Streaming Video Generation","url":"https://arxiv.org/html/2605.04461"},{"title":"Layer Pruning Harms Test-Time Scaling in LLMs","url":"https://arxiv.org/pdf/2510.22228"},{"title":"GitHub - ThreeSR/Awesome-Inference-Time-Scaling: Paper List of Inference/Test Time Scaling/Computing · GitHub","url":"https://github.com/ThreeSR/Awesome-Inference-Time-Scaling"},{"title":"TTSnap: Test-Time Scaling of Diffusion Models via Noise-Aware Pruning","url":"https://www.arxiv.org/pdf/2511.22242v2"},{"title":"Scaling up Test-Time Compute with Latent Reasoning: A Recurrent Depth Approach | OpenReview","url":"https://openreview.net/forum?id=D6o6Bwtq7h"},{"title":"Pruning Extensions and Efficiency Trade-Offs for Sustainable Time Series Classification","url":"https://arxiv.org/html/2604.07953"},{"title":"MemCoT: Test-Time Scaling through Memory-Driven Chain-of-Thought","url":"https://arxiv.org/html/2604.08216v1"}]

Based on the search results, I found the paper you're looking for:

**Title:** "Doing More With Less: Revisiting the Effectiveness of LLM Pruning for Test-Time Scaling"

**Authors:** Ocean Monjur, Shahriar Kabir Nahin, Anshuman Chhabra

**ArXiv ID:** 2604.25098

**Summary:** The paper investigates whether unstructured pruning (methods that carefully remove only certain redundant/detrimental weights) exhibits similar limitations as structured pruning, and their extensive experiments across four reasoning benchmarks on t
…[truncated 328 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 140 · 2026-05-14T09:53:45.744060+00:00_

Web search results for query: "arxiv 2509.04377 PagedEviction block-wise KV cache pruning authors"

Links: [{"title":"PagedEviction: Structured Block-wise KV Cache Pruning ...","url":"https://arxiv.org/pdf/2509.04377"},{"title":"[2509.04377] PagedEviction: Structured Block-wise KV Cache Pruning for Efficient Large Language Model Inference","url":"https://arxiv.org/abs/2509.04377"},{"title":"PagedEviction: Structured Block-wise KV Cache Pruning for Efficient Large Language Model Inference","url":"https://arxiv.org/html/2509.04377"},{"title":"(PDF) PagedEviction: Structured Block-wise KV Cache Pruning for Efficient Large Language Model Inference","url":"https://www.researchgate.net/publication/395270805_PagedEviction_Structured_Block-wise_KV_Cache_Pruning_for_Efficient_Large_Language_Model_Inference"},{"title":"PagedEviction: Structured Block-wise KV Cache Pruning ...","url":"https://aclanthology.org/2026.findings-eacl.168.pdf"},{"title":"KV Cache Pruning in Transformers","url":"https://www.emergentmind.com/topics/kv-cache-pruning"},{"title":"PagedEviction: Block-Aligned KV Cache Management","url":"https://www.emergentmind.com/topics/pagedeviction"},{"title":"Make Your LVLM KV Cache More Lightweight","url":"https://arxiv.org/html/2605.00789"},{"title":"EpiCache: Episodic KV Cache Management for Long Conversational Question Answering","url":"https://arxiv.org/html/2509.17396v1"},{"title":"Paper page - EpiCache: Episodic KV Cache Management for Long Conversational Question Answering","url":"https://huggingface.co/papers/2509.17396"}]

Based on the search results, the authors of arXiv paper 2509.04377 "PagedEviction: Structured Block-wise KV Cache Pruning for Efficient Large Language Model Inference" are Krishna Teja Chitty-Venkata, Jie Ye, Xian-He Sun, Anthony Kougkas, Murali Emani, Venkatram Vishwanath, and Bogdan Nicolae.

The paper proposes PagedEviction, a novel fine-grained, structured KV cache pruning strategy that enhances the memory efficiency of vLLM's PagedAtt
…[truncated 331 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 141 · 2026-05-14T09:53:45.744293+00:00_

Web search results for query: "arxiv 2510.07651 OBCache optimal brain KV cache pruning authors"

Links: [{"title":"[2510.07651] OBCache: Optimal Brain KV Cache Pruning for Efficient Long-Context LLM Inference","url":"https://arxiv.org/abs/2510.07651"},{"title":"OBCache: Optimal Brain KV Cache Pruning for Efficient Long-Context LLM Inference","url":"https://arxiv.org/html/2510.07651"},{"title":"OBCache: Optimal Brain KV Cache Pruning for Efficient Long-Context LLM Inference | OpenReview","url":"https://openreview.net/forum?id=JLfky7RakB"},{"title":"Make Your LVLM KV Cache More Lightweight","url":"https://arxiv.org/html/2605.00789"},{"title":"OBCACHE: OPTIMAL BRAIN KV CACHE PRUNING","url":"https://openreview.net/pdf/0d93ba99551baa503e09d14f51a1fde9c899638f.pdf"},{"title":"KV Cache Pruning in Transformers","url":"https://www.emergentmind.com/topics/kv-cache-pruning"},{"title":"Towards Threshold-Free KV Cache Pruning","url":"https://arxiv.org/html/2502.16886v3"},{"title":"LMCache: An Efficient KV Cache Layer for Enterprise","url":"https://www.facebook.com/james24plus1/photos/lmcache-an-efficient-kv-cache-layer-for-enterprise-scale-llm-inference-httpsarxi/1375993941221803/"},{"title":"[2510.25600] PureKV: Plug-and-Play KV Cache Optimization with Spatial-Temporal Sparse Attention for Vision-Language Large Models","url":"https://arxiv.org/abs/2510.25600"},{"title":"[2510.09665] LMCache: An Efficient KV Cache Layer for Enterprise-Scale LLM Inference","url":"https://arxiv.org/abs/2510.09665"}]

Based on the search results, I found information about the arxiv paper 2510.07651:

**Paper Title:** OBCache: Optimal Brain KV Cache Pruning for Efficient Long-Context LLM Inference

**Authors:** Yuzhe Gu, Xiyu Liang, Jiaojiao Zhao, Enmao Diao

**Submission Date:** October 9, 2025

**Summary:** OBCache proposes a principled framework that formulates cache eviction as a layer-wise structured pruning problem. Building upon the Optimal Brain Damage (OBD) theory, OBCache quantifies token 
…[truncated 284 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 142 · 2026-05-14T09:53:45.744579+00:00_

Web search results for query: "arxiv 2602.09130 UniComp unified evaluation LLM compression authors"

Links: [{"title":"[2602.09130] UniComp: A Unified Evaluation of Large Language Model Compression via Pruning, Quantization and Distillation","url":"https://arxiv.org/abs/2602.09130"},{"title":"UniComp: A Unified Evaluation of Large Language Model Compression via Pruning, Quantization, and Distillation","url":"https://arxiv.org/html/2602.09130"},{"title":"UNICOMP: A Unified Evaluation of Large Language Model Compression","url":"https://arxiv.org/pdf/2602.09130"},{"title":"[2602.09130v2] UniComp: A Unified Evaluation of Large Language Model Compression via Pruning, Quantization and Distillation","url":"https://arxiv.org/abs/2602.09130v2"},{"title":"(PDF) UniComp: A Unified Evaluation of Large Language Model Compression via Pruning, Quantization and Distillation","url":"https://www.researchgate.net/publication/400660606_UniComp_A_Unified_Evaluation_of_Large_Language_Model_Compression_via_Pruning_Quantization_and_Distillation"},{"title":"UniComp: Rethinking Video Compression Through Informational Uniqueness","url":"https://arxiv.org/html/2512.03575"},{"title":"UniCom: Unified Multimodal Modeling via Compressed Continuous Semantic Representations","url":"https://arxiv.org/html/2603.10702"},{"title":"GitHub - TimeMarker-LLM/UniComp: [CVPR 2026] Official repository for \"UniComp: Rethinking Video Compression Through Informational Uniqueness\" · GitHub","url":"https://github.com/TimeMarker-LLM/UniComp"},{"title":"UniCompress: Token Compression for Unified Vision–Language Understanding and Generation","url":"https://arxiv.org/html/2603.11320"},{"title":"LLaMo: Scaling Pretrained Language Models for Unified Motion Understanding and Generation with Continuous Autoregressive Tokens","url":"https://arxiv.org/html/2602.12370"}]

Based on the search results, here is the information about the paper arxiv 2602.09130:

**Title:** UniComp: A Unified Evaluation of Large Language Model C
…[truncated 1229 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 143 · 2026-05-14T09:53:45.744850+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2508.15212 SparK query-aware unstructured sparsity KV cache channel pruning authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2508.15212 SparK query-aware unstructured sparsity KV cache channel pruning authors"
  }
}
```

</details>

---

### Tool call

_source line 144 · 2026-05-14T09:53:45.745033+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2410.09615 SLiM one-shot quantization sparsity low-rank LLM weight compression authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2410.09615 SLiM one-shot quantization sparsity low-rank LLM weight compression authors"
  }
}
```

</details>

---

### Tool call

_source line 145 · 2026-05-14T09:53:45.745199+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2510.01290 ThinKV thought-adaptive KV cache compression reasoning authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2510.01290 ThinKV thought-adaptive KV cache compression reasoning authors"
  }
}
```

</details>

---

### Tool call

_source line 146 · 2026-05-14T09:53:45.745362+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2510.13334 DefensiveKV taming fragility KV cache eviction authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2510.13334 DefensiveKV taming fragility KV cache eviction authors"
  }
}
```

</details>

---

### Tool call

_source line 147 · 2026-05-14T09:53:45.745561+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2604.19398 GRASPrune global gating budgeted structured pruning authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2604.19398 GRASPrune global gating budgeted structured pruning authors"
  }
}
```

</details>

---

### Tool call

_source line 148 · 2026-05-14T09:53:45.745728+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2505.22913 Mustafar promoting unstructured sparsity KV cache pruning authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2505.22913 Mustafar promoting unstructured sparsity KV cache pruning authors"
  }
}
```

</details>

---

### Tool result

_source line 149 · 2026-05-14T09:53:45.745942+00:00_

Web search results for query: "arxiv 2410.09615 SLiM one-shot quantization sparsity low-rank LLM weight compression authors"

Links: [{"title":"[2410.09615] SLiM: One-shot Quantization and Sparsity with Low-rank Approximation for LLM Weight Compression","url":"https://arxiv.org/abs/2410.09615"},{"title":"SLiM: One-shot Quantization and Sparsity with Low-rank ...","url":"https://arxiv.org/pdf/2410.09615"},{"title":"SLiM: One-shot Quantization and Sparsity with Low-rank Approximation for LLM Weight Compression","url":"https://arxiv.org/html/2410.09615"},{"title":"SLiM: One-shot Quantization and Sparsity with Low-rank Approximation for LLM Weight Compression | alphaXiv","url":"https://www.alphaxiv.org/abs/2410.09615"},{"title":"SLiM: One-shot Quantization and Sparsity with Low-rank Approximation for LLM Weight Compression - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv241009615M/abstract"},{"title":"ICML Poster SLiM: One-shot Quantization and Sparsity with Low-rank Approximation for LLM Weight Compression","url":"https://icml.cc/virtual/2025/poster/46479"},{"title":"SLiM : One-shot Quantized Sparse Plus Low-rank Approximation of LLMs","url":"https://arxiv.org/html/2410.09615v1"},{"title":"GitHub - Paramathic/slim: SLiM: One-shot Quantized Sparse Plus Low-rank Approximation of LLMs (ICML 2025) · GitHub","url":"https://github.com/Mohammad-Mozaffari/slim"},{"title":"SLIM: One-shot Quantization and Sparsity with Low-rank Approximation for LLM Weight Compression | Research","url":"https://research.nvidia.com/publication/2025-06_slim-one-shot-quantization-and-sparsity-low-rank-approximation-llm-weight"},{"title":"[Literature Review] SLiM: One-shot Quantization and Sparsity with Low-rank Approximation for LLM Weight Compression","url":"https://www.themoonlight.io/en/review/slim-one-shot-quantization-and-sparsity-with-low-rank-approximation-for-llm-weight-compression"}]

Based on the search results, here's the information about arxiv paper 2410.09615:

## SLiM: One-s
…[truncated 1123 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 150 · 2026-05-14T09:53:45.746186+00:00_

Web search results for query: "arxiv 2508.15212 SparK query-aware unstructured sparsity KV cache channel pruning authors"

Links: [{"title":"[2508.15212] SparK: Query-Aware Unstructured Sparsity with Recoverable KV Cache Channel Pruning","url":"https://arxiv.org/abs/2508.15212"},{"title":"SPARK: Query-Aware Unstructured Sparsity with","url":"https://arxiv.org/pdf/2508.15212"},{"title":"SparK: Query-Aware Unstructured Sparsity with Recoverable KV Cache Channel Pruning","url":"https://arxiv.org/html/2508.15212"},{"title":"GitHub - Xnhyacinth/SparK: [AAAI 2026] SparK: Query-Aware Unstructured Sparsity with Recoverable KV Cache Channel Pruning","url":"https://github.com/Xnhyacinth/SparK"},{"title":"SparK: Query-Aware Unstructured Sparsity with Recoverable KV Cache Channel Pruning - haebom","url":"https://haebom.dev/daily_arxiv?tl=en&post=dk58wg2e67jr3mnqevxz"},{"title":"Learnable Permutation for Structured Sparsity on Transformer Models","url":"https://arxiv.org/html/2601.22980v1"},{"title":"[Literature Review] SparK: Query-Aware Unstructured Sparsity with Recoverable KV Cache Channel Pruning","url":"https://www.themoonlight.io/en/review/spark-query-aware-unstructured-sparsity-with-recoverable-kv-cache-channel-pruning"},{"title":"Computation and Language 2025","url":"https://www.arxiv.org/list/cs.CL/2025?skip=11125&show=2000"},{"title":"PocketLLM: Ultimate Compression of Large Language Models via Meta Networks","url":"https://arxiv.org/html/2511.17637v1"},{"title":"SparK: Query-Aware Unstructured Sparsity with Recoverable KV Cache Channel Pruning — ROCm Blogs","url":"https://rocm.blogs.amd.com/artificial-intelligence/spark-blog/README.html"}]

Based on the search results, here is the information about arXiv paper 2508.15212:

**Title:** SparK: Query-Aware Unstructured Sparsity with Recoverable KV Cache Channel Pruning

**Authors:** Huanxuan Liao, Yixing Xu, Shizhu He, Guanchen Li, Xuanwu Yin, Dong Li, Emad Barsoum, Jun Zhao, and Kang Liu

**Overview:** The paper address
…[truncated 814 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 151 · 2026-05-14T09:53:45.746467+00:00_

Web search results for query: "arxiv 2510.01290 ThinKV thought-adaptive KV cache compression reasoning authors"

Links: [{"title":"[2510.01290] ThinKV: Thought-Adaptive KV Cache Compression for Efficient Reasoning Models","url":"https://arxiv.org/abs/2510.01290"},{"title":"[2510.01290v1] ThinKV: Thought-Adaptive KV Cache Compression for Efficient Reasoning Models","url":"https://arxiv.org/abs/2510.01290v1"},{"title":"ThinKV: Thought-Adaptive KV Cache Compression for Efficient Reasoning Models | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/arxiv/2510.01290"},{"title":"ThinKV: Thought-Adaptive KV Cache Compression for Efficient Reasoning Models","url":"https://arxiv.org/html/2510.01290v1"},{"title":"(PDF) ThinKV: Thought-Adaptive KV Cache Compression for Efficient Reasoning Models","url":"https://www.researchgate.net/publication/396142746_ThinKV_Thought-Adaptive_KV_Cache_Compression_for_Efficient_Reasoning_Models"},{"title":"THINKV: THOUGHT-ADAPTIVE KV CACHE COM- PRESSION FOR EFFICIENT REASONING MODELS","url":"https://arxiv.org/pdf/2510.01290v1"},{"title":"ThinKV: Thought-Adaptive KV Cache Compression for Efficient Reasoning Models | OpenReview","url":"https://openreview.net/forum?id=M3CeHnZKNC"},{"title":"Thought-Adaptive KV Cache Compression","url":"https://www.emergentmind.com/topics/thought-adaptive-kv-cache-compression"},{"title":"ICLR Oral ThinKV: Thought-Adaptive KV Cache Compression for Efficient Reasoning Models","url":"https://iclr.cc/virtual/2026/oral/10009981"},{"title":"Hold Onto That Thought: Assessing KV Cache Compression On Reasoning","url":"https://arxiv.org/html/2512.12008v1"}]

Based on the search results, here's the information about the arxiv paper 2510.01290 on ThinKV:

## Paper Overview
ThinKV: Thought-Adaptive KV Cache Compression for Efficient Reasoning Models

## Authors
The authors are Akshat Ramachandran, Marina Neseem, Charbel Sakr, Rangharajan Venkatesan, Brucek Khailany, and Tushar Krishna

## Main Contribution
Thi
…[truncated 900 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 152 · 2026-05-14T09:53:45.746736+00:00_

Web search results for query: "arxiv 2604.19398 GRASPrune global gating budgeted structured pruning authors"

Links: [{"title":"[2604.19398] GRASPrune: Global Gating for Budgeted Structured Pruning of Large Language Models","url":"https://arxiv.org/abs/2604.19398"},{"title":"GRASPrune: Global Gating for Budgeted Structured Pruning of Large Language Models","url":"https://arxiv.org/html/2604.19398"},{"title":"GitHub - ZiY-Wang/GRASPrune: Official implementation of GRASPrune, ACL 2026 Main: global gating for budgeted structured pruning of LLMs. · GitHub","url":"https://github.com/ZiY-Wang/GRASPrune"},{"title":"StructPrune: Structured Global Pruning asymptotics with 𝒪⁢(√𝑁) GPU Memory","url":"https://arxiv.org/html/2510.03246v1"},{"title":"From Local to Global: Revisiting Structured Pruning Paradigms for Large Language Models","url":"https://arxiv.org/html/2510.18030v1"},{"title":"Optimization-based Structural Pruning for Large Language Models without Back-Propagation","url":"https://arxiv.org/html/2406.10576v1"},{"title":"[2004.02164] DSA: More Efficient Budgeted Pruning via Differentiable Sparsity Allocation","url":"https://arxiv.org/abs/2004.02164"},{"title":"[2503.09657] Týr-the-Pruner: Structural Pruning LLMs via Global Sparsity Distribution Optimization","url":"https://arxiv.org/abs/2503.09657"},{"title":"HAP-E: HESSIAN-AWARE STRUCTURED PRUNING OF LLMS FOR EFFICIENT INFERENCE | OpenReview","url":"https://openreview.net/forum?id=B0C0bt2R7l"},{"title":"[1811.09332] Structured Pruning of Neural Networks with Budget-Aware Regularization","url":"https://arxiv.org/abs/1811.09332"}]

Based on the search results, here's information about the arXiv paper 2604.19398:

## GRASPrune: Global Gating for Budgeted Structured Pruning

GRASPrune is a structured pruning framework applied after pretraining that jointly prunes FFN channels and KV head groups under a single global budget.

**Authors:** Ziyang Wang, Jiangfeng Xiao, Chuan Xiao, Ruoxiang Li, Rui Mao, and Jianbin Qin

**Ke
…[truncated 728 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 153 · 2026-05-14T09:53:45.746990+00:00_

Web search results for query: "arxiv 2505.22913 Mustafar promoting unstructured sparsity KV cache pruning authors"

Links: [{"title":"[2505.22913] Mustafar: Promoting Unstructured Sparsity for KV Cache Pruning in LLM Inference","url":"https://arxiv.org/abs/2505.22913"},{"title":"MUSTAFAR: Promoting Unstructured Sparsity for KV Cache Pruning in LLM Inference","url":"https://arxiv.org/html/2505.22913v2"},{"title":"Paper page - Mustafar: Promoting Unstructured Sparsity for KV Cache Pruning in LLM Inference","url":"https://huggingface.co/papers/2505.22913"},{"title":"[PDF] Mustafar: Promoting Unstructured Sparsity for KV Cache Pruning in LLM Inference | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Mustafar:-Promoting-Unstructured-Sparsity-for-KV-in-Joo-Hosseini/643c287adfaccc9d5c06496c9711beb96b2b4d3c"},{"title":"(PDF) Mustafar: Promoting Unstructured Sparsity for KV Cache Pruning in LLM Inference","url":"https://www.researchgate.net/publication/392204576_Mustafar_Promoting_Unstructured_Sparsity_for_KV_Cache_Pruning_in_LLM_Inference"},{"title":"GitHub - dhjoo98/mustafar: codebase for MUSTAFAR:Promoting Unstructured Sparsity for KV Pruning in LLM Inference","url":"https://github.com/dhjoo98/mustafar"},{"title":"MUSTAFAR: Promoting Unstructured Sparsity for KV Cache Pruning in LLM Inference | OpenReview","url":"https://openreview.net/forum?id=C69741fMFX"},{"title":"Mustafar: Promoting Unstructured Sparsity for KV Cache Pruning in LLM Inference | alphaXiv","url":"https://www.alphaxiv.org/overview/2505.22913v1"},{"title":"Mustafar: Promoting Unstructured Sparsity for KV Cache Pruning ...","url":"https://neurips.cc/media/neurips-2025/Slides/119320.pdf"},{"title":"MUSTAFAR: Promoting Unstructured Sparsity for KV Cache Pruning in LLM Inference","url":"https://openreview.net/pdf?id=C69741fMFX"}]

Based on the search results, I found information about arxiv paper 2505.22913. Here are the key details:

**Title:** Mustafar: Promoting Unstructured Sparsity for KV 
…[truncated 957 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 154 · 2026-05-14T09:53:45.747240+00:00_

Web search results for query: "arxiv 2510.13334 DefensiveKV taming fragility KV cache eviction authors"

Links: [{"title":"TAMING THE FRAGILITY OF KV CACHE EVICTION IN LLM INFERENCE","url":"https://arxiv.org/pdf/2510.13334"},{"title":"GitHub - FFY0/DefensiveKV: Official Implementation for [ICLR26] DefensiveKV: Taming the Fragility of KV Cache Eviction in LLM Inference · GitHub","url":"https://github.com/FFY0/DefensiveKV"},{"title":"[2510.13334] Taming the Fragility of KV Cache Eviction in LLM Inference","url":"https://arxiv.org/abs/2510.13334"},{"title":"DefensiveKV: Taming the Fragility of KV Cache Eviction in LLM Inference | OpenReview","url":"https://openreview.net/forum?id=nJgS06sX3O"},{"title":"DEFENSIVEKV: TAMING THE FRAGILITY OF KV CACHE ...","url":"https://openreview.net/pdf?id=nJgS06sX3O"},{"title":"(PDF) Taming the Fragility of KV Cache Eviction in LLM Inference","url":"https://www.researchgate.net/publication/396517805_Taming_the_Fragility_of_KV_Cache_Eviction_in_LLM_Inference"},{"title":"[PDF] Taming the Fragility of KV Cache Eviction in LLM Inference | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Taming-the-Fragility-of-KV-Cache-Eviction-in-LLM-Feng-Guo/10b323b80b3f57a7f15d44eb5a72872a3adfbcb3"},{"title":"TAMING THE FRAGILITY OF KV CACHE EVICTION","url":"https://openreview.net/pdf/2d8c7805c4fcdb477dd04f7b60dd05bd9551c246.pdf"},{"title":"Taming the Fragility of KV Cache Eviction in LLM Inference","url":"https://www.aimodels.fyi/papers/arxiv/taming-fragility-kv-cache-eviction-llm-inference"},{"title":"[2604.25975] Rethinking KV Cache Eviction via a Unified Information-Theoretic Objective","url":"https://arxiv.org/abs/2604.25975"}]

Based on the search results for arxiv 2510.13334, here is the information about DefensiveKV:

## Paper Details

The paper is titled "Taming the Fragility of KV Cache Eviction in LLM Inference" with authors Feng, Yuan; Guo, Haoyu; Lv, JunLin; Zhou, S Kevin; and Xie, Xike.

## Key Contribution

The paper argues 
…[truncated 870 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 155 · 2026-05-14T09:53:45.747525+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2408.03675 NACL general effective KV cache eviction framework LLM authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2408.03675 NACL general effective KV cache eviction framework LLM authors"
  }
}
```

</details>

---

### Tool call

_source line 156 · 2026-05-14T09:53:45.747716+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2602.02199 \"more than a quick glance\" greedy bias KV cache full author list"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2602.02199 \"more than a quick glance\" greedy bias KV cache full author list"
  }
}
```

</details>

---

### Tool call

_source line 157 · 2026-05-14T09:53:45.747924+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2404.14469 SnapKV LLM knows what you are looking for authors Li"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2404.14469 SnapKV LLM knows what you are looking for authors Li"
  }
}
```

</details>

---

### Tool call

_source line 158 · 2026-05-14T09:53:45.748095+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2407.11550 Ada-KV optimizing KV cache eviction adaptive budget allocation authors Feng"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2407.11550 Ada-KV optimizing KV cache eviction adaptive budget allocation authors Feng"
  }
}
```

</details>

---

### Tool call

_source line 159 · 2026-05-14T09:53:45.748261+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2306.14048 H2O heavy hitter oracle efficient generative inference authors Zhang"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2306.14048 H2O heavy hitter oracle efficient generative inference authors Zhang"
  }
}
```

</details>

---

### Tool call

_source line 160 · 2026-05-14T09:53:45.748445+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2406.02069 PyramidKV dynamic KV cache compression pyramidal information funneling authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2406.02069 PyramidKV dynamic KV cache compression pyramidal information funneling authors"
  }
}
```

</details>

---

### Tool result

_source line 161 · 2026-05-14T09:53:45.748648+00:00_

Web search results for query: "arxiv 2602.02199 "more than a quick glance" greedy bias KV cache full author list"

Links: [{"title":"[2602.02199] More Than a Quick Glance: Overcoming the Greedy Bias in KV-Cache Compression","url":"https://arxiv.org/abs/2602.02199"},{"title":"More Than a Quick Glance: Overcoming the Greedy Bias in KV-Cache Compression","url":"https://arxiv.org/html/2602.02199"},{"title":"Fast KV Compaction via Attention Matching","url":"https://arxiv.org/html/2602.16284"},{"title":"Predicting Future Utility: Global Combinatorial Optimization for Task-Agnostic KV Cache Eviction","url":"https://arxiv.org/html/2602.08585v1"},{"title":"[2602.16284] Fast KV Compaction via Attention Matching","url":"https://arxiv.org/abs/2602.16284"},{"title":"KEEP: A KV-Cache-Centric Memory Management System for Efficient Embodied Planning","url":"https://arxiv.org/html/2602.23592"},{"title":"DeltaKV: Residual-Based KV Cache Compression via Long-Range Similarity","url":"https://arxiv.org/html/2602.08005"},{"title":"Preprint THE PITFALLS OF KV CACHE COMPRESSION","url":"https://arxiv.org/pdf/2510.00231"},{"title":"[2602.23200] InnerQ: Hardware-aware Tuning-free Quantization of KV Cache for Large Language Models","url":"https://arxiv.org/abs/2602.23200"},{"title":"[2602.22603] SideQuest: Model-Driven KV Cache Management for Long-Horizon Agentic Reasoning","url":"https://arxiv.org/abs/2602.22603"}]

Based on the search results, I found the paper arxiv 2602.02199. According to the arxiv abstract page, the paper "More Than a Quick Glance: Overcoming the Greedy Bias in KV-Cache Compression" has authors listed as "Aryan Sood and 2 other authors".

However, the search results do not provide the complete full author list. To get the complete list of all authors, you would need to visit the arxiv page directly at https://arxiv.org/abs/2602.02199 or the HTML version at https://arxiv.org/html/2602.02199, where the full author information is typically displayed.


REMINDER: You MUST in
…[truncated 79 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 162 · 2026-05-14T09:53:45.748891+00:00_

Web search results for query: "arxiv 2404.14469 SnapKV LLM knows what you are looking for authors Li"

Links: [{"title":"[2404.14469] SnapKV: LLM Knows What You are Looking for Before Generation","url":"https://arxiv.org/abs/2404.14469"},{"title":"SnapKV: LLM Knows What You are Looking for Before Generation Yuhong Li1∗","url":"https://arxiv.org/pdf/2404.14469"},{"title":"SnapKV : LLM Knows What You are Looking for Before Generation","url":"https://arxiv.org/html/2404.14469v1"},{"title":"[PDF] SnapKV: LLM Knows What You are Looking for Before Generation | Semantic Scholar","url":"https://www.semanticscholar.org/paper/SnapKV:-LLM-Knows-What-You-are-Looking-for-Before-Li-Huang/1784c987e681d60c634765fe64c8d9c26f73d5ff"},{"title":"Paper page - SnapKV: LLM Knows What You are Looking for Before Generation","url":"https://huggingface.co/papers/2404.14469"},{"title":"GitHub - FasterDecoding/SnapKV · GitHub","url":"https://github.com/FasterDecoding/SnapKV"},{"title":"SnapKV: LLM Knows What You are Looking for Before Generation | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/snapkv-llm-knows-what-you-are-looking"},{"title":"SnapKV: Cache compression technique for faster LLM generation with less compute and memory | by SACHIN KUMAR | Medium","url":"https://medium.com/@techsachin/snapkv-cache-compression-technique-for-faster-llm-generation-with-less-compute-and-memory-516ac599c8ee"},{"title":"NeurIPS Poster SnapKV: LLM Knows What You are Looking for Before Generation","url":"https://neurips.cc/virtual/2024/poster/93531"},{"title":"SnapKV: LLM Knows What You are Looking for Before Generation | alphaXiv","url":"https://www.alphaxiv.org/overview/2404.14469"}]

Based on the search results, I found the paper you're looking for:

**Title:** SnapKV: LLM Knows What You are Looking for Before Generation

**Authors:** Yuhong Li, Yingbing Huang, Bowen Yang, Bharat Venkitesh, Acyr Locatelli, Hanchen Ye, Tianle Cai, Patrick Lewis, Deming Chen

**Overview:** SnapKV i
…[truncated 790 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 163 · 2026-05-14T09:53:45.749158+00:00_

Web search results for query: "arxiv 2408.03675 NACL general effective KV cache eviction framework LLM authors"

Links: [{"title":"[2408.03675] NACL: A General and Effective KV Cache Eviction Framework for LLMs at Inference Time","url":"https://arxiv.org/abs/2408.03675"},{"title":"NACL: A General and Effective KV Cache Eviction Framework for LLMs","url":"https://arxiv.org/pdf/2408.03675"},{"title":"Paper page - NACL: A General and Effective KV Cache Eviction Framework for LLMs at Inference Time","url":"https://huggingface.co/papers/2408.03675"},{"title":"NaCl: A General and Effective KV Cache Eviction Framework for LLMs at Inference Time","url":"https://arxiv.org/html/2408.03675"},{"title":"RETHINKING KEY-VALUE CACHE COMPRESSION TECHNIQUES FOR LARGE","url":"https://arxiv.org/pdf/2503.24000"},{"title":"NACL: A General and Effective KV Cache Eviction ...","url":"https://www.emergentmind.com/papers/2408.03675"},{"title":"[Literature Review] NACL: A General and Effective KV Cache Eviction Framework for LLMs at Inference Time","url":"https://www.themoonlight.io/en/review/nacl-a-general-and-effective-kv-cache-eviction-framework-for-llms-at-inference-time"},{"title":"IN-CONTEXT KV-CACHE EVICTION FOR LLMS","url":"https://openreview.net/pdf/28994ecde81dc28a4b4f92441562ed2f2f02c0bb.pdf"},{"title":"Reformulating KV Cache Eviction Problem for Long-Context LLM Inference","url":"https://arxiv.org/html/2605.07234"},{"title":"KV Cache Compression for Inference Efficiency in LLMs: A Review","url":"https://arxiv.org/pdf/2508.06297"}]

Based on the search results, here is information about the paper arxiv 2408.03675:

## NACL: A General and Effective KV Cache Eviction Framework for LLMs

**Title:** NACL is a general framework for long-context KV cache eviction that achieves more optimal and efficient eviction in a single operation during the encoding phase.

**Authors:** Yilong Chen, Guoxia Wang, Junyuan Shang, Shiyao Cui, Zhenyu Zhang, Tingwen Liu, Shuohuan Wang, Yu Sun, Dianhai Yu, 
…[truncated 873 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 164 · 2026-05-14T09:53:45.749526+00:00_

Web search results for query: "arxiv 2407.11550 Ada-KV optimizing KV cache eviction adaptive budget allocation authors Feng"

Links: [{"title":"[2407.11550] Ada-KV: Optimizing KV Cache Eviction by Adaptive Budget Allocation for Efficient LLM Inference","url":"https://arxiv.org/abs/2407.11550"},{"title":"Ada-KV: Optimizing KV Cache Eviction by Adaptive Budget ...","url":"https://arxiv.org/pdf/2407.11550"},{"title":"Ada-KV: Optimizing KV Cache Eviction by Adaptive Budget Allocation for Efficient LLM Inference - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv240711550F/abstract"},{"title":"[2407.11550v5] Ada-KV: Optimizing KV Cache Eviction by Adaptive Budget Allocation for Efficient LLM Inference","url":"https://arxiv.org/abs/2407.11550v5"},{"title":"Ada-KV: Optimizing KV Cache Eviction by Adaptive Budget Allocation for Efficient LLM Inference","url":"https://arxiv.org/html/2407.11550v5"},{"title":"Ada-KV: Optimizing KV Cache Eviction by Adaptive Budget Allocation for Efficient LLM Inference | alphaXiv","url":"https://www.alphaxiv.org/overview/2407.11550v5"},{"title":"GitHub - FFY0/AdaKV: The Official Implementation of Ada-KV [NeurIPS 2025] · GitHub","url":"https://github.com/FFY0/AdaKV"},{"title":"Ada-KV: Optimizing KV Cache Eviction by Adaptive Budget Allocation for Efficient LLM Inference | OpenReview","url":"https://openreview.net/forum?id=tcisuhGsQZ"},{"title":"Optimizing KV Cache Eviction in LLMs: Adaptive Allocation for Enhanced Budget Utilization","url":"https://arxiv.org/html/2407.11550v1"},{"title":"(PDF) Optimizing KV Cache Eviction in LLMs: Adaptive Allocation for Enhanced Budget Utilization","url":"https://www.researchgate.net/publication/382302689_Optimizing_KV_Cache_Eviction_in_LLMs_Adaptive_Allocation_for_Enhanced_Budget_Utilization"}]

I found the paper! Here are the key details about arxiv 2407.11550:

**Title:** Ada-KV: Optimizing KV Cache Eviction by Adaptive Budget Allocation for Efficient LLM Inference

**Authors:** Yuan Feng, Junlin Lv, 
…[truncated 1032 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 165 · 2026-05-14T09:53:45.749832+00:00_

Web search results for query: "arxiv 2306.14048 H2O heavy hitter oracle efficient generative inference authors Zhang"

Links: [{"title":"[2306.14048] H$_2$O: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models","url":"https://arxiv.org/abs/2306.14048"},{"title":"Paper page - H_2O: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models","url":"https://huggingface.co/papers/2306.14048"},{"title":"[PDF] H2O: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/H2O:-Heavy-Hitter-Oracle-for-Efficient-Generative-Zhang-Sheng/e586a4591ba0303b769f2c07cbddaf1899cb72e4"},{"title":"\"H\"₂⁢\"O\": Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models","url":"https://arxiv.org/html/2306.14048v3"},{"title":"H2O: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models | OpenReview","url":"https://openreview.net/forum?id=RkRrPp7GKO"},{"title":"H2O: Heavy-Hitter Oracle for Efficient Generative Inference ...","url":"https://arxiv.org/pdf/2306.14048"},{"title":"H2O: Heavy-Hitter Oracle for Efficient Generative Inference ...","url":"https://dblp.org/rec/journals/corr/abs-2306-14048.html"},{"title":"H$_2$O: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models | Request PDF","url":"https://www.researchgate.net/publication/371871295_H_2O_Heavy-Hitter_Oracle_for_Efficient_Generative_Inference_of_Large_Language_Models"},{"title":"Q-Hitter: A Better Token Oracle for Efficient LLM Inference ...","url":"https://proceedings.mlsys.org/paper_files/paper/2024/file/bbb7506579431a85861a05fff048d3e1-Paper-Conference.pdf"},{"title":"H2O: Heavy-Hitter Oracle for Efficient Generative Inference ...","url":"https://github.com/vllm-project/vllm/issues/3532"}]

I found the paper! Here's a summary of the search results for arxiv 2306.14048:

## Paper Summary

The paper proposes Heavy Hitter O
…[truncated 1115 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 166 · 2026-05-14T09:53:45.750108+00:00_

Web search results for query: "arxiv 2406.02069 PyramidKV dynamic KV cache compression pyramidal information funneling authors"

Links: [{"title":"[2406.02069] PyramidKV: Dynamic KV Cache Compression based on Pyramidal Information Funneling","url":"https://arxiv.org/abs/2406.02069"},{"title":"PyramidKV: Dynamic KV Cache Compression based on Pyramidal Information Funneling","url":"https://arxiv.org/html/2406.02069v1"},{"title":"[2406.02069v1] PyramidKV: Dynamic KV Cache Compression based on Pyramidal Information Funneling","url":"https://arxiv.org/abs/2406.02069v1"},{"title":"PyramidKV: Dynamic KV Cache Compression based on Pyramidal Information Funneling | OpenReview","url":"https://openreview.net/forum?id=ayi7qezU87"},{"title":"PyramidKV: Dynamic KV Cache Compression based on Pyramidal Information Funneling | alphaXiv","url":"https://www.alphaxiv.org/abs/2406.02069"},{"title":"[2406.02069v3] PyramidKV: Dynamic KV Cache Compression based on Pyramidal Information Funneling","url":"https://arxiv.org/abs/2406.02069v3"},{"title":"Paper page - PyramidKV: Dynamic KV Cache Compression based on Pyramidal Information Funneling","url":"https://huggingface.co/papers/2406.02069"},{"title":"PyramidKV: Dynamic KV Cache Compression based on Pyramidal Information Funneling | Request PDF","url":"https://www.researchgate.net/publication/381158444_PyramidKV_Dynamic_KV_Cache_Compression_based_on_Pyramidal_Information_Funneling?_tp=eyJjb250ZXh0Ijp7InBhZ2UiOiJzY2llbnRpZmljQ29udHJpYnV0aW9ucyIsInByZXZpb3VzUGFnZSI6bnVsbCwic3ViUGFnZSI6bnVsbH19"},{"title":"GitHub - Zefan-Cai/KVCache-Factory: Unified KV Cache Compression Methods for Auto-Regressive Models · GitHub","url":"https://github.com/Zefan-Cai/KVCache-Factory"},{"title":"Dynamic KV Cache Compression based on Pyramidal ...","url":"https://ribbitribbit.co/paper/arxiv.2406.02069-PyramidKV-Dynamic-KV-Cache-Compression-based-on-Pyramidal"}]

Based on the search results, here is information about arxiv paper 2406.02069 on PyramidKV:

## Paper
…[truncated 1412 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 167 · 2026-05-14T09:53:45.750397+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2602.02199 Sood Kaur Singh \"more than a quick glance\" greedy bias KV cache authors complete list"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2602.02199 Sood Kaur Singh \"more than a quick glance\" greedy bias KV cache authors complete list"
  }
}
```

</details>

---

### Tool call

_source line 168 · 2026-05-14T09:53:45.750621+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "MATH-500 subset \"let's verify step by step\" Lightman 2024 ICLR OR Hendrycks MATH benchmark 500 problems citation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "WebSearch",
  "tool_args": {
    "query": "MATH-500 subset \"let's verify step by step\" Lightman 2024 ICLR OR Hendrycks MATH benchmark 500 problems citation"
  }
}
```

</details>

---

### Tool result

_source line 169 · 2026-05-14T09:53:45.750825+00:00_

Web search results for query: "arxiv 2602.02199 Sood Kaur Singh "more than a quick glance" greedy bias KV cache authors complete list"

Links: [{"title":"[2602.02199] More Than a Quick Glance: Overcoming the Greedy Bias in KV-Cache Compression","url":"https://arxiv.org/abs/2602.02199"},{"title":"More Than a Quick Glance: Overcoming the Greedy Bias in KV-Cache Compression","url":"https://arxiv.org/html/2602.02199"},{"title":"[2602.22603] SideQuest: Model-Driven KV Cache Management for Long-Horizon Agentic Reasoning","url":"https://arxiv.org/abs/2602.22603"},{"title":"[2602.16284] Fast KV Compaction via Attention Matching","url":"https://arxiv.org/abs/2602.16284"},{"title":"[2602.05929] KV-CoRE: Benchmarking Data-Dependent Low-Rank Compressibility of KV-Caches in LLMs","url":"https://arxiv.org/abs/2602.05929"},{"title":"Learning to Evict from Key-Value Cache","url":"https://arxiv.org/html/2602.10238v1"},{"title":"[2602.10238] Learning to Evict from Key-Value Cache","url":"https://arxiv.org/abs/2602.10238"},{"title":"[2602.08005] DeltaKV: Residual-Based KV Cache Compression via Long-Range Similarity","url":"https://arxiv.org/abs/2602.08005"},{"title":"[2602.07721] ParisKV: Fast and Drift-Robust KV-Cache Retrieval for Long-Context LLMs","url":"https://arxiv.org/abs/2602.07721"},{"title":"[2602.03203] ForesightKV: Optimizing KV Cache Eviction for Reasoning Models by Learning Long-Term Contribution","url":"https://arxiv.org/abs/2602.03203"}]

Based on the search results, I found the paper you're looking for. The complete list of authors for arxiv paper 2602.02199 "More Than a Quick Glance: Overcoming the Greedy Bias in KV-Cache Compression" is: Aryan Sood, Tanvi Sharma, and Vansh Agrawal, all from the Indian Institute of Technology, Roorkee.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 170 · 2026-05-14T09:53:45.751066+00:00_

Web search results for query: "MATH-500 subset "let's verify step by step" Lightman 2024 ICLR OR Hendrycks MATH benchmark 500 problems citation"

Links: [{"title":"\\method: Optimizing Mathematical Reasoning through Stepwise Binary Feedback","url":"https://arxiv.org/html/2501.10799v1"},{"title":"Hyperbolic on X: \"LLM Evaluation Benchmarks\" / X","url":"https://x.com/hyperbolic_labs/status/1913033586447700446"},{"title":"Under review as a conference paper at ICLR 2024 LET’S REWARD STEP BY STEP:","url":"https://openreview.net/pdf?id=RSQL6xvUYW"},{"title":"Published as a conference paper at ICLR 2025","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/7c04aea54c2a60a632a47bd451cd2849-Paper-Conference.pdf"},{"title":"MATH-500 Benchmark Leaderboard | Artificial Analysis","url":"https://artificialanalysis.ai/evaluations/math-500"},{"title":"Big-Math: A Large-Scale, High-Quality Math Dataset for Reinforcement Learning in Language Models","url":"https://arxiv.org/html/2502.17387v1"},{"title":"MATH-500 Leaderboard","url":"https://llm-stats.com/benchmarks/math-500"},{"title":"Benchmark2: Systematic Evaluation of LLM Benchmarks Qi Qian1∗ Chengsong Huang2∗","url":"https://arxiv.org/pdf/2601.03986"},{"title":"Benchmarking LLMs' Mathematical Reasoning with ...","url":"https://arxiv.org/pdf/2501.11790"},{"title":"Published as a conference paper at ICLR 2024 MATHCODER:","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/15425f2df99aa1ba52712c9a4afc8536-Paper-Conference.pdf"}]

Based on the search results, here's what I found regarding MATH-500 and related benchmarks:

## Key Findings

MATH-500 is a subset of the MATH dataset curated to include 500 challenging competition-style problems. It features competition-level mathematics across six domains including algebra, geometry, and number theory.

### The Original MATH Dataset

Dan Hendrycks, Collin Burns, Saurav Kadavath, Akul Arora, Steven Basart, Eric Tang, Dawn Song, and Jacob Steinhardt published "Measuri
…[truncated 1064 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 171 · 2026-05-14T09:53:45.751462+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/references.bib",
  "content": "% References for Phase-Gated Compound Sparse paper\n% Generated 2026-05-14; all entries verified via web search\n\n@inproceedings{adakv-neurips2025,\n    title     = {Ada-{KV}: Optimizing {KV} Cache Eviction by Adaptive Budget Allocation for Efficient {LLM} Inference},\n    author    = {Feng, Yuan and Lv, Junlin and Cao, Yukun and Xie, Xike and Zhou, S. Kevin},\n    booktitle = {Advances in Neural Information Processing Systems},\n    year      = {2025},\n    url       = {https://arxiv.org/abs/2407.11550},\n}\n\n@article{compression-ordering-2025,\n    title   = {A Systematic Study of Compression Ordering for Large Language Models},\n    author  = {Chhawri, Shivansh and Mahadik, Rahul and Rooj, Suparna},\n    journal = {arXiv preprint arXiv:2511.19495},\n    year    = {2025},\n    url     = {https://arxiv.org/abs/2511.19495},\n}\n\n@article{decision-repr-transition-2026,\n    title   = {Understanding Performance Collapse in Layer-Pruned Large Language Models via Decision Representation Transitions},\n    author  = {Shi, Boyu and Liu, Chang and Gao, ChuanBao and Yang, Xu and Geng, Xin},\n    journal = {arXiv preprint arXiv:2605.07271},\n    year    = {2026},\n    url     = {https://arxiv.org/abs/2605.07271},\n}\n\n@article{deepseek-r1,\n    title   = {{DeepSeek-R1}: Incentivizing Reasoning Capability in {LLMs} via Reinforcement Learning},\n    author  = {{DeepSeek-AI}},\n    journal = {Nature},\n    volume  = {645},\n    pages   = {633--638},\n    year    = {2025},\n    url     = {https://arxiv.org/abs/2501.12948},\n}\n\n@inproceedings{defensivekv-iclr2026,\n    title     = {{DefensiveKV}: Taming the Fragility of {KV} Cache Eviction in {LLM} Inference},\n    author    = {Feng, Yuan and Guo, Haoyu and Lv, Junlin and Zhou, S. Kevin and Xie, Xike},\n    booktitle = {International Conference on Learning Representations},\n    year      = {2026},\n    url       = {https://arxiv.org/abs/2510.13334},\n}\n\n@article{doing-more-with-less-2026,\n    title   = {Doing More With Less: Revisiting the Effectiveness of {LLM} Pruning for Test-Time Scaling},\n    author  = {Monjur, Ocean and Nahin, Shahriar Kabir and Chhabra, Anshuman},\n    journal = {arXiv preprint arXiv:2604.25098},\n    year    = {2026},\n    url     = {https://arxiv.org/abs/2604.25098},\n}\n\n@book{efron1993bootstrap,\n    title     = {An Introduction to the Bootstrap},\n    author    = {Efron, Bradley and Tibshirani, Robert J.},\n    publisher = {Chapman \\& Hall/CRC},\n    year      = {1993},\n}\n\n@inproceedings{graspune-acl2026,\n    title     = {{GRASPrune}: Global Gating for Budgeted Structured Pruning of Large Language Models},\n    author    = {Wang, Ziyang and Xiao, Jiangfeng and Xiao, Chuan and Li, Ruoxiang and Mao, Rui and Qin, Jianbin},\n    booktitle = {Proceedings of the 64th Annual Meeting of the Association for Computational Linguistics},\n    year      = {2026},\n    url       = {https://arxiv.org/abs/2604.19398},\n}\n\n@article{greedy-bias-kvcache-2026,\n    title   = {More Than a Quick Glance: Overcoming the Greedy Bias in {KV}-Cache Compression},\n    author  = {Sood, Aryan and Sharma, Tanvi and Agrawal, Vansh},\n    journal = {arXiv preprint arXiv:2602.02199},\n    year    = {2026},\n    url     = {https://arxiv.org/abs/2602.02199},\n}\n\n@inproceedings{h2o2024,\n    title     = {{H\\textsubscript{2}O}: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models},\n    author    = {Zhang, Zhenyu and Sheng, Ying and Zhou, Tianyi and Chen, Tianlong and Zheng, Lianmin and Cai, Ruisi and Song, Zhao and Tian, Yuandong and R{\\'e}, Christopher and Barrett, Clark and Wang, Zhangyang and Chen, Beidi},\n    booktitle = {Advances in Neural Information Processing Systems},\n    year      = {2023},\n    url       = {https://arxiv.org/abs/2306.14048},\n}\n\n@inproceedings{kwon2023vllm,\n    title     = {Efficient Memory Management for Large Language Model Serving with {PagedAttention}},\n    author    = {Kwon, Woosuk and Li, Zhuohan and Zhuang, Siyuan and Sheng, Ying and Zheng, Lianmin and Yu, Cody Hao and Gonzalez, Joseph E. and Zhang, Hao and Stoica, Ion},\n    booktitle = {Proceedings of the 29th Symposium on Operating Systems Principles},\n    year      = {2023},\n    url       = {https://arxiv.org/abs/2309.06180},\n}\n\n@inproceedings{math500,\n    title     = {Measuring Mathematical Problem Solving With the {MATH} Dataset},\n    author    = {Hendrycks, Dan and Burns, Collin and Kadavath, Saurav and Arora, Akul and Basart, Steven and Tang, Eric and Song, Dawn and Steinhardt, Jacob},\n    booktitle = {Advances in Neural Information Processing Systems},\n    year      = {2021},\n    url       = {https://arxiv.org/abs/2103.03874},\n}\n\n@inproceedings{michel2019sixteen,\n    title     = {Are Sixteen Heads Really Better than One?},\n    author    = {Michel, Paul and Levy, Omer and Neubig, Graham},\n    booktitle = {Advances in Neural Information Processing Systems},\n    year      = {2019},\n    url       = {https://arxiv.org/abs/1905.10650},\n}\n\n@inproceedings{mustafar-neurips2025,\n    title     = {Mustafar: Promoting Unstructured Sparsity for {KV} Cache Pruning in {LLM} Inference},\n    author    = {Joo, Donghyeon and Hosseini, Helya and Hadidi, Ramyad and Asgari, Bahar},\n    booktitle = {Advances in Neural Information Processing Systems},\n    year      = {2025},\n    url       = {https://arxiv.org/abs/2505.22913},\n}\n\n@inproceedings{nacl-acl2024,\n    title     = {{NACL}: A General and Effective {KV} Cache Eviction Framework for {LLMs} at Inference Time},\n    author    = {Chen, Yilong and Wang, Guoxia and Shang, Junyuan and Cui, Shiyao and Zhang, Zhenyu and Liu, Tingwen and Wang, Shuohuan and Sun, Yu and Yu, Dianhai and Wu, Hua},\n    booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2408.03675},\n}\n\n@article{obcache-2025,\n    title   = {{OBCache}: Optimal Brain {KV} Cache Pruning for Efficient Long-Context {LLM} Inference},\n    author  = {Gu, Yuzhe and Liang, Xiyu and Zhao, Jiaojiao and Diao, Enmao},\n    journal = {arXiv preprint arXiv:2510.07651},\n    year    = {2025},\n    url     = {https://arxiv.org/abs/2510.07651},\n}\n\n@inproceedings{pagedeviction-eacl2026,\n    title     = {{PagedEviction}: Structured Block-wise {KV} Cache Pruning for Efficient Large Language Model Inference},\n    author    = {Chitty-Venkata, Krishna Teja and Ye, Jie and Sun, Xian-He and Kougkas, Anthony and Emani, Murali and Vishwanath, Venkatram and Nicolae, Bogdan},\n    booktitle = {Findings of the European Chapter of the Association for Computational Linguistics},\n    year      = {2026},\n    url       = {https://arxiv.org/abs/2509.04377},\n}\n\n@article{phase-transition-compression-2026,\n    title   = {Phase transitions in large language model compression},\n    author  = {Ma, Ziyang and Li, Zuchao and Zhang, Lefei and Xia, Gui-Song and Du, Bo and Zhang, Liangpei and Tao, Dacheng},\n    journal = {npj Artificial Intelligence},\n    volume  = {2},\n    number  = {21},\n    year    = {2026},\n    url     = {https://www.nature.com/articles/s44387-026-00072-8},\n}\n\n@inproceedings{pope2023efficiently,\n    title     = {Efficiently Scaling Transformer Inference},\n    author    = {Pope, Reiner and Douglas, Sholto and Chowdhery, Aakanksha and Devlin, Jacob and Bradbury, James and Heek, Jonathan and Xiao, Kefan and Agrawal, Shivani and Dean, Jeff},\n    booktitle = {Proceedings of Machine Learning and Systems},\n    year      = {2023},\n    url       = {https://arxiv.org/abs/2211.05102},\n}\n\n@article{pyramidkv2024,\n    title   = {{PyramidKV}: Dynamic {KV} Cache Compression based on Pyramidal Information Funneling},\n    author  = {Cai, Zefan and Zhang, Yichi and Gao, Bofei and Liu, Yuliang and Liu, Tianyu and Lu, Keming and Xiong, Wayne and Dong, Yue and Chang, Baobao and Hu, Junjie and Xiao, Wen},\n    journal = {arXiv preprint arXiv:2406.02069},\n    year    = {2024},\n    url     = {https://arxiv.org/abs/2406.02069},\n}\n\n@article{qwen2.5,\n    title   = {{Qwen2.5} Technical Report},\n    author  = {Yang, An and Yang, Baosong and Zhang, Beichen and Hui, Binyuan and Zheng, Bo and Yu, Bowen and Li, Chengyuan and Liu, Dayiheng and Huang, Fei and Wei, Haoran and others},\n    journal = {arXiv preprint arXiv:2412.15115},\n    year    = {2024},\n    url     = {https://arxiv.org/abs/2412.15115},\n}\n\n@inproceedings{raas-acl2025,\n    title     = {{RaaS}: Reasoning-Aware Attention Sparsity for Efficient {LLM} Reasoning},\n    author    = {Hu, Junhao and Huang, Wenrui and Wang, Weidong and Li, Zhenwen and Hu, Tiancheng and Liu, Zhixia and Chen, Xusheng and Xie, Tao and Shan, Yizhou},\n    booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},\n    year      = {2025},\n    url       = {https://arxiv.org/abs/2502.11147},\n}\n\n@article{retentivekv-2026,\n    title   = {{RetentiveKV}: State-Space Memory for Uncertainty-Aware Multimodal {KV} Cache Eviction},\n    author  = {Liu, Sihao and Xiong, YuFan and Jiang, Zhonghua and Wang, Zhaode and Lv, Chengfei and Zhang, Shengyu},\n    journal = {arXiv preprint arXiv:2605.04075},\n    year    = {2026},\n    url     = {https://arxiv.org/abs/2605.04075},\n}\n\n@inproceedings{slim-icml2025,\n    title     = {{SLiM}: One-shot Quantization and Sparsity with Low-rank Approximation for {LLM} Weight Compression},\n    author    = {Mozaffari, Mohammad and Yazdanbakhsh, Amir and Dehnavi, Maryam Mehri},\n    booktitle = {Proceedings of the 42nd International Conference on Machine Learning},\n    year      = {2025},\n    url       = {https://arxiv.org/abs/2410.09615},\n}\n\n@inproceedings{snapkv-neurips2024,\n    title     = {{SnapKV}: {LLM} Knows What You Are Looking for Before Generation},\n    author    = {Li, Yuhong and Huang, Yingbing and Yang, Bowen and Venkitesh, Bharat and Locatelli, Acyr and Ye, Hanchen and Cai, Tianle and Lewis, Patrick and Chen, Deming},\n    booktitle = {Advances in Neural Information Processing Systems},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2404.14469},\n}\n\n@inproceedings{snapkv2024,\n    title     = {{SnapKV}: {LLM} Knows What You Are Looking for Before Generation},\n    author    = {Li, Yuhong and Huang, Yingbing and Yang, Bowen and Venkitesh, Bharat and Locatelli, Acyr and Ye, Hanchen and Cai, Tianle and Lewis, Patrick and Chen, Deming},\n    booktitle = {Advances in Neural Information Processing Systems},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2404.14469},\n}\n\n@inproceedings{spark-aaai2026,\n    title     = {{SparK}: Query-Aware Unstructured Sparsity with Recoverable {KV} Cache Channel Pruning},\n    author    = {Liao, Huanxuan and Xu, Yixing and He, Shizhu and Li, Guanchen and Yin, Xuanwu and Li, Dong and Barsoum, Emad and Zhao, Jun and Liu, Kang},\n    booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},\n    year      = {2026},\n    url       = {https://arxiv.org/abs/2508.15212},\n}\n\n@article{sparse-frontier-2025,\n    title   = {The Sparse Frontier: Sparse Attention Trade-offs in Transformer {LLMs}},\n    author  = {Nawrot, Piotr and Li, Robert and Huang, Renjie and Ruder, Sebastian and Marchisio, Kelly and Ponti, Edoardo M.},\n    journal = {arXiv preprint arXiv:2504.17768},\n    year    = {2025},\n    url     = {https://arxiv.org/abs/2504.17768},\n}\n\n@inproceedings{thinkv-iclr2026,\n    title     = {{ThinKV}: Thought-Adaptive {KV} Cache Compression for Efficient Reasoning Models},\n    author    = {Ramachandran, Akshat and Neseem, Marina and Sakr, Charbel and Venkatesan, Rangharajan and Khailany, Brucek and Krishna, Tushar},\n    booktitle = {International Conference on Learning Representations},\n    year      = {2026},\n    url       = {https://arxiv.org/abs/2510.01290},\n}\n\n@article{unicomp-2026,\n    title   = {{UniComp}: A Unified Evaluation of Large Language Model Compression via Pruning, Quantization and Distillation},\n    author  = {von Rad, Jonathan and Cao, Yong and Geiger, Andreas},\n    journal = {arXiv preprint arXiv:2602.09130},\n    year    = {2026},\n    url     = {https://arxiv.org/abs/2602.09130},\n}\n\n@inproceedings{voita2019heads,\n    title     = {Analyzing Multi-Head Self-Attention: Specialized Heads Do the Heavy Lifting, the Rest Can Be Pruned},\n    author    = {Voita, Elena and Talbot, David and Moiseev, Fedor and Sennrich, Rico and Titov, Ivan},\n    booktitle = {Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics},\n    year      = {2019},\n    url       = {https://arxiv.org/abs/1905.09418},\n}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/references.bib",
    "content": "% References for Phase-Gated Compound Sparse paper\n% Generated 2026-05-14; all entries verified via web search\n\n@inproceedings{adakv-neurips2025,\n    title     = {Ada-{KV}: Optimizing {KV} Cache Eviction by Adaptive Budget Allocation for Efficient {LLM} Inference},\n    author    = {Feng, Yuan and Lv, Junlin and Cao, Yukun and Xie, Xike and Zhou, S. Kevin},\n    booktitle = {Advances in Neural Information Processing Systems},\n    year      = {2025},\n    url       = {https://arxiv.org/abs/2407.11550},\n}\n\n@article{compression-ordering-2025,\n    title   = {A Systematic Study of Compression Ordering for Large Language Models},\n    author  = {Chhawri, Shivansh and Mahadik, Rahul and Rooj, Suparna},\n    journal = {arXiv preprint arXiv:2511.19495},\n    year    = {2025},\n    url     = {https://arxiv.org/abs/2511.19495},\n}\n\n@article{decision-repr-transition-2026,\n    title   = {Understanding Performance Collapse in Layer-Pruned Large Language Models via Decision Representation Transitions},\n    author  = {Shi, Boyu and Liu, Chang and Gao, ChuanBao and Yang, Xu and Geng, Xin},\n    journal = {arXiv preprint arXiv:2605.07271},\n    year    = {2026},\n    url     = {https://arxiv.org/abs/2605.07271},\n}\n\n@article{deepseek-r1,\n    title   = {{DeepSeek-R1}: Incentivizing Reasoning Capability in {LLMs} via Reinforcement Learning},\n    author  = {{DeepSeek-AI}},\n    journal = {Nature},\n    volume  = {645},\n    pages   = {633--638},\n    year    = {2025},\n    url     = {https://arxiv.org/abs/2501.12948},\n}\n\n@inproceedings{defensivekv-iclr2026,\n    title     = {{DefensiveKV}: Taming the Fragility of {KV} Cache Eviction in {LLM} Inference},\n    author    = {Feng, Yuan and Guo, Haoyu and Lv, Junlin and Zhou, S. Kevin and Xie, Xike},\n    booktitle = {International Conference on Learning Representations},\n    year      = {2026},\n    url       = {https://arxiv.org/abs/2510.13334},\n}\n\n@article{doing-more-with-less-2026,\n    title   = {Doing More With Less: Revisiting the Effectiveness of {LLM} Pruning for Test-Time Scaling},\n    author  = {Monjur, Ocean and Nahin, Shahriar Kabir and Chhabra, Anshuman},\n    journal = {arXiv preprint arXiv:2604.25098},\n    year    = {2026},\n    url     = {https://arxiv.org/abs/2604.25098},\n}\n\n@book{efron1993bootstrap,\n    title     = {An Introduction to the Bootstrap},\n    author    = {Efron, Bradley and Tibshirani, Robert J.},\n    publisher = {Chapman \\& Hall/CRC},\n    year      = {1993},\n}\n\n@inproceedings{graspune-acl2026,\n    title     = {{GRASPrune}: Global Gating for Budgeted Structured Pruning of Large Language Models},\n    author    = {Wang, Ziyang and Xiao, Jiangfeng and Xiao, Chuan and Li, Ruoxiang and Mao, Rui and Qin, Jianbin},\n    booktitle = {Proceedings of the 64th Annual Meeting of the Association for Computational Linguistics},\n    year      = {2026},\n    url       = {https://arxiv.org/abs/2604.19398},\n}\n\n@article{greedy-bias-kvcache-2026,\n    title   = {More Than a Quick Glance: Overcoming the Greedy Bias in {KV}-Cache Compression},\n    author  = {Sood, Aryan and Sharma, Tanvi and Agrawal, Vansh},\n    journal = {arXiv preprint arXiv:2602.02199},\n    year    = {2026},\n    url     = {https://arxiv.org/abs/2602.02199},\n}\n\n@inproceedings{h2o2024,\n    title     = {{H\\textsubscript{2}O}: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models},\n    author    = {Zhang, Zhenyu and Sheng, Ying and Zhou, Tianyi and Chen, Tianlong and Zheng, Lianmin and Cai, Ruisi and Song, Zhao and Tian, Yuandong and R{\\'e}, Christopher and Barrett, Clark and Wang, Zhangyang and Chen, Beidi},\n    booktitle = {Advances in Neural Information Processing Systems},\n    year      = {2023},\n    url       = {https://arxiv.org/abs/2306.14048},\n}\n\n@inproceedings{kwon2023vllm,\n    title     = {Efficient Memory Management for Large Language Model Serving with {PagedAttention}},\n    author    = {Kwon, Woosuk and Li, Zhuohan and Zhuang, Siyuan and Sheng, Ying and Zheng, Lianmin and Yu, Cody Hao and Gonzalez, Joseph E. and Zhang, Hao and Stoica, Ion},\n    booktitle = {Proceedings of the 29th Symposium on Operating Systems Principles},\n    year      = {2023},\n    url       = {https://arxiv.org/abs/2309.06180},\n}\n\n@inproceedings{math500,\n    title     = {Measuring Mathematical Problem Solving With the {MATH} Dataset},\n    author    = {Hendrycks, Dan and Burns, Collin and Kadavath, Saurav and Arora, Akul and Basart, Steven and Tang, Eric and Song, Dawn and Steinhardt, Jacob},\n    booktitle = {Advances in Neural Information Processing Systems},\n    year      = {2021},\n    url       = {https://arxiv.org/abs/2103.03874},\n}\n\n@inproceedings{michel2019sixteen,\n    title     = {Are Sixteen Heads Really Better than One?},\n    author    = {Michel, Paul and Levy, Omer and Neubig, Graham},\n    booktitle = {Advances in Neural Information Processing Systems},\n    year      = {2019},\n    url       = {https://arxiv.org/abs/1905.10650},\n}\n\n@inproceedings{mustafar-neurips2025,\n    title     = {Mustafar: Promoting Unstructured Sparsity for {KV} Cache Pruning in {LLM} Inference},\n    author    = {Joo, Donghyeon and Hosseini, Helya and Hadidi, Ramyad and Asgari, Bahar},\n    booktitle = {Advances in Neural Information Processing Systems},\n    year      = {2025},\n    url       = {https://arxiv.org/abs/2505.22913},\n}\n\n@inproceedings{nacl-acl2024,\n    title     = {{NACL}: A General and Effective {KV} Cache Eviction Framework for {LLMs} at Inference Time},\n    author    = {Chen, Yilong and Wang, Guoxia and Shang, Junyuan and Cui, Shiyao and Zhang, Zhenyu and Liu, Tingwen and Wang, Shuohuan and Sun, Yu and Yu, Dianhai and Wu, Hua},\n    booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2408.03675},\n}\n\n@article{obcache-2025,\n    title   = {{OBCache}: Optimal Brain {KV} Cache Pruning for Efficient Long-Context {LLM} Inference},\n    author  = {Gu, Yuzhe and Liang, Xiyu and Zhao, Jiaojiao and Diao, Enmao},\n    journal = {arXiv preprint arXiv:2510.07651},\n    year    = {2025},\n    url     = {https://arxiv.org/abs/2510.07651},\n}\n\n@inproceedings{pagedeviction-eacl2026,\n    title     = {{PagedEviction}: Structured Block-wise {KV} Cache Pruning for Efficient Large Language Model Inference},\n    author    = {Chitty-Venkata, Krishna Teja and Ye, Jie and Sun, Xian-He and Kougkas, Anthony and Emani, Murali and Vishwanath, Venkatram and Nicolae, Bogdan},\n    booktitle = {Findings of the European Chapter of the Association for Computational Linguistics},\n    year      = {2026},\n    url       = {https://arxiv.org/abs/2509.04377},\n}\n\n@article{phase-transition-compression-2026,\n    title   = {Phase transitions in large language model compression},\n    author  = {Ma, Ziyang and Li, Zuchao and Zhang, Lefei and Xia, Gui-Song and Du, Bo and Zhang, Liangpei and Tao, Dacheng},\n    journal = {npj Artificial Intelligence},\n    volume  = {2},\n    number  = {21},\n    year    = {2026},\n    url     = {https://www.nature.com/articles/s44387-026-00072-8},\n}\n\n@inproceedings{pope2023efficiently,\n    title     = {Efficiently Scaling Transformer Inference},\n    author    = {Pope, Reiner and Douglas, Sholto and Chowdhery, Aakanksha and Devlin, Jacob and Bradbury, James and Heek, Jonathan and Xiao, Kefan and Agrawal, Shivani and Dean, Jeff},\n    booktitle = {Proceedings of Machine Learning and Systems},\n    year      = {2023},\n    url       = {https://arxiv.org/abs/2211.05102},\n}\n\n@article{pyramidkv2024,\n    title   = {{PyramidKV}: Dynamic {KV} Cache Compression based on Pyramidal Information Funneling},\n    author  = {Cai, Zefan and Zhang, Yichi and Gao, Bofei and Liu, Yuliang and Liu, Tianyu and Lu, Keming and Xiong, Wayne and Dong, Yue and Chang, Baobao and Hu, Junjie and Xiao, Wen},\n    journal = {arXiv preprint arXiv:2406.02069},\n    year    = {2024},\n    url     = {https://arxiv.org/abs/2406.02069},\n}\n\n@article{qwen2.5,\n    title   = {{Qwen2.5} Technical Report},\n    author  = {Yang, An and Yang, Baosong and Zhang, Beichen and Hui, Binyuan and Zheng, Bo and Yu, Bowen and Li, Chengyuan and Liu, Dayiheng and Huang, Fei and Wei, Haoran and others},\n    journal = {arXiv preprint arXiv:2412.15115},\n    year    = {2024},\n    url     = {https://arxiv.org/abs/2412.15115},\n}\n\n@inproceedings{raas-acl2025,\n    title     = {{RaaS}: Reasoning-Aware Attention Sparsity for Efficient {LLM} Reasoning},\n    author    = {Hu, Junhao and Huang, Wenrui and Wang, Weidong and Li, Zhenwen and Hu, Tiancheng and Liu, Zhixia and Chen, Xusheng and Xie, Tao and Shan, Yizhou},\n    booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},\n    year      = {2025},\n    url       = {https://arxiv.org/abs/2502.11147},\n}\n\n@article{retentivekv-2026,\n    title   = {{RetentiveKV}: State-Space Memory for Uncertainty-Aware Multimodal {KV} Cache Eviction},\n    author  = {Liu, Sihao and Xiong, YuFan and Jiang, Zhonghua and Wang, Zhaode and Lv, Chengfei and Zhang, Shengyu},\n    journal = {arXiv preprint arXiv:2605.04075},\n    year    = {2026},\n    url     = {https://arxiv.org/abs/2605.04075},\n}\n\n@inproceedings{slim-icml2025,\n    title     = {{SLiM}: One-shot Quantization and Sparsity with Low-rank Approximation for {LLM} Weight Compression},\n    author    = {Mozaffari, Mohammad and Yazdanbakhsh, Amir and Dehnavi, Maryam Mehri},\n    booktitle = {Proceedings of the 42nd International Conference on Machine Learning},\n    year      = {2025},\n    url       = {https://arxiv.org/abs/2410.09615},\n}\n\n@inproceedings{snapkv-neurips2024,\n    title     = {{SnapKV}: {LLM} Knows What You Are Looking for Before Generation},\n    author    = {Li, Yuhong and Huang, Yingbing and Yang, Bowen and Venkitesh, Bharat and Locatelli, Acyr and Ye, Hanchen and Cai, Tianle and Lewis, Patrick and Chen, Deming},\n    booktitle = {Advances in Neural Information Processing Systems},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2404.14469},\n}\n\n@inproceedings{snapkv2024,\n    title     = {{SnapKV}: {LLM} Knows What You Are Looking for Before Generation},\n    author    = {Li, Yuhong and Huang, Yingbing and Yang, Bowen and Venkitesh, Bharat and Locatelli, Acyr and Ye, Hanchen and Cai, Tianle and Lewis, Patrick and Chen, Deming},\n    booktitle = {Advances in Neural Information Processing Systems},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2404.14469},\n}\n\n@inproceedings{spark-aaai2026,\n    title     = {{SparK}: Query-Aware Unstructured Sparsity with Recoverable {KV} Cache Channel Pruning},\n    author    = {Liao, Huanxuan and Xu, Yixing and He, Shizhu and Li, Guanchen and Yin, Xuanwu and Li, Dong and Barsoum, Emad and Zhao, Jun and Liu, Kang},\n    booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},\n    year      = {2026},\n    url       = {https://arxiv.org/abs/2508.15212},\n}\n\n@article{sparse-frontier-2025,\n    title   = {The Sparse Frontier: Sparse Attention Trade-offs in Transformer {LLMs}},\n    author  = {Nawrot, Piotr and Li, Robert and Huang, Renjie and Ruder, Sebastian and Marchisio, Kelly and Ponti, Edoardo M.},\n    journal = {arXiv preprint arXiv:2504.17768},\n    year    = {2025},\n    url     = {https://arxiv.org/abs/2504.17768},\n}\n\n@inproceedings{thinkv-iclr2026,\n    title     = {{ThinKV}: Thought-Adaptive {KV} Cache Compression for Efficient Reasoning Models},\n    author    = {Ramachandran, Akshat and Neseem, Marina and Sakr, Charbel and Venkatesan, Rangharajan and Khailany, Brucek and Krishna, Tushar},\n    booktitle = {International Conference on Learning Representations},\n    year      = {2026},\n    url       = {https://arxiv.org/abs/2510.01290},\n}\n\n@article{unicomp-2026,\n    title   = {{UniComp}: A Unified Evaluation of Large Language Model Compression via Pruning, Quantization and Distillation},\n    author  = {von Rad, Jonathan and Cao, Yong and Geiger, Andreas},\n    journal = {arXiv preprint arXiv:2602.09130},\n    year    = {2026},\n    url     = {https://arxiv.org/abs/2602.09130},\n}\n\n@inproceedings{voita2019heads,\n    title     = {Analyzing Multi-Head Self-Attention: Specialized Heads Do the Heavy Lifting, the Rest Can Be Pruned},\n    author    = {Voita, Elena and Talbot, David and Moiseev, Fedor and Sennrich, Rico and Titov, Ivan},\n    booktitle = {Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics},\n    year      = {2019},\n    url       = {https://arxiv.org/abs/1905.09418},\n}\n"
  }
}
```

</details>

---

### Tool result

_source line 172 · 2026-05-14T09:53:45.751880+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/references.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 173 · 2026-05-14T09:53:45.752128+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/citation_audit_report.md",
  "content": "# Citation Audit Report\n\nGenerated: 2026-05-14\nPaper: Phase-Gated Compound Sparse (EMNLP 2026 ARR submission)\n\n## Summary\n\n- **Total unique citation keys**: 31\n- **Verified**: 31 (100%)\n- **Unverified / Fake**: 0\n- **Placeholder citations**: 0\n- **Duplicate keys (same paper)**: `snapkv-neurips2024` and `snapkv2024` both cite Li et al. (NeurIPS 2024)\n\n## Per-Citation Verification\n\n### Classic / Well-Established Papers\n\n| # | Key | Status | Title | Authors | Venue | Year | arXiv |\n|---|-----|--------|-------|---------|-------|------|-------|\n| 1 | `kwon2023vllm` | ✅ | Efficient Memory Management for Large Language Model Serving with PagedAttention | Kwon et al. | SOSP | 2023 | 2309.06180 |\n| 2 | `pope2023efficiently` | ✅ | Efficiently Scaling Transformer Inference | Pope et al. | MLSys | 2023 | 2211.05102 |\n| 3 | `voita2019heads` | ✅ | Analyzing Multi-Head Self-Attention: Specialized Heads Do the Heavy Lifting, the Rest Can Be Pruned | Voita et al. | ACL | 2019 | 1905.09418 |\n| 4 | `michel2019sixteen` | ✅ | Are Sixteen Heads Really Better than One? | Michel et al. | NeurIPS | 2019 | 1905.10650 |\n| 5 | `efron1993bootstrap` | ✅ | An Introduction to the Bootstrap | Efron & Tibshirani | Chapman & Hall | 1993 | — |\n| 6 | `deepseek-r1` | ✅ | DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning | DeepSeek-AI | Nature | 2025 | 2501.12948 |\n| 7 | `qwen2.5` | ✅ | Qwen2.5 Technical Report | Yang et al. | arXiv | 2024 | 2412.15115 |\n| 8 | `math500` | ✅ | Measuring Mathematical Problem Solving With the MATH Dataset | Hendrycks et al. | NeurIPS | 2021 | 2103.03874 |\n\n### KV Cache Eviction Papers (2023-2025)\n\n| # | Key | Status | Title | Authors | Venue | Year | arXiv |\n|---|-----|--------|-------|---------|-------|------|-------|\n| 9 | `h2o2024` | ✅ | H₂O: Heavy-Hitter Oracle for Efficient Generative Inference of LLMs | Zhang et al. | NeurIPS | 2023 | 2306.14048 |\n| 10 | `snapkv-neurips2024` | ✅ | SnapKV: LLM Knows What You Are Looking for Before Generation | Li et al. | NeurIPS | 2024 | 2404.14469 |\n| 11 | `snapkv2024` | ✅ | (same as above — duplicate key) | Li et al. | NeurIPS | 2024 | 2404.14469 |\n| 12 | `nacl-acl2024` | ✅ | NACL: A General and Effective KV Cache Eviction Framework for LLMs | Chen et al. | ACL | 2024 | 2408.03675 |\n| 13 | `pyramidkv2024` | ✅ | PyramidKV: Dynamic KV Cache Compression based on Pyramidal Information Funneling | Cai et al. | arXiv | 2024 | 2406.02069 |\n| 14 | `adakv-neurips2025` | ✅ | Ada-KV: Optimizing KV Cache Eviction by Adaptive Budget Allocation | Feng et al. | NeurIPS | 2025 | 2407.11550 |\n| 15 | `mustafar-neurips2025` | ✅ | Mustafar: Promoting Unstructured Sparsity for KV Cache Pruning | Joo et al. | NeurIPS | 2025 | 2505.22913 |\n| 16 | `obcache-2025` | ✅ | OBCache: Optimal Brain KV Cache Pruning for Efficient Long-Context LLM Inference | Gu et al. | arXiv | 2025 | 2510.07651 |\n\n### Compound Compression / Ordering Papers\n\n| # | Key | Status | Title | Authors | Venue | Year | arXiv |\n|---|-----|--------|-------|---------|-------|------|-------|\n| 17 | `spark-aaai2026` | ✅ | SparK: Query-Aware Unstructured Sparsity with Recoverable KV Cache Channel Pruning | Liao et al. | AAAI | 2026 | 2508.15212 |\n| 18 | `slim-icml2025` | ✅ | SLiM: One-shot Quantization and Sparsity with Low-rank Approximation for LLM Weight Compression | Mozaffari et al. | ICML | 2025 | 2410.09615 |\n| 19 | `unicomp-2026` | ✅ | UniComp: A Unified Evaluation of LLM Compression via Pruning, Quantization and Distillation | von Rad et al. | arXiv | 2026 | 2602.09130 |\n| 20 | `compression-ordering-2025` | ✅ | A Systematic Study of Compression Ordering for Large Language Models | Chhawri et al. | arXiv | 2025 | 2511.19495 |\n| 21 | `phase-transition-compression-2026` | ✅ | Phase transitions in large language model compression | Ma et al. | npj AI | 2026 | — |\n| 22 | `graspune-acl2026` | ✅ | GRASPrune: Global Gating for Budgeted Structured Pruning of LLMs | Wang et al. | ACL | 2026 | 2604.19398 |\n\n### Phase-Aware / Reasoning-Aware Inference Papers\n\n| # | Key | Status | Title | Authors | Venue | Year | arXiv |\n|---|-----|--------|-------|---------|-------|------|-------|\n| 23 | `thinkv-iclr2026` | ✅ | ThinKV: Thought-Adaptive KV Cache Compression for Efficient Reasoning Models | Ramachandran et al. | ICLR (Oral) | 2026 | 2510.01290 |\n| 24 | `defensivekv-iclr2026` | ✅ | DefensiveKV: Taming the Fragility of KV Cache Eviction in LLM Inference | Feng et al. | ICLR | 2026 | 2510.13334 |\n| 25 | `decision-repr-transition-2026` | ✅ | Understanding Performance Collapse in Layer-Pruned LLMs via Decision Representation Transitions | Shi et al. | arXiv | 2026 | 2605.07271 |\n| 26 | `doing-more-with-less-2026` | ✅ | Doing More With Less: Revisiting the Effectiveness of LLM Pruning for Test-Time Scaling | Monjur et al. | arXiv | 2026 | 2604.25098 |\n| 27 | `raas-acl2025` | ✅ | RaaS: Reasoning-Aware Attention Sparsity for Efficient LLM Reasoning | Hu et al. | Findings of ACL | 2025 | 2502.11147 |\n| 28 | `sparse-frontier-2025` | ✅ | The Sparse Frontier: Sparse Attention Trade-offs in Transformer LLMs | Nawrot et al. | arXiv | 2025 | 2504.17768 |\n| 29 | `pagedeviction-eacl2026` | ✅ | PagedEviction: Structured Block-wise KV Cache Pruning for Efficient LLM Inference | Chitty-Venkata et al. | Findings of EACL | 2026 | 2509.04377 |\n| 30 | `retentivekv-2026` | ✅ | RetentiveKV: State-Space Memory for Uncertainty-Aware Multimodal KV Cache Eviction | Liu et al. | arXiv | 2026 | 2605.04075 |\n| 31 | `greedy-bias-kvcache-2026` | ✅ | More Than a Quick Glance: Overcoming the Greedy Bias in KV-Cache Compression | Sood et al. | arXiv | 2026 | 2602.02199 |\n\n## Notes\n\n1. **`h2o2024` key vs actual year**: The cite key says \"2024\" but H₂O was published at NeurIPS 2023. The bib entry uses the correct year (2023).\n\n2. **Duplicate SnapKV keys**: `snapkv-neurips2024` and `snapkv2024` both reference the same paper. Both entries are included in the .bib file.\n\n3. **`retentivekv-2026`**: This paper (arXiv 2605.04075, May 2026) is about multimodal KV cache eviction. The paper's usage context focuses on the \"deferred importance\" concept. The paper is very recent (7 days old as of audit date) but verified on arXiv.\n\n4. **`decision-repr-transition-2026`**: Also very recent (arXiv 2605.07271, May 2026). Verified on arXiv.\n\n5. **Venue verification**: All papers claimed to be at specific venues (AAAI 2026, ICLR 2026, ACL 2026, etc.) were cross-verified via official venue pages (OpenReview, ACL Anthology, conference virtual sites).\n\n## Conclusion\n\nAll 31 citations are real, verified papers. No placeholder or hallucinated references detected. The references.bib file is ready for compilation with acl_natbib style.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/citation_audit_report.md",
    "content": "# Citation Audit Report\n\nGenerated: 2026-05-14\nPaper: Phase-Gated Compound Sparse (EMNLP 2026 ARR submission)\n\n## Summary\n\n- **Total unique citation keys**: 31\n- **Verified**: 31 (100%)\n- **Unverified / Fake**: 0\n- **Placeholder citations**: 0\n- **Duplicate keys (same paper)**: `snapkv-neurips2024` and `snapkv2024` both cite Li et al. (NeurIPS 2024)\n\n## Per-Citation Verification\n\n### Classic / Well-Established Papers\n\n| # | Key | Status | Title | Authors | Venue | Year | arXiv |\n|---|-----|--------|-------|---------|-------|------|-------|\n| 1 | `kwon2023vllm` | ✅ | Efficient Memory Management for Large Language Model Serving with PagedAttention | Kwon et al. | SOSP | 2023 | 2309.06180 |\n| 2 | `pope2023efficiently` | ✅ | Efficiently Scaling Transformer Inference | Pope et al. | MLSys | 2023 | 2211.05102 |\n| 3 | `voita2019heads` | ✅ | Analyzing Multi-Head Self-Attention: Specialized Heads Do the Heavy Lifting, the Rest Can Be Pruned | Voita et al. | ACL | 2019 | 1905.09418 |\n| 4 | `michel2019sixteen` | ✅ | Are Sixteen Heads Really Better than One? | Michel et al. | NeurIPS | 2019 | 1905.10650 |\n| 5 | `efron1993bootstrap` | ✅ | An Introduction to the Bootstrap | Efron & Tibshirani | Chapman & Hall | 1993 | — |\n| 6 | `deepseek-r1` | ✅ | DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning | DeepSeek-AI | Nature | 2025 | 2501.12948 |\n| 7 | `qwen2.5` | ✅ | Qwen2.5 Technical Report | Yang et al. | arXiv | 2024 | 2412.15115 |\n| 8 | `math500` | ✅ | Measuring Mathematical Problem Solving With the MATH Dataset | Hendrycks et al. | NeurIPS | 2021 | 2103.03874 |\n\n### KV Cache Eviction Papers (2023-2025)\n\n| # | Key | Status | Title | Authors | Venue | Year | arXiv |\n|---|-----|--------|-------|---------|-------|------|-------|\n| 9 | `h2o2024` | ✅ | H₂O: Heavy-Hitter Oracle for Efficient Generative Inference of LLMs | Zhang et al. | NeurIPS | 2023 | 2306.14048 |\n| 10 | `snapkv-neurips2024` | ✅ | SnapKV: LLM Knows What You Are Looking for Before Generation | Li et al. | NeurIPS | 2024 | 2404.14469 |\n| 11 | `snapkv2024` | ✅ | (same as above — duplicate key) | Li et al. | NeurIPS | 2024 | 2404.14469 |\n| 12 | `nacl-acl2024` | ✅ | NACL: A General and Effective KV Cache Eviction Framework for LLMs | Chen et al. | ACL | 2024 | 2408.03675 |\n| 13 | `pyramidkv2024` | ✅ | PyramidKV: Dynamic KV Cache Compression based on Pyramidal Information Funneling | Cai et al. | arXiv | 2024 | 2406.02069 |\n| 14 | `adakv-neurips2025` | ✅ | Ada-KV: Optimizing KV Cache Eviction by Adaptive Budget Allocation | Feng et al. | NeurIPS | 2025 | 2407.11550 |\n| 15 | `mustafar-neurips2025` | ✅ | Mustafar: Promoting Unstructured Sparsity for KV Cache Pruning | Joo et al. | NeurIPS | 2025 | 2505.22913 |\n| 16 | `obcache-2025` | ✅ | OBCache: Optimal Brain KV Cache Pruning for Efficient Long-Context LLM Inference | Gu et al. | arXiv | 2025 | 2510.07651 |\n\n### Compound Compression / Ordering Papers\n\n| # | Key | Status | Title | Authors | Venue | Year | arXiv |\n|---|-----|--------|-------|---------|-------|------|-------|\n| 17 | `spark-aaai2026` | ✅ | SparK: Query-Aware Unstructured Sparsity with Recoverable KV Cache Channel Pruning | Liao et al. | AAAI | 2026 | 2508.15212 |\n| 18 | `slim-icml2025` | ✅ | SLiM: One-shot Quantization and Sparsity with Low-rank Approximation for LLM Weight Compression | Mozaffari et al. | ICML | 2025 | 2410.09615 |\n| 19 | `unicomp-2026` | ✅ | UniComp: A Unified Evaluation of LLM Compression via Pruning, Quantization and Distillation | von Rad et al. | arXiv | 2026 | 2602.09130 |\n| 20 | `compression-ordering-2025` | ✅ | A Systematic Study of Compression Ordering for Large Language Models | Chhawri et al. | arXiv | 2025 | 2511.19495 |\n| 21 | `phase-transition-compression-2026` | ✅ | Phase transitions in large language model compression | Ma et al. | npj AI | 2026 | — |\n| 22 | `graspune-acl2026` | ✅ | GRASPrune: Global Gating for Budgeted Structured Pruning of LLMs | Wang et al. | ACL | 2026 | 2604.19398 |\n\n### Phase-Aware / Reasoning-Aware Inference Papers\n\n| # | Key | Status | Title | Authors | Venue | Year | arXiv |\n|---|-----|--------|-------|---------|-------|------|-------|\n| 23 | `thinkv-iclr2026` | ✅ | ThinKV: Thought-Adaptive KV Cache Compression for Efficient Reasoning Models | Ramachandran et al. | ICLR (Oral) | 2026 | 2510.01290 |\n| 24 | `defensivekv-iclr2026` | ✅ | DefensiveKV: Taming the Fragility of KV Cache Eviction in LLM Inference | Feng et al. | ICLR | 2026 | 2510.13334 |\n| 25 | `decision-repr-transition-2026` | ✅ | Understanding Performance Collapse in Layer-Pruned LLMs via Decision Representation Transitions | Shi et al. | arXiv | 2026 | 2605.07271 |\n| 26 | `doing-more-with-less-2026` | ✅ | Doing More With Less: Revisiting the Effectiveness of LLM Pruning for Test-Time Scaling | Monjur et al. | arXiv | 2026 | 2604.25098 |\n| 27 | `raas-acl2025` | ✅ | RaaS: Reasoning-Aware Attention Sparsity for Efficient LLM Reasoning | Hu et al. | Findings of ACL | 2025 | 2502.11147 |\n| 28 | `sparse-frontier-2025` | ✅ | The Sparse Frontier: Sparse Attention Trade-offs in Transformer LLMs | Nawrot et al. | arXiv | 2025 | 2504.17768 |\n| 29 | `pagedeviction-eacl2026` | ✅ | PagedEviction: Structured Block-wise KV Cache Pruning for Efficient LLM Inference | Chitty-Venkata et al. | Findings of EACL | 2026 | 2509.04377 |\n| 30 | `retentivekv-2026` | ✅ | RetentiveKV: State-Space Memory for Uncertainty-Aware Multimodal KV Cache Eviction | Liu et al. | arXiv | 2026 | 2605.04075 |\n| 31 | `greedy-bias-kvcache-2026` | ✅ | More Than a Quick Glance: Overcoming the Greedy Bias in KV-Cache Compression | Sood et al. | arXiv | 2026 | 2602.02199 |\n\n## Notes\n\n1. **`h2o2024` key vs actual year**: The cite key says \"2024\" but H₂O was published at NeurIPS 2023. The bib entry uses the correct year (2023).\n\n2. **Duplicate SnapKV keys**: `snapkv-neurips2024` and `snapkv2024` both reference the same paper. Both entries are included in the .bib file.\n\n3. **`retentivekv-2026`**: This paper (arXiv 2605.04075, May 2026) is about multimodal KV cache eviction. The paper's usage context focuses on the \"deferred importance\" concept. The paper is very recent (7 days old as of audit date) but verified on arXiv.\n\n4. **`decision-repr-transition-2026`**: Also very recent (arXiv 2605.07271, May 2026). Verified on arXiv.\n\n5. **Venue verification**: All papers claimed to be at specific venues (AAAI 2026, ICLR 2026, ACL 2026, etc.) were cross-verified via official venue pages (OpenReview, ACL Anthology, conference virtual sites).\n\n## Conclusion\n\nAll 31 citations are real, verified papers. No placeholder or hallucinated references detected. The references.bib file is ready for compilation with acl_natbib style.\n"
  }
}
```

</details>

---

### Tool result

_source line 174 · 2026-05-14T09:53:45.752484+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/citation_audit_report.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 175 · 2026-05-14T09:53:45.752702+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -c '^@' /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/references.bib",
  "description": "Count bib entries"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -c '^@' /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/references.bib",
    "description": "Count bib entries"
  }
}
```

</details>

---

### Tool result

_source line 176 · 2026-05-14T09:53:45.752884+00:00_

31

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 177 · 2026-05-14T09:53:45.753048+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep '^@' /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/references.bib | sort",
  "description": "List all bib entry types and keys"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "Bash",
  "tool_args": {
    "command": "grep '^@' /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/references.bib | sort",
    "description": "List all bib entry types and keys"
  }
}
```

</details>

---

### Tool result

_source line 178 · 2026-05-14T09:53:45.753231+00:00_

@article{compression-ordering-2025,
@article{decision-repr-transition-2026,
@article{deepseek-r1,
@article{doing-more-with-less-2026,
@article{greedy-bias-kvcache-2026,
@article{obcache-2025,
@article{phase-transition-compression-2026,
@article{pyramidkv2024,
@article{qwen2.5,
@article{retentivekv-2026,
@article{sparse-frontier-2025,
@article{unicomp-2026,
@book{efron1993bootstrap,
@inproceedings{adakv-neurips2025,
@inproceedings{defensivekv-iclr2026,
@inproceedings{graspune-acl2026,
@inproceedings{h2o2024,
@inproceedings{kwon2023vllm,
@inproceedings{math500,
@inproceedings{michel2019sixteen,
@inproceedings{mustafar-neurips2025,
@inproceedings{nacl-acl2024,
@inproceedings{pagedeviction-eacl2026,
@inproceedings{pope2023efficiently,
@inproceedings{raas-acl2025,
@inproceedings{slim-icml2025,
@inproceedings{snapkv-neurips2024,
@inproceedings{snapkv2024,
@inproceedings{spark-aaai2026,
@inproceedings{thinkv-iclr2026,
@inproceedings{voita2019heads,

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference_audit_20260514T094550",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 179 · 2026-05-14T09:53:45.753432+00:00_

31 个 bib 条目，与 31 个唯一引用 key 完全匹配。

## 审计结果

**31/31 引用全部验证通过 ✅** — 无虚假引用、无 placeholder、无幻觉。

产出文件：
- **references.bib**: `/artifacts/_project/paper/references.bib` — 31 条完整 BibTeX 条目，acl_natbib 兼容
- **审计报告**: `/artifacts/_project/paper/citation_audit_report.md` — 每条引用的验证状态、作者、venue、arXiv ID

关键发现：
- `snapkv-neurips2024` 和 `snapkv2024` 是同一篇论文的两个 key（已分别建条目）
- `h2o2024` cite key 写的 2024，实际论文发表于 NeurIPS 2023（bib 中已用正确年份）
- 2026 论文（如 `retentivekv-2026`、`decision-repr-transition-2026`）均为最近几天发布的 arXiv 预印本，已验证存在

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_reference_audit_20260514T094550"
}
```

</details>

---
