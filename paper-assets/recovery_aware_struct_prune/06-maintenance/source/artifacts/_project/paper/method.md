# Method

## 3.1 Overview

We study the interaction between structural pruning decisions and post-pruning recovery paradigms in reasoning LLMs. Our methodology has three components: (1) Recovery-Aware Structural Pruning (RASP), a scoring function that incorporates functional redundancy into pruning decisions; (2) a two-stage recovery pipeline (SFT warmup followed by GRPO alignment); and (3) a collapse diagnostic framework that uses GRPO training dynamics to reveal structural damage patterns. Figure 1 illustrates the overall framework.

## 3.2 Recovery-Aware Structural Pruning (RASP)

### Scoring Function

RASP assigns each structural group (attention head or MLP intermediate group) a composite score that balances structural importance against functional uniqueness. For a structural group $h$ in layer $l$, the score is:

$$S(h) = I(h) \times (1 - F(h))^{\alpha}$$

where $I(h)$ denotes the structural importance of group $h$, $F(h)$ denotes the functional overlap of $h$ with other groups in the same layer, and $\alpha \geq 0$ controls the weight placed on functional uniqueness. Groups with the lowest scores are pruned first.

**Structural Importance $I(h)$.**  We compute importance via first-order Taylor expansion over a calibration set of reasoning traces. Given input-output pairs $(x, y)$ from the calibration set, the importance of group $h$ is:

$$I(h) = \left| \sum_{(x,y) \in \mathcal{D}_{\text{cal}}} \frac{\partial \mathcal{L}(x, y)}{\partial h} \cdot h \right|$$

This measures the expected change in loss when group $h$ is removed, approximated to first order.

**Functional Overlap $F(h)$.**  We quantify redundancy using Centered Kernel Alignment (CKA; Kornblith et al., 2019) computed between group $h$ and all other groups within the same layer. Given activation matrices $X_h, X_{h'}$ collected over the calibration set, the linear CKA between groups $h$ and $h'$ is:

$$\text{CKA}(h, h') = \frac{\|X_h^T X_{h'}\|_F^2}{\|X_h^T X_h\|_F \cdot \|X_{h'}^T X_{h'}\|_F}$$

The functional overlap for group $h$ is the mean CKA with all other groups in its layer:

$$F(h) = \frac{1}{|G_l| - 1} \sum_{h' \in G_l \setminus \{h\}} \text{CKA}(h, h')$$

where $G_l$ is the set of structural groups in layer $l$.

### Scoring Interpretation

The factor $(1 - F(h))^{\alpha}$ penalizes functionally unique groups (low $F(h)$, so $(1-F)$ is large) relative to redundant ones (high $F(h)$, so $(1-F)$ is small). When $\alpha = 0$, RASP reduces to importance-only scoring (Standard pruning). As $\alpha$ increases, RASP preferentially preserves unique structures and removes redundant ones. The default is $\alpha = 1.0$.

### Pruning Procedure

We apply structured pruning at the granularity of GQA-aware attention head groups and MLP intermediate neuron groups. Given a target sparsity ratio $s$, we compute $S(h)$ for all groups across all layers, enforce a per-layer capacity floor (minimum 50% retention per layer to prevent layer collapse), rank groups globally by score, and remove the lowest-scoring groups until the target parameter reduction is reached.

## 3.3 Two-Stage Recovery Pipeline

### Stage 1: SFT Warmup

After pruning, the model loses coherent generation ability (EOS rate drops below 5% at 20% sparsity). We restore basic reasoning format through supervised fine-tuning on GSM8K training data (7,473 examples). Training runs for 2 epochs with learning rate $2 \times 10^{-5}$, batch size 1, gradient accumulation 8 steps, and cosine learning rate schedule. This stage restores output format and partial reasoning ability within approximately 35 minutes on 2 RTX PRO 6000 GPUs.

### Stage 2: GRPO Alignment

Following SFT, we apply Group Relative Policy Optimization (GRPO; Shao et al., 2024) to test whether reinforcement learning from verifiable rewards (RLVR) can further improve reasoning accuracy. GRPO generates $G=8$ completions per prompt, scores them against a verifiable answer, and optimizes the policy using group-relative advantages. Key hyperparameters: learning rate $1 \times 10^{-6}$, KL penalty coefficient $\beta = 0.01$, sampling temperature 0.4, repetition penalty 1.15, format reward weight 0.1, maximum completion length 1024 tokens, 8-bit AdamW optimizer, and 100 training steps. We save checkpoints every 5 steps to capture fine-grained training dynamics.

## 3.4 Collapse Diagnostic Framework

We introduce three metrics to characterize GRPO training stability:

1. **Fraction of zero-standard-deviation completions (frac\_zero\_std):** For each prompt, we compute the standard deviation of rewards across $G$ completions. When all completions receive identical rewards, the group provides zero gradient signal. frac\_zero\_std measures the proportion of prompts in each batch where this occurs. Values above 0.8 indicate severe policy collapse.

2. **Gradient norm:** The L2 norm of parameter gradients at each step. A sustained drop below 0.01 signals that the model has converged to a degenerate policy.

3. **Mean terminated completion length:** The average length of completions that end with an EOS token (excluding those truncated at maximum length). A sudden drop indicates the model has learned to produce minimal outputs rather than reasoning traces.

We define **collapse onset** as the first training step where frac\_zero\_std exceeds 0.8 and remains above this threshold for at least 3 consecutive logging intervals. A collapse is **permanent** if the model never recovers (frac\_zero\_std remains above 0.8 until training ends) and **transient** if frac\_zero\_std returns below 0.8 before training completes.

## 3.5 Experimental Design

**Model.** DeepSeek-R1-Distill-Qwen-7B (7.6B parameters), a reasoning-specialized LLM distilled from DeepSeek-R1 that produces explicit chain-of-thought traces.

**Pruning conditions.** Three configurations at 20% structured sparsity:
- *Unpruned*: the original model (control)
- *Standard*: importance-only scoring ($\alpha = 0$, equivalent to magnitude-based structured pruning)
- *RASP*: CKA-weighted scoring ($\alpha = 1.0$)

**Calibration.** 512 reasoning traces from the GSM8K training set, selected by length diversity.

**Evaluation.** GSM8K test set ($N = 1{,}319$), greedy decoding, seed 42. Accuracy is measured by exact-match answer extraction against ground truth.

**Comparisons.** Each pruning condition undergoes both SFT-only and SFT+GRPO recovery, yielding six model variants for direct comparison of recovery paradigm effects.

### Notation Summary

| Symbol | Definition |
|--------|-----------|
| $I(h)$ | Structural importance (Taylor expansion) |
| $F(h)$ | Functional overlap (intra-layer mean CKA) |
| $S(h)$ | Recovery-aware composite score |
| $\alpha$ | Overlap weight (default 1.0) |
| $t_c$ | Collapse onset step |
| $G$ | GRPO group size (8) |
| frac\_zero\_std | Fraction of zero-variance reward groups |
