# research plan b literature

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 77
- **Recorded user turns:** 0
- **Tool calls:** 38
- **Original source:** `logs/chats/worker_research_plan-b-literature_20260526T095830.jsonl`
- **Structured JSON:** [`c5df6c40b8e375953420.json`](../../sessions/c5/c5df6c40b8e375953420.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

77 recorded events

### Tool call

_source line 1 · 2026-05-26T10:04:17.064757+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__append_idea",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_plan-b-literature_20260526T095830",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__append_idea",
    "max_results": "5"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-26T10:04:17.065085+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan-b-literature_20260526T095830",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-26T10:04:17.065267+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "occsafe_vla",
  "file": "memory.md",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_plan-b-literature_20260526T095830",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "occsafe_vla",
    "file": "memory.md",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-26T10:04:17.065428+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/memory.md\", \"content\": \"# Memory\\n\\n## 2026-05-26 Eval Readiness Pre-check\\n\\n### CRITICAL: westd-10894 Disk Full Crisis (discovered ~04:30 UTC)\\n- 10894 disk 100% full (250G/250G, 824K free). Root cause: 229G in /root/autodl-tmp/checkpoints/ from accumulated old experiments.\\n- 3 resume experiments (mvp_occ_s3, full_occ_ln_s3, ablation_occ_detach_s3) ALL CRASHED at ~04:24 UTC (exit code 1) during 30000_chkpt save.\\n  - ablation_occ_detach_s3: 30000_chkpt COMPLETE (saved first, got lucky)\\n  - full_occ_ln_s3: 30000_chkpt BROKEN (only tokenizer files). 20000_chkpt intact.\\n  - mvp_occ_s3: 30000_chkpt NEVER CREATED. 20000_chkpt intact.\\n- cutoff_45k_s2_v2 still running (step ~10624/50005), will crash at step 20000 (~8h) when next checkpoint save triggers.\\n\\n### Checkpoint Naming: Resume experiments use LOCAL step numbers\\n- Resume experiments (loaded 20K ckpt as vla_path, NOT --resume flag): checkpoints at 10000, 20000, 30000 (local steps)\\n- From-scratch experiments: checkpoints at 10000, 20000, ..., 50000\\n- eval_batch_10894.sh and cka_batch_s3.sh both reference `50000_chkpt` for resume experiments → WRONG, should be `30000_chkpt`\\n\", \"total_chars\": 1111, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan-b-literature_20260526T095830",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-26T10:04:17.065572+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "auxiliary task negative transfer multi-task learning hurts performance robotics VLA"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_plan-b-literature_20260526T095830",
  "tool": "WebSearch",
  "tool_args": {
    "query": "auxiliary task negative transfer multi-task learning hurts performance robotics VLA"
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-26T10:04:17.065755+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "SafeLIBERO safe robot learning VLA collision avoidance occupancy prediction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_plan-b-literature_20260526T095830",
  "tool": "WebSearch",
  "tool_args": {
    "query": "SafeLIBERO safe robot learning VLA collision avoidance occupancy prediction"
  }
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-26T10:04:17.065889+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "gradient conflict multi-task learning negative transfer mechanism task interference auxiliary supervision"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_plan-b-literature_20260526T095830",
  "tool": "WebSearch",
  "tool_args": {
    "query": "gradient conflict multi-task learning negative transfer mechanism task interference auxiliary supervision"
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-26T10:04:17.066008+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "cautionary study negative result paper NeurIPS ICML CoRL robotics machine learning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_plan-b-literature_20260526T095830",
  "tool": "WebSearch",
  "tool_args": {
    "query": "cautionary study negative result paper NeurIPS ICML CoRL robotics machine learning"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-26T10:04:17.066147+00:00_

Web search results for query: "gradient conflict multi-task learning negative transfer mechanism task interference auxiliary supervision"

Links: [{"title":"ForkMerge: Mitigating Negative Transfer in Auxiliary-Task Learning","url":"https://ise.thss.tsinghua.edu.cn/~mlong/doc/ForkMerge-nips23.pdf"},{"title":"Gradient Interference-Aware Graph Coloring for Multitask Learning","url":"https://arxiv.org/html/2509.16959v1"},{"title":"Token Space Manipulation for Transformer-Based Multi-Task ...","url":"https://openaccess.thecvf.com/content/ICCV2025/papers/Jeong_Resolving_Token-Space_Gradient_Conflicts_Token_Space_Manipulation_for_Transformer-Based_Multi-Task_ICCV_2025_paper.pdf"},{"title":"[2301.12618] ForkMerge: Mitigating Negative Transfer in Auxiliary-Task Learning","url":"https://arxiv.org/abs/2301.12618"},{"title":"MetaBalance: Improving Multi-Task Recommendations via Adapting Gradient Magnitudes of Auxiliary Tasks","url":"https://dl.acm.org/doi/fullHtml/10.1145/3485447.3512093"},{"title":"Locating and Mitigating Gradient Conflicts in Point Cloud Domain Adaptation via Saliency Map Skewness","url":"https://arxiv.org/html/2504.15796"},{"title":"Gradient Descent in Multi-Task Learning Stanford CS224N Default Project","url":"https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1244/final-projects/DavidSaykinKfirShmuelDolev.pdf"},{"title":"GDOD: Effective Gradient Descent using Orthogonal ...","url":"https://dl.acm.org/doi/abs/10.1145/3511808.3557333"}]

Here are the search results for your query on gradient conflict, multi-task learning, negative transfer, task interference, and auxiliary supervision:

## Key Findings:

**Negative Transfer and Gradient Conflicts:**
Learning multiple tasks simultaneously can result in lower accuracy than learning only the target task, known as negative transfer, which is often attributed to gradient conflicts among tasks. However, negative transfer and gradient conflicts are not strongly correlated, and negative transfer might be severe
…[truncated 1090 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan-b-literature_20260526T095830",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-26T10:04:17.066333+00:00_

Web search results for query: "SafeLIBERO safe robot learning VLA collision avoidance occupancy prediction"

Links: [{"title":"VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer [Quick Review]","url":"https://liner.com/review/vlsa-visionlanguageaction-models-with-plugandplay-safety-constraint-layer"},{"title":"VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer","url":"https://vlsa-aegis.github.io/"},{"title":"(PDF) VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer","url":"https://www.researchgate.net/publication/398721287_VLSA_Vision-Language-Action_Models_with_Plug-and-Play_Safety_Constraint_Layer"},{"title":"[2311.02817] Safe-VLN: Collision Avoidance for Vision-and-Language Navigation of Autonomous Robots Operating in Continuous Environments","url":"https://arxiv.org/abs/2311.02817"},{"title":"SafeVLA: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning","url":"https://safevla.github.io/"},{"title":"Safe\\text-VLN: Collision Avoidance for Vision-and-Language Navigation of Autonomous Robots Operating in Continuous Environments","url":"https://arxiv.org/html/2311.02817v2"},{"title":"SafeVLA: Towards Safety Alignment of Vision-Language-Action Model via Safe Reinforcement Learning","url":"https://arxiv.org/html/2503.03480v1"}]

Based on the search results, here's what I found about SafeLIBERO and related safe robot learning research:

## SafeLIBERO Benchmark

SafeLIBERO is a comprehensive safety-critical benchmark derived from the LIBERO dataset, designed to evaluate systems across diverse manipulation scenarios with varying spatial complexity. The benchmark covers 32 distinct scenarios with varying spatial complexities.

## VLSA/AEGIS Framework

The search results reveal a related research effort called VLSA (Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer), which includes the AEGIS framework that uses SafeLIBERO for evaluation. 
…[truncated 986 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan-b-literature_20260526T095830",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-26T10:04:17.066520+00:00_

Web search results for query: "auxiliary task negative transfer multi-task learning hurts performance robotics VLA"

Links: [{"title":"ForkMerge: Mitigating Negative Transfer in Auxiliary-Task Learning","url":"https://ise.thss.tsinghua.edu.cn/~mlong/doc/ForkMerge-nips23.pdf"},{"title":"AuxVLA: Auxiliary Task Learning and Multi-Modal Enhancement for Vision-Language-Action Models in Mobile Manipulation | OpenReview","url":"https://openreview.net/forum?id=lcuA4RYit9"},{"title":"[2301.12618] ForkMerge: Mitigating Negative Transfer in Auxiliary-Task Learning","url":"https://arxiv.org/abs/2301.12618"},{"title":"Multi-Task Learning in Natural Language Processing: An Overview","url":"https://arxiv.org/html/2109.09138v2"},{"title":"A Vision-Language-Action-Critic Model for Robotic Real- ...","url":"https://arxiv.org/pdf/2509.15937"},{"title":"Task Uncertainty Loss Reduce Negative Transfer in Asymmetric Multi-task Feature Learning - ADS","url":"https://ui.adsabs.harvard.edu/abs/2020arXiv201209575P/abstract"},{"title":"Embodiment Transfer Learning for Vision-Language-Action Models","url":"https://arxiv.org/pdf/2511.01224"},{"title":"A Guide to Multi-Task Learning in Machine Learning | by Hey Amit | Data Scientist’s Diary | Medium","url":"https://medium.com/data-scientists-diary/a-guide-to-multi-task-learning-in-machine-learning-768d22b88715"},{"title":"Unified Vision-Language-Action Model","url":"https://arxiv.org/html/2506.19850v1"}]

I found several relevant research papers on this topic. Here are the key findings:

## Negative Transfer in Multi-Task Learning

Learning multiple tasks simultaneously can result in lower accuracy than learning only the target task, a phenomenon known as negative transfer. This problem is often attributed to gradient conflicts among tasks.

Negative transfer is more likely to occur when the distribution shift between the multi-task training data and target test data is enlarged.

## Approaches to Mitigate Negative Transfer

**ForkMerge Method**:
…[truncated 1305 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan-b-literature_20260526T095830",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-26T10:04:17.066900+00:00_

Web search results for query: "cautionary study negative result paper NeurIPS ICML CoRL robotics machine learning"

Links: [{"title":"CoRL 2024 - Instruction for Reviews","url":"https://2024.corl.org/contributions/instruction-for-reviews"},{"title":"GPTZero finds 100 new hallucinations in NeurIPS 2025 accepted papers","url":"https://gptzero.me/news/neurips/"},{"title":"CoRL 2026 - Instruction for Authors","url":"https://www.corl.org/contributions/instruction-for-authors"},{"title":"ICML 2024 Paper Guidelines","url":"https://icml.cc/Conferences/2024/PaperGuidelines"},{"title":"Position: Machine Learning Conferences Should Establish a “Refutations and Critiques” Track","url":"https://arxiv.org/html/2506.19882v3"},{"title":"Position: Embracing Negative Results in Machine Learning","url":"https://arxiv.org/pdf/2406.03980"}]

Based on the web search results, I found several relevant items about negative results and cautionary studies in machine learning conferences:

1. **Position on Negative Results**: There is a position paper titled "Embracing Negative Results in Machine Learning" that argues predictive performance alone is not a good indicator for the worth of a publication, and calls for the publication of "negative" results.

2. **Refutations and Critiques Track**: A proposal has been made to establish a dedicated "Refutations and Critiques" (R&C) track within ML conferences such as NeurIPS, ICML, and ICLR to provide a peer-reviewed platform for research that identifies, analyzes, and corrects misleading, incorrect, or potentially fraudulent claims in impactful ML publications.

3. **Machine Learning Retrospectives**: Machine Learning Retrospectives was hosted in 2020 at ICML and NeurIPS, which invited authors to correct mistakes in their previous papers and accepted submissions highlighting poor scientific practice or conflicting claims.

4. **CoRL's Approach**: The search results show that CoRL (Conference on Robot Learning) evaluates submissions based on signifi
…[truncated 528 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan-b-literature_20260526T095830",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-26T10:04:17.067177+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2301.12618",
  "prompt": "Extract the paper title, authors, year, venue, and summarize the key findings about negative transfer in auxiliary-task learning. What mechanisms do they identify for when auxiliary tasks hurt performance?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_plan-b-literature_20260526T095830",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2301.12618",
    "prompt": "Extract the paper title, authors, year, venue, and summarize the key findings about negative transfer in auxiliary-task learning. What mechanisms do they identify for when auxiliary tasks hurt performance?"
  }
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-26T10:04:17.067327+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://openreview.net/forum?id=lcuA4RYit9",
  "prompt": "Extract the paper title, authors, year, venue, and summarize what AuxVLA does - what auxiliary tasks does it add to VLA models, and what are the results? Does it show any negative effects?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_plan-b-literature_20260526T095830",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://openreview.net/forum?id=lcuA4RYit9",
    "prompt": "Extract the paper title, authors, year, venue, and summarize what AuxVLA does - what auxiliary tasks does it add to VLA models, and what are the results? Does it show any negative effects?"
  }
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-26T10:04:17.067453+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/html/2503.03480v1",
  "prompt": "Extract the paper title, authors, year, venue, and summarize SafeVLA's approach to safety alignment of VLA models. What benchmark do they use? What results do they achieve for collision avoidance?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_plan-b-literature_20260526T095830",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/html/2503.03480v1",
    "prompt": "Extract the paper title, authors, year, venue, and summarize SafeVLA's approach to safety alignment of VLA models. What benchmark do they use? What results do they achieve for collision avoidance?"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-26T10:04:17.067592+00:00_

# ForkMerge Paper Summary

**Title:** ForkMerge: Mitigating Negative Transfer in Auxiliary-Task Learning

**Authors:** Junguang Jiang, Baixu Chen, Junwei Pan, Ximei Wang, Liu Dapeng, Jie Jiang, Mingsheng Long

**Year:** 2023

**Venue:** NeurIPS 2023

## Key Findings on Negative Transfer

The researchers identify that negative transfer—when "learning multiple tasks simultaneously results in lower accuracy than learning only the target task"—stems from two distinct sources:

1. **Optimization perspective:** Gradient conflicts between tasks prevent optimal model updates for the primary objective.

2. **Generalization perspective:** Auxiliary task knowledge fails to transfer effectively to the target domain, causing detrimental parameter updates.

## The ForkMerge Solution

Rather than relying solely on gradient coordination methods, the approach periodically branches the model, automatically adjusts task weightings based on target validation performance, and merges branches to eliminate harmful updates. This dual-perspective strategy proved more effective than existing optimization-focused techniques at preventing performance degradation from auxiliary tasks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan-b-literature_20260526T095830",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-26T10:04:17.067769+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://vlsa-aegis.github.io/",
  "prompt": "Extract the paper title, authors, year, venue, key method description, and results. How does VLSA/AEGIS achieve safety in VLA models? What is the SafeLIBERO benchmark? What collision avoidance rate do they achieve?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_plan-b-literature_20260526T095830",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://vlsa-aegis.github.io/",
    "prompt": "Extract the paper title, authors, year, venue, key method description, and results. How does VLSA/AEGIS achieve safety in VLA models? What is the SafeLIBERO benchmark? What collision avoidance rate do they achieve?"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-26T10:04:17.067911+00:00_

# AuxVLA Paper Summary

**Title:** AuxVLA: Auxiliary Task Learning and Multi-Modal Enhancement for Vision-Language-Action Models in Mobile Manipulation

**Authors:** Ruisen Tu, Arth Shukla, Sohyun Yoo, Xuanlin Li, Junxi Li, Jianwen Xie, Hao Su, Zhuowen Tu

**Year:** 2025

**Venue:** ICLR 2026 Conference

## What AuxVLA Does

The approach addresses robotic control in household settings by combining two strategies: enriched sensory inputs (multi-view visuals and depth data) and co-training with auxiliary decoders. The auxiliary tasks predict "interpretable intermediate representations including global robot position, joint configurations, grasp affordances, target object relative positions, and segmentation masks."

## Results

AuxVLA demonstrates "favorable performance across picking, placing, opening and closing tasks." The authors propose that auxiliary supervision enhances spatial understanding and scene reasoning, while enriched sensory inputs provide necessary spatial context for precise manipulation.

## Negative Effects

The document provided contains no discussion of negative effects, failure cases, or limitations of the approach.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan-b-literature_20260526T095830",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-26T10:04:17.068046+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/pdf/2406.03980",
  "prompt": "Extract the paper title, authors, year, venue, and key arguments about why negative results should be published in ML. What writing strategies or frameworks do they recommend for presenting negative results?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_plan-b-literature_20260526T095830",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/pdf/2406.03980",
    "prompt": "Extract the paper title, authors, year, venue, and key arguments about why negative results should be published in ML. What writing strategies or frameworks do they recommend for presenting negative results?"
  }
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-26T10:04:17.068171+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"auxiliary loss\" \"hurts\" OR \"degrades\" OR \"harmful\" robot learning manipulation policy"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_plan-b-literature_20260526T095830",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"auxiliary loss\" \"hurts\" OR \"degrades\" OR \"harmful\" robot learning manipulation policy"
  }
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-26T10:04:17.068287+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "multi-task learning auxiliary head depth prediction occupancy VLA detrimental representation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_plan-b-literature_20260526T095830",
  "tool": "WebSearch",
  "tool_args": {
    "query": "multi-task learning auxiliary head depth prediction occupancy VLA detrimental representation"
  }
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-26T10:04:17.068402+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "GradNorm PCGrad gradient surgery multi-task conflicting gradients shared representation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_plan-b-literature_20260526T095830",
  "tool": "WebSearch",
  "tool_args": {
    "query": "GradNorm PCGrad gradient surgery multi-task conflicting gradients shared representation"
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-26T10:04:17.068532+00:00_

# SafeVLA: Safety Alignment of Vision-Language-Action Models

**Title:** SafeVLA: Towards Safety Alignment of Vision-Language-Action Model via Safe Reinforcement Learning

**Authors:** Borong Zhang, Yuhao Zhang, Jiaming Ji, Yingshan Lei, Josef Dai, Yuanpei Chen, Yaodong Yang

**Year:** 2025

**Venue:** ICML

## Approach

SafeVLA addresses a critical gap in existing VLA models by explicitly incorporating safety constraints during training. The method formulates robotic control as a language-conditioned constrained Markov decision process (CMDP), defining two primary safety constraints:

1. **Object Safety Constraint:** Prevents damage to task-irrelevant objects and unsafe interactions
2. **Robot Safety Constraint:** Protects the robotic hardware from collision damage

The authors employ a Lagrangian dual optimization approach that "alternate[s] between updating the VLA model parameters θ and the Lagrange multipliers λ" to balance safety and task performance simultaneously, rather than treating them as competing objectives.

## Benchmark

The evaluation uses **Safety-CHORES**, a novel benchmark built on AI2THOR with procedurally generated environments featuring millions of unique scenes. The benchmark includes three tasks: Safety-ObjNav (navigation), Safety-PickUp (manipulation), and Safety-Fetch (combined). Testing spans over 500 procedurally generated scenes with out-of-distribution perturbations including lighting, material, and color variations.

## Results

SafeVLA achieves substantial improvements:
- **Safety improvement:** 83.58% reduction in cumulative costs compared to state-of-the-art
- **Task performance:** 3.85% improvement in success rates
- **Safety distribution:** Reduces the upper bound of unsafe behaviors to 1/35th of baseline methods
- **Robustness:** Maintains safety and performance gains across OOD scenarios

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan-b-literature_20260526T095830",
  "tool": "WebFetch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-26T10:04:17.068710+00:00_

# VLSA: Vision-Language-Action Models with Safety Constraints

**Paper Title:** "VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer"

**Authors:** Songqiao Hu, Zeyi Liu, Shuang Liu, Jun Cen, Zihan Meng, Xiao He

**Year:** 2025

**Venue:** arXiv (cs.RO)

## Key Method Description

The researchers developed AEGIS, an architecture that implements safety through a "plug-and-play safety constraint (SC) layer formulated via control barrier functions." This approach integrates with existing VLA models without requiring retraining. The system combines a vision-language safety assessment module with an action-driven control module that uses a control barrier function quadratic programming solver to mathematically guarantee action safety.

## SafeLIBERO Benchmark

The team constructed SafeLIBERO as "a comprehensive safety-critical benchmark derived from the LIBERO dataset, encompassing 32 diverse scenarios and 1600 episodes." The benchmark includes four categories: spatial constraints, goal-based tasks, object-specific picking, and long-horizon manipulation.

## Key Results

**Collision Avoidance Performance:**
- Translational-only actions: 77.9% (versus 18.7% baseline)
- Full action space: 68.9% (versus 18.1% baseline)

**Task Success:** 68.1% and 67.5% respectively across the two action configurations, while maintaining comparable execution efficiency with baseline systems.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan-b-literature_20260526T095830",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-26T10:04:17.068887+00:00_

I appreciate your interest in this document, but I'm unable to extract the requested information. The content provided appears to be a PDF file rendered as raw binary/compressed data, making it unreadable for me to identify:

- The paper title
- Authors
- Publication year
- Venue
- Arguments about negative results publication
- Writing strategies or frameworks

The text shows PDF encoding markers and compressed streams rather than human-readable content. To help you effectively, I would need:

1. The paper in a text-readable format (plain text, Word document, or HTML)
2. A direct link to the paper
3. The paper's DOI or citation information

If you can provide the document in an accessible format or share the bibliographic details, I'd be happy to discuss the paper's arguments about publishing negative results in machine learning and any recommended presentation strategies.

[Binary content (application/pdf, 179.4KB) also saved to /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-projects-occsafe-vla/276303e7-80de-4de8-a10c-32275e9e650a/tool-results/webfetch-1779789564737-h5a214.pdf]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan-b-literature_20260526T095830",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-26T10:04:17.069041+00:00_

Web search results for query: ""auxiliary loss" "hurts" OR "degrades" OR "harmful" robot learning manipulation policy"

Links: [{"title":"Reinforcement Learning Journal 2025 Cover Page","url":"https://rlj.cs.umass.edu/2025/papers/RLJ_RLC_2025_148.pdf"},{"title":"Lowering barriers to human-robot communication","url":"https://www.ri.cmu.edu/app/uploads/2025/08/Jain_Vidhi_PhD_THESIS-3.pdf"},{"title":"Overcoming catastrophic forgetting in robotic manipulation via knowledge-compositional reinforcement learning - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0925231225024725"},{"title":"Conditioning Matters: Training Diffusion Policies is Faster Than You Think","url":"https://arxiv.org/html/2505.11123v1"},{"title":"Hierarchical reinforcement learning with curriculum demonstrations and goal-guided policies for sequential robotic manipulation - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0952197625008668"},{"title":"DiffSkill: Improving Reinforcement Learning through diffusion-based skill denoiser for robotic manipulation - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0950705124008244"},{"title":"Robot policy learning from demonstrations and visual rewards for sequential manipulation tasks - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0921889025004087"},{"title":"Towards cost-effective and safe contact-rich robotic manipulation with reinforcement learning: A review of techniques for future industrial automation - Anselmo Parnada, Mo Qu, Marco Castellani, Hyung Jin Chang, Yongjing Wang, 2026","url":"https://journals.sagepub.com/doi/10.1177/09596518251350353"}]

I found several relevant results about auxiliary losses and robot manipulation policies. Here are the key findings:

## Key Results:

1. **Auxiliary Tasks and Sample Efficiency**: Auxiliary tasks like pixel-reconstruction loss signals can hinder world model performance through visual distrac
…[truncated 1259 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan-b-literature_20260526T095830",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-26T10:04:17.069219+00:00_

Web search results for query: "multi-task learning auxiliary head depth prediction occupancy VLA detrimental representation"

Links: [{"title":"QDepth-VLA: Quantized Depth Prediction as Auxiliary Supervision for Vision–Language–Action Models","url":"https://arxiv.org/html/2510.14836v2"},{"title":"[2510.14836] QDepth-VLA: Quantized Depth Prediction as Auxiliary Supervision for Vision-Language-Action Models","url":"https://arxiv.org/abs/2510.14836"},{"title":"QDepth-VLA: Quantized Depth Prediction as Auxiliary Supervision for Vision-Language-Action Models - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv251014836L/abstract"},{"title":"[PDF] GeoVLA: Empowering 3D Representations in Vision-Language-Action Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/GeoVLA:-Empowering-3D-Representations-in-Models-Sun-Xie/c47f648b3e7ef7c67cca80ff8d6b00da36a84373"},{"title":"GitHub - ucasmichael/QDepth-VLA: QDepth-VLA: Quantized Depth Prediction as Auxiliary Supervision for Vision-Language-Action Models · GitHub","url":"https://github.com/ucasmichael/QDepth-VLA"},{"title":"MT-DEPTH: MULTI-TASK INSTANCE FEATURE ANALYSIS FOR THE DEPTH COMPLETION","url":"https://arxiv.org/pdf/2512.04734"},{"title":"Optimizing Dense Visual Predictions Through Multi-Task Coherence and","url":"https://openaccess.thecvf.com/content/WACV2025/papers/Fontana_Optimizing_Dense_Visual_Predictions_Through_Multi-Task_Coherence_and_Prioritization_WACV_2025_paper.pdf"},{"title":"Complementary Information Guided Occupancy Prediction via Multi-Level Representation Fusion","url":"https://arxiv.org/html/2510.13198"}]

Based on the search results, I found highly relevant information about your query. The key finding relates to **QDepth-VLA**, a recent research paper that directly addresses the issue of auxiliary depth prediction heads in Vision-Language-Action models.

## Key Finding: Depth Prediction Auxiliary Tasks Can Be Detrimental

Existing works that employ depth-map-based visual predic
…[truncated 1465 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan-b-literature_20260526T095830",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-26T10:04:17.069397+00:00_

Web search results for query: "GradNorm PCGrad gradient surgery multi-task conflicting gradients shared representation"

Links: [{"title":"Gradient Descent in Multi-Task Learning Stanford CS224N Default Project","url":"https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1244/final-projects/DavidSaykinKfirShmuelDolev.pdf"},{"title":"Gradient Surgery for Multi-Task Learning","url":"https://proceedings.neurips.cc/paper/2020/file/3fe78a8acf5fda99de95303940a2420c-Paper.pdf"},{"title":"PCGrad: Gradient Surgery for Multi-Task Learning","url":"https://www.emergentmind.com/topics/pcgrad-optimization-technique"},{"title":"Multi-Task Optimization in Neural Networks: Theory and Practice","url":"https://mlfrontiers.substack.com/p/multi-task-optimization-in-neural"},{"title":"GitHub - tianheyu927/PCGrad: Code for \"Gradient Surgery for Multi-Task Learning\" · GitHub","url":"https://github.com/tianheyu927/PCGrad"},{"title":"GCond: Gradient Conflict Resolution via Accumulation-based Stabilization for Large-Scale Multi-Task Learning","url":"https://arxiv.org/html/2509.07252v1"},{"title":"GRADIENT SURGERY FOR MULTI-TASK LEARNING","url":"https://openreview.net/pdf/78aa2ffcfff2647e283ab11388b26ea883f44bd5.pdf"},{"title":"PCGrad: Gradient Surgery for Multi-Task Learning | PDF | Mathematical Optimization | Computer Vision","url":"https://www.scribd.com/document/558287008/Yu-Et-Al-2020-Gradient-Surgery-for-Multi-Task-Learning"},{"title":"Paper10. PCGrad - Cornor’s Blog","url":"https://wjddyd66.github.io/paper/Paper(10)PCGrad/"}]

I've found comprehensive information about GradNorm, PCGrad, and gradient surgery for multi-task learning. Here's what the search reveals:

## PCGrad and Gradient Surgery

PCGrad is a form of gradient surgery that projects a task's gradient onto the normal plane of the gradient of any other task that has a conflicting gradient, achieving substantial gains in efficiency and performance on supervised multi-task learning and multi-task reinforcement learning dom
…[truncated 1220 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan-b-literature_20260526T095830",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-26T10:04:17.069582+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2510.14836",
  "prompt": "Extract the full paper title, all authors, year, venue. Summarize: 1) What specific evidence do they show that depth prediction as auxiliary supervision can be detrimental to VLA? 2) What mechanisms do they identify? 3) What is their proposed solution (QDepth-VLA)?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_plan-b-literature_20260526T095830",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2510.14836",
    "prompt": "Extract the full paper title, all authors, year, venue. Summarize: 1) What specific evidence do they show that depth prediction as auxiliary supervision can be detrimental to VLA? 2) What mechanisms do they identify? 3) What is their proposed solution (QDepth-VLA)?"
  }
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-26T10:04:17.069752+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://www.semanticscholar.org/paper/GeoVLA:-Empowering-3D-Representations-in-Models-Sun-Xie/c47f648b3e7ef7c67cca80ff8d6b00da36a84373",
  "prompt": "Extract the paper title, authors, year, venue, and summarize what GeoVLA does - how does it add 3D spatial representations to VLA models? Does it use occupancy or depth as auxiliary tasks?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_plan-b-literature_20260526T095830",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://www.semanticscholar.org/paper/GeoVLA:-Empowering-3D-Representations-in-Models-Sun-Xie/c47f648b3e7ef7c67cca80ff8d6b00da36a84373",
    "prompt": "Extract the paper title, authors, year, venue, and summarize what GeoVLA does - how does it add 3D spatial representations to VLA models? Does it use occupancy or depth as auxiliary tasks?"
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-26T10:04:17.069899+00:00_

# Paper Summary

**Full Title:** QDepth-VLA: Quantized Depth Prediction as Auxiliary Supervision for Vision-Language-Action Models

**Authors:** Yixuan Li, Yuhui Chen, Mingcai Zhou, Haoran Li, Zhengtao Zhang, Dongbin Zhao

**Year:** 2025 (submitted October 16, 2025; revised December 22, 2025)

**Venue:** arXiv (cs.CV/cs.RO)

---

## Response to Your Questions

Based on the provided abstract and metadata, I cannot answer your specific questions about:

1. **Evidence of depth prediction being detrimental** - The abstract does not discuss negative effects or detriment from depth supervision.

2. **Identified mechanisms of harm** - No such mechanisms are mentioned in the available content.

3. **The QDepth-VLA solution** - The abstract states the framework "augments VLA models with an auxiliary depth prediction task" through "a dedicated depth expert" that "predict[s] quantized latent tokens of depth maps obtained from a VQ-VAE encoder." However, this describes the *positive* approach rather than addressing detriment.

The abstract emphasizes that QDepth-VLA addresses a *limitation* in existing VLA models: their "lack [of] ability to understand and reason over the essential 3D structures necessary for precise control." The proposal appears constructive rather than addressing negative effects of depth supervision itself.

**To fully answer your questions, the complete paper would need to be reviewed.**

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan-b-literature_20260526T095830",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-26T10:04:17.070036+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/html/2506.19882v3",
  "prompt": "Extract the paper title, authors, year, venue. Summarize the key arguments for why ML conferences should have a \"Refutations and Critiques\" track. What examples of successful negative result papers do they cite?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_plan-b-literature_20260526T095830",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/html/2506.19882v3",
    "prompt": "Extract the paper title, authors, year, venue. Summarize the key arguments for why ML conferences should have a \"Refutations and Critiques\" track. What examples of successful negative result papers do they cite?"
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-26T10:04:17.070169+00:00_

I appreciate your request, but I'm unable to provide the information you're looking for because **no web page content was included** in your message. The section marked "Web page content:" appears to be empty.

To help you extract details about GeoVLA (paper title, authors, year, venue, and its approach to 3D spatial representations), please provide:

1. The actual web page content or paper text
2. A link to the paper if available
3. Or the paper's full text

Once you share the content, I'll be happy to summarize GeoVLA's methodology regarding how it integrates 3D spatial information into Vision-Language Action models, and clarify whether it employs occupancy grids, depth estimation, or other auxiliary tasks—all while adhering to your guidelines on quotation limits and paraphrasing requirements.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan-b-literature_20260526T095830",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-26T10:04:17.070298+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arXiv \"negative result\" \"multi-task\" \"auxiliary\" \"does not improve\" OR \"fails to improve\" deep learning 2023 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_plan-b-literature_20260526T095830",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arXiv \"negative result\" \"multi-task\" \"auxiliary\" \"does not improve\" OR \"fails to improve\" deep learning 2023 2024 2025"
  }
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-26T10:04:17.070416+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"when does multi-task learning help\" OR \"when auxiliary tasks hurt\" representation learning survey"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_plan-b-literature_20260526T095830",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"when does multi-task learning help\" OR \"when auxiliary tasks hurt\" representation learning survey"
  }
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-26T10:04:17.070531+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "SafeVLA SafeLIBERO VLSA AEGIS VLA safety benchmark collision avoidance 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_plan-b-literature_20260526T095830",
  "tool": "WebSearch",
  "tool_args": {
    "query": "SafeVLA SafeLIBERO VLSA AEGIS VLA safety benchmark collision avoidance 2025"
  }
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-26T10:04:17.070712+00:00_

# Paper Summary

**Title:** Position: Machine Learning Conferences Should Establish a "Refutations and Critiques" Track

**Authors:** Rylan Schaeffer, Joshua Kazdan, Yegor Denisov-Blanch, Brando Miranda, Matthias Gerstgrasser, Susan Zhang, Andreas Haupt, Isha Gupta, Elyas Obbad, Jesse Dodge, Jessica Zosa Forde, Francesco Orabona, Sanmi Koyejo, David Donoho

**Year:** 2025

**Venue:** arXiv (position paper)

## Key Arguments for an R&C Track

The authors present four main arguments:

1. **Flawed research gets accepted:** ML conferences sometimes publish misleading or incorrect studies due to peer review limitations, which then propagate false information.

2. **No correction mechanisms exist:** Unlike journals, ML conferences lack official processes to address errors post-acceptance through retractions, errata, or editorial oversight.

3. **Peer review reform is impractical:** Reviewers lack incentives, adequate time, and there are insufficient qualified reviewers given the volume explosion (NeurIPS received over 27,000 submissions).

4. **Current alternatives are inadequate:** Critiques dispersed across blogs and social media lack rigor, visibility, and permanence compared to peer-reviewed venues.

## Examples of Successful Critical Papers

The authors cite several instances where critical responses were published:

- **Agarwal et al. (2021)** - demonstrated deep reinforcement learning lacked actual progress by re-evaluating prior work
- **Carlini et al. (2022)** - refuted privacy claims in an ICML Outstanding Paper
- **Schaeffer et al. (2022, 2023)** - revealed how neural representations in neuroscience models were researcher-inserted, not emergent

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan-b-literature_20260526T095830",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-26T10:04:17.070900+00:00_

Web search results for query: ""when does multi-task learning help" OR "when auxiliary tasks hurt" representation learning survey"

Links: [{"title":"Multi-task learning - Wikipedia","url":"https://en.wikipedia.org/wiki/Multi-task_learning"},{"title":"Multi-Task Learning in ML: Optimization & Use Cases [Overview]","url":"https://www.v7labs.com/blog/multi-task-learning-guide"},{"title":"An Overview of Multi-Task Learning in Deep Neural Networks","url":"https://www.ruder.io/multi-task/"},{"title":"How to Do Multi-Task Learning Intelligently","url":"https://thegradient.pub/how-to-do-multi-task-learning-intelligently/"},{"title":"[1805.06334] Auxiliary Tasks in Multi-task Learning","url":"https://arxiv.org/abs/1805.06334"},{"title":"A Guide to Multi-Task Learning in Machine Learning | by Hey Amit | Data Scientist’s Diary | Medium","url":"https://medium.com/data-scientists-diary/a-guide-to-multi-task-learning-in-machine-learning-768d22b88715"},{"title":"Learning through Auxiliary Tasks | Unsupervised Thoughts","url":"https://vivien000.github.io/blog/journal/learning-though-auxiliary_tasks.html"},{"title":"Learning Representation for Multitask Learning through Self-Supervised Auxiliary Learning","url":"https://arxiv.org/html/2409.16651v1"},{"title":"An Overview of Multi-Task Learning in Deep Neural Networks∗ Sebastian Ruder","url":"https://arxiv.org/pdf/1706.05098"}]

I found relevant information about when multi-task learning helps or hurts representation learning. Here are the key findings:

## When Multi-Task Learning Helps

With the right unrelated auxiliary tasks, joint learning has been shown to be beneficial and provide significant improvement over standard MTL, as prior knowledge about task relatedness can lead to sparser and more informative representations.

The goal of an auxiliary task in MTL is to enable the model to learn representations that are shared or helpful for the main task.

## When Multi-Task Learning Hurts (Negative Transfer)

MTL may hinder indiv
…[truncated 1061 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan-b-literature_20260526T095830",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-26T10:04:17.071076+00:00_

Web search results for query: "SafeVLA SafeLIBERO VLSA AEGIS VLA safety benchmark collision avoidance 2025"

Links: [{"title":"[2512.11891] VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer","url":"https://arxiv.org/abs/2512.11891"},{"title":"VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer","url":"https://arxiv.org/html/2512.11891v1"},{"title":"VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer [Quick Review]","url":"https://liner.com/review/vlsa-visionlanguageaction-models-with-plugandplay-safety-constraint-layer"},{"title":"Paper page - VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer","url":"https://huggingface.co/papers/2512.11891"},{"title":"GitHub - THU-RCSCT/vlsa-aegis: VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer","url":"https://github.com/THU-RCSCT/vlsa-aegis"},{"title":"VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer","url":"https://vlsa-aegis.github.io/"},{"title":"(PDF) VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer","url":"https://www.researchgate.net/publication/398721287_VLSA_Vision-Language-Action_Models_with_Plug-and-Play_Safety_Constraint_Layer"},{"title":"VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer - Paper Details","url":"https://www.chatpaper.ai/dashboard/paper/94b34e07-289d-4650-a2e6-14d20295c2de"},{"title":"THURCSCT/SafeLIBERO · Datasets at Hugging Face","url":"https://huggingface.co/datasets/THURCSCT/SafeLIBERO"}]

Based on the search results, here's what I found about these safety-focused robotics research topics:

## VLSA and AEGIS Architecture

VLSA (Vision-Language-Safe Action) is an architecture named AEGIS that contains a plug-and-play safety constraint layer formulated via control barrier functions and integrates directly with existing VLA models to improve safety with theoretical guarantees
…[truncated 1004 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan-b-literature_20260526T095830",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-26T10:04:17.071249+00:00_

Web search results for query: "arXiv "negative result" "multi-task" "auxiliary" "does not improve" OR "fails to improve" deep learning 2023 2024 2025"

Links: [{"title":"[2404.18961] Unleashing the Power of Multi-Task Learning: A Comprehensive Survey Spanning Traditional, Deep, and Pretrained Foundation Model Eras","url":"https://arxiv.org/abs/2404.18961"},{"title":"HM3: Heterogeneous Multi-Class Model Merging","url":"https://arxiv.org/html/2409.19173v1"},{"title":"Unleashing the Power of Multi-Task Learning: A Comprehensive Survey Spanning Traditional, Deep, and Pretrained Foundation Model Eras","url":"https://arxiv.org/html/2404.18961v1"},{"title":"A Unified Multi-Task Learning Framework for Generative Auto-Bidding with Validation-Aligned Optimization","url":"https://arxiv.org/html/2510.07760v1"},{"title":"Computer Science Aug 2024","url":"https://arxiv.org/list/cs/2024-08?skip=375&show=2000"},{"title":"A Comprehensive Survey of Deep Research: Systems, Methodologies, and Applications","url":"https://arxiv.org/html/2506.12594v1"},{"title":"Date of publication October 2024, date of current version October 18, 2024.","url":"https://arxiv.org/pdf/2103.01566v3"},{"title":"Stealthy Multi-Task Adversarial Attacks","url":"https://arxiv.org/html/2411.17936"},{"title":"[2505.24281] Multi-task Learning for Heterogeneous Data via Integrating Shared and Task-Specific Encodings","url":"https://arxiv.org/abs/2505.24281"},{"title":"Machine Learning May 2025","url":"https://arxiv.org/list/cs.LG/2025-05?skip=600&show=2000"}]

I've performed a web search based on your query. The search results return papers related to multi-task learning and auxiliary tasks in deep learning from 2023-2025, but the results appear to be primarily positive findings about multi-task learning rather than negative results papers.

The search found:

1. A comprehensive survey on multi-task learning spanning traditional, deep, and pretrained foundation model eras from 2023

2. Papers on multi-task learning 
…[truncated 1178 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan-b-literature_20260526T095830",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-26T10:04:17.071429+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Embracing Negative Results in Machine Learning\" position paper 2024 arxiv publication bias"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_plan-b-literature_20260526T095830",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Embracing Negative Results in Machine Learning\" position paper 2024 arxiv publication bias"
  }
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-26T10:04:17.071557+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Standley \"which tasks should be learned together\" multi-task learning task grouping negative transfer CVPR"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_plan-b-literature_20260526T095830",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Standley \"which tasks should be learned together\" multi-task learning task grouping negative transfer CVPR"
  }
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-26T10:04:17.071692+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "GeoVLA 3D representation VLA auxiliary occupancy depth spatial prediction robotic manipulation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_plan-b-literature_20260526T095830",
  "tool": "WebSearch",
  "tool_args": {
    "query": "GeoVLA 3D representation VLA auxiliary occupancy depth spatial prediction robotic manipulation"
  }
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-26T10:04:17.071824+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"does X improve\" cautionary tale empirical study negative finding robot learning 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_plan-b-literature_20260526T095830",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"does X improve\" cautionary tale empirical study negative finding robot learning 2024 2025"
  }
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-26T10:04:17.071963+00:00_

Web search results for query: ""Embracing Negative Results in Machine Learning" position paper 2024 arxiv publication bias"

Links: [{"title":"Position: Embracing Negative Results in Machine Learning","url":"https://arxiv.org/pdf/2406.03980"},{"title":"[2406.03980] Position: Embracing Negative Results in Machine Learning","url":"https://arxiv.org/abs/2406.03980"},{"title":"Position: Embracing Negative Results in Machine Learning | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/position-embracing-negative-results-machine-learning"},{"title":"Machine Learning Jun 2024","url":"https://web3.arxiv.org/list/cs.LG/2024-06?skip=475&show=25"},{"title":"(PDF) Position: Embracing Negative Results in Machine Learning","url":"https://www.researchgate.net/publication/381226301_Position_Embracing_Negative_Results_in_Machine_Learning"},{"title":"Position: Causal Machine Learning Requires Rigorous Synthetic Experiments for Broader Adoption","url":"https://arxiv.org/html/2508.08883"},{"title":"dblp: Position: Embracing Negative Results in Machine Learning.","url":"https://dblp.org/rec/journals/corr/abs-2406-03980.html"},{"title":"Position: Embracing Negative Results in Machine Learning | OpenReview","url":"https://openreview.net/forum?id=3RXAiU7sss"},{"title":"Position: Embracing Negative Results in Machine Learning","url":"https://proceedings.mlr.press/v235/karl24a.html"}]

I found the paper you're looking for. Here are the key details:

**Paper Title:** Position: Embracing Negative Results in Machine Learning

**Authors:** Florian Karl, Lukas Malte Kemeter, Gabriel Dax, and Paulina Sierak

**Publication:** Proceedings of the 41st International Conference on Machine Learning, PMLR 235:23256-23265, 2024

**arXiv Identifier:** 2406.03980 (published June 6, 2024)

**Main Argument:** The paper argues that predictive performance alone is not a good indicator for the worth of a publication, and that using it as such fosters problems like inefficiencies of the mach
…[truncated 687 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan-b-literature_20260526T095830",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-26T10:04:17.072131+00:00_

Web search results for query: "Standley "which tasks should be learned together" multi-task learning task grouping negative transfer CVPR"

Links: [{"title":"[1905.07553] Which Tasks Should Be Learned Together in Multi-task Learning?","url":"https://arxiv.org/abs/1905.07553"},{"title":"Which Tasks Should Be Learned Together in Multi-task Learning?","url":"https://arxiv.org/pdf/1905.07553"},{"title":"[PDF] Which Tasks Should Be Learned Together in Multi-task Learning? | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Which-Tasks-Should-Be-Learned-Together-in-Learning-Standley-Zamir/356941da708c6d5b06bce17463aca309fd33151a"},{"title":"Which Tasks Should Be Learned Together in Multi-task Learning?","url":"https://proceedings.mlr.press/v119/standley20a.html"},{"title":"GitHub - tstandley/taskgrouping: Code for Which Tasks Should Be Learned Together in Multi-task Learning? · GitHub","url":"https://github.com/tstandley/taskgrouping"},{"title":"2020 - Which Tasks Should Be Learned Together in Multi-Task Learning - Standley Et Al - PMLR | PDF | Applied Mathematics | Cognitive Science","url":"https://www.scribd.com/document/838744932/2020-Which-Tasks-Should-Be-Learned-Together-in-Multi-task-Learning-Standley-et-al-PMLR"},{"title":"taskgrouping","url":"http://taskgrouping.stanford.edu/"},{"title":"Which Tasks Should Be Learned Together in Multi-task Learning? | Request PDF","url":"https://www.researchgate.net/publication/333233738_Which_Tasks_Should_Be_Learned_Together_in_Multi-task_Learning"},{"title":"How to Do Multi-Task Learning Intelligently","url":"https://thegradient.pub/how-to-do-multi-task-learning-intelligently/"}]

Based on the search results, I found the paper you're looking for:

"Which Tasks Should Be Learned Together in Multi-task Learning?" is authored by Trevor Standley, Amir R. Zamir, Dawn Chen, Leonidas Guibas, Jitendra Malik, and Silvio Savarese.

**Paper Overview:**

The paper addresses how task objectives can compete in multi-task learning
…[truncated 1142 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan-b-literature_20260526T095830",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-26T10:04:17.072304+00:00_

Web search results for query: ""does X improve" cautionary tale empirical study negative finding robot learning 2024 2025"

Links: [{"title":"Machine Learning May 2025","url":"https://arxiv.org/list/cs.LG/2025-05?skip=3050&show=2000"},{"title":"World Model for Robot Learning: A Comprehensive Survey","url":"https://arxiv.org/html/2605.00080v1"},{"title":"Machine Learning Dec 2024","url":"https://www.arxiv.org/list/cs.LG/2024-12?skip=1100&show=1000"},{"title":"Psychological impacts of AI use on school students","url":"https://rptel.apsce.net/index.php/RPTEL/article/download/2025-20030/2025-20030/4456"},{"title":"Frontiers | Interactive imitation learning for dexterous robotic manipulation: challenges and perspectives—a survey","url":"https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2025.1682437/full"},{"title":"Deep Reinforcement Learning for Robotics: A Survey of Real-World Successes | Annual Reviews","url":"https://www.annualreviews.org/content/journals/10.1146/annurev-control-030323-022510"},{"title":"Artificial Intelligence Nov 2024","url":"https://www.arxiv.org/list/cs.AI/2024-11?skip=300&show=1000"},{"title":"Robot learning in the era of foundation models: : a survey: Neurocomputing: Vol 638, No C","url":"https://dl.acm.org/doi/10.1016/j.neucom.2025.129963"}]

Based on the search results, I found some relevant information about empirical questions in robot learning from 2024-2025:

Whether video-pretrained backbones are consistently superior to matched-scale vision-language model backbones for robotic control remains an open empirical question, with current results viewed as suggestive evidence for a promising inductive bias rather than a definitive architectural conclusion.

This appears to be an example of a cautionary finding in robot learning research, where a potentially beneficial technique (video-pretraining) has not yet shown conclusive advantages compared to alternatives, highlighting the importance of rigorous empirical valid
…[truncated 616 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan-b-literature_20260526T095830",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-26T10:04:17.072472+00:00_

Web search results for query: "GeoVLA 3D representation VLA auxiliary occupancy depth spatial prediction robotic manipulation"

Links: [{"title":"GeoVLA: Empowering 3D Representations in Vision-Language-Action Models","url":"https://arxiv.org/html/2508.09071v2"},{"title":"[PDF] GeoVLA: Empowering 3D Representations in Vision-Language-Action Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/GeoVLA:-Empowering-3D-Representations-in-Models-Sun-Xie/c47f648b3e7ef7c67cca80ff8d6b00da36a84373"},{"title":"GeoPredict: Leveraging Predictive Kinematics and 3D Gaussian Geometry for Precise VLA Manipulation","url":"https://arxiv.org/html/2512.16811v1"},{"title":"[2508.09071] GeoVLA: Empowering 3D Representations in Vision-Language-Action Models","url":"https://arxiv.org/abs/2508.09071"},{"title":"GeoVLA","url":"https://linsun449.github.io/GeoVLA/"},{"title":"GeoVLA: Empowering 3D Representations in Vision-Language-Action Models - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250809071S/abstract"},{"title":"[2512.16811] GeoPredict: Leveraging Predictive Kinematics and 3D Gaussian Geometry for Precise VLA Manipulation","url":"https://arxiv.org/abs/2512.16811"},{"title":"Spatial Forcing: Implicit Spatial Representation Alignment for Vision-language-action Model","url":"https://arxiv.org/html/2510.12276v1"},{"title":"GeoPredict: Leveraging Predictive Kinematics and 3D Gaussian Geometry for Precise VLA Manipulation","url":"https://www.researchgate.net/publication/398850804_GeoPredict_Leveraging_Predictive_Kinematics_and_3D_Gaussian_Geometry_for_Precise_VLA_Manipulation"},{"title":"(PDF) GeoVLA: Empowering 3D Representations in Vision-Language-Action Models","url":"https://www.researchgate.net/publication/394458041_GeoVLA_Empowering_3D_Representations_in_Vision-Language-Action_Models"}]

Based on the search results, here's what I found about GeoVLA and related work:

## GeoVLA Overview

GeoVLA is a novel VLA framework that effectively integrates 3D inform
…[truncated 1355 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan-b-literature_20260526T095830",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-26T10:04:17.072648+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2406.03980",
  "prompt": "Extract full title, authors, year, venue. What specific measures do they recommend for publishing negative results? What writing strategies for framing negative findings?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_plan-b-literature_20260526T095830",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2406.03980",
    "prompt": "Extract full title, authors, year, venue. What specific measures do they recommend for publishing negative results? What writing strategies for framing negative findings?"
  }
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-26T10:04:17.072804+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/1905.07553",
  "prompt": "Extract title, authors, year, venue. Summarize: 1) Key finding about task competition in multi-task learning 2) When do tasks hurt each other? 3) What role does network capacity play?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_plan-b-literature_20260526T095830",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/1905.07553",
    "prompt": "Extract title, authors, year, venue. Summarize: 1) Key finding about task competition in multi-task learning 2) When do tasks hurt each other? 3) What role does network capacity play?"
  }
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-26T10:04:17.072926+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2508.09071",
  "prompt": "Extract full title, authors, year, venue. Does GeoVLA use depth/occupancy as auxiliary supervision? How does it integrate 3D information? Results on LIBERO?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_plan-b-literature_20260526T095830",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2508.09071",
    "prompt": "Extract full title, authors, year, venue. Does GeoVLA use depth/occupancy as auxiliary supervision? How does it integrate 3D information? Results on LIBERO?"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-26T10:04:17.073051+00:00_

# Paper Analysis

**Full Title:** Position: Embracing Negative Results in Machine Learning

**Authors:** Florian Karl, Lukas Malte Kemeter, Gabriel Dax, Paulina Sierak

**Year:** 2024

**Venue:** arXiv (cs.LG - Computer Science, Machine Learning)

---

## Specific Measures and Writing Strategies

Based on the provided webpage content, the abstract indicates the authors advocate for normalizing negative result publications and present "concrete measures for the community to move towards a paradigm where their publication is normalized."

However, **the specific measures and writing strategies are not detailed in the available excerpt.** The abstract only states their position that "predictive performance alone is not a good indicator for the worth of a publication" and that publishing negative results could "alleviate some of these problems and improve the scientific output of the machine learning research community."

To access the detailed recommendations for framing negative findings and concrete implementation measures, you would need to read the full paper via the PDF or HTML links provided on the arXiv page.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan-b-literature_20260526T095830",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-26T10:04:17.073177+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "SpatialVLA Qu \"spatial understanding\" VLA auxiliary 3D prediction action learning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_plan-b-literature_20260526T095830",
  "tool": "WebSearch",
  "tool_args": {
    "query": "SpatialVLA Qu \"spatial understanding\" VLA auxiliary 3D prediction action learning"
  }
}
```

</details>

---

### Tool call

_source line 54 · 2026-05-26T10:04:17.073299+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"representation interference\" \"feature competition\" auxiliary task shared backbone transformer multi-task"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_plan-b-literature_20260526T095830",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"representation interference\" \"feature competition\" auxiliary task shared backbone transformer multi-task"
  }
}
```

</details>

---

### Tool result

_source line 55 · 2026-05-26T10:04:17.073421+00:00_

# Paper Extract

**Title:** Which Tasks Should Be Learned Together in Multi-task Learning?

**Authors:** Trevor Standley, Amir R. Zamir, Dawn Chen, Leonidas Guibas, Jitendra Malik, Silvio Savarese

**Year:** 2019 (submitted); presented to ICML 2020

**Venue:** ICML 2020

---

## Summary

**1) Key Finding on Task Competition:**
The paper identifies that "task objectives can compete," causing inferior performance when multiple tasks share a single network. The researchers propose grouping cooperating tasks together while separating competing ones across different networks to optimize the accuracy-efficiency trade-off.

**2) When Tasks Hurt Each Other:**
The abstract does not provide specific conditions explaining when tasks compete versus cooperate. The framework focuses on empirically studying these dynamics "in several different learning settings" but the webpage excerpt doesn't detail the underlying mechanisms triggering task interference.

**3) Network Capacity's Role:**
The content provided does not explicitly discuss how network capacity influences task competition or cooperation. While the framework aims to produce better accuracy with less inference time, specific analysis of capacity constraints is absent from this excerpt.

**Note:** Full details on these three points likely appear in the complete paper, available via the PDF link.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan-b-literature_20260526T095830",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-26T10:04:17.073549+00:00_

# GeoVLA Paper Summary

**Full Title:** GeoVLA: Empowering 3D Representations in Vision-Language-Action Models

**Authors:** Lin Sun, Bin Xie, Yingfei Liu, Hao Shi, Tiancai Wang, Jale Cao

**Year:** 2025 (submitted August 12, 2025)

**Venue:** arXiv (Computer Science > Robotics)

## 3D Integration Method

GeoVLA incorporates 3D information through a dual-pathway approach: "it converts depth maps into point clouds and employs a customized point encoder, called Point Embedding Network, to generate 3D geometric embeddings independently." These embeddings are then merged with vision-language features and processed by a "spatial-aware action expert, called 3D-enhanced Action Expert."

## Auxiliary Supervision

The provided abstract does not indicate whether depth or occupancy serve as auxiliary supervision signals during training.

## LIBERO Results

The paper demonstrates strong performance, achieving "state-of-the-art results in the LIBERO and ManiSkill2 simulation benchmarks." However, specific quantitative results on LIBERO are not detailed in the abstract.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan-b-literature_20260526T095830",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 57 · 2026-05-26T10:04:17.073751+00:00_

Web search results for query: ""representation interference" "feature competition" auxiliary task shared backbone transformer multi-task"

Links: [{"title":"AdaLTM: Adaptive Layer-wise Task Vector Merging for Categorical Speech Emotion Recognition with ASR Knowledge Integration","url":"https://arxiv.org/html/2603.25041"},{"title":"Optimizing Dense Visual Predictions Through Multi-Task Coherence and Prioritization","url":"https://arxiv.org/html/2412.03179v1"},{"title":"Multi-Task Pre-Finetuning of Lightweight Transformer Encoders for Text Classification and NER","url":"https://arxiv.org/html/2510.07566"},{"title":"Multi-task learning with multi-gate mixture of transformer-based experts for predictive process monitoring in manufacturing - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC11788810/"},{"title":"All-in-One Transferring Image Compression from Human Perception to Multi-Machine Perception","url":"https://arxiv.org/html/2504.12997v1"},{"title":"MTFormer: Multi-Task Learning via Transformer and Cross-Task Reasoning","url":"https://www.ecva.net/papers/eccv_2022/papers_ECCV/papers/136870299.pdf"},{"title":"[2208.09427] Curbing Task Interference using Representation Similarity-Guided Multi-Task Feature Sharing","url":"https://arxiv.org/abs/2208.09427"},{"title":"Balancing Shared and Task-Specific Representations: A Hybrid Approach to Depth-Aware Video Panoptic Segmentation","url":"https://arxiv.org/html/2412.07966"},{"title":"Curbing Task Interference using Representation Similarity-Guided Multi-Task Feature Sharing","url":"https://proceedings.mlr.press/v199/gurulingan22a.html"}]

I've found several relevant research papers on multi-task learning with shared backbones and transformers that address representation interference and feature competition issues. Here are the key findings:

## Task Interference and Representation Degradation

Jointly optimizing a single backbone for diametrically opposed tasks can degrade acoustic representations. Conventional MTL a
…[truncated 1295 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan-b-literature_20260526T095830",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-26T10:04:17.073952+00:00_

Web search results for query: "SpatialVLA Qu "spatial understanding" VLA auxiliary 3D prediction action learning"

Links: [{"title":"SpatialVLA: Exploring Spatial Representations for Visual-Language-Action Models","url":"https://spatialvla.github.io/"},{"title":"SpatialVLA: Exploring Spatial Representations for Visual-Language-Action Models | Request PDF","url":"https://www.researchgate.net/publication/395370588_SpatialVLA_Exploring_Spatial_Representations_for_Visual-Language-Action_Models"},{"title":"[2501.15830] SpatialVLA: Exploring Spatial Representations for Visual-Language-Action Model","url":"https://arxiv.org/abs/2501.15830"},{"title":"QDepth-VLA: Quantized Depth Prediction as Auxiliary Supervision for Vision–Language–Action Models","url":"https://arxiv.org/html/2510.14836"},{"title":"SpatialVLA: Exploring Spatial Representations for Visual-Language-Action Models","url":"https://arxiv.org/html/2501.15830v1"},{"title":"SpatialVLA: Exploring Spatial Representations for Visual-Language-Action Model","url":"https://arxiv.org/html/2501.15830v5"},{"title":"Spatial-Aware VLA Pretraining through Visual-Physical Alignment from Human Videos","url":"https://arxiv.org/html/2512.13080v1"},{"title":"[Literature Review] SpatialVLA: Exploring Spatial Representations for Visual-Language-Action Model","url":"https://www.themoonlight.io/en/review/spatialvla-exploring-spatial-representations-for-visual-language-action-model"}]

Based on the search results, I've found relevant information about SpatialVLA and related approaches focusing on spatial understanding and 3D prediction for VLA models:

## SpatialVLA Overview

SpatialVLA proposes that spatial understanding is key in robot manipulation, introducing Ego3D Position Encoding to inject 3D information into visual-language-action models, along with Adaptive Action Grids to represent spatial robot movement actions with adaptive discretized action grids.

## Key Components

The model extracts 2D semantic features with SigLIP vis
…[truncated 1168 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan-b-literature_20260526T095830",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-26T10:04:17.074135+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2501.15830",
  "prompt": "Extract full title, authors, year, venue. How does SpatialVLA inject 3D spatial information into VLA? Does it use auxiliary prediction tasks? What are the key results? Any discussion of when spatial auxiliary tasks fail or hurt?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_plan-b-literature_20260526T095830",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2501.15830",
    "prompt": "Extract full title, authors, year, venue. How does SpatialVLA inject 3D spatial information into VLA? Does it use auxiliary prediction tasks? What are the key results? Any discussion of when spatial auxiliary tasks fail or hurt?"
  }
}
```

</details>

---

### Tool call

_source line 60 · 2026-05-26T10:04:17.074270+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Spatial Forcing\" implicit spatial representation VLA auxiliary loss action prediction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_plan-b-literature_20260526T095830",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Spatial Forcing\" implicit spatial representation VLA auxiliary loss action prediction"
  }
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-26T10:04:17.074391+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "GradNorm \"gradient normalization\" multi-task learning task weighting Chen ICML 2018"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_plan-b-literature_20260526T095830",
  "tool": "WebSearch",
  "tool_args": {
    "query": "GradNorm \"gradient normalization\" multi-task learning task weighting Chen ICML 2018"
  }
}
```

</details>

---

### Tool call

_source line 62 · 2026-05-26T10:04:17.074510+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"auxiliary depth\" OR \"auxiliary occupancy\" \"does not help\" OR \"harmful\" OR \"detrimental\" robot policy learning VLA 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_plan-b-literature_20260526T095830",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"auxiliary depth\" OR \"auxiliary occupancy\" \"does not help\" OR \"harmful\" OR \"detrimental\" robot policy learning VLA 2024 2025"
  }
}
```

</details>

---

### Tool result

_source line 63 · 2026-05-26T10:04:17.074682+00:00_

# SpatialVLA Paper Summary

**Title:** "SpatialVLA: Exploring Spatial Representations for Visual-Language-Action Model"

**Authors:** Delin Qu, Haoming Song, Qizhi Chen, Yuanqi Yao, Xinyi Ye, Yan Ding, Zhigang Wang, JiaYuan Gu, Bin Zhao, Dong Wang, Xuelong Li

**Year:** 2025

**Venue:** Robotics: Science and Systems, 2025

## 3D Spatial Information Injection

SpatialVLA incorporates spatial understanding through "Ego3D Position Encoding to inject 3D information into the input observations" of the model. The paper emphasizes that "spatial understanding is the keypoint in robot manipulation."

## Action Representation

Rather than auxiliary prediction tasks, the model uses "Adaptive Action Grids to represent spatial robot movement actions with adaptive discretized action grids." This enables learning of "generalizable and transferrable spatial action knowledge for cross-robot control."

## Key Results

The model demonstrates strong performance after pre-training on 1.1 million robot episodes, showing "in-domain multi-task generalization ability" and performing "numerous tasks in a zero-shot manner." Results also highlight "in-distribution generalization and out-of-distribution adaptation capability."

## Limitations Discussion

The provided abstract does not discuss scenarios where spatial auxiliary tasks fail or when they negatively impact performance.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan-b-literature_20260526T095830",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-26T10:04:17.074882+00:00_

Web search results for query: "GradNorm "gradient normalization" multi-task learning task weighting Chen ICML 2018"

Links: [{"title":"[1711.02257] GradNorm: Gradient Normalization for Adaptive Loss Balancing in Deep Multitask Networks","url":"https://arxiv.org/abs/1711.02257"},{"title":"models/grad-norm/README.md at master · chainer/models","url":"https://github.com/chainer/models/blob/master/grad-norm/README.md"},{"title":"GradNorm: Gradient Normalization for Adaptive Loss Balancing in Deep Multitask Networks","url":"https://proceedings.mlr.press/v80/chen18a.html"},{"title":"Under review as a conference paper at ICLR 2018 GRADNORM: GRADIENT","url":"https://openreview.net/pdf?id=H1bM1fZCW"},{"title":"GitHub - hosseinshn/GradNorm: This in my Demo of Chen et al. \"GradNorm: Gradient Normalization for Adaptive Loss Balancing in Deep Multitask Networks\" ICML 2018 · GitHub","url":"https://github.com/hosseinshn/GradNorm"},{"title":"GradNorm: Gradient Normalization for Adaptive Loss ...","url":"https://arxiv.org/pdf/1711.02257"},{"title":"GradNorm: Adaptive Loss Balancing for Multitask Networks","url":"https://www.emergentmind.com/papers/1711.02257"},{"title":"(PDF) GradNorm: Gradient Normalization for Adaptive Loss Balancing in Deep Multitask Networks","url":"https://www.researchgate.net/publication/320920333_GradNorm_Gradient_Normalization_for_Adaptive_Loss_Balancing_in_Deep_Multitask_Networks"},{"title":"Gradnorm: Gradient Normalization For Adaptive Loss Balancing in Deep Multitask Networks | PDF | Image Segmentation | Computer Science","url":"https://www.scribd.com/document/615850392/1711-02257"}]

Based on the search results, here's information about GradNorm:

## Overview

GradNorm is a gradient normalization algorithm that automatically balances training in deep multitask models by dynamically tuning gradient magnitudes. The paper was authored by Zhao Chen, Vijay Badrinarayanan, Chen-Yu Lee and Andrew Rabinovich and published at ICML in 2018.

## Key Contributions
…[truncated 985 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan-b-literature_20260526T095830",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 65 · 2026-05-26T10:04:17.075062+00:00_

Web search results for query: ""Spatial Forcing" implicit spatial representation VLA auxiliary loss action prediction"

Links: [{"title":"Spatial Forcing: Implicit Spatial Representation Alignment for Vision-language-action Model","url":"https://arxiv.org/html/2510.12276v1"},{"title":"[2510.12276] Spatial Forcing: Implicit Spatial Representation Alignment for Vision-language-action Model","url":"https://arxiv.org/abs/2510.12276"},{"title":"Spatial Forcing: Implicit Spatial Representation Alignment for Vision-language-action Model | OpenReview","url":"https://openreview.net/forum?id=euMVC1DO4k"},{"title":"Spatial Forcing","url":"https://spatial-forcing.github.io/"},{"title":"Spatial Forcing: Implicit Spatial Representation Alignment for Vision-language-action Model","url":"https://www.researchgate.net/publication/396500145_Spatial_Forcing_Implicit_Spatial_Representation_Alignment_for_Vision-language-action_Model"},{"title":"[Literature Review] Spatial Forcing: Implicit Spatial Representation Alignment for Vision-language-action Model","url":"https://www.themoonlight.io/en/review/spatial-forcing-implicit-spatial-representation-alignment-for-vision-language-action-model"},{"title":"CorridorVLA: Explicit Spatial Constraints for Generative Action Heads via Sparse Anchors","url":"https://arxiv.org/html/2604.21241"},{"title":"SPATIAL FORCING","url":"https://openreview.net/pdf/aaa4ee40d98552e39b3ce25d8301cadf300d58ec.pdf"},{"title":"Paper page - Spatial Forcing: Implicit Spatial Representation Alignment for Vision-language-action Model","url":"https://huggingface.co/papers/2510.12276"}]

Based on the search results, I found comprehensive information about Spatial Forcing:

## Spatial Forcing Overview

Spatial Forcing (SF) is a simple yet effective alignment strategy that implicitly forces VLA models to develop spatial comprehension capabilities without relying on explicit 3D inputs.

## The Problem It Addresses

Most VLAs are built upon vision-language models pretrained sol
…[truncated 1214 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan-b-literature_20260526T095830",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-26T10:04:17.075248+00:00_

Web search results for query: ""auxiliary depth" OR "auxiliary occupancy" "does not help" OR "harmful" OR "detrimental" robot policy learning VLA 2024 2025"

Links: [{"title":"GitHub - jonyzhang2023/awesome-embodied-vla-va-vln: A curated list of state-of-the-art research in embodied AI, focusing on vision-language-action (VLA) models, vision-language navigation (VLN), and related multimodal learning approaches. · GitHub","url":"https://github.com/jonyzhang2023/awesome-embodied-vla-va-vln"},{"title":"VLA-RL: Towards Masterful and General Robotic Manipulation with Scalable Reinforcement Learning","url":"https://arxiv.org/html/2505.18719v1"},{"title":"NoTVLA: Narrowing of Dense Action Trajectories for Generalizable Robotic Manipulation","url":"https://arxiv.org/html/2510.03895v1"},{"title":"MimicDreamer: Aligning Human and Robot Demonstrations for Scalable VLA Training","url":"https://arxiv.org/html/2509.22199v1"},{"title":"Pure Vision Language Action (VLA) Models: A Comprehensive Survey","url":"https://arxiv.org/html/2509.19012v1"}]

Let me perform another search with different keywords to find more specific results about auxiliary depth or occupancy being harmful in VLA research.

Links: [{"title":"NoTVLA: Narrowing of Dense Action Trajectories for Generalizable Robotic Manipulation","url":"https://arxiv.org/html/2510.03895v1"},{"title":"Paper page - VLA-0: Building State-of-the-Art VLAs with Zero Modification","url":"https://huggingface.co/papers/2510.13054"},{"title":"How brittle are the VLA models in robotics | by Yanan Chen | Medium","url":"https://medium.com/@yananchen1116/how-brittle-are-the-vla-models-in-robotics-66ab85286ecf"},{"title":"Do World Action Models Generalize Better than VLAs? A Robustness Study","url":"https://arxiv.org/html/2603.22078v1"},{"title":"QDepth-VLA: Quantized Depth Prediction as Auxiliary Supervision for Vision-Language-Action Models","url":"https://arxiv.org/pdf/2510.14836"},{"title":"SG-VLA: Learning Spatially-Grounded Vision-Languag
…[truncated 1987 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan-b-literature_20260526T095830",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 67 · 2026-05-26T10:04:17.075435+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/html/2510.14836v2",
  "prompt": "Extract from the introduction and related work sections: 1) What specific evidence or citations do they give that naïve depth prediction auxiliary tasks can be detrimental to VLA policy learning? 2) What are the three mechanisms they identify (supervision quality, redundant signals, interference with pre-trained representations)? Quote or paraphrase the specific claims. 3) What existing works do they cite that show depth auxiliary tasks failing?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_plan-b-literature_20260526T095830",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/html/2510.14836v2",
    "prompt": "Extract from the introduction and related work sections: 1) What specific evidence or citations do they give that naïve depth prediction auxiliary tasks can be detrimental to VLA policy learning? 2) What are the three mechanisms they identify (supervision quality, redundant signals, interference with pre-trained representations)? Quote or paraphrase the specific claims. 3) What existing works do they cite that show depth auxiliary tasks failing?"
  }
}
```

</details>

---

### Tool call

_source line 68 · 2026-05-26T10:04:17.075571+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2510.12276",
  "prompt": "Extract full title, authors, year, venue. How does Spatial Forcing differ from explicit auxiliary prediction (like depth/occupancy prediction head)? Does it discuss why explicit 3D auxiliary tasks can fail?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_plan-b-literature_20260526T095830",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2510.12276",
    "prompt": "Extract full title, authors, year, venue. How does Spatial Forcing differ from explicit auxiliary prediction (like depth/occupancy prediction head)? Does it discuss why explicit 3D auxiliary tasks can fail?"
  }
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-26T10:04:17.075727+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"task weighting\" \"auxiliary task\" \"representation collapse\" OR \"feature distortion\" multi-task shared encoder"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_plan-b-literature_20260526T095830",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"task weighting\" \"auxiliary task\" \"representation collapse\" OR \"feature distortion\" multi-task shared encoder"
  }
}
```

</details>

---

### Tool call

_source line 70 · 2026-05-26T10:04:17.075863+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Zamir Taskonomy \"task transfer learning\" which tasks compete visual representations CVPR 2018"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_plan-b-literature_20260526T095830",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Zamir Taskonomy \"task transfer learning\" which tasks compete visual representations CVPR 2018"
  }
}
```

