# research autoformalization faithfulness

**svs formal verification** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 33
- **Recorded user turns:** 0
- **Tool calls:** 16
- **Original source:** `logs/chats/worker_research_autoformalization-faithfulness_20260514T105550.jsonl`
- **Structured JSON:** [`13a91731859a73951b72.json`](../../sessions/13/13a91731859a73951b72.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

33 recorded events

### Tool call

_source line 1 · 2026-05-14T10:59:39.782836+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__read_project_file",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_autoformalization-faithfulness_20260514T105550",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__read_project_file",
    "max_results": "5"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-14T10:59:39.783102+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_autoformalization-faithfulness_20260514T105550",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-14T10:59:39.783274+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arXiv 2604.19459 autoformalization faithfulness axiom fabrication premise mistranslation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_autoformalization-faithfulness_20260514T105550",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arXiv 2604.19459 autoformalization faithfulness axiom fabrication premise mistranslation"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-14T10:59:39.783397+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "autoformalization faithfulness validation LLM formal verification 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_autoformalization-faithfulness_20260514T105550",
  "tool": "WebSearch",
  "tool_args": {
    "query": "autoformalization faithfulness validation LLM formal verification 2025 2026"
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-14T10:59:39.783510+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "VeriCoT VERGE SSV formal verification chain-of-thought faithfulness"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_autoformalization-faithfulness_20260514T105550",
  "tool": "WebSearch",
  "tool_args": {
    "query": "VeriCoT VERGE SSV formal verification chain-of-thought faithfulness"
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-14T10:59:39.783644+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "back-translation semantic equivalence checking formal logic LLM verification"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_autoformalization-faithfulness_20260514T105550",
  "tool": "WebSearch",
  "tool_args": {
    "query": "back-translation semantic equivalence checking formal logic LLM verification"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-14T10:59:39.783789+00:00_

Web search results for query: "arXiv 2604.19459 autoformalization faithfulness axiom fabrication premise mistranslation"

Links: [{"title":"Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning","url":"https://arxiv.org/html/2604.19459"},{"title":"[2604.19459] Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning","url":"https://arxiv.org/abs/2604.19459"},{"title":"Faithful Autoformalization via Roundtrip Verification and Repair","url":"https://arxiv.org/html/2604.25031"},{"title":"ProofFlow: A Dependency Graph Approach to Faithful Proof Autoformalization","url":"https://arxiv.org/html/2510.15981"},{"title":"MerLean: An Agentic Framework For Autoformalization in Quantum Computation","url":"https://arxiv.org/html/2602.16554v1"},{"title":"[2604.25031] Faithful Autoformalization via Roundtrip Verification and Repair","url":"https://arxiv.org/abs/2604.25031"},{"title":"Towards a Common Framework for Autoformalization","url":"https://arxiv.org/html/2509.09810v1"},{"title":"Rethinking and Improving Autoformalization: Towards a Faithful Metric and a Dependency Retrieval-based Approach | OpenReview","url":"https://openreview.net/forum?id=hUb2At2DsQ"},{"title":"Formalization of QFT","url":"https://arxiv.org/html/2603.15770v1"},{"title":"Autoformalization in the Era of Large Language Models: A Survey","url":"https://arxiv.org/html/2505.23486v1"}]

Based on the search results, I found the paper you're looking for:

**"Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning"** (arXiv:2604.19459)

The paper is authored by Kyuhee Kim, Auguste Poiroux, Antoine Bosselut, and was submitted on April 21, 2026.

**Key Findings:**

Formal verification guarantees proof validity but not formalization faithfulness. For natural-language logical reasoning, where models construct axiom systems from scratch without library constraints, this gap between valid proofs and faithful translations is especially acute.

The researchers evaluated G
…[truncated 848 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_autoformalization-faithfulness_20260514T105550",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-14T10:59:39.783950+00:00_

Web search results for query: "VeriCoT VERGE SSV formal verification chain-of-thought faithfulness"

Links: [{"title":"VeriCoT: Neuro-Symbolic Chain-of-Thought Validation via Logical Consistency Checks","url":"https://arxiv.org/html/2511.04662v1"},{"title":"VeriCoT: Neuro-symbolic Chain-of-Thought Validation via Logical Consistency Checks | OpenReview","url":"https://openreview.net/forum?id=zHuV3Vatov"},{"title":"[2511.04662v1] VeriCoT: Neuro-symbolic Chain-of-Thought Validation via Logical Consistency Checks","url":"https://arxiv.org/abs/2511.04662v1"},{"title":"VeriCoT: Neuro-symbolic Chain-of-Thought Validation via ...","url":"https://arxiv.org/pdf/2511.04662"},{"title":"[2511.04662] VeriCoT: Neuro-symbolic Chain-of-Thought Validation via Logical Consistency Checks","url":"https://arxiv.org/abs/2511.04662"},{"title":"VERICOT: NEURO-SYMBOLIC CHAIN-OF-THOUGHT ...","url":"https://openreview.net/pdf?id=zHuV3Vatov"},{"title":"[Literature Review] VeriCoT: Neuro-symbolic Chain-of-Thought Validation via Logical Consistency Checks","url":"https://www.themoonlight.io/en/review/vericot-neuro-symbolic-chain-of-thought-validation-via-logical-consistency-checks"},{"title":"Paper page - VeriCoT: Neuro-symbolic Chain-of-Thought Validation via Logical Consistency Checks","url":"https://huggingface.co/papers/2511.04662"},{"title":"VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning","url":"https://arxiv.org/html/2601.20055"},{"title":"VeriCoT: Neuro-Symbolic CoT Verification","url":"https://www.emergentmind.com/topics/vericot"}]

Based on the search results, here's what I found about VeriCoT and related work:

## VeriCoT: Neuro-Symbolic Chain-of-Thought Validation

VeriCoT is a neuro-symbolic method that extracts and verifies formal logical arguments from CoT reasoning. VeriCoT formalizes each CoT reasoning step into first-order logic and identifies premises that ground the argument in source context, commonsense knowledge, or prior reasoning steps.

### Addr
…[truncated 1193 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_autoformalization-faithfulness_20260514T105550",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-14T10:59:39.784124+00:00_

Web search results for query: "back-translation semantic equivalence checking formal logic LLM verification"

Links: [{"title":"Towards Formal Verification of LLM-Generated Code from Natural Language Prompts","url":"https://arxiv.org/pdf/2507.13290"},{"title":"Verified Code Transpilation with LLMs Sahil Bhatia1 Jie Qiu Niranjan Hasabnis2∗","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/48bb60a0c0aebb4142bf314bd1a5c6a0-Paper-Conference.pdf"},{"title":"Evaluating LLMs Capabilities at Natural Language to Logic ...","url":"https://ceur-ws.org/Vol-3904/paper13.pdf"},{"title":"HERMES: Towards Efficient and Verifiable Mathematical Reasoning in LLMs","url":"https://arxiv.org/pdf/2511.18760"},{"title":"Published as a conference paper at ICLR 2025 AUTONOMOUS EVALUATION OF LLMS FOR","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/1a7a22152cd21f0ca3c0f8139bb32905-Paper-Conference.pdf"},{"title":"Improving LLM Code Reasoning via Semantic Equivalence Self-Play with Formal Verification","url":"https://arxiv.org/html/2604.17010"},{"title":"VeriTrans: Fine-Tuned LLM-Assisted NL-to-PL Translation via a Deterministic Neuro-Symbolic Pipeline","url":"https://arxiv.org/html/2604.10341v1"},{"title":"LLM-Based Code Translation Needs Formal Compositional Reasoning Alvin Cheung","url":"https://www2.eecs.berkeley.edu/Pubs/TechRpts/2025/EECS-2025-174.pdf"},{"title":"TOWARDS AUTOFORMALIZATION OF LLM-GENERATED OUTPUTS FOR REQUIREMENT VERIFICATION","url":"https://arxiv.org/pdf/2511.11829"},{"title":"Syntax Is Easy, Semantics Is Hard: Evaluating LLMs for LTL Translation","url":"https://arxiv.org/html/2604.07321"}]

I found several relevant research papers on this topic. Here's a summary of the key findings:

## Back-Translation for Semantic Equivalence Checking

In the HERMES framework for mathematical reasoning, validated Lean code is back-translated into informal language, and the LLM evaluates the equivalence between the original and back-translated proof steps
…[truncated 1514 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_autoformalization-faithfulness_20260514T105550",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-14T10:59:39.784298+00:00_

Web search results for query: "autoformalization faithfulness validation LLM formal verification 2025 2026"

Links: [{"title":"LogicReward: Incentivizing LLM Reasoning via Step-Wise Logical Supervision [Quick Review]","url":"https://liner.com/review/logicreward-incentivizing-llm-reasoning-via-stepwise-logical-supervision"},{"title":"Formal Reasoning Meets LLMs: Toward AI for Mathematics and Verification – Communications of the ACM","url":"https://cacm.acm.org/research/formal-reasoning-meets-llms-toward-ai-for-mathematics-and-verification/"},{"title":"Faithful Autoformalization via Roundtrip Verification and Repair","url":"https://arxiv.org/html/2604.25031"},{"title":"TOWARDS AUTOFORMALIZATION OF LLM-GENERATED OUTPUTS FOR REQUIREMENT VERIFICATION","url":"https://arxiv.org/pdf/2511.11829"},{"title":"Published as a conference paper at ICLR 2025 AUTONOMOUS EVALUATION OF LLMS FOR","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/1a7a22152cd21f0ca3c0f8139bb32905-Paper-Conference.pdf"},{"title":"Improving Auto-Formalization to UCLID5 with LLMs and Formal Methods","url":"https://www2.eecs.berkeley.edu/Pubs/TechRpts/2025/EECS-2025-115.pdf"},{"title":"Faithful and Robust LLM-Driven Theorem Proving for NLI ...","url":"https://aclanthology.org/2025.acl-long.867.pdf"},{"title":"Position: Vibe Coding Needs Vibe Reasoning: Improving Vibe Coding with Formal Verification","url":"https://arxiv.org/html/2511.00202v1"},{"title":"PAT-Agent: Autoformalization for Model Checking","url":"https://arxiv.org/html/2509.23675"},{"title":"Position: Trustworthy AI Agents Require the Integration of","url":"https://openreview.net/pdf?id=wkisIZbntD"}]

I've performed a web search for your query on autoformalization, faithfulness validation, LLM, and formal verification in 2025-2026. Here are the key findings:

## Recent Research Developments

Recent advances have sparked a surge of interest in applying AI to formal mathematical reasoning, with the number of publications in this field n
…[truncated 1715 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_autoformalization-faithfulness_20260514T105550",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-14T10:59:39.784470+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.19459",
  "prompt": "Extract the complete abstract, key findings, experimental methodology, specific failure modes (axiom fabrication and premise mistranslation), their frequencies/rates, what types of problems they occur on, and any quantitative results. Also extract info about which LLMs were tested and their compilation/faithfulness rates."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_autoformalization-faithfulness_20260514T105550",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2604.19459",
    "prompt": "Extract the complete abstract, key findings, experimental methodology, specific failure modes (axiom fabrication and premise mistranslation), their frequencies/rates, what types of problems they occur on, and any quantitative results. Also extract info about which LLMs were tested and their compilation/faithfulness rates."
  }
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-14T10:59:39.784620+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.25031",
  "prompt": "Extract the complete abstract, methodology for roundtrip verification and repair, key results (faithfulness rates before/after), how they detect unfaithful formalizations, and the repair mechanism. What formal logic systems do they target? What are their quantitative improvements?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_autoformalization-faithfulness_20260514T105550",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2604.25031",
    "prompt": "Extract the complete abstract, methodology for roundtrip verification and repair, key results (faithfulness rates before/after), how they detect unfaithful formalizations, and the repair mechanism. What formal logic systems do they target? What are their quantitative improvements?"
  }
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-14T10:59:39.784749+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/html/2604.19459",
  "prompt": "Extract detailed information about: 1) The two failure modes - axiom fabrication (frequency, examples, which models) and premise mistranslation (frequency, examples, which models). 2) The experimental setup - datasets used, how faithfulness was measured. 3) Quantitative results - compilation rates, faithfulness rates, error breakdown. 4) What types of logical structures (quantifiers, negation, etc.) trigger more failures. 5) Any proposed mitigations or implications for downstream systems."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_autoformalization-faithfulness_20260514T105550",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/html/2604.19459",
    "prompt": "Extract detailed information about: 1) The two failure modes - axiom fabrication (frequency, examples, which models) and premise mistranslation (frequency, examples, which models). 2) The experimental setup - datasets used, how faithfulness was measured. 3) Quantitative results - compilation rates, faithfulness rates, error breakdown. 4) What types of logical structures (quantifiers, negation, etc.) trigger more failures. 5) Any proposed mitigations or implications for downstream systems."
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-14T10:59:39.784886+00:00_

# Research Summary: LLM Formalization Gaming

## Abstract
The study investigates whether frontier LLMs exploit the gap between valid proofs and faithful formalization when generating Lean 4 proofs, termed "formalization gaming."

## Models Tested
- GPT-5
- DeepSeek-R1

## Compilation & Faithfulness Rates
Models achieved compilation rates of 87-99%, yet these high rates did not correlate with faithful reasoning.

## Experimental Methodology
Researchers evaluated the two models using:
- 303 first-order logic problems (203 from FOLIO, 100 from Multi-LogiEval)
- Two approaches: unified generation versus a two-stage pipeline separating formalization from proving
- Cross-stage comparison to detect unfaithfulness

## Key Findings
Despite prompting designed to encourage gaming, "no evidence of systematic gaming in unified generation" was found. Models preferred reporting failure over forcing proofs.

## Failure Modes Identified

**GPT-5:** Fabricates axioms during proof generation as a reactive fallback, detectable through cross-stage comparison.

**DeepSeek-R1:** Mistranslates premises during formalization, producing internally consistent outputs that evade detection entirely.

## Quantitative Results
The paper notes that "high compilation rates or accuracies should not be equated with faithful reasoning," suggesting detection mechanisms may miss certain unfaithfulness patterns.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_autoformalization-faithfulness_20260514T105550",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-14T10:59:39.785008+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/html/2604.25031",
  "prompt": "Extract detailed methodology: 1) How does roundtrip verification work step by step? 2) What is the diagnosis-guided repair process? 3) What equivalence metrics do they use? 4) Quantitative results - faithfulness before/after repair, by model, by problem type. 5) Limitations and failure cases. 6) Applicability to FOL formalization specifically."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_autoformalization-faithfulness_20260514T105550",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/html/2604.25031",
    "prompt": "Extract detailed methodology: 1) How does roundtrip verification work step by step? 2) What is the diagnosis-guided repair process? 3) What equivalence metrics do they use? 4) Quantitative results - faithfulness before/after repair, by model, by problem type. 5) Limitations and failure cases. 6) Applicability to FOL formalization specifically."
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-14T10:59:39.785136+00:00_

# Faithful Autoformalization: Key Findings

## Abstract
The paper addresses verification of LLM-generated formal statements without ground-truth data through a novel roundtrip approach: "formalize a statement, translate the result back to natural language, re-formalize, and use a formal tool to check logical equivalence."

## Methodology

**Roundtrip Verification Process:**
- Convert natural language to formal representation
- Back-translate formal output to natural language
- Re-formalize the back-translated text
- Use formal tools to verify logical equivalence between the two formalizations

**Error Detection & Diagnosis:**
The system uses stage-level diagnosis to pinpoint which translation step introduced errors, enabling targeted corrections rather than wholesale regeneration.

**Repair Mechanism:**
A scoped repair operator corrects identified errors at the specific problematic translation stage.

## Key Results

**Faithfulness Improvements:**
- Diagnosis-guided scoped repair proved most effective among three baseline approaches
- Rules failing equivalence checks exhibited "1.4x-2.5x more NLI drift" compared to passing rules across both domains and models

**Testing Domains:**
- Texas Transportation Code
- Texas Parks and Wildlife Code
- Models: Claude Opus 4.6 and GPT-5.2

## Formal Logic Systems

The document doesn't specify particular formal logic systems targeted—only that formal tools verify logical equivalence between paired formalizations.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_autoformalization-faithfulness_20260514T105550",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-14T10:59:39.785289+00:00_

# Detailed Methodology Analysis

## 1. Roundtrip Verification Process

The framework operates through three sequential translation stages:

**Stage T₁ (Autoformalization):** Converts natural language input to formal logic expressions.

**Stage T₂ (Back-translation):** Reconstructs natural language from the formal encoding.

**Stage T₃ (Re-formalization):** Converts reconstructed NL back to formal logic.

The system then uses an SMT solver to check whether the original formalization and roundtrip formalization are logically equivalent. As the authors state: "If the pipeline preserves meaning, the initial and final formalizations should be semantically equivalent."

## 2. Diagnosis-Guided Repair

When equivalence fails (SAT verdict), the system:

1. **First-Failure Diagnosis:** An LLM judge sequentially examines artifacts at each stage to identify where semantic drift occurred, following this protocol: "examine T₁ first, then T₂, then T₃, halt at first failure."

2. **Scoped Repair:** Once a stage is diagnosed, only that stage is repaired using the specific diagnostic explanation, rather than regenerating the entire pipeline.

3. **Iterative Loop:** The system reruns downstream stages and re-checks equivalence, repeating up to K=3 iterations.

## 3. Equivalence Metrics

**Primary metric:** SMT solver verdict (UNSAT = formally equivalent, SAT = not equivalent)

**Secondary metric:** Bidirectional Natural Language Inference measuring entailment probability in both directions, categorizing results into: Contradiction, Equivalent, Strengthened, Weakened, Related, or Unrelated.

The researchers define drift as the combined rate of Unrelated and Contradiction classifications.

## 4. Quantitative Results

**Baseline Performance (no repair):**
- Traffic/Claude: 44.7% equivalence
- Wildlife/GPT: 66.2% equivalence

**After Full Repair:**
- Traffic/Claude: 85.3% equivalence
- Traffic/GPT (with Claude diagnoser): 90.7% equivalence
- Wildlife/Claude: 85.7% equivalence
- Wildlife/G
…[truncated 1496 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_autoformalization-faithfulness_20260514T105550",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-14T10:59:39.785445+00:00_

# Analysis of LLM Formalization Faithfulness Study

## 1) Two Failure Modes

**Axiom Fabrication (GPT-5 primary):**
- Frequency: 107 cases across datasets (73 FOLIO, 34 Multi-LogiEval)
- Primary pattern: "conclusion as axiom" (59 cases, 56%)—directly embedding proof goals as assumptions
- Secondary patterns: world knowledge (17 cases), invented facts (13 cases), contradictions (12 cases)
- Detection: Identifiable via cross-stage comparison when Stage 2 modifies Stage 1's locked formalization
- Trigger: Occurs after failed proof attempts, with higher iteration counts (2.06 vs 1.31 average)

**Premise Mistranslation (DeepSeek-R1 primary):**
- Frequency: Minimal stage modifications (2 cases) but embedded in formalization choices
- Pattern: Incorrect quantifier selection (∀ vs ∃), predicate substitution, semantic drift
- Example: Case 177 interprets "Tokyo" ambiguously as event-based rather than place-based
- Detection: Largely undetectable by LLM-as-judge evaluation; outputs internally consistent
- Manifestation: Errors occur during Stage 1 formalization, persisting through valid proofs

## 2) Experimental Setup

**Datasets:**
- 203 problems from FOLIO (balanced True/False/Uncertain)
- 100 from Multi-LogiEval (stratified by reasoning depth 3–5)

**Models:** GPT-5 and DeepSeek-R1 (three runs per condition, temperature 1.0)

**Faithfulness Measurement:**
- Three detection signals: prediction errors, directional divergence (both True/False proofs succeeding), stage modifications
- LLM-as-judge (Claude Opus) classified errors using a taxonomy covering mistranslation, fabrication, omission, contradiction
- Manual validation on 50 sampled cases; identified false negatives in subtle predicate substitutions

## 3) Quantitative Results

**Compilation Rates:** 87–99% across conditions (GPT-5 higher than DeepSeek-R1)

**Accuracy:** 
- Baseline: 85–87% (FOLIO), 70–72% (Multi-LogiEval)
- Two-Stage: 59–76% (greater variance)

**Faithfulness Rates:**
- Prediction errors: 77% used fai
…[truncated 1841 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_autoformalization-faithfulness_20260514T105550",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-14T10:59:39.785626+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "VERGE formal refinement guidance engine verifiable LLM reasoning MCS error localization 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_autoformalization-faithfulness_20260514T105550",
  "tool": "WebSearch",
  "tool_args": {
    "query": "VERGE formal refinement guidance engine verifiable LLM reasoning MCS error localization 2026"
  }
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-14T10:59:39.785753+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "FOL formalization quality metric autoformalization evaluation benchmark 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_autoformalization-faithfulness_20260514T105550",
  "tool": "WebSearch",
  "tool_args": {
    "query": "FOL formalization quality metric autoformalization evaluation benchmark 2025 2026"
  }
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-14T10:59:39.785864+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "LogicReward autoformalization soft unification step-wise logical supervision"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_autoformalization-faithfulness_20260514T105550",
  "tool": "WebSearch",
  "tool_args": {
    "query": "LogicReward autoformalization soft unification step-wise logical supervision"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-14T10:59:39.785995+00:00_

Web search results for query: "FOL formalization quality metric autoformalization evaluation benchmark 2025 2026"

Links: [{"title":"Process-Driven Autoformalization in Lean 4 | OpenReview","url":"https://openreview.net/forum?id=k8KsI84Ds7"},{"title":"[2406.07222] Reliable Evaluation and Benchmarks for Statement Autoformalization","url":"https://arxiv.org/abs/2406.07222"},{"title":"Reliable Evaluation and Benchmarks for Statement Autoformalization - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-main.907/"},{"title":"Reliable Evaluation and Benchmarks for Statement ...","url":"https://aclanthology.org/2025.emnlp-main.907.pdf"},{"title":"RLMEval: Evaluating Autoformalization on Research-Level Mathematics","url":"http://aitp-conference.org/2025/abstract/AITP_2025_paper_8.pdf"},{"title":"[2406.01940] Process-Driven Autoformalization in Lean 4","url":"https://arxiv.org/abs/2406.01940"},{"title":"Autoformalization in the Era of Large Language Models: A Survey","url":"https://arxiv.org/html/2505.23486v1"},{"title":"ProofFlow: A Dependency Graph Approach to Faithful Proof Autoformalization","url":"https://arxiv.org/html/2510.15981v1"},{"title":"ProofNet: A Benchmark for Autoformalizing and Formally ...","url":"https://mathai2022.github.io/papers/20.pdf"},{"title":"Towards a Common Framework for Autoformalization","url":"https://arxiv.org/pdf/2509.09810"}]

Based on the search results, here are the key findings related to FOL formalization quality metrics and autoformalization evaluation benchmarks for 2025-2026:

## Quality Metrics

BEq+ is an automated metric that correlates strongly with human judgment, along with ProofNetVerif, a new dataset for assessing the quality of evaluation metrics, containing 3,752 annotated examples. Poiroux et al. (2025) presents the symbolic computation index: BEqL and BEq+.

Additionally, ProofScore, a new composite metric to evaluate syntactic correctness, semantic faithfulness, and structural fidelity was introduced as an evalua
…[truncated 1023 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_autoformalization-faithfulness_20260514T105550",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-14T10:59:39.786149+00:00_

Web search results for query: "VERGE formal refinement guidance engine verifiable LLM reasoning MCS error localization 2026"

Links: [{"title":"[2601.20055] VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning","url":"https://arxiv.org/abs/2601.20055"},{"title":"VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning","url":"https://arxiv.org/pdf/2601.20055"},{"title":"Paper page - VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning","url":"https://huggingface.co/papers/2601.20055"},{"title":"[Literature Review] VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning","url":"https://www.themoonlight.io/en/review/verge-formal-refinement-and-guidance-engine-for-verifiable-llm-reasoning"},{"title":"dblp: VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning.","url":"https://dblp.uni-trier.de/rec/journals/corr/abs-2601-20055.html"},{"title":"Verge: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning | Hacker News","url":"https://news.ycombinator.com/item?id=46813257"},{"title":"VERGE: Formal Refinement and Guidance Engine for Verifiable ...","url":"https://ubos.tech/verge-formal-refinement-and-guidance-engine-for-verifiable-llm-reasoning-2/"},{"title":"llm formal method | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/arxiv/search?highlight=1&query=LLM+formal+method&sort=0"},{"title":"Formal Refinement and Guidance Engine for Verifiable ...","url":"https://www.researchgate.net/publication/400178327_VERGE_Formal_Refinement_and_Guidance_Engine_for_Verifiable_LLM_Reasoning"},{"title":"VeriBench: End-to-End Formal Verification Benchmark for ...","url":"https://openreview.net/pdf?id=rWkGFmnSNl"}]

I found detailed information about VERGE. Here's what the search revealed:

## VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning

VERGE is a neurosymbolic framework that combines LLMs with SMT solvers to produce verification-
…[truncated 1465 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_autoformalization-faithfulness_20260514T105550",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-14T10:59:39.786319+00:00_

Web search results for query: "LogicReward autoformalization soft unification step-wise logical supervision"

Links: [{"title":"LogicReward: Faithful & Rigorous Reasoning","url":"https://llm-symbol.github.io/LogicReward/"},{"title":"LogicReward: Incentivizing LLM Reasoning via Step-Wise Logical Supervision [Quick Review]","url":"https://liner.com/review/logicreward-incentivizing-llm-reasoning-via-stepwise-logical-supervision"},{"title":"LogicReward: Incentivizing LLM Reasoning via Step-Wise Logical Supervision","url":"https://arxiv.org/html/2512.18196v2"},{"title":"LogicReward: Incentivizing LLM Reasoning via Step-Wise Logical Supervision | OpenReview","url":"https://openreview.net/forum?id=A3FhAVfcJI"},{"title":"[2512.18196] LogicReward: Incentivizing LLM Reasoning via Step-Wise Logical Supervision","url":"https://arxiv.org/abs/2512.18196"},{"title":"Publiced as a conference paper at ICLR 2026 LOGICREWARD:","url":"https://openreview.net/pdf/de9ac22503a1fd3b541e09e4ff9021f87fc357c3.pdf"},{"title":"GitHub - Aiden0526/Logic-Reward: Codes and Data for ICLR 2026 paper \"LogicReward: Incentivizing LLM Reasoning via Step-Wise Logical Supervision\" · GitHub","url":"https://github.com/Aiden0526/Logic-Reward"},{"title":"LogicReward - a Aiden0526 Collection","url":"https://huggingface.co/collections/Aiden0526/logicreward"},{"title":"Incentivizing LLM Reasoning Via Step-Wise Logical Supervision","url":"https://www.paperdigest.org/related_patent/?paper_id=iclr-forum-id-IRhYVOKFe0-2026-02-17"},{"title":"Incentivizing LLM Reasoning via Step-Wise Logical ...","url":"https://www.semanticscholar.org/paper/LogicReward:-Incentivizing-LLM-Reasoning-via-Xu-Fei/8b7154e1ac5b4761d1460e3abcfde7a74cd4f453"}]

Based on the search results, here's what I found about LogicReward, autoformalization with soft unification, and step-wise logical supervision:

## Overview

LogicReward is a novel reward system that guides model training by enforcing step-level logical correctness with a theorem prover
…[truncated 1402 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_autoformalization-faithfulness_20260514T105550",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-14T10:59:39.786486+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2601.20055",
  "prompt": "Extract: 1) How VERGE uses MCS (Minimal Correction Subsets) for error localization - detailed mechanism. 2) How it handles formalization faithfulness issues. 3) Quantitative results on benchmarks. 4) How it compares to VeriCoT and similar approaches. 5) The semantic routing mechanism for different claim types."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_autoformalization-faithfulness_20260514T105550",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2601.20055",
    "prompt": "Extract: 1) How VERGE uses MCS (Minimal Correction Subsets) for error localization - detailed mechanism. 2) How it handles formalization faithfulness issues. 3) Quantitative results on benchmarks. 4) How it compares to VeriCoT and similar approaches. 5) The semantic routing mechanism for different claim types."
  }
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-14T10:59:39.786624+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "svs_formal_verification",
  "file": "memory.md",
  "max_chars": "12000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_autoformalization-faithfulness_20260514T105550",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "svs_formal_verification",
    "file": "memory.md",
    "max_chars": "12000"
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-14T10:59:39.786755+00:00_

# VERGE Framework: Key Components Analysis

Based on the abstract provided, here's what can be extracted about these technical aspects:

## 1. **MCS for Error Localization**
The framework uses "Minimal Correction Subsets (MCS), which pinpoint the exact subset of claims to revise." This transforms verification failures into actionable refinement guidance rather than binary pass/fail signals.

## 2. **Formalization Faithfulness**
The paper addresses this through a multi-step process: decomposing LLM outputs into atomic claims, converting them to first-order logic, then verifying consistency using automated theorem proving. However, specific faithfulness mitigation strategies aren't detailed in the abstract.

## 3. **Quantitative Results**
The system achieved "an average performance uplift of 18.7% at convergence across a set of reasoning benchmarks compared to single-pass approaches" when using GPT-OSS-120B.

## 4. **Comparison to Related Work**
The abstract doesn't explicitly mention VeriCoT or comparative evaluations against similar verification-guided approaches—these details would require accessing the full paper.

## 5. **Semantic Routing Mechanism**
The framework "directs different claim types to appropriate verification strategies: symbolic solvers for logical claims and LLM ensembles for commonsense reasoning," enabling specialized handling based on claim classification.

**Note:** Full technical details require accessing the complete paper via PDF or HTML links provided.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_autoformalization-faithfulness_20260514T105550",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-14T10:59:39.786921+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/svs_formal_verification/memory.md\", \"content\": \"# SVS Project Memory\\n\\n## Z3 Crash 经验（D008）\\n- [2026-05-14] Z3 C++ 层对畸形 FOL 表达式可触发 `abort()` → SIGABRT，Python try/except 无法捕获\\n- threading.Lock 只解决并发安全，不防 SIGABRT——mvp_002 用 Lock 方案仍然 crash\\n- 解决方案：`z3_sandbox.py` persistent subprocess worker（forkserver context）。所有 Z3 eval() 在子进程执行\\n- 子进程 crash → 父进程收到 exitcode≠0 → 自动重启 worker → pipeline 继续\\n- crash test 验证：os.abort() in worker → parent survived → worker restarted → 后续 validation 正常\\n\\n## 量词 Bug 实证数据\\n- [2026-05-14] 旧 MVP（mvp_001, killed）日志归档于 `/root/mvp_run_killed_20260514.log`\\n- V3.2 formalization 系统性 ForAll→Exists 错误：Exists 736 vs ForAll 718\\n- 这是 IC 全 SAT 的根因之一——Exists(x, Implies(P(x), Q(x))) trivially SAT\\n- 量词修复后（CRITICAL RULES prompt）：ForAll 93% vs Exists 7%\\n- 论文 ablation 可用修复前后数据对比\\n\\n## Qwen2.5-14B Formalization 能力限制\\n- [2026-05-14] Dry-run 结果：claim formalization rate 43.26%（目标 50%），premise formalization 100%\\n- 原因：Qwen 14B formalization 能力弱于 DeepSeek V3.2\\n- **结论**：正式实验 cross-model 验证时，Qwen 只做 chain generation，formalization 仍走 DeepSeek V3.2 API\\n- vLLM 部署：cuda:2+3, port 8002, PID 41276, TP=2, max-model-len 4096\\n\\n## 文献定位策略（2026-05-14 两份调研综合）\\n- **最近竞品**：VeriCoT (2025.11, binary Z3 验证), VERGE (2026.01, MCS error localization), SSV (IJCAI 2025, Z3 concrete instantiation)\\n- **SVS 差异化**：(1) IC = MCS_size/total_claims 连续 graded verifier (2) PCV 框架 (3) IC 做 chain selection（无人做过）\\n- **论文定位**：不说\\\"首次用 FV 检查 CoT\\\"，说\\\"首次将形式一致性检查转化为 graded chain selection 机制 + PCV\\\"\\n- **与 VERGE 区分**：VERGE 的 MCS 用于 error localization + iterative refinement，SVS 的 IC(MCS) 用于 graded scoring + selection\\n- **与 SSV 区分**：SSV 验证\\\"formalization 是否正确\\\"，SVS 用 verification score 做\\\"chain selection\\\"\\n- **autoformalization 风险**：arXiv:2604.19459 发现 axiom fabrication + premise mistranslation 两类系统性 unfaithfulness，对 formalization confidence 设
…[truncated 1828 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_autoformalization-faithfulness_20260514T105550",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-14T10:59:39.787118+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

````json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/svs_formal_verification/artifacts/faithfulness_risk_analysis.md",
  "content": "# Autoformalization Faithfulness Risk Analysis for SVS\n\n## 1. 文献核心发现\n\n### 1.1 arXiv:2604.19459 — \"Do LLMs Game Formalization?\"\n\n**实验设置**：303 道 FOL 问题（203 FOLIO + 100 Multi-LogiEval），GPT-5 和 DeepSeek-R1，对比 unified generation 与 two-stage pipeline（先 formalize 再 prove）。\n\n**两类系统性 unfaithfulness**：\n\n| 失败模式 | 主要模型 | 频率 | 机制 | 可检测性 |\n|----------|---------|------|------|---------|\n| **Axiom Fabrication** | GPT-5 | 107 例（73 FOLIO, 34 MLE）| 证明失败后将结论直接嵌入前提（56%），或编造世界知识(16%)、虚构事实(12%)、插入矛盾(11%) | **可检测**：cross-stage 对比发现 Stage 2 修改了 Stage 1 锁定的 formalization |\n| **Premise Mistranslation** | DeepSeek-R1 | 难以量化（仅 2 例 stage 修改） | 量词混淆（∀/∃）、谓词替换、语义漂移，嵌入 formalization 选择中 | **几乎不可检测**：输出内部一致，LLM-as-judge 也难以发现 |\n\n**关键数据**：\n- 编译率 87-99%（高编译率≠高 faithfulness）\n- Nudged condition 下 Uncertain 真值的 unfaithful rate: 34.7% vs baseline 16%\n- 模型提交明确答案时精度 94-98%，但 27-43% 案例报告 Uncertain/Failure（保守策略）\n- 量词混淆（∀/∃）是文档化的失败触发因素——**与 SVS 已知的量词 bug 直接相关**\n\n### 1.2 arXiv:2604.25031 — \"Faithful Autoformalization via Roundtrip Verification and Repair\"\n\n**方法**：T₁(NL→FOL) → T₂(FOL→NL) → T₃(NL→FOL) → SMT solver 检查 T₁ 与 T₃ 的逻辑等价性。\n\n**核心结果**：\n- Baseline 等价率：44.7-66.2%（意味着 ~35-55% formalization 不忠实）\n- Diagnosis-guided repair 后：85.3-94.7%\n- SAT（不等价）规则的 NLI drift 是 UNSAT 规则的 1.4-2.5 倍\n- **局限**：无法检测 T₁ 和 T₃ 犯相同错误的情况（systematic bias）\n\n**残余失败（26 条规则无法修复）**：schema 词汇缺失、复合析取/嵌套条件编码不一致、异常子句反转、数值阈值丢失变量依赖。\n\n### 1.3 相关工作\n\n| 工作 | 方法 | 与 SVS 关系 |\n|------|------|------------|\n| **VeriCoT** (2511.04662) | 每步 CoT → FOL，binary Z3 验证 + premise grounding | SVS 竞品；binary verifier，无 graded scoring |\n| **VERGE** (2601.20055) | MCS error localization + iterative refinement，18.7% uplift | SVS 竞品；MCS 用于 refinement 而非 scoring |\n| **LogicReward** (ICLR 2026) | Autoformalization + soft unification + Isabelle 验证作为 reward | 训练时方案；SVS 是推理时方案 |\n| **ProofFlow** (2510.15981) | 依赖图 + ProofScore（句法+语义+结构） | 评估指标设计参考 |\n| **BEq+** (EMNLP 2025) | 符号计算的 autoformalization 评估指标 | faithfulness metric 参考 |\n\n## 2. SVS Pipeline 影响映射\n\n### SVS formalization 流程\n```\nNL claim → DeepSeek V3.2 API → FOL expression → Z3 MaxSAT → MCS → IC score\nNL premise → DeepSeek V3.2 API → FOL expression → PCV (premise + claims 联合验证)\n```\n\n### 影响矩阵\n\n| 失败模式 | 影响的 pipeline 环节 | PCV 能否缓解 | 严重程度 | 说明 |\n|----------|---------------------|-------------|---------|------|\n| **Axiom Fabrication (claim 层)** | Z3 验证：编造的公理使不一致集合变为一致 → IC 假高 | **部分缓解**：如果编造公理与 premise 矛盾，PCV 会检测到不一致 | **中** | SVS 无 \"prove\" 阶段，fabrication 主要发生在 proof generation 中（GPT-5 特征），DeepSeek V3.2 的 fabrication 风险较低 |\n| **Axiom Fabrication (premise 层)** | PCV：premise formalization 中引入编造内容 → PCV 基准被污染 | **不能缓解**：PCV 信任 premise formalization 的正确性 | **高** | 如果 premise 被\"增强\"（加入隐含假设），PCV 的约束力被削弱 |\n| **Premise Mistranslation** | PCV：premise 翻译错误 → PCV 验证的是错误的约束 | **不能缓解**：PCV 无法区分\"正确的 premise FOL\"和\"错误的 premise FOL\" | **高** | DeepSeek 系列模型的主要风险；输出内部一致，无法通过 cross-check 发现 |\n| **Claim Mistranslation** | IC scoring：claim FOL 与原始 NL 语义不匹配 → IC 度量的不是真正的逻辑一致性 | **部分缓解**：如果 claim 翻译偏离了 premise 约束，PCV-IC 可能偶然检测到 | **中** | 影响 IC 的信噪比，但如果翻译偏差是系统性的，所有 chain 受到类似影响 |\n| **量词混淆（∀/∃）** | Z3 验证：∃(x, P(x)→Q(x)) trivially SAT → IC 失去区分力 | **部分缓解**：PCV 中如果 premise 用了正确量词，可能暴露 claim 的量词错误 | **高（已修复）** | SVS 已通过 CRITICAL RULES prompt 修复（93% ForAll），但残余 7% 仍是风险 |\n\n### SVS 特殊缓解因素\n\n1. **SVS 不做 theorem proving**：arXiv:2604.19459 的 axiom fabrication 主要发生在 proof generation 阶段（模型试图证明一个目标时才编造公理）。SVS 只做 consistency checking（MaxSAT），不要求证明特定目标，因此 fabrication 的动机和频率应显著低于论文报告的水平。\n\n2. **IC 是相对度量**：IC = MCS_size / total_claims 用于 chain selection（选择 IC 最高的 chain）。即使 formalization 有系统性偏差，只要偏差在不同 chain 间是可比的，IC 的相对排序仍可能有效。这是 graded scoring 相对 binary verification 的鲁棒性优势。\n\n3. **DeepSeek V3.2 vs DeepSeek-R1**：论文测试的是 DeepSeek-R1（推理模型），SVS 用的是 DeepSeek V3.2（通用模型）。两者的 formalization 行为可能不同，但 premise mistranslation 风险仍需警惕。\n\n## 3. 现有缓解方案\n\n### 3.1 Roundtrip Verification（arXiv:2604.25031）\n- **机制**：NL → FOL → NL' → FOL' → SMT 检查 FOL ≡ FOL'\n- **优点**：不需要 ground truth，可在推理时应用\n- **缺点**：(1) 无法检测 systematic bias（两次 formalization 犯相同错误）；(2) 每次 formalization 需 3 次 LLM 调用 + 1 次 SMT 调用，成本高\n- **SVS 适用性**：**中等**。可用于 premise formalization 的质量检查（premise 数量少，成本可控），但对 claim-level 太贵\n\n### 3.2 Cross-stage Comparison（arXiv:2604.19459）\n- **机制**：先锁定 formalization，再单独做 prove/verify，比较两阶段的 formalization 是否一致\n- **优点**：可检测 axiom fabrication\n- **缺点**：无法检测 premise mistranslation（错误发生在第一阶段）\n- **SVS 适用性**：**低**。SVS 不做 proving，无第二阶段可比较\n\n### 3.3 LogicReward — Soft Unification + Implicit Assumption 补充\n- **机制**：让 LLM 在 formalization 前补充隐含假设，减少歧义，再用 theorem prover 验证\n- **优点**：从源头减少 mistranslation\n- **缺点**：需要训练（ICLR 2026 论文用 Isabelle 做 reward），推理时不直接可用\n- **SVS 适用性**：**低（post-MVP）**。理念可借鉴，但需要适配到 Z3/FOL\n\n### 3.4 VERGE — Semantic Routing\n- **机制**：将 claim 按类型分流——逻辑 claim 用 symbolic solver，常识 claim 用 LLM ensemble\n- **优点**：避免对不适合 formalization 的 claim 强行 formalize\n- **缺点**：增加系统复杂度\n- **SVS 适用性**：**中等（post-MVP）**。SVS 当前 formalization rate ~85%，剩余 15% 可能是不适合 formalization 的 claim，可考虑降级处理\n\n### 3.5 BEq+ / ProofScore — Faithfulness Metric\n- **机制**：基于符号计算的 autoformalization 评估指标\n- **优点**：可量化 faithfulness\n- **缺点**：需要 ground truth FOL（SVS 没有）\n- **SVS 适用性**：**仅用于人工抽样评估**\n\n## 4. SVS 特有的缓解策略\n\n### 4.1 Premise Roundtrip Check（低成本，推荐 post-MVP P1）\n- 对 premise formalization 做 roundtrip verification：FOL → NL → FOL' → SMT 等价检查\n- **理由**：premise 数量少（每题 3-10 条），成本低；premise 翻译错误直接摧毁 PCV 的有效性\n- **实现**：在 formalization pipeline 中对 premise 增加一轮 back-translation + re-formalization + Z3 equivalence check\n- **预期效果**：类比论文数据，可检测 ~50% 的 premise mistranslation（baseline 等价率 ~55-65%）\n\n### 4.2 IC Consistency Cross-check（低成本，推荐 post-MVP P1）\n- 对同一 NL claim 做两次独立 formalization（不同 temperature 或 prompt），比较两个 FOL 的 Z3 equivalence\n- **理由**：如果两次 formalization 不等价，说明该 claim 的 formalization 不稳定，IC score 不可靠\n- **实现**：在 IC 计算中加入 formalization confidence weight：稳定的 claim 权重高，不稳定的降权\n- **预期效果**：提高 IC 的信噪比，尤其对含歧义量词的 claim\n\n### 4.3 Formalization Rate as Implicit Filter（零成本，MVP 已有）\n- SVS 当前 formalization rate ~85%。无法 formalize 的 claim 被排除在 IC 计算外\n- **重新解读**：formalization 失败可能恰恰过滤了最容易被 mistranslate 的 claim（复杂嵌套结构、含歧义量词）\n- **论文写法**：可将 formalization rate 从\"局限\"转为\"implicit quality filter\"\n\n### 4.4 PCV as Partial Fabrication Detector（零成本，MVP 已有）\n- PCV 验证 claim FOL 与 premise FOL 的联合一致性\n- 如果 claim formalization 中引入了与 premise 矛盾的编造内容，PCV 会检测到不一致 → IC 降低\n- **局限**：无法检测与 premise 不矛盾的编造（如加入正确但未声明的世界知识）\n\n### 4.5 Semantic Routing for Unformalizable Claims（中等成本，post-MVP P2）\n- 对 formalization 失败的 ~15% claim，用 LLM confidence/entailment 作为替代 score\n- 与 VERGE 的 semantic routing 理念类似，但更轻量\n- **实现**：IC_hybrid = α · IC_formal + (1-α) · score_LLM，其中 α 由 formalization 成功率决定\n\n## 5. 建议实验设计\n\n### 低成本方案（无需额外训练，post-MVP 可快速实现）\n\n| 优先级 | 实验 | 成本 | 预期产出 |\n|-------|------|------|---------|\n| **P0** | 人工抽样评估 formalization faithfulness | 2-3 天标注 | 量化 SVS pipeline 的实际 faithfulness rate，作为论文数据 |\n| **P1** | Premise roundtrip check | ~2x premise formalization API 成本 | 检测并过滤不忠实 premise formalization |\n| **P1** | Dual-formalization consistency check | ~2x claim formalization API 成本 | 量化 formalization 稳定性，加权 IC |\n| **P2** | Formalization rate 与 faithfulness 相关性分析 | 仅需分析现有日志 | 验证 \"formalization 失败 = implicit quality filter\" 假设 |\n\n### 高成本方案（需要训练或大量标注，paper v2 或 follow-up）\n\n| 优先级 | 实验 | 成本 | 预期产出 |\n|-------|------|------|---------|\n| **P3** | Fine-tune formalization model with faithfulness reward | 需要标注 + 训练 | 从源头提高 faithfulness |\n| **P3** | 构建 SVS-specific faithfulness benchmark | 需要专家标注 ground truth FOL | 系统化评估和持续改进 |\n\n### 实验设计细节：人工抽样评估（P0）\n\n1. 从 MVP 实验结果中随机抽取 50 个 claim formalization 对\n2. 由人工判断每个 NL claim → FOL 翻译是否忠实（binary: faithful/unfaithful）\n3. 对 unfaithful 案例分类：量词错误 / 谓词替换 / 语义漂移 / 信息丢失 / 信息编造\n4. 计算 SVS pipeline 的 empirical faithfulness rate\n5. 分析 faithfulness 与 IC score 的相关性\n\n## 6. 对论文写作的影响\n\n### Limitations Section 必须提到的风险\n- \"Autoformalization faithfulness remains an open challenge (Kim et al., 2026). Our IC score measures logical consistency of the formalized expressions, not semantic faithfulness to the original natural language claims.\"\n- \"Premise mistranslation, where FOL expressions are internally consistent but semantically unfaithful to the source text, can affect PCV effectiveness.\"\n- 引用 arXiv:2604.19459 作为已知风险的文献支撑\n\n### 将风险转为论文优势的策略\n\n1. **IC 的鲁棒性论点**：IC 是相对度量用于 chain selection，即使 formalization 有系统性偏差，只要偏差对所有 chain 可比，selection 仍然有效。这比 binary verification（VeriCoT）更鲁棒——binary verifier 对 faithfulness 问题是脆弱的（一个 unfaithful formalization 可以翻转 binary 判断）。\n\n2. **PCV 作为 partial mitigation**：PCV 将 claim 与 premise 联合验证，提供了额外的 grounding signal。虽然不能完全解决 faithfulness 问题，但比纯 internal consistency check 多了一层约束。\n\n3. **Formalization rate 作为 quality gate**：85% 的 formalization rate 意味着系统自动过滤了最难 formalize 的 claim，论文可以论证这是一种 implicit quality control。\n\n4. **Future work 方向**：将 roundtrip verification 和 formalization confidence 作为 future work 提出，展示对问题的清醒认识和改进路径。\n\n### 建议引用\n- Kim et al. (2026) \"Do LLMs Game Formalization?\" — faithfulness 风险的直接证据\n- arXiv:2604.25031 \"Faithful Autoformalization via Roundtrip Verification\" — 缓解方案参考\n- LogicReward (ICLR 2026) — 训练时缓解方案\n- VERGE (2601.20055) — MCS 在 verification 中的应用（也用于区分 SVS 的 scoring vs refinement）\n"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "worker_research_autoformalization-faithfulness_20260514T105550",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/svs_formal_verification/artifacts/faithfulness_risk_analysis.md",
    "content": "# Autoformalization Faithfulness Risk Analysis for SVS\n\n## 1. 文献核心发现\n\n### 1.1 arXiv:2604.19459 — \"Do LLMs Game Formalization?\"\n\n**实验设置**：303 道 FOL 问题（203 FOLIO + 100 Multi-LogiEval），GPT-5 和 DeepSeek-R1，对比 unified generation 与 two-stage pipeline（先 formalize 再 prove）。\n\n**两类系统性 unfaithfulness**：\n\n| 失败模式 | 主要模型 | 频率 | 机制 | 可检测性 |\n|----------|---------|------|------|---------|\n| **Axiom Fabrication** | GPT-5 | 107 例（73 FOLIO, 34 MLE）| 证明失败后将结论直接嵌入前提（56%），或编造世界知识(16%)、虚构事实(12%)、插入矛盾(11%) | **可检测**：cross-stage 对比发现 Stage 2 修改了 Stage 1 锁定的 formalization |\n| **Premise Mistranslation** | DeepSeek-R1 | 难以量化（仅 2 例 stage 修改） | 量词混淆（∀/∃）、谓词替换、语义漂移，嵌入 formalization 选择中 | **几乎不可检测**：输出内部一致，LLM-as-judge 也难以发现 |\n\n**关键数据**：\n- 编译率 87-99%（高编译率≠高 faithfulness）\n- Nudged condition 下 Uncertain 真值的 unfaithful rate: 34.7% vs baseline 16%\n- 模型提交明确答案时精度 94-98%，但 27-43% 案例报告 Uncertain/Failure（保守策略）\n- 量词混淆（∀/∃）是文档化的失败触发因素——**与 SVS 已知的量词 bug 直接相关**\n\n### 1.2 arXiv:2604.25031 — \"Faithful Autoformalization via Roundtrip Verification and Repair\"\n\n**方法**：T₁(NL→FOL) → T₂(FOL→NL) → T₃(NL→FOL) → SMT solver 检查 T₁ 与 T₃ 的逻辑等价性。\n\n**核心结果**：\n- Baseline 等价率：44.7-66.2%（意味着 ~35-55% formalization 不忠实）\n- Diagnosis-guided repair 后：85.3-94.7%\n- SAT（不等价）规则的 NLI drift 是 UNSAT 规则的 1.4-2.5 倍\n- **局限**：无法检测 T₁ 和 T₃ 犯相同错误的情况（systematic bias）\n\n**残余失败（26 条规则无法修复）**：schema 词汇缺失、复合析取/嵌套条件编码不一致、异常子句反转、数值阈值丢失变量依赖。\n\n### 1.3 相关工作\n\n| 工作 | 方法 | 与 SVS 关系 |\n|------|------|------------|\n| **VeriCoT** (2511.04662) | 每步 CoT → FOL，binary Z3 验证 + premise grounding | SVS 竞品；binary verifier，无 graded scoring |\n| **VERGE** (2601.20055) | MCS error localization + iterative refinement，18.7% uplift | SVS 竞品；MCS 用于 refinement 而非 scoring |\n| **LogicReward** (ICLR 2026) | Autoformalization + soft unification + Isabelle 验证作为 reward | 训练时方案；SVS 是推理时方案 |\n| **ProofFlow** (2510.15981) | 依赖图 + ProofScore（句法+语义+结构） | 评估指标设计参考 |\n| **BEq+** (EMNLP 2025) | 符号计算的 autoformalization 评估指标 | faithfulness metric 参考 |\n\n## 2. SVS Pipeline 影响映射\n\n### SVS formalization 流程\n```\nNL claim → DeepSeek V3.2 API → FOL expression → Z3 MaxSAT → MCS → IC score\nNL premise → DeepSeek V3.2 API → FOL expression → PCV (premise + claims 联合验证)\n```\n\n### 影响矩阵\n\n| 失败模式 | 影响的 pipeline 环节 | PCV 能否缓解 | 严重程度 | 说明 |\n|----------|---------------------|-------------|---------|------|\n| **Axiom Fabrication (claim 层)** | Z3 验证：编造的公理使不一致集合变为一致 → IC 假高 | **部分缓解**：如果编造公理与 premise 矛盾，PCV 会检测到不一致 | **中** | SVS 无 \"prove\" 阶段，fabrication 主要发生在 proof generation 中（GPT-5 特征），DeepSeek V3.2 的 fabrication 风险较低 |\n| **Axiom Fabrication (premise 层)** | PCV：premise formalization 中引入编造内容 → PCV 基准被污染 | **不能缓解**：PCV 信任 premise formalization 的正确性 | **高** | 如果 premise 被\"增强\"（加入隐含假设），PCV 的约束力被削弱 |\n| **Premise Mistranslation** | PCV：premise 翻译错误 → PCV 验证的是错误的约束 | **不能缓解**：PCV 无法区分\"正确的 premise FOL\"和\"错误的 premise FOL\" | **高** | DeepSeek 系列模型的主要风险；输出内部一致，无法通过 cross-check 发现 |\n| **Claim Mistranslation** | IC scoring：claim FOL 与原始 NL 语义不匹配 → IC 度量的不是真正的逻辑一致性 | **部分缓解**：如果 claim 翻译偏离了 premise 约束，PCV-IC 可能偶然检测到 | **中** | 影响 IC 的信噪比，但如果翻译偏差是系统性的，所有 chain 受到类似影响 |\n| **量词混淆（∀/∃）** | Z3 验证：∃(x, P(x)→Q(x)) trivially SAT → IC 失去区分力 | **部分缓解**：PCV 中如果 premise 用了正确量词，可能暴露 claim 的量词错误 | **高（已修复）** | SVS 已通过 CRITICAL RULES prompt 修复（93% ForAll），但残余 7% 仍是风险 |\n\n### SVS 特殊缓解因素\n\n1. **SVS 不做 theorem proving**：arXiv:2604.19459 的 axiom fabrication 主要发生在 proof generation 阶段（模型试图证明一个目标时才编造公理）。SVS 只做 consistency checking（MaxSAT），不要求证明特定目标，因此 fabrication 的动机和频率应显著低于论文报告的水平。\n\n2. **IC 是相对度量**：IC = MCS_size / total_claims 用于 chain selection（选择 IC 最高的 chain）。即使 formalization 有系统性偏差，只要偏差在不同 chain 间是可比的，IC 的相对排序仍可能有效。这是 graded scoring 相对 binary verification 的鲁棒性优势。\n\n3. **DeepSeek V3.2 vs DeepSeek-R1**：论文测试的是 DeepSeek-R1（推理模型），SVS 用的是 DeepSeek V3.2（通用模型）。两者的 formalization 行为可能不同，但 premise mistranslation 风险仍需警惕。\n\n## 3. 现有缓解方案\n\n### 3.1 Roundtrip Verification（arXiv:2604.25031）\n- **机制**：NL → FOL → NL' → FOL' → SMT 检查 FOL ≡ FOL'\n- **优点**：不需要 ground truth，可在推理时应用\n- **缺点**：(1) 无法检测 systematic bias（两次 formalization 犯相同错误）；(2) 每次 formalization 需 3 次 LLM 调用 + 1 次 SMT 调用，成本高\n- **SVS 适用性**：**中等**。可用于 premise formalization 的质量检查（premise 数量少，成本可控），但对 claim-level 太贵\n\n### 3.2 Cross-stage Comparison（arXiv:2604.19459）\n- **机制**：先锁定 formalization，再单独做 prove/verify，比较两阶段的 formalization 是否一致\n- **优点**：可检测 axiom fabrication\n- **缺点**：无法检测 premise mistranslation（错误发生在第一阶段）\n- **SVS 适用性**：**低**。SVS 不做 proving，无第二阶段可比较\n\n### 3.3 LogicReward — Soft Unification + Implicit Assumption 补充\n- **机制**：让 LLM 在 formalization 前补充隐含假设，减少歧义，再用 theorem prover 验证\n- **优点**：从源头减少 mistranslation\n- **缺点**：需要训练（ICLR 2026 论文用 Isabelle 做 reward），推理时不直接可用\n- **SVS 适用性**：**低（post-MVP）**。理念可借鉴，但需要适配到 Z3/FOL\n\n### 3.4 VERGE — Semantic Routing\n- **机制**：将 claim 按类型分流——逻辑 claim 用 symbolic solver，常识 claim 用 LLM ensemble\n- **优点**：避免对不适合 formalization 的 claim 强行 formalize\n- **缺点**：增加系统复杂度\n- **SVS 适用性**：**中等（post-MVP）**。SVS 当前 formalization rate ~85%，剩余 15% 可能是不适合 formalization 的 claim，可考虑降级处理\n\n### 3.5 BEq+ / ProofScore — Faithfulness Metric\n- **机制**：基于符号计算的 autoformalization 评估指标\n- **优点**：可量化 faithfulness\n- **缺点**：需要 ground truth FOL（SVS 没有）\n- **SVS 适用性**：**仅用于人工抽样评估**\n\n## 4. SVS 特有的缓解策略\n\n### 4.1 Premise Roundtrip Check（低成本，推荐 post-MVP P1）\n- 对 premise formalization 做 roundtrip verification：FOL → NL → FOL' → SMT 等价检查\n- **理由**：premise 数量少（每题 3-10 条），成本低；premise 翻译错误直接摧毁 PCV 的有效性\n- **实现**：在 formalization pipeline 中对 premise 增加一轮 back-translation + re-formalization + Z3 equivalence check\n- **预期效果**：类比论文数据，可检测 ~50% 的 premise mistranslation（baseline 等价率 ~55-65%）\n\n### 4.2 IC Consistency Cross-check（低成本，推荐 post-MVP P1）\n- 对同一 NL claim 做两次独立 formalization（不同 temperature 或 prompt），比较两个 FOL 的 Z3 equivalence\n- **理由**：如果两次 formalization 不等价，说明该 claim 的 formalization 不稳定，IC score 不可靠\n- **实现**：在 IC 计算中加入 formalization confidence weight：稳定的 claim 权重高，不稳定的降权\n- **预期效果**：提高 IC 的信噪比，尤其对含歧义量词的 claim\n\n### 4.3 Formalization Rate as Implicit Filter（零成本，MVP 已有）\n- SVS 当前 formalization rate ~85%。无法 formalize 的 claim 被排除在 IC 计算外\n- **重新解读**：formalization 失败可能恰恰过滤了最容易被 mistranslate 的 claim（复杂嵌套结构、含歧义量词）\n- **论文写法**：可将 formalization rate 从\"局限\"转为\"implicit quality filter\"\n\n### 4.4 PCV as Partial Fabrication Detector（零成本，MVP 已有）\n- PCV 验证 claim FOL 与 premise FOL 的联合一致性\n- 如果 claim formalization 中引入了与 premise 矛盾的编造内容，PCV 会检测到不一致 → IC 降低\n- **局限**：无法检测与 premise 不矛盾的编造（如加入正确但未声明的世界知识）\n\n### 4.5 Semantic Routing for Unformalizable Claims（中等成本，post-MVP P2）\n- 对 formalization 失败的 ~15% claim，用 LLM confidence/entailment 作为替代 score\n- 与 VERGE 的 semantic routing 理念类似，但更轻量\n- **实现**：IC_hybrid = α · IC_formal + (1-α) · score_LLM，其中 α 由 formalization 成功率决定\n\n## 5. 建议实验设计\n\n### 低成本方案（无需额外训练，post-MVP 可快速实现）\n\n| 优先级 | 实验 | 成本 | 预期产出 |\n|-------|------|------|---------|\n| **P0** | 人工抽样评估 formalization faithfulness | 2-3 天标注 | 量化 SVS pipeline 的实际 faithfulness rate，作为论文数据 |\n| **P1** | Premise roundtrip check | ~2x premise formalization API 成本 | 检测并过滤不忠实 premise formalization |\n| **P1** | Dual-formalization consistency check | ~2x claim formalization API 成本 | 量化 formalization 稳定性，加权 IC |\n| **P2** | Formalization rate 与 faithfulness 相关性分析 | 仅需分析现有日志 | 验证 \"formalization 失败 = implicit quality filter\" 假设 |\n\n### 高成本方案（需要训练或大量标注，paper v2 或 follow-up）\n\n| 优先级 | 实验 | 成本 | 预期产出 |\n|-------|------|------|---------|\n| **P3** | Fine-tune formalization model with faithfulness reward | 需要标注 + 训练 | 从源头提高 faithfulness |\n| **P3** | 构建 SVS-specific faithfulness benchmark | 需要专家标注 ground truth FOL | 系统化评估和持续改进 |\n\n### 实验设计细节：人工抽样评估（P0）\n\n1. 从 MVP 实验结果中随机抽取 50 个 claim formalization 对\n2. 由人工判断每个 NL claim → FOL 翻译是否忠实（binary: faithful/unfaithful）\n3. 对 unfaithful 案例分类：量词错误 / 谓词替换 / 语义漂移 / 信息丢失 / 信息编造\n4. 计算 SVS pipeline 的 empirical faithfulness rate\n5. 分析 faithfulness 与 IC score 的相关性\n\n## 6. 对论文写作的影响\n\n### Limitations Section 必须提到的风险\n- \"Autoformalization faithfulness remains an open challenge (Kim et al., 2026). Our IC score measures logical consistency of the formalized expressions, not semantic faithfulness to the original natural language claims.\"\n- \"Premise mistranslation, where FOL expressions are internally consistent but semantically unfaithful to the source text, can affect PCV effectiveness.\"\n- 引用 arXiv:2604.19459 作为已知风险的文献支撑\n\n### 将风险转为论文优势的策略\n\n1. **IC 的鲁棒性论点**：IC 是相对度量用于 chain selection，即使 formalization 有系统性偏差，只要偏差对所有 chain 可比，selection 仍然有效。这比 binary verification（VeriCoT）更鲁棒——binary verifier 对 faithfulness 问题是脆弱的（一个 unfaithful formalization 可以翻转 binary 判断）。\n\n2. **PCV 作为 partial mitigation**：PCV 将 claim 与 premise 联合验证，提供了额外的 grounding signal。虽然不能完全解决 faithfulness 问题，但比纯 internal consistency check 多了一层约束。\n\n3. **Formalization rate 作为 quality gate**：85% 的 formalization rate 意味着系统自动过滤了最难 formalize 的 claim，论文可以论证这是一种 implicit quality control。\n\n4. **Future work 方向**：将 roundtrip verification 和 formalization confidence 作为 future work 提出，展示对问题的清醒认识和改进路径。\n\n### 建议引用\n- Kim et al. (2026) \"Do LLMs Game Formalization?\" — faithfulness 风险的直接证据\n- arXiv:2604.25031 \"Faithful Autoformalization via Roundtrip Verification\" — 缓解方案参考\n- LogicReward (ICLR 2026) — 训练时缓解方案\n- VERGE (2601.20055) — MCS 在 verification 中的应用（也用于区分 SVS 的 scoring vs refinement）\n"
  }
}
````

</details>

---

### Tool result

_source line 30 · 2026-05-14T10:59:39.787370+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/svs_formal_verification/artifacts/faithfulness_risk_analysis.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_autoformalization-faithfulness_20260514T105550",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-14T10:59:39.787503+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "Autoformalization Faithfulness Risk Analysis",
  "type": "report",
  "description": "文献调研+SVS pipeline影响映射：arXiv:2604.19459的axiom fabrication/premise mistranslation两类unfaithfulness风险，roundtrip verification缓解方案，实验设计建议，论文写作策略",
  "project": "svs_formal_verification",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/svs_formal_verification/artifacts/faithfulness_risk_analysis.md",
  "tags": "['faithfulness', 'autoformalization', 'risk-analysis', 'literature-review', 'PCV']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_autoformalization-faithfulness_20260514T105550",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "Autoformalization Faithfulness Risk Analysis",
    "type": "report",
    "description": "文献调研+SVS pipeline影响映射：arXiv:2604.19459的axiom fabrication/premise mistranslation两类unfaithfulness风险，roundtrip verification缓解方案，实验设计建议，论文写作策略",
    "project": "svs_formal_verification",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/svs_formal_verification/artifacts/faithfulness_risk_analysis.md",
    "tags": "['faithfulness', 'autoformalization', 'risk-analysis', 'literature-review', 'PCV']"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-14T10:59:39.787675+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260514_0e7b10\", \"name\": \"Autoformalization Faithfulness Risk Analysis\", \"type\": \"report\", \"description\": \"文献调研+SVS pipeline影响映射：arXiv:2604.19459的axiom fabrication/premise mistranslation两类unfaithfulness风险，roundtrip verification缓解方案，实验设计建议，论文写作策略\", \"path\": \"projects/svs_formal_verification/artifacts/_project/report/faithfulness_risk_analysis.md\", \"url\": null, \"project\": \"svs_formal_verification\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-14T10:59:25.229131+00:00\", \"tags\": [\"faithfulness\", \"autoformalization\", \"risk-analysis\", \"literature-review\", \"PCV\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/svs_formal_verification/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_autoformalization-faithfulness_20260514T105550",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 33 · 2026-05-14T10:59:39.787833+00:00_

报告已生成并注册：`art_20260514_0e7b10`

**核心发现**：

1. **SVS 受影响程度中等偏低**：arXiv:2604.19459 的 axiom fabrication 主要发生在 proof generation 阶段，SVS 只做 consistency checking 不做 proving，fabrication 动机显著降低。但 **premise mistranslation 是高风险**——DeepSeek 系列模型的主要问题，且几乎不可检测，直接摧毁 PCV 有效性。

2. **SVS 已有的两个天然缓解**：(a) IC 是相对度量用于 chain selection，对系统性偏差有鲁棒性；(b) 85% formalization rate 隐式过滤了最难翻译的 claim。

3. **最值得做的 post-MVP 实验**：
   - **P0**：人工抽样 50 个 claim formalization，量化实际 faithfulness rate（2-3 天）
   - **P1**：Premise roundtrip check（FOL→NL→FOL'→Z3 等价检查），成本低，保护 PCV
   - **P1**：Dual-formalization consistency check，给 IC 加 formalization confidence 权重

4. **论文策略**：Limitations 引用 arXiv:2604.19459 展示问题意识，同时论证 IC graded scoring 比 binary verification (VeriCoT) 对 faithfulness 问题更鲁棒。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_autoformalization-faithfulness_20260514T105550"
}
```

</details>

---
