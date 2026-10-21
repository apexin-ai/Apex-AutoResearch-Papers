# 3. Method

## 3.1 Problem Formulation

### Interactive Agent as POMDP

We formalize the interactive agent task as a Partially Observable Markov Decision Process (POMDP) $\mathcal{M} = \langle \mathcal{S}, \mathcal{A}, \mathcal{O}, T, O, R, \gamma \rangle$, where $\mathcal{S}$ is the state space of the environment (e.g., object locations and states in a household), $\mathcal{A}$ is the action space (e.g., natural language commands such as `go to shelf 1`, `take mug 2`), $\mathcal{O}$ is the observation space (textual descriptions of the environment), $T: \mathcal{S} \times \mathcal{A} \rightarrow \Delta(\mathcal{S})$ is the transition function, $O: \mathcal{S} \rightarrow \Delta(\mathcal{O})$ is the observation function, $R: \mathcal{S} \times \mathcal{A} \rightarrow \mathbb{R}$ is the reward function, and $\gamma$ is the discount factor.

At each timestep $t$, the agent receives observation $o_t \in \mathcal{O}$ and selects action $a_t \in \mathcal{A}$ according to its policy $\pi_\phi(a_t \mid h_t)$, where $h_t = (o_1, a_1, \ldots, o_t)$ is the interaction history. The episode terminates upon task completion (success) or after a maximum number of steps $T_{\max}$.

### Verification Decision

At each step $t$, in addition to the primary action $a_t$, the agent makes a binary verification decision:
$$d_t \in \{0, 1\}$$
where $d_t = 1$ triggers a self-verification subroutine and $d_t = 0$ skips verification. When $d_t = 1$, the agent re-examines its current observation and proposed action, potentially revising $a_t$ to an alternative $a_t'$.

We parameterize the verification policy as $\pi_\theta(d_t \mid s_t)$, where $s_t$ is a compact representation of the agent's state at step $t$ (including the current observation, proposed action, and task context). In practice, $\pi_\theta$ is realized by augmenting the agent's action space with a special control token $\langle\text{VERIFY}\rangle$ that precedes the action output, such that the language model generates either $\langle\text{VERIFY}\rangle\, a_t$ or $\langle\text{SKIP}\rangle\, a_t$ at each step.

### Action-Change Signal

We define the **action-change indicator** as the primary signal for verification informativeness:
$$\Delta a_t = \mathbb{1}\left[a_t^{\text{post}} \neq a_t^{\text{pre}}\right]$$
where $a_t^{\text{pre}}$ is the action the agent would have taken without verification (obtained via a single greedy decode pass), and $a_t^{\text{post}}$ is the action after the verification subroutine. Equality is assessed via semantic canonicalization (e.g., mapping actions to $\langle \text{verb}, \text{object}, \text{receptacle} \rangle$ tuples in ALFWorld) to avoid spurious mismatches from surface-form variation.

The key insight is that **most self-verification is confirmatory rather than corrective** \cite{self-verification-dilemma-2026}. When $\Delta a_t = 0$, the verification consumed compute without altering behavior---it was uninformative. When $\Delta a_t = 1$, the verification produced a behavioral change, indicating it carried decision-relevant information.

### Verification Cost Model

Each verification incurs a fixed cost $c_{\text{verify}}$ (proportional to the additional inference tokens required). The total verification cost for an episode of length $T$ is:
$$C_{\text{total}} = \sum_{t=1}^{T} d_t \cdot c_{\text{verify}}$$

In practice, $c_{\text{verify}}$ corresponds to the additional forward pass needed for the verification subroutine (re-observation, re-reasoning, and potential action revision), which approximately doubles the per-step inference cost.

<!-- [中文注释] Director 决策点：c_verify 是固定常数还是与 step 相关的变量？当前设定为固定值，但如果 verification 长度变化大可能需要 token-level cost -->

### Objective

The goal of B-IAVR is to learn a verification policy $\pi_\theta$ that maximizes task success while minimizing verification cost. We formulate this as a constrained optimization problem:
$$\max_\theta \; \mathbb{E}_{\pi_\theta, \pi_\phi}\left[\sum_{t=1}^{T} R(s_t, a_t)\right] \quad \text{s.t.} \quad \mathbb{E}_{\pi_\theta}\left[C_{\text{total}}\right] \leq C_{\text{budget}}$$

where $C_{\text{budget}}$ is the verification budget constraint. In practice, we relax this to an unconstrained objective via Lagrangian relaxation (Section 3.2).


