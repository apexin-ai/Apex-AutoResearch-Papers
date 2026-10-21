# HCAPO ALFWorld Analysis

## HCAPO Results

### ALFWorld Numbers (Qwen2.5-7B-Instruct)
- **HCAPO: 91.4%** overall success rate
- GRPO baseline: 77.6% → **+13.8 points**
- Per-subtask: Pick 99.1%, Look 90.3%, Clean 97.3%, Heat 81.8%, Cool 90.8%, Pick2 81.9%

### Smaller Model (Qwen2.5-1.5B-Instruct)
- HCAPO: 87.0% vs GRPO 72.8% → +14.2 points

### Model/Method/Baseline
- Models: Qwen2.5-Instruct 1.5B/3B/7B
- Training: 128 environments per rollout (group size G=8), 150 training iterations, max 50 env steps/episode, LR 1e-6, KL coeff 0.01
- Reward: binary (+10 success, 0 failure) with -0.1 penalty for invalid actions
- Context: **2-step lookback** for action/observation pairs (windowed, not full trajectory)

### Credit Assignment Method
HCAPO uses the **LLM itself as a post-hoc critic** via "Generative Verification":
1. After trajectory collection, the LLM is conditioned on the trajectory outcome (hindsight)
2. For each step t, compute hindsight importance ratio: ρ_t = clip(π_hind(a_t) / π̄_hind, 0.8, 1.2)
3. Per-step Q-value: Q_t^H = ρ_t · G_t
4. Composite advantage: **A_t = (R(τ)−μ_R)/σ_R + ω·(Q_t^H−μ_H)/σ_H**

This combines macro-scale episode-level GRPO signal (stability) + micro-scale hindsight correction (precision). The hindsight probability aggregates token-level log-probs when conditioned on final states.

### Full Baseline Comparison (7B, ALFWorld)

| Method | Success Rate |
|--------|-------------|
| ReAct (prompting) | 31.2% |
| Reflexion (prompting) | 42.7% |
| RLOO | 75.5% |
| GRPO | 77.6% |
| EMPG | 78.5% |
| PPO | 80.4% |
| GiGPO | 90.8% |
| **HCAPO** | **91.4%** |

### Ablation (1.5B)
| ω (hindsight weight) | Success |
|-----------------------|---------|
| 0 (= GRPO) | 72.8% |
| 0.2 | 79.7% |
| 0.5 | 84.4% |
| 1.0 (full HCAPO) | 87.0% |

With temporal smoothing on 7B: 96.9% (near-perfect).

---

## GiGPO / Turn-PPO ALFWorld Results

### GiGPO (NeurIPS 2025)
**Qwen2.5-7B-Instruct:**
- GiGPO (w/o std): **90.2%**
- GRPO: 77.6%, RLOO: 75.5%, PPO: 80.4%

**Qwen2.5-1.5B-Instruct:**
- GiGPO (w/o std): **86.1%**
- GRPO: 72.8%, RLOO: 69.7%, PPO: 54.4%

Method: Two-level hierarchical advantage — episode-level macro advantages + step-level micro advantages via "anchor state grouping" (retroactively identifies repeated environment states across trajectories). Uses **history length 2** (windowed context).

Note: HCAPO paper reports GiGPO at 90.8% (7B) — slight discrepancy with GiGPO paper's 90.2%, likely different eval protocols.

### Turn-PPO
**No ALFWorld results reported.** Turn-PPO (arXiv 2512.17008) evaluates only on WebShop and Sokoban. Uses turn-level MDP formulation with PPO, found PPO more robust than GRPO for multi-turn tasks.

---

## Diagnostic Framework Analysis

### M1 (Policy Information Loss) — Addressed?

**No. Neither HCAPO nor GiGPO address M1.**

Both use **windowed context (history length = 2)** for the policy. The agent only sees the last 2 action-observation pairs when deciding its next action, discarding earlier trajectory context. This means:
- The policy cannot condition on early observations that may be critical for later decisions
- In long ALFWorld episodes (up to 50 steps), substantial context is lost
- The capacity ceiling imposed by M1 remains

HCAPO's hindsight critic sees the full trajectory, but this only affects advantage estimation, not the policy's decision-making capability. The policy itself is still blind to truncated history.

### M2 (Advantage Sign Misattribution) — Addressed?

