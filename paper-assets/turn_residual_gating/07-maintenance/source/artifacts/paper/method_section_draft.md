# 3. Method

## 3.1 Problem Setup

Consider a multi-turn dialogue sequence $\mathbf{x} = [s, u_1, a_1, u_2, a_2, \ldots, u_T, a_T]$, where $s$ denotes the system prompt, and $u_t$, $a_t$ represent the user and assistant turns at round $t$. We define the **goal token set** $\mathcal{G}$ as the token positions corresponding to the system prompt $s$ and the first user query $u_1$, which together specify the task objective for the conversation.

For a query position $q$ and goal set $\mathcal{G}$, the Goal Attention Ratio (GAR) measures how much attention the model allocates to goal-specifying tokens:

$$\text{GAR}(q, \mathcal{G}) = \frac{1}{LH} \sum_{l=1}^{L} \sum_{h=1}^{H} \sum_{g \in \mathcal{G}} \alpha_l^h(q, g)$$

where $\alpha_l^h(q, g)$ is the softmax attention weight from position $q$ to position $g$ at layer $l$, head $h$, and $L$, $H$ are the total number of layers and attention heads. In practice, we evaluate GAR at the last token of each assistant turn $a_t$, as this position aggregates the model's contextual state for the next prediction.

Dongre et al. (2026) established that GAR decays by 27-48% over 50 turns across 12 LLM families. Their residual stream probes further reveal that goal information persists in hidden representations (probe AUC $\geq 0.98$) even after attention to goal tokens has collapsed. The model retains goal knowledge in its residual stream but progressively fails to access it through the attention mechanism. This dissociation between information retention and attention loss motivates an intervention at the residual pathway rather than at the attention computation itself.


## 3.2 ThreadGate Architecture

ThreadGate inserts a lightweight gating module at each transformer layer's residual connection. For layer $l$, let $f_l(\cdot)$ denote the combined self-attention and feed-forward transformation. The standard residual update $\mathbf{x}_l = \mathbf{x}_{l-1} + f_l(\mathbf{x}_{l-1})$ is replaced by:

$$\mathbf{x}_l = \mathbf{x}_{l-1} + g_l \cdot f_l(\mathbf{x}_{l-1}), \quad g_l \in (0, 1)$$

where $g_l$ is a scalar gate value produced by a learned gate network $\phi_l$. Each layer has its own gate network, and $g_l$ varies across token positions: $g_l^{(i)}$ denotes the gate value for position $i$ at layer $l$. When $g_l \approx 1$, the layer operates normally; when $g_l < 1$, its residual contribution is attenuated.

**Gate Network.** Each gate network $\phi_l$ accepts two inputs: (1) the hidden state $\mathbf{x}_{l-1} \in \mathbb{R}^d$ at the current position, and (2) a turn feature embedding. A down-projection $W_{\text{down}} \in \mathbb{R}^{d \times r}$ first reduces the hidden state to dimension $r$. The turn features are embedded into a vector $\mathbf{e} \in \mathbb{R}^{d_t}$ through a TurnEmbedding module (described below). The gate value is then:

$$g_l = \sigma\!\Big(W_2 \, \text{ReLU}\!\big(W_1 [\mathbf{x}_{l-1} W_{\text{down}};\; \mathbf{e}]\big) + b\Big)$$

where $W_1 \in \mathbb{R}^{(r + d_t) \times d_h}$, $W_2 \in \mathbb{R}^{d_h \times 1}$, $\sigma$ is the sigmoid function, and $[\cdot\,;\,\cdot]$ denotes concatenation. We set $r = 16$, $d_h = 64$, and $d_t = 16$. The output bias $b$ is initialized to 1.5, so $\sigma(b) \approx 0.82$ at initialization. This warm start ensures the gated model behaves nearly identically to the original LLM at the onset of training.

**TurnEmbedding.** This module encodes the structural position of each token within the multi-turn dialogue. For each token position $i$, we compute two discrete features: (1) *turn distance* $d_i$, the number of tokens since the nearest turn boundary marker (\texttt{<|im\_start|>} or \texttt{<|im\_end|>}), and (2) *turn index* $t_i$, the ordinal index of the dialogue turn that contains position $i$. Both features are capped at 32 and mapped through learned embedding tables:

$$\mathbf{e}_i = [\text{Embed}_{\text{dist}}(d_i);\; \text{Embed}_{\text{turn}}(t_i)]$$

where $\text{Embed}_{\text{dist}}, \text{Embed}_{\text{turn}} \in \mathbb{R}^{33 \times 8}$. The resulting 16-dimensional vector allows the gate to condition on dialogue structure (how far the current token is from a turn boundary, which turn it belongs to) without encoding turn content.

