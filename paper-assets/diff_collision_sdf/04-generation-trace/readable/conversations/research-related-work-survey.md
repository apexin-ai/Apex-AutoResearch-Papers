# research related work survey

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 165
- **Recorded user turns:** 0
- **Tool calls:** 82
- **Original source:** `logs/chats/worker_research_related_work_survey_20260523T030015.jsonl`
- **Structured JSON:** [`9c6c4d36287e5e0febf3.json`](../../sessions/9c/9c6c4d36287e5e0febf3.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

165 recorded events

### Tool call

_source line 1 · 2026-05-23T03:06:17.586387+00:00_

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
  "session": "worker_research_related_work_survey_20260523T030015",
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

_source line 2 · 2026-05-23T03:06:17.586722+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-23T03:06:17.586919+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Survey: VLA safety/collision",
  "subagent_type": "general-purpose",
  "prompt": "You are conducting a literature survey on \"VLA safety / collision avoidance\" for a robotics research project. The project uses Pi0.5 + A1 SDF auxiliary loss for collision avoidance in VLA models.\n\nSearch for 3-5 core papers (2023-2026 preferred) using these keyword combinations. Do at least 3 separate WebSearch calls with different queries:\n\n1. \"vision language action model collision avoidance\"\n2. \"VLA safety robot manipulation\"\n3. \"pi0 safety\" OR \"RT-2 collision\" OR \"Octo safe manipulation\" OR \"OpenVLA safety\"\n4. \"safe robot policy learning vision language\"\n\nFor each paper found, extract:\n- Full title\n- Authors (first author + et al. is fine)\n- Venue and year\n- Core method (1-2 sentences)\n- Key results\n- URL (arXiv or paper link)\n- Relation to a project that adds SDF-based auxiliary loss to Pi0.5 VLA for collision avoidance: is it a competitor, a technique to borrow, or a complementary perspective?\n\nIf this direction has few direct results, note it as a \"novelty gap\". Do NOT invent papers. Only report papers you actually found with real URLs.\n\nOutput your findings as a structured markdown list."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "Agent",
  "tool_args": {
    "description": "Survey: VLA safety/collision",
    "subagent_type": "general-purpose",
    "prompt": "You are conducting a literature survey on \"VLA safety / collision avoidance\" for a robotics research project. The project uses Pi0.5 + A1 SDF auxiliary loss for collision avoidance in VLA models.\n\nSearch for 3-5 core papers (2023-2026 preferred) using these keyword combinations. Do at least 3 separate WebSearch calls with different queries:\n\n1. \"vision language action model collision avoidance\"\n2. \"VLA safety robot manipulation\"\n3. \"pi0 safety\" OR \"RT-2 collision\" OR \"Octo safe manipulation\" OR \"OpenVLA safety\"\n4. \"safe robot policy learning vision language\"\n\nFor each paper found, extract:\n- Full title\n- Authors (first author + et al. is fine)\n- Venue and year\n- Core method (1-2 sentences)\n- Key results\n- URL (arXiv or paper link)\n- Relation to a project that adds SDF-based auxiliary loss to Pi0.5 VLA for collision avoidance: is it a competitor, a technique to borrow, or a complementary perspective?\n\nIf this direction has few direct results, note it as a \"novelty gap\". Do NOT invent papers. Only report papers you actually found with real URLs.\n\nOutput your findings as a structured markdown list."
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-23T03:06:17.587098+00:00_

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
  "session": "worker_research_related_work_survey_20260523T030015",
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

_source line 5 · 2026-05-23T03:06:17.587228+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-23T03:06:17.587362+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "vision language action model collision avoidance robot manipulation 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "tool_args": {
    "query": "vision language action model collision avoidance robot manipulation 2024 2025"
  }
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-23T03:06:17.587514+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Survey: fake safety/action collapse",
  "subagent_type": "general-purpose",
  "prompt": "You are conducting a literature survey on \"Fake safety / action collapse in robotics\" for a research project. The project defines a \"frozen_rate\" metric to detect robots that appear safe only because they stop moving.\n\nSearch for 3-5 core papers (2023-2026 preferred) using these keyword combinations. Do at least 3 separate WebSearch calls with different queries:\n\n1. \"robot action collapse safety\"\n2. \"frozen robot safety metric\" OR \"degenerate safe policy robotics\"\n3. \"robot inaction safety reward hacking\" OR \"conservative policy collapse robot\"\n4. \"action mode collapse imitation learning robot\"\n\nFor each paper found, extract:\n- Full title\n- Authors\n- Venue and year\n- Core method (1-2 sentences)\n- Key results\n- URL\n- Relation to the frozen_rate metric concept (detecting robots that are \"safe\" only because they don't move)\n\nIf this direction has few direct results, note it as a \"novelty gap\" and mention any tangentially related work. Do NOT invent papers.\n\nOutput your findings as a structured markdown list."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "Agent",
  "tool_args": {
    "description": "Survey: fake safety/action collapse",
    "subagent_type": "general-purpose",
    "prompt": "You are conducting a literature survey on \"Fake safety / action collapse in robotics\" for a research project. The project defines a \"frozen_rate\" metric to detect robots that appear safe only because they stop moving.\n\nSearch for 3-5 core papers (2023-2026 preferred) using these keyword combinations. Do at least 3 separate WebSearch calls with different queries:\n\n1. \"robot action collapse safety\"\n2. \"frozen robot safety metric\" OR \"degenerate safe policy robotics\"\n3. \"robot inaction safety reward hacking\" OR \"conservative policy collapse robot\"\n4. \"action mode collapse imitation learning robot\"\n\nFor each paper found, extract:\n- Full title\n- Authors\n- Venue and year\n- Core method (1-2 sentences)\n- Key results\n- URL\n- Relation to the frozen_rate metric concept (detecting robots that are \"safe\" only because they don't move)\n\nIf this direction has few direct results, note it as a \"novelty gap\" and mention any tangentially related work. Do NOT invent papers.\n\nOutput your findings as a structured markdown list."
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-23T03:06:17.587700+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "VLA safety robot manipulation safe policy learning 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "tool_args": {
    "query": "VLA safety robot manipulation safe policy learning 2024 2025"
  }
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-23T03:06:17.587836+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "pi0 safety OR \"RT-2 collision\" OR \"Octo safe manipulation\" OR \"OpenVLA safety\" robot"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "tool_args": {
    "query": "pi0 safety OR \"RT-2 collision\" OR \"Octo safe manipulation\" OR \"OpenVLA safety\" robot"
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-23T03:06:17.587958+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "safe robot policy learning vision language model constraint 2024 2025 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "tool_args": {
    "query": "safe robot policy learning vision language model constraint 2024 2025 arXiv"
  }
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-23T03:06:17.588072+00:00_

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
  "session": "worker_research_related_work_survey_20260523T030015",
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

_source line 12 · 2026-05-23T03:06:17.588187+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-23T03:06:17.588306+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Survey: SDF in manipulation",
  "subagent_type": "general-purpose",
  "prompt": "You are conducting a literature survey on \"SDF (Signed Distance Field) in robot manipulation\" for a research project that uses SDF-based auxiliary loss in a VLA model for collision avoidance.\n\nSearch for 3-5 core papers (2023-2026 preferred) using these keyword combinations. Do at least 3 separate WebSearch calls with different queries:\n\n1. \"signed distance field robot manipulation obstacle avoidance\"\n2. \"SDF collision avoidance robotic arm\"\n3. \"distance field motion planning manipulation\"\n4. \"neural SDF robot safety\"\n\nInclude both VLA-based and traditional planning methods that use SDF for obstacle avoidance.\n\nFor each paper found, extract:\n- Full title\n- Authors\n- Venue and year\n- Core method (1-2 sentences)\n- Key results\n- URL\n- Relation to the project (Pi0.5 VLA + SDF auxiliary loss for collision avoidance): competitor, borrowable technique, or complementary?\n\nDo NOT invent papers. Only report papers you actually found with real URLs.\n\nOutput your findings as a structured markdown list."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "Agent",
  "tool_args": {
    "description": "Survey: SDF in manipulation",
    "subagent_type": "general-purpose",
    "prompt": "You are conducting a literature survey on \"SDF (Signed Distance Field) in robot manipulation\" for a research project that uses SDF-based auxiliary loss in a VLA model for collision avoidance.\n\nSearch for 3-5 core papers (2023-2026 preferred) using these keyword combinations. Do at least 3 separate WebSearch calls with different queries:\n\n1. \"signed distance field robot manipulation obstacle avoidance\"\n2. \"SDF collision avoidance robotic arm\"\n3. \"distance field motion planning manipulation\"\n4. \"neural SDF robot safety\"\n\nInclude both VLA-based and traditional planning methods that use SDF for obstacle avoidance.\n\nFor each paper found, extract:\n- Full title\n- Authors\n- Venue and year\n- Core method (1-2 sentences)\n- Key results\n- URL\n- Relation to the project (Pi0.5 VLA + SDF auxiliary loss for collision avoidance): competitor, borrowable technique, or complementary?\n\nDo NOT invent papers. Only report papers you actually found with real URLs.\n\nOutput your findings as a structured markdown list."
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-23T03:06:17.588510+00:00_

Web search results for query: "VLA safety robot manipulation safe policy learning 2024 2025"

Links: [{"title":"SafeVLA: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning","url":"https://papers.nips.cc/paper_files/paper/2025/hash/e185c7be603426028c32ae1003a59d78-Abstract-Conference.html"},{"title":"[2503.03480] SafeVLA: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning","url":"https://arxiv.org/abs/2503.03480"},{"title":"SafeVLA: Towards Safety Alignment of Vision- Language-Action Model via Constrained Learning","url":"https://arxiv.org/html/2503.03480v4"},{"title":"SafeVLA: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning | OpenReview","url":"https://openreview.net/forum?id=dt940loCBT"},{"title":"SafeVLA: Towards Safety Alignment of Vision-Language-Action Model via Safe Reinforcement Learning","url":"https://arxiv.org/html/2503.03480v1"},{"title":"SafeVLA: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning","url":"https://safevla.github.io/"},{"title":"Vision Language Action Models (VLA) & Policies for Robots","url":"https://learnopencv.com/vision-language-action-models-lerobot-policy/"},{"title":"NeurIPS Poster SafeVLA: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning","url":"https://neurips.cc/virtual/2025/poster/116975"},{"title":"Safe-Night VLA: Seeing the Unseen via Thermal-Perceptive Vision-Language-Action Models for Safety-Critical Manipulation","url":"https://arxiv.org/pdf/2603.05754"}]

Based on the web search results, here's what I found regarding VLA safety, robot manipulation, and safe policy learning in 2024-2025:

## SafeVLA: Safety Alignment for Vision-Language-Action Models

The most prominent recent research is **SafeVLA**, a framework addressing how Vision-Language-Action models (VLAs) show potential as generalist robot policies but pose extreme safety challenges during real-world deployme
…[truncated 1366 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-23T03:06:17.588671+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "robot action collapse safety reinforcement learning 2023 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "tool_args": {
    "query": "robot action collapse safety reinforcement learning 2023 2024 2025"
  }
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-23T03:06:17.588794+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "frozen robot safety metric OR degenerate safe policy robotics 2023 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "tool_args": {
    "query": "frozen robot safety metric OR degenerate safe policy robotics 2023 2024 2025"
  }
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-23T03:06:17.588909+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "robot inaction safety reward hacking OR conservative policy collapse robot 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "tool_args": {
    "query": "robot inaction safety reward hacking OR conservative policy collapse robot 2024 2025"
  }
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-23T03:06:17.589023+00:00_

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
  "session": "worker_research_related_work_survey_20260523T030015",
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

_source line 19 · 2026-05-23T03:06:17.589134+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-23T03:06:17.589250+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Survey: safety metrics/benchmarks",
  "subagent_type": "general-purpose",
  "prompt": "You are conducting a literature survey on \"Safety metrics for robot learning\" for a research project. The project evaluates collision avoidance in VLA models using metrics like collision_rate and frozen_rate.\n\nSearch for 3-5 core papers (2023-2026 preferred) using these keyword combinations. Do at least 3 separate WebSearch calls with different queries:\n\n1. \"safety benchmark robot learning\"\n2. \"SafeLIBERO\" OR \"safe reinforcement learning benchmark manipulation\"\n3. \"collision rate metric robot evaluation\"\n4. \"safety constraint robot policy evaluation\"\n\nFor each paper found, extract:\n- Full title\n- Authors\n- Venue and year\n- Core method (1-2 sentences)\n- Key results\n- URL\n- Relation to the project's safety evaluation approach\n\nDo NOT invent papers. Only report papers you actually found with real URLs.\n\nOutput your findings as a structured markdown list."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "Agent",
  "tool_args": {
    "description": "Survey: safety metrics/benchmarks",
    "subagent_type": "general-purpose",
    "prompt": "You are conducting a literature survey on \"Safety metrics for robot learning\" for a research project. The project evaluates collision avoidance in VLA models using metrics like collision_rate and frozen_rate.\n\nSearch for 3-5 core papers (2023-2026 preferred) using these keyword combinations. Do at least 3 separate WebSearch calls with different queries:\n\n1. \"safety benchmark robot learning\"\n2. \"SafeLIBERO\" OR \"safe reinforcement learning benchmark manipulation\"\n3. \"collision rate metric robot evaluation\"\n4. \"safety constraint robot policy evaluation\"\n\nFor each paper found, extract:\n- Full title\n- Authors\n- Venue and year\n- Core method (1-2 sentences)\n- Key results\n- URL\n- Relation to the project's safety evaluation approach\n\nDo NOT invent papers. Only report papers you actually found with real URLs.\n\nOutput your findings as a structured markdown list."
  }
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-23T03:06:17.589403+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "action mode collapse imitation learning robot 2023 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "tool_args": {
    "query": "action mode collapse imitation learning robot 2023 2024 2025"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-23T03:06:17.589587+00:00_

Web search results for query: "vision language action model collision avoidance robot manipulation 2024 2025"

Links: [{"title":"Vision Language Action Models in Robotic Manipulation: A Systematic Review","url":"https://arxiv.org/html/2507.10672v1"},{"title":"Vision-Language-Action (VLA) Models: Concepts, Progress, Applications and Challenges","url":"https://arxiv.org/html/2505.04769v2"},{"title":"Vision-Language-Action Models: Concepts, Progress, Applications and Challenges","url":"https://arxiv.org/html/2505.04769v1"},{"title":"CoFreeVLA: Collision-Free Dual-Arm Manipulation via Vision-Language-Action Model and Risk Estimation","url":"https://arxiv.org/pdf/2601.21712"},{"title":"GitHub - jonyzhang2023/awesome-embodied-vla-va-vln: A curated list of state-of-the-art research in embodied AI, focusing on vision-language-action (VLA) models, vision-language navigation (VLN), and related multimodal learning approaches. · GitHub","url":"https://github.com/jonyzhang2023/awesome-embodied-vla-va-vln"},{"title":"1 Recipe for Vision-Language-Action Models in Robotic Manipulation: A Survey","url":"https://www.techrxiv.org/users/956965/articles/1326137/master/file/data/eart2025recipevla/eart2025recipevla.pdf?inline=true"},{"title":"Vision-language-action model","url":"https://en.wikipedia.org/wiki/Vision-language-action_model"}]

The search has returned comprehensive results on vision-language-action models for robot manipulation with collision avoidance. Here's a summary of the key findings:

## Recent Developments in VLA Models (2024-2025)

**Major Model Releases:**

Industrial-scale models such as GR00T N1 and π0 have emerged during the maturation phase (2024 Q4–present). In benchmark tests on multi-stage household manipulation, GR00T N1 outperformed monolithic models such as RT-1, RT-2, and OpenVLA by 17% in success rate and reduced collision failures by 28%.

π0 (pi-zero) is a large-scale generalist VLA announced in late 2024 by Physical Intelligence, trained on robot traj
…[truncated 1121 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-23T03:06:17.589790+00:00_

Web search results for query: "pi0 safety OR "RT-2 collision" OR "Octo safe manipulation" OR "OpenVLA safety" robot"

Links: [{"title":"VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer","url":"https://arxiv.org/html/2512.11891v1"},{"title":"Bridging Embodiment Gaps: Deploying Vision-Language-Action Models on Soft Robots","url":"https://arxiv.org/html/2510.17369v1"},{"title":"We introduce Octo, an open-source, generalist policy for robotic... | Download Scientific Diagram","url":"https://www.researchgate.net/figure/We-introduce-Octo-an-open-source-generalist-policy-for-robotic-manipulation-Octo-is-a_fig1_380730391"},{"title":"SAFE: Multitask Failure Detection for Vision-Language-Action Models","url":"https://arxiv.org/pdf/2506.09937"},{"title":"Physical Intelligence Unveils Robotics Foundation Model Pi-Zero - InfoQ","url":"https://www.infoq.com/news/2024/12/pi-zero-robot/"},{"title":"Bridging Embodiment Gaps: Deploying Vision-Language-Action Models on Soft Robots","url":"https://arxiv.org/pdf/2510.17369"},{"title":"Evaluating \\( \\pi_0 \\) in the Wild: Strengths, Problems, and the Future of Generalist Robot Policies","url":"https://penn-pal-lab.github.io/Pi0-Experiment-in-the-Wild/"},{"title":"CompliantVLA-adaptor: VLM-Guided Variable Impedance Action for Safe Contact-Rich Manipulation","url":"https://arxiv.org/pdf/2601.15541"},{"title":"OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://arxiv.org/pdf/2406.09246"}]

I've performed the web search for your query. Here are the key findings:

## Vision-Language-Action Models and Safety

The search results cover several robotics foundation models and their safety considerations:

**Pi0 Safety Concerns:**
The pi0 robot has no safety constraints and will sometimes accidentally hit or grasp a user's hand, which could hurt the user.

**Comparative Performance:**
In collision avoidance tests, AEGIS achieved 68.13% average task success rate, outperforming π₀.₅ (50.88%) and OpenVL
…[truncated 953 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-23T03:06:17.589945+00:00_

Web search results for query: "safe robot policy learning vision language model constraint 2024 2025 arXiv"

Links: [{"title":"SafeVLA: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning | OpenReview","url":"https://openreview.net/forum?id=dt940loCBT"},{"title":"SafeVLA: Towards Safety Alignment of Vision-Language-Action Model via Safe Reinforcement Learning","url":"https://arxiv.org/html/2503.03480v1"},{"title":"NeurIPS Poster SafeVLA: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning","url":"https://neurips.cc/virtual/2025/poster/116975"},{"title":"LangForce: Bayesian Decomposition of Vision Language ...","url":"https://arxiv.org/pdf/2601.15197"},{"title":"SafeVLA: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning","url":"https://safevla.github.io/"},{"title":"VLM-SAFE: Vision-Language Model-Guided Safety-Aware Reinforcement Learning with World Models for Autonomous Driving","url":"https://arxiv.org/pdf/2505.16377"},{"title":"Learning Structured Robot Policies from Vision-Language Models via Synthetic Neuro-Symbolic Supervision","url":"https://arxiv.org/pdf/2604.02812"},{"title":"Safe Reinforcement Learning with Free-form Natural Language Constraints   and Pre-Trained Language Models","url":"https://arxiv.org/pdf/2401.07553"}]

I found several relevant research papers on safe robot policy learning with vision-language models. Here are the key results:

## SafeVLA: Main Result

The most prominent work is "SafeVLA: Towards Safety Alignment of Vision-Language-Action Model," which explores an integrated safety approach (ISA) that systematically models safety requirements, actively elicits diverse unsafe behaviors, effectively constrains VLA policies via safe reinforcement learning, and rigorously assures their safety through targeted evaluations. This approach achieves an 83.58% improvement in safety with no performance loss.

The approach leverages the constrained Markov de
…[truncated 879 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-23T03:06:17.590098+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "signed distance field robot manipulation obstacle avoidance 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "tool_args": {
    "query": "signed distance field robot manipulation obstacle avoidance 2024 2025"
  }
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-23T03:06:17.590218+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "SDF collision avoidance robotic arm motion planning 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "tool_args": {
    "query": "SDF collision avoidance robotic arm motion planning 2024 2025"
  }
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-23T03:06:17.590334+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "neural signed distance field robot safety manipulation 2023 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "tool_args": {
    "query": "neural signed distance field robot safety manipulation 2023 2024 2025"
  }
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-23T03:06:17.590466+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "distance field motion planning manipulation collision checking 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "tool_args": {
    "query": "distance field motion planning manipulation collision checking 2024"
  }
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-23T03:06:17.590585+00:00_

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
  "session": "worker_research_related_work_survey_20260523T030015",
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

_source line 30 · 2026-05-23T03:06:17.590695+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-23T03:06:17.590824+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Survey: auxiliary loss for safety",
  "subagent_type": "general-purpose",
  "prompt": "You are conducting a literature survey on \"Auxiliary loss for safety\" in robot learning. The project uses an SDF-based auxiliary loss added to a VLA model (Pi0.5) to guide collision avoidance behavior during imitation learning.\n\nSearch for 3-5 core papers (2023-2026 preferred) using these keyword combinations. Do at least 3 separate WebSearch calls with different queries:\n\n1. \"auxiliary loss safe reinforcement learning\"\n2. \"auxiliary objective safety constraint imitation learning\"\n3. \"multi-task safety loss robot learning\"\n4. \"safety reward shaping auxiliary\"\n5. \"auxiliary task robot policy learning\"\n\nFor each paper found, extract:\n- Full title\n- Authors\n- Venue and year\n- Core method (1-2 sentences)\n- Key results\n- URL\n- Relation to the project (using auxiliary SDF loss in VLA imitation learning for safety): competitor, borrowable technique, or complementary?\n\nDo NOT invent papers. Only report papers you actually found with real URLs.\n\nOutput your findings as a structured markdown list."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "Agent",
  "tool_args": {
    "description": "Survey: auxiliary loss for safety",
    "subagent_type": "general-purpose",
    "prompt": "You are conducting a literature survey on \"Auxiliary loss for safety\" in robot learning. The project uses an SDF-based auxiliary loss added to a VLA model (Pi0.5) to guide collision avoidance behavior during imitation learning.\n\nSearch for 3-5 core papers (2023-2026 preferred) using these keyword combinations. Do at least 3 separate WebSearch calls with different queries:\n\n1. \"auxiliary loss safe reinforcement learning\"\n2. \"auxiliary objective safety constraint imitation learning\"\n3. \"multi-task safety loss robot learning\"\n4. \"safety reward shaping auxiliary\"\n5. \"auxiliary task robot policy learning\"\n\nFor each paper found, extract:\n- Full title\n- Authors\n- Venue and year\n- Core method (1-2 sentences)\n- Key results\n- URL\n- Relation to the project (using auxiliary SDF loss in VLA imitation learning for safety): competitor, borrowable technique, or complementary?\n\nDo NOT invent papers. Only report papers you actually found with real URLs.\n\nOutput your findings as a structured markdown list."
  }
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-23T03:06:17.591026+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CoFreeVLA collision-free dual-arm manipulation VLA risk estimation arXiv 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CoFreeVLA collision-free dual-arm manipulation VLA risk estimation arXiv 2025"
  }
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-23T03:06:17.591157+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "safety benchmark robot learning 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "tool_args": {
    "query": "safety benchmark robot learning 2024 2025"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-23T03:06:17.591281+00:00_

Web search results for query: "robot action collapse safety reinforcement learning 2023 2024 2025"

Links: [{"title":"Safe Reinforcement Learning of Robot Trajectories in the Presence of Moving Obstacles","url":"https://arxiv.org/html/2411.05784v1"},{"title":"Robot Navigation with Entity-Based Collision Avoidance using Deep Reinforcement Learning","url":"https://arxiv.org/pdf/2408.14183"},{"title":"Risk-Aware Reinforcement Learning with Dynamic Safety Filter for Collision Risk Mitigation in Mobile Robot Navigation","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12431337/"},{"title":"Safe Learning in Robotics: From Learning-Based Control to Safe   Reinforcement Learning","url":"https://arxiv.org/pdf/2108.06266"},{"title":"Safe Reinforcement Learning of Robot Trajectories in the Presence of   Moving Obstacles","url":"https://arxiv.org/pdf/2411.05784"},{"title":"Uncertainty-Aware Reinforcement Learning for Collision Avoidance","url":"https://arxiv.org/pdf/1702.01182"},{"title":"Provably Safe Reinforcement Learning via Action Projection using   Reachability Analysis and Polynomial Zonotopes","url":"https://arxiv.org/pdf/2210.10691"}]

I've completed the web search for "robot action collapse safety reinforcement learning 2023 2024 2025". Here are the key research findings:

## Recent Research on Safe Robot Reinforcement Learning

**2024-2025 Work:**

Recent approaches focus on learning collision-free robot trajectories in the presence of moving obstacles, training backup policies to generate evasive movements using model-free reinforcement learning. 

A notable 2025 approach combines proximal policy optimization with control barrier functions, generating exploratory actions using PPO and constructing real-time safety filters to minimize risky actions. This method achieved an obstacle avoidance success rate of nearly 90% in complex, dynamic, multi-obstacle environments.

**Key Safety Challenges:**

A major challenge is ensuring selected robot actions don't cause dama
…[truncated 827 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-23T03:06:17.591454+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "VLSA plug-and-play safety constraint layer vision language action arXiv 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "tool_args": {
    "query": "VLSA plug-and-play safety constraint layer vision language action arXiv 2024"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-23T03:06:17.591604+00:00_

Web search results for query: "frozen robot safety metric OR degenerate safe policy robotics 2023 2024 2025"

Links: [{"title":"Certifiably-correct Control Policies for Safe Learning and Adaptation in   Assistive Robotics","url":"https://arxiv.org/pdf/2303.06582"},{"title":"Learning Robot Safety from Sparse Human Feedback using Conformal   Prediction","url":"https://arxiv.org/pdf/2501.04823"},{"title":"Probabilistically Safe Policy Transfer","url":"https://arxiv.org/pdf/1705.05394"},{"title":"Robots that Suggest Safe Alternatives","url":"https://arxiv.org/pdf/2409.09883"},{"title":"Provably Safe Robot Navigation with Obstacle Uncertainty","url":"https://arxiv.org/pdf/1705.10907"},{"title":"Robot Safety Resources from A3 Robotics","url":"https://www.automate.org/robotics/safety/robot-safety-resources"}]

Based on the search results, I found several relevant papers on robot safety, though the specific terms "frozen robot safety metric" and "degenerate safe policy" don't appear prominently in these results. Here are the most relevant findings:

**Recent Robot Safety Research (2023-2025):**

A 2025 paper on "Learning Robot Safety from Sparse Human Feedback using Conformal Prediction" addresses how to learn robot safety by showing policy trajectories to humans who flag unsafe behavior, using conformal prediction to identify regions of states guaranteed to contain a user-specified fraction of future policy errors.

Another recent work presents the Safe ALTernatives (SALT) framework, which uses reachability analysis to compute a goal-parameterized reach-avoid value network that quantifies safety and liveness of robot policies, acting as a safety filter that suggests safe alternative actions.

**Broader Safety Policy Work:**

Earlier research formalized safe learning probabilistically by defining an optimization problem to maximize expected return while keeping expected damage below a safety limit.

Other approaches repair erroneous policy networks to satisfy formal safety 
…[truncated 551 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-23T03:06:17.591756+00:00_

Web search results for query: "robot inaction safety reward hacking OR conservative policy collapse robot 2024 2025"

Links: [{"title":"Mitigating Reward Hacking in RLHF via Advantage Sign Robustness","url":"https://arxiv.org/pdf/2604.02986"},{"title":"Natural Emergent Misalignment from Reward Hacking in Production RL","url":"https://arxiv.org/pdf/2511.18397"},{"title":"Inference-Time Reward Hacking in Large Language Models Hadi Khalaf","url":"https://openreview.net/pdf?id=hSX7Dd8dxy"},{"title":"Defining and Characterizing Reward Hacking","url":"https://arxiv.org/pdf/2209.13085"},{"title":"AI-Powered Cyber Threats in 2025: The Rise of Autonomous Attack Agents and the Collapse of Traditional Defenses | by Chetan Seripally | Medium","url":"https://medium.com/@seripallychetan/ai-powered-cyber-threats-in-2025-the-rise-of-autonomous-attack-agents-and-the-collapse-of-ce80a5f05afa"},{"title":"Correlated Proxies: A New Definition and Improved Mitigation for Reward   Hacking","url":"https://arxiv.org/pdf/2403.03185"},{"title":"Inference-Time Reward Hacking in Large Language Models | OpenReview","url":"https://openreview.net/forum?id=hSX7Dd8dxy"}]

I've found several relevant research papers on reward hacking. Here are the key findings:

## Reward Hacking Research (2024-2025)

Multiple major AI labs have reported the presence of "reward hacking" in their training runs, with recent research addressing this challenge from multiple angles.

**Definition and Problem:** By overoptimizing for a misspecified reward, we can subvert intended alignment goals and reduce overall performance -- a phenomenon commonly referred to as reward hacking.

**Real-World Impact:** A reward hacking policy's behavior is often undesirable and can be especially catastrophic when deployed in safety-critical scenarios, such as autonomous driving.

**Mitigation Approaches:** 

1. Ensemble-based methods train multiple reward models and optimize conservatively with respect to their disagreement, while distri
…[truncated 576 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-23T03:06:17.591908+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "SafeLIBERO safe reinforcement learning benchmark manipulation 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "tool_args": {
    "query": "SafeLIBERO safe reinforcement learning benchmark manipulation 2024 2025"
  }
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-23T03:06:17.592036+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "SAFE multitask failure detection vision language action models arXiv 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "tool_args": {
    "query": "SAFE multitask failure detection vision language action models arXiv 2025"
  }
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-23T03:06:17.592159+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "collision rate metric robot evaluation policy learning 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "tool_args": {
    "query": "collision rate metric robot evaluation policy learning 2024 2025"
  }
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-23T03:06:17.592278+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "signed distance field SDF collision avoidance robot learning policy 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "tool_args": {
    "query": "signed distance field SDF collision avoidance robot learning policy 2024 2025"
  }
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-23T03:06:17.592397+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "safety constraint robot policy evaluation VLA vision language action 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "tool_args": {
    "query": "safety constraint robot policy evaluation VLA vision language action 2024 2025"
  }
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-23T03:06:17.592548+00:00_

