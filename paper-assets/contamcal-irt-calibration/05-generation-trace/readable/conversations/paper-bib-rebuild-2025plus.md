# paper bib rebuild 2025plus

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 81
- **Recorded user turns:** 0
- **Tool calls:** 40
- **Original source:** `logs/chats/worker_paper_bib_rebuild_2025plus_20260517T051927.jsonl`
- **Structured JSON:** [`fccee2ebf254532d17fa.json`](../../sessions/fc/fccee2ebf254532d17fa.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

81 recorded events

### Tool call

_source line 1 · 2026-05-17T05:24:49.032199+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

````json
{
  "description": "Verify 2025+ bib entries",
  "prompt": "I need to verify and rebuild bibtex entries for 2025+ year citations in an academic paper. The task involves:\n\n1. Reading the current bib file and tex files to understand citation context\n2. WebSearching each entry to verify correctness (many are AI hallucinations)\n3. Producing correct bibtex entries\n\n**Working directory**: /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/\n\n**Steps**:\n\nFirst, read the current references.bib to see existing entries for these keys:\n- chang2025benchmarking\n- duan2025minkpp\n- habba_2025_growing_pains\n- li2025dcr / li_2025_dcr\n- luettgau_2025_hibayes\n- polo2026growing\n- xu2025emperor\n- wust2025selfcritique / wust_2025_selfcritique\n\nThen grep all .tex files for each key to understand citation context.\n\nThen WebSearch each one to find the real paper. For each:\n- Search the title + key terms\n- Find: correct title, all authors, year, venue/arXiv ID\n- Generate correct bibtex\n\n**Special cases**:\n- `wust2025selfcritique` / `wust_2025_selfcritique`: CONFIRMED HALLUCINATION. Replace with: Tao et al. \"Detecting Data Contamination from Reinforcement Learning Post-training for Large Language Models\", ICLR 2026, arXiv 2510.09259. WebSearch to confirm full author list.\n- Add NEW entry: Kadavath et al. 2022 \"Language Models (Mostly) Know What They Know\" — key: `kadavath_2022_self_eval`. WebSearch to confirm details.\n\n**Output**: Write the file `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/bib_rebuild_2025plus.bib`\n\nFormat each entry with a comment header:\n```\n% KEY: xxx | STATUS: VERIFIED/NOT_FOUND/REPLACED | SOURCE: arXiv XXXX.XXXXX or venue\n@article{...}\n```\n\nFor entries that can't be found, mark STATUS: NOT_FOUND and suggest alternatives.\n\nIMPORTANT: Actually perform WebSearches to verify each entry. Do not guess or fabricate information.",
  "subagent_type": "general-purpose"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "worker_paper_bib_rebuild_2025plus_20260517T051927",
  "tool": "Agent",
  "tool_args": {
    "description": "Verify 2025+ bib entries",
    "prompt": "I need to verify and rebuild bibtex entries for 2025+ year citations in an academic paper. The task involves:\n\n1. Reading the current bib file and tex files to understand citation context\n2. WebSearching each entry to verify correctness (many are AI hallucinations)\n3. Producing correct bibtex entries\n\n**Working directory**: /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/\n\n**Steps**:\n\nFirst, read the current references.bib to see existing entries for these keys:\n- chang2025benchmarking\n- duan2025minkpp\n- habba_2025_growing_pains\n- li2025dcr / li_2025_dcr\n- luettgau_2025_hibayes\n- polo2026growing\n- xu2025emperor\n- wust2025selfcritique / wust_2025_selfcritique\n\nThen grep all .tex files for each key to understand citation context.\n\nThen WebSearch each one to find the real paper. For each:\n- Search the title + key terms\n- Find: correct title, all authors, year, venue/arXiv ID\n- Generate correct bibtex\n\n**Special cases**:\n- `wust2025selfcritique` / `wust_2025_selfcritique`: CONFIRMED HALLUCINATION. Replace with: Tao et al. \"Detecting Data Contamination from Reinforcement Learning Post-training for Large Language Models\", ICLR 2026, arXiv 2510.09259. WebSearch to confirm full author list.\n- Add NEW entry: Kadavath et al. 2022 \"Language Models (Mostly) Know What They Know\" — key: `kadavath_2022_self_eval`. WebSearch to confirm details.\n\n**Output**: Write the file `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/bib_rebuild_2025plus.bib`\n\nFormat each entry with a comment header:\n```\n% KEY: xxx | STATUS: VERIFIED/NOT_FOUND/REPLACED | SOURCE: arXiv XXXX.XXXXX or venue\n@article{...}\n```\n\nFor entries that can't be found, mark STATUS: NOT_FOUND and suggest alternatives.\n\nIMPORTANT: Actually perform WebSearches to verify each entry. Do not guess or fabricate information.",
    "subagent_type": "general-purpose"
  }
}
````

</details>

---

### Tool call

_source line 2 · 2026-05-17T05:24:49.032674+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_bib_rebuild_2025plus_20260517T051927",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/references.bib"
  }
}
```

</details>

---

### Tool result

_source line 3 · 2026-05-17T05:24:49.032991+00:00_

1	% ============================================================
2	% Literature Map Entries (keys from literature_map.yaml ids)
3	% ============================================================
4	
5	@inproceedings{adams_1997_mrcml,
6	  author    = {Adams, Raymond J. and Wilson, Mark and Wang, Wen-chung},
7	  title     = {The Multidimensional Random Coefficients Multinomial Logit Model},
8	  booktitle = {Applied Psychological Measurement},
9	  volume    = {21},
10	  number    = {1},
11	  pages     = {1--23},
12	  year      = {1997}
13	}
14	
15	@article{angelopoulos_2023_conformal,
16	  author        = {Angelopoulos, Anastasios N. and Bates, Stephen},
17	  title         = {A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification},
18	  journal       = {Foundations and Trends in Machine Learning},
19	  year          = {2023},
20	  url           = {https://arxiv.org/abs/2107.07511}
21	}
22	
23	@article{brown_2024_ppp,
24	  author  = {Brown, Jeremy M. and Thomson, Robert C.},
25	  title   = {The Expected Behaviors of Posterior Predictive Tests and Their Unexpected Interpretation},
26	  journal = {Molecular Biology and Evolution},
27	  volume  = {41},
28	  number  = {3},
29	  pages   = {msae051},
30	  year    = {2024}
31	}
32	
33	@article{burnell_2023_structure,
34	  author        = {Burnell, Ryan and Schellaert, Wout and Burden, John and Ullman, Tomer D. and Martinez-Plumed, Fernando and Tenenbaum, Joshua B. and Rutar, Danaja and Murfet, Daniel and Zheng, Hananel and Hern\'{a}ndez-Orallo, Jos\'{e}},
35	  title         = {Revealing the Structure of Language Model Capabilities},
36	  journal       = {arXiv preprint},
37	  year          = {2023},
38	  eprint        = {2306.10062},
39	  archiveprefix = {arXiv},
40	  url           = {https://arxiv.org/abs/2306.10062}
41	}
42	
43	@inproceedings{carlini_2021_extracting,
44	  author    = {Carlini, Nicholas and Tramer, Florian and Wallace, Eric and Jagielski, Matthew and Herbert-Voss, Ariel an
…[truncated 42274 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_bib_rebuild_2025plus_20260517T051927",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-17T05:24:49.033179+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_bib_rebuild_2025plus_20260517T051927",
  "tool": "Glob",
  "tool_args": {
    "pattern": "*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-17T05:24:49.033336+00:00_

artifacts/paper_draft/main.tex
artifacts/paper_draft/method.tex
artifacts/paper_draft/experiments.tex
artifacts/paper_draft/results.tex
artifacts/paper_draft/related_work.tex
artifacts/paper_draft/discussion.tex
artifacts/paper_draft/introduction.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_bib_rebuild_2025plus_20260517T051927",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-17T05:24:49.033488+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "chang2025benchmarking|duan2025minkpp|habba_2025_growing_pains|li2025dcr|li_2025_dcr|luettgau_2025_hibayes|polo2026growing|xu2025emperor|wust2025selfcritique|wust_2025_selfcritique",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft",
  "glob": "*.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_bib_rebuild_2025plus_20260517T051927",
  "tool": "Grep",
  "tool_args": {
    "pattern": "chang2025benchmarking|duan2025minkpp|habba_2025_growing_pains|li2025dcr|li_2025_dcr|luettgau_2025_hibayes|polo2026growing|xu2025emperor|wust2025selfcritique|wust_2025_selfcritique",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft",
    "glob": "*.tex",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-17T05:24:49.033619+00:00_

artifacts/paper_draft/related_work.tex:10:[Omitted long matching line]
artifacts/paper_draft/related_work.tex:18:[Omitted long matching line]
artifacts/paper_draft/experiments.tex:36:[Omitted long matching line]
artifacts/paper_draft/method.tex:22:[Omitted long matching line]
artifacts/paper_draft/method.tex:72:This reveals a domain-method mismatch: IRT-based LLM evaluation typically pools $J = 8$--$30$ models \citep{polo2026growing,lalor2024irt}, well below the $J \geq 50$ regime where $\gamma$ recovery is reliable. This structural gap is itself a central finding (\S\ref{sec:results}).
artifacts/paper_draft/introduction.tex:3:[Omitted long matching line]
artifacts/paper_draft/introduction.tex:5:[Omitted long matching line]
artifacts/paper_draft/introduction.tex:7:[Omitted long matching line]
artifacts/paper_draft/results.tex:38:[Omitted long matching line]
artifacts/paper_draft/results.tex:53:[Omitted long matching line]
artifacts/paper_draft/results.tex:67:[Omitted long matching line]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_bib_rebuild_2025plus_20260517T051927",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-17T05:24:49.033753+00:00_

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
  "session": "worker_paper_bib_rebuild_2025plus_20260517T051927",
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

_source line 9 · 2026-05-17T05:24:49.033869+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_bib_rebuild_2025plus_20260517T051927",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-17T05:24:49.033994+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Chang Yupeng \"A Survey on Evaluation of Large Language Models\" 2024 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_bib_rebuild_2025plus_20260517T051927",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Chang Yupeng \"A Survey on Evaluation of Large Language Models\" 2024 arXiv"
  }
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-17T05:24:49.034122+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Min-K%++ \"Improved Baseline for Detecting Pre-Training Data\" Zhang Jingyang 2024 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_bib_rebuild_2025plus_20260517T051927",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Min-K%++ \"Improved Baseline for Detecting Pre-Training Data\" Zhang Jingyang 2024 arXiv"
  }
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-17T05:24:49.034258+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Growing Pains\" IRT LLM evaluation Polo Felipe Maia 2025 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_bib_rebuild_2025plus_20260517T051927",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Growing Pains\" IRT LLM evaluation Polo Felipe Maia 2025 arXiv"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-17T05:24:49.034428+00:00_

Web search results for query: "Chang Yupeng "A Survey on Evaluation of Large Language Models" 2024 arXiv"

Links: [{"title":"[2307.03109] A Survey on Evaluation of Large Language Models","url":"https://arxiv.org/abs/2307.03109"},{"title":"[2307.03109v1] A Survey on Evaluation of Large Language Models","url":"https://arxiv.org/abs/2307.03109v1"},{"title":"111 A Survey on Evaluation of Large Language Models","url":"https://arxiv.org/pdf/2307.03109"},{"title":"A Survey on Evaluation of Large Language Models","url":"https://dl.acm.org/doi/pdf/10.1145/3641289"},{"title":"A Survey on Evaluation of Large Language Models","url":"https://arxiv.org/html/2307.03109v1"},{"title":"A Survey on Evaluation of Large Language Models | ACM Transactions on Intelligent Systems and Technology","url":"https://dl.acm.org/doi/full/10.1145/3641289"},{"title":"A Systematic Survey and Critical Review on Evaluating Large Language Models: Challenges, Limitations, and Recommendations","url":"https://arxiv.org/html/2407.04069v1"},{"title":"(PDF) A Survey on Evaluation of Large Language Models","url":"https://www.researchgate.net/publication/377639945_A_Survey_on_Evaluation_of_Large_Language_Models"},{"title":"Paper page - A Survey on Evaluation of Large Language Models","url":"https://huggingface.co/papers/2307.03109"},{"title":"GitHub - MLGroupJLU/LLM-eval-survey: The official GitHub page for the survey paper \"A Survey on Evaluation of Large Language Models\". · GitHub","url":"https://github.com/MLGroupJLU/LLM-eval-survey"}]

I found the paper you're looking for. Here are the search results:

## Paper Information

"A Survey on Evaluation of Large Language Models" is authored by Yupeng Chang, Xu Wang, Jindong Wang, Yuan Wu, Linyi Yang, Kaijie Zhu, Hao Chen, Xiaoyuan Yi, Cunxiang Wang, Yidong Wang, Wei Ye, Yue Zhang, Yi Chang, Philip S. Yu, Qiang Yang, and Xing Xie.

**Note:** The paper was initially published on arXiv as version 2307.03109 in July 2023. It was later published in March 2024 in ACM
…[truncated 721 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_bib_rebuild_2025plus_20260517T051927",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-17T05:24:49.034592+00:00_

Web search results for query: ""Growing Pains" IRT LLM evaluation Polo Felipe Maia 2025 arXiv"

Links: [{"title":"Growing Pains: Extensible and Efficient LLM Benchmarking Via Fixed Parameter Calibration","url":"https://arxiv.org/html/2604.12843"},{"title":"[2604.12843] Growing Pains: Extensible and Efficient LLM Benchmarking Via Fixed Parameter Calibration","url":"https://arxiv.org/abs/2604.12843"},{"title":"[2508.12792] Bridging Human and LLM Judgments: Understanding and Narrowing the Gap","url":"https://arxiv.org/abs/2508.12792"},{"title":"[2512.06553] A Latent Variable Framework for Scaling Laws in Large Language Models","url":"https://arxiv.org/abs/2512.06553"},{"title":"Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory","url":"https://arxiv.org/html/2505.15055v2"},{"title":"[2402.14992v2] tinyBenchmarks: evaluating LLMs with fewer examples","url":"https://arxiv.org/abs/2402.14992v2"},{"title":"Felipe Maia Polo's Post","url":"https://www.linkedin.com/posts/felipemaiapolo_ai-evaluation-llm-activity-7247597112882778112-bSeg"},{"title":"[2405.16236] A transfer learning framework for weak-to-strong generalization","url":"https://arxiv.org/abs/2405.16236"},{"title":"Toward a unified framework for data-efficient evaluation of large language models","url":"https://arxiv.org/html/2510.04051"},{"title":"A Psychometric Deep Dive into the Topic-Specific Medical ...","url":"https://arxiv.org/pdf/2509.24186"}]

I found the paper you were looking for! Here are the search results:

## "Growing Pains: Extensible and Efficient LLM Benchmarking Via Fixed Parameter Calibration"

The paper proposes a framework based on multidimensional Item Response Theory (IRT) that uses anchor items to calibrate new benchmarks to the evaluation suite while holding previously calibrated item parameters fixed.

The approach supports a realistic evaluation setting in which datasets are introduced over time and models are evaluated only on the datasets availab
…[truncated 862 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_bib_rebuild_2025plus_20260517T051927",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-17T05:24:49.034755+00:00_

Web search results for query: "Min-K%++ "Improved Baseline for Detecting Pre-Training Data" Zhang Jingyang 2024 arXiv"

Links: [{"title":"[2404.02936] Min-K%++: Improved Baseline for Detecting Pre-Training Data from Large Language Models","url":"https://arxiv.org/abs/2404.02936"},{"title":"Min-K%++: Improved Baseline for Detecting Pre-Training Data from Large Language Models | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/min-kpercent-improved-baseline-detecting-pre-training"},{"title":"Min-K%++: Improved Baseline for Detecting Pre-Training Data from Large Language Models","url":"https://arxiv.org/html/2404.02936v1"},{"title":"(PDF) Min-K%++: Improved Baseline for Detecting Pre-Training Data from Large Language Models (2024) | Jingyang Zhang | 16 Citations","url":"https://scispace.com/papers/min-k-improved-baseline-for-detecting-pre-training-data-from-1r3llgg58h"},{"title":"Paper page - Min-K%++: Improved Baseline for Detecting Pre-Training Data from Large Language Models","url":"https://huggingface.co/papers/2404.02936"},{"title":"(PDF) Min-K%++: Improved Baseline for Detecting Pre-Training Data from Large Language Models","url":"https://www.researchgate.net/publication/379541659_Min-K_Improved_Baseline_for_Detecting_Pre-Training_Data_from_Large_Language_Models"},{"title":"Min-K%++: Improved Baseline for Detecting Pre-Training Data from Large Language Models - 专知论文","url":"https://sl.zhuanzhi.ai/paper/e31511b756378dfdbb98e08410253633"},{"title":"publications | Jingyang Zhang - GitHub Pages","url":"https://zjysteven.github.io/publications/"},{"title":"fine-tuning can help detect pretraining data","url":"https://arxiv.org/pdf/2410.10880"},{"title":"GitHub - zjysteven/mink-plus-plus: [ICLR'25 Spotlight] Min-K%++: Improved baseline for detecting pre-training data of LLMs · GitHub","url":"https://github.com/zjysteven/mink-plus-plus"}]

I found the paper! Here are the search results for Min-K%++ by Jingyang Zhang et al.:

## Paper Overview

The 
…[truncated 1425 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_bib_rebuild_2025plus_20260517T051927",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-17T05:24:49.034908+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arXiv 2604.12843 authors \"Growing Pains\" Habba Maryam Polo Felipe"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_bib_rebuild_2025plus_20260517T051927",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arXiv 2604.12843 authors \"Growing Pains\" Habba Maryam Polo Felipe"
  }
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-17T05:24:49.035040+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Decontaminated Calibration and Ranking\" Li Yucheng LLM evaluation 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_bib_rebuild_2025plus_20260517T051927",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Decontaminated Calibration and Ranking\" Li Yucheng LLM evaluation 2025"
  }
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-17T05:24:49.035166+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arXiv 2505.05602 HiBayES hierarchical Bayesian AI evaluation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_bib_rebuild_2025plus_20260517T051927",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arXiv 2505.05602 HiBayES hierarchical Bayesian AI evaluation"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-17T05:24:49.035293+00:00_

Web search results for query: "arXiv 2604.12843 authors "Growing Pains" Habba Maryam Polo Felipe"

Links: [{"title":"[2604.12843] Growing Pains: Extensible and Efficient LLM Benchmarking Via Fixed Parameter Calibration","url":"https://arxiv.org/abs/2604.12843"},{"title":"Growing Pains: Extensible and Efficient LLM Benchmarking Via Fixed Parameter Calibration","url":"https://arxiv.org/html/2604.12843"},{"title":"Computer Science","url":"https://arxiv.org/list/cs/recent?skip=543&show=2000"},{"title":"[2602.12843] Thinking Like a Radiologist: A Dataset for Anatomy-Guided Interleaved Vision Language Reasoning in Chest X-ray Interpretation","url":"https://arxiv.org/abs/2602.12843"},{"title":"Arxiv","url":"https://arxiv.org/pdf/2406.12843"},{"title":"[2405.12843] OpenCarbonEval: A Unified Carbon Emission Estimation Framework in Large-Scale AI Models","url":"https://arxiv.org/abs/2405.12843"},{"title":"[2506.12843] Transforming Chatbot Text: A Sequence-to-Sequence Approach","url":"https://arxiv.org/abs/2506.12843"},{"title":"[2406.12843] Can Go AIs be adversarially robust?","url":"https://arxiv.org/abs/2406.12843"},{"title":"arXiv:2506.12843v1 [cs.CL] 15 Jun 2025 Transforming Chatbot Text: A","url":"https://arxiv.org/pdf/2506.12843"},{"title":"[2003.12843] A Close Look at Deep Learning with Small Data","url":"https://ar5iv.labs.arxiv.org/html/2003.12843"}]

Based on the search results, I found the paper you're looking for. arXiv paper 2604.12843 is titled "Growing Pains: Extensible and Efficient LLM Benchmarking Via Fixed Parameter Calibration".

However, regarding the author names you mentioned, the search results show that the authors are Eliya Habba, Itay Itzhak, Asaf Yehudai, Yotam Perlitz, Elron Bandel, Michal Shmueli-Scheuer, Leshem Choshen, and Gabriel Stanovsky. 

The names "Habba Maryam Polo Felipe" you mentioned don't match the actual author list for this paper. "Habba" appears to be part of the first author's name (Eliya Habba), but "Maryam Polo Felipe" are not 
…[truncated 138 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_bib_rebuild_2025plus_20260517T051927",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-17T05:24:49.035481+00:00_

Web search results for query: ""Decontaminated Calibration and Ranking" Li Yucheng LLM evaluation 2025"

Links: [{"title":"Benchmarking LLM accuracy for engineering QA systems | PatSnap","url":"https://www.patsnap.com/resources/blog/articles/benchmarking-llm-accuracy-for-engineering-qa-systems/"},{"title":"Accepted Findings Papers - EMNLP 2025","url":"https://2025.emnlp.org/program/find_papers/"},{"title":"LLM evaluation benchmarks and safety datasets for 2025 | RAIL Score Knowledge Hub","url":"https://responsibleailabs.ai/knowledge-hub/articles/llm-evaluation-benchmarks-2025"},{"title":"Benchmarking LLM accuracy for engineering technical QA | PatSnap","url":"https://www.patsnap.com/resources/blog/articles/benchmarking-llm-accuracy-for-engineering-technical-qa/"},{"title":"Language Ranker: A Metric for Quantifying LLM Performance Across High and Low-Resource Languages - New Jersey Institute of Technology","url":"https://researchwith.njit.edu/en/publications/language-ranker-a-metric-for-quantifying-llm-performance-across-h/"},{"title":"LLM Evaluation in 2025: Metrics, RAG, LLM-as-Judge & Best Practices | by QuarkAndCode | Medium","url":"https://medium.com/@QuarkAndCode/llm-evaluation-in-2025-metrics-rag-llm-as-judge-best-practices-ad2872cfa7cb"},{"title":"CalibJudge: Calibrated LLM-as-a-Judge for Multilingual ...","url":"https://www.preprints.org/manuscript/202603.1324"},{"title":"Evaluating and Calibrating LLM Confidence on Questions with Multiple Correct Answers","url":"https://arxiv.org/html/2602.07842v1"},{"title":"KNOWLEDGE DISTILLATION AS DECONTAMINATION? ...","url":"https://openreview.net/pdf?id=W8VCH9x1HZ"},{"title":"GitHub - SihengLi99/LLM-Honesty-Survey: [2025-TMLR] A Survey on the Honesty of Large Language Models · GitHub","url":"https://github.com/SihengLi99/LLM-Honesty-Survey"}]

Based on the web search results, I found relevant information about LLM evaluation and decontamination approaches in 2025, though the specific paper you mentioned wasn't directl
…[truncated 1421 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_bib_rebuild_2025plus_20260517T051927",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-17T05:24:49.035638+00:00_

Web search results for query: "arXiv 2505.05602 HiBayES hierarchical Bayesian AI evaluation"

Links: [{"title":"[2505.05602] HiBayES: A Hierarchical Bayesian Modeling Framework for AI Evaluation Statistics","url":"https://arxiv.org/abs/2505.05602"},{"title":"[2505.05602v2] HiBayES: A Hierarchical Bayesian Modeling Framework for AI Evaluation Statistics","url":"http://arxiv.org/abs/2505.05602v2"},{"title":"HiBayESA Hierarchical Bayesian Modeling Frameworkfor AI Evaluation Statistics","url":"https://arxiv.org/html/2505.05602v1"},{"title":"(PDF) HiBayES: A Hierarchical Bayesian Modeling Framework for AI Evaluation Statistics","url":"https://www.researchgate.net/publication/391658520_HiBayES_A_Hierarchical_Bayesian_Modeling_Framework_for_AI_Evaluation_Statistics"},{"title":"GitHub - UKGovernmentBEIS/hibayes","url":"https://github.com/UKGovernmentBEIS/hibayes"},{"title":"HiBayES: A hierarchical bayesian modelling framework for AI evaluation statistics","url":"https://www.aisi.gov.uk/research/hibayes-a-hierarchical-bayesian-modeling-framework-for-ai-evaluation-statistics"},{"title":"Computer Science May 2025","url":"https://arxiv.org/list/cs/2025-05?skip=2500&show=500"},{"title":"HiBayES: Improving LLM evaluation with hierarchical Bayesian modelling | AISI Work","url":"https://www.aisi.gov.uk/blog/hibayes-improving-llm-evaluation-with-hierarchical-bayesian-modelling"},{"title":"Bayesian Hierarchical Invariant Prediction","url":"https://arxiv.org/html/2505.11211v2"},{"title":"HIP-LLM: A Hierarchical Imprecise Probability Approach to Reliability Assessment of Large Language Models","url":"https://arxiv.org/html/2511.00527"}]

Based on the search results, here's what I found about arXiv paper 2505.05602:

## HiBayES: A Hierarchical Bayesian Modeling Framework for AI Evaluation Statistics

As Large Language Models (LLMs) and other AI systems evolve, robustly estimating their capabilities from inherently stochastic outputs while systematically quantifying uncertainty in these 
…[truncated 1286 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_bib_rebuild_2025plus_20260517T051927",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-17T05:24:49.035790+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"The Emperor's New Clothes\" LLM benchmark contamination mitigation 2025 arXiv 2503.16402"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_bib_rebuild_2025plus_20260517T051927",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"The Emperor's New Clothes\" LLM benchmark contamination mitigation 2025 arXiv 2503.16402"
  }
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-17T05:24:49.035921+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arXiv 2510.09259 \"Detecting Data Contamination\" reinforcement learning post-training Tao 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_bib_rebuild_2025plus_20260517T051927",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arXiv 2510.09259 \"Detecting Data Contamination\" reinforcement learning post-training Tao 2025"
  }
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-17T05:24:49.036050+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Kadavath \"Language Models Mostly Know What They Know\" 2022 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_bib_rebuild_2025plus_20260517T051927",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Kadavath \"Language Models Mostly Know What They Know\" 2022 arXiv"
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-17T05:24:49.036188+00:00_

Web search results for query: ""The Emperor's New Clothes" LLM benchmark contamination mitigation 2025 arXiv 2503.16402"

Links: [{"title":"[2503.16402] The Emperor's New Clothes in Benchmarking? A Rigorous Examination of Mitigation Strategies for LLM Benchmark Data Contamination","url":"https://arxiv.org/abs/2503.16402"},{"title":"GitHub - ASTRAL-Group/BDC-mitigation-assessment: [ICML 2025] Official implementation for \"The Emperor's New Clothes in Benchmarking? A Rigorous Examination of Mitigation Strategies for LLM Benchmark Data Contamination\" · GitHub","url":"https://github.com/ASTRAL-Group/BDC-mitigation-assessment"},{"title":"ICML Poster The Emperor's New Clothes in Benchmarking? A Rigorous Examination of Mitigation Strategies for LLM Benchmark Data Contamination","url":"https://icml.cc/virtual/2025/poster/45153"},{"title":"The Emperor's New Clothes in Benchmarking? A Rigorous Examination of Mitigation Strategies for LLM Benchmark Data Contamination | OpenReview","url":"https://openreview.net/forum?id=TuvDxubEfE"},{"title":"Machine Learning Mar 2025","url":"https://arxiv.org/list/cs.LG/2025-03?skip=3150&show=50"},{"title":"Computation and Language Mar 2025","url":"https://arxiv.org/list/cs.CL/2025-03?skip=1675&show=1000"},{"title":"The Emperor's New Clothes in Benchmarking? A Rigorous ...","url":"https://gangw.cs.illinois.edu/ICMLEmperor25.pdf"},{"title":"Computation and Language 2025","url":"https://arxiv.org/list/cs.CL/2025?skip=18400&show=50"},{"title":"The Emperor's New Clothes in Benchmarking? A Rigorous Examination of Mitigation Strategies For LLM Benchmark Data Contamination | PDF | Accuracy And Precision","url":"https://www.scribd.com/document/841775342/The-Emperor-s-New-Clothes-in-Benchmarking-A-Rigorous-Examination-of-Mitigation-Strategies-for-LLM-Benchmark-Data-Contamination"},{"title":"Yifan Sun, Han Wang, Dongbai Li, Gang Wang, Huan Zhang · The Emperor's New Clothes in Benchmarking? A Rigorous Examination of Mitigation Strategies for LLM Benchma
…[truncated 1674 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_bib_rebuild_2025plus_20260517T051927",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-17T05:24:49.036368+00:00_

Web search results for query: "Kadavath "Language Models Mostly Know What They Know" 2022 arXiv"

Links: [{"title":"[2207.05221] Language Models (Mostly) Know What They Know","url":"https://arxiv.org/abs/2207.05221"},{"title":"(PDF) Language Models (Mostly) Know What They Know","url":"https://www.researchgate.net/publication/361949621_Language_Models_Mostly_Know_What_They_Know"},{"title":"Language Models (Mostly) Know What They Know","url":"https://arxiv.org/pdf/2207.05221"},{"title":"Language Models (Mostly) Know What They Know","url":"https://bibbase.org/network/publication/kadavath-conerly-askell-henighan-drain-perez-schiefer-hatfielddodds-etal-languagemodelsmostlyknowwhattheyknow-2022"},{"title":"(PDF) Language Models (Mostly) Know What They Know (2022) | Saurav Kadavath | 413 Citations","url":"https://scispace.com/papers/language-models-mostly-know-what-they-know-zkg0pou4"},{"title":"Language Models (Mostly) Know What They Know - ADS","url":"https://ui.adsabs.harvard.edu/abs/2022arXiv220705221K/abstract"},{"title":"[PDF] Language Models (Mostly) Know What They Know | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Language-Models-(Mostly)-Know-What-They-Know-Kadavath-Conerly/142ebbf4760145f591166bde2564ac70c001e927"},{"title":"Language Models (Mostly) Know What They Know | BibSonomy","url":"https://www.bibsonomy.org/bibtex/2683f0b3b83a56dc82614c7e4257c3b6d/lumeng"},{"title":"[2207.05221] Language Models (Mostly) Know What They Know – Papiers","url":"https://papiers.ai/2207.05221"},{"title":"ml-papers/papers/2022/220711 Language Models (Mostly) Know What They Know.md at main · rosinality/ml-papers","url":"https://github.com/rosinality/ml-papers/blob/main/papers/2022/220711%20Language%20Models%20(Mostly)%20Know%20What%20They%20Know.md"}]

I found the paper you were looking for. Here's the information:

**Title:** Language Models (Mostly) Know What They Know

**Authors:** Saurav Kadavath, Tom Conerly, Amanda Askell, Tom Henighan, Dawn Drain, Ethan P
…[truncated 1008 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_bib_rebuild_2025plus_20260517T051927",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-17T05:24:49.036566+00:00_

Web search results for query: "arXiv 2510.09259 "Detecting Data Contamination" reinforcement learning post-training Tao 2025"

Links: [{"title":"[2510.09259] Detecting Data Contamination from Reinforcement Learning Post-training for Large Language Models","url":"https://arxiv.org/abs/2510.09259"},{"title":"Detecting Data Contamination from Reinforcement Learning Post-training for Large Language Models","url":"https://arxiv.org/html/2510.09259v1"},{"title":"detecting data contamination from reinforcement learning ...","url":"https://arxiv.org/pdf/2510.09259"},{"title":"Detecting Data Contamination in LLMs via In-Context Learning","url":"https://arxiv.org/html/2510.27055v1"},{"title":"Paper page - Detecting Data Contamination from Reinforcement Learning Post-training for Large Language Models","url":"https://huggingface.co/papers/2510.09259"},{"title":"Detecting Data Contamination from Reinforcement Learning Post-training for Large Language Models | Request PDF","url":"https://www.researchgate.net/publication/396459308_Detecting_Data_Contamination_from_Reinforcement_Learning_Post-training_for_Large_Language_Models"},{"title":"[2510.27055] Detecting Data Contamination in LLMs via In-Context Learning","url":"https://arxiv.org/abs/2510.27055"},{"title":"Reasoning or Memorization? Unreliable Results of Reinforcement Learning Due to Data Contamination","url":"https://arxiv.org/html/2507.10532v2"},{"title":"Evading Data Contamination Detection for Language ...","url":"https://arxiv.org/pdf/2402.02823"},{"title":"Investigating Data Contamination for Pre-training Language Models","url":"https://arxiv.org/html/2401.06059v1"}]

I found the paper you're looking for! Here are the key details:

## Paper: Detecting Data Contamination from Reinforcement Learning Post-training for Large Language Models

**arXiv ID:** 2510.09259

**Authors:** Yongding Tao, Tian Wang, Yihong Dong, Huanyu Liu, Kechi Zhang, Xiaolong Hu, Ge Li

**Key Findings:**

Data contamination poses a significant thr
…[truncated 1274 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_bib_rebuild_2025plus_20260517T051927",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-17T05:24:49.036733+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arXiv 2604.12843 \"Growing Pains\" authors full list 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_bib_rebuild_2025plus_20260517T051927",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arXiv 2604.12843 \"Growing Pains\" authors full list 2026"
  }
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-17T05:24:49.036869+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Decontaminated Calibration\" LLM benchmark EMNLP 2025 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_bib_rebuild_2025plus_20260517T051927",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Decontaminated Calibration\" LLM benchmark EMNLP 2025 arXiv"
  }
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-17T05:24:49.036998+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arXiv 2510.09259 ICLR 2026 \"Detecting Data Contamination\" Tao Yongding venue accepted"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_bib_rebuild_2025plus_20260517T051927",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arXiv 2510.09259 ICLR 2026 \"Detecting Data Contamination\" Tao Yongding venue accepted"
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-17T05:24:49.037126+00:00_

Web search results for query: "arXiv 2604.12843 "Growing Pains" authors full list 2026"

Links: [{"title":"[2604.12843] Growing Pains: Extensible and Efficient LLM Benchmarking Via Fixed Parameter Calibration","url":"https://arxiv.org/abs/2604.12843"},{"title":"Growing Pains: Extensible and Efficient LLM Benchmarking Via Fixed Parameter Calibration","url":"https://arxiv.org/html/2604.12843"},{"title":"(PDF) Growing Pains","url":"https://www.researchgate.net/publication/342540625_Growing_Pains"},{"title":"[2304.06138] Growing Pains: Understanding the Impact of Likelihood Uncertainty on Hierarchical Bayesian Inference for Gravitational-Wave Astronomy","url":"https://arxiv.org/abs/2304.06138"},{"title":"7. Growing Pains","url":"https://www.degruyterbrill.com/document/doi/10.3138/9781442670143-009/html"},{"title":"Growing Pains: Challenges for a Rising China","url":"https://dash.harvard.edu/entities/publication/73120378-c5a0-6bd4-e053-0100007fdf3b"},{"title":"(PDF) Virtual Growing Pains: Initial Lessons Learned from Organizing Virtual Workshops, Summits, Conferences, and Networking Events during a Global Pandemic","url":"https://www.researchgate.net/publication/349413071_Virtual_Growing_Pains_Initial_Lessons_Learned_from_Organizing_Virtual_Workshops_Summits_Conferences_and_Networking_Events_during_a_Global_Pandemic"},{"title":"(PDF) Growing Pains: The History of Human Development and the Future of the Field","url":"https://www.researchgate.net/publication/388209564_Growing_Pains_The_History_of_Human_Development_and_the_Future_of_the_Field"},{"title":"View of Growing Pains: Opportunities to Adjust Phenotypic Trajectories in Childhood and Adolescence Complicate Studies of Developmental Plasticity in Late Homo","url":"https://paleoanthropology.org/ojs/index.php/paleo/article/view/121/3614"},{"title":"Arxiv","url":"https://arxiv.org/pdf/2210.12843"}]

Based on the search results, the full list of authors for arXiv paper 2604.12843 "Growing Pains: Extensible and Efficient LL
…[truncated 364 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_bib_rebuild_2025plus_20260517T051927",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-17T05:24:49.037282+00:00_

Web search results for query: "arXiv 2510.09259 ICLR 2026 "Detecting Data Contamination" Tao Yongding venue accepted"

Links: [{"title":"[2510.09259] Detecting Data Contamination from Reinforcement Learning Post-training for Large Language Models","url":"https://arxiv.org/abs/2510.09259"},{"title":"detecting data contamination from reinforcement learning ...","url":"https://arxiv.org/pdf/2510.09259"},{"title":"Detecting Data Contamination from Reinforcement Learning Post-training for Large Language Models","url":"https://arxiv.org/html/2510.09259"},{"title":"Unveiling the Spectrum of Data Contamination in Language Models: A Survey from Detection to Remediation","url":"https://arxiv.org/html/2406.14644v1"},{"title":"Machine Learning Oct 2025","url":"https://arxiv.org/list/cs.LG/2025-10?skip=3650&show=250"},{"title":"Detecting Data Contamination from Reinforcement Learning Post-training for Large Language Models | OpenReview","url":"https://openreview.net/forum?id=EjiJmiA6ea"},{"title":"A Comprehensive Survey of Contamination Detection Methods in Large Language Models","url":"https://arxiv.org/html/2404.00699v5"},{"title":"Detecting Data Contamination in LLMs via In-Context Learning","url":"https://arxiv.org/html/2510.27055v1"},{"title":"Evading Data Contamination Detection for Language ...","url":"https://arxiv.org/pdf/2402.02823"},{"title":"Towards Data Contamination Detection for Modern Large Language Models: Limitations, Inconsistencies, and Oracle Challenges","url":"https://arxiv.org/html/2409.09927v2"}]

Based on the search results, I found information about the arXiv paper 2510.09259:

The paper is titled "Detecting Data Contamination from Reinforcement Learning Post-training for Large Language Models" with authors including Yongding Tao, Tian Wang, Yihong Dong, Huanyu Liu, Kechi Zhang, Xiaolong Hu, and Ge Li.

The paper addresses how data contamination poses a significant threat to the reliable evaluation of LLMs, arising when benchmark samples may inadvertent
…[truncated 832 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_bib_rebuild_2025plus_20260517T051927",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-17T05:24:49.037465+00:00_

Web search results for query: ""Decontaminated Calibration" LLM benchmark EMNLP 2025 arXiv"

Links: [{"title":"Benchmarking Large Language Models Under Data Contamination: A Survey from Static to Dynamic Evaluation","url":"https://arxiv.org/html/2502.17521v2"},{"title":"Accepted Findings Papers - EMNLP 2025","url":"https://2025.emnlp.org/program/find_papers/"},{"title":"A Survey from Static to Dynamic Evaluation","url":"https://aclanthology.org/2025.emnlp-main.511.pdf"},{"title":"DCR: Quantifying Data Contamination in LLMs Evaluation","url":"https://aclanthology.org/2025.emnlp-main.1173.pdf"},{"title":"Benchmarking Large Language Models Under Data Contamination: A Survey from Static to Dynamic Evaluation - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-main.511/"},{"title":"Evaluating and Calibrating LLM Confidence on Questions with Multiple Correct Answers","url":"https://arxiv.org/html/2602.07842v1"},{"title":"Rethinking Benchmark and Contamination for Language Models with","url":"https://arxiv.org/pdf/2311.04850"},{"title":"(PDF) Calibration and Control Techniques for LLM-Based Evaluation Models","url":"https://www.researchgate.net/publication/398235035_Calibration_and_Control_Techniques_for_LLM-Based_Evaluation_Models"},{"title":"GitHub - ShiyuNee/Awesome-Calibration-Papers: A curated list of awesome papers about calibration · GitHub","url":"https://github.com/ShiyuNee/Awesome-Calibration-Papers"},{"title":"GitHub - llm-as-a-judge/Awesome-LLM-as-a-judge · GitHub","url":"https://github.com/llm-as-a-judge/Awesome-LLM-as-a-judge"}]

Based on the web search results, I found relevant information about research on decontamination and calibration in LLM benchmarking. Here are the key findings:

## Related Work on Data Contamination and LLM Benchmarking

A comprehensive survey titled "Benchmarking Large Language Models Under Data Contamination: A Survey from Static to Dynamic Evaluation" was published in 2025 at the Conference on Empirical Methods in Natural 
…[truncated 1280 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_bib_rebuild_2025plus_20260517T051927",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-17T05:24:49.037625+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "openreview.net \"Detecting Data Contamination from Reinforcement Learning\" EjiJmiA6ea ICLR 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_bib_rebuild_2025plus_20260517T051927",
  "tool": "WebSearch",
  "tool_args": {
    "query": "openreview.net \"Detecting Data Contamination from Reinforcement Learning\" EjiJmiA6ea ICLR 2026"
  }
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-17T05:24:49.037758+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"DCR\" \"Quantifying Data Contamination\" LLM evaluation EMNLP 2025 Xu Yanyang arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_bib_rebuild_2025plus_20260517T051927",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"DCR\" \"Quantifying Data Contamination\" LLM evaluation EMNLP 2025 Xu Yanyang arXiv"
  }
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-17T05:24:49.037885+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Chang Yupeng \"Survey on Evaluation of Large Language Models\" ACM TIST 2024 volume issue doi"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_bib_rebuild_2025plus_20260517T051927",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Chang Yupeng \"Survey on Evaluation of Large Language Models\" ACM TIST 2024 volume issue doi"
  }
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-17T05:24:49.038016+00:00_

Web search results for query: "openreview.net "Detecting Data Contamination from Reinforcement Learning" EjiJmiA6ea ICLR 2026"

Links: [{"title":"Detecting Data Contamination from Reinforcement Learning Post-training for Large Language Models | OpenReview","url":"https://openreview.net/forum?id=EjiJmiA6ea"},{"title":"Detecting Data Contamination in LLMs via In-Context ...","url":"https://openreview.net/pdf?id=YlpaaYxx4t"},{"title":"Published as a conference paper at ICLR 2026","url":"https://openreview.net/pdf?id=W8VCH9x1HZ"},{"title":"DETECTING BENCHMARK CONTAMINATION THROUGH ...","url":"https://openreview.net/pdf?id=WFGxFzFDmQ"},{"title":"OBSCURING DATA CONTAMINATION THROUGH TRANSLATION","url":"https://openreview.net/pdf?id=omg9K6lI93"},{"title":"The Impact of Post-training on Data Contamination | OpenReview","url":"https://openreview.net/forum?id=GFDSGlEks2"},{"title":"Can In-Context Reinforcement Learning Recover From Reward Poisoning Attacks? | OpenReview","url":"https://openreview.net/forum?id=MtsmJZXIu5"},{"title":"[2510.09259] Detecting Data Contamination from Reinforcement Learning Post-training for Large Language Models","url":"https://arxiv.org/abs/2510.09259"},{"title":"Knowledge Distillation as Decontamination? Revisiting the “Data...","url":"https://openreview.net/forum?id=W8VCH9x1HZ"},{"title":"Detecting Data Contamination in LLMs via In-Context Learning | OpenReview","url":"https://openreview.net/forum?id=YlpaaYxx4t"}]

I found the paper! Here's what I discovered:

The paper addresses how data contamination poses a significant threat to the reliable evaluation of Large Language Models, arising when benchmark samples may inadvertently appear in training sets and compromise the validity of reported performance.

The work addresses a critical research gap by focusing on detection methods for the Reinforcement Learning (RL) post-training phase, which had previously not been systematically studied for contamination detection.

The authors conduct the firs
…[truncated 472 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_bib_rebuild_2025plus_20260517T051927",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-17T05:24:49.038177+00:00_

Web search results for query: "Chang Yupeng "Survey on Evaluation of Large Language Models" ACM TIST 2024 volume issue doi"

Links: [{"title":"A Survey on Evaluation of Large Language Models | ACM Transactions on Intelligent Systems and Technology","url":"https://dl.acm.org/doi/full/10.1145/3641289"},{"title":"[2307.03109] A Survey on Evaluation of Large Language Models","url":"https://arxiv.org/abs/2307.03109"},{"title":"A Survey on Evaluation of Large Language Models","url":"https://dl.acm.org/doi/pdf/10.1145/3641289"},{"title":"TIST: Vol 15, No 3","url":"https://dl.acm.org/toc/tist/2024/15/3"},{"title":"A Survey on Evaluation of Large Language Models - The Hong Kong University of Science and Technology","url":"https://researchportal.hkust.edu.hk/en/publications/a-survey-on-evaluation-of-large-language-models/"},{"title":"(PDF) A Survey on Evaluation of Large Language Models","url":"https://www.researchgate.net/publication/377639945_A_Survey_on_Evaluation_of_Large_Language_Models"},{"title":"GitHub - MLGroupJLU/LLM-eval-survey: The official GitHub page for the survey paper \"A Survey on Evaluation of Large Language Models\". · GitHub","url":"https://github.com/MLGroupJLU/LLM-eval-survey"},{"title":"Google Scholar","url":"https://scholar.google.com/scholar_lookup?title=A+survey+on+evaluation+of+large+language+models&amp=&author=Yupeng+Chang&amp=&author=Xu+Wang&amp=&author=Jindong+Wang&amp=&author=Yuan+Wu&amp=&author=Linyi+Yang&amp=&author=Kaijie+Zhu&amp=&author=Hao+Chen&amp=&author=Xiaoyuan+Yi&amp=&author=Cunxiang+Wang&amp=&author=Yidong+Wang&amp=&publication_year=2024&amp=&journal=ACM+Transactions+on+Intelligent+Systems+and+Technology&amp=&pages=1-45&amp=&doi=10.1145/3641289"},{"title":"Survey on Knowledge Distillation for Large Language Models: Methods, Evaluation, and Application | ACM Transactions on Intelligent Systems and Technology","url":"https://dl.acm.org/doi/10.1145/3699518"},{"title":"A Survey on Large Language Models for Mathematical Reasoning | ACM Co
…[truncated 865 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_bib_rebuild_2025plus_20260517T051927",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-17T05:24:49.038387+00:00_

Web search results for query: ""DCR" "Quantifying Data Contamination" LLM evaluation EMNLP 2025 Xu Yanyang arXiv"

Links: [{"title":"DCR: Quantifying Data Contamination in LLMs Evaluation - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-main.1173/"},{"title":"DCR: Quantifying Data Contamination in LLMs Evaluation","url":"https://aclanthology.org/2025.emnlp-main.1173.pdf"},{"title":"[2507.11405] DCR: Quantifying Data Contamination in LLMs Evaluation","url":"https://arxiv.org/abs/2507.11405"},{"title":"DCR: Quantifying Data Contamination in LLMs Evaluation","url":"https://arxiv.org/html/2507.11405v2"},{"title":"Benchmarking Large Language Models Under Data Contamination: A Survey from Static to Dynamic Evaluation - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-main.511/"},{"title":"A Survey from Static to Dynamic Evaluation","url":"https://aclanthology.org/2025.emnlp-main.511.pdf"},{"title":"A Survey on Data Contamination for Large Language Models","url":"https://openreview.net/pdf?id=O3rnGt7DK7"},{"title":"CodeCleaner: Mitigating Data Contamination for LLM Benchmarking | Proceedings of the 16th International Conference on Internetware","url":"https://dl.acm.org/doi/10.1145/3755881.3755901"},{"title":"Data Contamination or Genuine Generalization ... - SUAS","url":"https://www.suaspress.org/ojs/index.php/AJNS/article/download/v2n2a03/v2n2a03"},{"title":"Benchmarking Large Language Models Under Data Contamination: A Survey from Static to Dynamic Evaluation","url":"https://arxiv.org/html/2502.17521v2"}]

I found the paper you're looking for! Here's the information about the DCR paper:

## DCR: Quantifying Data Contamination in LLMs Evaluation

The paper introduces the Data Contamination Risk (DCR) framework, a lightweight, interpretable pipeline designed to detect and quantify BDC risk across four granular levels: semantic, informational, data, and label.

**Authors:** Cheng Xu, Nan Yan, Shuhao Guan, Changhong Jin, Yuke Mei, Yibing Guo, Tahar Kecha
…[truncated 848 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_bib_rebuild_2025plus_20260517T051927",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-17T05:24:49.038648+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "site:aclanthology.org \"DCR\" EMNLP 2025 authors Cheng Xu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_bib_rebuild_2025plus_20260517T051927",
  "tool": "WebSearch",
  "tool_args": {
    "query": "site:aclanthology.org \"DCR\" EMNLP 2025 authors Cheng Xu"
  }
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-17T05:24:49.038801+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"The Emperor's New Clothes in Benchmarking\" ICML 2025 authors \"Yifan Sun\" \"Han Wang\" \"Dongbai Li\" \"Gang Wang\" \"Huan Zhang\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_bib_rebuild_2025plus_20260517T051927",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"The Emperor's New Clothes in Benchmarking\" ICML 2025 authors \"Yifan Sun\" \"Han Wang\" \"Dongbai Li\" \"Gang Wang\" \"Huan Zhang\""
  }
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-17T05:24:49.038939+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Kadavath 2022 \"Language Models Mostly Know What They Know\" arXiv 2207.05221 all authors full list"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_bib_rebuild_2025plus_20260517T051927",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Kadavath 2022 \"Language Models Mostly Know What They Know\" arXiv 2207.05221 all authors full list"
  }
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-17T05:24:49.039066+00:00_

Web search results for query: "site:aclanthology.org "DCR" EMNLP 2025 authors Cheng Xu"

Links: [{"title":"DCR: Quantifying Data Contamination in LLMs Evaluation - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-main.1173/"},{"title":"DCR: Quantifying Data Contamination in LLMs Evaluation","url":"https://aclanthology.org/2025.emnlp-main.1173.pdf"},{"title":"DCRM: A Heuristic to Measure Response Pair Quality in ...","url":"https://aclanthology.org/2025.findings-emnlp.136.pdf"}]

Based on the search results, I found the paper you're looking for:

**DCR: Quantifying Data Contamination in LLMs Evaluation** is a paper by Xu et al. published at EMNLP 2025, authored by Cheng Xu, Nan Yan, Shuhao Guan, Changhong Jin, Yuke Mei, Yibing Guo, and Tahar Kechadi.

The paper introduces the Data Contamination Risk (DCR) framework, a lightweight, interpretable pipeline designed to detect and quantify benchmark data contamination risk across four granular levels: semantic, informational, data, and label. By synthesizing contamination scores via a fuzzy inference system, DCR produces a unified DCR Factor that adjusts raw accuracy to reflect contamination-aware performance.

The paper is available on ACL Anthology at: https://aclanthology.org/2025.emnlp-main.1173/


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_bib_rebuild_2025plus_20260517T051927",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-17T05:24:49.039214+00:00_

Web search results for query: "Kadavath 2022 "Language Models Mostly Know What They Know" arXiv 2207.05221 all authors full list"

Links: [{"title":"[2207.05221] Language Models (Mostly) Know What They Know","url":"https://arxiv.org/abs/2207.05221"},{"title":"Language Models (Mostly) Know What They Know","url":"https://arxiv.org/pdf/2207.05221"},{"title":"(PDF) Language Models (Mostly) Know What They Know","url":"https://www.researchgate.net/publication/361949621_Language_Models_Mostly_Know_What_They_Know"},{"title":"[PDF] Language Models (Mostly) Know What They Know | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Language-Models-(Mostly)-Know-What-They-Know-Kadavath-Conerly/142ebbf4760145f591166bde2564ac70c001e927"},{"title":"Language Models (Mostly) Know What They Know","url":"https://bibbase.org/network/publication/kadavath-conerly-askell-henighan-drain-perez-schiefer-hatfielddodds-etal-languagemodelsmostlyknowwhattheyknow-2022"},{"title":"(PDF) Language Models (Mostly) Know What They Know (2022) | Saurav Kadavath | 413 Citations","url":"https://scispace.com/papers/language-models-mostly-know-what-they-know-zkg0pou4"},{"title":"Language Models (Mostly) Know What They Know | BibSonomy","url":"https://www.bibsonomy.org/bibtex/2683f0b3b83a56dc82614c7e4257c3b6d/lumeng"},{"title":"[2207.05221] Language Models (Mostly) Know What They Know – Papiers","url":"https://papiers.ai/2207.05221"},{"title":"ml-papers/papers/2022/220711 Language Models (Mostly) Know What They Know.md at main · rosinality/ml-papers","url":"https://github.com/rosinality/ml-papers/blob/main/papers/2022/220711%20Language%20Models%20(Mostly)%20Know%20What%20They%20Know.md"},{"title":"[2207.05221v4] Language Models (Mostly) Know What They Know","url":"https://arxiv.org/abs/2207.05221v4"}]

Based on the search results, here is the complete list of authors for the paper "Language Models (Mostly) Know What They Know" (arXiv 2207.05221):

Saurav Kadavath, Tom Conerly, Amanda Askell, Tom He
…[truncated 574 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_bib_rebuild_2025plus_20260517T051927",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-17T05:24:49.039450+00:00_

Web search results for query: ""The Emperor's New Clothes in Benchmarking" ICML 2025 authors "Yifan Sun" "Han Wang" "Dongbai Li" "Gang Wang" "Huan Zhang""

Links: [{"title":"ICML Poster The Emperor's New Clothes in Benchmarking? A Rigorous Examination of Mitigation Strategies for LLM Benchmark Data Contamination","url":"https://icml.cc/virtual/2025/poster/45153"},{"title":"GitHub - ASTRAL-Group/BDC-mitigation-assessment: [ICML 2025] Official implementation for \"The Emperor's New Clothes in Benchmarking? A Rigorous Examination of Mitigation Strategies for LLM Benchmark Data Contamination\" · GitHub","url":"https://github.com/ASTRAL-Group/BDC-mitigation-assessment"},{"title":"The Emperor's New Clothes in Benchmarking? A Rigorous Examination of Mitigation Strategies for LLM Benchmark Data Contamination | OpenReview","url":"https://openreview.net/forum?id=TuvDxubEfE"},{"title":"[2503.16402] The Emperor's New Clothes in Benchmarking? A Rigorous Examination of Mitigation Strategies for LLM Benchmark Data Contamination","url":"https://arxiv.org/abs/2503.16402"},{"title":"Published as a paper at 2nd DATA-FM workshop @ ICLR 2025, Singapore.","url":"https://gangw.cs.illinois.edu/cvpr_Emperor25.pdf"},{"title":"Yifan Sun - Homepage","url":"https://yifansun99.github.io/"},{"title":"ASTRAL Group @ UIUC · GitHub","url":"https://github.com/ASTRAL-Group"},{"title":"The Emperor’s New Clothes in Benchmarking? A Rigorous Examination of Mitigation Strategies for LLM Benchmark Data Contamination","url":"https://arxiv.org/html/2503.16402"},{"title":"ICML Poster EmbodiedBench: Comprehensive Benchmarking Multi-modal Large Language Models for Vision-Driven Embodied Agents","url":"https://icml.cc/virtual/2025/poster/45994"},{"title":"ICML 2025 Papers","url":"https://icml.cc/virtual/2025/papers.html"}]

I found the paper successfully! Here's the information about "The Emperor's New Clothes in Benchmarking":

## Paper Details

**Title:** The Emperor's New Clothes in Benchmarking? A Rigorous Ex
…[truncated 1325 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_bib_rebuild_2025plus_20260517T051927",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-17T05:24:49.039660+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Decontaminated Calibration and Ranking\" \"Li Yucheng\" OR \"Yucheng Li\" LLM 2025 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_bib_rebuild_2025plus_20260517T051927",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Decontaminated Calibration and Ranking\" \"Li Yucheng\" OR \"Yucheng Li\" LLM 2025 arXiv"
  }
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-17T05:24:49.039803+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "openreview ICLR 2026 \"Detecting Data Contamination from Reinforcement Learning\" accepted decision"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_bib_rebuild_2025plus_20260517T051927",
  "tool": "WebSearch",
  "tool_args": {
    "query": "openreview ICLR 2026 \"Detecting Data Contamination from Reinforcement Learning\" accepted decision"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-17T05:24:49.039928+00:00_

Web search results for query: "openreview ICLR 2026 "Detecting Data Contamination from Reinforcement Learning" accepted decision"

Links: [{"title":"Detecting Data Contamination from Reinforcement Learning Post-training for Large Language Models | OpenReview","url":"https://openreview.net/forum?id=EjiJmiA6ea"},{"title":"[2510.09259] Detecting Data Contamination from Reinforcement Learning Post-training for Large Language Models","url":"https://arxiv.org/abs/2510.09259"}]

I found the paper on OpenReview. Based on the search results, data contamination poses a significant threat to the reliable evaluation of Large Language Models (LLMs), arising when benchmark samples may inadvertently appear in training sets, compromising the validity of reported performance. 

While detection methods have been developed for the pre-training and Supervised Fine-Tuning stages, a critical research gap exists for the increasingly significant phase of Reinforcement Learning (RL) post-training. The paper conducts the first systematic study of data detection within RL post-training scenario and proposes Self-Critique.

However, the search results do not contain information about the acceptance decision status for this paper at ICLR 2026. To find that specific information, you would need to visit the OpenReview forum directly at https://openreview.net/forum?id=EjiJmiA6ea to check the decision status.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_bib_rebuild_2025plus_20260517T051927",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-17T05:24:49.040084+00:00_

Web search results for query: ""Decontaminated Calibration and Ranking" "Li Yucheng" OR "Yucheng Li" LLM 2025 arXiv"

Links: [{"title":"Preprint, Under Review POSITION: THE HIDDEN COSTS AND MEASUREMENT","url":"https://www.arxiv.org/pdf/2509.21882"},{"title":"A Comprehensive Survey of Contamination Detection Methods in Large Language Models","url":"https://arxiv.org/html/2404.00699v4"},{"title":"How Much are LLMs Contaminated? A Comprehensive Survey and the LLMSanitize Library.","url":"https://arxiv.org/html/2404.00699v1"},{"title":"K2-V2: A 360-Open, Reasoning-Enhanced LLM","url":"https://arxiv.org/html/2512.06201v1"},{"title":"Restoring Calibration for Aligned Large Language Models: A Calibration-Aware Fine-Tuning Approach","url":"https://arxiv.org/html/2505.01997v3"},{"title":"CalibJudge: Calibrated LLM-as-a-Judge for Multilingual ...","url":"https://www.preprints.org/manuscript/202603.1324"},{"title":"ICML Poster Restoring Calibration for Aligned Large Language Models: A Calibration-Aware Fine-Tuning Approach","url":"https://icml.cc/virtual/2025/poster/46448"},{"title":"Evaluating and Calibrating LLM Confidence on Questions with Multiple Correct Answers","url":"https://arxiv.org/html/2602.07842v1"},{"title":"(PDF) Calibration and Control Techniques for LLM-Based Evaluation Models","url":"https://www.researchgate.net/publication/398235035_Calibration_and_Control_Techniques_for_LLM-Based_Evaluation_Models"},{"title":"Accepted Findings Papers - ACL 2025","url":"https://2025.aclweb.org/program/find_papers/"}]

The search results show several papers related to LLM calibration and contamination detection, with some mentions of work by Li Yucheng. However, I didn't find a specific paper titled "Decontaminated Calibration and Ranking" by Li Yucheng. Let me search more specifically:

No links found.

The search didn't return specific results for that exact title. Let me try an alternative search:

Links: [{"title":"An Open-Source Data Contamination Report for Large ...","
…[truncated 2548 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_bib_rebuild_2025plus_20260517T051927",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-17T05:24:49.040244+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Yucheng Li liyucheng09 \"latent jailbreak\" OR \"contamination\" EMNLP 2025 paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_bib_rebuild_2025plus_20260517T051927",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Yucheng Li liyucheng09 \"latent jailbreak\" OR \"contamination\" EMNLP 2025 paper"
  }
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-17T05:24:49.040460+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ICLR 2026 accepted papers list \"Self-Critique\" OR \"data contamination\" OR \"reinforcement learning\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_bib_rebuild_2025plus_20260517T051927",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ICLR 2026 accepted papers list \"Self-Critique\" OR \"data contamination\" OR \"reinforcement learning\""
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-17T05:24:49.040676+00:00_

Web search results for query: "Yucheng Li liyucheng09 "latent jailbreak" OR "contamination" EMNLP 2025 paper"

Links: [{"title":"Yucheng Li","url":"https://liyucheng09.github.io/"},{"title":"An Open-Source Data Contamination Report for Large Language Models - ACL Anthology","url":"https://aclanthology.org/2024.findings-emnlp.30/"},{"title":"Accepted Findings Papers - EMNLP 2025","url":"https://2025.emnlp.org/program/find_papers/"},{"title":"liyucheng09 (Yucheng Li) · GitHub","url":"https://github.com/liyucheng09"},{"title":"GitHub - liyucheng09/Contamination_Detector: Lightweight tool to identify Data Contamination in LLMs evaluation","url":"https://github.com/liyucheng09/Contamination_Detector"},{"title":"Benchmarking Large Language Models Under Data Contamination: A Survey from Static to Dynamic Evaluation","url":"https://arxiv.org/html/2502.17521v2"},{"title":"LLM Jailbreak Detection for (Almost) Free! - ACL Anthology","url":"https://aclanthology.org/2025.findings-emnlp.309/"},{"title":"Jailbreak Attack Initializations as Extractors of Compliance ...","url":"https://aclanthology.org/2025.findings-emnlp.354.pdf"},{"title":"LLM Jailbreak Detection for (Almost) Free!","url":"https://aclanthology.org/2025.findings-emnlp.309.pdf"},{"title":"An Open-Source Data Contamination Report for Large ...","url":"https://aclanthology.org/2024.findings-emnlp.30.pdf"}]

Based on my search results, I found information about Yucheng Li's work on data contamination, but I did not find a specific EMNLP 2025 paper matching your exact query about "latent jailbreak" or a paper with that username combination.

Here's what I found about Yucheng Li's related work:

Yucheng Li authored "An Open-Source Data Contamination Report for Large Language Models" published in Findings of the Association for Computational Linguistics: EMNLP 2024. This paper presents an extensive data contamination report for over 15 popular large language models across six popular multiple-choice QA benchmarks and intr
…[truncated 577 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_bib_rebuild_2025plus_20260517T051927",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 53 · 2026-05-17T05:24:49.040846+00:00_

Web search results for query: "ICLR 2026 accepted papers list "Self-Critique" OR "data contamination" OR "reinforcement learning""

Links: [{"title":"ICLR 2026 Accepted Paper List - Paper Copilot","url":"https://papercopilot.com/paper-list/iclr-paper-list/iclr-2026-paper-list/"},{"title":"ICLR 2026 Papers","url":"https://iclr.cc/virtual/2026/papers.html"},{"title":"ICLR 2026","url":"https://iclr.cc/"},{"title":"Paper Digest: ICLR 2026 Papers & Highlights – Paper Digest","url":"https://www.paperdigest.org/2026/02/iclr-2026-papers-highlights/"},{"title":"ICLR.2026 | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/venue/ICLR.2026"},{"title":"Papers from the Department of Computing accepted at ICLR 2026 | Imperial News | Imperial College London","url":"https://www.imperial.ac.uk/news/articles/engineering/computing/2026/papers-from-the-department-of-computing-accepted-at-iclr-2026/"},{"title":"ICLR 2026 Papers with Code & Data – Paper Digest","url":"https://www.paperdigest.org/2026/04/iclr-2026-papers-with-code-data/"},{"title":"ICLR 2026 Call for Papers","url":"https://iclr.cc/Conferences/2026/CallForPapers"},{"title":"ICLR 2026 Papers with Code & Data – Resources | Paper Digest","url":"https://resources.paperdigest.org/2026/04/iclr-2026-papers-with-code-data/"},{"title":"ICLR 2026 Accepted Papers: Oral Papers, Research Trends & Top Highlights","url":"https://www.bohrium.com/en/blog/research-notes/iclr-2026-accepted-papers-highlights/"}]

Based on the web search results, I found information about ICLR 2026 accepted papers. Here are the key findings:

ICLR 2026 accepted more than 5,300 papers, and several resources catalog these papers, though I found limited specific matches for the exact search terms you requested.

From the search results, I can identify papers related to **reinforcement learning**, which was one of your search terms:

- Med-Copilot achieved performance gains through offline and online reinforcement learning
- Behavior Foundation M
…[truncated 1075 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_bib_rebuild_2025plus_20260517T051927",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 54 · 2026-05-17T05:24:49.041011+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "site:iclr.cc \"Detecting Data Contamination from Reinforcement Learning\" 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_bib_rebuild_2025plus_20260517T051927",
  "tool": "WebSearch",
  "tool_args": {
    "query": "site:iclr.cc \"Detecting Data Contamination from Reinforcement Learning\" 2026"
  }
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-17T05:24:49.041150+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Yucheng Li \"Open-Source Data Contamination Report\" 2024 arXiv benchmark decontamination"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_bib_rebuild_2025plus_20260517T051927",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Yucheng Li \"Open-Source Data Contamination Report\" 2024 arXiv benchmark decontamination"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-17T05:24:49.041284+00:00_

Web search results for query: "site:iclr.cc "Detecting Data Contamination from Reinforcement Learning" 2026"

Links: [{"title":"[2510.09259] Detecting Data Contamination from Reinforcement Learning Post-training for Large Language Models","url":"https://arxiv.org/abs/2510.09259"},{"title":"Detecting Data Contamination from Reinforcement Learning Post-training for Large Language Models | OpenReview","url":"https://openreview.net/forum?id=EjiJmiA6ea"},{"title":"Detecting Data Contamination from Reinforcement Learning Post-training for Large Language Models","url":"https://arxiv.org/html/2510.09259v1"},{"title":"detecting data contamination from reinforcement learning ...","url":"https://arxiv.org/pdf/2510.09259"},{"title":"Detecting Data Contamination from Reinforcement Learning Post-training for Large Language Models | Request PDF","url":"https://www.researchgate.net/publication/396459308_Detecting_Data_Contamination_from_Reinforcement_Learning_Post-training_for_Large_Language_Models"},{"title":"Paper page - Detecting Data Contamination from Reinforcement Learning Post-training for Large Language Models","url":"https://huggingface.co/papers/2510.09259"},{"title":"Detecting Data Contamination in LLMs via In-Context Learning | OpenReview","url":"https://openreview.net/forum?id=YlpaaYxx4t"},{"title":"Detecting Data Contamination in LLMs via In-Context Learning","url":"https://arxiv.org/html/2510.27055v1"},{"title":"Evaluating the Robustness of Large Language Model ...","url":"https://www.arxiv.org/pdf/2511.22047"},{"title":"Computation and Language Oct 2025","url":"https://www.arxiv.org/list/cs.CL/2025-10?skip=675&show=250"}]

Based on the search results, I found the paper you're looking for. However, the paper does not appear to be specifically hosted on the ICLR website (iclr.cc) based on the search results. Instead, it's available on:

**Paper Title:** "Detecting Data Contamination from Reinforcement Learning Post-training for Large Language Models"

**Authors:** Yon
…[truncated 828 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_bib_rebuild_2025plus_20260517T051927",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 57 · 2026-05-17T05:24:49.041550+00:00_

Web search results for query: "Yucheng Li "Open-Source Data Contamination Report" 2024 arXiv benchmark decontamination"

Links: [{"title":"Benchmarking Large Language Models Under Data Contamination: A Survey from Static to Dynamic Evaluation","url":"https://arxiv.org/html/2502.17521v2"},{"title":"GitHub - lyy1994/awesome-data-contamination: The Paper List on Data Contamination for Large Language Models Evaluation. · GitHub","url":"https://github.com/lyy1994/awesome-data-contamination"},{"title":"When Benchmarks Leak: Inference-Time Decontamination for LLMs","url":"https://arxiv.org/html/2601.19334v1"},{"title":"A Survey on Data Contamination for Large Language Models","url":"https://arxiv.org/html/2502.14425v2"},{"title":"An Open-Source Data Contamination Report for Large Language Models","url":"https://arxiv.org/pdf/2310.17589"},{"title":"[2310.17589] An Open Source Data Contamination Report for Large Language Models","url":"https://arxiv.org/abs/2310.17589"},{"title":"Inference-Time Decontamination: Reusing Leaked Benchmarks for Large Language Model Evaluation","url":"https://arxiv.org/html/2406.13990v1"},{"title":"[2310.17589] An Open-Source Data Contamination Report for Large Language Models","url":"https://ar5iv.labs.arxiv.org/html/2310.17589"},{"title":"An Open-Source Data Contamination Report for Large Language Models - ACL Anthology","url":"https://aclanthology.org/2024.findings-emnlp.30/"},{"title":"Benchmark Data Contamination of Large Language Models: A Survey","url":"https://arxiv.org/html/2406.04244v1"}]

Based on the search results, I found information about Yucheng Li's Open-Source Data Contamination Report for Large Language Models:

## Overview

Yucheng Li, Yunhao Guo, Frank Guerin, and Chenghua Lin published "An Open-Source Data Contamination Report for Large Language Models" in the Findings of the Association for Computational Linguistics: EMNLP 2024.

## Key Findings

The paper presents an extensive data contamination report for over 15 popular 
…[truncated 974 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_bib_rebuild_2025plus_20260517T051927",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 58 · 2026-05-17T05:24:49.041722+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Published as a conference paper at ICLR 2026\" \"data contamination\" \"reinforcement learning\" Tao"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_bib_rebuild_2025plus_20260517T051927",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Published as a conference paper at ICLR 2026\" \"data contamination\" \"reinforcement learning\" Tao"
  }
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-17T05:24:49.041862+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "HiBayES 2505.05602 authors \"Lennart Luettgau\" \"Harry Coppock\" \"Magda Dubois\" \"Christopher Summerfield\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_bib_rebuild_2025plus_20260517T051927",
  "tool": "WebSearch",
  "tool_args": {
    "query": "HiBayES 2505.05602 authors \"Lennart Luettgau\" \"Harry Coppock\" \"Magda Dubois\" \"Christopher Summerfield\""
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-17T05:24:49.042032+00:00_

Web search results for query: ""Published as a conference paper at ICLR 2026" "data contamination" "reinforcement learning" Tao"

Links: [{"title":"2026 Conference","url":"https://iclr.cc/"},{"title":"Published as a conference paper at ICLR 2026","url":"https://openreview.net/pdf?id=nAO9LcV7nE"},{"title":"ICLR 2026 Papers","url":"https://iclr.cc/virtual/2026/papers.html"},{"title":"ICLR 2026 Schedule","url":"https://iclr.cc/virtual/2026/calendar"},{"title":"ICLR 2026 Call for Papers","url":"https://iclr.cc/Conferences/2026/CallForPapers"},{"title":"ICLR 2026 Orals","url":"https://iclr.cc/virtual/2026/events/oral"},{"title":"ICLR 2026 Accepted Paper List - Paper Copilot","url":"https://papercopilot.com/paper-list/iclr-paper-list/iclr-2026-paper-list/"},{"title":"ICLR 2026 Papers with Code & Data – Paper Digest","url":"https://www.paperdigest.org/2026/04/iclr-2026-papers-with-code-data/"},{"title":"Paper Digest: ICLR 2026 Papers & Highlights – Paper Digest","url":"https://www.paperdigest.org/2026/02/iclr-2026-papers-highlights/"},{"title":"GitHub - Allenpandas/Reinforcement-Learning-Papers: 📚 List of Top-tier Conference Papers on Reinforcement Learning (RL)，including: NeurIPS, ICML, AAAI, IJCAI, AAMAS, ICLR, ICRA, etc.","url":"https://github.com/Allenpandas/Reinforcement-Learning-Papers"}]

I found search results related to ICLR 2026, but the results don't contain a paper specifically matching all your query terms ("data contamination" + "reinforcement learning" + author "Tao" published at ICLR 2026). 

The search returned general ICLR 2026 information and papers on reinforcement learning topics, but not a specific paper with those exact characteristics. The one paper I found titled "Published as a conference paper at ICLR 2026" appears to focus on robot manipulation and exploration with reinforcement learning, but doesn't specifically address data contamination.

If you're looking for a specific paper, you might want to:
- Check the OpenReview ICLR 2026 proceedings d
…[truncated 343 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_bib_rebuild_2025plus_20260517T051927",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 61 · 2026-05-17T05:24:49.042287+00:00_

Web search results for query: "HiBayES 2505.05602 authors "Lennart Luettgau" "Harry Coppock" "Magda Dubois" "Christopher Summerfield""

Links: [{"title":"[2505.05602] HiBayES: A Hierarchical Bayesian Modeling Framework for AI Evaluation Statistics","url":"https://arxiv.org/abs/2505.05602"},{"title":"[2505.05602v2] HiBayES: A Hierarchical Bayesian Modeling Framework for AI Evaluation Statistics","url":"http://arxiv.org/abs/2505.05602v2"},{"title":"(PDF) HiBayES: A Hierarchical Bayesian Modeling Framework for AI Evaluation Statistics","url":"https://www.researchgate.net/publication/391658520_HiBayES_A_Hierarchical_Bayesian_Modeling_Framework_for_AI_Evaluation_Statistics"},{"title":"GitHub - UKGovernmentBEIS/hibayes","url":"https://github.com/UKGovernmentBEIS/hibayes"},{"title":"dblp: Cozmin Ududec","url":"https://dblp.org/pid/254/3053.html"},{"title":"Magda DUBOIS | PhD Student | University College London, London | UCL | Institute of Neurology | Research profile","url":"https://www.researchgate.net/profile/Magda-Dubois"},{"title":"[2507.03772] Skewed Score: A statistical framework to assess autograders","url":"https://arxiv.org/abs/2507.03772"},{"title":"[2511.15352] People readily follow personal advice from AI but it does not improve their well-being","url":"https://arxiv.org/abs/2511.15352"},{"title":"[2507.03409] Lessons from a Chimp: AI \"Scheming\" and the Quest for Ape Language","url":"https://arxiv.org/abs/2507.03409"},{"title":"[2507.03409v1] Lessons from a Chimp: AI \"Scheming\" and the Quest for Ape Language","url":"https://arxiv.org/abs/2507.03409v1"}]

I found the paper you're looking for. The authors of HiBayES (arXiv:2505.05602) are Lennart Luettgau, Harry Coppock, Magda Dubois, Christopher Summerfield, and Cozmin Ududec.

HiBayES is a generalizable Hierarchical Bayesian modeling framework for AI Evaluation Statistics that supports robust inferences in classical question-answer benchmarks and advanced agentic evaluations, particularly in low-data scenar
…[truncated 147 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_bib_rebuild_2025plus_20260517T051927",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 62 · 2026-05-17T05:24:49.042550+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "openreview.net/forum?id=EjiJmiA6ea decision \"ICLR 2026\" poster OR oral OR spotlight"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_bib_rebuild_2025plus_20260517T051927",
  "tool": "WebSearch",
  "tool_args": {
    "query": "openreview.net/forum?id=EjiJmiA6ea decision \"ICLR 2026\" poster OR oral OR spotlight"
  }
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-17T05:24:49.042708+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"duan2025\" OR \"Duan Jiawen\" Min-K%++ membership inference 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_bib_rebuild_2025plus_20260517T051927",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"duan2025\" OR \"Duan Jiawen\" Min-K%++ membership inference 2025"
  }
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-17T05:24:49.042847+00:00_

Web search results for query: "openreview.net/forum?id=EjiJmiA6ea decision "ICLR 2026" poster OR oral OR spotlight"

Links: [{"title":"ICLR 2026 Conference | OpenReview","url":"https://openreview.net/group?id=ICLR.cc%2F2026%2FConference"},{"title":"ICLR 2026 Workshop Proposal MemAgents: Memory for LLM-Based Agentic Systems","url":"https://openreview.net/pdf?id=U51WxL382H"},{"title":"ICLR 2026 Call for Papers","url":"https://iclr.cc/Conferences/2026/CallForPapers"},{"title":"2026 Poster Instructions","url":"https://iclr.cc/Conferences/2026/PosterInstructions"},{"title":"Venues | OpenReview","url":"https://openreview.net/"},{"title":"On the identifiability of causal graphs with multiple environments | OpenReview","url":"https://openreview.net/forum?id=ta8BKRa1bl"},{"title":"Thyme: Think Beyond Images | OpenReview","url":"https://openreview.net/forum?id=gCWLkqK45O"},{"title":"Position: Want Better ML Reviews? Stop Asking Nicely and Start Incentivizing with a Credit System | OpenReview","url":"https://openreview.net/forum?id=6IiZXiqP3Q"},{"title":"ICLR 2026 Workshop SPOT | OpenReview","url":"https://openreview.net/group?id=ICLR.cc%2F2026%2FWorkshop%2FSPOT"},{"title":"ICLR 2026 Conference Submissions","url":"https://openreview.net/submissions?page=202&venue=ICLR.cc/2026/Conference"}]

The search results don't contain information about the specific paper with ID "EjiJmiA6ea". Let me try a more direct search using that specific paper ID.

No links found.

The search didn't return results for that specific paper ID. Unfortunately, I cannot find information about the specific OpenReview forum with ID "EjiJmiA6ea" and its ICLR 2026 decision status (whether it was accepted as a poster, oral, or spotlight presentation) in the search results. 

To find this information, you would need to:
1. Visit the paper directly at `openreview.net/forum?id=EjiJmiA6ea`
2. Look for the decision note or announcement section on that page, which should indicate the acceptance status

If the paper
…[truncated 225 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_bib_rebuild_2025plus_20260517T051927",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 65 · 2026-05-17T05:24:49.043003+00:00_

Web search results for query: ""duan2025" OR "Duan Jiawen" Min-K%++ membership inference 2025"

Links: [{"title":"MIN-K%++: IMPROVED BASELINE FOR DETECTING PRE ...","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/a2e3b4132ab2e0b7a21e6e75da7f91a9-Paper-Conference.pdf"},{"title":"Scaling Up Membership Inference: When and How Attacks ...","url":"https://aclanthology.org/2025.findings-naacl.234.pdf"},{"title":"RECALL: Membership Inference via Relative Conditional ...","url":"https://aclanthology.org/2024.emnlp-main.493.pdf"},{"title":"[2402.07841] Do Membership Inference Attacks Work on Large Language Models?","url":"https://arxiv.org/abs/2402.07841"},{"title":"Reassessing EMNLP 2024’s Best Paper: Does Divergence-Based Calibration for Membership Inference Attacks Hold Up? | ICLR Blogposts 2025","url":"https://iclr-blogposts.github.io/2025/blog/calibrated-mia/"},{"title":"Membership Inference Attacks against Diffusion Models | Request PDF","url":"https://www.researchgate.net/publication/372665277_Membership_Inference_Attacks_against_Diffusion_Models"},{"title":"[PDF] Do Membership Inference Attacks Work on Large Language Models? | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Do-Membership-Inference-Attacks-Work-on-Large-Duan-Suri/f16c669c126c800dac38d445ddd178ffb9af5b7a"},{"title":"Membership Inference Attacks Against In-Context Learning | Proceedings of the 2024 on ACM SIGSAC Conference on Computer and Communications Security","url":"https://dl.acm.org/doi/10.1145/3658644.3690306"},{"title":"Accepted Main Conference Papers - EMNLP 2025","url":"https://2025.emnlp.org/program/main_papers/"},{"title":"Image Corruption-Inspired Membership Inference Attacks ...","url":"https://arxiv.org/pdf/2506.12340"}]

Based on the search results, I found relevant information about your query:

## Min-K%++ and Membership Inference

Min-K%++ is a reference-free method that provides competitive performance comparable to reference model-based approaches for m
…[truncated 1158 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_bib_rebuild_2025plus_20260517T051927",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 66 · 2026-05-17T05:24:49.043184+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Inference-Time Decontamination\" LLM benchmark \"Li Yucheng\" OR \"Yucheng Li\" EMNLP findings 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_bib_rebuild_2025plus_20260517T051927",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Inference-Time Decontamination\" LLM benchmark \"Li Yucheng\" OR \"Yucheng Li\" EMNLP findings 2024"
  }
}
```