**Integration with Frozen LLM.** The base LLM (Qwen2.5-7B-Instruct) remains frozen throughout training. LoRA adapters (rank 16, $\alpha = 32$) are attached to the query and value projections to preserve language modeling capacity, while the gate networks and TurnEmbedding are trained jointly. The gating mechanism is implemented via forward hooks registered on each transformer layer: after a layer computes its output, the hook extracts the residual update $f_l(\mathbf{x}_{l-1}) = \mathbf{x}_l - \mathbf{x}_{l-1}$ and scales it by $g_l$ before the result passes to the next layer. A single TurnEmbedding module is shared across all layers.

**Parameter Overhead.** Each gate network contains approximately 60K parameters, dominated by the $d \times r$ down-projection. Across all 28 layers, the total gate parameter count is ~1.67M, or roughly 0.02% of the 7.6B base model. The shared TurnEmbedding adds 528 parameters. This minimal footprint makes ThreadGate a practical plug-in for pretrained LLMs.


## 3.3 Training Objective

The total training loss combines three terms:

$$\mathcal{L} = \mathcal{L}_{\text{NTP}} + \lambda_{\text{gar}} \cdot \mathcal{L}_{\text{GAR}} + \lambda_{\text{div}} \cdot \mathcal{L}_{\text{div}}$$

with $\lambda_{\text{gar}} = 1.0$ and $\lambda_{\text{div}} = 1.0$.

**Next-Token Prediction Loss.** $\mathcal{L}_{\text{NTP}}$ is the standard cross-entropy loss computed only over assistant tokens. Tokens in the system prompt and user turns are masked (label set to $-100$), so the model is trained exclusively to produce assistant responses. This preserves the natural training signal of multi-turn dialogue.

**GAR Regularization Loss.** We use a bidirectional mean squared error (MSE) loss that pulls the mean GAR toward a target value $\tau$:

$$\mathcal{L}_{\text{GAR}} = \left(\overline{\text{GAR}} - \tau\right)^2$$

where $\overline{\text{GAR}} = \frac{1}{T} \sum_{t=1}^{T} \text{GAR}(q_t, \mathcal{G})$ is the mean GAR across assistant turns (with $q_t$ the last token of turn $a_t$), and $\tau = 0.5$.

The choice of MSE over a monotonic reward (e.g., $\mathcal{L} = -\overline{\text{GAR}}$) is deliberate. A monotonic signal pushes gates toward identity ($g_l \to 1$ everywhere), which maximizes GAR trivially by removing all gating. The bidirectional MSE penalty resists this collapse: when $\overline{\text{GAR}} > \tau$, the gradient reverses and penalizes further GAR increase. This keeps the gates in a functionally meaningful regime where they can selectively modulate layers rather than uniformly pass through all residual updates.

**Differentiable GAR Computation.** To backpropagate through $\mathcal{L}_{\text{GAR}}$, we register forward hooks on the self-attention modules to capture attention weight tensors before detachment. The model runs with eager attention (not FlashAttention) during training so that per-head attention matrices remain in the computation graph. The GAR value is then computed by indexing into these attention matrices at the goal and query positions, and the gradient flows from $\mathcal{L}_{\text{GAR}}$ through the attention weights to the gate parameters.

**Gate Diversity Loss.** Without explicit regularization, gate values across layers can converge to a uniform scalar, which collapses the per-layer structure that ThreadGate is designed to learn. We add a diversity term:

$$\mathcal{L}_{\text{div}} = \text{ReLU}\!\left(\sigma_{\min} - \text{std}(\bar{g}_1, \ldots, \bar{g}_L)\right)$$

where $\bar{g}_l = \frac{1}{N} \sum_{i=1}^{N} g_l^{(i)}$ is the mean gate value at layer $l$ across all $N$ token positions in the sequence, and $\sigma_{\min} = 0.05$. This loss activates only when the standard deviation of layer-averaged gates falls below the threshold. When the gates already exhibit sufficient variation across layers, $\mathcal{L}_{\text{div}} = 0$ and imposes no gradient. The ReLU formulation provides a soft floor on diversity without over-constraining the learned gate profile.


## 3.4 Uniform Gate Baseline

To isolate the contribution of turn-aware conditioning, we introduce a Uniform Gate ablation baseline. This variant shares the same architecture and training objective as ThreadGate, with one modification: the TurnEmbedding output is replaced by a single learned constant vector $\mathbf{c} \in \mathbb{R}^{d_t}$, broadcast identically to all token positions. The Uniform Gate can still learn layer-specific gating patterns through the hidden-state-dependent pathway of its gate network, but it cannot condition gate values on turn structure. Any performance gap between ThreadGate and the Uniform Gate therefore isolates the value of turn boundary information in the gating decision.
