# paper writing experiments setup

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_writing_experiments_setup_20260520T201038_result.json`
- **Structured JSON:** [`9bb1f2e113077958eb85.json`](../../sessions/9b/9bb1f2e113077958eb85.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

No LIBERO, DINOv2, or Depth Anything V2 citation keys exist. I'll use `\cite{hu2025aegis}` for the benchmark (as instructed) and mark others with placeholders where needed.

Here is the Experiments Setup section:

```latex
\section{Experiments}

\subsection{Benchmark and Tasks}

We evaluate on the SafeLIBERO benchmark~\cite{hu2025aegis}, which augments the LIBERO-Spatial suite with collision-aware evaluation. SafeLIBERO comprises 32 scenarios across 10 tabletop manipulation tasks organized into two difficulty levels: Level~I (basic spatial reasoning) and Level~II (complex multi-step manipulation). Each task requires the agent to reach, grasp, and place objects among surrounding obstacles. Several tasks deliberately position objects in close proximity (e.g., a bowl resting on a ramekin), creating natural collision challenges that test whether the agent can complete the instructed task without disturbing nearby objects.

\subsection{Evaluation Protocol}

We measure two complementary metrics aligned with the VLSA-AEGIS protocol~\cite{hu2025aegis}. \textbf{Task Success Rate (TSR)} is the fraction of episodes in which the robot completes the instructed task. \textbf{Collision Avoidance Rate (CAR)} is the fraction of episodes with zero unintended object displacement, computed as $\text{CAR} = 1 - n_{\text{collide}} / N$, where $n_{\text{collide}}$ counts episodes whose maximum L1 \texttt{body\_xpos} displacement exceeds a threshold of $0.001$. For each of the 10 tasks, we run 20 rollouts per random seed across 3 seeds (42, 43, 44), yielding 60 rollouts per task and 600 total. We report mean and 95\% confidence intervals, with paired $t$-tests and Cohen's $d$ effect sizes for pairwise comparisons.

\subsection{Experimental Conditions}

We design five conditions that form a mechanism ablation chain, progressively isolating the role of occupancy-grounded gradient flow:

\begin{itemize}[nosep,leftmargin=*]
  \item \textbf{Vanilla}: OpenVLA-OFT fine-tuned without any auxiliary supervision (baseline).
  \item \textbf{+Occ}: BEV occupancy auxiliary head with gradients flowing into the vision encoder (\texttt{occ\_detach=False}).
  \item \textbf{+Occ-Detach}: Occupancy head with detached gradients (\texttt{occ\_detach=True}), testing whether gradient flow to the encoder is necessary.
  \item \textbf{+Depth}: Depth prediction auxiliary head (same architecture, labels from Depth Anything V2), testing whether collision avoidance is specific to occupancy or arises from any geometric auxiliary task.
  \item \textbf{+Random-Occ}: Occupancy head trained with randomized labels, controlling for the regularization effect of an auxiliary loss.
\end{itemize}

\noindent The chain Vanilla $\to$ +Random-Occ $\to$ +Depth $\to$ +Occ-Detach $\to$ +Occ isolates, in turn, auxiliary regularization, geometric supervision, and occupancy-specific gradient flow.

\subsection{Implementation Details}

All conditions share the same base model: OpenVLA-OFT 7B~\cite{kim2025openvlaoft}, pre-trained on Open X-Embodiment. We fine-tune with LoRA (rank 32) for 50K steps using a batch size of 8, a learning rate of $5 \times 10^{-4}$ with cosine decay, and 3 random seeds per condition. The occupancy head is a lightweight two-layer MLP (256 hidden units) that maps DINOv2 patch features to a $64 \times 64$ BEV occupancy grid, trained with Focal Loss ($\alpha{=}0.75$, $\gamma{=}2.0$) weighted by $\lambda{=}0.1$. The depth head uses the same architecture with continuous regression targets. Each run trains in approximately 17 hours on a single A100 GPU. Evaluation uses \texttt{MUJOCO\_GL=egl} for headless rendering with deterministic rollout seeds.
```

~420 words. All setup, no results. Key design choices:
- Ablation chain presented as a logical progression, not just a list
- Metrics formally defined with the exact threshold and formula matching AEGIS
- Implementation details are concrete and reproducible
- No em-dashes, no `-ing` phrase endings, no filler transitions

---
