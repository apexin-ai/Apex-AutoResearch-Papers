# validation ref audit B

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 95
- **Recorded user turns:** 0
- **Tool calls:** 47
- **Original source:** `logs/chats/worker_validation_ref-audit-B_20260526T104735.jsonl`
- **Structured JSON:** [`be4dd1def325164cd28e.json`](../../sessions/be/be4dd1def325164cd28e.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

95 recorded events

### Tool call

_source line 1 · 2026-05-26T10:53:21.825832+00:00_

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
  "session": "worker_validation_ref-audit-B_20260526T104735",
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

_source line 2 · 2026-05-26T10:53:21.826270+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_validation_ref-audit-B_20260526T104735",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-26T10:53:21.826569+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Panickssery \"LLM Evaluators Recognize and Favor Their Own Generations\" NeurIPS 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_validation_ref-audit-B_20260526T104735",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Panickssery \"LLM Evaluators Recognize and Favor Their Own Generations\" NeurIPS 2024"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-26T10:53:21.826770+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Ye et al \"Justice or Prejudice\" LLM judge EMNLP 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_validation_ref-audit-B_20260526T104735",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Ye et al \"Justice or Prejudice\" LLM judge EMNLP 2024"
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-26T10:53:21.826944+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Polo et al \"tinyBenchmarks\" ICML 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_validation_ref-audit-B_20260526T104735",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Polo et al \"tinyBenchmarks\" ICML 2024"
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-26T10:53:21.827115+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Choi \"Diagnosing Reliability LLM-as-a-Judge IRT\" arXiv 2602.00521"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_validation_ref-audit-B_20260526T104735",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Choi \"Diagnosing Reliability LLM-as-a-Judge IRT\" arXiv 2602.00521"
  }
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-26T10:53:21.827298+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Rajore et al \"TRUCE\" arXiv 2403.00393 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_validation_ref-audit-B_20260526T104735",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Rajore et al \"TRUCE\" arXiv 2403.00393 2024"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-26T10:53:21.827548+00:00_

Web search results for query: "Panickssery "LLM Evaluators Recognize and Favor Their Own Generations" NeurIPS 2024"

Links: [{"title":"LLM Evaluators Recognize and Favor Their Own Generations","url":"https://proceedings.neurips.cc/paper_files/paper/2024/hash/7f1f0218e45f5414c79c0679633e47bc-Abstract-Conference.html"},{"title":"[2404.13076] LLM Evaluators Recognize and Favor Their Own Generations","url":"https://arxiv.org/abs/2404.13076"},{"title":"NeurIPS Poster LLM Evaluators Recognize and Favor Their Own Generations","url":"https://neurips.cc/virtual/2024/poster/96672"},{"title":"LLM Evaluators Recognize and Favor Their Own Generations","url":"https://papers.nips.cc/paper_files/paper/2024/hash/7f1f0218e45f5414c79c0679633e47bc-Abstract-Conference.html"},{"title":"LLM Evaluators Recognize and Favor Their Own Generations","url":"https://www.researchgate.net/publication/397200002_LLM_Evaluators_Recognize_and_Favor_Their_Own_Generations"},{"title":"LLM evaluators recognize and favor their own generations | Proceedings of the 38th International Conference on Neural Information Processing Systems","url":"https://dl.acm.org/doi/10.5555/3737916.3740113"},{"title":"LLM Evaluators Recognize and Favor Their Own Generations [Quick Review]","url":"https://liner.com/review/llm-evaluators-recognize-and-favor-their-own-generations"},{"title":"[PDF] LLM Evaluators Recognize and Favor Their Own Generations | Semantic Scholar","url":"https://www.semanticscholar.org/paper/LLM-Evaluators-Recognize-and-Favor-Their-Own-Panickssery-Bowman/5c7f465d162aade4a4c0eefb02fd7aadeebdaf58"},{"title":"NeurIPS 2024 LLM Evaluators Recognize and Favor Their Own Generations Oral","url":"https://neurips.cc/virtual/2024/oral/97998"},{"title":"LLM Evaluators Recognize and Favor Their Own Generations | OpenReview","url":"https://openreview.net/forum?id=4NJBV6Wp0h"}]

I found the paper you're looking for! Here's information about it:

## "LLM Evaluators Recognize and Favor Their Own Generations"

