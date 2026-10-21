## 3. Method

We present **ColliForce**, a framework that integrates differentiable workspace Signed Distance Fields (SDFs) into Vision-Language-Action models to enable collision-aware action generation. Our approach operates in the feature space of a pretrained VLA, requiring no architectural modification to the backbone. We describe the problem setting (Sec. 3.1), the differentiable SDF integration (Sec. 3.2), the gradient-guided action refinement mechanism (Sec. 3.3), the training protocol (Sec. 3.4), and inference-time deployment (Sec. 3.5).

### 3.1 Problem Formulation

We consider a language-conditioned robotic manipulation setting where a Vision-Language-Action model $\pi_\theta$ generates an action trajectory $\{a_t\}_{t=1}^{H}$ with action horizon $H = 50$ conditioned on visual observations $o$ and a language instruction $l$. Each action $a_t \in \mathbb{R}^7$ specifies the desired end-effector (EE) displacement in position ($\Delta x, \Delta y, \Delta z$), orientation ($\Delta q_1, \ldots, \Delta q_3$), and gripper state.

In cluttered workspaces, the generated trajectory may command the EE into regions occupied by obstacles, causing collisions that damage objects or interrupt task execution. We formalize the collision avoidance objective through the workspace Signed Distance Field $\Phi: \mathbb{R}^3 \to \mathbb{R}$, where $\Phi(\mathbf{x}) > 0$ indicates free space, $\Phi(\mathbf{x}) = 0$ denotes the obstacle boundary, and $\Phi(\mathbf{x}) < 0$ indicates penetration. The goal is to learn a policy that generates trajectories satisfying $\Phi(\text{EE}(a_t)) > 0$ for all $t$, while preserving task success.

Our base VLA is $\pi_0$ (Physical Intelligence), a 3.5B-parameter flow-matching model comprising a PaliGemma vision-language encoder (Gemma 2B) and a Gemma 300M action expert. Action generation proceeds via iterative denoising over $H$ steps, producing a sequence of action tokens through the action expert's output projection $W_{\text{out}} \in \mathbb{R}^{1024 \times 32}$ that maps from the expert's hidden dimension to the action token space.

### 3.2 Differentiable Workspace SDF Integration

We augment the VLA with two lightweight auxiliary modules that operate on the action expert's intermediate representations.

**Feature extraction.** We capture the action expert's suffix output $\mathbf{z} \in \mathbb{R}^{B \times H \times 1024}$ — the input to the action output projection $W_{\text{out}}$ — via a forward hook registered on `action_out_proj`. A mean-pooling operation along the action horizon dimension yields a compact feature vector $\bar{\mathbf{z}} = \frac{1}{H} \sum_{t=1}^{H} \mathbf{z}_t \in \mathbb{R}^{1024}$ that summarizes the action expert's spatial understanding of the current scene.

**SDF Decoder.** A 4-layer MLP $f_\text{SDF}$ predicts the signed distance value at arbitrary 3D query points given the pooled action expert features:

$$f_\text{SDF}: (\bar{\mathbf{z}}, \mathbf{x}) \mapsto \hat{\Phi}(\mathbf{x}), \quad \bar{\mathbf{z}} \in \mathbb{R}^{1024}, \; \mathbf{x} \in \mathbb{R}^3$$

The architecture employs hidden dimension 256 with Softplus activation ($\beta = 5$) and a skip connection that re-injects the query coordinates at the second layer:

$$\mathbf{h}_0 = \sigma(\mathbf{W}_0 [\bar{\mathbf{z}}; \mathbf{x}] + \mathbf{b}_0)$$
$$\mathbf{h}_1 = \sigma(\mathbf{W}_1 \mathbf{h}_0 + \mathbf{b}_1)$$
$$\mathbf{h}_2 = \sigma(\mathbf{W}_2 [\mathbf{h}_1; \mathbf{x}] + \mathbf{b}_2)$$
$$\hat{\Phi}(\mathbf{x}) = \mathbf{W}_3 \mathbf{h}_2 + \mathbf{b}_3$$

where $\sigma(\cdot) = \text{Softplus}_{\beta=5}(\cdot)$, $\mathbf{W}_0 \in \mathbb{R}^{256 \times 1027}$, $\mathbf{W}_1 \in \mathbb{R}^{256 \times 256}$, $\mathbf{W}_2 \in \mathbb{R}^{256 \times 259}$, and $\mathbf{W}_3 \in \mathbb{R}^{1 \times 256}$. All weights are initialized with Kaiming normal initialization.

For spatial gradient computation (required by Eikonal regularization and gradient-guided refinement), the decoder computes $\nabla_{\mathbf{x}} \hat{\Phi}(\mathbf{x})$ via `torch.autograd.grad` with graph creation enabled during training.

**End-Effector Position Extractor.** A 2-layer MLP $g_\text{EE}$ predicts the current EE position from the pooled features:

