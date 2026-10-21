# paper research citation fill

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 49
- **Recorded user turns:** 0
- **Tool calls:** 24
- **Original source:** `logs/chats/worker_paper_research_citation_fill_20260521T101219.jsonl`
- **Structured JSON:** [`97104a9652a70a398be1.json`](../../sessions/97/97104a9652a70a398be1.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

49 recorded events

### Tool call

_source line 1 · 2026-05-21T10:17:18.463435+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_citation_fill_20260521T101219",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/references.bib"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-21T10:17:18.463831+00:00_

1	@inproceedings{murugadoss2025sos,
2	  title={Style Over Substance: Failure Modes of {LLM} Judges in Alignment Benchmarking},
3	  author={Murugadoss, Aakanksha and others},
4	  booktitle={Proceedings of the International Conference on Learning Representations (ICLR)},
5	  year={2025},
6	  url={https://arxiv.org/abs/2409.15268}
7	}
8	
9	@inproceedings{li2026preference,
10	  title={Preference Leakage: A Contamination Problem in {LLM}-as-a-Judge},
11	  author={Li, Dawei and others},
12	  booktitle={Proceedings of the International Conference on Learning Representations (ICLR)},
13	  year={2026},
14	  url={https://arxiv.org/abs/2502.01534}
15	}
16	
17	@article{wang2026fairjudge,
18	  title={{FairJudge}: An Adaptive, Debiased, and Consistent {LLM}-as-a-Judge},
19	  author={Yang, Bo and Feng, Lanfei and Chen, Yunkui and Zhang, Yu and Xu, Xiao and Li, Shijian},
20	  journal={arXiv preprint arXiv:2602.06625},
21	  year={2026},
22	  url={https://arxiv.org/abs/2602.06625}
23	}
24	
25	
26	@inproceedings{dubois2025lc,
27	  title={Length-Controlled {AlpacaEval}: A Simple Way to Debias Automatic Evaluators},
28	  author={Dubois, Yann and others},
29	  booktitle={Proceedings of the International Conference on Learning Representations (ICLR)},
30	  year={2025},
31	  url={https://arxiv.org/abs/2404.04475}
32	}
33	
34	@article{casse2026concise,
35	  title={A Concise Agent is Less Expert: Revealing Side Effects of Using Style Features on Conversational Agents},
36	  author={Cho, Young-Min and Yuan, Yuan and Guntuku, Sharath Chandra and Ungar, Lyle},
37	  journal={arXiv preprint arXiv:2601.10809},
38	  year={2026},
39	  url={https://arxiv.org/abs/2601.10809}
40	}
41	
42	@article{counterfactual2025rhetorical,
43	  title={Counterfactual {LLM}-based Framework for Measuring Rhetorical Style},
44	  author={Qiu, Jingyi and Chen, Hong and Li, Zongyi},
45	  journal={arXiv preprint arXiv:2512.19908},
46	  year={2025},
47	  url={https://arxiv.org/abs/2512.19908}
48	}
49	
50	@article{soumik2026j
…[truncated 7759 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_citation_fill_20260521T101219",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-21T10:17:18.464039+00:00_

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
  "session": "worker_paper_research_citation_fill_20260521T101219",
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

_source line 4 · 2026-05-21T10:17:18.464202+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_citation_fill_20260521T101219",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-21T10:17:18.464405+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CausaLM Feder 2021 counterfactual text generation causal reasoning Computational Linguistics"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_citation_fill_20260521T101219",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CausaLM Feder 2021 counterfactual text generation causal reasoning Computational Linguistics"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-21T10:17:18.464577+00:00_

Web search results for query: "CausaLM Feder 2021 counterfactual text generation causal reasoning Computational Linguistics"

Links: [{"title":"CausaLM: Causal Model Explanation Through Counterfactual Language Models - ACL Anthology","url":"https://aclanthology.org/2021.cl-2.13/"},{"title":"Quantifying Symptom Causality in Clinical Decision Making: An Exploration Using CausaLM","url":"https://arxiv.org/html/2503.19394"},{"title":"Causalm: Causal model explanation through counterfactual language models - Technion - Israel Institute of Technology","url":"https://cris.technion.ac.il/en/publications/causalm-causal-model-explanation-through-counterfactual-language-/"},{"title":"CausaLM: Causal Model Explanation Through Counterfactual Language Models | Computational Linguistics | MIT Press","url":"https://direct.mit.edu/coli/article/47/2/333/98518/CausaLM-Causal-Model-Explanation-Through"},{"title":"Causalm: Causal model explanation through counterfactual language models - Tel Aviv University","url":"https://cris.tau.ac.il/en/publications/causalm-causal-model-explanation-through-counterfactual-language-/"},{"title":"(PDF) CausaLM: Causal Model Explanation Through Counterfactual Language Models","url":"https://www.researchgate.net/publication/350482062_CausaLM_Causal_Model_Explanation_Through_Counterfactual_Language_Models"},{"title":"CausaLM: Causal Model Explanation Through Counterfactual Language Models","url":"https://dev.datascienceassn.org/sites/default/files/pdf_files/CausaLM%20Causal%20Model%20Explanation%20Through%20Counterfactual%20Language%20Models.pdf"},{"title":"GitHub - amirfeder/CausaLM: CausaLM: Causal Model Explanation Through Counterfactual Language Models","url":"https://github.com/amirfeder/CausaLM"},{"title":"[PDF] CausaLM: Causal Model Explanation Through Counterfactual Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/CausaLM:-Causal-Model-Explanation-Through-Language-Feder-Oved/4f0318290bc75294338fdeb450e4365929b3aa0c"
…[truncated 1428 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_citation_fill_20260521T101219",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-21T10:17:18.464746+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Polyjuice Wu 2021 counterfactual text edits ACL 2021"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_citation_fill_20260521T101219",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Polyjuice Wu 2021 counterfactual text edits ACL 2021"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-21T10:17:18.464897+00:00_

Web search results for query: "Polyjuice Wu 2021 counterfactual text edits ACL 2021"

Links: [{"title":"Polyjuice: Generating Counterfactuals for Explaining, Evaluating, and Improving Models - ACL Anthology","url":"https://aclanthology.org/2021.acl-long.523/"},{"title":"Polyjuice: Generating Counterfactuals for Explaining, Evaluating, and Improving Models","url":"https://idl.uw.edu/papers/polyjuice"},{"title":"polyjuice-nlp · PyPI","url":"https://pypi.org/project/polyjuice-nlp/"},{"title":"uw-hai/polyjuice · Hugging Face","url":"https://huggingface.co/uw-hai/polyjuice"},{"title":"GitHub - tongshuangwu/polyjuice · GitHub","url":"https://github.com/tongshuangwu/polyjuice"},{"title":"Polyjuice: Generating Counterfactuals for Explaining, Evaluating, and Improving Models | Request PDF","url":"https://www.researchgate.net/publication/353484822_Polyjuice_Generating_Counterfactuals_for_Explaining_Evaluating_and_Improving_Models"},{"title":"ACL-IJCNLP 2021","url":"https://2021.aclweb.org/program/accept/"},{"title":"Explaining NLP Models via Minimal Contrastive Editing ( ...","url":"https://aclanthology.org/2021.findings-acl.336.pdf"},{"title":"[2101.00288] Polyjuice: Generating Counterfactuals for Explaining, Evaluating, and Improving Models","url":"https://arxiv.org/abs/2101.00288"}]

Based on the search results, here's what I found about Polyjuice:

Polyjuice is a general-purpose counterfactual generator that allows for control over perturbation types and locations, trained by finetuning GPT-2 on multiple datasets of paired sentences.

While counterfactual examples are useful for analysis and training of NLP models, current generation methods either rely on manual labor to create very few counterfactuals, or only instantiate limited types of perturbations such as paraphrases or word substitutions.

Polyjuice produces diverse sets of realistic counterfactuals, which in turn are useful in various distinct applications: improving training and evaluation on three different tas
…[truncated 625 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_citation_fill_20260521T101219",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-21T10:17:18.465043+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Clark 2021 \"All That's Human Is Not Gold\" evaluating human evaluation generated text ACL"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_citation_fill_20260521T101219",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Clark 2021 \"All That's Human Is Not Gold\" evaluating human evaluation generated text ACL"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-21T10:17:18.465190+00:00_

Web search results for query: "Clark 2021 "All That's Human Is Not Gold" evaluating human evaluation generated text ACL"

Links: [{"title":"Language, Logic and Information | [Reminder] NLP RG Thu-11-Nov at 15:00: All That's Human Is Not Gold (hosted)","url":"https://uilotslli.sites.uu.nl/2021/11/10/reminder-nlp-rg-thu-11-nov-at-1500-all-thats-human-is-not-gold-hosted/"},{"title":"Language, Logic and Information | NLP RG Thu-11-Nov at 15:00: All That's Human Is Not Gold (hosted)","url":"https://uilotslli.sites.uu.nl/2021/11/08/nlp-rg-thu-11-nov-at-1500-all-thats-human-is-not-gold-hosted/"},{"title":"All That's 'Human' Is Not Gold: Evaluating Human Evaluation of Generated   Text","url":"https://arxiv.org/pdf/2107.00061"},{"title":"The Authenticity Gap in Human Evaluation","url":"https://arxiv.org/pdf/2205.11930"},{"title":"A Gold Standard Methodology for Evaluating Accuracy in Data-To-Text   Systems","url":"https://arxiv.org/pdf/2011.03992"},{"title":"Statistical Multicriteria Evaluation of LLM-Generated Text","url":"https://arxiv.org/pdf/2506.18082"},{"title":"Dynamic Human Evaluation for Relative Model Comparisons","url":"https://arxiv.org/pdf/2112.08048"}]

Based on the search results, I found the paper you're looking for:

"All That's 'Human' Is Not Gold: Evaluating Human Evaluation of Generated Text" by Elizabeth Clark, Tal August, Sofia Serrano, Nikita Haduong, Suchin Gururangan, and Noah A. Smith was published at ACL 2021.

The paper addresses an important question: as models' fluency improves, how well can evaluators detect and judge machine-generated text?

Key findings from the study include:

- The researchers assessed nonexperts' ability to distinguish between human- and machine-authored text (GPT2 and GPT3) in three domains (stories, news articles, and recipes).

- Without training, evaluators distinguished between GPT3- and human-authored text at random chance level.

- While evaluators' accuracy improved up to 55% with training approaches (detailed inst
…[truncated 618 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_citation_fill_20260521T101219",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-21T10:17:18.465355+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Amidei 2019 Likert scales NLG evaluation INLG"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_citation_fill_20260521T101219",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Amidei 2019 Likert scales NLG evaluation INLG"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-21T10:17:18.465502+00:00_

Web search results for query: "Amidei 2019 Likert scales NLG evaluation INLG"

Links: [{"title":"The use of rating and Likert scales in Natural Language Generation human evaluation tasks: A review and some recommendations - ACL Anthology","url":"https://aclanthology.org/W19-8648/"},{"title":"The use of rating and Likert scales in Natural Language Generation human evaluation tasks: A review and some recommendations | Request PDF","url":"https://www.researchgate.net/publication/338053074_The_use_of_rating_and_Likert_scales_in_Natural_Language_Generation_human_evaluation_tasks_A_review_and_some_recommendations"},{"title":"Best practices for the human evaluation of automatically ...","url":"https://aclanthology.org/W19-8643.pdf"},{"title":"Best practices for the human evaluation of automatically generated text","url":"https://www.inlg2019.com/assets/papers/98_Paper.pdf"},{"title":"GitHub - jacopoamidei/Supplementary-material-INLG-2019","url":"https://github.com/jacopoamidei/Supplementary-material-INLG-2019"},{"title":"A Survey of Obstacles in Evaluation Practices for ...","url":"https://www.jair.org/index.php/jair/article/download/13715/26927/34555"},{"title":"[PDF] The use of rating and Likert scales in Natural Language Generation human evaluation tasks: A review and some recommendations | Semantic Scholar","url":"https://www.semanticscholar.org/paper/The-use-of-rating-and-Likert-scales-in-Natural-A-Amidei-Piwek/73b6a65b283c9c0602822420b11b260925a4cff1"},{"title":"The use of rating and Likert scales in Natural Language","url":"https://oro.open.ac.uk/67963/"},{"title":"The use of rating and Likert scales in Natural Language ...","url":"https://aclanthology.org/W19-8648.pdf"},{"title":"The use of rating and Likert scales in Natural Language ...","url":"https://www.inlg2019.com/assets/papers/57_Paper.pdf"}]

Based on the search results, I found the paper you're looking for:

The paper "The use of rating and Likert scales in Natural Language Generation human evaluation tas
…[truncated 943 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_citation_fill_20260521T101219",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-21T10:17:18.465651+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Boubdir 2023 \"Elo Uncovered\" robustness LLM evaluation Bradley-Terry"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_citation_fill_20260521T101219",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Boubdir 2023 \"Elo Uncovered\" robustness LLM evaluation Bradley-Terry"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-21T10:17:18.465795+00:00_

Web search results for query: "Boubdir 2023 "Elo Uncovered" robustness LLM evaluation Bradley-Terry"

Links: [{"title":"Elo Uncovered: Robustness and Best Practices in Language Model Evaluation | Request PDF","url":"https://www.researchgate.net/publication/397197352_Elo_Uncovered_Robustness_and_Best_Practices_in_Language_Model_Evaluation"},{"title":"[2311.17295v1] Elo Uncovered: Robustness and Best Practices in Language Model Evaluation","url":"http://export.arxiv.org/abs/2311.17295v1"},{"title":"Elo Uncovered: Robustness and Best Practices in Language Model Evaluation","url":"https://surrealyz.github.io/classes/llmsec-fall24/slides/22-ELO.pdf"},{"title":"[2311.17295] Elo Uncovered: Robustness and Best Practices in Language Model Evaluation","url":"https://arxiv.org/abs/2311.17295"},{"title":"Elo Uncovered: Robustness and Best Practices in Language Model Evaluation","url":"http://paperreading.club/page?id=196556"},{"title":"Elo Uncovered: Robustness and Best Practices in Language Model Evaluation - ACL Anthology","url":"https://aclanthology.org/2023.gem-1.28/"},{"title":"Elo Uncovered: Robustness and Best Practices in Language Model   Evaluation","url":"https://arxiv.org/pdf/2311.17295"},{"title":"Paper page - Elo Uncovered: Robustness and Best Practices in Language Model Evaluation","url":"https://huggingface.co/papers/2311.17295"},{"title":"Elo Uncovered: Robustness and Best Practices in Language Model Evaluation","url":"https://proceedings.neurips.cc/paper_files/paper/2024/hash/bfba8efb806a970455b83b852c9cf846-Abstract-Conference.html"},{"title":"Elo Uncovered: Robustness and Best Practices in Language Model Evaluation","url":"https://arxiv.org/html/2311.17295"}]

Based on the search results, I found information about the paper "Elo Uncovered: Robustness and Best Practices in Language Model Evaluation" by Boubdir and colleagues.

## Overview

The paper examines the Elo rating system, originally designed for ranking players in dynamic games such as chess, which is
…[truncated 1381 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_citation_fill_20260521T101219",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-21T10:17:18.465932+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Wu Aji 2023 style evaluation bias LLM judges"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_citation_fill_20260521T101219",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Wu Aji 2023 style evaluation bias LLM judges"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-21T10:17:18.466067+00:00_

Web search results for query: "Wu Aji 2023 style evaluation bias LLM judges"

Links: [{"title":"(PDF) Justice or Prejudice? Quantifying Biases in LLM-as-a-Judge","url":"https://www.researchgate.net/publication/384630680_Justice_or_Prejudice_Quantifying_Biases_in_LLM-as-a-Judge"},{"title":"Judging the Judges: A Systematic Evaluation of Bias Mitigation Strategies in LLM-as-a-Judge Pipelines","url":"https://arxiv.org/html/2604.23178v1"},{"title":"LLM Evaluators Recognize and Favor Their Own Generations","url":"https://www.researchgate.net/publication/397200002_LLM_Evaluators_Recognize_and_Favor_Their_Own_Generations"},{"title":"Grading Scale Impact on LLM-as-a-Judge: Human-LLM Alignment Is Highest on 0-5 Grading Scale","url":"https://arxiv.org/html/2601.03444v1"},{"title":"Justice or Prejudice? Quantifying Biases in LLM-as-a-Judge","url":"https://arxiv.org/html/2410.02736v1"},{"title":"Humans or LLMs as the Judge? A Study on Judgement Bias","url":"https://arxiv.org/html/2402.10669"},{"title":"Humans or LLMs as the Judge? A Study on Judgement Biases","url":"https://arxiv.org/html/2402.10669v2"},{"title":"Judging the Judges: A Systematic Evaluation of Bias Miti-","url":"https://arxiv.org/pdf/2604.23178"},{"title":"Humans or LLMs as the Judge? A Study on Judgement Bias Anonymous ACL submission","url":"https://openreview.net/pdf/11860ac4da20a2218eb96b78c49f43912297949f.pdf"}]

Based on the search results, I found information about Wu & Aji's work on evaluation biases in LLM judges:

Wu & Aji (2024) documented style bias as one of the systematic biases in LLM judges, along with other biases like position bias and verbosity bias. Their research found that LLM judges prioritize stylistic fluency over factual accuracy.

Wu & Aji (2023) demonstrated that the limited size and scope of test data increase the risk of random interference, potentially obscuring the true extent of bias in LLM judgments. This points to an important methodological consideration in studying LLM evaluati
…[truncated 426 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_citation_fill_20260521T101219",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-21T10:17:18.466209+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Wu Aji 2023 \"style over substance\" evaluation biases large language models arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_citation_fill_20260521T101219",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Wu Aji 2023 \"style over substance\" evaluation biases large language models arxiv"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-21T10:17:18.466368+00:00_

Web search results for query: "Wu Aji 2023 "style over substance" evaluation biases large language models arxiv"

Links: [{"title":"[PDF] Style Over Substance: Evaluation Biases for Large Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Style-Over-Substance:-Evaluation-Biases-for-Large-Wu-Aji/7ace46ab8e71c4304682ab126b1212deb54b9b03"},{"title":"Large Language Models are Inconsistent and Biased Evaluators","url":"https://arxiv.org/html/2405.01724v1"},{"title":"Benchmarking Cognitive Biases in Large Language Models as Evaluators","url":"https://arxiv.org/html/2309.17012v3"},{"title":"LLMs are Biased Evaluators But Not Biased for Retrieval Augmented Generation","url":"https://arxiv.org/html/2410.20833v1"},{"title":"[2307.03025] Style Over Substance: Evaluation Biases for Large Language Models","url":"https://arxiv.org/abs/2307.03025"},{"title":"From Lists to Emojis: How Format Bias Affects Model Alignment","url":"https://arxiv.org/html/2409.11704"},{"title":"Style Over Substance: Evaluation Biases for Large Language Models","url":"https://www.researchgate.net/publication/372163436_Style_Over_Substance_Evaluation_Biases_for_Large_Language_Models"},{"title":"Style Over Substance: Evaluation Biases for Large Language Models","url":"https://arxiv.org/pdf/2307.03025"},{"title":"Large Language Models are Inconsistent and Biased Evaluators - arXiv.gg","url":"https://arxiv.gg/abs/2405.01724"}]

I've found the paper you're looking for. "Style Over Substance: Evaluation Biases for Large Language Models" is a 2023 paper by Minghao Wu and Alham Fikri Aji, published on arXiv (2307.03025).

The study investigates the behavior of crowd-sourced and expert annotators, as well as LLMs, when comparing outputs from different models, using a dataset of intentionally flawed machine-generated answers.

The research proposes independently evaluating machine-generated text across multiple dimensions, resulting in the Multi-Elo Rating System (MERS). Their empiric
…[truncated 486 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_citation_fill_20260521T101219",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-21T10:17:18.466532+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "pairwise comparison vs Likert rating LLM evaluation NLG 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_citation_fill_20260521T101219",
  "tool": "WebSearch",
  "tool_args": {
    "query": "pairwise comparison vs Likert rating LLM evaluation NLG 2024 2025"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-21T10:17:18.466673+00:00_

Web search results for query: "pairwise comparison vs Likert rating LLM evaluation NLG 2024 2025"

Links: [{"title":"PRePair: Pointwise Reasoning Enhance Pairwise Evaluating for Robust Instruction-Following Assessments","url":"https://arxiv.org/html/2406.12319v1"},{"title":"LLM-based NLG Evaluation: Current Status and Challenges | Computational Linguistics | MIT Press","url":"https://direct.mit.edu/coli/article/51/2/661/128807/LLM-based-NLG-Evaluation-Current-Status-and"},{"title":"The Comparative Trap: Pairwise Comparisons Amplifies Biased Preferences   of LLM Evaluators","url":"https://arxiv.org/pdf/2406.12319"},{"title":"Direct-Scoring NLG Evaluators Can Use Pairwise Comparisons Too","url":"https://arxiv.org/html/2509.05440v1"},{"title":"A reliable LLM-as-a-Judge framework for evaluating text ...","url":"https://aclanthology.org/2025.emnlp-main.796.pdf"},{"title":"LLM Comparative Assessment: Zero-shot NLG Evaluation through Pairwise Comparisons using Large Language Models - ACL Anthology","url":"https://aclanthology.org/2024.eacl-long.8/"},{"title":"LLM Comparative Assessment: Zero-shot NLG Evaluation through Pairwise   Comparisons using Large Language Models","url":"https://arxiv.org/pdf/2307.07889"},{"title":"Reference-Free Rating of LLM Responses via Latent Information","url":"https://hcai-munich.com/pubs/Girrbach2025Reference.pdf"}]

Based on the web search results, here's what recent research shows about pairwise comparison versus Likert rating for LLM-based NLG evaluation:

## Key Differences

In the pairwise approach, an LLM receives an instruction and two model-generated outputs and then chooses a higher-quality output, while in the pointwise approach, an LLM assigns a single score on a Likert scale to each generated output independently.

## Alignment with Human Preferences

The pairwise approach aligns closely with human preferences, achieving levels of agreement comparable to those among human annotators. Comparison-based approaches have seen considera
…[truncated 912 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_citation_fill_20260521T101219",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-21T10:17:18.466814+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Liusie 2024 \"LLM Comparative Assessment\" pairwise comparisons NLG evaluation EACL"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_citation_fill_20260521T101219",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Liusie 2024 \"LLM Comparative Assessment\" pairwise comparisons NLG evaluation EACL"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-21T10:17:18.466948+00:00_

Web search results for query: "Liusie 2024 "LLM Comparative Assessment" pairwise comparisons NLG evaluation EACL"

Links: [{"title":"LLM Comparative Assessment: Zero-shot NLG Evaluation through Pairwise Comparisons using Large Language Models - ACL Anthology","url":"https://aclanthology.org/2024.eacl-long.8/"},{"title":"dblp: LLM Comparative Assessment: Zero-shot NLG Evaluation through Pairwise Comparisons using Large Language Models.","url":"https://dblp.dagstuhl.de/rec/conf/eacl/LiusieMG24.html"},{"title":"Efficient LLM Comparative Assessment: a Product of Experts Framework for Pairwise Comparisons","url":"https://arxiv.org/html/2405.05894v2"},{"title":"Efficient LLM Comparative Assessment: A Product of Experts Framework for Pairwise Comparisons - ACL Anthology","url":"https://aclanthology.org/2024.emnlp-main.389/"},{"title":"Efficient LLM Comparative Assessment: a Product of","url":"https://scispace.com/pdf/efficient-llm-comparative-assessment-a-product-of-experts-3a4gdmipeh.pdf"},{"title":"LLM Comparative Assessment: Zero-shot NLG Evaluation through Pairwise Comparisons using Large Language Models | Request PDF","url":"https://www.researchgate.net/publication/393020372_LLM_Comparative_Assessment_Zero-shot_NLG_Evaluation_through_Pairwise_Comparisons_using_Large_Language_Models"},{"title":"[2307.07889v3] LLM Comparative Assessment: Zero-shot NLG Evaluation through Pairwise Comparisons using Large Language Models","url":"https://arxiv.org/abs/2307.07889v3"},{"title":"Efficient LLM Comparative Assessment: a Product of Experts Framework for   Pairwise Comparisons","url":"https://arxiv.org/pdf/2405.05894"}]

Based on the search results, I found the paper you're looking for:

"LLM Comparative Assessment: Zero-shot NLG Evaluation through Pairwise Comparisons using Large Language Models" by Adian Liusie, Potsawee Manakul, and Mark Gales, published at the 18th Conference of the European Chapter of the Association for Computational Linguistics (EACL 2024) in St. Julian's, 
…[truncated 642 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_citation_fill_20260521T101219",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-21T10:17:18.467093+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "counterfactual interventional text analysis causal inference NLP 2024 2025 style confounding"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_citation_fill_20260521T101219",
  "tool": "WebSearch",
  "tool_args": {
    "query": "counterfactual interventional text analysis causal inference NLP 2024 2025 style confounding"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-21T10:17:18.467237+00:00_

Web search results for query: "counterfactual interventional text analysis causal inference NLP 2024 2025 style confounding"

Links: [{"title":"Counterfactual Causal Inference in Natural Language with Large Language Models","url":"https://arxiv.org/html/2410.06392v1"},{"title":"[Literature Review] Counterfactual Causal Inference in Natural Language with Large Language Models","url":"https://www.themoonlight.io/en/review/counterfactual-causal-inference-in-natural-language-with-large-language-models"},{"title":"GitHub - zhijing-jin/CausalNLP_Papers: A reading list for papers on causality for natural language processing (NLP) · GitHub","url":"https://github.com/zhijing-jin/CausalNLP_Papers"},{"title":"Estimating Causal Effects of Text Interventions Leveraging LLMs","url":"https://arxiv.org/pdf/2410.21474"},{"title":"Causal Inference in Natural Language Processing: Estimation, Prediction, Interpretation and Beyond | Transactions of the Association for Computational Linguistics | MIT Press","url":"https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00511/113490/Causal-Inference-in-Natural-Language-Processing"},{"title":"Counterfactual Causal Inference in Natural Language with Large Language   Models","url":"https://arxiv.org/pdf/2410.06392"},{"title":"Counterfactual Interventions Reveal the Causal Effect of Relative Clause   Representations on Agreement Prediction","url":"https://arxiv.org/pdf/2105.06965"}]

Based on the search results, here's what I found regarding counterfactual interventional text analysis and causal inference in NLP for 2024-2025:

## Recent Work on Counterfactual Causal Inference in NLP

Recent research proposes end-to-end causal structure discovery and counterfactual inference methods from unstructured natural language text data. One approach uses LLMs to generate causal graphs describing relationships between events in text, then performs atomic interventions on sequences of events to infer consequences in counterfactual scenarios.

## Handling
…[truncated 1005 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_citation_fill_20260521T101219",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-21T10:17:18.467401+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Feder Causal Inference NLP survey 2022 TACL \"Causal Inference in Natural Language Processing\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_citation_fill_20260521T101219",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Feder Causal Inference NLP survey 2022 TACL \"Causal Inference in Natural Language Processing\""
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-21T10:17:18.467568+00:00_

Web search results for query: "Feder Causal Inference NLP survey 2022 TACL "Causal Inference in Natural Language Processing""

Links: [{"title":"Causal Inference in Natural Language Processing: Estimation, Prediction, Interpretation and Beyond - ACL Anthology","url":"https://aclanthology.org/2022.tacl-1.66/"},{"title":"GitHub - zhijing-jin/CausalNLP_Papers: A reading list for papers on causality for natural language processing (NLP) · GitHub","url":"https://github.com/zhijing-jin/CausalNLP_Papers"},{"title":"Causal Inference in Natural Language Processing: Estimation, Prediction, Interpretation and Beyond - Princeton University","url":"https://collaborate.princeton.edu/en/publications/causal-inference-in-natural-language-processing-estimation-predic/"},{"title":"Causal Inference in Natural Language Processing: Estimation, Prediction, Interpretation and Beyond","url":"https://ouci.dntb.gov.ua/en/works/leREMaJ9/"},{"title":"[2109.00725v1] Causal Inference in Natural Language Processing: Estimation, Prediction, Interpretation and Beyond","url":"https://arxiv.org/abs/2109.00725v1"},{"title":"[2109.00725] Causal Inference in Natural Language Processing: Estimation, Prediction, Interpretation and Beyond","url":"https://arxiv.org/abs/2109.00725"},{"title":"Causal Inference in Natural Language Processing:","url":"https://aclanthology.org/2022.tacl-1.66.pdf"},{"title":"Causal Inference with Large Language Model: A Survey","url":"https://arxiv.org/pdf/2409.09822"},{"title":"dblp: Causal Inference in Natural Language Processing: Estimation, Prediction, Interpretation and Beyond.","url":"https://dblp.org/rec/journals/tacl/FederKMPSWEGRRS22.html"}]

I found the paper you were looking for! Here are the key details:

**Title:** Causal Inference in Natural Language Processing: Estimation, Prediction, Interpretation and Beyond

**Authors:** Amir Feder, Katherine A. Keith, Emaad Manzoor, Reid Pryzant, Dhanya Sridhar, Zach Wood-Doughty, Jacob Eisenstein, Justin Grimmer, Roi Reichart, 
…[truncated 802 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_citation_fill_20260521T101219",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-21T10:17:18.467719+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Koo 2024 \"benchmarking cognitive biases\" LLM evaluators pairwise scoring"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_citation_fill_20260521T101219",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Koo 2024 \"benchmarking cognitive biases\" LLM evaluators pairwise scoring"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-21T10:17:18.467870+00:00_

Web search results for query: "Koo 2024 "benchmarking cognitive biases" LLM evaluators pairwise scoring"

Links: [{"title":"Benchmarking Cognitive Biases in Large Language Models as Evaluators - ACL Anthology","url":"https://aclanthology.org/2024.findings-acl.29/"},{"title":"Benchmarking Cognitive Biases in Large Language Models as Evaluators | Request PDF","url":"https://www.researchgate.net/publication/384209612_Benchmarking_Cognitive_Biases_in_Large_Language_Models_as_Evaluators"},{"title":"LLM Evaluators Recognize and Favor Their Own Generations Arjun Panickssery1","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/7f1f0218e45f5414c79c0679633e47bc-Paper-Conference.pdf"},{"title":"Benchmarking Cognitive Biases in Large Language Models as Evaluators - Experts@Minnesota","url":"https://experts.umn.edu/en/publications/benchmarking-cognitive-biases-in-large-language-models-as-evaluat/"},{"title":"[2309.17012] Benchmarking Cognitive Biases in Large Language Models as Evaluators","url":"https://arxiv.org/abs/2309.17012"},{"title":"The Comparative Trap: Pairwise Comparisons Amplifies Biased Preferences   of LLM Evaluators","url":"https://arxiv.org/pdf/2406.12319"},{"title":"Pairwise or Pointwise? Evaluating Feedback Protocols for ...","url":"https://arxiv.org/pdf/2504.14716"},{"title":"GitHub - minnesotanlp/cobbler: Code and data for Koo et al's ACL 2024 paper \"Benchmarking Cognitive Biases in Large Language Models as Evaluators\" · GitHub","url":"https://github.com/minnesotanlp/cobbler"},{"title":"Benchmarking Cognitive Biases in Large Language Models as Evaluators","url":"https://arxiv.org/html/2309.17012v3"}]

Based on the search results, here's what I found about the Koo et al. 2024 paper on benchmarking cognitive biases in LLM evaluators:

## Overview

The paper "Benchmarking Cognitive Biases in Large Language Models as Evaluators" was published in the Findings of the Association for Computational Linguistics: ACL 2024.

## Methodology

The work ass
…[truncated 1224 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_citation_fill_20260521T101219",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-21T10:17:18.468019+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Panickssery 2024 \"LLM Evaluators Recognize and Favor Their Own Generations\" NeurIPS self-preference bias"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_citation_fill_20260521T101219",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Panickssery 2024 \"LLM Evaluators Recognize and Favor Their Own Generations\" NeurIPS self-preference bias"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-21T10:17:18.468187+00:00_

Web search results for query: "Panickssery 2024 "LLM Evaluators Recognize and Favor Their Own Generations" NeurIPS self-preference bias"

Links: [{"title":"LLM Evaluators Recognize and Favor Their Own Generations [Quick Review]","url":"https://liner.com/review/llm-evaluators-recognize-and-favor-their-own-generations"},{"title":"NeurIPS Poster LLM Evaluators Recognize and Favor Their Own Generations","url":"https://neurips.cc/virtual/2024/poster/96672"},{"title":"LLM Evaluators Recognize and Favor Their Own Generations","url":"https://proceedings.neurips.cc/paper_files/paper/2024/hash/7f1f0218e45f5414c79c0679633e47bc-Abstract-Conference.html"},{"title":"LLM Evaluators Recognize and Favor Their Own Generations","url":"https://papers.nips.cc/paper_files/paper/2024/hash/7f1f0218e45f5414c79c0679633e47bc-Abstract-Conference.html"},{"title":"LLM Evaluators Recognize and Favor Their Own Generations Arjun Panickssery1","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/7f1f0218e45f5414c79c0679633e47bc-Paper-Conference.pdf"},{"title":"[2404.13076] LLM Evaluators Recognize and Favor Their Own Generations","url":"https://arxiv.org/abs/2404.13076"},{"title":"Do LLM Evaluators Prefer Themselves for a Reason?","url":"https://arxiv.org/pdf/2504.03846"},{"title":"Self-Preference Bias in LLM-as-a-Judge","url":"https://arxiv.org/html/2410.21819v2"},{"title":"Are LLM Evaluators Really Narcissists? Sanity Checking Self-Preference Evaluations","url":"https://arxiv.org/pdf/2601.22548"},{"title":"NeurIPS Self-Preference Bias in LLM-as-a-Judge","url":"https://neurips.cc/virtual/2024/106181"}]

I found the research you were looking for. Here's what I found about Panickssery et al.'s 2024 NeurIPS paper on LLM self-preference bias:

## Overview

Arjun Panickssery, Samuel R. Bowman, and Shi Feng published this work at NeurIPS 2024. The paper was also published on arXiv in April 2024.

## Main Findings

The research identifies self-preference bias, where an LLM evaluator scores it
…[truncated 888 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_citation_fill_20260521T101219",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-21T10:17:18.468353+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Boubdir \"Elo Uncovered\" full author list 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_citation_fill_20260521T101219",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Boubdir \"Elo Uncovered\" full author list 2023"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-21T10:17:18.468490+00:00_

Web search results for query: "Boubdir "Elo Uncovered" full author list 2023"

Links: [{"title":"[2311.17295] Elo Uncovered: Robustness and Best Practices in Language Model Evaluation","url":"https://arxiv.org/abs/2311.17295"},{"title":"Elo Uncovered: Robustness and Best Practices in Language Model Evaluation - ACL Anthology","url":"https://aclanthology.org/2023.gem-1.28/"},{"title":"[2311.17295v1] Elo Uncovered: Robustness and Best Practices in Language Model Evaluation","url":"http://export.arxiv.org/abs/2311.17295v1"},{"title":"Elo Uncovered: Robustness and Best Practices in Language Model Evaluation","url":"https://arxiv.org/html/2311.17295"},{"title":"Published as a conference paper at ICLR 2025 UNICBE: AN UNIFORMITY-DRIVEN","url":"https://www.arxiv.org/pdf/2502.11454"},{"title":"Elo Uncovered: Robustness and Best Practices in Language Model Evaluation","url":"https://proceedings.neurips.cc/paper_files/paper/2024/hash/bfba8efb806a970455b83b852c9cf846-Abstract-Conference.html"},{"title":"Elo Uncovered: Robustness and Best Practices in Language Model Evaluation | Request PDF","url":"https://www.researchgate.net/publication/397197352_Elo_Uncovered_Robustness_and_Best_Practices_in_Language_Model_Evaluation"},{"title":"NeurIPS Poster Elo Uncovered: Robustness and Best Practices in Language Model Evaluation","url":"https://neurips.cc/virtual/2024/poster/95297"}]

Based on the search results, the full author list for "Elo Uncovered: Robustness and Best Practices in Language Model Evaluation" from 2023 is: Meriem Boubdir, Edward Kim, Beyza Ermis, Sara Hooker, and Marzieh Fadaee.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_citation_fill_20260521T101219",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-21T10:17:18.468641+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "site:aclanthology.org \"CausaLM\" Feder Oved Shalit Reichart 2021 Computational Linguistics"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_citation_fill_20260521T101219",
  "tool": "WebSearch",
  "tool_args": {
    "query": "site:aclanthology.org \"CausaLM\" Feder Oved Shalit Reichart 2021 Computational Linguistics"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-21T10:17:18.468791+00:00_

Web search results for query: "site:aclanthology.org "CausaLM" Feder Oved Shalit Reichart 2021 Computational Linguistics"

Links: [{"title":"CausaLM: Causal Model Explanation Through Counterfactual Language Models | Computational Linguistics | MIT Press","url":"https://direct.mit.edu/coli/article/47/2/333/98518/"},{"title":"CausaLM: Causal Model Explanation Through Counterfactual Language Models - ACL Anthology","url":"https://aclanthology.org/2021.cl-2.13/"},{"title":"References – CORTEX","url":"https://cortex.gplsi.es/en/references/"},{"title":"(PDF) CausaLM: Causal Model Explanation Through Counterfactual Language Models","url":"https://www.researchgate.net/publication/350482062_CausaLM_Causal_Model_Explanation_Through_Counterfactual_Language_Models"},{"title":"Causalm: Causal model explanation through counterfactual language models - Technion - Israel Institute of Technology","url":"https://cris.technion.ac.il/en/publications/causalm-causal-model-explanation-through-counterfactual-language-/"},{"title":"Causalm: Causal model explanation through counterfactual language models - Tel Aviv University","url":"https://cris.tau.ac.il/en/publications/causalm-causal-model-explanation-through-counterfactual-language-/"},{"title":"[PDF] Causal Inference in Natural Language Processing: Estimation, Prediction, Interpretation and Beyond | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Causal-Inference-in-Natural-Language-Processing:-Feder-Keith/130d432ccbc836380a212bea618f84ff094a6a52"},{"title":"[PDF] CausaLM: Causal Model Explanation Through Counterfactual Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/CausaLM:-Causal-Model-Explanation-Through-Language-Feder-Oved/4f0318290bc75294338fdeb450e4365929b3aa0c"},{"title":"Publications - Amir Feder","url":"https://amirfeder.github.io/publications/"},{"title":"CausaLM: Causal Model Explanation Through Counterfactual Language Models - ADS","url":"https://ui.adsabs.harvard.edu/abs/2020
…[truncated 791 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_citation_fill_20260521T101219",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-21T10:17:18.468939+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "site:aclanthology.org Clark August Serrano \"All That's Human Is Not Gold\" ACL 2021"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_citation_fill_20260521T101219",
  "tool": "WebSearch",
  "tool_args": {
    "query": "site:aclanthology.org Clark August Serrano \"All That's Human Is Not Gold\" ACL 2021"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-21T10:17:18.469084+00:00_

Web search results for query: "site:aclanthology.org Clark August Serrano "All That's Human Is Not Gold" ACL 2021"

Links: [{"title":"All That’s ‘Human’ Is Not Gold: Evaluating Human Evaluation of Generated Text - ACL Anthology","url":"https://aclanthology.org/2021.acl-long.565/"},{"title":"Language, Logic and Information | [Reminder] NLP RG Thu-11-Nov at 15:00: All That's Human Is Not Gold (hosted)","url":"https://uilotslli.sites.uu.nl/2021/11/10/reminder-nlp-rg-thu-11-nov-at-1500-all-thats-human-is-not-gold-hosted/"},{"title":"Language, Logic and Information | NLP RG Thu-11-Nov at 15:00: All That's Human Is Not Gold (hosted)","url":"https://uilotslli.sites.uu.nl/2021/11/08/nlp-rg-thu-11-nov-at-1500-all-thats-human-is-not-gold-hosted/"},{"title":"[2021] All That's 'Human' Is Not Gold: Evaluating Human Evaluation of Generated Text · Issue #139 · cfiken/paper-reading","url":"https://github.com/cfiken/paper-reading/issues/139"},{"title":"Aclanthology","url":"https://aclanthology.org/2025.acl-long.267.pdf"},{"title":"ACL-IJCNLP 2021","url":"https://2021.aclweb.org/program/accept/"},{"title":"[PDF] All That’s ‘Human’ Is Not Gold: Evaluating Human Evaluation of Generated Text | Semantic Scholar","url":"https://www.semanticscholar.org/paper/All-That%E2%80%99s-%E2%80%98Human%E2%80%99-Is-Not-Gold:-Evaluating-Human-of-Clark-August/a16ae67070de155789a871cb27ecbf9eaa98b379"},{"title":"Grounding Summarization Evaluation with Robust Human ...","url":"https://aclanthology.org/2023.acl-long.228.pdf"},{"title":"All That's 'Human' Is Not Gold: Evaluating Human Evaluation of Generated   Text","url":"https://arxiv.org/pdf/2107.00061"}]

I found the paper you were searching for! The paper "All That's 'Human' Is Not Gold: Evaluating Human Evaluation of Generated Text" examines the role untrained human evaluations play in NLG evaluation and provides recommendations to NLG researchers for improving human evaluations of text generated from state-of-the-art models.

The authors are Elizabet
…[truncated 501 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_citation_fill_20260521T101219",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-21T10:17:18.469224+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Koo Ryan Kim Kang \"Benchmarking Cognitive Biases\" LLM evaluators ACL 2024 full author list"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_citation_fill_20260521T101219",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Koo Ryan Kim Kang \"Benchmarking Cognitive Biases\" LLM evaluators ACL 2024 full author list"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-21T10:17:18.469380+00:00_

Web search results for query: "Koo Ryan Kim Kang "Benchmarking Cognitive Biases" LLM evaluators ACL 2024 full author list"

Links: [{"title":"Benchmarking Cognitive Biases in Large Language Models as Evaluators - Experts@Minnesota","url":"https://experts.umn.edu/en/publications/benchmarking-cognitive-biases-in-large-language-models-as-evaluat/"},{"title":"Benchmarking Cognitive Biases in Large Language Models as Evaluators - ACL Anthology","url":"https://aclanthology.org/2024.findings-acl.29/"},{"title":"Benchmarking Cognitive Biases in Large Language Models as Evaluators | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/benchmarking-cognitive-biases-large-language-models-as"},{"title":"Benchmarking Cognitive Biases in Large Language Models as Evaluators","url":"https://aclanthology.org/2024.findings-acl.29.xml"},{"title":"Benchmarking Cognitive Biases in Large Language Models as Evaluators","url":"https://arxiv.org/html/2309.17012v3"},{"title":"Accepted Findings Papers - ACL 2024","url":"https://2024.aclweb.org/program/finding_papers/"},{"title":"[2309.17012] Benchmarking Cognitive Biases in Large Language Models as Evaluators","url":"https://arxiv.org/abs/2309.17012"},{"title":"Benchmarking Cognitive Biases in Large Language ...","url":"https://aclanthology.org/2024.findings-acl.29.pdf"},{"title":"Benchmarking Cognitive Biases in Large Language Models as Evaluators","url":"https://arxiv.org/pdf/2309.17012"}]

Based on the search results, here is the full author list for the paper "Benchmarking Cognitive Biases in Large Language Models as Evaluators" presented at ACL 2024:

Ryan Koo, Minhwa Lee, Vipul Raheja, Jong Inn Park, Zae Myung Kim, and Dongyeop Kang.

The authors are affiliated with the University of Minnesota and Grammarly, with Vipul Raheja at Grammarly and the other five authors at the University of Minnesota.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_citation_fill_20260521T101219",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-21T10:17:18.469536+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Liusie Manakul Gales EACL 2024 \"LLM Comparative Assessment\" pages"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_citation_fill_20260521T101219",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Liusie Manakul Gales EACL 2024 \"LLM Comparative Assessment\" pages"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-21T10:17:18.469813+00:00_

Web search results for query: "Liusie Manakul Gales EACL 2024 "LLM Comparative Assessment" pages"

Links: [{"title":"LLM Comparative Assessment: Zero-shot NLG Evaluation through Pairwise Comparisons using Large Language Models - ACL Anthology","url":"https://aclanthology.org/2024.eacl-long.8/"},{"title":"Efficient LLM Comparative Assessment: a Product of Experts Framework for Pairwise Comparisons","url":"https://arxiv.org/html/2405.05894v2"},{"title":"Efficient LLM Comparative Assessment: a Product of","url":"https://scispace.com/pdf/efficient-llm-comparative-assessment-a-product-of-experts-3a4gdmipeh.pdf"},{"title":"Efficient LLM Comparative Assessment: A Product of Experts Framework for Pairwise Comparisons - ACL Anthology","url":"https://aclanthology.org/2024.emnlp-main.389/"},{"title":"LLM Comparative Assessment","url":"https://github.com/adianliusie/comparative-assessment"},{"title":"LLM Comparative Assessment: Zero-shot NLG Evaluation through Pairwise Comparisons using Large Language Models | Request PDF","url":"https://www.researchgate.net/publication/393020372_LLM_Comparative_Assessment_Zero-shot_NLG_Evaluation_through_Pairwise_Comparisons_using_Large_Language_Models"},{"title":"dblp: LLM Comparative Assessment: Zero-shot NLG Evaluation through Pairwise Comparisons using Large Language Models.","url":"https://dblp.dagstuhl.de/rec/conf/eacl/LiusieMG24.html"},{"title":"[2307.07889v3] LLM Comparative Assessment: Zero-shot NLG Evaluation through Pairwise Comparisons using Large Language Models","url":"https://arxiv.org/abs/2307.07889v3"},{"title":"[2307.07889] LLM Comparative Assessment: Zero-shot NLG Evaluation through Pairwise Comparisons using Large Language Models","url":"https://arxiv.org/abs/2307.07889"},{"title":"LLM Comparative Assessment: Zero-shot NLG Evaluation through Pairwise   Comparisons using Large Language Models","url":"https://arxiv.org/pdf/2307.07889"}]

Based on the search results, I found the paper you're looking for:

"LLM Comparative Asse
…[truncated 628 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_citation_fill_20260521T101219",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-21T10:17:18.470038+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Panickssery Bowman Feng \"LLM Evaluators Recognize Favor Own Generations\" arxiv 2404.13076 full authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_citation_fill_20260521T101219",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Panickssery Bowman Feng \"LLM Evaluators Recognize Favor Own Generations\" arxiv 2404.13076 full authors"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-21T10:17:18.470193+00:00_

Web search results for query: "Panickssery Bowman Feng "LLM Evaluators Recognize Favor Own Generations" arxiv 2404.13076 full authors"

Links: [{"title":"[2404.13076] LLM Evaluators Recognize and Favor Their Own Generations","url":"https://arxiv.org/abs/2404.13076"},{"title":"[2404.13076v1] LLM Evaluators Recognize and Favor Their Own Generations","url":"https://arxiv.org/abs/2404.13076v1"},{"title":"[PDF] LLM Evaluators Recognize and Favor Their Own Generations | Semantic Scholar","url":"https://www.semanticscholar.org/paper/LLM-Evaluators-Recognize-and-Favor-Their-Own-Panickssery-Bowman/5c7f465d162aade4a4c0eefb02fd7aadeebdaf58"},{"title":"LLMs are Biased Evaluators But Not Biased for Retrieval Augmented Generation","url":"https://arxiv.org/html/2410.20833v1"},{"title":"LLM Evaluators Recognize and Favor Their Own Generations","url":"https://proceedings.neurips.cc/paper_files/paper/2024/hash/7f1f0218e45f5414c79c0679633e47bc-Abstract-Conference.html"},{"title":"Preference Leakage: A Contamination Problem in LLM-as- ...","url":"https://arxiv.org/pdf/2502.01534"},{"title":"LLM Evaluators Recognize and Favor Their Own Generations","url":"https://arxiv.org/pdf/2404.13076"},{"title":"LLM evaluators recognize and favor their own generations | Proceedings of the 38th International Conference on Neural Information Processing Systems","url":"https://dl.acm.org/doi/10.5555/3737916.3740113"},{"title":"LLM Evaluators Recognize and Favor Their Own Generations | alphaXiv","url":"https://www.alphaxiv.org/abs/2404.13076"}]

The full authors of the paper arxiv 2404.13076 "LLM Evaluators Recognize and Favor Their Own Generations" are Arjun Panickssery, Samuel R. Bowman, and Shi Feng.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_citation_fill_20260521T101219",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-21T10:17:18.470435+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Wu Aji \"Style Over Substance: Evaluation Biases\" 2307.03025 conference venue EMNLP"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_citation_fill_20260521T101219",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Wu Aji \"Style Over Substance: Evaluation Biases\" 2307.03025 conference venue EMNLP"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-21T10:17:18.470612+00:00_

Web search results for query: "Wu Aji "Style Over Substance: Evaluation Biases" 2307.03025 conference venue EMNLP"

Links: [{"title":"[2307.03025] Style Over Substance: Evaluation Biases for Large Language Models","url":"https://arxiv.org/abs/2307.03025"},{"title":"Large Language Models are Inconsistent and Biased Evaluators","url":"https://arxiv.org/html/2405.01724v1"},{"title":"Humans or LLMs as the Judge? A Study on Judgement Bias","url":"https://arxiv.org/html/2402.10669v3"},{"title":"Finding Blind Spots in Evaluator LLMs with Interpretable ...","url":"https://aclanthology.org/2024.emnlp-main.911.pdf"},{"title":"Style Over Substance: Evaluation Biases for Large Language Models","url":"https://www.researchgate.net/publication/372163436_Style_Over_Substance_Evaluation_Biases_for_Large_Language_Models"},{"title":"[PDF] Style Over Substance: Evaluation Biases for Large Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Style-Over-Substance:-Evaluation-Biases-for-Large-Wu-Aji/7ace46ab8e71c4304682ab126b1212deb54b9b03"},{"title":"Humans or LLMs as the Judge? A Study on Judgement Bias","url":"https://aclanthology.org/2024.emnlp-main.474.pdf"},{"title":"arXiv Comp. Linguistics📚: \"📝 Style Over Substance: Evaluation Biases for Lar…\" - creative.ai (fediverse)","url":"https://creative.ai/@arxiv_cl/110676555372271258"},{"title":"Style Over Substance: Evaluation Biases for Large Language Models | OpenReview","url":"https://openreview.net/forum?id=UnstiBOfnv"},{"title":"Style Over Substance: Evaluation Biases for Large Language Models","url":"https://arxiv.org/pdf/2307.03025"}]

Based on the search results, I found information about the paper "Style Over Substance: Evaluation Biases for Large Language Models" with arXiv ID 2307.03025 by Wu and Aji.

The paper was authored by Minghao Wu and Alham Fikri Aji and submitted to arXiv on July 6, 2023.

However, the search results show that this paper appears to be an arXiv preprint rather than a confere
…[truncated 825 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_citation_fill_20260521T101219",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-21T10:17:18.470785+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "site:aclanthology.org \"Style Over Substance\" Wu Aji evaluation biases"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_citation_fill_20260521T101219",
  "tool": "WebSearch",
  "tool_args": {
    "query": "site:aclanthology.org \"Style Over Substance\" Wu Aji evaluation biases"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-21T10:17:18.470923+00:00_

Web search results for query: "site:aclanthology.org "Style Over Substance" Wu Aji evaluation biases"

Links: [{"title":"Style Over Substance: Evaluation Biases for Large Language Models - ACL Anthology","url":"https://aclanthology.org/2025.coling-main.21/"},{"title":"Evaluation Biases for Large Language Models","url":"https://aclanthology.org/2025.coling-main.21.pdf"},{"title":"Style Over Substance: Evaluation Biases for Large Language Models","url":"https://arxiv.org/pdf/2307.03025"},{"title":"Everyone prefers human writers, including AI","url":"https://arxiv.org/pdf/2510.08831"},{"title":"Style Outweighs Substance: Failure Modes of LLM Judges in Alignment   Benchmarking","url":"https://arxiv.org/pdf/2409.15268"}]

I found the paper! Here are the search results for the ACL Anthology paper by Wu and Aji:

"Style Over Substance: Evaluation Biases for Large Language Models" is a paper by Minghao Wu and Alham Fikri Aji, published in the Proceedings of the 31st International Conference on Computational Linguistics in 2025.

**Key Findings:**

The paper reveals a concerning bias in the evaluation process, as answers with factual errors are rated more favorably than answers that are too short or contained grammatical errors.

**Proposed Solution:**

To address this issue, the authors propose independently evaluating machine-generated text across multiple dimensions, rather than merging all the evaluation aspects into a single score, instantiating this idea with the Elo rating system to create the Multi-Elo Rating System (MERS).

**Results:**

Empirical results reveal that this proposed approach significantly enhances the quality of LLM-based evaluations, particularly in terms of factual accuracy, though there is no significant improvement in crowd-sourced evaluations.

The paper is available at: https://aclanthology.org/2025.coling-main.21/


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_citation_fill_20260521T101219",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-21T10:17:18.471116+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/references.bib",
  "old_string": "@article{ye2024justice,\n  title={Justice or Prejudice? Quantifying Biases in {LLM}-as-a-Judge},\n  author={Ye, Jiayi and Wang, Yanbo and Huang, Yue and Chen, Dongping and Zhang, Qihui and Moniz, Nuno and Gao, Tian and Geyer, Werner and Huang, Chao and Chen, Pin-Yu},\n  journal={arXiv preprint arXiv:2410.02736},\n  year={2024},\n  url={https://arxiv.org/abs/2410.02736}\n}",
  "new_string": "@article{ye2024justice,\n  title={Justice or Prejudice? Quantifying Biases in {LLM}-as-a-Judge},\n  author={Ye, Jiayi and Wang, Yanbo and Huang, Yue and Chen, Dongping and Zhang, Qihui and Moniz, Nuno and Gao, Tian and Geyer, Werner and Huang, Chao and Chen, Pin-Yu},\n  journal={arXiv preprint arXiv:2410.02736},\n  year={2024},\n  url={https://arxiv.org/abs/2410.02736}\n}\n\n@article{feder2021causalm,\n  title={{CausaLM}: Causal Model Explanation Through Counterfactual Language Models},\n  author={Feder, Amir and Oved, Nadav and Shalit, Uri and Reichart, Roi},\n  journal={Computational Linguistics},\n  volume={47},\n  number={2},\n  pages={333--386},\n  year={2021},\n  url={https://aclanthology.org/2021.cl-2.13/}\n}\n\n@inproceedings{wu2021polyjuice,\n  title={Polyjuice: Generating Counterfactuals for Explaining, Evaluating, and Improving Models},\n  author={Wu, Tongshuang and Ribeiro, Marco Tulio and Heer, Jeffrey and Weld, Daniel},\n  booktitle={Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processing (Volume 1: Long Papers)},\n  year={2021},\n  url={https://aclanthology.org/2021.acl-long.523/}\n}\n\n@inproceedings{clark2021human,\n  title={All That's `Human' Is Not Gold: Evaluating Human Evaluation of Generated Text},\n  author={Clark, Elizabeth and August, Tal and Serrano, Sofia and Haduong, Nikita and Gururangan, Suchin and Smith, Noah A.},\n  booktitle={Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processing (Volume 1: Long Papers)},\n  pages={7282--7296},\n  year={2021},\n  url={https://aclanthology.org/2021.acl-long.565/}\n}\n\n@inproceedings{amidei2019likert,\n  title={The Use of Rating and {Likert} Scales in Natural Language Generation Human Evaluation Tasks: A Review and Some Recommendations},\n  author={Amidei, Jacopo and Piwek, Paul and Willis, Alistair},\n  booktitle={Proceedings of the 12th International Conference on Natural Language Generation (INLG)},\n  year={2019},\n  url={https://aclanthology.org/W19-8648/}\n}\n\n@inproceedings{boubdir2023elo,\n  title={Elo Uncovered: Robustness and Best Practices in Language Model Evaluation},\n  author={Boubdir, Meriem and Kim, Edward and Ermis, Beyza and Hooker, Sara and Fadaee, Marzieh},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2024},\n  url={https://arxiv.org/abs/2311.17295}\n}\n\n@inproceedings{wu2023style,\n  title={Style Over Substance: Evaluation Biases for Large Language Models},\n  author={Wu, Minghao and Aji, Alham Fikri},\n  booktitle={Proceedings of the 31st International Conference on Computational Linguistics (COLING)},\n  year={2025},\n  url={https://aclanthology.org/2025.coling-main.21/}\n}\n\n@inproceedings{liusie2024comparative,\n  title={{LLM} Comparative Assessment: Zero-shot {NLG} Evaluation through Pairwise Comparisons using Large Language Models},\n  author={Liusie, Adian and Manakul, Potsawee and Gales, Mark},\n  booktitle={Proceedings of the 18th Conference of the European Chapter of the Association for Computational Linguistics (Volume 1: Long Papers)},\n  pages={139--151},\n  year={2024},\n  url={https://aclanthology.org/2024.eacl-long.8/}\n}\n\n@article{feder2022causal,\n  title={Causal Inference in Natural Language Processing: Estimation, Prediction, Interpretation and Beyond},\n  author={Feder, Amir and Keith, Katherine A. and Manzoor, Emaad and Pryzant, Reid and Sridhar, Dhanya and Wood-Doughty, Zach and Eisenstein, Jacob and Grimmer, Justin and Reichart, Roi and Roberts, Margaret E. and Stewart, Brandon M. and Veitch, Victor and Yang, Diyi},\n  journal={Transactions of the Association for Computational Linguistics},\n  volume={10},\n  pages={1138--1158},\n  year={2022},\n  url={https://aclanthology.org/2022.tacl-1.66/}\n}\n\n@inproceedings{koo2024cobbler,\n  title={Benchmarking Cognitive Biases in Large Language Models as Evaluators},\n  author={Koo, Ryan and Lee, Minhwa and Raheja, Vipul and Park, Jong Inn and Kim, Zae Myung and Kang, Dongyeop},\n  booktitle={Findings of the Association for Computational Linguistics: ACL 2024},\n  year={2024},\n  url={https://aclanthology.org/2024.findings-acl.29/}\n}\n\n@inproceedings{panickssery2024selfpreference,\n  title={{LLM} Evaluators Recognize and Favor Their Own Generations},\n  author={Panickssery, Arjun and Bowman, Samuel R. and Feng, Shi},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2024},\n  url={https://arxiv.org/abs/2404.13076}\n}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_citation_fill_20260521T101219",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/references.bib",
    "old_string": "@article{ye2024justice,\n  title={Justice or Prejudice? Quantifying Biases in {LLM}-as-a-Judge},\n  author={Ye, Jiayi and Wang, Yanbo and Huang, Yue and Chen, Dongping and Zhang, Qihui and Moniz, Nuno and Gao, Tian and Geyer, Werner and Huang, Chao and Chen, Pin-Yu},\n  journal={arXiv preprint arXiv:2410.02736},\n  year={2024},\n  url={https://arxiv.org/abs/2410.02736}\n}",
    "new_string": "@article{ye2024justice,\n  title={Justice or Prejudice? Quantifying Biases in {LLM}-as-a-Judge},\n  author={Ye, Jiayi and Wang, Yanbo and Huang, Yue and Chen, Dongping and Zhang, Qihui and Moniz, Nuno and Gao, Tian and Geyer, Werner and Huang, Chao and Chen, Pin-Yu},\n  journal={arXiv preprint arXiv:2410.02736},\n  year={2024},\n  url={https://arxiv.org/abs/2410.02736}\n}\n\n@article{feder2021causalm,\n  title={{CausaLM}: Causal Model Explanation Through Counterfactual Language Models},\n  author={Feder, Amir and Oved, Nadav and Shalit, Uri and Reichart, Roi},\n  journal={Computational Linguistics},\n  volume={47},\n  number={2},\n  pages={333--386},\n  year={2021},\n  url={https://aclanthology.org/2021.cl-2.13/}\n}\n\n@inproceedings{wu2021polyjuice,\n  title={Polyjuice: Generating Counterfactuals for Explaining, Evaluating, and Improving Models},\n  author={Wu, Tongshuang and Ribeiro, Marco Tulio and Heer, Jeffrey and Weld, Daniel},\n  booktitle={Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processing (Volume 1: Long Papers)},\n  year={2021},\n  url={https://aclanthology.org/2021.acl-long.523/}\n}\n\n@inproceedings{clark2021human,\n  title={All That's `Human' Is Not Gold: Evaluating Human Evaluation of Generated Text},\n  author={Clark, Elizabeth and August, Tal and Serrano, Sofia and Haduong, Nikita and Gururangan, Suchin and Smith, Noah A.},\n  booktitle={Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processing (Volume 1: Long Papers)},\n  pages={7282--7296},\n  year={2021},\n  url={https://aclanthology.org/2021.acl-long.565/}\n}\n\n@inproceedings{amidei2019likert,\n  title={The Use of Rating and {Likert} Scales in Natural Language Generation Human Evaluation Tasks: A Review and Some Recommendations},\n  author={Amidei, Jacopo and Piwek, Paul and Willis, Alistair},\n  booktitle={Proceedings of the 12th International Conference on Natural Language Generation (INLG)},\n  year={2019},\n  url={https://aclanthology.org/W19-8648/}\n}\n\n@inproceedings{boubdir2023elo,\n  title={Elo Uncovered: Robustness and Best Practices in Language Model Evaluation},\n  author={Boubdir, Meriem and Kim, Edward and Ermis, Beyza and Hooker, Sara and Fadaee, Marzieh},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2024},\n  url={https://arxiv.org/abs/2311.17295}\n}\n\n@inproceedings{wu2023style,\n  title={Style Over Substance: Evaluation Biases for Large Language Models},\n  author={Wu, Minghao and Aji, Alham Fikri},\n  booktitle={Proceedings of the 31st International Conference on Computational Linguistics (COLING)},\n  year={2025},\n  url={https://aclanthology.org/2025.coling-main.21/}\n}\n\n@inproceedings{liusie2024comparative,\n  title={{LLM} Comparative Assessment: Zero-shot {NLG} Evaluation through Pairwise Comparisons using Large Language Models},\n  author={Liusie, Adian and Manakul, Potsawee and Gales, Mark},\n  booktitle={Proceedings of the 18th Conference of the European Chapter of the Association for Computational Linguistics (Volume 1: Long Papers)},\n  pages={139--151},\n  year={2024},\n  url={https://aclanthology.org/2024.eacl-long.8/}\n}\n\n@article{feder2022causal,\n  title={Causal Inference in Natural Language Processing: Estimation, Prediction, Interpretation and Beyond},\n  author={Feder, Amir and Keith, Katherine A. and Manzoor, Emaad and Pryzant, Reid and Sridhar, Dhanya and Wood-Doughty, Zach and Eisenstein, Jacob and Grimmer, Justin and Reichart, Roi and Roberts, Margaret E. and Stewart, Brandon M. and Veitch, Victor and Yang, Diyi},\n  journal={Transactions of the Association for Computational Linguistics},\n  volume={10},\n  pages={1138--1158},\n  year={2022},\n  url={https://aclanthology.org/2022.tacl-1.66/}\n}\n\n@inproceedings{koo2024cobbler,\n  title={Benchmarking Cognitive Biases in Large Language Models as Evaluators},\n  author={Koo, Ryan and Lee, Minhwa and Raheja, Vipul and Park, Jong Inn and Kim, Zae Myung and Kang, Dongyeop},\n  booktitle={Findings of the Association for Computational Linguistics: ACL 2024},\n  year={2024},\n  url={https://aclanthology.org/2024.findings-acl.29/}\n}\n\n@inproceedings{panickssery2024selfpreference,\n  title={{LLM} Evaluators Recognize and Favor Their Own Generations},\n  author={Panickssery, Arjun and Bowman, Samuel R. and Feng, Shi},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2024},\n  url={https://arxiv.org/abs/2404.13076}\n}"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-21T10:17:18.471363+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/references.bib has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_citation_fill_20260521T101219",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 49 · 2026-05-21T10:17:18.471551+00:00_

Appended 10 new BibTeX entries. Total references: 37 (27 existing + 10 new).

**Director-specified (6):**
| Key | Paper | Venue |
|-----|-------|-------|
| `feder2021causalm` | CausaLM: Causal Model Explanation Through Counterfactual Language Models | Computational Linguistics 2021 |
| `wu2021polyjuice` | Polyjuice: Generating Counterfactuals for Explaining, Evaluating, and Improving Models | ACL 2021 |
| `clark2021human` | All That's 'Human' Is Not Gold: Evaluating Human Evaluation of Generated Text | ACL 2021 |
| `amidei2019likert` | The Use of Rating and Likert Scales in NLG Human Evaluation Tasks | INLG 2019 |
| `boubdir2023elo` | Elo Uncovered: Robustness and Best Practices in Language Model Evaluation | NeurIPS 2024 |
| `wu2023style` | Style Over Substance: Evaluation Biases for Large Language Models | COLING 2025 |

**Additional (4):**
| Key | Paper | Venue |
|-----|-------|-------|
| `liusie2024comparative` | LLM Comparative Assessment: Zero-shot NLG Evaluation through Pairwise Comparisons | EACL 2024 |
| `feder2022causal` | Causal Inference in NLP: Estimation, Prediction, Interpretation and Beyond | TACL 2022 |
| `koo2024cobbler` | Benchmarking Cognitive Biases in Large Language Models as Evaluators | Findings of ACL 2024 |
| `panickssery2024selfpreference` | LLM Evaluators Recognize and Favor Their Own Generations | NeurIPS 2024 |

All entries verified via web search — no fabricated details. Existing entries left untouched.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_research_citation_fill_20260521T101219"
}
```

</details>

---
