# research reconvla citation audit

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 37
- **Recorded user turns:** 0
- **Tool calls:** 18
- **Original source:** `logs/chats/worker_research_reconvla-citation-audit_20260513T220502.jsonl`
- **Structured JSON:** [`1ea2dc62f7aa0a290464.json`](../../sessions/1e/1ea2dc62f7aa0a290464.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

37 recorded events

### Tool call

_source line 1 · 2026-05-13T22:07:29.931726+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,mcp__agent-ml-research__read_project_file",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reconvla-citation-audit_20260513T220502",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,mcp__agent-ml-research__read_project_file",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-13T22:07:29.932123+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reconvla-citation-audit_20260513T220502",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-13T22:07:29.932341+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arXiv 2508.10333"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reconvla-citation-audit_20260513T220502",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arXiv 2508.10333"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-13T22:07:29.932501+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ReconVLA paper arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reconvla-citation-audit_20260513T220502",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ReconVLA paper arXiv"
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-13T22:07:29.932628+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"action sample selection\" \"sample mean\" \"Euclidean distance\" VLA policy inference"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reconvla-citation-audit_20260513T220502",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"action sample selection\" \"sample mean\" \"Euclidean distance\" VLA policy inference"
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-13T22:07:29.932749+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "multiple action samples argmin mean distance generative policy robot"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reconvla-citation-audit_20260513T220502",
  "tool": "WebSearch",
  "tool_args": {
    "query": "multiple action samples argmin mean distance generative policy robot"
  }
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-13T22:07:29.932867+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "file": "references.bib",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reconvla-citation-audit_20260513T220502",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "file": "references.bib",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-13T22:07:29.933021+00:00_

Web search results for query: "arXiv 2508.10333"

Links: [{"title":"[2508.10333] ReconVLA: Reconstructive Vision-Language-Action Model as Effective Robot Perceiver","url":"https://arxiv.org/abs/2508.10333"},{"title":"ReconVLA: Reconstructive Vision-Language-Action Model as Effective Robot Perceiver","url":"https://arxiv.org/html/2508.10333"},{"title":"爆肝解读AAAI 2026最佳论文！华人团队三大突破，大模型+机器人+CLIP技术让小白秒变大神_reconvla: reconstructive vision-language-action mo-CSDN博客","url":"https://blog.csdn.net/m0_59235245/article/details/157297653"},{"title":"图灵奖得主Bengio斩获AAAI 2026大奖！5篇杰出论文，华人占3篇 - 智源社区","url":"https://hub.baai.ac.cn/view/52060"},{"title":"Towards provably efficient quantum algorithms for large-scale machine-learning models - PubMed","url":"https://pubmed.ncbi.nlm.nih.gov/38199993/"},{"title":"Computer Science Aug 2025","url":"https://arxiv.org/list/cs/2025-08?skip=4500&show=2000"},{"title":"AAAI杰出论文来了！港科大、同济、浙师大等国内高校获奖_腾讯新闻","url":"https://news.qq.com/rain/a/20260122A05AJG00"},{"title":"Computer Science Aug 2025","url":"https://www.arxiv.org/list/cs/2025-08?skip=3275&show=250"},{"title":"Computer Science","url":"https://arxiv.org/list/cs/pastweek?skip=389&show=2000"},{"title":"Computer Science","url":"https://www.arxiv.org/list/cs/recent?skip=1928&show=1000"}]

Based on the search results, here's what I found about arXiv 2508.10333:

**ReconVLA** is a reconstructive Vision-Language-Action (VLA) model that uses an implicit grounding paradigm. Conditioned on the model's visual outputs, a diffusion transformer reconstructs the gaze region of the image corresponding to target manipulated objects, prompting the VLA model to learn fine-grained representations and accurately allocate visual attention for precise manipulation.

The research identifies that current VLA models struggle to allocate visual attention to target regions, with visual attention always being dispersed.

The authors curated a large-scale pretraining dataset comprising over 100k trajectories and 2 million dat
…[truncated 275 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reconvla-citation-audit_20260513T220502",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-13T22:07:29.933212+00:00_

Web search results for query: "ReconVLA paper arXiv"

Links: [{"title":"[2508.10333] ReconVLA: Reconstructive Vision-Language-Action Model as Effective Robot Perceiver","url":"https://arxiv.org/abs/2508.10333"},{"title":"ReconVLA: Reconstructive Vision-Language-Action Model as Effective Robot Perceiver","url":"https://arxiv.org/html/2508.10333v1"},{"title":"ReconVLA: An Uncertainty-Guided and Failure-Aware Vision-Language-Action Framework for Robotic Control","url":"https://arxiv.org/html/2604.16677v1"},{"title":"ReconVLA: Reconstructive Vision-Language-Action Model as Effective Robot Perceiver","url":"https://zionchow.github.io/ReconVLA/"},{"title":"GitHub - OpenHelix-Team/ReconVLA: Official implementation of ReconVLA: Reconstructive Vision-Language-Action Model as Effective Robot Perceiver. · GitHub","url":"https://github.com/OpenHelix-Team/ReconVLA"},{"title":"Explore | alphaXiv","url":"https://www.alphaxiv.org/"},{"title":"[2604.01128] Paper Reconstruction Evaluation: Evaluating Presentation and Hallucination in AI-written Papers","url":"https://arxiv.org/abs/2604.01128"},{"title":"[2407.13211] Research on Image Super-Resolution Reconstruction Mechanism based on Convolutional Neural Network","url":"https://arxiv.org/abs/2407.13211"},{"title":"ReconVAT: A Semi-Supervised Automatic Music Transcription Framework for Low-Resource Real-World Data | Proceedings of the 29th ACM International Conference on Multimedia","url":"https://dl.acm.org/doi/10.1145/3474085.3475405"},{"title":"arXiv.org e-Print archive","url":"https://arxiv.org/"}]

I found the ReconVLA paper on arXiv. Here are the key details:

## ReconVLA: Reconstructive Vision-Language-Action Model as Effective Robot Perceiver

**Paper ID:** arXiv:2508.10333

**Overview:**
ReconVLA is a reconstructive VLA model with an implicit grounding paradigm designed to improve robotic control. Recent advances in Vision-Language-Action (VLA) models have enabled robotic agents to integrate multimodal understanding with acti
…[truncated 1028 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reconvla-citation-audit_20260513T220502",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-13T22:07:29.933433+00:00_

Web search results for query: ""action sample selection" "sample mean" "Euclidean distance" VLA policy inference"

Links: [{"title":"VLD: Visual Language Goal Distance for Reinforcement Learning Navigation","url":"https://arxiv.org/html/2512.07976"},{"title":"VQ-VLA: Improving Vision-Language-Action Models via Scaling","url":"https://xiaoxiao0406.github.io/vqvla.github.io/static/pdfs/VQ-VLA.pdf"},{"title":"Measuring Policy Distance for Multi-Agent Reinforcement Learning","url":"https://arxiv.org/html/2401.11257v2"},{"title":"Pure Vision Language Action (VLA) Models: A Comprehensive Survey","url":"https://arxiv.org/html/2509.19012v1"},{"title":"ACG: Action Coherence Guidance for Flow-based VLA models","url":"https://arxiv.org/pdf/2510.22201"},{"title":"DeeR-VLA: Dynamic Inference of Multimodal Large ...","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/67b0e7c7c2a5780aeefe3b79caac106e-Paper-Conference.pdf"},{"title":"VLAPS: Vision-Language-Action Planning","url":"https://www.emergentmind.com/topics/vision-language-action-planning-search-vlaps"},{"title":"Act, Think or Abstain: Complexity-Aware Adaptive Inference for Vision-Language-Action Models | Request PDF","url":"https://www.researchgate.net/publication/401600553_Act_Think_or_Abstain_Complexity-Aware_Adaptive_Inference_for_Vision-Language-Action_Models"},{"title":"EfficientVLA: Training-Free Acceleration and Compression ...","url":"https://openreview.net/pdf?id=SELYlDHZk2"},{"title":"Open-Loop Planning, Closed-Loop Verification: Speculative Verification for VLA","url":"https://arxiv.org/html/2604.02965"}]

The search results contain relevant information about Vision-Language-Action (VLA) models and related topics. Here's what I found:

## Key Findings

The search results cover several VLA-related research areas:

1. **Distance-based approaches in VLA**: VIP reframed representation learning as goal-conditioned value prediction, where Euclidean distance in latent space acts as a reward. Additionall
…[truncated 1268 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reconvla-citation-audit_20260513T220502",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-13T22:07:29.933641+00:00_

Web search results for query: "multiple action samples argmin mean distance generative policy robot"

Links: [{"title":"IMLE Policy: Fast and Sample Efficient Visuomotor Policy Learning via Implicit Maximum Likelihood Estimation","url":"https://arxiv.org/html/2502.12371v2"},{"title":"Discrete Policy: Learning Disentangled Action Space for Multi-Task Robotic Manipulation","url":"https://arxiv.org/html/2409.18707v2"},{"title":"Diffusion Policy:","url":"https://www.roboticsproceedings.org/rss19/p026.pdf"},{"title":"Diffusion Policy: Visuomotor Policy Learning via Action Diffusion .","url":"https://arxiv.org/pdf/2303.04137"},{"title":"MSG: Multi-Stream Generative Policies for Sample-Efficient Robotic Manipulation","url":"https://arxiv.org/html/2509.24956v1"},{"title":"MP1: Mean Flow Tames Policy Learning in 1-step for Robotic Manipulation","url":"https://arxiv.org/html/2507.10543v1"},{"title":"1 Generative Artificial Intelligence in Robotic Manipulation: A Survey","url":"https://arxiv.org/pdf/2503.03464"},{"title":"The duality of generative AI and reinforcement learning in robotics: A review - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S1566253525010656"},{"title":"[2303.04137] Diffusion Policy: Visuomotor Policy Learning via Action Diffusion","url":"https://arxiv.org/abs/2303.04137"},{"title":"RoboBERT: An End-to-end Multimodal Robotic Manipulation Model","url":"https://arxiv.org/html/2502.07837v2"}]

The search results provide relevant information about generative policy approaches for robot learning. Here's what I found:

## Key Findings

The search results reveal several important developments in generative policy learning for robotics:

**Diffusion Policy Approach**: Diffusion Policy represents a robot's visuomotor policy as a conditional denoising diffusion process, and the diffusion formulation yields powerful advantages when used for robot policies, including gracefully handling multimodal action distributions, being suitable for hig
…[truncated 1245 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reconvla-citation-audit_20260513T220502",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-13T22:07:29.933798+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'references.bib'\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reconvla-citation-audit_20260513T220502",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-13T22:07:29.933961+00:00_

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
  "session": "worker_research_reconvla-citation-audit_20260513T220502",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arXiv 2604.16677 ReconVLA uncertainty-guided failure-aware"
  }
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-13T22:07:29.934085+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"sample consensus\" action selection diffusion policy inference time robot manipulation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reconvla-citation-audit_20260513T220502",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"sample consensus\" action selection diffusion policy inference time robot manipulation"
  }
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-13T22:07:29.934209+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "draw K action samples select closest sample mean VLA baseline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reconvla-citation-audit_20260513T220502",
  "tool": "WebSearch",
  "tool_args": {
    "query": "draw K action samples select closest sample mean VLA baseline"
  }
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-13T22:07:29.934372+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reconvla-citation-audit_20260513T220502",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.bib"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-13T22:07:29.934500+00:00_

artifacts/_project/paper/references_e9d4d2.bib
artifacts/_project/paper/references.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reconvla-citation-audit_20260513T220502",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-13T22:07:29.934636+00:00_

Web search results for query: "arXiv 2604.16677 ReconVLA uncertainty-guided failure-aware"

Links: [{"title":"ReconVLA: An Uncertainty-Guided and Failure-Aware Vision-Language-Action Framework for Robotic Control","url":"https://arxiv.org/html/2604.16677v1"},{"title":"Entropy-Guided Loop: Achieving Reasoning through Uncertainty-Aware Generation","url":"https://arxiv.org/html/2509.00079v1"},{"title":"Machine Learning Jul 2025","url":"https://arxiv.org/list/cs.LG/2025-07?skip=25&show=2000"},{"title":"Machine Learning Sep 2025","url":"https://arxiv.org/list/cs.LG/2025-09?skip=550&show=2000"},{"title":"[2604.13352] A Machine Learning Framework for Uncertainty-Calibrated Capability Decision under Finite Samples","url":"https://arxiv.org/abs/2604.13352"},{"title":"Towards Reliable Truth-Aligned Uncertainty Estimation in Large Language Models","url":"https://arxiv.org/html/2604.00445"},{"title":"[2604.11036] Uncertainty-Aware Web-Conditioned Scientific Fact-Checking","url":"https://arxiv.org/abs/2604.11036"},{"title":"Uncertainty-aware Generative Learning Path Recommendation with Cognition-Adaptive Diffusion","url":"https://arxiv.org/html/2604.14613"},{"title":"[2503.15742] Uncertainty-Aware Diffusion Guided Refinement of 3D Scenes","url":"https://arxiv.org/abs/2503.15742"},{"title":"Uncertainty Propagation in LLM-Based Systems","url":"https://arxiv.org/html/2604.23505"}]

Based on the search results, I found the paper you're looking for:

## ReconVLA: An Uncertainty-Guided and Failure-Aware Vision-Language-Action Framework for Robotic Control

ReconVLA is a reliable conformal model that produces uncertainty-guided and failure-aware control signals. Vision-language-action (VLA) models have emerged as generalist robotic controllers capable of mapping visual observations and natural language instructions to continuous action sequences, but VLAs provide no calibrated measure of confidence in their action predictions, thus limiting their reliability in real-world settings wher
…[truncated 801 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reconvla-citation-audit_20260513T220502",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-13T22:07:29.934806+00:00_

Web search results for query: "draw K action samples select closest sample mean VLA baseline"

Links: [{"title":"SimVLA: A Simple VLA Baseline for Robotic Manipulation","url":"https://arxiv.org/html/2602.18224"},{"title":"RoboMonkey","url":"https://robomonkey-vla.github.io/"},{"title":"2.2 Random Sampling and the Distribution of Sample Averages | Introduction to Econometrics with R","url":"https://www.econometrics-with-r.org/2.2-RSATDOSA.html"},{"title":". Drawing a Sample from a Given Distribution Dhiren Ghosh1 and Andrew Vogt2","url":"http://www.asasrms.org/Proceedings/y2008/Files/300875.pdf"},{"title":"10.5 Draw a Random Sample | Analytics Using R","url":"https://pubs.wsb.wisc.edu/academics/analytics-using-r-2019/draw-a-random-sample.html"},{"title":"CoT-VLA","url":"https://cot-vla.github.io/"},{"title":"How can I draw a random sample of my data? | Stata FAQ","url":"https://stats.oarc.ucla.edu/stata/faq/how-can-i-draw-a-random-sample-of-my-data/"},{"title":"Draw samples from a Stan model — sampling • rstan","url":"https://mc-stan.org/rstan/reference/stanmodel-method-sampling.html"},{"title":"Chapter 5 Sampling | Exploring Data Science with R and the Tidyverse: A Concise Introduction","url":"https://ds4world.cs.miami.edu/sampling"},{"title":"Descriptive Drawing Random Samples From Statistical Distributions","url":"https://pj.freefaculty.org/guides/stat/Distributions/DrawingRandomSamples/DrawingSamples.pdf"}]

Based on the search results, I found relevant information about this technique in the context of Vision-Language-Action (VLA) models for robotics.

The technique involves sampling N candidate actions per state from a generalist robot policy, applying clustering to reduce them to K representative actions, and then constructing synthetic action comparisons with preferences assigned based on the RMSE between each sampled action and the ground-truth action.

This approach is part of the RoboMonkey framework, which is a test-time scaling method for VLA models. The
…[truncated 773 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reconvla-citation-audit_20260513T220502",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-13T22:07:29.934979+00:00_

Web search results for query: ""sample consensus" action selection diffusion policy inference time robot manipulation"

Links: [{"title":"Diffusion Policy: Visuomotor Policy Learning via Action Diffusion","url":"https://diffusion-policy.cs.columbia.edu/"},{"title":"[2303.04137] Diffusion Policy: Visuomotor Policy Learning via Action Diffusion","url":"https://arxiv.org/abs/2303.04137"},{"title":"Diffusion Policy:","url":"https://www.roboticsproceedings.org/rss19/p026.pdf"},{"title":"Diffusion policy: : Visuomotor policy learning via action diffusion: International Journal of Robotics Research: Vol 44, No 10-11","url":"https://dl.acm.org/doi/10.1177/02783649241273668"},{"title":"Diffusion Policy: Visuomotor Policy Learning via Action Diffusion .","url":"https://arxiv.org/pdf/2303.04137"},{"title":"Diffusion policy: Visuomotor policy learning via action diffusion - Cheng Chi, Zhenjia Xu, Siyuan Feng, Eric Cousineau, Yilun Du, Benjamin Burchfiel, Russ Tedrake, Shuran Song, 2025","url":"https://journals.sagepub.com/doi/full/10.1177/02783649241273668"},{"title":"Latent Theory of Mind: A Decentralized Diffusion Architecture for Cooperative Manipulation","url":"https://arxiv.org/html/2505.09144v1"},{"title":"Compose Your Policies! Improving Diffusion-based or Flow-based Robot Policies via Test-time Distribution-level Composition","url":"https://arxiv.org/html/2510.01068"},{"title":"Two-Steps Diffusion Policy for Robotic Manipulation via Genetic Denoising","url":"https://arxiv.org/html/2510.21991v1"},{"title":"A Survey on Diffusion Policy for Robotic Manipulation","url":"https://www.techrxiv.org/users/908014/articles/1282755/master/file/data/TPAMI/TPAMI.pdf"}]

I found comprehensive search results related to your query. Here's what the research shows about diffusion policies, action selection, and robot manipulation:

## Diffusion Policy Overview

Diffusion Policy is a new way of generating robot behavior by representing a robot's visuomotor policy as a conditional denoising
…[truncated 1548 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reconvla-citation-audit_20260513T220502",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-13T22:07:29.935143+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reconvla-citation-audit_20260513T220502",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/references.bib"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-13T22:07:29.935371+00:00_

1	@misc{a2c2_2025,
2	    title={Leave No Observation Behind: Real-time Correction for VLA Action Chunks},
3	    author={Kohei Sendai and Maxime Alvarez and Tatsuya Matsushima and Yutaka Matsuo and Yusuke Iwasawa},
4	    year={2025},
5	    eprint={2509.23224},
6	    archivePrefix={arXiv},
7	    primaryClass={cs.RO}
8	}
9	
10	@article{angelopoulos2023gentle,
11	    title={A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification},
12	    author={Anastasios N. Angelopoulos and Stephen Bates},
13	    journal={Foundations and Trends in Machine Learning},
14	    year={2023},
15	    eprint={2107.07511},
16	    archivePrefix={arXiv},
17	    primaryClass={cs.LG}
18	}
19	
20	@article{barber2023conformal,
21	    title={Conformal Prediction Beyond Exchangeability},
22	    author={Rina Foygel Barber and Emmanuel J. Cand{\`e}s and Aaditya Ramdas and Ryan J. Tibshirani},
23	    journal={Annals of Statistics},
24	    volume={51},
25	    number={2},
26	    pages={816--845},
27	    year={2023}
28	}
29	
30	@misc{black2024pi0,
31	    title={$\pi_0$: A Vision-Language-Action Flow Model for General Robot Control},
32	    author={Kevin Black and Noah Brown and Danny Driess and Adnan Esmail and Michael Equi and Chelsea Finn and Niccolo Fusai and Lachy Groom and Karol Hausman and Brian Ichter and Szymon Jakubczak and Tim Jones and Liyiming Ke and Sergey Levine and Adrian Li-Bell and Mohith Mothukuri and Suraj Nair and Karl Pertsch and Lucy Xiaoyang Shi and James Tanner and Quan Vuong and Anna Walling and Haohuan Wang and Ury Zhilinsky},
33	    year={2024},
34	    eprint={2410.24164},
35	    archivePrefix={arXiv},
36	    primaryClass={cs.RO}
37	}
38	
39	@misc{braun2025cgs,
40	    title={Multivariate Standardized Residuals for Conformal Prediction},
41	    author={Sacha Braun and Eug{\`e}ne Berta and Michael I. Jordan and Francis Bach},
42	    year={2025},
43	    eprint={2507.20941},
44	    archivePrefix={arXiv},
45	    primaryClass={stat.ML}
46	}
47	
48	@
…[truncated 10622 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reconvla-citation-audit_20260513T220502",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-13T22:07:29.935547+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "RoboMonkey VLA test-time scaling sampling verification action selection mean"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reconvla-citation-audit_20260513T220502",
  "tool": "WebSearch",
  "tool_args": {
    "query": "RoboMonkey VLA test-time scaling sampling verification action selection mean"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-13T22:07:29.935697+00:00_

Web search results for query: "RoboMonkey VLA test-time scaling sampling verification action selection mean"

Links: [{"title":"RoboMonkey","url":"https://robomonkey-vla.github.io/"},{"title":"[2506.17811] RoboMonkey: Scaling Test-Time Sampling and Verification for Vision-Language-Action Models","url":"https://arxiv.org/abs/2506.17811"},{"title":"RoboMonkey: Scaling Test-Time Sampling and Verification for Vision-Language-Action Models | Scaling Intelligence Lab at Stanford University","url":"https://scalingintelligence.stanford.edu/pubs/robomonkey/"},{"title":"RoboMonkey: Scaling Test-Time Sampling and Verification for Vision-Language-Action Models | OpenReview","url":"https://openreview.net/forum?id=QPTZfaxATs"},{"title":"RoboMonkey: Scaling Test-Time Sampling and Verification for Vision-Language-Action Models | alphaXiv","url":"https://www.alphaxiv.org/overview/2506.17811"},{"title":"RoboMonkey: Scaling Test-Time Sampling and Verification for Vision-Language-Action Models","url":"https://arxiv.org/html/2506.17811"},{"title":"(PDF) RoboMonkey: Scaling Test-Time Sampling and Verification for Vision-Language-Action Models","url":"https://www.researchgate.net/publication/392941464_RoboMonkey_Scaling_Test-Time_Sampling_and_Verification_for_Vision-Language-Action_Models"},{"title":"RoboMonkey: Scaling Test-Time Sampling and Verification for Vision-Language-Action Models","url":"https://proceedings.mlr.press/v305/kwok25a.html"},{"title":"RoboMonkey: Scaling Test-Time Sampling and Verification ...","url":"https://openreview.net/pdf/a720cb48cd7150227b0ee68c7b7a312584efe4aa.pdf"},{"title":"robomonkey-vla/RoboMonkey | DeepWiki","url":"https://deepwiki.com/robomonkey-vla/RoboMonkey"}]

I've found detailed information about RoboMonkey. Here's a summary of the key findings:

## Overview

RoboMonkey is a test-time scaling framework for VLAs (Vision-Language-Action models). It investigates test-time scaling through the lens of sampling and verification as means to enhance the rob
…[truncated 1115 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reconvla-citation-audit_20260513T220502",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-13T22:07:29.935892+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "artifacts/_project/paper/**/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reconvla-citation-audit_20260513T220502",
  "tool": "Glob",
  "tool_args": {
    "pattern": "artifacts/_project/paper/**/*.tex"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-13T22:07:29.936023+00:00_

artifacts/_project/paper/related_work_9c2927.tex
artifacts/_project/paper/related_work.tex
artifacts/_project/paper/introduction_c83872.tex
artifacts/_project/paper/introduction.tex
artifacts/_project/paper/method_section_draft.tex
artifacts/_project/paper/experiments_c64a8c.tex
artifacts/_project/paper/experiments.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reconvla-citation-audit_20260513T220502",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-13T22:07:29.936173+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "reconvla|ReconVLA|chen2026|2508\\.10333|sample mean|closest.*mean|argmin.*mean",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper",
  "output_mode": "content",
  "-i": "True",
  "-n": "True",
  "context": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reconvla-citation-audit_20260513T220502",
  "tool": "Grep",
  "tool_args": {
    "pattern": "reconvla|ReconVLA|chen2026|2508\\.10333|sample mean|closest.*mean|argmin.*mean",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper",
    "output_mode": "content",
    "-i": "True",
    "-n": "True",
    "context": "3"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-13T22:07:29.936456+00:00_

&lt;persisted-output>
Output too large (32.5KB). Full output saved to: /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/40478bb2-6fdd-4066-8024-6be53ea65aa2/tool-results/toolu_01XrTv9nLz4o3noVChw6Na3A.txt

Preview (first 2KB):
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/related_work.tex-36-The most closely related line of work addresses action refinement at inference time without retraining the base policy.
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/related_work.tex-37-A2C2~\cite{a2c2_2025} learns an asynchronous residual correction that runs in parallel with the base policy's action chunk generation, reducing effective latency.
artifacts/_project/paper/related_work.tex-38-However, A2C2 applies a generic residual without uncertainty conditioning: it has no mechanism to modulate correction magnitude based on per-dimension confidence, which can lead to unnecessary perturbation of already-accurate action components.
artifacts/_project/paper/related_work.tex:39:ReconVLA~\cite{chen2026reconvla} draws multiple action samples and selects the one closest to the sample mean based on scalar Euclidean distance, using this distance as a proxy for uncertainty.
artifacts/_project/paper/related_work.tex-40-While effective as a variance-reduction strategy, sample selection is fundamentally limited: it cannot synthesize an action better than any individual sample, and its scalar uncertainty measure does not distinguish which degrees of freedom are unreliable.
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/related_work.tex-41-ACR-VLA addresses both limitations.
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/related_work.tex-42-Compared to A2C2, it condi
…[truncated 213 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reconvla-citation-audit_20260513T220502",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-13T22:07:29.936627+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/40478bb2-6fdd-4066-8024-6be53ea65aa2/tool-results/toolu_01XrTv9nLz4o3noVChw6Na3A.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reconvla-citation-audit_20260513T220502",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/40478bb2-6fdd-4066-8024-6be53ea65aa2/tool-results/toolu_01XrTv9nLz4o3noVChw6Na3A.txt"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-13T22:07:29.936959+00:00_

1	/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/related_work.tex-36-The most closely related line of work addresses action refinement at inference time without retraining the base policy.
2	/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/related_work.tex-37-A2C2~\cite{a2c2_2025} learns an asynchronous residual correction that runs in parallel with the base policy's action chunk generation, reducing effective latency.
3	artifacts/_project/paper/related_work.tex-38-However, A2C2 applies a generic residual without uncertainty conditioning: it has no mechanism to modulate correction magnitude based on per-dimension confidence, which can lead to unnecessary perturbation of already-accurate action components.
4	artifacts/_project/paper/related_work.tex:39:ReconVLA~\cite{chen2026reconvla} draws multiple action samples and selects the one closest to the sample mean based on scalar Euclidean distance, using this distance as a proxy for uncertainty.
5	artifacts/_project/paper/related_work.tex-40-While effective as a variance-reduction strategy, sample selection is fundamentally limited: it cannot synthesize an action better than any individual sample, and its scalar uncertainty measure does not distinguish which degrees of freedom are unreliable.
6	/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/related_work.tex-41-ACR-VLA addresses both limitations.
7	/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/related_work.tex-42-Compared to A2C2, it conditions correction on calibrated per-DOF conformal features, enabling the refinement module to selectively correct high-uncertainty dimensions while preserving accurate predictions on others.
8	artifacts/_project/paper/related_work.tex:43:Compared to ReconVLA, it performs learned synthesi
…[truncated 31883 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reconvla-citation-audit_20260513T220502",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-13T22:07:29.937160+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arXiv 2604.16677 \"ReconVLA\" Chen Lyu Beksi method conformal prediction action sampling"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reconvla-citation-audit_20260513T220502",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arXiv 2604.16677 \"ReconVLA\" Chen Lyu Beksi method conformal prediction action sampling"
  }
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-13T22:07:29.937309+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebFetch",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reconvla-citation-audit_20260513T220502",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebFetch",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-13T22:07:29.937436+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reconvla-citation-audit_20260513T220502",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-13T22:07:29.937576+00:00_

Web search results for query: "arXiv 2604.16677 "ReconVLA" Chen Lyu Beksi method conformal prediction action sampling"

Links: [{"title":"ReconVLA: An Uncertainty-Guided and Failure-Aware Vision-Language-Action Framework for Robotic Control","url":"https://arxiv.org/html/2604.16677v1"},{"title":"COPU: Conformal Prediction for Uncertainty Quantification in Natural Language Generation","url":"https://arxiv.org/html/2502.12601v1"},{"title":"[2107.07511] A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification","url":"https://arxiv.org/abs/2107.07511"},{"title":"[2503.17678] Computationally and Sample Efficient Safe Reinforcement Learning Using Adaptive Conformal Prediction","url":"https://arxiv.org/abs/2503.17678"},{"title":"Another Fit Bites the Dust: Conformal Prediction as a Calibration Standard for Machine Learning in High-Energy Physics","url":"https://arxiv.org/html/2512.17048v1"},{"title":"Conformal Predictions for Human Action Recognition with Vision-Language Models","url":"https://arxiv.org/html/2502.06631"},{"title":"[2410.06494] Conformal Prediction: A Data Perspective","url":"https://arxiv.org/abs/2410.06494"},{"title":"[2306.10193] Conformal Language Modeling","url":"https://arxiv.org/abs/2306.10193"},{"title":"Conformal Prediction & Uncertainty Quantification","url":"https://www.emergentmind.com/papers/2107.07511"},{"title":"Conformal Prediction","url":"https://bactra.org/notebooks/conformal-prediction.html"}]

I found the paper! Here are the search results for arXiv 2604.16677:

**ReconVLA: An Uncertainty-Guided and Failure-Aware Vision-Language-Action Framework for Robotic Control**

The paper is authored by Lingling Chen, Zongyao Lyu, and William J. Beksi from the Department of Computer Science and Engineering at The University of Texas at Arlington.

**Overview:**
ReconVLA is a reliable conformal model that produces uncertainty-guided and failure-aware control signals. Vision-language-action (VLA) models are gener
…[truncated 1093 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reconvla-citation-audit_20260513T220502",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-13T22:07:29.937738+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.16677",
  "prompt": "Extract the full abstract and the method description. Specifically, does this paper describe a method that \"draws multiple action samples and selects the one closest to the sample mean using scalar Euclidean distance\"? What is the actual method proposed in this paper?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_reconvla-citation-audit_20260513T220502",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2604.16677",
    "prompt": "Extract the full abstract and the method description. Specifically, does this paper describe a method that \"draws multiple action samples and selects the one closest to the sample mean using scalar Euclidean distance\"? What is the actual method proposed in this paper?"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-13T22:07:29.937873+00:00_

# ReconVLA Paper Analysis

## Full Abstract

"Vision-language-action (VLA) models have emerged as generalist robotic controllers capable of mapping visual observations and natural language instructions to continuous action sequences. However, VLAs provide no calibrated measure of confidence in their action predictions, thus limiting their reliability in real-world settings where uncertainty and failures must be anticipated. To address this problem we introduce ReconVLA, a reliable conformal model that produces uncertainty-guided and failure-aware control signals. Concretely, our approach applies conformal prediction directly to the action token outputs of pretrained VLA policies, yielding calibrated uncertainty estimates that correlate with execution quality and task success. Furthermore, we extend conformal prediction to the robot state space to detect outliers or unsafe states before failures occur, providing a simple yet effective failure detection mechanism that complements the action-level uncertainty. We evaluate ReconVLA in both simulation and real robot experiments across diverse manipulation tasks. Our results show that conformalized action predictions consistently improve failure anticipation, reduce catastrophic errors, and provide a calibrated measure of confidence without retraining or modifying the underlying VLA."

## Method Description

The paper proposes **ReconVLA**, which applies **conformal prediction** to VLA action outputs. The key components include:

1. Applying conformal prediction to action token outputs from pretrained VLAs
2. Generating calibrated uncertainty estimates correlated with execution quality
3. Extending conformal prediction to robot state space for failure detection

## Does it use the described sampling method?

**No.** The abstract contains no mention of "drawing multiple action samples" or "selecting based on Euclidean distance to sample mean." The method relies on conformal prediction techniques, not ensemble sampling appr
…[truncated 7 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_reconvla-citation-audit_20260513T220502",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 37 · 2026-05-13T22:07:29.938092+00:00_

调查完成。结论明确。

---

## 调查结果

### 1. bib 条目实际指向的论文

`chen2026reconvla` 指向 **arXiv 2604.16677**（非用户提到的 2508.10333）：

| 字段 | 内容 |
|------|------|
| 标题 | ReconVLA: An Uncertainty-Guided and Failure-Aware Vision-Language-Action Framework |
| 作者 | Lingling Chen, Zongyao Lyu, William J. Beksi (UT Arlington) |
| 实际方法 | 对 VLA action token 输出施加 **conformal prediction**，生成校准的不确定性估计，用于 failure detection |
| 提交日期 | 2026-04-17 |

**该论文完全不包含 "draw K samples, select closest to sample mean" 这一方法。**

### 2. arXiv 2508.10333（用户提到的 ID）

这是另一篇同名论文：*"ReconVLA: Reconstructive Vision-Language-Action Model as Effective Robot Perceiver"*，AAAI 2026 杰出论文，关于 **visual attention reconstruction via diffusion transformer**。与 action sampling 也完全无关。

### 3. "draw K samples → select closest to sample mean" 方法是否有出处

搜索了以下关键词组合，**未找到任何已发表论文描述这一具体方法**：
- "action sample selection" + "sample mean" + "Euclidean distance"
- "multiple action samples argmin mean distance"
- "sample consensus action selection"

最接近的已发表工作是 **RoboMonkey**（arXiv 2506.17811），但它使用 sampling + VLM verifier 而非 scalar Euclidean distance to mean。

---

## 结论：**引用造假确认**

我们论文中存在两层问题：

1. **方法归因造假**：我们在 `introduction.tex:14`、`related_work.tex:39`、`experiments.tex:49` 中将一个自造的 baseline 方法（"draw K samples, select closest to sample mean via scalar Euclidean distance"）归因给 Chen et al. 的 ReconVLA，但该论文根本不包含这个方法。

2. **讽刺的是**：真实的 ReconVLA (2604.16677) 实际上也在做 **conformal prediction for VLA**——和我们的 ACR-VLA 高度相关。我们把一个真正的竞品论文错误描述成了一个更弱的 strawman baseline。

涉及的文件位置：
- `introduction.tex` 第 14, 23 行
- `related_work.tex` 第 39, 43 行
- `experiments.tex` 第 49, 73, 80, 83, 84, 157, 195 行
- `references.bib` 第 57-64 行

**建议**：将 "ReconVLA" baseline 改名为描述性名称（如 "Sample-Mean Selection" 或 "Scalar-Distance Selection"），标注为我们自己构建的 baseline，移除对 chen2026reconvla 的虚假归因。同时需要重新审视如何在 related work 中正确讨论真实的 ReconVLA 论文。

Sources:
- [ReconVLA (2508.10333) - Reconstructive VLA](https://arxiv.org/abs/2508.10333)
- [ReconVLA (2604.16677) - Conformal Prediction VLA](https://arxiv.org/html/2604.16677v1)
- [RoboMonkey - Test-Time Scaling](https://arxiv.org/abs/2506.17811)
- [Diffusion Policy](https://arxiv.org/abs/2303.04137)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_reconvla-citation-audit_20260513T220502"
}
```

</details>

---