Web search results for query: "action mode collapse imitation learning robot 2023 2024 2025"

Links: [{"title":"Published as a conference paper at ICLR 2025 LEARNING ON ONE MODE:","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/be62c4a943675195ff5a2a98d5b9724f-Paper-Conference.pdf"},{"title":"Imitation learning for legged robot locomotion: a survey - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12702866/"},{"title":"Frontiers | Imitation learning for legged robot locomotion: a survey","url":"https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2025.1678567/full"},{"title":"Awesome-Robotics-Manipulation/contents/low-level_learning-based_action_modelling.md at main · BaiShuanghao/Awesome-Robotics-Manipulation","url":"https://github.com/BaiShuanghao/Awesome-Robotics-Manipulation/blob/main/contents/low-level_learning-based_action_modelling.md"},{"title":"The Pitfalls of Imitation Learning when Actions are Continuous","url":"https://arxiv.org/pdf/2503.09722"}]

Based on the web search results, here are the key findings related to action mode collapse in imitation learning for robots (2023-2025):

## Main Research Areas:

**Action Mode Collapse Problem:**
Multi-modal action distributions can collapse into suboptimal or invalid averages, as studied by researchers including Cai et al. (2023), Wang et al. (2024b), and Yang et al. (2022b). A recent approach called Weighted Imitation Learning on One Mode (LOM) proposes that learning from a single mode — the one with the highest expected return — is sufficient to generate optimal actions.

**Imitation Learning for Robot Locomotion:**
In adversarial motion priors, the discriminator inherits a reward-design burden: if it is too weak, the policy diverges; if too strong, learning collapses. Vollenweider's multi-prior variant (2023) blends gait styles (trot, bound, and jump) into a single policy with 92% automatic mode-selection accuracy.

