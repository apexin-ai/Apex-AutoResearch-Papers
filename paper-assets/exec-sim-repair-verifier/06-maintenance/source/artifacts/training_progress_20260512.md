# Training Progress Check — 2026-05-12

## repo-level-cwm-v6 (seetacloud cuda:2)
- Status: **running** (PID 84887)
- Current step: 166 / 6633 (2.5%)
- Latest train_loss: 11.1592 (step 150), down from 28.168 (step 50) → 16.348 (step 100)
- Latest eval_loss: 0.4332 (step 150), down from 0.6099 (step 100)
- Learning rate: 4.49e-05 (warmup phase)
- GPU util: 97%, VRAM: 22351/32607 MiB (68.6%)
- Elapsed: 1h 06m
- Training speed: ~8.0s/step, eval every 50 steps (~12.5 min/eval)
- ETA: ~42h (eval overhead dominates: 19.5 min per 50-step cycle)

## repo-level-cls-home (home cuda:0)
- Status: **running** (log last modified 13:24:11, file actively written)
- Current step: 1577 / 6633 (23.8%)
- Latest train_loss: N/A (training script does not log loss to stdout)
- GPU util: 92%, VRAM: 19465/32607 MiB (59.7%)
- Elapsed: 3h 06m (started 10:17:09)
- Training speed: ~7.1s/step
- ETA: ~10h

## Notes
- cwm-v6 runs eval on full val set (9335 samples) every 50 steps, which adds ~12.5 min overhead per eval. This makes total wall time ~42h despite only 6633 training steps.
- cls-home does not appear to run inline eval (no eval metrics in log), so it trains much faster per step. No loss visibility in current log — consider checking wandb or a separate metrics file.
- Both models: Qwen3-4B with LoRA (trainable 11.8M / 4.03B params, 0.29%).
- cls-home dataset: train=70748, val=9335, class weights fail=1.70/pass=0.30.
