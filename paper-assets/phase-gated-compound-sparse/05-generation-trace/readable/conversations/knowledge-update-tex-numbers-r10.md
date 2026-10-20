# knowledge update tex numbers r10

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 121
- **Recorded user turns:** 0
- **Tool calls:** 60
- **Original source:** `logs/chats/worker_knowledge_update_tex_numbers_r10_20260516T020339.jsonl`
- **Structured JSON:** [`1b3524d500186c1341f5.json`](../../sessions/1b/1b3524d500186c1341f5.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

121 recorded events

### Tool call

_source line 1 · 2026-05-16T02:10:04.094737+00:00_

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
  "session": "worker_knowledge_update_tex_numbers_r10_20260516T020339",
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

_source line 2 · 2026-05-16T02:10:04.095133+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_knowledge_update_tex_numbers_r10_20260516T020339",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-16T02:10:04.095308+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "phase-gated-compound-sparse",
  "file": "paper_framing.md",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_knowledge_update_tex_numbers_r10_20260516T020339",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "phase-gated-compound-sparse",
    "file": "paper_framing.md",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-16T02:10:04.095653+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/paper_framing.md\", \"content\": \"# Paper Framing — Phase-Gated Compound Sparsity\\n\\n> 最后更新: 2026-05-16 (数值对齐 registry: DS median_diff 恢复 0.32/1.15/3.97/9.94; Cohen's d 改 registry cohens_d 0.61→1.13/0.37→1.44; C7+C10 status→confirmed; imp/rand 2.7-15×) | 维护者: Director\\n\\n## Core Insight\\n\\nCompound sparsity（attention head pruning + KV cache eviction）的 severity 不是固定常数——它是 eviction strategy 和 reasoning phase 交互的涌现属性。Importance-based eviction 的 compound interaction severity（paired median difference: median(II_low_i − II_high_i)）随 sparsity 单调递增（DeepSeek: 0.32→1.15→3.97→9.94; Qwen: 0.048→0.208→1.109→2.619），而 random masking 在 s015/s020 NS，在 s025 跨模型显著但效应量远小于 importance（DS: 0.257 vs 3.986; QW: 0.393 vs 1.074, 2.7-15×差异），存在 sparsity threshold ~s020-s025（D063; s030 待定）。Cohen's d（per-problem paired, B=10000）从 medium 到 large（DeepSeek: 0.61→1.13; Qwen: 0.37→1.44，registry cohens_d s015→s030）。LLaMA 跨架构验证（D060）qualitative direction consistent（within-importance d_z~1.0），但 strategy×phase 交互弱于 Qwen2 架构（imp_vs_rand d_z 0.19→0.34, 仅 s030 显著），且 random 在 LLaMA 上也显示显著 phase gradient（d_z 0.35→0.44），与 DeepSeek/Qwen random 低 sparsity NS 模式定性不同。GSM8K 跨 benchmark 验证（D075）：importance masking 的 phase gradient 在 GSM8K 上同样单调递增（QW: 0.039→0.158→1.100→2.092; DS: 0.241→0.740→1.992→4.682），但 strategy specificity（importance/random gradient ratio）从 MATH-500 的 15-36× 衰减至 GSM8K 的 2.3-3.8×。注意：\\\"反转\\\"仅在原始 II_low 值上（random > importance），phase gradient 层面 importance ≥ random。Strategy specificity 的 task-dependence 机制是开放问题（见 §6 Discussion）。这一发现挑战了 compound degradation 均匀分布的隐含假设。\\n\\n**数字基准**：所有数字基于 bf16 per-problem paired 统计量（B=10000 bootstrap）。median_diff 定义为 median(II_low_i − II_high_i)（逐 problem 配对差的中位数）。fp16 旧数据已弃用。\\n\\n## Narrative Arc\\n\\nCompound sparsity 是高效 LLM 推理的实用部署需求，但 prior work（SparK, Ada-KV, SLiM）将 compound interaction 视为均匀超可加。我们发现 severity 是 stra
…[truncated 11238 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_knowledge_update_tex_numbers_r10_20260516T020339",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-16T02:10:04.095965+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "1\\.15",
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
  "session": "worker_knowledge_update_tex_numbers_r10_20260516T020339",
  "tool": "Grep",
  "tool_args": {
    "pattern": "1\\.15",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-16T02:10:04.096127+00:00_

artifacts/_project/paper/numerical_audit_report.md:130:| 0.20 | 0.52 | 1.15 [0.66, 1.26] | 0.55 | 0.21 [0.07, 0.40] | ✅ |
artifacts/_project/paper/main.log:60:Package: keyval 2022/05/29 v1.15 key=value parser (DPC)
artifacts/_project/paper/main.log:143:Package: pdfescape 2019/12/09 v1.15 Implements pdfTeX's escape features (HO)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_knowledge_update_tex_numbers_r10_20260516T020339",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-16T02:10:04.096274+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "3\\.97",
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
  "session": "worker_knowledge_update_tex_numbers_r10_20260516T020339",
  "tool": "Grep",
  "tool_args": {
    "pattern": "3\\.97",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-16T02:10:04.096433+00:00_

artifacts/_project/paper/numerical_audit_report.md:131:| 0.25 | 0.68 | 3.97 [2.83, 5.29] | 0.89 | 1.11 [0.61, 1.47] | ✅ |
artifacts/_project/paper/appendix_robustness.tex:113:B (head-heavy) & 0.30 & 0.20 & 18.77 & 3.97 & 0.52 & $+$18.25 \\
artifacts/_project/paper/appendix_robustness.tex:115:Symmetric & 0.25 & 0.25 & 3.97 & --- & 0.02 & $+$3.99 \\
artifacts/_project/paper/appendix_robustness.tex:120:[Omitted long matching line]
artifacts/_project/paper/appendix_moved.tex:5:[Omitted long matching line]
artifacts/_project/paper/results.tex:48:0.25 & Importance & 0.021 & 3.971 & 3.99\; $[3.53,\; 4.36]$ & $\mathbf{49.1}$\; $[40.1,\; 57.8]$ \\
artifacts/_project/paper/results.tex:82:[Omitted long matching line]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_knowledge_update_tex_numbers_r10_20260516T020339",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-16T02:10:04.096610+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "9\\.94",
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
  "session": "worker_knowledge_update_tex_numbers_r10_20260516T020339",
  "tool": "Grep",
  "tool_args": {
    "pattern": "9\\.94",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-16T02:10:04.096786+00:00_

artifacts/_project/paper/numerical_audit_report.md:132:| 0.30 | 0.80 | 9.94 [8.39, 16.65] | 1.02 | 2.62 [1.72, 3.65] | ✅ |
artifacts/_project/paper/numerical_audit_report.md:209:Framing constraint values: DS paired 0.32→9.94, QW paired 0.048→2.619 — all present in Tab 6 (cohens-d).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_knowledge_update_tex_numbers_r10_20260516T020339",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-16T02:10:04.096939+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "3--15|3-15|3\\\\\\\\times|3×",
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
  "session": "worker_knowledge_update_tex_numbers_r10_20260516T020339",
  "tool": "Grep",
  "tool_args": {
    "pattern": "3--15|3-15|3\\\\\\\\times|3×",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-16T02:10:04.097071+00:00_

artifacts/_project/paper/numerical_audit_report.md:26:- **Appendix values** (`appendix_results.tex`): 3.9× (s015), 5.4× (s020), 5.3× (s025), **3.6×** (s030)
artifacts/_project/paper/numerical_audit_report.md:87:| G s020 (importance) | 103× | 103.1 | ✅ |
artifacts/_project/paper/numerical_audit_report.md:148:| 0.25 | 5.3× | 7.195958/1.36269 = 5.28 | ✅ |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_knowledge_update_tex_numbers_r10_20260516T020339",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-16T02:10:04.097198+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "3.{0,3}15.*\\\\\\\\times|3.{0,3}15.*×|2\\.7|3--15|3\\\\\\\\text",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
  "output_mode": "content",
  "-n": "True",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_knowledge_update_tex_numbers_r10_20260516T020339",
  "tool": "Grep",
  "tool_args": {
    "pattern": "3.{0,3}15.*\\\\\\\\times|3.{0,3}15.*×|2\\.7|3--15|3\\\\\\\\text",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
    "output_mode": "content",
    "-n": "True",
    "glob": "*.tex"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-16T02:10:04.097333+00:00_

artifacts/_project/paper/appendix_robustness.tex:135:We binarize each token as ``thinking'' (inside \texttt{&lt;think>}) or ``answer'' (outside) and compare against the sparsity-based low/high phase assignment. Cohen's $\kappa{=}0.887$ (median across problems), indicating near-perfect agreement between the data-driven sparsity proxy and the model's explicit reasoning markers. Of thinking tokens, $57.8\%$ fall in the low-sparsity phase; of answer tokens, $62.7\%$ fall in the high-sparsity phase.
artifacts/_project/paper/appendix_moved.tex:98:As a control, random eviction on Qwen mirrors DeepSeek: non-significant at $s \leq 0.20$ ($\Delta$: $-0.01$, $0.02$; CIs span zero) but significant at $s \geq 0.25$ ($\Delta{=}0.39$, $p_{\text{Bonf}} < 10^{-10}$; $\Delta{=}0.91$, $p_{\text{Bonf}} < 10^{-13}$). Where significant, the random phase gradient is $2.7$--$3.5{\times}$ weaker than importance-based ($0.39$ vs.\ $1.07$ at $s{=}0.25$; $0.91$ vs.\ $3.16$ at $s{=}0.30$), confirming strategy-specific amplification.
artifacts/_project/paper/appendix_disc_analysis.tex:53:These effects are genuine but $2.7$--$20{\times}$ weaker than importance-based eviction at the same sparsity levels, consistent with a weak phase gradient that is detectable at sufficient sample size but not the primary driver of compound severity.
artifacts/_project/paper/results.tex:45:0.20 & Importance & 0.008 & 1.211 & 1.21\; $[1.11,\; 1.34]$ & $\mathbf{17.9}$\; $[12.7,\; 26.3]$ \\
artifacts/_project/paper/results.tex:64:0.30 & Importance & 0.014 & 3.208 & 3.16\; $[2.78,\; 3.56]$ & $\mathbf{36.9}$\; $[25.3,\; 49.1]$ \\
artifacts/_project/paper/results.tex:88:[Omitted long matching line]
artifacts/_project/paper/results.tex:117:0.30 & $8.48$\; $[7.75,\; 9.69]$ & $3.16$\; $[2.78,\; 3.56]$ \\

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_knowledge_update_tex_numbers_r10_20260516T020339",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-16T02:10:04.097529+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "d=0\\.28|d\\s*=\\s*0\\.28|0\\.28",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
  "output_mode": "content",
  "-n": "True",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_knowledge_update_tex_numbers_r10_20260516T020339",
  "tool": "Grep",
  "tool_args": {
    "pattern": "d=0\\.28|d\\s*=\\s*0\\.28|0\\.28",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
    "output_mode": "content",
    "-n": "True",
    "glob": "*.tex"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-16T02:10:04.097671+00:00_

artifacts/_project/paper/appendix_disc_analysis.tex:84:0.20 & Random     & 0.143 & 0.423 & 0.28\textsuperscript{ns} & 0.96 \\

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_knowledge_update_tex_numbers_r10_20260516T020339",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-16T02:10:04.097816+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "0\\.32.*1\\.15|1\\.15.*3\\.97|3\\.97.*9\\.94|0\\.32.*9\\.94",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
  "output_mode": "content",
  "-n": "True",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_knowledge_update_tex_numbers_r10_20260516T020339",
  "tool": "Grep",
  "tool_args": {
    "pattern": "0\\.32.*1\\.15|1\\.15.*3\\.97|3\\.97.*9\\.94|0\\.32.*9\\.94",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
    "output_mode": "content",
    "-n": "True",
    "glob": "*.tex"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-16T02:10:04.097935+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_knowledge_update_tex_numbers_r10_20260516T020339",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-16T02:10:04.098049+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "1\\.15|3\\.97|9\\.94",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
  "output_mode": "content",
  "-n": "True",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_knowledge_update_tex_numbers_r10_20260516T020339",
  "tool": "Grep",
  "tool_args": {
    "pattern": "1\\.15|3\\.97|9\\.94",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
    "output_mode": "content",
    "-n": "True",
    "glob": "*.tex"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-16T02:10:04.098169+00:00_

artifacts/_project/paper/appendix_robustness.tex:113:B (head-heavy) & 0.30 & 0.20 & 18.77 & 3.97 & 0.52 & $+$18.25 \\
artifacts/_project/paper/appendix_robustness.tex:115:Symmetric & 0.25 & 0.25 & 3.97 & --- & 0.02 & $+$3.99 \\
artifacts/_project/paper/appendix_robustness.tex:120:[Omitted long matching line]
artifacts/_project/paper/appendix_moved.tex:5:[Omitted long matching line]
artifacts/_project/paper/results.tex:48:0.25 & Importance & 0.021 & 3.971 & 3.99\; $[3.53,\; 4.36]$ & $\mathbf{49.1}$\; $[40.1,\; 57.8]$ \\
artifacts/_project/paper/results.tex:82:[Omitted long matching line]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_knowledge_update_tex_numbers_r10_20260516T020339",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-16T02:10:04.098351+00:00_

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
  "session": "worker_knowledge_update_tex_numbers_r10_20260516T020339",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/results.tex"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-16T02:10:04.098596+00:00_

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
13	\caption{Median compound severity difference ($\Delta = \widetilde{\mathrm{II}}_{\textit{low}} - \widetilde{\mathrm{II}}_{\textit{high}}$) by eviction strategy and sparsity level on DeepSeek-R1-Distill-Qwen-7B ($n{=}496$, 500 MATH-500 problems).}
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
29	Decomposing II by reasoning phase reveals that strategy-dependent severity is driven by amplification in the low-sparsity phase. Table~\ref{tab:main-results} reports the per-phase breakdown at $n{=}496$. The per-problem amplification ratio $G$ (Eq.~\ref{eq:gradient}) increases from $7.5{\times}$ (95\% CI: $[4.1, 11.4]$) at $s{=}0.15$ to $79.8{\times}$ ($[63.3, 96.5]$) at $s{=}0.30$ under imp
…[truncated 12220 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_knowledge_update_tex_numbers_r10_20260516T020339",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-16T02:10:04.098787+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_moved.tex",
  "offset": "1",
  "limit": "20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_knowledge_update_tex_numbers_r10_20260516T020339",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_moved.tex",
    "offset": "1",
    "limit": "20"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-16T02:10:04.098930+00:00_

1	
2	\section{Phase-Strategy Crossover Details}
3	\label{app:crossover-details}
4	
5	On DeepSeek ($n{=}496$), a strategy ranking reversal emerges at $s{=}0.25$ (Figure~\ref{fig:crossover}): importance-based eviction yields \emph{lower} II than random in the high-sparsity phase ($0.021$ vs.\ $1.113$) but \emph{higher} II in the low-sparsity phase ($3.971$ vs.\ $1.514$---a $2.6{\times}$ reversal; both $p < 10^{-4}$). This crossover is confirmed at all four sparsity levels, with reversal magnitude of $4.0{\times}$ at $s{=}0.15$, $3.4{\times}$ at $s{=}0.20$, $2.6{\times}$ at $s{=}0.25$, and $2.2{\times}$ at $s{=}0.30$ (decreasing as random eviction severity rises). The reversal arises because head pruning redistributes attention mass, altering importance rankings in a way that couples the two sparsity mechanisms in low-sparsity phases (\S\ref{sec:discrimination-collapse-main}). Qwen does not exhibit a crossover: importance-based eviction produces lower II than random in both phases across all sparsity levels (e.g., at $s{=}0.25$: high $0.004$ vs.\ $1.108$; low $1.053$ vs.\ $1.769$).
6	
7	\begin{figure}[t]
8	\centering
9	\includegraphics[width=\columnwidth]{fig3_crossover.pdf}
10	\caption{Strategy-dependent crossover at $s{=}0.25$ on DeepSeek ($n{=}496$). Grouped bar chart of median II by eviction strategy and reasoning phase. Importance-based eviction outperforms random in the high-sparsity phase but produces $2.6{\times}$ higher II in the low-sparsity phase, reversing the strategy ranking.}
11	\label{fig:crossover}
12	\end{figure}
13	
14	
15	\section{Profiling Subset Per-Phase Breakdown}
16	\label{app:profiling-subset}
17	
18	\begin{table*}[t]
19	\centering
20	\small

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_knowledge_update_tex_numbers_r10_20260516T020339",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-16T02:10:04.099070+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_moved.tex",
  "offset": "80",
  "limit": "40"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_knowledge_update_tex_numbers_r10_20260516T020339",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_moved.tex",
    "offset": "80",
    "limit": "40"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-16T02:10:04.099222+00:00_

80	\midrule
81	DeepSeek-R1-Distill-Qwen-7B ($n{=}496$) & 0.39 & 1.21 & 3.99 & 8.48 \\
82	Qwen2.5-7B-Instruct ($n{=}475$)         & 0.07 & 0.31 & 1.07 & 3.16 \\
83	\bottomrule
84	\end{tabular}
85	\end{table}
86	
87	\begin{figure}[t]
88	\centering
89	\includegraphics[width=\columnwidth]{fig5_crossmodel.pdf}
90	\caption{Cross-training-paradigm comparison of the median severity difference under importance-based eviction ($n{=}496$/$475$). Both DeepSeek (solid) and Qwen (dashed) exhibit monotonically increasing $\Delta$ with sparsity; Qwen's magnitude is approximately one-quarter to one-sixth of DeepSeek's.}
91	\label{fig:cross-model}
92	\end{figure}
93	
94	\paragraph{Per-problem concordance.}
95	The per-problem concordance across models is not significant (mean $\rho = -0.107$, $p = 0.926$), indicating that while the aggregate gradient direction replicates, the specific problems driving severity differ between models---consistent with model-specific attention patterns rather than a universal per-problem vulnerability ranking.
96	
97	\paragraph{Random eviction control.}
98	As a control, random eviction on Qwen mirrors DeepSeek: non-significant at $s \leq 0.20$ ($\Delta$: $-0.01$, $0.02$; CIs span zero) but significant at $s \geq 0.25$ ($\Delta{=}0.39$, $p_{\text{Bonf}} < 10^{-10}$; $\Delta{=}0.91$, $p_{\text{Bonf}} < 10^{-13}$). Where significant, the random phase gradient is $2.7$--$3.5{\times}$ weaker than importance-based ($0.39$ vs.\ $1.07$ at $s{=}0.25$; $0.91$ vs.\ $3.16$ at $s{=}0.30$), confirming strategy-specific amplification.
99	
100	
101	\section{Permutation Test Details}
102	\label{app:permutation-details}
103	
104	For each problem $i$ and sparsity level $s$, we compute the compound severity difference $\Delta_i^{(\text{strat})} = \mathrm{II}_{\textit{low},i} - \mathrm{II}_{\textit{high},i}$ under each eviction strategy. The test statistic is the median of the paired difference $\widetilde{\Delta} = \text{median}_i\!\bigl(\Delta_i^{(\text{imp})} - \Delta_i^{
…[truncated 2016 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_knowledge_update_tex_numbers_r10_20260516T020339",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-16T02:10:04.099365+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_robustness.tex",
  "offset": "100",
  "limit": "40"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_knowledge_update_tex_numbers_r10_20260516T020339",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_robustness.tex",
    "offset": "100",
    "limit": "40"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-16T02:10:04.099548+00:00_

100	
101	Our main experiments use symmetric sparsity ($s_{\text{head}} = s_{\text{KV}} = s$). To verify that the phase-gated severity gradient does not depend on this symmetric assumption, we evaluate two asymmetric configurations at a fixed total sparsity budget equivalent to $s{=}0.25$, using importance-based eviction on DeepSeek-R1-Distill-Qwen-7B.
102	
103	\begin{table}[h]
104	\centering
105	\small
106	\caption{Asymmetric sparsity robustness: per-phase II under two head/KV allocations (DeepSeek, importance-based eviction, $n{=}50$ spot check).}
107	\label{tab:asymmetric-robust}
108	\begin{tabular}{@{}lcccccc@{}}
109	\toprule
110	Config & $s_{\text{head}}$ & $s_{\text{KV}}$ & $\widetilde{\mathrm{II}}_{\textit{low}}$ & $\widetilde{\mathrm{II}}_{\textit{mid}}$ & $\widetilde{\mathrm{II}}_{\textit{high}}$ & $\Delta$ \\
111	\midrule
112	A (KV-heavy) & 0.20 & 0.30 & 19.51 & 6.05 & 0.38 & $+$19.13 \\
113	B (head-heavy) & 0.30 & 0.20 & 18.77 & 3.97 & 0.52 & $+$18.25 \\
114	\addlinespace
115	Symmetric & 0.25 & 0.25 & 3.97 & --- & 0.02 & $+$3.99 \\
116	\bottomrule
117	\end{tabular}
118	\end{table}
119	
120	Both asymmetric configurations produce large positive $\Delta$ ($+19.13$ and $+18.25$), confirming that the phase-gated severity gradient is robust to the head/KV allocation ratio. The KV-heavy configuration (A) exhibits higher mid-phase II ($6.05$ vs.\ $3.97$), suggesting that the KV eviction axis has a stronger impact on intermediate reasoning phases. Both asymmetric $\Delta$ values exceed the symmetric baseline ($3.99$), consistent with one axis operating at $s{=}0.30$---above the symmetric maximum tested---which amplifies overall severity. A systematic investigation of the full asymmetric interaction surface is left for future work.
121	
122	
123	\section{Outlier Robustness Analysis}
124	\label{app:outlier-robustness}
125	
126	The extreme mean/median ratio (up to $97{,}640{:}1$ in individual conditions) reflects heavy-tailed II distributions driven by near-zero denom
…[truncated 2261 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_knowledge_update_tex_numbers_r10_20260516T020339",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-16T02:10:04.099731+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "0\\.32",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
  "output_mode": "content",
  "-n": "True",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_knowledge_update_tex_numbers_r10_20260516T020339",
  "tool": "Grep",
  "tool_args": {
    "pattern": "0\\.32",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
    "output_mode": "content",
    "-n": "True",
    "glob": "*.tex"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-16T02:10:04.099893+00:00_

artifacts/_project/paper/appendix_robustness.tex:53:QW & Imp & 0.20 & 0.307 & 0.307 & 0.325 & 475 & 289 \\

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_knowledge_update_tex_numbers_r10_20260516T020339",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-16T02:10:04.100021+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "1\\.13|3\\.96|9\\.97",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
  "output_mode": "content",
  "-n": "True",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_knowledge_update_tex_numbers_r10_20260516T020339",
  "tool": "Grep",
  "tool_args": {
    "pattern": "1\\.13|3\\.96|9\\.97",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
    "output_mode": "content",
    "-n": "True",
    "glob": "*.tex"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-16T02:10:04.100142+00:00_

artifacts/_project/paper/appendix_robustness.tex:89:& 0.25 & 1.074 & 1.870\; $[1.05,\; 2.44]$ & 1.801\; $[1.13,\; 2.38]$ \\

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_knowledge_update_tex_numbers_r10_20260516T020339",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-16T02:10:04.100676+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "0\\.61.*1\\.13|0\\.37.*1\\.44|cohens.*d",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
  "output_mode": "content",
  "-n": "True",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_knowledge_update_tex_numbers_r10_20260516T020339",
  "tool": "Grep",
  "tool_args": {
    "pattern": "0\\.61.*1\\.13|0\\.37.*1\\.44|cohens.*d",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
    "output_mode": "content",
    "-n": "True",
    "glob": "*.tex"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-16T02:10:04.100844+00:00_

artifacts/_project/paper/appendix_disc_analysis.tex:50:[Omitted long matching line]
artifacts/_project/paper/results.tex:103:[Omitted long matching line]
artifacts/_project/paper/results.tex:109:\label{tab:cohens-d}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_knowledge_update_tex_numbers_r10_20260516T020339",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-16T02:10:04.101020+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "0\\.32.*to.*9\\.|0\\.32.*arrow|\\\\$0\\.32\\\\$|0\\.32→",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
  "output_mode": "content",
  "-n": "True",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_knowledge_update_tex_numbers_r10_20260516T020339",
  "tool": "Grep",
  "tool_args": {
    "pattern": "0\\.32.*to.*9\\.|0\\.32.*arrow|\\\\$0\\.32\\\\$|0\\.32→",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
    "output_mode": "content",
    "-n": "True",
    "glob": "*.tex"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-16T02:10:04.101151+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_knowledge_update_tex_numbers_r10_20260516T020339",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-16T02:10:04.101278+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Search .tex files for old values",
  "prompt": "Search all .tex files under `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/` for ANY occurrence of these specific old values that need to be updated. Report the file, line number, and surrounding context for each match.\n\nValues to search for:\n1. `1.15` (DS dose curve s020 value) - but NOT in main.log\n2. `3.97` (DS dose curve s025 value) - but only when it represents the DS dose curve paired median difference, NOT when it's a raw II value in a table  \n3. `9.94` (DS dose curve s030 value)\n4. Any \"3--15\" or \"3-15\" or similar pattern representing a \"3 to 15\" ratio range (imp/rand ratio lower bound should be 2.7, not 3)\n5. `d=0.28` or `0.28` in the context of Cohen's d for Qwen s015\n6. `0.39` at s=0.15 when describing DS dose curve (this might need to be 0.32)\n7. Any text pattern like \"from X to Y\" or \"X→Y\" that describes the DS dose-response going through the four sparsity levels\n\nAlso read abstract.tex, introduction.tex, discussion.tex, conclusion.tex, analysis.tex, appendix.tex, appendix_disc_analysis.tex fully to find any prose mentions of these values.\n\nReport exhaustively every occurrence found.",
  "subagent_type": "Explore"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_knowledge_update_tex_numbers_r10_20260516T020339",
  "tool": "Agent",
  "tool_args": {
    "description": "Search .tex files for old values",
    "prompt": "Search all .tex files under `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/` for ANY occurrence of these specific old values that need to be updated. Report the file, line number, and surrounding context for each match.\n\nValues to search for:\n1. `1.15` (DS dose curve s020 value) - but NOT in main.log\n2. `3.97` (DS dose curve s025 value) - but only when it represents the DS dose curve paired median difference, NOT when it's a raw II value in a table  \n3. `9.94` (DS dose curve s030 value)\n4. Any \"3--15\" or \"3-15\" or similar pattern representing a \"3 to 15\" ratio range (imp/rand ratio lower bound should be 2.7, not 3)\n5. `d=0.28` or `0.28` in the context of Cohen's d for Qwen s015\n6. `0.39` at s=0.15 when describing DS dose curve (this might need to be 0.32)\n7. Any text pattern like \"from X to Y\" or \"X→Y\" that describes the DS dose-response going through the four sparsity levels\n\nAlso read abstract.tex, introduction.tex, discussion.tex, conclusion.tex, analysis.tex, appendix.tex, appendix_disc_analysis.tex fully to find any prose mentions of these values.\n\nReport exhaustively every occurrence found.",
    "subagent_type": "Explore"
  }
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-16T02:10:04.101488+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper -name \"*.tex\" -type f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_knowledge_update_tex_numbers_r10_20260516T020339",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper -name \"*.tex\" -type f"
  }
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-16T02:10:04.101634+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/results.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_disc_analysis.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/background.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/methodology.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_moved.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_robustness.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/analysis.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_knowledge_update_tex_numbers_r10_20260516T020339",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-16T02:10:04.101782+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "1\\.15",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
  "type": "tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_knowledge_update_tex_numbers_r10_20260516T020339",
  "tool": "Grep",
  "tool_args": {
    "pattern": "1\\.15",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
    "type": "tex",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-16T02:10:04.102074+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_knowledge_update_tex_numbers_r10_20260516T020339",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-16T02:10:04.102213+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "3\\.97",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
  "type": "tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_knowledge_update_tex_numbers_r10_20260516T020339",
  "tool": "Grep",
  "tool_args": {
    "pattern": "3\\.97",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
    "type": "tex",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-16T02:10:04.102334+00:00_

artifacts/_project/paper/appendix_robustness.tex:113:B (head-heavy) & 0.30 & 0.20 & 18.77 & 3.97 & 0.52 & $+$18.25 \\
artifacts/_project/paper/appendix_robustness.tex:115:Symmetric & 0.25 & 0.25 & 3.97 & --- & 0.02 & $+$3.99 \\
artifacts/_project/paper/appendix_robustness.tex:120:[Omitted long matching line]
artifacts/_project/paper/appendix_moved.tex:5:[Omitted long matching line]
artifacts/_project/paper/results.tex:48:0.25 & Importance & 0.021 & 3.971 & 3.99\; $[3.53,\; 4.36]$ & $\mathbf{49.1}$\; $[40.1,\; 57.8]$ \\
artifacts/_project/paper/results.tex:82:[Omitted long matching line]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_knowledge_update_tex_numbers_r10_20260516T020339",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-16T02:10:04.102486+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "9\\.94",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
  "type": "tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_knowledge_update_tex_numbers_r10_20260516T020339",
  "tool": "Grep",
  "tool_args": {
    "pattern": "9\\.94",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
    "type": "tex",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-16T02:10:04.102606+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_knowledge_update_tex_numbers_r10_20260516T020339",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-16T02:10:04.102727+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "3[--]15|3-15",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
  "type": "tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_knowledge_update_tex_numbers_r10_20260516T020339",
  "tool": "Grep",
  "tool_args": {
    "pattern": "3[--]15|3-15",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
    "type": "tex",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-16T02:10:04.102840+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_knowledge_update_tex_numbers_r10_20260516T020339",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-16T02:10:04.102967+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "d=0\\.28|d = 0\\.28",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
  "type": "tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_knowledge_update_tex_numbers_r10_20260516T020339",
  "tool": "Grep",
  "tool_args": {
    "pattern": "d=0\\.28|d = 0\\.28",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
    "type": "tex",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-16T02:10:04.103094+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_knowledge_update_tex_numbers_r10_20260516T020339",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-16T02:10:04.103214+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "0\\.28",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
  "type": "tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_knowledge_update_tex_numbers_r10_20260516T020339",
  "tool": "Grep",
  "tool_args": {
    "pattern": "0\\.28",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
    "type": "tex",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-16T02:10:04.103326+00:00_

artifacts/_project/paper/appendix_disc_analysis.tex:84:0.20 & Random     & 0.143 & 0.423 & 0.28\textsuperscript{ns} & 0.96 \\

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_knowledge_update_tex_numbers_r10_20260516T020339",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 52 · 2026-05-16T02:10:04.103465+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "0\\.32",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
  "type": "tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_knowledge_update_tex_numbers_r10_20260516T020339",
  "tool": "Grep",
  "tool_args": {
    "pattern": "0\\.32",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
    "type": "tex",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 53 · 2026-05-16T02:10:04.103581+00:00_

artifacts/_project/paper/appendix_robustness.tex:53:QW & Imp & 0.20 & 0.307 & 0.307 & 0.325 & 475 & 289 \\

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_knowledge_update_tex_numbers_r10_20260516T020339",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 54 · 2026-05-16T02:10:04.103705+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "from.*to|→|dose.*curve|sparsity",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
  "type": "tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_knowledge_update_tex_numbers_r10_20260516T020339",
  "tool": "Grep",
  "tool_args": {
    "pattern": "from.*to|→|dose.*curve|sparsity",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
    "type": "tex",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 55 · 2026-05-16T02:10:04.103920+00:00_

&lt;persisted-output>
Output too large (19.9KB). Full output saved to: /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-phase-gated-compound-sparse/dc0135ec-faf8-442a-970d-d96f910518d8/tool-results/toolu_01AtaQUcjdWJsmGGWagbTCus.txt

Preview (first 2KB):
artifacts/_project/paper/analysis.tex:11:This pattern---\emph{importance discrimination collapse}---reflects eviction degenerating into noise-sensitive selection as score distributions approach uniformity. The effect is phase-dependent: low-sparsity phases have broadly distributed attention where collapse has maximum impact; high-sparsity phases preserve concentration. \cite{hies-2025} report this collapse under single-axis pruning; we extend it to the compound setting.
artifacts/_project/paper/analysis.tex:13:[Omitted long matching line]
artifacts/_project/paper/related_work.tex:6:\cite{spark-aaai2026} report super-additive degradation when combining channel pruning with token eviction; \cite{slim-icml2025} formalize compound error for quantization and sparsity.
artifacts/_project/paper/related_work.tex:12:\cite{kim2026pqqp} show that compression order (prune-then-quantize vs.\ quantize-then-prune) significantly affects joint quality, and their Progressive Intensity Hypothesis---that weaker perturbations should precede stronger ones---echoes our dose-response finding that interaction severity increases monotonically with sparsity.
artifacts/_project/paper/related_work.tex:25:\cite{physics-kvcache-2026} identify a sharp phase transition in single-axis KV cache compression at high sparsity, characterizing the single-dimension failure mode that our compound analysis extends across multiple axes.
artifacts/_project/paper/conclusion.tex:4:[Omitted long matching line]
artifacts/_project/paper/discussion.tex:5:[Omitted long matching line]
artifacts/_project/paper/appendix_robustness.tex:17:Adjacent sparsity ($k{=}12$) & 10 & 1 \\
artifacts/_project/paper/appendix_robustness.te
…[truncated 138 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_knowledge_update_tex_numbers_r10_20260516T020339",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 56 · 2026-05-16T02:10:04.104095+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "2\\.7|imp.*rand|ratio",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
  "type": "tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_knowledge_update_tex_numbers_r10_20260516T020339",
  "tool": "Grep",
  "tool_args": {
    "pattern": "2\\.7|imp.*rand|ratio",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
    "type": "tex",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 57 · 2026-05-16T02:10:04.104248+00:00_

artifacts/_project/paper/analysis.tex:4:[Omitted long matching line]
artifacts/_project/paper/analysis.tex:11:This pattern---\emph{importance discrimination collapse}---reflects eviction degenerating into noise-sensitive selection as score distributions approach uniformity. The effect is phase-dependent: low-sparsity phases have broadly distributed attention where collapse has maximum impact; high-sparsity phases preserve concentration. \cite{hies-2025} report this collapse under single-axis pruning; we extend it to the compound setting.
artifacts/_project/paper/analysis.tex:13:[Omitted long matching line]
artifacts/_project/paper/related_work.tex:9:GRASPrune~\cite{graspune-acl2026} learns global budget-constrained gates for joint pruning but treats decisions as static across generation.
artifacts/_project/paper/related_work.tex:10:PM-KVQ~\cite{pmkvq-iclr2026} demonstrates that progressive quantization---gradually reducing bit-width over the generation process---mitigates cumulative error in long-CoT reasoning, implicitly introducing a temporal dimension to compression severity that resonates with our finding that compound interaction is phase-dependent.
artifacts/_project/paper/related_work.tex:14:These works establish compound interaction but share an implicit assumption: interaction magnitude is constant across the generation process.
artifacts/_project/paper/related_work.tex:24:\cite{doing-more-with-less-2026} show pruning combined with test-time scaling can exceed unpruned baselines; \cite{sparse-frontier-2025} find no universally optimal sparse attention strategy across generation stages.
artifacts/_project/paper/conclusion.tex:4:[Omitted long matching line]
artifacts/_project/paper/appendix_robustness.tex:31:[Omitted long matching line]
artifacts/_project/paper/appendix_robustness.tex:101:Our main experiments use symmetric sparsity ($s_{\text{head}} = s_{\text{KV}} = s$). To verify that the phase-gated severity gradient does not depend on this symmetric assum
…[truncated 11797 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_knowledge_update_tex_numbers_r10_20260516T020339",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 58 · 2026-05-16T02:10:04.104391+00:00_

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
  "session": "worker_knowledge_update_tex_numbers_r10_20260516T020339",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/abstract.tex"
  }
}
```

</details>

---

### Tool result

_source line 59 · 2026-05-16T02:10:04.104545+00:00_

1	\begin{abstract}
2	Compound sparsity---simultaneously pruning attention heads and evicting KV cache entries---is essential for efficient LLM inference but produces super-additive quality degradation whose structure is poorly understood.
3	We show that compound severity is not phase-invariant: it is an emergent phase-strategy interaction with amplification ratios $G{=}7.5$--$79.8{\times}$ across reasoning phases in 7B-scale mathematical reasoning models.
4	
5	On DeepSeek-R1-Distill-Qwen-7B (MATH-500, $n{=}496$), importance-based eviction produces a monotonically increasing severity gradient (median $\Delta$: $0.39 \to 8.48$; all $p \ll 10^{-10}$). Random eviction is $3$--$17{\times}$ weaker where significant ($s \geq 0.25$), with a strategy ranking crossover at $s{=}0.25$.
6	The pattern replicates on Qwen2.5-7B-Instruct ($n_{\text{eff}}{=}475$, $\Delta$: $0.07 \to 3.16$; all $p < 10^{-14}$), with exploratory cross-architecture evidence from a LlamaForCausalLM model ($n{=}49$; ${\sim}1/40$ effect size) suggesting the qualitative pattern may extend beyond Qwen2 (\S\ref{sec:cross-arch}).
7	We present \emph{importance discrimination collapse}---the degeneration of head importance scores toward uniformity under compound stress---as a correlational diagnostic: both strategies exhibit near-identical Gini drops, yet severity diverges by $15$--$17{\times}$, implicating the structural specificity of importance-based pruning as the key differentiator.
8	These findings establish the phase-dependent nature of compound severity as a diagnostic foundation for future phase-aware mitigation strategies.
9	\end{abstract}
10	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_knowledge_update_tex_numbers_r10_20260516T020339",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 60 · 2026-05-16T02:10:04.104687+00:00_

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
  "session": "worker_knowledge_update_tex_numbers_r10_20260516T020339",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 61 · 2026-05-16T02:10:04.104894+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Long-context language models place acute pressure on the key--value (KV) cache, which grows linearly with sequence length \cite{kwon-sosp2023, pope-mlsys2023}.
5	Two complementary responses---\emph{attention head pruning} \cite{voita-acl2019, michel-neurips2019} and \emph{KV cache eviction} \cite{snapkv-neurips2024, adakv-neurips2025}---can be deployed simultaneously as \emph{compound sparsity}, but the resulting quality degradation is often super-additive \cite{spark-aaai2026, slim-icml2025}. Recent evaluations confirm that reasoning capabilities degrade disproportionately under compound compression \cite{unicomp-2026}, and that per-dimension safe zones intersect to form a smaller joint safe region \cite{phase-transition-compression-2026}.
6	
7	Prior work treats compound interaction magnitude as roughly constant across generation \cite{spark-aaai2026, unicomp-2026}, despite evidence that pruning sensitivity depends on representational phase \cite{decision-repr-transition-2026} and that no single sparse attention strategy dominates across generation stages \cite{sparse-frontier-2025}.
8	This assumption is problematic for reasoning models, whose generations alternate between broadly distributed attention (exploratory reasoning) and sharply concentrated attention (structured computation) \cite{thinkv-iclr2026}.
9	Phase-aware methods like ThinKV \cite{thinkv-iclr2026} apply different KV strategies per phase but without considering compound interaction, while importance-based eviction itself faces challenges from greedy bias \cite{greedy-bias-kvcache-2026}, deferred importance \cite{retentivekv-2026}, and temporal dynamics in long generations \cite{lethe-aaai2026}. These methods each optimize a single pruning axis; we characterize the interaction when multiple mechanisms are composed.
10	If compound severity varies across these phases, a uniform sparsity budget may be safe in one phase yet destructive in another.

…[truncated 3857 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_knowledge_update_tex_numbers_r10_20260516T020339",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 62 · 2026-05-16T02:10:04.105133+00:00_

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
  "session": "worker_knowledge_update_tex_numbers_r10_20260516T020339",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/discussion.tex"
  }
}
```

</details>

---

### Tool result

_source line 63 · 2026-05-16T02:10:04.105321+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Implications for deployment.}
5	A uniform compression budget implicitly accepts order-of-magnitude severity penalties during low-sparsity reasoning phases. Pilot evaluation (Appendix~\ref{app:pilot-mitigation}) achieved 18\% recovery, below the pre-registered 30\% gate, suggesting that effective phase-aware allocation requires finer phase boundary estimation than current proxies provide. Additional mechanisms (e.g., strategy switching, adaptive thresholding) warrant investigation. We expect qualitatively similar behavior for other attention-mass-based scoring methods (H$_2$O \cite{h2o-neurips2023}, SnapKV \cite{snapkv-neurips2024}, PyramidKV \cite{pyramidkv-colm2025}), though quantitative magnitudes may differ. Extended discussion in Appendix~\ref{app:extended-discussion}.
6	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_knowledge_update_tex_numbers_r10_20260516T020339",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 64 · 2026-05-16T02:10:04.105560+00:00_

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
  "session": "worker_knowledge_update_tex_numbers_r10_20260516T020339",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/conclusion.tex"
  }
}
```

</details>

---

### Tool result

_source line 65 · 2026-05-16T02:10:04.105760+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We showed that compound sparsity severity is not phase-invariant but exhibits an emergent phase-strategy interaction. Under importance-based eviction, the paired median difference $\Delta$ increases from $0.39$ to $8.48$ (DeepSeek, $n{=}496$) and $0.07$ to $3.16$ (Qwen, $n{=}475$), all $p < 10^{-13}$, with amplification ratios $G{=}7.5$--$79.8{\times}$. Random eviction is $3$--$17{\times}$ weaker where both strategies are significant ($s \geq 0.25$). A model-dependent crossover on DeepSeek demonstrates that no single strategy dominates uniformly. Importance discrimination collapse provides a correlational diagnostic: despite near-identical Gini drops, severity diverges by $15$--$17{\times}$, implicating the structural specificity of importance-based pruning.
5	These findings establish compound severity as phase-dependent, providing a diagnostic foundation for future phase-aware mitigation. Future work could explore whether these patterns generalize to other reasoning domains, provide causal validation of importance discrimination collapse, and systematically characterize asymmetric compound interactions.
6	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_knowledge_update_tex_numbers_r10_20260516T020339",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 66 · 2026-05-16T02:10:04.105973+00:00_

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
  "session": "worker_knowledge_update_tex_numbers_r10_20260516T020339",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/analysis.tex"
  }
}
```

</details>

---

### Tool result

_source line 67 · 2026-05-16T02:10:04.106187+00:00_

1	\section{Importance Discrimination Collapse under Compound Sparsity}
2	\label{sec:analysis}
3	
4	The mechanisms discussed here are \emph{correlational diagnostics} that illuminate but do not fully explain the $15$--$17{\times}$ severity divergence between strategies. Both strategies exhibit near-identical Gini drops ($<10\%$ difference), yet severity diverges by $15$--$17{\times}$---an order-of-magnitude mismatch indicating that aggregate concentration collapse alone is insufficient. The critical differentiator is \emph{structural specificity} of importance-based pruning, which systematically removes high-attention-score heads (\S\ref{sec:discrimination-collapse-main}).
5	
6	\subsection{Importance Discrimination Collapse}
7	\label{sec:discrimination-collapse-main}
8	
9	Head pruning systematically reduces the discriminative power of cumulative importance scores, suggesting a mechanism for the phase-strategy interaction. The Gini coefficient decreases by $0.030$--$0.081$ (DeepSeek, $6$--$17\%$ relative to dense baseline) and $0.010$--$0.020$ (Qwen, $2$--$4\%$) after pruning, with consistent negative deltas in all 16 conditions (Appendix~\ref{app:analysis}, Table~\ref{tab:discrimination-metrics-full}). Random eviction shows near-identical Gini drops (e.g., DeepSeek $s{=}0.25$: $-0.065$ vs.\ $-0.060$), confirming that collapse is a consequence of head pruning \emph{per se}. Yet importance-based severity is $15$--$17{\times}$ larger---the amplification arises because importance-based eviction \emph{depends on} the very scores that pruning degrades.
10	
11	This pattern---\emph{importance discrimination collapse}---reflects eviction degenerating into noise-sensitive selection as score distributions approach uniformity. The effect is phase-dependent: low-sparsity phases have broadly distributed attention where collapse has maximum impact; high-sparsity phases preserve concentration. \cite{hies-2025} report this collapse under single-axis pruning; we extend it to the compo
…[truncated 1582 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_knowledge_update_tex_numbers_r10_20260516T020339",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 68 · 2026-05-16T02:10:04.106438+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_disc_analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_knowledge_update_tex_numbers_r10_20260516T020339",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_disc_analysis.tex"
  }
}
```

</details>

---

### Tool result

_source line 69 · 2026-05-16T02:10:04.106719+00:00_

1	\section{Importance Discrimination Collapse Details}
2	\label{app:discrimination-collapse-details}
3	
4	This cross-model consistency (Table~\ref{tab:discrimination-metrics-full}) establishes importance discrimination collapse as a robust consequence of compound sparsity. When importance scores lose discriminative power, thresholding the bottom-$s$ fraction becomes noise-sensitive: small perturbations change which positions cross the eviction boundary. In the limit of perfectly uniform scores, importance-based eviction degenerates into an arbitrary selection functionally equivalent to biased random eviction. The same pattern holds under random eviction (DeepSeek: $-0.031$ to $-0.071$; Qwen: $-0.019$ to $-0.046$), confirming that importance discrimination collapse is a consequence of head pruning \emph{per se}, not of the eviction strategy.
5	
6	
7	\section{Extended Discussion}
8	\label{app:extended-discussion}
9	
10	\paragraph{On the predictability of phase-modulated severity.}
11	The compound interaction is not uniformly fragile---it is selectively fragile in a phase-dependent manner ($\widetilde{\mathrm{II}}_{\text{high}} < 0.06$ at $s \leq 0.30$).
12	
13	\paragraph{Random masking as falsification control.}
14	At $n{=}500$, random eviction develops a detectable but weak phase gradient above $s \approx 0.20$: non-significant at $s \leq 0.20$ for both models, but significant at $s \geq 0.25$ (DS: $\Delta{=}0.26$--$0.51$, $p_{\text{Bonf}} < 0.006$; QW: $\Delta{=}0.39$--$0.91$, $p_{\text{Bonf}} < 10^{-10}$). Where significant, the random phase gradient is $3$--$17{\times}$ weaker than importance-based (restricted to conditions where both strategies are significant, $s \geq 0.25$), confirming that the dominant amplification is strategy-specific.
15	
16	\paragraph{Entropy mechanism boundary conditions.}
17	Directly measuring per-head entropy shifts across architecturally distinct models---and identifying what training-time properties determine whether entropy concentra
…[truncated 13583 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_knowledge_update_tex_numbers_r10_20260516T020339",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 70 · 2026-05-16T02:10:04.106944+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_knowledge_update_tex_numbers_r10_20260516T020339",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix.tex"
  }
}
```

</details>

---

### Tool result

_source line 71 · 2026-05-16T02:10:04.107150+00:00_

1	\section{Compound Sparsity Formulation}
2	\label{app:formulation-details}
3	
4	\paragraph{Attention head pruning.}
5	Heads are ranked by Frobenius norm importance $w_j^{(\ell)} = \|\mathbf{A}_j^{(\ell)}\|_F$ \cite{voita-acl2019, michel-neurips2019}; a binary mask $m_j^{(\ell)} \in \{0,1\}$ retains the top-$(1{-}s)\cdot H$ heads:
6	\begin{equation}
7	    \tilde{\mathbf{o}}_j^{(\ell)} = m_j^{(\ell)} \cdot \mathbf{o}_j^{(\ell)}.
8	    \label{eq:head-mask}
9	\end{equation}
10	
11	\paragraph{KV cache eviction.}
12	A position mask $\mathbf{m}_k \in \{0,1\}^T$ retains the top-$(1{-}s)\cdot T$ positions (BOS always preserved):
13	\begin{equation}
14	    \tilde{a}_{ij} = a_{ij} \cdot m_{k,j}, \quad \forall\, i, j.
15	    \label{eq:kv-mask}
16	\end{equation}
17	Under importance-based eviction, each position $j$ is scored by its cumulative attention mass with position normalization:
18	\begin{equation}
19	    \mathrm{imp}(j) = \frac{\sum_{\ell, h, i} a_{ij}^{(\ell,h)}}{T - j},
20	    \label{eq:kv-importance}
21	\end{equation}
22	where the denominator compensates for causal bias---earlier positions are attended to by more queries \cite{thinkv-iclr2026, defensivekv-iclr2026}. Under random eviction, positions (excluding BOS) are evicted uniformly at random.
23	
24	\paragraph{Compound sparsity.}
25	Applying both mechanisms simultaneously yields compound sparsity. The two axes interact: head pruning redistributes attention mass, altering the importance ranking for KV eviction. Prior work \cite{spark-aaai2026} reports super-additive joint effects but treats interaction magnitude as a fixed property of $s$.
26	
27	\paragraph{Attention sparsity metric.}
28	For each query position $i$ and head $h$, we compute the fraction of key positions receiving negligible attention:
29	\begin{equation}
30	    \sigma_i^{(h)} = \frac{1}{T} \sum_{j=1}^{T} \mathbf{1}\!\left[a_{ij}^{(h)} < 0.01 \cdot \max_k a_{ik}^{(h)}\right].
31	    \label{eq:attn-sparsity}
32	\end{equation}
33	The per-position spar
…[truncated 2530 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_knowledge_update_tex_numbers_r10_20260516T020339",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 72 · 2026-05-16T02:10:04.107382+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_moved.tex",
  "limit": "250"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_knowledge_update_tex_numbers_r10_20260516T020339",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_moved.tex",
    "limit": "250"
  }
}
```

</details>

---

### Tool result

_source line 73 · 2026-05-16T02:10:04.107682+00:00_

1	
2	\section{Phase-Strategy Crossover Details}
3	\label{app:crossover-details}
4	
5	On DeepSeek ($n{=}496$), a strategy ranking reversal emerges at $s{=}0.25$ (Figure~\ref{fig:crossover}): importance-based eviction yields \emph{lower} II than random in the high-sparsity phase ($0.021$ vs.\ $1.113$) but \emph{higher} II in the low-sparsity phase ($3.971$ vs.\ $1.514$---a $2.6{\times}$ reversal; both $p < 10^{-4}$). This crossover is confirmed at all four sparsity levels, with reversal magnitude of $4.0{\times}$ at $s{=}0.15$, $3.4{\times}$ at $s{=}0.20$, $2.6{\times}$ at $s{=}0.25$, and $2.2{\times}$ at $s{=}0.30$ (decreasing as random eviction severity rises). The reversal arises because head pruning redistributes attention mass, altering importance rankings in a way that couples the two sparsity mechanisms in low-sparsity phases (\S\ref{sec:discrimination-collapse-main}). Qwen does not exhibit a crossover: importance-based eviction produces lower II than random in both phases across all sparsity levels (e.g., at $s{=}0.25$: high $0.004$ vs.\ $1.108$; low $1.053$ vs.\ $1.769$).
6	
7	\begin{figure}[t]
8	\centering
9	\includegraphics[width=\columnwidth]{fig3_crossover.pdf}
10	\caption{Strategy-dependent crossover at $s{=}0.25$ on DeepSeek ($n{=}496$). Grouped bar chart of median II by eviction strategy and reasoning phase. Importance-based eviction outperforms random in the high-sparsity phase but produces $2.6{\times}$ higher II in the low-sparsity phase, reversing the strategy ranking.}
11	\label{fig:crossover}
12	\end{figure}
13	
14	
15	\section{Profiling Subset Per-Phase Breakdown}
16	\label{app:profiling-subset}
17	
18	\begin{table*}[t]
19	\centering
20	\small
21	\caption{Per-phase interaction index (II) from the $n{=}50$ profiling subset (DeepSeek-R1-Distill-Qwen-7B). The main analysis ($n{=}496$) appears in Table~\ref{tab:main-results}. $G$ values in this table use the ratio-of-medians definition ($\widetilde{\mathrm{II}}_{\textit{low}} / \widetilde{\mathrm{II
…[truncated 17518 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_knowledge_update_tex_numbers_r10_20260516T020339",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 74 · 2026-05-16T02:10:04.107938+00:00_

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
  "session": "worker_knowledge_update_tex_numbers_r10_20260516T020339",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/results.tex"
  }
}
```

</details>

---

### Tool result

_source line 75 · 2026-05-16T02:10:04.108194+00:00_

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
13	\caption{Median compound severity difference ($\Delta = \widetilde{\mathrm{II}}_{\textit{low}} - \widetilde{\mathrm{II}}_{\textit{high}}$) by eviction strategy and sparsity level on DeepSeek-R1-Distill-Qwen-7B ($n{=}496$, 500 MATH-500 problems).}
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
29	Decomposing II by reasoning phase reveals that strategy-dependent severity is driven by amplification in the low-sparsity phase. Table~\ref{tab:main-results} reports the per-phase breakdown at $n{=}496$. The per-problem amplification ratio $G$ (Eq.~\ref{eq:gradient}) increases from $7.5{\times}$ (95\% CI: $[4.1, 11.4]$) at $s{=}0.15$ to $79.8{\times}$ ($[63.3, 96.5]$) at $s{=}0.30$ under imp
…[truncated 12220 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_knowledge_update_tex_numbers_r10_20260516T020339",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 76 · 2026-05-16T02:10:04.108446+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_robustness.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_knowledge_update_tex_numbers_r10_20260516T020339",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_robustness.tex"
  }
}
```

</details>

---

### Tool result

_source line 77 · 2026-05-16T02:10:04.108699+00:00_

1	\section{Benjamini-Hochberg FDR Correction}
2	\label{app:bh-fdr}
3	
4	Table~\ref{tab:bh-fdr} compares Bonferroni ($k{=}4$, per model$\times$strategy family) and Benjamini-Hochberg FDR correction across all 44 statistical tests. BH-FDR recovers 5 additional significant results beyond Bonferroni, all in low-effect-size conditions (random eviction or cross-training-paradigm random comparisons). All 32 Bonferroni-significant results remain significant under BH-FDR.
5	
6	\begin{table}[t]
7	\centering
8	\small
9	\caption{Bonferroni vs.\ BH-FDR correction summary ($\alpha{=}0.05$, 44 tests). ``BH only'' denotes tests significant under BH-FDR but not Bonferroni.}
10	\label{tab:bh-fdr}
11	\begin{tabular}{@{}lcc@{}}
12	\toprule
13	Category & Bonf.\ sig. & BH-only sig. \\
14	\midrule
15	Per-condition Wilcoxon ($k{=}16$) & 10 & 2 \\
16	Imp vs.\ rand ($k{=}8$) & 8 & 0 \\
17	Adjacent sparsity ($k{=}12$) & 10 & 1 \\
18	Cross-paradigm Mann-Whitney ($k{=}8$) & 4 & 2 \\
19	\midrule
20	Total ($k{=}44$) & 32 & 5 \\
21	\bottomrule
22	\end{tabular}
23	\end{table}
24	
25	The 5 BH-only results are: DeepSeek random $s{=}0.25$ and $s{=}0.30$ per-condition Wilcoxon ($p_{\text{Bonf}}{=}0.064$/$0.065$, BH $q{=}0.002$), DeepSeek random $s{=}0.25 \to 0.30$ adjacent-sparsity step ($p_{\text{Bonf}}{=}0.078$, BH $q{=}0.002$), and cross-training-paradigm random $s{=}0.25$/$s{=}0.30$ Mann-Whitney ($p_{\text{Bonf}}{=}0.66$/$0.17$, BH $q{=}0.018$/$0.005$). All involve random eviction---the weakest effects---confirming that Bonferroni is conservative but does not miss any importance-based findings.
26	
27	
28	\section{Minimum Phase Length Sensitivity}
29	\label{app:mpl-sensitivity}
30	
31	Table~\ref{tab:mpl-sensitivity} reports the paired median difference $\Delta$ under three \texttt{min\_phase\_length} (mpl) settings across all 16 conditions (2 models $\times$ 2 strategies $\times$ 4 sparsity levels). Conclusions are robust: all importance-based conditions remain significant at $p_{\text{Bonf}} < 10^
…[truncated 9862 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_knowledge_update_tex_numbers_r10_20260516T020339",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 78 · 2026-05-16T02:10:04.109063+00:00_

Perfect! Now I have comprehensive coverage of the LaTeX files. Let me compile a detailed report of all the values found:

## EXHAUSTIVE SEARCH REPORT

Based on my thorough search of all `.tex` files in `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/`, here are all occurrences of the specified old values that need updating:

### **1. VALUE: `3.99` (DS dose curve s025 value - paired median difference)**

**File: `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/results.tex`**
- **Line 19:** `Importance & 0.39 & 1.21 & 3.99 & 8.48 \\` (in Table caption)
- **Line 48:** `0.25 & Importance & 0.021 & 3.971 & 3.99\; $[3.53,\; 4.36]$ & $\mathbf{49.1}$\; $[40.1,\; 57.8]$ \\` (in Table tab:main-results)
- **Line 81:** `DeepSeek-R1-Distill-Qwen-7B ($n{=}496$) & 0.39 & 1.21 & 3.99 & 8.48 \\` (in Table tab:cross-model, appendix_moved.tex)
- **Line 115:** `0.25 & $3.99$\; $[3.53,\; 4.36]$ & $\mathbf{49.1}$\; $[40.1,\; 57.8]$ \\` (in Table tab:cohens-d)

**File: `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_moved.tex`**
- **Line 5:** "importance-based eviction yields \emph{lower} II than random in the high-sparsity phase ($0.021$ vs.\ $1.113$) but \emph{higher} II in the low-sparsity phase ($3.971$ vs.\ $1.514$---a $2.6{\times}$ reversal; both $p < 10^{-4}$). This crossover is confirmed at all four sparsity levels" - Context discussing strategy crossover at s=0.25

**File: `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_robustness.tex`**
- **Line 113:** `B (head-heavy) & 0.30 & 0.20 & 18.77 & 3.97 & 0.52 & $+$18.25 \\` (in Table tab:asymmetric-robust - asymmetric sparsity configuration, mid-phase II)
- **Line 115:** `Symmetric & 0.25 & 0.25 & 3.97 & --- & 0.02 & $+$3.99 \\` (in Table tab:asymmetric-robust - symm
…[truncated 3816 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_knowledge_update_tex_numbers_r10_20260516T020339",
  "tool": "Agent",
  "elapsed_ms": 7
}
```

</details>

---

### Tool call

_source line 79 · 2026-05-16T02:10:04.109455+00:00_

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
  "session": "worker_knowledge_update_tex_numbers_r10_20260516T020339",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/abstract.tex"
  }
}
```

</details>

---

### Tool result

_source line 80 · 2026-05-16T02:10:04.109708+00:00_

1	\begin{abstract}
2	Compound sparsity---simultaneously pruning attention heads and evicting KV cache entries---is essential for efficient LLM inference but produces super-additive quality degradation whose structure is poorly understood.
3	We show that compound severity is not phase-invariant: it is an emergent phase-strategy interaction with amplification ratios $G{=}7.5$--$79.8{\times}$ across reasoning phases in 7B-scale mathematical reasoning models.
4	
5	On DeepSeek-R1-Distill-Qwen-7B (MATH-500, $n{=}496$), importance-based eviction produces a monotonically increasing severity gradient (median $\Delta$: $0.39 \to 8.48$; all $p \ll 10^{-10}$). Random eviction is $3$--$17{\times}$ weaker where significant ($s \geq 0.25$), with a strategy ranking crossover at $s{=}0.25$.
6	The pattern replicates on Qwen2.5-7B-Instruct ($n_{\text{eff}}{=}475$, $\Delta$: $0.07 \to 3.16$; all $p < 10^{-14}$), with exploratory cross-architecture evidence from a LlamaForCausalLM model ($n{=}49$; ${\sim}1/40$ effect size) suggesting the qualitative pattern may extend beyond Qwen2 (\S\ref{sec:cross-arch}).
7	We present \emph{importance discrimination collapse}---the degeneration of head importance scores toward uniformity under compound stress---as a correlational diagnostic: both strategies exhibit near-identical Gini drops, yet severity diverges by $15$--$17{\times}$, implicating the structural specificity of importance-based pruning as the key differentiator.
8	These findings establish the phase-dependent nature of compound severity as a diagnostic foundation for future phase-aware mitigation strategies.
9	\end{abstract}
10	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_knowledge_update_tex_numbers_r10_20260516T020339",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 81 · 2026-05-16T02:10:04.109928+00:00_

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
  "session": "worker_knowledge_update_tex_numbers_r10_20260516T020339",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 82 · 2026-05-16T02:10:04.110173+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Long-context language models place acute pressure on the key--value (KV) cache, which grows linearly with sequence length \cite{kwon-sosp2023, pope-mlsys2023}.
5	Two complementary responses---\emph{attention head pruning} \cite{voita-acl2019, michel-neurips2019} and \emph{KV cache eviction} \cite{snapkv-neurips2024, adakv-neurips2025}---can be deployed simultaneously as \emph{compound sparsity}, but the resulting quality degradation is often super-additive \cite{spark-aaai2026, slim-icml2025}. Recent evaluations confirm that reasoning capabilities degrade disproportionately under compound compression \cite{unicomp-2026}, and that per-dimension safe zones intersect to form a smaller joint safe region \cite{phase-transition-compression-2026}.
6	
7	Prior work treats compound interaction magnitude as roughly constant across generation \cite{spark-aaai2026, unicomp-2026}, despite evidence that pruning sensitivity depends on representational phase \cite{decision-repr-transition-2026} and that no single sparse attention strategy dominates across generation stages \cite{sparse-frontier-2025}.
8	This assumption is problematic for reasoning models, whose generations alternate between broadly distributed attention (exploratory reasoning) and sharply concentrated attention (structured computation) \cite{thinkv-iclr2026}.
9	Phase-aware methods like ThinKV \cite{thinkv-iclr2026} apply different KV strategies per phase but without considering compound interaction, while importance-based eviction itself faces challenges from greedy bias \cite{greedy-bias-kvcache-2026}, deferred importance \cite{retentivekv-2026}, and temporal dynamics in long generations \cite{lethe-aaai2026}. These methods each optimize a single pruning axis; we characterize the interaction when multiple mechanisms are composed.
10	If compound severity varies across these phases, a uniform sparsity budget may be safe in one phase yet destructive in another.

…[truncated 3857 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_knowledge_update_tex_numbers_r10_20260516T020339",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 83 · 2026-05-16T02:10:04.110399+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_disc_analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_knowledge_update_tex_numbers_r10_20260516T020339",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_disc_analysis.tex"
  }
}
```

</details>

---

### Tool result

_source line 84 · 2026-05-16T02:10:04.110751+00:00_

1	\section{Importance Discrimination Collapse Details}
2	\label{app:discrimination-collapse-details}
3	
4	This cross-model consistency (Table~\ref{tab:discrimination-metrics-full}) establishes importance discrimination collapse as a robust consequence of compound sparsity. When importance scores lose discriminative power, thresholding the bottom-$s$ fraction becomes noise-sensitive: small perturbations change which positions cross the eviction boundary. In the limit of perfectly uniform scores, importance-based eviction degenerates into an arbitrary selection functionally equivalent to biased random eviction. The same pattern holds under random eviction (DeepSeek: $-0.031$ to $-0.071$; Qwen: $-0.019$ to $-0.046$), confirming that importance discrimination collapse is a consequence of head pruning \emph{per se}, not of the eviction strategy.
5	
6	
7	\section{Extended Discussion}
8	\label{app:extended-discussion}
9	
10	\paragraph{On the predictability of phase-modulated severity.}
11	The compound interaction is not uniformly fragile---it is selectively fragile in a phase-dependent manner ($\widetilde{\mathrm{II}}_{\text{high}} < 0.06$ at $s \leq 0.30$).
12	
13	\paragraph{Random masking as falsification control.}
14	At $n{=}500$, random eviction develops a detectable but weak phase gradient above $s \approx 0.20$: non-significant at $s \leq 0.20$ for both models, but significant at $s \geq 0.25$ (DS: $\Delta{=}0.26$--$0.51$, $p_{\text{Bonf}} < 0.006$; QW: $\Delta{=}0.39$--$0.91$, $p_{\text{Bonf}} < 10^{-10}$). Where significant, the random phase gradient is $3$--$17{\times}$ weaker than importance-based (restricted to conditions where both strategies are significant, $s \geq 0.25$), confirming that the dominant amplification is strategy-specific.
15	
16	\paragraph{Entropy mechanism boundary conditions.}
17	Directly measuring per-head entropy shifts across architecturally distinct models---and identifying what training-time properties determine whether entropy concentra
…[truncated 13583 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_knowledge_update_tex_numbers_r10_20260516T020339",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 85 · 2026-05-16T02:10:04.110988+00:00_

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
  "session": "worker_knowledge_update_tex_numbers_r10_20260516T020339",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/discussion.tex"
  }
}
```

</details>

---

### Tool result

_source line 86 · 2026-05-16T02:10:04.111177+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Implications for deployment.}
5	A uniform compression budget implicitly accepts order-of-magnitude severity penalties during low-sparsity reasoning phases. Pilot evaluation (Appendix~\ref{app:pilot-mitigation}) achieved 18\% recovery, below the pre-registered 30\% gate, suggesting that effective phase-aware allocation requires finer phase boundary estimation than current proxies provide. Additional mechanisms (e.g., strategy switching, adaptive thresholding) warrant investigation. We expect qualitatively similar behavior for other attention-mass-based scoring methods (H$_2$O \cite{h2o-neurips2023}, SnapKV \cite{snapkv-neurips2024}, PyramidKV \cite{pyramidkv-colm2025}), though quantitative magnitudes may differ. Extended discussion in Appendix~\ref{app:extended-discussion}.
6	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_knowledge_update_tex_numbers_r10_20260516T020339",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 87 · 2026-05-16T02:10:04.111369+00:00_

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
  "session": "worker_knowledge_update_tex_numbers_r10_20260516T020339",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/conclusion.tex"
  }
}
```

</details>

---

### Tool result

_source line 88 · 2026-05-16T02:10:04.111583+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We showed that compound sparsity severity is not phase-invariant but exhibits an emergent phase-strategy interaction. Under importance-based eviction, the paired median difference $\Delta$ increases from $0.39$ to $8.48$ (DeepSeek, $n{=}496$) and $0.07$ to $3.16$ (Qwen, $n{=}475$), all $p < 10^{-13}$, with amplification ratios $G{=}7.5$--$79.8{\times}$. Random eviction is $3$--$17{\times}$ weaker where both strategies are significant ($s \geq 0.25$). A model-dependent crossover on DeepSeek demonstrates that no single strategy dominates uniformly. Importance discrimination collapse provides a correlational diagnostic: despite near-identical Gini drops, severity diverges by $15$--$17{\times}$, implicating the structural specificity of importance-based pruning.
5	These findings establish compound severity as phase-dependent, providing a diagnostic foundation for future phase-aware mitigation. Future work could explore whether these patterns generalize to other reasoning domains, provide causal validation of importance discrimination collapse, and systematically characterize asymmetric compound interactions.
6	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_knowledge_update_tex_numbers_r10_20260516T020339",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 89 · 2026-05-16T02:10:04.111769+00:00_

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
  "session": "worker_knowledge_update_tex_numbers_r10_20260516T020339",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/analysis.tex"
  }
}
```

</details>

---

### Tool result

_source line 90 · 2026-05-16T02:10:04.112005+00:00_

1	\section{Importance Discrimination Collapse under Compound Sparsity}
2	\label{sec:analysis}
3	
4	The mechanisms discussed here are \emph{correlational diagnostics} that illuminate but do not fully explain the $15$--$17{\times}$ severity divergence between strategies. Both strategies exhibit near-identical Gini drops ($<10\%$ difference), yet severity diverges by $15$--$17{\times}$---an order-of-magnitude mismatch indicating that aggregate concentration collapse alone is insufficient. The critical differentiator is \emph{structural specificity} of importance-based pruning, which systematically removes high-attention-score heads (\S\ref{sec:discrimination-collapse-main}).
5	
6	\subsection{Importance Discrimination Collapse}
7	\label{sec:discrimination-collapse-main}
8	
9	Head pruning systematically reduces the discriminative power of cumulative importance scores, suggesting a mechanism for the phase-strategy interaction. The Gini coefficient decreases by $0.030$--$0.081$ (DeepSeek, $6$--$17\%$ relative to dense baseline) and $0.010$--$0.020$ (Qwen, $2$--$4\%$) after pruning, with consistent negative deltas in all 16 conditions (Appendix~\ref{app:analysis}, Table~\ref{tab:discrimination-metrics-full}). Random eviction shows near-identical Gini drops (e.g., DeepSeek $s{=}0.25$: $-0.065$ vs.\ $-0.060$), confirming that collapse is a consequence of head pruning \emph{per se}. Yet importance-based severity is $15$--$17{\times}$ larger---the amplification arises because importance-based eviction \emph{depends on} the very scores that pruning degrades.
10	
11	This pattern---\emph{importance discrimination collapse}---reflects eviction degenerating into noise-sensitive selection as score distributions approach uniformity. The effect is phase-dependent: low-sparsity phases have broadly distributed attention where collapse has maximum impact; high-sparsity phases preserve concentration. \cite{hies-2025} report this collapse under single-axis pruning; we extend it to the compo
…[truncated 1582 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_knowledge_update_tex_numbers_r10_20260516T020339",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 91 · 2026-05-16T02:10:04.112277+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_moved.tex",
  "offset": "15",
  "limit": "60"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_knowledge_update_tex_numbers_r10_20260516T020339",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_moved.tex",
    "offset": "15",
    "limit": "60"
  }
}
```

</details>

---

### Tool result

_source line 92 · 2026-05-16T02:10:04.112552+00:00_

15	\section{Profiling Subset Per-Phase Breakdown}
16	\label{app:profiling-subset}
17	
18	\begin{table*}[t]
19	\centering
20	\small
21	\caption{Per-phase interaction index (II) from the $n{=}50$ profiling subset (DeepSeek-R1-Distill-Qwen-7B). The main analysis ($n{=}496$) appears in Table~\ref{tab:main-results}. $G$ values in this table use the ratio-of-medians definition ($\widetilde{\mathrm{II}}_{\textit{low}} / \widetilde{\mathrm{II}}_{\textit{high}}$), which differs from the primary per-problem definition in Eq.~\ref{eq:gradient}. At low sparsity ($s{=}0.15$), the two definitions diverge substantially ($7.5{\times}$ vs.\ $69{\times}$) because per-problem ratios are sensitive to near-zero $\mathrm{II}_{\textit{high}}$ values.}
22	\label{tab:profiling-subset}
23	\begin{tabular}{@{}llccccr@{}}
24	\toprule
25	$s$ & Strategy & $\widetilde{\mathrm{II}}_{\textit{high}}$ & $\widetilde{\mathrm{II}}_{\textit{mid}}$ & $\widetilde{\mathrm{II}}_{\textit{low}}$ & $\Delta$ & $G$ \\
26	\midrule
27	0.15 & Importance & 0.006 & 0.081 & 0.398 & 0.39 & $\mathbf{69}$ \\
28	0.15 & Random     & 0.093 & 0.097 & 0.103 & 0.01 & 1.1 \\
29	\addlinespace
30	0.20 & Importance & 0.015 & 0.203 & 1.496 & 1.48 & $\mathbf{103}$ \\
31	0.20 & Random     & 0.292 & 0.350 & 0.276 & $-$0.02 & 0.9 \\
32	\addlinespace
33	0.25 & Importance & 0.032 & 1.118 & 7.196 & 7.16 & $\mathbf{222}$ \\
34	0.25 & Random     & 0.818 & 0.932 & 1.363 & 0.54 & 1.7 \\
35	\addlinespace
36	0.30 & Importance & 0.053 & 2.283 & 14.639 & 14.59 & $\mathbf{274}$ \\
37	0.30 & Random     & 2.503 & 2.592 & 4.041 & 1.54 & 1.6 \\
38	\bottomrule
39	\end{tabular}
40	\end{table*}
41	
42	
43	\section{Cross-Training-Paradigm Replication Details}
44	\label{app:cross-model-details}
45	
46	Both models share the Qwen2ForCausalLM backbone (28 layers, 28 heads, 4-group GQA) but differ in training: DeepSeek uses reasoning distillation from DeepSeek-R1, while Qwen2.5 uses standard instruction tuning without explicit reasoning delimiters. This within-a
…[truncated 1925 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_knowledge_update_tex_numbers_r10_20260516T020339",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 93 · 2026-05-16T02:10:04.112854+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "d\\s*[=_]\\s*0\\.\\d+|cohen|effect.size",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
  "output_mode": "content",
  "-n": "True",
  "glob": "*.tex",
  "-i": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_knowledge_update_tex_numbers_r10_20260516T020339",
  "tool": "Grep",
  "tool_args": {
    "pattern": "d\\s*[=_]\\s*0\\.\\d+|cohen|effect.size",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
    "output_mode": "content",
    "-n": "True",
    "glob": "*.tex",
    "-i": "True"
  }
}
```

</details>

---

### Tool result

_source line 94 · 2026-05-16T02:10:04.113070+00:00_

artifacts/_project/paper/analysis.tex:13:[Omitted long matching line]
artifacts/_project/paper/appendix_robustness.tex:4:Table~\ref{tab:bh-fdr} compares Bonferroni ($k{=}4$, per model$\times$strategy family) and Benjamini-Hochberg FDR correction across all 44 statistical tests. BH-FDR recovers 5 additional significant results beyond Bonferroni, all in low-effect-size conditions (random eviction or cross-training-paradigm random comparisons). All 32 Bonferroni-significant results remain significant under BH-FDR.
artifacts/_project/paper/appendix_robustness.tex:135:We binarize each token as ``thinking'' (inside \texttt{&lt;think>}) or ``answer'' (outside) and compare against the sparsity-based low/high phase assignment. Cohen's $\kappa{=}0.887$ (median across problems), indicating near-perfect agreement between the data-driven sparsity proxy and the model's explicit reasoning markers. Of thinking tokens, $57.8\%$ fall in the low-sparsity phase; of answer tokens, $62.7\%$ fall in the high-sparsity phase.
artifacts/_project/paper/appendix_moved.tex:164:[Omitted long matching line]
artifacts/_project/paper/background.tex:31:[Omitted long matching line]
artifacts/_project/paper/abstract.tex:6:The pattern replicates on Qwen2.5-7B-Instruct ($n_{\text{eff}}{=}475$, $\Delta$: $0.07 \to 3.16$; all $p < 10^{-14}$), with exploratory cross-architecture evidence from a LlamaForCausalLM model ($n{=}49$; ${\sim}1/40$ effect size) suggesting the qualitative pattern may extend beyond Qwen2 (\S\ref{sec:cross-arch}).
artifacts/_project/paper/appendix_disc_analysis.tex:50:[Omitted long matching line]
artifacts/_project/paper/results.tex:8:[Omitted long matching line]
artifacts/_project/paper/results.tex:103:[Omitted long matching line]
artifacts/_project/paper/results.tex:109:\label{tab:cohens-d}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_knowledge_update_tex_numbers_r10_20260516T020339",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 95 · 2026-05-16T02:10:04.113290+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "d_z|d_\\{?z\\}?",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
  "output_mode": "content",
  "-n": "True",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_knowledge_update_tex_numbers_r10_20260516T020339",
  "tool": "Grep",
  "tool_args": {
    "pattern": "d_z|d_\\{?z\\}?",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
    "output_mode": "content",
    "-n": "True",
    "glob": "*.tex"
  }
}
```

</details>

---

### Tool result

_source line 96 · 2026-05-16T02:10:04.113517+00:00_

artifacts/_project/paper/appendix_moved.tex:144:[Omitted long matching line]
artifacts/_project/paper/limitations.tex:2:[Omitted long matching line]
artifacts/_project/paper/appendix_disc_analysis.tex:38:[Omitted long matching line]
artifacts/_project/paper/results.tex:103:[Omitted long matching line]
artifacts/_project/paper/results.tex:119:\multicolumn{3}{@{}l}{\footnotesize All $p_{\text{Bonf}} < 10^{-13}$. Within-importance $d_z$ (s015 vs.\ s030): DS $0.94$, QW $0.92$.}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_knowledge_update_tex_numbers_r10_20260516T020339",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 97 · 2026-05-16T02:10:04.113723+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_moved.tex",
  "offset": "140",
  "limit": "30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_knowledge_update_tex_numbers_r10_20260516T020339",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_moved.tex",
    "offset": "140",
    "limit": "30"
  }
}
```

</details>

---

### Tool result

_source line 98 · 2026-05-16T02:10:04.113963+00:00_

140	To test whether the phase-modulated severity pattern extends beyond the Qwen2 architecture, we replicate the experiment on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, 8B parameters; $n{=}49$ paired problems). Table~\ref{tab:llama-cross-arch} reports the strategy-dependent severity comparison across sparsity levels.
141	
142	The evidence for a strategy contrast on LLaMA is mixed: at $s{=}0.15$, the bootstrap CI excludes zero ($[0.002, 0.043]$) but the Bonferroni-corrected Wilcoxon test is non-significant ($p_{\text{Bonf}}{=}0.219$); conversely, at $s{=}0.30$ the CI spans zero ($[-0.069, 0.544]$) while the Wilcoxon test reaches significance ($p_{\text{Bonf}}{=}0.029$). At intermediate levels ($s \in \{0.20, 0.25\}$), neither CI nor Wilcoxon reaches significance. The median paired difference increases monotonically ($\widetilde{\Delta}$: $0.020 \to 0.356$), consistent with a genuine but weak trend---partially confirming the cross-architecture hypothesis while underscoring the substantially weaker interaction on LlamaForCausalLM.\footnote{The CI/Wilcoxon discrepancy reflects differing power profiles under small $n$ with heavy-tailed distributions: the percentile bootstrap CI is based on the resampled median distribution and is less sensitive to tail observations, while the Wilcoxon signed-rank test uses signed ranks and is more sensitive to tail outliers. This inconsistency itself supports the conservative ``mixed/weak evidence'' interpretation.}
143	
144	The absolute magnitude is architecture-dependent: LLaMA severity differences are ${\sim}40{\times}$ smaller than DeepSeek and ${\sim}7{\times}$ smaller than Qwen. Notably, random eviction on LLaMA also exhibits a non-trivial phase gradient ($d_z$: $0.35 \to 0.44$), substantially reducing the strategy contrast that is the hallmark of the phase-strategy interaction on Qwen2 models. This suggests that the strength of the strategy$\times$phase interaction---not merely the severity gradient itself---is architecture-
…[truncated 2193 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_knowledge_update_tex_numbers_r10_20260516T020339",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 99 · 2026-05-16T02:10:04.114206+00:00_

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
  "session": "worker_knowledge_update_tex_numbers_r10_20260516T020339",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/limitations.tex"
  }
}
```

</details>

---

### Tool result

_source line 100 · 2026-05-16T02:10:04.114466+00:00_

1	\paragraph{Model scale and architecture.}
2	All experiments are conducted at the 7--8B parameter scale. Whether the phase-modulated severity patterns persist, amplify, or attenuate at larger scales (e.g., 70B) remains untested. Preliminary cross-architecture validation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, \S\ref{sec:cross-arch}, Appendix~\ref{app:cross-arch}) partially confirms the qualitative pattern beyond the Qwen2 architecture---monotonically increasing $d_z$ with within-importance phase gradient $\sim$1.0---but with substantially weaker interaction magnitude ($\sim$1/40 of DeepSeek) and mixed statistical evidence (only $s{=}0.30$ significant after Bonferroni correction). The pattern has been tested on two architecture families (Qwen2ForCausalLM, LlamaForCausalLM); comprehensive validation across more diverse architectures (e.g., Mistral, multi-latent attention) and larger scales is needed for full generalization claims.
3	
4	\paragraph{Task coverage.}
5	Our primary evaluation uses MATH-500; cross-benchmark validation on GSM8K (\S\ref{sec:cross-benchmark}) confirms the phase gradient direction under importance-based eviction but reveals that random eviction is non-significant on GSM8K (CIs spanning zero), precluding meaningful ratio computation. On MATH-500, strategy specificity is quantifiable ($15$--$17{\times}$); on GSM8K, it manifests as a qualitative gap (significant vs.\ non-significant). This suggests that the phase-strategy interaction is robust in direction but task-dependent in form---complex reasoning (MATH-500) produces quantitative strategy contrast while simpler arithmetic (GSM8K) produces qualitative separation. Qwen GSM8K outputs were truncated at \texttt{max\_new\_tokens}${=}$2047, so Qwen GSM8K absolute values carry this limitation; DeepSeek GSM8K data is untruncated. Our task-complexity explanation for specificity attenuation (lower cognitive load $\to$ more uniform attention $\to$ reduced strategy sensitivity) is supported by 
…[truncated 3213 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_knowledge_update_tex_numbers_r10_20260516T020339",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 101 · 2026-05-16T02:10:04.114734+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_disc_analysis.tex",
  "offset": "35",
  "limit": "20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_knowledge_update_tex_numbers_r10_20260516T020339",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_disc_analysis.tex",
    "offset": "35",
    "limit": "20"
  }
}
```

</details>

---

### Tool result

_source line 102 · 2026-05-16T02:10:04.114978+00:00_

35	\paragraph{Architectural scope.}
36	Our two models---DeepSeek-R1-Distill-Qwen-7B and Qwen2.5-7B-Instruct---share the Qwen2ForCausalLM architecture.
37	The cross-training-paradigm replication (\S\ref{sec:cross-model}) establishes that the findings are not artifacts of a single model's weights, though both models share the same Qwen2ForCausalLM architecture.
38	Preliminary cross-architecture validation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, \S\ref{sec:cross-arch}, Appendix~\ref{app:cross-arch}) shows qualitatively consistent within-importance phase gradients ($d_z \sim 1.0$) but a substantially weaker strategy $\times$ phase interaction than in Qwen2-based architectures; random pruning also exhibits a non-trivial phase gradient on LLaMA, reducing the strategy contrast. This partial confirmation ($s{=}0.30$ Wilcoxon $p_{\text{Bonf}}{=}0.029$; $s \leq 0.25$ non-significant) suggests the qualitative pattern may generalize but quantitative impact is architecture-dependent. Comprehensive cross-architecture validation across more diverse designs (e.g., Mistral, multi-latent attention architectures) and scales remains an important next step.
39	
40	
41	\paragraph{Task coverage.}
42	We evaluate exclusively on MATH-500, a mathematical reasoning benchmark.
43	Different reasoning tasks---code generation, commonsense reasoning, multi-hop question answering---may induce different phase structures with different sparsity distributions, potentially altering the severity gradient profile.
44	Generalizing the phase-strategy interaction to broader reasoning domains is an important next step.
45	
46	
47	\paragraph{Statistical scope.}
48	Bootstrap confidence intervals use $B{=}10{,}000$ resamples (seed$=$42). The primary analysis uses $n{=}496$ paired problems for DeepSeek (4 excluded) and $n{=}475$ for Qwen (25 excluded); the permutation test (Table~\ref{tab:permutation}) uses $n{=}49$ from an initial profiling subset.
49	The severity difference distribution is right-skew
…[truncated 1175 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_knowledge_update_tex_numbers_r10_20260516T020339",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 103 · 2026-05-16T02:10:04.115278+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "→|\\\\to|\\\\rightarrow",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
  "output_mode": "content",
  "-n": "True",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_knowledge_update_tex_numbers_r10_20260516T020339",
  "tool": "Grep",
  "tool_args": {
    "pattern": "→|\\\\to|\\\\rightarrow",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
    "output_mode": "content",
    "-n": "True",
    "glob": "*.tex"
  }
}
```

</details>

---

### Tool result

_source line 104 · 2026-05-16T02:10:04.115551+00:00_

artifacts/_project/paper/appendix_robustness.tex:12:\toprule
artifacts/_project/paper/appendix_robustness.tex:25:[Omitted long matching line]
artifacts/_project/paper/appendix_robustness.tex:39:\toprule
artifacts/_project/paper/appendix_robustness.tex:79:\toprule
artifacts/_project/paper/appendix_robustness.tex:109:\toprule
artifacts/_project/paper/appendix_moved.tex:24:\toprule
artifacts/_project/paper/appendix_moved.tex:60:\toprule
artifacts/_project/paper/appendix_moved.tex:78:\toprule
artifacts/_project/paper/appendix_moved.tex:110:[Omitted long matching line]
artifacts/_project/paper/appendix_moved.tex:118:\toprule
artifacts/_project/paper/appendix_moved.tex:142:[Omitted long matching line]
artifacts/_project/paper/appendix_moved.tex:144:[Omitted long matching line]
artifacts/_project/paper/appendix_moved.tex:152:\toprule
artifacts/_project/paper/appendix_moved.tex:181:\toprule
artifacts/_project/paper/appendix_moved.tex:221:\toprule
artifacts/_project/paper/limitations.tex:5:[Omitted long matching line]
artifacts/_project/paper/abstract.tex:5:On DeepSeek-R1-Distill-Qwen-7B (MATH-500, $n{=}496$), importance-based eviction produces a monotonically increasing severity gradient (median $\Delta$: $0.39 \to 8.48$; all $p \ll 10^{-10}$). Random eviction is $3$--$17{\times}$ weaker where significant ($s \geq 0.25$), with a strategy ranking crossover at $s{=}0.25$.
artifacts/_project/paper/abstract.tex:6:The pattern replicates on Qwen2.5-7B-Instruct ($n_{\text{eff}}{=}475$, $\Delta$: $0.07 \to 3.16$; all $p < 10^{-14}$), with exploratory cross-architecture evidence from a LlamaForCausalLM model ($n{=}49$; ${\sim}1/40$ effect size) suggesting the qualitative pattern may extend beyond Qwen2 (\S\ref{sec:cross-arch}).
artifacts/_project/paper/appendix_disc_analysis.tex:69:[Omitted long matching line]
artifacts/_project/paper/appendix_disc_analysis.tex:77:\toprule
artifacts/_project/paper/appendix_disc_analysis.tex:101:\toprule
artifacts/_project/paper/appendix_disc_analysi
…[truncated 1064 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_knowledge_update_tex_numbers_r10_20260516T020339",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 105 · 2026-05-16T02:10:04.115880+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/abstract.tex",
  "old_string": "Random eviction is $3$--$17{\\times}$ weaker",
  "new_string": "Random eviction is $2.7$--$17{\\times}$ weaker"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_knowledge_update_tex_numbers_r10_20260516T020339",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/abstract.tex",
    "old_string": "Random eviction is $3$--$17{\\times}$ weaker",
    "new_string": "Random eviction is $2.7$--$17{\\times}$ weaker"
  }
}
```

</details>

---

### Tool result

_source line 106 · 2026-05-16T02:10:04.116115+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/abstract.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_knowledge_update_tex_numbers_r10_20260516T020339",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 107 · 2026-05-16T02:10:04.116315+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/introduction.tex",
  "old_string": "($3$--$17{\\times}$ smaller than importance-based where both strategies are significant, $s \\geq 0.25$)",
  "new_string": "($2.7$--$17{\\times}$ smaller than importance-based where both strategies are significant, $s \\geq 0.25$)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_knowledge_update_tex_numbers_r10_20260516T020339",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/introduction.tex",
    "old_string": "($3$--$17{\\times}$ smaller than importance-based where both strategies are significant, $s \\geq 0.25$)",
    "new_string": "($2.7$--$17{\\times}$ smaller than importance-based where both strategies are significant, $s \\geq 0.25$)"
  }
}
```

</details>

---

### Tool result

_source line 108 · 2026-05-16T02:10:04.116580+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/introduction.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_knowledge_update_tex_numbers_r10_20260516T020339",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 109 · 2026-05-16T02:10:04.116783+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/introduction.tex",
  "old_string": "severity gradient across reasoning phases that is $3$--$17{\\times}$ larger",
  "new_string": "severity gradient across reasoning phases that is $2.7$--$17{\\times}$ larger"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_knowledge_update_tex_numbers_r10_20260516T020339",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/introduction.tex",
    "old_string": "severity gradient across reasoning phases that is $3$--$17{\\times}$ larger",
    "new_string": "severity gradient across reasoning phases that is $2.7$--$17{\\times}$ larger"
  }
}
```

</details>

---

### Tool result

_source line 110 · 2026-05-16T02:10:04.117034+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/introduction.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_knowledge_update_tex_numbers_r10_20260516T020339",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 111 · 2026-05-16T02:10:04.117230+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/conclusion.tex",
  "old_string": "Random eviction is $3$--$17{\\times}$ weaker",
  "new_string": "Random eviction is $2.7$--$17{\\times}$ weaker"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_knowledge_update_tex_numbers_r10_20260516T020339",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/conclusion.tex",
    "old_string": "Random eviction is $3$--$17{\\times}$ weaker",
    "new_string": "Random eviction is $2.7$--$17{\\times}$ weaker"
  }
}
```

</details>

---

### Tool result

_source line 112 · 2026-05-16T02:10:04.117471+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/conclusion.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_knowledge_update_tex_numbers_r10_20260516T020339",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 113 · 2026-05-16T02:10:04.117680+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_disc_analysis.tex",
  "old_string": "the random phase gradient is $3$--$17{\\times}$ weaker",
  "new_string": "the random phase gradient is $2.7$--$17{\\times}$ weaker"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_knowledge_update_tex_numbers_r10_20260516T020339",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_disc_analysis.tex",
    "old_string": "the random phase gradient is $3$--$17{\\times}$ weaker",
    "new_string": "the random phase gradient is $2.7$--$17{\\times}$ weaker"
  }
}
```

</details>

---

### Tool result

_source line 114 · 2026-05-16T02:10:04.117892+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_disc_analysis.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_knowledge_update_tex_numbers_r10_20260516T020339",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 115 · 2026-05-16T02:10:04.118045+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\$3\\$--\\$17",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
  "output_mode": "content",
  "-n": "True",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_knowledge_update_tex_numbers_r10_20260516T020339",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\$3\\$--\\$17",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
    "output_mode": "content",
    "-n": "True",
    "glob": "*.tex"
  }
}
```

</details>

---

### Tool result

_source line 116 · 2026-05-16T02:10:04.118171+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_knowledge_update_tex_numbers_r10_20260516T020339",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 117 · 2026-05-16T02:10:04.118289+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\$3\\$.*\\\\times",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
  "output_mode": "content",
  "-n": "True",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_knowledge_update_tex_numbers_r10_20260516T020339",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\$3\\$.*\\\\times",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
    "output_mode": "content",
    "-n": "True",
    "glob": "*.tex"
  }
}
```

</details>

---

### Tool result

_source line 118 · 2026-05-16T02:10:04.118428+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_knowledge_update_tex_numbers_r10_20260516T020339",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 119 · 2026-05-16T02:10:04.118877+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\$2\\.7\\$",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
  "output_mode": "content",
  "-n": "True",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_knowledge_update_tex_numbers_r10_20260516T020339",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\$2\\.7\\$",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
    "output_mode": "content",
    "-n": "True",
    "glob": "*.tex"
  }
}
```

</details>

---

### Tool result

_source line 120 · 2026-05-16T02:10:04.119034+00:00_

artifacts/_project/paper/conclusion.tex:4:[Omitted long matching line]
artifacts/_project/paper/appendix_moved.tex:98:As a control, random eviction on Qwen mirrors DeepSeek: non-significant at $s \leq 0.20$ ($\Delta$: $-0.01$, $0.02$; CIs span zero) but significant at $s \geq 0.25$ ($\Delta{=}0.39$, $p_{\text{Bonf}} < 10^{-10}$; $\Delta{=}0.91$, $p_{\text{Bonf}} < 10^{-13}$). Where significant, the random phase gradient is $2.7$--$3.5{\times}$ weaker than importance-based ($0.39$ vs.\ $1.07$ at $s{=}0.25$; $0.91$ vs.\ $3.16$ at $s{=}0.30$), confirming strategy-specific amplification.
artifacts/_project/paper/abstract.tex:5:On DeepSeek-R1-Distill-Qwen-7B (MATH-500, $n{=}496$), importance-based eviction produces a monotonically increasing severity gradient (median $\Delta$: $0.39 \to 8.48$; all $p \ll 10^{-10}$). Random eviction is $2.7$--$17{\times}$ weaker where significant ($s \geq 0.25$), with a strategy ranking crossover at $s{=}0.25$.
artifacts/_project/paper/appendix_disc_analysis.tex:14:[Omitted long matching line]
artifacts/_project/paper/appendix_disc_analysis.tex:53:These effects are genuine but $2.7$--$20{\times}$ weaker than importance-based eviction at the same sparsity levels, consistent with a weak phase gradient that is detectable at sufficient sample size but not the primary driver of compound severity.
artifacts/_project/paper/introduction.tex:18:Random eviction develops a detectable but weak phase gradient only above $s \approx 0.20$ ($2.7$--$17{\times}$ smaller than importance-based where both strategies are significant, $s \geq 0.25$), confirming that the dominant gradient is an emergent phase-strategy interaction.
artifacts/_project/paper/introduction.tex:25:[Omitted long matching line]
artifacts/_project/paper/results.tex:88:[Omitted long matching line]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_knowledge_update_tex_numbers_r10_20260516T020339",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 121 · 2026-05-16T02:10:04.119225+00:00_

所有 `$3$--$17{\times}$` 已更新为 `$2.7$--$17{\times}$`，无遗漏。

## 修改清单

| 文件 | 行号 | 旧值 | 新值 |
|------|------|------|------|
| abstract.tex | 5 | `$3$--$17{\times}$` | `$2.7$--$17{\times}$` |
| introduction.tex | 18 | `$3$--$17{\times}$` | `$2.7$--$17{\times}$` |
| introduction.tex | 25 | `$3$--$17{\times}$` | `$2.7$--$17{\times}$` |
| conclusion.tex | 4 | `$3$--$17{\times}$` | `$2.7$--$17{\times}$` |
| appendix_disc_analysis.tex | 14 | `$3$--$17{\times}$` | `$2.7$--$17{\times}$` |

## 未找到的值

- **DS dose curve (1.15/3.97/9.94)**: .tex 文件中不存在这些值。.tex 使用的是 n=496 的 Δ 值（0.39/1.21/3.99/8.48），而 paper_framing.md 的 0.32→1.15→3.97→9.94 是 per-problem paired median 的不同统计量，未写入论文正文。
- **`$d=0.28$` (QW Cohen's d s015)**: .tex 中无此值。唯一的 `0.28` 出现在 appendix_disc_analysis.tex:84，是 GSM8K DeepSeek random s020 的原始 Δ 值（不相关）。
- appendix_moved.tex:98、appendix_disc_analysis.tex:53、results.tex:88 中已有 `$2.7$` 作为下界，无需修改。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_knowledge_update_tex_numbers_r10_20260516T020339"
}
```

</details>

---
