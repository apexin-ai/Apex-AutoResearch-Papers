# paper writing method

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_writing_method_20260520T201415_result.json`
- **Structured JSON:** [`4d9c7cf5a459974a8062.json`](../../sessions/4d/4d9c7cf5a459974a8062.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```latex
\section{Method}

We present OccSafe-VLA, a framework that injects 3D spatial awareness into Vision-Language-Action (VLA) models through auxiliary Bird's-Eye-View (BEV) occupancy supervision. Section~\ref{sec:problem} formalizes the problem. Section~\ref{sec:occ_head} introduces the BEV occupancy auxiliary head. Section~\ref{sec:training} describes the joint training pipeline. Section~\ref{sec:occ_cbf} presents the Occupancy-Conditioned Control Barrier Function (OCC-CBF) for explicit safety enforcement.

\subsection{Problem Formulation}
\label{sec:problem}

A VLA policy $\pi_\theta$ maps a visual observation $o_t$ and a language instruction $l$ to an action $a_t \in \mathbb{R}^7$, where the seven dimensions encode the delta end-effector pose: 3D position, 3D rotation, and a scalar gripper command. Standard VLA fine-tuning optimizes a single action prediction objective:
\begin{equation}
\label{eq:action_loss}
\mathcal{L}_{\text{action}} = \|a_t - \hat{a}_t\|_1,
\end{equation}
where $\hat{a}_t = \pi_\theta(o_t, l)$ is the predicted action. This objective encourages the model to learn a semantic-action mapping from visual observations and language, but it provides no explicit incentive to understand 3D spatial boundaries between objects.

Safe manipulation requires jointly maximizing two objectives: Task Success Rate (TSR) and Collision Avoidance Rate (CAR). Modern VLA architectures such as OpenVLA-OFT~\cite{kim2025openvlaoft} employ 2D pretrained vision encoders (SigLIP for semantic features, DINOv2 for spatial features) that produce effective action predictions yet lack volumetric scene understanding. Consequently, the resulting policies frequently collide with surrounding objects during manipulation.

Our key insight is that auxiliary BEV occupancy supervision during fine-tuning forces the vision encoder to develop 3D spatial representations, without modifying the action prediction pipeline or incurring any inference overhead.

\subsection{BEV Occupancy Auxiliary Head}
\label{sec:occ_head}

We attach a lightweight auxiliary head to the DINOv2 vision encoder branch that predicts a BEV occupancy grid from patch-level features. This head is active only during training; at inference time, it is discarded entirely, preserving the original model's computational cost.

\paragraph{Architecture.} The DINOv2 encoder produces patch features $z_{\text{patch}} \in \mathbb{R}^{N \times d}$, where $N$ is the number of patches and $d$ is the feature dimension. The occupancy head $f_{\text{occ}}$ is a two-layer MLP with 256 hidden units and ReLU activation that maps these features to a $64 \times 64$ BEV occupancy grid:
\begin{equation}
\label{eq:occ_pred}
\hat{y}_{\text{occ}} = f_{\text{occ}}(z_{\text{patch}}), \quad z_{\text{patch}} = \text{DINOv2}(o_t).
\end{equation}

\paragraph{BEV Grid.} The BEV grid discretizes the top-down view of the workspace into a $64 \times 64$ binary grid, where each cell is labeled as either free or occupied. Ground-truth labels are generated offline from MuJoCo simulator body positions by rasterizing object bounding volumes onto the grid plane. These labels are available only during training since they require privileged simulator access.

\paragraph{Loss Function.} Because the majority of cells in a typical workspace are free, we use Focal Loss~\cite{lin2017focal} to handle the class imbalance:
\begin{equation}
\label{eq:occ_loss}
\mathcal{L}_{\text{occ}} = \text{FL}(\hat{y}_{\text{occ}}, y_{\text{occ}};\, \alpha{=}0.75,\, \gamma{=}2.0),
\end{equation}
where $\alpha$ controls the class weighting and $\gamma$ modulates the focusing effect on hard examples.

\paragraph{Design Choices.} Three decisions shape the effectiveness of the auxiliary head:

\textit{(1) Branching from DINOv2, not SigLIP.} OpenVLA-OFT uses a dual vision encoder: SigLIP for semantic features and DINOv2 for spatial and geometric features. We attach the occupancy head to DINOv2 because its self-supervised pre-training yields patch features that carry richer geometric structure, making them more suitable for learning volumetric spatial layouts.

\textit{(2) Zero inference overhead.} The occupancy head serves purely as an auxiliary training signal. At deployment, the entire MLP is discarded, so the model retains the same architecture and latency as the baseline.

\textit{(3) Gradient flow to the vision encoder.} The occupancy loss $\mathcal{L}_{\text{occ}}$ backpropagates through $f_{\text{occ}}$ into the DINOv2 encoder (\texttt{occ\_detach=False}). This is the core mechanism: gradients from the occupancy objective reshape the patch features to encode 3D spatial structure, which in turn improves the downstream action predictions. When gradients are detached (\texttt{occ\_detach=True}), the encoder receives no spatial learning signal, and collision avoidance does not improve (Section~\ref{sec:experiments}).