</details>

---

### Tool call

_source line 67 · 2026-05-17T05:24:49.043423+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "iclr.cc virtual 2026 \"Detecting Data Contamination\" poster"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_bib_rebuild_2025plus_20260517T051927",
  "tool": "WebSearch",
  "tool_args": {
    "query": "iclr.cc virtual 2026 \"Detecting Data Contamination\" poster"
  }
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-17T05:24:49.043626+00:00_

Web search results for query: "iclr.cc virtual 2026 "Detecting Data Contamination" poster"

Links: [{"title":"ICLR 2026: Detecting Data Contamination in LLMs via In- ...","url":"https://www.linkedin.com/posts/besmira-nushi-43969712_our-work-on-data-contamination-analysis-was-activity-7422343437376561152-O2kU"}]

I found a search result related to "Detecting Data Contamination" at ICLR 2026. The result is a LinkedIn post by Besmira Nushi about work on data contamination analysis that was presented at ICLR 2026. The post title references "ICLR 2026: Detecting Data Contamination in LLMs via In-..." 

However, the search result doesn't provide detailed content about the poster itself. You may want to visit the LinkedIn post directly at the link above, or search the ICLR 2026 conference website directly for more information about this specific poster presentation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_bib_rebuild_2025plus_20260517T051927",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 69 · 2026-05-17T05:24:49.043822+00:00_

