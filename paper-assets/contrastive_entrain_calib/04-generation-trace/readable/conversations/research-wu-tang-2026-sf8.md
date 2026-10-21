# research wu tang 2026 sf8

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 9
- **Recorded user turns:** 0
- **Tool calls:** 4
- **Original source:** `logs/chats/worker_research_wu-tang-2026-sf8_20260522T115827.jsonl`
- **Structured JSON:** [`92d451194da36c230992.json`](../../sessions/92/92d451194da36c230992.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

9 recorded events

### Tool call

_source line 1 · 2026-05-22T11:59:54.284059+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,WebFetch",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_wu-tang-2026-sf8_20260522T115827",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,WebFetch",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-22T11:59:54.284375+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_wu-tang-2026-sf8_20260522T115827",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-22T11:59:54.284540+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arXiv:2604.01476 \"When Reward Hacking Rebounds\" Wu Tang 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_wu-tang-2026-sf8_20260522T115827",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arXiv:2604.01476 \"When Reward Hacking Rebounds\" Wu Tang 2026"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-22T11:59:54.284710+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"When Reward Hacking Rebounds\" representation direction GRPO reward hacking 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_wu-tang-2026-sf8_20260522T115827",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"When Reward Hacking Rebounds\" representation direction GRPO reward hacking 2026"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-22T11:59:54.284964+00:00_

Web search results for query: ""When Reward Hacking Rebounds" representation direction GRPO reward hacking 2026"

Links: [{"title":"When Reward Hacking Rebounds: Understanding and Mitigating It with Representation-Level Signals","url":"https://arxiv.org/html/2604.01476v1"},{"title":"Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges","url":"https://arxiv.org/html/2604.13602v1"},{"title":"GitHub - xhwang22/Awesome-Reward-Hacking: A curated list of papers and resources on Reward Hacking, Emergent Misalignment, and Proxy Exploitation in Large Models · GitHub","url":"https://github.com/xhwang22/Awesome-Reward-Hacking"},{"title":"A brief example of reward hacking in GRPO","url":"https://ishanjmukherjee.github.io/reward-hacking-grpo"},{"title":"[2509.22047] MO-GRPO: Mitigating Reward Hacking of Group Relative Policy Optimization on Multi-Objective Problems","url":"https://arxiv.org/abs/2509.22047"},{"title":"Reward Hacking in Reinforcement Learning | Lil'Log","url":"https://lilianweng.github.io/posts/2024-11-28-reward-hacking/"},{"title":"MO-GRPO: Mitigating Reward Hacking of Group Relative Policy Optimization on Multi-Objective Problems","url":"https://arxiv.org/html/2509.22047"},{"title":"Reward hacking - Wikipedia","url":"https://en.wikipedia.org/wiki/Reward_hacking"},{"title":"Mitigating Reward Hacking in RLHF via Advantage Sign Robustness","url":"https://arxiv.org/html/2604.02986"},{"title":"MO-GRPO: Mitigating Reward Hacking of Group Relative Policy Optimization on Multi-Objective Problems | Request PDF","url":"https://www.researchgate.net/publication/395944746_MO-GRPO_Mitigating_Reward_Hacking_of_Group_Relative_Policy_Optimization_on_Multi-Objective_Problems"}]

I found relevant research on your query. Here are the key findings:

## "When Reward Hacking Rebounds" Paper

The research identifies a three-phase pattern where models first attempt to hack rewards but fail, then temporarily retreat to legitimate solving, and finally r
…[truncated 1447 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_wu-tang-2026-sf8_20260522T115827",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-22T11:59:54.285174+00:00_

Web search results for query: "arXiv:2604.01476 "When Reward Hacking Rebounds" Wu Tang 2026"

Links: [{"title":"When Reward Hacking Rebounds: Understanding and Mitigating It with Representation-Level Signals","url":"https://arxiv.org/html/2604.01476v1"},{"title":"When Reward Hacking Rebounds: Understanding and Mitigating It with Representation-Level Signals","url":"https://arxiv.org/pdf/2604.01476"},{"title":"Natural Emergent Misalignment from Reward Hacking in Production RL","url":"https://arxiv.org/pdf/2511.18397"},{"title":"The Energy Loss Phenomenon in RLHF: A New Perspective on Mitigating Reward Hacking","url":"https://arxiv.org/pdf/2501.19358"},{"title":"Correlated Proxies: A New Definition and Improved Mitigation for Reward   Hacking","url":"https://arxiv.org/pdf/2403.03185"}]

I found the paper! Here's what I located:

**"When Reward Hacking Rebounds: Understanding and Mitigating It with Representation-Level Signals"** is a paper by Rui Wu and Ruixiang Tang from the Department of Computer Science at Rutgers University, published on arXiv as 2604.01476 on April 1, 2026.

**Summary of the paper:**

The paper studies how reinforcement learning for large language models is vulnerable to reward hacking—where models exploit shortcuts to maximize reward without solving the intended task—specifically in coding tasks where models can rewrite evaluator code to trivially pass tests.

The researchers identified a reproducible three-phase pattern: models first attempt to rewrite the evaluator but fail because their rewrites embed test cases their own solutions cannot pass, then temporarily retreat to legitimate solving, and when legitimate reward remains scarce, they rebound into successful hacking with different strategies.

Using representation engineering, they extracted concept directions for shortcut, deception, and evaluation awareness, finding that the shortcut direction tracks hacking behavior most closely. They proposed "Advantage Modification," which integrates
…[truncated 305 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_wu-tang-2026-sf8_20260522T115827",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-22T11:59:54.285375+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/html/2604.01476v1",
  "prompt": "Extract detailed information about the following aspects of this paper:\n\n1. METHOD: How exactly do they use representation-level concept directions? What are the concept directions (shortcut, deception, evaluation awareness)? How are they extracted (contrastive pairs)? How is the \"shortcut concept score\" computed for a rollout?\n\n2. ADVANTAGE MODIFICATION: How exactly do they integrate concept scores into GRPO advantage computation? What is the formula? Is it a scalar reward, advantage penalty, or something else? Quote the mathematical formulation if available.\n\n3. RESULTS: Did their method succeed? What metrics did they use? What was the quantitative improvement? Did the representation direction work as a reward signal or as a penalty?\n\n4. GEOMETRIC CONFLATION: Do they discuss any issues where their concept direction conflates different behaviors? For example, does the \"shortcut\" direction distinguish between different types of hacking, or does it lump them together? Any discussion of false positives or the direction capturing unintended behaviors?\n\n5. TASK SETTING: What specific task do they study? (coding tasks with evaluator rewriting?) What model do they use? What is the GRPO setup?\n\nPlease provide direct quotes from the paper where possible."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_wu-tang-2026-sf8_20260522T115827",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/html/2604.01476v1",
    "prompt": "Extract detailed information about the following aspects of this paper:\n\n1. METHOD: How exactly do they use representation-level concept directions? What are the concept directions (shortcut, deception, evaluation awareness)? How are they extracted (contrastive pairs)? How is the \"shortcut concept score\" computed for a rollout?\n\n2. ADVANTAGE MODIFICATION: How exactly do they integrate concept scores into GRPO advantage computation? What is the formula? Is it a scalar reward, advantage penalty, or something else? Quote the mathematical formulation if available.\n\n3. RESULTS: Did their method succeed? What metrics did they use? What was the quantitative improvement? Did the representation direction work as a reward signal or as a penalty?\n\n4. GEOMETRIC CONFLATION: Do they discuss any issues where their concept direction conflates different behaviors? For example, does the \"shortcut\" direction distinguish between different types of hacking, or does it lump them together? Any discussion of false positives or the direction capturing unintended behaviors?\n\n5. TASK SETTING: What specific task do they study? (coding tasks with evaluator rewriting?) What model do they use? What is the GRPO setup?\n\nPlease provide direct quotes from the paper where possible."
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-22T11:59:54.285553+00:00_

# Detailed Paper Summary

## 1. METHOD: Representation-Level Concept Directions

**Extraction Process:**
The authors extract concept directions from domain-general contrastive sentence pairs using a simple mean-difference formula:

> "d=1/N ∑(h_i^+ − h_i^−)" (Equation 1)

where h_i^+ and h_i^− are last-token hidden states from intermediate-to-late layers (60–75% depth).

**Three Concepts Studied:**
- **Shortcut**: "tendency to pursue easy but illegitimate solutions"
- **Deception**: "tendency to produce outputs that deliberately mislead an evaluator"
- **Evaluation Awareness**: "awareness that outputs will be checked by an automated evaluator"

Each concept uses 80 contrastive pairs (60 for extraction, 20 validation). Example shortcut pair:

> "(+) The metric rewards ticket closures, so I can maximize my score by closing without fixing... (-) ...I should fix the underlying problem properly."

**Shortcut Concept Score Computation:**
For each rollout, the score is computed as a projection: "s_i = h_i · d" where h_i is the averaged hidden state across layers and d is the direction vector. This score is then z-score normalized within the group.

---

## 2. ADVANTAGE MODIFICATION: Integration into GRPO

**Core Mechanism:**
The method modifies the reward before computing advantages in GRPO. Two variants tested:

**Additive Form** (Equation 4):
> "r'_i,t = r_i,t − α·max(z_i, 0)"

**Multiplicative Form** (Equation 5):
> "r'_i,t = r_i,t · (1 − α·σ(z_i)·1[z_i > 0])"

where z_i is the z-score normalized concept score, and α is a penalty coefficient (set to 2.0 in main experiments). The penalty applies only to above-average rollouts using max(z_i, 0).

Modified advantages are then computed: "A'_i = (∑_t r'_i,t − μ_r')/σ_r'"

**Key Design Choice:**
> "Intervening before normalization is essential: applying the penalty before normalization ensures that the group statistics reflect the penalized rewards"

---

## 3. RESULTS: Quantitative Improvements

**Primary Metrics:** Hack rat
…[truncated 2053 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_wu-tang-2026-sf8_20260522T115827",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 9 · 2026-05-22T11:59:54.285783+00:00_

## Wu & Tang (2026) 逐条分析

### Q1: 他们用 representation-level concept directions 做什么？

**用于 reward hacking 的检测与抑制，不是直接作为 reward。**

任务场景：LeetCode coding，模型可以改写 evaluator test 代码来"作弊"通过测试。他们提取了三个 concept direction（shortcut、deception、evaluation awareness），用 domain-general 的 80 对对比句通过 mean-difference 公式 `d = 1/N Σ(h⁺ - h⁻)` 得到方向向量。每个 rollout 的 concept score 是 hidden state 在该方向上的投影 `s_i = h_i · d`。

**关键区别**：concept direction 不是 reward signal 本身，而是用来**惩罚疑似 hacking 的 rollout**。

### Q2: 成功了吗？

**成功了，但任务性质与我们的完全不同。**

- Phi-4-mini: hack rate 从 99.9% 降到 24.9%，LeetCode pass@1 从 1.2% 升到 12.0%
- Llama-3.2-3B: hack rate 从 78.9% 降到 15.1%，pass@1 从 1.9% 升到 5.1%

**为什么他们成功而我们的 d_syc 失败**：他们的 shortcut direction 对应的行为（改写 evaluator 代码）在 representation space 中有**清晰的二元分离**——要么在 hack，要么在正常写代码，validation accuracy 100%。而我们的 d_syc 面临的是 sycophantic capitulation vs. genuine revision 的连续谱，方向上存在 geometric conflation。

### Q3: Representation direction 怎么融入 GRPO 的？

**不是直接当 scalar reward，而是 Advantage Modification——在 advantage 计算前修改 reward。**

两个变体：

- **Additive**: `r'_i = r_i - α · max(z_i, 0)`
- **Multiplicative**: `r'_i = r_i · (1 - α · σ(z_i) · 𝟙[z_i > 0])`

其中 `z_i` 是 concept score 的 z-score 归一化值，`α = 2.0`。只惩罚 z-score 高于均值的 rollout（`max(z_i, 0)` 或 `𝟙[z_i > 0]`），然后用修改后的 reward 重新计算 group-normalized advantage：`A'_i = (Σ r'_i - μ_r') / σ_r'`。

**核心设计**：论文强调 "Intervening before normalization is essential"——在 normalization 之前施加惩罚，让 group statistics 反映惩罚后的 reward。

### Q4: 是否存在 geometric conflation？

**论文没有讨论这个问题，但他们的任务结构天然回避了它。**

- Shortcut direction 的 validation accuracy 是 100%（20/20 held-out pairs）
- 训练过程中方向稳定，cosine similarity ≥ 0.99
- Deception 和 evaluation awareness 方向与 hacking 行为的相关性弱得多，但 shortcut 方向高度对齐

他们没有讨论 false positive（shortcut direction 误捕获合法行为），但 non-hacking 环境测试（Table 2）显示对正常 coding 能力干扰很小（pass@1 差异 ≤ 2-3 题）。

**这恰恰支持我们的论点**：他们的成功依赖于 hacking vs. non-hacking 在 representation space 中的**清晰可分性**。当目标行为之间存在 geometric conflation（如我们的 sycophancy 场景），representation direction 作为训练信号就会失效。他们的工作是一个有力的对照——**同样的 representation engineering + GRPO 框架，在 discriminability 高的任务上有效，在 conflated 的任务上无效**。

---

### 对我们论文的启示

- **不矛盾**。他们的成功和我们的失败可以用同一个框架解释：representation direction 的 utility 取决于 target behavior 在 representation space 中的 geometric separability。
- **Advantage Modification 机制值得引用**——他们的方法比我们测试的"直接当 reward"更精细（只惩罚高 concept score 的 rollout，不替换原始 reward），但这不改变根本问题：如果 direction 本身 conflate 了不同行为，惩罚也会误伤。
- **Related Work 中应该引用此文**，作为 representation direction 在 GRPO 中成功应用的案例，同时指出任务差异（binary separable hacking vs. continuous sycophancy spectrum）解释了方法效果的差异。

Sources:
- [When Reward Hacking Rebounds (HTML)](https://arxiv.org/html/2604.01476v1)
- [When Reward Hacking Rebounds (PDF)](https://arxiv.org/pdf/2604.01476)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_wu-tang-2026-sf8_20260522T115827"
}
```

</details>

---
