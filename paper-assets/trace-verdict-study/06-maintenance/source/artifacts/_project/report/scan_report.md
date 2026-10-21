# Literature Scan Report — VOTA (Verdict-Oriented Trace Abstraction)

**Date**: 2026-05-15  
**Target**: EMNLP 2026 Main (ARR May 25 deadline)  
**Queries executed**: 16 search groups across arXiv, ACL Anthology, Semantic Scholar, IEEE Xplore  

## Summary

No direct competitor was found that combines execution trace compression with SFT for binary verdict prediction. However, Wang et al. (EMNLP 2025 Findings) present a significant conceptual challenge: their comprehensive study of 5 trace formats for SFT concludes that semantic information from execution traces has limited usefulness. VOTA's response hinges on the distinction between raw/formatted traces and decision-relevant compression targeting fault indicator signals. The closest methodological neighbors are in **patch correctness prediction**, which shares input signal space but differs in task definition and approach.

---

## New Papers Found (10 additions, 16→26 total)

### MEDIUM-HIGH Threat — Trace SFT Effectiveness

| # | Paper | Venue | Threat | Relation to VOTA |
|---|-------|-------|--------|-----------------|
| 1 | **Wang et al. "Do Code Semantics Help?"** (Jian Wang, Xiaofei Xie, Qiang Hu, Shangqing Liu, Yi Li) | Findings of EMNLP 2025 | **MEDIUM-HIGH** | Comprehensive study testing 5 trace formats (Scratchpad, NExT, SemCoder, CodeExecutor, Concise) for SFT on code generation/repair. Conclusion: "semantic information has limited usefulness for SFT." Conceptually the strongest challenge to any trace-based SFT approach including VOTA. |

**Why MEDIUM-HIGH, not HIGH**: Wang et al.'s study differs from VOTA on three axes:
- **Task**: They evaluate code generation and repair; VOTA targets verdict prediction (binary classification), a fundamentally different downstream task where trace signals serve as discriminative features rather than generative context
- **Trace content**: All 5 formats they test preserve execution flow information (variable states, step-by-step traces); none isolates fault indicator signals (exception events, assertion comparison outcomes) — the specific signals VOTA's ablation identifies as carrying nearly all discriminative power
- **Compression strategy**: Their "Concise" format is a syntactic reduction of trace verbosity; VOTA's compression is semantic, retaining only decision-relevant signals for the verdict task

**Implication for VOTA paper**: This paper must be cited and directly addressed. The argument is: "raw trace ineffective for SFT ≠ compressed fault-indicator signals ineffective for SFT." VOTA's component ablation (exception_only achieving 99.83%) provides the empirical counterpoint — the value is not in trace format but in isolating the right signals for the right task.

### MEDIUM Threat — Patch Correctness Prediction

| # | Paper | Venue | Threat | Relation to VOTA |
|---|-------|-------|--------|-----------------|
| 2 | **LLM4PatchCorrect** (Xin Zhou et al.) | TSE 2024 | **MEDIUM** | Uses execution traces + test cases as input for patch correctness assessment. Key difference: zero-shot prompting (no SFT), task is patch correctness (not test verdict), no trace compression. |
| 3 | **APSG + Graph-LoRA** (Zhenyu Yang et al., arXiv 2505.02629) | arXiv 2025 | **LOW-MEDIUM** | PEFT for patch correctness with graph-structured code representation. Key difference: uses static code graph (not runtime trace), no fault indicator signals. |

**Differentiation from VOTA**:
- **Task**: Patch correctness (is this fix correct?) vs. VOTA's verdict prediction (does this test pass/fail?)
- **Input**: LLM4PatchCorrect uses raw traces + test info; VOTA uses decision-relevant compressed signals
- **Method**: LLM4PatchCorrect = zero-shot prompting; APSG = graph-LoRA on static graphs; VOTA = SFT with trace abstraction
- **Signal identification**: Neither work isolates fault indicator signals or measures their individual contribution

### LOW Threat — Supporting Evidence & Background

| # | Paper | Venue | Category | Why Relevant |
|---|-------|-------|----------|-------------|
| 4 | **FuseFL** (Widyasari et al.) | SANER 2024 | code-verdict | Uses test execution outcomes (expected/actual output, errors) for fault localization. Validates that test outcome signals carry discriminative value — same intuition as VOTA, different task. |
| 5 | **REval** (Junkai Chen et al.) | arXiv 2403.16437 | evaluation | LLM runtime behavior prediction: avg accuracy 44.4%. Supports VOTA's argument that LLMs struggle with raw trace reasoning. |
| 6 | **CodeMind** (Changshu Liu et al.) | arXiv 2402.09664 | evaluation | Code reasoning drops with complexity (control flow, API calls). Supports trace abstraction motivation. |
| 7 | **CRUXEval-X** (Ruiyang Xu et al.) | ACL 2025 | evaluation | Multilingual CRUXEval (19 langs). Cross-language generalization reference for VOTA's cross-model experiments. |
| 8 | **InspectCoder** (Yunkun Wang et al., arXiv 2510.18327) | arXiv 2025 | trace-compression | Strategic breakpoint placement + runtime state inspection for repair. Selective inspection philosophy aligns with VOTA's fault indicator extraction. |
| 9 | **MGDebugger** (Yuling Shi et al.) | arXiv 2410.01215 | trace-compression | Hierarchical debugging with LLM-simulated execution tracking key variables. Implicit trace abstraction. |
| 10 | **UniDebugger** (Cheryl Lee et al.) | EMNLP 2025 | debugging-agents | Multi-agent debugging without execution traces (static analysis). Orthogonal to VOTA. |
| 11 | **Seeker** (Xuanming Zhang et al.) | ICLR 2025 | debugging-agents | Exception handling with CEE knowledge base. Exception taxonomy provides complementary perspective to VOTA's exception event signals. |

