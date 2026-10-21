# paper research oracle upper bound

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_research_oracle_upper_bound_20260517T175752_result.json`
- **Structured JSON:** [`0c8fba8087ea2a724877.json`](../../sessions/0c/0c8fba8087ea2a724877.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Both files updated correctly. Here's a summary of the 3 papers added to the `oracle_upper_bound_experiments` dimension:

| Paper | Venue | arXiv | Oracle Methodology |
|-------|-------|-------|-------------------|
| **Press et al.** "Measuring and Narrowing the Compositionality Gap" | EMNLP Findings 2023 | 2210.03350 | Oracle sub-question decomposition to diagnose that compositional reasoning (not knowledge) is the bottleneck |
| **Trivedi et al.** "IRCoT: Interleaving Retrieval with Chain-of-Thought" | ACL 2023 | 2212.10509 | Gold supporting paragraphs as oracle retrieval upper bound to isolate retrieval as the multi-step QA bottleneck |
| **Saparov & He** "Language Models Are Greedy Reasoners" | ICLR 2023 | 2210.01240 | Gold FOL proofs on synthetic data to diagnose that proof planning (not individual deduction) is the CoT bottleneck |

All three are verified, marked `status: should_cite`, and provide direct methodological precedent for the SICA oracle control experiment (replacing self-extracted FOL with gold FOLIO annotations to isolate extraction quality as the bottleneck).

---