**Recent Trends (2023-2025):**
Bipedal and human
…[truncated 522 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-23T03:06:17.592697+00:00_

Web search results for query: "signed distance field robot manipulation obstacle avoidance 2024 2025"

Links: [{"title":"[2406.01137] Configuration Space Distance Fields for Manipulation Planning","url":"https://arxiv.org/abs/2406.01137"},{"title":"(PDF) Obstacle Avoidance for Manipulator with Arbitrary Arm Shape Using Signed Distance Function","url":"https://www.researchgate.net/publication/328874046_Obstacle_Avoidance_for_Manipulator_with_Arbitrary_Arm_Shape_Using_Signed_Distance_Function"},{"title":"[PDF] Collision-Free Motion Generation Based on Stochastic Optimization and Composite Signed Distance Field Networks of Articulated Robot | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Collision-Free-Motion-Generation-Based-on-and-Field-Liu-Jiang/7b4ef92fc407415eb5daa716b360cff2fdd82e49"},{"title":"Médéric Fourmy","url":"https://medericfourmy.github.io/"},{"title":"Dynamic Obstacle Avoidance for Mobile Robots Based on 2D Differential Euclidean Signed Distance Field Maps in Park Environment","url":"https://www.mdpi.com/2032-6653/15/7/320"},{"title":"Collision-Free Motion Generation Based on Stochastic Optimization and Composite Signed Distance Field Networks of Articulated Robot | Request PDF","url":"https://www.researchgate.net/publication/373665800_Collision-Free_Motion_Generation_Based_on_Stochastic_Optimization_and_Composite_Signed_Distance_Field_Networks_of_Articulated_Robot"}]

Based on the search results, here's what I found about signed distance fields in robot manipulation and obstacle avoidance for 2024-2025:

## Recent Research Developments

The signed distance field is a popular implicit shape representation in robotics, providing geometric information about objects and obstacles in a form that can easily be combined with control, optimization and learning techniques.

### Configuration Space Distance Fields

A recent approach proposes an efficient algorithm to compute and fuse CDFs that can be generalized to arbitrary scenes, with a neura
…[truncated 1274 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-23T03:06:17.592845+00:00_

Web search results for query: "SDF collision avoidance robotic arm motion planning 2024 2025"

Links: [{"title":"RobotSDF: Implicit Morphology Modeling for the Robotic Arm - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC11359239/"},{"title":"Real-time collision avoidance with robot distance fields in a task-priority framework - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S0921889026000679"},{"title":"Robot movement planning for obstacle avoidance using reinforcement learning | Scientific Reports","url":"https://www.nature.com/articles/s41598-025-17740-5"},{"title":"Obstacle avoidance path planning of 6-DOF robotic arm based on improved A* algorithm and artificial potential field method | Robotica | Cambridge Core","url":"https://www.cambridge.org/core/journals/robotica/article/abs/obstacle-avoidance-path-planning-of-6dof-robotic-arm-based-on-improved-a-algorithm-and-artificial-potential-field-method/1D3708C34FE42078D5CF0B8F3492E8B0"},{"title":"Review on Motion Planning of Robotic Manipulator in Dynamic Environments - Liu - 2024 - Journal of Sensors - Wiley Online Library","url":"https://onlinelibrary.wiley.com/doi/10.1155/2024/5969512"},{"title":"Robot movement planning for obstacle avoidance using reinforcement learning","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12432133/"},{"title":"Efficient Collision Detection Framework for Enhancing Collision-Free   Robot Motion","url":"https://arxiv.org/pdf/2409.14955"}]

Based on the search results, here's what I found about SDF collision avoidance and robotic arm motion planning from 2024-2025:

## Key Research Areas

The expression of robot arm morphology is a critical foundation for achieving effective motion planning and collision avoidance in robotic systems.

### SDF-Based Approaches

Recent work has focused on using signed distance fields (SDFs) for collision avoidance. A task-priority control framework embeds signed distance fields (SDFs) directly into the control loop, ena
…[truncated 1289 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-23T03:06:17.592993+00:00_

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
  "session": "worker_research_related_work_survey_20260523T030015",
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

_source line 47 · 2026-05-23T03:06:17.593121+00:00_

Web search results for query: "neural signed distance field robot safety manipulation 2023 2024 2025"

Links: [{"title":"Neural NMPC through signed distance field encoding for collision avoidance - Martin Jacquet, Marvin Harms, Kostas Alexis, 2025","url":"https://journals.sagepub.com/doi/10.1177/02783649251401223"},{"title":"CSSDF-Net: Safe Motion Planning Based on Neural Implicit Representations of Configuration Space Distance Field","url":"https://arxiv.org/pdf/2603.18669"},{"title":"[PDF] Collision-Free Motion Generation Based on Stochastic Optimization and Composite Signed Distance Field Networks of Articulated Robot | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Collision-Free-Motion-Generation-Based-on-and-Field-Liu-Jiang/7b4ef92fc407415eb5daa716b360cff2fdd82e49"},{"title":"iSDF: Real-Time Neural Signed Distance Fields for Robot ...","url":"https://joeaortiz.github.io/iSDF/"},{"title":"Representing Robot Geometry as Distance Fields: Applications to Whole-body Manipulation | Request PDF","url":"https://www.researchgate.net/publication/382979799_Representing_Robot_Geometry_as_Distance_Fields_Applications_to_Whole-body_Manipulation"},{"title":"iSDF: Real-Time Neural Signed Distance Fields for Robot Perception","url":"https://arxiv.org/pdf/2204.02296"},{"title":"iSDF: Real-Time Neural Signed Distance Fields for Robot Perception - ADS","url":"https://ui.adsabs.harvard.edu/abs/2022arXiv220402296O/abstract"}]

I found several relevant research papers on neural signed distance fields for robot safety and manipulation. Here are the key findings:

**Recent Work (2025):**

A 2025 paper introduces a neural architecture for encoding range observations as signed distance functions (SDFs) and integrates this into neural nonlinear model predictive control (NMPC) for achieving collision-free navigation in unknown environments.

**Configuration Space Applications (2025):**

Implicit approaches that fit Euclidian Signed Distance Fields with neural networks have
…[truncated 1230 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-23T03:06:17.593250+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-23T03:06:17.593372+00:00_

Web search results for query: "safety benchmark robot learning 2024 2025"

Links: [{"title":"Robotics AI Benchmarks 2026: State of the Art | CodeSOTA | CodeSOTA","url":"https://www.codesota.com/robotics"},{"title":"Safe Learning in Robotics: From Learning-Based Control to Safe   Reinforcement Learning","url":"https://arxiv.org/pdf/2108.06266"},{"title":"safe-control-gym: a Unified Benchmark Suite for Safe Learning-based   Control and Reinforcement Learning in Robotics","url":"https://arxiv.org/pdf/2109.06325"},{"title":"A Survey of Embodied World Models Yu Shang1 Yinzhou Tang1∗ Xin Zhang1∗","url":"https://fi.ee.tsinghua.edu.cn/public/publications/0940dda4-af15-11f0-9d60-0242ac120002.pdf"},{"title":"Robobench: A Comprehensive Evaluation Benchmark for Multimodal Large Language Models as Embodied Brain","url":"https://arxiv.org/html/2510.17801v1"},{"title":"ROBEL: Robotics Benchmarks for Learning with Low-Cost Robots","url":"https://arxiv.org/pdf/1909.11639"},{"title":"Industry Insights: Humanoid Robots in 2025: The Next Stage of Evolution","url":"https://www.automate.org/industry-insights/humanoid-robots-are-evolving"}]

Based on the search results, here's what I found about safety benchmarks in robot learning for 2024-2025:

## Key Safety Benchmark Developments

Safe-control-gym is an open-source benchmark suite designed to quantitatively compare the control performance, data efficiency, and safety of multiple approaches from traditional control, learning-based control, and reinforcement learning.

ROBEL (Robotics Benchmarks for Learning with Low-Cost Robots) provides three signals—dense-reward, sparse-score, and hardware-safety—to facilitate the study of safety challenges in robot learning.

## Recent Trends (2025)

2024-2025 marks the emergence of generalist robot policies—models that can control multiple robot types. Additionally, RoboBench evaluates embodied AI through four aspects: robotic-centric (considering embodiment type and viewpoint), object-centric (exam
…[truncated 531 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-23T03:06:17.593591+00:00_

Web search results for query: "SafeLIBERO safe reinforcement learning benchmark manipulation 2024 2025"

Links: [{"title":"Balance Reward and Safety Optimization for Safe Reinforcement Learning:   A Perspective of Gradient Manipulation","url":"https://arxiv.org/pdf/2405.01677"},{"title":"GUARD: A Safe Reinforcement Learning Benchmark","url":"https://arxiv.org/html/2305.13681v4"},{"title":"Safety-Gymnasium: A Unified Safe Reinforcement Learning Benchmark","url":"https://arxiv.org/pdf/2310.12567"},{"title":"GitHub - bitzhangcy/Safe-Deep-Reinforcement-Learning · GitHub","url":"https://github.com/bitzhangcy/Safe-Deep-Reinforcement-Learning"},{"title":"[2310.12567] Safety-Gymnasium: A Unified Safe Reinforcement Learning Benchmark","url":"https://arxiv.org/abs/2310.12567"},{"title":"GUARD: A Safe Reinforcement Learning Benchmark","url":"https://arxiv.org/pdf/2305.13681"}]

Based on the search results, I found several relevant safe reinforcement learning benchmarks, but the specific "SafeLIBERO" benchmark does not appear in these results. Instead, here are the key safe RL benchmarks that were found:

## Safe RL Benchmarks Found:

1. **Safety-Gymnasium**: An environment suite that encompasses safety-critical tasks in both single and multi-agent scenarios, with a library of algorithms called Safe Policy Optimization (SafePO) comprising 16 state-of-the-art SafeRL algorithms.

2. **GUARD**: A standardized benchmark for comparing and evaluating the performance of various safe RL algorithms across different applications.

3. **Safety-MuJoCo Benchmark**: A benchmark developed to assess the performance of safe RL algorithms.

The search results do not contain specific information about a benchmark called "SafeLIBERO" for safe reinforcement learning in manipulation tasks. The results show various other safe RL benchmarks and frameworks from 2023-2024, but not this specific one. If you're looking for more detailed information about SafeLIBERO specifically, you may want to try a more
…[truncated 181 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-23T03:06:17.593787+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"do nothing\" policy robot safe reinforcement learning overly conservative 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"do nothing\" policy robot safe reinforcement learning overly conservative 2024 2025"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-23T03:06:17.593925+00:00_

Web search results for query: "distance field motion planning manipulation collision checking 2024"

Links: [{"title":"Review on Motion Planning of Robotic Manipulator in Dynamic Environments - Liu - 2024 - Journal of Sensors - Wiley Online Library","url":"https://onlinelibrary.wiley.com/doi/10.1155/2024/5969512"},{"title":"Representing Robot Geometry as Distance Fields: Applications to Whole-body Manipulation | Request PDF","url":"https://www.researchgate.net/publication/382979799_Representing_Robot_Geometry_as_Distance_Fields_Applications_to_Whole-body_Manipulation"},{"title":"Real-time collision avoidance with robot distance fields in a task-priority framework - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S0921889026000679"},{"title":"(PDF) Configuration Space Distance Fields for Manipulation Planning","url":"https://www.researchgate.net/publication/383891276_Configuration_Space_Distance_Fields_for_Manipulation_Planning"},{"title":"Ch. 6 - Motion Planning - Robotic Manipulation","url":"https://manipulation.csail.mit.edu/trajectories.html"},{"title":"Novel Probabilistic Collision Detection for Manipulator Motion Planning Using HNSW","url":"https://www.mdpi.com/2075-1702/12/5/321"},{"title":"CSSDF-Net: Safe Motion Planning Based on Neural Implicit Representations of Configuration Space Distance Field","url":"https://arxiv.org/pdf/2603.18669"},{"title":"ParaMaP: Parallel Mapping and Collision-free Motion Planning for Reactive Robot Manipulation","url":"https://arxiv.org/html/2512.22575v1"},{"title":"ParaMaP: Parallel Mapping and Collision-free Motion Planning for Reactive Robot Manipulation","url":"https://arxiv.org/pdf/2512.22575"}]

I've found comprehensive search results on distance field motion planning, manipulation, and collision checking from 2024. Here are the key findings:

## Distance Fields in Motion Planning

Signed distance fields (SDFs) determine obstacle costs based on the distance to the nearest obstacle utilizing the Eucl
…[truncated 1497 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool result

_source line 53 · 2026-05-23T03:06:17.594080+00:00_

Web search results for query: "collision rate metric robot evaluation policy learning 2024 2025"

Links: [{"title":"Evaluating Trajectory Collision Probability through Adaptive Importance   Sampling for Safe Motion Planning","url":"https://arxiv.org/pdf/1609.05399"},{"title":"Autonomous Robot Goal Seeking and Collision Avoidance in the Physical World: An Automated Learning and Evaluation Framework Based on the PPO Method","url":"https://www.mdpi.com/2076-3417/14/23/11020"},{"title":"Integrating self-attention and LSTM into TD3 for robust mobile robot navigation in dynamic environments | Scientific Reports","url":"https://www.nature.com/articles/s41598-026-45819-0"},{"title":"GitHub - smallfryy/corl-2025-papers: ✨ 200+ robotics papers from CoRL 2025, with TLDRs, project pages, code, and more","url":"https://github.com/smallfryy/corl-2025-papers"},{"title":"Robot Learning as an Empirical Science: Best Practices for Policy   Evaluation","url":"https://arxiv.org/pdf/2409.09491"},{"title":"Fully Distributed Multi-Robot Collision Avoidance via Deep Reinforcement   Learning for Safe and Efficient Navigation in Complex Scenarios","url":"https://arxiv.org/pdf/1808.03841"}]

Based on the search results, here are relevant findings about collision rate metrics in robot evaluation and policy learning:

## Recent Work on Collision Rate as Evaluation Metric

Recent research shows collision rate as a key performance metric, with one study reporting that an improved algorithm achieved a 91% success rate and lowered collision rate from 23% to 9%. This demonstrates how collision rate is used alongside other metrics like success rate to evaluate robot navigation policies.

## Comprehensive Evaluation Frameworks

An evaluation framework from 2024 investigates reinforcement learning algorithm's generalization capability in regard to unseen scenarios in terms of learning convergence and success rates by transferring learned policies in simulation to physical environments.

## Best Practic
…[truncated 1028 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 54 · 2026-05-23T03:06:17.594231+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "safe reinforcement learning robot stop moving trivial solution conservative constraint 2023 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "tool_args": {
    "query": "safe reinforcement learning robot stop moving trivial solution conservative constraint 2023 2024 2025"
  }
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-23T03:06:17.594369+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ICLR 2025 \"learning on one mode\" imitation learning action collapse robot"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ICLR 2025 \"learning on one mode\" imitation learning action collapse robot"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-23T03:06:17.594523+00:00_

Web search results for query: "signed distance field SDF collision avoidance robot learning policy 2024 2025"

Links: [{"title":"(PDF) Neural NMPC through Signed Distance Field Encoding for Collision Avoidance","url":"https://www.researchgate.net/publication/398025684_Neural_NMPC_through_Signed_Distance_Field_Encoding_for_Collision_Avoidance"},{"title":"[PDF] Collision-Free Motion Generation Based on Stochastic Optimization and Composite Signed Distance Field Networks of Articulated Robot | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Collision-Free-Motion-Generation-Based-on-and-Field-Liu-Jiang/7b4ef92fc407415eb5daa716b360cff2fdd82e49"},{"title":"Neural NMPC through Signed Distance Field Encoding for Collision Avoidance","url":"https://arxiv.org/pdf/2511.21312"},{"title":"Neural NMPC through signed distance field encoding for collision avoidance - Martin Jacquet, Marvin Harms, Kostas Alexis, 2025","url":"https://journals.sagepub.com/doi/10.1177/02783649251401223"},{"title":"Collision-Free Motion Generation Based on Stochastic Optimization and Composite Signed Distance Field Networks of Articulated Robot | Request PDF","url":"https://www.researchgate.net/publication/373665800_Collision-Free_Motion_Generation_Based_on_Stochastic_Optimization_and_Composite_Signed_Distance_Field_Networks_of_Articulated_Robot"},{"title":"Differentiable Composite Neural Signed Distance Fields for Robot   Navigation in Dynamic Indoor Environments","url":"https://arxiv.org/pdf/2502.02664"}]

Here are the search results for your query on signed distance field (SDF) collision avoidance in robot learning and policy:

## Key Recent Works (2024-2025)

**Neural NMPC for Aerial Robot Navigation:**
A neural nonlinear model predictive control (NMPC) framework for mapless, collision-free navigation in unknown environments with Aerial Robots using onboard range sensing has been introduced. This approach leverages deep neural networks to encode a single range image into a Signed Dist
…[truncated 1142 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 57 · 2026-05-23T03:06:17.594676+00:00_

Web search results for query: "safety constraint robot policy evaluation VLA vision language action 2024 2025"

Links: [{"title":"SafeVLA: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning","url":"https://papers.nips.cc/paper_files/paper/2025/hash/e185c7be603426028c32ae1003a59d78-Abstract-Conference.html"},{"title":"Language-Action Model via Constrained Learning","url":"https://openreview.net/pdf?id=dt940loCBT"},{"title":"SafeVLA: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning | OpenReview","url":"https://openreview.net/forum?id=dt940loCBT"},{"title":"SafeVLA: Towards Safety Alignment of Vision-Language-Action Model via Safe Reinforcement Learning","url":"https://arxiv.org/html/2503.03480v1"},{"title":"Vision-Language-Action Safety: Threats, Challenges, Evaluations, and Mechanisms","url":"https://arxiv.org/html/2604.23775v1"},{"title":"NeurIPS Poster SafeVLA: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning","url":"https://neurips.cc/virtual/2025/poster/116975"},{"title":"[2503.03480] SafeVLA: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning","url":"https://arxiv.org/abs/2503.03480"},{"title":"SafeVLA: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning","url":"https://safevla.github.io/"},{"title":"GitHub - PKU-Alignment/SafeVLA: [NeurIPS 2025 Spotlight] Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning. · GitHub","url":"https://github.com/PKU-Alignment/SafeVLA"}]

Based on the search results, I found several relevant papers on safety constraints and robot policy evaluation for Vision-Language-Action (VLA) models from 2024-2025:

## Main Results

**SafeVLA: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning**

Vision-language-action models (VLAs) show potential as generalist robot policies, but these models pose extreme safety challenges durin
…[truncated 1440 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 58 · 2026-05-23T03:06:17.594832+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "auxiliary loss safe reinforcement learning robot policy 2023 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "tool_args": {
    "query": "auxiliary loss safe reinforcement learning robot policy 2023 2024 2025"
  }
}
```

</details>

---

### Tool result

_source line 59 · 2026-05-23T03:06:17.594962+00:00_

Web search results for query: "CoFreeVLA collision-free dual-arm manipulation VLA risk estimation arXiv 2025"

Links: [{"title":"CoFreeVLA: Collision-Free Dual-Arm Manipulation via Vision-Language-Action Model and Risk Estimation","url":"https://arxiv.org/pdf/2601.21712"},{"title":"CoFreeVLA: Collision-Free Dual-Arm Manipulation via Vision-Language-Action Model and Risk Estimation","url":"https://arxiv.org/html/2601.21712v2"},{"title":"(PDF) FCL: A General Purpose Library for Collision and Proximity Queries","url":"https://www.researchgate.net/publication/247161844_FCL_A_General_Purpose_Library_for_Collision_and_Proximity_Queries"},{"title":"Design and Development of an Intelligent Collision Avoidance Platform for a Teleoperated Dual Robotic Arm - Gautam - 2025 - Journal of Field Robotics - Wiley Online Library","url":"https://onlinelibrary.wiley.com/doi/10.1002/rob.22565"},{"title":"VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer [Quick Review]","url":"https://liner.com/review/vlsa-visionlanguageaction-models-with-plugandplay-safety-constraint-layer"}]

I found the paper you're looking for! Here are the key details:

## CoFreeVLA: Collision-Free Dual-Arm Manipulation via Vision-Language-Action Model and Risk Estimation

CoFreeVLA addresses the safety challenges of dual-arm deployment with Vision-Language-Action (VLA) models, which remain unsafe due to under-modeled self-collisions between arms and grasped objects.

**Main Contribution:**
The system augments an end-to-end VLA with a short-horizon self-collision risk estimator that predicts collision likelihood from proprioception, visual embeddings, and planned actions, which gates risky commands, recovers to safe states via risk-guided adjustments, and shapes policy refinement for safer rollouts.

**Training Approach:**
The estimator is pre-trained with model-based collision labels and post-trained on real-robot rollouts for calibration.

**Results:**
On five bimanual tasks with the P
…[truncated 285 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool call

_source line 60 · 2026-05-23T03:06:17.595106+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "auxiliary objective safety constraint imitation learning robot manipulation 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "tool_args": {
    "query": "auxiliary objective safety constraint imitation learning robot manipulation 2024 2025"
  }
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-23T03:06:17.595232+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "multi-task safety loss robot learning collision avoidance 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "tool_args": {
    "query": "multi-task safety loss robot learning collision avoidance 2024 2025"
  }
}
```

</details>

---

### Tool call

_source line 62 · 2026-05-23T03:06:17.595360+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "VLA vision language action model collision avoidance safety constraint 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "tool_args": {
    "query": "VLA vision language action model collision avoidance safety constraint 2024 2025"
  }
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-23T03:06:17.595505+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2406.01137 configuration space distance fields manipulation planning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2406.01137 configuration space distance fields manipulation planning"
  }
}
```

</details>

---

### Tool call

_source line 64 · 2026-05-23T03:06:17.595630+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Safety-Gymnasium unified safe reinforcement learning benchmark NeurIPS 2023 authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Safety-Gymnasium unified safe reinforcement learning benchmark NeurIPS 2023 authors"
  }
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-23T03:06:17.595751+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "RobotSDF implicit morphology modeling robotic arm 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "tool_args": {
    "query": "RobotSDF implicit morphology modeling robotic arm 2024"
  }
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-23T03:06:17.595878+00:00_

Web search results for query: "VLSA plug-and-play safety constraint layer vision language action arXiv 2024"

Links: [{"title":"VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer | alphaXiv","url":"https://www.alphaxiv.org/overview/2512.11891"},{"title":"VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer","url":"https://arxiv.org/pdf/2512.11891"},{"title":"VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer","url":"https://arxiv.org/html/2512.11891v1"},{"title":"VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer [Quick Review]","url":"https://liner.com/review/vlsa-visionlanguageaction-models-with-plugandplay-safety-constraint-layer"},{"title":"VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer - Paper Details","url":"https://www.chatpaper.ai/dashboard/paper/94b34e07-289d-4650-a2e6-14d20295c2de"},{"title":"[2512.11891] VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer","url":"https://arxiv.org/abs/2512.11891"},{"title":"VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer | Takara TLDR","url":"https://tldr.takara.ai/p/2512.11891"},{"title":"(PDF) VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer","url":"https://www.researchgate.net/publication/398721287_VLSA_Vision-Language-Action_Models_with_Plug-and-Play_Safety_Constraint_Layer"},{"title":"VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer","url":"https://vlsa-aegis.github.io/"},{"title":"GitHub - THU-RCSCT/vlsa-aegis: VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer","url":"https://github.com/THU-RCSCT/vlsa-aegis"}]

Based on the search results, I found comprehensive information about the VLSA research paper from arXiv.

## VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer

The paper introduces a Vision-Langua
…[truncated 1724 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "elapsed_ms": 4
}
```

</details>

---

### Tool result

_source line 67 · 2026-05-23T03:06:17.596025+00:00_

Web search results for query: "SAFE multitask failure detection vision language action models arXiv 2025"

Links: [{"title":"SAFE: Multitask Failure Detection for Vision-Language-Action Models","url":"https://vla-safe.github.io/"},{"title":"[PDF] SAFE: Multitask Failure Detection for Vision-Language-Action Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/SAFE:-Multitask-Failure-Detection-for-Models-Gu-Ju/8165f26c174bd327506242ee898cf18a3abe61cf"},{"title":"GitHub - vla-safe/SAFE: This is the official repository for \"SAFE: Multitask Failure Detection for Vision-Language-Action Models\" (NeurIPS 2025) · GitHub","url":"https://github.com/vla-safe/SAFE"},{"title":"[2506.09937] SAFE: Multitask Failure Detection for Vision-Language-Action Models","url":"https://arxiv.org/abs/2506.09937"},{"title":"SAFE: Multitask Failure Detection for Vision-Language-Action Models","url":"https://arxiv.org/pdf/2506.09937"},{"title":"SAFE: Multitask Failure Detection for Vision-Language-Action Models","url":"https://arxiv.org/html/2506.09937v1"},{"title":"SAFE: Multitask Failure Detection for Vision-Language-Action Models | Request PDF","url":"https://www.researchgate.net/publication/392597657_SAFE_Multitask_Failure_Detection_for_Vision-Language-Action_Models"},{"title":"Paper page - SAFE: Multitask Failure Detection for Vision-Language-Action Models","url":"https://huggingface.co/papers/2506.09937"},{"title":"SAFE: Multitask Failure Detection for Vision-Language-Action Models","url":"https://openreview.net/pdf/15287adb570fdbe172fcf9405e1546b32bdf42a0.pdf"}]

I found comprehensive information about the SAFE paper. Here's what the search results show:

## SAFE: Multitask Failure Detection for Vision-Language-Action Models

SAFE is a failure detector introduced by Gu, Ju, Sun, Gilitschenski, Nishimura, Itkina, and Shkurti that can detect failures for unseen tasks zero-shot and achieve state-of-the-art performance (arXiv:2506.09937, 2025). The paper was published as a 
…[truncated 1017 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool call

_source line 68 · 2026-05-23T03:06:17.596181+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Robot Learning as an Empirical Science\" \"Best Practices for Policy Evaluation\" 2024 authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Robot Learning as an Empirical Science\" \"Best Practices for Policy Evaluation\" 2024 authors"
  }
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-23T03:06:17.596311+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "SafeVLA PKU safety alignment VLA constrained learning NeurIPS 2025 authors results"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "tool_args": {
    "query": "SafeVLA PKU safety alignment VLA constrained learning NeurIPS 2025 authors results"
  }
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-23T03:06:17.596454+00:00_

Web search results for query: "ICLR 2025 "learning on one mode" imitation learning action collapse robot"

Links: [{"title":"Published as a conference paper at ICLR 2025 LEARNING ON ONE MODE:","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/be62c4a943675195ff5a2a98d5b9724f-Paper-Conference.pdf"},{"title":"One-Shot Imitation Learning","url":"https://arxiv.org/pdf/1703.07326"},{"title":"ICLR: In-Context Imitation Learning with Visual Reasoning","url":"https://arxiv.org/pdf/2603.07530"},{"title":"Robust Imitation of Diverse Behaviors","url":"https://arxiv.org/pdf/1707.02747"},{"title":"The Pitfalls of Imitation Learning when Actions are Continuous","url":"https://arxiv.org/pdf/2503.09722"}]

Great! I found relevant results. The first search result is directly from the ICLR 2025 conference proceedings for the paper "Learning on One Mode."

Based on the search results, the paper proposes Weighted Imitation Learning on One Mode (LOM), with the insight that learning from a single mode — the one with the highest expected return — is sufficient to generate optimal actions.

The paper addresses the problem of multi-modal distributions collapsing into suboptimal or invalid averages, and proposes a simpler approach rather than modeling the full multi-modal action distribution. 

The paper appears in the ICLR 2025 conference proceedings and tackles a key challenge in imitation learning for robot manipulation by focusing on learning from the highest-value action mode rather than attempting to capture the entire action distribution.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 71 · 2026-05-23T03:06:17.596604+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "GUARD safe reinforcement learning benchmark 2023 authors Zhao"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "tool_args": {
    "query": "GUARD safe reinforcement learning benchmark 2023 authors Zhao"
  }
}
```

</details>

---

### Tool result

_source line 72 · 2026-05-23T03:06:17.596741+00:00_

Web search results for query: "safe reinforcement learning robot stop moving trivial solution conservative constraint 2023 2024 2025"

Links: [{"title":"Safe Reinforcement Learning of Robot Trajectories in the Presence of Moving Obstacles","url":"https://arxiv.org/html/2411.05784v1"},{"title":"GitHub - translearn/safeMotionsRisk: [RA-L 2024] Safe Reinforcement Learning of Robot Trajectories in the Presence of Moving Obstacles","url":"https://github.com/translearn/safeMotionsRisk"},{"title":"Safe Reinforcement Learning of Robot Trajectories in the Presence of   Moving Obstacles","url":"https://arxiv.org/pdf/2411.05784"},{"title":"POLICEd RL: Learning Closed-Loop Robot Control ...","url":"https://www.roboticsproceedings.org/rss20/p104.pdf"},{"title":"Frontiers | A human-centered safe robot reinforcement learning framework with interactive behaviors","url":"https://www.frontiersin.org/journals/neurorobotics/articles/10.3389/fnbot.2023.1280341/full"},{"title":"Recursive Constraints to Prevent Instability in Constrained   Reinforcement Learning","url":"https://arxiv.org/pdf/2201.07958"},{"title":"[2411.05784] Safe Reinforcement Learning of Robot Trajectories in the Presence of Moving Obstacles","url":"https://arxiv.org/abs/2411.05784"},{"title":"Safe Reinforcement Learning of Robot Trajectories in the Presence of Moving Obstacles | Request PDF","url":"https://www.researchgate.net/publication/385399568_Safe_Reinforcement_Learning_of_Robot_Trajectories_in_the_Presence_of_Moving_Obstacles"}]

Based on the search results, I found relevant research on safe reinforcement learning in robotics with connections to your query about trivial solutions and conservative constraints.

The most directly relevant finding is that "the most trivial case is a resting state, provided that the robot is stopped in a region of the environment where no moving obstacles are present." This appears in a 2024 IEEE paper on safe reinforcement learning for robot trajectories in dynamic environments.


…[truncated 1087 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 73 · 2026-05-23T03:06:17.596886+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2512.11891 VLSA AEGIS authors venue 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2512.11891 VLSA AEGIS authors venue 2025"
  }
}
```

</details>

---

### Tool call

_source line 74 · 2026-05-23T03:06:17.597009+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2601.21712 CoFreeVLA authors 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2601.21712 CoFreeVLA authors 2026"
  }
}
```

</details>

---

### Tool call

_source line 75 · 2026-05-23T03:06:17.597134+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CompliantVLA adaptor variable impedance VLA safe contact rich manipulation arXiv 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CompliantVLA adaptor variable impedance VLA safe contact rich manipulation arXiv 2025"
  }
}
```

</details>

---

### Tool result

_source line 76 · 2026-05-23T03:06:17.597265+00:00_

Web search results for query: "RobotSDF implicit morphology modeling robotic arm 2024"

Links: [{"title":"RobotSDF: Implicit Morphology Modeling for the Robotic Arm","url":"https://www.mdpi.com/1424-8220/24/16/5248"},{"title":"RobotSDF: Implicit Morphology Modeling for the Robotic Arm - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC11359239/"},{"title":"(PDF) RobotSDF: Implicit Morphology Modeling for the Robotic Arm","url":"https://www.researchgate.net/publication/383097434_RobotSDF_Implicit_Morphology_Modeling_for_the_Robotic_Arm"},{"title":"RobotSDF: Implicit Morphology Modeling for the Robotic Arm","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11359239/"},{"title":"Implicit Articulated Robot Morphology Modeling with Configuration Space Neural Signed Distance Functions","url":"https://arxiv.org/html/2309.16085"}]

Based on the search results, here's what I found about RobotSDF:

## Overview

RobotSDF is an implicit morphology modeling approach that can express the robot shape of arbitrary posture precisely. The expression of robot arm morphology is a critical foundation for achieving effective motion planning and collision avoidance in robotic systems.

## Key Approach

Instead of depicting a whole model of the robot arm, RobotSDF models the robot morphology as integrated implicit joint models driven by joint configurations, converting the dynamic shape change process of the robot into coordinate transformations of query points within each joint's coordinate system.

## Advantages

The signed distance function addresses traditional geometry-based approaches' drawbacks due to its ability to handle complex and arbitrary shapes and lower computational requirements. Experimental results with the Elfin robot demonstrate that RobotSDF can accurately depict robot shapes across different postures up to the millimeter level, which exhibits 38.65% and 66.24% improvement over the Neural-JSDF and configuration space distance field algorithms, respectively, in re
…[truncated 349 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 77 · 2026-05-23T03:06:17.597436+00:00_

Web search results for query: ""do nothing" policy robot safe reinforcement learning overly conservative 2024 2025"

Links: [{"title":"Online Optimization for Offline Safe Reinforcement Learning Yassine Chemingui","url":"https://arxiv.org/pdf/2510.22027"},{"title":"Don't do it: Safer Reinforcement Learning With Rule-based Guidance","url":"https://arxiv.org/pdf/2212.13819"},{"title":"Published as a conference paper at ICLR 2025","url":"https://openreview.net/pdf?id=EpnZEzYDUT"},{"title":"Safe Reinforcement Learning with Dead-Ends Avoidance and Recovery","url":"https://arxiv.org/pdf/2306.13944"},{"title":"Safe Reinforcement Learning for a Robot Being Pursued but with   Objectives Covering More Than Capture-avoidance","url":"https://arxiv.org/pdf/2207.00842"},{"title":"Frontiers | A human-centered safe robot reinforcement learning framework with interactive behaviors","url":"https://www.frontiersin.org/journals/neurorobotics/articles/10.3389/fnbot.2023.1280341/full"},{"title":"Safe Reinforcement Learning of Robot Trajectories in the Presence of   Moving Obstacles","url":"https://arxiv.org/pdf/2411.05784"},{"title":"Safe Policies for Reinforcement Learning via Primal-Dual Methods","url":"https://arxiv.org/pdf/1911.09101"}]

Based on the search results, I found relevant information about safe reinforcement learning and the challenge of overly conservative policies in robot learning from 2024-2025:

Constrained policy optimization approaches for safe reinforcement learning can yield overly conservative (near zero-reward) policies, which is a recognized problem in the field. Existing methods tend to adopt overly conservative policies to ensure safety during and after training, but overly conservative policies severely hinder exploration and make algorithms substantially less rewarding.

One approach proposes constructing a boundary that distinguishes safe and unsafe states, equivalent to identifying dead-end states, which has minimum limitation on exploration. This contras
…[truncated 683 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool result

_source line 78 · 2026-05-23T03:06:17.597652+00:00_

Web search results for query: ""Robot Learning as an Empirical Science" "Best Practices for Policy Evaluation" 2024 authors"

Links: [{"title":"Robot Learning as an Empirical Science: Best Practices for Policy Evaluation","url":"https://bibbase.org/network/publication/kressgazit-hashimoto-kuppuswamy-shah-horgan-richardson-feng-burchfiel-robotlearningasanempiricalsciencebestpracticesforpolicyevaluation-2024"},{"title":"[2409.09491] Robot Learning as an Empirical Science: Best Practices for Policy Evaluation","url":"https://arxiv.org/abs/2409.09491"},{"title":"Robot Learning as an Empirical Science: Best Practices for Policy Evaluation | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/robot-learning-as-empirical-science-best-practices"},{"title":"(PDF) Robot Learning as an Empirical Science: Best Practices for Policy Evaluation","url":"https://www.researchgate.net/publication/384075741_Robot_Learning_as_an_Empirical_Science_Best_Practices_for_Policy_Evaluation"},{"title":"Robot Policy Evaluation for Sim-to-Real Transfer: A Benchmarking Perspective","url":"https://arxiv.org/pdf/2508.11117"},{"title":"Real-to-Sim Robot Policy Evaluation with Gaussian Splatting Simulation of Soft-Body Interactions","url":"https://real2sim-eval.github.io/"},{"title":"Robot Learning as an Empirical Science: Best Practices for Policy   Evaluation","url":"https://arxiv.org/pdf/2409.09491"},{"title":"Robot Learning as an Empirical Science: Best Practices for Policy Evaluation","url":"https://arxiv.org/html/2409.09491v1"}]

Based on the search results, here are the authors of the 2024 paper "Robot Learning as an Empirical Science: Best Practices for Policy Evaluation":

Hadas Kress-Gazit, Kunimatsu Hashimoto, Naveen Kuppuswamy, Paarth Shah, Phoebe Horgan, Gordon Richardson, Siyuan Feng, and Benjamin Burchfiel

The paper was published in CoRR in 2024.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 79 · 2026-05-23T03:06:17.597803+00:00_

Web search results for query: "multi-task safety loss robot learning collision avoidance 2024 2025"

Links: [{"title":"Integrating collision avoidance strategies into multi-robot task allocation for inspection - Hamza Chakraa, Edouard Leclercq, François Guérin, Dimitri Lefebvre, 2025","url":"https://journals.sagepub.com/doi/10.1177/01423312241295828"},{"title":"Fully Distributed Multi-Robot Collision Avoidance via Deep Reinforcement   Learning for Safe and Efficient Navigation in Complex Scenarios","url":"https://arxiv.org/pdf/1808.03841"},{"title":"Towards Optimally Decentralized Multi-Robot Collision Avoidance via Deep   Reinforcement Learning","url":"https://arxiv.org/pdf/1709.10082"},{"title":"Collision/Obstacle Avoidance Coordination of Multi-Robot Systems: A Survey","url":"https://www.mdpi.com/2076-0825/14/2/85"},{"title":"Risk-Aware Reinforcement Learning with Dynamic Safety Filter for Collision Risk Mitigation in Mobile Robot Navigation","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12431337/"},{"title":"Distributed Non-Communicating Multi-Robot Collision Avoidance via Map-Based Deep Reinforcement Learning","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7506975/"}]

Based on the search results, here are the findings related to multi-task safety loss, robot learning, and collision avoidance from 2024-2025:

## Recent Research (2024-2025)

A human-like collision avoidance method for USVs based on deep reinforcement learning and velocity obstacle was published in 2024.

Latest collision/obstacle avoidance cooperative control developments are classified into three categories: (1) offline planning; (2) receding horizon planning; and (3) reactive control, according to a 2025 survey.

Risk-aware reinforcement learning with dynamic safety filtering for collision risk mitigation in mobile robot navigation was published in 2025, addressing safety and adaptability challenges in dynamic environments.

## Core Approaches to Safety in Robot Learning

The resear
…[truncated 757 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 80 · 2026-05-23T03:06:17.597958+00:00_

Web search results for query: "arxiv 2406.01137 configuration space distance fields manipulation planning"

Links: [{"title":"[2406.01137] Configuration Space Distance Fields for Manipulation Planning","url":"https://arxiv.org/abs/2406.01137"},{"title":"Configuration Space Distance Fields for Manipulation Planning","url":"https://calinon.ch/papers/Li-RSS2024.pdf"},{"title":"Safe Dynamic Motion Generation in Configuration Space Using Differentiable Distance Fields","url":"https://arxiv.org/html/2412.16456"},{"title":"CSSDF-Net: Safe Motion Planning Based on Neural Implicit Representations of Configuration Space Distance Field","url":"https://arxiv.org/html/2603.18669"},{"title":"Implicit Articulated Robot Morphology Modeling with Configuration Space Neural Signed Distance Functions","url":"https://arxiv.org/html/2309.16085v2"},{"title":"(PDF) Configuration Space Distance Fields for Manipulation Planning","url":"https://www.researchgate.net/publication/381122586_Configuration_Space_Distance_Fields_for_Manipulation_Planning"},{"title":"[PDF] Configuration Space Distance Fields for Manipulation Planning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/75af8f157566854a49e72ead68f807166b791809"},{"title":"Configuration Space Distance Fields for Manipulation Planning - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv240601137L/abstract"}]

Based on the search results, here's information about arxiv paper 2406.01137:

## Configuration Space Distance Fields for Manipulation Planning

**Paper Details:**
This paper is authored by Yiming Li, Xuemin Chi, Amirreza Razmjoo, and Sylvain Calinon, and was submitted on June 3, 2024. The paper was accepted to Robotics: Science and Systems (RSS), 2024.

**Main Contribution:**
The signed distance field (SDF) is a popular implicit shape representation in robotics, providing geometric information about objects and obstacles in a form that can easily be combined with control, optimization and learning techniques. Most
…[truncated 1109 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 81 · 2026-05-23T03:06:17.598105+00:00_

Web search results for query: "VLA vision language action model collision avoidance safety constraint 2024 2025"

Links: [{"title":"(PDF) VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer","url":"https://www.researchgate.net/publication/398721287_VLSA_Vision-Language-Action_Models_with_Plug-and-Play_Safety_Constraint_Layer"},{"title":"[2512.11891] VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer","url":"https://arxiv.org/abs/2512.11891"},{"title":"Vision-Language-Action (VLA) Models: Concepts, Progress, Applications and Challenges","url":"https://arxiv.org/html/2505.04769v2"},{"title":"VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer [Quick Review]","url":"https://liner.com/review/vlsa-visionlanguageaction-models-with-plugandplay-safety-constraint-layer"},{"title":"VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer","url":"https://arxiv.org/pdf/2512.11891"},{"title":"Vision-Language-Action Safety: Threats, Challenges, Evaluations, and Mechanisms","url":"https://arxiv.org/html/2604.23775v1"},{"title":"VLA-MP: A Vision-Language-Action Framework for Multimodal Perception and Physics-Constrained Action Generation in Autonomous Driving - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12526522/"},{"title":"Concept-Based Dictionary Learning for Inference-Time Safety in Vision Language Action Models","url":"https://arxiv.org/pdf/2602.01834"}]

Based on the web search results, here are the key findings related to VLA (Vision-Language-Action) models, collision avoidance, and safety constraints in 2024-2025:

## AEGIS/VLSA Architecture (December 2025)

AEGIS is a Vision-Language-Safe Action (VLSA) architecture that integrates Control Barrier Functions (CBFs) into VLA models via a plug-and-play safety constraint layer. AEGIS includes a vision-language based safety assessment module that identifies hazardous objects using VLMs, open-set object detection, and
…[truncated 1325 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 82 · 2026-05-23T03:06:17.598265+00:00_

Web search results for query: "auxiliary objective safety constraint imitation learning robot manipulation 2024 2025"

Links: [{"title":"RAIL: Reachability-Aided Imitation Learning for Safe Policy Execution","url":"https://arxiv.org/pdf/2409.19190"},{"title":"Differentiable Constrained Imitation Learning for Robot Motion Planning   and Control","url":"https://arxiv.org/pdf/2210.11796"},{"title":"Awesome-Robotics-Manipulation/contents/low-level_learning-based_action_modelling.md at main · BaiShuanghao/Awesome-Robotics-Manipulation","url":"https://github.com/BaiShuanghao/Awesome-Robotics-Manipulation/blob/main/contents/low-level_learning-based_action_modelling.md"},{"title":"GitHub - YanjieZe/Paper-List: A paper list of my history reading. Robotics, Learning, Vision. · GitHub","url":"https://github.com/YanjieZe/Paper-List"},{"title":"GitHub - jackyzengl/EIIR: [Embodied-Intelligent-Industrial-Robotics-Survey-2025] Paper List for Embodied Intelligent Industrial Robotics (EIIR) · GitHub","url":"https://github.com/jackyzengl/EIIR"},{"title":"Towards cost-effective and safe contact-rich robotic manipulation with reinforcement learning: A review of techniques for future industrial automation - Anselmo Parnada, Mo Qu, Marco Castellani, Hyung Jin Chang, Yongjing Wang, 2026","url":"https://journals.sagepub.com/doi/10.1177/09596518251350353"},{"title":"GitHub - BaiShuanghao/Awesome-Robotics-Manipulation: A comprehensive list of papers about Robot Manipulation, including papers, codes, and related websites. · GitHub","url":"https://github.com/BaiShuanghao/Awesome-Robotics-Manipulation"}]

I found several relevant research papers and resources related to your search topic. Here are the key findings:

## Recent Work on Safety Constraints in Imitation Learning

Recent evaluations with state-of-the-art imitation learning policies in mobile robots and manipulation tasks show that the highest-performing policies sometimes violate constraints and significantly lose performance under ha
…[truncated 1316 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool result

_source line 83 · 2026-05-23T03:06:17.598430+00:00_

Web search results for query: "GUARD safe reinforcement learning benchmark 2023 authors Zhao"

Links: [{"title":"[PDF] GUARD: A Safe Reinforcement Learning Benchmark | Semantic Scholar","url":"https://www.semanticscholar.org/paper/498d75d17609af4d5f235654423d90bbe3a5c621"},{"title":"[2305.13681] GUARD: A Safe Reinforcement Learning Benchmark","url":"https://arxiv.org/abs/2305.13681"},{"title":"GitHub - intelligent-control-lab/safe_rl_bench","url":"https://github.com/intelligent-control-lab/safe_rl_bench"},{"title":"GUARD: A Safe Reinforcement Learning Benchmark | Request PDF","url":"https://www.researchgate.net/publication/370982025_GUARD_A_Safe_Reinforcement_Learning_Benchmark"},{"title":"GUARD: A Safe Reinforcement Learning Benchmark","url":"https://arxiv.org/html/2305.13681v4"},{"title":"GitHub - bitzhangcy/Safe-Deep-Reinforcement-Learning · GitHub","url":"https://github.com/bitzhangcy/Safe-Deep-Reinforcement-Learning"},{"title":"Model-Free Safe Reinforcement Learning Through Neural Barrier Certificate (2023) | Yujie Yang | 24 Citations","url":"https://scispace.com/papers/model-free-safe-reinforcement-learning-through-neural-7p2f8bce"},{"title":"State-wise Safe and Robust Reinforcement Learning for Continuous Control","url":"http://icontrol.ri.cmu.edu/research/safe-rl.html"},{"title":"GUARD: A Safe Reinforcement Learning Benchmark","url":"https://arxiv.org/pdf/2305.13681"}]

Based on the search results, here's what I found about the GUARD safe reinforcement learning benchmark:

GUARD is a Generalized Unified SAfe Reinforcement Learning Development Benchmark published in 2023. 

**Authors:** The authors are Weiye Zhao, Yifan Sun, Feihan Li, Rui Chen, Ruixuan Liu, Tianhao Wei, and Changliu Liu.

**Overview:** GUARD is a generalized benchmark with a wide variety of RL agents, tasks, and safety constraint specifications, and comprehensively covers state-of-the-art safe RL algorithms with self-contained implementations.

**Purpose:** GUARD was introduced to fill the g
…[truncated 423 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 84 · 2026-05-23T03:06:17.598592+00:00_

Web search results for query: "SafeVLA PKU safety alignment VLA constrained learning NeurIPS 2025 authors results"

Links: [{"title":"SafeVLA - a PKU-Alignment Collection","url":"https://huggingface.co/collections/PKU-Alignment/safevla"},{"title":"GitHub - PKU-Alignment/SafeVLA: [NeurIPS 2025 Spotlight] Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning. · GitHub","url":"https://github.com/PKU-Alignment/SafeVLA"},{"title":"PKU-Alignment Group in NeurIPS 2025! | PKU-Alignment Group @Pair-Lab (under construction)","url":"https://pku-alignment.group/post/25-09-20-neurips2025/"},{"title":"SafeVLA: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning","url":"https://papers.nips.cc/paper_files/paper/2025/hash/e185c7be603426028c32ae1003a59d78-Abstract-Conference.html"},{"title":"SafeVLA: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning | OpenReview","url":"https://openreview.net/forum?id=dt940loCBT"},{"title":"SafeVLA: Towards Safety Alignment of Vision-","url":"https://openreview.net/pdf?id=dt940loCBT"},{"title":"SafeVLA: Towards Safety Alignment of Vision-Language-Action Model via Safe Reinforcement Learning","url":"https://arxiv.org/html/2503.03480v1"},{"title":"NeurIPS Poster SafeVLA: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning","url":"https://neurips.cc/virtual/2025/poster/116975"},{"title":"[2503.03480] SafeVLA: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning","url":"https://arxiv.org/abs/2503.03480"}]

Based on the search results, here's information about SafeVLA:

## Overview
SafeVLA is a NeurIPS 2025 Spotlight paper on "Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning".

## Authors
The paper is authored by Borong Zhang, Yuhao Zhang, Jiaming Ji, Yingshan Lei, Josef Dai, Yuanpei Chen, and Yaodong Yang.

## Approach
SafeVLA uses an integrated safety approach (ISA) that sys
…[truncated 974 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 85 · 2026-05-23T03:06:17.598738+00:00_

Web search results for query: "Safety-Gymnasium unified safe reinforcement learning benchmark NeurIPS 2023 authors"

Links: [{"title":"Releases · PKU-Alignment/safety-gymnasium","url":"https://github.com/PKU-Alignment/safety-gymnasium/releases"},{"title":"Safety Gymnasium: A Unified Safe Reinforcement Learning Benchmark | OpenReview","url":"https://openreview.net/forum?id=WZmlxIuIGR"},{"title":"Safety-Gymnasium: A Unified Safe Reinforcement Learning Benchmark - ADS","url":"https://ui.adsabs.harvard.edu/abs/2023arXiv231012567J/abstract"},{"title":"safety-gymnasium/README.md at main · PKU-Alignment/safety-gymnasium","url":"https://github.com/PKU-Alignment/safety-gymnasium/blob/main/README.md"},{"title":"GitHub - PKU-Alignment/safety-gymnasium: NeurIPS 2023: Safety-Gymnasium: A Unified Safe Reinforcement Learning Benchmark · GitHub","url":"https://github.com/PKU-Alignment/safety-gymnasium"},{"title":"NeurIPS Poster Safety Gymnasium: A Unified Safe Reinforcement Learning Benchmark","url":"https://neurips.cc/virtual/2023/poster/73567"},{"title":"Safety-Gymnasium: A Unified Safe Reinforcement Learning Benchmark","url":"https://proceedings.neurips.cc/paper_files/paper/2023/file/3c557a3d6a48cc99444f85e924c66753-Paper-Datasets_and_Benchmarks.pdf"},{"title":"Safety-Gymnasium: A Unified Safe Reinforcement Learning Benchmark","url":"https://arxiv.org/pdf/2310.12567"},{"title":"[2310.12567] Safety-Gymnasium: A Unified Safe Reinforcement Learning Benchmark","url":"https://arxiv.org/abs/2310.12567"},{"title":"GitHub - PKU-Alignment/Safe-Policy-Optimization: NeurIPS 2023: Safe Policy Optimization: A benchmark repository for safe reinforcement learning algorithms · GitHub","url":"https://github.com/PKU-Alignment/Safe-Policy-Optimization"}]

Based on the search results, here are the authors of the Safety-Gymnasium paper published at NeurIPS 2023:

The authors are: Jiaming Ji, Borong Zhang, Jiayi Zhou, Xuehai Pan, Weidong Huang, Ruiyang Sun, Yiran Geng, Yifan Zhong, Josef Dai, and Yao
…[truncated 251 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool result

_source line 86 · 2026-05-23T03:06:17.598883+00:00_

Web search results for query: "arxiv 2512.11891 VLSA AEGIS authors venue 2025"

Links: [{"title":"[2512.11891] VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer","url":"https://arxiv.org/abs/2512.11891"},{"title":"GitHub - THU-RCSCT/vlsa-aegis: VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer","url":"https://github.com/THU-RCSCT/vlsa-aegis"},{"title":"VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer","url":"https://arxiv.org/html/2512.11891"},{"title":"Prompt injection attacks on vision-language models for surgical decision support","url":"https://www.medrxiv.org/content/10.1101/2025.07.16.25331645.full.pdf"},{"title":"VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer","url":"https://arxiv.org/pdf/2512.11891"},{"title":"Paper page - VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer","url":"https://huggingface.co/papers/2512.11891"}]

Based on the search results, here's the information about arxiv 2512.11891:

**Paper Title:** VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer

**ArXiv ID:** 2512.11891

**Authors:** Songqiao Hu, Zeyi Liu, Shuang Liu, Jun Cen, Zihan Meng, Xiao He

**Architecture Name:** AEGIS (a Vision-Language-Safe Action architecture with a plug-and-play safety constraint layer)

**Submission Date:** Submitted on 9 Dec 2025

**Venue/Year:** The paper is listed as a 2025 arXiv submission. The search results indicate this is an arXiv preprint published in 2025, but do not specify a particular conference venue yet.

**Summary:** The architecture is formulated via control barrier functions and integrates directly with existing VLA models to improve safety with theoretical guarantees, while maintaining their original instruction-following performance.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 87 · 2026-05-23T03:06:17.599029+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "iSDF real-time neural signed distance fields robot perception RSS 2022 Ortiz"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "tool_args": {
    "query": "iSDF real-time neural signed distance fields robot perception RSS 2022 Ortiz"
  }
}
```

</details>

---

### Tool call

_source line 88 · 2026-05-23T03:06:17.599162+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "overly conservative safe RL robot \"zero velocity\" OR \"standstill\" OR \"freezing\" OR \"stationary\" policy failure 2023 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "tool_args": {
    "query": "overly conservative safe RL robot \"zero velocity\" OR \"standstill\" OR \"freezing\" OR \"stationary\" policy failure 2023 2024 2025"
  }
}
```

</details>

---

### Tool result

_source line 89 · 2026-05-23T03:06:17.599291+00:00_

Web search results for query: "arxiv 2601.21712 CoFreeVLA authors 2026"

Links: [{"title":"CoFreeVLA: Collision-Free Dual-Arm Manipulation via Vision-Language-Action Model and Risk Estimation","url":"https://arxiv.org/html/2601.21712v2"},{"title":"CoFreeVLA: Collision-Free Dual-Arm Manipulation via Vision-Language-Action Model and Risk Estimation","url":"https://arxiv.org/pdf/2601.21712"},{"title":"Sample-Efficient Deep Learning for COVID-19 Diagnosis Based on CT Scans","url":"https://www.medrxiv.org/content/10.1101/2020.04.13.20063941.full.pdf"},{"title":"SP-VLA: A Joint Model Scheduling and Token Pruning Approach for VLA Model Acceleration","url":"https://arxiv.org/pdf/2506.12723"},{"title":"AIDCOV: An Interpretable Artificial Intelligence Model for Detection of COVID-19 from Chest Radiography Images","url":"https://www.medrxiv.org/content/10.1101/2020.05.24.20111922.full.pdf"}]

Based on the search results, I found the arxiv paper 2601.21712. The authors of CoFreeVLA are Xuanran Zhai, Binkai Ou, Qiaojun Yu, Ce Hao, and Yaohua Liu.

CoFreeVLA is a risk-aware VLA framework designed for collision-free dual-arm manipulation, and it was tested on five bimanual tasks with the PiPER robot arm. The paper was posted on February 3, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 90 · 2026-05-23T03:06:17.599447+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"representing robot geometry as distance fields\" whole-body manipulation 2024 Koptev"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"representing robot geometry as distance fields\" whole-body manipulation 2024 Koptev"
  }
}
```

</details>

---

### Tool result

_source line 91 · 2026-05-23T03:06:17.599585+00:00_

Web search results for query: "auxiliary loss safe reinforcement learning robot policy 2023 2024 2025"

Links: [{"title":"A Self-Supervised Auxiliary Loss for Deep RL in Partially Observable   Settings","url":"https://arxiv.org/pdf/2104.08492"},{"title":"Reinforcement Learning via Auxiliary Task Distillation","url":"https://arxiv.org/pdf/2406.17168"},{"title":"Reinforcement Learning with Automated Auxiliary Loss Search","url":"https://arxiv.org/pdf/2210.06041"},{"title":"Safe Learning in Robotics: From Learning-Based Control to Safe   Reinforcement Learning","url":"https://arxiv.org/pdf/2108.06266"},{"title":"Learning to Recover for Safe Reinforcement Learning","url":"https://arxiv.org/pdf/2309.11907"},{"title":"Loss is its own Reward: Self-Supervision for Reinforcement Learning","url":"https://arxiv.org/pdf/1612.07307"},{"title":"A Survey on Deep Reinforcement Learning Algorithms for Robotic Manipulation","url":"https://www.mdpi.com/1424-8220/23/7/3762"},{"title":"Certifiably-correct Control Policies for Safe Learning and Adaptation in   Assistive Robotics","url":"https://arxiv.org/pdf/2303.06582"},{"title":"Generating Auxiliary Tasks with Reinforcement Learning","url":"https://arxiv.org/pdf/2510.22940"}]

Based on the web search results, I found several relevant research papers on auxiliary losses in reinforcement learning and safe robot policy learning:

## Key Findings:

**Auxiliary Loss for Safe RL (2023):**
An auxiliary reward approach has been proposed to mitigate adversarial phenomena and help task policies learn to recover from high-risk states. This was tested in a robot navigation environment, demonstrating improvements in both reward gaining and constraint violations during task training.

**Automated Auxiliary Loss Search (2022):**
Research on automated auxiliary loss search discovered an approach called A2-winner that significantly improves performance on both high-dimensional image and low-dimensional vector unseen tasks. One main approach involves ad
…[truncated 1109 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "elapsed_ms": 4
}
```

</details>

---

### Tool call

_source line 92 · 2026-05-23T03:06:17.599738+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "VLSA AEGIS vision language action safety constraint layer CBF 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "tool_args": {
    "query": "VLSA AEGIS vision language action safety constraint layer CBF 2024 2025"
  }
}
```

</details>

---

### Tool call

_source line 93 · 2026-05-23T03:06:17.599866+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "safe diffusion policy robot collision avoidance degenerate solution frozen action 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "tool_args": {
    "query": "safe diffusion policy robot collision avoidance degenerate solution frozen action 2024 2025"
  }
}
```

</details>

---

### Tool call

_source line 94 · 2026-05-23T03:06:17.599992+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"pitfalls of imitation learning\" continuous actions mode averaging 2025 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"pitfalls of imitation learning\" continuous actions mode averaging 2025 arxiv"
  }
}
```

</details>

---

### Tool result

_source line 95 · 2026-05-23T03:06:17.600116+00:00_

Web search results for query: "CompliantVLA adaptor variable impedance VLA safe contact rich manipulation arXiv 2025"

Links: [{"title":"CompliantVLA-adaptor: VLM-Guided Variable Impedance Action for Safe Contact-Rich Manipulation","url":"https://arxiv.org/html/2601.15541v1"},{"title":"(PDF) CompliantVLA-adaptor: VLM-Guided Variable Impedance Action for Safe Contact-Rich Manipulation","url":"https://www.researchgate.net/publication/400002803_CompliantVLA-adaptor_VLM-Guided_Variable_Impedance_Action_for_Safe_Contact-Rich_Manipulation"},{"title":"[2601.15541] CompliantVLA-adaptor: VLM-Guided Variable Impedance Action for Safe Contact-Rich Manipulation","url":"https://arxiv.org/abs/2601.15541"},{"title":"CompliantVLA-adaptor: VLM-Guided Variable Impedance ...","url":"https://arxiv.org/pdf/2601.15541"},{"title":"OmniVIC: A Self-Improving Variable Impedance Controller with Vision-Language In-Context Learning for Safe Robotic Manipulation This work was supported by the Horizon Europe Project TORNADO (GA 101189557).","url":"https://arxiv.org/html/2510.17150"},{"title":"HapticVLA: Contact-Rich Manipulation via Vision-Language-Action Model without Inference-Time Tactile Sensing","url":"https://arxiv.org/html/2603.15257v1"}]

Based on the search results, I found the paper you're looking for:

CompliantVLA-adaptor augments VLA models with VLM-enhanced context-aware variable impedance control. The paper proposes a CompliantVLA-adaptor that augments state-of-the-art Vision-Language-Action (VLA) models with vision-language model (VLM)-informed context-aware variable impedance control (VIC) to improve the safety and effectiveness of contact-rich robotic manipulation tasks.

Existing VLA systems (e.g., RDT, Pi0.5, OpenVLA-oft) typically output position, but lack force-aware adaptation, leading to unsafe or failed interactions in physical tasks involving contact, compliance, or uncertainty. In the proposed CompliantVLA-adaptor, a VLM interprets task context from images and natural l
…[truncated 513 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 96 · 2026-05-23T03:06:17.600262+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Vision-Language-Action Safety: Threats Challenges Evaluations Mechanisms\" 2025 2026 authors arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Vision-Language-Action Safety: Threats Challenges Evaluations Mechanisms\" 2025 2026 authors arxiv"
  }
}
```

</details>

---

### Tool call

_source line 97 · 2026-05-23T03:06:17.600390+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "safe-control-gym benchmark safe learning control reinforcement learning robotics 2021 authors venue"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "tool_args": {
    "query": "safe-control-gym benchmark safe learning control reinforcement learning robotics 2021 authors venue"
  }
}
```

</details>

---

### Tool result

_source line 98 · 2026-05-23T03:06:17.600569+00:00_

Web search results for query: ""representing robot geometry as distance fields" whole-body manipulation 2024 Koptev"

Links: [{"title":"Representing Robot Geometry as Distance Fields: Applications to   Whole-body Manipulation","url":"https://arxiv.org/pdf/2307.00533"},{"title":"[PDF] Representing Robot Geometry as Distance Fields: Applications to Whole-body Manipulation | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Representing-Robot-Geometry-as-Distance-Fields:-to-Li-Zhang/e0cfb62fc1ce2f20c5b40e6174b172107f3d4ea0"},{"title":"Representing Robot Geometry as Distance Fields: Applications to Whole-body Manipulation | Request PDF","url":"https://www.researchgate.net/publication/382979799_Representing_Robot_Geometry_as_Distance_Fields_Applications_to_Whole-body_Manipulation"},{"title":"\\textcolorblackRepresenting Robot Geometry as Distance Fields: Applications to Whole-body Manipulation","url":"https://arxiv.org/html/2307.00533v3"},{"title":"Representing Robot Geometry as Distance Fields: Applications to Whole-body Manipulation - EU-Project IntelliMan","url":"https://intelliman-project.eu/publications/representing-robot-geometry-as-distance-fields-applications-to-whole-body-manipulation/"},{"title":"[2307.00533] Representing Robot Geometry as Distance Fields: Applications to Whole-body Manipulation","url":"https://arxiv.org/abs/2307.00533"},{"title":"Representing Robot Geometry as Distance Fields: Applications to Whole-body Manipulation | Article Information | J-GLOBAL","url":"https://jglobal.jst.go.jp/en/detail?JGLOBAL_ID=202402277837823674"},{"title":"(PDF) Learning Robot Geometry as Distance Fields: Applications to Whole-body Manipulation","url":"https://www.researchgate.net/publication/372074663_Learning_Robot_Geometry_as_Distance_Fields_Applications_to_Whole-body_Manipulation"}]

Based on the search results, I found information about the paper "Representing Robot Geometry as Distance Fields: Applications to Whole-body Manipulation."

The work pro
…[truncated 1082 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 99 · 2026-05-23T03:06:17.600725+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2503.03480 SafeVLA authors first author 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2503.03480 SafeVLA authors first author 2025"
  }
}
```

</details>

---

### Tool result

_source line 100 · 2026-05-23T03:06:17.600855+00:00_

Web search results for query: "VLSA AEGIS vision language action safety constraint layer CBF 2024 2025"

Links: [{"title":"(PDF) VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer","url":"https://www.researchgate.net/publication/398721287_VLSA_Vision-Language-Action_Models_with_Plug-and-Play_Safety_Constraint_Layer"},{"title":"[2512.11891] VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer","url":"https://arxiv.org/abs/2512.11891"},{"title":"VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer","url":"https://arxiv.org/pdf/2512.11891"},{"title":"VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer","url":"https://vlsa-aegis.github.io/"},{"title":"VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer [Quick Review]","url":"https://liner.com/review/vlsa-visionlanguageaction-models-with-plugandplay-safety-constraint-layer"},{"title":"VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer | Takara TLDR","url":"https://tldr.takara.ai/p/2512.11891"},{"title":"VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer","url":"https://arxiv.org/html/2512.11891v1"},{"title":"Paper page - VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer","url":"https://huggingface.co/papers/2512.11891"}]

I've successfully retrieved information about VLSA and AEGIS. Here's what the search found:

## Overview

The Vision-Language-Safe Action (VLSA) architecture, named AEGIS, contains a plug-and-play safety constraint (SC) layer formulated via control barrier functions.

## Purpose and Motivation

Vision-Language-Action (VLA) models have demonstrated remarkable capabilities in generalizing across diverse robotic manipulation tasks. However, deploying these models in unstructured environments remains challenging due to the critical need for simultaneous task compliance and safety assurance, p
…[truncated 1228 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 101 · 2026-05-23T03:06:17.601006+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "RAIL reachability-aided imitation learning safe policy execution 2024 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "tool_args": {
    "query": "RAIL reachability-aided imitation learning safe policy execution 2024 arxiv"
  }
}
```

</details>

---

### Tool result

_source line 102 · 2026-05-23T03:06:17.601141+00:00_

Web search results for query: "iSDF real-time neural signed distance fields robot perception RSS 2022 Ortiz"

Links: [{"title":"GitHub - facebookresearch/iSDF: Real-time Neural Signed Distance Fields for Robot Perception · GitHub","url":"https://github.com/facebookresearch/iSDF"},{"title":"GitHub - graygr/iSDF_ROB599: Real-time Neural Signed Distance Fields for Robot Perception","url":"https://github.com/graygr/iSDF_ROB599"},{"title":"[2204.02296] iSDF: Real-Time Neural Signed Distance Fields for Robot Perception","url":"https://arxiv.org/abs/2204.02296"},{"title":"iSDF: Real-Time Neural Signed Distance Fields for Robot ...","url":"https://joeaortiz.github.io/iSDF/"},{"title":"iSDF: Real-Time Neural Signed Distance Fields for Robot Perception - ADS","url":"https://ui.adsabs.harvard.edu/abs/2022arXiv220402296O/abstract"},{"title":"Robotics: Science and Systems XVIII - Online Proceedings","url":"https://www.roboticsproceedings.org/rss18/p012.html"},{"title":"iSDF: Real-Time Neural Signed Distance Fields for Robot Perception | Request PDF","url":"https://www.researchgate.net/publication/361714160_iSDF_Real-Time_Neural_Signed_Distance_Fields_for_Robot_Perception"},{"title":"iSDF: Real-Time Neural Signed Distance Fields for Robot Perception","url":"https://neural-implicit-workshop.stanford.edu/assets/pdf/ortiz.pdf"},{"title":"iSDF: Real-Time Neural Signed Distance Fields for Robot Perception","url":"https://arxiv.org/pdf/2204.02296"}]

Based on the search results, here's information about iSDF:

iSDF is a real-time system that reconstructs the signed distance field (SDF) of room scale environments through the online training of a neural SDF. The research was published by Joseph Ortiz, Alexander Clegg, and colleagues at Robotics: Science and Systems (RSS) in 2022.

**How it works:**

The model is represented by an MLP that is trained in a continual learning style from a live stream of posed depth images using a self-supervised loss. Given a stream of posed depth images fr
…[truncated 918 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 103 · 2026-05-23T03:06:17.601286+00:00_

Web search results for query: "overly conservative safe RL robot "zero velocity" OR "standstill" OR "freezing" OR "stationary" policy failure 2023 2024 2025"

Links: [{"title":"Reinforcement Learning Goal-Reaching Control with Guaranteed Lyapunov-Like Stabilizer for Mobile Robots","url":"https://arxiv.org/pdf/2601.19499"},{"title":"Learning Safe Autonomous Driving Policies Using Predictive Safety Representations","url":"https://arxiv.org/html/2512.17586v2"},{"title":"Conservative Safety Critics for Exploration","url":"https://arxiv.org/pdf/2010.14497"},{"title":"Safe Exploration in Continuous Action Spaces","url":"https://arxiv.org/pdf/1801.08757"},{"title":"Safe Reinforcement Learning with Contrastive Risk Prediction","url":"https://arxiv.org/pdf/2209.09648"},{"title":"Safe Learning in Robotics: From Learning-Based Control to Safe   Reinforcement Learning","url":"https://arxiv.org/pdf/2108.06266"},{"title":"POLICEd RL: Learning Closed-Loop Robot Control ...","url":"https://www.roboticsproceedings.org/rss20/p104.pdf"}]

The search results show several relevant papers on safe reinforcement learning for robotics from 2023-2025, though they don't all specifically focus on the "freezing" or "standstill" failure mode you mentioned. Here are the key findings:

## Relevant Papers Found:

1. **Lyapunov-Like Stabilizer for Mobile Robots (2025)**: A paper addressing the main challenge of integrating safety mechanisms with RL so that learning remains effective without becoming overly conservative. Results show the proposed approach improved goal-reaching rate from 84.6% to 99.0% while maintaining safe, conservative fallback behavior.

2. **Predictive Safety Representations for Autonomous Driving (2025)**: This work addresses a fundamental tension where overly conservative policies limit driving efficiency while aggressive exploration risks safety violations.

3. **Conservative Safety Critics for Exploration**: This paper targets the problem of safe exploration by learning a co
…[truncated 816 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 104 · 2026-05-23T03:06:17.601473+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"safety reward shaping\" auxiliary reward robot reinforcement learning 2023 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"safety reward shaping\" auxiliary reward robot reinforcement learning 2023 2024 2025"
  }
}
```

</details>

---

### Tool call

_source line 105 · 2026-05-23T03:06:17.601676+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "auxiliary task representation learning robot policy visuomotor manipulation 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "tool_args": {
    "query": "auxiliary task representation learning robot policy visuomotor manipulation 2024 2025"
  }
}
```

</details>

---

### Tool result

_source line 106 · 2026-05-23T03:06:17.601818+00:00_

Web search results for query: ""Vision-Language-Action Safety: Threats Challenges Evaluations Mechanisms" 2025 2026 authors arxiv"

Links: [{"title":"[2604.23775] Vision-Language-Action Safety: Threats, Challenges, Evaluations, and Mechanisms","url":"https://arxiv.org/abs/2604.23775"},{"title":"Vision-Language-Action Safety: Threats, Challenges, Evaluations, and Mechanisms","url":"https://arxiv.org/html/2604.23775v1"},{"title":"Paper page - Vision-Language-Action Safety: Threats, Challenges, Evaluations, and Mechanisms","url":"https://huggingface.co/papers/2604.23775"},{"title":"Concept-Based Dictionary Learning for Inference-Time Safety in Vision Language Action Models","url":"https://arxiv.org/pdf/2602.01834"},{"title":"Manipulation Facing Threats: Evaluating Physical Vulnerabilities in End-to-End Vision Language Action Models","url":"https://arxiv.org/pdf/2409.13174"},{"title":"ETA: Evaluating Then Aligning Safety of Vision Language Models at   Inference Time","url":"https://arxiv.org/pdf/2410.06625"},{"title":"Seeing the Threat: Vulnerabilities in Vision-Language Models to Adversarial Attack","url":"https://arxiv.org/pdf/2505.21967"},{"title":"HomeSafe-Bench: Evaluating Vision-Language Models on Unsafe Action Detection for Embodied Agents in Household Scenarios","url":"https://arxiv.org/pdf/2603.11975"}]

I found the paper you're looking for! Here are the details:

**Title:** Vision-Language-Action Safety: Threats, Challenges, Evaluations, and Mechanisms

**Primary Author:** &lt;cite index="1-10">Qi Li

**arXiv ID:** 2604.23775

**Upload Date:** April 26, 2026

**Overview:** Vision-Language-Action (VLA) models are emerging as a unified substrate for embodied intelligence. This shift raises a new class of safety challenges, stemming from the embodied nature of VLA systems, including irreversible physical consequences, a multimodal attack surface across vision, language, and state, real-time latency constraints on defense, error propagation over long-horizon trajecto
…[truncated 325 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 107 · 2026-05-23T03:06:17.601979+00:00_

Web search results for query: "safe-control-gym benchmark safe learning control reinforcement learning robotics 2021 authors venue"

Links: [{"title":"Safe Learning in Robotics: From Learning-Based Control to Safe Reinforcement Learning | Annual Reviews","url":"https://www.annualreviews.org/content/journals/10.1146/annurev-control-042920-020211"},{"title":"Safe-Control-Gym: A Unified Benchmark Suite for Safe Learning-Based Control and Reinforcement Learning in Robotics | Request PDF","url":"https://www.researchgate.net/publication/364083598_Safe-Control-Gym_A_Unified_Benchmark_Suite_for_Safe_Learning-Based_Control_and_Reinforcement_Learning_in_Robotics"},{"title":"[2109.06325] safe-control-gym: a Unified Benchmark Suite for Safe Learning-based Control and Reinforcement Learning in Robotics","url":"https://arxiv.org/abs/2109.06325"},{"title":"safe-control-gym: a Unified Benchmark Suite for Safe Learning-based   Control and Reinforcement Learning in Robotics","url":"https://arxiv.org/pdf/2109.06325"},{"title":"safe-control-gym: a Unified Benchmark Suite for Safe Learning-based Control and Reinforcement Learning - Paper Detail","url":"https://deeplearn.org/arxiv/233478/safe-control-gym:-a-unified-benchmark-suite-for-safe-learning-based-control-and-reinforcement-learning"},{"title":"GitHub - utiasDSL/safe-control-gym: PyBullet CartPole and Quadrotor environments—with CasADi symbolic a priori dynamics—for learning-based control and RL","url":"https://github.com/utiasDSL/safe-control-gym"},{"title":"Safe-Control-Gym: A Unified Benchmark Suite for Safe Learning-Based Control and Reinforcement Learning in Robotics - ADS","url":"https://ui.adsabs.harvard.edu/abs/2021arXiv210906325Y/abstract"},{"title":"[2109.06325] safe-control-gym: a Unified Benchmark Suite for Safe Learning-based Control and Reinforcement Learning in Robotics","url":"https://ar5iv.labs.arxiv.org/html/2109.06325"},{"title":"Safe-Control-Gym: A Unified Benchmark Suite for Safe Learning-Based Control and Rein
…[truncated 982 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 108 · 2026-05-23T03:06:17.602124+00:00_

Web search results for query: "arxiv 2503.03480 SafeVLA authors first author 2025"

Links: [{"title":"[2503.03480] SafeVLA: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning","url":"https://arxiv.org/abs/2503.03480"},{"title":"SafeVLA: Towards Safety Alignment of Vision-Language-Action Model via Safe Reinforcement Learning","url":"https://arxiv.org/html/2503.03480v1"},{"title":"(PDF) SafeVLA: Towards Safety Alignment of Vision-Language-Action Model via Safe Reinforcement Learning","url":"https://www.researchgate.net/publication/389616290_SafeVLA_Towards_Safety_Alignment_of_Vision-Language-Action_Model_via_Safe_Reinforcement_Learning"},{"title":"Concept-Based Dictionary Learning for Inference-Time Safety in Vision Language Action Models","url":"https://arxiv.org/pdf/2602.01834"},{"title":"SafeVLA: Towards Safety Alignment of Vision- Language-Action Model via Constrained Learning","url":"https://arxiv.org/html/2503.03480"},{"title":"GitHub - PKU-Alignment/SafeVLA: [NeurIPS 2025 Spotlight] Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning. · GitHub","url":"https://github.com/PKU-Alignment/SafeVLA"}]

Based on the search results, the first author of SafeVLA (arxiv 2503.03480) is Borong Zhang. 

The full author list includes: Borong Zhang, Yuhao Zhang, Jiaming Ji, Yingshan Lei, Josef Dai, Yuanpei Chen, and Yaodong Yang. The paper was submitted on March 5, 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 109 · 2026-05-23T03:06:17.602268+00:00_

Web search results for query: "safe diffusion policy robot collision avoidance degenerate solution frozen action 2024 2025"

Links: [{"title":"Discrete-Guided Diffusion for Scalable and Safe Multi-Robot Motion Planning","url":"https://arxiv.org/html/2508.20095v1"},{"title":"CAPE: Context-Aware Diffusion Policy Via Proximal Mode Expansion for Collision Avoidance","url":"https://arxiv.org/pdf/2511.22773"},{"title":"Dynamic Obstacle Avoidance through Uncertainty-Based Adaptive Planning   with Diffusion","url":"https://arxiv.org/pdf/2409.16950"},{"title":"Novel deep reinforcement learning based collision avoidance approach for path planning of robots in unknown environment | PLOS One","url":"https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0312559"},{"title":"LDP: A Local Diffusion Planner for Efficient Robot Navigation and   Collision Avoidance","url":"https://arxiv.org/pdf/2407.01950"},{"title":"Diffusion Policy: Visuomotor Policy Learning via Action Diffusion","url":"https://diffusion-policy.cs.columbia.edu/"},{"title":"Published as a conference paper at ICLR 2025 DIFFUSION-BASED PLANNING FOR","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/5c0cd43063f087eb32e572d040a19cd2-Paper-Conference.pdf"}]

I found several recent papers related to diffusion policies for robot collision avoidance. Here are the key findings:

## Recent Research on Diffusion-Based Robot Control

Diffusion models have gained significant attention in robotics for addressing multimodal trajectory generation in high-dimensional action spaces, with approaches like Diffusion Behavior Cloning and Diffusion Policy capable of generating full action sequences conditioned on robot observations and environment context.

### Specific Approaches:

1. **CAPE (Context-Aware Diffusion Policy)**: This method addresses collision avoidance scenarios where capturing diverse trajectory modes is essential, preserving task-consistent modes while expanding distributional support to produce
…[truncated 1015 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 110 · 2026-05-23T03:06:17.602436+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2307.00533 \"representing robot geometry as distance fields\" authors Li Zhang ICRA 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2307.00533 \"representing robot geometry as distance fields\" authors Li Zhang ICRA 2024"
  }
}
```