Web search results for query: ""Inference-Time Decontamination" LLM benchmark "Li Yucheng" OR "Yucheng Li" EMNLP findings 2024"

Links: [{"title":"When Benchmarks Leak: Inference-Time Decontamination for LLMs","url":"https://arxiv.org/html/2601.19334v1"},{"title":"Inference-Time Decontamination: Reusing Leaked Benchmarks for Large Language Model Evaluation - ACL Anthology","url":"https://aclanthology.org/2024.findings-emnlp.532/"},{"title":"Inference-Time Decontamination: Reusing Leaked Benchmarks for Large Language Model Evaluation","url":"https://arxiv.org/html/2406.13990v1"},{"title":"Reusing Leaked Benchmarks for Large Language Model ...","url":"https://aclanthology.org/2024.findings-emnlp.532.pdf"},{"title":"Benchmarking Large Language Models Under Data Contamination: A Survey from Static to Dynamic Evaluation","url":"https://arxiv.org/html/2502.17521v2"},{"title":"[Quick Review] Inference-Time Decontamination: Reusing Leaked Benchmarks for Large Language Model Evaluation","url":"https://liner.com/review/inferencetime-decontamination-reusing-leaked-benchmarks-for-large-language-model-evaluation"},{"title":"[2406.13990] Inference-Time Decontamination: Reusing Leaked Benchmarks for Large Language Model Evaluation","url":"https://arxiv.org/abs/2406.13990"},{"title":"Findings - EMNLP 2024","url":"https://2024.emnlp.org/program/accepted_findings/"},{"title":"Inference-Time Decontamination: Reusing Leaked Benchmarks for Large Language Model Evaluation | Request PDF","url":"https://www.researchgate.net/publication/386183526_Inference-Time_Decontamination_Reusing_Leaked_Benchmarks_for_Large_Language_Model_Evaluation"},{"title":"GitHub - lyy1994/awesome-data-contamination: The Paper List on Data Contamination for Large Language Models Evaluation. · GitHub","url":"https://github.com/lyy1994/awesome-data-contamination"}]

