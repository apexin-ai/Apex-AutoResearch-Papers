# code exp70 deberta large scale

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp70_deberta_large_scale_20260523T235132_result.json`
- **Structured JSON:** [`8410ddc0f8258b3529de.json`](../../sessions/84/8410ddc0f8258b3529de.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**exp70_deberta_large_scale** is running successfully on westd-33183. Here's the summary:

**What's running:**
- tmux session `exp70` on cuda:0 (~16GB VRAM)
- Script: `scripts/exp70_deberta_large_scale.py` (adapted from exp15_roberta_large.py)
- Log: `logs/exp70_deberta_large_scale.log`

**Pipeline:**
1. **Stage 1 DAPT** — 3 seeds × 5 epochs of 9-class multitask training on DeBERTa-v3-large (currently on seed 42, epoch 2/5 done, val_acc=0.8388)
2. **Stage 2** — For each variant (vanilla + 9-class) × 3 seeds: train BiGRU classifier, evaluate DD OOD + AA OOD
3. Results saved to `results/rebuttal/deberta_large_scale/exp70_deberta_large_scale.json`

**Data:** Same as exp15 (plan_002_splits for train/val/test, generated/deceptive_delight_all.jsonl for DD, generated/actorattack_all.jsonl for AA)

**Registry:** `exp70_deberta_large_scale` set to RUNNING with hypothesis about scale effect vs architecture specificity.

**Estimated runtime:** ~3-5h total (Stage 1: ~1h per seed × 3 = 3h + Stage 2 + eval ~1-2h).

**Key issues resolved:**
- Server needs `source /etc/network_turbo` for HuggingFace access
- Set `HF_HUB_DISABLE_XET=1` for reliable downloads
- Set `TRANSFORMERS_OFFLINE=1` for runtime to avoid network hangs

---