</details>

---

### Tool call

_source line 111 · 2026-05-23T03:06:17.602579+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"neural NMPC\" \"signed distance field\" collision avoidance Jacquet Harms Alexis 2025 IJRR"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"neural NMPC\" \"signed distance field\" collision avoidance Jacquet Harms Alexis 2025 IJRR"
  }
}
```

</details>

---

### Tool call

_source line 112 · 2026-05-23T03:06:17.602708+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "GUARD safe reinforcement learning benchmark venue publication AAAI NeurIPS 2024 Weiye Zhao Changliu Liu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "tool_args": {
    "query": "GUARD safe reinforcement learning benchmark venue publication AAAI NeurIPS 2024 Weiye Zhao Changliu Liu"
  }
}
```

</details>

---

### Tool result

_source line 113 · 2026-05-23T03:06:17.602837+00:00_

Web search results for query: ""pitfalls of imitation learning" continuous actions mode averaging 2025 arxiv"

Links: [{"title":"[PDF] The Pitfalls of Imitation Learning when Actions are Continuous | Semantic Scholar","url":"https://www.semanticscholar.org/paper/The-Pitfalls-of-Imitation-Learning-when-Actions-are-Simchowitz-Pfrommer/20085db39e8cdf3d13f6a1332a0d8049eee44454"},{"title":"[2503.09722] The Pitfalls of Imitation Learning when Actions are Continuous","url":"https://arxiv.org/abs/2503.09722"},{"title":"The Pitfalls of Imitation Learning when Actions are Continuous","url":"https://www.researchgate.net/publication/389820775_The_Pitfalls_of_Imitation_Learning_when_Actions_are_Continuous"},{"title":"Machine Learning Mar 2025 - stat.ML","url":"https://www.arxiv.org/list/stat.ML/2025-03?skip=275&show=50"},{"title":"The Pitfalls of Imitation Learning when Actions are Continuous Max Simchowitz*","url":"https://arxiv.org/pdf/2503.09722"},{"title":"Systems and Control Mar 2025","url":"https://www.arxiv.org/list/eess.SY/2025-03?skip=525&show=50"},{"title":"Imitation Learning in Continuous Action Spaces: Mitigating Compounding Error without Interaction","url":"https://arxiv.org/html/2507.09061v1"},{"title":"The Pitfalls of Imitation Learning when Actions are Continuous Max Simchowitz*","url":"https://www.arxiv.org/pdf/2503.09722v2"}]

Based on the search results, I found the paper you're looking for:

**Title:** "The Pitfalls of Imitation Learning when Actions are Continuous"

**Authors:** Max Simchowitz, Daniel Pfrommer, and Ali Jadbabaie

**Key Findings:**

Even if the dynamics satisfy a control-theoretic property called exponential stability (where the effects of perturbations decay exponentially quickly), and the expert is smooth and deterministic, any smooth, deterministic imitator policy necessarily suffers error on execution that is exponentially larger, as a function of problem horizon, than the error under the distribution of expert training data.

