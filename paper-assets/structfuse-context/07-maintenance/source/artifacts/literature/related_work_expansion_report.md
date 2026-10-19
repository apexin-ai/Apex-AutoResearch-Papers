# Related Work Expansion Report — StructFuse
**Date**: 2026-05-14

## Summary
Literature map expanded from ~22 entries (6 needing verification) to **37 verified entries** across 7 categories. All "需验证" flags resolved. 15 new papers added, 2 existing entries corrected.

---

## New Papers Added (15)

### Category 1: Code Retrieval / SWE-bench (+2)

| Paper | Venue | Year | Relation to StructFuse |
|-------|-------|------|----------------------|
| **SweRank**: Software Issue Localization with Code Ranking | arXiv | 2025 | Text-based retrieve-and-rerank baseline for SWE-bench; direct comparison target |
| **SWE-Fixer**: Training Open-Source LLMs for Effective and Efficient GitHub Issue Resolution | ACL Findings | 2025 | BM25 + LLM retriever pipeline; another text-based retrieval competitor |

### Category 2: Hard Negative Mining (+1, +1 replacement)

| Paper | Venue | Year | Relation to StructFuse |
|-------|-------|------|----------------------|
| **CoCoHaNeRe**: Effective Hard Negative Mining for Contrastive Learning-Based Code Search | ACM TOSEM | 2025 | **CRITICAL**: Claim 1 correction target. See note below. |
| **CL-DRD**: Curriculum Learning for Dense Retrieval Distillation | SIGIR (Best Short Paper) | 2022 | Replaces the unverified "curriculum HN mining" entry |

### Category 3: Contrastive Learning for Code (NEW category, +3)

| Paper | Venue | Year | Relation to StructFuse |
|-------|-------|------|----------------------|
| **ContraCode**: Contrastive Code Representation Learning | EMNLP | 2021 | Self-supervised contrastive pre-training via compiler transformations |
| **CodeRetriever**: A Large Scale Contrastive Pre-Training Method for Code Search | EMNLP | 2022 | Unimodal + bimodal contrastive pre-training for code search |
| **Towards Learning (Dis)-Similarity of Source Code from Program Contrasts** | ACL Long Papers | 2022 | Moved from Cat 4; title and venue corrected |

### Category 4: Program Analysis (+1)

| Paper | Venue | Year | Relation to StructFuse |
|-------|-------|------|----------------------|
| **ARISE**: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair | arXiv | 2025 | Intra-procedural def-use + runtime tool API; contrasts with StructFuse's inter-procedural static mining |

### Category 5: Code Embeddings (+2)

| Paper | Venue | Year | Relation to StructFuse |
|-------|-------|------|----------------------|
| **DeepSeek-Coder**: When the Large Language Model Meets Programming | arXiv | 2024 | Alternative code LLM backbone reference |
| **RepoFusion**: Training Code Models to Understand Your Repository | arXiv | 2023 | Cross-file repo context fusion for code completion |

### Category 6: Graph-Guided Inference (NEW category, +3)

| Paper | Venue | Year | Relation to StructFuse |
|-------|-------|------|----------------------|
| **LocAgent**: Graph-Guided LLM Agents for Code Localization | ACL | 2025 | Inference-time graph navigation; complementary to StructFuse's training-time structural signal |
| **CodexGraph**: Bridging LLMs and Code Repositories via Code Graph Databases | NAACL | 2025 | Graph DB interface for code retrieval at inference |
| **RANGER**: Repository-Level Agent for Graph-Enhanced Retrieval | arXiv | 2025 | Repo knowledge graph + MCTS exploration |

### Category 7: Infrastructure (NEW category, +2)

| Paper | Venue | Year | Relation to StructFuse |
|-------|-------|------|----------------------|
| **FAISS**: Billion-Scale Similarity Search with GPUs | IEEE Trans Big Data | 2021 | ANN library used for embedding-based hard negative mining |
| **Tree-sitter**: Incremental Parsing System | Software (Zenodo) | 2018 | Parsing tool; no formal paper, cite via Zenodo DOI |

