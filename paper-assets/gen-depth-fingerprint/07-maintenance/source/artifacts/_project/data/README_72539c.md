# Supplementary Data

## Dataset Overview

This dataset accompanies the paper on generative-depth fingerprinting. It contains extracted statistical features from iterative text generation chains, where each "depth" represents one additional round of LLM rewriting from an original human-written Wikipedia passage (depth 0).

- **Total samples**: 27,529 (main) + 34,131 (detector scores)
- **Generators**: 6 core models (Pythia-2.8B, Pythia-1B, Qwen3-0.6B, Qwen3-1.7B, Qwen3-8B, OLMo-2-1B) + 2 held-out models (Llama-3.2-3B, Mistral-7B-v0.3)
- **Model families**: 4 (Pythia, Qwen3, OLMo-2, + held-out Llama/Mistral)
- **Depths**: 0 (human) through 4 (4th-generation LLM text)
- **Seed passages**: 1,000 Wikipedia articles, 1,500 domain-specific passages (news, creative, scientific)

## File Descriptions

### Core Data

| File | Rows | Description |
|------|------|-------------|
| `features_all_models.csv` | 27,529 | Statistical features for 6-generator main experiment |
| `detector_scores_8gen.csv` | 34,131 | Detector scores (FastDetectGPT, Binoculars) for 8 generators |
| `wiki_seed_1000.jsonl` | 1,000 | Wikipedia seed passages (depth-0 source text) |

### Ablation Data

| File | Rows | Description |
|------|------|-------------|
| `paraphrase_features.csv` | 4,912 | Prompt-type ablation (paraphrase vs. continuation) |
| `cross-model-chains/features.csv` | 4,773 | Cross-model generation chains (mixed-generator pipelines) |
| `features_pythia-2.8b-creative.csv` | 2,466 | Multi-domain: creative writing seeds |
| `features_pythia-2.8b-news.csv` | 2,314 | Multi-domain: news article seeds |
| `features_pythia-2.8b-scientific.csv` | 2,316 | Multi-domain: scientific text seeds |
| `features_qwen3-1.7b-high-temp.csv` | 4,702 | Sampling ablation: temperature = 1.2 |
| `features_qwen3-1.7b-low-temp.csv` | 4,810 | Sampling ablation: temperature = 0.5 |
| `features_qwen3-0.6b-instruct.csv` | 4,923 | Instruct-tuned variant: Qwen3-0.6B-Instruct |
| `features_qwen3-1.7b-instruct.csv` | 4,963 | Instruct-tuned variant: Qwen3-1.7B-Instruct |
| `features_olmo-2-0425-1b-instruct.csv` | 4,429 | Instruct-tuned variant: OLMo-2-0425-1B-Instruct |

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