## 3.2 B-IAVR: Selective Self-Verification via RL

### Overview

B-IAVR (**B**inary **I**nformative **A**ction **V**erification via **R**L) trains a language model agent to decide *when* to invoke self-verification, using action change as a reward signal for verification informativeness. The method consists of three components: (1) a selective verification policy that makes per-step binary verify/skip decisions, (2) a composite reward function combining task success, verification informativeness, and cost, and (3) an RL training procedure based on GRPO with optional GiGPO extension for step-level credit assignment.

### Selective Verification Policy

The agent's generation at each step $t$ is structured as:
$$\pi(d_t, a_t \mid h_t) = \pi_\theta(d_t \mid h_t) \cdot \pi_\phi(a_t \mid h_t, d_t)$$

When the model generates $\langle\text{VERIFY}\rangle$, a verification subroutine is triggered:
1. The agent produces a preliminary action $a_t^{\text{pre}}$ via greedy decoding from the current state.
2. The verification module re-examines the observation $o_t$, the proposed action $a_t^{\text{pre}}$, and the task goal $g$, generating a verification rationale.
3. Based on the rationale, the agent either confirms $a_t^{\text{pre}}$ or revises it to $a_t^{\text{post}}$.

When $\langle\text{SKIP}\rangle$ is generated, $a_t^{\text{pre}}$ is directly executed without verification.

In practice, $\pi_\theta$ and $\pi_\phi$ share the same language model backbone, with the verification decision encoded as a special token prefix. This avoids the overhead of maintaining separate models and allows end-to-end RL training.

<!-- [中文注释] Director 决策点：verification subroutine 的具体 prompt 设计需要确认——是 re-observe environment 还是 re-reason on existing observation？当前写为 re-examine observation，但如果 re-observe 有不同 cost implications -->

### Reward Design

The reward function combines three components to balance task performance, verification quality, and cost:

**Task success reward.** A binary episode-level reward indicating whether the task was completed:
$$r_{\text{task}} = \begin{cases} r_+ & \text{if task completed successfully} \\ 0 & \text{otherwise} \end{cases}$$

**Action-change reward.** A step-level reward given when verification produces a behavioral change, serving as a proxy for verification informativeness:
$$r_{\text{ac}, t} = \alpha \cdot d_t \cdot \Delta a_t$$
where $\alpha > 0$ controls the magnitude of the informativeness bonus. This reward is only assigned at steps where verification is triggered ($d_t = 1$) and the action changes ($\Delta a_t = 1$).

**Verification cost penalty.** A step-level penalty for each verification invocation:
$$r_{\text{cost}, t} = -\gamma_c \cdot d_t$$
where $\gamma_c > 0$ is the per-verification cost coefficient.

The **combined reward** for an episode is:
$$R = r_{\text{task}} + \sum_{t=1}^{T}\left(\beta \cdot r_{\text{ac}, t} + r_{\text{cost}, t}\right)$$
$$= r_{\text{task}} + \sum_{t=1}^{T} d_t \left(\beta \cdot \alpha \cdot \Delta a_t - \gamma_c\right)$$

where $\beta$ balances the informativeness bonus against the cost penalty. The cost coefficient $\gamma_c$ is updated via dual gradient ascent to enforce the budget constraint:
$$\gamma_c \leftarrow \gamma_c + \eta_\gamma \left(\mathbb{E}[C_{\text{total}}] - C_{\text{budget}}\right)$$

This Lagrangian formulation allows the agent to learn a cost-performance tradeoff without hand-tuning $\gamma_c$.

<!-- [中文注释] Director 决策点：α 和 β 的关系是否冗余？当前公式 β·α·Δa_t 可以简化为单一系数。保留两个是为了区分 action-change signal 的 base magnitude (α) 和 informativeness-vs-task 的 tradeoff (β)。如果觉得过度参数化，可以合并 -->

**Interaction between action-change reward and task success.** Note that $r_{\text{ac}}$ is not gated on task success. A verification that changes the action is informative regardless of episode outcome---even in failed episodes, action changes driven by verification reveal that the agent's initial action was uncertain, providing useful training signal. This design choice avoids the bootstrap problem encountered with success-gated rewards when base success rates are low [TBD: cite exp013f gaming / D012-D013 analysis].

### Training with GRPO

We train $\pi_\theta$ using Group Relative Policy Optimization (GRPO) \cite{shao2024deepseekmath}, which estimates advantages from groups of rollouts without requiring a learned value function.

