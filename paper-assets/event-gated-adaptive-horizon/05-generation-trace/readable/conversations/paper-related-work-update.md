# paper related work update

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 33
- **Recorded user turns:** 0
- **Tool calls:** 16
- **Original source:** `logs/chats/worker_paper_related-work-update_20260518T142443.jsonl`
- **Structured JSON:** [`62b42bdd0c3e0d0bffd1.json`](../../sessions/62/62b42bdd0c3e0d0bffd1.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

33 recorded events

### Tool call

_source line 1 · 2026-05-18T14:27:42.166364+00:00_

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
  "session": "worker_paper_related-work-update_20260518T142443",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-18T14:27:42.166777+00:00_

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
  "session": "worker_paper_related-work-update_20260518T142443",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-18T14:27:42.167014+00:00_

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
  "session": "worker_paper_related-work-update_20260518T142443",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/references.bib"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-18T14:27:42.167343+00:00_

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
  "session": "worker_paper_related-work-update_20260518T142443",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-18T14:27:42.167556+00:00_

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
  "session": "worker_paper_related-work-update_20260518T142443",
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

_source line 6 · 2026-05-18T14:27:42.167692+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_related-work-update_20260518T142443",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-18T14:27:42.167836+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Nauman \"Overestimation, Overfitting, and Plasticity in Actor-Critic\" ICML 2024 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_related-work-update_20260518T142443",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Nauman \"Overestimation, Overfitting, and Plasticity in Actor-Critic\" ICML 2024 arXiv"
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-18T14:27:42.168018+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arXiv 2502.03550 TD-MPC2 value overestimation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_related-work-update_20260518T142443",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arXiv 2502.03550 TD-MPC2 value overestimation"
  }
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-18T14:27:42.168146+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"A Study of Plasticity Loss in On-Policy Deep Reinforcement Learning\" NeurIPS 2024 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_related-work-update_20260518T142443",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"A Study of Plasticity Loss in On-Policy Deep Reinforcement Learning\" NeurIPS 2024 arXiv"
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-18T14:27:42.168264+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Mitigating Plasticity Loss in Continual Reinforcement Learning by Reducing Churn\" ICML 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_related-work-update_20260518T142443",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Mitigating Plasticity Loss in Continual Reinforcement Learning by Reducing Churn\" ICML 2025"
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-18T14:27:42.168422+00:00_

Web search results for query: "Nauman "Overestimation, Overfitting, and Plasticity in Actor-Critic" ICML 2024 arXiv"

