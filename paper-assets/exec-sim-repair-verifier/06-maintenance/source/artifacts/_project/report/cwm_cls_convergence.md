# CWM vs CLS Training Convergence

Source: trainer_state.json (HuggingFace Trainer log_history) at end of epoch 3 for each run.
All runs use identical config: LoRA rank=16, alpha=32, lr=2e-4, epochs=3, bs=2, ga=16 (effective 32), max_seq_length=2048, seed varies by run.

## Function-level (4B + 8B): eval_loss by epoch

| Run                    | Epoch 1 | Epoch 2 | Epoch 3 | Val-best step (epoch) | Min train_loss |
|------------------------|---------|---------|---------|-----------------------|----------------|
| CWM 4B (seed=123)      | 0.0676  | **0.0589** | 0.0680 | 956 (ep 2)           | 0.0135 @ ep 2.83 |
| CLS 4B (seed=0)        | 0.1069  | **0.0823** | 0.0963 | 956 (ep 2)           | 0.0194 @ ep 2.93 |
| CWM 8B (seed=42)       | 0.0554  | **0.0512** | 0.0564 | 956 (ep 2)           | 0.0139 @ ep 2.83 |
| CLS 8B (seed=42)       | **0.0723** | 0.0741 | 0.0783 | 478 (ep 1)          | 0.0194 @ ep 2.83 |

## Repo-level 8B (s42, currently running ckpt-4400 / 6633): eval_loss

CWM 8B repo-level (eval every 100 steps):
- Min eval_loss = **0.2862 @ step 400 (epoch 0.18)** — earliest checkpoint after warmup
- Monotonic INCREASE thereafter: 0.30 → 0.40 → 0.47 (step 4400, ep 1.99)
- Train_loss continues to drop: 0.0220 (step 4050) → 0.0130 (step 4400)
- **Severe overfitting from epoch 0.18 onward**

CLS 8B repo-level (eval every 200 steps):
- Min eval_loss = **0.0796 @ step 200 (epoch 0.09)**
- Plateau / bounce range 0.25–0.41 since step 600
- Train_loss noisy 0.17–0.46, no clear monotonic trend
- **Plateau reached by epoch 0.27**

## Currently running rank=32 ablation

- Exp ID: `cwm-rank32-ablation`
- Server: seetacloud-westd-4x5090 cuda:0, PID 368823 (tmux session `cwm-rank32-ablation`)
- Config: `train_cwm_baseline.py --lora_rank 32 --seed 42 --batch_size 2 --grad_accumulation 16 --no_wandb` (rest = baseline defaults)
- Output: `/home/sonny/exec-sim-repair-verifier/checkpoints_cwm_rank32/`
- Total steps: 1434. At step 122/1434 (~8%) after duplicate killed; 3.35 s/it now (was 4.1 s/it when competing). ETA ~1h20m to completion + auto-eval on `eval_cwm_baseline.py`.
- Duplicate `cwm-4b-rank32-ablation` (PID 369497, bs=1/ga=32, same effective batch but slower and non-canonical) was killed at ~5 min to free GPU.
