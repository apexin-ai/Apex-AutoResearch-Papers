# LOFO Non-Qwen Reframing Results

## Source Files (cqa1-22115)
- results/lofo_theta_validation/lofo_nonqwen_reframing.json
- results/lofo_theta_validation/lofo_nonqwen_reframing_table.tex

## Non-Qwen Derivation (5 families)

| Family | 1v2 ci_lower | K* at θ=0.60 | K* at θ=0.58 |
|--------|-------------|--------------|--------------|
| Gemma-2B | 0.5882 | 1 | 2 |
| OLMo | 0.6045 | 2 | 2 |
| Pythia-1.4B | 0.6454 | 2 | 2 |
| LLaMA-8B | 0.6028 | 2 | 2 |
| Mistral-7B | 0.5835 | 1 | 2 |

Non-Qwen consensus θ̂ range: (0.5417, 0.5835]

## Qwen Validation (3 models)

| Qwen Model | 1v2 ci_lower | K* at θ̂=0.58 | margin |
|------------|-------------|---------------|--------|
| Qwen-1.5B-rw | 0.6859 | 2 | +0.1059 |
| Qwen-1.5B-cont | 0.6015 | 2 | +0.0215 |
| Qwen-7B | 0.6080 | 2 | +0.0280 |

## Director Decision: Option A — keep θ=0.60 as conservative lower bound
Paper framing: "Including Gemma-2B narrows the consensus range to [0.57, 0.59]; θ=0.60 sits above this interval, making K* assignments conservative lower bounds."
