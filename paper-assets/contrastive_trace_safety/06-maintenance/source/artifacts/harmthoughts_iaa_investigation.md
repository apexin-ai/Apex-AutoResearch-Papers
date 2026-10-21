# HarmThoughts IAA Investigation

## Paper Info
- **Title**: When Safety Fails Before the Answer: Benchmarking Harmful Behavior Detection in Reasoning Chains
- **Authors**: Ishita Kakkar, Enze Zhang, Rheeya Uppaal, Junjie Hu
- **arXiv**: [2604.19001](https://arxiv.org/abs/2604.19001)
- **Dataset**: [huggingface.co/datasets/ishitakakkar-10/HarmThoughts](https://huggingface.co/datasets/ishitakakkar-10/HarmThoughts)
- **Scale**: 1,018 reasoning traces, 56,931 annotated sentences, 4 model families

## IAA / Agreement

**Reported.** Fleiss' kappa on human-annotated subset:
- Group 1 (7 traces, 359 sentences): **κ = 0.74** (substantial agreement)
- Group 2 (6 traces, 332 sentences): **κ = 0.80** (substantial-to-almost-perfect agreement)

**Important caveats:**
1. Human annotation covers only **13 traces (691 sentences)** out of 1,018 traces (56,931 sentences) — **1.2% of total data**
2. Full dataset annotated by **Claude Sonnet 4.6 API** with few-shot prompting (cost: $22.38)
3. Human-LLM consistency validated via **Jensen-Shannon divergence = 0.035 bits** (distributional agreement, not per-sample agreement)
4. No per-sample Cohen's κ or accuracy between human and LLM annotations is reported — only label distribution similarity

## Annotation Methodology

### Taxonomy
16 behavioral labels organized into 4 harmful types + harmless + neutral:

| Group | Labels | Description |
|-------|--------|-------------|
| Type I: Disabling Safety | RS, CR, PS | Refusal Suppression, Constraint Reframing, Performative Safety |
| Type II: Enabling Compliance | IR, PA | Intent Rationalization, Persona Adoption |
| Type III: Executing Harm | TD, DKE, HV, CE | Task Decomposition, Domain Knowledge Synthesis, Harmful Verification, Challenge Engineering |
| Type IV: Concealing Harm | OB | Obfuscation |
| Harmless | RA, AL, CC | Risk Acknowledgement, Safe Alternative, Compliance Check |
| Neutral | IA, ED, FL | Intent Assessment, Ethical Deliberation, Filler Sentences |

### Annotator Recruitment
- 12 candidates screened via taxonomy application test
- 8 selected (threshold: >60% on distinguishing similar-looking label pairs)
- Split into 2 independent groups

### Annotation Process
1. Human annotators independently labeled sentences in their assigned traces
2. Disagreements resolved via **joint review** with all annotators and paper authors
3. Final labels determined by **majority vote**
4. Disambiguation rules and refined taxonomy definitions established during adjudication

### LLM Annotation (full dataset)
- Claude Sonnet 4.6 API with few-shot prompting
- Each sentence received: original prompt, full reasoning trace, target sentence highlighted, taxonomy definitions, and few-shot examples from human-annotated set
- 33.7M input tokens, 303K output tokens

### CP (Commitment Point) — Our Project's Derivation
**HarmThoughts itself does NOT define "Commitment Point."** Our project derives CP from HarmThoughts' behavioral labels:
- SAFETY_LABELS = {RA, AL, CC, ED, IA} (Risk Acknowledgement, Safe Alternative, Compliance Check, Ethical Deliberation, Intent Assessment)
- **CP = first step after which safety-related labels permanently cease**
- Traces with oscillating safety deliberation resolved by taking the final irreversible transition
- This operationalization is ours (Section 3.1 of our paper), not from Kakkar et al.

## External Discussion

- **Citation count**: 0 (as of 2026-05-19, per Semantic Scholar)
- **No external discussion found** — the paper is very recent (April 2026)
- No other papers have questioned or validated annotation quality
- The related paper "The Point of No Return" (Merrill & Srivastava, arXiv:2605.17113) uses a different dataset for commitment point analysis but does not cite or discuss HarmThoughts

