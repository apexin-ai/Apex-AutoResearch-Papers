# code a1 sdf decoder integration

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_a1_sdf_decoder_integration_20260519T203309_result.json`
- **Structured JSON:** [`c928097fc2df6f51cead.json`](../../sessions/c9/c928097fc2df6f51cead.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

A1 SDF Decoder integration complete. **37/37 verification checks passed** on cuda:3.

### Deployed files on server (`/root/colliforce-vla/`):

| File | Description |
|------|-------------|
| `colliforce/sdf_decoder.py` | 4-layer MLP (395K params), Softplus(β=5), skip@L2 |
| `colliforce/ee_extractor.py` | 2-layer MLP (263K params) → EE xyz |
| `scripts/train_a1_sdf_aux.py` | Full A1 training script with two-phase training |
| `scripts/verify_a1.py` | 37-check verification suite |
| `data/a1_integration_report.txt` | Verification report |

### Key findings during integration:
1. **No LoRA in PyTorch pi0** — all 3.5B params are full-rank; Phase 2 unfreezes everything
2. **action_dim=32** — pi0_base pads LIBERO's 7-dim actions/8-dim state to 32
3. **state[:,:3] = normalized EE position** — confirmed by cross-referencing with HDF5 ee_positions
4. **Peak memory: 62.93 GB** for B=2 end-to-end step (sufficient on 95GB GPU)

---
