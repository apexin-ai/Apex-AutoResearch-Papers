# Qwen3 TRAJ Repo-Level Training Launch Config

**Target**: GPU 3 on seetacloud-westd-4x5090, after CWM s123 e2 eval completes (~04:15 UTC May 19)

## IMPORTANT: Model Availability

**Qwen3-4B is NOT on the server.** Available Qwen3 models:
- `/root/autodl-tmp/models/Qwen/Qwen3-8B`
- `/root/autodl-tmp/models/Qwen/Qwen3-32B`

Commands below use **Qwen3-8B**.

## Data

- Path: `data/swebench_full/`
- Data prefix: `traj`
- Train: `traj_train.jsonl` (386 lines, SWE-bench verified repo-level diffs)
- Val: `traj_val.jsonl` (43 lines)
- Test: `traj_test.jsonl` (48 lines)

## DeepSeek TRAJ Repo Reference (8k variant)

- Checkpoint: `/root/autodl-tmp/checkpoints_deepseek_traj_repo_8k/`
- Config: batch_size=1, grad_accum=8, max_seq=8192, epochs=3, lr=2e-4
- 49 steps/epoch, 147 total steps, best at epoch 2 (step 98)
- eval_loss: epoch1=0.159, **epoch2=0.122 (best)**, epoch3=0.145
- Test: 81.25% acc (+27.08pp over majority baseline)
- Training time: ~0.65 GPU-hr

## Training Command

```bash
cd /home/sonny/exec-sim-repair-verifier && \
CUDA_VISIBLE_DEVICES=3 HF_HUB_OFFLINE=1 /root/miniconda3/bin/python train_traj_verifier.py \
  --data_dir data/swebench_full/ \
  --model_name /root/autodl-tmp/models/Qwen/Qwen3-8B \
  --output_dir /root/autodl-tmp/checkpoints_qwen3_8b_traj_repo/ \
  --run_name qwen3-8b-traj-repo \
  --seed 42 \
  --max_seq_length 8192 \
  --batch_size 1 \
  --grad_accumulation 8 \
  --lr 2e-4 \
  --epochs 3 \
  --lora_rank 16 \
  --lora_alpha 32 \
  --no_wandb
```

## Eval Command (run after training)

```bash
cd /home/sonny/exec-sim-repair-verifier && \
CUDA_VISIBLE_DEVICES=3 HF_HUB_OFFLINE=1 /root/miniconda3/bin/python eval_traj_verifier.py \
  --data_dir data/swebench_full/ \
  --checkpoint_dir /root/autodl-tmp/checkpoints_qwen3_8b_traj_repo/best \
  --model_name /root/autodl-tmp/models/Qwen/Qwen3-8B \
  --output /root/autodl-tmp/checkpoints_qwen3_8b_traj_repo/eval_test_s42.json \
  --max_seq_length 8192 \
  --batch_size 1
```

## Time Estimate

- Qwen3-8B is ~1.2x DeepSeek-6.7B model size
- LoRA training, so forward pass dominates; marginal overhead from larger model
- **Estimate: ~0.75-0.85 GPU-hr (~45-51 min)**
- Eval on 48 test samples: ~2-3 min

## Potential Issues

1. **Qwen3 thinking mode**: The training script already handles this via `detect_thinking_support()`, which sets `enable_thinking=False` for Qwen3's chat template. No action needed.

2. **Memory**: Qwen3-8B at seq_len=8192 with LoRA (rank 16) + bf16 + gradient checkpointing on 32GB 5090. Should fit with batch_size=1. If OOM, reduce max_seq_length to 4096 (DeepSeek non-8k variant got similar results with max_seq=2048, eval_loss=0.111 vs 0.122).

3. **Tokenizer**: Qwen3 uses a different tokenizer from DeepSeek. Repo-level diffs are long, so some examples may truncate differently. The script logs truncation stats, check those.

4. **Multi-seed runs**: DeepSeek had 6 seeds (42, 0, 123, 456, 789, 999). If Qwen3 s42 results are promising, follow up with additional seeds.

## Fallback if OOM

```bash
# Option A: reduce seq length
--max_seq_length 4096

# Option B: increase grad accumulation, still batch=1
--batch_size 1 --grad_accumulation 8
# (already at these values, so try Option A first)
```