Based on the search results, I found relevant information about "Inference-Time Decontamination" and related research presented at EMNLP 2024:

## Infer
…[truncated 1387 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_bib_rebuild_2025plus_20260517T051927",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 70 · 2026-05-17T05:24:49.043992+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Yucheng Li\" \"Frank Guerin\" \"Chenghua Lin\" contamination decontamination arXiv 2310.17589"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_bib_rebuild_2025plus_20260517T051927",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Yucheng Li\" \"Frank Guerin\" \"Chenghua Lin\" contamination decontamination arXiv 2310.17589"
  }
}
```

</details>

---

### Tool call

_source line 71 · 2026-05-17T05:24:49.044132+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "papercopilot.com ICLR 2026 \"Detecting Data Contamination from Reinforcement Learning Post-training\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_bib_rebuild_2025plus_20260517T051927",
  "tool": "WebSearch",
  "tool_args": {
    "query": "papercopilot.com ICLR 2026 \"Detecting Data Contamination from Reinforcement Learning Post-training\""
  }
}
```

</details>

---

### Tool result

_source line 72 · 2026-05-17T05:24:49.044255+00:00_

Web search results for query: "papercopilot.com ICLR 2026 "Detecting Data Contamination from Reinforcement Learning Post-training""

No links found.

The search did not return any results. It's possible that:

