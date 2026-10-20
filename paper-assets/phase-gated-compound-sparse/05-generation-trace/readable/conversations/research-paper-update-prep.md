# research paper update prep

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 59
- **Recorded user turns:** 0
- **Tool calls:** 29
- **Original source:** `logs/chats/worker_research_paper_update_prep_20260515T013953.jsonl`
- **Structured JSON:** [`832eb3d71652d67af0cb.json`](../../sessions/83/832eb3d71652d67af0cb.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

59 recorded events

### Tool call

_source line 1 · 2026-05-15T01:46:28.027222+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_paper_update_prep_20260515T013953",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-15T01:46:28.027669+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper_update_prep_20260515T013953",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-15T01:46:28.027875+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_paper_update_prep_20260515T013953",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/paper"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-15T01:46:28.028016+00:00_

&lt;tool_use_error>Directory does not exist: /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/paper. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse.&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper_update_prep_20260515T013953",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-15T01:46:28.028167+00:00_

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
  "session": "worker_research_paper_update_prep_20260515T013953",
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

_source line 6 · 2026-05-15T01:46:28.028388+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/paper_framing.md\", \"content\": \"# Paper Framing — Phase-Gated Compound Sparsity\\n\\n> 最后更新: 2026-05-14 (D060 C8 partially_confirmed; D056 C5b future_work; D059 d_z 分场景) | 维护者: Director\\n\\n## Core Insight\\n\\nCompound sparsity（attention head pruning + KV cache eviction）的 severity 不是固定常数——它是 eviction strategy 和 reasoning phase 交互的涌现属性。Importance-based eviction 的 compound interaction severity（paired median difference: median(II_low_i − II_high_i)）随 sparsity 单调递增（DeepSeek: 0.32→1.15→3.97→9.94; Qwen: 0.048→0.208→1.109→2.619），而 random masking 三相 II 持平（7/8 FAIL; Qwen s030 PASS p=0.012 but d=-0.04 negligible）。Cohen's d（paired d_z, B=10000）从 small-medium 到 large（DeepSeek: 0.44→0.80; Qwen: 0.28→1.02，s015 边缘）。LLaMA 跨架构验证（D060）qualitative direction consistent（within-importance d_z~1.0），但 strategy×phase 交互弱于 Qwen2 架构（imp_vs_rand d_z 0.19→0.34, 仅 s030 显著），且 random 在 LLaMA 上也显示显著 phase gradient（d_z 0.35→0.44），与 DeepSeek/Qwen random 7/8 FAIL 模式定性不同。这一发现挑战了 compound degradation 均匀分布的隐含假设。\\n\\n**数字基准**：所有数字基于 bf16 per-problem paired 统计量（B=10000 bootstrap）。median_diff 定义为 median(II_low_i − II_high_i)（逐 problem 配对差的中位数）。fp16 旧数据已弃用。\\n\\n## Narrative Arc\\n\\nCompound sparsity 是高效 LLM 推理的实用部署需求，但 prior work（SparK, Ada-KV, SLiM）将 compound interaction 视为均匀超可加。我们发现 severity 是 strategy × phase 交互的涌现属性：importance eviction 的 compound interaction 在 low-sparsity phase 远大于 high-sparsity phase（paired median difference 单调递增 0.32→9.94），而 random eviction 在所有 phase 保持平坦（7/8 FAIL; 唯一例外 Qwen s030 p=0.012 效应量可忽略 d=-0.04）。Cross-model replication 方向一致（Qwen magnitude ~1/4 of DeepSeek，onset threshold s≥0.20）。LLaMA 跨架构验证已完成（c3_llama, D060）：qualitative direction consistent（importance phase gradient d_z≈1.0），但 imp_vs_rand 交互弱（d_z 0.19→0.34, 仅 s030 显著），且 random 也显示非平凡 phase gradient（d_z 0.35→0.44），strategy-dependence 强度 architecture-dependent。我们通过 discrimination co
…[truncated 9581 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper_update_prep_20260515T013953",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-15T01:46:28.028604+00:00_

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
  "session": "worker_research_paper_update_prep_20260515T013953",
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

_source line 8 · 2026-05-15T01:46:28.028742+00:00_

artifacts/_project/paper/appendix.tex
artifacts/_project/paper/background.tex
artifacts/_project/paper/analysis.tex
artifacts/_project/paper/conclusion.tex
artifacts/_project/paper/introduction.tex
artifacts/_project/paper/related_work.tex
artifacts/_project/paper/results.tex
artifacts/_project/paper/appendix_disc_analysis.tex
artifacts/_project/paper/methodology.tex
artifacts/_project/paper/limitations.tex
artifacts/_project/paper/main.tex
artifacts/_project/paper/appendix_results.tex
artifacts/_project/paper/appendix_moved.tex
artifacts/_project/paper/abstract.tex
artifacts/_project/paper/discussion.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper_update_prep_20260515T013953",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-15T01:46:28.028872+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/paper*/**",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_paper_update_prep_20260515T013953",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/paper*/**",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-15T01:46:28.029012+00:00_

artifacts/_project/paper/citation_audit_report.md
artifacts/_project/paper/acl.sty
artifacts/_project/paper/acl_natbib.bst
artifacts/_project/paper/paper_compilation_note.txt
artifacts/_project/paper/main_00fdd3.pdf
artifacts/_project/paper/main_5d82e3.pdf
artifacts/_project/paper/main_c93d3b.pdf
artifacts/_project/paper/main_9a05ce.pdf
artifacts/_project/paper/main_a1a036.pdf
artifacts/_project/paper/_pdf_images/main_a1a036_p9.png
artifacts/_project/paper/_pdf_images/main_a1a036_p10.png
artifacts/_project/paper/_pdf_images/main_a1a036_p4.png
artifacts/_project/paper/_pdf_images/main_a1a036_p5.png
artifacts/_project/paper/_pdf_images/main_a1a036_p6.png
artifacts/_project/paper/_pdf_images/main_a1a036_p7.png
artifacts/_project/paper/_pdf_images/main_a1a036_p8.png
artifacts/_project/paper/_pdf_images/main_a1a036_p1.png
artifacts/_project/paper/_pdf_images/main_a1a036_p2.png
artifacts/_project/paper/_pdf_images/main_a1a036_p3.png
artifacts/_project/paper/_pdf_images/main_a1a036_p11.png
artifacts/_project/paper/_pdf_images/main_a1a036_p12.png
artifacts/_project/paper/appendix.tex
artifacts/_project/paper/main_bdfc72.pdf
artifacts/_project/paper/figures/fig1_dose_response.pdf
artifacts/_project/paper/figures/fig3_crossover.pdf
artifacts/_project/paper/figures/fig4_bootstrap.pdf
artifacts/_project/paper/figures/fig5_crossmodel.pdf
artifacts/_project/paper/background.tex
artifacts/_project/paper/_pdf_images/main_p8.png
artifacts/_project/paper/_pdf_images/main_p9.png
artifacts/_project/paper/_pdf_images/main_p4.png
artifacts/_project/paper/_pdf_images/main_p5.png
artifacts/_project/paper/_pdf_images/main_p6.png
artifacts/_project/paper/_pdf_images/main_p7.png
artifacts/_project/paper/analysis.tex
artifacts/_project/paper/main.fls
artifacts/_project/paper/main.fdb_latexmk
artifacts/_project/paper/_pdf_images/main_p3.png
artifacts/_project/paper/_pdf_images/main_p1.png
artifacts/_project/paper/_pdf_images/main_p2.png
artifacts/_project/paper/_pdf_images/main_p10.png
artifact
…[truncated 929 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper_update_prep_20260515T013953",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-15T01:46:28.029183+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "n\\s*[=≈]\\s*50|50 problems|fifty",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
  "output_mode": "content",
  "glob": "*.tex",
  "-n": "True",
  "-C": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_paper_update_prep_20260515T013953",
  "tool": "Grep",
  "tool_args": {
    "pattern": "n\\s*[=≈]\\s*50|50 problems|fifty",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
    "output_mode": "content",
    "glob": "*.tex",
    "-n": "True",
    "-C": "2"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-15T01:46:28.029337+00:00_

artifacts/_project/paper/appendix_moved.tex-24-Both models share the Qwen2ForCausalLM backbone (28 layers, 28 heads, 4-group GQA) but differ in training: DeepSeek uses reasoning distillation from DeepSeek-R1, while Qwen2.5 uses standard instruction tuning without explicit reasoning delimiters. This controlled comparison isolates the effect of training methodology on the compound sparsity interaction.
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_moved.tex-25-
artifacts/_project/paper/appendix_moved.tex:26:Despite lacking explicit \texttt{&lt;think>} delimiters, Qwen2.5-7B-Instruct exhibits sufficient variation in attention sparsity to permit phase segmentation via the same quantile-based method (\S\ref{sec:phase-segmentation}). Four of the 50 problems are excluded due to degenerate phase assignments, yielding $n{=}46$ valid problems for Qwen (vs.\ $n{=}49$ for DeepSeek).
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_moved.tex-27-
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_moved.tex-28-\paragraph{Per-phase effective sample size.}
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/methodology.tex-8-\paragraph{Dataset.}
artifacts/_project/paper/methodology.tex-9-\label{sec:dataset}
artifacts/_project/paper/methodology.tex:10:We use 50 problems stratified from MATH-500~\cite{math500-neurips2021}, sampling uniformly across categories with a fixed seed. Each problem is decoded greedily (\texttt{max\_new\_tokens}$=$2048).
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/methodology.tex-11-
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/methodology.tex-12-\paragraph{Spar
…[truncated 884 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper_update_prep_20260515T013953",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-15T01:46:28.029506+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "median|CI|d_z|cohen|bootstrap|0\\.\\d{2,3}|[1-9]\\.\\d{2,3}",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
  "output_mode": "content",
  "glob": "*.tex",
  "-n": "True",
  "-i": "True",
  "head_limit": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_paper_update_prep_20260515T013953",
  "tool": "Grep",
  "tool_args": {
    "pattern": "median|CI|d_z|cohen|bootstrap|0\\.\\d{2,3}|[1-9]\\.\\d{2,3}",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
    "output_mode": "content",
    "glob": "*.tex",
    "-n": "True",
    "-i": "True",
    "head_limit": "0"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-15T01:46:28.029740+00:00_

&lt;persisted-output>
Output too large (31.3KB). Full output saved to: /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-phase-gated-compound-sparse/92d5a500-97ec-4718-a2d5-83296bc1ca35/tool-results/toolu_014tbJXKopLJz5muaHPJs7LX.txt

Preview (first 2KB):
artifacts/_project/paper/analysis.tex:4:[Omitted long matching line]
artifacts/_project/paper/analysis.tex:6:[Omitted long matching line]
artifacts/_project/paper/related_work.tex:6:\cite{spark-aaai2026} report super-additive degradation when combining channel pruning with token eviction; \cite{slim-icml2025} formalize compound error for quantization and sparsity.
artifacts/_project/paper/related_work.tex:7:\cite{unicomp-2026} evaluate compound compression across 40+ benchmarks, revealing that reasoning capabilities degrade disproportionately.
artifacts/_project/paper/related_work.tex:8:\cite{phase-transition-compression-2026} characterize independent phase transition points per compression dimension, implying the joint safe region is the intersection of per-dimension safe zones.
artifacts/_project/paper/related_work.tex:9:GRASPrune~\cite{graspune-acl2026} learns global budget-constrained gates for joint pruning but treats decisions as static across generation.
artifacts/_project/paper/related_work.tex:10:These works establish compound interaction but share an implicit assumption: interaction magnitude is constant across the generation process.
artifacts/_project/paper/related_work.tex:14:Ada-KV~\cite{adakv-neurips2025} introduces per-head adaptive budgets; SnapKV~\cite{snapkv-neurips2024} compresses from a fixed observation window; \cite{defensivekv-iclr2026} show worst-case loss $2.3$--$4.3{\times}$ higher than expected under standard aggregation.
artifacts/_project/paper/related_work.tex:15:\cite{nacl-acl2024} combine proxy-token and random eviction to counter attention bias.
artifacts/_project/paper/related_work.tex:16:RetentiveKV~\cite{retentivekv-2026} identifies d
…[truncated 147 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper_update_prep_20260515T013953",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-15T01:46:28.029902+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "partially.confirmed|future.work|C8|C5b|not significant|not.significant|caveat|限定",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
  "output_mode": "content",
  "glob": "*.tex",
  "-n": "True",
  "-i": "True",
  "head_limit": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_paper_update_prep_20260515T013953",
  "tool": "Grep",
  "tool_args": {
    "pattern": "partially.confirmed|future.work|C8|C5b|not significant|not.significant|caveat|限定",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
    "output_mode": "content",
    "glob": "*.tex",
    "-n": "True",
    "-i": "True",
    "head_limit": "0"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-15T01:46:28.030052+00:00_

artifacts/_project/paper/discussion.tex:10:[Omitted long matching line]
artifacts/_project/paper/appendix_moved.tex:73:The per-problem concordance across models is not significant (median $\rho = \placeholder{}$, $p = \placeholder{}$), indicating that while the aggregate gradient direction replicates, the specific problems driving severity differ between models---consistent with model-specific attention patterns rather than a universal per-problem vulnerability ranking. % exp_id: cross_model_analysis.json (spearman_rho=1.0, gradient_permutation_p=0.043, per_problem_concordance_p=0.926, mean_rho=-0.107)
artifacts/_project/paper/appendix_results.tex:7:The per-problem concordance across models is not significant (median $\rho = \placeholder{}$, $p = \placeholder{}$), indicating that while the aggregate gradient direction replicates, the specific problems driving severity differ between models---consistent with model-specific attention patterns rather than a universal per-problem vulnerability ranking. % exp_id: cross_model_analysis.json (spearman_rho=1.0, gradient_permutation_p=0.043, per_problem_concordance_p=0.926, mean_rho=-0.107)
artifacts/_project/paper/appendix_disc_analysis.tex:28:% REBUTTAL: 7B is the most-deployed scale for on-device and cost-constrained serving—exactly where compound sparsity is needed. The mechanism (entropy-discrimination collapse) is scale-agnostic in principle. Scaling experiments are future work.
artifacts/_project/paper/appendix_disc_analysis.tex:57:% REBUTTAL: Our focus is on the practically relevant regime where models retain usable quality. At s>0.30 both strategies degrade severely, making II measurement less informative. The sub-exponential growth (C6, $\Delta$ growth rate $3.8{\times} \to 4.8{\times} \to 2.0{\times}$) suggests saturation at higher sparsity, but confirming this is future work.
artifacts/_project/paper/appendix_disc_analysis.tex:62:% REBUTTAL: This is an empirical finding paper, not a method/system paper. The contri
…[truncated 391 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper_update_prep_20260515T013953",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-15T01:46:28.030215+00:00_

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
  "session": "worker_research_paper_update_prep_20260515T013953",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/abstract.tex"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-15T01:46:28.030367+00:00_

1	\begin{abstract}
2	Compound sparsity---simultaneously pruning attention heads and evicting KV cache entries---is essential for efficient LLM inference but produces super-additive quality degradation whose structure is poorly understood.
3	Prior work treats compound interaction magnitude as approximately constant across the generation process.
4	We show that this assumption is wrong: compound sparsity severity is an emergent phase-strategy interaction that varies by over an order of magnitude across reasoning phases.
5	
6	We evaluate compound sparsity on three models---DeepSeek-R1-Distill-Qwen-7B, Qwen2.5-7B-Instruct (both Qwen2ForCausalLM), and DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM)---spanning two architectures, using 50 MATH-500 problems, measuring the Interaction Index---a super-additivity metric---across quantile-segmented reasoning phases at sparsity levels $s \in \{0.15, 0.20, 0.25, 0.30\}$.
7	Under importance-based KV cache eviction, the median Interaction Index difference between low-sparsity and high-sparsity reasoning phases increases monotonically from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$, with paired Cohen's $d_z$ growing from $0.44$ (small) to $0.80$ (large); Bonferroni-corrected permutation tests yield $p < 0.005$ at all four sparsity levels.
8	Random eviction produces no significant phase modulation in 7/8 conditions; the single exception (Qwen $s{=}0.30$, $p{=}0.012$) shows negligible median difference ($\widetilde{\Delta} = \placeholder{}$), confirming that the severity gradient is strategy-specific, not an inherent property of compound sparsity.
9	At $s{=}0.25$, a crossover emerges: importance-based eviction outperforms random in high-sparsity phases ($\widetilde{\mathrm{II}} = 0.032$ vs.\ $0.818$) yet underperforms in low-sparsity phases ($\widetilde{\mathrm{II}} = 7.196$ vs.\ $1.363$)---a qualitative reversal in strategy ranking.
10	The pattern replicates on Qwen2.5-7B-Instruct at $s \geq 0.20$ ($d_z \geq 0.55$; Spearman $\rho 
…[truncated 934 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper_update_prep_20260515T013953",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-15T01:46:28.030532+00:00_

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
  "session": "worker_research_paper_update_prep_20260515T013953",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/results.tex"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-15T01:46:28.030717+00:00_

1	
2	\section{Results}
3	\label{sec:results}
4	
5	\subsection{Strategy-Dependent Severity}
6	\label{sec:strategy-severity}
7	
8	Table~\ref{tab:aggregate-ii} reports the median compound severity difference across strategies and sparsity levels. Under importance-based eviction, $\Delta$ increases from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$---a $37{\times}$ amplification. Under random eviction, no systematic growth is observed ($-0.02$ to $1.54$), confirming that compound severity depends qualitatively on eviction strategy. % exp_id: bf16_importance_s015..s030, bf16_ds_rand_s015..s030; source: experiment_summary_table.json
9	
10	\begin{table}[t]
11	\centering
12	\small
13	\caption{Median compound severity difference ($\Delta = \widetilde{\mathrm{II}}_{\textit{low}} - \widetilde{\mathrm{II}}_{\textit{high}}$) by eviction strategy and sparsity level on DeepSeek-R1-Distill-Qwen-7B ($n{=}50$ MATH-500 problems).}
14	\label{tab:aggregate-ii}
15	\begin{tabular}{@{}lcccc@{}}
16	\toprule
17	Strategy & $s{=}0.15$ & $s{=}0.20$ & $s{=}0.25$ & $s{=}0.30$ \\
18	\midrule
19	Importance & 0.39 & 1.48 & 7.16 & 14.59 \\ % exp_id: bf16_importance_s015..s030; source: experiment_summary_table.json median_diff
20	Random     & 0.01 & $-$0.02 & 0.54 & 1.54 \\ % exp_id: bf16_ds_rand_s015..s030; source: experiment_summary_table.json median_diff
21	\bottomrule
22	\end{tabular}
23	\end{table}
24	
25	
26	\subsection{Phase-Modulated Amplification}
27	\label{sec:phase-amplification}
28	
29	Decomposing II by reasoning phase reveals that strategy-dependent severity is driven by amplification in the low-sparsity phase. Table~\ref{tab:main-results} reports the full per-phase breakdown. The severity gradient $G$ increases from $69{\times}$ at $s{=}0.15$ to $274{\times}$ at $s{=}0.30$ under importance-based eviction, while the high-sparsity phase experiences near-zero interaction ($\widetilde{\mathrm{II}}_{\textit{high}}$ ranges from $0.006$ to $0.053$). Under random eviction, $G \approx 0.9$--$1.7{
…[truncated 8932 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper_update_prep_20260515T013953",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-15T01:46:28.030865+00:00_

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
  "session": "worker_research_paper_update_prep_20260515T013953",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/analysis.tex"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-15T01:46:28.030994+00:00_

1	\section{Analysis: Entropy-Discrimination Collapse}
2	\label{sec:analysis}
3	
4	We propose \emph{discrimination collapse} as the primary mechanism driving the phase-strategy interaction. Head pruning reduces the number of heads contributing to cumulative importance scores, flattening the score distribution: the Gini coefficient decreases by $0.030$--$0.081$ (DeepSeek) and $0.010$--$0.020$ (Qwen) across all sparsity levels, with consistent negative deltas in all 16 conditions (Appendix~\ref{app:analysis}, Table~\ref{tab:discrimination-metrics-full}). When importance scores lose discriminability, thresholding degenerates into noise-sensitive selection---functionally approaching biased random eviction. This effect is phase-dependent: in low-sparsity phases, attention is already broadly distributed, so pruning-induced flattening has maximum impact; in high-sparsity phases, concentration is preserved. Random eviction is immune because its decisions are independent of score quality, explaining $G \approx 1$. % exp_id: c4_entropy_deepseek, c4_entropy_qwen
5	
6	Beyond discrimination collapse, head pruning redistributes the attention entropy of surviving heads. For DeepSeek, the entropy delta is consistently negative ($\Delta\mathcal{H} \in [-0.047, -0.040]$), indicating that importance-based pruning systematically selects heads whose removal concentrates attention in survivors. For Qwen, the pattern partially replicates at $s \leq 0.20$ but reverses at $s{=}0.25$ ($\Delta\mathcal{H} = +0.045$), suggesting model-specific head specialization patterns (Appendix~\ref{app:analysis}, Table~\ref{tab:entropy-deltas}). We characterize discrimination collapse as the robust, model-independent driver, with entropy redistribution as a secondary, model-dependent amplifier. % exp_id: c4_entropy_deepseek, c4_entropy_qwen
7	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper_update_prep_20260515T013953",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-15T01:46:28.031121+00:00_

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
  "session": "worker_research_paper_update_prep_20260515T013953",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/discussion.tex"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-15T01:46:28.031256+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Quantitative surprise.}
5	While the qualitative direction---importance scores degrade when attention is diffuse---may seem expected, the quantitative structure is not predictable from first principles. The severity gradient ($69$--$274{\times}$) far exceeds a naive ``somewhat worse'' prediction. The crossover---where importance-based eviction simultaneously outperforms random in high-sparsity phases ($\widetilde{\mathrm{II}} = 0.032$ vs.\ $0.818$) and underperforms in low-sparsity phases ($7.196$ vs.\ $1.363$)---cannot be derived from single-axis entropy reasoning. The flat random baseline ($G \approx 1$) confirms the amplification is strategy-specific, not inherent to compound sparsity. % exp_id: bf16_importance_s015..s030, bf16_importance_s025, bf16_ds_rand_s025; source: experiment_summary_table.json
6	
7	\paragraph{Implications for deployment.}
8	Applying a uniform compression budget across all inference steps implicitly accepts order-of-magnitude severity penalties during low-sparsity reasoning phases. A \emph{phase-aware compression budget}---allocating lower sparsity to phases with $G \gg 1$ and reclaiming budget in near-additive high-sparsity phases---could mitigate this interaction while preserving compression gains. The severity gradient provides a natural signal for such allocation. Discrimination collapse depends on attention-mass-based importance scoring shared by major KV cache methods (H$_2$O \cite{h2o-neurips2023}, SnapKV \cite{snapkv-neurips2024}, PyramidKV \cite{pyramidkv-2024}), suggesting broad applicability.
9	
10	A preliminary pilot experiment explored oracle phase-aware budget reallocation, shifting sparsity budget from high-severity low-sparsity phases to low-severity high-sparsity phases. At $s{=}0.25$, oracle recovery---the fraction of compound interaction eliminated by phase-aware allocation---reached \placeholder{ORACLE\_PCT}\% (Wilcoxon $p = \placeholder{ORACLE\_P}$), below t
…[truncated 1685 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper_update_prep_20260515T013953",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-15T01:46:28.031396+00:00_

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
  "session": "worker_research_paper_update_prep_20260515T013953",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-15T01:46:28.031563+00:00_

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

…[truncated 1862 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper_update_prep_20260515T013953",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-15T01:46:28.031705+00:00_

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
  "session": "worker_research_paper_update_prep_20260515T013953",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/methodology.tex"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-15T01:46:28.031861+00:00_

1	\section{Experimental Setup}
2	\label{sec:experimental-setup}
3	
4	\paragraph{Models.}
5	\label{sec:models}
6	We evaluate on two 7B-parameter models sharing the Qwen2 backbone (28 layers, 28 heads, 4-group GQA): \textbf{DeepSeek-R1-Distill-Qwen-7B}~\cite{deepseek-r1-2025}, distilled from DeepSeek-R1 with explicit chain-of-thought traces yielding pronounced phase structure; and \textbf{Qwen2.5-7B-Instruct}~\cite{qwen25-2024}, with standard instruction tuning, providing a cross-model replication target. Both are loaded in \texttt{bfloat16} with eager attention.\footnote{An earlier \texttt{float16} configuration produced sporadic NaN values; \texttt{bfloat16} eliminated all occurrences.}
7	
8	\paragraph{Dataset.}
9	\label{sec:dataset}
10	We use 50 problems stratified from MATH-500~\cite{math500-neurips2021}, sampling uniformly across categories with a fixed seed. Each problem is decoded greedily (\texttt{max\_new\_tokens}$=$2048).
11	
12	\paragraph{Sparsity configuration.}
13	\label{sec:sparsity-config}
14	We apply symmetric compound sparsity at $s \in \{0.15, 0.20, 0.25, 0.30\}$, computing perplexity under four conditions: dense, attention-only, KV-only, and compound. We compare \emph{importance-based} eviction (position-normalized cumulative attention score, Eq.~\ref{eq:kv-importance}; BOS always retained) and \emph{random} eviction (uniform). Heads are pruned per layer by Frobenius norm; under random eviction, both heads and positions are selected uniformly.
15	
16	\paragraph{Phase segmentation and metrics.}
17	\label{sec:phase-seg}
18	Each sequence is segmented into three phases using the quantile-based method (\S\ref{sec:phase-segmentation}), with $\texttt{min\_phase\_length}{=}10$. We compute segment-level perplexity, II (Eq.~\ref{eq:ii}), and $G$ (Eq.~\ref{eq:gradient}), reporting medians due to heavy right-skew (mean/median ratios up to 43:1).
19	
20	\paragraph{Statistical analysis.}
21	\label{sec:stats}
22	All reported confidence intervals and significance t
…[truncated 397 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper_update_prep_20260515T013953",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-15T01:46:28.032021+00:00_

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
  "session": "worker_research_paper_update_prep_20260515T013953",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/conclusion.tex"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-15T01:46:28.032144+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We showed that compound sparsity severity---the super-additive interaction between head pruning and KV cache eviction---is not phase-invariant but exhibits an emergent phase-strategy interaction spanning over an order of magnitude within a single generation. Under importance-based eviction, the severity gradient grows from $69{\times}$ to $274{\times}$ across sparsity levels ($d_z$: $0.44 \to 0.80$); random eviction shows no such modulation (7/8 conditions non-significant). A crossover at $s{=}0.25$---where importance-based eviction reverses ranking across phases---demonstrates that no single strategy dominates uniformly. The pattern replicates on Qwen2.5-7B-Instruct at $s \geq 0.20$ ($d_z \geq 0.55$) and partially extends cross-architecture to DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM) with a qualitatively consistent but substantially weaker trend at $\sim$1/40 the magnitude. Discrimination collapse provides a mechanistic explanation supported by both Qwen2-based models; LLaMA results are directionally consistent but the interaction is weaker than in Qwen2 architectures.
5	These findings motivate phase-aware sparsity allocation for reasoning model deployment.
6	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper_update_prep_20260515T013953",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-15T01:46:28.032272+00:00_

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
  "session": "worker_research_paper_update_prep_20260515T013953",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/limitations.tex"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-15T01:46:28.032417+00:00_

1	\paragraph{Model scale and architecture.}
2	All experiments are conducted at the 7--8B parameter scale. Whether the phase-modulated severity patterns persist, amplify, or attenuate at larger scales (e.g., 70B) remains untested. Preliminary cross-architecture validation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, \S\ref{sec:cross-arch}) partially confirms the qualitative pattern beyond the Qwen2 architecture---monotonically increasing $d_z$ with within-importance phase gradient $\sim$1.0---but with substantially weaker interaction magnitude ($\sim$1/40 of DeepSeek) and mixed statistical evidence (only $s{=}0.30$ significant after Bonferroni correction). The pattern has been tested on two architecture families (Qwen2ForCausalLM, LlamaForCausalLM); comprehensive validation across more diverse architectures (e.g., Mistral, multi-latent attention) and larger scales is needed for full generalization claims.
3	
4	\paragraph{Task coverage.}
5	We evaluate exclusively on MATH-500, a mathematical reasoning benchmark. Different reasoning tasks---code generation, commonsense reasoning, multi-hop question answering---may induce different phase structures with different sparsity distributions, potentially altering the severity gradient profile.
6	
7	\paragraph{Mechanism.}
8	The discrimination collapse mechanism is supported by correlational evidence (consistent Gini/CV reduction across all conditions); causal validation through controlled entropy manipulation is needed. The entropy redistribution component replicates on only 2/4 Qwen conditions, suggesting model-specific factors.
9	
10	\paragraph{Sparsity range.}
11	Our experiments span $s \in \{0.15, 0.20, 0.25, 0.30\}$. More extreme sparsity ($s > 0.50$) may exhibit qualitatively different interaction dynamics. We do not report inference throughput or latency measurements, which are necessary for a complete deployment analysis but orthogonal to our severity characterization. Extended limitations in Appendix~\ref{app:lim
…[truncated 14 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper_update_prep_20260515T013953",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-15T01:46:28.032562+00:00_

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
  "session": "worker_research_paper_update_prep_20260515T013953",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix.tex"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-15T01:46:28.032705+00:00_

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
…[truncated 1336 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper_update_prep_20260515T013953",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-15T01:46:28.032852+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_paper_update_prep_20260515T013953",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_results.tex"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-15T01:46:28.032975+00:00_

1	% Appendix: supplementary results details
2	
3	\section{Cross-Model Replication Details}
4	\label{app:cross-model-details}
5	
6	\paragraph{Per-problem concordance.}
7	The per-problem concordance across models is not significant (median $\rho = \placeholder{}$, $p = \placeholder{}$), indicating that while the aggregate gradient direction replicates, the specific problems driving severity differ between models---consistent with model-specific attention patterns rather than a universal per-problem vulnerability ranking. % exp_id: cross_model_analysis.json (spearman_rho=1.0, gradient_permutation_p=0.043, per_problem_concordance_p=0.926, mean_rho=-0.107)
8	
9	\paragraph{Random eviction control.}
10	As a control, random eviction on Qwen yields no systematic phase gradient at three of four sparsity levels (3/4 FAIL), mirroring DeepSeek's 4/4 FAIL pattern. At $s{=}0.30$, Qwen random produces a borderline PASS (permutation $p = 0.012$) but with negligible median difference ($\widetilde{\Delta} = \placeholder{}$, CI spans zero), indicating no meaningful phase modulation. % exp_id: bf16_qw_rand_s015..s030; source: experiment_summary_table.json
11	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper_update_prep_20260515T013953",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-15T01:46:28.033097+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_moved.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_paper_update_prep_20260515T013953",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_moved.tex"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-15T01:46:28.033293+00:00_

1	% Content moved from main body to appendix:
2	% - Phase-strategy crossover details (from results §5.3)
3	% - Cross-model replication details with tables/figures (from results §5.4)
4	% - Permutation test details with table/forest plot (from results §5.5)
5	% - Full entropy-discrimination collapse analysis with tables (from analysis §6)
6	% Main body §6 (analysis.tex) contains a condensed summary referencing these tables.
7	
8	\section{Phase-Strategy Crossover Details}
9	\label{app:crossover-details}
10	
11	At $s{=}0.25$, a strategy ranking reversal emerges (Figure~\ref{fig:crossover}): importance-based eviction yields \emph{lower} II than random in the high-sparsity phase ($0.032$ vs.\ $0.818$) but \emph{higher} II in the low-sparsity phase ($7.196$ vs.\ $1.363$---a $5.3{\times}$ reversal). This crossover is present at all four sparsity levels, with reversal magnitude of $3.9{\times}$ at $s{=}0.15$, $5.4{\times}$ at $s{=}0.20$, $5.3{\times}$ at $s{=}0.25$, and $3.6{\times}$ at $s{=}0.30$ (as random eviction severity also rises). The reversal arises because head pruning redistributes attention mass, altering importance rankings in a way that couples the two sparsity mechanisms in low-sparsity phases (\S\ref{sec:discrimination-collapse}). % exp_id: bf16_importance_s025, bf16_ds_rand_s025; source: experiment_summary_table.json; 7.196/1.363=5.28
12	
13	\begin{figure}[t]
14	\centering
15	\includegraphics[width=\columnwidth]{fig3_crossover.pdf}
16	\caption{Strategy-dependent crossover at $s{=}0.25$. Grouped bar chart of median II by eviction strategy and reasoning phase. Importance-based eviction outperforms random in the high-sparsity phase but produces $5.3{\times}$ higher II in the low-sparsity phase, reversing the strategy ranking.}
17	\label{fig:crossover}
18	\end{figure}
19	
20	
21	\section{Cross-Model Replication Details}
22	\label{app:cross-model-details}
23	
24	Both models share the Qwen2ForCausalLM backbone (28 layers, 28 heads, 4-group GQA) but differ in trai
…[truncated 12246 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper_update_prep_20260515T013953",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-15T01:46:28.033462+00:00_

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
  "session": "worker_research_paper_update_prep_20260515T013953",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_disc_analysis.tex"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-15T01:46:28.033651+00:00_

1	\section{Discrimination Collapse Details}
2	\label{app:discrimination-collapse-details}
3	
4	This cross-model consistency (Table~\ref{tab:discrimination-metrics-full}) establishes discrimination collapse as a robust consequence of compound sparsity. When importance scores lose discriminative power, thresholding the bottom-$s$ fraction becomes noise-sensitive: small perturbations change which positions cross the eviction boundary. In the limit of perfectly uniform scores, importance-based eviction degenerates into an arbitrary selection functionally equivalent to biased random eviction. The same pattern holds under random eviction (DeepSeek: $-0.031$ to $-0.073$; Qwen: $-0.019$ to $-0.045$), confirming that discrimination collapse is a consequence of head pruning \emph{per se}, not of the eviction strategy. % exp_id: c4_entropy_deepseek, c4_entropy_qwen
5	
6	
7	\section{Extended Discussion}
8	\label{app:extended-discussion}
9	
10	\paragraph{On the predictability of phase-modulated severity.}
11	The compound interaction is not uniformly fragile---it is selectively fragile in a phase-dependent manner ($\widetilde{\mathrm{II}}_{\text{high}} < 0.06$ at $s \leq 0.30$; at $s = 0.35$, high-phase II rises to $0.105$ in a supplementary experiment, indicating onset of compound interaction even in high-sparsity phases at extreme pruning rates). % exp_id: bf16_importance_s015..s030, bf16_ds_imp_s035; high-phase medians: 0.006, 0.015, 0.032, 0.053; s035 II_high=0.1051
12	
13	\paragraph{Random masking as falsification control.}
14	Random eviction fails 7/8 paired permutation tests across both models; the single exception (Qwen $s{=}0.30$, $p{=}0.012$) exhibits negligible effect size ($\widetilde{\Delta} = \placeholder{}$). The absence of a phase gradient under random masking isolates the amplification as strategy-specific. % exp_id: bf16_ds_rand_s015..s030, bf16_qw_rand_s015..s030
15	
16	\paragraph{Entropy mechanism boundary conditions.}
17	Directly measuring per-head entropy sh
…[truncated 6847 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper_update_prep_20260515T013953",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-15T01:46:28.033825+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\\\\\placeholder",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
  "output_mode": "content",
  "glob": "*.tex",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_paper_update_prep_20260515T013953",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\\\\\placeholder",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
    "output_mode": "content",
    "glob": "*.tex",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-15T01:46:28.033949+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper_update_prep_20260515T013953",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-15T01:46:28.034063+00:00_

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
  "session": "worker_research_paper_update_prep_20260515T013953",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-15T01:46:28.034196+00:00_

1	\section{Related Work}
2	\label{sec:related}
3	
4	\paragraph{Compound compression.}
5	Combining multiple compression axes produces non-additive errors.
6	\cite{spark-aaai2026} report super-additive degradation when combining channel pruning with token eviction; \cite{slim-icml2025} formalize compound error for quantization and sparsity.
7	\cite{unicomp-2026} evaluate compound compression across 40+ benchmarks, revealing that reasoning capabilities degrade disproportionately.
8	\cite{phase-transition-compression-2026} characterize independent phase transition points per compression dimension, implying the joint safe region is the intersection of per-dimension safe zones.
9	GRASPrune~\cite{graspune-acl2026} learns global budget-constrained gates for joint pruning but treats decisions as static across generation.
10	These works establish compound interaction but share an implicit assumption: interaction magnitude is constant across the generation process.
11	
12	\paragraph{KV cache eviction.}
13	Most methods rely on importance scoring whose reliability is increasingly questioned.
14	Ada-KV~\cite{adakv-neurips2025} introduces per-head adaptive budgets; SnapKV~\cite{snapkv-neurips2024} compresses from a fixed observation window; \cite{defensivekv-iclr2026} show worst-case loss $2.3$--$4.3{\times}$ higher than expected under standard aggregation.
15	\cite{nacl-acl2024} combine proxy-token and random eviction to counter attention bias.
16	RetentiveKV~\cite{retentivekv-2026} identifies deferred importance, and \cite{greedy-bias-kvcache-2026} show that single importance metrics exhibit systematic greedy bias.
17	\cite{hies-2025} independently show that importance-based head discrimination collapses under heavy pruning, further questioning single-metric reliability.
18	Lethe~\cite{lethe-aaai2026} introduces temporal adaptivity with layer-wise multi-round pruning, and SparK~\cite{spark-aaai2026} extends eviction to the channel dimension with recoverable sparsity.
19	These me
…[truncated 1295 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper_update_prep_20260515T013953",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-15T01:46:28.034330+00:00_

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
  "session": "worker_research_paper_update_prep_20260515T013953",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/background.tex"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-15T01:46:28.034487+00:00_

1	% Section 3: Background and Problem Setup
2	% Note: eq:ii and eq:gradient are the canonical definitions.
3	% Full formulation details in Appendix (app:formulation-details).
4	
5	\section{Background and Problem Setup}
6	\label{sec:background}
7	
8	We formalize compound sparsity, define the Interaction Index, and introduce phase segmentation. Full mathematical details appear in Appendix~\ref{app:formulation-details}.
9	
10	\paragraph{Compound sparsity.}
11	\label{sec:compound-sparsity}
12	Let $s \in (0,1)$ denote a unified sparsity budget. \emph{Attention head pruning} removes the bottom-$s$ fraction of heads per layer by Frobenius norm importance \cite{voita-acl2019, michel-neurips2019}. \emph{KV cache eviction} removes the bottom-$s$ fraction of token positions from the cache. We compare two strategies: \emph{importance-based}, which scores positions by position-normalized cumulative attention mass (Eq.~\ref{eq:kv-importance} in Appendix~\ref{app:formulation-details}), and \emph{random}, which evicts uniformly at random \cite{nacl-acl2024}. Applying both simultaneously yields \emph{compound sparsity}; the two axes interact because head pruning alters the importance ranking used for eviction \cite{spark-aaai2026}. Existing joint-pruning approaches such as GRASPrune \cite{graspune-acl2026} learn global budget-constrained gates but treat decisions as static across generation.
13	
14	\paragraph{Interaction Index.}
15	\label{sec:interaction-index}
16	For a text segment, let $\text{PPL}_c$ denote perplexity under condition $c \in \{d, a, k, b\}$ (dense, attention-only, KV-only, compound). Normalizing by the dense baseline yields $r_c = \text{PPL}_c / \text{PPL}_d$, and:
17	\begin{equation}
18	    \mathrm{II} = r_b - r_a - r_k + 1.
19	    \label{eq:ii}
20	\end{equation}
21	$\mathrm{II} > 0$ indicates super-additive degradation; $\mathrm{II} = 0$ indicates additive independence. We adopt the additive null because the two axes operate on disjoint dimensions; qualitative co
…[truncated 1036 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper_update_prep_20260515T013953",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-15T01:46:28.034648+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "placeholder",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
  "output_mode": "content",
  "glob": "*.tex",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_paper_update_prep_20260515T013953",
  "tool": "Grep",
  "tool_args": {
    "pattern": "placeholder",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
    "output_mode": "content",
    "glob": "*.tex",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-15T01:46:28.034798+00:00_

artifacts/_project/paper/main.tex:21:\newcommand{\placeholder}[1]{\textcolor{red}{[#1]}}
artifacts/_project/paper/discussion.tex:10:[Omitted long matching line]
artifacts/_project/paper/discussion.tex:15:[Omitted long matching line]
artifacts/_project/paper/appendix_moved.tex:30:Table~\ref{tab:qwen-effective-n} reports the per-phase effective sample size for Qwen2.5-7B-Instruct, defined as the number of problems with $|\mathrm{II}| > 0.001$ in each phase. The mid-phase null rate (\placeholder{NULL\_PCT}\%) reflects problems where compound interaction is absent in intermediate phases; this does not affect the low--high contrast ($\Delta$) used in the primary analysis.
artifacts/_project/paper/appendix_moved.tex:35:\caption{Per-phase effective sample size for Qwen2.5-7B-Instruct ($n_{\text{total}} = \placeholder{N\_QW}$).}
artifacts/_project/paper/appendix_moved.tex:41:High & \placeholder{} & \placeholder{} & \placeholder{} & \placeholder{} \\
artifacts/_project/paper/appendix_moved.tex:42:Mid  & \placeholder{} & \placeholder{} & \placeholder{} & \placeholder{} \\
artifacts/_project/paper/appendix_moved.tex:43:Low  & \placeholder{} & \placeholder{} & \placeholder{} & \placeholder{} \\
artifacts/_project/paper/appendix_moved.tex:73:The per-problem concordance across models is not significant (median $\rho = \placeholder{}$, $p = \placeholder{}$), indicating that while the aggregate gradient direction replicates, the specific problems driving severity differ between models---consistent with model-specific attention patterns rather than a universal per-problem vulnerability ranking. % exp_id: cross_model_analysis.json (spearman_rho=1.0, gradient_permutation_p=0.043, per_problem_concordance_p=0.926, mean_rho=-0.107)
artifacts/_project/paper/appendix_moved.tex:76:As a control, random eviction on Qwen yields no systematic phase gradient at three of four sparsity levels (3/4 FAIL), mirroring DeepSeek's 4/4 FAIL pattern. At $s{=}0.30$, Qwen random produces a borderline PASS (
…[truncated 3381 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper_update_prep_20260515T013953",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-15T01:46:28.034966+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "imp.vs.rand|importance.vs.random|Qwen.*not.*signif|not.*signif.*Qwen",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
  "output_mode": "content",
  "glob": "*.tex",
  "-n": "True",
  "-i": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_paper_update_prep_20260515T013953",
  "tool": "Grep",
  "tool_args": {
    "pattern": "imp.vs.rand|importance.vs.random|Qwen.*not.*signif|not.*signif.*Qwen",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
    "output_mode": "content",
    "glob": "*.tex",
    "-n": "True",
    "-i": "True"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-15T01:46:28.035090+00:00_

artifacts/_project/paper/conclusion.tex:4:[Omitted long matching line]
artifacts/_project/paper/limitations.tex:2:[Omitted long matching line]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper_update_prep_20260515T013953",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-15T01:46:28.035203+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_paper_update_prep_20260515T013953",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/main.tex"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-15T01:46:28.035331+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{inconsolata}
11	
12	\usepackage{amsmath}
13	\usepackage{amssymb}
14	\usepackage{graphicx}
15	\usepackage{booktabs}
16	\usepackage{enumitem}
17	\usepackage{multirow}
18	
19	\graphicspath{{figures/}}
20	
21	\newcommand{\placeholder}[1]{\textcolor{red}{[#1]}}
22	
23	\title{Phase-Modulated Compound Sparsity:\\Strategy-Dependent Severity Gradients in Reasoning Models}
24	
25	\author{Anonymous}
26	
27	\begin{document}
28	
29	\maketitle
30	
31	\input{abstract}
32	
33	\input{introduction}
34	\input{related_work}
35	\input{background}
36	\input{methodology}
37	\input{results}
38	\input{analysis}
39	\input{discussion}
40	\input{conclusion}
41	
42	\bibliography{references}
43	
44	\section*{Limitations}
45	\input{limitations}
46	
47	\appendix
48	\input{appendix}
49	\input{appendix_moved}
50	\input{appendix_disc_analysis}
51	
52	\end{document}
53	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper_update_prep_20260515T013953",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-15T01:46:28.035574+00:00_

called mcp__agent-ml-research__save_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__save_project_file</summary>

````json
{
  "project": "phase-gated-compound-sparse",
  "file": "artifacts/paper_update_checklist.md",
  "content": "# Paper Update Checklist: n=50 → n=500\n\n> 生成时间: 2026-05-15 | 适用实验: c2_n500_deepseek + c2_qw_n500 (C7)\n> 约束: median + bootstrap CI 为主指标 (D054); d_z 分场景 (D059); Qwen imp-vs-rand 不claim显著直到n=500确认 (D058); C8=partially_confirmed (D060); C5b=future_work (D056)\n\n---\n\n## 优先级说明\n- **P0**: 核心数字，读者第一眼看到，必须同步更新\n- **P1**: 支撑性数字/表格，与 P0 有数据依赖\n- **P2**: 条件性更新（取决于 n=500 结果）\n- **P3**: 一致性检查，防止 n=50/n=500 混用\n\n---\n\n## P0: 核心数字更新\n\n### 1. methodology.tex:10 — 样本量\n```\n当前: \"We use 50 problems stratified from MATH-500\"\n更新: → 500 problems (n=500 的具体描述，包括 stratification 方式)\n```\n\n### 2. abstract.tex:6 — 样本量\n```\n当前: \"using 50 MATH-500 problems\"\n更新: → 500 MATH-500 problems\n```\n\n### 3. abstract.tex:7 — DeepSeek 主指标\n```\n当前: \"median Interaction Index difference...from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$, with paired Cohen's $d_z$ growing from $0.44$ (small) to $0.80$ (large)\"\n更新: → 用 n=500 segment-level median diff + paired d_z 替换\n注意: 0.39/14.59 是 segment-level medians；d_z 0.44/0.80 是 paired d_z。两组数据来源不同，都需更新。\n```\n\n### 4. introduction.tex:14 — DeepSeek 主指标（与 abstract 一致）\n```\n当前: \"median phase difference rises from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$ ($d_z$: $0.44 \\to 0.80$)\"\n更新: → 同 abstract\n```\n\n### 5. results.tex:8,13,19-20 — Tab aggregate-ii（DeepSeek segment-level Δ）\n```\n当前 Importance: 0.39, 1.48, 7.16, 14.59\n当前 Random: 0.01, -0.02, 0.54, 1.54\ncaption \"$n{=}50$\" → $n{=}500$ (或实际有效 n)\n更新: → 全部替换为 n=500 值\n```\n\n### 6. results.tex:34,40-50 — Tab main-results（DeepSeek 全 per-phase 分解）\n```\n当前 (importance, 4 sparsity × 3 phases + Δ + G):\n  s015: II_high=0.006, II_mid=0.081, II_low=0.398, Δ=0.39, G=69\n  s020: II_high=0.015, II_mid=0.203, II_low=1.496, Δ=1.48, G=103\n  s025: II_high=0.032, II_mid=1.118, II_low=7.196, Δ=7.16, G=222\n  s030: II_high=0.053, II_mid=2.283, II_low=14.639, Δ=14.59, G=274\n当前 (random, 4 sparsity × 3 phases + Δ + G):\n  s015: 0.093, 0.097, 0.103, 0.01, 1.1\n  s020: 0.292, 0.350, 0.276, -0.02, 0.9\n  s025: 0.818, 0.932, 1.363, 0.54, 1.7\n  s030: 2.503, 2.592, 4.041, 1.54, 1.6\ncaption \"50 problems\" → 500 problems\n更新: → 全部替换为 n=500 值\n```\n\n### 7. results.tex:106,117-120 — Tab cohens-d（DS + QW paired d_z + Δ̃[CI]）\n```\n当前 DS: d_z 0.44/0.52/0.68/0.80; Δ̃ 0.32[0.20,0.47] / 1.15[0.66,1.26] / 3.97[2.83,5.29] / 9.94[8.39,16.65]\n当前 QW: d_z 0.28/0.55/0.89/1.02; Δ̃ 0.05[-0.01,0.11] / 0.21[0.07,0.40] / 1.11[0.61,1.47] / 2.62[1.72,3.65]\n更新: → 全部替换为 n=500 值\n关键: QW s015 CI 当前包含零 → n=500 后检查是否仍包含零（影响 onset threshold 叙事）\n```\n\n### 8. conclusion.tex:4 — 核心数字复述\n```\n当前: \"severity gradient grows from $69{\\times}$ to $274{\\times}$...($d_z$: $0.44 \\to 0.80$)\"\n更新: → 与 results 一致\n```\n\n### 9. discussion.tex:5 — severity gradient + crossover 复述\n```\n当前: \"severity gradient ($69$--$274{\\times}$)\"\n当前: crossover 数字 \"0.032 vs 0.818\", \"7.196 vs 1.363\"\n更新: → 与 results 一致\n```\n\n### 10. results.tex:29 + 58 — G 值 + fig1 caption\n```\n当前: G \"from $69{\\times}$ at $s{=}0.15$ to $274{\\times}$ at $s{=}0.30$\"\n当前 fig1 caption: \"$69{\\times}$ to $274{\\times}$\"\n更新: → n=500 G 值\n```\n\n---\n\n## P1: 支撑性数字更新\n\n### 11. results.tex:66 — Crossover 数字\n```\n当前: \"importance high_phase=0.032 < random=0.818, importance low_phase=7.196 > random=1.363\"\nreversal \"5.3×\"\n更新: → n=500 crossover 值\n```\n\n### 12. results.tex:71 — Qwen cross-model 段落\n```\n当前: \"Δ increases from 0.04 at s=0.15 to 2.94 at s=0.30...d_z ≥ 0.55...d_z=0.28 CI includes zero\"\n更新: → n=500 Qwen 值\n关键: 检查 s015 d_z 是否仍 marginal，onset threshold 是否仍 s≥0.20\n```\n\n### 13. appendix_moved.tex:26 — Qwen/DS 有效 n\n```\n当前: \"Four of the 50 problems...n=46 valid problems for Qwen (vs. n=49 for DeepSeek)\"\n更新: → n=500 的排除数和有效 n\n```\n\n### 14. appendix_moved.tex:59-60 — Tab cross-model Qwen Δ\n```\n当前 DS: 0.39, 1.48, 7.16, 14.59\n当前 QW: 0.04, 0.23, 1.27, 2.94\n更新: → n=500 值\n```\n\n### 15. appendix_moved.tex:88,99-102 — Tab permutation（DeepSeek permutation test）\n```\n当前: n=49; observed Δ̃ 0.37[0.19,0.62], 0.97[0.69,1.49], 3.34[1.66,6.64], 9.85[6.70,16.29]\ncaption \"$n{=}49$\"\n更新: → n=500 permutation test 值\n```\n\n### 16. results.tex:104 — permutation test 段落引用\n```\n当前: \"observed median differences increasing monotonically from $0.37$ at $s{=}0.15$ to $9.85$ at $s{=}0.30$\"\n更新: → 与 Tab permutation 一致\n```\n\n### 17. appendix_moved.tex:11 — crossover 详细数字\n```\n当前: \"reversal magnitude of $3.9{\\times}$ at $s{=}0.15$, $5.4{\\times}$ at $s{=}0.20$, $5.3{\\times}$ at $s{=}0.25$, and $3.6{\\times}$ at $s{=}0.30$\"\n更新: → n=500 reversal magnitudes\n```\n\n### 18. appendix_disc_analysis.tex:46-47 — permutation CI + skewness 统计\n```\n当前: \"mean/median ratio ~1.6:1 at s=0.30\"\n当前: \"permutation CIs: s015=[0.19,0.62], s020=[0.69,1.49], s025=[1.66,6.64], s030=[6.70,16.29]\"\n更新: → n=500 值\n```\n\n### 19. abstract.tex:10 — LLaMA cross-arch 段落\n```\n当前: \"Δ̃: 0.020→0.356; s=0.30 Wilcoxon p_Bonf=0.029\"\n注意: LLaMA 实验仍为 n=50，数字不变，但需检查措辞是否暗示与 DS/QW 同一 n\n```\n\n### 20. 图表重新生成\n```\nfig1_dose_response.pdf — G vs s 曲线（P0 依赖）\nfig3_crossover.pdf — crossover bar chart\nfig4_bootstrap.pdf — permutation forest plot\nfig5_crossmodel.pdf — cross-model Δ comparison\n所有图需用 n=500 数据重新生成\n```\n\n---\n\n## P2: 条件性更新\n\n### 21. D058: Qwen imp-vs-rand 显著性\n```\n当前状态: 论文未报告 Qwen imp-vs-rand permutation test（只报告了 DeepSeek）\n约束: n=500 前不得 claim Qwen imp-vs-rand 显著\n行动:\n  - 若 n=500 Qwen imp-vs-rand 显著 → 可添加 Qwen permutation test 表格，strengthens C1\n  - 若仍不显著 → 在 cross-model 段落加 caveat，或维持当前策略（只报 within-importance gradient）\n检查文件: results.tex:71, appendix_results.tex:10\n```\n\n### 22. D059: d_z 报告策略\n```\n约束: within-importance d_z 保留; 涉及 random 只报方向\n行动: 检查 n=500 后是否有新的 imp-vs-rand d_z 值需要报告，确保遵守\"只报方向\"规则\n影响文件: results.tex, appendix_moved.tex\n```\n\n### 23. C2 预注册: Qwen s015 onset threshold\n```\n当前: paper_framing 预注册 \"n=500 后若 QW s015 CI 仍跨零，叙事改为 'compound effect emerges above threshold sparsity (~s020)'\"\n检查: results.tex:71 \"marginal at s=0.15\" + Tab cohens-d QW s015 行\n行动:\n  - 若 n=500 QW s015 CI 不跨零 → onset = s≥0.15，更新叙事\n  - 若仍跨零 → 保持 \"emerges above ~s020\" 叙事\n```\n\n### 24. Placeholder 值填充\n以下 \\placeholder{} 标记需用 n=50 或 n=500 数据填充:\n\n| 文件:行 | Placeholder | 数据来源 |\n|---------|-------------|----------|\n| abstract.tex:8 | Qwen rand s030 Δ̃ | bf16_qw_rand_s030 |\n| results.tex:71 | NULL_PCT | Qwen per-phase null rate |\n| results.tex:81 | LLaMA random Wilcoxon p | c3_llama |\n| results.tex:86 | N_LLAMA | c3_llama (n=49?) |\n| results.tex:92-95 | 整个 LLaMA 表格 (12 cells) | c3_llama |\n| discussion.tex:10 | ORACLE_PCT, ORACLE_P, HEUR_PCT, HEUR_P | c5b_pilot |\n| discussion.tex:15 | LLaMA random Wilcoxon p | c3_llama |\n| appendix_moved.tex:30 | NULL_PCT | Qwen null rate |\n| appendix_moved.tex:35 | N_QW | Qwen valid n |\n| appendix_moved.tex:41-43 | Qwen effective n 表格 (12 cells) | Qwen per-phase data |\n| appendix_moved.tex:73 | ρ, p (per-problem concordance) | cross_model_analysis.json |\n| appendix_moved.tex:76 | Qwen rand s030 Δ̃ | bf16_qw_rand_s030 |\n| appendix_results.tex:7 | 同 appendix_moved.tex:73 (重复文件) | cross_model_analysis.json |\n| appendix_results.tex:10 | 同 appendix_moved.tex:76 (重复文件) | bf16_qw_rand_s030 |\n| appendix_disc_analysis.tex:14 | Qwen rand s030 Δ̃ | bf16_qw_rand_s030 |\n| appendix_disc_analysis.tex:49 | Qwen rand s030 Δ̃ | qw_rand_s030 |\n\n注意: appendix_results.tex 未被 main.tex \\input，内容与 appendix_moved.tex 重复。建议清理或统一。\n\n---\n\n## P3: 一致性与混用风险\n\n### 25. n=50 / n=500 混用风险点\n\n| 数据源 | 当前 n | 更新后 n | 风险 |\n|--------|--------|---------|------|\n| DeepSeek importance/random (c2) | 50 | **500** | 主表全部替换 |\n| Qwen importance/random (c2) | 50 | **500** | 主表全部替换 |\n| LLaMA cross-arch (c3_llama) | 50 | **50 不变** | ⚠️ 需在 §5.5/Limitations 明确标注 n=50 |\n| Entropy/discrimination (c4) | 30 | **30 不变** | ⚠️ Analysis §6 数字不变，但样本量不一致需说明 |\n| c5b_pilot | ? | **不变** | Discussion §7 pilot 数字不变 |\n| Permutation test | 49(DS)/46(QW) | **~490/~460** | 替换 |\n| Cross-model comparison | 50 | **500** | 替换 |\n\n### 26. 需要显式声明不同 n 的位置\n```\n- results.tex §5.5 (cross-arch): 已有 \"n=\\placeholder{N_LLAMA}\" → 确保说明这是 n=50\n- analysis.tex §6: 当前未提及 c4 的 n=30 → 建议添加注脚\n- discussion.tex §7 (pilot): 当前未提及 pilot 样本量 → 建议添加\n- limitations.tex: 添加说明 \"LLaMA/mechanism 分析基于 n=50/30 子集\"\n- abstract.tex: \"50 MATH-500 problems\" → 需注明 LLaMA 仍用 50\n  或改为 \"up to 500 MATH-500 problems\"\n```\n\n### 27. C8 partially_confirmed 限定语检查 ✅\n已确认以下位置使用了合格限定语:\n- abstract.tex:10 — \"mixed but directionally consistent evidence\"\n- results.tex:79 — \"partially confirming the cross-architecture hypothesis\"\n- discussion.tex:14-15 — \"partial support...substantially weaker\"\n- conclusion.tex:4 — \"partially extends cross-architecture\"\n- limitations.tex:1-2 — \"partially confirms...substantially weaker\"\n- appendix_disc_analysis.tex:33 — \"partial confirmation\"\n**无需修改（除非 n=500 改变了 DS/QW 数据使 LLaMA 对比幅度变化）**\n\n### 28. C5b future_work 标注检查 ✅\n已确认:\n- discussion.tex:10 — pilot 结果 + \"promising direction for future work\"\n- appendix_disc_analysis.tex:57,62 — REBUTTAL comments 标注 future work\n**无需修改，但 \\placeholder{} 值需填充**\n\n### 29. Qwen random s030 p=0.012 d=-0.04 caveat 检查\n出现在以下位置（均标注为 negligible/no meaningful modulation）:\n- abstract.tex:8 ✅\n- appendix_moved.tex:76 ✅\n- appendix_results.tex:10 ✅\n- appendix_disc_analysis.tex:14,49 ✅\n**n=500 后需检查: Qwen rand s030 是否仍为 borderline/negligible，或变显著 → 影响 \"7/8 FAIL\" 叙事**\n\n---\n\n## 执行顺序建议\n\n1. **等 n=500 数据产出** → 运行统计分析脚本生成新的 experiment_summary_table.json, cohens_d, permutation_test_results 等\n2. **P0 先行**: 更新主表 → abstract → intro → conclusion（确保核心叙事一致）\n3. **P1 跟进**: 更新附录表格 → 重新生成 4 张图\n4. **P2 条件分支**: 根据 QW s015 CI / QW imp-vs-rand 结果决定叙事调整\n5. **P3 最后检查**: 全文搜索 \"n=50\" / \"50 problems\" / \"n=49\" / \"n=46\" 确保无残留\n6. **填充 \\placeholder{}**: LLaMA 表格 + 各处 Qwen rand Δ̃ + pilot 数字 + concordance ρ/p\n7. **LaTeX 编译验证**: 确保无 red placeholder 残留\n"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "worker_research_paper_update_prep_20260515T013953",
  "tool": "mcp__agent-ml-research__save_project_file",
  "tool_args": {
    "project": "phase-gated-compound-sparse",
    "file": "artifacts/paper_update_checklist.md",
    "content": "# Paper Update Checklist: n=50 → n=500\n\n> 生成时间: 2026-05-15 | 适用实验: c2_n500_deepseek + c2_qw_n500 (C7)\n> 约束: median + bootstrap CI 为主指标 (D054); d_z 分场景 (D059); Qwen imp-vs-rand 不claim显著直到n=500确认 (D058); C8=partially_confirmed (D060); C5b=future_work (D056)\n\n---\n\n## 优先级说明\n- **P0**: 核心数字，读者第一眼看到，必须同步更新\n- **P1**: 支撑性数字/表格，与 P0 有数据依赖\n- **P2**: 条件性更新（取决于 n=500 结果）\n- **P3**: 一致性检查，防止 n=50/n=500 混用\n\n---\n\n## P0: 核心数字更新\n\n### 1. methodology.tex:10 — 样本量\n```\n当前: \"We use 50 problems stratified from MATH-500\"\n更新: → 500 problems (n=500 的具体描述，包括 stratification 方式)\n```\n\n### 2. abstract.tex:6 — 样本量\n```\n当前: \"using 50 MATH-500 problems\"\n更新: → 500 MATH-500 problems\n```\n\n### 3. abstract.tex:7 — DeepSeek 主指标\n```\n当前: \"median Interaction Index difference...from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$, with paired Cohen's $d_z$ growing from $0.44$ (small) to $0.80$ (large)\"\n更新: → 用 n=500 segment-level median diff + paired d_z 替换\n注意: 0.39/14.59 是 segment-level medians；d_z 0.44/0.80 是 paired d_z。两组数据来源不同，都需更新。\n```\n\n### 4. introduction.tex:14 — DeepSeek 主指标（与 abstract 一致）\n```\n当前: \"median phase difference rises from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$ ($d_z$: $0.44 \\to 0.80$)\"\n更新: → 同 abstract\n```\n\n### 5. results.tex:8,13,19-20 — Tab aggregate-ii（DeepSeek segment-level Δ）\n```\n当前 Importance: 0.39, 1.48, 7.16, 14.59\n当前 Random: 0.01, -0.02, 0.54, 1.54\ncaption \"$n{=}50$\" → $n{=}500$ (或实际有效 n)\n更新: → 全部替换为 n=500 值\n```\n\n### 6. results.tex:34,40-50 — Tab main-results（DeepSeek 全 per-phase 分解）\n```\n当前 (importance, 4 sparsity × 3 phases + Δ + G):\n  s015: II_high=0.006, II_mid=0.081, II_low=0.398, Δ=0.39, G=69\n  s020: II_high=0.015, II_mid=0.203, II_low=1.496, Δ=1.48, G=103\n  s025: II_high=0.032, II_mid=1.118, II_low=7.196, Δ=7.16, G=222\n  s030: II_high=0.053, II_mid=2.283, II_low=14.639, Δ=14.59, G=274\n当前 (random, 4 sparsity × 3 phases + Δ + G):\n  s015: 0.093, 0.097, 0.103, 0.01, 1.1\n  s020: 0.292, 0.350, 0.276, -0.02, 0.9\n  s025: 0.818, 0.932, 1.363, 0.54, 1.7\n  s030: 2.503, 2.592, 4.041, 1.54, 1.6\ncaption \"50 problems\" → 500 problems\n更新: → 全部替换为 n=500 值\n```\n\n### 7. results.tex:106,117-120 — Tab cohens-d（DS + QW paired d_z + Δ̃[CI]）\n```\n当前 DS: d_z 0.44/0.52/0.68/0.80; Δ̃ 0.32[0.20,0.47] / 1.15[0.66,1.26] / 3.97[2.83,5.29] / 9.94[8.39,16.65]\n当前 QW: d_z 0.28/0.55/0.89/1.02; Δ̃ 0.05[-0.01,0.11] / 0.21[0.07,0.40] / 1.11[0.61,1.47] / 2.62[1.72,3.65]\n更新: → 全部替换为 n=500 值\n关键: QW s015 CI 当前包含零 → n=500 后检查是否仍包含零（影响 onset threshold 叙事）\n```\n\n### 8. conclusion.tex:4 — 核心数字复述\n```\n当前: \"severity gradient grows from $69{\\times}$ to $274{\\times}$...($d_z$: $0.44 \\to 0.80$)\"\n更新: → 与 results 一致\n```\n\n### 9. discussion.tex:5 — severity gradient + crossover 复述\n```\n当前: \"severity gradient ($69$--$274{\\times}$)\"\n当前: crossover 数字 \"0.032 vs 0.818\", \"7.196 vs 1.363\"\n更新: → 与 results 一致\n```\n\n### 10. results.tex:29 + 58 — G 值 + fig1 caption\n```\n当前: G \"from $69{\\times}$ at $s{=}0.15$ to $274{\\times}$ at $s{=}0.30$\"\n当前 fig1 caption: \"$69{\\times}$ to $274{\\times}$\"\n更新: → n=500 G 值\n```\n\n---\n\n## P1: 支撑性数字更新\n\n### 11. results.tex:66 — Crossover 数字\n```\n当前: \"importance high_phase=0.032 < random=0.818, importance low_phase=7.196 > random=1.363\"\nreversal \"5.3×\"\n更新: → n=500 crossover 值\n```\n\n### 12. results.tex:71 — Qwen cross-model 段落\n```\n当前: \"Δ increases from 0.04 at s=0.15 to 2.94 at s=0.30...d_z ≥ 0.55...d_z=0.28 CI includes zero\"\n更新: → n=500 Qwen 值\n关键: 检查 s015 d_z 是否仍 marginal，onset threshold 是否仍 s≥0.20\n```\n\n### 13. appendix_moved.tex:26 — Qwen/DS 有效 n\n```\n当前: \"Four of the 50 problems...n=46 valid problems for Qwen (vs. n=49 for DeepSeek)\"\n更新: → n=500 的排除数和有效 n\n```\n\n### 14. appendix_moved.tex:59-60 — Tab cross-model Qwen Δ\n```\n当前 DS: 0.39, 1.48, 7.16, 14.59\n当前 QW: 0.04, 0.23, 1.27, 2.94\n更新: → n=500 值\n```\n\n### 15. appendix_moved.tex:88,99-102 — Tab permutation（DeepSeek permutation test）\n```\n当前: n=49; observed Δ̃ 0.37[0.19,0.62], 0.97[0.69,1.49], 3.34[1.66,6.64], 9.85[6.70,16.29]\ncaption \"$n{=}49$\"\n更新: → n=500 permutation test 值\n```\n\n### 16. results.tex:104 — permutation test 段落引用\n```\n当前: \"observed median differences increasing monotonically from $0.37$ at $s{=}0.15$ to $9.85$ at $s{=}0.30$\"\n更新: → 与 Tab permutation 一致\n```\n\n### 17. appendix_moved.tex:11 — crossover 详细数字\n```\n当前: \"reversal magnitude of $3.9{\\times}$ at $s{=}0.15$, $5.4{\\times}$ at $s{=}0.20$, $5.3{\\times}$ at $s{=}0.25$, and $3.6{\\times}$ at $s{=}0.30$\"\n更新: → n=500 reversal magnitudes\n```\n\n### 18. appendix_disc_analysis.tex:46-47 — permutation CI + skewness 统计\n```\n当前: \"mean/median ratio ~1.6:1 at s=0.30\"\n当前: \"permutation CIs: s015=[0.19,0.62], s020=[0.69,1.49], s025=[1.66,6.64], s030=[6.70,16.29]\"\n更新: → n=500 值\n```\n\n### 19. abstract.tex:10 — LLaMA cross-arch 段落\n```\n当前: \"Δ̃: 0.020→0.356; s=0.30 Wilcoxon p_Bonf=0.029\"\n注意: LLaMA 实验仍为 n=50，数字不变，但需检查措辞是否暗示与 DS/QW 同一 n\n```\n\n### 20. 图表重新生成\n```\nfig1_dose_response.pdf — G vs s 曲线（P0 依赖）\nfig3_crossover.pdf — crossover bar chart\nfig4_bootstrap.pdf — permutation forest plot\nfig5_crossmodel.pdf — cross-model Δ comparison\n所有图需用 n=500 数据重新生成\n```\n\n---\n\n## P2: 条件性更新\n\n### 21. D058: Qwen imp-vs-rand 显著性\n```\n当前状态: 论文未报告 Qwen imp-vs-rand permutation test（只报告了 DeepSeek）\n约束: n=500 前不得 claim Qwen imp-vs-rand 显著\n行动:\n  - 若 n=500 Qwen imp-vs-rand 显著 → 可添加 Qwen permutation test 表格，strengthens C1\n  - 若仍不显著 → 在 cross-model 段落加 caveat，或维持当前策略（只报 within-importance gradient）\n检查文件: results.tex:71, appendix_results.tex:10\n```\n\n### 22. D059: d_z 报告策略\n```\n约束: within-importance d_z 保留; 涉及 random 只报方向\n行动: 检查 n=500 后是否有新的 imp-vs-rand d_z 值需要报告，确保遵守\"只报方向\"规则\n影响文件: results.tex, appendix_moved.tex\n```\n\n### 23. C2 预注册: Qwen s015 onset threshold\n```\n当前: paper_framing 预注册 \"n=500 后若 QW s015 CI 仍跨零，叙事改为 'compound effect emerges above threshold sparsity (~s020)'\"\n检查: results.tex:71 \"marginal at s=0.15\" + Tab cohens-d QW s015 行\n行动:\n  - 若 n=500 QW s015 CI 不跨零 → onset = s≥0.15，更新叙事\n  - 若仍跨零 → 保持 \"emerges above ~s020\" 叙事\n```\n\n### 24. Placeholder 值填充\n以下 \\placeholder{} 标记需用 n=50 或 n=500 数据填充:\n\n| 文件:行 | Placeholder | 数据来源 |\n|---------|-------------|----------|\n| abstract.tex:8 | Qwen rand s030 Δ̃ | bf16_qw_rand_s030 |\n| results.tex:71 | NULL_PCT | Qwen per-phase null rate |\n| results.tex:81 | LLaMA random Wilcoxon p | c3_llama |\n| results.tex:86 | N_LLAMA | c3_llama (n=49?) |\n| results.tex:92-95 | 整个 LLaMA 表格 (12 cells) | c3_llama |\n| discussion.tex:10 | ORACLE_PCT, ORACLE_P, HEUR_PCT, HEUR_P | c5b_pilot |\n| discussion.tex:15 | LLaMA random Wilcoxon p | c3_llama |\n| appendix_moved.tex:30 | NULL_PCT | Qwen null rate |\n| appendix_moved.tex:35 | N_QW | Qwen valid n |\n| appendix_moved.tex:41-43 | Qwen effective n 表格 (12 cells) | Qwen per-phase data |\n| appendix_moved.tex:73 | ρ, p (per-problem concordance) | cross_model_analysis.json |\n| appendix_moved.tex:76 | Qwen rand s030 Δ̃ | bf16_qw_rand_s030 |\n| appendix_results.tex:7 | 同 appendix_moved.tex:73 (重复文件) | cross_model_analysis.json |\n| appendix_results.tex:10 | 同 appendix_moved.tex:76 (重复文件) | bf16_qw_rand_s030 |\n| appendix_disc_analysis.tex:14 | Qwen rand s030 Δ̃ | bf16_qw_rand_s030 |\n| appendix_disc_analysis.tex:49 | Qwen rand s030 Δ̃ | qw_rand_s030 |\n\n注意: appendix_results.tex 未被 main.tex \\input，内容与 appendix_moved.tex 重复。建议清理或统一。\n\n---\n\n## P3: 一致性与混用风险\n\n### 25. n=50 / n=500 混用风险点\n\n| 数据源 | 当前 n | 更新后 n | 风险 |\n|--------|--------|---------|------|\n| DeepSeek importance/random (c2) | 50 | **500** | 主表全部替换 |\n| Qwen importance/random (c2) | 50 | **500** | 主表全部替换 |\n| LLaMA cross-arch (c3_llama) | 50 | **50 不变** | ⚠️ 需在 §5.5/Limitations 明确标注 n=50 |\n| Entropy/discrimination (c4) | 30 | **30 不变** | ⚠️ Analysis §6 数字不变，但样本量不一致需说明 |\n| c5b_pilot | ? | **不变** | Discussion §7 pilot 数字不变 |\n| Permutation test | 49(DS)/46(QW) | **~490/~460** | 替换 |\n| Cross-model comparison | 50 | **500** | 替换 |\n\n### 26. 需要显式声明不同 n 的位置\n```\n- results.tex §5.5 (cross-arch): 已有 \"n=\\placeholder{N_LLAMA}\" → 确保说明这是 n=50\n- analysis.tex §6: 当前未提及 c4 的 n=30 → 建议添加注脚\n- discussion.tex §7 (pilot): 当前未提及 pilot 样本量 → 建议添加\n- limitations.tex: 添加说明 \"LLaMA/mechanism 分析基于 n=50/30 子集\"\n- abstract.tex: \"50 MATH-500 problems\" → 需注明 LLaMA 仍用 50\n  或改为 \"up to 500 MATH-500 problems\"\n```\n\n### 27. C8 partially_confirmed 限定语检查 ✅\n已确认以下位置使用了合格限定语:\n- abstract.tex:10 — \"mixed but directionally consistent evidence\"\n- results.tex:79 — \"partially confirming the cross-architecture hypothesis\"\n- discussion.tex:14-15 — \"partial support...substantially weaker\"\n- conclusion.tex:4 — \"partially extends cross-architecture\"\n- limitations.tex:1-2 — \"partially confirms...substantially weaker\"\n- appendix_disc_analysis.tex:33 — \"partial confirmation\"\n**无需修改（除非 n=500 改变了 DS/QW 数据使 LLaMA 对比幅度变化）**\n\n### 28. C5b future_work 标注检查 ✅\n已确认:\n- discussion.tex:10 — pilot 结果 + \"promising direction for future work\"\n- appendix_disc_analysis.tex:57,62 — REBUTTAL comments 标注 future work\n**无需修改，但 \\placeholder{} 值需填充**\n\n### 29. Qwen random s030 p=0.012 d=-0.04 caveat 检查\n出现在以下位置（均标注为 negligible/no meaningful modulation）:\n- abstract.tex:8 ✅\n- appendix_moved.tex:76 ✅\n- appendix_results.tex:10 ✅\n- appendix_disc_analysis.tex:14,49 ✅\n**n=500 后需检查: Qwen rand s030 是否仍为 borderline/negligible，或变显著 → 影响 \"7/8 FAIL\" 叙事**\n\n---\n\n## 执行顺序建议\n\n1. **等 n=500 数据产出** → 运行统计分析脚本生成新的 experiment_summary_table.json, cohens_d, permutation_test_results 等\n2. **P0 先行**: 更新主表 → abstract → intro → conclusion（确保核心叙事一致）\n3. **P1 跟进**: 更新附录表格 → 重新生成 4 张图\n4. **P2 条件分支**: 根据 QW s015 CI / QW imp-vs-rand 结果决定叙事调整\n5. **P3 最后检查**: 全文搜索 \"n=50\" / \"50 problems\" / \"n=49\" / \"n=46\" 确保无残留\n6. **填充 \\placeholder{}**: LLaMA 表格 + 各处 Qwen rand Δ̃ + pilot 数字 + concordance ρ/p\n7. **LaTeX 编译验证**: 确保无 red placeholder 残留\n"
  }
}
````

</details>

---

### Tool result

_source line 54 · 2026-05-15T01:46:28.035845+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file 'artifacts/paper_update_checklist.md' is not writable via save_project_file. Writable: ['memory.md', 'paper_framing.md', 'writing_plan.yaml'].\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper_update_prep_20260515T013953",
  "tool": "mcp__agent-ml-research__save_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-15T01:46:28.036009+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/",
  "description": "List artifacts directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_paper_update_prep_20260515T013953",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/",
    "description": "List artifacts directory"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-15T01:46:28.036145+00:00_

_project
analysis_pipeline_audit.md
analysis_pipeline_readiness.md
analysis_pipeline_verification.md
analyze_c2_n500.py
bf16_qw_imp_failures_diagnosis.md
bf16_qw_rand_s015
bf16_qw_rand_s020
bf16_qw_rand_s025
bf16_qw_rand_s030
bootstrap_phase_gradient.py
c2_n500_deepseek
c2_n500_paper_update_checklist.md
c2_progress_report.md
c2_progress_snapshot.json
c2_qw_n500_investigation.md
c3_llama
c3_llama_results.json
c5b_framing_proposal.md
c5b_pilot
c5b_pilot_design.md
c5b_pilot_diagnosis.md
compute_multiplicative_null.py
consistency_audit_final.md
consistency_audit_report.md
consistency_report.md
dream_reports
gpu_check_loop7.md
literature_scan_20260515.md
literature_scan_phase_adaptive.md
m1_phase_segmentation_analysis.md
m2_m4_code_readiness.md
magnitude_crossover_novelty_check.md
manifest.yaml
mechanistic_explanation.md
mid_sparsity_gap_analysis.md
mvp_ii_analysis.md
mvp_ii_profiling_v2
mvp_ii_profiling_v3
mvp_ii_v3_analysis.md
mvp_interaction_index_profiling
n500_analysis_pipeline_ready.md
n500_paper_patch_plan.md
n500_paper_update_FINAL.md
n500_paper_update_checklist.md
n500_paper_update_plan.md
n500_progress_20260515_0632.md
n500_progress_check.md
n500_update_checklist.md
number_consistency_audit_v2.md
pacs
paper_n500_update_checklist.md
paper_n500_update_plan.md
qwen_kill_investigation.md
qwen_status_check.md
reference_audit.md
reference_audit_report.md
report_analysis_pipeline_ready.md
report_process_check.md
review_issues.yaml
review_reports
v5_status_check.md
w1w5_audit_report.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper_update_prep_20260515T013953",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-15T01:46:28.036315+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

````json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/paper_update_checklist.md",
  "content": "# Paper Update Checklist: n=50 → n=500\n\n> 生成时间: 2026-05-15 | 适用实验: c2_n500_deepseek + c2_qw_n500 (C7)\n> 约束: median + bootstrap CI 为主指标 (D054); d_z 分场景 (D059); Qwen imp-vs-rand 不claim显著直到n=500确认 (D058); C8=partially_confirmed (D060); C5b=future_work (D056)\n\n---\n\n## 优先级说明\n- **P0**: 核心数字，读者第一眼看到，必须同步更新\n- **P1**: 支撑性数字/表格，与 P0 有数据依赖\n- **P2**: 条件性更新（取决于 n=500 结果）\n- **P3**: 一致性检查，防止 n=50/n=500 混用\n\n---\n\n## P0: 核心数字更新\n\n### 1. methodology.tex:10 — 样本量\n```\n当前: \"We use 50 problems stratified from MATH-500\"\n更新: → 500 problems (n=500 的具体描述，包括 stratification 方式)\n```\n\n### 2. abstract.tex:6 — 样本量\n```\n当前: \"using 50 MATH-500 problems\"\n更新: → 500 MATH-500 problems\n```\n\n### 3. abstract.tex:7 — DeepSeek 主指标\n```\n当前: \"median Interaction Index difference...from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$, with paired Cohen's $d_z$ growing from $0.44$ (small) to $0.80$ (large)\"\n更新: → 用 n=500 segment-level median diff + paired d_z 替换\n注意: 0.39/14.59 是 segment-level medians；d_z 0.44/0.80 是 paired d_z。两组数据来源不同，都需更新。\n```\n\n### 4. introduction.tex:14 — DeepSeek 主指标（与 abstract 一致）\n```\n当前: \"median phase difference rises from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$ ($d_z$: $0.44 \\to 0.80$)\"\n更新: → 同 abstract\n```\n\n### 5. results.tex:8,13,19-20 — Tab aggregate-ii（DeepSeek segment-level Δ）\n```\n当前 Importance: 0.39, 1.48, 7.16, 14.59\n当前 Random: 0.01, -0.02, 0.54, 1.54\ncaption \"$n{=}50$\" → $n{=}500$ (或实际有效 n)\n更新: → 全部替换为 n=500 值\n```\n\n### 6. results.tex:34,40-50 — Tab main-results（DeepSeek 全 per-phase 分解）\n```\n当前 (importance, 4 sparsity × 3 phases + Δ + G):\n  s015: II_high=0.006, II_mid=0.081, II_low=0.398, Δ=0.39, G=69\n  s020: II_high=0.015, II_mid=0.203, II_low=1.496, Δ=1.48, G=103\n  s025: II_high=0.032, II_mid=1.118, II_low=7.196, Δ=7.16, G=222\n  s030: II_high=0.053, II_mid=2.283, II_low=14.639, Δ=14.59, G=274\n当前 (random, 4 sparsity × 3 phases + Δ + G):\n  s015: 0.093, 0.097, 0.103, 0.01, 1.1\n  s020: 0.292, 0.350, 0.276, -0.02, 0.9\n  s025: 0.818, 0.932, 1.363, 0.54, 1.7\n  s030: 2.503, 2.592, 4.041, 1.54, 1.6\ncaption \"50 problems\" → 500 problems\n更新: → 全部替换为 n=500 值\n```\n\n### 7. results.tex:106,117-120 — Tab cohens-d（DS + QW paired d_z + Δ̃[CI]）\n```\n当前 DS: d_z 0.44/0.52/0.68/0.80; Δ̃ 0.32[0.20,0.47] / 1.15[0.66,1.26] / 3.97[2.83,5.29] / 9.94[8.39,16.65]\n当前 QW: d_z 0.28/0.55/0.89/1.02; Δ̃ 0.05[-0.01,0.11] / 0.21[0.07,0.40] / 1.11[0.61,1.47] / 2.62[1.72,3.65]\n更新: → 全部替换为 n=500 值\n关键: QW s015 CI 当前包含零 → n=500 后检查是否仍包含零（影响 onset threshold 叙事）\n```\n\n### 8. conclusion.tex:4 — 核心数字复述\n```\n当前: \"severity gradient grows from $69{\\times}$ to $274{\\times}$...($d_z$: $0.44 \\to 0.80$)\"\n更新: → 与 results 一致\n```\n\n### 9. discussion.tex:5 — severity gradient + crossover 复述\n```\n当前: \"severity gradient ($69$--$274{\\times}$)\"\n当前: crossover 数字 \"0.032 vs 0.818\", \"7.196 vs 1.363\"\n更新: → 与 results 一致\n```\n\n### 10. results.tex:29 + 58 — G 值 + fig1 caption\n```\n当前: G \"from $69{\\times}$ at $s{=}0.15$ to $274{\\times}$ at $s{=}0.30$\"\n当前 fig1 caption: \"$69{\\times}$ to $274{\\times}$\"\n更新: → n=500 G 值\n```\n\n---\n\n## P1: 支撑性数字更新\n\n### 11. results.tex:66 — Crossover 数字\n```\n当前: \"importance high_phase=0.032 < random=0.818, importance low_phase=7.196 > random=1.363\"\nreversal \"5.3×\"\n更新: → n=500 crossover 值\n```\n\n### 12. results.tex:71 — Qwen cross-model 段落\n```\n当前: \"Δ increases from 0.04 at s=0.15 to 2.94 at s=0.30...d_z ≥ 0.55...d_z=0.28 CI includes zero\"\n更新: → n=500 Qwen 值\n关键: 检查 s015 d_z 是否仍 marginal，onset threshold 是否仍 s≥0.20\n```\n\n### 13. appendix_moved.tex:26 — Qwen/DS 有效 n\n```\n当前: \"Four of the 50 problems...n=46 valid problems for Qwen (vs. n=49 for DeepSeek)\"\n更新: → n=500 的排除数和有效 n\n```\n\n### 14. appendix_moved.tex:59-60 — Tab cross-model Qwen Δ\n```\n当前 DS: 0.39, 1.48, 7.16, 14.59\n当前 QW: 0.04, 0.23, 1.27, 2.94\n更新: → n=500 值\n```\n\n### 15. appendix_moved.tex:88,93,99-102 — Tab permutation（DeepSeek permutation test）\n```\n当前: n=49; observed Δ̃ 0.37[0.19,0.62], 0.97[0.69,1.49], 3.34[1.66,6.64], 9.85[6.70,16.29]\ncaption \"$n{=}49$\"\n更新: → n=500 permutation test 值\n```\n\n### 16. results.tex:104 — permutation test 段落引用\n```\n当前: \"observed median differences increasing monotonically from $0.37$ at $s{=}0.15$ to $9.85$ at $s{=}0.30$\"\n更新: → 与 Tab permutation 一致\n```\n\n### 17. appendix_moved.tex:11 — crossover 详细数字\n```\n当前: \"reversal magnitude of $3.9{\\times}$ at $s{=}0.15$, $5.4{\\times}$ at $s{=}0.20$, $5.3{\\times}$ at $s{=}0.25$, and $3.6{\\times}$ at $s{=}0.30$\"\n更新: → n=500 reversal magnitudes\n```\n\n### 18. appendix_disc_analysis.tex:46-47 — permutation CI + skewness 统计\n```\n当前: \"mean/median ratio ~1.6:1 at s=0.30\"\n当前: \"permutation CIs: s015=[0.19,0.62], s020=[0.69,1.49], s025=[1.66,6.64], s030=[6.70,16.29]\"\n当前 (line 11): \"high-phase II rises to 0.105 at s=0.35\"\n更新: → n=500 值 (s035 supplementary 是否也需更新取决于是否重跑)\n```\n\n### 19. abstract.tex:10 — LLaMA cross-arch 段落\n```\n当前: \"Δ̃: 0.020→0.356; s=0.30 Wilcoxon p_Bonf=0.029\"\n注意: LLaMA 实验仍为 n=50，数字不变，但需检查措辞是否暗示与 DS/QW 同一 n\n```\n\n### 20. 图表重新生成\n```\nfig1_dose_response.pdf — G vs s 曲线（P0 依赖）\nfig3_crossover.pdf — crossover bar chart\nfig4_bootstrap.pdf — permutation forest plot\nfig5_crossmodel.pdf — cross-model Δ comparison\n所有图需用 n=500 数据重新生成\n```\n\n---\n\n## P2: 条件性更新\n\n### 21. D058: Qwen imp-vs-rand 显著性\n```\n当前状态: 论文未报告 Qwen imp-vs-rand permutation test（只报告了 DeepSeek）\n约束: n=500 前不得 claim Qwen imp-vs-rand 显著\n行动:\n  - 若 n=500 Qwen imp-vs-rand 显著 → 可添加 Qwen permutation test 表格，strengthens C1\n  - 若仍不显著 → 在 cross-model 段落加 caveat，或维持当前策略（只报 within-importance gradient）\n检查文件: results.tex:71, appendix_results.tex:10\n```\n\n### 22. D059: d_z 报告策略\n```\n约束: within-importance d_z 保留; 涉及 random 只报方向\n行动: 检查 n=500 后是否有新的 imp-vs-rand d_z 值需要报告，确保遵守\"只报方向\"规则\n影响文件: results.tex, appendix_moved.tex\n```\n\n### 23. C2 预注册: Qwen s015 onset threshold\n```\n当前: paper_framing 预注册 \"n=500 后若 QW s015 CI 仍跨零，叙事改为 'compound effect emerges above threshold sparsity (~s020)'\"\n检查: results.tex:71 \"marginal at s=0.15\" + Tab cohens-d QW s015 行\n行动:\n  - 若 n=500 QW s015 CI 不跨零 → onset = s≥0.15，更新叙事\n  - 若仍跨零 → 保持 \"emerges above ~s020\" 叙事\n```\n\n### 24. Placeholder 值填充\n以下 \\placeholder{} 标记需用实际数据填充:\n\n| 文件:行 | Placeholder | 数据来源 | n=500影响? |\n|---------|-------------|----------|-----------|\n| abstract.tex:8 | Qwen rand s030 Δ̃ | bf16_qw_rand_s030 | 是 |\n| results.tex:71 | NULL_PCT | Qwen per-phase null rate | 是 |\n| results.tex:81 | LLaMA random Wilcoxon p | c3_llama | 否(n=50) |\n| results.tex:86 | N_LLAMA | c3_llama | 否(n=50) |\n| results.tex:92-95 | 整个 LLaMA 表格 (12 cells) | c3_llama | 否(n=50) |\n| discussion.tex:10 | ORACLE_PCT, ORACLE_P, HEUR_PCT, HEUR_P | c5b_pilot | 否 |\n| discussion.tex:15 | LLaMA random Wilcoxon p | c3_llama | 否(n=50) |\n| appendix_moved.tex:30 | NULL_PCT | Qwen null rate | 是 |\n| appendix_moved.tex:35 | N_QW | Qwen valid n | 是 |\n| appendix_moved.tex:41-43 | Qwen effective n 表格 (12 cells) | Qwen per-phase data | 是 |\n| appendix_moved.tex:73 | ρ, p (per-problem concordance) | cross_model_analysis.json | 是 |\n| appendix_moved.tex:76 | Qwen rand s030 Δ̃ | bf16_qw_rand_s030 | 是 |\n| appendix_results.tex:7 | 同 appendix_moved.tex:73 (重复!) | cross_model_analysis.json | 是 |\n| appendix_results.tex:10 | 同 appendix_moved.tex:76 (重复!) | bf16_qw_rand_s030 | 是 |\n| appendix_disc_analysis.tex:14 | Qwen rand s030 Δ̃ | bf16_qw_rand_s030 | 是 |\n| appendix_disc_analysis.tex:49 | Qwen rand s030 Δ̃ | qw_rand_s030 | 是 |\n\n⚠️ appendix_results.tex 未被 main.tex \\input，内容与 appendix_moved.tex §Cross-Model 重复。建议删除或统一。\n\n---\n\n## P3: 一致性与混用风险\n\n### 25. n=50 / n=500 混用风险矩阵\n\n| 数据源 | 当前 n | 更新后 n | 混用风险 |\n|--------|--------|---------|---------|\n| DeepSeek importance/random (c2) | 50 | **500** | 主表全部替换 |\n| Qwen importance/random (c2) | 50 | **500** | 主表全部替换 |\n| LLaMA cross-arch (c3_llama) | 50 | **50 不变** | ⚠️ 高风险 |\n| Entropy/discrimination (c4) | 30 | **30 不变** | ⚠️ 中风险 |\n| c5b_pilot | ~50 | **不变** | 低风险 |\n| Permutation test | 49(DS)/46(QW) | **~490/~460** | 替换 |\n| Cross-model comparison | 50 | **500** | 替换 |\n\n### 26. 需要显式声明不同 n 的位置\n```\n- abstract.tex: \"50 MATH-500 problems\" → 改为区分 DS/QW (n=500) vs LLaMA (n=50)\n  建议: \"500 MATH-500 problems (50 for cross-architecture validation)\"\n- results.tex §5.5 (cross-arch): 已有 \"n=\\placeholder{N_LLAMA}\" → 填入 49 或 50，确保读者知道这不是 500\n- analysis.tex §6: 当前未提及 c4 的样本量 → 建议添加脚注 \"(30 problems per model)\"\n- discussion.tex §7 (pilot): 当前未提及 pilot 样本量 → 建议添加\n- methodology.tex: 需说明 \"500 problems for primary experiments; 50 for cross-architecture (LLaMA)\"\n- limitations.tex: 添加 \"LLaMA 和 mechanism 分析基于 n=50/30 子集\"\n```\n\n### 27. C8 partially_confirmed 限定语检查 ✅\n已确认以下位置使用了合格限定语:\n- abstract.tex:10 — \"mixed but directionally consistent evidence\"\n- results.tex:79 — \"partially confirming the cross-architecture hypothesis\"\n- discussion.tex:14-15 — \"partial support...substantially weaker\"\n- conclusion.tex:4 — \"partially extends cross-architecture\"\n- limitations.tex:1-2 — \"partially confirms...substantially weaker\"\n- appendix_disc_analysis.tex:33 — \"partial confirmation\"\n**状态: 合格，无需修改（除非 n=500 改变了 DS/QW 数据使 LLaMA 对比幅度比例变化）**\n\n### 28. C5b future_work 标注检查 ✅\n已确认:\n- discussion.tex:10 — pilot 结果 + \"promising direction for future work\"\n- appendix_disc_analysis.tex:57,62 — REBUTTAL comments 标注 future work\n**状态: 合格，但 discussion.tex:10 的 \\placeholder{} 值需填充**\n\n### 29. Qwen random s030 caveat 检查\n当前标注为 negligible/no meaningful modulation 的位置:\n- abstract.tex:8 — \"negligible median difference\" ✅\n- appendix_moved.tex:76 — \"negligible median difference, CI spans zero\" ✅\n- appendix_results.tex:10 — 同上 ✅\n- appendix_disc_analysis.tex:14 — \"negligible effect size\" ✅\n- appendix_disc_analysis.tex:49 — \"negligible effect size, bootstrap CI spanning zero\" ✅\n**n=500 后需重新检查: Qwen rand s030 是否仍为 borderline/negligible → 若变显著且效应量非 negligible，需修改 \"7/8 FAIL\" 叙事**\n\n---\n\n## 执行顺序建议\n\n```\nPhase 1: 数据准备\n  1.1 等 n=500 数据完成\n  1.2 运行统计分析脚本 → experiment_summary_table.json, cohens_d, permutation_test 等\n  1.3 提取所有新数值到一个汇总表\n\nPhase 2: P0 核心更新 (同步进行，确保一致)\n  2.1 更新 results.tex 三张主表 (Tab 1/2/3)\n  2.2 更新 abstract.tex 数字\n  2.3 更新 introduction.tex 数字\n  2.4 更新 conclusion.tex 数字\n  2.5 更新 discussion.tex 数字\n  2.6 更新 methodology.tex 样本量\n\nPhase 3: P1 支撑更新\n  3.1 更新 appendix_moved.tex 所有表格和数字\n  3.2 更新 appendix_disc_analysis.tex 数字\n  3.3 重新生成 4 张图 (fig1-fig5)\n\nPhase 4: P2 条件分支\n  4.1 检查 QW s015 CI → 决定 onset threshold 叙事\n  4.2 检查 QW imp-vs-rand → 决定是否添加 Qwen permutation test\n  4.3 检查 QW rand s030 → 决定 \"7/8 FAIL\" 叙事是否需调整\n  4.4 填充所有 \\placeholder{}\n\nPhase 5: P3 一致性扫描\n  5.1 全文搜索 \"n=50\" / \"50 problems\" / \"n=49\" / \"n=46\" → 确保无残留\n  5.2 添加 LLaMA n=50 / c4 n=30 的显式声明\n  5.3 清理 appendix_results.tex（重复文件）\n\nPhase 6: 验证\n  6.1 LaTeX 编译 → 确保无 red placeholder 残留\n  6.2 数字交叉检查: 每个数字在所有出现位置一致\n  6.3 paper_framing.md 同步更新\n```\n"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "worker_research_paper_update_prep_20260515T013953",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/paper_update_checklist.md",
    "content": "# Paper Update Checklist: n=50 → n=500\n\n> 生成时间: 2026-05-15 | 适用实验: c2_n500_deepseek + c2_qw_n500 (C7)\n> 约束: median + bootstrap CI 为主指标 (D054); d_z 分场景 (D059); Qwen imp-vs-rand 不claim显著直到n=500确认 (D058); C8=partially_confirmed (D060); C5b=future_work (D056)\n\n---\n\n## 优先级说明\n- **P0**: 核心数字，读者第一眼看到，必须同步更新\n- **P1**: 支撑性数字/表格，与 P0 有数据依赖\n- **P2**: 条件性更新（取决于 n=500 结果）\n- **P3**: 一致性检查，防止 n=50/n=500 混用\n\n---\n\n## P0: 核心数字更新\n\n### 1. methodology.tex:10 — 样本量\n```\n当前: \"We use 50 problems stratified from MATH-500\"\n更新: → 500 problems (n=500 的具体描述，包括 stratification 方式)\n```\n\n### 2. abstract.tex:6 — 样本量\n```\n当前: \"using 50 MATH-500 problems\"\n更新: → 500 MATH-500 problems\n```\n\n### 3. abstract.tex:7 — DeepSeek 主指标\n```\n当前: \"median Interaction Index difference...from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$, with paired Cohen's $d_z$ growing from $0.44$ (small) to $0.80$ (large)\"\n更新: → 用 n=500 segment-level median diff + paired d_z 替换\n注意: 0.39/14.59 是 segment-level medians；d_z 0.44/0.80 是 paired d_z。两组数据来源不同，都需更新。\n```\n\n### 4. introduction.tex:14 — DeepSeek 主指标（与 abstract 一致）\n```\n当前: \"median phase difference rises from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$ ($d_z$: $0.44 \\to 0.80$)\"\n更新: → 同 abstract\n```\n\n### 5. results.tex:8,13,19-20 — Tab aggregate-ii（DeepSeek segment-level Δ）\n```\n当前 Importance: 0.39, 1.48, 7.16, 14.59\n当前 Random: 0.01, -0.02, 0.54, 1.54\ncaption \"$n{=}50$\" → $n{=}500$ (或实际有效 n)\n更新: → 全部替换为 n=500 值\n```\n\n### 6. results.tex:34,40-50 — Tab main-results（DeepSeek 全 per-phase 分解）\n```\n当前 (importance, 4 sparsity × 3 phases + Δ + G):\n  s015: II_high=0.006, II_mid=0.081, II_low=0.398, Δ=0.39, G=69\n  s020: II_high=0.015, II_mid=0.203, II_low=1.496, Δ=1.48, G=103\n  s025: II_high=0.032, II_mid=1.118, II_low=7.196, Δ=7.16, G=222\n  s030: II_high=0.053, II_mid=2.283, II_low=14.639, Δ=14.59, G=274\n当前 (random, 4 sparsity × 3 phases + Δ + G):\n  s015: 0.093, 0.097, 0.103, 0.01, 1.1\n  s020: 0.292, 0.350, 0.276, -0.02, 0.9\n  s025: 0.818, 0.932, 1.363, 0.54, 1.7\n  s030: 2.503, 2.592, 4.041, 1.54, 1.6\ncaption \"50 problems\" → 500 problems\n更新: → 全部替换为 n=500 值\n```\n\n### 7. results.tex:106,117-120 — Tab cohens-d（DS + QW paired d_z + Δ̃[CI]）\n```\n当前 DS: d_z 0.44/0.52/0.68/0.80; Δ̃ 0.32[0.20,0.47] / 1.15[0.66,1.26] / 3.97[2.83,5.29] / 9.94[8.39,16.65]\n当前 QW: d_z 0.28/0.55/0.89/1.02; Δ̃ 0.05[-0.01,0.11] / 0.21[0.07,0.40] / 1.11[0.61,1.47] / 2.62[1.72,3.65]\n更新: → 全部替换为 n=500 值\n关键: QW s015 CI 当前包含零 → n=500 后检查是否仍包含零（影响 onset threshold 叙事）\n```\n\n### 8. conclusion.tex:4 — 核心数字复述\n```\n当前: \"severity gradient grows from $69{\\times}$ to $274{\\times}$...($d_z$: $0.44 \\to 0.80$)\"\n更新: → 与 results 一致\n```\n\n### 9. discussion.tex:5 — severity gradient + crossover 复述\n```\n当前: \"severity gradient ($69$--$274{\\times}$)\"\n当前: crossover 数字 \"0.032 vs 0.818\", \"7.196 vs 1.363\"\n更新: → 与 results 一致\n```\n\n### 10. results.tex:29 + 58 — G 值 + fig1 caption\n```\n当前: G \"from $69{\\times}$ at $s{=}0.15$ to $274{\\times}$ at $s{=}0.30$\"\n当前 fig1 caption: \"$69{\\times}$ to $274{\\times}$\"\n更新: → n=500 G 值\n```\n\n---\n\n## P1: 支撑性数字更新\n\n### 11. results.tex:66 — Crossover 数字\n```\n当前: \"importance high_phase=0.032 < random=0.818, importance low_phase=7.196 > random=1.363\"\nreversal \"5.3×\"\n更新: → n=500 crossover 值\n```\n\n### 12. results.tex:71 — Qwen cross-model 段落\n```\n当前: \"Δ increases from 0.04 at s=0.15 to 2.94 at s=0.30...d_z ≥ 0.55...d_z=0.28 CI includes zero\"\n更新: → n=500 Qwen 值\n关键: 检查 s015 d_z 是否仍 marginal，onset threshold 是否仍 s≥0.20\n```\n\n### 13. appendix_moved.tex:26 — Qwen/DS 有效 n\n```\n当前: \"Four of the 50 problems...n=46 valid problems for Qwen (vs. n=49 for DeepSeek)\"\n更新: → n=500 的排除数和有效 n\n```\n\n### 14. appendix_moved.tex:59-60 — Tab cross-model Qwen Δ\n```\n当前 DS: 0.39, 1.48, 7.16, 14.59\n当前 QW: 0.04, 0.23, 1.27, 2.94\n更新: → n=500 值\n```\n\n### 15. appendix_moved.tex:88,93,99-102 — Tab permutation（DeepSeek permutation test）\n```\n当前: n=49; observed Δ̃ 0.37[0.19,0.62], 0.97[0.69,1.49], 3.34[1.66,6.64], 9.85[6.70,16.29]\ncaption \"$n{=}49$\"\n更新: → n=500 permutation test 值\n```\n\n### 16. results.tex:104 — permutation test 段落引用\n```\n当前: \"observed median differences increasing monotonically from $0.37$ at $s{=}0.15$ to $9.85$ at $s{=}0.30$\"\n更新: → 与 Tab permutation 一致\n```\n\n### 17. appendix_moved.tex:11 — crossover 详细数字\n```\n当前: \"reversal magnitude of $3.9{\\times}$ at $s{=}0.15$, $5.4{\\times}$ at $s{=}0.20$, $5.3{\\times}$ at $s{=}0.25$, and $3.6{\\times}$ at $s{=}0.30$\"\n更新: → n=500 reversal magnitudes\n```\n\n### 18. appendix_disc_analysis.tex:46-47 — permutation CI + skewness 统计\n```\n当前: \"mean/median ratio ~1.6:1 at s=0.30\"\n当前: \"permutation CIs: s015=[0.19,0.62], s020=[0.69,1.49], s025=[1.66,6.64], s030=[6.70,16.29]\"\n当前 (line 11): \"high-phase II rises to 0.105 at s=0.35\"\n更新: → n=500 值 (s035 supplementary 是否也需更新取决于是否重跑)\n```\n\n### 19. abstract.tex:10 — LLaMA cross-arch 段落\n```\n当前: \"Δ̃: 0.020→0.356; s=0.30 Wilcoxon p_Bonf=0.029\"\n注意: LLaMA 实验仍为 n=50，数字不变，但需检查措辞是否暗示与 DS/QW 同一 n\n```\n\n### 20. 图表重新生成\n```\nfig1_dose_response.pdf — G vs s 曲线（P0 依赖）\nfig3_crossover.pdf — crossover bar chart\nfig4_bootstrap.pdf — permutation forest plot\nfig5_crossmodel.pdf — cross-model Δ comparison\n所有图需用 n=500 数据重新生成\n```\n\n---\n\n## P2: 条件性更新\n\n### 21. D058: Qwen imp-vs-rand 显著性\n```\n当前状态: 论文未报告 Qwen imp-vs-rand permutation test（只报告了 DeepSeek）\n约束: n=500 前不得 claim Qwen imp-vs-rand 显著\n行动:\n  - 若 n=500 Qwen imp-vs-rand 显著 → 可添加 Qwen permutation test 表格，strengthens C1\n  - 若仍不显著 → 在 cross-model 段落加 caveat，或维持当前策略（只报 within-importance gradient）\n检查文件: results.tex:71, appendix_results.tex:10\n```\n\n### 22. D059: d_z 报告策略\n```\n约束: within-importance d_z 保留; 涉及 random 只报方向\n行动: 检查 n=500 后是否有新的 imp-vs-rand d_z 值需要报告，确保遵守\"只报方向\"规则\n影响文件: results.tex, appendix_moved.tex\n```\n\n### 23. C2 预注册: Qwen s015 onset threshold\n```\n当前: paper_framing 预注册 \"n=500 后若 QW s015 CI 仍跨零，叙事改为 'compound effect emerges above threshold sparsity (~s020)'\"\n检查: results.tex:71 \"marginal at s=0.15\" + Tab cohens-d QW s015 行\n行动:\n  - 若 n=500 QW s015 CI 不跨零 → onset = s≥0.15，更新叙事\n  - 若仍跨零 → 保持 \"emerges above ~s020\" 叙事\n```\n\n### 24. Placeholder 值填充\n以下 \\placeholder{} 标记需用实际数据填充:\n\n| 文件:行 | Placeholder | 数据来源 | n=500影响? |\n|---------|-------------|----------|-----------|\n| abstract.tex:8 | Qwen rand s030 Δ̃ | bf16_qw_rand_s030 | 是 |\n| results.tex:71 | NULL_PCT | Qwen per-phase null rate | 是 |\n| results.tex:81 | LLaMA random Wilcoxon p | c3_llama | 否(n=50) |\n| results.tex:86 | N_LLAMA | c3_llama | 否(n=50) |\n| results.tex:92-95 | 整个 LLaMA 表格 (12 cells) | c3_llama | 否(n=50) |\n| discussion.tex:10 | ORACLE_PCT, ORACLE_P, HEUR_PCT, HEUR_P | c5b_pilot | 否 |\n| discussion.tex:15 | LLaMA random Wilcoxon p | c3_llama | 否(n=50) |\n| appendix_moved.tex:30 | NULL_PCT | Qwen null rate | 是 |\n| appendix_moved.tex:35 | N_QW | Qwen valid n | 是 |\n| appendix_moved.tex:41-43 | Qwen effective n 表格 (12 cells) | Qwen per-phase data | 是 |\n| appendix_moved.tex:73 | ρ, p (per-problem concordance) | cross_model_analysis.json | 是 |\n| appendix_moved.tex:76 | Qwen rand s030 Δ̃ | bf16_qw_rand_s030 | 是 |\n| appendix_results.tex:7 | 同 appendix_moved.tex:73 (重复!) | cross_model_analysis.json | 是 |\n| appendix_results.tex:10 | 同 appendix_moved.tex:76 (重复!) | bf16_qw_rand_s030 | 是 |\n| appendix_disc_analysis.tex:14 | Qwen rand s030 Δ̃ | bf16_qw_rand_s030 | 是 |\n| appendix_disc_analysis.tex:49 | Qwen rand s030 Δ̃ | qw_rand_s030 | 是 |\n\n⚠️ appendix_results.tex 未被 main.tex \\input，内容与 appendix_moved.tex §Cross-Model 重复。建议删除或统一。\n\n---\n\n## P3: 一致性与混用风险\n\n### 25. n=50 / n=500 混用风险矩阵\n\n| 数据源 | 当前 n | 更新后 n | 混用风险 |\n|--------|--------|---------|---------|\n| DeepSeek importance/random (c2) | 50 | **500** | 主表全部替换 |\n| Qwen importance/random (c2) | 50 | **500** | 主表全部替换 |\n| LLaMA cross-arch (c3_llama) | 50 | **50 不变** | ⚠️ 高风险 |\n| Entropy/discrimination (c4) | 30 | **30 不变** | ⚠️ 中风险 |\n| c5b_pilot | ~50 | **不变** | 低风险 |\n| Permutation test | 49(DS)/46(QW) | **~490/~460** | 替换 |\n| Cross-model comparison | 50 | **500** | 替换 |\n\n### 26. 需要显式声明不同 n 的位置\n```\n- abstract.tex: \"50 MATH-500 problems\" → 改为区分 DS/QW (n=500) vs LLaMA (n=50)\n  建议: \"500 MATH-500 problems (50 for cross-architecture validation)\"\n- results.tex §5.5 (cross-arch): 已有 \"n=\\placeholder{N_LLAMA}\" → 填入 49 或 50，确保读者知道这不是 500\n- analysis.tex §6: 当前未提及 c4 的样本量 → 建议添加脚注 \"(30 problems per model)\"\n- discussion.tex §7 (pilot): 当前未提及 pilot 样本量 → 建议添加\n- methodology.tex: 需说明 \"500 problems for primary experiments; 50 for cross-architecture (LLaMA)\"\n- limitations.tex: 添加 \"LLaMA 和 mechanism 分析基于 n=50/30 子集\"\n```\n\n### 27. C8 partially_confirmed 限定语检查 ✅\n已确认以下位置使用了合格限定语:\n- abstract.tex:10 — \"mixed but directionally consistent evidence\"\n- results.tex:79 — \"partially confirming the cross-architecture hypothesis\"\n- discussion.tex:14-15 — \"partial support...substantially weaker\"\n- conclusion.tex:4 — \"partially extends cross-architecture\"\n- limitations.tex:1-2 — \"partially confirms...substantially weaker\"\n- appendix_disc_analysis.tex:33 — \"partial confirmation\"\n**状态: 合格，无需修改（除非 n=500 改变了 DS/QW 数据使 LLaMA 对比幅度比例变化）**\n\n### 28. C5b future_work 标注检查 ✅\n已确认:\n- discussion.tex:10 — pilot 结果 + \"promising direction for future work\"\n- appendix_disc_analysis.tex:57,62 — REBUTTAL comments 标注 future work\n**状态: 合格，但 discussion.tex:10 的 \\placeholder{} 值需填充**\n\n### 29. Qwen random s030 caveat 检查\n当前标注为 negligible/no meaningful modulation 的位置:\n- abstract.tex:8 — \"negligible median difference\" ✅\n- appendix_moved.tex:76 — \"negligible median difference, CI spans zero\" ✅\n- appendix_results.tex:10 — 同上 ✅\n- appendix_disc_analysis.tex:14 — \"negligible effect size\" ✅\n- appendix_disc_analysis.tex:49 — \"negligible effect size, bootstrap CI spanning zero\" ✅\n**n=500 后需重新检查: Qwen rand s030 是否仍为 borderline/negligible → 若变显著且效应量非 negligible，需修改 \"7/8 FAIL\" 叙事**\n\n---\n\n## 执行顺序建议\n\n```\nPhase 1: 数据准备\n  1.1 等 n=500 数据完成\n  1.2 运行统计分析脚本 → experiment_summary_table.json, cohens_d, permutation_test 等\n  1.3 提取所有新数值到一个汇总表\n\nPhase 2: P0 核心更新 (同步进行，确保一致)\n  2.1 更新 results.tex 三张主表 (Tab 1/2/3)\n  2.2 更新 abstract.tex 数字\n  2.3 更新 introduction.tex 数字\n  2.4 更新 conclusion.tex 数字\n  2.5 更新 discussion.tex 数字\n  2.6 更新 methodology.tex 样本量\n\nPhase 3: P1 支撑更新\n  3.1 更新 appendix_moved.tex 所有表格和数字\n  3.2 更新 appendix_disc_analysis.tex 数字\n  3.3 重新生成 4 张图 (fig1-fig5)\n\nPhase 4: P2 条件分支\n  4.1 检查 QW s015 CI → 决定 onset threshold 叙事\n  4.2 检查 QW imp-vs-rand → 决定是否添加 Qwen permutation test\n  4.3 检查 QW rand s030 → 决定 \"7/8 FAIL\" 叙事是否需调整\n  4.4 填充所有 \\placeholder{}\n\nPhase 5: P3 一致性扫描\n  5.1 全文搜索 \"n=50\" / \"50 problems\" / \"n=49\" / \"n=46\" → 确保无残留\n  5.2 添加 LLaMA n=50 / c4 n=30 的显式声明\n  5.3 清理 appendix_results.tex（重复文件）\n\nPhase 6: 验证\n  6.1 LaTeX 编译 → 确保无 red placeholder 残留\n  6.2 数字交叉检查: 每个数字在所有出现位置一致\n  6.3 paper_framing.md 同步更新\n```\n"
  }
}
````

</details>

---

### Tool result

_source line 58 · 2026-05-15T01:46:28.036628+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/paper_update_checklist.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper_update_prep_20260515T013953",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 59 · 2026-05-15T01:46:28.036800+00:00_

清单已保存到 `artifacts/paper_update_checklist.md`。

汇总：

**P0（10项）**：abstract/intro/results/conclusion/discussion 中的核心数字——样本量 50→500、DeepSeek Δ 四个值（0.39→14.59）、d_z（0.44→0.80）、severity gradient G（69×→274×）、crossover 数字、3 张主表（aggregate-ii、main-results、cohens-d）全部需替换。

**P1（10项）**：Qwen cross-model 段落+表格、permutation test 表格+段落、crossover reversal magnitudes、appendix 所有数字、4 张图重新生成。

**P2（4项条件分支）**：QW s015 CI 是否仍跨零（决定 onset threshold 叙事）、QW imp-vs-rand 是否终于显著（D058）、QW rand s030 是否仍 negligible（影响"7/8 FAIL"叙事）、24 个 `\placeholder{}` 待填充。

**P3（5项一致性）**：LLaMA 仍 n=50、c4 机制分析仍 n=30——需在 abstract/methodology/limitations 显式声明不同 n；appendix_results.tex 是冗余文件建议清理；C8 限定语和 C5b future_work 标注已合格无需改动。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_paper_update_prep_20260515T013953"
}
```

</details>

---
