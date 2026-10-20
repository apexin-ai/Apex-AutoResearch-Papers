# AI Text Detection & Model Collapse — Research Patterns

25 papers (8 deep-read, 17 abstract). Domain: LLM text detection + model collapse + data quality.

## Method Trends

**Rising**: Zero-shot statistical scoring: DetectGPT→Fast-DetectGPT(340x)→Binoculars(>90%@0.01%FPR)→DivEye(+33.2%). Continuous/ordinal replacing binary (EditLens, CLOC). Detection-as-collapse-mitigation (Drayson 2025). Verifier-based filtering: short-term gains, long-term converges to verifier center (Yi 2026). **Declining**: Supervised binary classifiers OOD (MAGE: 0.99→0.93 AUROC). Support: 8/8, high.

## Baselines & Metrics

DetectGPT(8/25)>RoBERTa(5/25)>Binoculars≈Fast-DetectGPT(4/25). New work must benchmark Binoculars+Fast-DetectGPT.

AUROC dominant(12/25) but misleading under imbalance(Two Paradigms)—supplement PR-AUC. TPR@low-FPR for deployment. Collapse: FID(4/25), perplexity(4/25), entropy as diagnostic(r=0.91, Closer Look). Support: high.

## Datasets

Detection: MAGE(7dom×27LLM), RAID(2.6M), PAN'24(15LLM). Legacy trio: XSum/SQuAD/WritingPrompts. Collapse: CIFAR-10/FFHQ/MNIST(image), Wikitext-103/BabiStories(LM). Quality: FineWeb 15T tokens.

## Experimental Consensus (6/8)

1. Cross-domain+cross-model eval mandatory (MAGE,Two Paradigms,Ghostbuster)
2. Paraphrasing robustness required—recall drops 30-40% (MAGE,Ghostbuster,DivEye)
3. Progressive difficulty testbeds as narrative (MAGE:8 scenarios)
4. Collapse: 8-60 rounds, per-round FID/entropy trajectory

## Common Limitations

Short text <100 tokens: universal degradation (4/8). Newest LLMs closing gap: GPT-4o entropy≈human >4K chars; o1 undetectable (Two Paradigms). Paraphrasing breaks all (3/8; Ghostbuster 99→62%). Theory assumes Gaussian/linear (4/8).

## Research Gaps

- **No paper estimates recursive generation depth**—detection binary/ternary only
- Detection×collapse barely connected (only Drayson); no work diagnoses how many generations
- Ordinal framing (EditLens,CLOC) unapplied to depth
- Strong Collapse proves mixing fails unless synthetic→0, but no depth-aware curation proposed

## Competitor Map

Foundation(9): DetectGPT,Two Paradigms,Tale of Tails,Strong Collapse,Closer Look,Broken Telephone,Ghostbuster,Demystified,survey. Competitor(6): MAGE,Binoculars,Fast-DetectGPT,DivEye,Intrinsic Dim,EditLens. Complementary(7): FineWeb,QuRating,Escaping Collapse,Drayson,Synthetic Eggs,LOKI,CLOC. Orthogonal(2): watermark,text degeneration.