1. The specific paper or article may not exist or may not be indexed by search engines
2. The website papercopilot.com may not have this content publicly available
3. ICLR 2026 submissions or papers may not yet be fully indexed or released

If you're looking for a specific paper, I'd recommend:
- Visiting the ICLR 2026 official website or proceedings directly
- Checking papercopilot.com directly by typing the URL into your browser
- Searching for the paper title alone without the website restriction
- Looking at academic repositories like arXiv or OpenReview

Would you like me to try a different search approach?


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_bib_rebuild_2025plus_20260517T051927",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 73 · 2026-05-17T05:24:49.044434+00:00_

Web search results for query: ""Yucheng Li" "Frank Guerin" "Chenghua Lin" contamination decontamination arXiv 2310.17589"

Links: [{"title":"[2310.17589] An Open-Source Data Contamination Report for Large Language Models","url":"https://ar5iv.labs.arxiv.org/html/2310.17589"},{"title":"[2310.17589] An Open Source Data Contamination Report for Large Language Models","url":"https://arxiv.org/abs/2310.17589"},{"title":"arXiv:2310.17589v3 [cs.CL] 29 Jan 2024","url":"https://arxiv.org/pdf/2310.17589"},{"title":"GitHub - lyy1994/awesome-data-contamination: The Paper List on Data Contamination for Large Language Models Evaluation. · GitHub","url":"https://github.com/lyy1994/awesome-data-contamination"},{"title":"[PDF] LatestEval: Addressing Data Contamination in Language Model Evaluation through Dynamic and Time-Sensitive Test Construction | Semantic Scholar","url":"https://www.semanticscholar.org/paper/LatestEval:-Addressing-Data-Contamination-in-Model-Li-Geurin/8106d03fb984afd8c3d066cd4f993eb2616a0da5"},{"title":"An Open-Source Data Contamination Report for Large Language Models - ACL Anthology","url":"https://aclanthology.org/2024.findings-emnlp.30/"},{"title":"An Open-Source Data Contamination Report for Large Language Models | Request PDF","url":"https://www.researchgate.net/publication/386197129_An_Open-Source_Data_Contamination_Report_for_Large_Language_Models"},{"title":"Yucheng Li | Semantic Scholar","url":"https://www.semanticscholar.org/author/Yucheng-Li/1527099159"},{"title":"Yucheng Li","url":"https://liyucheng09.github.io/"},{"title":"Toxicity Characterization, Detection and Remediation of ...","url":"https://mdpi-res.com/bookfiles/book/9417/Toxicity_Characterization_Detection_and_Remediation_of_Contaminants_in_Soils_and_Groundwater.pdf?v=1740190114"}]

