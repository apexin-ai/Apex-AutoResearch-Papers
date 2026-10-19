# Experiment Analysis: mvp_c1_s42

```yaml
conclusion: success
final_train_loss: 0.4426 (avg over 3 epochs), last logged: 0.2437 (epoch 2.998)
final_eval_loss: N/A (no eval dataset configured)
checkpoint_path: /root/tbab_multi_turn/checkpoints/c1_lora_only_seed42
total_epochs: 3
total_steps: 471
train_runtime: 5761s (~1.6h)
train_samples_per_second: 1.302
train_steps_per_second: 0.082
wandb_run_id: sgftthsz (offline mode, no cloud sync)
adapter_size: 335MB (adapter_model.safetensors)
total_checkpoint_size: 4.1GB (includes 4 intermediate checkpoints: 3, 157, 314, 471)
trainable_params: 83,886,080 / 7,325,618,176 (1.15%)
exit_code: 0
issues: none
```

## Loss Trajectory

| Epoch Range | Loss Range | Notes |
|-------------|-----------|-------|
| 0.0 - 1.0  | 0.67 → 0.61 | Initial convergence |
| 1.0 - 2.0  | 0.46 → 0.43 | Steady decrease, second epoch |
| 2.0 - 3.0  | 0.32 → 0.24 | Continued improvement, no overfitting signs |

## Configuration Verified
- Model: Mistral-7B-Instruct-v0.1
- Condition: C1_lora_only (use_bridge_tokens=False, use_position_reset=False)
- Seed: 42
- Dataset: 2500 samples (ShareGPT 1500 + UltraChat 1000)
- Labels correctly masked for instruction tokens (loss only on response tokens)
