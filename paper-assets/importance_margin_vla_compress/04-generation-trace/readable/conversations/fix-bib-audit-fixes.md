# fix bib audit fixes

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 77
- **Recorded user turns:** 0
- **Tool calls:** 38
- **Original source:** `logs/chats/worker_fix_bib_audit_fixes_20260528T171451.jsonl`
- **Structured JSON:** [`3d01a47e8ab4869c3fa0.json`](../../sessions/3d/3d01a47e8ab4869c3fa0.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

77 recorded events

### Tool call

_source line 1 · 2026-05-28T17:17:48.472891+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.bib",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_bib_audit_fixes_20260528T171451",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.bib",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/paper"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-28T17:17:48.473262+00:00_

&lt;tool_use_error>Directory does not exist: /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/paper. Note: your current working directory is /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress.&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_bib_audit_fixes_20260528T171451",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-28T17:17:48.473439+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.bib",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_bib_audit_fixes_20260528T171451",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.bib",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-28T17:17:48.473577+00:00_

artifacts/corl_template/corl_2026_template_submission/example.bib
artifacts/corl_template/__MACOSX/corl_2026_template_submission/._example.bib
artifacts/_project/paper/new_references_8papers.bib
artifacts/new_references_8papers.bib
artifacts/missing_citations_4papers.bib
docs/paper/references.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_bib_audit_fixes_20260528T171451",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-28T17:17:48.473701+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_bib_audit_fixes_20260528T171451",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/references.bib"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-28T17:17:48.473975+00:00_

1	% References for: The Cliff Edge — Why Vision Token Reduction Fails
2	% Catastrophically in VLA Closed-Loop Control
3	% Auto-generated from literature_map.yaml (verified entries only)
4	% 2026-05-17
5	
6	% ============================================================
7	% Attention Analysis
8	% ============================================================
9	
10	@inproceedings{abnar2020quantifying,
11	  title={Quantifying Attention Flow in Transformers},
12	  author={Abnar, Samira and Zuidema, Willem},
13	  booktitle={Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics},
14	  pages={4190--4197},
15	  year={2020},
16	}
17	
18	% ============================================================
19	% VLA Token Compression (concurrent work)
20	% ============================================================
21	
22	@article{gao2025compressorvla,
23	  title={Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation},
24	  author={Gao, Juntao and Ye, Feiyang and Zhang, Jing and Qian, Wenjing},
25	  journal={arXiv preprint arXiv:2511.18950},
26	  year={2025},
27	  eprint={2511.18950},
28	  archivePrefix={arXiv}
29	}
30	
31	@article{wang2025specprunevla,
32	  title={SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning},
33	  author={Wang, Hanzhen and Xu, Jiaming and Xiang, Yushun and Pan, Jiayi and Zhou, Yongkang and Li, Yong-Lu and Dai, Guohao},
34	  journal={arXiv preprint arXiv:2509.05614},
35	  year={2025},
36	  eprint={2509.05614},
37	  archivePrefix={arXiv}
38	}
39	
40	@inproceedings{jiang2026lightvla,
41	  title={The Better You Learn, The Smarter You Prune: Towards Efficient Vision-Language-Action Models via Differentiable Token Pruning},
42	  author={Jiang, Titong and Jiang, Xuefeng and Ma, Yuan and Wen, Xin and Li, Bailin and Zhan, Kun and Jia, Peng and Liu, Yahui and Sun, Sheng and Lang, Xianpeng},
43	  booktitle={Proceedings of the IEEE International Confe
…[truncated 23702 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_bib_audit_fixes_20260528T171451",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-28T17:17:48.474204+00:00_

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
  "session": "worker_fix_bib_audit_fixes_20260528T171451",
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

_source line 8 · 2026-05-28T17:17:48.474360+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_bib_audit_fixes_20260528T171451",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-28T17:17:48.474541+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "FastV \"An Image is Worth 1/2 Tokens After Layer 2\" ECCV 2024 full author list"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_bib_audit_fixes_20260528T171451",
  "tool": "WebSearch",
  "tool_args": {
    "query": "FastV \"An Image is Worth 1/2 Tokens After Layer 2\" ECCV 2024 full author list"
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-28T17:17:48.474718+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "pi0.5 \"pi_{0.5}\" black 2025 CoRL PMLR 305 proceedings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_bib_audit_fixes_20260528T171451",
  "tool": "WebSearch",
  "tool_args": {
    "query": "pi0.5 \"pi_{0.5}\" black 2025 CoRL PMLR 305 proceedings"
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-28T17:17:48.474883+00:00_

Web search results for query: "pi0.5 "pi_{0.5}" black 2025 CoRL PMLR 305 proceedings"

Links: [{"title":"GitHub - mlresearch/v305: Proceedings of CoRL 2025 · GitHub","url":"https://github.com/mlresearch/v305"},{"title":"CoRL 2025 - Awards","url":"https://2025.corl.org/program/awards"},{"title":"CoRL 2025 Survey - Speaker Deck","url":"https://speakerdeck.com/harukiabe/corl-2025-survey"},{"title":"GitHub - UT-Austin-RPL/openreview-to-pmlr: Making PMLR Proceedings from CoRL OpenReview Data · GitHub","url":"https://github.com/UT-Austin-RPL/openreview-to-pmlr"},{"title":"CoRL Papers Published in Proceedings of Machine Learning - News/Research - Berkeley Center for New Media","url":"https://bcnm.berkeley.edu/news-research/5515/corl-papers-published-in-proceedings-of-machine-learning"},{"title":"Task adaptation of Vision-Language-Action model: 1st Place Solution for the 2025 BEHAVIOR Challenge","url":"https://arxiv.org/pdf/2512.06951"},{"title":"Evaluating \\( \\pi_0 \\) in the Wild: Strengths, Problems, and the Future of Generalist Robot Policies","url":"https://penn-pal-lab.github.io/Pi0-Experiment-in-the-Wild/"},{"title":"Proceedings of Machine Learning Research | The Proceedings of Machine Learning Research (formerly JMLR Workshop and Conference Proceedings) is a series aimed specifically at publishing machine learning research presented at workshops and conferences. Each volume is separately titled and associated with a particular workshop or conference. Volumes are published online on the PMLR web site. The Series Editors are Neil D. Lawrence and Mark Reid.","url":"https://proceedings.mlr.press/"},{"title":"Journal and Conference Papers","url":"http://rl.cs.rutgers.edu/publications.html"}]

Based on the search results, I found relevant information about your query:

Pi 0.5 is "a Vision-Language-Action Model with Open-World Generalization" with Kevin Black as one of the lead authors. This work was published as Volume 305 by the Proceedings of Machine Learning Research
…[truncated 356 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_bib_audit_fixes_20260528T171451",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-28T17:17:48.475055+00:00_

Web search results for query: "FastV "An Image is Worth 1/2 Tokens After Layer 2" ECCV 2024 full author list"

Links: [{"title":"GitHub - MachineLearningSystem/24ECCV-FastV: [ECCV 2024] Code for paper: An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models · GitHub","url":"https://github.com/MachineLearningSystem/24ECCV-FastV"},{"title":"GitHub - pkunlp-icler/FastV: [ECCV 2024 Oral] Code for paper: An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models · GitHub","url":"https://github.com/pkunlp-icler/FastV"},{"title":"An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models | Computer Vision – ECCV 2024","url":"https://dl.acm.org/doi/10.1007/978-3-031-73004-7_2"},{"title":"[2403.06764] An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models","url":"https://arxiv.org/abs/2403.06764"},{"title":"GitHub - chenllliang/FastV: Code for paper: An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models · GitHub","url":"https://github.com/chenllliang/FastV"},{"title":"An Image is Worth 1/2 Tokens After Layer 2: Plug-and-PLay Acceleration for VLLM Inference","url":"https://arxiv.org/html/2403.06764v3"},{"title":"An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference   Acceleration for Large Vision-Language Models","url":"https://arxiv.org/pdf/2403.06764"},{"title":"[PDF] An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/An-Image-is-Worth-1-2-Tokens-After-Layer-2:-for-Chen-Zhao/3421d12d98956c36c5d39c0ef023b378b6922068"}]

Based on the search results, I found the full author list for the FastV paper. The authors are: Liang Chen, Haozhe Zhao, Tianyu Liu, Shu
…[truncated 153 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_bib_audit_fixes_20260528T171451",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-28T17:17:48.475248+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "site:proceedings.mlr.press \"pi_{0.5}\" OR \"pi0.5\" v305"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_bib_audit_fixes_20260528T171451",
  "tool": "WebSearch",
  "tool_args": {
    "query": "site:proceedings.mlr.press \"pi_{0.5}\" OR \"pi0.5\" v305"
  }
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-28T17:17:48.475377+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2403.06764 FastV authors \"Liang Chen\" \"Haozhe Zhao\" \"Tianyu Liu\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_bib_audit_fixes_20260528T171451",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2403.06764 FastV authors \"Liang Chen\" \"Haozhe Zhao\" \"Tianyu Liu\""
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-28T17:17:48.475527+00:00_

Web search results for query: "arxiv 2403.06764 FastV authors "Liang Chen" "Haozhe Zhao" "Tianyu Liu""

Links: [{"title":"[2403.06764] An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models","url":"https://arxiv.org/abs/2403.06764"},{"title":"An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models","url":"https://arxiv.org/html/2403.06764v1"},{"title":"Paper page - An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models","url":"https://huggingface.co/papers/2403.06764"},{"title":"[2403.06764] An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models","url":"http://export.arxiv.org/abs/2403.06764"},{"title":"GitHub - chenllliang/FastV: Code for paper: An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models · GitHub","url":"https://github.com/chenllliang/FastV"},{"title":"GitHub - pkunlp-icler/FastV: [ECCV 2024 Oral] Code for paper: An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models · GitHub","url":"https://github.com/pkunlp-icler/FastV"},{"title":"FastV: Plug-and-Play LVLM Inference Acceleration","url":"https://www.emergentmind.com/papers/2403.06764"},{"title":"[PDF] An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/An-Image-is-Worth-1-2-Tokens-After-Layer-2:-for-Chen-Zhao/3421d12d98956c36c5d39c0ef023b378b6922068"},{"title":"An Image is Worth 1/2 Tokens After Layer 2: Plug-and-PLay Acceleration for VLLM Inference","url":"https://arxiv.org/html/2403.06764v3"}]

Based on the search results, I found the paper arxiv:2403.06764 titled "An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inferen
…[truncated 646 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_bib_audit_fixes_20260528T171451",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-28T17:17:48.475775+00:00_

Web search results for query: "site:proceedings.mlr.press "pi_{0.5}" OR "pi0.5" v305"

Links: [{"title":"$\\pi_0.5$: a Vision-Language-Action Model with Open-World Generalization","url":"https://proceedings.mlr.press/v305/black25a.html"},{"title":"Sample-Efficient Online Control Policy Learning with Real-Time Recursive Model Updates","url":"https://proceedings.mlr.press/v305/zhang25d.html"},{"title":"Learning Long-Context Diffusion Policies via Past-Token Prediction","url":"https://proceedings.mlr.press/v305/villasevil25a.html"},{"title":"Meta-Optimization and Program Search using Language Models for Task and Motion Planning","url":"https://proceedings.mlr.press/v305/shcherba25a.html"},{"title":"About | Proceedings of Machine Learning Research - mlr.press","url":"https://proceedings.mlr.press/about/"},{"title":"A mixture representation of \\pi with applications in Markov chain Monte   Carlo and perfect sampling","url":"https://arxiv.org/pdf/math/0407120"},{"title":"Proceedings of Machine Learning Research | Proceedings of The 9th Conference on Robot Learning Held in Seoul, Korea on 27-30 September 2025 Published as Volume 305 by the Proceedings of Machine Learning Research on 07 October 2025. Volume Edited by: Joseph Lim Shuran Song Hae-Won Park Series Editors: Neil D. Lawrence","url":"https://proceedings.mlr.press/v305/"},{"title":"Proceedings of Machine Learning Research | The Proceedings of Machine Learning Research (formerly JMLR Workshop and Conference Proceedings) is a series aimed specifically at publishing machine learning research presented at workshops and conferences. Each volume is separately titled and associated with a particular workshop or conference. Volumes are published online on the PMLR web site. The Series Editors are Neil D. Lawrence and Mark Reid.","url":"https://proceedings.mlr.press/"}]

The search was successful! I found the paper you were looking for:

**π₀.₅: a Vision-Language-Action Model with Open-World Generalization** was published i
…[truncated 525 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_bib_audit_fixes_20260528T171451",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-28T17:17:48.475973+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_bib_audit_fixes_20260528T171451",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-28T17:17:48.476107+00:00_

docs/paper/sections/analysis.tex
docs/paper/sections/background.tex
docs/paper/sections/experimental_setup.tex
docs/paper/sections/results_draft.tex
docs/paper/sections/analysis_draft.tex
docs/paper/experiments_deprecated.tex
docs/paper/sections/experiments.tex
docs/paper/sections/related_work_draft.tex
docs/paper/sections/introduction.tex
docs/paper/background.tex
docs/paper/results_v2.tex
docs/paper/experimental_setup.tex
docs/paper/results.tex
docs/paper/discussion.tex
docs/paper/analysis.tex
docs/paper/introduction.tex
docs/paper/related_work.tex
docs/paper/abstract.tex
docs/paper/appendix.tex
docs/paper/conclusion.tex
docs/paper/limitations.tex
docs/paper/main.tex
docs/paper/experiments.tex
docs/paper/method.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_bib_audit_fixes_20260528T171451",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-28T17:17:48.476258+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Find all cited bib keys in tex",
  "prompt": "I need to find ALL citation keys referenced in .tex files under /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/. \n\nSearch for all occurrences of \\cite{...}, \\citep{...}, \\citet{...}, and similar citation commands across all .tex files. Extract just the citation keys (the text inside the braces). Note that a single \\cite command can contain multiple comma-separated keys like \\cite{key1,key2}.\n\nReport a deduplicated sorted list of all citation keys found."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_bib_audit_fixes_20260528T171451",
  "tool": "Agent",
  "tool_args": {
    "subagent_type": "Explore",
    "description": "Find all cited bib keys in tex",
    "prompt": "I need to find ALL citation keys referenced in .tex files under /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/. \n\nSearch for all occurrences of \\cite{...}, \\citep{...}, \\citet{...}, and similar citation commands across all .tex files. Extract just the citation keys (the text inside the braces). Note that a single \\cite command can contain multiple comma-separated keys like \\cite{key1,key2}.\n\nReport a deduplicated sorted list of all citation keys found."
  }
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-28T17:17:48.476417+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/**/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_bib_audit_fixes_20260528T171451",
  "tool": "Glob",
  "tool_args": {
    "pattern": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/**/*.tex"
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-28T17:17:48.476540+00:00_

docs/paper/sections/analysis.tex
docs/paper/sections/background.tex
docs/paper/sections/experimental_setup.tex
docs/paper/sections/results_draft.tex
docs/paper/sections/analysis_draft.tex
docs/paper/experiments_deprecated.tex
docs/paper/sections/experiments.tex
docs/paper/sections/related_work_draft.tex
docs/paper/sections/introduction.tex
docs/paper/background.tex
docs/paper/results_v2.tex
docs/paper/experimental_setup.tex
docs/paper/results.tex
docs/paper/discussion.tex
docs/paper/analysis.tex
docs/paper/introduction.tex
docs/paper/related_work.tex
docs/paper/abstract.tex
docs/paper/appendix.tex
docs/paper/conclusion.tex
docs/paper/limitations.tex
docs/paper/main.tex
docs/paper/experiments.tex
docs/paper/method.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_bib_audit_fixes_20260528T171451",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-28T17:17:48.476668+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\cite[tp]*\\{[^}]+\\}",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper",
  "type": "tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_bib_audit_fixes_20260528T171451",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\cite[tp]*\\{[^}]+\\}",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper",
    "type": "tex",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-28T17:17:48.476791+00:00_

&lt;persisted-output>
Output too large (20.7KB). Full output saved to: /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress/5fcbbc8f-a94c-480e-bf9e-7ce4eca56009/tool-results/toolu_01MpHFdJF6cp3R1cC4oympNJ.txt

Preview (first 2KB):
docs/paper/related_work.tex:5:DynamicViT~\cite{rao2021dynamicvit}, EViT~\cite{liang2022evit}, A-ViT~\cite{yin2022avit}, and Token Merging~\cite{bolya2023tome} remove 50--66\% of tokens with under 0.5\,pp ImageNet accuracy loss, but robotic manipulation inverts the spatial-insensitivity assumption. None has been evaluated in closed-loop VLA control.
docs/paper/related_work.tex:8:[Omitted long matching line]
docs/paper/related_work.tex:11:LLaVA~\cite{liu2023llava} projects patches independently through an MLP; BLIP-2~\cite{li2023blip2} uses cross-attention queries; pixel shuffle~\cite{shi2016subpixel} folds spatial neighborhoods into channels. These create qualitatively different token dependencies whose pruning consequences have not been characterized. We provide the first cross-architecture analysis of how connector coupling and task complexity jointly govern VLA token compressibility.
docs/paper/experiments.tex:7:We evaluate vision token pruning across six VLA architectures spanning three connector families on LIBERO~\cite{liu2023libero}, which provides four task suites of increasing complexity: Object, Spatial, Goal, and Long (10 tasks $\times$ 50 episodes each).
docs/paper/experiments.tex:9:[Omitted long matching line]
docs/paper/results_v2.tex:4:We evaluate token pruning across six VLA models spanning three connector families on LIBERO-Object~\cite{liu2023libero} (10 tasks, 50 episodes each, 500 total). All success rates report Wilson 95\% confidence intervals for single-seed results and mean $\pm$ standard deviation for multi-seed results.
docs/paper/results_v2.tex:9:[Omitted long matching line]
docs/paper/results_v2.tex:11:[Omitted long matching line]
docs/pap
…[truncated 247 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_bib_audit_fixes_20260528T171451",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-28T17:17:48.476937+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress/5fcbbc8f-a94c-480e-bf9e-7ce4eca56009/tool-results/toolu_01MpHFdJF6cp3R1cC4oympNJ.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_bib_audit_fixes_20260528T171451",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress/5fcbbc8f-a94c-480e-bf9e-7ce4eca56009/tool-results/toolu_01MpHFdJF6cp3R1cC4oympNJ.txt"
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-28T17:17:48.477107+00:00_

1	docs/paper/related_work.tex:5:DynamicViT~\cite{rao2021dynamicvit}, EViT~\cite{liang2022evit}, A-ViT~\cite{yin2022avit}, and Token Merging~\cite{bolya2023tome} remove 50--66\% of tokens with under 0.5\,pp ImageNet accuracy loss, but robotic manipulation inverts the spatial-insensitivity assumption. None has been evaluated in closed-loop VLA control.
2	docs/paper/related_work.tex:8:[Omitted long matching line]
3	docs/paper/related_work.tex:11:LLaVA~\cite{liu2023llava} projects patches independently through an MLP; BLIP-2~\cite{li2023blip2} uses cross-attention queries; pixel shuffle~\cite{shi2016subpixel} folds spatial neighborhoods into channels. These create qualitatively different token dependencies whose pruning consequences have not been characterized. We provide the first cross-architecture analysis of how connector coupling and task complexity jointly govern VLA token compressibility.
4	docs/paper/experiments.tex:7:We evaluate vision token pruning across six VLA architectures spanning three connector families on LIBERO~\cite{liu2023libero}, which provides four task suites of increasing complexity: Object, Spatial, Goal, and Long (10 tasks $\times$ 50 episodes each).
5	docs/paper/experiments.tex:9:[Omitted long matching line]
6	docs/paper/results_v2.tex:4:We evaluate token pruning across six VLA models spanning three connector families on LIBERO-Object~\cite{liu2023libero} (10 tasks, 50 episodes each, 500 total). All success rates report Wilson 95\% confidence intervals for single-seed results and mean $\pm$ standard deviation for multi-seed results.
7	docs/paper/results_v2.tex:9:[Omitted long matching line]
8	docs/paper/results_v2.tex:11:[Omitted long matching line]
9	docs/paper/results_v2.tex:16:[Omitted long matching line]
10	docs/paper/results_v2.tex:22:$\pi_0$~\cite{black2024pi0} & Linear proj & 3.3B & 256 & 0.038 & $k{=}0.1$: $\mathcal{L}_1{=}0.976$ ($+$2.4\%)$^\dagger$ & Uniformly critical \\
11	docs/paper/results_v2.tex:23:$\pi_0.5$~\cite{black2025pi05
…[truncated 19455 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_bib_audit_fixes_20260528T171451",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-28T17:17:48.477280+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper -name \"*.tex\" -type f | sort"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_bib_audit_fixes_20260528T171451",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper -name \"*.tex\" -type f | sort"
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-28T17:17:48.477408+00:00_

/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/analysis.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/appendix.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/background.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/discussion.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experimental_setup.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experiments.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experiments_deprecated.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/limitations.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/method.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/related_work.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/results.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/results_v2.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/sections/analysis.t
…[truncated 910 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_bib_audit_fixes_20260528T171451",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-28T17:17:48.477554+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_bib_audit_fixes_20260528T171451",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/main.tex"
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-28T17:17:48.477678+00:00_

1	\documentclass{article}
2	
3	\usepackage{corl_2026} % Submission version: anonymous, line numbers enabled.
4	% \usepackage[final]{corl_2026} % Uncomment for camera-ready.
5	
6	\usepackage{amsmath,amssymb}
7	\usepackage{graphicx}
8	\usepackage{booktabs}
9	\usepackage{multirow}
10	\usepackage{enumitem}
11	\usepackage{subcaption}
12	\usepackage{wrapfig}
13	
14	% Tighten float spacing for page limit
15	\setlength{\textfloatsep}{8pt plus 2pt minus 4pt}
16	\setlength{\floatsep}{8pt plus 2pt minus 4pt}
17	\setlength{\intextsep}{8pt plus 2pt minus 4pt}
18	\setlength{\abovecaptionskip}{4pt}
19	\setlength{\belowcaptionskip}{0pt}
20	
21	\title{Why Token Pruning Crashes Some Robot Policies but Not Others:\\Vision Connectors and VLA Token Compressibility}
22	
23	\begin{document}
24	\maketitle
25	
26	\input{abstract}
27	
28	\keywords{vision-language-action models, token pruning, robot learning}
29	
30	\input{introduction}
31	
32	\input{related_work}
33	
34	\input{method}
35	
36	\input{experiments}
37	
38	\input{conclusion}
39	
40	\input{limitations}
41	
42	\bibliography{references}
43	
44	\input{appendix}
45	
46	\end{document}
47	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_bib_audit_fixes_20260528T171451",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-28T17:17:48.477810+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_bib_audit_fixes_20260528T171451",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-28T17:17:48.477927+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{ViT token pruning.}
5	DynamicViT~\cite{rao2021dynamicvit}, EViT~\cite{liang2022evit}, A-ViT~\cite{yin2022avit}, and Token Merging~\cite{bolya2023tome} remove 50--66\% of tokens with under 0.5\,pp ImageNet accuracy loss, but robotic manipulation inverts the spatial-insensitivity assumption. None has been evaluated in closed-loop VLA control.
6	
7	\paragraph{Token efficiency in VLMs and VLAs.}
8	FastV~\cite{chen2024fastv} and PruMerge~\cite{shang2024prumerge} reduce vision tokens in VLMs using attention signals. VLA-specific methods have emerged: VLA-IAP~\cite{cheng2026vlaiap}, VLA-Cache~\cite{xu2025vlacache}, EfficientVLA~\cite{yang2025efficientvla}, VLA-Pruner~\cite{liu2025vlapruner}, LightVLA~\cite{jiang2026lightvla}, and Compressor-VLA~\cite{gao2025compressorvla}. Each validates on a single architecture; we ask how architectural choices determine which compression approaches succeed or fail.
9	
10	\paragraph{Vision connectors.}
11	LLaVA~\cite{liu2023llava} projects patches independently through an MLP; BLIP-2~\cite{li2023blip2} uses cross-attention queries; pixel shuffle~\cite{shi2016subpixel} folds spatial neighborhoods into channels. These create qualitatively different token dependencies whose pruning consequences have not been characterized. We provide the first cross-architecture analysis of how connector coupling and task complexity jointly govern VLA token compressibility.
12	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_bib_audit_fixes_20260528T171451",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-28T17:17:48.478065+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_bib_audit_fixes_20260528T171451",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-28T17:17:48.478215+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	\begin{figure*}[t]
5	\centering
6	\includegraphics[width=\textwidth]{figures/paper/fig_hero_overview.pdf}
7	\caption{Overview of VLA token compressibility.
8	\textbf{(a)}~The same robot observation produces qualitatively different token importance patterns through different vision connectors, quantified by the coefficient of variation (CV) of post-connector token norms.
9	\textbf{(b)}~Connector architecture determines pruning tolerance: independent connectors degrade gracefully, entangling connectors exhibit cliffs; task complexity amplifies the divergence.
10	\textbf{(c)}~A single forward pass CV diagnostic routes each architecture to an appropriate compression strategy.}
11	\label{fig:teaser}
12	\end{figure*}
13	
14	Remove 5\% of vision tokens from SmolVLA and its success rate collapses from 59.2\% to near-zero (${\leq}$6.6\%). Apply the same reduction to $\pi_{0.5}$ and it retains 98.2\% under L2 norm selection. Both are Vision-Language-Action (VLA) models built on a ViT encoder feeding tokens through a connector into a language model backbone; the critical difference is the connector architecture. Token pruning is well-established for ViTs~\cite{rao2021dynamicvit,bolya2023tome,liang2022evit} and extends to VLAs~\cite{cheng2026vlaiap,xu2025vlacache,yang2025efficientvla,liu2025vlapruner}, but each method validates on a single architecture, implicitly assuming pruning transfers across designs.
15	
16	Yet current VLAs employ fundamentally different vision connectors---linear projections~\cite{black2024pi0}, MLP projectors~\cite{kim2024openvla}, pixel-shuffle folding~\cite{shukor2025smolvla}, and learned encoders with cross-token self-attention~\cite{zheng2025xvla}---each imposing distinct constraints on how visual information distributes across tokens. Deploying a pruning method validated on one connector type to another risks silent degradation or complete failure.
17	
18	We present an empirical study of VLA 
…[truncated 1579 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_bib_audit_fixes_20260528T171451",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-28T17:17:48.478374+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_bib_audit_fixes_20260528T171451",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-28T17:17:48.478569+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Models and Connectors}
5	\label{sec:models}
6	
7	We evaluate token pruning across six VLA architectures spanning three vision connector families (Table~\ref{tab:model_properties}; Figure~\ref{fig:architecture}). These connectors differ in whether they process ViT patches independently or create cross-token dependencies.
8	
9	\textbf{Linear projection} applies a single matrix multiplication per patch. $\pi_{0}$~\cite{black2024pi0} projects 256 patches through a linear layer; $\pi_{0.5}$~\cite{black2025pi05} uses a $\times\!\sqrt{d}$-scaled linear projection across 768 tokens from three cameras (CV$\,{<}\,$0.06).
10	
11	\textbf{MLP projector} maps each patch independently through a multi-layer perceptron. OpenVLA~\cite{kim2024openvla} uses a three-layer MLP (256 tokens; CV$\,{=}\,$0.215); OFT~\cite{kim2025openoft} shares the same connector (512 tokens; CV$\,{=}\,$0.219).
12	
13	\textbf{Token-entangling connectors} introduce cross-token dependencies. X-VLA~\cite{zheng2025xvla} feeds tokens through a 12-layer BART encoder~\cite{lewis2020bart} (50 tokens). SmolVLA~\cite{shukor2025smolvla} applies pixel-shuffle $4{\times}4$ folding, concatenating 16 contiguous patches per output token (128 tokens).
14	
15	We classify coupling as \emph{independent} when each output token depends on a single input patch, and \emph{entangling} when output tokens encode information from multiple patches. Four models are evaluated in closed-loop control on LIBERO~\cite{liu2023libero}; $\pi_{0}$ and OFT contribute to the CV diagnostic only.
16	
17	\begin{figure*}[t]
18	\centering
19	\includegraphics[width=\textwidth]{figures/paper/fig_architecture_v4.pdf}
20	\caption{Vision connector architectures across four closed-loop VLAs, ordered by increasing compressibility fragility. Token-independent connectors ($\pi_{0.5}$: linear; OpenVLA: MLP) yield low CV. Token-entangling connectors (X-VLA: BART encoder; SmolVLA: pixel-shuffle) create cross-
…[truncated 3154 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_bib_audit_fixes_20260528T171451",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-28T17:17:48.478737+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/background.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_bib_audit_fixes_20260528T171451",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/background.tex"
  }
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-28T17:17:48.478881+00:00_

1	% background.tex -- Section 2: Background
2	
3	\section{Background}
4	\label{sec:background}
5	
6	This section describes the architectures and benchmark used in our study: SmolVLA~\cite{shukor2025smolvla} and OpenVLA~\cite{kim2024openvla}, two VLA models with contrasting vision connector designs, and the LIBERO benchmark~\cite{liu2023libero} on which we evaluate closed-loop performance.
7	
8	\subsection{SmolVLA Architecture}
9	\label{sec:smolvla_arch}
10	
11	Vision-Language-Action (VLA) models cast robotic control as conditional generation: given a camera observation and a language instruction, the model predicts a continuous action.
12	SmolVLA~\cite{shukor2025smolvla} instantiates this paradigm with approximately 451.5M parameters, organized into a vision encoder, a vision connector, a language model backbone, and an action head.
13	Figure~\ref{fig:architecture} contrasts the vision pipelines of SmolVLA and OpenVLA, highlighting the connector designs that determine compressibility.
14	
15	\begin{figure}[t]
16	\centering
17	\includegraphics[width=\linewidth]{figures/paper/fig_architecture.pdf}
18	\caption{Vision connector comparison. \textbf{Left}: SmolVLA applies $4{\times}4$ pixel-shuffle to fold 1024 SigLIP patches into 64 tokens per camera (128 total), creating dense, spatially entangled representations. \textbf{Right}: OpenVLA uses an MLP projector that maps each patch independently, producing 256 tokens with per-token independence. We hypothesize that this architectural difference is the primary factor governing token compressibility: pixel-shuffle tokens resist any form of deletion, while independently projected tokens allow graded pruning.}
19	\label{fig:architecture}
20	\end{figure}
21	
22	\paragraph{Vision encoder.}
23	SmolVLA uses the Sigmoid Loss for Language-Image Pre-training (SigLIP) encoder~\cite{zhai2023siglip} to process visual input.
24	SigLIP divides each camera image into non-overlapping spatial patches on a $32 \times 32$ grid, producing 1024
…[truncated 6245 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_bib_audit_fixes_20260528T171451",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-28T17:17:48.479033+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_bib_audit_fixes_20260528T171451",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/results.tex"
  }
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-28T17:17:48.479223+00:00_

1	\section{Results}
2	\label{sec:results}
3	
4	We evaluate token pruning across six VLA models spanning three connector families on LIBERO-Object~\cite{liu2023libero} (10 tasks, 50 episodes each, 500 total). All success rates report Wilson 95\% confidence intervals for single-seed results and mean $\pm$ standard deviation for multi-seed results.
5	
6	\subsection{Taxonomy Overview}
7	\label{sec:taxonomy_overview}
8	
9	Table~\ref{tab:taxonomy} organizes seven models into four response classes. The taxonomy reveals that effective vision-to-LLM pipeline complexity, not the nominal connector label or model scale, is strongly associated with pruning tolerance. Token importance CV tracks this ordering continuously across an 8$\times$ parameter range (450M to 7B): uniformly critical models cluster at CV $< 0.06$, threshold-graded at $\sim$0.15, smooth graded at $\sim$0.22, and catastrophic cliff at $>$0.3. A pairwise comparison between $\pi_0$ and OpenVLA (both consuming 256 SigLIP-based~\cite{zhai2023siglip} tokens but differing in connector, backbone, and encoder fusion) yields a 63\,pp gap at $k{=}0.1$; this gap is consistent with the monotonic CV-degradation pattern across all seven models (Section~\ref{sec:linear_results}).
10	
11	The four classes differ qualitatively in their failure mode. Uniformly critical models ($\pi_0$, $\pi_0.5$~\cite{black2025pi05}) distribute importance so evenly that no scoring method can identify dispensable tokens; pruning either preserves random spatial coverage (and survives) or removes a clustered patch (and fails). Threshold-graded models (X-VLA) tolerate removal up to a sharp onset point. Smooth graded models (OpenVLA, OFT, CogACT) degrade proportionally to the fraction removed. Catastrophic cliff models (SmolVLA) collapse at any removal level.
12	
13	\begin{table*}[t]
14	\centering
15	\small
16	\caption{Seven-model connector taxonomy. CV = coefficient of variation of vision token L2 norms. $^\dagger\pi_0$: offline metrics only, no clo
…[truncated 15852 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_bib_audit_fixes_20260528T171451",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-28T17:17:48.479380+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/appendix.tex",
  "limit": "500"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_bib_audit_fixes_20260528T171451",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/appendix.tex",
    "limit": "500"
  }
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-28T17:17:48.479613+00:00_

1	\appendix
2	
3	\section{Full Pruning Results}
4	\label{app:full_results}
5	
6	Table~\ref{tab:full_results} reports the complete closed-loop success rates for all four models across all tested retention ratios, including OpenVLA and $k{=}0.7$ data omitted from Table~\ref{tab:main_results} for space.
7	
8	\begin{table*}[ht]
9	\centering
10	\footnotesize
11	\caption{Full closed-loop success rates (\%) on LIBERO under L2 norm (L2) and random (R) token pruning. Best result per row in \textbf{bold}. ``--'' indicates data not yet collected. OpenVLA Goal, Spatial, and Long use per-suite fine-tuned checkpoints. Single seed (seed 42) except $\pi_{0.5}$ Long (five-seed mean, $n{=}5$). \textsuperscript{$\dagger$}Attention-based scoring (A) at $k{=}0.9$ for OpenVLA.}
12	\label{tab:full_results}
13	\setlength{\tabcolsep}{4pt}
14	\begin{tabular}{llccccc}
15	\toprule
16	Model & Suite & Baseline & $k{=}0.95$ (L2 / R) & $k{=}0.9$ (L2 / R) & $k{=}0.7$ (L2 / R) & $k{=}0.5$ (L2 / R) \\
17	\midrule
18	\multirow{4}{*}{$\pi_{0.5}$}
19	& Object  & \textbf{98.2} & 98.2 / 74.0 & \textbf{98.2} / 9.0 & 55.0 / 74.0 & 33.4 / 69.4 \\
20	& Spatial & \textbf{97.2} & \textbf{97.8} / 76.4 & 95.0 / 54.6 & 67.0 / 74.4 & 55.6 / 71.6 \\
21	& Goal    & \textbf{96.4} & 89.4 / 84.0 & 90.6 / 62.2 & 71.2 / 78.2 & 59.2 / 73.6 \\
22	& Long    & \textbf{91.6} & 86.8 / 61.2 & 80.4 / 33.6 & 63.2 / 64.6 & 51.7 / 50.4 \\
23	\midrule
24	\multirow{4}{*}{X-VLA}
25	& Object  & \textbf{99.2} & 99.0 / 98.8 & 97.6 / 97.8 & 56.2 / 65.2 & 43.4 / 70.6 \\
26	& Spatial & \textbf{93.0} & 71.6 / 70.2 & 78.8 / 77.8 & 72.0 / -- & 58.8 / 71.4 \\
27	& Goal    & \textbf{98.4} & 53.8 / 54.0 & 70.2 / 70.6 & 53.4 / 57.2 & 59.0 / 67.2 \\
28	& Long    & \textbf{94.0} & 47.0 / 48.2 & 27.5 / 29.6 & -- / -- & 45.0 / 61.6 \\
29	\midrule
30	\multirow{4}{*}{OpenVLA}
31	& Object  & \textbf{74.0} & 70.6 / -- & 70.6 / 62.8 / 61.4\textsuperscript{$\dagger$} & -- / -- & 39.2 / 35.8 \\
32	& Goal    & \textbf{74.8} & -- / -- & 74.8 / 79.6 / 73.2\texts
…[truncated 37517 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_bib_audit_fixes_20260528T171451",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-28T17:17:48.479774+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_bib_audit_fixes_20260528T171451",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-28T17:17:48.479931+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:exp_setup}
6	
7	We evaluate vision token pruning across six VLA architectures spanning three connector families on LIBERO~\cite{liu2023libero}, which provides four task suites of increasing complexity: Object, Spatial, Goal, and Long (10 tasks $\times$ 50 episodes each).
8	
9	Four models are evaluated in closed-loop control: $\pi_{0.5}$~\cite{black2025pi05} (4B, linear projection, 768 tokens, CV$\,{=}\,$0.055), X-VLA~\cite{zheng2025xvla} (0.9B, linear + 12-layer BART encoder, 50 tokens, CV$\,{=}\,$0.151), OpenVLA~\cite{kim2024openvla} (7B, 3-layer MLP, 256 tokens, CV$\,{=}\,$0.215), and SmolVLA~\cite{shukor2025smolvla} (450M, pixel-shuffle $4{\times}4$, 128 tokens, CV$\,{=}\,$0.314). Two additional models ($\pi_{0}$~\cite{black2024pi0}, OFT~\cite{kim2025openoft}) are analyzed via offline metrics only. Table~\ref{tab:model_properties} summarizes all six architectures. We prune at $k \in \{0.3, 0.5, 0.7, 0.85, 0.9, 0.95\}$, reporting mean success rate (SR) over 500 episodes.
10	
11	\subsection{Two-Axis Framework Overview}
12	\label{sec:two_axis}
13	
14	\begin{figure}[t]
15	\centering
16	\includegraphics[width=0.75\linewidth]{figures/paper/fig_pruning_overview.pdf}
17	\caption{Pruning degradation on LIBERO-Object (L2 norm scoring). $\pi_{0.5}$ maintains ${\geq}$98\% through $k{=}0.85$, OpenVLA degrades linearly, X-VLA cliffs at $k{=}0.7$, SmolVLA collapses to 0\% at $k{=}0.95$.}
18	\label{fig:pruning_overview}
19	\end{figure}
20	
21	Three qualitatively distinct response patterns emerge across the connector spectrum (Table~\ref{tab:main_results}; Figure~\ref{fig:pruning_overview}); a fourth (OpenVLA, MLP connector) is detailed in Appendix Table~\ref{tab:full_results}.
22	
23	\textbf{$\pi_{0.5}$ (linear, CV$\,{=}\,$0.055).} Low-CV models are \emph{uniformly critical}: which tokens are removed matters more than how many. L2 maintains ${\geq}$98.0\% through $k{=}0.85$, while
…[truncated 7861 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_bib_audit_fixes_20260528T171451",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-28T17:17:48.480079+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/analysis.tex",
  "limit": "300"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_bib_audit_fixes_20260528T171451",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/analysis.tex",
    "limit": "300"
  }
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-28T17:17:48.480230+00:00_

1	\section{Discussion}
2	\label{sec:analysis}
3	
4	CV predicts connector-level compressibility, but task complexity determines \emph{which} scoring method succeeds within a given connector. On OpenVLA, L2 leads on single-step Object ($+$7.8\,pp at $k{=}0.9$) but the hierarchy inverts on multi-step Long, where Random outperforms both L2 and attention at $k{=}0.7$ (Appendix~\ref{app:extended_discussion}). The monotonic L2 curve versus the non-monotonic random curve on $\pi_{0.5}$ Long (Figure~\ref{fig:cliff_highlight}) reflects position encoding sensitivity: L2 preserves spatial locality after re-indexing, while random creates scattered gaps that maximally disrupt RoPE at $k{\approx}0.9$ before recovering at $k{\leq}0.7$ as surviving positions become approximately uniform (Appendix~\ref{app:extended_discussion}).
5	
6	\paragraph{Limitations.}
7	All evaluations use LIBERO simulation; we provide no sim-to-real evidence. The six architectures differ in backbone, encoder, and scale beyond the connector, preventing causal isolation. The CV--SR correlation relies on four closed-loop models, too few for a general law. VTR is validated on SmolVLA only. Most conditions use a single seed; $\pi_{0.5}$ Long uses five-seed means ($n{=}5$, sample s.d.\ ${\leq}$2.7\,pp; Appendix~\ref{app:pi05_long_multiseed}); cross-seed validation on other models shows $\Delta \leq 5.8$\,pp (Appendix~\ref{app:pi05_multiseed},~\ref{app:openvla_multiseed}). Extended discussion in Appendix~\ref{app:extended_discussion}.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_bib_audit_fixes_20260528T171451",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-28T17:17:48.480370+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_bib_audit_fixes_20260528T171451",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/conclusion.tex"
  }
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-28T17:17:48.480488+00:00_

1	\section{Discussion and Conclusion}
2	\label{sec:conclusion}
3	\label{sec:analysis}
4	
5	CV predicts connector-level compressibility, but task complexity determines \emph{which} scoring method succeeds within a given connector---L2 leads on $\pi_{0.5}$ Object but inverts on Long; on X-VLA, attention recovers near-baseline while L2 is anti-informative (Appendix~\ref{app:extended_discussion}). The V-shaped random recovery on $\pi_{0.5}$ Long reflects position encoding sensitivity: scattered gaps maximally disrupt RoPE at $k{\approx}0.9$, recovering as surviving positions become approximately uniform.
6	
7	Connector architecture is the primary factor governing VLA token compressibility. Token-independent connectors degrade gracefully; entangling connectors exhibit catastrophic cliffs amplified by task complexity ($20{\times}$ from Object to Goal). CV partitions models in a single forward pass. Under sufficient compression, scoring effectiveness becomes connector- and $k$-dependent. Where all deletion fails, VTR recovers over 60\% SR at 75\% compression. Real-robot validation and adaptive per-task pruning schedules remain open.
8	
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_bib_audit_fixes_20260528T171451",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-28T17:17:48.480617+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_bib_audit_fixes_20260528T171451",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/abstract.tex"
  }
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-28T17:17:48.480734+00:00_

1	\begin{abstract}
2	Vision-Language-Action (VLA) models encode observations as hundreds of vision tokens, creating a computational bottleneck for real-time robotic control. Token pruning offers a training-free remedy, yet its effect varies dramatically across architectures: at retention ratio $k{=}0.95$, $\pi_{0.5}$ preserves 98\% task success while SmolVLA collapses to 0\%---why?
3	
4	We identify the vision-language connector as the primary architectural factor governing pruning tolerance. The coefficient of variation (CV) of post-connector token norms, computable in a single forward pass, predicts compressibility across the full architecture spectrum: from CV$\,{=}\,$0.038 (near-immune linear projection) to CV$\,{=}\,$0.314 (catastrophic pixel-shuffle collapse). Across five VLA architectures (450\,M--7\,B parameters) and four LIBERO manipulation suites, token-independent connectors degrade gracefully, while token-entangling connectors exhibit abrupt cliffs: SmolVLA collapses when just 6 of 128 tokens are removed.
5	
6	Importance-based selection is not universally beneficial---it can be actively harmful. L2 norm selection preserves 98\% success on $\pi_{0.5}$ where random yields 5\% (93\,pp gap); at aggressive ratios, random outperforms L2 by up to 36\,pp. No scoring method is universally safe: task complexity amplifies connector-dependent patterns ($20{\times}$ from Object to Goal). A zero-mask ablation isolates the mechanism: zeroing 10\% of tokens preserves 98.0\% SR while physical removal collapses to 9.0\%---the 89\,pp gap is entirely attributable to position disruption, not information loss. For architectures where all deletion fails, a lightweight re-encoding module (${\sim}$5\% extra parameters) recovers $>$60\% success at 75\% compression.
7	\end{abstract}
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_bib_audit_fixes_20260528T171451",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-28T17:17:48.480892+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/sections/related_work_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_bib_audit_fixes_20260528T171451",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/sections/related_work_draft.tex"
  }
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-28T17:17:48.481091+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\subsection{Vision-Language-Action Models}
5	
6	Recent advances in foundation models have enabled a new class of robotic policies that map visual observations and language instructions directly to actions. RT-2~\cite{brohan2023rt2} first demonstrated that fine-tuning large vision-language models on robot demonstrations transfers web-scale semantic knowledge to robotic control; it tokenizes actions as text and trains jointly on internet and robot data. Octo~\cite{ghosh2024octo} introduced a modular transformer backbone trained on 800k trajectories from the Open X-Embodiment dataset, with flexible adaptation to new observation spaces and embodiments. OpenVLA~\cite{kim2024openvla} scaled this paradigm to 7B parameters with a fused SigLIP-DinoV2 visual encoder and an MLP projector that maps visual embeddings into the Llama~2 input space; it outperforms RT-2-X (55B) by 16.5\% in absolute success rate with 7$\times$ fewer parameters. SmolVLA~\cite{shukor2025smolvla} pursued the opposite end of the efficiency spectrum: a 450M-parameter model that combines aggressive pixel shuffle compression (64 visual tokens per frame) with a flow-matching action expert, and matches or exceeds larger VLAs on both simulation and real-world benchmarks. $\pi_0$~\cite{black2024pi0} and $\pi_{0.5}$~\cite{physicalintelligence2025pi05} built on PaLiGemma with a separate action expert connected via cross-attention and produce smooth 50Hz action trajectories through flow matching.
7	
8	A critical but underexplored dimension across these models is the \emph{vision connector}: the module that bridges the visual encoder and the language/action backbone. OpenVLA and LLaVA~\cite{liu2023llava} use per-patch MLP projectors that preserve the spatial independence of each visual token. SmolVLA and InternVL~\cite{chen2024internvl} employ pixel shuffle (space-to-depth) connectors that fold spatial neighborhoods into channel dimensions before projection,
…[truncated 7011 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_bib_audit_fixes_20260528T171451",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 52 · 2026-05-28T17:17:48.481305+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper && find . -name \"*.tex\" -type f -exec grep -h \"\\\\\\\\cite[tp]*{[^}]*}\" {} \\; | sed 's/.*\\\\cite[tp]*{\\([^}]*\\)}.*/\\1/g' | tr ',' '\\n' | sed 's/^[[:space:]]*//;s/[[:space:]]*$//' | sort -u"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_bib_audit_fixes_20260528T171451",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper && find . -name \"*.tex\" -type f -exec grep -h \"\\\\\\\\cite[tp]*{[^}]*}\" {} \\; | sed 's/.*\\\\cite[tp]*{\\([^}]*\\)}.*/\\1/g' | tr ',' '\\n' | sed 's/^[[:space:]]*//;s/[[:space:]]*$//' | sort -u"
  }
}
```

</details>

---

### Tool result

_source line 53 · 2026-05-28T17:17:48.481437+00:00_

abnar2020quantifying
alayrac2022flamingo
black2024pi0
black2025pi05
bolya2023tome
brohan2023rt2
chen2024fastv
chen2024internvl
cheng2026vlaiap
gao2025compressorvla
karl2024negative
kim2024openvla
kim2025openoft
lewis2020bart
li2024cogact
liang2022evit
lipman2023flow
liu2023libero
liu2025vlapruner
physicalintelligence2025pi05
rao2021dynamicvit
shi2016subpixel
shukor2025smolvla
su2024roformer
xu2025vlacache
yang2024qwen2
yang2025efficientvla
zeng2023transformers_tsf
zhai2023siglip
zhang2023h2o
zheng2025xvla

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_bib_audit_fixes_20260528T171451",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 54 · 2026-05-28T17:17:48.481570+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper && find . -name \"*.tex\" -type f -exec grep -h \"\\\\\\\\cite[tp]*{[^}]*}\" {} \\; | grep -o \"\\\\\\\\cite[tp]*{[^}]*}\" | sed 's/.*{\\([^}]*\\)}/\\1/g' | tr ',' '\\n' | sed 's/^[[:space:]]*//;s/[[:space:]]*$//' | sort | uniq -c | sort -rn"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_bib_audit_fixes_20260528T171451",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper && find . -name \"*.tex\" -type f -exec grep -h \"\\\\\\\\cite[tp]*{[^}]*}\" {} \\; | grep -o \"\\\\\\\\cite[tp]*{[^}]*}\" | sed 's/.*{\\([^}]*\\)}/\\1/g' | tr ',' '\\n' | sed 's/^[[:space:]]*//;s/[[:space:]]*$//' | sort | uniq -c | sort -rn"
  }
}
```

</details>

---

### Tool result

_source line 55 · 2026-05-28T17:17:48.481693+00:00_

     15 shukor2025smolvla
     15 bolya2023tome
     13 liu2023libero
     13 kim2024openvla
     10 zhai2023siglip
     10 rao2021dynamicvit
     10 black2024pi0
      9 liang2022evit
      7 yang2025efficientvla
      7 kim2025openoft
      7 cheng2026vlaiap
      7 black2025pi05
      6 zheng2025xvla
      6 xu2025vlacache
      6 li2024cogact
      4 li2023blip2
      4 lewis2020bart
      4 chen2024fastv
      3 yang2024qwen2
      3 liu2025vlapruner
      3 liu2023llava
      3 brohan2023rt2
      3 alayrac2022flamingo
      2 oquab2023dinov2
      2 lipman2023flow
      2 chen2024internvl
      1 zhang2023h2o
      1 zeng2023transformers_tsf
      1 yin2022avit
      1 su2024roformer
      1 shi2016subpixel
      1 shang2024prumerge
      1 physicalintelligence2025pi05
      1 karl2024negative
      1 jiang2026lightvla
      1 ghosh2024octo
      1 gao2025compressorvla
      1 abnar2020quantifying

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_bib_audit_fixes_20260528T171451",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 56 · 2026-05-28T17:17:48.481824+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper && find . -name \"*.tex\" -type f -exec grep -h \"\\\\\\\\cite[tp]*{[^}]*}\" {} \\; | sed 's/.*\\\\cite[tp]*{\\([^}]*\\)}.*/\\1/g' | tr ',' '\\n' | sed 's/^[[:space:]]*//;s/[[:space:]]*$//' | sort -u"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_bib_audit_fixes_20260528T171451",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper && find . -name \"*.tex\" -type f -exec grep -h \"\\\\\\\\cite[tp]*{[^}]*}\" {} \\; | sed 's/.*\\\\cite[tp]*{\\([^}]*\\)}.*/\\1/g' | tr ',' '\\n' | sed 's/^[[:space:]]*//;s/[[:space:]]*$//' | sort -u"
  }
}
```

</details>

---

### Tool result

_source line 57 · 2026-05-28T17:17:48.481966+00:00_

abnar2020quantifying
alayrac2022flamingo
black2024pi0
black2025pi05
bolya2023tome
brohan2023rt2
chen2024fastv
chen2024internvl
cheng2026vlaiap
gao2025compressorvla
karl2024negative
kim2024openvla
kim2025openoft
lewis2020bart
li2024cogact
liang2022evit
lipman2023flow
liu2023libero
liu2025vlapruner
physicalintelligence2025pi05
rao2021dynamicvit
shi2016subpixel
shukor2025smolvla
su2024roformer
xu2025vlacache
yang2024qwen2
yang2025efficientvla
zeng2023transformers_tsf
zhai2023siglip
zhang2023h2o
zheng2025xvla

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_bib_audit_fixes_20260528T171451",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 58 · 2026-05-28T17:17:48.482191+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper && find . -name \"*.tex\" -type f -print0 | xargs -0 grep -h \"\\\\\\\\cite[tp]*{[^}]*}\" | sed 's/.*\\\\cite[tp]*{\\([^}]*\\)}.*/\\1/g' | tr ',' '\\n' | sed 's/^[[:space:]]*//;s/[[:space:]]*$//' | grep -v '^$' | sort -u"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_bib_audit_fixes_20260528T171451",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper && find . -name \"*.tex\" -type f -print0 | xargs -0 grep -h \"\\\\\\\\cite[tp]*{[^}]*}\" | sed 's/.*\\\\cite[tp]*{\\([^}]*\\)}.*/\\1/g' | tr ',' '\\n' | sed 's/^[[:space:]]*//;s/[[:space:]]*$//' | grep -v '^$' | sort -u"
  }
}
```

</details>

---

### Tool result

_source line 59 · 2026-05-28T17:17:48.482432+00:00_

abnar2020quantifying
alayrac2022flamingo
black2024pi0
black2025pi05
bolya2023tome
brohan2023rt2
chen2024fastv
chen2024internvl
cheng2026vlaiap
gao2025compressorvla
karl2024negative
kim2024openvla
kim2025openoft
lewis2020bart
li2024cogact
liang2022evit
lipman2023flow
liu2023libero
liu2025vlapruner
physicalintelligence2025pi05
rao2021dynamicvit
shi2016subpixel
shukor2025smolvla
su2024roformer
xu2025vlacache
yang2024qwen2
yang2025efficientvla
zeng2023transformers_tsf
zhai2023siglip
zhang2023h2o
zheng2025xvla

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_bib_audit_fixes_20260528T171451",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 60 · 2026-05-28T17:17:48.482661+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper && grep -rh \"oquab2023dinov2\\|yin2022avit\\|shang2024prumerge\\|jiang2026lightvla\\|ghosh2024octo\\|li2023blip2\\|liu2023llava\" . --include=\"*.tex\" | head -5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_bib_audit_fixes_20260528T171451",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper && grep -rh \"oquab2023dinov2\\|yin2022avit\\|shang2024prumerge\\|jiang2026lightvla\\|ghosh2024octo\\|li2023blip2\\|liu2023llava\" . --include=\"*.tex\" | head -5"
  }
}
```

</details>

---

### Tool result

_source line 61 · 2026-05-28T17:17:48.482899+00:00_

\textbf{Linear projection.} $\pi_0$~\cite{black2024pi0} (3.3B, 256 tokens) maps SigLIP~\cite{zhai2023siglip} patches through a single linear layer; $\pi_0.5$~\cite{black2025pi05} (4B, 768 tokens from three cameras) adds a learned $\times\!\sqrt{d}$ scaling; X-VLA~\cite{zheng2025xvla} (880M, 50 tokens) augments its linear projection with a 12-layer BART encoder~\cite{lewis2020bart} that introduces cross-token mixing. \textbf{MLP projector.} OpenVLA~\cite{kim2024openvla} (7B, 256 tokens) fuses DINOv2~\cite{oquab2023dinov2} and SigLIP through a three-layer MLP; OFT~\cite{kim2025openoft} shares this connector (entropy comparison only); CogACT~\cite{li2024cogact} retains 74.2\% SR under 78\% pruning per EfficientVLA~\cite{yang2025efficientvla} (literature corroboration, not our evaluation). \textbf{Spatial folding.} SmolVLA~\cite{shukor2025smolvla} (450M, 128 tokens) applies pixel-shuffle ($4{\times}4$ folding) so each token encodes 16 contiguous patches.
OpenVLA uses a dual encoder combining DINOv2~\cite{oquab2023dinov2} and SigLIP~\cite{zhai2023siglip}. The two encoders produce complementary representations (self-supervised spatial features and language-aligned features) that are concatenated per patch position.
Recent advances in foundation models have enabled a new class of robotic policies that map visual observations and language instructions directly to actions. RT-2~\cite{brohan2023rt2} first demonstrated that fine-tuning large vision-language models on robot demonstrations transfers web-scale semantic knowledge to robotic control; it tokenizes actions as text and trains jointly on internet and robot data. Octo~\cite{ghosh2024octo} introduced a modular transformer backbone trained on 800k trajectories from the Open X-Embodiment dataset, with flexible adaptation to new observation spaces and embodiments. OpenVLA~\cite{kim2024openvla} scaled this paradigm to 7B parameters with a fused SigLIP-DinoV2 visual encoder and an MLP projector that maps visual embeddings int
…[truncated 2378 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_bib_audit_fixes_20260528T171451",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 62 · 2026-05-28T17:17:48.483347+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper && find . -name \"*.tex\" -type f -print0 | xargs -0 grep -oh \"\\\\\\\\cite[tp]*{[^}]*}\" | sed 's/\\\\cite[tp]*{\\([^}]*\\)}/\\1/g' | tr ',' '\\n' | sed 's/^[[:space:]]*//;s/[[:space:]]*$//' | grep -v '^$' | sort -u"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_bib_audit_fixes_20260528T171451",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper && find . -name \"*.tex\" -type f -print0 | xargs -0 grep -oh \"\\\\\\\\cite[tp]*{[^}]*}\" | sed 's/\\\\cite[tp]*{\\([^}]*\\)}/\\1/g' | tr ',' '\\n' | sed 's/^[[:space:]]*//;s/[[:space:]]*$//' | grep -v '^$' | sort -u"
  }
}
```

</details>

---

### Tool result

_source line 63 · 2026-05-28T17:17:48.483551+00:00_

abnar2020quantifying
alayrac2022flamingo
black2024pi0
black2025pi05
bolya2023tome
brohan2023rt2
chen2024fastv
chen2024internvl
cheng2026vlaiap
gao2025compressorvla
ghosh2024octo
jiang2026lightvla
karl2024negative
kim2024openvla
kim2025openoft
lewis2020bart
li2023blip2
li2024cogact
liang2022evit
lipman2023flow
liu2023libero
liu2023llava
liu2025vlapruner
oquab2023dinov2
physicalintelligence2025pi05
rao2021dynamicvit
shang2024prumerge
shi2016subpixel
shukor2025smolvla
su2024roformer
xu2025vlacache
yang2024qwen2
yang2025efficientvla
yin2022avit
zeng2023transformers_tsf
zhai2023siglip
zhang2023h2o
zheng2025xvla

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_bib_audit_fixes_20260528T171451",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-28T17:17:48.483725+00:00_

Perfect! Now I have the complete deduplicated list. Let me format it nicely:

Based on my comprehensive search of all .tex files in `/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/`, here is the complete deduplicated sorted list of all citation keys referenced:

1. abnar2020quantifying
2. alayrac2022flamingo
3. black2024pi0
4. black2025pi05
5. bolya2023tome
6. brohan2023rt2
7. chen2024fastv
8. chen2024internvl
9. cheng2026vlaiap
10. gao2025compressorvla
11. ghosh2024octo
12. jiang2026lightvla
13. karl2024negative
14. kim2024openvla
15. kim2025openoft
16. lewis2020bart
17. li2023blip2
18. li2024cogact
19. liang2022evit
20. lipman2023flow
21. liu2023libero
22. liu2023llava
23. liu2025vlapruner
24. oquab2023dinov2
25. physicalintelligence2025pi05
26. rao2021dynamicvit
27. shang2024prumerge
28. shi2016subpixel
29. shukor2025smolvla
30. su2024roformer
31. xu2025vlacache
32. yang2024qwen2
33. yang2025efficientvla
34. yin2022avit
35. zeng2023transformers_tsf
36. zhai2023siglip
37. zhang2023h2o
38. zheng2025xvla

**Total: 38 unique citation keys**

The most frequently cited works are:
- shukor2025smolvla (15 occurrences)
- bolya2023tome (15 occurrences)
- liu2023libero (13 occurrences)
- kim2024openvla (13 occurrences)
- zhai2023siglip (10 occurrences)
- rao2021dynamicvit (10 occurrences)
- black2024pi0 (10 occurrences)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_bib_audit_fixes_20260528T171451",
  "tool": "Agent",
  "elapsed_ms": 7
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-28T17:17:48.483925+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/references.bib",
  "old_string": "  author={Zheng, Yifu and Li, Zhihao and Wang, Shengjie and Wang, Jianxiong and others},",
  "new_string": "  author={Zheng, Jinliang and Li, Zhihao and Wang, Shengjie and Wang, Jianxiong and others},"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_bib_audit_fixes_20260528T171451",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/references.bib",
    "old_string": "  author={Zheng, Yifu and Li, Zhihao and Wang, Shengjie and Wang, Jianxiong and others},",
    "new_string": "  author={Zheng, Jinliang and Li, Zhihao and Wang, Shengjie and Wang, Jianxiong and others},"
  }
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-28T17:17:48.484123+00:00_

The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/references.bib has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_bib_audit_fixes_20260528T171451",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 67 · 2026-05-28T17:17:48.484301+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/references.bib",
  "old_string": "@inproceedings{chen2024fastv,\n  title={An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models},\n  author={Chen, Liang and others},\n  booktitle={European Conference on Computer Vision (ECCV)},\n  year={2024},\n  note={Oral presentation}\n}",
  "new_string": "@inproceedings{chen2024fastv,\n  title={An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models},\n  author={Chen, Liang and Zhao, Haozhe and Liu, Tianyu and Bai, Shuai and Lin, Junyang and Zhou, Chang and Chang, Baobao},\n  booktitle={European Conference on Computer Vision (ECCV)},\n  year={2024},\n  eprint={2403.06764},\n  archivePrefix={arXiv},\n  note={Oral presentation}\n}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_bib_audit_fixes_20260528T171451",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/references.bib",
    "old_string": "@inproceedings{chen2024fastv,\n  title={An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models},\n  author={Chen, Liang and others},\n  booktitle={European Conference on Computer Vision (ECCV)},\n  year={2024},\n  note={Oral presentation}\n}",
    "new_string": "@inproceedings{chen2024fastv,\n  title={An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models},\n  author={Chen, Liang and Zhao, Haozhe and Liu, Tianyu and Bai, Shuai and Lin, Junyang and Zhou, Chang and Chang, Baobao},\n  booktitle={European Conference on Computer Vision (ECCV)},\n  year={2024},\n  eprint={2403.06764},\n  archivePrefix={arXiv},\n  note={Oral presentation}\n}"
  }
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-28T17:17:48.484515+00:00_

The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/references.bib has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_bib_audit_fixes_20260528T171451",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-28T17:17:48.484653+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/references.bib",
  "old_string": "@article{black2025pi05,\n  title={$\\pi_{0.5}$: a Vision-Language-Action Model with Open-World Generalization},\n  author={Black, Kevin and Brown, Noah and Shafiullah, Nur Muhammad Mahi and others},\n  journal={arXiv preprint arXiv:2504.16054},\n  year={2025},\n  eprint={2504.16054},\n  archivePrefix={arXiv}\n}",
  "new_string": "@inproceedings{black2025pi05,\n  title={$\\pi_{0.5}$: a Vision-Language-Action Model with Open-World Generalization},\n  author={Black, Kevin and Brown, Noah and Shafiullah, Nur Muhammad Mahi and others},\n  booktitle={Proceedings of The 9th Conference on Robot Learning (CoRL)},\n  series={Proceedings of Machine Learning Research},\n  volume={305},\n  pages={17--40},\n  year={2025},\n  publisher={PMLR},\n  eprint={2504.16054},\n  archivePrefix={arXiv}\n}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_bib_audit_fixes_20260528T171451",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/references.bib",
    "old_string": "@article{black2025pi05,\n  title={$\\pi_{0.5}$: a Vision-Language-Action Model with Open-World Generalization},\n  author={Black, Kevin and Brown, Noah and Shafiullah, Nur Muhammad Mahi and others},\n  journal={arXiv preprint arXiv:2504.16054},\n  year={2025},\n  eprint={2504.16054},\n  archivePrefix={arXiv}\n}",
    "new_string": "@inproceedings{black2025pi05,\n  title={$\\pi_{0.5}$: a Vision-Language-Action Model with Open-World Generalization},\n  author={Black, Kevin and Brown, Noah and Shafiullah, Nur Muhammad Mahi and others},\n  booktitle={Proceedings of The 9th Conference on Robot Learning (CoRL)},\n  series={Proceedings of Machine Learning Research},\n  volume={305},\n  pages={17--40},\n  year={2025},\n  publisher={PMLR},\n  eprint={2504.16054},\n  archivePrefix={arXiv}\n}"
  }
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-28T17:17:48.484849+00:00_

The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/references.bib has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_bib_audit_fixes_20260528T171451",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 71 · 2026-05-28T17:17:48.484994+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/references.bib",
  "offset": "126",
  "limit": "20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_bib_audit_fixes_20260528T171451",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/references.bib",
    "offset": "126",
    "limit": "20"
  }
}
```

</details>

---

### Tool result

_source line 72 · 2026-05-28T17:17:48.485126+00:00_

126	
127	@inproceedings{black2025pi05,
128	  title={$\pi_{0.5}$: a Vision-Language-Action Model with Open-World Generalization},
129	  author={Black, Kevin and Brown, Noah and Shafiullah, Nur Muhammad Mahi and others},
130	  booktitle={Proceedings of The 9th Conference on Robot Learning (CoRL)},
131	  series={Proceedings of Machine Learning Research},
132	  volume={305},
133	  pages={17--40},
134	  year={2025},
135	  publisher={PMLR},
136	  eprint={2504.16054},
137	  archivePrefix={arXiv}
138	}
139	
140	@inproceedings{ghosh2024octo,
141	  title={Octo: An Open-Source Generalist Robot Policy},
142	  author={{Octo Model Team} and Ghosh, Dibya and Walke, Homer and Pertsch, Karl and Black, Kevin and others},
143	  booktitle={Robotics: Science and Systems (RSS)},
144	  year={2024}
145	}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_bib_audit_fixes_20260528T171451",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 73 · 2026-05-28T17:17:48.485303+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/references.bib",
  "offset": "154",
  "limit": "15"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_bib_audit_fixes_20260528T171451",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/references.bib",
    "offset": "154",
    "limit": "15"
  }
}
```

</details>

---

### Tool result

_source line 74 · 2026-05-28T17:17:48.485442+00:00_

154	
155	% ============================================================
156	% VLM/LLM Token Efficiency
157	% ============================================================
158	
159	@inproceedings{chen2024fastv,
160	  title={An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models},
161	  author={Chen, Liang and Zhao, Haozhe and Liu, Tianyu and Bai, Shuai and Lin, Junyang and Zhou, Chang and Chang, Baobao},
162	  booktitle={European Conference on Computer Vision (ECCV)},
163	  year={2024},
164	  eprint={2403.06764},
165	  archivePrefix={arXiv},
166	  note={Oral presentation}
167	}
168	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_bib_audit_fixes_20260528T171451",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 75 · 2026-05-28T17:17:48.485568+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/references.bib",
  "offset": "358",
  "limit": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_bib_audit_fixes_20260528T171451",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/references.bib",
    "offset": "358",
    "limit": "10"
  }
}
```

</details>

---

### Tool result

_source line 76 · 2026-05-28T17:17:48.485689+00:00_

358	  journal={arXiv preprint arXiv:2407.02392},
359	  year={2024},
360	  eprint={2407.02392},
361	  archivePrefix={arXiv}
362	}
363	
364	@inproceedings{zheng2025xvla,
365	  title={{X-VLA}: Soft-Prompted Transformer as Scalable Cross-Embodiment Vision-Language-Action Model},
366	  author={Zheng, Jinliang and Li, Zhihao and Wang, Shengjie and Wang, Jianxiong and others},
367	  booktitle={International Conference on Learning Representations (ICLR)},

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_bib_audit_fixes_20260528T171451",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 77 · 2026-05-28T17:17:48.485850+00:00_

三项修改均已生效。

## 改动摘要

### Critical — 已修复
1. **`zheng2025xvla`** (line 366): 第一作者 `Zheng, Yifu` → `Zheng, Jinliang`

### Warning — 已修复
2. **`chen2024fastv`** (line 159-167): 作者列表从 `Chen, Liang and others` 补全为 7 位完整作者：Chen, Liang; Zhao, Haozhe; Liu, Tianyu; Bai, Shuai; Lin, Junyang; Zhou, Chang; Chang, Baobao。同时补充了 eprint 字段。

3. **`black2025pi05`** (line 127-138): 从 `@article`(arXiv preprint）转为 `@inproceedings`（CoRL 2025 正式发表），新增 `booktitle`, `series=PMLR`, `volume=305`, `pages=17--40`, `publisher=PMLR`。

### Orphan 条目（26 条，保留未删除）

以下 bib key 在 `references.bib` 中定义但未被任何 `.tex` 文件引用：

`wang2025specprunevla`, `feng2026seewhatmatters`, `zhang2025sparsevlm`, `khaki2025sparsevila`, `jabbour2025dontrun`, `li2024roboflamingo`, `brohan2023rt1`, `jaegle2021perceiver`, `li2024tokenpacker`, `wen2024tinyvla`, `ryoo2021tokenlearner`, `meng2022adavit`, `chen2023sparsevit`, `ye2025fitprune`, `shi2024crossget`, `zhang2024fastervlm`, `liu2024llava15`, `chen2024internvl25`, `gao2024miniinternvl`, `zitkovich2023rt2`, `openxembodiment2024`, `xiao2024streamingllm`, `mees2022calvin`, `chi2023diffusionpolicy`, `bouthillier2024negative`, `oquab2024dinov2`

另外，tex 中引用了 `karl2024negative` 和 `physicalintelligence2025pi05` 两个 key，但 bib 中不存在对应条目——这属于 missing citation，非本次任务范围。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_fix_bib_audit_fixes_20260528T171451"
}
```

</details>

---
