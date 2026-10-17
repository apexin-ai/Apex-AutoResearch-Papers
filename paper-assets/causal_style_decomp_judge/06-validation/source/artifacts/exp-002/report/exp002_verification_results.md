# exp-002 Content Verification Results

## Setup
- Model: Qwen3-32B via vLLM
- Protocol: RATE double-rewrite (detect → flip → flip back)
- Axis: formality (formal ↔ casual)
- BERTScore model: microsoft/deberta-xlarge-mnli
- NLI model: cross-encoder/nli-deberta-v3-large
- Thresholds: BERTScore ≥ 0.92, NLI ≥ 0.90 (joint)

## AlpacaEval (100 samples)

### Original vs Counterfactual
- BERTScore: mean 0.8594, std 0.1093
- NLI: mean 0.8618, std 0.3250
- Joint pass: 20/100 (20.0%)

### Original vs Double-Rewrite
- BERTScore: mean 0.8438, std 0.1229
- NLI: mean 0.8576, std 0.3141
- Joint pass: 18/100 (18.0%)

## MT-Bench (80 samples)

### Original vs Counterfactual
- BERTScore: mean 0.8855, std 0.0900
- NLI: mean 0.9152, std 0.2469
- Joint pass: 26/80 (32.5%)

### Original vs Double-Rewrite
- BERTScore: mean 0.8842, std 0.0905
- NLI: mean 0.9579, std 0.1514
- Joint pass: 26/80 (32.5%)

## Remote file paths
- verified_alpacaeval.jsonl: /root/causal_style_decomp_judge/data/verified_alpacaeval.jsonl (100 records)
- verified_mtbench.jsonl: /root/causal_style_decomp_judge/data/verified_mtbench.jsonl (80 records)
- counterfactuals_alpacaeval.jsonl: /root/causal_style_decomp_judge/data/counterfactuals_alpacaeval.jsonl (100 records)
- counterfactuals_mtbench.jsonl: /root/causal_style_decomp_judge/data/counterfactuals_mtbench.jsonl (80 records, deduplicated)
- Server: westb-29275, account: root