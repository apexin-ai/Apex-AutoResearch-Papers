# paper research condorcet voting theory

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 37
- **Recorded user turns:** 0
- **Tool calls:** 18
- **Original source:** `logs/chats/worker_paper_research_condorcet_voting_theory_20260519T033450.jsonl`
- **Structured JSON:** [`dbf8e6f3f6d51e6bb99a.json`](../../sessions/db/dbf8e6f3f6d51e6bb99a.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

37 recorded events

### Tool call

_source line 1 · 2026-05-19T03:37:36.116637+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/literature_map.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_condorcet_voting_theory_20260519T033450",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/literature_map.yaml"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-19T03:37:36.117394+00:00_

1	# Literature Map — symb_invariant_consensus (SICA)
2	# Last updated: 2026-05-16
3	# Purpose: Track related work coverage for EMNLP 2026 submission
4	
5	dimensions:
6	
7	  self_consistency_and_variants:
8	    description: "Self-Consistency (SC) decoding and improvements"
9	    papers:
10	      - id: wang2023sc
11	        title: "Self-Consistency Improves Chain of Thought Reasoning in Language Models"
12	        authors: "Wang et al."
13	        venue: "ICLR 2023"
14	        arxiv: "2203.11171"
15	        relevance: "Foundational SC method; our primary baseline"
16	        status: must_cite
17	
18	      - id: chen2024usc
19	        title: "Universal Self-Consistency for Large Language Model Generation"
20	        authors: "Chen et al."
21	        venue: "ICML 2024"
22	        arxiv: "2311.17311"
23	        relevance: "Extends SC to free-form answers via LLM-based selection; alternative aggregation"
24	        status: must_cite
25	
26	      - id: taubenfeld2025cisc
27	        title: "Confidence Improves Self-Consistency in LLMs"
28	        authors: "Taubenfeld et al."
29	        venue: "ACL Findings 2025"
30	        arxiv: "2502.06233"
31	        relevance: "Weighted voting via model confidence; reduces samples 40-50%. Shows SC can be improved with non-uniform weighting — SICA uses constraint-based weighting instead"
32	        status: must_cite
33	
34	      - id: kim2026reasc
35	        title: "Reliability-Aware Adaptive Self-Consistency (ReASC)"
36	        authors: "Kim et al."
37	        venue: "2026"
38	        relevance: "Response-level confidence for early halting; 70-80% cost saving vs naive SC"
39	        status: should_cite
40	
41	      - id: loo2025reevaluating
42	        title: "Reevaluating Self-Consistency Scaling in Multi-Agent Systems"
43	        authors: "Loo et al."
44	        venue: "arXiv 2025"
45	        arxiv: "2511.00751"
46	        relevance: "CRITICAL — shows SC gains plateau early and can decline at high sample counts for strong models. Direc
…[truncated 19508 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_condorcet_voting_theory_20260519T033450",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-19T03:37:36.117644+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,WebFetch",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_condorcet_voting_theory_20260519T033450",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,WebFetch",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-19T03:37:36.117804+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_condorcet_voting_theory_20260519T033450",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-19T03:37:36.118167+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2409.00094",
  "prompt": "Extract the exact title, full author list, year, venue (if published at a conference/journal), and a detailed summary of what this paper does. Specifically: does it apply the Condorcet Jury Theorem to LLMs? Does it deal with cross-model ensembles or within-model self-consistency? What are its key contributions and findings?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_condorcet_voting_theory_20260519T033450",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2409.00094",
    "prompt": "Extract the exact title, full author list, year, venue (if published at a conference/journal), and a detailed summary of what this paper does. Specifically: does it apply the Condorcet Jury Theorem to LLMs? Does it deal with cross-model ensembles or within-model self-consistency? What are its key contributions and findings?"
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-19T03:37:36.118530+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Condorcet 1785 \"Essai sur l'application de l'analyse\" standard citation machine learning papers"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_condorcet_voting_theory_20260519T033450",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Condorcet 1785 \"Essai sur l'application de l'analyse\" standard citation machine learning papers"
  }
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-19T03:37:36.118705+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Austen-Smith Banks 1996 \"Information Aggregation Rationality Condorcet Jury Theorem\" American Political Science Review"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_condorcet_voting_theory_20260519T033450",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Austen-Smith Banks 1996 \"Information Aggregation Rationality Condorcet Jury Theorem\" American Political Science Review"
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-19T03:37:36.118869+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Condorcet jury theorem machine learning ensemble diversity correlated voters effective ensemble size"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_condorcet_voting_theory_20260519T033450",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Condorcet jury theorem machine learning ensemble diversity correlated voters effective ensemble size"
  }
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-19T03:37:36.119135+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Fleiss kappa inter-rater agreement machine learning ensemble reliability"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_condorcet_voting_theory_20260519T033450",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Fleiss kappa inter-rater agreement machine learning ensemble reliability"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-19T03:37:36.119343+00:00_

# Paper Summary

**Title:** "Examining Independence in Ensemble Sentiment Analysis: A Study on the Limits of Large Language Models Using the Condorcet Jury Theorem"

**Authors:** Baptiste Lefort, Eric Benhamou, Jean-Jacques Ohana, Beatrice Guez, David Saltiel, Thomas Jacquot

**Year:** 2024 (submitted August 26, 2024)

**Venue:** Not published at a conference/journal (preprint on arXiv, cs.CL category)

## Key Details

**Does it apply Condorcet Jury Theorem to LLMs?** Yes. The research directly applies this classical theorem, which predicts that majority voting improves accuracy when individual classifiers make independent decisions.

**Ensemble Type:** Cross-model ensembles. The study tests majority voting across different model architectures, including advanced LLMs like ChatGPT-4 and simpler NLP baselines.

**Main Contributions & Findings:**

The authors empirically investigate whether ensemble voting strategies enhance sentiment analysis performance. Their central finding contradicts the theoretical expectation: when combining diverse LLMs through majority voting, they observe only "marginal improvements in performance." They conclude this demonstrates a "lack of independence among" advanced language models. The research suggests that despite greater complexity, LLMs don't substantially outperform simpler models for sentiment reasoning tasks, revealing "practical limits of model independence" in advanced NLP applications.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_condorcet_voting_theory_20260519T033450",
  "tool": "WebFetch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-19T03:37:36.119541+00:00_

Web search results for query: "Condorcet 1785 "Essai sur l'application de l'analyse" standard citation machine learning papers"

