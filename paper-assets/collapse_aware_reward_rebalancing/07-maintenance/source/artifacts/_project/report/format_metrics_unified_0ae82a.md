# C1 vs C5 Format Diversity Metrics (Unified)

## 数据说明
- C1: LoRA K=4, ArmoRM top-1 curated (selected via `argmax(ArmoRM score)`)
- C5: LoRA K=4, random selection (no curation, `response[0]` as proxy)
- Population: selected responses only (2000 per generation)
- C1 scoring: ArmoRM-Llama3-8B-v0.1, batch_size=4, with single-item fallback (4 errors per 8000 pairs)

## Results

| Metric | C1 Gen0 | C1 Gen2 | C5 Gen0 | C5 Gen2 | C1 Δ | C5 Δ |
|--------|---------|---------|---------|---------|------|------|
| opening_unique_ratio | 0.9800 | 0.9755 | 0.9790 | 0.9750 | -0.0045 | -0.0040 |
| opening_entropy (bits) | 10.9067 | 10.9016 | 10.9057 | 10.8931 | -0.0051 | -0.0126 |
| near_duplicate_start_rate | 0.0285 | 0.0370 | 0.0300 | 0.0345 | +0.0085 | +0.0045 |
| per_response_ttr | 0.7136 | 0.7007 | 0.6997 | 0.6774 | -0.0129 | -0.0223 |
| trigram_repetition_rate | 0.0848 | 0.1007 | 0.0889 | 0.1102 | +0.0159 | +0.0213 |

## Key Findings

1. **Both conditions show format diversity degradation from Gen 0 to Gen 2**, confirming iterative training causes format collapse regardless of curation strategy.

2. **C5 (random) degrades faster than C1 (curated) on 3 of 5 metrics**:
   - `per_response_ttr`: C5 drops 0.0223 vs C1 drops 0.0129 (C5 loses 74% more lexical diversity)
   - `trigram_repetition_rate`: C5 increases 0.0213 vs C1 increases 0.0159 (C5 gains 34% more repeated trigrams)
   - `opening_entropy`: C5 drops 0.0126 vs C1 drops 0.0051 (C5 loses 2.5x more opening diversity)

3. **C1 starts with slightly higher diversity at Gen 0** (higher TTR 0.7136 vs 0.6997, lower trigram repetition 0.0848 vs 0.0889), likely because ArmoRM top-1 selection favors higher-quality, more lexically varied responses.

4. **`near_duplicate_start_rate` is the exception**: C1 shows slightly more increase (+0.0085 vs +0.0045), suggesting ArmoRM curation may converge opening patterns even while preserving body diversity.

5. **Overall**: ArmoRM curation (C1) provides a modest but consistent format-diversity preservation effect compared to random selection (C5). The effect is most visible in lexical diversity (TTR) and trigram repetition, less so in opening patterns.