$$g_\text{EE}: \bar{\mathbf{z}} \mapsto \hat{\mathbf{p}}_\text{EE} \in \mathbb{R}^3$$

with architecture $\text{Linear}(1024, 256) \to \text{ReLU} \to \text{Linear}(256, 3)$. The EE prediction serves dual purposes: (1) it provides the query point for evaluating collision proximity, and (2) its auxiliary loss encourages the action expert features to encode spatial position information.

**Auxiliary training losses.** The SDF decoder is trained with a clamped L1 loss augmented by Eikonal regularization:

$$\mathcal{L}_\text{SDF} = \underbrace{\frac{1}{N} \sum_{i=1}^{N} \left| \text{clamp}(\hat{\Phi}(\mathbf{x}_i), \pm\delta) - \text{clamp}(\Phi^*(\mathbf{x}_i), \pm\delta) \right|}_{\mathcal{L}_\text{L1}} + \lambda_\text{eik} \underbrace{\frac{1}{N} \sum_{i=1}^{N} \left( \|\nabla_{\mathbf{x}} \hat{\Phi}(\mathbf{x}_i)\|_2 - 1 \right)^2}_{\mathcal{L}_\text{eikonal}}$$

where $\delta = 0.05$ is the clamping threshold, $\lambda_\text{eik} = 0.1$, and $N = 64$ query points are randomly sampled from the ground-truth SDF volume per training step. The clamping focuses learning on the near-surface region most relevant for collision detection. The Eikonal term enforces the unit-gradient property of valid distance fields.

The EE extractor is trained with MSE loss against ground-truth EE positions from the robot state:

$$\mathcal{L}_\text{EE} = \|\hat{\mathbf{p}}_\text{EE} - \mathbf{p}^*_\text{EE}\|_2^2$$

### 3.3 SDF Gradient-Guided Action Refinement

The core contribution of ColliForce is a gradient-based mechanism that leverages the differentiable SDF to steer the action expert's representations away from collision-prone regions during training. Unlike post-hoc action filtering, this approach modifies the feature space directly, enabling the model to internalize collision avoidance behavior.

**Refinement procedure.** Given the captured suffix output $\mathbf{z} \in \mathbb{R}^{B \times H \times 1024}$, the refiner:

1. Predicts the EE position and evaluates the SDF: $\hat{\mathbf{p}}_\text{EE} = g_\text{EE}(\bar{\mathbf{z}})$, $\hat{\Phi}(\hat{\mathbf{p}}_\text{EE}) = f_\text{SDF}(\bar{\mathbf{z}}, \hat{\mathbf{p}}_\text{EE})$.

2. Identifies near-collision samples: $\mathcal{S} = \{i : \hat{\Phi}(\hat{\mathbf{p}}_{\text{EE},i}) < m\}$, where the safety margin $m = 0.01$.

3. For samples in $\mathcal{S}$, computes the SDF gradient with respect to the suffix features: $\nabla_{\mathbf{z}} \hat{\Phi} = \frac{\partial \hat{\Phi}(\hat{\mathbf{p}}_\text{EE})}{\partial \mathbf{z}}$, capturing how changes in the action expert's internal representation affect the predicted collision distance.

4. Performs gradient ascent on the SDF (toward higher, safer values):

$$\mathbf{z}' = \mathbf{z} + \alpha \cdot \text{clip}(\nabla_{\mathbf{z}} \hat{\Phi}) \odot \mathbf{m}_\mathcal{S}$$

where $\alpha = 0.1$ is the step size, $\text{clip}(\cdot)$ denotes per-sample L2 norm clipping with threshold $\gamma = 1.0$ for gradient stability, and $\mathbf{m}_\mathcal{S}$ is a binary mask selecting only near-collision samples.

5. Projects both original and refined features through the action output head: $\mathbf{v}_t = W_\text{out}(\mathbf{z})$, $\mathbf{v}'_t = W_\text{out}(\mathbf{z}')$.

**Refinement loss.** The model is trained to directly output the collision-corrected actions by minimizing the discrepancy between the original and refined predictions on near-collision samples:

