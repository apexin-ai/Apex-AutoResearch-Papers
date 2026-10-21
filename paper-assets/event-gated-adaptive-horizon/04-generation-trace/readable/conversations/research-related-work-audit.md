# research related work audit

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 53
- **Recorded user turns:** 0
- **Tool calls:** 26
- **Original source:** `logs/chats/worker_research_related-work-audit_20260518T135805.jsonl`
- **Structured JSON:** [`f4a1360b739bf1b88881.json`](../../sessions/f4/f4a1360b739bf1b88881.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

53 recorded events

### Tool call

_source line 1 · 2026-05-18T14:01:30.587064+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related-work-audit_20260518T135805",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-18T14:01:30.587646+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Temporal Abstraction.}
5	The options framework \citep{sutton1999options} and model-free action-repetition methods \citep{sharma2017figar, biedenkapp2021temporl, lakshminarayanan2017dynamic} achieve temporal abstraction by training values on real transitions, insulating them from model-induced bias. In world-model RL, the Dreamer family \citep{hafner2020dreamerv1, hafner2021dreamerv2, hafner2023dreamerv3} and transformer-based variants \citep{micheli2023iris, robine2023twm, hafner2025dreamerv4} train policies in imagination at fixed $\dt{=}1$. Several works introduce temporal abstraction via hierarchical representations \citep{gumbsch2024thick, mattes2024hieros}, goal-conditioned jumps \citep{li2025lsimagine}, or multi-scale state-space models \citep{shaj2023mts3}, but none conditions a flat dynamics model on $\dt$ for imagination-based policy training.
6	
7	\paragraph{TAWM and the MPC--Imagination Contrast.}
8	TAWM \citep{nhu2025tawm} conditions a world model on $\dt$ within TD-MPC2 \citep{hansen2024tdmpc2} and achieves consistent gains. The critical distinction is architectural: TAWM re-plans from real states at every step, so model errors do not accumulate into the critic. We show that identical $\dt$-conditioning fails in DreamerV3's imagination loop, where errors compound through bootstrapping and transform manageable imprecision into pathological value overestimation.
9	
10	\paragraph{Value Overestimation.}
11	\citet{thrun1993issues} first identified maximization bias in Q-learning with function approximation. Double Q-learning \citep{vanhasselt2016double} decouples action selection from evaluation; TD3 \citep{fujimoto2018td3} extends this to actor-critic methods via clipped double-Q critics; SAC \citep{haarnoja2018sac} uses entropy regularization to implicitly reduce overestimation; REDQ \citep{chen2021redq} further mitigates overestimation through randomized Q-function ensembles. These model-
…[truncated 2516 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related-work-audit_20260518T135805",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-18T14:01:30.588044+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "docs/paper/**/*.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related-work-audit_20260518T135805",
  "tool": "Glob",
  "tool_args": {
    "pattern": "docs/paper/**/*.bib",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-18T14:01:30.588248+00:00_

docs/paper/_corl_template/corl_2026_template_submission/example.bib
docs/paper/_corl_template/__MACOSX/corl_2026_template_submission/._example.bib
docs/paper/references.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related-work-audit_20260518T135805",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-18T14:01:30.588387+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related-work-audit_20260518T135805",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/references.bib"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-18T14:01:30.588752+00:00_

1	% Auto-generated from literature_map.yaml
2	% 76 entries
3	
4	@article{sutton1999options,
5	  title = {Between MDPs and Semi-MDPs: A Framework for Temporal Abstraction in Reinforcement Learning},
6	  author = {Sutton, R.S and Precup, D and Singh, S},
7	  year = {1999},
8	  journal = {Artificial Intelligence 112},
9	}
10	
11	@inproceedings{hafner2020dreamerv1,
12	  title = {Dream to Control: Learning Behaviors by Latent Imagination},
13	  author = {Hafner, D and Lillicrap, T and Ba, J and Norouzi, M},
14	  year = {2020},
15	  booktitle = {International Conference on Learning Representations},
16	}
17	
18	@article{hafner2023dreamerv3,
19	  title = {Mastering Diverse Domains through World Models},
20	  author = {Hafner, Danijar and Pasukonis, Jurgis and Ba, Jimmy and Lillicrap, Timothy},
21	  year = {2025},
22	  journal = {Nature},
23	  eprint = {2301.04104},
24	  archivePrefix = {arXiv},
25	}
26	
27	@inproceedings{sharma2017figar,
28	  title = {Fine Grained Action Repetition for Deep Reinforcement Learning},
29	  author = {Sharma, S and Lakshminarayanan, A.S and Ravindran, B},
30	  year = {2017},
31	  booktitle = {International Conference on Learning Representations},
32	}
33	
34	@inproceedings{janner2019mbpo,
35	  title = {When to Trust Your Model: Model-Based Policy Optimization},
36	  author = {Janner, M and Fu, J and Zhang, M and Levine, S},
37	  year = {2019},
38	  booktitle = {Advances in Neural Information Processing Systems},
39	}
40	
41	@inproceedings{ke2019learning,
42	  title = {Learning Dynamics Model in Reinforcement Learning by Incorporating the Long Term Future},
43	  author = {Ke, N.R and Singh, A and Touati, A and Goyal, A and Bengio, Y and Parikh, D and Batra, D},
44	  year = {2019},
45	  booktitle = {International Conference on Learning Representations},
46	}
47	
48	@article{asadi2019combating,
49	  title = {Combating the Compounding-Error Problem with a Multi-step Model},
50	  author = {Asadi, K and Misra, D and Kim, S and Littman, M.L},
51	  yea
…[truncated 22973 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related-work-audit_20260518T135805",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-18T14:01:30.589260+00:00_

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
  "session": "worker_research_related-work-audit_20260518T135805",
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

_source line 8 · 2026-05-18T14:01:30.589415+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related-work-audit_20260518T135805",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-18T14:01:30.589571+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "world model reinforcement learning temporal abstraction 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related-work-audit_20260518T135805",
  "tool": "WebSearch",
  "tool_args": {
    "query": "world model reinforcement learning temporal abstraction 2024 2025"
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-18T14:01:30.589698+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "DreamerV3 temporal abstraction variable time step options framework"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related-work-audit_20260518T135805",
  "tool": "WebSearch",
  "tool_args": {
    "query": "DreamerV3 temporal abstraction variable time step options framework"
  }
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-18T14:01:30.589837+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "value overestimation model-based reinforcement learning 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related-work-audit_20260518T135805",
  "tool": "WebSearch",
  "tool_args": {
    "query": "value overestimation model-based reinforcement learning 2024 2025"
  }
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-18T14:01:30.590013+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "critic overestimation world model imagination rollout bias"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related-work-audit_20260518T135805",
  "tool": "WebSearch",
  "tool_args": {
    "query": "critic overestimation world model imagination rollout bias"
  }
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-18T14:01:30.590178+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "TAWM temporal abstraction world model Nhu 2025 ICML"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related-work-audit_20260518T135805",
  "tool": "WebSearch",
  "tool_args": {
    "query": "TAWM temporal abstraction world model Nhu 2025 ICML"
  }
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-18T14:01:30.590303+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "DreamerV3 variant improvement modification 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related-work-audit_20260518T135805",
  "tool": "WebSearch",
  "tool_args": {
    "query": "DreamerV3 variant improvement modification 2024 2025"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-18T14:01:30.590474+00:00_

Web search results for query: "DreamerV3 temporal abstraction variable time step options framework"

Links: [{"title":"TransDreamerV3: Implanting Transformer In DreamerV3","url":"https://arxiv.org/html/2506.17103v1"},{"title":"Learning Temporal Abstractions via Variational Homomorphisms in Option-Induced Abstract MDPs","url":"https://arxiv.org/html/2507.16473"},{"title":"DreamerNav: learning-based autonomous navigation in dynamic indoor environments using world models - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12510832/"},{"title":"Mastering diverse control tasks through world models | Nature","url":"https://www.nature.com/articles/s41586-025-08744-2"},{"title":"Mastering Diverse Control Tasks through World Models","url":"https://danijar.com/project/dreamerv3/"},{"title":"GitHub - danijar/dreamerv3: Mastering Diverse Domains through World Models · GitHub","url":"https://github.com/danijar/dreamerv3"},{"title":"Next Embedding Prediction Makes World Models Stronger","url":"https://arxiv.org/html/2603.02765v1"},{"title":"Mastering diverse control tasks through world models - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12003158/"},{"title":"DreamerV3: Mastering Diverse Domains through World Models","url":"https://vitalab.github.io/article/2023/01/19/DreamerV3.html"},{"title":"Temporal Abstraction and the Options Framework How Agents Learn to Think in Subgoals - Engineering Notes","url":"https://notes.muthu.co/2026/02/temporal-abstraction-and-the-options-framework-how-agents-learn-to-think-in-subgoals/"}]

Based on the search results, I found information relevant to your query. Here's what I discovered:

## DreamerV3 Framework

DreamerV3 is a general algorithm that outperforms specialized methods across over 150 diverse tasks, with a single configuration. Dreamer learns a model of the environment and improves its behaviour by imagining future scenarios, with robustness techniques based on normalization, balancing and transformations enabling stable l
…[truncated 1363 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related-work-audit_20260518T135805",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-18T14:01:30.590687+00:00_

Web search results for query: "value overestimation model-based reinforcement learning 2024 2025"

Links: [{"title":"A value-based deep reinforcement learning model with human expertise in optimal treatment of sepsis | npj Digital Medicine","url":"https://www.nature.com/articles/s41746-023-00755-5"},{"title":"MAD-TD: MODEL-AUGMENTED DATA STABILIZES HIGH ...","url":"https://www.seas.upenn.edu/~eeaton/papers/Voelcker2025MADTD.pdf"},{"title":"model-based offline reinforcement learning","url":"https://arxiv.org/pdf/2407.00699"},{"title":"mad-td: model-augmented data stabilizes high update ratio rl","url":"https://arxiv.org/pdf/2410.08896"},{"title":"The State of Reinforcement Learning in 2025 - DataRoot Labs","url":"https://datarootlabs.com/blog/state-of-reinforcement-learning-2025"},{"title":"“Deep Reinforcement Learning for Autonomous Navigation ...","url":"https://jisem-journal.com/index.php/journal/article/download/3620/1566/5930"},{"title":"[2506.14245] Reinforcement Learning with Verifiable Rewards Implicitly Incentivizes Correct Reasoning in Base LLMs","url":"https://arxiv.org/abs/2506.14245"},{"title":"GitHub - opendilab/awesome-RLVR: A curated list of reinforcement learning with verifiable rewards (continually updated) · GitHub","url":"https://github.com/opendilab/awesome-RLVR"},{"title":"GitHub - yingchengyang/Reinforcement-Learning-Papers: Related papers for reinforcement learning, including classic papers and latest papers in top conferences · GitHub","url":"https://github.com/yingchengyang/Reinforcement-Learning-Papers"},{"title":"[1803.00101] Model-Based Value Estimation for Efficient Model-Free Reinforcement Learning","url":"https://arxiv.org/abs/1803.00101"}]

Here are the search results for "value overestimation model-based reinforcement learning 2024 2025":

## Key Findings

**Value Overestimation in Reinforcement Learning:**

One of the major challenges in offline reinforcement learning (RL) is the overestimation of values for out-of-distribution acti
…[truncated 1447 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related-work-audit_20260518T135805",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-18T14:01:30.591093+00:00_

Web search results for query: "critic overestimation world model imagination rollout bias"

Links: [{"title":"Dreamer: Learning Long-Horizon Behaviors through Latent Imagination | by Dong-Keon Kim | Medium","url":"https://medium.com/@kdk199604/dreamer-learning-long-horizon-behaviors-through-latent-imagination-fa60327c2843"},{"title":"Critiques of World Models","url":"https://arxiv.org/pdf/2507.05169"},{"title":"Mastering diverse control tasks through world models - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12003158/"},{"title":"Realistic Actor-Critic: A framework for balance between value overestimation and underestimation - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC9868235/"},{"title":"World Models with Hints of Large Language ...","url":"https://aclanthology.org/2025.naacl-long.3.pdf"},{"title":"Interpretable World Model Imaginations as Deep Reinforcement Learning Explanation | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-032-08327-2_7"},{"title":"arXiv:2507.05169v1 [cs.LG] 7 Jul 2025 Critiques of World Models","url":"https://arxiv.org/pdf/2507.05169v1"},{"title":"Reinforcement Learning Journal 2025 Cover Page","url":"https://rlj.cs.umass.edu/2025/papers/RLJ_RLC_2025_136.pdf"},{"title":"Critique of World Models As A Path to Human Level Intelligence: A Comprehensive Outline with References | by Jacob Grow | Medium","url":"https://medium.com/@Gbgrow/critique-of-world-models-as-a-path-to-human-level-intelligence-a-comprehensive-outline-with-1a50e459b050"},{"title":"Moderate Actor-Critic Methods: Controlling Overestimation Bias via Expectile Loss","url":"https://arxiv.org/html/2504.09929v1"}]

Here are the search results for your query about critic overestimation, world models, imagination rollout bias:

## Key Findings

### Critic Overestimation in World Models

Undesirable overestimation bias and accumulation of function approximation errors in temporal difference methods may lead to sub-optimal policy updates an
…[truncated 1182 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related-work-audit_20260518T135805",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-18T14:01:30.591334+00:00_

Web search results for query: "world model reinforcement learning temporal abstraction 2024 2025"

Links: [{"title":"Learning Hierarchical World Models with Adaptive Temporal Abstractions from Discrete Latent Dynamics | OpenReview","url":"https://openreview.net/forum?id=TjCDNssXKU"},{"title":"Exploring the limits of hierarchical world models in reinforcement learning | Scientific Reports","url":"https://www.nature.com/articles/s41598-024-76719-w"},{"title":"[2512.20605] Emergent temporal abstractions in autoregressive models enable hierarchical reinforcement learning","url":"https://arxiv.org/abs/2512.20605"},{"title":"Mastering diverse control tasks through world models | Nature","url":"https://www.nature.com/articles/s41586-025-08744-2"},{"title":"Hierarchical Planning with Latent World Models","url":"https://arxiv.org/html/2604.03208v1"},{"title":"ICLR Poster Learning Hierarchical World Models with Adaptive Temporal Abstractions from Discrete Latent Dynamics","url":"https://iclr.cc/virtual/2024/poster/18558"},{"title":"Emergent temporal abstractions in autoregressive models enable hierarchical reinforcement learning","url":"https://arxiv.org/html/2512.20605v1"},{"title":"Published as a conference paper at ICLR 2024 LEARNING HIERARCHICAL WORLD MODELS","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/13b45b44e26c353c64cba9529bf4724f-Paper-Conference.pdf"},{"title":"[Quick Review] Emergent temporal abstractions in autoregressive models enable hierarchical reinforcement learning","url":"https://liner.com/review/emergent-temporal-abstractions-in-autoregressive-models-enable-hierarchical-reinforcement-learning"},{"title":"Humans rationally balance detailed and temporally abstract world models - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC11700031/"}]

I found several highly relevant research papers on world models, reinforcement learning, and temporal abstraction from 2024-2025. Here's a summary of the key findings:

## Recent Advances in Hierarc
…[truncated 2138 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related-work-audit_20260518T135805",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-18T14:01:30.591536+00:00_

Web search results for query: "TAWM temporal abstraction world model Nhu 2025 ICML"

Links: [{"title":"GitHub - anh-nn01/Time-Aware-World-Model: Official Code for Time-Aware World Model (TAWM) with TD-MPC2 as the baseline architecture in the experiments.","url":"https://github.com/anh-nn01/Time-Aware-World-Model"},{"title":"Time-Aware World Model for Adaptive Prediction and Control","url":"https://arxiv.org/html/2506.08441v1"},{"title":"[2506.08441] Time-Aware World Model for Adaptive Prediction and Control","url":"https://arxiv.org/abs/2506.08441"},{"title":"Time-Aware World Model for Adaptive Prediction and Control | OpenReview","url":"https://openreview.net/forum?id=gZ5N3TLjwv"},{"title":"ICML 2025 Schedule","url":"https://icml.cc/virtual/2025/calendar"},{"title":"World Models - ICLR 2025 Workshop","url":"https://sites.google.com/view/worldmodel-iclr2025/"},{"title":"[2404.16078] Learning World Models With Hierarchical Temporal Abstractions: A Probabilistic Perspective","url":"https://arxiv.org/abs/2404.16078"},{"title":"Feature 14 IEEE CIRCUITS AND SYSTEMS MAGAZINE FOURTH QUARTER 2025","url":"https://mn.cs.tsinghua.edu.cn/xinwang/PDF/papers/2025_Embodied%20AI%20from%20LLMs%20to%20World%20Models.pdf"},{"title":"Assessing World Models: Methods and Metrics for Evaluating Understanding","url":"https://icml.cc/virtual/2025/workshop/39967"},{"title":"ICML 2025 Papers","url":"https://icml.cc/virtual/2025/papers.html"}]

Based on the search results, here's information about TAWM (Time-Aware World Model) by Nhu et al. at ICML 2025:

## Overview

Time-Aware World Model (TAWM) is a model-agnostic and more efficient training method for world models, presented by Anh N. Nhu, Sanghyun Son, and Ming C. Lin from the University of Maryland at the International Conference on Machine Learning (ICML) 2025.

## Core Approach

TAWM is a model-based approach that explicitly incorporates temporal dynamics by conditioning on the time-step size (Δt) and training over a diverse range of Δ
…[truncated 1037 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related-work-audit_20260518T135805",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-18T14:01:30.591726+00:00_

Web search results for query: "DreamerV3 variant improvement modification 2024 2025"

Links: [{"title":"GitHub - danijar/dreamerv3: Mastering Diverse Domains through World Models · GitHub","url":"https://github.com/danijar/dreamerv3"},{"title":"Mastering Diverse Control Tasks through World Models","url":"https://danijar.com/project/dreamerv3/"},{"title":"Mastering diverse control tasks through world models - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12003158/"},{"title":"DreamerV3: Robust Latent Model-Based RL","url":"https://www.emergentmind.com/topics/dreamerv3"},{"title":"Extended Abstract - CS 224R Deep Reinforcement Learning","url":"https://cs224r.stanford.edu/projects/pdfs/Set_Dreamer_CS224R_Final_Project.pdf"},{"title":"RLJ | RLC 2024 Dreaming of Many Worlds: Learning Contextual","url":"https://rlj.cs.umass.edu/2024/papers/RLJ_RLC_2024_167.pdf"},{"title":"DreamerV3-style MBRL Agent","url":"https://www.emergentmind.com/topics/dreamerv3-style-mbrl-agent"},{"title":"DreamerV3-XP: Optimizing exploration through uncertainty estimation","url":"https://arxiv.org/html/2510.21418v1"},{"title":"HarmonyDream: Task Harmonization Inside World Models","url":"https://ise.thss.tsinghua.edu.cn/~mlong/doc/HarmonyDream-icml24.pdf"},{"title":"Mastering Diverse Domains through World Models","url":"https://arxiv.org/pdf/2301.04104"}]

Based on the search results, here are the key DreamerV3 variants and improvements from 2024-2025:

## Core DreamerV3 Improvements

DreamerV3 introduced several key improvements including robustness techniques (observation symlog, KL balance with free bits, 1% unimix for categoricals, percentile return normalization, symexp two-hot loss), network architecture changes (block GRU, RMSNorm normalization, SiLU activation), optimizer improvements (adaptive gradient clipping, LaProp), and replay buffer enhancements (larger capacity, online queue, storing and updating latent states).

## Notable Variants and Extensions (2024-2025)

**Exploration E
…[truncated 1225 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related-work-audit_20260518T135805",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-18T14:01:30.591943+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "delusional bias model-based reinforcement learning 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related-work-audit_20260518T135805",
  "tool": "WebSearch",
  "tool_args": {
    "query": "delusional bias model-based reinforcement learning 2024 2025"
  }
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-18T14:01:30.592110+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "TD-MPC2 temporal abstraction action repetition 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related-work-audit_20260518T135805",
  "tool": "WebSearch",
  "tool_args": {
    "query": "TD-MPC2 temporal abstraction action repetition 2024 2025"
  }
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-18T14:01:30.592801+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "options framework world model reinforcement learning 2024 2025 ICLR NeurIPS ICML"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related-work-audit_20260518T135805",
  "tool": "WebSearch",
  "tool_args": {
    "query": "options framework world model reinforcement learning 2024 2025 ICLR NeurIPS ICML"
  }
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-18T14:01:30.592987+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"compounding error\" \"world model\" reinforcement learning 2024 2025 rollout"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related-work-audit_20260518T135805",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"compounding error\" \"world model\" reinforcement learning 2024 2025 rollout"
  }
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-18T14:01:30.593127+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "DreamerV3-XP exploration uncertainty estimation 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related-work-audit_20260518T135805",
  "tool": "WebSearch",
  "tool_args": {
    "query": "DreamerV3-XP exploration uncertainty estimation 2025"
  }
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-18T14:01:30.593274+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "MuDreamer reconstruction-free world model 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related-work-audit_20260518T135805",
  "tool": "WebSearch",
  "tool_args": {
    "query": "MuDreamer reconstruction-free world model 2024"
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-18T14:01:30.593442+00:00_

Web search results for query: "delusional bias model-based reinforcement learning 2024 2025"

Links: [{"title":"Simulating AI Psychosis, Delusion Reinforcement and ...","url":"https://arxiv.org/pdf/2509.10970"},{"title":"AI 101: The State of Reinforcement Learning in 2025","url":"https://www.turingpost.com/p/stateofrl2025"},{"title":"The State of Reinforcement Learning in 2025 - DataRoot Labs","url":"https://datarootlabs.com/blog/state-of-reinforcement-learning-2025"},{"title":"GitHub - opendilab/awesome-model-based-RL: A curated list of awesome model based RL resources (continually updated) · GitHub","url":"https://github.com/opendilab/awesome-model-based-RL"},{"title":"Reinforcement Learning in 2024: Transforming the Landscape of Generative AI and Large Language Models | by Debu Sinha | Medium","url":"https://medium.com/@debusinha2009/reinforcement-learning-in-2024-transforming-the-landscape-of-generative-ai-and-large-language-fee8b65b1a42"},{"title":"Experimental data-efficient reinforcement learning with an ensemble of surrogate models - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S0893608025007506"},{"title":"ICLR 2025 Papers","url":"https://iclr.cc/virtual/2025/papers.html"},{"title":"Handling New Class in Online Label Shift - Peng Zhao","url":"https://www.pengzhao-ml.com/publication/TKDE'25_NOLS.pdf"},{"title":"Latest AI Research (Dec 2025): GPT-5, Agents & Trends | IntuitionLabs","url":"https://intuitionlabs.ai/articles/latest-ai-research-trends-2025"},{"title":"Reinforcement Learning Conference 2024","url":"https://rl-conference.cc/2024/papers.html"}]

Based on the web search results, here's what I found regarding delusional bias in model-based reinforcement learning for 2024-2025:

## Model-Based Reinforcement Learning (2024-2025)

Model-based RL incorporates an internal model of the environment, enabling agents to plan and simulate outcomes before acting. Recent research in 2024-2025 has focused on addressing modeling errors an
…[truncated 1239 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related-work-audit_20260518T135805",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-18T14:01:30.593794+00:00_

Web search results for query: "TD-MPC2 temporal abstraction action repetition 2024 2025"

Links: [{"title":"TD-MPC2","url":"https://www.tdmpc2.com/"},{"title":"GitHub - nicklashansen/tdmpc2: Code for \"TD-MPC2: Scalable, Robust World Models for Continuous Control\" · GitHub","url":"https://github.com/nicklashansen/tdmpc2"},{"title":"Reinforcement Learning Journal 2025 Cover Page","url":"https://rlj.cs.umass.edu/2025/papers/RLJ_RLC_2025_136.pdf"},{"title":"Temporal Difference MPC","url":"https://www.emergentmind.com/topics/temporal-difference-model-predictive-control-td-mpc"},{"title":"[2310.16828] TD-MPC2: Scalable, Robust World Models for Continuous Control","url":"https://arxiv.org/abs/2310.16828"},{"title":"Improving Temporal Difference MPC Through Policy Constraint","url":"https://darthutopian.github.io/tdmpc_square/"},{"title":"[2502.03550] TD-M(PC)$^2$: Improving Temporal Difference MPC Through Policy Constraint","url":"https://arxiv.org/abs/2502.03550"},{"title":"TD-MPC: Temporal Difference for Control","url":"https://www.emergentmind.com/topics/temporal-difference-learning-for-model-predictive-control-td-mpc"},{"title":"TD-MPC2: Scalable, Robust World Models for Continuous Control TD-MPC2","url":"https://iclr.cc/media/iclr-2024/Slides/18722.pdf"},{"title":"TD-M(PC)2: Improving Temporal Difference MPC Through Policy Constraint","url":"https://darthutopian.github.io/tdmpc_square/static/pdfs/paper.pdf"}]

I found several relevant results about TD-MPC2 and related temporal abstraction and action repetition concepts. Here's what the search revealed:

## TD-MPC2 Overview

TD-MPC is a model-based reinforcement learning (MBRL) algorithm that performs local trajectory optimization in the latent space of a learned implicit (decoder-free) world model, with TD-MPC2 presenting a series of improvements upon the TD-MPC algorithm. TD-MPC2 compares favorably to existing model-free and model-based methods across 104 continuous control tasks spanning multiple domains, with a s
…[truncated 1065 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related-work-audit_20260518T135805",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-18T14:01:30.594254+00:00_

Web search results for query: "DreamerV3-XP exploration uncertainty estimation 2025"

Links: [{"title":"[2510.21418] DreamerV3-XP: Optimizing exploration through uncertainty estimation","url":"https://arxiv.org/abs/2510.21418"},{"title":"DreamerV3-XP: Optimizing exploration through uncertainty estimation","url":"https://arxiv.org/html/2510.21418v1"},{"title":"DreamerV3-XP: Optimizing exploration through uncertainty estimation | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/arxiv/2510.21418"},{"title":"(PDF) DreamerV3-XP: Optimizing exploration through uncertainty estimation","url":"https://www.researchgate.net/publication/396924103_DreamerV3-XP_Optimizing_exploration_through_uncertainty_estimation"},{"title":"DreamerV3: Robust Latent Model-Based RL","url":"https://www.emergentmind.com/topics/dreamerv3"},{"title":"(PDF) Exploiting Model Errors for Exploration in Model-Based Reinforcement Learning","url":"https://www.researchgate.net/publication/395384561_Exploiting_Model_Errors_for_Exploration_in_Model-Based_Reinforcement_Learning"},{"title":"Mueed Mohammed's Post","url":"https://www.linkedin.com/posts/mueed-mohammed_ai-machinelearning-dreamerv3-activity-7264338975278997504-6hPa"},{"title":"GitHub - LMD0311/Awesome-World-Model: Collect some World Models for Autonomous Driving (and Robotic, etc.) papers. · GitHub","url":"https://github.com/LMD0311/Awesome-World-Model"},{"title":"DreamerNav: learning-based autonomous navigation in dynamic indoor environments using world models - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12510832/"},{"title":"GitHub - danijar/dreamerv3: Mastering Diverse Domains through World Models · GitHub","url":"https://github.com/danijar/dreamerv3"}]

Based on the search results, here's what I found about DreamerV3-XP:

## Overview

DreamerV3-XP is an extension of DreamerV3 that improves exploration and learning efficiency. It optimizes exploration through uncertainty estimation.

## Key Components

DreamerV3-XP inc
…[truncated 1142 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related-work-audit_20260518T135805",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-18T14:01:30.594467+00:00_

Web search results for query: "options framework world model reinforcement learning 2024 2025 ICLR NeurIPS ICML"

Links: [{"title":"ICLR 2025 Papers","url":"https://iclr.cc/virtual/2025/papers.html"},{"title":"GitHub - DmitryRyumin/ICML-2025-Papers: ICML 2025 Papers: Dive into cutting-edge research from the premier machine learning conference. Stay current with breakthroughs in deep learning, generative AI, optimization, reinforcement learning, and beyond. Code implementations included. ⭐ support the future of machine learning research!","url":"https://github.com/DmitryRyumin/ICML-2025-Papers"},{"title":"GitHub - opendilab/awesome-model-based-RL: A curated list of awesome model based RL resources (continually updated) · GitHub","url":"https://github.com/opendilab/awesome-model-based-RL"},{"title":"Published as a conference paper at ICLR 2025","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/5fc1e662bd63c4a70b95088ba5d08cb8-Paper-Conference.pdf"},{"title":"ICML 2024 Papers","url":"https://icml.cc/virtual/2024/papers.html"},{"title":"ICML 2025 Schedule","url":"https://icml.cc/virtual/2025/calendar"},{"title":"AAAI-26 New Faculty Highlights Program - AAAI","url":"https://aaai.org/conference/aaai/aaai-26/new-faculty-highlights-program/"},{"title":"ICML 2025 Papers","url":"https://icml.cc/virtual/2025/papers.html"},{"title":"ICML Poster Knowledge Retention in Continual Model-Based Reinforcement Learning","url":"https://icml.cc/virtual/2025/poster/45991"},{"title":"Apple Machine Learning Research at ICLR 2025 - Apple Machine Learning Research","url":"https://machinelearning.apple.com/research/iclr-2025"}]

I've completed the web search for your query on options framework, world models, and reinforcement learning research at major 2024-2025 conferences. Here are the key findings:

## Search Results Summary

The search returned information about recent reinforcement learning research at ICLR 2025, NeurIPS 2025, and ICML 2025, though the specific "options frame
…[truncated 1401 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related-work-audit_20260518T135805",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-18T14:01:30.594651+00:00_

Web search results for query: "MuDreamer reconstruction-free world model 2024"

Links: [{"title":"MuDreamer: Learning Predictive World Models without Reconstruction | OpenReview","url":"https://openreview.net/forum?id=9pe38WpsbX"},{"title":"[2405.15083] MuDreamer: Learning Predictive World Models without Reconstruction","url":"https://arxiv.org/abs/2405.15083"},{"title":"(PDF) MuDreamer: Learning Predictive World Models without Reconstruction","url":"https://www.researchgate.net/publication/380894388_MuDreamer_Learning_Predictive_World_Models_without_Reconstruction"},{"title":"MuDreamer: Learning Predictive World Models without Reconstruction","url":"https://arxiv.org/html/2405.15083v1"},{"title":"MUDREAMER: LEARNING PREDICTIVE WORLD ...","url":"https://openreview.net/pdf/8801375407fde3d9751dbb78c2f906238f519a12.pdf"},{"title":"[Literature Review] MuDreamer: Learning Predictive World Models without Reconstruction","url":"https://www.themoonlight.io/en/review/mudreamer-learning-predictive-world-models-without-reconstruction"},{"title":"MuDreamer: Learning Predictive World Mod...","url":"https://axi.lims.ac.uk/paper/2405.15083"},{"title":"DreamerPro: Reconstruction-Free Model-Based Reinforcement Learning","url":"https://proceedings.mlr.press/v162/deng22a/deng22a.pdf"},{"title":"Learning Predictive World Models without Reconstruction","url":"https://www.semanticscholar.org/paper/MuDreamer:-Learning-Predictive-World-Models-without-Burchi-Timofte/c1657ff831dccf187a109ebee73c45a915080156"},{"title":"Learning Predictive World Models without Reconstruction","url":"https://www.connectedpapers.com/main/c1657ff831dccf187a109ebee73c45a915080156/MuDreamer:-Learning-Predictive-World-Models-without-Reconstruction/graph"}]

Based on the search results, here's what I found about MuDreamer:

## Overview

MuDreamer is a robust reinforcement learning agent that builds upon the DreamerV3 algorithm by learning a predictive world model without the need for reconstructing input signals, in
…[truncated 1354 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related-work-audit_20260518T135805",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-18T14:01:30.594864+00:00_

Web search results for query: ""compounding error" "world model" reinforcement learning 2024 2025 rollout"

Links: [{"title":"Reinforcement Learning Journal 2025 Cover Page","url":"https://rlj.cs.umass.edu/2025/papers/RLJ_RLC_2025_136.pdf"},{"title":"Robotic World Model","url":"https://sites.google.com/view/roboticworldmodel"},{"title":"World Model for Robot Learning: A Comprehensive Survey","url":"https://ntumars.github.io/wm-robot-survey/"},{"title":"[Literature Review] Diffusion World Model: Future Modeling Beyond Step-by-Step Rollout for Offline Reinforcement Learning","url":"https://www.themoonlight.io/en/review/diffusion-world-model-future-modeling-beyond-step-by-step-rollout-for-offline-reinforcement-learning"},{"title":"Model-Based Reinforcement Learning","url":"https://www.emergentmind.com/topics/model-based-reinforcement-learning"},{"title":"A unified objective for dynamics model and policy learning ...","url":"https://www.eurekalert.org/news-releases/1056672"},{"title":"The World Model Inflection: 2025 Made It Real | by Graison Thomas | Dec, 2025 | Medium","url":"https://medium.com/@graison/the-world-model-inflection-2025-made-it-real-f5a9c31475d4"},{"title":"World Model for Robot Learning: A Comprehensive Survey","url":"https://arxiv.org/html/2605.00080v1"},{"title":"Learning to Combat Compounding-Error in Model-Based Reinforcement Learning","url":"https://webdocs.cs.ualberta.ca/~chenjun/files/drlw_adambrl_full.pdf"},{"title":"Learning to Combat Compounding-Error in Model-Based Reinforcement Learning | OpenReview","url":"https://openreview.net/forum?id=S1g_S0VYvr"}]

I've found several relevant research results on compounding error in world models for reinforcement learning rollouts. Here's what the search reveals:

## The Compounding Error Problem

Due to compounding model errors, world model-based methods are generally limited to rolling out the model for a small number of time steps, which severely reduces their ability to solve complex tasks that req
…[truncated 1683 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related-work-audit_20260518T135805",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-18T14:01:30.595069+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"TD-M(PC)2\" \"policy constraint\" temporal difference MPC value overestimation 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related-work-audit_20260518T135805",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"TD-M(PC)2\" \"policy constraint\" temporal difference MPC value overestimation 2025"
  }
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-18T14:01:30.595387+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Moderate Actor-Critic expectile loss overestimation bias 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related-work-audit_20260518T135805",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Moderate Actor-Critic expectile loss overestimation bias 2025"
  }
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-18T14:01:30.595705+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Critiques of World Models\" 2025 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related-work-audit_20260518T135805",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Critiques of World Models\" 2025 arxiv"
  }
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-18T14:01:30.595963+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "plasticity loss deep reinforcement learning 2024 2025 capacity network resets"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related-work-audit_20260518T135805",
  "tool": "WebSearch",
  "tool_args": {
    "query": "plasticity loss deep reinforcement learning 2024 2025 capacity network resets"
  }
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-18T14:01:30.596117+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "VANTA semantic temporal abstraction vision language model ICLR 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related-work-audit_20260518T135805",
  "tool": "WebSearch",
  "tool_args": {
    "query": "VANTA semantic temporal abstraction vision language model ICLR 2025"
  }
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-18T14:01:30.596243+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"adaptive rollout length\" model-based reinforcement learning uncertainty 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related-work-audit_20260518T135805",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"adaptive rollout length\" model-based reinforcement learning uncertainty 2024 2025"
  }
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-18T14:01:30.596478+00:00_

Web search results for query: ""TD-M(PC)2" "policy constraint" temporal difference MPC value overestimation 2025"

Links: [{"title":"[2502.03550] TD-M(PC)$^2$: Improving Temporal Difference MPC Through Policy Constraint","url":"https://arxiv.org/abs/2502.03550"},{"title":"TD-M(PC)2: Improving Temporal Difference MPC Through Policy Constraint","url":"https://arxiv.org/html/2502.03550v1"},{"title":"Improving Temporal Difference MPC Through Policy Constraint","url":"https://darthutopian.github.io/tdmpc_square/"},{"title":"TD-M(PC)$^2$: Improving Temporal Difference MPC Through Policy Constraint | OpenReview","url":"https://openreview.net/forum?id=ph7BXPU08c"},{"title":"TD-M(PC)2: Improving Temporal Difference MPC Through Policy Constraint","url":"https://darthutopian.github.io/tdmpc_square/static/pdfs/paper.pdf"},{"title":"[2502.03550v1] TD-M(PC)$^2$: Improving Temporal Difference MPC Through Policy Constraint","url":"http://arxiv.org/abs/2502.03550v1"},{"title":"Guanya Shi ✈️ NeurIPS'25 on X: \"TD-M(PC)^2 (Temporal Difference MPC with Policy Constraints) is a new planner-based MBRL algorithm that achieves SOTA 🚀performance in various benchmarks. We observed and proved the persistent value overestimation problem in planner-based MBRL with learned value/policy priors: https://t.co/qib8xVz6Dk\" / X","url":"https://x.com/GuanyaShi/status/1889143771432112406"},{"title":"[Literature Review] TD-M(PC)$^2$: Improving Temporal Difference MPC Through Policy Constraint","url":"https://www.themoonlight.io/en/review/td-mpc2-improving-temporal-difference-mpc-through-policy-constraint"},{"title":"GitHub - DarthUtopian/tdmpc_square_public: Official repo for paper \"TD-M(PC)^2: Improving Temporal Difference MPC Through Policy Constraint\" · GitHub","url":"https://github.com/DarthUtopian/tdmpc_square_public"},{"title":"Temporal Difference MPC","url":"https://www.emergentmind.com/topics/temporal-difference-model-predictive-control-td-mpc"}]

I found comprehensive information about TD-M(P
…[truncated 1408 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related-work-audit_20260518T135805",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-18T14:01:30.596779+00:00_

Web search results for query: ""Critiques of World Models" 2025 arxiv"

Links: [{"title":"[2507.05169] Critiques of World Models","url":"https://arxiv.org/abs/2507.05169"},{"title":"Critiques of World Models","url":"https://arxiv.org/pdf/2507.05169"},{"title":"arXiv:2507.05169v1 [cs.LG] 7 Jul 2025 Critiques of World Models","url":"https://arxiv.org/pdf/2507.05169v1"},{"title":"Critiques of World Models - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250705169X/abstract"},{"title":"Critiques of World Models - ArXivIQ","url":"https://arxiviq.substack.com/p/critiques-of-world-models"},{"title":"Internalizing World Models via Self-Play Finetuning for Agentic RL","url":"https://arxiv.org/html/2510.15047v1"},{"title":"Critiques of World Models | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/critiques-world-models"},{"title":"(PDF) Critiques of World Models","url":"https://www.researchgate.net/publication/393478311_Critiques_of_World_Models"},{"title":"Robotics Jul 2025","url":"https://www.arxiv.org/list/cs.RO/2025-07?skip=625&show=50"},{"title":"Paper page - Critiques of World Models","url":"https://huggingface.co/papers/2507.05169"}]

I found the paper "Critiques of World Models" from 2025 on arXiv. Here's what I found:

## Paper Overview

The paper addresses world models as algorithmic surrogates of real-world environments that agents experience and act upon, which has become an emerging topic due to rising needs to develop artificial (general) intelligence agents.

## Main Contributions

The authors offer critiques of several schools of thought on world modeling and argue the primary goal of a world model is to simulate all actionable possibilities of the real world for purposeful reasoning and acting.

Building on these critiques, the authors propose a new architecture for a general-purpose world model based on hierarchical, multi-level, and mixed continuous/discrete representations, and a generative and self-supervision learning fra
…[truncated 690 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related-work-audit_20260518T135805",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-18T14:01:30.596991+00:00_

Web search results for query: "Moderate Actor-Critic expectile loss overestimation bias 2025"

Links: [{"title":"[2504.09929] Moderate Actor-Critic Methods: Controlling Overestimation Bias via Expectile Loss","url":"https://arxiv.org/abs/2504.09929"},{"title":"Moderate Actor-Critic Methods: Controlling Overestimation Bias via Expectile Loss","url":"https://arxiv.org/html/2504.09929v1"},{"title":"[Literature Review] Moderate Actor-Critic Methods: Controlling Overestimation Bias via Expectile Loss","url":"https://www.themoonlight.io/en/review/moderate-actor-critic-methods-controlling-overestimation-bias-via-expectile-loss"},{"title":"Machine Learning Apr 2025","url":"https://www.arxiv.org/list/cs.LG/2025-04?skip=725&show=50"},{"title":"Computer Science Apr 2025","url":"https://www.arxiv.org/list/cs/2025-04?skip=4400&show=2000"},{"title":"Value Improved Actor Critic Algorithms Yaniv Oren","url":"https://arxiv.org/pdf/2406.01423"},{"title":"Value Improved Actor Critic Algorithms","url":"https://arxiv.org/html/2406.1423"},{"title":"A Case for Validation Buffer in Pessimistic Actor-Critic","url":"https://www.ijcai.org/proceedings/2025/0665.pdf"},{"title":"Overestimation, Overfitting, and Plasticity in Actor-Critic: the Bitter Lesson of Reinforcement Learning","url":"https://arxiv.org/html/2403.00514v1"},{"title":"Addressing Function Approximation Error in Actor-Critic Methods","url":"https://proceedings.mlr.press/v80/fujimoto18a/fujimoto18a.pdf"}]

Based on the search results, I found relevant information about "Moderate Actor-Critic Methods: Controlling Overestimation Bias via Expectile Loss."

## Key Findings

Overestimation is a fundamental characteristic of model-free reinforcement learning (MF-RL), arising from the principles of temporal difference learning and the approximation of the Q-function.

### The Proposed Solution

The paper proposes a novel moderate target in the Q-function update, formulated as a convex optimization of an overestimated Q-function and its 
…[truncated 1177 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related-work-audit_20260518T135805",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-18T14:01:30.597171+00:00_

Web search results for query: "VANTA semantic temporal abstraction vision language model ICLR 2025"

Links: [{"title":"SEMANTIC TEMPORAL ABSTRACTION VIA VISION","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/7c8c0db90a14c7a2db9475e52dc343a9-Paper-Conference.pdf"},{"title":"ICLR Poster Semantic Temporal Abstraction via Vision-Language Model Guidance for Efficient Reinforcement Learning","url":"https://iclr.cc/virtual/2025/poster/27665"},{"title":"Semantic Temporal Abstraction via Vision-Language Model Guidance for Efficient Reinforcement Learning","url":"https://proceedings.iclr.cc/paper_files/paper/2025/hash/7c8c0db90a14c7a2db9475e52dc343a9-Abstract-Conference.html"},{"title":"Semantic Temporal Abstraction via Vision-Language Model Guidance for Efficient Reinforcement Learning | OpenReview","url":"https://openreview.net/forum?id=zY37C8d6bS"},{"title":"Semantic Temporal Abstraction via Vision-Language ...","url":"https://iclr.cc/media/iclr-2025/Slides/27665_0737VV2.pdf"},{"title":"dblp: Semantic Temporal Abstraction via Vision-Language Model Guidance for Efficient Reinforcement Learning.","url":"https://dblp.dagstuhl.de/rec/conf/iclr/LiuL0JWZ025.html"},{"title":"Planning with Reasoning using Vision Language World Model","url":"https://arxiv.org/html/2509.02722v1"},{"title":"Published as a conference paper at ICLR 2025 VLAS: VISION-LANGUAGE-ACTION MODEL","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/804a1a9de5787e3597b4bb64e1a48ec3-Paper-Conference.pdf"},{"title":"[2510.09586] Vision Language Models: A Survey of 26K Papers","url":"https://arxiv.org/abs/2510.09586"},{"title":"Towards Comprehensive Reasoning in Vision-Language Models | ICCV 2025","url":"https://wangywust.github.io/iccv-tutorial-reasoning-vlm/"}]

I found relevant information about VANTA (Vision-language model guided Temporal Abstraction) from ICLR 2025. Here's what the search revealed:

## Overview

VanTA (Vision-language model guided Temporal Abstraction) facilitates th
…[truncated 1422 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related-work-audit_20260518T135805",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-18T14:01:30.597516+00:00_

Web search results for query: "plasticity loss deep reinforcement learning 2024 2025 capacity network resets"

Links: [{"title":"Attribution-Based Neuron Utility for Plasticity Restoration in Deep Networks","url":"https://arxiv.org/html/2605.06834"},{"title":"[2411.04832] Plasticity Loss in Deep Reinforcement Learning: A Survey","url":"https://arxiv.org/abs/2411.04832"},{"title":"Loss of plasticity in deep continual learning | Nature","url":"https://www.nature.com/articles/s41586-024-07711-7"},{"title":"Self-Normalized Resets for Plasticity in Continual Learning | OpenReview","url":"https://openreview.net/forum?id=G82uQztzxl"},{"title":"Paper Notes: Loss of Plasticity in Deep Continual Learning – Shawn’s Blog","url":"https://pengxiang-wang.com/posts/paper-notes-loss-of-plasticity-in-deep-continual-learning"},{"title":"A Study of Plasticity Loss in On-Policy Deep Reinforcement Learning","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/ce7984e36d58659211a8dc7d5457cd6f-Paper-Conference.pdf"},{"title":"ICML Poster Mitigating Plasticity Loss in Continual Reinforcement Learning by Reducing Churn","url":"https://icml.cc/virtual/2025/poster/45929"},{"title":"Loss of plasticity in deep continual learning","url":"https://pubmed.ncbi.nlm.nih.gov/39169245/"},{"title":"[2303.07507] Loss of Plasticity in Continual Deep Reinforcement Learning","url":"https://ar5iv.labs.arxiv.org/html/2303.07507"},{"title":"Mitigating Plasticity Loss in Continual Reinforcement Learning by Reducing Churn","url":"https://arxiv.org/html/2506.00592v1"}]

I've completed a web search on plasticity loss in deep reinforcement learning with recent developments from 2024-2025. Here are the key findings:

## Key Concepts and Recent Work

Plasticity refers to a network's ability to adapt to changing data distributions, which is crucial for deep reinforcement learning. Loss of plasticity causes performance plateaus and contributes to scaling failures, overestimation bias, and insufficient explo
…[truncated 1791 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related-work-audit_20260518T135805",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-18T14:01:30.597770+00:00_

Web search results for query: ""adaptive rollout length" model-based reinforcement learning uncertainty 2024 2025"

Links: [{"title":"T2PO: Uncertainty-Guided Exploration Control for Stable Multi-Turn Agentic Reinforcement Learning","url":"https://arxiv.org/html/2605.02178v1"},{"title":"ON ROLLOUTS IN MODEL-BASED REINFORCEMENT ...","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/be7a642a92de108a57e4d50866144d73-Paper-Conference.pdf"},{"title":"On Rollouts in Model-Based Reinforcement Learning","url":"https://arxiv.org/html/2501.16918v1"},{"title":"[PDF] Improving model-based RL with Adaptive Rollout using Uncertainty Estimation | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Improving-model-based-RL-with-Adaptive-Rollout-Nguyen/cf40c34c1020819ffd7c4696904233a379f57b73"},{"title":"ZERO-SHOT MODEL-BASED REINFORCEMENT LEARN","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/5fc1e662bd63c4a70b95088ba5d08cb8-Paper-Conference.pdf"},{"title":"[2501.16918] On Rollouts in Model-Based Reinforcement Learning","url":"https://arxiv.org/abs/2501.16918"},{"title":"Controllable Flow Matching for Online Reinforcement Learning","url":"https://arxiv.org/html/2511.06816v1"},{"title":"Reinforcement Learning Journal 2025 Cover Page","url":"https://rlj.cs.umass.edu/2025/papers/RLJ_RLC_2025_136.pdf"},{"title":"Scalable and reliable multi-agent reinforcement learning for traffic assignment - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S2772424725000654"},{"title":"Efficient Reinforcement Learning for LLM Reasoning via ...","url":"https://www.arxiv.org/pdf/2506.02177"}]

The search has returned several highly relevant results on adaptive rollout length in model-based reinforcement learning with uncertainty. Here are the key findings:

## Key Papers and Findings

### Infoprop: On Rollouts in Model-Based Reinforcement Learning

Infoprop is a model-based rollout mechanism that separates aleatoric from epistemic model uncer
…[truncated 1655 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related-work-audit_20260518T135805",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-18T14:01:30.598003+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"overestimation overfitting plasticity actor-critic bitter lesson\" reinforcement learning 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related-work-audit_20260518T135805",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"overestimation overfitting plasticity actor-critic bitter lesson\" reinforcement learning 2024"
  }
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-18T14:01:30.598277+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Diffusion World Model\" offline reinforcement learning step-by-step rollout 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related-work-audit_20260518T135805",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Diffusion World Model\" offline reinforcement learning step-by-step rollout 2024"
  }
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-18T14:01:30.598433+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"SPlaTES\" stable planning temporally extended skills reinforcement learning 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related-work-audit_20260518T135805",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"SPlaTES\" stable planning temporally extended skills reinforcement learning 2025"
  }
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-18T14:01:30.598634+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"learning world models hierarchical temporal abstractions probabilistic\" 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related-work-audit_20260518T135805",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"learning world models hierarchical temporal abstractions probabilistic\" 2024"
  }
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-18T14:01:30.598858+00:00_

Web search results for query: ""overestimation overfitting plasticity actor-critic bitter lesson" reinforcement learning 2024"

Links: [{"title":"[2403.00514] Overestimation, Overfitting, and Plasticity in Actor-Critic: the Bitter Lesson of Reinforcement Learning","url":"https://arxiv.org/abs/2403.00514"},{"title":"Overestimation, Overfitting, and Plasticity in Actor-Critic: the Bitter Lesson of Reinforcement Learning","url":"https://proceedings.mlr.press/v235/nauman24a.html"},{"title":"[PDF] Overestimation, Overfitting, and Plasticity in Actor-Critic: the Bitter Lesson of Reinforcement Learning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Overestimation,-Overfitting,-and-Plasticity-in-the-Nauman-Bortkiewicz/dcf39ce4ea7c1d073dcd0dbb131a0b90a4bd2977"},{"title":"Overestimation, Overfitting, and Plasticity in Actor-Critic: the Bitter Lesson of Reinforcement Learning | OpenReview","url":"https://openreview.net/forum?id=5vZzmCeTYu"},{"title":"Overestimation, Overfitting, and Plasticity in Actor-Critic: the Bitter Lesson of Reinforcement Learning","url":"https://arxiv.org/html/2403.00514v2"},{"title":"[2403.00514v2] Overestimation, Overfitting, and Plasticity in Actor-Critic: the Bitter Lesson of Reinforcement Learning","url":"https://arxiv.org/abs/2403.00514v2"},{"title":"Overestimation, Overfitting, and Plasticity in Actor-Critic: the Bitter Lesson of Reinforcement Learning | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/overestimation-overfitting-plasticity-actor-critic-bitter-lesson"},{"title":"Overestimation, overfitting, and plasticity in actor-critic | Proceedings of the 41st International Conference on Machine Learning","url":"https://dl.acm.org/doi/10.5555/3692070.3693586"},{"title":"ICML Poster Overestimation, Overfitting, and Plasticity in Actor-Critic: the Bitter Lesson of Reinforcement Learning","url":"https://icml.cc/virtual/2024/poster/34956"},{"title":"Overestimation, Overfitting, and Plasticity in Actor-Critic
…[truncated 2030 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related-work-audit_20260518T135805",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-18T14:01:30.599057+00:00_

Web search results for query: ""SPlaTES" stable planning temporally extended skills reinforcement learning 2025"

Links: [{"title":"Reinforcement Learning Journal 2025 Cover Page","url":"https://rlj.cs.umass.edu/2025/papers/RLJ_RLC_2025_136.pdf"},{"title":"Learning Temporally Extended Skills in Continuous Domains as Symbolic Actions for Planning | seads","url":"https://seads.is.tue.mpg.de/"},{"title":"[2207.05018] Learning Temporally Extended Skills in Continuous Domains as Symbolic Actions for Planning","url":"https://arxiv.org/abs/2207.05018"},{"title":"Learning Temporally Extended Skills in Continuous Domains as Symbolic Actions for Planning | OpenReview","url":"https://openreview.net/forum?id=t-IO7wCaNgH"},{"title":"Temporally extended successor feature neural episodic control | Scientific Reports","url":"https://www.nature.com/articles/s41598-024-65687-w"},{"title":"LLMs augmented hierarchical reinforcement learning with action primitives for long-horizon manipulation tasks | Scientific Reports","url":"https://www.nature.com/articles/s41598-025-20653-y"},{"title":"Multi-Turn Reinforcement Learning","url":"https://www.emergentmind.com/topics/multi-turn-reinforcement-learning-mt-rl"},{"title":"Published as a conference paper at ICLR 2025","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/7c8c0db90a14c7a2db9475e52dc343a9-Paper-Conference.pdf"},{"title":"Learning Temporally Extended Skills in Continuous Domains ...","url":"https://proceedings.mlr.press/v205/achterhold23a/achterhold23a.pdf"},{"title":"Learning Temporally Extended Skills in Continuous Domains as Symbolic Actions for Planning | Request PDF","url":"https://www.researchgate.net/publication/361923815_Learning_Temporally_Extended_Skills_in_Continuous_Domains_as_Symbolic_Actions_for_Planning?_tp=eyJjb250ZXh0Ijp7InBhZ2UiOiJzY2llbnRpZmljQ29udHJpYnV0aW9ucyIsInByZXZpb3VzUGFnZSI6bnVsbH19"}]

I found information about SPlaTES! Based on the search results, here's what I found:

## SPlaTES Overview

S
…[truncated 1369 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related-work-audit_20260518T135805",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-18T14:01:30.599251+00:00_

Web search results for query: ""Diffusion World Model" offline reinforcement learning step-by-step rollout 2024"

Links: [{"title":"[2402.03570] Diffusion World Model: Future Modeling Beyond Step-by-Step Rollout for Offline Reinforcement Learning","url":"https://arxiv.org/abs/2402.03570"},{"title":"Diffusion World Model: Future Modeling Beyond Step-by-Step Rollout for Offline Reinforcement Learning - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv240203570D/abstract"},{"title":"Diffusion World Model: Future Modeling Beyond Step-by-Step Rollout for Offline Reinforcement Learning - DEV Community","url":"https://dev.to/aimodels-fyi/diffusion-world-model-future-modeling-beyond-step-by-step-rollout-for-offline-reinforcement-learning-o66"},{"title":"Diffusion World Model: Future Modeling Beyond Step-by-Step Rollout for Offline Reinforcement Learning","url":"https://arxiv.org/html/2402.03570v3"},{"title":"Diffusion World Model: Future Modeling Beyond Step-by-Step Rollout for Offline Reinforcement Learning | alphaXiv","url":"https://www.alphaxiv.org/overview/2402.03570v4"},{"title":"World model-driven process industry operations: An offline reinforcement learning solution based on conditional diffusion - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S0166361526000096"},{"title":"Diffusion World Model: Future Modeling Beyond Step-by-Step Rollout for Offline Reinforcement Learning | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/diffusion-world-model-future-modeling-beyond-step"},{"title":"[Literature Review] Diffusion World Model: Future Modeling Beyond Step-by-Step Rollout for Offline Reinforcement Learning","url":"https://www.themoonlight.io/en/review/diffusion-world-model-future-modeling-beyond-step-by-step-rollout-for-offline-reinforcement-learning"},{"title":"RLJ | RLC 2024 Policy-Guided Diffusion Matthew T. Jackson∗ Michael T. Matthews","url":"https://rlj.cs.umass.edu/2024/papers/RLJ_RLC_2024_233.pdf"},{"title"
…[truncated 1882 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related-work-audit_20260518T135805",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-18T14:01:30.599440+00:00_

Web search results for query: ""learning world models hierarchical temporal abstractions probabilistic" 2024"

Links: [{"title":"[2404.16078] Learning World Models With Hierarchical Temporal Abstractions: A Probabilistic Perspective","url":"https://arxiv.org/abs/2404.16078"},{"title":"ICLR Poster Learning Hierarchical World Models with Adaptive Temporal Abstractions from Discrete Latent Dynamics","url":"https://iclr.cc/virtual/2024/poster/18558"},{"title":"Learning Hierarchical World Models with Adaptive Temporal Abstractions from Discrete Latent Dynamics | OpenReview","url":"https://openreview.net/forum?id=TjCDNssXKU"},{"title":"Published as a conference paper at ICLR 2024 LEARNING HIERARCHICAL WORLD MODELS","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/13b45b44e26c353c64cba9529bf4724f-Paper-Conference.pdf"},{"title":"Exploring the limits of hierarchical world models in reinforcement learning | Scientific Reports","url":"https://www.nature.com/articles/s41598-024-76719-w"},{"title":"GitHub - CognitiveModeling/THICK · GitHub","url":"https://github.com/CognitiveModeling/THICK"},{"title":"Learning Hierarchical World Models with Adaptive Temporal Abstractions from Discrete Latent Dynamics | Autonomous Learning – MPI-IS","url":"https://is.mpg.de/al/publications/gumbsch2024-thickworldmodels"},{"title":"Hierarchical Model-Based Reinforcement Learning with Temporal Abstractions | Open Research Commons","url":"https://bcommons.berkeley.edu/hierarchical-model-based-reinforcement-learning-temporal-abstractions"},{"title":"Exploring the limits of hierarchical world models in reinforcement learning - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC11538428/"},{"title":"GitHub - GuochenZhou/World-Model: A paper list of world model","url":"https://github.com/GuochenZhou/World-Model"}]

I found several relevant results for your search on learning world models with hierarchical temporal abstractions and probabilistic approaches in 2024. Here are the key findin
…[truncated 1579 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related-work-audit_20260518T135805",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 53 · 2026-05-18T14:01:30.599723+00:00_

搜索完成。现在编译分析报告。

---

## 已引用论文清单

**Temporal Abstraction 段落 (14篇):**
- Sutton et al. 1999 (Options framework)
- Sharma et al. 2017 (FiGAR)
- Biedenkapp et al. 2021 (TempoRL)
- Lakshminarayanan et al. 2017 (Dynamic action repetition)
- Hafner et al. 2020/2021/2023/2025 (DreamerV1/V2/V3/V4)
- Micheli et al. 2023 (IRIS)
- Robine et al. 2023 (TWM)
- Gumbsch et al. 2024 (THICK)
- Mattes et al. 2024 (Hieros)
- Li et al. 2025 (LS-Imagine)
- Shaj et al. 2023 (MTS3)

**TAWM 段落 (2篇):**
- Nhu et al. 2025 (TAWM)
- Hansen et al. 2024 (TD-MPC2)

**Value Overestimation 段落 (10篇):**
- Thrun & Schwartz 1993, van Hasselt et al. 2016 (Double Q), Fujimoto et al. 2018 (TD3), Haarnoja et al. 2018 (SAC), Chen et al. 2021 (REDQ)
- Janner et al. 2019 (MBPO), Yu et al. 2020 (MOPO), Lu et al. 2018 (Non-delusional)
- Tallec et al. 2019 (Time discretization)

**Model Fidelity 段落 (5篇):**
- Lambert et al. 2020 (Objective mismatch), Asadi et al. 2019, Lambert et al. 2022 (Compounding error)
- Ma et al. 2024 (HarmonyDream)
- Palenicek et al. 2025, Frauenknecht et al. 2025 (Rollout diminishing returns)

**Network Capacity 段落 (5篇):**
- Nikishin et al. 2022 (Primacy bias), Lyle et al. 2022 (Capacity loss), Nikishin et al. 2023 (Plasticity injection)
- Henderson et al. 2018, Engstrom et al. 2020, Andrychowicz et al. 2021

---

## 搜索发现的相关但未引用论文

### 直接相关（建议添加）

**1. Nauman et al., "Overestimation, Overfitting, and Plasticity in Actor-Critic: the Bitter Lesson of Reinforcement Learning" (ICML 2024)**
- 相关性: **直接相关**
- 与本文关系: 系统性研究 overestimation、overfitting、plasticity loss 三者的耦合关系。对 60+ off-policy agent 进行消融实验，发现适当 regularization 同时缓解三个问题。这与本文将 CIVO（value overestimation）和 seed-dependent divergence（plasticity/capacity）联系起来的分析高度吻合。审稿人极有可能要求引用此文。
- 建议添加位置: **Value Overestimation 段落**末尾或 **Network Capacity 段落**，作为连接 overestimation 与 plasticity 的桥梁文献。

**2. TD-M(PC)² (2025, arXiv 2502.03550)**
- 相关性: **直接相关**
- 与本文关系: 发现并证明 TD-MPC2 中 planner 和 learned policy prior 之间的 structural policy mismatch 导致持续性 value overestimation。由于 TAWM 基于 TD-MPC2，而本文的核心对比就是 TAWM（MPC re-planning）vs DreamerV3（imagination loop）在 overestimation 上的差异，该工作提供了 TD-MPC2 一侧 overestimation 机制的详细分析，有力支撑本文的 "MPC re-plans from real states so errors don't compound into critic" 的论点。
- 建议添加位置: **TAWM 段落**，在讨论 TAWM 与 DreamerV3 架构差异时引用。

**3. "A Study of Plasticity Loss in On-Policy Deep Reinforcement Learning" (NeurIPS 2024)**
- 相关性: **直接相关**
- 与本文关系: 已引用 Nikishin 2022/2023 和 Lyle 2022，但缺少 2024 NeurIPS 上的最新 plasticity 研究。该文将 plasticity loss 研究从 off-policy 扩展到 on-policy 场景，提供更全面的理论视角。
- 建议添加位置: **Network Capacity 段落**，与 Nikishin 2022/2023 并列。

**4. "Mitigating Plasticity Loss in Continual Reinforcement Learning by Reducing Churn" (ICML 2025)**
- 相关性: **直接相关**
- 与本文关系: 通过 Neural Tangent Kernel (NTK) 矩阵的 rank 下降解释 plasticity loss 的机制，提出 churn 作为 plasticity loss 的直接度量。为本文的 seed-dependent CIVO 现象提供了更精细的机制解释。
- 建议添加位置: **Network Capacity 段落**。

### 间接相关（可考虑添加）

**5. MuDreamer (Burchi & Timofte, arXiv 2024)**
- 相关性: 间接相关
- 与本文关系: 移除 DreamerV3 的 pixel reconstruction loss，改用 value function + action prediction。与本文 gradient decomposition 中 observation decoder channel 只占 16-22% 但承载关键 Δt spatial information 的发现形成有趣对照：如果去掉 reconstruction，Δt conditioning 的信息传播路径会完全不同。
- 建议添加位置: **Temporal Abstraction 段落**，作为 DreamerV3 变体之一提及。

**6. "Learning World Models With Hierarchical Temporal Abstractions: A Probabilistic Perspective" (arXiv 2404.16078)**
- 相关性: 间接相关
- 与本文关系: 从概率角度形式化分层时间抽象 world model，提出 Hidden-Parameter SSMs 和 Multi-Time Scale SSMs。已引用 THICK 和 MTS3，此文是同方向的理论补充。
- 建议添加位置: **Temporal Abstraction 段落**，与 THICK 和 MTS3 并列。

**7. Diffusion World Model (DWM, arXiv 2024)**
- 相关性: 间接相关
- 与本文关系: 用 diffusion model 一次性预测多步未来状态，回避 step-by-step rollout 的 compounding error。与本文 compounding error 段落讨论的问题直接相关，但方法路线完全不同（offline RL）。
- 建议添加位置: **Model Fidelity 段落**，可一句话提及作为非自回归方案对比。

**8. MACURA / Lenz et al. 2025 "Trust the Model Where It Trusts Itself"**
- 相关性: 间接相关
- 与本文关系: 基于模型不确定性自适应调整 rollout 长度。已在 bib 中（lenz2025macura），但未在 related work 引用。与 Frauenknecht et al. 2025 主题接近。
- 建议添加位置: **Model Fidelity 段落**，与 Frauenknecht et al. 并列。

---

## TAWM 引用验证

当前 bib 条目：
```bibtex
@inproceedings{nhu2025tawm,
  title = {Time-Aware World Model for Adaptive Prediction and Control},
  author = {Nhu, A.N and Son, S and Lin, M.C},
  year = {2025},
  booktitle = {International Conference on Machine Learning},
  eprint = {2506.08441},
  archivePrefix = {arXiv},
}
```

验证结果：
- **Title**: 正确 ✓
- **Authors**: Anh N. Nhu, Sanghyun Son, Ming C. Lin (University of Maryland) ✓
- **Venue**: ICML 2025 ✓ (已通过 OpenReview 和 ICML 2025 schedule 确认)
- **arXiv ID**: 2506.08441 ✓
- **Year**: 2025 ✓

TAWM 引用信息全部准确，无需修改。

---

## 总结建议

**必须添加（2篇）：**
1. **Nauman et al. (ICML 2024)** — 审稿人最可能指出的遗漏。该文是 2024 年 overestimation + plasticity 交叉研究的标杆，与本文横跨 Value Overestimation 和 Network Capacity 两个段落的主题高度重合。
2. **TD-M(PC)² (2025)** — 本文花了整段讨论 TAWM/TD-MPC2 vs DreamerV3 的架构对比，引用在 TD-MPC2 上发现 overestimation 问题的最新工作能强化论证。

**强烈建议添加（2篇）：**
3. **NeurIPS 2024 plasticity study** — 补全 plasticity 文献的时效性
4. **ICML 2025 churn-based plasticity** — 最新 plasticity 机制研究

**可选添加（4篇）：**
5-8. MuDreamer、Probabilistic hierarchical WM、DWM、MACURA — 根据页数空间决定

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_related-work-audit_20260518T135805"
}
```

</details>

---