</details>

---

### Tool result

_source line 71 · 2026-05-26T10:04:17.075995+00:00_

# Analysis of QDepth-VLA's Claims on Depth Prediction Challenges

## 1) Evidence That Naive Depth Prediction Can Be Detrimental

The paper states: "existing works that employ depth-map–based visual prediction as auxiliary tasks...have not achieved consistent performance improvements, and in some cases even indicate that introducing depth prediction as an auxiliary loss can be detrimental to policy learning due to noisy supervision and weak geometric grounding."

However, the document does **not cite specific prior works** that demonstrated this detrimental effect. It references Zhang2025DreamVLAAV as an existing depth-based auxiliary approach, but doesn't explicitly cite papers showing failures.

## 2) Three Identified Mechanisms

The authors articulate three distinct challenges:

1. **Supervision Quality**: "the supervision quality of depth maps is often limited by insufficient spatial–temporal consistency across frames...introducing substantial noise that weakens geometric grounding."

2. **Redundant Signals**: "pixel-wise depth regression produces highly redundant learning signals, forcing the model to reconstruct every pixel rather than focusing on salient structural cues."

3. **Semantic Interference**: "using a vision–language backbone to predict depth maps may interfere with its pre-trained semantic alignment, potentially degrading multimodal reasoning."

## 3) Cited Works Showing Depth Failures