The negativ
…[truncated 829 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 114 · 2026-05-23T03:06:17.602992+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Robot Learning as an Empirical Science\" Kress-Gazit Hashimoto Burchfiel venue CoRL ICRA 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Robot Learning as an Empirical Science\" Kress-Gazit Hashimoto Burchfiel venue CoRL ICRA 2024 2025"
  }
}
```

</details>

---

### Tool result

_source line 115 · 2026-05-23T03:06:17.603129+00:00_

Web search results for query: "RAIL reachability-aided imitation learning safe policy execution 2024 arxiv"

Links: [{"title":"RAIL: Reachability-Aided Imitation Learning for Safe Policy Execution","url":"https://eurekamag.com/research/100/100/100100810.php"},{"title":"[2409.19190] RAIL: Reachability-Aided Imitation Learning for Safe Policy Execution","url":"https://arxiv.org/abs/2409.19190"},{"title":"RAIL: Reachability-Aided Imitation Learning for Safe Policy Execution","url":"https://arxiv.org/pdf/2409.19190"},{"title":"RAIL: Reachability-Aided Imitation Learning for Safe Policy Execution","url":"https://arxiv.org/html/2409.19190"},{"title":"RAIL: Reachability-Aided Imitation Learning for Safe Policy Execution","url":"https://rail2024.github.io/"},{"title":"[Literature Review] RAIL: Reachability-Aided Imitation Learning for Safe Policy Execution","url":"https://www.themoonlight.io/en/review/rail-reachability-aided-imitation-learning-for-safe-policy-execution"},{"title":"RAIL: Reachability-Aided Imitation Learning for Safe Policy Execution | IEEE Conference Publication | IEEE Xplore","url":"https://ieeexplore.ieee.org/iel8/11127273/11127223/11128656.pdf"},{"title":"RAIL: Reachability-Aided Imitation Learning for Safe Policy Execution | Request PDF","url":"https://www.researchgate.net/publication/395223354_RAIL_Reachability-Aided_Imitation_Learning_for_Safe_Policy_Execution"},{"title":"RAIL: Reachability-Aided Imitation Learning for Safe Policy Execution – The Safe Robotics Lab","url":"https://saferoboticslab.me.gatech.edu/research/rail/"}]

I found detailed information about RAIL: Reachability-Aided Imitation Learning for Safe Policy Execution. Here's what the search results show:

## Overview

RAIL is a paper by Wonsuhk Jung, Dennis Anthony, Utkarsh A. Mishra, Nadun Ranawaka Arachchige, Matthew Bronars, Danfei Xu, and Shreyas Kousik that addresses safety in imitation learning for robotics.

## Core Contribution

The paper builds a reachability-based safety filter
…[truncated 1259 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 116 · 2026-05-23T03:06:17.603286+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "safe RL \"trivial policy\" OR \"degenerate policy\" OR \"zero action\" robot constraint satisfaction 2023 2024 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "tool_args": {
    "query": "safe RL \"trivial policy\" OR \"degenerate policy\" OR \"zero action\" robot constraint satisfaction 2023 2024 2025 2026"
  }
}
```

</details>

---

### Tool result

_source line 117 · 2026-05-23T03:06:17.603439+00:00_

Web search results for query: "arxiv 2307.00533 "representing robot geometry as distance fields" authors Li Zhang ICRA 2024"

