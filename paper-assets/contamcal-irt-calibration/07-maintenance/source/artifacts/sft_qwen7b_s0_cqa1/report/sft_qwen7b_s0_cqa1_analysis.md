# sft_qwen7b_s0_cqa1 Training Analysis

## Conclusion: SUCCESS

All 5 dosage levels completed training. Process exited with code 0. Marker `ALL_DONE_QWEN7B_S0` confirmed.

## Configuration
- Model: Qwen2.5-7B (LoRA r=16, alpha=32, lr=5e-5)
- Seed: 0 (third seed after s42, s123)
- GPU: cuda:0 on cqa1-21977
- Epochs: 1, batch=1, grad_accum=16, max_seq_length=2048, gradient_checkpointing=True

## Training Metrics

| Dosage | Train Loss | Token Acc | Runtime (h) | Steps |
|--------|-----------|-----------|-------------|-------|
| d000   | 0.9259    | 0.7891    | 3.73        | 3125  |
| d005   | 0.9297    | 0.7774    | 3.90        | —     |
| d025   | 0.9427    | 0.7705    | 3.90        | —     |
| d050   | 0.9595    | 0.7782    | 4.12        | —     |
| d100   | 0.9884    | 0.7615    | 4.31        | 4159  |

Total wall time: ~19.9 hours.

## Observations
- Loss increases monotonically with dosage (0.926 → 0.988), consistent with higher contamination dosage introducing more distributional shift.
- Token accuracy decreases with dosage (0.789 → 0.762), same pattern.
- Runtime increases with dosage due to larger training data at higher dosage levels.
- All adapter_model.safetensors are 155M, consistent across dosages.

## Checkpoint Integrity
All 5 checkpoints verified at `/root/autodl-tmp/exp001/checkpoints/Qwen2.5-7B_d{000,005,025,050,100}_s0/lora_adapter/`:
- adapter_model.safetensors: 155M ✓
- adapter_config.json: lora_alpha=32 ✓
- tokenizer files: present ✓
- training_args.bin: present ✓

## Next Steps
- Run eval on all 5 checkpoints to measure dose-response curve for s0
- Compare with s42 and s123 results for triple-seed bootstrap CI