\subsection{Training Pipeline}
\label{sec:training}

OccSafe-VLA fine-tunes the base OpenVLA-OFT model with a joint objective that combines the standard action prediction loss with the occupancy auxiliary loss:
\begin{equation}
\label{eq:total_loss}
\mathcal{L}_{\text{total}} = \mathcal{L}_{\text{action}} + \lambda \cdot \mathcal{L}_{\text{occ}},
\end{equation}
where $\lambda = 0.1$ balances the two terms. The action loss preserves the semantic-action mapping learned during pre-training, while the occupancy loss injects 3D spatial awareness into the shared vision encoder.

\paragraph{Gradient Flow.} Two gradient pathways converge at the vision encoder during training. The action pathway flows from $\mathcal{L}_{\text{action}}$ through the action head, the LLM backbone, and into the vision encoder, maintaining the standard VLA learning signal. The occupancy pathway flows from $\mathcal{L}_{\text{occ}}$ through the occupancy MLP directly into the DINOv2 patch features and their associated LoRA weights. The confluence of these two signals at the vision encoder is what enables the model to learn spatial-aware features that serve both accurate manipulation and collision avoidance.

\paragraph{Base Configuration.} We follow the OpenVLA-OFT fine-tuning recipe~\cite{kim2025openvlaoft}: LoRA with rank 32, L1 regression loss with action tokenization, a learning rate of $5 \times 10^{-4}$ with cosine decay, batch size 8, and training for 50K steps across 3 random seeds per condition.

\paragraph{Data.} The training data consists of approximately 25K demonstration episodes from LIBERO-Spatial~\cite{liu2024libero}. Occupancy labels are generated offline by rasterizing MuJoCo body positions to BEV grids, requiring no additional human annotation effort.

\subsection{Occupancy-Conditioned Control Barrier Function}
\label{sec:occ_cbf}

The implicit safety induced by occupancy supervision provides a first line of defense. We complement it with an explicit safety layer: the Occupancy-Conditioned Control Barrier Function (OCC-CBF), which constrains actions at test time using the learned spatial representations.

\paragraph{Background.} Standard CBF-based safety filters, such as the AEGIS framework~\cite{hu2025aegis}, define a barrier function $h(x) = \min_v \|x_{\text{robot}} - v_{\text{obstacle}}\|$ based on Euclidean distances to detected obstacles. This formulation is inherently reactive: the barrier responds to proximity after the robot has already approached an obstacle.

\paragraph{OCC-CBF Formulation.} We propose a barrier function conditioned on the learned occupancy features:
\begin{equation}
\label{eq:occ_cbf}
h_{\text{occ}}(x) = g_\phi(z_{\text{occ}}, x_{\text{robot}}),
\end{equation}
where $z_{\text{occ}}$ denotes the intermediate occupancy features extracted from the DINOv2 encoder, and $g_\phi$ is a lightweight MLP with spectral normalization that enforces Lipschitz continuity, a requirement for valid CBF certificates~\cite{ji2024ogmcbf}. The features $z_{\text{occ}}$ encode the volumetric free-space structure of the scene, including occluded regions and multi-object spatial relationships that point-based distance metrics cannot capture. The function $g_\phi$ is trained on collision labels derived from training rollouts, requiring no additional annotation.

\paragraph{Safety-Constrained Action Correction.} At inference, the OCC-CBF filters the VLA output through a quadratic program (QP):
\begin{equation}
\label{eq:qp}
a^* = \arg\min_{a'} \|a' - \hat{a}_t\|^2 \quad \text{s.t.} \quad \dot{h}_{\text{occ}}(x) + \alpha \cdot h_{\text{occ}}(x) \geq 0,
\end{equation}
where $\alpha > 0$ controls the conservativeness of the safety constraint. The correction is minimal: the QP finds the closest safe action to the VLA prediction, preserving task performance while enforcing spatial safety.

\paragraph{Reactive vs.\ Anticipatory.} The key distinction from AEGIS~\cite{hu2025aegis} lies in the information available to the barrier function. AEGIS computes distances from detected object positions and applies corrections after proximity is detected. OCC-CBF reasons over volumetric occupancy features that encode free-space geometry, enabling anticipatory avoidance before the robot enters a dangerous region. In sparse scenes, the correction budget remains large and OCC-CBF intervenes rarely; in cluttered scenes with tight clearances, it provides stronger corrections.

The complete OCC-CBF implementation and ablation results will be presented in Section~\ref{sec:experiments}. \textit{[Results pending OCC-CBF PoC completion.]}
```

Method section complete. Key design decisions in the writing:

- Symbols and terminology match `experiments.tex` exactly (TSR, CAR, `occ_detach`, $\lambda{=}0.1$, $\alpha{=}0.75$, $\gamma{=}2.0$, LoRA rank 32, 50K steps, batch 8, lr $5\times10^{-4}$, $64\times64$ BEV grid, Focal Loss).
- Six labeled equations for the core formulations.
- No em-dashes, no -ing phrase endings, no "notably"/"furthermore"/"moreover" chains.
- §3.4 OCC-CBF is written as a conceptual description with a pending-results note, as requested.
- Approximately 1200 words across the four subsections.

---
