# Spider SQL SC Pilot Analysis (196/200)

> Analyzed 2026-05-20. 198 records in checkpoint, 196 valid (2 skipped due to gold SQL execution error). 98% of target 200 instances completed before API budget exhausted.

## 1. Configuration

| Parameter | Value |
|-----------|-------|
| Model | openai/gpt-5.5 via OpenRouter |
| Dataset | Spider dev (xlangai/spider) |
| N samples | 8 |
| Temperature | 1.0 |
| Few-shot | 3 (same-db priority) |
| Equivalence | Execution-result (not SQL text) |
| Unique DBs | 19 |

## 2. Accuracy

| Method | Exec Accuracy | vs Greedy |
|--------|--------------|-----------|
| Greedy | 0.7653 (150/196) | -- |
| Majority Vote | 0.7704 (151/196) | **+0.51pp** |
| Oracle | 0.8061 (158/196) | +4.08pp |

MV gain negligible. Only 1 instance improved by MV. Zero instances hurt.

## 3. Degeneracy Rate

**87.24% (171/196)** -- all 8 samples produce execution-equivalent results.

Dramatically higher than any NER/RE task. Mechanism: execution-result equivalence collapses syntactic SQL diversity.

- 142/171 degenerate correct (83.0%)
- 29/171 degenerate wrong (17.0%)

## 4. Agreement-Correctness Correlation

| Metric | Value |
|--------|-------|
| Spearman rho | **0.5501** (p=6.77e-17) |
| Kendall tau | **0.5259** (p=8.40e-15) |
| Mean agreement | 0.9611 |
| Median agreement | 1.0000 |

**Caveat: rho=0.55 is ceiling artifact.** 87% instances at agreement=1.0. Non-degenerate subset: rho=0.13.

## 5. Failure Mode Distribution (F1-F4 Cascade)

| Mode | Count | Rate |
|------|-------|------|
| F1 (Degeneracy) | 171 | **87.2%** |
| F2 (Low Agreement) | 0 | 0.0% |
| F3 (High Agree + Wrong) | 16 | 8.2% |
| F4 (Selection Gap) | 0 | 0.0% |
| None (SC Success) | 9 | 4.6% |

F1-dominated. Diagnostic cascade correctly identifies degeneracy as bottleneck and predicts MV ineffectiveness.

## 6. Cross-Task Comparison

| Metric | FewNERD | SciERC | CoNLL | FewRel RE | DocRED RE | Spider SQL |
|--------|---------|--------|-------|-----------|-----------|------------|
| Degen% | 10-13% | 17-27% | 85-89% | 5.9% | 3.5% | **87.2%** |
| rho (best) | 0.30-0.42 | 0.36-0.42 | 0.43-0.47 | ~0.39 | -- | **0.55*** |
| MV delta | varies | varies | ~0 | -- | -- | **+0.51pp** |
| Dominant FM | F2 | F2 | F1 | F2 | F2 | **F1** |
| Oracle headroom | 8-15pp | 12-15pp | 2.1pp | 10.2pp | 6.6pp | **4.1pp** |

*Inflated by ceiling effect; non-degenerate rho=0.13.

### Key cross-task patterns:

1. **Degeneracy dichotomy**: low-degen (FewNERD/SciERC/FewRel/DocRED: 3-27%) vs high-degen (CoNLL/Spider: 85-87%). High-degen = near-zero MV gain.
2. **Failure mode shift**: NER/RE F2-dominated; SQL/CoNLL F1-dominated.
3. **Oracle-MV gap**: Spider 4.1pp oracle headroom, 0.51pp MV gain = 87.5% unrealized potential, caused by F1.
4. **Correlation inflation**: rho=0.55 reflects degenerate clustering, not better calibration.

## 7. MV Threshold Sweep

Completely flat -- 170/196 at agreement=1.0, no threshold discriminates.

## 8. Non-Degenerate Subset (n=25)

| Method | Accuracy |
|--------|----------|
| Greedy | 0.3200 |
| MV | 0.3600 (+4.0pp) |
| Oracle | 0.6400 (+32.0pp) |

SC works when diversity exists. But only 12.8% of instances.

## 9. Sufficiency

196/200 instances. Degeneracy 95% CI: ~82-92%. rho p<1e-16. Sufficient for all diagnostic cascade analyses.

## 10. Paper Takeaway

Spider SQL = contrasting case study for cross-task universality:
- Same diagnostic framework applies (F1-F4 cascade identifies bottleneck)
- Different bottleneck (F1 degeneracy vs F2 low-agreement in NER)
- Same prediction holds (F1 dominance -> MV ineffective, confirmed)
- Mechanism is task-specific: execution-result equivalence collapses diversity
