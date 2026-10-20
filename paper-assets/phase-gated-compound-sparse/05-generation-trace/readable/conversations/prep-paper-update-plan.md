# prep paper update plan

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 53
- **Recorded user turns:** 0
- **Tool calls:** 26
- **Original source:** `logs/chats/worker_prep_paper_update_plan_20260514T220436.jsonl`
- **Structured JSON:** [`f9ce24be69aa274be5ff.json`](../../sessions/f9/f9ce24be69aa274be5ff.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

53 recorded events

### Tool call

_source line 1 · 2026-05-14T22:08:29.837060+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__register_artifact",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_prep_paper_update_plan_20260514T220436",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__register_artifact",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-14T22:08:29.837541+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_prep_paper_update_plan_20260514T220436",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-14T22:08:29.837747+00:00_

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
  "session": "worker_prep_paper_update_plan_20260514T220436",
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

_source line 4 · 2026-05-14T22:08:29.837987+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/paper_framing.md\", \"content\": \"# Paper Framing — Phase-Gated Compound Sparsity\\n\\n> 最后更新: 2026-05-14 (D060 C8 partially_confirmed; D056 C5b future_work; D059 d_z 分场景) | 维护者: Director\\n\\n## Core Insight\\n\\nCompound sparsity（attention head pruning + KV cache eviction）的 severity 不是固定常数——它是 eviction strategy 和 reasoning phase 交互的涌现属性。Importance-based eviction 的 compound interaction severity（paired median difference: median(II_low_i − II_high_i)）随 sparsity 单调递增（DeepSeek: 0.32→1.15→3.97→9.94; Qwen: 0.048→0.208→1.109→2.619），而 random masking 三相 II 持平（7/8 FAIL; Qwen s030 PASS p=0.012 but d=-0.04 negligible）。Cohen's d（paired d_z, B=10000）从 small-medium 到 large（DeepSeek: 0.44→0.80; Qwen: 0.28→1.02，s015 边缘）。LLaMA 跨架构验证（D060）qualitative direction consistent（within-importance d_z~1.0），但 strategy×phase 交互弱于 Qwen2 架构（imp_vs_rand d_z 0.19→0.34, 仅 s030 显著），且 random 在 LLaMA 上也显示显著 phase gradient（d_z 0.35→0.44），与 DeepSeek/Qwen random 7/8 FAIL 模式定性不同。这一发现挑战了 compound degradation 均匀分布的隐含假设。\\n\\n**数字基准**：所有数字基于 bf16 per-problem paired 统计量（B=10000 bootstrap）。median_diff 定义为 median(II_low_i − II_high_i)（逐 problem 配对差的中位数）。fp16 旧数据已弃用。\\n\\n## Narrative Arc\\n\\nCompound sparsity 是高效 LLM 推理的实用部署需求，但 prior work（SparK, Ada-KV, SLiM）将 compound interaction 视为均匀超可加。我们发现 severity 是 strategy × phase 交互的涌现属性：importance eviction 的 compound interaction 在 low-sparsity phase 远大于 high-sparsity phase（paired median difference 单调递增 0.32→9.94），而 random eviction 在所有 phase 保持平坦（7/8 FAIL; 唯一例外 Qwen s030 p=0.012 效应量可忽略 d=-0.04）。Cross-model replication 方向一致（Qwen magnitude ~1/4 of DeepSeek，onset threshold s≥0.20）。LLaMA 跨架构验证已完成（c3_llama, D060）：qualitative direction consistent（importance phase gradient d_z≈1.0），但 imp_vs_rand 交互弱（d_z 0.19→0.34, 仅 s030 显著），且 random 也显示非平凡 phase gradient（d_z 0.35→0.44），strategy-dependence 强度 architecture-dependent。我们通过 discrimination co
…[truncated 9581 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_prep_paper_update_plan_20260514T220436",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-14T22:08:29.838235+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "phase-gated-compound-sparse",
  "file": "ROADMAP.md",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_prep_paper_update_plan_20260514T220436",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "phase-gated-compound-sparse",
    "file": "ROADMAP.md",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-14T22:08:29.838506+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/ROADMAP.md\", \"content\": \"# phase-gated-compound-sparse — Research Dashboard\\n\\n> 最后更新: 2026-05-14 18:53 UTC | 更新原因: D060 C8 partially_confirmed（LLaMA random 也显示 phase gradient，交互弱于 Qwen2 架构）\\n\\n> 核心文档链: paper_framing.md → experiment_plan.yaml → 本 ROADMAP\\n\\n## 核心方向\\n**Phase-modulated compound sparsity severity**：importance-based eviction 的 compound interaction severity 随 sparsity 单调递增（DeepSeek: 0.32→1.15→3.97→9.94; Qwen: 0.048→0.208→1.109→2.619），random masking 全 FAIL。Cross-model replication 方向一致（Cohen's d ρ=1.0, gradient permutation p=0.043）。LLaMA 跨架构验证 qualitative consistent（D060: importance phase gradient d_z~1.0, 但 imp vs rand 交互弱，random 也显示 phase gradient）。详见 paper_framing.md。\\n\\n## 目标会议\\nEMNLP 2026 ARR — **截稿 2026-05-25（距今 11 天）**\\n\\n## 当前进展\\n- 阶段：**论文完成 + n=500 补充实验冲刺**（审稿由 Group C 并行）\\n- 82 实验（36 success / 9 negative / 14 failed / 21 killed / 2 running）\\n- **C1/C2/C3/C5/C6/S3→C/S7→C confirmed**\\n- **C8 partially_confirmed**（D060）：LLaMA qualitative direction consistent, quantitative interaction weaker\\n- **C5b future_work**（D056）：oracle recovery 18% < 30% gate\\n- C4 降级为 §6 supporting, C7 running\\n- 论文全文已完成（§1-§8），PDF 可编译\\n- D059：d_z 分场景报告（within-importance 保留，涉及 random 不报）\\n- ⚠️ Qwen mid-phase 58% null rate + imp vs rand paired 全部不显著，等 n=500 评估\\n\\n## 近期任务\\n- [ ] **[P0]** c2_n500_deepseek — cuda:0+1 RUNNING, DeepSeek s020 进行中, ETA ~2026-05-15 15-17h UTC\\n- [ ] **[P0]** c2_qw_n500 — cuda:2+3 RUNNING, Qwen s015 ~92%, ETA ~2026-05-15 21h UTC\\n- [ ] **[P1]** c2_n500 完成后：分析 pipeline（median II + bootstrap CI + d_z within-importance only）\\n- [ ] **[P1]** 分析完成后：Paper Agent 统一更新论文（n=500 tables/figures + c5b §8 + C8 限定语 + Qwen caveat）\\n- [ ] 全部完成后提交 Group C full review\\n\\n## GPU 预算\\n- RTX 6000 Pro ×4: westd-22162 cuda:0~3\\n- 当前分配：cuda:0+1 → c2_n500_deepseek | cuda:2+3 → c2_qw_n500\\n- 已用: ~25h / ~2
…[truncated 1427 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_prep_paper_update_plan_20260514T220436",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-14T22:08:29.838708+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "paper/**/*.{md,tex}",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_prep_paper_update_plan_20260514T220436",
  "tool": "Glob",
  "tool_args": {
    "pattern": "paper/**/*.{md,tex}",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-14T22:08:29.838845+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_prep_paper_update_plan_20260514T220436",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-14T22:08:29.838992+00:00_

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
  "session": "worker_prep_paper_update_plan_20260514T220436",
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

_source line 10 · 2026-05-14T22:08:29.839121+00:00_

artifacts/_project/paper/methodology.tex
artifacts/_project/paper/appendix_results.tex
artifacts/_project/paper/appendix.tex
artifacts/_project/paper/background.tex
artifacts/_project/paper/analysis.tex
artifacts/_project/paper/main.tex
artifacts/_project/paper/appendix_moved.tex
artifacts/_project/paper/abstract.tex
artifacts/_project/paper/discussion.tex
artifacts/_project/paper/results.tex
artifacts/_project/paper/conclusion.tex
artifacts/_project/paper/appendix_disc_analysis.tex
artifacts/_project/paper/introduction.tex
artifacts/_project/paper/limitations.tex
artifacts/_project/paper/related_work.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_prep_paper_update_plan_20260514T220436",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-14T22:08:29.839254+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "artifacts/**/*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_prep_paper_update_plan_20260514T220436",
  "tool": "Glob",
  "tool_args": {
    "pattern": "artifacts/**/*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-14T22:08:29.839429+00:00_

artifacts/_project/intermediate/phase_segmentation.py
artifacts/pacs/profiling/__init__.py
artifacts/pacs/utils/__init__.py
artifacts/_project/intermediate/metrics.py
artifacts/_project/intermediate/run_profiling.py
artifacts/_project/intermediate/interaction_index.py
artifacts/pacs/__init__.py
artifacts/pacs/utils/data_utils.py
artifacts/pacs/__pycache__/__init__.cpython-314.pyc
artifacts/pacs/profiling/__pycache__/__init__.cpython-314.pyc
artifacts/pacs/utils/__pycache__/__init__.cpython-314.pyc
artifacts/pacs/utils/__pycache__/data_utils.cpython-314.pyc
artifacts/pacs/profiling/__pycache__/run_profiling.cpython-314.pyc
artifacts/pacs/utils/__pycache__/metrics.cpython-314.pyc
artifacts/pacs/compound/__init__.py
artifacts/pacs/compound/head_selector.py
artifacts/pacs/compound/kv_evictor.py
artifacts/pacs/compound/compound_forward.py
artifacts/pacs/compound/__pycache__/__init__.cpython-314.pyc
artifacts/pacs/compound/__pycache__/head_selector.cpython-314.pyc
artifacts/m2_m4_code_readiness.md
artifacts/mvp_ii_analysis.md
artifacts/mvp_interaction_index_profiling/report/mvp_ii_analysis.md
artifacts/pacs/profiling/phase_segmentation.py
artifacts/pacs/profiling/__pycache__/interaction_index.cpython-314.pyc
artifacts/m1_phase_segmentation_analysis.md
artifacts/pacs/profiling/__pycache__/phase_segmentation.cpython-314.pyc
artifacts/pacs/profiling/alt_segmentation.py
artifacts/pacs/profiling/__pycache__/alt_segmentation.cpython-314.pyc
artifacts/pacs/compound/test_compound.py
artifacts/pacs/profiling/analyze_results.py
artifacts/mvp_ii_profiling_v2/report/mvp_ii_v2_analysis.md
artifacts/mvp_ii_profiling_v2/report/mvp_ii_v2_analysis_c4933e.md
artifacts/mvp_ii_v3_analysis.md
artifacts/mvp_ii_profiling_v3/report/mvp_ii_v3_analysis.md
artifacts/pacs/profiling/analyze_v4_results.py
artifacts/pacs/profiling/run_profiling.py
artifacts/pacs/profiling/interaction_index.py
artifacts/pacs/utils/metrics.py
artifacts/v5_status_check.md
artifacts/literature_scan_phase_adaptive.md
artifa
…[truncated 3469 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_prep_paper_update_plan_20260514T220436",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-14T22:08:29.839590+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse -maxdepth 3 -type f \\( -name \"*.tex\" -o -name \"*.md\" \\) | head -50",
  "description": "Find tex and md files in project directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_prep_paper_update_plan_20260514T220436",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse -maxdepth 3 -type f \\( -name \"*.tex\" -o -name \"*.md\" \\) | head -50",
    "description": "Find tex and md files in project directory"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-14T22:08:29.839739+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/IDEA_BRIEF.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/task_context/agent.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/task_context/director.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/task_context/reviewer.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/memory.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/report.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/AGENTS.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/CLAUDE.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/literature_scan_phase_adaptive.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/m1_phase_segmentation_analysis.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/m2_m4_code_readiness.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/reference_audit_report.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/n500_update_checklist.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/mvp_ii_v3_analysis.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/n500_paper_patch_plan.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/c2_n500_paper_update_checklist.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/consistency_audit_final.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/
…[truncated 3183 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_prep_paper_update_plan_20260514T220436",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-14T22:08:29.839927+00:00_

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
  "session": "worker_prep_paper_update_plan_20260514T220436",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/abstract.tex"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-14T22:08:29.840078+00:00_

1	\begin{abstract}
2	Compound sparsity---simultaneously pruning attention heads and evicting KV cache entries---is essential for efficient LLM inference but produces super-additive quality degradation whose structure is poorly understood.
3	Prior work treats compound interaction magnitude as approximately constant across the generation process.
4	We show that this assumption is wrong: compound sparsity severity is an emergent phase-strategy interaction that varies by over an order of magnitude across reasoning phases.
5	
6	We evaluate compound sparsity on three models---DeepSeek-R1-Distill-Qwen-7B, Qwen2.5-7B-Instruct (both Qwen2ForCausalLM), and DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM)---spanning two architectures, using 50 MATH-500 problems, measuring the Interaction Index---a super-additivity metric---across quantile-segmented reasoning phases at sparsity levels $s \in \{0.15, 0.20, 0.25, 0.30\}$.
7	Under importance-based KV cache eviction, the median Interaction Index difference between low-sparsity and high-sparsity reasoning phases increases monotonically from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$, with paired Cohen's $d_z$ growing from $0.44$ (small) to $0.80$ (large); Bonferroni-corrected permutation tests yield $p < 0.005$ at all four sparsity levels.
8	Random eviction produces no significant phase modulation in 7/8 conditions; the single exception (Qwen $s{=}0.30$, $p{=}0.012$) shows negligible effect size ($d_z{=}{-}0.04$), confirming that the severity gradient is strategy-specific, not an inherent property of compound sparsity.
9	At $s{=}0.25$, a crossover emerges: importance-based eviction outperforms random in high-sparsity phases ($\widetilde{\mathrm{II}} = 0.032$ vs.\ $0.818$) yet underperforms in low-sparsity phases ($\widetilde{\mathrm{II}} = 7.196$ vs.\ $1.363$)---a qualitative reversal in strategy ranking.
10	The pattern replicates on Qwen2.5-7B-Instruct at $s \geq 0.20$ ($d_z \geq 0.55$; Spearman $\rho = 1.0$; gradient permutation
…[truncated 815 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_prep_paper_update_plan_20260514T220436",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-14T22:08:29.840221+00:00_

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
  "session": "worker_prep_paper_update_plan_20260514T220436",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-14T22:08:29.840375+00:00_

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
  "session": "worker_prep_paper_update_plan_20260514T220436",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-14T22:08:29.840545+00:00_

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
  "session": "worker_prep_paper_update_plan_20260514T220436",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-14T22:08:29.840686+00:00_

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
  "session": "worker_prep_paper_update_plan_20260514T220436",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-14T22:08:29.841013+00:00_

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
  "session": "worker_prep_paper_update_plan_20260514T220436",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/methodology.tex"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-14T22:08:29.841166+00:00_

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
22	All confidence intervals and significance tests use 
…[truncated 262 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_prep_paper_update_plan_20260514T220436",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-14T22:08:29.841314+00:00_

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
  "session": "worker_prep_paper_update_plan_20260514T220436",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/results.tex"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-14T22:08:29.841892+00:00_

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
…[truncated 8203 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_prep_paper_update_plan_20260514T220436",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-14T22:08:29.842107+00:00_

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
  "session": "worker_prep_paper_update_plan_20260514T220436",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/analysis.tex"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-14T22:08:29.842260+00:00_

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
  "session": "worker_prep_paper_update_plan_20260514T220436",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-14T22:08:29.842402+00:00_

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
  "session": "worker_prep_paper_update_plan_20260514T220436",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/discussion.tex"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-14T22:08:29.842573+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Quantitative surprise.}
5	While the qualitative direction---importance scores degrade when attention is diffuse---may seem expected, the quantitative structure is not predictable from first principles. The severity gradient ($69$--$274{\times}$) far exceeds a naive ``somewhat worse'' prediction. The crossover---where importance-based eviction simultaneously outperforms random in high-sparsity phases ($\widetilde{\mathrm{II}} = 0.032$ vs.\ $0.818$) and underperforms in low-sparsity phases ($7.196$ vs.\ $1.363$)---cannot be derived from single-axis entropy reasoning. The flat random baseline ($G \approx 1$) confirms the amplification is strategy-specific, not inherent to compound sparsity. % exp_id: bf16_importance_s015..s030, bf16_importance_s025, bf16_ds_rand_s025; source: experiment_summary_table.json
6	
7	\paragraph{Implications for deployment.}
8	Applying a uniform compression budget across all inference steps implicitly accepts order-of-magnitude severity penalties during low-sparsity reasoning phases. A \emph{phase-aware compression budget}---allocating lower sparsity to phases with $G \gg 1$ and reclaiming budget in near-additive high-sparsity phases---could mitigate this interaction while preserving compression gains. The severity gradient provides a natural signal for such allocation. Discrimination collapse depends on attention-mass-based importance scoring shared by major KV cache methods (H$_2$O \cite{h2o-neurips2023}, SnapKV \cite{snapkv-neurips2024}, PyramidKV \cite{pyramidkv-2024}), suggesting broad applicability. Extended discussion in Appendix~\ref{app:extended-discussion}.
9	
10	\paragraph{Architecture-dependent magnitude.}
11	Cross-architecture validation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM) provides partial support for the qualitative pattern---monotonically increasing severity gradient under importance-based eviction with within-strategy phase gradient $d_z \geq 1.0$---
…[truncated 803 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_prep_paper_update_plan_20260514T220436",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-14T22:08:29.842714+00:00_

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
  "session": "worker_prep_paper_update_plan_20260514T220436",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/conclusion.tex"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-14T22:08:29.842839+00:00_

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
  "session": "worker_prep_paper_update_plan_20260514T220436",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-14T22:08:29.842971+00:00_

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
  "session": "worker_prep_paper_update_plan_20260514T220436",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/limitations.tex"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-14T22:08:29.843098+00:00_

1	\paragraph{Model scale and architecture.}
2	All experiments are conducted at the 7B parameter scale. Whether the phase-modulated severity patterns persist, amplify, or attenuate at larger scales (e.g., 70B) remains untested. Cross-architecture validation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, \S\ref{sec:cross-arch}) partially extends the findings beyond the Qwen2 architecture: the directional pattern is qualitatively consistent but the interaction magnitude is substantially weaker and random pruning also exhibits a non-trivial phase gradient on LLaMA. The qualitative pattern has been tested on only two architecture families at the 7--8B scale; further validation on larger models and more diverse architectures (e.g., Mistral, multi-latent attention) is needed.
3	
4	\paragraph{Task coverage.}
5	We evaluate exclusively on MATH-500, a mathematical reasoning benchmark. Different reasoning tasks---code generation, commonsense reasoning, multi-hop question answering---may induce different phase structures with different sparsity distributions, potentially altering the severity gradient profile.
6	
7	\paragraph{Mechanism.}
8	The discrimination collapse mechanism is supported by correlational evidence (consistent Gini/CV reduction across all conditions); causal validation through controlled entropy manipulation is needed. The entropy redistribution component replicates on only 2/4 Qwen conditions, suggesting model-specific factors.
9	
10	\paragraph{Sparsity range.}
11	Our experiments span $s \in \{0.15, 0.20, 0.25, 0.30\}$. More extreme sparsity ($s > 0.50$) may exhibit qualitatively different interaction dynamics. We do not report inference throughput or latency measurements, which are necessary for a complete deployment analysis but orthogonal to our severity characterization. Extended limitations in Appendix~\ref{app:limitations}.
12	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_prep_paper_update_plan_20260514T220436",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-14T22:08:29.843228+00:00_

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
  "session": "worker_prep_paper_update_plan_20260514T220436",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/main.tex"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-14T22:08:29.843360+00:00_

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
21	\title{Phase-Modulated Compound Sparsity:\\Strategy-Dependent Severity Gradients in Reasoning Models}
22	
23	\author{Anonymous}
24	
25	\begin{document}
26	
27	\maketitle
28	
29	\input{abstract}
30	
31	\input{introduction}
32	\input{related_work}
33	\input{background}
34	\input{methodology}
35	\input{results}
36	\input{analysis}
37	\input{discussion}
38	\input{conclusion}
39	
40	\bibliography{references}
41	
42	\section*{Limitations}
43	\input{limitations}
44	
45	\appendix
46	\input{appendix}
47	\input{appendix_moved}
48	\input{appendix_disc_analysis}
49	
50	\end{document}
51	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_prep_paper_update_plan_20260514T220436",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-14T22:08:29.843515+00:00_

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
  "session": "worker_prep_paper_update_plan_20260514T220436",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix.tex"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-14T22:08:29.843666+00:00_

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
  "session": "worker_prep_paper_update_plan_20260514T220436",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-14T22:08:29.844503+00:00_

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
  "session": "worker_prep_paper_update_plan_20260514T220436",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_results.tex"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-14T22:08:29.844670+00:00_

1	% Appendix: supplementary results details
2	
3	\section{Cross-Model Replication Details}
4	\label{app:cross-model-details}
5	
6	\paragraph{Per-problem concordance.}
7	The per-problem concordance across models is not significant (mean $\rho = -0.11$, $p = 0.926$), indicating that while the aggregate gradient direction replicates, the specific problems driving severity differ between models---consistent with model-specific attention patterns rather than a universal per-problem vulnerability ranking. % exp_id: cross_model_analysis.json (spearman_rho=1.0, gradient_permutation_p=0.043, per_problem_concordance_p=0.926, mean_rho=-0.107)
8	
9	\paragraph{Random eviction control.}
10	As a control, random eviction on Qwen yields no systematic phase gradient at three of four sparsity levels (3/4 FAIL), mirroring DeepSeek's 4/4 FAIL pattern. At $s{=}0.30$, Qwen random produces a borderline PASS (permutation $p = 0.012$) but with negligible effect size ($d_z = -0.04$, CI spans zero), indicating no meaningful phase modulation. % exp_id: bf16_qw_rand_s015..s030; source: experiment_summary_table.json
11	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_prep_paper_update_plan_20260514T220436",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-14T22:08:29.844825+00:00_

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
  "session": "worker_prep_paper_update_plan_20260514T220436",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_disc_analysis.tex"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-14T22:08:29.845119+00:00_

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
14	Random eviction fails 7/8 paired permutation tests across both models; the single exception (Qwen $s{=}0.30$, $p{=}0.012$) exhibits negligible effect size ($d_z{=}{-}0.04$). The absence of a phase gradient under random masking isolates the amplification as strategy-specific. % exp_id: bf16_ds_rand_s015..s030, bf16_qw_rand_s015..s030
15	
16	\paragraph{Entropy mechanism boundary conditions.}
17	Directly measuring per-head entropy shifts across architectu
…[truncated 6489 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_prep_paper_update_plan_20260514T220436",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-14T22:08:29.845335+00:00_

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
  "session": "worker_prep_paper_update_plan_20260514T220436",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/background.tex"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-14T22:08:29.845538+00:00_

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
  "session": "worker_prep_paper_update_plan_20260514T220436",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-14T22:08:29.845699+00:00_

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
  "session": "worker_prep_paper_update_plan_20260514T220436",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_moved.tex"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-14T22:08:29.845904+00:00_

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
…[truncated 11098 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_prep_paper_update_plan_20260514T220436",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-14T22:08:29.846213+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/n500_paper_patch_plan.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_prep_paper_update_plan_20260514T220436",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/n500_paper_patch_plan.md"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-14T22:08:29.846530+00:00_

1	# n=500 Paper Patch Plan
2	
3	> 精确位置清单 + 预写文本
4	> 基于论文目录：`artifacts/_project/paper/`
5	> 生成日期：2026-05-14
6	> 硬约束：D054 (median only), D059 (within-imp d_z only), D060 (C8=partially_confirmed)
7	
8	---
9	
10	## A. 更新位置清单
11	
12	### A1. Tables（含 n=50 数据的表格）
13	
14	| # | 文件:行号 | 表格 ID | 内容 | 操作 |
15	|---|----------|---------|------|------|
16	| T1 | results.tex:10-23 | tab:aggregate-ii | DeepSeek aggregate Δ by strategy (caption L13: "n=50") | 替换 8 个数据单元格 + caption n 值 |
17	| T2 | results.tex:31-53 | tab:main-results | Per-phase II breakdown (caption L34: "50 problems") | 替换 24 个数据单元格 + caption n 值 |
18	| T3 | results.tex:83-98 | tab:llama-cross-arch | LLaMA cross-arch (caption L86: "n=49") | **D059 重构**：d_z 列为 imp-vs-rand → 替换为 within-imp d_z 或改为 Wilcoxon p + median_diff；若 LLaMA 不重跑则数值不变但列定义必须改 |
19	| T4 | results.tex:108-124 | tab:cohens-d | DS/QW paired d_z (within-imp, 合规) | 替换 16 个数据单元格（4行 × 4列） |
20	| T5 | appendix_moved.tex:30-43 | tab:cross-model | Cross-model Δ comparison | 替换 8 个数据单元格 |
21	| T6 | appendix_moved.tex:70-85 | tab:permutation | Permutation test results (caption L73: "n=49") | 替换 12 个数据单元格 + caption n 值 |
22	| T7 | appendix_moved.tex:103-123 | tab:discrimination-metrics-full | Gini/CV deltas | 替换 16 个数据单元格（若 C4 基于 n=500 重跑） |
23	| T8 | appendix_moved.tex:143-163 | tab:entropy-deltas | Entropy Δ𝓗 | 替换 8 个数据单元格（若 C4 基于 n=500 重跑） |
24	
25	---
26	
27	### A2. Quantitative Claims（文中引用具体数字的句子）
28	
29	#### abstract.tex
30	| # | 行号 | 当前文本片段 | 替换说明 |
31	|---|------|-------------|---------|
32	| Q1 | 6 | `50 MATH-500 problems` | → `500 MATH-500 problems` |
33	| Q2 | 6 | `$s \in \{0.15, 0.20, 0.25, 0.30\}$` | 保留（sparsity levels 不变） |
34	| Q3 | 7 | `from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$` | → n=500 DeepSeek importance Δ (4值) |
35	| Q4 | 7 | `$d_z$ growing from $0.44$ (small) to $0.80$ (large)` | → n=500 within-imp d_z (合规 ✓) |
36	| Q5 | 7 | `$p < 0.005$ at all four sparsity levels` | → n=500 permutation p |
37	| Q6 | 8 | `7/8 conditions` | → n=500
…[truncated 14987 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_prep_paper_update_plan_20260514T220436",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-14T22:08:29.846716+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/chart/paper_figures_v2_manifest.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_prep_paper_update_plan_20260514T220436",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/chart/paper_figures_v2_manifest.txt"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-14T22:08:29.846855+00:00_

1	fig4_bootstrap.pdf (19.1 KB) — Forest plot, difference statistic 95% CI, Bonferroni p annotations
2	fig5_crossmodel.pdf (18.5 KB) — Cross-model comparison, DS solid/QW dashed, symlog Y
3	Script: /root/autodl-tmp/pacs/analysis/generate_paper_figures.py
4	Style: serif, 9pt, hidden top/right spines, 300 dpi

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_prep_paper_update_plan_20260514T220436",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-14T22:08:29.847090+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/paper_n500_update_plan.md",
  "content": "# n=500 Paper Update Plan — Section-by-Section Diff Spec\n\n> 生成日期: 2026-05-14\n> 前置依赖: n500_paper_patch_plan.md（逐行数值替换清单）\n> 本文档补充: 每个 section 的 claim 强度评估 + 条件分支逻辑 + Qwen caveat + C8/C5b 专项\n\n---\n\n## 硬约束（Paper Worker 必读）\n\n| 约束 | 来源 | 含义 |\n|------|------|------|\n| 指标只用 **median + median bootstrap CI** | D054 | 禁止 mean，所有表格/正文/caption 一律 median |\n| d_z 只报 **within-importance**（low−high 配对） | D059 | imp-vs-rand d_z 和 random d_z 全部删除，改用 Wilcoxon p + median_diff |\n| LLaMA 为 **qualitative pattern**，不做定量跨架构比较 | D060 | 禁用 \"confirms\"，只用 \"suggests\"/\"provides partial support\"/\"directionally consistent\" |\n\n---\n\n## §Abstract (abstract.tex)\n\n### 当前 n=50 数据引用\n- L6: `50 MATH-500 problems`\n- L7: DeepSeek Δ `0.39→14.59`, d_z `0.44→0.80`, `p < 0.005`\n- L8: random `7/8 conditions`, Qwen s030 `p=0.012`, `d_z=-0.04`（**D059 违规**）\n- L9: crossover II 数值 `0.032 vs 0.818`, `7.196 vs 1.363`\n- L10: Qwen `d_z ≥ 0.55`, `ρ=1.0`, `p=0.043`; LLaMA `d_z (0.19→0.34)`（**D059 违规**）, `~1/40`\n\n### n=500 更新操作\n1. `50` → `500`\n2. 替换所有 DeepSeek/Qwen 数值为 n=500 结果\n3. **D059 修复**:\n   - L8: 删 `d_z=-0.04`，改为 `negligible median difference`\n   - L10: 删 LLaMA imp-vs-rand d_z 序列，改为 `Wilcoxon signed-rank test reaching significance at s=0.30 (p_Bonf=X)`\n4. LLaMA `~1/40` → 用 n=500 DeepSeek Δ 重算比值\n\n### Claim 强度调整逻辑\n- **若 n=500 CI 变窄且不跨零**: 可加强 → 删除 `(small)` 修饰词，直接报 d_z 值\n- **若 Qwen s015 CI 仍跨零**: 保持 `s ≥ 0.20` 下界，不加强\n- **若 Qwen s015 CI 排除零**: 可改为 `s ≥ 0.15`，abstract 同步\n- **若 random PASS/FAIL 比例变化**: 更新 `7/8` 为实际比例\n\n---\n\n## §1 Introduction (introduction.tex)\n\n### 当前 n=50 数据引用\n- L14: DeepSeek Δ `0.39→14.59`, d_z `0.44→0.80`, `p < 0.005`\n- L15: Qwen `d_z ≥ 0.55`, LLaMA `~1/40`\n- L16: `7/8 conditions non-significant`\n\n### n=500 更新操作\n1. L14: 与 abstract Q3/Q4/Q5 同步替换\n2. L15: 与 abstract Q9/Q11 同步\n3. L16: 与 abstract Q6 同步\n\n### Claim 强度调整逻辑\n- Introduction 措辞已较保守（`partially extends`），n=500 后无需改措辞方向\n- 若 n=500 效应量增大（d_z > 1.0），可在 `($d_z$: X → Y)` 后加 `(large)` 标注\n\n---\n\n## §2 Related Work (related_work.tex)\n\n### n=50 数据引用: **无**\n### n=500 更新操作: **无**（纯引用区分，不含实验数据）\n\n---\n\n## §3 Background (background.tex)\n\n### n=50 数据引用: **无**（只有公式定义）\n### n=500 更新操作: **无**\n\n---\n\n## §4 Experimental Setup (methodology.tex)\n\n### 当前 n=50 数据引用\n- L10: `50 problems stratified from MATH-500`\n- L18: `mean/median ratios up to 43:1`\n- L22: `All tests yield p_Bonf < 0.005`\n\n### n=500 更新操作\n1. L10: `50 problems stratified from MATH-500` → `500 problems from MATH-500`（删 \"stratified\"，500≈全集）\n2. L18: `43:1` → n=500 实际 mean/median ratio\n3. L22: 更新 p 值（预期 n=500 仍 <0.005，但需确认实际值）\n\n### Claim 强度: 无需调整（方法描述）\n\n---\n\n## §5 Results (results.tex)\n\n### 当前 n=50 数据引用（按子节）\n\n**§5.1 Strategy-Dependent Severity (L1-23)**\n- L8: Δ `0.39→14.59`, `37×` amplification; random `-0.02 to 1.54`\n- Table 1 (tab:aggregate-ii): 8 个数据单元格, caption `n=50`\n  - Importance: 0.39, 1.48, 7.16, 14.59\n  - Random: 0.01, -0.02, 0.54, 1.54\n\n**§5.2 Phase-Modulated Amplification (L26-60)**\n- L29: G `69×→274×`, II_high `0.006→0.053`, random G `0.9–1.7×`\n- Table 2 (tab:main-results): 24 个数据单元格, caption `50 problems`\n  - 完整 per-phase II breakdown（8行×3列 II + Δ + G）\n- Fig 1 (fig1_dose_response.pdf): G vs s 曲线, caption `69×→274×`\n\n**§5.3 Crossover (L63-67)**\n- L66: II 数值 `0.032 vs 0.818`, `7.196 vs 1.363`, `5.3× reversal`\n\n**§5.4 Cross-Model (L68-72)**\n- L71: Qwen Δ `0.04→2.94`, `~1/5`, `ρ=1.0`, `p=0.043`, `d_z=0.28 CI includes zero`, `d_z ≥ 0.55`\n\n**§5.5 Cross-Architecture (L74-98)**\n- L79: LLaMA d_z `0.19→0.26→0.29→0.34`（**D059 违规**）, `p=0.029`, `Δ=0.020 [0.002,0.043]`\n- L79: within-imp d_z `[1.00, 1.12]`（合规）, random d_z `[0.35, 0.45]`（**D059 违规**）\n- L81: `~40× smaller than DeepSeek`, `~7× smaller than Qwen`\n- Table 3 (tab:llama-cross-arch): d_z 列为 imp-vs-rand（**D059 违规，需重构**）\n\n**§5.6 Statistical Validation (L101-127)**\n- L104: permutation `p < 0.005`, `0.37→9.85`\n- L106: DeepSeek d_z `0.44→0.80`, Qwen d_z `0.28→1.02`, `0.89/1.02 vs 0.68/0.80`\n- Table 4 (tab:cohens-d): 16 个数据单元格（DS/QW × 4 sparsity × d_z + Δ[CI]）\n\n### n=500 更新操作\n\n**Tables 替换清单**:\n\n| Table | ID | 需替换单元格数 | 数据来源 |\n|-------|----|--------------|---------|\n| Table 1 | tab:aggregate-ii | 8 + caption n | n=500 experiment_summary_table.json median_diff |\n| Table 2 | tab:main-results | 24 + caption n | n=500 per-phase median II |\n| Table 3 | tab:llama-cross-arch | **重构**: d_z列→within-imp d_z 或删除 d_z 列改为 Wilcoxon p + Δ̃ | LLaMA 不重跑→数值不变但列定义改 |\n| Table 4 | tab:cohens-d | 16 | n=500 within-imp d_z + paired median diff + CI |\n\n**Figures 替换清单**:\n\n| Figure | 文件 | 数据来源 | 操作 |\n|--------|------|---------|------|\n| Fig 1 | fig1_dose_response.pdf | n=500 G values (imp+rand) | 重绘，caption G值同步 |\n\n**D059 修复** (§5.5):\n- L79 `paired d_z (0.19→...→0.34)` → `Wilcoxon signed-rank tests with median paired difference increasing from X to Y`\n- L79 `d_z ∈ [0.35, 0.45]` → `random eviction also shows a non-trivial phase gradient (Wilcoxon p < X)`\n- Table 3: d_z列→within-importance d_z (low−high)，caption 相应修改\n\n**C8 限定语修复** (§5.5):\n- L79 `The qualitative pattern replicates` → `The qualitative pattern is directionally consistent`（唯一需修改处，其余已合规）\n\n### Claim 强度调整逻辑\n\n**§5.4 Cross-Model — Qwen onset threshold 关键分支**:\n- **若 Qwen n=500 s015 d_z CI 排除零**: onset threshold 从 `s ≥ 0.20` 改为 `s ≥ 0.15`，L71 删 `CI includes zero`，改为 `d_z=X [CI_lo, CI_hi]`\n- **若 Qwen n=500 s015 CI 仍跨零**: 保持 `marginal at s=0.15, reliable at s ≥ 0.20`，在后续文字加 caveat: `the onset threshold for reliable detection appears model-dependent (DeepSeek: s ≥ 0.15; Qwen: s ≥ 0.20)`\n- **若 Qwen n=500 s020 CI 也跨零**: 升级 caveat 为 `s ≥ 0.25`，narrative 改为 `compound effect emerges above threshold sparsity (~s020-s025)`\n\n**§5.6 Statistical Validation — n=500 power 增益**:\n- n=500 预期 CI 收窄 ~√10 倍，d_z 估计更稳定\n- 若所有 CI lower bounds > 0: 可删除 `marginal` 相关修饰语\n- 若 permutation p 值从 `< 0.005` 变为 `< 0.001`: 更新但不改措辞\n\n---\n\n## §6 Analysis (analysis.tex)\n\n### 当前 n=50 数据引用\n- L4: Gini Δ `0.030–0.081` (DS), `0.010–0.020` (QW)\n- L6: entropy Δ𝓗 `[-0.047, -0.040]` (DS), `+0.045` (QW s025)\n\n### n=500 更新操作\n- **条件性**: C4 entropy 分析是否基于 n=500 重跑？\n  - **若重跑**: 替换所有 Gini/CV/entropy 数值\n  - **若不重跑**: 保留 n=50 数值，添加脚注 `Mechanism analysis based on a 30-problem subset; main results use n=500`\n\n### Claim 强度: 无需调整（机制分析，结论不变）\n\n---\n\n## §7 Discussion (discussion.tex)\n\n### 当前 n=50 数据引用\n- L5: G `69–274×`, crossover II `0.032 vs 0.818`, `7.196 vs 1.363`, `G ≈ 1`\n- L11: LLaMA `~40× smaller`, `~7× smaller`, `d_z ≥ 1.0`, `d_z ∈ [0.35, 0.45]`（**D059 违规**）\n\n### n=500 更新操作\n1. L5: 与 §5 同步更新所有数值\n2. **D059 修复**: L11 删 random d_z `[0.35, 0.45]`，改为定性描述 + Wilcoxon p\n3. L11: `~40×/~7×` 用 n=500 重算\n\n### 新增内容\n- **C5b pilot 结果** (B2 预写文本): 插入 L8 段末（`Extended discussion in Appendix~\\ref{app:extended-discussion}.` 之前）\n  - 内容: oracle recovery 18% < 30% gate, heuristic 32% CI 跨零, 作为 future work\n  - 这是 §8 future work 的铺垫\n\n### Claim 强度调整\n- 若 n=500 G 值变化幅度 ≤20%: `far exceeds a naive \"somewhat worse\" prediction` 保留\n- 若 G 值大幅缩小（如 274× → <100×）: 需调弱 `far exceeds` 措辞\n\n---\n\n## §8 Conclusion (conclusion.tex)\n\n### 当前 n=50 数据引用\n- L4: G `69×→274×`, d_z `0.44→0.80`, `7/8`, `d_z ≥ 0.55`, `~1/40`\n\n### n=500 更新操作\n1. 全部数值与 §5/Abstract 同步\n2. 若 n=500 效应增强: 可从 `strongly modulated` 加强为 `robustly modulated`（谨慎）\n\n### 新增内容\n- L5 之后追加一句指向 discussion C5b: `A preliminary pilot of phase-aware budget reallocation yielded 18\\% oracle recovery, below pre-registered thresholds, motivating joint phase--strategy optimization as future work (\\S\\ref{sec:discussion}).`\n\n### C5b §8 Future Work 准确性验证\n当前 conclusion.tex L5: `These findings motivate phase-aware sparsity allocation for reasoning model deployment.`\n- **问题**: 这句暗示 mitigation 是直接可行的，但 C5b pilot 已经 gate_failed\n- **修复**: 改为 `These findings motivate phase-aware sparsity allocation as a promising but non-trivial direction: a preliminary oracle pilot recovered only 18\\% of compound interaction, suggesting that effective mitigation requires joint optimization of budget allocation and strategy selection across phases.`\n\n---\n\n## Limitations (limitations.tex)\n\n### 当前 n=50 数据引用\n- L1: LLaMA `d_z ∈ [0.35, 0.45]`（隐含在定性描述中，无具体数字）\n- L11: `s ∈ {0.15, 0.20, 0.25, 0.30}`\n\n### n=500 更新操作\n- L1: 无具体数字需替换（定性描述），但审查 LLaMA 措辞是否合规 → 已合规（`partially extends`）\n- **新增**: L1 末尾加 `Cross-architecture validation is based on n=50; repeating at n=500 is future work.`（若 LLaMA 不重跑）\n\n### Claim 强度\n- 若 n=500 CI 全部排除零: 可删除 `$n{=}49$ paired problems` statistical scope 中关于小样本的讨论，或改为 `$n{=}X$ paired problems (primary models) and $n{=}49$ (cross-architecture)`\n- Statistical scope (L44-50): `n=49`/`n=46` → `n=X`/`n=Y`（n=500 有效问题数）\n\n---\n\n## Appendix\n\n### appendix.tex\n- L38: multiplicative null G `58–241×` → n=500 值\n\n### appendix_results.tex\n- L7: per-problem concordance `ρ=-0.11, p=0.926` → n=500 值\n- L10: random PASS/FAIL 计数 + `p=0.012`, `d_z=-0.04`（**D059 违规**）\n\n### appendix_moved.tex\n\n**Tables**:\n| Table | ID | 操作 |\n|-------|----|------|\n| tab:cross-model | L30-43 | 替换 8 单元格 |\n| tab:permutation | L70-85 | 替换 12 单元格 + caption n |\n| tab:discrimination-metrics-full | L103-123 | 条件性：C4 重跑则替换 |\n| tab:entropy-deltas | L143-163 | 条件性：C4 重跑则替换 |\n\n**Figures**:\n| Figure | 文件 | 操作 |\n|--------|------|------|\n| fig3_crossover.pdf | L15 | n=500 s=0.25 per-phase median → 重绘 |\n| fig4_bootstrap.pdf | L89 | n=500 paired d_z + permutation CI → 重绘 |\n| fig5_crossmodel.pdf | L47 | n=500 DS/QW paired median diffs → 重绘 |\n\n**文本**:\n- L11: crossover 全部数值（6 个数字 + 4 个比值）\n- L26: `Four of the 50 problems excluded` → `X of 500 problems excluded`\n- L53/56: per-problem concordance + random d_z（**D059 违规**）\n- L62/73: `n=49` → n=500 值\n- L68: CI lower bounds `0.19→0.69→1.66→6.70`\n\n### appendix_disc_analysis.tex\n- L4: random Gini 范围 `−0.031 to −0.073; Qwen: −0.019 to −0.045`（条件性）\n- L11: `II_high < 0.06`, `0.105`\n- L14: `7/8`, `p=0.012`, `d_z=-0.04`（**D059 违规**）\n- L45-50: statistical scope 全部 n 值 + 偏度统计 + permutation CI\n- L57: growth rate `3.8×→4.8×→2.0×`\n\n---\n\n## Qwen Caveat 专项\n\n### 触发条件\n**若 Qwen n=500 mid-phase (s015/s020) 仍不显著**:\n\n### 需加 caveat 的位置\n\n| # | 文件 | 位置 | 当前文本 | 需加的限定 |\n|---|------|------|---------|-----------|\n| QC1 | abstract.tex:10 | Qwen 结果句 | `$d_z \\geq 0.55$` | 加 `at $s \\geq 0.20$`（若 s015 仍不显著）|\n| QC2 | results.tex:71 | §5.4 末尾 | Qwen cross-model | 插入 B1 预写文本（imp-vs-rand 衰减 caveat）|\n| QC3 | appendix_moved.tex:28 | cross-model detail | `Qwen reproduces the monotonic severity gradient` | 加 `at $s \\geq 0.20$; the effect is marginal at $s{=}0.15$` |\n| QC4 | limitations.tex | 新增 | （无） | 加 `The onset sparsity for reliable phase modulation is model-dependent` |\n| QC5 | paper_framing.md | C2 预注册 | `叙事改为 'compound effect emerges above threshold sparsity (~s020)'` | 执行预注册承诺 |\n\n### 若 Qwen n=500 s015 显著\n- 删除所有 `marginal at s=0.15` 限定\n- onset threshold 统一为 `s ≥ 0.15`\n- abstract/introduction 可加强为 `replicates at all four sparsity levels`\n\n### Qwen imp-vs-rand 对比\nD058 记录 n=50 imp-vs-rand 全不显著。n=500 后:\n- **若仍全不显著**: 在 §5.4 加 B1 caveat（已预写），说明 within-importance gradient robust 但 strategy contrast attenuated\n- **若 s025/s030 显著**: 报告为 `strategy contrast reaches significance at higher sparsity`\n- **若全显著**: 删 caveat，报告为 `strategy contrast replicates on Qwen at all levels`\n\n---\n\n## C8 限定语专项\n\n### 当前 LLaMA partially_confirmed 措辞审查\n\n| # | 文件:行号 | 当前文本 | 状态 |\n|---|----------|---------|------|\n| 1 | abstract.tex:10 | `suggests cross-architecture generalization, though at...` | ✅ 合规 |\n| 2 | introduction.tex:15 | `partially extends to a distinct architecture` | ✅ 合规 |\n| 3 | results.tex:79 | `The qualitative pattern replicates` | ⚠️ 需改为 `is directionally consistent` |\n| 4 | results.tex:81 | `qualitatively consistent...substantially weaker` | ✅ 合规 |\n| 5 | discussion.tex:11 | `provides partial support for the qualitative pattern` | ✅ 合规 |\n| 6 | conclusion.tex:4 | `partially extends cross-architecture` | ✅ 合规 |\n| 7 | limitations.tex:2 | `partially extends the findings beyond` | ✅ 合规 |\n| 8 | appendix_disc_analysis.tex:33 | `provides partial support` | ✅ 合规 |\n\n**唯一需修改**: #3 results.tex:79\n\n### n=500 后是否需要调整 C8\n- LLaMA 不重跑 n=500（未在 ROADMAP 中），所以 C8 数据不变\n- n=500 改变的是 DeepSeek/Qwen 的 Δ 绝对值 → 重算 LLaMA/DS 和 LLaMA/QW 的比值\n  - 当前: `~40× smaller` (DS), `~7× smaller` (QW)\n  - n=500 后: 分母变化 → 比值可能变化\n  - **操作**: 等 n=500 DS/QW Δ 出来后重算，更新 abstract/results/discussion/conclusion 中的倍数\n\n---\n\n## C5b §8 Future Work 专项\n\n### 当前状态\n- C5b: `future_work`（D056: oracle recovery 18% < 30% gate, heuristic 32% CI 跨零）\n- 论文**无独立 Future Work section**\n\n### 当前提及位置\n| # | 文件 | 内容 | 准确性 |\n|---|------|------|--------|\n| 1 | discussion.tex:8 | `A phase-aware compression budget...could mitigate...` | ⚠️ 过于乐观——未提及 pilot 失败 |\n| 2 | conclusion.tex:5 | `These findings motivate phase-aware sparsity allocation...` | ⚠️ 同上 |\n\n### 需要的修改\n1. **discussion.tex**: L8 段末插入 B2 预写文本（pilot 结果: oracle 18% < 30% gate）\n2. **conclusion.tex**: L5 改写，加入 pilot 限定（见上文 §8 Conclusion 部分）\n3. **验证 paper_framing.md 中 C5b 描述**: `oracle recovery 18%, heuristic 32% CI 跨零, 方向正确但效应量不足` → 与论文叙事一致 ✅\n4. **Heuristic > Oracle 悖论**: paper_framing.md 提到值得在论文中提及 → 在 discussion B2 文本中加一句: `Notably, the heuristic boundary (token position ratio) yielded higher recovery (32\\%) than the oracle (18\\%), suggesting that optimal phase granularity for mitigation may differ from that for characterization---an open question for future work.`\n\n---\n\n## Figures 完整重绘清单\n\n| # | 文件 | 引用位置 | n=500 数据源 | 操作 |\n|---|------|---------|-------------|------|\n| F1 | fig1_dose_response.pdf | results.tex:57 | n=500 G values from experiment_summary_table.json | 重绘: G vs s, imp solid + rand dashed, 95% bootstrap CI |\n| F2 | fig3_crossover.pdf | appendix_moved.tex:15 | n=500 s=0.25 per-phase median II | 重绘: grouped bar, 3 phases × 2 strategies |\n| F3 | fig4_bootstrap.pdf | appendix_moved.tex:89 | n=500 within-imp d_z + permutation CI | 重绘: forest plot, 4 sparsity levels |\n| F4 | fig5_crossmodel.pdf | appendix_moved.tex:47 | n=500 DS/QW paired median Δ | 重绘: line plot, DS solid + QW dashed, symlog Y |\n\n生成方式: 服务器端 `/root/autodl-tmp/pacs/analysis/generate_paper_figures.py`（draw-paper-figure skill）\n样式: serif, 9pt, hidden top/right spines, 300 dpi\n\n---\n\n## Tables 完整替换清单\n\n| # | Table ID | 文件:行号 | 单元格数 | 依赖 |\n|---|----------|----------|---------|------|\n| T1 | tab:aggregate-ii | results.tex:10-23 | 8 + caption | n=500 DS imp+rand Δ |\n| T2 | tab:main-results | results.tex:31-53 | 24 + caption | n=500 DS per-phase II |\n| T3 | tab:llama-cross-arch | results.tex:83-98 | **重构** | D059: 列定义改为 within-imp d_z；数值不变（LLaMA 不重跑） |\n| T4 | tab:cohens-d | results.tex:108-124 | 16 | n=500 DS/QW within-imp d_z + Δ[CI] |\n| T5 | tab:cross-model | appendix_moved.tex:30-43 | 8 | n=500 DS/QW Δ |\n| T6 | tab:permutation | appendix_moved.tex:70-85 | 12 + caption | n=500 permutation Δ + CI + p |\n| T7 | tab:discrimination-metrics-full | appendix_moved.tex:103-123 | 16 | **条件**: 仅 C4 重跑 |\n| T8 | tab:entropy-deltas | appendix_moved.tex:143-163 | 8 | **条件**: 仅 C4 重跑 |\n\n---\n\n## 执行顺序\n\n### Phase 1: 数据到手立即执行（~2h）\n1. 跑 n=500 analysis pipeline: median II + bootstrap CI + d_z within-importance + permutation test\n2. 生成 experiment_summary_table.json（n=500 版）\n3. 替换 T1, T2, T4, T5, T6 表格数据\n4. 替换全文 ~77 处数值引用（详见 n500_paper_patch_plan.md A2 清单）\n5. 重绘 F1-F4 图表\n\n### Phase 2: D059 合规修复（~1h，可与 Phase 1 并行）\n6. 修复 10 处 D059 违规（详见 n500_paper_patch_plan.md A3 清单）\n7. 重构 Table 3 (tab:llama-cross-arch) 列定义\n\n### Phase 3: 文本修改（~1h，依赖 Phase 1 结果）\n8. 评估 Qwen s015 CI → 决定是否触发 Qwen caveat\n9. 修复 C8 限定语（results.tex:79 一处）\n10. 插入 C5b future work 文本（discussion.tex + conclusion.tex）\n11. 插入 Qwen caveat（若触发）\n12. 插入 mid-phase null rate 说明（若 n=500 确认高 null rate）\n\n### Phase 4: 一致性验证（~30min）\n13. 全文 grep 所有 n=50 相关数字确认无遗漏\n14. 交叉验证 abstract/introduction/results/conclusion 数值一致性\n15. 确认 paper_framing.md 与论文最终文本同步\n16. 编译 PDF 检查无 LaTeX 错误\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_prep_paper_update_plan_20260514T220436",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/paper_n500_update_plan.md",
    "content": "# n=500 Paper Update Plan — Section-by-Section Diff Spec\n\n> 生成日期: 2026-05-14\n> 前置依赖: n500_paper_patch_plan.md（逐行数值替换清单）\n> 本文档补充: 每个 section 的 claim 强度评估 + 条件分支逻辑 + Qwen caveat + C8/C5b 专项\n\n---\n\n## 硬约束（Paper Worker 必读）\n\n| 约束 | 来源 | 含义 |\n|------|------|------|\n| 指标只用 **median + median bootstrap CI** | D054 | 禁止 mean，所有表格/正文/caption 一律 median |\n| d_z 只报 **within-importance**（low−high 配对） | D059 | imp-vs-rand d_z 和 random d_z 全部删除，改用 Wilcoxon p + median_diff |\n| LLaMA 为 **qualitative pattern**，不做定量跨架构比较 | D060 | 禁用 \"confirms\"，只用 \"suggests\"/\"provides partial support\"/\"directionally consistent\" |\n\n---\n\n## §Abstract (abstract.tex)\n\n### 当前 n=50 数据引用\n- L6: `50 MATH-500 problems`\n- L7: DeepSeek Δ `0.39→14.59`, d_z `0.44→0.80`, `p < 0.005`\n- L8: random `7/8 conditions`, Qwen s030 `p=0.012`, `d_z=-0.04`（**D059 违规**）\n- L9: crossover II 数值 `0.032 vs 0.818`, `7.196 vs 1.363`\n- L10: Qwen `d_z ≥ 0.55`, `ρ=1.0`, `p=0.043`; LLaMA `d_z (0.19→0.34)`（**D059 违规**）, `~1/40`\n\n### n=500 更新操作\n1. `50` → `500`\n2. 替换所有 DeepSeek/Qwen 数值为 n=500 结果\n3. **D059 修复**:\n   - L8: 删 `d_z=-0.04`，改为 `negligible median difference`\n   - L10: 删 LLaMA imp-vs-rand d_z 序列，改为 `Wilcoxon signed-rank test reaching significance at s=0.30 (p_Bonf=X)`\n4. LLaMA `~1/40` → 用 n=500 DeepSeek Δ 重算比值\n\n### Claim 强度调整逻辑\n- **若 n=500 CI 变窄且不跨零**: 可加强 → 删除 `(small)` 修饰词，直接报 d_z 值\n- **若 Qwen s015 CI 仍跨零**: 保持 `s ≥ 0.20` 下界，不加强\n- **若 Qwen s015 CI 排除零**: 可改为 `s ≥ 0.15`，abstract 同步\n- **若 random PASS/FAIL 比例变化**: 更新 `7/8` 为实际比例\n\n---\n\n## §1 Introduction (introduction.tex)\n\n### 当前 n=50 数据引用\n- L14: DeepSeek Δ `0.39→14.59`, d_z `0.44→0.80`, `p < 0.005`\n- L15: Qwen `d_z ≥ 0.55`, LLaMA `~1/40`\n- L16: `7/8 conditions non-significant`\n\n### n=500 更新操作\n1. L14: 与 abstract Q3/Q4/Q5 同步替换\n2. L15: 与 abstract Q9/Q11 同步\n3. L16: 与 abstract Q6 同步\n\n### Claim 强度调整逻辑\n- Introduction 措辞已较保守（`partially extends`），n=500 后无需改措辞方向\n- 若 n=500 效应量增大（d_z > 1.0），可在 `($d_z$: X → Y)` 后加 `(large)` 标注\n\n---\n\n## §2 Related Work (related_work.tex)\n\n### n=50 数据引用: **无**\n### n=500 更新操作: **无**（纯引用区分，不含实验数据）\n\n---\n\n## §3 Background (background.tex)\n\n### n=50 数据引用: **无**（只有公式定义）\n### n=500 更新操作: **无**\n\n---\n\n## §4 Experimental Setup (methodology.tex)\n\n### 当前 n=50 数据引用\n- L10: `50 problems stratified from MATH-500`\n- L18: `mean/median ratios up to 43:1`\n- L22: `All tests yield p_Bonf < 0.005`\n\n### n=500 更新操作\n1. L10: `50 problems stratified from MATH-500` → `500 problems from MATH-500`（删 \"stratified\"，500≈全集）\n2. L18: `43:1` → n=500 实际 mean/median ratio\n3. L22: 更新 p 值（预期 n=500 仍 <0.005，但需确认实际值）\n\n### Claim 强度: 无需调整（方法描述）\n\n---\n\n## §5 Results (results.tex)\n\n### 当前 n=50 数据引用（按子节）\n\n**§5.1 Strategy-Dependent Severity (L1-23)**\n- L8: Δ `0.39→14.59`, `37×` amplification; random `-0.02 to 1.54`\n- Table 1 (tab:aggregate-ii): 8 个数据单元格, caption `n=50`\n  - Importance: 0.39, 1.48, 7.16, 14.59\n  - Random: 0.01, -0.02, 0.54, 1.54\n\n**§5.2 Phase-Modulated Amplification (L26-60)**\n- L29: G `69×→274×`, II_high `0.006→0.053`, random G `0.9–1.7×`\n- Table 2 (tab:main-results): 24 个数据单元格, caption `50 problems`\n  - 完整 per-phase II breakdown（8行×3列 II + Δ + G）\n- Fig 1 (fig1_dose_response.pdf): G vs s 曲线, caption `69×→274×`\n\n**§5.3 Crossover (L63-67)**\n- L66: II 数值 `0.032 vs 0.818`, `7.196 vs 1.363`, `5.3× reversal`\n\n**§5.4 Cross-Model (L68-72)**\n- L71: Qwen Δ `0.04→2.94`, `~1/5`, `ρ=1.0`, `p=0.043`, `d_z=0.28 CI includes zero`, `d_z ≥ 0.55`\n\n**§5.5 Cross-Architecture (L74-98)**\n- L79: LLaMA d_z `0.19→0.26→0.29→0.34`（**D059 违规**）, `p=0.029`, `Δ=0.020 [0.002,0.043]`\n- L79: within-imp d_z `[1.00, 1.12]`（合规）, random d_z `[0.35, 0.45]`（**D059 违规**）\n- L81: `~40× smaller than DeepSeek`, `~7× smaller than Qwen`\n- Table 3 (tab:llama-cross-arch): d_z 列为 imp-vs-rand（**D059 违规，需重构**）\n\n**§5.6 Statistical Validation (L101-127)**\n- L104: permutation `p < 0.005`, `0.37→9.85`\n- L106: DeepSeek d_z `0.44→0.80`, Qwen d_z `0.28→1.02`, `0.89/1.02 vs 0.68/0.80`\n- Table 4 (tab:cohens-d): 16 个数据单元格（DS/QW × 4 sparsity × d_z + Δ[CI]）\n\n### n=500 更新操作\n\n**Tables 替换清单**:\n\n| Table | ID | 需替换单元格数 | 数据来源 |\n|-------|----|--------------|---------|\n| Table 1 | tab:aggregate-ii | 8 + caption n | n=500 experiment_summary_table.json median_diff |\n| Table 2 | tab:main-results | 24 + caption n | n=500 per-phase median II |\n| Table 3 | tab:llama-cross-arch | **重构**: d_z列→within-imp d_z 或删除 d_z 列改为 Wilcoxon p + Δ̃ | LLaMA 不重跑→数值不变但列定义改 |\n| Table 4 | tab:cohens-d | 16 | n=500 within-imp d_z + paired median diff + CI |\n\n**Figures 替换清单**:\n\n| Figure | 文件 | 数据来源 | 操作 |\n|--------|------|---------|------|\n| Fig 1 | fig1_dose_response.pdf | n=500 G values (imp+rand) | 重绘，caption G值同步 |\n\n**D059 修复** (§5.5):\n- L79 `paired d_z (0.19→...→0.34)` → `Wilcoxon signed-rank tests with median paired difference increasing from X to Y`\n- L79 `d_z ∈ [0.35, 0.45]` → `random eviction also shows a non-trivial phase gradient (Wilcoxon p < X)`\n- Table 3: d_z列→within-importance d_z (low−high)，caption 相应修改\n\n**C8 限定语修复** (§5.5):\n- L79 `The qualitative pattern replicates` → `The qualitative pattern is directionally consistent`（唯一需修改处，其余已合规）\n\n### Claim 强度调整逻辑\n\n**§5.4 Cross-Model — Qwen onset threshold 关键分支**:\n- **若 Qwen n=500 s015 d_z CI 排除零**: onset threshold 从 `s ≥ 0.20` 改为 `s ≥ 0.15`，L71 删 `CI includes zero`，改为 `d_z=X [CI_lo, CI_hi]`\n- **若 Qwen n=500 s015 CI 仍跨零**: 保持 `marginal at s=0.15, reliable at s ≥ 0.20`，在后续文字加 caveat: `the onset threshold for reliable detection appears model-dependent (DeepSeek: s ≥ 0.15; Qwen: s ≥ 0.20)`\n- **若 Qwen n=500 s020 CI 也跨零**: 升级 caveat 为 `s ≥ 0.25`，narrative 改为 `compound effect emerges above threshold sparsity (~s020-s025)`\n\n**§5.6 Statistical Validation — n=500 power 增益**:\n- n=500 预期 CI 收窄 ~√10 倍，d_z 估计更稳定\n- 若所有 CI lower bounds > 0: 可删除 `marginal` 相关修饰语\n- 若 permutation p 值从 `< 0.005` 变为 `< 0.001`: 更新但不改措辞\n\n---\n\n## §6 Analysis (analysis.tex)\n\n### 当前 n=50 数据引用\n- L4: Gini Δ `0.030–0.081` (DS), `0.010–0.020` (QW)\n- L6: entropy Δ𝓗 `[-0.047, -0.040]` (DS), `+0.045` (QW s025)\n\n### n=500 更新操作\n- **条件性**: C4 entropy 分析是否基于 n=500 重跑？\n  - **若重跑**: 替换所有 Gini/CV/entropy 数值\n  - **若不重跑**: 保留 n=50 数值，添加脚注 `Mechanism analysis based on a 30-problem subset; main results use n=500`\n\n### Claim 强度: 无需调整（机制分析，结论不变）\n\n---\n\n## §7 Discussion (discussion.tex)\n\n### 当前 n=50 数据引用\n- L5: G `69–274×`, crossover II `0.032 vs 0.818`, `7.196 vs 1.363`, `G ≈ 1`\n- L11: LLaMA `~40× smaller`, `~7× smaller`, `d_z ≥ 1.0`, `d_z ∈ [0.35, 0.45]`（**D059 违规**）\n\n### n=500 更新操作\n1. L5: 与 §5 同步更新所有数值\n2. **D059 修复**: L11 删 random d_z `[0.35, 0.45]`，改为定性描述 + Wilcoxon p\n3. L11: `~40×/~7×` 用 n=500 重算\n\n### 新增内容\n- **C5b pilot 结果** (B2 预写文本): 插入 L8 段末（`Extended discussion in Appendix~\\ref{app:extended-discussion}.` 之前）\n  - 内容: oracle recovery 18% < 30% gate, heuristic 32% CI 跨零, 作为 future work\n  - 这是 §8 future work 的铺垫\n\n### Claim 强度调整\n- 若 n=500 G 值变化幅度 ≤20%: `far exceeds a naive \"somewhat worse\" prediction` 保留\n- 若 G 值大幅缩小（如 274× → <100×）: 需调弱 `far exceeds` 措辞\n\n---\n\n## §8 Conclusion (conclusion.tex)\n\n### 当前 n=50 数据引用\n- L4: G `69×→274×`, d_z `0.44→0.80`, `7/8`, `d_z ≥ 0.55`, `~1/40`\n\n### n=500 更新操作\n1. 全部数值与 §5/Abstract 同步\n2. 若 n=500 效应增强: 可从 `strongly modulated` 加强为 `robustly modulated`（谨慎）\n\n### 新增内容\n- L5 之后追加一句指向 discussion C5b: `A preliminary pilot of phase-aware budget reallocation yielded 18\\% oracle recovery, below pre-registered thresholds, motivating joint phase--strategy optimization as future work (\\S\\ref{sec:discussion}).`\n\n### C5b §8 Future Work 准确性验证\n当前 conclusion.tex L5: `These findings motivate phase-aware sparsity allocation for reasoning model deployment.`\n- **问题**: 这句暗示 mitigation 是直接可行的，但 C5b pilot 已经 gate_failed\n- **修复**: 改为 `These findings motivate phase-aware sparsity allocation as a promising but non-trivial direction: a preliminary oracle pilot recovered only 18\\% of compound interaction, suggesting that effective mitigation requires joint optimization of budget allocation and strategy selection across phases.`\n\n---\n\n## Limitations (limitations.tex)\n\n### 当前 n=50 数据引用\n- L1: LLaMA `d_z ∈ [0.35, 0.45]`（隐含在定性描述中，无具体数字）\n- L11: `s ∈ {0.15, 0.20, 0.25, 0.30}`\n\n### n=500 更新操作\n- L1: 无具体数字需替换（定性描述），但审查 LLaMA 措辞是否合规 → 已合规（`partially extends`）\n- **新增**: L1 末尾加 `Cross-architecture validation is based on n=50; repeating at n=500 is future work.`（若 LLaMA 不重跑）\n\n### Claim 强度\n- 若 n=500 CI 全部排除零: 可删除 `$n{=}49$ paired problems` statistical scope 中关于小样本的讨论，或改为 `$n{=}X$ paired problems (primary models) and $n{=}49$ (cross-architecture)`\n- Statistical scope (L44-50): `n=49`/`n=46` → `n=X`/`n=Y`（n=500 有效问题数）\n\n---\n\n## Appendix\n\n### appendix.tex\n- L38: multiplicative null G `58–241×` → n=500 值\n\n### appendix_results.tex\n- L7: per-problem concordance `ρ=-0.11, p=0.926` → n=500 值\n- L10: random PASS/FAIL 计数 + `p=0.012`, `d_z=-0.04`（**D059 违规**）\n\n### appendix_moved.tex\n\n**Tables**:\n| Table | ID | 操作 |\n|-------|----|------|\n| tab:cross-model | L30-43 | 替换 8 单元格 |\n| tab:permutation | L70-85 | 替换 12 单元格 + caption n |\n| tab:discrimination-metrics-full | L103-123 | 条件性：C4 重跑则替换 |\n| tab:entropy-deltas | L143-163 | 条件性：C4 重跑则替换 |\n\n**Figures**:\n| Figure | 文件 | 操作 |\n|--------|------|------|\n| fig3_crossover.pdf | L15 | n=500 s=0.25 per-phase median → 重绘 |\n| fig4_bootstrap.pdf | L89 | n=500 paired d_z + permutation CI → 重绘 |\n| fig5_crossmodel.pdf | L47 | n=500 DS/QW paired median diffs → 重绘 |\n\n**文本**:\n- L11: crossover 全部数值（6 个数字 + 4 个比值）\n- L26: `Four of the 50 problems excluded` → `X of 500 problems excluded`\n- L53/56: per-problem concordance + random d_z（**D059 违规**）\n- L62/73: `n=49` → n=500 值\n- L68: CI lower bounds `0.19→0.69→1.66→6.70`\n\n### appendix_disc_analysis.tex\n- L4: random Gini 范围 `−0.031 to −0.073; Qwen: −0.019 to −0.045`（条件性）\n- L11: `II_high < 0.06`, `0.105`\n- L14: `7/8`, `p=0.012`, `d_z=-0.04`（**D059 违规**）\n- L45-50: statistical scope 全部 n 值 + 偏度统计 + permutation CI\n- L57: growth rate `3.8×→4.8×→2.0×`\n\n---\n\n## Qwen Caveat 专项\n\n### 触发条件\n**若 Qwen n=500 mid-phase (s015/s020) 仍不显著**:\n\n### 需加 caveat 的位置\n\n| # | 文件 | 位置 | 当前文本 | 需加的限定 |\n|---|------|------|---------|-----------|\n| QC1 | abstract.tex:10 | Qwen 结果句 | `$d_z \\geq 0.55$` | 加 `at $s \\geq 0.20$`（若 s015 仍不显著）|\n| QC2 | results.tex:71 | §5.4 末尾 | Qwen cross-model | 插入 B1 预写文本（imp-vs-rand 衰减 caveat）|\n| QC3 | appendix_moved.tex:28 | cross-model detail | `Qwen reproduces the monotonic severity gradient` | 加 `at $s \\geq 0.20$; the effect is marginal at $s{=}0.15$` |\n| QC4 | limitations.tex | 新增 | （无） | 加 `The onset sparsity for reliable phase modulation is model-dependent` |\n| QC5 | paper_framing.md | C2 预注册 | `叙事改为 'compound effect emerges above threshold sparsity (~s020)'` | 执行预注册承诺 |\n\n### 若 Qwen n=500 s015 显著\n- 删除所有 `marginal at s=0.15` 限定\n- onset threshold 统一为 `s ≥ 0.15`\n- abstract/introduction 可加强为 `replicates at all four sparsity levels`\n\n### Qwen imp-vs-rand 对比\nD058 记录 n=50 imp-vs-rand 全不显著。n=500 后:\n- **若仍全不显著**: 在 §5.4 加 B1 caveat（已预写），说明 within-importance gradient robust 但 strategy contrast attenuated\n- **若 s025/s030 显著**: 报告为 `strategy contrast reaches significance at higher sparsity`\n- **若全显著**: 删 caveat，报告为 `strategy contrast replicates on Qwen at all levels`\n\n---\n\n## C8 限定语专项\n\n### 当前 LLaMA partially_confirmed 措辞审查\n\n| # | 文件:行号 | 当前文本 | 状态 |\n|---|----------|---------|------|\n| 1 | abstract.tex:10 | `suggests cross-architecture generalization, though at...` | ✅ 合规 |\n| 2 | introduction.tex:15 | `partially extends to a distinct architecture` | ✅ 合规 |\n| 3 | results.tex:79 | `The qualitative pattern replicates` | ⚠️ 需改为 `is directionally consistent` |\n| 4 | results.tex:81 | `qualitatively consistent...substantially weaker` | ✅ 合规 |\n| 5 | discussion.tex:11 | `provides partial support for the qualitative pattern` | ✅ 合规 |\n| 6 | conclusion.tex:4 | `partially extends cross-architecture` | ✅ 合规 |\n| 7 | limitations.tex:2 | `partially extends the findings beyond` | ✅ 合规 |\n| 8 | appendix_disc_analysis.tex:33 | `provides partial support` | ✅ 合规 |\n\n**唯一需修改**: #3 results.tex:79\n\n### n=500 后是否需要调整 C8\n- LLaMA 不重跑 n=500（未在 ROADMAP 中），所以 C8 数据不变\n- n=500 改变的是 DeepSeek/Qwen 的 Δ 绝对值 → 重算 LLaMA/DS 和 LLaMA/QW 的比值\n  - 当前: `~40× smaller` (DS), `~7× smaller` (QW)\n  - n=500 后: 分母变化 → 比值可能变化\n  - **操作**: 等 n=500 DS/QW Δ 出来后重算，更新 abstract/results/discussion/conclusion 中的倍数\n\n---\n\n## C5b §8 Future Work 专项\n\n### 当前状态\n- C5b: `future_work`（D056: oracle recovery 18% < 30% gate, heuristic 32% CI 跨零）\n- 论文**无独立 Future Work section**\n\n### 当前提及位置\n| # | 文件 | 内容 | 准确性 |\n|---|------|------|--------|\n| 1 | discussion.tex:8 | `A phase-aware compression budget...could mitigate...` | ⚠️ 过于乐观——未提及 pilot 失败 |\n| 2 | conclusion.tex:5 | `These findings motivate phase-aware sparsity allocation...` | ⚠️ 同上 |\n\n### 需要的修改\n1. **discussion.tex**: L8 段末插入 B2 预写文本（pilot 结果: oracle 18% < 30% gate）\n2. **conclusion.tex**: L5 改写，加入 pilot 限定（见上文 §8 Conclusion 部分）\n3. **验证 paper_framing.md 中 C5b 描述**: `oracle recovery 18%, heuristic 32% CI 跨零, 方向正确但效应量不足` → 与论文叙事一致 ✅\n4. **Heuristic > Oracle 悖论**: paper_framing.md 提到值得在论文中提及 → 在 discussion B2 文本中加一句: `Notably, the heuristic boundary (token position ratio) yielded higher recovery (32\\%) than the oracle (18\\%), suggesting that optimal phase granularity for mitigation may differ from that for characterization---an open question for future work.`\n\n---\n\n## Figures 完整重绘清单\n\n| # | 文件 | 引用位置 | n=500 数据源 | 操作 |\n|---|------|---------|-------------|------|\n| F1 | fig1_dose_response.pdf | results.tex:57 | n=500 G values from experiment_summary_table.json | 重绘: G vs s, imp solid + rand dashed, 95% bootstrap CI |\n| F2 | fig3_crossover.pdf | appendix_moved.tex:15 | n=500 s=0.25 per-phase median II | 重绘: grouped bar, 3 phases × 2 strategies |\n| F3 | fig4_bootstrap.pdf | appendix_moved.tex:89 | n=500 within-imp d_z + permutation CI | 重绘: forest plot, 4 sparsity levels |\n| F4 | fig5_crossmodel.pdf | appendix_moved.tex:47 | n=500 DS/QW paired median Δ | 重绘: line plot, DS solid + QW dashed, symlog Y |\n\n生成方式: 服务器端 `/root/autodl-tmp/pacs/analysis/generate_paper_figures.py`（draw-paper-figure skill）\n样式: serif, 9pt, hidden top/right spines, 300 dpi\n\n---\n\n## Tables 完整替换清单\n\n| # | Table ID | 文件:行号 | 单元格数 | 依赖 |\n|---|----------|----------|---------|------|\n| T1 | tab:aggregate-ii | results.tex:10-23 | 8 + caption | n=500 DS imp+rand Δ |\n| T2 | tab:main-results | results.tex:31-53 | 24 + caption | n=500 DS per-phase II |\n| T3 | tab:llama-cross-arch | results.tex:83-98 | **重构** | D059: 列定义改为 within-imp d_z；数值不变（LLaMA 不重跑） |\n| T4 | tab:cohens-d | results.tex:108-124 | 16 | n=500 DS/QW within-imp d_z + Δ[CI] |\n| T5 | tab:cross-model | appendix_moved.tex:30-43 | 8 | n=500 DS/QW Δ |\n| T6 | tab:permutation | appendix_moved.tex:70-85 | 12 + caption | n=500 permutation Δ + CI + p |\n| T7 | tab:discrimination-metrics-full | appendix_moved.tex:103-123 | 16 | **条件**: 仅 C4 重跑 |\n| T8 | tab:entropy-deltas | appendix_moved.tex:143-163 | 8 | **条件**: 仅 C4 重跑 |\n\n---\n\n## 执行顺序\n\n### Phase 1: 数据到手立即执行（~2h）\n1. 跑 n=500 analysis pipeline: median II + bootstrap CI + d_z within-importance + permutation test\n2. 生成 experiment_summary_table.json（n=500 版）\n3. 替换 T1, T2, T4, T5, T6 表格数据\n4. 替换全文 ~77 处数值引用（详见 n500_paper_patch_plan.md A2 清单）\n5. 重绘 F1-F4 图表\n\n### Phase 2: D059 合规修复（~1h，可与 Phase 1 并行）\n6. 修复 10 处 D059 违规（详见 n500_paper_patch_plan.md A3 清单）\n7. 重构 Table 3 (tab:llama-cross-arch) 列定义\n\n### Phase 3: 文本修改（~1h，依赖 Phase 1 结果）\n8. 评估 Qwen s015 CI → 决定是否触发 Qwen caveat\n9. 修复 C8 限定语（results.tex:79 一处）\n10. 插入 C5b future work 文本（discussion.tex + conclusion.tex）\n11. 插入 Qwen caveat（若触发）\n12. 插入 mid-phase null rate 说明（若 n=500 确认高 null rate）\n\n### Phase 4: 一致性验证（~30min）\n13. 全文 grep 所有 n=50 相关数字确认无遗漏\n14. 交叉验证 abstract/introduction/results/conclusion 数值一致性\n15. 确认 paper_framing.md 与论文最终文本同步\n16. 编译 PDF 检查无 LaTeX 错误\n"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-14T22:08:29.847560+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/paper_n500_update_plan.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_prep_paper_update_plan_20260514T220436",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-14T22:08:29.847722+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "paper_n500_update_plan",
  "type": "report",
  "description": "Section-by-section diff plan for updating the paper from n=50 to n=500 data, with claim strength adjustment logic, Qwen caveat triggers, C8 限定语 audit, C5b future work spec, and prioritized execution checklist",
  "project": "phase-gated-compound-sparse",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/paper_n500_update_plan.md",
  "tags": "['paper', 'n500', 'update-plan', 'diff-spec']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_prep_paper_update_plan_20260514T220436",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "paper_n500_update_plan",
    "type": "report",
    "description": "Section-by-section diff plan for updating the paper from n=50 to n=500 data, with claim strength adjustment logic, Qwen caveat triggers, C8 限定语 audit, C5b future work spec, and prioritized execution checklist",
    "project": "phase-gated-compound-sparse",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/paper_n500_update_plan.md",
    "tags": "['paper', 'n500', 'update-plan', 'diff-spec']"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-14T22:08:29.847988+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260514_479d6c\", \"name\": \"paper_n500_update_plan\", \"type\": \"report\", \"description\": \"Section-by-section diff plan for updating the paper from n=50 to n=500 data, with claim strength adjustment logic, Qwen caveat triggers, C8 限定语 audit, C5b future work spec, and prioritized execution checklist\", \"path\": \"projects/phase-gated-compound-sparse/artifacts/_project/report/paper_n500_update_plan.md\", \"url\": null, \"project\": \"phase-gated-compound-sparse\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-14T22:08:19.991912+00:00\", \"tags\": [\"paper\", \"n500\", \"update-plan\", \"diff-spec\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_prep_paper_update_plan_20260514T220436",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 53 · 2026-05-14T22:08:29.848177+00:00_

计划已写入并注册。核心内容：

**覆盖范围**: §1-§8 + Abstract + Appendix，共识别 ~77 处数值替换、10 处 D059 违规修复、4 张图重绘、8 张表更新。

**关键决策点**:
- **Qwen s015 CI**: 若排除零→onset 改为 `s ≥ 0.15`；若仍跨零→保持 `s ≥ 0.20` + 触发 5 处 caveat
- **C8**: 仅 results.tex:79 一处需从 `replicates` 改为 `is directionally consistent`；LLaMA/DS 倍数需用 n=500 DS Δ 重算
- **C5b**: discussion.tex 和 conclusion.tex 均过于乐观（未提 pilot 失败），需插入 oracle 18% < 30% gate 结果 + heuristic > oracle 悖论
- **Table 3 重构**: imp-vs-rand d_z 列违反 D059，需改为 within-imp d_z 或 Wilcoxon p + median_diff

本计划与已有 `n500_paper_patch_plan.md`（逐行替换清单）互补使用。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_prep_paper_update_plan_20260514T220436"
}
```

</details>

---