---

## Verification Results

### Previously "需验证" — Now Resolved

| Entry | Status | Change |
|-------|--------|--------|
| SWE-smith venue | **Corrected** | arXiv → **NeurIPS 2025 D&B Spotlight** |
| SWE-smith authors | **Corrected** | Added Kilian Lieret, Kabir Khandpur, Yanzhe Zhang, Binyuan Hui, Ludwig Schmidt, Diyi Yang |
| RepoBench year/venue | **Confirmed** | ICLR 2024 ✓ |
| FA-AST authors/venue | **Confirmed** | Wenhan Wang et al., SANER 2020 ✓ |
| StarCoder venue | **Confirmed** | TMLR 2023 ✓ |
| Qwen2.5-Coder title/year | **Confirmed** | arXiv 2024 ✓ |
| Contrastive Learning paper | **Corrected** | Title: "Towards Learning (Dis)-Similarity of Source Code from Program Contrasts"; Venue: ACL 2022 Long Papers (not Findings) |
| Curriculum HN mining | **Replaced** | Was placeholder → Now: CL-DRD (Zeng et al., SIGIR 2022 Best Short Paper) |

---

## CoCoHaNeRe — Critical Finding

**Full citation**: Fan Y., Li C., Ge J., Huang L., Luo B. "Effective Hard Negative Mining for Contrastive Learning-Based Code Search." ACM TOSEM, Vol 34, No 3, 2025. DOI: 10.1145/3695994.

**Important nuance for Claim 1 framing**: CoCoHaNeRe does NOT explicitly claim that "embedding-distance hard negatives harm code search." Its argument is that using non-differentiable embedding negatives makes learning "slow and ineffective," and proposes differentiable gradient-based hard negatives as a solution. The paper's position is about the mechanism (differentiable vs. non-differentiable), not about whether embedding-distance negatives are inherently harmful.

**Implication for StructFuse Claim 1**: The "correcting misconception" framing should be adjusted. Instead of "CoCoHaNeRe claims embedding negatives harm performance," the accurate framing is: "CoCoHaNeRe characterizes non-differentiable embedding negatives as ineffective and proposes gradient-based alternatives; we show that simple embedding-distance mining (without gradient coupling) consistently improves retrieval, challenging the premise that more complex mechanisms are necessary."

---

## What's NOT Included (and why)

| Paper/Tool | Reason |
|------------|--------|
| **GRACE** (code-specific) | No well-known paper called "GRACE" for general code representation. Multiple GRACE papers exist (graph contrastive learning, vulnerability detection) but none match the intended scope. |
| **Aider** | Software tool, no formal paper. Can be mentioned in text as an SWE-bench method but not a citable reference. |
| **Moatless Tools** | Software tool by Albert Orwall. The associated paper is **SWE-Search** (Antoniades et al., ICLR 2025) — could be added if SWE-bench retrieval coverage needs strengthening. |
| **CoSQA** | Not searched; lower priority for this paper's scope. |

---

## Citation Count by Category

| Category | Count |
|----------|-------|
| Code Retrieval / SWE-bench | 8 |
| Hard Negative Mining | 6 |
| Contrastive Learning for Code | 3 |
| Program Analysis for ML | 6 |
| Code Embeddings / Search | 9 |
| Graph-Guided Inference | 3 |
| Infrastructure / Tools | 2 |
| **Total** | **37** |

---

## Recency Distribution

| Period | Count |
|--------|-------|
| 2025 | 10 |
| 2024 | 6 |
| 2023 | 3 |
| 2022 | 5 |
| 2021 | 4 |
| 2020 | 4 |
| 2019 | 4 |
| ≤2018 | 1 |

27% of citations are from 2025, 70% from 2022+. Recency is strong.
