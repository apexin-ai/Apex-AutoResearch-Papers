# research update lit section5

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 0
- **Tool calls:** 6
- **Original source:** `logs/chats/worker_research_update-lit-section5_20260521T125300.jsonl`
- **Structured JSON:** [`a02a2f80c141027f0e63.json`](../../sessions/a0/a02a2f80c141027f0e63.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

13 recorded events

### Tool call

_source line 1 · 2026-05-21T12:54:21.444890+00:00_

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
  "session": "worker_research_update-lit-section5_20260521T125300",
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

_source line 2 · 2026-05-21T12:54:21.445220+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_update-lit-section5_20260521T125300",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-21T12:54:21.445404+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "event-gated-adaptive-horizon",
  "file": "artifacts/literature/dual_critic_cross_env_literature.md",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_update-lit-section5_20260521T125300",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "event-gated-adaptive-horizon",
    "file": "artifacts/literature/dual_critic_cross_env_literature.md",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-21T12:54:21.445553+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'mistakes.yaml', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'artifacts/literature/dual_critic_cross_env_literature.md'\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_update-lit-section5_20260521T125300",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-21T12:54:21.445693+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/literature/dual_critic_cross_env_literature.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_update-lit-section5_20260521T125300",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/literature/dual_critic_cross_env_literature.md"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-21T12:54:21.445955+00:00_

1	# Dual-Critic Cross-Environment Effectiveness: Literature Survey
2	
3	**Date:** 2026-05-21
4	**Context:** DreamerV3 + dual-critic (min-of-two, TD3-style) as CIVO intervention. Walker: full prevention (NVE≤1.4). Cheetah: partial mitigation (peak NVE 1.8, 40× compression vs baseline NVE 70.64). Key finding: v1 ≈ v2 (critic difference < 0.2), suggesting implicit value regularization rather than pessimistic estimation.
5	
6	---
7	
8	## 1. Environment-Dependent Effectiveness of Bias Correction
9	
10	### 1.1 Turcato et al. 2024 — Bias Preference is Environment-Dependent
11	
12	- **Title:** Exploiting Estimation Bias in Clipped Double Q-Learning for Continuous Control Reinforcement Learning Tasks
13	- **Authors:** Turcato N., Sinigaglia A., Dalla Libera A., Carli R., Susto G.A.
14	- **Year:** 2024
15	- **Venue:** arXiv:2402.09078
16	- **Core finding:** "None of the considered update strategies performs the best among all the considered environments." Specifically:
17	  - **Walker, Ant, Hopper, Humanoid:** TD3's underestimation bias performs best
18	  - **Swimmer, Reacher:** Overestimation bias performs best
19	  - Sufficient condition for overestimation advantage: "noisy regions of the MDP correlate with the high reward"
20	- **Relevance to our finding:** Walker's reward landscape (stand + walk forward, 2 joints) favors underestimation → dual-critic's conservative bias fully prevents CIVO. Cheetah Run's reward landscape (forward speed, 6 joints, more complex coordination) may have regions where underestimation is suboptimal, explaining partial rather than full prevention.
21	
22	### 1.2 Nauman et al. 2024 — Regularization Effectiveness is Task-Dependent (Already in map: nauman2024bitter)
23	
24	- **Title:** Overestimation, Overfitting, and Plasticity in Actor-Critic: the Bitter Lesson of Reinforcement Learning
25	- **Authors:** Nauman M., Bortkiewicz M., Miłoś P., Trzcinski T., Ostaszewski M., Cygan M.
26	- **Year:** 2024
27	- **Venue:** ICML 2024
28	- **Core finding:** 
…[truncated 15293 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_update-lit-section5_20260521T125300",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-21T12:54:21.446202+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/literature/dual_critic_cross_env_literature.md",
  "old_string": "**Context:** DreamerV3 + dual-critic (min-of-two, TD3-style) as CIVO intervention. Walker: full prevention (NVE≤1.4). Cheetah: partial mitigation (peak NVE 1.8, 40× compression vs baseline NVE 70.64). Key finding: v1 ≈ v2 (critic difference < 0.2), suggesting implicit value regularization rather than pessimistic estimation.",
  "new_string": "**Context:** DreamerV3 + dual-critic (min-of-two, TD3-style) as CIVO intervention. 2×2 factorial (dual/single × narrow/scaled) reveals that neither the min operation alone nor increased capacity alone prevents CIVO on Walker; only their combination succeeds (exp_032, NVE < 1.5). Key finding: v1 ≈ v2 (critic difference < 0.2), confirming implicit regularization rather than pessimistic estimation — but this regularization requires sufficient critic capacity to be effective."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_update-lit-section5_20260521T125300",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/literature/dual_critic_cross_env_literature.md",
    "old_string": "**Context:** DreamerV3 + dual-critic (min-of-two, TD3-style) as CIVO intervention. Walker: full prevention (NVE≤1.4). Cheetah: partial mitigation (peak NVE 1.8, 40× compression vs baseline NVE 70.64). Key finding: v1 ≈ v2 (critic difference < 0.2), suggesting implicit value regularization rather than pessimistic estimation.",
    "new_string": "**Context:** DreamerV3 + dual-critic (min-of-two, TD3-style) as CIVO intervention. 2×2 factorial (dual/single × narrow/scaled) reveals that neither the min operation alone nor increased capacity alone prevents CIVO on Walker; only their combination succeeds (exp_032, NVE < 1.5). Key finding: v1 ≈ v2 (critic difference < 0.2), confirming implicit regularization rather than pessimistic estimation — but this regularization requires sufficient critic capacity to be effective."
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-21T12:54:21.446401+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/literature/dual_critic_cross_env_literature.md has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_update-lit-section5_20260521T125300",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-21T12:54:21.446577+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/literature/dual_critic_cross_env_literature.md",
  "old_string": "## 5. Synthesis: Explaining Prevention vs. Mitigation\n\n### Why Full Prevention on Walker\n\n1. **Simple reward landscape** (2 joints, stand + walk) → overestimation manifests in a lower-dimensional value function space\n2. **Dual-critic implicit regularization** (redundant parameterization, shared target convergence) is sufficient to constrain value growth in this simpler space\n3. **Short credit assignment chain** → regularization doesn't need to propagate through many imagination steps\n4. **Walker favors underestimation** (Turcato et al. 2024) → even the tiny residual pessimism from min(v1, v2) when v1 ≈ v2 helps\n\n### Why Only Mitigation on Cheetah\n\n1. **Complex reward landscape** (6 joints, forward speed) → value function has more degrees of freedom for overestimation\n2. **Implicit regularization from 2 critics is insufficient** for this higher-dimensional problem; need stronger intervention (REDQ-style larger ensembles, or explicit pessimism)\n3. **Longer credit assignment chain** (Ma et al. 2024) → regularization effect attenuates across more imagination steps\n4. **v1 ≈ v2 means no effective pessimism** → the 40× compression vs baseline is entirely from regularization, which has limits in complex environments\n5. **Task-dependent regularization effectiveness** is a general phenomenon (Nauman et al. 2024), not specific to our method\n\n### The Implicit Regularization Hypothesis\n\nThe v1 ≈ v2 finding (< 0.2 difference) is the key evidence. If dual-critic worked via pessimism, we would expect persistent v1 ≠ v2 gaps. Instead, the mechanism appears to be:\n\n1. **Redundant parameterization** → training two networks on the same target creates mutual regularization through gradient noise decorrelation\n2. **Shared target coupling** → the min operation creates a self-consistent training signal that prevents either network from diverging\n3. **Implicit capacity constraint** → maintaining two networks that must agree constrains the representational capacity available for fitting overestimated values\n4. **This is analogous to** CrossQ's finding that architectural regularization (BN) outperforms algorithmic pessimism (min-of-two)",
  "new_string": "## 5. Synthesis: Synergistic Prevention\n\n### 2×2 Factorial Evidence\n\nA controlled 2×2 factorial on Walker (dual/single × narrow/scaled) isolates the contributions of the min operation and critic capacity:\n\n| Configuration | Params | CIVO? | NVE | Interpretation |\n|--------------|--------|-------|-----|----------------|\n| Single + normal (baseline) | ~1.2M | ✓ | baseline | Reference |\n| Single + scaled (exp_033) | ~2.9M | ✓ | 4.7 | Capacity alone insufficient |\n| Dual + narrow (exp_035) | ~1.05M | ✓ | 2.75 | Min operation alone insufficient |\n| Dual + scaled (exp_032) | ~2.4M | ✗ | <1.5 | Min + capacity → prevention |\n\nThis overturns the initial \"Walker: full prevention\" characterization. The default dual-critic (2×256, ~1.05M total < baseline 1.18M) does *not* prevent CIVO (NVE 2.75). Prevention requires the combination of dual architecture and scaled capacity.\n\n### Neither Factor Alone Suffices\n\n**Min operation alone is ineffective.** In exp_035 (dual + narrow, 2×256 hidden), v1 ≈ v2 throughout training — the min operation produces no pessimism when critics have limited capacity and converge to the same function. NVE 2.75 represents marginal improvement over baseline, with CIVO still triggered. This confirms the v1 ≈ v2 convergence phenomenon (Section 2): with identical targets, data, and loss, two narrow networks learn the same function.\n\n**Capacity alone is ineffective.** In exp_033 (single + wide, ~2.9M params), the enlarged critic still reaches NVE 4.7 and triggers CIVO. More parameters without structural constraint simply provide more capacity for fitting overestimated values. This rules out a pure \"underfitting\" explanation for CIVO.\n\n### The Synergy: Implicit Regularization Requires Sufficient Capacity\n\nThe key finding is that prevention emerges only from the *interaction* of dual architecture and scaled capacity (exp_032, ~2.4M, NVE < 1.5). We hypothesize the mechanism operates in two stages:\n\n1. **Capacity enables representational diversity.** Scaled critics (≥512 hidden per critic) can maintain distinct value landscapes rather than collapsing to the same function. This is a prerequisite for the min operation to exert any pessimistic pressure.\n\n2. **The min operation constrains the diverse representations.** Given critics with enough capacity to disagree, `min(v1, v2)` selects the conservative estimate, preventing either critic's overestimation from propagating to the actor. The constraint is only meaningful when there is something to constrain.\n\nThis is analogous to CrossQ's batch normalization mechanism (Bhatt et al. 2024): BN regularization is effective only when the network has sufficient capacity for BN statistics to meaningfully decorrelate activations. In undersized networks, BN has little to regularize. Similarly, our dual-critic's implicit regularization — redundant parameterization, shared target coupling, gradient noise decorrelation — requires sufficient per-critic capacity to produce the representational diversity that makes the min operation functional.\n\n### Environment-Dependent Considerations\n\nThe 2×2 factorial was conducted on Walker. Whether the same capacity threshold applies to Cheetah remains an open question. Given Cheetah's more complex reward landscape (6 joints, forward speed optimization) and longer credit assignment chain (Ma et al. 2024), the required capacity for synergistic prevention may be higher:\n\n- **Walker** (2 joints, simple reward): ~1.2M per critic (2×512) suffices for synergy\n- **Cheetah** (6 joints, complex coordination): threshold unknown; task-dependent regularization effectiveness (Nauman et al. 2024; Turcato et al. 2024) suggests it may require larger ensembles (REDQ, N > 2; Chen et al. 2021) or stronger architectural regularization"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_update-lit-section5_20260521T125300",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/literature/dual_critic_cross_env_literature.md",
    "old_string": "## 5. Synthesis: Explaining Prevention vs. Mitigation\n\n### Why Full Prevention on Walker\n\n1. **Simple reward landscape** (2 joints, stand + walk) → overestimation manifests in a lower-dimensional value function space\n2. **Dual-critic implicit regularization** (redundant parameterization, shared target convergence) is sufficient to constrain value growth in this simpler space\n3. **Short credit assignment chain** → regularization doesn't need to propagate through many imagination steps\n4. **Walker favors underestimation** (Turcato et al. 2024) → even the tiny residual pessimism from min(v1, v2) when v1 ≈ v2 helps\n\n### Why Only Mitigation on Cheetah\n\n1. **Complex reward landscape** (6 joints, forward speed) → value function has more degrees of freedom for overestimation\n2. **Implicit regularization from 2 critics is insufficient** for this higher-dimensional problem; need stronger intervention (REDQ-style larger ensembles, or explicit pessimism)\n3. **Longer credit assignment chain** (Ma et al. 2024) → regularization effect attenuates across more imagination steps\n4. **v1 ≈ v2 means no effective pessimism** → the 40× compression vs baseline is entirely from regularization, which has limits in complex environments\n5. **Task-dependent regularization effectiveness** is a general phenomenon (Nauman et al. 2024), not specific to our method\n\n### The Implicit Regularization Hypothesis\n\nThe v1 ≈ v2 finding (< 0.2 difference) is the key evidence. If dual-critic worked via pessimism, we would expect persistent v1 ≠ v2 gaps. Instead, the mechanism appears to be:\n\n1. **Redundant parameterization** → training two networks on the same target creates mutual regularization through gradient noise decorrelation\n2. **Shared target coupling** → the min operation creates a self-consistent training signal that prevents either network from diverging\n3. **Implicit capacity constraint** → maintaining two networks that must agree constrains the representational capacity available for fitting overestimated values\n4. **This is analogous to** CrossQ's finding that architectural regularization (BN) outperforms algorithmic pessimism (min-of-two)",
    "new_string": "## 5. Synthesis: Synergistic Prevention\n\n### 2×2 Factorial Evidence\n\nA controlled 2×2 factorial on Walker (dual/single × narrow/scaled) isolates the contributions of the min operation and critic capacity:\n\n| Configuration | Params | CIVO? | NVE | Interpretation |\n|--------------|--------|-------|-----|----------------|\n| Single + normal (baseline) | ~1.2M | ✓ | baseline | Reference |\n| Single + scaled (exp_033) | ~2.9M | ✓ | 4.7 | Capacity alone insufficient |\n| Dual + narrow (exp_035) | ~1.05M | ✓ | 2.75 | Min operation alone insufficient |\n| Dual + scaled (exp_032) | ~2.4M | ✗ | <1.5 | Min + capacity → prevention |\n\nThis overturns the initial \"Walker: full prevention\" characterization. The default dual-critic (2×256, ~1.05M total < baseline 1.18M) does *not* prevent CIVO (NVE 2.75). Prevention requires the combination of dual architecture and scaled capacity.\n\n### Neither Factor Alone Suffices\n\n**Min operation alone is ineffective.** In exp_035 (dual + narrow, 2×256 hidden), v1 ≈ v2 throughout training — the min operation produces no pessimism when critics have limited capacity and converge to the same function. NVE 2.75 represents marginal improvement over baseline, with CIVO still triggered. This confirms the v1 ≈ v2 convergence phenomenon (Section 2): with identical targets, data, and loss, two narrow networks learn the same function.\n\n**Capacity alone is ineffective.** In exp_033 (single + wide, ~2.9M params), the enlarged critic still reaches NVE 4.7 and triggers CIVO. More parameters without structural constraint simply provide more capacity for fitting overestimated values. This rules out a pure \"underfitting\" explanation for CIVO.\n\n### The Synergy: Implicit Regularization Requires Sufficient Capacity\n\nThe key finding is that prevention emerges only from the *interaction* of dual architecture and scaled capacity (exp_032, ~2.4M, NVE < 1.5). We hypothesize the mechanism operates in two stages:\n\n1. **Capacity enables representational diversity.** Scaled critics (≥512 hidden per critic) can maintain distinct value landscapes rather than collapsing to the same function. This is a prerequisite for the min operation to exert any pessimistic pressure.\n\n2. **The min operation constrains the diverse representations.** Given critics with enough capacity to disagree, `min(v1, v2)` selects the conservative estimate, preventing either critic's overestimation from propagating to the actor. The constraint is only meaningful when there is something to constrain.\n\nThis is analogous to CrossQ's batch normalization mechanism (Bhatt et al. 2024): BN regularization is effective only when the network has sufficient capacity for BN statistics to meaningfully decorrelate activations. In undersized networks, BN has little to regularize. Similarly, our dual-critic's implicit regularization — redundant parameterization, shared target coupling, gradient noise decorrelation — requires sufficient per-critic capacity to produce the representational diversity that makes the min operation functional.\n\n### Environment-Dependent Considerations\n\nThe 2×2 factorial was conducted on Walker. Whether the same capacity threshold applies to Cheetah remains an open question. Given Cheetah's more complex reward landscape (6 joints, forward speed optimization) and longer credit assignment chain (Ma et al. 2024), the required capacity for synergistic prevention may be higher:\n\n- **Walker** (2 joints, simple reward): ~1.2M per critic (2×512) suffices for synergy\n- **Cheetah** (6 joints, complex coordination): threshold unknown; task-dependent regularization effectiveness (Nauman et al. 2024; Turcato et al. 2024) suggests it may require larger ensembles (REDQ, N > 2; Chen et al. 2021) or stronger architectural regularization"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-21T12:54:21.446875+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/literature/dual_critic_cross_env_literature.md has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_update-lit-section5_20260521T125300",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-21T12:54:21.447057+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/literature/dual_critic_cross_env_literature.md",
  "offset": "139",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_update-lit-section5_20260521T125300",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/literature/dual_critic_cross_env_literature.md",
    "offset": "139",
    "limit": "50"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-21T12:54:21.447225+00:00_

139	
140	## 5. Synthesis: Synergistic Prevention
141	
142	### 2×2 Factorial Evidence
143	
144	A controlled 2×2 factorial on Walker (dual/single × narrow/scaled) isolates the contributions of the min operation and critic capacity:
145	
146	| Configuration | Params | CIVO? | NVE | Interpretation |
147	|--------------|--------|-------|-----|----------------|
148	| Single + normal (baseline) | ~1.2M | ✓ | baseline | Reference |
149	| Single + scaled (exp_033) | ~2.9M | ✓ | 4.7 | Capacity alone insufficient |
150	| Dual + narrow (exp_035) | ~1.05M | ✓ | 2.75 | Min operation alone insufficient |
151	| Dual + scaled (exp_032) | ~2.4M | ✗ | <1.5 | Min + capacity → prevention |
152	
153	This overturns the initial "Walker: full prevention" characterization. The default dual-critic (2×256, ~1.05M total < baseline 1.18M) does *not* prevent CIVO (NVE 2.75). Prevention requires the combination of dual architecture and scaled capacity.
154	
155	### Neither Factor Alone Suffices
156	
157	**Min operation alone is ineffective.** In exp_035 (dual + narrow, 2×256 hidden), v1 ≈ v2 throughout training — the min operation produces no pessimism when critics have limited capacity and converge to the same function. NVE 2.75 represents marginal improvement over baseline, with CIVO still triggered. This confirms the v1 ≈ v2 convergence phenomenon (Section 2): with identical targets, data, and loss, two narrow networks learn the same function.
158	
159	**Capacity alone is ineffective.** In exp_033 (single + wide, ~2.9M params), the enlarged critic still reaches NVE 4.7 and triggers CIVO. More parameters without structural constraint simply provide more capacity for fitting overestimated values. This rules out a pure "underfitting" explanation for CIVO.
160	
161	### The Synergy: Implicit Regularization Requires Sufficient Capacity
162	
163	The key finding is that prevention emerges only from the *interaction* of dual architecture and scaled capacity (exp_032, ~2.4M, NVE < 1.5). We hypothesize th
…[truncated 2469 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_update-lit-section5_20260521T125300",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-21T12:54:21.447420+00:00_

Section 5 updated. Changes made:

1. **Context header** (line 4): Updated from "Walker: full prevention" to reflect 2×2 factorial findings — prevention requires min + capacity synergy.

2. **Section 5 title**: "Prevention vs. Mitigation" → "Synergistic Prevention"

3. **New structure with four subsections**:
   - **2×2 Factorial Evidence**: Summary table with all four conditions (baseline, exp_033, exp_035, exp_032) and their NVE/CIVO outcomes
   - **Neither Factor Alone Suffices**: min operation alone → v1≈v2 convergence, no pessimism (exp_035); capacity alone → more room for overestimation (exp_033)
   - **The Synergy**: Two-stage mechanism hypothesis — capacity enables representational diversity, min operation constrains it. CrossQ BN analogy for why regularization needs sufficient capacity.
   - **Environment-Dependent Considerations**: Walker threshold established (~1.2M per critic), Cheetah threshold unknown, with literature pointers for why it may be higher.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_update-lit-section5_20260521T125300"
}
```

</details>

---
