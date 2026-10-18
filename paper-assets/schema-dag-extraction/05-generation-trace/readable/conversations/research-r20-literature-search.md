# research r20 literature search

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 31
- **Recorded user turns:** 0
- **Tool calls:** 15
- **Original source:** `logs/chats/worker_research_r20_literature_search_20260519T045626.jsonl`
- **Structured JSON:** [`ce4b33433ad525993838.json`](../../sessions/ce/ce4b33433ad525993838.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

31 recorded events

### Tool call

_source line 1 · 2026-05-19T04:58:45.580663+00:00_

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
  "session": "worker_research_r20_literature_search_20260519T045626",
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

_source line 2 · 2026-05-19T04:58:45.581044+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_r20_literature_search_20260519T045626",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-19T04:58:45.581268+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Dubey et al. 2018 \"Pairwise Confusion for Fine-Grained Visual Classification\" ECCV bibtex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_r20_literature_search_20260519T045626",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Dubey et al. 2018 \"Pairwise Confusion for Fine-Grained Visual Classification\" ECCV bibtex"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-19T04:58:45.581415+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Collier et al. 2021 \"Exploiting Class Similarity for Machine Learning with Confidence Labels\" bibtex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_r20_literature_search_20260519T045626",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Collier et al. 2021 \"Exploiting Class Similarity for Machine Learning with Confidence Labels\" bibtex"
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-19T04:58:45.581553+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "constrained decoding calibration LLM structured output 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_r20_literature_search_20260519T045626",
  "tool": "WebSearch",
  "tool_args": {
    "query": "constrained decoding calibration LLM structured output 2024 2025"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-19T04:58:45.581720+00:00_

Web search results for query: "Dubey et al. 2018 "Pairwise Confusion for Fine-Grained Visual Classification" ECCV bibtex"

Links: [{"title":"Pairwise Confusion for Fine-Grained Visual Classification | SpringerLink","url":"https://link.springer.com/chapter/10.1007/978-3-030-01258-8_5"},{"title":"GitHub - abhimanyudubey/confusion: Code for the ECCV 2018 paper \"Pairwise Confusion for Fine-Grained Visual Classification\" · GitHub","url":"https://github.com/abhimanyudubey/confusion"},{"title":"dblp: Pairwise Confusion for Fine-Grained Visual Classification.","url":"https://dblp.org/rec/conf/eccv/DubeyGGRFN18.html"},{"title":"Fine-grained visual classification with multi-scale features based on self-supervised attention filtering mechanism | Applied Intelligence","url":"https://link.springer.com/article/10.1007/s10489-022-03232-w"},{"title":"[1705.08016] Pairwise Confusion for Fine-Grained Visual Classification","url":"https://arxiv.org/abs/1705.08016"},{"title":"Pairwise Confusion for Fine-Grained Visual Classification","url":"https://openaccess.thecvf.com/content_ECCV_2018/papers/Abhimanyu_Dubey_Improving_Fine-Grained_Visual_ECCV_2018_paper.pdf"},{"title":"Awesome Fine-Grained Image Analysis – Papers, Codes and Datasets","url":"http://www.weixiushen.com/project/Awesome_FGIA/Awesome_FGIA.html"},{"title":"Learning Attentive Pairwise Interaction for Fine-Grained ...","url":"https://cdn.aaai.org/ojs/7016/7016-13-10245-1-10-20200525.pdf"}]

Based on the search results, I found the BibTeX entry for the Dubey et al. 2018 paper. The official BibTeX citation is:

```
@InProceedings{Dubey_2018_ECCV,
  author = {Dubey, Abhimanyu and Gupta, Otkrist and Guo, Pei and Raskar, Ramesh and Farrell, Ryan and Naik, Nikhil},
  title = {Pairwise Confusion for Fine-Grained Visual Classification},
  booktitle = {The European Conference on Computer Vision (ECCV)},
  month = {September},
  year = {2018}
}
```

This entry was provided by the authors in their official GitHub repository for the co
…[truncated 121 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_r20_literature_search_20260519T045626",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-19T04:58:45.581952+00:00_

Web search results for query: "Collier et al. 2021 "Exploiting Class Similarity for Machine Learning with Confidence Labels" bibtex"

Links: [{"title":"Exploiting Class Similarity for Machine Learning with Confidence Labels   and Projective Loss Functions","url":"https://arxiv.org/pdf/2103.13607"},{"title":"Exploiting Class Similarity for Machine Learning with Confidence Labels and Projective Loss Functions | DeepAI","url":"https://deepai.org/publication/exploiting-class-similarity-for-machine-learning-with-confidence-labels-and-projective-loss-functions"},{"title":"(PDF) Exploiting Class Similarity for Machine Learning with Confidence Labels and Projective Loss Functions","url":"https://www.researchgate.net/publication/350398245_Exploiting_Class_Similarity_for_Machine_Learning_with_Confidence_Labels_and_Projective_Loss_Functions"},{"title":"[2103.13607] Exploiting Class Similarity for Machine Learning with Confidence Labels and Projective Loss Functions","url":"https://arxiv.org/abs/2103.13607"},{"title":"[PDF] Exploiting Class Similarity for Machine Learning with Confidence Labels and Projective Loss Functions | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Exploiting-Class-Similarity-for-Machine-Learning-Gare-Galeotti/1c808e1aa382a1e4a59763a15e733457d1bd459b"}]

Based on the search results, I found the paper you're looking for. However, I should note that the paper is by Gautam Rajendrakumar Gare and John Michael Galeotti, not "Collier et al." as mentioned in your query.

Here is the BibTeX entry from Semantic Scholar:

```
@article{Gare2021ExploitingCS, 
  title={Exploiting Class Similarity for Machine Learning with Confidence Labels and Projective Loss Functions}, 
  author={Gautam Rajendrakumar Gare and John Michael Galeotti}, 
  journal={ArXiv}, 
  year={2021}, 
  volume={abs/2103.13607} 
}
```


The paper was published on arXiv in March 2021. If you need additional citation formats or more specific publication details, you may want to check 
…[truncated 163 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_r20_literature_search_20260519T045626",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-19T04:58:45.582182+00:00_

Web search results for query: "constrained decoding calibration LLM structured output 2024 2025"

Links: [{"title":"How Structured Outputs and Constrained Decoding Work | Let's Data Science","url":"https://letsdatascience.com/blog/structured-outputs-making-llms-return-reliable-json"},{"title":"Beyond Free-Form Text: How Constrained Decoding is Reshaping Structured Generation in LLMs | by Brijesh Nambiar | Medium","url":"https://medium.com/@brijeshrn/beyond-free-form-text-how-constrained-decoding-is-reshaping-structured-generation-in-llms-5f7a38bef259"},{"title":"GitHub - Saibo-creator/Awesome-LLM-Constrained-Decoding: A curated list of papers related to constrained decoding of LLM, along with their relevant code and resources. · GitHub","url":"https://github.com/Saibo-creator/Awesome-LLM-Constrained-Decoding"},{"title":"Constrained Decoding: Grammar-Guided Generation for Structured LLM Output - Interactive | Michael Brenndoerfer | Michael Brenndoerfer","url":"https://mbrenndoerfer.com/writing/constrained-decoding-structured-llm-output"},{"title":"Draft-Conditioned Constrained Decoding for Structured Generation in LLMs","url":"https://arxiv.org/pdf/2603.03305"},{"title":"Generating Structured Outputs from Language Models: Benchmark and Studies","url":"https://arxiv.org/html/2501.10868v1"},{"title":"Logically Constrained Decoding - ACL Anthology","url":"https://aclanthology.org/2025.mathnlp-main.11/"},{"title":"Grammar-Aligned Decoding | OpenReview","url":"https://openreview.net/forum?id=5G7ve8E1Lu"}]

I've completed the web search for your query. Here are the key findings about constrained decoding, calibration, and structured output for LLMs in 2024-2025:

## Recent Releases and Industry Adoption

OpenAI released Structured Outputs in August 2024 with response_format: { type: "json_schema" }, Google Gemini added response_schema at Google I/O in May 2024, and Anthropic followed in November 2025 with constrained decoding for Claude.

## Key Technical Developments

Con
…[truncated 1304 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_r20_literature_search_20260519T045626",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-19T04:58:45.582379+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Collier 2021 class similarity machine learning confidence labels"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_r20_literature_search_20260519T045626",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Collier 2021 class similarity machine learning confidence labels"
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-19T04:58:45.582519+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Grammar-Aligned Decoding\" 2024 bibtex constrained decoding calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_r20_literature_search_20260519T045626",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Grammar-Aligned Decoding\" 2024 bibtex constrained decoding calibration"
  }
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-19T04:58:45.582643+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Dubey 2018 pairwise confusion ECCV pages proceedings LNCS"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_r20_literature_search_20260519T045626",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Dubey 2018 pairwise confusion ECCV pages proceedings LNCS"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-19T04:58:45.582800+00:00_

Web search results for query: ""Grammar-Aligned Decoding" 2024 bibtex constrained decoding calibration"

Links: [{"title":"NeurIPS Poster Grammar-Aligned Decoding","url":"https://neurips.cc/virtual/2024/poster/96599"},{"title":"Grammar-Aligned Decoding | OpenReview","url":"https://openreview.net/forum?id=5G7ve8E1Lu"},{"title":"[2405.21047] Grammar-Aligned Decoding","url":"https://arxiv.org/abs/2405.21047"},{"title":"Grammar-Aligned Decoding","url":"https://papers.nips.cc/paper_files/paper/2024/hash/2bdc2267c3d7d01523e2e17ac0a754f3-Abstract-Conference.html"},{"title":"Grammar-Aligned Decoding","url":"https://proceedings.neurips.cc/paper_files/paper/2024/hash/2bdc2267c3d7d01523e2e17ac0a754f3-Abstract-Conference.html"},{"title":"Beyond Free-Form Text: How Constrained Decoding is Reshaping Structured Generation in LLMs | by Brijesh Nambiar | Medium","url":"https://medium.com/@brijeshrn/beyond-free-form-text-how-constrained-decoding-is-reshaping-structured-generation-in-llms-5f7a38bef259"},{"title":"Grammar-aligned decoding | Proceedings of the 38th International Conference on Neural Information Processing Systems","url":"https://dl.acm.org/doi/10.5555/3737916.3738690"},{"title":"Grammar-Aligned Decoding Kanghee Park1∗ Jiayu Wang1∗ Taylor Berg-Kirkpatrick2","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/2bdc2267c3d7d01523e2e17ac0a754f3-Paper-Conference.pdf"},{"title":"Grammar-Aligned Decoding","url":"https://arxiv.org/html/2405.21047v3"}]

Based on the web search results, here's what I found about "Grammar-Aligned Decoding":

## Overview

Grammar-Aligned Decoding (GAD) addresses a key problem: while constrained decoding approaches restrict LLM outputs to match a given grammar, these techniques can distort the LLM's distribution, leading to grammatical outputs with likelihoods that are not proportional to the original LLM's distribution.

## The ASAp Algorithm

The paper proposes adaptive sampling with approximate expected futures (ASAp), a decoding alg
…[truncated 953 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_r20_literature_search_20260519T045626",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-19T04:58:45.583001+00:00_

Web search results for query: "Collier 2021 class similarity machine learning confidence labels"

Links: [{"title":"Exploiting Class Similarity for Machine Learning with Confidence Labels   and Projective Loss Functions","url":"https://arxiv.org/pdf/2103.13607"},{"title":"[2103.13607] Exploiting Class Similarity for Machine Learning with Confidence Labels and Projective Loss Functions","url":"https://arxiv.org/abs/2103.13607"},{"title":"Exploiting Class Similarity for Machine Learning with Confidence Labels and Projective Loss Functions | DeepAI","url":"https://deepai.org/publication/exploiting-class-similarity-for-machine-learning-with-confidence-labels-and-projective-loss-functions"},{"title":"[PDF] Exploiting Class Similarity for Machine Learning with Confidence Labels and Projective Loss Functions | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Exploiting-Class-Similarity-for-Machine-Learning-Gare-Galeotti/1c808e1aa382a1e4a59763a15e733457d1bd459b"},{"title":"(PDF) Exploiting Class Similarity for Machine Learning with Confidence Labels and Projective Loss Functions","url":"https://www.researchgate.net/publication/350398245_Exploiting_Class_Similarity_for_Machine_Learning_with_Confidence_Labels_and_Projective_Loss_Functions"},{"title":"ICML 2021 Learning from Similarity-Confidence Data Spotlight","url":"https://icml.cc/virtual/2021/spotlight/9870"},{"title":"Learning from Similarity-Confidence and Confidence-Difference","url":"https://arxiv.org/html/2508.05108"}]

Based on the search results, I found the paper you're looking for. The document is titled "Exploiting Class Similarity for Machine Learning with Confidence Labels and Projective Loss Functions" by Gautam Rajendrakumar Gare and John Michael Galeotti from Carnegie Mellon University, published in 2021.

The key contribution of this paper is the introduction of confidence labels, which are probabilistic labels denoting the likelihood of similarity, or confusability, between classes. Class si
…[truncated 724 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_r20_literature_search_20260519T045626",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-19T04:58:45.583192+00:00_

Web search results for query: "Dubey 2018 pairwise confusion ECCV pages proceedings LNCS"

Links: [{"title":"GitHub - abhimanyudubey/confusion: Code for the ECCV 2018 paper \"Pairwise Confusion for Fine-Grained Visual Classification\" · GitHub","url":"https://github.com/abhimanyudubey/confusion"},{"title":"Pairwise Confusion for Fine-Grained Visual Classiﬁcation","url":"https://openaccess.thecvf.com/content_ECCV_2018/papers/Abhimanyu_Dubey_Improving_Fine-Grained_Visual_ECCV_2018_paper.pdf"},{"title":"Computer Vision – ECCV 2018 Workshops: Munich, Germany, September 8-14, 2018, Proceedings, Part II [1st ed.] 978-3-030-11011-6, 978-3-030-11012-3 - DOKUMEN.PUB","url":"https://dokumen.pub/computer-vision-eccv-2018-workshops-munich-germany-september-8-14-2018-proceedings-part-ii-1st-ed-978-3-030-11011-6-978-3-030-11012-3.html"},{"title":"Computer Vision – ECCV 2018 Workshops: Munich, Germany, September 8-14, 2018, Proceedings, Part III [1st ed.] 978-3-030-11014-7, 978-3-030-11015-4 - DOKUMEN.PUB","url":"https://dokumen.pub/computer-vision-eccv-2018-workshops-munich-germany-september-8-14-2018-proceedings-part-iii-1st-ed-978-3-030-11014-7-978-3-030-11015-4.html"},{"title":"Computer Vision – ECCV 2018 15th European Conference, Munich, Germany, September 8-14, 2018, Proceedings, Part VIII: 15th European Conference, Munich, Germany, September 8-14, 2018, Proceedings, Part VIII","url":"https://www.researchgate.net/publication/345574969_Computer_Vision_-_ECCV_2018_15th_European_Conference_Munich_Germany_September_8-14_2018_Proceedings_Part_VIII_15th_European_Conference_Munich_Germany_September_8-14_2018_Proceedings_Part_VIII"},{"title":"Computer Vision – ECCV 2018 15th European Conference, Munich, Germany, September 8-14, 2018, Proceedings, Part XV: 15th European Conference, Munich, Germany, September 8-14, 2018, Proceedings, Part XV","url":"https://www.researchgate.net/publication/345602389_Computer_Vision_-_ECCV_2018_15th_European_Conference_Munich_Germany_September_8-14_201
…[truncated 1559 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_r20_literature_search_20260519T045626",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-19T04:58:45.583377+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Collier 2021 class similarity classification NeurIPS ICML"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_r20_literature_search_20260519T045626",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Collier 2021 class similarity classification NeurIPS ICML"
  }
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-19T04:58:45.583504+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "site:dblp.org \"Pairwise Confusion for Fine-Grained Visual Classification\" Dubey"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_r20_literature_search_20260519T045626",
  "tool": "WebSearch",
  "tool_args": {
    "query": "site:dblp.org \"Pairwise Confusion for Fine-Grained Visual Classification\" Dubey"
  }
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-19T04:58:45.583624+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Grammar-Aligned Decoding\" Park Wang Berg-Kirkpatrick NeurIPS 2024 bibtex authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_r20_literature_search_20260519T045626",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Grammar-Aligned Decoding\" Park Wang Berg-Kirkpatrick NeurIPS 2024 bibtex authors"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-19T04:58:45.583767+00:00_

Web search results for query: "Collier 2021 class similarity classification NeurIPS ICML"

Links: [{"title":"Visualizing Classification Structure of Large-Scale Classifiers","url":"https://arxiv.org/pdf/2007.06068"},{"title":"Leveraging Class Similarity to Improve Deep Neural Network Robustness","url":"https://arxiv.org/pdf/1812.09744"},{"title":"Exploiting Class Similarity for Machine Learning with Confidence Labels   and Projective Loss Functions","url":"https://arxiv.org/pdf/2103.13607"},{"title":"Weakly-Supervised Contrastive Learning for Imprecise Class Labels","url":"https://palm.seu.edu.cn/zhangml/files/ICML'25c.pdf"},{"title":"A Similarity-based Framework for Classification Task","url":"https://arxiv.org/pdf/2203.02669"},{"title":"ClassSim: Similarity between Classes Defined by Misclassification Ratios   of Trained Classifiers","url":"https://arxiv.org/pdf/1802.01267"},{"title":"Yu Gong, Greg Mori, Frederick Tung RankSim: Ranking Similarity Regularization","url":"https://icml.cc/media/icml-2022/Slides/16496.pdf"},{"title":"Label-similarity Curriculum Learning","url":"https://arxiv.org/pdf/1911.06902"}]

Based on the search results, I found several papers related to class similarity and classification, but I did not find a specific 2021 paper by an author named Collier that was published at NeurIPS or ICML.

The search results include various papers on class similarity in classification, such as:
- Papers on visualizing classification structure and leveraging class similarity for improved neural network robustness
- Papers on similarity-based frameworks for classification tasks
- Papers on label-similarity curriculum learning

However, none of these appear to be specifically authored by Collier in 2021 at NeurIPS or ICML based on the search results returned. The search may not have captured the specific paper you're looking for. 

Could you provide additional context about the paper, such as:
- The first name of the author (Collier)?
- The full title of the p
…[truncated 265 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_r20_literature_search_20260519T045626",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-19T04:58:45.583986+00:00_

Web search results for query: "site:dblp.org "Pairwise Confusion for Fine-Grained Visual Classification" Dubey"

Links: [{"title":"dblp: Pairwise Confusion for Fine-Grained Visual Classification.","url":"https://dblp.org/rec/conf/eccv/DubeyGGRFN18.html"},{"title":"Pairwise Confusion for Fine-Grained Visual Classification","url":"https://arxiv.org/pdf/1705.08016"},{"title":"Learning Attentive Pairwise Interaction for Fine-Grained Classification","url":"https://arxiv.org/pdf/2002.10191"},{"title":"Pairwise Matching of Intermediate Representations for Fine-grained Explainability","url":"https://arxiv.org/pdf/2503.22881"},{"title":"Low-Rank Pairwise Alignment Bilinear Network For Few-Shot Fine-Grained   Image Classification","url":"https://arxiv.org/pdf/1908.01313"}]

The web search found the paper you're looking for! Here are the results:

"Pairwise Confusion for Fine-Grained Visual Classification" is authored by Abhimanyu Dubey, Otkrist Gupta, Pei Guo, Ramesh Raskar, Ryan Farrell, and Nikhil Naik, and was published at ECCV in 2018 (pages 71-88).

The paper addresses inter-class similarity in fine-grained visual classification through a novel optimization procedure called Pairwise Confusion (PC) that attempts to learn features with greater generalization, thereby preventing overfitting. With PC regularization, the authors obtained state-of-the-art performance on six of the most widely-used FGVC datasets and demonstrated improved localization ability.

The DBLP entry is available at: https://dblp.org/rec/conf/eccv/DubeyGGRFN18.html


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_r20_literature_search_20260519T045626",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-19T04:58:45.584167+00:00_

Web search results for query: ""Grammar-Aligned Decoding" Park Wang Berg-Kirkpatrick NeurIPS 2024 bibtex authors"

Links: [{"title":"Grammar-Aligned Decoding","url":"https://papers.nips.cc/paper_files/paper/2024/hash/2bdc2267c3d7d01523e2e17ac0a754f3-Abstract-Conference.html"},{"title":"Grammar-Aligned Decoding","url":"https://proceedings.neurips.cc/paper_files/paper/2024/hash/2bdc2267c3d7d01523e2e17ac0a754f3-Abstract-Conference.html"},{"title":"[2405.21047] Grammar-Aligned Decoding","url":"https://arxiv.org/abs/2405.21047"},{"title":"NeurIPS Poster Grammar-Aligned Decoding","url":"https://nips.cc/virtual/2024/poster/96599"},{"title":"Kanghee Park, Jiayu Wang, Taylor Berg-Kirkpatrick, Nadia Polikarpova, Loris D'Antoni · Grammar-Aligned Decoding","url":"https://slideslive.com/39028324/grammaraligned-decoding"},{"title":"NeurIPS Poster Grammar-Aligned Decoding","url":"https://neurips.cc/virtual/2024/poster/96599"},{"title":"Grammar-Aligned Decoding Kanghee Park1∗ Jiayu Wang1∗ Taylor Berg-Kirkpatrick2","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/2bdc2267c3d7d01523e2e17ac0a754f3-Paper-Conference.pdf"},{"title":"Grammar-Aligned Decoding | OpenReview","url":"https://openreview.net/forum?id=5G7ve8E1Lu"},{"title":"Grammar-Aligned Decoding","url":"https://arxiv.org/html/2405.21047v3"},{"title":"Grammar-aligned decoding | Proceedings of the 38th International Conference on Neural Information Processing Systems","url":"https://dl.acm.org/doi/10.5555/3737916.3738690"}]

Based on the search results, here is the information about "Grammar-Aligned Decoding":

**Authors:** Kanghee Park, Jiayu Wang, Taylor Berg-Kirkpatrick, Nadia Polikarpova, Loris D'Antoni

**Conference:** Advances in Neural Information Processing Systems 37 (NeurIPS 2024) Main Conference Track

**Paper Information:** The paper addresses the problem of reliable structured output generation from large language models. GCD techniques can distort the LLM's distribution, leading to outputs that are
…[truncated 506 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_r20_literature_search_20260519T045626",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-19T04:58:45.584334+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Mark Collier\" 2021 class similarity correlated softmax label"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_r20_literature_search_20260519T045626",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Mark Collier\" 2021 class similarity correlated softmax label"
  }
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-19T04:58:45.584457+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Collier Beel 2021 class similarity confusion matrix loss function"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_r20_literature_search_20260519T045626",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Collier Beel 2021 class similarity confusion matrix loss function"
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-19T04:58:45.584603+00:00_

Web search results for query: ""Mark Collier" 2021 class similarity correlated softmax label"

Links: [{"title":"[PDF] Correlated Input-Dependent Label Noise in Large-Scale Image Classification | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Correlated-Input-Dependent-Label-Noise-in-Image-Collier-Mustafa/6ac8e0915df41692bdceef7f18bc1c50271630fc"},{"title":"Correlated Input-Dependent Label Noise in Large-Scale Image Classification | Request PDF","url":"https://www.researchgate.net/publication/355866332_Correlated_Input-Dependent_Label_Noise_in_Large-Scale_Image_Classification"},{"title":"Correlated Input-Dependent Label Noise in Large-Scale Image Classiﬁcation","url":"https://openaccess.thecvf.com/content/CVPR2021/papers/Collier_Correlated_Input-Dependent_Label_Noise_in_Large-Scale_Image_Classification_CVPR_2021_paper.pdf"},{"title":"Class-Similarity Based Label Smoothing for Conﬁdence Calibration","url":"http://users.umiacs.umd.edu/~josephj/ClassSimiliarity.pdf"},{"title":"Class-Similarity Based Label Smoothing for Confidence Calibration","url":"https://arxiv.org/pdf/2006.14028"},{"title":"[2406.09908] What Does Softmax Probability Tell Us about Classifiers Ranking Across Diverse Test Conditions?","url":"https://arxiv.org/abs/2406.09908"},{"title":"Leveraging Class Similarity to Improve Deep Neural Network Robustness","url":"https://arxiv.org/pdf/1812.09744"},{"title":"Multiclass classification with softmax regression explained | Towards Data Science","url":"https://towardsdatascience.com/multiclass-classification-with-softmax-regression-explained-ea320518ea5d/"},{"title":"Exploiting Class Similarity for Machine Learning with Confidence Labels   and Projective Loss Functions","url":"https://arxiv.org/pdf/2103.13607"}]

Based on the search results, I found the relevant research. Mark Collier published work in May 2021 on "Correlated Input-Dependent Label Noise in Large-Scale Image Classification". 

The work demonstrates that a learned covariance str
…[truncated 711 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_r20_literature_search_20260519T045626",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-19T04:58:45.584777+00:00_

Web search results for query: "Collier Beel 2021 class similarity confusion matrix loss function"

Links: [{"title":"On the Normalization of Confusion Matrices: Methods and Geometric Interpretations","url":"https://arxiv.org/html/2509.04959v1"},{"title":"Confusion Matrix-Based Loss Functions","url":"https://www.emergentmind.com/topics/confusion-matrix-based-loss-functions"},{"title":"Confusion Matrix–Based Loss Functions","url":"https://www.emergentmind.com/topics/confusion-matrix-based-loss-functions-b066a765-0eb4-49e5-a836-c85ecd113561"},{"title":"AnyLoss: Transforming Classification Metrics into Loss Functions","url":"https://arxiv.org/html/2405.14745v1"},{"title":"1 INTRODUCTION","url":"https://arxiv.org/html/2509.04959"},{"title":"AnyLoss: Transforming Classification Metrics into Loss Functions","url":"https://arxiv.org/pdf/2405.14745"}]

Based on the search results, I found relevant information about confusion matrix-based loss functions and class similarity, though the specific 2021 Collier and Beel paper was not directly returned. However, the results discuss related concepts:

In heterogeneous settings, confusion matrix values are shaped by two main factors: class similarity—how easily the model confuses two classes—and distribution bias, arising from skewed distributions in the training and test sets.

Since confusion matrix values reflect a mix of both factors, making it difficult to disentangle their individual contributions, bistochastic normalization using Iterative Proportional Fitting has been introduced as a generalization of row and column normalization.

The search results also discuss modern approaches to confusion matrix-based loss functions. Methods have been developed that can use any confusion matrix-based evaluation metric as a loss function to optimize learning processes.

If you're looking for the specific 2021 Collier and Beel paper, you may want to search directly on arxiv.org or Google Scholar with those author names, as my search didn'
…[truncated 142 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_r20_literature_search_20260519T045626",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-19T04:58:45.584972+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Mark Collier \"Correlated Input-Dependent Label Noise\" CVPR 2021 bibtex full authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_r20_literature_search_20260519T045626",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Mark Collier \"Correlated Input-Dependent Label Noise\" CVPR 2021 bibtex full authors"
  }
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-19T04:58:45.585097+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Gare Galeotti 2021 \"Exploiting Class Similarity\" published venue conference journal"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_r20_literature_search_20260519T045626",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Gare Galeotti 2021 \"Exploiting Class Similarity\" published venue conference journal"
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-19T04:58:45.585259+00:00_

Web search results for query: "Mark Collier "Correlated Input-Dependent Label Noise" CVPR 2021 bibtex full authors"

Links: [{"title":"Correlated Input-Dependent Label Noise in Large-Scale Image Classification - researchr publication","url":"https://researchr.org/publication/CollierMKJB21"},{"title":"Papers with Code - Correlated Input-Dependent Label Noise in Large-Scale Image Classification","url":"https://paperswithcode.com/paper/correlated-input-dependent-label-noise-in"},{"title":"Related Material - CVPR 2021 Open Access Repository","url":"https://openaccess.thecvf.com/content/CVPR2021/html/Collier_Correlated_Input-Dependent_Label_Noise_in_Large-Scale_Image_Classification_CVPR_2021_paper.html"},{"title":"[PDF] Correlated Input-Dependent Label Noise in Large-Scale Image Classification | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Correlated-Input-Dependent-Label-Noise-in-Image-Collier-Mustafa/6ac8e0915df41692bdceef7f18bc1c50271630fc"},{"title":"[2105.10305] Correlated Input-Dependent Label Noise in Large-Scale Image Classification","url":"https://arxiv.org/abs/2105.10305"},{"title":"Correlated Input-Dependent Label Noise in Large-Scale Image Classification - ADS","url":"https://ui.adsabs.harvard.edu/abs/2021arXiv210510305C/abstract"},{"title":"Correlated Input-Dependent Label Noise in Large-Scale Image Classification | Request PDF","url":"https://www.researchgate.net/publication/355866332_Correlated_Input-Dependent_Label_Noise_in_Large-Scale_Image_Classification"},{"title":"Correlated Input-Dependent Label Noise in Large-Scale Image   Classification","url":"https://arxiv.org/pdf/2105.10305"},{"title":"Basil Mustafa - Label noise","url":"https://www.basilmustafa.com/publications/label-noise"},{"title":"Correlated Input-Dependent Label Noise in Large-Scale Image Classiﬁcation","url":"https://openaccess.thecvf.com/content/CVPR2021/papers/Collier_Correlated_Input-Dependent_Label_Noise_in_Large-Scale_Image_Classification_CVPR_2021_paper.pdf"}]

Bas
…[truncated 922 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_r20_literature_search_20260519T045626",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-19T04:58:45.585422+00:00_

Web search results for query: "Gare Galeotti 2021 "Exploiting Class Similarity" published venue conference journal"

Links: [{"title":"[PDF] Exploiting Class Similarity for Machine Learning with Confidence Labels and Projective Loss Functions | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Exploiting-Class-Similarity-for-Machine-Learning-Gare-Galeotti/1c808e1aa382a1e4a59763a15e733457d1bd459b"},{"title":"(PDF) Exploiting Class Similarity for Machine Learning with Confidence Labels and Projective Loss Functions","url":"https://www.researchgate.net/publication/350398245_Exploiting_Class_Similarity_for_Machine_Learning_with_Confidence_Labels_and_Projective_Loss_Functions"},{"title":"[2103.13607] Exploiting Class Similarity for Machine Learning with Confidence Labels and Projective Loss Functions","url":"https://arxiv.org/abs/2103.13607"},{"title":"Exploiting Class Similarity for Machine Learning with Confidence Labels and Projective Loss Functions | DeepAI","url":"https://deepai.org/publication/exploiting-class-similarity-for-machine-learning-with-confidence-labels-and-projective-loss-functions"},{"title":"Exploiting Class Similarity for Machine Learning with Confidence Labels   and Projective Loss Functions","url":"https://arxiv.org/pdf/2103.13607"},{"title":"Gautam Rajendrakumar Gare","url":"https://ggare-cmu.github.io/"}]

Based on the search results, the paper "Exploiting Class Similarity for Machine Learning with Confidence Labels and Projective Loss Functions" by Gautam Rajendrakumar Gare and John Michael Galeotti was published in ArXiv in 2021 (volume abs/2103.13607). The paper was published as a preprint on March 25, 2021.

The published venue is **ArXiv** (an open-access repository for preprints), rather than a traditional conference or journal. The work has a DOI of 10.48550/arXiv.2103.13607.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_r20_literature_search_20260519T045626",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-19T04:58:45.585634+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

````json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/r20_literature_additions.md",
  "content": "# R20 Literature Additions\n\n## MR1: Dubey et al. (2018)\n\n### BibTeX\n```bibtex\n@inproceedings{dubey-2018-pairwise-confusion,\n  author    = {Abhimanyu Dubey and Otkrist Gupta and Pei Guo and Ramesh Raskar and Ryan Farrell and Nikhil Naik},\n  title     = {Pairwise Confusion for Fine-Grained Visual Classification},\n  booktitle = {Proceedings of the European Conference on Computer Vision (ECCV)},\n  pages     = {71--88},\n  year      = {2018}\n}\n```\n\n### Suggested citation text\nIn visual recognition, pairwise confusion between classes has been explicitly modeled to improve fine-grained classification \\citep{dubey-2018-pairwise-confusion}, where a regularization objective encourages the learned features to reduce inter-class confusability. Our Schema Confusability Score (SCS) brings a similar pairwise confusability quantification to NLP information extraction, measuring how likely an LLM is to confuse one relation (or event) type with another under structured decoding.\n\n\n## MR2: Collier et al. (2021)\n\n> **注意**: 用户指定的标题 \"Exploiting Class Similarity for Machine Learning with Confidence Labels\" 实际作者是 Gare & Galeotti (arXiv 2021)，不是 Collier。Collier et al. 2021 的论文是 \"Correlated Input-Dependent Label Noise in Large-Scale Image Classification\" (CVPR 2021)，主题也涉及 class similarity（通过 label noise correlation 建模类间相似性）。两篇均列出，请确认需要哪篇。\n\n### Option A: Gare & Galeotti (2021) — 匹配用户给的标题\n```bibtex\n@article{gare-2021-class-similarity,\n  author    = {Gautam Rajendrakumar Gare and John Michael Galeotti},\n  title     = {Exploiting Class Similarity for Machine Learning with Confidence Labels and Projective Loss Functions},\n  journal   = {arXiv preprint arXiv:2103.13607},\n  year      = {2021}\n}\n```\n\n#### Suggested citation text (Option A)\n\\citet{gare-2021-class-similarity} introduce confidence labels that encode pairwise class similarity and propose projective loss functions that relax penalties for confusions between similar classes, showing that explicitly modeling inter-class confusability improves robustness to label noise.\n\n### Option B: Collier et al. (2021) — 匹配用户给的作者名\n```bibtex\n@inproceedings{collier-2021-correlated-noise,\n  author    = {Mark Collier and Basil Mustafa and Efi Kokiopoulou and Rodolphe Jenatton and Jesse Berent},\n  title     = {Correlated Input-Dependent Label Noise in Large-Scale Image Classification},\n  booktitle = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},\n  pages     = {1551--1560},\n  year      = {2021}\n}\n```\n\n#### Suggested citation text (Option B)\n\\citet{collier-2021-correlated-noise} model label noise as input-dependent and correlated across semantically similar classes, demonstrating that the learned covariance structure captures known inter-class confusability patterns in large-scale classification.\n\n\n## MR3: LLM calibration × constrained decoding\n\n### BibTeX\n```bibtex\n@inproceedings{park-2024-grammar-aligned,\n  author    = {Kanghee Park and Jiayu Wang and Taylor Berg-Kirkpatrick and Nadia Polikarpova and Loris D'Antoni},\n  title     = {Grammar-Aligned Decoding},\n  booktitle = {Advances in Neural Information Processing Systems 37 (NeurIPS)},\n  year      = {2024}\n}\n```\n\n### Suggested citation text\nConstrained decoding techniques that restrict LLM outputs to valid grammars (e.g., JSON schemas) can distort the model's original probability distribution, producing outputs whose likelihoods are no longer proportional to the unconstrained distribution \\citep{park-2024-grammar-aligned}. This distribution distortion is directly relevant to our setting, where structured extraction under schema constraints may alter the model's calibration and confusability patterns across relation types.\n"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "worker_research_r20_literature_search_20260519T045626",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/r20_literature_additions.md",
    "content": "# R20 Literature Additions\n\n## MR1: Dubey et al. (2018)\n\n### BibTeX\n```bibtex\n@inproceedings{dubey-2018-pairwise-confusion,\n  author    = {Abhimanyu Dubey and Otkrist Gupta and Pei Guo and Ramesh Raskar and Ryan Farrell and Nikhil Naik},\n  title     = {Pairwise Confusion for Fine-Grained Visual Classification},\n  booktitle = {Proceedings of the European Conference on Computer Vision (ECCV)},\n  pages     = {71--88},\n  year      = {2018}\n}\n```\n\n### Suggested citation text\nIn visual recognition, pairwise confusion between classes has been explicitly modeled to improve fine-grained classification \\citep{dubey-2018-pairwise-confusion}, where a regularization objective encourages the learned features to reduce inter-class confusability. Our Schema Confusability Score (SCS) brings a similar pairwise confusability quantification to NLP information extraction, measuring how likely an LLM is to confuse one relation (or event) type with another under structured decoding.\n\n\n## MR2: Collier et al. (2021)\n\n> **注意**: 用户指定的标题 \"Exploiting Class Similarity for Machine Learning with Confidence Labels\" 实际作者是 Gare & Galeotti (arXiv 2021)，不是 Collier。Collier et al. 2021 的论文是 \"Correlated Input-Dependent Label Noise in Large-Scale Image Classification\" (CVPR 2021)，主题也涉及 class similarity（通过 label noise correlation 建模类间相似性）。两篇均列出，请确认需要哪篇。\n\n### Option A: Gare & Galeotti (2021) — 匹配用户给的标题\n```bibtex\n@article{gare-2021-class-similarity,\n  author    = {Gautam Rajendrakumar Gare and John Michael Galeotti},\n  title     = {Exploiting Class Similarity for Machine Learning with Confidence Labels and Projective Loss Functions},\n  journal   = {arXiv preprint arXiv:2103.13607},\n  year      = {2021}\n}\n```\n\n#### Suggested citation text (Option A)\n\\citet{gare-2021-class-similarity} introduce confidence labels that encode pairwise class similarity and propose projective loss functions that relax penalties for confusions between similar classes, showing that explicitly modeling inter-class confusability improves robustness to label noise.\n\n### Option B: Collier et al. (2021) — 匹配用户给的作者名\n```bibtex\n@inproceedings{collier-2021-correlated-noise,\n  author    = {Mark Collier and Basil Mustafa and Efi Kokiopoulou and Rodolphe Jenatton and Jesse Berent},\n  title     = {Correlated Input-Dependent Label Noise in Large-Scale Image Classification},\n  booktitle = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},\n  pages     = {1551--1560},\n  year      = {2021}\n}\n```\n\n#### Suggested citation text (Option B)\n\\citet{collier-2021-correlated-noise} model label noise as input-dependent and correlated across semantically similar classes, demonstrating that the learned covariance structure captures known inter-class confusability patterns in large-scale classification.\n\n\n## MR3: LLM calibration × constrained decoding\n\n### BibTeX\n```bibtex\n@inproceedings{park-2024-grammar-aligned,\n  author    = {Kanghee Park and Jiayu Wang and Taylor Berg-Kirkpatrick and Nadia Polikarpova and Loris D'Antoni},\n  title     = {Grammar-Aligned Decoding},\n  booktitle = {Advances in Neural Information Processing Systems 37 (NeurIPS)},\n  year      = {2024}\n}\n```\n\n### Suggested citation text\nConstrained decoding techniques that restrict LLM outputs to valid grammars (e.g., JSON schemas) can distort the model's original probability distribution, producing outputs whose likelihoods are no longer proportional to the unconstrained distribution \\citep{park-2024-grammar-aligned}. This distribution distortion is directly relevant to our setting, where structured extraction under schema constraints may alter the model's calibration and confusability patterns across relation types.\n"
  }
}
````

</details>

---

### Tool result

_source line 30 · 2026-05-19T04:58:45.585827+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/r20_literature_additions.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_r20_literature_search_20260519T045626",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 31 · 2026-05-19T04:58:45.586018+00:00_

文件已写入 `artifacts/r20_literature_additions.md`。

关键发现：
- **MR1** — Dubey et al. (2018) ECCV，pages 71-88，信息完整
- **MR2** — 标题与作者不匹配。"Exploiting Class Similarity..." 实际是 Gare & Galeotti (arXiv 2021)，而 Collier et al. 2021 是 "Correlated Input-Dependent Label Noise"（CVPR 2021, pages 1551-1560）。两篇都列出了 bib 和引用文本，请确认用哪篇
- **MR3** — Park et al. (2024) "Grammar-Aligned Decoding"，NeurIPS 2024，核心论点：constrained decoding 会扭曲 LLM 的概率分布，直接关联 schema 约束下的 calibration 问题

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_r20_literature_search_20260519T045626"
}
```

</details>

---
