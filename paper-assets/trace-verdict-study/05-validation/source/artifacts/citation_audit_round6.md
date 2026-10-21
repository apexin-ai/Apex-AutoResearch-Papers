# Citation Audit — Round 6 (R-BIB fix)

## 1. dong2024composition

- **BibTeX key**: dong2024composition
- **Issue**: Orphan citation (in .bib but not cited in text)
- **Verification**: Paper is "How Abilities in Large Language Models are Affected by Supervised Fine-tuning Data Composition" by Guanting Dong, Hongyi Yuan, Keming Lu, et al., published at ACL 2024 (https://aclanthology.org/2024.acl-long.12/). The paper studies how SFT data composition affects LLM abilities (math reasoning, code generation, instruction following). It is about general LLM training dynamics, not about test verdict prediction or trace analysis.
- **Current status**: Already removed from current `references.bib` and not cited in any .tex file. No action needed.
- **Recommendation**: **No action required.** Entry was already cleaned up in a prior round. If re-adding is desired (e.g., to support SFT training methodology discussion), it should be cited in the training section, but this is not necessary for the current paper's narrative.

## 2. foster2025mutation

- **BibTeX key**: foster2025mutation
- **Issue**: Author mismatch (bib says "foster", OpenAlex flagged "harman")
- **Verification**: The paper is "Mutation-Guided LLM-based Test Generation at Meta" (arXiv:2501.12862, FSE 2025 Industry Track). Full author list: **Christopher Foster**, Abhishek Gulati, **Mark Harman**, Inna Harper, Ke Mao, Jillian Ritchey, Herve Robert, Shubho Sengupta. Foster IS the first author; Harman is a co-author (3rd position). The bib key `foster2025mutation` is correct by convention (first-author-based). OpenAlex likely flagged Harman because he is the most prominent author in the mutation testing field.
- **Current bib entry problem**: Uses `author={Christopher Foster and others}` which is incomplete. Should list all 8 authors.
- **Recommendation**: **Expand author list** to: `Christopher Foster and Abhishek Gulati and Mark Harman and Inna Harper and Ke Mao and Jillian Ritchey and Herv{\'e} Robert and Shubho Sengupta`. Keep bib key as `foster2025mutation`. No other changes needed.

## 3. widyasari2024fusefl

- **BibTeX key**: widyasari2024fusefl
- **Issue**: Title mismatch (text calls it "FuseFL" but bib title does not contain "FuseFL")
- **Verification**: The paper is "Demystifying Faulty Code: Step-by-Step Reasoning for Explainable Fault Localization" by Ratnadira Widyasari, Jia Wei Ang, Truong Giang Nguyen, Neil Sharma, and David Lo, published at SANER 2024 (arXiv:2403.10507). **FuseFL is the method name proposed within the paper**, not part of the official title. The bib title is correct and matches the real publication title exactly.
- **Current bib entry**: Title, authors, venue, and year are all correct.
- **Recommendation**: **No change needed.** The bib title correctly reflects the official paper title. Using the method name `fusefl` in the bib key is a common and acceptable convention. The in-text reference to "FuseFL" is appropriate when discussing the method.

---

## Summary

| Key | Issue | Verdict | Action |
|-----|-------|---------|--------|
| dong2024composition | Orphan citation | Already removed | None |
| foster2025mutation | Author "and others" | Incomplete author list | Expand to full 8 authors |
| widyasari2024fusefl | FuseFL not in title | Title is correct; FuseFL is the method name | None |

**Only actionable fix**: Expand `foster2025mutation` author field.