The paper does **not explicitly cite any prior work demonstrating that depth auxiliary tasks failed**. It references DreamVLA (Zhang2025) as an example of depth-based auxiliary supervision but does not cite it as evidence of failure—only as context for their proposed improvement.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan-b-literature_20260526T095830",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 72 · 2026-05-26T10:04:17.076145+00:00_

# Paper Details

**Full Title:** Spatial Forcing: Implicit Spatial Representation Alignment for Vision-language-action Model

**Authors:** Fuhao Li, Wenxuan Song, Han Zhao, Jingbo Wang, Pengxiang Ding, Donglin Wang, Long Zeng, Haoang Li

**Year:** 2025

**Venue:** arXiv (cs.RO - Computer Science, Robotics)

---

# Key Distinction from Explicit Auxiliary Tasks

Based on the abstract provided, Spatial Forcing fundamentally differs from explicit auxiliary prediction approaches in its approach to spatial reasoning:

**The Core Difference:**
Rather than adding prediction heads for depth or occupancy, Spatial Forcing "implicitly forces VLA models to develop spatial comprehension" by aligning intermediate visual embeddings with 3D foundation model representations. This indirect alignment strategy avoids the need for explicit 3D ground truth annotations.

**Why Explicit Methods Struggle:**
The paper identifies that explicit 3D approaches "face challenges due to sensor noise, hardware heterogeneity, and incomplete depth coverage in existing datasets." Additionally, methods attempting to estimate 3D information from 2D images "suffer from the limited performance of depth estimators."

