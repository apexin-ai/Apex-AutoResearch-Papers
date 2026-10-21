# GoLLIE & SciERC RE F1 Baselines

## Key Finding: GoLLIE Does NOT Report Zero-Shot SciERC RE F1

GoLLIE (Sainz et al., ICLR 2024) uses SciERC as one of 8 **supervised training** RE datasets (alongside ACE05, ADE, CoNLL04, GIDS, kbp37, NYT, SemEval RE). It is **not** a zero-shot evaluation target for RE in GoLLIE.

- **Model**: CodeLlama (7B / 13B / 34B), fine-tuned with QLoRA
- **Supervised RE results reported only on ACE05**:
  - GoLLIE-7B: 63.6 F1
  - GoLLIE-13B: 67.5 F1
  - GoLLIE-34B: 70.1 F1
- **Zero-shot evaluation**: Only on NER (CrossNER domains) and EE/EAE (CASIE), not RE
- **SciERC RE F1**: Not reported (SciERC was in-domain training data)
- **DocRED results**: Not reported



---

## Supervised SciERC Joint Entity-Relation Extraction SOTA

**Evaluation protocol**: SciERC uses span-level evaluation for joint entity-relation extraction.
- **Ent**: Entity NER F1 (span boundary + type)
- **Rel**: Relation F1 (entity boundary match, ignoring entity type)
- **Rel+**: Strict Relation F1 (entity boundary + entity type + relation type must all match)

| Method | Type | Ent F1 | Rel F1 | Rel+ F1 | Year | Venue |
|--------|------|--------|--------|---------|------|-------|
| DyGIE++ | Span-graph | 67.5 | 48.4 | — | 2019 | EMNLP |
| SpERT | Span-based | 68.0 | 47.6 | 34.6 | 2020 | ECAI |
| PURE | Pipeline | 66.6 | 48.2 | 35.6 | 2021 | NAACL |
| UniRE | Unified table | 68.4 | — | 36.9 | 2021 | ACL |
| UIE | Seq2seq | — | — | 36.5 | 2022 | ACL |
| PFN | Table-filling | 66.8 | — | 38.4 | 2022 | ACL |
| ATG | Autoregressive | 69.7 | 51.1 | 38.6 | 2024 | AAAI |
| MGE | Multi-granular | 68.4 | — | 39.4 | — | — |
| PL-Marker | Span-pair | **69.9** | 53.2 | 41.6 | 2022 | ACL |
| FSN | Filter-sep | 69.5 | **54.2** | **42.3** | 2024 | Sensors |

**Supervised SOTA**: Rel F1 = 54.2 (FSN), Rel+ F1 = 42.3 (FSN)

---

## LLM-Based SciERC RE Results

**Important caveat**: These results may use different evaluation protocols than the joint extraction models above. AgentRE/GPT-RE likely use a relation classification or triplet extraction setup that may differ from the strict span-level joint evaluation above. Direct comparison requires protocol alignment.

| Method | Model | Setting | RE F1 | Year | Venue |
|--------|-------|---------|-------|------|-------|
| CodeKGC | — | Zero-shot | 20.12 | — | — |
| AgentRE | LLM-agent | Zero-shot | 23.14 | 2024 | CIKM |
| GPT-RE | text-davinci-003 | Few-shot (ICL) | 26.75 | 2023 | EMNLP |
| AgentRE | LLM-agent | Few-shot | 33.70 | 2024 | CIKM |
| GPT+ASP | GPT-4 | 10% train data | 38.23 (micro) | 2025 | arXiv |
| InstructUIE | — | SFT | 45.15 | — | — |
| AgentRE | Llama-2-7b | SFT (full) | 62.42 | 2024 | CIKM |
| GPT-RE | text-davinci-003 | SFT (full) | 69.00 | 2023 | EMNLP |

---

## Other Zero-Shot RE Models (Not Evaluated on SciERC)

| Method | Datasets | Best Zero-shot F1 | Model | Year |
|--------|----------|-------------------|-------|------|
| GLiREL | Wiki-ZSL, FewRel | 83.28 / 94.20 (m=5) | DeBERTa-v3-large (467M) | 2025 NAACL |
| ChatGPT+SumAsk | TACRED | 79.6 (micro) | gpt-3.5-turbo | 2024 |
| GoLLIE-34B | ACE05 RE (supervised) | 70.1 | CodeLlama-34B | 2024 ICLR |

---

## Sources

- GoLLIE: Sainz et al. (2024). "GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction." ICLR 2024. https://arxiv.org/abs/2310.03668
- AgentRE: CIKM 2024. https://arxiv.org/abs/2409.01854
- GPT-RE: Wan et al. (2023). "GPT-RE: In-context Learning for Relation Extraction." EMNLP 2023. https://arxiv.org/abs/2305.02105
- ATG: "An Autoregressive Text-to-Graph Framework for Joint Entity and Relation Extraction." AAAI 2024. https://arxiv.org/abs/2401.01326
- FSN: "Joint Entity and Relation Extraction Based on Filter Separator Network." Sensors 2024. https://pmc.ncbi.nlm.nih.gov/articles/PMC10887558/
- GLiREL: "Generalist Model for Zero-Shot Relation Extraction." NAACL 2025. https://arxiv.org/abs/2501.03172
- LLM+ASP: "An LLM + ASP Workflow for Joint Entity-Relation Extraction." 2025. https://arxiv.org/abs/2508.12611
- PL-Marker: Ye et al. (2022). ACL 2022.
- PURE: Zhong & Chen (2021). NAACL 2021.
