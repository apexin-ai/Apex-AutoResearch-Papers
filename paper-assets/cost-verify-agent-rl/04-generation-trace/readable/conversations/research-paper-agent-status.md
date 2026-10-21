# research paper agent status

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 17
- **Recorded user turns:** 0
- **Tool calls:** 8
- **Original source:** `logs/chats/worker_research_paper_agent_status_20260520T040003.jsonl`
- **Structured JSON:** [`3d808ab5ef8d740fa978.json`](../../sessions/3d/3d808ab5ef8d740fa978.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

17 recorded events

### Tool call

_source line 1 · 2026-05-20T04:01:03.107421+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__list_workers,mcp__agent-ml-research__read_registry",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_paper_agent_status_20260520T040003",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__list_workers,mcp__agent-ml-research__read_registry",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-20T04:01:03.107923+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper_agent_status_20260520T040003",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-20T04:01:03.108216+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "cost-verify-agent-rl",
  "file": "writing_plan.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_paper_agent_status_20260520T040003",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "cost-verify-agent-rl",
    "file": "writing_plan.yaml"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-20T04:01:03.108548+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/writing_plan.yaml\", \"content\": \"# Writing Plan — Sign Misattribution in Step-Independent Agent RL\\n# Updated: 2026-05-18 (D073 narrative pivot)\\n# Scope: Method + Related Work + Experimental Setup (Results/Abstract/Conclusion deferred)\\n\\nmeta:\\n  venue: \\\"NeurIPS 2026 / ICLR 2026 (TBD)\\\"\\n  track: main\\n  template: null  # TODO: download official template\\n  template_note: \\\"Template pending. Will fetch before final formatting.\\\"\\n  page_limit: 9\\n  deadline: null  # TBD by Director\\n  core_claim: >\\n    Step-independent GRPO catastrophically fails in multi-turn agent RL due to\\n    dual mechanism failure (policy information loss + advantage sign misattribution).\\n    The failure manifests as three qualitatively distinct training dynamics:\\n    monotonic collapse, oscillation-then-degradation, and stable learning.\\n    Episode-level GRPO eliminates both mechanisms.\\n  created_at: \\\"2026-05-18T12:00:00Z\\\"\\n  narrative_version: \\\"D073\\\"\\n  narrative_strategy: >\\n    Training dynamics contrast (3 modes) as core argument, NOT quantitative\\n    percentage decomposition. Checkpoint-dependent numbers are fragile;\\n    qualitative training regime differences are robust.\\n\\npaper_outline:\\n  - section: abstract\\n    word_budget: 220\\n    status: DEFERRED\\n    core_bullets:\\n      - \\\"Problem: step-independent GRPO silently fails in multi-turn agent tasks\\\"\\n      - \\\"Diagnosis: dual mechanism (information loss + sign misattribution)\\\"\\n      - \\\"Evidence: 3 training regimes + factorial mechanism separation\\\"\\n      - \\\"Fix: episode-level GRPO\\\"\\n    dependencies: [experiments, method]\\n\\n  - section: introduction\\n    word_budget: 1400\\n    status: EXISTS (needs D073 rewrite later)\\n    core_bullets:\\n      - \\\"Hook: community default (step-independent) produces 3 fail
…[truncated 11365 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper_agent_status_20260520T040003",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-20T04:01:03.108749+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "cost-verify-agent-rl",
  "file": "paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_paper_agent_status_20260520T040003",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "cost-verify-agent-rl",
    "file": "paper_framing.md"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-20T04:01:03.108995+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/paper_framing.md\", \"content\": \"# Paper Framing — Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Fix\\n\\n> Plan A 转正 (2026-05-17) | Diagnostic + analysis paper. Selective verification 降级为 future work.\\n\\n## Core Insight\\n\\nLLM agent 社区默认的 step-independent training 在长 horizon 多轮任务中表现出严重的训练不稳定性和脆弱性（seed 间表现从崩溃至 0% 到极度延迟学习不等）。根因是**双机制失效**（D073：两个机制有定性不同的破坏效果——sign misattribution 破坏训练稳定性使学习极不可靠，information loss 杀死泛化能力，两者必须同时解决）：\\n\\n1. **Policy Information Loss**: 短窗口（h 步）的 policy 无法学习跨步策略（如 \\\"先探索 drawer 再去 countertop\\\"）\\n2. **Advantage Sign Misattribution**: step_independent 中，per-window advantage 的符号由 group normalization + episode outcome 共同决定，而非 task-relevant action quality：\\n   - **Type C evidence (D063)**: 失败 episode 中零 penalty 的 window（action 全 valid 但 task 失败）→ step_return=0 高于被 penalty 拉负的 group mean → 获得**正** advantage 被强化。直接证据：32/800 windows (4%)\\n   - 模型学会避免 format errors（action_is_valid ↑）但不学 task success — 与 exp013f gaming 观察一致\\n   - GRPO group normalization 使 advantage 区分 format quality（有无 penalty），不区分 task progress\\n   - 附加：γ^k magnitude decay 使早期 window 信号更弱（γ^24 ≈ 29%）\\n   - **实证确认 (tab3)**：per-sample advantage sign accuracy = 52.07% (n=3000, ≈random)；GRPO group majority = 81.25% vs 理论 79.5%（高度吻合）。Sign misattribution 从理论预测升级为实证确认\\n   - **理论精度注意**：Proposition 2 的纯二值假设 (R ∈ {0, r+}) 需要扩展为包含 penalty 影响的版本。\\\"80.9% wrong sign\\\" 基于 binary assumption；实际 penalty 创造连续分布，misattribution 机制更复杂但方向不变\\n\\nEpisode-level training 同时解决两者：policy 看全历史（解决 1），整条 trajectory 作为一个 GRPO 样本，所有 tokens 共享同一 advantage — 虽然仍是 episode-level credit（非 per-token），但消除了 window 间的 sign misattribution，因为不再需要将 episode reward 分配到独立优化的子窗口（解决 2）。\\n\\n**8B Scale Verification (D083-D085)**：Qwen3-8B (8.2B params) 验证双机制 scale-invariance：\\n- **Information loss 量化 (D087, deterministic eval 完成)**：同一 8
…[truncated 10690 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper_agent_status_20260520T040003",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-20T04:01:03.109175+00:00_

called mcp__agent-ml-research__list_workers

<details open><summary>🔧 Tool call — mcp__agent-ml-research__list_workers</summary>

```json
{
  "project": "cost-verify-agent-rl",
  "limit": "20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_paper_agent_status_20260520T040003",
  "tool": "mcp__agent-ml-research__list_workers",
  "tool_args": {
    "project": "cost-verify-agent-rl",
    "limit": "20"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-20T04:01:03.109409+00:00_

{"result":"{\"success\": true, \"data\": {\"workers\": [{\"worker_id\": \"worker_code_d098_fsdp2_full_audit_20260519T185853\", \"task_type\": \"code:d098_fsdp2_full_audit\", \"project\": \"cost-verify-agent-rl\", \"status\": \"done\", \"started_at\": \"2026-05-19T18:58:53.262727+00:00\", \"ended_at\": \"2026-05-19T19:07:41.821639+00:00\"}, {\"worker_id\": \"worker_monitor_v9c_status_check_20260519T201126\", \"task_type\": \"monitor:v9c_status_check\", \"project\": \"cost-verify-agent-rl\", \"status\": \"done\", \"started_at\": \"2026-05-19T20:11:26.218966+00:00\", \"ended_at\": \"2026-05-19T20:12:38.511166+00:00\"}, {\"worker_id\": \"worker_monitor_scienceworld_eval_v2_progress_20260519T201136\", \"task_type\": \"monitor:scienceworld_eval_v2_progress\", \"project\": \"cost-verify-agent-rl\", \"status\": \"done\", \"started_at\": \"2026-05-19T20:11:36.212084+00:00\", \"ended_at\": \"2026-05-19T20:13:08.678241+00:00\"}, {\"worker_id\": \"worker_research_scienceworld_grpo_feasibility_20260519T201151\", \"task_type\": \"research:scienceworld_grpo_feasibility\", \"project\": \"cost-verify-agent-rl\", \"status\": \"done\", \"started_at\": \"2026-05-19T20:11:51.614055+00:00\", \"ended_at\": \"2026-05-19T20:14:08.893649+00:00\"}, {\"worker_id\": \"worker_code_scienceworld_grpo_config_20260519T201551\", \"task_type\": \"code:scienceworld_grpo_config\", \"project\": \"cost-verify-agent-rl\", \"status\": \"done\", \"started_at\": \"2026-05-19T20:15:51.985251+00:00\", \"ended_at\": \"2026-05-19T20:20:13.368484+00:00\"}, {\"worker_id\": \"worker_monitor_v9c_status_urgent_20260519T230842\", \"task_type\": \"monitor:v9c_status_urgent\", \"project\": \"cost-verify-agent-rl\", \"status\": \"done\", \"started_at\": \"2026-05-19T23:08:43.029384+00:00\", \"ended_at\": \"2026-05-19T23:10:06.435904+00:00\"}, {\"worker_id\": \"worker_monitor_eval_v2_progress_urgent_20260519T230854\", \"task_type\": \"monitor:eval_v2_progress_urgent\", \"project\": \"cost-verify-agent-rl\", \"status\": \"d
…[truncated 3872 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper_agent_status_20260520T040003",
  "tool": "mcp__agent-ml-research__list_workers",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-20T04:01:03.109627+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/artifacts/**",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_paper_agent_status_20260520T040003",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/artifacts/**",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-20T04:01:03.109806+00:00_

artifacts/env_setup_report.md
artifacts/alfworld_dryrun_report.md
artifacts/exp_001/intermediate/exp_001_config_summary.txt
artifacts/biavr/action_canonicalize.py
artifacts/biavr/reward.py
artifacts/biavr/envs_biavr_entry.yaml
artifacts/biavr/tests/__init__.py
artifacts/biavr/REPORT.md
artifacts/exp003/report/exp003_launch_report.md
artifacts/exp003_status_check.md
artifacts/exp003_invalid_action_diagnosis.md
artifacts/exp003/report/exp003_invalid_action_diagnosis.md
artifacts/sft_warmup_plan.md
artifacts/disk_cleanup_report.md
artifacts/exp007/report/exp007_analysis.md
artifacts/exp007/report/exp007_analysis_475afa.md
artifacts/exp008_sft/intermediate/convert_sft_data_info.txt
artifacts/exp008_sft/intermediate/sft_train_info.txt
artifacts/exp009/report/exp009_analysis.md
artifacts/exp009/report/exp009_analysis_955f15.md
artifacts/_project/report/phase_b_literature_survey.md
artifacts/phase_b_literature_survey.md
artifacts/_project/report/phase_b_readiness_check.md
artifacts/phase_b_readiness_check.md
artifacts/exp010_reward_analysis.md
artifacts/exp010/report/exp010_reward_analysis.md
artifacts/phase_b_prep_checklist.md
artifacts/exp013f_training_metrics.md
artifacts/reward_shaping_literature.md
artifacts/expert_trajectory_plan.md
artifacts/_project/report/literature_rl_alternatives.md
artifacts/literature_rl_alternatives.md
artifacts/_project/report/grpo_alternatives_survey.md
artifacts/grpo_alternatives_survey.md
artifacts/exp017_status_check.md
artifacts/exp021_ragen_sft_v4/data/v4_data_conversion_notes.md
artifacts/exp021_ragen_sft_v4/report/exp021_analysis_report.md
artifacts/exp021/report/exp021_val_report.md
artifacts/_project/report/verl_agent_migration_plan.md
artifacts/verl_agent_migration_plan.md
artifacts/_project/report/inference_diff_diagnosis.md
artifacts/inference_diff_diagnosis.md
artifacts/exp023c_grpo_serial/report/grpo_val_degradation_diagnosis.md
artifacts/exp024_success_gated/intermediate/exp024_launch_summary.txt
artifacts/exp025_training_scr
…[truncated 2605 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper_agent_status_20260520T040003",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-20T04:01:03.109955+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/paper/**",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_paper_agent_status_20260520T040003",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/paper/**",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-20T04:01:03.110118+00:00_

artifacts/_project/paper/method_draft.md
artifacts/_project/paper/theoretical_analysis.tex
artifacts/_project/paper/introduction.tex
artifacts/_project/paper/related_work.tex
artifacts/_project/paper/references.bib
docs/paper/citation_verification_report.md
artifacts/_project/paper/experiments_aa43d8.tex
artifacts/_project/paper/experiments.tex
artifacts/_project/paper/discussion.tex
artifacts/_project/paper/conclusion.tex
docs/paper/discussion.tex
docs/paper/theoretical_analysis.tex
docs/paper/introduction.tex
docs/paper/conclusion.tex
docs/paper/method.tex
docs/paper/related_work.tex
docs/paper/experiments.tex
docs/paper/references.bib
figures/paper/gen_fig6_training_curves.py
figures/paper/fig6_training_curves.pdf
figures/paper/fig6_training_curves.png
figures/paper/gen_fig_theoretical_sign_probability.py
figures/paper/fig_theoretical_sign_probability.pdf
figures/paper/fig_theoretical_sign_probability.png

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper_agent_status_20260520T040003",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-20T04:01:03.110313+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/_project/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_paper_agent_status_20260520T040003",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/_project/paper/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-20T04:01:03.110961+00:00_

1	\newcommand{\placeholder}[1]{\textcolor{red}{[#1]}}
2	
3	\section{Experiments}
4	\label{sec:experiments}
5	
6	We design experiments to answer three questions. First, does step-independent training collapse as predicted by our dual mechanism analysis, and does episode-level training avoid this collapse? Second, how does the window size $h$ modulate the severity of failure, and is there a credit assignment cliff below some critical threshold? Third, can we directly measure advantage sign misattribution during training to validate the theoretical predictions of Section~\ref{sec:m2_sign_misattribution}?
7	
8	\subsection{Experimental Setup}
9	\label{sec:experimental_setup}
10	
11	\paragraph{Environment.}
12	We evaluate on ALFWorld~\cite{shridhar2021alfworld}, a text-based household environment where an agent interacts with a simulated kitchen, bedroom, and living room through natural language commands. % TODO: add shridhar2021alfworld to .bib
13	ALFWorld provides six task types (pick, clean, heat, cool, examine, pick two) that require sequential reasoning over multiple interaction steps. The agent issues text commands (e.g., ``go to countertop 1'', ``take knife 2 from drawer 3'') and receives textual observations describing the environment state. Episodes terminate after task completion or a maximum of 50 interaction steps. The reward is binary: $R = 1$ for successful task completion and $R = 0$ for failure. This binary reward structure makes ALFWorld a particularly challenging testbed for credit assignment: the only learning signal arrives at episode termination, and intermediate steps receive no direct feedback.
14	
15	ALFWorld is well-suited for studying the step-independent failure because its tasks exhibit strong sequential dependencies. A typical task requires the agent to locate an object (steps 1--5), pick it up (step 6), navigate to a target receptacle (steps 7--10), and place the object (step 11). With step-independent windowing at $h = 2$, the window contain
…[truncated 14854 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper_agent_status_20260520T040003",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-20T04:01:03.111137+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "results|Results|RESULTS",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/_project/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_paper_agent_status_20260520T040003",
  "tool": "Grep",
  "tool_args": {
    "pattern": "results|Results|RESULTS",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/_project/paper",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-20T04:01:03.111511+00:00_

artifacts/_project/paper/theoretical_analysis.tex:60:\textbf{6. Absence of negative results.} When step-independent training fails, practitioners attribute the failure to insufficient hyperparameter tuning or the inherent difficulty of sparse rewards. Without published analyses that isolate the credit assignment mechanism as the root cause, the community cannot distinguish between ``this problem is hard'' and ``this training paradigm is broken for this class of problems.''
artifacts/_project/paper/experiments.tex:33:[Omitted long matching line]
artifacts/_project/paper/experiments.tex:52:\subsection{Results}
artifacts/_project/paper/experiments.tex:53:\label{sec:results}
artifacts/_project/paper/experiments.tex:56:\label{sec:results_main}
artifacts/_project/paper/experiments.tex:60:\placeholder{tab1\_main\_results: Episode-level vs step-independent comparison. Columns: Method, $h$-value, Val Success (\%), Action Valid (\%), Pass@8. Multi-seed mean$\pm$std from plan\_003.}
artifacts/_project/paper/experiments.tex:69:\label{sec:results_hsweep}
artifacts/_project/paper/experiments.tex:71:\placeholder{tab2\_h\_sweep: $h$-sweep ablation results. Columns: $h$, Seed 1/2/3, Mean$\pm$Std, Collapse Step (first step where val success $= 0$). Rows: $h \in \{2, 5, 10, 20, \text{full}\}$, 3 seeds per $h$.}
artifacts/_project/paper/experiments.tex:82:\label{sec:results_dense}
artifacts/_project/paper/experiments.tex:121:[Omitted long matching line]
artifacts/_project/paper/discussion.tex:38:[Omitted long matching line]
artifacts/_project/paper/experiments_aa43d8.tex:33:[Omitted long matching line]
artifacts/_project/paper/experiments_aa43d8.tex:52:\subsection{Results}
artifacts/_project/paper/experiments_aa43d8.tex:53:\label{sec:results}
artifacts/_project/paper/experiments_aa43d8.tex:56:\label{sec:results_main}
artifacts/_project/paper/experiments_aa43d8.tex:60:\placeholder{tab1\_main\_results: Episode-level vs step-independent comparison. Columns: Method, $h$-value, Val Success 
…[truncated 646 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper_agent_status_20260520T040003",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-20T04:01:03.111873+00:00_

## 汇报

### Results section 产出状态：已有初稿

文件路径：`artifacts/_project/paper/experiments.tex`（第 52-122 行）

已写内容：
- **§5.2.1 Episode-Level vs Step-Independent**：核心对比已写完（episode-level 28.125% vs step-independent h=2 崩溃至 0%），含 two-phase collapse 分析
- **§5.2.2 Window-Size Ablation**：文字框架已写，但缺多 seed 数据，含 placeholder
- **§5.2.3 Dense Reward Baseline**：exp013f 分析已完成（action validity 97.5% but success 0%）
- **§5.3 Sign Misattribution Verification**：方法论已写，tab3 数据 placeholder

未完成项（`\placeholder` 标记）：
| Placeholder | 状态 |
|---|---|
| `tab1_main_results` | 缺多 seed 数据 |
| `fig6_training_curves` | 数据已有，图未生成 |
| `tab2_h_sweep` | 缺多 seed 数据 |
| `fig5_h_sweep_curve` | blocked on h=5/10/20 多 seed |
| `tab3_mechanism_verification` | 数据已有（seed2 adv_log），未填入 |
| GAE baseline / Selective verification | 实验未完成 |

### Paper Agent Worker 状态

当前无 paper/writing 类 worker 在运行。两个 running worker 都是 monitor/research 类型，与论文写作无关。

### 结论

Results section **已有初稿框架和部分内容**，不需要重新派单写全文。需要的是：
1. **填充 placeholder**：将已有实验数据（tab3 sign verification、fig6 training curves）填入
2. **补充缺失内容**：8B scale verification 结果（D085/D087/D088）、factorial experiment 结果（Cell A/B/C 对比）、OOD 134-task 数据——这些在 paper_framing.md 中有详细数据但未写入 tex
3. **生成图表**：fig6_training_curves 的生成脚本已存在（`figures/paper/gen_fig6_training_curves.py`）

建议派单方向：**Results section 补全 worker**，重点是将 paper_framing.md 中已确认的实验数据写入 experiments.tex 的 placeholder 位置，而非从头写。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_paper_agent_status_20260520T040003"
}
```

</details>

---
