# Diagnosis: exp029_per_task_t04_v2

**Date**: 2026-05-19  
**Status**: FALSE POSITIVE — eval completed successfully  

## What Happened

The cron monitor reported "process dead 5× with no sentinel/W&B — auto-resolved as failed." However, the eval script **ran all 134/134 OOD games to completion** and saved results to `/root/autodl-tmp/tmp/exp029_per_task_type_breakdown_t04.json` (49K, timestamped 22:58).

## Why Cron Flagged It as Failed

Two reasons, both false-positive triggers:

1. **Non-zero exit code from vLLM shutdown**: After all inference completed, vLLM v0.18.1 emitted `ERROR: Engine core proc EngineCore died unexpectedly` during process cleanup. This is a known vLLM v0.18.x shutdown race: the EngineCore subprocess receives SIGTERM before the client finishes graceful shutdown. The `destroy_process_group()` warning confirms this is cleanup-phase, not inference-phase.

2. **No sentinel file / W&B run**: The eval script (`eval_per_task_type.py`) is a standalone script that writes JSON output but doesn't create a sentinel file or W&B run that the cron monitor expects.

## Actual Results (T=0.4, 134 OOD games)

| Task Type | Count | Success | Rate |
|-----------|-------|---------|------|
| pick_and_place_simple | 24 | 4 | 16.7% |
| pick_clean_then_place_in_recep | 31 | 8 | 25.8% |
| pick_heat_then_place_in_recep | 23 | 4 | 17.4% |
| pick_cool_then_place_in_recep | 21 | 5 | 23.8% |
| look_at_obj_in_light | 18 | 5 | 27.8% |
| pick_two_obj_and_place | 17 | 0 | 0.0% |
| **Total** | **134** | **26** | **19.4%** |

## GPU State

Both GPUs (RTX PRO 6000, 96GB each) idle, 0MiB used, no residual processes. Clean.

## Recommendations

1. **No re-run needed** — results are complete and saved.
2. **Cron monitor fix**: For standalone eval scripts, either (a) write a sentinel file at script end, or (b) exempt eval runs from the "sentinel/W&B required" check.
3. **vLLM shutdown noise**: Suppress or ignore the EngineCore shutdown error. It's cosmetic and fixed in vLLM ≥0.19. Alternatively, add explicit `llm.shutdown()` before script exit.

## v1 vs v2

Both v1 and v2 wrote to the same log path (`exp029_per_task_t04.log`). The current log content corresponds to the v2 run (last modified 22:58). v1 was likely overwritten. Both runs likely completed but were flagged by the same false-positive mechanism.
