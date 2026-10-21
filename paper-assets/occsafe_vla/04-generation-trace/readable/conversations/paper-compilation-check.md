# paper compilation check

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 51
- **Recorded user turns:** 0
- **Tool calls:** 25
- **Original source:** `logs/chats/worker_paper_compilation_check_20260528T062030.jsonl`
- **Structured JSON:** [`ba87e9e626c020a12945.json`](../../sessions/ba/ba87e9e626c020a12945.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

51 recorded events

### Tool call

_source line 1 · 2026-05-28T06:22:43.719266+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__detect_image",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_compilation_check_20260528T062030",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__detect_image",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-28T06:22:43.719595+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_compilation_check_20260528T062030",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-28T06:22:43.719784+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_compilation_check_20260528T062030",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-28T06:22:43.719930+00:00_

artifacts/_project/paper/related_work.tex
docs/paper/references.tex
artifacts/dream_reports/dream_20260523T025401/best/paper.tex
artifacts/dream_reports/dream_20260523T025401/median/paper.tex
artifacts/dream_reports/dream_20260523T034027/best/paper.tex
artifacts/dream_reports/dream_20260523T034027/median/paper.tex
artifacts/dream_reports/dream_20260523T034027/worst/paper.tex
docs/paper/experiments_old.tex
docs/drafts/scenario_variants.tex
docs/paper/related_work.tex
docs/paper/method.tex
docs/paper/discussion.tex
docs/paper/results.tex
docs/paper/conclusion.tex
docs/paper/main.tex
docs/paper/introduction.tex
docs/paper/appendix.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_compilation_check_20260528T062030",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-28T06:22:43.720059+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_compilation_check_20260528T062030",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.bib",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-28T06:22:43.720179+00:00_

docs/paper/references.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_compilation_check_20260528T062030",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-28T06:22:43.720318+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-34685",
  "command": "find /root/occsafe_vla -name \"*.tex\" -o -name \"*.bib\" -o -name \"*.pdf\" 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_compilation_check_20260528T062030",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-34685",
    "command": "find /root/occsafe_vla -name \"*.tex\" -o -name \"*.bib\" -o -name \"*.pdf\" 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-28T06:22:43.720439+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_compilation_check_20260528T062030",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-28T06:22:43.720555+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "occsafe_vla",
  "file": "paper_framing.md",
  "max_chars": "12000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_compilation_check_20260528T062030",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "occsafe_vla",
    "file": "paper_framing.md",
    "max_chars": "12000"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-28T06:22:43.720866+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/paper_framing.md\", \"content\": \"# OccSafe-VLA — Paper Framing\\n\\n> 维护者: Director | 最后更新: 2026-05-27 22:00 UTC | 状态: Draft — **D074 Dual Main Effects** — v2 factorial: gradient flow 主效应 (Δ=-4.6pp, d=0.60) + normalization 主效应 (LN>BN, Δ=+5.6pp, d≈1.03); ANOVA interaction ≈ 0 (不显著); BN+Grad ON 是唯一 < Vanilla 的配置。Cell 1 n=3, Cell 2 n=3 v2, Cell 3 n=4, Cell 4 n=1 v2 (expanding)。CoRL 2026 target (Paper May 29)\\n>\\n> ⚠️ **D074 Dual Main Effects Transition (2026-05-27)**: Reviewer 审查发现 ANOVA 交互项 contrast ≈ 0 (+0.007pp)，数学上不可能显著。\\\"ordinal interaction\\\" framing 改为 \\\"dual main effects + practical threshold crossing\\\"。新增 normalization 主效应 (d≈1.03) 作为 secondary claim。详见 D074。\\n\\n## Architecture Facts (from code, verified)\\n- **Occ head input**: DINOv2(1024) + SigLIP(1152) 拼接 = 2176d（非仅 DINOv2）\\n- **Occ head**: Linear(2176→256) → reshape(B,256,16,16) → ConvTranspose2d×2 上采样(16→32→64) → Conv2d(64→1)。BatchNorm2d + GELU。参数量 1.2M。\\n- **FocalLoss**: α=0.25, γ=2.0\\n- **occ_loss_weight**: λ=0.01, 指数衰减 w(t)=0.01×exp(-t/50000)\\n- **LR**: 5e-4 恒定（MultiStepLR milestone=100K > max_steps，从未触发）\\n- **LoRA**: rank=32, alpha=16, dropout=0.0\\n- **GPU**: 4× RTX PRO 6000 98GB per server\\n- **训练时间**: ~12.9h/run @ 1.08 it/s\\n\\n### 叙事含义\\n- **双编码器梯度流**: Occ head 接收 DINOv2+SigLIP 拼接特征，occupancy supervision 同时影响两个编码器。\\n  比\\\"仅改善 DINOv2\\\"更强 — 同时改善语义(SigLIP)和空间(DINOv2)编码器的 3D 感知。\\n- **极轻量**: occ_head 仅 1.2M params = 全模型 7.65B 的 0.016%，强化 \\\"lightweight auxiliary\\\" 叙事\\n- **occ_loss 指数衰减**: w(t)=0.01×exp(-t/50000) → 训练后期 occ 监督逐渐\\\"放手\\\"让 action loss 主导，\\n  可论证为\\\"先学空间结构，再精化动作\\\"的课程学习效果\\n- **LoRA alpha=16 < rank=32**: 有效 scaling factor = alpha/rank = 0.5，比常见的 1.0 更保守\\n\\n### DepthHead (新增, 2026-05-22)\\n- **Depth head**: Linear(2176→256) → ConvTranspose2d×2 (256→128→64, kernel=4, stride=2) → ReLU（无 sigmoid）\\n- **SmoothL1Loss**, depth_loss_weight=0.
…[truncated 10947 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_compilation_check_20260528T062030",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-28T06:22:43.721062+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_compilation_check_20260528T062030",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/main.tex"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-28T06:22:43.721223+00:00_

1	% OccSafe-VLA: Occupancy-Aware Safety for Vision-Language-Action Models
2	% Target: CoRL 2026
3	\documentclass{article}
4	
5	\usepackage[dvipsnames]{xcolor}
6	\usepackage{corl_2026}
7	
8	\usepackage{graphicx}
9	\usepackage{amsmath,amssymb}
10	\usepackage{booktabs}
11	\usepackage{enumitem}
12	\usepackage{subcaption}
13	\usepackage{placeins}
14	
15	\title{Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer?\\ An Empirical Investigation}
16	
17	\author{
18	Anonymous Author(s)
19	}
20	
21	\begin{document}
22	\maketitle
23	
24	\begin{abstract}
25	Fine-tuned Vision-Language-Action (VLA) models can achieve high task success yet remain behaviorally unsafe, with collision avoidance rates lagging task completion on safety-critical benchmarks.
26	We present a factorial study of twelve conditions varying five factors (gradient flow, label content, normalization type, spatial reference frame, and temporal extent) to isolate how auxiliary spatial supervision during VLA fine-tuning affects collision avoidance.
27	Our central finding is a \textbf{normalization-dependent gradient flow effect}. Under Batch Normalization (BN), gradient flow degrades safety: Full OCC BN achieves a 0.725 Collision Avoidance Rate versus 0.767 for Detach BN (Cohen's $d = -0.93$, large), falling below the no-auxiliary-head Vanilla baseline (0.745). Under Layer Normalization (LN), gradient flow is benign: Full OCC LN reaches 0.777, above Vanilla (Cohen's $d = +1.11$, large). Two large main effects drive this pattern: (1)~gradient flow under BN reduces CAR by 4.2\,pp ($d{=}0.93$), with BN + gradient flow as the sole configuration falling below the Vanilla baseline; (2)~LN provides a consistent 4--5\,pp safety advantage over BN ($d{\approx}1.03$, large), regardless of gradient flow. The BN + gradient flow cell is both the worst-performing and most unstable configuration ($\sigma{=}0.064$, ${\geq}\,2{\times}$ all other cells). Spatial label content (ground-truth occupancy, random bina
…[truncated 1094 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_compilation_check_20260528T062030",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-28T06:22:43.721375+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_compilation_check_20260528T062030",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-28T06:22:43.721560+00:00_

1	
2	\section{Results}
3	\label{sec:results}
4	
5	\subsection{Main Results}
6	
7	Table~\ref{tab:main_results} summarizes TSR and CAR across conditions (50 rollouts $\times$ 10 tasks per seed). $\Delta$CAR is computed against the matched-codebase Vanilla baseline (v2: $0.745 \pm 0.024$, 3 seeds, for factorial conditions above the midrule; v1: 0.780 for supplementary conditions below). Random OCC ($^\star$) uses v1 code but is included above the midrule as a factorial control; its $\Delta$CAR is omitted due to the cross-codebase baseline mismatch. Statistical comparisons use permutation tests and Cohen's $d$ against the Vanilla baseline.
8	
9	\textbf{Gradient flow interacts with normalization type.} The four factorial cells reveal a normalization-dependent pattern. Under BatchNorm, gradient flow degrades safety: Full OCC (BN, gradient ON) is the worst-performing cell (CAR $0.725$, $\Delta{=}-2.0$\,pp vs.\ Vanilla) and the sole configuration falling below baseline, while Detach OCC (gradient OFF) exceeds it ($0.767$, $\Delta{=}+2.2$\,pp). Under LayerNorm, gradient flow is benign: Full OCC+LN ($0.777$, $\Delta{=}+3.2$\,pp) already exceeds Vanilla, and the preliminary Detach+LN result (CAR $0.826$, $n{=}1$) suggests further gains ($\Delta{=}+8.1$\,pp). Both LN cells exceed the Vanilla baseline, whereas only the gradient-OFF BN cell does so. The BN + gradient flow cell also exhibits the highest instability ($\sigma{=}0.064$, ${\geq}\,2{\times}$ all other cells). Spatial label content does not detectably affect outcomes: Full OCC (ground-truth occupancy), Random OCC (random binary labels), and Depth (egocentric depth maps) all fall within cross-seed variance ($p > 0.4$, observed under v1 codebase for Random OCC and Depth).
10	
11	\textbf{BN + gradient flow destabilizes training.} Full OCC (BN) exhibits the highest variance of any factorial cell ($\sigma{=}0.064$, ${\geq}\,2{\times}$ that of all other cells; $\sigma \leq 0.032$ for all other cells): individual seeds range f
…[truncated 7050 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_compilation_check_20260528T062030",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-28T06:22:43.721754+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-34685",
  "command": "find /root/occsafe_vla -name \"*.tex\" -o -name \"*.bib\" -o -name \"*.pdf\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_compilation_check_20260528T062030",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-34685",
    "command": "find /root/occsafe_vla -name \"*.tex\" -o -name \"*.bib\" -o -name \"*.pdf\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-28T06:22:43.721906+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/occsafe_vla/openvla-oft/analysis/per_task_comparison.pdf\\n/root/occsafe_vla/openvla-oft/analysis/per_task_ci.tex\\n/root/occsafe_vla/openvla-oft/analysis/output/per_task_tsr.pdf\\n/root/occsafe_vla/openvla-oft/analysis/output/per_task_car.pdf\\n/root/occsafe_vla/openvla-oft/analysis/output/hard_tasks.pdf\\n/root/occsafe_vla/openvla-oft/analysis/output/seed_variance_heatmap.pdf\\n/root/occsafe_vla/openvla-oft/analysis/output/variance_ratio.pdf\\n/root/occsafe_vla/openvla-oft/analysis/output/ablation_car_comparison.pdf\\n/root/occsafe_vla/openvla-oft/analysis/output/ablation_tsr_comparison.pdf\\n/root/occsafe_vla/openvla-oft/analysis/output/diagnostic_matrix.pdf\\n/root/occsafe_vla/artifacts/figures/gradient_analysis_combined.pdf\\n/root/occsafe_vla/artifacts/gradient_analysis_mixed_seed/Vanilla_s0_gradient_norms.pdf\\n/root/occsafe_vla/artifacts/gradient_analysis_mixed_seed/Full_OCC_s0_gradient_norms.pdf\\n/root/occsafe_vla/artifacts/gradient_analysis_mixed_seed/Detach_BN_s2_gradient_norms.pdf\\n/root/occsafe_vla/artifacts/gradient_analysis_mixed_seed/Random_s2_gradient_norms.pdf\\n/root/occsafe_vla/figures/learning_curve.pdf\\n/root/occsafe_vla/figures/car_heatmap.pdf\\n/root/occsafe_vla/figures/delta_car.pdf\\n/root/occsafe_vla/figures/delta_car_2seed.pdf\\n/root/occsafe_vla/analysis/results/depth_gradient_norms.pdf\\n/root/occsafe_vla/analysis/results/invalid/full_occ_gradient_norms.pdf\\n/root/occsafe_vla/analysis/results/invalid/cka_full_occ_vs_depth.pdf\\n/root/occsafe_vla/analysis/results/figures/gradient_analysis_combined.pdf\\n/root/occsafe_vla/analysis/results/gradient/vanilla_gradient_norms.pdf\\n/root/occsafe_vla/analysis/results/gradient/full_occ_gradient_norms.pdf\\n/root/occsafe_vla/analysis/results/gradient/detach_gradient_norms.pdf\\n/root/occsafe_vla/analysis/results/gradient/random_occ_gradient_norms.pdf\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elap
…[truncated 23 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_compilation_check_20260528T062030",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-28T06:22:43.722050+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_compilation_check_20260528T062030",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-28T06:22:43.722211+00:00_

1	\section{Introduction}
2	
3	Vision-language-action (VLA) models map visual observations and language instructions to robot actions, and recent fine-tuning recipes achieve high task success on standard manipulation benchmarks~\cite{brohan2023rt2, kim2024openvla, kim2025oft}. Behavioral safety, however, does not follow from task completion. On SafeLIBERO Level~I~\cite{hu2025vlsa}, OpenVLA-7B fine-tuned with the OFT recipe~\cite{kim2025oft} reaches a Task Success Rate (TSR) of 87.8\% but a Collision Avoidance Rate (CAR) of only 74.5\%. On the three most constrained tasks, collision rates reach 43--93\%. These numbers expose a gap between what training objectives optimize for and what safe deployment requires: the robot completes the task but fails to avoid contact with surrounding objects. Identifying which fine-tuning design choices affect collision avoidance is a prerequisite for closing this gap.
4	
5	Two active research threads address related but distinct aspects of this problem. The first enriches VLA models with auxiliary spatial prediction (occupancy grids, depth maps, point clouds) to inject 3D geometric structure into vision encoders~\cite{li2026spatialforcing, yuan2025depthvla, wu2025spatialvla, liu2025occvla}. At least fifteen such methods have appeared in the past year~\cite{wu2026stvla, chen2026gstvla, tu2026sgvla, xiao2026stemvla, li2025pointvla, sun2025geovla, bhat20253dcavla, li2025qdepthvla, abouzeid2025geoaware, rao2026augvla3d, li2026corridorvla}, all reporting improved task success. The implicit assumption in this literature is that better spatial awareness should also yield safer behavior, since the robot ``knows where things are.'' The second thread targets VLA safety directly through runtime action filtering~\cite{hu2025vlsa, zhai2026cofreevla, raja2024ogmcbf} or constrained reinforcement learning~\cite{zhang2025safevla}. These two lines of work are disconnected: no spatial method evaluates its effect on collision avoidance, and no safety meth
…[truncated 4953 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_compilation_check_20260528T062030",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-28T06:22:43.722357+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_compilation_check_20260528T062030",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/discussion.tex"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-28T06:22:43.722509+00:00_

1	
2	\section{Discussion}
3	\label{sec:discussion}
4	\label{sec:why_gradient}
5	
6	BatchNorm is not inherently harmful: Detach OCC (BN, gradient OFF) matches or slightly exceeds Vanilla (0.767 vs.\ 0.745, $p{=}0.28$). The damage is BN-specific: under BatchNorm, gradient flow drops CAR below the Vanilla baseline (0.725 vs.\ 0.745, $d{=}{-}0.93$), while under LayerNorm, gradient flow is benign (0.777 vs.\ 0.745, $d{=}{+}1.11$). Both normalization rows show within-row deficits from gradient flow ($-$4.2\,pp for BN, $-$4.9\,pp for LN), but only the BN row falls below the no-auxiliary baseline. CKA analysis confirms that encoder representations remain intact under all conditions (CKA $\geq$ 0.95 for both DINOv2 and SigLIP), ruling out representational drift and localizing the effect to optimization dynamics. The BN + gradient flow cell is both the worst-performing and the most unstable configuration ($\sigma{=}0.064$, ${\geq}\,2{\times}$ all other cells). We hypothesize that BatchNorm's running statistics introduce sensitivity to distributional shifts from auxiliary gradients, a coupling absent in LayerNorm's per-token computation. The numerical advantage of Detach OCC ($+$2.2\,pp, with 3 of 4 seeds exceeding the Vanilla mean) raises the possibility that detached auxiliary heads provide a mild regularization benefit, though larger samples are needed to confirm.
7	
8	\textbf{Normalization independently affects safety.} LN provides a consistent safety advantage over BN ($+$5.2\,pp under gradient flow, $d{=}1.03$; $+$5.9\,pp without, Cell~4 preliminary), comparable in magnitude to the gradient flow effect. For practitioners who must retain gradient flow, LayerNorm converts the BN safety deficit into a gain, an architectural advantage, since label content does not detectably affect outcomes.
9	
10	\textbf{Additive protection model.} Cell~1 (BN + gradient flow) is the only factorial cell below Vanilla, confirming that safety degradation requires the joint presence of BatchNor
…[truncated 3353 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_compilation_check_20260528T062030",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-28T06:22:43.722648+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_compilation_check_20260528T062030",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/conclusion.tex"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-28T06:22:43.722796+00:00_

1	
2	\section{Conclusion}
3	
4	We presented a systematic factorial study of auxiliary spatial supervision during VLA fine-tuning. A $2{\times}2$ factorial reveals two large main effects: gradient flow under BatchNorm degrades collision avoidance below the Vanilla baseline ($d{=}{-}0.93$) and produces the highest training instability ($\sigma{=}0.064$); LayerNorm provides a consistent 4--5\,pp safety advantage ($d{\approx}1.03$). Only the BN + gradient flow combination harms safety; spatial label content showed no detectable effect. Practitioners should omit auxiliary spatial heads or, if required, use detached gradients with LayerNorm; avoid combining BatchNorm with gradient flow. CKA analysis localizes the degradation to optimization dynamics rather than representational capacity (CKA $\geq$ 0.95). Training-time collision avoidance may instead require approaches that directly encode safety constraints~\cite{zhang2025safevla}.
5	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_compilation_check_20260528T062030",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-28T06:22:43.722920+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_compilation_check_20260528T062030",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/appendix.tex"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-28T06:22:43.723164+00:00_

1	
2	\section{Extended Per-Task Results}
3	\label{app:per_task}
4	
5	Table~\ref{tab:per_task} reports per-task mean CAR across seeds for each condition. Seven tasks achieve CAR $\geq$ 0.92 under Vanilla, while three physically constrained tasks (T3, T5, T6) fall below 0.58. The overall CAR differences reported in the main text are dominated by these three hard tasks, which average 0.342 compared to 0.968 for the seven easy tasks.
6	
7	\begin{table}[h]
8	\centering
9	\caption{Per-task mean CAR across seeds (50 rollouts per seed, v1 code). This table reports v1 codebase results retained for completeness; all main analyses use v2 data (Table~\ref{tab:main_results}). All conditions use 3 seeds except Depth (4). Detach+LN per-task uses 2 seeds (s1, s2; s0 lacks per-task breakdown).}
10	\label{tab:per_task}
11	\begin{tabular}{clccccccc}
12	\toprule
13	 & & \multicolumn{7}{c}{Mean CAR by Condition} \\
14	\cmidrule(lr){3-9}
15	Task & Diff. & Vanilla & Full OCC & Random & Detach & Det+LN & Depth & Cut@35K \\
16	\midrule
17	T0 & Easy  & 0.98 & 0.98 & 0.99 & 0.97 & 0.97 & 0.99 & 0.98 \\
18	T1 & Easy  & 0.92 & 0.93 & 0.99 & 0.89 & 0.78 & 0.93 & 0.95 \\
19	T2 & Easy  & 0.92 & 0.93 & 0.94 & 0.93 & 0.90 & 0.90 & 0.94 \\
20	T3 & Hard  & 0.38 & 0.37 & 0.31 & \textbf{0.11} & 0.44 & 0.50 & 0.55 \\
21	T4 & Easy  & 0.98 & 0.99 & 0.95 & 0.98 & 0.96 & 0.92 & 0.97 \\
22	T5 & Hard  & 0.07 & 0.17 & 0.23 & \textbf{0.05} & 0.12 & 0.08 & 0.04 \\
23	T6 & Hard  & 0.57 & 0.61 & 0.55 & 0.56 & 0.36 & 0.54 & 0.38 \\
24	T7 & Easy  & 0.97 & 0.99 & 0.95 & 0.98 & 1.00 & 0.96 & 0.98 \\
25	T8 & Easy  & 1.00 & 1.00 & 1.00 & 0.99 & 0.99 & 0.99 & 0.99 \\
26	T9 & Easy  & 1.00 & 0.99 & 0.99 & 1.00 & 1.00 & 1.00 & 1.00 \\
27	\midrule
28	\multicolumn{2}{l}{Overall} & 0.780 & 0.797 & 0.789 & 0.746 & 0.765 & 0.780 & 0.779 \\
29	\bottomrule
30	\end{tabular}
31	\end{table}
32	
33	\textbf{Ceiling effects.} On the seven easy tasks (T0--T2, T4, T7--T9), all conditions achieve CAR $\geq$ 0.89, leaving minimal room for au
…[truncated 20046 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_compilation_check_20260528T062030",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-28T06:22:43.723319+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_compilation_check_20260528T062030",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-28T06:22:43.723486+00:00_

1	
2	\section{Method}
3	
4	We fine-tune OpenVLA-7B~\cite{kim2024openvla} with the OFT recipe~\cite{kim2025oft}, which concatenates DINOv2~\cite{oquab2024dinov2} (1024-d) and SigLIP~\cite{zhai2023siglip} (1152-d) patch features into a 2176-dimensional representation per spatial token. We apply LoRA~\cite{hu2022lora} (rank 32, $\alpha{=}16$) and augment the action prediction loss with an auxiliary spatial prediction head:
5	\begin{equation}
6	\mathcal{L}_\text{total} = \mathcal{L}_\text{action} + \lambda(t) \cdot \mathcal{L}_\text{aux}(h(\phi_v(o_t)), s_t^*),
7	\quad \lambda(t) = 0.01 \cdot \exp(-t / 50000)
8	\end{equation}
9	where $h$ denotes the auxiliary head, $\phi_v$ the frozen-then-LoRA-adapted vision encoders, and $s_t^*$ the ground-truth spatial label at step $t$. The coefficient $\lambda(t)$ decays exponentially so that spatial gradients shape early representations without dominating late-stage action refinement. The auxiliary head is discarded at inference, incurring zero additional cost.
10	
11	\textbf{BEV occupancy head.} The head (1.2M parameters) maps the 256 patch tokens from the current observation frame to a $64{\times}64$ binary occupancy grid. A linear projection ($2176{\to}256$) is reshaped to $16{\times}16$, followed by two transposed convolutions ($256{\to}128{\to}64$, kernel 4, stride 2) each with BatchNorm2d and GELU, and a final $1{\times}1$ convolution with sigmoid activation. Ground-truth grids are rendered from MuJoCo simulator state replay by projecting object bounding boxes onto the table-plane BEV. Training uses focal loss~\cite{lin2017focal} ($\alpha{=}0.25$, $\gamma{=}2.0$) to handle class imbalance in the sparse occupancy signal. The initial auxiliary weight $\lambda_0{=}0.01$ is set to keep auxiliary gradients below 2\% of the action loss magnitude, avoiding interference with action learning.
12	
13	\textbf{Monocular depth head.} This head shares the same convolutional architecture but replaces the sigmoid with ReLU and uses smooth-L
…[truncated 4176 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_compilation_check_20260528T062030",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-28T06:22:43.723689+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-34685",
  "command": "ls -la /root/occsafe_vla/docs/paper/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_compilation_check_20260528T062030",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-34685",
    "command": "ls -la /root/occsafe_vla/docs/paper/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-28T06:22:43.723831+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"ls: cannot access '/root/occsafe_vla/docs/paper/': No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_compilation_check_20260528T062030",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-28T06:22:43.723954+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "X\\.XX|TODO|FIXME|XXX|\\?\\?\\?",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_compilation_check_20260528T062030",
  "tool": "Grep",
  "tool_args": {
    "pattern": "X\\.XX|TODO|FIXME|XXX|\\?\\?\\?",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-28T06:22:43.724077+00:00_

docs/paper/aaai.bst:620:      "empty year in " cite$ * "; set to ????" * warning$
docs/paper/aaai.bst:621:       pop$ "????"
docs/paper/appendix.tex:116:\textbf{Cross-benchmark Vanilla baseline.} Vanilla baseline on LIBERO-Object achieves CAR \textbf{X.XX} ($n{=}2$), confirming that the safety gap between TSR and CAR is not specific to LIBERO-Spatial.
docs/paper/appendix.tex:117:% TODO: fill X.XX with vanilla_object eval data (~08:45 UTC)
docs/paper/corl_2026.sty:29:% TODO: nohyperref is not working at the moment

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_compilation_check_20260528T062030",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-28T06:22:43.724196+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "n\\{?=\\}?1|preliminary|in progress|camera-ready",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper",
  "output_mode": "content",
  "-n": "True",
  "-i": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_compilation_check_20260528T062030",
  "tool": "Grep",
  "tool_args": {
    "pattern": "n\\{?=\\}?1|preliminary|in progress|camera-ready",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper",
    "output_mode": "content",
    "-n": "True",
    "-i": "True"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-28T06:22:43.724367+00:00_

docs/paper/BATCH_A_PATCH_TEMPLATE.md:30:- 若 n≥2 且不再 preliminary，移除 `$^{b}$` 标记
docs/paper/BATCH_A_PATCH_TEMPLATE.md:34:当前: `$^{b}$Preliminary; additional seeds in progress, full results in camera-ready.`
docs/paper/BATCH_A_PATCH_TEMPLATE.md:36:若 Cell 4 n≥3: 移除 `$^{b}$Preliminary...camera-ready` 部分
docs/paper/BATCH_A_PATCH_TEMPLATE.md:37:若 Cell 4 n=2: 改为 `$^{b}$Two seeds; additional seeds in camera-ready.`
docs/paper/BATCH_A_PATCH_TEMPLATE.md:56:当前: `$^{b}$Cell~4 preliminary ($n{=}1$); additional seeds in progress.`
docs/paper/BATCH_A_PATCH_TEMPLATE.md:64:- `Detach+LN result (CAR $0.826$, $n{=}1$)` → 更新 CAR/n
docs/paper/BATCH_A_PATCH_TEMPLATE.md:70:- `The within-LN deficit ($-$4.9\,pp) is preliminary ($n{=}1$ for Cell~4)` → 更新 n
docs/paper/BATCH_A_PATCH_TEMPLATE.md:72:- `$n{\geq}3$ confirmation is in progress for camera-ready` → 若 n≥3 删除此句
docs/paper/BATCH_A_PATCH_TEMPLATE.md:92:- 若 Detach+LN n≥3 不再 preliminary, 删除 discussion 中的 preliminary 注释
docs/paper/BATCH_A_PATCH_TEMPLATE.md:100:- `the v2 preliminary result ($n{=}1$, CAR $0.826$)` → 更新
docs/paper/BATCH_A_PATCH_TEMPLATE.md:104:- `Detach+LN uses v2 ($n{=}1$, preliminary)` → 更新 n
docs/paper/BATCH_A_PATCH_TEMPLATE.md:124:| results.tex | Table 1 (line 28) | 0.826, n=1 | ✅ |
docs/paper/BATCH_A_PATCH_TEMPLATE.md:127:| results.tex | §4.2 text | -4.9pp, n=1 | ✅ |
docs/paper/BATCH_A_PATCH_TEMPLATE.md:130:| discussion.tex | — | (检查 preliminary 标记) | ✅ |
docs/paper/BATCH_A_PATCH_TEMPLATE.md:131:| appendix.tex | Extended Analysis | 0.826, n=1 | ✅ |
docs/paper/BATCH_A_PATCH_TEMPLATE.md:132:| method.tex | Evaluation | n=1, preliminary | ✅ |
docs/paper/main.log:52:Package: corl_2026 2026/08/15 CORL2026 submission/preprint/camera-ready style f
docs/paper/aaai25.sty:8:\def\nocopyright{\gdef\copyright@on{}} % Copyright notice is required for camera-ready only.
docs/paper/discussion.tex:8:\textbf{Normalization independently affects safety.} LN provides a consistent safety advantage over BN ($+$5.2\,pp under gradient flow, $d{=}1.03
…[truncated 6922 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_compilation_check_20260528T062030",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-28T06:22:43.724520+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "0\\.826|0\\.814|Cell.?4",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_compilation_check_20260528T062030",
  "tool": "Grep",
  "tool_args": {
    "pattern": "0\\.826|0\\.814|Cell.?4",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-28T06:22:43.724711+00:00_

docs/paper/BATCH_A_PATCH_TEMPLATE.md:11:| Cell 4 (Detach+LN) | 1 | 0.826 | detach_ln_s3 (0.802?), detach_ln_v2_s0 | 2-3 |
docs/paper/BATCH_A_PATCH_TEMPLATE.md:16:### Cell 4 更新 (Detach+LN, 当前 line 28)
docs/paper/BATCH_A_PATCH_TEMPLATE.md:20:OFF & LN & 1 & $0.826^{b}$ & $0.894$ & $+$8.1 \\
docs/paper/BATCH_A_PATCH_TEMPLATE.md:36:若 Cell 4 n≥3: 移除 `$^{b}$Preliminary...camera-ready` 部分
docs/paper/BATCH_A_PATCH_TEMPLATE.md:37:若 Cell 4 n=2: 改为 `$^{b}$Two seeds; additional seeds in camera-ready.`
docs/paper/BATCH_A_PATCH_TEMPLATE.md:41:当前 Cell 4 行:
docs/paper/BATCH_A_PATCH_TEMPLATE.md:43:LayerNorm    & Full OCC+LN (0.777) & Detach+LN ($0.826^{b}$) & $-$4.9$^{b}$ \\
docs/paper/BATCH_A_PATCH_TEMPLATE.md:56:当前: `$^{b}$Cell~4 preliminary ($n{=}1$); additional seeds in progress.`
docs/paper/BATCH_A_PATCH_TEMPLATE.md:64:- `Detach+LN result (CAR $0.826$, $n{=}1$)` → 更新 CAR/n
docs/paper/BATCH_A_PATCH_TEMPLATE.md:70:- `The within-LN deficit ($-$4.9\,pp) is preliminary ($n{=}1$ for Cell~4)` → 更新 n
docs/paper/BATCH_A_PATCH_TEMPLATE.md:71:- `Detach+LN shows the highest observed CAR in the factorial design ($0.826$)` → 更新值
docs/paper/BATCH_A_PATCH_TEMPLATE.md:79:OFF_mean = (Cell3 + NEW_Cell4) / 2 = (0.767 + NEW) / 2
docs/paper/BATCH_A_PATCH_TEMPLATE.md:83:当前: d=-0.60, p=0.396 → 需用新 Cell 4 数据重算
docs/paper/BATCH_A_PATCH_TEMPLATE.md:96:- 无 Cell 4 具体数字，不需改
docs/paper/BATCH_A_PATCH_TEMPLATE.md:100:- `the v2 preliminary result ($n{=}1$, CAR $0.826$)` → 更新
docs/paper/BATCH_A_PATCH_TEMPLATE.md:110:Cell 4 数据点变化 → 需重新生成 factorial interaction plot。
docs/paper/BATCH_A_PATCH_TEMPLATE.md:117:2. 手动交叉检查: Abstract ↔ Table 1 ↔ §4.2 ↔ Discussion 中的 Cell 4 数字
docs/paper/BATCH_A_PATCH_TEMPLATE.md:120:## 快速对照表：Cell 4 数字出现位置
docs/paper/BATCH_A_PATCH_TEMPLATE.md:124:| results.tex | Table 1 (line 28) | 0.826, n=1 | ✅ |
docs/paper/BATCH_A_PATCH_TEMPLATE.md:125:| results.tex | Table 2 (line 66) | 0.826^b | ✅ |
docs/paper/BATCH_A_PATCH_TEMPLATE.md:126:| results.tex | §4.1 text | 0.826, +8.1pp | ✅ |
docs/paper/BATC
…[truncated 5443 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_compilation_check_20260528T062030",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-28T06:22:43.724881+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.pdf",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_compilation_check_20260528T062030",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.pdf",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-28T06:22:43.725010+00:00_

docs/paper/figures/gradient_analysis_combined.pdf
docs/paper/figures/cka_analysis.pdf
docs/paper/figures/per_layer_conflict_rate.pdf
docs/paper/figures/grad_norm_heatmap.pdf
docs/paper/figures/per_layer_combined.pdf
docs/paper/figures/dose_response.pdf
docs/paper/figures/gradient_analysis_v2_combined.pdf
docs/paper/figures/factorial_2x2.pdf
docs/paper/figures/fig1_overview.pdf
docs/paper/main.pdf

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_compilation_check_20260528T062030",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-28T06:22:43.725156+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/main.pdf",
  "description": "Check main.pdf timestamp"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_compilation_check_20260528T062030",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/main.pdf",
    "description": "Check main.pdf timestamp"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-28T06:22:43.725275+00:00_

-rw-r--r-- 1 ubuntu ubuntu 466472 May 28 02:04 /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/main.pdf

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_compilation_check_20260528T062030",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-28T06:22:43.725388+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "^!",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/main.log",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_compilation_check_20260528T062030",
  "tool": "Grep",
  "tool_args": {
    "pattern": "^!",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/main.log",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-28T06:22:43.725502+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_compilation_check_20260528T062030",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-28T06:22:43.725613+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/main.log",
  "offset": "0",
  "limit": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_compilation_check_20260528T062030",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/main.log",
    "offset": "0",
    "limit": "5"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-28T06:22:43.725749+00:00_

0	This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex 2026.5.2)  28 MAY 2026 02:04
1	entering extended mode
2	 restricted \write18 enabled.
3	 %&-line parsing enabled.
4	**main.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_compilation_check_20260528T062030",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-28T06:22:43.725862+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/BATCH_A_PATCH_TEMPLATE.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_compilation_check_20260528T062030",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/BATCH_A_PATCH_TEMPLATE.md"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-28T06:22:43.726016+00:00_

1	# Batch A Incremental Patch Template
2	
3	> 当 Batch A eval 数据到达后，按此模板快速更新论文。
4	
5	## 预期新数据
6	
7	Batch A 可能包含以下 v2 seeds（以 registry 为准）：
8	
9	| Cell | 当前 n | 当前 CAR | 预期新增 seeds | 新增后 n |
10	|------|--------|---------|---------------|---------|
11	| Cell 4 (Detach+LN) | 1 | 0.826 | detach_ln_s3 (0.802?), detach_ln_v2_s0 | 2-3 |
12	| Cell 2 (Full OCC+LN) | 3 | 0.777±0.032 | (可能已完成) | 3+ |
13	
14	## Step 1: 数据填入 — Table 1 (results.tex)
15	
16	### Cell 4 更新 (Detach+LN, 当前 line 28)
17	
18	当前:
19	```latex
20	OFF & LN & 1 & $0.826^{b}$ & $0.894$ & $+$8.1 \\
21	```
22	
23	替换为（以 n=N, mean=M, std=S 为准）:
24	```latex
25	OFF & LN & N & $M \pm S$ & $TSR_M \pm TSR_S$ & $+$DELTA \\
26	```
27	
28	计算公式:
29	- `DELTA = (M - 0.745) * 100`（vs v2 Vanilla 0.745）
30	- 若 n≥2 且不再 preliminary，移除 `$^{b}$` 标记
31	
32	### 脚注更新 (Table 1 caption, line 16)
33	
34	当前: `$^{b}$Preliminary; additional seeds in progress, full results in camera-ready.`
35	
36	若 Cell 4 n≥3: 移除 `$^{b}$Preliminary...camera-ready` 部分
37	若 Cell 4 n=2: 改为 `$^{b}$Two seeds; additional seeds in camera-ready.`
38	
39	### Factorial Table 更新 (Table 2, results.tex line 57-71)
40	
41	当前 Cell 4 行:
42	```latex
43	LayerNorm    & Full OCC+LN (0.777) & Detach+LN ($0.826^{b}$) & $-$4.9$^{b}$ \\
44	```
45	
46	替换为:
47	```latex
48	LayerNorm    & Full OCC+LN (0.777) & Detach+LN (NEW_MEAN) & $-$NEW_DELTA \\
49	```
50	
51	- `NEW_DELTA = 0.777 - NEW_MEAN`（pp, 保留 1 位小数）
52	- `Δ(BN-LN) Grad OFF` = `0.767 - NEW_MEAN`
53	
54	### Factorial caption (line 59)
55	
56	当前: `$^{b}$Cell~4 preliminary ($n{=}1$); additional seeds in progress.`
57	更新为实际 n。
58	
59	## Step 2: 文本级联更新
60	
61	### results.tex §4.1 (line 7-9)
62	
63	数字引用:
64	- `Detach+LN result (CAR $0.826$, $n{=}1$)` → 更新 CAR/n
65	- `$\Delta{=}+8.1$\,pp` → 重算 ΔCAR
66	
67	### results.tex §4.2 (lines 49-55)
68	
69	- `$-$4.9\,pp` (LN simple effect) → 重算 `0.777 - NEW_CELL4_MEAN`
70	- `The within-LN deficit ($-$4.9\,pp) is preliminary ($n{=}1$ for Cell~4)` → 更新 n
71	- `Detach+LN shows the highest observed
…[truncated 1972 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_compilation_check_20260528T062030",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-28T06:22:43.726192+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "0\\.814|F\\{?=\\}?0\\.02|p\\{?=\\}?0\\.89|eta|0\\.003",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_compilation_check_20260528T062030",
  "tool": "Grep",
  "tool_args": {
    "pattern": "0\\.814|F\\{?=\\}?0\\.02|p\\{?=\\}?0\\.89|eta|0\\.003",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-28T06:22:43.726401+00:00_

docs/paper/main.bbl:252:  Chechik, and Fetaya]{navon2022nashmtl}
docs/paper/main.bbl:254:  E.~Fetaya.
docs/paper/main.tex:27:[Omitted long matching line]
docs/paper/main.tex:28:We hypothesize that this normalization dependence arises from BN's running statistics: auxiliary gradients may shift batch-level statistics in the shared encoder, a coupling absent in LN's per-token computation. Practical guidelines: detach auxiliary gradients under BN architectures; gradient flow is safe under LN; avoid combining BN with gradient flow.
docs/paper/BATCH_A_PATCH_TEMPLATE.md:11:| Cell 4 (Detach+LN) | 1 | 0.826 | detach_ln_s3 (0.802?), detach_ln_v2_s0 | 2-3 |
docs/paper/BATCH_A_PATCH_TEMPLATE.md:16:### Cell 4 更新 (Detach+LN, 当前 line 28)
docs/paper/BATCH_A_PATCH_TEMPLATE.md:43:LayerNorm    & Full OCC+LN (0.777) & Detach+LN ($0.826^{b}$) & $-$4.9$^{b}$ \\
docs/paper/BATCH_A_PATCH_TEMPLATE.md:48:LayerNorm    & Full OCC+LN (0.777) & Detach+LN (NEW_MEAN) & $-$NEW_DELTA \\
docs/paper/BATCH_A_PATCH_TEMPLATE.md:64:- `Detach+LN result (CAR $0.826$, $n{=}1$)` → 更新 CAR/n
docs/paper/BATCH_A_PATCH_TEMPLATE.md:71:- `Detach+LN shows the highest observed CAR in the factorial design ($0.826$)` → 更新值
docs/paper/BATCH_A_PATCH_TEMPLATE.md:87:- `Detach+LN` 相关数字如出现需同步
docs/paper/BATCH_A_PATCH_TEMPLATE.md:92:- 若 Detach+LN n≥3 不再 preliminary, 删除 discussion 中的 preliminary 注释
docs/paper/BATCH_A_PATCH_TEMPLATE.md:104:- `Detach+LN uses v2 ($n{=}1$, preliminary)` → 更新 n
docs/paper/conclusion.tex:4:[Omitted long matching line]
docs/paper/main.log:314:\multlinetaggap=\skip58
docs/paper/corlabbrvnat.bst:33: %   citations, while retaining the commands \citeauthor, \citefullauthor,
docs/paper/discussion.tex:6:[Omitted long matching line]
docs/paper/discussion.tex:8:\textbf{Normalization independently affects safety.} LN provides a consistent safety advantage over BN ($+$5.2\,pp under gradient flow, $d{=}1.03$; $+$5.9\,pp without, Cell~4 preliminary), comparable in magnitude to the gradient flow effect. For practi
…[truncated 10476 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_compilation_check_20260528T062030",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-28T06:22:43.726558+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "0\\.826",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/main.tex",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_compilation_check_20260528T062030",
  "tool": "Grep",
  "tool_args": {
    "pattern": "0\\.826",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/main.tex",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-28T06:22:43.726699+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_compilation_check_20260528T062030",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-28T06:22:43.726875+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/discussion.tex",
  "offset": "9",
  "limit": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_compilation_check_20260528T062030",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/discussion.tex",
    "offset": "9",
    "limit": "3"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-28T06:22:43.727004+00:00_

9	
10	\textbf{Additive protection model.} Cell~1 (BN + gradient flow) is the only factorial cell below Vanilla, confirming that safety degradation requires the joint presence of BatchNorm and gradient flow in this setting; removing either condition suffices to restore safety above baseline. The two protections, switching to LayerNorm and detaching auxiliary gradients, are not redundant but complementary: each independently contributes ${\approx}$4--5\,pp (LN: $+$5.2\,pp, detach: $+$4.2\,pp relative to Cell~1), and the $2{\times}2$ ANOVA interaction term is negligible ($F{=}0.02$, $p{=}0.89$, $\eta^2{=}0.003$; Table~\ref{tab:anova}), consistent with a purely additive model. Cell~4 (Detach+LN), which applies both protections simultaneously, yields a preliminary CAR of 0.814 ($n{=}2$), close to the additive prediction from Cell~1 plus both main effects. Additional seeds (target $n{\geq}3$) are in progress to confirm the additive pattern; final values will appear in the camera-ready version.
11	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_compilation_check_20260528T062030",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 51 · 2026-05-28T06:22:43.727233+00:00_

Here's the complete audit:

---

## 论文状态清单

### 1. 文件位置
- **本地**: `/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/` (main.tex + 7 section files + references.bib)
- **远程 (westd-34685)**: 无 .tex 文件，仅有分析产出 PDF（`/root/occsafe_vla/artifacts/`, `/root/occsafe_vla/analysis/`）
- **已有 Patch 模板**: `docs/paper/BATCH_A_PATCH_TEMPLATE.md`

### 2. 编译状态
- **最近成功编译**: 2026-05-28 02:04 UTC（main.pdf, 466KB）
- **编译错误**: **无**（main.log 中无 `!` error）
- 编译器: pdfTeX/TeX Live 2025

### 3. 内部数据不一致 (CRITICAL)

**Cell 4 (Detach+LN) 数值冲突**:
| 文件 | 行号 | CAR 值 | n |
|------|------|--------|---|
| results.tex | 28 | 0.826 | 1 |
| results.tex | 9, 49, 62 | 0.826 | 1 |
| **discussion.tex** | **10** | **0.814** | **2** |
| appendix.tex | 85, 156, 160 | 0.826 | 1 |
| method.tex | 51 | — | 1 |
| figures/fig1_overview.py | 216 | 0.826 | 1 |

`discussion.tex:10` 已更新为 n=2, CAR=0.814，但**所有其他文件仍为 n=1, CAR=0.826**。必须统一。

### 4. 需更新的位置（按 Cell 4 新数据到达后）

**BATCH_A_PATCH_TEMPLATE.md 已列出完整更新清单**，核心 16 处：

| # | 文件:行 | 当前值 | 更新内容 |
|---|---------|--------|---------|
| 1 | results.tex:28 | `0.826^{b}`, n=1, TSR=0.894, Δ=+8.1 | CAR/n/TSR/Δ |
| 2 | results.tex:9 | "0.826, n=1" | CAR/n |
| 3 | results.tex:49 | "-4.9pp, n=1 preliminary" | LN simple effect + n |
| 4 | results.tex:55 | "$^{b}$Cell~4 preliminary (n=1)" | caption |
| 5 | results.tex:62 | `$0.826^{b}$`, `-4.9^{b}` | Table 2 LN row |
| 6 | results.tex:72 | "Cell~4 n=1; in progress" | Figure 2 caption |
| 7 | discussion.tex:8 | "Cell~4 preliminary" | 移除 preliminary |
| 8 | discussion.tex:10 | **0.814 (n=2)** ← 已部分更新 | 统一到最终值 |
| 9 | appendix.tex:85 | "n=1, CAR $0.826$" | CAR/n |
| 10 | appendix.tex:139-154 | ANOVA: F=0.02, p=0.89, η²=0.003 | 全部重算 |
| 11 | appendix.tex:156,160 | "preliminary (n=1)" | caption |
| 12 | appendix.tex:169,171,172,177 | Pairwise d involving Cell 4 | 全部重算 |
| 13 | method.tex:51 | "n=1, preliminary" | n |
| 14 | main.tex:27 (abstract) | 无直接 0.826 引用，但引用效应量 | 核对效应量 |
| 15 | figures/factorial_2x2.pdf | Cell 4 单点 | **重绘** |
| 16 | figures/fig1_overview.py:216 | 0.826 hardcoded | **重绘** |

### 5. 派生统计量（需重算）

当 Cell 4 值确定后：
- Gradient flow 主效应 d（当前 d=-0.60）
- Normalization 主效应 d（当前 d≈1.03）
- LN simple effect（当前 -4.9pp）
- Δ(BN-LN) Grad OFF（当前 -5.9pp）
- ANOVA F/p/η²
- 6 个 pairwise Cohen's d

### 6. Placeholder

- **appendix.tex:116-117**: `CAR \textbf{X.XX} ($n{=}2$)` — LIBERO-Object Vanilla baseline，TODO 注释标注 "~08:45 UTC"

### 7. Cell 4 样本量提及

Cell 4 n 值的 "preliminary" / "$^{b}$" 标记出现在 **14 处**（上面已列）。如果最终 n≥3，所有 `$^{b}$` 和 "preliminary" 标记都需移除；如果 n=2，改为 "Two seeds; additional seeds in camera-ready"。

### 8. 当前训练进度（per paper_framing.md）
- `detach_ln_v2_s3` (34685:cuda:3) — ETA 05:51 UTC May 28
- `detach_ln_v2_s2` (34685:cuda:0) — resume
- `detach_ln_v2_s0c_r3` (10894:cuda:2) — ETA 22:45 UTC today（超 DDL）

最乐观情况: DDL 前 Cell 4 可达 n=2-3。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_compilation_check_20260528T062030"
}
```

</details>

---
