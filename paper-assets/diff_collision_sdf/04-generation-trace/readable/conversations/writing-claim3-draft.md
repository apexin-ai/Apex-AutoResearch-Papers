# writing claim3 draft

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 15
- **Recorded user turns:** 0
- **Tool calls:** 7
- **Original source:** `logs/chats/worker_writing_claim3_draft_20260527T080803.jsonl`
- **Structured JSON:** [`cbb325fb761c6f8ff999.json`](../../sessions/cb/cbb325fb761c6f8ff999.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

15 recorded events

### Tool call

_source line 1 · 2026-05-27T08:10:17.373159+00:00_

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
  "session": "worker_writing_claim3_draft_20260527T080803",
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

_source line 2 · 2026-05-27T08:10:17.373512+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_claim3_draft_20260527T080803",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-27T08:10:17.373687+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "diff_collision_sdf",
  "file": "paper_framing.md",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_claim3_draft_20260527T080803",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "diff_collision_sdf",
    "file": "paper_framing.md",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-27T08:10:17.373963+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/paper_framing.md\", \"content\": \"# ColliForce-VLA Paper Framing\\n\\n> 维护者: Director | 最后更新: 2026-05-27 01:15 UTC | D035: Scenario B 双 seed 确认，Core Insight 修正 | Post-MVP research phase\\n\\n## Core Insight\\n\\nVLA safety 评估存在系统性缺陷：collision avoidance rate (CAR) 被 action collapse 和几何路径安全严重污染，导致 \\\"安全\\\" 指标虚高。我们通过大规模实证分析（90+ 实验, 6000+ episodes）揭示这一系统性缺陷，提出 EE displacement-filtered CAR 作为修正指标，并证明碰撞避免能力隐式来自 collision-free demonstration data，而非显式几何监督——SDF auxiliary loss 在全测试范围 λ∈[0.005, 0.1] 完全冗余，binding constraint 是 EE-only 的结构性不匹配。\\n\\n## Working Title\\n\\n\\\"Rethinking VLA Safety Evaluation: When 98% of Collision Avoidance is an Illusion\\\"\\n\\n> 聚焦评估方法论贡献（影响面广、scope-proof），SDF 作为验证工具而非主贡献\\n\\n## Target Venue\\n\\n**Primary**: CoRL 2026 Main / ICRA 2027 (用户明确要求主会)\\n**定位**: Diagnostic/evaluation methodology paper with positive method contribution\\n**Fit**: Robotics safety track — \\\"VLA safety metrics are fundamentally broken\\\" 对社区有直接影响\\n\\n## Core Claims (D028 重组: 4→3 claims)\\n\\n### Claim 1: CAR Metric Contaminated by Fake Safety (Primary — 证据强度 ★★★★★)\\n\\nStandard CAR metric is systematically contaminated by two distinct mechanisms: (a) action collapse producing frozen robots falsely counted as \\\"safe\\\", and (b) geometric path safety where capable robots happen to avoid obstacles without any avoidance behavior. \\\"Collision-free\\\" ≠ \\\"collision-avoiding.\\\"\\n\\n**Primary evidence — Action collapse (fake safety)**:\\n- 800 episodes A1 per-episode analysis: CAR=91.5%, but 99.6% of safe episodes show obstacle displacement < 0.1mm (~5nm median) — robot is frozen\\n- TSR=0% 独立确认 action collapse\\n- 术语修正 (D023): fake safety 判定以 TSR=0% + obstacle displacement < 0.1mm 双证据链为主\\n\\n**Supporting evidence — Capability-safety anti-correlation (原 Claim 2)**:\\n- Pi0.5 3-seed eval: TSR=74.7±1.5%, CAR=26.8±1.6% — 更强模型完成更多任务
…[truncated 9749 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_claim3_draft_20260527T080803",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-27T08:10:17.374141+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/claim3.tex",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_claim3_draft_20260527T080803",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/claim3.tex",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-27T08:10:17.374270+00:00_

docs/paper/claim3.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_claim3_draft_20260527T080803",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-27T08:10:17.374404+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim3.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_claim3_draft_20260527T080803",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim3.tex"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-27T08:10:17.374608+00:00_

1	\section{Avoidance Source Diagnosis}\label{sec:avoidance_source}
2	
3	Fine-tuning on collision-free demonstrations produces genuine collision avoidance: LoRA-adapted Pi0.5 raises CAR by ${\sim}$28 percentage points with zero frozen episodes. Does SDF geometric supervision contribute additional avoidance beyond what demonstrations provide? We compare LoRA-only, LoRA+SDF ($\lambda = 0.005$), and LoRA+SDF ($\lambda = 0.01$) on Pi0.5, all evaluated at the 30K-step checkpoint.
4	
5	\begin{table}[t]
6	\centering
7	\caption{Avoidance source attribution on SafeLIBERO. SDF adds no measurable CAR beyond LoRA-only across $\lambda \in [0.005, 0.1]$ ($p > 0.1$). All fine-tuned models exhibit 0\% frozen rate and displacement $>$\,0.37\,m.}
8	\label{tab:avoidance_source}
9	\vspace{2pt}
10	\small
11	\begin{tabular}{lcccc}
12	\toprule
13	Method & Seeds & TSR (\%) & CAR (\%) & EE Disp (m) \\
14	\midrule
15	Pi0.5 baseline & 3 & 74.7\,$\pm$\,1.5 & 26.8\,$\pm$\,1.6 & 0.367 \\
16	\midrule
17	LoRA-only (no SDF) & 2 & 51.5 & 54.5\,$\pm$\,2.8 & 0.392 \\
18	LoRA+SDF $\lambda{=}0.005$ & 3 & 54.0\,$\pm$\,3.0 & 54.5\,$\pm$\,2.3 & 0.387 \\
19	LoRA+SDF $\lambda{=}0.01$ & 3 & 53.8\,$\pm$\,1.5 & 56.3\,$\pm$\,1.6 & 0.389 \\
20	LoRA+SDF $\lambda{=}0.1$\textsuperscript{$\dagger$} & 2 & 52.5 & 55.5 & -- \\
21	\bottomrule
22	\end{tabular}
23	\vspace{1pt}
24	{\footnotesize \textsuperscript{$\dagger$}20K-step checkpoint, 2 seeds; 30K results pending.}
25	\end{table}
26	
27	Table~\ref{tab:avoidance_source} shows that collision-free demonstrations alone raise CAR by ${\sim}$28 percentage points (26.8\% $\to$ 54.5\%) with zero frozen episodes and displacement above 0.37\,m, confirming genuine avoidance rather than action collapse. Adding SDF supervision produces no measurable benefit: LoRA-only CAR (54.5\%) is identical to $\lambda = 0.005$ and statistically indistinguishable from $\lambda = 0.01$ (56.3\%, $p > 0.1$; null distribution details in Appendix~\ref{sec:appendix_null}). A Phase~2 ablation ($\lamb
…[truncated 2745 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_claim3_draft_20260527T080803",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-27T08:10:17.374840+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim3.tex",
  "old_string": "\\paragraph{Dose-response at higher loss weights.}\\label{sec:lambda_high}\nIncreasing $\\lambda$ by 20$\\times$ to 0.1 yields CAR\\,=\\,55.5\\% (seeds: 55\\%, 56\\%; 20K-step checkpoint), within the null distribution (mean 54.5\\%, $\\sigma = 2.15$, $z = 0.47$). Step-wise evaluation shows CAR remains flat across training steps (dual-seed means: 55.5\\% at 16K, 55.5\\% at 20K, 58.5\\% at 22K), all within the null range (per-seed details in Appendix~\\ref{sec:appendix_stepwise}). EE-only SDF supervision is redundant with the demonstration signal across the full tested range $\\lambda \\in [0.005, 0.1]$ (Figure~\\ref{fig:lambda_car}). This result disambiguates the two-level failure analysis (Section~\\ref{sec:conclusion}): because even a 20$\\times$ increase in SDF loss weight fails to produce additional avoidance, the binding constraint is not training signal magnitude but the structural mismatch between end-effector monitoring and full-body collision surfaces. Per-task CAR ordering is identical across all conditions (chocolate\\_pudding $>$ milk $>$ orange\\_juice $>$ bbq\\_sauce), indicating that the avoidance pattern reflects demonstration distribution characteristics, not geometric supervision.",
  "new_string": "\\paragraph{Dose-response at higher loss weights.}\\label{sec:lambda_high}\nIncreasing $\\lambda$ by 20$\\times$ to 0.1 yields CAR\\,=\\,55.5\\% at the 20K checkpoint (2-seed mean; seeds: 55.0\\%, 56.0\\%), within the null distribution (mean 54.5\\%, $\\sigma = 2.15$, $z = 0.47$). The seed-0 stepwise curve spans six checkpoints from 16K to 28K: 55.5\\%, 55.0\\%, 60.5\\%, 52.5\\%, 53.5\\%, 54.5\\% (mean 55.3\\%), fluctuating around the LoRA-only baseline of 54.5\\% with no upward trend (per-seed details in Appendix~\\ref{sec:appendix_stepwise}). The 22K checkpoint reaches 60.5\\% ($z = 2.79$ against the curve mean), but three observations identify this as single-seed noise: (i)~seed-1 records only 56.5\\% at the same step; (ii)~the three subsequent checkpoints (24K, 26K, 28K) all revert to 52.5--54.5\\%; (iii)~the six-point mean of 55.3\\% falls within 0.4$\\sigma$ of the null. \\placeholder{$\\lambda{=}0.1$ 30K three-seed mean pending.}\n\nAcross the full tested range $\\lambda \\in [0.005, 0.1]$---a 20$\\times$ span---no condition exceeds the null: $\\lambda = 0.005$ yields 54.5\\%\\,$\\pm$\\,2.3 (3 seeds, 30K), $\\lambda = 0.01$ yields 56.3\\%\\,$\\pm$\\,1.6 ($p \\approx 0.12$, 3 seeds, 30K), $\\lambda = 0.1$ yields 55.5\\% (2 seeds, 20K). EE-only SDF supervision exhibits no dose-response relationship with CAR (Figure~\\ref{fig:lambda_car}). This disambiguates the two-level failure: because a 20$\\times$ increase in loss weight fails to produce additional avoidance, the binding constraint is the structural mismatch between end-effector monitoring and full-body collision surfaces, not training signal magnitude. Per-task CAR ordering remains identical across all conditions (chocolate\\_pudding $>$ milk $>$ orange\\_juice $>$ bbq\\_sauce), confirming that avoidance patterns reflect demonstration distribution characteristics rather than geometric supervision."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_claim3_draft_20260527T080803",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim3.tex",
    "old_string": "\\paragraph{Dose-response at higher loss weights.}\\label{sec:lambda_high}\nIncreasing $\\lambda$ by 20$\\times$ to 0.1 yields CAR\\,=\\,55.5\\% (seeds: 55\\%, 56\\%; 20K-step checkpoint), within the null distribution (mean 54.5\\%, $\\sigma = 2.15$, $z = 0.47$). Step-wise evaluation shows CAR remains flat across training steps (dual-seed means: 55.5\\% at 16K, 55.5\\% at 20K, 58.5\\% at 22K), all within the null range (per-seed details in Appendix~\\ref{sec:appendix_stepwise}). EE-only SDF supervision is redundant with the demonstration signal across the full tested range $\\lambda \\in [0.005, 0.1]$ (Figure~\\ref{fig:lambda_car}). This result disambiguates the two-level failure analysis (Section~\\ref{sec:conclusion}): because even a 20$\\times$ increase in SDF loss weight fails to produce additional avoidance, the binding constraint is not training signal magnitude but the structural mismatch between end-effector monitoring and full-body collision surfaces. Per-task CAR ordering is identical across all conditions (chocolate\\_pudding $>$ milk $>$ orange\\_juice $>$ bbq\\_sauce), indicating that the avoidance pattern reflects demonstration distribution characteristics, not geometric supervision.",
    "new_string": "\\paragraph{Dose-response at higher loss weights.}\\label{sec:lambda_high}\nIncreasing $\\lambda$ by 20$\\times$ to 0.1 yields CAR\\,=\\,55.5\\% at the 20K checkpoint (2-seed mean; seeds: 55.0\\%, 56.0\\%), within the null distribution (mean 54.5\\%, $\\sigma = 2.15$, $z = 0.47$). The seed-0 stepwise curve spans six checkpoints from 16K to 28K: 55.5\\%, 55.0\\%, 60.5\\%, 52.5\\%, 53.5\\%, 54.5\\% (mean 55.3\\%), fluctuating around the LoRA-only baseline of 54.5\\% with no upward trend (per-seed details in Appendix~\\ref{sec:appendix_stepwise}). The 22K checkpoint reaches 60.5\\% ($z = 2.79$ against the curve mean), but three observations identify this as single-seed noise: (i)~seed-1 records only 56.5\\% at the same step; (ii)~the three subsequent checkpoints (24K, 26K, 28K) all revert to 52.5--54.5\\%; (iii)~the six-point mean of 55.3\\% falls within 0.4$\\sigma$ of the null. \\placeholder{$\\lambda{=}0.1$ 30K three-seed mean pending.}\n\nAcross the full tested range $\\lambda \\in [0.005, 0.1]$---a 20$\\times$ span---no condition exceeds the null: $\\lambda = 0.005$ yields 54.5\\%\\,$\\pm$\\,2.3 (3 seeds, 30K), $\\lambda = 0.01$ yields 56.3\\%\\,$\\pm$\\,1.6 ($p \\approx 0.12$, 3 seeds, 30K), $\\lambda = 0.1$ yields 55.5\\% (2 seeds, 20K). EE-only SDF supervision exhibits no dose-response relationship with CAR (Figure~\\ref{fig:lambda_car}). This disambiguates the two-level failure: because a 20$\\times$ increase in loss weight fails to produce additional avoidance, the binding constraint is the structural mismatch between end-effector monitoring and full-body collision surfaces, not training signal magnitude. Per-task CAR ordering remains identical across all conditions (chocolate\\_pudding $>$ milk $>$ orange\\_juice $>$ bbq\\_sauce), confirming that avoidance patterns reflect demonstration distribution characteristics rather than geometric supervision."
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-27T08:10:17.375049+00:00_

The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim3.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_claim3_draft_20260527T080803",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-27T08:10:17.375195+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim3.tex",
  "old_string": "{\\footnotesize \\textsuperscript{$\\dagger$}20K-step checkpoint, 2 seeds; 30K results pending.}",
  "new_string": "{\\footnotesize \\textsuperscript{$\\dagger$}20K-step checkpoint, 2 seeds. Stepwise curve (16K--28K) available for seed-0; 30K three-seed mean pending.}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_claim3_draft_20260527T080803",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim3.tex",
    "old_string": "{\\footnotesize \\textsuperscript{$\\dagger$}20K-step checkpoint, 2 seeds; 30K results pending.}",
    "new_string": "{\\footnotesize \\textsuperscript{$\\dagger$}20K-step checkpoint, 2 seeds. Stepwise curve (16K--28K) available for seed-0; 30K three-seed mean pending.}"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-27T08:10:17.375351+00:00_

The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim3.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_claim3_draft_20260527T080803",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-27T08:10:17.375508+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim3.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_claim3_draft_20260527T080803",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim3.tex"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-27T08:10:17.375681+00:00_

1	\section{Avoidance Source Diagnosis}\label{sec:avoidance_source}
2	
3	Fine-tuning on collision-free demonstrations produces genuine collision avoidance: LoRA-adapted Pi0.5 raises CAR by ${\sim}$28 percentage points with zero frozen episodes. Does SDF geometric supervision contribute additional avoidance beyond what demonstrations provide? We compare LoRA-only, LoRA+SDF ($\lambda = 0.005$), and LoRA+SDF ($\lambda = 0.01$) on Pi0.5, all evaluated at the 30K-step checkpoint.
4	
5	\begin{table}[t]
6	\centering
7	\caption{Avoidance source attribution on SafeLIBERO. SDF adds no measurable CAR beyond LoRA-only across $\lambda \in [0.005, 0.1]$ ($p > 0.1$). All fine-tuned models exhibit 0\% frozen rate and displacement $>$\,0.37\,m.}
8	\label{tab:avoidance_source}
9	\vspace{2pt}
10	\small
11	\begin{tabular}{lcccc}
12	\toprule
13	Method & Seeds & TSR (\%) & CAR (\%) & EE Disp (m) \\
14	\midrule
15	Pi0.5 baseline & 3 & 74.7\,$\pm$\,1.5 & 26.8\,$\pm$\,1.6 & 0.367 \\
16	\midrule
17	LoRA-only (no SDF) & 2 & 51.5 & 54.5\,$\pm$\,2.8 & 0.392 \\
18	LoRA+SDF $\lambda{=}0.005$ & 3 & 54.0\,$\pm$\,3.0 & 54.5\,$\pm$\,2.3 & 0.387 \\
19	LoRA+SDF $\lambda{=}0.01$ & 3 & 53.8\,$\pm$\,1.5 & 56.3\,$\pm$\,1.6 & 0.389 \\
20	LoRA+SDF $\lambda{=}0.1$\textsuperscript{$\dagger$} & 2 & 52.5 & 55.5 & -- \\
21	\bottomrule
22	\end{tabular}
23	\vspace{1pt}
24	{\footnotesize \textsuperscript{$\dagger$}20K-step checkpoint, 2 seeds. Stepwise curve (16K--28K) available for seed-0; 30K three-seed mean pending.}
25	\end{table}
26	
27	Table~\ref{tab:avoidance_source} shows that collision-free demonstrations alone raise CAR by ${\sim}$28 percentage points (26.8\% $\to$ 54.5\%) with zero frozen episodes and displacement above 0.37\,m, confirming genuine avoidance rather than action collapse. Adding SDF supervision produces no measurable benefit: LoRA-only CAR (54.5\%) is identical to $\lambda = 0.005$ and statistically indistinguishable from $\lambda = 0.01$ (56.3\%, $p > 0.1$; null distribution details in Appen
…[truncated 3453 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_claim3_draft_20260527T080803",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-27T08:10:17.375894+00:00_

完成。`docs/paper/claim3.tex` 已更新：

**表格脚注** (L24): 补充了 stepwise curve 可用范围和 30K pending 说明。

**Dose-response 段落** (L34-37): 重写为两段结构：
1. **λ=0.1 stepwise 分析** — seed-0 六点曲线 (16K-28K, mean 55.3%) + 22K outlier 三证据排除 (cross-seed 56.5%, 24K-28K 回落, curve mean within 0.4σ) + `\placeholder` 标注 30K pending
2. **全域总结** — λ∈[0.005, 0.1] 三个条件的 CAR 数值汇总，无 dose-response，binding constraint 归因于 EE-only 结构性不匹配

注意：`\placeholder` 宏需要在 preamble 中定义（如 `\newcommand{\placeholder}[1]{\textcolor{red}{[#1]}}`），否则编译会报错。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_writing_claim3_draft_20260527T080803"
}
```

</details>

---
