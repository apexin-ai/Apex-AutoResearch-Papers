# paper c8 llama results integration

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 75
- **Recorded user turns:** 0
- **Tool calls:** 37
- **Original source:** `logs/chats/worker_paper_c8_llama_results_integration_20260516T220519.jsonl`
- **Structured JSON:** [`41a3c3eff0b8f0d128b9.json`](../../sessions/41/41a3c3eff0b8f0d128b9.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

75 recorded events

### Tool call

_source line 1 · 2026-05-16T22:12:24.027052+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_c8_llama_results_integration_20260516T220519",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_project_file",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-16T22:12:24.027597+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_c8_llama_results_integration_20260516T220519",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-16T22:12:24.027824+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "phase-gated-compound-sparse",
  "file": "paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_c8_llama_results_integration_20260516T220519",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "phase-gated-compound-sparse",
    "file": "paper_framing.md"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-16T22:12:24.028084+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/paper_framing.md\", \"content\": \"# Paper Framing — Phase-Gated Compound Sparsity\\n\\n> 最后更新: 2026-05-16 (数值对齐 n=500 registry: DS median_diff 0.39/1.21/3.99/8.48; QW 0.07/0.31/1.07/3.16; Cohen's d registry 0.61→1.13/0.37→1.44; C7+C10 status→confirmed; imp/rand 2.7-15×) | 维护者: Director\\n\\n## Core Insight\\n\\nCompound sparsity（attention head pruning + KV cache eviction）的 severity 不是固定常数——它是 eviction strategy 和 reasoning phase 交互的涌现属性。Importance-based eviction 的 compound interaction severity（paired median difference: median(II_low_i − II_high_i)）随 sparsity 单调递增（DeepSeek: 0.39→1.21→3.99→8.48; Qwen: 0.07→0.31→1.07→3.16），而 random masking 在 s015/s020 NS，在 s025 跨模型显著但效应量远小于 importance（DS: 0.257 vs 3.986; QW: 0.393 vs 1.074, 2.7-15×差异），存在 sparsity threshold ~s020-s025（D063; s030 待定）。Cohen's d（per-problem paired, B=10000）从 medium 到 large（DeepSeek: 0.61→1.13; Qwen: 0.37→1.44，registry cohens_d s015→s030）。LLaMA 跨架构验证（D060）qualitative direction consistent（within-importance d_z~1.0），但 strategy×phase 交互弱于 Qwen2 架构（imp_vs_rand d_z 0.19→0.34, 仅 s030 显著），且 random 在 LLaMA 上也显示显著 phase gradient（d_z 0.35→0.44），与 DeepSeek/Qwen random 低 sparsity NS 模式定性不同。GSM8K 跨 benchmark 验证（D075）：importance masking 的 phase gradient 在 GSM8K 上同样单调递增（QW: 0.039→0.158→1.100→2.092; DS: 0.241→0.740→1.992→4.682），但 strategy specificity（importance/random gradient ratio）从 MATH-500 的 15-36× 衰减至 GSM8K 的 2.3-3.8×。注意：\\\"反转\\\"仅在原始 II_low 值上（random > importance），phase gradient 层面 importance ≥ random。Strategy specificity 的 task-dependence 机制是开放问题（见 §6 Discussion）。这一发现挑战了 compound degradation 均匀分布的隐含假设。\\n\\n**数字基准**：所有数字基于 bf16 per-problem paired 统计量（B=10000 bootstrap）。median_diff 定义为 median(II_low_i − II_high_i)（逐 problem 配对差的中位数）。fp16 旧数据已弃用。\\n\\n## Narrative Arc\\n\\nCompound sparsity 是高效 LLM 推理的实用部署需求，但 prior work（SparK, Ada-KV, SLiM）将 compound interaction 视为均匀超可加。我们发现 sev
…[truncated 10631 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_c8_llama_results_integration_20260516T220519",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-16T22:12:24.028275+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "phase-gated-compound-sparse",
  "file": "writing_plan.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_c8_llama_results_integration_20260516T220519",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "phase-gated-compound-sparse",
    "file": "writing_plan.yaml"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-16T22:12:24.028582+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/writing_plan.yaml\", \"content\": \"## Writing Plan — Phase-Gated Compound Sparsity\\n## 最后更新: 2026-05-14\\n\\n# ============================================================\\n# 投稿目标\\n# ============================================================\\ntarget:\\n  venue: EMNLP 2026 ARR\\n  deadline: 2026-05-25\\n  days_remaining: 11\\n  format: long paper (8 pages + references + appendix)\\n  anonymization: ARR double-blind\\n\\n# ============================================================\\n# Paper Outline\\n# ============================================================\\noutline:\\n  title_candidates:\\n    - \\\"Phase-Modulated Compound Sparsity: How Eviction Strategy and Reasoning Phase Interact in Sparse LLM Inference\\\"\\n    - \\\"Emergent Phase-Strategy Interaction in Compound Sparse LLM Inference\\\"\\n    - \\\"When Compound Sparsity Bites Back: Phase-Dependent Severity Amplification in Importance-Based Eviction\\\"\\n\\n  sections:\\n    - id: abstract\\n      title: Abstract\\n      summary: >\\n        Compound sparsity (head pruning + KV cache eviction) is assumed to degrade uniformly.\\n        We show the interaction is strategy-dependent and phase-modulated: importance-based eviction\\n        exhibits 12-75× severity amplification in low-sparsity reasoning phases, while random eviction\\n        stays flat (~1×). Bootstrap CI (B=10000) confirms significance at all 4 sparsity levels (p<0.0001).\\n        Cross-model replication on Qwen2.5-7B validates generalizability. We explain this via an\\n        entropy-discrimination collapse mechanism: head pruning distributes surviving attention,\\n        destroying importance score discriminability specifically in distributed-attention phases.\\n      length: 250 words\\n\\n    - id: introduction\\n      title: \\\"1. Introduction\\\"\\n      summary: >\\n        Motiv
…[truncated 11186 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_c8_llama_results_integration_20260516T220519",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-16T22:12:24.028789+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_c8_llama_results_integration_20260516T220519",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-16T22:12:24.028933+00:00_

artifacts/_project/paper/main.tex
artifacts/_project/paper/appendix.tex
artifacts/_project/paper/appendix_robustness.tex
artifacts/_project/paper/appendix_disc_analysis.tex
artifacts/dream_reports/dream_20260516T073742/best/paper.tex
artifacts/dream_reports/dream_20260516T073742/median/paper.tex
artifacts/dream_reports/dream_20260516T073742/worst/paper.tex
artifacts/dream_reports/dream_20260516T150210/best/paper.tex
artifacts/dream_reports/dream_20260516T150210/median/paper.tex
artifacts/dream_reports/dream_20260516T150210/worst/paper.tex
artifacts/_project/paper/related_work.tex
artifacts/_project/paper/analysis.tex
artifacts/dream_reports/dream_20260516T164305/best/paper.tex
artifacts/dream_reports/dream_20260516T164305/median/paper.tex
artifacts/dream_reports/dream_20260516T164305/worst/paper.tex
artifacts/_project/paper/abstract.tex
artifacts/_project/paper/introduction.tex
artifacts/_project/paper/limitations.tex
artifacts/_project/paper/conclusion.tex
artifacts/_project/paper/appendix_moved.tex
artifacts/_project/paper/results.tex
artifacts/_project/paper/discussion.tex
artifacts/_project/paper/methodology.tex
artifacts/_project/paper/background.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_c8_llama_results_integration_20260516T220519",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-16T22:12:24.029070+00:00_

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
  "session": "worker_paper_c8_llama_results_integration_20260516T220519",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/results.tex"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-16T22:12:24.029327+00:00_

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
13	\caption{Median of per-problem paired severity differences ($\Delta$) by eviction strategy and sparsity level on DeepSeek-R1-Distill-Qwen-7B ($n{=}496$, MATH-500).}
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
29	Decomposing II by reasoning phase reveals that strategy-dependent severity is driven by amplification in the low-sparsity phase. Table~\ref{tab:main-results} reports the per-phase breakdown. Under importance-based eviction, the median II in the low-sparsity phase rises from $0.357$ ($s{=}0.15$) to $8.456$ ($s{=}0.30$), while the high-sparsity phase remains near zero ($0.003$--$0.038$), yielding paired median differences $\Delta$ from $0.39$ to $8.48$ (all $p \ll 10^{-10}$
…[truncated 16649 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_c8_llama_results_integration_20260516T220519",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-16T22:12:24.029568+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "tab:llama-cross-arch",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_c8_llama_results_integration_20260516T220519",
  "tool": "Grep",
  "tool_args": {
    "pattern": "tab:llama-cross-arch",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-16T22:12:24.029716+00:00_

artifacts/_project/paper/appendix_moved.tex:142:To test whether the phase-modulated severity pattern extends beyond the Qwen2 architecture, we replicate the full experiment on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, 8B parameters; $n{=}250$, MATH-500) under both importance-based and random eviction at $s \in \{0.15, 0.20, 0.25, 0.30\}$. Table~\ref{tab:llama-cross-arch} reports per-phase interaction indices for all 8 conditions.
artifacts/_project/paper/appendix_moved.tex:152:\label{tab:llama-cross-arch}
artifacts/_project/paper/results.tex:93:[Omitted long matching line]
artifacts/_project/paper/main.aux:1736:\newlabel{tab:llama-cross-arch}{{10}{18}{Cross-architecture validation: per-phase II on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, $n{=}250$, MATH-500). Low/High: ratio of low-phase to high-phase median II}{table.caption.52}{}}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_c8_llama_results_integration_20260516T220519",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-16T22:12:24.029850+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "cross-arch",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_c8_llama_results_integration_20260516T220519",
  "tool": "Grep",
  "tool_args": {
    "pattern": "cross-arch",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-16T22:12:24.030013+00:00_

artifacts/_project/paper/numerical_audit_report.md:176:### I2. cross-model vs cross-architecture correctly distinguished ✅
artifacts/_project/paper/numerical_audit_report.md:177:- Main text uses "cross-model" for Qwen2-based comparisons, "cross-architecture" for LLaMA validation
artifacts/_project/paper/numerical_audit_report.md:178:- Limitations acknowledges LLaMA cross-architecture validation (§5.5) as partial support, calls for further validation on more diverse architectures (e.g., Mistral, multi-latent attention)
artifacts/_project/paper/numerical_audit_report.md:179:- Appendix includes rebuttal note acknowledging Qwen2ForCausalLM shared architecture and LlamaForCausalLM cross-architecture result
artifacts/_project/paper/appendix_moved.tex:140:\label{app:cross-arch}
artifacts/_project/paper/appendix_moved.tex:142:To test whether the phase-modulated severity pattern extends beyond the Qwen2 architecture, we replicate the full experiment on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, 8B parameters; $n{=}250$, MATH-500) under both importance-based and random eviction at $s \in \{0.15, 0.20, 0.25, 0.30\}$. Table~\ref{tab:llama-cross-arch} reports per-phase interaction indices for all 8 conditions.
artifacts/_project/paper/appendix_moved.tex:152:\label{tab:llama-cross-arch}
artifacts/_project/paper/limitations.tex:2:[Omitted long matching line]
artifacts/_project/paper/appendix_disc_analysis.tex:38:[Omitted long matching line]
artifacts/_project/paper/introduction.tex:15:The pattern replicates on Qwen2.5-7B-Instruct ($\Delta$: $0.07 \to 3.16$; all $p < 0.005$), with cross-architecture confirmation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, $n{=}250$), where the strategy${\times}$phase gradient ratio of $15$--$33{\times}$ replicates despite ${\sim}26{\times}$ smaller absolute magnitude.
artifacts/_project/paper/introduction.tex:26:    \item We replicate the pattern \textbf{across training paradigms and architectures}: within-architecture replication on Qw
…[truncated 1287 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_c8_llama_results_integration_20260516T220519",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-16T22:12:24.030158+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_moved.tex",
  "offset": "138",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_c8_llama_results_integration_20260516T220519",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_moved.tex",
    "offset": "138",
    "limit": "80"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-16T22:12:24.030458+00:00_

138	
139	\section{Cross-Architecture Analysis}
140	\label{app:cross-arch}
141	
142	To test whether the phase-modulated severity pattern extends beyond the Qwen2 architecture, we replicate the full experiment on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, 8B parameters; $n{=}250$, MATH-500) under both importance-based and random eviction at $s \in \{0.15, 0.20, 0.25, 0.30\}$. Table~\ref{tab:llama-cross-arch} reports per-phase interaction indices for all 8 conditions.
143	
144	The phase gradient replicates fully: importance-based eviction yields low/high ratios of $49{\times}$ to $22{\times}$, while random eviction yields $1.2$--$1.5{\times}$, producing a strategy${\times}$phase gradient ratio of $15$--$33{\times}$ that matches the Qwen2-family pattern. The absolute magnitude is architecture-dependent (${\sim}26{\times}$ smaller than Qwen2 models), consistent with architecture-specific attention head specialization, but the qualitative structure is preserved.
145	
146	A key observation: at $s{=}0.30$, the low-phase absolute II values under importance ($1.465$) and random ($1.461$) eviction are nearly identical, yet phase gradients diverge by $18{\times}$ ($22{\times}$ vs.\ $1.21{\times}$). This confirms that the phase gradient is the informative compound interaction signature, structurally coupled to the scoring mechanism rather than to compression magnitude.
147	
148	\begin{table}[t]
149	\centering
150	\small
151	\caption{Cross-architecture validation: per-phase II on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, $n{=}250$, MATH-500). Low/High: ratio of low-phase to high-phase median II.}
152	\label{tab:llama-cross-arch}
153	\begin{tabular}{@{}llcccc@{}}
154	\toprule
155	$s$ & Strategy & $\widetilde{\mathrm{II}}_{\textit{high}}$ & $\widetilde{\mathrm{II}}_{\textit{low}}$ & Low/High & Gradient ratio \\
156	\midrule
157	0.15 & Importance & $0.001$ & $0.049$ & $49{\times}$ & \multirow{2}{*}{$33{\times}$} \\
158	0.15 & Random     & $0.055$ & $0.072$ & $1.47{\times}
…[truncated 3850 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_c8_llama_results_integration_20260516T220519",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-16T22:12:24.030789+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/introduction.tex",
  "offset": "1",
  "limit": "40"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_c8_llama_results_integration_20260516T220519",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/introduction.tex",
    "offset": "1",
    "limit": "40"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-16T22:12:24.030982+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Long-context language models place acute pressure on the key--value (KV) cache, which grows linearly with sequence length \cite{kwon-sosp2023, pope-mlsys2023}.
5	Two complementary responses---\emph{attention head pruning} \cite{voita-acl2019, michel-neurips2019} and \emph{KV cache eviction} \cite{snapkv-neurips2024, adakv-neurips2025}---are increasingly deployed simultaneously as \emph{compound sparsity}, but the resulting quality degradation is often super-additive \cite{spark-aaai2026, slim-icml2025}. Recent evaluations show that reasoning capabilities degrade disproportionately under compound compression \cite{unicomp-2026}, and that per-dimension safe zones intersect to form a smaller joint safe region \cite{phase-transition-compression-2026}.
6	
7	Prior work treats compound interaction magnitude as roughly constant across generation \cite{spark-aaai2026, unicomp-2026}, despite evidence that pruning sensitivity depends on representational phase \cite{decision-repr-transition-2026} and that no single sparse attention strategy dominates across generation stages \cite{sparse-frontier-2025}.
8	This assumption is problematic for reasoning models, whose chain-of-thought generations \cite{wei-neurips2022-cot} alternate between broadly distributed attention (exploratory reasoning) and sharply concentrated attention (structured computation) \cite{thinkv-iclr2026}.
9	Phase-aware methods like ThinKV \cite{thinkv-iclr2026} apply different KV strategies per phase but without considering compound interaction, while importance-based eviction itself faces challenges from score collapse \cite{hies-2025}, greedy bias \cite{greedy-bias-kvcache-2026}, and temporal dynamics \cite{lethe-aaai2026}. These methods each optimize a single pruning axis; we characterize the interaction when multiple axes are composed.
10	If compound severity varies across these phases, a uniform sparsity budget may be safe in one phase yet destructive
…[truncated 4091 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_c8_llama_results_integration_20260516T220519",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-16T22:12:24.031163+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_c8_llama_results_integration_20260516T220519",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/limitations.tex"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-16T22:12:24.031345+00:00_

1	\paragraph{Model scale and architecture.}
2	Our primary experiments span 7--14B parameters: DeepSeek-R1-Distill-Qwen-7B, Qwen2.5-7B-Instruct, and Qwen2.5-14B-Instruct (\S\ref{sec:scale-14b}). Whether the phase-modulated severity patterns persist, amplify, or attenuate at substantially larger scales (e.g., 70B) remains untested. Cross-architecture validation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, \S\ref{sec:cross-arch}, Appendix~\ref{app:cross-arch}) confirms that both the phase gradient and strategy specificity extend beyond the Qwen2 architecture ($n{=}250$, all 8 conditions; strategy${\times}$phase gradient ratio $15$--$33{\times}$) but with substantially reduced absolute interaction magnitude (${\sim}26{\times}$ smaller than Qwen2-architecture models). The pattern has been tested on two architecture families (Qwen2ForCausalLM, LlamaForCausalLM) at two scale points (7B, 14B); comprehensive validation across more diverse architectures (e.g., Mistral, multi-latent attention) and larger scales is needed for full generalization claims.
3	
4	\paragraph{Task coverage.}
5	We evaluate on three benchmarks spanning mathematical and scientific reasoning: MATH-500 (primary), GSM8K (\S\ref{sec:cross-benchmark}), and GPQA Diamond (\S\ref{sec:cross-benchmark-gpqa}). Cross-benchmark validation on GSM8K supports the phase gradient direction under importance-based eviction but reveals that random eviction is non-significant (CIs spanning zero), precluding meaningful ratio computation. On MATH-500, strategy specificity is quantifiable ($15$--$17{\times}$); on GSM8K, it manifests as a qualitative gap (significant vs.\ non-significant). This suggests that the phase-strategy interaction is robust in direction but task-dependent in form---complex reasoning (MATH-500) produces quantitative strategy contrast while simpler arithmetic (GSM8K) produces qualitative separation. Qwen GSM8K outputs were truncated at \texttt{max\_new\_tokens}${=}$2047, so Qwen GSM8K absolute values 
…[truncated 4776 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_c8_llama_results_integration_20260516T220519",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-16T22:12:24.031618+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/results.tex",
  "old_string": "\\subsection{Cross-Architecture Validation}\n\\label{sec:cross-arch}\n\nCross-architecture validation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, $n{=}250$, MATH-500) confirms that phase-gated compound interaction is architecture-general. Under importance-based eviction, the low/high phase ratio ranges from $49{\\times}$ ($s{=}0.15$) to $22{\\times}$ ($s{=}0.30$); under random eviction, the same ratio is $1.2$--$1.5{\\times}$ (Table~\\ref{tab:llama-cross-arch}). The strategy${\\times}$phase gradient ratio ($15$--$33{\\times}$) replicates the pattern observed on Qwen2-architecture models, confirming that the phenomenon generalizes across Qwen2 (MHA) and LLaMA (GQA) attention implementations.\n\nA striking finding: at $s{=}0.30$, the mean low-phase II values under importance and random eviction are nearly identical ($1.465$ vs.\\ $1.461$), yet the phase \\emph{gradients} diverge by $18{\\times}$ ($22{\\times}$ vs.\\ $1.21{\\times}$). This dissociation demonstrates that the phase gradient, not absolute severity, is the informative signature of compound interaction, and that it is structurally coupled to the eviction strategy's scoring mechanism.\n\nAbsolute interaction magnitudes remain architecture-dependent (${\\sim}26{\\times}$ smaller than Qwen2-family models), consistent with architecture-specific attention head specialization patterns. Full per-condition breakdowns appear in Appendix~\\ref{app:cross-arch}.",
  "new_string": "\\subsection{Cross-Architecture Validation}\n\\label{sec:cross-arch}\n\nCross-architecture validation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, $n{=}250$, MATH-500) supports the generality of phase-modulated compound interaction beyond the Qwen2 architecture family. Under importance-based eviction, the paired median difference $\\Delta$ rises monotonically from $0.050$ ($s{=}0.15$) to $0.695$ ($s{=}0.30$), with large effect sizes throughout ($d_z{=}0.81$--$1.15$; all $p < 10^{-29}$; Table~\\ref{tab:llama-cross-arch}).\n\nA key architectural difference emerges in strategy specificity. On LLaMA, random eviction also exhibits significant phase gradients ($\\Delta{=}0.025$--$0.271$; $d_z{=}0.41$--$0.46$; all $p < 10^{-12}$), unlike DeepSeek and Qwen where random is non-significant at $s \\leq 0.20$. The importance/random $\\Delta$ ratio is $2.0$--$2.6{\\times}$ on LLaMA, substantially weaker than the $15$--$17{\\times}$ observed on DeepSeek. Dose-response monotonicity holds for both strategies (all conditions monotonic). This indicates that the phase gradient itself is architecture-general, while the degree of strategy specificity is architecture-dependent, likely reflecting differences between GQA (LLaMA, 32 heads with 8 KV groups) and MHA (Qwen2, 28 heads) in how head pruning differentially disrupts importance scoring.\n\nAbsolute interaction magnitudes are approximately $7$--$12{\\times}$ smaller than Qwen2-family models at matched sparsity, consistent with architecture-specific attention head specialization patterns. Full per-condition breakdowns appear in Appendix~\\ref{app:cross-arch}."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_c8_llama_results_integration_20260516T220519",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/results.tex",
    "old_string": "\\subsection{Cross-Architecture Validation}\n\\label{sec:cross-arch}\n\nCross-architecture validation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, $n{=}250$, MATH-500) confirms that phase-gated compound interaction is architecture-general. Under importance-based eviction, the low/high phase ratio ranges from $49{\\times}$ ($s{=}0.15$) to $22{\\times}$ ($s{=}0.30$); under random eviction, the same ratio is $1.2$--$1.5{\\times}$ (Table~\\ref{tab:llama-cross-arch}). The strategy${\\times}$phase gradient ratio ($15$--$33{\\times}$) replicates the pattern observed on Qwen2-architecture models, confirming that the phenomenon generalizes across Qwen2 (MHA) and LLaMA (GQA) attention implementations.\n\nA striking finding: at $s{=}0.30$, the mean low-phase II values under importance and random eviction are nearly identical ($1.465$ vs.\\ $1.461$), yet the phase \\emph{gradients} diverge by $18{\\times}$ ($22{\\times}$ vs.\\ $1.21{\\times}$). This dissociation demonstrates that the phase gradient, not absolute severity, is the informative signature of compound interaction, and that it is structurally coupled to the eviction strategy's scoring mechanism.\n\nAbsolute interaction magnitudes remain architecture-dependent (${\\sim}26{\\times}$ smaller than Qwen2-family models), consistent with architecture-specific attention head specialization patterns. Full per-condition breakdowns appear in Appendix~\\ref{app:cross-arch}.",
    "new_string": "\\subsection{Cross-Architecture Validation}\n\\label{sec:cross-arch}\n\nCross-architecture validation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, $n{=}250$, MATH-500) supports the generality of phase-modulated compound interaction beyond the Qwen2 architecture family. Under importance-based eviction, the paired median difference $\\Delta$ rises monotonically from $0.050$ ($s{=}0.15$) to $0.695$ ($s{=}0.30$), with large effect sizes throughout ($d_z{=}0.81$--$1.15$; all $p < 10^{-29}$; Table~\\ref{tab:llama-cross-arch}).\n\nA key architectural difference emerges in strategy specificity. On LLaMA, random eviction also exhibits significant phase gradients ($\\Delta{=}0.025$--$0.271$; $d_z{=}0.41$--$0.46$; all $p < 10^{-12}$), unlike DeepSeek and Qwen where random is non-significant at $s \\leq 0.20$. The importance/random $\\Delta$ ratio is $2.0$--$2.6{\\times}$ on LLaMA, substantially weaker than the $15$--$17{\\times}$ observed on DeepSeek. Dose-response monotonicity holds for both strategies (all conditions monotonic). This indicates that the phase gradient itself is architecture-general, while the degree of strategy specificity is architecture-dependent, likely reflecting differences between GQA (LLaMA, 32 heads with 8 KV groups) and MHA (Qwen2, 28 heads) in how head pruning differentially disrupts importance scoring.\n\nAbsolute interaction magnitudes are approximately $7$--$12{\\times}$ smaller than Qwen2-family models at matched sparsity, consistent with architecture-specific attention head specialization patterns. Full per-condition breakdowns appear in Appendix~\\ref{app:cross-arch}."
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-16T22:12:24.031869+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/results.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_c8_llama_results_integration_20260516T220519",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-16T22:12:24.032030+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_moved.tex",
  "old_string": "To test whether the phase-modulated severity pattern extends beyond the Qwen2 architecture, we replicate the full experiment on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, 8B parameters; $n{=}250$, MATH-500) under both importance-based and random eviction at $s \\in \\{0.15, 0.20, 0.25, 0.30\\}$. Table~\\ref{tab:llama-cross-arch} reports per-phase interaction indices for all 8 conditions.\n\nThe phase gradient replicates fully: importance-based eviction yields low/high ratios of $49{\\times}$ to $22{\\times}$, while random eviction yields $1.2$--$1.5{\\times}$, producing a strategy${\\times}$phase gradient ratio of $15$--$33{\\times}$ that matches the Qwen2-family pattern. The absolute magnitude is architecture-dependent (${\\sim}26{\\times}$ smaller than Qwen2 models), consistent with architecture-specific attention head specialization, but the qualitative structure is preserved.\n\nA key observation: at $s{=}0.30$, the low-phase absolute II values under importance ($1.465$) and random ($1.461$) eviction are nearly identical, yet phase gradients diverge by $18{\\times}$ ($22{\\times}$ vs.\\ $1.21{\\times}$). This confirms that the phase gradient is the informative compound interaction signature, structurally coupled to the scoring mechanism rather than to compression magnitude.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-architecture validation: per-phase II on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, $n{=}250$, MATH-500). Low/High: ratio of low-phase to high-phase median II.}\n\\label{tab:llama-cross-arch}\n\\begin{tabular}{@{}llcccc@{}}\n\\toprule\n$s$ & Strategy & $\\widetilde{\\mathrm{II}}_{\\textit{high}}$ & $\\widetilde{\\mathrm{II}}_{\\textit{low}}$ & Low/High & Gradient ratio \\\\\n\\midrule\n0.15 & Importance & $0.001$ & $0.049$ & $49{\\times}$ & \\multirow{2}{*}{$33{\\times}$} \\\\\n0.15 & Random     & $0.055$ & $0.072$ & $1.47{\\times}$ & \\\\\n\\addlinespace\n0.20 & Importance & $0.007$ & $0.172$ & $25{\\times}$ & \\multirow{2}{*}{$18{\\times}$} \\\\\n0.20 & Random     & $0.164$ & $0.214$ & $1.36{\\times}$ & \\\\\n\\addlinespace\n0.25 & Importance & $0.019$ & $0.415$ & $23{\\times}$ & \\multirow{2}{*}{$18{\\times}$} \\\\\n0.25 & Random     & $0.435$ & $0.563$ & $1.27{\\times}$ & \\\\\n\\addlinespace\n0.30 & Importance & $0.032$ & $0.809$ & $22{\\times}$ & \\multirow{2}{*}{$18{\\times}$} \\\\\n0.30 & Random     & $0.837$ & $1.044$ & $1.21{\\times}$ & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Magnitude comparison.}\nLLaMA interaction indices are approximately $26{\\times}$ smaller than those on Qwen2-architecture models at matched sparsity. This gap likely reflects differences in attention head specialization between MHA (Qwen2, 28 heads) and GQA (LLaMA, 32 heads with 8 KV groups). Despite this magnitude difference, the strategy specificity replicates ($15$--$33{\\times}$ on LLaMA vs.\\ $15$--$17{\\times}$ on DeepSeek and $2.7$--$3.5{\\times}$ on Qwen), confirming that the phase-gated interaction pattern is architecture-general.",
  "new_string": "To test whether the phase-modulated severity pattern extends beyond the Qwen2 architecture, we replicate the full experiment on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, 8B parameters; $n{=}250$, MATH-500) under both importance-based and random eviction at $s \\in \\{0.15, 0.20, 0.25, 0.30\\}$. Table~\\ref{tab:llama-cross-arch} reports paired median differences and effect sizes for all 8 conditions.\n\nThe within-importance phase gradient replicates with large effect sizes: $\\Delta$ rises monotonically from $0.050$ ($s{=}0.15$, $d_z{=}0.81$) to $0.695$ ($s{=}0.30$, $d_z{=}1.15$), all $p < 10^{-29}$. An architecture-specific difference emerges in strategy specificity: random eviction on LLaMA also exhibits statistically significant phase gradients at all four sparsity levels ($\\Delta{=}0.025$--$0.271$; $d_z{=}0.41$--$0.46$; all $p < 10^{-12}$), unlike DeepSeek and Qwen where random eviction is non-significant at $s \\leq 0.20$. The importance/random $\\Delta$ ratio on LLaMA is $2.0$--$2.6{\\times}$, substantially weaker than the $15$--$17{\\times}$ observed on DeepSeek.\n\nDose-response monotonicity holds for both strategies across all sparsity levels, supporting the phase gradient as an architecture-general phenomenon. The reduced strategy specificity on LLaMA suggests that GQA's grouped key-value structure partially preserves importance score quality under head pruning, attenuating the discrimination collapse that drives strategy divergence on MHA architectures.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-architecture validation: paired median difference ($\\Delta$) and effect size ($d_z$) on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, $n{=}250$, MATH-500). All conditions are monotonic.}\n\\label{tab:llama-cross-arch}\n\\begin{tabular}{@{}llccc@{}}\n\\toprule\n$s$ & Strategy & $\\Delta$ & $d_z$ & $p$ \\\\\n\\midrule\n0.15 & Importance & $0.050$ & $0.814$ & $1.4 \\times 10^{-29}$ \\\\\n0.15 & Random     & $0.025$ & $0.436$ & $9.3 \\times 10^{-13}$ \\\\\n\\addlinespace\n0.20 & Importance & $0.159$ & $1.010$ & $8.9 \\times 10^{-35}$ \\\\\n0.20 & Random     & $0.065$ & $0.459$ & $3.6 \\times 10^{-15}$ \\\\\n\\addlinespace\n0.25 & Importance & $0.376$ & $1.115$ & $4.3 \\times 10^{-39}$ \\\\\n0.25 & Random     & $0.184$ & $0.424$ & $3.8 \\times 10^{-13}$ \\\\\n\\addlinespace\n0.30 & Importance & $0.695$ & $1.150$ & $1.5 \\times 10^{-40}$ \\\\\n0.30 & Random     & $0.271$ & $0.410$ & $6.0 \\times 10^{-12}$ \\\\\n\\bottomrule\n\\multicolumn{5}{@{}l}{\\footnotesize Imp/Rand $\\Delta$ ratio: $2.0$--$2.6{\\times}$ (cf.\\ $15$--$17{\\times}$ on DeepSeek).}\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Magnitude comparison.}\nLLaMA interaction magnitudes are approximately $7$--$12{\\times}$ smaller than Qwen2-architecture models at matched sparsity. This gap likely reflects differences in attention head specialization between MHA (Qwen2, 28 heads) and GQA (LLaMA, 32 heads with 8 KV groups). The phase gradient direction and dose-response monotonicity replicate, supporting the architecture-generality of phase-modulated compound interaction. Strategy specificity, however, is weaker ($2.0$--$2.6{\\times}$ on LLaMA vs.\\ $15$--$17{\\times}$ on DeepSeek), indicating that the magnitude of strategy${\\times}$phase interaction depends on architectural factors governing importance score stability under pruning."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_c8_llama_results_integration_20260516T220519",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_moved.tex",
    "old_string": "To test whether the phase-modulated severity pattern extends beyond the Qwen2 architecture, we replicate the full experiment on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, 8B parameters; $n{=}250$, MATH-500) under both importance-based and random eviction at $s \\in \\{0.15, 0.20, 0.25, 0.30\\}$. Table~\\ref{tab:llama-cross-arch} reports per-phase interaction indices for all 8 conditions.\n\nThe phase gradient replicates fully: importance-based eviction yields low/high ratios of $49{\\times}$ to $22{\\times}$, while random eviction yields $1.2$--$1.5{\\times}$, producing a strategy${\\times}$phase gradient ratio of $15$--$33{\\times}$ that matches the Qwen2-family pattern. The absolute magnitude is architecture-dependent (${\\sim}26{\\times}$ smaller than Qwen2 models), consistent with architecture-specific attention head specialization, but the qualitative structure is preserved.\n\nA key observation: at $s{=}0.30$, the low-phase absolute II values under importance ($1.465$) and random ($1.461$) eviction are nearly identical, yet phase gradients diverge by $18{\\times}$ ($22{\\times}$ vs.\\ $1.21{\\times}$). This confirms that the phase gradient is the informative compound interaction signature, structurally coupled to the scoring mechanism rather than to compression magnitude.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-architecture validation: per-phase II on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, $n{=}250$, MATH-500). Low/High: ratio of low-phase to high-phase median II.}\n\\label{tab:llama-cross-arch}\n\\begin{tabular}{@{}llcccc@{}}\n\\toprule\n$s$ & Strategy & $\\widetilde{\\mathrm{II}}_{\\textit{high}}$ & $\\widetilde{\\mathrm{II}}_{\\textit{low}}$ & Low/High & Gradient ratio \\\\\n\\midrule\n0.15 & Importance & $0.001$ & $0.049$ & $49{\\times}$ & \\multirow{2}{*}{$33{\\times}$} \\\\\n0.15 & Random     & $0.055$ & $0.072$ & $1.47{\\times}$ & \\\\\n\\addlinespace\n0.20 & Importance & $0.007$ & $0.172$ & $25{\\times}$ & \\multirow{2}{*}{$18{\\times}$} \\\\\n0.20 & Random     & $0.164$ & $0.214$ & $1.36{\\times}$ & \\\\\n\\addlinespace\n0.25 & Importance & $0.019$ & $0.415$ & $23{\\times}$ & \\multirow{2}{*}{$18{\\times}$} \\\\\n0.25 & Random     & $0.435$ & $0.563$ & $1.27{\\times}$ & \\\\\n\\addlinespace\n0.30 & Importance & $0.032$ & $0.809$ & $22{\\times}$ & \\multirow{2}{*}{$18{\\times}$} \\\\\n0.30 & Random     & $0.837$ & $1.044$ & $1.21{\\times}$ & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Magnitude comparison.}\nLLaMA interaction indices are approximately $26{\\times}$ smaller than those on Qwen2-architecture models at matched sparsity. This gap likely reflects differences in attention head specialization between MHA (Qwen2, 28 heads) and GQA (LLaMA, 32 heads with 8 KV groups). Despite this magnitude difference, the strategy specificity replicates ($15$--$33{\\times}$ on LLaMA vs.\\ $15$--$17{\\times}$ on DeepSeek and $2.7$--$3.5{\\times}$ on Qwen), confirming that the phase-gated interaction pattern is architecture-general.",
    "new_string": "To test whether the phase-modulated severity pattern extends beyond the Qwen2 architecture, we replicate the full experiment on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, 8B parameters; $n{=}250$, MATH-500) under both importance-based and random eviction at $s \\in \\{0.15, 0.20, 0.25, 0.30\\}$. Table~\\ref{tab:llama-cross-arch} reports paired median differences and effect sizes for all 8 conditions.\n\nThe within-importance phase gradient replicates with large effect sizes: $\\Delta$ rises monotonically from $0.050$ ($s{=}0.15$, $d_z{=}0.81$) to $0.695$ ($s{=}0.30$, $d_z{=}1.15$), all $p < 10^{-29}$. An architecture-specific difference emerges in strategy specificity: random eviction on LLaMA also exhibits statistically significant phase gradients at all four sparsity levels ($\\Delta{=}0.025$--$0.271$; $d_z{=}0.41$--$0.46$; all $p < 10^{-12}$), unlike DeepSeek and Qwen where random eviction is non-significant at $s \\leq 0.20$. The importance/random $\\Delta$ ratio on LLaMA is $2.0$--$2.6{\\times}$, substantially weaker than the $15$--$17{\\times}$ observed on DeepSeek.\n\nDose-response monotonicity holds for both strategies across all sparsity levels, supporting the phase gradient as an architecture-general phenomenon. The reduced strategy specificity on LLaMA suggests that GQA's grouped key-value structure partially preserves importance score quality under head pruning, attenuating the discrimination collapse that drives strategy divergence on MHA architectures.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-architecture validation: paired median difference ($\\Delta$) and effect size ($d_z$) on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, $n{=}250$, MATH-500). All conditions are monotonic.}\n\\label{tab:llama-cross-arch}\n\\begin{tabular}{@{}llccc@{}}\n\\toprule\n$s$ & Strategy & $\\Delta$ & $d_z$ & $p$ \\\\\n\\midrule\n0.15 & Importance & $0.050$ & $0.814$ & $1.4 \\times 10^{-29}$ \\\\\n0.15 & Random     & $0.025$ & $0.436$ & $9.3 \\times 10^{-13}$ \\\\\n\\addlinespace\n0.20 & Importance & $0.159$ & $1.010$ & $8.9 \\times 10^{-35}$ \\\\\n0.20 & Random     & $0.065$ & $0.459$ & $3.6 \\times 10^{-15}$ \\\\\n\\addlinespace\n0.25 & Importance & $0.376$ & $1.115$ & $4.3 \\times 10^{-39}$ \\\\\n0.25 & Random     & $0.184$ & $0.424$ & $3.8 \\times 10^{-13}$ \\\\\n\\addlinespace\n0.30 & Importance & $0.695$ & $1.150$ & $1.5 \\times 10^{-40}$ \\\\\n0.30 & Random     & $0.271$ & $0.410$ & $6.0 \\times 10^{-12}$ \\\\\n\\bottomrule\n\\multicolumn{5}{@{}l}{\\footnotesize Imp/Rand $\\Delta$ ratio: $2.0$--$2.6{\\times}$ (cf.\\ $15$--$17{\\times}$ on DeepSeek).}\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Magnitude comparison.}\nLLaMA interaction magnitudes are approximately $7$--$12{\\times}$ smaller than Qwen2-architecture models at matched sparsity. This gap likely reflects differences in attention head specialization between MHA (Qwen2, 28 heads) and GQA (LLaMA, 32 heads with 8 KV groups). The phase gradient direction and dose-response monotonicity replicate, supporting the architecture-generality of phase-modulated compound interaction. Strategy specificity, however, is weaker ($2.0$--$2.6{\\times}$ on LLaMA vs.\\ $15$--$17{\\times}$ on DeepSeek), indicating that the magnitude of strategy${\\times}$phase interaction depends on architectural factors governing importance score stability under pruning."
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-16T22:12:24.032653+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_moved.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_c8_llama_results_integration_20260516T220519",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-16T22:12:24.032850+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/introduction.tex",
  "old_string": "The pattern replicates on Qwen2.5-7B-Instruct ($\\Delta$: $0.07 \\to 3.16$; all $p < 0.005$), with cross-architecture confirmation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, $n{=}250$), where the strategy${\\times}$phase gradient ratio of $15$--$33{\\times}$ replicates despite ${\\sim}26{\\times}$ smaller absolute magnitude.",
  "new_string": "The pattern replicates on Qwen2.5-7B-Instruct ($\\Delta$: $0.07 \\to 3.16$; all $p < 0.005$), with cross-architecture support from DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, $n{=}250$), where the importance phase gradient replicates with large effect sizes ($d_z{=}0.81$--$1.15$; all $p < 10^{-29}$) despite reduced strategy specificity ($2.0$--$2.6{\\times}$ vs.\\ $15$--$17{\\times}$ on Qwen2-family models)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_c8_llama_results_integration_20260516T220519",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/introduction.tex",
    "old_string": "The pattern replicates on Qwen2.5-7B-Instruct ($\\Delta$: $0.07 \\to 3.16$; all $p < 0.005$), with cross-architecture confirmation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, $n{=}250$), where the strategy${\\times}$phase gradient ratio of $15$--$33{\\times}$ replicates despite ${\\sim}26{\\times}$ smaller absolute magnitude.",
    "new_string": "The pattern replicates on Qwen2.5-7B-Instruct ($\\Delta$: $0.07 \\to 3.16$; all $p < 0.005$), with cross-architecture support from DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, $n{=}250$), where the importance phase gradient replicates with large effect sizes ($d_z{=}0.81$--$1.15$; all $p < 10^{-29}$) despite reduced strategy specificity ($2.0$--$2.6{\\times}$ vs.\\ $15$--$17{\\times}$ on Qwen2-family models)."
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-16T22:12:24.033022+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/introduction.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_c8_llama_results_integration_20260516T220519",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-16T22:12:24.033165+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/introduction.tex",
  "old_string": "    \\item We replicate the pattern \\textbf{across training paradigms and architectures}: within-architecture replication on Qwen2.5-7B-Instruct (same Qwen2 backbone, instruction-tuned; $\\Delta$: $0.07 \\to 3.16$; $\\rho{=}1.0$) and cross-architecture validation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM; $n{=}250$; strategy${\\times}$phase gradient ratio $15$--$33{\\times}$ replicates, ${\\sim}26{\\times}$ reduced absolute magnitude; \\S\\ref{sec:cross-arch}).",
  "new_string": "    \\item We replicate the pattern \\textbf{across training paradigms and architectures}: within-architecture replication on Qwen2.5-7B-Instruct (same Qwen2 backbone, instruction-tuned; $\\Delta$: $0.07 \\to 3.16$; $\\rho{=}1.0$) and cross-architecture validation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM; $n{=}250$; importance phase gradient $d_z{=}0.81$--$1.15$, all $p < 10^{-29}$; strategy specificity reduced to $2.0$--$2.6{\\times}$, architecture-dependent; \\S\\ref{sec:cross-arch})."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_c8_llama_results_integration_20260516T220519",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/introduction.tex",
    "old_string": "    \\item We replicate the pattern \\textbf{across training paradigms and architectures}: within-architecture replication on Qwen2.5-7B-Instruct (same Qwen2 backbone, instruction-tuned; $\\Delta$: $0.07 \\to 3.16$; $\\rho{=}1.0$) and cross-architecture validation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM; $n{=}250$; strategy${\\times}$phase gradient ratio $15$--$33{\\times}$ replicates, ${\\sim}26{\\times}$ reduced absolute magnitude; \\S\\ref{sec:cross-arch}).",
    "new_string": "    \\item We replicate the pattern \\textbf{across training paradigms and architectures}: within-architecture replication on Qwen2.5-7B-Instruct (same Qwen2 backbone, instruction-tuned; $\\Delta$: $0.07 \\to 3.16$; $\\rho{=}1.0$) and cross-architecture validation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM; $n{=}250$; importance phase gradient $d_z{=}0.81$--$1.15$, all $p < 10^{-29}$; strategy specificity reduced to $2.0$--$2.6{\\times}$, architecture-dependent; \\S\\ref{sec:cross-arch})."
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-16T22:12:24.033333+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/introduction.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_c8_llama_results_integration_20260516T220519",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-16T22:12:24.033526+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/limitations.tex",
  "old_string": "Cross-architecture validation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, \\S\\ref{sec:cross-arch}, Appendix~\\ref{app:cross-arch}) confirms that both the phase gradient and strategy specificity extend beyond the Qwen2 architecture ($n{=}250$, all 8 conditions; strategy${\\times}$phase gradient ratio $15$--$33{\\times}$) but with substantially reduced absolute interaction magnitude (${\\sim}26{\\times}$ smaller than Qwen2-architecture models).",
  "new_string": "Cross-architecture validation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, \\S\\ref{sec:cross-arch}, Appendix~\\ref{app:cross-arch}) supports that the phase gradient extends beyond the Qwen2 architecture ($n{=}250$, all 8 conditions significant; importance $d_z{=}0.81$--$1.15$), but strategy specificity is substantially weaker ($2.0$--$2.6{\\times}$ vs.\\ $15$--$17{\\times}$ on DeepSeek) because random eviction also exhibits significant phase gradients on LLaMA ($d_z{=}0.41$--$0.46$). This architecture-dependent strategy specificity indicates that the degree of strategy${\\times}$phase interaction, not just absolute magnitude, varies across attention implementations."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_c8_llama_results_integration_20260516T220519",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/limitations.tex",
    "old_string": "Cross-architecture validation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, \\S\\ref{sec:cross-arch}, Appendix~\\ref{app:cross-arch}) confirms that both the phase gradient and strategy specificity extend beyond the Qwen2 architecture ($n{=}250$, all 8 conditions; strategy${\\times}$phase gradient ratio $15$--$33{\\times}$) but with substantially reduced absolute interaction magnitude (${\\sim}26{\\times}$ smaller than Qwen2-architecture models).",
    "new_string": "Cross-architecture validation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, \\S\\ref{sec:cross-arch}, Appendix~\\ref{app:cross-arch}) supports that the phase gradient extends beyond the Qwen2 architecture ($n{=}250$, all 8 conditions significant; importance $d_z{=}0.81$--$1.15$), but strategy specificity is substantially weaker ($2.0$--$2.6{\\times}$ vs.\\ $15$--$17{\\times}$ on DeepSeek) because random eviction also exhibits significant phase gradients on LLaMA ($d_z{=}0.41$--$0.46$). This architecture-dependent strategy specificity indicates that the degree of strategy${\\times}$phase interaction, not just absolute magnitude, varies across attention implementations."
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-16T22:12:24.033722+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/limitations.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_c8_llama_results_integration_20260516T220519",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-16T22:12:24.033869+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "15.*33.*\\\\\\\\times",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_c8_llama_results_integration_20260516T220519",
  "tool": "Grep",
  "tool_args": {
    "pattern": "15.*33.*\\\\\\\\times",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-16T22:12:24.033992+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_c8_llama_results_integration_20260516T220519",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-16T22:12:24.034108+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "15--33",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_c8_llama_results_integration_20260516T220519",
  "tool": "Grep",
  "tool_args": {
    "pattern": "15--33",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-16T22:12:24.034224+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_c8_llama_results_integration_20260516T220519",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-16T22:12:24.034354+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "LLaMA|Llama|llama|cross-arch",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/discussion.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_c8_llama_results_integration_20260516T220519",
  "tool": "Grep",
  "tool_args": {
    "pattern": "LLaMA|Llama|llama|cross-arch",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/discussion.tex",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-16T22:12:24.034497+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_c8_llama_results_integration_20260516T220519",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-16T22:12:24.034614+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "LLaMA|Llama|llama|cross-arch",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/abstract.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_c8_llama_results_integration_20260516T220519",
  "tool": "Grep",
  "tool_args": {
    "pattern": "LLaMA|Llama|llama|cross-arch",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/abstract.tex",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-16T22:12:24.034730+00:00_

6:The pattern replicates on Qwen2.5-7B-Instruct ($\Delta$: $0.07 \to 3.16$; $\rho{=}1.0$), shows consistent phase gradient direction on GSM8K for both models, and generalizes to LlamaForCausalLM ($n{=}250$; strategy${\times}$phase gradient ratio of $15$--$33{\times}$ replicates despite ${\sim}26{\times}$ smaller absolute magnitude).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_c8_llama_results_integration_20260516T220519",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-16T22:12:24.034862+00:00_

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
  "session": "worker_paper_c8_llama_results_integration_20260516T220519",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/abstract.tex"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-16T22:12:24.034994+00:00_

1	\begin{abstract}
2	Compound sparsity---simultaneously pruning attention heads and evicting KV cache entries---is essential for efficient LLM inference but produces super-additive quality degradation whose structure is poorly understood.
3	We find that compound sparsity severity is not a fixed constant but an emergent property of the interaction among eviction strategy, reasoning phase, and sparsity level.
4	On DeepSeek-R1-Distill-Qwen-7B (MATH-500), importance-based eviction exhibits a monotonically increasing phase--severity gradient: the paired median difference $\Delta$ rises from $0.39$ at sparsity $s{=}0.15$ to $8.48$ at $s{=}0.30$ (Spearman $\rho{=}1.0$; all Bonferroni-corrected $p < 0.005$).
5	Random eviction develops a detectable gradient only above $s \approx 0.20$, at $2.7$--$17{\times}$ smaller magnitude.
6	The pattern replicates on Qwen2.5-7B-Instruct ($\Delta$: $0.07 \to 3.16$; $\rho{=}1.0$), shows consistent phase gradient direction on GSM8K for both models, and generalizes to LlamaForCausalLM ($n{=}250$; strategy${\times}$phase gradient ratio of $15$--$33{\times}$ replicates despite ${\sim}26{\times}$ smaller absolute magnitude).
7	Per-phase Gini analysis identifies \emph{importance discrimination collapse}---the degeneration of head importance scores toward uniformity under compound stress---as a correlational diagnostic of this severity divergence.
8	Prior work characterizes compound degradation as phase-agnostic; we show that phase modulates severity by $15$--$17{\times}$ on DeepSeek and $2.7$--$3.5{\times}$ on Qwen. These findings establish phase-gated analysis---decomposing compound severity by reasoning phase and eviction strategy---as a principled diagnostic framework, with direct implications for phase-aware budget allocation in inference systems.
9	\end{abstract}
10	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_c8_llama_results_integration_20260516T220519",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-16T22:12:24.035126+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/abstract.tex",
  "old_string": "The pattern replicates on Qwen2.5-7B-Instruct ($\\Delta$: $0.07 \\to 3.16$; $\\rho{=}1.0$), shows consistent phase gradient direction on GSM8K for both models, and generalizes to LlamaForCausalLM ($n{=}250$; strategy${\\times}$phase gradient ratio of $15$--$33{\\times}$ replicates despite ${\\sim}26{\\times}$ smaller absolute magnitude).",
  "new_string": "The pattern replicates on Qwen2.5-7B-Instruct ($\\Delta$: $0.07 \\to 3.16$; $\\rho{=}1.0$), shows consistent phase gradient direction on GSM8K for both models, and generalizes to LlamaForCausalLM ($n{=}250$; importance phase gradient $d_z{=}0.81$--$1.15$, all $p < 10^{-29}$; strategy specificity architecture-dependent)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_c8_llama_results_integration_20260516T220519",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/abstract.tex",
    "old_string": "The pattern replicates on Qwen2.5-7B-Instruct ($\\Delta$: $0.07 \\to 3.16$; $\\rho{=}1.0$), shows consistent phase gradient direction on GSM8K for both models, and generalizes to LlamaForCausalLM ($n{=}250$; strategy${\\times}$phase gradient ratio of $15$--$33{\\times}$ replicates despite ${\\sim}26{\\times}$ smaller absolute magnitude).",
    "new_string": "The pattern replicates on Qwen2.5-7B-Instruct ($\\Delta$: $0.07 \\to 3.16$; $\\rho{=}1.0$), shows consistent phase gradient direction on GSM8K for both models, and generalizes to LlamaForCausalLM ($n{=}250$; importance phase gradient $d_z{=}0.81$--$1.15$, all $p < 10^{-29}$; strategy specificity architecture-dependent)."
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-16T22:12:24.035264+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/abstract.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_c8_llama_results_integration_20260516T220519",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-16T22:12:24.035392+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "26.*smaller|26.*times",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_c8_llama_results_integration_20260516T220519",
  "tool": "Grep",
  "tool_args": {
    "pattern": "26.*smaller|26.*times",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-16T22:12:24.035540+00:00_

artifacts/_project/paper/related_work.tex:42:[Omitted long matching line]
artifacts/_project/paper/appendix_disc_analysis.tex:14:[Omitted long matching line]
artifacts/_project/paper/introduction.tex:5:[Omitted long matching line]
artifacts/_project/paper/results.tex:8:[Omitted long matching line]
artifacts/_project/paper/results.tex:29:[Omitted long matching line]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_c8_llama_results_integration_20260516T220519",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-16T22:12:24.035657+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "26.*times.*Qwen|26.*smaller.*Qwen",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_c8_llama_results_integration_20260516T220519",
  "tool": "Grep",
  "tool_args": {
    "pattern": "26.*times.*Qwen|26.*smaller.*Qwen",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-16T22:12:24.035769+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_c8_llama_results_integration_20260516T220519",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-16T22:12:24.035878+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "~26",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_c8_llama_results_integration_20260516T220519",
  "tool": "Grep",
  "tool_args": {
    "pattern": "~26",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-16T22:12:24.035987+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_c8_llama_results_integration_20260516T220519",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-16T22:12:24.036095+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "sim.26",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_c8_llama_results_integration_20260516T220519",
  "tool": "Grep",
  "tool_args": {
    "pattern": "sim.26",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-16T22:12:24.036204+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_c8_llama_results_integration_20260516T220519",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-16T22:12:24.036329+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "49.*times|1\\.465",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_c8_llama_results_integration_20260516T220519",
  "tool": "Grep",
  "tool_args": {
    "pattern": "49.*times|1\\.465",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-16T22:12:24.036470+00:00_

artifacts/_project/paper/appendix_moved.tex:5:[Omitted long matching line]
artifacts/_project/paper/appendix_moved.tex:10:\caption{Strategy-dependent crossover at $s{=}0.25$ on DeepSeek ($n{=}496$). Grouped bar chart of median II by eviction strategy and reasoning phase. Importance-based eviction outperforms random in the high-sparsity phase but produces $2.6{\times}$ higher II in the low-sparsity phase, reversing the strategy ranking.}
artifacts/_project/paper/appendix_moved.tex:21:[Omitted long matching line]
artifacts/_project/paper/methodology.tex:21:[Omitted long matching line]
artifacts/_project/paper/results.tex:74:[Omitted long matching line]
artifacts/_project/paper/results.tex:82:[Omitted long matching line]
artifacts/_project/paper/main.aux:744:[Omitted long matching line]
artifacts/_project/paper/main.aux:745:[Omitted long matching line]
artifacts/_project/paper/main.aux:1573:\@writefile{lof}{\contentsline {figure}{\numberline {2}{\ignorespaces Strategy-dependent crossover at $s{=}0.25$ on DeepSeek ($n{=}496$). Grouped bar chart of median II by eviction strategy and reasoning phase. Importance-based eviction outperforms random in the high-sparsity phase but produces $2.6{\times }$ higher II in the low-sparsity phase, reversing the strategy ranking.}}{15}{figure.caption.42}\protected@file@percent }
artifacts/_project/paper/main.aux:1574:\newlabel{fig:crossover}{{2}{15}{Strategy-dependent crossover at $s{=}0.25$ on DeepSeek ($n{=}496$). Grouped bar chart of median II by eviction strategy and reasoning phase. Importance-based eviction outperforms random in the high-sparsity phase but produces $2.6{\times }$ higher II in the low-sparsity phase, reversing the strategy ranking}{figure.caption.42}{}}
artifacts/_project/paper/main.aux:1608:[Omitted long matching line]
artifacts/_project/paper/main.aux:1609:[Omitted long matching line]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_c8_llama_results_integration_20260516T220519",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-16T22:12:24.036626+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "Llama|LLaMA",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_disc_analysis.tex",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_c8_llama_results_integration_20260516T220519",
  "tool": "Grep",
  "tool_args": {
    "pattern": "Llama|LLaMA",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_disc_analysis.tex",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-16T22:12:24.036743+00:00_

38:[Omitted long matching line]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_c8_llama_results_integration_20260516T220519",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-16T22:12:24.036854+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_disc_analysis.tex",
  "offset": "35",
  "limit": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_c8_llama_results_integration_20260516T220519",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_disc_analysis.tex",
    "offset": "35",
    "limit": "10"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-16T22:12:24.036980+00:00_

35	\paragraph{Architectural scope.}
36	Our two models---DeepSeek-R1-Distill-Qwen-7B and Qwen2.5-7B-Instruct---share the Qwen2ForCausalLM architecture.
37	The cross-training-paradigm replication (\S\ref{sec:cross-model}) suggests that the findings are not artifacts of a single model's weights, though both models share the same Qwen2ForCausalLM architecture.
38	Pilot cross-architecture evidence from DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, \S\ref{sec:cross-arch}, Appendix~\ref{app:cross-arch}) suggests qualitatively consistent within-importance phase gradients ($d_z \sim 1.0$) but a substantially weaker strategy $\times$ phase interaction than in Qwen2-based architectures; random pruning also exhibits a non-trivial phase gradient on LLaMA, reducing the strategy contrast. This preliminary evidence ($s{=}0.30$ Wilcoxon $p_{\text{Bonf}}{=}0.029$; $s \leq 0.25$ non-significant) is consistent with the qualitative pattern extending beyond Qwen2 but is insufficient for definitive cross-architecture claims; quantitative impact is architecture-dependent. Comprehensive cross-architecture validation across more diverse designs (e.g., Mistral, multi-latent attention architectures) and scales remains an important next step.
39	
40	
41	\paragraph{Task coverage.}
42	We evaluate exclusively on MATH-500, a mathematical reasoning benchmark.
43	Different reasoning tasks---code generation, commonsense reasoning, multi-hop question answering---may induce different phase structures with different sparsity distributions, potentially altering the severity gradient profile.
44	Generalizing the phase-strategy interaction to broader reasoning domains is an important next step.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_c8_llama_results_integration_20260516T220519",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-16T22:12:24.037141+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_disc_analysis.tex",
  "old_string": "Pilot cross-architecture evidence from DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, \\S\\ref{sec:cross-arch}, Appendix~\\ref{app:cross-arch}) suggests qualitatively consistent within-importance phase gradients ($d_z \\sim 1.0$) but a substantially weaker strategy $\\times$ phase interaction than in Qwen2-based architectures; random pruning also exhibits a non-trivial phase gradient on LLaMA, reducing the strategy contrast. This preliminary evidence ($s{=}0.30$ Wilcoxon $p_{\\text{Bonf}}{=}0.029$; $s \\leq 0.25$ non-significant) is consistent with the qualitative pattern extending beyond Qwen2 but is insufficient for definitive cross-architecture claims; quantitative impact is architecture-dependent. Comprehensive cross-architecture validation across more diverse designs (e.g., Mistral, multi-latent attention architectures) and scales remains an important next step.",
  "new_string": "Cross-architecture validation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, $n{=}250$, \\S\\ref{sec:cross-arch}, Appendix~\\ref{app:cross-arch}) confirms qualitatively consistent within-importance phase gradients ($d_z{=}0.81$--$1.15$; all $p < 10^{-29}$) but a substantially weaker strategy${\\times}$phase interaction than in Qwen2-based architectures: random eviction also exhibits significant phase gradients on LLaMA ($d_z{=}0.41$--$0.46$; all $p < 10^{-12}$), reducing the importance/random ratio to $2.0$--$2.6{\\times}$ (vs.\\ $15$--$17{\\times}$ on DeepSeek). The phase gradient direction and dose-response monotonicity are architecture-general; quantitative strategy specificity is architecture-dependent. Comprehensive cross-architecture validation across more diverse designs (e.g., Mistral, multi-latent attention architectures) and scales remains an important next step."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_c8_llama_results_integration_20260516T220519",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_disc_analysis.tex",
    "old_string": "Pilot cross-architecture evidence from DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, \\S\\ref{sec:cross-arch}, Appendix~\\ref{app:cross-arch}) suggests qualitatively consistent within-importance phase gradients ($d_z \\sim 1.0$) but a substantially weaker strategy $\\times$ phase interaction than in Qwen2-based architectures; random pruning also exhibits a non-trivial phase gradient on LLaMA, reducing the strategy contrast. This preliminary evidence ($s{=}0.30$ Wilcoxon $p_{\\text{Bonf}}{=}0.029$; $s \\leq 0.25$ non-significant) is consistent with the qualitative pattern extending beyond Qwen2 but is insufficient for definitive cross-architecture claims; quantitative impact is architecture-dependent. Comprehensive cross-architecture validation across more diverse designs (e.g., Mistral, multi-latent attention architectures) and scales remains an important next step.",
    "new_string": "Cross-architecture validation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, $n{=}250$, \\S\\ref{sec:cross-arch}, Appendix~\\ref{app:cross-arch}) confirms qualitatively consistent within-importance phase gradients ($d_z{=}0.81$--$1.15$; all $p < 10^{-29}$) but a substantially weaker strategy${\\times}$phase interaction than in Qwen2-based architectures: random eviction also exhibits significant phase gradients on LLaMA ($d_z{=}0.41$--$0.46$; all $p < 10^{-12}$), reducing the importance/random ratio to $2.0$--$2.6{\\times}$ (vs.\\ $15$--$17{\\times}$ on DeepSeek). The phase gradient direction and dose-response monotonicity are architecture-general; quantitative strategy specificity is architecture-dependent. Comprehensive cross-architecture validation across more diverse designs (e.g., Mistral, multi-latent attention architectures) and scales remains an important next step."
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-16T22:12:24.037345+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_disc_analysis.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_c8_llama_results_integration_20260516T220519",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-16T22:12:24.037518+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "gradient ratio.*LLaMA|gradient ratio.*Llama|Llama.*gradient ratio",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_c8_llama_results_integration_20260516T220519",
  "tool": "Grep",
  "tool_args": {
    "pattern": "gradient ratio.*LLaMA|gradient ratio.*Llama|Llama.*gradient ratio",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-16T22:12:24.037642+00:00_

artifacts/_project/paper/conclusion.tex:4:[Omitted long matching line]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_c8_llama_results_integration_20260516T220519",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-16T22:12:24.037755+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "Llama.*confirm",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_c8_llama_results_integration_20260516T220519",
  "tool": "Grep",
  "tool_args": {
    "pattern": "Llama.*confirm",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-16T22:12:24.037867+00:00_

artifacts/_project/paper/conclusion.tex:4:[Omitted long matching line]
artifacts/_project/paper/appendix_disc_analysis.tex:38:[Omitted long matching line]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_c8_llama_results_integration_20260516T220519",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-16T22:12:24.037979+00:00_

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
  "session": "worker_paper_c8_llama_results_integration_20260516T220519",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/conclusion.tex"
  }
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-16T22:12:24.038101+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We showed that compound sparsity severity is not phase-invariant but exhibits an emergent phase-strategy interaction. Under importance-based eviction, the paired median difference $\Delta$ increases from $0.39$ to $8.48$ (DeepSeek, $n{=}500$; Spearman $\rho{=}1.0$) and $0.07$ to $3.16$ (Qwen, $n{=}475$), all $p < 10^{-13}$. Random eviction is $2.7$--$17{\times}$ weaker where both strategies are significant ($s \geq 0.25$; DeepSeek $15$--$17{\times}$, Qwen $2.7$--$3.5{\times}$). The strategy${\times}$phase gradient ratio replicates on LlamaForCausalLM ($15$--$33{\times}$, $n{=}250$), confirming architecture-generality. A model-dependent crossover on DeepSeek demonstrates that no single strategy dominates uniformly. Per-phase Gini analysis reveals importance discrimination collapse as a correlational diagnostic: despite near-identical aggregate Gini drops, severity diverges by $2.7$--$17{\times}$, implicating the structural specificity of importance-based pruning.
5	Beyond the empirical findings, the phase-gated analysis framework itself---decomposing compound severity by reasoning phase and eviction strategy---transforms a scalar interaction metric into a structured diagnostic that reveals where compound sparsity fails and why. This framework provides practitioners with a principled basis for phase-aware sparsity allocation: applying aggressive compression during high-sparsity (structured computation) phases while preserving budget during low-sparsity (exploratory reasoning) phases. Future work could explore generalization to other reasoning domains, causal validation of importance discrimination collapse, and systematic characterization of asymmetric compound interactions.
6	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_c8_llama_results_integration_20260516T220519",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-16T22:12:24.038237+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/conclusion.tex",
  "old_string": "The strategy${\\times}$phase gradient ratio replicates on LlamaForCausalLM ($15$--$33{\\times}$, $n{=}250$), confirming architecture-generality.",
  "new_string": "The importance phase gradient replicates on LlamaForCausalLM ($d_z{=}0.81$--$1.15$, $n{=}250$, all $p < 10^{-29}$), supporting architecture-generality of phase modulation, while strategy specificity is architecture-dependent ($2.0$--$2.6{\\times}$ on LLaMA vs.\\ $15$--$17{\\times}$ on DeepSeek)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_c8_llama_results_integration_20260516T220519",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/conclusion.tex",
    "old_string": "The strategy${\\times}$phase gradient ratio replicates on LlamaForCausalLM ($15$--$33{\\times}$, $n{=}250$), confirming architecture-generality.",
    "new_string": "The importance phase gradient replicates on LlamaForCausalLM ($d_z{=}0.81$--$1.15$, $n{=}250$, all $p < 10^{-29}$), supporting architecture-generality of phase modulation, while strategy specificity is architecture-dependent ($2.0$--$2.6{\\times}$ on LLaMA vs.\\ $15$--$17{\\times}$ on DeepSeek)."
  }
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-16T22:12:24.038381+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/conclusion.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_c8_llama_results_integration_20260516T220519",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 67 · 2026-05-16T22:12:24.038531+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_disc_analysis.tex",
  "offset": "36",
  "limit": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_c8_llama_results_integration_20260516T220519",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_disc_analysis.tex",
    "offset": "36",
    "limit": "5"
  }
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-16T22:12:24.038659+00:00_

36	Our two models---DeepSeek-R1-Distill-Qwen-7B and Qwen2.5-7B-Instruct---share the Qwen2ForCausalLM architecture.
37	The cross-training-paradigm replication (\S\ref{sec:cross-model}) suggests that the findings are not artifacts of a single model's weights, though both models share the same Qwen2ForCausalLM architecture.
38	Cross-architecture validation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, $n{=}250$, \S\ref{sec:cross-arch}, Appendix~\ref{app:cross-arch}) confirms qualitatively consistent within-importance phase gradients ($d_z{=}0.81$--$1.15$; all $p < 10^{-29}$) but a substantially weaker strategy${\times}$phase interaction than in Qwen2-based architectures: random eviction also exhibits significant phase gradients on LLaMA ($d_z{=}0.41$--$0.46$; all $p < 10^{-12}$), reducing the importance/random ratio to $2.0$--$2.6{\times}$ (vs.\ $15$--$17{\times}$ on DeepSeek). The phase gradient direction and dose-response monotonicity are architecture-general; quantitative strategy specificity is architecture-dependent. Comprehensive cross-architecture validation across more diverse designs (e.g., Mistral, multi-latent attention architectures) and scales remains an important next step.
39	
40	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_c8_llama_results_integration_20260516T220519",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-16T22:12:24.038820+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/results.tex",
  "offset": "90",
  "limit": "20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_c8_llama_results_integration_20260516T220519",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/results.tex",
    "offset": "90",
    "limit": "20"
  }
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-16T22:12:24.038959+00:00_

90	\subsection{Cross-Architecture Validation}
91	\label{sec:cross-arch}
92	
93	Cross-architecture validation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, $n{=}250$, MATH-500) supports the generality of phase-modulated compound interaction beyond the Qwen2 architecture family. Under importance-based eviction, the paired median difference $\Delta$ rises monotonically from $0.050$ ($s{=}0.15$) to $0.695$ ($s{=}0.30$), with large effect sizes throughout ($d_z{=}0.81$--$1.15$; all $p < 10^{-29}$; Table~\ref{tab:llama-cross-arch}).
94	
95	A key architectural difference emerges in strategy specificity. On LLaMA, random eviction also exhibits significant phase gradients ($\Delta{=}0.025$--$0.271$; $d_z{=}0.41$--$0.46$; all $p < 10^{-12}$), unlike DeepSeek and Qwen where random is non-significant at $s \leq 0.20$. The importance/random $\Delta$ ratio is $2.0$--$2.6{\times}$ on LLaMA, substantially weaker than the $15$--$17{\times}$ observed on DeepSeek. Dose-response monotonicity holds for both strategies (all conditions monotonic). This indicates that the phase gradient itself is architecture-general, while the degree of strategy specificity is architecture-dependent, likely reflecting differences between GQA (LLaMA, 32 heads with 8 KV groups) and MHA (Qwen2, 28 heads) in how head pruning differentially disrupts importance scoring.
96	
97	Absolute interaction magnitudes are approximately $7$--$12{\times}$ smaller than Qwen2-family models at matched sparsity, consistent with architecture-specific attention head specialization patterns. Full per-condition breakdowns appear in Appendix~\ref{app:cross-arch}.
98	
99	\subsection{Scale Analysis: Qwen2.5-14B}
100	\label{sec:scale-14b}
101	
102	To assess whether phase-modulated severity persists at larger model scale within the same architecture family, we evaluate Qwen2.5-14B-Instruct on MATH-500 ($n{=}500$) at $s \in \{0.15, 0.20, 0.25, 0.30\}$.
103	
104	\begin{table}[t]
105	\centering
106	\small
107	\caption{Median of per-p
…[truncated 199 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_c8_llama_results_integration_20260516T220519",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 71 · 2026-05-16T22:12:24.039133+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -n \"—\\|–\" /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/results.tex 2>/dev/null | head -5",
  "description": "Check for em-dash and en-dash in results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_c8_llama_results_integration_20260516T220519",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -n \"—\\|–\" /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/results.tex 2>/dev/null | head -5",
    "description": "Check for em-dash and en-dash in results.tex"
  }
}
```

</details>

---

### Tool result

_source line 72 · 2026-05-16T22:12:24.039260+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_c8_llama_results_integration_20260516T220519",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 73 · 2026-05-16T22:12:24.039386+00:00_

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
  "session": "worker_paper_c8_llama_results_integration_20260516T220519",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/abstract.tex"
  }
}
```

</details>

---

### Tool result

_source line 74 · 2026-05-16T22:12:24.039546+00:00_

1	\begin{abstract}
2	Compound sparsity---simultaneously pruning attention heads and evicting KV cache entries---is essential for efficient LLM inference but produces super-additive quality degradation whose structure is poorly understood.
3	We find that compound sparsity severity is not a fixed constant but an emergent property of the interaction among eviction strategy, reasoning phase, and sparsity level.
4	On DeepSeek-R1-Distill-Qwen-7B (MATH-500), importance-based eviction exhibits a monotonically increasing phase--severity gradient: the paired median difference $\Delta$ rises from $0.39$ at sparsity $s{=}0.15$ to $8.48$ at $s{=}0.30$ (Spearman $\rho{=}1.0$; all Bonferroni-corrected $p < 0.005$).
5	Random eviction develops a detectable gradient only above $s \approx 0.20$, at $2.7$--$17{\times}$ smaller magnitude.
6	The pattern replicates on Qwen2.5-7B-Instruct ($\Delta$: $0.07 \to 3.16$; $\rho{=}1.0$), shows consistent phase gradient direction on GSM8K for both models, and generalizes to LlamaForCausalLM ($n{=}250$; importance phase gradient $d_z{=}0.81$--$1.15$, all $p < 10^{-29}$; strategy specificity architecture-dependent).
7	Per-phase Gini analysis identifies \emph{importance discrimination collapse}---the degeneration of head importance scores toward uniformity under compound stress---as a correlational diagnostic of this severity divergence.
8	Prior work characterizes compound degradation as phase-agnostic; we show that phase modulates severity by $15$--$17{\times}$ on DeepSeek and $2.7$--$3.5{\times}$ on Qwen. These findings establish phase-gated analysis---decomposing compound severity by reasoning phase and eviction strategy---as a principled diagnostic framework, with direct implications for phase-aware budget allocation in inference systems.
9	\end{abstract}
10	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_c8_llama_results_integration_20260516T220519",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 75 · 2026-05-16T22:12:24.039732+00:00_

All updates complete. Here's a summary of changes made across 5 files:

**Files modified:**
1. `artifacts/_project/paper/results.tex` (§5.5) — Rewrote cross-architecture section with c8_llama_n250_fixed data: Δ=0.050→0.695, d_z=0.81-1.15 for importance; Δ=0.025→0.271, d_z=0.41-0.46 for random; imp/rand ratio 2.0-2.6×. Changed "confirms" to "supports".

2. `artifacts/_project/paper/appendix_moved.tex` (Appendix G) — Replaced old table (per-phase II with Low/High ratios) with new table showing Δ, d_z, and p-values for all 8 conditions. Updated narrative to reflect weaker strategy specificity and significant random gradients.

3. `artifacts/_project/paper/introduction.tex` — Updated two references: paragraph text (line 15) and contribution bullet (line 26) now report d_z=0.81-1.15 and ratio 2.0-2.6× instead of old "15-33× gradient ratio".

4. `artifacts/_project/paper/abstract.tex` — Updated LLaMA claim to "importance phase gradient d_z=0.81-1.15, all p<10^{-29}; strategy specificity architecture-dependent".

5. `artifacts/_project/paper/conclusion.tex` — Updated LLaMA summary from "gradient ratio 15-33× confirms" to "d_z=0.81-1.15 supports; strategy specificity architecture-dependent (2.0-2.6×)".

6. `artifacts/_project/paper/appendix_disc_analysis.tex` — Replaced outdated "pilot" language (n=50, only s030 significant) with full n=250 results (all conditions significant).

Key narrative shift: the phase gradient itself is confirmed as architecture-general, but strategy specificity (importance vs random divergence) is now acknowledged as architecture-dependent, which is a more nuanced and accurate claim.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_c8_llama_results_integration_20260516T220519"
}
```

</details>

---