Links: [{"title":"Condorcet, Marie Jean Antoine Nicolas Caritat, Marquis de (1743–1794) | Springer Nature Link","url":"https://link.springer.com/rwe/10.1057/978-1-349-95189-5_248"},{"title":"Essai sur l'application de l'analyse à la probabilité des décisions rendues à la pluralité des voix (Book, 1785) [WorldCat.org]","url":"https://www.worldcat.org/title/essai-sur-lapplication-de-lanalyse-a-la-probabilite-des-decisions-rendues-a-la-pluralite-des-voix/oclc/1429244"},{"title":"Essai sur l'application de l'analyse à la probabilité des décisions rendues à la pluralité des voix","url":"https://www.researchgate.net/publication/364839190_Essai_sur_l'application_de_l'analyse_a_la_probabilite_des_decisions_rendues_a_la_pluralite_des_voix"},{"title":"Essai sur l'application de l'analyse à la probabilité des décisions rendues à la pluralité des voix ([Reprod.]) / par M. le marquis de Condorcet,... | Gallica","url":"https://gallica.bnf.fr/ark:/12148/bpt6k417181.image"},{"title":"Essai sur l'application de l'analyse à la probabilité des décisions rendues à la pluralité des voix . Par M. le marquis de Condorcet,... | Gallica","url":"https://gallica.bnf.fr/ark:/12148/bpt6k1057808s"},{"title":"Essai sur l'application de l'analyse à la probabilité des décisions rendues ... - Jean-Antoine-Nicolas de Caritat marquis de Condorcet - Google Books","url":"https://books.google.com/books/about/Essai_sur_l_application_de_l_analyse_%C3%A0.html?id=_mFbAAAAcAAJ"},{"title":"Essai sur l'application de l'analyse à la probabilité des décisions rendues à la pluralité des voix","url":"https://www.cambridge.org/core/books/essai-sur-lapplication-de-lanalyse-a-la-probabilite-des-decisions-rendues-a-la-pluralite-des-voix/1D38B9E4EAFF9AFC42313B19DC8C8070"},{"title":"Essai sur l'application de l'analyse à la probabilité des décisions rendues à la pluralité des voix : C
…[truncated 2063 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_condorcet_voting_theory_20260519T033450",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-19T03:37:36.119763+00:00_

Web search results for query: "Austen-Smith Banks 1996 "Information Aggregation Rationality Condorcet Jury Theorem" American Political Science Review"

Links: [{"title":"Information Aggregation, Rationality and the Condorcet Jury Theorem | Kellogg School of Management","url":"https://www.kellogg.northwestern.edu/academics-research/research/detail/1996/information-aggregation-rationality-and-the-condorcet-jury-theorem/"},{"title":"Information Aggregation, Rationality, and the Condorcet Jury Theorem","url":"http://econdse.org/wp-content/uploads/2013/03/jury-austensmith.pdf"},{"title":"Information Aggregation, Rationality, and the Condorcet Jury Theorem","url":"https://ideas.repec.org/a/cup/apsrev/v90y1996i01p34-45_20.html"},{"title":"[PDF] Information Aggregation, Rationality, and the Condorcet Jury Theorem | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Information-Aggregation,-Rationality,-and-the-Jury-Austen-Smith-Banks/c4914af1fb00d786be04da0a97d1245faebda4cb"},{"title":"Consequences of the Condorcet Jury Theorem for Beneficial Information Aggregation by Rational Agents | American Political Science Review | Cambridge Core","url":"https://www.cambridge.org/core/journals/american-political-science-review/article/abs/consequences-of-the-condorcet-jury-theorem-for-beneficial-information-aggregation-by-rational-agents/AB1FA7F59F68A84302A34E294EEC71BD"},{"title":"Information Aggregation, Rationality, and the Condorcet Jury Theorem","url":"https://authors.library.caltech.edu/records/j7tn8-0pj80"},{"title":"Information Aggregation, Rationality, and the Condorcet Jury Theorem | American Political Science Review | Cambridge Core","url":"https://www.cambridge.org/core/journals/american-political-science-review/article/abs/information-aggregation-rationality-and-the-condorcet-jury-theorem/26AF80760F07CCB9E1E4F604C6811CF6"},{"title":"EconPapers: Information Aggregation, Rationality, and the Condorcet Jury Theorem","url":"https://econpapers.repec.org/RePEc:cup:
…[truncated 1016 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_condorcet_voting_theory_20260519T033450",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-19T03:37:36.120087+00:00_

Web search results for query: "Fleiss kappa inter-rater agreement machine learning ensemble reliability"

Links: [{"title":"Fleiss' Kappa Inter-Rater Reliability Calculator","url":"https://metricgate.com/docs/fleiss-kappa/"},{"title":"Fleiss' Kappa: Measuring Agreement Among Multiple Raters","url":"https://numiqo.com/tutorial/fleiss-kappa"},{"title":"Inter-Annotator Agreement: Building Datasets | Keymakr","url":"https://keymakr.com/blog/measuring-inter-annotator-agreement-building-trustworthy-datasets/"},{"title":"Fleiss's kappa - Wikipedia","url":"https://en.wikipedia.org/wiki/Fleiss%27s_kappa"},{"title":"Enhancing Answer Reliability Through Inter-Model Consensus of Large Language Models | SpringerLink","url":"https://link.springer.com/chapter/10.1007/978-3-031-96235-6_22"},{"title":"Measuring agreement among several raters classifying subjects into one or more (hierarchical) categories: A generalization of Fleiss' kappa","url":"https://arxiv.org/pdf/2303.12502"},{"title":"Fleiss' Kappa - Statistics How To","url":"https://www.statisticshowto.com/fleiss-kappa/"},{"title":"Inter-Rater: Software for analysis of inter-rater reliability by   permutating pairs of multiple users","url":"https://arxiv.org/pdf/1809.05731"},{"title":"Measuring agreement among several raters classifying subjects into one or more (hierarchical) categories: A generalization of Fleiss’ kappa","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12436533/"}]

Based on the search results, here's what I found about Fleiss' kappa, inter-rater agreement, machine learning, ensemble methods, and reliability:

## Fleiss' Kappa Overview

Fleiss' kappa is the standard nonparametric measure of inter-rater reliability when three or more raters independently classify a set of subjects into mutually exclusive nominal categories. Kappa equals 1 for perfect agreement, 0 for chance-level agreement, and negative values for systematic disagreement below chance.

## Applications in Machine Learning

Fleiss' kappa is
…[truncated 1020 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_condorcet_voting_theory_20260519T033450",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-19T03:37:36.120548+00:00_

Web search results for query: "Condorcet jury theorem machine learning ensemble diversity correlated voters effective ensemble size"

Links: [{"title":"Harnessing the Crowd: Condorcet’s Jury Theorem from Political Science to Ensemble Learning in AI | by Nkugwa Mark William | Jun, 2024 | Medium","url":"https://medium.com/@nkugwamarkwilliam/harnessing-the-crowd-condorcets-jury-theorem-from-political-science-to-ensemble-learning-in-ai-85f27f1db913"},{"title":"arXiv:1604.07711v2 [stat.ML] 10 Oct 2016 Condorcet’s Jury Theorem for","url":"https://arxiv.org/pdf/1604.07711"},{"title":"MAJORITY VOTING AND THE CONDORCET’S JURY THEOREM A PREPRINT","url":"https://arxiv.org/pdf/2002.03153"},{"title":"Condorcet's jury theorem - Wikipedia","url":"https://en.wikipedia.org/wiki/Condorcet's_jury_theorem"},{"title":"Confidence-Credibility Aware Weighted Ensembles of Small","url":"https://arxiv.org/pdf/2512.17630"},{"title":"Re-Interpreting The Condorcet Jury Theorem (DRAFT) Lu Hong","url":"https://www.law.nyu.edu/sites/default/files/upload_documents/Re-Interpreting%20the%20Condorcet%20Jury%20Theorem.pdf"},{"title":"[2002.03153] Majority Voting and the Condorcet's Jury Theorem","url":"https://arxiv.org/abs/2002.03153"}]

The search results provide valuable information about Condorcet's Jury Theorem in the context of machine learning ensemble learning. Here are the key findings:

## Core Concept

Condorcet's Jury Theorem states that a majority of independent individuals who make correct decisions with probability p > 1/2 are more likely to choose correctly than each individual. In ensemble methods, predictions from many individual classifiers are combined by majority voting, and assuming each classifier predicts with slightly greater than 50% accuracy and their predictions are independent, the ensemble's predictions will be far greater than individual predictive scores.

## Key Pillars for Ensemble Effectiveness

Three key pillars—diversity, independence, and accuracy—form the bedrock o
…[truncated 1173 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_condorcet_voting_theory_20260519T033450",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-19T03:37:36.120757+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/1604.07711",
  "prompt": "Extract the exact title, full author list, year, venue, and a summary of what this paper does. Does it relate Condorcet's Jury Theorem to machine learning ensembles? Does it discuss correlated voters, effective ensemble size, or voter independence?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_condorcet_voting_theory_20260519T033450",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/1604.07711",
    "prompt": "Extract the exact title, full author list, year, venue, and a summary of what this paper does. Does it relate Condorcet's Jury Theorem to machine learning ensembles? Does it discuss correlated voters, effective ensemble size, or voter independence?"
  }
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-19T03:37:36.120913+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2002.03153",
  "prompt": "Extract the exact title, full author list, year, venue if published, and a summary. Does it discuss Condorcet Jury Theorem in the context of ML classifiers? Does it address the independence assumption, correlated voters, or effective ensemble size?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_condorcet_voting_theory_20260519T033450",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2002.03153",
    "prompt": "Extract the exact title, full author list, year, venue if published, and a summary. Does it discuss Condorcet Jury Theorem in the context of ML classifiers? Does it address the independence assumption, correlated voters, or effective ensemble size?"
  }
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-19T03:37:36.121053+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"effective ensemble size\" correlated classifiers independence voting machine learning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_condorcet_voting_theory_20260519T033450",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"effective ensemble size\" correlated classifiers independence voting machine learning"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-19T03:37:36.121250+00:00_

# Paper Summary

**Title:** "Majority Voting and the Condorcet's Jury Theorem"

**Authors:** Hanan Shteingart, Eran Marom, Igor Itkin, Gil Shabat, Michael Kolomenkin, Moshe Salhov, Liran Katzir

**Year:** 2020 (submitted February 8, 2020)

**Venue:** Not published in a journal (arXiv preprint: 2002.03153)

## Summary

The authors establish a connection between Condorcet's jury theorem from 1785 and modern "Strength of Weak Learnability" in machine learning. They provide "a more publicly available simple derivation" of the theorem for pedagogical purposes in ML courses, aiming to explain ensemble learning motivation.

## Key Questions Addressed

**Does it discuss Condorcet Jury Theorem in the context of ML classifiers?**
Yes. The abstract explicitly connects the theorem to ensemble learning and weak learner conversion.

**Does it address the independence assumption?**
Partially. The abstract mentions votes being "often correct and independent," but the provided content does not elaborate on how the paper handles or examines this assumption.

**Does it address correlated voters or effective ensemble size?**
Not evident from the available content. These topics are not mentioned in the abstract or metadata provided.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_condorcet_voting_theory_20260519T033450",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-19T03:37:36.121634+00:00_

# Paper Analysis

**Exact Title:** "Condorcet's Jury Theorem for Consensus Clustering and its Implications for Diversity"

**Full Author List:** Brijnesh J. Jain

**Year:** 2016 (submitted April 26, 2016; revised October 10, 2016)

**Venue:** arXiv:1604.07711 [stat.ML] (Statistics > Machine Learning)

## Summary

This work extends Condorcet's Jury Theorem from ensemble classifiers to consensus clustering. The author establishes theoretical conditions under which combining multiple clustering partitions can outperform individual partitions, requiring assumptions that a ground-truth partition exists and sample partitions remain within a constrained neighborhood of that truth.

## Relationship to Machine Learning Ensembles

Yes, the paper explicitly addresses ensemble methods. It notes that Condorcet's Jury Theorem "has been invoked for ensemble classifiers to indicate that the combination of many classifiers can have better predictive performance than a single classifier," extending this principle to clustering ensembles.

## Discussion of Specific Topics

The paper does **not** discuss correlated voters, effective ensemble size, or voter independence based on the abstract provided. Instead, it challenges conventional wisdom about diversity, conjecturing that "limiting the diversity of the mean partitions is necessary for controlling the quality" rather than maximizing diversity among component partitions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_condorcet_voting_theory_20260519T033450",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-19T03:37:36.121908+00:00_

Web search results for query: ""effective ensemble size" correlated classifiers independence voting machine learning"

Links: [{"title":"Ensemble Performance Through the Lens of Linear Independence of Classifier Votes in Data Streams","url":"https://arxiv.org/html/2511.21465v1"},{"title":"Ensemble Performance Through the Lens of Linear Independence of Classifier Votes in Data Streams","url":"https://arxiv.org/pdf/2511.21465"},{"title":"[2511.21465] Ensemble Performance Through the Lens of Linear Independence of Classifier Votes in Data Streams","url":"https://arxiv.org/abs/2511.21465"},{"title":"Leveraging Linear Independence of Component Classifiers: Optimizing Size   and Prediction Accuracy for Online Ensembles","url":"https://arxiv.org/pdf/2308.14175"},{"title":"Ensemble Learning Explained: How Voting Classifiers Boost Machine Learning Accuracy - Machine Learning Site","url":"https://machinelearningsite.com/ensemble-learning-machine-learning/"}]

I found relevant research on this topic. Here are the key findings:

## Ensemble Size and Linear Independence

A theoretical framework explains the trade-off between ensemble size and performance by modeling the linear independence of classifier vote vectors. Achieving a set of m linearly independent votes is a necessary condition for an ensemble's representational capacity, and a probabilistic model determines the ensemble size required to meet this condition with a specified confidence level.

## Effective Size and Performance Saturation

While increasing the number of classifiers generally enhances accuracy, excessively large ensembles can lead to computational inefficiency and diminishing returns, and the relationship between ensemble size and performance can be investigated through the lens of linear independence among classifier votes.

There is a strong correlation between the Probability of Linear Independence (PLI) and accuracy, and this method can effectively identify the point of diminishing returns for majori
…[truncated 754 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_condorcet_voting_theory_20260519T033450",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-19T03:37:36.122197+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Ladha 1992 \"Condorcet jury theorem\" correlated voters"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_condorcet_voting_theory_20260519T033450",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Ladha 1992 \"Condorcet jury theorem\" correlated voters"
  }
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-19T03:37:36.122395+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2511.21465",
  "prompt": "Extract the exact title, full author list, year, venue if published, and summary. Does it discuss effective ensemble size, how correlated classifiers reduce ensemble gains, or independence among voters/classifiers? What are the key findings?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_condorcet_voting_theory_20260519T033450",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2511.21465",
    "prompt": "Extract the exact title, full author list, year, venue if published, and summary. Does it discuss effective ensemble size, how correlated classifiers reduce ensemble gains, or independence among voters/classifiers? What are the key findings?"
  }
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-19T03:37:36.122586+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Fleiss 1971 \"Measuring nominal scale agreement among many raters\" original paper citation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_condorcet_voting_theory_20260519T033450",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Fleiss 1971 \"Measuring nominal scale agreement among many raters\" original paper citation"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-19T03:37:36.122816+00:00_

Web search results for query: "Ladha 1992 "Condorcet jury theorem" correlated voters"

Links: [{"title":"Aggregation of Correlated Votes and Condorcet’s Jury Theorem Serguei Kaniovski∗","url":"https://serguei.kaniovski.wifo.ac.at/fileadmin/pdf/condorcet.pdf"},{"title":"The Condorcet jury theorem and extension of the franchise with rationally ignorant voters | Public Choice | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s11127-010-9663-0"},{"title":"Condorcet's jury theorem in light of de Finetti's theorem | Social Choice and Welfare | Springer Nature Link","url":"https://link.springer.com/content/pdf/10.1007/BF00187434.pdf"},{"title":"(PDF) When is Condorcet's Jury Theorem valid?","url":"https://www.researchgate.net/publication/24064212_When_is_Condorcet's_Jury_Theorem_valid"},{"title":"Aggregation of correlated votes and Condorcet’s Jury Theorem | Theory and Decision","url":"https://link.springer.com/article/10.1007/s11238-008-9120-4"},{"title":"Political Discourse, Factions, and the General Will: Correlated Voting and Condorcet’s Jury Theorem | SpringerLink","url":"https://link.springer.com/chapter/10.1007/978-94-015-8767-9_19"},{"title":"On Optimal Voting Rules with Homogeneous Preferences∗ Arnaud Costinot†","url":"https://economics.mit.edu/sites/default/files/publications/jurydesign_20090113b.pdf"},{"title":"Optimal jury design for homogeneous juries with correlated votes | Theory and Decision | Springer Nature Link","url":"https://link.springer.com/content/pdf/10.1007/s11238-009-9170-2.pdf?pdf=preview"},{"title":"Information pooling through majority-rule voting: Condorcet's jury theorem with correlated votes - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/016726819400068P"},{"title":"The Condorcet Jury Theorem, Free Speech and Correlated Votes - Krisha K. Ladha - Google Books","url":"https://books.google.com/books/about/The_Condorcet_Jury_Theorem_Free_Speech_a.html?id=_iU4GwAACAAJ"}]

Based on the search r
…[truncated 1094 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_condorcet_voting_theory_20260519T033450",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-19T03:37:36.123114+00:00_

# Paper Summary

**Title:** "Ensemble Performance Through the Lens of Linear Independence of Classifier Votes in Data Streams"

**Authors:** Enes Bektas, Fazli Can

**Year:** 2025 (submitted November 26, 2025)

**Venue:** Not yet published; arXiv preprint (cs.LG)

## Key Content

This paper directly addresses ensemble size effectiveness and classifier independence. The researchers propose that "ensembles composed of linearly independent classifiers maximize representational capacity" and develop a theoretical framework linking ensemble diversity to performance saturation.

**Key Findings:**

- The study investigates how increasing ensemble size affects accuracy, establishing that diversity among voter predictions is crucial for performance gains
- The authors derive a mathematical estimate for optimal ensemble size based on achieving a specified probability of linear independence among classifier outputs
- Their experiments validate this theory using OzaBagging and GOOWE ensemble methods on real and synthetic datasets
- For robust methods like OzaBagging, their theoretical estimates effectively identify where performance stabilizes
- Interestingly, for complex weighting schemes like GOOWE, excessive diversity can cause algorithmic instability

The paper directly addresses the trade-off between ensemble size and returns, concluding that understanding linear independence among classifier votes provides insight into when additional classifiers cease providing meaningful performance improvements.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_condorcet_voting_theory_20260519T033450",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-19T03:37:36.123371+00:00_

Web search results for query: "Fleiss 1971 "Measuring nominal scale agreement among many raters" original paper citation"

Links: [{"title":"Fleiss, J. L. (1971). Measuring Nominal Scale Agreement among Many Raters. Psychological Bulletin, 76, 378-382. - References - Scientific Research Publishing","url":"https://www.scirp.org/reference/referencespapers?referenceid=1733370"},{"title":"Fleiss, J.L. (1971) Measuring nominal scale agreement among many raters. Psychological Bulletin, 76, 378-382. doi10.1037/h0031619 - References - Scientific Research Publishing","url":"https://www.scirp.org/reference/referencespapers?referenceid=853322"},{"title":"Measuring nominal scale agreement among many raters","url":"https://www.ovid.com/journals/plbul/pdf/00006823-197111000-00006~measuring-nominal-scale-agreement-among-many-raters"},{"title":"Measuring nominal scale agreement among many raters | BibSonomy","url":"https://www.bibsonomy.org/bibtex/2506a1115df044659165a488a75f9e449/folke"},{"title":"Measuring nominal scale agreement among many raters. | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Measuring-nominal-scale-agreement-among-many-Fleiss/cfb4592221080deb127de94e8063fb403b13a298"},{"title":"Measuring nominal scale agreement among many raters","url":"https://www.researchgate.net/publication/200086110_Measuring_nominal_scale_agreement_among_many_raters"},{"title":"GitHub - Shamya/FleissKappa: Implementation of Fleiss' Kappa (Joseph L. Fleiss, Measuring Nominal Scale Agreement Among Many Raters, 1971.)","url":"https://github.com/Shamya/FleissKappa"},{"title":"Measuring nominal scale agreement among many raters","url":"https://www.proquest.com/docview/614289059"},{"title":"Measuring agreement among several raters classifying subjects into one or more (hierarchical) categories: A generalization of Fleiss' kappa","url":"https://arxiv.org/pdf/2303.12502"},{"title":"Measuring inter-rater reliability for nominal data – which coefficients and confidence intervals a
…[truncated 670 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_condorcet_voting_theory_20260519T033450",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-19T03:37:36.123678+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://www.semanticscholar.org/paper/The-Condorcet-jury-theorem-free-speech-and-Ladha/3e8c0485f3a8ad7eae1d39b940b4fc0f1989bf3c",
  "prompt": "Verify: Is this \"The Condorcet Jury Theorem, Free Speech, and Correlated Votes\" by Krishna K. Ladha, published in American Journal of Political Science, 1992, volume 36, pages 617-634? Give the exact title, author, year, venue, volume, pages."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_condorcet_voting_theory_20260519T033450",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://www.semanticscholar.org/paper/The-Condorcet-jury-theorem-free-speech-and-Ladha/3e8c0485f3a8ad7eae1d39b940b4fc0f1989bf3c",
    "prompt": "Verify: Is this \"The Condorcet Jury Theorem, Free Speech, and Correlated Votes\" by Krishna K. Ladha, published in American Journal of Political Science, 1992, volume 36, pages 617-634? Give the exact title, author, year, venue, volume, pages."
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-19T03:37:36.123909+00:00_

I cannot verify the publication details you've provided because the web page content provided is empty (showing only dashes with no actual text). Without the actual content of the web page, I'm unable to confirm whether it contains the article "The Condorcet Jury Theorem, Free Speech, and Correlated Votes" by Krishna K. Ladha or verify any of the bibliographic information you mentioned.

To complete this verification, please share the actual web page content.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_condorcet_voting_theory_20260519T033450",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-19T03:37:36.124101+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Ladha 1992 \"Condorcet jury theorem free speech correlated votes\" American Journal Political Science volume pages"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_condorcet_voting_theory_20260519T033450",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Ladha 1992 \"Condorcet jury theorem free speech correlated votes\" American Journal Political Science volume pages"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-19T03:37:36.124318+00:00_

Web search results for query: "Ladha 1992 "Condorcet jury theorem free speech correlated votes" American Journal Political Science volume pages"

Links: [{"title":"Aggregation of Correlated Votes and Condorcet’s Jury Theorem Serguei Kaniovski∗","url":"https://serguei.kaniovski.wifo.ac.at/fileadmin/pdf/condorcet.pdf"},{"title":"Convicting the Innocent: The Inferiority of Unanimous Jury Verdicts under Strategic Voting | American Political Science Review | Cambridge Core","url":"https://www.cambridge.org/core/journals/american-political-science-review/article/abs/convicting-the-innocent-the-inferiority-of-unanimous-jury-verdicts-under-strategic-voting/2464A10255F23A692DFDC6B92E46E1A9"},{"title":"In Defense of Unanimous Jury Verdicts: Mistrials, Communication, and Strategic Voting | American Political Science Review | Cambridge Core","url":"https://www.cambridge.org/core/journals/american-political-science-review/article/abs/in-defense-of-unanimous-jury-verdicts-mistrials-communication-and-strategic-voting/A16FEAC6592A686C5805AF2ADB5EC57B"},{"title":"Information, individual errors, and collective performance: Empirical evidence on the Condorcet Jury Theorem | Group Decision and Negotiation | Springer Nature Link","url":"https://link.springer.com/article/10.1007/PL00020686"},{"title":"Information Aggregation, Rationality, and the Condorcet Jury Theorem | American Political Science Review | Cambridge Core","url":"https://www.cambridge.org/core/journals/american-political-science-review/article/abs/information-aggregation-rationality-and-the-condorcet-jury-theorem/26AF80760F07CCB9E1E4F604C6811CF6"},{"title":"Consequences of the Condorcet Jury Theorem for Beneficial Information Aggregation by Rational Agents | American Political Science Review | Cambridge Core","url":"https://www.cambridge.org/core/journals/american-political-science-review/article/abs/consequences-of-the-condorcet-jury-theorem-for-beneficial-information-aggregation-by-rational-agents/AB1FA7F59F68A84302A34E
…[truncated 1136 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_condorcet_voting_theory_20260519T033450",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-19T03:37:36.124612+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/literature_map.yaml",
  "old_string": "gaps:\n  resolved:",
  "new_string": "  condorcet_voting_theory:\n    description: \"Condorcet Jury Theorem, voting theory, and ensemble independence\"\n    papers:\n      - id: condorcet1785\n        title: \"Essai sur l'application de l'analyse à la probabilité des décisions rendues à la pluralité des voix\"\n        authors: \"Marquis de Condorcet\"\n        venue: \"Paris: Imprimerie Royale, 1785\"\n        relevance: \"The original Jury Theorem: majority voting among independent voters each with p>0.5 converges to correct answer as group size grows. Foundation for our theoretical framing of SC as majority voting over reasoning traces\"\n        status: must_cite\n        verified: true\n\n      - id: austensmith1996\n        title: \"Information Aggregation, Rationality, and the Condorcet Jury Theorem\"\n        authors: \"Austen-Smith, David and Banks, Jeffrey S.\"\n        venue: \"American Political Science Review, 90(1), 34-45, 1996\"\n        relevance: \"Key modern formalization of CJT; explicitly introduces the independence requirement and shows sincere voting is not always rational. Provides the formal basis for why trace independence matters in SC aggregation\"\n        status: must_cite\n        verified: true\n\n      - id: lefort2024condorcet_llm\n        title: \"Examining Independence in Ensemble Sentiment Analysis: A Study on the Limits of Large Language Models Using the Condorcet Jury Theorem\"\n        authors: \"Lefort, Baptiste and Benhamou, Eric and Ohana, Jean-Jacques and Guez, Beatrice and Saltiel, David and Jacquot, Thomas\"\n        venue: \"arXiv 2024\"\n        arxiv: \"2409.00094\"\n        relevance: \"CLOSEST PRIOR WORK applying CJT to LLM aggregation. Tests cross-model ensembles via majority voting; finds marginal gains due to lack of independence among advanced LLMs. Key difference from SICA: they study cross-model ensembles, we study within-model trace independence and propose Fleiss' kappa + Effective-K to quantify it\"\n        status: must_cite\n        verified: true\n\n      - id: ladha1992correlated\n        title: \"The Condorcet Jury Theorem, Free Speech, and Correlated Votes\"\n        authors: \"Ladha, Krishna K.\"\n        venue: \"American Journal of Political Science, 36(3), 617-634, 1992\"\n        relevance: \"Generalizes CJT to correlated voters; shows majority-rule effectiveness decreases as vote correlation increases. Directly supports our Effective-K concept: correlated traces reduce the effective number of independent voters below nominal K\"\n        status: should_cite\n        verified: true\n\n      - id: fleiss1971kappa\n        title: \"Measuring Nominal Scale Agreement among Many Raters\"\n        authors: \"Fleiss, Joseph L.\"\n        venue: \"Psychological Bulletin, 76(5), 378-382, 1971\"\n        relevance: \"Defines Fleiss' kappa for multi-rater agreement on nominal categories. Our framework uses Fleiss' kappa to quantify inter-trace agreement as a proxy for trace independence in SC sampling\"\n        status: should_cite\n        verified: true\n\ngaps:\n  resolved:"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_condorcet_voting_theory_20260519T033450",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/literature_map.yaml",
    "old_string": "gaps:\n  resolved:",
    "new_string": "  condorcet_voting_theory:\n    description: \"Condorcet Jury Theorem, voting theory, and ensemble independence\"\n    papers:\n      - id: condorcet1785\n        title: \"Essai sur l'application de l'analyse à la probabilité des décisions rendues à la pluralité des voix\"\n        authors: \"Marquis de Condorcet\"\n        venue: \"Paris: Imprimerie Royale, 1785\"\n        relevance: \"The original Jury Theorem: majority voting among independent voters each with p>0.5 converges to correct answer as group size grows. Foundation for our theoretical framing of SC as majority voting over reasoning traces\"\n        status: must_cite\n        verified: true\n\n      - id: austensmith1996\n        title: \"Information Aggregation, Rationality, and the Condorcet Jury Theorem\"\n        authors: \"Austen-Smith, David and Banks, Jeffrey S.\"\n        venue: \"American Political Science Review, 90(1), 34-45, 1996\"\n        relevance: \"Key modern formalization of CJT; explicitly introduces the independence requirement and shows sincere voting is not always rational. Provides the formal basis for why trace independence matters in SC aggregation\"\n        status: must_cite\n        verified: true\n\n      - id: lefort2024condorcet_llm\n        title: \"Examining Independence in Ensemble Sentiment Analysis: A Study on the Limits of Large Language Models Using the Condorcet Jury Theorem\"\n        authors: \"Lefort, Baptiste and Benhamou, Eric and Ohana, Jean-Jacques and Guez, Beatrice and Saltiel, David and Jacquot, Thomas\"\n        venue: \"arXiv 2024\"\n        arxiv: \"2409.00094\"\n        relevance: \"CLOSEST PRIOR WORK applying CJT to LLM aggregation. Tests cross-model ensembles via majority voting; finds marginal gains due to lack of independence among advanced LLMs. Key difference from SICA: they study cross-model ensembles, we study within-model trace independence and propose Fleiss' kappa + Effective-K to quantify it\"\n        status: must_cite\n        verified: true\n\n      - id: ladha1992correlated\n        title: \"The Condorcet Jury Theorem, Free Speech, and Correlated Votes\"\n        authors: \"Ladha, Krishna K.\"\n        venue: \"American Journal of Political Science, 36(3), 617-634, 1992\"\n        relevance: \"Generalizes CJT to correlated voters; shows majority-rule effectiveness decreases as vote correlation increases. Directly supports our Effective-K concept: correlated traces reduce the effective number of independent voters below nominal K\"\n        status: should_cite\n        verified: true\n\n      - id: fleiss1971kappa\n        title: \"Measuring Nominal Scale Agreement among Many Raters\"\n        authors: \"Fleiss, Joseph L.\"\n        venue: \"Psychological Bulletin, 76(5), 378-382, 1971\"\n        relevance: \"Defines Fleiss' kappa for multi-rater agreement on nominal categories. Our framework uses Fleiss' kappa to quantify inter-trace agreement as a proxy for trace independence in SC sampling\"\n        status: should_cite\n        verified: true\n\ngaps:\n  resolved:"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-19T03:37:36.124852+00:00_

&lt;tool_use_error>File has been modified since read, either by the user or by a linter. Read it again before attempting to write it.&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_condorcet_voting_theory_20260519T033450",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-19T03:37:36.125080+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/literature_map.yaml",
  "offset": "410"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_condorcet_voting_theory_20260519T033450",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/literature_map.yaml",
    "offset": "410"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-19T03:37:36.125304+00:00_

410	
411	      - id: trivedi2023ircot
412	        title: "Interleaving Retrieval with Chain-of-Thought Reasoning for Knowledge-Intensive Multi-Step Questions"
413	        authors: "Trivedi et al."
414	        venue: "ACL 2023"
415	        arxiv: "2212.10509"
416	        relevance: "Uses gold supporting paragraphs as oracle retrieval upper bound to diagnose that retrieval quality is the primary bottleneck in multi-step QA. Same diagnostic design as our oracle experiment: replace one pipeline component with gold data to isolate the bottleneck."
417	        status: should_cite
418	        verified: true
419	
420	      - id: saparov2023greedy
421	        title: "Language Models Are Greedy Reasoners: A Systematic Formal Analysis of Chain-of-Thought"
422	        authors: "Saparov and He"
423	        venue: "ICLR 2023"
424	        arxiv: "2210.01240"
425	        relevance: "Uses synthetic data with gold FOL proofs to formally analyze where CoT reasoning fails. Isolates proof planning (not individual deduction) as bottleneck. Closest methodological parallel: uses formal logic ground truth to diagnose LLM reasoning limitations."
426	        status: should_cite
427	        verified: true
428	
429	gaps:
430	  resolved:
431	    - dimension: "verification_reranking"
432	      gap: "Added ORM, PRM, Math-Shepherd, V-STaR (2026-05-17)"
433	    - dimension: "debate_multi_agent"
434	      gap: "Added Liang 2023, Du 2023, Khan 2024 (2026-05-17)"
435	    - dimension: "benchmarks_and_datasets"
436	      gap: "Added FOLIO, ProofWriter, StrategyQA, ARC (2026-05-17)"
437	    - dimension: "negative_results_analysis"
438	      gap: "Added Huang 2024 (self-correct), Mirzadeh 2024 (GSM-Symbolic) (2026-05-17)"
439	    - dimension: "symbolic_reasoning_llm"
440	      gap: "Added LINC (Olausson et al. 2023) (2026-05-17)"
441	    - dimension: "self_consistency_and_variants"
442	      gap: "Added DiVeRSe (Li et al. 2023) (2026-05-17)"
443	    - dimension: "oracle_upper_bound_experiments"
444	      g
…[truncated 160 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_condorcet_voting_theory_20260519T033450",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-19T03:37:36.125540+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/literature_map.yaml",
  "old_string": "gaps:\n  resolved:\n    - dimension: \"verification_reranking\"\n      gap: \"Added ORM, PRM, Math-Shepherd, V-STaR (2026-05-17)\"\n    - dimension: \"debate_multi_agent\"\n      gap: \"Added Liang 2023, Du 2023, Khan 2024 (2026-05-17)\"\n    - dimension: \"benchmarks_and_datasets\"\n      gap: \"Added FOLIO, ProofWriter, StrategyQA, ARC (2026-05-17)\"\n    - dimension: \"negative_results_analysis\"\n      gap: \"Added Huang 2024 (self-correct), Mirzadeh 2024 (GSM-Symbolic) (2026-05-17)\"\n    - dimension: \"symbolic_reasoning_llm\"\n      gap: \"Added LINC (Olausson et al. 2023) (2026-05-17)\"\n    - dimension: \"self_consistency_and_variants\"\n      gap: \"Added DiVeRSe (Li et al. 2023) (2026-05-17)\"\n    - dimension: \"oracle_upper_bound_experiments\"\n      gap: \"Added Press 2023 (compositionality gap), Trivedi 2023 (IRCoT oracle retrieval), Saparov & He 2023 (greedy reasoners) (2026-05-17)\"\n  remaining: []",
  "new_string": "  condorcet_voting_theory:\n    description: \"Condorcet Jury Theorem, voting theory, and ensemble independence\"\n    papers:\n      - id: condorcet1785\n        title: \"Essai sur l'application de l'analyse à la probabilité des décisions rendues à la pluralité des voix\"\n        authors: \"Marquis de Condorcet\"\n        venue: \"Paris: Imprimerie Royale, 1785\"\n        relevance: \"The original Jury Theorem: majority voting among independent voters each with p>0.5 converges to correct answer as group size grows. Foundation for our theoretical framing of SC as majority voting over reasoning traces\"\n        status: must_cite\n        verified: true\n\n      - id: austensmith1996\n        title: \"Information Aggregation, Rationality, and the Condorcet Jury Theorem\"\n        authors: \"Austen-Smith, David and Banks, Jeffrey S.\"\n        venue: \"American Political Science Review, 90(1), 34-45, 1996\"\n        relevance: \"Key modern formalization of CJT; explicitly introduces the independence requirement and shows sincere voting is not always rational. Provides the formal basis for why trace independence matters in SC aggregation\"\n        status: must_cite\n        verified: true\n\n      - id: lefort2024condorcet_llm\n        title: \"Examining Independence in Ensemble Sentiment Analysis: A Study on the Limits of Large Language Models Using the Condorcet Jury Theorem\"\n        authors: \"Lefort, Baptiste and Benhamou, Eric and Ohana, Jean-Jacques and Guez, Beatrice and Saltiel, David and Jacquot, Thomas\"\n        venue: \"arXiv 2024\"\n        arxiv: \"2409.00094\"\n        relevance: \"CLOSEST PRIOR WORK applying CJT to LLM aggregation. Tests cross-model ensembles via majority voting for sentiment analysis; finds marginal gains due to lack of independence among advanced LLMs. Key difference from SICA: they study cross-model ensembles, we study within-model trace independence and propose Fleiss kappa + Effective-K to quantify it\"\n        status: must_cite\n        verified: true\n\n      - id: ladha1992correlated\n        title: \"The Condorcet Jury Theorem, Free Speech, and Correlated Votes\"\n        authors: \"Ladha, Krishna K.\"\n        venue: \"American Journal of Political Science, 36(3), 617-634, 1992\"\n        relevance: \"Generalizes CJT to correlated voters; shows majority-rule effectiveness decreases as vote correlation increases. Directly supports our Effective-K concept: correlated traces reduce the effective number of independent voters below nominal K\"\n        status: should_cite\n        verified: true\n\n      - id: fleiss1971kappa\n        title: \"Measuring Nominal Scale Agreement among Many Raters\"\n        authors: \"Fleiss, Joseph L.\"\n        venue: \"Psychological Bulletin, 76(5), 378-382, 1971\"\n        relevance: \"Defines Fleiss kappa for multi-rater agreement on nominal categories. Our framework uses Fleiss kappa to quantify inter-trace agreement as a proxy for trace independence in SC sampling\"\n        status: should_cite\n        verified: true\n\ngaps:\n  resolved:\n    - dimension: \"verification_reranking\"\n      gap: \"Added ORM, PRM, Math-Shepherd, V-STaR (2026-05-17)\"\n    - dimension: \"debate_multi_agent\"\n      gap: \"Added Liang 2023, Du 2023, Khan 2024 (2026-05-17)\"\n    - dimension: \"benchmarks_and_datasets\"\n      gap: \"Added FOLIO, ProofWriter, StrategyQA, ARC (2026-05-17)\"\n    - dimension: \"negative_results_analysis\"\n      gap: \"Added Huang 2024 (self-correct), Mirzadeh 2024 (GSM-Symbolic) (2026-05-17)\"\n    - dimension: \"symbolic_reasoning_llm\"\n      gap: \"Added LINC (Olausson et al. 2023) (2026-05-17)\"\n    - dimension: \"self_consistency_and_variants\"\n      gap: \"Added DiVeRSe (Li et al. 2023) (2026-05-17)\"\n    - dimension: \"oracle_upper_bound_experiments\"\n      gap: \"Added Press 2023 (compositionality gap), Trivedi 2023 (IRCoT oracle retrieval), Saparov & He 2023 (greedy reasoners) (2026-05-17)\"\n    - dimension: \"condorcet_voting_theory\"\n      gap: \"Added Condorcet 1785, Austen-Smith & Banks 1996, Lefort et al. 2024 (arXiv:2409.00094), Ladha 1992, Fleiss 1971 (2026-05-19)\"\n  remaining: []"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_condorcet_voting_theory_20260519T033450",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/literature_map.yaml",
    "old_string": "gaps:\n  resolved:\n    - dimension: \"verification_reranking\"\n      gap: \"Added ORM, PRM, Math-Shepherd, V-STaR (2026-05-17)\"\n    - dimension: \"debate_multi_agent\"\n      gap: \"Added Liang 2023, Du 2023, Khan 2024 (2026-05-17)\"\n    - dimension: \"benchmarks_and_datasets\"\n      gap: \"Added FOLIO, ProofWriter, StrategyQA, ARC (2026-05-17)\"\n    - dimension: \"negative_results_analysis\"\n      gap: \"Added Huang 2024 (self-correct), Mirzadeh 2024 (GSM-Symbolic) (2026-05-17)\"\n    - dimension: \"symbolic_reasoning_llm\"\n      gap: \"Added LINC (Olausson et al. 2023) (2026-05-17)\"\n    - dimension: \"self_consistency_and_variants\"\n      gap: \"Added DiVeRSe (Li et al. 2023) (2026-05-17)\"\n    - dimension: \"oracle_upper_bound_experiments\"\n      gap: \"Added Press 2023 (compositionality gap), Trivedi 2023 (IRCoT oracle retrieval), Saparov & He 2023 (greedy reasoners) (2026-05-17)\"\n  remaining: []",
    "new_string": "  condorcet_voting_theory:\n    description: \"Condorcet Jury Theorem, voting theory, and ensemble independence\"\n    papers:\n      - id: condorcet1785\n        title: \"Essai sur l'application de l'analyse à la probabilité des décisions rendues à la pluralité des voix\"\n        authors: \"Marquis de Condorcet\"\n        venue: \"Paris: Imprimerie Royale, 1785\"\n        relevance: \"The original Jury Theorem: majority voting among independent voters each with p>0.5 converges to correct answer as group size grows. Foundation for our theoretical framing of SC as majority voting over reasoning traces\"\n        status: must_cite\n        verified: true\n\n      - id: austensmith1996\n        title: \"Information Aggregation, Rationality, and the Condorcet Jury Theorem\"\n        authors: \"Austen-Smith, David and Banks, Jeffrey S.\"\n        venue: \"American Political Science Review, 90(1), 34-45, 1996\"\n        relevance: \"Key modern formalization of CJT; explicitly introduces the independence requirement and shows sincere voting is not always rational. Provides the formal basis for why trace independence matters in SC aggregation\"\n        status: must_cite\n        verified: true\n\n      - id: lefort2024condorcet_llm\n        title: \"Examining Independence in Ensemble Sentiment Analysis: A Study on the Limits of Large Language Models Using the Condorcet Jury Theorem\"\n        authors: \"Lefort, Baptiste and Benhamou, Eric and Ohana, Jean-Jacques and Guez, Beatrice and Saltiel, David and Jacquot, Thomas\"\n        venue: \"arXiv 2024\"\n        arxiv: \"2409.00094\"\n        relevance: \"CLOSEST PRIOR WORK applying CJT to LLM aggregation. Tests cross-model ensembles via majority voting for sentiment analysis; finds marginal gains due to lack of independence among advanced LLMs. Key difference from SICA: they study cross-model ensembles, we study within-model trace independence and propose Fleiss kappa + Effective-K to quantify it\"\n        status: must_cite\n        verified: true\n\n      - id: ladha1992correlated\n        title: \"The Condorcet Jury Theorem, Free Speech, and Correlated Votes\"\n        authors: \"Ladha, Krishna K.\"\n        venue: \"American Journal of Political Science, 36(3), 617-634, 1992\"\n        relevance: \"Generalizes CJT to correlated voters; shows majority-rule effectiveness decreases as vote correlation increases. Directly supports our Effective-K concept: correlated traces reduce the effective number of independent voters below nominal K\"\n        status: should_cite\n        verified: true\n\n      - id: fleiss1971kappa\n        title: \"Measuring Nominal Scale Agreement among Many Raters\"\n        authors: \"Fleiss, Joseph L.\"\n        venue: \"Psychological Bulletin, 76(5), 378-382, 1971\"\n        relevance: \"Defines Fleiss kappa for multi-rater agreement on nominal categories. Our framework uses Fleiss kappa to quantify inter-trace agreement as a proxy for trace independence in SC sampling\"\n        status: should_cite\n        verified: true\n\ngaps:\n  resolved:\n    - dimension: \"verification_reranking\"\n      gap: \"Added ORM, PRM, Math-Shepherd, V-STaR (2026-05-17)\"\n    - dimension: \"debate_multi_agent\"\n      gap: \"Added Liang 2023, Du 2023, Khan 2024 (2026-05-17)\"\n    - dimension: \"benchmarks_and_datasets\"\n      gap: \"Added FOLIO, ProofWriter, StrategyQA, ARC (2026-05-17)\"\n    - dimension: \"negative_results_analysis\"\n      gap: \"Added Huang 2024 (self-correct), Mirzadeh 2024 (GSM-Symbolic) (2026-05-17)\"\n    - dimension: \"symbolic_reasoning_llm\"\n      gap: \"Added LINC (Olausson et al. 2023) (2026-05-17)\"\n    - dimension: \"self_consistency_and_variants\"\n      gap: \"Added DiVeRSe (Li et al. 2023) (2026-05-17)\"\n    - dimension: \"oracle_upper_bound_experiments\"\n      gap: \"Added Press 2023 (compositionality gap), Trivedi 2023 (IRCoT oracle retrieval), Saparov & He 2023 (greedy reasoners) (2026-05-17)\"\n    - dimension: \"condorcet_voting_theory\"\n      gap: \"Added Condorcet 1785, Austen-Smith & Banks 1996, Lefort et al. 2024 (arXiv:2409.00094), Ladha 1992, Fleiss 1971 (2026-05-19)\"\n  remaining: []"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-19T03:37:36.126056+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/literature_map.yaml has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_condorcet_voting_theory_20260519T033450",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 37 · 2026-05-19T03:37:36.126280+00:00_

Done. Added 5 papers under `condorcet_voting_theory` dimension:

**Must-cite (3):**
1. **Condorcet 1785** — Original Jury Theorem. Standard citation: *Essai sur l'application de l'analyse à la probabilité des décisions rendues à la pluralité des voix*.
2. **Austen-Smith & Banks 1996** — Modern formalization in *American Political Science Review* 90(1):34-45. Explicitly introduces the independence requirement.
3. **Lefort et al. 2024 (arXiv:2409.00094)** — "Examining Independence in Ensemble Sentiment Analysis: A Study on the Limits of Large Language Models Using the Condorcet Jury Theorem." Tests **cross-model** LLM ensembles via majority voting for sentiment analysis; finds marginal gains due to lack of independence among advanced LLMs. Your novelty positioning: they do cross-model ensembles, you do **within-model** trace independence with Fleiss' κ + Effective-K.

**Should-cite (2):**
4. **Ladha 1992** — "The Condorcet Jury Theorem, Free Speech, and Correlated Votes." *AJPS* 36(3):617-634. Generalizes CJT to correlated voters; directly supports the Effective-K concept.
5. **Fleiss 1971** — "Measuring Nominal Scale Agreement among Many Raters." *Psychological Bulletin* 76(5):378-382. The original Fleiss' κ definition.

All 5 verified. Literature map updated.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_research_condorcet_voting_theory_20260519T033450"
}
```

</details>

---