For each training step, we sample $G$ groups of $K$ rollouts per task instance. Within each group $g$, the advantage of rollout $k$ is computed as:
$$\hat{A}^{(g)}_k = \frac{R^{(g)}_k - \text{mean}(\{R^{(g)}_j\}_{j=1}^K)}{\text{std}(\{R^{(g)}_j\}_{j=1}^K) + \epsilon}$$

The GRPO objective with KL regularization is:
$$\mathcal{L}_{\text{GRPO}}(\theta) = -\mathbb{E}_{g,k}\left[\min\left(\rho_t \hat{A}^{(g)}_k, \; \text{clip}(\rho_t, 1-\varepsilon, 1+\varepsilon) \hat{A}^{(g)}_k\right)\right] + \lambda_{\text{KL}} \, D_{\text{KL}}(\pi_\theta \| \pi_{\text{ref}})$$

where $\rho_t = \frac{\pi_\theta(a_t | h_t)}{\pi_{\text{ref}}(a_t | h_t)}$ is the importance ratio and $\pi_{\text{ref}}$ is the reference policy (initialized from the SFT checkpoint).

**Step-independent context.** Following the rollout design of verl-agent \cite{selfguide2026}, we employ step-independent context for multi-turn rollouts: at each step, the model receives only the current observation and task context rather than the full interaction history. This prevents context length explosion in long-horizon tasks and maintains consistent inference quality across steps---a critical factor for training stability in interactive agent settings.

<!-- [中文注释] Director 决策点：step-independent context 是否需要更详细的描述？这实际上是 exp026 成功的关键技术因素（vs RAGEN full-history 三次 entropy collapse），但如果论文 framing 不强调框架差异可以简写 -->

### Extension: GiGPO for Step-Level Credit Assignment

[TBD: GiGPO details]

A known limitation of episode-level GRPO is that the advantage $\hat{A}^{(g)}_k$ is shared across all steps within a rollout, providing no step-level credit assignment. In multi-turn agent tasks where episodes span 10--30 steps, this leads to high variance and slow learning---a single failed step can assign negative advantage to all preceding correct actions.

GiGPO (Group-in-Group Policy Optimization) \cite{feng2025gigpo} addresses this via a nested group structure. For each step $t$ within a rollout, GiGPO constructs a *step-level group* by comparing the outcomes of rollouts that share the same prefix up to step $t-1$ but diverge at step $t$:
$$\hat{A}^{\text{step}}_t = \frac{R_t^{>} - \text{mean}(\{R^{>}_j\})}{\text{std}(\{R^{>}_j\}) + \epsilon}$$
where $R_t^{>}$ denotes the cumulative reward from step $t$ onward. This provides dense, step-level learning signal without requiring a learned critic.

In the B-IAVR context, GiGPO is particularly well-suited because:

1. **Verification decisions are step-level.** The verify/skip decision at step $t$ has localized impact---GiGPO can attribute the outcome change to the specific verification decision rather than spreading credit across the entire episode.
2. **Action-change reward is already step-level.** The reward $r_{\text{ac},t}$ naturally aligns with GiGPO's step-level advantage structure, providing dense reward signal at the granularity where credit assignment operates.
3. **Sparse task reward benefits from decomposition.** When the episode-level task reward $r_{\text{task}}$ is binary and sparse, GiGPO's step-level groups break the learning signal into denser components, mitigating the cold-start problem observed with pure GRPO on sparse rewards.

[TBD: exp result --- GiGPO vs GRPO training curves, convergence speed comparison]

### Self-Guide Integration

B-IAVR builds upon the Self-Guide framework \cite{selfguide2026}, which co-evolves a task policy and an internal reward model through iterative RL training. Specifically, Self-Guide trains a policy $\pi_\phi$ alongside an internal evaluator $V_\psi$ that scores intermediate states, providing denser reward signal than the sparse environment reward alone.

We extend Self-Guide by introducing the verification decision layer: the internal evaluator $V_\psi(s_t)$ serves as an additional input feature to the verification policy $\pi_\theta(d_t \mid s_t, V_\psi(s_t))$. Intuitively, when the internal evaluator assigns low confidence to the current state (indicating the agent is uncertain about its action), verification is more likely to be informative. This creates a natural trigger mechanism:

$$P(d_t = 1) \uparrow \quad \text{when} \quad V_\psi(s_t) \text{ is low (uncertain)}$$

