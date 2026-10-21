# DPO Rebuilt 3-Epoch Eval Analysis

## Conclusion: NEGATIVE — 3 epochs confirms overfitting

ign_f1 dropped from 0.3223 (1ep) to 0.3076 (3ep), a **-4.6% relative decline**. The hypothesis is confirmed: additional DPO training beyond 1 epoch hurts downstream RE performance.

## Metrics Comparison (3ep vs 1ep)

| Metric | 1ep | 3ep | Δ (abs) | Δ (%) |
|--------|-----|-----|---------|-------|
| **ign_f1** | 0.3223 | 0.3076 | -0.0147 | **-4.6%** |
| ign_precision | 0.2787 | 0.2765 | -0.0022 | -0.8% |
| ign_recall | 0.3820 | 0.3466 | -0.0354 | **-9.3%** |
| f1 | 0.3338 | 0.3145 | -0.0193 | -5.8% |
| precision | — | 0.2939 | — | — |
| recall | — | 0.3381 | — | — |
| **edcr** | 0.8123 | 0.7503 | -0.0620 | **-7.6%** |
| evi_f1 (TP) | 0.8090 | 0.8484 | +0.0394 | +4.9% |
| evi_f1_joint | — | 0.2451 | — | — |
| format_ok_rate | 0.997 | 0.997 | 0 | 0% |
| n_truncated | 175 | 220 | +45 | **+25.7%** |
| n_predictions | — | 24637 | — | — |
| n_documents | — | 985 | — | — |

## Key Findings

1. **Recall is the primary casualty**: ign_recall dropped 9.3% while ign_precision barely moved (-0.8%). The model became more conservative — extracting fewer relations overall.

2. **EDCR degraded significantly** (-7.6%): The model cites more distractor sentences (28464 distractor citations out of 37937 total). Longer training made evidence selection noisier.

3. **evi_f1 (TP) paradoxically improved** (+4.9%): For the relations the model *does* correctly extract, evidence quality is better. But this is offset by extracting fewer correct relations.

4. **Generation length increased** (n_truncated 175→220, +25.7%): The model produces longer outputs, hitting the 2048-token cap more often. This is consistent with DPO overfitting — the model learns to be verbose rather than precise.

5. **Training accuracy kept rising** (ep1 ~0.78 → ep3 ~0.87) while eval performance dropped — textbook overfitting to the preference data.

## Training Curve Summary (from trainer_state.json)

- **Epoch 1** (steps 1–187): accuracy 0.47 → 0.78, loss 0.69 → 0.48. Rapid learning phase.
- **Epoch 2** (steps 188–374): accuracy 0.78 → 0.86, loss ~0.40–0.46. Diminishing returns.
- **Epoch 3** (steps 375–561): accuracy fluctuates 0.83–0.91, loss ~0.27–0.36. Overfitting to training preferences.

## Recommendation

**1 epoch is the optimal DPO training duration.** Do not train beyond 1 epoch for this task. Future DPO experiments should use the 1ep checkpoint as the reference point.

## Config

- Base model: Qwen3-4B
- SFT adapter: /root/autodl-tmp/sft_output
- DPO adapter: /root/autodl-tmp/dpo_output_rebuilt_3ep
- Eval data: DocRED dev (985 docs)
- Eval time: ~3h55m (14077s)