The implicit alignment strategy thus bypasses these bottlenecks by leveraging pretrained 3D models rather than requiring direct supervision or estimation of spatial properties.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan-b-literature_20260526T095830",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 73 · 2026-05-26T10:04:17.076306+00:00_

Web search results for query: ""task weighting" "auxiliary task" "representation collapse" OR "feature distortion" multi-task shared encoder"

Links: [{"title":"Adaptive Task Weighting in Multi-Task Learning","url":"https://www.emergentmind.com/topics/adaptive-task-weighting-in-multi-task-learning"},{"title":"c2al: cohort-contrastive auxiliary learn","url":"https://arxiv.org/pdf/2510.02215"},{"title":"Learning Representation for Multitask Learning through Self-Supervised Auxiliary Learning","url":"https://arxiv.org/html/2409.16651v1"},{"title":"Multi-task Speech Learning - Arun Baby","url":"https://www.arunbaby.com/speech-tech/0036-multi-task-speech-learning/"},{"title":"Survey on Self-Supervised Learning: Auxiliary Pretext Tasks and Contrastive Learning Methods in Imaging - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC9029566/"},{"title":"Cross-task Attention Mechanism for Dense Multi-task Learning","url":"https://arxiv.org/html/2206.08927v2"},{"title":"Towards Task-Compatible Compressible Representations","url":"https://arxiv.org/html/2405.10244"},{"title":"Cross-Task & Cross-Domain Shared Encoders","url":"https://www.emergentmind.com/topics/cross-task-and-cross-domain-shared-encoders"},{"title":"Cross-task Attention Mechanism for Dense Multi-task Learning Ivan Lopes Inria","url":"https://openaccess.thecvf.com/content/WACV2023/papers/Lopes_Cross-Task_Attention_Mechanism_for_Dense_Multi-Task_Learning_WACV_2023_paper.pdf"}]

