# Supplementary Data

## Dataset Overview

This dataset accompanies the paper on generation depth profiling. It contains extracted statistical features from iterative text generation chains, where each "depth" represents one additional round of LLM rewriting from an original human-written Wikipedia passage (depth 0).

- **Total samples**: 37,058 (main) + 34,131 (detector scores)
- **Generators**: 9 models from 6 families (Pythia-2.8B, Pythia-1B, Qwen3-0.6B, Qwen3-1.7B, Qwen3-8B, OLMo-2-1B, Llama-3.2-3B, Mistral-7B-v0.3, Gemma-2-2B)
- **Model families**: 6 (Pythia, Qwen3, OLMo-2, Llama, Mistral, Gemma)
- **Depths**: 0 (human) through 4 (4th-generation LLM text)
- **Seed passages**: 1,000 Wikipedia articles, 1,500 domain-specific passages (news, creative, scientific)

## File Descriptions

### Core Data

| File | Rows | Description |
|------|------|-------------|
| `features_all_models.csv` | 37,058 | Statistical features for 8-generator main experiment |
| `detector_scores_8gen.csv` | 34,131 | Detector scores (FastDetectGPT, Binoculars) for 8 generators |
| `wiki_seed_1000.jsonl` | 1,000 | Wikipedia seed passages (depth-0 source text) |
| `features_gemma-2-2b.csv` | 4,957 | Statistical features for Gemma-2-2B (9th generator) |

### Evaluation Results

| File | Description |
|------|-------------|
| `9gen_logo_results.json` | 9-generator LOGO evaluation (3-class + binary F1, per-generator CIs) |
| `tost_bootstrap.json` | TOST bootstrap equivalence test (1000 resamples, 4 stationary features) |
| `ddr_causal_permutation.json` | DDR permutation importance (7 features, 8-fold LOGO) |
| `ddr_causal_granger.json` | DDR Granger causality (pooled panel + per-generator + Fisher combined) |
| `ddr_causal_intervention.json` | DDR feature intervention (counterfactual F1 drops) |

### Ablation Data

| File | Rows | Description |
|------|------|-------------|
| `paraphrase_features.csv` | 4,912 | Prompt-type ablation (paraphrase vs. continuation) |
| `cross-model-chains/features.csv` | 4,773 | Cross-model generation chains (mixed-generator pipelines) |
| `features_pythia-2.8b-creative.csv` | 2,466 | Multi-domain: creative writing seeds |
| `features_pythia-2.8b-news.csv` | 2,314 | Multi-domain: news article seeds |
| `features_pythia-2.8b-scientific.csv` | 2,316 | Multi-domain: scientific text seeds |
| `features_qwen3-1.7b-high-temp.csv` | 4,702 | Sampling ablation: temperature = 1.0, top_p = 0.95 |
| `features_qwen3-1.7b-low-temp.csv` | 4,810 | Sampling ablation: temperature = 0.5, top_p = 0.9 |
| `features_qwen3-0.6b-instruct.csv` | 4,923 | Instruct-tuned variant: Qwen3-0.6B-Instruct |
| `features_qwen3-1.7b-instruct.csv` | 4,963 | Instruct-tuned variant: Qwen3-1.7B-Instruct |
| `features_olmo-2-0425-1b-instruct.csv` | 4,429 | Instruct-tuned variant: OLMo-2-0425-1B-Instruct |
| `transfer_matrix.csv` | 8 | Cross-generator binary F1 transfer matrix (8x8) |
| `features_llama-3.2-3b-instruct.csv` | 4,974 | Instruct-tuned variant: Llama-3.2-3B-Instruct |
| `features_indep_pythia-2.8b.csv` | — | Independent-seed features: Pythia-2.8B (non-overlapping seeds) |
| `features_indep_olmo-2-1b.csv` | — | Independent-seed features: OLMo-2-1B (non-overlapping seeds) |
| `features_ref_olmo.csv` | — | Cross-reference features: OLMo-2-1B as reference model |
| `features_ref_qwen.csv` | — | Cross-reference features: Qwen3-0.6B as reference model |
| `features_pythia-2.8b-t05.csv` | — | Temperature ablation: Pythia-2.8B, t=0.5 |
| `features_pythia-2.8b-t09.csv` | — | Temperature ablation: Pythia-2.8B, t=0.9 |
| `features_qwen3-0.6b-t05.csv` | — | Temperature ablation: Qwen3-0.6B, t=0.5 |
| `features_qwen3-0.6b-t09.csv` | — | Temperature ablation: Qwen3-0.6B, t=0.9 |
| `features_qwen3-1.7b-t09.csv` | — | Temperature ablation: Qwen3-1.7B, t=0.9 |
| `features_olmo-2-1b-t05.csv` | — | Temperature ablation: OLMo-2-1B, t=0.5 |
| `features_olmo-2-1b-t09.csv` | — | Temperature ablation: OLMo-2-1B, t=0.9 |
| `features_qwen8b_ref_olmo.csv` | — | Qwen3-8B features extracted with OLMo-2-1B reference |
| `features_qwen8b_ref_qwen.csv` | — | Qwen3-8B features extracted with Qwen3-0.6B reference |

