# NLP Control: Llama-2-7b-chat R² Probing Results

## Key Finding: Zero Exit Collapse

R² ≈ 0.155 constant across all 32 layers. Δ = 0.000.

## Per-layer Summary
- Peak: 0.1555 (L15)
- Exit: 0.1555 (L31)
- Min: 0.1547, Max: 0.1555, Mean: 0.1553
- Profile: flat constant (noise baseline)

## Interpretation
- R² ≈ 0.155 = between-task variance / total variance (noise floor)
- NLP-finetuned model has identical hidden states for same text across all timesteps
- Ridge regression can only fit task-mean action, not timestep-specific variation
- Confirms exit collapse is VLA-specific, not a general LLM/fine-tuning artifact

## Comparison with VLA (same Llama-2-7B backbone)
| Model | R² peak | R² exit | Δ |
|-------|---------|---------|---|
| Llama-2-7b-chat (NLP) | 0.156 | 0.156 | 0.000 |
| OpenVLA-Goal (VLA) | 0.869 | 0.853 | 0.016 |
| OpenVLA-Spatial (VLA) | 0.845 | 0.735 | 0.110 |
| OpenVLA-Object (VLA) | 0.787 | 0.666 | 0.121 |
| OpenVLA-Long (VLA) | 0.871 | 0.867 | 0.004 |