The co-evolution property of Self-Guide ensures that as the task policy improves, the internal evaluator also calibrates, leading to a progressively refined verification trigger that adapts to the agent's evolving competence.

[TBD: exp result --- Self-Guide internal reward correlation with action-change frequency]

<!-- [中文注释] Director 决策点：Self-Guide integration 的描述深度——当前写了 V_ψ 作为 verification trigger 的机制，但实际实现可能更简单（直接用 token logits confidence 而非独立 V_ψ）。需要确认最终实现方案后 revise -->


## 3.3 Comparison with Related Methods

We position B-IAVR against three categories of related methods: adaptive reasoning effort, selective verification, and self-correction in agents.

### vs ARES: Adaptive Reasoning Effort Selection

ARES \cite{yang2026ares} trains an SFT-initialized router to allocate continuous reasoning effort per step, optimized via GRPO with a combined outcome and token-efficiency reward. B-IAVR differs in three fundamental aspects:

| Dimension | ARES | B-IAVR (Ours) |
|-----------|------|----------------|
| **Decision type** | Continuous effort level | Binary verify/skip |
| **Training signal** | Pre-defined quality metrics + token efficiency | Action change (behavioral) |
| **Data requirement** | Difficulty-annotated data for SFT bootstrap | Environment interaction only |
| **Scope** | General reasoning tasks | Interactive agent tasks |

The binary decision in B-IAVR offers two advantages: (1) it is more interpretable---one can directly audit *which steps* were verified and *whether* the verification changed behavior, and (2) it avoids the need for difficulty annotations, as the action-change signal is self-supervised from the agent's own behavioral variation.

Conversely, ARES's continuous allocation is more flexible for tasks where "partial verification" makes sense. B-IAVR's binary design is motivated by the interactive agent setting, where verification is a discrete subroutine (re-observe environment, re-reason, potentially revise) that is either invoked or not.

### vs Thinkless: Learning When to Think

Thinkless \cite{du2025thinkless} uses RL to train a control token that decides whether to invoke extended thinking (chain-of-thought) before answering. While methodologically parallel to B-IAVR (both learn a binary computation trigger via RL), they address different settings:

- **Single-turn vs multi-turn.** Thinkless operates on single-turn QA; B-IAVR on multi-step interactive agent trajectories where each decision depends on environment feedback.
- **Computation type.** Thinkless controls *internal reasoning* (thinking tokens); B-IAVR controls *external verification* (re-observation of the environment), grounding the signal in behavioral change rather than token-level computation.
- **Reward signal.** Thinkless uses task correctness; B-IAVR introduces the action-change signal as a verification-specific informativeness measure.

### vs Derailer-Rerailer: Adaptive Verification for Reasoning

Derailer-Rerailer \cite{wan2025derailer-rerailer} uses a heuristic instability signal to detect "derailed" reasoning steps and trigger correction. Compared to B-IAVR:

- **Heuristic vs learned.** Derailer-Rerailer relies on hand-designed instability metrics; B-IAVR learns the verification trigger end-to-end via RL. This eliminates the need for task-specific heuristic engineering and allows the trigger to adapt as the policy improves.
- **Reasoning chains vs agent trajectories.** Derailer-Rerailer operates on single-turn reasoning chains; B-IAVR on multi-turn agent trajectories with environment interaction. The environment provides a concrete grounding signal (observation changes) absent in pure reasoning settings.
- **Correction scope.** Derailer-Rerailer re-generates from the derailed step; B-IAVR's verification may confirm or revise a single action, preserving the trajectory structure.

### vs Sherlock: Reliable Agentic Workflow Execution

Sherlock \cite{sherlock2025} applies selective verification to agentic *workflows* (DAG-structured task plans) using offline counterfactual analysis and speculative execution. The key distinction is the level of abstraction: Sherlock verifies workflow nodes (coarse-grained, offline planning); B-IAVR verifies individual agent actions (fine-grained, online decision-making). The two approaches are complementary---Sherlock could serve as a workflow-level planner while B-IAVR handles step-level verification within each workflow node.

[TBD: exp result --- ablation table comparing B-IAVR with always-on / no-verify / random-$p$ / confidence-threshold baselines]

<!-- [中文注释] Director 决策点：3.3 节的对比深度是否合适？当前对 ARES 最详细（主要竞争者），Thinkless/Derailer-Rerailer/Sherlock 较简洁。如果 page budget 紧张，Sherlock 段可以移到 Related Work -->