**HCAPO: Yes, directly targets M2.** The hindsight credit assignment refines per-step Q-values using the LLM's post-hoc evaluation of each action's contribution. Instead of uniformly assigning the episode outcome to all steps (as GRPO does), HCAPO modulates advantages by ρ_t (how likely the action is under hindsight-conditioned policy). This directly addresses the core M2 problem: bad actions in successful episodes get lower credit, good actions in failed episodes get higher credit.

**GiGPO: Partially addresses M2.** The anchor state grouping compares actions from the same state across trajectories, providing local relative advantages. However, this requires finding repeated states — in environments with diverse state spaces, this mechanism may fire infrequently. It's a less direct solution than HCAPO's explicit hindsight reasoning.

### Predicted Advantages Over Episode-Level GRPO

1. **Long sequences**: HCAPO's per-step credit should increasingly outperform episode-level GRPO as episode length grows, since uniform advantage assignment becomes noisier with more steps
2. **Mixed-quality trajectories**: When episodes contain both good and bad actions, HCAPO can selectively reinforce the good ones — GRPO cannot
3. **The +13.8% gap on ALFWorld** is substantial and consistent across model sizes, suggesting the credit assignment problem is a real bottleneck for GRPO on this benchmark

### Predicted Limitations

1. **M1 remains a binding constraint**: HCAPO still uses windowed context. On tasks where early context is critical for late decisions, better credit assignment cannot compensate for the policy simply not seeing the relevant information
2. **Hindsight critic quality**: The per-step Q-values are only as good as the LLM's ability to evaluate action quality post-hoc. If the LLM itself cannot distinguish good from bad actions (e.g., subtle mistakes), the hindsight signal degrades to noise
3. **Computational cost**: Running the LLM as a hindsight critic adds inference overhead per trajectory. The paper doesn't report wall-clock time comparisons
4. **ω sensitivity**: The ablation shows performance is sensitive to ω (72.8% → 87.0% as ω goes 0→1). In practice, this is another hyperparameter to tune per task
5. **Potential for our approach**: If our method addresses both M1 (via full context) AND M2 (via better advantage estimation), we should outperform HCAPO on tasks where early context matters. On tasks where context is not the bottleneck, HCAPO's explicit credit assignment may be competitive or superior

---

## Other ALFWorld RL Results

### EPO (Entropy-regularized Policy Optimization)
- Model: Qwen2.5-3B-Instruct
- GRPO+EPO: 75.8% IID avg, 75.4% OOD avg (Succ̄ metric = avg after convergence)
- GRPO alone: 63.3% IID avg, 63.5% OOD avg
- Improvement: +19.8% IID, +18.7% OOD on Succ̄
- Note: Uses 3B model, not directly comparable to 7B results above. EPO is complementary (addresses exploration/exploitation, not credit assignment)

### RWML (Reinforcement World Model Learning)
- Model: Qwen2.5-7B-Instruct
- RWML + Policy RL: **87.9%** avg (86.7% ID, 90.1% OOD)
- Policy RL alone: 81.0% avg
- Improvement: +6.9 points
- Method: Self-supervised world model learning via sim-to-real gap rewards, then standard RL. Not a credit assignment method — improves the model's environment understanding before RL

### FEDAGENT (Federated Agent RL)
- 75.5% total success rate with Qwen2.5-7B-Instruct
- Federated training approach, not directly comparable

### Summary Table (7B models, ALFWorld)

| Method | Success Rate | Credit Assignment? |
|--------|-------------|-------------------|
| GRPO | 77.6% | Episode-level |
| PPO | 80.4% | Token-level (critic) |
| RWML + RL | 87.9% | Episode-level + world model |
| GiGPO | 90.2-90.8% | Step-level (anchor states) |
| **HCAPO** | **91.4%** | Step-level (hindsight critic) |
| HCAPO + smoothing | 96.9% | Step-level + temporal |

### Key Takeaway for Our Paper

The ALFWorld landscape clearly shows credit assignment matters: methods with per-step advantages (GiGPO, HCAPO) consistently beat episode-level methods (GRPO) by 12-14 points. However, **none of these methods address M1** — they all use windowed context. This is the gap our work fills. If our approach provides full trajectory context (solving M1) with appropriate advantage estimation (solving M2), we have a clear differentiation story against HCAPO/GiGPO.

The risk: HCAPO at 91.4% (96.9% with smoothing) sets a high bar on ALFWorld specifically. We need to either (a) demonstrate that M1 matters more on harder/longer tasks, or (b) show competitive ALFWorld results while excelling on tasks where context loss is the bottleneck.