I found the paper you were searching for. arXiv:2310.17589 is titled "An Open Source Data Contamination Report for Large Language Models" with authors Yucheng Li, Frank Guerin, and Chenghua Lin.

The paper addr
…[truncated 901 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_bib_rebuild_2025plus_20260517T051927",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 74 · 2026-05-17T05:24:49.044619+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arXiv 2207.05221 Kadavath 2022 \"Language Models Mostly Know What They Know\" full author list complete"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_bib_rebuild_2025plus_20260517T051927",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arXiv 2207.05221 Kadavath 2022 \"Language Models Mostly Know What They Know\" full author list complete"
  }
}
```

</details>

---

### Tool result

_source line 75 · 2026-05-17T05:24:49.044762+00:00_

Web search results for query: "arXiv 2207.05221 Kadavath 2022 "Language Models Mostly Know What They Know" full author list complete"

Links: [{"title":"[2207.05221] Language Models (Mostly) Know What They Know","url":"https://arxiv.org/abs/2207.05221"},{"title":"Language Models (Mostly) Know What They Know","url":"https://arxiv.org/pdf/2207.05221"},{"title":"(PDF) Language Models (Mostly) Know What They Know","url":"https://www.researchgate.net/publication/361949621_Language_Models_Mostly_Know_What_They_Know"},{"title":"[PDF] Language Models (Mostly) Know What They Know | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Language-Models-(Mostly)-Know-What-They-Know-Kadavath-Conerly/142ebbf4760145f591166bde2564ac70c001e927"},{"title":"(PDF) Language Models (Mostly) Know What They Know (2022) | Saurav Kadavath | 413 Citations","url":"https://scispace.com/papers/language-models-mostly-know-what-they-know-zkg0pou4"},{"title":"Language Models (Mostly) Know What They Know","url":"https://bibbase.org/network/publication/kadavath-conerly-askell-henighan-drain-perez-schiefer-hatfielddodds-etal-languagemodelsmostlyknowwhattheyknow-2022"},{"title":"[2207.05221v4] Language Models (Mostly) Know What They Know","url":"https://arxiv.org/abs/2207.05221v4"},{"title":"[2207.05221] Language Models (Mostly) Know What They Know – Papiers","url":"https://papiers.ai/2207.05221"},{"title":"Language Models (Mostly) Know What They Know | alphaXiv","url":"https://www.alphaxiv.org/overview/2207.05221v4"},{"title":"ml-papers/papers/2022/220711 Language Models (Mostly) Know What They Know.md at main · rosinality/ml-papers","url":"https://github.com/rosinality/ml-papers/blob/main/papers/2022/220711%20Language%20Models%20(Mostly)%20Know%20What%20They%20Know.md"}]

Based on the search results, the complete author list for arXiv paper 2207.05221 "Language Models (Mostly) Know What They Know" includes: Saurav Kadavath, Tom Conerly, Amanda Askell, Tom Henighan, Dawn Drain, Ethan Perez, N
…[truncated 544 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_bib_rebuild_2025plus_20260517T051927",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 76 · 2026-05-17T05:24:49.044941+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/bib_rebuild_2025plus.bib",
  "content": "% =============================================================================\n% BIB REBUILD: 2025+ Citations Verification\n% Generated: 2026-05-17\n% =============================================================================\n\n% KEY: chang2025benchmarking | STATUS: VERIFIED | SOURCE: ACM TIST 2024, arXiv 2307.03109\n% NOTE: Published in 2024 (not 2025). Journal article in ACM TIST Vol.15 No.3.\n%       The bib key says \"2025\" but the paper was published March 2024.\n%       Venue in existing bib (\"EMNLP 2025\") is WRONG -- it is ACM TIST 2024.\n@article{chang2025benchmarking,\n  author    = {Chang, Yupeng and Wang, Xu and Wang, Jindong and Wu, Yuan and Yang, Linyi and Zhu, Kaijie and Chen, Hao and Yi, Xiaoyuan and Wang, Cunxiang and Wang, Yidong and Ye, Wei and Zhang, Yue and Chang, Yi and Yu, Philip S. and Yang, Qiang and Xie, Xing},\n  title     = {A Survey on Evaluation of Large Language Models},\n  journal   = {ACM Transactions on Intelligent Systems and Technology},\n  volume    = {15},\n  number    = {3},\n  pages     = {1--45},\n  year      = {2024},\n  doi       = {10.1145/3641289},\n  eprint    = {2307.03109},\n  archiveprefix = {arXiv},\n  url       = {https://arxiv.org/abs/2307.03109}\n}\n\n% KEY: duan2025minkpp | STATUS: REPLACED | SOURCE: arXiv 2404.02936, ICLR 2025 Spotlight\n% NOTE: The original entry listed fabricated authors \"Duan, Jiawen; Xie, Cheng; Zhang, Jian; Li, Kai\".\n%       The real Min-K%++ paper is by Zhang, Jingyang et al. This is the same paper already\n%       correctly entered as zhang_2024_minkpp in the main bib. Keeping corrected version here.\n@inproceedings{duan2025minkpp,\n  author    = {Zhang, Jingyang and Sun, Jingwei and Yeats, Eric and Ouyang, Yang and Kuo, Martin and Zhang, Jianyi and Yang, Hao Frank and Li, Hai},\n  title     = {{Min-K\\%++}: Improved Baseline for Detecting Pre-Training Data from Large Language Models},\n  booktitle = {Proceedings of the 13th International Conference on Learning Representations (ICLR)},\n  year      = {2025},\n  note      = {Spotlight. arXiv:2404.02936},\n  eprint    = {2404.02936},\n  archiveprefix = {arXiv},\n  url       = {https://arxiv.org/abs/2404.02936}\n}\n\n% KEY: habba_2025_growing_pains | STATUS: VERIFIED | SOURCE: arXiv 2604.12843\n% NOTE: The existing bib entry had WRONG authors (listed Polo, Mamani, Zhuang, Xu, Choshen,\n%       Yurochkin, Sun). The real authors are Habba, Itzhak, Yehudai, Perlitz, Bandel,\n%       Shmueli-Scheuer, Choshen, Stanovsky. Also the year is 2026 (April 2026), not 2025.\n%       First author is \"Eliya Habba\" not \"Maryam Habba\".\n@article{habba_2025_growing_pains,\n  author        = {Habba, Eliya and Itzhak, Itay and Yehudai, Asaf and Perlitz, Yotam and Bandel, Elron and Shmueli-Scheuer, Michal and Choshen, Leshem and Stanovsky, Gabriel},\n  title         = {Growing Pains: Extensible and Efficient {LLM} Benchmarking Via Fixed Parameter Calibration},\n  journal       = {arXiv preprint},\n  year          = {2026},\n  eprint        = {2604.12843},\n  archiveprefix = {arXiv},\n  url           = {https://arxiv.org/abs/2604.12843}\n}\n\n% KEY: li_2025_dcr / li2025dcr | STATUS: NOT_FOUND | SOURCE: N/A\n% NOTE: No paper titled \"Decontaminated Calibration and Ranking for Trustworthy LLM Evaluation\"\n%       by \"Li, Yucheng; Flanigan, Frank; Sherborne, Tom; Sherborne, Charlie\" exists.\n%       This appears to be a HALLUCINATION. The real \"DCR\" paper at EMNLP 2025 is\n%       \"DCR: Quantifying Data Contamination in LLMs Evaluation\" by Cheng Xu et al.\n%       (arXiv 2507.11405). That paper is already in the bib as xu_2025_dcr.\n%       Yucheng Li's real EMNLP 2024 paper is \"An Open-Source Data Contamination Report\n%       for Large Language Models\" (arXiv 2310.17589).\n%       SUGGESTED REPLACEMENT: Use xu_2025_dcr for DCR-related citations, or cite\n%       Yucheng Li's actual 2024 paper if contamination reporting is the intended context.\n% --- Option A: Alias to the real DCR paper (Xu et al. EMNLP 2025) ---\n@inproceedings{li_2025_dcr,\n  author    = {Xu, Cheng and Yan, Nan and Guan, Shuhao and Jin, Changhong and Mei, Yuke and Guo, Yibing and Kechadi, Tahar},\n  title     = {{DCR}: Quantifying Data Contamination in {LLMs} Evaluation},\n  booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  pages     = {23002--23020},\n  year      = {2025},\n  eprint    = {2507.11405},\n  archiveprefix = {arXiv},\n  url       = {https://aclanthology.org/2025.emnlp-main.1173/}\n}\n\n% KEY: luettgau_2025_hibayes | STATUS: VERIFIED | SOURCE: arXiv 2505.05602\n% NOTE: The existing bib entry had WRONG authors (listed Polo, Zhuang, Yurochkin, Sun).\n%       The real authors are from the UK AI Safety Institute.\n@article{luettgau_2025_hibayes,\n  author        = {Luettgau, Lennart and Coppock, Harry and Dubois, Magda and Summerfield, Christopher and Ududec, Cozmin},\n  title         = {{HiBayES}: A Hierarchical {Bayesian} Modeling Framework for {AI} Evaluation Statistics},\n  journal       = {arXiv preprint},\n  year          = {2025},\n  eprint        = {2505.05602},\n  archiveprefix = {arXiv},\n  url           = {https://arxiv.org/abs/2505.05602}\n}\n\n% KEY: polo2026growing | STATUS: REPLACED | SOURCE: arXiv 2604.12843\n% NOTE: This is the SAME paper as habba_2025_growing_pains (arXiv 2604.12843).\n%       The existing entry had completely wrong authors (Polo, Mamani, Zhuang, Xu, Choshen,\n%       Yurochkin, Sun) and wrong title framing. Polo is NOT an author of this paper.\n%       Corrected to match the real paper. Consider merging with habba_2025_growing_pains.\n@article{polo2026growing,\n  author        = {Habba, Eliya and Itzhak, Itay and Yehudai, Asaf and Perlitz, Yotam and Bandel, Elron and Shmueli-Scheuer, Michal and Choshen, Leshem and Stanovsky, Gabriel},\n  title         = {Growing Pains: Extensible and Efficient {LLM} Benchmarking Via Fixed Parameter Calibration},\n  journal       = {arXiv preprint},\n  year          = {2026},\n  eprint        = {2604.12843},\n  archiveprefix = {arXiv},\n  url           = {https://arxiv.org/abs/2604.12843}\n}\n\n% KEY: xu2025emperor | STATUS: VERIFIED | SOURCE: arXiv 2503.16402, ICML 2025\n% NOTE: The existing bib entry had WRONG authors (Xu, Yiwen; Song, Kaijie; Zhou, Jianfeng; Chen, Liang).\n%       The real authors are Yifan Sun, Han Wang, Dongbai Li, Gang Wang, and Huan Zhang.\n%       Also the title in the old entry was slightly paraphrased. Corrected below.\n@inproceedings{xu2025emperor,\n  author    = {Sun, Yifan and Wang, Han and Li, Dongbai and Wang, Gang and Zhang, Huan},\n  title     = {The Emperor's New Clothes in Benchmarking? {A} Rigorous Examination of Mitigation Strategies for {LLM} Benchmark Data Contamination},\n  booktitle = {Proceedings of the 42nd International Conference on Machine Learning (ICML)},\n  year      = {2025},\n  eprint    = {2503.16402},\n  archiveprefix = {arXiv},\n  url       = {https://arxiv.org/abs/2503.16402}\n}\n\n% KEY: wust2025selfcritique / wust_2025_selfcritique | STATUS: REPLACED | SOURCE: arXiv 2510.09259\n% NOTE: CONFIRMED HALLUCINATION. The original entry attributed this to fabricated authors\n%       \"Wust, Timon; Hoffmann, Jan; Pang, Richard Yuanzhe\" with a fake title about\n%       \"Self-Critique as a Contamination Signal: Detecting Memorization via Entropy Collapse\".\n%       The real paper at arXiv 2510.09259 is by Tao et al. and is titled\n%       \"Detecting Data Contamination from Reinforcement Learning Post-training for LLMs\".\n%       It proposes \"Self-Critique\" method. Paper is on OpenReview (ICLR 2026 submission).\n@article{wust2025selfcritique,\n  author        = {Tao, Yongding and Wang, Tian and Dong, Yihong and Liu, Huanyu and Zhang, Kechi and Hu, Xiaolong and Li, Ge},\n  title         = {Detecting Data Contamination from Reinforcement Learning Post-training for Large Language Models},\n  journal       = {arXiv preprint},\n  year          = {2025},\n  eprint        = {2510.09259},\n  archiveprefix = {arXiv},\n  url           = {https://arxiv.org/abs/2510.09259}\n}\n\n% KEY: wust_2025_selfcritique | STATUS: REPLACED | SOURCE: arXiv 2510.09259\n% NOTE: Same as wust2025selfcritique above. Duplicate key variant.\n@article{wust_2025_selfcritique,\n  author        = {Tao, Yongding and Wang, Tian and Dong, Yihong and Liu, Huanyu and Zhang, Kechi and Hu, Xiaolong and Li, Ge},\n  title         = {Detecting Data Contamination from Reinforcement Learning Post-training for Large Language Models},\n  journal       = {arXiv preprint},\n  year          = {2025},\n  eprint        = {2510.09259},\n  archiveprefix = {arXiv},\n  url           = {https://arxiv.org/abs/2510.09259}\n}\n\n% =============================================================================\n% NEW ENTRY (requested addition)\n% =============================================================================\n\n% KEY: kadavath_2022_self_eval | STATUS: VERIFIED | SOURCE: arXiv 2207.05221\n@article{kadavath_2022_self_eval,\n  author        = {Kadavath, Saurav and Conerly, Tom and Askell, Amanda and Henighan, Tom and Drain, Dawn and Perez, Ethan and Schiefer, Nicholas and Hatfield-Dodds, Zac and DasSarma, Nova and Tran-Johnson, Eli and Johnston, Scott and El-Showk, Sheer and Jones, Andy and Elhage, Nelson and Hume, Tristan and Chen, Anna and Bai, Yuntao and Bowman, Sam and Fort, Stanislav and Ganguli, Deep and Hernandez, Danny and Jacobson, Josh and Kernion, Jackson and Kravec, Shauna and Lovitt, Liane and Ndousse, Kamal and Olsson, Catherine and Ringer, Sam and Amodei, Dario and Brown, Tom and Clark, Jack and Joseph, Nicholas and Mann, Ben and McCandlish, Sam and Olah, Chris and Kaplan, Jared},\n  title         = {Language Models (Mostly) Know What They Know},\n  journal       = {arXiv preprint},\n  year          = {2022},\n  eprint        = {2207.05221},\n  archiveprefix = {arXiv},\n  url           = {https://arxiv.org/abs/2207.05221}\n}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_bib_rebuild_2025plus_20260517T051927",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/bib_rebuild_2025plus.bib",
    "content": "% =============================================================================\n% BIB REBUILD: 2025+ Citations Verification\n% Generated: 2026-05-17\n% =============================================================================\n\n% KEY: chang2025benchmarking | STATUS: VERIFIED | SOURCE: ACM TIST 2024, arXiv 2307.03109\n% NOTE: Published in 2024 (not 2025). Journal article in ACM TIST Vol.15 No.3.\n%       The bib key says \"2025\" but the paper was published March 2024.\n%       Venue in existing bib (\"EMNLP 2025\") is WRONG -- it is ACM TIST 2024.\n@article{chang2025benchmarking,\n  author    = {Chang, Yupeng and Wang, Xu and Wang, Jindong and Wu, Yuan and Yang, Linyi and Zhu, Kaijie and Chen, Hao and Yi, Xiaoyuan and Wang, Cunxiang and Wang, Yidong and Ye, Wei and Zhang, Yue and Chang, Yi and Yu, Philip S. and Yang, Qiang and Xie, Xing},\n  title     = {A Survey on Evaluation of Large Language Models},\n  journal   = {ACM Transactions on Intelligent Systems and Technology},\n  volume    = {15},\n  number    = {3},\n  pages     = {1--45},\n  year      = {2024},\n  doi       = {10.1145/3641289},\n  eprint    = {2307.03109},\n  archiveprefix = {arXiv},\n  url       = {https://arxiv.org/abs/2307.03109}\n}\n\n% KEY: duan2025minkpp | STATUS: REPLACED | SOURCE: arXiv 2404.02936, ICLR 2025 Spotlight\n% NOTE: The original entry listed fabricated authors \"Duan, Jiawen; Xie, Cheng; Zhang, Jian; Li, Kai\".\n%       The real Min-K%++ paper is by Zhang, Jingyang et al. This is the same paper already\n%       correctly entered as zhang_2024_minkpp in the main bib. Keeping corrected version here.\n@inproceedings{duan2025minkpp,\n  author    = {Zhang, Jingyang and Sun, Jingwei and Yeats, Eric and Ouyang, Yang and Kuo, Martin and Zhang, Jianyi and Yang, Hao Frank and Li, Hai},\n  title     = {{Min-K\\%++}: Improved Baseline for Detecting Pre-Training Data from Large Language Models},\n  booktitle = {Proceedings of the 13th International Conference on Learning Representations (ICLR)},\n  year      = {2025},\n  note      = {Spotlight. arXiv:2404.02936},\n  eprint    = {2404.02936},\n  archiveprefix = {arXiv},\n  url       = {https://arxiv.org/abs/2404.02936}\n}\n\n% KEY: habba_2025_growing_pains | STATUS: VERIFIED | SOURCE: arXiv 2604.12843\n% NOTE: The existing bib entry had WRONG authors (listed Polo, Mamani, Zhuang, Xu, Choshen,\n%       Yurochkin, Sun). The real authors are Habba, Itzhak, Yehudai, Perlitz, Bandel,\n%       Shmueli-Scheuer, Choshen, Stanovsky. Also the year is 2026 (April 2026), not 2025.\n%       First author is \"Eliya Habba\" not \"Maryam Habba\".\n@article{habba_2025_growing_pains,\n  author        = {Habba, Eliya and Itzhak, Itay and Yehudai, Asaf and Perlitz, Yotam and Bandel, Elron and Shmueli-Scheuer, Michal and Choshen, Leshem and Stanovsky, Gabriel},\n  title         = {Growing Pains: Extensible and Efficient {LLM} Benchmarking Via Fixed Parameter Calibration},\n  journal       = {arXiv preprint},\n  year          = {2026},\n  eprint        = {2604.12843},\n  archiveprefix = {arXiv},\n  url           = {https://arxiv.org/abs/2604.12843}\n}\n\n% KEY: li_2025_dcr / li2025dcr | STATUS: NOT_FOUND | SOURCE: N/A\n% NOTE: No paper titled \"Decontaminated Calibration and Ranking for Trustworthy LLM Evaluation\"\n%       by \"Li, Yucheng; Flanigan, Frank; Sherborne, Tom; Sherborne, Charlie\" exists.\n%       This appears to be a HALLUCINATION. The real \"DCR\" paper at EMNLP 2025 is\n%       \"DCR: Quantifying Data Contamination in LLMs Evaluation\" by Cheng Xu et al.\n%       (arXiv 2507.11405). That paper is already in the bib as xu_2025_dcr.\n%       Yucheng Li's real EMNLP 2024 paper is \"An Open-Source Data Contamination Report\n%       for Large Language Models\" (arXiv 2310.17589).\n%       SUGGESTED REPLACEMENT: Use xu_2025_dcr for DCR-related citations, or cite\n%       Yucheng Li's actual 2024 paper if contamination reporting is the intended context.\n% --- Option A: Alias to the real DCR paper (Xu et al. EMNLP 2025) ---\n@inproceedings{li_2025_dcr,\n  author    = {Xu, Cheng and Yan, Nan and Guan, Shuhao and Jin, Changhong and Mei, Yuke and Guo, Yibing and Kechadi, Tahar},\n  title     = {{DCR}: Quantifying Data Contamination in {LLMs} Evaluation},\n  booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  pages     = {23002--23020},\n  year      = {2025},\n  eprint    = {2507.11405},\n  archiveprefix = {arXiv},\n  url       = {https://aclanthology.org/2025.emnlp-main.1173/}\n}\n\n% KEY: luettgau_2025_hibayes | STATUS: VERIFIED | SOURCE: arXiv 2505.05602\n% NOTE: The existing bib entry had WRONG authors (listed Polo, Zhuang, Yurochkin, Sun).\n%       The real authors are from the UK AI Safety Institute.\n@article{luettgau_2025_hibayes,\n  author        = {Luettgau, Lennart and Coppock, Harry and Dubois, Magda and Summerfield, Christopher and Ududec, Cozmin},\n  title         = {{HiBayES}: A Hierarchical {Bayesian} Modeling Framework for {AI} Evaluation Statistics},\n  journal       = {arXiv preprint},\n  year          = {2025},\n  eprint        = {2505.05602},\n  archiveprefix = {arXiv},\n  url           = {https://arxiv.org/abs/2505.05602}\n}\n\n% KEY: polo2026growing | STATUS: REPLACED | SOURCE: arXiv 2604.12843\n% NOTE: This is the SAME paper as habba_2025_growing_pains (arXiv 2604.12843).\n%       The existing entry had completely wrong authors (Polo, Mamani, Zhuang, Xu, Choshen,\n%       Yurochkin, Sun) and wrong title framing. Polo is NOT an author of this paper.\n%       Corrected to match the real paper. Consider merging with habba_2025_growing_pains.\n@article{polo2026growing,\n  author        = {Habba, Eliya and Itzhak, Itay and Yehudai, Asaf and Perlitz, Yotam and Bandel, Elron and Shmueli-Scheuer, Michal and Choshen, Leshem and Stanovsky, Gabriel},\n  title         = {Growing Pains: Extensible and Efficient {LLM} Benchmarking Via Fixed Parameter Calibration},\n  journal       = {arXiv preprint},\n  year          = {2026},\n  eprint        = {2604.12843},\n  archiveprefix = {arXiv},\n  url           = {https://arxiv.org/abs/2604.12843}\n}\n\n% KEY: xu2025emperor | STATUS: VERIFIED | SOURCE: arXiv 2503.16402, ICML 2025\n% NOTE: The existing bib entry had WRONG authors (Xu, Yiwen; Song, Kaijie; Zhou, Jianfeng; Chen, Liang).\n%       The real authors are Yifan Sun, Han Wang, Dongbai Li, Gang Wang, and Huan Zhang.\n%       Also the title in the old entry was slightly paraphrased. Corrected below.\n@inproceedings{xu2025emperor,\n  author    = {Sun, Yifan and Wang, Han and Li, Dongbai and Wang, Gang and Zhang, Huan},\n  title     = {The Emperor's New Clothes in Benchmarking? {A} Rigorous Examination of Mitigation Strategies for {LLM} Benchmark Data Contamination},\n  booktitle = {Proceedings of the 42nd International Conference on Machine Learning (ICML)},\n  year      = {2025},\n  eprint    = {2503.16402},\n  archiveprefix = {arXiv},\n  url       = {https://arxiv.org/abs/2503.16402}\n}\n\n% KEY: wust2025selfcritique / wust_2025_selfcritique | STATUS: REPLACED | SOURCE: arXiv 2510.09259\n% NOTE: CONFIRMED HALLUCINATION. The original entry attributed this to fabricated authors\n%       \"Wust, Timon; Hoffmann, Jan; Pang, Richard Yuanzhe\" with a fake title about\n%       \"Self-Critique as a Contamination Signal: Detecting Memorization via Entropy Collapse\".\n%       The real paper at arXiv 2510.09259 is by Tao et al. and is titled\n%       \"Detecting Data Contamination from Reinforcement Learning Post-training for LLMs\".\n%       It proposes \"Self-Critique\" method. Paper is on OpenReview (ICLR 2026 submission).\n@article{wust2025selfcritique,\n  author        = {Tao, Yongding and Wang, Tian and Dong, Yihong and Liu, Huanyu and Zhang, Kechi and Hu, Xiaolong and Li, Ge},\n  title         = {Detecting Data Contamination from Reinforcement Learning Post-training for Large Language Models},\n  journal       = {arXiv preprint},\n  year          = {2025},\n  eprint        = {2510.09259},\n  archiveprefix = {arXiv},\n  url           = {https://arxiv.org/abs/2510.09259}\n}\n\n% KEY: wust_2025_selfcritique | STATUS: REPLACED | SOURCE: arXiv 2510.09259\n% NOTE: Same as wust2025selfcritique above. Duplicate key variant.\n@article{wust_2025_selfcritique,\n  author        = {Tao, Yongding and Wang, Tian and Dong, Yihong and Liu, Huanyu and Zhang, Kechi and Hu, Xiaolong and Li, Ge},\n  title         = {Detecting Data Contamination from Reinforcement Learning Post-training for Large Language Models},\n  journal       = {arXiv preprint},\n  year          = {2025},\n  eprint        = {2510.09259},\n  archiveprefix = {arXiv},\n  url           = {https://arxiv.org/abs/2510.09259}\n}\n\n% =============================================================================\n% NEW ENTRY (requested addition)\n% =============================================================================\n\n% KEY: kadavath_2022_self_eval | STATUS: VERIFIED | SOURCE: arXiv 2207.05221\n@article{kadavath_2022_self_eval,\n  author        = {Kadavath, Saurav and Conerly, Tom and Askell, Amanda and Henighan, Tom and Drain, Dawn and Perez, Ethan and Schiefer, Nicholas and Hatfield-Dodds, Zac and DasSarma, Nova and Tran-Johnson, Eli and Johnston, Scott and El-Showk, Sheer and Jones, Andy and Elhage, Nelson and Hume, Tristan and Chen, Anna and Bai, Yuntao and Bowman, Sam and Fort, Stanislav and Ganguli, Deep and Hernandez, Danny and Jacobson, Josh and Kernion, Jackson and Kravec, Shauna and Lovitt, Liane and Ndousse, Kamal and Olsson, Catherine and Ringer, Sam and Amodei, Dario and Brown, Tom and Clark, Jack and Joseph, Nicholas and Mann, Ben and McCandlish, Sam and Olah, Chris and Kaplan, Jared},\n  title         = {Language Models (Mostly) Know What They Know},\n  journal       = {arXiv preprint},\n  year          = {2022},\n  eprint        = {2207.05221},\n  archiveprefix = {arXiv},\n  url           = {https://arxiv.org/abs/2207.05221}\n}\n"
  }
}
```

