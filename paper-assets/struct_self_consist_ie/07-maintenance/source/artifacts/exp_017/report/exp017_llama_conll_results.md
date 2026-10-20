## LLaMA CoNLL Results (exp-017)

### Training
- Model: Meta-Llama-3.1-8B-Instruct
- Checkpoint: `checkpoints/llama3.1-8b-conll2003-lora/` (LoRA adapter)
- Epochs: 5, Steps: 4390, Batch size: 2
- Training loss (final): 0.0392
- Training runtime: 8523s (~2.4h)

### Inference
- Output: `output/exp_017_llama_conll_infer/samples.jsonl`
- N=8, T=1.0, seed=42
- n_instances: 3453
- gold-filtered n: 2756
- conditional n: 2642

### QE Analysis (gold-filtered, full, n=2756)

| Signal | ρ | AUROC | Sel F1 | Δ vs Greedy |
|--------|-------|-------|--------|-------------|
| LP     | .307  | .761  | .9244  | +0.03pp     |
| SJ     | .431  | .704  | .9237  | -0.04pp     |
| FK     | .428  | .703  | .9245  | +0.03pp     |
| EM     | .431  | .705  | .9244  | +0.02pp     |
| VC     | .426  | .709  | .9233  | -0.09pp     |
| Greedy | —     | —     | .9242  | —           |
| Oracle | —     | —     | .9426  | +1.84pp     |

### QE Analysis (conditional, n=2642)

| Signal | ρ | AUROC |
|--------|-------|-------|
| LP     | .328  | .810  |
| SJ     | .436  | .723  |
| FK     | .431  | .721  |
| EM     | .440  | .726  |
| VC     | .374  | .699  |

### Additional Metrics
- Degeneracy (F1-based, gold-filtered): 89.2%
- LP range: mean=0.0198, std=0.0315, median=0.0002
- Within-instance ρ(LP, F1): median=0.512, mean=0.217, n_valid=298/2756 (65.1% positive, 56.7% > 0.3)
  - 1957 instances excluded (constant F1), 501 excluded (constant LP)

### Cross-model Comparison (N=8, T=1.0, CoNLL-2003)

| Metric | Qwen-2.5-7B (exp_002) | LLaMA-3.1-8B (exp_017) |
|--------|----------------------|------------------------|
| Greedy F1 | .908 | .927 |
| Oracle F1 | .947 | .944 |
| Headroom | 3.94pp | 1.77pp |
| Degeneracy | 59.1% | 89.2% |
| SJ ρ (full) | .436 | .431 |
| FK ρ (full) | .400 | .428 |
| EM ρ (full) | .451 | .431 |
| VC ρ (full) | .424 | .426 |
| LP ρ (full) | .316 | .307 |
| Best ρ signal | EM (.451) | SJ/EM (.431) |
| LP AUROC | .753 | .761 |
| SJ Sel Δ | -0.89pp | -0.04pp |
| LP Sel Δ | -1.05pp | +0.03pp |
| EM Sel Δ | -1.04pp | +0.02pp |

### 结论

1. **LLaMA vs Qwen degeneracy**: LLaMA 远高于 Qwen（89.2% vs 59.1%）。LLaMA Greedy F1 更高（.927 vs .908），意味着更多 instance 所有 sample 都是正确的，headroom 很小（1.77pp vs 3.94pp）。

2. **QE signal ranking 跨 backbone 一致性**:
   - 两个模型的 ranking correlation (ρ) 模式一致：structural signals (SJ/FK/EM) > surface signal (LP)
   - SJ ρ: Qwen .436 ≈ LLaMA .431，差异 <0.01
   - LP ρ: Qwen .316 ≈ LLaMA .307，差异 <0.01
   - ρ-AUROC dissociation 在两个模型上都成立：LP 的 AUROC (.753/.761) > structural (.70-.71/.70-.71)，但 ρ 最低

3. **Selection F1 差异显著**: Qwen 所有 signal 的 selection 都低于 greedy（-0.89 to -1.53pp），而 LLaMA 基本持平（±0.09pp）。这直接由 degeneracy 差异驱动——LLaMA 89.2% instance 所有 sample F1 相同，selection 几乎无法产生影响。

4. **Within-instance ρ(LP, F1)**: LLaMA 中 LP 与 F1 的 instance 内相关为正（median=0.512），但仅有 298/2756 instance 有足够变异来计算此指标。