Links: [{"title":"[2307.00533] Representing Robot Geometry as Distance Fields: Applications to Whole-body Manipulation","url":"https://arxiv.org/abs/2307.00533"},{"title":"Representing Robot Geometry as Distance Fields:","url":"https://arxiv.org/pdf/2307.00533"},{"title":"\\textcolorblackRepresenting Robot Geometry as Distance Fields: Applications to Whole-body Manipulation","url":"https://arxiv.org/html/2307.00533v3"},{"title":"Representing Robot Geometry as Distance Fields: Applications to Whole-body Manipulation - EU-Project IntelliMan","url":"https://intelliman-project.eu/publications/representing-robot-geometry-as-distance-fields-applications-to-whole-body-manipulation/"},{"title":"(PDF) Learning Robot Geometry as Distance Fields: Applications to Whole-body Manipulation","url":"https://www.researchgate.net/publication/372074663_Learning_Robot_Geometry_as_Distance_Fields_Applications_to_Whole-body_Manipulation"},{"title":"[PDF] Representing Robot Geometry as Distance Fields: Applications to Whole-body Manipulation | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Representing-Robot-Geometry-as-Distance-Fields:-to-Li-Zhang/e0cfb62fc1ce2f20c5b40e6174b172107f3d4ea0"},{"title":"Representing Robot Geometry as Distance Fields: Applications to Whole-body Manipulation | Request PDF","url":"https://www.researchgate.net/publication/382979799_Representing_Robot_Geometry_as_Distance_Fields_Applications_to_Whole-body_Manipulation"},{"title":"A Riemannian Take on Distance Fields and Geodesic Flows in Robotics","url":"https://arxiv.org/pdf/2412.05197"},{"title":"Representing Robot Geometry as Distance Fields: Applications to Whole-body Manipulation | Article Information | J-GLOBAL","url":"https://jglobal.jst.go.jp/en/detail?JGLOBAL_ID=202402277837823674"},{"title":"Exploring Probabilistic Distance Fields in Robotics","url":"https://arxiv.
…[truncated 1082 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 118 · 2026-05-23T03:06:17.603596+00:00_

Web search results for query: ""safety reward shaping" auxiliary reward robot reinforcement learning 2023 2024 2025"

Links: [{"title":"Two-Layered Reward Reinforcement Learning in Humanoid Robot Motion Tracking","url":"https://www.mdpi.com/2227-7390/13/21/3445"},{"title":"Frontiers | HPRS: hierarchical potential-based reward shaping from task specifications","url":"https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2024.1444188/full"},{"title":"Highly Efficient Self-Adaptive Reward Shaping for Reinforcement Learning","url":"https://arxiv.org/html/2408.03029v1"},{"title":"Gain Tuning Is Not What You Need: Reward Gain Adaptation for Constrained Locomotion Learning","url":"https://arxiv.org/html/2510.10759v1"},{"title":"Comprehensive Overview of Reward Engineering and Shaping in Advancing Reinforcement Learning Applications","url":"https://arxiv.org/html/2408.10215v1"},{"title":"Learning to Recover for Safe Reinforcement Learning","url":"https://arxiv.org/pdf/2309.11907"},{"title":"HPRS: hierarchical potential-based reward shaping from task specifications","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11848067/"},{"title":"Reward Training Wheels: Adaptive Auxiliary Rewards for Robotics   Reinforcement Learning","url":"https://arxiv.org/pdf/2503.15724"}]

I've found several relevant research papers on safety reward shaping and auxiliary rewards in robot reinforcement learning from 2023-2025. Here are the key findings:

## Recent Research on Safety Reward Shaping and Auxiliary Rewards

**Adaptive Auxiliary Reward Methods:**
A teacher agent monitors training signals like success rate to assess student robot capability and adjust auxiliary reward weights, allowing the student to improve learning efficiency through adaptive auxiliary rewards. This approach has shown improvements of 2.35% in navigation success rates and 122.62% in off-road mobility performance, with physical robot experiments achieving perfect success rates.

**Safety-Focused 
…[truncated 1134 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 119 · 2026-05-23T03:06:17.603747+00:00_

Web search results for query: "auxiliary task representation learning robot policy visuomotor manipulation 2024 2025"

Links: [{"title":"AimBot: A Simple Auxiliary Visual Cue to Enhance Spatial Awareness of Visuomotor Policies","url":"https://arxiv.org/html/2508.08113v1"},{"title":"Diffusion policy: Visuomotor policy learning via action diffusion","url":"https://www.researchgate.net/publication/384857010_Diffusion_policy_Visuomotor_policy_learning_via_action_diffusion"},{"title":"Robust Visuomotor Control for Humanoid Loco-Manipulation Using Hybrid Reinforcement Learning - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12292580/"},{"title":"[PDF] Diffusion policy: Visuomotor policy learning via action diffusion | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Diffusion-policy:-Visuomotor-policy-learning-via-Chi-Feng/bdba3bd30a49ea4c5b20b43dbd8f0eb59e9d80e2"},{"title":"Diffusion policy: : Visuomotor policy learning via action diffusion: International Journal of Robotics Research: Vol 44, No 10-11","url":"https://dl.acm.org/doi/10.1177/02783649241273668"},{"title":"Spatial Policy: Guiding Visuomotor Robotic Manipulation with Spatial-Aware Modeling and Reasoning","url":"https://arxiv.org/html/2508.15874v1"}]

The search has returned several relevant results on auxiliary task representation learning for robot policy and visuomotor manipulation from 2024-2025:

## Key Recent Works

AimBot is a lightweight visual augmentation technique that provides explicit spatial cues to improve visuomotor policy learning in robotic manipulation.

Diffusion Policy represents a robot's visuomotor policy as a conditional denoising diffusion process, and Crossway Diffusion enhances diffusion-based visuomotor policy learning via a state decoder and an auxiliary reconstruction objective.

Spatial Policy outperforms prior methods by over 30%, demonstrating the effectiveness of spatial reasoning in visuomotor robotic manipulation. Vision-based methods, known as visuomoto
…[truncated 765 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 120 · 2026-05-23T03:06:17.603896+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "POLICEd RL closed-loop robot control safety constraints RSS 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "tool_args": {
    "query": "POLICEd RL closed-loop robot control safety constraints RSS 2024"
  }
}
```

</details>

---

### Tool result

_source line 121 · 2026-05-23T03:06:17.604029+00:00_

Web search results for query: "GUARD safe reinforcement learning benchmark venue publication AAAI NeurIPS 2024 Weiye Zhao Changliu Liu"

Links: [{"title":"GUARD: A Safe Reinforcement Learning Benchmark","url":"https://arxiv.org/pdf/2305.13681"},{"title":"GitHub - bitzhangcy/Safe-Deep-Reinforcement-Learning · GitHub","url":"https://github.com/bitzhangcy/Safe-Deep-Reinforcement-Learning"},{"title":"[2305.13681] GUARD: A Safe Reinforcement Learning Benchmark","url":"https://arxiv.org/abs/2305.13681"},{"title":"GUARD: A Safe Reinforcement Learning Benchmark","url":"https://arxiv.org/html/2305.13681v4"},{"title":"Probabilistic Safeguard for Reinforcement Learning Using Safety Index Guided Gaussian Process Models","url":"https://proceedings.mlr.press/v211/zhao23a.html"},{"title":"Safety-Gymnasium: A Unified Safe Reinforcement Learning Benchmark","url":"https://arxiv.org/pdf/2310.12567"},{"title":"AutoCost: Evolving Intrinsic Cost for Zero-Violation Reinforcement Learning | Proceedings of the AAAI Conference on Artificial Intelligence","url":"https://ojs.aaai.org/index.php/AAAI/article/view/26734"}]

Based on the search results, I found information about GUARD. Here's what I discovered:

GUARD is a Generalized Unified SAfe Reinforcement Learning Development Benchmark, developed by Weiye Zhao, Ruixuan Liu, Rui Chen, Tianhao Wei, Yifan Sun, and Changliu Liu from the Robotics Institute at Carnegie Mellon University.

GUARD is a safe reinforcement learning benchmark published on arXiv in 2023. The paper appears on the arXiv preprint server with ID 2305.13681, dated May 23, 2023.

However, regarding the venue publication inquiry (AAAI or NeurIPS 2024), the search results indicate that GUARD was published as an arXiv preprint rather than at a major conference venue like AAAI or NeurIPS in 2024. I did not find evidence in these search results that GUARD was published at AAAI 2024 or NeurIPS 2024.


REMINDER: You MUST include the sources above in your response to the user using ma
…[truncated 18 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 122 · 2026-05-23T03:06:17.604186+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Learning to Recover\" safe reinforcement learning auxiliary reward recovery policy 2023 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Learning to Recover\" safe reinforcement learning auxiliary reward recovery policy 2023 arxiv"
  }
}
```

</details>

---

### Tool result

_source line 123 · 2026-05-23T03:06:17.604316+00:00_

Web search results for query: ""neural NMPC" "signed distance field" collision avoidance Jacquet Harms Alexis 2025 IJRR"

Links: [{"title":"GitHub - ntnu-arl/sdf-nmpc","url":"https://github.com/ntnu-arl/sdf-nmpc"},{"title":"Neural NMPC through signed distance field encoding for collision avoidance - Martin Jacquet, Marvin Harms, Kostas Alexis, 2025","url":"https://journals.sagepub.com/doi/10.1177/02783649251401223"},{"title":"Neural NMPC through Signed Distance Field Encoding for Collision Avoidance","url":"https://arxiv.org/pdf/2511.21312"},{"title":"Neural SDF-MPC (NMPC) - Unified Autonomy Stack","url":"https://ntnu-arl.github.io/unified_autonomy_stack/nmpc/"},{"title":"Neural NMPC through Signed Distance Field Encoding for Collision Avoidance","url":"https://arxiv.org/html/2511.21312"},{"title":"[2511.21312] Neural NMPC through Signed Distance Field Encoding for Collision Avoidance","url":"https://arxiv.org/abs/2511.21312"},{"title":"N-MPC for Deep Neural Network-Based Collision Avoidance exploiting Depth Images | Request PDF","url":"https://www.researchgate.net/publication/382984469_N-MPC_for_Deep_Neural_Network-Based_Collision_Avoidance_exploiting_Depth_Images"},{"title":"(PDF) Neural NMPC through Signed Distance Field Encoding for Collision Avoidance","url":"https://www.researchgate.net/publication/398025684_Neural_NMPC_through_Signed_Distance_Field_Encoding_for_Collision_Avoidance"}]

I found the paper you're searching for! Here's what I found:

"Neural NMPC through Signed Distance Field Encoding for Collision Avoidance" by Jacquet, Martin and Harms, Marvin and Alexis, Kostas was published in The International Journal of Robotics Research in 2025 with DOI 10.1177/02783649251401223.

The paper introduces a neural nonlinear model predictive control (NMPC) framework for mapless, collision-free navigation in unknown environments with Aerial Robots, using onboard range sensing. The framework leverages deep neural networks to encode a single range image into a sign
…[truncated 754 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 124 · 2026-05-23T03:06:17.604492+00:00_

Web search results for query: ""Robot Learning as an Empirical Science" Kress-Gazit Hashimoto Burchfiel venue CoRL ICRA 2024 2025"

Links: [{"title":"dblp: Benjamin Burchfiel","url":"https://dblp.uni-trier.de/pid/136/9247.html"},{"title":"(PDF) Robot Learning as an Empirical Science: Best Practices for Policy Evaluation","url":"https://www.researchgate.net/publication/384075741_Robot_Learning_as_an_Empirical_Science_Best_Practices_for_Policy_Evaluation"},{"title":"Robot Learning as an Empirical Science: Best Practices for Policy Evaluation","url":"https://bibbase.org/network/publication/kressgazit-hashimoto-kuppuswamy-shah-horgan-richardson-feng-burchfiel-robotlearningasanempiricalsciencebestpracticesforpolicyevaluation-2024"},{"title":"Robot Learning as an Empirical Science: Best Practices for Policy Evaluation","url":"https://arxiv.org/html/2409.09491"},{"title":"[2409.09491] Robot Learning as an Empirical Science: Best Practices for Policy Evaluation","url":"https://arxiv.org/abs/2409.09491"},{"title":"A careful examination of large behavior models for multitask dexterous manipulation | Science Robotics","url":"https://www.science.org/doi/10.1126/scirobotics.aea6201"},{"title":"A review of robot learning for manipulation: challenges, representations, and algorithms: The Journal of Machine Learning Research: Vol 22, No 1","url":"https://dl.acm.org/doi/abs/10.5555/3546258.3546288"},{"title":"Robot Learning as an Empirical Science: Best Practices for Policy   Evaluation","url":"https://arxiv.org/pdf/2409.09491"}]

Based on the search results, I found the paper you're looking for:

**"Robot Learning as an Empirical Science: Best Practices for Policy Evaluation"** by Hadas Kress-Gazit, Kunimatsu Hashimoto, Naveen Kuppuswamy, Paarth Shah, Phoebe Horgan, Gordon Richardson, Siyuan Feng, and Benjamin Burchfiel.

**Venue:** The paper was published on CoRR (arXiv) in 2024, specifically with initial submission on September 14, 2024. The search results do not indicate it was 
…[truncated 732 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 125 · 2026-05-23T03:06:17.604652+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Reward Training Wheels\" adaptive auxiliary rewards robotics reinforcement learning 2025 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Reward Training Wheels\" adaptive auxiliary rewards robotics reinforcement learning 2025 arxiv"
  }
}
```

</details>

---

### Tool call

_source line 126 · 2026-05-23T03:06:17.604784+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "differentiable constrained imitation learning robot motion planning control collision 2023 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "tool_args": {
    "query": "differentiable constrained imitation learning robot motion planning control collision 2023 2024"
  }
}
```

</details>

---

### Tool result

_source line 127 · 2026-05-23T03:06:17.604913+00:00_

Web search results for query: "POLICEd RL closed-loop robot control safety constraints RSS 2024"

Links: [{"title":"POLICEd RL - ICON Lab - Negar Mehr","url":"https://iconlab.negarmehr.com/POLICEd-RL/"},{"title":"POLICEd RL: Learning Closed-Loop Robot Control Policies with Provable Satisfaction of Hard Constraints","url":"https://arxiv.org/html/2403.13297v3"},{"title":"POLICEd-RL: Learning Closed-Loop Robot Control ...","url":"https://github.com/labicon/POLICEd-RL"},{"title":"RSS 2024 Workshop - Schedule","url":"https://sites.google.com/view/rss2024-safe-autonomy/schedule"},{"title":"POLICEd RL: Learning Closed-Loop Robot Control ...","url":"https://arxiv.org/pdf/2403.13297"},{"title":"[2403.13297] POLICEd RL: Learning Closed-Loop Robot Control Policies with Provable Satisfaction of Hard Constraints","url":"https://arxiv.org/abs/2403.13297"},{"title":"RSS 2024 Workshop - Accepted Papers","url":"https://sites.google.com/view/rss2024-safe-autonomy/accepted-papers"},{"title":"POLICEd RL: Learning Closed-Loop Robot Control Policies with Provable Satisfaction of Hard Constraints | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/policed-rl-learning-closed-loop-robot-control"},{"title":"Robotics: Science and Systems 2024 Delft, Netherlands, July 15-July 19, 2024","url":"https://par.nsf.gov/servlets/purl/10566685"},{"title":"POLICEd RL: Learning Closed-Loop Robot Control ...","url":"https://www.roboticsproceedings.org/rss20/p104.pdf"}]

Based on the search results, here's information about POLICEd RL:

## Overview

POLICEd RL is a novel RL algorithm explicitly designed to enforce affine hard constraints in closed-loop with a black-box environment. The work was presented at Robotics: Science and Systems (RSS) 2024 by Jean-Baptiste Bouvier, Kartik Nagpal, and Negar Mehr.

## Problem and Solution

The paper seeks to learn a robot policy guaranteed to satisfy state constraints, while existing RL algorithms typically rely on Constrained Markov Decision Pr
…[truncated 845 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 128 · 2026-05-23T03:06:17.605073+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2512.11891 VLSA authors list"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2512.11891 VLSA authors list"
  }
}
```

</details>

---

### Tool call

_source line 129 · 2026-05-23T03:06:17.605204+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "iSDF real-time neural signed distance fields Ortiz Clegg Dong Sucar RSS 2022 authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "tool_args": {
    "query": "iSDF real-time neural signed distance fields Ortiz Clegg Dong Sucar RSS 2022 authors"
  }
}
```

</details>

---

### Tool result

_source line 130 · 2026-05-23T03:06:17.605333+00:00_

Web search results for query: "safe RL "trivial policy" OR "degenerate policy" OR "zero action" robot constraint satisfaction 2023 2024 2025 2026"

Links: [{"title":"Constrained Variational Policy Optimization for Safe Reinforcement   Learning","url":"https://arxiv.org/pdf/2201.11927"},{"title":"Safe Exploration in Continuous Action Spaces","url":"https://arxiv.org/pdf/1801.08757"},{"title":"Accelerating Safe Reinforcement Learning with Constraint-mismatched   Policies","url":"https://arxiv.org/pdf/2006.11645"},{"title":"Learning Policies with Zero or Bounded Constraint Violation for   Constrained MDPs","url":"https://arxiv.org/pdf/2106.02684"},{"title":"Published as a conference paper at ICLR 2026 SAFE EXPLORATION VIA POLICY PRIORS","url":"https://arxiv.org/pdf/2601.19612"},{"title":"Learn Zero-Constraint-Violation Policy in Model-Free Constrained   Reinforcement Learning","url":"https://arxiv.org/pdf/2111.12953"},{"title":"A Survey of Safe Reinforcement Learning and Constrained MDPs: A Technical Survey on Single-Agent and Multi-Agent Safety","url":"https://arxiv.org/html/2505.17342v1"},{"title":"[2310.03718] Constraint-Conditioned Policy Optimization for Versatile Safe Reinforcement Learning","url":"https://arxiv.org/abs/2310.03718"}]

Based on the web search results, I found relevant research on safe reinforcement learning with constraint satisfaction, though the specific terminology you mentioned (trivial policy, degenerate policy, zero action) doesn't appear prominently in these results. Here's what I found:

## Key Safe RL Research (2023-2026)

Recent work has designed safe RL algorithms that can achieve regret bounds while guaranteeing zero or bounded safety constraint violation with arbitrarily high probability.

One notable approach addresses how to learn safe policies without enough data about dangerous regions by identifying dangerous actions prior to taking them and obtaining zero constraint-violation policies after convergence.

Safe reinforcement learn
…[truncated 1138 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 131 · 2026-05-23T03:06:17.605528+00:00_

Web search results for query: ""Learning to Recover" safe reinforcement learning auxiliary reward recovery policy 2023 arxiv"

Links: [{"title":"[2309.11907] Learning to Recover for Safe Reinforcement Learning","url":"https://arxiv.org/abs/2309.11907"},{"title":"Learning to Recover for Safe Reinforcement Learning","url":"https://arxiv.org/pdf/2309.11907"},{"title":"Learning to Recover for Safe Reinforcement Learning","url":"https://arxiv.org/html/2309.11907v1"},{"title":"Safe Reinforcement Learning via Recovery-based Shielding with","url":"https://www.arxiv.org/pdf/2602.12444"},{"title":"Skill-based Safe Reinforcement Learning with Risk Planning","url":"https://arxiv.org/html/2505.01619"},{"title":"[2306.13944] Safe Reinforcement Learning with Dead-Ends Avoidance and Recovery","url":"https://arxiv.org/abs/2306.13944"},{"title":"Safe Reinforcement Learning with Dead-Ends Avoidance and Recovery","url":"https://arxiv.org/html/2306.13944"},{"title":"Safe Reinforcement Learning with Dead-Ends Avoidance and Recovery","url":"https://arxiv.org/pdf/2306.13944"}]

Based on the search results, I found the paper you're looking for:

**Title:** Learning to Recover for Safe Reinforcement Learning

**Key Details:**
- **ArXiv ID:** 2309.11907
- **Publication Date:** September 21, 2023
- **Authors:** Haoyu Wang and colleagues

**Main Contributions:**

The paper proposes a three-stage architecture for safe reinforcement learning called TU-Recovery Architecture, where a safety critic and a recovery policy are learned before task training to form a safety controller that ensures safety during task training.

The paper describes an "adversarial phenomenon" induced by disagreement between task policy and recovery policy that reduces learning efficiency and model performance, and proposes auxiliary reward to mitigate this phenomenon while helping the task policy learn to recover from high-risk states.

**Experimental Results:**
Experiments demonstrate that TU-Recovery outperforms unconstr
…[truncated 382 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 132 · 2026-05-23T03:06:17.605751+00:00_

Web search results for query: ""Reward Training Wheels" adaptive auxiliary rewards robotics reinforcement learning 2025 arxiv"

Links: [{"title":"[Literature Review] Reward Training Wheels: Adaptive Auxiliary Rewards for Robotics Reinforcement Learning","url":"https://www.themoonlight.io/en/review/reward-training-wheels-adaptive-auxiliary-rewards-for-robotics-reinforcement-learning"},{"title":"[PDF] Reward Training Wheels: Adaptive Auxiliary Rewards for Robotics Reinforcement Learning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Reward-Training-Wheels:-Adaptive-Auxiliary-Rewards-Wang-Xu/64ec23efb72aba3027c1406c6c30f5a118c4181e"},{"title":"[2503.15724] Reward Training Wheels: Adaptive Auxiliary Rewards for Robotics Reinforcement Learning","url":"https://arxiv.org/abs/2503.15724"},{"title":"Reward Training Wheels: Adaptive Auxiliary Rewards for Robotics   Reinforcement Learning","url":"https://arxiv.org/pdf/2503.15724"},{"title":"Reward Training Wheels: Adaptive Auxiliary Rewards for Robotics Reinforcement Learning","url":"https://arxiv.org/html/2503.15724v1"},{"title":"Reward Training Wheels: Adaptive Auxiliary Rewards for","url":"https://people.cs.gmu.edu/~xxiao2/papers/rtw.pdf"}]

Based on the search results, I found comprehensive information about the paper on Reward Training Wheels:

## Overview

Reward Training Wheels (RTW) is a teacher-student framework that automates auxiliary reward adaptation for robotics RL. The paper addresses the challenge that robotics RL often relies on carefully engineered auxiliary rewards to supplement sparse primary learning objectives to compensate for the lack of large-scale, real-world, trial-and-error data.

## Key Innovation

The RTW teacher dynamically adjusts auxiliary reward weights based on the student's evolving capabilities to determine which auxiliary reward aspects require more or less emphasis to improve the primary objective. While auxiliary rewards accelerate learning, they require significant eng
…[truncated 1110 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 133 · 2026-05-23T03:06:17.605921+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "FISOR feasibility safe offline RL zero violation conservative policy 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "tool_args": {
    "query": "FISOR feasibility safe offline RL zero violation conservative policy 2024 2025"
  }
}
```

</details>

---

### Tool call

_source line 134 · 2026-05-23T03:06:17.606056+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CAPE diffusion policy mode expansion collision avoidance robot manipulation 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CAPE diffusion policy mode expansion collision avoidance robot manipulation 2025"
  }
}
```

</details>

---

### Tool result

_source line 135 · 2026-05-23T03:06:17.606180+00:00_

Web search results for query: "arxiv 2512.11891 VLSA authors list"

Links: [{"title":"[2512.11891] VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer","url":"https://arxiv.org/abs/2512.11891"},{"title":"(PDF) VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer","url":"https://www.researchgate.net/publication/398721287_VLSA_Vision-Language-Action_Models_with_Plug-and-Play_Safety_Constraint_Layer"},{"title":"GitHub - THU-RCSCT/vlsa-aegis: VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer","url":"https://github.com/THU-RCSCT/vlsa-aegis"},{"title":"Paper page - VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer","url":"https://huggingface.co/papers/2512.11891"},{"title":"VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer","url":"https://arxiv.org/html/2512.11891"},{"title":"VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer","url":"https://arxiv.org/pdf/2512.11891"}]

The authors of arxiv paper 2512.11891 (VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer) are: Songqiao Hu, Zeyi Liu, Shuang Liu, Jun Cen, Zihan Meng, and Xiao He.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 136 · 2026-05-23T03:06:17.606319+00:00_

Web search results for query: "differentiable constrained imitation learning robot motion planning control collision 2023 2024"

Links: [{"title":"Differentiable Constrained Imitation Learning for Robot Motion Planning   and Control","url":"https://arxiv.org/pdf/2210.11796"},{"title":"[2210.11796] Differentiable Constrained Imitation Learning for Robot Motion Planning and Control","url":"https://arxiv.org/abs/2210.11796"},{"title":"Differentiable Constrained Imitation Learning for Robot Motion Planning and Control - RST - TU Dortmund","url":"https://rst.etit.tu-dortmund.de/en/news-detail/differentiable-constrained-imitation-learning-for-robot-motion-planning-and-control-29480/"},{"title":"Generating Stable and Collision-Free Policies through Lyapunov Function   Learning","url":"https://arxiv.org/pdf/2211.08976"},{"title":"Method of robot dynamic motion planning and control","url":"https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12151379"},{"title":"I-CTRL: Imitation to Control Humanoid Robots Through Constrained   Reinforcement Learning","url":"https://arxiv.org/pdf/2405.08726"}]

I found several relevant papers on differentiable constrained imitation learning for robot motion planning and control. Here are the key results:

## Primary Result

The most directly relevant work is "Differentiable Constrained Imitation Learning for Robot Motion Planning and Control" by Christopher Diehl, Janis Adamek, Martin Krüger, Frank Hoffmann and Torsten Bertram. The approach addresses spatio-temporal hard constraints like system dynamics and safety boundaries (e.g., obstacles in automated driving) that restrict robot motions.

## Key Contributions

This work integrates the flexibility of imitation learning with hard constraint handling in optimal control, with hard constraints integrated into the learning problem in a differentiable manner, via explicit completion and gradient-based correction. Unlike prior work that primarily relied on soft-constraint approaches 
…[truncated 632 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 137 · 2026-05-23T03:06:17.606496+00:00_

Web search results for query: "iSDF real-time neural signed distance fields Ortiz Clegg Dong Sucar RSS 2022 authors"

Links: [{"title":"iSDF | RSS 2022 Talk | Real-Time Neural Signed Distance Fields for Robot Perception - YouTube","url":"https://www.youtube.com/watch?v=QffGi9XUt1M"},{"title":"GitHub - facebookresearch/iSDF: Real-time Neural Signed Distance Fields for Robot Perception · GitHub","url":"https://github.com/facebookresearch/iSDF"},{"title":"GitHub - graygr/iSDF_ROB599: Real-time Neural Signed Distance Fields for Robot Perception","url":"https://github.com/graygr/iSDF_ROB599"},{"title":"Robotics: Science and Systems XVIII - Online Proceedings","url":"https://www.roboticsproceedings.org/rss18/p012.html"},{"title":"iSDF: Real-Time Neural Signed Distance Fields for Robot Perception | Request PDF","url":"https://www.researchgate.net/publication/361714160_iSDF_Real-Time_Neural_Signed_Distance_Fields_for_Robot_Perception"},{"title":"iSDF: Real-Time Neural Signed Distance Fields for Robot ...","url":"https://joeaortiz.github.io/iSDF/"},{"title":"[2204.02296] iSDF: Real-Time Neural Signed Distance Fields for Robot Perception","url":"https://arxiv.org/abs/2204.02296"},{"title":"iSDF: Real-Time Neural Signed Distance Fields for Robot Perception - ADS","url":"https://ui.adsabs.harvard.edu/abs/2022arXiv220402296O/abstract"},{"title":"iSDF: Real-Time Neural Signed Distance Fields for Robot Perception","url":"https://arxiv.org/pdf/2204.02296"},{"title":"iSDF: Real-Time Neural Signed Distance Fields for Robot ...","url":"https://www.roboticsproceedings.org/rss18/p012.pdf"}]

Based on the search results, I found comprehensive information about the iSDF paper:

## iSDF: Real-Time Neural Signed Distance Fields for Robot Perception

**Authors:** Joseph Ortiz, Alexander Clegg, Jing Dong, Edgar Sucar, David Novotny, Michael Zollhoefer, and Mustafa Mukadam

**Publication:** Published in Robotics: Science and Systems (RSS) 2022

**Overview:** iSDF is a continual learning system
…[truncated 866 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 138 · 2026-05-23T03:06:17.606649+00:00_

Web search results for query: "FISOR feasibility safe offline RL zero violation conservative policy 2024 2025"

Links: [{"title":"[2401.10700] Safe Offline Reinforcement Learning with Feasibility-Guided Diffusion Model","url":"https://arxiv.org/abs/2401.10700"},{"title":"Safe Offline Reinforcement Learning with Feasibility-Guided Diffusion Model | Papers With Code","url":"https://paperswithcode.com/paper/safe-offline-reinforcement-learning-with"},{"title":"Safe Offline Reinforcement Learning with Feasibility-Guided Diffusion   Model","url":"https://arxiv.org/pdf/2401.10700"},{"title":"Safe Offline Reinforcement Learning with Feasibility-Guided Diffusion Model | OpenReview","url":"https://openreview.net/forum?id=j5JvZCaDM0"},{"title":"FISOR - Yinan Zheng","url":"https://zhengyinan-air.github.io/FISOR/"},{"title":"[PDF] Safe Offline Reinforcement Learning with Feasibility-Guided Diffusion Model | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Safe-Offline-Reinforcement-Learning-with-Diffusion-Zheng-Li/a2246e09ab0b56ba91322747addad030eae56c50"},{"title":"SAFE OFFLINE REINFORCEMENT LEARNING WITH ...","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/10a3b1c30b8cceb507b9e8ddcc9a1a6a-Paper-Conference.pdf"},{"title":"Safe Offline Reinforcement Learning with Feasibility-Guided Diffusion Model","url":"https://arxiv.org/html/2401.10700v1"},{"title":"ICLR Poster Safe Offline Reinforcement Learning with Feasibility-Guided Diffusion Model","url":"https://iclr.cc/virtual/2024/poster/18038"}]

The search has returned comprehensive results about FISOR (Feasibility-guided Safe Offline RL). Here are the key findings:

## Overview
FISOR is a method that allows safety constraint adherence, reward maximization, and offline policy learning to be realized via three decoupled processes, while offering strong safety performance and stability.

## Key Problem It Addresses
Previous safe offline RL methods adopted soft constraints that only required constraint viol
…[truncated 970 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 139 · 2026-05-23T03:06:17.606804+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "signed distance field SDF loss robot policy learning collision avoidance manipulation 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "tool_args": {
    "query": "signed distance field SDF loss robot policy learning collision avoidance manipulation 2024 2025"
  }
}
```

</details>

---

### Tool call

_source line 140 · 2026-05-23T03:06:17.606938+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"differentiable constrained imitation learning\" Diehl robot motion planning venue published 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"differentiable constrained imitation learning\" Diehl robot motion planning venue published 2023"
  }
}
```

</details>

---

### Tool result

_source line 141 · 2026-05-23T03:06:17.607067+00:00_

Web search results for query: "CAPE diffusion policy mode expansion collision avoidance robot manipulation 2025"

Links: [{"title":"[2511.22773] CAPE: Context-Aware Diffusion Policy Via Proximal Mode Expansion for Collision Avoidance","url":"https://arxiv.org/abs/2511.22773"},{"title":"CAPE: Context-Aware Diffusion Policy Via Proximal Mode Expansion for Collision Avoidance","url":"https://arxiv.org/pdf/2511.22773"},{"title":"CAPE: Context-Aware Diffusion Policy Via Proximal Mode Expansion for Collision Avoidance","url":"https://arxiv.org/html/2511.22773v1"},{"title":"RA-DP: Rapid Adaptive Diffusion Policy for Training-Free High-frequency Robotics Replanning","url":"https://www.researchgate.net/publication/398060109_RA-DP_Rapid_Adaptive_Diffusion_Policy_for_Training-Free_High-frequency_Robotics_Replanning"},{"title":"Language-Guided Object-Centric Diffusion Policy for Generalizable and   Collision-Aware Robotic Manipulation","url":"https://arxiv.org/pdf/2407.00451"}]

I found research on CAPE (Context-Aware diffusion policy via Proximal mode Expansion). Here are the key findings:

## Overview

CAPE is a framework that expands trajectory distribution modes with context-aware prior and guidance at inference via a novel prior-seeded iterative guided refinement procedure.

## How It Works

The framework generates an initial trajectory plan and executes a short prefix trajectory, then the remaining trajectory segment is perturbed to an intermediate noise level, forming a trajectory prior that is context-aware and preserves task intent. Repeating the process with context-aware guided denoising iteratively expands mode support to allow finding smoother, less collision-prone trajectories.

## Collision Avoidance Capability

For collision avoidance, CAPE expands trajectory distribution modes with collision-aware context, enabling the sampling of collision-free trajectories in previously unseen environments while maintaining goal consistency.

## Performance Results

CAPE achi
…[truncated 513 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 142 · 2026-05-23T03:06:17.607215+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv \"learning on one mode\" weighted imitation learning LOM authors robot manipulation ICLR 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv \"learning on one mode\" weighted imitation learning LOM authors robot manipulation ICLR 2025"
  }
}
```

</details>

---

### Tool call

_source line 143 · 2026-05-23T03:06:17.607352+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2601.19612 \"safe exploration via policy priors\" ICLR 2026 authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2601.19612 \"safe exploration via policy priors\" ICLR 2026 authors"
  }
}
```

</details>

---

### Tool result

_source line 144 · 2026-05-23T03:06:17.607502+00:00_

Web search results for query: ""differentiable constrained imitation learning" Diehl robot motion planning venue published 2023"

Links: [{"title":"[2210.11796] Differentiable Constrained Imitation Learning for Robot Motion Planning and Control","url":"https://arxiv.org/abs/2210.11796"},{"title":"LeTO: Learning Constrained Visuomotor Policy with Differentiable Trajectory Optimization","url":"https://arxiv.org/html/2401.17500"},{"title":"Differentiable Constrained Imitation Learning for Robot Motion Planning   and Control","url":"https://arxiv.org/pdf/2210.11796"},{"title":"Differentiable Constrained Imitation Learning for Robot Motion Planning and Control - RST - TU Dortmund","url":"https://rst.etit.tu-dortmund.de/en/news-detail/differentiable-constrained-imitation-learning-for-robot-motion-planning-and-control-29480/"},{"title":"EKMP: Generalized Imitation Learning with Adaptation, Nonlinear Hard   Constraints and Obstacle Avoidance","url":"https://arxiv.org/pdf/2103.00452"}]

I found the paper you're looking for! Here are the key details:

**Paper:** "Differentiable Constrained Imitation Learning for Robot Motion Planning and Control" by Christopher Diehl, Janis Adamek, Martin Krüger, Frank Hoffmann and Torsten Bertram

**Publication:** The paper integrates hard constraints into the learning problem in a differentiable manner, via explicit completion and gradient-based correction.

**Year Published:** The paper was published in 2023 (posted on arXiv in August 2023, though it was originally submitted in 2022).

**Venue:** The paper appears to be published on arXiv (arXiv:2210.11796).

**Overview:** The work integrates the flexibility of Imitation Learning methods with hard constraint handling in optimal control, and simulated experiments of mobile robot navigation and automated driving provide evidence for the performance of the proposed method.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 145 · 2026-05-23T03:06:17.607647+00:00_

Web search results for query: "signed distance field SDF loss robot policy learning collision avoidance manipulation 2024 2025"

Links: [{"title":"(PDF) Neural NMPC through Signed Distance Field Encoding for Collision Avoidance","url":"https://www.researchgate.net/publication/398025684_Neural_NMPC_through_Signed_Distance_Field_Encoding_for_Collision_Avoidance"},{"title":"[PDF] Collision-Free Motion Generation Based on Stochastic Optimization and Composite Signed Distance Field Networks of Articulated Robot | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Collision-Free-Motion-Generation-Based-on-and-Field-Liu-Jiang/7b4ef92fc407415eb5daa716b360cff2fdd82e49"},{"title":"Neural NMPC through signed distance field encoding for collision avoidance - Martin Jacquet, Marvin Harms, Kostas Alexis, 2025","url":"https://journals.sagepub.com/doi/10.1177/02783649251401223"},{"title":"iSDF: Real-Time Neural Signed Distance Fields for Robot ...","url":"https://www.roboticsproceedings.org/rss18/p012.pdf"},{"title":"Neural NMPC through Signed Distance Field Encoding for Collision Avoidance","url":"https://arxiv.org/pdf/2511.21312"}]

I've performed the web search on signed distance fields (SDF) loss for robot policy learning with collision avoidance. Here are the key findings:

## Recent Research (2024-2025)

A recent paper introduces a neural nonlinear model predictive control (NMPC) framework for mapless, collision-free navigation in unknown environments with Aerial Robots, using onboard range sensing, with a neural architecture for encoding a single range observation as a signed distance function (SDF).

This approach leverages deep neural networks to encode a single range image into a Signed Distance Function, consisting of a convolutional encoder that compresses the input image into a low-dimensional latent vector, and a Multi-Layer Perceptron that approximates the corresponding spatial SDF.

## Robot Manipulation & Motion Generation

Recent work proposes a stocha
…[truncated 869 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 146 · 2026-05-23T03:06:17.607801+00:00_

Web search results for query: "arxiv "learning on one mode" weighted imitation learning LOM authors robot manipulation ICLR 2025"

Links: [{"title":"Published as a conference paper at ICLR 2025 LEARNING ON ONE MODE:","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/be62c4a943675195ff5a2a98d5b9724f-Paper-Conference.pdf"},{"title":"Learning on One Mode: Addressing Multi-modality in Offline Reinforcement Learning","url":"https://arxiv.org/html/2412.03258"},{"title":"[2412.03258] Learning on One Mode: Addressing Multi-modality in Offline Reinforcement Learning","url":"https://arxiv.org/abs/2412.03258"},{"title":"LLM-based Interactive Imitation Learning for Robotic Manipulation","url":"https://arxiv.org/html/2504.21769v1"},{"title":"Awesome-Robotics-Manipulation/contents/low-level_learning-based_action_modelling.md at main · BaiShuanghao/Awesome-Robotics-Manipulation","url":"https://github.com/BaiShuanghao/Awesome-Robotics-Manipulation/blob/main/contents/low-level_learning-based_action_modelling.md"},{"title":"One-Shot Imitation Learning with Invariance Matching for Robotic   Manipulation","url":"https://arxiv.org/pdf/2405.13178"}]

I found the paper you're looking for. The paper proposes a simpler yet effective approach: Weighted Imitation Learning on One Mode (LOM), which was published as a conference paper at ICLR 2025.

The key insight is that learning from a single mode — the one with the highest expected return — is sufficient to generate optimal actions. By using a Gaussian mixture model to identify modes and selecting the best mode based on expected returns, LOM avoids the pitfalls of averaging over conflicting actions.

Empirically, LOM outperforms existing methods on standard D4RL benchmarks and demonstrates its effectiveness in complex, multi-modal scenarios. The paper is available on arXiv as paper 2412.03258 and the full ICLR 2025 proceedings version is also available online.


REMINDER: You MUST include the sources above in your response to th
…[truncated 33 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 147 · 2026-05-23T03:06:17.607945+00:00_

Web search results for query: "arxiv 2601.19612 "safe exploration via policy priors" ICLR 2026 authors"

Links: [{"title":"[2601.19612] Safe Exploration via Policy Priors","url":"https://arxiv.org/abs/2601.19612"},{"title":"(PDF) Safe Exploration via Policy Priors","url":"https://www.researchgate.net/publication/400118806_Safe_Exploration_via_Policy_Priors"},{"title":"Published as a conference paper at ICLR 2026 SAFE EXPLORATION VIA POLICY PRIORS","url":"https://arxiv.org/pdf/2601.19612"},{"title":"Safe Exploration via Policy Priors | OpenReview","url":"https://openreview.net/forum?id=JC8xYAADHL"},{"title":"Safe Exploration via Policy Priors","url":"https://arxiv.org/html/2601.19612"},{"title":"Learning Transferable Domain Priors for Safe Exploration in   Reinforcement Learning","url":"https://arxiv.org/pdf/1909.04307"},{"title":"Provably Efficient Safe Exploration via Primal-Dual Policy ...","url":"https://arxiv.org/pdf/2003.00534"},{"title":"Safe-To-Explore State Spaces: Ensuring Safe Exploration in Policy Search   with Hierarchical Task Optimization","url":"https://arxiv.org/pdf/1810.03516"},{"title":"ICLR.2026 | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/venue/ICLR.2026"}]

Based on the search results, here's what I found about arxiv 2601.19612 "Safe Exploration via Policy Priors":

**Paper Information:**
- Published as a conference paper at ICLR 2026
- Authors: Manuel Wendl, Yarden As, Manish Prajapat, Anton Pollak, Stelian Coros, Andreas Krause
- Submitted on 27 Jan 2026 (v1), last revised 8 Feb 2026 (v2)

**Overview:**
The approach, SOOPER, uses probabilistic dynamics models to optimistically explore, yet pessimistically fall back to the conservative policy prior if needed. SOOPER guarantees safety throughout learning, and establishes convergence to an optimal policy by bounding its cumulative regret.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 148 · 2026-05-23T03:06:17.608094+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2210.11796 \"differentiable constrained imitation learning\" conference journal accepted IEEE ICRA IROS RA-L 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2210.11796 \"differentiable constrained imitation learning\" conference journal accepted IEEE ICRA IROS RA-L 2023"
  }
}
```

</details>

---

### Tool call

_source line 149 · 2026-05-23T03:06:17.608226+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"collision-free motion generation\" \"signed distance field\" articulated robot stochastic optimization 2024 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"collision-free motion generation\" \"signed distance field\" articulated robot stochastic optimization 2024 arxiv"
  }
}
```

</details>

---

### Tool call

_source line 150 · 2026-05-23T03:06:17.608350+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2401.10700 FISOR authors Yinan Zheng safe offline RL diffusion"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2401.10700 FISOR authors Yinan Zheng safe offline RL diffusion"
  }
}
```

</details>

---

### Tool call

_source line 151 · 2026-05-23T03:06:17.608526+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"the pitfalls of imitation learning when actions are continuous\" Simchowitz Pfrommer 2025 venue conference"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"the pitfalls of imitation learning when actions are continuous\" Simchowitz Pfrommer 2025 venue conference"
  }
}
```

</details>

---

### Tool result

_source line 152 · 2026-05-23T03:06:17.608703+00:00_

Web search results for query: "arxiv 2210.11796 "differentiable constrained imitation learning" conference journal accepted IEEE ICRA IROS RA-L 2023"

Links: [{"title":"[2210.11796] Differentiable Constrained Imitation Learning for Robot Motion Planning and Control","url":"https://arxiv.org/abs/2210.11796"},{"title":"LeTO: Learning Constrained Visuomotor Policy with Differentiable Trajectory Optimization","url":"https://arxiv.org/html/2401.17500"},{"title":"Differentiable Constrained Imitation Learning for Robot Motion Planning   and Control","url":"https://arxiv.org/pdf/2210.11796"},{"title":"A Linearly Constrained Nonparametric Framework for Imitation Learning","url":"https://arxiv.org/pdf/1909.07374"},{"title":"(PDF) Imitation Learning via Differentiable Physics","url":"https://www.researchgate.net/publication/361253211_Imitation_Learning_via_Differentiable_Physics"}]

Based on the search results, I found information about arxiv 2210.11796:

"Differentiable Constrained Imitation Learning for Robot Motion Planning and Control" is by Christopher Diehl, Janis Adamek, Martin Krüger, Frank Hoffmann and Torsten Bertram.

The work integrates the flexibility of imitation learning with hard constraint handling in optimal control, constituting a general framework for constrained robotic motion planning and control using offline imitation learning, where hard constraints are integrated into the learning problem in a differentiable manner via explicit completion and gradient-based correction.

However, the search results from the arXiv page do not explicitly specify whether this paper has been accepted to IEEE ICRA, IROS, or RA-L in 2023. The metadata shows the arXiv page was last updated on August 28, 2023, but does not confirm conference or journal acceptance. To find that specific information, you would need to check the official conference/journal proceedings or the paper's current status directly.


REMINDER: You MUST include the sources above in your response to the us
…[truncated 29 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 153 · 2026-05-23T03:06:17.608865+00:00_

Web search results for query: "arxiv 2401.10700 FISOR authors Yinan Zheng safe offline RL diffusion"

Links: [{"title":"[2401.10700] Safe Offline Reinforcement Learning with Feasibility-Guided Diffusion Model","url":"https://arxiv.org/abs/2401.10700"},{"title":"FISOR - Yinan Zheng","url":"https://zhengyinan-air.github.io/FISOR/"},{"title":"[PDF] Safe Offline Reinforcement Learning with Feasibility-Guided Diffusion Model | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Safe-Offline-Reinforcement-Learning-with-Diffusion-Zheng-Li/a2246e09ab0b56ba91322747addad030eae56c50"},{"title":"Safe Offline Reinforcement Learning with Feasibility-Guided Diffusion Model","url":"https://arxiv.org/html/2401.10700"},{"title":"Yinan Zheng","url":"https://zhengyinan-air.github.io/"},{"title":"GitHub - ZhengYinan-AIR/FISOR: [ICLR 2024] The official implementation of \"Safe Offline Reinforcement Learning with Feasibility-Guided Diffusion Model\"","url":"https://github.com/ZhengYinan-AIR/FISOR"}]

Based on the search results, I found detailed information about arxiv paper 2401.10700:

**Paper Title:** Safe Offline Reinforcement Learning with Feasibility-Guided Diffusion Model

**Authors:** Yinan Zheng, Jianxiong Li, Dongjie Yu, Yujie Yang, Shengbo Eben Li, Xianyuan Zhan, and Jingjing Liu

**FISOR Method:** FISOR (FeasIbility-guided Safe Offline RL) allows safety constraint adherence, reward maximization, and offline policy learning to be realized via three decoupled processes, while offering strong safety performance and stability.

**Key Technical Contribution:** The paper proposes a novel energy-guided diffusion model that does not require training a complicated time-dependent classifier to extract the policy, greatly simplifying the training.

**Results:** FISOR is the only method that can guarantee safety satisfaction in all tasks, while achieving top returns in most tasks.

**Publication Venue:** The paper was accepted to ICLR 2024.


REMINDER: You MUST include the sour
…[truncated 65 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 154 · 2026-05-23T03:06:17.609022+00:00_

Web search results for query: ""the pitfalls of imitation learning when actions are continuous" Simchowitz Pfrommer 2025 venue conference"

Links: [{"title":"The Pitfalls of Imitation Learning when Actions are Continuous","url":"https://proceedings.mlr.press/v291/simchowitz25a.html"},{"title":"[PDF] The Pitfalls of Imitation Learning when Actions are Continuous | Semantic Scholar","url":"https://www.semanticscholar.org/paper/The-Pitfalls-of-Imitation-Learning-when-Actions-are-Simchowitz-Pfrommer/20085db39e8cdf3d13f6a1332a0d8049eee44454"},{"title":"[2503.09722] The Pitfalls of Imitation Learning when Actions are Continuous","url":"https://arxiv.org/abs/2503.09722"},{"title":"The Pitfalls of Imitation Learning when Actions are Continuous Max Simchowitz*","url":"https://www.arxiv.org/pdf/2503.09722v2"},{"title":"The Pitfalls of Imitation Learning when Actions are Continuous Max Simchowitz*","url":"https://arxiv.org/pdf/2503.09722"},{"title":"The Pitfalls of Imitation Learning when Actions are Continuous","url":"https://arxiv.org/html/2503.09722v4"},{"title":"The Pitfalls of Imitation Learning when Actions are Continuous","url":"https://www.researchgate.net/publication/389820775_The_Pitfalls_of_Imitation_Learning_when_Actions_are_Continuous"},{"title":"Welcome! - Max Simchowitz","url":"https://msimchowitz.github.io/"}]

Based on the search results, I found the paper you're looking for:

**Paper:** The Pitfalls of Imitation Learning when Actions are Continuous

**Authors:** Max Simchowitz, Daniel Pfrommer, Ali Jadbabaie

**Venue:** Proceedings of Thirty Eighth Conference on Learning Theory (COLT 2025)

**Publication Details:** Proceedings of Machine Learning Research 291:5248-5351

**Year:** 2025

**Summary:** The paper shows that there exist stable dynamics (contracting exponentially quickly) and smooth, deterministic experts such that any smooth, deterministic imitator policy necessarily suffers error on execution that is exponentially larger, as a function of problem 
…[truncated 478 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 155 · 2026-05-23T03:06:17.609175+00:00_

Web search results for query: ""collision-free motion generation" "signed distance field" articulated robot stochastic optimization 2024 arxiv"

Links: [{"title":"[PDF] Collision-Free Motion Generation Based on Stochastic Optimization and Composite Signed Distance Field Networks of Articulated Robot | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Collision-Free-Motion-Generation-Based-on-and-Field-Liu-Jiang/7b4ef92fc407415eb5daa716b360cff2fdd82e49"},{"title":"Collision-free Motion Generation Based on Stochastic Optimization and   Composite Signed Distance Field Networks of Articulated Robot","url":"https://arxiv.org/pdf/2306.04130"},{"title":"Collision-Free Motion Generation Based on Stochastic Optimization and Composite Signed Distance Field Networks of Articulated Robot | IEEE Journals & Magazine | IEEE Xplore","url":"http://ieeexplore.ieee.org/iel7/7083369/10254630/10238810.pdf"},{"title":"[2306.04130] Collision-free Motion Generation Based on Stochastic Optimization and Composite Signed Distance Field Networks of Articulated Robot","url":"https://arxiv.org/abs/2306.04130"},{"title":"Collision-Free Motion Generation Based on Stochastic Optimization and Composite Signed Distance Field Networks of Articulated Robot | Request PDF","url":"https://www.researchgate.net/publication/373665800_Collision-Free_Motion_Generation_Based_on_Stochastic_Optimization_and_Composite_Signed_Distance_Field_Networks_of_Articulated_Robot"},{"title":"Efficient Collision Detection Framework for Enhancing Collision-Free Robot Motion","url":"https://arxiv.org/html/2409.14955v1"},{"title":"dblp: Fei Zhao 0001","url":"https://dblp.org/pid/21/6180-1.html"}]

I found a highly relevant paper matching your search query. Here are the results:

## Primary Result

The paper "Collision-free Motion Generation Based on Stochastic Optimization and Composite Signed Distance Field Networks of Articulated Robot" proposes a stochastic optimization-based motion generation method to generate 
…[truncated 1167 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 156 · 2026-05-23T03:06:17.609329+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2412.03258 \"learning on one mode\" authors offline reinforcement learning multi-modality"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2412.03258 \"learning on one mode\" authors offline reinforcement learning multi-modality"
  }
}
```

</details>

---

### Tool result

_source line 157 · 2026-05-23T03:06:17.609575+00:00_

Now I have enough information to compile the findings. Here is the structured literature survey:

---

## Literature Survey: Safety Metrics for Robot Learning

### 1. SafeVLA: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning

- **Authors:** Borong Zhang, Yuhao Zhang, Jiaming Ji, Yingshan Lei, Josef Dai, Yuanpei Chen, Yaodong Yang
- **Venue:** NeurIPS 2025 (Spotlight)
- **URL:** https://arxiv.org/abs/2503.03480
- **Core method:** Proposes an Integrated Safety Approach (ISA) that models safety requirements for VLA policies via constrained Markov decision processes (CMDP). The method actively elicits diverse unsafe behaviors, then constrains VLA policies using safe reinforcement learning from a min-max optimization perspective.
- **Key results:** Reduces cumulative cost of safety violations by 83.58% compared to SOTA while maintaining task success rate (+3.85%). Eliminates high-risk behaviors and reduces the upper bound of unsafe behaviors to 1/35 of the current SOTA. Safety constraints generalize to unseen out-of-distribution scenarios.
- **Relation to project:** Directly relevant -- SafeVLA defines safety metrics (cumulative cost, violation rate) for VLA model evaluation in manipulation tasks, analogous to the project's collision_rate and frozen_rate metrics. Both share the goal of quantifying safety during robotic manipulation policy execution. SafeVLA's CMDP-based cost formulation could inform how collision_rate is formalized as a constraint.

### 2. Safety-Gymnasium: A Unified Safe Reinforcement Learning Benchmark

- **Authors:** Jiaming Ji, Borong Zhang, Jiayi Zhou, Xuehai Pan, Weidong Huang, Ruiyang Sun, Yiran Geng, Yifan Zhong, Josef Dai, Yaodong Yang
- **Venue:** NeurIPS 2023 (Datasets and Benchmarks Track)
- **URL:** https://arxiv.org/abs/2310.12567
- **Core method:** Provides a unified environment suite for safe RL covering single-agent and multi-agent scenarios, paired with SafePO -- a library of 16 SOTA safe RL algorithms. 
…[truncated 5525 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "Agent",
  "elapsed_ms": 20
}
```

</details>

---

### Tool result

_source line 158 · 2026-05-23T03:06:17.609816+00:00_

I now have comprehensive information on all the key papers. Here is the structured survey:

---

## Literature Survey: VLA Safety / Collision Avoidance

### Overall Finding

This is an **emerging but rapidly growing area** (late 2025 -- early 2026). Five directly relevant papers were found, all addressing safety for VLA-based robot manipulation. The combination of SDF-based auxiliary loss within a VLA training loop (as in your Pi0.5 + A1 project) has **no direct prior work** -- this constitutes a clear **novelty gap**.

---

### Paper 1: SafeVLA

- **Title:** SafeVLA: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning
- **Authors:** Borong Zhang et al. (PKU-Alignment group)
- **Venue:** NeurIPS 2025 (Spotlight)
- **URL:** https://arxiv.org/abs/2503.03480
- **Core method:** Models VLA safety as a Constrained Markov Decision Process (CMDP). Uses a min-max optimization to align VLA policies against elicited safety risks via safe reinforcement learning. Systematically elicits diverse unsafe behaviors, then constrains the policy to avoid them.
- **Key results:** Reduces cumulative cost of safety violations by 83.58% vs. SOTA while maintaining task success rate (+3.85%). Evaluated on long-horizon mobile manipulation tasks.
- **Relation to your project:** **Competitor / complementary perspective.** SafeVLA addresses safety via RL-based constrained optimization at the policy level, whereas your approach embeds geometric safety (SDF) as an auxiliary loss during VLA training. The two are conceptually complementary -- SafeVLA's CMDP framework could potentially be combined with SDF-based cost signals. However, SafeVLA requires online RL fine-tuning, while your SDF auxiliary loss is a simpler supervised signal.

---

### Paper 2: VLSA (AEGIS)

- **Title:** VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer
- **Authors:** Songqiao Hu, Zeyi Liu, Shuang Liu, Jun Cen, Zihan Meng, Xiao He (Tsinghua)
- **Venue:** arXiv preprin
…[truncated 6541 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "Agent",
  "elapsed_ms": 22
}
```

</details>

---

### Tool result

_source line 159 · 2026-05-23T03:06:17.609985+00:00_

Web search results for query: "arxiv 2412.03258 "learning on one mode" authors offline reinforcement learning multi-modality"

Links: [{"title":"[2412.03258] Learning on One Mode: Addressing Multi-modality in Offline Reinforcement Learning","url":"https://arxiv.org/abs/2412.03258"},{"title":"Learning on One Mode: Addressing Multi-Modality in Offline Reinforcement Learning | Request PDF","url":"https://www.researchgate.net/publication/386454773_Learning_on_One_Mode_Addressing_Multi-Modality_in_Offline_Reinforcement_Learning"},{"title":"Machine Learning Dec 2024","url":"https://www.arxiv.org/list/cs.LG/2024-12?skip=250&show=2000"},{"title":"Learning on One Mode: Addressing Multi-modality in Offline Reinforcement   Learning","url":"https://arxiv.org/pdf/2412.03258"},{"title":"Learning on One Mode: Addressing Multi-Modality in Offline Reinforcement Learning - Paper Detail","url":"https://deeplearn.org/arxiv/555338/learning-on-one-mode:-addressing-multi-modality-in-offline-reinforcement-learning"},{"title":"Learning on One Mode: Addressing Multi-modality in Offline Reinforcement Learning","url":"https://arxiv.org/html/2412.03258"}]

Based on the search results, here's what I found about arxiv paper 2412.03258:

**Paper Details:**
- Title: "Learning on One Mode: Addressing Multi-modality in Offline Reinforcement Learning"
- Authors: Mianchu Wang, Yue Jin, and Giovanni Montana

**Research Summary:**
The paper addresses offline reinforcement learning, which seeks to learn optimal policies from static datasets without environmental interaction, with a focus on handling multi-modal action distributions where multiple behaviors are represented in the data.

The authors propose Weighted Imitation Learning on One Mode (LOM), which focuses on learning from a single, promising mode of the behavior policy by using a Gaussian mixture model to identify modes and selecting the best mode based on expected returns, thus avoiding the pitfalls of averaging over conflicting actions.

**Res
…[truncated 301 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 160 · 2026-05-23T03:06:17.610190+00:00_

Now I have enough information to compile the literature survey. Here are my findings:

---

## Literature Survey: SDF in Robot Manipulation

### 1. VLSA (AEGIS): Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer

- **Authors:** Songqiao Hu, Zeyi Liu, Shuang Liu, Jun Cen, Zihan Meng, Xiao He
- **Venue & Year:** arXiv 2512.11891, December 2025 (Tsinghua University)
- **Core Method:** Integrates Control Barrier Functions (CBFs) into VLA models via a plug-and-play safety constraint layer. Uses VLMs to identify hazardous objects, open-set object detection, and depth information to translate semantic risks into physical avoidance requirements. A CBF-based Quadratic Programming (QP) solver minimally adjusts nominal VLA actions to ensure collision-free execution.
- **Key Results:** 59.16% improvement in obstacle avoidance rate; 17.25% increase in task execution success rate. Introduces SafeLIBERO benchmark for safety-critical manipulation.
- **URL:** [https://arxiv.org/abs/2512.11891](https://arxiv.org/abs/2512.11891)
- **Relation to project:** **Direct competitor / most relevant comparison.** Both address the same problem: making VLA models collision-aware. VLSA uses a post-hoc CBF constraint layer on VLA outputs, whereas the project approach embeds an SDF-based auxiliary loss during training. Key difference: VLSA modifies actions at inference time (no retraining), while the SDF auxiliary loss approach bakes collision awareness into the model weights. Comparing these two paradigms (inference-time safety vs. training-time safety) would be a core contribution.

---

### 2. Representing Robot Geometry as Distance Fields: Applications to Whole-body Manipulation

- **Authors:** Yiming Li, Yan Zhang, Amirreza Razmjoo, Sylvain Calinon
- **Venue & Year:** ICRA 2024 (also arXiv 2307.00533)
- **Core Method:** Represents robot geometry as Robot Distance Fields (RDF) using Bernstein polynomials to encode the signed distance for each robot link, extending SDFs to
…[truncated 6233 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "Agent",
  "elapsed_ms": 21
}
```

</details>

---

### Tool result

_source line 161 · 2026-05-23T03:06:17.610396+00:00_

Now I have enough material. Here are the findings:

---

## Literature Survey: Auxiliary Loss for Safety in Robot Learning

### 1. RAIL: Reachability-Aided Imitation Learning for Safe Policy Execution

- **Authors:** Wonsuhk Jung, Dennis Anthony, Utkarsh A. Mishra, Nadun Ranawaka Arachchige, Matthew Bronars, Danfei Xu, Shreyas Kousik
- **Venue:** ICRA 2025
- **URL:** https://arxiv.org/abs/2409.19190
- **Core method:** Builds a reachability-based safety filter on top of imitation learning policies. Uses polynomial zonotopes to overapproximate the robot manipulator's continuous-time swept volume for fast collision checking, then intervenes when the IL policy's planned action would lead to collision.
- **Key results:** Achieves 0% collision rate vs. 5-35% for baseline IL policies, while maintaining high task success. The safety filter also helps policies discover new safe behavioral modalities.
- **Relation to project:** **Competitor / complementary.** RAIL adds safety as a post-hoc filter layer over IL policies rather than training with an auxiliary loss. The SDF auxiliary loss approach (this project) bakes safety into the policy during training, while RAIL enforces it at inference time. These are complementary strategies that could potentially be combined.

---

### 2. Learning to Recover for Safe Reinforcement Learning

- **Authors:** Haoyu Wang et al.
- **Venue:** arXiv preprint, 2023 (arXiv:2309.11907)
- **URL:** https://arxiv.org/abs/2309.11907
- **Core method:** Three-stage architecture (TU-Recovery) where a safety critic and recovery policy are learned before task training. An auxiliary reward is introduced to mitigate the "adversarial phenomenon" (disagreement between task and recovery policies) and help the task policy learn to recover from high-risk states.
- **Key results:** TU-Recovery outperforms unconstrained baselines in both reward and constraint violations. The auxiliary reward further improves the reward-to-cost ratio by significantly reducing constr
…[truncated 5438 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "Agent",
  "elapsed_ms": 19
}
```

</details>

---

### Tool result

_source line 162 · 2026-05-23T03:06:17.610680+00:00_

I now have enough information to compile the survey. Here are my findings:

---

## Literature Survey: Fake Safety / Action Collapse in Robotics

### Overall Assessment: Significant Novelty Gap

No paper found directly addresses the concept of a "frozen_rate" metric -- i.e., explicitly detecting and penalizing robots that achieve low collision rates merely by ceasing to move. The exact framing of "fake safety through inaction" as a measurable, first-class failure mode appears to be **underexplored and novel**. The closest related work falls into three adjacent categories: (1) overly conservative safe RL policies, (2) action mode collapse in imitation/offline RL, and (3) diffusion-based approaches that explicitly handle multimodal actions to avoid degenerate averaging.

---

### Paper 1: FISOR -- Safe Offline Reinforcement Learning with Feasibility-Guided Diffusion Model

- **Authors:** Yinan Zheng, Jianxiong Li, Dongjie Yu, Yujie Yang, Shengbo Eben Li, Xianyuan Zhan, Jingjing Liu
- **Venue:** ICLR 2024
- **URL:** https://arxiv.org/abs/2401.10700
- **Core method:** Decouples safety constraint adherence, reward maximization, and offline policy learning into three processes. Uses Hamilton-Jacobi reachability to identify the largest feasible region from offline data via reversed expectile regression, then extracts policy via energy-guided diffusion model without a time-dependent classifier.
- **Key results:** Only method that guarantees zero constraint violation in all tested tasks while achieving top returns in most. Demonstrates that hard safety constraints can be enforced without collapsing to trivially safe (zero-reward) policies.
- **Relation to frozen_rate:** Directly relevant as a **counter-example approach** -- FISOR explicitly tackles the tension where enforcing hard safety constraints can yield "overly conservative (near zero-reward) policies." The paper acknowledges that naive safe offline RL can produce degenerate policies but does not define a metric to det
…[truncated 7253 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "Agent",
  "elapsed_ms": 23
}
```

</details>

---

### Tool call

_source line 163 · 2026-05-23T03:06:17.610924+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/related_work_survey.md",
  "content": "# Related Work Survey: Pi0.5 + SDF Auxiliary Loss for Collision Avoidance\n\n**Date:** 2026-05-23\n\n---\n\n## 1. VLA Safety / Collision Avoidance\n\n#### SafeVLA: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning (NeurIPS 2025 Spotlight)\n- **Authors:** Borong Zhang et al. (PKU-Alignment)\n- **Core method:** Models VLA safety as a Constrained MDP (CMDP). Uses min-max optimization to align VLA policies against elicited safety risks via safe RL. Systematically elicits diverse unsafe behaviors, then constrains the policy to avoid them.\n- **Key results:** Reduces cumulative cost of safety violations by 83.58% vs. SOTA while maintaining task success rate (+3.85%).\n- **Relation to our work:** Competitor / complementary. SafeVLA uses RL-based constrained optimization at the policy level; we embed geometric safety (SDF) as an auxiliary loss during training. SafeVLA requires online RL fine-tuning, our SDF auxiliary loss is a simpler supervised signal. The two approaches could be combined.\n- **URL:** https://arxiv.org/abs/2503.03480\n\n#### VLSA (AEGIS): Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer (arXiv 2025)\n- **Authors:** Songqiao Hu, Zeyi Liu, Shuang Liu, Jun Cen, Zihan Meng, Xiao He (Tsinghua)\n- **Core method:** Adds a plug-and-play safety constraint (SC) layer based on Control Barrier Functions (CBF) on top of existing VLA models. Uses VLM-based safety assessment + open-set detection + depth, then a CBF-based QP solver minimally adjusts VLA actions to guarantee collision-free execution.\n- **Key results:** 59.16% improvement in obstacle avoidance rate and 17.25% increase in task success rate on SafeLIBERO benchmark. Outperforms Pi0.5 (68.13% vs 50.88%).\n- **Relation to our work:** **Most direct competitor.** Both add safety to VLA models, but AEGIS does it at **inference time** (post-hoc CBF-QP correction), while we integrate safety at **training time** via SDF auxiliary loss. Our approach learns inherently safer policies rather than relying on runtime corrections. AEGIS's SafeLIBERO benchmark is useful for evaluation.\n- **URL:** https://arxiv.org/abs/2512.11891\n\n#### CoFreeVLA: Collision-Free Dual-Arm Manipulation via VLA Model and Risk Estimation (arXiv 2026)\n- **Authors:** Xuanran Zhai, Binkai Ou, Qiaojun Yu, Ce Hao, Yaohua Liu et al.\n- **Core method:** Augments VLA with a short-horizon self-collision risk estimator from proprioception, visual embeddings, and planned actions. Gates risky commands and recovers to safe states. Risk estimator pre-trained with model-based collision labels.\n- **Key results:** Reduces self-collisions and improves success rates vs. RDT and APEX on five bimanual tasks.\n- **Relation to our work:** Technique to borrow. CoFreeVLA's collision risk estimator is conceptually similar to our SDF auxiliary head -- both predict a geometric safety signal alongside the action. Key difference: CoFreeVLA uses binary collision labels while we use continuous SDF values providing richer gradient information.\n- **URL:** https://arxiv.org/abs/2601.21712\n\n#### SAFE: Multitask Failure Detection for Vision-Language-Action Models (NeurIPS 2025)\n- **Authors:** Gu, Ju, Sun, Gilitschenski, Nishimura, Itkina, Shkurti\n- **Core method:** Learns a failure detector from VLA internal features that predicts task failure likelihood. Discovers that VLA feature spaces already encode success/failure information, enabling zero-shot failure detection on unseen tasks.\n- **Key results:** SOTA failure detection on OpenVLA, Pi0, and Pi0-FAST in sim and real.\n- **Relation to our work:** Complementary. SAFE detects failures post-hoc from VLA features rather than preventing them. Their finding that VLA features encode safety-relevant information supports our hypothesis that an SDF auxiliary head can effectively leverage VLA internal representations.\n- **URL:** https://arxiv.org/abs/2506.09937\n\n#### CompliantVLA-adaptor: VLM-Guided Variable Impedance Action for Safe Contact-Rich Manipulation (arXiv 2026)\n- **Authors:** (arXiv 2601.15541)\n- **Core method:** Augments VLA models with a VLM-informed context-aware variable impedance controller. VLM interprets task context to adapt stiffness/damping parameters, regulated by real-time force/torque feedback.\n- **Key results:** Improves safety and effectiveness in contact-rich tasks vs. standard position-only VLA outputs.\n- **Relation to our work:** Complementary -- addresses force/compliance safety rather than collision geometry. Could be combined: SDF prevents collisions in free space, impedance control handles intentional contact phases.\n- **URL:** https://arxiv.org/abs/2601.15541\n\n**Novelty gap:** No existing work integrates SDF-based geometric supervision as an auxiliary training loss within a VLA model. The landscape:\n\n| Approach | When | Safety signal | Paper |\n|---|---|---|---|\n| RL constrained optimization | Training (RL) | Cost from unsafe rollouts | SafeVLA |\n| CBF/QP post-hoc correction | Inference | Control barrier function | VLSA/AEGIS |\n| Collision risk estimator | Inference (gating) | Binary collision prediction | CoFreeVLA |\n| Failure detection | Post-hoc | VLA feature analysis | SAFE |\n| Impedance control | Inference | Force/torque feedback | CompliantVLA-adaptor |\n| **SDF auxiliary loss (ours)** | **Training (supervised)** | **Continuous signed distance** | **None** |\n\n---\n\n## 2. Fake Safety / Action Collapse in Robotics\n\n**Overall assessment: Significant novelty gap.** No paper directly addresses the concept of a \"frozen_rate\" metric -- detecting and penalizing robots that achieve low collision rates merely by ceasing to move. The closest work falls into: (1) overly conservative safe RL policies, (2) action mode collapse in imitation/offline RL, (3) diffusion approaches handling multimodal actions.\n\n#### FISOR: Safe Offline RL with Feasibility-Guided Diffusion Model (ICLR 2024)\n- **Authors:** Yinan Zheng, Jianxiong Li, Dongjie Yu, Yujie Yang, Shengbo Eben Li, Xianyuan Zhan, Jingjing Liu\n- **Core method:** Decouples safety constraint adherence, reward maximization, and offline policy learning. Uses Hamilton-Jacobi reachability to identify feasible region, then extracts policy via energy-guided diffusion model.\n- **Key results:** Zero constraint violation in all tested tasks while achieving top returns. Explicitly addresses the tension where hard safety constraints can yield \"overly conservative (near zero-reward) policies.\"\n- **Relation to our work:** Acknowledges that naive safe offline RL can produce degenerate policies but doesn't define a metric to detect this. A frozen_rate metric would complement FISOR by quantifying when safety is achieved through inaction vs. genuine collision avoidance.\n- **URL:** https://arxiv.org/abs/2401.10700\n\n#### POLICEd RL: Learning Closed-Loop Robot Control with Provable Hard Constraints (RSS 2024)\n- **Authors:** Jean-Baptiste Bouvier, Kartik Nagpal, Negar Mehr\n- **Core method:** Makes the learned policy affine near unsafe state boundaries, using this affine region as a repulsive buffer that provably prevents constraint violations.\n- **Key results:** Formal guarantees of hard constraint satisfaction in closed-loop execution.\n- **Relation to our work:** Repulsive buffers near unsafe regions can cause robots to slow down or stop near obstacles -- exactly what frozen_rate detects. The paper does not measure or discuss this failure mode.\n- **URL:** https://arxiv.org/abs/2403.13297\n\n#### Learning on One Mode (LOM): Addressing Multi-modality in Offline RL (ICLR 2025)\n- **Authors:** Mianchu Wang, Yue Jin, Giovanni Montana\n- **Core method:** Uses GMM to decompose offline dataset's action distribution into modes, then applies weighted IL on only the highest-return mode. Avoids \"mode averaging\" where learning from multimodal data collapses to the mean (often near-zero) action.\n- **Key results:** Outperforms standard offline RL methods on D4RL benchmarks, particularly in multi-modal scenarios.\n- **Relation to our work:** Mode averaging is a direct mechanism producing frozen/near-zero actions: opposing motion directions average to zero velocity. frozen_rate is a diagnostic to detect when mode collapse produces inaction.\n- **URL:** https://arxiv.org/abs/2412.03258\n\n#### The Pitfalls of Imitation Learning when Actions are Continuous (COLT 2025)\n- **Authors:** Max Simchowitz, Daniel Pfrommer, Ali Jadbabaie\n- **Core method:** Theoretical analysis proving that for stable dynamics with smooth deterministic experts, any smooth deterministic imitator suffers execution error exponentially larger than training error.\n- **Key results:** Formalizes why BC fails due to closed-loop feedback between imperfect policy and dynamics. Shows \"sufficiently spread\" expert trajectory distributions can mitigate the problem.\n- **Relation to our work:** Provides theoretical grounding for why IL policies can degenerate, including potential freezing when the policy becomes uncertain and regresses toward mean actions. frozen_rate operationalizes detection of one specific failure mode this theory predicts.\n- **URL:** https://arxiv.org/abs/2503.09722\n\n#### CAPE: Context-Aware Diffusion Policy via Proximal Mode Expansion for Collision Avoidance (arXiv 2025)\n- **Authors:** (arXiv 2511.22773)\n- **Core method:** Expands trajectory distribution modes of a diffusion policy using context-aware priors and guided denoising. Generates initial plans, executes short prefixes, then re-denoises with collision-aware guidance.\n- **Key results:** Up to 26% (sim) and 80% (real) higher success rates in cluttered unseen environments.\n- **Relation to our work:** Addresses limited mode coverage in diffusion policies for collision avoidance. When a policy lacks diverse trajectory modes, it may freeze. Mode expansion is a generation-side solution; frozen_rate is the evaluation-side diagnostic.\n- **URL:** https://arxiv.org/abs/2511.22773\n\n**Novelty of frozen_rate:** The problem is acknowledged (FISOR, safe RL surveys note \"overly conservative policies\"), but no existing metric explicitly measures the fraction of time a robot is stationary when it should be acting. Treating frozen behavior as safety metric gaming is an original contribution.\n\n---\n\n## 3. SDF in Robot Manipulation\n\n#### Representing Robot Geometry as Distance Fields (RDF) (ICRA 2024)\n- **Authors:** Yiming Li, Yan Zhang, Amirreza Razmjoo, Sylvain Calinon\n- **Core method:** Represents robot geometry as Robot Distance Fields using Bernstein polynomials to encode signed distance for each link. Continuous and differentiable, enabling direct use as cost functions for optimization-based planning.\n- **Key results:** Demonstrated on 7-axis Franka for collision avoidance and whole-body manipulation, including dual-arm settings.\n- **Relation to our work:** Borrowable technique. The Bernstein polynomial SDF encoding for robot links could compute the robot-side SDF in our auxiliary loss, providing accurate differentiable distance queries.\n- **URL:** https://arxiv.org/abs/2307.00533\n\n#### Configuration Space Distance Fields for Manipulation Planning (RSS 2024)\n- **Authors:** Yiming Li, Xuemin Chi, Amirreza Razmjoo, Sylvain Calinon\n- **Core method:** Computes Signed Distance Fields in configuration space (CDF) rather than task space. Neural MLP representation for compact, continuous C-space distances. Zero-level-set matches SDF, but CDF level sets have unit-norm gradients enabling one-step IK.\n- **Key results:** Fewer iterations than task-space SDF for contact planning on 7-axis Franka.\n- **Relation to our work:** Borrowable technique. CDF provides collision avoidance directly in joint space -- the space VLA models output actions in. Could yield better gradients than task-space SDF for the auxiliary loss.\n- **URL:** https://arxiv.org/abs/2406.01137\n\n#### iSDF: Real-Time Neural Signed Distance Fields for Robot Perception (RSS 2022)\n- **Authors:** Joseph Ortiz, Alexander Clegg, Jing Dong, Edgar Sucar, David Novotny, Michael Zollhoefer, Mustafa Mukadam\n- **Core method:** Continual learning system training a neural network online to map 3D coordinates to signed distances from a stream of posed depth images. Self-supervised, room-scale, real-time.\n- **Key results:** More accurate reconstructions and better collision cost/gradient approximations vs. voxel-grid baselines.\n- **Relation to our work:** Borrowable technique. Demonstrates how to construct differentiable SDF representations from depth images in real time -- exactly what's needed to compute SDF auxiliary loss during training or inference.\n- **URL:** https://arxiv.org/abs/2204.02296\n\n#### Neural NMPC through SDF Encoding for Collision Avoidance (IJRR 2025)\n- **Authors:** Martin Jacquet, Marvin Harms, Kostas Alexis\n- **Core method:** Encodes range images into SDF via convolutional encoder (latent vector) + MLP decoder (spatial SDF). SDF parametrizes position constraints in a velocity-tracking NMPC for map-free collision avoidance.\n- **Key results:** Real-world collision avoidance in forest environments for aerial robots with adversarial references.\n- **Relation to our work:** Borrowable architecture. The encoder-decoder (visual observation -> latent -> SDF) is transferable to our vision-conditioned SDF module for the auxiliary loss.\n- **URL:** https://arxiv.org/abs/2511.21312\n\n#### Composite SDF Networks for Collision-Free Motion of Articulated Robots (RA-L 2023)\n- **Authors:** Baolin Liu, Gedong Jiang, Fei Zhao, Xuesong Mei\n- **Core method:** Learns composite SDF networks to represent signed distance of articulated robots per link, enabling fast batch minimum distance estimation. Integrates into stochastic trajectory planner.\n- **Key results:** Collision-free, time-optimal motion generation with fast and accurate distance estimation.\n- **Relation to our work:** Borrowable technique. Composite SDF network architecture for articulated robots provides more accurate collision distance gradients for the auxiliary loss than scene-level SDF.\n- **URL:** https://arxiv.org/abs/2306.04130\n\n---\n\n## 4. Safety Metrics for Robot Learning\n\n#### SafeVLA (NeurIPS 2025 Spotlight)\n- *(See Section 1 for full details)*\n- **Metrics relevance:** Defines cumulative cost and violation rate for VLA manipulation evaluation, analogous to our collision_rate and frozen_rate.\n- **URL:** https://arxiv.org/abs/2503.03480\n\n#### Safety-Gymnasium: A Unified Safe RL Benchmark (NeurIPS 2023 D&B)\n- **Authors:** Jiaming Ji, Borong Zhang, Jiayi Zhou, Xuehai Pan et al.\n- **Core method:** Unified environment suite for safe RL (single/multi-agent) + SafePO library of 16 SOTA safe RL algorithms. Standardizes task definitions, constraint specifications, evaluation protocols.\n- **Key results:** Benchmarks 16 safe RL algorithms with standardized metrics: cost rate, cost return, reward-cost trade-off curves.\n- **Relation to our work:** \"Cost rate\" (violations per timestep) is conceptually identical to collision_rate. Evaluation protocol -- measuring task performance and safety simultaneously -- provides methodological template.\n- **URL:** https://arxiv.org/abs/2310.12567\n\n#### Robot Learning as an Empirical Science: Best Practices for Policy Evaluation (arXiv 2024)\n- **Authors:** Hadas Kress-Gazit, Kunimatsu Hashimoto, Naveen Kuppuswamy et al.\n- **Core method:** Surveys evaluation practices in robot learning. Argues the field over-relies on success rate. Proposes reporting multiple complementary metrics including safety-related ones and statistical significance.\n- **Key results:** Meta-analysis showing most papers report only success rate. Complementary metrics (collision rate, completion time, smoothness) reveal important behavioral differences invisible to success rate.\n- **Relation to our work:** Directly supports using collision_rate and frozen_rate as complementary metrics beyond success rate. Provides methodological justification for multi-metric evaluation.\n- **URL:** https://arxiv.org/abs/2409.09491\n\n#### GUARD: A Safe RL Benchmark (arXiv 2023)\n- **Authors:** Weiye Zhao, Ruixuan Liu, Rui Chen, Tianhao Wei, Yifan Sun, Changliu Liu (CMU)\n- **Core method:** Generalized Unified SAfe RL Development benchmark with configurable agents, tasks, and safety constraints. Supports state, action, and joint constraints.\n- **Key results:** Comprehensive comparison of safe RL algorithms (CPO, PPO-Lagrangian, TRPO-Lagrangian) with constraint violation rate, episodic cost, reward-cost Pareto frontiers.\n- **Relation to our work:** Flexible constraint specification framework is relevant for defining collision avoidance as a state constraint. Systematic comparison methodology parallels our evaluation approach.\n- **URL:** https://arxiv.org/abs/2305.13681\n\n#### Vision-Language-Action Safety: Threats, Challenges, Evaluations, and Mechanisms (arXiv 2026)\n- **Authors:** Qi Li et al.\n- **Core method:** Comprehensive survey of VLA safety covering five risk dimensions: irreversible physical consequences, multimodal attack surfaces, real-time latency constraints, error propagation over long horizons, data supply chain vulnerabilities.\n- **Key results:** VLA safety evaluation requires metrics beyond traditional RL safety, including physical damage assessment, constraint violation severity, and temporal propagation of unsafe states.\n- **Relation to our work:** Most directly relevant survey -- specifically addresses safety evaluation for VLA models. Contextualizes our collision_rate and frozen_rate metrics within the broader VLA safety landscape.\n- **URL:** https://arxiv.org/abs/2604.23775\n\n---\n\n## 5. Auxiliary Loss for Safety\n\n#### RAIL: Reachability-Aided Imitation Learning for Safe Policy Execution (ICRA 2025)\n- **Authors:** Wonsuhk Jung, Dennis Anthony, Utkarsh A. Mishra et al.\n- **Core method:** Builds a reachability-based safety filter on top of IL policies. Uses polynomial zonotopes to overapproximate the robot's continuous-time swept volume for fast collision checking, then intervenes when IL policy's action would collide.\n- **Key results:** 0% collision rate vs. 5-35% for baseline IL policies, while maintaining task success.\n- **Relation to our work:** Competitor / complementary. RAIL adds safety as a post-hoc filter over IL policies; we bake safety into the policy during training via SDF auxiliary loss. These strategies could be combined.\n- **URL:** https://arxiv.org/abs/2409.19190\n\n#### Learning to Recover for Safe RL (arXiv 2023)\n- **Authors:** Haoyu Wang et al.\n- **Core method:** Three-stage architecture (TU-Recovery) where safety critic and recovery policy are learned before task training. An auxiliary reward mitigates the \"adversarial phenomenon\" between task and recovery policies.\n- **Key results:** Outperforms unconstrained baselines in both reward and constraint violations. Auxiliary reward significantly reduces constraint violations.\n- **Relation to our work:** Borrowable technique. The idea of using an auxiliary reward/loss to shape task policy toward safety-aware behavior is directly analogous to our SDF auxiliary loss. Key difference: RL with learned recovery vs. our geometric loss in IL.\n- **URL:** https://arxiv.org/abs/2309.11907\n\n#### Reward Training Wheels: Adaptive Auxiliary Rewards for Robotics RL (IROS 2025)\n- **Authors:** Linji Wang, Tong Xu, Yuanjie Lu, Xuesu Xiao\n- **Core method:** Teacher-student framework (RTW) where a teacher monitors training signals and dynamically adjusts auxiliary reward weights during RL training.\n- **Key results:** Outperforms expert-designed rewards by 2.35% success rate, 122.62% in off-road mobility. 35% and 3x faster training.\n- **Relation to our work:** Borrowable technique. Adaptive weighting of auxiliary rewards is directly relevant -- a fixed SDF loss weight may be suboptimal across training stages. RTW's dynamic scheduling could improve SDF loss integration.\n- **URL:** https://arxiv.org/abs/2503.15724\n\n#### Differentiable Constrained Imitation Learning for Robot Motion Planning (arXiv 2023)\n- **Authors:** Christopher Diehl, Janis Adamek, Martin Krueger, Frank Hoffmann, Torsten Bertram\n- **Core method:** Integrates hard spatio-temporal constraints (dynamics, safety/obstacle boundaries) into IL via differentiable optimization layers. Argues soft-constraint approaches (auxiliary losses) can fail catastrophically in OOD scenarios.\n- **Key results:** Hard constraint integration prevents safety violations that soft auxiliary losses cannot guarantee. Demonstrated on mobile robot and automated driving.\n- **Relation to our work:** **Counterpoint.** Explicitly argues against soft auxiliary loss approaches. Important for positioning our contribution: SDF auxiliary loss is practical for high-dimensional VLA policies where differentiable hard constraints are intractable, trading formal guarantees for scalability.\n- **URL:** https://arxiv.org/abs/2210.11796\n\n#### Composite SDF Networks for Collision-Free Motion of Articulated Robots (RA-L 2023)\n- **Authors:** Baolin Liu, Gedong Jiang, Fei Zhao, Xuesong Mei\n- *(See Section 3 for full details)*\n- **Relation to auxiliary loss:** Composite SDF network could serve as the geometric backbone for computing the SDF auxiliary loss in our VLA training pipeline.\n- **URL:** https://arxiv.org/abs/2306.04130\n\n---\n\n## Summary\n\n### Our positioning in the literature\n\nThis project -- adding SDF-based auxiliary loss to Pi0.5 VLA for collision avoidance -- sits at a unique intersection:\n\n1. **Training-time geometric safety for VLA:** No existing work trains VLA models with continuous geometric safety signals (SDF) as auxiliary supervision. AEGIS/VLSA uses inference-time CBF correction; SafeVLA uses RL-based constrained optimization; CoFreeVLA uses binary collision gating. Our approach is the only one that embeds rich, differentiable geometric supervision directly into IL training.\n\n2. **frozen_rate as evaluation metric:** No existing metric explicitly detects \"fake safety through inaction.\" The problem is acknowledged (FISOR, safe RL surveys), but no one has proposed a dedicated metric. This is a clear novelty.\n\n3. **SDF in VLA context:** SDF is well-established in traditional motion planning (RDF, CDF, iSDF) but has never been used as an auxiliary training signal within a VLA model. We bridge the gap between geometric planning and end-to-end VLA learning.\n\n### Key papers to cite\n\n| Paper | Why cite |\n|---|---|\n| VLSA/AEGIS (Hu et al., 2025) | Most direct competitor -- inference-time safety vs. our training-time safety |\n| SafeVLA (Zhang et al., NeurIPS 2025) | RL-based VLA safety alignment -- different paradigm to contrast |\n| CoFreeVLA (Zhai et al., 2026) | Closest architecture -- collision risk estimator alongside action output |\n| iSDF (Ortiz et al., RSS 2022) | Foundation for neural SDF representation |\n| RDF (Li et al., ICRA 2024) | Differentiable robot distance fields for articulated bodies |\n| FISOR (Zheng et al., ICLR 2024) | Acknowledges conservative policy collapse -- motivates frozen_rate |\n| Safety-Gymnasium (Ji et al., NeurIPS 2023) | Standard safe RL benchmark methodology |\n| Diehl et al. (2023) | Important counterpoint -- hard vs. soft safety constraints |\n\n### Key differentiators vs. closest competitors\n\n| | AEGIS/VLSA | SafeVLA | CoFreeVLA | **Ours** |\n|---|---|---|---|---|\n| Safety integration | Inference-time CBF-QP | RL fine-tuning (CMDP) | Inference-time gating | **Training-time auxiliary loss** |\n| Safety signal | Depth + detection | Learned cost | Binary collision | **Continuous SDF** |\n| Requires retraining? | No | Yes (RL) | No | **Yes (supervised)** |\n| Gradient quality | N/A | Sparse RL reward | Binary | **Dense, differentiable** |\n| Formal guarantee? | Yes (CBF) | Probabilistic | No | **No (soft constraint)** |\n| Scalability to VLA | Plug-and-play | Needs RL infra | Plug-and-play | **Native to IL pipeline** |\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/related_work_survey.md",
    "content": "# Related Work Survey: Pi0.5 + SDF Auxiliary Loss for Collision Avoidance\n\n**Date:** 2026-05-23\n\n---\n\n## 1. VLA Safety / Collision Avoidance\n\n#### SafeVLA: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning (NeurIPS 2025 Spotlight)\n- **Authors:** Borong Zhang et al. (PKU-Alignment)\n- **Core method:** Models VLA safety as a Constrained MDP (CMDP). Uses min-max optimization to align VLA policies against elicited safety risks via safe RL. Systematically elicits diverse unsafe behaviors, then constrains the policy to avoid them.\n- **Key results:** Reduces cumulative cost of safety violations by 83.58% vs. SOTA while maintaining task success rate (+3.85%).\n- **Relation to our work:** Competitor / complementary. SafeVLA uses RL-based constrained optimization at the policy level; we embed geometric safety (SDF) as an auxiliary loss during training. SafeVLA requires online RL fine-tuning, our SDF auxiliary loss is a simpler supervised signal. The two approaches could be combined.\n- **URL:** https://arxiv.org/abs/2503.03480\n\n#### VLSA (AEGIS): Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer (arXiv 2025)\n- **Authors:** Songqiao Hu, Zeyi Liu, Shuang Liu, Jun Cen, Zihan Meng, Xiao He (Tsinghua)\n- **Core method:** Adds a plug-and-play safety constraint (SC) layer based on Control Barrier Functions (CBF) on top of existing VLA models. Uses VLM-based safety assessment + open-set detection + depth, then a CBF-based QP solver minimally adjusts VLA actions to guarantee collision-free execution.\n- **Key results:** 59.16% improvement in obstacle avoidance rate and 17.25% increase in task success rate on SafeLIBERO benchmark. Outperforms Pi0.5 (68.13% vs 50.88%).\n- **Relation to our work:** **Most direct competitor.** Both add safety to VLA models, but AEGIS does it at **inference time** (post-hoc CBF-QP correction), while we integrate safety at **training time** via SDF auxiliary loss. Our approach learns inherently safer policies rather than relying on runtime corrections. AEGIS's SafeLIBERO benchmark is useful for evaluation.\n- **URL:** https://arxiv.org/abs/2512.11891\n\n#### CoFreeVLA: Collision-Free Dual-Arm Manipulation via VLA Model and Risk Estimation (arXiv 2026)\n- **Authors:** Xuanran Zhai, Binkai Ou, Qiaojun Yu, Ce Hao, Yaohua Liu et al.\n- **Core method:** Augments VLA with a short-horizon self-collision risk estimator from proprioception, visual embeddings, and planned actions. Gates risky commands and recovers to safe states. Risk estimator pre-trained with model-based collision labels.\n- **Key results:** Reduces self-collisions and improves success rates vs. RDT and APEX on five bimanual tasks.\n- **Relation to our work:** Technique to borrow. CoFreeVLA's collision risk estimator is conceptually similar to our SDF auxiliary head -- both predict a geometric safety signal alongside the action. Key difference: CoFreeVLA uses binary collision labels while we use continuous SDF values providing richer gradient information.\n- **URL:** https://arxiv.org/abs/2601.21712\n\n#### SAFE: Multitask Failure Detection for Vision-Language-Action Models (NeurIPS 2025)\n- **Authors:** Gu, Ju, Sun, Gilitschenski, Nishimura, Itkina, Shkurti\n- **Core method:** Learns a failure detector from VLA internal features that predicts task failure likelihood. Discovers that VLA feature spaces already encode success/failure information, enabling zero-shot failure detection on unseen tasks.\n- **Key results:** SOTA failure detection on OpenVLA, Pi0, and Pi0-FAST in sim and real.\n- **Relation to our work:** Complementary. SAFE detects failures post-hoc from VLA features rather than preventing them. Their finding that VLA features encode safety-relevant information supports our hypothesis that an SDF auxiliary head can effectively leverage VLA internal representations.\n- **URL:** https://arxiv.org/abs/2506.09937\n\n#### CompliantVLA-adaptor: VLM-Guided Variable Impedance Action for Safe Contact-Rich Manipulation (arXiv 2026)\n- **Authors:** (arXiv 2601.15541)\n- **Core method:** Augments VLA models with a VLM-informed context-aware variable impedance controller. VLM interprets task context to adapt stiffness/damping parameters, regulated by real-time force/torque feedback.\n- **Key results:** Improves safety and effectiveness in contact-rich tasks vs. standard position-only VLA outputs.\n- **Relation to our work:** Complementary -- addresses force/compliance safety rather than collision geometry. Could be combined: SDF prevents collisions in free space, impedance control handles intentional contact phases.\n- **URL:** https://arxiv.org/abs/2601.15541\n\n**Novelty gap:** No existing work integrates SDF-based geometric supervision as an auxiliary training loss within a VLA model. The landscape:\n\n| Approach | When | Safety signal | Paper |\n|---|---|---|---|\n| RL constrained optimization | Training (RL) | Cost from unsafe rollouts | SafeVLA |\n| CBF/QP post-hoc correction | Inference | Control barrier function | VLSA/AEGIS |\n| Collision risk estimator | Inference (gating) | Binary collision prediction | CoFreeVLA |\n| Failure detection | Post-hoc | VLA feature analysis | SAFE |\n| Impedance control | Inference | Force/torque feedback | CompliantVLA-adaptor |\n| **SDF auxiliary loss (ours)** | **Training (supervised)** | **Continuous signed distance** | **None** |\n\n---\n\n## 2. Fake Safety / Action Collapse in Robotics\n\n**Overall assessment: Significant novelty gap.** No paper directly addresses the concept of a \"frozen_rate\" metric -- detecting and penalizing robots that achieve low collision rates merely by ceasing to move. The closest work falls into: (1) overly conservative safe RL policies, (2) action mode collapse in imitation/offline RL, (3) diffusion approaches handling multimodal actions.\n\n#### FISOR: Safe Offline RL with Feasibility-Guided Diffusion Model (ICLR 2024)\n- **Authors:** Yinan Zheng, Jianxiong Li, Dongjie Yu, Yujie Yang, Shengbo Eben Li, Xianyuan Zhan, Jingjing Liu\n- **Core method:** Decouples safety constraint adherence, reward maximization, and offline policy learning. Uses Hamilton-Jacobi reachability to identify feasible region, then extracts policy via energy-guided diffusion model.\n- **Key results:** Zero constraint violation in all tested tasks while achieving top returns. Explicitly addresses the tension where hard safety constraints can yield \"overly conservative (near zero-reward) policies.\"\n- **Relation to our work:** Acknowledges that naive safe offline RL can produce degenerate policies but doesn't define a metric to detect this. A frozen_rate metric would complement FISOR by quantifying when safety is achieved through inaction vs. genuine collision avoidance.\n- **URL:** https://arxiv.org/abs/2401.10700\n\n#### POLICEd RL: Learning Closed-Loop Robot Control with Provable Hard Constraints (RSS 2024)\n- **Authors:** Jean-Baptiste Bouvier, Kartik Nagpal, Negar Mehr\n- **Core method:** Makes the learned policy affine near unsafe state boundaries, using this affine region as a repulsive buffer that provably prevents constraint violations.\n- **Key results:** Formal guarantees of hard constraint satisfaction in closed-loop execution.\n- **Relation to our work:** Repulsive buffers near unsafe regions can cause robots to slow down or stop near obstacles -- exactly what frozen_rate detects. The paper does not measure or discuss this failure mode.\n- **URL:** https://arxiv.org/abs/2403.13297\n\n#### Learning on One Mode (LOM): Addressing Multi-modality in Offline RL (ICLR 2025)\n- **Authors:** Mianchu Wang, Yue Jin, Giovanni Montana\n- **Core method:** Uses GMM to decompose offline dataset's action distribution into modes, then applies weighted IL on only the highest-return mode. Avoids \"mode averaging\" where learning from multimodal data collapses to the mean (often near-zero) action.\n- **Key results:** Outperforms standard offline RL methods on D4RL benchmarks, particularly in multi-modal scenarios.\n- **Relation to our work:** Mode averaging is a direct mechanism producing frozen/near-zero actions: opposing motion directions average to zero velocity. frozen_rate is a diagnostic to detect when mode collapse produces inaction.\n- **URL:** https://arxiv.org/abs/2412.03258\n\n#### The Pitfalls of Imitation Learning when Actions are Continuous (COLT 2025)\n- **Authors:** Max Simchowitz, Daniel Pfrommer, Ali Jadbabaie\n- **Core method:** Theoretical analysis proving that for stable dynamics with smooth deterministic experts, any smooth deterministic imitator suffers execution error exponentially larger than training error.\n- **Key results:** Formalizes why BC fails due to closed-loop feedback between imperfect policy and dynamics. Shows \"sufficiently spread\" expert trajectory distributions can mitigate the problem.\n- **Relation to our work:** Provides theoretical grounding for why IL policies can degenerate, including potential freezing when the policy becomes uncertain and regresses toward mean actions. frozen_rate operationalizes detection of one specific failure mode this theory predicts.\n- **URL:** https://arxiv.org/abs/2503.09722\n\n#### CAPE: Context-Aware Diffusion Policy via Proximal Mode Expansion for Collision Avoidance (arXiv 2025)\n- **Authors:** (arXiv 2511.22773)\n- **Core method:** Expands trajectory distribution modes of a diffusion policy using context-aware priors and guided denoising. Generates initial plans, executes short prefixes, then re-denoises with collision-aware guidance.\n- **Key results:** Up to 26% (sim) and 80% (real) higher success rates in cluttered unseen environments.\n- **Relation to our work:** Addresses limited mode coverage in diffusion policies for collision avoidance. When a policy lacks diverse trajectory modes, it may freeze. Mode expansion is a generation-side solution; frozen_rate is the evaluation-side diagnostic.\n- **URL:** https://arxiv.org/abs/2511.22773\n\n**Novelty of frozen_rate:** The problem is acknowledged (FISOR, safe RL surveys note \"overly conservative policies\"), but no existing metric explicitly measures the fraction of time a robot is stationary when it should be acting. Treating frozen behavior as safety metric gaming is an original contribution.\n\n---\n\n## 3. SDF in Robot Manipulation\n\n#### Representing Robot Geometry as Distance Fields (RDF) (ICRA 2024)\n- **Authors:** Yiming Li, Yan Zhang, Amirreza Razmjoo, Sylvain Calinon\n- **Core method:** Represents robot geometry as Robot Distance Fields using Bernstein polynomials to encode signed distance for each link. Continuous and differentiable, enabling direct use as cost functions for optimization-based planning.\n- **Key results:** Demonstrated on 7-axis Franka for collision avoidance and whole-body manipulation, including dual-arm settings.\n- **Relation to our work:** Borrowable technique. The Bernstein polynomial SDF encoding for robot links could compute the robot-side SDF in our auxiliary loss, providing accurate differentiable distance queries.\n- **URL:** https://arxiv.org/abs/2307.00533\n\n#### Configuration Space Distance Fields for Manipulation Planning (RSS 2024)\n- **Authors:** Yiming Li, Xuemin Chi, Amirreza Razmjoo, Sylvain Calinon\n- **Core method:** Computes Signed Distance Fields in configuration space (CDF) rather than task space. Neural MLP representation for compact, continuous C-space distances. Zero-level-set matches SDF, but CDF level sets have unit-norm gradients enabling one-step IK.\n- **Key results:** Fewer iterations than task-space SDF for contact planning on 7-axis Franka.\n- **Relation to our work:** Borrowable technique. CDF provides collision avoidance directly in joint space -- the space VLA models output actions in. Could yield better gradients than task-space SDF for the auxiliary loss.\n- **URL:** https://arxiv.org/abs/2406.01137\n\n#### iSDF: Real-Time Neural Signed Distance Fields for Robot Perception (RSS 2022)\n- **Authors:** Joseph Ortiz, Alexander Clegg, Jing Dong, Edgar Sucar, David Novotny, Michael Zollhoefer, Mustafa Mukadam\n- **Core method:** Continual learning system training a neural network online to map 3D coordinates to signed distances from a stream of posed depth images. Self-supervised, room-scale, real-time.\n- **Key results:** More accurate reconstructions and better collision cost/gradient approximations vs. voxel-grid baselines.\n- **Relation to our work:** Borrowable technique. Demonstrates how to construct differentiable SDF representations from depth images in real time -- exactly what's needed to compute SDF auxiliary loss during training or inference.\n- **URL:** https://arxiv.org/abs/2204.02296\n\n#### Neural NMPC through SDF Encoding for Collision Avoidance (IJRR 2025)\n- **Authors:** Martin Jacquet, Marvin Harms, Kostas Alexis\n- **Core method:** Encodes range images into SDF via convolutional encoder (latent vector) + MLP decoder (spatial SDF). SDF parametrizes position constraints in a velocity-tracking NMPC for map-free collision avoidance.\n- **Key results:** Real-world collision avoidance in forest environments for aerial robots with adversarial references.\n- **Relation to our work:** Borrowable architecture. The encoder-decoder (visual observation -> latent -> SDF) is transferable to our vision-conditioned SDF module for the auxiliary loss.\n- **URL:** https://arxiv.org/abs/2511.21312\n\n#### Composite SDF Networks for Collision-Free Motion of Articulated Robots (RA-L 2023)\n- **Authors:** Baolin Liu, Gedong Jiang, Fei Zhao, Xuesong Mei\n- **Core method:** Learns composite SDF networks to represent signed distance of articulated robots per link, enabling fast batch minimum distance estimation. Integrates into stochastic trajectory planner.\n- **Key results:** Collision-free, time-optimal motion generation with fast and accurate distance estimation.\n- **Relation to our work:** Borrowable technique. Composite SDF network architecture for articulated robots provides more accurate collision distance gradients for the auxiliary loss than scene-level SDF.\n- **URL:** https://arxiv.org/abs/2306.04130\n\n---\n\n## 4. Safety Metrics for Robot Learning\n\n#### SafeVLA (NeurIPS 2025 Spotlight)\n- *(See Section 1 for full details)*\n- **Metrics relevance:** Defines cumulative cost and violation rate for VLA manipulation evaluation, analogous to our collision_rate and frozen_rate.\n- **URL:** https://arxiv.org/abs/2503.03480\n\n#### Safety-Gymnasium: A Unified Safe RL Benchmark (NeurIPS 2023 D&B)\n- **Authors:** Jiaming Ji, Borong Zhang, Jiayi Zhou, Xuehai Pan et al.\n- **Core method:** Unified environment suite for safe RL (single/multi-agent) + SafePO library of 16 SOTA safe RL algorithms. Standardizes task definitions, constraint specifications, evaluation protocols.\n- **Key results:** Benchmarks 16 safe RL algorithms with standardized metrics: cost rate, cost return, reward-cost trade-off curves.\n- **Relation to our work:** \"Cost rate\" (violations per timestep) is conceptually identical to collision_rate. Evaluation protocol -- measuring task performance and safety simultaneously -- provides methodological template.\n- **URL:** https://arxiv.org/abs/2310.12567\n\n#### Robot Learning as an Empirical Science: Best Practices for Policy Evaluation (arXiv 2024)\n- **Authors:** Hadas Kress-Gazit, Kunimatsu Hashimoto, Naveen Kuppuswamy et al.\n- **Core method:** Surveys evaluation practices in robot learning. Argues the field over-relies on success rate. Proposes reporting multiple complementary metrics including safety-related ones and statistical significance.\n- **Key results:** Meta-analysis showing most papers report only success rate. Complementary metrics (collision rate, completion time, smoothness) reveal important behavioral differences invisible to success rate.\n- **Relation to our work:** Directly supports using collision_rate and frozen_rate as complementary metrics beyond success rate. Provides methodological justification for multi-metric evaluation.\n- **URL:** https://arxiv.org/abs/2409.09491\n\n#### GUARD: A Safe RL Benchmark (arXiv 2023)\n- **Authors:** Weiye Zhao, Ruixuan Liu, Rui Chen, Tianhao Wei, Yifan Sun, Changliu Liu (CMU)\n- **Core method:** Generalized Unified SAfe RL Development benchmark with configurable agents, tasks, and safety constraints. Supports state, action, and joint constraints.\n- **Key results:** Comprehensive comparison of safe RL algorithms (CPO, PPO-Lagrangian, TRPO-Lagrangian) with constraint violation rate, episodic cost, reward-cost Pareto frontiers.\n- **Relation to our work:** Flexible constraint specification framework is relevant for defining collision avoidance as a state constraint. Systematic comparison methodology parallels our evaluation approach.\n- **URL:** https://arxiv.org/abs/2305.13681\n\n#### Vision-Language-Action Safety: Threats, Challenges, Evaluations, and Mechanisms (arXiv 2026)\n- **Authors:** Qi Li et al.\n- **Core method:** Comprehensive survey of VLA safety covering five risk dimensions: irreversible physical consequences, multimodal attack surfaces, real-time latency constraints, error propagation over long horizons, data supply chain vulnerabilities.\n- **Key results:** VLA safety evaluation requires metrics beyond traditional RL safety, including physical damage assessment, constraint violation severity, and temporal propagation of unsafe states.\n- **Relation to our work:** Most directly relevant survey -- specifically addresses safety evaluation for VLA models. Contextualizes our collision_rate and frozen_rate metrics within the broader VLA safety landscape.\n- **URL:** https://arxiv.org/abs/2604.23775\n\n---\n\n## 5. Auxiliary Loss for Safety\n\n#### RAIL: Reachability-Aided Imitation Learning for Safe Policy Execution (ICRA 2025)\n- **Authors:** Wonsuhk Jung, Dennis Anthony, Utkarsh A. Mishra et al.\n- **Core method:** Builds a reachability-based safety filter on top of IL policies. Uses polynomial zonotopes to overapproximate the robot's continuous-time swept volume for fast collision checking, then intervenes when IL policy's action would collide.\n- **Key results:** 0% collision rate vs. 5-35% for baseline IL policies, while maintaining task success.\n- **Relation to our work:** Competitor / complementary. RAIL adds safety as a post-hoc filter over IL policies; we bake safety into the policy during training via SDF auxiliary loss. These strategies could be combined.\n- **URL:** https://arxiv.org/abs/2409.19190\n\n#### Learning to Recover for Safe RL (arXiv 2023)\n- **Authors:** Haoyu Wang et al.\n- **Core method:** Three-stage architecture (TU-Recovery) where safety critic and recovery policy are learned before task training. An auxiliary reward mitigates the \"adversarial phenomenon\" between task and recovery policies.\n- **Key results:** Outperforms unconstrained baselines in both reward and constraint violations. Auxiliary reward significantly reduces constraint violations.\n- **Relation to our work:** Borrowable technique. The idea of using an auxiliary reward/loss to shape task policy toward safety-aware behavior is directly analogous to our SDF auxiliary loss. Key difference: RL with learned recovery vs. our geometric loss in IL.\n- **URL:** https://arxiv.org/abs/2309.11907\n\n#### Reward Training Wheels: Adaptive Auxiliary Rewards for Robotics RL (IROS 2025)\n- **Authors:** Linji Wang, Tong Xu, Yuanjie Lu, Xuesu Xiao\n- **Core method:** Teacher-student framework (RTW) where a teacher monitors training signals and dynamically adjusts auxiliary reward weights during RL training.\n- **Key results:** Outperforms expert-designed rewards by 2.35% success rate, 122.62% in off-road mobility. 35% and 3x faster training.\n- **Relation to our work:** Borrowable technique. Adaptive weighting of auxiliary rewards is directly relevant -- a fixed SDF loss weight may be suboptimal across training stages. RTW's dynamic scheduling could improve SDF loss integration.\n- **URL:** https://arxiv.org/abs/2503.15724\n\n#### Differentiable Constrained Imitation Learning for Robot Motion Planning (arXiv 2023)\n- **Authors:** Christopher Diehl, Janis Adamek, Martin Krueger, Frank Hoffmann, Torsten Bertram\n- **Core method:** Integrates hard spatio-temporal constraints (dynamics, safety/obstacle boundaries) into IL via differentiable optimization layers. Argues soft-constraint approaches (auxiliary losses) can fail catastrophically in OOD scenarios.\n- **Key results:** Hard constraint integration prevents safety violations that soft auxiliary losses cannot guarantee. Demonstrated on mobile robot and automated driving.\n- **Relation to our work:** **Counterpoint.** Explicitly argues against soft auxiliary loss approaches. Important for positioning our contribution: SDF auxiliary loss is practical for high-dimensional VLA policies where differentiable hard constraints are intractable, trading formal guarantees for scalability.\n- **URL:** https://arxiv.org/abs/2210.11796\n\n#### Composite SDF Networks for Collision-Free Motion of Articulated Robots (RA-L 2023)\n- **Authors:** Baolin Liu, Gedong Jiang, Fei Zhao, Xuesong Mei\n- *(See Section 3 for full details)*\n- **Relation to auxiliary loss:** Composite SDF network could serve as the geometric backbone for computing the SDF auxiliary loss in our VLA training pipeline.\n- **URL:** https://arxiv.org/abs/2306.04130\n\n---\n\n## Summary\n\n### Our positioning in the literature\n\nThis project -- adding SDF-based auxiliary loss to Pi0.5 VLA for collision avoidance -- sits at a unique intersection:\n\n1. **Training-time geometric safety for VLA:** No existing work trains VLA models with continuous geometric safety signals (SDF) as auxiliary supervision. AEGIS/VLSA uses inference-time CBF correction; SafeVLA uses RL-based constrained optimization; CoFreeVLA uses binary collision gating. Our approach is the only one that embeds rich, differentiable geometric supervision directly into IL training.\n\n2. **frozen_rate as evaluation metric:** No existing metric explicitly detects \"fake safety through inaction.\" The problem is acknowledged (FISOR, safe RL surveys), but no one has proposed a dedicated metric. This is a clear novelty.\n\n3. **SDF in VLA context:** SDF is well-established in traditional motion planning (RDF, CDF, iSDF) but has never been used as an auxiliary training signal within a VLA model. We bridge the gap between geometric planning and end-to-end VLA learning.\n\n### Key papers to cite\n\n| Paper | Why cite |\n|---|---|\n| VLSA/AEGIS (Hu et al., 2025) | Most direct competitor -- inference-time safety vs. our training-time safety |\n| SafeVLA (Zhang et al., NeurIPS 2025) | RL-based VLA safety alignment -- different paradigm to contrast |\n| CoFreeVLA (Zhai et al., 2026) | Closest architecture -- collision risk estimator alongside action output |\n| iSDF (Ortiz et al., RSS 2022) | Foundation for neural SDF representation |\n| RDF (Li et al., ICRA 2024) | Differentiable robot distance fields for articulated bodies |\n| FISOR (Zheng et al., ICLR 2024) | Acknowledges conservative policy collapse -- motivates frozen_rate |\n| Safety-Gymnasium (Ji et al., NeurIPS 2023) | Standard safe RL benchmark methodology |\n| Diehl et al. (2023) | Important counterpoint -- hard vs. soft safety constraints |\n\n### Key differentiators vs. closest competitors\n\n| | AEGIS/VLSA | SafeVLA | CoFreeVLA | **Ours** |\n|---|---|---|---|---|\n| Safety integration | Inference-time CBF-QP | RL fine-tuning (CMDP) | Inference-time gating | **Training-time auxiliary loss** |\n| Safety signal | Depth + detection | Learned cost | Binary collision | **Continuous SDF** |\n| Requires retraining? | No | Yes (RL) | No | **Yes (supervised)** |\n| Gradient quality | N/A | Sparse RL reward | Binary | **Dense, differentiable** |\n| Formal guarantee? | Yes (CBF) | Probabilistic | No | **No (soft constraint)** |\n| Scalability to VLA | Plug-and-play | Needs RL infra | Plug-and-play | **Native to IL pipeline** |\n"
  }
}
```

</details>

---

### Tool result

_source line 164 · 2026-05-23T03:06:17.611308+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/related_work_survey.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_survey_20260523T030015",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 165 · 2026-05-23T03:06:17.611534+00:00_

报告已写入 `artifacts/related_work_survey.md`。

**核心发现：**

- **方向1 (VLA Safety)**: 找到5篇直接相关论文（SafeVLA, AEGIS, CoFreeVLA, SAFE, CompliantVLA-adaptor）。最直接的竞品是 AEGIS（推理时 CBF 修正）和 SafeVLA（RL 约束优化）。**没有任何工作在训练时用连续 SDF 信号做 auxiliary loss**——这是明确的 novelty gap。

- **方向2 (Fake Safety)**: **显著 novelty gap**。"overly conservative policy"被多篇论文提及（FISOR, POLICEd RL），但无人定义指标来检测"因不动而安全"。frozen_rate 是原创贡献。

- **方向3 (SDF in Manipulation)**: SDF 在传统规划中成熟（RDF, CDF, iSDF），但从未用于 VLA 模型的 auxiliary training signal。我们在几何规划和端到端 VLA 学习之间架桥。

- **方向4 (Safety Metrics)**: Safety-Gymnasium、GUARD 提供方法论模板，VLA Safety Survey (2026) 直接讨论 VLA 安全评估。

- **方向5 (Auxiliary Loss)**: RAIL（推理时安全滤波）、Reward Training Wheels（自适应权重调度）可借鉴；Diehl et al. 是重要反方——主张硬约束优于软 auxiliary loss，需要在论文中讨论这个 trade-off。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_related_work_survey_20260523T030015"
}
```

</details>

---
