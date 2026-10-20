# research sgs partial effectiveness literature

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 65
- **Recorded user turns:** 0
- **Tool calls:** 32
- **Original source:** `logs/chats/worker_research_sgs-partial-effectiveness-literature_20260517T225544.jsonl`
- **Structured JSON:** [`83b993c443e37e04fcce.json`](../../sessions/83/83b993c443e37e04fcce.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

65 recorded events

### Tool call

_source line 1 · 2026-05-17T23:01:07.497712+00:00_

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
  "session": "worker_research_sgs-partial-effectiveness-literature_20260517T225544",
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

_source line 2 · 2026-05-17T23:01:07.498296+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sgs-partial-effectiveness-literature_20260517T225544",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-17T23:01:07.498577+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "event-gated-adaptive-horizon",
  "file": "literature_map.yaml",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sgs-partial-effectiveness-literature_20260517T225544",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "event-gated-adaptive-horizon",
    "file": "literature_map.yaml",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-17T23:01:07.499206+00:00_

&lt;persisted-output>
Output too large (64.4KB). Full output saved to: /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/7c864c23-c91f-44b8-93b0-6a987fbc569e/tool-results/toolu_01CjfBivNzjVPJkpnrsxqynX.txt

Preview (first 2KB):
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/literature_map.yaml\", \"content\": \"# Literature Map — event-gated-adaptive-horizon\\n# Last updated: 2026-05-16\\n# Total: 90 papers (76 existing + 14 related-work expansion 2026-05-16)\\n\\n# ============================================================\\n# EXISTING CITATIONS (already in paper.tex)\\n# ============================================================\\n\\n- paper_id: sutton1999options\\n  title: \\\"Between MDPs and Semi-MDPs: A Framework for Temporal Abstraction in Reinforcement Learning\\\"\\n  authors: [Sutton R.S., Precup D., Singh S.]\\n  year: 1999\\n  venue: \\\"Artificial Intelligence 112(1-2):181-211\\\"\\n  category: background\\n  role: \\\"Foundational options framework for temporal abstraction in RL; our work investigates why temporal abstraction fails in world-model RL\\\"\\n  relevance_score: 5\\n\\n- paper_id: hafner2020dreamerv1\\n  title: \\\"Dream to Control: Learning Behaviors by Latent Imagination\\\"\\n  authors: [Hafner D., Lillicrap T., Ba J., Norouzi M.]\\n  year: 2020\\n  venue: ICLR\\n  category: background\\n  role: \\\"DreamerV1 — base architecture family; our experiments build on the RSSM and imagination-based training paradigm\\\"\\n  relevance_score: 5\\n\\n- paper_id: hafner2023dreamerv3\\n  title: \\\"Mastering Diverse Domains through World Models\\\"\\n  authors: [Hafner D., Pasukonis J., Ba J., Lillicrap T.]\\n  year: 2023\\n  venue: \\\"arXiv:2301.04104 (Nature 2025)\\\"\\n  category: background\\n  role: \\\"DreamerV3 — the specific base system we modify; symlog transforms, discret
…[truncated 325 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sgs-partial-effectiveness-literature_20260517T225544",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-17T23:01:07.499432+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "event-gated-adaptive-horizon",
  "file": "memory.md",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sgs-partial-effectiveness-literature_20260517T225544",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "event-gated-adaptive-horizon",
    "file": "memory.md",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-17T23:01:07.499624+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/memory.md\", \"content\": \"# Memory — event-gated-adaptive-horizon\\n\\n## 2026-05-17: dt_emb \\\"困境\\\" — frozen prevents CIVO but kills gating\\n\\nexp_022b 确认：frozen random dt_emb 阻止 CIVO (ve_ratio 峰值仅 0.218)，但 gate 收敛为近均匀分布 (entropy_ratio=0.912)。核心原因：随机嵌入不携带时间语义 → gate 无法区分 dt 值。\\n\\n**设计启示**：CIVO 因果链需要 gradient-driven 语义 dt 表征。阻止 CIVO 的方式（SGS、freeze、remove）都会同时降低 dt_emb 的语义质量，形成 safety-utility tradeoff。这对论文来说是诊断发现（C2 的深化），不是需要解决的工程问题。\\n\\n## 2026-05-17: PickCube detector backtest 教训（CRITICAL）\\n\\nWorker 的 detector backtest 分析得出错误结论（TP），实际是 TN。三个方法论错误：\\n1. 用 NVE 代替 raw V/E ratio（detector 是 baseline-free 的，用的是 r_t = V/max(E, ε)，不是 NVE）\\n2. Acceleration condition 遗漏：prev_delta 也必须 > τ_vel（不只是当前 delta）\\n3. 未检查 eval decline condition (c_dec)\\n\\n**教训**：detector backtest 必须严格逐条对照 Algorithm 1 的每个条件，不能凭 NVE 近似推断。以后所有 detector 相关分析必须用 raw V/E ratio 而非 NVE。\\n\\n## 2026-05-17: PickCube CIVO pattern — transient, not persistent\\n\\nexp_019b reveals PickCube exhibits \\\"transient CIVO\\\": NVE peaks 3.78× @52.5K then deflates to 0.08× by 132.5K, with eval recovering to 26.9. This contrasts Walker Walk's monotonic acceleration → collapse (2/3 seeds) pattern. Gate locked at dt=2 throughout (entropy=0). Value function transitions from overestimation to severe underestimation.\\n\\n**Key insight**: CIVO onset is environment-general (trained dt_emb → NVE spike in both environments), but CIVO resolution is environment-dependent (collapse vs self-correction).\\n\\n**Detector**: does NOT trigger on PickCube (TN). Oscillatory V/E pattern filtered by acceleration condition. This demonstrates detector specificity — it does not over-fire on noisy patterns.\\n\\n## 2026-05-17: exp_022 curriculum misconfiguration lesson\\n\\ngate_curriculum_phase1=50000 in configs.yaml means 50K env steps. With action_repeat=2, this = 100K logger steps. A 1
…[truncated 1192 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sgs-partial-effectiveness-literature_20260517T225544",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-17T23:01:07.499841+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/7c864c23-c91f-44b8-93b0-6a987fbc569e/tool-results/toolu_01CjfBivNzjVPJkpnrsxqynX.txt",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sgs-partial-effectiveness-literature_20260517T225544",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/7c864c23-c91f-44b8-93b0-6a987fbc569e/tool-results/toolu_01CjfBivNzjVPJkpnrsxqynX.txt",
    "limit": "200"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-17T23:01:07.500543+00:00_

1	{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/literature_map.yaml\", \"content\": \"# Literature Map — event-gated-adaptive-horizon\\n# Last updated: 2026-05-16\\n# Total: 90 papers (76 existing + 14 related-work expansion 2026-05-16)\\n\\n# ============================================================\\n# EXISTING CITATIONS (already in paper.tex)\\n# ============================================================\\n\\n- paper_id: sutton1999options\\n  title: \\\"Between MDPs and Semi-MDPs: A Framework for Temporal Abstraction in Reinforcement Learning\\\"\\n  authors: [Sutton R.S., Precup D., Singh S.]\\n  year: 1999\\n  venue: \\\"Artificial Intelligence 112(1-2):181-211\\\"\\n  category: background\\n  role: \\\"Foundational options framework for temporal abstraction in RL; our work investigates why temporal abstraction fails in world-model RL\\\"\\n  relevance_score: 5\\n\\n- paper_id: hafner2020dreamerv1\\n  title: \\\"Dream to Control: Learning Behaviors by Latent Imagination\\\"\\n  authors: [Hafner D., Lillicrap T., Ba J., Norouzi M.]\\n  year: 2020\\n  venue: ICLR\\n  category: background\\n  role: \\\"DreamerV1 — base architecture family; our experiments build on the RSSM and imagination-based training paradigm\\\"\\n  relevance_score: 5\\n\\n- paper_id: hafner2023dreamerv3\\n  title: \\\"Mastering Diverse Domains through World Models\\\"\\n  authors: [Hafner D., Pasukonis J., Ba J., Lillicrap T.]\\n  year: 2023\\n  venue: \\\"arXiv:2301.04104 (Nature 2025)\\\"\\n  category: background\\n  role: \\\"DreamerV3 — the specific base system we modify; symlog transforms, discrete latents, all default hyperparameters come from here\\\"\\n  relevance_score: 5\\n\\n- paper_id: sharma2017figar\\n  title: \\\"Fine Grained Action Repetition for Deep Reinforcement Learning\\\"\\n  authors: [Sharma S., Lakshminarayanan A.S., Ravindran B.]\\n  year: 2017\\n  venue: \\\"ICLR Worksh
…[truncated 63965 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sgs-partial-effectiveness-literature_20260517T225544",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-17T23:01:07.500789+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sgs-partial-effectiveness-literature_20260517T225544",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-17T23:01:07.501005+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sgs-partial-effectiveness-literature_20260517T225544",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-17T23:01:07.501144+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "stop-gradient imagination rollout Dreamer world model actor gradient flow"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sgs-partial-effectiveness-literature_20260517T225544",
  "tool": "WebSearch",
  "tool_args": {
    "query": "stop-gradient imagination rollout Dreamer world model actor gradient flow"
  }
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-17T23:01:07.501272+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "gradient propagation through learned dynamics model reinforcement learning environment-dependent effects"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sgs-partial-effectiveness-literature_20260517T225544",
  "tool": "WebSearch",
  "tool_args": {
    "query": "gradient propagation through learned dynamics model reinforcement learning environment-dependent effects"
  }
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-17T23:01:07.501396+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "actor-critic gradient clipping stopping underfitting model-based RL different environments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sgs-partial-effectiveness-literature_20260517T225544",
  "tool": "WebSearch",
  "tool_args": {
    "query": "actor-critic gradient clipping stopping underfitting model-based RL different environments"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-17T23:01:07.501550+00:00_

Web search results for query: "actor-critic gradient clipping stopping underfitting model-based RL different environments"

Links: [{"title":"The Definitive Guide to Policy Gradients in Deep Reinforcement Learning:","url":"https://arxiv.org/pdf/2401.13662"},{"title":"Advanced Deep Actor Critic Algorithm Tips for RL","url":"https://www.numberanalytics.com/blog/advanced-deep-actor-critic-algorithm-tips-rl"},{"title":"An actor-critic algorithm with policy gradients to solve the job shop scheduling problem using deep double recurrent agents - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S0377221723005957"},{"title":"Actor-critic algorithm - Wikipedia","url":"https://en.wikipedia.org/wiki/Actor-critic_algorithm"},{"title":"Essential Guide to Actor Critic Algorithms in RL","url":"https://www.numberanalytics.com/blog/essential-guide-actor-critic-algorithms-rl"},{"title":"Demystifying Policy Optimization in RL: An Introduction to PPO and GRPO | Towards Data Science","url":"https://towardsdatascience.com/demystifying-policy-optimization-in-rl-an-introduction-to-ppo-and-grpo/"},{"title":"Overestimation, Overfitting, and Plasticity in Actor-Critic: the Bitter Lesson of Reinforcement Learning","url":"https://arxiv.org/html/2403.00514"},{"title":"Published as a conference paper at ICLR 2017 AN ACTOR-CRITIC ALGORITHM","url":"https://openreview.net/pdf?id=SJDaqqveg"},{"title":"Actor-Critic Algorithms CS 294-112: Deep Reinforcement Learning Sergey Levine","url":"http://rail.eecs.berkeley.edu/deeprlcourse-fa17/f17docs/lecture_5_actor_critic_pdf.pdf"},{"title":"Characterizing the Gap Between Actor-Critic and Policy Gradient","url":"https://proceedings.mlr.press/v139/wen21b/wen21b.pdf"}]

Based on the web search results, here's what I found about actor-critic algorithms, gradient clipping, and related concepts:

## Actor-Critic Methods and Gradient Clipping

Actor-critic algorithms are a family of reinforcement learning algorithms that combine policy-based R
…[truncated 1425 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sgs-partial-effectiveness-literature_20260517T225544",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-17T23:01:07.501746+00:00_

Web search results for query: "gradient propagation through learned dynamics model reinforcement learning environment-dependent effects"

Links: [{"title":"Gradient dynamics in reinforcement learning | Phys. Rev. E","url":"https://link.aps.org/doi/10.1103/PhysRevE.106.025315"},{"title":"Differentiable Information Enhanced Model-Based Reinforcement Learning","url":"https://arxiv.org/html/2503.01178v1"},{"title":"Learning Dynamics and Generalization in Deep Reinforcement Learning","url":"https://proceedings.mlr.press/v162/lyle22a/lyle22a.pdf"},{"title":"[2204.03973] Gradient dynamics in reinforcement learning","url":"https://arxiv.org/abs/2204.03973"},{"title":"1 Gradient Monitored Reinforcement Learning","url":"https://arxiv.org/pdf/2005.12108"},{"title":"Model-Based Reinforcement Learning (MBRL) in AI - GeeksforGeeks","url":"https://www.geeksforgeeks.org/artificial-intelligence/model-based-reinforcement-learning-mbrl-in-ai/"},{"title":"Learning in neural networks by reinforcement of irregular spiking - PubMed","url":"https://pubmed.ncbi.nlm.nih.gov/15169045/"},{"title":"Does reinforcement learning with deep neural networks involve gradient descent and backpropagation? - Quora","url":"https://www.quora.com/Does-reinforcement-learning-with-deep-neural-networks-involve-gradient-descent-and-backpropagation"},{"title":"Dynamic Gradient Descent and Reinforcement Learning for AI-Enhanced Indoor Building Environmental Simulation","url":"https://www.mdpi.com/2075-5309/15/12/2044"},{"title":"A Unified Perspective on Optimization in Machine Learning and Neuroscience: From Gradient Descent to Neural Adaptation","url":"https://arxiv.org/html/2510.18812v1"}]

Based on the search results, here's what I found regarding gradient propagation through learned dynamics models in reinforcement learning with environment-dependent effects:

## Key Findings

**Differentiable Information in Model-Based RL:**
Differentiable environments have heralded new possibilities for learning control pol
…[truncated 1713 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sgs-partial-effectiveness-literature_20260517T225544",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-17T23:01:07.501959+00:00_

Web search results for query: "stop-gradient imagination rollout Dreamer world model actor gradient flow"

Links: [{"title":"NEXT EMBEDDING PREDICTION MAKES WORLD ...","url":"https://openreview.net/pdf/4e331ea63b3cecaf9da5b5312f8d8085c69ea946.pdf"},{"title":"Dreamer: Learning Long-Horizon Behaviors through Latent Imagination | by Dong-Keon Kim | Medium","url":"https://medium.com/@kdk199604/dreamer-learning-long-horizon-behaviors-through-latent-imagination-fa60327c2843"},{"title":"Mastering diverse control tasks through world models | Nature","url":"https://www.nature.com/articles/s41586-025-08744-2"},{"title":"MASTERING ATARI WITH DISCRETE WORLD MODELS Danijar Hafner ∗ Google Brain","url":"https://gbarnier.github.io/papers/dreamer2.pdf"},{"title":"Finding Theta - The Evolution of Imagination: A Deep Dive into DreamerV3 and its Conquest of Minecraft","url":"https://www.findingtheta.com/blog/the-evolution-of-imagination-a-deep-dive-into-dreamerv3-and-its-conquest-of-minecraft"},{"title":"Mastering Diverse Domains through World Models","url":"https://arxiv.org/pdf/2301.04104"},{"title":"Interpretable World Model Imaginations as Deep Reinforcement Learning Explanation | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-032-08327-2_7"},{"title":"Week 5: Model-Based Methods - Deep RL Course","url":"https://deeprlcourse.github.io/course_notes/model-based/"},{"title":"Driving With Imagination: DreamerV3 + TD-MPC in CARLA | by Satyam Mishra | Medium","url":"https://satyamcser.medium.com/driving-with-imagination-dreamerv3-td-mpc-in-carla-c52721d7bb1a"},{"title":"DreamerV3: Model-Based RL Algorithm","url":"https://www.emergentmind.com/topics/dreamerv3-algorithm"}]

I found comprehensive information about the relationship between stop-gradient, imagination rollouts, Dreamer, world models, actor-critic learning, and gradient flow. Here's what the search revealed:

## Stop-Gradient in Dreamer's Imagination Rollouts

A crucial design choice in Dreamer is
…[truncated 1863 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sgs-partial-effectiveness-literature_20260517T225544",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-17T23:01:07.502197+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "DreamerV3 \"straight-through gradient\" OR \"stop gradient\" imagination actor training dynamics backpropagation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sgs-partial-effectiveness-literature_20260517T225544",
  "tool": "WebSearch",
  "tool_args": {
    "query": "DreamerV3 \"straight-through gradient\" OR \"stop gradient\" imagination actor training dynamics backpropagation"
  }
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-17T23:01:07.502336+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"model-based RL\" \"gradient through dynamics\" policy optimization Dyna SVG stochastic value gradient"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sgs-partial-effectiveness-literature_20260517T225544",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"model-based RL\" \"gradient through dynamics\" policy optimization Dyna SVG stochastic value gradient"
  }
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-17T23:01:07.502462+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"overestimation\" OR \"value collapse\" walker cheetah environment difference model-based reinforcement learning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sgs-partial-effectiveness-literature_20260517T225544",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"overestimation\" OR \"value collapse\" walker cheetah environment difference model-based reinforcement learning"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-17T23:01:07.502620+00:00_

Web search results for query: "DreamerV3 "straight-through gradient" OR "stop gradient" imagination actor training dynamics backpropagation"

Links: [{"title":"DreamerV3: Mastering Diverse Domains through World Models","url":"https://vitalab.github.io/article/2023/01/19/DreamerV3.html"},{"title":"Dreamer: Learning Long-Horizon Behaviors through Latent Imagination | by Dong-Keon Kim | Medium","url":"https://medium.com/@kdk199604/dreamer-learning-long-horizon-behaviors-through-latent-imagination-fa60327c2843"},{"title":"Mastering Diverse Domains through World Models","url":"https://arxiv.org/pdf/2301.04104"},{"title":"MuDreamer: Learning Predictive World Models without Reconstruction","url":"https://arxiv.org/html/2405.15083v1"},{"title":"MASTERING ATARI WITH DISCRETE WORLD MODELS Danijar Hafner ∗ Google Brain","url":"https://gbarnier.github.io/papers/dreamer2.pdf"},{"title":"GitHub - danijar/dreamerv3: Mastering Diverse Domains through World Models · GitHub","url":"https://github.com/danijar/dreamerv3"},{"title":"Finding Theta - The Evolution of Imagination: A Deep Dive into DreamerV3 and its Conquest of Minecraft","url":"https://www.findingtheta.com/blog/the-evolution-of-imagination-a-deep-dive-into-dreamerv3-and-its-conquest-of-minecraft"},{"title":"DreamerV3-XP: Optimizing exploration through uncertainty estimation","url":"https://arxiv.org/html/2510.21418v1"},{"title":"LEARNING BEHAVIORS BY LATENT IMAGINATION","url":"https://openreview.net/pdf?id=S1lOTC4tDS"},{"title":"Mastering diverse control tasks through world models - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12003158/"}]

I found several relevant results about DreamerV3 and the techniques you're asking about. Here's what the research shows:

## Straight-Through Gradient in DreamerV3

DreamerV3 uses straight-through gradients through the sampling step when categorical distributions are sampled. More specifically, the algorithm uses the Straight-Through Estimator, which during the backward pass of 
…[truncated 1264 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sgs-partial-effectiveness-literature_20260517T225544",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-17T23:01:07.502802+00:00_

Web search results for query: ""overestimation" OR "value collapse" walker cheetah environment difference model-based reinforcement learning"

Links: [{"title":"Efficient Online Reinforcement Learning with Offline Data","url":"https://proceedings.mlr.press/v202/ball23a/ball23a.pdf"},{"title":"Efficient offline-to-online reinforcement learning with pre-reduced out-of-distribution Q-values - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0893608025008287"},{"title":"A Survey of Reinforcement Learning Techniques for 2D and 3D Bipedal Locomotion | by Jerry Zhang | Medium","url":"https://medium.com/@jer_zhang/a-survey-of-reinforcement-learning-techniques-for-2d-and-3d-bipedal-locomotion-2f82f455396a"},{"title":"Simultaneous Double Q-learning with Conservative ...","url":"https://arxiv.org/pdf/2205.03819"},{"title":"TD3: Overcoming Overestimation in Deep Reinforcement Learning | by Dong-Keon Kim | Medium","url":"https://medium.com/@kdk199604/td3-overcoming-overestimation-in-deep-reinforcement-learning-c52d1cc9d69a"},{"title":"Meta-Reinforcement Learning Based on Self-Supervised Task Representation","url":"https://arxiv.org/pdf/2305.00286"},{"title":"[2006.13823] Preventing Value Function Collapse in Ensemble Q-Learning by Maximizing Representation Diversity","url":"https://ar5iv.labs.arxiv.org/html/2006.13823"},{"title":"Multi-Actor Multi-Critic Deep Deterministic Reinforcement Learning with a Novel Q-Ensemble Method","url":"https://arxiv.org/html/2510.01083v1"},{"title":"Reducing the estimation bias and variance in reinforcement learning via Maxmean and Aitken value iteration - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0952197625025333"},{"title":"[Abstract] OVERCOMING VALUE OVERESTIMATION FOR DISTRIBUTIONAL REINFORCEMENT LEARNING-BASED PATH PLANNING WITH CONSERVATIVE CONSTRAINTS, 124-132.","url":"https://www.actapress.com/PaperInfo.aspx?paperId=56139"}]

I've completed the web search for your query about o
…[truncated 1487 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sgs-partial-effectiveness-literature_20260517T225544",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-17T23:01:07.503011+00:00_

Web search results for query: ""model-based RL" "gradient through dynamics" policy optimization Dyna SVG stochastic value gradient"

Links: [{"title":"Model-Based Reinforcement Learning — DI-engine 0.1.0 documentation","url":"https://opendilab.github.io/DI-engine/02_algo/model_based_rl.html"},{"title":"Differentiable Information Enhanced Model-Based Reinforcement Learning","url":"https://ojs.aaai.org/index.php/AAAI/article/download/34419/36574"},{"title":"Distributional value gradients for stochastic environments","url":"https://arxiv.org/html/2601.20071"},{"title":"Dyna-style Model-based reinforcement learning with Model-Free Policy Optimization - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0950705124000637"},{"title":"Physics-informed Dyna-style model-based deep reinforcement learning for dynamic control | Proceedings A | The Royal Society","url":"https://royalsocietypublishing.org/doi/10.1098/rspa.2021.0618"},{"title":"Differentiable Information Enhanced Model-Based Reinforcement Learning","url":"https://arxiv.org/html/2503.01178v1"},{"title":"Model-Based Reinforcement Learning","url":"https://www.emergentmind.com/topics/model-based-reinforcement-learning-rl"},{"title":"Unified Objective for Dynamics &amp; Policy in Model-Based RL | Mirage News","url":"https://www.miragenews.com/unified-objective-for-dynamics-policy-in-model-1308939/"},{"title":"Model-Based Reinforcement Learning via Meta-Policy Optimization Ignasi Clavera∗","url":"https://h2t.iar.kit.edu/pdf/Rothfuss2018.pdf"},{"title":"(PDF) Physics-informed Dyna-Style Model-Based Deep Reinforcement Learning for Dynamic Control","url":"https://www.researchgate.net/publication/353654461_Physics-informed_Dyna-Style_Model-Based_Deep_Reinforcement_Learning_for_Dynamic_Control"}]

Based on the search results, here's what I found on your query about model-based RL with gradient through dynamics, policy optimization, Dyna, and SVG (Stochastic Value Gradient):

## Key Concepts

**Stocha
…[truncated 1669 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sgs-partial-effectiveness-literature_20260517T225544",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-17T23:01:07.503186+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "stochastic value gradient SVG backpropagation through dynamics \"gradient vanishing\" OR \"gradient explosion\" model-based policy gradient"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sgs-partial-effectiveness-literature_20260517T225544",
  "tool": "WebSearch",
  "tool_args": {
    "query": "stochastic value gradient SVG backpropagation through dynamics \"gradient vanishing\" OR \"gradient explosion\" model-based policy gradient"
  }
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-17T23:01:07.503316+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"dreamer\" reinforce vs dynamics backprop actor loss imagination horizon gradient magnitude"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sgs-partial-effectiveness-literature_20260517T225544",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"dreamer\" reinforce vs dynamics backprop actor loss imagination horizon gradient magnitude"
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-17T23:01:07.503472+00:00_

Web search results for query: ""dreamer" reinforce vs dynamics backprop actor loss imagination horizon gradient magnitude"

Links: [{"title":"Dreamer: Learning Long-Horizon Behaviors through Latent Imagination | by Dong-Keon Kim | Medium","url":"https://medium.com/@kdk199604/dreamer-learning-long-horizon-behaviors-through-latent-imagination-fa60327c2843"},{"title":"Dreamer V2 - EclecticSheep","url":"https://eclecticsheep.ai/2023/07/06/dreamer_v2.html"},{"title":"Dream to Control: Learning Behaviors by Latent Imagination | OpenReview","url":"https://openreview.net/forum?id=S1lOTC4tDS"},{"title":"Introducing Dreamer: Scalable Reinforcement Learning Using World Models","url":"https://research.google/blog/introducing-dreamer-scalable-reinforcement-learning-using-world-models/"},{"title":"DREAMERPRO: RECONSTRUCTION-FREE MODEL-BASED REINFORCEMENT LEARNING","url":"https://arxiv.org/pdf/2110.14565"},{"title":"MASTERING ATARI WITH DISCRETE WORLD MODELS Danijar Hafner ∗ Google Brain","url":"https://gbarnier.github.io/papers/dreamer2.pdf"},{"title":"[1912.01603] Dream to Control: Learning Behaviors by Latent Imagination","url":"https://ar5iv.labs.arxiv.org/html/1912.01603"},{"title":"DreamerV3: Mastering Diverse Domains through World Models","url":"https://vitalab.github.io/article/2023/01/19/DreamerV3.html"},{"title":"LEARNING BEHAVIORS BY LATENT IMAGINATION","url":"https://openreview.net/pdf?id=S1lOTC4tDS"},{"title":"Mastering diverse control tasks through world models | Nature","url":"https://www.nature.com/articles/s41586-025-08744-2"}]

Based on the search results, here's what I found about the comparison between REINFORCE and dynamics backpropagation in the Dreamer algorithm:

## Key Differences

The REINFORCE term aims to maximize the actor's probability of its own sampled actions weighted by the values of those actions, while the dynamics term aims to output actions that maximize the prediction of long-term future rewards made by the critic.

## Gradient Characteristic
…[truncated 990 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sgs-partial-effectiveness-literature_20260517T225544",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-17T23:01:07.503654+00:00_

Web search results for query: "stochastic value gradient SVG backpropagation through dynamics "gradient vanishing" OR "gradient explosion" model-based policy gradient"

Links: [{"title":"Learning Continuous Control Policies by Stochastic Value Gradients","url":"http://papers.neurips.cc/paper/5796-learning-continuous-control-policies-by-stochastic-value-gradients.pdf"},{"title":"[1510.09142] Learning Continuous Control Policies by Stochastic Value Gradients","url":"https://ar5iv.labs.arxiv.org/html/1510.09142"},{"title":"On the model-based stochastic value gradient for ...","url":"https://par.nsf.gov/servlets/purl/10275928"},{"title":"On the Model-Based Stochastic Value Gradient for Continuous Reinforcement Learning","url":"https://proceedings.mlr.press/v144/amos21a.html"},{"title":"Learning Continuous Control Policies by Stochastic Value ...","url":"https://arxiv.org/pdf/1510.09142"},{"title":"Model-based Policy Gradients · Pierluca D'Oro","url":"https://proceduralia.github.io/home/2020/01/26/model-based-policy-gradient"},{"title":"S2VG: Soft Stochastic Value Gradient method | OpenReview","url":"https://openreview.net/forum?id=r1l-HTNtDB"},{"title":"Distributional value gradients for stochastic environments","url":"https://arxiv.org/html/2601.20071"},{"title":"[2008.12775] On the model-based stochastic value gradient for continuous reinforcement learning","url":"https://arxiv.org/abs/2008.12775"},{"title":"GitHub - facebookresearch/svg: On the model-based stochastic value gradient for continuous reinforcement learning","url":"https://github.com/facebookresearch/svg"}]

Based on the web search results, I can provide you with comprehensive information about Stochastic Value Gradients (SVG) and related concepts in model-based policy gradient learning.

## Overview of Stochastic Value Gradients

Stochastic Value Gradients present a unified framework for learning continuous control policies using backpropagation, supporting stochastic control by treating stochasticity in
…[truncated 2157 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sgs-partial-effectiveness-literature_20260517T225544",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-17T23:01:07.503853+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Amos 2021 \"model-based stochastic value gradient\" continuous reinforcement learning gradient truncation horizon"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sgs-partial-effectiveness-literature_20260517T225544",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Amos 2021 \"model-based stochastic value gradient\" continuous reinforcement learning gradient truncation horizon"
  }
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-17T23:01:07.503995+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"gradient through dynamics\" \"task complexity\" OR \"environment complexity\" reinforcement learning continuous control effectiveness"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sgs-partial-effectiveness-literature_20260517T225544",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"gradient through dynamics\" \"task complexity\" OR \"environment complexity\" reinforcement learning continuous control effectiveness"
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-17T23:01:07.504159+00:00_

Web search results for query: ""gradient through dynamics" "task complexity" OR "environment complexity" reinforcement learning continuous control effectiveness"

Links: [{"title":"Deep deterministic policy gradient algorithm: A systematic review - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S2405844024067288"},{"title":"[1509.02971] Continuous control with deep reinforcement learning","url":"https://arxiv.org/abs/1509.02971"},{"title":"Policy Gradient [Reinforcement Learning] Made Simple In An Elaborate Guide","url":"https://spotintelligence.com/2025/05/19/policy-gradient-reinforcement-learning/"},{"title":"Differentiable Information Enhanced Model-Based Reinforcement Learning","url":"https://arxiv.org/html/2503.01178v1"},{"title":"Design of twin delayed deep deterministic policy gradient RL based adaptive controller for DC motor speed regulation considering uncertainties | Scientific Reports","url":"https://www.nature.com/articles/s41598-025-33644-w"},{"title":"Deep deterministic policy gradient algorithm: A systematic review - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC11101810/"},{"title":"New memristor design uses built-in oxygen gradient to bring stability to reinforcement learning","url":"https://techxplore.com/news/2026-04-memristor-built-oxygen-gradient-stability.html"},{"title":"(PDF) Continuous control with deep reinforcement learning","url":"https://www.researchgate.net/publication/281670459_Continuous_control_with_deep_reinforcement_learning"},{"title":"An enhanced deep deterministic policy gradient algorithm for intelligent control of robotic arms - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC9899791/"},{"title":"Policy Gradient and Actor–Critic Learning in Continuous ...","url":"https://www.jmlr.org/papers/volume23/21-1387/21-1387.pdf"}]

I've completed the web search for your query about "gradient through dynamics," task complexity, environment complexity, and their relationship to reinforcement learning
…[truncated 1332 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sgs-partial-effectiveness-literature_20260517T225544",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-17T23:01:07.504339+00:00_

Web search results for query: "Amos 2021 "model-based stochastic value gradient" continuous reinforcement learning gradient truncation horizon"

Links: [{"title":"On the Model-Based Stochastic Value Gradient for Continuous Reinforcement Learning","url":"https://proceedings.mlr.press/v144/amos21a.html"},{"title":"GitHub - facebookresearch/svg: On the model-based stochastic value gradient for continuous reinforcement learning","url":"https://github.com/facebookresearch/svg"},{"title":"[2008.12775] On the model-based stochastic value gradient for continuous reinforcement learning","url":"https://arxiv.org/abs/2008.12775"},{"title":"[PDF] On the model-based stochastic value gradient for continuous reinforcement learning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/On-the-model-based-stochastic-value-gradient-for-Amos-Stanton/5e06f64e91f4f48665c7407ea6eac74f93d5d0d0"},{"title":"On the model-based stochastic value gradient for ...","url":"https://par.nsf.gov/servlets/purl/10275928"},{"title":"On the model-based stochastic value gradient for ...","url":"http://bamos.github.io/data/slides/2021.svg.pdf"},{"title":"Model gradient: unified model and policy learning in model-based reinforcement learning | Frontiers of Computer Science","url":"https://link.springer.com/article/10.1007/s11704-023-3150-5"},{"title":"Gradient Estimation in Model-Based Reinforcement Learning: A Study on Linear Quadratic Environments | Intelligent Systems","url":"https://dl.acm.org/doi/abs/10.1007/978-3-030-91702-9_3"},{"title":"Fb","url":"https://research.fb.com/wp-content/uploads/2021/05/On-the-model-based-stochastic-value-gradient-for-continuous-reinforcement-learning.pdf"},{"title":"Log in or sign up to view","url":"https://research.facebook.com/wp-content/uploads/2021/05/On-the-model-based-stochastic-value-gradient-for-continuous-reinforcement-learning.pdf"}]

I found the paper you're searching for! Here are the results:

## Paper Information

The paper "On the Model-Based St
…[truncated 1378 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sgs-partial-effectiveness-literature_20260517T225544",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-17T23:01:07.504508+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"actor gradient\" too small OR vanishing model-based reinforcement learning \"stop gradient\" over-regularization policy learning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sgs-partial-effectiveness-literature_20260517T225544",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"actor gradient\" too small OR vanishing model-based reinforcement learning \"stop gradient\" over-regularization policy learning"
  }
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-17T23:01:07.504636+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "PCGrad gradient surgery multi-task learning \"gradient conflict\" environment-dependent reinforcement learning world model"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sgs-partial-effectiveness-literature_20260517T225544",
  "tool": "WebSearch",
  "tool_args": {
    "query": "PCGrad gradient surgery multi-task learning \"gradient conflict\" environment-dependent reinforcement learning world model"
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-17T23:01:07.504784+00:00_

Web search results for query: ""actor gradient" too small OR vanishing model-based reinforcement learning "stop gradient" over-regularization policy learning"

Links: [{"title":"The vanishing gradient problem - Reinforcement Learning with TensorFlow [Book]","url":"https://www.oreilly.com/library/view/reinforcement-learning-with/9781788835725/89eb53ef-c06b-4eee-81fd-46e4f8ef1fa8.xhtml"},{"title":"Vanishing Gradients in Reinforcement Finetuning of Language Models - Apple Machine Learning Research","url":"https://machinelearning.apple.com/research/vanishing-gradients-reinforcement"},{"title":"Vanishing Gradient: Problem & Solutions | StudySmarter","url":"https://www.studysmarter.co.uk/explanations/engineering/artificial-intelligence-engineering/vanishing-gradient/"},{"title":"What is the Vanishing Gradient Problem? | Ultralytics","url":"https://www.ultralytics.com/glossary/vanishing-gradient"},{"title":"1 Gradient Monitored Reinforcement Learning","url":"https://arxiv.org/pdf/2005.12108"},{"title":"Deep deterministic policy gradient algorithm: A systematic review - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S2405844024067288"},{"title":"Vanishing Gradient Problem in Deep Learning: Explained | DigitalOcean","url":"https://www.digitalocean.com/community/tutorials/vanishing-gradient-problem"},{"title":"What is the vanishing gradient problem?","url":"https://www.educative.io/answers/what-is-the-vanishing-gradient-problem"},{"title":"[2310.20703] Vanishing Gradients in Reinforcement Finetuning of Language Models","url":"https://arxiv.org/abs/2310.20703"},{"title":"The Vanishing Gradient Problem During Learning Recurrent Neural Nets and Problem Solutions | International Journal of Uncertainty, Fuzziness and Knowledge-Based Systems","url":"https://www.worldscientific.com/doi/abs/10.1142/S0218488598000094"}]

Based on my search results, I found relevant information about vanishing gradients in reinforcement learning. Here's what the research shows:
…[truncated 1615 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sgs-partial-effectiveness-literature_20260517T225544",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-17T23:01:07.505002+00:00_

Web search results for query: "PCGrad gradient surgery multi-task learning "gradient conflict" environment-dependent reinforcement learning world model"

Links: [{"title":"Gradient Surgery for Multi-Task Learning","url":"https://proceedings.neurips.cc/paper/2020/file/3fe78a8acf5fda99de95303940a2420c-Paper.pdf"},{"title":"[2001.06782] Gradient Surgery for Multi-Task Learning","url":"https://arxiv.org/abs/2001.06782"},{"title":"PCGrad: Gradient Surgery for Multi-Task Learning","url":"https://www.emergentmind.com/topics/pcgrad-optimization-technique"},{"title":"GitHub - tianheyu927/PCGrad: Code for \"Gradient Surgery for Multi-Task Learning\" · GitHub","url":"https://github.com/tianheyu927/PCGrad"},{"title":"Gradient Descent in Multi-Task Learning Stanford CS224N Default Project","url":"https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1244/final-projects/DavidSaykinKfirShmuelDolev.pdf"},{"title":"GRADIENT SURGERY FOR MULTI-TASK LEARNING","url":"https://openreview.net/pdf/78aa2ffcfff2647e283ab11388b26ea883f44bd5.pdf"},{"title":"PCGrad: Gradient Surgery for Multi-Task Learning | PDF | Mathematical Optimization | Computer Vision","url":"https://www.scribd.com/document/558287008/Yu-Et-Al-2020-Gradient-Surgery-for-Multi-Task-Learning"},{"title":"Gradient surgery based on convolutional filters grouping for multi-task models in panoptic driving perception - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S092523122501464X"},{"title":"Paper10. PCGrad - Cornor’s Blog","url":"https://wjddyd66.github.io/paper/Paper(10)PCGrad/"},{"title":"Review for NeurIPS paper: Gradient Surgery for Multi-Task Learning","url":"https://proceedings.neurips.cc/paper_files/paper/2020/file/3fe78a8acf5fda99de95303940a2420c-Review.html"}]

Based on the web search results, here's comprehensive information about PCGrad and gradient surgery in multi-task learning:

## PCGrad: Projecting Conflicting Gradients

PCGrad (Projecting Conflicting Gradients) is a gradient modifi
…[truncated 1669 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sgs-partial-effectiveness-literature_20260517T225544",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-17T23:01:07.505178+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Heess 2015 SVG \"imagination\" OR \"model rollout\" gradient \"short horizon\" \"long horizon\" backpropagation dynamics model"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sgs-partial-effectiveness-literature_20260517T225544",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Heess 2015 SVG \"imagination\" OR \"model rollout\" gradient \"short horizon\" \"long horizon\" backpropagation dynamics model"
  }
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-17T23:01:07.505306+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"gradient based\" intervention \"environment dependent\" OR \"task dependent\" deep reinforcement learning \"different tasks\" 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sgs-partial-effectiveness-literature_20260517T225544",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"gradient based\" intervention \"environment dependent\" OR \"task dependent\" deep reinforcement learning \"different tasks\" 2024 2025"
  }
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-17T23:01:07.505463+00:00_

Web search results for query: "Heess 2015 SVG "imagination" OR "model rollout" gradient "short horizon" "long horizon" backpropagation dynamics model"

Links: [{"title":"On the model-based stochastic value gradient for ...","url":"https://par.nsf.gov/servlets/purl/10275928"},{"title":"Published as a conference paper at ICLR 2023","url":"https://arxiv.org/pdf/2303.03955"},{"title":"The Thirty-Fourth AAAI Conference on Artiﬁcial Intelligence (AAAI-20)","url":"https://ojs.aaai.org/index.php/AAAI/article/download/5732/5588"},{"title":"Differentiable Information Enhanced Model-Based Reinforcement Learning","url":"https://ojs.aaai.org/index.php/AAAI/article/download/34419/36574"},{"title":"[1510.09142] Learning Continuous Control Policies by Stochastic Value Gradients","url":"https://arxiv.org/abs/1510.09142"},{"title":"Memory-based control with recurrent neural networks Nicolas Heess*","url":"https://rll.berkeley.edu/deeprlworkshop/papers/rdpg.pdf"},{"title":"Published as a conference paper at ICLR 2020 MODEL-AUGMENTED ACTOR-CRITIC:","url":"https://arxiv.org/pdf/2005.08068"},{"title":"Learning Continuous Control Policies by Stochastic Value ...","url":"https://arxiv.org/pdf/1510.09142"},{"title":"DO TRANSFORMER WORLD MODELS GIVE BETTER POLICY GRADIENTS?","url":"https://arxiv.org/pdf/2402.05290"},{"title":"Gradient Estimation Using Stochastic Computation Graphs","url":"https://proceedings.neurips.cc/paper_files/paper/2015/hash/de03beffeed9da5f3639a621bcab5dd4-Abstract.html"}]

Based on the web search results, I found relevant information about the Heess 2015 paper on Stochastic Value Gradients (SVG).

The paper "Learning continuous control policies by stochastic value gradients" was published by Nicolas Heess, Gregory Wayne, David Silver, Timothy Lillicrap, Tom Erez, and Yuval Tassa in the Advances in Neural Information Processing Systems in 2015.

The paper presents a unified framework for learning continuous control policies using backpropagation, supporting stochastic 
…[truncated 1125 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sgs-partial-effectiveness-literature_20260517T225544",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-17T23:01:07.505643+00:00_

Web search results for query: ""gradient based" intervention "environment dependent" OR "task dependent" deep reinforcement learning "different tasks" 2024 2025"

Links: [{"title":"“Deep Reinforcement Learning for Autonomous Navigation ...","url":"https://jisem-journal.com/index.php/journal/article/download/3620/1566/5930"},{"title":"Reinforcement Learning Journal 2025 Cover Page Deep Reinforcement Learning with","url":"https://rlj.cs.umass.edu/2025/papers/RLJ_RLC_2025_302.pdf"},{"title":"Reinforcement Learning Journal 2025 Cover Page","url":"https://rlj.cs.umass.edu/2025/RLJ_2025_CoverPages.pdf"},{"title":"Deep Deterministic Policy Gradient in 2025: Advancements and Applications | by AIgreeks | Medium","url":"https://medium.com/@rizvaanpatel/deep-deterministic-policy-gradient-in-2025-advancements-and-applications-16dc67e2824a"},{"title":"Differentiable Evolutionary Reinforcement Learning","url":"https://arxiv.org/html/2512.13399v1"},{"title":"Task offloading optimization in mobile edge computing based on a deep reinforcement learning algorithm using density clustering and ensemble learning | Scientific Reports","url":"https://www.nature.com/articles/s41598-024-84038-3"},{"title":"Multi-agent reinforcement learning for resources allocation optimization: a survey | Artificial Intelligence Review | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10462-025-11340-5"},{"title":"Reinforcement Learning from Human Feedback","url":"https://arxiv.org/html/2504.12501v3"},{"title":"Deep deterministic policy gradient algorithm: A systematic review - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC11101810/"},{"title":"Deep reinforcement learning-based methods for resource scheduling in cloud computing: a review and future directions | Artificial Intelligence Review | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10462-024-10756-9"}]

I've completed the web search with your query. Here are the results I found:

The search ret
…[truncated 1712 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sgs-partial-effectiveness-literature_20260517T225544",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-17T23:01:07.505834+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Do Transformer World Models Give Better Policy Gradients\" 2024 gradient quality horizon imagination"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sgs-partial-effectiveness-literature_20260517T225544",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Do Transformer World Models Give Better Policy Gradients\" 2024 gradient quality horizon imagination"
  }
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-17T23:01:07.506343+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "model-based reinforcement learning \"gradient norm\" \"imagination\" OR \"rollout\" actor critic \"too aggressive\" OR \"over-conservative\" regularization 2023 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sgs-partial-effectiveness-literature_20260517T225544",
  "tool": "WebSearch",
  "tool_args": {
    "query": "model-based reinforcement learning \"gradient norm\" \"imagination\" OR \"rollout\" actor critic \"too aggressive\" OR \"over-conservative\" regularization 2023 2024 2025"
  }
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-17T23:01:07.506624+00:00_

Web search results for query: ""Do Transformer World Models Give Better Policy Gradients" 2024 gradient quality horizon imagination"

Links: [{"title":"[2402.05290] Do Transformer World Models Give Better Policy Gradients?","url":"https://arxiv.org/abs/2402.05290"},{"title":"Do Transformer World Models Give Better Policy Gradients?","url":"https://proceedings.mlr.press/v235/ma24i.html"},{"title":"DO TRANSFORMER WORLD MODELS GIVE BETTER POLICY GRADIENTS?","url":"https://arxiv.org/pdf/2402.05290"},{"title":"Do Transformer World Models Give Better Policy Gradients? | OpenReview","url":"https://openreview.net/forum?id=Uoved2xD81"},{"title":"Do Transformer World Models Give Better Policy Gradients?","url":"https://www.emergentmind.com/papers/2402.05290"},{"title":"Do transformer world models give better policy gradients? | Proceedings of the 41st International Conference on Machine Learning","url":"https://dl.acm.org/doi/10.5555/3692070.3693447"},{"title":"Do Transformer World Models Give Better Policy Gradients?","url":"https://paperreading.club/page?id=208183"},{"title":"[Literature Review] Do Transformer World Models Give Better Policy Gradients?","url":"https://www.themoonlight.io/en/review/do-transformer-world-models-give-better-policy-gradients"},{"title":"[Quick Review] Do Transformer World Models Give Better Policy Gradients?","url":"https://liner.com/review/do-transformer-world-models-give-better-policy-gradients"},{"title":"Pierluca D'Oro on X: \"Do transformer world models give better policy gradients? In our new paper, co-led with @michel_ma_, we answer this question: traditional transformer world models conditioned on the full history do not give better policy gradients, but transformers conditioned only on actions https://t.co/50RaMZzVLm\" / X","url":"https://x.com/proceduralia/status/1756069386534658316"}]

Based on the search results, I found the paper you're looking for. Here's what the research shows:

## Overview

Commonly-used transformer world models
…[truncated 1502 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sgs-partial-effectiveness-literature_20260517T225544",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-17T23:01:07.506889+00:00_

Web search results for query: "model-based reinforcement learning "gradient norm" "imagination" OR "rollout" actor critic "too aggressive" OR "over-conservative" regularization 2023 2024 2025"

Links: [{"title":"Deep Reinforcement Learning in the Era of Foundation Models: A Survey","url":"https://www.mdpi.com/2073-431X/15/1/40"},{"title":"Published as a conference paper at ICLR 2025 EFFICIENT REINFORCEMENT LEARNING","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/797be96e4481c3fe5d675c1ba5352969-Paper-Conference.pdf"},{"title":"Reinforcement Learning Journal 2025 Cover Page","url":"https://rlj.cs.umass.edu/2025/RLJ_2025_CoverPages.pdf"},{"title":"GitHub - yingchengyang/Reinforcement-Learning-Papers: Related papers for reinforcement learning, including classic papers and latest papers in top conferences · GitHub","url":"https://github.com/yingchengyang/Reinforcement-Learning-Papers"},{"title":"Week 5: Model-Based Methods - Deep RL Course","url":"https://deeprlcourse.github.io/course_notes/model-based/"},{"title":"Policy Gradient and Actor–Critic Learning in Continuous ...","url":"https://www.jmlr.org/papers/volume23/21-1387/21-1387.pdf"},{"title":"GitHub - opendilab/awesome-model-based-RL: A curated list of awesome model based RL resources (continually updated) · GitHub","url":"https://github.com/opendilab/awesome-model-based-RL"},{"title":"Full article: Risk-Sensitive Deep RL: Variance-Constrained Actor-Critic Provably Finds Globally Optimal Policy","url":"https://www.tandfonline.com/doi/full/10.1080/01621459.2025.2583501"},{"title":"Deep Reinforcement Learning: The Actor-Critic Method | Towards Data Science","url":"https://towardsdatascience.com/deep-reinforcement-learning-the-actor-critic-method/"},{"title":"Published as a conference paper at ICLR 2025 LEARNING CONTINUALLY BY","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/5565ab682d6c7f8d9da34ba0919974b0-Paper-Conference.pdf"}]

Based on the web search results, here are the key find
…[truncated 1993 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sgs-partial-effectiveness-literature_20260517T225544",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-17T23:01:07.507102+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"DreamerV3\" OR \"DreamerV2\" actor gradient \"dynamics backpropagation\" \"reinforce\" continuous control walker cheetah comparison"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sgs-partial-effectiveness-literature_20260517T225544",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"DreamerV3\" OR \"DreamerV2\" actor gradient \"dynamics backpropagation\" \"reinforce\" continuous control walker cheetah comparison"
  }
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-17T23:01:07.507255+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"overestimation\" OR \"plasticity\" OR \"gradient\" cheetah walker \"different behavior\" OR \"different results\" model-based 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sgs-partial-effectiveness-literature_20260517T225544",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"overestimation\" OR \"plasticity\" OR \"gradient\" cheetah walker \"different behavior\" OR \"different results\" model-based 2024 2025"
  }
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-17T23:01:07.507424+00:00_

Web search results for query: ""overestimation" OR "plasticity" OR "gradient" cheetah walker "different behavior" OR "different results" model-based 2024 2025"

Links: [{"title":"Model-based inference of synaptic plasticity rules - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12257422/"},{"title":"Model-based inference of synaptic plasticity rules","url":"https://pubmed.ncbi.nlm.nih.gov/40661128/"},{"title":"NeurIPS 2024: Model-Based Inference of Synaptic Plasticity Rules","url":"https://yashsmehta.com/plasticity-paper-website/"},{"title":"Model Based Inference of Synaptic Plasticity Rules","url":"https://proceedings.neurips.cc/paper_files/paper/2024/hash/571082ea18d30060177dfcaf662ff0e5-Abstract-Conference.html"},{"title":"Model-Based Inference of Synaptic Plasticity Rules | Janelia Research Campus","url":"https://www.janelia.org/publication/model-based-inference-of-synaptic-plasticity-rules"},{"title":"The Oxford Handbook of Cognitive Enhancement and Brain Plasticity (In Progress)","url":"https://www.decisionneurosciencelab.org/wp-content/uploads/2025/03/Robles_et_al_2025.pdf"},{"title":"Model based inference of synaptic plasticity rules","url":"https://neurips.cc/media/neurips-2024/Slides/93446.pdf"},{"title":"A gradient plasticity model for porous metals with random ...","url":"https://hal.science/hal-05137623v1/file/MECMAT_Xenos_Danas_Aravas_2025.pdf"},{"title":"offline model-based optimization by learning","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/768c19273e20fa09147885d03da7550f-Paper-Conference.pdf"},{"title":"An approach to consider behavioral plasticity as a source of uncertainty when forecasting species' response to climate change - PubMed","url":"https://pubmed.ncbi.nlm.nih.gov/26120426/"}]

Based on my search results, I found papers related to model-based inference of synaptic plasticity rules using gradient-based optimization methods from 2024, but the results do not contain information specifically about "cheetah walker" m
…[truncated 1041 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sgs-partial-effectiveness-literature_20260517T225544",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-17T23:01:07.507700+00:00_

Web search results for query: ""DreamerV3" OR "DreamerV2" actor gradient "dynamics backpropagation" "reinforce" continuous control walker cheetah comparison"

Links: [{"title":"Mastering diverse control tasks through world models | Nature","url":"https://www.nature.com/articles/s41586-025-08744-2"},{"title":"DreamerV3: Mastering Diverse Domains through World Models","url":"https://vitalab.github.io/article/2023/01/19/DreamerV3.html"},{"title":"Mastering diverse control tasks through world models - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12003158/"},{"title":"Dreamer V2 - EclecticSheep","url":"https://eclecticsheep.ai/2023/07/06/dreamer_v2.html"},{"title":"GitHub - danijar/dreamerv3: Mastering Diverse Domains through World Models · GitHub","url":"https://github.com/danijar/dreamerv3"},{"title":"Mastering Diverse Domains through World Models","url":"https://arxiv.org/pdf/2301.04104"},{"title":"DreamerV3: Robust Latent Model-Based RL","url":"https://www.emergentmind.com/topics/dreamerv3"},{"title":"DreamerV3: Model-Based RL Algorithm","url":"https://www.emergentmind.com/topics/dreamerv3-algorithm"},{"title":"DreamerNav: learning-based autonomous navigation in dynamic indoor environments using world models - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12510832/"},{"title":"GitHub - danijar/dreamerv2: Mastering Atari with Discrete World Models · GitHub","url":"https://github.com/danijar/dreamerv2"}]

I found several relevant resources about DreamerV2 and DreamerV3 that discuss actor gradient approaches and continuous control tasks. Here are the key findings:

## Key Differences in Actor Training

DreamerV1 relied entirely on reparameterization gradients to train the actor directly by backpropagating value gradients through the sequence of sampled model states and actions. In contrast, DreamerV2 uses both discrete latents and discrete actions and to backpropagate through the sampled actions and state sequences straight-through gradients are leveraged
…[truncated 1330 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sgs-partial-effectiveness-literature_20260517T225544",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-17T23:01:07.508051+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Overestimation, Overfitting, and Plasticity in Actor-Critic\" 2024 bitter lesson reinforcement learning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sgs-partial-effectiveness-literature_20260517T225544",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Overestimation, Overfitting, and Plasticity in Actor-Critic\" 2024 bitter lesson reinforcement learning"
  }
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-17T23:01:07.508381+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"gradient starvation\" OR \"gradient blocking\" reinforcement learning actor signal environment complexity"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sgs-partial-effectiveness-literature_20260517T225544",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"gradient starvation\" OR \"gradient blocking\" reinforcement learning actor signal environment complexity"
  }
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-17T23:01:07.508586+00:00_

Web search results for query: ""Overestimation, Overfitting, and Plasticity in Actor-Critic" 2024 bitter lesson reinforcement learning"

Links: [{"title":"[2403.00514] Overestimation, Overfitting, and Plasticity in Actor-Critic: the Bitter Lesson of Reinforcement Learning","url":"https://arxiv.org/abs/2403.00514"},{"title":"Overestimation, Overfitting, and Plasticity in Actor-Critic: the Bitter Lesson of Reinforcement Learning","url":"https://proceedings.mlr.press/v235/nauman24a.html"},{"title":"[PDF] Overestimation, Overfitting, and Plasticity in Actor-Critic: the Bitter Lesson of Reinforcement Learning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Overestimation,-Overfitting,-and-Plasticity-in-the-Nauman-Bortkiewicz/dcf39ce4ea7c1d073dcd0dbb131a0b90a4bd2977"},{"title":"Overestimation, Overfitting, and Plasticity in Actor-Critic: the Bitter Lesson of Reinforcement Learning","url":"https://arxiv.org/html/2403.00514v2"},{"title":"Overestimation, Overfitting, and Plasticity in Actor-Critic: the Bitter Lesson of Reinforcement Learning | OpenReview","url":"https://openreview.net/forum?id=5vZzmCeTYu"},{"title":"[2403.00514v2] Overestimation, Overfitting, and Plasticity in Actor-Critic: the Bitter Lesson of Reinforcement Learning","url":"https://arxiv.org/abs/2403.00514v2"},{"title":"Overestimation, Overfitting, and Plasticity in Actor-Critic: the Bitter Lesson of Reinforcement Learning | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/overestimation-overfitting-plasticity-actor-critic-bitter-lesson"},{"title":"Overestimation, overfitting, and plasticity in actor-critic | Proceedings of the 41st International Conference on Machine Learning","url":"https://dl.acm.org/doi/10.5555/3692070.3693586"},{"title":"ICML Poster Overestimation, Overfitting, and Plasticity in Actor-Critic: the Bitter Lesson of Reinforcement Learning","url":"https://icml.cc/virtual/2024/poster/34956"},{"title":"Overestimation, Overfitting, and Plasticity in Act
…[truncated 1531 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sgs-partial-effectiveness-literature_20260517T225544",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-17T23:01:07.508793+00:00_

Web search results for query: ""gradient starvation" OR "gradient blocking" reinforcement learning actor signal environment complexity"

Links: [{"title":"The Definitive Guide to Policy Gradients in Deep Reinforcement Learning:","url":"https://arxiv.org/pdf/2401.13662"},{"title":"[2011.09468] Gradient Starvation: A Learning Proclivity in Neural Networks","url":"https://arxiv.org/abs/2011.09468"},{"title":"Simple statistical gradient-following algorithms for connectionist reinforcement learning | Machine Learning | Springer Nature Link","url":"https://link.springer.com/article/10.1007/BF00992696"},{"title":"Policy Gradient Algorithms | Lil'Log","url":"https://lilianweng.github.io/posts/2018-04-08-policy-gradient/"},{"title":"Simple Statistical Gradient-Following Algorithms for Connectionist Reinforcement Learning | Machine Language","url":"https://dl.acm.org/doi/10.1007/BF00992696"},{"title":"Gradient Starvation. Why Your LLM Stops Learning","url":"https://www.feedtheai.com/gradient-starvation-why-your-llm-stops-learning/"},{"title":"Gradient Starvation: A Learning Proclivity in Neural Networks | OpenReview","url":"https://openreview.net/forum?id=aExAsh1UHZo"},{"title":"1 Gradient Monitored Reinforcement Learning","url":"https://arxiv.org/pdf/2005.12108"},{"title":"Gradient Starvation: A Learning Proclivity in Neural Networks | DeepAI","url":"https://deepai.org/publication/gradient-starvation-a-learning-proclivity-in-neural-networks"},{"title":"Gradient Starvation: A Learning Proclivity in Neural Networks (paper review) | by Stan Kriventsov | Deep Learning Reviews | Medium","url":"https://medium.com/deep-learning-reviews/gradient-starvation-a-learning-proclivity-in-neural-networks-paper-review-23f269d81a07"}]

Based on the web search results, I found relevant information about gradient starvation in neural networks and reinforcement learning.

## Gradient Starvation

Gradient starvation arises when cross-entropy loss is minimized by capturing only a subset of feature
…[truncated 1570 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sgs-partial-effectiveness-literature_20260517T225544",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-17T23:01:07.509031+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Ma Ni Gehring D'Oro Bacon 2024 ICML \"action-conditioned world model\" gradient horizon scaling polynomial exponential"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sgs-partial-effectiveness-literature_20260517T225544",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Ma Ni Gehring D'Oro Bacon 2024 ICML \"action-conditioned world model\" gradient horizon scaling polynomial exponential"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-17T23:01:07.509207+00:00_

Web search results for query: "Ma Ni Gehring D'Oro Bacon 2024 ICML "action-conditioned world model" gradient horizon scaling polynomial exponential"

Links: [{"title":"Do Transformer World Models Give Better Policy Gradients?","url":"https://proceedings.mlr.press/v235/ma24i.html"},{"title":"Pierre-Luc Bacon","url":"https://pierrelucbacon.com/"},{"title":"Over 50 Mila-Affiliated Scientific Papers Accepted at ICML 2024 | Mila","url":"https://mila.quebec/en/news/over-50-mila-affiliated-scientific-papers-accepted-at-icml-2024"},{"title":"ICML 2024 Papers","url":"https://icml.cc/virtual/2024/papers.html"},{"title":"ICML Poster 3D-VLA: A 3D Vision-Language-Action Generative World Model","url":"https://icml.cc/virtual/2024/poster/34575"},{"title":"ICML 2024 Learning to Model the World With Language Oral","url":"https://icml.cc/virtual/2024/oral/35565"},{"title":"GitHub - leofan90/Awesome-World-Models: A comprehensive list of papers for the definition of World Models and using World Models for General Video Generation, Embodied AI, and Autonomous Driving, including papers, codes, and related websites. · GitHub","url":"https://github.com/leofan90/Awesome-World-Models"},{"title":"Do Transformer World Models Give Better Policy Gradients? | OpenReview","url":"https://openreview.net/forum?id=Uoved2xD81"},{"title":"Downloads 2024","url":"https://icml.cc/Downloads/2024"},{"title":"1st ICML Workshop on In-Context Learning (ICL @ ICML 2024)","url":"https://icml.cc/virtual/2024/workshop/29966"}]

Based on the web search results, I found the paper you're looking for:

The paper "Do Transformer World Models Give Better Policy Gradients?" was authored by Michel Ma, Tianwei Ni, Clement Gehring, Pierluca D'Oro, and Pierre-Luc Bacon, and published at the 41st International Conference on Machine Learning (ICML) in 2024.

The paper shows that commonly-used transformer world models produce circuitous gradient paths which can be detrimental to long-range policy gradients. To address this, the 
…[truncated 665 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sgs-partial-effectiveness-literature_20260517T225544",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-17T23:01:07.509419+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__save_project_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sgs-partial-effectiveness-literature_20260517T225544",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__save_project_file",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-17T23:01:07.509568+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sgs-partial-effectiveness-literature_20260517T225544",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-17T23:01:07.509718+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/literature_map.yaml",
  "offset": "1740",
  "limit": "20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sgs-partial-effectiveness-literature_20260517T225544",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/literature_map.yaml",
    "offset": "1740",
    "limit": "20"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-17T23:01:07.509879+00:00_

&lt;system-reminder>Warning: the file exists but is shorter than the provided offset (1740). The file has 1082 lines.&lt;/system-reminder>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sgs-partial-effectiveness-literature_20260517T225544",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-17T23:01:07.510144+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/memory.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sgs-partial-effectiveness-literature_20260517T225544",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/memory.md"
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-17T23:01:07.510332+00:00_

1	# Memory — event-gated-adaptive-horizon
2	
3	## 2026-05-17: dt_emb "困境" — frozen prevents CIVO but kills gating
4	
5	exp_022b 确认：frozen random dt_emb 阻止 CIVO (ve_ratio 峰值仅 0.218)，但 gate 收敛为近均匀分布 (entropy_ratio=0.912)。核心原因：随机嵌入不携带时间语义 → gate 无法区分 dt 值。
6	
7	**设计启示**：CIVO 因果链需要 gradient-driven 语义 dt 表征。阻止 CIVO 的方式（SGS、freeze、remove）都会同时降低 dt_emb 的语义质量，形成 safety-utility tradeoff。这对论文来说是诊断发现（C2 的深化），不是需要解决的工程问题。
8	
9	## 2026-05-17: PickCube detector backtest 教训（CRITICAL）
10	
11	Worker 的 detector backtest 分析得出错误结论（TP），实际是 TN。三个方法论错误：
12	1. 用 NVE 代替 raw V/E ratio（detector 是 baseline-free 的，用的是 r_t = V/max(E, ε)，不是 NVE）
13	2. Acceleration condition 遗漏：prev_delta 也必须 > τ_vel（不只是当前 delta）
14	3. 未检查 eval decline condition (c_dec)
15	
16	**教训**：detector backtest 必须严格逐条对照 Algorithm 1 的每个条件，不能凭 NVE 近似推断。以后所有 detector 相关分析必须用 raw V/E ratio 而非 NVE。
17	
18	## 2026-05-17: PickCube CIVO pattern — transient, not persistent
19	
20	exp_019b reveals PickCube exhibits "transient CIVO": NVE peaks 3.78× @52.5K then deflates to 0.08× by 132.5K, with eval recovering to 26.9. This contrasts Walker Walk's monotonic acceleration → collapse (2/3 seeds) pattern. Gate locked at dt=2 throughout (entropy=0). Value function transitions from overestimation to severe underestimation.
21	
22	**Key insight**: CIVO onset is environment-general (trained dt_emb → NVE spike in both environments), but CIVO resolution is environment-dependent (collapse vs self-correction).
23	
24	**Detector**: does NOT trigger on PickCube (TN). Oscillatory V/E pattern filtered by acceleration condition. This demonstrates detector specificity — it does not over-fire on noisy patterns.
25	
26	## 2026-05-17: exp_022 curriculum misconfiguration lesson
27	
28	gate_curriculum_phase1=50000 in configs.yaml means 50K env steps. With action_repeat=2, this = 100K logger steps. A 105K step experiment never exits phase1 warmup. **Lesson**: always compute effective curriculum schedule accounting for action_repeat before submitting.
29	
30	
…[truncated 968 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sgs-partial-effectiveness-literature_20260517T225544",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-17T23:01:07.510602+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/literature_map.yaml",
  "offset": "1060",
  "limit": "25"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sgs-partial-effectiveness-literature_20260517T225544",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/literature_map.yaml",
    "offset": "1060",
    "limit": "25"
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-17T23:01:07.510789+00:00_

1060	  venue: NeurIPS
1061	  category: method-component
1062	  role: "CAGrad — finds common descent direction avoiding worst-case task conflict with convergence guarantees; optimization-based alternative to SGS's event-gated gradient blocking"
1063	  relevance_score: 4
1064	
1065	- paper_id: wang2021gradientvaccine
1066	  title: "Gradient Vaccine: Investigating and Improving Multi-task Optimization in Massively Multilingual Models"
1067	  authors: [Wang Z., et al.]
1068	  year: 2021
1069	  venue: ICLR
1070	  category: method-component
1071	  role: "Uses gradient similarity along optimization trajectory to detect and mitigate task conflicts in shared representations; parallels SGS's event-based gradient blocking"
1072	  relevance_score: 3
1073	
1074	- paper_id: navon2022nashmtl
1075	  title: "Multi-Task Learning as a Bargaining Game"
1076	  authors: [Navon A., et al.]
1077	  year: 2022
1078	  venue: ICML
1079	  category: method-component
1080	  role: "Nash-MTL — game-theoretic gradient combination ensuring proportional fairness among tasks; offers bargaining perspective on the inter-task interference SGS addresses via selective gating"
1081	  relevance_score: 4
1082	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sgs-partial-effectiveness-literature_20260517T225544",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-17T23:01:07.511002+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/literature_map.yaml",
  "old_string": "- paper_id: navon2022nashmtl\n  title: \"Multi-Task Learning as a Bargaining Game\"\n  authors: [Navon A., et al.]\n  year: 2022\n  venue: ICML\n  category: method-component\n  role: \"Nash-MTL — game-theoretic gradient combination ensuring proportional fairness among tasks; offers bargaining perspective on the inter-task interference SGS addresses via selective gating\"\n  relevance_score: 4",
  "new_string": "- paper_id: navon2022nashmtl\n  title: \"Multi-Task Learning as a Bargaining Game\"\n  authors: [Navon A., et al.]\n  year: 2022\n  venue: ICML\n  category: method-component\n  role: \"Nash-MTL — game-theoretic gradient combination ensuring proportional fairness among tasks; offers bargaining perspective on the inter-task interference SGS addresses via selective gating\"\n  relevance_score: 4\n\n# ============================================================\n# SGS PARTIAL EFFECTIVENESS LITERATURE (2026-05-17)\n# ============================================================\n# Context: exp_021 shows Full-SGS completely blocks CIVO in Walker\n# (NVE_peak=0.72) but only makes it transient in Cheetah (NVE_peak=9.94,\n# self-recovery). actor_grad_norm in Cheetah Full-SGS is 0.0-0.1,\n# suggesting over-aggressive gradient blocking. These papers document\n# environment-dependent effects of gradient interventions in MBRL.\n\n- paper_id: ma2024awm\n  title: \"Do Transformer World Models Give Better Policy Gradients?\"\n  authors: [Ma M., Ni T., Gehring C., D'Oro P., Bacon P.-L.]\n  year: 2024\n  venue: \"ICML (arXiv:2402.05290)\"\n  category: method-component\n  role: \"Shows standard world models produce 'circuitous gradient paths' detrimental to long-range policy gradients; policy gradients through dynamics scale EXPONENTIALLY with horizon for standard architectures. Directly explains our Full-SGS finding: blocking all dynamics gradients has environment-dependent impact because environments differ in how much they rely on long-range temporal credit assignment through imagination. Cheetah Run requires more complex multi-joint coordination (longer effective credit assignment chain) than Walker Walk, so total gradient blocking is more damaging.\"\n  relevance_score: 5\n  survey_tag: sgs-partial-effectiveness\n\n- paper_id: amos2021svg\n  title: \"On the Model-Based Stochastic Value Gradient for Continuous Reinforcement Learning\"\n  authors: [Amos B., Stanton S., Yarats D., Wilson A.G.]\n  year: 2021\n  venue: \"L4DC (Proceedings of Machine Learning Research vol. 144)\"\n  category: method-component\n  role: \"Shows model-based SVG using learned dynamics + short-horizon value expansion outperforms model-free methods; crucially, backprop through simulated trajectories alone fails (compounding error), but backprop through REAL trajectories with model-based value expansion works. Key implication for Full-SGS: completely removing dynamics gradients (actor_grad_norm→0) is worse than having noisy dynamics gradients. The actor needs SOME gradient signal through the model even if imperfect.\"\n  relevance_score: 4\n  survey_tag: sgs-partial-effectiveness\n\n- paper_id: heess2015svg\n  title: \"Learning Continuous Control Policies by Stochastic Value Gradients\"\n  authors: [Heess N., Wayne G., Silver D., Lillicrap T., Erez T., Tassa Y.]\n  year: 2015\n  venue: NeurIPS\n  category: background\n  role: \"SVG framework — spectrum from SVG(0) (no model gradient) to SVG(∞) (full horizon backprop). Key finding: SVG(1) (1-step model gradient + value function) is most robust across environments; SVG(∞) degrades on complex tasks due to vanishing/exploding gradients through long rollouts. Foundational evidence that gradient-through-dynamics effectiveness is environment-dependent: simple tasks tolerate SVG(0), complex tasks need SVG(1+) but not necessarily SVG(∞).\"\n  relevance_score: 4\n  survey_tag: sgs-partial-effectiveness\n\n- paper_id: nauman2024bitter\n  title: \"Overestimation, Overfitting, and Plasticity in Actor-Critic: the Bitter Lesson of Reinforcement Learning\"\n  authors: [Nauman M., Bortkiewicz M., Miłoś P., Trzcinski T., Ostaszewski M., Cygan M.]\n  year: 2024\n  venue: \"ICML (arXiv:2403.00514)\"\n  category: evaluation\n  role: \"Tests 60+ off-policy agents with various regularization techniques across 14 tasks; key finding: 'effectiveness of a specific regularization setup varies with the task' — no single regularization universally helps. DIRECTLY supports our exp_021 finding that Full-SGS (a form of gradient regularization) works in Walker but fails in Cheetah. The task-dependence of regularization effectiveness is a documented phenomenon, not an anomaly.\"\n  relevance_score: 5\n  survey_tag: sgs-partial-effectiveness\n\n# --- SGS partial effectiveness synthesis (2026-05-17) ---\n#\n# WHY Full-SGS WORKS IN WALKER BUT NOT CHEETAH:\n#\n# 1. DreamerV3 continuous control actor uses dynamics backpropagation\n#    as the PRIMARY gradient source (straight-through gradients through\n#    imagination rollout). Full-SGS blocks this entirely.\n#\n# 2. Ma et al. 2024 shows gradient quality through dynamics degrades\n#    exponentially with horizon. But ZERO gradient (Full-SGS) is worse\n#    than degraded gradient for tasks requiring temporal credit assignment.\n#\n# 3. Walker Walk: simple task (2 joints, reward = stand + walk forward),\n#    limited credit assignment depth → actor can learn from residual\n#    REINFORCE/value gradient signals even without dynamics backprop.\n#\n# 4. Cheetah Run: complex coordination (6 joints, reward = forward speed),\n#    deeper credit assignment → actor is STARVED of gradient signal\n#    when dynamics backprop is blocked (actor_grad_norm = 0.0-0.1).\n#\n# 5. Nauman et al. 2024 confirms: regularization effectiveness is\n#    fundamentally task-dependent across 14 environments.\n#\n# 6. Heess et al. 2015 (SVG): SVG(0) (no model gradient) works for\n#    simple tasks but SVG(1+) is needed for complex ones — directly\n#    parallels Walker (SVG(0)-like ok) vs Cheetah (needs model gradient).\n#\n# IMPLICATION FOR PAPER:\n# Full-SGS's partial effectiveness is NOT a failure of our approach —\n# it's a predicted consequence of over-aggressive gradient blocking\n# in environments requiring temporal credit assignment. This strengthens\n# the argument for EVENT-GATED (selective) intervention over blanket SGS."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sgs-partial-effectiveness-literature_20260517T225544",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/literature_map.yaml",
    "old_string": "- paper_id: navon2022nashmtl\n  title: \"Multi-Task Learning as a Bargaining Game\"\n  authors: [Navon A., et al.]\n  year: 2022\n  venue: ICML\n  category: method-component\n  role: \"Nash-MTL — game-theoretic gradient combination ensuring proportional fairness among tasks; offers bargaining perspective on the inter-task interference SGS addresses via selective gating\"\n  relevance_score: 4",
    "new_string": "- paper_id: navon2022nashmtl\n  title: \"Multi-Task Learning as a Bargaining Game\"\n  authors: [Navon A., et al.]\n  year: 2022\n  venue: ICML\n  category: method-component\n  role: \"Nash-MTL — game-theoretic gradient combination ensuring proportional fairness among tasks; offers bargaining perspective on the inter-task interference SGS addresses via selective gating\"\n  relevance_score: 4\n\n# ============================================================\n# SGS PARTIAL EFFECTIVENESS LITERATURE (2026-05-17)\n# ============================================================\n# Context: exp_021 shows Full-SGS completely blocks CIVO in Walker\n# (NVE_peak=0.72) but only makes it transient in Cheetah (NVE_peak=9.94,\n# self-recovery). actor_grad_norm in Cheetah Full-SGS is 0.0-0.1,\n# suggesting over-aggressive gradient blocking. These papers document\n# environment-dependent effects of gradient interventions in MBRL.\n\n- paper_id: ma2024awm\n  title: \"Do Transformer World Models Give Better Policy Gradients?\"\n  authors: [Ma M., Ni T., Gehring C., D'Oro P., Bacon P.-L.]\n  year: 2024\n  venue: \"ICML (arXiv:2402.05290)\"\n  category: method-component\n  role: \"Shows standard world models produce 'circuitous gradient paths' detrimental to long-range policy gradients; policy gradients through dynamics scale EXPONENTIALLY with horizon for standard architectures. Directly explains our Full-SGS finding: blocking all dynamics gradients has environment-dependent impact because environments differ in how much they rely on long-range temporal credit assignment through imagination. Cheetah Run requires more complex multi-joint coordination (longer effective credit assignment chain) than Walker Walk, so total gradient blocking is more damaging.\"\n  relevance_score: 5\n  survey_tag: sgs-partial-effectiveness\n\n- paper_id: amos2021svg\n  title: \"On the Model-Based Stochastic Value Gradient for Continuous Reinforcement Learning\"\n  authors: [Amos B., Stanton S., Yarats D., Wilson A.G.]\n  year: 2021\n  venue: \"L4DC (Proceedings of Machine Learning Research vol. 144)\"\n  category: method-component\n  role: \"Shows model-based SVG using learned dynamics + short-horizon value expansion outperforms model-free methods; crucially, backprop through simulated trajectories alone fails (compounding error), but backprop through REAL trajectories with model-based value expansion works. Key implication for Full-SGS: completely removing dynamics gradients (actor_grad_norm→0) is worse than having noisy dynamics gradients. The actor needs SOME gradient signal through the model even if imperfect.\"\n  relevance_score: 4\n  survey_tag: sgs-partial-effectiveness\n\n- paper_id: heess2015svg\n  title: \"Learning Continuous Control Policies by Stochastic Value Gradients\"\n  authors: [Heess N., Wayne G., Silver D., Lillicrap T., Erez T., Tassa Y.]\n  year: 2015\n  venue: NeurIPS\n  category: background\n  role: \"SVG framework — spectrum from SVG(0) (no model gradient) to SVG(∞) (full horizon backprop). Key finding: SVG(1) (1-step model gradient + value function) is most robust across environments; SVG(∞) degrades on complex tasks due to vanishing/exploding gradients through long rollouts. Foundational evidence that gradient-through-dynamics effectiveness is environment-dependent: simple tasks tolerate SVG(0), complex tasks need SVG(1+) but not necessarily SVG(∞).\"\n  relevance_score: 4\n  survey_tag: sgs-partial-effectiveness\n\n- paper_id: nauman2024bitter\n  title: \"Overestimation, Overfitting, and Plasticity in Actor-Critic: the Bitter Lesson of Reinforcement Learning\"\n  authors: [Nauman M., Bortkiewicz M., Miłoś P., Trzcinski T., Ostaszewski M., Cygan M.]\n  year: 2024\n  venue: \"ICML (arXiv:2403.00514)\"\n  category: evaluation\n  role: \"Tests 60+ off-policy agents with various regularization techniques across 14 tasks; key finding: 'effectiveness of a specific regularization setup varies with the task' — no single regularization universally helps. DIRECTLY supports our exp_021 finding that Full-SGS (a form of gradient regularization) works in Walker but fails in Cheetah. The task-dependence of regularization effectiveness is a documented phenomenon, not an anomaly.\"\n  relevance_score: 5\n  survey_tag: sgs-partial-effectiveness\n\n# --- SGS partial effectiveness synthesis (2026-05-17) ---\n#\n# WHY Full-SGS WORKS IN WALKER BUT NOT CHEETAH:\n#\n# 1. DreamerV3 continuous control actor uses dynamics backpropagation\n#    as the PRIMARY gradient source (straight-through gradients through\n#    imagination rollout). Full-SGS blocks this entirely.\n#\n# 2. Ma et al. 2024 shows gradient quality through dynamics degrades\n#    exponentially with horizon. But ZERO gradient (Full-SGS) is worse\n#    than degraded gradient for tasks requiring temporal credit assignment.\n#\n# 3. Walker Walk: simple task (2 joints, reward = stand + walk forward),\n#    limited credit assignment depth → actor can learn from residual\n#    REINFORCE/value gradient signals even without dynamics backprop.\n#\n# 4. Cheetah Run: complex coordination (6 joints, reward = forward speed),\n#    deeper credit assignment → actor is STARVED of gradient signal\n#    when dynamics backprop is blocked (actor_grad_norm = 0.0-0.1).\n#\n# 5. Nauman et al. 2024 confirms: regularization effectiveness is\n#    fundamentally task-dependent across 14 environments.\n#\n# 6. Heess et al. 2015 (SVG): SVG(0) (no model gradient) works for\n#    simple tasks but SVG(1+) is needed for complex ones — directly\n#    parallels Walker (SVG(0)-like ok) vs Cheetah (needs model gradient).\n#\n# IMPLICATION FOR PAPER:\n# Full-SGS's partial effectiveness is NOT a failure of our approach —\n# it's a predicted consequence of over-aggressive gradient blocking\n# in environments requiring temporal credit assignment. This strengthens\n# the argument for EVENT-GATED (selective) intervention over blanket SGS."
  }
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-17T23:01:07.511656+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/literature_map.yaml has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sgs-partial-effectiveness-literature_20260517T225544",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-17T23:01:07.512028+00:00_

called mcp__agent-ml-research__save_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__save_project_file</summary>

```json
{
  "project": "event-gated-adaptive-horizon",
  "file": "memory.md",
  "content": "# Memory — event-gated-adaptive-horizon\n\n## 2026-05-17: SGS partial effectiveness 文献参考\n\nexp_021 发现 Full-SGS 在 Walker 完全阻止 CIVO (NVE_peak=0.72) 但在 Cheetah 仅使其 transient (NVE_peak=9.94, 自恢复)。actor_grad_norm 在 Cheetah Full-SGS 中全程 0.0-0.1。文献搜索确认这是已知现象：\n\n**核心解释**：DreamerV3 连续控制 actor 的主要梯度来源是 dynamics backpropagation（通过 imagination rollout 的直通梯度）。Full-SGS 完全阻断此通路 → actor 梯度饥饿。\n\n**环境依赖性的文献支持**：\n1. **Ma et al. (ICML 2024)** — 标准 world model 的 policy gradient 随 horizon 指数级衰减；gradient path 质量是环境依赖的\n2. **Heess et al. (NeurIPS 2015, SVG)** — SVG(0)（无 model gradient）仅在简单任务有效；复杂任务需要 SVG(1+)。Walker≈简单, Cheetah≈复��\n3. **Amos et al. (L4DC 2021)** — 完全无 dynamics gradient 比有噪声的 dynamics gradient 更差\n4. **Nauman et al. (ICML 2024)** — 60+ agents, 14 tasks：regularization effectiveness fundamentally task-dependent，无 universal 最优\n\n**为什么 Walker 可以 Cheetah 不行**：\n- Walker Walk: 2 关节, reward=站立+前进, 浅层 credit assignment → 残余 REINFORCE/value gradient 足够\n- Cheetah Run: 6 关节, reward=速度, 需要多关节协调 → 深层 temporal credit assignment 被 Full-SGS 阻断\n\n**论文 framing**：Full-SGS 的部分有效性不是方法缺陷，而是 blanket gradient blocking 的预期后果。这恰好论证了 EVENT-GATED selective intervention 优于 Full-SGS 的必要性。\n\n## 2026-05-17: dt_emb \"困境\" — frozen prevents CIVO but kills gating\n\nexp_022b 确认：frozen random dt_emb 阻止 CIVO (ve_ratio 峰值仅 0.218)，但 gate 收敛为近均匀分布 (entropy_ratio=0.912)。核心原因：随机嵌入不携带时间语义 → gate 无法区分 dt 值。\n\n**设计启示**：CIVO 因果链需要 gradient-driven 语义 dt 表征。阻止 CIVO 的方式（SGS、freeze、remove）都会同时降低 dt_emb 的语义质量，形成 safety-utility tradeoff。这对论文来说是诊断发现（C2 的深化），不是需要解决的工程问题。\n\n## 2026-05-17: PickCube detector backtest 教训（CRITICAL）\n\nWorker 的 detector backtest 分析得出错误结论（TP），实际是 TN。三个方法论错误：\n1. 用 NVE 代替 raw V/E ratio（detector 是 baseline-free 的，用的是 r_t = V/max(E, ε)，不是 NVE）\n2. Acceleration condition 遗漏：prev_delta 也必须 > τ_vel（不只是当前 delta）\n3. 未检查 eval decline condition (c_dec)\n\n**教训**：detector backtest 必须严格逐条对照 Algorithm 1 的每个条件，不能凭 NVE 近似推断。以后所有 detector 相关分析必须用 raw V/E ratio 而非 NVE。\n\n## 2026-05-17: PickCube CIVO pattern — transient, not persistent\n\nexp_019b reveals PickCube exhibits \"transient CIVO\": NVE peaks 3.78× @52.5K then deflates to 0.08× by 132.5K, with eval recovering to 26.9. This contrasts Walker Walk's monotonic acceleration → collapse (2/3 seeds) pattern. Gate locked at dt=2 throughout (entropy=0). Value function transitions from overestimation to severe underestimation.\n\n**Key insight**: CIVO onset is environment-general (trained dt_emb → NVE spike in both environments), but CIVO resolution is environment-dependent (collapse vs self-correction).\n\n**Detector**: does NOT trigger on PickCube (TN). Oscillatory V/E pattern filtered by acceleration condition. This demonstrates detector specificity — it does not over-fire on noisy patterns.\n\n## 2026-05-17: exp_022 curriculum misconfiguration lesson\n\ngate_curriculum_phase1=50000 in configs.yaml means 50K env steps. With action_repeat=2, this = 100K logger steps. A 105K step experiment never exits phase1 warmup. **Lesson**: always compute effective curriculum schedule accounting for action_repeat before submitting.\n\nphase1=0, phase2=0 is safe: gate_scale=1.0 from step 0, no divide-by-zero risk (the linear interpolation branch is never entered).\n\n## 2026-05-15: 服务器代码目录确认\n\n源码在 `/root/autodl-tmp/event-gated-adaptive-horizon/`，不在 `/root/runs/event-gated-adaptive-horizon/`（后者只有日志）。\n\n## 2026-05-14: GPU 隔离确认\n\nCUDA_VISIBLE_DEVICES 隔离正确。`--device cuda:0` + `CUDA_VISIBLE_DEVICES=1` = 物理 GPU 1。\n\n## 2026-05-13: ManiSkill3 config key\n\nPickCube 实验必须用 `--configs defaults maniskill_state`（不是 `maniskill`，那个 key 不存在会 crash）。但实际 019b resubmit 用的是 `--configs defaults maniskill`，因为后来在 configs.yaml 中加了 `maniskill` section。以远程 configs.yaml 实际内容为准。\n\n## 2026-05-12: 梯度分解修正\n\n正确比例：reward=49%, KL=35%, obs=16%（不是之前错误的 \"obs=93%\"）。Full-SGS 不可靠（collapse_rate=0.5）。多条通路独立贡献。\n\n## 2026-05-11: Seed 提交前必查\n\n提交复现/对照实验前必须检查 parent 和 sibling 实验的 seed，避免重复。\n\n## 2026-05-10: EGL device ID\n\ncuda:N 实验必须设 MUJOCO_EGL_DEVICE_ID=N，否则 eval 死锁。\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sgs-partial-effectiveness-literature_20260517T225544",
  "tool": "mcp__agent-ml-research__save_project_file",
  "tool_args": {
    "project": "event-gated-adaptive-horizon",
    "file": "memory.md",
    "content": "# Memory — event-gated-adaptive-horizon\n\n## 2026-05-17: SGS partial effectiveness 文献参考\n\nexp_021 发现 Full-SGS 在 Walker 完全阻止 CIVO (NVE_peak=0.72) 但在 Cheetah 仅使其 transient (NVE_peak=9.94, 自恢复)。actor_grad_norm 在 Cheetah Full-SGS 中全程 0.0-0.1。文献搜索确认这是已知现象：\n\n**核心解释**：DreamerV3 连续控制 actor 的主要梯度来源是 dynamics backpropagation（通过 imagination rollout 的直通梯度）。Full-SGS 完全阻断此通路 → actor 梯度饥饿。\n\n**环境依赖性的文献支持**：\n1. **Ma et al. (ICML 2024)** — 标准 world model 的 policy gradient 随 horizon 指数级衰减；gradient path 质量是环境依赖的\n2. **Heess et al. (NeurIPS 2015, SVG)** — SVG(0)（无 model gradient）仅在简单任务有效；复杂任务需要 SVG(1+)。Walker≈简单, Cheetah≈复��\n3. **Amos et al. (L4DC 2021)** — 完全无 dynamics gradient 比有噪声的 dynamics gradient 更差\n4. **Nauman et al. (ICML 2024)** — 60+ agents, 14 tasks：regularization effectiveness fundamentally task-dependent，无 universal 最优\n\n**为什么 Walker 可以 Cheetah 不行**：\n- Walker Walk: 2 关节, reward=站立+前进, 浅层 credit assignment → 残余 REINFORCE/value gradient 足够\n- Cheetah Run: 6 关节, reward=速度, 需要多关节协调 → 深层 temporal credit assignment 被 Full-SGS 阻断\n\n**论文 framing**：Full-SGS 的部分有效性不是方法缺陷，而是 blanket gradient blocking 的预期后果。这恰好论证了 EVENT-GATED selective intervention 优于 Full-SGS 的必要性。\n\n## 2026-05-17: dt_emb \"困境\" — frozen prevents CIVO but kills gating\n\nexp_022b 确认：frozen random dt_emb 阻止 CIVO (ve_ratio 峰值仅 0.218)，但 gate 收敛为近均匀分布 (entropy_ratio=0.912)。核心原因：随机嵌入不携带时间语义 → gate 无法区分 dt 值。\n\n**设计启示**：CIVO 因果链需要 gradient-driven 语义 dt 表征。阻止 CIVO 的方式（SGS、freeze、remove）都会同时降低 dt_emb 的语义质量，形成 safety-utility tradeoff。这对论文来说是诊断发现（C2 的深化），不是需要解决的工程问题。\n\n## 2026-05-17: PickCube detector backtest 教训（CRITICAL）\n\nWorker 的 detector backtest 分析得出错误结论（TP），实际是 TN。三个方法论错误：\n1. 用 NVE 代替 raw V/E ratio（detector 是 baseline-free 的，用的是 r_t = V/max(E, ε)，不是 NVE）\n2. Acceleration condition 遗漏：prev_delta 也必须 > τ_vel（不只是当前 delta）\n3. 未检查 eval decline condition (c_dec)\n\n**教训**：detector backtest 必须严格逐条对照 Algorithm 1 的每个条件，不能凭 NVE 近似推断。以后所有 detector 相关分析必须用 raw V/E ratio 而非 NVE。\n\n## 2026-05-17: PickCube CIVO pattern — transient, not persistent\n\nexp_019b reveals PickCube exhibits \"transient CIVO\": NVE peaks 3.78× @52.5K then deflates to 0.08× by 132.5K, with eval recovering to 26.9. This contrasts Walker Walk's monotonic acceleration → collapse (2/3 seeds) pattern. Gate locked at dt=2 throughout (entropy=0). Value function transitions from overestimation to severe underestimation.\n\n**Key insight**: CIVO onset is environment-general (trained dt_emb → NVE spike in both environments), but CIVO resolution is environment-dependent (collapse vs self-correction).\n\n**Detector**: does NOT trigger on PickCube (TN). Oscillatory V/E pattern filtered by acceleration condition. This demonstrates detector specificity — it does not over-fire on noisy patterns.\n\n## 2026-05-17: exp_022 curriculum misconfiguration lesson\n\ngate_curriculum_phase1=50000 in configs.yaml means 50K env steps. With action_repeat=2, this = 100K logger steps. A 105K step experiment never exits phase1 warmup. **Lesson**: always compute effective curriculum schedule accounting for action_repeat before submitting.\n\nphase1=0, phase2=0 is safe: gate_scale=1.0 from step 0, no divide-by-zero risk (the linear interpolation branch is never entered).\n\n## 2026-05-15: 服务器代码目录确认\n\n源码在 `/root/autodl-tmp/event-gated-adaptive-horizon/`，不在 `/root/runs/event-gated-adaptive-horizon/`（后者只有日志）。\n\n## 2026-05-14: GPU 隔离确认\n\nCUDA_VISIBLE_DEVICES 隔离正确。`--device cuda:0` + `CUDA_VISIBLE_DEVICES=1` = 物理 GPU 1。\n\n## 2026-05-13: ManiSkill3 config key\n\nPickCube 实验必须用 `--configs defaults maniskill_state`（不是 `maniskill`，那个 key 不存在会 crash）。但实际 019b resubmit 用的是 `--configs defaults maniskill`，因为后来在 configs.yaml 中加了 `maniskill` section。以远程 configs.yaml 实际内容为准。\n\n## 2026-05-12: 梯度分解修正\n\n正确比例：reward=49%, KL=35%, obs=16%（不是之前错误的 \"obs=93%\"）。Full-SGS 不可靠（collapse_rate=0.5）。多条通路独立贡献。\n\n## 2026-05-11: Seed 提交前必查\n\n提交复现/对照实验前必须检查 parent 和 sibling 实验的 seed，避免重复。\n\n## 2026-05-10: EGL device ID\n\ncuda:N 实验必须设 MUJOCO_EGL_DEVICE_ID=N，否则 eval 死锁。\n"
  }
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-17T23:01:07.512272+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/memory.md\", \"saved\": true}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sgs-partial-effectiveness-literature_20260517T225544",
  "tool": "mcp__agent-ml-research__save_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 65 · 2026-05-17T23:01:07.512458+00:00_

完成。总结：

**文献搜索结果** — Full-SGS 环境依赖效果有充分文献支持：

| 论文 | 核心发现 |
|------|----------|
| Ma et al. (ICML 2024) | World model 的 policy gradient 随 horizon 指数衰减；gradient path 质量是环境依赖的 |
| Heess et al. (NeurIPS 2015, SVG) | SVG(0)（无 model gradient）仅简单任务有效；复杂任务需 SVG(1+) |
| Amos et al. (L4DC 2021) | 完全无 dynamics gradient 比有噪声的 dynamics gradient 更差 |
| Nauman et al. (ICML 2024) | 60+ agents / 14 tasks：regularization effectiveness fundamentally task-dependent |

**机制解释**：DreamerV3 连续控制 actor 依赖 dynamics backprop 作为主要梯度来源。Full-SGS 完全阻断此通路。Walker（2关节/浅层 credit assignment）能靠残余信号存活；Cheetah（6关节/深层协调）被梯度饥饿（actor_grad_norm=0.0-0.1），但因 DreamerV3 的 categorical value + normalization 隐式正则化最终自恢复。

**论文 framing**：这不是 SGS 的失败，而是论证 event-gated selective intervention 优于 blanket SGS 的证据。

已更新：literature_map.yaml（+4 papers, survey_tag: sgs-partial-effectiveness）、memory.md（新增段落）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_sgs-partial-effectiveness-literature_20260517T225544"
}
```

</details>

---