$$\mathcal{L}_\text{refine} = \frac{1}{|\mathcal{S}|} \sum_{i \in \mathcal{S}} \|\mathbf{v}_{t,i} - \text{sg}(\mathbf{v}'_{t,i})\|_2^2$$

where $\text{sg}(\cdot)$ denotes the stop-gradient operator. The gradient flows only through $\mathbf{v}_t \to \mathbf{z} \to \theta_\text{LoRA}$, training the LoRA adapters to anticipate and avoid collisions without requiring the gradient refiner at inference time. The refined target $\mathbf{v}'_t$ is detached, serving as a teacher signal that encodes collision-aware behavior.

This design is reminiscent of knowledge distillation: the SDF gradient refiner acts as a computationally expensive teacher that produces safe actions, while the student (the LoRA-adapted VLA) learns to replicate these actions directly, amortizing the SDF computation into the model's parameters.

### 3.4 Training Protocol

We adopt a two-phase training protocol that ensures SDF prediction accuracy before engaging gradient-guided refinement.

**Baseline.** Standard LoRA fine-tuning of $\pi_0$ on task demonstrations using the flow-matching action loss $\mathcal{L}_\text{action}$. LoRA adapters are injected into both the PaliGemma encoder (rank 16, $\alpha = 16$) and the action expert (rank 32, $\alpha = 32$), targeting the attention projections ($\mathbf{W}_q, \mathbf{W}_k, \mathbf{W}_v, \mathbf{W}_o$) and MLP layers ($\mathbf{W}_\text{gate}, \mathbf{W}_\text{up}, \mathbf{W}_\text{down}$). The total LoRA parameter count is approximately 33.5M.

**A1 — SDF Auxiliary Task.** This variant adds the SDF decoder and EE extractor as auxiliary tasks:

- *Phase 1* ($0 \to T_\text{warmup}$ steps, $T_\text{warmup} = 5000$): The entire backbone (including LoRA parameters) is frozen. Only the SDF decoder ($\sim$395K parameters) and EE extractor ($\sim$263K parameters) are trained. The auxiliary modules receive detached features ($\bar{\mathbf{z}}.\text{detach()}$) to avoid destabilizing the pretrained backbone during warmup. This phase establishes an accurate SDF predictor anchored to the backbone's current feature distribution.

- *Phase 2* ($T_\text{warmup} \to T_\text{end}$): LoRA parameters are unfrozen with a linear gradient warmup over 100 steps to prevent abrupt feature distribution shifts. The full loss is:

$$\mathcal{L}_\text{A1} = \mathcal{L}_\text{action} + \lambda_\text{SDF} \cdot \mathcal{L}_\text{SDF} + \lambda_\text{EE} \cdot \mathcal{L}_\text{EE}$$

where $\lambda_\text{SDF} = 0.1$ and $\lambda_\text{EE} = 0.01$. Gradients now flow from the auxiliary losses through the pooled features into the LoRA adapters, encouraging the action expert to develop features that encode workspace geometry.

**A3 — SDF Gradient-Guided Refinement.** This variant extends A1 with the gradient refiner:

- *Phase 1*: Identical to A1 — backbone frozen, SDF decoder and EE extractor warmup only.

- *Phase 2*: LoRA unfreezing with gradient warmup (same as A1), plus activation of the gradient refiner. The full loss becomes:

$$\mathcal{L}_\text{A3} = \mathcal{L}_\text{action} + \lambda_\text{SDF} \cdot \mathcal{L}_\text{SDF} + \lambda_\text{EE} \cdot \mathcal{L}_\text{EE} + \lambda_\text{refine} \cdot \mathcal{L}_\text{refine}$$

where $\lambda_\text{refine} = 0.1$. The refinement loss is only computed when near-collision samples exist in the batch ($|\mathcal{S}| > 0$), adding zero computational overhead for collision-free training steps.

All variants use AdamW with cosine decay scheduling (peak learning rate $2.5 \times 10^{-5}$, decaying to $2.5 \times 10^{-6}$), batch size 32, and train for 30,000 steps. The warmup period for the learning rate schedule is $\min(1000, T_\text{end} / 3)$ steps.

### 3.5 Inference-Time Refinement

At inference, ColliForce supports an optional SDF gradient correction that provides an additional safety layer without architectural changes to the deployed model:

1. The VLA generates an action $a_t$ through standard forward pass.
2. The predicted next EE position is computed: $\hat{\mathbf{p}}_\text{next} = \mathbf{p}_\text{EE} + a_t[:3]$.
3. The SDF decoder queries the predicted SDF at this position: $\hat{\Phi}(\hat{\mathbf{p}}_\text{next})$.
4. If $\hat{\Phi}(\hat{\mathbf{p}}_\text{next}) < m$ (near collision), the action's position component is corrected:

$$a'_t[:3] = a_t[:3] + \alpha \cdot \frac{\nabla_{\mathbf{x}} \hat{\Phi}(\hat{\mathbf{p}}_\text{next})}{\|\nabla_{\mathbf{x}} \hat{\Phi}(\hat{\mathbf{p}}_\text{next})\|_2}$$

The L2-normalization bounds the correction magnitude to $\alpha$ regardless of the SDF gradient scale, preventing over-correction near sharp obstacle boundaries. Orientation and gripper components of $a_t$ remain unchanged.

This inference-time mechanism introduces zero additional latency when $\hat{\Phi}(\hat{\mathbf{p}}_\text{next}) \geq m$ (i.e., the EE is sufficiently far from obstacles). For the A3 variant trained with gradient refinement, the model has already learned to produce collision-avoiding actions, so inference-time refinement serves as a complementary safety net for out-of-distribution obstacle configurations.
