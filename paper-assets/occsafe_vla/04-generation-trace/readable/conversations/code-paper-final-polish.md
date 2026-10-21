# code paper final polish

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 89
- **Recorded user turns:** 0
- **Tool calls:** 44
- **Original source:** `logs/chats/worker_code_paper_final_polish_20260525T104936.jsonl`
- **Structured JSON:** [`8ad47bb6eb6a6cf19784.json`](../../sessions/8a/8ad47bb6eb6a6cf19784.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

89 recorded events

### Tool call

_source line 1 · 2026-05-25T10:54:10.334800+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper && ls *.tex *.bib 2>/dev/null",
  "description": "List tex and bib files in paper directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_paper_final_polish_20260525T104936",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper && ls *.tex *.bib 2>/dev/null",
    "description": "List tex and bib files in paper directory"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-25T10:54:10.335128+00:00_

appendix.tex
conclusion.tex
discussion.tex
experiment_setup.tex
experiments.tex
experiments_old.tex
introduction.tex
main.tex
method.tex
references.bib
references.tex
related_work.tex
results.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_paper_final_polish_20260525T104936",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-25T10:54:10.335290+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "pdflatex -interaction=nonstopmode main.tex 2>&1 | tail -50 && bibtex main 2>&1 && pdflatex -interaction=nonstopmode main.tex 2>&1 | tail -20 && pdflatex -interaction=nonstopmode main.tex 2>&1 | tail -20",
  "description": "Compile LaTeX paper",
  "timeout": "120000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_paper_final_polish_20260525T104936",
  "tool": "Bash",
  "tool_args": {
    "command": "pdflatex -interaction=nonstopmode main.tex 2>&1 | tail -50 && bibtex main 2>&1 && pdflatex -interaction=nonstopmode main.tex 2>&1 | tail -20 && pdflatex -interaction=nonstopmode main.tex 2>&1 | tail -20",
    "description": "Compile LaTeX paper",
    "timeout": "120000"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-25T10:54:10.335460+00:00_

* \voffset=0.0pt
* \mag=1000
* \@twocolumnfalse
* \@twosidefalse
* \@mparswitchfalse
* \@reversemarginfalse
* (1in=72.27pt=25.4mm, 1cm=28.453pt)

(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)
(/usr/share/texlive/texmf-dist/tex/latex/psnfss/ot1phv.fd) (./introduction.tex
[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-
dist/fonts/enc/dvips/base/8r.enc}]) (./related_work.tex [2 <./figures/fig1_over
view.pdf>]) (./method.tex [3]
(/usr/share/texlive/texmf-dist/tex/latex/psnfss/ts1ptm.fd)
(/usr/share/texlive/texmf-dist/tex/latex/psnfss/omsptm.fd)) [4] (./results.tex
Underfull \vbox (badness 1735) has occurred while \output is active [5]
[6 <./figures/factorial_2x2.pdf>]
Underfull \vbox (badness 2762) has occurred while \output is active [7 <./figur
es/gradient_analysis_combined.pdf>]) (./discussion.tex [8 <./figures/cka_analys
is.pdf>]) (./conclusion.tex) (./main.bbl [9] [10] [11]) [12] (./appendix.tex

LaTeX Warning: `h' float specifier changed to `ht'.

[13]

LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: `h' float specifier changed to `ht'.

) [14] [15 <./figures/per_layer_combined.pdf> <./figures/dose_response.pdf>]
(./main.aux) )
(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmbsy10.pfb>&lt;/usr/share/texlive/texmf-dist/f
onts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/t
ype1/public/amsfonts/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pu
blic/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/am
sfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/c
m/cmr9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10
.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy6.pfb>&lt;/
usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb></usr/sha
re/texl
…[truncated 3237 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_paper_final_polish_20260525T104936",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-25T10:54:10.335629+00:00_

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
  "session": "worker_code_paper_final_polish_20260525T104936",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/main.tex"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-25T10:54:10.335805+00:00_

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
13	
14	\newcommand{\todo}[1]{\textcolor{red}{[TODO: #1]}}
15	
16	\title{Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer?\\ An Empirical Investigation}
17	
18	\author{
19	Anonymous Author(s)
20	}
21	
22	\begin{document}
23	\maketitle
24	
25	\begin{abstract}
26	Fine-tuned Vision-Language-Action (VLA) models can achieve high task success yet remain behaviorally unsafe: on SafeLIBERO Level~I, a fine-tuned OpenVLA-OFT attains 90.7\% task success but only 78.0\% collision avoidance.
27	We present a systematic factorial study isolating how auxiliary spatial supervision during VLA fine-tuning affects collision avoidance, with twelve conditions varying gradient flow, label content, normalization type, spatial reference frame, and temporal extent.
28	Our central finding is a crossover interaction between normalization type and gradient flow in the auxiliary head (interaction effect: 7.3\,pp, $p{=}0.025$). BatchNorm with gradient flow maintains CAR comparable to Vanilla (0.797 vs.\ 0.780), but without gradient flow causes catastrophic representational drift (Detach OCC 0.746, CKA $\downarrow$0.31--0.54). LayerNorm eliminates this drift under detachment (Detach+LN 0.765, CKA $\geq$0.96) but consistently degrades safety when gradient flow is present (Full OCC+LN 0.743, $-$3.7\,pp vs.\ Vanilla); this is the worst configuration tested. Gradient flow benefits are thus BatchNorm-mediated, not an intrinsic property of auxiliary gradients.
29	This reveals a representation-behavior dissociation: Full OCC+LN preserves pretrained representations yet achieves the lowest collision avoidance, which demonstrates that representational fidelity does not
…[truncated 824 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_paper_final_polish_20260525T104936",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-25T10:54:10.335961+00:00_

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
  "session": "worker_code_paper_final_polish_20260525T104936",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-25T10:54:10.336134+00:00_

1	
2	\section{Introduction}
3	
4	Vision-language-action (VLA) models map visual observations and language instructions directly to robot actions, achieving high task success on manipulation benchmarks~\cite{brohan2023rt2, kim2024openvla, kim2025oft}. Yet task success does not imply behavioral safety. On SafeLIBERO Level~I~\cite{hu2025vlsa}, a fine-tuned OpenVLA-OFT completes 90.7\% of tasks but avoids collisions in only 78.0\% of episodes; on the three most constrained tasks, collision rates reach 53--93\%.
5	
6	Auxiliary spatial prediction (occupancy grids, depth maps, point clouds) improves VLA task success by injecting 3D structure into vision encoders~\cite{li2026spatialforcing, yuan2025depthvla, wu2025spatialvla}. Separately, safety methods apply runtime action filtering~\cite{hu2025vlsa} or constrained RL~\cite{zhang2025safevla} to reduce collisions. These two threads remain disconnected: no spatial method evaluates collision avoidance, and no safety method leverages spatial representations. Whether auxiliary spatial supervision affects safety, and through what mechanism, is unknown.
7	
8	We present a systematic factorial study isolating how auxiliary spatial supervision during VLA fine-tuning affects collision avoidance. Twelve conditions on OpenVLA-OFT~\cite{kim2024openvla, kim2025oft} with LoRA vary gradient flow, label content, normalization type, spatial reference frame, and temporal extent. Figure~\ref{fig:overview} summarizes the setup and key finding. Our contributions:
9	
10	\begin{figure*}[t]
11	\centering
12	\includegraphics[width=\textwidth]{figures/fig1_overview.pdf}
13	\caption{\textbf{Overview.} \textbf{(a)}~VLA policies deployed in contact-rich environments lack collision awareness; a fine-tuned OpenVLA-OFT achieves 90.7\% task success but only 78.0\% collision avoidance on SafeLIBERO. \textbf{(b)}~We attach an auxiliary occupancy prediction head to the vision encoders; it provides gradient flow during training and is discarded at inference (ze
…[truncated 2135 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_paper_final_polish_20260525T104936",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-25T10:54:10.336369+00:00_

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
  "session": "worker_code_paper_final_polish_20260525T104936",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-25T10:54:10.336620+00:00_

1	
2	\section{Method}
3	\label{sec:method}
4	
5	We fine-tune OpenVLA-7B~\cite{kim2024openvla} with the OFT recipe~\cite{kim2025oft}, which concatenates DINOv2~\cite{oquab2024dinov2} (1024-d) and SigLIP~\cite{zhai2023siglip} (1152-d) patch features into a 2176-dimensional representation per spatial token. We apply LoRA~\cite{hu2022lora} (rank 32, $\alpha{=}16$) and augment the action prediction loss with an auxiliary spatial prediction head:
6	\begin{equation}
7	\mathcal{L}_\text{total} = \mathcal{L}_\text{action} + \lambda(t) \cdot \mathcal{L}_\text{aux}(h(\phi_v(o_t)), s_t^*),
8	\quad \lambda(t) = 0.01 \cdot \exp(-t / 50000)
9	\label{eq:total_loss}
10	\end{equation}
11	where $\lambda(t)$ decays exponentially so that spatial gradients shape early representations without dominating late-stage action refinement. The auxiliary head is discarded at inference.
12	
13	\textbf{BEV occupancy head.} The head (1.2M parameters) maps the first 256 patch tokens to a $64{\times}64$ binary occupancy grid: a linear projection ($2176{\to}256$) reshaped to $16{\times}16$, two transposed convolutions ($256{\to}128{\to}64$, kernel 4, stride 2) with BatchNorm and GELU, and a $1{\times}1$ convolution with sigmoid. Ground-truth grids are rendered from MuJoCo state replay. Training uses focal loss~\cite{lin2017focal} ($\alpha{=}0.25$, $\gamma{=}2.0$).
14	
15	\textbf{Monocular depth head.} Same architecture with ReLU output and smooth-L1 loss against egocentric depth maps rendered at $64{\times}64$ from MuJoCo. This head provides an egocentric spatial reference frame, complementing the allocentric BEV occupancy.
16	
17	\subsection{Ablation Design}
18	\label{sec:ablation}
19	
20	We evaluate twelve conditions that systematically vary gradient flow, label content, normalization type, spatial reference frame, and temporal extent:
21	
22	\begin{itemize}[nosep,leftmargin=*]
23	\item \textbf{Vanilla}: action loss only (baseline).
24	\item \textbf{Full OCC}: BEV occupancy with ground-truth labels a
…[truncated 3077 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_paper_final_polish_20260525T104936",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-25T10:54:10.336869+00:00_

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
  "session": "worker_code_paper_final_polish_20260525T104936",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-25T10:54:10.337186+00:00_

1	
2	\section{Results}
3	\label{sec:results}
4	
5	\subsection{Main Results}
6	\label{sec:main_results}
7	
8	Table~\ref{tab:main_results} summarizes TSR and CAR across conditions (50 rollouts $\times$ 10 tasks per seed). Statistical comparisons use paired $t$-tests and Cohen's $d$ against the Vanilla baseline.
9	
10	\textbf{Crossover interaction between normalization and gradient flow.} The four conditions crossing normalization type (BN/LN) with gradient flow (ON/OFF) reveal a crossover interaction rather than additive effects (Section~\ref{sec:mechanism}). Full OCC with BN maintains CAR comparable to Vanilla (0.797 vs.\ 0.780, $d{=}+0.69$, $p{=}0.44$). Detach OCC with BN falls 3.4\,pp below Vanilla ($p{=}0.031$, $d{=}-3.90$), the only statistically significant pairwise difference. Detach+LN (0.765) recovers 1.9\,pp of this deficit by eliminating BatchNorm interference. However, Full OCC+LN (0.743) consistently degrades CAR by 3.7\,pp below Vanilla despite maintaining gradient flow; this is the worst configuration tested. BN is thus beneficial when gradient flow calibrates its statistics, but harmful when gradient flow is absent; LN shows the opposite pattern. These results are consistent with the hypothesis that label content does not affect outcomes: Random OCC (0.789), Depth (0.780), and Full OCC (0.797) are all within cross-seed variance ($p > 0.4$).
11	
12	\textbf{Detach destabilizes optimization broadly.} Detach OCC exhibits TSR variance an order of magnitude above other conditions ($\sigma = 0.163$ vs.\ $< 0.050$): one seed collapses to TSR 0.624 with uniform degradation across all tasks, while its CAR (0.748) stays comparable to the other two seeds. The low CAR variance ($\sigma = 0.002$) despite volatile TSR ($\sigma = 0.163$) suggests deterministic convergence to a degraded safety behavior: BN interference imposes a consistent representational distortion regardless of initialization.
13	
14	
15	
16	\begin{table}[t]
17	\centering
18	\caption{Overall results
…[truncated 10901 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_paper_final_polish_20260525T104936",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-25T10:54:10.337422+00:00_

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
  "session": "worker_code_paper_final_polish_20260525T104936",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/discussion.tex"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-25T10:54:10.337638+00:00_

1	
2	\section{Discussion}
3	\label{sec:discussion}
4	\label{sec:why_gradient}
5	\label{sec:why_detach}
6	
7	Gradient norms, CKA, normalization ablation, and behavioral metrics converge on a crossover interaction account. BatchNorm and gradient flow are not independent factors with additive effects; they interact (7.3\,pp interaction effect, Table~\ref{tab:factorial}). BN is a context-dependent component: when gradient flow calibrates its running statistics, BN coupling is beneficial (Table~\ref{tab:main_results}, Full OCC); without gradient calibration, BN statistics drift uncompensated, causing catastrophic representational corruption (Detach OCC CKA $\downarrow$0.31--0.54). This is consistent with the known sensitivity of BatchNorm to distribution shift~\cite{ioffe2015batchnorm, li2017adabn, schneider2020bn}, here manifested as a training-time phenomenon rather than the typical train/test discrepancy.
8	
9	The crossover is most striking in the Full OCC+LN result (Table~\ref{tab:factorial}): gradient flow with LayerNorm produces the \emph{worst} safety behavior despite preserving pretrained representations (CKA $\geq$0.95). Same-seed gradient analysis reveals the mechanism: LN redistributes gradient magnitude across backbones, suppressing DINOv2 action gradients 3.5$\times$ while amplifying SigLIP 2.5$\times$ relative to BN, without increasing directional conflict. This cross-backbone gradient redistribution (not representation corruption) explains the CAR degradation, a representation-behavior dissociation where representational fidelity does not predict safety. This rules out the hypothesis that gradient flow provides intrinsic behavioral regularization~\cite{lee2015deeply, pezeshki2021gradient}. Instead, gradient flow benefits are predominantly BN-mediated: BN maintains balanced gradient allocation across encoders (DINOv2: 0.8$\times$, SigLIP: 1.0$\times$ Vanilla norms), a calibration effect that LN disrupts.
10	
11	We observe that under Detach BN, SigLIP drifts
…[truncated 2103 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_paper_final_polish_20260525T104936",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-25T10:54:10.337874+00:00_

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
  "session": "worker_code_paper_final_polish_20260525T104936",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/conclusion.tex"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-25T10:54:10.338068+00:00_

1	
2	\section{Conclusion}
3	\label{sec:conclusion}
4	
5	We presented a systematic factorial study of how auxiliary spatial supervision during VLA fine-tuning affects collision avoidance. The central finding is a crossover interaction between normalization type and gradient flow (7.3\,pp interaction effect, $p{=}0.025$): BatchNorm with gradient flow is the only beneficial configuration, while LayerNorm with gradient flow consistently degrades safety below Vanilla despite preserving pretrained representations, a representation-behavior dissociation. Three label types achieve comparable CAR, consistent with the hypothesis that label content does not affect outcomes. Practical guidelines: maintain BatchNorm with gradient flow; if gradient flow is unavailable, substitute LayerNorm; never combine LayerNorm with gradient flow. No ground-truth labels needed, zero inference cost. Same-seed gradient analysis reveals BN-mediated gradient calibration operates through balanced cross-backbone gradient allocation, which LN disrupts via amplitude redistribution. Open directions include generalization to other VLA architectures and benchmarks, dynamic obstacles, and real-world deployment.
6	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_paper_final_polish_20260525T104936",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-25T10:54:10.338259+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_paper_final_polish_20260525T104936",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-25T10:54:10.338481+00:00_

1	
2	\section{Related Work}
3	\label{sec:related}
4	
5	\subsection{VLA Safety and Spatial Representations}
6	
7	VLA models achieve high task success but remain prone to collisions~\cite{li2026vlasafety}. Two strategies address this gap. Runtime constraint methods add safety layers at inference: AEGIS~\cite{hu2025vlsa} filters actions via a CBF constructed from vision-language obstacle detection, improving CAR by 59pp on SafeLIBERO; CoFreeVLA~\cite{zhai2026cofreevla} trains a collision risk estimator for dual-arm settings; and OGM-CBF~\cite{raja2024ogmcbf} builds CBFs from occupancy grid maps. Training-time methods embed safety into the policy: SafeVLA~\cite{zhang2025safevla} applies constrained RL to reduce safety violations by 84\%. Both strategies treat safety as a behavioral constraint problem without investigating whether the VLA's internal spatial representations contribute to collision avoidance.
8	
9	Separately, a growing body of work injects 3D structure into VLA vision encoders to improve task success. Depth-based methods fuse monocular predictions with visual features~\cite{yuan2025depthvla, li2025qdepthvla, rao2026augvla3d, bhat20253dcavla, abouzeid2025geoaware}, building on foundation models like Depth Anything~\cite{yang2024depthanything}. Alignment-based approaches regularize internal representations: Spatial Forcing~\cite{li2026spatialforcing} aligns VLA embeddings with pretrained 3D features (ICLR 2026); SpatialVLA~\cite{wu2025spatialvla} introduces egocentric 3D position encoding (RSS 2025). Point cloud and geometric methods encode explicit 3D structure~\cite{li2025pointvla, sun2025geovla, wu2026stvla, chen2026gstvla, tu2026sgvla, xiao2026stemvla, li2026corridorvla}. In autonomous driving, OccVLA~\cite{liu2025occvla} uses occupancy prediction as auxiliary VLA supervision, drawing on BEV representations~\cite{li2022bevformer, sima2023occnet, tian2023occ3d}. These spatial methods consistently improve task success but none evaluates collision avoidance
…[truncated 2901 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_paper_final_polish_20260525T104936",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-25T10:54:10.338733+00:00_

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
  "session": "worker_code_paper_final_polish_20260525T104936",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/appendix.tex"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-25T10:54:10.338952+00:00_

1	
2	\section{Extended Per-Task Results}
3	\label{app:per_task}
4	
5	Table~\ref{tab:per_task} reports per-task mean CAR across seeds for each condition. Seven tasks achieve CAR $\geq$ 0.92 under Vanilla, while three physically constrained tasks (T3, T5, T6) fall below 0.58. The overall CAR differences reported in the main text are dominated by these three hard tasks, which average 0.342 compared to 0.968 for the seven easy tasks.
6	
7	\begin{table}[h]
8	\centering
9	\caption{Per-task mean CAR across seeds (50 rollouts per seed). All conditions use 3 seeds except Depth (4). Detach+LN per-task uses 2 seeds (s1, s2; s0 lacks per-task breakdown); 3-seed aggregate is in Table~\ref{tab:main_results}.}
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
33	\textbf{Ceiling effects.} On the seven easy tasks (T0--T2, T4, T7--T9), all conditions achieve CAR $\geq$ 0.89, leaving minimal room for auxiliary training to improve performance. The obstacle is spatially separated from th
…[truncated 7429 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_paper_final_polish_20260525T104936",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-25T10:54:10.339111+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_paper_final_polish_20260525T104936",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/references.bib"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-25T10:54:10.339345+00:00_

1	% References for OccSafe-VLA
2	% Bib key convention: {first_author_surname_lower}{year}{keyword_lower}
3	
4	% ============================================================
5	% VLA Safety
6	% ============================================================
7	
8	@article{hu2025vlsa,
9	  author    = {Songqiao Hu and Zeyi Liu and Shuang Liu and Jun Cen and Zihan Meng and Xiao He},
10	  title     = {{VLSA}: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer},
11	  journal   = {arXiv preprint arXiv:2512.11891},
12	  year      = {2025},
13	  note      = {arXiv:2512.11891}
14	}
15	
16	@inproceedings{zhang2025safevla,
17	  author    = {Borong Zhang and others},
18	  title     = {{SafeVLA}: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning},
19	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
20	  year      = {2025},
21	  note      = {Spotlight. arXiv:2503.03480}
22	}
23	
24	@article{zhai2026cofreevla,
25	  author    = {Xuanran Zhai and others},
26	  title     = {{CoFreeVLA}: Collision-Free Dual-Arm Manipulation via {VLA} Model and Risk Estimation},
27	  journal   = {arXiv preprint arXiv:2601.21712},
28	  year      = {2026},
29	  note      = {arXiv:2601.21712}
30	}
31	
32	
33	@article{li2026vlasafety,
34	  author    = {Li and others},
35	  title     = {Vision-Language-Action Safety: Threats, Challenges, Evaluations, and Mechanisms},
36	  journal   = {arXiv preprint arXiv:2604.23775},
37	  year      = {2026},
38	  note      = {arXiv:2604.23775}
39	}
40	
41	% ============================================================
42	% Safety Mechanisms (barrier functions / occupancy-based safety)
43	% ============================================================
44	
45	
46	@article{raja2024ogmcbf,
47	  author    = {Golnaz Raja and Teemu M{\"o}kk{\"o}nen and Reza Ghabcheloo},
48	  title     = {Safe Robot Control using Occupancy Grid Map-based Control Barrier Function ({OGM-CBF})},
49	  journal   = {arXiv preprint
…[truncated 16327 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_paper_final_polish_20260525T104936",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-25T10:54:10.339519+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -E \"undefined|multiply|Rerun|Warning\" main.log | grep -v \"specifier changed\" | head -40",
  "description": "Check compile log for undefined references and warnings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_paper_final_polish_20260525T104936",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -E \"undefined|multiply|Rerun|Warning\" main.log | grep -v \"specifier changed\" | head -40",
    "description": "Check compile log for undefined references and warnings"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-25T10:54:10.339646+00:00_

Package: rerunfilecheck 2025-06-21 v1.11 Rerun checks for auxiliary files (HO)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_paper_final_polish_20260525T104936",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-25T10:54:10.339810+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -c \"\\\\\\\\todo\" *.tex",
  "description": "Check for remaining \\todo markers"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_paper_final_polish_20260525T104936",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -c \"\\\\\\\\todo\" *.tex",
    "description": "Check for remaining \\todo markers"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-25T10:54:10.339935+00:00_

appendix.tex:0
conclusion.tex:0
discussion.tex:0
experiment_setup.tex:0
experiments.tex:0
experiments_old.tex:0
introduction.tex:0
main.tex:1
method.tex:0
references.tex:0
related_work.tex:0
results.tex:0

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_paper_final_polish_20260525T104936",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-25T10:54:10.340053+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep \"---\" *.tex",
  "description": "Check for em-dash usage"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_paper_final_polish_20260525T104936",
  "tool": "Bash",
  "tool_args": {
    "command": "grep \"---\" *.tex",
    "description": "Check for em-dash usage"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-25T10:54:10.340169+00:00_

Exit code 2
grep: unrecognized option '---'
Usage: grep [OPTION]... PATTERNS [FILE]...
Try 'grep --help' for more information.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_paper_final_polish_20260525T104936",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-25T10:54:10.340284+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "---",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper",
  "glob": "*.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_paper_final_polish_20260525T104936",
  "tool": "Grep",
  "tool_args": {
    "pattern": "---",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper",
    "glob": "*.tex",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-25T10:54:10.340403+00:00_

results.tex:28:Vanilla       & 3 & 0.907 $\pm$ 0.009 & 0.780 $\pm$ 0.012 & [.766, .788] & ---    \\
results.tex:34:Cutoff@15K$^\ddagger$   & 2 & 0.883 $\pm$ 0.041 & 0.782 $\pm$ 0.031 & --- & $+$0.2 \\
results.tex:35:Cutoff@25K$^\ddagger$   & 2 & 0.887 $\pm$ 0.061 & 0.724 $\pm$ 0.051 & --- & $-$5.6 \\
results.tex:37:Cutoff@45K$^\dagger$    & 1 & 0.896 & 0.764 & --- & $-$1.6 \\
results.tex:38:Reverse Cutoff$^\ddagger$ & 2 & 0.839 $\pm$ 0.072 & 0.718 $\pm$ 0.025 & --- & $-$6.2 \\

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_paper_final_polish_20260525T104936",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-25T10:54:10.340523+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\label\\{(fig|tab):",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper",
  "glob": "*.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_paper_final_polish_20260525T104936",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\label\\{(fig|tab):",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper",
    "glob": "*.tex",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-25T10:54:10.340644+00:00_

method.tex:39:\label{tab:ablation_design}
appendix.tex:10:\label{tab:per_task}
appendix.tex:43:\label{tab:hyperparams}
appendix.tex:87:\label{fig:per_layer_combined}
appendix.tex:88:\label{fig:conflict_rate}
appendix.tex:89:\label{fig:grad_norm_heatmap}
appendix.tex:99:\label{fig:dose_response}
introduction.tex:14:\label{fig:overview}
results.tex:19:\label{tab:main_results}
results.tex:55:\label{tab:factorial}
results.tex:72:\label{fig:factorial}
results.tex:82:\label{fig:gradient_analysis}
results.tex:93:\label{fig:cka_analysis}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_paper_final_polish_20260525T104936",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-25T10:54:10.340796+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\ref\\{",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper",
  "glob": "*.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_paper_final_polish_20260525T104936",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\ref\\{",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper",
    "glob": "*.tex",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-25T10:54:10.340939+00:00_

discussion.tex:7:[Omitted long matching line]
discussion.tex:9:[Omitted long matching line]
method.tex:34:Table~\ref{tab:ablation_design} summarizes what each pairwise comparison isolates.
method.tex:60:[Omitted long matching line]
appendix.tex:5:Table~\ref{tab:per_task} reports per-task mean CAR across seeds for each condition. Seven tasks achieve CAR $\geq$ 0.92 under Vanilla, while three physically constrained tasks (T3, T5, T6) fall below 0.58. The overall CAR differences reported in the main text are dominated by these three hard tasks, which average 0.342 compared to 0.968 for the seven easy tasks.
appendix.tex:9:\caption{Per-task mean CAR across seeds (50 rollouts per seed). All conditions use 3 seeds except Depth (4). Detach+LN per-task uses 2 seeds (s1, s2; s0 lacks per-task breakdown); 3-seed aggregate is in Table~\ref{tab:main_results}.}
appendix.tex:79:[Omitted long matching line]
appendix.tex:81:[Omitted long matching line]
appendix.tex:93:[Omitted long matching line]
experiments_old.tex:9:[Omitted long matching line]
experiments_old.tex:30:All conditions share the same base model: OpenVLA-OFT 7B~\cite{kim2025oft}, pre-trained on Open X-Embodiment. We fine-tune with LoRA (rank 32, $\alpha{=}16$) for 50K steps using AdamW (weight decay $0.01$), a batch size of 8, a constant learning rate of $5 \times 10^{-4}$, and 2--4 random seeds per condition (see Table~\ref{tab:main_results}). The LoRA adapter adds 110.8M trainable parameters (1.45\% of 7.65B total).
introduction.tex:8:We present a systematic factorial study isolating how auxiliary spatial supervision during VLA fine-tuning affects collision avoidance. Twelve conditions on OpenVLA-OFT~\cite{kim2024openvla, kim2025oft} with LoRA vary gradient flow, label content, normalization type, spatial reference frame, and temporal extent. Figure~\ref{fig:overview} summarizes the setup and key finding. Our contributions:
introduction.tex:20:    \item \textbf{Factorial decomposition reveals hidden interactions.} P
…[truncated 1724 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_paper_final_polish_20260525T104936",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-25T10:54:10.341078+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -n \"\\\\\\\\ref{fig:\" *.tex | grep -oP \"fig:\\w+\" | sort -u",
  "description": "Extract all fig: references used"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_paper_final_polish_20260525T104936",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -n \"\\\\\\\\ref{fig:\" *.tex | grep -oP \"fig:\\w+\" | sort -u",
    "description": "Extract all fig: references used"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-25T10:54:10.341196+00:00_

fig:cka_analysis
fig:dose_response
fig:factorial
fig:gradient_analysis
fig:overview
fig:per_layer_combined

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_paper_final_polish_20260525T104936",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-25T10:54:10.341309+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -n \"\\\\\\\\ref{tab:\" *.tex | grep -oP \"tab:\\w+\" | sort -u",
  "description": "Extract all tab: references used"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_paper_final_polish_20260525T104936",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -n \"\\\\\\\\ref{tab:\" *.tex | grep -oP \"tab:\\w+\" | sort -u",
    "description": "Extract all tab: references used"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-25T10:54:10.341429+00:00_

tab:ablation_design
tab:factorial
tab:main_results
tab:per_task

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_paper_final_polish_20260525T104936",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-25T10:54:10.341542+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -n \"\\\\\\\\ref{sec:\" *.tex | grep -oP \"sec:\\w+\" | sort -u",
  "description": "Extract all sec: references used"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_paper_final_polish_20260525T104936",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -n \"\\\\\\\\ref{sec:\" *.tex | grep -oP \"sec:\\w+\" | sort -u",
    "description": "Extract all sec: references used"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-25T10:54:10.341655+00:00_

sec:gradient_dynamics
sec:mechanism
sec:why_gradient

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_paper_final_polish_20260525T104936",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-25T10:54:10.341789+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -n \"\\\\\\\\ref{app:\" *.tex | grep -oP \"app:\\w+\" | sort -u",
  "description": "Extract all app: references used"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_paper_final_polish_20260525T104936",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -n \"\\\\\\\\ref{app:\" *.tex | grep -oP \"app:\\w+\" | sort -u",
    "description": "Extract all app: references used"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-25T10:54:10.341902+00:00_

app:per_task
app:temporal
app:training

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_paper_final_polish_20260525T104936",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-25T10:54:10.342012+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -n \"\\\\\\\\label{sec:\" *.tex | grep -oP \"sec:\\w+\" | sort -u",
  "description": "Extract all sec: labels defined"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_paper_final_polish_20260525T104936",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -n \"\\\\\\\\label{sec:\" *.tex | grep -oP \"sec:\\w+\" | sort -u",
    "description": "Extract all sec: labels defined"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-25T10:54:10.342126+00:00_

sec:ablation
sec:conclusion
sec:discussion
sec:evaluation
sec:exp_setup
sec:gradient_dynamics
sec:main_results
sec:mechanism
sec:method
sec:per_task
sec:related
sec:results
sec:temporal
sec:why_detach
sec:why_gradient

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_paper_final_polish_20260525T104936",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-25T10:54:10.342238+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -n \"\\\\\\\\label{app:\" *.tex | grep -oP \"app:\\w+\" | sort -u",
  "description": "Extract all app: labels defined"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_paper_final_polish_20260525T104936",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -n \"\\\\\\\\label{app:\" *.tex | grep -oP \"app:\\w+\" | sort -u",
    "description": "Extract all app: labels defined"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-25T10:54:10.342349+00:00_

app:extended
app:per_task
app:temporal
app:training

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_paper_final_polish_20260525T104936",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-25T10:54:10.342459+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -n \"\\\\\\\\cite{\" *.tex | grep -oP \"(?<=\\\\\\\\cite\\{)[^}]+\" | tr ',' '\\n' | sed 's/^ *//' | sort -u",
  "description": "Extract all citation keys used in tex files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_paper_final_polish_20260525T104936",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -n \"\\\\\\\\cite{\" *.tex | grep -oP \"(?<=\\\\\\\\cite\\{)[^}]+\" | tr ',' '\\n' | sed 's/^ *//' | sort -u",
    "description": "Extract all citation keys used in tex files"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-25T10:54:10.342603+00:00_

abouzeid2025geoaware
bhat20253dcavla
brohan2023rt2
caruana1997multitask
chen2018gradnorm
chen2026gstvla
hu2022lora
hu2025vlsa
ioffe2015batchnorm
kim2024openvla
kim2025oft
kirkpatrick2017ewc
kornblith2019similarity
lee2015deeply
li2017adabn
li2022bevformer
li2025pointvla
li2025qdepthvla
li2026corridorvla
li2026spatialforcing
li2026vlasafety
lin2017focal
lippl2024implicit
liu2021cagrad
liu2023libero
liu2025occvla
navon2022nashmtl
oquab2024dinov2
pezeshki2021gradient
raja2024ogmcbf
rao2026augvla3d
ruder2017overview
schneider2020bn
sima2023occnet
sun2025geovla
tian2023occ3d
tu2026sgvla
wu2025spatialvla
wu2026stvla
xiao2026stemvla
yang2024depthanything
yu2020pcgrad
yuan2025depthvla
zhai2023siglip
zhai2026cofreevla
zhang2025safevla

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_paper_final_polish_20260525T104936",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-25T10:54:10.342749+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -oP \"^@\\w+\\{([^,]+)\" references.bib | sed 's/^@[^{]*{//' | sort -u",
  "description": "Extract all bib entry keys"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_paper_final_polish_20260525T104936",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -oP \"^@\\w+\\{([^,]+)\" references.bib | sed 's/^@[^{]*{//' | sort -u",
    "description": "Extract all bib entry keys"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-25T10:54:10.342883+00:00_

abouzeid2025geoaware
bhat20253dcavla
brohan2023rt2
caruana1997multitask
chen2018gradnorm
chen2026gstvla
hu2022lora
hu2025vlsa
ioffe2015batchnorm
kim2024openvla
kim2025oft
kirkpatrick2017ewc
kornblith2019similarity
lee2015deeply
li2017adabn
li2022bevformer
li2025pointvla
li2025qdepthvla
li2026corridorvla
li2026spatialforcing
li2026vlasafety
lin2017focal
lippl2024implicit
liu2021cagrad
liu2023libero
liu2025occvla
navon2022nashmtl
oquab2024dinov2
pezeshki2021gradient
raja2024ogmcbf
rao2026augvla3d
ruder2017overview
schneider2020bn
sima2023occnet
sun2025geovla
tian2023occ3d
tu2026sgvla
wu2025spatialvla
wu2026stvla
xiao2026stemvla
yang2024depthanything
yu2020pcgrad
yuan2025depthvla
zhai2023siglip
zhai2026cofreevla
zhang2025safevla

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_paper_final_polish_20260525T104936",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-25T10:54:10.343022+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -n \"\\\\\\\\caption\" *.tex",
  "description": "Check all captions for period endings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_paper_final_polish_20260525T104936",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -n \"\\\\\\\\caption\" *.tex",
    "description": "Check all captions for period endings"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-25T10:54:10.343164+00:00_

appendix.tex:9:\caption{Per-task mean CAR across seeds (50 rollouts per seed). All conditions use 3 seeds except Depth (4). Detach+LN per-task uses 2 seeds (s1, s2; s0 lacks per-task breakdown); 3-seed aggregate is in Table~\ref{tab:main_results}.}
appendix.tex:42:\caption{Training hyperparameters.}
appendix.tex:86:\caption{Per-layer gradient analysis decomposed into amplitude and direction. \textbf{Top (a--b):} Action gradient norm heatmap (log scale). Gradient-flow conditions (Vanilla, Full OCC, Random OCC) maintain comparable norms; Detach collapses to 1--13\% of Vanilla across all layers. \textbf{Bottom (c--d):} Gradient conflict rate between action and auxiliary losses. DINOv2 maintains $\sim$50\% conflict (near-orthogonal), while SigLIP late layers drop to 19--25\% (cooperative alignment). Both amplitude and directional patterns are identical for Full OCC and Random OCC, which confirms architectural rather than label-dependent structure.}
appendix.tex:98:\caption{Dose-response: CAR vs.\ OCC gradient flow duration. Filled circles: early-cutoff conditions with all 3 seeds completed; open circles: conditions with $\leq$2 seeds (counts annotated as $n$). Diamond ($\diamond$): Reverse Cutoff (gradient flow restricted to the last 15K steps). Dashed line: Vanilla 3-seed mean; shaded band: $\pm\,$1\,SE. The ``+0.2\%'' annotation marks the Cutoff@15K--Vanilla gap. Intermediate cutoff conditions cluster near Vanilla, while Cutoff@25K and Reverse Cutoff fall substantially below.}
introduction.tex:13:\caption{\textbf{Overview.} \textbf{(a)}~VLA policies deployed in contact-rich environments lack collision awareness; a fine-tuned OpenVLA-OFT achieves 90.7\% task success but only 78.0\% collision avoidance on SafeLIBERO. \textbf{(b)}~We attach an auxiliary occupancy prediction head to the vision encoders; it provides gradient flow during training and is discarded at inference (zero cost). The normalization layer (BN/LN) at the encoder output is a critical design choice. \te
…[truncated 2207 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_paper_final_polish_20260525T104936",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-25T10:54:10.343303+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -n \"\\\\\\\\todo\" main.tex",
  "description": "Check the todo definition in main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_paper_final_polish_20260525T104936",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -n \"\\\\\\\\todo\" main.tex",
    "description": "Check the todo definition in main.tex"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-25T10:54:10.343418+00:00_

14:\newcommand{\todo}[1]{\textcolor{red}{[TODO: #1]}}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_paper_final_polish_20260525T104936",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-25T10:54:10.343535+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -rn \"\\\\\\\\label{sec:why_detach}\" *.tex",
  "description": "Check where sec:why_detach is defined"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_paper_final_polish_20260525T104936",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -rn \"\\\\\\\\label{sec:why_detach}\" *.tex",
    "description": "Check where sec:why_detach is defined"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-25T10:54:10.343647+00:00_

discussion.tex:5:\label{sec:why_detach}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_paper_final_polish_20260525T104936",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-25T10:54:10.343780+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -n \"\\\\\\\\label{app:temporal}\" *.tex",
  "description": "Check where app:temporal is defined"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_paper_final_polish_20260525T104936",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -n \"\\\\\\\\label{app:temporal}\" *.tex",
    "description": "Check where app:temporal is defined"
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-25T10:54:10.343894+00:00_

appendix.tex:92:\label{app:temporal}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_paper_final_polish_20260525T104936",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-25T10:54:10.344006+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -nP \"\\b\\.\\d{3}\" *.tex | head -20",
  "description": "Check for .xxx number format (without leading zero)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_paper_final_polish_20260525T104936",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -nP \"\\b\\.\\d{3}\" *.tex | head -20",
    "description": "Check for .xxx number format (without leading zero)"
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-25T10:54:10.344174+00:00_

appendix.tex:5:Table~\ref{tab:per_task} reports per-task mean CAR across seeds for each condition. Seven tasks achieve CAR $\geq$ 0.92 under Vanilla, while three physically constrained tasks (T3, T5, T6) fall below 0.58. The overall CAR differences reported in the main text are dominated by these three hard tasks, which average 0.342 compared to 0.968 for the seven easy tasks.
appendix.tex:28:\multicolumn{2}{l}{Overall} & 0.780 & 0.797 & 0.789 & 0.746 & 0.765 & 0.780 & 0.779 \\
appendix.tex:70:\textbf{Statistical tests.} Pairwise comparisons against Vanilla use two-tailed paired $t$-tests on per-seed mean CARs with Cohen's $d$ for effect size. With $n{=}3$ seeds, statistical power is limited; we report $p$-values and effect sizes for transparency. Only Detach OCC reaches significance ($p{=}0.031$, $d{=}-3.90$); all gradient-flow conditions show $p > 0.35$.
appendix.tex:79:The Detach+LN ablation replaces BatchNorm2d with LayerNorm in the auxiliary head while retaining \texttt{stop\_gradient}. Results (3 seeds) are reported in Table~\ref{tab:main_results} and analyzed in Section~\ref{sec:why_gradient}. Detach+LN recovers 1.9\,pp of the 3.4\,pp Detach deficit (CAR 0.765 vs.\ Detach 0.746) and fully restores pretrained CKA to Vanilla level (DINOv2: 0.966, SigLIP: 0.960), which confirms that BatchNorm interference accounts for all representational drift. The crossover interaction (Section~\ref{sec:mechanism}) reveals that this recovery is normalization-dependent: Full OCC+LN (gradient flow ON, LayerNorm) achieves CAR 0.743, \emph{below} Detach+LN. This demonstrates that gradient flow benefits are BN-mediated rather than intrinsic.
appendix.tex:93:\textbf{Dose-response: gradient flow duration vs.\ CAR.} Figure~\ref{fig:dose_response} plots CAR against the number of OCC gradient flow steps for the cutoff series (15K--45K, plus Detach at 0K and Full OCC at 50K). Cutoff@15K (2 seeds, CAR 0.782) clusters near Vanilla (0.780), while Cutoff@25K (2 seeds, 0.724) falls substantia
…[truncated 8516 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_paper_final_polish_20260525T104936",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-25T10:54:10.344317+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -nP \"percentage point\" *.tex",
  "description": "Check for \"percentage point\" vs pp usage"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_paper_final_polish_20260525T104936",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -nP \"percentage point\" *.tex",
    "description": "Check for \"percentage point\" vs pp usage"
  }
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-25T10:54:10.344445+00:00_

experiment_setup.tex:19:. LoRA adapters use rank 32, $\alpha = 16$, and no dropout. Each training sample consists of two input frames (\texttt{--num\_images\_in\_input 2}): the current observation and the preceding frame, providing temporal displacement cues. Image augmentation is enabled during training (\texttt{--image\_aug True}), applying random crops and color jitter. Training uses a batch size of 8, a constant learning rate of $5 \times 10^{-4}$, and runs for 50,005 steps with checkpoints saved every 10,000 steps. Each condition is trained with at least 3 random seeds (42, 43, 44); the depth condition uses 4 seeds (42, 43, 44, 45) for additional statistical power given that it is the primary comparison of interest. Evaluation uses 50 rollouts per task per checkpoint to reduce per-task confidence intervals to approximately $\pm$13 percentage points (compared to $\pm$21pp at 20 rollouts).
experiments.tex:19:. LoRA adapters use rank 32, $\alpha = 16$, and no dropout. Each training sample consists of two input frames (\texttt{--num\_images\_in\_input 2}): the current observation and the preceding frame, providing temporal displacement cues. Image augmentation is enabled during training (\texttt{--image\_aug True}), applying random crops and color jitter. Training uses a batch size of 8, a constant learning rate of $5 \times 10^{-4}$, and runs for 50,005 steps with checkpoints saved every 10,000 steps. Each condition is trained with at least 3 random seeds (42, 43, 44); the depth condition uses 4 seeds (42, 43, 44, 45) for additional statistical power given that it is the primary comparison of interest. Evaluation uses 50 rollouts per task per checkpoint to reduce per-task confidence intervals to approximately $\pm$13 percentage points (compared to $\pm$21pp at 20 rollouts).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_paper_final_polish_20260525T104936",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-25T10:54:10.344603+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -n \"Output written\" main.log",
  "description": "Check total page count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_paper_final_polish_20260525T104936",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -n \"Output written\" main.log",
    "description": "Check total page count"
  }
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-25T10:54:10.344742+00:00_

642:Output written on main.pdf (15 pages, 441140 bytes).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_paper_final_polish_20260525T104936",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-25T10:54:10.344860+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -n \"\\\\\\\\clearpage\" main.tex",
  "description": "Check where clearpage is for appendix boundary"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_paper_final_polish_20260525T104936",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -n \"\\\\\\\\clearpage\" main.tex",
    "description": "Check where clearpage is for appendix boundary"
  }
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-25T10:54:10.344974+00:00_

49:\clearpage

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_paper_final_polish_20260525T104936",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 67 · 2026-05-25T10:54:10.345085+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -n \"\\[.*\\]\" main.log | grep -P \"^\\d+:\\[\" | tail -20",
  "description": "Check page numbers in log for section boundaries"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_paper_final_polish_20260525T104936",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -n \"\\[.*\\]\" main.log | grep -P \"^\\d+:\\[\" | tail -20",
    "description": "Check page numbers in log for section boundaries"
  }
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-25T10:54:10.345197+00:00_

420:[Loading MPS to PDF converter (version 2006.09.02).]
575:[6 <./figures/factorial_2x2.pdf>]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_paper_final_polish_20260525T104936",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-25T10:54:10.345308+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -P \"^\\[\" main.log | head -30",
  "description": "Find page breaks in log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_paper_final_polish_20260525T104936",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -P \"^\\[\" main.log | head -30",
    "description": "Find page breaks in log"
  }
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-25T10:54:10.345418+00:00_

[Loading MPS to PDF converter (version 2006.09.02).]
[1
[6 <./figures/factorial_2x2.pdf>]
[13

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_paper_final_polish_20260525T104936",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 71 · 2026-05-25T10:54:10.345527+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -oP \"\\[\\d+\\]\" main.log | sort -u",
  "description": "Find all page numbers mentioned in log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_paper_final_polish_20260525T104936",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -oP \"\\[\\d+\\]\" main.log | sort -u",
    "description": "Find all page numbers mentioned in log"
  }
}
```

</details>

---

### Tool result

_source line 72 · 2026-05-25T10:54:10.345702+00:00_

[10]
[11]
[12]
[14]
[3]
[4]
[5]
[9]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_paper_final_polish_20260525T104936",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 73 · 2026-05-25T10:54:10.345836+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -n \"conclusion\\|appendix\\|clearpage\\|bibliography\" main.log",
  "description": "Check where conclusion/appendix appear in log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_paper_final_polish_20260525T104936",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -n \"conclusion\\|appendix\\|clearpage\\|bibliography\" main.log",
    "description": "Check where conclusion/appendix appear in log"
  }
}
```

</details>

---

### Tool result

_source line 74 · 2026-05-25T10:54:10.345951+00:00_

585:s/cka_analysis.pdf>]) (./conclusion.tex) (./main.bbl [9] [10] [11]) [12] (./app

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_paper_final_polish_20260525T104936",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 75 · 2026-05-25T10:54:10.346064+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -nP \"\\(\\./conclusion|\\(\\./appendix|\\(\\./main\\.bbl\" main.log",
  "description": "Check file includes in log to identify page boundaries"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_paper_final_polish_20260525T104936",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -nP \"\\(\\./conclusion|\\(\\./appendix|\\(\\./main\\.bbl\" main.log",
    "description": "Check file includes in log to identify page boundaries"
  }
}
```

</details>

---

### Tool result

_source line 76 · 2026-05-25T10:54:10.346177+00:00_

585:s/cka_analysis.pdf>]) (./conclusion.tex) (./main.bbl [9] [10] [11]) [12] (./app

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_paper_final_polish_20260525T104936",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 77 · 2026-05-25T10:54:10.346289+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -P \"\\(\\./|^\\[\" main.log | grep -v \"Loading\"",
  "description": "Trace file includes and page numbers"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_paper_final_polish_20260525T104936",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -P \"\\(\\./|^\\[\" main.log | grep -v \"Loading\"",
    "description": "Trace file includes and page numbers"
  }
}
```

</details>

---

### Tool result

_source line 78 · 2026-05-25T10:54:10.346405+00:00_

(./main.tex
(./corl_2026.sty
(./main.aux)
(./main.out) (./main.out)
) (./introduction.tex
[1
) (./related_work.tex [2 <./figures/fig1_overview.pdf>]) (./method.tex [3]
) [4] (./results.tex
[6 <./figures/factorial_2x2.pdf>]
 [7 <./figures/gradient_analysis_combined.pdf>]) (./discussion.tex [8 <./figure
s/cka_analysis.pdf>]) (./conclusion.tex) (./main.bbl [9] [10] [11]) [12] (./app
[13
(./main.aux)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_paper_final_polish_20260525T104936",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 79 · 2026-05-25T10:54:10.346655+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex",
  "old_string": "Full OCC (BN)      & 3 & 0.894 $\\pm$ 0.050 & \\textbf{0.797} $\\pm$ 0.032 & [.770, .832] & $+$1.7 \\\\\nRandom OCC (BN)    & 3 & 0.869 $\\pm$ 0.029 & 0.789 $\\pm$ 0.031 & [.754, .814] & $+$0.9 \\\\\nVanilla       & 3 & 0.907 $\\pm$ 0.009 & 0.780 $\\pm$ 0.012 & [.766, .788] & ---    \\\\\nDetach+LN     & 3 & 0.901 $\\pm$ 0.016 & 0.765 $\\pm$ 0.023 & [.748, .792] & $-$1.5 \\\\\nDetach OCC (BN)$^*$    & 3 & 0.812 $\\pm$ 0.163 & 0.746 $\\pm$ 0.002 & [.744, .748] & $-$3.4 \\\\\nFull OCC+LN   & 3 & 0.897 $\\pm$ 0.032 & 0.743 $\\pm$ 0.024 & [.718, .766] & $-$3.7 \\\\\n\\midrule\nDepth             & 4 & 0.889 $\\pm$ 0.042 & 0.780 $\\pm$ 0.039 & [.747, .812] & 0.0 \\\\",
  "new_string": "Full OCC (BN)      & 3 & 0.894 $\\pm$ 0.050 & \\textbf{0.797} $\\pm$ 0.032 & [0.770, 0.832] & $+$1.7 \\\\\nRandom OCC (BN)    & 3 & 0.869 $\\pm$ 0.029 & 0.789 $\\pm$ 0.031 & [0.754, 0.814] & $+$0.9 \\\\\nVanilla       & 3 & 0.907 $\\pm$ 0.009 & 0.780 $\\pm$ 0.012 & [0.766, 0.788] & ---    \\\\\nDetach+LN     & 3 & 0.901 $\\pm$ 0.016 & 0.765 $\\pm$ 0.023 & [0.748, 0.792] & $-$1.5 \\\\\nDetach OCC (BN)$^*$    & 3 & 0.812 $\\pm$ 0.163 & 0.746 $\\pm$ 0.002 & [0.744, 0.748] & $-$3.4 \\\\\nFull OCC+LN   & 3 & 0.897 $\\pm$ 0.032 & 0.743 $\\pm$ 0.024 & [0.718, 0.766] & $-$3.7 \\\\\n\\midrule\nDepth             & 4 & 0.889 $\\pm$ 0.042 & 0.780 $\\pm$ 0.039 & [0.747, 0.812] & 0.0 \\\\"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_paper_final_polish_20260525T104936",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex",
    "old_string": "Full OCC (BN)      & 3 & 0.894 $\\pm$ 0.050 & \\textbf{0.797} $\\pm$ 0.032 & [.770, .832] & $+$1.7 \\\\\nRandom OCC (BN)    & 3 & 0.869 $\\pm$ 0.029 & 0.789 $\\pm$ 0.031 & [.754, .814] & $+$0.9 \\\\\nVanilla       & 3 & 0.907 $\\pm$ 0.009 & 0.780 $\\pm$ 0.012 & [.766, .788] & ---    \\\\\nDetach+LN     & 3 & 0.901 $\\pm$ 0.016 & 0.765 $\\pm$ 0.023 & [.748, .792] & $-$1.5 \\\\\nDetach OCC (BN)$^*$    & 3 & 0.812 $\\pm$ 0.163 & 0.746 $\\pm$ 0.002 & [.744, .748] & $-$3.4 \\\\\nFull OCC+LN   & 3 & 0.897 $\\pm$ 0.032 & 0.743 $\\pm$ 0.024 & [.718, .766] & $-$3.7 \\\\\n\\midrule\nDepth             & 4 & 0.889 $\\pm$ 0.042 & 0.780 $\\pm$ 0.039 & [.747, .812] & 0.0 \\\\",
    "new_string": "Full OCC (BN)      & 3 & 0.894 $\\pm$ 0.050 & \\textbf{0.797} $\\pm$ 0.032 & [0.770, 0.832] & $+$1.7 \\\\\nRandom OCC (BN)    & 3 & 0.869 $\\pm$ 0.029 & 0.789 $\\pm$ 0.031 & [0.754, 0.814] & $+$0.9 \\\\\nVanilla       & 3 & 0.907 $\\pm$ 0.009 & 0.780 $\\pm$ 0.012 & [0.766, 0.788] & ---    \\\\\nDetach+LN     & 3 & 0.901 $\\pm$ 0.016 & 0.765 $\\pm$ 0.023 & [0.748, 0.792] & $-$1.5 \\\\\nDetach OCC (BN)$^*$    & 3 & 0.812 $\\pm$ 0.163 & 0.746 $\\pm$ 0.002 & [0.744, 0.748] & $-$3.4 \\\\\nFull OCC+LN   & 3 & 0.897 $\\pm$ 0.032 & 0.743 $\\pm$ 0.024 & [0.718, 0.766] & $-$3.7 \\\\\n\\midrule\nDepth             & 4 & 0.889 $\\pm$ 0.042 & 0.780 $\\pm$ 0.039 & [0.747, 0.812] & 0.0 \\\\"
  }
}
```

</details>

---

### Tool result

_source line 80 · 2026-05-25T10:54:10.346912+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_paper_final_polish_20260525T104936",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 81 · 2026-05-25T10:54:10.347057+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex",
  "old_string": "Cutoff@35K        & 3 & 0.933 $\\pm$ 0.032 & 0.779 $\\pm$ 0.017 & [.768, .798] & $-$0.1 \\\\",
  "new_string": "Cutoff@35K        & 3 & 0.933 $\\pm$ 0.032 & 0.779 $\\pm$ 0.017 & [0.768, 0.798] & $-$0.1 \\\\"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_paper_final_polish_20260525T104936",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex",
    "old_string": "Cutoff@35K        & 3 & 0.933 $\\pm$ 0.032 & 0.779 $\\pm$ 0.017 & [.768, .798] & $-$0.1 \\\\",
    "new_string": "Cutoff@35K        & 3 & 0.933 $\\pm$ 0.032 & 0.779 $\\pm$ 0.017 & [0.768, 0.798] & $-$0.1 \\\\"
  }
}
```

</details>

---

### Tool result

_source line 82 · 2026-05-25T10:54:10.347231+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_paper_final_polish_20260525T104936",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 83 · 2026-05-25T10:54:10.347359+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex",
  "old_string": "four conditions: Vanilla, Full OCC, Detach+BN, Full OCC+LN",
  "new_string": "four conditions: Vanilla, Full OCC, Detach OCC, Full OCC+LN"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_paper_final_polish_20260525T104936",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex",
    "old_string": "four conditions: Vanilla, Full OCC, Detach+BN, Full OCC+LN",
    "new_string": "four conditions: Vanilla, Full OCC, Detach OCC, Full OCC+LN"
  }
}
```

</details>

---

### Tool result

_source line 84 · 2026-05-25T10:54:10.347524+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_paper_final_polish_20260525T104936",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 85 · 2026-05-25T10:54:10.347650+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/related_work.tex",
  "old_string": "improving CAR by 59pp on SafeLIBERO",
  "new_string": "improving CAR by 59\\,pp on SafeLIBERO"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_paper_final_polish_20260525T104936",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/related_work.tex",
    "old_string": "improving CAR by 59pp on SafeLIBERO",
    "new_string": "improving CAR by 59\\,pp on SafeLIBERO"
  }
}
```

</details>

---

### Tool result

_source line 86 · 2026-05-25T10:54:10.347823+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/related_work.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_paper_final_polish_20260525T104936",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 87 · 2026-05-25T10:54:10.347959+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "pdflatex -interaction=nonstopmode main.tex 2>&1 | tail -5 && bibtex main 2>&1 | tail -3 && pdflatex -interaction=nonstopmode main.tex 2>&1 | tail -3 && pdflatex -interaction=nonstopmode main.tex 2>&1 | tail -5",
  "description": "Recompile paper after fixes",
  "timeout": "120000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_paper_final_polish_20260525T104936",
  "tool": "Bash",
  "tool_args": {
    "command": "pdflatex -interaction=nonstopmode main.tex 2>&1 | tail -5 && bibtex main 2>&1 | tail -3 && pdflatex -interaction=nonstopmode main.tex 2>&1 | tail -3 && pdflatex -interaction=nonstopmode main.tex 2>&1 | tail -5",
    "description": "Recompile paper after fixes",
    "timeout": "120000"
  }
}
```

</details>

---

### Tool result

_source line 88 · 2026-05-25T10:54:10.348086+00:00_

ts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/ti
mes/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb
>
Output written on main.pdf (15 pages, 441168 bytes).
Transcript written on main.log.
The top-level auxiliary file: main.aux
The style file: corlabbrvnat.bst
Database file #1: references.bib
>
Output written on main.pdf (15 pages, 441168 bytes).
Transcript written on main.log.
ts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/ti
mes/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb
>
Output written on main.pdf (15 pages, 441168 bytes).
Transcript written on main.log.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_paper_final_polish_20260525T104936",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 89 · 2026-05-25T10:54:10.348261+00:00_

编译通过，15 页不变。

---

## Final Polish 报告

### 已修复

| # | 文件 | 问题 | 修复 |
|---|------|------|------|
| 1 | results.tex Table 1 | CI 值缺少前导零 (`[.770, .832]`) | → `[0.770, 0.832]`（共 8 处） |
| 2 | results.tex L81 | fig:gradient_analysis caption 中 "Detach+BN" 与全文术语不一致 | → "Detach OCC" |
| 3 | related_work.tex L7 | "59pp" 缺少 thin space | → `59\,pp` |

### 需要确认（不自动修复）

**P1 — 检查 fig:gradient_analysis caption 与图的一致性**
Caption 写 "four conditions: Vanilla, Full OCC, Detach OCC, Full OCC+LN"，但 panel (a) 和 (c) 的描述还提到了 Random OCC。如果图中确实显示 5 个 condition，应改 "four" → "five" 并补 Random OCC 到列表中。

**P2 — 页数恰好 8 页**
主文（Abstract→Conclusion）结束于第 8 页底部，Bibliography 从第 9 页开始，Appendix 从第 12 页开始。正好踩在 CoRL 8-page 限制上，任何新增内容都会超页。

### 无问题项（已验证通过）

- **\ref / \cite 完整性**: 无 undefined reference、无 undefined citation。所有 46 个 bib 条目都被引用，所有引用都有对应 bib 条目。
- **Figure/Table 编号**: 所有 `\label{fig:...}` 和 `\label{tab:...}` 至少被 `\ref` 引用一次。
- **Appendix 交叉引用**: `\ref{app:per_task}`, `\ref{app:temporal}`, `\ref{app:training}` 均正确指向 Appendix 中的对应 label。
- **\todo{} 残留**: 仅 main.tex 有 `\newcommand{\todo}` 定义，无实际使用。
- **Em-dash**: 无 `---` 在正文中出现（Table 1 中 `---` 是缺失值标记，符合惯例）。
- **Caption 句号**: 所有 11 个 caption 均以句号结尾。
- **术语一致性**: BN/BatchNorm/BatchNorm2d 按 shorthand/prose/code 分层使用，一致。pp 全文统一使用 `\,pp` 格式。
- **数字格式**: 全文使用 `0.xxx` 格式（CI 已修复）。
- **数学公式**: 格式一致，无问题。

### 低优先级备注

- `\todo` 命令定义可在 camera-ready 时删除
- 目录中有未使用的 .tex 文件（experiment_setup.tex, experiments.tex, experiments_old.tex）
- "pp" 全文未展开为 "percentage points"——在 ML 论文中常见，但部分 reviewer 可能偏好首次展开

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_code_paper_final_polish_20260525T104936"
}
```

</details>

---
