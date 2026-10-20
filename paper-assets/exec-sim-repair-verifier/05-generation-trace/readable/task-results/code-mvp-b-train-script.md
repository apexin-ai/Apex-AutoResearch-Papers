# code mvp b train script

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_mvp-b-train-script_20260511T190206_result.json`
- **Structured JSON:** [`0517c704ca58314e2305.json`](../../sessions/05/0517c704ca58314e2305.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry-run complete. Summary:

**Scripts created:**
- `/home/sonny/exec-sim-repair-verifier/train_verifier.py` (222 lines)
- `/home/sonny/exec-sim-repair-verifier/eval_verifier.py` (235 lines)

**Dry-run results (Qwen3-0.6B, 2 steps):**
- Status: success
- Per step: ~1.0s/step (0.6B model; 4B will be ~5-7x slower ≈ 5-7s/step)
- Loss: 5.06 (expected for untrained model)
- LoRA params: 4.59M / 600.6M total (0.76% trainable)
- Truncation: 10/15290 (0.1%) train, 0/1896 val — `max_seq_length=2048` covers 99.9% of data
- VRAM: freed after exit; estimate for 4B model: ~15-20GB of 32GB (comfortable)

**Estimated full training time (Qwen3-4B):**
- ~478 steps/epoch × 3 epochs = ~1,434 steps
- At ~6s/step ≈ 2.4 hours

**To launch full training:**
```bash
cd /home/sonny/exec-sim-repair-verifier
python train_verifier.py \
  --data_dir data/ \
  --model_name Qwen/Qwen3-4B \
  --output_dir checkpoints/ \
  --wandb_project exec-sim-repair-verifier \
  --seed 42
```

**To evaluate after training:**
```bash
python eval_verifier.py \
  --data_dir data/ \
  --checkpoint_dir checkpoints/best/ \
  --output eval_results.json
```

Note: Qwen3-4B is not cached on the server — first run will download ~8GB. If bandwidth is slow, you could also use the cached Qwen3-8B (but needs more VRAM) or Qwen3-0.6B (faster but less capable).

---