**Authors:*
…[truncated 1175 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_validation_ref-audit-B_20260526T104735",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-26T10:53:21.827812+00:00_

Web search results for query: "Polo et al "tinyBenchmarks" ICML 2024"

Links: [{"title":"tinyBenchmarks: evaluating LLMs with fewer examples for ICLR 2024 - IBM Research","url":"https://research.ibm.com/publications/tinybenchmarks-evaluating-llms-with-fewer-examples"},{"title":"tinyBenchmarks: evaluating LLMs with fewer examples for ICML 2024 - IBM Research","url":"https://research.ibm.com/publications/tinybenchmarks-evaluating-llms-with-fewer-examples--1"},{"title":"dblp: tinyBenchmarks: evaluating LLMs with fewer examples.","url":"https://dblp.org/rec/conf/icml/PoloWCSXY24.html"},{"title":"tinyBenchmarks: evaluating LLMs with fewer examples [Quick Review]","url":"https://liner.com/review/tinybenchmarks-evaluating-llms-with-fewer-examples"},{"title":"tinyBenchmarks | Proceedings of the 41st International Conference on Machine Learning","url":"https://dl.acm.org/doi/10.5555/3692070.3693466"},{"title":"(PDF) tinyBenchmarks: evaluating LLMs with fewer examples","url":"https://www.researchgate.net/publication/383238265_tinyBenchmarks_evaluating_LLMs_with_fewer_examples"},{"title":"EVALUATING LLMS WITH FEWER EXAMPLES","url":"https://openreview.net/pdf/25ac9459dd5b345badfd3d9a2c5e56b32fd89b07.pdf"},{"title":"ICML Poster tinyBenchmarks: evaluating LLMs with fewer examples","url":"https://icml.cc/virtual/2024/poster/33007"},{"title":"What We Learned at ICML2024 ft. PLaG, XRM, tinyBenchmark, MagicLens, Prompt Sketching etc.","url":"https://jina.ai/news/what-we-learned-at-icml2024-ft-plag-xrm-tinybenchmark-magiclens-prompt-sketching-etc/"},{"title":"tinyBenchmarks: evaluating LLMs with fewer examples","url":"https://proceedings.mlr.press/v235/maia-polo24a.html"}]

Based on the search results, here's what I found about the paper:

tinyBenchmarks: evaluating LLMs with fewer examples for ICML 2024 by Felipe Maia Polo et al.

**Key Details:**

- **Authors:** Felipe Maia Polo, Lucas Weber, Leshem Choshen, Yuekai Sun, Gongjun Xu, Mikhail Yurochkin
- **Venue:** Proceedings of the 4
…[truncated 964 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_validation_ref-audit-B_20260526T104735",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-26T10:53:21.828084+00:00_

Web search results for query: "Choi "Diagnosing Reliability LLM-as-a-Judge IRT" arXiv 2602.00521"

Links: [{"title":"[2602.00521] Diagnosing the Reliability of LLM-as-a-Judge via Item Response Theory","url":"https://arxiv.org/abs/2602.00521"},{"title":"Diagnosing the Reliability of LLM-as-a-Judge via Item Response Theory","url":"https://arxiv.org/html/2602.00521v1"},{"title":"Diagnosing the Reliability of LLM-as-a-Judge via Item Response Theory","url":"https://www.arxiv.org/pdf/2602.00521"},{"title":"Paper page - Diagnosing the Reliability of LLM-as-a-Judge via Item Response Theory","url":"https://huggingface.co/papers/2602.00521"},{"title":"An Empirical Study of LLM-as-a-Judge: How Design Choices Impact Evaluation Reliability","url":"https://arxiv.org/html/2506.13639v1"},{"title":"Can You Trust LLM Judgments? Reliability of LLM-as-a-Judge","url":"https://arxiv.org/html/2412.12509v2"}]

I found the paper! Here's the information about the arXiv paper 2602.00521:

**Title:** Diagnosing the Reliability of LLM-as-a-Judge via Item Response Theory

**Authors:** Junhyuk Choi and 3 other authors (specifically Sohhyung Park, Chanhee Cho, Hyeonchu Park, and Bugeun Kim)

**Publication Date:** January 31, 2026

**Overview:**
The paper introduces a two-phase diagnostic framework for assessing reliability of LLM-as-a-Judge, grounded in Item Response Theory (IRT), which adopts the Graded Response Model (GRM) and formalizes reliability along two complementary dimensions: intrinsic consistency (the stability of measurement behavior under prompt variations) and human alignment (capturing correspondence with human quality assessments).

The research empirically examines diverse LLM judges with this framework, showing that leveraging IRT-GRM yields interpretable signals for diagnosing judgments systematically, providing practical guidance for verifying reliability of LLM-as-a-Judge and identifying potential causes of unreliability.

The paper is available on arXiv at: https://arxiv.org
…[truncated 118 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_validation_ref-audit-B_20260526T104735",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-26T10:53:21.828364+00:00_

Web search results for query: "Rajore et al "TRUCE" arXiv 2403.00393 2024"

Links: [{"title":"[2403.00393] TRUCE: Private Benchmarking to Prevent Contamination and Improve Comparative Evaluation of LLMs","url":"https://arxiv.org/abs/2403.00393"},{"title":"[2403.00393v2] TRUCE: Private Benchmarking to Prevent Contamination and Improve Comparative Evaluation of LLMs","url":"https://arxiv.org/abs/2403.00393v2"},{"title":"LastingBench: Defend Benchmarks Against Knowledge Leakage","url":"https://arxiv.org/html/2506.21614v2"},{"title":"[1908.00393] Explicit examples of probability distributions for the energy density in two-dimensional conformal field theory","url":"https://arxiv.org/abs/1908.00393"},{"title":"Arxiv","url":"https://arxiv.org/pdf/2306.00393"},{"title":"[2303.00393] Probing spin-dependent charge transport at single-nanometer length scales","url":"https://arxiv.org/abs/2303.00393"},{"title":"Top Viewed Papers Referred by ArXiv | Semantic Scholar","url":"https://www.semanticscholar.org/product/scholars-hub/top-viewed-papers-referred-by-arxiv"},{"title":"Publications - NYU Web Publishing - New York University","url":"https://wp.nyu.edu/cilvr/cilvr-group-publications/"}]

Based on the search results, I found the paper you're looking for:

**TRUCE: Private Benchmarking to Prevent Contamination and Improve Comparative Evaluation of LLMs** is a paper by Tanmay Rajore, Nishanth Chandran, Sunayana Sitaram, Divya Gupta, Rahul Sharma, Kashish Mittal, and Manohar Swaminathan, with arXiv ID 2403.00393, submitted on March 1, 2024, and last revised on June 24, 2024.

**Summary of the Paper:**

The paper addresses the problem that most open-source benchmarks available have been contaminated or leaked into LLMs, raising concerns about the validity of benchmarking studies. To solve this, the authors propose Private Benchmarking, a solution where test datasets are kept private and models are evaluated without revealing the test data to the model.

The paper describes various 
…[truncated 487 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_validation_ref-audit-B_20260526T104735",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-26T10:53:21.828651+00:00_

Web search results for query: "Ye et al "Justice or Prejudice" LLM judge EMNLP 2024"

Links: [{"title":"Justice or Prejudice? Quantifying Biases in LLM-as-a-Judge","url":"https://llm-judge-bias.github.io/"},{"title":"[2410.02736] Justice or Prejudice? Quantifying Biases in LLM-as-a-Judge","url":"https://arxiv.org/abs/2410.02736"},{"title":"GitHub - DataArcTech/LLM-as-a-Judge · GitHub","url":"https://github.com/DataArcTech/LLM-as-a-Judge"},{"title":"An Empirical Study of LLM-as-a-Judge: How Design Choices Impact Evaluation Reliability","url":"https://arxiv.org/html/2506.13639v1"},{"title":"Evaluating Scoring Bias in LLM-as-a-Judge","url":"https://arxiv.org/html/2506.22316v1"},{"title":"Justice or Prejudice? Quantifying Biases in LLM-as-a-Judge","url":"https://arxiv.org/html/2410.02736v1"},{"title":"Judging with Many Minds: Do More Perspectives Mean Less Prejudice? On Bias Amplification and Resistance in Multi-Agent Based LLM-as-Judge","url":"https://arxiv.org/html/2505.19477v3"},{"title":"LLM-as-a-Judge Criteria Review","url":"https://www.emergentmind.com/topics/llm-as-a-judge-criteria"},{"title":"JUSTICE OR PREJUDICE? QUANTIFYING BIASES IN LLM-AS-A-JUDGE for ICLR 2025 - IBM Research","url":"https://research.ibm.com/publications/justice-or-prejudice-quantifying-biases-in-llm-as-a-judge"}]

I found the paper! Here are the key details about the work:

"Justice or Prejudice? Quantifying Biases in LLM-as-a-Judge" is authored by Jiayi Ye, Yanbo Wang, Yue Huang, Dongping Chen, Qihui Zhang, Nuno Moniz, Tian Gao, Werner Geyer, Chao Huang, Pin-Yu Chen, Nitesh V Chawla, and Xiangliang Zhang.

However, I should note that based on the search results, this paper is published as an arXiv preprint (arXiv:2410.02736) in 2024, not specifically at EMNLP 2024. The paper was presented at the NeurIPS Safe Generative AI Workshop 2024, and it has also been accepted to ICLR 2025.

The paper addresses the use of LLMs as an evaluation method in various benchmarks and as supervised rewards in 
…[truncated 328 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_validation_ref-audit-B_20260526T104735",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-26T10:53:21.828949+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "White et al \"LiveBench\" ICLR 2025 benchmark"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_validation_ref-audit-B_20260526T104735",
  "tool": "WebSearch",
  "tool_args": {
    "query": "White et al \"LiveBench\" ICLR 2025 benchmark"
  }
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-26T10:53:21.829141+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Vehtari et al \"Improved R-hat\" Bayesian Analysis 2021"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_validation_ref-audit-B_20260526T104735",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Vehtari et al \"Improved R-hat\" Bayesian Analysis 2021"
  }
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-26T10:53:21.829314+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Gelman et al \"Bayesian Data Analysis\" 3rd edition CRC 2013"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_validation_ref-audit-B_20260526T104735",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Gelman et al \"Bayesian Data Analysis\" 3rd edition CRC 2013"
  }
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-26T10:53:21.829509+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Vehtari Gelman Gabry \"Practical Bayesian Model Evaluation LOO-CV\" Statistics Computing 2017"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_validation_ref-audit-B_20260526T104735",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Vehtari Gelman Gabry \"Practical Bayesian Model Evaluation LOO-CV\" Statistics Computing 2017"
  }
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-26T10:53:21.829821+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Wooldridge \"Econometric Analysis of Cross Section and Panel Data\" MIT Press 2010"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_validation_ref-audit-B_20260526T104735",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Wooldridge \"Econometric Analysis of Cross Section and Panel Data\" MIT Press 2010"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-26T10:53:21.830058+00:00_

Web search results for query: "White et al "LiveBench" ICLR 2025 benchmark"

Links: [{"title":"LiveBench: A Challenging, Contamination-Limited LLM Benchmark | OpenReview","url":"https://openreview.net/forum?id=sKYHBTAxVa"},{"title":"GitHub - LiveBench/LiveBench: LiveBench: A Challenging, Contamination-Free LLM Benchmark · GitHub","url":"https://github.com/LiveBench/LiveBench"},{"title":"[2406.19314] LiveBench: A Challenging, Contamination-Limited LLM Benchmark","url":"https://arxiv.org/abs/2406.19314"},{"title":"Published as a conference paper at ICLR 2025 LIVEBENCH: A CHALLENGING,","url":"https://arxiv.org/pdf/2406.19314"},{"title":"LiveBench: A Challenging, Contamination-Limited LLM Benchmark","url":"https://proceedings.iclr.cc/paper_files/paper/2025/hash/e4a46394ba5378b3f9a186a5b4c650d1-Abstract-Conference.html"},{"title":"LiveBench: A Challenging, Contamination-Limited LLM Benchmark, Colin White+, ICLR'25 · Issue #1982 · AkihikoWatanabe/paper_notes","url":"https://github.com/AkihikoWatanabe/paper_notes/issues/1982"},{"title":"(PDF) LiveBench: A Challenging, Contamination-Free LLM Benchmark","url":"https://www.researchgate.net/publication/397595302_LiveBench_A_Challenging_Contamination-Free_LLM_Benchmark"},{"title":"LiveBench: A Challenging, Contamination-Free LLM Benchmark","url":"https://livebench.ai/livebench.pdf"},{"title":"ICLR Poster LiveBench: A Challenging, Contamination-Limited LLM Benchmark","url":"https://iclr.cc/virtual/2025/poster/28134"}]

Based on the search results, I found comprehensive information about the LiveBench benchmark:

## LiveBench: A Challenging, Contamination-Limited LLM Benchmark

LiveBench appeared as a Spotlight Paper in ICLR 2025, and the work is authored by Colin White and collaborators.

### Key Features

LiveBench is the first benchmark that (1) contains frequently-updated questions from recent information sources, (2) scores answers automatically according to objective ground-truth values, and (3) contains a wide variety of c
…[truncated 1230 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_validation_ref-audit-B_20260526T104735",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-26T10:53:21.830356+00:00_

Web search results for query: "Vehtari Gelman Gabry "Practical Bayesian Model Evaluation LOO-CV" Statistics Computing 2017"

Links: [{"title":"Efficient Leave-One-Out Cross-Validation and WAIC for Bayesian Models • loo","url":"https://mc-stan.org/loo/"},{"title":"Vehtari, A., Gelman, A. and Gabry, J. (2017) Practical Bayesian Model Evaluation Using Leave-One-Out Cross-Validation and WAIC. Statistics and Computing, 27, 1413-1432. - References - Scientific Research Publishing","url":"https://www.scirp.org/reference/referencespapers?referenceid=2679088"},{"title":"Practical Bayesian model evaluation using leave-one-out cross-validation and WAIC | Statistics and Computing | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s11222-016-9696-4"},{"title":"Efficient LOO-CV and WAIC for Bayesian models — loo-package • loo","url":"http://mc-stan.org/loo/reference/loo-package.html"},{"title":"[1507.04544] Practical Bayesian model evaluation using leave-one-out cross-validation and WAIC","url":"https://arxiv.org/abs/1507.04544"},{"title":"[PDF] Practical Bayesian model evaluation using leave-one-out cross-validation and WAIC | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Practical-Bayesian-model-evaluation-using-and-WAIC-Vehtari-Gelman/cbc2a612e973491f1b49dffad465c94eed03108d"},{"title":"Vehtari, A., Gelman, A., & Gabry, J. (2017). Practical Bayesian Model Evaluation Using Leave-One-Out Cross-Validation and WAIC. Statistics and Computing, 27, 1413-1432. - References - Scientific Research Publishing","url":"https://www.scirp.org/reference/referencespapers?referenceid=2934766"},{"title":"loo package - CRAN - R Project","url":"https://cran.r-project.org/web/packages/loo/loo.pdf"},{"title":"Practical Bayesian model evaluation using leave-one-out cross-validation and WAIC | Statistics and Computing","url":"https://dl.acm.org/doi/10.1007/s11222-016-9696-4"},{"title":"Google Scholar","url":"https://scholar.google.com/scholar_lookup?author=A.+Veht
…[truncated 1643 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_validation_ref-audit-B_20260526T104735",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-26T10:53:21.830679+00:00_

Web search results for query: "Vehtari et al "Improved R-hat" Bayesian Analysis 2021"

Links: [{"title":"Rank-normalization, folding, and localization: An improved R-hat for assessing convergence of MCMC - Aalto University's research portal","url":"https://research.aalto.fi/en/publications/rank-normalization-folding-and-localization-an-improved-r-hat-for"},{"title":"Rhat convergence diagnostic — rhat • posterior - Stan","url":"https://mc-stan.org/posterior/reference/rhat.html"},{"title":"R: Rhat convergence diagnostic","url":"https://search.r-project.org/CRAN/refmans/posterior/html/rhat.html"},{"title":"Rank-normalization, folding, and localization: An improved R-hat for assessing convergence of MCMC","url":"https://aaltodoc.aalto.fi/handle/123456789/101647"},{"title":"Rank-normalization, folding, and localization: An improved R-hat for assessing convergence of MCMC (with Discussion) - ADS","url":"https://ui.adsabs.harvard.edu/abs/2021BayAn..16..667V/abstract"},{"title":"Basic version of the Rhat convergence diagnostic — rhat_basic • posterior","url":"https://mc-stan.org/posterior/reference/rhat_basic.html"},{"title":"Discuss our new R-hat paper for the journal Bayesian Analysis! | Statistical Modeling, Causal Inference, and Social Science","url":"https://statmodeling.stat.columbia.edu/2021/04/05/discuss-our-new-r-hat-paper-for-the-journal-bayesian-analysis/"},{"title":"Research - Théo Moins","url":"https://theomoins.github.io/research/"},{"title":"rhat_basic: Basic version of the Rhat convergence diagnostic in posterior: Tools for Working with Posterior Distributions","url":"https://rdrr.io/cran/posterior/man/rhat_basic.html"}]

I found the paper! Here are the details:

**Authors:** Vehtari, A., Gelman, A., Simpson, D., Carpenter, B., & Bürkner, P.C.

**Title:** "Rank-normalization, folding, and localization: An improved R-hat for assessing convergence of MCMC"

**Journal:** Bayesian Analysis

**Publication Date:** June 2021, Volume 16, Issue 2, Pages 667-718

**DO
…[truncated 616 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_validation_ref-audit-B_20260526T104735",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-26T10:53:21.830972+00:00_

Web search results for query: "Gelman et al "Bayesian Data Analysis" 3rd edition CRC 2013"

Links: [{"title":"Amazon.com: Bayesian Data Analysis (Chapman & Hall / CRC Texts in Statistical Science): 9781439840955: Gelman, Andrew, Carlin, John B., Stern, Hal S., Dunson, David B., Vehtari, Aki, Rubin, Donald B.: Books","url":"https://www.amazon.com/Bayesian-Analysis-Chapman-Statistical-Science/dp/1439840954"},{"title":"Bayesian Data Analysis 3rd edn A. Gelman, J. B. Carlin, H. S. Stern, D. B. Dunson, A. Vehtari and D. B. Rubin, 2013 Boca Raton, Chapman and Hall–CRC 676 pp., £44.99 ISBN 1‐439‐84095‐4 | Request PDF","url":"https://www.researchgate.net/publication/269467389_Bayesian_Data_Analysis_3rd_edn_A_Gelman_J_B_Carlin_H_S_Stern_D_B_Dunson_A_Vehtari_and_D_B_Rubin_2013_Boca_Raton_Chapman_and_Hall-CRC_676_pp_4499_ISBN_1-439-84095-4"},{"title":"Gelman, A., et al. (2013) Bayesian Data Analysis. 3rd Edition, CRC Press. - References - Scientific Research Publishing","url":"https://www.scirp.org/reference/referencespapers?referenceid=3832234"},{"title":"Bayesian Data Analysis - 3rd Edition - Andrew Gelman - John B. Carlin","url":"https://www.routledge.com/Bayesian-Data-Analysis/Gelman-Carlin-Stern-Dunson-Vehtari-Rubin/p/book/9781439840955"},{"title":"Bayesian Data Analysis, Third Edition - Andrew Gelman, John B. Carlin, Hal S. Stern, David B. Dunson, Aki Vehtari, Donald B. Rubin - Google Books","url":"https://books.google.com/books/about/Bayesian_Data_Analysis_Third_Edition.html?id=ZXL6AQAAQBAJ"},{"title":"Bayesian Data Analysis | BibSonomy","url":"https://www.bibsonomy.org/bibtex/d22f1da4df2934f61f1d4ef42c32e3be"},{"title":"Bayesian Data Analysis, Third Edition (Chapman & Hall/CRC Texts in Statistical Science) by Andrew Gelman John B. Carlin Hal S. Stern David B. Dunson Aki Vehtari Donald B. Rubin(2013-11-01): Andrew Gelman: Amazon.com: Books","url":"https://www.amazon.com/Bayesian-Analysis-Chapman-Statistical-2013-11-01/dp/B01JNVQ2QC"}]

I found the information about this
…[truncated 903 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_validation_ref-audit-B_20260526T104735",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-26T10:53:21.831245+00:00_

Web search results for query: "Wooldridge "Econometric Analysis of Cross Section and Panel Data" MIT Press 2010"

Links: [{"title":"Econometric Analysis of Cross Section and Panel Data, second edition (Mit Press): Wooldridge, Jeffrey M.: 9780262232586: Amazon.com: Books","url":"https://www.amazon.com/Econometric-Analysis-Cross-Section-Panel/dp/0262232588"},{"title":"Econometric Analysis of Cross Section and Panel Data","url":"https://ideas.repec.org/b/mtp/titles/0262232588.html"},{"title":"Wooldridge, J.M. (2010) Econometric Analysis of Cross Section and Panel Data. 2nd Edition, MIT Press, Cambridge. - References - Scientific Research Publishing","url":"https://www.scirp.org/reference/referencespapers?referenceid=2542922"},{"title":"Jeffrey Wooldridge, M. (2010) Econometric Analysis of Cross Section and Panel Data. Second Edition, MIT Press, Cambridge, MA. - References - Scientific Research Publishing","url":"https://www.scirp.org/reference/referencespapers?referenceid=2674337"},{"title":"Econometric Analysis of Cross Section and Panel Data, second edition (Mit Press) by Wooldridge, Jeffrey M | Hardcover | 10/1/2010 12:00:01 A | The MIT Press | 9780262232586 | Biblio","url":"https://www.biblio.com/book/econometric-analysis-cross-section-panel-data/d/1715172557"},{"title":"Wooldridge, J.M. (2010) Econometric Analysis of Cross Section and Panel Data. 2nd Edition, MIT Press. - References - Scientific Research Publishing","url":"https://www.scirp.org/reference/referencespapers?referenceid=3888907"},{"title":"Econometric Analysis of Cross Section and Panel Data, second edition (Mit Press) - Wooldridge, Jeffrey M.: 9780262232586 - AbeBooks","url":"https://www.abebooks.com/9780262232586/Econometric-Analysis-Cross-Section-Panel-0262232588/plp"},{"title":"Econometric Analysis of Cross Section and Panel Data, second edition by Wooldridge, Jeffrey M | Hardcover | 10/1/2010 | The MIT Press | 9780262232586 | Biblio","url":"https://www.biblio.com/book/econometric-analysis-cross-s
…[truncated 1069 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_validation_ref-audit-B_20260526T104735",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-26T10:53:21.831540+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Pagan \"Regressions with Generated Regressors\" International Economic Review 1984"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_validation_ref-audit-B_20260526T104735",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Pagan \"Regressions with Generated Regressors\" International Economic Review 1984"
  }
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-26T10:53:21.831745+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Murphy Topel \"Estimation and Inference in Two-Step Econometric Models\" JBES 1985"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_validation_ref-audit-B_20260526T104735",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Murphy Topel \"Estimation and Inference in Two-Step Econometric Models\" JBES 1985"
  }
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-26T10:53:21.831934+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Angrist Pischke \"Mostly Harmless Econometrics\" Princeton 2009"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_validation_ref-audit-B_20260526T104735",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Angrist Pischke \"Mostly Harmless Econometrics\" Princeton 2009"
  }
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-26T10:53:21.832136+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Talts et al \"Validating Bayesian Inference Algorithms with SBC\" arXiv 1804.06788"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_validation_ref-audit-B_20260526T104735",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Talts et al \"Validating Bayesian Inference Algorithms with SBC\" arXiv 1804.06788"
  }
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-26T10:53:21.832320+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Zheng et al \"Judging LLM-as-a-Judge MT-Bench\" NeurIPS 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_validation_ref-audit-B_20260526T104735",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Zheng et al \"Judging LLM-as-a-Judge MT-Bench\" NeurIPS 2023"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-26T10:53:21.832562+00:00_

Web search results for query: "Pagan "Regressions with Generated Regressors" International Economic Review 1984"

Links: [{"title":"Econometric Issues in the Analysis of Regressions with Generated Regressors","url":"https://ideas.repec.org/a/ier/iecrev/v25y1984i1p221-47.html"},{"title":"Google Scholar","url":"https://scholar.google.com/scholar_lookup?title=Econometric+issues+in+the+analysis+of+regressions+with+generated+regressors&amp=&author=A.+Pagan&amp=&publication_year=1984&amp=&journal=International+Economic+Review&amp=&volume=25&amp=&pages=221-247"},{"title":"Volume 22 - 19 References - Demographic Research","url":"https://www.demographic-research.org/articles/volume/22/19/references"},{"title":"Generated regressor - HandWiki","url":"https://handwiki.org/wiki/Generated_regressor"},{"title":"The econometric analysis of models with risk terms - Pagan - 1988 - Journal of Applied Econometrics - Wiley Online Library","url":"https://onlinelibrary.wiley.com/doi/abs/10.1002/jae.3950030202"},{"title":"On Efficient Estimation and Correct Inference in Models with Generated Regressors: A General Approach | The Japanese Economic Review | Springer Nature Link","url":"https://link.springer.com/article/10.1111/1468-5876.00060"},{"title":"The Asymptotic Variance of Semiparametric Estimators with Generated Regressors\u0003","url":"https://economics.ucr.edu/wp-content/uploads/2019/10/Ridder-paper-for-4-14-10-seminar.pdf"},{"title":"Standard Error Biases When Using Generated Regressors in Accounting Research","url":"https://ideas.repec.org/a/bla/joares/v61y2023i2p531-569.html"},{"title":"The generated regressor correction: Impacts upon inferences in hypothesis testing - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/0164070489900657"}]

Based on the search results, I found the paper you're looking for:

Pagan, Adrian published "Econometric Issues in the Analysis of Regressions with Generated Regressors" in the International Economic Review, vol. 25(1)
…[truncated 413 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_validation_ref-audit-B_20260526T104735",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-26T10:53:21.832851+00:00_

Web search results for query: "Murphy Topel "Estimation and Inference in Two-Step Econometric Models" JBES 1985"

Links: [{"title":"Estimation and Inference in Two-Step Econometric Models","url":"https://ideas.repec.org/a/bes/jnlbes/v3y1985i4p370-79.html"},{"title":"Estimation and Inference in Two-Step Econometric Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Estimation-and-Inference-in-Two-Step-Econometric-Murphy-Topel/ffa632fb57449d84d61757895e574e09b24ab1c4"},{"title":"EconPapers: Estimation and Inference in Two-Step Econometric Models","url":"https://econpapers.repec.org/RePEc:bes:jnlbes:v:3:y:1985:i:4:p:370-79"},{"title":"Estimation and Inference in Two-Step Econometric Models: Journal of Business & Economic Statistics: Vol 3, No 4","url":"https://www.tandfonline.com/doi/abs/10.1080/07350015.1985.10509471"},{"title":"Estimation and Inference in Two-Step Econometric Models (1985)","url":"https://scispace.com/papers/estimation-and-inference-in-two-step-econometric-models-13ajux81ao"},{"title":"Estimation and Inference in Two-Step Econometric Models | CoLab","url":"https://colab.ws/articles/10.2307/1391724"},{"title":"TECHNICAL WORKING PAPER SERIES TWO-SAMPLE INSTRUMENTAL VARIABLES ESTIMATORS","url":"https://www.nber.org/system/files/working_papers/t0311/t0311.pdf"},{"title":"Estimation and Inference in | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Estimation-and-Inference-in-Murphy-Topel/bb93b73bc3f77ccf9336b4edd961083398b333dd"},{"title":"Calculating Murphy–Topel variance estimates in Stata: A simplified procedure","url":"https://ageconsearch.umn.edu/record/119242/files/sjart_st0114.pdf"},{"title":"NONPARAMETRIC TWO-STEP SIEVE M ESTIMATION AND INFERENCE | Econometric Theory | Cambridge Core","url":"https://www.cambridge.org/core/journals/econometric-theory/article/abs/nonparametric-twostep-sieve-m-estimation-and-inference/C7A3ED7B194C1510599CBEE1D015D5B5"}]

I found the paper you're looking for! Here are the details:

…[truncated 882 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_validation_ref-audit-B_20260526T104735",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-26T10:53:21.833117+00:00_

Web search results for query: "Angrist Pischke "Mostly Harmless Econometrics" Princeton 2009"

Links: [{"title":"Mostly Harmless Econometrics | Princeton University Press","url":"https://press.princeton.edu/books/paperback/9780691120355/mostly-harmless-econometrics"},{"title":"Mostly Harmless Econometrics: An Empiricist's Companion: 8601300372600: Economics Books @ Amazon.com","url":"https://www.amazon.com/Mostly-Harmless-Econometrics-Empiricists-Companion/dp/0691120358"},{"title":"Mostly Harmless Econometrics: An Empiricist's Companion","url":"https://ideas.repec.org/b/pup/pbooks/8769.html"},{"title":"Angrist, J. D., & Pischke, J. S. (2009). Mostly Harmless Econometrics An Empiricist’s Companion. Princeton, NJ Princeton University Press. - References - Scientific Research Publishing","url":"https://www.scirp.org/reference/referencespapers?referenceid=2949116"},{"title":"Mostly Harmless Econometrics - Wikipedia","url":"https://en.wikipedia.org/wiki/Mostly_Harmless_Econometrics"},{"title":"Home - Mostly Harmless Econometrics","url":"https://www.mostlyharmlesseconometrics.com/"},{"title":"(PDF) Mostly Harmless Econometrics: An Empiricist's Companion","url":"https://www.researchgate.net/publication/51992844_Mostly_Harmless_Econometrics_An_Empiricist's_Companion"},{"title":"Mostly harmless econometrics: an empiricist's companion - LSE Research Online","url":"https://eprints.lse.ac.uk/6128/"},{"title":"Mostly Harmless Econometrics: An Empiricist's Companion (Paperback) by Joshua D. Angrist et al. - BooksRun","url":"https://booksrun.com/9780691120355-mostly-harmless-econometrics-an-empiricists-companion-1st-edition"}]

The search results provide comprehensive information about "Mostly Harmless Econometrics" by Angrist and Pischke:

Joshua D. Angrist & Jörn-Steffen Pischke published "Mostly Harmless Econometrics: An Empiricist's Companion" with Princeton University Press in December 2009.

This econometrics book was written by two labour economists and is not a textbook as
…[truncated 756 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_validation_ref-audit-B_20260526T104735",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-26T10:53:21.833384+00:00_

Web search results for query: "Talts et al "Validating Bayesian Inference Algorithms with SBC" arXiv 1804.06788"

Links: [{"title":"[1804.06788] Validating Bayesian Inference Algorithms with Simulation-Based Calibration","url":"https://arxiv.org/abs/1804.06788"},{"title":"Validating Bayesian Inference Algorithms with Simulation-Based Calibration","url":"https://arxiv.org/pdf/1804.06788"},{"title":"Validating Bayesian Inference Algorithms with Simulation-Based Calibration | Request PDF","url":"https://www.researchgate.net/publication/324600190_Validating_Bayesian_Inference_Algorithms_with_Simulation-Based_Calibration"},{"title":"Simulation Based Calibration • rstan","url":"https://mc-stan.org/rstan/articles/SBC.html"},{"title":"[1804.06788v2] Validating Bayesian Inference Algorithms with Simulation-Based Calibration","url":"https://arxiv.org/abs/1804.06788v2"},{"title":"[1804.06788v1] Validating Bayesian Inference Algorithms with Simulation-Based Calibration","url":"https://arxiv.org/abs/1804.06788v1"},{"title":"Validating Bayesian Inference Algorithms with Simulation-Based Calibration - ADS","url":"https://ui.adsabs.harvard.edu/abs/2018arXiv180406788T/abstract"},{"title":"Validating Bayesian Inference Algorithms with Simulation-Based Calibration","url":"https://sites.stat.columbia.edu/gelman/research/unpublished/sbc.pdf"},{"title":"Simulation Based Calibration","url":"https://cran.r-project.org/web/packages/rstan/vignettes/SBC.html"}]

I found the paper you're looking for! Here's what the search revealed:

"Validating Bayesian Inference Algorithms with Simulation-Based Calibration" by Talts, S., Betancourt, M., Simpson, D., Vehtari, A., and Gelman, A. (2018) is available as arXiv preprint 1804.06788.

The paper introduces simulation-based calibration (SBC), a general procedure for validating inferences from Bayesian algorithms capable of generating posterior samples. This procedure identifies inaccurate computation and inconsistencies in model implementations while 
…[truncated 482 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_validation_ref-audit-B_20260526T104735",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-26T10:53:21.833677+00:00_

Web search results for query: "Zheng et al "Judging LLM-as-a-Judge MT-Bench" NeurIPS 2023"

Links: [{"title":"NeurIPS Poster Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena","url":"https://neurips.cc/virtual/2023/poster/73434"},{"title":"[2306.05685] Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena","url":"https://arxiv.org/abs/2306.05685"},{"title":"Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena - United Arab Emirates - Ministry of Health and Prevention","url":"https://nchr.elsevierpure.com/en/publications/judging-llm-as-a-judge-with-mt-bench-and-chatbot-arena/"},{"title":"Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena | OpenReview","url":"https://openreview.net/forum?id=uccHPGDlao"},{"title":"Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena","url":"https://papers.nips.cc/paper_files/paper/2023/hash/91f18a1287b398d378ef22505bf41832-Abstract-Datasets_and_Benchmarks.html"},{"title":"Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena Lianmin Zheng1∗","url":"https://arxiv.org/pdf/2306.05685"},{"title":"[Quick Review] Judging LLM-as-a-judge with MT-Bench and Chatbot Arena","url":"https://liner.com/review/judging-llmasajudge-with-mtbench-and-chatbot-arena"},{"title":"[Paper Note] Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena, Lianmin Zheng+, NeurIPS'23, 2023.06 · Issue #903 · AkihikoWatanabe/paper_notes","url":"https://github.com/AkihikoWatanabe/paper_notes/issues/903"},{"title":"Judging LLM-as-a-judge with MT-bench and Chatbot Arena | Proceedings of the 37th International Conference on Neural Information Processing Systems","url":"https://dl.acm.org/doi/10.5555/3666122.3668142"}]

I found the paper you're looking for. Here's what I found:

**Paper Title:** Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena

**Authors:** Lianmin Zheng, Wei-Lin Chiang, Ying Sheng, Siyuan Zhuang, Zhanghao Wu, Yonghao Zhuang, Zi Lin, Zhuohan Li, Dacheng Li, Eric Xing, Hao Zhang, Joseph Gonzalez, and Ion Stoica

**Conference:** NeurIPS 2023
…[truncated 924 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_validation_ref-audit-B_20260526T104735",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-26T10:53:21.833945+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Li et al \"Arena-Hard BenchBuilder\" arXiv 2406.11939 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_validation_ref-audit-B_20260526T104735",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Li et al \"Arena-Hard BenchBuilder\" arXiv 2406.11939 2024"
  }
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-26T10:53:21.834141+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Li et al \"Preference Leakage\" ICLR 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_validation_ref-audit-B_20260526T104735",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Li et al \"Preference Leakage\" ICLR 2026"
  }
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-26T10:53:21.834322+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Shi et al \"Detecting Pretraining Data from Large Language Models\" Min-K ICLR 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_validation_ref-audit-B_20260526T104735",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Shi et al \"Detecting Pretraining Data from Large Language Models\" Min-K ICLR 2024"
  }
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-26T10:53:21.834527+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Yax et al \"LogProber\" arXiv 2408.14352 2024 contamination"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_validation_ref-audit-B_20260526T104735",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Yax et al \"LogProber\" arXiv 2408.14352 2024 contamination"
  }
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-26T10:53:21.834721+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Xu et al \"DCR Quantifying Data Contamination\" EMNLP 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_validation_ref-audit-B_20260526T104735",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Xu et al \"DCR Quantifying Data Contamination\" EMNLP 2025"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-26T10:53:21.834949+00:00_

Web search results for query: "Li et al "Preference Leakage" ICLR 2026"

Links: [{"title":"Dawei Li✈️ICLR2026 on X: \"Something we also observed in our Preference Leakage paper (now accepted by ICLR 2026). And we went one step further to reveal the leakage and contamination problem caused by these traits transmitting: https://t.co/NNOw7tvd6l\" / X","url":"https://x.com/Dawei_Li_ASU/status/2044931299836903711"},{"title":"Preference Leakage: A Contamination Problem in LLM-as-a-judge","url":"https://arxiv.org/html/2502.01534v3"},{"title":"Preference Leakage: A Contamination Problem in LLM-as-a-judge | OpenReview","url":"https://openreview.net/forum?id=grIvSXVJ65"},{"title":"ICLR Poster Preference Leakage: A Contamination Problem in LLM-as-a-judge","url":"https://iclr.cc/virtual/2026/poster/10008112"},{"title":"[2502.01534] Preference Leakage: A Contamination Problem in LLM-as-a-judge","url":"https://arxiv.org/abs/2502.01534"},{"title":"Preference Leakage: A Contamination Problem in LLM-as- ...","url":"https://arxiv.org/pdf/2502.01534"},{"title":"Preference Leakage: A Contamination Problem in LLM-as-a-judge","url":"https://openreview.net/pdf?id=gW6NT2IuME"},{"title":"(PDF) Preference Leakage: A Contamination Problem in LLM-as-a-judge","url":"https://www.researchgate.net/publication/388685541_Preference_Leakage_A_Contamination_Problem_in_LLM-as-a-judge"}]

I found the paper! Here's what I found about "Preference Leakage: A Contamination Problem in LLM-as-a-judge" by Li et al. at ICLR 2026:

## Overview

The paper is published at ICLR 2026 as a poster presentation. It addresses how Large Language Models (LLMs) as judges and LLM-based data synthesis have emerged as fundamental LLM-driven data annotation methods, but the combination raises potential contamination concerns.

## Main Problem

The paper identifies a new contamination called "preference leakage" that can emerge when the LLM used for data generation and the LLM used for evaluation are not independent, biasing ev
…[truncated 695 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_validation_ref-audit-B_20260526T104735",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-26T10:53:21.835217+00:00_

Web search results for query: "Shi et al "Detecting Pretraining Data from Large Language Models" Min-K ICLR 2024"

Links: [{"title":"DETECTING PRETRAINING DATA FROM LARGE LANGUAGE MODELS - Princeton University","url":"https://collaborate.princeton.edu/en/publications/detecting-pretraining-data-from-large-language-models/"},{"title":"[2310.16789] Detecting Pretraining Data from Large Language Models","url":"https://arxiv.org/abs/2310.16789"},{"title":"Detecting Pretraining Data from Large Language Models | OpenReview","url":"https://openreview.net/forum?id=zWqr3MQuNs"},{"title":"DETECTING PRETRAINING DATA FROM LARGE LAN","url":"https://openreview.net/pdf?id=zWqr3MQuNs"},{"title":"Detecting Pretraining Data from Large Language Models","url":"https://swj0419.github.io/detect-pretrain.github.io/"},{"title":"GitHub - swj0419/detect-pretrain-code: This repository provides an original implementation of Detecting Pretraining Data from Large Language Models by *Weijia Shi, *Anirudh Ajith, Mengzhou Xia, Yangsibo Huang, Daogao Liu , Terra Blevins , Danqi Chen , Luke Zettlemoyer. · GitHub","url":"https://github.com/swj0419/detect-pretrain-code"},{"title":"Min-K%++: Improved Baseline for Detecting Pre-Training Data from Large Language Models","url":"https://arxiv.org/html/2404.02936v1"},{"title":"Pretraining Data Detection for Large Language Models","url":"https://aclanthology.org/2024.emnlp-main.300.pdf"},{"title":"Fine-tuning can Help Detect Pretraining Data from Large Language Models","url":"https://arxiv.org/html/2410.10880v1"}]

I found the paper! Here are the key details about the work by Shi et al.:

**Paper Title:** Detecting Pretraining Data from Large Language Models

**Authors:** Weijia Shi, Anirudh Ajith, Mengzhou Xia, Yangsibo Huang, Daogao Liu, Terra Blevins, Danqi Chen, and Luke Zettlemoyer from University of Washington and Princeton University

**Venue:** Published at the 12th International Conference on Learning Representations, ICLR 2024, in Vienna, Austria

**
…[truncated 1061 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_validation_ref-audit-B_20260526T104735",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-26T10:53:21.835497+00:00_

Web search results for query: "Li et al "Arena-Hard BenchBuilder" arXiv 2406.11939 2024"

Links: [{"title":"[2406.11939] From Crowdsourced Data to High-Quality Benchmarks: Arena-Hard and BenchBuilder Pipeline","url":"https://arxiv.org/abs/2406.11939"},{"title":"FROM CROWDSOURCED DATA TO HIGH-QUALITY BENCHMARKS: ARENA-HARD AND BENCHBUILDER","url":"https://arxiv.org/pdf/2406.11939"},{"title":"[2406.11939v1] From Crowdsourced Data to High-Quality Benchmarks: Arena-Hard and BenchBuilder Pipeline","url":"https://arxiv.org/abs/2406.11939v1"},{"title":"Paper page - From Crowdsourced Data to High-Quality Benchmarks: Arena-Hard and BenchBuilder Pipeline","url":"https://huggingface.co/papers/2406.11939"},{"title":"dblp: From Crowdsourced Data to High-Quality Benchmarks: Arena-Hard and BenchBuilder Pipeline.","url":"https://dblp.org/rec/journals/corr/abs-2406-11939.html"},{"title":"From Crowdsourced Data to High-Quality Benchmarks: Arena-Hard and B…","url":"https://www.opentrain.ai/papers/from-crowdsourced-data-to-high-quality-benchmarks-arena-hard-and-benchbuilder-pi--arxiv-2406.11939/"},{"title":"From Crowdsourced Data to High-Quality Benchmarks: Arena-Hard and BenchBuilder Pipeline","url":"https://ai.updf.com/paper-detail/from-crowdsourced-data-to-high-quality-benchmarks-arena-hard-and-li-chiang-05f02b4ed43d01f3efbbdcb454cc17b333f74817"},{"title":"[PDF] From Crowdsourced Data to High-Quality Benchmarks: Arena-Hard and BenchBuilder Pipeline | Semantic Scholar","url":"https://www.semanticscholar.org/paper/From-Crowdsourced-Data-to-High-Quality-Benchmarks:-Li-Chiang/05f02b4ed43d01f3efbbdcb454cc17b333f74817"},{"title":"lmarena-ai/arena-hard-auto · Datasets at Hugging Face","url":"https://huggingface.co/datasets/lmarena-ai/arena-hard-auto"}]

I found the paper you're looking for. Here's a summary of the research:

The paper is titled "From Crowdsourced Data to High-Quality Benchmarks: Arena-Hard and BenchBuilder Pipeline" by Tianle Li, Wei-Lin Chiang, Evan Frick, Lisa Dunlap, Ti
…[truncated 1128 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_validation_ref-audit-B_20260526T104735",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-26T10:53:21.835750+00:00_

Web search results for query: "Yax et al "LogProber" arXiv 2408.14352 2024 contamination"

Links: [{"title":"[2408.14352] LogProber: Disentangling confidence from contamination in LLM responses","url":"https://arxiv.org/abs/2408.14352"},{"title":"Assessing Contamination in Large Language Models: Introducing the LogProber method","url":"https://arxiv.org/html/2408.14352v1"},{"title":"LogProber: Disentangling confidence from contamination in LLM responses","url":"https://arxiv.org/html/2408.14352"},{"title":"[2408.14352v3] LogProber: Disentangling confidence from contamination in LLM responses","url":"https://arxiv.org/abs/2408.14352v3"},{"title":"(PDF) Assessing Contamination in Large Language Models: Introducing the LogProber method","url":"https://www.researchgate.net/publication/383428980_Assessing_Contamination_in_Large_Language_Models_Introducing_the_LogProber_method"},{"title":"arXiv:2408.14352v3 [cs.CL] 20 Jun 2025","url":"https://arxiv.org/pdf/2408.14352v3"}]

Based on the search results, here's information about the LogProber paper:

## Overview

LogProber is a novel, efficient algorithm that can detect contamination in a black box setting by focusing on the familiarity with the question rather than the answer.

## What is Contamination?

In machine learning, contamination refers to situations where testing data leak into the training set. The issue is particularly relevant for the evaluation of the performance of Large Language Models (LLMs), which are generally trained on gargantuan, and generally opaque, corpora of text scraped from the world wide web.

## How LogProber Works

LogProber analyses the (log)probability of the question in a Q-A sequence and is computationally cheap because, compared to other approaches, LogProber only requires a single forward pass on the question and storing the log-probabilities of tokens.

## Key Findings

The results show that the method is effective in detecting contamination. However, in additional model training experi
…[truncated 512 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_validation_ref-audit-B_20260526T104735",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-26T10:53:21.836006+00:00_

Web search results for query: "Xu et al "DCR Quantifying Data Contamination" EMNLP 2025"

Links: [{"title":"DCR: Quantifying Data Contamination in LLMs Evaluation - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-main.1173/"},{"title":"DCR: Quantifying Data Contamination in LLMs Evaluation","url":"https://aclanthology.org/2025.emnlp-main.1173.pdf"},{"title":"[2507.11405] DCR: Quantifying Data Contamination in LLMs Evaluation","url":"https://arxiv.org/abs/2507.11405"},{"title":"DCR: Quantifying Data Contamination in LLMs Evaluation","url":"https://arxiv.org/html/2507.11405v2"},{"title":"Cheng Xu","url":"https://xucheng.space/"},{"title":"A Survey on Data Contamination for Large Language Models","url":"https://arxiv.org/html/2502.14425v2"},{"title":"SSA: Semantic Contamination of LLM-Driven Fake News Detection - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-main.744/"},{"title":"AI-Generated Data Contamination","url":"https://www.emergentmind.com/topics/ai-generated-data-contamination"}]

Based on the search results, I found the paper you're looking for:

## DCR: Quantifying Data Contamination in LLMs Evaluation

The paper "DCR: Quantifying Data Contamination in LLMs Evaluation" by Cheng Xu, Nan Yan, Shuhao Guan, Changhong Jin, Yuke Mei, Yibing Guo, and Tahar Kechadi was published at EMNLP 2025.

### Key Details:

**Authors:** Cheng Xu, Nan Yan, Shuhao Guan, Changhong Jin, Yuke Mei, Yibing Guo, and Tahar Kechadi

**Publication:** In Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing, pages 23002–23020, Suzhou, China

### Main Contribution:

The paper introduces the Data Contamination Risk (DCR) framework, a lightweight, interpretable pipeline designed to detect and quantify benchmark data contamination (BDC) risk across four granular levels: semantic, informational, data, and label.

### Results:

The DCR framework was validated on 9 LLMs (0.5B-72B) across sentiment analysis, fake news detection, and arithmetic
…[truncated 410 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_validation_ref-audit-B_20260526T104735",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-26T10:53:21.836319+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Dekoninck et al \"ConStat\" NeurIPS 2024 contamination statistics"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_validation_ref-audit-B_20260526T104735",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Dekoninck et al \"ConStat\" NeurIPS 2024 contamination statistics"
  }
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-26T10:53:21.836548+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Sainz et al \"NLP Evaluation in Trouble\" Findings EMNLP 2023 contamination"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_validation_ref-audit-B_20260526T104735",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Sainz et al \"NLP Evaluation in Trouble\" Findings EMNLP 2023 contamination"
  }
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-26T10:53:21.836744+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Deng et al \"Investigating Data Contamination\" NAACL 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_validation_ref-audit-B_20260526T104735",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Deng et al \"Investigating Data Contamination\" NAACL 2024"
  }
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-26T10:53:21.836923+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Oren et al \"Proving Test Set Contamination\" ICLR 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_validation_ref-audit-B_20260526T104735",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Oren et al \"Proving Test Set Contamination\" ICLR 2024"
  }
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-26T10:53:21.837097+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Golchin Surdeanu \"Time Travel in LLMs\" ICLR 2024 contamination"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_validation_ref-audit-B_20260526T104735",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Golchin Surdeanu \"Time Travel in LLMs\" ICLR 2024 contamination"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-26T10:53:21.837320+00:00_

Web search results for query: "Sainz et al "NLP Evaluation in Trouble" Findings EMNLP 2023 contamination"

Links: [{"title":"NLP Evaluation in trouble: On the Need to Measure LLM Data Contamination for each Benchmark - ACL Anthology","url":"https://aclanthology.org/2023.findings-emnlp.722/"},{"title":"(PDF) NLP Evaluation in trouble: On the Need to Measure LLM Data Contamination for each Benchmark","url":"https://www.researchgate.net/publication/376393345_NLP_Evaluation_in_trouble_On_the_Need_to_Measure_LLM_Data_Contamination_for_each_Benchmark"},{"title":"NLP Evaluation in trouble: On the Need to Measure LLM ...","url":"https://aclanthology.org/2023.findings-emnlp.722.pdf"},{"title":"NLP Evaluation in trouble: On the Need to Measure LLM Data Contamination for each Benchmark | Julen Etxaniz","url":"https://julenetxaniz.eus/en/publications/sainz-2023-nlp/"},{"title":"[2310.18018] NLP Evaluation in trouble: On the Need to Measure LLM Data Contamination for each Benchmark","url":"https://arxiv.org/abs/2310.18018"},{"title":"GitHub - hitz-zentroa/lm-contamination: The LM Contamination Index is a manually created database of contamination evidences for LMs.","url":"https://github.com/hitz-zentroa/lm-contamination"},{"title":"[PDF] NLP Evaluation in trouble: On the Need to Measure LLM Data Contamination for each Benchmark | Semantic Scholar","url":"https://www.semanticscholar.org/paper/NLP-Evaluation-in-trouble:-On-the-Need-to-Measure-Sainz-Campos/cd2f4aaf98bb1e020cff310000c8049d3460c54e"},{"title":"NLP Evaluation in trouble: On the Need to Measure LLM Data Contamination for each Benchmark | Documents - Universidad del País Vasco / Euskal Herriko Unibertsitatea","url":"https://ekoizpen-zientifikoa.ehu.eus/documentos/65c35d23d2edca1267d6ab7c"},{"title":"NLP Evaluation in trouble: On the Need to Measure LLM Data Contamination for each Benchmark | Documents - Sistema Vasco de Ciencia","url":"https://research.science.eus/documentos/65c35d23d2edca1267d6ab7c?lang=en"},{"title":
…[truncated 1558 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_validation_ref-audit-B_20260526T104735",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-26T10:53:21.837608+00:00_

Web search results for query: "Deng et al "Investigating Data Contamination" NAACL 2024"

Links: [{"title":"Investigating Data Contamination in Modern Benchmarks for Large Language Models - ACL Anthology","url":"https://aclanthology.org/2024.naacl-long.482/"},{"title":"Investigating Data Contamination in Modern Benchmarks for Large Language Models","url":"https://www.researchgate.net/publication/382633331_Investigating_Data_Contamination_in_Modern_Benchmarks_for_Large_Language_Models"},{"title":"dblp: Investigating Data Contamination in Modern Benchmarks for Large Language Models.","url":"https://dblp.org/rec/conf/naacl/Deng0TGC24.html"},{"title":"[2311.09783] Investigating Data Contamination in Modern Benchmarks for Large Language Models","url":"https://arxiv.org/abs/2311.09783"},{"title":"Investigating Data Contamination in Modern Benchmarks for Large Language Models","url":"https://papers.gersteinlab.org/papers/llmcontamination/index.html"},{"title":"[Quick Review] Investigating Data Contamination in Modern Benchmarks for Large Language Models","url":"https://liner.com/review/investigating-data-contamination-in-modern-benchmarks-for-large-language-models"},{"title":"A Survey on Data Contamination for Large Language Models","url":"https://arxiv.org/html/2502.14425v2"},{"title":"How Much Can We Forget about Data Contamination?","url":"https://arxiv.org/html/2410.03249v4"}]

I found the paper! Here are the search results for the Deng et al. "Investigating Data Contamination" NAACL 2024 paper:

**Basic Information:**
The paper is authored by Chunyuan Deng, Yilun Zhao, Xiangru Tang, Mark Gerstein, and Arman Cohan, and was published in Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers), pages 8706–8719, Mexico City, Mexico.

**Overview:**
The paper raises concerns about potential contamination of evaluation benchmarks, noting a disparity between inflated 
…[truncated 517 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_validation_ref-audit-B_20260526T104735",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-26T10:53:21.837876+00:00_

Web search results for query: "Dekoninck et al "ConStat" NeurIPS 2024 contamination statistics"

Links: [{"title":"ConStat: Performance-Based Contamination Detection in Large Language Models","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/a7f89793b9e6f8c6568dbbb6ff727b9b-Paper-Conference.pdf"},{"title":"NeurIPS Poster ConStat: Performance-Based Contamination Detection in Large Language Models","url":"https://neurips.cc/virtual/2024/poster/96266"},{"title":"GitHub - lyy1994/awesome-data-contamination: The Paper List on Data Contamination for Large Language Models Evaluation. · GitHub","url":"https://github.com/lyy1994/awesome-data-contamination"},{"title":"ConStat: Performance-Based Contamination Detection in Large Language Models","url":"https://neurips.cc/media/neurips-2024/Slides/96266.pdf"},{"title":"[2405.16281] ConStat: Performance-Based Contamination Detection in Large Language Models","url":"https://arxiv.org/abs/2405.16281"},{"title":"What Is a Contaminated LLM? Detection, Famous Cases, 2026 Guide","url":"https://llm-stats.com/blog/research/what-is-a-contaminated-llm"},{"title":"GitHub - eth-sri/ConStat: A statistical test for contamination detection in language models. · GitHub","url":"https://github.com/eth-sri/ConStat"},{"title":"ConStat: Performance-Based Contamination Detection in Large Language Models","url":"https://constat.ai/"},{"title":"A Survey on Data Contamination for Large Language Models","url":"https://arxiv.org/html/2502.14425v2"},{"title":"ConStat: Performance-Based Contamination Detection in Large Language Models | OpenReview","url":"https://openreview.net/forum?id=ALISPmDPCq"}]

I found comprehensive information about the Dekoninck et al. ConStat paper from NeurIPS 2024. Here's what I found:

## Paper Overview

ConStat was presented by Jasper Dekoninck, Mark Müller, and Martin Vechev at NeurIPS 2024. The full title is "ConStat: Performance-Based Contamination Detection in Large Language Models."

## Key Contribution: No
…[truncated 1273 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_validation_ref-audit-B_20260526T104735",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-26T10:53:21.838167+00:00_

Web search results for query: "Oren et al "Proving Test Set Contamination" ICLR 2024"

Links: [{"title":"[2310.17623] Proving Test Set Contamination in Black Box Language Models","url":"https://arxiv.org/abs/2310.17623"},{"title":"12th ICLR 2024: Vienna, Austria","url":"https://dblp.org/db/conf/iclr/iclr2024.html"},{"title":"Proving Test Set Contamination In Black Box Language Models | ICLR 2024 - YouTube","url":"https://www.youtube.com/watch?v=bDVCaYCOUfQ"},{"title":"ICLR Poster Proving Test Set Contamination in Black-Box Language Models","url":"https://iclr.cc/virtual/2024/poster/18904"},{"title":"Published as a conference paper at ICLR 2026 CONTAMINATION DETECTION","url":"https://openreview.net/pdf?id=gk6OC3XIZW"},{"title":"ICLR 2024 Proving Test Set Contamination in Black-Box Language Models Oral","url":"https://iclr.cc/virtual/2024/oral/19769"},{"title":"ICLR 2024 — Best Papers & Talks (Benchmarks, Reasoning & Agents) — ft. Graham Neubig, Aman Sanger, Moritz Hardt)","url":"https://www.latent.space/p/iclr-2024-benchmarks-agents"},{"title":"ICLR 2024 — Best Papers & Talk... - Latent Space: The AI Engineer Podcast - Apple Podcasts","url":"https://podcasts.apple.com/au/podcast/iclr-2024-best-papers-talks-benchmarks-reasoning-agents/id1674008350?i=1000658401616"},{"title":"[PDF] Proving Test Set Contamination in Black Box Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Proving-Test-Set-Contamination-in-Black-Box-Models-Oren-Meister/c871377b208814713c18e25633866323a2982136"}]

I found the paper you're looking for! Here are the key details:

**Paper:** "Proving Test Set Contamination in Black-Box Language Models" by Yonatan Oren, Nicole Meister, Niladri S. Chatterji, Faisal Ladhak, and Tatsunori Hashimoto

**Conference:** The paper was presented at ICLR 2024 (the Twelfth International Conference on Learning Representations) held in Vienna, Austria, May 7-11, 2024

**Recognition:** The paper received an Outstanding Paper Honorable Menti
…[truncated 564 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_validation_ref-audit-B_20260526T104735",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-26T10:53:21.838470+00:00_

Web search results for query: "Golchin Surdeanu "Time Travel in LLMs" ICLR 2024 contamination"

Links: [{"title":"Time Travel in LLMs: Tracing Data Contamination in Large Language Models","url":"https://bibbase.org/network/publication/golchin-surdeanu-timetravelinllmstracingdatacontaminationinlargelanguagemodels-2024"},{"title":"Time Travel in LLMs: Tracing Data Contamination in Large ...","url":"https://arxiv.org/pdf/2308.08493"},{"title":"[2308.08493] Time Travel in LLMs: Tracing Data Contamination in Large Language Models","url":"https://arxiv.org/abs/2308.08493"},{"title":"Published as a conference paper at ICLR 2024 TIME TRAVEL IN LLMS: TRACING DATA","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/bc39a59c49b731c51398ad6b12f301d3-Paper-Conference.pdf"},{"title":"Time Travel in LLMs: Tracing Data Contamination in Large Language Models","url":"https://proceedings.iclr.cc/paper_files/paper/2024/hash/bc39a59c49b731c51398ad6b12f301d3-Abstract-Conference.html"},{"title":"ICLR Poster Time Travel in LLMs: Tracing Data Contamination in Large Language Models","url":"https://iclr.cc/virtual/2024/poster/19550"},{"title":"(PDF) Time Travel in LLMs: Tracing Data Contamination in Large Language Models","url":"https://www.researchgate.net/publication/373163691_Time_Travel_in_LLMs_Tracing_Data_Contamination_in_Large_Language_Models"},{"title":"[2308.08493v3] Time Travel in LLMs: Tracing Data Contamination in Large Language Models","url":"https://arxiv.org/abs/2308.08493v3"},{"title":"What Is a Contaminated LLM? Detection, Famous Cases, 2026 Guide","url":"https://llm-stats.com/blog/research/what-is-a-contaminated-llm"},{"title":"Preference Leakage: A Contamination Problem in LLM-as- ...","url":"https://arxiv.org/pdf/2502.01534"}]

I found information about the paper you're looking for. Here are the key details:

"Time Travel in LLMs: Tracing Data Contamination in Large Language Models" was published by Golchin and Surdeanu in the Proceedings of the Twelfth Interna
…[truncated 1003 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_validation_ref-audit-B_20260526T104735",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-26T10:53:21.838858+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Fiedler \"Bias and Uncertainty in LLM-as-a-Judge\" arXiv 2605.06939 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_validation_ref-audit-B_20260526T104735",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Fiedler \"Bias and Uncertainty in LLM-as-a-Judge\" arXiv 2605.06939 2026"
  }
}
```

</details>

---

### Tool call

_source line 54 · 2026-05-26T10:53:21.839070+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Zhang et al \"UDA Unsupervised Debiasing Alignment\" AAAI 2026 LLM judge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_validation_ref-audit-B_20260526T104735",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Zhang et al \"UDA Unsupervised Debiasing Alignment\" AAAI 2026 LLM judge"
  }
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-26T10:53:21.839246+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Zhu et al \"CyclicJudge\" arXiv 2603.01865 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_validation_ref-audit-B_20260526T104735",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Zhu et al \"CyclicJudge\" arXiv 2603.01865 2026"
  }
}
```

</details>

---

### Tool call

_source line 56 · 2026-05-26T10:53:21.839440+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Bavaresco et al \"LLMs instead of Human Judges\" ACL 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_validation_ref-audit-B_20260526T104735",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Bavaresco et al \"LLMs instead of Human Judges\" ACL 2025"
  }
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-26T10:53:21.839630+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Koo et al \"Benchmarking Cognitive Biases LLMs Evaluators\" Findings ACL 2024 cobbler"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_validation_ref-audit-B_20260526T104735",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Koo et al \"Benchmarking Cognitive Biases LLMs Evaluators\" Findings ACL 2024 cobbler"
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-26T10:53:21.839842+00:00_

Web search results for query: "Fiedler "Bias and Uncertainty in LLM-as-a-Judge" arXiv 2605.06939 2026"

Links: [{"title":"[2605.06939] Bias and Uncertainty in LLM-as-a-Judge Estimation","url":"https://arxiv.org/abs/2605.06939"},{"title":"Bias and Uncertainty in LLM-as-a-Judge Estimation","url":"https://arxiv.org/html/2605.06939"},{"title":"Evaluating and Mitigating LLM-as-a-judge Bias in Communication Systems","url":"https://arxiv.org/html/2510.12462v3"},{"title":"Justice or Prejudice? Quantifying Biases in LLM-as-a-Judge","url":"https://arxiv.org/html/2410.02736v1"},{"title":"Analyzing Uncertainty of LLM-as-a-Judge: Interval Evaluations with Conformal Prediction","url":"https://arxiv.org/html/2509.18658v1"},{"title":"A survey on LLM-as-a-judge - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S2666675825004564"},{"title":"An Empirical Study of LLM-as-a-Judge: How Design Choices Impact Evaluation Reliability","url":"https://arxiv.org/html/2506.13639v1"},{"title":"How to Correctly Report LLM-as-a-Judge Evaluations","url":"https://arxiv.org/html/2511.21140"},{"title":"Quantifying biases in LLM-as-Judge evals | OpenReview","url":"https://openreview.net/forum?id=eQxVeNZcYT"},{"title":"1 Two Ways to De-Bias an LLM-as-a-Judge:","url":"https://arxiv.org/pdf/2605.09227"}]

I found the paper you're looking for! The paper "Bias and Uncertainty in LLM-as-a-Judge Estimation" by James Fiedler was submitted on May 7, 2026 with arXiv ID 2605.06939.

Here's a summary of the paper's key contributions:

LLM-as-a-Judge evaluation has become a standard tool for assessing base model performance, but characterizing performance via the naive estimator (raw judge outputs) is systematically biased. Recent work has proposed estimators to correct this bias, but their reliability depends critically on judge quality and, for model comparisons, on calibration stability.

Sharing calibration across compared models is practically attractive but can introduce severe bias, in
…[truncated 590 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_validation_ref-audit-B_20260526T104735",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 59 · 2026-05-26T10:53:21.840107+00:00_

Web search results for query: "Zhang et al "UDA Unsupervised Debiasing Alignment" AAAI 2026 LLM judge"

Links: [{"title":"UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge | Proceedings of the AAAI Conference on Artificial Intelligence","url":"https://ojs.aaai.org/index.php/AAAI/article/view/40788"},{"title":"UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge","url":"https://arxiv.org/pdf/2508.09724"},{"title":"UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge","url":"https://arxiv.org/html/2508.09724"},{"title":"[2508.09724] UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge","url":"https://arxiv.org/abs/2508.09724"},{"title":"(PDF) UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge","url":"https://www.researchgate.net/publication/394472798_UDA_Unsupervised_Debiasing_Alignment_for_Pair-wise_LLM-as-a-Judge"},{"title":"Improving Alignment in LVLMs with Debiased Self-Judgment","url":"https://arxiv.org/html/2508.20655v1"}]

I found the paper! Here are the search results for the Zhang et al. paper on "UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge":

## Publication Details

Zhang, Y., Wang, C., Wu, L., Yu, W., Wang, Y., Bao, G., & Tang, J. (2026). UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge. Proceedings of the AAAI Conference on Artificial Intelligence, 40(41), 34854–34861.

## Paper Overview

The paper addresses a key challenge in LLM evaluation: Pairwise evaluation of LLMs is prone to preference bias, where judges systematically favor certain outputs, such as their own. This bias leads to inconsistent and skewed rankings across different judges.

## Proposed Solution

The authors propose UDA (Unsupervised Debiasing Alignment), a framework that reduces inter-judge disagreement by dynamically adjusting the Elo rating system. For each pairwise comparison, a compact neural network learns to adaptively set the K-factor and refine win probabilities. C
…[truncated 625 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_validation_ref-audit-B_20260526T104735",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-26T10:53:21.840495+00:00_

Web search results for query: "Bavaresco et al "LLMs instead of Human Judges" ACL 2025"

Links: [{"title":"LLMs instead of Human Judges? A Large Scale Empirical Study across 20 NLP Evaluation Tasks - ACL Anthology","url":"https://aclanthology.org/2025.acl-short.20/"},{"title":"LLMs instead of Human Judges? A Large Scale Empirical Study across 20 NLP Evaluation Tasks - Utrecht University","url":"https://research-portal.uu.nl/en/publications/llms-instead-of-human-judges-a-large-scale-empirical-study-across/"},{"title":"LLMs instead of Human Judges? A Large Scale Empirical Study across 20 NLP Evaluation Tasks - Heriot-Watt Research Portal","url":"https://researchportal.hw.ac.uk/en/publications/llms-instead-of-human-judges-a-large-scale-empirical-study-across/"},{"title":"Accepted Main Conference Papers - ACL 2025","url":"https://2025.aclweb.org/program/main_papers/"},{"title":"[2406.18403] LLMs instead of Human Judges? A Large Scale Empirical Study across 20 NLP Evaluation Tasks","url":"https://arxiv.org/abs/2406.18403"},{"title":"LLMs instead of human judges? A large scale empirical study across 20 NLP evaluation tasks | Max Planck Institute","url":"https://www.mpi.nl/publications/item3650876/llms-instead-human-judges-large-scale-empirical-study-across-20-nlp"},{"title":"arXiv:2406.18403v3 [cs.CL] 2 Jun 2025 LLMs instead of Human Judges?","url":"https://clp.ling.uni-potsdam.de/publications/Bavaresco-2025.pdf"},{"title":"LLMs instead of Human Judges? A Large Scale Empirical Study across 20 NLP Evaluation Tasks | Request PDF","url":"https://www.researchgate.net/publication/394270204_LLMs_instead_of_Human_Judges_A_Large_Scale_Empirical_Study_across_20_NLP_Evaluation_Tasks"},{"title":"MCML - LLMs Instead of Human Judges? a Large Scale Empirical Study Across 20 NLP Evaluation Tasks","url":"https://mcml.ai/publications/bbb+25/"},{"title":"Evaluating Alignment and Vulnerabilities in LLMs-as-Judges","url":"https://aclanthology.org/2025.gem-1.33.pdf"}]

I found the paper you'r
…[truncated 1493 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_validation_ref-audit-B_20260526T104735",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 61 · 2026-05-26T10:53:21.841051+00:00_

Web search results for query: "Koo et al "Benchmarking Cognitive Biases LLMs Evaluators" Findings ACL 2024 cobbler"

Links: [{"title":"Benchmarking Cognitive Biases in Large Language Models as Evaluators - ACL Anthology","url":"https://aclanthology.org/2024.findings-acl.29/"},{"title":"Benchmarking Cognitive Biases in Large Language Models as Evaluators - Experts@Minnesota","url":"https://experts.umn.edu/en/publications/benchmarking-cognitive-biases-in-large-language-models-as-evaluat/"},{"title":"GitHub - minnesotanlp/cobbler: Code and data for Koo et al's ACL 2024 paper \"Benchmarking Cognitive Biases in Large Language Models as Evaluators\" · GitHub","url":"https://github.com/minnesotanlp/cobbler"},{"title":"Cognitive Biases in Large Language Models: A Survey and Mitigation Experiments","url":"https://arxiv.org/html/2412.00323v1"},{"title":"Accepted Findings Papers - ACL 2024","url":"https://2024.aclweb.org/program/finding_papers/"},{"title":"Benchmarking Cognitive Biases in Large Language Models as Evaluators | Request PDF","url":"https://www.researchgate.net/publication/384209612_Benchmarking_Cognitive_Biases_in_Large_Language_Models_as_Evaluators"},{"title":"Benchmarking Cognitive Biases in Large Language Models as Evaluators","url":"https://aclanthology.org/2024.findings-acl.29.xml"},{"title":"Benchmarking Cognitive Biases in Large Language Models as Evaluators","url":"https://arxiv.org/html/2309.17012v3"}]

Based on the search results, here's what I found about the Koo et al. paper:

## Overview

Ryan Koo, Minhwa Lee, Vipul Raheja, Jong Inn Park, Zae Myung Kim, and Dongyeop Kang published "Benchmarking Cognitive Biases in Large Language Models as Evaluators" in Findings of the Association for Computational Linguistics: ACL 2024.

## Key Findings and Methodology

The researchers assembled 16 LLMs encompassing four different size ranges and evaluated their output responses by preference ranking from the other LLMs as evaluators.

## The COBBLER Benchmark

The 
…[truncated 546 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_validation_ref-audit-B_20260526T104735",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-26T10:53:21.841448+00:00_

Web search results for query: "Zhu et al "CyclicJudge" arXiv 2603.01865 2026"

Links: [{"title":"CyclicJudge: Mitigating Judge Bias Efficiently in LLM-based Evaluation","url":"https://arxiv.org/html/2603.01865"},{"title":"[2603.01865] CyclicJudge: Mitigating Judge Bias Efficiently in LLM-based Evaluation","url":"https://arxiv.org/abs/2603.01865"},{"title":"CyclicJudge: Mitigating Judge Bias Efficiently in LLM-based Evaluation","url":"https://arxiv.org/pdf/2603.01865"},{"title":"Taming the Judge: Deconflicting AI Feedback for Stable Reinforcement Learning","url":"https://arxiv.org/pdf/2510.15514"},{"title":"Deep Learning Pipeline for Automated Cell Profiling from Cyclic Imaging","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10775369/"}]

Based on the search results, I found the paper you're looking for:

**Title:** CyclicJudge: Mitigating Judge Bias Efficiently in LLM-based Evaluation

**Authors:** Ziyi Zhu, Olivier Tieleman, Alexey Bukhtiyarov, and Jinghong Chen (from Slingshot AI and Department of Engineering, University of Cambridge)

**Key Contributions:**

The work introduces a variance decomposition that partitions benchmark score variance into scenario, generation, judge, and residual components. CyclicJudge, a round-robin assignment of judges to scenarios, is demonstrated to be the optimal strategy for a fixed judge-call budget.

**Main Problem Addressed:** LLM judges exhibit systematic biases that cannot be eliminated by increasing the number of scenarios or generations, and these biases are often similar in magnitude to the model differences that benchmarks are designed to detect, resulting in unreliable rankings when single-judge evaluations are used.

**Key Benefit:** CyclicJudge eliminates bias precisely while requiring each judge only once per cycle, maintaining the cost of single-judge evaluation.

The paper was submitted on March 2, 2026 (arXiv:2603.01865v2).


REMINDER: You MUST include the sources above in your response to the user using markd
…[truncated 15 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_validation_ref-audit-B_20260526T104735",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-26T10:53:21.841747+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Li et al \"Split and Merge\" EMNLP 2024 LLM judge bias"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_validation_ref-audit-B_20260526T104735",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Li et al \"Split and Merge\" EMNLP 2024 LLM judge bias"
  }
}
```

</details>

---

### Tool call

_source line 64 · 2026-05-26T10:53:21.841955+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Wang et al \"LLMs are not Fair Evaluators\" ACL 2024 position bias"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_validation_ref-audit-B_20260526T104735",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Wang et al \"LLMs are not Fair Evaluators\" ACL 2024 position bias"
  }
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-26T10:53:21.842147+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Vania et al \"Comparing Test Sets with Item Response Theory\" ACL 2021"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_validation_ref-audit-B_20260526T104735",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Vania et al \"Comparing Test Sets with Item Response Theory\" ACL 2021"
  }
}
```

</details>

---

### Tool call

_source line 66 · 2026-05-26T10:53:21.842322+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Rodriguez et al \"Evaluation Examples Are Not Equally Informative\" IRT ACL 2021"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_validation_ref-audit-B_20260526T104735",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Rodriguez et al \"Evaluation Examples Are Not Equally Informative\" IRT ACL 2021"
  }
}
```

</details>

---

### Tool call

_source line 67 · 2026-05-26T10:53:21.842520+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Lalor Wu Yu \"Learning Latent Parameters without Human Response Patterns\" EMNLP 2019 IRT"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_validation_ref-audit-B_20260526T104735",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Lalor Wu Yu \"Learning Latent Parameters without Human Response Patterns\" EMNLP 2019 IRT"
  }
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-26T10:53:21.842746+00:00_

Web search results for query: "Wang et al "LLMs are not Fair Evaluators" ACL 2024 position bias"

Links: [{"title":"Large Language Models are not Fair Evaluators - ACL Anthology","url":"https://aclanthology.org/2024.acl-long.511/"},{"title":"Large Language Models are not Fair Evaluators | Request PDF","url":"https://www.researchgate.net/publication/384214634_Large_Language_Models_are_not_Fair_Evaluators"},{"title":"Large Language Models are not Fair Evaluators - ar5iv - arXiv","url":"https://ar5iv.labs.arxiv.org/html/2305.17926"},{"title":"[Quick Review] Large Language Models are not Fair Evaluators","url":"https://liner.com/review/large-language-models-are-not-fair-evaluators"},{"title":"A Survey on LLM-as-a-Judge","url":"https://arxiv.org/html/2411.15594v6"},{"title":"Split and Merge: Aligning Position Biases in LLM-based Evaluators - ACL Anthology","url":"https://aclanthology.org/2024.emnlp-main.621/"},{"title":"Model grading • evalthat","url":"https://simonpcouch.github.io/evalthat/articles/model-grading.html"}]

Based on the search results, here's what I found about the Wang et al. paper:

## Paper Overview

"Large Language Models are not Fair Evaluators" by Wang et al. was published in the Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers) in Bangkok, Thailand in August 2024.

## Main Finding

The paper uncovers a positional bias in the evaluation paradigm of adopting large language models (LLMs), e.g., GPT-4, as a referee to score and compare the quality of responses generated by candidate models. More specifically, the quality ranking of candidate responses can be easily hacked by simply altering their order of appearance in the context.

## Proposed Solution

The authors proposed a calibration framework to mitigate this bias by swapping the contents and averaging the scores. Extensive experiments demonstrate that their approach successfully alleviates evaluation bias, resulting in closer alignment
…[truncated 326 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_validation_ref-audit-B_20260526T104735",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 69 · 2026-05-26T10:53:21.843004+00:00_

Web search results for query: "Vania et al "Comparing Test Sets with Item Response Theory" ACL 2021"

Links: [{"title":"Comparing Test Sets with Item Response Theory - ACL Anthology","url":"https://aclanthology.org/2021.acl-long.92/"},{"title":"[2106.00840] Comparing Test Sets with Item Response Theory","url":"https://arxiv.org/abs/2106.00840"},{"title":"dblp: Comparing Test Sets with Item Response Theory.","url":"https://dblp.org/rec/conf/acl/VaniaHHMPPLCB20.html"},{"title":"Comparing Test Sets with Item Response Theory | Request PDF","url":"https://www.researchgate.net/publication/353485709_Comparing_Test_Sets_with_Item_Response_Theory"},{"title":"[PDF] Comparing Test Sets with Item Response Theory | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Comparing-Test-Sets-with-Item-Response-Theory-Vania-Htut/4ca39cf99747b8962fe37e7e025e284872df3425"},{"title":"Comparing test sets with item response theory - NYU Scholars","url":"https://nyuscholars.nyu.edu/en/publications/comparing-test-sets-with-item-response-theory"},{"title":"ml-papers/papers/2021/210601 Comparing Test Sets with Item Response Theory.md at main · rosinality/ml-papers","url":"https://github.com/rosinality/ml-papers/blob/main/papers/2021/210601%20Comparing%20Test%20Sets%20with%20Item%20Response%20Theory.md"},{"title":"[2106.00840v1] Comparing Test Sets with Item Response Theory","url":"https://arxiv.org/abs/2106.00840v1"}]

I found the paper! Here are the search results for "Comparing Test Sets with Item Response Theory" by Vania et al., published at ACL 2021:

**Citation Details:**
The paper was authored by Clara Vania, Phu Mon Htut, William Huang, Dhara Mungra, Richard Yuanzhe Pang, Jason Phang, Haokun Liu, Kyunghyun Cho, and Samuel R. Bowman, and was published in the Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics (ACL) in August 2021, pages 1141-1158.

**Key Findings:**
The paper uses Item Response Theory to evaluate 29 datasets using prediction
…[truncated 652 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_validation_ref-audit-B_20260526T104735",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-26T10:53:21.843276+00:00_

Web search results for query: "Lalor Wu Yu "Learning Latent Parameters without Human Response Patterns" EMNLP 2019 IRT"

Links: [{"title":"Learning Latent Parameters without Human Response Patterns: Item Response Theory with Artificial Crowds - ACL Anthology","url":"https://aclanthology.org/D19-1434/"},{"title":"Learning Latent Parameters without Human Response Patterns: Item Response Theory with Artificial Crowds - PubMed","url":"https://pubmed.ncbi.nlm.nih.gov/31803865/"},{"title":"[PDF] Learning Latent Parameters without Human Response Patterns: Item Response Theory with Artificial Crowds | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Learning-Latent-Parameters-without-Human-Response-Lalor-Wu/df6cd8a8d836e75690141deb732f6d19f0176a2e"},{"title":"Learning Latent Parameters without Human Response Patterns: Item Response Theory with Artificial Crowds - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC6892593/"},{"title":"[1908.11421v1] Learning Latent Parameters without Human Response Patterns: Item Response Theory with Artificial Crowds","url":"https://arxiv.org/abs/1908.11421v1"},{"title":"[1908.11421] Learning Latent Parameters without Human Response Patterns: Item Response Theory with Artificial Crowds","url":"https://arxiv.org/abs/1908.11421"},{"title":"Learning Latent Parameters without Human Response Patterns: Item Response Theory with Artificial Crowds | Request PDF","url":"https://www.researchgate.net/publication/336999016_Learning_Latent_Parameters_without_Human_Response_Patterns_Item_Response_Theory_with_Artificial_Crowds"},{"title":"Learning Latent Parameters without Human Response Patterns: Item Response Theory with Artificial Crowds: Paper and Code - CatalyzeX","url":"https://www.catalyzex.com/paper/arxiv:1908.11421"},{"title":"Learning Latent Parameters without Human Response Patterns: Item Response Theory with Artificial Crowds","url":"https://europepmc.org/articles/pmc6892593/bin/nihms1059054-supplement-appendices.pdf"}]

I foun
…[truncated 1229 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_validation_ref-audit-B_20260526T104735",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 71 · 2026-05-26T10:53:21.843574+00:00_

Web search results for query: "Li et al "Split and Merge" EMNLP 2024 LLM judge bias"

Links: [{"title":"Split and Merge: Aligning Position Biases in LLM-based Evaluators - ACL Anthology","url":"https://aclanthology.org/2024.emnlp-main.621/"},{"title":"Split and Merge: Aligning Position Biases in LLM-based Evaluators - Harbin Institute of Technology","url":"https://scholar.hit.edu.cn/en/publications/split-and-merge-aligning-position-biases-in-llm-based-evaluators/"},{"title":"Judging the Judges: A Systematic Evaluation of Bias Mitigation Strategies in LLM-as-a-Judge Pipelines","url":"https://arxiv.org/html/2604.23178"},{"title":"Neither Valid nor Reliable? Investigating the Use of LLMs as Judges","url":"https://openreview.net/pdf?id=yqKfMr0yvY"},{"title":"Split and Merge: Aligning Position Biases in LLM-based Evaluators - Lingnan Scholars","url":"https://scholars.ln.edu.hk/en/publications/split-and-merge-aligning-position-biases-in-llm-based-evaluators"},{"title":"[2310.01432] Split and Merge: Aligning Position Biases in LLM-based Evaluators","url":"https://arxiv.org/abs/2310.01432"},{"title":"Evaluating Scoring Bias in LLM-as-a-Judge","url":"https://arxiv.org/html/2506.22316v1"}]

Based on the search results, here's what I found about the Li et al. "Split and Merge" EMNLP 2024 paper:

## Paper Overview

The paper is titled "Split and Merge: Aligning Position Biases in LLM-based Evaluators" by Zongjie Li, Chaozheng Wang, Pingchuan Ma, Daoyuan Wu, Shuai Wang, Cuiyun Gao, and Yang Liu, published at EMNLP 2024.

## The Problem

The paper addresses the fact that LLM-based evaluators exhibit position bias, or inconsistency, when used to evaluate candidate answers in pairwise comparisons, favoring either the first or second answer regardless of content.

## The Proposed Solution (PORTIA)

The authors propose PORTIA, which splits answers into multiple segments, taking into account both length and semantics, and merges them back into a single prompt for evaluation by LLMs.


…[truncated 616 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_validation_ref-audit-B_20260526T104735",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 72 · 2026-05-26T10:53:21.843853+00:00_

Web search results for query: "Rodriguez et al "Evaluation Examples Are Not Equally Informative" IRT ACL 2021"

Links: [{"title":"Evaluation Examples are not Equally Informative: How should that change NLP Leaderboards? - ACL Anthology","url":"https://aclanthology.org/2021.acl-long.346/"},{"title":"Evaluation Examples Are Not Equally Informative: How Should That Change NLP Leaderboards?","url":"https://www.pedro.ai/leaderboard-acl2021"},{"title":"Figure 2 from Evaluation Examples are not Equally Informative: How should that change NLP Leaderboards? | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Evaluation-Examples-are-not-Equally-Informative:-Rodriguez-Barrow/30f233eecca2239ee1dd754914324092e53f8f19/figure/2"},{"title":"Evaluation Examples are not Equally Informative: How should that change NLP Leaderboards? | Request PDF","url":"https://www.researchgate.net/publication/353488536_Evaluation_Examples_are_not_Equally_Informative_How_should_that_change_NLP_Leaderboards"},{"title":"[PDF] Evaluation Examples are not Equally Informative: How should that change NLP Leaderboards? | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Evaluation-Examples-are-not-Equally-Informative:-Rodriguez-Barrow/30f233eecca2239ee1dd754914324092e53f8f19"},{"title":"Evaluation Examples Are Not Equally Informative:","url":"https://par.nsf.gov/servlets/purl/10309824"},{"title":"Evaluation Examples Are Not Equally Informative: How Should That Change NLP Leaderboards? - Meta Research | Meta Research","url":"https://research.facebook.com/publications/evaluation-examples-are-not-equally-informative-how-should-that-change-nlp-leaderboards/"},{"title":"irt-leaderboard/README.md at main · facebookresearch/irt-leaderboard","url":"https://github.com/facebookresearch/irt-leaderboard/blob/main/README.md"}]

I found the paper! Here are the search results for Rodriguez et al. "Evaluation Examples Are Not Equally Informative: How should that change NLP Leaderboards?":

**Paper 
…[truncated 1317 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_validation_ref-audit-B_20260526T104735",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 73 · 2026-05-26T10:53:21.844107+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Uto Ueno \"Generalized MFRM Bayesian Estimation HMC\" Behaviormetrika 2020"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_validation_ref-audit-B_20260526T104735",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Uto Ueno \"Generalized MFRM Bayesian Estimation HMC\" Behaviormetrika 2020"
  }
}
```

</details>

---

### Tool call

_source line 74 · 2026-05-26T10:53:21.844320+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Betancourt Girolami \"Hamiltonian Monte Carlo for Hierarchical Models\" CRC 2015"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_validation_ref-audit-B_20260526T104735",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Betancourt Girolami \"Hamiltonian Monte Carlo for Hierarchical Models\" CRC 2015"
  }
}
```

</details>

---

### Tool call

_source line 75 · 2026-05-26T10:53:21.844539+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "San Martin \"Identification of Item Response Theory Models\" Handbook IRT Vol 2 CRC 2016"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_validation_ref-audit-B_20260526T104735",
  "tool": "WebSearch",
  "tool_args": {
    "query": "San Martin \"Identification of Item Response Theory Models\" Handbook IRT Vol 2 CRC 2016"
  }
}
```

</details>

---

### Tool call

_source line 76 · 2026-05-26T10:53:21.844722+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Rothenberg \"Identification in Parametric Models\" Econometrica 1971"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_validation_ref-audit-B_20260526T104735",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Rothenberg \"Identification in Parametric Models\" Econometrica 1971"
  }
}
```

</details>

---

### Tool call

_source line 77 · 2026-05-26T10:53:21.844901+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Zhou et al \"Lost in Benchmarks Rethinking LLM Benchmarking IRT\" arXiv 2505.15055 AAAI 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_validation_ref-audit-B_20260526T104735",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Zhou et al \"Lost in Benchmarks Rethinking LLM Benchmarking IRT\" arXiv 2505.15055 AAAI 2026"
  }
}
```

</details>

---

### Tool result

_source line 78 · 2026-05-26T10:53:21.845124+00:00_

Web search results for query: "Uto Ueno "Generalized MFRM Bayesian Estimation HMC" Behaviormetrika 2020"

Links: [{"title":"A multidimensional generalized many-facet Rasch model for rubric-based performance assessment | Behaviormetrika | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s41237-021-00144-w"},{"title":"A generalized many-facet Rasch model and its Bayesian estimation using Hamiltonian Monte Carlo | Behaviormetrika | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s41237-020-00115-7"},{"title":"A multidimensional generalized many-facet Rasch model ...","url":"https://d-nb.info/1244896063/34"},{"title":"[PDF] A generalized many-facet Rasch model and its Bayesian estimation using Hamiltonian Monte Carlo | Semantic Scholar","url":"https://www.semanticscholar.org/paper/A-generalized-many-facet-Rasch-model-and-its-using-Uto-Ueno/a0e9dab0b1856f10d3058a8226530fc7a1cba1aa"},{"title":"Special issue: Bayesian applications to educational and psychological testing | Behaviormetrika | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s41237-020-00120-w"},{"title":"Masaki Uto, UEC - Publications","url":"https://sites.google.com/site/utomasakieng/research"},{"title":"A review of deep-neural automated essay scoring models | Behaviormetrika | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s41237-021-00142-y"},{"title":"A Bayesian many-facet Rasch model with Markov modeling for rater severity drift - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC10615980/"}]

I found the paper you're looking for! The article by Masaki Uto and Maomi Ueno (2020) is titled "A generalized many-facet Rasch model and its Bayesian estimation using Hamiltonian Monte Carlo" and was published in Behaviormetrika, Vol. 47, Issue 2, pp. 469-496.

The paper proposes a new IRT model that can represent all three typical rater characteristics and develops a Bayesian estimation method using No-U-Turn Hamiltonia
…[truncated 441 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_validation_ref-audit-B_20260526T104735",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 79 · 2026-05-26T10:53:21.845399+00:00_

Web search results for query: "San Martin "Identification of Item Response Theory Models" Handbook IRT Vol 2 CRC 2016"

Links: [{"title":"Handbook of Item Response Theory: Volume 2: Statistical Tools - 1st Ed","url":"https://www.routledge.com/Handbook-of-Item-Response-Theory-Volume-2-Statistical-Tools/Linden/p/book/9780367221041"},{"title":"Handbook of Item Response Theory: Volume one, Models","url":"https://www.tandfonline.com/doi/pdf/10.1080/00949655.2019.1628905"},{"title":"Handbook of Item Response Theory: Three Volume Set - 1st Edition - Wim","url":"https://www.routledge.com/Handbook-of-Item-Response-Theory-Three-Volume-Set/vanderLinden/p/book/9780367221201"},{"title":"Full article: Handbook of Item Response Theory, Statistical Tools, Volume 2,","url":"https://www.tandfonline.com/doi/full/10.1080/00401706.2021.1945326"},{"title":"Handbook of Item Response Theory: Volume 1: Models - 1st Edition - Wim","url":"https://www.routledge.com/Handbook-of-Item-Response-Theory-Volume-1-Models/Linden/p/book/9780367220013"},{"title":"[IRT] Item Response Theory","url":"https://www.stata.com/manuals/irt.pdf"},{"title":"Full article: Handbook of Item Response Theory: Volume one, Models","url":"https://www.tandfonline.com/doi/full/10.1080/00949655.2019.1628905"},{"title":"Amazon.com: Handbook of Item Response Theory: Volume 1: Models (Chapman & Hall/CRC Statistics in the Social and Behavioral Sciences): 9781466514317: van der Linden, Wim J.: Books","url":"https://www.amazon.com/Handbook-Item-Response-Theory-One/dp/1466514310"},{"title":"Full article: Handbook of item response theory: volume three, applications","url":"https://www.tandfonline.com/doi/full/10.1080/00949655.2019.1628910"}]

I found information about the chapter you're looking for. "Identification of Item Response Theory Models" by Ernesto San Martín is a chapter in the Handbook of Item Response Theory: Volume 2: Statistical Tools, published in 2016 by CRC Press.

The chapter starts by reviewing Fisher (1922) and Ko
…[truncated 451 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_validation_ref-audit-B_20260526T104735",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 80 · 2026-05-26T10:53:21.845685+00:00_

Web search results for query: "Rothenberg "Identification in Parametric Models" Econometrica 1971"

Links: [{"title":"Identification in Parametric Models | The Econometric Society","url":"https://www.econometricsociety.org/publications/econometrica/1971/05/01/identification-parametric-models"},{"title":"Rothenberg (1971)","url":"https://jblevins.org/notes/rothenberg-1971"},{"title":"[PDF] Identification in Parametric Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Identification-in-Parametric-Models-Rothenberg/43588ff71d9a7646c114d6d63eb8fe235287651b"},{"title":"Identification in Parametric Models","url":"https://ideas.repec.org/a/ecm/emetrp/v39y1971i3p577-91.html"},{"title":"IDENTIFICATION IN PARAMETRIC MODELS - ProQuest","url":"https://www.proquest.com/openview/9c36cee7f0942f1a3fcfe8877d770a9d/1?pq-origsite=gscholar&cbl=48032"},{"title":"On identifiability of parametric statistical models | Statistical Methods & Applications","url":"https://link.springer.com/article/10.1007/BF02589044"},{"title":"Identification in Parametric Models: The Minimum Hellinger Distance Criterion","url":"https://www.mdpi.com/2225-1146/10/1/10"},{"title":"Time-varying models in econometrics: Identifiability and estimation | Springer Nature Link","url":"https://link.springer.com/content/pdf/10.1007/BFb0041137.pdf"},{"title":"Econometric Specification and Identification of the Behavior of Economic Agents | Journal of Quantitative Economics | Springer Nature Link","url":"https://link.springer.com/article/10.1007/BF03404615"}]

I found the article you're looking for. Here are the details:

**"Identification in Parametric Models"** by Thomas J. Rothenberg was published in *Econometrica* in May 1971, Volume 39, Issue 3, pages 577-591.

**Key contributions:**

The paper shows that under weak regularity conditions, local identifiability of the unknown parameter vector is equivalent to nonsingularity of the information matrix. The paper also analyzes the use of "reduced-for
…[truncated 412 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_validation_ref-audit-B_20260526T104735",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 81 · 2026-05-26T10:53:21.845941+00:00_

Web search results for query: "Zhou et al "Lost in Benchmarks Rethinking LLM Benchmarking IRT" arXiv 2505.15055 AAAI 2026"

Links: [{"title":"[2505.15055] Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory","url":"https://arxiv.org/abs/2505.15055"},{"title":"Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory","url":"https://arxiv.org/html/2505.15055v2"},{"title":"Lost in Benchmarks? Rethinking Large Language Model Benchmarking with","url":"https://arxiv.org/pdf/2505.15055"},{"title":"Paper page - Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory","url":"https://huggingface.co/papers/2505.15055"},{"title":"[PDF] Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Lost-in-Benchmarks-Rethinking-Large-Language-Model-Zhou-Huang/a43a21d3b8bcede381110da630421afca45c8e5d"},{"title":"(PDF) Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory","url":"https://www.researchgate.net/publication/391954139_Lost_in_Benchmarks_Rethinking_Large_Language_Model_Benchmarking_with_Item_Response_Theory"},{"title":"Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory","url":"https://chatpaper.com/paper/139423"},{"title":"[Literature Review] Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory","url":"https://www.themoonlight.io/en/review/lost-in-benchmarks-rethinking-large-language-model-benchmarking-with-item-response-theory"}]

I found the paper! Here's the information about Zhou et al.'s work:

**Paper Title:** "Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory"

**Authors:** Hongli Zhou and 12 other authors

**arXiv ID:** 2505.15055

**Publication Date:** Initially submitted May 21, 2025, with subsequent versions 
…[truncated 1013 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_validation_ref-audit-B_20260526T104735",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 82 · 2026-05-26T10:53:21.846330+00:00_

Web search results for query: "Betancourt Girolami "Hamiltonian Monte Carlo for Hierarchical Models" CRC 2015"

Links: [{"title":"(PDF) Hamiltonian Monte Carlo for Hierarchical Models","url":"https://www.researchgate.net/publication/259106135_Hamiltonian_Monte_Carlo_for_Hierarchical_Models"},{"title":"[1312.0906] Hamiltonian Monte Carlo for Hierarchical Models","url":"https://arxiv.org/abs/1312.0906"},{"title":"(PDF) Hamiltonian Monte Carlo for Hierarchical Models (2015) | Michael Betancourt | 172 Citations","url":"https://scispace.com/papers/hamiltonian-monte-carlo-for-hierarchical-models-362eaz7zyg"},{"title":"Hamiltonian Monte Carlo and Borrowing Strength in Hierarchical Inverse Problems | ASCE-ASME Journal of Risk and Uncertainty in Engineering Systems, Part A: Civil Engineering | Vol 2, No 3","url":"https://ascelibrary.org/doi/10.1061/AJRUA6.0000847"},{"title":"[PDF] Hamiltonian Monte Carlo for Hierarchical Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Hamiltonian-Monte-Carlo-for-Hierarchical-Models-Betancourt-Girolami/f7f38d7d679b1247a0620dfbc718ca5d9ff0f447"},{"title":"[1312.0906v1] Hamiltonian Monte Carlo for Hierarchical Models","url":"https://arxiv.org/abs/1312.0906v1"},{"title":"Hamiltonian Monte Carlo for Hierarchical Models - ADS","url":"https://ui.adsabs.harvard.edu/abs/2013arXiv1312.0906B/abstract"},{"title":"Faster estimation of Bayesian models in ecology using Hamiltonian Monte Carlo - Monnahan - 2017 - Methods in Ecology and Evolution - Wiley Online Library","url":"https://besjournals.onlinelibrary.wiley.com/doi/abs/10.1111/2041-210X.12681"}]

Based on the search results, I found information about the work you're looking for:

Betancourt and Girolami (2015) published "Hamiltonian Monte Carlo for hierarchical models" in Current Trends in Bayesian Methodology with Applications (edited by S. K. Upadhyay, U. Singh, D.K. Dey & A. Loganathan), pages 79–101, published by CRC Press in Boca Raton, FL, USA.

The paper explores the u
…[truncated 328 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_validation_ref-audit-B_20260526T104735",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 83 · 2026-05-26T10:53:21.846636+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Jiao Song Lee \"Comparing Human and AI Rater Effects Using MFRM\" arXiv 2505.18486 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_validation_ref-audit-B_20260526T104735",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Jiao Song Lee \"Comparing Human and AI Rater Effects Using MFRM\" arXiv 2505.18486 2025"
  }
}
```

</details>

---

### Tool call

_source line 84 · 2026-05-26T10:53:21.846845+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Shu Henson Luecht \"Deterministic Gated IRT Detect Cheating\" Psychometrika 2013"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_validation_ref-audit-B_20260526T104735",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Shu Henson Luecht \"Deterministic Gated IRT Detect Cheating\" Psychometrika 2013"
  }
}
```

</details>

---

### Tool call

_source line 85 · 2026-05-26T10:53:21.847026+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Linacre \"Many-Facet Rasch Measurement\" MESA Press 1989 1994"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_validation_ref-audit-B_20260526T104735",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Linacre \"Many-Facet Rasch Measurement\" MESA Press 1989 1994"
  }
}
```

</details>

---

### Tool call

_source line 86 · 2026-05-26T10:53:21.847206+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Piironen Vehtari \"Sparsity Information Regularization Horseshoe\" Electronic Journal Statistics 2017"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_validation_ref-audit-B_20260526T104735",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Piironen Vehtari \"Sparsity Information Regularization Horseshoe\" Electronic Journal Statistics 2017"
  }
}
```

</details>

---

### Tool call

_source line 87 · 2026-05-26T10:53:21.847398+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Zhou et al \"PSN-IRT\" AAAI 2026 \"Lost in Benchmarks\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_validation_ref-audit-B_20260526T104735",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Zhou et al \"PSN-IRT\" AAAI 2026 \"Lost in Benchmarks\""
  }
}
```

</details>

---

### Tool result

_source line 88 · 2026-05-26T10:53:21.847628+00:00_

Web search results for query: "Jiao Song Lee "Comparing Human and AI Rater Effects Using MFRM" arXiv 2505.18486 2025"

Links: [{"title":"[2505.18486] Comparing Human and AI Rater Effects Using the Many-Facet Rasch Model","url":"https://arxiv.org/abs/2505.18486"},{"title":"Comparing Human and AI Rater Effects Using the Many-Facet Rasch Model - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250518486J/abstract"},{"title":"Correcting Human Labels for Rater Effects in AI Evaluation: An Item Response Theory Approach","url":"https://arxiv.org/html/2602.22585"},{"title":"Machine Learning May 2025","url":"https://www.arxiv.org/list/cs.LG/2025-05?skip=4175&show=2000"},{"title":"Computation and Language May 2025","url":"https://www.arxiv.org/list/cs.CL/2025-05?skip=1325&show=250"},{"title":"Network Analysis for the investigation of rater effects in language assessment: A comparison of ChatGPT vs human raters - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S2772766125000266"},{"title":"Artificial Intelligence May 2025","url":"https://www.arxiv.org/list/cs.AI/2025-05?skip=1975&show=2000"}]

I found the paper you're looking for. Here are the key details:

**Paper Title:** Comparing Human and AI Rater Effects Using the Many-Facet Rasch Model

**Authors:** Hong Jiao, Dan Song, Won-Chan Lee

**arXiv ID:** 2505.18486

**Submission Date:** Submitted on 24 May 2025 (v1), last revised 28 May 2025 (this version, v2)

**Research Focus:** The study explores how large language models (LLMs) have been widely explored for automated scoring in low-stakes assessment, with empirical evidence needed regarding which LLM produces the most reliable scores and induces least rater effects.

**Models Compared:** The study compared ten LLMs (ChatGPT 3.5, ChatGPT 4, ChatGPT 4o, OpenAI o1, Claude 3.5 Sonnet, Gemini 1.5, Gemini 1.5 Pro, Gemini 2.0, as well as DeepSeek V3, and DeepSeek R1) with human expert raters in scoring two types of writing tasks.

**Evaluation Me
…[truncated 402 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_validation_ref-audit-B_20260526T104735",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 89 · 2026-05-26T10:53:21.847894+00:00_

Web search results for query: "Piironen Vehtari "Sparsity Information Regularization Horseshoe" Electronic Journal Statistics 2017"

Links: [{"title":"Sparsity information and regularization in the horseshoe and other shrinkage priors","url":"https://projecteuclid.org/journals/electronic-journal-of-statistics/volume-11/issue-2/Sparsity-information-and-regularization-in-the-horseshoe-and-other-shrinkage/10.1214/17-EJS1337SI.full"},{"title":"[1707.01694] Sparsity information and regularization in the horseshoe and other shrinkage priors","url":"https://arxiv.org/abs/1707.01694"},{"title":"Sparsity information and regularization in the horseshoe ...","url":"https://projecteuclid.org/journals/electronic-journal-of-statistics/volume-11/issue-2/Sparsity-information-and-regularization-in-the-horseshoe-and-other-shrinkage/10.1214/17-EJS1337SI.pdf"},{"title":"(PDF) Sparsity information and regularization in the horseshoe and other shrinkage priors","url":"https://www.researchgate.net/publication/318273761_Sparsity_information_and_regularization_in_the_horseshoe_and_other_shrinkage_priors"},{"title":"Sparsity information and regularization in the horseshoe and other","url":"https://arxiv.org/pdf/1707.01694"},{"title":"Sparsity information and regularization in the horseshoe and other shrinkage priors","url":"https://aaltodoc.aalto.fi/items/d7200721-a2a9-4ac1-b655-612659eeb45e"},{"title":"Sparse regression using the “ponyshoe” (regularized horseshoe) model, from Juho Piironen and Aki Vehtari | Statistical Modeling, Causal Inference, and Social Science","url":"https://statmodeling.stat.columbia.edu/2017/07/09/updated-ponyshoe-paper-juho-piironen-aki-vehtari/"},{"title":"Regularized horseshoe priors in brms — horseshoe • brms","url":"https://paulbuerkner.com/brms/reference/horseshoe.html"},{"title":"Sparsity information and regularization in the horseshoe and other shrinkage priors - ADS","url":"https://ui.adsabs.harvard.edu/abs/2017arXiv170701694P/abstract"}]

I found the paper
…[truncated 1113 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_validation_ref-audit-B_20260526T104735",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 90 · 2026-05-26T10:53:21.848192+00:00_

Web search results for query: "Linacre "Many-Facet Rasch Measurement" MESA Press 1989 1994"

Links: [{"title":"Many-facet Rasch measurement: Linacre book","url":"https://www.rasch.org/facet.htm"},{"title":"Many-Facet Rasch Measurement [2nd Edition] 0-941938-02-6 - DOKUMEN.PUB","url":"https://dokumen.pub/many-facet-rasch-measurement-2nd-edition-0-941938-02-6.html"},{"title":"Rasch Measurement Books","url":"https://www.rasch.org/books.htm"},{"title":"(PDF) MANY-FACET RASCH MEASUREMENT","url":"https://www.researchgate.net/publication/377065952_MANY-FACET_RASCH_MEASUREMENT"},{"title":"Rasch Measurement in Higher Education | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-94-011-3955-7_7"},{"title":"Received: Revised: Accepted: ISSN: 1307-9298 Copyright © IEJEE www.iejee.com","url":"https://files.eric.ed.gov/fulltext/EJ1250486.pdf"},{"title":"(PDF) Understanding Rasch measurement: Construction of measures from many-facet data","url":"https://www.researchgate.net/publication/10987756_Understanding_Rasch_measurement_Construction_of_measures_from_many-facet_data"},{"title":"References to Many-Facet Rasch Measurement","url":"https://www.winsteps.com/facetman/references.htm"},{"title":"Many-facet Rasch measurement by J. Michael Linacre | Open Library","url":"https://openlibrary.org/books/OL1130941M/Many-facet_Rasch_measurement"}]

Based on the search results, I found detailed information about this work:

"Many-Facet Rasch Measurement" by John Michael Linacre, published in 1989, applies objective measurement to the ratings awarded by judges to persons on items of performance or any other many-facet situation. The book derives the measurement model from Rasch's axioms and discusses estimation techniques.

A second edition was published by MESA Press Chicago in 1989, 1994. The book has ISBN 0-941938-02-6 and Library of Congress number 94-76939.

The book extends objective measurement to multiple independent rank orderings and provides examples of rati
…[truncated 274 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_validation_ref-audit-B_20260526T104735",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 91 · 2026-05-26T10:53:21.848479+00:00_

Web search results for query: "Zhou et al "PSN-IRT" AAAI 2026 "Lost in Benchmarks""

Links: [{"title":"GitHub - Joe-Hall-Lee/PSN-IRT: [AAAI 2026 Oral] Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory · GitHub","url":"https://github.com/Joe-Hall-Lee/PSN-IRT"},{"title":"Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory | Proceedings of the AAAI Conference on Artificial Intelligence","url":"https://ojs.aaai.org/index.php/AAAI/article/view/40814"},{"title":"Lost in Benchmarks? Rethinking Large Language Model Benchmarking with","url":"https://ojs.aaai.org/index.php/AAAI/article/view/40814/44775"},{"title":"Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory","url":"https://arxiv.org/html/2505.15055v2"},{"title":"GitHub - TongjiFinLab/awesome-time-series-forecasting: Awesome time series forecasting papers and codes · GitHub","url":"https://github.com/TongjiFinLab/awesome-time-series-forecasting"},{"title":"Can We Trust AI Benchmarks? An Interdisciplinary Review ...","url":"https://arxiv.org/pdf/2502.06559"},{"title":"Computer Science","url":"https://www.arxiv.org/list/cs/pastweek?skip=1066&show=1000"}]

I found the paper! Here's what I found about the Zhou et al. "PSN-IRT" AAAI 2026 paper titled "Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory":

## Overview
The paper provides a critical analysis of benchmark effectiveness, examining mainstream prominent LLM benchmarks using results from diverse models, and proposes Pseudo-Siamese Network for Item Response Theory (PSN-IRT), an enhanced Item Response Theory framework that incorporates a rich set of item parameters within an IRT-grounded architecture.

## Key Contributions
The authors conduct extensive analysis on 11 LLM benchmarks comprising 41,871 items, revealing significant and varied shortcomings in their measurement quality. Furthermore, they demonstrate t
…[truncated 701 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_validation_ref-audit-B_20260526T104735",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 92 · 2026-05-26T10:53:21.848748+00:00_

Web search results for query: "Shu Henson Luecht "Deterministic Gated IRT Detect Cheating" Psychometrika 2013"

Links: [{"title":"Using Deterministic, Gated Item Response Theory Model to Detect Test Cheating Due to Item Compromise IRT","url":"https://www.ets.org/research/policy_research_reports/publications/article/2013/jqft.html"},{"title":"Using Deterministic, Gated Item Response Theory Model to Detect Test Cheating due to Item Compromise | Psychometrika | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s11336-012-9311-3"},{"title":"(PDF) Using Deterministic, Gated Item Response Theory Model to Detect Test Cheating due to Item Compromise","url":"https://www.researchgate.net/publication/257678777_Using_Deterministic_Gated_Item_Response_Theory_Model_to_Detect_Test_Cheating_due_to_Item_Compromise"},{"title":"Using Deterministic, Gated Item Response Theory Model to detect test cheating due to item compromise - PubMed","url":"https://pubmed.ncbi.nlm.nih.gov/25106396/"},{"title":"Using Deterministic, Gated Item Response Theory Model to Detect Test Cheating due to Item Compromise | Psychometrika | Cambridge Core","url":"https://www.cambridge.org/core/journals/psychometrika/article/abs/using-deterministic-gated-item-response-theory-model-to-detect-test-cheating-due-to-item-compromise/34FE98C0FA7367881713D0019619E53E"},{"title":"Data Augmentation in Machine Learning for Cheating ...","url":"https://www.psychologie-aktuell.com/fileadmin/Redaktion/Journale/ptam_2022-4/PTAM_2022-4_3.pdf"},{"title":"Are Exam Questions Known in Advance? Using Local Dependence to Detect Cheating","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5131967/"},{"title":"Detection of Two-Way Outliers in Multivariate Data and Application to   Cheating Detection in Educational Tests","url":"https://arxiv.org/pdf/1911.09408"}]

I found information about the paper you're searching for. The article "Using Deterministic, Gated Item Response Theory Model to Detect Test Cheating due 
…[truncated 912 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_validation_ref-audit-B_20260526T104735",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 93 · 2026-05-26T10:53:21.849031+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Ye \"Justice or Prejudice Quantifying Biases LLM-as-a-Judge\" venue EMNLP ICLR 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_validation_ref-audit-B_20260526T104735",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Ye \"Justice or Prejudice Quantifying Biases LLM-as-a-Judge\" venue EMNLP ICLR 2025"
  }
}
```

</details>

---

### Tool result

_source line 94 · 2026-05-26T10:53:21.849256+00:00_

Web search results for query: "Ye "Justice or Prejudice Quantifying Biases LLM-as-a-Judge" venue EMNLP ICLR 2025"

Links: [{"title":"JUSTICE OR PREJUDICE? QUANTIFYING BIASES IN LLM-AS-A-JUDGE for ICLR 2025 - IBM Research","url":"https://research.ibm.com/publications/justice-or-prejudice-quantifying-biases-in-llm-as-a-judge"},{"title":"Justice or Prejudice? Quantifying Biases in LLM-as-a-Judge - Jiayi Ye, Yanbo Wang, Yue Huang, Dongping Chen, Qihui Zhang, Nuno Moniz, Tian Gao, Werner Geyer, Chao Huang, Pin-Yu Chen, Nitesh V Chawla, Xiangliang Zhang - ICLR, 2025 | Publications | News & Events | Ethics and the Common Good | University of Notre Dame","url":"https://ethics.nd.edu/news-and-events/publications/jiayi-ye-yanbo-wang-yue-huang-dongping-chen-qihui-zhang-nuno-moniz-tian-gao-werner-geyer-chao-huang-pin-yu-chen-nitesh-v-chawla-xiangliang-zhang-iclr-2025-justice-or-prejudice-quantifying-biases-in-llm-as-a-judge/"},{"title":"Justice or Prejudice? Quantifying Biases in LLM-as-a-Judge | OpenReview","url":"https://openreview.net/forum?id=3GTtZFiajM"},{"title":"ICLR Poster Justice or Prejudice? Quantifying Biases in LLM-as-a-Judge","url":"https://iclr.cc/virtual/2025/poster/31088"},{"title":"[2410.02736] Justice or Prejudice? Quantifying Biases in LLM-as-a-Judge","url":"https://arxiv.org/abs/2410.02736"},{"title":"Justice or Prejudice? Quantifying Biases in LLM-as-a-Judge","url":"https://proceedings.iclr.cc/paper_files/paper/2025/hash/fdca08d371e4b6c031397909e20043bd-Abstract-Conference.html"},{"title":"Justice or Prejudice? Quantifying Biases in LLM-as-a-Judge","url":"https://llm-judge-bias.github.io/"},{"title":"Justice or Prejudice? Quantifying Biases in LLM-as-a-Judge","url":"https://arxiv.org/html/2410.02736v1"},{"title":"GitHub - CSHaitao/Awesome-LLMs-as-Judges: The official repo for paper, LLMs-as-Judges: A Comprehensive Survey on LLM-based Evaluation Methods. · GitHub","url":"https://github.com/CSHaitao/Awesome-LLMs-as-Judges"}]

Based on the search results, the
…[truncated 540 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_validation_ref-audit-B_20260526T104735",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 95 · 2026-05-26T10:53:21.849611+00:00_

All 45 entries verified. Here are the results:

```
总条数: 45
问题条数: 1

逐条结果:
1.  panickssery2024selffavor — ✅ NeurIPS 2024 confirmed. Authors (Panickssery, Bowman, Feng) correct.
2.  ye2024justice — ❌ **Venue 和年份错误**。Bib 写 "EMNLP 2024"，实际发表于 **ICLR 2025**（poster）。应修正 venue 为 ICLR，年份为 2025。
3.  polo2024tinybenchmarks — ✅ ICML 2024 (PMLR 235). Felipe Maia Polo et al. confirmed.
4.  choi2026irt_judge — ✅ arXiv:2602.00521, 2026. Choi et al. confirmed.
5.  truce2024 — ✅ arXiv:2403.00393, 2024. Rajore et al. confirmed.
6.  livebench2025 — ✅ ICLR 2025 (Spotlight). Colin White et al. confirmed.
7.  vehtari2021rhat — ✅ Bayesian Analysis 16(2), 2021. Vehtari, Gelman, Simpson, Carpenter, Bürkner. confirmed.
8.  gelman2013bda — ✅ CRC 2013, 3rd edition. confirmed.
9.  vehtari2017loo — ✅ Statistics and Computing 27(5), 2017. confirmed.
10. wooldridge2010 — ✅ MIT Press 2010, 2nd edition. confirmed.
11. pagan1984 — ✅ International Economic Review 25(1), 1984. confirmed.
12. murphy1985 — ✅ JBES 3(4), 1985. Murphy & Topel. confirmed.
13. angrist2009mostly — ✅ Princeton 2009. Angrist & Pischke. confirmed.
14. talts2018sbc — ✅ arXiv:1804.06788, 2018. Talts, Betancourt, Simpson, Vehtari, Gelman. confirmed.
15. zheng2023mtbench — ✅ NeurIPS 2023 (Datasets & Benchmarks). Lianmin Zheng et al. confirmed.
16. li2024arenahard — ✅ arXiv:2406.11939, 2024. Tianle Li et al. confirmed.
17. preference_leakage2026 — ✅ ICLR 2026 (poster). Dawei Li et al. confirmed.
18. mink2024 — ✅ ICLR 2024. Weijia Shi et al. "Detecting Pretraining Data" (Min-K% method). confirmed.
19. logprober2024 — ✅ arXiv:2408.14352, 2024. Nicolas Yax, Oudeyer, Palminteri. 标题和作者均正确。
20. dcr2025 — ✅ EMNLP 2025. Cheng Xu et al. confirmed.
21. constat2024 — ✅ NeurIPS 2024. Dekoninck, Müller, Vechev. confirmed.
22. sainz2023contamination — ✅ Findings EMNLP 2023. Oscar Sainz et al. confirmed.
23. deng2024contamination — ✅ NAACL 2024. Chunyuan Deng et al. confirmed.
24. oren2024proving — ✅ ICLR 2024 (Outstanding Paper Honorable Mention). Oren et al. confirmed.
25. golchin2024timetravel — ✅ ICLR 2024 (Spotlight). Golchin & Surdeanu. confirmed.
26. fiedler2026bias_uncertainty — ✅ arXiv:2605.06939, 2026. James Fiedler. confirmed.
27. uda2026 — ✅ AAAI 2026. Zhang et al. confirmed.
28. cyclicjudge2026 — ✅ arXiv:2603.01865, 2026. Zhu et al. confirmed.
29. bavaresco2025judgebench — ✅ ACL 2025 Short. Bavaresco et al. confirmed.
30. koo2024cobbler — ✅ Findings ACL 2024. Ryan Koo et al. COBBLER benchmark. confirmed.
31. li2024splitmerge — ✅ EMNLP 2024. Zongjie Li et al. confirmed.
32. wang2024positionbias — ✅ ACL 2024. Wang et al. confirmed.
33. vania2021irt — ✅ ACL 2021. Clara Vania et al. confirmed.
34. rodriguez2021irt — ✅ ACL 2021. Pedro Rodriguez et al. confirmed.
35. lalor2019irt — ✅ EMNLP 2019. Lalor, Wu, Yu. confirmed.
36. uto2020generalized — ✅ Behaviormetrika 47(2), 2020. Uto & Ueno. confirmed.
37. betancourt2015 — ✅ CRC 2015. Betancourt & Girolami. confirmed.
38. sanmartin2016 — ✅ Handbook IRT Vol 2, CRC 2016. San Martín. confirmed.
39. rothenberg1971 — ✅ Econometrica 39(3), 1971. confirmed.
40. zhou2025psnirt — ✅ AAAI 2026 (Oral). arXiv:2505.15055. Zhou et al. confirmed.
41. jiao2025mfrm_llm — ✅ arXiv:2505.18486, 2025. Jiao, Song, Lee. confirmed.
42. shu2013dgirt — ✅ Psychometrika 78(3), 2013. Shu, Henson, Luecht. confirmed.
43. linacre1994mfrm — ✅ MESA Press 1994, 2nd edition. confirmed.
44. linacre1989mfrm — ✅ MESA Press 1989, 1st edition. confirmed.
45. piironen2017horseshoe — ✅ EJS 11(2), 2017. Piironen & Vehtari. confirmed.
```

**唯一问题：`ye2024justice`** — venue 写成 EMNLP 2024，实际是 **ICLR 2025**。bib key 的年份 2024 也应改为 2025。这篇论文 2024 年 10 月上 arXiv，2025 年被 ICLR 接收。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_validation_ref-audit-B_20260526T104735"
}
```

</details>

---
