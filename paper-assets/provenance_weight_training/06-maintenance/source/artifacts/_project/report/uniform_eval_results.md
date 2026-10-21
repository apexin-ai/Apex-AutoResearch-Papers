# Uniform OOD Eval Results

**Date:** 2026-05-20
**Server:** westd-41312
**Model:** Qwen3-0.6B, uniform weighting, contamination_ratio=0.4
**Eval script:** `eval_perplexity.py` (max_docs=5000, max_length=2048, stride=1024, fp16)

## In-distribution verification

| Seed | Expected PPL | Actual PPL | Delta | Status |
|------|-------------|-----------|-------|--------|
| 123 | 17.686 | 17.686 | +0.000 | PASS |
| 456 | 17.702 | 17.702 | -0.001 | PASS |

Both within tolerance (+-0.01). Proceeding to OOD eval.

## OOD Results

### OpenWebText

| Seed | PPL |
|------|-----|
| 42 | 18.37 (existing) |
| 123 | 18.37 |
| 456 | 18.39 |
| **Mean +- Std** | **18.37 +- 0.01** |

### Wikipedia

| Seed | PPL |
|------|-----|
| 42 | 15.34 (existing) |
| 123 | 15.38 |
| 456 | 15.36 |
| **Mean +- Std** | **15.36 +- 0.02** |

## Raw results (full precision)

### Holdout (in-distribution)
- seed123: loss=2.8728, ppl=17.6861, tokens=4077068, time=166.8s
- seed456: loss=2.8737, ppl=17.7015, tokens=4077068, time=120.4s

### OpenWebText
- seed123: loss=2.9106, ppl=18.3678, tokens=6767242, time=142.8s
- seed456: loss=2.9116, ppl=18.3865, tokens=6767242, time=140.1s

### Wikipedia
- seed123: loss=2.7329, ppl=15.3768, tokens=27000339, time=374.9s
- seed456: loss=2.7317, ppl=15.3594, tokens=27000339, time=373.9s

## Adaptive training progress
- adaptive_ood_seed123: COMPLETED (EXIT_CODE=0), saved to output/models/adaptive_ood_seed123/final
- adaptive_ood_seed456: COMPLETED (EXIT_CODE=0), saved to output/models/adaptive_ood_seed456/final

## Commands used

```bash
# In-dist holdout eval (GPU 2/3 parallel)
CUDA_VISIBLE_DEVICES=2 python eval_perplexity.py --checkpoints output/models/uniform_ood_seed123/final --data_path data/human/eval_holdout.jsonl --max_docs 5000 --max_length 2048 --output_path /tmp/eval_holdout_seed123.json
CUDA_VISIBLE_DEVICES=3 python eval_perplexity.py --checkpoints output/models/uniform_ood_seed456/final --data_path data/human/eval_holdout.jsonl --max_docs 5000 --max_length 2048 --output_path /tmp/eval_holdout_seed456.json

# OOD eval (GPU 2: seed123, GPU 3: seed456, OWT then Wiki sequential per GPU)
CUDA_VISIBLE_DEVICES=2 python eval_perplexity.py --checkpoints output/models/uniform_ood_seed123/final --data_path data/eval_openwebtext.jsonl --max_docs 5000 --max_length 2048 --output_path /tmp/eval_owt_seed123.json
CUDA_VISIBLE_DEVICES=2 python eval_perplexity.py --checkpoints output/models/uniform_ood_seed123/final --data_path data/eval_wikipedia.jsonl --max_docs 5000 --max_length 2048 --output_path /tmp/eval_wiki_seed123.json
CUDA_VISIBLE_DEVICES=3 python eval_perplexity.py --checkpoints output/models/uniform_ood_seed456/final --data_path data/eval_openwebtext.jsonl --max_docs 5000 --max_length 2048 --output_path /tmp/eval_owt_seed456.json
CUDA_VISIBLE_DEVICES=3 python eval_perplexity.py --checkpoints output/models/uniform_ood_seed456/final --data_path data/eval_wikipedia.jsonl --max_docs 5000 --max_length 2048 --output_path /tmp/eval_wiki_seed456.json
```
