# Diagnosis: sweep-isr-b02-s42 EXIT_CODE=129

## Verdict: FALSE ALARM — Training Completed Successfully

EXIT_CODE=129 (SIGHUP) was caused by the tmux session closing after the training process exited normally. The tmux session `sweep-isr-b02-s42` no longer exists (only `sweep-isr-b02-s43` is active), confirming the session was cleaned up post-completion.

## Evidence

### Training completed 500/500 steps
- Last log line: `[REWARD_LOG] step=500 reward=0.9792 prove_rate=0.875 isr=0.521 parse_rate=1.000 beta_t=0.2000`
- Final model saved at 2026-05-16 12:52:22 → 12:52:46 (24s save time)
- Final stats: `parse_rate=1.0, prove_rate=0.63025, mean_isr=0.36565`
- Train runtime: 2500.3s (~41.7 min), train_loss=0.00494

### Checkpoint status
- **Full final model**: `/root/autodl-tmp/outputs/sweep_isr_b02_s42_v2/` — 4 safetensors shards (~15GB)
- **checkpoint-500**: `/root/autodl-tmp/outputs/sweep_isr_b02_s42_v2/checkpoint-500/` — 4 safetensors shards (~15GB) + trainer_state.json
- **reward_log.jsonl**: 126KB, present in output_dir root
- Both copies are complete and usable

### GPU status (12:54:53 UTC)
- GPU 0: 85430MiB / 97887MiB, 93% util — PID 633515 (sweep-isr-b02-s43 running)
- GPU 1: 0MiB / 97887MiB, 0% util — **free** (sweep-isr-b02-s42 finished and released)

### Disk status
- `/root/autodl-tmp/`: 212G / 250G used (85%), 39G free
- ⚠️ Two copies of model weights (~30GB total) in output_dir. Consider deleting checkpoint-500/ to reclaim ~15GB.

### tmux status
- Only `sweep-isr-b02-s43` session active (PID 633507)
- `sweep-isr-b02-s42` session already cleaned up

## Root cause of EXIT_CODE=129
Training process completed normally and exited. The tmux session received SIGHUP (signal 1 → exit code 128+1=129) as part of standard session teardown. The monitoring system captured the exit code of the tmux session shell, not the Python training process.

## Action items
- **No retry needed** — training is complete with full outputs
- Registry should be updated: conclusion=success
- Proceed directly to eval with checkpoint at `/root/autodl-tmp/outputs/sweep_isr_b02_s42_v2/`
- Consider deleting `checkpoint-500/` subdirectory to free ~15GB (disk at 85%)