### Seed Passages

| File | Rows | Description |
|------|------|-------------|
| `seeds/news_seed_500.jsonl` | 500 | CNN/DailyMail news articles |
| `seeds/scientific_seed_500.jsonl` | 500 | Scientific abstracts |
| `seeds/creative_seed_500.jsonl` | 500 | Creative writing passages |

## Column Descriptions

### features_all_models.csv

| Column | Type | Description |
|--------|------|-------------|
| `model_name` | str | Generator model identifier |
| `seed_id` | int | Index of the seed passage (0-999) |
| `depth` | int | Generation depth (0 = human, 1-4 = LLM-generated) |
| `entropy_mean` | float | Mean token-level entropy from a reference LM (Pythia-410M) |
| `entropy_std` | float | Standard deviation of token-level entropy |
| `entropy_min` | float | Minimum token-level entropy |
| `entropy_max` | float | Maximum token-level entropy |
| `tail_decay` | float | Slope of entropy tail decay (linear fit to sorted entropy values) |
| `ttr` | float | Type-token ratio (unique tokens / total tokens) |
| `hapax_ratio` | float | Hapax legomena ratio (tokens appearing exactly once / unique tokens) |

### detector_scores_8gen.csv

| Column | Type | Description |
|--------|------|-------------|
| `model_name` | str | Generator model identifier |
| `seed_id` | int | Index of the seed passage |
| `depth` | int | Generation depth (0 = human, 1-4 = LLM-generated) |
| `label` | int | Binary label (0 = human, 1 = machine-generated) |
| `avg_logprob` | float | Average log-probability under reference LM |
| `fastdetectgpt` | float | FastDetectGPT detection score |
| `binoculars` | float | Binoculars detection score |

### wiki_seed_1000.jsonl

Each line is a JSON object:

| Field | Type | Description |
|-------|------|-------------|
| `id` | str | Wikipedia article ID |
| `title` | str | Article title |
| `text` | str | Full article text (truncated to first ~512 tokens for generation) |

### paraphrase_features.csv

Same columns as `features_all_models.csv`, plus:

| Column | Type | Description |
|--------|------|-------------|
| `id` | int | Sample index |
| `prompt_type` | str | Generation prompt type (e.g., "paraphrase") |

### cross-model-chains/features.csv

Same feature columns, plus:

| Column | Type | Description |
|--------|------|-------------|
| `id` | int | Sample index |
| `generator_at_depth` | str | Which model generated this specific depth |
| `chain_generators` | str | JSON list of all generators in the chain up to this depth |

### Domain-specific features (creative/news/scientific)

Same columns as `features_all_models.csv`, plus:

| Column | Type | Description |
|--------|------|-------------|
| `domain` | str | Text domain ("creative", "news", or "scientific") |

### Domain seed files (seeds/*.jsonl)

| Field | Type | Description |
|-------|------|-------------|
| `text` | str | Seed passage text |
| `seed_id` | int | Seed index (0-499) |
| `domain` | str | Domain label |

## Usage Example

```python
import pandas as pd

# Load main features
df = pd.read_csv("features_all_models.csv")

# Filter by generator and depth
pythia = df[df["model_name"] == "pythia-2.8b"]
human = df[df["depth"] == 0]
gen_d1 = df[df["depth"] == 1]

# Compare entropy between depths
print(f"Human entropy (mean): {human['entropy_mean'].mean():.4f}")
print(f"Depth-1 entropy (mean): {gen_d1['entropy_mean'].mean():.4f}")

# Load detector scores
det = pd.read_csv("detector_scores_8gen.csv")
print(f"FastDetectGPT AUC-like mean: {det.groupby('depth')['fastdetectgpt'].mean()}")
```

## License

Wikipedia seed passages are derived from Wikipedia and are available under [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/). News seeds are from CNN/DailyMail (see original dataset license). All extracted features are released under the same license as the accompanying paper.
