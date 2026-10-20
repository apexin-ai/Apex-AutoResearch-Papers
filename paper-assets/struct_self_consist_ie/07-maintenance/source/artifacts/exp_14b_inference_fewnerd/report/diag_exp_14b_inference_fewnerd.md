# Diagnosis: exp_14b_inference_fewnerd failure

**Date**: 2026-05-21
**Registered failure**: "process dead 5× with no sentinel/W&B — auto-resolved as failed"

## Root Cause: False positive — PID monitoring mismatch

**The inference is STILL RUNNING.** The cron monitor tracked PID 201001 (an intermediate process that exited after early phases), while the actual inference continued under new PIDs spawned by a surviving bash wrapper.

### Process tree (verified via /proc):
```
PID 200995 (bash, alive, sleeping)
  → PID 217692 (python, alive, sleeping)
    → PID 217960 (VLLM::EngineCore, State=R running, GPU 0: 31088/32607 MiB, 99% util)

PID 201001 (registered in spec): DEAD — No such process
PID 200993 (session leader): DEAD
```

### Current progress (from /tmp/14b_fewnerd.log):
- **Completed**: SciERC (all N∈{1,2,4,8,16}), CoNLL (all N), FewNERD N=1
- **In progress**: FewNERD N=2 — 24% (17870/75296 prompts), ~29 min elapsed, ETA ~2h
- Output dir: `/root/autodl-tmp/struct_self_consist_ie/output/14b_final_inference/`

## Earlier crash (separate run, /tmp/infer_14b_n1.log)

A previous attempt using `qwen25-14b-fewnerd-merged-ckpt36000` (not -final) crashed at 60% of fewnerd N=1:
- **Error**: `vllm.v1.engine.exceptions.EngineDeadError` — EngineCore died unexpectedly
- **Cause**: CUDA graph + torch.compile memory overhead on top of 27.57 GiB model → OOM
- **Fix applied in current run**: `enforce_eager=True` disables CUDA graphs, avoids OOM

## Key metrics from current run

| Resource | Value | Risk |
|----------|-------|------|
| Model VRAM | 27.57 GiB | HIGH — 84% of 32 GiB GPU |
| KV cache | 1.09 GiB (5,920 tokens) | CRITICAL — max 2.89 concurrent requests |
| Inference speed | ~10 it/s (fewnerd n=2) | SLOW due to KV cache bottleneck |

## Cross-domain results (SciERC/CoNLL are garbage)

Model fine-tuned only on FewNERD:
- SciERC: greedy_f1=0.004, 99% samples F1=0
- CoNLL: greedy_f1=0.046, 95% samples F1=0
- FewNERD: greedy_f1=0.798 ✓

## Recommendations

1. **Immediate**: Update registry — experiment is RUNNING, not failed
2. **Performance**: Use `--tensor_parallel 2` (2 GPUs) for 14B inference — frees ~28 GiB for KV cache
3. **Skip cross-domain**: SciERC/CoNLL outputs are useless for a FewNERD-only model
4. **Fix monitoring**: Track the main python PID (217692) or the bash wrapper PID (200995), not intermediate PIDs
