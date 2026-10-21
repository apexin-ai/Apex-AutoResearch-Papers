# Reference Audit Results

## 1. zhou2026snowballing
- **Status**: VERIFIED
- **Title**: "From Hallucination to Structure Snowballing: The Alignment Tax of Constrained Decoding in LLM Reflection"
- **Authors**: Hongxu Zhou
- **Venue**: arXiv preprint (arXiv:2604.06066), April 2026
- **Evidence**: Paper exists on arXiv. Introduces "structure snowballing" as a failure mode where constrained decoding's formatting cognitive load traps models in structural patterns, preventing effective self-correction. Tested on Qwen3-8B. Content matches the citation description.
- **Note**: This is an arXiv preprint (single-author, master's student at Saarland University), not a peer-reviewed publication. Consider whether the citation context requires a more established reference.
- **Action**: KEEP (content matches; flag as arXiv preprint in bibliography)

## 2. upadhyay2023openie
- **Status**: VERIFIED
- **Title**: "Open Information Extraction with Entity Focused Constraints"
- **Authors**: Prajna Upadhyay, Oana Balalau, Ioana Manolescu
- **Venue**: Findings of EACL 2023
- **Evidence**: Published in ACL Anthology (aclanthology.org/2023.findings-eacl.95). Injects entity-type knowledge as constraints into Open IE via constrained inference and constraint-aware training. Reports 29.17% F1 improvement on CaRB and 24.37% on WIRe57. Code at github.com/prajnaupadhyay/openie-with-entities.
- **Action**: KEEP

## 3. regino2025kgcurator
- **Status**: VERIFIED
- **Title**: "Can LLMs be Knowledge Graph Curators for Validating Triple Insertions?"
- **Authors**: André Gomes Regino, Julio Cesar dos Reis
- **Venue**: GenAIK Workshop (co-located with COLING 2025), Abu Dhabi, pp. 87-99
- **Evidence**: Published in ACL Anthology (aclanthology.org/2025.genaik-1.10). Investigates LLMs for validating RDF triple insertions across four tasks: class/property alignment, URI standardization, semantic consistency, syntactic correctness.
- **Note**: The citation description ("multi-stage LLM pipeline") is slightly inaccurate. The paper evaluates LLMs on validation tasks rather than proposing a specific multi-stage pipeline. Also, "domain/range constraints" is a simplification of the four validation dimensions. Consider adjusting the citing text.
- **Action**: KEEP (verify citing text accuracy)

## 4. qi2024adelie
- **Status**: VERIFIED
- **Title**: "ADELIE: Aligning Large Language Models on Information Extraction"
- **Authors**: Yunjia Qi, Hao Peng, Xiaozhi Wang, Bin Xu, Lei Hou, Juanzi Li
- **Venue**: EMNLP 2024 (Main Conference)
- **Evidence**: Published in ACL Anthology (aclanthology.org/2024.emnlp-main.419). Uses SFT on IEInstruct corpus + DPO to produce ADELIE_SFT and ADELIE_DPO. Achieves SOTA among open-source models on closed/open/on-demand IE tasks. Code at github.com/THU-KEG/ADELIE.
- **Action**: KEEP

---

## Summary

| Citation | Status | Action |
|----------|--------|--------|
| zhou2026snowballing | VERIFIED (arXiv preprint) | KEEP, note as preprint |
| upadhyay2023openie | VERIFIED | KEEP |
| regino2025kgcurator | VERIFIED | KEEP, check citing text accuracy |
| qi2024adelie | VERIFIED | KEEP |

All 4 citations are real papers. No hallucinated references found.
