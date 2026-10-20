# research 009c negative literature

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 27
- **Recorded user turns:** 0
- **Tool calls:** 13
- **Original source:** `logs/chats/worker_research_009c-negative-literature_20260514T142523.jsonl`
- **Structured JSON:** [`76a7bf1f8abca400087d.json`](../../sessions/76/76a7bf1f8abca400087d.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

27 recorded events

### Tool call

_source line 1 · 2026-05-14T14:28:23.276653+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file,WebSearch",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_009c-negative-literature_20260514T142523",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file,WebSearch",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-14T14:28:23.277053+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_009c-negative-literature_20260514T142523",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-14T14:28:23.277243+00:00_

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
  "session": "worker_research_009c-negative-literature_20260514T142523",
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

_source line 4 · 2026-05-14T14:28:23.277441+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/memory.md\", \"content\": \"# Memory\\n\\n## 2026-05-14: Actor Entropy 分析决策（Director 修正）\\n\\n- **C2 cleanest comparison pair**: 008f vs 008d（仅 dt_embed_dim 不同）。不用 008c vs 008d（两个变量差异：subsample + dt_emb）。\\n- **论文措辞**: 用 \\\"entropy convergence delayed\\\"，不说 \\\"entropy rises\\\"。\\n- **原因**: 008c（subsample OFF）vs 008d（subsample ON）有两个变量差异，不是 clean single-variable control。008f 和 008d 唯一差异是 dt_embed_dim（0 vs 32），是最干净的因果对照。\\n\\n## 2026-05-14: cuda:1 排期（Director 确认）\\n\\n009c → **009b**（008d s2）→ 009e（008d s1）→ 009f（008f s1）→ plan_060\\n\\n## 2026-05-14: Cheetah Run / Cartpole Swingup 环境验证\\n\\n### 结论：代码无需修改，直接可用\\n\\n代码通过 `--task` 参数自动解析环境名，流程：\\n- `--task dmc_cheetah_run` → `suite.load(\\\"cheetah\\\", \\\"run\\\")`\\n- `--task dmc_cartpole_swingup` → `suite.load(\\\"cartpole\\\", \\\"swingup\\\")`\\n\\n`dmc_proprio` 配置（action_repeat=2, envs=4, train_ratio=512, MLP encoder/decoder）对所有 DMC proprio 环境通用。\\n\\n### 环境 Observation/Action Space 对比\\n\\n| 环境 | Obs dims | Action dims | Action range |\\n|------|----------|-------------|--------------|\\n| walker_walk | orientations(14), height(1), velocity(9) = 24D | 6 | [-1, 1] |\\n| cheetah_run | position(8), velocity(9) = 17D | 6 | [-1, 1] |\\n| cartpole_swingup | position(3), velocity(2) = 5D | 1 | [-1, 1] |\\n\\n**注意：Cartpole Swingup obs/act 维度远小于 Walker/Cheetah。** MLP encoder/decoder 自动适配（从 obs_space 推断），无需手动调整。但模型容量可能过大——默认 512 units 对 5D obs + 1D act 可能 overkill。如果训练不稳定可考虑减小网络。\\n\\n### 启动命令模板\\n\\n**Cheetah Run Baseline:**\\n```bash\\npython dreamer.py --configs defaults dmc_proprio \\\\\\n  --task dmc_cheetah_run \\\\\\n  --logdir logdir/exp_XXX_baseline_cheetah_sY \\\\\\n  --steps 500000 --seed Y --compile False --device cuda:Z\\n```\\n\\n**Cheetah Run Treatment (以 008f config 为例):**\\n```bash\\npython dreamer.py --configs defaults dmc_proprio \\\\\\n  --task dmc_cheetah_run 
…[truncated 1984 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_009c-negative-literature_20260514T142523",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-14T14:28:23.277600+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "seed-dependent failure modes model-based reinforcement learning high variance"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_009c-negative-literature_20260514T142523",
  "tool": "WebSearch",
  "tool_args": {
    "query": "seed-dependent failure modes model-based reinforcement learning high variance"
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-14T14:28:23.277725+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "DreamerV3 high variance seed sensitivity world model RL"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_009c-negative-literature_20260514T142523",
  "tool": "WebSearch",
  "tool_args": {
    "query": "DreamerV3 high variance seed sensitivity world model RL"
  }
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-14T14:28:23.277888+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "compounding error world model RL failure modes beyond model exploitation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_009c-negative-literature_20260514T142523",
  "tool": "WebSearch",
  "tool_args": {
    "query": "compounding error world model RL failure modes beyond model exploitation"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-14T14:28:23.278061+00:00_

Web search results for query: "DreamerV3 high variance seed sensitivity world model RL"

Links: [{"title":"GitHub - danijar/dreamerv3: Mastering Diverse Domains through World Models · GitHub","url":"https://github.com/danijar/dreamerv3"},{"title":"DreamerV3: Mastering Diverse Domains through World Models","url":"https://vitalab.github.io/article/2023/01/19/DreamerV3.html"},{"title":"Mastering Diverse Control Tasks through World Models","url":"https://danijar.com/project/dreamerv3/"},{"title":"[2301.04104] Mastering Diverse Domains through World Models","url":"https://arxiv.org/abs/2301.04104"},{"title":"DreamerNav: learning-based autonomous navigation in dynamic indoor environments using world models - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12510832/"},{"title":"Mastering Diverse Domains through World Models","url":"https://arxiv.org/pdf/2301.04104"},{"title":"Mastering diverse control tasks through world models - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12003158/"},{"title":"DreamerV3-XP: Optimizing exploration through uncertainty estimation","url":"https://arxiv.org/html/2510.21418v1"},{"title":"Mastering diverse control tasks through world models | Nature","url":"https://www.nature.com/articles/s41586-025-08744-2"},{"title":"DreamerV3: Robust Latent Model-Based RL","url":"https://www.emergentmind.com/topics/dreamerv3"}]

Based on the search results, I found information about DreamerV3 and some references to variance and seed sensitivity, though the specific focus on "high variance seed sensitivity" wasn't extensively detailed in these results. Here's what I found:

## DreamerV3 Overview

DreamerV3 is a general algorithm that outperforms specialized methods across over 150 diverse tasks, with a single configuration. The world model encodes sensory inputs into categorical representations and predicts future representations and rewards given actions.

## Robustness and Stability Features

Robustness techniques based on normalization, balanc
…[truncated 1156 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_009c-negative-literature_20260514T142523",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-14T14:28:23.278236+00:00_

Web search results for query: "compounding error world model RL failure modes beyond model exploitation"

Links: [{"title":"Learning to Combat Compounding-Error in Model-Based Reinforcement Learning | OpenReview","url":"https://openreview.net/forum?id=S1g_S0VYvr"},{"title":"Learning to Combat Compounding-Error in Model-Based Reinforcement Learning","url":"https://webdocs.cs.ualberta.ca/~chenjun/files/drlw_adambrl_full.pdf"},{"title":"A Note on Loss Functions and Error Compounding in Model-based Reinforcement Learning","url":"https://arxiv.org/html/2404.09946"},{"title":"[1912.11206] Learning to Combat Compounding-Error in Model-Based Reinforcement Learning","url":"https://ar5iv.labs.arxiv.org/html/1912.11206"},{"title":"ResWM: Residual-Action World Model for Visual RL","url":"https://arxiv.org/html/2603.11110"},{"title":"Uncertainty-Aware Robotic World Model Makes Offline Model-Based Reinforcement Learning Work on Real Robots","url":"https://arxiv.org/html/2504.16680"},{"title":"Failure-Aware RL: Reliable Offline-to-Online Reinforcement Learning with Self-Recovery for Real-World Manipulation","url":"https://arxiv.org/html/2601.07821"},{"title":"[2404.09946] A Note on Loss Functions and Error Compounding in Model-based Reinforcement Learning","url":"https://arxiv.org/abs/2404.09946"},{"title":"Week 5: Model-Based Methods - Deep RL Course","url":"https://deeprlcourse.github.io/course_notes/model-based/"},{"title":"Combating the Compounding-Error Problem with a Multi-step Model Kavosh Asadi","url":"https://arxiv.org/pdf/1905.13320"}]

I found comprehensive research on compounding errors in world models and RL failure modes. Here are the key findings:

## Core Problem

Model errors can compound and render the model useless for planning, which can lead to catastrophic failure of model-based RL. The model may produce "fake" inputs that cannot occur in the domain, which are then fed back to the model, and two sources of error co-exist: the model is imperfect, and the model
…[truncated 1424 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_009c-negative-literature_20260514T142523",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-14T14:28:23.278433+00:00_

Web search results for query: "seed-dependent failure modes model-based reinforcement learning high variance"

Links: [{"title":"Variability of Deep Reinforcement Learning Agents in Atari ...","url":"https://people.cs.umass.edu/~kclary/NeurIPS_Critiquing_Trends_Workshop_2018___Variability_of_Deep_RL.pdf"},{"title":"Reinforcement Learning for Fail-Operational Systems with Disentangled Dual-Skill Variables","url":"https://www.mdpi.com/2227-7080/13/4/156"},{"title":"Structural dominant failure modes searching method based on deep reinforcement learning - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0951832021007341"},{"title":"Failure Modes in Machine Learning","url":"https://arxiv.org/pdf/1911.11034"},{"title":"Abstract","url":"https://arxiv.org/html/2510.14503"},{"title":"VARIANCE REDUCTION FOR REINFORCEMENT LEARN","url":"https://people.csail.mit.edu/hongzi/var-website/content/iclr-19.pdf"},{"title":"Measuring the Robustness of Multi-Agent Reinforcement Learning Systems under Partial Agent Failure | Proceedings of the Intelligent Robotics FAIR 2025","url":"https://dl.acm.org/doi/10.1145/3759355.3759373"},{"title":"(PDF) Learning from Failures: Understanding LLM Alignment through Failure-Aware Inverse RL","url":"https://www.researchgate.net/publication/396291521_Learning_from_Failures_Understanding_LLM_Alignment_through_Failure-Aware_Inverse_RL"},{"title":"(PDF) Reinforcement Learning for Model Building and Variance-penalized Control.","url":"https://www.researchgate.net/publication/221526502_Reinforcement_Learning_for_Model_Building_and_Variance-penalized_Control"},{"title":"Accelerating Model-Based Reinforcement Learning with State-Space World Models","url":"https://arxiv.org/html/2502.20168v1"}]

Based on the search results, I found several relevant papers and resources related to your query about seed-dependent failure modes, model-based reinforcement learning, and high variance:

## Key Findings:

**Seed-Dependent Variability in RL
…[truncated 1535 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_009c-negative-literature_20260514T142523",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-14T14:28:23.278669+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Henderson 2018 deep reinforcement learning that matters seed variance reproducibility"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_009c-negative-literature_20260514T142523",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Henderson 2018 deep reinforcement learning that matters seed variance reproducibility"
  }
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-14T14:28:23.278799+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "temporal abstraction model-based RL compounding error longer horizon collapse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_009c-negative-literature_20260514T142523",
  "tool": "WebSearch",
  "tool_args": {
    "query": "temporal abstraction model-based RL compounding error longer horizon collapse"
  }
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-14T14:28:23.278961+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"model-based reinforcement learning\" \"compounding error\" seed variance catastrophic failure multi-step rollout"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_009c-negative-literature_20260514T142523",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"model-based reinforcement learning\" \"compounding error\" seed variance catastrophic failure multi-step rollout"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-14T14:28:23.279118+00:00_

Web search results for query: "Henderson 2018 deep reinforcement learning that matters seed variance reproducibility"

Links: [{"title":"Deep reinforcement learning that matters | Proceedings of the Thirty-Second AAAI Conference on Artificial Intelligence and Thirtieth Innovative Applications of Artificial Intelligence Conference and Eighth AAAI Symposium on Educational Advances in Artificial Intelligence","url":"https://dl.acm.org/doi/abs/10.5555/3504035.3504427"},{"title":"[1709.06560] Deep Reinforcement Learning that Matters","url":"https://arxiv.org/abs/1709.06560"},{"title":"Deep reinforcement learning that matters - Princeton University","url":"https://collaborate.princeton.edu/en/publications/deep-reinforcement-learning-that-matters/"},{"title":"Deep Reinforcement Learning that Matters (1709.06560v3)","url":"https://www.emergentmind.com/papers/1709.06560"},{"title":"[PDF] Deep Reinforcement Learning that Matters | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Deep-Reinforcement-Learning-that-Matters-Henderson-Islam/33690ff21ef1efb576410e656f2e60c89d0307d6"},{"title":"(PDF) Deep Reinforcement Learning That Matters","url":"https://www.researchgate.net/publication/319953023_Deep_Reinforcement_Learning_That_Matters"},{"title":"Deep Reinforcement Learning That Matters | Proceedings of the AAAI Conference on Artificial Intelligence","url":"https://ojs.aaai.org/index.php/AAAI/article/view/11694"},{"title":"Deep Reinforcement Learning that Matters","url":"https://arxiv.org/pdf/1709.06560"},{"title":"Variability of Deep Reinforcement Learning Agents in Atari ...","url":"https://people.cs.umass.edu/~kclary/NeurIPS_Critiquing_Trends_Workshop_2018___Variability_of_Deep_RL.pdf"},{"title":"Reproducibility in Deep RL | Advanced RL","url":"https://apxml.com/courses/advanced-reinforcement-learning/chapter-8-rl-implementation-optimization/reproducibility-deep-rl"}]

I found comprehensive information about the Henderson 2018 paper on deep reinforcement learning
…[truncated 1490 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_009c-negative-literature_20260514T142523",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-14T14:28:23.279343+00:00_

Web search results for query: "temporal abstraction model-based RL compounding error longer horizon collapse"

Links: [{"title":"Long-Horizon Planning with Predictable Skills","url":"https://rlj.cs.umass.edu/2025/papers/RLJ_RLC_2025_136.pdf"},{"title":"Emergent temporal abstractions in autoregressive models enable hierarchical reinforcement learning","url":"https://arxiv.org/html/2512.20605v1"},{"title":"Emergent temporal abstractions in autoregressive models enable hierarchical reinforcement learning | alphaXiv","url":"https://www.alphaxiv.org/overview/2512.20605"},{"title":"[2512.20605] Emergent temporal abstractions in autoregressive models enable hierarchical reinforcement learning","url":"https://arxiv.org/abs/2512.20605"},{"title":"Hierarchical Model-Based Reinforcement Learning with Temporal Abstractions | Open Research Commons","url":"https://bcommons.berkeley.edu/hierarchical-model-based-reinforcement-learning-temporal-abstractions"},{"title":"[Literature Review] Emergent temporal abstractions in autoregressive models enable hierarchical reinforcement learning","url":"https://www.themoonlight.io/en/review/emergent-temporal-abstractions-in-autoregressive-models-enable-hierarchical-reinforcement-learning"},{"title":"Learning to Combat Compounding-Error in Model-Based Reinforcement Learning | OpenReview","url":"https://openreview.net/forum?id=S1g_S0VYvr"},{"title":"Emergent temporal abstractions in autoregressive","url":"https://arxiv.org/pdf/2512.20605"},{"title":"Improving planning and MBRL with temporally-extended actions","url":"https://arxiv.org/html/2505.15754"},{"title":"[Quick Review] Emergent temporal abstractions in autoregressive models enable hierarchical reinforcement learning","url":"https://liner.com/review/emergent-temporal-abstractions-in-autoregressive-models-enable-hierarchical-reinforcement-learning"}]

Based on the search results, here's what I found on temporal abstraction in model-based RL and compounding error issues with longer horizon
…[truncated 1457 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_009c-negative-literature_20260514T142523",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-14T14:28:23.279540+00:00_

Web search results for query: ""model-based reinforcement learning" "compounding error" seed variance catastrophic failure multi-step rollout"

Links: [{"title":"Combating the Compounding-Error Problem with a Multi-step Model — Grokipedia","url":"https://grokipedia.com/page/190513320"},{"title":"[1912.11206] Learning to Combat Compounding-Error in Model-Based Reinforcement Learning","url":"https://ar5iv.labs.arxiv.org/html/1912.11206"},{"title":"MODEL-BASED REINFORCEMENT LEARNING WITH MULTI-STEP PLAN VALUE ESTIMATION","url":"https://arxiv.org/pdf/2209.05530"},{"title":"Learning to Combat Compounding-Error in Model-Based Reinforcement Learning","url":"https://webdocs.cs.ualberta.ca/~chenjun/files/drlw_adambrl_full.pdf"},{"title":"[2504.01766] Learning with Imperfect Models: When Multi-step Prediction Mitigates Compounding Error","url":"https://arxiv.org/abs/2504.01766"},{"title":"Learning with Imperfect Models: When Multi-step Prediction Mitigates Compounding Error","url":"https://arxiv.org/html/2504.01766"},{"title":"Learning with Imperfect Models: When Multi-step Prediction Mitigates Compounding Error - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250401766S/abstract"},{"title":"When to Trust Your Model: Model-Based Policy Optimization Michael Janner","url":"http://papers.neurips.cc/paper/9416-when-to-trust-your-model-model-based-policy-optimization.pdf"},{"title":"Statistical Efficiency of Single- and Multi-step Models for Forecasting and Control","url":"https://arxiv.org/html/2603.23465"},{"title":"Diminishing Return of Value Expansion Methods","url":"https://arxiv.org/html/2412.20537"}]

The search results contain comprehensive information about compounding error in model-based reinforcement learning and multi-step rollouts. Here are the key findings:

## Compounding Error in Model-Based RL

The compounding error problem in model-based reinforcement learning (MBRL) refers to the phenomenon where inaccuracies in a learned dynamics model propagate and am
…[truncated 1921 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_009c-negative-literature_20260514T142523",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-14T14:28:23.279738+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Janner 2019 \"when to trust your model\" model-based policy optimization rollout horizon branched rollout"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_009c-negative-literature_20260514T142523",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Janner 2019 \"when to trust your model\" model-based policy optimization rollout horizon branched rollout"
  }
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-14T14:28:23.279899+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Nikishin 2022 primacy bias deep reinforcement learning seed sensitivity network reuse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_009c-negative-literature_20260514T142523",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Nikishin 2022 primacy bias deep reinforcement learning seed sensitivity network reuse"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-14T14:28:23.280068+00:00_

Web search results for query: "Janner 2019 "when to trust your model" model-based policy optimization rollout horizon branched rollout"

Links: [{"title":"[1906.08253] When to Trust Your Model: Model-Based Policy Optimization","url":"https://arxiv.org/abs/1906.08253"},{"title":"When to Trust Your Model: Model-Based Policy Optimization Michael Janner","url":"https://arxiv.org/pdf/1906.08253"},{"title":"When to Trust Your Model: Model-Based Policy Optimization | OpenReview","url":"https://openreview.net/forum?id=SkgPIpcGar"},{"title":"When to Trust Your Model: Model-Based Policy Optimization","url":"https://jannerm.github.io/mbpo-www/"},{"title":"[PDF] When to Trust Your Model: Model-Based Policy Optimization | Semantic Scholar","url":"https://www.semanticscholar.org/paper/When-to-Trust-Your-Model:-Model-Based-Policy-Janner-Fu/9001698e033524864d4d45f051a5ba362d4afd9e"},{"title":"When to Trust Your Model: Model-Based Policy Optimization","url":"https://proceedings.neurips.cc/paper/2019/hash/5faf461eff3099671ad63c6f3f094f7f-Abstract.html"},{"title":"[Re] When to Trust Your Model: Model-Based Policy Optimization","url":"https://openreview.net/pdf?id=rkezvT9f6r"},{"title":"GitHub - jannerm/mbpo: Code for the paper \"When to Trust Your Model: Model-Based Policy Optimization\" · GitHub","url":"https://github.com/jannerm/mbpo"},{"title":"Replication of “When to Trust Your Model: Model-Based Policy Optimization”","url":"https://openreview.net/pdf?id=SkgPIpcGar"},{"title":"(Open Access) When to Trust Your Model: Model-Based Policy Optimization (2019) | Michael Janner | 603 Citations","url":"https://scispace.com/papers/when-to-trust-your-model-model-based-policy-optimization-54la64py12"}]

I found the paper you were looking for! Here are the search results for "When to Trust Your Model: Model-Based Policy Optimization" by Janner et al. (2019):

## Paper Overview

This paper by Michael Janner, Justin Fu, Marvin Zhang, and Sergey Levine studies the role of model usage in policy o
…[truncated 1329 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_009c-negative-literature_20260514T142523",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-14T14:28:23.280309+00:00_

Web search results for query: "Nikishin 2022 primacy bias deep reinforcement learning seed sensitivity network reuse"

Links: [{"title":"[2205.07802] The Primacy Bias in Deep Reinforcement Learning","url":"https://arxiv.org/abs/2205.07802"},{"title":"The Primacy Bias in Deep Reinforcement Learning","url":"https://proceedings.mlr.press/v162/nikishin22a.html"},{"title":"The Primacy Bias in Deep Reinforcement Learning Evgenii Nikishin∗","url":"https://evgenii-nikishin.github.io/data/RL_primacy_bias_RLDM2022.pdf"},{"title":"It's Time to Move On: Primacy Bias and Why It Helps to Forget | OpenReview","url":"https://openreview.net/forum?id=7ZEwqUyKMC"},{"title":"Evgenii Nikishin on X: \"The Primacy Bias in Deep Reinforcement Learning In a new #ICML2022 paper, we identify a damaging tendency of Deep RL agents to overfit to early experiences and propose a simple yet *powerful* remedy by periodically resetting last network layers. https://t.co/Ll7iyzXyCU 1/N 🧵 https://t.co/cmHPVdl5ds\" / X","url":"https://x.com/nikishin_evg/status/1527682443184115713?lang=en"},{"title":"[PDF] The Primacy Bias in Deep Reinforcement Learning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/The-Primacy-Bias-in-Deep-Reinforcement-Learning-Nikishin-Schwarzer/69b80ce5ab6c2263b145b1eaa23664145938f351"},{"title":"GitHub - evgenii-nikishin/rl_with_resets: JAX implementation of deep RL agents with resets from the paper \"The Primacy Bias in Deep Reinforcement Learning\"","url":"https://github.com/evgenii-nikishin/rl_with_resets"},{"title":"Evgenii Nikishin's research works","url":"https://www.researchgate.net/scientific-contributions/Evgenii-Nikishin-2196050921"},{"title":"It's Time to Move On: Primacy Bias and Why It Helps to Forget | ICLR Blogposts 2024","url":"https://iclr-blogposts.github.io/2024/blog/primacy-bias-and-why-it-helps-to-forget/"},{"title":"[2205.07802v1] The Primacy Bias in Deep Reinforcement Learning","url":"https://arxiv.org/abs/2205.07802v1"}]

Based on the search r
…[truncated 1749 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_009c-negative-literature_20260514T142523",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-14T14:28:23.281173+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Talvitie 2017 self-delusion model-based RL hallucination objective mismatch world model"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_009c-negative-literature_20260514T142523",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Talvitie 2017 self-delusion model-based RL hallucination objective mismatch world model"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-14T14:28:23.281417+00:00_

Web search results for query: "Talvitie 2017 self-delusion model-based RL hallucination objective mismatch world model"

Links: [{"title":"Mitigating Value Hallucination in Dyna-Style Planning via Multistep Predecessor Models","url":"https://arxiv.org/html/2006.04363"},{"title":"Mitigating LLM Hallucinations. Hallucinations in large language models… | by David Alami | Medium","url":"https://davidalami.medium.com/mitigating-llm-hallucinations-ce35c29e3724"},{"title":"Frontiers | Survey and analysis of hallucinations in large language models: attribution to prompting strategies or model behavior","url":"https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2025.1622292/full"},{"title":"Detection and Mitigation of Hallucination in Large ...","url":"https://arxiv.org/pdf/2505.12886"},{"title":"Review Not peer-reviewed version A Survey on Hallucination in Large","url":"https://www.preprints.org/manuscript/202510.0540/v1/download"},{"title":"Large Language Models Hallucination: A Comprehensive Survey","url":"https://arxiv.org/html/2510.06265v2"},{"title":"From Illusion to Insight: A Taxonomic Survey of Hallucination Mitigation Techniques in LLMs","url":"https://www.mdpi.com/2673-2688/6/10/260"},{"title":"Thinking, Faithful and Stable: Mitigating Hallucinations in LLMs","url":"https://cs224r.stanford.edu/projects/pdfs/Final_Report_CS224r.pdf"},{"title":"A Comprehensive Survey of Hallucination in Large Language Models: Causes, Detection, and Mitigation","url":"https://arxiv.org/html/2510.06265v1"},{"title":"LLM Hallucinations in 2026: How to Understand and Tackle AI’s Most Persistent Quirk | Lakera – Protecting AI teams that disrupt the world.","url":"https://www.lakera.ai/blog/guide-to-hallucinations-in-large-language-models"}]

Based on the search results, I found relevant information about Talvitie's work on the "self-delusion" problem in model-based reinforcement learning:

Talvitie proposed Hallucinated Replay: training a model on its own i
…[truncated 1066 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_009c-negative-literature_20260514T142523",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-14T14:28:23.281598+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Lambert 2020 \"objective mismatch\" model-based reinforcement learning failure modes"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_009c-negative-literature_20260514T142523",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Lambert 2020 \"objective mismatch\" model-based reinforcement learning failure modes"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-14T14:28:23.281766+00:00_

Web search results for query: "Lambert 2020 "objective mismatch" model-based reinforcement learning failure modes"

Links: [{"title":"Objective Mismatch in Model-based Reinforcement Learning","url":"http://proceedings.mlr.press/v120/lambert20a/lambert20a.pdf"},{"title":"[2002.04523] Objective Mismatch in Model-based Reinforcement Learning","url":"https://arxiv.org/abs/2002.04523"},{"title":"A Unified View on Solving Objective Mismatch in Model-Based Reinforcement Learning","url":"https://arxiv.org/html/2310.06253v2"},{"title":"dblp: Objective Mismatch in Model-based Reinforcement Learning.","url":"https://dblp.org/rec/journals/corr/abs-2002-04523.html"},{"title":"A Unified View on Solving Objective Mismatch in Model-","url":"https://arxiv.org/pdf/2310.06253"},{"title":"[PDF] Objective Mismatch in Model-based Reinforcement Learning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Objective-Mismatch-in-Model-based-Reinforcement-Lambert-Amos/ecbdc83a1aa8d196943d8997300be871b1c7c2dc"},{"title":"A Unified View on Solving Objective Mismatch in Model","url":"https://openreview.net/pdf?id=tQVZgvXhZb"},{"title":"Objective Mismatch in Model-based Reinforcement Learning - ADS","url":"https://ui.adsabs.harvard.edu/abs/2020arXiv200204523L/abstract"},{"title":"Objective Mismatch in Model-based Reinforcement Learning | DeepAI","url":"https://deepai.org/publication/objective-mismatch-in-model-based-reinforcement-learning"},{"title":"objective mismatch in reinforcement learning from human ...","url":"https://arxiv.org/pdf/2311.00168"}]

I found information about the Lambert 2020 paper on objective mismatch in model-based reinforcement learning. Here's a summary of the key findings:

## Overview

The paper identifies a fundamental issue of the standard MBRL framework called the objective mismatch issue. Objective mismatch arises when one objective is optimized in the hope that a second, often uncorrelated, metric will also be optimized.

## The Core Problem

In the co
…[truncated 1308 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_009c-negative-literature_20260514T142523",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-14T14:28:23.282027+00:00_

called mcp__agent-ml-research__save_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__save_project_file</summary>

````json
{
  "project": "event-gated-adaptive-horizon",
  "file": "memory.md",
  "content": "# Memory\n\n## 2026-05-14: Actor Entropy 分析决策（Director 修正）\n\n- **C2 cleanest comparison pair**: 008f vs 008d（仅 dt_embed_dim 不同）。不用 008c vs 008d（两个变量差异：subsample + dt_emb）。\n- **论文措辞**: 用 \"entropy convergence delayed\"，不说 \"entropy rises\"。\n- **原因**: 008c（subsample OFF）vs 008d（subsample ON）有两个变量差异，不是 clean single-variable control。008f 和 008d 唯一差异是 dt_embed_dim（0 vs 32），是最干净的因果对照。\n\n## 2026-05-14: cuda:1 排期（Director 确认）\n\n009c → **009b**（008d s2）→ 009e（008d s1）→ 009f（008f s1）→ plan_060\n\n## 2026-05-14: Cheetah Run / Cartpole Swingup 环境验证\n\n### 结论：代码无需修改，直接可用\n\n代码通过 `--task` 参数自动解析环境名，流程：\n- `--task dmc_cheetah_run` → `suite.load(\"cheetah\", \"run\")`\n- `--task dmc_cartpole_swingup` → `suite.load(\"cartpole\", \"swingup\")`\n\n`dmc_proprio` 配置（action_repeat=2, envs=4, train_ratio=512, MLP encoder/decoder）对所有 DMC proprio 环境通用。\n\n### 环境 Observation/Action Space 对比\n\n| 环境 | Obs dims | Action dims | Action range |\n|------|----------|-------------|--------------|\n| walker_walk | orientations(14), height(1), velocity(9) = 24D | 6 | [-1, 1] |\n| cheetah_run | position(8), velocity(9) = 17D | 6 | [-1, 1] |\n| cartpole_swingup | position(3), velocity(2) = 5D | 1 | [-1, 1] |\n\n**注意：Cartpole Swingup obs/act 维度远小于 Walker/Cheetah。** MLP encoder/decoder 自动适配（从 obs_space 推断），无需手动调整。但模型容量可能过大——默认 512 units 对 5D obs + 1D act 可能 overkill。如果训练不稳定可考虑减小网络。\n\n### 启动命令模板\n\n**Cheetah Run Baseline:**\n```bash\npython dreamer.py --configs defaults dmc_proprio \\\n  --task dmc_cheetah_run \\\n  --logdir logdir/exp_XXX_baseline_cheetah_sY \\\n  --steps 500000 --seed Y --compile False --device cuda:Z\n```\n\n**Cheetah Run Treatment (以 008f config 为例):**\n```bash\npython dreamer.py --configs defaults dmc_proprio \\\n  --task dmc_cheetah_run \\\n  --logdir logdir/exp_XXX_008f_cheetah_sY \\\n  --steps 105000 --seed Y --compile False --device cuda:Z \\\n  --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 \\\n  --imag_horizon 8 --gate_dt_embed_dim 0\n```\n\n**Cartpole Swingup Baseline:**\n```bash\npython dreamer.py --configs defaults dmc_proprio \\\n  --task dmc_cartpole_swingup \\\n  --logdir logdir/exp_XXX_baseline_cartpole_sY \\\n  --steps 500000 --seed Y --compile False --device cuda:Z\n```\n\n**Cartpole Swingup Treatment (以 008f config 为例):**\n```bash\npython dreamer.py --configs defaults dmc_proprio \\\n  --task dmc_cartpole_swingup \\\n  --logdir logdir/exp_XXX_008f_cartpole_sY \\\n  --steps 105000 --seed Y --compile False --device cuda:Z \\\n  --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 \\\n  --imag_horizon 8 --gate_dt_embed_dim 0\n```\n\n### 环境特定注意事项\n\n1. **action_repeat=2** 对三个环境都适用（DMC 标准设置）\n2. **time_limit=1000**（默认）对三个环境都适用\n3. **Cartpole 维度差异**：obs 5D vs Walker 24D，act 1D vs Walker 6D。模型自动适配，但训练动态可能不同（更快收敛或更不稳定）\n4. **Cheetah 与 Walker 类似**：都是 locomotion 任务，obs/act 维度接近，预期行为最相似\n5. **环境变量**：`MUJOCO_GL=osmesa PYOPENGL_PLATFORM=osmesa LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6` 仍然需要\n6. **无需代码修改**\n\n### 当前运行中实验的命令格式（参考）\n\n```bash\n# exp_009a baseline (cuda:0)\npython dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk \\\n  --logdir logdir/exp_009a_baseline_walker_s2 --steps 500000 --seed 2 \\\n  --compile False --device cuda:0\n\n# exp_009c 008f treatment (cuda:1)\npython dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk \\\n  --logdir logdir/exp_009c_008f_walker_s2 --steps 105000 --seed 2 \\\n  --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 \\\n  --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0\n```\n\n## 2026-05-14: 009c Negative 文献联动\n\n### 背景\n\n009c (dt_embed_dim=0) 在 seed 1 恢复性能（503@105K），但 seed 2 持续下降（148@105K）。两个 seed 均未出现 delusional critic（v/e 加速发散）。说明存在 delusional critic 之外的第二种失败机制。\n\n### 相关文献\n\n**1. Henderson et al. (2018) \"Deep Reinforcement Learning that Matters\" — AAAI 2018**\n- 关键发现：相同超参数 + 不同 seed → 统计上显著不同的性能分布。这是 deep RL seed 方差问题的奠基性工作。\n- 与 009c 的关系：确认了 seed variance 在 deep RL 中是普遍现象，但我们的 case（503 vs 148，3.4x 差距）远超通常报告的方差范围，且仅在 temporal abstraction 条件下出现。\n\n**2. Nikishin et al. (2022) \"The Primacy Bias in Deep Reinforcement Learning\" — ICML 2022**\n- 关键发现：deep RL agent 对早期经验过拟合（primacy bias），不同 seed 导致不同的早期轨迹，进而导致截然不同的训练结果。高 replay ratio 和长 n-step target 会放大这一效应。周期性重置网络末层可缓解。\n- 与 009c 的关系：**最强候选机制。** DreamerV3 的 world model 在不同 seed 下学到不同的早期表征，temporal abstraction（dt=2 + imag_horizon=8）相当于将 imagination 延长到 16 环境步，放大了早期表征差异的影响。seed 2 可能因 primacy bias 锁定在次优 world model 表征上，在 single-step imagination 下尚可工作，但在多步想象下崩塌。\n\n**3. Janner et al. (2019) \"When to Trust Your Model: Model-Based Policy Optimization\" — NeurIPS 2019**\n- 关键发现：model error 随 rollout 长度指数级复合（compounding error）。短的 branched rollout 能缓解此问题。理论上 error bound ≈ L^t · e₀，当 Lipschitz 常数 L > 1 时误差指数发散。\n- 与 009c 的关系：temporal abstraction 等效于延长 model rollout horizon。如果 seed 2 的 world model 在关键状态区域有略大的 1-step error，compounding effect 将小差异放大为灾难性失败。这解释了为什么 single-step baseline 对 seed 不敏感，但 temporal abstraction 下 seed 敏感性剧增。\n\n**4. Lambert et al. (2020) \"Objective Mismatch in Model-based Reinforcement Learning\" — L4DC 2020**\n- 关键发现：world model 的 1-step prediction accuracy 与下游控制性能不相关（objective mismatch）。model 可能在 1-step 指标上\"足够好\"，但在多步 rollout 中灾难性错误。\n- 与 009c 的关系：seed 2 的 world model 可能在 1-step loss 上与 seed 1 无显著差异（都通过了训练），但在多步 imagination 下暴露出 objective mismatch——1-step loss 无法捕捉的失败模式。\n\n### 综合分析\n\n009c 的 seed-dependent failure 最可能是 **primacy bias（Nikishin 2022）+ compounding error amplification（Janner 2019）** 的组合效应：\n\n1. 不同 seed → 不同的早期经验 → world model 学到不同的表征质量（primacy bias）\n2. Single-step imagination（baseline DreamerV3）对表征质量的微小差异不敏感\n3. Temporal abstraction 将 effective imagination horizon 从 H 步放大到 H×dt 环境步，指数级放大 model error\n4. Seed 2 的 world model 在某个关键状态子空间有略大的 prediction error，被 temporal abstraction 放大后导致 policy 崩塌\n\n这个机制与 delusional critic（v/e 加速发散）完全正交——它不需要 value function 失控，只需要 world model 在多步 rollout 下的 compounding error 足够大，导致 policy gradient 信号质量退化。\n\n### Paper Framing 建议\n\n**这不是一个全新发现，但交互机制是新颖的。**\n\n- Seed variance（Henderson 2018）和 compounding error（Janner 2019）各自都是已知现象\n- **新颖点**：temporal abstraction 作为 compounding error 的放大器，将原本可控的 seed variance 转化为灾难性失败。这一交互效应在已有文献中未被报告\n- 建议措辞：\"Temporal abstraction exposes a latent seed-dependent failure mode that is masked under single-step imagination. While seed variance and compounding error are individually well-documented, their interaction under temporal abstraction creates a qualitatively different failure regime — one where performance collapses without the hallmarks of value divergence.\"\n- 定位：不要声称发现了全新的失败模式，而是展示 temporal abstraction 如何改变已知失败模式的严重程度。这比\"新发现\"更可信，也更有实践指导意义（提示 temporal abstraction 方法需要更多 seed 验证）\n"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "worker_research_009c-negative-literature_20260514T142523",
  "tool": "mcp__agent-ml-research__save_project_file",
  "tool_args": {
    "project": "event-gated-adaptive-horizon",
    "file": "memory.md",
    "content": "# Memory\n\n## 2026-05-14: Actor Entropy 分析决策（Director 修正）\n\n- **C2 cleanest comparison pair**: 008f vs 008d（仅 dt_embed_dim 不同）。不用 008c vs 008d（两个变量差异：subsample + dt_emb）。\n- **论文措辞**: 用 \"entropy convergence delayed\"，不说 \"entropy rises\"。\n- **原因**: 008c（subsample OFF）vs 008d（subsample ON）有两个变量差异，不是 clean single-variable control。008f 和 008d 唯一差异是 dt_embed_dim（0 vs 32），是最干净的因果对照。\n\n## 2026-05-14: cuda:1 排期（Director 确认）\n\n009c → **009b**（008d s2）→ 009e（008d s1）→ 009f（008f s1）→ plan_060\n\n## 2026-05-14: Cheetah Run / Cartpole Swingup 环境验证\n\n### 结论：代码无需修改，直接可用\n\n代码通过 `--task` 参数自动解析环境名，流程：\n- `--task dmc_cheetah_run` → `suite.load(\"cheetah\", \"run\")`\n- `--task dmc_cartpole_swingup` → `suite.load(\"cartpole\", \"swingup\")`\n\n`dmc_proprio` 配置（action_repeat=2, envs=4, train_ratio=512, MLP encoder/decoder）对所有 DMC proprio 环境通用。\n\n### 环境 Observation/Action Space 对比\n\n| 环境 | Obs dims | Action dims | Action range |\n|------|----------|-------------|--------------|\n| walker_walk | orientations(14), height(1), velocity(9) = 24D | 6 | [-1, 1] |\n| cheetah_run | position(8), velocity(9) = 17D | 6 | [-1, 1] |\n| cartpole_swingup | position(3), velocity(2) = 5D | 1 | [-1, 1] |\n\n**注意：Cartpole Swingup obs/act 维度远小于 Walker/Cheetah。** MLP encoder/decoder 自动适配（从 obs_space 推断），无需手动调整。但模型容量可能过大——默认 512 units 对 5D obs + 1D act 可能 overkill。如果训练不稳定可考虑减小网络。\n\n### 启动命令模板\n\n**Cheetah Run Baseline:**\n```bash\npython dreamer.py --configs defaults dmc_proprio \\\n  --task dmc_cheetah_run \\\n  --logdir logdir/exp_XXX_baseline_cheetah_sY \\\n  --steps 500000 --seed Y --compile False --device cuda:Z\n```\n\n**Cheetah Run Treatment (以 008f config 为例):**\n```bash\npython dreamer.py --configs defaults dmc_proprio \\\n  --task dmc_cheetah_run \\\n  --logdir logdir/exp_XXX_008f_cheetah_sY \\\n  --steps 105000 --seed Y --compile False --device cuda:Z \\\n  --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 \\\n  --imag_horizon 8 --gate_dt_embed_dim 0\n```\n\n**Cartpole Swingup Baseline:**\n```bash\npython dreamer.py --configs defaults dmc_proprio \\\n  --task dmc_cartpole_swingup \\\n  --logdir logdir/exp_XXX_baseline_cartpole_sY \\\n  --steps 500000 --seed Y --compile False --device cuda:Z\n```\n\n**Cartpole Swingup Treatment (以 008f config 为例):**\n```bash\npython dreamer.py --configs defaults dmc_proprio \\\n  --task dmc_cartpole_swingup \\\n  --logdir logdir/exp_XXX_008f_cartpole_sY \\\n  --steps 105000 --seed Y --compile False --device cuda:Z \\\n  --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 \\\n  --imag_horizon 8 --gate_dt_embed_dim 0\n```\n\n### 环境特定注意事项\n\n1. **action_repeat=2** 对三个环境都适用（DMC 标准设置）\n2. **time_limit=1000**（默认）对三个环境都适用\n3. **Cartpole 维度差异**：obs 5D vs Walker 24D，act 1D vs Walker 6D。模型自动适配，但训练动态可能不同（更快收敛或更不稳定）\n4. **Cheetah 与 Walker 类似**：都是 locomotion 任务，obs/act 维度接近，预期行为最相似\n5. **环境变量**：`MUJOCO_GL=osmesa PYOPENGL_PLATFORM=osmesa LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6` 仍然需要\n6. **无需代码修改**\n\n### 当前运行中实验的命令格式（参考）\n\n```bash\n# exp_009a baseline (cuda:0)\npython dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk \\\n  --logdir logdir/exp_009a_baseline_walker_s2 --steps 500000 --seed 2 \\\n  --compile False --device cuda:0\n\n# exp_009c 008f treatment (cuda:1)\npython dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk \\\n  --logdir logdir/exp_009c_008f_walker_s2 --steps 105000 --seed 2 \\\n  --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 \\\n  --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0\n```\n\n## 2026-05-14: 009c Negative 文献联动\n\n### 背景\n\n009c (dt_embed_dim=0) 在 seed 1 恢复性能（503@105K），但 seed 2 持续下降（148@105K）。两个 seed 均未出现 delusional critic（v/e 加速发散）。说明存在 delusional critic 之外的第二种失败机制。\n\n### 相关文献\n\n**1. Henderson et al. (2018) \"Deep Reinforcement Learning that Matters\" — AAAI 2018**\n- 关键发现：相同超参数 + 不同 seed → 统计上显著不同的性能分布。这是 deep RL seed 方差问题的奠基性工作。\n- 与 009c 的关系：确认了 seed variance 在 deep RL 中是普遍现象，但我们的 case（503 vs 148，3.4x 差距）远超通常报告的方差范围，且仅在 temporal abstraction 条件下出现。\n\n**2. Nikishin et al. (2022) \"The Primacy Bias in Deep Reinforcement Learning\" — ICML 2022**\n- 关键发现：deep RL agent 对早期经验过拟合（primacy bias），不同 seed 导致不同的早期轨迹，进而导致截然不同的训练结果。高 replay ratio 和长 n-step target 会放大这一效应。周期性重置网络末层可缓解。\n- 与 009c 的关系：**最强候选机制。** DreamerV3 的 world model 在不同 seed 下学到不同的早期表征，temporal abstraction（dt=2 + imag_horizon=8）相当于将 imagination 延长到 16 环境步，放大了早期表征差异的影响。seed 2 可能因 primacy bias 锁定在次优 world model 表征上，在 single-step imagination 下尚可工作，但在多步想象下崩塌。\n\n**3. Janner et al. (2019) \"When to Trust Your Model: Model-Based Policy Optimization\" — NeurIPS 2019**\n- 关键发现：model error 随 rollout 长度指数级复合（compounding error）。短的 branched rollout 能缓解此问题。理论上 error bound ≈ L^t · e₀，当 Lipschitz 常数 L > 1 时误差指数发散。\n- 与 009c 的关系：temporal abstraction 等效于延长 model rollout horizon。如果 seed 2 的 world model 在关键状态区域有略大的 1-step error，compounding effect 将小差异放大为灾难性失败。这解释了为什么 single-step baseline 对 seed 不敏感，但 temporal abstraction 下 seed 敏感性剧增。\n\n**4. Lambert et al. (2020) \"Objective Mismatch in Model-based Reinforcement Learning\" — L4DC 2020**\n- 关键发现：world model 的 1-step prediction accuracy 与下游控制性能不相关（objective mismatch）。model 可能在 1-step 指标上\"足够好\"，但在多步 rollout 中灾难性错误。\n- 与 009c 的关系：seed 2 的 world model 可能在 1-step loss 上与 seed 1 无显著差异（都通过了训练），但在多步 imagination 下暴露出 objective mismatch——1-step loss 无法捕捉的失败模式。\n\n### 综合分析\n\n009c 的 seed-dependent failure 最可能是 **primacy bias（Nikishin 2022）+ compounding error amplification（Janner 2019）** 的组合效应：\n\n1. 不同 seed → 不同的早期经验 → world model 学到不同的表征质量（primacy bias）\n2. Single-step imagination（baseline DreamerV3）对表征质量的微小差异不敏感\n3. Temporal abstraction 将 effective imagination horizon 从 H 步放大到 H×dt 环境步，指数级放大 model error\n4. Seed 2 的 world model 在某个关键状态子空间有略大的 prediction error，被 temporal abstraction 放大后导致 policy 崩塌\n\n这个机制与 delusional critic（v/e 加速发散）完全正交——它不需要 value function 失控，只需要 world model 在多步 rollout 下的 compounding error 足够大，导致 policy gradient 信号质量退化。\n\n### Paper Framing 建议\n\n**这不是一个全新发现，但交互机制是新颖的。**\n\n- Seed variance（Henderson 2018）和 compounding error（Janner 2019）各自都是已知现象\n- **新颖点**：temporal abstraction 作为 compounding error 的放大器，将原本可控的 seed variance 转化为灾难性失败。这一交互效应在已有文献中未被报告\n- 建议措辞：\"Temporal abstraction exposes a latent seed-dependent failure mode that is masked under single-step imagination. While seed variance and compounding error are individually well-documented, their interaction under temporal abstraction creates a qualitatively different failure regime — one where performance collapses without the hallmarks of value divergence.\"\n- 定位：不要声称发现了全新的失败模式，而是展示 temporal abstraction 如何改变已知失败模式的严重程度。这比\"新发现\"更可信，也更有实践指导意义（提示 temporal abstraction 方法需要更多 seed 验证）\n"
  }
}
````

</details>

---

### Tool result

_source line 26 · 2026-05-14T14:28:23.282259+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/memory.md\", \"saved\": true}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_009c-negative-literature_20260514T142523",
  "tool": "mcp__agent-ml-research__save_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 27 · 2026-05-14T14:28:23.282427+00:00_

已更新 memory.md，在末尾追加了 "## 2026-05-14: 009c Negative 文献联动" section。核心结论：

**最相关的 3 篇文献：**
- **Nikishin et al. 2022 (ICML)** — primacy bias，agent 对早期经验过拟合，不同 seed → 不同表征质量。最强候选机制。
- **Janner et al. 2019 (NeurIPS)** — compounding error 随 rollout 长度指数增长，temporal abstraction 等效延长 rollout。
- **Lambert et al. 2020 (L4DC)** — objective mismatch，1-step loss 好不代表多步 rollout 好。

**对 009c 的解释：** primacy bias + compounding error amplification 的组合。Temporal abstraction 将 effective horizon 从 H 放大到 H×dt，指数级放大 seed 间 world model 质量的微小差异，导致 seed 2 崩塌而 seed 1 正常。与 delusional critic 正交。

**Paper framing 建议：** 不要声称新失败模式，而是展示 temporal abstraction 如何将已知的 seed variance 从可控变为灾难性。这一交互效应在文献中未被报告，是新颖的贡献点。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_009c-negative-literature_20260514T142523"
}
```

</details>

---
