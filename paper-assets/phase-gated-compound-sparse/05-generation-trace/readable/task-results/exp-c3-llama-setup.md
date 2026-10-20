# exp c3 llama setup

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_c3-llama-setup_20260514T133515_result.json`
- **Structured JSON:** [`476252676c5a02a8759f.json`](../../sessions/47/476252676c5a02a8759f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All C3 LLaMA validation tasks complete:

1. **Model download** — DeepSeek-R1-Distill-Llama-8B (15GB) downloaded via ModelScope at ~20 MB/s, copied to `/root/autodl-tmp/models/DeepSeek-R1-Distill-Llama-8B/`
2. **Symlink** — Created at `/root/autodl-tmp/pacs/checkpoints/DeepSeek-R1-Distill-Llama-8B`
3. **Model verify** — LlamaForCausalLM, 32L/32H/8KV, bf16, 16.1GB VRAM, generation works
4. **Dry-run PASS** — 3 problems, s=0.25 importance. Phase-modulated pattern confirmed:
   - low_sparsity II = +0.43
   - mid_sparsity II = +0.21  
   - high_sparsity II = +0.06
   - Verdict: PASS (CIs non-overlapping)
5. **Full experiment launched** — PID 137204 on `westd-22162`, 8 conditions (importance×4 + random×4), n=50 stratified, running on cuda:2 and cuda:3 alongside C2 Qwen n500
6. **Registry** — `c3_llama` status=RUNNING with full provenance

Server: `westd-22162` (4× RTX PRO 6000 Blackwell 98GB). The experiment shares GPUs 2&3 with C2 Qwen n500 but VRAM is ample (~75GB free per GPU).

---
