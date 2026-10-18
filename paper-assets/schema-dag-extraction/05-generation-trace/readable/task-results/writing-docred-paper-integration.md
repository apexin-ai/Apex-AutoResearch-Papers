# writing docred paper integration

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_writing_docred_paper_integration_20260516T050933_result.json`
- **Structured JSON:** [`39447e6b910ec3b5b06b.json`](../../sessions/39/39447e6b910ec3b5b06b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All consistent. Summary of modifications:

**Files modified (6):**

1. **`abstract.tex`** — Added DocRED RE degradation stats (88.0%→38.7% with 96 types); changed "three datasets" → "four datasets"

2. **`introduction.tex`** — Added DocRED to dataset list (96 relation types, document-level); updated findings summary with DocRED slope/R²; updated contribution items to reference four datasets

3. **`experimental_setup.tex`** — Added DocRED dataset paragraph; added row to Table 1 (96 types, doc-level RE, cross-domain); added DocRED count levels {1,4,8,16,32,64,96}; added DocRED to BCS-controlled design (count∈{16,32}); updated metrics section

4. **`results.tex`** — Added "Document-level RE (DocRED)" paragraph in count curves (88%→38.7%, 56% relative drop); added DocRED BCS-controlled paragraph (slope=-0.713, gap 23.3pp at count 16, 17.6pp at count 32, R²=0.525); updated summary and figure caption

5. **`discussion.tex`** — Updated conclusion with DocRED replication stats (count decline -49pp, BCS slope=-0.71, R²=0.53)

6. **`references.bib`** — Added `docred-2019` citation (Yao et al., ACL 2019)

7. **`checklist.tex`** — Updated "three datasets" → "four datasets"

**Task count consistency:** 3 IE tasks (NER, RE, ED) × 4 datasets (Few-NERD, FewRel, DocRED, MAVEN) — unified across all sections.

**All numbers from artifacts:** count curve (88.0%→38.7%), BCS gaps (23.3pp, 17.6pp), slopes (-0.713, -0.690), CIs ([-0.909,-0.529], [-0.854,-0.519]), R² (0.525, 0.443), Spearman (-0.661, -0.509), quartile gaps (18.7pp, 10.5pp).

---
