# infra westd49690 env setup

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_westd49690_env_setup_20260522T111328_result.json`
- **Structured JSON:** [`9d00e9b394a7dbf48136.json`](../../sessions/9d/9d00e9b394a7dbf48136.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Setup complete. Report:

### westd-49690 Environment Report

| Item | Status |
|------|--------|
| **GPUs** | 2× NVIDIA RTX PRO 6000 Blackwell Server Edition (94GB each) |
| **CUDA** | 12.8 (nvcc V12.8.93) |
| **Python** | 3.12.3 (conda base) |
| **PyTorch** | 2.8.0+cu128 |
| **Transformers** | 5.9.0 |
| **Other ML** | datasets 4.8.5, accelerate 1.13.0, wandb 0.27.0, sklearn 1.8.0, pandas 3.0.3, einops 0.8.2 |

**Project code**: Synced to `/root/persuasion_turn_jailbreak_detect/` (412MB — src/, data/, scripts/, paper/, docs/)

**Checkpoints**: All 33 checkpoints synced to `/root/autodl-tmp/persuasion_turn_jailbreak_detect/checkpoints_archive/` (15GB), including:
- plan_002 (9-class, 3 seeds), plan_017_mlm (MLM, 3 seeds), plan_018_wiki_mlm (3 seeds)
- exp1_roberta variants (9 checkpoints), mf1_binary (3 seeds)
- GRU checkpoints (subset_baseline, vanilla seeds)

**Disk**: root 29GB free, data disk 236GB free

**Config**: `.bashrc` configured with conda activation, `HF_HOME=/root/autodl-tmp/.hf_cache`, `HF_HUB_DISABLE_XET=1`

**No issues encountered.**

---