---

## Threat Analysis

### Conceptual Threat: Wang et al. (EMNLP 2025 Findings) — MEDIUM-HIGH

This is the most important paper for VOTA to address. Their finding that "execution trace semantic information has limited usefulness for SFT" could be read as undermining any trace-based SFT approach. VOTA's differentiation rests on three empirical arguments:

1. **Task difference**: Wang et al. study code generation/repair (open-ended generative tasks); VOTA targets binary classification (verdict prediction). Trace signals that fail to improve generation may still serve as strong discriminative features for classification.
2. **Signal granularity**: Wang et al.'s 5 trace formats all represent execution flow at varying verbosity levels. None isolates fault indicator signals (exception type/message, assertion expected-vs-actual). VOTA's ablation shows the exception signal alone drives 99.83% accuracy — this is a qualitatively different use of trace information.
3. **Compression semantics**: Their "Concise" format reduces trace tokens but preserves the same information type. VOTA's compression is task-driven: it discards execution flow and retains only signals relevant to the pass/fail decision.

**Risk**: A reviewer familiar with Wang et al. may question whether VOTA is "yet another trace SFT paper." The response should preemptively frame VOTA as studying *which* trace signals matter for *which* tasks, not whether traces help generically.

### Methodological Threats

**vs. LLM4PatchCorrect (TSE 2024) — MEDIUM**: The closest work combining execution traces with correctness assessment. Differentiation: (a) VOTA identifies *which parts* of the trace matter (fault indicators), while LLM4PatchCorrect uses uncompressed traces; (b) SFT vs. zero-shot prompting; (c) verdict prediction vs. patch correctness. LLM4PatchCorrect should be cited as evidence that execution traces contain useful signals for correctness tasks, while noting the methodological gap VOTA addresses.

**vs. APSG + Graph-LoRA (arXiv 2025) — LOW-MEDIUM**: Concurrent work on PEFT for code correctness. Differentiation: (a) runtime signals vs. static code graphs; (b) VOTA's finding that 2 signal types suffice, vs. APSG's complex graph construction. The approaches are largely complementary — APSG could potentially benefit from incorporating runtime signals.

### Emerging Trend: Selective Trace

Multiple 2025-2026 papers (InspectCoder, TraceCoder, Runtime Traces + Multi-Agent Debate) converge on the insight that **selective trace information outperforms full traces**. VOTA aligns with this trend; its distinguishing characteristic is that the selection criterion is *decision-relevance for verdict prediction* rather than general debugging utility.

---

## Recommended Citations to Add

1. **Wang et al. "Do Code Semantics Help?"** (Findings of EMNLP 2025) — must-cite; primary conceptual challenge to address
2. **LLM4PatchCorrect** (TSE 2024) — closest work using execution traces for correctness assessment
3. **REval** (2024) — empirical evidence LLMs struggle with runtime reasoning (avg 44.4%)
4. **CodeMind** (2024) — code reasoning evaluation showing complexity-dependent degradation
5. **FuseFL** (SANER 2024) — validates test execution outcomes as discriminative signals
6. **CRUXEval-X** (ACL 2025) — cross-language generalization methodology reference
7. **InspectCoder** (Yunkun Wang et al., 2025) — selective runtime inspection trend

---

## Gap Assessment

Based on the current scan, the following gaps appear to hold:

1. **Binary verdict prediction from execution traces**: No identified work directly applies execution trace signals to pass/fail prediction via SFT. The closest (LLM4PatchCorrect) uses zero-shot prompting for a different task (patch correctness).
2. **Fault indicator signal isolation**: No identified work measures the individual contribution of exception events or assertion comparison signals to classification accuracy. VOTA's ablation results (exception_only at 99.83%) appear to be a novel empirical finding in this space.
3. **Decision-relevant trace compression for LLM classification**: Existing trace compression/selection work targets program repair or debugging, not binary classification. Whether VOTA's compression strategy generalizes beyond verdict prediction is an open question.
4. **Cross-model generalization**: Trace-based verdict prediction across different base models (Qwen, DeepSeek) has not been studied elsewhere in the surveyed literature.

These assessments are based on the 26 papers currently in the literature map. A reviewer with deeper knowledge of the software testing or mutation testing literature may identify additional related work not covered here.

---

## Search Methodology

16 query groups covering:
- "execution trace" + "fault detection" / "verdict prediction" / "test prediction"
- "trace compression" + "code understanding" / "debugging"
- "exception signal" + "fault localization"
- "VOTA" / "trace abstraction" / "verdict oriented"
- "CRUXEval" + "execution reasoning"
- "patch correctness prediction" / "automated patch assessment"
- "test outcome prediction" / "pass fail prediction"
- "selective trace" + "debugging" / "program repair"
- "code correctness prediction" / "classification"
- "error message" / "exception" + "program repair effectiveness"
- Cross-model generalization + code LLM fine-tuning
- "code semantics" + "execution trace" + "SFT" (added for Wang et al. coverage)

Sources: arXiv, ACL Anthology, IEEE Xplore, Semantic Scholar, DBLP, Google Scholar
