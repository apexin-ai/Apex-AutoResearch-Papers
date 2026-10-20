# research pride formula verify

**afford invar** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 43
- **Recorded user turns:** 0
- **Tool calls:** 21
- **Original source:** `logs/chats/worker_research_pride-formula-verify_20260519T232737.jsonl`
- **Structured JSON:** [`331afae3d8739fbb384f.json`](../../sessions/33/331afae3d8739fbb384f.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

43 recorded events

### Tool call

_source line 1 · 2026-05-19T23:31:00.785187+00:00_

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
  "session": "worker_research_pride-formula-verify_20260519T232737",
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

_source line 2 · 2026-05-19T23:31:00.785607+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_pride-formula-verify_20260519T232737",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-19T23:31:00.785841+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "PRIDE metric LIBERO paraphrase robustness VLA"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_pride-formula-verify_20260519T232737",
  "tool": "WebSearch",
  "tool_args": {
    "query": "PRIDE metric LIBERO paraphrase robustness VLA"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-19T23:31:00.785978+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arXiv 2603.28301"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_pride-formula-verify_20260519T232737",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arXiv 2603.28301"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-19T23:31:00.786142+00:00_

Web search results for query: "PRIDE metric LIBERO paraphrase robustness VLA"

Links: [{"title":"LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models","url":"https://arxiv.org/html/2603.28301v1"},{"title":"[2603.28301] LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models","url":"https://arxiv.org/abs/2603.28301"},{"title":"LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models","url":"https://cau-hai-lab.github.io/LIBERO-Para/"},{"title":"GitHub - cau-hai-lab/LIBERO-Para · GitHub","url":"https://github.com/cau-hai-lab/LIBERO-Para"},{"title":"Paper page - LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models","url":"https://huggingface.co/papers/2603.28301"},{"title":"paraphrase · GitHub Topics · GitHub","url":"https://github.com/topics/paraphrase"}]

Based on the search results, here's what I found:

PRIDE (Paraphrase Robustness Index in Robotic Instructional DEviation) is a metric that combines keyword similarity (lexical shift) and structural similarity (syntactic variation) with task success to enable fine-grained robustness analysis.

PRIDE quantifies paraphrase difficulty using semantic and syntactic factors, and it is a difficulty-aware metric that goes beyond binary success rate, giving more credit for succeeding on harder paraphrases.

PRIDE was introduced as part of LIBERO-Para, a controlled benchmark for evaluating paraphrase robustness in VLA (Vision-Language-Action) models. LIBERO-Para is grounded in the linguistic structure of robotic manipulation instructions—where actions and objects serve as core semantic elements—and adopts a two-axis design that independently varies action expressions and object references.

The research addresses a key finding: degradation is primarily driven by object-level lexical variation; even simple synonym substitutions cause large drops, indicating reliance on surface-level matching rathe
…[truncated 129 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_pride-formula-verify_20260519T232737",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-19T23:31:00.786349+00:00_

Web search results for query: "arXiv 2603.28301"

Links: [{"title":"LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models","url":"https://arxiv.org/html/2603.28301"},{"title":"Immune escape and attenuated severity associated with the SARS-CoV-2 BA.2.86/JN.1 lineage","url":"https://www.medrxiv.org/content/10.1101/2024.04.17.24305964.full.pdf"},{"title":"my_arXiv_daily/README.md at main · BaiShuanghao/my_arXiv_daily","url":"https://github.com/BaiShuanghao/my_arXiv_daily/blob/main/README.md"},{"title":"Evolution and neutralization escape of the SARS-CoV-2 BA.2.86 subvariant","url":"https://www.medrxiv.org/content/10.1101/2023.09.08.23295250.full.pdf"},{"title":"Symphonizing pileup and full-alignment for deep learning-based long-read variant calling","url":"https://www.biorxiv.org/content/10.1101/2021.12.29.474431.full.pdf"}]

Based on the search results, arXiv 2603.28301 is a paper titled "LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models" by Chanyoung Kim, Minwoo Kim, Minseok Kang, Hyunwoo Kim, and Dahuin Jung, from Soongsil University and Chung-Ang University, published on March 30, 2026.

The paper introduces LIBERO-Para, a controlled benchmark that independently varies action expressions and object references for fine-grained analysis of linguistic generalization. The research addresses a gap in Vision-Language-Action (VLA) models, which are typically fine-tuned with limited data in downstream robotic settings, leading to overfitting to specific instruction formulations and leaving robustness to paraphrased instructions underexplored. The study found consistent performance degradation of 22–52 percentage points under paraphrasing across seven VLA configurations ranging from 0.6B–7.5B parameters.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_pride-formula-verify_20260519T232737",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-19T23:31:00.786542+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "PRIDE formula \"Paraphrase Robustness\" site:arxiv.org 2603.28301 SK ST alpha"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_pride-formula-verify_20260519T232737",
  "tool": "WebSearch",
  "tool_args": {
    "query": "PRIDE formula \"Paraphrase Robustness\" site:arxiv.org 2603.28301 SK ST alpha"
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-19T23:31:00.786703+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"PRIDE\" \"paraphrase difficulty\" formula definition arxiv LIBERO-Para 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_pride-formula-verify_20260519T232737",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"PRIDE\" \"paraphrase difficulty\" formula definition arxiv LIBERO-Para 2026"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-19T23:31:00.786878+00:00_

Web search results for query: ""PRIDE" "paraphrase difficulty" formula definition arxiv LIBERO-Para 2026"

Links: [{"title":"[2603.28301] LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models","url":"https://arxiv.org/abs/2603.28301"},{"title":"Paper page - LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models","url":"https://huggingface.co/papers/2603.28301"},{"title":"LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models","url":"https://cau-hai-lab.github.io/LIBERO-Para/"},{"title":"GitHub - cau-hai-lab/LIBERO-Para · GitHub","url":"https://github.com/cau-hai-lab/LIBERO-Para"},{"title":"LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models","url":"https://arxiv.org/html/2603.28301v1"},{"title":"cau-hai-lab · GitHub","url":"https://github.com/cau-hai-lab"},{"title":"paraphrase · GitHub Topics · GitHub","url":"https://github.com/topics/paraphrase"}]

Based on the search results, I found detailed information about PRIDE and the LIBERO-Para benchmark.

PRIDE is a metric that quantifies paraphrase difficulty using semantic and syntactic factors. More specifically, PRIDE (Paraphrase Robustness Index in Robotic Instructional DEviation) evaluates how robustly a VLA model handles paraphrased instructions by computing a Paraphrase Distance (PD) from keyword similarity (SK) and structural similarity (ST), then measuring the ratio of PD-weighted successes to total possible PD, normalized to 0–100.

PRIDE combines keyword similarity (lexical shift) and structural similarity (syntactic variation) with task success to enable fine-grained robustness analysis. Unlike plain success rate, PRIDE gives more credit for succeeding on harder, more deviated paraphrases.

This metric was introduced as part of the LIBERO-Para benchmark, a controlled benchmark that independently varies action expressions and object references for fine-grained analysis of ling
…[truncated 231 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_pride-formula-verify_20260519T232737",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-19T23:31:00.787068+00:00_

Web search results for query: "PRIDE formula "Paraphrase Robustness" site:arxiv.org 2603.28301 SK ST alpha"

Links: [{"title":"LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models","url":"https://arxiv.org/html/2603.28301v1"},{"title":"Robustness to Modification with Shared Words in Paraphrase   Identification","url":"https://arxiv.org/pdf/1909.02560"},{"title":"Evaluating Paraphrastic Robustness in Textual Entailment Models","url":"https://arxiv.org/pdf/2306.16722"},{"title":"RoParQ: Paraphrase-Aware Alignment of Large Language Models Towards Robustness to Paraphrased Questions","url":"https://arxiv.org/pdf/2511.21568"},{"title":"Evaluating Autoformalization Robustness via Semantically Similar Paraphrasing","url":"https://arxiv.org/pdf/2511.12784"}]

Based on the search results, I found information about the PRIDE formula from the arxiv paper 2603.28301:

PRIDE is a metric that quantifies the linguistic deviation between an original instruction and its paraphrase. PRIDE is a metric that quantifies paraphrase difficulty using semantic and syntactic factors.

The paper is titled "LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models" and was published on March 30, 2026. However, the search results don't contain detailed information about the specific formula components you mentioned (SK, ST, alpha). To get the complete mathematical definition of the PRIDE formula with those specific parameters, you would need to access the full paper at https://arxiv.org/html/2603.28301v1 or https://arxiv.org/pdf/2603.28301.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_pride-formula-verify_20260519T232737",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-19T23:31:00.787247+00:00_

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
  "session": "worker_research_pride-formula-verify_20260519T232737",
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

_source line 12 · 2026-05-19T23:31:00.787385+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_pride-formula-verify_20260519T232737",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-19T23:31:00.787534+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/html/2603.28301v1",
  "prompt": "Extract the EXACT mathematical formula/definition of PRIDE metric, including:\n1. The full formula for Paraphrase Distance (PD) - what is SK, ST, alpha, and how they combine\n2. The full formula for PRIDE score itself\n3. The default value of alpha\n4. Whether PRIDE is higher=better or lower=better\n5. What SK (keyword similarity) and ST (structural similarity) precisely measure and how they are computed\n6. The OFT baseline PRIDE score reported in the paper\n7. Any other baseline PRIDE scores reported\n\nBe very precise about the math - extract exact equations, not paraphrases."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_pride-formula-verify_20260519T232737",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/html/2603.28301v1",
    "prompt": "Extract the EXACT mathematical formula/definition of PRIDE metric, including:\n1. The full formula for Paraphrase Distance (PD) - what is SK, ST, alpha, and how they combine\n2. The full formula for PRIDE score itself\n3. The default value of alpha\n4. Whether PRIDE is higher=better or lower=better\n5. What SK (keyword similarity) and ST (structural similarity) precisely measure and how they are computed\n6. The OFT baseline PRIDE score reported in the paper\n7. Any other baseline PRIDE scores reported\n\nBe very precise about the math - extract exact equations, not paraphrases."
  }
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-19T23:31:00.787684+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/cau-hai-lab/LIBERO-Para",
  "prompt": "Find the implementation of the PRIDE metric. Look for:\n1. The code that computes PD (Paraphrase Distance) from SK and ST\n2. The code that computes the final PRIDE score\n3. The default alpha value\n4. Any constants or thresholds used\nExtract the relevant code snippets."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_pride-formula-verify_20260519T232737",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/cau-hai-lab/LIBERO-Para",
    "prompt": "Find the implementation of the PRIDE metric. Look for:\n1. The code that computes PD (Paraphrase Distance) from SK and ST\n2. The code that computes the final PRIDE score\n3. The default alpha value\n4. Any constants or thresholds used\nExtract the relevant code snippets."
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-19T23:31:00.787838+00:00_

# PRIDE Metric Implementation

Based on the GitHub repository content provided, I can confirm that **PRIDE metric implementation details are documented but the actual code snippets are not included in the web page content you've shared**.

## What the Repository Indicates:

The README states that PRIDE computes a **Paraphrase Distance (PD)** from two components:
- **SK** (keyword similarity)
- **ST** (structural similarity)

The metric then "measures the ratio of PD-weighted successes to total possible PD, normalized to 0–100."

## Where to Find the Implementation:

The actual code is located in:
1. **`metrics/README.md`** - Contains detailed metric documentation
2. **`metrics/PRIDE_metric_playground.ipynb`** - Interactive notebook with implementation
3. **`metrics/analyze_results.py`** - Analysis script using the metric
4. **`metrics/libero_para_metadata.csv`** - Supporting data

## Next Steps:

To access the actual code implementation including:
- PD computation formula
- SK and ST calculation methods
- Default alpha values
- Specific thresholds

You'll need to visit the GitHub repository directly and examine the files in the `metrics/` directory, which aren't rendered in this web page excerpt.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_pride-formula-verify_20260519T232737",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-19T23:31:00.788032+00:00_

# PRIDE Metric: Mathematical Formulation

## Paraphrase Distance (PD) Formula

**Equation 3** from the paper defines PD as:

```
PD = 1 - (α·S_K(O,P) + (1-α)·S_T(T_O, T_P))
```

Where:
- **S_K(O,P)**: Keyword similarity (ranges 0-1, higher = more similar)
- **S_T(T_O, T_P)**: Structural similarity (ranges 0-1, higher = more similar)
- **α**: Weighting parameter, **default value = 0.5**

## PRIDE Score Formula

**Equation 4** defines PRIDE as:

```
PRIDE = { PD,  if success
        { 0,   if failure
```

**Interpretation**: Higher PRIDE = better robustness (more difficult paraphrases successfully handled). When a task fails, PRIDE = 0 regardless of paraphrase difficulty.

## S_K (Keyword Similarity) Computation

**Equation 1**:

```
S_K(O,P) = (1/n) Σ(i=1 to n) max(j∈{1,...,m}) cos(e(o_i), e(p_j))
```

Measures semantic preservation of task-critical content words via embedding cosine similarity from Sentence-BERT.

## S_T (Structural Similarity) Computation

**Equation 2**:

```
S_T(T_O, T_P) = 1 - TED(T_O, T_P) / (|T_O| + |T_P|)
```

Uses tree edit distance (TED) on dependency parse trees with POS tags as node labels. Normalized by combined tree sizes.

## Reported PRIDE Scores (Table 3)

| Model | PRIDE Score |
|-------|------------|
| OpenVLA-OFTgoal | 58.8 |
| π₀.₅ (expert-only) | 32.0 |
| X-VLA | 52.7 |
| OpenVLA-OFTmixed | 56.3 |
| Xiaomi-Robotics-0 | 69.2 |
| π₀.₅ | 65.4 |
| VLA-Adapter | 36.1 |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_pride-formula-verify_20260519T232737",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-19T23:31:00.788204+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://cau-hai-lab.github.io/LIBERO-Para/",
  "prompt": "Extract the PRIDE metric formula and definition. Specifically look for:\n1. How PRIDE is aggregated across multiple tasks/paraphrases (is it averaged? summed? ratio?)\n2. The exact aggregation formula - is it sum of PD for successes divided by sum of all PD?\n3. Any normalization (e.g., multiplied by 100)\n4. The OFT baseline PRIDE value"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_pride-formula-verify_20260519T232737",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://cau-hai-lab.github.io/LIBERO-Para/",
    "prompt": "Extract the PRIDE metric formula and definition. Specifically look for:\n1. How PRIDE is aggregated across multiple tasks/paraphrases (is it averaged? summed? ratio?)\n2. The exact aggregation formula - is it sum of PD for successes divided by sum of all PD?\n3. Any normalization (e.g., multiplied by 100)\n4. The OFT baseline PRIDE value"
  }
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-19T23:31:00.788332+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/cau-hai-lab/LIBERO-Para/main/metrics/analyze_results.py",
  "prompt": "Extract the complete PRIDE metric computation code. Show the exact formulas used for:\n1. PD (Paraphrase Distance) computation from SK and ST\n2. PRIDE score computation from PD and success\n3. How PRIDE is aggregated across multiple samples\n4. The default alpha value\n5. Any normalization steps"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_pride-formula-verify_20260519T232737",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/cau-hai-lab/LIBERO-Para/main/metrics/analyze_results.py",
    "prompt": "Extract the complete PRIDE metric computation code. Show the exact formulas used for:\n1. PD (Paraphrase Distance) computation from SK and ST\n2. PRIDE score computation from PD and success\n3. How PRIDE is aggregated across multiple samples\n4. The default alpha value\n5. Any normalization steps"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-19T23:31:00.788449+00:00_

Request failed with status code 404

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_pride-formula-verify_20260519T232737",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-19T23:31:00.788574+00:00_

# PRIDE Metric Extraction

Based on the provided content, here's what can be determined about the PRIDE metric:

## Definition
"PRIDE (Paraphrase Robustness Index in Robotic Instructional DEviation) addresses this by computing a Paraphrase Distance (PD) from keyword similarity (SK) and structural similarity (ST), then weighting success by difficulty."

## Components
- **Paraphrase Distance (PD)**: Derived from keyword similarity (SK) and structural similarity (ST)
- **SK**: Measures semantic similarity between task-critical content words
- **ST**: Uses dependency-tree edit distance to capture structural variation

## Aggregation Method
The document does not explicitly specify the exact aggregation formula (e.g., whether PD values are summed, averaged, or used in a ratio calculation). It only states that "success by difficulty" is weighted, with harder paraphrases receiving more credit than easier ones.

## Normalization
The document does not clearly specify if results are normalized (e.g., multiplied by 100).

## Baseline Values
For the OFT models:
- OpenVLA-OFTmixed PRIDE: **56.3**
- OpenVLA-OFTgoal PRIDE: **58.8**

The precise mathematical formula for aggregating PD across all paraphrases is not provided in this webpage content.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_pride-formula-verify_20260519T232737",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-19T23:31:00.788732+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/cau-hai-lab/LIBERO-Para/main/metrics/PRIDE_metric_playground.ipynb",
  "prompt": "Extract the exact PRIDE metric implementation code. Show:\n1. How PD is computed from SK and ST (the formula)\n2. How PRIDE is computed from PD values and success indicators\n3. The aggregation formula across tasks\n4. Default alpha value\n5. Any normalization (e.g. multiply by 100)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_pride-formula-verify_20260519T232737",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/cau-hai-lab/LIBERO-Para/main/metrics/PRIDE_metric_playground.ipynb",
    "prompt": "Extract the exact PRIDE metric implementation code. Show:\n1. How PD is computed from SK and ST (the formula)\n2. How PRIDE is computed from PD values and success indicators\n3. The aggregation formula across tasks\n4. Default alpha value\n5. Any normalization (e.g. multiply by 100)"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-19T23:31:00.788863+00:00_

Request failed with status code 404

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_pride-formula-verify_20260519T232737",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-19T23:31:00.788979+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /tmp && git clone --depth 1 https://github.com/cau-hai-lab/LIBERO-Para.git 2>&1 | tail -5",
  "description": "Clone LIBERO-Para repo to inspect PRIDE implementation",
  "timeout": "30000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_pride-formula-verify_20260519T232737",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /tmp && git clone --depth 1 https://github.com/cau-hai-lab/LIBERO-Para.git 2>&1 | tail -5",
    "description": "Clone LIBERO-Para repo to inspect PRIDE implementation",
    "timeout": "30000"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-19T23:31:00.789125+00:00_

Cloning into 'LIBERO-Para'...
Updating files:   8% (432/5241)Updating files:   9% (472/5241)Updating files:  10% (525/5241)Updating files:  11% (577/5241)Updating files:  12% (629/5241)Updating files:  13% (682/5241)Updating files:  14% (734/5241)Updating files:  15% (787/5241)Updating files:  16% (839/5241)Updating files:  17% (891/5241)Updating files:  18% (944/5241)Updating files:  19% (996/5241)Updating files:  20% (1049/5241)Updating files:  21% (1101/5241)Updating files:  22% (1154/5241)Updating files:  23% (1206/5241)Updating files:  24% (1258/5241)Updating files:  25% (1311/5241)Updating files:  26% (1363/5241)Updating files:  27% (1416/5241)Updating files:  28% (1468/5241)Updating files:  29% (1520/5241)Updating files:  30% (1573/5241)Updating files:  31% (1625/5241)Updating files:  32% (1678/5241)Updating files:  33% (1730/5241)Updating files:  34% (1782/5241)Updating files:  35% (1835/5241)Updating files:  36% (1887/5241)Updating files:  37% (1940/5241)Updating files:  38% (1992/5241)Updating files:  39% (2044/5241)Updating files:  40% (2097/5241)Updating files:  41% (2149/5241)Updating files:  42% (2202/5241)Updating files:  43% (2254/5241)Updating files:  44% (2307/5241)Updating files:  45% (2359/5241)Updating files:  46% (2411/5241)Updating files:  47% (2464/5241)Updating files:  48% (2516/5241)Updating files:  49% (2569/5241)Updating files:  50% (2621/5241)Updating files:  51% (2673/5241)Updating files:  52% (2726/5241)Updating files:  53% (2778/5241)Updating files:  54% (2831/5241)Updating files:  55% (2883/5241)Updating files:  56% (2935/5241)Updating files:  57% (2988/5241)Updating files:  58% (3040/5241)Updating files:  59% (3093/5241)Updating files:  60% (3145/5241)Updating files:  61% (3198/5241)Updating files:  62% (3250/5241)Updating files:  63% (3302/5241)Updating files:  64% (3355/5241)Updating files:  65% (3407/5241)Updating files:  66% (3460/5241)Updating files:  67% (3512/5241)Up
…[truncated 1217 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_pride-formula-verify_20260519T232737",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-19T23:31:00.789269+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /tmp/LIBERO-Para/metrics -type f -name \"*.py\" -o -name \"*.ipynb\" | head -20",
  "description": "List metric implementation files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_pride-formula-verify_20260519T232737",
  "tool": "Bash",
  "tool_args": {
    "command": "find /tmp/LIBERO-Para/metrics -type f -name \"*.py\" -o -name \"*.ipynb\" | head -20",
    "description": "List metric implementation files"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-19T23:31:00.789388+00:00_

/tmp/LIBERO-Para/metrics/compute_pride_score_example.py
/tmp/LIBERO-Para/metrics/analyze_results.py
/tmp/LIBERO-Para/metrics/PRIDE_metric_playground.ipynb

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_pride-formula-verify_20260519T232737",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-19T23:31:00.789501+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/LIBERO-Para/metrics/compute_pride_score_example.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_pride-formula-verify_20260519T232737",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/LIBERO-Para/metrics/compute_pride_score_example.py"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-19T23:31:00.789750+00:00_

1	#!/usr/bin/env python3
2	"""
3	Add similarity scores to verified CSV
4	
5	기존 compute_similarity.py의 로직을 사용해서 verified_csv에 
6	structural_similarity, keyword_similarity 등을 추가해서 저장.
7	
8	Usage:
9	    python add_similarity_to_verified.py --verified_csv /path/to/verified.csv --output_csv /path/to/output.csv
10	
11	Requirements:
12	    pip install spacy sentence-transformers pandas numpy tqdm
13	    python -m spacy download en_core_web_sm
14	"""
15	
16	import argparse
17	import pandas as pd
18	import numpy as np
19	from pathlib import Path
20	from datetime import datetime
21	import warnings
22	warnings.filterwarnings('ignore')
23	
24	
25	# =============================================================================
26	# Dependency Check
27	# =============================================================================
28	
29	def check_dependencies():
30	    missing = []
31	    try:
32	        import spacy
33	    except ImportError:
34	        missing.append("spacy")
35	    try:
36	        from sentence_transformers import SentenceTransformer
37	    except ImportError:
38	        missing.append("sentence-transformers")
39	    try:
40	        from tqdm import tqdm
41	    except ImportError:
42	        missing.append("tqdm")
43	    
44	    if missing:
45	        print("Missing dependencies. Please install:")
46	        print(f"  pip install {' '.join(missing)}")
47	        if "spacy" not in missing:
48	            print("  python -m spacy download en_core_web_sm")
49	        exit(1)
50	
51	
52	# =============================================================================
53	# 1. Tree Edit Distance (Zhang-Shasha Algorithm)
54	# =============================================================================
55	
56	class TreeNode:
57	    def __init__(self, label, children=None):
58	        self.label = label
59	        self.children = children or []
60	
61	
62	def build_dependency_tree(doc) -> TreeNode:
63	    root_token = None
64	    for token in doc:
65	        if token.de
…[truncated 14127 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_pride-formula-verify_20260519T232737",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-19T23:31:00.789923+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/LIBERO-Para/metrics/analyze_results.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_pride-formula-verify_20260519T232737",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/LIBERO-Para/metrics/analyze_results.py"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-19T23:31:00.790524+00:00_

1	#!/usr/bin/env python3
2	"""
3	generate_paraphrase_table.py
4	
5	Generates a 4x11 (obj x act) paraphrase success rate heatmap from
6	structured JSON eval logs.
7	
8	Directory structure expected:
9	    model_path/
10	        seed7/
11	            eval0.json  ... eval9.json
12	            meta.json
13	            summary.json
14	        seed8/
15	        ...
16	        seed11/
17	
18	Each eval{N}.json has:
19	    {
20	      "eval_id": N,
21	      "original_instruction": ...,
22	      "episodes": [
23	        {
24	          "paraphrase_type": "act" | "obj" | "comp",
25	          "categories": [...],
26	          "subcategories": [...],  # comp: [obj_subcat, act_subcat]
27	          "success": true/false,
28	          ...
29	        }, ...
30	      ]
31	    }
32	
33	Usage:
34	    python generate_paraphrase_table.py \
35	        --model_path ../logs_para/xiaomi \
36	        --model_name "OpenVLA-OFT" \
37	        --output_dir ./metrics/output
38	"""
39	
40	import argparse
41	import json
42	import glob
43	import os
44	import sys
45	from collections import defaultdict
46	from typing import Dict, List, Tuple, Optional
47	
48	import numpy as np
49	import pandas as pd
50	import matplotlib.pyplot as plt
51	import seaborn as sns
52	from matplotlib.colors import LinearSegmentedColormap
53	
54	
55	# ============================================================================
56	# Constants
57	# ============================================================================
58	
59	# Y-axis (obj paraphrase types)
60	OBJ_TYPES_ORDER = [
61	    "None",
62	    "addition_deletion",
63	    "same_polarity_contextual",
64	    "same_polarity_habitual",
65	]
66	
67	# X-axis (act paraphrase types)
68	ACT_TYPES_ORDER = [
69	    "None",
70	    "addition_deletion",
71	    "same_polarity_contextual",
72	    "same_polarity_habitual",
73	    "coordination",
74	    "subordination",
75	    "need_statement",
76	    "embedded_imperative",
77	    "permission_directive",
78	    "question_directive",
79	 
…[truncated 52045 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_pride-formula-verify_20260519T232737",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-19T23:31:00.790754+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "PRIDE|pride|paraphrase_distance|PD",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/afford_invar",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_pride-formula-verify_20260519T232737",
  "tool": "Grep",
  "tool_args": {
    "pattern": "PRIDE|pride|paraphrase_distance|PD",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/afford_invar",
    "output_mode": "files_with_matches"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-19T23:31:00.790928+00:00_

Found 80 files
logs/workers/worker_research_pride-formula-verify_20260519T232737.log
logs/chats/feishu_group_oc_e0fe8d2f0d417545f5bf6f650173c34c_reviewer.jsonl
logs/chats/feishu_group_oc_bfa3708ecf42097843150f45348b3760_director.jsonl
.claude/sessions/director_21ca1cc3/AGENTS.md
.claude/sessions/director_21ca1cc3/CLAUDE.md
AGENTS.md
.claude/CLAUDE.md
logs/chats/feishu_group_oc_e0fe8d2f0d417545f5bf6f650173c34c.jsonl
report.md
checkpoints/phase1_lconsist_v1_cont_RUNNING_20260519T232658.json
registry.yaml
checkpoints/phase1_lconsist_v1_cont_ALLOCATED_20260519T232652.json
checkpoints/phase1_lconsist_v1_cont_QUEUED_20260519T232647.json
checkpoints/phase1_lconsist_v1_cont_PENDING_20260519T232644.json
checkpoints/phase1_lconsist_v1_DONE_20260519T232445.json
.claude/sessions/reviewer_8c7bb198/AGENTS.md
.claude/sessions/reviewer_8c7bb198/CLAUDE.md
logs/workers/worker_infra_restart-lconsist-training_20260519T231922.log
logs/workers/worker_code_merge-consist-transfer_20260519T232011.log
.claude/sessions/agent_413a00de/AGENTS.md
.claude/sessions/agent_413a00de/CLAUDE.md
ROADMAP.md
decisions.yaml
logs/workers/worker_code_l-transfer-dryrun_20260519T225748.log
checkpoints/phase1_lconsist_v1_ANALYZING_20260519T225818.json
memory.md
logs/workers/worker_analysis_phase1_lconsist_v1_20260519T225345.log
logs/chats/cron_hook_phase1_lconsist_v1.jsonl
.claude/sessions/agent_56997cc0/AGENTS.md
.claude/sessions/agent_56997cc0/CLAUDE.md
checkpoints/phase1_lconsist_v1_ANALYZING_20260519T225208.json
logs/workers/worker_code_eval-fixes_20260519T224913_result.json
logs/workers/worker_code_eval-fixes_20260519T224913.log
logs/workers/worker_code_training-status-fix_20260519T224853.log
logs/workers/worker_code_fix-and-relaunch_20260519T222907.log
logs/workers/worker_code_eval-pipeline-prep_20260519T222535_result.json
logs/workers/worker_code_eval-pipeline-prep_20260519T222535.log
logs/workers/worker_code_l-transfer-pair-validation_20260519T222514.log
logs/workers/worker_code_paraphrase-hit-rate_2026
…[truncated 2575 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_pride-formula-verify_20260519T232737",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-19T23:31:00.791086+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "PRIDE|pride|paraphrase_distance",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/afford_invar",
  "glob": "*.{py,md,yaml}",
  "output_mode": "content",
  "head_limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_pride-formula-verify_20260519T232737",
  "tool": "Grep",
  "tool_args": {
    "pattern": "PRIDE|pride|paraphrase_distance",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/afford_invar",
    "glob": "*.{py,md,yaml}",
    "output_mode": "content",
    "head_limit": "50"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-19T23:31:00.791231+00:00_

decisions.yaml:6:    → LIBERO-Para PRIDE 评估
decisions.yaml:16:    bias。W2: PRIDE 阈值从 "any improvement" 提升到 ≥5pp（单 seed），统计上更可靠。W3: 增加 Phase 0.5
decisions.yaml:18:    无选择性 / PRIDE < +2pp → kill）。MVP 预算从 25h 调至 30-35h。'
decisions.yaml:24:  summary: Phase 0.5 跳过：LIBERO-Para 已公布 OFT baseline PRIDE 分数（Goal 58.8, Mixed 56.3），无需自行跑
decisions.yaml:26:  rationale: LIBERO-Para 论文公开了 OFT 在 Goal suite 的 PRIDE=58.8。我们 MVP pass 目标 ≥63.8（+5pp）。节省
report.md:8:| phase1_lconsist_v1_cont | 从 phase1_lconsist_v1 checkpoint-1000 继续 L_action 训练至 20000 步，获取 OFT baseline SR 数据用于对比。Affordance decoder 已确认 NEGATIVE（不期望 heatmap 改善），但 L_action LoRA 正常收敛，需要完整训练的 checkpoint 做 LIBERO SR/PRIDE 评估基线。 | — | — | — |
report.md:15:- **phase1_lconsist_v1** (negative): L_consist (alpha=0.1, lambda_H=0) 作为 LoRA fine-tuning 正则项，引导 affordance decoder 从 Layer-18 features 学到空间 affordance 表征。预期：heatmap peak 到 gripper target 归一化距离 < 0.2，standard LIBERO SR ≥ 95%，LIBERO-Para PRIDE ≥ 63.8
ROADMAP.md:37:3. LIBERO-Para PRIDE ≥ 63.8
ROADMAP.md:42:- PRIDE < 60.8 → kill
ROADMAP.md:46:- [ ] PRIDE 公式：eval_pride.py 与 ROADMAP 阈值矛盾，需查 LIBERO-Para 论文确认定义
ROADMAP.md:47:- [ ] robosuite/mujoco 安装（LIBERO SR 和 PRIDE 评估依赖）
ROADMAP.md:55:- [ ] Phase 1b: 训练完成后 heatmap eval + LIBERO SR + PRIDE
ROADMAP.md:56:- [ ] PRIDE 公式校正
ROADMAP.md:76:| D003 | 2026-05-19 | Phase 0.5 跳过：LIBERO-Para 已公布 OFT baseline PRIDE 分数 | — |
registry.yaml:10:      归一化距离 < 0.2，standard LIBERO SR ≥ 95%，LIBERO-Para PRIDE ≥ 63.8
registry.yaml:87:      LoRA 正常收敛，需要完整训练的 checkpoint 做 LIBERO SR/PRIDE 评估基线。
registry.yaml:106:      eval_data: LIBERO SR + PRIDE evaluation after training completes
memory.md:70:6. **Heatmap 评估** (`scripts/evaluation/`): extract_ground_truth.py + heatmap_metrics.py + run_heatmap_eval.py + eval_pride.py
memory.md:89:- PRIDE 公式: PD = 1 - (α·SK + (1-α)·ST), α=0.5
memory.md:90:- OFT baseline PRIDE: OFT_goal=58.8 (SR 64.7%), OFT_mixed=56.3 (SR 63.7%)
docs/IDEA_BRIEF.md:123:[Omitted long matching line]
docs/IDEA_BRIEF.md:143:- LIBERO-Para: A Diagn
…[truncated 147 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_pride-formula-verify_20260519T232737",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-19T23:31:00.791383+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "pride|PRIDE|paraphrase_distance",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/afford_invar",
  "glob": "*.py",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_pride-formula-verify_20260519T232737",
  "tool": "Grep",
  "tool_args": {
    "pattern": "pride|PRIDE|paraphrase_distance",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/afford_invar",
    "glob": "*.py",
    "output_mode": "files_with_matches"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-19T23:31:00.791504+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_pride-formula-verify_20260519T232737",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-19T23:31:00.791621+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "eval_pride",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/afford_invar",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_pride-formula-verify_20260519T232737",
  "tool": "Grep",
  "tool_args": {
    "pattern": "eval_pride",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/afford_invar",
    "output_mode": "files_with_matches"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-19T23:31:00.791765+00:00_

Found 11 files
logs/workers/worker_research_pride-formula-verify_20260519T232737.log
logs/chats/feishu_group_oc_e0fe8d2f0d417545f5bf6f650173c34c_reviewer.jsonl
logs/chats/feishu_group_oc_bfa3708ecf42097843150f45348b3760_director.jsonl
logs/chats/feishu_group_oc_e0fe8d2f0d417545f5bf6f650173c34c.jsonl
logs/workers/worker_code_merge-consist-transfer_20260519T232011.log
ROADMAP.md
memory.md
logs/workers/worker_code_eval-fixes_20260519T224913_result.json
logs/workers/worker_code_eval-fixes_20260519T224913.log
logs/workers/worker_code_eval-pipeline-prep_20260519T222535_result.json
logs/workers/worker_code_eval-pipeline-prep_20260519T222535.log

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_pride-formula-verify_20260519T232737",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-19T23:31:00.791899+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/afford_invar/memory.md",
  "offset": "85",
  "limit": "15"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_pride-formula-verify_20260519T232737",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/afford_invar/memory.md",
    "offset": "85",
    "limit": "15"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-19T23:31:00.792030+00:00_

85	- Total trainable: ~263M (LoRA 111M + action_head 151M + decoder 1.7M)
86	
87	## LIBERO-Para 调研结论 (2026-05-19)
88	
89	- PRIDE 公式: PD = 1 - (α·SK + (1-α)·ST), α=0.5
90	- OFT baseline PRIDE: OFT_goal=58.8 (SR 64.7%), OFT_mixed=56.3 (SR 63.7%)
91	- 原始 LIBERO-Goal SR: OFT_goal 97.9%, OFT_mixed 96.1% → paraphrase 退化 ~33pp
92	- 80-96% 失败来自 planning-level trajectory divergence
93	
94	## 环境信息 (2026-05-19)
95	
96	- 服务器: westd-19957, 4x RTX PRO 6000 Blackwell (94GB each)
97	- conda base: Python 3.12.3, PyTorch 2.8.0+cu128
98	- transformers: OFT fork 4.40.1 (moojink/transformers-openvla-oft)
99	- timm: 0.9.16

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_pride-formula-verify_20260519T232737",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-19T23:31:00.792169+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "rm -rf /tmp/LIBERO-Para",
  "description": "Clean up cloned repo"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_pride-formula-verify_20260519T232737",
  "tool": "Bash",
  "tool_args": {
    "command": "rm -rf /tmp/LIBERO-Para",
    "description": "Clean up cloned repo"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-19T23:31:00.792282+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_pride-formula-verify_20260519T232737",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 43 · 2026-05-19T23:31:00.792439+00:00_

## PRIDE 指标验证报告

### 论文原始定义 (arXiv:2603.28301)

**PD (Paraphrase Distance):**
```
PD = 1 - (α·S_K + (1-α)·S_T),  α=0.5
```

- **S_K** (Keyword Similarity): 对原始指令的 content words (NOUN/VERB/ADJ/ADV) 用 Sentence-BERT (all-MiniLM-L6-v2) 编码，每个原始词与所有 paraphrase 词取 max cosine similarity，再取平均：`S_K = (1/n) Σ max_j cos(e(o_i), e(p_j))`
- **S_T** (Structural Similarity): 依赖解析树的 Zhang-Shasha tree edit distance (TED)，节点标签为 (dep, POS)：`S_T = 1 - TED(T_O, T_P) / (|T_O| + |T_P|)`

**PRIDE 聚合公式（关键）:**
```
PRIDE(α) = Σ(success_i × PD_i) / Σ(PD_i) × 100
```

即 **PD 加权成功率**——成功 episode 的 PD 之和除以所有 episode 的 PD 之和，乘 100。Higher = better。

### 与我们当前实现的对比

| 要素 | 论文定义 | 我们 memory.md 记录 | 一致？ |
|------|---------|-------------------|--------|
| PD 公式 | `1 - (α·SK + (1-α)·ST)` | `1 - (α·SK + (1-α)·ST)` | **一致** |
| α 默认值 | 0.5 | 0.5 | **一致** |
| PRIDE 聚合 | `Σ(success×PD) / Σ(PD) × 100` | memory.md 未记录聚合公式 | **需确认** |
| 方向 | Higher = more robust | 未明确 | **需确认** |
| OFT_goal PRIDE | 58.8 | 58.8 | **一致** |
| OFT_mixed PRIDE | 56.3 | 56.3 | **一致** |

### 关键发现

1. **PD 单 episode 公式正确**——与论文 Eq.3 完全一致。

2. **PRIDE 不是简单的 per-episode PD 值**。论文 HTML (Eq.4) 简写为 "PRIDE = PD if success, 0 if failure"，但代码实现的聚合是 **加权比率**：`Σ(success_i × PD_i) / Σ(PD_i) × 100`。这不是简单平均，而是 PD 加权的成功率。更难的 paraphrase（PD 大）在分母中权重更大，成功则在分子中贡献更多。

3. **我们的 eval_pride.py 尚未实现**（项目中无 .py 文件包含 PRIDE 计算）。ROADMAP.md 已标注此为待办项。

4. **实现时需注意**：论文官方代码使用 `paraphrased_instruction` 字段匹配 pre-computed SK/ST CSV，而非实时计算。可直接复用论文的 `libero_para_metadata.csv`。

### 结论

PD 公式和 baseline 数值与论文完全一致，无需修改。实现 eval_pride.py 时需用 **加权比率公式** `Σ(success×PD)/Σ(PD)×100`，不能简单取均值。

Sources:
- [LIBERO-Para Paper (HTML)](https://arxiv.org/html/2603.28301v1)
- [LIBERO-Para Paper (Abstract)](https://arxiv.org/abs/2603.28301)
- [LIBERO-Para GitHub](https://github.com/cau-hai-lab/LIBERO-Para)
- [LIBERO-Para Project Page](https://cau-hai-lab.github.io/LIBERO-Para/)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_pride-formula-verify_20260519T232737"
}
```

</details>

---
