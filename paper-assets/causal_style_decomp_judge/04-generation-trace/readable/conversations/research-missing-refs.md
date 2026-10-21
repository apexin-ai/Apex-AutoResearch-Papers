# research missing refs

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 35
- **Recorded user turns:** 0
- **Tool calls:** 17
- **Original source:** `logs/chats/worker_research_missing-refs_20260522T043517.jsonl`
- **Structured JSON:** [`cf9b5aacc4d40ee9a9d9.json`](../../sessions/cf/cf9b5aacc4d40ee9a9d9.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

35 recorded events

### Tool call

_source line 1 · 2026-05-22T04:37:26.585109+00:00_

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
  "session": "worker_research_missing-refs_20260522T043517",
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

_source line 2 · 2026-05-22T04:37:26.585499+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_missing-refs_20260522T043517",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-22T04:37:26.585671+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Girrbach \"Likert or Not\" LLM evaluation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_missing-refs_20260522T043517",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Girrbach \"Likert or Not\" LLM evaluation"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-22T04:37:26.585800+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "PRePair Jeong 2025 pairwise evaluation LLM"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_missing-refs_20260522T043517",
  "tool": "WebSearch",
  "tool_args": {
    "query": "PRePair Jeong 2025 pairwise evaluation LLM"
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-22T04:37:26.585919+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "acquiescence bias central tendency bias Likert scale classic reference Krosnick Paulhus"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_missing-refs_20260522T043517",
  "tool": "WebSearch",
  "tool_args": {
    "query": "acquiescence bias central tendency bias Likert scale classic reference Krosnick Paulhus"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-22T04:37:26.586086+00:00_

Web search results for query: "Girrbach "Likert or Not" LLM evaluation"

Links: [{"title":"[2505.19334] Likert or Not: LLM Absolute Relevance Judgments on Fine-Grained Ordinal Scales","url":"https://ar5iv.labs.arxiv.org/html/2505.19334"},{"title":"[2505.19334] Likert or Not: LLM Absolute Relevance Judgments on Fine-Grained Ordinal Scales","url":"https://arxiv.org/abs/2505.19334"},{"title":"Likert or Not: LLM Absolute Relevance Judgments on Fine-Grained Ordinal Scales","url":"https://arxiv.org/html/2505.19334v1"},{"title":"Likert or Not: LLM Absolute Relevance Judgments on Fine-Grained Ordinal Scales - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250519334G/abstract"},{"title":"Reference-Free Rating of LLM Responses via Latent Information","url":"https://arxiv.org/pdf/2509.24678"}]

Based on the search results, here's what I found:

"Likert or Not: LLM Absolute Relevance Judgments on Fine-Grained Ordinal Scales" is a research paper that examines two common methods for eliciting LLM relevance judgments: pointwise scoring (where an LLM sees a single query-document pair and outputs a relevance score) and listwise ranking (where the LLM sees a query and list of documents and outputs a permutation sorting them by relevance).

The research community consensus has been that listwise ranking yields superior performance, with the hypothesis that LLMs are better at making relative relevance judgments than absolute ones. However, the researchers found that the gap between pointwise scoring and listwise ranking shrinks when pointwise scoring is implemented using a sufficiently large ordinal relevance label space, becoming statistically insignificant for many LLM-benchmark dataset combinations.

Specifically, simple pointwise scoring prompts featuring relevance rubrics with up to 11 bins not only narrow the gap with listwise ranking, but do so to a point where the difference in performance has low statistical significance for many model-dataset combinations. The evaluat
…[truncated 296 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_missing-refs_20260522T043517",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-22T04:37:26.586261+00:00_

Web search results for query: "PRePair Jeong 2025 pairwise evaluation LLM"

Links: [{"title":"The Comparative Trap: Pairwise Comparisons Amplifies Biased Preferences of LLM Evaluators - ACL Anthology","url":"https://aclanthology.org/2025.blackboxnlp-1.5/"},{"title":"LLM-based Evaluators: Methods & Applications","url":"https://www.emergentmind.com/topics/llm-based-evaluators"},{"title":"[2406.12319] The Comparative Trap: Pairwise Comparisons Amplifies Biased Preferences of LLM Evaluators","url":"https://arxiv.org/abs/2406.12319"},{"title":"PRePair: Pointwise Reasoning Enhance Pairwise Evaluating for Robust Instruction-Following Assessments","url":"https://arxiv.org/html/2406.12319v1"},{"title":"The Comparative Trap: Pairwise Comparisons Amplifies Biased Preferences of LLM Evaluators (arXiv:2406.12319v4) - ScienceStack","url":"https://www.sciencestack.ai/paper/2406.12319"},{"title":"[Literature Review] The Comparative Trap: Pairwise Comparisons Amplifies Biased Preferences of LLM Evaluators","url":"https://www.themoonlight.io/en/review/the-comparative-trap-pairwise-comparisons-amplifies-biased-preferences-of-llm-evaluators"},{"title":"Aligning with Human Judgement: The Role of Pairwise Preference in Large   Language Model Evaluators","url":"https://arxiv.org/pdf/2403.16950"},{"title":"Pairwise Comparisons Amplify Biased Preferences of LLM ...","url":"https://aclanthology.org/2025.blackboxnlp-1.5.pdf"},{"title":"Efficient LLM Comparative Assessment: a Product of Experts Framework for   Pairwise Comparisons","url":"https://arxiv.org/pdf/2405.05894"}]

Based on the search results, here's what I found about PRePair and the Jeong 2025 research:

## Overview

The paper is authored by Hawon Jeong, ChaeHun Park, Jimin Hong, Hojoon Lee, and Jaegul Choo, and was published in the Proceedings of the 8th BlackboxNLP Workshop: Analyzing and Interpreting Neural Networks for NLP in 2025.

## Problem Addressed

As large language models (LLMs) are increasingly used as evaluators for na
…[truncated 884 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_missing-refs_20260522T043517",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-22T04:37:26.586512+00:00_

Web search results for query: "acquiescence bias central tendency bias Likert scale classic reference Krosnick Paulhus"

Links: [{"title":"Acquiescence Bias: What It Is, Examples & How to Reduce | Lensym","url":"https://lensym.com/blog/acquiescence-bias-guide"},{"title":"(PDF) A Bayesian Perspective on Likert Scales and Central Tendency","url":"https://www.researchgate.net/publication/318013690_A_Bayesian_Perspective_on_Likert_Scales_and_Central_Tendency"},{"title":"Likert Scale Design: How to Build Scales That Measure What You Think | Lensym","url":"https://lensym.com/blog/likert-scale-design-guide"},{"title":"Acquiescence Bias and Criterion Validity: Problems and Potential Solutions for Agree-Disagree Scales | Political Behavior | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s11109-026-10124-z"},{"title":"Some Biases in Likert Scaling Usage and its Correction","url":"https://www.gssrr.org/index.php/JournalOfBasicAndApplied/article/download/9874/4329/"},{"title":"Information loss and bias in likert survey responses | PLOS One","url":"https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0271949"},{"title":"Controlling for Response Biases in Self-Report Scales: Forced-Choice vs. Psychometric Modeling of Likert Items - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC6803422/"},{"title":"The effects of reverse items on psychometric properties ...","url":"https://files.eric.ed.gov/fulltext/EJ1440235.pdf"},{"title":"Frontiers | Controlling for Response Biases in Self-Report Scales: Forced-Choice vs. Psychometric Modeling of Likert Items","url":"https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2019.02309/full"}]

Based on the search results, here's what I found regarding acquiescence bias, central tendency bias, Likert scales, and the key researchers you mentioned:

## Acquiescence Bias

Acquiescence bias is the tendency to agree with statements regardless of their content, creating a "yes-saying" pattern
…[truncated 1140 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_missing-refs_20260522T043517",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-22T04:37:26.586697+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2505.19334 \"Likert or Not\" authors Girrbach"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_missing-refs_20260522T043517",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2505.19334 \"Likert or Not\" authors Girrbach"
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-22T04:37:26.586827+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"The Comparative Trap\" PRePair Jeong BlackboxNLP 2025 BibTeX"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_missing-refs_20260522T043517",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"The Comparative Trap\" PRePair Jeong BlackboxNLP 2025 BibTeX"
  }
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-22T04:37:26.586945+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Krosnick 1999 \"response order effects\" survey methodology handbook BibTeX"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_missing-refs_20260522T043517",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Krosnick 1999 \"response order effects\" survey methodology handbook BibTeX"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-22T04:37:26.587081+00:00_

Web search results for query: "arxiv 2505.19334 "Likert or Not" authors Girrbach"

Links: [{"title":"[2505.19334] Likert or Not: LLM Absolute Relevance Judgments on Fine-Grained Ordinal Scales","url":"https://arxiv.org/abs/2505.19334"},{"title":"[2505.19334] Likert or Not: LLM Absolute Relevance Judgments on Fine-Grained Ordinal Scales","url":"https://ar5iv.labs.arxiv.org/html/2505.19334"},{"title":"Information loss and bias in likert survey responses","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9333316/"},{"title":"Likert or Not: LLM Absolute Relevance Judgments on Fine-Grained Ordinal Scales","url":"https://arxiv.org/html/2505.19334"},{"title":"Information Retrieval May 2025","url":"https://www.arxiv.org/list/cs.IR/2025-05?skip=375&show=250"},{"title":"How does item wording affect participants’ responses in Likert scale? Evidence from IRT analysis","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11486723/"}]

Based on the search results, I found the paper you're looking for. However, I should note that the author you mentioned (Girrbach) does not appear to be listed as an author of this paper.

The paper arxiv 2505.19334 titled "Likert or Not: LLM Absolute Relevance Judgments on Fine-Grained Ordinal Scales" was authored by Charles Godfrey, Ping Nie, Natalia Ostapuk, David Ken, Shang Gao, and Souheil Inati.

The paper examines how Large Language Models obtain state-of-the-art zero-shot relevance ranking performance, with the underlying hypothesis being that LLMs are better at making relative relevance judgments than absolute ones.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_missing-refs_20260522T043517",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-22T04:37:26.587239+00:00_

Web search results for query: ""The Comparative Trap" PRePair Jeong BlackboxNLP 2025 BibTeX"

Links: [{"title":"The Comparative Trap: Pairwise Comparisons Amplifies Biased Preferences of LLM Evaluators - ACL Anthology","url":"https://aclanthology.org/2025.blackboxnlp-1.5/"},{"title":"Proceedings of the 8th BlackboxNLP Workshop: Analyzing and Interpreting Neural Networks for NLP - ACL Anthology","url":"https://aclanthology.org/volumes/2025.blackboxnlp-1/"},{"title":"BlackboxNLP: Analyzing and Interpreting Neural Networks for NLP (2025) - ACL Anthology","url":"https://aclanthology.org/events/blackboxnlp-2025/"},{"title":"@inproceedings{jeong-etal-2025-comparative,","url":"https://aclanthology.org/2025.blackboxnlp-1.5.bib"},{"title":"[PDF] The Comparative Trap: Pairwise Comparisons Amplifies Biased Preferences of LLM Evaluators | Semantic Scholar","url":"https://www.semanticscholar.org/paper/The-Comparative-Trap:-Pairwise-Comparisons-Biased-Jeong-Park/cd6191f270c5b98dec44a294e4f3cebcf371ac5f"},{"title":"[2406.12319] The Comparative Trap: Pairwise Comparisons Amplifies Biased Preferences of LLM Evaluators","url":"https://arxiv.org/abs/2406.12319"},{"title":"BlackboxNLP 2025 The 8th BlackboxNLP Workshop: Analyzing and","url":"https://aclanthology.org/2025.blackboxnlp-1.0.pdf"},{"title":"[Literature Review] The Comparative Trap: Pairwise Comparisons Amplifies Biased Preferences of LLM Evaluators","url":"https://www.themoonlight.io/en/review/the-comparative-trap-pairwise-comparisons-amplifies-biased-preferences-of-llm-evaluators"},{"title":"Preprint. Under review. The Comparative Trap: Pairwise Comparisons Amplifies","url":"https://arxiv.org/pdf/2406.12319"}]

I found the paper and its BibTeX entry. Here are the results:

## Paper Information

"The Comparative Trap: Pairwise Comparisons Amplifies Biased Preferences of LLM Evaluators" was published in Proceedings of the 8th BlackboxNLP Workshop: Analyzing and Interpreting Neural Networks for NLP, with authors Hawon Jeong, C
…[truncated 547 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_missing-refs_20260522T043517",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-22T04:37:26.587468+00:00_

Web search results for query: "Krosnick 1999 "response order effects" survey methodology handbook BibTeX"

Links: [{"title":"Response-Order Effects for Self-report Questionnaires","url":"https://www.jasnh.com/pdf/Vol16-No2-article4.pdf"},{"title":"Question and Questionnaire Design (Chapter 16) - The Cambridge Handbook of Research Methods and Statistics for the Social and Behavioral Sciences","url":"https://www.cambridge.org/core/books/abs/cambridge-handbook-of-research-methods-and-statistics-for-the-social-and-behavioral-sciences/question-and-questionnaire-design/EC913C0C701B356AE4EF7DAB57270BA3"},{"title":"JON A. KROSNICK 450 Serra Mall Stanford University Stanford, CA 94305","url":"https://www.coastalresearchcenter.ucsb.edu/cmi/CMI%20CVs/Krosnick.pdf"},{"title":"Exploring the impact of response option sequences/order on survey rating scale responses | Forum for Philosophical Studies","url":"https://ojs.acad-pub.com/index.php/FPS/article/view/452"},{"title":"(PDF) An Evaluation of a Cognitive Theory of Response-Order Effects in Survey Measurement","url":"https://www.academia.edu/130434109/An_Evaluation_of_a_Cognitive_Theory_of_Response_Order_Effects_in_Survey_Measurement"},{"title":"[PDF] AN EVALUATION OF A COGNITIVE THEORY OF RESPONSE-ORDER EFFECTS IN SURVEY MEASUREMENT | Semantic Scholar","url":"https://www.semanticscholar.org/paper/AN-EVALUATION-OF-A-COGNITIVE-THEORY-OF-EFFECTS-IN-Krosnick-Alwin/3c6cbd0875c08364aa86123ae110f2871a01885e"},{"title":"(PDF) An Evaluation of A Cognitive Theory of Response-Order Effects in Survey Measurement","url":"https://www.researchgate.net/publication/31106425_An_Evaluation_of_A_Cognitive_Theory_of_Response-Order_Effects_in_Survey_Measurement"}]

Based on the search results, I found references to Krosnick's work on response order effects. The most relevant citation appears to be Krosnick, J. A. (1999). Survey research. Annual Review of Psychology, 50, 537–567.

However, the search results also reference an earlier and widely-cite
…[truncated 737 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_missing-refs_20260522T043517",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-22T04:37:26.587633+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2505.19334 Girrbach Likert ordinal scales authors list"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_missing-refs_20260522T043517",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2505.19334 Girrbach Likert ordinal scales authors list"
  }
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-22T04:37:26.587755+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Paulhus 1991 \"measurement and control of response bias\" \"measures of personality and social psychological attitudes\" BibTeX"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_missing-refs_20260522T043517",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Paulhus 1991 \"measurement and control of response bias\" \"measures of personality and social psychological attitudes\" BibTeX"
  }
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-22T04:37:26.587868+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclanthology.org/2025.blackboxnlp-1.5.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_missing-refs_20260522T043517",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclanthology.org/2025.blackboxnlp-1.5.bib"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-22T04:37:26.587990+00:00_

Web search results for query: "arxiv 2505.19334 Girrbach Likert ordinal scales authors list"

Links: [{"title":"[2505.19334] Likert or Not: LLM Absolute Relevance Judgments on Fine-Grained Ordinal Scales","url":"https://arxiv.org/abs/2505.19334"},{"title":"Likert or Not: LLM Absolute Relevance Judgments on Fine-Grained Ordinal Scales - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250519334G/abstract"},{"title":"Statistical Practices of Likert Scales","url":"https://www.emergentmind.com/topics/statistical-practices-of-likert-scales"},{"title":"Information Retrieval May 2025","url":"https://www.arxiv.org/list/cs.IR/2025-05?skip=375&show=250"},{"title":"A Comparison of Parametric and Non-Parametric Methods Applied to a Likert Scale","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5597151/"},{"title":"Don't Let Your Likert Scales Grow Up To Be Visual Analog ...","url":"https://arxiv.org/pdf/2502.02846"},{"title":"A geometrical approach to the ordinal data of Likert scaling and attitude measurements: The density matrix in psychology - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0022249613000254"}]

Based on the search results, I found the information about arxiv paper 2505.19334. The authors are: Charles Godfrey, Ping Nie, Natalia Ostapuk, David Ken, Shang Gao, and Souheil Inati. 

The paper is titled "Likert or Not: LLM Absolute Relevance Judgments on Fine-Grained Ordinal Scales".


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_missing-refs_20260522T043517",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-22T04:37:26.588141+00:00_

Web search results for query: "Paulhus 1991 "measurement and control of response bias" "measures of personality and social psychological attitudes" BibTeX"

Links: [{"title":"Measurement and Control of Response Bias In Non- ...","url":"https://ijahss.com/Paper/04062019/1179495084.pdf"},{"title":"Paulhus, D. L. (1991). Measurement and control of response bias. In J. P. Robinson, J. R. Shaver, & L. S. Wrightsman (Eds.), Measure of personality and social psychological attitudes (pp. 17-59). San Diego, CA Academic Press. - References - Scientific Research Publishing","url":"https://www.scirp.org/(S(vtj3fa45qm1ean45wffcz5%205))/reference/referencespapers.aspx?referenceid=447986"},{"title":"Paulhus, D. L. (1991). Measurement and control of response bias. J. P. Robinson, P. R. Shaver, & L. S. Wrightsman (Eds.), Measures of personality and social psychological attitudes (pp. 17-59). San Diego, CA Academic Press. - References - Scientific Research Publishing","url":"https://www.scirp.org/reference/referencespapers?referenceid=254751"},{"title":"Paulhus, D.L. (1991) Measurement and Control of Response Bias. In Measures of Personality and Social Psychological Attitudes, Academic Press, San Diego, 17-59. - References - Scientific Research Publishing","url":"https://www.scirp.org/reference/referencespapers?referenceid=2477368"},{"title":"Measurement and control of response bias. | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Measurement-and-control-of-response-bias.-Paulhus/26c2b538729679b9f956687fe753cff9038ac8a6"},{"title":"(PDF) Measurement and Control of Response Bias","url":"https://www.researchgate.net/publication/246790479_Measurement_and_Control_of_Response_Bias"},{"title":"Decision Making Individual Differences Inventory - Balanced Inventory of Desirable Responding","url":"https://sjdm.org/dmidi/Balanced_Inventory_of_Desirable_Responding.html"},{"title":"115 Paulhus, D. L. (1991). Measurement and control of ...","url":"http://digitalwolfgram.widener.ed
…[truncated 1218 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_missing-refs_20260522T043517",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-22T04:37:26.588299+00:00_

&lt;tool_use_error>InputValidationError: WebFetch failed due to the following issue:
The required parameter `prompt` is missing

This tool's schema was not sent to the API — it was not in the discovered-tool set derived from message history. Without the schema in your prompt, typed parameters (arrays, numbers, booleans) get emitted as strings and the client-side parser rejects them. Load the tool first: call ToolSearch with query "select:WebFetch", then retry this call.&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_missing-refs_20260522T043517",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-22T04:37:26.588449+00:00_

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
  "session": "worker_research_missing-refs_20260522T043517",
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

_source line 22 · 2026-05-22T04:37:26.588566+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_missing-refs_20260522T043517",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-22T04:37:26.588675+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2505.19334",
  "prompt": "List ALL authors of this paper exactly as shown. I need every author name."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_missing-refs_20260522T043517",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2505.19334",
    "prompt": "List ALL authors of this paper exactly as shown. I need every author name."
  }
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-22T04:37:26.588786+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclanthology.org/2025.blackboxnlp-1.5/",
  "prompt": "Extract the complete BibTeX entry for this paper, including all authors, title, booktitle, year, pages, publisher, url, doi."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_missing-refs_20260522T043517",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclanthology.org/2025.blackboxnlp-1.5/",
    "prompt": "Extract the complete BibTeX entry for this paper, including all authors, title, booktitle, year, pages, publisher, url, doi."
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-22T04:37:26.588904+00:00_

# Authors of arXiv:2505.19334

Based on the paper content, the authors are:

1. Charles Godfrey
2. Ping Nie
3. Natalia Ostapuk
4. David Ken
5. Shang Gao
6. Souheil Inati

The paper's authors section lists these six researchers as contributors to "Likert or Not: LLM Absolute Relevance Judgments on Fine-Grained Ordinal Scales."

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_missing-refs_20260522T043517",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-22T04:37:26.589024+00:00_

# BibTeX Entry

```bibtex
@inproceedings{jeong-etal-2025-comparative,
    title = "The Comparative Trap: Pairwise Comparisons Amplifies Biased Preferences of {LLM} Evaluators",
    author = "Jeong, Hawon  and
      Park, ChaeHun  and
      Hong, Jimin  and
      Lee, Hojoon  and
      Choo, Jaegul",
    editor = "Belinkov, Yonatan  and
      Mueller, Aaron  and
      Kim, Najoung  and
      Mohebbi, Hosein  and
      Chen, Hanjie  and
      Arad, Dana  and
      Sarti, Gabriele",
    booktitle = "Proceedings of the 8th BlackboxNLP Workshop: Analyzing and Interpreting Neural Networks for NLP",
    month = nov,
    year = "2025",
    address = "Suzhou, China",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2025.blackboxnlp-1.5/",
    doi = "10.18653/v1/2025.blackboxnlp-1.5",
    pages = "79--108",
    ISBN = "979-8-89176-346-3"
}
```

This entry includes all five authors, the complete title, conference proceedings designation, publication details, and both URL and DOI identifiers for the paper presented at the BlackboxNLP workshop in November 2025.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_missing-refs_20260522T043517",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-22T04:37:26.589155+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Girrbach author \"Likert\" LLM judge evaluation paper 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_missing-refs_20260522T043517",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Girrbach author \"Likert\" LLM judge evaluation paper 2025 2026"
  }
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-22T04:37:26.589267+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Krosnick 1999 \"survey research\" \"Annual Review of Psychology\" BibTeX"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_missing-refs_20260522T043517",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Krosnick 1999 \"survey research\" \"Annual Review of Psychology\" BibTeX"
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-22T04:37:26.589422+00:00_

Web search results for query: "Krosnick 1999 "survey research" "Annual Review of Psychology" BibTeX"

Links: [{"title":"Survey research. | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Survey-research.-Krosnick/2f6a21095cff8b18e8f16f9390b1160bd0315167"},{"title":"Krosnick, J. A. (1999). Survey research. Annual Review of Psychology, 50, 537-567. doi10.1146/annurev.psych.50.1.537 - References - Scientific Research Publishing","url":"https://www.scirp.org/reference/referencespapers?referenceid=691628"},{"title":"Krosnick, J. A. (1999). Survey Research. Annual Review of Psychology, 50, 537-567. - References - Scientific Research Publishing","url":"https://www.scirp.org/reference/referencespapers?referenceid=3978928"},{"title":"SURVEY RESEARCH | Annual Reviews","url":"https://www.annualreviews.org/content/journals/10.1146/annurev.psych.50.1.537"},{"title":"Survey Research | SpringerLink","url":"https://link.springer.com/10.1007/978-94-007-0753-5_2925"},{"title":"Survey research - WebSM.org","url":"https://www.websm.org/db/12/16451/Web%20Survey%20Bibliography/Survey_research/?cat=378&p1=1123&p2=82&p3=85&p4=87&p5=551&id=551&cat=378&page=47"},{"title":"Survey research - ProQuest","url":"https://www.proquest.com/scholarly-journals/survey-research/docview/205847042/se-2"},{"title":"Survey research - PubMed","url":"https://pubmed.ncbi.nlm.nih.gov/15012463/"},{"title":"Publications - Jon A. Krosnick, Ph.D.","url":"https://www.jonkrosnick.com/publications.html"}]

Based on the search results, here is the BibTeX entry for the Krosnick 1999 publication:

@article{Krosnick1999SurveyR,
  title={Survey research.},
  author={Jon A. Krosnick},
  journal={Annual review of psychology},
  year={1999},
  volume={50},
  pages={537-567}
}

Alternatively, a more complete version with DOI information would be:

```
@article{Krosnick1999,
  author={Krosnick, Jon A.},
  title={Survey research},
  journal={Annual Review of Psychology},
  year={1999},
  volume={50},
  pages={537--
…[truncated 153 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_missing-refs_20260522T043517",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-22T04:37:26.589584+00:00_

Web search results for query: "Girrbach author "Likert" LLM judge evaluation paper 2025 2026"

Links: [{"title":"LLM-as-a-Judge: automated evaluation of search query parsing using large language models - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12319771/"},{"title":"Moving LLM evaluation forward: lessons from human judgment research","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12149859/"},{"title":"Published as a conference paper at ICLR 2025 TRUST OR ESCALATE: LLM JUDGES WITH","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/08dabd5345b37fffcbe335bd578b15a0-Paper-Conference.pdf"},{"title":"Judging the Judges: Evaluating Alignment and Vulnerabilities in LLMs-as-Judges","url":"https://arxiv.org/pdf/2406.12624"},{"title":"LLM-as-a-Judge Scoring","url":"https://www.emergentmind.com/topics/llm-as-a-judge-scoring"},{"title":"A Judge-Aware Ranking Framework for Evaluating Large Language Models without Ground Truth","url":"https://arxiv.org/pdf/2601.21817"},{"title":"Reference-Free Rating of LLM Responses via Latent Information","url":"https://arxiv.org/pdf/2509.24678"},{"title":"The Silent Judge: Unacknowledged Shortcut Bias in LLM-as-a-Judge","url":"https://arxiv.org/pdf/2509.26072"}]

Based on the search results, I found a relevant paper by Leander Girrbach and colleagues:

"Reference-Free Rating of LLM Responses via Latent Information" by Leander Girrbach, Chi-Ping Su, Tankred Saanum, Richard Socher, Eric Schulz, and Zeynep Akata

This paper studies the common practice of asking a judge model to assign Likert-scale scores to free-text responses and shows two systematic issues: scores are unstable under sampling and poorly calibrated, leading to compression near the top of the scale and frequent ties. The authors propose Latent Judges, which derive scalar ratings from internal model signals: (i) probability-weighted scores over integer ratings, (ii) verifier-style probabilities of "yes", and (iii) linear probes trained on model activati
…[truncated 296 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_missing-refs_20260522T043517",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-22T04:37:26.589757+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2509.24678",
  "prompt": "List ALL authors of this paper, the exact title, and the submission date. Also check if the paper mentions \"Likert or Not\" or if the subtitle contains these words."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_missing-refs_20260522T043517",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2509.24678",
    "prompt": "List ALL authors of this paper, the exact title, and the submission date. Also check if the paper mentions \"Likert or Not\" or if the subtitle contains these words."
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-22T04:37:26.589884+00:00_

# Paper Information

**Authors:**
1. Leander Girrbach
2. Chi-Ping Su
3. Tankred Saanum
4. Richard Socher
5. Eric Schulz
6. Zeynep Akata

**Exact Title:**
"Reference-Free Rating of LLM Responses via Latent Information"

**Submission Date:**
September 29, 2025

**"Likert or Not" Search:**
The paper does not mention "Likert or Not" as a phrase, nor does the subtitle contain these words. However, the abstract does reference "Likert-scale scores" as part of the research focus.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_missing-refs_20260522T043517",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-22T04:37:26.590049+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Leander Girrbach\" Likert LLM evaluation 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_missing-refs_20260522T043517",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Leander Girrbach\" Likert LLM evaluation 2025 2026"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-22T04:37:26.590196+00:00_

Web search results for query: ""Leander Girrbach" Likert LLM evaluation 2025 2026"

Links: [{"title":"Reference-Free Rating of LLM Responses via Latent Information | Request PDF","url":"https://www.researchgate.net/publication/395969429_Reference-Free_Rating_of_LLM_Responses_via_Latent_Information"},{"title":"LLM Evaluation Frameworks 2025 vs 2026: What Matters ...","url":"https://www.mlaidigital.com/blogs/llm-evaluation-frameworks-2025-vs-2026-what-matters-now-2026"},{"title":"Leander Girrbach","url":"https://scholar.google.com/citations?user=xk6HHiAAAAAJ&hl=de"},{"title":"MCML - \"See, Don’t Assume\": Revealing and Reducing Gender Bias in AI","url":"https://mcml.ai/news/2025-12-18-research-insight-girrbach/"},{"title":"Reference-Free Rating of LLM Responses via Latent Information","url":"https://arxiv.org/pdf/2509.24678"},{"title":"Top 15 LLM Evaluation Metrics to Explore in 2026","url":"https://www.analyticsvidhya.com/blog/2025/03/llm-evaluation-metrics/"},{"title":"EconEvals: Benchmarks and Litmus Tests for Economic Decision-Making by LLM Agents","url":"https://arxiv.org/pdf/2503.18825"}]

Based on the search results, here's what I found about Leander Girrbach and LLM evaluation with Likert scales:

## Recent Work on LLM Evaluation

Leander Girrbach authored research on "Reference-Free Rating of LLM Responses via Latent Information" (published in September 2025), which addresses systematic issues with single-response LLM-as-a-judge ratings using Likert-scale scores, including instability under sampling and poor calibration.

The research proposes "Latent Judges," which derive scalar ratings from internal model signals including probability-weighted scores over integer ratings, verifier-style probabilities, and linear probes trained on model activations.

## Other Research by Girrbach

Beyond the Likert evaluation work, Girrbach was also involved in an ICLR 2025 paper on "Revealing and Reducing Gender Biases in Vision and Language Assistants," investigating biase
…[truncated 305 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_missing-refs_20260522T043517",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 35 · 2026-05-22T04:37:26.590438+00:00_

所有信息已收集完毕，以下是验证结果。

---

## Reference 1: "Girrbach et al. Likert or Not"

- **状态: 存疑 — 两篇论文混淆**

不存在一篇由 Girrbach 撰写、标题为 "Likert or Not" 的论文。这很可能是以下两篇论文的混淆：

**论文 A — 标题匹配 "Likert or Not"，但作者不含 Girrbach：**

```bibtex
@article{godfrey2025likert,
  title={Likert or Not: {LLM} Absolute Relevance Judgments on Fine-Grained Ordinal Scales},
  author={Godfrey, Charles and Nie, Ping and Ostapuk, Natalia and Ken, David and Gao, Shang and Inati, Souheil},
  journal={arXiv preprint arXiv:2505.19334},
  year={2025}
}
```
- 内容：pointwise scoring vs listwise ranking，ordinal scale 粒度对 LLM relevance judgment 的影响
- 偏 IR 方向，与 LLM-as-Judge style bias 关系较远

**论文 B — 作者含 Girrbach，讨论 Likert-scale rating 问题，但标题不是 "Likert or Not"：**

```bibtex
@article{girrbach2025reference,
  title={Reference-Free Rating of {LLM} Responses via Latent Information},
  author={Girrbach, Leander and Su, Chi-Ping and Saanum, Tankred and Socher, Richard and Schulz, Eric and Akata, Zeynep},
  journal={arXiv preprint arXiv:2509.24678},
  year={2025}
}
```
- 内容：LLM judge 用 Likert-scale 打分时 scores 不稳定、calibration 差、top-of-scale compression、frequent ties。提出 Latent Judges 用 internal signals 替代显式打分
- **与 style bias 项目高度相关，极可能是你想引的那篇**

**建议：确认你想引的是论文 B (Girrbach et al., 2025)，修正标题为 "Reference-Free Rating of LLM Responses via Latent Information"。**

---

## Reference 2: PRePair (Jeong et al. 2025)

- **状态: 存在**
- 完整标题: The Comparative Trap: Pairwise Comparisons Amplifies Biased Preferences of LLM Evaluators
- 作者: Hawon Jeong, ChaeHun Park, Jimin Hong, Hojoon Lee, Jaegul Choo
- Venue: BlackboxNLP 2025 (EMNLP Workshop), Suzhou, China
- PRePair 是论文提出的方法（Pointwise Reasoning Enhanced Pairwise evaluation）

```bibtex
@inproceedings{jeong-etal-2025-comparative,
    title = "The Comparative Trap: Pairwise Comparisons Amplifies Biased Preferences of {LLM} Evaluators",
    author = "Jeong, Hawon and Park, ChaeHun and Hong, Jimin and Lee, Hojoon and Choo, Jaegul",
    booktitle = "Proceedings of the 8th BlackboxNLP Workshop: Analyzing and Interpreting Neural Networks for NLP",
    month = nov,
    year = "2025",
    address = "Suzhou, China",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2025.blackboxnlp-1.5/",
    doi = "10.18653/v1/2025.blackboxnlp-1.5",
    pages = "79--108"
}
```

---

## Reference 3: Acquiescence Bias / Central Tendency Bias 经典引用

- **状态: 存在，推荐两篇互补经典**

**推荐 A — Krosnick (1999)：survey response bias 的综述性权威引用**

覆盖 acquiescence bias、satisficing、response order effects、central tendency 等所有 rating scale bias，被引 5000+。

```bibtex
@article{krosnick1999survey,
  title={Survey Research},
  author={Krosnick, Jon A.},
  journal={Annual Review of Psychology},
  volume={50},
  number={1},
  pages={537--567},
  year={1999},
  doi={10.1146/annurev.psych.50.1.537},
  publisher={Annual Reviews}
}
```

**推荐 B — Paulhus (1991)：response bias measurement 的经典 chapter**

专门讨论 acquiescence、social desirability、extreme response style 的测量与控制，心理测量学标准引用。

```bibtex
@incollection{paulhus1991measurement,
  title={Measurement and Control of Response Bias},
  author={Paulhus, Delroy L.},
  booktitle={Measures of Personality and Social Psychological Attitudes},
  editor={Robinson, John P. and Shaver, Phillip R. and Wrightsman, Lawrence S.},
  pages={17--59},
  year={1991},
  publisher={Academic Press},
  address={San Diego, CA}
}
```

**建议：引 Krosnick (1999) 作为一站式引用最方便（一篇覆盖 acquiescence + central tendency + satisficing）。如果需要更专门讨论 response style 的分类学，补引 Paulhus (1991)。**

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_missing-refs_20260522T043517"
}
```

</details>

---
