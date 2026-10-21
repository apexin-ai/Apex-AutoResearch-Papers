# Tokenization Analysis: CodeLlama vs 3 Models (tail-2048)

## Key Stats

| Model | Vocab | Chars/Token | Avg Tokens | Content Retained | Tokens Lost |
|---|---|---|---|---|---|
| Qwen-7B | 151K | 3.03 | 1929 | 100% | ~1 |
| Qwen-1.5B | 151K | 3.03 | 1929 | 100% | ~1 |
| CodeLlama-13B | 32K | 2.49 | 2341 (1.21x) | 83.3% | 412 |
| DeepSeek-6.7B | 32K | 2.29 | 2551 (1.32x) | 74.4% | 692 |

## Core Finding

**Tokenization cannot fully explain CodeLlama's failure.** DeepSeek retains only 74.4% of content (worse than CodeLlama's 83.3%) but achieves 95-97.9% accuracy. Token inflation is systematic but not fatal — DeepSeek has similar vocab size and worse inflation yet learns normally.

## Label Analysis
All models encode pass/fail as single token. Label = 0.051% of 2048-token sequence. With label_only_loss, only 1 token per sequence contributes gradient.

## Likely Root Cause
Model architecture/LoRA interaction compound effect, not tokenization alone. CodeLlama (Llama-2 based) may need larger max_length or different LoRA config for long-sequence verdict tasks.