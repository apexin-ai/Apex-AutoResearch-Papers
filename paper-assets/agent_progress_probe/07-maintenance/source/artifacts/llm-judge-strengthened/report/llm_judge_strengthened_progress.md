# LLM-as-Judge Strengthened Evaluation — Progress Report (2026-05-15)

## Status Summary

| Variant | Model | Mode | Progress | Status |
|---------|-------|------|----------|--------|
| 1 | Claude Sonnet 4.6 | few-shot | 1824/1824 | ✅ DONE |
| 2 | Claude Sonnet 4.6 | cot | 150/1824 (8%) | 🔄 Running |
| 3 | Claude Sonnet 4.6 | few-shot-cot | 0/1824 | ⏳ Queued (after CoT) |
| 4 | GPT-5.5 | zero-shot | 1400/1824 (77%) | 🔄 Running |
| 5 | GPT-5-mini | zero-shot | 0/1824 | ❌ Failed (model_not_found) |

## Results

### Completed: Claude Sonnet 4.6, few-shot (1824/1824)
- **macro_f1 = 0.7514** | accuracy = 0.7703
- f1_stagnation = 0.6828 | f1_progress = 0.8199
- precision_macro = 0.7525 | recall_macro = 0.8212
- parse_failures = 0 | cost = $36.08

### Partial: GPT-5.5, zero-shot (1400/1824)
- **macro_f1 = 0.7604** | accuracy = 0.7631
- f1_stagnation = 0.7348 | f1_progress = 0.7860
- precision_stag = 0.6024 | recall_stag = 0.9418
- precision_prog = 0.9555 | recall_prog = 0.6676
- parse_failures = 315 (22.5%) | cost = $8.87 (projected ~$11.5)

### Partial: Claude Sonnet 4.6, CoT (150/1824)
- macro_f1 = 0.6250 (too early, only 8%)
- f1_stag = 0.4500 | f1_prog = 0.8000
- parse_failures = 0 | cost = $1.43

## Comparison with Baseline (zero-shot)

| Metric | Claude zero-shot | Claude few-shot | Δ | GPT-5.5 zero-shot* |
|--------|-----------------|-----------------|---|---------------------|
| macro_f1 | 0.6625 | **0.7514** | +0.089 (+13.4%) | **0.7604** |
| f1_stag | 0.6055 | **0.6828** | +0.077 (+12.8%) | **0.7348** |
| f1_prog | 0.7195 | **0.8199** | +0.100 (+13.9%) | 0.7860 |
| cost | $11.66 | $36.08 | 3.1x | ~$11.5 (proj.) |
| fails | 0 | 0 | — | 315 (22.5%) |

*GPT-5.5 partial (1400/1824, 77%), metrics may shift.

## Key Observations

1. **Few-shot prompting substantially improves Claude**: +13.4% macro_f1 over zero-shot, but at 3.1x cost
2. **GPT-5.5 competitive on macro_f1** (0.7604) but has high parse failure rate (22.5%) — those windows get no prediction
3. **GPT-5.5 has interesting precision/recall asymmetry**: very high stag recall (0.94) but low stag precision (0.60); very high prog precision (0.96) but low prog recall (0.67) — essentially a conservative "default to stagnation" judge
4. **GPT-5-mini not available** on OpenRouter — killed the process
5. **Claude CoT too early to evaluate** at 8% completion

## Running Processes
- PID 215405: Claude few-shot→cot→few-shot-cot (currently on cot, ~8%)
- PID 216929: GPT-5.5 zero-shot (~77%)

## Missing Variants
- Claude Sonnet 4.6, cot — in progress
- Claude Sonnet 4.6, few-shot-cot — pending
- GPT-5-mini — failed, would need different model ID or provider
