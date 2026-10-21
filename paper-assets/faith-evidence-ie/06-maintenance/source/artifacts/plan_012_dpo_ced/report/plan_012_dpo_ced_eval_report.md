# Plan 012: DPO + CED Preference Learning — Eval Report

## Conclusion: **NEGATIVE**

DPO with CED-constructed preference pairs **degraded** relation extraction below the SFT baseline. The model produces well-formatted outputs with good evidence quality, but relation F1 regressed by 15.5% relative to SFT.

---

## Training Summary

| Item | Value |
|------|-------|
| Method | DPO (trl DPOTrainer) with CED preference pairs (top-1 chosen, bottom-1 rejected) |
| Base model | Qwen3-4B → merge SFT LoRA → new DPO LoRA |
| LoRA config | r=64, alpha=128, dropout=0.05 |
| DPO pairs | 2666 (from dpo_pairs.jsonl) |
| Training | 3 epochs, 501 steps, 1h41m |
| Final train_loss | 0.2925 |
| rewards/accuracies | 1.0 |
| rewards/margins | 9.01 |
| rewards/chosen | -4.76 |
| rewards/rejected | -13.77 |
| EXIT_CODE | 0 (success) |

## Dev Eval Results (985 docs, 12275 gold triples)

| Metric | DPO CED | SFT | RSFT CED mean | bf16 GRPO G=8 | QLoRA GRPO |
|--------|---------|-----|---------------|---------------|------------|
| **rel_f1** | **0.3429** | 0.4057 | 0.4596 | 0.4549 | 0.2167 |
| evi_f1 | 0.8403 | — | — | — | — |
| edcr | 0.7294 | — | — | — | — |
| format_ok | 99.5% (980/985) | — | — | — | — |
| n_predictions | 18445 | — | — | — | — |
| n_truncated | 260/985 | — | — | — | — |

### Detailed Metrics
- Precision: 0.3244, Recall: 0.3638
- Evi precision: 0.8647, Evi recall: 0.8172
- Field compliance: 73.1%, Evidence format: 73.0%
- Inference time: 6411s (6.51 s/doc), 124 batches

## Analysis

1. **rel_f1=0.3429 < SFT=0.4057**: DPO training caused a -15.5% relative degradation in relation extraction. This is below the SFT baseline, indicating the DPO optimization hurt core task performance.

2. **Evidence quality preserved**: evi_f1=0.8403 and edcr=0.7294 are strong, suggesting DPO successfully learned evidence citation patterns from CED preference pairs, but at the cost of relation accuracy.

3. **Format compliance excellent**: 99.5% parseable outputs — the model structure is intact.

4. **Overfitting signals in training**: rewards/accuracies=1.0 and rewards/margins=9.01 suggest the DPO model perfectly separated chosen/rejected during training, indicating possible overfitting to the preference signal rather than learning generalizable improvements.

5. **Better than QLoRA GRPO** (0.2167) but this is a low bar — QLoRA GRPO suffered from catastrophic forgetting due to quantization.

## Verdict

DPO with offline CED preference pairs is **not a viable replacement** for online GRPO in this setting. The preference signal from CED top-1/bottom-1 pairs appears insufficient or misaligned for improving relation extraction — the model learns to differentiate chosen/rejected perfectly in training (acc=1.0) but this doesn't transfer to better generation at inference time. This is a known failure mode of DPO when preference pairs are too easy to distinguish.

Possible next steps (if pursuing DPO further):
- Use harder preference pairs (e.g., top-1 vs mid-ranked instead of top-1 vs bottom-1)
- Reduce training epochs (1 instead of 3) to mitigate overfitting
- Try IPO or KTO as alternatives to DPO
- Increase preference pair diversity
