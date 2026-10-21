# research corl2026 literature update

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 32
- **Recorded user turns:** 0
- **Tool calls:** 16
- **Original source:** `logs/chats/worker_research_corl2026-literature-update_20260515T013205.jsonl`
- **Structured JSON:** [`71bb20ef1b3ae946ee05.json`](../../sessions/71/71bb20ef1b3ae946ee05.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

32 recorded events

### Tool call

_source line 1 · 2026-05-15T01:33:26.485154+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,mcp__agent-ml-research__save_project_file",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_corl2026-literature-update_20260515T013205",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,mcp__agent-ml-research__save_project_file",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-15T01:33:26.485661+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_corl2026-literature-update_20260515T013205",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-15T01:33:26.485954+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "VLA action correction sample selection uncertainty 2025 2026 robot manipulation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_corl2026-literature-update_20260515T013205",
  "tool": "WebSearch",
  "tool_args": {
    "query": "VLA action correction sample selection uncertainty 2025 2026 robot manipulation"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-15T01:33:26.486169+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "conformal prediction robotics manipulation 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_corl2026-literature-update_20260515T013205",
  "tool": "WebSearch",
  "tool_args": {
    "query": "conformal prediction robotics manipulation 2025 2026"
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-15T01:33:26.486397+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ReconVLA SC-VLA VLA-Pilot action selection robot"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_corl2026-literature-update_20260515T013205",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ReconVLA SC-VLA VLA-Pilot action selection robot"
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-15T01:33:26.486594+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "flow matching VLA robot policy 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_corl2026-literature-update_20260515T013205",
  "tool": "WebSearch",
  "tool_args": {
    "query": "flow matching VLA robot policy 2025 2026"
  }
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-15T01:33:26.486785+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "LIBERO benchmark robot manipulation 2025 2026 new results"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_corl2026-literature-update_20260515T013205",
  "tool": "WebSearch",
  "tool_args": {
    "query": "LIBERO benchmark robot manipulation 2025 2026 new results"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-15T01:33:26.487028+00:00_

Web search results for query: "ReconVLA SC-VLA VLA-Pilot action selection robot"

Links: [{"title":"ReconVLA: Reconstructive Vision-Language-Action Model as Effective Robot Perceiver","url":"https://arxiv.org/html/2508.10333v1"},{"title":"GitHub - OpenHelix-Team/ReconVLA: Official implementation of ReconVLA: Reconstructive Vision-Language-Action Model as Effective Robot Perceiver. · GitHub","url":"https://github.com/OpenHelix-Team/ReconVLA"},{"title":"ReconVLA: An Uncertainty-Guided and Failure-Aware Vision-Language-Action Framework for Robotic Control","url":"https://arxiv.org/html/2604.16677v1"},{"title":"Vision Language Action Models (VLA) & Policies for Robots","url":"https://learnopencv.com/vision-language-action-models-lerobot-policy/"},{"title":"[2508.10333] ReconVLA: Reconstructive Vision-Language-Action Model as Effective Robot Perceiver","url":"https://arxiv.org/abs/2508.10333"},{"title":"GitHub - jonyzhang2023/awesome-embodied-vla-va-vln: A curated list of state-of-the-art research in embodied AI, focusing on vision-language-action (VLA) models, vision-language navigation (VLN), and related multimodal learning approaches. · GitHub","url":"https://github.com/jonyzhang2023/awesome-embodied-vla-va-vln"},{"title":"[PDF] ReconVLA: Reconstructive Vision-Language-Action Model as Effective Robot Perceiver | Semantic Scholar","url":"https://www.semanticscholar.org/paper/ReconVLA:-Reconstructive-Vision-Language-Action-as-Song-Zhou/c87ea2afcd9212e5128e01daf17c733d285ac345"},{"title":"Vision-language-action model - Wikipedia","url":"https://en.wikipedia.org/wiki/Vision-language-action_model"},{"title":"GitHub - openvla/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub","url":"https://github.com/openvla/openvla"},{"title":"VLAS: Vision-Language-Action Model with Speech Instructions for Customized Robot Manipulation | OpenReview","url":"https://openreview.net/forum?id=K4FAFNRpko"}]

Based on the search results, here's what
…[truncated 1425 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_corl2026-literature-update_20260515T013205",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-15T01:33:26.487342+00:00_

Web search results for query: "conformal prediction robotics manipulation 2025 2026"

Links: [{"title":"Conformal Prediction for Robotics | xLAB: Safe Autonomous Systems Lab","url":"https://xlab.upenn.edu/conformal-prediction-robotics/"},{"title":"End-to-End Conformal Prediction for Trajectory Optimization | OpenReview","url":"https://openreview.net/forum?id=ilcsm8B7Pe"},{"title":"Formal Verification and Control With Conformal Prediction: Practical Safety Guarantees For Autonomous Systems | IEEE Journals & Magazine | IEEE Xplore","url":"https://ieeexplore.ieee.org/iel8/5488303/11274416/11274485.pdf"},{"title":"A Review of Theoretical Advances and Practical Applications of Conformal Prediction in China | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-032-15120-9_11"},{"title":"Conformal Prediction Conference 2026","url":"https://copa-conference.com/"},{"title":"Conformal Prediction Conference 2025","url":"https://copa-conference.com/copa2025/"},{"title":"GitHub - jonyzhang2023/awesome-embodied-vla-va-vln: A curated list of state-of-the-art research in embodied AI, focusing on vision-language-action (VLA) models, vision-language navigation (VLN), and related multimodal learning approaches. · GitHub","url":"https://github.com/jonyzhang2023/awesome-embodied-vla-va-vln"},{"title":"Conformal prediction - Google Groups","url":"https://groups.google.com/g/conformal-prediction"},{"title":"What foundation models can bring for robot learning in manipulation: A survey - Dingzhe Li, Yixiang Jin, YuHao Sun, Yong A, Hongze Yu, Jun Shi, Xiaoshuai Hao, Peng Hao, Huaping Liu, Xiang Li, Xinde Li, Fuchun Sun, Jianwei Zhang, Bin Fang, 2025","url":"https://journals.sagepub.com/doi/10.1177/02783649251390579"},{"title":"Extreme conformal prediction: Reliable intervals for high-impact events | Extremes | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10687-026-00536-9"}]

Here are the search results for "conformal prediction robotics ma
…[truncated 1746 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_corl2026-literature-update_20260515T013205",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-15T01:33:26.487629+00:00_

Web search results for query: "VLA action correction sample selection uncertainty 2025 2026 robot manipulation"

Links: [{"title":"VLA-OPD: Bridging Offline SFT and Online RL for Vision-Language-Action Models via On-Policy Distillation","url":"https://arxiv.org/html/2603.26666v1"},{"title":"Do World Action Models Generalize Better than VLAs? A Robustness Study","url":"https://arxiv.org/html/2603.22078v1"},{"title":"State of Vision-Language-Action (VLA) Research at ICLR 2026 – Moritz Reuss","url":"https://mbreuss.github.io/blog_post_iclr_26_vla.html"},{"title":"GitHub - jonyzhang2023/awesome-embodied-vla-va-vln: A curated list of state-of-the-art research in embodied AI, focusing on vision-language-action (VLA) models, vision-language navigation (VLN), and related multimodal learning approaches. · GitHub","url":"https://github.com/jonyzhang2023/awesome-embodied-vla-va-vln"},{"title":"Multimodal fusion with vision-language-action models for robotic manipulation: A systematic review - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S1566253525011248"},{"title":"GitHub - OpenDriveLab/WholebodyVLA: [ICLR 2026] Towards Unified Latent VLA for Whole-body Loco-manipulation Control · GitHub","url":"https://github.com/OpenDriveLab/WholebodyVLA"},{"title":"Pure Vision Language Action (VLA) Models: A Comprehensive Survey","url":"https://arxiv.org/html/2509.19012v1"},{"title":"2025-9-22 A Vision-Language-Action-Critic Model","url":"https://arxiv.org/pdf/2509.15937"},{"title":"World Model for Robot Learning: A Comprehensive Survey","url":"https://arxiv.org/html/2605.00080"},{"title":"FPC-VLA: A Vision-Language-Action Framework with a Supervisor for Failure Prediction and Correction - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S095741742600655X"}]

I've completed a web search for your query about VLA (Vision-Language-Action) models with focus on action correction, sample selection, uncertainty, and robot manipulation research
…[truncated 1455 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_corl2026-literature-update_20260515T013205",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-15T01:33:26.487911+00:00_

Web search results for query: "flow matching VLA robot policy 2025 2026"

Links: [{"title":"Rohit Bandaru | Foundation Models for Robotics: Vision-Language-Action (VLA)","url":"https://rohitbandaru.github.io/blog/Foundation-Models-for-Robotics-VLA/"},{"title":"Vision-language-action model - Wikipedia","url":"https://en.wikipedia.org/wiki/Vision-language-action_model"},{"title":"VLM, VLA, Diffusion Policy, Flow Matching in Robotics | by Ranko Mosic | Medium","url":"https://ranko-mosic.medium.com/vla-9bd14b1a23ee"},{"title":"Pure Vision Language Action (VLA) Models: A Comprehensive Survey","url":"https://arxiv.org/html/2509.19012v1"},{"title":"GitHub - jonyzhang2023/awesome-embodied-vla-va-vln: A curated list of state-of-the-art research in embodied AI, focusing on vision-language-action (VLA) models, vision-language navigation (VLN), and related multimodal learning approaches. · GitHub","url":"https://github.com/jonyzhang2023/awesome-embodied-vla-va-vln"},{"title":"Vision-Language-Action Models and the Search for a Generalist Robot Policy","url":"https://itcanthink.substack.com/p/vision-language-action-models-and"},{"title":"Vision Language Action Models (VLA) & Policies for Robots","url":"https://learnopencv.com/vision-language-action-models-lerobot-policy/"},{"title":"Large VLM-based Vision-Language-Action Models for Robotic Manipulation: A Survey","url":"https://arxiv.org/html/2508.13073v1"},{"title":"π0: A Vision-Language-Action Flow Model for General Robot Control","url":"https://www.pi.website/download/pi0.pdf"},{"title":"VLS: Steering Pretrained Robot Policies via Vision–Language Models","url":"https://arxiv.org/html/2602.03973v1"}]

Based on the search results, here's what I found regarding flow matching VLA robot policy in 2025-2026:

## Key Developments

**Flow Matching as a Core Technology:**
Flow matching is more effective at generating continuous actions, though it is slower to train than autoregressive architectures. Flow matching can result in faster i
…[truncated 1329 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_corl2026-literature-update_20260515T013205",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-15T01:33:26.488204+00:00_

Web search results for query: "LIBERO benchmark robot manipulation 2025 2026 new results"

Links: [{"title":"GitHub - Lifelong-Robot-Learning/LIBERO: Benchmarking Knowledge Transfer in Lifelong Robot Learning · GitHub","url":"https://github.com/Lifelong-Robot-Learning/LIBERO"},{"title":"LIBERO Benchmark: Vision-Language-Action in Robotics","url":"https://www.emergentmind.com/topics/libero"},{"title":"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning | OpenReview","url":"https://openreview.net/forum?id=xzEtNSuDJk"},{"title":"Do World Action Models Generalize Better than VLAs? A Robustness Study","url":"https://arxiv.org/html/2603.22078v1"},{"title":"[2306.03310] LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning","url":"https://arxiv.org/abs/2306.03310"},{"title":"[2510.13626] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/abs/2510.13626"},{"title":"LIBERO vs CALVIN (2026): Benchmark Comparison | Silicon Valley Robotics Center","url":"https://www.roboticscenter.ai/datasets/compare/libero-vs-calvin"},{"title":"LIBERO-PRO: Towards Robust and Fair Evaluation of ...","url":"https://arxiv.org/pdf/2510.03827"},{"title":"LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization","url":"https://arxiv.org/html/2510.03827v1"},{"title":"LIBERO: simulation benchmark for the study of lifelong robot learning | by Deepthi Karkada | Medium","url":"https://medium.com/@deepkarkada/libero-simulation-benchmark-for-the-study-of-lifelong-robot-learning-583b786a96f6"}]

Based on the web search results, here are the key findings on LIBERO benchmark robot manipulation results from 2025-2026:

## Recent Performance Results

Strong 2025-era VLA policies (OpenVLA, pi0, Octo variants) typically achieve 70-90% success on Spatial, Object, and Goal tasks, and 30-60% on LIBERO-100.

## 2025-2026 Developments

Several important extensions and analyses have emerged:

**LIB
…[truncated 1315 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_corl2026-literature-update_20260515T013205",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-15T01:33:26.488738+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arXiv 2604.16677 ReconVLA uncertainty-guided failure-aware"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_corl2026-literature-update_20260515T013205",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arXiv 2604.16677 ReconVLA uncertainty-guided failure-aware"
  }
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-15T01:33:26.488970+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "SC-VLA sample consensus vision language action model robot 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_corl2026-literature-update_20260515T013205",
  "tool": "WebSearch",
  "tool_args": {
    "query": "SC-VLA sample consensus vision language action model robot 2025"
  }
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-15T01:33:26.489158+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACoT-VLA action chain of thought VLA robot 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_corl2026-literature-update_20260515T013205",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACoT-VLA action chain of thought VLA robot 2025 2026"
  }
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-15T01:33:26.489367+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "VLA-Pilot multi-sample selection robot manipulation 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_corl2026-literature-update_20260515T013205",
  "tool": "WebSearch",
  "tool_args": {
    "query": "VLA-Pilot multi-sample selection robot manipulation 2025"
  }
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-15T01:33:26.489557+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "VLAC vision language action critic robot manipulation 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_corl2026-literature-update_20260515T013205",
  "tool": "WebSearch",
  "tool_args": {
    "query": "VLAC vision language action critic robot manipulation 2025"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-15T01:33:26.489772+00:00_

Web search results for query: "arXiv 2604.16677 ReconVLA uncertainty-guided failure-aware"

Links: [{"title":"ReconVLA: An Uncertainty-Guided and Failure-Aware Vision-Language-Action Framework for Robotic Control","url":"https://arxiv.org/html/2604.16677v1"},{"title":"Dyna-Style Safety Augmented Reinforcement Learning: Staying Safe in the Face of Uncertainty","url":"https://arxiv.org/html/2604.25508"},{"title":"Entropy-Guided Loop: Achieving Reasoning through Uncertainty-Aware Generation","url":"https://arxiv.org/html/2509.00079v1"},{"title":"Machine Learning Jul 2025","url":"https://arxiv.org/list/cs.LG/2025-07?skip=25&show=2000"},{"title":"PiGGO: Physics-Guided Learnable Graph Kalman Filters for Virtual Sensing of Nonlinear Dynamic Structures under Uncertainty","url":"https://arxiv.org/html/2604.26593"},{"title":"Machine Learning Sep 2025","url":"https://arxiv.org/list/cs.LG/2025-09?skip=550&show=2000"},{"title":"[2604.13352] A Machine Learning Framework for Uncertainty-Calibrated Capability Decision under Finite Samples","url":"https://arxiv.org/abs/2604.13352"},{"title":"Towards Reliable Truth-Aligned Uncertainty Estimation in Large Language Models","url":"https://arxiv.org/html/2604.00445"},{"title":"[2604.11036] Uncertainty-Aware Web-Conditioned Scientific Fact-Checking","url":"https://arxiv.org/abs/2604.11036"},{"title":"Uncertainty-aware Generative Learning Path Recommendation with Cognition-Adaptive Diffusion","url":"https://arxiv.org/html/2604.14613"}]

Based on the search results, I found the paper you're looking for:

**ReconVLA: An Uncertainty-Guided and Failure-Aware Vision-Language-Action Framework** is a reliable conformal model that produces uncertainty-guided and failure-aware control signals.

Vision-language-action (VLA) models have emerged as generalist robotic controllers capable of mapping visual observations and natural language instructions to continuous action sequences, but VLAs provide no calibrated measure of confidence in their action p
…[truncated 730 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_corl2026-literature-update_20260515T013205",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-15T01:33:26.490049+00:00_

Web search results for query: "VLA-Pilot multi-sample selection robot manipulation 2025"

Links: [{"title":"OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://openvla.github.io/"},{"title":"Vision Language Action Models (VLA) & Policies for Robots","url":"https://learnopencv.com/vision-language-action-models-lerobot-policy/"},{"title":"GitHub - jonyzhang2023/awesome-embodied-vla-va-vln: A curated list of state-of-the-art research in embodied AI, focusing on vision-language-action (VLA) models, vision-language navigation (VLN), and related multimodal learning approaches. · GitHub","url":"https://github.com/jonyzhang2023/awesome-embodied-vla-va-vln"},{"title":"LangForce: Bayesian Decomposition of Vision Language ...","url":"https://arxiv.org/pdf/2601.15197"},{"title":"GitHub - OpenDriveLab/WholebodyVLA: [ICLR 2026] Towards Unified Latent VLA for Whole-body Loco-manipulation Control · GitHub","url":"https://github.com/OpenDriveLab/WholebodyVLA"},{"title":"Vision Language Action Models in Robotic Manipulation: A Systematic Review","url":"https://arxiv.org/html/2507.10672v1"},{"title":"Vision-language-action model - Wikipedia","url":"https://en.wikipedia.org/wiki/Vision-language-action_model"},{"title":"GitHub - JiuTian-VL/Large-VLM-based-VLA-for-Robotic-Manipulation: A curated list of large VLM-based VLA models for robotic manipulation. · GitHub","url":"https://github.com/JiuTian-VL/Large-VLM-based-VLA-for-Robotic-Manipulation"},{"title":"VLAbot: A human Vision–Language–Action models interaction framework for robotic assembly - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S0736584526000475"},{"title":"Shake-VLA: Vision-Language-Action Model-Based System for Bimanual Robotic Manipulations and Liquid Mixing | Proceedings of the 2025 ACM/IEEE International Conference on Human-Robot Interaction","url":"https://dl.acm.org/doi/10.5555/3721488.3721686"}]

I've performed a web search for "VLA-Pilot multi-sample selection robot manipu
…[truncated 1292 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_corl2026-literature-update_20260515T013205",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-15T01:33:26.490336+00:00_

Web search results for query: "ACoT-VLA action chain of thought VLA robot 2025 2026"

Links: [{"title":"GitHub - AgibotTech/ACoT-VLA: [CVPR 2026] Official implementation of \"ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models\" · GitHub","url":"https://github.com/AgibotTech/ACoT-VLA"},{"title":"[2601.11404] ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models","url":"https://arxiv.org/abs/2601.11404"},{"title":"[Quick Review] ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models","url":"https://liner.com/review/acotvla-action-chainofthought-for-visionlanguageaction-models"},{"title":"(PDF) ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models","url":"https://www.researchgate.net/publication/399875837_ACoT-VLA_Action_Chain-of-Thought_for_Vision-Language-Action_Models"},{"title":"ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models","url":"https://arxiv.org/html/2601.11404v2"},{"title":"[2503.22020] CoT-VLA: Visual Chain-of-Thought Reasoning for Vision-Language-Action Models","url":"https://arxiv.org/abs/2503.22020"},{"title":"Paper page - ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models","url":"https://huggingface.co/papers/2601.11404"},{"title":"ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models | alphaXiv","url":"https://www.alphaxiv.org/overview/2601.11404"},{"title":"CVPR Poster CoT-VLA: Visual Chain-of-Thought Reasoning for Vision-Language-Action Models","url":"https://cvpr.thecvf.com/virtual/2025/poster/33233"},{"title":"CoT-VLA: Visual Chain-of-Thought Reasoning for Vision-Language-Action Models","url":"https://openaccess.thecvf.com/content/CVPR2025/papers/Zhao_CoT-VLA_Visual_Chain-of-Thought_Reasoning_for_Vision-Language-Action_Models_CVPR_2025_paper.pdf"}]

## Search Results: ACoT-VLA

I found comprehensive information about ACoT-VLA. Here's what the search revealed:

### Overview

ACoT-VLA is a novel paradigm designed to bridge the fundamental sema
…[truncated 1262 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_corl2026-literature-update_20260515T013205",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-15T01:33:26.492656+00:00_

Web search results for query: "SC-VLA sample consensus vision language action model robot 2025"

Links: [{"title":"Vision-Language-Action Models for Robotics: A Review Towards Real-World Applications","url":"https://vla-survey.github.io/"},{"title":"Pure Vision Language Action (VLA) Models: A Comprehensive Survey","url":"https://arxiv.org/html/2509.19012v1"},{"title":"Vision-language-action model - Wikipedia","url":"https://en.wikipedia.org/wiki/Vision-language-action_model"},{"title":"GitHub - Psi-Robot/Awesome-VLA-Papers: Paper list in the survey: A Survey on Vision-Language-Action Models: An Action Tokenization Perspective · GitHub","url":"https://github.com/Psi-Robot/Awesome-VLA-Papers"},{"title":"arXiv:2506.01844v1 [cs.LG] 2 Jun 2025 SmolVLA: A vision-language-action model","url":"https://arxiv.org/pdf/2506.01844"},{"title":"NeurIPS Poster ChatVLA-2: Vision-Language-Action Model with Open-World Reasoning","url":"https://neurips.cc/virtual/2025/poster/120199"},{"title":"Multimodal fusion with vision-language-action models for robotic manipulation: A systematic review - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S1566253525011248"},{"title":"Vision-Language-Action (VLA) Models: Concepts, Progress, Applications and Challenges","url":"https://arxiv.org/html/2505.04769v2"},{"title":"[2505.04769] Vision-Language-Action (VLA) Models: Concepts, Progress, Applications and Challenges","url":"https://arxiv.org/abs/2505.04769"},{"title":"Vision Language Action Models in Robotic Manipulation: A Systematic Review","url":"https://arxiv.org/html/2507.10672v1"}]

The search results cover Vision-Language-Action (VLA) models in robotics broadly, but I don't see a specific model called "SC-VLA" mentioned in these results. The results show various VLA models from 2025 like Helix, GR00T N1, Gemini Robotics, π0, SmolVLA, ChatVLA-2, and others, but no reference to "SC-VLA" or "Sample Consensus VLA."

Let me search more specifically for SC-VLA:

Links: [{"t
…[truncated 2710 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_corl2026-literature-update_20260515T013205",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-15T01:33:26.492994+00:00_

Web search results for query: "VLAC vision language action critic robot manipulation 2025"

Links: [{"title":"GitHub - InternRobotics/VLAC: VLAC: A Vision-Language-Action-Critic Model for Robotic Real-World Reinforcement Learning · GitHub","url":"https://github.com/InternRobotics/VLAC"},{"title":"VLAC: A Generalist Action-Critic Model via Pair-wise Progress Understanding | OpenReview","url":"https://openreview.net/forum?id=PmYX0XiQQ0"},{"title":"2025-9-22 A Vision-Language-Action-Critic Model","url":"https://arxiv.org/pdf/2509.15937"},{"title":"[2509.15937] A Vision-Language-Action-Critic Model for Robotic Real-World Reinforcement Learning","url":"https://arxiv.org/abs/2509.15937"},{"title":"Paper page - A Vision-Language-Action-Critic Model for Robotic Real-World Reinforcement Learning","url":"https://huggingface.co/papers/2509.15937"},{"title":"A Vision-Language-Action-Critic Model for Robotic Real-World Reinforcement Learning","url":"https://arxiv.org/html/2509.15937v1"},{"title":"GitHub - JiuTian-VL/Large-VLM-based-VLA-for-Robotic-Manipulation: A curated list of large VLM-based VLA models for robotic manipulation. · GitHub","url":"https://github.com/JiuTian-VL/Large-VLM-based-VLA-for-Robotic-Manipulation"},{"title":"[Quick Review] A Vision-Language-Action-Critic Model for Robotic Real-World\\n Reinforcement Learning","url":"https://liner.com/review/visionlanguageactioncritic-model-for-robotic-realworld-reinforcement-learning"},{"title":"[2507.10672] Vision Language Action Models in Robotic Manipulation: A Systematic Review","url":"https://arxiv.org/abs/2507.10672"},{"title":"Vision Language Action Models in Robotic Manipulation: A Systematic Review","url":"https://arxiv.org/html/2507.10672v1"}]

Based on the search results, here's what I found about VLAC:

## Overview

VLAC is a general-purpose pair-wise critic and manipulation model which designed for real world robot reinforcement learning and data refinement.

## Key Features

VLAC is a generalist Vision Lang
…[truncated 1294 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_corl2026-literature-update_20260515T013205",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-15T01:33:26.493329+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"ReconVLA\" \"conformal prediction\" \"action token\" per-DOF nonconformity 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_corl2026-literature-update_20260515T013205",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"ReconVLA\" \"conformal prediction\" \"action token\" per-DOF nonconformity 2026"
  }
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-15T01:33:26.493556+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "FPC-VLA failure prediction correction VLA supervisor 2025 2026 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_corl2026-literature-update_20260515T013205",
  "tool": "WebSearch",
  "tool_args": {
    "query": "FPC-VLA failure prediction correction VLA supervisor 2025 2026 arXiv"
  }
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-15T01:33:26.493758+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "VLA-OPD on-policy distillation epistemic uncertainty 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_corl2026-literature-update_20260515T013205",
  "tool": "WebSearch",
  "tool_args": {
    "query": "VLA-OPD on-policy distillation epistemic uncertainty 2026"
  }
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-15T01:33:26.493959+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"per-DOF\" OR \"per-dimension\" conformal prediction action robot manipulation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_corl2026-literature-update_20260515T013205",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"per-DOF\" OR \"per-dimension\" conformal prediction action robot manipulation"
  }
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-15T01:33:26.494160+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CoRL 2026 robot learning VLA submission deadline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_corl2026-literature-update_20260515T013205",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CoRL 2026 robot learning VLA submission deadline"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-15T01:33:26.494664+00:00_

Web search results for query: ""ReconVLA" "conformal prediction" "action token" per-DOF nonconformity 2026"

Links: [{"title":"TECP: Token-Entropy Conformal Prediction for LLMs","url":"https://www.mdpi.com/2227-7390/13/20/3351"},{"title":"1 INTRODUCTION","url":"https://arxiv.org/html/2510.04318"},{"title":"Online Conformal Prediction: Enforcing monotonicity via Online Optimization","url":"https://arxiv.org/html/2605.12668"},{"title":"TRACE: Transport Alignment Conformal Prediction via Diffusion and Flow Matching Models","url":"https://arxiv.org/html/2605.07100"},{"title":"GitHub - valeman/awesome-conformal-prediction: A professionally curated list of awesome Conformal Prediction videos, tutorials, books, papers, PhD and MSc theses, articles and open-source libraries. · GitHub","url":"https://github.com/valeman/awesome-conformal-prediction"},{"title":"Task-Driven Uncertainty Quantification in Inverse Problems via Conformal Prediction - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12109201/"},{"title":"Beyond Surface Statistics: Robust Conformal Prediction for LLMs via Internal Representations","url":"https://arxiv.org/html/2604.16217"},{"title":"Conformal prediction - Wikipedia","url":"https://en.wikipedia.org/wiki/Conformal_prediction"},{"title":"A Review of Nonconformity Measures for Conformal ...","url":"https://proceedings.mlr.press/v204/kato23a/kato23a.pdf"},{"title":"Reliable TV Audience Forecasting with Conformal Prediction | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-032-06164-5_6"}]

I searched for "ReconVLA conformal prediction action token per-DOF nonconformity 2026" but the results did not contain any papers or resources specifically about "ReconVLA" combined with conformal prediction and action tokens. 

The search returned several recent papers about conformal prediction in various applications (LLMs, time series, image inverse problems, etc.), but none mentioning "ReconVLA" or the specific combination of concep
…[truncated 575 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_corl2026-literature-update_20260515T013205",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-15T01:33:26.494956+00:00_

Web search results for query: "FPC-VLA failure prediction correction VLA supervisor 2025 2026 arXiv"

Links: [{"title":"FPC-VLA: A Vision-Language-Action Framework with a Supervisor for Failure Prediction and Correction","url":"https://arxiv.org/html/2509.04018"},{"title":"FPC-VLA: A Vision-Language-Action Framework with a Supervisor","url":"https://arxiv.org/pdf/2509.04018"},{"title":"[2509.04018] FPC-VLA: A Vision-Language-Action Framework with a Supervisor for Failure Prediction and Correction","url":"https://arxiv.org/abs/2509.04018"},{"title":"FPC-VLA: A Vision-Language-Action Framework with a Supervisor for Failure Prediction and Correction by Yifan Yang, Zhixiang Duan, Tianshi Xie, Fuyu Cao, Pinxi Shen, Peili Song, Chenyang Zhao, Piaopiao Jin, Guokang Sun, Shaoqing Xu, Yangwei You, Jingtai Liu :: SSRN","url":"https://papers.ssrn.com/sol3/Delivery.cfm/fb935762-45ef-4d2a-9621-dd505dfaf134-MECA.pdf?abstractid=5912300&mirid=1"},{"title":"FPC-VLA: A Vision-Language-Action Framework with a Supervisor for Failure Prediction and Correction | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/fpc-vla-vision-language-action-framework-supervisor"},{"title":"FPC-VLA: A Vision-Language-Action Framework with a Supervisor for Failure Prediction and Correction - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S095741742600655X"},{"title":"[Literature Review] FPC-VLA: A Vision-Language-Action Framework with a Supervisor for Failure Prediction and Correction","url":"https://www.themoonlight.io/en/review/fpc-vla-a-vision-language-action-framework-with-a-supervisor-for-failure-prediction-and-correction"},{"title":"FPC-VLA: A Vision-Language-Action Framework with a Supervisor for Failure Prediction and Correction","url":"https://fpcvla.github.io/"},{"title":"GitHub - jonyzhang2023/awesome-embodied-vla-va-vln: A curated list of state-of-the-art research in embodied AI, focusing on vision-language-action (VLA) models, vision-language
…[truncated 1756 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_corl2026-literature-update_20260515T013205",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-15T01:33:26.495226+00:00_

Web search results for query: "VLA-OPD on-policy distillation epistemic uncertainty 2026"

Links: [{"title":"VLA-OPD: Bridging Offline SFT and Online RL for Vision-Language-Action Models via On-Policy Distillation","url":"https://arxiv.org/html/2603.26666v1"},{"title":"Daily Papers - Hugging Face","url":"https://huggingface.co/papers?q=Hindsight-Guided+On-Policy+Distillation"},{"title":"(PDF) Retrieval-Guided Policy Distillation for Accelerating Vision-Language-Action Specialization Under Demonstration Scarcity","url":"https://www.researchgate.net/publication/401513215_Retrieval-Guided_Policy_Distillation_for_Accelerating_Vision-Language-Action_Specialization_Under_Demonstration_Scarcity"},{"title":"TRACE: Distilling Where It Matters via Token-Routed Self On-Policy Alignment","url":"https://arxiv.org/html/2605.10194v1"},{"title":"Training Driving AI at 50,000× Real Time - IEEE Spectrum","url":"https://spectrum.ieee.org/gm-scalable-driving-ai"},{"title":"GitHub - thinkwee/AwesomeOPD: Awesome List for On-Policy Distillation · GitHub","url":"https://github.com/thinkwee/AwesomeOPD"},{"title":"On-Policy Distillation (OPD) - Research Survey 2026 - Amy's Blog","url":"https://amysheng-ai.github.io/AmyBlog/posts/opd-survey-2026/"},{"title":"[2604.00626] A Survey of On-Policy Distillation for Large Language Models","url":"https://arxiv.org/abs/2604.00626"},{"title":"Paper page - A Survey of On-Policy Distillation for Large Language Models","url":"https://huggingface.co/papers/2604.00626"},{"title":"(PDF) Self-Distilled RLVR","url":"https://www.researchgate.net/publication/403530504_Self-Distilled_RLVR"}]

Based on the search results, here's what I found about VLA-OPD on-policy distillation and epistemic uncertainty:

## VLA-OPD (Vision-Language-Action On-Policy Distillation)

VLA-OPD is a framework that bridges the efficiency of Supervised Fine-Tuning (SFT) with the robustness of Reinforcement Learning (RL). Instead of relying on sparse environmental rewards, VLA-OPD leverage
…[truncated 1178 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_corl2026-literature-update_20260515T013205",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-15T01:33:26.495518+00:00_

Web search results for query: "CoRL 2026 robot learning VLA submission deadline"

Links: [{"title":"CoRL 2026 - Call for Papers","url":"https://www.corl.org/contributions/call-for-papers"},{"title":"CoRL 2026","url":"https://www.corl.org/"},{"title":"Update CoRL 2026 conference details · huggingface/ai-deadlines at 0ba012a","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/0ba012abbc2f4e96e0072f99fd68649bfc69d9cf"},{"title":"CoRL 2026 - Instruction for Authors","url":"https://www.corl.org/contributions/instruction-for-authors"},{"title":"CoRL LaTeX Template | Robot Learning Conference Format | Underleaf","url":"https://www.underleaf.ai/templates/corl"},{"title":"Robot Learning Foundation","url":"https://www.robot-learning.org/"},{"title":"CoRL 2026 Conference | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2026%2FConference"},{"title":"Conference on Robot Learning (@corl_conf) / Posts / X","url":"https://x.com/corl_conf"},{"title":"Conference on Robot Learning (CoRL) 2026: Everything You Need to Know - AI Expert Magazine - premier publication dedicated to AI","url":"https://www.aiexpertmagazine.com/conference-on-robot-learning-corl-2026-everything-you-need-to-know/"},{"title":"CoRL 2026 - Contributions","url":"https://www.corl.org/contributions"}]

Based on the search results, here are the submission deadlines for CoRL 2026:

The abstract submission deadline is May 26, 2026 11:59 UTC, and the paper submission deadline is May 29, 2026 11:59 UTC. However, the paper submission deadline is Thursday (5/28) EOD rather than Friday, which indicates the actual paper deadline may be May 28, 2026.

CoRL 2026 will be held in Austin, Texas, US, and the conference dates are November 9-12, 2026.

The search results focused on general paper submissions to CoRL 2026. While the results mention video models and latent world models as topics of interest, I did not find specific information about a separate "VLA (Vision Language Action
…[truncated 220 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_corl2026-literature-update_20260515T013205",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-15T01:33:26.495794+00:00_

Web search results for query: ""per-DOF" OR "per-dimension" conformal prediction action robot manipulation"

Links: [{"title":"Robotics: Science and Systems 2024 Delft, Netherlands, July 15-July 19, 2024","url":"https://www.roboticsproceedings.org/rss20/p008.pdf"},{"title":"Conformalized Teleoperation: Confidently Mapping Human Inputs to High-Dimensional Robot Actions","url":"https://arxiv.org/html/2406.07767v2"},{"title":"Interaction-aware Conformal Prediction for Crowd Navigation","url":"https://arxiv.org/html/2502.06221"},{"title":"Learning Robot Safety from Sparse Human Feedback using Conformal Prediction","url":"https://arxiv.org/html/2501.04823"},{"title":"Probabilistically Correct Language-based Multi-Robot Planning using Conformal Prediction","url":"https://arxiv.org/html/2402.15368"},{"title":"Safe Task Planning for Language-Instructed Multi-Robot Systems using Conformal Prediction","url":"https://arxiv.org/html/2402.15368v1"},{"title":"Adaptive Conformal Prediction for Motion Planning among ...","url":"https://proceedings.mlr.press/v211/dixit23a/dixit23a.pdf"},{"title":"[2406.07767] Conformalized Teleoperation: Confidently Mapping Human Inputs to High-Dimensional Robot Actions","url":"https://arxiv.org/abs/2406.07767"},{"title":"Preprint WHOLEBODYVLA: TOWARDS UNIFIED LATENT VLA","url":"https://opendrivelab.com/WholeBodyVLA/static/pdf/WholeBodyVLA.pdf"},{"title":"GitHub - Argo-Robot/foundation_models: Overview about state-of-art imitation learning techniques for robotic manipulation, enabling generalization across diverse tasks and environments. · GitHub","url":"https://github.com/Argo-Robot/foundation_models"}]

Based on the search results, I found relevant research on conformal prediction applied to robot manipulation and action prediction. Here are the key findings:

## Conformalized Teleoperation

The most directly relevant work seeks to rigorously quantify if a learned assistive controller can confidently infer a user's intended high-dimensional action
…[truncated 1443 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_corl2026-literature-update_20260515T013205",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---
