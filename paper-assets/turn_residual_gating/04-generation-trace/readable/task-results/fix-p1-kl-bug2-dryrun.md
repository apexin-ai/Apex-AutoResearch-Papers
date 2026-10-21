# fix p1 kl bug2 dryrun

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_p1_kl_bug2_dryrun_20260524T065444_result.json`
- **Structured JSON:** [`5e65db495e4514182225.json`](../../sessions/5e/5e65db495e4514182225.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Process is running on GPU (PID 155327, 38GB VRAM, 77% GPU util). The Python output is just buffered since it's redirected to file. Dry-run took ~20s per conversation, so 30 conversations should take ~10 minutes.

**Summary of fixes:**
1. **`p1_kl_divergence.py` line 123-125**: `gate_values_ref[0].items()` → `gate_values_ref.items()`. The `register_gating_hooks` returns a dict `{layer_idx: tensor}`, not a list. Changed the check to `isinstance(gate_values_ref, dict) and len(gate_values_ref) > 0`.
2. **`threadgate.py` GateNetwork.forward**: Added seq_len alignment before `torch.cat`. During AR decode, hidden_state has `seq_len=1` but turn_features cover the full prompt. Added `turn_emb = turn_emb[:, -down.shape[-2]:, :]` to slice the last positions.

Full run is in progress (~10 min ETA). Check with `tail -20 /root/turn_residual_gating/logs/p1_kl_divergence_step2.log`.

---