Links: [{"title":"[2403.00514] Overestimation, Overfitting, and Plasticity in Actor-Critic: the Bitter Lesson of Reinforcement Learning","url":"https://arxiv.org/abs/2403.00514"},{"title":"Overestimation, overfitting, and plasticity in actor-critic | Proceedings of the 41st International Conference on Machine Learning","url":"https://dl.acm.org/doi/10.5555/3692070.3693586"},{"title":"[2403.00514v2] Overestimation, Overfitting, and Plasticity in Actor-Critic: the Bitter Lesson of Reinforcement Learning","url":"https://arxiv.org/abs/2403.00514v2"},{"title":"[PDF] Overestimation, Overfitting, and Plasticity in Actor-Critic: the Bitter Lesson of Reinforcement Learning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Overestimation,-Overfitting,-and-Plasticity-in-the-Nauman-Bortkiewicz/dcf39ce4ea7c1d073dcd0dbb131a0b90a4bd2977"},{"title":"Overestimation, Overfitting, and Plasticity in Actor-Critic: the Bitter Lesson of Reinforcement Learning","url":"https://arxiv.org/html/2403.00514v1"},{"title":"Overestimation, Overfitting, and Plasticity in Actor-Critic: the Bitter Lesson of Reinforcement Learning | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/overestimation-overfitting-plasticity-actor-critic-bitter-lesson"},{"title":"Overestimation, Overfitting, and Plasticity in Actor-Critic: the Bitter Lesson of Reinforcement Learning | OpenReview","url":"https://openreview.net/forum?id=5vZzmCeTYu"},{"title":"Overestimation, Overfitting, and Plasticity in Actor-Critic: the Bitter Lesson of Reinforcement Learning","url":"https://proceedings.mlr.press/v235/nauman24a.html"},{"title":"Machine Learning Mar 2024","url":"https://web3.arxiv.org/list/cs.LG/2024-03?skip=10&show=10"},{"title":"ICML Poster Overestimation, Overfitting, and Plasticity in Actor-Critic: the Bitter Lesson of Reinforcement Learning","url":"https://icml.cc/vir
…[truncated 1741 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_related-work-update_20260518T142443",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-18T14:27:42.168607+00:00_

Web search results for query: ""A Study of Plasticity Loss in On-Policy Deep Reinforcement Learning" NeurIPS 2024 arXiv"

Links: [{"title":"A Study of Plasticity Loss in On-Policy Deep Reinforcement Learning","url":"https://proceedings.neurips.cc/paper_files/paper/2024/hash/ce7984e36d58659211a8dc7d5457cd6f-Abstract-Conference.html"},{"title":"NeurIPS Poster A Study of Plasticity Loss in On-Policy Deep Reinforcement Learning","url":"https://neurips.cc/virtual/2024/poster/95486"},{"title":"A Study of Plasticity Loss in On-Policy Deep Reinforcement Learning | OpenReview","url":"https://openreview.net/forum?id=MsUf8kpKTF"},{"title":"A Study of Plasticity Loss in On-Policy Deep Reinforcement Learning","url":"https://papers.nips.cc/paper_files/paper/2024/hash/ce7984e36d58659211a8dc7d5457cd6f-Abstract-Conference.html"},{"title":"[2405.19153] A Study of Plasticity Loss in On-Policy Deep Reinforcement Learning","url":"https://arxiv.org/abs/2405.19153"},{"title":"A Study of Plasticity Loss in On-Policy Deep Reinforcement Learning - Microsoft Research","url":"https://www.microsoft.com/en-us/research/publication/a-study-of-plasticity-loss-in-on-policy-deep-reinforcement-learning/"},{"title":"[Quick Review] A Study of Plasticity Loss in On-Policy Deep Reinforcement Learning","url":"https://liner.com/review/a-study-of-plasticity-loss-in-onpolicy-deep-reinforcement-learning"},{"title":"A Study of Plasticity Loss in On-Policy Deep Reinforcement Learning - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv240519153J/abstract"},{"title":"A Study of Plasticity Loss in On-Policy Deep Reinforcement Learning","url":"https://arxiv.org/html/2405.19153v1"},{"title":"A Study of Plasticity Loss in On-Policy Deep Reinforcement Learning | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/study-plasticity-loss-policy-deep-reinforcement-learning"}]

I found the paper! Here's what I found about "A Study of Plasticity Loss in On-Policy Deep Reinforcement Learning":

## Pa
…[truncated 1173 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_related-work-update_20260518T142443",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-18T14:27:42.168786+00:00_

Web search results for query: "arXiv 2502.03550 TD-MPC2 value overestimation"

Links: [{"title":"[2502.03550] TD-M(PC)$^2$: Improving Temporal Difference MPC Through Policy Constraint","url":"https://arxiv.org/abs/2502.03550"},{"title":"TD-M(PC)2: Improving Temporal Difference MPC Through Policy Constraint","url":"https://arxiv.org/html/2502.03550"},{"title":"arXiv:2502.03550v1 [cs.LG] 5 Feb 2025","url":"https://arxiv.org/pdf/2502.03550"},{"title":"Improving Temporal Difference MPC Through Policy Constraint","url":"https://darthutopian.github.io/tdmpc_square/"},{"title":"[2502.03550v1] TD-M(PC)$^2$: Improving Temporal Difference MPC Through Policy Constraint","url":"http://arxiv.org/abs/2502.03550v1"},{"title":"TD-M(PC)2: Improving Temporal Difference MPC Through Policy Constraint","url":"https://darthutopian.github.io/tdmpc_square/static/pdfs/paper.pdf"},{"title":"Bigger, Regularized, Optimistic: scaling for compute and sample-efficient continuous control","url":"https://arxiv.org/html/2405.16158v3"},{"title":"TD-MPC2: Scalable Model-Based Control","url":"https://www.emergentmind.com/topics/td-mpc2"},{"title":"TD-MPC2: Scalable, Robust World Models for Continuous Control | OpenReview","url":"https://openreview.net/forum?id=Oxh5CstDJU"},{"title":"[2310.16828] TD-MPC2: Scalable, Robust World Models for Continuous Control","url":"https://arxiv.org/abs/2310.16828"}]

Based on the search results, here's what arXiv paper 2502.03550 is about:

## Overview

The paper is titled "TD-M(PC)²: Improving Temporal Difference MPC Through Policy Constraint" and was published on February 5, 2025.

## The Value Overestimation Problem

The paper discovers that existing methods that rely on standard SAC-style policy iteration for value learning, directly using data generated by the planner, often result in persistent value overestimation. While overestimation bias is within an acceptable range in low-dimensional tasks, it is incredibly large in high-dimensional tasks and does not tend 
…[truncated 1204 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_related-work-update_20260518T142443",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-18T14:27:42.168994+00:00_

Web search results for query: ""Mitigating Plasticity Loss in Continual Reinforcement Learning by Reducing Churn" ICML 2025"

Links: [{"title":"ICML Poster Mitigating Plasticity Loss in Continual Reinforcement Learning by Reducing Churn","url":"https://icml.cc/virtual/2025/poster/45929"},{"title":"Mitigating Plasticity Loss in Continual Reinforcement Learning by Reducing Churn | OpenReview","url":"https://openreview.net/forum?id=EkoFXfSauv"},{"title":"[2506.00592] Mitigating Plasticity Loss in Continual Reinforcement Learning by Reducing Churn","url":"https://arxiv.org/abs/2506.00592"},{"title":"Mitigating Plasticity Loss in Continual Reinforcement Learning by Reducing Churn","url":"https://arxiv.org/html/2506.00592v1"},{"title":"Mitigating Plasticity Loss in Continual Reinforcement Learning by Reducing Churn","url":"https://proceedings.mlr.press/v267/tang25g.html"},{"title":"GitHub - bluecontra/C-CHAIN: The code implementation of Continual Churn Approximation Reduction (C-CHAIN) for ICML 2025 paper \"Mitigating Plasticity Loss in Continual RL by Reducing Churn\"","url":"https://github.com/bluecontra/C-CHAIN"},{"title":"[2506.00592v1] Mitigating Plasticity Loss in Continual Reinforcement Learning by Reducing Churn","url":"https://arxiv.org/abs/2506.00592v1"},{"title":"Mitigating Plasticity Loss in Continual Reinforcement Learning by Reducing Churn | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/mitigating-plasticity-loss-continual-reinforcement-learning-by"},{"title":"GitHub - datake/Papers-Of-Continual-RL: Related papers for Continual Reinforcement Learning. · GitHub","url":"https://github.com/datake/Papers-Of-Continual-RL"},{"title":"GitHub - xialeiliu/Awesome-Incremental-Learning: Awesome Incremental Learning · GitHub","url":"https://github.com/xialeiliu/Awesome-Incremental-Learning"}]

Based on the search results, here's information about the paper "Mitigating Plasticity Loss in Continual Reinforcement Learning by Reducing Churn" from I
…[truncated 1378 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_related-work-update_20260518T142443",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-18T14:27:42.169178+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arXiv 2405.19153 authors \"plasticity loss\" on-policy"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_related-work-update_20260518T142443",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arXiv 2405.19153 authors \"plasticity loss\" on-policy"
  }
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-18T14:27:42.169306+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arXiv 2502.03550 \"TD-M(PC)2\" authors full list"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_related-work-update_20260518T142443",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arXiv 2502.03550 \"TD-M(PC)2\" authors full list"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-18T14:27:42.169452+00:00_

Web search results for query: "arXiv 2502.03550 "TD-M(PC)2" authors full list"

Links: [{"title":"[2502.03550] TD-M(PC)$^2$: Improving Temporal Difference MPC Through Policy Constraint","url":"https://arxiv.org/abs/2502.03550"},{"title":"TD-M(PC)2: Improving Temporal Difference MPC Through Policy Constraint","url":"https://arxiv.org/html/2502.03550"},{"title":"Computer Science","url":"https://www.arxiv.org/list/cs/recent?skip=356&show=2000"},{"title":"TD-M(PC)2: Improving Temporal Difference MPC Through Policy Constraint","url":"https://darthutopian.github.io/tdmpc_square/static/pdfs/paper.pdf"},{"title":"TD-MPC2: Scalable, Robust World Models for Continuous Control | OpenReview","url":"https://openreview.net/forum?id=Oxh5CstDJU"},{"title":"[2310.16828] TD-MPC2: Scalable, Robust World Models for Continuous Control","url":"https://arxiv.org/abs/2310.16828"},{"title":"TD-GRPC: Temporal Difference Learning with Group ...","url":"https://arxiv.org/pdf/2505.13549"},{"title":"[PDF] TD-MPC2: Scalable, Robust World Models for Continuous Control | Semantic Scholar","url":"https://www.semanticscholar.org/paper/TD-MPC2:-Scalable,-Robust-World-Models-for-Control-Hansen-Su/8eeccf1033fd759c868b29ccb6aa70f5ffd1887c"},{"title":"TD-MPC2: Scalable, Robust World Models for Continuous Control","url":"https://arxiv.org/html/2310.16828v2"},{"title":"GitHub - iszhanjiawei/flow_matching_arxiv_daily · GitHub","url":"https://github.com/iszhanjiawei/flow_matching_arxiv_daily"}]

The authors of arXiv paper 2502.03550 "TD-M(PC)²: Improving Temporal Difference MPC Through Policy Constraint" are: Haotian Lin, Pengcheng Wang, Jeff Schneider, and Guanya Shi.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_related-work-update_20260518T142443",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-18T14:27:42.169611+00:00_

Web search results for query: "arXiv 2405.19153 authors "plasticity loss" on-policy"

Links: [{"title":"[2405.19153] A Study of Plasticity Loss in On-Policy Deep Reinforcement Learning","url":"https://arxiv.org/abs/2405.19153"},{"title":"A Study of Plasticity Loss in On-Policy Deep Reinforcement Learning","url":"https://arxiv.org/html/2405.19153"},{"title":"LLMs as verification oracles for Solidity","url":"https://arxiv.org/html/2509.19153"},{"title":"Spatiotemporal Variations of Temperature in Jupiter’s Upper Atmosphere","url":"https://arxiv.org/html/2503.19153"},{"title":"A tweezer array with 6100 highly coherent atomic qubits","url":"https://inspirehep.net/literature/2770085"},{"title":"Rearrangement of individual atoms in a 2000-site optical- ...","url":"https://inspirehep.net/literature/2791714"},{"title":"Arxiv","url":"https://arxiv.org/pdf/2405.13356"},{"title":"Desiree Lim (0009-0008-1256-3499)","url":"https://orcid.org/0009-0008-1256-3499"},{"title":"[2305.19153] FERN: Leveraging Graph Attention Networks for Failure Evaluation and Robust Network Design","url":"https://arxiv.org/abs/2305.19153"},{"title":"Untitled Document","url":"https://arxiv.org/html/2604.19153"}]

Based on the search results, the authors of arXiv paper 2405.19153 are Arthur Juliani and Jordan T. Ash. 

The paper is titled "A Study of Plasticity Loss in On-Policy Deep Reinforcement Learning". Plasticity loss is a problem wherein a neural network trained in an online fashion displays a degraded ability to fit new tasks. While plasticity loss has received less attention in the on-policy deep RL setting, the paper performs an extensive set of experiments examining plasticity loss and a variety of mitigation methods in on-policy deep RL.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_related-work-update_20260518T142443",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-18T14:27:42.169868+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/related_work.tex",
  "old_string": "and achieves consistent gains. The critical distinction is architectural:",
  "new_string": "and achieves consistent gains. \\citet{lin2025tdmpcsquare} trace persistent value overestimation in TD-MPC2 to structural policy mismatch, a complementary diagnosis to our identification of the imagination-based feedback loop as the critical factor. The critical distinction is architectural:"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_related-work-update_20260518T142443",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/related_work.tex",
    "old_string": "and achieves consistent gains. The critical distinction is architectural:",
    "new_string": "and achieves consistent gains. \\citet{lin2025tdmpcsquare} trace persistent value overestimation in TD-MPC2 to structural policy mismatch, a complementary diagnosis to our identification of the imagination-based feedback loop as the critical factor. The critical distinction is architectural:"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-18T14:27:42.170077+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/related_work.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_related-work-update_20260518T142443",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-18T14:27:42.170221+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/related_work.tex",
  "old_string": "from policy-class constraints. Our CIVO is mechanistically distinct:",
  "new_string": "from policy-class constraints. \\citet{nauman2024overestimation} show that overestimation, overfitting, and plasticity loss are coupled phenomena in actor-critic methods; CIVO can be understood as a model-induced instance within this broader framework. Our CIVO is mechanistically distinct:"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_related-work-update_20260518T142443",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/related_work.tex",
    "old_string": "from policy-class constraints. Our CIVO is mechanistically distinct:",
    "new_string": "from policy-class constraints. \\citet{nauman2024overestimation} show that overestimation, overfitting, and plasticity loss are coupled phenomena in actor-critic methods; CIVO can be understood as a model-induced instance within this broader framework. Our CIVO is mechanistically distinct:"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-18T14:27:42.170378+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/related_work.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_related-work-update_20260518T142443",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-18T14:27:42.170502+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/related_work.tex",
  "old_string": "(\\S\\ref{sec:seed_divergence}). Our factorial diagnostic approach",
  "new_string": "(\\S\\ref{sec:seed_divergence}). \\citet{juliani2024plasticity} extend this analysis to on-policy settings and find that regenerative interventions are the most reliable mitigation, while \\citet{tang2025churn} link plasticity loss to value churn through NTK rank collapse. \\citet{nauman2024overestimation} further demonstrate that overestimation and plasticity loss are coupled, consistent with our observation that seed-dependent CIVO outcomes correlate with critic capacity. Our factorial diagnostic approach"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_related-work-update_20260518T142443",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/related_work.tex",
    "old_string": "(\\S\\ref{sec:seed_divergence}). Our factorial diagnostic approach",
    "new_string": "(\\S\\ref{sec:seed_divergence}). \\citet{juliani2024plasticity} extend this analysis to on-policy settings and find that regenerative interventions are the most reliable mitigation, while \\citet{tang2025churn} link plasticity loss to value churn through NTK rank collapse. \\citet{nauman2024overestimation} further demonstrate that overestimation and plasticity loss are coupled, consistent with our observation that seed-dependent CIVO outcomes correlate with critic capacity. Our factorial diagnostic approach"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-18T14:27:42.170651+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/related_work.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_related-work-update_20260518T142443",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-18T14:27:42.170791+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/references.bib",
  "old_string": "@article{lenz2025macura,\n  title = {Trust the Model Where It Trusts Itself -- Model-Based Actor-Critic with Uncertainty-Aware Rollout Adaption},\n  author = {Lenz, S and et, al},\n  year = {2025},\n  journal = {arXiv preprint arXiv:2405.19014},\n  eprint = {2405.19014},\n  archivePrefix = {arXiv},\n}",
  "new_string": "@article{lenz2025macura,\n  title = {Trust the Model Where It Trusts Itself -- Model-Based Actor-Critic with Uncertainty-Aware Rollout Adaption},\n  author = {Lenz, S and et, al},\n  year = {2025},\n  journal = {arXiv preprint arXiv:2405.19014},\n  eprint = {2405.19014},\n  archivePrefix = {arXiv},\n}\n\n@inproceedings{nauman2024overestimation,\n  title = {Overestimation, Overfitting, and Plasticity in Actor-Critic: the Bitter Lesson of Reinforcement Learning},\n  author = {Nauman, Michal and Bortkiewicz, Micha{\\l} and Mi{\\l}o{\\'s}, Piotr and Trzcinski, Tomasz and Ostaszewski, Mateusz and Cygan, Marek},\n  year = {2024},\n  booktitle = {International Conference on Machine Learning},\n  eprint = {2403.00514},\n  archivePrefix = {arXiv},\n}\n\n@article{lin2025tdmpcsquare,\n  title = {{TD-M(PC)$^2$}: Improving Temporal Difference MPC Through Policy Constraint},\n  author = {Lin, Haotian and Wang, Pengcheng and Schneider, Jeff and Shi, Guanya},\n  year = {2025},\n  journal = {arXiv preprint arXiv:2502.03550},\n  eprint = {2502.03550},\n  archivePrefix = {arXiv},\n}\n\n@inproceedings{juliani2024plasticity,\n  title = {A Study of Plasticity Loss in On-Policy Deep Reinforcement Learning},\n  author = {Juliani, Arthur and Ash, Jordan T.},\n  year = {2024},\n  booktitle = {Advances in Neural Information Processing Systems},\n  eprint = {2405.19153},\n  archivePrefix = {arXiv},\n}\n\n@inproceedings{tang2025churn,\n  title = {Mitigating Plasticity Loss in Continual Reinforcement Learning by Reducing Churn},\n  author = {Tang, Hongyao and Obando-Ceron, Johan and Castro, Pablo Samuel and Courville, Aaron and Berseth, Glen},\n  year = {2025},\n  booktitle = {International Conference on Machine Learning},\n  eprint = {2506.00592},\n  archivePrefix = {arXiv},\n}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_related-work-update_20260518T142443",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/references.bib",
    "old_string": "@article{lenz2025macura,\n  title = {Trust the Model Where It Trusts Itself -- Model-Based Actor-Critic with Uncertainty-Aware Rollout Adaption},\n  author = {Lenz, S and et, al},\n  year = {2025},\n  journal = {arXiv preprint arXiv:2405.19014},\n  eprint = {2405.19014},\n  archivePrefix = {arXiv},\n}",
    "new_string": "@article{lenz2025macura,\n  title = {Trust the Model Where It Trusts Itself -- Model-Based Actor-Critic with Uncertainty-Aware Rollout Adaption},\n  author = {Lenz, S and et, al},\n  year = {2025},\n  journal = {arXiv preprint arXiv:2405.19014},\n  eprint = {2405.19014},\n  archivePrefix = {arXiv},\n}\n\n@inproceedings{nauman2024overestimation,\n  title = {Overestimation, Overfitting, and Plasticity in Actor-Critic: the Bitter Lesson of Reinforcement Learning},\n  author = {Nauman, Michal and Bortkiewicz, Micha{\\l} and Mi{\\l}o{\\'s}, Piotr and Trzcinski, Tomasz and Ostaszewski, Mateusz and Cygan, Marek},\n  year = {2024},\n  booktitle = {International Conference on Machine Learning},\n  eprint = {2403.00514},\n  archivePrefix = {arXiv},\n}\n\n@article{lin2025tdmpcsquare,\n  title = {{TD-M(PC)$^2$}: Improving Temporal Difference MPC Through Policy Constraint},\n  author = {Lin, Haotian and Wang, Pengcheng and Schneider, Jeff and Shi, Guanya},\n  year = {2025},\n  journal = {arXiv preprint arXiv:2502.03550},\n  eprint = {2502.03550},\n  archivePrefix = {arXiv},\n}\n\n@inproceedings{juliani2024plasticity,\n  title = {A Study of Plasticity Loss in On-Policy Deep Reinforcement Learning},\n  author = {Juliani, Arthur and Ash, Jordan T.},\n  year = {2024},\n  booktitle = {Advances in Neural Information Processing Systems},\n  eprint = {2405.19153},\n  archivePrefix = {arXiv},\n}\n\n@inproceedings{tang2025churn,\n  title = {Mitigating Plasticity Loss in Continual Reinforcement Learning by Reducing Churn},\n  author = {Tang, Hongyao and Obando-Ceron, Johan and Castro, Pablo Samuel and Courville, Aaron and Berseth, Glen},\n  year = {2025},\n  booktitle = {International Conference on Machine Learning},\n  eprint = {2506.00592},\n  archivePrefix = {arXiv},\n}"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-18T14:27:42.171060+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/references.bib has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_related-work-update_20260518T142443",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-18T14:27:42.171217+00:00_

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
  "session": "worker_paper_related-work-update_20260518T142443",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-18T14:27:42.171372+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Temporal Abstraction.}
5	The options framework \citep{sutton1999options} and model-free action-repetition methods \citep{sharma2017figar, biedenkapp2021temporl, lakshminarayanan2017dynamic} achieve temporal abstraction by training values on real transitions, insulating them from model-induced bias. In world-model RL, the Dreamer family \citep{hafner2020dreamerv1, hafner2021dreamerv2, hafner2023dreamerv3} and transformer-based variants \citep{micheli2023iris, robine2023twm, hafner2025dreamerv4} train policies in imagination at fixed $\dt{=}1$. Several works introduce temporal abstraction via hierarchical representations \citep{gumbsch2024thick, mattes2024hieros}, goal-conditioned jumps \citep{li2025lsimagine}, or multi-scale state-space models \citep{shaj2023mts3}, but none conditions a flat dynamics model on $\dt$ for imagination-based policy training.
6	
7	\paragraph{TAWM and the MPC--Imagination Contrast.}
8	TAWM \citep{nhu2025tawm} conditions a world model on $\dt$ within TD-MPC2 \citep{hansen2024tdmpc2} and achieves consistent gains. \citet{lin2025tdmpcsquare} trace persistent value overestimation in TD-MPC2 to structural policy mismatch, a complementary diagnosis to our identification of the imagination-based feedback loop as the critical factor. The critical distinction is architectural: TAWM re-plans from real states at every step, so model errors do not accumulate into the critic. We show that identical $\dt$-conditioning fails in DreamerV3's imagination loop, where errors compound through bootstrapping and transform manageable imprecision into pathological value overestimation.
9	
10	\paragraph{Value Overestimation.}
11	\citet{thrun1993issues} first identified maximization bias in Q-learning with function approximation. Double Q-learning \citep{vanhasselt2016double} decouples action selection from evaluation; TD3 \citep{fujimoto2018td3} extends this to actor-critic methods via clipped doubl
…[truncated 3398 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_related-work-update_20260518T142443",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-18T14:27:42.171526+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -n \"—\\| – \" /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/related_work.tex",
  "description": "Check for em-dash and en-dash AI writing markers"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_related-work-update_20260518T142443",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -n \"—\\| – \" /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/related_work.tex",
    "description": "Check for em-dash and en-dash AI writing markers"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-18T14:27:42.171652+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_related-work-update_20260518T142443",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-18T14:27:42.171787+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -n \"ing\\.\" /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/related_work.tex | grep -v \"learning\\.\\|bootstrapping\\.\\|conditioning\\.\"",
  "description": "Check for -ing phrase endings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_related-work-update_20260518T142443",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -n \"ing\\.\" /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/related_work.tex | grep -v \"learning\\.\\|bootstrapping\\.\\|conditioning\\.\"",
    "description": "Check for -ing phrase endings"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-18T14:27:42.171945+00:00_

5:The options framework \citep{sutton1999options} and model-free action-repetition methods \citep{sharma2017figar, biedenkapp2021temporl, lakshminarayanan2017dynamic} achieve temporal abstraction by training values on real transitions, insulating them from model-induced bias. In world-model RL, the Dreamer family \citep{hafner2020dreamerv1, hafner2021dreamerv2, hafner2023dreamerv3} and transformer-based variants \citep{micheli2023iris, robine2023twm, hafner2025dreamerv4} train policies in imagination at fixed $\dt{=}1$. Several works introduce temporal abstraction via hierarchical representations \citep{gumbsch2024thick, mattes2024hieros}, goal-conditioned jumps \citep{li2025lsimagine}, or multi-scale state-space models \citep{shaj2023mts3}, but none conditions a flat dynamics model on $\dt$ for imagination-based policy training.
11:\citet{thrun1993issues} first identified maximization bias in Q-learning with function approximation. Double Q-learning \citep{vanhasselt2016double} decouples action selection from evaluation; TD3 \citep{fujimoto2018td3} extends this to actor-critic methods via clipped double-Q critics; SAC \citep{haarnoja2018sac} uses entropy regularization to implicitly reduce overestimation; REDQ \citep{chen2021redq} further mitigates overestimation through randomized Q-function ensembles. These model-free solutions target the max operator as the amplifier. In model-based settings, MBPO \citep{janner2019mbpo} bounds model use via short rollouts and MOPO \citep{yu2020mopo} penalizes rewards by model uncertainty. \citet{lu2018nondelusional} identify delusional bias from policy-class constraints. \citet{nauman2024overestimation} show that overestimation, overfitting, and plasticity loss are coupled phenomena in actor-critic methods; CIVO can be understood as a model-induced instance within this broader framework. Our CIVO is mechanistically distinct: the amplifier is the world model's co-adaptation with a learned temporal embedding. This produces systema
…[truncated 638 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_related-work-update_20260518T142443",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 33 · 2026-05-18T14:27:42.172119+00:00_

新增内容无 -ing 短语结尾问题。已有内容（training, conditioning 等）是名词性用法，不是 AI 痕迹。

完成。修改汇总：

**references.bib** — 添加 4 个条目：
- `nauman2024overestimation` (ICML 2024, arXiv 2403.00514)
- `lin2025tdmpcsquare` (arXiv 2502.03550)
- `juliani2024plasticity` (NeurIPS 2024, arXiv 2405.19153)
- `tang2025churn` (ICML 2025, arXiv 2506.00592)

**related_work.tex** — 3 处插入：
1. **TAWM 段落**：TD-M(PC)² 引用，指出其将 TD-MPC2 中的 value overestimation 归因于 policy mismatch，与本文对 imagination loop 的诊断互补
2. **Value Overestimation 段落**：Nauman 引用，将 CIVO 定位为其 overestimation-plasticity 耦合框架下的 model-induced 实例
3. **Network Capacity 段落**：Juliani、Tang、Nauman 三篇并入，分别补充 on-policy plasticity loss、churn-based plasticity 机制、overestimation-plasticity 耦合证据

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_related-work-update_20260518T142443"
}
```

</details>

---
