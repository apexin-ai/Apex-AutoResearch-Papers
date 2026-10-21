# Citation Cross-Check Report: related_work.md vs literature_map.yaml

**Date**: 2026-05-16  
**Related Work cite keys**: 47  
**Literature Map entries**: 101  
**Issues found**: 11

---

## A. Missing from literature_map (1)

Papers cited in related_work.md but absent from literature_map.yaml:

| Cite Key | Paper | Context in RW |
|----------|-------|---------------|
| `seo2024qblora` | Q-BLoRA (TACL 2025) | Sec 4: "identifies an imbalance between overly complex adapter I/O and insufficient trainability in quantized LLMs" |

**Action**: Add Q-BLoRA to literature_map.yaml with role `key_evidence` — directly supports the quantization-amplifies-decoupling argument.

---

## B. Missing from related_work (6)

Entries in literature_map.yaml with role `direct-competitor` or `method-component` not cited in related_work.md:

### Direct Competitors (1)

| Lit Map Idx | Paper | Role | Recommendation |
|-------------|-------|------|----------------|
| 64 | **OREO**: Offline RL for LLM Multi-Step Reasoning | direct-competitor | Consider adding to Sec 4 (RL for Structured Generation) — offline RL alternative to online GRPO |

### Method Components (5)

| Lit Map Idx | Paper | Role | Recommendation |
|-------------|-------|------|----------------|
| 52 | **DocGNRE**: Semi-automatic Data Enhancement for DocRE with Distant Supervision | method-component | Add to Sec 1 (DocRE) — data augmentation baseline relevant to evidence annotation scarcity |
| 63 | **Posterior-GRPO**: Rewarding Reasoning Processes in Code Generation | method-component | Add to Sec 4 (RL) — process-level reward design relevant to CED reward |
| 87 | **Inference-Aware Fine-Tuning for BoN** | method_component | Add to Sec 3 (RSFT/BoN) — directly relevant to CED-based BoN reranking |
| 92 | **FaithLens**: Detecting and Explaining Faithfulness Hallucination | method_component | Add to Sec 2 (Evidence-Based IE) — faithfulness detection tool relevant to CED metric |
| 93 | **PrefixNLI**: Detecting Factual Inconsistencies as Soon as They Arise | method_component | Add to Sec 2 (Evidence-Based IE) — incremental NLI relevant to evidence verification |

> Note: Only 1 direct-competitor is missing (OREO). No critical gap (threshold was >3 for red flag).

---

## C. Role Inconsistencies (4)

| Cite Key | Lit Map Role | RW Description | Suggested Role |
|----------|-------------|----------------|----------------|
| `autore2024` | background | Described as introducing "Relation-Head-Facts paradigm with QLoRA fine-tuning" — a specific competing method | `related_method` |
| `glidre2025` | background | Described as "extending generative approach to zero/few-shot settings with lightweight dual-encoder" — specific method contribution | `related_method` |
| `qerl2025` | direct-competitor | Described as showing "standard quantization introduces deterministic noise harmful to RL exploration" — empirical finding, not a competing DocRE system | `key_evidence` |
| `rift2026` | direct_competitor | Described as RSFT variant "replacing hard rejection with soft reweighting" for math reasoning — not a DocRE competitor | `method_component` |

---

## D. Q-BLoRA Status

- **In related_work.md**: YES — cited as `\cite{seo2024qblora}` in Sec 4
- **In literature_map.yaml**: **NOT FOUND**
- **Relevance**: High — supports core claim that QLoRA amplifies evidence-extraction decoupling
- **Action required**: Add to literature_map.yaml (suggested role: `key_evidence`)

---

## Summary

| Category | Count | Severity |
|----------|-------|----------|
| Missing from literature_map | 1 | Medium — Q-BLoRA is actively cited |
| Missing from related_work (direct-competitor) | 1 | Low — only OREO |
| Missing from related_work (method-component) | 5 | Medium — FaithLens and PrefixNLI are relevant to evidence verification narrative |
| Role inconsistencies | 4 | Low — cosmetic, but qerl2025 and rift2026 inflate direct-competitor count |
| **Total** | **11** | |

### Priority Actions
1. **Add Q-BLoRA to literature_map.yaml** — the only paper cited in RW without a literature map entry
2. **Add FaithLens + PrefixNLI to related_work Sec 2** — both directly relevant to evidence-based IE narrative
3. **Add Inference-Aware BoN FT to Sec 3** — directly relevant to CED-based BoN reranking
4. **Fix role for qerl2025 and rift2026** in literature_map.yaml — neither is actually a direct DocRE competitor
