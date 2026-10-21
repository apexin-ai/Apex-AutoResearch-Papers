# pipeline openvla crm bjb2 28827

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_pipeline_openvla-crm-bjb2-28827_20260520T132403_result.json`
- **Structured JSON:** [`c8dba6e2d2a98b59245f.json`](../../sessions/c8/c8dba6e2d2a98b59245f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All tasks complete. Summary:

**Precompute job running on cuda:3** (`openvla-precompute-k1`, PID 365142):
- Processing 74,507 timesteps from 500 LIBERO-Object demos
- Output: `/root/autodl-tmp/crm_cache_k1_openvla/object/sample_XXXXXX.pt`
- Each sample: `multi_scale_obs (4,4096)`, `obs_features (4096)`, `vla_action (6)`, `expert_action (6)`, `task_name`
- ETA: ~10-14 hours
- Log: `~/runs/acr-vla-conformal-refinement/openvla-precompute-k1.log`

**After precompute finishes**, CRM training command for cuda:4:
```bash
python train_crm_k1.py --action_dim 6 --obs_dim 4096 \
  --cache_dir /root/autodl-tmp/crm_cache_k1_openvla/ \
  --output_dir /root/autodl-tmp/checkpoints/crm_k1_openvla/
```

---