</details>

---

### Tool result

_source line 77 · 2026-05-17T05:24:49.045154+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/bib_rebuild_2025plus.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_bib_rebuild_2025plus_20260517T051927",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 78 · 2026-05-17T05:24:49.045360+00:00_

The rebuilt bib file has been written to `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/bib_rebuild_2025plus.bib`.

Summary of findings:

| Key | Status | Issue |
|-----|--------|-------|
| `chang2025benchmarking` | VERIFIED | Wrong venue (not EMNLP 2025; actually ACM TIST 2024). Correct arXiv ID 2307.03109. |
| `duan2025minkpp` | REPLACED | Fabricated authors. Real Min-K%++ paper is by Zhang Jingyang et al. (arXiv 2404.02936, ICLR 2025 Spotlight). Duplicate of existing `zhang_2024_minkpp`. |
| `habba_2025_growing_pains` | VERIFIED | Wrong authors (listed Polo/Mamani/Zhuang; real authors: Habba Eliya, Itzhak, Yehudai, Perlitz, Bandel, Shmueli-Scheuer, Choshen, Stanovsky). First name is "Eliya" not "Maryam". Year is 2026. |
| `li_2025_dcr` / `li2025dcr` | NOT_FOUND | Complete hallucination. No paper "Decontaminated Calibration and Ranking" by Li Yucheng exists. The real DCR paper at EMNLP 2025 is by Cheng Xu et al. (arXiv 2507.11405), already in the bib as `xu_2025_dcr`. |
| `luettgau_2025_hibayes` | VERIFIED | Wrong authors (listed Polo/Zhuang/Yurochkin/Sun; real authors: Luettgau, Coppock, Dubois, Summerfield, Ududec from UK AI Safety Institute). Correct arXiv 2505.05602. |
| `polo2026growing` | REPLACED | Same paper as `habba_2025_growing_pains` (arXiv 2604.12843). Polo is NOT an author. |
| `xu2025emperor` | VERIFIED | Wrong authors (listed Xu Yiwen/Song/Zhou/Chen; real authors: Yifan Sun, Han Wang, Dongbai Li, Gang Wang, Huan Zhang). Correct arXiv 2503.16402, ICML 2025. |
| `wust2025selfcritique` | REPLACED | Confirmed hallucination. Real paper at arXiv 2510.09259 is "Detecting Data Contamination from Reinforcement Learning Post-training for LLMs" by Tao Yongding et al. On OpenReview for ICLR 2026. |
| `kadavath_2022_self_eval` | VERIFIED (new) | arXiv 2207.05221, Kadavath et al. 2022, 35 authors from Anthropic. |

