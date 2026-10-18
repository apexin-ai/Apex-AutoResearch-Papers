# paper writing method

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_writing_method_20260515T092702_result.json`
- **Structured JSON:** [`c9cbe8e7256278120d1c.json`](../../sessions/c9/c9cbe8e7256278120d1c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`section_method.tex` written and registered. Structure:

- **§3.1 Problem Definition** — formalizes the recursive generation chain, defines ordinal classification over depths $d \in \{0, \dots, K\}$
- **§3.2 Benchmark Construction** — 3 models × 3 strategies × 4 depths, 180K samples, LoRA pipeline, fixed GPT-2 base reference model
- **§3.3 Statistical Feature Design** — 19-dim feature vector in 4 categories with compact `tab_features` table; describes each category with rationale
- **§3.4 Effective Discriminable Depth** — defines EDD_T (Eq. 1), binary RF per adjacent pair, default T=0.75, classifier summary

Note: `main.tex` uses `\input{method}` — you'll need to either rename the file to `method.tex` or update the input path.

---