Here are the search results for your query about task weighting, auxiliary tasks, representation collapse, and feature distortion in multi-task learning with shared encoders:

## Key Findings:

**Adaptive Task Weighting Approaches:**
Recent algorithms combine uncertainty weighting in the decoder with gradient norm balancing and uncertainty mapping in the shared encoder, as in the Impartial Auxiliary Learning method (IAL).

**Core Challenges:**
Auxiliary tasks may be harmful if their signal does not align with the main task, or if label n
…[truncated 1090 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan-b-literature_20260526T095830",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 74 · 2026-05-26T10:04:17.076485+00:00_

Web search results for query: "Zamir Taskonomy "task transfer learning" which tasks compete visual representations CVPR 2018"

Links: [{"title":"Taskonomy: Disentangling Task Transfer Learning","url":"https://openaccess.thecvf.com/content_cvpr_2018/html/Zamir_Taskonomy_Disentangling_Task_CVPR_2018_paper.html"},{"title":"Taskonomy","url":"http://taskonomy.stanford.edu/"},{"title":"Taskonomy: Disentangling Task Transfer Learning (CVPR 2018 Best Paper Winner) | TWIML - The Voice of Machine Learning & AI","url":"https://twimlai.com/podcast/twimlai/taskonomy-disentangling-task-transfer-learning-cvpr-2018-best-paper-winner-amir-zamir/"},{"title":"Taskonomy: Disentangling Task Transfer Learning Amir R. Zamir1,2","url":"https://openaccess.thecvf.com/content_cvpr_2018/papers/Zamir_Taskonomy_Disentangling_Task_CVPR_2018_paper.pdf"},{"title":"taskonomy/taskbank at master · StanfordVL/taskonomy","url":"https://github.com/StanfordVL/taskonomy/tree/master/taskbank"},{"title":"Taskonomy: Disentangling Transfer Learning for Perception with Amir Zamir","url":"https://twimlai.com/twiml-talk-164-taskonomy-disentangling-transfer-learning-for-perception-cvpr-2018-best-paper-winner-with-amir-zamir/"},{"title":"[1804.08328] Taskonomy: Disentangling Task Transfer Learning","url":"https://arxiv.org/abs/1804.08328"},{"title":"Taskonomy: Disentangling Transfer Learning for Perception with Amir Zamir | by The TWIML AI Podcast | The TWIML AI Podcast | Medium","url":"https://medium.com/this-week-in-machine-learning-ai/taskonomy-disentangling-transfer-learning-for-perception-with-amir-zamir-e8e3b102a7e2"},{"title":"Google Scholar","url":"https://scholar.google.com/scholar?q=Zamir%2C+A.R.%2C+Sax%2C+A.%2C+Shen%2C+W.B.%2C+Guibas%2C+L.%2C+Malik%2C+J.%2C+Savarese%2C+S.%3A+Taskonomy%3A+disentangling+task+transfer+learning.+In%3A+2018+IEEE+Conference+on+Computer+Vision+and+Pattern+Recognition+%28CVPR%29.+IEEE+%282018%29"},{"title":"taskonomy/taskbank/README.md at master · StanfordVL/taskonomy","url":"ht
…[truncated 1572 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan-b-literature_20260526T095830",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 75 · 2026-05-26T10:04:17.076726+00:00_

called mcp__agent-ml-research__save_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__save_project_file</summary>

```json
{
  "project": "occsafe_vla",
  "file": "memory.md",
  "content": "# Memory\n\n## 2026-05-26 Eval Readiness Pre-check\n\n### CRITICAL: westd-10894 Disk Full Crisis (discovered ~04:30 UTC)\n- 10894 disk 100% full (250G/250G, 824K free). Root cause: 229G in /root/autodl-tmp/checkpoints/ from accumulated old experiments.\n- 3 resume experiments (mvp_occ_s3, full_occ_ln_s3, ablation_occ_detach_s3) ALL CRASHED at ~04:24 UTC (exit code 1) during 30000_chkpt save.\n  - ablation_occ_detach_s3: 30000_chkpt COMPLETE (saved first, got lucky)\n  - full_occ_ln_s3: 30000_chkpt BROKEN (only tokenizer files). 20000_chkpt intact.\n  - mvp_occ_s3: 30000_chkpt NEVER CREATED. 20000_chkpt intact.\n- cutoff_45k_s2_v2 still running (step ~10624/50005), will crash at step 20000 (~8h) when next checkpoint save triggers.\n\n### Checkpoint Naming: Resume experiments use LOCAL step numbers\n- Resume experiments (loaded 20K ckpt as vla_path, NOT --resume flag): checkpoints at 10000, 20000, 30000 (local steps)\n- From-scratch experiments: checkpoints at 10000, 20000, ..., 50000\n- eval_batch_10894.sh and cka_batch_s3.sh both reference `50000_chkpt` for resume experiments → WRONG, should be `30000_chkpt`\n\n## 2026-05-26 Plan B 文献调研 — 辅助监督在 VLA/机器人中的负面效果\n\n### 一、Negative Transfer / Auxiliary Task 有害的先例\n\n#### 1. ForkMerge: Mitigating Negative Transfer in Auxiliary-Task Learning\n- **作者**: Junguang Jiang, Baixu Chen, Junwei Pan, Ximei Wang, Liu Dapeng, Jie Jiang, Mingsheng Long\n- **年份/Venue**: NeurIPS 2023\n- **核心发现**: 负迁移来源于两个层面——(1) 优化层面的梯度冲突，(2) 泛化层面的辅助任务知识无法有效迁移到目标域。提出 ForkMerge：周期性分叉模型、自动搜索任务权重、合并分支以过滤有害参数更新。\n- **与我们的关系**: 直接支持我们的核心论点——auxiliary OCC head 导致的性能下降可以从 optimization（梯度冲突）和 generalization（OCC 知识无法迁移到 action prediction）两个角度解释。ForkMerge 是我们 detach 实验的理论对标：detach 切断梯度流 ≈ 消除 optimization 层面的干扰，但 Detach 配置仍 ≤ vanilla 说明可能还有 representation competition（shared backbone capacity 被占用）的问题。\n\n#### 2. Which Tasks Should Be Learned Together in Multi-task Learning?\n- **作者**: Trevor Standley, Amir R. Zamir, Dawn Chen, Leonidas Guibas, Jitendra Malik, Silvio Savarese\n- **年份/Venue**: ICML 2020\n- **核心发现**: 任务目标可以竞争——在单一网络中同时学习多个任务可能导致性能低于分别学习。提出任务分组框架，将合作任务放在同一网络，竞争任务分开。关键洞见：更相似的任务不一定训练得更好，task affinity 与 transfer learning affinity 没有相关性。\n- **与我们的关系**: Occupancy prediction 和 action prediction 虽然都需要空间理解，但 Standley 的框架表明\"直觉上相关\"不等于\"训练上兼容\"。我们的实验结果是这一理论的 VLA 领域实证。\n\n#### 3. QDepth-VLA: Quantized Depth Prediction as Auxiliary Supervision for VLA Models\n- **作者**: Yixuan Li, Yuhui Chen, Mingcai Zhou, Haoran Li, Zhengtao Zhang, Dongbin Zhao\n- **年份/Venue**: arXiv 2025 (cs.CV/cs.RO)\n- **核心发现**: 明确指出 naïve depth map 辅助监督可能对 VLA 策略学习有害，识别三个机制：\n  1. **监督质量问题**: depth map 帧间空间-时间一致性不足，引入噪声，削弱几何 grounding\n  2. **冗余学习信号**: 逐像素 depth regression 产生高度冗余信号，迫使模型重建每个像素而非聚焦操作关键的结构线索\n  3. **干扰预训练表征**: 用 vision-language backbone 预测 depth map 可能干扰其预训练的语义对齐，降低多模态推理性能\n- **与我们的关系**: **极其相关**。QDepth-VLA 的第三点\"干扰预训练表征\"直接解释了我们 Full OCC 配置（梯度回传到 backbone）为何比 Detach 配置更差——OCC loss 梯度破坏了 backbone 的 pre-trained semantic alignment。我们的 OCC 实验可以看作 QDepth-VLA 所指出问题的一个极端案例（occupancy 比 depth 更 dense，干扰更大）。但 QDepth-VLA 只是提出问题然后给解法，没有系统的 controlled experiment 来量化这个负面效应。我们的 2×2 factorial design 填补了这个实证空白。\n\n#### 4. Spatial Forcing: Implicit Spatial Representation Alignment for VLA Model\n- **作者**: Fuhao Li, Wenxuan Song, Han Zhao, Jingbo Wang, Pengxiang Ding, Donglin Wang, Long Zeng, Haoang Li\n- **年份/Venue**: arXiv 2025 (cs.RO)\n- **核心发现**: 提出隐式对齐策略替代显式辅助预测——将 VLA 中间视觉 embedding 与预训练 3D 基础模型的几何表征对齐（cosine similarity loss），而非添加 depth/occupancy prediction head。显式方法的问题：sensor noise、hardware heterogeneity、depth estimator 性能有限。\n- **与我们的关系**: Spatial Forcing 选择隐式对齐而非显式预测 head，间接论证了我们的发现——显式 auxiliary spatial prediction head 不是注入 3D 理解的最优方式。我们的实验从安全性角度进一步证实了这一点。\n\n### 二、VLA 安全性相关工作\n\n#### 5. VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer (AEGIS)\n- **作者**: Songqiao Hu, Zeyi Liu, Shuang Liu, Jun Cen, Zihan Meng, Xiao He\n- **年份/Venue**: arXiv 2025 (cs.RO)\n- **核心发现**: 提出 AEGIS 架构——通过 control barrier function 实现即插即用的安全约束层，不需要重训 VLA。构建 SafeLIBERO benchmark（32 场景，1600 episodes，从 LIBERO 衍生，按障碍物干预程度分 Level I/II）。Collision avoidance rate: 77.9%（vs baseline 18.7%）。\n- **与我们的关系**: **直接竞品/baseline**。我们使用相同的 SafeLIBERO benchmark 和 CAR 指标。VLSA 的方法是 post-hoc constraint（不改变训练），而我们的方法是 training-time auxiliary supervision——两种不同的安全增强范式。我们的负面结果表明 training-time auxiliary supervision 这条路径可能根本行不通（至少对 occupancy prediction 而言），进一步验证了 VLSA 选择 post-hoc constraint 路线的合理性。\n\n#### 6. SafeVLA: Towards Safety Alignment of Vision-Language-Action Model via Safe Reinforcement Learning\n- **作者**: Borong Zhang, Yuhao Zhang, Jiaming Ji, Yingshan Lei, Josef Dai, Yuanpei Chen, Yaodong Yang\n- **年份/Venue**: ICML 2025\n- **核心发现**: 用 constrained MDP + Lagrangian dual optimization 将安全约束纳入 VLA 训练。在 Safety-CHORES benchmark 上实现 83.58% cost reduction，同时 success rate 提升 3.85%。方法核心：把安全当作约束而非辅助任务。\n- **与我们的关系**: SafeVLA 把安全建模为约束（constraint），我们把空间感知建模为辅助任务（auxiliary task）。两种路径的对比强化了我们的论点：VLA 安全性可能不应该通过 auxiliary prediction head 来实现，而应该通过更直接的约束机制。\n\n#### 7. Safe-VLN: Collision Avoidance for Vision-and-Language Navigation\n- **作者**: (2023, arXiv)\n- **核心发现**: 在 vision-language navigation 场景中用 occupancy mask（来自 2D LiDAR 仿真）来约束 waypoint 预测，防止 waypoint 落在障碍物区域。\n- **与我们的关系**: 另一种使用 occupancy 信息增强安全性的方法，但用法不同——Safe-VLN 用 occupancy 做硬约束（filtering），不是辅助损失。再次支持\"occupancy 信息应该作为约束而非训练信号\"的论点。\n\n### 三、VLA + 空间/3D 辅助任务（正面结果 — 形成对比）\n\n#### 8. AuxVLA: Auxiliary Task Learning and Multi-Modal Enhancement for VLA Models\n- **作者**: Ruisen Tu, Arth Shukla, Sohyun Yoo, Xuanlin Li, Junxi Li, Jianwen Xie, Hao Su, Zhuowen Tu\n- **年份/Venue**: ICLR 2026\n- **核心发现**: 添加多种辅助解码器（global position, joint configuration, grasp affordance, target position, segmentation mask）到 VLA，在 mobile manipulation 中取得好效果。\n- **与我们的关系**: AuxVLA 是正面案例——但关键区别：(1) AuxVLA 的辅助任务是高度 action-relevant 的（joint config, grasp affordance），而 OCC 是 dense spatial prediction，与 action 的耦合度低；(2) AuxVLA 的任务粒度多样（有 sparse 的也有 dense 的），不像 OCC 全是 dense。这个对比可以帮助我们的论文解释\"并非所有辅助任务都有害，而是 dense spatial prediction 特别容易产生干扰\"。\n\n#### 9. SpatialVLA: Exploring Spatial Representations for Visual-Language-Action Model\n- **作者**: Delin Qu, Haoming Song, et al.\n- **年份/Venue**: RSS 2025\n- **核心发现**: 通过 Ego3D Position Encoding 注入 3D 信息，用 Adaptive Action Grids 表征空间动作。在 1.1M 机器人 episodes 上预训练，展示 zero-shot 泛化能力。LIBERO-Spatial 88.2% 成功率。\n- **与我们的关系**: SpatialVLA 把 3D 信息注入到 input encoding 层面而非作为 auxiliary prediction head，是另一种避免 auxiliary task interference 的设计选择。\n\n#### 10. GeoVLA: Empowering 3D Representations in Vision-Language-Action Models\n- **作者**: Lin Sun, Bin Xie, Yingfei Liu, Hao Shi, Tiancai Wang, Jale Cao\n- **年份/Venue**: arXiv 2025\n- **核心发现**: 用 Point Embedding Network 将 depth→point cloud 的 3D geometric embedding 与 VL embedding 拼接，通过 3D-enhanced Action Expert 融合。LIBERO 和 ManiSkill2 上 SOTA。\n- **与我们的关系**: 又一个把 3D 信息作为额外 input 而非 auxiliary prediction target 的例子。形成一个清晰的模式：成功的空间增强方法倾向于把 3D 信息作为输入或对齐目标，而非要求 shared backbone 去预测 dense spatial output。\n\n### 四、梯度冲突 / Negative Transfer 理论基础\n\n#### 11. PCGrad: Gradient Surgery for Multi-Task Learning\n- **作者**: Tianhe Yu, Saurabh Kumar, Abhishek Gupta, Sergey Levine, Karol Hausman, Chelsea Finn\n- **年份/Venue**: NeurIPS 2020\n- **核心发现**: 当多任务梯度方向冲突时，PCGrad 将每个任务的梯度投影到其他任务梯度的法平面上，消除冲突分量。在 multi-task supervised learning 和 multi-task RL 中都取得了显著提升。\n- **与我们的关系**: PCGrad 的核心假设（梯度冲突是负迁移的主要机制）为我们理解 OCC loss 如何干扰 action loss 提供理论框架。我们的 detach 实验是 PCGrad 的一个极端版本——完全切断（而非投影）OCC 梯度对 backbone 的影响。Detach 仍不如 vanilla 的结果暗示问题不仅在梯度层面，还有 capacity competition。\n\n#### 12. GradNorm: Gradient Normalization for Adaptive Loss Balancing in Deep Multitask Networks\n- **作者**: Zhao Chen, Vijay Badrinarayanan, Chen-Yu Lee, Andrew Rabinovich\n- **年份/Venue**: ICML 2018\n- **核心发现**: 动态调整梯度 magnitude 以平衡多任务训练。只调 magnitude 不调方向，因此与 PCGrad 互补。\n- **与我们的关系**: 我们的实验中 OCC loss weight 是固定的，GradNorm 提供了一种可能的缓解策略——但我们的论文可以论证：即使有更好的 loss balancing，根本问题（dense spatial prediction 干扰 pre-trained representation）仍然存在。\n\n#### 13. Taskonomy: Disentangling Task Transfer Learning\n- **作者**: Amir R. Zamir, Alexander Sax, William Shen, Leonidas J. Guibas, Jitendra Malik, Silvio Savarese\n- **年份/Venue**: CVPR 2018 (Best Paper)\n- **核心发现**: 构建 26 个视觉任务之间的迁移学习 taxonomy，发现任务间存在结构化的迁移关系——有些任务 pair 互利，有些互害。\n- **与我们的关系**: Taskonomy 是理解任务关系的经典工作。在 Taskonomy 的框架下，我们可以论证 occupancy prediction 和 action prediction 在 VLA 的 task taxonomy 中是竞争关系而非合作关系，尽管直觉上它们应该互补。\n\n### 五、Negative Result 论文的发表范式与写作策略\n\n#### 14. Position: Embracing Negative Results in Machine Learning\n- **作者**: Florian Karl, Lukas Malte Kemeter, Gabriel Dax, Paulina Sierak\n- **年份/Venue**: ICML 2024 (PMLR 235:23256-23265)\n- **核心论点**: 预测性能不应是判断论文价值的唯一标准。负面结果的发表有助于减少社区效率低下、纠正错误激励。\n- **与我们的关系**: 为我们论文的存在价值提供元层面的辩护。可以在 Introduction 中引用，说明 negative/cautionary result 在 ML 社区中的价值正在被认可。\n\n#### 15. Position: ML Conferences Should Establish a \"Refutations and Critiques\" Track\n- **作者**: Rylan Schaeffer, Joshua Kazdan, Yegor Denisov-Blanch, Brando Miranda, et al.\n- **年份/Venue**: arXiv 2025\n- **核心论点**: ML 会议缺乏纠错机制，应建立 R&C track。引用了成功的批判性论文案例：Agarwal et al. (2021) 证明 deep RL 缺乏真正进步、Carlini et al. (2022) 反驳隐私声明。\n- **与我们的关系**: 进一步佐证 cautionary/critical study 在学术界的合法性。\n\n### 六、对论文 Framing 的建议\n\n基于以上调研，Plan B 论文的最佳 framing 策略：\n\n1. **不要只说\"不行\"，要说\"为什么不行\"**: QDepth-VLA 已经指出 dense spatial auxiliary task 可能干扰 VLA 的三个机制，但没有 controlled experiment。我们的 2×2 factorial design（gradient flow × normalization）是第一个系统量化这些干扰机制的工作。\n\n2. **定位为 mechanism analysis 而非 failure report**: 标题已经很好——\"Does Auxiliary Spatial Supervision Make VLA Models Safer? A Mechanism Analysis\"。重点不是\"我们试了没用\"，而是\"通过系统的消融实验，我们揭示了 auxiliary spatial supervision 在 VLA 中失败的机制\"。\n\n3. **利用正面结果论文形成对比**: AuxVLA（action-relevant sparse auxiliary tasks 有效）vs 我们（dense spatial prediction 无效）→ 暗示 auxiliary task 的设计选择至关重要，不是\"加了就好\"。SpatialVLA/GeoVLA/Spatial Forcing 都把 3D 信息作为 input 或 alignment target 而非 prediction head → 我们的负面结果为\"为什么这些方法选择避免 auxiliary prediction head\"提供了实证解释。\n\n4. **与 VLA Safety 文献建立联系**: VLSA 用 post-hoc constraint、SafeVLA 用 constrained RL、我们用 auxiliary supervision → 三种范式的对比表明 auxiliary supervision 可能不是 VLA 安全性的正确路径。\n\n5. **Gradient interference 理论线**: Full OCC（梯度回传）< Detach OCC（切断梯度）< Vanilla → 两层问题：(a) 梯度冲突（Full vs Detach 差异），(b) capacity/representation competition（Detach vs Vanilla 差异）。这为 mechanism analysis 提供了清晰的叙事结构。\n\n6. **BN vs LN 的发现作为额外 insight**: BN 在所有配置中都比 LN 差 → normalization 选择在 multi-task VLA 中很重要，BN 的 batch statistics 可能在 multi-task 训练中不稳定。这是一个独立的 practical insight，增加论文的贡献密度。\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_plan-b-literature_20260526T095830",
  "tool": "mcp__agent-ml-research__save_project_file",
  "tool_args": {
    "project": "occsafe_vla",
    "file": "memory.md",
    "content": "# Memory\n\n## 2026-05-26 Eval Readiness Pre-check\n\n### CRITICAL: westd-10894 Disk Full Crisis (discovered ~04:30 UTC)\n- 10894 disk 100% full (250G/250G, 824K free). Root cause: 229G in /root/autodl-tmp/checkpoints/ from accumulated old experiments.\n- 3 resume experiments (mvp_occ_s3, full_occ_ln_s3, ablation_occ_detach_s3) ALL CRASHED at ~04:24 UTC (exit code 1) during 30000_chkpt save.\n  - ablation_occ_detach_s3: 30000_chkpt COMPLETE (saved first, got lucky)\n  - full_occ_ln_s3: 30000_chkpt BROKEN (only tokenizer files). 20000_chkpt intact.\n  - mvp_occ_s3: 30000_chkpt NEVER CREATED. 20000_chkpt intact.\n- cutoff_45k_s2_v2 still running (step ~10624/50005), will crash at step 20000 (~8h) when next checkpoint save triggers.\n\n### Checkpoint Naming: Resume experiments use LOCAL step numbers\n- Resume experiments (loaded 20K ckpt as vla_path, NOT --resume flag): checkpoints at 10000, 20000, 30000 (local steps)\n- From-scratch experiments: checkpoints at 10000, 20000, ..., 50000\n- eval_batch_10894.sh and cka_batch_s3.sh both reference `50000_chkpt` for resume experiments → WRONG, should be `30000_chkpt`\n\n## 2026-05-26 Plan B 文献调研 — 辅助监督在 VLA/机器人中的负面效果\n\n### 一、Negative Transfer / Auxiliary Task 有害的先例\n\n#### 1. ForkMerge: Mitigating Negative Transfer in Auxiliary-Task Learning\n- **作者**: Junguang Jiang, Baixu Chen, Junwei Pan, Ximei Wang, Liu Dapeng, Jie Jiang, Mingsheng Long\n- **年份/Venue**: NeurIPS 2023\n- **核心发现**: 负迁移来源于两个层面——(1) 优化层面的梯度冲突，(2) 泛化层面的辅助任务知识无法有效迁移到目标域。提出 ForkMerge：周期性分叉模型、自动搜索任务权重、合并分支以过滤有害参数更新。\n- **与我们的关系**: 直接支持我们的核心论点——auxiliary OCC head 导致的性能下降可以从 optimization（梯度冲突）和 generalization（OCC 知识无法迁移到 action prediction）两个角度解释。ForkMerge 是我们 detach 实验的理论对标：detach 切断梯度流 ≈ 消除 optimization 层面的干扰，但 Detach 配置仍 ≤ vanilla 说明可能还有 representation competition（shared backbone capacity 被占用）的问题。\n\n#### 2. Which Tasks Should Be Learned Together in Multi-task Learning?\n- **作者**: Trevor Standley, Amir R. Zamir, Dawn Chen, Leonidas Guibas, Jitendra Malik, Silvio Savarese\n- **年份/Venue**: ICML 2020\n- **核心发现**: 任务目标可以竞争——在单一网络中同时学习多个任务可能导致性能低于分别学习。提出任务分组框架，将合作任务放在同一网络，竞争任务分开。关键洞见：更相似的任务不一定训练得更好，task affinity 与 transfer learning affinity 没有相关性。\n- **与我们的关系**: Occupancy prediction 和 action prediction 虽然都需要空间理解，但 Standley 的框架表明\"直觉上相关\"不等于\"训练上兼容\"。我们的实验结果是这一理论的 VLA 领域实证。\n\n#### 3. QDepth-VLA: Quantized Depth Prediction as Auxiliary Supervision for VLA Models\n- **作者**: Yixuan Li, Yuhui Chen, Mingcai Zhou, Haoran Li, Zhengtao Zhang, Dongbin Zhao\n- **年份/Venue**: arXiv 2025 (cs.CV/cs.RO)\n- **核心发现**: 明确指出 naïve depth map 辅助监督可能对 VLA 策略学习有害，识别三个机制：\n  1. **监督质量问题**: depth map 帧间空间-时间一致性不足，引入噪声，削弱几何 grounding\n  2. **冗余学习信号**: 逐像素 depth regression 产生高度冗余信号，迫使模型重建每个像素而非聚焦操作关键的结构线索\n  3. **干扰预训练表征**: 用 vision-language backbone 预测 depth map 可能干扰其预训练的语义对齐，降低多模态推理性能\n- **与我们的关系**: **极其相关**。QDepth-VLA 的第三点\"干扰预训练表征\"直接解释了我们 Full OCC 配置（梯度回传到 backbone）为何比 Detach 配置更差——OCC loss 梯度破坏了 backbone 的 pre-trained semantic alignment。我们的 OCC 实验可以看作 QDepth-VLA 所指出问题的一个极端案例（occupancy 比 depth 更 dense，干扰更大）。但 QDepth-VLA 只是提出问题然后给解法，没有系统的 controlled experiment 来量化这个负面效应。我们的 2×2 factorial design 填补了这个实证空白。\n\n#### 4. Spatial Forcing: Implicit Spatial Representation Alignment for VLA Model\n- **作者**: Fuhao Li, Wenxuan Song, Han Zhao, Jingbo Wang, Pengxiang Ding, Donglin Wang, Long Zeng, Haoang Li\n- **年份/Venue**: arXiv 2025 (cs.RO)\n- **核心发现**: 提出隐式对齐策略替代显式辅助预测——将 VLA 中间视觉 embedding 与预训练 3D 基础模型的几何表征对齐（cosine similarity loss），而非添加 depth/occupancy prediction head。显式方法的问题：sensor noise、hardware heterogeneity、depth estimator 性能有限。\n- **与我们的关系**: Spatial Forcing 选择隐式对齐而非显式预测 head，间接论证了我们的发现——显式 auxiliary spatial prediction head 不是注入 3D 理解的最优方式。我们的实验从安全性角度进一步证实了这一点。\n\n### 二、VLA 安全性相关工作\n\n#### 5. VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer (AEGIS)\n- **作者**: Songqiao Hu, Zeyi Liu, Shuang Liu, Jun Cen, Zihan Meng, Xiao He\n- **年份/Venue**: arXiv 2025 (cs.RO)\n- **核心发现**: 提出 AEGIS 架构——通过 control barrier function 实现即插即用的安全约束层，不需要重训 VLA。构建 SafeLIBERO benchmark（32 场景，1600 episodes，从 LIBERO 衍生，按障碍物干预程度分 Level I/II）。Collision avoidance rate: 77.9%（vs baseline 18.7%）。\n- **与我们的关系**: **直接竞品/baseline**。我们使用相同的 SafeLIBERO benchmark 和 CAR 指标。VLSA 的方法是 post-hoc constraint（不改变训练），而我们的方法是 training-time auxiliary supervision——两种不同的安全增强范式。我们的负面结果表明 training-time auxiliary supervision 这条路径可能根本行不通（至少对 occupancy prediction 而言），进一步验证了 VLSA 选择 post-hoc constraint 路线的合理性。\n\n#### 6. SafeVLA: Towards Safety Alignment of Vision-Language-Action Model via Safe Reinforcement Learning\n- **作者**: Borong Zhang, Yuhao Zhang, Jiaming Ji, Yingshan Lei, Josef Dai, Yuanpei Chen, Yaodong Yang\n- **年份/Venue**: ICML 2025\n- **核心发现**: 用 constrained MDP + Lagrangian dual optimization 将安全约束纳入 VLA 训练。在 Safety-CHORES benchmark 上实现 83.58% cost reduction，同时 success rate 提升 3.85%。方法核心：把安全当作约束而非辅助任务。\n- **与我们的关系**: SafeVLA 把安全建模为约束（constraint），我们把空间感知建模为辅助任务（auxiliary task）。两种路径的对比强化了我们的论点：VLA 安全性可能不应该通过 auxiliary prediction head 来实现，而应该通过更直接的约束机制。\n\n#### 7. Safe-VLN: Collision Avoidance for Vision-and-Language Navigation\n- **作者**: (2023, arXiv)\n- **核心发现**: 在 vision-language navigation 场景中用 occupancy mask（来自 2D LiDAR 仿真）来约束 waypoint 预测，防止 waypoint 落在障碍物区域。\n- **与我们的关系**: 另一种使用 occupancy 信息增强安全性的方法，但用法不同——Safe-VLN 用 occupancy 做硬约束（filtering），不是辅助损失。再次支持\"occupancy 信息应该作为约束而非训练信号\"的论点。\n\n### 三、VLA + 空间/3D 辅助任务（正面结果 — 形成对比）\n\n#### 8. AuxVLA: Auxiliary Task Learning and Multi-Modal Enhancement for VLA Models\n- **作者**: Ruisen Tu, Arth Shukla, Sohyun Yoo, Xuanlin Li, Junxi Li, Jianwen Xie, Hao Su, Zhuowen Tu\n- **年份/Venue**: ICLR 2026\n- **核心发现**: 添加多种辅助解码器（global position, joint configuration, grasp affordance, target position, segmentation mask）到 VLA，在 mobile manipulation 中取得好效果。\n- **与我们的关系**: AuxVLA 是正面案例——但关键区别：(1) AuxVLA 的辅助任务是高度 action-relevant 的（joint config, grasp affordance），而 OCC 是 dense spatial prediction，与 action 的耦合度低；(2) AuxVLA 的任务粒度多样（有 sparse 的也有 dense 的），不像 OCC 全是 dense。这个对比可以帮助我们的论文解释\"并非所有辅助任务都有害，而是 dense spatial prediction 特别容易产生干扰\"。\n\n#### 9. SpatialVLA: Exploring Spatial Representations for Visual-Language-Action Model\n- **作者**: Delin Qu, Haoming Song, et al.\n- **年份/Venue**: RSS 2025\n- **核心发现**: 通过 Ego3D Position Encoding 注入 3D 信息，用 Adaptive Action Grids 表征空间动作。在 1.1M 机器人 episodes 上预训练，展示 zero-shot 泛化能力。LIBERO-Spatial 88.2% 成功率。\n- **与我们的关系**: SpatialVLA 把 3D 信息注入到 input encoding 层面而非作为 auxiliary prediction head，是另一种避免 auxiliary task interference 的设计选择。\n\n#### 10. GeoVLA: Empowering 3D Representations in Vision-Language-Action Models\n- **作者**: Lin Sun, Bin Xie, Yingfei Liu, Hao Shi, Tiancai Wang, Jale Cao\n- **年份/Venue**: arXiv 2025\n- **核心发现**: 用 Point Embedding Network 将 depth→point cloud 的 3D geometric embedding 与 VL embedding 拼接，通过 3D-enhanced Action Expert 融合。LIBERO 和 ManiSkill2 上 SOTA。\n- **与我们的关系**: 又一个把 3D 信息作为额外 input 而非 auxiliary prediction target 的例子。形成一个清晰的模式：成功的空间增强方法倾向于把 3D 信息作为输入或对齐目标，而非要求 shared backbone 去预测 dense spatial output。\n\n### 四、梯度冲突 / Negative Transfer 理论基础\n\n#### 11. PCGrad: Gradient Surgery for Multi-Task Learning\n- **作者**: Tianhe Yu, Saurabh Kumar, Abhishek Gupta, Sergey Levine, Karol Hausman, Chelsea Finn\n- **年份/Venue**: NeurIPS 2020\n- **核心发现**: 当多任务梯度方向冲突时，PCGrad 将每个任务的梯度投影到其他任务梯度的法平面上，消除冲突分量。在 multi-task supervised learning 和 multi-task RL 中都取得了显著提升。\n- **与我们的关系**: PCGrad 的核心假设（梯度冲突是负迁移的主要机制）为我们理解 OCC loss 如何干扰 action loss 提供理论框架。我们的 detach 实验是 PCGrad 的一个极端版本——完全切断（而非投影）OCC 梯度对 backbone 的影响。Detach 仍不如 vanilla 的结果暗示问题不仅在梯度层面，还有 capacity competition。\n\n#### 12. GradNorm: Gradient Normalization for Adaptive Loss Balancing in Deep Multitask Networks\n- **作者**: Zhao Chen, Vijay Badrinarayanan, Chen-Yu Lee, Andrew Rabinovich\n- **年份/Venue**: ICML 2018\n- **核心发现**: 动态调整梯度 magnitude 以平衡多任务训练。只调 magnitude 不调方向，因此与 PCGrad 互补。\n- **与我们的关系**: 我们的实验中 OCC loss weight 是固定的，GradNorm 提供了一种可能的缓解策略——但我们的论文可以论证：即使有更好的 loss balancing，根本问题（dense spatial prediction 干扰 pre-trained representation）仍然存在。\n\n#### 13. Taskonomy: Disentangling Task Transfer Learning\n- **作者**: Amir R. Zamir, Alexander Sax, William Shen, Leonidas J. Guibas, Jitendra Malik, Silvio Savarese\n- **年份/Venue**: CVPR 2018 (Best Paper)\n- **核心发现**: 构建 26 个视觉任务之间的迁移学习 taxonomy，发现任务间存在结构化的迁移关系——有些任务 pair 互利，有些互害。\n- **与我们的关系**: Taskonomy 是理解任务关系的经典工作。在 Taskonomy 的框架下，我们可以论证 occupancy prediction 和 action prediction 在 VLA 的 task taxonomy 中是竞争关系而非合作关系，尽管直觉上它们应该互补。\n\n### 五、Negative Result 论文的发表范式与写作策略\n\n#### 14. Position: Embracing Negative Results in Machine Learning\n- **作者**: Florian Karl, Lukas Malte Kemeter, Gabriel Dax, Paulina Sierak\n- **年份/Venue**: ICML 2024 (PMLR 235:23256-23265)\n- **核心论点**: 预测性能不应是判断论文价值的唯一标准。负面结果的发表有助于减少社区效率低下、纠正错误激励。\n- **与我们的关系**: 为我们论文的存在价值提供元层面的辩护。可以在 Introduction 中引用，说明 negative/cautionary result 在 ML 社区中的价值正在被认可。\n\n#### 15. Position: ML Conferences Should Establish a \"Refutations and Critiques\" Track\n- **作者**: Rylan Schaeffer, Joshua Kazdan, Yegor Denisov-Blanch, Brando Miranda, et al.\n- **年份/Venue**: arXiv 2025\n- **核心论点**: ML 会议缺乏纠错机制，应建立 R&C track。引用了成功的批判性论文案例：Agarwal et al. (2021) 证明 deep RL 缺乏真正进步、Carlini et al. (2022) 反驳隐私声明。\n- **与我们的关系**: 进一步佐证 cautionary/critical study 在学术界的合法性。\n\n### 六、对论文 Framing 的建议\n\n基于以上调研，Plan B 论文的最佳 framing 策略：\n\n1. **不要只说\"不行\"，要说\"为什么不行\"**: QDepth-VLA 已经指出 dense spatial auxiliary task 可能干扰 VLA 的三个机制，但没有 controlled experiment。我们的 2×2 factorial design（gradient flow × normalization）是第一个系统量化这些干扰机制的工作。\n\n2. **定位为 mechanism analysis 而非 failure report**: 标题已经很好——\"Does Auxiliary Spatial Supervision Make VLA Models Safer? A Mechanism Analysis\"。重点不是\"我们试了没用\"，而是\"通过系统的消融实验，我们揭示了 auxiliary spatial supervision 在 VLA 中失败的机制\"。\n\n3. **利用正面结果论文形成对比**: AuxVLA（action-relevant sparse auxiliary tasks 有效）vs 我们（dense spatial prediction 无效）→ 暗示 auxiliary task 的设计选择至关重要，不是\"加了就好\"。SpatialVLA/GeoVLA/Spatial Forcing 都把 3D 信息作为 input 或 alignment target 而非 prediction head → 我们的负面结果为\"为什么这些方法选择避免 auxiliary prediction head\"提供了实证解释。\n\n4. **与 VLA Safety 文献建立联系**: VLSA 用 post-hoc constraint、SafeVLA 用 constrained RL、我们用 auxiliary supervision → 三种范式的对比表明 auxiliary supervision 可能不是 VLA 安全性的正确路径。\n\n5. **Gradient interference 理论线**: Full OCC（梯度回传）< Detach OCC（切断梯度）< Vanilla → 两层问题：(a) 梯度冲突（Full vs Detach 差异），(b) capacity/representation competition（Detach vs Vanilla 差异）。这为 mechanism analysis 提供了清晰的叙事结构。\n\n6. **BN vs LN 的发现作为额外 insight**: BN 在所有配置中都比 LN 差 → normalization 选择在 multi-task VLA 中很重要，BN 的 batch statistics 可能在 multi-task 训练中不稳定。这是一个独立的 practical insight，增加论文的贡献密度。\n"
  }
}
```

</details>

---

### Tool result

_source line 76 · 2026-05-26T10:04:17.076998+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/memory.md\", \"saved\": true}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan-b-literature_20260526T095830",
  "tool": "mcp__agent-ml-research__save_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 77 · 2026-05-26T10:04:17.077172+00:00_

调研完成，已追加到 memory.md。核心发现总结：

**最相关的论文**:
- **QDepth-VLA** (2025) — 明确指出 naïve depth auxiliary supervision 对 VLA 有害的三个机制（监督噪声、冗余信号、干扰预训练表征），但缺乏 controlled experiment。我们的 2×2 factorial design 填补这个空白。
- **ForkMerge** (NeurIPS 2023) — 负迁移的 optimization + generalization 双层解释，直接对应我们的 Full OCC vs Detach vs Vanilla 结果。

**形成清晰对比的模式**: 成功的 VLA 空间增强方法（SpatialVLA, GeoVLA, Spatial Forcing）都把 3D 信息作为 **input 或 alignment target**，而非让 shared backbone 去 predict dense spatial output。AuxVLA 的成功辅助任务是 action-relevant sparse 任务（joint config, grasp affordance），而非 dense spatial prediction。

**VLA Safety 竞品**: VLSA/AEGIS（post-hoc constraint, SafeLIBERO benchmark）和 SafeVLA（constrained RL）都不走 auxiliary supervision 路线——我们的负面结果解释了为什么。

**论文 framing 建议**: 定位为 "mechanism analysis" 而非 "failure report"，核心叙事是两层干扰机制（梯度冲突 + capacity competition），用正面结果论文做对比论证。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_plan-b-literature_20260526T095830"
}
```

</details>

---