Key pattern: Most entries had the correct arXiv IDs but **fabricated author lists** and sometimes sli
…[truncated 273 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_bib_rebuild_2025plus_20260517T051927",
  "tool": "Agent",
  "elapsed_ms": 13
}
```

</details>

---

### Tool call

_source line 79 · 2026-05-17T05:24:49.045538+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/bib_rebuild_2025plus.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_bib_rebuild_2025plus_20260517T051927",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/bib_rebuild_2025plus.bib"
  }
}
```

</details>

---

### Tool result

_source line 80 · 2026-05-17T05:24:49.045732+00:00_

1	% =============================================================================
2	% BIB REBUILD: 2025+ Citations Verification
3	% Generated: 2026-05-17
4	% =============================================================================
5	
6	% KEY: chang2025benchmarking | STATUS: VERIFIED | SOURCE: ACM TIST 2024, arXiv 2307.03109
7	% NOTE: Published in 2024 (not 2025). Journal article in ACM TIST Vol.15 No.3.
8	%       The bib key says "2025" but the paper was published March 2024.
9	%       Venue in existing bib ("EMNLP 2025") is WRONG -- it is ACM TIST 2024.
10	@article{chang2025benchmarking,
11	  author    = {Chang, Yupeng and Wang, Xu and Wang, Jindong and Wu, Yuan and Yang, Linyi and Zhu, Kaijie and Chen, Hao and Yi, Xiaoyuan and Wang, Cunxiang and Wang, Yidong and Ye, Wei and Zhang, Yue and Chang, Yi and Yu, Philip S. and Yang, Qiang and Xie, Xing},
12	  title     = {A Survey on Evaluation of Large Language Models},
13	  journal   = {ACM Transactions on Intelligent Systems and Technology},
14	  volume    = {15},
15	  number    = {3},
16	  pages     = {1--45},
17	  year      = {2024},
18	  doi       = {10.1145/3641289},
19	  eprint    = {2307.03109},
20	  archiveprefix = {arXiv},
21	  url       = {https://arxiv.org/abs/2307.03109}
22	}
23	
24	% KEY: duan2025minkpp | STATUS: REPLACED | SOURCE: arXiv 2404.02936, ICLR 2025 Spotlight
25	% NOTE: The original entry listed fabricated authors "Duan, Jiawen; Xie, Cheng; Zhang, Jian; Li, Kai".
26	%       The real Min-K%++ paper is by Zhang, Jingyang et al. This is the same paper already
27	%       correctly entered as zhang_2024_minkpp in the main bib. Keeping corrected version here.
28	@inproceedings{duan2025minkpp,
29	  author    = {Zhang, Jingyang and Sun, Jingwei and Yeats, Eric and Ouyang, Yang and Kuo, Martin and Zhang, Jianyi and Yang, Hao Frank and Li, Hai},
30	  title     = {{Min-K\%++}: Improved Baseline for Detecting Pre-Training Data from Large Language Models},
31	  booktitle = {Proceedings of the 13th Intern
…[truncated 8309 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_bib_rebuild_2025plus_20260517T051927",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 81 · 2026-05-17T05:24:49.045928+00:00_

文件已生成。验证结果汇总：

| Key | 状态 | 问题 |
|-----|------|------|
| `chang2025benchmarking` | VERIFIED | 年份实为 2024，venue 是 ACM TIST（非 EMNLP 2025） |
| `duan2025minkpp` | REPLACED | 作者全部捏造，实际是 Zhang et al. ICLR 2025（与现有 `zhang_2024_minkpp` 重复） |
| `habba_2025_growing_pains` | VERIFIED | 作者列表全错，年份实为 2026，arXiv 2604.12843 |
| `li_2025_dcr` | NOT_FOUND | 完全幻觉，不存在该论文。真正 DCR 是 Xu et al. EMNLP 2025（已有 `xu_2025_dcr`） |
| `luettgau_2025_hibayes` | VERIFIED | 作者全错（原写 Polo 等人），实际是 UK AI Safety Institute 团队，arXiv 2505.05602 |
| `polo2026growing` | REPLACED | 与 `habba_2025_growing_pains` 是同一篇，Polo 非该文作者 |
| `xu2025emperor` | VERIFIED | 作者全错，实为 Sun Yifan 等，ICML 2025，arXiv 2503.16402 |
| `wust2025selfcritique` | REPLACED | 确认幻觉，替换为 Tao et al. arXiv 2510.09259 |
| `kadavath_2022_self_eval` | NEW | 已添加，arXiv 2207.05221 |

需要决策：
- `duan2025minkpp` 与已有 `zhang_2024_minkpp` 重复，tex 中是否统一改用后者？
- `li_2025_dcr` 是幻觉，引用上下文需要改用 `xu_2025_dcr` 还是 Li Yucheng 2024 的 contamination report？
- `polo2026growing` 与 `habba_2025_growing_pains` 同一论文，需合并 key。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_bib_rebuild_2025plus_20260517T051927"
}
```

</details>

---
